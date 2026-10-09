---
title: "Learning 4D Geometric Priors for Inference-Efficient World Action Models"
authors: Jianjun Zhang; Jian Zhu; Taiyi Su; Chong Ma; Zitai Huang; Yi Xu; Hanli Wang
year: 2026
source_pdf: "/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/VFAT5V4G/Zhang 等 - 2026 - Learning 4D Geometric Priors for Inference-Efficient World Action Models.pdf"
source_pages: 9
reader_mode: complete bilingual reader
---

# Learning 4D Geometric Priors for Inference-Efficient World Action Models

# 为推理高效世界动作模型学习四维几何先验

## 阅读索引

- p.1：摘要、引言（前半）与 Fig. 1
- p.2：引言（后半）、相关工作
- p.3：方法：问题形式化、多专家协同训练与 Eq. (1)–(5)，Fig. 2
- p.4：混合注意力、衰减式四维读掩码与蒸馏定义，Eq. (6)–(19)，Fig. 3–4
- p.5：训练目标、实验设置与 Eq. (20)–(23)
- p.6：LIBERO / RoboTwin 2.0 主结果，Table 1–2
- p.7：真实机器人结果、消融与结论，Fig. 5–6、Table 3–4
- pp.8–9：完整作者—年份参考文献（42 条；原文未编号）

## 摘要

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> World Action Models (WAMs) have shown strong potential for robotic manipulation by jointly modeling visual future dynamics and executable action sequences. However, existing video-action co-training methods primarily optimize appearance-oriented video latents, which may insufficiently capture the temporally evolving geometry required for precise manipulation. We propose MECo-WAM, a Multi-Expert Co-Training World Action Model that injects action-relevant 4D geometric priors into video-action representations while preserving the original lightweight inference graph. During training, MECo-WAM combines video and action experts with a lightweight 4D expert supervised by relational targets from a frozen VGGT encoder. Asymmetric expert visibility prevents non-causal shortcuts from auxiliary geometry to action generation. To transfer geometric knowledge into the deployed video-action pathway, we introduce decayed 4D read-mask attention, which provides restricted current-frame geometric guidance early in training and progressively removes this dependency. We further propose action-aware temporal geometric distillation, which aligns within-frame geometric relations and their temporal evolution while emphasizing visual regions most relevant to robot actions. At deployment, all auxiliary 4D components are removed. Experiments on LIBERO (98.2%), RoboTwin 2.0 (92.6%), and challenging real-world manipulation tasks show that MECo-WAM improves manipulation performance without increasing inference cost.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 世界动作模型（WAM）通过联合建模视觉未来动态与可执行动作序列，已展现出用于机器人操作的强大潜力。然而，现有视频—动作协同训练方法主要优化面向外观的视频潜变量，可能不足以捕获精确操作所需、随时间演化的几何结构。本文提出 MECo-WAM：一种多专家协同训练世界动作模型；它将与动作相关的四维几何先验注入视频—动作表征，同时保留原有的轻量级推理图。训练时，MECo-WAM 将视频专家和动作专家与轻量级四维专家结合；该专家由冻结 VGGT 编码器给出的关系目标监督。非对称专家可见性可阻止辅助几何通往动作生成的非因果捷径。为将几何知识迁移至部署的视频—动作路径，本文提出衰减式四维读掩码注意力：它在训练早期提供受限的当前帧几何引导，并逐步移除这一依赖。本文还提出动作感知时序几何蒸馏，在强调与机器人动作最相关视觉区域的同时，对齐帧内几何关系及其时序演化。部署时，所有辅助四维组件均被移除。在 LIBERO（98.2%）、RoboTwin 2.0（92.6%）和具有挑战性的真实操作任务上的实验表明，MECo-WAM 能在不增加推理成本的情况下提升操作性能。

### Fig. 1. MECo-WAM 的效率—成功率比较

![Fig. 1](WorldModel/Learning%204D%20Geometric%20Priors%20for%20Inference-Efficient%20World%20Action%20Models/assets/fig1.png)

**Caption:** Figure 1: Comparison of MECo-WAM with Baselines in action-chunk inference latency and task success rate on RoboTwin.

**Caption[CN]:** 图 1：MECo-WAM 与基线方法在 RoboTwin 上的动作块推理延迟和任务成功率对比。

**Reading note:** 该散点图将动作块延迟与成功率同时呈现；MECo-WAM 的标注为 $(198.73, 92.6)$，且部署图不引入辅助四维路径。

## 引言

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Robotic manipulation requires a policy to map visual observations and language instructions to precise action trajectories (Hu et al. 2025; Ma et al. 2026; Su et al. 2026; Wang et al. 2026; Su et al. 2025). World action models offer a promising formulation by jointly learning how visual states evolve under interaction and how robot actions should be generated (Ye et al. 2026c; Kim et al. 2026; Bi et al. 2026; Li et al. 2026b). Compared with direct action policies, video-action co-training can provide richer motion and interaction priors, enabling the policy to reason over changes that unfold beyond a single observation (Ye et al. 2026a; Yuan et al. 2026).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 机器人操作要求策略将视觉观测和语言指令映射为精确的动作轨迹（Hu et al. 2025；Ma et al. 2026；Su et al. 2026；Wang et al. 2026；Su et al. 2025）。世界动作模型通过联合学习视觉状态如何在交互中演化以及机器人动作应如何生成，提供了一种有前景的形式化方案（Ye et al. 2026c；Kim et al. 2026；Bi et al. 2026；Li et al. 2026b）。相较于直接动作策略，视频—动作协同训练能提供更丰富的运动和交互先验，使策略可推理超出单次观测而逐步展开的变化（Ye et al. 2026a；Yuan et al. 2026）。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Despite this advantage, the visual representation learned by many WAMs remains dominated by appearance-oriented video prediction. A video latent can support plausible future synthesis without explicitly preserving the spatial relations that determine whether a grasp is reachable, whether an object is aligned with a target, or whether contact will cause a stable transition. These relations are not static: they evolve as the robot approaches, contacts, moves, and releases objects. Recent geometry-aware VLA and WAM studies therefore introduce 3D or 4D structure to strengthen spatial grounding for manipulation (Qu et al. 2025; Li et al. 2025a,b; Guo et al. 2026; Li et al. 2026c). Thus, manipulation-oriented WAMs require geometry-aware temporal representations beyond visual plausibility.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 尽管具有这一优势，许多 WAM 学到的视觉表征仍受面向外观的视频预测主导。视频潜变量可以支持看似合理的未来合成，却不必显式保留决定抓取是否可达、物体是否与目标对齐、或接触是否引发稳定状态转移的空间关系。这些关系并非静态：它们会随机器人接近、接触、移动和释放物体而演化。因此，近期几何感知 VLA 与 WAM 研究引入三维或四维结构，以增强操作的空间落地能力（Qu et al. 2025；Li et al. 2025a,b；Guo et al. 2026；Li et al. 2026c）。由此，面向操作的 WAM 需要超越视觉合理性的、几何感知的时序表征。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> A direct approach is to introduce explicit 4D reconstruction or dense geometric prediction into the world action modeling pipeline (Guo et al. 2026; Li et al. 2026c). However, making geometry an explicit deployment-time output increases inference cost and may shift optimization toward geometric reconstruction that is only weakly coupled with action generation. More importantly, generic geometric supervision may overlook action-relevant relations among manipulated objects, target regions, and their temporal interactions.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 一种直接做法是在世界动作建模流水线中引入显式四维重建或稠密几何预测（Guo et al. 2026；Li et al. 2026c）。但将几何作为部署时的显式输出会增加推理成本，并可能将优化导向与动作生成耦合较弱的几何重建。更重要的是，通用几何监督可能忽略被操作物体、目标区域及其时序交互之间与动作相关的关系。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> We therefore ask a focused question: can a world action model acquire action-relevant temporal geometry during training while retaining the same lightweight video-action inference graph at deployment? Our answer is MECo-WAM, a Multi-Expert Co-Training World Action Model. MECo-WAM adds a lightweight 4D expert only during training, where frozen VGGT features supervise temporal geometric prediction alongside video and action denoising. Rather than allowing unrestricted cross-expert communication, the deployed video-action pathway receives only restricted current-frame geometric guidance during early training, while future geometry remains loss-side supervision. This design transfers 4D priors without creating non-causal shortcuts or adding inference-time cost. As shown in Figure 1, this design achieves a strong task success rate on RoboTwin 2.0 while keeping action-chunk inference latency low.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 因此，本文聚焦一个问题：世界动作模型能否在训练中获得与动作相关的时序几何，同时在部署时保留相同的轻量级视频—动作推理图？答案是 MECo-WAM，即多专家协同训练世界动作模型。MECo-WAM 仅在训练时增加轻量级四维专家；冻结的 VGGT 特征与视频、动作去噪一起监督时序几何预测。部署的视频—动作路径并不允许无约束的跨专家通信，而仅在训练早期接收受限的当前帧几何引导；未来几何仍只通过损失进行监督。这一设计传递四维先验，却不产生非因果捷径或额外推理成本。如图 1 所示，它在保持低动作块推理延迟的同时，在 RoboTwin 2.0 上获得了很高的任务成功率。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> To transfer geometry without a permanent 4D dependency, we introduce decayed 4D read-mask attention, which exposes only the current-frame geometry token early in training and removes this access before deployment. We further propose action-aware temporal geometric distillation, aligning predicted 4D keyframes and their temporal relation changes with frozen VGGT targets while emphasizing action-relevant token pairs.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 为在不形成永久四维依赖的情况下传递几何知识，本文提出衰减式四维读掩码注意力：它只在训练早期暴露当前帧几何令牌，并在部署前移除该访问。本文进一步提出动作感知时序几何蒸馏：在强调动作相关令牌对的同时，使预测的四维关键帧及其时序关系变化与冻结 VGGT 目标对齐。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Our contributions are fourfold: (i) MECo-WAM injects action-aware 4D geometric priors into WAM representations while preserving the original lightweight inference graph; (ii) decayed 4D read-mask attention supplies early geometric guidance and progressively removes dependence on 4D tokens before deployment; (iii) action-aware temporal geometric distillation aligns within-frame relations and their evolution while emphasizing action-relevant visual regions, enabling task-conditioned geometry learning; and (iv) experiments on LIBERO, RoboTwin 2.0, and real-world manipulation demonstrate consistent gains in task success and execution efficiency.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 本文贡献有四点：（i）MECo-WAM 向 WAM 表征注入动作感知四维几何先验，同时保留原始轻量级推理图；（ii）衰减式四维读掩码注意力提供早期几何引导，并在部署前逐步去除对四维令牌的依赖；（iii）动作感知时序几何蒸馏对齐帧内关系及其演化，并强调动作相关视觉区域，从而支持任务条件化的几何学习；（iv）LIBERO、RoboTwin 2.0 和真实机器人操作实验展示了任务成功率和执行效率的一致提升。

