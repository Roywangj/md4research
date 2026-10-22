# 第一部分 · Dream-1 相关论文：末端位姿（EEF）动作空间

> 整理日期：2026-10-22（UTC+8）。正文是一张末端位姿（EEF）动作空间的论文表（26 项），并在文末按表序号逐篇简介。Dream-1 本身是官方博客，不是论文。
> 核验方式：
> - **arXiv**：每个 ID 都打开了 abs 页，核对 `citation_title` 与提交日期；文中日期一律为 **arXiv v1 提交日期**。
> - **GitHub**：每个仓库都用 `git ls-remote` 确认存在，关键仓库还核对了 README 中引用的论文。
> - **项目主页**：用 curl 确认返回 HTTP 200。
>
> 标注约定：
> - 【推断】：整理者的判断，不是原文结论。
> - 【未核实】：没能找到可核对的来源。
> - “无公开代码”：在论文页和项目页都没有找到官方仓库。

---

## ★ 末端位姿（EEF）动作空间相关工作

> 收录**动作空间可核实为末端（位姿）**的工作，按时间排序。同时支持关节与末端的双模式工作（如 π0.5、Fast-WAM、GR00T、ImageWAM、CrossFormer）也列入，并在「动作空间要点」里注明。
>
> 「是否开源」指是否有可用的官方代码仓库；权重许可另注。纯潜动作、纯视频基座、纯仿真 / IK 工具、动作空间【未核实】的条目不列入。

### 末端位姿（EEF / Pose）论文表

