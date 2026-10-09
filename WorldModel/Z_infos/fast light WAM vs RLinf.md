---
tags:
  - papers/world-model
  - research/embodied-ai
  - research/systems
aliases:
  - Fast-WAM vs Light-WAM vs RLinf
  - WAM 算法与 RL 系统比较
created: 2026-07-29
---

# Fast-WAM、Light-WAM 与 RLinf：如何选择研究起点

## 结论先行

这三者不处于同一抽象层，不能简单按成功率或吞吐率横向排名：

- **Fast-WAM** 是研究 WAM 机制最干净的基线。它用训练期视频预测学习动态表征，但推理时删除未来视频生成，仅保留当前观测编码和迭代式动作生成。它适合回答“视频监督为什么有用”“显式未来想象是否必要”等问题。
- **Light-WAM** 是最快进入模型迭代的代码库。它缩小并冻结视频骨干，以 LoRA/adapter 适配，用多层状态融合和单次前向动作回归代替 10 步动作去噪。它适合做动作头、特征融合、时域监督和效率—性能帕累托研究。
- **RLinf** 是分布式强化学习运行时，而不是另一种 WAM。它优化 rollout、环境、推理、奖励和训练阶段如何放置、通信、流水化与复用 GPU。它适合研究“模型计算图 × 分布式执行计划”，不适合作为最快的 WAM 模型修改入口。

如果目标是**快速上手、改代码、完成一篇范围清楚的技术报告**，我的推荐顺序是：

1. 先在本机 **Light-WAM** 仓库复现 released-checkpoint 推理；
2. 做“**动作块监督权重与闭环重规划间隔匹配**”实验；
3. 若需要更强的机制论证，再在 **Fast-WAM** 上扫描动作去噪步数、视频损失权重或注意力信息流；
4. 只有当单机训练/评测吞吐成为明确瓶颈，或论文主张本身就是系统问题时，再把模型接入 **RLinf**。

不建议从“把 Fast-WAM/Light-WAM 移植进 RLinf”开始。RLinf 当前支持 DreamZero，但没有 Fast-WAM 或 Light-WAM；移植不是改一个配置，而是新增模型、数据、checkpoint、推理、训练和评测适配层。这个工作会推迟算法证据的获得。

---

## 1. 三者真正研究的是什么

| 维度 | Fast-WAM | Light-WAM | RLinf |
|---|---|---|---|
| 抽象层 | 模型与训练目标 | 模型、动作解码器与训练管线 | 分布式 RL 运行时 |
| 核心问题 | 测试时未来视频想象是否必要 | 如何低成本保留视频监督收益 | 如何把宏观 RL 工作流转换为高效微观执行流 |
| 视频监督 | 训练期全分辨率视频 flow matching | 训练期低分辨率视频辅助目标 | 由接入模型决定 |
| 在线未来视频 | Fast 基线删除；Joint/IDM 保留作对照 | 删除 | 框架不限定 |
| 动作生成 | 约 1B ActionDiT，10 步 flow matching | State-Fusion 直接回归，一次前向 | 由接入模型决定 |
| 主要优化单位 | 单次策略调用与因果信息流 | 参数、显存、训练吞吐、推理延迟 | 端到端 rollout/训练吞吐和资源利用率 |
| 最适合的论文类型 | 机制与因果消融 | 轻量架构与效率帕累托 | 系统、调度和模型—系统协同 |

最重要的边界是：**M2Flow 不会自动让一个 WAM 的动作预测更准确，也不会自动减少其模型 FLOPs。** 它重新安排组件放置、通信和时间重叠。相反，Fast-WAM 与 Light-WAM 改变的是模型计算和训练目标。若要比较系统收益，必须固定模型、硬件、环境并分别报告策略延迟与端到端吞吐。

---

## 2. Fast-WAM：机制最清楚，但完整训练最贵

### 2.1 方法与代码结构

Fast-WAM 使用：

- `Wan2.2-TI2V-5B` 视频 DiT；
- 约 1B 参数的 `ActionDiT`；
- `MoT` 混合 Transformer；
- 分离的视频与动作 flow-matching scheduler；
- 显式控制信息流的结构化 attention mask。

训练时，动作 token 只能访问当前第一帧视频 token 和动作 token，不能读取未来视频 token。因此，未来视频损失只能通过训练共享表征产生影响，而不能成为动作预测的 teacher-forcing 捷径。测试时先编码当前图像并预填充视频 K/V cache，再执行 10 步动作去噪，不生成未来视频。

官方代码中的主要修改面：

- `src/fastwam/models/wan22/fastwam.py`
  - `FastWAM._build_mot_attention_mask`
  - `FastWAM.training_loss`
  - `FastWAM._predict_action_noise_with_cache`
  - `FastWAM.infer_action`
- `src/fastwam/models/wan22/fastwam_joint.py`
- `src/fastwam/models/wan22/fastwam_idm.py`
- `src/fastwam/models/wan22/action_dit.py`
- `configs/model/fastwam*.yaml`
- `experiments/libero/` 与 `experiments/robotwin/`

