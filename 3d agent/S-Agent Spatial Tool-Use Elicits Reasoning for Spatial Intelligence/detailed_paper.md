# Spatial Tool-Use Elicits Reasoning for Spatial Intelligence

Yalun Dai¹\*, Hao Li¹˒⁴˒★\*, Shulin Tian¹, Runmao Yao¹, Yuhao Dong¹, Fangzhou Hong¹˒★, Zhaoxi Chen¹˒★, Fangfu Liu², Baoliang Tian³, Dingwen Zhang⁴, Tao Wang³†, Kim-Hui Yap¹†, Ziwei Liu¹˒★

¹ NTU　² THU　³ ByteDance　⁴ NWPU　★ Ropedia

Project Page: Ropedia/S-Agent

arXiv:2606.20515v1 [cs.CV], 18 Jun 2026

\* Equal contributors. † Corresponding author.

### Figure 1. Overview of S-Agent

![Figure 1](3d%20agent/S-Agent%20Spatial%20Tool-Use%20Elicits%20Reasoning%20for%20Spatial%20Intelligence/assets/fig1_overview.png)

**Caption:** Overview of S-Agent. S-Agent is the spatial tool-use agentic paradigm designed for continuous multi-view image and video reasoning, which formulates spatial reasoning as an active process of spatio-temporal evidence accumulation. It contains a VLM semantic planner with a hierarchy of spatial tools to ground, lift, and aggregate geometric cues, alongside a dual-memory system to maintain the evolving scene and reasoning history. Extensive experiments show that our paradigm consistently enhances zero-shot VLMs and distills a compact agent (S-Agent-8B) that rivals advanced closed-source models.

**Caption[CN]:** S-Agent 概览。S-Agent 是一种面向连续多视角图像与视频推理的空间工具使用智能体范式，它将空间推理表述为主动的时空证据累积过程。该范式包含一个 VLM 语义规划器、一套用于定位、提升并聚合几何线索的层级化空间工具，以及一个用于维护演化场景与推理历史的双记忆系统。大量实验表明，我们的范式能够持续增强零样本 VLM，并可蒸馏得到紧凑型智能体 S-Agent-8B，其性能可媲美先进的闭源模型。

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Real-world spatial intelligence requires reasoning over a continuous and evolving 3D world, yet existing VLMs and tool-augmented agents largely remain tied to static, stateless inference from isolated visual observations. We introduce S-Agent, a spatial tool-use agentic paradigm for understanding and reasoning over continuous multi-view images and videos. By formulating spatial reasoning as spatio-temporal evidence accumulation rather than isolated frame-level prediction, S-Agent reshapes spatial perception into scene-centric understanding beyond frame-centric recognition. Specifically, S-Agent casts the VLM as a semantic planner that decides what evidence is needed, while a hierarchy of spatial tools and experts grounds objects in 2D, lifts them into 3D geometric evidence, and aggregates this evidence into high-level spatial knowledge (e.g., counting, measurement, orientation, and relative position). Additionally, a temporal memory mechanism, including Scene Memory for maintaining the evolving scene state and Agent Memory for accumulating reasoning context, enables evidence integration across frames and reasoning steps. Comprehensive experiments on multi-view and video spatial reasoning benchmarks show that S-Agent consistently improves both open-source and closed-source VLMs in a training-free manner. Beyond inference-time augmentation, supervised fine-tuning (SFT) on S-Agent-generated spatial trajectories S-300K yields S-Agent-8B, a compact spatial agent that significantly surpasses similar-scale baselines (e.g., Qwen3-VL-8B) and performs comparably to advanced closed-source models (e.g., GPT-5.4 and Gemini 3).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 真实世界的空间智能要求对一个连续且不断演化的三维世界进行推理，然而现有 VLM 与工具增强型智能体在很大程度上仍局限于基于孤立视觉观测的静态、无状态推断。我们提出 S-Agent：一种用于理解连续多视角图像与视频并对其进行推理的空间工具使用智能体范式。S-Agent 不再把空间推理表述为孤立的帧级预测，而是将其表述为时空证据累积，从而把空间感知由以帧为中心的识别重塑为超越单帧、以场景为中心的理解。具体而言，S-Agent 将 VLM 作为决定需要何种证据的语义规划器，同时利用层级化的空间工具与专家在二维空间中定位对象、将其提升为三维几何证据，并把这些证据聚合为高层空间知识（例如计数、测量、朝向和相对位置）。此外，时间记忆机制——包括用于维护演化场景状态的 Scene Memory，以及用于累积推理上下文的 Agent Memory——使系统能够跨帧、跨推理步骤整合证据。针对多视角与视频空间推理基准的综合实验表明，S-Agent 能够以免训练方式持续提升开源和闭源 VLM。除推理时增强外，在 S-Agent 生成的空间轨迹 S-300K 上进行监督微调（SFT），可得到紧凑型空间智能体 S-Agent-8B；它显著超越相近规模的基线（例如 Qwen3-VL-8B），并取得与先进闭源模型（例如 GPT-5.4 和 Gemini 3）相当的性能。

## 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Spatial intelligence, the ability to understand geometric relations among objects and their 3D environments, is essential for vision-language models (VLMs) to operate in the physical world and represents a key step toward artificial general intelligence (AGI), where models are expected to perceive, reason, and make decisions in 3D space as humans do. Such capability is crucial for real-world applications, including embodied robotics [8, 2], AR/VR perception [18], and autonomous driving [11, 4]. However, unlike human perception, which naturally integrates visual cues into coherent 3D understanding, current VLMs are primarily trained on passive 2D visual-text corpora, with limited explicit 3D supervision or embodied experience [20, 1, 15]. This creates a fundamental semantic-to-geometric gap: while VLMs excel at probabilistic and qualitative semantic inference, their reasoning is often mediated by lossy semantic representations that fail to faithfully capture high-fidelity geometry, leaving them susceptible to textual patterns and semantic priors rather than grounded 3D geometric evidence [7, 3].

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 空间智能，即理解对象及其三维环境之间几何关系的能力，是视觉语言模型（VLM）在物理世界中运行所必需的能力，也代表着迈向通用人工智能（AGI）的关键一步；在 AGI 中，模型应当像人类一样在三维空间中感知、推理并做出决策。这种能力对现实应用至关重要，包括具身机器人 [8, 2]、AR/VR 感知 [18] 和自动驾驶 [11, 4]。然而，人类感知能够自然地将视觉线索整合成连贯的三维理解，当前 VLM 却主要在被动式二维视觉—文本语料上训练，获得的显式三维监督或具身经验十分有限 [20, 1, 15]。这造成了根本性的语义—几何鸿沟：VLM 擅长概率性、定性的语义推断，但其推理往往由有损的语义表征所介导，无法忠实捕获高保真几何信息，因此容易依赖文本模式和语义先验，而不是有根基的三维几何证据 [7, 3]。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Recent advances in agentic VLMs substantially push the boundary of spatial understanding by augmenting VLMs with external tools, executable programs, and explicit geometric structure. For example, VADAR [17] dynamically constructs a Python API and synthesizes programs for 3D spatial reasoning; SpaceTools [6] trains VLMs to coordinate multiple vision and robotic tools through interactive reinforcement learning. However, despite their strong performance, these methods still largely focus on static images or isolated visual observations, which remains far from the goal of real-world spatial intelligence: the real 3D world is hidden, evolving, and continuously projected into streams of 2D observations. Reasoning from isolated 2D views alone makes it fundamentally challenging to maintain persistent object states, integrate evidence across viewpoints and time, and build a coherent understanding of the underlying 3D scene.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 智能体式 VLM 的最新进展通过为 VLM 增配外部工具、可执行程序与显式几何结构，显著拓展了空间理解的边界。例如，VADAR [17] 动态构建 Python API，并合成用于三维空间推理的程序；SpaceTools [6] 则通过交互式强化学习训练 VLM 协调多种视觉与机器人工具。然而，尽管这些方法表现强劲，它们仍主要聚焦于静态图像或孤立视觉观测，与真实世界空间智能的目标仍相去甚远：真实的三维世界是隐藏的、不断演化的，并被持续投影为二维观测流。仅从孤立的二维视图进行推理，会使维持持久对象状态、跨视角和时间整合证据，以及形成对底层三维场景的连贯理解，从根本上变得困难。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> To move beyond static and stateless spatial reasoning, we introduce S-Agent, a Spatial tool-use agentic paradigm for understanding and reasoning over continuous multi-view images and videos. Our key motivation is that the missing ingredient for video-based spatial intelligence is not merely stronger 2D/3D visual recognition, but a reasoning mechanism that can accumulate spatial evidence along both spatial and temporal dimensions. Specifically, in continuous multi-view and video settings, each frame is only a partial and transient observation of the scene, while the key to spatial intelligence is to connect these observations into a spatially structured and temporally persistent understanding of the underlying 3D world. Rather than asking VLMs to implicitly internalize this entire process, our S-Agent casts the VLM as a semantic planner that decides what evidence is needed, while spatial tools/experts and temporal memory provide continuous and explicit 3D awareness of the specific scene, ranging from low-level 2D/3D evidence (e.g., object grounding, depth information) to high-level spatial knowledge (e.g., orientations, relationships). This separation enables the agent to reason from accumulated evidence instead of isolated visual impressions, extending existing spatial agent methods toward stateful, temporally grounded understanding of evolving scenes.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 为了超越静态、无状态的空间推理，我们提出 S-Agent：一种用于理解连续多视角图像与视频并对其进行推理的空间工具使用智能体范式。我们的核心动机是，视频空间智能所缺失的要素并非仅仅是更强的二维/三维视觉识别，而是一种能够沿空间与时间两个维度累积空间证据的推理机制。具体来说，在连续多视角和视频场景中，每一帧都只是对场景的局部、瞬时观测，而空间智能的关键在于将这些观测连接起来，形成对底层三维世界具有空间结构且在时间上持久的理解。S-Agent 并不要求 VLM 隐式内化整个过程，而是把 VLM 作为决定需要何种证据的语义规划器；空间工具/专家与时间记忆则针对特定场景提供连续且显式的三维认知，覆盖从低层二维/三维证据（例如对象定位、深度信息）到高层空间知识（例如朝向、关系）的不同层次。这种分离使智能体能够依据累积证据而非孤立的视觉印象进行推理，从而推动现有空间智能体方法走向对演化场景的有状态、时间有根基的理解。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Motivated by this perspective, S-Agent is designed as a VLM-orchestrated spatio-temporal reasoning framework: it progressively aggregates spatial evidence from fragmented 2D observations into structured 3D scene knowledge, while persistently accumulating temporal evidence across frames and reasoning iterations. (1) For the spatial dimension, S-Agent follows a hierarchical understanding process. At the first level, 2D perception tools ground objects and regions in individual frames, establishing object-centric visual facts for subsequent reasoning. At the second level, multi-view 3D tools enrich these grounded entities with geometric cues (e.g., depth, 3D coordinates, and camera poses), allowing evidence from different viewpoints to be integrated beyond the original image plane. At the third level, specialized spatial experts aggregate these geometric signals into higher-level spatial knowledge (e.g., object counts, physical measurements, orientations, and relative positions). (2) For the temporal dimension, S-Agent maintains memory over the evolving reasoning process: Scene Memory tracks grounded entities across frames to preserve object identity and suppress duplicate evidence, while Agent Memory stores accumulated tool observations and intermediate reasoning traces for iterative refinement. In this way, S-Agent turns video spatial reasoning from disconnected frame-level prediction into evidence accumulation over an evolving 3D scene.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 基于这一视角，S-Agent 被设计为一个由 VLM 编排的时空推理框架：它逐步将碎片化二维观测中的空间证据聚合为结构化三维场景知识，同时跨帧、跨推理迭代持续累积时间证据。（1）在空间维度上，S-Agent 遵循层级化理解过程。第一层的二维感知工具在各帧中定位对象和区域，为后续推理建立以对象为中心的视觉事实。第二层的多视角三维工具利用几何线索（例如深度、三维坐标和相机位姿）丰富这些已定位实体，使来自不同视角的证据能够脱离原始图像平面而被整合。第三层的专门空间专家将这些几何信号聚合为更高层的空间知识（例如对象数量、物理测量、朝向和相对位置）。（2）在时间维度上，S-Agent 为不断演化的推理过程维持记忆：Scene Memory 跨帧追踪已定位实体，以保持对象身份并抑制重复证据；Agent Memory 则存储累积的工具观测和中间推理轨迹，以供迭代式细化。通过这种方式，S-Agent 将视频空间推理由彼此割裂的帧级预测转变为对演化三维场景的证据累积。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Comprehensive experiments on multi-image benchmarks (MMSI-Bench [31] and ViewSpatial-Bench [12]) and video spatial reasoning benchmarks (ReVSI [37] and VSI-SUPER [30]) validate the robustness and generalizability of our approach. (1) Zero-shot setting. We directly instantiate S-Agent with both open-source models (e.g., Qwen3) and closed-source APIs (e.g., Gemini and GPT) in a training-free manner. Simply and directly applying the S-Agent framework consistently improves the spatial reasoning ability of these VLMs, improving over GPT-5.4 by 4.5% on MMSI-Bench. (2) Training setting. Beyond inference-time improvement, we further construct a spatial-instruction dataset S-300K from zero-shot S-Agent trajectories on the SenseNova-SI-800K [5] training set (which is fully disjoint from all evaluation benchmarks) and use it to perform supervised fine-tuning on Qwen3-VL-8B, resulting in S-Agent-8B. Compared with direct Qwen3-VL-8B inference, S-Agent-8B achieves a 10.5% improvement on MMSI-Bench, improving accuracy from 31.1% to 41.6%, and performs comparably to advanced closed-source models such as GPT-5.4 and Gemini 3 Pro across multiple benchmarks. These results show that S-Agent is not only an effective training-free inference framework, but also a scalable paradigm for building compact spatially capable agents.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 在多图像基准（MMSI-Bench [31] 和 ViewSpatial-Bench [12]）以及视频空间推理基准（ReVSI [37] 和 VSI-SUPER [30]）上的综合实验，验证了我们方法的稳健性与泛化能力。（1）零样本设置。我们以免训练方式，直接使用开源模型（例如 Qwen3）和闭源 API（例如 Gemini 和 GPT）来实例化 S-Agent。简单、直接地应用 S-Agent 框架，便能持续提升这些 VLM 的空间推理能力；在 MMSI-Bench 上，它比 GPT-5.4 提高 4.5%。（2）训练设置。除推理时提升外，我们还从 SenseNova-SI-800K [5] 训练集（与所有评估基准完全不相交）上的零样本 S-Agent 轨迹构建空间指令数据集 S-300K，并用它对 Qwen3-VL-8B 进行监督微调，得到 S-Agent-8B。与直接进行 Qwen3-VL-8B 推理相比，S-Agent-8B 在 MMSI-Bench 上提高 10.5%，准确率由 31.1% 升至 41.6%，并在多个基准上取得与 GPT-5.4、Gemini 3 Pro 等先进闭源模型相当的性能。这些结果表明，S-Agent 不仅是一种有效的免训练推理框架，也是一种可扩展的范式，可用于构建具备空间能力的紧凑型智能体。

