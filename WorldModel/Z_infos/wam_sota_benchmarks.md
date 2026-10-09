---
tags:
  - papers/WorldModel
  - WAM
  - benchmark
  - open-source
  - sota-survey
aliases:
  - WAM SOTA 与共性 Benchmark 调研
  - wam_sota_benchmarks
date: 2026-07-20
status: living-survey
last_verified: 2026-07-20
last_audit: 2026-07-20-codex-gpt5.6-sol-xhigh
bwm_added: 2026-07-20
---

# WAM 最新论文、共性 Benchmark 与开源 SOTA 基座调研

> **目的**：为「基于共性 benchmark + 最强开源 SOTA 方法开发」做独立调研台账。  
> **原则**：优先实访仓库/HF/arXiv；旧笔记仅作线索；**Codex 审查作批评源，不盲从**（见 §0.5）。  
> **范围**：World Action Model（WAM / VAM：联合或级联预测未来世界状态 + 动作）。  
> **旁支**：动作条件 **视频世界模型 / 数据引擎 / 仿真器**（如 BWM）单独成轨，**不与策略 WAM 混排成功率**。  
> **约束**：本文只维护本文件；不修改 `paper_insight.md` 等其余内容。

### 术语硬区分（全文适用）

| 标签 | 含义 | 能推出什么 |
|---|---|---|
| **论文表 SOTA** | 作者论文/README 自报数字 | 仅上界参考；**不能**当复现承诺 |
| **作者可运行** | 官方 ckpt + eval 脚本可跑 | 可对照，不保证你能训出同分 |
| **可训练开源** | 训练代码 + 权重/初始化 + 数据路径齐全 | 适合当开发脚手架 |
| **协议对齐可复现** | 同 instruction split / seed / 相机 / 数据版本下第三方复现 | 本文**无方法达到**；一律不宣称 |
| **4×H100 原生验证** | 官方脚本默认/文档写明 4 GPU 训练 | 目前主要 **Light-WAM** 明确 `GPU_IDS=0,1,2,3` |
| **4×H100 可缩放（未验证）** | 可用 grad accum / 减 batch 尝试 | **不**等于能复现论文分 |
| **公开可下载权重** | HF/ModelScope 能下 ckpt | **≠** 权重许可明确；**≠** 与竞赛提交同权重 |
| **仓内有 train.py** | 存在训练入口文件 | **≠** 对应发布模型的「可训练开源」；需数据配方+超参+与 ckpt 同骨干配置 |

---

## 0. 执行摘要（可直接用于选型）

### 0.1 一句话

**2025 末–2026 中，WAM 已成主流：骨干多收敛到 Wan / Cosmos；评测共性收敛到 LIBERO + RoboTwin 2.0。已有足够「可训练开源」候选支撑开发，但除少数轻量配方外，论文级 4×H100 复现大多未验证；数字应读作作者报告，不是第三方可复现 SOTA。**

### 0.2 必修正的旧结论（相对 `paper_insight.md`）

| # | 旧结论 | 本次核验 | 新立场 |
|---|---|---|---|
| **1–2** | R5：优先评估 **BiWM** 当训练平台 | arXiv **2606.10135 撤稿**（作者：可视化配置错误，影响视觉对比可靠性）；**无模型权重**；代码仍在 `LynnReal-AI/BiWM`（可训） | **降级**：可参考脚手架/损失想法；**不可**当学术可信基座。**注意**：撤稿不等于「方法设计已证伪」，只是论文主张暂不可引用为证据 |
| **3** | LaWAM「无代码无权重」，可复现 1.5 | **实访推翻**：`RLinf/LaWAM` + HF 权重/数据齐全 | **工程可复现 ≥ 4**；升为潜空间对照。但 **无根 LICENSE**；RoboTwin 数据若派生自 NC 数据则有再许可风险 → **legal hold**，不做「可随便再分发」判断 |

### 0.3 分轨候选（取代单一 T1-A…E 线性排名）

> 拒绝把「论文高分 / 社区 star / 4GPU 友好」压成一条序。开发决策按**用途分轨**。

#### Track A — 4×H100 策略脚手架（先跑通 / 缩小配方）

> 标题不再写「原生」一锅炖：拆成 **A1 论文明确 4×H100** vs **A2 可缩到 4 卡但论文分未验证**。细节对照见 **§0.6**。