官方仓库和资源：

- 代码：<https://github.com/yuantianyuan01/FastWAM>
- 项目页：<https://yuantianyuan01.github.io/FastWAM/>
- checkpoint：<https://huggingface.co/yuanty/fastwam>
- LIBERO 数据：<https://huggingface.co/datasets/yuanty/LIBERO-fastwam>
- RoboTwin 数据：<https://huggingface.co/datasets/yuanty/robotwin2.0-fastwam>

代码是可用的研究发布：有 Fast、Joint、IDM 三条训练/推理路径、checkpoint 恢复、LIBERO/RoboTwin manager、数据和基线 checkpoint。但没有 CI、单元测试、Docker、tagged release、Joint/IDM checkpoint 或完整真机资产。

### 2.2 优势

1. **机制控制最干净。** 同一框架内可以控制是否使用未来视频、动作是否可见未来 token、是否启用视频损失。
2. **动作生成能力更强。** 迭代式 ActionDiT 比直接 MSE 回归更能表达多模态动作，但代价更高。
3. **官方资产较完整。** 基线 LIBERO/RoboTwin checkpoint 和预处理数据已发布。
4. **适合做因果问题。** 例如视频共同训练究竟提供动态表征，还是只增加优化信号。

### 2.3 成本与风险

- 总规模约 6B；论文中的 LIBERO 训练为 8 GPU，RoboTwin 使用 64 GPU 加速。
- 报告的 190 ms 来自 RTX 5090D V2，不能和 Light-WAM 的 RTX 4090 数字直接相减。
- “一次前向”只适用于视频编码分支，动作仍有 10 次迭代。
- `negative_prompt`、`text_cfg_scale`、`action_cfg_scale` 等接口在所检查路径中似乎未改变核心计算，做实验前应写行为测试。
- IDM 中视频条件扰动概率 `0.5` 是硬编码值。
- 不同长度的视频/动作 scheduler 被 `zip` 组合时可能截断为较短者。
- LIBERO 接近饱和，平均成功率可能掩盖困难任务差异。

---

## 3. Light-WAM：最适合快速迭代的起点

### 3.1 方法与本机代码

本机仓库：

`/Users/roywangj/journey_wj/research/author/WAM/Light-WAM`

它以 Fast-WAM 数据和模拟器路径为基础，但做了三项关键简化：

1. 将视频骨干换为较小的 `Wan2.1-T2V-1.3B`，冻结主干，仅训练 LoRA/adapter；
2. 在多个中间层抽取适配后的视觉状态；
3. 通过 State-Fusion Action Expert 一次性回归动作块，不再运行 ActionDiT 多步去噪。

State-Fusion 的实际路径是：

1. 单帧观测经过视频专家；
2. 从指定层取得 `backbone`、`adapted` 和 `delta = adapted - backbone` 状态；
3. 每层用 learned queries 池化密集 token；
4. 压缩并拼接多层表征；
5. 加入动作 horizon 位置编码；
6. 一次前向输出 `[B, K, A]` 动作块。

最重要的代码入口：

- `src/lightwam/models/wan22/state_fusion_action_expert.py`
  - `LearnedQueryPooler`
  - `LayerFusionCompressor`
  - `StateFusionActionExpert`
- `src/lightwam/models/wan22/lightwam.py`
  - `_build_multilayer_action_fusion_inputs`
  - `_predict_state_fusion_action_from_observation`
  - `_training_loss_state_fusion`
  - `_build_action_temporal_weights`
  - `_compute_action_loss_per_sample`
  - `infer_action`
- `configs/model/lightwam.yaml`
- `scripts/train_libero_*.sh`
- `scripts/precompute_video_latents.py`
- `scripts/eval_libero.sh`

### 3.2 一个值得立即关注的实现细节

训练 launcher 默认没有均匀监督完整 32 步动作块：

- LIBERO 主要监督前 8 步；
- RoboTwin/真机主要监督前 24 步；
- 后部位置权重可为 0。

这意味着模型训练目标和闭环执行策略强耦合。若测试时实际执行的 `replan_steps` 与训练时有权重的动作前缀不一致，模型可能在“不会被执行”的尾部浪费容量，或者在“会被执行但训练权重不足”的位置积累误差。

这正是最适合快速技术报告的切口：改动集中、训练逻辑明确、机制可解释，并且同时影响成功率、动作误差和闭环延迟。

### 3.3 优势

- 本机已有代码，可直接修改，无移植成本。
- 总规模约 1.99B，约 0.44B 可训练，训练和消融明显便宜。
- 离线视频 latent/text cache 降低训练 I/O 和 VAE 成本。
- StateFusion head 的 query 数、层来源、融合维度和 temporal weighting 都是局部可改参数。
- 报告 72.03 ms、4.1 GiB 和较高训练吞吐，适合构建效率—性能曲线。

### 3.4 局限