## 2. Method

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This section details the design of S-Agent. We first formulate spatial reasoning as iterative updates to a scene state and an agent state in Section 2.1. We then describe how S-Agent acquires hierarchical spatial evidence in Section 2.1.1, maintains temporal memory for stateful reasoning in Section 2.1.2, and uses S-Agent trajectories to train compact agents in Section 2.2.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本节详细介绍 S-Agent 的设计。我们首先在第 2.1 节中将空间推理表述为对场景状态和智能体状态的迭代更新。随后，我们分别说明 S-Agent 如何在第 2.1.1 节获取层级化空间证据、在第 2.1.2 节维持用于有状态推理的时间记忆，以及在第 2.2 节利用 S-Agent 轨迹训练紧凑型智能体。

### Figure 2. The pipeline of S-Agent

![Figure 2](fig2_pipeline.png)

**Caption:** The pipeline of S-Agent. Instead of answering from an isolated visual impression, S-Agent uses a VLM as a semantic planner, spatial tools and experts as scene-specific evidence providers, and memory as the carrier of persistent 3D state across views, frames, and reasoning steps.

**Caption[CN]:** S-Agent 的流程。S-Agent 不再依据孤立的视觉印象作答，而是使用 VLM 作为语义规划器，使用空间工具与专家作为特定场景的证据提供者，并以记忆作为跨视角、跨帧和跨推理步骤承载持久三维状态的载体。

### 2.1. S-Agent Framework

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We consider spatial reasoning problems defined by a question $q$ and a sequence or set of visual observations $\mathcal{F}$. The input can be a video (e.g., the scene and camera may evolve over time) or a multi-view image set (e.g., different images capture the same scene from different viewpoints). The goal of S-Agent is to produce an answer $a$ that depends on the underlying 3D scene state rather than on a single 2D projection. To this end, S-Agent performs inference as an iterative evidence-seeking process, progressively acquiring and reusing scene-specific spatial evidence, as illustrated in Figure 2.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们考虑由问题 $q$ 和一组或一系列视觉观测 $\mathcal{F}$ 所定义的空间推理问题。输入可以是视频（例如场景和相机可能随时间演化），也可以是多视角图像集（例如不同图像从不同视点捕获同一场景）。S-Agent 的目标是生成依赖底层三维场景状态、而非单个二维投影的答案 $a$。为此，如图 2 所示，S-Agent 将推断作为一个迭代式证据搜寻过程来执行，逐步获取并复用特定场景的空间证据。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> At reasoning step $t$, S-Agent maintains two memory states. The first is a scene memory state $\mathcal{S}_t$ for grounded spatial evidence, which stores grounded entities and their accumulated spatial attributes. The second is an agent memory state $\mathcal{H}_t$ for reasoning history, which records previous tool calls, observations, and reasoning decisions. A tool-calling VLM planner $\pi_\theta$ maps the question $q$, input observations $\mathcal{F}$, and current memory states $(\mathcal{S}_t,\mathcal{H}_t)$ to an evidence request $r_t$:

$$
r_t=\pi_\theta(q,\mathcal{F},\mathcal{S}_t,\mathcal{H}_t).
$$

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在推理步骤 $t$，S-Agent 维持两种记忆状态。第一种是面向有根基空间证据的场景记忆状态 $\mathcal{S}_t$，用于存储已定位实体及其累积的空间属性。第二种是面向推理历史的智能体记忆状态 $\mathcal{H}_t$，用于记录先前的工具调用、观测和推理决策。能够调用工具的 VLM 规划器 $\pi_\theta$ 将问题 $q$、输入观测 $\mathcal{F}$ 与当前记忆状态 $(\mathcal{S}_t,\mathcal{H}_t)$ 映射为证据请求 $r_t$，如上式所示。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> A spatial tool or expert executes $r_t$ and returns an observation $o_t$, which is used to update both memory states:

$$
(\mathcal{S}_{t+1},\mathcal{H}_{t+1})=\operatorname{Update}(\mathcal{S}_t,\mathcal{H}_t,r_t,o_t).
$$

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 空间工具或专家执行 $r_t$ 并返回观测 $o_t$，该观测随后用于更新两种记忆状态，如上式所示。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The agent terminates when the accumulated evidence is sufficient to answer $q$. This formulation separates semantic planning from spatial evidence acquisition: the VLM decides what to measure or compare, while tools and memory provide scene-specific spatio-temporal evidence for the final reasoning. Unlike fixed pipelines or standard tool-use agents that treat each tool call as an isolated action, S-Agent conditions each evidence request on both the question and the evolving memory state. As a result, perception and geometric computation are invoked on demand, and their outputs remain reusable across later reasoning steps. The following sections describe the two core mechanisms of this framework: hierarchical spatial evidence acquisition (Section 2.1.1) and temporal memory for stateful reasoning (Section 2.1.2).

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 当累积证据足以回答 $q$ 时，智能体终止。这一表述将语义规划与空间证据获取分离开来：VLM 决定测量或比较什么，而工具与记忆为最终推理提供特定场景的时空证据。固定流程或标准工具使用智能体把每次工具调用视为孤立动作；与之不同，S-Agent 的每个证据请求都同时以问题和不断演化的记忆状态为条件。因此，感知与几何计算按需调用，其输出可在后续推理步骤中持续复用。下文将介绍该框架的两项核心机制：层级化空间证据获取（第 2.1.1 节）与用于有状态推理的时间记忆（第 2.1.2 节）。

#### 2.1.1. Hierarchical Spatial Evidence

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> S-Agent acquires spatial evidence through a three-level hierarchy that transforms raw 2D observations into explicit, scene-specific spatial knowledge. This hierarchy reflects the varying levels of evidence required by spatial tasks: some questions can be answered from localized image-level cues, while others require lifting those cues into 3D geometry or aggregating them through specialized spatial experts. This staged design keeps the VLM focused on semantic planning, while delegating scene-specific perception and spatial computation (e.g., visual localization, geometric recovery, and metric or relational computation) to tools whose outputs can also be stored and reused in memory.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> S-Agent 通过一个三级层级结构获取空间证据，将原始二维观测转化为显式、特定场景的空间知识。该层级结构反映了空间任务所需证据层次的差异：有些问题可依据局部图像级线索回答，另一些则需要将这些线索提升到三维几何空间，或通过专门的空间专家进行聚合。这种分阶段设计使 VLM 专注于语义规划，同时把特定场景的感知与空间计算（例如视觉定位、几何恢复，以及度量或关系计算）委托给工具；工具输出还可被存入记忆并复用。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> We denote the three tool levels as $\mathcal{T}^{(1)}$, $\mathcal{T}^{(2)}$, and $\mathcal{T}^{(3)}$, corresponding to 2D visual evidence acquisition, 2D-to-3D geometric lifting, and spatial knowledge aggregation, respectively. Given an evidence request $r_t$, S-Agent selects a tool or expert $T^{(k)}\in\mathcal{T}^{(k)}$ and produces an observation

$$
o_t=T^{(k)}(r_t,\mathcal{F},\mathcal{S}_t),\qquad k\in\{1,2,3\}.
$$

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 我们将三个工具层级记为 $\mathcal{T}^{(1)}$、$\mathcal{T}^{(2)}$ 和 $\mathcal{T}^{(3)}$，分别对应二维视觉证据获取、二维到三维的几何提升，以及空间知识聚合。给定证据请求 $r_t$，S-Agent 选择工具或专家 $T^{(k)}\in\mathcal{T}^{(k)}$，并按上式生成观测。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Depending on the selected level, $o_t$ may contain localized image-level cues, lifted 3D geometry, or high-level spatial knowledge.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 根据所选层级，$o_t$ 可以包含局部图像级线索、提升后的三维几何信息或高层空间知识。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Level 1: 2D Visual Evidence Acquisition (Figure 2(a-c)).** The first level identifies what visual evidence should be extracted from the raw 2D observations before higher-level spatial reasoning. Since videos or multi-view images contain many redundant, partial, or irrelevant views, S-Agent first gathers query-relevant image-level cues, such as selecting informative frames, grounding referred entities with VLMs, and localizing candidate regions with open-vocabulary detectors. These image-level cues can directly support simple queries, while also serving as observations for subsequent 3D lifting and spatial reasoning.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **第 1 层：二维视觉证据获取（图 2(a-c)）。** 第一层确定在进行更高层空间推理之前，应当从原始二维观测中提取哪些视觉证据。由于视频或多视角图像包含大量冗余、局部或无关视图，S-Agent 首先收集与查询相关的图像级线索，例如选择信息丰富的帧、使用 VLM 定位被指称实体，以及使用开放词表检测器定位候选区域。这些图像级线索既可直接支持简单查询，也可作为后续三维提升与空间推理的观测。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Level 2: 2D-to-3D Geometric Lifting (Figure 2(d-e)).** The second level lifts image-level evidence into a 3D-aware representation of the scene. Given the cues collected at Level 1, S-Agent invokes multi-view geometric tools to recover scene-level 3D information, such as depth structure, metric coordinates, camera poses, and bird’s-eye-view or novel-view evidence. This geometric lifting allows the agent to reason beyond the original image plane: fragmented 2D observations can be compared in a shared spatial context, apparent 2D size can be disambiguated from physical scale, and spatial relations can be evaluated with respect to camera motion or alternative viewpoints.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **第 2 层：二维到三维的几何提升（图 2(d-e)）。** 第二层将图像级证据提升为具备三维认知的场景表征。给定第 1 层收集的线索，S-Agent 调用多视角几何工具来恢复场景级三维信息，例如深度结构、度量坐标、相机位姿，以及鸟瞰视图或新视角证据。这种几何提升使智能体能够超越原始图像平面进行推理：碎片化二维观测可以在共享空间上下文中比较，表观二维尺寸可与物理尺度区分开来，并且空间关系可相对于相机运动或其他视点进行评估。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Level 3: Spatial Knowledge Aggregation (Figure 2(f-j)).** The third level abstracts the 2D and 3D cues collected in the previous stages into high-level, scene-specific spatial knowledge. To this end, S-Agent uses a set of specialized spatial experts, each responsible for a particular class of spatial queries, including counting, relative direction, object orientation, and physical size/distance. These experts aggregate the relevant evidence and return structured observations that can be directly consumed by the VLM planner for final reasoning. This design turns fragmented perceptual and geometric cues into explicit scene-level spatial knowledge, reducing the need for the VLM to perform unreliable metric or relational reasoning in free-form text.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **第 3 层：空间知识聚合（图 2(f-j)）。** 第三层将前几个阶段收集的二维与三维线索抽象为高层、特定场景的空间知识。为此，S-Agent 使用一组专门空间专家；每位专家负责某一类空间查询，包括计数、相对方向、对象朝向以及物理尺寸/距离。这些专家聚合相关证据并返回结构化观测，VLM 规划器可直接使用这些观测进行最终推理。该设计把碎片化的感知与几何线索转化为显式的场景级空间知识，降低了 VLM 以自由文本执行不可靠度量或关系推理的需要。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Details of the tools and experts used in Levels 1-3 are provided in Appendix B.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 第 1–3 层所用工具与专家的详细信息见附录 B。

#### 2.1.2. Temporal Memory for Stateful Reasoning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> To support stateful reasoning over continuous observations, S-Agent maintains two complementary memories: Scene Memory for reusable scene evidence and Agent Memory for the reasoning process. Each tool or expert observation from Section 2.1.1 updates both memories in different ways: its scene-relevant content is consolidated into Scene Memory, while the request, returned observation, and reasoning context are recorded in Agent Memory. This separation allows the VLM planner to reason over accumulated spatial knowledge while keeping track of what has been tried, what remains uncertain, and what evidence should be requested next.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 为了支持对连续观测的有状态推理，S-Agent 维护两种互补记忆：用于可复用场景证据的 Scene Memory，以及用于推理过程的 Agent Memory。第 2.1.1 节中的每项工具或专家观测都会以不同方式更新两种记忆：其中与场景相关的内容被整合进 Scene Memory，而请求、返回的观测和推理上下文被记录进 Agent Memory。这种分离使 VLM 规划器能够依据累积空间知识进行推理，同时跟踪已经尝试过什么、哪些内容仍不确定，以及下一步应请求何种证据。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Formally, after executing request $r_t$ and receiving observation $o_t$, each tool observation is decomposed into reusable scene evidence $e_t$ and process context $c_t$. The two memories are then updated with different operations:

$$
\mathcal{S}_{t+1}=\operatorname{Merge}(\mathcal{S}_t,e_t),\qquad
\mathcal{H}_{t+1}=\operatorname{Append}(\mathcal{H}_t,c_t).
$$

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 形式化地说，在执行请求 $r_t$ 并接收观测 $o_t$ 后，每项工具观测被分解为可复用场景证据 $e_t$ 和过程上下文 $c_t$。随后，两种记忆通过不同操作按上式更新。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Scene Memory merges $e_t$ into the current scene state, either by updating an existing entry or creating a new one, while Agent Memory appends $c_t$ to the reasoning trajectory.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Scene Memory 将 $e_t$ 合并到当前场景状态中，具体方式是更新已有条目或新建条目；Agent Memory 则将 $c_t$ 追加至推理轨迹。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Scene Memory (Figure 2(l-o)).** Scene Memory turns 2D/3D cues into a persistent, scene-level understanding. In multi-view images or videos, the same object may appear across different frames, viewpoints, scales, and referring expressions. Without a persistent memory, reasoning over these cues independently would lead to duplicated evidence and unstable object identity. Scene Memory therefore consolidates scene-relevant tool/expert observations into an evolving, entity-centric memory, binding repeated observations to persistent scene entities and accumulating their visual and geometric evidence over time. It is not a dense reconstruction of the full environment, but a question-conditioned spatial memory that preserves the evidence needed for the current query.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **Scene Memory（图 2(l-o)）。** Scene Memory 将二维/三维线索转化为持久的场景级理解。在多视角图像或视频中，同一对象可能跨不同帧、视点、尺度和指称表达出现。若无持久记忆，对这些线索分别进行推理将导致证据重复和对象身份不稳定。因此，Scene Memory 将与场景相关的工具/专家观测整合为不断演化的、以实体为中心的记忆，把重复观测绑定到持久场景实体，并随时间累积其视觉和几何证据。它并非对完整环境的稠密重建，而是一种以问题为条件、保留当前查询所需证据的空间记忆。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Concretely, Scene Memory stores two types of reusable content: grounded entities and derived spatial facts. For entities, the memory stores their textual aliases, supporting frames, localized visual evidence, and accumulated geometric attributes. For derived facts, it stores spatial relations or measurements computed by higher-level experts, together with the evidence from which they are derived. When a new observation arrives, S-Agent either links it to an existing scene memory entry or creates a new one, allowing later reasoning steps to reuse previously grounded evidence or facts instead of re-processing each frame from scratch.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 具体而言，Scene Memory 存储两类可复用内容：已定位实体和推导出的空间事实。对于实体，记忆存储其文本别名、支持帧、局部视觉证据和累积几何属性。对于推导事实，记忆存储由高层专家计算出的空间关系或测量结果，以及这些结果所依据的证据。当新观测到来时，S-Agent 会将其链接到已有场景记忆条目，或创建新条目，使后续推理步骤可以复用先前已定位的证据或事实，而不必从头重新处理每一帧。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Agent Memory (Figure 2(p-s)).** Agent Memory preserves the reasoning process that leads to the evolving scene understanding. In iterative tool-use reasoning, the agent should remember not only what has been observed, but also what has already been tried, which evidence was requested, which tools succeeded or failed, and why the planner decided to continue. Without such process memory, the planner may repeatedly issue redundant tool calls, overlook unresolved uncertainties, or contradict its earlier observations. Agent Memory therefore records the reasoning trajectory across iterations, providing the planner with a compact context for deciding the next evidence request.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **Agent Memory（图 2(p-s)）。** Agent Memory 保存导向演化场景理解的推理过程。在迭代式工具使用推理中，智能体不仅应记住已经观测到什么，还应记住已经尝试了什么、请求了哪些证据、哪些工具成功或失败，以及规划器为何决定继续。若缺少这种过程记忆，规划器可能重复发出冗余工具调用、忽视尚未解决的不确定性，或与先前观测相矛盾。因此，Agent Memory 记录跨迭代的推理轨迹，为规划器决定下一项证据请求提供紧凑上下文。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Specifically, Agent Memory stores the planner’s intermediate thoughts, issued tool calls, returned observations, failure messages, and intermediate conclusions. Unlike Scene Memory, which consolidates reusable scene evidence, Agent Memory keeps the procedural context around how that evidence was obtained and used. When the planner receives a new memory summary, it can identify missing evidence, revisit uncertain observations, or refine its strategy based on previous tool feedback.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 具体而言，Agent Memory 存储规划器的中间思考、已发出的工具调用、返回的观测、失败消息和中间结论。Scene Memory 整合可复用场景证据，而 Agent Memory 则保留这些证据如何被获取和使用的过程上下文。规划器接收新的记忆摘要后，可以识别缺失证据、重新审视不确定观测，或依据先前工具反馈细化策略。

### 2.2. Training-Time Distillation

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Beyond inference-time reasoning, S-Agent can also serve as a teacher for training compact spatial agents. We construct training data from SenseNova-SI-800K [5] by selecting samples that are both challenging for a weaker student model and likely to require tool use.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 除推理时推理外，S-Agent 还可以充当教师，用于训练紧凑型空间智能体。我们从 SenseNova-SI-800K [5] 中选择对较弱学生模型具有挑战、且很可能需要使用工具的样本，以此构建训练数据。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Data generation.** We estimate sample difficulty from multiple rollouts of Qwen3-VL-8B and prioritize questions on which the student is uncertain or unstable, rather than questions it already solves reliably. We further favor spatial questions that are likely to benefit from tool use, such as metric measurement, counting, relative position, camera/viewpoint reasoning, and grounding-dependent queries. A frozen teacher S-Agent, instantiated with GPT-5.4, is then used to generate complete trajectories, including planner prompts and responses, tool calls, tool observations, intermediate artifacts, memory states, final answers, and evaluation results.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **数据生成。** 我们根据 Qwen3-VL-8B 的多次 rollout 估计样本难度，并优先选择学生模型表现不确定或不稳定的问题，而不是它已经能够可靠解决的问题。我们进一步偏向可能从工具使用中获益的空间问题，例如度量测量、计数、相对位置、相机/视点推理，以及依赖定位的查询。随后，我们使用由 GPT-5.4 实例化的冻结教师 S-Agent 生成完整轨迹，其中包括规划器提示与响应、工具调用、工具观测、中间产物、记忆状态、最终答案和评估结果。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Data filtering.** We then apply quality filtering when exporting trajectories for supervised fine-tuning. All generated trajectories are first preserved in full as raw agent traces for analysis and possible re-export, regardless of whether the final answer is correct or whether some tool calls fail. For SFT data, we retain only trajectories with valid executions and correct final answers under answer-type-specific criteria. Multiple-choice questions require the predicted option in the final answer to match the ground-truth option, numeric questions are filtered by mean relative accuracy, and text questions are filtered by normalized answer matching. Importantly, tool usage itself is not used as a hard filtering criterion: the goal is to keep high-quality agent behavior while allowing the planner to decide when tool calls are necessary. The filtering ratio distribution is shown in Figure 3(a).

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **数据过滤。** 随后，我们在导出用于监督微调的轨迹时执行质量过滤。所有生成轨迹首先都被完整保留为原始智能体轨迹，以供分析及可能的再次导出，而不论最终答案是否正确、某些工具调用是否失败。对于 SFT 数据，我们仅保留执行有效且最终答案满足对应答案类型正确性标准的轨迹。多项选择题要求最终答案中预测的选项与真实选项一致；数值题使用平均相对准确率过滤；文本题使用归一化答案匹配过滤。重要的是，工具使用本身不被用作硬性过滤标准：目标是在保留高质量智能体行为的同时，允许规划器自行决定何时需要调用工具。过滤比例分布见图 3(a)。

### Figure 3. Data composition and tool invocation statistics of S-300K

![Figure 3](fig3_s300k_statistics.png)

**Caption:** Data composition and tool invocation statistics of S-300K.

**Caption[CN]:** S-300K 的数据组成与工具调用统计。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Data decomposition.** Each retained trajectory is finally decomposed into multiple forms of supervision rather than being used only as a final-answer example. We construct final-answer trajectories to teach end-to-end spatial reasoning, turn-level trajectories to teach iterative tool-use decisions under partial reasoning context, and expert/tool trajectories to improve spatial tool-use policy and expert-level reasoning. This decomposition converts a single teacher-agent rollout into multi-granularity training signals, enabling the student model to learn not only the final answer distribution, but also how to request evidence, interpret tool observations, and accumulate spatial knowledge across reasoning steps.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **数据分解。** 每条保留轨迹最终都被分解为多种监督形式，而不是仅作为最终答案样本使用。我们构造最终答案轨迹以教授端到端空间推理，构造回合级轨迹以教授在部分推理上下文下进行迭代式工具使用决策，并构造专家/工具轨迹以改进空间工具使用策略和专家级推理。这种分解把一次教师智能体 rollout 转换为多粒度训练信号，使学生模型不仅学习最终答案分布，还学习如何请求证据、解释工具观测，以及跨推理步骤累积空间知识。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> After this process, we obtain the S-300K dataset for supervised fine-tuning. We fine-tune Qwen3-VL-8B on S-300K to obtain our compact spatial agent, S-Agent-8B. The detailed data distribution of S-300K is shown in Figure 3(b). Further details are provided in Appendix C.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 经过这一过程，我们得到用于监督微调的 S-300K 数据集。我们在 S-300K 上微调 Qwen3-VL-8B，得到紧凑型空间智能体 S-Agent-8B。S-300K 的详细数据分布见图 3(b)，更多细节见附录 C。

## 3. Experiments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We conduct extensive experiments on a diverse suite of spatial reasoning benchmarks to evaluate S-Agent under both training-free zero-shot and trained-agent regimes. Section 3.1 introduces the training and evaluation setup. Section 3.2 reports the main zero-shot and comparative results, while Section 3.3 evaluates training compact agents from S-Agent trajectories. Section 3.4 presents ablations, and Section 3.5 analyzes qualitative examples and failure cases.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们在一组多样化的空间推理基准上开展广泛实验，以在免训练零样本和已训练智能体两种范式下评估 S-Agent。第 3.1 节介绍训练与评估设置；第 3.2 节报告主要零样本和比较结果；第 3.3 节评估如何从 S-Agent 轨迹训练紧凑型智能体；第 3.4 节给出消融实验；第 3.5 节分析定性示例和失败案例。

### Table 1. Detailed MMSI-Bench results

![Table 1](table1_mmsi_bench.png)

**Caption:** Detailed MMSI-Bench results. We follow the taxonomy of [31] and group dimensions into Positional Relationship, Geometric Attribute, Motion Perception, and Multi-step Reasoning (MSR). C/O/R denote camera/object/region in positional relation subcategories. SenseNova is abbreviated as SN. Top-1/top-2/ top-3 results are highlighted in deep, medium, and light lavender.

**Caption[CN]:** MMSI-Bench 详细结果。我们遵循 [31] 的分类法，将维度划分为位置关系、几何属性、运动感知和多步推理（MSR）。在位置关系子类别中，C/O/R 分别表示相机/对象/区域。SenseNova 简写为 SN。每列中除随机基线外的前 1/前 2/前 3 名结果分别以深、中、浅薰衣草色标出。

| Model | C-C | O-O | R-R | C-O | O-R | C-R | Meas. | Appr. | Cam. | Obj. | MSR | Avg. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| *Proprietary Models* |  |  |  |  |  |  |  |  |  |  |  |  |
| Gemini 3 Pro | 47.3 | 48.9 | 42.0 | 43.0 | 37.6 | 60.2 | 64.1 | 39.4 | 41.9 | 47.4 | 37.9 | 45.2 |
| Gemini 2.5 Pro | 38.7 | 34.0 | 40.7 | 44.2 | 38.8 | 41.0 | 62.5 | 30.3 | 39.2 | 25.0 | 33.3 | 38.0 |
| GPT-5.4 | 41.9 | 33.0 | 35.8 | 49.8 | 42.4 | 68.7 | 54.7 | 37.4 | 28.3 | 40.8 | 36.6 | 41.9 |
| Grok 4 | 36.6 | 36.2 | 39.5 | 34.9 | 45.0 | 40.2 | 41.9 | 22.7 | 40.5 | 43.4 | 38.8 | 37.8 |
| *Open-weight General Models* |  |  |  |  |  |  |  |  |  |  |  |  |
| Seed 1.6 | 36.6 | 36.2 | 32.1 | 32.6 | 42.4 | 46.9 | 48.4 | 33.0 | 31.1 | 42.1 | 40.4 | 38.5 |
| InternVL3.5-8B | 29.0 | 26.6 | 29.6 | 24.4 | 31.8 | 25.3 | 29.7 | 25.8 | 14.9 | 34.2 | 36.4 | 29.0 |
| SN-U1-8B-MoT | 46.2 | 41.5 | 29.6 | 58.1 | 38.8 | 63.9 | 43.8 | 21.2 | 25.7 | 31.6 | 26.8 | 38.0 |
| Qwen3-VL-8B-Instruct | 28.0 | 37.2 | 32.1 | 31.4 | 35.3 | 38.5 | 37.5 | 15.2 | 27.0 | 28.9 | 29.8 | 31.1 |
| Qwen3-VL-8B-Thinking | 31.2 | 26.6 | 32.1 | 29.1 | 32.9 | 30.1 | 50.0 | 16.7 | 17.6 | 23.7 | 27.3 | 28.6 |
| Qwen3-VL-8B | 34.4 | 36.2 | 34.6 | 39.5 | 38.8 | 54.2 | 56.3 | 28.8 | 36.5 | 26.3 | 28.8 | 36.5 |
| Qwen3-VL-8B-A3B-Thinking | 27.3 | 31.9 | 35.8 | 31.4 | 36.5 | 40.6 | 19.8 | 18.9 | 18.9 | 26.3 | 31.3 | 29.4 |
| *Open-weight Spatial Models* |  |  |  |  |  |  |  |  |  |  |  |  |
| SN-S1-1-Qwen2.5VL-7B | 51.6 | 29.8 | 32.1 | 50.0 | 29.4 | 42.2 | 37.5 | 28.8 | 23.0 | 34.2 | 18.7 | 32.8 |
| SN-S1-1-Qwen3VL-8B | 44.1 | 31.3 | 33.8 | 65.1 | 38.8 | 59.0 | 48.4 | 29.7 | 29.7 | 34.2 | 22.2 | 38.1 |
| VST-7B-SFT | 39.8 | 36.2 | 35.8 | 37.2 | 29.4 | 33.7 | 29.7 | 47.0 | 36.5 | 35.5 | 18.2 | 32.5 |
| **Ours (S-Agent)** | **46.2 (+7.2)** | **43.6 (+7.4)** | **37.0 (+7.4)** | **43.0 (+18.6)** | **43.5 (+11.7)** | **63.9 (+18.4)** | **57.8 (+8.4)** | **40.9 (+15.1)** | **46.0 (+14.1)** | **48.7 (+14.5)** | **44.4 (+17.4)** | **46.4 (+17.4)** |