| 子轨 | 方法 | 训练 / 算力证据 | 共性 bench（作者报告） | 代码/权重 | 判断 |
|---|---|---|---|---|---|
| **A1 4×H100 原生** | **Light-WAM** | 论文明确 **4×H100** 训练；脚本默认 4 GPU；~0.44B 可训；**冻结 Wan2.1-1.3B** + StateFusion 单次解码 | LIBERO **~97.2**；RoboTwin **C~76.4 / R~76.3**（效率路线，**远低于** Fast 的 ~91.8） | [L1ziang/Light-WAM](https://github.com/L1ziang/Light-WAM)；代码 **MIT**；数据复用 Fast HF 集；权重/cache 许可常未声明 | **首次动手 / 省卡迭代默认**；**不是**强 RoboTwin baseline |
| **A2 缩小配方** | **Fast-WAM** | 官方 LIBERO **8 GPU** / RoboTwin **64 GPU**；可减 GPU；4 卡仅工程可跑 | LIBERO **~97.6**；RoboTwin **C~91.9 / R~91.8**（**unseen**）；自报延迟 ~**190 ms**（硬件见 §0.6，勿与 Light 跨表除） | [yuantianyuan01/FastWAM](https://github.com/yuantianyuan01/FastWAM)；**MIT**；预处理数据 | **强 RoboTwin/联合视频–动作 科研主基座**；4 卡**不能**声称复现论文全量分 |

#### Track B — 高分 **公开实现参考**（对齐社区数字）

| 方法 | 官方训练规模 | 作者报告成绩 | 代码/权重 | 判断 |
|---|---|---|---|---|
| **LingBot-VA** | 后训练文档示例 **NGPU=8** | RoboTwin Clean **92.93** / Rand **91.55**（与 Fast-WAM 对比时注意其 eval 常用 **seen instruction**，README 指出 seen 可高约 1–2pt）；LIBERO avg **98.5** | Apache-2.0；权重+后训练+数据；⭐~1628 | **高分 checkpoint + 后训练参考首选**；**不是**「已验证 4×H100 默认后训练基座」。全量预训练不可复现，应以后训练/改模块为主 |
| **LaWAM** | 轻量潜空间 | LIBERO **98.6**；RoboTwin Overall **91.22**（项目页 Clean 92.52 / Rand 89.48；**Overall 聚合规则未解释**，(92.52+89.48)/2=91.00≠91.22）；延迟 **187 ms @ A100 / 10 denoising steps / action-chunk** | 代码+权重+数据；**无根 LICENSE** | 潜空间/延迟路线强对照；许可与数据来源澄清前不作默认主栈 |
| **DiT4DiT**（VAM） | 证据**分层**：仓库脚本 LIBERO **64** / RoboCasa **16** 进程；README **>8 GPU**；论文附录另有 **32 GPU** 叙事；HF 发布 config 的 step/batch 与脚本**不完全一致** | **仓库 README**：LIBERO avg **98.6**（98.6/100/99.2/96.6）；RoboCasa-GR1 **~56.7**（5 run）。**arXiv 分项可能不同**，禁止与 README 混成单一「作者表」。**无完整官方 RoboTwin recipe/ckpt/结果**（dataloader 或有 mixture 名，≠可跑闭环） | [Mondo-Robotics/DiT4DiT](https://github.com/Mondo-Robotics/DiT4DiT)；代码 **MIT**；HF 元数据 **Apache-2.0**（上游 **Cosmos-Predict2.5** 仍受 NVIDIA Open Model License）；arXiv **2603.10448** | 见 §4.13。**Cosmos 策略 VAM 对照**；4×H100 以 **ckpt eval** 为主；真机 G1 有文档 |

#### Track C — 大算力 / 条件参考（不默认）

| 方法 | 关键约束 | 判断 |
|---|---|---|
| **Motus** | 训练 VRAM **>80 GB/卡**；普通 DP **不会**把 4×80G 合成一张卡；RoboTwin Clean **88.66** / Rand **87.02**（**87.02 是 Randomized，不是总平均**）；公开仓 LIBERO 闭环弱 | **4×H100 80G 默认不可判定可训**；需 94G/显存优化/明确 FSDP 后再验 |
| **Cosmos-Policy** | LIBERO 原始配方量级 **64×H100 / ~48h**；8×80G 梯度累积≠4GPU 已验证；代码 Apache-2.0，**LIBERO 权重多为非商用（NSCLv1 等）** | 官方稳文档对照；4×H100 时间/收敛**未验证** |
| **DiT4DiT 全量训练** | 同 Track B：官方 LIBERO 64 进程 / RoboCasa 16 进程；DeepSpeed ZeRO-2 | 仅当你有 ≥8–16 GPU 想复现作者训练配方时；否则用 **公开 ckpt eval** |
| **DreamZero** | 已有 **4 GPU LoRA / Wan2.2-5B** 路径（不仅 14B）；但 **PolaRiS/Genie 本地 sim 仍 Coming Soon**；DROID 14B 权重 **CC-BY-NC** | **跨 embodiment / 零样本研究线**；不进 LIBERO/RoboTwin 主线排名 |
| **StarWAM** | 无正式论文；作者自报 RoboTwin MoT ~89.5；训练示例 8 GPU | **工程孵化/模块乐高（T2）**，不参与 SOTA 排名 |

#### Track E — 动作条件 **视频世界模型 / 数据引擎**（不是策略 WAM）

> 输入：初始视频历史 + **动作/位姿轨迹条件**（BWM 公开 profile 为 14-D 双臂 EEF/state_pose；± 语言）→ 输出：**未来视频**。  
> **不**输出可执行策略，也**没有** LIBERO/RoboTwin 成功率表。用途：仿真器候选、合成数据引擎、物理一致性评测、给策略 WAM 当世界模型支路。

| 方法 | 骨干 | 开源状态 | 关键成绩 / 定位 | 4×H100 / 选型判断 |
|---|---|---|---|---|
| **boundless-world-model（BWM）** | **Wan2.2-TI2V-5B** + action encoder | [boundless-large-model/boundless-world-model](https://github.com/boundless-large-model/boundless-world-model) ⭐~**1845**；代码 **Apache-2.0**；HF `BLM-Lab/Boundless-World-Model`（`step-12000.safetensors`，**权重许可未声明**）；**推理入口+模型定义+公开 ckpt** | **无独立 tech report / 无 paper score**。WorldArena **竞赛快照（约 2026-05）**：项目团队提交 **`BLM`** 在开源 Track1 与 Track2 Data Engine 自报第 1；**`BWM-Fast`** 自报 Track1 overall 第 2（开源标签以后续 Space JSON 为准，Codex 称其 `open_source: no`）。**公开 HF ckpt 与上述提交的映射未披露** | 见 §4.11。**Track E 优先推理审计候选**（非 4×H100 可训默认）。**不能**当策略 WAM 主基座。训练：**未正式发布**；仓内有通用脚手架但默认 **Wan2.1-Fun-1.3B**，**不是** BWM 5B 可复现配方 |
| **WoW** | Wan/Cosmos DiT 系 | 推理+权重；训练 roadmap 未勾 | 物理一致性视频先验 | 同类：推理-only 先验，非策略 |
| **BiWM** | Wan/HY/LTX 多骨干 | 可训脚手架；**论文撤稿**；无权重 | 交互视频 WM 框架 | 学术主张降权；工程可参考 |

#### Track D — Paper-only / 策略向观察名单（原「黑名单」改名）

| 项目 | 状态 | 用法 |
|---|---|---|
| **Motubrain**（arXiv 2604.27792） | 作者报告 RoboTwin Clean **95.8** / Rand **96.1** 量级（**论文表高锚**）；公开训练仓/权重未形成可开发闭环 | 论文表上界；**不可当基座** |
| **Next Forcing**（2606.11187） | README **Code coming soon**；有项目页与结果图；RoboTwin Clean 94.1 / Rand 93.5 | **训练代码未发布**（不宜简单骂「空壳仓库」，但**不可训**） |
| **FlowWAM**（2607.13017） | 光流统一动作表示；有论文数字，完整训练发布需再核 | paper/效率路线观察 |
| **BiWM**（策略平台语境） | **撤稿** + 无权重 | 勿当 WAM 训练平台（脚手架见 Track E） |

### 0.4 给 4×H100 的**双默认**（独立结论，非盲从 Codex）

Codex 审查主张「默认只选 Light-WAM」。**部分同意**：

| 目标 | 默认选择 | 理由 |
|---|---|---|
| **W1 先跑通训练闭环** | **Light-WAM** | 论文明确 4×H100；脚本 4 GPU；数据/评测接口近 Fast |
| **强 RoboTwin / 联合 flow–动作科研主基座** | **Fast-WAM** | ~91.8 RoboTwin 量级；科学问题定义正统 |
| **效率 / adapter / 单次解码 / 严格 4 卡迭代** | **留在 Light-WAM** | RoboTwin 比 Fast 低约 **15pt**，但吞吐/显存更优（论文同硬件表） |
| **对齐社区高分 ckpt** | **LingBot-VA** | 后训练参考；注意 seen/unseen |
| **改结构（sim critic）** | **StarWAM** 或从 Fast/Light 拆 | 工程乐高 |
| **Cosmos VAM / LIBERO+RoboCasa / G1** | **DiT4DiT ckpt eval** | 无完整 RoboTwin 官方闭环；全量训练配方有冲突 |
| **视频 WM / 数据引擎** | **BWM 推理** | 非策略 |

**不同意**把 Light 说成最强开源 SOTA（RoboTwin 明显弱于 Fast）。  
**不同意**无条件「最终必须落 Fast」——由研究问题分流（Codex #3 采纳）。  
**不同意** BWM 当策略默认。

### 0.5 Codex 审查采纳日志（保留思考）

| 轮次 | Codex 意见 | 独立裁决 |
|---|---|---|
| #1 | 混用「论文 SOTA / 可复现 / 4H100」 | **采纳** → 文首术语表 |
| #1 | Motus「4×H100 恰好够」逻辑错 | **采纳** |
| #1 | Fast-WAM unseen vs LingBot seen | **采纳并核对 README** |
| #1 | Light-WAM 升为唯一默认 | **部分采纳** → Track A 脚手架，非唯一科研基座 |
| #1 | 物理一致性「真空」过强 | **采纳** → WorldArena 等 |
| #2 | BWM「训练半公开」过强；默认脚本是 1.3B 非 5B | **采纳**（核对 train_distributed.sh + train yaml） |
| #2 | 公开 ckpt 与 BLM/BWM-Fast 提交映射未披露 | **采纳** |
| #2 | HF 480×640/81 vs repo infer 672×896/57 | **采纳**（核对 HF config.json） |
| #2 | action_dim 与 eef_abs→state_pose 接口 | **采纳** |
| #2 | 「low-cost high-fidelity」当事实 | **采纳** → 标 README claim |
| #2 | BWM-Fast 榜单 `open_source: no` | **谨慎采纳措辞**；未本机重下 Space JSON，文中标「以后续 Space 为准」 |
| #2 | 全文 7/10、Track E 分类正确 | **同意方向** |
| **#3** | DiT4DiT 成绩/配方混源；§0.6 漏 Light 性能代价与同硬件延迟 | **采纳要点**（见下）；学习序改为「问题分流」非无条件落 Fast |

### 0.6 Fast-WAM vs Light-WAM：差别大吗？先学习用哪个？

> **Codex #3 评分 §0.6：7/10**（方向对，缺性能差与证据分层）。本小节已按审查修订。  
> 结论：**方法与算力差别大；raw 数据/评测接口近，但 Light 的 latent cache 预处理成本高。**  
> **先动手 → Light**；**科学问题 → Fast 论文**；**主基座 → 由目标分流，不是无条件「最终 Fast」**。

#### 一句话关系

```
同一赛道（LIBERO + RoboTwin；Light 代码/数据明确继承 Fast 生态）
  ├─ Fast-WAM：Wan2.2 系 + 迭代式 ActionDiT（多步 denoising）+ 联合视频–动作
  └─ Light-WAM：冻结 Wan2.1-1.3B + LoRA/adapters + StateFusion **单次** action 解码
     （不是「把 Fast 缩宽」那么简单——策略头与推理机制重构）
```

#### 对照表（含成绩与延迟条件）

| 维度 | **Fast-WAM** | **Light-WAM** |
|---|---|---|
| 论文问题 | 测试时要不要显式想象未来？ | 轻量可部署 WAM |
| arXiv | **2603.16666** | **2606.08242** |
| 代码 | [yuantianyuan01/FastWAM](https://github.com/yuantianyuan01/FastWAM) | [L1ziang/Light-WAM](https://github.com/L1ziang/Light-WAM) |
| 骨干 / 动作头 | Wan2.2 系；**迭代式** ActionDiT（论文叙事约 10-step action denoising） | **冻结** Wan2.1-1.3B；**StateFusion 单次** decoding |
| 可训参数 | 较大（含视频协同） | 约 **0.44B**（作者） |
| 训练算力 | 官方 LIBERO **8** / RoboTwin **64** GPU；4 卡可试但**论文分未验证** | 论文明确 **4×H100**；脚本默认 4 GPU；同硬件吞吐优于 Fast（论文表：如 2.08 vs 0.49 step/s 量级，以论文 Table 为准） |
| 数据 | HF 预处理 LIBERO/RoboTwin | **复用** Fast 的 HF raw 集；另需 **Wan1.3B latent cache**（发布 cache 体积可到 **TB 级**；RoboTwin text cache 或需本地生成） |
| LIBERO（论文） | **~97.6** | **~97.2**（接近） |
| RoboTwin（论文） | **C~91.9 / R~91.8**（unseen） | **C~76.4 / R~76.3**（约 **−15pt**；效率代价） |
| 延迟 | 自报 ~**190 ms**（**RTX 5090D** 等，见 Fast 文） | 自报 ~**72 ms**；**同源同硬件**重测叙事：Fast ~**405 ms** vs Light ~**72 ms**（Light 文 Table，**优先用此对照，勿 190/72 跨表硬除**） |
| instruction | 评测默认 **unseen**（README 明示） | 发布 config 常见 **unseen**；论文正文未必写清 split |
| 代码 LICENSE | **MIT** | **MIT**（根 LICENSE 含 Light-WAM Authors） |
| 权重/cache 许可 | HF ckpt 常 **无 license 字段** | 同；offline-cache **未声明** |
| 适合 | 强 RoboTwin baseline、联合 flow 消融 | 4 卡闭环、效率/adapter 研究、学习 pipeline |

#### 「差别大吗」

| 关心点 | 差别 |
|---|---|
| raw 数据 URL / LIBERO·RoboTwin 评测 harness | **相对小** |
| 训练预处理（latent cache、存储） | **大**（Light 额外 cache 成本） |
| 模型机制（多步 ActionDiT vs 单次 StateFusion） | **大** |
| RoboTwin 分数 | **大**（~92 vs ~76） |
| 4 卡可训性 | Light **原生**；Fast **可缩未验证论文分** |

#### 学习 / 选型路径（修订，问题分流）

| 阶段 | 建议 |
|---|---|
| **0** | 可选：Fast / Light **官方 ckpt eval smoke**（先确认环境与指标） |
| **1** | **Light 短训练闭环**（记录 cache 体积、显存、吞吐）+ 精读 **Fast 论文** |
| **2a 强 RoboTwin / 联合视频–动作** | 深入 **Fast-WAM** 代码与缩小后训练 |
| **2b 效率 / 单次解码 / 严格 4 卡** | 留在 **Light-WAM** 迭代 |
| **2c 高分对照** | LingBot-VA ckpt（协议对齐） |

#### 决策口令

1. **先学习、4 卡跑通** → **Light** 动手 + **Fast** 读论文。  
2. **要强 RoboTwin 开源 baseline** → **Fast**（接受更重训练）。  
3. **要效率或 adapter 叙事** → **Light**（接受 RoboTwin 低约 15pt）。  
4. **不要**无条件写「最终必须 Fast」；**不要**把 Light 说成更强 SOTA；**不要**跨硬件拼延迟倍数。

---

## 1. 领域现状与文献入口（2026-07）

### 1.1 两份 Survey

| Survey | 出处 | 用途 |
|---|---|---|
| **World Action Models: The Next Frontier in Embodied AI** | OpenMOSS / 复旦等，arXiv **2605.12090**；[Awesome-WAM](https://github.com/OpenMOSS/Awesome-WAM) | Cascaded vs Joint；持续更新 + leaderboard |
| **World Action Models: A Survey** | NUS 等，[world-action-models.github.io](https://world-action-models.github.io/) | 另一套 taxonomy + 周更 list |

NVIDIA 博文（2026-06）定义 WAM：从预训练视频/世界模型骨干出发，同时建模场景随时间变化并输出动作。

### 1.2 架构谱系

```
Cascaded WAM:  先生成未来视频/几何  →  再 IDM / 规划出动作
Joint WAM:     同一模型联合 p(future, action | obs, ...)
  ├─ Autoregressive (离散 / 因果块)   WorldVLA, RynnVLA-002, LingBot-VA
  └─ Diffusion / Flow
       ├─ Unified stream              DreamZero, Cosmos-Policy, Fast-WAM(训)
       └─ Multi-stream MoT            Motus, LingBot-VA MoT, StarWAM mot_wam
Latent WAM:    特征/子目标，不重建像素   LaWAM, Light-WAM(降采样潜空间监督)
```

---

## 2. 共性 Benchmark

### 2.1 Tier-0 必跑

| Benchmark | 类型 | 为何共性 | 协议要点（报告时强制） | 饱和风险 |
|---|---|---|---|---|
| **LIBERO** | 单臂桌面 | 几乎所有开源 WAM 都报 | 套件拆分；no-ops；相机数；seed×trial；**&lt;1–2pt 不得单独宣称优越** | **很高** ~98%+ |
| **RoboTwin 2.0** | 双臂 50 任务 + 随机化 | 2026 WAM 主战场 | 统一 **Clean / Randomized**（勿混用 Easy/Hard 除非官方同义）；**instruction_type=seen\|unseen**；每任务 trials；数据 clean/random 配比；视角/分辨率；action chunk | **中高** 头部 90–96% 论文表；任务异质性强 |

**开发建议**：

- **主指标**：RoboTwin Clean + Randomized（分列 + 平均）。  
- **副指标**：LIBERO 四套件。  
- **强制元数据**：具身预训练与否、官方 GPU 数、是否缩小配方、延迟（硬件 + denoising steps + chunk 定义）。

### 2.2 Tier-1 扩展

| Benchmark | 用途 |
|---|---|
| **RoboCasa** | Cosmos 系第二尺 |
| **SimplerEnv** | 传统 VLA / sim-real 相关 |
| **CALVIN** | 长程语言 |
| **RoboArena / MolmoSpaces** | 真机 leaderboard（贵） |
| **RMBench** | RoboTwin 上的记忆依赖扩展 |

### 2.3 物理一致性 / 世界模型功能评测（**尚未统一主导协议**）

> 旧表述「评测真空」**过强**。已有公开基准，但**无单一社区默认尺**，接触级闭环漂移仍弱。

| 资源 | 内容 | 备注 |
|---|---|---|
| **WorldArena（v1）** arXiv **2602.08971**；[WorldArena](https://github.com/tsinghua-fib-lab/WorldArena/) | 具身世界模型感知与功能效用统一评测 | **BWM 竞赛/Space 证据主要属此协议族**；leaderboard: [HF Space](https://huggingface.co/spaces/WorldArena/WorldArena)（名次会变，应记 snapshot date） |
| **WorldArena 2.0** arXiv **2605.17912** | 扩模态、功能角色、平台（含更广 sim/real 等） | **不能**把 v1 challenge 名次自动当成 2.0 已测 |
| **BWM 项目团队 @ WorldArena（竞赛快照）** | 提交名 **`BLM`** / **`BWM-Fast`** 的 Track 成绩（README 2026-05 图） | **≠** 已证明 HF `step-12000` 复现该名次；动态榜需重查 |
| **WoWBench** | 物理/因果样本 | HF samples；协议成熟度有限 |
| **BadWAM 类工作** | 对抗/扰动下 WAM 成功率崩塌 | 提醒：clean SR 不够 |
| **GPC sim 上界协议** | 用真值 sim 定价模型误差 | 思想可复用 |
| **自建 Step-0** | 穿透、漂移、接触时序、末态 | 仍可做差异化贡献；可与 WorldArena 对齐指标 |

### 2.4 公开数字对照（**禁止跨协议硬比**）

| 方法 | RoboTwin（作者报告） | 指令协议 | LIBERO | 延迟条件 | 开源训练？ |
|---|---:|---|---:|---|---|
| Motubrain | C 95.8 / R 96.1 量级 | 待核 | — | — | **否**（paper-only） |
| Next Forcing | C 94.1 / R 93.5 | 待核 | — | MCP 2× 模式 | **否** |
| LingBot-VA | C 92.93 / R 91.55 | 常 **seen**（对照 Fast-WAM README） | 98.5 | 异步管线 | **是**（后训练；预训练否） |
| Fast-WAM | C≈91.9 / R≈91.8 | **unseen**（README 明示） | ≈97.6 | ~190 ms | **是** |
| LaWAM | Overall 91.22（C 92.52 / R 89.48） | 待核 | 98.6 | 187 ms，**A100 / 10 steps / chunk** | **是** |
| Motus | C 88.66 / R 87.02 | 待核 | 论文对照 ~97.7 | 推理 24–41GB+ | **是**（RoboTwin；LIBERO 弱） |
| Light-WAM | **C~76.4 / R~76.3**（论文） | 发布 config 常 unseen | **~97.2** | ~72 ms（Light 文；同硬件 vs Fast 见 §0.6） | **是**，论文 **4×H100** |
| **DiT4DiT** | **无完整官方 RoboTwin 结果** | — | README avg **98.6**（分项见 §4.13；**与 arXiv 分项可能不同**） | 视频侧特征提取常 **1 step**；动作 DiT **4** step（配置） | 训练配方冲突；**eval 单卡可行** |
| Cosmos-Policy | —（主 RoboCasa） | — | 98.5 | ~0.61s/chunk @5 步 H100 | **是**（大规模） |
| StarWAM MoT | ~89.5 作者报 | 待核 | 有 ckpt | — | 工程仓 |

**读表规则**：

1. 论文表最高 ≠ 可训练开源最强。  
2. LingBot vs Fast-WAM：**seen/unseen 不对齐则禁止排名**。  
3. &lt;1–2pt：要求 task-level、种子、CI、最差任务。  
4. 延迟无硬件/步数/chunk 定义则**不可比**。

### 2.5 诊断警示

- arXiv 2606.04233：LIBERO/CALVIN/SimplerEnv 多项诊断偏弱；RoboTwin/RoboCasa 相对更健康。  
- **选择门槛**：无协议元数据的「SOTA」一律降权。

---

## 3. 最新 / 关键论文地图

### 3.1 联合像素/视频 WAM

| 论文 | arXiv | 核心主张 | 开源状态 |
|---|---|---|---|
| DreamZero | 2602.15922 | 14B 联合视频+动作；零样本 | 训练/推理开；4GPU LoRA/5B 有；**sim 入口弱** |
| LingBot-VA | 2601.21998 RSS'26 | 因果 AR 扩散 + MoT + 闭环回填 | **完整后训练** |
| Motus | 2512.13030 CVPR'26 | MoT 三专家 + 多模式 | 训练+权重；显存重 |
| Fast-WAM | 2603.16666 | 测试时想象非必要 | **MIT + 预处理数据** |
| Cosmos Policy | 2601.16163 | 单阶段视频模型→策略 | 官方文档强 |
| Light-WAM | 2606.08242 | 轻量 + StateFusion | **4 GPU 原生** |
| Next Forcing | 2606.11187 | Multi-Chunk Prediction | **代码未发布** |
| Motubrain | 2604.27792 | UniDiffuser + 三流 MoT | **paper-only 高分锚** |
| FlowWAM | 2607.13017 | 光流统一动作表示 | 观察 |
| **DiT4DiT** | 2603.10448 | 视频 DiT + 动作 DiT 级联；中间去噪特征条件动作（非重建帧） | 训练+eval+G1 真机；LIBERO/RoboCasa ckpt；**无 RoboTwin**；官方 16–64 GPU 训练 |

### 3.2 潜空间 / 高效

| 论文 | arXiv | 开源 |
|---|---|---|
| LaWAM | 2606.15768 | **RLinf/LaWAM**（legal hold） |
| mimic-video / VLA-JEPA / S-VAM 等 | 2025–26 | 部分有代码 |

### 3.3 级联 / 规划 / 推理时

GPC、SimDist、UniPi/VLP/TesserAct 等——见 Awesome-WAM。

### 3.4 基础设施 / 动作条件视频世界模型

| 项目 | 状态 | 与 WAM 开发关系 |
|---|---|---|
| **BWM（boundless-world-model）** | 公开推理入口+定义+可下载 ckpt；**训练未正式发布**；团队 WorldArena 竞赛成绩有、**ckpt↔提交映射无** | **EEF 轨迹条件视频生成**候选 / 潜在数据引擎；**不是**策略 WAM |
| BiWM 2606.10135 | **撤稿**；代码可训；无权重 | 脚手架参考 |
| WoW | 推理+权重；无训练 | 物理视频先验 |
| Wan2.1/2.2、Cosmos-Predict | 默认骨干 | BWM/多数 WAM 底座 |

### 3.5 AR 统一族（对照）

WorldVLA、RynnVLA-002、F1-VLA——离散 AR，与 Wan 扩散栈不同。

---

## 4. 开源方法深潜（实访 + 审查修订）

### 4.1 LingBot-VA — 高分参考（非 4GPU 已验证默认）

| 项 | 内容 |
|---|---|
| 代码 | https://github.com/Robbyant/lingbot-va |
| 论文 | 2601.21998，RSS 2026 |
| 权重 | `robbyant/lingbot-va-base`、posttrain-robotwin、posttrain-libero-long |
| 数据 | robotwin-clean-and-aug-lerobot、libero-long-lerobot（**数据许可可能 NC 系，用前核 model/dataset card**） |
| 代码许可 | Apache-2.0 |
| 官方训练 | 后训练示例 **8 GPU**；`attn_mode` train=`flex` / infer=`torch\|flashattn` |
| 成绩 | RoboTwin C/R 92.93/91.55；LIBERO 98.5 |
| 风险 | 预训练不可复现；seen instruction 优势；4×H100 后训练**未官方验证** |

**选型**：要对齐社区高分与活跃维护 → **参考 ckpt + 尝试缩小后训练**。不要写成「4×H100 已验证默认基座」。

### 4.2 Fast-WAM — 数据/消融基座

| 项 | 内容 |
|---|---|
| 代码 | https://github.com/yuantianyuan01/FastWAM |
| 许可 | **MIT**（有 LICENSE 文件） |
| 数据 | HF 预处理 LIBERO + RoboTwin |
| 训练 | LIBERO 8 GPU；RoboTwin **64 GPU**；可减 GPU |
| Eval | 默认 **unseen** instruction；与 LingBot **seen** 不对齐 |
| 科学点 | 训练时视频协同训练关键；测试时显式未来非主因 |

**选型**：最快双 bench 闭环与因果消融；4 GPU 仅「缩小配方」。

### 4.3 Light-WAM — 4×H100 原生脚手架

| 项 | 内容 |
|---|---|
| 代码 | https://github.com/L1ziang/Light-WAM |
| 论文 | 2606.08242 |
| 训练 | `train_robotwin.sh` 默认 `GPU_IDS=0,1,2,3`，`NUM_PROCESSES=4` |
| 数据 | 明确复用 Fast-WAM 预处理集 |
| 定位 | **效率路线**；可训参数约 0.44B |

**选型**：**算力诚实下的 W1 默认**。不与 LingBot 论文表分直接比「谁更强」。

### 4.4 Motus — 显存顶格，逻辑修正

| 项 | 内容 |
|---|---|
| 代码 | https://github.com/thu-ml/Motus |
| 训练 VRAM | **>80 GB/卡** |
| 4×H100 80G | **默认不可判定可训**（DP 不合并单卡峰值） |
| RoboTwin | Clean **88.66** / Randomized **87.02** |
| LIBERO | 公开仓闭环弱；97.7 仅作论文对照表 |

### 4.5 Cosmos-Policy — 官方对照 + 许可拆分

| 项 | 内容 |
|---|---|
| 代码 | NVlabs/cosmos-policy，Apache-2.0 |
| 权重 | 常为 **非商用**（如 NSCLv1 / One-Way Noncommercial）——**勿用代码许可证代替** |
| 训练 | LIBERO 原始规模约 64×H100/48h；4×H100 **未验证** |

### 4.6 StarWAM — 工程 T2

无正式论文；Wan2.2/Cosmos 可插拔；MoT / Shared-DiT / Feature-conditioned。  
**不参与 SOTA 排名**；改结构时优先。

### 4.7 LaWAM — 开源已确认 + legal hold

| 项 | 内容 |
|---|---|
| 代码/权重/数据 | 齐全（见 README HF 表） |
| Overall 91.22 | 与 C/R 简单平均不一致 → **聚合待澄清** |
| 延迟 | 条件：A100、10 steps、per chunk |
| LICENSE | **根目录无 LICENSE**；权重/数据声明需逐卡核；可能与 NC 派生数据冲突 |
| 可复现（工程） | **4+**；可复现（法律清晰）**暂降** |

### 4.8 DreamZero — 研究线更新

- 不再只是「14B 不适用」：存在 **4 GPU LoRA / 5B** 路径。  
- **共性仿真闭环仍弱**（PolaRiS Coming Soon）。  
- 权重许可与代码许可分离（DROID 常 NC）。

### 4.9 BiWM — 撤稿

- 撤稿原因：可视化配置错误。  
- 无权重。  
- 代码可训 → 想法可借鉴，**论文表与 R5 平台建议降级**。

### 4.10 （占位说明）

> 编号：原 4.10 并入许可证矩阵为 §4.12；BWM 深潜为 §4.11。

### 4.11 Boundless-World-Model（BWM）— 动作条件视频世界模型（Track E）

> **身份澄清（最重要）**：BWM **不是** World-Action **Policy**（不输出控制动作、不报 LIBERO/RoboTwin SR）。  
> 公开接口更准确是：**初始视频历史 + 14-D 双臂绝对 EEF pose/gripper 轨迹（`eef_abs`→`observation.state/state_pose`）→ 未来视频**。  
> README 自我定位 *physically consistent / low-cost / high-fidelity simulator* → **作者 claim**，非本文件独立测定。  
> 与 LingBot/Fast-WAM **策略轨正交**；与 BiWM/WoW 同属视频 WM 族。

#### 证据状态四行（2026-07-20）

| 证据类型 | 状态 |
|---|---|
| technical report / paper score | **无**（BWM 独立 tech report 未放） |
| challenge / leaderboard submission | **有**（README：CVPR 2026 WorldArena 团队提交 `BLM` / `BWM-Fast` 名次图） |
| public checkpoint | **有**（HF `step-12000.safetensors` ~10GB 级；**许可未声明**） |
| reproducible training（=本文「可训练开源」） | **无**（README Coming soon；仓内脚手架默认 **非** BWM-5B 配方） |

| 项 | 内容 |
|---|---|
| 仓库 | https://github.com/boundless-large-model/boundless-world-model |
| 实访 commit | `44acfd1b06f3…`（2026-07-20 shallow clone） |
| 组织 | Boundless Large Model / BLM-Lab；致谢含同济等；与 BLM₁（arXiv 2510.24161）叙事相关但 **≠ 同一可复现训练产物** |
| 骨干 | **Wan2.2-TI2V-5B** |
| 权重 | HF [`BLM-Lab/Boundless-World-Model`](https://huggingface.co/BLM-Lab/Boundless-World-Model)；HF `config.json`：`height/width` **480×640**，`num_frames` **81**，`num_history_frames` **9**，`action_type` **state_pose**，`max_train_steps` **12000**（与文件名一致）；**无 license 字段** |
| 代码许可 | **Apache-2.0** |
| 社区 | ⭐~1845；forks ~75 |
| 栈 | PyTorch 2.8 + cu128；DiffSynth-Studio 2.0.11；包名 `wan-video-action` |

#### 架构（代码级）

- 包 `wan_video_action/`：DiffSynth Wan 管线 + 动作条件 units。  
- **`WanVideoActionEncoder`**：  
  - **`noise`**：逐帧动作注入；  
  - **`adaln`**：chunk/全局条件 + `encode_ti2v2`（面向 Wan2.2 TI2V）。  
- **`action_dim=14`**：**每臂 6-D joint/EEF pose + 1-D gripper，×2 臂**（非「7 关节+夹爪」笔误）。  
- 公开推理 profile（`configs/infer/infer.yaml`）：`action_type: eef_abs` → 代码映射 **`state_pose`**；**672×896**、`num_frames: 57`、`history: 9`、`action_mode: adaln`、50 steps。  
  → 与 HF card **480×640 / 81 frames** **并存且未说明**哪套对应 `step-12000` 训练或榜单提交。  
- 训练脚手架（`train.py`）：FlowMatch SFT 等；示例 yaml 可 `trainable_models: "dit,action_encoder"` 或 HF config 中 `dit`。  
- Demo：RoboTwin 风格任务元数据 + WorldArena 场景定性 GIF（堆叠/铰链/affordance/双臂 handover/长程放置/OOD 初值）。

#### 开源完整度（诚实账）

| 组件 | README TODO | 仓库/HF 实况 | 判定 |
|---|---|---|---|
| 推理代码 | ✅ | `scripts/infer.py`、`infer_example.sh` | **入口可用**（本文未做端到端 smoke test） |
| 模型定义 | ✅ | `wan_video_action/*` + docs | **可用** |
| 模型权重 | ✅ | HF `step-12000` | **公开可下载**；许可未声明；**≠** 已映射竞赛提交 |
| 训练代码 | ☐ Coming soon | 有 `train.py` / `train.sh` / `train_distributed.sh` / yaml | **不满足「可训练开源」**：默认 `MODEL_DIR`→**Wan2.1-Fun-1.3B-InP**，`train_action_noise.yaml`→`wan2_1_fun_1_3b_inp.yaml`；**无 BWM/Wan2.2-5B 数据配方、日志、复现命令** |
| Technical report | ☐ | 无 | **无** |

**4×GPU**：`train_distributed.sh` 仅证明可 `NUM_PROCESSES=4` 启动**通用**训练进程；**不能**推出 BWM-5B 在 4×H100 上显存/吞吐/收敛可行。删除「4×GPU 友好」表述。

#### WorldArena 成绩（竞赛快照，非本机复现）

| 提交名（README） | 自报名次 | 备注 |
|---|---|---|
| **BLM** | 开源 Track 1 与 Track 2 Data Engine **第 1**（2026-05 图） | 动态 Space 可能已变；开源标签以 Space 元数据为准 |
| **BWM-Fast** | Track 1 overall **第 2** | Codex 称 Space JSON 中 `open_source: no` → **勿当「开源冠军 ckpt」**；需自行复核 Space |
| 映射 | — | **HF `step-12000` ↔ 上述提交：未公开映射** |

Leaderboard：https://huggingface.co/spaces/WorldArena/WorldArena  

**独立结论**：WorldArena 证明「物理/功能向世界模型评测」已有社区尺；BWM **项目团队**有强竞赛记录；**不能**写成「公开 BWM 权重已复现该名次」。

#### 与本文其他项的关系

| 对比 | 结论 |
|---|---|
| vs 策略 WAM | 任务不同；**不可替代** |
| vs WoW | 同族；BWM **有明确动作条件 + 可下载 5B ckpt**，优先作推理审计 |
| vs BiWM | BiWM 撤稿无权重；视频 WM 参考 **优先 BWM 推理** |
| vs sim-anchored | 可作 **EEF 轨迹→视频** 支路 / 合成视频源；接策略前需 **动作空间对齐与归一化**；物理仍应用 **sim GT** 锚定 |

#### 选型判断（独立，吸收 Codex #2）

1. 刷 RoboTwin/LIBERO **策略 SR** → **不要** BWM 主基座。  
2. Track E：把 BWM 当作 **优先推理 smoke-test / 接口研究候选**，不是「已验证 4×H100 可训视频 WM 基座」。  
3. 准入再升格为「世界模型轨默认」前建议满足：单样本推理 smoke test、peak VRAM、动作适配层、WorldArena 子集自跑、（若训练）5B 正式配方发布。  
4. 与 Fast-WAM/LingBot **双轨组合**，而非二选一。

### 4.13 DiT4DiT — Cosmos 骨干 Video-Action Model（策略 VAM）

> **Codex #3 评分 Focus A：6/10**——大方向对，但论文/README/HF/脚本被混成单一证据链。下表已分层。  
> **身份**：VAM——**输出动作**（策略轨），**不是** BWM 纯视频 WM。骨干 **Cosmos-Predict2.5-2B**。  
> **机制（更准确）**：固定 \(\tau_f\) 对 noisy future latent 做 Video-DiT 前向取中间特征；配置 **`future_num_inference_steps: 1`**（非多步完整未来视频），动作 DiT **`num_inference_timesteps: 4`**。  
> **RoboTwin**：无完整官方 recipe/eval/ckpt/结果；代码侧或有 mixture 名 ≠ 可复现闭环。

#### 证据状态

| 类型 | 状态 |
|---|---|
| paper | arXiv **2603.10448** |
| code | https://github.com/Mondo-Robotics/DiT4DiT |
| ckpt | HF `mondo-robotics/dit4dit-model` |
| code license | **MIT** |
| weight license | HF 元数据 **Apache-2.0**；**上游 Cosmos = NVIDIA Open Model License** |
| 4×H100 全量训练 | **无闭合配方**；README **>8 GPU** 推荐 |

#### 训练配方来源冲突

| 来源 | 进程/GPU | per-device batch | max steps |
|---|---|---|---|
| 论文附录通用叙事（Codex 读 PDF） | ~**32** GPU | 8 等 | ~100k |
| `run_libero.sh` | **64** | 4 | **80k** |
| `run_robocasa.sh` | **16** | 4 | **200k** |
| HF `dit4dit_libero/config.yaml` | 未写死进程 | 4 | **160k** |

#### 架构要点（按 benchmark）

| 项 | LIBERO（HF config 已核） | RoboCasa（仓库 yaml） |
|---|---|---|
| `extract_layer` | **17**（论文或写 18） | 同系 |
| `action_horizon` | **8** | **16** |
| `action_dim` / `state_dim` | 8 / 16 | 32 / 64 |
| 视频特征步 / 动作步 | **1** / **4** | **1** / **4** |

#### 成绩分层

**README / Model Zoo**：LIBERO 98.6/100/99.2/96.6 → **Avg 98.6**；RoboCasa-GR1 五次 ~**56.3–57.4**（入口 56.7）。  
**arXiv（Codex 核 v2）**：LIBERO 分项 **98.4/99.6/98.6/97.6**（Avg 仍 98.6）；RoboCasa 论文表约 **50.8** ≠ README 56.7。  
→ **引用必须标明来源**。

#### 选型

1. 主 RoboTwin+Wan → **旁路对照**。  
2. Cosmos LIBERO 高分 → **ckpt eval**。  
3. G1 真机 → Real_G1。  
4. 全量训练仅 ≥8–16 GPU 且接受配方未闭合。

### 4.12 许可证矩阵（代码 ≠ 权重 ≠ 数据）

| 项目 | 代码 | 权重 | 数据 | 备注 |
|---|---|---|---|---|
| LingBot-VA | Apache-2.0 | 待核 card | 可能 NC-SA 系 | 用前读 dataset card |
| **Fast-WAM** | **MIT** | HF ckpt 常无 license 字段 | 预处理集 | 权重再分发谨慎 |
| **Light-WAM** | **MIT** | ckpt/offline-cache 常无 license | 复用 Fast raw + latent cache | 论文 4×H100；cache 体积大 |
| Motus | Apache-2.0 | 待核 | RoboTwin 系 | >80G/卡 |
| Cosmos-Policy | Apache-2.0 | **常非商用** | 官方提供 | 大规模训练 |
| LaWAM | **无根 LICENSE** | 声明 MIT 待核 | 可能 NC 派生 | legal hold |
| DreamZero | Apache-2.0 | DROID **NC** 等 | 混合 | 分资产 |
| StarWAM | Apache-2.0 | ModelScope | 待核 | 工程仓 |
| **BWM** | **Apache-2.0** | 可下载；HF 无 license 字段 | demo 在仓；全量配方未公开 | 上游 Wan2.2 另遵其许可 |
| **DiT4DiT** | **MIT** | HF 元数据 Apache-2.0 | LIBERO LeRobot；GR00T-X sim | **上游 Cosmos = NVIDIA Open Model License** |
| BiWM | Apache-2.0 | **无** | 有脚本数据 | 撤稿 |

---

## 5. 面向 4×H100 的推荐栈（修订）

### 5.1 默认组合

```
W1 跑通（原生 4 GPU）:
  Light-WAM train + Fast-WAM 预处理数据 + RoboTwin/LIBERO eval

W1–W2 高分参考:
  下载 LingBot-VA 官方 posttrain ckpt，同协议 eval（记录 seen/unseen）

W2 缩小后训练实验:
  Fast-WAM 或 LingBot-VA 后训练（grad accum / 减 batch）——只报「缩小配方」

W2 并行（世界模型轨，可选）:
  BWM 推理 smoke test（记录 peak VRAM、分辨率/帧配置用 HF 还是 repo infer.yaml）
  准备 EEF trajectory / state_pose 与策略动作空间的适配层
  可选：WorldArena v1 子集自跑——不与策略 SR 混表

W3 改结构:
  StarWAM 或 Fast-WAM 上挂 sim critic / 新损失
  （可选）BWM 作 EEF轨迹→视频 支路或合成视频源（需适配层）

对照:
  LaWAM（潜空间） | Cosmos-Policy（官方） | DiT4DiT（Cosmos VAM / LIBERO ckpt） | Motus（条件满足） | BWM（视频 WM 推理候选）
```

### 5.2 不作为**策略**主基座

- BiWM（撤稿+无权重）  
- Next Forcing / Motubrain / FlowWAM（无完整可训练发布）  
- WoW / **BWM**（**视频世界模型**，不是策略；BWM = Track E **推理审计优先**，非已验证可训基座）  
- **DiT4DiT 全量训练**（无 4×H100 官方配方；且无 RoboTwin）— **ckpt eval 可以，当主训练基座不推荐**  
- 只刷 LIBERO 不报 RoboTwin  
- 任何「论文分 − 未声明协议差」的假 SOTA

### 5.3 与 sim-anchored 项目的接口

1. 共性 bench：RoboTwin + LIBERO，**先锁协议元数据**再谈增益。  
2. 监督：Fast-WAM → 训练时视频目标重要；LaWAM → 潜空间未来可够用；sim GT 更自然挂**状态/特征**。  
3. 策略平台：**Light-WAM / Fast-WAM / LingBot 后训练 / StarWAM**，不是 BiWM。  
4. **世界模型轨**：**BWM 公开 ckpt** 优先于 WoW/BiWM 作 **EEF 轨迹条件视频** 推理试验；升格「默认」前完成 smoke test + 动作适配 +（可选）WorldArena 子集。  
5. 评测：执行率 + **WorldArena v1（动态榜）/ Step-0**；团队竞赛名次仅作动机，不代替自跑。  
6. 数据：非专家/扰动覆盖与脚手架正交；BWM 可生成反事实视频，物理仍用 **sim GT** 锚定。

### 5.4 30 天路径（修订）

| 周 | 动作 | 退出标准 |
|---|---|---|
| W1 | （可选）Fast/Light/**DiT4DiT** 官方 **ckpt eval smoke** → **Light 短训练**（记 cache/显存）；读 Fast 论文 | 协议可复述；Light 闭环；能口述 Fast vs Light |
| W2 | 目标分流：强 RoboTwin→**Fast**；效率→**Light**；Cosmos/LIBERO 对照→**DiT4DiT eval**；可选 BWM | 选定主轨并出缩小配方 ckpt |
| W3 | 主轨改结构 + sim 信号 | 同协议 A/B |
| W4 | 旁路对照 + WorldArena/Step-0；**按问题**定主基座（非无条件 Fast） | 决策有数字支撑 |

> 细节见 **§0.6**、**§4.13**。

---

## 6. 资源索引

### 6.1 Survey

- https://github.com/OpenMOSS/Awesome-WAM  
- https://world-action-models.github.io/  
- NVIDIA WAM blog

### 6.2 代码

| 项目 | GitHub |
|---|---|
| LingBot-VA | Robbyant/lingbot-va |
| Fast-WAM | yuantianyuan01/FastWAM |
| Light-WAM | L1ziang/Light-WAM |
| Motus | thu-ml/Motus |
| Cosmos-Policy | NVlabs/cosmos-policy |
| StarWAM | shaohua-pan/StarWAM |
| LaWAM | RLinf/LaWAM |
| DreamZero | dreamzero0/dreamzero |
| **DiT4DiT** | Mondo-Robotics/DiT4DiT（HF mondo-robotics/dit4dit-model；docs/libero.md、robocasa_tabletop.md、Real_G1） |
| **BWM** | **boundless-large-model/boundless-world-model**（HF BLM-Lab/Boundless-World-Model） |
| Next Forcing | gangweix/next-forcing（无训练代码） |
| BiWM | LynnReal-AI/BiWM |
| WoW | wow-world-model/wow-world-model |
| WorldArena | tsinghua-fib-lab/WorldArena |

### 6.3 Benchmark

- LIBERO、RoboTwin 2.0、RoboCasa、SimplerEnv、CALVIN、RoboArena  
- WorldArena / 2.0（物理与功能评测）

---

## 7. 核验日志

| 声明 | 方式 | 结果 |
|---|---|---|
| BiWM 撤稿 | arXiv API comment | 确认；可视化配置错误 |
| LaWAM 开源 | GitHub+HF | 确认；无根 LICENSE |
| Fast-WAM unseen | README 原文 | 确认；并指出 LingBot seen 可 +1–2pt |
| Fast-WAM GPU | README | LIBERO 8；RoboTwin 64；可减 |
| Light-WAM 4 GPU | `train_robotwin.sh` 默认 0,1,2,3 | 确认 |
| Motus >80G | README | 确认；**否定**「4×80G 恰好够」 |
| Motus 分数 | README | C 88.66 / R 87.02 |
| Next Forcing 无训练代码 | README badge | 确认 |
| Motubrain 高分 paper | arXiv 2604.27792 | 存在；开源闭环未立 |
| WorldArena 2.0 | arXiv 2605.17912 | 存在；修正「真空」 |
| **DiT4DiT** | README + 训练脚本 + HF libero config + Codex #3 PDF 交叉 | MIT；HF Apache 元数据+Cosmos 上游；脚本 64/16 vs 论文 32 vs HF 160k steps **冲突**；README LIBERO 分项 ≠ arXiv 分项（Avg 可同 98.6）；RoboCasa README 56.7 vs 论文 ~50.8；horizon 8 vs 16；无完整 RoboTwin 闭环 |
| **Fast vs Light §0.6** | 两论文 + 两 LICENSE + Light 复用 Fast 数据 | Light MIT；RoboTwin ~76 vs Fast ~92；4×H100 论文明确；延迟勿跨表；cache 成本 |
| **BWM 仓库** | clone commit `44acfd1` + README + train/infer + HF config | ⭐~1845；代码 Apache-2.0；公开 ckpt **无声明许可**；训练未正式发布且默认 1.3B 脚手架；WorldArena **团队提交**成绩有、**ckpt 映射无**；**非策略 WAM** |
| HF BWM config | `config.json` raw | 480×640、81 帧、history 9、`state_pose`、`max_train_steps=12000` |
| WorldArena arXiv | API | v1=`2602.08971`；2.0=`2605.17912` |
| Codex 审计 #1/#2/#3 | gpt-5.6-sol xhigh | #3：DiT4DiT+§0.6；见 §0.5 |

---

## 8. 维护说明

- Living survey：放码/撤稿/许可/GPU 配方变化时更新 Track 表。  
- **禁止**「论文表 SOTA = 可复现开源 SOTA」。  
- 星标与 README 会变；关键结论应绑 **commit/date + model-card license + instruction split**。

---

## 9. 最终选型结论（修订版）

1. **共性 bench**：主 **RoboTwin**（Clean/Randomized + instruction_type），副 **LIBERO**。  
2. **先学习 / 4×H100**：**Light-WAM**（§0.6）；接受 RoboTwin ~76 量级。  
3. **强 RoboTwin 开源主基座**：**Fast-WAM**（~92）；4 卡不声称论文全量复现。  
4. **效率 / adapter / 单次解码**：**Light 可作主轨**（问题分流，非无条件「最终 Fast」）。  
5. **高分 ckpt**：**LingBot-VA**。  
6. **Cosmos VAM**：**DiT4DiT** — 成绩/配方**分层引用**；4×H100 以 eval 为主。  
7. **Track E**：**BWM** 推理审计候选。  
8. **改结构**：StarWAM 或 Fast/Light 上改。  
9. **降权**：BiWM、paper-only 空训练、无协议假排名。

*初版 2026-07-20；Codex #1/#2；**Codex #3（DiT4DiT + §0.6，gpt-5.6-sol xhigh）** 后修订。仅写入本文件。*