- RoboTwin 平均成功率约 76.4，明显低于 Fast-WAM 的约 91.9；不能把它称为严格优于 Fast-WAM。
- Fast/Light 同时改变了骨干版本、模型容量、全量训练/adapter、视频目标分辨率、动作解码器和缓存管线，二者结果不能直接归因于“flow 对比回归”。
- 直接 MSE 动作头可能在多模态、接触敏感和双臂协同任务上平均化动作。
- 本机目前没有确认已安装所有数据、checkpoint 和模拟器资产；应先做环境与 checkpoint smoke test，而不是直接发起完整训练。

---

## 4. RLinf：成熟的系统平台，但不是快速改 WAM 的捷径

### 4.1 M2Flow 在代码中如何落地

检查版本：RLinf `0.3.0`，HEAD `e7609d4c9e2f33c5ffc10b67c61c8e4b73208b45`，Apache-2.0。

论文把设计称为 Macro-to-Micro Flow Transformation，但当前仓库没有一个单体 `M2Flow` 类。能力分布在多个模块中：

- `rlinf/scheduler/worker/worker.py`：Ray remote process、设备/端口锁、`send`/`recv`、collective；
- `rlinf/scheduler/worker/worker_group.py`：placement 后的 actor group 与异步组调用；
- `rlinf/scheduler/channel/channel.py`：带 key/weight 的同步或异步数据通道；
- `rlinf/scheduler/manager/lock_manager.py`：全局 device lock；
- rollout、Megatron worker 和 model manager：模型 offload/reload 与资源复用；
- `toolkits/auto_placement/`：基于 profile 拟合和工作流 cut 的静态计划搜索；
- `rlinf/scheduler/dynamic_scheduler/`：面向 rollout/inference/actor 的在线迁移和扩容；
- `rlinf/runners/embodied_runner.py`：环境、rollout、actor、reward 的 channel 和训练流水线。

RLinf 的优势是支持范围广、Docker/installer/documentation/CI 较完整，并已有 DreamZero、LIBERO、RoboTwin、ManiSkill 等路径。论文报告的 1.07–2.43× 端到端吞吐来自选定的 H100 规模工作负载；这些收益包含 engine、KV cache、环境、通信和实现差异，不能解读成纯调度算法对任意模型的保证。

### 4.2 为什么 Fast-WAM 不能配置式接入

RLinf 有 DreamZero，但没有 Fast-WAM/Light-WAM。最低限度需要：

1. 包装 `training_loss`、`infer_action`、checkpoint load/save；
2. 适配 33 帧窗口、32 步动作、多相机 canvas 和 normalization stats；
3. 表达 5B 视频专家 + 1B ActionDiT/MoT 配置；
4. 处理 K/V prefill 与动作迭代采样；
5. 添加安装依赖、LIBERO evaluation adapter；
6. 增加最小 SFT/evaluation e2e test；
7. 核验 FSDP/ZeRO 与 checkpoint schema 的兼容性。

Light-WAM 同样需要独立 model wrapper、离线 latent cache 路径和 StateFusion action interface。若研究问题只是 temporal weighting 或 action head，先做这些适配会让系统工程压过算法实验。

### 4.3 什么时候应该选择 RLinf

满足以下至少一项时，RLinf 才是合适起点：

- 论文问题是 placement、pipeline、通信、tail latency 或 GPU 利用率；
- 需要在线 RL，而不是只做监督微调与固定 checkpoint 评测；
- 单机模型结论已经成立，下一步要测分布式训练/rollout 的真实收益；
- 已有 4–8 GPU 甚至多节点资源，并能稳定复现环境资产；
- 愿意把模型适配本身作为可复用工程贡献。

---

## 5. 上手与实验路线

## 阶段 0：先建立可相信的基线

### Light-WAM 环境

建议在 Linux/CUDA 机器上建立独立环境：

```bash
conda create -n lightwam python=3.10 -y
conda activate lightwam
pip install torch==2.7.1+cu128 torchvision==0.22.1+cu128 \
  --extra-index-url https://download.pytorch.org/whl/cu128
pip install -e .
```

下载对应 Wan 骨干后，先运行 released checkpoint 的 LIBERO 评测。注意 `scripts/eval_libero.sh` 的轻量默认值可能只有 5 trials；调试可用 5 次，但正式报告至少应固定为 50 次并给出逐任务结果。

基线核验必须记录：

- Git commit 与配置快照；
- GPU、CUDA、PyTorch、MuJoCo 版本；
- checkpoint 与 normalization stats；
- 相机 canvas、action horizon、replan steps；
- 模型延迟与包含环境渲染的端到端延迟；
- 每任务成功次数，而不只报告平均值；
- 固定 seed 是否真正传入每次环境 reset。

### Fast-WAM 零训练基线

最低成本实验可以直接使用 released LIBERO checkpoint：

```bash
huggingface-cli download yuanty/fastwam \
  libero_uncond_2cam224.pt \
  libero_uncond_2cam224_dataset_stats.json \
  --local-dir ./checkpoints/fastwam_release
```