### 3.1. Experimental Setup

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Benchmarks.** We evaluate S-Agent on four benchmarks that stress different forms of spatial reasoning across multi-image and video inputs. For *multi-image reasoning*, **MMSI-Bench** [31] provides multiple images of the same scene and tests whether models can integrate evidence across views for positional relationships, geometric attributes, motion perception, and multi-step spatial reasoning. **ViewSpatial-Bench** [12] focuses more specifically on perspective-aware localization, requiring models to locate objects or infer positions under different camera viewpoints. For *video reasoning*, **ReVSI** [37] evaluates 3D spatial reasoning from dynamic observations, emphasizing whether models can infer spatial relations that are not reliably recoverable from isolated frames. **VSI-SUPER** [30] focuses on video spatial change reasoning, requiring models to identify how objects, viewpoints, or spatial layouts change over time.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **基准。** 我们在四个基准上评估 S-Agent，这些基准覆盖多图像和视频输入中的不同空间推理形式。对于*多图像推理*，**MMSI-Bench** [31] 提供同一场景的多张图像，并测试模型能否跨视图整合证据，以完成位置关系、几何属性、运动感知和多步空间推理。**ViewSpatial-Bench** [12] 更具体地聚焦于视角感知的定位，要求模型在不同相机视点下定位对象或推断位置。对于*视频推理*，**ReVSI** [37] 从动态观测中评估三维空间推理，强调模型能否推断无法从孤立帧中可靠恢复的空间关系。**VSI-SUPER** [30] 聚焦于视频空间变化推理，要求模型识别对象、视点或空间布局如何随时间变化。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Baselines.** We compare S-Agent with three categories of baselines: advanced proprietary VLMs (e.g., Gemini 3 Pro, GPT-5.4, and Grok 4), open-weight general VLMs (e.g., Qwen series), and spatially specialized models (e.g., Cambrian-S, VST-SFT, and SenseNova-SI series). The first two groups measure performance against strong general-purpose multimodal systems, while the third evaluates whether S-Agent can compete with models explicitly trained or tuned for spatial reasoning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **基线。** 我们将 S-Agent 与三类基线进行比较：先进的专有 VLM（例如 Gemini 3 Pro、GPT-5.4 和 Grok 4）、开放权重通用 VLM（例如 Qwen 系列），以及空间专用模型（例如 Cambrian-S、VST-SFT 和 SenseNova-SI 系列）。前两组衡量其相对于强大通用多模态系统的性能，第三组则评估 S-Agent 是否能够与显式接受空间推理训练或调优的模型竞争。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Models.** In the zero-shot setting, we instantiate S-Agent with advanced VLMs (GPT-5.4 and Gemini 3 Pro) as tool-calling planners, without any task-specific training. In the trained-agent setting, we use Qwen3-VL-8B-Instruct as the backbone planner and train it on trajectories generated by zero-shot S-Agent, yielding our compact agent S-Agent-8B.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **模型。** 在零样本设置中，我们以先进 VLM（GPT-5.4 和 Gemini 3 Pro）作为工具调用规划器来实例化 S-Agent，且不进行任何任务特定训练。在已训练智能体设置中，我们使用 Qwen3-VL-8B-Instruct 作为骨干规划器，并在零样本 S-Agent 生成的轨迹上进行训练，得到紧凑型智能体 S-Agent-8B。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Training Data.** We construct training data from SenseNova-SI-800K [5], which is fully disjoint from all evaluation benchmarks. We randomly sample 100K questions and use zero-shot S-Agent with GPT-5.4 as the planner to generate tool-use trajectories. We then filter the trajectories based on execution validity and final-answer correctness, and decompose the retained trajectories into final-answer samples, turn-level VLM-call samples, and expert/tool-specific samples. This yields 292,391 SFT samples, denoted as S-300K. Appendix C provides the detailed filtering criteria and data distribution.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **训练数据。** 我们从与所有评估基准完全不相交的 SenseNova-SI-800K [5] 构建训练数据。我们随机采样 10 万个问题，并使用以 GPT-5.4 为规划器的零样本 S-Agent 生成工具使用轨迹。随后，我们根据执行有效性和最终答案正确性过滤轨迹，并将保留轨迹分解为最终答案样本、回合级 VLM 调用样本以及专家/工具特定样本。这产生了 292,391 个 SFT 样本，记为 S-300K。附录 C 给出了详细的过滤标准和数据分布。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Training Configuration.** We fine-tune Qwen3-VL-8B-Instruct on S-300K using LLaMA-Factory [39] with the `qwen3_vl_nothink` template on 8× B200 GPUs. The model is trained with the standard supervised next-token prediction objective over assistant responses, including serialized tool-use trajectories, tool observations, and final answers. We use a maximum sequence length of 8192, a learning rate of $5\times10^{-5}$, cosine learning-rate decay with 3% warmup, and train for one epoch. The resulting compact spatial agent is denoted as S-Agent-8B.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **训练配置。** 我们使用 LLaMA-Factory [39]，采用 `qwen3_vl_nothink` 模板，在 8× B200 GPU 上对 Qwen3-VL-8B-Instruct 进行 S-300K 微调。模型采用标准的监督式下一 token 预测目标，在助手响应上训练，其中包括序列化工具使用轨迹、工具观测和最终答案。我们使用 8192 的最大序列长度、$5\times10^{-5}$ 的学习率、带有 3% 预热的余弦学习率衰减，并训练一个 epoch。所得紧凑型空间智能体记为 S-Agent-8B。

### Table 2. Results on ViewSpatial-Bench

![Table 2](table2_viewspatial_bench.png)

**Caption:** Results on ViewSpatial-Bench [12]. We report the official five question types: camera-perspective object view orientation (C-OVO), camera-perspective relative direction (C-RD), person-perspective object view orientation (P-OVO), person-perspective relative direction (P-RD), and person-perspective scene-simulation relative direction (P-SSRD).

**Caption[CN]:** ViewSpatial-Bench [12] 的结果。我们报告官方的五类问题：相机视角对象视图朝向（C-OVO）、相机视角相对方向（C-RD）、人物视角对象视图朝向（P-OVO）、人物视角相对方向（P-RD），以及人物视角场景模拟相对方向（P-SSRD）。

| Model | C-OVO | C-RD | P-OVO | P-RD | P-SSRD | Avg. |
|---|---:|---:|---:|---:|---:|---:|
| *Proprietary Models* |  |  |  |  |  |  |
| Gemini 3 Pro | 31.6 | 61.9 | 41.1 | 74.4 | 38.9 | 50.4 |
| Gemini 2.5 Pro | 33.0 | 59.1 | 51.0 | 45.8 | 32.6 | 46.1 |
| GPT-5.4 | 27.9 | 60.2 | 41.0 | 48.5 | 40.1 | 43.6 |
| Grok 4 | 23.9 | 57.1 | 47.8 | 51.7 | 24.9 | 43.2 |
| *Open-weight General Models* |  |  |  |  |  |  |
| Seed-1.6 | 26.9 | 55.8 | 54.8 | 48.5 | 26.6 | 43.9 |
| Qwen3-VL-8B-Instruct | 29.7 | 54.2 | 47.3 | 40.3 | 31.1 | 42.2 |
| BAIR-VL-7B-MoT | 38.2 | 48.3 | 57.0 | 42.5 | 25.5 | 41.3 |
| InternVL3.5-8B | 24.7 | 49.8 | 50.3 | 34.6 | 32.9 | 40.0 |
| *Open-weight Spatial Models* |  |  |  |  |  |  |
| Cambrian-S-7B | 27.7 | 50.4 | 45.0 | 38.8 | 41.9 | 41.3 |
| VST-3B-SFT | 35.4 | 46.9 | 70.3 | 52.6 | 62.8 | 52.9 |
| VST-7B-SFT | 29.6 | 52.7 | 51.9 | 50.7 | 64.5 | 50.5 |
| SN-S1-1-Qwen2.5VL-7B | 26.7 | 47.9 | 57.1 | 43.2 | 49.7 | 45.5 |
| SN-S1-1-Qwen3VL-8B | 22.0 | 60.3 | 67.8 | 41.5 | 55.6 | 51.2 |
| **Ours (S-Agent)** | **55.5 (+27.6)** | **62.5 (+2.3)** | **42.2 (+1.2)** | **81.1 (+32.6)** | **60.6 (+20.5)** | **60.0** |

### 3.2. Zero-Shot Performance

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We report the results on MMSI-Bench, ViewSpatial-Bench, and ReVSI in the main text, while the results on VSI-SUPER are provided in Appendix D.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们在正文中报告 MMSI-Bench、ViewSpatial-Bench 和 ReVSI 的结果，而 VSI-SUPER 的结果见附录 D。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Results on MMSI-Bench.** Table 1 shows that our S-Agent achieves the best overall zero-shot performance on MMSI-Bench, obtaining the highest average score of 46.4%. It outperforms the strongest proprietary baseline Gemini 3 Pro by 1.2%, and surpasses GPT-5.4 by 4.5%. Notably, S-Agent achieves the best results on both motion perception subtasks, i.e., camera motion (46.0%) and object motion (48.7%), as well as multi-step reasoning (44.4%), while remaining competitive across positional and geometric categories. These results demonstrate the effectiveness of S-Agent for zero-shot spatial reasoning, particularly strong performance on dynamic motion understanding and multi-step reasoning while maintaining robust results across static spatial and geometric tasks.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **MMSI-Bench 结果。** 表 1 显示，我们的 S-Agent 在 MMSI-Bench 上取得最佳整体零样本性能，获得最高平均分 46.4%。它比最强的专有基线 Gemini 3 Pro 高 1.2%，并比 GPT-5.4 高 4.5%。值得注意的是，S-Agent 在两个运动感知子任务——相机运动（46.0%）和对象运动（48.7%）——以及多步推理（44.4%）上均取得最佳结果，同时在位置和几何类别上保持竞争力。这些结果证明了 S-Agent 对零样本空间推理的有效性；它在动态运动理解和多步推理上尤其强大，同时在静态空间和几何任务上保持稳健结果。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Results on ViewSpatial-Bench.** Table 2 reports the zero-shot results on ViewSpatial-Bench. S-Agent achieves an average score of 60.0%, outperforming GPT-5.4 by 14.4%. It obtains the best performance on C-OVO (55.5%) and P-RD (81.1%), showing strong capability in both camera-centered and person-centered spatial reasoning. S-Agent also brings large gains on the more challenging P-SSRD split, improving over GPT-5.4 by 20.5%. These results further demonstrate the effectiveness of S-Agent for zero-shot view-aware spatial reasoning, especially when reasoning over relative directions and perspective-dependent spatial relations.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **ViewSpatial-Bench 结果。** 表 2 报告了 ViewSpatial-Bench 的零样本结果。S-Agent 取得 60.0% 的平均分，比 GPT-5.4 高 14.4%。它在 C-OVO（55.5%）和 P-RD（81.1%）上表现最佳，显示出在以相机为中心和以人为中心的空间推理中均具有强大能力。S-Agent 在更具挑战性的 P-SSRD 划分上也带来显著增益，比 GPT-5.4 高 20.5%。这些结果进一步证明 S-Agent 对零样本视角感知空间推理的有效性，尤其是在针对相对方向和依赖视角的空间关系进行推理时。

### Table 3. Detailed comparison on the ReVSI leaderboard

![Table 3](table3_revsi_leaderboard.png)

**Caption:** Detailed comparison on the ReVSI [37] leaderboard. ReVSI scores are shown as the main values, and corresponding VSI-Bench scores from the official ReVSI experiments page are shown in gray parentheses when available. We follow the official evaluation dimensions: four numerical question types (object counting, absolute distance, object size, and room size) and three multiple-choice question types (relative distance, relative direction, and route planning). The top-1 / top-2 / top-3 ReVSI results in each column, excluding chance baselines, are highlighted with deep, medium, and light lavender.

**Caption[CN]:** ReVSI [37] 排行榜的详细比较。ReVSI 分数显示为主要数值；在可用时，官方 ReVSI 实验页面中的对应 VSI-Bench 分数以灰色括号给出。我们遵循官方评估维度：四类数值问题（对象计数、绝对距离、对象尺寸和房间尺寸）以及三类多项选择问题（相对距离、相对方向和路径规划）。每列中除随机机会基线外的前 1 / 前 2 / 前 3 名 ReVSI 结果分别以深、中、浅薰衣草色标出。