## 相关工作

### 世界动作模型

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> World action models bridge two complementary embodied learning paradigms: policies that map observations and instructions to executable actions, and world models that predict how the environment evolves under interaction. Direct VLA policies, including the $\pi$ model family and OpenVLA, provide strong reactive observation-to-action baselines. Recent WAMs adapt pretrained video priors or unified multimodal architectures to jointly model future observations, latent dynamics, and action chunks. DreamZero, Mimic-Video, Cosmos Policy, Motus, and LingBot-VA show that video-based temporal supervision can improve policy learning beyond direct behavior cloning by exposing the model to physical evolution and action-conditioned scene changes.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 世界动作模型连接两种互补的具身学习范式：将观测和指令映射为可执行动作的策略，以及预测环境如何在交互下演化的世界模型。包括 $\pi$ 模型家族和 OpenVLA 在内的直接 VLA 策略提供了强有力的反应式观测到动作基线。近期 WAM 调整预训练视频先验或统一多模态架构，以联合建模未来观测、潜在动态和动作块。DreamZero、Mimic-Video、Cosmos Policy、Motus 和 LingBot-VA 表明，基于视频的时序监督可通过使模型接触物理演化和动作条件化场景变化，将策略学习推进到直接行为克隆之外。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Some systems improve practical execution through causal attention, multi-chunk prediction, caching, asynchronous denoising, or action-centered interfaces. Fast-WAM makes this deployment-oriented view explicit: future video prediction remains useful during training, while test-time action generation can proceed without explicit future imagination. MECo-WAM follows this efficient WAM principle but studies a different source of supervision. Rather than adding rollout to the deployed policy, it uses a training-only 4D expert to transfer action-relevant temporal geometry into the shared video-action representation. The inference graph therefore remains the same lightweight observation-to-action path used by the base WAM.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 一些系统通过因果注意力、多动作块预测、缓存、异步去噪或以动作为中心的接口提升实际执行。Fast-WAM 明确了这一部署导向观点：未来视频预测在训练时仍有用，而测试时动作生成可在不显式进行未来想象的情况下进行。MECo-WAM 遵循这一高效 WAM 原则，但研究不同的监督来源。它不向部署策略添加轨迹展开，而是使用仅训练期的四维专家，将与动作相关的时序几何传递到共享的视频—动作表征中。因此，其推理图仍是基础 WAM 使用的同一轻量级观测到动作路径。

### 几何感知具身模型

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Geometry-aware embodied models improve manipulation by injecting 3D structure through depth, point clouds, spatial priors, or representation alignment. In VLA models, 3D-VLA connects 3D perception, reasoning, and action through a generative world model. SpatialVLA studies spatial representations for action prediction, BridgeVLA aligns 3D inputs and heatmap-style outputs in a shared 2D space, 3DS-VLA introduces 3D spatial constraints for robust multi-task manipulation, and GeoVLA strengthens VLA policies with explicit 3D representations. Recent variants further improve robustness or data efficiency through diverse point clouds, lightweight spatiotemporal dynamics, manipulation data beyond action labels, spatial foundation priors, predictive kinematics with 3D Gaussian geometry, and spatially guided training. Spatial Forcing further shows that spatial foundation priors can be transferred into VLA representations through implicit spatial alignment.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 几何感知具身模型通过深度、点云、空间先验或表征对齐注入三维结构，从而改善操作。对 VLA 模型而言，3D-VLA 经由生成式世界模型连接三维感知、推理与动作；SpatialVLA 研究用于动作预测的空间表征；BridgeVLA 在共享二维空间中对齐三维输入和热图式输出；3DS-VLA 为鲁棒多任务操作引入三维空间约束；GeoVLA 用显式三维表征增强 VLA 策略。近期变体则借助多样点云、轻量时空动态、超越动作标签的操作数据、空间基础先验、带三维高斯几何的预测运动学和空间引导训练，进一步提高鲁棒性或数据效率。Spatial Forcing 还显示，空间基础先验可通过隐式空间对齐迁移至 VLA 表征。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In the WAM setting, geometry has begun to move from direct policy inputs into future prediction and video-action co-training. X-WAM unifies action execution with 4D world synthesis by predicting multi-view RGB-D futures, adding a lightweight depth branch to a pretrained video diffusion backbone, and using asynchronous denoising for efficient action decoding. WAM4D studies fast 4D world action modeling with spatial register tokens and future-depth readouts, then removes the register branch for action inference. MECo-WAM follows this geometry-for-WAM direction but differs in where geometry lives: it treats frozen VGGT 4D structure as a training-time representation constraint, uses decayed read-mask attention to avoid permanent dependence, and transfers temporal geometry into the lightweight video-action path rather than requiring explicit 4D reconstruction during deployment.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在 WAM 场景中，几何已经开始从直接策略输入转移到未来预测和视频—动作协同训练。X-WAM 通过预测多视角 RGB-D 未来、在预训练视频扩散骨干上添加轻量深度分支、并采用异步去噪实现高效动作解码，从而统一动作执行与四维世界合成。WAM4D 以空间寄存器令牌和未来深度读出研究快速四维世界动作建模，随后在动作推理时移除寄存器分支。MECo-WAM 遵循这一“为 WAM 引入几何”的方向，但其区别在于几何存在的位置：它将冻结 VGGT 的四维结构视为训练期表征约束，以衰减读掩码注意力避免永久依赖，并将时序几何传递入轻量级视频—动作路径，而非在部署时要求显式四维重建。

## 方法

### 问题形式化

### Fig. 2. MECo-WAM 概览

![Fig. 2](WorldModel/Learning%204D%20Geometric%20Priors%20for%20Inference-Efficient%20World%20Action%20Models/assets/fig2.png)

**Caption:** Figure 2: Overview of MECo-WAM. The left side illustrates the training process, while the right side shows the inference process. During training, video frames are encoded by the VAE for video denoising, while current and future frames are encoded by a frozen VGGT encoder to provide targets for 4D geometry denoising. The 4D expert takes $g_0$, $g_1$, $g_2$, and $g_h$ as input slots, predicts $g_{p1}$, $g_{p2}$, and $g_{ph}$, and applies keyframe 4D losses on selected predictions. Decayed 4D read-mask attention transfers early current-frame geometric guidance to the video-action pathway. At inference, only the original video and action experts remain.

**Caption[CN]:** 图 2：MECo-WAM 概览。左侧展示训练过程，右侧展示推理过程。训练时，视频帧经 VAE 编码以进行视频去噪；当前帧与未来帧则经由冻结 VGGT 编码器编码，为四维几何去噪提供目标。四维专家以 $g_0$、$g_1$、$g_2$ 和 $g_h$ 为输入槽位，预测 $g_{p1}$、$g_{p2}$ 和 $g_{ph}$，并在选定预测上施加关键帧四维损失。衰减式四维读掩码注意力将早期当前帧几何引导传递到视频—动作路径。推理时，仅保留原始视频专家和动作专家。

**Reading note:** 图左是三专家训练图，图右是移除四维专家后的原始视频—动作推理图。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Figure 2 gives an overview of MECo-WAM. Let $o_0$ denote the current visual observation, $a_0$ the current robot-state/proprioceptive context, $\ell$ a language instruction, and $a_{1:H}$ an action chunk of horizon $H$. The deployed policy models

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 图 2 给出 MECo-WAM 的概览。令 $o_0$ 表示当前视觉观测，$a_0$ 表示当前机器人状态／本体感觉上下文，$\ell$ 表示语言指令，$a_{1:H}$ 表示视界为 $H$ 的动作块。部署的策略建模为

$$
p_\theta(a_{1:H}\mid o_0,a_0,\ell). \tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> During training, the model observes visual trajectories and action chunks, and the base video-action pathway learns future visual dynamics together with action denoising. MECo-WAM adds a lightweight 4D expert only for training, using frozen VGGT features from current and future frames as geometric supervision. This auxiliary path constrains the shared representation through relational 4D losses, while the deployed policy remains an observation-to-action model.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 训练时，模型观测视觉轨迹和动作块，基础视频—动作路径同时学习未来视觉动态与动作去噪。MECo-WAM 仅为训练增加轻量级四维专家，使用来自当前和未来帧的冻结 VGGT 特征作为几何监督。该辅助路径通过关系式四维损失约束共享表征，而部署策略仍是观测到动作模型。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Our design principle is that 4D geometry serves as a training-time representation constraint rather than an inference-time input or output. At deployment, the 4D expert, frozen VGGT encoder, and alignment modules are removed, preserving the original observation-to-action interface.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 本文的设计原则是：四维几何是训练期表征约束，而非推理期输入或输出。部署时，移除四维专家、冻结 VGGT 编码器和对齐模块，从而保留原始观测到动作接口。