然后在少量任务上扫描动作去噪步数和重规划长度。先不训练即可得到完整的速度—成功率曲线。

---

## 6. 最推荐的短技术报告

# Replan-Aligned Temporal Supervision for Direct WAM Action Decoding

### 6.1 研究问题

Light-WAM 用一个动作块损失训练直接解码器，但闭环控制只执行该块的一部分后就重新观测。问题是：

> 动作监督权重是否应该与实际重规划长度一致？在相同模型和推理成本下，合理的时域权重能否提高闭环成功率，尤其是长时程和接触敏感任务？

该问题比单纯“换一个 loss”更有价值，因为它连接了训练目标、动作块语义和闭环执行策略。

### 6.2 最小实验矩阵

固定骨干、adapter、StateFusion head、数据、训练步数和随机种子，只修改 temporal weights：

| 组别 | 动作位置权重 | 目的 |
|---|---|---|
| Uniform | 32 步全为 1 | 测完整轨迹监督 |
| Hard prefix | 前 `R` 步为 1，其余为 0 | 复现当前思路 |
| Linear decay | 前部高、尾部线性下降 | 减少硬边界 |
| Exponential | $w_t=\exp(-t/\tau)$ | 平滑强调近期动作 |
| Two-stage | 前 `R` 步为 1，尾部为小权重 $\epsilon$ | 保留长期结构但聚焦可执行前缀 |

其中 `R` 必须与评测的 `replan_steps` 联合扫描，例如：

- `R ∈ {4, 8, 16}`；
- 每种模型分别用执行长度 `{4, 8, 16}` 评测；
- 核心结果是一个“训练监督长度 × 执行长度”矩阵，而不是只比较一个平均值。

### 6.3 指标

至少报告：

1. LIBERO-Spatial 逐任务成功率与 macro average；
2. 若资源允许，增加 LIBERO-10 中较难任务；
3. 各动作位置的归一化 L1/L2 error；
4. episode 中首次明显偏离或失败的时间；
5. policy-only latency、端到端环境 step time、peak GPU memory；
6. 动作平滑度、gripper 状态错误、累计漂移；
7. 三个 seed，或明确说明只有单 seed 并避免统计显著性表述。

### 6.4 成功标准与失败标准

有报告价值的结果不一定要求整体成功率大幅提升。以下任一结果都可形成可信技术报告：

- matched supervision 在相同延迟下稳定提高困难任务成功率；
- soft tail 比 hard cutoff 更稳，说明尾部预测仍提供轨迹正则化；
- 最佳训练 `R` 不等于执行 `R`，揭示表征学习和闭环控制目标不一致；
- uniform 在离线动作误差更低但闭环成功率更差，说明离线指标不能代表闭环控制；
- 所有策略无显著差异，也可作为“当前模型瓶颈不在时域权重”的负结果，但需确认训练量与 seed 足够。

### 6.5 必要消融

- 保持总权重和归一化方式一致，避免某组只是梯度尺度更大；
- 记录前缀/尾部的 loss，而非仅记录总 loss；
- 固定数据窗口、action normalization、augmentation；
- 至少检查 query 数或 StateFusion 宽度不改变主要结论；
- 将执行长度变化带来的控制频率/延迟变化单独列出；
- 区分 checkpoint selection 使用的验证指标，避免测试集选择偏差。

---

## 7. 第二优先级：Fast-WAM 零训练报告

若希望更快，不训练模型，直接研究：

# How Many Action Denoising Steps Does Fast-WAM Need?

扫描：

- action denoising steps：`{2, 4, 6, 8, 10}`；
- replanning steps：`{4, 8, 16}`；
- 固定 checkpoint、任务、seed 和硬件。

报告成功率、策略延迟、端到端控制频率、peak memory、动作相对 10-step 参考轨迹的偏差，以及 grasp/placement/gripper/drift 失败类型。

该实验成本最低，但创新性也较弱。要避免只在饱和的 LIBERO 平均分上得出“4 步足够”的结论；应增加困难任务、逐任务结果，并把求解器步数与闭环重规划的交互作为主线。

---

## 8. 更强但更贵的后续方向

### 8.1 视频共同训练权重

扫描：

$$
\lambda_{\text{video}}\in\{0,0.1,0.3,1,3\}.
$$

固定 action loss、初始化、数据和 optimizer steps，测成功率、video PSNR/SSIM、动作误差、不同层的梯度 norm。重点判断视频预测究竟提供动态语义，还是主要改变了共享骨干的梯度尺度。

### 8.2 真实历史对比想象未来

比较当前单帧、2/4 帧真实历史 cache、Fast-WAM Joint imagined future、IDM future。这个问题比简单恢复未来视频更有意义：闭环机器人可以获得新的真实观测，真实历史可能比昂贵且有误差的想象未来更有效。

### 8.3 直接动作头与 flow head 的受控比较