| Model | Frames | Obj. Cnt. | Abs. Dist. | Obj. Size | Room Size | Rel. Dist. | Rel. Dir. | Route Plan | Avg. |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| *Baseline* |  |  |  |  |  |  |  |  |  |
| Chance (Random) | ALL | — | — | — | — | 23.7 | 26.8 | 26.0 | — |
| Chance (Frequency) | ALL | 52.2 | 40.1 | 17.4 | 20.9 | 25.8 | 31.9 | 30.2 | 31.4 |
| *Proprietary Models (API)* |  |  |  |  |  |  |  |  |  |
| GPT-5.2 | 64 | 56.2 | 41.5 | 73.9 | 63.0 | 48.4 | 34.9 | 38.2 | 50.9 |
| Gemini 3 Flash | 1 FPS | 65.7 | 53.1 | 77.6 | 52.8 | 64.6 | 47.9 | 41.8 | 57.6 |
| Gemini 3 Pro | 1 FPS | 60.1 | 54.7 | 79.3 | 51.9 | 68.1 | 56.5 | 56.4 | 60.9 |
| *Open-Source General Models* |  |  |  |  |  |  |  |  |  |
| Qwen3-VL-8B-Instruct | 64 | 40.4 | 52.3 | 69.0 | 45.1 | 57.1 | 39.5 | 40.5 | 49.1 |
| Qwen3-VL-32B-Instruct | 64 | 46.9 | 65.0 | 70.4 | 55.8 | 53.8 | 34.0 | 47.3 | 53.3 |
| InternVL3.5-8B | 64 | 43.3 | 54.6 | 64.2 | 47.6 | 45.0 | 36.3 | 44.4 | 47.9 |
| InternVL3.5-38B | 64 | 43.8 | 60.6 | 70.2 | 58.4 | 57.4 | 45.9 | 42.7 | 54.1 |
| LLaVA-Video-7B-Qwen2 | 64 | 31.3 | 1.4 | 52.5 | 16.7 | 38.3 | 33.3 | 38.4 | 30.3 |
| LLaVA-Video-72B-Qwen2 | 64 | 29.6 | 59.3 | 27.9 | 29.7 | 39.6 | 24.8 | 43.0 | 37.8 |
| *Spatially Specialized Models and Base Models* |  |  |  |  |  |  |  |  |  |
| Cambrian-S-7B | 128 | 48.4 | 60.5 | 65.5 | 46.7 | 37.1 | 48.5 | 37.0 | 49.1 |
| Qwen2.5-VL-7B-Instruct | 4 FPS | 36.9 | 15.0 | 49.7 | 29.0 | 31.5 | 29.5 | 36.7 | 32.6 |
| VST-7B-SFT | 4 FPS | 35.4 | 52.6 | 67.9 | 47.2 | 49.2 | 36.9 | 35.4 | 46.4 |
| Qwen2.5-VL-7B-Instruct | 32 | 34.3 | 21.7 | 45.5 | 35.1 | 32.6 | 33.7 | 34.1 | 33.9 |
| SpaceR-7B (SG-RLVR) | 32 | 30.7 | 34.5 | 52.0 | 18.6 | 22.8 | 34.5 | 20.2 | 30.5 |
| Qwen2.5-VL-3B-Instruct | 16 | 18.7 | 15.6 | 16.8 | — | 33.2 | 34.3 | — | 23.7 |
| Spatial-MLLM-4B-135k | 16 | 40.7 | 45.3 | 46.8 | — | 32.3 | 37.4 | — | 40.5 |
| Spatial-MLLM-4B-820k | 16 | 41.5 | 40.0 | 53.1 | — | 30.7 | 39.2 | — | 40.9 |
| LLaVA-Video-7B-Qwen2 | 32 | 29.9 | 1.5 | 53.0 | 19.3 | 39.1 | 33.8 | 38.8 | 30.8 |
| VLMR3-7B | 32 | 41.6 | 61.6 | 64.8 | 52.5 | 46.5 | 49.5 | 34.1 | 50.1 |
| **Ours (S-Agent)** | **64** | **54.0** | **45.6** | **62.6** | **53.4** | **63.6** | **66.4** | **66.1** | **58.8** |

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Results on ReVSI.** Table 3 reports detailed results on ReVSI. S-Agent achieves an average score of 58.8, ranking second overall and outperforming all open-source general models and spatially specialized baselines. The gains are especially pronounced on multiple-choice spatial reasoning tasks: S-Agent obtains the best results on relative direction and route planning, and ranks third on relative distance. These categories require integrating evidence across frames and viewpoints rather than relying on a single visual impression, which aligns well with the design of stateful evidence accumulation.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **ReVSI 结果。** 表 3 报告了 ReVSI 上的详细结果。S-Agent 取得 58.8 的平均分，整体排名第二，并优于所有开源通用模型和空间专用基线。其增益在多项选择空间推理任务上尤为明显：S-Agent 在相对方向和路径规划上取得最佳结果，并在相对距离上排名第三。这些类别要求跨帧和视点整合证据，而非依赖单一视觉印象，这与有状态证据累积的设计高度契合。

### 3.3. Trajectory Distillation from S-Agent

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We evaluate whether the reasoning trajectories generated by S-Agent can be used to train a smaller open-weight spatial agent. Specifically, we fine-tune Qwen3-VL-8B-Instruct on S-300K and obtain S-Agent-8B. Table 4 compares S-Agent-8B with proprietary VLMs, the original Qwen3-VL-8B-Instruct, and S-Agent using the same Qwen3-VL-8B backbone. A key observation is that simply equipping the base Qwen3-VL-8B-Instruct with S-Agent does not consistently improve performance. The base 8B planner often struggles with tool selection and noisy tool observations, so tool use can bring limited gains or even hurt performance.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们评估 S-Agent 生成的推理轨迹能否用于训练更小的开放权重空间智能体。具体而言，我们在 S-300K 上微调 Qwen3-VL-8B-Instruct，得到 S-Agent-8B。表 4 将 S-Agent-8B 与专有 VLM、原始 Qwen3-VL-8B-Instruct，以及使用相同 Qwen3-VL-8B 骨干的 S-Agent 进行比较。一个关键观察是，仅为基础 Qwen3-VL-8B-Instruct 配备 S-Agent 并不能始终提升性能。基础 8B 规划器经常难以进行工具选择并处理带噪工具观测，因此使用工具可能只带来有限增益，甚至损害性能。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In contrast, S-Agent-8B consistently improves over both the base Qwen3-VL-8B-Instruct and S-Agent with the same 8B planner across the three main benchmarks. This shows that trajectory distillation teaches not only spatial answers, but also reusable tool-use and evidence-integration patterns for spatial reasoning. Notably, S-Agent-8B also achieves competitive performance compared with state-of-the-art proprietary models such as GPT-5.4 and Gemini 3 Pro.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 相比之下，S-Agent-8B 在三个主要基准上均持续优于基础 Qwen3-VL-8B-Instruct 和采用相同 8B 规划器的 S-Agent。这表明轨迹蒸馏不仅教授空间答案，还教授可复用的工具使用和证据整合模式，以进行空间推理。值得注意的是，S-Agent-8B 与 GPT-5.4、Gemini 3 Pro 等最先进专有模型相比也取得了有竞争力的性能。

### Table 4. Trajectory distillation results across three main spatial reasoning benchmarks

![Table 4](table4_trajectory_distillation.png)

**Caption:** Trajectory distillation results across three main spatial reasoning benchmarks.

**Caption[CN]:** 三个主要空间推理基准上的轨迹蒸馏结果。

| Model | MMSI | ViewSpatial | ReVSI |
|---|---:|---:|---:|
| *Proprietary VLMs* |  |  |  |
| Gemini 3 Pro | 45.2 | 50.4 | 60.9 |
| GPT-5.4 | 41.9 | 45.6 | — |
| *Open-weight Models* |  |  |  |
| Qwen3-VL-8B-Instruct | 31.1 | 42.2 | 49.1 |
| S-Agent (Qwen3-VL-8B) | 30.7 | 44.1 | 49.5 |
| **S-Agent-8B** | **41.6** | **46.8** | **58.2** |

### 3.4. Ablation Studies

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We ablate the spatial evidence hierarchy and memory modules of S-Agent on ViewSpatial using GPT-5.4 as the planner. As shown in Table 5, adding Level-1 2D evidence improves the VLM-only baseline from 45.6% to 49.0%, showing that explicit visual grounding provides useful support for spatial reasoning. However, directly adding Level-2 3D evidence provides limited benefit. We observe that raw 3D evidence often contains dense numerical information, such as camera poses, depth values, and noisy reconstructed points, which can be difficult for the VLM planner to interpret and may even distract from the task-relevant spatial cues.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们以 GPT-5.4 为规划器，在 ViewSpatial 上消融 S-Agent 的空间证据层级和记忆模块。如表 5 所示，加入第 1 层二维证据可将仅 VLM 基线从 45.6% 提升到 49.0%，表明显式视觉定位为空间推理提供了有益支持。然而，直接加入第 2 层三维证据带来的收益有限。我们观察到，原始三维证据通常包含密集的数值信息，例如相机位姿、深度值和带噪重建点；这些信息可能难以被 VLM 规划器解释，甚至会使其偏离与任务相关的空间线索。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In contrast, enabling Level-3 3D experts substantially improves the score to 56.7%. This suggests that 3D evidence becomes most useful when it is filtered and interpreted by specialized experts, which convert noisy geometric outputs into task-oriented measurements, relative positions, or spatial conclusions. The memory modules provide additional gains: scene memory improves the score to 58.2%, agent memory improves it to 57.6%, and combining both yields the full S-Agent score of 60.0%. These results show that S-Agent benefits from both structured spatial evidence and persistent memory, with expert-mediated interpretation being crucial for effectively using 3D information.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 相比之下，启用第 3 层三维专家可将得分大幅提升至 56.7%。这表明，当三维证据由专门专家进行过滤和解释时最为有用；这些专家将带噪几何输出转化为面向任务的测量、相对位置或空间结论。记忆模块带来额外增益：场景记忆将得分提升至 58.2%，智能体记忆将其提升至 57.6%，二者结合则得到完整 S-Agent 的 60.0% 得分。这些结果表明，S-Agent 同时受益于结构化空间证据和持久记忆，其中专家介导的解释对于有效利用三维信息至关重要。

### Table 5. Ablation on ViewSpatial with S-Agent using GPT-5.4 as the planner

![Table 5](table5_ablation_viewspatial.png)

**Caption:** Ablation on ViewSpatial with S-Agent using GPT-5.4 as the planner.

**Caption[CN]:** 以 GPT-5.4 为规划器的 S-Agent 在 ViewSpatial 上的消融实验。

| S-Agent | Evidence L1 | Evidence L2 | Evidence L3 | Scene Memory | Agent Memory | Avg. |
|---|:---:|:---:|:---:|:---:|:---:|---:|
| *Spatial evidence ablation* |  |  |  |  |  |  |
| VLM-only |  |  |  |  |  | 45.6 |
| + Level-1 2D evidence | ✓ |  |  |  |  | 49.0 |
| + Level-2 3D evidence | ✓ | ✓ |  |  |  | 49.8 |
| + Level-3 3D experts | ✓ | ✓ | ✓ |  |  | 56.7 |
| *Memory ablation* |  |  |  |  |  |  |
| Spatial only | ✓ | ✓ | ✓ |  |  | 56.7 |
| + Scene memory | ✓ | ✓ | ✓ | ✓ |  | 58.2 |
| + Agent memory | ✓ | ✓ | ✓ |  | ✓ | 57.6 |
| + Full S-Agent | ✓ | ✓ | ✓ | ✓ | ✓ | 60.0 |

### 3.5. Qualitative Analysis

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We provide qualitative examples to illustrate how S-Agent obtains explicit spatial evidence before answering. Figure 4 shows a relative-position question in a first-person video. A direct VLM response struggles with this case because the queried objects are partially occluded and not both clearly visible in the target view. Without grounded evidence, it relies on the apparent 2D layout and incorrectly guesses that the shelf is in the front-right direction.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们提供定性示例来说明 S-Agent 如何在作答前获取显式空间证据。图 4 展示了第一人称视频中的一个相对位置问题。直接的 VLM 响应难以处理该案例，因为被查询的对象部分被遮挡，且在目标视图中并非都清晰可见。没有有根基的证据时，它依赖表观二维布局，并错误地猜测书架位于右前方。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In contrast, S-Agent follows a tool-grounded trajectory. Although the initial grounding tool fails to locate both queried objects, the agent does not answer immediately. It instead issues targeted detection calls over the video frames, using both the original object names, “shelf” and “telephone”, and a semantically related query, “desk phone”. These calls recover usable boxes for the shelf and telephone. The relative-position expert then lifts the selected boxes into a metric 3D representation via the depth tool and constructs a bird’s-eye-view layout. In this layout, the shelf is estimated at $(-0.52, 1.21)$ and the telephone at $(-0.34, 1.46)$. The recovered geometry shows that the shelf is to the left of and behind the telephone, leading to the correct answer.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 相比之下，S-Agent 遵循一条由工具支撑的轨迹。尽管初始定位工具未能同时定位两个被查询对象，智能体并未立即作答。它转而在视频帧上发出有针对性的检测调用，同时使用原始对象名称“shelf”和“telephone”，以及语义相关查询“desk phone”。这些调用恢复了书架和电话的可用边界框。随后，相对位置专家通过深度工具将选定边界框提升为度量三维表征，并构建鸟瞰布局。在该布局中，书架估计为 $(-0.52, 1.21)$，电话估计为 $(-0.34, 1.46)$。恢复出的几何关系表明书架位于电话左侧且后方，从而得到正确答案。

### Figure 4. Tool-grounded spatial reasoning example

![Figure 4](fig4_tool_grounded_reasoning.png)

**Caption:** Qualitative example of tool-grounded spatial reasoning. Unlike vanilla VLMs that fail on incomplete cues, our approach accurately infers 3D relations using hierarchical spatial tools and a depth-guided position expert.

**Caption[CN]:** 工具支撑空间推理的定性示例。不同于会在不完整线索上失败的原始 VLM，我们的方法使用层级化空间工具和深度引导的位置专家，准确推断三维关系。

### Figure 5. Additional qualitative visualizations

![Figure 5](fig5_qualitative_main.png)

**Caption:** Additional qualitative visualizations of S-Agent across representative spatial reasoning tasks.