### 多专家协同训练架构

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Expert tokens.** The video expert uses the clean first-frame VAE token as visual context and denoises noisy future VAE target slots. Let $\bar Y_v=[\bar f_1,\bar f_2,\bar f_h]$ denote the clean future VAE targets. For flow-matching time $r$, we construct noisy future slots

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **专家令牌。** 视频专家使用干净的首帧 VAE 令牌作为视觉上下文，并对有噪的未来 VAE 目标槽位去噪。令 $\bar Y_v=[\bar f_1,\bar f_2,\bar f_h]$ 表示干净的未来 VAE 目标。对流匹配时间 $r$，构造有噪未来槽位

$$
[f_1,f_2,f_h]=(1-r)\bar Y_v+r\epsilon_v,\qquad X_v=[f_0,f_1,f_2,f_h],
$$
$$
[f_{p1},f_{p2},f_{ph}]=E_v(X_v,r;\ell). \tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Here $f_{p1}$, $f_{p2}$, and $f_{ph}$ are predicted future video outputs supervised against $\bar Y_v$ through the video loss. The action expert uses the same noise-slot convention, with $a_0$ serving as a clean robot-state/proprioceptive anchor rather than a prediction target. Let $\bar Y_a=[\bar a_1,\bar a_2,\bar a_h]$ denote clean future action targets:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 其中，$f_{p1}$、$f_{p2}$ 和 $f_{ph}$ 是相应的未来视频预测输出，并通过视频损失相对 $\bar Y_v$ 进行监督。动作专家采用同样的噪声槽位约定，其中 $a_0$ 是干净的机器人状态／本体感觉锚点，而非预测目标。令 $\bar Y_a=[\bar a_1,\bar a_2,\bar a_h]$ 表示干净的未来动作目标：

$$
[a_1,a_2,a_h]=(1-r)\bar Y_a+r\epsilon_a,\qquad X_a=[a_0,a_1,a_2,a_h],
$$
$$
[a_{p1},a_{p2},a_{ph}]=E_a(X_a,r;f_0,\ell). \tag{3}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The 4D expert uses the same denoising convention, but obtains tokens from a frozen VGGT encoder instead of the VAE. Given current and future RGB frames, frozen VGGT produces clean geometry targets $g_0$ and $\bar Y_g=[\bar g_1,\bar g_2,\bar g_h]$. The current geometry token remains clean, while future geometry slots are noisy:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 四维专家使用同样的去噪约定，但令牌来自冻结的 VGGT 编码器而非 VAE。给定当前和未来 RGB 帧，冻结 VGGT 产生干净几何目标 $g_0$ 与 $\bar Y_g=[\bar g_1,\bar g_2,\bar g_h]$。当前几何令牌保持干净，而未来几何槽位带噪：

$$
[g_1,g_2,g_h]=(1-r)\bar Y_g+r\epsilon_g,\qquad X_{4d}=[g_0,g_1,g_2,g_h],
$$
$$
[g_{p1},g_{p2},g_{ph}]=E_{4d}(X_{4d},r). \tag{4}
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The 4D objective is applied only on selected keyframe predictions. Let $\mathcal K\subseteq\{1,2,h\}$ denote selected keyframe indices. Clean VGGT targets $G_\mathcal K$ are used only for training losses and never become input to the deployed policy.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 四维目标仅施加于选定的关键帧预测。令 $\mathcal K\subseteq\{1,2,h\}$ 表示选定的关键帧索引。干净 VGGT 目标 $G_\mathcal K$ 仅用于训练损失，绝不成为部署策略的输入。

$$
\widehat G_{\mathcal K}=\{g_{pk}\mid k\in\mathcal K\},\qquad G_{\mathcal K}=\{\bar g_k\mid k\in\mathcal K\}. \tag{5}
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The mixed-attention sequence is $X=[X_v,X_a,X_{4d}]$. At each transformer layer, expert $e\in\{v,a,4d\}$ has separate query, key, and value projections. After concatenating expert-specific tensors, masked mixed attention produces $Y$, where $M$ is an expert-level attention mask. The mask defines the information paths allowed during co-training.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 混合注意力序列为 $X=[X_v,X_a,X_{4d}]$。在每个 Transformer 层中，专家 $e\in\{v,a,4d\}$ 都有独立的查询、键和值投影。拼接专家特定张量后，带掩码混合注意力产生 $Y$；其中 $M$ 是专家级注意力掩码。该掩码定义协同训练期间允许的信息路径。

$$
X=[X_v,X_a,X_{4d}]. \tag{6}
$$
$$
Q_e=X_eW_e^Q,\qquad K_e=X_eW_e^K,\qquad V_e=X_eW_e^V. \tag{7}
$$
$$
Y=\operatorname{softmax}\left(\frac{QK^\top}{\sqrt d}+M\right)V. \tag{8}
$$

### 衰减式四维读掩码注意力

### Fig. 3. 衰减式读掩码注意力

![Fig. 3](WorldModel/Learning%204D%20Geometric%20Priors%20for%20Inference-Efficient%20World%20Action%20Models/assets/fig3.png)

**Caption:** Figure 3: Decayed read-mask attention. Rows and columns denote query and key slots. Hatched cells are temporary reads from future video/action queries to current geometry $g_0$; white cells are masked. Future 4D slots are auxiliary training targets, and all 4D tokens are removed at inference.

**Caption[CN]:** 图 3：衰减式读掩码注意力。行和列分别表示查询与键槽位。斜线单元格表示未来视频／动作查询对当前几何 $g_0$ 的临时读取；白色单元格被掩码。未来四维槽位是辅助训练目标，推理时移除所有四维令牌。

**Reading note:** $g_0$ 只由当前 RGB 帧编码，故临时读取不会泄露未来信息；未来四维槽位仅留在辅助分支。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> MECo-WAM introduces decayed 4D read-mask attention to preserve video-geometry co-training benefits while decoupling the 4D path at inference. The mask prevents future-information shortcuts: current anchors $f_0$, $a_0$, and $g_0$ are self-only; future video tokens read the video branch but not action tokens; and future action tokens read clean visual context plus the action branch, but not noisy future video slots. MECo-WAM then adds temporary read edges from future video/action queries to the current-frame geometry token $g_0$, which is safe because it is encoded from the current RGB frame only. Future 4D slots stay inside the 4D branch and serve only as auxiliary prediction targets.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> MECo-WAM 引入衰减式四维读掩码注意力，以在保留视频—几何协同训练收益的同时，于推理时解耦四维路径。该掩码避免未来信息捷径：当前锚点 $f_0$、$a_0$ 和 $g_0$ 仅能读取自身；未来视频令牌读取视频分支但不读取动作令牌；未来动作令牌读取干净视觉上下文和动作分支，但不读取有噪未来视频槽位。随后，MECo-WAM 增加从未来视频／动作查询到当前帧几何令牌 $g_0$ 的临时读取边；它只由当前 RGB 帧编码，因此是安全的。未来四维槽位留在四维分支内部，仅作为辅助预测目标。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Figure 3 visualizes the proposed visibility mask and the decayed 4D attention edges used only during training. The read edges are stochastic and decay over optimization. Let $s$ be the optimization step and let $\gamma_s$ indicate whether the $g_0$ read edges are active:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 图 3 可视化了所提出的可见性掩码和仅在训练期间使用的衰减四维注意力边。这些读取边是随机的，并随优化而衰减。令 $s$ 为优化步，$\gamma_s$ 表示 $g_0$ 读取边是否激活：

$$
\gamma_s\sim\operatorname{Bernoulli}(p_{4d}(s)). \tag{9}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The activation probability follows a linear decay. The read edges are present only when $\gamma_s=1$. This schedule exposes the video-action path to current-frame geometry early in training and gradually removes the auxiliary dependency. At deployment, $p_{\mathrm{end}}=0$, no 4D tokens are instantiated, and the original video-action graph is recovered.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 激活概率遵循线性衰减。读取边仅在 $\gamma_s=1$ 时存在。该调度在训练早期将视频—动作路径暴露给当前帧几何，并逐步去除辅助依赖。部署时，$p_{\mathrm{end}}=0$，不实例化四维令牌，并恢复原始视频—动作图。

$$
p_{4d}(s)=\begin{cases}p_{\mathrm{start}}+(p_{\mathrm{end}}-p_{\mathrm{start}})\dfrac{s}{S_{\mathrm{decay}}},&s<S_{\mathrm{decay}},\\p_{\mathrm{end}},&s\ge S_{\mathrm{decay}}.\end{cases} \tag{10}
$$

### 动作感知时序几何蒸馏

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The distillation objective uses frozen VGGT as a geometry teacher, but supervises only predictions of the training-time 4D expert. Its mechanism has three parts. First, relation matching transfers 3D layout without requiring student and teacher to share an absolute feature coordinate system. Second, action-aware weights identify visual tokens most coupled with contemporaneous robot motion, so the loss focuses on manipulated objects, targets, and contact regions. Third, temporal relation matching teaches how these action-relevant relations change across keyframes, capturing approach, contact, transport, and release dynamics rather than only static scene geometry.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 该蒸馏目标以冻结 VGGT 为几何教师，但只监督训练期四维专家的预测。其机制有三部分。第一，关系匹配在不要求学生和教师共享绝对特征坐标系的情况下传递三维布局。第二，动作感知权重识别与同时刻机器人运动耦合最强的视觉令牌，因此损失聚焦于被操作物体、目标和接触区域。第三，时序关系匹配学习这些动作相关关系如何跨关键帧变化，从而捕获接近、接触、搬运和释放动态，而不仅是静态场景几何。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **VGGT-aligned geometry.** For selected keyframes $k\in\mathcal K$, student geometry features are $Z^k=P_{\mathrm{align}}(g_{pk})$; frozen VGGT supplies the clean target $G_T^k=\bar g_k$. Geometry is represented by pairwise feature relations. Valid entries of each relation matrix are normalized before alignment, yielding $\widehat R_{4d}^k$ and $\widehat R_T^k$. Relational matching avoids an assumed shared absolute feature coordinate system and focuses supervision on relative object–gripper–target structure.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **VGGT 对齐几何。** 对选定关键帧 $k\in\mathcal K$，学生几何特征为 $Z^k=P_{\mathrm{align}}(g_{pk})$；冻结 VGGT 给出干净目标 $G_T^k=\bar g_k$。几何由成对特征关系表示。对齐前，对每个关系矩阵的有效条目进行归一化，得到 $\widehat R_{4d}^k$ 和 $\widehat R_T^k$。关系匹配避免假定存在共享绝对特征坐标系，并将监督集中于相对的物体—夹爪—目标结构。