应在相同 backbone、视频损失、输入表征和尽量接近的 action-head capacity 下比较：

- StateFusion direct decoder；
- 小型 flow action decoder；
- 原始 1B ActionDiT；
- direct + gated refinement。

不要直接用现成 Fast-WAM 与 Light-WAM 数字宣称“直接回归导致 RoboTwin 差距”，因为骨干和训练管线也不同。

### 8.4 RLinf 系统方向

若转向系统论文，最好的低成本入口不是完整移植 WAM，而是 **tail-aware placement calibration**：

- 修改 `toolkits/auto_placement/fitter.py` 和 `_find_schedule` 代价模型；
- 比较 mean、p50、p90、p95 stage cost；
- 指标为预测误差、selected-plan regret、p95/p99 iteration time、idle fraction 与吞吐；
- 先用记录的 stage-latency replay，再上 1–8 GPU。

这比“把模型接进去然后报告更快”更有独立系统贡献，也更容易明确因果变量。

---

## 9. 建议的四周执行计划

### 第 1 周：可重复基线

- 固定 Light-WAM commit、环境和数据版本；
- 下载 checkpoint/normalization stats；
- 通过单 episode、5 trials、50 trials 三层 smoke test；
- 保存逐任务结果、日志、视频和 latency breakdown；
- 写脚本验证 temporal weight 向量、loss normalization 与 replan config。

### 第 2 周：最小训练矩阵

- 先训练 `Uniform`、当前 `Hard prefix`、一个 `Two-stage`；
- 用一个任务/小套件做 early rejection；
- 确认 loss、梯度、吞吐和 checkpoint 可恢复；
- 只把机制成立的配置扩展到完整 LIBERO-Spatial。

### 第 3 周：完整评测与消融

- 完成监督长度 × 执行长度矩阵；
- 增加 3 seeds 或至少多个 evaluation seeds；
- 加入困难任务与失败类型；
- 核查结果是否仅来自梯度总量或 checkpoint selection。

### 第 4 周：报告与边界

- 主表：成功率、延迟、显存；
- 主图：训练监督长度 × 执行长度 heatmap；
- 辅图：动作位置误差与失败时间；
- 写清负结果、硬件口径和跨论文不可比项；
- 如果改进只在低难度任务出现，不扩大到“解决 WAM 长时程控制”。

---

## 10. 技术报告结构

1. **Introduction**：直接动作块预测快，但训练损失通常忽略闭环只执行前缀这一事实。
2. **Background**：Fast-WAM 的视频共同训练与迭代动作生成；Light-WAM 的 StateFusion direct decoder；RLinf 仅作为系统背景，不混入模型贡献。
3. **Method**：定义动作时域权重 $w_t$，说明 loss normalization 与 replan policy。
4. **Experimental Setup**：数据、任务、相机、horizon、replan、硬件、checkpoint、seed。
5. **Main Results**：监督长度 × 执行长度矩阵，逐任务成功率。
6. **Analysis**：动作位置误差、失败类型、控制频率、效率—成功率帕累托。
7. **Ablations**：hard/soft tail、权重总量、query capacity、困难任务。
8. **Limitations**：单 benchmark、训练资源、真实机器人缺失、直接回归多模态限制。
9. **Conclusion**：只陈述数据实际支持的闭环监督结论。

---

## 11. 最终选择建议

### 只有 1–2 张 GPU，目标是尽快出结果

选 **Light-WAM**。先做 released-checkpoint 评测，再做 temporal weighting。不要先接 RLinf。

### 有 4–8 张 GPU，目标是机制性更强

先做 **Light-WAM temporal supervision**；随后在 **Fast-WAM** 做 denoising/replanning 或视频损失权重验证。两套代码中的结果分开表述，不做未经控制的归因。

### 有多节点 GPU，目标是系统论文

选 **RLinf**，研究 placement、tail latency、packed trajectory/channel 或 WAM 计算图与 pipeline 的交互。先用 DreamZero 或小模型验证系统方法，再决定是否移植 Fast/Light-WAM。

### 目标是真机或 RoboTwin 高成功率

优先从 **Fast-WAM** 开始，因为 Light-WAM 当前是效率帕累托点而非准确率优势点；但必须接受更高训练成本和较弱的真机复现资产。

我的最终建议是：**第一篇短报告用 Light-WAM 做“重规划对齐的动作时域监督”；第二阶段用 Fast-WAM 做迭代动作头与视频共同训练的机制对照；RLinf 留到算法结论稳定后，作为系统扩展，而不是起点。**

---

## 12. LIBERO 评测脚本与 headless 渲染后端

### 12.1 总结

三个仓库的 LIBERO 测试脚本**并不一致**。Fast-WAM 与 Light-WAM 的底层单环境适配高度同源，但上层调度、默认 trial 数和渲染后端不同；RLinf 则使用统一的 embodied runner、Ray worker 和大规模向量环境，属于另一套评测架构。