**Caption[CN]:** S-Agent 在代表性空间推理任务上的更多定性可视化。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Beyond the detailed case in Figure 4, Figure 5 provides broader qualitative visualizations across diverse spatial reasoning scenarios, including absolute distance estimation, object size estimation, object counting, multi-step reasoning, relative position reasoning, and route planning. These examples show that S-Agent does not rely on a fixed prompt or a single type of visual cue. Instead, it dynamically invokes different tools and experts according to the task, such as metric measurement for distance and size, key-frame selection and counting tools for object enumeration, 3D lifting for relational reasoning, and route-oriented evidence aggregation for navigation-style questions. Across these cases, S-Agent selects evidence frames, grounds relevant objects, lifts visual observations into metric or top-down spatial evidence, and aggregates the recovered evidence into a final answer.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 除图 4 的详细案例外，图 5 还在多样的空间推理场景中提供了更广泛的定性可视化，包括绝对距离估计、对象尺寸估计、对象计数、多步推理、相对位置推理和路径规划。这些示例表明，S-Agent 不依赖固定提示或单一类型的视觉线索。相反，它会根据任务动态调用不同工具和专家，例如使用度量测量处理距离和尺寸，使用关键帧选择和计数工具进行对象枚举，使用三维提升进行关系推理，以及对导航类问题进行面向路径的证据聚合。在这些案例中，S-Agent 选择证据帧、定位相关对象、将视觉观测提升为度量或俯视空间证据，并将恢复的证据聚合为最终答案。

## 4. Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We introduce S-Agent, a spatial tool-use agentic framework for spatial reasoning over continuous multi-view images and videos. Instead of treating spatial reasoning as a single-shot prediction from isolated visual inputs, S-Agent formulates it as a process of spatio-temporal evidence accumulation. It uses a VLM planner to actively acquire hierarchical spatial evidence, from 2D grounding to 3D geometric lifting and expert-level spatial knowledge, while maintaining scene and agent memories for stateful reasoning across views, frames, and tool-use steps. Extensive experiments show that S-Agent consistently improves strong VLMs in the training-free zero-shot setting, especially on motion, perspective-aware, and multi-step spatial reasoning tasks. Furthermore, trajectories generated by S-Agent can be distilled into S-Agent-8B, enabling an open-weight 8B model to learn more reliable tool-use and spatial evidence integration. These results suggest that agentic evidence accumulation is a promising direction for building VLMs with stronger and more grounded spatial intelligence.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们提出 S-Agent：一个用于连续多视角图像和视频空间推理的空间工具使用智能体框架。S-Agent 不将空间推理视为从孤立视觉输入进行的一次性预测，而是将其表述为时空证据累积过程。它使用 VLM 规划器主动获取层级化空间证据，覆盖从二维定位到三维几何提升和专家级空间知识，同时维护场景记忆和智能体记忆，以便跨视图、跨帧和跨工具使用步骤进行有状态推理。广泛实验表明，S-Agent 在免训练零样本设置中持续提升强大 VLM，尤其是在运动、视角感知和多步空间推理任务上。进一步地，S-Agent 生成的轨迹可被蒸馏到 S-Agent-8B 中，使一个开放权重 8B 模型学习更可靠的工具使用和空间证据整合。这些结果表明，智能体式证据累积是构建具有更强、更有根基空间智能的 VLM 的一条有前景方向。

## References

Bibliography entries are retained in their original searchable form and are not translated.

[1] Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katie Millican, Malcolm Reynolds, Roman Ring, Eliza Rutherford, Serkan Cabi, Tengda Han, Zhitao Gong, Sina Samangooei, Marianne Monteiro, Jacob Menick, Sebastian Borgeaud, and 8 others. 2022. Flamingo: a visual language model for few-shot learning. Preprint, arXiv:2204.14198.

[2] Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding, Danny Driess, Avinava Dubey, Chelsea Finn, Pete Florence, Chuyuan Fu, Montse Gonzalez Arenas, Keerthana Gopalakrishnan, Kehang Han, Karol Hausman, Alexander Herzog, Jasmine Hsu, Brian Ichter, and 35 others. 2023. Rt-2: Vision-language-action models transfer web knowledge to robotic control. Preprint, arXiv:2307.15818.

[3] Ellis Brown, Jihan Yang, Shusheng Yang, Rob Fergus, and Saining Xie. 2025. Benchmark designers should "train on the test set" to expose exploitable non-visual shortcuts. Preprint, arXiv:2511.04655.

[4] Holger Caesar, Varun Bankiti, Alex H. Lang, Sourabh Vora, Venice Erin Liong, Qiang Xu, Anush Krishnan, Yu Pan, Giancarlo Baldan, and Oscar Beijbom. 2020. nuscenes: A multimodal dataset for autonomous driving. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 11621–11631.

[5] Zhongang Cai, Ruisi Wang, Chenyang Gu, Fanyi Pu, Junxiang Xu, Yubo Wang, Wanqi Yin, Zhitao Yang, Chen Wei, Qingping Sun, Tongxi Zhou, Jiaqi Li, Hui En Pang, Oscar Qian, Yukun Wei, Zhiqian Lin, Xuanke Shi, Kewang Deng, Xiaoyang Han, and 10 others. 2026. Scaling spatial intelligence with multimodal foundation models. Preprint, arXiv:2511.13719.

[6] Siyi Chen, Mikaela Angelina Uy, Chan Hee Song, Faisal Ladhak, Adithyavairavan Murali, Qing Qu, Stan Birchfield, Valts Blukis, and Jonathan Tremblay. 2025. Spacetools: Tool-augmented spatial reasoning via double interactive rl. Preprint, arXiv:2512.04069.

[7] Zeren Chen, Xiaoya Lu, Zhijie Zheng, Pengrui Li, Lehan He, Yijin Zhou, Jing Shao, Bohan Zhuang, and Lu Sheng. 2025. Geometrically-constrained agent for spatial reasoning. Preprint, arXiv:2511.22659.

[8] Danny Driess, Fei Xia, Mehdi S. M. Sajjadi, Corey Lynch, Aakanksha Chowdhery, Brian Ichter, Ayzaan Wahid, Jonathan Tompson, Quan Vuong, Tianhe Yu, Wenlong Huang, Yevgen Chebotar, Pierre Sermanet, Daniel Duckworth, Sergey Levine, Vincent Vanhoucke, Karol Hausman, Marc Toussaint, Klaus Greff, and 3 others. 2023. Palm-e: An embodied multimodal language model. Preprint, arXiv:2303.03378.

[9] Mengfei Du, Binhao Wu, Zejun Li, Xuanjing Huang, and Zhongyu Wei. 2024. Embspatial-bench: Benchmarking spatial understanding for embodied tasks with large vision-language models. Preprint, arXiv:2406.05756.

[10] Xingyu Fu, Yushi Hu, Bangzheng Li, Yu Feng, Haoyu Wang, Xudong Lin, Dan Roth, Noah A. Smith, Wei-Chiu Ma, and Ranjay Krishna. 2024. Blink: Multimodal large language models can see but not perceive. Preprint, arXiv:2404.12390.

[11] Andreas Geiger, Philip Lenz, and Raquel Urtasun. 2012. Are we ready for autonomous driving? the kitti vision benchmark suite. In Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, pages 3354–3361.

[12] Dingming Li, Hongxing Li, Zixuan Wang, Yuchen Yan, Hang Zhang, Siqi Chen, Guiyang Hou, Shengpei Jiang, Wenqi Zhang, Yongliang Shen, Weiming Lu, and Yueting Zhuang. 2025. Viewspatial-bench: Evaluating multi-perspective spatial localization in vision-language models. Preprint, arXiv:2505.21500.

[13] Hongxing Li, Dingming Li, Zixuan Wang, Yuchen Yan, Hang Wu, Wenqi Zhang, Yongliang Shen, Weiming Lu, Jun Xiao, and Yueting Zhuang. 2025. Spatialladder: Progressive training for spatial reasoning in vision-language models. Preprint, arXiv:2510.08531.

[14] Haotong Lin, Sili Chen, Junhao Liew, Donny Y. Chen, Zhenyu Li, Guang Shi, Jiashi Feng, and Bingyi Kang. 2025. Depth anything 3: Recovering the visual space from any views. Preprint, arXiv:2511.10647.

[15] Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. 2023. Visual instruction tuning. Preprint, arXiv:2304.08485.

[16] Wufei Ma, Haoyu Chen, Guofeng Zhang, Yu-Cheng Chou, Jieneng Chen, Celso M. de Melo, and Alan Yuille. 2025. 3dsrbench: A comprehensive 3d spatial reasoning benchmark. Preprint, arXiv:2412.07825.

[17] Damiano Marsili, Rohun Agrawal, Yisong Yue, and Georgia Gkioxari. 2025. Visual agentic ai for spatial reasoning with a dynamic api. Preprint, arXiv:2502.06787.

[18] Richard A. Newcombe, Shahram Izadi, Otmar Hilliges, David Molyneaux, David Kim, Andrew J. Davison, Pushmeet Kohli, Jamie Shotton, Steve Hodges, and Andrew Fitzgibbon. 2011. Kinectfusion: Real-time dense surface mapping and tracking. In 2011 10th IEEE International Symposium on Mixed and Augmented Reality, pages 127–136. IEEE.

[19] Kun Ouyang, Yuanxin Liu, Haoning Wu, Yi Liu, Hao Zhou, Jie Zhou, Fandong Meng, and Xu Sun. 2025. Spacer: Reinforcing mllms in video spatial reasoning. Preprint, arXiv:2504.01805.

[20] Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, and Ilya Sutskever. 2021. Learning transferable visual models from natural language supervision. Preprint, arXiv:2103.00020.

[21] Dídac Surís, Sachit Menon, and Carl Vondrick. 2023. Vipergpt: Visual inference via python execution for reasoning. Preprint, arXiv:2303.08128.

[22] Vishaal Udandarao, Shyamgopal Karthik, Surabhi S Nath, Andreas Hochlehnert, Matthias Bethge, and Ameya Prabhu. 2025. Solving spatial supersensing without spatial supersensing. arXiv preprint arXiv:2511.16655.

[23] Jianyuan Wang, Minghao Chen, Nikita Karaev, Andrea Vedaldi, Christian Rupprecht, and David Novotny. 2025. Vggt: Visual geometry grounded transformer. Preprint, arXiv:2503.11651.

[24] Qineng Wang, Baiqiao Yin, Pingyue Zhang, Jianshu Zhang, Kangrui Wang, Zihan Wang, Jieyu Zhang, Keshigeyan Chandrasegaran, Han Liu, Ranjay Krishna, Saining Xie, Jiajun Wu, Li Fei-Fei, and Manling Li. 2026. Mindcube: Spatial mental modeling from limited views. Preprint, arXiv:2506.21458.

[25] Chenfei Wu, Shengming Yin, Weizhen Qi, Xiaodong Wang, Zecheng Tang, and Nan Duan. 2023. Visual chatgpt: Talking, drawing and editing with visual foundation models. Preprint, arXiv:2303.04671.

[26] Diankun Wu, Fangfu Liu, Yi-Hsin Hung, and Yueqi Duan. 2025. Spatial-mllm: Boosting mllm capabilities in visual-based spatial intelligence. Preprint, arXiv:2505.23747.

[27] Junfei Wu, Jian Guan, Kaituo Feng, Qiang Liu, Shu Wu, Liang Wang, Wei Wu, and Tieniu Tan. 2025. Reinforcing spatial reasoning in vision-language models with interwoven thinking and visual drawing. Preprint, arXiv:2506.09965.

[28] Jihan Yang, Shusheng Yang, Anjali W. Gupta, Rilyn Han, Li Fei-Fei, and Saining Xie. 2025. Thinking in space: How multimodal large language models see, remember, and recall spaces. Preprint, arXiv:2412.14171.

[29] Rui Yang, Ziyu Zhu, Yanwei Li, Jingjia Huang, Shen Yan, Siyuan Zhou, Zhe Liu, Xiangtai Li, Shuangye Li, Wenqian Wang, Yi Lin, and Hengshuang Zhao. 2025. Visual spatial tuning. Preprint, arXiv:2511.05491.

[30] Shusheng Yang, Jihan Yang, Pinzhi Huang, Ellis Brown, Zihao Yang, Yue Yu, Shengbang Tong, Zihan Zheng, Yifan Xu, Muhan Wang, Daohan Lu, Rob Fergus, Yann LeCun, Li Fei-Fei, and Saining Xie. 2025. Cambrian-s: Towards spatial supersensing in video. Preprint, arXiv:2511.04670.

[31] Sihan Yang, Runsen Xu, Yiman Xie, Sizhe Yang, Mo Li, Jingli Lin, Chenming Zhu, Xiaochen Chen, Haodong Duan, Xiangyu Yue, Dahua Lin, Tai Wang, and Jiangmiao Pang. 2025. Mmsi-bench: A benchmark for multi-image spatial intelligence. Preprint, arXiv:2505.23764.

[32] Zhengyuan Yang, Linjie Li, Jianfeng Wang, Kevin Lin, Ehsan Azarnasab, Faisal Ahmed, Zicheng Liu, Ce Liu, Michael Zeng, and Lijuan Wang. 2023. Mm-react: Prompting chatgpt for multimodal reasoning and action. Preprint, arXiv:2303.11381.

[33] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. 2023. React: Synergizing reasoning and acting in language models. Preprint, arXiv:2210.03629.

[34] Jinhui Ye, Zihan Wang, Haosen Sun, Keshigeyan Chandrasegaran, Zane Durante, Cristobal Eyzaguirre, Yonatan Bisk, Juan Carlos Niebles, Ehsan Adeli, Li Fei-Fei, Jiajun Wu, and Manling Li. 2025. T*: Re-thinking temporal search for long-form video understanding. Preprint, arXiv:2504.02259.

[35] Hang Zhang, Xin Li, and Lidong Bing. 2023. Video-llama: An instruction-tuned audio-visual language model for video understanding. Preprint, arXiv:2306.02858.

[36] Peiyuan Zhang, Kaichen Zhang, Bo Li, Guangtao Zeng, Jingkang Yang, Yuanhan Zhang, Ziyue Wang, Haoran Tan, Chunyuan Li, and Ziwei Liu. 2024. Long context transfer from language to vision. Preprint, arXiv:2406.16852.

[37] Yiming Zhang, Jiacheng Chen, Jiaqi Tan, Yongsen Mao, Wenhu Chen, and Angel X. Chang. 2026. Revsi: Rebuilding visual spatial intelligence evaluation for accurate assessment of vlm 3d reasoning. Preprint, arXiv:2604.24300.