$$
Z^k=P_{\mathrm{align}}(g_{pk}),\quad k\in\mathcal K. \tag{11}
$$
$$
R_{4d}^k(i,j)=\lVert Z_i^k-Z_j^k\rVert_2^2,\qquad R_T^k(i,j)=\lVert G_{T,i}^k-G_{T,j}^k\rVert_2^2. \tag{12}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Action-aware weights.** Not all visual regions contribute equally to a given action. Let $v_i^k$ be a selected video token and $\bar a^k$ a pooled action representation aligned to the same temporal segment. The learned relevance $r_i^k$ is mixed with a uniform prior; $\eta$ prevents collapse onto one location. The pair weight is $w_{ij}^k=\sqrt{w_i^kw_j^k}$.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **动作感知权重。** 并非所有视觉区域都对给定动作有同等贡献。令 $v_i^k$ 是选定视频令牌，$\bar a^k$ 是与同一时序片段对齐的池化动作表征。学习到的相关性 $r_i^k$ 与均匀先验混合；$\eta$ 防止塌缩到单一位置。令牌对权重为 $w_{ij}^k=\sqrt{w_i^kw_j^k}$。

$$
s_i^k=\frac{(W_vv_i^k)^\top(W_a\bar a^k)}{\tau\lVert W_vv_i^k\rVert_2\lVert W_a\bar a^k\rVert_2},\qquad r_i^k=\operatorname{softmax}_i(s_i^k). \tag{13}
$$
$$
w_i^k=N\left((1-\eta)r_i^k+\frac{\eta}{N}\right),\qquad w_{ij}^k=\sqrt{w_i^kw_j^k}. \tag{14}
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The within-frame loss is a weighted average of the absolute discrepancy between normalized student and teacher relation matrices. This weighting makes the 4D loss action-conditioned: high-relevance tokens contribute more strongly to pairwise geometry, while the uniform mixture preserves useful scene context.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 帧内损失是归一化学生与教师关系矩阵之间绝对差异的加权平均。这一加权使四维损失受动作条件化：高相关令牌对成对几何贡献更强，而均匀混合保留有用的场景上下文。

$$
\mathcal L_{\mathrm{geo}}^{\mathrm{act}}=\frac{\sum_{k\in\mathcal K,i,j}w_{ij}^k\left|\widehat R_{4d}^k(i,j)-\widehat R_T^k(i,j)\right|}{\sum_{k\in\mathcal K,i,j}w_{ij}^k}. \tag{15}
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Temporal geometry.** Manipulation also depends on how geometry changes. For consecutive selected keyframe pairs $(k,k^+)\in\mathcal A_\mathcal K$, the method defines normalized relation change, adjacent-frame pair weights, a discrepancy $D_{ij}^{k,k^+}$ between student and teacher changes, and the temporal loss. This objective complements static relation matching by supervising how action-relevant geometry evolves between keyframes.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **时序几何。** 操作还取决于几何如何变化。对连续选定关键帧对 $(k,k^+)\in\mathcal A_\mathcal K$，该方法定义归一化关系变化、相邻帧令牌对权重、学生与教师变化之间的差异 $D_{ij}^{k,k^+}$，以及时序损失。该目标通过监督动作相关几何如何在关键帧之间演化，补充静态关系匹配。

$$
\Delta(R_k,R_{k^+})=\frac{R_{k^+}-R_k}{|R_{k^+}|+|R_k|+\epsilon}. \tag{16}
$$
$$
w_{ij}^{k,k^+}=\sqrt{w_{ij}^kw_{ij}^{k^+}}. \tag{17}
$$
$$
D_{ij}^{k,k^+}=\left|\Delta(\widehat R_{4d}^k,\widehat R_{4d}^{k^+})-\Delta(\widehat R_T^k,\widehat R_T^{k^+})\right|. \tag{18}
$$
$$
\mathcal L_{\mathrm{tem}}^{\mathrm{act}}=\frac{\sum_{(k,k^+)\in\mathcal A_\mathcal K,i,j}w_{ij}^{k,k^+}D_{ij}^{k,k^+}}{\sum_{(k,k^+)\in\mathcal A_\mathcal K,i,j}w_{ij}^{k,k^+}}. \tag{19}
$$

### Fig. 4. 共享视频—动作表征的深度探测

![Fig. 4](WorldModel/Learning%204D%20Geometric%20Priors%20for%20Inference-Efficient%20World%20Action%20Models/assets/fig4.png)

**Caption:** Figure 4: Depth probing of shared video-action representations. A matched DPT-style head is trained on tokens from the final four layers of Fast-WAM or MECo-WAM. The improved MECo-WAM depth structure indicates that 4D co-training enriches the deployed video-action representation. Pseudo-GT depth maps are generated by VDA (Chen et al. 2025).

**Caption[CN]:** 图 4：共享视频—动作表征的深度探测。对 Fast-WAM 或 MECo-WAM 最后四层的令牌训练匹配的 DPT 风格头。MECo-WAM 改进的深度结构表明，四维协同训练丰富了部署的视频—动作表征。伪真值深度图由 VDA（Chen et al. 2025）生成。

**Reading note:** 探测头不使用辅助四维令牌；该图意在检验几何先验是否转移进部署路径。

### 训练目标与推理

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The video and action experts follow the conditional flow-matching objective of the base WAM. For target $y$, Gaussian noise $\epsilon$, and interpolation time $r$, the method constructs $y_r=(1-r)y+r\epsilon$ and optimizes $\mathcal L_{\mathrm{FM}}(y)$. Instantiating this loss for future video latents and action chunks yields $\mathcal L_{\mathrm{video}}$ and $\mathcal L_{\mathrm{action}}$.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 视频和动作专家遵循基础 WAM 的条件流匹配目标。对于目标 $y$、高斯噪声 $\epsilon$ 和插值时间 $r$，方法构造 $y_r=(1-r)y+r\epsilon$，并优化 $\mathcal L_{\mathrm{FM}}(y)$。将此损失实例化到未来视频潜变量和动作块，得到 $\mathcal L_{\mathrm{video}}$ 与 $\mathcal L_{\mathrm{action}}$。

$$
y_r=(1-r)y+r\epsilon. \tag{20}
$$
$$
\mathcal L_{\mathrm{FM}}(y)=\mathbb E_{y,\epsilon,r}\left[\lVert u_\theta(y_r,r,o_0,a_0,\ell)-(\epsilon-y)\rVert_2^2\right]. \tag{21}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The 4D objective and total objective are given below. During training, MECo-WAM uses the auxiliary 4D expert, frozen VGGT encoder, and decayed read mask; these components are removed at inference, leaving only the original video and action experts. Thus, MECo-WAM adds no geometric decoder, sensor input, or extra denoising stage to the deployed policy. Figure 4 further suggests that the training-time 4D objective transfers geometric priors into the WAM representation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 四维目标和总目标如下。训练期间，MECo-WAM 使用辅助四维专家、冻结 VGGT 编码器和衰减读掩码；推理时移除这些组件，仅留下原始视频与动作专家。因此，MECo-WAM 未向部署策略增加几何解码器、传感器输入或额外去噪阶段。图 4 还表明，训练期四维目标将几何先验转移到了 WAM 表征中。

$$
\mathcal L_{4d}=\alpha_{\mathrm{geo}}\mathcal L_{\mathrm{geo}}^{\mathrm{act}}+\alpha_{\mathrm{tem}}\mathcal L_{\mathrm{tem}}^{\mathrm{act}}. \tag{22}
$$
$$
\mathcal L_{\mathrm{total}}=\lambda_{\mathrm{video}}\mathcal L_{\mathrm{video}}+\lambda_{\mathrm{action}}\mathcal L_{\mathrm{action}}+\lambda_{4d}\mathcal L_{4d}. \tag{23}
$$

## 实验