| 仓库 | 默认入口 | 并发方式 | 默认 trials / 规模 | 默认 OpenGL 后端 | EGL 风险 |
|---|---|---|---|---|---|
| Fast-WAM | `run_libero_manager.py` | Hydra manager → tmux → 每任务独立 Python 进程 | 每任务 50；默认 8 GPU、每卡最多 2 个任务 | 仓库未显式设置 | 可能落入 EGL、GLFW 或系统默认并报 context 错误 |
| Light-WAM | `scripts/eval_libero.sh` | Bash 顺序遍历 suite/task；单进程单环境 | wrapper 默认 5，config 为 50 | `egl` | 三者中最直接暴露于 EGL 初始化问题 |
| RLinf | `evaluations/run_eval.sh` | runner / Ray worker → `ReconfigureSubprocEnv` → `spawn` 子进程 | config 常为 120、128 或 500 个总评测环境 | `osmesa` | 正常入口不主动走 EGL，但可能遇到 OSMesa 缺库或软件渲染瓶颈 |

`OffScreenRenderEnv` 只表示不创建可见窗口，不负责自动选择可用的 OpenGL backend。真正决定渲染路径的是：

```bash
MUJOCO_GL
PYOPENGL_PLATFORM
```

因此，“都使用 `OffScreenRenderEnv`”并不等于“都以相同方式 headless 渲染”。

### 12.2 Fast-WAM 的评测调用链

官方入口是：

```bash
python experiments/libero/run_libero_manager.py \
  task=libero_uncond_2cam224_1e-4 \
  ckpt=./checkpoints/fastwam_release/libero_uncond_2cam224.pt \
  EVALUATION.dataset_stats_path=./checkpoints/fastwam_release/libero_uncond_2cam224_dataset_stats.json \
  MULTIRUN.num_gpus=8
```

完整调用链为：

```text
run_libero_manager.py
  → 生成四个 suite 的 task 列表
  → run_libero_parallel_test.sh
  → tmux pane 按 GPU 分配任务
  → eval_libero_single.py
  → get_libero_env()
  → OffScreenRenderEnv
```

`configs/sim_libero.yaml` 默认设置：

- `num_trials: 50`；
- `env_num: 1`；
- `num_steps_wait: 30`；
- `replan_steps: 10`；
- `MULTIRUN.num_gpus: 8`；
- `MULTIRUN.max_tasks_per_gpu: 2`。

因此它不是一个 Python 进程内创建大量 vector env，而是每个 suite/task 启动独立 Python 进程，每个进程默认只有一个 `OffScreenRenderEnv`，再由 tmux 调度多个任务进程到 GPU。

Fast-WAM 的 `experiments/libero/libero_utils.py` 在 `env_num=1` 时直接执行：

```python
env = OffScreenRenderEnv(**env_args)
```

在 `env_num>1` 时才使用 `SubprocVectorEnv`。但当前单任务评测默认固定为 `env_num=1`。

#### Fast-WAM 的后端隐患

所检查的官方 LIBERO manager、parallel shell、worker 和配置中没有显式设置：

```bash
export MUJOCO_GL=...
export PYOPENGL_PLATFORM=...
```

所以它将后端选择交给用户 shell、MuJoCo/PyOpenGL 默认值和服务器环境。在无显示器节点上，可能出现：

- `EGL_NOT_INITIALIZED`；
- `Cannot initialize a EGL device display`；
- `Failed to create an OpenGL context`；
- `GLFWError: The DISPLAY environment variable is missing`。

它不一定总是“EGL 报错”，因为未强制 EGL 时也可能先走 GLFW/X11 并报 `DISPLAY` 错。

另外，Fast-WAM 通过 tmux 启动 worker。若复用旧 tmux server，pane 可能没有继承当前 shell 刚设置的变量。正式评测前应在 pane 内确认：

```bash
tmux show-environment MUJOCO_GL
tmux show-environment PYOPENGL_PLATFORM
```

### 12.3 Light-WAM 的评测调用链

官方入口是：

```bash
CKPT=/path/to/checkpoint.pt bash scripts/eval_libero.sh
```

脚本依次遍历：

```text
libero_10
libero_goal
libero_spatial
libero_object
```

以及每个 suite 的任务 `0–9`，逐个运行：

```bash
python experiments/libero/eval_libero_single.py
```

Light-WAM 的 `libero_utils.py` 与 Fast-WAM 几乎完全相同：均从 BDDL 创建 `OffScreenRenderEnv`，读取 agent-view 与 wrist camera，并按相同方式 seed 环境。可见 Light-WAM 复用了 Fast-WAM 的 LIBERO 单环境适配层。

但是二者的上层评测并不相同：

- Fast-WAM 使用 Hydra manager 和 tmux 多 GPU 调度；
- Light-WAM wrapper 默认单 GPU、顺序执行；
- Light-WAM `eval_libero_single.py` 明确只支持 `env_num=1`；
- Light-WAM shell 默认 `NUM_TRIALS=5`，而 `configs/sim_libero.yaml` 为 50。