[38] Zaibin Zhang, Yuhan Wu, Lianjie Jia, Yifan Wang, Zhongbo Zhang, Yijiang Li, Binghao Ran, Fuxi Zhang, Zhuohan Sun, Zhenfei Yin, and 1 others. 2026. Think3d: Thinking with space for spatial reasoning. arXiv preprint arXiv:2601.13029.

[39] Yaowei Zheng, Richong Zhang, Junhao Zhang, Yanhan Ye, Zheyan Luo, Zhangchi Feng, and Yongqiang Ma. 2024. Llamafactory: Unified efficient fine-tuning of 100+ language models. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 3: System Demonstrations), Bangkok, Thailand. Association for Computational Linguistics.

## Appendix A. Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Spatial Intelligence in VLMs.** Recent work has sought to improve the spatial intelligence of VLMs by scaling spatial supervision, introducing geometry-aware architectures, or designing spatially focused training objectives. Cambrian-S [30] and SenseNova-SI [5] construct large-scale spatial instruction data, while Spatial-MLLM [26] and VST [29] inject explicit spatial modeling or visual spatial tuning into multimodal backbones. Other works, such as SpaceR [19], ViLaSR [27], MindCube [24], and SpatialLadder [13], further improve spatial reasoning through reinforcement learning, verifiable rewards, or curriculum design. These efforts have advanced performance on spatial benchmarks such as BLINK [10], 3DSR [16], EmbSpatial [9], MMSI-Bench [31], and VSI-Bench [28]. However, most of them remain training-driven and single-shot: the model is expected to encode spatial capability into its parameters and produce an answer in one forward pass, relying on the model’s internalized spatial knowledge rather than explicit, scene-specific evidence acquisition at inference time.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **VLM 中的空间智能。** 近期工作试图通过扩大空间监督规模、引入几何感知架构，或设计侧重空间能力的训练目标来提升 VLM 的空间智能。Cambrian-S [30] 和 SenseNova-SI [5] 构建大规模空间指令数据；Spatial-MLLM [26] 和 VST [29] 则将显式空间建模或视觉空间调优注入多模态骨干网络。其他工作，如 SpaceR [19]、ViLaSR [27]、MindCube [24] 和 SpatialLadder [13]，进一步通过强化学习、可验证奖励或课程设计提升空间推理能力。这些工作推动了 BLINK [10]、3DSR [16]、EmbSpatial [9]、MMSI-Bench [31] 和 VSI-Bench [28] 等空间基准上的性能。然而，其中大多数仍是训练驱动且单次前向的：模型被期望将空间能力编码进其参数，并在一次前向传播中生成答案，依赖于模型内化的空间知识，而非在推理时显式获取特定场景的证据。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Agentic Spatial Reasoning.** Tool-use agents extend language and vision-language models by interleaving reasoning with calls to external tools, as shown in general agent frameworks such as ReAct [33] and visual tool-use systems such as ViperGPT [21], Visual ChatGPT [25], and MM-ReAct [32]. More recent work brings this paradigm to spatial reasoning by equipping VLMs with explicit geometric tools or structured computation. VADAR [17] synthesizes Python programs over dynamically constructed 3D APIs, SpaceTools [6] trains VLMs to coordinate vision and robotic tools through reinforcement learning, and GCA [7] constrains the reasoning process with formal reference-frame and objective constraints before deterministic geometric computation. Concurrent to these efforts, Think3D [38] equips VLM agents with 3D reconstruction and camera-manipulation tools, enabling active exploration through ego/global-view switching and novel-view rendering. These methods demonstrate the promise of agentic spatial reasoning, yet they are still limited in capturing the continuous nature of human spatial understanding, where partial observations are integrated over time, object states are maintained across viewpoints, and spatial judgments are made from an evolving scene representation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **智能体式空间推理。** 工具使用智能体通过将推理与对外部工具的调用交错进行，扩展了语言模型和视觉语言模型；通用智能体框架 ReAct [33] 以及 ViperGPT [21]、Visual ChatGPT [25] 和 MM-ReAct [32] 等视觉工具使用系统展示了这一点。更近期的工作通过为 VLM 配备显式几何工具或结构化计算，将这一范式引入空间推理。VADAR [17] 在动态构建的三维 API 上合成 Python 程序；SpaceTools [6] 通过强化学习训练 VLM 协调视觉与机器人工具；GCA [7] 则在确定性几何计算之前，使用形式化参考系和目标约束限制推理过程。与这些工作同期，Think3D [38] 为 VLM 智能体配备三维重建和相机操控工具，使其能够通过自我/全局视图切换和新视图渲染进行主动探索。这些方法展现了智能体式空间推理的前景，但它们在捕获人类空间理解的连续本质方面仍受限制；人类会随时间整合局部观测、跨视点维持对象状态，并从不断演化的场景表征中做出空间判断。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Long-video and Multi-view Understanding.** Methods commonly handle continuous observations through frame compression or reconstruction-first pipelines. Frame-compression methods sample, retrieve, or summarize a limited set of frames before feeding them to long-context VLMs [35, 36, 34], improving efficiency but risking the loss of question-relevant spatial evidence. Reconstruction-first methods instead build an explicit 3D representation using multi-view geometry or feedforward reconstruction models [23, 14], providing stronger geometric grounding but often incurring unnecessary computation when the query only requires sparse or localized evidence. However, the selected frames or reconstructed geometry are typically consumed as fixed context, leaving spatial grounding, cross-view association, and metric comparison largely to implicit reasoning or a separate downstream step. Thus, they improve access to visual or geometric information, but do not fully close the loop between evidence acquisition, spatial computation, and persistent scene-level reasoning.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **长视频与多视角理解。** 方法通常通过帧压缩或重建优先的流程处理连续观测。帧压缩方法在将有限数量的帧送入长上下文 VLM [35, 36, 34] 之前，对其进行采样、检索或摘要；这提高了效率，但可能丢失与问题相关的空间证据。重建优先的方法则使用多视角几何或前馈重建模型 [23, 14] 构建显式三维表征，提供更强的几何基础，但当查询仅需要稀疏或局部证据时，往往会带来不必要的计算。不过，选定的帧或重建的几何信息通常被作为固定上下文使用，空间定位、跨视图关联和度量比较在很大程度上仍留给隐式推理或单独的下游步骤。因此，它们改善了对视觉或几何信息的获取，却未能完全闭合证据获取、空间计算与持久场景级推理之间的循环。

## Appendix B. Details of Tools and Experts

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Level 1 tools.** Level 1 contains tools for extracting query-relevant evidence from raw 2D observations. The `detect_objects_tool` performs open-vocabulary 2D object detection using GroundingDINO. Given an image path and a text prompt, it returns bounding boxes, confidence scores, predicted labels, textual location descriptions, and a visualization with detected boxes. This tool converts entities mentioned in the question into localized 2D regions, which serve as the basis for later measurement, counting, and relative-position reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **第 1 层工具。** 第 1 层包含用于从原始二维观测中提取与查询相关证据的工具。`detect_objects_tool` 使用 GroundingDINO 执行开放词汇二维目标检测。给定图像路径和文本提示，它返回边界框、置信度得分、预测标签、文本位置描述，以及带检测框的可视化结果。该工具将问题中提到的实体转换为局部化的二维区域，为后续测量、计数和相对位置推理奠定基础。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The `vlm_ground_objects` tool performs multi-frame or multi-image grounding for target entities. It uses a two-stage procedure: first, a VLM performs a visibility vote over candidate frames to determine where the target is visible; second, `detect_objects_tool` is applied to the selected best frame to obtain the final bounding box. The tool returns the best supporting frame, bounding box, VLM confidence, detector confidence, and visualization for each target. This is useful when the target may appear across multiple views or when the referring expression is too complex for direct single-frame detection.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> `vlm_ground_objects` 工具对目标实体执行多帧或多图像定位。它采用两阶段流程：首先，VLM 对候选帧进行可见性投票，以确定目标在哪些帧中可见；其次，将 `detect_objects_tool` 应用于选出的最佳帧，以获得最终边界框。该工具针对每个目标返回最佳支持帧、边界框、VLM 置信度、检测器置信度和可视化结果。当目标可能出现于多个视图中，或指代表达过于复杂而无法直接进行单帧检测时，这一工具尤为有用。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The `depth_estimation_tool` provides lightweight image-level depth cues. Given a single image and optional query points, it returns a depth-map visualization and depth estimates at the specified locations. We use this tool to support simple depth, occlusion, and front/back reasoning at the image level. It should be distinguished from Level 2 geometric lifting, as it provides local image-level depth evidence rather than a full 3D scene representation.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> `depth_estimation_tool` 提供轻量级的图像层面深度线索。给定单张图像和可选查询点，它返回深度图可视化以及指定位置处的深度估计。我们使用该工具在图像层面支持简单的深度、遮挡和前/后推理。它应与第 2 层几何提升区分开来，因为它提供的是局部图像层面的深度证据，而非完整的三维场景表征。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> For videos, S-Agent further uses frame or keyframe selection tools, such as `TStarKeyframeSearchTool`, to identify informative frames before applying the above image-level tools. This reduces redundant visual input and allows the agent to focus subsequent grounding and perception on frames that are most relevant to the current question.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 对于视频，S-Agent 还会使用帧或关键帧选择工具（如 `TStarKeyframeSearchTool`），在应用上述图像层面工具之前识别信息丰富的帧。这减少了冗余视觉输入，并使智能体能够将后续定位和感知集中于与当前问题最相关的帧。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Level 2 tools.** Level 2 contains tools for lifting localized 2D evidence into metric 3D geometry. The main tool in our current implementation is `metric_depth3d_tool`, which is built on Depth-Anything-3. Given multiple images and query points or boxes, it estimates metric depth, 3D coordinates, camera poses, and depth visualizations. This tool provides the shared 3D geometric substrate used by downstream spatial experts, especially the Metric Measurement Expert and Relative Position Expert. In our implementation, `metric_depth3d_tool` is the core Level-2 module for stable 2D-to-3D lifting.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **第 2 层工具。** 第 2 层包含将局部二维证据提升至度量三维几何的工具。我们当前实现的主要工具是构建于 Depth-Anything-3 之上的 `metric_depth3d_tool`。给定多张图像以及查询点或边界框，它估计度量深度、三维坐标、相机位姿和深度可视化。该工具提供下游空间专家共享使用的三维几何基础，尤其服务于度量测量专家和相对位置专家。在我们的实现中，`metric_depth3d_tool` 是用于稳定二维到三维提升的核心第 2 层模块。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Level 3 experts.** Level 3 consists of five specialized spatial experts: the Metric Measurement Expert, Counting Expert, Visual Orientation Expert, Relative Position Expert, and Object-Centric View Expert. Each expert integrates the 2D evidence from Level 1 and, when needed, the lifted 3D evidence from Level 2 to produce structured, scene-specific spatial knowledge for the planner.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **第 3 层专家。** 第 3 层由五个专门的空间专家组成：度量测量专家、计数专家、视觉朝向专家、相对位置专家和以对象为中心的视图专家。每个专家整合来自第 1 层的二维证据，并在需要时整合来自第 2 层的提升后三维证据，为规划器产生结构化、场景特定的空间知识。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span>
>
> - **Metric measurement expert** serves as a geometry-grounded measurement specialist that estimates explicit spatial quantities (e.g., camera-to-object distance, object-to-object distance, and physical object size). Given target entities specified by the planner, it first reuses or obtains Level-1 evidence as normalized object boxes, and then queries the Level-2 geometric module to recover metric 3D points inside these regions. The expert deterministically maps the request to a measurement route, such as closest-point distance, center-to-center distance, or longest object dimension, samples representative points from the grounded boxes, and computes the final value from their recovered 3D coordinates. It returns a structured observation containing the **measurement type, numerical value, unit, confidence, and supporting regions**.
>
> - **Counting expert** serves as a detection-grounded aggregation specialist that answers object-counting queries, including single-object counts and condition-aware counts over multiple frames. Given target entities or counting constraints specified by the planner, it first reuses or obtains Level-1 evidence by localizing candidate objects with open-vocabulary detection. The expert then normalizes the detected boxes across frames, removes duplicated detections with non-maximum suppression, and aggregates the remaining candidates according to the question-specific counting target. For relational or attribute-conditioned counting, it further uses the available visual or geometric evidence to filter candidates before computing the final count. It returns a structured observation containing the **counted target, numerical count, aggregation mode, confidence, and supporting detections**.
>
> - **Visual orientation expert** serves as an appearance-grounded orientation specialist that answers questions about the intrinsic facing direction or pose of an object. Given the target object and the original question specified by the planner, it collects the relevant Level-1 visual evidence, such as frames where the object is visible and localized object regions when available. The expert then examines orientation cues including object front/back surfaces, handles, screens, openings, symmetry, and surrounding reference context, and maps the observed pose to the candidate directions or options in the question. Unlike geometric relation experts that compare object positions in 3D space, this expert focuses on the object’s own visual orientation. It returns a structured observation containing the **predicted orientation, confidence, and supporting visual evidence**.
>
> - **Relative position expert** serves as a 3D relation specialist that answers directional queries between entities, such as left/right, front/back, and cardinal directions. Given the target and reference entities specified by the planner, it first reuses or obtains Level-1 evidence as grounded object boxes, and then queries the Level-2 geometric module to lift these regions into a shared 3D coordinate system. The expert deterministically maps the question to a relation route, such as object-to-object direction, egocentric left/right, viewpoint-conditioned direction, or cardinal-anchor reasoning. It then compares the recovered 3D positions under the corresponding reference frame, optionally using camera poses or known direction anchors to calibrate the axes. It returns a structured observation containing the **predicted relation or option, confidence, route type, and supporting geometric evidence**.
>
> - **Object-centric view expert** serves as a view-aware specialist for questions where the input images are organized around different views of the same target object. Given the target object, labelled viewpoints, and question context specified by the planner, it reuses Level-1 visual evidence from the corresponding object-centric frames and identifies how surrounding objects appear under the specified viewpoint. The expert maps the labelled views, such as front, back, left, and right, to the spatial frame required by the question, and then determines the queried relation from this object-centered coordinate system. It returns a structured observation containing the **predicted view-conditioned relation, confidence, and supporting frames**.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span>
>
> - **度量测量专家**充当地几何支撑的测量专家，估计显式空间量（例如相机到对象距离、对象到对象距离和对象的物理尺寸）。给定由规划器指定的目标实体，它首先复用或获取作为归一化对象边界框的第 1 层证据，然后查询第 2 层几何模块以恢复这些区域内的度量三维点。该专家以确定性方式将请求映射到一条测量路径，例如最近点距离、中心到中心距离或对象最长尺寸；从已定位的边界框中采样代表性点，并根据其恢复的三维坐标计算最终数值。它返回一条结构化观测，其中包含**测量类型、数值、单位、置信度和支持区域**。
>
> - **计数专家**充当检测支撑的聚合专家，回答对象计数查询，包括单对象计数和跨多帧的条件感知计数。给定由规划器指定的目标实体或计数约束，它首先通过开放词汇检测定位候选对象，从而复用或获取第 1 层证据。随后，该专家对跨帧检测到的边界框进行归一化，使用非极大值抑制去除重复检测，并根据问题特定的计数目标聚合其余候选项。对于关系或属性条件化的计数，它还会在计算最终计数前使用可用的视觉或几何证据筛选候选项。它返回一条结构化观测，其中包含**被计数目标、数值计数、聚合模式、置信度和支持检测结果**。
>
> - **视觉朝向专家**充当由外观支撑的朝向专家，回答关于对象内在朝向或姿态的问题。给定由规划器指定的目标对象和原始问题，它收集相关的第 1 层视觉证据，例如对象可见的帧，以及在可用时的局部对象区域。该专家随后检查朝向线索，包括对象的前/后表面、把手、屏幕、开口、对称性和周围参照上下文，并将观察到的姿态映射到问题中的候选方向或选项。不同于在三维空间中比较对象位置的几何关系专家，该专家聚焦于对象自身的视觉朝向。它返回一条结构化观测，其中包含**预测朝向、置信度和支持视觉证据**。
>
> - **相对位置专家**充当三维关系专家，回答实体之间的方向查询，如左/右、前/后和基数方向。给定由规划器指定的目标实体和参照实体，它首先复用或获取作为已定位对象边界框的第 1 层证据，然后查询第 2 层几何模块，将这些区域提升到共享的三维坐标系中。该专家以确定性方式将问题映射到一条关系路径，例如对象到对象方向、自我中心左/右、视点条件化方向或基数锚点推理。随后，它在相应的参照系下比较恢复的三维位置，并可选择使用相机位姿或已知方向锚点校准坐标轴。它返回一条结构化观测，其中包含**预测关系或选项、置信度、路径类型和支持几何证据**。
>
> - **以对象为中心的视图专家**充当面向视图的专家，适用于输入图像围绕同一目标对象的不同视图组织的问题。给定由规划器指定的目标对象、标注视点和问题上下文，它复用来自相应对象中心帧的第 1 层视觉证据，并识别周围对象在指定视点下如何出现。该专家将标注视图（如前、后、左和右）映射到问题所需的空间参照系，然后从这一以对象为中心的坐标系中确定所查询的关系。它返回一条结构化观测，其中包含**预测的视图条件关系、置信度和支持帧**。