### 实验设置

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Implementation details.** MECo-WAM uses Wan2.2-TI2V-5B as the video backbone and follows the Fast-WAM observation-to-action deployment interface. The action expert uses 30 DiT blocks, 24 attention heads, 128-dimensional heads, and hidden width $d_a=1024$ (about 1B parameters). The auxiliary 4D expert uses $d_{4d}=512$ (about 0.45B parameters), with supervision from a frozen VGGT-1B encoder. Decayed 4D read probability decreases linearly from 1.0 to 0 over the first half of training, and final-layer VGGT/MECo-WAM tokens are used for relational alignment.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **实现细节。** MECo-WAM 使用 Wan2.2-TI2V-5B 作为视频骨干，并遵循 Fast-WAM 的观测到动作部署接口。动作专家使用 30 个 DiT 块、24 个注意力头、128 维头与隐藏宽度 $d_a=1024$（约 10 亿参数）。辅助四维专家采用 $d_{4d}=512$（约 4.5 亿参数），由冻结 VGGT-1B 编码器监督。衰减四维读取概率在训练前半程从 1.0 线性降至 0；关系对齐采用最终层 VGGT/MECo-WAM 令牌。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Each training chunk contains 33 robot steps, corresponding to action horizon $H=32$ and 9 video frames under a $4\times$ action-to-video temporal ratio. The authors use continuous flow matching with 1000 training timesteps and shift 5.0, AdamW with learning rate $1\times10^{-4}$, weight decay 0.01, cosine decay, bfloat16 mixed precision, and gradient clipping at 1.0. Training is conducted on 64 NVIDIA H20 96GB GPUs. Inference uses 10 denoising steps with CFG scale 1.0 on one NVIDIA RTX 5090 32GB GPU; real-world experiments use an ARX-R5 arm.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 每个训练块含 33 个机器人步，对应于 $4\times$ 动作到视频时间比下动作视界 $H=32$ 与 9 个视频帧。作者使用连续流匹配、1000 个训练时间步和 5.0 的 shift；优化器为 AdamW，学习率 $1\times10^{-4}$、权重衰减 0.01、余弦衰减、bfloat16 混合精度与 1.0 梯度裁剪。训练在 64 张 NVIDIA H20 96GB GPU 上进行。推理在一张 NVIDIA RTX 5090 32GB GPU 上使用 10 步去噪、CFG scale 1.0；真实实验使用 ARX-R5 机械臂。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Benchmarks.** MECo-WAM is evaluated on LIBERO, RoboTwin 2.0, and real-world tabletop manipulation. Simulation follows the Fast-WAM evaluation configuration. LIBERO has Spatial, Object, Goal, and Long suites, each with 10 tasks and 500 expert demonstrations. RoboTwin 2.0 evaluates bimanual manipulation under clean and randomized conditions, where randomization changes object poses, appearances, clutter, illumination, and tabletop layouts. Real-world evaluation stacks three sponge cubes vertically and sorts three cubes into a size-ordered line, reporting success rate, progress rate, correction count, and completion time under an identical camera setup and execution budget.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **基准。** MECo-WAM 在 LIBERO、RoboTwin 2.0 和真实桌面操作上评估。仿真遵循 Fast-WAM 评测配置。LIBERO 包含 Spatial、Object、Goal 和 Long 四个套件，各有 10 个任务和 500 条专家演示。RoboTwin 2.0 在干净与随机化条件下评估双臂操作；随机化会改变物体姿态、外观、杂乱程度、照明和桌面布局。真实评估包括将三个海绵立方体垂直堆叠、及将三个立方体按尺寸排成一线；在相同相机配置和执行预算下报告成功率、进度率、纠正次数与完成时间。

### 主要结果

### Table 1. LIBERO 成功率（%）

![Table 1](WorldModel/Learning%204D%20Geometric%20Priors%20for%20Inference-Efficient%20World%20Action%20Models/assets/table1.png)

**Caption:** Table 1: LIBERO success rates (%). Spat./Obj./Avg. denote Spatial/Object/Average; P.T. denotes embodied-policy pre-training; bold/underline denote best/second-best.

**Caption[CN]:** 表 1：LIBERO 成功率（%）。Spat./Obj./Avg. 分别表示 Spatial/Object/Average；P.T. 表示具身策略预训练；粗体／下划线表示最佳／次佳。

| 方法 | Spat. | Obj. | Goal | Long | Avg. |
|---|---:|---:|---:|---:|---:|
| $\pi_0$ | 96.8 | 98.8 | 95.8 | 85.2 | 94.1 |
| $\pi_0$ + FAST | 96.4 | 96.8 | 88.6 | 60.2 | 85.5 |
| OpenVLA | 94.4 | 88.4 | 79.2 | 53.7 | 76.5 |
| OpenVLA-OFT | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 |
| DD-VLA | 97.2 | 96.6 | 97.4 | 92.0 | 96.3 |
| Uni-VLA | 95.4 | 98.8 | 93.6 | 94.0 | 95.4 |
| X-VLA | 98.2 | 98.6 | 97.8 | 97.6 | 98.1 |
| LingBot-VA (P.T.) | 98.5 | 99.6 | 97.2 | 98.5 | 98.5 |
| Motus (P.T.) | 96.8 | 99.8 | 96.6 | 97.6 | 97.7 |
| Fast-WAM (w/o P.T.) | 98.2 | 100.0 | 97.0 | 95.2 | 97.6 |
| MECo-WAM (w/o P.T.) | 98.8 | 100.0 | 98.2 | 95.8 | 98.2 |

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **LIBERO.** Table 1 compares MECo-WAM with VLA policies and WAM-style models. Without embodied-policy pretraining, MECo-WAM reaches 98.2% average success, improving over Fast-WAM by 0.6 points and Motus by 0.5 points, while remaining close to the pretrained LingBot-VA result (98.5%). Gains are most apparent on geometry-sensitive suites: MECo-WAM obtains 98.8% on Spatial, 100.0% on Object, and 98.2% on Goal, improving Fast-WAM by 0.6 points on Spatial, matching it on Object, and adding 1.2 points on Goal. These results suggest that action-aware 4D co-training mainly strengthens spatial and object-centric reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **LIBERO。** 表 1 将 MECo-WAM 与 VLA 策略和 WAM 风格模型比较。在没有具身策略预训练的情况下，MECo-WAM 达到 98.2% 的平均成功率，较 Fast-WAM 高 0.6 个百分点、较 Motus 高 0.5 个百分点，同时接近预训练 LingBot-VA 的 98.5%。增益在几何敏感套件上最明显：MECo-WAM 在 Spatial、Object 和 Goal 上分别获得 98.8%、100.0% 和 98.2%，相对 Fast-WAM 在 Spatial 高 0.6 点、在 Object 持平、在 Goal 高 1.2 点。这些结果表明，动作感知四维协同训练主要增强空间和以物体为中心的推理。

### Table 2. RoboTwin 2.0 成功率（%）

![Table 2](WorldModel/Learning%204D%20Geometric%20Priors%20for%20Inference-Efficient%20World%20Action%20Models/assets/table2.png)

**Caption:** Table 2: RoboTwin 2.0 success rates (%) under clean and randomized evaluation. P.T. denotes embodied-policy pre-training.

**Caption[CN]:** 表 2：干净和随机化评估下的 RoboTwin 2.0 成功率（%）。P.T. 表示具身策略预训练。

| 方法 | P.T. | Clean | Rand. | Average |
|---|:---:|---:|---:|---:|
| $\pi_{0.5}$ | ✓ | 82.74 | 76.76 | 79.75 |
| X-VLA | ✓ | 72.80 | 72.84 | 72.82 |
| Motus | ✓ | 88.66 | 87.02 | 87.84 |
| LingBot-VA | ✓ | 92.90 | 91.50 | 92.20 |
| Fast-WAM | ✗ | 91.88 | 91.78 | 91.83 |
| MECo-WAM | ✗ | 93.26 | 91.98 | 92.62 |

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **RoboTwin 2.0.** Table 2 reports aggregate success and compares with $\pi_{0.5}$. MECo-WAM obtains the best overall average, improving non-pretrained Fast-WAM from 91.83% to 92.62% while keeping the same inference-time video-action graph. The clean-setting improvement is 93.26% versus 91.88% (+1.38 points), and the randomized improvement is 91.98% versus 91.78% (+0.20 points). MECo-WAM also slightly surpasses the strongest pretraining-based WAM average in the table, LingBot-VA (92.62% versus 92.20%), indicating that training-time 4D supervision can make a non-pretrained WAM competitive without deployment geometry modules.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **RoboTwin 2.0。** 表 2 报告汇总成功率，并额外与 $\pi_{0.5}$ 比较。MECo-WAM 获得最佳总体平均值：在保持相同推理期视频—动作图的同时，将未预训练 Fast-WAM 的 91.83% 提高到 92.62%。干净设置中为 93.26% 对 91.88%（+1.38 点），随机化设置中为 91.98% 对 91.78%（+0.20 点）。MECo-WAM 还略超表中最强预训练 WAM LingBot-VA 的平均值（92.62% 对 92.20%），表明训练期四维监督可使未预训练 WAM 在不部署几何模块的情况下具备竞争力。

### 真实世界评估与表征探测

### Fig. 5. 真实机器人桌面实验

![Fig. 5](WorldModel/Learning%204D%20Geometric%20Priors%20for%20Inference-Efficient%20World%20Action%20Models/assets/fig5.png)

**Caption:** Figure 5: Representative real-robot tabletop experiments on cube stacking and size-based cube sorting.

**Caption[CN]:** 图 5：立方体堆叠和基于尺寸的立方体排序的代表性真实机器人桌面实验。

**Reading note:** 图中任务指令分别是“竖直堆叠三个海绵立方体”和“按尺寸将三个立方体排成一线”。

### Table 3. 两项真实桌面任务的结果

![Table 3](WorldModel/Learning%204D%20Geometric%20Priors%20for%20Inference-Efficient%20World%20Action%20Models/assets/table3.png)

**Caption:** Table 3: Real-world tabletop results on two tasks (SR/PR/CR/CT: success rate/progress rate/correction count/completion time).

**Caption[CN]:** 表 3：两项真实世界桌面任务结果（SR/PR/CR/CT：成功率／进度率／纠正次数／完成时间）。