所以直接运行 Light-WAM wrapper 只是 smoke test。论文级评测应显式设置：

```bash
NUM_TRIALS=50 \
CKPT=/path/to/checkpoint.pt \
bash scripts/eval_libero.sh
```

#### Light-WAM 默认强制 EGL

当前官方 `scripts/eval_libero.sh` 在首次导入 LIBERO 之前执行：

```bash
export MUJOCO_GL="${MUJOCO_GL:-egl}"
export PYOPENGL_PLATFORM="${PYOPENGL_PLATFORM:-egl}"
```

随后才执行 `python -c "import libero"`。设置时序是正确的，但默认值意味着它最直接依赖 NVIDIA EGL、`libEGL.so`、容器设备映射和驱动一致性。

若 headless 服务器 EGL 不稳定，可以不改代码，直接覆盖：

```bash
MUJOCO_GL=osmesa \
PYOPENGL_PLATFORM=osmesa \
NUM_TRIALS=5 \
CKPT=/path/to/checkpoint.pt \
bash scripts/eval_libero.sh
```

稳定后再将 `NUM_TRIALS` 提升到 50。

### 12.4 RLinf 的评测调用链

RLinf 使用统一入口：

```bash
bash evaluations/run_eval.sh \
  libero \
  libero_spatial_openpi_pi05_eval \
  rollout.model.model_path=/path/to/model
```

调用链为：

```text
evaluations/run_eval.sh
  → evaluations/eval_embodied_agent.py
  → RLinf runner / worker / placement
  → LiberoEnv
  → ReconfigureSubprocEnv
  → multiprocessing spawn workers
  → OffScreenRenderEnv
```

这与 Fast/Light-WAM 的 task-by-task shell 调度不同。`LiberoEnv` 总是将 env functions 交给 `ReconfigureSubprocEnv`，而 `ReconfigureSubprocEnvWorker` 使用：

```python
ctx = multiprocessing.get_context("spawn")
```

每个子进程再创建 `OffScreenRenderEnv`。RLinf 的配置表达的是大规模评测环境总量，例如：

- OpenPI/OpenVLA-OFT 多个配置为 `total_num_envs: 500`；
- DreamZero spatial 为 128；
- StarVLA spatial 为 120。

这些环境还会由 RLinf 的 worker/placement 分配，不等同于 Fast-WAM 的“8 GPU × 每卡两个独立 task process”。

#### RLinf 文档与代码一致：默认 OSMesa

`evaluations/run_eval.sh` 的 `setup_sim_env()` 明确设置：

```bash
export MUJOCO_GL="${MUJOCO_GL:-osmesa}"
export PYOPENGL_PLATFORM="${PYOPENGL_PLATFORM:-osmesa}"
```

对所有非 real-world benchmark，脚本会在启动 Python 之前调用 `setup_sim_env`。因此 RLinf 中文文档中“`run_eval.sh` 默认已设置 OSMesa”的描述与当前代码一致。

正常通过 wrapper 启动且没有预先覆盖变量时，RLinf 不会主动进入 EGL，所以典型 EGL 初始化错误的概率较低。但仍有三种例外：

1. 用户已提前设置 `MUJOCO_GL=egl`；`${VAR:-osmesa}` 不会覆盖已有值；
2. 绕过 `run_eval.sh`，直接运行 `eval_embodied_agent.py`；
3. Ray 已在设置 OSMesa 之前启动，远端 worker 没有继承新环境变量。

多节点时，应在每个节点执行 `ray start` 之前设置：

```bash
export MUJOCO_GL=osmesa
export PYOPENGL_PLATFORM=osmesa
```

OSMesa 也不是无代价方案。它依赖 Mesa/OSMesa library，并通常由 CPU 软件渲染。在 RLinf 的 120–500 环境评测中，可能出现：

- `OSMesa` library not found；
- Mesa renderer 初始化失败；
- CPU 利用率和内存压力过高；
- 软件渲染成为整体吞吐瓶颈。

### 12.5 三者是否会“都遇到 EGL 报错”

严格结论是：**不会以相同方式、相同概率遇到。**

- **Light-WAM：会直接尝试 EGL。** 如果驱动、容器或 `libEGL` 不正确，最容易得到明确 EGL 错误。
- **Fast-WAM：未指定后端。** 在 headless 环境同样可能失败，但具体表现取决于环境，既可能是 EGL，也可能是 GLFW/X11/`DISPLAY` 错误。
- **RLinf：正常 wrapper 默认 OSMesa。** 通常不会进入 EGL；更可能遇到 OSMesa 缺库或 CPU 软件渲染性能问题。

常见 EGL 失败原因包括：

- NVIDIA driver 与用户态 EGL library 不一致；
- 容器未正确暴露 GPU、`/dev/dri` 或 graphics capability；
- Mesa 和 NVIDIA 的 `libEGL`/PyOpenGL 混装；
- 同一 GPU 上并发建立过多 context；
- OpenGL backend 在导入 MuJoCo/PyOpenGL 后才设置；
- tmux 或 Ray worker 未继承当前 shell 环境。