## Appendix C. Details of S-300K

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We construct S-300K from SenseNova-SI-800K [5], which is fully disjoint from all evaluation benchmarks used in this work. The construction pipeline consists of three stages: trajectory generation, trajectory filtering, and trajectory decomposition.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们从 SenseNova-SI-800K [5] 构建 S-300K；该数据集与本工作使用的所有评估基准完全不重叠。构建管线包含三个阶段：轨迹生成、轨迹过滤和轨迹分解。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Trajectory generation.** We follow Section 2.2 and sample **100K** questions from SenseNova-SI-800K and run zero-shot S-Agent with GPT-5.4 as the planner to generate tool-use reasoning trajectories. Each trajectory contains the original question, the visual inputs, intermediate planner responses, issued tool calls, returned tool observations, and the final answer produced by the agent.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **轨迹生成。** 我们遵循第 2.2 节，从 SenseNova-SI-800K 中采样 **100K** 个问题，并以 GPT-5.4 为规划器运行零样本 S-Agent，以生成工具使用推理轨迹。每条轨迹包含原始问题、视觉输入、中间规划器响应、发出的工具调用、返回的工具观测，以及智能体产生的最终答案。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Trajectory filtering.** We keep only trajectories whose final answers are valid and correct under the corresponding answer type. Specifically, we discard a trajectory if its execution status is marked as `failed`, if any unrecovered `error` occurs, or if no final answer is produced. For multiple-choice questions, we extract the prediction only from the final `<answer>...</answer>` field and require the predicted option letter to exactly match the ground-truth option letter. For example, if the ground truth is “B. Northwest”, the trajectory is retained only when the final answer predicts option B. For numeric questions, we parse floating-point values from both the prediction and the ground truth, and compute mean relative accuracy (MRA) with a default threshold of 0.6; the trajectory is retained only if MRA ≥ 0.6. For free-form text questions, we normalize both the prediction and the ground truth by lowercasing, stripping punctuation and extra whitespace, and then require either exact string match or that the ground-truth answer appears as a substring of the predicted phrase. In short, our SFT data includes only trajectories whose final answers pass answer-type-specific quality checks. We do not use whether a trajectory calls tools as a hard filtering criterion.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **轨迹过滤。** 我们仅保留其最终答案在相应答案类型下有效且正确的轨迹。具体而言，若其执行状态被标记为 `failed`，若发生任何未恢复的 `error`，或若未产生最终答案，我们将丢弃该轨迹。对于多项选择问题，我们仅从最终的 `<answer>...</answer>` 字段提取预测，并要求预测选项字母与真实选项字母完全匹配。例如，若真实答案为 “B. Northwest”，则仅当最终答案预测选项 B 时才保留该轨迹。对于数值问题，我们从预测和真实答案中解析浮点值，并以默认阈值 0.6 计算平均相对准确度（MRA）；仅当 MRA ≥ 0.6 时才保留该轨迹。对于自由形式文本问题，我们通过小写化、去除标点和额外空白来规范化预测与真实答案，然后要求二者精确字符串匹配，或者真实答案作为预测短语的子串出现。简言之，我们的 SFT 数据仅包含最终答案通过答案类型特定质量检查的轨迹。我们不将轨迹是否调用工具用作硬过滤标准。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Trajectory decomposition.** After filtering, we decompose each retained trajectory into three complementary supervision formats.
>
> 1. **Final-answer trajectories:** each original question corresponds to one full trajectory ending in the final answer; these samples train the model to imitate complete S-Agent reasoning.
> 2. **Turn-level trajectories:** each VLM planner call is converted into an independent training sample. This reduces excessively long contexts, especially for trajectories involving many images or long tool histories, and exposes the model to intermediate planning decisions.
> 3. **Expert trajectories:** individual expert or tool calls are converted into specialized sub-samples, such as calls to the metric measurement expert, counting expert, and relative-position expert. A sub-sample is included only when its input is complete, its tool response is available, and the corresponding result can be verified.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **轨迹分解。** 过滤后，我们将每条保留轨迹分解为三种互补的监督格式。
>
> 1. **最终答案轨迹：**每个原始问题对应一条以最终答案结束的完整轨迹；这些样本训练模型模仿完整的 S-Agent 推理。
> 2. **轮次级轨迹：**每次 VLM 规划器调用被转换为一个独立训练样本。这减少了过长的上下文，尤其是涉及许多图像或较长工具历史的轨迹，并使模型接触中间规划决策。
> 3. **专家轨迹：**将单个专家或工具调用转换为专门的子样本，例如对度量测量专家、计数专家和相对位置专家的调用。仅当子样本的输入完整、其工具响应可用，且相应结果可被验证时，才将该子样本纳入。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Dataset statistics.** After trajectory generation, filtering, and decomposition, the initial 100K sampled questions yield 292,391 supervised fine-tuning samples. We denote the resulting dataset as S-300K. Table 6 summarizes the data statistics. Starting from 100,000 raw agent traces, 51,596 trajectories pass the quality filtering stage. We keep one final-answer trajectory for each filtered trace, resulting in 51,596 final-answer samples. Trajectory decomposition further produces 154,590 turn-level planner samples and 86,205 nontrivial tool/expert samples. Together, these three categories form S-300K, containing 292,391 supervised fine-tuning samples.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **数据集统计。** 经历轨迹生成、过滤和分解后，初始采样的 100K 个问题产生了 292,391 个监督微调样本。我们将所得数据集称为 S-300K。表 6 汇总了数据统计信息。从 100,000 条原始智能体轨迹开始，有 51,596 条轨迹通过质量过滤阶段。我们为每条过滤后的轨迹保留一条最终答案轨迹，得到 51,596 个最终答案样本。轨迹分解还产生了 154,590 个轮次级规划器样本和 86,205 个非平凡工具/专家样本。这三类样本共同构成 S-300K，其中包含 292,391 个监督微调样本。

### Table 6. Statistics of S-300K

![Table 6](table6_s300k_statistics.png)

**Caption:** Table 6 | Statistics of S-300K. The main training set consists of final-answer, turn-level, and nontrivial tool/expert trajectories.

**Caption[CN]:** 表 6｜S-300K 的统计信息。主训练集由最终答案轨迹、轮次级轨迹和非平凡工具/专家轨迹组成。

| Data Type | Number of Samples |
|---|---:|
| Quality-filtered trajectories | 51,596 |
| Final-answer trajectories | 51,596 |
| Turn-level trajectories | 154,590 |
| Nontrivial tool/expert trajectories | 86,205 |
| Total SFT samples in S-300K | 292,391 |

### Table 7. Comparison with existing long-video methods on VSI-SUPER

![Table 7](table7_vsi_super.png)

**Caption:** Table 7 | Comparison with existing long-video methods on VSI-SUPER. We report results on VSR and VSC under different video durations.

**Caption[CN]:** 表 7｜与现有长视频方法在 VSI-SUPER 上的比较。我们报告了不同视频时长下 VSR 和 VSC 的结果。

| Eval Setups | VSR (Duration in Mins.) |  |  |  |  | VSC (Duration in Mins.) |  |  |  |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|  | 10 | 30 | 60 | 120 | 240 | 10 | 30 | 60 | 120 |
| MovieChat | 18.3 | 21.7 | 16.7 | 26.7 | 25.6 | 0.0 | 0.0 | 0.0 | 0.0 |
| Flash-VStream | 28.3 | 33.3 | 23.3 | 28.3 | 31.7 | 0.0 | 0.0 | 0.0 | 0.0 |
| Cambrian-S-7B | 38.3 | 35.0 | 6.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Cambrian-S-7B-LFP | 45.0 | 41.7 | 40.0 | 40.0 | 40.0 | 40.6 | 42.0 | 35.0 | 34.0 |
| **S-Agent (Ours)** | **75.0** | **55.0** | **63.3** | **66.1** | **77.2** | 10.6 | 4.2 | 0.0 | 0.0 |

## Appendix D. More Experiments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Results on VSR.** Table 7 shows that S-Agent substantially outperforms existing methods on the VSR subset, achieving particularly large gains in long-video settings. For example, under the 240-minute setting, S-Agent surpasses the strongest Cambrian-S-7B-LFP baseline by 37.2 percentage points, which we attribute to the introduction and strong performance of our frame-selection tool. On VSC, S-Agent does not outperform Cambrian-S-7B-LFP, but it still performs better than the non-LFP baselines on average. However, since the reliability of VSI-SUPER as an indicator of genuine spatial perception has been questioned in recent work [22], we avoid over-interpreting this result and include it mainly as a reference.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **VSR 结果。** 表 7 显示，S-Agent 在 VSR 子集上显著优于现有方法，并在长视频设置中取得了尤为显著的增益。例如，在 240 分钟设置下，S-Agent 比最强的 Cambrian-S-7B-LFP 基线高出 37.2 个百分点；我们将此归因于帧选择工具的引入及其强劲表现。在 VSC 上，S-Agent 并未优于 Cambrian-S-7B-LFP，但其平均表现仍优于非 LFP 基线。然而，鉴于近期工作 [22] 对 VSI-SUPER 作为真实空间感知指标的可靠性提出了质疑，我们避免对该结果作出过度解读，主要将其作为参考纳入。

## Appendix E. Additional Qualitative Visualizations

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Figures 6 and 7 provide additional qualitative examples beyond those in the main paper. These cases further illustrate how S-Agent adapts its tool-use trajectory to different spatial questions, including counting, multi-step reasoning, relative position, and route planning. Across these examples, the agent first selects or grounds task-relevant evidence, then applies metric or spatial experts to convert visual observations into explicit intermediate evidence before producing the final answer.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 图 6 和图 7 提供了正文之外的更多定性示例。这些案例进一步说明 S-Agent 如何使其工具使用轨迹适应不同的空间问题，包括计数、多步推理、相对位置和路径规划。在这些示例中，智能体首先选择或定位与任务相关的证据，然后应用度量或空间专家，将视觉观测转换为显式的中间证据，最后生成最终答案。

### Figure 6. Additional qualitative examples of S-Agent in the appendix

![Figure 6](fig6_appendix_qualitative.png)

**Caption:** Figure 6 | Additional qualitative examples of S-Agent in the appendix.

**Caption[CN]:** 图 6｜附录中 S-Agent 的更多定性示例。

### Figure 7. More qualitative examples showing evidence-driven spatial reasoning by S-Agent

![Figure 7](fig7_appendix_qualitative.png)

**Caption:** Figure 7 | More qualitative examples showing evidence-driven spatial reasoning by S-Agent.

**Caption[CN]:** 图 7｜展示 S-Agent 基于证据的空间推理的更多定性示例。