| 任务 | 方法 | SR（Test 1/2/n/Avg） | PR（Test 1/2/n/Avg） | CR（Test 1/2/n/Avg） | CT（Test 1/2/n/Avg） |
|---|---|---|---|---|---|
| Stack Cubes | $\pi_0$ | 0/100/0/40.0 | 50/100/50/55.0 | –/1/–/0.75 | –/32.62/–/25.98 |
| Stack Cubes | Fast-WAM | 100/0/100/60.0 | 100/50/100/75.0 | 3/–/2/1.67 | 28.15/–/30.65/27.06 |
| Stack Cubes | MECo-WAM | 100/0/100/60.0 | 100/50/100/75.0 | 0/–/1/0.83 | 25.69/–/29.62/25.71 |
| Sort Cubes by Size | $\pi_0$ | 100/0/100/40.0 | 100/50/100/60.0 | 1/–/1/1.50 | 22.88/–/25.04/30.82 |
| Sort Cubes by Size | Fast-WAM | 100/100/100/60.0 | 100/100/100/75.0 | 0/4/0/1.33 | 26.03/57.94/25.23/38.49 |
| Sort Cubes by Size | MECo-WAM | 100/100/100/70.0 | 100/100/100/80.0 | 0/2/3/1.00 | 26.35/28.15/55.47/31.96 |

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Real-world evaluation.** The tabletop study evaluates Stack Cubes and Sort Cubes by Size with representative rollouts in Figure 5. On Stack Cubes, MECo-WAM matches Fast-WAM in SR/PR (60.0%/75.0%) but reduces corrections from 1.67 to 0.83 and completion time from 27.06s to 25.71s. On Sort Cubes by Size, it improves Fast-WAM from 60.0% to 70.0% SR and from 75.0% to 80.0% PR, while reducing corrections from 1.33 to 1.00 and time from 38.49s to 31.96s. Across both tasks, it gains 5.0 SR points and 2.5 PR points over Fast-WAM, with about 39% fewer corrections and 12% shorter completion time.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **真实世界评估。** 桌面研究评估 Stack Cubes 和 Sort Cubes by Size，代表性轨迹见图 5。在 Stack Cubes 上，MECo-WAM 的 SR/PR 与 Fast-WAM 相同（60.0%/75.0%），但将纠正次数从 1.67 降至 0.83，完成时间从 27.06s 缩短至 25.71s。在 Sort Cubes by Size 上，它将 Fast-WAM 的 SR 从 60.0% 提升至 70.0%、PR 从 75.0% 提升至 80.0%，并将纠正次数从 1.33 降至 1.00、时间从 38.49s 降至 31.96s。跨两个任务，相对 Fast-WAM，平均 SR 增加 5.0 点、PR 增加 2.5 点，纠正约少 39%，完成时间约短 12%。

### Fig. 6. 抓取期间的三维位置和姿态敏感性

![Fig. 6](WorldModel/Learning%204D%20Geometric%20Priors%20for%20Inference-Efficient%20World%20Action%20Models/assets/fig6.png)

**Caption:** Figure 6: 3D position and pose sensitivity during real-robot grasping. MECo-WAM better preserves action-relevant cube position, grasp pose, and contact geometry.

**Caption[CN]:** 图 6：真实机器人抓取期间的三维位置和姿态敏感性。MECo-WAM 更好地保持与动作相关的立方体位置、抓取姿态和接触几何。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Representation probing.** With the video-action backbone frozen, a matched DPT-style head on tokens from the final four layers shows sharper depth for MECo-WAM (Figure 4). The grasp comparison in Figure 6 further shows stronger sensitivity to action-relevant 3D position and pose. Both probes exclude auxiliary 4D tokens, indicating that geometry transfers into deployed video-action features.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **表征探测。** 在冻结视频—动作骨干后，使用最终四层令牌的匹配 DPT 风格头显示 MECo-WAM 的深度更清晰（图 4）。图 6 的抓取比较进一步显示其对动作相关三维位置和姿态更敏感。两种探测均排除辅助四维令牌，说明几何已经迁移到部署的视频—动作特征。

### 消融研究

### Table 4. RoboTwin 消融结果

![Table 4](WorldModel/Learning%204D%20Geometric%20Priors%20for%20Inference-Efficient%20World%20Action%20Models/assets/table4.png)

**Caption:** Table 4: Ablation results on RoboTwin.

**Caption[CN]:** 表 4：RoboTwin 上的消融结果。

| Variant | PSNR ↑ | SSIM ↑ | LPIPS ↓ | MSE ($\times10$) ↓ | Avg SR ↑ |
|---|---:|---:|---:|---:|---:|
| Fast-WAM | 29.55 | 0.936 | 0.038 | 0.032 | 91.83 |
| + 4D expert | 29.81 | 0.935 | 0.039 | 0.034 | 91.87 |
| + decayed read | 30.06 | 0.939 | 0.038 | 0.026 | 92.14 |
| + $\mathcal L_{\mathrm{geo}}^{\mathrm{act}}$ | 29.97 | 0.938 | 0.037 | 0.022 | 92.22 |
| + $\mathcal L_{\mathrm{tem}}^{\mathrm{act}}$ | 30.42 | 0.940 | 0.039 | 0.019 | 92.25 |
| Full w/o aware | 30.31 | 0.942 | 0.038 | 0.017 | 92.38 |
| MECo-WAM | 30.72 | 0.942 | 0.037 | 0.013 | 92.62 |

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Table 4 isolates the proposed 4D co-training components under identical training and inference settings, evaluating video quality, action prediction, and task success. Adding only an isolated 4D expert raises success only from 91.83% to 91.87% and does not improve action MSE (0.032 to 0.034), suggesting that geometry is weak when confined to an auxiliary branch. With decayed 4D read access, average success reaches 92.14% and action MSE drops to 0.026. The spatial and temporal relation losses further reduce MSE to 0.022 and 0.019 and raise success above 92.2%. Full MECo-WAM has best PSNR (30.72), lowest MSE (0.013), and highest average success (92.62%), a 0.79-point gain over Fast-WAM. The uniform-weight variant reaches 92.38%, supporting the value of action-aware geometry emphasis.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 表 4 在相同训练和推理设置下隔离所提出的四维协同训练组件，并从视频质量、动作预测和任务成功三个方面评估。仅添加孤立四维专家时，成功率只从 91.83% 升至 91.87%，且动作 MSE 没有改善（0.032 到 0.034），表明局限于辅助分支的几何监督较弱。加入衰减四维读取后，平均成功率达到 92.14%，动作 MSE 降至 0.026。空间和时序关系损失进一步将 MSE 降至 0.022 和 0.019，并将成功率提高到 92.2% 以上。完整 MECo-WAM 取得最佳 PSNR（30.72）、最低 MSE（0.013）和最高平均成功率（92.62%），比 Fast-WAM 高 0.79 点。均匀权重变体为 92.38%，支持突出动作感知几何的价值。

## 结论

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We presented MECo-WAM, an inference-efficient WAM that injects 4D geometry only during training. A training-only 4D expert, decayed read-mask attention, and action-aware temporal geometric distillation transfer frozen VGGT priors into the deployed video-action representation, while all auxiliary geometry modules are removed at inference. Results on LIBERO, RoboTwin 2.0, and ARX-R5 real-world tasks, together with ablations, show that action-relevant 4D supervision improves geometric reasoning without increasing deployment cost.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本文提出 MECo-WAM：一种仅在训练时注入四维几何的推理高效 WAM。仅训练期四维专家、衰减读掩码注意力和动作感知时序几何蒸馏将冻结 VGGT 先验传递至部署的视频—动作表征；推理时移除所有辅助几何模块。LIBERO、RoboTwin 2.0 和 ARX-R5 真实任务的结果，以及消融实验表明，动作相关四维监督能在不增加部署成本的情况下提升几何推理。