### 12.6 推荐的排查和启动顺序

#### Fast-WAM

先使用单 GPU、单任务并显式指定 OSMesa：

```bash
export MUJOCO_GL=osmesa
export PYOPENGL_PLATFORM=osmesa

python experiments/libero/run_libero_manager.py \
  task=libero_uncond_2cam224_1e-4 \
  ckpt=/path/to/checkpoint.pt \
  MULTIRUN.num_gpus=1 \
  MULTIRUN.max_tasks_per_gpu=1
```

Fast-WAM manager 默认仍会生成完整任务列表；若只做渲染诊断，最好直接调用 `eval_libero_single.py` 并指定单个 suite/task 和少量 trials，避免一开始引入 tmux 调度变量。

#### Light-WAM

```bash
MUJOCO_GL=osmesa \
PYOPENGL_PLATFORM=osmesa \
NUM_TRIALS=5 \
TASK_SUITES=libero_spatial \
TASK_ORDERS=0 \
CKPT=/path/to/checkpoint.pt \
bash scripts/eval_libero.sh
```

确认单任务通过后，再扩展到 50 trials 和全部 suites。

#### RLinf

通过官方 wrapper 启动，并先降低并行环境数：

```bash
bash evaluations/run_eval.sh \
  libero \
  libero_spatial_openpi_pi05_eval \
  rollout.model.model_path=/path/to/model \
  env.eval.total_num_envs=8
```

不要在第一次诊断时直接使用 128 或 500 个环境。如果需要 EGL 加速，应先单独验证单 env EGL smoke test，再运行：

```bash
MUJOCO_GL=egl \
PYOPENGL_PLATFORM=egl \
bash evaluations/run_eval.sh ...
```

### 12.7 公平比较必须统一的评测变量

如果后续要比较 Fast-WAM、Light-WAM 和 RLinf 中某个 policy，至少应统一：

- `MUJOCO_GL` 与 `PYOPENGL_PLATFORM`；
- MuJoCo、robosuite、LIBERO commit/version；
- suite、task 和 initial-state IDs；
- 每任务 trials；
- action horizon、replan steps、action chunk；
- 环境并发数和每 GPU 任务数；
- 是否保存视频；
- policy-only latency 与包含环境渲染的端到端 latency；
- seed 的设置位置及子进程继承；
- 成功率按逐任务 macro average 还是按所有 episode micro average 汇总。

否则，渲染后端和并发模式本身就足以改变端到端吞吐，不能把差异归因于 WAM 模型。

---

## 13. 证据与可复现性边界

- Fast-WAM 官方代码检查基于 `45d8e1458921d83f8ad6cf9ce993d371208dabd0`；未在本机执行训练或模拟器。
- LIBERO 脚本补充核查于 2026-07-29 对三个官方仓库当前默认分支进行；结论来自静态代码路径，未实际初始化 EGL/OSMesa context。
- RLinf 检查基于本地只读快照 `e7609d4c9e2f33c5ffc10b67c61c8e4b73208b45`；未运行其 H100 规模 benchmark。
- Light-WAM 本机仓库检查基于 `a09a24bc883a577aee124789af9a277fd0c78099`；没有修改仓库中现有文件。
- 三篇论文使用不同 GPU、分辨率、模型规模、缓存策略、动作 solver、控制协议和环境设置；原始延迟与吞吐数字不可直接横比。
- Fast-WAM checkpoint 仓库没有独立明确的权重许可证；源代码 MIT 不应自动推断为模型权重许可证。
- RLinf 的 auto-placement 使用特定 workflow template，dynamic scheduler 也主要面向 rollout/inference/actor；不能把论文中的通用描述等同于任意 DAG 的在线最优调度保证。
- 本文建议是基于代码和论文的静态审阅，不替代实际环境安装、显存 profiling、seed 核验和 checkpoint 复现。

## 参考入口

- [Fast-WAM code](https://github.com/yuantianyuan01/FastWAM)
- [Fast-WAM paper](https://arxiv.org/abs/2603.16666)
- [Light-WAM code](https://github.com/L1ziang/Light-WAM)
- [Light-WAM paper](https://arxiv.org/abs/2606.08242)
- [RLinf code](https://github.com/RLinf/RLinf)
- [RLinf paper note](RLinf%20Flexible%20and%20Efficient%20Large-scale%20Reinforcement%20Learning%20via%20Macro-to-Micro%20Flow%20Transformation/paper_DeepPaperNote.md)
- [Fast-WAM local note](Fast-WAM%20Do%20World%20Action%20Models%20Need%20Test-time%20Future%20Imagination/paper_DeepPaperNote.md)
- [Light-WAM local note](Light-WAM%20Efficient%20World%20Action%20Models%20with%20State-Fusion%20Action%20Decoding/paper_DeepPaperNote.md)
