# Think3D: Thinking with Space for Spatial Reasoning

**Authors:** Zaibin Zhang¹*, Yuhan Wu¹*, Lianjie Jia¹*, Yifan Wang¹, Zhongbo Zhang¹, Yijiang Li²†, Binghao Ran¹, Fuxi Zhang¹, Zhuohan Sun¹, Zhenfei Yin³, Lijun Wang¹, Huchuan Lu¹

¹ Dalian University of Technology, ² University of California San Diego, ³ University of Oxford

`dlutzzb@gmail.com, {tracy1252684562, jialianjie}@mail.dlut.edu.cn, ljwang@dlut.edu.cn`

\* Equal contribution　† Project leader

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> While contemporary Vision-Language Models (VLMs) excel at 2D visual understanding, they remain constrained by a passive, 2D-centric paradigm that severely limits genuine 3D spatial reasoning. To bridge this gap, we introduce Think3D, a novel framework that equips VLM agents with interactive, 3D chain-of-thought reasoning capabilities. By integrating a suite of 3D manipulation tools, Think3D transforms passive perception into active spatial exploration, closely mirroring human geometric reasoning. We demonstrate that Think3D acts as a highly effective zero-shot plug-in for state-of-the-art closed-source models (e.g., GPT-4.1, Gemini 2.5 Pro), yielding absolute performance gains of +7.8% on BLINK Multi-view and MindCube, and +4.7% on VSI-Bench. Furthermore, to optimize tool-use in smaller open-weight models, we propose Think3D-RL, a reinforcement learning paradigm designed to autonomously learn spatial exploration strategies. When applied to Qwen3-VL-4B, Think3D-RL amplifies the performance gain from a marginal +0.7% to a substantial +10.7%. Notably, this RL formulation induces an exploration policy that qualitatively aligns with the sophisticated behavior of much larger models, entirely circumventing the need for costly operation-trajectory annotations. Ultimately, Think3D establishes tool-augmented active exploration as an effective paradigm for unlocking human-like 3D reasoning in multimodal agents. Code, models, and data are available at https://github.com/zhangzaibin/spagent
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 尽管当代视觉语言模型（VLM）擅长二维视觉理解，但它们仍受限于一种被动的、以二维为中心的范式，这严重限制了真正的三维空间推理。为弥合这一差距，我们提出 Think3D，这是一种为 VLM 智能体赋予交互式三维思维链推理能力的新框架。通过集成一套三维操作工具，Think3D 将被动感知转化为主动空间探索，与人类的几何推理方式高度相似。我们证明，Think3D 可作为最先进闭源模型（例如 GPT-4.1、Gemini 2.5 Pro）极为有效的零样本插件，在 BLINK Multi-view 和 MindCube 上带来 +7.8% 的绝对性能增益，在 VSI-Bench 上带来 +4.7% 的绝对性能增益。此外，为优化较小开放权重模型中的工具使用，我们提出 Think3D-RL，这是一种旨在自主学习空间探索策略的强化学习范式。当应用于 Qwen3-VL-4B 时，Think3D-RL 将性能增益从微弱的 +0.7% 放大至显著的 +10.7%。值得注意的是，这一强化学习形式诱导出一种探索策略，其行为在定性上与大得多的模型所展现的复杂行为一致，同时完全无需代价高昂的操作轨迹标注。最终，Think3D 确立了工具增强的主动探索这一有效范式，用以释放多模态智能体类人的三维推理能力。代码、模型和数据见 https://github.com/zhangzaibin/spagent

**Keywords:** Vision Language Model · Spatial Intelligence · 3D

## 1 Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Understanding and interacting with the physical world has long been a fundamental objective of vision-language models (VLMs) [4, 14, 21]. Achieving this objective necessitates *spatial intelligence*—the ability to reason about geometry, viewpoint, and spatial relationships [18, 69, 76].
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 理解物理世界并与之交互，长期以来一直是视觉语言模型（VLM）的一个基本目标 [4, 14, 21]。实现这一目标需要具备*空间智能*——即对几何、视点和空间关系进行推理的能力 [18, 69, 76]。

![Fig. 1](3d%20agent/Think3D/assets/page_002_fig_fig_1.png)
**Caption:** Fig. 1. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 1。完整原文图注及可检索内容见下文对应条目。

**Caption:** Fig. 1: Comparison between prior “think with image” [46, 84] and our “think with 3D space”. While the former reasons over 2D content by manipulating images, our method operates directly within 3D point cloud space for spatial understanding.

**Caption[CN]:** 图 1： 先前的“think with image”[46, 84] 与我们的“think with 3D space”之比较。前者通过操作图像对二维内容进行推理，而我们的方法直接在三维点云空间中进行空间理解。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Despite remarkable progress in visual understanding, current VLMs remain powerful yet fundamentally *2D analyzers*. Their performance drops sharply on tasks that require spatial reasoning, such as multi-view understanding and route planning. For instance, although recent models achieve near human-level performance on comprehensive benchmarks like MMMU [77], they still lag far behind humans on tasks that demand genuine 3D reasoning [69, 75].
>
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 尽管视觉理解已取得显著进展，当前的 VLM 虽然强大，却从根本上仍是*二维分析器*。在多视角理解和路径规划等需要空间推理的任务上，它们的性能会急剧下降。例如，尽管近期模型在 MMMU [77] 等综合基准上已达到接近人类的水平，但在需要真正三维推理的任务上仍远远落后于人类 [69, 75]。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Several main research directions have emerged to bridge this gap. The first direction aims to internalize spatial knowledge by training on large-scale and spatially diverse datasets [8, 17, 22, 52, 86]. This approach requires enormous computation and can degrade general reasoning ability. The second direction, often referred to as *think with image* [45, 46, 81, 84, 88], enables models to call external tools (e.g., zoom [84], crop [81], depth estimation [88]) to enhance perception. However, these 2.5D operations primarily provide shallow spatial cues, such as relative depth, object ordering, or counting, and they do not support deeper reasoning across multiple views or 3D geometry [36, 65]. By comparison, humans naturally manipulate consistent 3D representations through operations such as dragging and rotation to support comprehensive spatial reasoning. Inspired by this cognitive process, we ask: **Can VLMs “think” with 3D space as humans do?**
>
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 为弥合这一差距，若干主要研究方向应运而生。第一个方向旨在通过大规模且空间多样的数据集进行训练，将空间知识内化 [8, 17, 22, 52, 86]。这种方法需要巨量计算，并可能损害通用推理能力。第二个方向通常称为 *think with image* [45, 46, 81, 84, 88]，它使模型能够调用外部工具（例如缩放 [84]、裁剪 [81]、深度估计 [88]）来增强感知。然而，这些 2.5D 操作主要提供浅层空间线索，例如相对深度、物体顺序或计数，并不支持跨多个视图或三维几何的更深层推理 [36, 65]。相比之下，人类会自然地通过拖动和旋转等操作来操纵一致的三维表征，从而支持全面的空间推理。受这一认知过程启发，我们提出问题：**VLM 能否像人类一样“用三维空间思考”？**

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Recent advances in 3D reconstruction [23, 56, 59] make this possible. These models can estimate camera poses and reconstruct 3D point clouds from videos or multi-view images, providing a geometric foundation for explicit spatial reasoning. Building on this foundation, we propose **Think3D**—a framework that enables VLMs to actively interact with reconstructed 3D point clouds and reason in a spatial manner through *thinking with 3D space*.
>
> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 三维重建方面的近期进展 [23, 56, 59] 使这成为可能。这些模型可以从视频或多视角图像中估计相机位姿并重建三维点云，为显式空间推理提供几何基础。在此基础上，我们提出 **Think3D**——一个使 VLM 能够主动与重建的三维点云交互，并通过*用三维空间思考*来进行空间化推理的框架。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Effective 3D reasoning requires a consistent reference frame. We use estimated camera poses as anchors so the model can interpret rotations and directions consistently, avoiding ambiguous spatial manipulations. With this design, the agent can choose a camera, select a rotation, and decide where to explore next, while switching between a global view (overall layout) and a local view (fine-grained details) to capture both coarse and fine cues. The process is inherently iterative: the model repeatedly interacts with the reconstructed 3D scene, observes new views, and refines its understanding step by step. Through this iterative reasoning process, Think3D develops a coherent spatial representation, mirroring how humans explore 3D space.
>
> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 有效的三维推理需要一致的参考系。我们使用估计的相机位姿作为锚点，使模型能够一致地理解旋转与方向，避免有歧义的空间操作。借助这一设计，智能体可以选择相机、选定旋转，并决定下一步探索何处，同时在全局视图（整体布局）与局部视图（细粒度细节）之间切换，以同时捕获粗粒度和细粒度线索。该过程本质上是迭代式的：模型反复与重建的三维场景交互，观察新视图，并逐步完善其理解。通过这一迭代推理过程，Think3D 形成连贯的空间表征，映照了人类探索三维空间的方式。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> We find that the effectiveness of spatial exploration is strongly correlated with the intrinsic reasoning capability of VLMs. Frontier models such as GPT-4.1 [2] and Gemini-2.5-Pro [14] tend to generate diverse and semantically meaningful viewpoints, whereas less capable models often drift toward redundant or even misleading camera poses, which ultimately limits spatial understanding. To narrow this gap, we propose a reinforcement learning approach, **Think3D-RL**, that enables models to autonomously discover effective exploration policies. Importantly, Think3D-RL relies only on final task rewards, without supervision over how the model should manipulate the 3D scene. During training, the model conducts multi-round spatial exploration, and the reward signal reinforces trajectories that lead to stronger downstream performance. Through this reward-driven process, the model progressively learns when and how to interact with the 3D environment, converging to substantially more informative viewpoint manipulation strategies. As a result, models exhibit increasingly consistent exploration behaviors that more closely match those of frontier VLMs, which leads to substantial improvements across diverse spatial reasoning benchmarks.
>
> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 我们发现，空间探索的有效性与 VLM 的内在推理能力高度相关。GPT-4.1 [2] 和 Gemini-2.5-Pro [14] 等前沿模型倾向于生成多样且语义上有意义的视点，而能力较弱的模型往往会偏向冗余甚至误导性的相机位姿，最终限制空间理解。为缩小这一差距，我们提出强化学习方法 **Think3D-RL**，使模型能够自主发现有效的探索策略。重要的是，Think3D-RL 仅依赖最终任务奖励，而不监督模型应如何操作三维场景。训练期间，模型进行多轮空间探索，奖励信号会强化能够带来更强下游性能的轨迹。通过这一奖励驱动的过程，模型逐步学会何时以及如何与三维环境交互，最终收敛到信息量大得多的视点操作策略。因此，模型表现出日益一致的探索行为，更接近前沿 VLM 的探索方式，并在多种空间推理基准上带来显著提升。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> We evaluate Think3D on three challenging benchmarks (BLINK Multi-view [19], MindCube [75], and VSI-Bench [69]) and observe consistent improvements across all tasks. For closed-source models such as GPT-4.1 and Gemini-2.5-Pro, we apply Think3D in a training-free manner, yielding an average +7.8% gain on BLINK Multi-view and MindCube and an additional +4.7% improvement on VSI-Bench. For open-source models, we introduce Think3D-RL; on Qwen3-VL-4B [3], the benefit of tool usage rises from +0.7% before RL to +10.7% after RL, demonstrating that learned exploration strategies strengthen the model’s ability to extract informative 3D viewpoints and improve reasoning performance.
>
> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 我们在三个具有挑战性的基准（BLINK Multi-view [19]、MindCube [75] 和 VSI-Bench [69]）上评估 Think3D，并在所有任务上观察到一致的提升。对于 GPT-4.1 和 Gemini-2.5-Pro 等闭源模型，我们以免训练方式应用 Think3D，在 BLINK Multi-view 和 MindCube 上平均提升 +7.8%，并在 VSI-Bench 上额外提升 +4.7%。对于开源模型，我们引入 Think3D-RL；在 Qwen3-VL-4B [3] 上，工具使用带来的收益从强化学习前的 +0.7% 上升至强化学习后的 +10.7%，证明学习到的探索策略增强了模型提取信息丰富的三维视点并提升推理性能的能力。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Our main contributions can be summarized as follows:
>
> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 我们的主要贡献可概括如下：

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> – **A new perspective on spatial reasoning.** We frame spatial reasoning as an active 3D exploration process, referred to as *Think with 3D Space*, rather than conventional passive 2D perception.
>
> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> – **空间推理的新视角。** 我们将空间推理表述为一种主动的三维探索过程，称为 *Think with 3D Space*，而非传统的被动二维感知。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> – **A framework for explicit 3D interaction.** We design Think3D, allowing the VLM-based agent to manipulate point clouds through camera-based reference actions and iterative spatial reasoning chains.
>
> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> – **显式三维交互框架。** 我们设计了 Think3D，使基于 VLM 的智能体能够通过以相机为参照的动作和迭代式空间推理链来操作点云。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> – **Reinforcement learning for spatial exploration.** We formulate the model’s acquisition of viewpoint and action selection as an RL process, enabling it to develop efficient 3D exploration strategies that enhance reasoning performance across spatial benchmarks.
>
> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> – **用于空间探索的强化学习。** 我们将模型对视点和动作的选择建模为强化学习过程，使其能够形成高效的三维探索策略，从而提升其在各类空间基准上的推理性能。

## 2 Related Work

### 2.1 VLMs for Spatial Reasoning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Recent advances in Vision Language Models (VLMs) have substantially improved spatial reasoning, which is a key capability for understanding and interacting with the physical world. This progress is driven by more capable models [12, 25, 29, 42, 54, 73] and comprehensive benchmarks [6, 12, 13, 35, 65, 69]. Methods such as VLM-3R [17], SpatialRAGPT [12], and SpatialVLM [8] incorporate 3D reconstruction, depth cues [39], and large-scale 3D spatial VQA data [5, 78] to improve quantitative spatial reasoning. Recent works further strengthen the coupling between perception and reasoning through holistic perception [25, 29, 36, 48, 49, 78], mental simulation [11, 25], visual chain-of-thought or RL-based reasoning [16, 42, 60, 61], and explicit visual grounding [66]. In robotics, systems such as RoboBrain [22, 51], Gemini Robotics [1, 52], and RoboRefer [85] extend these capabilities to embodied interaction and precise 3D spatial grounding, and evaluation often uses standardized spatial benchmarks such as VSI-Bench [69] and MindCube [13, 68, 75]. In navigation, a growing body of work studies how VLMs perceive, plan, and act in 3D environments [80, 87], often by coupling visual understanding with mapping, route planning, and embodied decision making. More recent works [10, 32] have also explore code-driven use of 3D model outputs to improve spatial intelligence with an emphasis on task decomposition rather than direct spatial reasoning. Another concurrent work related to ours is [71], which uses video generative models to imagine the 3D spatial space. Our Think3D differs from [71] in two aspects. First, [71] selects the exploration trajectory with beam search, whereas Think3D empowers the VLMs with the ability to actively plan when and how to explore the 3D space with 3D manipulation tools. Second, Think3D performs exploration on reconstructed 3D point clouds, thereby avoiding the hallucinations introduced by video generative models. Overall, Think3D offers a more faithful paradigm that allows models to reason about 3D space in a manner more aligned with human geometric reasoning.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 视觉语言模型（VLM）的近期进展已显著改善空间推理能力，而空间推理是理解物理世界并与之交互的一项关键能力。这一进展由能力更强的模型 [12, 25, 29, 42, 54, 73] 和综合性基准 [6, 12, 13, 35, 65, 69] 所推动。VLM-3R [17]、SpatialRAGPT [12] 和 SpatialVLM [8] 等方法结合三维重建、深度线索 [39] 和大规模三维空间 VQA 数据 [5, 78]，以改善定量空间推理。近期工作还通过整体感知 [25, 29, 36, 48, 49, 78]、心理模拟 [11, 25]、视觉思维链或基于强化学习的推理 [16, 42, 60, 61]，以及显式视觉定位 [66]，进一步加强感知与推理的耦合。在机器人领域，RoboBrain [22, 51]、Gemini Robotics [1, 52] 和 RoboRefer [85] 等系统将这些能力扩展至具身交互和精确的三维空间定位，评估通常采用 VSI-Bench [69] 和 MindCube [13, 68, 75] 等标准化空间基准。在导航领域，越来越多的工作研究 VLM 如何在三维环境中感知、规划和行动 [80, 87]，通常将视觉理解与建图、路径规划和具身决策相结合。更近期的工作 [10, 32] 还探索了以代码驱动的方式使用三维模型输出以提升空间智能，其重点是任务分解而非直接空间推理。另一项与我们相关的同期工作是 [71]，它使用视频生成模型来想象三维空间。我们的 Think3D 与 [71] 有两方面不同。首先，[71] 使用束搜索选择探索轨迹，而 Think3D 使 VLM 能够借助三维操作工具，主动规划何时以及如何探索三维空间。其次，Think3D 在重建的三维点云上进行探索，从而避免视频生成模型引入的幻觉。总体而言，Think3D 提供了一种更忠实的范式，使模型能够以更符合人类几何推理的方式对三维空间进行推理。

### 2.2 VLM tool calling

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The efficacy of VLMs is further enhanced by tool calling, where the model leverages external tools via prompting or code generation, as in HuggingGPT [44] and related systems [47, 63, 73, 81]. For long-horizon or high-complexity problems, agent-based systems have been applied to long-video understanding [7, 48, 72, 79], high-resolution image analysis [24, 70, 89], and medical diagnosis [30, 33]. OpenThinkImage [45] provides a unified platform for tool-augmented vision-language models, while others [20, 28, 31, 50, 55, 68, 89] train VLMs to use specific toolsets through fine-tuning. Reinforcement learning (RL) has become a central paradigm for tool-use and reasoning policies [9, 15, 45, 67, 83, 88]. In particular, DeepEyes [84] promotes “think with images”, enabling models to leverage internal visual reasoning without external tools and directly inspiring our design.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 工具调用进一步增强了 VLM 的效能；在这一范式中，模型通过提示或代码生成来利用外部工具，例如 HuggingGPT [44] 及相关系统 [47, 63, 73, 81]。对于长时程或高复杂度问题，基于智能体的系统已被应用于长视频理解 [7, 48, 72, 79]、高分辨率图像分析 [24, 70, 89] 和医学诊断 [30, 33]。OpenThinkImage [45] 为工具增强的视觉语言模型提供了统一平台，而其他工作 [20, 28, 31, 50, 55, 68, 89] 则通过微调来训练 VLM 使用特定工具集。强化学习（RL）已成为工具使用和推理策略的核心范式 [9, 15, 45, 67, 83, 88]。尤其是 DeepEyes [84] 提倡“think with images”，使模型能够在没有外部工具的情况下利用内部视觉推理，并直接启发了我们的设计。

### 2.3 3D Reconstruction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In the parallel field of computer vision, 3D reconstruction from 2D images has seen significant breakthroughs, largely driven by transformer-based architectures [40]. DUSt3R [58] introduces a novel paradigm for multi-view 3D reconstruction that does not require predefined camera poses. Building on this, MASt3R [26] enhances the process by regressing dense local feature maps to produce metric-scale reconstructions. VGGT [56], a feed-forward neural network, is capable of directly inferring a comprehensive set of 3D scene attributes—including camera parameters, depth maps, and point tracks—from multiple views in a single forward pass. Methods like CUT3R [57], MapAnything [23], and Pi3 [59] further support continual reconstruction, multi-task metric 3D geometry, and permutation-equivariant visual geometry, providing versatile backbones for our 3D spatial reasoning framework.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在计算机视觉这一并行领域，从二维图像进行三维重建已取得重大突破，这主要由基于 Transformer 的架构 [40] 推动。DUSt3R [58] 提出了一种无需预定义相机位姿的多视角三维重建新范式。在此基础上，MASt3R [26] 通过回归稠密局部特征图来生成度量尺度的重建，从而增强了这一过程。VGGT [56] 是一种前馈神经网络，能够在单次前向传播中直接从多个视图推断一整套三维场景属性，包括相机参数、深度图和点轨迹。CUT3R [57]、MapAnything [23] 和 Pi3 [59] 等方法进一步支持连续重建、多任务度量三维几何和置换等变视觉几何，为我们的三维空间推理框架提供了多用途骨干。

## 3 Think3D for Spatial Reasoning

![Fig. 2](3d%20agent/Think3D/assets/page_005_fig_fig_2.png)
**Caption:** Fig. 2. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 2。完整原文图注及可检索内容见下文对应条目。

**Caption:** Fig. 2: The **Think3D** pipeline. The VLM interacts with the 3D scene through iterative calls to the 3D Manipulation Toolkit, issuing viewpoint-manipulation actions that control camera pose and rendering parameters. Each rendered image is appended to the agent’s memory and informs the next reasoning step, forming a repeated cycle of observe → manipulate → reflect.

**Caption[CN]:** 图 2： **Think3D** 流程。VLM 通过迭代调用三维操作工具箱与三维场景交互，发出控制相机位姿和渲染参数的视点操作动作。每个渲染图像都会被追加到智能体的记忆中，并为下一推理步骤提供信息，从而形成“观察 → 操作 → 反思”的重复循环。

### 3.1 Framework Overview

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> As illustrated in Figure 2, **Think3D** equips a VLM with the ability to explore and reason directly in 3D via a multi-turn *observe → manipulate → reflect* loop. Given multi-view images $\{I_t\}_{t=1}^{T}$ and a query $q$, the VLM autonomously decides whether to invoke the 3D reconstruction tool to obtain a 3D point cloud and camera poses. During the subsequent 3D interaction process, the VLM is able to iteratively manipulate the point cloud and observe the 3D environment from novel views. By progressively accumulating complementary geometric observations, the VLMs form an explicit 3D chain of thought, facilitating structured spatial exploration that cannot be achieved using static 2D inputs alone. We run the loop for at most $K$ iterations (default $K$=3), with at most one reconstruction call per query and at most $K$ rendering calls. The agent can terminate early by issuing a STOP action when it deems the evidence sufficient. The above 3D interaction process is powered by the following three key components of Think3D. We present the details in the subsequent sections.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 如图 2 所示，**Think3D** 使 VLM 能够通过多轮“*观察 → 操作 → 反思*”循环，直接在三维空间中进行探索和推理。给定多视角图像 $\{I_t\}_{t=1}^{T}$ 和查询 $q$，VLM 自主决定是否调用三维重建工具，以获得三维点云和相机位姿。在随后的三维交互过程中，VLM 能够迭代地操作点云，并从新视角观察三维环境。通过逐步积累互补的几何观察，VLM 形成显式的三维思维链，从而促进仅凭静态二维输入无法实现的结构化空间探索。我们将循环最多运行 $K$ 次迭代（默认 $K$=3），每个查询最多调用一次重建，并最多调用 $K$ 次渲染。当智能体认为证据充分时，可以发出 STOP 动作提前终止。上述三维交互过程由 Think3D 的以下三个关键组件驱动。我们将在后续小节中介绍其细节。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> – **3D Manipulation Toolkit** integrates a suite of callable 3D tools, providing the agent with flexible and expressive control for exploring the 3D environment.
>
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> – **三维操作工具箱**集成了一套可调用的三维工具，为智能体探索三维环境提供灵活且富有表现力的控制能力。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> – **Spatial Reasoning Agent** performs 3D interactions by calling 3D manipulation tools and reasoning over the geometric observations.
>
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> – **空间推理智能体**通过调用三维操作工具并基于几何观察进行推理，来执行三维交互。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> – **Think3D-RL Reinforcement Learning Module** optimizes multi-step 3D exploration policy through tool calling, trained with Group Relative Policy Optimization (GRPO) [43].
>
> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> – **Think3D-RL 强化学习模块**通过工具调用优化多步三维探索策略，并使用组相对策略优化（GRPO）[43] 进行训练。