## 参考文献（pp.8–9；作者—年份体例，42 条）

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Bi, H.; Tan, H.; Xie, S.; Wang, Z.; Huang, S.; Liu, H.; Zhao, R.; Feng, Y.; Xiang, C.; Rong, Y.; et al. 2026. Motus: A unified latent action world model. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, 35101–35113.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Bi 等，2026。《Motus：统一潜在动作世界模型》。IEEE/CVF 计算机视觉与模式识别会议，35101–35113。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Black, K.; Brown, N.; Driess, D.; Esmail, A.; Equi, M.; Finn, C.; Fusai, N.; Groom, L.; Hausman, K.; Ichter, B.; et al. 2024. $\pi_0$: A Vision-Language-Action Flow Model for General Robot Control. arXiv preprint arXiv:2410.24164.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> Black 等，2024。《$\pi_0$：用于通用机器人控制的视觉—语言—动作流模型》。arXiv 预印本 arXiv:2410.24164。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Chen, S.; Guo, H.; Zhu, S.; Zhang, F.; Huang, Z.; Feng, J.; and Kang, B. 2025. Video Depth Anything: Consistent Depth Estimation for Super-Long Videos. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, 22831–22840.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Chen 等，2025。《Video Depth Anything：超长视频的一致深度估计》。IEEE/CVF 计算机视觉与模式识别会议，22831–22840。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Fan, X.; Deng, S.; Wu, X.; Lu, Y.; Li, Z.; Yan, M.; Zhang, Y.; Zhang, Z.; Wang, H.; and Zhao, H. 2026. Any3D-VLA: Enhancing VLA Robustness via Diverse Point Clouds. arXiv preprint arXiv:2602.00807.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> Fan 等，2026。《Any3D-VLA：通过多样点云增强 VLA 鲁棒性》。arXiv 预印本 arXiv:2602.00807。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Guo, J.; Li, Q.; Li, P.; Chen, Z.; Sun, N.; Su, Y.; Wang, H.; Zhang, Y.; Li, X.; and Liu, H. 2026. Unified 4D world action modeling from video priors with asynchronous denoising. arXiv preprint arXiv:2604.26694.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> Guo 等，2026。《利用异步去噪从视频先验进行统一四维世界动作建模》。arXiv 预印本 arXiv:2604.26694。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Hu, Y.; Guo, Y.; Wang, P.; Chen, X.; Wang, Y.-J.; Zhang, J.; Sreenath, K.; Lu, C.; and Chen, J. 2025. Video Prediction Policy: A Generalist Robot Policy with Predictive Visual Representations. In International Conference on Machine Learning, volume 267, 24328–24346.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> Hu 等，2025。《视频预测策略：具备预测性视觉表征的通才机器人策略》。国际机器学习会议，第 267 卷，24328–24346。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Intelligence, P.; Black, K.; Brown, N.; Darpinian, J.; Dhabalia, K.; Driess, D.; Esmail, A.; Equi, M.; Finn, C.; Fusai, N.; et al. 2025. $\pi_{0.5}$: A Vision-Language-Action Model with Open-World Generalization. arXiv preprint arXiv:2504.16054.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> Intelligence 等，2025。《$\pi_{0.5}$：具有开放世界泛化能力的视觉—语言—动作模型》。arXiv 预印本 arXiv:2504.16054。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Kim, M. J.; Finn, C.; and Liang, P. 2025. Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success. arXiv preprint arXiv:2502.19645.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> Kim、Finn 与 Liang，2025。《微调视觉—语言—动作模型：优化速度和成功率》。arXiv 预印本 arXiv:2502.19645。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Kim, M. J.; Gao, Y.; Lin, T.-Y.; Lin, Y.-C.; Ge, Y.; Lam, G.; Liang, P.; Song, S.; Liu, M.-Y.; Finn, C.; et al. 2026. Cosmos Policy: Fine-tuning video models for visuomotor control and planning. arXiv preprint arXiv:2601.16163.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> Kim 等，2026。《Cosmos Policy：为视动控制与规划微调视频模型》。arXiv 预印本 arXiv:2601.16163。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> Kim, M. J.; Pertsch, K.; Karamcheti, S.; Xiao, T.; Balakrishna, A.; Nair, S.; Rafailov, R.; Foster, E. P.; Sanketi, P. R.; Vuong, Q.; Kollar, T.; Burchfiel, B.; Tedrake, R.; Sadigh, D.; Levine, S.; Liang, P.; and Finn, C. 2025. OpenVLA: An Open-Source Vision-Language-Action Model. In Conference on Robot Learning, volume 270, 2679–2713.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> Kim 等，2025。《OpenVLA：开源视觉—语言—动作模型》。机器人学习会议，第 270 卷，2679–2713。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> Li, F.; Song, W.; Zhao, H.; Wang, J.; Ding, P.; Wang, D.; Zeng, L.; and Li, H. 2026a. Spatial Forcing: Implicit Spatial Representation Alignment for Vision-Language-Action Model. In International Conference on Learning Representations.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> Li 等，2026a。《Spatial Forcing：视觉—语言—动作模型的隐式空间表征对齐》。国际学习表征会议。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> Li, L.; Zhang, Q.; Luo, Y.; Yang, S.; Wang, R.; Han, F.; Yu, M.; Gao, Z.; Xue, N.; Zhu, X.; et al. 2026b. Causal World Modeling for Robot Control. arXiv preprint arXiv:2601.21998.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> Li 等，2026b。《用于机器人控制的因果世界建模》。arXiv 预印本 arXiv:2601.21998。

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> Li, P.; Chen, Y.; Wu, H.; Ma, X.; Wu, X.; Huang, Y.; Wang, L.; Kong, T.; and Tan, T. 2025a. BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models. In Conference on Neural Information Processing Systems.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> Li 等，2025a。《BridgeVLA：利用视觉语言模型输入—输出对齐进行高效三维操作学习》。神经信息处理系统会议。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> Li, X.; Heng, L.; Liu, J.; Shen, Y.; Gu, C.; Liu, Z.; Chen, H.; Han, N.; Zhang, R.; Tang, H.; Zhang, S.; and Dong, H. 2025b. 3DS-VLA: A 3D Spatial-Aware Vision Language Action Model for Robust Multi-Task Manipulation. In Conference on Robot Learning, volume 305 of Proceedings of Machine Learning Research, 2344–2359. PMLR.

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> Li 等，2025b。《3DS-VLA：用于鲁棒多任务操作的三维空间感知视觉语言动作模型》。机器人学习会议，机器学习研究论文集第 305 卷，2344–2359。PMLR。

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> Li, Y.; Wei, X.; Cao, J.; Wang, H.; Chi, X.; Bai, C.; Sun, Q.; Li, J.; Zhang, X.; Tang, J.; et al. 2026c. WAM4D: Fast 4D World Action Model via Spatial Register Tokens. arXiv preprint arXiv:2606.14048.

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> Li 等，2026c。《WAM4D：通过空间寄存器令牌实现快速四维世界动作模型》。arXiv 预印本 arXiv:2606.14048。

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> Liang, Z.; Li, Y.; Yang, T.; Wu, C.; Mao, S.; Pei, L.; Nian, T.; Zhou, S.; Yang, X.; Pang, J.; et al. 2025. Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies. arXiv preprint arXiv:2508.20072.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> Liang 等，2025。《离散扩散 VLA：将离散扩散引入视觉—语言—动作策略的动作解码》。arXiv 预印本 arXiv:2508.20072。

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> Liu, B.; Zhu, Y.; Gao, C.; Feng, Y.; Liu, Q.; Zhu, Y.; and Stone, P. 2023. LIBERO: Benchmarking knowledge transfer for lifelong robot learning. Advances in Neural Information Processing Systems, 36: 44776–44791.

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> Liu 等，2023。《LIBERO：终身机器人学习的知识迁移基准》。神经信息处理系统进展，36：44776–44791。

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> Ma, T.; Zheng, J.; Wang, Z.; Jiang, C.; Cui, A.; Liang, J.; and Yang, S. 2026. DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control. arXiv preprint arXiv:2603.10448.

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> Ma 等，2026。《DiT4DiT：联合建模视频动态和动作以实现可泛化机器人控制》。arXiv 预印本 arXiv:2603.10448。

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> Mu, Y.; Chen, T.; Chen, Z.; Peng, S.; Lan, Z.; Gao, Z.; Liang, Z.; Yu, Q.; Zou, Y.; Xu, M.; et al. 2025. RoboTwin: Dual-arm robot benchmark with generative digital twins. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, 27649–27660.

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> Mu 等，2025。《RoboTwin：具有生成式数字孪生的双臂机器人基准》。IEEE/CVF 计算机视觉与模式识别会议，27649–27660。

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> Ni, C.; Chen, C.; Wang, X.; Zhu, Z.; Zheng, W.; Wang, B.; Chen, T.; Zhao, G.; Li, H.; Dong, Z.; Zhang, Q.; Ye, Y.; Wang, Y.; Huang, G.; and Mei, W. 2026. SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, 13474–13485.

> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> Ni 等，2026。《SwiftVLA：以极小开销释放轻量级 VLA 模型的时空动态》。IEEE/CVF 计算机视觉与模式识别会议，13474–13485。

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> Pai, J.; Achenbach, L.; Montesinos, V.; Forrai, B.; Mees, O.; and Nava, E. 2025. mimic-video: Video-action models for generalizable robot control beyond VLAs. arXiv preprint arXiv:2512.15692.

> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> Pai 等，2025。《mimic-video：超越 VLA 的、用于可泛化机器人控制的视频—动作模型》。arXiv 预印本 arXiv:2512.15692。

> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> Pertsch, K.; Stachowicz, K.; Ichter, B.; Driess, D.; Nair, S.; Vuong, Q.; Mees, O.; Finn, C.; and Levine, S. 2025. FAST: Efficient action tokenization for vision-language-action models. arXiv preprint arXiv:2501.09747.

> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> Pertsch 等，2025。《FAST：视觉—语言—动作模型的高效动作令牌化》。arXiv 预印本 arXiv:2501.09747。

> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> Qian, J.; Han, B.; Shi, C.; Xiao, L.; Yang, L.; Shi, S.; and Jiang, L. 2026. GeoPredict: Leveraging Predictive Kinematics and 3D Gaussian Geometry for Precise VLA Manipulation. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, 13529–13539.

> <span style="color:#F59E0B"><strong>Para. 23[CN]:</strong></span> Qian 等，2026。《GeoPredict：利用预测运动学和三维高斯几何实现精确 VLA 操作》。IEEE/CVF 计算机视觉与模式识别会议，13529–13539。

> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> Qu, D.; Song, H.; Chen, Q.; Yao, Y.; Ye, X.; Ding, Y.; Wang, Z.; Gu, J.; Zhao, B.; Wang, D.; et al. 2025. SpatialVLA: Exploring spatial representations for visual-language-action model. arXiv preprint arXiv:2501.15830.

> <span style="color:#F59E0B"><strong>Para. 24[CN]:</strong></span> Qu 等，2025。《SpatialVLA：探索视觉—语言—动作模型的空间表征》。arXiv 预印本 arXiv:2501.15830。

> <span style="color:#3B82F6"><strong>Para. 25:</strong></span> Ranftl, R.; Bochkovskiy, A.; and Koltun, V. 2021. Vision Transformers for Dense Prediction. In IEEE/CVF International Conference on Computer Vision, 12179–12188.

> <span style="color:#F59E0B"><strong>Para. 25[CN]:</strong></span> Ranftl、Bochkovskiy 与 Koltun，2021。《用于稠密预测的视觉 Transformer》。IEEE/CVF 国际计算机视觉会议，12179–12188。

> <span style="color:#3B82F6"><strong>Para. 26:</strong></span> Spiridonov, A.; Zaech, J.-N.; Nikolov, N.; Van Gool, L.; and Paudel, D. P. 2025. Generalist Robot Manipulation beyond Action Labeled Data. In Conference on Robot Learning.

> <span style="color:#F59E0B"><strong>Para. 26[CN]:</strong></span> Spiridonov 等，2025。《超越动作标注数据的通才机器人操作》。机器人学习会议。

> <span style="color:#3B82F6"><strong>Para. 27:</strong></span> Su, T.; Zhu, J.; Li, Y.; Ma, C.; Zhang, J.; Huang, Z.; Wang, H.; and Xu, Y. 2025. Towards high-consistency embodied world model with multi-view trajectory videos. arXiv preprint arXiv:2511.12882.

> <span style="color:#F59E0B"><strong>Para. 27[CN]:</strong></span> Su 等，2025。《利用多视角轨迹视频迈向高一致性具身世界模型》。arXiv 预印本 arXiv:2511.12882。

> <span style="color:#3B82F6"><strong>Para. 28:</strong></span> Su, T.; Zhu, J.; Wang, T.; He, Y.; Huang, Z.; Zhang, J.; Ma, C.; Wang, H.; Zhang, T.; Yin, M.; et al. 2026. DeMaVLA: A Vision-Language-Action Foundation Model for Generalizable Deformable Manipulation. arXiv preprint arXiv:2605.31286.