| 序号 | 时间 | 工作 | 动作空间要点 | 论文 | 仓库 / 主页 | 是否开源 |
| --- |---|---|---|---|---|---|
| 1 | 2022-12 | RT-1 | 离散化末端增量 | [2212.06817](https://arxiv.org/abs/2212.06817) | [google-research/robotics_transformer](https://github.com/google-research/robotics_transformer) | 是 |
| 2 | 2023-03 | Diffusion Policy | 绝对末端位置 + 6D 旋转 | [2303.04137](https://arxiv.org/abs/2303.04137) | [real-stanford/diffusion_policy](https://github.com/real-stanford/diffusion_policy) | 是 |
| 3 | 2023-06 | LIBERO | 末端增量（基准） | [2306.03310](https://arxiv.org/abs/2306.03310) | [Lifelong-Robot-Learning/LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO) | 是 |
| 4 | 2023-10 | Open X-Embodiment / RT-X | 粗对齐到 7 维末端增量 | [2310.08864](https://arxiv.org/abs/2310.08864) | [google-deepmind/open_x_embodiment](https://github.com/google-deepmind/open_x_embodiment) | 是 |
| 5 | 2023-12 | GR-1 | 末端（CALVIN）【维度未核实】 | [2312.13139](https://arxiv.org/abs/2312.13139) | [bytedance/GR-1](https://github.com/bytedance/GR-1) | 是 |
| 6 | 2024-02 | UMI | 每臂 10 维相对末端（6D） | [2402.10329](https://arxiv.org/abs/2402.10329) | [real-stanford/universal_manipulation_interface](https://github.com/real-stanford/universal_manipulation_interface) | 是 |
| 7 | 2024-02 | Mirage | 笛卡尔 / 末端控制 | [2402.19249](https://arxiv.org/abs/2402.19249) | [项目页](https://robot-mirage.github.io/) | 否（仅项目页） |
| 8 | 2024-05 | Octo | 预训练以末端增量为主 | [2405.12213](https://arxiv.org/abs/2405.12213) | [octo-models/octo](https://github.com/octo-models/octo) | 是 |
| 9 | 2024-06 | OpenVLA | 7 维末端增量 token | [2406.09246](https://arxiv.org/abs/2406.09246) | [openvla/openvla](https://github.com/openvla/openvla) | 是 |
| 10 | 2024-08 | CrossFormer | 含单臂末端读出头 | [2408.11812](https://arxiv.org/abs/2408.11812) | [rail-berkeley/crossformer](https://github.com/rail-berkeley/crossformer) | 是 |
| 11 | 2024-10 | RDT-1B | 统一槽位含末端量 | [2410.07864](https://arxiv.org/abs/2410.07864) | [thu-ml/RoboticsDiffusionTransformer](https://github.com/thu-ml/RoboticsDiffusionTransformer) | 是 |
| 12 | 2024-10 | EgoMimic | 人手与机器人对齐到末端类表示【维度未核实】 | [2410.24221](https://arxiv.org/abs/2410.24221) | [SimarKareer/EgoMimic](https://github.com/SimarKareer/EgoMimic) | 是 |
| 13 | 2025-03 | GR00T N1 / N1.7 | 相对末端（XYZ+ROT6D），可同时预测关节 | [2503.14734](https://arxiv.org/abs/2503.14734) | [NVIDIA/Isaac-GR00T](https://github.com/NVIDIA/Isaac-GR00T) | 是 |
| 14 | 2025-04 | π0.5 | 控制模式 token 可切末端；与关节双模 | [2504.16054](https://arxiv.org/abs/2504.16054) | [Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) | 是 |
| 15 | 2025-07 | TRI LBM | 20 维 UMI 式相对末端 + 6D | [2507.05331](https://arxiv.org/abs/2507.05331) | [项目页](https://toyotaresearchinstitute.github.io/lbm1/) | 否（仅项目页） |
| 16 | 2025-07 | EgoVLA | 预测手腕 / 手部，经 IK 重定向 | [2507.12440](https://arxiv.org/abs/2507.12440) | [项目页](https://rchalyang.github.io/EgoVLA) | 否（仅项目页） |
| 17 | 2025-10 | X-VLA | EE6D 末端 + 本体 soft prompt | [2510.10274](https://arxiv.org/abs/2510.10274) | [2toinf/X-VLA](https://github.com/2toinf/X-VLA) | 是 |
| 18 | 2026-01 | LingBot-VA | 相对末端 + 四元数（RoboTwin 16 维） | [2601.21998](https://arxiv.org/abs/2601.21998) | [Robbyant/lingbot-va](https://github.com/Robbyant/lingbot-va) | 是 |
| 19 | 2026-02 | RDT2 | UMI 式相对末端，动作块 (24, 20) | [2602.03310](https://arxiv.org/abs/2602.03310) | [thu-ml/RDT2](https://github.com/thu-ml/RDT2) | 是 |
| 20 | 2026-02 | LAP | 语言编码的末端增量 | [2602.10556](https://arxiv.org/abs/2602.10556) | [lihzha/lap](https://github.com/lihzha/lap) | 是 |
| 21 | 2026-03 | Fast-WAM | LIBERO 上 7 维末端增量（RoboTwin 另用关节） | [2603.16666](https://arxiv.org/abs/2603.16666) | [yuantianyuan01/FastWAM](https://github.com/yuantianyuan01/FastWAM) | 是 |
| 22 | 2026-04 | MotuBrain | 每末端 10 维相对 + 6D | [2604.27792](https://arxiv.org/abs/2604.27792) | [shengshu-ai/MotuBrain](https://github.com/shengshu-ai/MotuBrain) | 否（仅 README/PDF） |
| 23 | 2026-06 | ImageWAM | 另有 InternData-A1 末端预训练 ckpt | [2606.19531](https://arxiv.org/abs/2606.19531) | [yuyangalin/ImageWAM](https://github.com/yuyangalin/ImageWAM) | 是 |
| 24 | 2026-10 | OpenWAM | 真机 20 维 chunk 相对末端 | [2610.07922](https://arxiv.org/abs/2610.07922) | [OpenWAM/OpenWAM](https://github.com/OpenWAM/OpenWAM) | 是（AGPL） |
| 25 | 2026-10 | 离散 vs 连续动作（Discrete Actions） | 10 维相对末端（双臂 20 维），512 均匀分箱 | [2610.20429](https://arxiv.org/abs/2610.20429) | [项目页](https://iscoyizj.github.io/discrete-action-website/) | 否（代码待发布） |
| 26 | 2026-10 | Dream-1 | 未见本体：末端 + 本机 IK（参数化未披露） | [博客](https://dreamlabs.ai/research/dream-1) | [PyPI API](https://pypi.org/project/dreamlabs-client/) | 否（无权重） |

---

## 各篇简介（按表序号）

> 每篇三句话以内：做了什么、动作空间怎么设、与 Dream-1 的关系。【推断】为整理者判断。

1. **RT-1**（2022-12，Google）：大规模单本体真机 Transformer 策略，动作是离散化的末端增量加底盘和模式位。它是单本体时代的基线，说明末端增量足以支撑大规模真机模仿。
2. **Diffusion Policy**（2023-03）：用扩散模型生成动作块，真机上用绝对末端位置加 6D 旋转，论文指出位置控制对它更有利。它是后来大多数动作头（包括 WAM 的动作分支）的设计基础。
3. **LIBERO**（2023-06）：终身学习与知识迁移的仿真基准，动作是末端增量。它是 WAM 的常用评测基准，Fast-WAM 等在上面用 7 维末端增量；另有 LIBERO-Plus（[2510.13626](https://arxiv.org/abs/2510.13626)）做扰动鲁棒性评测。
4. **Open X-Embodiment / RT-X**（2023-10）：汇集 21 家机构、22 种机器人的数据，RT-X 把动作粗对齐到 7 维末端增量。它是跨本体数据聚合的起点，也是“统一末端增量”这一方案的源头。
5. **GR-1**（2023-12，ByteDance）：先在 Ego4D 上做视频生成预训练，再联合预测未来帧与动作，动作为 CALVIN 设定下的末端（具体维度未核实）。它较早证明了人类视频预训练能帮助操作策略，是 WAM 的前驱之一。
6. **UMI**（2024-02，Stanford / Columbia 等）：手持夹爪加腕部相机采集野外数据，每臂 10 维相对末端（6D 旋转）。对照实验中相对末端 20/20、绝对 5/20、增量 16/20，是相对末端最强的实证；Dream-1 博客致谢了这项腕部相机工作。
7. **Mirage**（2024-02，UC Berkeley）：用笛卡尔（末端）控制并补偿前向动力学，再把未见机器人遮掉、补画成训练时的机器人（cross-painting），实现零样本换臂。它是“末端 + 目标机器人自带控制器”做零样本的早期证据，也提醒外观差异是另一半问题【推断】。
8. **Octo**（2024-05）：在 80 万条 OXE 轨迹上预训练的开源通用策略，预训练以末端增量为主，微调时可换新动作头。它是“跨本体但仍需微调”的代表（LAP 论文没有测 Octo）。
9. **OpenVLA**（2024-06）：7B 开源 VLA，动作是 7 维末端增量 token。在 LAP 的未见本体零样本实验中，这类开源 VLA 的成功率约为 0，是零样本对照的下界。
10. **CrossFormer**（2024-08）：一个策略覆盖操作、导航、四足等多种本体，每个本体一个读出头（单臂用末端，双臂用关节）。它是“本体专属头”方案的代表，这里只列它的末端读出头。
11. **RDT-1B**（2024-10，清华）：面向双臂操作的扩散基础模型，用物理可解释的统一动作空间，关节和末端量各占一个槽位。它是“统一槽位”方案，末端只是其中一部分槽位。
12. **EgoMimic**（2024-10，Georgia Tech）：把人类第一视角数据与机器人数据协同训练，二者对齐到末端类表示（具体维度未核实）。它说明末端空间让人类数据与机器人数据能直接混合训练。
13. **GR00T N1 / N1.7**（2025-03，NVIDIA）：面向人形机器人的开放基础模型。论文用本体专属的状态和动作编码器；仓库中的 N1.7 用相对末端（xyz + 6D 旋转），也可同时预测相对关节，并加入了 EgoScale 人类数据。作者与 DreamZero、Dream Labs 团队有重叠。
14. **π0.5**（2025-04，Physical Intelligence）：在异构数据上协同训练实现开放世界泛化，用控制模式 token 区分关节与末端（π0.5-DROID 用关节速度）。同一模型兼容两种接口，与 Dream-1 的“末端 / 关节双接口”相似【推断】。
15. **TRI LBM**（2025-07，TRI）：对大行为模型做严格的统计评测，动作是 20 维 UMI 式相对末端加 6D 旋转。它是工业级采用相对末端的实证，评测方法也值得借鉴；仅有项目页，未见官方代码。
16. **EgoVLA**（2025-07）：在人类视频上训练 VLA，预测手腕与手部动作，再经 IK 和重定向转成机器人动作，最后用少量机器人示范微调。它是“末端 + IK”接口在人类数据上的版本；仅有项目页。
17. **X-VLA**（2025-10）：用可学习的本体 soft prompt 吸收本体差异，动作是 EE6D 末端。末端加轻量本体条件的组合，是复现 Dream-1 时的候选设计【推断】。
18. **LingBot-VA**（2026-01-29，Robbyant）：因果自回归的视频-动作世界模型，动作是相对末端加四元数，RoboTwin 上 16 维，放在统一的 30 维布局里。它早于 DreamZero 就采用末端动作的 WAM，复现末端接口时可以直接参考。
19. **RDT2**（2026-02）：只用 UMI 手持数据训练，零样本部署到新本体（前提是使用指定的夹爪和相机），动作是 UMI 式相对末端，动作块为 (24, 20)。它和 Dream-1 同为“腕部相机 + 相对末端”的零样本方案，是最接近的开源对照之一。
20. **LAP**（2026-02）：把末端增量编码成语言做预训练，在 3 种单臂机器人上零样本平均成功率超过 50%。开源 VLA 约为 0，作者复现的强基线约为 LAP 的一半；它是显式零样本跨本体的直接同类。
21. **Fast-WAM**（2026-03）：消融表明 WAM 的关键是训练时的视频联合训练，推理时可以跳过视频生成；LIBERO 上用 7 维末端增量，RoboTwin 上用 14 维 qpos。它决定复现时推理路径怎么设计。
22. **MotuBrain**（2026-04，生数科技）：两阶段训练，先只训视频，再做 WAM 训练，动作是每个末端 10 维相对量加 6D 旋转。它是同期采用相对末端的 WAM，但仓库只有 README 和 PDF，无法复现。
23. **ImageWAM**（2026-06）：质疑 WAM 是否需要生成视频，用图像级预测替代；RoboTwin 上用 qpos，另有在 InternData-A1 上做末端预训练的 checkpoint。它说明 2026 年并没有全面转向末端。
24. **OpenWAM**（2026-10）：可组合的开源 WAM 框架，重点是组件可替换，真机上用 20 维 chunk 相对末端。适合作为复现底座【推断】，但论文没有跨本体实验，许可证是 AGPL。
25. **When Do Discrete Actions Make Good Continuous Controllers?**（2026-10-14，Zeji Yi、Guanya Shi 等）：系统比较连续回归、连续流、离散回归、离散流四种动作头，覆盖 RoboMimic 单任务、PaliGemma VLA（RoboCasa / DROID / LIBERO）和真机。结论是最朴素的 512 均匀分箱离散动作也能持平或超过连续动作，瓶颈不在精度，而在跨时间步和维度独立预测带来的分解误差，离散流的迭代计算和 classifier-free guidance 能缓解它（RoboCasa 上 guidance 把离散回归从 27.1% 提到 49.2%）。动作空间消融里，相对末端优于增量和绝对，关节空间与末端空间差距不大。对 Dream-1 的意义是：动作头可以用 LLM 式离散 token，和“取消先验、向 LLM 共识靠拢”的思路一致【推断】；代码和权重尚未发布。
26. **Dream-1**（2026-10，Dream Labs）：只在 YAM 上训练、三相机（头部 + 双腕）输入，对未见本体输出末端位姿 + 夹爪开合，交给机器人自带 IK 执行；原生本体可输出关节角。在 27 个仿真本体和 4 个真机本体上零样本评测（结果以相对 YAM 的比例报告）；没有论文和权重，只有博客与 API，末端的维度、旋转表示、相对还是绝对都未披露。

---

# 第二部分 · 复现 Dream-1 关键性质：开源框架盘点与两条路线建议

---

## 0. 复现目标：Dream-1 官方可核实的性质 vs 未披露项

来源：[Dream-1 官方博客](https://dreamlabs.ai/research/dream-1)（"How zero-shot embodiment generalization works"、"Why does this work?"、评测图注各节）。

| 性质 | 官方原文要点 | 状态 |
|---|---|---|
| 未见本体输出 EEF + 夹爪，由机器人自带 IK 执行 | "it can also predict end-effector (EEF) poses: where each gripper should be and whether it should be open or closed … its own IK solver turns the poses into joint commands" | 已披露 |
| 原生支持的本体输出关节 | "Dream-1 can do the same [joint angles] for the embodiments it supports natively" | 已披露 |
| 三相机布局 | "three cameras: a head view and a wrist view on each arm" | 已披露 |
| 只在一种本体上训练 | "relative to YAM, the robot Dream-1 was actually trained on" | 已披露 |
| 评测规模 | 仿真 27 个未见本体 + 4 台真机。每个仿真本体 300 次 rollout：50 个任务上 150 次测语言跟随，150 个任务上 150 次测未见任务。指标为**相对 YAM 的比值**。真机用的是更早的 checkpoint | 已披露 |
| 适用范围 | "a manipulation policy for bimanual robots with parallel grippers" | 已披露 |
| 自述局限 | 成功率依赖各机 IK 质量；不控制手臂如何到达目标位姿；用 5 分钟本体数据微调（FaaS）仍明显优于零样本 | 已披露 |
| 动作维度、旋转表示、相对/绝对、参考系、模型规模、骨干、仿真平台、训练数据量 | — | **未披露**（无论文、无权重，只有 API 和 PyPI `dreamlabs-client`） |

> 渊源：Dream Labs 由 DreamZero 作者创立，博客称 DreamZero 是 "the paper that introduced World Action Models"。DreamZero 论文（[arXiv:2602.15922](https://arxiv.org/abs/2602.15922)）已做过"AgiBot 预训练 → 30 分钟 YAM play 数据适配"的实验。

---

## 1. 开源框架盘点（截至 2026-10-22）

### 1.1 总表

| 序号  | 名称                                                                                          | 类型                  | 开放权重                                                                                                                                                    | 动作空间（公开实现）                                                                                                | 多本体机制                                                                                              | 视频骨干                                       | 资源需求（官方所述）                                                            |
| --- | ------------------------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------ | --------------------------------------------------------------------- |
| 1   | **DreamZero**（NVIDIA GEAR）[repo](https://github.com/dreamzero0/dreamzero)                   | WAM                 | ✅ [DreamZero-DROID](https://huggingface.co/GEAR-Dreams/DreamZero-DROID)、[DreamZero-AgiBot](https://huggingface.co/GEAR-Dreams/DreamZero-AgiBot)（约 45GB） | **相对关节**（`relative_action: true`，YAM 为左右 joint_pos + gripper，共 14 维）                                      | `CategorySpecificLinear` 按 embodiment_id 分头（`max_num_embodiments=32`），`max_action_dim=32` 补零       | Wan2.1-I2V-14B（另有 Wan2.2-TI2V-5B 选项）       | 推理至少 2 GPU，H100 约 3 s/chunk、GB200 约 0.6 s；训练默认 4 GPU、DeepSpeed ZeRO-2 |
| 2   | **LingBot-VA** [repo](https://github.com/Robbyant/lingbot-va)                               | WAM（自回归）            | ✅ [lingbot-va-base](https://huggingface.co/robbyant/lingbot-va-base)、RoboTwin 和 LIBERO 后训练版                                                             | **EEF**：统一 30 维布局，其中左右 EEF 各 7、左右关节各 7（已发布 ckpt 未使用）、左右夹爪各 1                                              | 30 维通道补零，`used_action_channel_ids` 选通道                                                             | Wan2.2（约 5B DiT）                           | RoboTwin 单卡评测约 24GB（offload）；后训练示例 `NGPU=8`                           |
| 3   | **OpenWAM**（Stanford）[repo](https://github.com/OpenWAM/OpenWAM)                             | WAM 框架              | ⚠️ 只有视频预训练权重 [OpenWAM-Pretraining](https://huggingface.co/OpenWAM-Stanford/OpenWAM-Pretraining)；策略权重 "being prepared"                                   | 相对位姿目标构造器；RoboTwin 适配器支持 `ee` 和 `qpos`                                                                    | 可组合交互程序；跨本体未做实验                                                                                    | Wan2.2-5B（论文 §4）                           | LIBERO 配置在 4×48GB 上实测                                                 |
| 4   | **Motus**（清华）[repo](https://github.com/thu-ml/Motus)                                        | 潜动作 WAM             | ✅ [motus-robotics/*](https://huggingface.co/motus-robotics)                                                                                             | RoboTwin 上为 14 维 qpos；预训练用光流潜动作                                                                           | 六层数据金字塔、三阶段训练                                                                                      | Wan2.2-5B + Qwen3-VL-2B                    | 推理约 41GB；训练 >80GB/卡                                                   |
| 5   | **MotuBrain** [repo](https://github.com/shengshu-ai/MotuBrain)                              | 商用 WAM              | ❌                                                                                                                                                       | 论文：每个末端 10 维相对 EEF                                                                                        | —                                                                                                  | —                                          | —                                                                     |
| 6   | **Fast-WAM** [repo](https://github.com/yuantianyuan01/FastWAM)                              | WAM（测试时不生成视频）       | ✅ [yuanty/fastwam](https://huggingface.co/yuanty/fastwam)（含 `robotwin_uncond_3cam_384.pt`）                                                              | RoboTwin 14 维 qpos；LIBERO 7 维 EEF 增量                                                                      | 无本体条件化                                                                                             | Wan2.2-5B，加 1B action expert，共 6B（论文 §4.1） | LIBERO 单节点 8 GPU；RoboTwin 用 64 GPU（README L388）                       |
| 7   | **ImageWAM** [repo](https://github.com/yuyangalin/ImageWAM)                                 | WAM（图像编辑骨干）         | ✅ 含 [ImageWAM-FLUX.2-4B-InternData-A1-EE](https://huggingface.co/yuyangalin/ImageWAM-FLUX.2-4B-InternData-A1-EE)（**EE 预训练**）                            | RoboTwin qpos；另有 EE 预训练 ckpt                                                                              | —                                                                                                  | FLUX.2-4B 等                                | 未核实                                                                   |
| 8   | **Cosmos Policy**（NVIDIA）[repo](https://github.com/NVlabs/cosmos-policy)                    | 视频模型策略              | ✅ LIBERO / RoboCasa / ALOHA 版                                                                                                                           | 动作作为潜帧注入；ALOHA 本体状态为 14 维关节                                                                               | 每个基准单独训练                                                                                           | Cosmos-Predict2-2B                         | 推理约 6–9GB；训练 8–64×H100×48h（README "System Requirements"）              |
| 9   | **Cosmos3-Nano-Policy-DROID** [HF](https://huggingface.co/nvidia/Cosmos3-Nano-Policy-DROID) | 全模态世界模型策略           | ✅                                                                                                                                                       | 卡片列出按本体固定的维度（如双臂 Franka 20D、UR 10D、UMI 9D）                                                                | 按本体固定维度                                                                                            | Cosmos3                                    | 未细述                                                                   |
| 10  | **UVA** [repo](https://github.com/ShuangLI59/unified_video_action)                          | 视频-动作联合             | ✅（Google Drive：PushT、LIBERO10）                                                                                                                          | 单基准动作                                                                                                     | ❌                                                                                                  | MAR + VAE                                  | 建议至少 4 GPU                                                            |
| 11  | **UWM** [repo](https://github.com/WEIRDLabUW/unified-world-model)                           | 视频-动作扩散             | 未核实                                                                                                                                                     | DROID / robomimic / LIBERO 原生动作                                                                           | 异构数据预训练                                                                                            | 自训                                         | 未说明                                                                   |
| 12  | **GR00T N1.7**（NVIDIA）[repo](https://github.com/NVIDIA/Isaac-GR00T)                         | VLA（无视频生成）          | ✅ [GR00T-N1.7-3B](https://huggingface.co/nvidia/GR00T-N1.7-3B)                                                                                          | **相对 EEF**（XYZ+ROT6D，可与相对关节同时输出）                                                                          | embodiment tag + 按本体的 modality config                                                              | 无（VLM 为 Cosmos-Reason2-2B）                 | 推理 16GB+；微调 40GB+（README L132–134）                                    |
| 13  | **openpi π0 / π0.5** [repo](https://github.com/Physical-Intelligence/openpi)                | VLA                 | ✅                                                                                                                                                       | 按数据集定义；π0.5-DROID 为关节速度                                                                                   | 论文中有 control-mode token，但**公开代码里没检索到**                                                             | 无                                          | 推理 >8GB；LoRA >22.5GB；全参 >70GB（README L26–30）                          |
| 14  | **X-VLA** [repo](https://github.com/2toinf/X-VLA)                                           | VLA                 | ✅ X-VLA-Pt 及各基准版（含 [RoboTwin2](https://huggingface.co/2toINF/X-VLA-RoboTwin2)）                                                                          | 统一 **EE6D**（README §5, L194–201）                                                                          | 按 domain_id 的 soft prompt；新本体需微调                                                                   | 无                                          | 0.9B                                                                  |
| 15  | **RDT2**（清华）[repo](https://github.com/thu-ml/RDT2)                                          | VLA                 | ✅ RDT2-VQ / RDT2-FM                                                                                                                                     | UMI 式 EEF，`(24, 20)` chunk（README L267–268）                                                               | 统一 UMI 夹爪和相机，**零样本**部署到未见本体（README L62），但须使用指定末端和相机（L90）                                           | 无（Qwen2.5-VL-7B）                           | 推理约 16GB；VQ 全参 >80GB                                                  |
| 16  | **LAP** [repo](https://github.com/lihzha/lap)                                               | VLA                 | ✅ [LAP-3B](https://huggingface.co/lihzha/LAP-3B)                                                                                                        | 语言化的末端增量                                                                                                  | 零样本跨本体，平均成功率 >50%（[arXiv:2602.10556](https://arxiv.org/abs/2602.10556)）                            | 无（基于 openpi）                               | GPU 或 TPU 均可训练（README）                                                |
| 17  | **LeRobot** [repo](https://github.com/huggingface/lerobot)                                  | 框架                  | 托管多家权重                                                                                                                                                  | 已集成 `fastwam`、`lingbot_va`、`lawam`、`groot`、`pi05`、`xvla` 等策略；`envs/robotwin.py` 支持 `action_mode=joint/ee` | —                                                                                                  | —                                          | —                                                                     |
| 18  | **RoboTwin 2.0** [repo](https://github.com/RoboTwin-Platform/RoboTwin)                      | 双臂仿真与基准             | 预采集数据（[HF](https://huggingface.co/datasets/TianxingChen/RoboTwin2.0)）                                                                                   | `take_action` 支持 qpos / ee                                                                                | 5 个本体：aloha-agilex、piper、franka-panda、ARX-X5、ur5-wsg（`env_cfg/task_config/_embodiment_config.yml`） | —                                          | —                                                                     |
| 19  | **ManiSkill3** [repo](https://github.com/haosulab/ManiSkill)                                | GPU 并行仿真            | —                                                                                                                                                       | 多数臂提供 `pd_ee_pose` / `pd_ee_delta_pose` 控制器                                                               | PickCube 支持 panda、fetch、xarm6_robotiq、so100、widowxai（`pick_cube.py` L37–43）                        | —                                          | —                                                                     |
| 20  | **robosuite** [repo](https://github.com/ARISE-Initiative/robosuite)                         | 仿真                  | —                                                                                                                                                       | OSC / IK 控制器（`controllers/parts/arm/osc.py`、`ik.py`）                                                      | Panda、Sawyer、IIWA、Jaco、Kinova3、UR5e、xArm7、GR1 等                                                    | —                                          | —                                                                     |
| 21  | **RoboCasa(365)** [repo](https://github.com/robocasa/robocasa)                              | 仿真与基准               | 数据集                                                                                                                                                     | 基于 robosuite                                                                                              | 多机器人【未逐一核实】                                                                                        | —                                          | —                                                                     |
| 22  | **cuRobo** [repo](https://github.com/NVlabs/curobo)                                         | GPU IK / 运动生成       | —                                                                                                                                                       | IK、碰撞感知轨迹优化                                                                                               | 通用（URDF）                                                                                           | —                                          | GPU                                                                   |
| 23  | **mink** [repo](https://github.com/kevinzakka/mink)                                         | 差分 IK（MuJoCo，QP）    | —                                                                                                                                                       | —                                                                                                         | 通用（MJCF）                                                                                           | —                                          | CPU                                                                   |
| 24  | **pink** [repo](https://github.com/stephane-caron/pink)                                     | 差分 IK（Pinocchio，QP） | —                                                                                                                                                       | —                                                                                                         | 通用（URDF）                                                                                           | —                                          | CPU                                                                   |

### 1.2 与复现最相关的事实（逐条来源）

1. **没有哪个开源项目同时具备"视频 WAM + EEF 统一接口 + 单本体训练后零样本跨本体"**。DreamZero 有 WAM 和 YAM 管线，但动作是相对关节；LingBot-VA 有 WAM 和 EEF，但没有报告零样本跨本体实验【未核实，未见相关结果】；LAP 和 RDT2 做到了零样本跨本体，但都不是视频世界模型。
2. **DreamZero 的 YAM 管线与 Dream-1 的相机布局一致**：
   - 三路视频为 `top_camera`、`left_camera`、`right_camera`（`groot/vla/configs/data/dreamzero/base_48_wan_fine_aug_relative.yaml` L267–275）；
   - `scripts/train/yam_training.sh` L9–11 写明 "state 14, action 14, 3 views: top, left, right"；
   - 动作为相对关节（`yam_relative.yaml` L9–15）；
   - README L167 提醒 "Make sure to align the 3 camera view order to ensure positive transfer"。
3. **DreamZero 已有多本体分头机制**：`groot/vla/model/dreamzero/modules/wan_video_dit_action_casual_chunk.py` L31–50 的 `CategorySpecificLinear/MLP`，以及 `wan_flow_matching_action_tf.py` L131 的 `max_num_embodiments=32`。这适合实现"原生本体走关节头"。
4. **LingBot-VA 自带"EEF + 关节"双通道布局**：README L280–287 定义了 30 维（左右 EEF 各 7、左右关节各 7、左右夹爪各 1）。LeRobot 文档说明关节通道 "unused by the released checkpoints"，RoboTwin 只用 `[0–6, 28, 7–13, 29]` 共 16 维，经 CuRobo IK 执行（`docs/source/lingbot_va.mdx` L131–147）。
5. **GR00T N1.7 已经做到"EEF 与关节同时预测"**：DROID 预训练配置里，`eef_9d` 为 RELATIVE / EEF / XYZ_ROT6D，`joint_position` 为 RELATIVE / NON_EEF，夹爪为 ABSOLUTE（`gr00t/configs/data/embodiment_configs.py` L28–58）。README L90–92 称相对 EEF "is a key factor in the model's cross-embodiment performance"，并用了 20K 小时 EgoScale 人类视频。但它**不是视频生成模型**，新本体仍要后训练（README L68）。
6. **Fast-WAM 论文给出了"视频共训练 vs 测试时想象"的对照**（[arXiv:2603.16666](https://arxiv.org/abs/2603.16666) §3.3、§4.3.2）：
   - RoboTwin 上 Fast-WAM 91.8%，Fast-WAM-Joint 90.6%，Fast-WAM-IDM 91.3%，去掉视频共训练降到 83.8%；
   - 真机叠毛巾去掉视频共训练只剩 10%；
   - 这些都是**单本体、分布内**的结论。
7. **RoboTwin 2.0 的预采集数据覆盖 4 个本体**：以 `adjust_bottle` 为例，有 `aloha-agilex`、`arx-x5`、`franka`、`ur5` 四个本体的 `_clean_50.zip` 和 `_randomized_500.zip`（HF 目录 `dataset/<task>/`）。仓库还有 piper 资产，但该任务没有 piper 预采集包。RoboTwin README 把 "cross-embodiment performance" 列为推荐研究方向（README "Experiment & LeaderBoard" 节）。
8. **LeRobot 的 RoboTwin 环境默认 aloha-agilex**：`src/lerobot/envs/robotwin.py` L245 注明 "Uses aloha-agilex … by default"；`ACTION_DIM = 14`（L53）是写死的，`EEF_ACTION_DIM = 16`（L56）；ee 模式下把动作当作相对 episode 初始 EEF 的增量（L486–489）。换成 franka（7+7 关节）时 joint 模式维度不匹配，ee 模式理论上可用【推断，需实测】。

---

## 2. 路线 A：基于成熟框架

### 2.1 推荐：以 **LingBot-VA** 为主干，DreamZero 作为"真机 YAM 线"的备选

**选 LingBot-VA 的理由（逐条来源）：**
- 它是唯一已开源、**原生输出 EEF** 的视频-动作 WAM，在 RoboTwin 上走 `ee` 加 CuRobo IK（LeRobot `lingbot_va.mdx` L80–84、L144–147），与 Dream-1 "EEF + 本体 IK" 的接口一致。
- 30 维布局里预留了关节通道（README L280–287），可直接实现 Dream-1 式的"未见本体走 EEF，原生本体走关节"【推断：需自己加关节监督，已发布的 ckpt 未用这些通道】。
- 代码和权重都是 Apache-2.0，base 权重公开；LeRobot 已集成训练和评测（`lingbot_va.mdx` "Training / fine-tuning" 节，24–32GB 单卡需 LoRA）。
- 约 5B 参数，比 DreamZero 的 14B 便宜（DreamZero README 写的是至少 2 GPU 推理，H100 约 3 s/chunk）。

**DreamZero 作为备选的场景**：如果真机目标就是 YAM，DreamZero 现成的 YAM 配置（三相机、相对关节、embodiment 分头）最接近 Dream-1 团队的起点（同一批作者，博客自述），但需要**新增 EEF 动作键**（README "Adding a New Embodiment" → `docs/DATASET_TO_GEAR_AND_TRAIN.md` Step 3/4）。另外 DROID 权重是 CC-BY-NC-4.0，商用需改从 AgiBot 权重（Apache-2.0）起步。

**为什么不选 VLA 类作为主干【推断】**：GR00T N1.7、X-VLA、RDT2、LAP 都没有视频世界模型分支，而 Dream-1 博客把零样本能力主要归功于"video is the one representation every robot type shares"。不过它们很适合作**对照基线**，尤其 RDT2 和 LAP 都声称零样本跨本体。

### 2.2 具体计划
1. **基线复现**：用 LeRobot `lerobot/lingbot_va_robotwin` 在 RoboTwin aloha-agilex 的 `ee` 模式下复现成绩（`lingbot_va.mdx` L86–93 命令），确认 CuRobo 和 IK 链路正常。
2. **单本体训练**：从 `lingbot_va_base` 起，只用**一个**本体（如 aloha-agilex）的 RoboTwin 数据后训练 EEF 通道。
   - 数据需映射成 30 维格式，见 README L287。
   - 统一采用**相对 chunk 起点**的 EEF，降低世界系、基座位置差异的影响。LingBot-VA 原实现相对 episode 首帧，见 `lerobot_latent_dataset.py` L62–64；chunk 相对是否更好属【推断】，需要做消融。
3. **零样本评测**：在 arx-x5、franka、ur5 上用 `ee` 模式零样本评测（RoboTwin 预采集数据覆盖这 3 个本体，评测本身只需仿真资产）。按 Dream-1 的方式报告"相对训练本体的成功率比"。
4. **加关节头（原生本体）**：用训练本体的 qpos 填充 30 维中的关节通道（14–27），联合监督。推理时按本体选择通道。对照 GR00T 的同时监督做法（`embodiment_configs.py` L28–58）。
5. **真机**：如需 YAM，用 DreamZero 的 YAM 管线采集格式，三相机为 top/left/right（`yam_training.sh` L9–11），并转换成 EEF。

### 2.3 风险
- LingBot-VA 预训练数据的本体构成，会影响"只训一个本体"实验是否干净（base 已见过多本体）。这一点【未核实】；严格复现时要说明这是"预训练后单本体后训练"，不是 Dream-1 式的"只在 YAM 上训练"。
- RoboTwin 的 endpose 在**世界系**下，以 wxyz 四元数表示（RoboTwin 配置文档）。不同本体基座位置和 TCP 定义不同，直接迁移可能出现系统偏差【推断】。
- RoboTwin 的 `ee` 执行是逐步规划（CuRobo 或 mplib，依本体配置而定），规划失败会被计入策略失败。必须按 4.5 节的规范区分"策略错误 / 执行错误"（出自原文档，属方法论建议）。
- LingBot-VA 自回归推理较慢（视频约 20 步、动作约 50 步去噪，`lingbot_va.mdx` "Model Overview"），大规模评测成本高。
- OpenWAM 是 AGPL-3.0，如果借用其代码（如相对位姿构造器），衍生代码通过网络提供服务时须开源。

---

## 3. 路线 B：基于 Fast-WAM（FastWAM @7faa711）

### 3.1 要改什么（文件 / 行号）
| 项 | 现状（来源） | 改法 |
|---|---|---|
| **数据：EEF 重导出** | 训练读预处理好的 LeRobot 数据 `yuanty/robotwin2.0-fastwam`（14 维 qpos）；仓库没有 RoboTwin 转换脚本（`configs/data/robotwin.yaml` L3–4、L16–23） | 从 RoboTwin 原始 HDF5（`data_type.endpose: true`；endpose 为 wxyz、世界系）重导出 20 维 chunk-relative EEF（xyz + rot6d + 夹爪）×2。可参考 RoboTwin README 的 XPolicyLab LeRobot 转换脚本 |
| **配置** | `action_output_dim` / `proprio_output_dim: 14`（train L39–40，val L102–103），`shape_meta` 14（L16–23、L79–86），`pretrained_norm_stats`（L31、L94） | 全部改为 20；train 侧 stats 设为 null 让主进程重算，val 必须指向新文件（`robot_video_dataset.py` L99–101） |
| **模型层** | `ActionDiT.action_encoder`（`action_dit.py` L73）、`head`（L97）、`proprio_encoder`（`fastwam.py` L60）；`load_checkpoint` 对 mot 用 strict=False，对 proprio 用 strict=True（L1214–1222） | 从 `robotwin_uncond_3cam_384.pt` 继承时删除 `mixtures.action.action_encoder.*`、`mixtures.action.head.*`、`proprio_encoder`（见修订稿 4.3 步骤三） |
| **本体条件化** | 没有 embodiment id | 【推断】先**不加**：Dream-1 的设定是单本体训练、未见本体零样本，用不上 id。做多本体扩展时可仿照 DreamZero 的 `CategorySpecificLinear` |
| **相机布局** | `concat_multi_camera: "robotwin"` 要求恰好 3 路：头部 256×320 在上，左右腕各 128×160 拼在下方，合成 384×320（`robot_video_dataset.py` L168–192） | 已与 Dream-1 的"头 + 双腕"一致。注意腕部分辨率较低，跨本体时腕部外观差异会被放大还是被抹平，【推断】需要消融 |
| **多本体数据** | `dataset_dirs` 是列表（`robotwin.yaml` L3–4） | 跨本体训练时可列多个目录；但 Dream-1 式实验**只放一个本体** |
| **部署 / IK** | `deploy_policy.py` L238 读 qpos，L292 执行 `take_action(..., "qpos")` | 改为读 `endpose`，还原绝对位姿后调用 `take_action(ee_action, action_type="ee")`（16 维，wxyz，世界系）；真机用 mink 或 pink 做差分 IK |
| **测试时视频** | 默认 `infer_action` 只做一次前向，不生成未来视频（`fastwam.py` L979）；`infer_joint` 会同时生成视频，并对比两者动作差异（L771–792、L966–971）；另有 `configs/model/fastwam_joint.yaml`、`fastwam_idm.yaml` 变体 | 用这几个现成变体做"测试时想象"消融 |
| **"无视频"消融** | 总损失为 `loss_lambda_video * loss_video + loss_lambda_action * loss_action`（`fastwam.py` L603），`loss_lambda_video` 默认 1.0（L39） | 设 `loss_lambda_video=0` 即为论文 §3.3 的 "without video co-training" 对照 |
| **算力** | RoboTwin 官方训练用 64 GPU（README L388） | 最小实验减少任务数和步数【推断】 |

### 3.2 路线 B 的特有风险
- **核心风险：Fast-WAM 测试时跳过视频，而 Dream-1 依赖视频先验。**
  - Fast-WAM 的结论（测试时想象作用有限、视频共训练才关键，论文 §4.3.2）只在**分布内、单本体**上验证过；
  - Dream-1 博客的论点是"WAM 预测机器人将呈现的样子，因此能控制陌生本体"（"Why does this work?" 节）；
  - 对未见本体，测试时生成未来视频是否带来额外收益，**目前没有公开证据**【推断】。最小实验必须包含 Fast-WAM-Joint / IDM 对照。
- 没有大规模多本体视频预训练：Fast-WAM 直接从 Wan2.2-5B 起步（论文 §4.1），而 Dream-1 的训练数据量未披露。单本体训练的零样本上限可能很低【推断】。
- 只开源了 qpos 版 RoboTwin 权重，EEF 版要从头后训练，且官方配方用 64 GPU。
- 好处：MIT 许可、代码结构清晰、已有修订稿里的改造细节；LeRobot 也有 `policy.type=fastwam` 封装（`docs/source/fastwam.mdx`），可以复用 LeRobot 的 RoboTwin 环境和评测。

---

## 4. 最小可验证实验：在两条路线之间做判定

**目标**：用最少算力回答三个问题：
- 只训一个本体、输出 EEF 的 WAM，能否在其他本体上零样本跑通；
- 视频共训练的贡献有多大；
- 测试时想象的贡献有多大。

### 4.1 设定
- **平台**：RoboTwin 2.0（MIT）。三相机（cam_high、左右腕）与 Dream-1 布局一致，且有 `ee` 执行接口。
- **训练本体**：aloha-agilex（只用这一个）。
- **零样本本体**：arx-x5、franka、ur5（RoboTwin 预采集数据覆盖这 3 个本体，这里只用来作评测参照；评测只需仿真资产）。
- **任务**：取 5–10 个**单臂或简单**任务（如 adjust_bottle、click_bell、beat_block_hammer），用 clean_50 数据【推断：先简单任务，与 LAP / Dream-1 博客展示的简单任务量级相当】。
- **动作**：每臂 xyz + rot6d + 夹爪，chunk-relative（左右共 20 维）。部署时还原到世界系，用 wxyz 四元数送入 `take_action(..., "ee")`。
- **指标**：成功率，以及 Dream-1 式的"相对训练本体成功率比"。失败分为"策略错误"和"执行错误"（规划或 IK 失败、超限）。每组至少 100 次 rollout【推断】。

### 4.2 实验组
| 组 | 配置 | 回答的问题 | 实现位置 |
|---|---|---|---|
| E1 | Fast-WAM，EEF，`loss_lambda_video=1`，`infer_action` | 主方法：零样本能否跨本体 | 路线 B 改造 |
| E2 | 同 E1，但 `loss_lambda_video=0` | **"只用 EEF、不用视频"消融**（Dream-1 未做） | `fastwam.py` L603 |
| E3 | Fast-WAM-Joint 或 IDM，EEF | 测试时想象在**跨本体**上是否重要 | `configs/model/fastwam_joint.yaml` / `fastwam_idm.yaml` |
| E4 | 原版 qpos（14 维） | 关节空间上界和对照；franka 维度不同，无法直接迁移 | 现有 ckpt `robotwin_uncond_3cam_384.pt` |
| E5 | LingBot-VA，EEF，同样只用 aloha-agilex 后训练 | 路线 A 的同条件对比 | LeRobot `lingbot_va` |
| E6（可选） | 只用腕部相机 vs 三相机 | 检验 Dream-1 "头部相机 + 视频"的论点 | 改 `shape_meta.images` |

### 4.3 判定规则【推断】
- **E1 明显好于 E2**（视频共训练对零样本跨本体有贡献），且 **E5 ≥ E1**：选**路线 A**。成熟框架的自回归视频推理和 EEF 原生接口更有利。
- **E1 ≈ E5**，且 **E3 ≈ E1**（测试时想象无额外收益）：选**路线 B**，延迟更低、许可更宽（MIT）、改造可控。
- **E1 ≈ E2 ≈ 0**：说明仅靠单本体加 RoboTwin 规模不足以零样本迁移，瓶颈在数据和预训练规模，换框架没用。应转向多本体或人类视频预训练（GR00T N1.7 用了 20K 小时人类视频，README L92），或先做 Dream-1 式的少量本体微调（博客 FaaS 节：5 分钟数据即有提升）。
- **执行错误占比 > 30%**：先修 IK 和规划链路（TCP 对齐、基座系转换），再比较模型。

### 4.4 落地前必须先验证的前提
1. RoboTwin 预采集 HDF5 是否含 `endpose` 字段【未核实】。若没有，需用 `collect_data.sh` 加 `data_type.endpose: true` 重新采集（RoboTwin README "Collect data yourself"）。
2. 各本体的 `cam_high` 是否在同一世界位置和视角【未核实】。若头部相机随本体变化，"跨本体"会混入视角差异。
3. 各本体在 `ee` 模式下用哪种规划器（CuRobo 还是 mplib），以及是否支持 7 自由度的 franka 冗余解【未核实】。
4. LeRobot `envs/robotwin.py` 能否切换到非 aloha 本体（L245、L260–275 的 embodiment 解析逻辑存在，但默认值和 `ACTION_DIM=14` 写死）【推断：需小改】。

---

## 5. 结论
1. **当前（2026-10-22）没有开箱即用的"Dream-1 等价物"**。最接近的组件分散在几处：
   - DreamZero：WAM、YAM 三相机、embodiment 分头，但动作是关节；
   - LingBot-VA：WAM，原生 EEF + 30 维含关节通道；
   - GR00T N1.7：相对 EEF 与关节同时预测，加人类视频，但没有视频生成；
   - RDT2 / LAP：零样本跨本体，但不是 WAM；
   - RoboTwin 2.0：5 本体双臂仿真，带 ee 和 IK 接口。
2. **建议顺序**：先跑第 4 节的最小实验（E1–E5，以 Fast-WAM 为主、LingBot-VA 为对照，都能通过 LeRobot 统一评测），再按 4.3 的规则定路线。实验前先核实 4.4 的四个前提。
3. 无论选哪条路线，**IK 和执行层都是零样本成败的关键变量（量化占比无公开数据）**。Dream-1 官方也承认 "Performance depends on the quality of each robot's IK solver"。必须把执行失败从策略失败中剥离出来。