### 3.2 3D Manipulation Toolkit

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Under the Think3D framework, a suite of callable 3D tools enables flexible agentic 3D manipulation and exploration, featuring three core functionalities: 3D reconstruction, 3D transformation, and novel-view rendering.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在 Think3D 框架下，一套可调用的三维工具使灵活的智能体式三维操作与探索成为可能，其中包含三项核心功能：三维重建、三维变换和新视角渲染。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **3D Reconstruction:** Given multi-view images $\{I_t\}_{t=1}^{T}$, a 3D point cloud and the corresponding camera poses can be estimated using Pi3 [59]. Each camera is represented as
>
>C_t=(\mathbf{K}_t,\mathbf{R}_t,\mathbf{t}_t), \mathrm{Eq.}{1}$
> $
> where $\mathbf{K}_t\in\mathbb{R}^{3\times3}$ denotes the intrinsic matrix, $\mathbf{R}_t\in SO(3)$ denotes the rotation matrix, and $\mathbf{t}_t\in\mathbb{R}^3$ represents the camera center in world coordinates. Here, $t$ indexes the input views. Depth and confidence predictions are fused across views to obtain a clean colored point cloud:
> $
>\mathcal{X}=\{(\mathbf{x}_n,\mathbf{c}_n)\}_{n=1}^{N}, \mathrm{Eq.}{2}$
> $
> where $\mathbf{x}_n$ is the 3D location and $\mathbf{c}_n$ is the RGB color.
> $
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **三维重建：** 给定多视角图像 $\{I_t\}_{t=1}^{T}$，可以使用 Pi3 [59] 估计三维点云及其对应的相机位姿。每个相机表示为
>
>C_t=(\mathbf{K}_t,\mathbf{R}_t,\mathbf{t}_t), \mathrm{Eq.}{1}$
> $
> 其中，$\mathbf{K}_t\in\mathbb{R}^{3\times3}$ 表示内参矩阵，$\mathbf{R}_t\in SO(3)$ 表示旋转矩阵，$\mathbf{t}_t\in\mathbb{R}^3$ 表示世界坐标中的相机中心。这里，$t$ 是输入视图的索引。跨视图融合深度与置信度预测，以获得干净的彩色点云：
> $
>\mathcal{X}=\{(\mathbf{x}_n,\mathbf{c}_n)\}_{n=1}^{N}, \mathrm{Eq.}{2}$
> $
> 其中，$\mathbf{x}_n$ 是三维位置，$\mathbf{c}_n$ 是 RGB 颜色。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **3D Transformation** To enable flexible 3D exploration, the agent manipulates the reconstructed 3D point cloud to select informative viewpoints. At each step, it predicts: (i) a discrete camera index $i\in\{1,\ldots,T\}$, (ii) a pair of rotation angles $(\Delta\alpha,\Delta\beta)$ specifying horizontal (azimuth) and vertical (elevation) rotations, and (iii) a binary transformation mode $m\in\{\mathrm{global},\mathrm{ego}\}$ indicating whether to use a global or an ego-centric view. For $m=\mathrm{global}$, we define a global center $\mathbf{c}$ as the centroid of $\mathcal{X}$ and apply a scene-centric similarity transform, i.e., we rotate (and optionally scale) the scene around $\mathbf{c}$ while keeping the camera fixed:
> $
>\mathbf{x}'_n=s\Delta\mathbf{R}(\Delta\alpha,\Delta\beta)(\mathbf{x}_n-\mathbf{c})+\mathbf{c}, \mathrm{Eq.}{3}$
> $
> where $\Delta\mathbf{R}(\Delta\alpha,\Delta\beta)\in SO(3)$ is induced by the predicted angles and $s$ controls the zoom level of the global view (we set $s$=1 by default). This yields an updated point cloud $\mathcal{X}^{g}=\{(\mathbf{x}'_n,\mathbf{c}_n)\}_{n=1}^{N}$. We then render $\mathcal{X}^{g}$ using the selected camera $C_i$ to provide a consistent global overview. For $m=\mathrm{ego}$, we keep the point cloud fixed and apply a camera-centric rotation around the anchor camera center. Given the selected anchor camera $C_i$, we construct a virtual camera:
> $
>C_{\mathrm{new}}=(\mathbf{K}_i,\,\Delta\mathbf{R}(\Delta\alpha,\Delta\beta)\mathbf{R}_i,\,\mathbf{t}_i), \mathrm{Eq.}{4}$
> $
> where $\Delta\mathbf{R}(\Delta\alpha,\Delta\beta)\in SO(3)$ is an incremental rotation applied to the camera orientation, while the camera center remains fixed at $\mathbf{t}_i$. When $\Delta\mathbf{R}=\mathbf{I}$, the virtual camera $C_{\mathrm{new}}$ reduces to the original camera $C_i$.
> $
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **三维变换** 为实现灵活的三维探索，智能体对重建的三维点云进行操作，以选择信息丰富的视点。在每一步，它预测：(i) 一个离散相机索引 $i\in\{1,\ldots,T\}$；(ii) 一对旋转角 $(\Delta\alpha,\Delta\beta)$，分别指定水平（方位角）和垂直（俯仰角）旋转；以及 (iii) 一个二元变换模式 $m\in\{\mathrm{global},\mathrm{ego}\}$，指示使用全局视图还是自我中心视图。当 $m=\mathrm{global}$ 时，我们将全局中心 $\mathbf{c}$ 定义为 $\mathcal{X}$ 的质心，并应用以场景为中心的相似变换，即在保持相机固定的同时，围绕 $\mathbf{c}$ 旋转（并可选地缩放）场景：
>
>\mathbf{x}'_n=s\Delta\mathbf{R}(\Delta\alpha,\Delta\beta)(\mathbf{x}_n-\mathbf{c})+\mathbf{c}, \mathrm{Eq.}{3}$
> $
> 其中，$\Delta\mathbf{R}(\Delta\alpha,\Delta\beta)\in SO(3)$ 由预测角度决定，$s$ 控制全局视图的缩放级别（默认设为 $s$=1）。由此得到更新后的点云 $\mathcal{X}^{g}=\{(\mathbf{x}'_n,\mathbf{c}_n)\}_{n=1}^{N}$。随后，我们使用选定的相机 $C_i$ 渲染 $\mathcal{X}^{g}$，以提供一致的全局概览。当 $m=\mathrm{ego}$ 时，我们保持点云固定，并围绕锚点相机中心应用以相机为中心的旋转。给定选定的锚点相机 $C_i$，我们构造虚拟相机：
> $
>C_{\mathrm{new}}=(\mathbf{K}_i,\,\Delta\mathbf{R}(\Delta\alpha,\Delta\beta)\mathbf{R}_i,\,\mathbf{t}_i), \mathrm{Eq.}{4}$
> $
> 其中，$\Delta\mathbf{R}(\Delta\alpha,\Delta\beta)\in SO(3)$ 是施加于相机朝向的增量旋转，而相机中心保持固定在 $\mathbf{t}_i$。当 $\Delta\mathbf{R}=\mathbf{I}$ 时，虚拟相机 $C_{\mathrm{new}}$ 退化为原始相机 $C_i$。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Novel View Rendering** In the global mode, we render the transformed point cloud $\mathcal{X}^{g}$ with the anchor camera $C_i$ to obtain a global view of the 3D scene. In the ego-centric mode, we emulate a first-person perspective by restricting $\mathcal{X}$ to a wide field-of-view cone aligned with the forward direction of the virtual camera $C_{\mathrm{new}}$, yielding $\mathcal{X}^{e}$. A lightweight, point-based renderer then produces the synthesized view:
> $
>\hat{I}_k=\operatorname{Render}(\mathcal{X}^{(m)},C^{(m)},m), \mathrm{Eq.}{5}$
> $
> where $\mathcal{X}^{(m)}=\mathcal{X}^{g}$ and $C^{(m)}=C_i$ for the global mode, and $\mathcal{X}^{(m)}=\mathcal{X}^{e}$ and $C^{(m)}=C_{\mathrm{new}}$ for the ego mode.
> $
> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **新视角渲染** 在全局模式下，我们使用锚点相机 $C_i$ 渲染变换后的点云 $\mathcal{X}^{g}$，以获得三维场景的全局视图。在自我中心模式下，我们通过将 $\mathcal{X}$ 限制在一个与虚拟相机 $C_{\mathrm{new}}$ 前向方向对齐的宽视场锥体内来模拟第一人称视角，得到 $\mathcal{X}^{e}$。随后，轻量级的基于点的渲染器生成合成视图：
>
>\hat{I}_k=\operatorname{Render}(\mathcal{X}^{(m)},C^{(m)},m), \mathrm{Eq.}{5}$
> $
> 其中，在全局模式下，$\mathcal{X}^{(m)}=\mathcal{X}^{g}$ 且 $C^{(m)}=C_i$；在自我中心模式下，$\mathcal{X}^{(m)}=\mathcal{X}^{e}$ 且 $C^{(m)}=C_{\mathrm{new}}$。

### 3.3 VLM-based Spatial Reasoning Agent

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> As shown in Figure 2(a), the VLM-based agent iteratively interacts with the 3D scene via the manipulation toolkit and accumulates rendered observations for spatial reasoning.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 如图 2(a) 所示，基于 VLM 的智能体通过操作工具箱与三维场景进行迭代交互，并积累渲染观察以进行空间推理。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In the $k$-th iteration, given the history $\mathcal{H}_{k-1}$, the VLM acts as a multimodal policy:
>
>\mathbf{o}_k=\pi_\theta(q,\{I_t\}_{t=1}^{T},\mathcal{H}_{k-1}), \mathrm{Eq.}{6}$
> $
> where $q$ and $\{I_t\}_{t=1}^{T}$ denote the input query and the original multi-view images, respectively. The output $\mathbf{o}_k$ is parsed into a textual response and an optional tool call.
> $
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在第 $k$ 次迭代中，给定历史 $\mathcal{H}_{k-1}$，VLM 充当多模态策略：
>
>\mathbf{o}_k=\pi_\theta(q,\{I_t\}_{t=1}^{T},\mathcal{H}_{k-1}), \mathrm{Eq.}{6}$
> $
> 其中，$q$ 和 $\{I_t\}_{t=1}^{T}$ 分别表示输入查询和原始多视角图像。输出 $\mathbf{o}_k$ 被解析为文本响应和可选的工具调用。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> We optionally invoke 3D reconstruction once at the beginning with a binary decision $r\in\{0,1\}$. When $r=1$, Pi3 [59] reconstructs the point cloud $\mathcal{X}$ and estimates camera poses $\{C_t\}_{t=1}^{T}$ from the multi-view inputs. For viewpoint manipulation and rendering, the tool-call parameters at iteration $k$ are:
> $
>\mathbf{a}_k=(i_k,m_k,\Delta\alpha_k,\Delta\beta_k), \mathrm{Eq.}{7}$
> $
> where $i_k\in\{1,\ldots,T\}$ selects the anchor camera $C_{i_k}$, $m_k\in\{\mathrm{global},\mathrm{ego}\}$ specifies the view mode, and $\Delta\alpha_k,\Delta\beta_k$ denote the azimuth and elevation angles.
> $
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 我们可以在开始时选择调用一次三维重建，并以二元决策 $r\in\{0,1\}$ 表示。当 $r=1$ 时，Pi3 [59] 从多视角输入重建点云 $\mathcal{X}$ 并估计相机位姿 $\{C_t\}_{t=1}^{T}$。对于视点操作与渲染，第 $k$ 次迭代的工具调用参数为：
>
>\mathbf{a}_k=(i_k,m_k,\Delta\alpha_k,\Delta\beta_k), \mathrm{Eq.}{7}$
> $
> 其中，$i_k\in\{1,\ldots,T\}$ 选择锚点相机 $C_{i_k}$，$m_k\in\{\mathrm{global},\mathrm{ego}\}$ 指定视图模式，$\Delta\alpha_k,\Delta\beta_k$ 表示方位角和俯仰角。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Given $\mathbf{a}_k$, the toolkit applies the transformation associated with $m_k$. If $m_k=\mathrm{ego}$, it constructs a virtual camera via Eq. (4):
> $
>C_{\mathrm{new}}^{(k)}=(\mathbf{K}_{i_k},\,\Delta\mathbf{R}(\Delta\alpha_k,\Delta\beta_k)\mathbf{R}_{i_k},\,\mathbf{t}_{i_k}). \mathrm{Eq.}{8}$
> $
> If $m_k=\mathrm{global}$, it applies the global transform in Eq. (3) to obtain $\mathcal{X}^{g}$ while keeping the anchor camera $C_{i_k}$ fixed. The renderer then synthesizes the novel view $\hat{I}_k$ according to Eq. (5), which is appended to the history:
> $
>\mathcal{H}_k=\mathcal{H}_{k-1}\mathbin{\|}[(\hat{I}_k,\mathbf{a}_k)]. \mathrm{Eq.}{9}$
> $
> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 给定 $\mathbf{a}_k$，工具箱应用与 $m_k$ 相关联的变换。若 $m_k=\mathrm{ego}$，则通过式 (4) 构造虚拟相机：
> $
>C_{\mathrm{new}}^{(k)}=(\mathbf{K}_{i_k},\,\Delta\mathbf{R}(\Delta\alpha_k,\Delta\beta_k)\mathbf{R}_{i_k},\,\mathbf{t}_{i_k}). \mathrm{Eq.}{8}$
> $
> 若 $m_k=\mathrm{global}$，则应用式 (3) 中的全局变换得到 $\mathcal{X}^{g}$，同时保持锚点相机 $C_{i_k}$ 固定。随后，渲染器依据式 (5) 合成新视图 $\hat{I}_k$，并将其追加到历史中：
> $
>\mathcal{H}_k=\mathcal{H}_{k-1}\mathbin{\|}[(\hat{I}_k,\mathbf{a}_k)]. \mathrm{Eq.}{9}$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Thus, Think3D implements an iterative *observe → manipulate → reflect* loop, where the VLM maintains an explicit 3D-aware reasoning trace over the rendered views. The detailed prompts are provided in the supplementary material.
>
> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 因此，Think3D 实现了一个迭代式的“*观察 → 操作 → 反思*”循环，其中 VLM 在渲染视图之上维护一条显式的三维感知推理轨迹。详细提示词见补充材料。

## 3.4 Think3D-RL for Multi-Step Exploration

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> While the reasoning loop allows the model to explore 3D space, its effectiveness depends on learning *which viewpoints* provide informative observations and *when* such exploration should be conducted. We therefore optimize the exploration policy using reinforcement learning.
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 尽管该推理循环使模型能够探索三维空间，但其有效性取决于学习哪些视点能够提供信息丰富的观测，以及何时应当进行此类探索。因此，我们使用强化学习来优化探索策略。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Trajectory Formulation & Training-time Sampling.** We represent an agentic reasoning episode as the following trajectory:
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **轨迹形式化与训练时采样。** 我们将一个智能体推理回合表示为如下轨迹：

$
\tau=\{(\mathbf{s}_1,\mathbf{o}_1),(\mathbf{s}_2,\mathbf{o}_2)\ldots,(\mathbf{s}_K,\mathbf{o}_K),\hat{y}\}, \mathrm{Eq.}{10}
$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> where $\mathbf{s}_k=(q,\{I_t\},\mathcal{H}_{k-1})$ represents an input to the VLM agent at the $k$-th iteration; $\hat{y}$ denotes the final answer generated by the agent; and $K$ denotes the total number of exploration steps determined by the agent.
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 其中，$\mathbf{s}_k=(q,\{I_t\},\mathcal{H}_{k-1})$ 表示第 $k$ 次迭代时 VLM 智能体的输入；$\hat{y}$ 表示智能体生成的最终答案；$K$ 表示由智能体决定的探索步骤总数。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> To avoid repeatedly reconstructing 3D geometry during optimization, we precompute a point cloud for each sample beforehand. At the $k$-th exploration step, the agent selects a camera pose, and we render the corresponding view from the precomputed point cloud as the observation $\mathbf{o}_k$. This design keeps the reasoning loop fully interactive while making training and evaluation efficient.
> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 为避免在优化过程中反复重建三维几何，我们预先为每个样本计算点云。在第 $k$ 个探索步骤中，智能体选择一个相机位姿，我们从预计算的点云中渲染相应视图作为观测 $\mathbf{o}_k$。这一设计在保持推理循环完全交互式的同时，也使训练和评估更加高效。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Trajectory-level reward.** Rewards are assigned only at the end of each trajectory:
> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **轨迹级奖励。** 奖励仅在每条轨迹结束时赋予：

$
R(\tau)=R_{\mathrm{ans}}(\hat{y})+R_{\mathrm{fmt}}(\hat{y}), \mathrm{Eq.}{11}
$

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> where $R_{\mathrm{ans}}(\hat{y})$ measures answer correctness by matching $\hat{y}$ to the multiple-choice ground-truth option and $R_{\mathrm{fmt}}$ applies a small formatting bonus. This trajectory-level reward jointly reinforces all preceding viewpoint decisions, thereby promoting more efficient multi-step spatial exploration.
> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 其中，$R_{\mathrm{ans}}(\hat{y})$ 通过将 $\hat{y}$ 与多项选择题的真实选项进行匹配来衡量答案正确性，$R_{\mathrm{fmt}}$ 则施加一个较小的格式奖励。该轨迹级奖励会联合强化此前的所有视点决策，从而促进更高效的多步空间探索。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> **Optimization.** We train the policy with Group Relative Policy Optimization (GRPO) [43] for stable multi-turn reasoning. Following [84], we use a token-wise mask to stop gradients on observation tokens (rendered images encoded as text), optimizing only model-generated action and answer tokens.
> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> **优化。** 我们使用组相对策略优化（Group Relative Policy Optimization，GRPO）[43] 训练策略，以实现稳定的多轮推理。遵循 [84]，我们使用逐 token 掩码来停止观测 token（编码为文本的渲染图像）上的梯度，仅优化模型生成的动作 token 和答案 token。

## 4 Experiment

### 4.1 Experiment Setup

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> **Setting and Dataset** Our reinforcement learning (RL) training framework is based on SWIFT [82]. We fine-tune the VLM using the GRPO training strategy with 8 rollouts per step to estimate advantages. The model is trained for one epoch on 8 H200 GPUs with a batch size of 8 and gradient accumulation of 4, using a cosine learning rate schedule with 5% warmup and a base learning rate of $1\times10^{-6}$. The maximum completion length is set to 1024 tokens. During training, the language model is fully fine-tuned while the vision encoder is frozen. The training set contains 977 samples randomly selected from the MindCube dataset, with no overlap with the test set. During inference, we deploy a Pi3 tool on a RTX 3090 GPU to perform inference. We provide full implementation details of Think3D, along with the prompts used in supplementary material.
> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **设置与数据集** 我们的强化学习（RL）训练框架基于 SWIFT [82]。我们使用 GRPO 训练策略微调 VLM，每步进行 8 次 rollout 以估计优势。模型在 8 块 H200 GPU 上训练一个 epoch，批大小为 8，梯度累积为 4；采用具有 5% 预热的余弦学习率调度，基础学习率为 $1\times10^{-6}$。最大补全长度设为 1024 个 token。训练期间，对语言模型进行完全微调，而视觉编码器保持冻结。训练集包含从 MindCube 数据集中随机选取的 977 个样本，与测试集没有重叠。推理期间，我们在一块 RTX 3090 GPU 上部署 Pi3 工具执行推理。我们在补充材料中提供 Think3D 的完整实现细节以及所使用的提示词。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **Benchmarks** We evaluate our method on 3 challenging spatial reasoning benchmarks: BLINK (Multi-view) [19], MindCube [75], and the video-based VSI-Bench [69]. BLINK (Multi-view) uses all the multi-view data from the BLINK dataset and focuses on multi-view geometric understanding, particularly assessing a model’s ability to infer relative camera motion across views. MindCube contains 3 canonical camera-motion types—rotation, around, and among. We sample 40 questions from each category, resulting in 120 questions in total for evaluation. VSI-Bench assesses visual–spatial intelligence in dynamic egocentric videos across four tasks: route planning, object relative direction prediction, appearance order reasoning, and relative distance. We adopt the VSI-Bench-tiny split and sample 7 frames from each video for evaluation. All models are evaluated on the same sample sets for fair comparison.
> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **基准** 我们在 3 个具有挑战性的空间推理基准上评估所提出的方法：BLINK（Multi-view）[19]、MindCube [75]，以及基于视频的 VSI-Bench [69]。BLINK（Multi-view）使用 BLINK 数据集中的全部多视图数据，并聚焦于多视图几何理解，尤其评估模型推断跨视图相对相机运动的能力。MindCube 包含 3 种典型相机运动类型——rotation、around 和 among。我们从每个类别中抽取 40 个问题，总计使用 120 个问题进行评估。VSI-Bench 通过四项任务评估动态自我中心视频中的视觉—空间智能：路径规划、物体相对方向预测、出现顺序推理和相对距离。我们采用 VSI-Bench-tiny 划分，并从每个视频中抽取 7 帧进行评估。为公平比较，所有模型均在相同的样本集上进行评估。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> **Table 1:** Results on VSI-Bench-tiny (%). Think3D uses up to two exploration iterations for proprietary baselines and up to three for Qwen-VL-4B. Qwen3-VL-4B$_{\mathrm{T3RL}}$ is trained with Think3D-RL, and Qwen3-VL-4B$_{\mathrm{GRPO}}$ with standard GRPO.
> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> **表 1：** VSI-Bench-tiny 上的结果（%）。对于专有基线，Think3D 最多使用两次探索迭代；对于 Qwen-VL-4B，最多使用三次。Qwen3-VL-4B$_{\mathrm{T3RL}}$ 使用 Think3D-RL 训练，而 Qwen3-VL-4B$_{\mathrm{GRPO}}$ 使用标准 GRPO 训练。

| Model | Route Plan | Rel. Dir. | Rel. Dist. | App. Order | Avg |
|---|---:|---:|---:|---:|---:|
| **Proprietary models** | | | | | |
| GLM-4.5V [53] | 34.69 | 41.03 | 40.00 | 79.16 | 48.72 |
| Doubao-1.5 [41] | 42.86 | 18.00 | 40.00 | 71.40 | 43.07 |
| **Specialized Spatial Models** | | | | | |
| RoBoBrain [22] | 28.57 | 36.00 | 16.00 | 12.24 | 23.20 |
| Spatial-MLLM [64] | 38.30 | 44.00 | 40.00 | 65.31 | 46.94 |
| VLM-3R [17] | 46.94 | 64.27 | 38.00 | 55.10 | 51.08 |
| REVPT [88] | 28.57 | 40.00 | 40.00 | 51.02 | 39.90 |
| GPT-4.1 [37] | 40.80 | 40.63 | 43.30 | 68.00 | 48.18 |
| **Think3D (GPT-4.1)** | **45.26 (+5.18)** | **45.30 (+4.67)** | **46.00 (+2.70)** | **68.00 (+0.00)** | **51.14 (+2.96)** |
| Gemini-2.5-Pro [14] | 45.58 | 28.67 | 50.67 | 55.73 | 45.16 |
| **Think3D (Gemini-2.5-Pro)** | **46.93 (+1.35)** | **37.30 (+8.63)** | **54.00 (+3.33)** | **68.24 (+12.51)** | **51.61 (+6.45)** |
| Qwen3-VL-4B [38] | 34.69 | 40.67 | 35.33 | 42.44 | 38.28 |
| **Think3D (Qwen3-VL-4B)** | **30.61 (-4.08)** | **44.00 (+3.33)** | **29.33 (-6.00)** | **52.38 (+9.94)** | **39.08 (+0.80)** |
| Qwen3-VL-4B$_{\mathrm{GRPO}}$ | 28.57 | 38.00 | 36.00 | 30.61 | 33.30 |
| Qwen3-VL-4B$_{\mathrm{T3RL}}$ | 27.89 | 30.67 | 32.00 | 42.86 | 33.36 |
| **Think3D (Qwen3-VL-4B$_{\mathrm{T3RL}}$)** | **36.73 (+8.84)** | **39.00 (+8.33)** | **44.67 (+12.67)** | **61.22 (+18.36)** | **45.41 (+12.05)** |

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> **Baseline Models** For leading closed-source state-of-the-art models, we evaluate GLM-4.5V [53], Doubao-1.5 [41], GPT-4.1 [37], and Gemini-2.5-Pro [14]. In addition, we compare against specialized models fine-tuned on spatial reasoning datasets, including RoboBrain [22], Spatial-MLLM [64], and VLM-3R [17], as well as REVPT [88], a tool-augmented fine-tuning method. For Qwen3-VL-4B, we use the standard GRPO algorithm and denote the resulting model as Qwen3-VL-4B$_{\mathrm{GRPO}}$. Training uses an accuracy-based reward and a format reward, and the training setting is aligned with Think3D-RL. More model experiments are provided in the supplementary material.
> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> **基线模型** 对于领先的闭源最先进模型，我们评估 GLM-4.5V [53]、Doubao-1.5 [41]、GPT-4.1 [37] 和 Gemini-2.5-Pro [14]。此外，我们还与在空间推理数据集上微调的专用模型进行比较，包括 RoboBrain [22]、Spatial-MLLM [64] 和 VLM-3R [17]，以及工具增强的微调方法 REVPT [88]。对于 Qwen3-VL-4B，我们使用标准 GRPO 算法，并将得到的模型记为 Qwen3-VL-4B$_{\mathrm{GRPO}}$。训练采用基于准确率的奖励和格式奖励，训练设置与 Think3D-RL 保持一致。更多模型实验见补充材料。

### 4.2 Main Results

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> Results on the multi-view reasoning benchmark (Table 2) show that Think3D substantially improves proprietary models such as GPT-4.1 and Gemini-2.5-Pro, yielding 11.57% and 4.00% relative gains, respectively, in a zero-shot setting. In contrast, for smaller models such as Qwen3-VL-4B, the gain is marginal (0.61%), suggesting limited spatial reasoning capacity constrains the benefit of exploration. However, once Qwen3-VL-4B is fine-tuned with Think3D-RL (Qwen3-VL-4B$_{\mathrm{T3RL}}$), it improves by 9.32% with Think3D. This provides evidence that RL strengthens viewpoint selection and spatial exploration. We further analyze how RL-trained models achieve these gains in Section 5.4. On VSI-Bench (Table 1), results further support Think3D, yielding a 2.96% improvement on GPT-4.1 and a 6.45% improvement on Gemini-2.5-Pro. These gains indicate that Think3D also improves video-based spatial reasoning. Moreover, our RL-fine-tuned model achieves larger gains with Think3D, rising from 0.8% to 12.05%,
> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 多视图推理基准（表 2）上的结果表明，在零样本设置下，Think3D 显著提升了 GPT-4.1 和 Gemini-2.5-Pro 等专有模型，分别带来 11.57% 和 4.00% 的相对增益。相比之下，对于 Qwen3-VL-4B 等较小模型，增益很有限（0.61%），这表明有限的空间推理能力会制约探索所带来的收益。然而，一旦使用 Think3D-RL 对 Qwen3-VL-4B 进行微调（Qwen3-VL-4B$_{\mathrm{T3RL}}$），它在使用 Think3D 时便提升了 9.32%。这证明 RL 增强了视点选择和空间探索。我们在第 5.4 节进一步分析经 RL 训练的模型如何获得这些增益。在 VSI-Bench（表 1）上，结果进一步支持 Think3D：GPT-4.1 提升 2.96%，Gemini-2.5-Pro 提升 6.45%。这些增益表明 Think3D 也能改善基于视频的空间推理。此外，我们经 RL 微调的模型在 Think3D 下获得了更大的增益，从 0.8% 上升至 12.05%，

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> **Table 2:** Results on BLINK (Multi-view) and the MindCube subset (%). Think3D uses up to three exploration iterations. Qwen3-VL-4B$_{\mathrm{T3RL}}$ is trained with Think3D-RL, and Qwen3-VL-4B$_{\mathrm{GRPO}}$ with standard GRPO.
> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> **表 2：** BLINK（Multi-view）和 MindCube 子集上的结果（%）。Think3D 最多使用三次探索迭代。Qwen3-VL-4B$_{\mathrm{T3RL}}$ 使用 Think3D-RL 训练，而 Qwen3-VL-4B$_{\mathrm{GRPO}}$ 使用标准 GRPO 训练。

| Model | BLINK (MV) | MC (Rotation) | MC (Among) | MC (Around) | Avg |
|---|---:|---:|---:|---:|---:|
| **Proprietary models** | | | | | |
| GLM-4.5V [53] | 39.85 | 45.00 | 45.00 | 22.50 | 38.09 |
| Doubao-1.5 [41] | 50.93 | 72.50 | 40.00 | 35.00 | 49.61 |
| **Specialized Spatial Models** | | | | | |
| RoBoBrain [22] | 55.64 | 32.50 | 57.50 | 52.50 | 49.54 |
| Spatial-MLLM [64] | 56.06 | 32.50 | 47.50 | 35.00 | 42.77 |
| VLM-3R [17] | 41.35 | 25.00 | 47.50 | 37.50 | 37.84 |
| REVPT [88] | 51.89 | 30.00 | 55.00 | 50.50 | 47.35 |
| GPT-4.1 [37] | 36.82 | 60.00 | 46.67 | 55.00 | 49.62 |
| **Think3D (GPT-4.1)** | **63.91 (+27.09)** | **63.33 (+3.33)** | **57.50 (+5.00)** | **60.83 (+14.16)** | **61.19 (+11.57)** |
| Gemini-2.5-Pro [14] | 44.86 | 85.00 | 49.17 | 58.33 | 59.34 |
| **Think3D (Gemini-2.5-Pro)** | **52.88 (+8.02)** | **86.67 (+1.67)** | **54.17 (+5.00)** | **60.83 (+2.50)** | **63.34 (+4.00)** |
| Qwen3-VL-4B [38] | 47.87 | 34.17 | 20.00 | 41.67 | 35.92 |
| **Think3D (Qwen3-VL-4B)** | **48.62 (+0.75)** | **35.83 (+1.66)** | **28.33 (+8.33)** | **33.33 (-8.34)** | **36.53 (+0.61)** |
| Qwen3-VL-4B$_{\mathrm{GRPO}}$ | 52.38 | 35.00 | 21.67 | 28.33 | 34.34 |
| Qwen3-VL-4B$_{\mathrm{T3RL}}$ | 46.11 | 30.83 | 25.83 | 35.83 | 34.65 |
| **Think3D (Qwen3-VL-4B$_{\mathrm{T3RL}}$)** | **53.39 (+7.28)** | **42.50 (+11.67)** | **37.47 (+11.64)** | **42.50 (+6.67)** | **43.97 (+9.32)** |

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> highlighting that RL enables more effective 3D spatial exploration. We also provide a qualitative example in Figure 3.
> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> 这突显出 RL 能够实现更有效的三维空间探索。我们还在图 3 中提供了一个定性示例。

![Fig. 3](3d%20agent/Think3D/assets/page_011_fig_fig_3.png)
**Caption:** Fig. 3. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 3。完整原文图注及可检索内容见下文对应条目。

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> **Fig. 3:** Spatial exploration behavior of Think3D. The agent autonomously selects viewpoints and switches between global and ego-centric views; after RL training, it explores angles more systematically than the untuned baseline.
> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> **图 3：** Think3D 的空间探索行为。智能体自主选择视点，并在全局视图与自我中心视图之间切换；经过 RL 训练后，它对角度的探索比未经微调的基线更加系统。

## 5 Ablation Study

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> **Table 3:** Ablation on different 3D reasoning components. All results are reported as accuracy (%). 3D Rec. denotes reasoning with reconstructed 3D geometry; Cam. Anchor uses the camera pose as the manipulation anchor; Cam. Cho. enables camera selection; and Ego-view indicates whether the model may request ego-centric views. We report results on BLINK (multi-view) and MindCube.
> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> **表 3：** 不同三维推理组件的消融。所有结果均以准确率（%）报告。3D Rec. 表示使用重建的三维几何进行推理；Cam. Anchor 使用相机位姿作为操作锚点；Cam. Cho. 启用相机选择；Ego-view 表示模型是否可以请求自我中心视图。我们报告 BLINK（multi-view）和 MindCube 上的结果。

| 3D Rec. | Cam. Anchor | Cam. Cho. | Ego View | BLINK | MindCube |
|:---:|:---:|:---:|:---:|---:|---:|
|  |  |  |  | 36.82 | 55.83 |
| ✓ |  |  |  | 41.17 | 54.59 |
| ✓ | ✓ |  |  | 55.46 | 57.22 |
| ✓ | ✓ | ✓ |  | 61.65 | 58.89 |
| ✓ | ✓ | ✓ | ✓ | **63.91** | **63.33** |

### 5.1 Ablation of Components

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> As shown in Table 3, we ablate key Think3D components. Compared to the GPT-4.1 baseline (first row) that never calls the 3D tool, directly using 3D reconstruction space without an anchor camera pose to guide point cloud manipulation causes a mild performance drop. This suggests raw 3D input alone is insufficient, as the model must actively explore multiple viewpoints to reach the correct answer. Adding anchor camera selection and ego-view configuration greatly improves performance. These components help the model process 3D point clouds more efficiently.
> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> 如表 3 所示，我们对 Think3D 的关键组件进行了消融。与从不调用三维工具的 GPT-4.1 基线（第一行）相比，直接使用三维重建空间、但没有锚点相机位姿来引导点云操作，会导致性能小幅下降。这表明仅有原始三维输入并不足够，因为模型必须主动探索多个视点才能得出正确答案。加入锚点相机选择和自我中心视图配置会大幅提升性能。这些组件有助于模型更高效地处理三维点云。

### 5.2 Ablation of Space Exploration Strategy

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> As shown in Figure 4a, we analyze the spatial exploration strategies of VLMs across multiple task types—including multi-view reasoning, route planning, and object-orientation estimation—and across models with different base capabilities. Visualizing GPT-4.1’s exploration behavior reveals clear task-dependent patterns. For instance, in route planning and appearance-order tasks, GPT-4.1 predominantly uses top-down viewpoints to capture global spatial structure. In contrast, for tasks such as MindCube and object-orientation estimation, the model relies more on rotational viewpoints that support orientation inference.
> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> 如图 4a 所示，我们分析了 VLM 在多种任务类型上的空间探索策略——包括多视图推理、路径规划和物体朝向估计——并比较了基础能力不同的模型。对 GPT-4.1 探索行为的可视化揭示出清晰的任务依赖模式。例如，在路径规划和出现顺序任务中，GPT-4.1 主要使用俯视视点来捕获全局空间结构。相比之下，对于 MindCube 和物体朝向估计等任务，模型更多依赖有助于朝向推断的旋转视点。

### 5.3 Ablation of Reinforcement Learning Dynamics

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> As shown in Figure 5, we visualize RL training dynamics of one checkpoint by tracking the evolution of the accuracy reward and the number of turns per trajectory. During the first 50 training steps, the model tends to reduce turns to increase reward. However, this reduction causes a noticeable drop in accuracy: with fewer turns, the model invokes spatial tools less often and thus obtains fewer 3D viewpoints. After about 50 training steps, the model gradually increases its spatial tool usage to render point-cloud images, resulting in steady improvement in accuracy.
> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> 如图 5 所示，我们通过跟踪准确率奖励和每条轨迹轮数的变化，将一个检查点的 RL 训练动态可视化。在前 50 个训练步骤中，模型倾向于减少轮数以提高奖励。然而，这种减少会导致准确率明显下降：轮数更少时，模型调用空间工具的频率降低，因此获得的三维视点也更少。约 50 个训练步骤后，模型逐渐增加空间工具的使用以渲染点云图像，从而使准确率稳步提升。

![Fig. 4](3d%20agent/Think3D/assets/page_013_fig_fig_4.png)
**Caption:** Fig. 4. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 4。完整原文图注及可检索内容见下文对应条目。

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> **Fig. 4:** Spatial exploration patterns in viewpoint selection. Strong models concentrate on informative angles (e.g., oblique and top-down views); after RL fine-tuning, Qwen3-VL-4B$_{\mathrm{T3RL}}$ shifts toward a similar distribution. Across tasks, exploration varies substantially (e.g., route planning prefers top-down views around $(0,60)$).
> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> **图 4：** 视点选择中的空间探索模式。强模型集中于信息丰富的角度（例如斜视图和俯视图）；经过 RL 微调后，Qwen3-VL-4B$_{\mathrm{T3RL}}$ 转向了相似的分布。不同任务之间的探索差异显著（例如，路径规划偏好 $(0,60)$ 附近的俯视图）。

![Fig. 5](3d%20agent/Think3D/assets/page_013_fig_fig_5.png)
**Caption:** Fig. 5. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 5。完整原文图注及可检索内容见下文对应条目。

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> **Fig. 5:** Reinforcement Learning Dynamics. As RL fine-tuning progresses, the model learns when extra 3D tool calls are worthwhile, shifting from shorter but less accurate trajectories to more informative explorations with higher reward.
> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> **图 5：** 强化学习动态。随着 RL 微调的推进，模型学会何时值得进行额外的三维工具调用，从较短但准确性较低的轨迹转向信息更丰富、奖励更高的探索。

### 5.4 Ablation on What the Model Learns through RL

> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> To better understand what the model learns from reinforcement learning, we analyze spatial exploration behavior before and after RL fine-tuning. We visualize viewpoint distributions of strong models such as GPT-4.1 and Gemini-2.5-Pro, whose robust strategies correlate with substantial gains under Think3D. We then compare these behaviors with those of a smaller model, Qwen3-VL-4B, and its RL-enhanced variant, Qwen3-VL-4B$_{\mathrm{T3RL}}$. As shown in Figure 4b, Qwen3-VL-4B$_{\mathrm{T3RL}}$ adopts viewpoint patterns closer to the stronger models, for example selecting top-down perspectives more often to capture global spatial structure. These results indicate that RL improves informed 3D exploration.
> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> 为了更好地理解模型从强化学习中学到了什么，我们分析了 RL 微调前后的空间探索行为。我们可视化了 GPT-4.1 和 Gemini-2.5-Pro 等强模型的视点分布；这些模型的稳健策略与 Think3D 下的显著增益相关。随后，我们将这些行为与较小模型 Qwen3-VL-4B 及其 RL 增强变体 Qwen3-VL-4B$_{\mathrm{T3RL}}$ 的行为进行比较。如图 4b 所示，Qwen3-VL-4B$_{\mathrm{T3RL}}$ 采用了更接近强模型的视点模式，例如更频繁地选择俯视视角以捕获全局空间结构。这些结果表明，RL 改善了有依据的三维探索。

### 5.5 Ablation of Exploration Rounds

> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> We further analyze how the number of exploration iterations affects model performance. As shown in Figure 6, for models without RL training, increasing the number of interaction turns does not yield a clear performance gain. After RL training, Qwen3-VL-4B$_{\mathrm{T3RL}}$ begins to follow the same trend as the stronger models: its accuracy steadily increases as the number of exploration turns grows, indicating improved returns from additional visual evidence. These results suggest that RL enables the model to learn deeper and more effective spatial exploration strategies, which supports a more reliable and efficient utilization of Think3D.
> <span style="color:#F59E0B"><strong>Para. 23[CN]:</strong></span> 我们进一步分析探索迭代次数如何影响模型性能。如图 6 所示，对于未经 RL 训练的模型，增加交互轮数并不会带来明确的性能提升。经过 RL 训练后，Qwen3-VL-4B$_{\mathrm{T3RL}}$ 开始呈现与强模型相同的趋势：随着探索轮数增加，其准确率稳步上升，表明额外视觉证据带来的回报有所提高。这些结果表明，RL 使模型能够学习更深入、更有效的空间探索策略，从而支持对 Think3D 更可靠、更高效的利用。

![Fig. 6](3d%20agent/Think3D/assets/page_014_fig_fig_6.png)
**Caption:** Fig. 6. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 6。完整原文图注及可检索内容见下文对应条目。

> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> **Fig. 6:** The ablation of turns.
> <span style="color:#F59E0B"><strong>Para. 24[CN]:</strong></span> **图 6：** 轮数消融。

### 5.6 Efficiency vs. Multi-round Prompting Baseline

> <span style="color:#3B82F6"><strong>Para. 25:</strong></span> A natural question is whether Think3D’s gain simply comes from running more rounds of reasoning. We compare Think3D to a strong multi-round prompting baseline that matches the same number of rounds (3) using Self-Refine [34] without any 3D tools. As shown in Figure 7, multi-round self-critiques bring only marginal improvements, while incurring comparable or higher token/time cost. This indicates that Think3D’s advantage primarily stems from *explicit 3D interaction* rather than multi-round prompting.
> <span style="color:#F59E0B"><strong>Para. 25[CN]:</strong></span> 一个自然的问题是，Think3D 的增益是否仅仅来自运行更多轮推理。我们将 Think3D 与一个强大的多轮提示基线进行比较；该基线使用 Self-Refine [34]，在不使用任何三维工具的情况下匹配相同的轮数（3）。如图 7 所示，多轮自我批评仅带来微小提升，却产生相当或更高的 token／时间成本。这表明 Think3D 的优势主要源自*显式三维交互*，而非多轮提示。

![Fig. 7](3d%20agent/Think3D/assets/page_014_fig_fig_7.png)
**Caption:** Fig. 7. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 7。完整原文图注及可检索内容见下文对应条目。

> <span style="color:#3B82F6"><strong>Para. 26:</strong></span> **Fig. 7:** Efficiency ablation on BLINK (accuracy vs. token usage).
> <span style="color:#F59E0B"><strong>Para. 26[CN]:</strong></span> **图 7：** BLINK 上的效率消融（准确率与 token 使用量）。

### 5.7 Robustness of the 3D Reconstruction Tool

> <span style="color:#3B82F6"><strong>Para. 27:</strong></span> To test whether Think3D depends on a specific 3D reconstructor, we replace Pi3 with VGGT while keeping the rest of the pipeline unchanged, including prompting, tool-calling, and the reasoning budget. As shown in Table 4, Think3D remains effective: VGGT still delivers clear gains over the no-tool baseline on both BLINK and MindCube, and retains most of the improvement achieved with Pi3. This indicates that Think3D is largely reconstructor-agnostic and can benefit from off-the-shelf 3D tools with different accuracy profiles.
> <span style="color:#F59E0B"><strong>Para. 27[CN]:</strong></span> 为检验 Think3D 是否依赖特定的三维重建器，我们用 VGGT 替换 Pi3，同时保持流水线其余部分不变，包括提示、工具调用和推理预算。如表 4 所示，Think3D 仍然有效：在 BLINK 和 MindCube 上，VGGT 相较于无工具基线仍带来明显增益，并保留了 Pi3 所实现的大部分提升。这表明 Think3D 在很大程度上与重建器无关，并且能够受益于具有不同准确率特征的现成三维工具。

> <span style="color:#3B82F6"><strong>Para. 28:</strong></span> **Table 4:** Comparison of 3D reconstruction tools on spatial benchmarks (Acc.%).
> <span style="color:#F59E0B"><strong>Para. 28[CN]:</strong></span> **表 4：** 空间基准上三维重建工具的比较（准确率，%）。

| Tool | Conference | BLINK | MindCube |
|---|---|---:|---:|
| w/o Tool | – | 36.82 | 53.89 |
| VGGT [56] | CVPR 2025 | 59.65 | 59.59 |
| **Pi3 [59]** | **ICLR 2026** | **63.91** | **60.55** |

## 6 Conclusion

> <span style="color:#3B82F6"><strong>Para. 29:</strong></span> We introduce Think3D, a framework that lets VLM agents actively reason in 3D rather than rely on passive 2D perception. By iteratively exploring reconstructed point clouds with a 3D manipulation toolkit, Think3D achieves deeper and more consistent spatial understanding. Its RL-enhanced variant (Qwen-4B-VL$_{\mathrm{T3RL}}$) learns efficient exploration, enabling smaller VLMs to approach the behavior and performance of large proprietary models. Experiments on BLINK, MindCube, and VSI-Bench-Tiny show strong gains and cross-benchmark generalization. Overall, Think3D suggests explicit 3D interaction as a promising route to genuine spatial reasoning in VLMs.
> <span style="color:#F59E0B"><strong>Para. 29[CN]:</strong></span> 我们提出 Think3D，这是一个让 VLM 智能体在三维空间中主动推理、而非依赖被动二维感知的框架。通过使用三维操作工具包迭代探索重建点云，Think3D 实现了更深入且更一致的空间理解。其 RL 增强变体（Qwen-4B-VL$_{\mathrm{T3RL}}$）学会了高效探索，使较小的 VLM 能够接近大型专有模型的行为和性能。在 BLINK、MindCube 和 VSI-Bench-Tiny 上的实验显示出显著增益和跨基准泛化能力。总体而言，Think3D 表明，显式三维交互是 VLM 实现真正空间推理的一条有前景的路径。

# Appendix A. Prompts and Implementation Details

## Training-free Workflow Prompt
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Following [27,74], the prompt design in Think3D is structured into three parts: a system prompt (Fig. 8), a tool prompt that describes the 3D tools and their usage rules (Fig. 9), and a continual prompt that updates the context at the beginning of each reasoning round (Fig. 10). We adopt this modular design to improve prompt clarity and make multi-round tool-augmented reasoning more stable.
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 遵循文献 [27,74]，Think3D 的提示设计由三部分组成：系统提示（图 8）、描述三维工具及其使用规则的工具提示（图 9），以及在每轮推理开始时更新上下文的持续提示（图 10）。我们采用这种模块化设计，以提升提示的清晰度，并使多轮工具增强推理更加稳定。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The system prompt defines the model’s role, the overall reasoning workflow, and the required output format. This helps reduce invalid tool calls and keeps the reasoning process executable and consistent. The tool prompt specifies how the model should use 3D reconstruction tools, including which new viewpoints are worth exploring and how to avoid redundant views. In particular, we explicitly state that the input image already corresponds to the default (0°, 0°) view, and provide recommended alternative viewpoints such as left, right, top, back, and diagonal views. This design encourages the model to request complementary observations that are more informative for spatial reasoning.
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 系统提示定义模型的角色、总体推理工作流以及所需的输出格式。这有助于减少无效工具调用，并保持推理过程可执行且一致。工具提示规定模型应如何使用三维重建工具，包括哪些新视点值得探索以及如何避免冗余视图。具体而言，我们明确说明输入图像已经对应默认的 (0°, 0°) 视图，并给出左视图、右视图、顶视图、后视图和对角视图等推荐替代视点。这一设计鼓励模型请求对空间推理更具信息量的互补观察。
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The continual prompt is used to maintain reasoning progress across multiple rounds. At each round, it reminds the model of the task goal, the current context, and the need to decide whether additional tool use is still necessary. This helps the model stay focused on unresolved spatial uncertainty rather than repeatedly generating redundant analysis. Overall, this three-part prompt design improves format reliability, viewpoint efficiency, and multi-round reasoning stability in the training-free workflow.
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 持续提示用于在多轮过程中维持推理进展。每一轮中，它都会提醒模型任务目标、当前上下文，并要求判断是否仍有必要进一步使用工具。这有助于模型专注于尚未解决的空间不确定性，而不是反复生成冗余分析。总体而言，这种三部分提示设计提升了免训练工作流中的格式可靠性、视点效率和多轮推理稳定性。

## RL Training Prompt
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> During RL training, directly invoking external tools online at every rollout step is prohibitively time-consuming, which would significantly reduce training efficiency and make large-scale optimization impractical. To address this issue, we pre-generate point clouds for all training scenes in advance, thereby eliminating the need to run Pi3 inference during RL training. This design substantially reduces the per-sample processing overhead and enables more efficient policy optimization while keeping the spatial input representation consistent across training iterations.
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在强化学习训练期间，若在每个 rollout 步骤在线直接调用外部工具，会耗费难以承受的时间，从而显著降低训练效率，并使大规模优化不切实际。为解决这一问题，我们预先为所有训练场景生成点云，从而无需在强化学习训练期间运行 Pi3 推理。这一设计大幅降低了每个样本的处理开销，在保持各次训练迭代中空间输入表示一致的同时，实现了更高效的策略优化。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In addition, we observe that smaller open-source models generally exhibit weaker instruction-following and prompt-utilization capabilities than larger proprietary models. A single fixed prompt is therefore often insufficient for stable multi-round RL optimization, especially when the model needs to progressively refine its reasoning and action prediction over repeated iterations. To improve prompt efficiency, we further divide the continual training prompts according to the current iteration stage. Specifically, different prompts are used for the initial training round, intermediate continuation rounds, and the final refinement stage. This stage-aware prompt design allows the model to receive instructions that are better aligned with its current optimization status, improving both prompt utilization and training stability.
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 此外，我们观察到，与较大的专有模型相比，较小的开源模型通常表现出较弱的指令遵循能力和提示利用能力。因此，单一固定提示往往不足以支持稳定的多轮强化学习优化，尤其是在模型需要经过反复迭代逐步改进其推理和动作预测时。为提升提示效率，我们进一步依据当前迭代阶段划分持续训练提示。具体而言，初始训练轮、中间持续轮和最终精炼阶段分别使用不同提示。这种阶段感知的提示设计使模型能够接收与其当前优化状态更匹配的指令，从而同时改善提示利用率和训练稳定性。

## Figure 8 — System Prompt
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> > You are a helpful assistant that can analyze images and answer questions.
>
> **Tools**  
> You have access to the following tools to assist with user queries:  
> `<tools>{tools_json}</tools>`
>
> **How to call a tool**  
> When you need to use a tool, return a JSON object with the function name and arguments within `<tool_call></tool_call>` XML tags:  
> `<tool_call>{{"name": "<function-name>", "arguments": {{"param1": "value1", "param2": "value2"}}}}</tool_call>`
>
> You can call multiple tools if needed by using multiple `<tool_call>` blocks.
>
> **Multi-Step Workflow**  
> You can perform MULTIPLE rounds of tool calls and analysis. When using 3D reconstruction tools (Pi3), autonomously explore viewpoints:
>
> IMPORTANT: The input image(s) already show the scene at (azimuth=0°, elevation=0°) viewpoint. DO NOT call Pi3 tools with (0°, 0°) as it will just return the same view you already have!  
> The camera is visualized as a pyramid frustum, where the apex represents the camera's position and viewing direction.
>
> Recommended NEW viewing angles to explore:
> - Left views: azimuth=-45° or -90° (see scenes from right view)
> - Right views: azimuth=45° or 90° (see scenes from left view)
> - Top views: elevation=30° to 60° (see scenes from top view, better capture the object relation and relatifve position of cam and objects.)
> - Back views: azimuth=180° or ±135° (see scenes from back view)
> - Diagonal views: combine azimuth and elevation (e.g., 45°, 30°)
>
> Workflow:
> 1. Analyze the current view(s) you have
> 2. Decide which NEW angles (NOT 0°,0°!) would help answer the question
> 3. Call tools with specific angles that are DIFFERENT from (0°,0°)
> 4. If you have multiple input images: Try different rotation_reference_camera values (1, 2, 3, etc.) to see the scene from different camera positions base on your analysis on the question.
> 5. Consider using camera_view=true to get first-person perspective from specific camera positions, especially useful for understanding spatial relationships and what each camera can actually see
> 6. After each round, analyze whether additional angles, camera positions, or perspective modes would reduce uncertainty
> 8. Continue until additional views no longer change your conclusion
> 9. Only put number (like 1,2,3) or Options in `<answer></answer>` tags, do not put any other text.
>
> Note that in 3D reconstruction, the camera numbering corresponds directly to the image numbering — cam1 represents the first frame.  
> You can examine the image to understand what is around cam1.  
> The 3D reconstruction provides relative positional information, so you should reason interactively and complementarily between the 2D image and the 3D reconstruction to form a complete understanding.  
> You need to analyze deeply the camera, its orientation, and the content captured in the frame.
>
> TIPS: For questions related to orientation or relative positioning, it is recommended to choose top view.
>
> Please analyze the following image(s):
>
> Images to analyze:  
> `{images_info}`
>
> Question:  
> `{question}`
>
> Think step by step to analyze the question and provide a detailed answer.
>
> Important Notes:
> - You can call tools MULTIPLE times with different parameters to gather comprehensive information
> - After each tool execution, you'll see the results and can decide if you need more information
> - Only provide your final `<answer></answer>` when you have gathered sufficient information
>
> You MUST output your thinking process in `<think></think>` and tool choices in `<tool_call></tool_call>`. When you have enough information, output your final choice in `<answer></answer>`. Only put Options in `<answer></answer>` tags, do not put any other text.
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> > 你是一名能够分析图像并回答问题的有用助手。
>
> **工具**  
> 你可以使用以下工具来协助处理用户查询：  
> `<tools>{tools_json}</tools>`
>
> **如何调用工具**  
> 当你需要使用工具时，请在 `<tool_call></tool_call>` XML 标签内返回一个包含函数名称和参数的 JSON 对象：  
> `<tool_call>{{"name": "<function-name>", "arguments": {{"param1": "value1", "param2": "value2"}}}}</tool_call>`
>
> 如有需要，你可以使用多个 `<tool_call>` 块调用多个工具。
>
> **多步工作流**  
> 你可以执行多轮工具调用和分析。使用三维重建工具（Pi3）时，请自主探索视点：
>
> 重要：输入图像已经展示了 (azimuth=0°, elevation=0°) 视点下的场景。不要用 (0°, 0°) 调用 Pi3 工具，因为它只会返回你已经拥有的同一视图！  
> 相机被可视化为一个棱锥形视锥，其顶点表示相机的位置和观察方向。
>
> 推荐探索的新观察角度：
> - 左侧视图：azimuth=-45° 或 -90°（从右侧视角观察场景）
> - 右侧视图：azimuth=45° 或 90°（从左侧视角观察场景）
> - 顶部视图：elevation=30° 到 60°（从顶部视角观察场景，更好地捕捉物体关系以及相机与物体的相对位置。）
> - 后侧视图：azimuth=180° 或 ±135°（从后侧视角观察场景）
> - 对角视图：组合 azimuth 和 elevation（例如 45°, 30°）
>
> 工作流：
> 1. 分析你当前拥有的视图
> 2. 判断哪些新角度（不是 0°,0°！）有助于回答问题
> 3. 使用与 (0°,0°) 不同的具体角度调用工具
> 4. 如果有多张输入图像：尝试不同的 rotation_reference_camera 值（1、2、3 等），根据你对问题的分析，从不同相机位置观察场景。
> 5. 考虑使用 camera_view=true，从特定相机位置获得第一人称视角；这尤其有助于理解空间关系以及每台相机实际能看到什么
> 6. 每轮结束后，分析额外角度、相机位置或透视模式是否会减少不确定性
> 8. 持续进行，直到额外视图不再改变你的结论
> 9. `<answer></answer>` 标签中只能放数字（如 1,2,3）或选项，不要放任何其他文本。
>
> 请注意，在三维重建中，相机编号与图像编号直接对应——cam1 表示第一帧。  
> 你可以检查图像，以了解 cam1 周围有什么。  
> 三维重建提供相对位置信息，因此你应在二维图像与三维重建之间进行交互式、互补式推理，以形成完整理解。  
> 你需要深入分析相机、其朝向以及画面中捕获的内容。
>
> 提示：对于与朝向或相对定位有关的问题，建议选择顶部视图。
>
> 请分析以下图像：
>
> 待分析图像：  
> `{images_info}`
>
> 问题：  
> `{question}`
>
> 请逐步思考、分析问题，并给出详细答案。
>
> 重要说明：
> - 你可以使用不同参数多次调用工具，以收集全面信息
> - 每次工具执行后，你都会看到结果，并可判断是否需要更多信息
> - 只有在收集到足够信息后，才提供最终的 `<answer></answer>`
>
> 你必须在 `<think></think>` 中输出思考过程，并在 `<tool_call></tool_call>` 中输出工具选择。当你拥有足够信息时，在 `<answer></answer>` 中输出最终选择。`<answer></answer>` 标签中只能放选项，不要放任何其他文本。

![Fig. 8](3d%20agent/Think3D/assets/page_017_fig_fig_8.png)
**Caption:** Fig. 8. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 8。完整原文图注及可检索内容见下文对应条目。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Fig. 8: The system prompt.** Instruction prompt detailing tool invocation rules and the multi-step workflow for iterative 3D viewpoint exploration, including tool-call format, recommended angles, and guidelines for reasoning with reconstructed camera poses.
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 8：系统提示。** 该指令提示详细说明工具调用规则以及用于迭代式三维视点探索的多步工作流，包括工具调用格式、推荐角度和使用重建相机位姿进行推理的准则。
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The corresponding prompts used in different stages are shown in Fig. 11, Fig. 12, and Fig. 13.
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 不同阶段所使用的相应提示见图 11、图 12 和图 13。

## Figure 9 — Pi3 Tool Prompt
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> > This tool is suitable for motion and spatial reasoning tasks that involve camera movement, object rotation, or directional motion analysis. It performs 3D reconstruction from images to generate point clouds and visualizations from CUSTOM viewing angles.
>
> **Important Note:** The 0° azimuth angle and 0° elevation angle corresponds to the first input image viewpoint (cam1). Do not use this angle.
>
> **Angle Parameters:**
> - **azimuth_angle** (-180° to 180°, integer only): Controls left-right rotation.
> - **elevation_angle** (-90° to 90°, integer only): Controls up-down rotation. By convention, (azimuth=0, elevation=0) corresponds EXACTLY to the first input image viewpoint (cam1). All rotations are defined in the INPUT CAMERA coordinate frame: azimuth rotates left/right around the camera's vertical axis; elevation rotates up/down around the camera's right axis.
> - **rotation_reference_camera** (must be output, 1-based):This parameter is used to rotate around a specific input image's camera. By picking an image you pick its camera (e.g., set rotation_reference_camera=3 for the third image's viewpoint; defaults to 1).
>
> **camera_view** (must be output, boolean): This parameter is used to generate first-person perspective from the selected camera position (as if standing at that camera looking at the scene), instead of the default global bird's-eye view. This is especially useful for understanding what each camera can see and analyzing spatial relationships from specific viewpoints. Combine with rotation_reference_camera to experience the scene from different camera positions.
>
> Note that default camera_view is false. You must output camera_view = true if you want to set ego-view. If you want to set global-view, you must output camera_view = false.
>
> **Usage Strategy:** You can call this tool MULTIPLE times with DIFFERENT angles and different camera views to analyze the 3D structure comprehensively. The MLLM is encouraged to autonomously explore angles (coarse-to-fine) until sufficient evidence is gathered. The generated visualization uses cone-shaped markers to indicate camera positions, numbered from 1 (cam1, cam2, etc.).
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> > 该工具适用于涉及相机移动、物体旋转或方向运动分析的运动与空间推理任务。它根据图像执行三维重建，以从自定义观察角度生成点云和可视化结果。
>
> **重要说明：** 0° 方位角和 0° 仰角对应第一张输入图像的视点 (cam1)。不要使用该角度。
>
> **角度参数：**
> - **azimuth_angle**（-180° 到 180°，仅限整数）：控制左右旋转。
> - **elevation_angle**（-90° 到 90°，仅限整数）：控制上下旋转。按照约定，(azimuth=0, elevation=0) 与第一张输入图像的视点 (cam1) 完全对应。所有旋转均在输入相机坐标系中定义：azimuth 围绕相机的垂直轴向左/向右旋转；elevation 围绕相机的右轴向上/向下旋转。
> - **rotation_reference_camera**（必须输出，从 1 开始）：此参数用于围绕特定输入图像的相机旋转。选择一张图像即选择其相机（例如，为第三张图像的视点设置 rotation_reference_camera=3；默认值为 1）。
>
> **camera_view**（必须输出，布尔值）：此参数用于从所选相机位置生成第一人称视角（如同站在该相机处观察场景），而不是默认的全局鸟瞰视图。这尤其有助于理解每台相机能看到什么，并从特定视点分析空间关系。可与 rotation_reference_camera 结合，以从不同相机位置体验场景。
>
> 请注意，camera_view 默认为 false。若要设置自我视图，必须输出 camera_view = true。若要设置全局视图，必须输出 camera_view = false。
>
> **使用策略：** 你可以用不同角度和不同相机视图多次调用该工具，以全面分析三维结构。鼓励 MLLM 自主探索角度（由粗到细），直到收集到充分证据。生成的可视化使用锥形标记表示相机位置，并从 1 开始编号（cam1、cam2 等）。

![Fig. 9](3d%20agent/Think3D/assets/page_018_fig_fig_9.png)
**Caption:** Fig. 9. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 9。完整原文图注及可检索内容见下文对应条目。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Fig. 9: The Pi3 Tool Prompt.** The prompt specifies the tool’s capabilities, key control parameters, and multi-angle query usage strategies to support comprehensive spatial understanding.
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 9：Pi3 工具提示。** 该提示规定工具的能力、关键控制参数和多角度查询使用策略，以支持全面的空间理解。

## Prompt for evaluation without tools
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> When no tool is available, we adopt standard chain-of-thought (CoT) [62] reasoning. The corresponding prompt is shown in Fig 14.
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 当没有工具可用时，我们采用标准的思维链（CoT）[62] 推理。相应提示见图 14。

## Prompt for self-refine experiment
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The corresponding prompt is shown in Fig 15.
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 相应提示见图 15。

## Algorithm 1 — Self-Refine Inference
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Algorithm 1 Self-Refine Inference**

> **Require:** Question $q$, iterations $T$

> 1. $a_0 \leftarrow \mathrm{LLM}(q)$
> 2. **for** $t = 0$ to $T - 1$ **do**
> 3. &nbsp;&nbsp;&nbsp;&nbsp;$c_t \leftarrow \mathrm{LLM}_{\mathrm{critique}}(q,a_t)$
> 4. &nbsp;&nbsp;&nbsp;&nbsp;$a_{t+1} \leftarrow \mathrm{LLM}_{\mathrm{refine}}(q,a_t,c_t)$
> 5. **end for**
> 6. **return** $a_T$
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **算法 1 自我精炼推理**

**要求：** 问题 $q$，迭代次数 $T$

1. $a_0 \leftarrow \mathrm{LLM}(q)$
2. **对于** $t = 0$ 到 $T - 1$ **执行**
3. &nbsp;&nbsp;&nbsp;&nbsp;$c_t \leftarrow \mathrm{LLM}_{\mathrm{critique}}(q,a_t)$
4. &nbsp;&nbsp;&nbsp;&nbsp;$a_{t+1} \leftarrow \mathrm{LLM}_{\mathrm{refine}}(q,a_t,c_t)$
5. **结束循环**
6. **返回** $a_T$

![Algorithm 1](3d%20agent/Think3D/assets/page_018_fig_algorithm_1.png)
**Caption:** Algorithm 1. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Algorithm 1。完整原文图注及可检索内容见下文对应条目。

## Figure 10 — Multi-step Prompt for Iterative 3D Viewpoint Exploration
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> > `=== Multi-Step Analysis: Iteration {current_iteration}/{max_iterations} ===`
>
> Original Question: `{question}`
>
> Your Previous Response:  
> `{last_response}`
>
> Tool Execution Summary:  
> `{tool_summary_text}`  
> `{angle_info_text}`
>
> Original Images:  
> `{original_images_info}`
>
> Generated Images Available for Analysis:  
> `{additional_images_info}`
>
> `=== Next Steps ===`
>
> You have `{remaining}` more iteration(s) available. You can:
>
> 1. Continue investigating - Call tools with DIFFERENT parameters:
>    - IMPORTANT: Your original input images are already at (azimuth=0°, elevation=0°). DO NOT call Pi3 tools with (0°, 0°) again!
>    - For Pi3 tools: Try NEW viewing angles to understand the 3D structure better
>    - Recommended NEW angles (NOT 0°,0°!):
>      - Left: (-45°, 0°) or (-90°, 0°)
>      - Right: (45°, 0°) or (90°, 0°)
>      - Top: (0°, 45°) or (0°, 60°)
>      - Bottom: (0°, -45°)
>      - Back: (180°, 0°) or (±135°, 0°)
>      - Diagonal: (45°, 30°) or (-45°, 30°)
>    - Each NEW angle reveals different aspects of the 3D structure
>
>    Advanced Pi3 Parameters:
>    - rotation_reference_camera (integer, 1-based): When you have multiple input images, try DIFFERENT camera positions as rotation centers
>      - Default is 1 (first camera), Set to 2, 3, etc. to rotate around different camera positions
>      - Example: rotation_reference_camera=2 rotates around the second camera's viewpoint
>      - Useful for analyzing different parts of the scene from various perspectives
>    - camera_view (boolean): Control the visualization perspective
>      - False (default): Global bird's-eye view showing the entire scene
>      - True: First-person camera view - see the scene from the selected camera's perspective (as if standing at that camera)
>      - Combine with rotation_reference_camera to experience different camera viewpoints
>      - Example: camera_view=True with rotation_reference_camera=2 shows first-person view from camera 2
>      - Useful for understanding what each camera can see and spatial relationships
>
> 2. Provide final answer - If you have sufficient information from current viewpoints:
>    - Output your comprehensive analysis in `<think></think>` tags
>    - Reference the specific viewpoints that helped you understand the structure
>
> Instructions:
> - Think: Do you need to see the object from another NEW angle (NOT 0°,0°!) to answer the question better?
> - If YES: Use `<tool_call></tool_call>` to request a DIFFERENT viewing angle (avoid 0°,0° as you already have it!)
> - If NO: output your thinking process in `<think></think>` and your final answer in `<answer></answer>`. Only put Options in `<answer></answer>` tags, do not put any other text.
>
> Note that in 3D reconstruction, the camera numbering corresponds directly to the image numbering — cam1 represents the first frame.  
> You can examine the image to understand what is around cam1.  
> The 3D reconstruction provides relative positional information, so you should reason interactively and complementarily between the 2D image and the 3D reconstruction to form a complete understanding.
>
> Please continue:
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> > `=== 多步分析：第 {current_iteration}/{max_iterations} 次迭代 ===`
>
> 原始问题：`{question}`
>
> 你先前的响应：  
> `{last_response}`
>
> 工具执行摘要：  
> `{tool_summary_text}`  
> `{angle_info_text}`
>
> 原始图像：  
> `{original_images_info}`
>
> 可用于分析的生成图像：  
> `{additional_images_info}`
>
> `=== 后续步骤 ===`
>
> 你还有 `{remaining}` 次可用迭代。你可以：
>
> 1. 继续调查——使用不同参数调用工具：
>    - 重要：你的原始输入图像已经处于 (azimuth=0°, elevation=0°)。不要再次用 (0°, 0°) 调用 Pi3 工具！
>    - 对于 Pi3 工具：尝试新的观察角度，以更好地理解三维结构
>    - 推荐的新角度（不是 0°,0°！）：
>      - 左侧：(-45°, 0°) 或 (-90°, 0°)
>      - 右侧：(45°, 0°) 或 (90°, 0°)
>      - 顶部：(0°, 45°) 或 (0°, 60°)
>      - 底部：(0°, -45°)
>      - 后侧：(180°, 0°) 或 (±135°, 0°)
>      - 对角：(45°, 30°) 或 (-45°, 30°)
>    - 每个新角度都会揭示三维结构的不同方面
>
>    高级 Pi3 参数：
>    - rotation_reference_camera（整数，从 1 开始）：当有多张输入图像时，尝试用不同相机位置作为旋转中心
>      - 默认值为 1（第一台相机）；设为 2、3 等可围绕不同相机位置旋转
>      - 示例：rotation_reference_camera=2 围绕第二台相机的视点旋转
>      - 有助于从不同视角分析场景的不同部分
>    - camera_view（布尔值）：控制可视化视角
>      - False（默认）：展示整个场景的全局鸟瞰视图
>      - True：第一人称相机视图——从所选相机的视角观察场景（如同站在该相机处）
>      - 与 rotation_reference_camera 结合，以体验不同相机视点
>      - 示例：camera_view=True 且 rotation_reference_camera=2 会展示来自相机 2 的第一人称视图
>      - 有助于理解每台相机能看到什么以及空间关系
>
> 2. 提供最终答案——如果你从当前视点获得了充分信息：
>    - 在 `<think></think>` 标签中输出全面分析
>    - 引用帮助你理解结构的具体视点
>
> 指令：
> - 思考：为了更好地回答问题，你是否需要从另一个新角度（不是 0°,0°！）观察物体？
> - 如果是：使用 `<tool_call></tool_call>` 请求一个不同的观察角度（避免 0°,0°，因为你已经拥有该视图！）
> - 如果否：在 `<think></think>` 中输出思考过程，并在 `<answer></answer>` 中输出最终答案。`<answer></answer>` 标签中只能放选项，不要放任何其他文本。
>
> 请注意，在三维重建中，相机编号与图像编号直接对应——cam1 表示第一帧。  
> 你可以检查图像，以了解 cam1 周围有什么。  
> 三维重建提供相对位置信息，因此你应在二维图像与三维重建之间进行交互式、互补式推理，以形成完整理解。
>
> 请继续：

![Fig. 10](3d%20agent/Think3D/assets/page_019_fig_fig_10.png)
**Caption:** Fig. 10. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 10。完整原文图注及可检索内容见下文对应条目。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Fig. 10: Multi-step prompt for iterative 3D viewpoint exploration.** Including angle selection, camera rotation controls, tool invocation rules to refine spatial reasoning.
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 10：用于迭代式三维视点探索的多步提示。** 包括用于改进空间推理的角度选择、相机旋转控制和工具调用规则。

## Figure 11 — RL System Prompt
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> > You are a helpful assistant that can analyze images and answer questions.
>
> **Tools**  
> You have access to the following tools to assist with user queries:  
> `<tools>{tools_json}</tools>`
>
> **How to call a tool**  
> When you need to use a tool, return a JSON object with the function name and arguments within `<tool_call>` `</tool_call>` XML tags:  
> `<tool_call>{{"name": "<function-name>", "arguments": {{"param1": "value1", "param2": "value2"}}}}</tool_call>`
>
> You can call multiple tools if needed by using multiple `<tool_call>` blocks.
>
> **Multi-Step Workflow**  
> You can perform MULTIPLE rounds of tool calls and analysis. When using 3D reconstruction tools (Pi3), autonomously explore viewpoints:
>
> IMPORTANT: The input image(s) already show the scene at (azimuth=0°, elevation=0°) viewpoint. DO NOT call Pi3 tools with (0°, 0°) as it will just return the same view you already have!  
> The camera is visualized as a pyramid frustum, where the apex represents the camera's position and viewing direction.  
> You only have 8 viewing angles to choose:
> - Left views (see scenes from right view): (azimuth_angle, elevation_angle) = (-45°, 0°)/(-90°, 0°)
> - Right views (see scenes from left view): (azimuth_angle, elevation_angle) = (45°, 0°)/(90°, 0°)
> - Top views (see scenes from top view, better capture the object relation and relatifve position of cam and objects.): (azimuth_angle, elevation_angle) = (0°, 60°)
> - Opposite views: (azimuth_angle, elevation_angle) = (45°, 60°)/(45°, 30°)/(-45°, 30°)
>
> Workflow:
> 1. Analyze the current view(s) you have
> 2. Decide which NEW angles (NOT 0°,0°!) would help answer the question
> 3. Call tools with specific angles that are DIFFERENT from (0°,0°)
> 4. After each round, analyze whether additional angles or perspective modes would reduce uncertainty
> 5. Continue until additional views no longer change your conclusion
> 6. Only put letters of options (like A,B,C) in `<answer></answer>` tags, do not put any other text.
>
> TIPS: For questions related to orientation or relative positioning, it is recommended to choose top view.
>
> Please analyze the following image(s):
>
> Images to analyze:  
> `{images_info}`
>
> Question:  
> `{question}`
>
> Think step by step to analyze the question and provide a detailed answer
>
> Important Notes:
> - You can call tools MULTIPLE times with different parameters to gather comprehensive information
> - After each tool execution, you'll see the results and can decide if you need more information
> - Only provide your final `<answer></answer>` when you have gathered sufficient information
>
> You MUST output your thinking process in `<think></think>` and tool choices in `<tool_call></tool_call>`. When you have enough information, output your final choice in `<answer></answer>`. Only put Options in `<answer>` `</answer>` tags, do not put any other text.
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> > 你是一名能够分析图像并回答问题的有用助手。
>
> **工具**  
> 你可以使用以下工具来协助处理用户查询：  
> `<tools>{tools_json}</tools>`
>
> **如何调用工具**  
> 当你需要使用工具时，请在 `<tool_call>` `</tool_call>` XML 标签内返回一个包含函数名称和参数的 JSON 对象：  
> `<tool_call>{{"name": "<function-name>", "arguments": {{"param1": "value1", "param2": "value2"}}}}</tool_call>`
>
> 如有需要，你可以使用多个 `<tool_call>` 块调用多个工具。
>
> **多步工作流**  
> 你可以执行多轮工具调用和分析。使用三维重建工具（Pi3）时，请自主探索视点：
>
> 重要：输入图像已经展示了 (azimuth=0°, elevation=0°) 视点下的场景。不要用 (0°, 0°) 调用 Pi3 工具，因为它只会返回你已经拥有的同一视图！  
> 相机被可视化为一个棱锥形视锥，其顶点表示相机的位置和观察方向。  
> 你只有 8 个观察角度可供选择：
> - 左侧视图（从右侧视角观察场景）：(azimuth_angle, elevation_angle) = (-45°, 0°)/(-90°, 0°)
> - 右侧视图（从左侧视角观察场景）：(azimuth_angle, elevation_angle) = (45°, 0°)/(90°, 0°)
> - 顶部视图（从顶部视角观察场景，更好地捕捉物体关系以及相机与物体的相对位置）：(azimuth_angle, elevation_angle) = (0°, 60°)
> - 相对视图：(azimuth_angle, elevation_angle) = (45°, 60°)/(45°, 30°)/(-45°, 30°)
>
> 工作流：
> 1. 分析你当前拥有的视图
> 2. 判断哪些新角度（不是 0°,0°！）有助于回答问题
> 3. 使用与 (0°,0°) 不同的具体角度调用工具
> 4. 每轮结束后，分析额外角度或透视模式是否会减少不确定性
> 5. 持续进行，直到额外视图不再改变你的结论
> 6. `<answer></answer>` 标签中只能放选项字母（如 A,B,C），不要放任何其他文本。
>
> 提示：对于与朝向或相对定位有关的问题，建议选择顶部视图。
>
> 请分析以下图像：
>
> 待分析图像：  
> `{images_info}`
>
> 问题：  
> `{question}`
>
> 请逐步思考、分析问题，并给出详细答案
>
> 重要说明：
> - 你可以使用不同参数多次调用工具，以收集全面信息
> - 每次工具执行后，你都会看到结果，并可判断是否需要更多信息
> - 只有在收集到足够信息后，才提供最终的 `<answer></answer>`
>
> 你必须在 `<think></think>` 中输出思考过程，并在 `<tool_call></tool_call>` 中输出工具选择。当你拥有足够信息时，在 `<answer></answer>` 中输出最终选择。`<answer>` `</answer>` 标签中只能放选项，不要放任何其他文本。

![Fig. 11](3d%20agent/Think3D/assets/page_020_fig_fig_11.png)
**Caption:** Fig. 11. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 11。完整原文图注及可检索内容见下文对应条目。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Fig. 11: The RL system prompt.** Instruction prompt defining the constrained 3-view 3D analysis workflow, including tool-call format, angle selection rules (left, right, top), and iterative reasoning steps for viewpoint-guided spatial understanding.
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 11：强化学习系统提示。** 该指令提示定义受约束的三视图三维分析工作流，包括工具调用格式、角度选择规则（左、右、顶部），以及用于视点引导空间理解的迭代推理步骤。

## Figure 12 — RL Continuation Prompt During Non-final Turns
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> > `=== Multi-Step Analysis: Iteration {current_iteration}/{max_iterations} ===`
> Original Question: `{question}`
>
> Your Previous Response:  
> `{last_response}`
>
> Tool Execution Summary:  
> `{tool_summary_text}`  
> `{angle_info_text}`
>
> Original Images:  
> `{original_images_info}`
>
> Generated Images Available for Analysis:  
> `{additional_images_info}`
>
> `=== Next Steps ===`
>
> You have `{remaining}` more turn(s) available. You can:
>
> Continue investigating - Call tools with DIFFERENT parameters:
> - IMPORTANT: Your original input images are already at (azimuth=0°, elevation=0°). DO NOT call Pi3 tools with (0°, 0°) again!
> - For Pi3 tools: Try NEW viewing angles to understand the 3D structure better
>
> Instructions:
> - Think: Do you need to see the object from another NEW angle (NOT 0°,0°!) to answer the question better?
> - If YES: Use `<tool_call></tool_call>` to request a DIFFERENT viewing angle (avoid 0°,0° as you already have it!)
> - If NO: output your thinking process in `<think></think>` and your final answer in `<answer></answer>`. Only put letters of option in `<answer>` `</answer>` tags, do not put any other text.
> - You only have 8 viewing angles to **choose**:
> - Left views (see scenes from right view): (azimuth_angle, elevation_angle) = (-45°, 0°)/(-90°, 0°)
> - Right views (see scenes from left view): (azimuth_angle, elevation_angle) = (45°, 0°)/(90°, 0°)
> - Top views (see scenes from top view, better capture the object relation and relatifve position of cam and objects.): (azimuth_angle, elevation_angle) = (0°, 60°)
> - Opposite views: (azimuth_angle, elevation_angle) = (45°, 60°)/(45°, 30°)/(-45°, 30°)
> - Do not request the same angle as before.
>
> Note that in 3D reconstruction, the camera numbering corresponds directly to the image numbering — cam1 represents the first frame.  
> You can examine the image to understand what is around cam1.  
> The 3D reconstruction provides relative positional information, so you should reason interactively and complementarily between the 2D image and the 3D reconstruction to form a complete understanding.
>
> IMPORTANT: You MUST start your response with `<think>...</think>` tags to explain your reasoning!
>
> Provide final answer - If you have sufficient information from current viewpoints:
> - Output your comprehensive analysis in `<think></think>` tags
> - Reference the specific viewpoints that helped you understand the structure
> - if you want to provide final answer, the reasoning process and answer are enclosed within `<think>` `</think>` and `<answer>` `</answer>` tags, respectively, i.e., `<think> reasoning process here </think><answer> answer here </answer>`
>
> Please continue:
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> > `=== 多步分析：第 {current_iteration}/{max_iterations} 次迭代 ===`
> 原始问题：`{question}`
>
> 你先前的响应：  
> `{last_response}`
>
> 工具执行摘要：  
> `{tool_summary_text}`  
> `{angle_info_text}`
>
> 原始图像：  
> `{original_images_info}`
>
> 可用于分析的生成图像：  
> `{additional_images_info}`
>
> `=== 后续步骤 ===`
>
> 你还有 `{remaining}` 轮可用。你可以：
>
> 继续调查——使用不同参数调用工具：
> - 重要：你的原始输入图像已经处于 (azimuth=0°, elevation=0°)。不要再次用 (0°, 0°) 调用 Pi3 工具！
> - 对于 Pi3 工具：尝试新的观察角度，以更好地理解三维结构
>
> 指令：
> - 思考：为了更好地回答问题，你是否需要从另一个新角度（不是 0°,0°！）观察物体？
> - 如果是：使用 `<tool_call></tool_call>` 请求一个不同的观察角度（避免 0°,0°，因为你已经拥有该视图！）
> - 如果否：在 `<think></think>` 中输出思考过程，并在 `<answer></answer>` 中输出最终答案。`<answer>` `</answer>` 标签中只能放选项字母，不要放任何其他文本。
> - 你只有 8 个观察角度可供**选择**：
> - 左侧视图（从右侧视角观察场景）：(azimuth_angle, elevation_angle) = (-45°, 0°)/(-90°, 0°)
> - 右侧视图（从左侧视角观察场景）：(azimuth_angle, elevation_angle) = (45°, 0°)/(90°, 0°)
> - 顶部视图（从顶部视角观察场景，更好地捕捉物体关系以及相机与物体的相对位置）：(azimuth_angle, elevation_angle) = (0°, 60°)
> - 相对视图：(azimuth_angle, elevation_angle) = (45°, 60°)/(45°, 30°)/(-45°, 30°)
> - 不要请求与之前相同的角度。
>
> 请注意，在三维重建中，相机编号与图像编号直接对应——cam1 表示第一帧。  
> 你可以检查图像，以了解 cam1 周围有什么。  
> 三维重建提供相对位置信息，因此你应在二维图像与三维重建之间进行交互式、互补式推理，以形成完整理解。
>
> 重要：你必须以 `<think>...</think>` 标签开始响应，以解释你的推理！
>
> 提供最终答案——如果你从当前视点获得了充分信息：
> - 在 `<think></think>` 标签中输出全面分析
> - 引用帮助你理解结构的具体视点
> - 如果要提供最终答案，推理过程和答案应分别置于 `<think>` `</think>` 与 `<answer>` `</answer>` 标签中，即 `<think> reasoning process here </think><answer> answer here </answer>`
>
> 请继续：

![Fig. 12](3d%20agent/Think3D/assets/page_021_fig_fig_12.png)
**Caption:** Fig. 12. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 12。完整原文图注及可检索内容见下文对应条目。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Fig. 12: The RL continuation prompt used during non-final turns.** Iterative-step instruction prompt outlining allowed viewpoint choices (left/right/top), tool-call rules, and the decision process for progressing or concluding 3D spatial analysis.
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 12：非最终轮次中使用的强化学习持续提示。** 该迭代步骤指令提示概述允许的视点选择（左/右/顶部）、工具调用规则，以及推进或结束三维空间分析的决策过程。

## Figure 13 — RL Continuation Prompt in the Final Turn
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> > ⚠️ WARNING: This is the FINAL turn
> Original Question: `{question}`
>
> Original Images:  
> `{original_images_info}`
>
> The 3D Reconstruction image.  
> `{additional_images_info}`
>
> Note that in 3D reconstruction, the camera numbering corresponds directly to the image numbering — cam1 represents the first frame.  
> You can examine the image to understand what is around cam1.  
> The 3D reconstruction provides relative positional information, so you should reason interactively and complementarily between the 2D image and the 3D reconstruction to form a complete understanding.
>
> All available tools have been used up, and you can no longer call any additional tools. You have no remaining steps for tool invocation. You can now see the different perspectives generated by the previous tool calls, as well as the original image. Please use the provided content to answer the original question.
>
> You MUST NOT call any tools.  
> You MUST NOT output `<tool_call>`.  
> You MUST directly reason and answer in this round.  
> All reasoning MUST be written explicitly within `<think>` `</think>` tags.  
> The final answer MUST be written within `<answer>` `</answer>` tags.
>
> Format strictly as follows:  
> `<think>[Your reasoning process here — show step-by-step thinking, explanations, or derivations]</think><answer>`  
> `[Your final answer here — only put your choice here]</answer>`
>
> Example:  
> `<think>First, analyze the question carefully. Then, derive the solution using logical reasoning.</think>`  
> `<answer>A</answer>`
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> > ⚠️ 警告：这是最终轮次
> 原始问题：`{question}`
>
> 原始图像：  
> `{original_images_info}`
>
> 三维重建图像。  
> `{additional_images_info}`
>
> 请注意，在三维重建中，相机编号与图像编号直接对应——cam1 表示第一帧。  
> 你可以检查图像，以了解 cam1 周围有什么。  
> 三维重建提供相对位置信息，因此你应在二维图像与三维重建之间进行交互式、互补式推理，以形成完整理解。
>
> 所有可用工具都已用尽，你不能再调用任何其他工具。你已没有剩余的工具调用步骤。现在你可以看到先前工具调用生成的不同视角以及原始图像。请使用所提供的内容回答原始问题。
>
> 你绝对不能调用任何工具。  
> 你绝对不能输出 `<tool_call>`。  
> 你必须在本轮中直接推理并作答。  
> 所有推理都必须明确写在 `<think>` `</think>` 标签内。  
> 最终答案必须写在 `<answer>` `</answer>` 标签内。
>
> 严格采用以下格式：  
> `<think>[在此写出你的推理过程——展示逐步思考、解释或推导]</think><answer>`  
> `[在此写出你的最终答案——这里只能放你的选择]</answer>`
>
> 示例：  
> `<think>首先，仔细分析问题。然后，使用逻辑推理推导解决方案。</think>`  
> `<answer>A</answer>`

![Fig. 13](3d%20agent/Think3D/assets/page_022_fig_fig_13.png)
**Caption:** Fig. 13. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 13。完整原文图注及可检索内容见下文对应条目。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Fig. 13: The RL continuation prompt used in the final turn.** Final-turn instruction prompt specifying the no-tool phase, requiring explicit reasoning and a final answer based solely on previously generated 3D views and the original image.
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 13：最终轮次中使用的强化学习持续提示。** 该最终轮指令提示规定无工具阶段，要求仅依据先前生成的三维视图和原始图像进行明确推理并给出最终答案。

## Figure 14 — Prompt Without Tools
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> > You are a helpful assistant that can analyze images and answer questions.
>
> Please analyze the following image(s):
>
> Images to analyze:  
> `{images_info}`
>
> Question:  
> `{question}`
>
> Think step by step to analyze the question and provide a detailed answer.
>
> You MUST output your thinking process in `<think></think>` and your final answer in `<answer></answer>`.  
> Only put Options in `<answer></answer>` tags, do not put any other text.
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> > 你是一名能够分析图像并回答问题的有用助手。
>
> 请分析以下图像：
>
> 待分析图像：  
> `{images_info}`
>
> 问题：  
> `{question}`
>
> 请逐步思考、分析问题，并给出详细答案。
>
> 你必须在 `<think></think>` 中输出思考过程，并在 `<answer></answer>` 中输出最终答案。  
> `<answer></answer>` 标签中只能放选项，不要放任何其他文本。

![Fig. 14](3d%20agent/Think3D/assets/page_022_fig_fig_14.png)
**Caption:** Fig. 14. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 14。完整原文图注及可检索内容见下文对应条目。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Fig. 14: The prompt without tools.** Base instruction prompt for direct image-question analysis, requiring explicit reasoning and final answer formatting without tool interactions.
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 14：无工具提示。** 用于直接进行图像—问题分析的基础指令提示，要求在无工具交互的情况下进行明确推理并按规定格式输出最终答案。

## Figure 15 — Critique Prompt and Refinement Prompt
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> > `=== Self-Refine: Critique Round {critique_round + 1}/{max_iterations} ===`
>
> You are a critical reviewer. Your task is to carefully analyze the following answer and provide constructive feedback.
>
> Original Question:  
> `{question}`
>
> Answer to Critique:  
> `{last_answer}`
>
> Your Task:  
> Please critically evaluate the above answer. Consider:
> 1. Correctness: Is the answer factually correct? Are there any logical errors?
> 2. Completeness: Does the answer fully address all aspects of the question?
> 3. Reasoning: Is the reasoning clear and well-supported by visual evidence?
> 4. Confidence: How confident should we be in this answer? Are there alternative interpretations?
>
> Provide your critique in `<critique></critique>` tags. Be specific about:
> - What aspects are correct and well-reasoned
> - What aspects might be wrong or need improvement
> - Specific suggestions for how to improve the answer
>
> Format:  
> `<critique> [Your detailed critique here] </critique>"""`
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> > `=== 自我精炼：第 {critique_round + 1}/{max_iterations} 轮批评 ===`
>
> 你是一名严格的评审者。你的任务是仔细分析以下答案并提供建设性反馈。
>
> 原始问题：  
> `{question}`
>
> 待批评的答案：  
> `{last_answer}`
>
> 你的任务：  
> 请批判性地评价上述答案。请考虑：
> 1. 正确性：答案在事实层面是否正确？是否存在逻辑错误？
> 2. 完整性：答案是否充分回应了问题的所有方面？
> 3. 推理：推理是否清晰，并得到视觉证据的充分支持？
> 4. 置信度：我们应当对该答案有多大信心？是否存在其他解释？
>
> 请在 `<critique></critique>` 标签中提供批评。请具体说明：
> - 哪些方面正确且推理充分
> - 哪些方面可能错误或需要改进
> - 如何改进答案的具体建议
>
> 格式：  
> `<critique> [在此写出你的详细批评] </critique>"""`
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> > `=== Self-Refine: Refinement Round {refine_round}/{max_iterations} ===`
>
> Based on the critique below, please refine your answer to the original question.
>
> Original Question:  
> `{question}`
>
> Your Previous Answer:  
> `{last_answer}`
>
> Critique of Your Answer:  
> `{critique}`
>
> Your Task:  
> Carefully consider the critique and improve your answer. Address the issues raised and strengthen your reasoning.
>
> Please provide an improved answer based on the critique.  
> You MUST output your thinking in `<think></think>` tags and your refined answer in `<answer></answer>` tags."""
>
> Format your response as:  
> `<think> [Your refined reasoning, addressing the critique] </think>`  
> `<answer> [Your refined answer] </answer>"""`
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> > `=== 自我精炼：第 {refine_round}/{max_iterations} 轮精炼 ===`
>
> 请根据下方批评，精炼你对原始问题的答案。
>
> 原始问题：  
> `{question}`
>
> 你先前的答案：  
> `{last_answer}`
>
> 对你答案的批评：  
> `{critique}`
>
> 你的任务：  
> 仔细考虑批评并改进答案。处理所指出的问题，并加强你的推理。
>
> 请根据批评提供改进后的答案。  
> 你必须在 `<think></think>` 标签中输出思考，并在 `<answer></answer>` 标签中输出精炼后的答案。"""
>
> 按以下格式作答：  
> `<think> [针对批评进行改进后的推理] </think>`  
> `<answer> [精炼后的答案] </answer>"""`

![Fig. 15](3d%20agent/Think3D/assets/page_023_fig_fig_15.png)
**Caption:** Fig. 15. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 15。完整原文图注及可检索内容见下文对应条目。
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Fig. 15: The critique prompt and refinement prompt used in the self-refine experiment.**
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **图 15：自我精炼实验中使用的批评提示和精炼提示。**

# Appendix B. Further Experiment Analysis

## Ego view analysis
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> As shown in Fig 16, we visualize the proportion of ego-view versus global-view usage by GPT-4.1 across different tasks. We find that tasks requiring fine-grained local understanding—such as MindCube and Object Direction—exhibit a much higher reliance on ego-view. In contrast, tasks like Route Planning, which demand broader global context, show minimal use of ego-view and favor global-view instead.
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 如图 16 所示，我们可视化了 GPT-4.1 在不同任务中使用自我视图与全局视图的比例。我们发现，需要细粒度局部理解的任务——如 MindCube 和 Object Direction——对自我视图的依赖高得多。相比之下，Route Planning 等需要更广泛全局上下文的任务极少使用自我视图，而是偏好全局视图。

![Fig. 16](3d%20agent/Think3D/assets/page_024_fig_fig_16.png)
**Caption:** Fig. 16. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 16。完整原文图注及可检索内容见下文对应条目。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Fig. 16: Ego view usage ratio across different tasks.** Distribution of GPT-4.1’s reliance on ego-view versus global-view across tasks. Fine-grained tasks emphasize ego-centric information, whereas tasks requiring broad context predominantly utilize global-view.
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 16：不同任务中的自我视图使用比例。** GPT-4.1 在各任务中依赖自我视图与全局视图的分布。细粒度任务强调以自我为中心的信息，而需要广泛上下文的任务主要使用全局视图。

## Tool calling iteration analysis
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> As shown in Fig 17, we also visualize the proportion of tool calls across different tasks. We find that for route planning, GPT-4.1 uses the tools much less frequently. For the other tasks, GPT-4.1 often performs multiple rounds of tool calls to obtain richer spatial information.
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 如图 17 所示，我们还可视化了不同任务中的工具调用比例。我们发现，对于路径规划，GPT-4.1 使用工具的频率低得多。对于其他任务，GPT-4.1 通常会执行多轮工具调用，以获取更丰富的空间信息。

![Fig. 17](3d%20agent/Think3D/assets/page_024_fig_fig_17.png)
**Caption:** Fig. 17. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 17。完整原文图注及可检索内容见下文对应条目。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Fig. 17: Tool calling iteration ratio across different tasks.** GPT-4.1 rarely uses tools for route planning, while conducting multiple rounds of tool calls for other tasks to acquire richer spatial information.
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 17：不同任务中的工具调用迭代比例。** GPT-4.1 很少为路径规划使用工具，而在其他任务中会进行多轮工具调用，以获得更丰富的空间信息。

# Appendix C. Think3D-RL Training And Evaluation Setting
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Table 5: Training and evaluation parameters used in both the RL optimization process and subsequent evaluation.**
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **表 5：强化学习优化过程及后续评估中使用的训练与评估参数。**
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> | Parameter | Setting |
> |---|---:|
> | Foundation model | Qwen3-4B-Instruct |
> | Number of trained agents | 1 |
> | Number of solution rounds | 3 |
> | Number of evaluation rounds | 3 |
> | Horizon for discussion history | 1 |
> | Token limit for prompts | 180000 |
> | Token limit for responses | 1024 |
> | Training temperature | 0.6 |
> | Evaluation temperature | 1.0 |
> | Clipping epsilon | 0.2 |
> | Weight of KL penalty | 0.05 |
> | Number of training epochs | 1 |
> | Training batch size | 32(8*4accu) |
> | Rollout batch size | 64 |
> | Optimizer name | AdamW |
> | Learning rate | 1e-6 |
> | Weight decay | 0.1 |
> | Gradient norm | 0.5 |
> | Gradient clipping | False |
> | Gradient checkpoint | True |
> | Flash Attention | True |
> | Mixed precision | True |
> | Enable vLLM | False |
> | Enable DeepSpeed | True |
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> | 参数 | 设置 |
|---|---:|
| 基础模型 | Qwen3-4B-Instruct |
| 训练的代理数量 | 1 |
| 求解轮数 | 3 |
| 评估轮数 | 3 |
| 讨论历史窗口 | 1 |
| 提示 token 上限 | 180000 |
| 响应 token 上限 | 1024 |
| 训练温度 | 0.6 |
| 评估温度 | 1.0 |
| 裁剪 epsilon | 0.2 |
| KL 惩罚权重 | 0.05 |
| 训练 epoch 数 | 1 |
| 训练批大小 | 32(8*4accu) |
| Rollout 批大小 | 64 |
| 优化器名称 | AdamW |
| 学习率 | 1e-6 |
| 权重衰减 | 0.1 |
| 梯度范数 | 0.5 |
| 梯度裁剪 | False |
| 梯度检查点 | True |
| Flash Attention | True |
| 混合精度 | True |
| 启用 vLLM | False |
| 启用 DeepSpeed | True |
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> As shown in Tab 5, we provide the parameters used for both RL training and evaluation. For all experiments, including the main results and ablation studies, we run each setting three times and report the average performance to ensure a fair comparison.
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 如表 5 所示，我们给出了强化学习训练和评估所使用的参数。对于包括主要结果和消融研究在内的所有实验，我们对每项设置运行三次并报告平均性能，以确保公平比较。

# Appendix D. Angle choose
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Random samples two views from eight candidate angles, while Heuristic uses fixed views (−45, 30) and (45, 30); both use the original Qwen3-VL-4B. We also test the RL-trained backbone with random exploration (RLrandom). All methods run three rounds. As shown in Table 6, RLrandom performs similarly to Random, while the learned RL policy significantly improves performance, indicating that gains mainly come from spatial policy learning.
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Random 从八个候选角度中随机采样两个视图，而 Heuristic 使用固定视图 (−45, 30) 和 (45, 30)；二者均使用原始 Qwen3-VL-4B。我们还测试了采用随机探索的强化学习训练骨干网络（RLrandom）。所有方法均运行三轮。如表 6 所示，RLrandom 的表现与 Random 相近，而学习得到的强化学习策略显著提升了性能，这表明增益主要来自空间策略学习。

![Table 6](3d%20agent/Think3D/assets/page_026_fig_table_6.png)
**Caption:** Table 6. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Table 6。完整原文图注及可检索内容见下文对应条目。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Table 6: Effect of exploration strategies.**
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **表 6：探索策略的影响。**
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> | Angle | BLINK | MindCube | Avg (%) |
> |---|---:|---:|---:|
> | Random | 45.86 | 27.50 | 36.68 |
> | Heuristic | 47.37 | 30.00 | 38.69 |
> | RLrandom | 45.11 | 30.00 | 37.56 |
> | RL | 53.39 | 40.82 | 47.11 |
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> | 角度策略 | BLINK | MindCube | 平均值 (%) |
|---|---:|---:|---:|
| Random | 45.86 | 27.50 | 36.68 |
| Heuristic | 47.37 | 30.00 | 38.69 |
| RLrandom | 45.11 | 30.00 | 37.56 |
| RL | 53.39 | 40.82 | 47.11 |

# Appendix E. Results on More Models
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We provide additional evaluation results on more vision-language models in this section. The results on BLINK(Multi-view) and MindCube subset are reported in Table 7. These results provide a broader comparison of current VLMs on spatial reasoning benchmarks.
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本节提供更多视觉语言模型的额外评估结果。BLINK(Multi-view) 和 MindCube 子集上的结果见表 7。这些结果对当前 VLM 在空间推理基准上的表现提供了更广泛的比较。

![Table 7](3d%20agent/Think3D/assets/page_026_fig_table_7.png)
**Caption:** Table 7. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Table 7。完整原文图注及可检索内容见下文对应条目。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Table 7: More results on BLINK(Multi-view) and the MindCube subbset(%).**
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **表 7：BLINK(Multi-view) 和 MindCube 子集上的更多结果（%）。**
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> | Model | BLINK (MV) | MC (Rotation) | MC (Among) | MC (Around) | Avg |
> |---|---:|---:|---:|---:|---:|
> | InternVL3.5-1B | 51.13 | 37.50 | 35.00 | 25.00 | 36.66 |
> | InternVL3.5-2B | 49.62 | 37.50 | 32.50 | 42.50 | 38.46 |
> | InternVL3.5-4B | 53.38 | 50.00 | 30.00 | 25.00 | 36.67 |
> | Llava-onevision-qwen2-0.5b | 43.61 | 32.50 | 22.50 | 40.00 | 34.65 |
> | Llava-onevision-qwen2-7b | 45.86 | 37.50 | 25.00 | 35.00 | 35.84 |
> | Qwen3-VL-8B | 47.36 | 45.00 | 30.00 | 47.50 | 42.47 |
> | Qwen3-VL-30B-a3b-instruct | 49.62 | 37.50 | 37.50 | 52.50 | 44.28 |
> | GPT-4.1-mini | 49.62 | 54.17 | 39.17 | 45.83 | 47.20 |
> | Think3D(GPT-4.1-mini) | 52.38 | 53.33 | 47.5 | 41.67 | 48.72 |
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> | 模型 | BLINK (MV) | MC（Rotation） | MC（Among） | MC（Around） | 平均值 |
|---|---:|---:|---:|---:|---:|
| InternVL3.5-1B | 51.13 | 37.50 | 35.00 | 25.00 | 36.66 |
| InternVL3.5-2B | 49.62 | 37.50 | 32.50 | 42.50 | 38.46 |
| InternVL3.5-4B | 53.38 | 50.00 | 30.00 | 25.00 | 36.67 |
| Llava-onevision-qwen2-0.5b | 43.61 | 32.50 | 22.50 | 40.00 | 34.65 |
| Llava-onevision-qwen2-7b | 45.86 | 37.50 | 25.00 | 35.00 | 35.84 |
| Qwen3-VL-8B | 47.36 | 45.00 | 30.00 | 47.50 | 42.47 |
| Qwen3-VL-30B-a3b-instruct | 49.62 | 37.50 | 37.50 | 52.50 | 44.28 |
| GPT-4.1-mini | 49.62 | 54.17 | 39.17 | 45.83 | 47.20 |
| Think3D(GPT-4.1-mini) | 52.38 | 53.33 | 47.5 | 41.67 | 48.72 |

# Appendix F Interaction Visualization

# 附录 F 交互可视化
> <span style="color:#3B82F6"><strong>Para. 1:</strong></span>
> **Question:**

> If I am standing at the same spot and facing the same direction as shown in image 2, then I turn 180 degrees around, what is to my right?

> A. Several pictures  B. Window and brown cabinet  C. Green cabinet
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span>
**问题：**

如果我站在同一地点，面向图像 2 所示的同一方向，然后转身 180 度，我的右边是什么？

A. 几幅画  B. 窗户和棕色橱柜  C. 绿色橱柜
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span>
> ```text
> Assistant: <think>Let's break down the question and images step by step:
> - Image 1 shows a green cabinet, a door, and a picture frame.
> - Image 2 shows a window and a brown cabinet.
> - Image 3 shows several pictures on the wall and a green cabinet (partially visible).

> Let's visualize:
> - Facing image 2 direction, turning 180° means facing the opposite direction (image 3's direction).
> - "To my right" after turning 180° is the same as "to my left" before turning (relative to the original facing).

> To be sure, I need to confirm the spatial arrangement of the cabinets, window, and pictures. The best way is to use a top-down (elevation=60°) view to see the relative positions of all objects and cameras.

> I will call the Pi3 tool with a top-down view (azimuth=0°, elevation=60°) using camera 1 as reference to get the spatial layout.
> </think>
> <tool_call>{"name": "pi3_tool", "arguments": {"image_path": ["dataset/mindcube/data/other_all_image/rotation/arkitscenes_43896310/view_1_1.jpg", "dataset/mindcube/data/other_all_image/rotation/arkitscenes_43896310/view_2_7.jpg", "dataset/mindcube/data/other_all_image/rotation/arkitscenes_43896310/view_3_14.jpg"], "azimuth_angle": 0, "elevation_angle": 60, "rotation_reference_camera": 1, "camera_view": false}}</tool_call>
> ```
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span>
```text
Assistant: <think>让我们逐步分解问题和图像：
- 图像 1 显示一个绿色橱柜、一扇门和一个画框。
- 图像 2 显示一扇窗户和一个棕色橱柜。
- 图像 3 显示墙上的几幅画和一个绿色橱柜（部分可见）。

让我们进行可视化：
- 面向图像 2 的方向，转身 180° 意味着面向相反方向（图像 3 的方向）。
- 转身 180° 后“我的右边”等同于转身前“我的左边”（相对于原始朝向）。

为确保无误，我需要确认橱柜、窗户和画的空间排列。最佳方式是使用俯视（elevation=60°）视图，查看所有物体和相机的相对位置。

我将调用 Pi3 工具，使用以相机 1 为参照的俯视图（azimuth=0°, elevation=60°）来获取空间布局。
</think>
<tool_call>{"name": "pi3_tool", "arguments": {"image_path": ["dataset/mindcube/data/other_all_image/rotation/arkitscenes_43896310/view_1_1.jpg", "dataset/mindcube/data/other_all_image/rotation/arkitscenes_43896310/view_2_7.jpg", "dataset/mindcube/data/other_all_image/rotation/arkitscenes_43896310/view_3_14.jpg"], "azimuth_angle": 0, "elevation_angle": 60, "rotation_reference_camera": 1, "camera_view": false}}</tool_call>
```
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span>
> ```text
> Assistant: <think>Let's reason using the images and the top-down 3D reconstruction:
> Step-by-step:
> 1. **Image 2 (cam2)**: Facing the window and brown cabinet.
> 2. **Turn 180°**: Now facing the opposite direction (as in image 3, cam3).
> 3. **What is to my right?**: When facing the direction of image 3, "to my right" is the direction that was "to my left" when facing image 2.

> From the top-down view:
> - The cameras are arranged in a triangle, each 90° apart.
> - Cam2 (image 2) faces the window/brown cabinet.
> - Cam3 (image 3) faces the wall with several pictures.
> - Cam1 (image 1) faces the green cabinet and door.

> When facing cam3's direction (after 180° turn from cam2), the green cabinet (from cam1) is to the right of cam3's viewpoint, and the wall with several pictures is directly ahead.

> **Mapping options:**
> A. Several pictures — these are directly ahead when facing cam3.
> B. Window and brown cabinet — these are behind you (opposite direction).
> C. Green cabinet — this is to the right when facing cam3.

> **Conclusion:** After turning 180° from image 2's direction, the green cabinet is to your right.
> </think><answer>C. Green cabinet</answer>
> ```
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span>
```text
Assistant: <think>让我们利用图像和俯视 3D 重建进行推理：
逐步分析：
1. **图像 2 (cam2)**：面向窗户和棕色橱柜。
2. **转身 180°**：现在面向相反方向（如图像 3，即 cam3）。
3. **我的右边是什么？**：当面向图像 3 的方向时，“我的右边”就是面向图像 2 时“我的左边”所指的方向。

从俯视图来看：
- 相机呈三角形排列，彼此相隔 90°。
- Cam2（图像 2）面向窗户/棕色橱柜。
- Cam3（图像 3）面向挂有几幅画的墙。
- Cam1（图像 1）面向绿色橱柜和门。

面向 cam3 的方向（从 cam2 转身 180° 后）时，绿色橱柜（来自 cam1）位于 cam3 视点的右侧，而挂有几幅画的墙就在正前方。

**选项映射：**
A. 几幅画——面向 cam3 时，它们就在正前方。
B. 窗户和棕色橱柜——它们在你身后（相反方向）。
C. 绿色橱柜——面向 cam3 时，它在右侧。

**结论：** 从图像 2 的方向转身 180° 后，绿色橱柜位于你的右侧。
</think><answer>C. 绿色橱柜</answer>
```

![Fig. 18: The Mindcube example.](3d%20agent/Think3D/assets/page_027_fig_fig_18.png)
**Caption:** Fig. 18: The Mindcube example.. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 18: The Mindcube example.。完整原文图注及可检索内容见下文对应条目。

*Fig. 18: The Mindcube example.*

*图 18：Mindcube 示例。*
> <span style="color:#3B82F6"><strong>Para. 4:</strong></span>
> **Question:**

> If I am standing at the same spot and facing the same direction as shown in image 1, what is to my behind?

> A. Wardrobes  B. Door  C. Window
> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span>
**问题：**

如果我站在同一地点，面向图像 1 所示的同一方向，我身后是什么？

A. 衣柜  B. 门  C. 窗户
> <span style="color:#3B82F6"><strong>Para. 5:</strong></span>
> ```text
> Assistant: <think>
> <think>
> Let's analyze the spatial arrangement step by step.
> Image 1 shows a door on the left and what appears to be wardrobes on the right.
>   - Image 2 is said to be a 90° right turn from image 1 and shows wardrobes directly ahead, with a door visible to the left and background room elements on the right.
>   - Image 3 is another 90° right turn (so 180° from image 1), showing a window and likely facing the direction opposite image 1.

> Given the camera rotation pattern:
>   - If I'm standing in the same spot facing the door and wardrobes (as in image 1), then turning right 90° takes me to face the wardrobes directly (image 2), and another 90°, the window (image 3).
>   - The question asks what is behind me when facing the image 1 direction.

> To confirm, the spatial layout should show what's on the opposite side of image 1's direction, which is image 3's viewpoint. In image 3, the window is directly in front, so that would be behind me if I started facing the door and wardrobes.

> For further confirmation of object positions and spatial relations, a top-view 3D reconstruction can clarify relative placements (especially the window's location in relation to cam1 and cam2). I will call the tool for a top view (azimuth=180°, elevation=60°) to see relationships from above.

> I will call the tool to generate a top-down view.
> <tool_call>
> {"name": "pi3_tool", "arguments": {"image_path": ["dataset/mindcube/data/other_all_image/rotation/arkitscenes_41126518/view_1_8.jpg", "dataset/mindcube/data/other_all_image/rotation/arkitscenes_41126518/view_2_27.jpg", "dataset/mindcube/data/other_all_image/rotation/arkitscenes_41126518/view_3_59.jpg"], "azimuth_angle": 180, "elevation_angle": 60, "camera_view": false}}
> </tool_call>
> ```
> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span>
```text
Assistant: <think>
<think>
让我们逐步分析空间排列。
图像 1 左侧显示一扇门，右侧显示看起来像衣柜的物体。
  - 据称图像 2 是从图像 1 向右转 90°，它显示衣柜就在正前方，左侧可见一扇门，右侧是房间背景元素。
  - 图像 3 是再次向右转 90°（因此相对图像 1 为 180°），其中显示一扇窗户，朝向很可能与图像 1 相反。

根据相机旋转模式：
  - 如果我站在同一地点，面向门和衣柜（如图像 1），那么向右转 90° 会让我直接面向衣柜（图像 2），再转 90° 则面向窗户（图像 3）。
  - 问题询问的是面向图像 1 的方向时，我身后是什么。

为进行确认，空间布局应显示图像 1 朝向相反一侧的内容，即图像 3 的视点。在图像 3 中，窗户就在正前方，因此如果我一开始面向门和衣柜，它就会在我身后。

为了进一步确认物体位置和空间关系，俯视 3D 重建可以阐明相对位置（尤其是窗户相对于 cam1 和 cam2 的位置）。我将调用工具获得俯视图（azimuth=180°, elevation=60°），从上方查看这些关系。

我将调用工具生成俯视图。
<tool_call>
{"name": "pi3_tool", "arguments": {"image_path": ["dataset/mindcube/data/other_all_image/rotation/arkitscenes_41126518/view_1_8.jpg", "dataset/mindcube/data/other_all_image/rotation/arkitscenes_41126518/view_2_27.jpg", "dataset/mindcube/data/other_all_image/rotation/arkitscenes_41126518/view_3_59.jpg"], "azimuth_angle": 180, "elevation_angle": 60, "camera_view": false}}
</tool_call>
```
> <span style="color:#3B82F6"><strong>Para. 6:</strong></span>
> ```text
> Assistant: <think>
> Let’s reason through the answer using the provided images and the 3D top-down reconstruction.
>     - Image 1 (cam1) shows a door on the left and wardrobes on the right.
>     - We know from the prompt that for image 2 (cam2), the camera was rotated 90° right (clockwise), and for image 3 (cam3), another 90° right (so image 3's view is directly opposite to image 1's view).
>     - The 3D reconstruction (top-down, azimuth=180°, elevation=60°) confirms the spatial relations:
>          - The camera markers’ field of view confirms that cam1 faces towards the top edge of the box (where the door and wardrobes are).
>          - Cam3, 180° from cam1, is facing towards the bottom edge, where the large window and sofa are located.

> If you are standing at cam1's spot, facing the same way as image 1 (towards the door/wardrobes), your back is towards the opposite direction — i.e., towards the window and sofa, as seen in cam3 and in the 3D model.
> Thus, the object behind you while facing image 1's direction is the window.

> </think>
> <answer>C. Window</answer>
> ```
> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span>
```text
Assistant: <think>
让我们利用所提供的图像和俯视 3D 重建来推理答案。
    - 图像 1 (cam1) 左侧显示一扇门，右侧显示衣柜。
    - 根据提示可知，对于图像 2 (cam2)，相机向右旋转了 90°（顺时针）；对于图像 3 (cam3)，又向右旋转了 90°（因此图像 3 的视角与图像 1 的视角正好相反）。
    - 3D 重建（俯视，azimuth=180°, elevation=60°）确认了空间关系：
         - 相机标记的视场确认 cam1 朝向盒子的上边缘（门和衣柜所在之处）。
         - 与 cam1 相差 180° 的 Cam3 朝向下边缘，大窗户和沙发位于那里。

如果你站在 cam1 的位置，朝向与图像 1 相同（朝向门/衣柜），你的背后就是相反方向——也就是朝向窗户和沙发，如 cam3 和 3D 模型中所示。
因此，面向图像 1 的方向时，位于你身后的物体是窗户。

</think>
<answer>C. 窗户</answer>
```

![Fig. 19: The Mindcube example.](3d%20agent/Think3D/assets/page_028_fig_fig_19.png)
**Caption:** Fig. 19: The Mindcube example.. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 19: The Mindcube example.。完整原文图注及可检索内容见下文对应条目。

*Fig. 19: The Mindcube example.*

*图 19：Mindcube 示例。*
> <span style="color:#3B82F6"><strong>Para. 7:</strong></span>
> **Question:**

> Is the camera moving left or right when shooting the video? Select from the following options.

> (A) left  (B) right
> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span>
**问题：**

拍摄视频时，相机是在向左移动还是向右移动？请从以下选项中选择。

(A) 向左  (B) 向右
> <span style="color:#3B82F6"><strong>Para. 8:</strong></span>
> ```text
> Assistant: <think>To determine whether the camera is moving left (clockwise) or right (counter-clockwise) around the object, I need to analyze the change in perspective between the two images. The key object is the mug with the bicycle and Chinese text. In the first image, the handle of the mug is on the right side, and in the second image, the handle is more visible and appears to have rotated further to the right, suggesting the camera has moved around the mug. To confirm the direction, I should examine the relative movement of background objects and the mug's orientation. A top-down view from 3D reconstruction will help clarify the camera's path around the mug and the direction of movement.
> </think>
> <tool_call>{"name": "pi3_tool", "arguments": {"image_path": ["dataset/BLINK_images/Multi-view_Reasoning_val_000101_img1.jpg", "dataset/BLINK_images/Multi-view_Reasoning_val_000101_img2.jpg"], "azimuth_angle": 0, "elevation_angle": 60, "rotation_reference_camera": 1, "camera_view": false}}</tool_call>
> ```
> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span>
```text
Assistant: <think>为了判断相机是围绕物体向左（顺时针）还是向右（逆时针）移动，我需要分析两幅图像之间的透视变化。关键物体是带有自行车和中文文字的马克杯。在第一幅图像中，杯柄位于马克杯右侧；在第二幅图像中，杯柄更加清晰可见，而且看起来进一步转向了右侧，这表明相机已经绕马克杯移动。为了确认方向，我应检查背景物体的相对移动和马克杯的朝向。3D 重建的俯视图将有助于阐明相机绕马克杯的路径和移动方向。
</think>
<tool_call>{"name": "pi3_tool", "arguments": {"image_path": ["dataset/BLINK_images/Multi-view_Reasoning_val_000101_img1.jpg", "dataset/BLINK_images/Multi-view_Reasoning_val_000101_img2.jpg"], "azimuth_angle": 0, "elevation_angle": 60, "rotation_reference_camera": 1, "camera_view": false}}</tool_call>
```
> <span style="color:#3B82F6"><strong>Para. 9:</strong></span>
> ```text
> (0, 60)    (90, 0)

> Assistant: <think>From the current 3D reconstruction (azimuth=60°, elevation=60°), I can see the relative positions of cam1 and cam2. Both cameras are positioned to the left of the scene (from the viewer's perspective), with cam2 slightly to the right of cam1. The mug's handle is more visible in the second image (cam2), indicating the camera moved to reveal more of the right side of the mug. The background objects (bottles and basket) also shift slightly rightward in the second image, consistent with a rightward (counter-clockwise) camera movement around the object.

> However, to be absolutely certain of the direction, I want to see the scene from a more horizontal viewpoint, which will clarify the arc of the camera movement. I will request a new viewpoint from azimuth=90°, elevation=0°, which gives a direct side view of the camera positions and their movement path.</think>
> ```
> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span>
```text
(0, 60)    (90, 0)

Assistant: <think>从当前的 3D 重建（azimuth=60°, elevation=60°）中，我可以看到 cam1 和 cam2 的相对位置。两个相机都位于场景左侧（从观察者视角看），cam2 略微位于 cam1 的右侧。马克杯的杯柄在第二幅图像 (cam2) 中更加可见，这表明相机发生了移动，从而显露出马克杯右侧的更多部分。背景物体（瓶子和篮子）在第二幅图像中也略微向右偏移，这与相机围绕物体向右（逆时针）移动一致。

不过，为了完全确定方向，我希望从一个更水平的视点观察场景，这将阐明相机移动的弧线。我将请求 azimuth=90°, elevation=0° 的新视点，以直接从侧面查看相机位置及其移动路径。</think>
```
> <span style="color:#3B82F6"><strong>Para. 10:</strong></span>
> ```text
> Assistant: <think>Let's synthesize all the evidence:

> 1. **2D Image Comparison**:
>   - In the first image, the mug's handle is barely visible, mostly hidden behind the mug.
>   - In the second image, the handle is clearly visible on the right side of the mug.
>   - The background objects (bottles, basket) shift slightly to the right in the second image, indicating the camera moved to reveal more of the right side of the scene.

> 2. **3D Reconstruction (azimuth=90°, elevation=0°)**:
>   - The top-down view shows cam1 (first image) is positioned slightly to the left of cam2 (second image).
>   - The camera movement path is from cam1 (left) to cam2 (right), both facing the scene.
>   - The arc of movement is consistent with a rightward (counter-clockwise) motion around the object.

> 3. **Spatial Reasoning**:
>   - If the camera moves rightward around the mug, the handle (which is on the right side of the mug from the initial viewpoint) becomes more visible.
>   - The 3D visualization confirms the camera's trajectory is from left to right.

> **Conclusion**: The camera is moving to the right (counter-clockwise) around the object, as evidenced by both the change in handle visibility and the 3D camera positions.

> </think>
> <answer>(B) right</answer>
> ```
> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span>
```text
Assistant: <think>让我们综合所有证据：

1. **2D 图像比较**：
  - 在第一幅图像中，马克杯的杯柄几乎不可见，大部分隐藏在杯身后面。
  - 在第二幅图像中，杯柄在马克杯右侧清晰可见。
  - 背景物体（瓶子、篮子）在第二幅图像中略微向右偏移，这表明相机移动后显露出场景右侧的更多部分。

2. **3D 重建 (azimuth=90°, elevation=0°)**：
  - 俯视图显示 cam1（第一幅图像）的位置略微位于 cam2（第二幅图像）的左侧。
  - 相机移动路径是从 cam1（左）到 cam2（右），两者都面向场景。
  - 移动弧线与围绕物体向右（逆时针）运动一致。

3. **空间推理**：
  - 如果相机围绕马克杯向右移动，杯柄（从初始视点看位于马克杯右侧）会变得更加可见。
  - 3D 可视化确认相机轨迹是从左向右。

**结论**：相机正在围绕物体向右（逆时针）移动，杯柄可见性的变化和 3D 相机位置都证明了这一点。

</think>
<answer>(B) 向右</answer>
```

![Fig. 20: The BLINK example.](3d%20agent/Think3D/assets/page_029_fig_fig_20.png)
**Caption:** Fig. 20: The BLINK example.. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 20: The BLINK example.。完整原文图注及可检索内容见下文对应条目。

*Fig. 20: The BLINK example.*

*图 20：BLINK 示例。*
> <span style="color:#3B82F6"><strong>Para. 11:</strong></span>
> **Question:**

> Is the camera moving left or right when shooting the video? Select from the following options.

> (A) left  (B) right
> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span>
**问题：**

拍摄视频时，相机是在向左移动还是向右移动？请从以下选项中选择。

(A) 向左  (B) 向右
> <span style="color:#3B82F6"><strong>Para. 12:</strong></span>
> ```text
> Assistant: <think>
> Step 1: Analyze both images for camera position and orientation changes.
> - Both images show a bowl and instant noodle containers on a shelf in a store.
> - In the first image, the camera is positioned to the right of the bowl and shelf, showing the aisle and products on the right side.
> - In the second image, the camera is more to the left of the bowl and shelf, facing more directly toward the front of the shelf, with the aisle less visible and the price tag more prominent.

> Step 2: Infer camera movement direction.
> - The camera starts from a position showing more of the aisle (right side of the shelf) and moves to a position showing more of the front of the shelf (left side).
> - This suggests the camera is moving left (clockwise around the object).

> Step 3: Use 3D reconstruction for confirmation.
> - To confirm, I will generate a top-down view (elevation=60°) to clearly see the relative camera positions and movement direction.
> </think>
> <tool_call>
> {"name": "pi3_tool", "arguments": {"image_path": ["dataset/BLINK_images/Multi-view_Reasoning_val_000119_img1.jpg", "dataset/BLINK_images/Multi-view_Reasoning_val_000119_img2.jpg"], "azimuth_angle": 0, "elevation_angle": 60, "rotation_reference_camera": 1, "camera_view": false}}
> </tool_call>
> ```
> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span>
```text
Assistant: <think>
步骤 1：分析两幅图像中的相机位置和朝向变化。
- 两幅图像都显示商店货架上的一个碗和方便面容器。
- 在第一幅图像中，相机位于碗和货架的右侧，显示右侧的过道和商品。
- 在第二幅图像中，相机更靠近碗和货架的左侧，更直接地面向货架正面，过道较不明显，而价格标签更加突出。

步骤 2：推断相机移动方向。
- 相机从一个能看到更多过道（货架右侧）的位置开始，移动到一个能看到更多货架正面（左侧）的位置。
- 这表明相机正在向左移动（围绕物体顺时针）。

步骤 3：使用 3D 重建进行确认。
- 为了确认，我将生成俯视图（elevation=60°），以清楚查看相机的相对位置和移动方向。
</think>
<tool_call>
{"name": "pi3_tool", "arguments": {"image_path": ["dataset/BLINK_images/Multi-view_Reasoning_val_000119_img1.jpg", "dataset/BLINK_images/Multi-view_Reasoning_val_000119_img2.jpg"], "azimuth_angle": 0, "elevation_angle": 60, "rotation_reference_camera": 1, "camera_view": false}}
</tool_call>
```
> <span style="color:#3B82F6"><strong>Para. 13:</strong></span>
> ```text
> Assistant: <think>
> Let's analyze the 3D reconstruction and the original images to clarify the camera movement direction.

> - In the top-down 3D view (azimuth=0°, elevation=60°), Cam1 (red) and Cam2 (blue) are positioned along the X axis, both facing toward the shelf with the bowls and instant noodles.
> - Cam1 is further to the left (lower X value), Cam2 is to the right (higher X value).
> - Comparing with the 2D images:
>   - Image 1 (Cam1): Shows more of the aisle on the right side of the shelf, with the bowl in the foreground and the instant noodles stacked to the left.
>   - Image 2 (Cam2): Shows more of the front of the shelf, with less aisle visible, and the price tag in front.

> From the 3D view, the camera moves from Cam1 (left side of the shelf, showing the aisle) to Cam2 (right side, facing the front of the shelf). This means the camera is moving to the right (counter-clockwise around the shelf).

> The 3D reconstruction confirms that the camera started on the left and ended on the right, moving counter-clockwise (right) around the object.
> </think>
> <answer>(B) right</answer>
> ```
> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span>
```text
Assistant: <think>
让我们分析 3D 重建和原始图像，以阐明相机的移动方向。

- 在俯视 3D 视图（azimuth=0°, elevation=60°）中，Cam1（红色）和 Cam2（蓝色）沿 X 轴布置，二者都面向放有碗和方便面的货架。
- Cam1 更靠左（X 值较低），Cam2 位于右侧（X 值较高）。
- 与 2D 图像进行比较：
  - 图像 1 (Cam1)：显示货架右侧更多的过道，碗位于前景，方便面堆叠在左侧。
  - 图像 2 (Cam2)：显示货架正面的更多部分，可见的过道较少，价格标签位于前方。

从 3D 视图来看，相机从 Cam1（货架左侧，显示过道）移动到 Cam2（右侧，面向货架正面）。这意味着相机正在向右移动（围绕货架逆时针）。

3D 重建确认相机从左侧开始，在右侧结束，围绕物体逆时针（向右）移动。
</think>
<answer>(B) 向右</answer>
```

![Fig. 21: The BLINK example.](3d%20agent/Think3D/assets/page_030_fig_fig_21.png)
**Caption:** Fig. 21: The BLINK example.. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 21: The BLINK example.。完整原文图注及可检索内容见下文对应条目。

*Fig. 21: The BLINK example.*

*图 21：BLINK 示例。*
> <span style="color:#3B82F6"><strong>Para. 14:</strong></span>
> **Question:**

> Measuring from the closest point of each object, which of these objects (heater, plant, chair, ceiling light) is the closest to the pillow?

> A. heater

> B. plant

> C. chair

> D. ceiling light
> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span>
**问题：**

从每个物体的最近点测量，以下物体（暖气、植物、椅子、顶灯）中哪一个离枕头最近？

A. 暖气

B. 植物

C. 椅子

D. 顶灯
> <span style="color:#3B82F6"><strong>Para. 15:</strong></span>
> ```text
> Assistant: <think>
> To answer which object (heater, plant, chair, ceiling light) is closest to the pillow (measuring from the closest point of each object), I first need to identify all four objects and the pillow in the frames. The pillow is clearly visible in frames 2, 3, 6, and 7. The plant (a green bush in a brown box) is visible in frame 6, right behind the pillow. The chair is visible in frames 2, 6, and 7, positioned near the foot/side of the bed and wall. The heater (radiator under the window) is visible in frame 1. The ceiling light (track light) is seen at the top of frame 1 but is physically far from the pillow, as it is on the ceiling.
> To determine proximity, I want a top-down view that can capture all objects’ spatial relationship. A top view (elevation=60°) will best reveal their placements relative to the pillow, especially between heater, plant, and chair.
> </think>
> <tool_call>
> {"name": "pi3x_tool", "arguments": {"image_path": ["temp_frames/scannetpp_bcd2436daf_frame_0.jpg", "temp_frames/scannetpp_bcd2436daf_frame_1.jpg", "temp_frames/scannetpp_bcd2436daf_frame_2.jpg", "temp_frames/scannetpp_bcd2436daf_frame_3.jpg", "temp_frames/scannetpp_bcd2436daf_frame_4.jpg", "temp_frames/scannetpp_bcd2436daf_frame_5.jpg", "temp_frames/scannetpp_bcd2436daf_frame_6.jpg"], "azimuth_angle": 0, "elevation_angle": 60, "rotation_reference_camera": 1, "camera_view": false}}
> </tool_call>
> ```
> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span>
```text
Assistant: <think>
为了回答哪个物体（暖气、植物、椅子、顶灯）离枕头最近（从每个物体的最近点测量），我首先需要在各帧中识别所有四个物体和枕头。枕头在第 2、3、6 和 7 帧中清晰可见。植物（棕色盒子中的绿色灌木）在第 6 帧中可见，就在枕头后面。椅子在第 2、6 和 7 帧中可见，位于床尾/床侧和墙附近。暖气（窗下的散热器）在第 1 帧中可见。顶灯（轨道灯）出现在第 1 帧顶部，但它实际上离枕头很远，因为它位于天花板上。
为了确定邻近程度，我想要一个能够呈现所有物体空间关系的俯视图。俯视图（elevation=60°）最能揭示它们相对于枕头的位置，尤其是暖气、植物和椅子之间的比较。
</think>
<tool_call>
{"name": "pi3x_tool", "arguments": {"image_path": ["temp_frames/scannetpp_bcd2436daf_frame_0.jpg", "temp_frames/scannetpp_bcd2436daf_frame_1.jpg", "temp_frames/scannetpp_bcd2436daf_frame_2.jpg", "temp_frames/scannetpp_bcd2436daf_frame_3.jpg", "temp_frames/scannetpp_bcd2436daf_frame_4.jpg", "temp_frames/scannetpp_bcd2436daf_frame_5.jpg", "temp_frames/scannetpp_bcd2436daf_frame_6.jpg"], "azimuth_angle": 0, "elevation_angle": 60, "rotation_reference_camera": 1, "camera_view": false}}
</tool_call>
```
> <span style="color:#3B82F6"><strong>Para. 16:</strong></span>
> ```text
> Assistant: <think>
> The top-down (azimuth=0°, elevation=60°) point cloud image gives a clear layout of the room, helping to assess distances from each object to the pillow. Here’s what is visible:
>     - The pillow is at the left side of the bed.
>     - The heater is positioned below the window, on the far wall relative to the pillow.
>     - The plant (green foliage in brown box) and chair are situated along the wall at the head of the bed, nearer to the pillow, with the plant directly above the pillow’s head-board.
>     - The ceiling light is overhead, but from top view it appears not particularly close horizontally.

> From the 3D view and 2D frames:
>     - Plant: Frame 6 shows the plant is immediately above or behind the headboard next to the pillow, with virtually no gap. In the point cloud, it is directly above the pillow’s closest edge.
>     - Chair: It is beside the plant, but spatially further—frames 2 and 6 confirm it is not as close as the plant and separated by a gap.
>     - Heater: Clearly further, at the opposite wall relative to pillow.
>     - Ceiling light: On the ceiling, not horizontally adjacent.

> The top-down point cloud confirms the plant is nearest to the pillow (measured from closest point of each object). I do not need another angle to make the determination.
> </think>
> <answer>
> (B) B. plant
> </answer>
> ```
> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span>
```text
Assistant: <think>
俯视（azimuth=0°, elevation=60°）点云图像清晰呈现了房间布局，有助于评估每个物体到枕头的距离。可以看到：
    - 枕头位于床的左侧。
    - 暖气位于窗户下方，相对于枕头处在远端墙壁上。
    - 植物（棕色盒子中的绿色枝叶）和椅子沿床头处的墙放置，离枕头较近，其中植物就在枕头床头板的正上方。
    - 顶灯在上方，但从俯视图看，它在水平方向上似乎并不特别近。

从 3D 视图和 2D 帧来看：
    - 植物：第 6 帧显示植物就在枕头旁的床头板正上方或后方，几乎没有间隙。在点云中，它就在枕头最近边缘的正上方。
    - 椅子：它在植物旁边，但空间上更远——第 2 和第 6 帧确认它不如植物近，且中间有间隙。
    - 暖气：显然更远，相对于枕头位于对面的墙上。
    - 顶灯：位于天花板上，水平方向上并不相邻。

俯视点云确认植物离枕头最近（从每个物体的最近点测量）。我不需要另一个角度即可作出判断。
</think>
<answer>
(B) B. 植物
</answer>
```

![Fig. 22: The VSI-Bench example.](3d%20agent/Think3D/assets/page_031_fig_fig_22.png)
**Caption:** Fig. 22: The VSI-Bench example.. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 22: The VSI-Bench example.。完整原文图注及可检索内容见下文对应条目。

*Fig. 22: The VSI-Bench example.*

*图 22：VSI-Bench 示例。*
> <span style="color:#3B82F6"><strong>Para. 17:</strong></span>
> **Question:**

> Measuring from the closest point of each object, which of these objects (heater, plant, chair, ceiling light) is the closest to the pillow?

> A. heater  B. plant

> C. chair  D. ceiling light
> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span>
**问题：**

从每个物体的最近点测量，以下物体（暖气、植物、椅子、顶灯）中哪一个离枕头最近？

A. 暖气  B. 植物

C. 椅子  D. 顶灯
> <span style="color:#3B82F6"><strong>Para. 18:</strong></span>
> ```text
> Assistant: <think>
> To answer the question, I need to:
> 1. Identify the window and the clock in the room.
> 2. Determine the position where a person would stand "by the window and facing the clock."
> 3. Locate the trash bin relative to this position and orientation.
> 4. Use the Cartesian quadrant analogy to determine if the trash bin is front-left, front-right, back-left, or back-right.

> From the images:
> - The window is visible in frames 0 and 1 (right side of the room, above the desk).
> - The clock is visible in frames 5 and 6 (on the wall above the desk area).
> - The trash bin is visible in frame 0 (under the desk with the computer, next to the blue chair).

> To confirm the spatial relationships, I will use a top-down (bird's-eye) view to see the layout of the room and the relative positions of the window, clock, and trash bin.
> </think>
> <tool_call>
> {"name": "pi3x_tool", "arguments": {"image_path": ["temp_frames/scannet_scene0378_01_frame_0.jpg", "temp_frames/scannet_scene0378_01_frame_1.jpg", "temp_frames/scannet_scene0378_01_frame_2.jpg", "temp_frames/scannet_scene0378_01_frame_3.jpg", "temp_frames/scannet_scene0378_01_frame_4.jpg", "temp_frames/scannet_scene0378_01_frame_5.jpg", "temp_frames/scannet_scene0378_01_frame_6.jpg"], "azimuth_angle": 0, "elevation_angle": 60, "rotation_reference_camera": 1, "camera_view": false}}
> </tool_call>
> ```
> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span>
```text
Assistant: <think>
为了回答这个问题，我需要：
1. 识别房间中的窗户和时钟。
2. 确定一个人“站在窗边并面向时钟”时的位置。
3. 确定垃圾桶相对于该位置和朝向的位置。
4. 使用笛卡尔象限类比来判断垃圾桶是在左前、右前、左后还是右后。

从图像来看：
- 窗户在第 0 和第 1 帧中可见（房间右侧，书桌上方）。
- 时钟在第 5 和第 6 帧中可见（书桌区域上方的墙上）。
- 垃圾桶在第 0 帧中可见（带电脑的书桌下方，蓝色椅子旁边）。

为了确认空间关系，我将使用俯视（鸟瞰）图来查看房间布局以及窗户、时钟和垃圾桶的相对位置。
</think>
<tool_call>
{"name": "pi3x_tool", "arguments": {"image_path": ["temp_frames/scannet_scene0378_01_frame_0.jpg", "temp_frames/scannet_scene0378_01_frame_1.jpg", "temp_frames/scannet_scene0378_01_frame_2.jpg", "temp_frames/scannet_scene0378_01_frame_3.jpg", "temp_frames/scannet_scene0378_01_frame_4.jpg", "temp_frames/scannet_scene0378_01_frame_5.jpg", "temp_frames/scannet_scene0378_01_frame_6.jpg"], "azimuth_angle": 0, "elevation_angle": 60, "rotation_reference_camera": 1, "camera_view": false}}
</tool_call>
```
> <span style="color:#3B82F6"><strong>Para. 19:</strong></span>
> ```text
> Assistant: <think>
> The top-down 3D reconstruction (azimuth=0°, elevation=60°) gives a clear layout of the room. The window is along the upper right wall, and the clock is on the wall above the desk area (visible in frames 5 and 6). The trash bin is under the desk with the computer, next to the blue chair (visible in frame 0).

> To answer the question, I need to confirm the spatial relationship from another angle, ideally from the left or right, to see the depth and relative positions more clearly. This will help verify if the trash bin is in front-left, front-right, back-left, or back-right when standing by the window and facing the clock.

> I will request a Pi3X visualization from the left side (azimuth = -90°, elevation = 45°) to better understand the spatial arrangement.
> </think>
> <tool_call>
> {"name": "pi3x_tool",
>   "arguments": {
>    "image_path": ["..."], "azimuth_angle": -90, "elevation_angle": 45, "rotation_reference_camera": 1, "camera_view": false}}
> </tool_call>
> ```
> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span>
```text
Assistant: <think>
俯视 3D 重建（azimuth=0°, elevation=60°）清晰呈现了房间布局。窗户位于右上方的墙上，时钟位于书桌区域上方的墙上（在第 5 和第 6 帧中可见）。垃圾桶位于带电脑的书桌下方、蓝色椅子旁边（在第 0 帧中可见）。

为了回答问题，我需要从另一个角度确认空间关系，最好从左侧或右侧观察，以更清楚地看到深度和相对位置。这将有助于验证当站在窗边并面向时钟时，垃圾桶是在左前、右前、左后还是右后。

我将请求从左侧进行 Pi3X 可视化（azimuth = -90°, elevation = 45°），以更好地理解空间排列。
</think>
<tool_call>
{"name": "pi3x_tool",
  "arguments": {
   "image_path": ["..."], "azimuth_angle": -90, "elevation_angle": 45, "rotation_reference_camera": 1, "camera_view": false}}
</tool_call>
```
> <span style="color:#3B82F6"><strong>Para. 20:</strong></span>
> ```text
> Assistant: <think>
> Let's synthesize the spatial information:
> - The window is visible in frames 0, 1, and 2, and is along the right wall in the top-down 3D reconstructions.
> - The clock is above the desk with the computer (frames 5, 6, and 0), and is on the wall opposite the window.
> - The trash bin is under the desk with the computer (frame 0), which is adjacent to the window.

> If you are standing by the window and facing the clock, you are facing away from the window toward the opposite wall. The desk with the computer (and the trash bin) is directly to your right, as seen in the 3D reconstructions (especially the azimuth = -90°, elevation = 45° view).

> In Cartesian terms:
> - Facing the clock (positive y-axis), the window is behind you.
> - The trash bin (under the computer desk) is to your right and slightly forward.

> Therefore, the trash bin is in the front-right quadrant relative to your position.
> </think>
> <answer>B. front-right</answer>
> ```
> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span>
```text
Assistant: <think>
让我们综合空间信息：
- 窗户在第 0、1 和 2 帧中可见，并且在俯视 3D 重建中位于右侧墙上。
- 时钟位于带电脑的书桌上方（第 5、6 和 0 帧），并且位于窗户对面的墙上。
- 垃圾桶位于带电脑的书桌下方（第 0 帧），该书桌与窗户相邻。

如果你站在窗边并面向时钟，你会背对窗户，朝向对面的墙。带电脑的书桌（以及垃圾桶）就在你的正右侧，如 3D 重建所示（尤其是 azimuth = -90°, elevation = 45° 视图）。

用笛卡尔坐标术语来说：
- 面向时钟（y 轴正方向）时，窗户在你身后。
- 垃圾桶（在电脑桌下）位于你的右侧并略微靠前。

因此，相对于你的位置，垃圾桶位于右前象限。
</think>
<answer>B. 右前</answer>
```

![Fig. 23: The VSI-Bench example.](3d%20agent/Think3D/assets/page_032_fig_fig_23.png)
**Caption:** Fig. 23: The VSI-Bench example.. See the complete source caption and searchable content associated with this item below.
**Caption[CN]:** Fig. 23: The VSI-Bench example.。完整原文图注及可检索内容见下文对应条目。

*Fig. 23: The VSI-Bench example.*

*图 23：VSI-Bench 示例。*

## References

The bibliography remains in its original language and wording for searchability.

1. Abdolmaleki, A., Abeyruwan, S., Ainslie, J., Alayrac, J.B., Arenas, M.G., Balakrishna, A., Batchelor, N., Bewley, A., Bingham, J., Bloesch, M., et al.: Gemini robotics 1.5: Pushing the frontier of generalist robots with advanced embodied reasoning, thinking, and motion transfer. arXiv preprint arXiv:2510.03342 (2025)
2. Achiam, J., Adler, S., Agarwal, S., Ahmad, L., Akkaya, I., Aleman, F.L., Almeida, D., Altenschmidt, J., Altman, S., Anadkat, S., et al.: Gpt-4 technical report. arXiv preprint arXiv:2303.08774 (2023)
3. Bai, S., Cai, Y., Chen, R., Chen, K., Chen, X., Cheng, Z., Deng, L., Ding, W., Gao, C., Ge, C., et al.: Qwen3-vl technical report. arXiv preprint arXiv:2511.21631 (2025)
4. Bai, S., Chen, K., Liu, X., Wang, J., Ge, W., Song, S., Dang, K., Wang, P., Wang, S., Tang, J., et al.: Qwen2. 5-vl technical report. arXiv preprint arXiv:2502.13923 (2025)
5. Balazadeh, V., Ataei, M., Cheong, H., Hosein Khasahmadi, A., Krishnan, R.G.: Synthetic vision: Training vision-language models to understand physics. arXiv e-prints pp. arXiv–2412 (2024)
6. Cai, W., Ponomarenko, I., Yuan, J., Li, X., Yang, W., Dong, H., Zhao, B.: Spatialbot: Precise spatial understanding with vision language models. In: 2025 IEEE International Conference on Robotics and Automation (ICRA). pp. 9490–9498. IEEE (2025)
7. Chen, B., Yue, Z., Chen, S., Wang, Z., Liu, Y., Li, P., Wang, Y.: Lvagent: Long video understanding by multi-round dynamical collaboration of mllm agents. arXiv preprint arXiv:2503.10200 (2025)
8. Chen, B., Xu, Z., Kirmani, S., Ichter, B., Sadigh, D., Guibas, L., Xia, F.: Spatialvlm: Endowing vision-language models with spatial reasoning capabilities. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 14455–14465 (2024)
9. Chen, Y., Shen, Y., Huang, W., Zhou, S., Lin, Q., Cai, X., Yu, Z., Bu, J., Shi, B., Qiao, Y.: Learning only with images: Visual reinforcement learning with reasoning, rendering, and visual feedback. arXiv preprint arXiv:2507.20766 (2025)
10. Chen, Z., Lu, X., Zheng, Z., Li, P., He, L., Zhou, Y., Shao, J., Zhuang, B., Sheng, L.: Geometrically-constrained agent for spatial reasoning. arXiv preprint arXiv:2511.22659 (2025)
11. Chen, Z., Zhang, M., Yu, X., Luo, X., Sun, M., Pan, Z., Feng, Y., Pei, P., Cai, X., Huang, R.: Think with 3d: Geometric imagination grounded spatial reasoning from limited views. arXiv preprint arXiv:2510.18632 (2025)
12. Cheng, A.C., Yin, H., Fu, Y., Guo, Q., Yang, R., Kautz, J., Wang, X., Liu, S.: Spatialrgpt: Grounded spatial reasoning in vision-language models. Advances in Neural Information Processing Systems 37, 135062–135093 (2024)
13. Chow, W., Mao, J., Li, B., Seita, D., Guizilini, V., Wang, Y.: Physbench: Benchmarking and enhancing vision-language models for physical world understanding. arXiv preprint arXiv:2501.16411 (2025)
14. Comanici, G., Bieber, E., Schaekermann, M., Pasupat, I., Sachdeva, N., Dhillon, I., Blistein, M., Ram, O., Zhang, D., Rosen, E., et al.: Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261 (2025)
15. Dong, G., Mao, H., Ma, K., Bao, L., Chen, Y., Wang, Z., Chen, Z., Du, J., Wang, H., Zhang, F., et al.: Agentic reinforced policy optimization. arXiv preprint arXiv:2507.19849 (2025)
16. Fan, Y., He, X., Yang, D., Zheng, K., Kuo, C.C., Zheng, Y., Narayanaraju, S.J., Guan, X., Wang, X.E.: Grit: Teaching mllms to think with images. arXiv preprint arXiv:2505.15879 (2025)
17. Fan, Z., Zhang, J., Li, R., Zhang, J., Chen, R., Hu, H., Wang, K., Qu, H., Wang, D., Yan, Z., et al.: Vlm-3r: Vision-language models augmented with instruction-aligned 3d reconstruction. arXiv preprint arXiv:2505.20279 (2025)
18. Feng, J., Zeng, J., Long, Q., Chen, H., Zhao, J., Xi, Y., Zhou, Z., Yuan, Y., Wang, S., Zeng, Q., et al.: A survey of large language model-powered spatial intelligence across scales: Advances in embodied agents, smart cities, and earth science. arXiv preprint arXiv:2504.09848 (2025)
19. Fu, X., Hu, Y., Li, B., Feng, Y., Wang, H., Lin, X., Roth, D., Smith, N.A., Ma, W.C., Krishna, R.: Blink: Multimodal large language models can see but not perceive. In: European Conference on Computer Vision. pp. 148–166. Springer (2024)
20. Han, Y., Chi, C., Zhou, E., Rong, S., An, J., Wang, P., Wang, Z., Sheng, L., Zhang, S.: Tiger: Tool-integrated geometric reasoning in vision-language models for robotics. arXiv preprint arXiv:2510.07181 (2025)
21. Hurst, A., Lerer, A., Goucher, A.P., Perelman, A., Ramesh, A., Clark, A., Ostrow, A., Welihinda, A., Hayes, A., Radford, A., et al.: Gpt-4o system card. arXiv preprint arXiv:2410.21276 (2024)
22. Ji, Y., Tan, H., Shi, J., Hao, X., Zhang, Y., Zhang, H., Wang, P., Zhao, M., Mu, Y., An, P., et al.: Robobrain: A unified brain model for robotic manipulation from abstract to concrete. In: Proceedings of the Computer Vision and Pattern Recognition Conference. pp. 1724–1734 (2025)
23. Keetha, N., Müller, N., Schönberger, J., Porzi, L., Zhang, Y., Fischer, T., Knapitsch, A., Zauss, D., Weber, E., Antunes, N., et al.: Mapanything: Universal feed-forward metric 3d reconstruction. arXiv preprint arXiv:2509.13414 (2025)
24. Lee, J., Choi, Y., Choi, H., Kim, H., Kim, S.: A training-free, task-agnostic framework for enhancing mllm performance on high-resolution images. arXiv preprint arXiv:2507.10202 (2025)
25. Lee, P.Y., Je, J., Park, C., Uy, M.A., Guibas, L., Sung, M.: Perspective-aware reasoning in vision-language models via mental imagery simulation. arXiv preprint arXiv:2504.17207 (2025)
26. Leroy, V., Cabon, Y., Revaud, J.: Grounding image matching in 3d with mast3r. In: European Conference on Computer Vision. pp. 71–91. Springer (2024)
27. Li, G., Hammoud, H., Itani, H., Khizbullin, D., Ghanem, B.: Camel: Communicative agents for" mind" exploration of large language model society. Advances in neural information processing systems 36, 51991–52008 (2023)
28. Lin, Y., Li, Y., Chen, D., Xu, W., Clark, R., Torr, P.: Olympus: A universal task router for computer vision tasks. In: Proceedings of the Computer Vision and Pattern Recognition Conference. pp. 14235–14246 (2025)
29. Liu, B., Dong, Y., Wang, Y., Ma, Z., Tang, Y., Tang, L., Rao, Y., Ma, W.C., Krishna, R.: Coarse correspondences boost spatial-temporal reasoning in multimodal language model. In: Proceedings of the Computer Vision and Pattern Recognition Conference. pp. 3783–3792 (2025)
30. Liu, J., Wang, H., Zhang, Y., Luo, X., Hu, J., Liu, Z., Xie, M.: Insightx agent: An lmm-based agentic framework with integrated tools for reliable x-ray ndt analysis. arXiv preprint arXiv:2507.14899 (2025)
31. Liu, S., Cheng, H., Liu, H., Zhang, H., Li, F., Ren, T., Zou, X., Yang, J., Su, H., Zhu, J., et al.: Llava-plus: Learning to use tools for creating multimodal agents. In: European conference on computer vision. pp. 126–142. Springer (2024)
32. Luo, Z., Zhang, C., Yong, S., Dai, C., Wang, Q., Ran, H., Shi, G., Sycara, K., Xie, Y.: pyspatial: Generating 3d visual programs for zero-shot spatial reasoning. In: The Fourteenth International Conference on Learning Representations (2026), https://openreview.net/forum?id=yv15C8ql24
33. Lyu, X., Liang, Y., Chen, W., Ding, M., Yang, J., Huang, G., Zhang, D., He, X., Shen, L.: Wsi-agents: A collaborative multi-agent system for multi-modal whole slide image analysis. arXiv preprint arXiv:2507.14680 (2025)
34. Madaan, A., et al.: Self-refine: Iterative refinement with self-feedback. NeurIPS (2023)
35. Majumdar, A., Ajay, A., Zhang, X., Putta, P., Yenamandra, S., Henaff, M., Silwal, S., Mcvay, P., Maksymets, O., Arnaud, S., et al.: Openeqa: Embodied question answering in the era of foundation models. In: Proceedings of the IEEE/CVF conference on computer vision and pattern recognition. pp. 16488–16498 (2024)
36. Marsili, D., Agrawal, R., Yue, Y., Gkioxari, G.: Visual agentic ai for spatial reasoning with a dynamic api. In: Proceedings of the Computer Vision and Pattern Recognition Conference. pp. 19446–19455 (2025)
37. OpenAI: Introducing gpt-4.1 in the api (2025), https://openai.com/index/gpt-4-1
38. QwenTeam: Qwen3-vl: Sharper vision, deeper thought, broader action (2025), https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef&from=research.latest-advancements-list
39. Roy, R., Das, D., Banerjee, A., Bhattacharjee, A., Dasgupta, K., Tripathi, S.: Bydeway: Boost your multimodal llm with depth prompting in a training-free way. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. pp. 6058–6064 (2025)
40. Schonberger, J.L., Frahm, J.M.: Structure-from-motion revisited. In: Proceedings of the IEEE conference on computer vision and pattern recognition. pp. 4104–4113 (2016)
41. Seed, B., Chen, J., Fan, T., Liu, X., Liu, L., Lin, Z., Wang, M., Wang, C., Wei, X., Xu, W., et al.: Seed1. 5-thinking: Advancing superb reasoning models with reinforcement learning. arXiv preprint arXiv:2504.13914 (2025)
42. Shao, H., Qian, S., Xiao, H., Song, G., Zong, Z., Wang, L., Liu, Y., Li, H.: Visual cot: Advancing multi-modal language models with a comprehensive dataset and benchmark for chain-of-thought reasoning. Advances in Neural Information Processing Systems 37, 8612–8642 (2024)
43. Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y., Wu, Y., et al.: Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300 (2024)
44. Shen, Y., Song, K., Tan, X., Li, D., Lu, W., Zhuang, Y.: Hugginggpt: Solving ai tasks with chatgpt and its friends in hugging face. Advances in Neural Information Processing Systems 36, 38154–38180 (2023)
45. Su, Z., Li, L., Song, M., Hao, Y., Yang, Z., Zhang, J., Chen, G., Gu, J., Li, J., Qu, X., et al.: Openthinkimg: Learning to think with images via visual tool reinforcement learning. arXiv preprint arXiv:2505.08617 (2025)
46. Su, Z., Xia, P., Guo, H., Liu, Z., Ma, Y., Qu, X., Liu, J., Li, Y., Zeng, K., Yang, Z., et al.: Thinking with images for multimodal reasoning: Foundations, methods, and future frontiers. arXiv preprint arXiv:2506.23918 (2025)
47. Surís, D., Menon, S., Vondrick, C.: Vipergpt: Visual inference via python execution for reasoning. In: Proceedings of the IEEE/CVF international conference on computer vision. pp. 11888–11898 (2023)
48. Taguchi, S., Deguchi, H., Hamazaki, T., Sakai, H.: Spatialprompting: Keyframe-driven zero-shot spatial reasoning with off-the-shelf multimodal large language models. arXiv preprint arXiv:2505.04911 (2025)
49. Tang, H., Cao, M., Liu, R., Liang, X., Li, L., Li, G., Liang, X.: Video spatial reasoning with object-centric 3d rollout. arXiv preprint arXiv:2511.13190 (2025)
50. Tang, Z., Wang, S., Cho, J., Yoo, J., Sun, C.: How can objects help video-language understanding? arXiv preprint arXiv:2504.07454 (2025)
51. Team, B.R., Cao, M., Tan, H., Ji, Y., Chen, X., Lin, M., Li, Z., Cao, Z., Wang, P., Zhou, E., et al.: Robobrain 2.0 technical report. arXiv preprint arXiv:2507.02029 (2025)
52. Team, G.R., Abeyruwan, S., Ainslie, J., Alayrac, J.B., Arenas, M.G., Armstrong, T., Balakrishna, A., Baruch, R., Bauza, M., Blokzijl, M., et al.: Gemini robotics: Bringing ai into the physical world. arXiv preprint arXiv:2503.20020 (2025)
53. Team, V., Hong, W., Yu, W., Gu, X., Wang, G., Gan, G., Tang, H., Cheng, J., Qi, J., Ji, J., et al.: Glm-4.5 v and glm-4.1 v-thinking: Towards versatile multimodal reasoning with scalable reinforcement learning, 2025. URL https://arxiv.org/abs/2507.01006
54. Wake, N., Kanehira, A., Sasabuchi, K., Takamatsu, J., Ikeuchi, K.: Gpt-4v (ision) for robotics: Multimodal task planning from human demonstration. IEEE Robotics and Automation Letters (2024)
55. Wang, C., Luo, W., Dong, S., Xuan, X., Li, Z., Ma, L., Gao, S.: Mllm-tool: A multimodal large language model for tool agent learning. In: 2025 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV). pp. 6678–6687. IEEE (2025)
56. Wang, J., Chen, M., Karaev, N., Vedaldi, A., Rupprecht, C., Novotny, D.: Vggt: Visual geometry grounded transformer. In: Proceedings of the Computer Vision and Pattern Recognition Conference. pp. 5294–5306 (2025)
57. Wang, Q., Zhang, Y., Holynski, A., Efros, A.A., Kanazawa, A.: Continuous 3d perception model with persistent state. In: Proceedings of the Computer Vision and Pattern Recognition Conference. pp. 10510–10522 (2025)
58. Wang, S., Leroy, V., Cabon, Y., Chidlovskii, B., Revaud, J.: Dust3r: Geometric 3d vision made easy. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 20697–20709 (2024)
59. Wang, Y., Zhou, J., Zhu, H., Chang, W., Zhou, Y., Li, Z., Chen, J., Pang, J., Shen, C., He, T.: pi3: Scalable permutation-equivariant visual geometry learning. arXiv e-prints pp. arXiv–2507 (2025)
60. Wang, Y., Wang, S., Cheng, Q., Fei, Z., Ding, L., Guo, Q., Tao, D., Qiu, X.: Visuothink: Empowering lvlm reasoning with multimodal tree search. arXiv preprint arXiv:2504.09130 (2025)
61. Wang, Z., Guo, X., Stoica, S., Xu, H., Wang, H., Ha, H., Chen, X., Chen, Y., Yan, M., Huang, F., et al.: Perception-aware policy optimization for multimodal reasoning. arXiv preprint arXiv:2507.06448 (2025)
62. Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., Le, Q.V., Zhou, D., et al.: Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing systems 35, 24824–24837 (2022)
63. Wu, C., Yin, S., Qi, W., Wang, X., Tang, Z., Duan, N.: Visual chatgpt: Talking, drawing and editing with visual foundation models. arXiv preprint arXiv:2303.04671 (2023)
64. Wu, D., Liu, F., Hung, Y.H., Duan, Y.: Spatial-mllm: Boosting mllm capabilities in visual-based spatial intelligence. arXiv preprint arXiv:2505.23747 (2025)
65. Wu, H., Huang, X., Chen, Y., Zhang, Y., Wang, Y., Xie, W.: Spatialscore: Towards unified evaluation for multimodal spatial understanding. arXiv preprint arXiv:2505.17012 (2025)
66. Wu, J., Guan, J., Feng, K., Liu, Q., Wu, S., Wang, L., Wu, W., Tan, T.: Reinforcing spatial reasoning in vision-language models with interwoven thinking and visual drawing. arXiv preprint arXiv:2506.09965 (2025)
67. Wu, M., Yang, J., Jiang, J., Li, M., Yan, K., Yu, H., Zhang, M., Zhai, C., Nahrstedt, K.: Vtool-r1: Vlms learn to think with images via reinforcement learning on multimodal tool use. arXiv preprint arXiv:2505.19255 (2025)
68. Wu, Y., Wang, Y., Tang, S., Wu, W., He, T., Ouyang, W., Torr, P., Wu, J.: Dettoolchain: A new prompting paradigm to unleash detection ability of mllm. In: European Conference on Computer Vision. pp. 164–182. Springer (2024)
69. Yang, J., Yang, S., Gupta, A.W., Han, R., Fei-Fei, L., Xie, S.: Thinking in space: How multimodal large language models see, remember, and recall spaces. In: Proceedings of the Computer Vision and Pattern Recognition Conference. pp. 10632–10643 (2025)
70. Yang, S., Li, J., Lai, X., Yu, B., Zhao, H., Jia, J.: Visionthink: Smart and efficient vision language model via reinforcement learning. arXiv preprint arXiv:2507.13348 (2025)
71. Yang, Y., Liu, J., Zhang, Z., Zhou, S., Tan, R., Yang, J., Du, Y., Gan, C.: Mindjourney: Test-time scaling with world models for spatial reasoning. arXiv preprint arXiv:2507.12508 (2025)
72. Yang, Z., Chen, D., Yu, X., Shen, M., Gan, C.: Vca: Video curious agent for long video understanding. In: Proceedings of the IEEE/CVF International Conference on Computer Vision. pp. 20168–20179 (2025)
73. Yang, Z., Li, L., Wang, J., Lin, K., Azarnasab, E., Ahmed, F., Liu, Z., Liu, C., Zeng, M., Wang, L.: Mm-react: Prompting chatgpt for multimodal reasoning and action. arXiv preprint arXiv:2303.11381 (2023)
74. Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K.R., Cao, Y.: React: Synergizing reasoning and acting in language models. In: The eleventh international conference on learning representations (2022)
75. Yin, B., Wang, Q., Zhang, P., Zhang, J., Wang, K., Wang, Z., Zhang, J., Chandrasegaran, K., Liu, H., Krishna, R., et al.: Spatial mental modeling from limited views. In: Structural Priors for Vision Workshop at ICCV’25 (2025)
76. Yu, S., Chen, Y., Ju, H., Jia, L., Zhang, F., Huang, S., Wu, Y., Cui, R., Ran, B., Zhang, Z., et al.: How far are vlms from visual spatial intelligence? a benchmark-driven perspective. arXiv preprint arXiv:2509.18905 (2025)
77. Yue, X., Ni, Y., Zhang, K., Zheng, T., Liu, R., Zhang, G., Stevens, S., Jiang, D., Ren, W., Sun, Y., et al.: Mmmu: A massive multi-discipline multimodal understanding and reasoning benchmark for expert agi. In: Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. pp. 9556–9567 (2024)
78. Zhang, H., Liu, M., Li, Z., Wen, H., Guan, W., Wang, Y., Nie, L.: Spatial understanding from videos: Structured prompts meet simulation data. arXiv preprint arXiv:2506.03642 (2025)
79. Zhang, X., Jia, Z., Guo, Z., Li, J., Li, B., Li, H., Lu, Y.: Deep video discovery: Agentic search with tool use for long-form video understanding. arXiv preprint arXiv:2505.18079 (2025)
80. Zhao, H., Liu, A., Zhang, Z., Wang, W., Chen, F., Zhu, R., Haffari, G., Zhuang, B.: Cov: Chain-of-view prompting for spatial reasoning. arXiv preprint arXiv:2601.05172 (2026)
81. Zhao, S., Zhang, H., Lin, S., Li, M., Wu, Q., Zhang, K., Wei, C.: Pyvision: Agentic vision with dynamic tooling. arXiv preprint arXiv:2507.07998 (2025)
82. Zhao, Y., Huang, J., Hu, J., Wang, X., Mao, Y., Zhang, D., Jiang, Z., Wu, Z., Ai, B., Wang, A., Zhou, W., Chen, Y.: Swift:a scalable lightweight infrastructure for fine-tuning (2024), https://arxiv.org/abs/2408.05517
83. Zheng, W., Mao, X., Ye, N., Li, P., Zhan, K., Lang, X., Zhao, H.: Driveagent-r1: Advancing vlm-based autonomous driving with hybrid thinking and active perception. arXiv e-prints pp. arXiv–2507 (2025)
84. Zheng, Z., Yang, M., Hong, J., Zhao, C., Xu, G., Yang, L., Shen, C., Yu, X.: Deepeyes: Incentivizing" thinking with images" via reinforcement learning. arXiv preprint arXiv:2505.14362 (2025)
85. Zhou, E., An, J., Chi, C., Han, Y., Rong, S., Zhang, C., Wang, P., Wang, Z., Huang, T., Sheng, L., et al.: Roborefer: Towards spatial referring with reasoning in vision-language models for robotics. arXiv preprint arXiv:2506.04308 (2025)
86. Zhou, E., Chi, C., Li, Y., An, J., Zhang, J., Rong, S., Han, Y., Ji, Y., Liu, M., Wang, P., et al.: Robotracer: Mastering spatial trace with reasoning in vision-language models for robotics. arXiv preprint arXiv:2512.13660 (2025)
87. Zhou, G., Hong, Y., Wu, Q.: Navgpt: Explicit reasoning in vision-and-language navigation with large language models. In: Proceedings of the AAAI Conference on Artificial Intelligence. vol. 38, pp. 7641–7649 (2024)
88. Zhou, Z., Chen, D., Ma, Z., Hu, Z., Fu, M., Wang, S., Wan, Y., Zhao, Z., Krishna, R.: Reinforced visual perception with tools. arXiv preprint arXiv:2509.01656 (2025)
89. Zhu, M., Tian, Y., Chen, H., Zhou, C., Guo, Q., Liu, Y., Yang, M., Shen, C.: Segagent: Exploring pixel understanding capabilities in mllms by imitating human annotator trajectories. In: Proceedings of the Computer Vision and Pattern Recognition Conference. pp. 3686–3696 (2025)