> <span style="color:#F59E0B"><strong>Para. 28[CN]:</strong></span> Su 等，2026。《DeMaVLA：用于可泛化可变形物操作的视觉—语言—动作基础模型》。arXiv 预印本 arXiv:2605.31286。

> <span style="color:#3B82F6"><strong>Para. 29:</strong></span> Sun, L.; Xie, B.; Liu, Y.; Shi, H.; Wang, T.; and Cao, J. 2025. GeoVLA: Empowering 3D Representations in Vision-Language-Action Models. arXiv preprint arXiv:2508.09071.

> <span style="color:#F59E0B"><strong>Para. 29[CN]:</strong></span> Sun 等，2025。《GeoVLA：赋能视觉—语言—动作模型中的三维表征》。arXiv 预印本 arXiv:2508.09071。

> <span style="color:#3B82F6"><strong>Para. 30:</strong></span> Team, M.; Xiang, C.; Bao, F.; Liu, H.; Tan, H.; Bi, H.; Li, J.; Liu, J.; Pang, J.; Jing, K.; et al. 2026. MotuBrain: An advanced world action model for robot control. arXiv preprint arXiv:2604.27792.

> <span style="color:#F59E0B"><strong>Para. 30[CN]:</strong></span> Team 等，2026。《MotuBrain：用于机器人控制的高级世界动作模型》。arXiv 预印本 arXiv:2604.27792。

> <span style="color:#3B82F6"><strong>Para. 31:</strong></span> Wan, T.; Wang, A.; Ai, B.; Wen, B.; Mao, C.; Xie, C.-W.; Chen, D.; Yu, F.; Zhao, H.; Yang, J.; et al. 2025. Wan: Open and advanced large-scale video generative models. arXiv preprint arXiv:2503.20314.

> <span style="color:#F59E0B"><strong>Para. 31[CN]:</strong></span> Wan 等，2025。《Wan：开放且先进的大规模视频生成模型》。arXiv 预印本 arXiv:2503.20314。

> <span style="color:#3B82F6"><strong>Para. 32:</strong></span> Wang, J.; Chen, M.; Karaev, N.; Vedaldi, A.; Rupprecht, C.; and Novotny, D. 2025a. VGGT: Visual Geometry Grounded Transformer. In IEEE/CVF Conference on Computer Vision and Pattern Recognition, 5294–5306.

> <span style="color:#F59E0B"><strong>Para. 32[CN]:</strong></span> Wang 等，2025a。《VGGT：视觉几何落地 Transformer》。IEEE/CVF 计算机视觉与模式识别会议，5294–5306。

> <span style="color:#3B82F6"><strong>Para. 33:</strong></span> Wang, S.; Shi, J.; Fu, Z.; He, X.; Liu, F.; Yang, C.; Zhou, Y.; Fei, Z.; Gong, J.; Fu, J.; et al. 2026. World Action Models: The Next Frontier in Embodied AI. arXiv preprint arXiv:2605.12090.

> <span style="color:#F59E0B"><strong>Para. 33[CN]:</strong></span> Wang 等，2026。《世界动作模型：具身 AI 的下一前沿》。arXiv 预印本 arXiv:2605.12090。

> <span style="color:#3B82F6"><strong>Para. 34:</strong></span> Wang, Y.; Li, X.; Wang, W.; Zhang, J.; Li, Y.; Chen, Y.; Wang, X.; and Zhang, Z. 2025b. Unified Vision-Language-Action Model. arXiv preprint arXiv:2506.19850.

> <span style="color:#F59E0B"><strong>Para. 34[CN]:</strong></span> Wang 等，2025b。《统一视觉—语言—动作模型》。arXiv 预印本 arXiv:2506.19850。

> <span style="color:#3B82F6"><strong>Para. 35:</strong></span> Xu, G.; Zhang, Q.; Zhou, J.; Zhu, X.; Shen, Y.; Yang, X.; and Xu, Y. 2026. Next Forcing: Causal World Modeling with Multi-Chunk Prediction. arXiv preprint arXiv:2606.11187.

> <span style="color:#F59E0B"><strong>Para. 35[CN]:</strong></span> Xu 等，2026。《Next Forcing：具有多动作块预测的因果世界建模》。arXiv 预印本 arXiv:2606.11187。

> <span style="color:#3B82F6"><strong>Para. 36:</strong></span> Ye, A.; Wang, B.; Ni, C.; Huang, G.; Zhao, G.; Li, H.; Li, H.; Li, J.; Lv, J.; Liu, J.; et al. 2026a. GigaWorld-Policy: An Efficient Action-Centered World–Action Model. arXiv preprint arXiv:2603.17240.

> <span style="color:#F59E0B"><strong>Para. 36[CN]:</strong></span> Ye 等，2026a。《GigaWorld-Policy：高效的以动作为中心的世界—动作模型》。arXiv 预印本 arXiv:2603.17240。

> <span style="color:#3B82F6"><strong>Para. 37:</strong></span> Ye, J.; Wang, F.; Gao, N.; Yu, J.; Zhu, Yangkun; Wang, B.; Zhang, J.; Jin, W.; Fu, Y.; Zheng, F.; Chen, Y.; and Pang, J. 2026b. Spatially Guided Training for Vision-Language-Action Model. In International Conference on Learning Representations.

> <span style="color:#F59E0B"><strong>Para. 37[CN]:</strong></span> Ye 等，2026b。《用于视觉—语言—动作模型的空间引导训练》。国际学习表征会议。

> <span style="color:#3B82F6"><strong>Para. 38:</strong></span> Ye, S.; Ge, Y.; Zheng, K.; Gao, S.; Yu, S.; Kurian, G.; Indupuru, S.; Tan, Y. L.; Zhu, C.; Xiang, J.; et al. 2026c. World action models are zero-shot policies. arXiv preprint arXiv:2602.15922.

> <span style="color:#F59E0B"><strong>Para. 38[CN]:</strong></span> Ye 等，2026c。《世界动作模型是零样本策略》。arXiv 预印本 arXiv:2602.15922。

> <span style="color:#3B82F6"><strong>Para. 39:</strong></span> Yuan, T.; Dong, Z.; Liu, Y.; and Zhao, H. 2026. Fast-WAM: Do world action models need test-time future imagination? arXiv preprint arXiv:2603.16666.

> <span style="color:#F59E0B"><strong>Para. 39[CN]:</strong></span> Yuan 等，2026。《Fast-WAM：世界动作模型需要测试时未来想象吗？》。arXiv 预印本 arXiv:2603.16666。

> <span style="color:#3B82F6"><strong>Para. 40:</strong></span> Zhang, Z.; Li, H.; Dai, Y.; Zhu, Z.; Zhou, L.; Liu, C.; Wang, D.; Tay, F. E. H.; Chen, S.; Liu, Z.; Liu, Y.; Li, X.; and Zhou, P. 2026. From Spatial to Actions: Grounding Vision-Language-Action Model in Spatial Foundation Priors. In International Conference on Learning Representations.

> <span style="color:#F59E0B"><strong>Para. 40[CN]:</strong></span> Zhang 等，2026。《从空间到动作：将视觉—语言—动作模型落地于空间基础先验》。国际学习表征会议。

> <span style="color:#3B82F6"><strong>Para. 41:</strong></span> Zhen, H.; Qiu, X.; Chen, P.; Yang, J.; Yan, X.; Du, Y.; Hong, Y.; and Gan, C. 2024. 3D-VLA: A 3D Vision-Language-Action Generative World Model. In International Conference on Machine Learning, volume 235, 61229–61245.

> <span style="color:#F59E0B"><strong>Para. 41[CN]:</strong></span> Zhen 等，2024。《3D-VLA：三维视觉—语言—动作生成式世界模型》。国际机器学习会议，第 235 卷，61229–61245。

> <span style="color:#3B82F6"><strong>Para. 42:</strong></span> Zheng, J.; Li, J.; Wang, Z.; Liu, D.; Kang, X.; Feng, Y.; Zheng, Y.; Zou, J.; Chen, Y.; Zeng, J.; et al. 2025. X-VLA: Soft-prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model. arXiv preprint arXiv:2510.10274.

> <span style="color:#F59E0B"><strong>Para. 42[CN]:</strong></span> Zheng 等，2025。《X-VLA：作为可扩展跨具身视觉—语言—动作模型的软提示 Transformer》。arXiv 预印本 arXiv:2510.10274。

## 术语表

| English | 中文 | 说明 |
|---|---|---|
| World Action Model (WAM) | 世界动作模型 | 首次出现后保留 WAM。 |
| MECo-WAM | 多专家协同训练世界动作模型 | 模型专名保持 MECo-WAM。 |
| Multi-Expert Co-Training | 多专家协同训练 | 不与“联合训练”混用。 |
| 4D geometric priors | 四维几何先验 | 指几何及其时序演化。 |
| frozen VGGT | 冻结 VGGT | 训练期几何教师；非部署模块。 |
| decayed 4D read-mask attention | 衰减式四维读掩码注意力 | 固定模块名称。 |
| action-aware temporal geometric distillation | 动作感知时序几何蒸馏 | 固定模块名称。 |
| relational matching | 关系匹配 | 比较关系矩阵，不要求绝对特征坐标一致。 |
| action chunk | 动作块 | 视界为 $H$ 的动作序列。 |
| video-action pathway | 视频—动作路径 | 部署时保留的路径。 |
| inference graph | 推理图 | 部署计算图。 |
| spatial grounding | 空间落地能力 | 物体—夹爪—目标空间关系。 |

## 阅读提示

- 核心因果链是：冻结 VGGT 的关系监督 → 训练期四维专家 → 受限且逐渐关闭的 $g_0$ 读取 → 部署的视频—动作特征具备更强几何能力；并非在测试时显式预测四维几何。
- Eq. (15) 是帧内关系匹配，Eq. (19) 是关键帧间关系变化匹配；二者均以动作相关令牌权重加权。
- 所有正文页面（pp.1–7）与原始作者—年份书目页（pp.8–9）均已覆盖；未检测到附录。
