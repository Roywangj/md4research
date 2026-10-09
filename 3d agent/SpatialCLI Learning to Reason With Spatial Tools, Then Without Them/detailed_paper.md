---
tags:
  - papers/3d-agent
  - papers/spatial-reasoning
  - papers/tool-use
aliases:
  - SpatialCLI
  - Learning to Reason With Spatial Tools
arxiv_id: 2607.27703
---

> <!-- Page 1 -->

> # SpatialCLI: Learning to Reason With Spatial Tools, Then Without Them

> Yang Zhou<sup>1,2,†</sup>, Zixuan Huang<sup>2,3,†</sup>, Sunzhu Li<sup>2</sup>, Zhuo Yang<sup>4</sup>, Chen Zhang<sup>1</sup>, Shunian Chen<sup>2,6</sup>, Caijun Yan<sup>1</sup>, Jianyao Xu<sup>2</sup>, Shunyu Liu<sup>1</sup>, Weijie Fu<sup>2</sup>, Peiliang Li<sup>2</sup>, Xiaozhi Chen<sup>2</sup>, Yuxiang Cai<sup>1,*</sup>

> <sup>1</sup>Zhejiang University, <sup>2</sup>Zhejiang University Technology, Shenzhen, China, <sup>3</sup>Beihang University  
> <sup>4</sup>University of Electronic Science and Technology of China, <sup>5</sup>Nanyang Technological University  
> <sup>6</sup>The Chinese University of Hong Kong, Shenzhen  
> <sup>†</sup>Equal contribution, <sup>*</sup>Corresponding author

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Vision-language models (VLMs) are increasingly used in embodied agents to interpret visual inputs, reason about spatial relationships, and make task-level decisions based on that reasoning. However, a fundamental capability mismatch remains: general VLMs can reason about the overall task but often miss the visual details that determine success, while specialist vision models can capture those details but cannot translate them into task-level decisions. In this work, we propose SpatialCLI, a framework that teaches VLMs to reason with spatial tools and progressively internalize the specialist perceptual capabilities they provide. SpatialCLI proceeds in three stages: (1) **Call** exposes specialist vision models as spatial tools to augment the VLM’s perception; (2) **Learn** uses Cold-Start SFT and agentic RL to improve tool use; and (3) **Internalize** verbalizes successful tool-use trajectories to internalize specialist perceptual capabilities. We further introduce SpatialCLI-Bench, a 516-example benchmark for compositional spatial reasoning across localization, segmentation, depth, and pose. On MindCube, SpatialCLI raises Qwen3-VL-8B-Instruct from 29.3% to 84.6% with tools, surpassing GPT-5.6 Sol with tools (72.1%), while retaining 73.8% without tools after internalization.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 视觉语言模型（VLM）正越来越多地用于具身智能体，以解释视觉输入、推理空间关系，并基于这些推理做出任务级决策。然而，当前仍存在一个根本性的能力不匹配：通用 VLM 能够推理整体任务，却经常忽略决定任务成功的视觉细节；而专业视觉模型能够捕捉这些细节，却无法将其转化为任务级决策。在本文中，我们提出 SpatialCLI，这是一个教会 VLM 使用空间工具进行推理，并逐步内化这些工具所提供的专业感知能力的框架。SpatialCLI 分为三个阶段：（1）**调用（Call）**将专业视觉模型作为空间工具，以增强 VLM 的感知能力；（2）**学习（Learn）**使用 Cold-Start SFT 和智能体强化学习来改进工具使用；（3）**内化（Internalize）**将成功的工具使用轨迹转换为文字，使模型内化专业感知能力。我们进一步提出 SpatialCLI-Bench，这是一个包含 516 个样例、覆盖定位、分割、深度和姿态的组合空间推理基准。在 MindCube 上，SpatialCLI 将 Qwen3-VL-8B-Instruct 的成绩从 29.3% 提升至使用工具时的 84.6%，超过了使用工具时 GPT-5.6 Sol 的 72.1%，同时在内化后不使用工具仍保留 73.8% 的成绩。

> **Date:** 2026.7.31  
> **Code:** https://github.com/IANNXANG/SpatialCLI  
> **Model:** https://huggingface.co/ZYT-MY/SpatialCLI-8B  
> **Dataset:** https://huggingface.co/datasets/ZYT-MY/SpatialCLI-Data  
> **Correspondence:** lmzhuhyang@zju.edu.cn, caijunyang@zju.edu.cn

> ## 1 Introduction

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> As physical AI moves into open-ended real-world environments, task success increasingly depends on composing multiple spatial perceptual capabilities on demand rather than improving any single capability in isolation [21, 63]. As shown in Figure 1, finding the farthest teddy bear requires first using segmentation to identify all candidate bears, then comparing their distances using depth information, and finally localizing the selected bear. Different real-world tasks require different combinations of spatial perceptual capabilities, requiring general physical intelligence to select and coordinate complementary capabilities according to the task objective.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 随着物理智能进入开放式现实世界环境，任务成功越来越依赖于按需组合多种空间感知能力，而不是孤立地提升某一种能力 [21, 63]。如图 1 所示，寻找最远的泰迪熊需要首先使用分割识别出所有候选泰迪熊，然后利用深度信息比较它们的距离，最后定位被选中的泰迪熊。不同的现实世界任务需要不同的空间感知能力组合，因此需要通用物理智能根据任务目标选择并协调互补能力。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> However, general VLMs and specialist vision models exhibit a fundamental capability mismatch under this requirement. General VLMs can interpret instructions, decompose tasks, and organize multi-step reasoning, but become unreliable when an answer hinges on precise localization, object boundaries, metric depth, or pose. Specialist vision models such as SAM 3 [4], DA3 [25], and VGGT [45] provide more reliable local perceptual evidence, but each primarily handles a specific perceptual operation and cannot understand which capabilities a task requires, compose outputs from multiple specialists, or translate those outputs into task-level decisions. Recent systems such as SpaceTools [7], AlloSpatial [37], and S-Agent [10] take important steps by organizing external tools and spatial priors into agentic reasoning processes and training VLMs on the resulting interactions. An open question is whether the perceptual evidence accumulated during tool interaction can be converted into supervision that enables VLMs to internalize specialist perceptual capabilities

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 然而，在这一要求下，通用 VLM 与专业视觉模型存在根本性的能力不匹配。通用 VLM 能够理解指令、分解任务并组织多步推理，但当答案依赖精确定位、目标边界、度量深度或姿态时，就会变得不可靠。SAM 3 [4]、DA3 [25] 和 VGGT [45] 等专业视觉模型能够提供更可靠的局部感知证据，但每个模型主要处理一种特定的感知操作，无法理解任务需要哪些能力、组合多个专业模型的输出，或将这些输出转化为任务级决策。SpaceTools [7]、AlloSpatial [37] 和 S-Agent [10] 等近期系统通过将外部工具和空间先验组织进智能体推理过程，并在由此产生的交互上训练 VLM，迈出了重要一步。一个尚未解决的问题是：在工具交互过程中积累的感知证据，能否转化为监督信号，使 VLM 能够内化专业感知能力

> <!-- Page 2 -->

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> capabilities and reason without invoking spatial tools. This would bring VLMs closer to becoming *foundation models native to the physical world.*

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 与空间工具无关地进行感知和推理。这将使 VLM 更接近于成为*原生面向物理世界的基础模型*。

> [Figure asset retained in assets/; see source map.]

**Caption:** Figure 1. A conceptual comparison of a general VLM with and without SpatialCLI Tools.

**Caption[CN]:** 图 1。 通用 VLM 在有无 SpatialCLI Tools 时的概念性比较。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> In this work, we introduce SpatialCLI, a three-stage framework that enables VLMs to reason with spatial tools and then internalize the specialist perceptual capabilities they provide: (1) **Call: Inference-Time Tool Augmentation.** The Call stage exposes specialist vision models for localization, segmentation, depth, and pose as spatial tools, augmenting the VLM’s perception with fine-grained visual evidence. (2) **Learn: Agentic Fine-Tuning.** The Learn stage uses Cold-Start SFT to establish basic tool-use behaviors and agentic RL to improve tool planning, response, and result utilization through task-level feedback. (3) **Internalize: Trajectory-Guided Capability Internalization.** SpatialCLI converts successful tool-use trajectories collected from SpatialCLI-RL into evidence-grounded perceptual reasoning chains, and then applies **Dual-View Capability Internalization** to train the final SpatialCLI model to internalize specialist perceptual capabilities while preserving its learned tool-use policy. Existing benchmarks predominantly evaluate spatial abilities in isolation, leaving it unclear whether models can coordinate multiple complementary capabilities to solve complex spatial problems. To address this evaluation gap, we construct SpatialCLI-Bench, a 516-example six-choice benchmark for compositional perceptual reasoning across localization, segmentation, depth, and pose. Our main contributions are summarized as follows:

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 在本文中，我们提出 SpatialCLI，这是一个使 VLM 能够使用空间工具进行推理，并进一步内化这些工具所提供的专业感知能力的三阶段框架：（1）**调用：推理时工具增强。** Call 阶段将用于定位、分割、深度和姿态的专业视觉模型作为空间工具，使 VLM 的感知获得细粒度视觉证据增强。（2）**学习：智能体微调。** Learn 阶段使用 Cold-Start SFT 建立基本的工具使用行为，并通过任务级反馈进行智能体强化学习，以改进工具规划、响应和结果利用。（3）**内化：轨迹引导的能力内化。** SpatialCLI 将从 SpatialCLI-RL 收集的成功工具使用轨迹转换为基于证据的感知推理链，然后应用**双视角能力内化**训练最终的 SpatialCLI 模型，使其在保留已学习工具使用策略的同时内化专业感知能力。现有基准主要孤立地评估空间能力，因此尚不清楚模型能否协调多种互补能力来解决复杂空间问题。为弥补这一评测空白，我们构建了 SpatialCLI-Bench，这是一个包含 516 个样例、每题六个选项的组合感知推理基准，覆盖定位、分割、深度和姿态。我们的主要贡献总结如下：

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> - We propose SpatialCLI, a *Call–Learn–Internalize* framework that equips VLMs with specialist vision models as spatial tools. Through agentic fine-tuning, SpatialCLI learns to coordinate these tools and turns successful tool-use trajectories into evidence-grounded supervision for internalizing specialist perceptual capabilities.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> - 我们提出 SpatialCLI，这是一个 *Call–Learn–Internalize（调用—学习—内化）*框架，将专业视觉模型作为空间工具赋予 VLM。通过智能体微调，SpatialCLI 学会协调这些工具，并将成功的工具使用轨迹转换为基于证据的监督信号，以内化专业感知能力。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> - We construct SpatialCLI-Bench, a 516-example benchmark that evaluates compositional perceptual reasoning across localization, segmentation, depth, and pose. The benchmark exposes a substantial limitation of current frontier models: GPT-5.6 Sol achieves only 48.8%.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> - 我们构建 SpatialCLI-Bench，这是一个包含 516 个样例、评估定位、分割、深度和姿态组合感知推理的基准。该基准揭示了当前前沿模型的一项显著局限：GPT-5.6 Sol 的成绩仅为 48.8%。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> - Extensive experiments show that SpatialCLI effectively improves both tool-enabled and tool-free reasoning. On SpatialCLI-Bench, SpatialCLI-8B reaches 91.3% with tools and 72.7% without tools, with consistent gains on other embodied and spatial benchmarks. These results show that external tool use and internalized direct reasoning can coexist in one model, providing a path toward *foundation models native to the physical world.*

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> - 大量实验表明，SpatialCLI 能够有效提升使用工具和不使用工具时的推理能力。在 SpatialCLI-Bench 上，SpatialCLI-8B 使用工具时达到 91.3%，不使用工具时达到 72.7%，并在其他具身和空间基准上取得一致提升。这些结果表明，外部工具使用与内化的直接推理能够在同一个模型中共存，为通向*原生面向物理世界的基础模型*提供了一条路径。

> ## 2 Related Work

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **Learning Spatial Capabilities in Vision-Language Models.** Embodied VLMs and VLAs acquire grounded visual-language knowledge through pretraining and robot demonstrations [21, 43, 63]. However, current multimodal models still struggle with spatial relations, viewpoint transformation, and 3D understanding [51, 54, 57]. SpatialVLM, SpatialGPT, and RoboRefer directly train spatial capabilities with spatial question answering, depth cues, 3D annotations, and task-specific supervision [5, 9, 62]. VLM3 further shows that standard VLM architectures can learn depth, pixel coordinates, camera pose, and object-level 3D understanding from text-based supervision and scaled data mixtures [3]. SpatialCLI follows a different route: the VLM

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **视觉语言模型中的空间能力学习。**具身 VLM 和视觉语言动作模型（VLA）通过预训练和机器人示范获得有依据的视觉语言知识 [21, 43, 63]。然而，当前的多模态模型在空间关系、视角变换和三维理解方面仍然存在困难 [51, 54, 57]。SpatialVLM、SpatialGPT 和 RoboRefer 通过空间问答、深度线索、三维标注和任务特定监督，直接训练空间能力 [5, 9, 62]。VLM3 进一步表明，标准 VLM 架构能够通过基于文本的监督和扩展的数据混合学习深度、像素坐标、相机姿态和目标级三维理解 [3]。SpatialCLI 采取了不同的路径：VLM

> <!-- Page 3 -->

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> invokes external specialist perception tools, then learns direct reasoning from supervision derived from its own successful tool-use trajectories.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 调用外部专业感知工具，然后从其自身成功的工具使用轨迹所产生的监督中学习直接推理。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> **Tool-Augmented Agents and Spatial Reasoning.** Building on advances in LLM reasoning [13, 19, 48], agents can plan, interact with environments, and invoke tools [14, 38, 40, 42, 56], enabling applications in search and information seeking [20, 29, 32], coding [52, 59], and GUI interaction [34, 61]. In robotics, hierarchical agents use VLMs as high-level planners and VLAs as low-level executors [6, 17, 24, 55, 60], but their reliability remains constrained by the spatial perception of the VLM planner. Spatial reasoning systems use 3D priors or constraints [8, 31], geometric computation or multi-tool coordination [7, 15], and egocentric representations or spatiotemporal evidence [10, 37]. SpatialCLI not only learns to use multiple specialist perception tools through interaction, but also transforms the VLM’s own successful tool-use trajectories into supervision for direct reasoning, enabling reasoning both with external tools and directly without them.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> **工具增强智能体与空间推理。**基于大语言模型推理方面的进展 [13, 19, 48]，智能体能够进行规划、与环境交互并调用工具 [14, 38, 40, 42, 56]，从而支持搜索和信息获取 [20, 29, 32]、代码编写 [52, 59] 以及图形用户界面交互 [34, 61] 等应用。在机器人领域，分层智能体使用 VLM 作为高级规划器、使用 VLA 作为低级执行器 [6, 17, 24, 55, 60]，但其可靠性仍受 VLM 规划器空间感知能力的限制。空间推理系统使用三维先验或约束 [8, 31]、几何计算或多工具协调 [7, 15]，以及自我中心表示或时空证据 [10, 37]。SpatialCLI 不仅通过交互学习使用多个专业感知工具，还将 VLM 自身成功的工具使用轨迹转换为直接推理的监督信号，使模型能够既借助外部工具推理，也能够直接在不使用工具时推理。

> ## 3 Method

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> SpatialCLI aims to turn external specialist perceptual capabilities into abilities that VLMs can **call, learn, and internalize**. As shown in Figure 2, it proceeds in three stages. (1) *inference-time tool augmentation* equips VLMs with specialist vision models as spatial tools. (2) *agentic fine-tuning* fine-tunes the model to learn effective tool-use policies. (3) *trajectory-guided capability internalization* verbalizes tool-use trajectories to internalize specialist perceptual capabilities while preserving tool-use ability. The complete end-to-end procedure is summarized in Algorithm 1 of Appendix A. In the following, we first introduce the three stages of SpatialCLI and then describe the construction of SpatialCLI-Bench.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> SpatialCLI 旨在将外部专业感知能力转化为 VLM 能够**调用、学习和内化**的能力。如图 2 所示，该过程分为三个阶段。（1）*推理时工具增强*将专业视觉模型作为空间工具赋予 VLM。（2）*智能体微调*对模型进行微调，使其学习有效的工具使用策略。（3）*轨迹引导的能力内化*将工具使用轨迹转换为文字，使模型在保留工具使用能力的同时内化专业感知能力。完整的端到端过程总结于附录 A 的算法 1 中。下文首先介绍 SpatialCLI 的三个阶段，然后描述 SpatialCLI-Bench 的构建过程。

> ### 3.1 Inference-Time Tool Augmentation

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> Neither VLMs nor specialist vision models can independently solve complex embodied tasks, but they offer complementary strengths. (1) VLMs excel at semantic understanding and task-level reasoning, but remain unreliable for fine-grained localization, segmentation, depth, and pose perception. (2) Specialist vision models provide precise perceptual outputs, but lack the task-level understanding needed to determine when they should be invoked or how their outputs should be combined.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> VLM 和专业视觉模型都无法独立解决复杂的具身任务，但二者具有互补优势。（1）VLM 擅长语义理解和任务级推理，但在细粒度定位、分割、深度和姿态感知方面仍不可靠。（2）专业视觉模型能够提供精确的感知输出，但缺乏判断何时调用这些模型以及如何组合其输出所需的任务级理解。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> To combine these complementary strengths, SpatialCLI builds an inference-time tool-augmented agent framework that equips the VLM with specialist vision models as spatial tools. Within this framework, the VLM understands the task, selects tools, composes evidence, and completes reasoning, while specialist vision models provide reliable local perceptual evidence. Following ReAct [56], at each interaction step, the VLM first reasons internally and then either produces a final answer or makes a tool call. When the VLM makes a tool call, SpatialCLI executes the corresponding spatial tool and returns the tool result to the VLM. The

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> 为了结合这些互补优势，SpatialCLI 构建了一个推理时工具增强的智能体框架，将专业视觉模型作为空间工具赋予 VLM。在该框架中，VLM 理解任务、选择工具、组合证据并完成推理，而专业视觉模型提供可靠的局部感知证据。遵循 ReAct [56]，在每一步交互中，VLM 首先进行内部推理，然后生成最终答案或发出工具调用。当 VLM 发出工具调用时，SpatialCLI 执行相应的空间工具，并将工具结果返回给 VLM。该

> <!-- Page 4 -->

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> VLM then continues reasoning with the updated interaction history until it produces a final answer or exhausts the tool-call budget. Following budget-aware tool use agents [30], SpatialCLI exposes the remaining tool-call budget after each tool response, allowing the VLM to decide whether to gather additional evidence or terminate the interaction. We observe that discarding reasoning content across interaction turns causes redundant reasoning and token inefficiency [26]; we therefore retain the VLM’s reasoning throughout the entire interaction.

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> VLM 随后基于更新后的交互历史继续推理，直到生成最终答案或耗尽工具调用预算。遵循预算感知工具使用智能体 [30] 的做法，SpatialCLI 在每次工具响应后公开剩余的工具调用预算，使 VLM 能够决定是收集更多证据还是终止交互。我们观察到，在交互轮次之间丢弃推理内容会导致重复推理和 token 使用效率低下 [26]；因此，我们保留 VLM 在整个交互过程中的推理内容。

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> SpatialCLI provides four spatial tools. (1) **Locate**, backed by Locate Anything [46] and Grounding DINO [28], takes a language query and returns object bounding boxes. (2) **Segment**, backed by SAM 3 [4], takes a language query and returns polygonal object boundaries. (3) **Depth**, backed by Depth Anything 3 [25], takes queried image points and returns metric depth. (4) **Pose**, backed by Orient Anything V2 [47] and VGGT [45], takes an object or camera-motion query and returns object orientation or cross-view camera motion. The complete interfaces and registrations are provided in Appendix D.2 and Boxes D.1–D.4, while the shared agentic tool-use prompt is shown in Box G.1. SpatialCLI records the returned tool calls, returned results, and final answer. We represent the executed tool-interaction trace and the corresponding complete interaction sample as

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> SpatialCLI 提供四种空间工具。（1）**Locate** 由 Locate Anything [46] 和 Grounding DINO [28] 支持，接收语言查询并返回目标边界框。（2）**Segment** 由 SAM 3 [4] 支持，接收语言查询并返回多边形目标边界。（3）**Depth** 由 Depth Anything 3 [25] 支持，接收查询的图像点并返回度量深度。（4）**Pose** 由 Orient Anything V2 [47] 和 VGGT [45] 支持，接收目标或相机运动查询，并返回目标方向或跨视角相机运动。完整的接口和注册方式见附录 D.2 以及框 D.1–D.4，共享的智能体工具使用提示词见框 G.1。SpatialCLI 记录工具调用、工具返回结果和最终答案。我们将执行的工具交互轨迹以及相应的完整交互样例表示为

> $\tau = ((z_t, a_t, o_t)_{t=1}^{T}), \qquad \xi = (I, q, \tau, y),$

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> where $z_t$ is the reasoning preceding the $t$-th executed tool call, $a_t$ is that tool call, $o_t$ is its returned result, $T$ is the number of executed tool calls, and $y$ is the final answer produced after the trace.

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> 其中，$z_t$ 是第 $t$ 次已执行工具调用之前的推理，$a_t$ 是该工具调用，$o_t$ 是其返回结果，$T$ 是已执行工具调用的数量，$y$ 是轨迹之后生成的最终答案。

> ### 3.2 Agentic Fine-Tuning

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> Within this agent framework, the VLM can interact with spatial tools to produce complete interaction trajectories, but it cannot reliably determine when to use which tool, how to specify appropriate arguments, or how to use the returned results to guide subsequent reasoning. Directly applying multi-turn tool RL to the initial model requires exploration over a large hybrid action space, where the model is prone to several failure patterns: incorrect tool-call formats, invalid arguments, unnecessary repeated calls, and ignoring tool results when they conflict with its prior beliefs. SpatialCLI therefore first uses Cold-Start SFT to establish basic tool-interaction behaviors and then applies agentic RL to improve tool-use planning, argument generation, result utilization, and termination through task-level feedback.

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> 在该智能体框架中，VLM 能够与空间工具交互并生成完整的交互轨迹，但无法可靠地判断何时使用哪种工具、如何指定合适的参数，或如何利用返回结果指导后续推理。直接对初始模型应用多轮工具强化学习，需要在庞大的混合动作空间中进行探索，此时模型容易出现多种失败模式：工具调用格式错误、参数无效、不必要的重复调用，以及当工具结果与先前信念冲突时忽略工具结果。因此，SpatialCLI 首先使用 Cold-Start SFT 建立基本的工具交互行为，然后应用智能体强化学习，通过任务级反馈改进工具使用规划、参数生成、结果利用和终止决策。

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> **Cold-Start SFT.** Effective RL exploration requires an initial policy capable of selecting appropriate tools and specifying valid arguments. SpatialCLI therefore uses Qwen3.5-397B-A17B [35] as the teacher model, equips it with the inference-time agent framework, and records the complete multi-turn trajectories it produces while solving the training tasks. As illustrated by the cases in Appendix H, these trajectories provide reusable reasoning and common tool-use patterns, such as planning before execution. We discard samples with invalid tool-call formats, failed tool execution, or incorrect final answers, yielding the SFT dataset $\mathcal{D}_{\mathrm{SFT}}$. During training, returned tool results serve only as context for subsequent generation, while the loss is computed over model-generated reasoning, tool calls, and final-answer tokens. This stage transfers these patterns to the initial model and yields the SpatialCLI-SFT checkpoint $\pi_{\mathrm{SFT}}$ for RL.

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> **Cold-Start SFT[CN]。** 有效的强化学习探索需要一个能够选择合适工具并指定有效参数的初始策略。因此，SpatialCLI 使用 Qwen3.5-397B-A17B [35] 作为教师模型，为其配备推理时智能体框架，并记录它在解决训练任务时产生的完整多轮轨迹。如附录 H 的案例所示，这些轨迹提供了可复用的推理和常见工具使用模式，例如执行前进行规划。我们丢弃工具调用格式无效、工具执行失败或最终答案错误的样例，得到 SFT 数据集 $\mathcal{D}_{\mathrm{SFT}}$。训练期间，工具返回结果仅作为后续生成的上下文，而损失则在模型生成的推理、工具调用和最终答案 token 上计算。该阶段将这些模式迁移到初始模型，并得到用于强化学习的 SpatialCLI-SFT 检查点 $\pi_{\mathrm{SFT}}$。

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> **Agentic RL.** SFT can only imitate filtered teacher trajectories and cannot use task outcomes to improve tool-use decisions beyond the demonstrations. Starting from the SpatialCLI-SFT checkpoint $\pi_{\mathrm{SFT}}$, the model follows the same interaction loop as inference-time tool augmentation during rollout, with tool results dynamically appended to the interaction history to guide subsequent decisions. For each task $x = (I, q, y^*) \sim \mathcal{D}_{\mathrm{RL}}$, GRPO [39] samples a group of $G$ complete interactions $\{\xi_i\}_{i=1}^{G}$ from the old policy $\pi_{\mathrm{old}}$. Each interaction receives an outcome reward $R_i = V(y_i, y^*)$ based on its final answer. Optimizing these rewards yields the SpatialCLI-RL checkpoint $\pi_{\mathrm{RL}}$; the complete objective and training configuration are provided in Appendix B.1.

> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> **Agentic RL[CN]。** SFT 只能模仿经过筛选的教师轨迹，无法利用任务结果超越示范来改进工具使用决策。从 SpatialCLI-SFT 检查点 $\pi_{\mathrm{SFT}}$ 出发，模型在 rollout 期间遵循与推理时工具增强相同的交互循环，并将工具结果动态追加到交互历史中，以指导后续决策。对于每个任务 $x = (I, q, y^*) \sim \mathcal{D}_{\mathrm{RL}}$，GRPO [39] 从旧策略 $\pi_{\mathrm{old}}$ 中采样一组包含 $G$ 个完整交互的样本 $\{\xi_i\}_{i=1}^{G}$。每个交互根据其最终答案获得结果奖励 $R_i = V(y_i, y^*)$。优化这些奖励得到 SpatialCLI-RL 检查点 $\pi_{\mathrm{RL}}$；完整目标函数和训练配置见附录 B.1。

> ### 3.3 Trajectory-Guided Capability Internalization

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> Moving toward foundation models native to the physical world requires perceptual capabilities to reside in the model itself rather than depending entirely on external tools. Inspired by learning from visual-program

> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> 要迈向原生面向物理世界的基础模型，需要让感知能力存在于模型自身，而不是完全依赖外部工具。受从视觉程序

> <!-- Page 5 -->

> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> execution traces [18], SpatialCLI therefore uses successful SpatialCLI-RL trajectories as the source of supervision for internalizing the specialist perceptual capabilities supplied by spatial tools while preserving the learned tool-use policy. This process consists of two steps: (1) **Progressive Evidence-Grounded Trajectory Verbalization** converts successful tool-use trajectories into explicit perceptual reasoning chains, and (2) **Dual-View Capability Internalization** jointly trains on capability-internalization and tool-use views to internalize specialist perceptual capabilities without sacrificing tool use.

> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> 执行轨迹 [18] 的启发，SpatialCLI 使用成功的 SpatialCLI-RL 轨迹作为监督来源，在保留已学习工具使用策略的同时，内化空间工具所提供的专业感知能力。该过程包含两个步骤：（1）**渐进式基于证据的轨迹文字化**将成功的工具使用轨迹转换为显式的感知推理链；（2）**双视角能力内化**联合训练能力内化视角和工具使用视角，在不牺牲工具使用能力的情况下内化专业感知能力。

> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> **Progressive Evidence-Grounded Trajectory Verbalization.** Raw SpatialCLI-RL trajectories contain lengthy model reasoning, tool-call syntax, heterogeneous tool returns, and repeated interaction history, making them unsuitable as direct natural-language supervision. Verbalizing an entire trajectory in a single pass requires processing a long context and can obscure dependencies between evidence collected across turns. SpatialCLI therefore processes each successful trajectory ($y = y^*$) in two successive steps. (1) **Turn-wise evidence consolidation.** To preserve cross-turn dependencies without repeatedly processing the full raw history, SpatialCLI consolidates the newly collected evidence after each tool interaction. Let $e_t$ denote the resulting evidence-reasoning unit at turn $t$, and let $e_{<t} = (e_1, \ldots, e_{t-1})$, with $e_{<1} = \varnothing$. The extractor combines the visual input and task instruction with the previously consolidated units and the current interaction:

> <span style="color:#F59E0B"><strong>Para. 23[CN]:</strong></span> **渐进式基于证据的轨迹文字化。**原始 SpatialCLI-RL 轨迹包含冗长的模型推理、工具调用语法、异构工具返回结果以及重复的交互历史，因此不适合作为直接的自然语言监督。一次性将整个轨迹转换为文字需要处理很长的上下文，并且可能模糊不同轮次所收集证据之间的依赖关系。因此，SpatialCLI 对每条成功轨迹（$y = y^*$）分两个连续步骤进行处理。（1）**逐轮证据整合。**为了在不重复处理完整原始历史的情况下保留跨轮次依赖，SpatialCLI 在每次工具交互之后整合新收集的证据。令 $e_t$ 表示第 $t$ 轮得到的证据—推理单元，并令 $e_{<t} = (e_1, \ldots, e_{t-1})$，其中 $e_{<1} = \varnothing$。提取器将视觉输入和任务指令、此前整合的单元以及当前交互结合起来：

> $e_t = \Psi_{\mathrm{ext}}(I,q,e_{<t},z_t,a_t,o_t), \qquad t=1,\ldots,T.$

> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> Each $e_t$ exhaustively verbalizes the current tool result, preserves explicit visual observations from $z_t$, and records how they update the accumulated evidence without repeating unchanged content. Any perceptual statement must be traceable to the current tool result, an explicit visual observation in $z_t$, or a previous unit; the correct answer $y^*$ is withheld to prevent answer-conditioned evidence reconstruction. (2) **Global trajectory verbalization.** To integrate evidence distributed across turns into a coherent task-level reasoning chain, SpatialCLI passes the visual input, task instruction, consolidated evidence trajectory $E_T = (e_1,\ldots,e_T)$, and correct answer to a global verbalizer:

> <span style="color:#F59E0B"><strong>Para. 24[CN]:</strong></span> 每个 $e_t$ 都详尽地将当前工具结果转换为文字，保留 $z_t$ 中明确的视觉观察，并记录这些观察如何更新累积证据，同时不重复未改变的内容。任何感知陈述都必须能够追溯到当前工具结果、$z_t$ 中明确的视觉观察或先前的单元；正确答案 $y^*$ 被隐藏，以避免基于答案重建证据。（2）**全局轨迹文字化。**为了将分布在不同轮次的证据整合为连贯的任务级推理链，SpatialCLI 将视觉输入、任务指令、整合后的证据轨迹 $E_T = (e_1,\ldots,e_T)$ 以及正确答案传递给全局文字化器：

> $c = \Phi_{\mathrm{verbal}}(I,q,E_T,y^*).$

> <span style="color:#3B82F6"><strong>Para. 25:</strong></span> The verbalizer removes redundancy and organizes the dependencies from perceptual observations to the correct answer into a concise reasoning chain $c$, without introducing entities, attributes, values, or relations absent from $E_T$. The complete turn-wise consolidation and global verbalization prompts are provided in Appendix G, Boxes G.2 and G.3.

> <span style="color:#F59E0B"><strong>Para. 25[CN]:</strong></span> 文字化器去除冗余，并将从感知观察到正确答案的依赖关系组织成简洁的推理链 $c$，且不引入 $E_T$ 中不存在的实体、属性、数值或关系。完整的逐轮整合和全局文字化提示词见附录 G 的框 G.2 和 G.3。

> <span style="color:#3B82F6"><strong>Para. 26:</strong></span> **Dual-View Capability Internalization.** To internalize specialist perceptual capabilities while preserving the model’s learned tool-use policy, SpatialCLI constructs two training views from each successful trajectory. (1) The **Capability-Internalization View** uses a direct-answer prompt and forms each training sample from the image, task instruction, explicit perceptual reasoning chain, and final answer. The model learns to generate the reasoning chain and answer without accessing external tools, thereby internalizing the specialist perceptual capabilities originally supplied by spatial tools. (2) The **Tool-Use View** uses a prompt containing tool descriptions and preserves the original interaction structure, with the returned tool results serving as context for subsequent generation. Training supervises model-generated reasoning, tool calls, and final-answer tokens, preserving the model’s ability to decide when to invoke tools and how to use returned results. The two views are jointly optimized as:

> <span style="color:#F59E0B"><strong>Para. 26[CN]:</strong></span> 为了在保留模型已学习工具使用策略的同时内化专业感知能力，SpatialCLI 从每条成功轨迹中构造两个训练视角。（1）**能力内化视角**使用直接回答提示词，并将图像、任务指令、显式感知推理链和最终答案构成每个训练样本。模型学习生成推理链和答案，而无需访问外部工具，从而内化原本由空间工具提供的专业感知能力。（2）**工具使用视角**使用包含工具描述的提示词，并保留原始交互结构，将工具返回结果作为后续生成的上下文。训练监督模型生成的推理、工具调用和最终答案 token，保留模型决定何时调用工具以及如何使用返回结果的能力。两个视角联合优化为：

> $\mathcal{L}_{\mathrm{CI}} = \mathcal{L}_{\mathrm{internal}} + \lambda \mathcal{L}_{\mathrm{agentic}}.$

> <span style="color:#3B82F6"><strong>Para. 27:</strong></span> Here, $\mathcal{L}_{\mathrm{internal}}$ supervises tool-free explicit perceptual reasoning and the final answer, while $\mathcal{L}_{\mathrm{agentic}}$ supervises model-generated tokens in the tool-interaction trajectory. Both terms are mean negative log-likelihoods over their respective supervised tokens, and $\lambda$ controls the relative weight of the Tool-Use View.

> <span style="color:#F59E0B"><strong>Para. 27[CN]:</strong></span> 其中，$\mathcal{L}_{\mathrm{internal}}$ 监督不使用工具时的显式感知推理和最终答案，而 $\mathcal{L}_{\mathrm{agentic}}$ 监督工具交互轨迹中模型生成的 token。两项均是在各自受监督 token 上计算的平均负对数似然，$\lambda$ 控制工具使用视角的相对权重。

> ### 3.4 SpatialCLI-Bench Construction

> <span style="color:#3B82F6"><strong>Para. 28:</strong></span> Existing benchmarks predominantly evaluate spatial capabilities in isolation, making it difficult to assess whether models can coordinate multiple perceptual capabilities. We therefore construct SpatialCLI-Bench, a 516-example English six-choice visual question answering benchmark for compositional reasoning across localization, segmentation, depth, and pose.

> <span style="color:#F59E0B"><strong>Para. 28[CN]:</strong></span> 现有基准主要孤立地评估空间能力，因此难以判断模型是否能够协调多种感知能力。为此，我们构建 SpatialCLI-Bench，这是一个包含 516 个样例、每题六个选项的英文视觉问答基准，用于评估跨定位、分割、深度和姿态的组合推理。

> <!-- Page 6 -->

> ## Table 1. Overall performance on embodied and spatial benchmarks

> Scores in model-name rows are obtained under inference w/o Tools, while + rows are obtained under inference w/ the indicated tools. Arrows denote score changes from the corresponding base model w/o Tools. Avg. macro-averages benchmarks after first averaging subsets within each benchmark. The best result in each column is highlighted in **bold**.

> | Model | SpatialCLI Bench | MindCube | MMSI Motion-Cam | MMSI Pos-Cam | MMSI Cam-Cam | DA-2K | BOPASK Traj. | BOPASK ObjRrr | Avg. |
> |---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
> | **Frontier Models** |  |  |  |  |  |  |  |  |  |
> | GPT-5.6 Sol | 48.8 | 70.3 | 52.7 | 62.4 | 79.2 | 51.5 | **56.4** | 62.0 |  |
> | + SpatialCLI Tools | 72.9 (+24.1) | 72.1 (+1.8) | 54.1 (+1.4) | 62.4 (0.0) | 86.1 (+6.9) | 52.8 (+1.3) | 49.5 (−6.9) | 68.1 (+6.1) |  |
> | Gemini 3.1 Pro | 52.9 | 74.2 | 59.5 | 51.6 | 86.7 | 48.6 | 54.2 | 65.4 |  |
> | Qwen3.7-Plus | 43.8 | 62.8 | 43.2 | 45.2 | 76.3 | **61.3** | 42.4 | 55.8 |  |
> | Qwen3.5-397B-A17B | 40.9 | 49.3 | 43.2 | 46.2 | 70.3 | 56.4 | 31.0 | 49.8 |  |
> | + SpatialCLI Tools | 79.8 (+39.0) | 67.6 (+18.3) | 46.0 (+2.8) | 54.8 (+8.6) | 91.9 (+21.6) | 57.7 (+1.3) | 44.7 (+13.7) | 68.2 (+18.4) |  |
> | **Our Models** |  |  |  |  |  |  |  |  |  |
> | Qwen3.6-27B | 46.3 | 56.6 | 40.5 | 40.9 | 75.0 | 50.9 | 36.8 | 52.5 |  |
> | + SpatialCLI Tools | 82.2 (+35.9) | 62.4 (+5.8) | 51.4 (+10.9) | 46.2 (+5.3) | 91.5 (+16.5) | 60.6 (+9.7) | 50.6 (+13.8) | 68.1 (+15.6) |  |
> | SpatialCLI-27B | 76.3 (+30.0) | 80.4 (+23.8) | 41.9 (+1.4) | 43.0 (+2.1) | 85.5 (+10.5) | 57.3 (+6.4) | 53.1 (+16.3) | 68.0 (+15.5) |  |
> | + SpatialCLI Tools | 91.7 (+45.4) | 85.5 (+28.9) | 52.7 (+12.2) | 53.8 (+12.9) | 91.9 (+16.9) | 58.2 (+17.3) | 55.6 (+18.8) | 75.9 (+23.4) |  |
> | Qwen3.6-35B-A3B | 44.4 | 54.2 | 36.5 | 44.1 | 71.9 | 52.3 | 39.2 | 51.3 |  |
> | + SpatialCLI Tools | 80.2 (+35.8) | 63.3 (+9.1) | 48.7 (+12.2) | 45.2 (+1.1) | 93.9 (+19.4) | 58.5 (+6.2) | 45.3 (+5.4) | 66.6 (+15.2) |  |
> | SpatialCLI-35B-A3B | 75.0 (+30.6) | 78.8 (+24.6) | 43.2 (+6.7) | 46.2 (+2.1) | 83.9 (+12.0) | 57.6 (+5.3) | 54.7 (+15.5) | 67.7 (+16.4) |  |
> | + SpatialCLI Tools | 91.9 (+47.5) | 85.6 (+31.4) | 50.0 (+13.5) | 53.8 (+17.9) | 91.8 (+19.9) | 57.9 (+5.6) | 53.7 (+14.5) | 75.4 (+24.1) |  |
> | Qwen3-VL-8B-Instruct | 35.3 | 29.3 | 27.0 | 25.8 | 68.1 | 25.8 | 13.3 | 35.7 |  |
> | + AlloSpatial Tools | 43.2 (+7.9) | 35.2 (+5.9) | 24.3 (−2.7) | 35.5 (+9.7) | 47.4 (−20.7) | 25.9 (+0.1) | 9.7 (−3.6) | 34.7 (−1.0) |  |
> | + SpaceTools | 39.3 (+4.0) | 30.5 (+1.2) | 21.6 (−5.4) | 20.4 (−5.4) | 95.9 (+27.8) | 44.0 (+18.2) | 22.3 (+9.0) | 44.0 (+8.2) |  |
> | + SpatialCLI Tools | 66.5 (+31.2) | 47.2 (+17.9) | 41.9 (+14.9) | 39.8 (+14.0) | 81.6 (+23.5) | 54.3 (+28.5) | 20.6 (+7.3) | 56.7 (+21.0) |  |
> | SpatialCLI-8B | 72.7 (+37.4) | 73.8 (+44.5) | 35.1 (+8.1) | 32.3 (+6.5) | 84.0 (+15.9) | 56.8 (+28.8) | 53.2 (+39.9) | 62.9 (+27.2) |  |
> | + SpatialCLI Tools | **91.3 (+56.0)** | **84.6 (+55.3)** | 39.2 (+12.2) | **53.8 (+28.0)** | 91.8 (+23.7) | 55.2 (+29.4) | 48.5 (+35.2) | 73.2 (+37.5) |  |

> **表 1[CN]。具身和空间基准上的总体性能。**模型名称行的得分是在不使用工具的推理条件下获得的，而带有 “+” 的行是在使用所指示工具的推理条件下获得的。箭头表示相对于对应的不使用工具的基础模型的得分变化。Avg. 是先对每个基准内部的子集求平均，再对基准进行宏平均。每列最佳结果以**粗体**突出显示。

> <span style="color:#3B82F6"><strong>Para. 29:</strong></span> The construction follows four stages: (1) Gemini 3.1 Pro [11] inventories reliable entities and scene relations; (2) specialist vision models provide localization, segmentation, metric-depth, and pose evidence, which is used to filter candidates with missing, inconsistent, or ambiguous evidence; (3) conditioned on the verified evidence, Gemini 3.1 Pro generates the question, correct answer, and five plausible distractors; and (4) human experts independently answer the questions without seeing Gemini’s answers, and only examples with matching answers are retained. Further details are provided in Appendix C.

> <span style="color:#F59E0B"><strong>Para. 29[CN]:</strong></span> 构建过程分为四个阶段：（1）Gemini 3.1 Pro [11] 盘点可靠的实体和场景关系；（2）专业视觉模型提供定位、分割、度量深度和姿态证据，并利用这些证据过滤掉存在证据缺失、不一致或歧义的候选样例；（3）以经过验证的证据为条件，Gemini 3.1 Pro 生成问题、正确答案和五个合理的干扰项；（4）人类专家在不知道 Gemini 答案的情况下独立回答问题，仅保留答案匹配的样例。更多细节见附录 C。

> ## 4 Experiments

> ### 4.1 Experimental Setup

> <span style="color:#3B82F6"><strong>Para. 30:</strong></span> **Models and Training Settings.** We instantiate SpatialCLI with three base VLMs: Qwen3-VL-8B-Instruct [1], Qwen3.6-35B-A3B [35], and Qwen3.6-27B [35]. All SFT and RL experiments are conducted using verl [41]. Detailed training configurations are provided in Appendix B.1.

> <span style="color:#F59E0B"><strong>Para. 30[CN]:</strong></span> **Models and Training Settings[CN]。** 我们使用三个基础 VLM 实例化 SpatialCLI：Qwen3-VL-8B-Instruct [1]、Qwen3.6-35B-A3B [35] 和 Qwen3.6-27B [35]。所有 SFT 和强化学习实验均使用 verl [41] 完成。详细的训练配置见附录 B.1。

> <span style="color:#3B82F6"><strong>Para. 31:</strong></span> **Evaluation Benchmarks.** We evaluate SpatialCLI on SpatialCLI-Bench, MindCube [57], MMSI [54], DA-2K [53], and BOPASK [2]. We evaluate each model both w/o Tools and w/ Tools. Detailed evaluation settings, including decoding parameters, tool-call budgets, and repeated evaluations, are provided in Appendix B.2.

> <span style="color:#F59E0B"><strong>Para. 31[CN]:</strong></span> **Evaluation Benchmarks[CN]。** 我们在 SpatialCLI-Bench、MindCube [57]、MMSI [54]、DA-2K [53] 和 BOPASK [2] 上评估 SpatialCLI。每个模型均在不使用工具和使用工具两种条件下进行评估。详细的评测设置，包括解码参数、工具调用预算和重复评估，见附录 B.2。

> <span style="color:#3B82F6"><strong>Para. 32:</strong></span> **Baselines.** We compare SpatialCLI with general-purpose models, including GPT-5.6 Sol [33], Gemini 3.1 Pro [11], Qwen3.7-Plus [36], and Qwen3.5-397B-A17B [35]. We further compare with SpaceTools [7] and AlloSpatial [37], two agentic methods for improving model spatial capabilities.

> <span style="color:#F59E0B"><strong>Para. 32[CN]:</strong></span> **Baselines[CN]。** 我们将 SpatialCLI 与通用模型进行比较，包括 GPT-5.6 Sol [33]、Gemini 3.1 Pro [11]、Qwen3.7-Plus [36] 和 Qwen3.5-397B-A17B [35]。我们还与 SpaceTools [7] 和 AlloSpatial [37] 进行比较，这两种方法都是用于提升模型空间能力的智能体方法。

> <!-- Page 7 -->

**Caption:** Figure 3. Training dynamics of Qwen3-VL-8B-Instruct under different RL strategies. (a,b) Inference w/ Tools (solid) and Inference w/o Tools (dashed) scores on SpatialCLI-Bench and MindCube. (c) Training reward over RL training. (d) Number of executed tool calls per trajectory over RL training. We compare RL w/ Tools + SFT, RL w/ Tools w/o SFT, and RL w/o Tools.

**Caption[CN]:** 图 3。 不同强化学习策略下 Qwen3-VL-8B-Instruct 的训练动态。（a、b）SpatialCLI-Bench 和 MindCube 上使用工具推理（实线）与不使用工具推理（虚线）的得分。（c）强化学习训练过程中的训练奖励。（d）强化学习训练过程中每条轨迹执行的工具调用次数。我们比较 RL w/ Tools + SFT、RL w/ Tools w/o SFT 和 RL w/o Tools。

**Caption:** Figure 4. Capability internalization across training-data exposure and model capacity. (a) SpatialCLI-Bench scores under inference w/ Tools and w/o Tools over internalization-stage training steps. (b) Capability-specific CII over the same process. (c) Capability-specific CII across model capacities. (d) SpatialCLI-Bench, MindCube, and DA-2K scores under inference w/o Tools (dashed) and w/ Tools (solid) across model capacities.

**Caption[CN]:** 图 4。 不同训练数据暴露量和模型容量下的能力内化。（a）内化阶段训练步数变化过程中，使用工具和不使用工具推理时的 SpatialCLI-Bench 得分。（b）同一过程中的特定能力 CII。（c）不同模型容量下的特定能力 CII。（d）不同模型容量下，不使用工具推理（虚线）和使用工具推理（实线）时的 SpatialCLI-Bench、MindCube 和 DA-2K 得分。

> ### 4.2 Overall Performance

> <span style="color:#3B82F6"><strong>Para. 33:</strong></span> **SpatialCLI Tools provide effective runtime spatial augmentation.** Table 1 shows that SpatialCLI Tools provide broad gains across both frontier and smaller models. The gains are generally larger for less capable base models: averaged over benchmarks, SpatialCLI Tools improve GPT-5.6 Sol by 6.1 points, compared with 21.0 points for Qwen3-VL-8B-Instruct. This suggests that external specialist perception is particularly valuable when the base model’s native spatial capabilities are limited. Under the controlled Qwen3-VL-8B-Instruct comparison, SpatialCLI Tools outperform the other tool frameworks on most subsets and AlloSpatial on every subset, showing that effective tool interfaces and tool-use policies are critical for transferring specialist perception into task performance.

> <span style="color:#F59E0B"><strong>Para. 33[CN]:</strong></span> **SpatialCLI Tools provide effective runtime spatial augmentation[CN]。** 表 1 表明，SpatialCLI Tools 在前沿模型和较小模型上都带来了广泛提升。对于能力较弱的基础模型，提升通常更大：在各基准的平均结果上，SpatialCLI Tools 将 GPT-5.6 Sol 提升了 6.1 个百分点，而将 Qwen3-VL-8B-Instruct 提升了 21.0 个百分点。这表明，当基础模型自身的空间能力有限时，外部专业感知尤其有价值。在受控的 Qwen3-VL-8B-Instruct 比较中，SpatialCLI Tools 在大多数子集上超过了其他工具框架，并在每个子集上超过了 AlloSpatial，说明有效的工具接口和工具使用策略对于将专业感知迁移为任务性能至关重要。

> <span style="color:#3B82F6"><strong>Para. 34:</strong></span> **Training jointly improves direct answering and practical tool use.** After training, every SpatialCLI variant outperforms its corresponding initial model w/o Tools on every reported evaluation subset, demonstrating consistent capability internalization. Training also strengthens practical tool use: compared with applying SpatialCLI Tools directly to the corresponding initial models, the trained variants achieve higher w/ Tools performance on most evaluation subsets. For example, SpatialCLI-8B improves from 35.3 to 72.7 on SpatialCLI-Bench w/o Tools and further reaches 91.3 w/ Tools. These results indicate that capability internalization need not trade off against tool use; training strengthens native spatial reasoning while preserving, and often further improving, the model’s ability to benefit from external tools.

> <span style="color:#F59E0B"><strong>Para. 34[CN]:</strong></span> **Training jointly improves direct answering and practical tool use[CN]。** 训练后，每个 SpatialCLI 变体在报告的每个评测子集上都超过了其对应的初始模型在不使用工具时的表现，体现出一致的能力内化效果。训练还增强了实际工具使用能力：与直接将 SpatialCLI Tools 应用于对应初始模型相比，训练后的变体在大多数评测子集上取得了更高的使用工具性能。例如，SpatialCLI-8B 在 SpatialCLI-Bench 不使用工具时从 35.3 提升至 72.7，并在使用工具时进一步达到 91.3。这些结果表明，能力内化不必以牺牲工具使用为代价；训练能够增强原生空间推理，同时保留并且通常进一步提升模型从外部工具中受益的能力。

> ### 4.3 Analysis

> <span style="color:#3B82F6"><strong>Para. 35:</strong></span> In this subsection, we analyze RL training dynamics, the progression of capability internalization with increasing training data, and its scaling behavior across model capacities. To quantify internalization, we use the Capability Internalization Index (CII), which measures how closely a model can reproduce the corre-

> <span style="color:#F59E0B"><strong>Para. 35[CN]:</strong></span> 在本小节中，我们分析强化学习训练动态、随着训练数据增加而产生的能力内化进展，以及其在不同模型容量下的缩放行为。为了量化内化程度，我们使用能力内化指数（CII），该指标衡量模型能够多大程度上复现相应的

> <!-- Page 8 -->

> <span style="color:#3B82F6"><strong>Para. 36:</strong></span> sponding spatial-tool outputs without invoking the tools; higher values indicate stronger internalization, and the complete definition is provided in Appendix E.

> <span style="color:#F59E0B"><strong>Para. 36[CN]:</strong></span> 空间工具输出而无需调用工具；数值越高表示内化程度越强，完整定义见附录 E。

> <span style="color:#3B82F6"><strong>Para. 37:</strong></span> **Training Dynamics.** Figure 3 compares RL w/ Tools + SFT, RL w/ Tools w/o SFT, and RL w/o Tools. RL w/ Tools + SFT starts from a strong tool-use policy, remains stable on both evaluation benchmarks, and finishes with the highest training reward and substantially better MindCube performance than RL w/ Tools w/o SFT. RL w/ Tools w/o SFT expands from 3.36 to 6.74 executed tool calls per trajectory, whereas RL w/ Tools + SFT remains near 2.56 throughout training, indicating that SFT provides a stable tool-use policy before RL. RL w/o Tools generally improves direct-answer performance, but its w/ Tools performance begins to decline after approximately 100 training steps, indicating degraded tool-use competence. Moreover, its direct-answer performance reaches only 52.7, well below the 72.7 achieved through capability internalization. This gap indicates that SpatialCLI uses the available training data substantially more effectively than direct SFT or RL. Appendix F.1 provides the complete comparison.

> <span style="color:#F59E0B"><strong>Para. 37[CN]:</strong></span> **Training Dynamics[CN]。** 图 3 比较了 RL w/ Tools + SFT、RL w/ Tools w/o SFT 和 RL w/o Tools。RL w/ Tools + SFT 从较强的工具使用策略开始，在两个评测基准上保持稳定，并以最高的训练奖励结束，其 MindCube 性能也显著优于 RL w/ Tools w/o SFT。RL w/ Tools w/o SFT 将每条轨迹执行的工具调用次数从 3.36 扩大到 6.74，而 RL w/ Tools + SFT 在整个训练过程中保持在约 2.56，说明 SFT 在强化学习之前提供了稳定的工具使用策略。RL w/o Tools 通常能够提升直接回答性能，但其使用工具性能在大约 100 个训练步之后开始下降，表明工具使用能力退化。此外，其直接回答性能仅达到 52.7，远低于通过能力内化达到的 72.7。这一差距表明，与直接 SFT 或强化学习相比，SpatialCLI 更充分地利用了可用训练数据。附录 F.1 给出了完整比较。

> <span style="color:#3B82F6"><strong>Para. 38:</strong></span> **Data Scaling of Capability Internalization.** Figures 4a and 4b show that, as the model is exposed to more internalization data, its w/o Tools score rises from 40.1% to 74.0%, while the four-capability macro-averaged CII increases from 45.6 to 61.6; the curves exhibit closely aligned upward trends. This synchronized improvement establishes a clear data-scaling trend: as internalization data increases, both task performance and CII continue to rise, indicating genuine transfer of specialist perceptual capabilities rather than final-answer memorization. Although the w/ Tools score temporarily declines, it recovers close to its starting level, indicating that Dual-View Capability Internalization restores the learned tool-use policy after transient interference and avoids catastrophic forgetting. Finally, the narrowing performance gap shows that, with increasing internalization data, SpatialCLI tools shift from an external capability source for solving the tasks to an optional augmentation of the model’s native capabilities.

> <span style="color:#F59E0B"><strong>Para. 38[CN]:</strong></span> **Data Scaling of Capability Internalization[CN]。** 图 4a 和图 4b 表明，随着模型接触更多内化数据，其不使用工具得分从 40.1% 上升到 74.0%，而四种能力宏平均的 CII 从 45.6 提升到 61.6；这些曲线呈现出高度一致的上升趋势。这种同步提升确立了清晰的数据缩放趋势：随着内化数据增加，任务性能和 CII 都持续上升，说明发生了专业感知能力的真实迁移，而不是对最终答案的记忆。尽管使用工具得分暂时下降，但其恢复到接近起始水平，表明双视角能力内化能够在短暂干扰之后恢复已学习的工具使用策略，并避免灾难性遗忘。最后，性能差距的缩小表明，随着内化数据增加，SpatialCLI 工具从解决任务所需的外部能力来源，转变为对模型原生能力的可选增强。

> <span style="color:#3B82F6"><strong>Para. 39:</strong></span> **Internalization continues to scale with model capacity after tool-use performance saturates.** Figure 4d reveals a clear separation between tool-use and internalization scaling: across the three model variants, w/ Tools scores vary by at most 1.0 point on each benchmark, whereas both larger variants substantially outperform SpatialCLI-8B w/o Tools. The saturation of w/ Tools performance is consistent with tool use requiring a relatively compact invocation-and-integration policy; once this policy is learned, the shared external specialists supply most of the required perceptual capability and thereby compress capacity-dependent differences. Internalization is less prone to saturation because the model must instead encode and reproduce multiple specialist capabilities in its own parameters; accordingly, Figure 4c shows that SpatialCLI-35B-A3B and SpatialCLI-27B substantially outperform SpatialCLI-8B across all four capability-specific CII values. These results show that external tools reduce performance differences across model sizes, whereas capability internalization continues to scale along two complementary dimensions: data exposure determines how fully a given model learns from the specialists, and model capacity affects how much of their capability it can absorb.

> <span style="color:#F59E0B"><strong>Para. 39[CN]:</strong></span> **Internalization continues to scale with model capacity after tool-use performance saturates[CN]。** 图 4d 揭示了工具使用和能力内化之间清晰的缩放差异：在三个模型变体中，使用工具得分在每个基准上的差异最多为 1.0 分，而两个更大的变体在不使用工具时都显著超过 SpatialCLI-8B。使用工具性能的饱和与工具使用只需要相对紧凑的调用—整合策略相一致；一旦学会该策略，共享的外部专业模型就会提供大部分所需的感知能力，从而压缩与模型容量相关的差异。内化不易饱和，因为模型需要在自身参数中编码并复现多种专业能力；相应地，图 4c 表明，在四种特定能力的 CII 指标上，SpatialCLI-35B-A3B 和 SpatialCLI-27B 都显著超过 SpatialCLI-8B。这些结果表明，外部工具能够减小不同模型规模之间的性能差异，而能力内化则沿着两个互补维度持续缩放：数据暴露量决定给定模型从专业模型中学习的充分程度，模型容量则影响其能够吸收多少专业模型的能力。

> ### 4.4 Ablation Studies

> <span style="color:#3B82F6"><strong>Para. 40:</strong></span> Using Qwen3-VL-8B-Instruct, we ablate how tools expose perceptual evidence and how tool-use trajectories are converted into capability-internalization supervision.

> <span style="color:#F59E0B"><strong>Para. 40[CN]:</strong></span> 我们使用 Qwen3-VL-8B-Instruct，消融研究工具如何呈现感知证据，以及工具使用轨迹如何转换为能力内化监督。

> <span style="color:#3B82F6"><strong>Para. 41:</strong></span> **Structured returns provide more effective tool evidence.** Table 2 compares the current structured tool returns with two red-border visual-return variants for Locate and Segment. The structured-plus-visual variant retains the structured coordinates and polygons while appending each visualization as a new image, whereas the visual-only variant returns the visualization without the corresponding structured result; Depth and Pose return remain unchanged.

> <span style="color:#F59E0B"><strong>Para. 41[CN]:</strong></span> **Structured returns provide more effective tool evidence[CN]。** 表 2 比较了当前的结构化工具返回结果，以及 Locate 和 Segment 的两种红框视觉返回变体。结构化加视觉的变体保留结构化坐标和多边形，同时将每个可视化结果作为新图像追加；而仅视觉变体返回可视化结果，不返回相应的结构化结果；Depth 和 Pose 的返回结果保持不变。

> <span style="color:#3B82F6"><strong>Para. 42:</strong></span> Visual Only improves over the initial model on all three evaluations, showing that tool-provided perceptual evidence remains useful even without structured Locate and Segment outputs. Adding structured coordinates and polygons yields substantially stronger performance, including a 20.1-point gain on SpatialCLI-Bench over Visual Only and consistent improvements on BOPASK. Structured Only performs comparably to Structured + Visual across all evaluations. Thus, explicit coordinates and polygons are the primary source of the improvement, while rendering the same evidence as additional images introduces extra visual context

> <span style="color:#F59E0B"><strong>Para. 42[CN]:</strong></span> 仅视觉在三个评测上都优于初始模型，表明即使没有结构化的 Locate 和 Segment 输出，工具提供的感知证据仍然有用。加入结构化坐标和多边形能够带来显著更强的性能，包括在 SpatialCLI-Bench 上相比仅视觉提升 20.1 分，并在 BOPASK 上取得一致提升。仅结构化在所有评测中都与结构化加视觉表现相当。因此，显式坐标和多边形是性能提升的主要来源，而将相同证据渲染为额外图像则引入了额外的视觉上下文

> <!-- Page 9 -->

> | Tool Return | SpatialCLI-Bench | BOPASK Traj. | BOPASK ObjRrr |
> |---|---:|---:|---:|
> | No Tools (Initial Model) | 35.3 | 25.8 | 13.3 |
> | Visual Only | 45.9 | 45.6 | 18.3 |
> | Structured + Visual | 66.0 | 54.5 | 20.1 |
> | Structured Only (Ours) | 66.5 | 54.3 | 20.6 |

**Caption:** Table 2. Tool-return format ablation with Qwen3-VL-8B-Instruct. Locate and Segment return red-border visualizations, structured coordinates or polygons, or both.

**Caption[CN]:** 表 2。Qwen3-VL-8B-Instruct 的工具返回格式消融。Locate 和 Segment 返回红框可视化、结构化坐标或多边形，或同时返回二者。

> **表 2[CN]。**使用 Qwen3-VL-8B-Instruct 进行的工具返回格式消融。Locate 和 Segment 返回红框可视化结果、结构化坐标或多边形，或者同时返回二者。

> <span style="color:#3B82F6"><strong>Para. 43:</strong></span> without a consistent score benefit. Structured returns can also be directly converted into textual capability-internalization supervision, making them easier for current VLMs to internalize than multimodal tool outputs such as annotated images.

> <span style="color:#F59E0B"><strong>Para. 43[CN]:</strong></span> 而没有带来一致的得分收益。结构化返回结果还可以直接转换为文本形式的能力内化监督，这使其比标注图像等多模态工具输出更容易被当前 VLM 内化。

> <span style="color:#3B82F6"><strong>Para. 44:</strong></span> **Progressive verbalization and dual-view training are both necessary.** Table 3 compares different forms of capability-internalization supervision. One-Pass Dual-View replaces Progressive Evidence-Grounded Trajectory Verbalization with a single pass over the complete trajectory while retaining the same dual-view training.

> <span style="color:#F59E0B"><strong>Para. 44[CN]:</strong></span> **Progressive verbalization and dual-view training are both necessary[CN]。** 表 3 比较了不同形式的能力内化监督。One-Pass Dual-View 在保留相同双视角训练的同时，用对完整轨迹进行一次处理替代渐进式基于证据的轨迹文字化。

> | Internalization Variant | w/o Tools Score | w/o Tools Tokens | w/ Tools Score | w/ Tools Tokens |
> |---|---:|---:|---:|---:|
> | Qwen3-VL-8B-Instruct | 35.3 | 2738 | 66.5 | 949 |
> | Final Answer Only | 52.7 | 1969 | 52.1 | 28 |
> | CoT + Answer | 45.0 | 5646 | 42.2 | 4401 |
> | Internalization View Only | 71.1 | 227 | 62.6 | 235 |
> | Tool-Use View Only | 42.2 | 6049 | 89.0 | 2155 |
> | One-Pass Dual-View | 64.5 | 451 | 90.2 | 2599 |
> | Full Dual-View (Ours) | **72.7** | 274 | **91.3** | 2480 |

**Caption:** Table 3. Capability-internalization ablation on SpatialCLI-Bench. One-Pass and Full Dual-View use single-pass and progressive trajectory verbalization, respectively. Tokens include model outputs and, w/ Tools, tool returns; the best scores are bold.

**Caption[CN]:** 表 3。SpatialCLI-Bench 上的能力内化消融。One-Pass 和 Full Dual-View 分别使用单次和渐进式轨迹文字化；token 包括模型输出，并且在使用工具时包括工具返回结果，最佳分数以粗体标示。

> **表 3[CN]。**SpatialCLI-Bench 上的能力内化消融。One-Pass 和 Full Dual-View 分别使用单次处理和渐进式轨迹文字化。Tokens 包含模型输出；在使用工具时，还包含工具返回结果；最佳得分以粗体显示。

> <span style="color:#3B82F6"><strong>Para. 45:</strong></span> For the untrained Qwen3-VL-8B-Instruct, external tools improve the score while reducing trajectory length from 2738 to 949 tokens, indicating that tool use can also lower decoding cost. The Qwen3.5-397B-A17B case studies in Appendix H exhibit the same qualitative trend, with tools enabling more direct and reliable problem solving. Final Answer Only yields concise but limited direct answers and loses tool use, while CoT + Answer is verbose and weaker, showing that neither outcome supervision nor ungrounded reasoning transfers the perceptual process. Internalization View Only produces strong and compact w/o Tools reasoning but weakens tool use, whereas Tool-Use View Only preserves w/ Tools performance without internalizing the capability, demonstrating the complementary roles of the two views. One-Pass Dual-View supports both modes, but Full Dual-View reaches the best w/o Tools and w/ Tools scores of 72.7 and 91.3 with shorter outputs, validating progressive evidence consolidation. Appendix F.3 further confirms that Full Dual-View retains the controlled calling behavior learned from the tool-use view.

> <span style="color:#F59E0B"><strong>Para. 45[CN]:</strong></span> 对于未经训练的 Qwen3-VL-8B-Instruct，外部工具在将轨迹长度从 2738 个 token 减少到 949 个 token 的同时提升了得分，说明工具使用也能够降低解码成本。附录 H 中 Qwen3.5-397B-A17B 的案例研究呈现出相同的定性趋势，工具使问题求解更加直接和可靠。仅最终答案能够产生简洁但有限的直接答案，并且会失去工具使用能力；而 CoT + Answer 冗长且性能更弱，表明无论是结果监督还是无依据的推理，都不能迁移感知过程。仅内化视角能够产生强且紧凑的不使用工具推理，但会削弱工具使用；仅工具使用视角能够保留使用工具时的性能，却无法内化能力，展示了两个视角的互补作用。One-Pass Dual-View 同时支持两种模式，但 Full Dual-View 以更短的输出取得了最佳的不使用工具和使用工具得分 72.7 和 91.3，验证了渐进式证据整合的有效性。附录 F.3 进一步确认，Full Dual-View 保留了从工具使用视角学习到的受控调用行为。

> ## 5 Conclusion

> <span style="color:#3B82F6"><strong>Para. 46:</strong></span> General VLMs lack the fine-grained perceptual capabilities required for embodied and spatial reasoning and cannot readily learn them from specialist vision models. SpatialCLI addresses this gap by connecting specialist models as runtime tools, learning agentic tool use, and converting successful trajectories into dual-view supervision for capability internalization. Across embodied and spatial benchmarks, SpatialCLI consistently improves both w/ Tools and w/o Tools reasoning, showing that external specialist capabilities can augment inference and be transferred into the VLM without sacrificing tool use.

> <span style="color:#F59E0B"><strong>Para. 46[CN]:</strong></span> 通用 VLM 缺乏具身和空间推理所需的细粒度感知能力，也无法轻易从专业视觉模型中学习这些能力。SpatialCLI 通过将专业模型连接为运行时工具、学习智能体式工具使用，并将成功轨迹转换为用于能力内化的双视角监督，弥补了这一差距。在具身和空间基准上，SpatialCLI 持续提升使用工具和不使用工具时的推理能力，表明外部专业能力能够增强推理，并且能够在不牺牲工具使用的情况下迁移到 VLM 中。

> <span style="color:#3B82F6"><strong>Para. 47:</strong></span> SpatialCLI remains limited by specialist-tool coverage and reliability, with its current scope restricted to structured perceptual outputs and perception-centric tasks. Future work will extend internalization to multimodal outputs using unified multimodal models capable of both understanding and generation, and integrate VLA tools under VLM planning for joint perception and action.

> <span style="color:#F59E0B"><strong>Para. 47[CN]:</strong></span> SpatialCLI 仍受专业工具覆盖范围和可靠性的限制，目前的范围局限于结构化感知输出和以感知为中心的任务。未来工作将使用同时具备理解和生成能力的统一多模态模型，把内化扩展到多模态输出，并在 VLM 规划下集成 VLA 工具，以实现感知与动作的联合。

> <!-- Page 10 -->

> [Page 10 contains no additional text.]

> <!-- Page 11 -->

> # References

> <span style="color:#3B82F6"><strong>Para. 48:</strong></span> [1] Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang Gao, Chumeng Ge, et al. Qwen3-vl technical report. *arXiv preprint arXiv:2511.21631*, 2025.

> <span style="color:#F59E0B"><strong>Para. 48[CN]:</strong></span> [1] Shuai Bai、Yuxuan Cai、Ruizhe Chen、Keqin Chen、Xionghui Chen、Zesen Cheng、Lianghao Deng、Wei Ding、Chang Gao、Chumeng Ge 等。Qwen3-vl 技术报告。*arXiv 预印本 arXiv:2511.21631*，2025。

> <span style="color:#3B82F6"><strong>Para. 49:</strong></span> [2] Vineet Bhat, Sungsu Kim, Valts Blukis, Greg Heinrich, Prashanth Krishnamurthy, Ramesh Karri, Stan Birchfield, Farshad Khorrami, and Jonathan Tremblay. Bop-ask: Object-interaction reasoning for vision-language models. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 16746–16757, 2026.

> <span style="color:#F59E0B"><strong>Para. 49[CN]:</strong></span> [2] Vineet Bhat、Sungsu Kim、Valts Blukis、Greg Heinrich、Prashanth Krishnamurthy、Ramesh Karri、Stan Birchfield、Farshad Khorrami 和 Jonathan Tremblay。Bop-ask：面向视觉语言模型的目标交互推理。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，第 16746–16757 页，2026。

> <span style="color:#3B82F6"><strong>Para. 50:</strong></span> [3] Zhipeng Cai, Zhuang Liu, Yunyong Xiong, Zechun Liu, Vikas Chandra, and Yangyang Shi. Vlm3: Vision language models are native 3d learners. *arXiv preprint arXiv:2605.30561*, 2026.

> <span style="color:#F59E0B"><strong>Para. 50[CN]:</strong></span> [3] Zhipeng Cai、Zhuang Liu、Yunyong Xiong、Zechun Liu、Vikas Chandra 和 Yangyang Shi。Vlm3：视觉语言模型是原生三维学习器。*arXiv 预印本 arXiv:2605.30561*，2026。

> <span style="color:#3B82F6"><strong>Para. 51:</strong></span> [4] Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath, Ronghang Hu, Didac Suris, Chaitanya Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew Huang, et al. Sam 3: Segment anything with concepts. *arXiv preprint arXiv:2511.16719*, 2025.

> <span style="color:#F59E0B"><strong>Para. 51[CN]:</strong></span> [4] Nicolas Carion、Laura Gustafson、Yuan-Ting Hu、Shoubhik Debnath、Ronghang Hu、Didac Suris、Chaitanya Ryali、Kalyan Vasudev Alwala、Haitham Khedr、Andrew Huang 等。Sam 3：使用概念分割一切。*arXiv 预印本 arXiv:2511.16719*，2025。

> <span style="color:#3B82F6"><strong>Para. 52:</strong></span> [5] Boyuan Chen, Zhuo Xu, Sean Kirmani, Brain Ichter, Dorsa Sadigh, Leonidas Guibas, and Fei Xia. Spatialvlm: Endowing vision-language models with spatial reasoning capabilities. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 14455–14465, 2024.

> <span style="color:#F59E0B"><strong>Para. 52[CN]:</strong></span> [5] Boyuan Chen、Zhuo Xu、Sean Kirmani、Brain Ichter、Dorsa Sadigh、Leonidas Guibas 和 Fei Xia。Spatialvlm：赋予视觉语言模型空间推理能力。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，第 14455–14465 页，2024。

> <span style="color:#3B82F6"><strong>Para. 53:</strong></span> [6] Siyi Chen, Hugo Hadfield, Alex Zook, Mikaela Angelina Uy, Chan Hee Song, Erwin Coumans, Xuning Yang, Faisal Ladhaq, Qing Qu, Stan Birchfield, et al. Volo: A physical orchestrator for open-vocabulary long-horizon manipulation. *arXiv preprint arXiv:2606.07713*, 2026.

> <span style="color:#F59E0B"><strong>Para. 53[CN]:</strong></span> [6] Siyi Chen、Hugo Hadfield、Alex Zook、Mikaela Angelina Uy、Chan Hee Song、Erwin Coumans、Xuning Yang、Faisal Ladhaq、Qing Qu、Stan Birchfield 等。Volo：面向开放词汇长时程操作的物理协调器。*arXiv 预印本 arXiv:2606.07713*，2026。

> <span style="color:#3B82F6"><strong>Para. 54:</strong></span> [7] Siyi Chen, Mikaela Angelina Uy, Chan Hee Song, Faisal Ladhak, Adithyavairavan Murali, Qing Qu, Stan Birchfield, Valts Blukis, and Jonathan Tremblay. Spacetools: Tool-augmented spatial reasoning via double interactive rl. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 37109–37120, 2026.

> <span style="color:#F59E0B"><strong>Para. 54[CN]:</strong></span> [7] Siyi Chen、Mikaela Angelina Uy、Chan Hee Song、Faisal Ladhak、Adithyavairavan Murali、Qing Qu、Stan Birchfield、Valts Blukis 和 Jonathan Tremblay。Spacetools：通过双重交互式强化学习实现工具增强的空间推理。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，第 37109–37120 页，2026。

> <span style="color:#3B82F6"><strong>Para. 55:</strong></span> [8] Zeren Chen, Xiaoya Lu, Zhijie Zheng, Pengmou Li, Lehan He, Yijin Zhou, Jinxue Shao, Bohan Zhuang, and Lu Sheng. Geometrically-constrained agent for spatial reasoning. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 38689–38699, 2026.

> <span style="color:#F59E0B"><strong>Para. 55[CN]:</strong></span> [8] Zeren Chen、Xiaoya Lu、Zhijie Zheng、Pengmou Li、Lehan He、Yijin Zhou、Jinxue Shao、Bohan Zhuang 和 Lu Sheng。用于空间推理的几何约束智能体。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，第 38689–38699 页，2026。

> <span style="color:#3B82F6"><strong>Para. 56:</strong></span> [9] An-Chieh Cheng, Hongxu Yin, Yang Fu, Qianqiao Guo, Ruihan Yang, Jan Kautz, Xiaolong Wang, and Sifei Liu. Spatialgpt: Grounded spatial reasoning in vision-language models. In *Advances in Neural Information Processing Systems*, volume 37, pages 135062–135093, 2024.

> <span style="color:#F59E0B"><strong>Para. 56[CN]:</strong></span> [9] An-Chieh Cheng、Hongxu Yin、Yang Fu、Qianqiao Guo、Ruihan Yang、Jan Kautz、Xiaolong Wang 和 Sifei Liu。Spatialgpt：视觉语言模型中的有依据空间推理。载于 *神经信息处理系统进展*，第 37 卷，第 135062–135093 页，2024。

> <span style="color:#3B82F6"><strong>Para. 57:</strong></span> [10] Yalun Dai, Hao Li, Shulin Tian, Runmao Yao, Yuhao Dong, Fangzhou Hong, Zhaoxi Chen, Fangfu Liu, Baoliang Tian, Dingwen Zhang, et al. S-agent: Spatial tool-use elicits reasoning for spatial intelligence. *arXiv preprint arXiv:2606.20515*, 2026.

> <span style="color:#F59E0B"><strong>Para. 57[CN]:</strong></span> [10] Yalun Dai、Hao Li、Shulin Tian、Runmao Yao、Yuhao Dong、Fangzhou Hong、Zhaoxi Chen、Fangfu Liu、Baoliang Tian、Dingwen Zhang 等。S-agent：空间工具使用激发空间智能推理。*arXiv 预印本 arXiv:2606.20515*，2026。

> <span style="color:#3B82F6"><strong>Para. 58:</strong></span> [11] Google DeepMind. Gemini 3.1 Pro model card, February 2026. https://deepmind.google/models/model-cards/gemini-3-1-pro/.

> <span style="color:#F59E0B"><strong>Para. 58[CN]:</strong></span> [11] Google DeepMind。Gemini 3.1 Pro 模型卡，2026 年 2 月。https://deepmind.google/models/model-cards/gemini-3-1-pro/。

> <span style="color:#3B82F6"><strong>Para. 59:</strong></span> [12] Andrew Guo, Bowen Wen, Jianhe Yuan, Jonathan Tremblay, Stephen Tyree, Jeffrey Smith, and Stan Birchfield. A dataset of real-world manipulable object categories with pose annotations, affordances, and reconstructions. In *2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, pages 11428–11435. IEEE, 2023.

> <span style="color:#F59E0B"><strong>Para. 59[CN]:</strong></span> [12] Andrew Guo、Bowen Wen、Jianhe Yuan、Jonathan Tremblay、Stephen Tyree、Jeffrey Smith 和 Stan Birchfield。带有姿态标注、可供性和重建信息的真实世界可操作目标类别数据集。载于 *2023 IEEE/RSJ 智能机器人与系统国际会议（IROS）*，第 11428–11435 页。IEEE，2023。

> <span style="color:#3B82F6"><strong>Para. 60:</strong></span> [13] Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu Zhang, Shirong Ma, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. *arXiv preprint arXiv:2501.12948*, 2025.

> <span style="color:#F59E0B"><strong>Para. 60[CN]:</strong></span> [13] Daya Guo、Dejian Yang、Haowei Zhang、Junxiao Song、Peiyi Wang、Qihao Zhu、Runxin Xu、Ruoyu Zhang、Shirong Ma、Xiao Bi 等。Deepseek-r1：通过强化学习激励大语言模型中的推理能力。*arXiv 预印本 arXiv:2501.12948*，2025。

> <span style="color:#3B82F6"><strong>Para. 61:</strong></span> [14] Tanmay Gupta and Aniruddha Kembhavi. Visual programming: Compositional visual reasoning without training. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, pages 14953–14962, 2023.

> <span style="color:#F59E0B"><strong>Para. 61[CN]:</strong></span> [14] Tanmay Gupta 和 Aniruddha Kembhavi。视觉编程：无需训练的组合视觉推理。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，第 14953–14962 页，2023。

> <span style="color:#3B82F6"><strong>Para. 62:</strong></span> [15] Yi Han, Enshen Zhou, Shanyu Rong, Jingkun An, Pengwei Wang, Zhongyuan Wang, Cheng Chi, Lu Sheng, and Shanghang Zhang. Tiger: Tool-ontin rated geometric reasoning in vision-language models for robotics. *arXiv preprint arXiv:2510.07181*, 2025.

> <span style="color:#F59E0B"><strong>Para. 62[CN]:</strong></span> [15] Yi Han、Enshen Zhou、Shanyu Rong、Jingkun An、Pengwei Wang、Zhongyuan Wang、Cheng Chi、Lu Sheng 和 Shanghang Zhang。Tiger：面向机器人的视觉语言模型中的工具导向几何推理。*arXiv 预印本 arXiv:2510.07181*，2025。

> <span style="color:#3B82F6"><strong>Para. 63:</strong></span> [16] Stefan Hinterstoisser, Vincent Lepetit, Slobodan Ilic, Stefan Holzer, Gary Bradski, Kurt Konolige, and Nassir Navab. Model based training, detection and pose estimation of texture-less 3d objects in heavily cluttered scenes. In *Asian conference on computer vision*, pages 548–562. Springer, 2012.

> <span style="color:#F59E0B"><strong>Para. 63[CN]:</strong></span> [16] Stefan Hinterstoisser、Vincent Lepetit、Slobodan Ilic、Stefan Holzer、Gary Bradski、Kurt Konolige 和 Nassir Navab。在高度杂乱场景中对无纹理三维目标进行基于模型的训练、检测和姿态估计。载于 *亚洲计算机视觉会议*，第 548–562 页。Springer，2012。

> <!-- Page 12 -->

> <span style="color:#3B82F6"><strong>Para. 64:</strong></span> [17] Jiaheng Hu, Monit Shridhara, Caden Lu, Dhruv Shah, Hao-Tien Lewis Chiang, Jie Tan, and Annie Xie. What matters in orchestrating robot policies: A systematic study of hierarchical vla agents. *arXiv preprint arXiv:2606.10267*, 2026.

> <span style="color:#F59E0B"><strong>Para. 64[CN]:</strong></span> [17] Jiaheng Hu、Monit Shridhara、Caden Lu、Dhruv Shah、Hao-Tien Lewis Chiang、Jie Tan 和 Annie Xie。编排机器人策略时什么最重要：分层 VLA 智能体的系统性研究。*arXiv 预印本 arXiv:2606.10267*，2026。

> <span style="color:#3B82F6"><strong>Para. 65:</strong></span> [18] Yushi Hu, Elliott Tretter, Chun-Tan Lu, Krishnamurthy Viswanathan, Kenji Hata, Enming Luo, Ranjay Krishna, and Ariel Fuxman. Visual program distillation: Distilling tools and programmatic reasoning into vision-language models. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 9580–9601, 2024.

> <span style="color:#F59E0B"><strong>Para. 65[CN]:</strong></span> [18] Yushi Hu、Elliott Tretter、Chun-Tan Lu、Krishnamurthy Viswanathan、Kenji Hata、Enming Luo、Ranjay Krishna 和 Ariel Fuxman。视觉程序蒸馏：将工具和程序化推理蒸馏到视觉语言模型中。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，第 9580–9601 页，2024。

> <span style="color:#3B82F6"><strong>Para. 66:</strong></span> [19] Zixuan Huang, Xin Xia, Yuxi Ren, Jianbin Zheng, Xuanda Wang, Zhixia Zhang, Hongyan Xie, Songshi Jiang, Zehao Chen, Xuefeng Xiao, et al. Does your reasoning model implicitly know when to stop thinking? *arXiv preprint arXiv:2602.08584*, 2026.

> <span style="color:#F59E0B"><strong>Para. 66[CN]:</strong></span> [19] Zixuan Huang、Xin Xia、Yuxi Ren、Jianbin Zheng、Xuanda Wang、Zhixia Zhang、Hongyan Xie、Songshi Jiang、Zehao Chen、Xuefeng Xiao 等。你的推理模型是否隐式地知道何时停止思考？*arXiv 预印本 arXiv:2602.08584*，2026。

> <span style="color:#3B82F6"><strong>Para. 67:</strong></span> [20] Bowen Jin, Hansi Zeng, Zhenrui Yue, Jinsung Yoon, Sercan Arik, Dong Wang, Hamed Zamani, and Jiawei Han. Search-r1: Training llms to reason and leverage search engines with reinforcement learning. *arXiv preprint arXiv:2503.09516*, 2025.

> <span style="color:#F59E0B"><strong>Para. 67[CN]:</strong></span> [20] Bowen Jin、Hansi Zeng、Zhenrui Yue、Jinsung Yoon、Sercan Arik、Dong Wang、Hamed Zamani 和 Jiawei Han。Search-r1：通过强化学习训练大语言模型进行推理并利用搜索引擎。*arXiv 预印本 arXiv:2503.09516*，2025。

> <span style="color:#3B82F6"><strong>Para. 68:</strong></span> [21] Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov, Ethan Foster, Grace Lam, Pannag Sanketi, et al. Openvla: An open-source vision-language-action model. *arXiv preprint arXiv:2406.09246*, 2024.

> <span style="color:#F59E0B"><strong>Para. 68[CN]:</strong></span> [21] Moo Jin Kim、Karl Pertsch、Siddharth Karamcheti、Ted Xiao、Ashwin Balakrishna、Suraj Nair、Rafael Rafailov、Ethan Foster、Grace Lam、Pannag Sanketi 等。Openvla：一种开源视觉语言动作模型。*arXiv 预印本 arXiv:2406.09246*，2024。

> <span style="color:#3B82F6"><strong>Para. 69:</strong></span> [22] Alina Kuznetsova, Hassan Rom, Neil Alldrin, Jasper Uijlings, Ivan Krasin, Jordi Pont-Tuset, Shahab Kamali, Stefan Popov, Matteo Matalto, Alexander Koloskov, et al. The open images dataset v4: Unified image classification, object detection, and visual relationship detection at scale. *arXiv preprint arXiv:1811.11819*, 2018.

> <span style="color:#F59E0B"><strong>Para. 69[CN]:</strong></span> [22] Alina Kuznetsova、Hassan Rom、Neil Alldrin、Jasper Uijlings、Ivan Krasin、Jordi Pont-Tuset、Shahab Kamali、Stefan Popov、Matteo Matalto、Alexander Koloskov 等。Open Images 数据集 v4：大规模统一图像分类、目标检测和视觉关系检测。*arXiv 预印本 arXiv:1811.11819*，2018。

> <span style="color:#3B82F6"><strong>Para. 70:</strong></span> [23] Justin Lazarow, David Griffiths, Gefen Kohavi, Francisco Crespo, and Afshin Dehghan. Cubify anything: Scaling indoor 3d object detection. *arXiv preprint arXiv:2412.04458*, 2024.

> <span style="color:#F59E0B"><strong>Para. 70[CN]:</strong></span> [23] Justin Lazarow、David Griffiths、Gefen Kohavi、Francisco Crespo 和 Afshin Dehghan。Cubify anything：扩展室内三维目标检测。*arXiv 预印本 arXiv:2412.04458*，2024。

> <span style="color:#3B82F6"><strong>Para. 71:</strong></span> [24] Zixing Lei, Changxing Liu, Yichen Xiong, Minhao Xiong, Yuanzhuo Ding, Zhipeng Zhang, Weixin Li, and Siheng Chen. Towards long-horizon embodied agents with tool-aligned vision-language-action models. *arXiv preprint arXiv:2605.12119*, 2026.

> <span style="color:#F59E0B"><strong>Para. 71[CN]:</strong></span> [24] Zixing Lei、Changxing Liu、Yichen Xiong、Minhao Xiong、Yuanzhuo Ding、Zhipeng Zhang、Weixin Li 和 Siheng Chen。迈向具有工具对齐视觉语言动作模型的长时程具身智能体。*arXiv 预印本 arXiv:2605.12119*，2026。

> <span style="color:#3B82F6"><strong>Para. 72:</strong></span> [25] Haotong Lin, Sili Chen, Junhao Liew, Donny Y Chen, Zhenyu Li, Guang Shi, Jiashi Feng, and Bingyi Kang. Depth anything 3: Recovering the visual space from any views. *arXiv preprint arXiv:2511.10647*, 2025.

> <span style="color:#F59E0B"><strong>Para. 72[CN]:</strong></span> [25] Haotong Lin、Sili Chen、Junhao Liew、Donny Y Chen、Zhenyu Li、Guang Shi、Jiashi Feng 和 Bingyi Kang。Depth anything 3：从任意视角恢复视觉空间。*arXiv 预印本 arXiv:2511.10647*，2025。

> <span style="color:#3B82F6"><strong>Para. 73:</strong></span> [26] Aixin Liu, Aoxue Mei, Bangcai Lin, Bing Xue, Bingxuan Wang, Bingzhang Xu, Bochao Wu, Bowei Zhang, Chaofan Lin, Chen Dong, et al. Deepseek-v3.2: Pushing the frontier of open large language models. *arXiv preprint arXiv:2512.02556*, 2025.

> <span style="color:#F59E0B"><strong>Para. 73[CN]:</strong></span> [26] Aixin Liu、Aoxue Mei、Bangcai Lin、Bing Xue、Bingxuan Wang、Bingzhang Xu、Bochao Wu、Bowei Zhang、Chaofan Lin、Chen Dong 等。Deepseek-v3.2：推动开放大语言模型的前沿。*arXiv 预印本 arXiv:2512.02556*，2025。

> <span style="color:#3B82F6"><strong>Para. 74:</strong></span> [27] Haowen Liu, Xirui Li, Shaoxiong Yao, Peng Shi, Tianyi Zhou, Jia-Bin Huang, Furong Huang, and Jiayuan Mao. Guava: An effective and universal harness for embodied manipulation. *arXiv preprint arXiv:2606.18638*, 2026.

> <span style="color:#F59E0B"><strong>Para. 74[CN]:</strong></span> [27] Haowen Liu、Xirui Li、Shaoxiong Yao、Peng Shi、Tianyi Zhou、Jia-Bin Huang、Furong Huang 和 Jiayuan Mao。Guava：一种有效且通用的具身操作框架。*arXiv 预印本 arXiv:2606.18638*，2026。

> <span style="color:#3B82F6"><strong>Para. 75:</strong></span> [28] Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao Zhang, Jinglin Yang, Qing Jiang, Chunyuang Li, Jianwei Yang, Hang Su, et al. Grounding dino: Marrying dino with grounded pre-training for open-set object detection. In *European conference on computer vision*, pages 358–355. Springer, 2024.

> <span style="color:#F59E0B"><strong>Para. 75[CN]:</strong></span> [28] Shilong Liu、Zhaoyang Zeng、Tianhe Ren、Feng Li、Hao Zhang、Jinglin Yang、Qing Jiang、Chunyuang Li、Jianwei Yang、Hang Su 等。Grounding DINO：将 DINO 与基于 grounding 的预训练结合，用于开放集目标检测。载于 *欧洲计算机视觉会议*，第 358–355 页。Springer，2024。

> <span style="color:#3B82F6"><strong>Para. 76:</strong></span> [29] Shunyu Liu, Minghao Liu, Huichi Zhou, Zhenyu Cui, Yang Zhou, Yuhao Zhou, Jiahao Gao, Heng Zhou, Yunhao Yang, Wendong Fan, et al. Veriwbe: Verifiable long-chain web benchmark for agentic information-seeking. *arXiv preprint arXiv:2508.04026*, 2025.

> <span style="color:#F59E0B"><strong>Para. 76[CN]:</strong></span> [29] Shunyu Liu、Minghao Liu、Huichi Zhou、Zhenyu Cui、Yang Zhou、Yuhao Zhou、Jiahao Gao、Heng Zhou、Yunhao Yang、Wendong Fan 等。Veriwbe：面向智能体信息检索的可验证长链网页基准。*arXiv 预印本 arXiv:2508.04026*，2025。

> <span style="color:#3B82F6"><strong>Para. 77:</strong></span> [30] Tengxiao Liu, Zifeng Wang, Jin Miao, I Hsu, Jun Yan, Jiefeng Chen, Rujun Han, Fangyuan Xu, Yanfei Chen, Ke Jiang, et al. Budget-aware tool-use enables effective agent scaling. *arXiv preprint arXiv:2511.17006*, 2025.

> <span style="color:#F59E0B"><strong>Para. 77[CN]:</strong></span> [30] Tengxiao Liu、Zifeng Wang、Jin Miao、I Hsu、Jun Yan、Jiefeng Chen、Rujun Han、Fangyuan Xu、Yanfei Chen、Ke Jiang 等。预算感知工具使用实现有效的智能体扩展。*arXiv 预印本 arXiv:2511.17006*，2025。

> <span style="color:#3B82F6"><strong>Para. 78:</strong></span> [31] Chenyang Ma, Kai Lu, Ta-Ying Cheng, Niki Trigoni, and Andrew Markham. Spatialpin: Enhancing spatial reasoning capabilities of vision-language models through prompting and interacting 3d priors. In *Advances in neural information processing systems*, volume 37, pages 68803–68832, 2024.

> <span style="color:#F59E0B"><strong>Para. 78[CN]:</strong></span> [31] Chenyang Ma、Kai Lu、Ta-Ying Cheng、Niki Trigoni 和 Andrew Markham。Spatialpin：通过提示和交互式三维先验增强视觉语言模型的空间推理能力。载于 *神经信息处理系统进展*，第 37 卷，第 68803–68832 页，2024。

> <span style="color:#3B82F6"><strong>Para. 79:</strong></span> [32] Reichiro Nakano, Jacob Hilton, Suchir Balaji, Jeff Wu, Long Ouyang, Christina Kim, Christopher Hesse, Shantanu Jain, Vineet Kosaraju, William Saunders, et al. Webgpt: Browser-assisted question-answering with human feedback. *arXiv preprint arXiv:2112.09332*, 2021.

> <span style="color:#F59E0B"><strong>Para. 79[CN]:</strong></span> [32] Reichiro Nakano、Jacob Hilton、Suchir Balaji、Jeff Wu、Long Ouyang、Christina Kim、Christopher Hesse、Shantanu Jain、Vineet Kosaraju、William Saunders 等。WebGPT：带有人类反馈的浏览器辅助问答。*arXiv 预印本 arXiv:2112.09332*，2021。

> <span style="color:#3B82F6"><strong>Para. 80:</strong></span> [33] OpenAI. Gpt-5.6: Frontier intelligence that scales with your ambition, July 2026. https://openai.com/index/gpt-5-6/.

> <span style="color:#F59E0B"><strong>Para. 80[CN]:</strong></span> [33] OpenAI。Gpt-5.6：随您的抱负扩展的前沿智能，2026 年 7 月。https://openai.com/index/gpt-5-6/。

> <span style="color:#3B82F6"><strong>Para. 81:</strong></span> [34] Yujia Qin, Ying Ye, Junjie Fang, Haoming Wang, Shihao Liang, Shizuo Tian, Junda Zhang, Jiahao Li, Yunxin Li, Shijue Huang, et al. Ui-tars: Pioneering automated gui interaction with native agents. *arXiv preprint arXiv:2501.12326*, 2025.

> <span style="color:#F59E0B"><strong>Para. 81[CN]:</strong></span> [34] Yujia Qin、Ying Ye、Junjie Fang、Haoming Wang、Shihao Liang、Shizuo Tian、Junda Zhang、Jiahao Li、Yunxin Li、Shijue Huang 等。Ui-tars：使用原生智能体开创自动化 GUI 交互。*arXiv 预印本 arXiv:2501.12326*，2025。


> ## Page 13 / 第 13 页

> Para. 1: [35] Qwen Team. Qwen3.5: Towards native multimodal agents, February 2026. https://qwen.ai/blog?id=qwen3.5.

> Para. 1[CN]: [35] Qwen Team. Qwen3.5：迈向原生多模态智能体，2026 年 2 月。https://qwen.ai/blog?id=qwen3.5.

> Para. 2: [36] Qwen Team. Qwen3.7-Plus: Multimodal agent intelligence, June 2026. https://qwen.ai/blog?id=qwen3.7-plus.

> Para. 2[CN]: [36] Qwen Team. Qwen3.7-Plus：多模态智能体智能，2026 年 6 月。https://qwen.ai/blog?id=qwen3.7-plus.

> Para. 3: [37] Shouwei Ruan, Bin Wang, Zhenyu Wu, Qihui Zhu, Yuxiang Zhang, Jingzhi Li, Yubin Wang, and Xingxing Wei. AI-lospatial: Agentic harness framework for spatial reasoning in foundation models. *arXiv preprint arXiv:2606.08952*, 2026.

> Para. 3[CN]: [37] Shouwei Ruan, Bin Wang, Zhenyu Wu, Qihui Zhu, Yuxiang Zhang, Jingzhi Li, Yubin Wang, and Xingxing Wei. AI-lospatial：用于基础模型空间推理的智能体式支架框架。*arXiv 预印本 arXiv:2606.08952*，2026。

> Para. 4: [38] Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Toolformer: Language models can teach themselves to use tools. In *Advances in neural information processing systems*, volume 36, pages 68539–68551, 2023.

> Para. 4[CN]: [38] Timo Schick, Jane Dwivedi-Yu, Roberto Dessi, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Toolformer：语言模型可以自学使用工具。载于 *Advances in Neural Information Processing Systems*，第 36 卷，第 68539–68551 页，2023。

> Para. 5: [39] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. *arXiv preprint arXiv:2402.03300*, 2024.

> Para. 5[CN]: [39] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Yang Wu, 等。Deepseekmath：推动开放语言模型中数学推理的极限。*arXiv 预印本 arXiv:2402.03300*，2024。

> Para. 6: [40] Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, and Yueting Zhuang. Hugginggpt: Solving ai tasks with chatgpt and its friends in hugging face. In *Advances in Neural Information Processing Systems*, volume 36, pages 38154–38180, 2023.

> Para. 6[CN]: [40] Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, and Yueting Zhuang. Hugginggpt：使用 ChatGPT 及其在 Hugging Face 中的伙伴解决 AI 任务。载于 *Advances in Neural Information Processing Systems*，第 36 卷，第 38154–38180 页，2023。

> Para. 7: [41] Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. *arXiv preprint arXiv:2409.19256*, 2024.

> Para. 7[CN]: [41] Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua Peng, Haibin Lin, and Chuan Wu. Hybridflow：灵活且高效的 RLHF 框架。*arXiv 预印本 arXiv:2409.19256*，2024。

> Para. 8: [42] Dídac Surís, Sachit Menon, and Carl Vondrick. Vipergpt: Visual inference via python execution for reasoning. In *Proceedings of the IEEE/CVF international conference on computer vision*, pages 11888–11898, 2023.

> Para. 8[CN]: [42] Dídac Surís, Sachit Menon, and Carl Vondrick. Vipergpt：通过执行 Python 进行视觉推理。载于 *IEEE/CVF 计算机视觉国际会议论文集*，第 11888–11898 页，2023。

> Para. 9: [43] HY Team, Xumin Yu, Zuyan Liu, Ziyi Wang, He Zhang, Yongming Rao, Fangfu Liu, Yani Zhang, Ruowen Zhao, Oran Wang, et al. Hy-embodied-0.5: Embodied foundation models for real-world agents. *arXiv preprint arXiv:2604.07430*, 2026.

> Para. 9[CN]: [43] HY Team, Xumin Yu, Zuyan Liu, Ziyi Wang, He Zhang, Yongming Rao, Fangfu Liu, Yani Zhang, Ruowen Zhao, Oran Wang, 等。Hy-embodied-0.5：面向真实世界智能体的具身基础模型。*arXiv 预印本 arXiv:2604.07430*，2026。

> Para. 10: [44] Stephen Tyree, Jonathan Tremblay, Thang To, Jia Cheng, Terry Mossier, Jeffrey Smith, and Stan Birchfield. 6-dof pose estimation of household objects for robotic manipulation: An accessible dataset and benchmark. In *2022 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*, pages 13081–13088. IEEE, 2022.

> Para. 10[CN]: [44] Stephen Tyree, Jonathan Tremblay, Thang To, Jia Cheng, Terry Mossier, Jeffrey Smith, and Stan Birchfield. 用于机器人操作的家居物体六自由度位姿估计：一个易获取的数据集与基准。载于 *2022 IEEE/RSJ 智能机器人与系统国际会议（IROS）*，第 13081–13088 页。IEEE，2022。

> Para. 11: [45] Jianyuan Wang, Minghao Chen, Nikita Karaev, Andrea Vedaldi, Christian Rupprecht, and David Novotny. Vggt: Visual geometry grounded transformer. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, pages 5294–5306, 2025.

> Para. 11[CN]: [45] Jianyuan Wang, Minghao Chen, Nikita Karaev, Andrea Vedaldi, Christian Rupprecht, and David Novotny. Vggt：以视觉几何为基础的 Transformer。载于 *计算机视觉与模式识别会议论文集*，第 5294–5306 页，2025。

> Para. 12: [46] Shihao Wang, Shilong Liu, Yuanguo Kuang, Xinyu Wei, Yangzhou Liu, Zhiqi Li, Yunze Man, Guo Chen, Andrew Tao, Guilin Liu, et al. Locateanything: Fast and high-quality vision-language grounding with parallel box decoding. *arXiv preprint arXiv:2605.27365*, 2026.

> Para. 12[CN]: [46] Shihao Wang, Shilong Liu, Yuanguo Kuang, Xinyu Wei, Yangzhou Liu, Zhiqi Li, Yunze Man, Guo Chen, Andrew Tao, Guilin Liu, 等。Locateanything：通过并行框解码实现快速、高质量的视觉—语言定位。*arXiv 预印本 arXiv:2605.27365*，2026。

> Para. 13: [47] Zehan Wang, Ziang Zhang, Jiaguan Xu, Jialei Wang, Tianyu Pang, Chao Du, Hengshuang Zhao, and Zhou Zhao. Orient anything v2: Unifying orientation and rotation understanding. *arXiv preprint arXiv:2601.05573*, 2026.

> Para. 13[CN]: [47] Zehan Wang, Ziang Zhang, Jiaguan Xu, Jialei Wang, Tianyu Pang, Chao Du, Hengshuang Zhao, and Zhou Zhao. Orient anything v2：统一方向与旋转理解。*arXiv 预印本 arXiv:2601.05573*，2026。

> Para. 14: [48] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. In *Advances in neural information processing systems*, volume 35, pages 24824–24837, 2022.

> Para. 14[CN]: [48] Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, 等。思维链提示可引出大型语言模型中的推理。载于 *Advances in Neural Information Processing Systems*，第 35 卷，第 24824–24837 页，2022。

> Para. 15: [49] Yu Xiang, Tanner Schmidt, Venkatraman Narayanan, and Dieter Fox. Posecnn: A convolutional neural network for 6d object pose estimation in cluttered scenes. *arXiv preprint arXiv:1711.00199*, 2017.

> Para. 15[CN]: [49] Yu Xiang, Tanner Schmidt, Venkatraman Narayanan, and Dieter Fox. Posecnn：用于杂乱场景中六维物体位姿估计的卷积神经网络。*arXiv 预印本 arXiv:1711.00199*，2017。

> Para. 16: [50] Ganlin Yang, Tianyi Zhang, Haoran Hao, Weiyun Wang, Yibin Liu, Dehui Wang, Guanzhou Chen, Zijian Cai, Junting Chen, Weijie Su, et al. Vlaser: Vision-language-action model with synergistic embodied reasoning. *arXiv preprint arXiv:2510.11027*, 2025.

> Para. 16[CN]: [50] Ganlin Yang, Tianyi Zhang, Haoran Hao, Weiyun Wang, Yibin Liu, Dehui Wang, Guanzhou Chen, Zijian Cai, Junting Chen, Weijie Su, 等。Vlaser：具有协同具身推理能力的视觉—语言—动作模型。*arXiv 预印本 arXiv:2510.11027*，2025。

> Para. 17: [51] Jihan Yang, Shusheng Yang, Anjali W Gupta, Rilyn Han, Li Fei-Fei, and Saining Xie. Thinking in space: How multimodal large language models see, remember, and recall spaces. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, pages 10632–10643, 2025.

> Para. 17[CN]: [51] Jihan Yang, Shusheng Yang, Anjali W Gupta, Rilyn Han, Li Fei-Fei, and Saining Xie. 在空间中思考：多模态大型语言模型如何观察、记忆与回忆空间。载于 *计算机视觉与模式识别会议论文集*，第 10632–10643 页，2025。

> Para. 18: [52] John Yang, Carlos Jimenez, Alexander Wettig, Kilian Lieret, Shubham Yao, Karthik Narasimhan, and Ofir Press. Swe-agent: Agent-computer interfaces enable automated software engineering. In *Advances in Neural Information Processing Systems*, volume 37, pages 50528–50652, 2024.

> Para. 18[CN]: [52] John Yang, Carlos Jimenez, Alexander Wettig, Kilian Lieret, Shubham Yao, Karthik Narasimhan, and Ofir Press. Swe-agent：智能体—计算机接口实现自动化软件工程。载于 *Advances in Neural Information Processing Systems*，第 37 卷，第 50528–50652 页，2024。

> Para. 19: [53] Lihe Yang, Bingyi Kang, Zilong Huang, Zhen Zhao, Xiaogang Xu, Jiashi Feng, and Hengshuang Zhao. Depth anything v2. In *Advances in Neural Information Processing Systems*, volume 37, pages 21875–21911, 2024.

> Para. 19[CN]: [53] Lihe Yang, Bingyi Kang, Zilong Huang, Zhen Zhao, Xiaogang Xu, Jiashi Feng, and Hengshuang Zhao. Depth anything v2。载于 *Advances in Neural Information Processing Systems*，第 37 卷，第 21875–21911 页，2024。

> ---

> ## Page 14 / 第 14 页

> Para. 20: [54] Sihan Yang, Runsen Xu, Yiman Xie, Sizhe Yang, Mo Li, Jingli Lin, Chenming Zhu, Xiaochen Chen, Haodong Duan, Xiangyu Yue, et al. Mmsi-bench: A benchmark for multi-image spatial intelligence. *arXiv preprint arXiv:2505.23764*, 2025.

> Para. 20[CN]: [54] Sihan Yang, Runsen Xu, Yiman Xie, Sizhe Yang, Mo Li, Jingli Lin, Chenming Zhu, Xiaochen Chen, Haodong Duan, Xiangyu Yue, 等。Mmsi-bench：多图像空间智能基准。*arXiv 预印本 arXiv:2505.23764*，2025。

> Para. 21: [55] Zhejian Yang, Yongchao Chen, Xueyang Zhou, Jiangyue Yan, Dingjie Song, Yinuo Liu, Yuting Li, Yu Zhang, Pan Zhou, Hechang Chen, et al. Agentic robot: A brain-inspired framework for vision-language-action models in embodied agents. *arXiv preprint arXiv:2505.23450*, 2025.

> Para. 21[CN]: [55] Zhejian Yang, Yongchao Chen, Xueyang Zhou, Jiangyue Yan, Dingjie Song, Yinuo Liu, Yuting Li, Yu Zhang, Pan Zhou, Hechang Chen, 等。Agentic robot：用于具身智能体视觉—语言—动作模型的脑启发框架。*arXiv 预印本 arXiv:2505.23450*，2025。

> Para. 22: [56] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React: Synergizing reasoning and acting in language models. *arXiv preprint arXiv:2210.03629*, 2022.

> Para. 22[CN]: [56] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. React：在语言模型中协同推理与行动。*arXiv 预印本 arXiv:2210.03629*，2022。

> Para. 23: [57] Baiqiao Yin, Qineng Wang, Pingyue Zhang, Jianshu Zhang, Kangrui Wang, Zihan Wang, Jieyu Zhang, Keshigeyan Chandrasegaran, Han Liu, Ranjay Krishna, et al. Spatial mental modeling from limited views. In *Structural Priors for Vision Workshop at ICCV’25*, 2025.

> Para. 23[CN]: [57] Baiqiao Yin, Qineng Wang, Pingyue Zhang, Jianshu Zhang, Kangrui Wang, Zihan Wang, Jieyu Zhang, Keshigeyan Chandrasegaran, Han Liu, Ranjay Krishna, 等。从有限视角进行空间心智建模。载于 *ICCV’25 视觉结构先验研讨会*，2025。

> Para. 24: [58] Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system at scale. In *Advances in Neural Information Processing Systems*, volume 38, pages 113222–113244, 2025.

> Para. 24[CN]: [58] Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian Fan, Gaohong Liu, Lingjun Liu, 等。Dapo：大规模开源 LLM 强化学习系统。载于 *Advances in Neural Information Processing Systems*，第 38 卷，第 113222–113244 页，2025。

> Para. 25: [59] Aohan Zeng, Xin Lv, Zhenyu Hui, Zhengxiao Du, Qinkai Zheng, Bin Chen, Da Yin, Chendi Ge, Changhai Huang, Chengxing Xie, et al. Glm-5: from vibe coding to agentic engineering. *arXiv preprint arXiv:2602.15763*, 2026.

> Para. 25[CN]: [59] Aohan Zeng, Xin Lv, Zhenyu Hui, Zhengxiao Du, Qinkai Zheng, Bin Chen, Da Yin, Chendi Ge, Changhai Huang, Chengxing Xie, 等。Glm-5：从氛围编码到智能体工程。*arXiv 预印本 arXiv:2602.15763*，2026。

> Para. 26: [60] Yixian Zhang, Huanming Zhang, Feng Gao, Xiao Li, Zhihao Liu, Chunyang Zhu, Jiaxing Qiu, Yuchen Yan, Jiyuan Liu, Wenhao Tang, et al. Harness vla: Steering frozen vlas into reliable manipulation primitives via memory-guided agents. *arXiv preprint arXiv:2607.08448*, 2026.

> Para. 26[CN]: [60] Yixian Zhang, Huanming Zhang, Feng Gao, Xiao Li, Zhihao Liu, Chunyang Zhu, Jiaxing Qiu, Yuchen Yan, Jiyuan Liu, Wenhao Tang, 等。Harness vla：通过记忆引导的智能体将冻结的 VLA 引导为可靠的操作原语。*arXiv 预印本 arXiv:2607.08448*，2026。

> Para. 27: [61] Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, and Yu Su. Gpt-4v (ision) is a generalist web agent, if grounded. *arXiv preprint arXiv:2401.01614*, 2024.

> Para. 27[CN]: [61] Boyuan Zheng, Boyu Gou, Jihyung Kil, Huan Sun, and Yu Su. 如果得到定位，Gpt-4v（ision）就是一个通用网络智能体。*arXiv 预印本 arXiv:2401.01614*，2024。

> Para. 28: [62] Enshen Zhou, Jingkun An, Cheng Chi, Yi Han, Shanyu Rong, Chi Zhang, Pengwei Wang, Zhongyuan Wang, Tiejun Huang, Lu Sheng, et al. Roborefer: Towards spatial referring with reasoning in vision-language models for robotics. In *Advances in Neural Information Processing Systems*, volume 38, pages 28404–28481, 2025.

> Para. 28[CN]: [62] Enshen Zhou, Jingkun An, Cheng Chi, Yi Han, Shanyu Rong, Chi Zhang, Pengwei Wang, Zhongyuan Wang, Tiejun Huang, Lu Sheng, 等。Roborefer：迈向机器人视觉—语言模型中带推理的空间指代。载于 *Advances in Neural Information Processing Systems*，第 38 卷，第 28404–28481 页，2025。

> Para. 29: [63] Brianna Zitkovich, Tianhe Yu, Sichun Xu, Peng Xu, Ted Xiao, Fei Xia, Jialin Wu, Paul Wohlhart, Stefan Welker, Ayzaan Wahid, et al. Rt-2: Vision-language-action models transfer web knowledge to robotic control. In *Conference on Robot Learning*, pages 2165–2183. PMLR, 2023.

> Para. 29[CN]: [63] Brianna Zitkovich, Tianhe Yu, Sichun Xu, Peng Xu, Ted Xiao, Fei Xia, Jialin Wu, Paul Wohlhart, Stefan Welker, Ayzaan Wahid, 等。Rt-2：视觉—语言—动作模型将网络知识迁移到机器人控制。载于 *机器人学习会议*，第 2165–2183 页。PMLR，2023。

> ---

> ## Page 15 / 第 15 页

> # Appendix

> # 附录

> ## Table of Contents

> ## 目录

> | Entry | Page |
> |---|---:|
> | A　Algorithm Pseudocode | 17 |
> | B　Detailed Experimental Settings | 18 |
> | B.1　Detailed Training Settings | 18 |
> | B.2　Detailed Evaluation Settings | 19 |
> | B.3　Hardware and Software Environment | 20 |
> | C　SpatialCLI-Bench | 20 |
> | C.1　Scope and Sample Format | 20 |
> | C.2　Data Provenance and Composition | 20 |
> | C.3　Capability Composition and Oracle Plans | 20 |
> | C.4　Multi-Stage Construction Pipeline | 21 |
> | C.5　Independent Human Review and Filtering Yield | 21 |
> | D　Spatial Tool Interfaces and Implementation | 21 |
> | D.1　Coordinate and Serialization Convention | 21 |
> | D.2　Spatial Tool Interfaces | 22 |
> | E　Capability Internalization Metric | 27 |
> | E.1　Evaluation Data and Capability Coverage | 27 |
> | E.2　Reference Construction and Evaluation Protocol | 27 |
> | E.3　Independent Human Verification | 27 |
> | E.4　Similarity Functions and Aggregation | 27 |
> | F　Additional Experiments | 29 |
> | F.1　Comparison with Direct Fine-Tuning | 29 |
> | F.2　Tool-Set Ablation | 30 |
> | F.3　Tool-Use Behavior across Internalization Variants | 31 |
> | F.4　Sensitivity to the Tool-Use View Loss Weight | 31 |
> | G　Prompt Templates | 32 |
> | G.1　Agentic Tool-Use Prompt Template | 32 |
> | G.2　Turn-Wise Evidence Consolidation Prompt | 32 |
> | G.3　Global Trajectory Verbalization Prompt | 34 |

> | 条目 | 页码 |
> |---|---:|
> | A　算法伪代码 | 17 |
> | B　详细实验设置 | 18 |
> | B.1　详细训练设置 | 18 |
> | B.2　详细评估设置 | 19 |
> | B.3　硬件与软件环境 | 20 |
> | C　SpatialCLI-Bench | 20 |
> | C.1　范围与样本格式 | 20 |
> | C.2　数据来源与构成 | 20 |
> | C.3　能力构成与预言机计划 | 20 |
> | C.4　多阶段构建流程 | 21 |
> | C.5　独立人工审查与过滤产出率 | 21 |
> | D　空间工具接口与实现 | 21 |
> | D.1　坐标与序列化约定 | 21 |
> | D.2　空间工具接口 | 22 |
> | E　能力内化度量 | 27 |
> | E.1　评估数据与能力覆盖 | 27 |
> | E.2　参考构建与评估协议 | 27 |
> | E.3　独立人工验证 | 27 |
> | E.4　相似度函数与聚合 | 27 |
> | F　附加实验 | 29 |
> | F.1　与直接微调的比较 | 29 |
> | F.2　工具集消融 | 30 |
> | F.3　不同内化变体的工具使用行为 | 31 |
> | F.4　对工具使用视图损失权重的敏感性 | 31 |
> | G　提示模板 | 32 |
> | G.1　智能体式工具使用提示模板 | 32 |
> | G.2　逐轮证据整合提示 | 32 |
> | G.3　全局轨迹语言化提示 | 34 |

> ---

> ## Page 16 / 第 16 页

> | Entry | Page |
> |---|---:|
> | H　Case Studies | 35 |
> | H.1　Case 1: Two-Image Camera Rotation and Depth | 35 |
> | H.2　Case 2: Two-Image Camera Translation and Instance Segmentation | 38 |
> | H.3　Case 3: SpatialCLI-8B after Capability Internalization | 43 |

> | 条目 | 页码 |
> |---|---:|
> | H　案例研究 | 35 |
> | H.1　案例 1：双图像相机旋转与深度 | 35 |
> | H.2　案例 2：双图像相机平移与实例分割 | 38 |
> | H.3　案例 3：能力内化后的 SpatialCLI-8B | 43 |

> ---

> ## Page 17 / 第 17 页

> # A　Algorithm Pseudocode

> # A　算法伪代码

> Para. 30: Algorithm 1 summarizes the complete Call–Learn–Internalize procedure. Here, Interact$(\pi,x,\mathcal U,B)$ runs the ReAct agent with tools $\mathcal U$ and call budget $B$, returning $\xi=(I,q,\tau,y)$; $\tau$ records each call’s reasoning, action, and observation, while $\xi$ retains complete assistant responses, including terminal reasoning. Tool outputs are context only, and SFT minimizes mean negative log-likelihood over model-generated tokens.

> Para. 30[CN]: 算法 1 总结了完整的“调用—学习—内化”过程。这里，Interact$(\pi,x,\mathcal U,B)$ 使用工具 $\mathcal U$ 和调用预算 $B$ 运行 ReAct 智能体，并返回 $\xi=(I,q,\tau,y)$；$\tau$ 记录每次调用的推理、动作和观察，而 $\xi$ 保留完整的助手响应，包括终止推理。工具输出仅作为上下文，SFT 在模型生成的词元上最小化平均负对数似然。

> ### Algorithm 1: SpatialCLI: Call–Learn–Internalize

> ### 算法 1：SpatialCLI：调用—学习—内化

> ```text
> Require: Initial policy π₀; teacher policy π_teacher; shared task pool 𝒟; RL subset 𝒟_RL; spatial tools 𝒰; executed-
>          call budget B; Tool-Use View weight λ
> Ensure: Trained SpatialCLI policy π_θ
>  1: Call: Register 𝒰 = {LOCATE, SEGMENT, DEPTH, POSE} in the live agent loop.
>  2: Define Interact(π, x, 𝒰, B) for x = (I, q, y*) as follows; y* is not exposed to π:
>  3:     Initialize the complete history ℋ ← (P_𝒰, I, q), trace τ ← (), and executed-call count k ← 0, where P_𝒰
>         is the shared agentic prompt with the registrations of 𝒰.
>  4: while k < B do
>  5:     Sample the next complete assistant response r = (z, u) ∼ π(· | ℋ).
>  6:     if u is a terminal answer y then
>  7:         Append r to ℋ.
>  8:         return The serialized interaction ξ = (I, q, τ, y).
>  9:     end if
> 10:     Parse u as the next tool call a_{k+1}, execute o_{k+1} ← 𝒰(a_{k+1}), and set k ← k + 1.
> 11:     Append (z, a_k, o_k) to τ and append the complete response r, observation o_k, and budget notice for
>         B − k remaining calls to ℋ; use the budget-exhausted instruction when B − k = 0.
> 12: end while
> 13: Sample a terminal response r = (z_term, y) ∼ π(· | ℋ) with tool calls disabled and append r to ℋ.
> 14: return The serialized interaction ξ = (I, q, τ, y).
> 15: Learn—Cold-Start SFT: D̃_SFT ← {Interact(π_teacher, x, 𝒰, B) : x = (I, q, y*) is sampled from 𝒟}.
> 16: 𝒟_SFT ← {ξ ∈ D̃_SFT : valid call format, successful tool execution, and y = y*}.
> 17: π_SFT ← SFT(π₀, 𝒟_SFT) on reasoning, tool-call, and final-answer tokens.
> 18: Learn—Agentic RL: Initialize π_θ ← π_SFT.
> 19: for each agentic RL update do
> 20:     Sample x = (I, q, y*) ∼ 𝒟_RL.
> 21:     Set θ_old ← θ.
> 22:     Sample {ξ_i}_{i=1}^G ∼ μ_{θ_old}(· | I, q) through Interact(π_{θ_old}, x, 𝒰, B).
> 23:     for i = 1, …, G do
> 24:         Set R_i ← V(y_i, y*) from the final answer of ξ_i.
> 25:     end for
> 26:     Update θ by maximizing J_GRPO(θ) in Equation (1).
> 27: end for
> 28: Set π_RL ← π_θ.
> 29: Internalize: Collect successful ξ = Interact(π_RL, x, 𝒰, B) with y = y* for tasks x ∈ 𝒟.
> 30: Initialize 𝒟_internal ← ∅ and 𝒟_agentic ← ∅.
> 31: for each collected ξ = (I, q, τ, y*), where τ = ((z_t, a_t, o_t)_{t=1}^T) do
> 32:     Set e_{<1} ← ∅.
> 33:     for t = 1, …, T do
> 34:         e_t ← Ψ_ext(I, q, e_{<t}, z_t, a_t, o_t); set e_{<t+1} ← (e₁, …, e_t).
> 35:     end for
> 36:     Set E_τ ← (e₁, …, e_T) and c ← Φ_verb(I, q, E_τ, y*).
> 37:     Add the direct-answer sample ((I, q), (c, y*)) to 𝒟_internal.
> 38:     Add the original interaction ξ to 𝒟_agentic, masking all returned tool outputs from the loss.
> 39: end for
> 40: Initialize π_θ ← π_RL and minimize ℒ_CI = ℒ_internal + λℒ_agentic on 𝒟_internal and 𝒟_agentic.
> 41: return π_θ
> ```

> ```text
> 要求：初始策略 π₀；教师策略 π_teacher；共享任务池 𝒟；RL 子集 𝒟_RL；空间工具 𝒰；已执行调用预算 B；
>       工具使用视图权重 λ
> 保证：训练后的 SpatialCLI 策略 π_θ
>  1：调用：在实时智能体循环中注册 𝒰 = {LOCATE, SEGMENT, DEPTH, POSE}。
>  2：对 x = (I, q, y*) 定义 Interact(π, x, 𝒰, B) 如下；y* 不向 π 暴露：
>  3：    初始化完整历史 ℋ ← (P_𝒰, I, q)、轨迹 τ ← () 和已执行调用计数 k ← 0，其中 P_𝒰
>         是包含 𝒰 注册信息的共享智能体提示。
>  4：当 k < B 时执行
>  5：    采样下一个完整助手响应 r = (z, u) ∼ π(· | ℋ)。
>  6：    如果 u 是终止答案 y，则
>  7：        将 r 追加到 ℋ。
>  8：        返回序列化交互 ξ = (I, q, τ, y)。
>  9：    结束如果
> 10：    将 u 解析为下一个工具调用 a_{k+1}，执行 o_{k+1} ← 𝒰(a_{k+1})，并令 k ← k + 1。
> 11：    将 (z, a_k, o_k) 追加到 τ，并将完整响应 r、观察 o_k 以及关于剩余 B − k 次调用的预算通知
>         追加到 ℋ；当 B − k = 0 时使用预算耗尽指令。
> 12：结束循环
> 13：在禁用工具调用的情况下采样终止响应 r = (z_term, y) ∼ π(· | ℋ)，并将 r 追加到 ℋ。
> 14：返回序列化交互 ξ = (I, q, τ, y)。
> 15：学习——冷启动 SFT：D̃_SFT ← {Interact(π_teacher, x, 𝒰, B)：x = (I, q, y*) 从 𝒟 中采样}。
> 16：𝒟_SFT ← {ξ ∈ D̃_SFT：调用格式有效、工具执行成功且 y = y*}。
> 17：π_SFT ← SFT(π₀, 𝒟_SFT)，作用于推理、工具调用和最终答案词元。
> 18：学习——智能体 RL：初始化 π_θ ← π_SFT。
> 19：对每次智能体 RL 更新执行
> 20：    采样 x = (I, q, y*) ∼ 𝒟_RL。
> 21：    令 θ_old ← θ。
> 22：    通过 Interact(π_{θ_old}, x, 𝒰, B) 采样 {ξ_i}_{i=1}^G ∼ μ_{θ_old}(· | I, q)。
> 23：    对 i = 1, …, G 执行
> 24：        根据 ξ_i 的最终答案令 R_i ← V(y_i, y*)。
> 25：    结束循环
> 26：    通过最大化式（1）中的 J_GRPO(θ) 更新 θ。
> 27：结束循环
> 28：令 π_RL ← π_θ。
> 29：内化：对于任务 x ∈ 𝒟，收集满足 y = y* 的成功交互 ξ = Interact(π_RL, x, 𝒰, B)。
> 30：初始化 𝒟_internal ← ∅ 和 𝒟_agentic ← ∅。
> 31：对每个收集到的 ξ = (I, q, τ, y*) 执行，其中 τ = ((z_t, a_t, o_t)_{t=1}^T)
> 32：    令 e_{<1} ← ∅。
> 33：    对 t = 1, …, T 执行
> 34：        e_t ← Ψ_ext(I, q, e_{<t}, z_t, a_t, o_t)；令 e_{<t+1} ← (e₁, …, e_t)。
> 35：    结束循环
> 36：    令 E_τ ← (e₁, …, e_T)，并令 c ← Φ_verb(I, q, E_τ, y*)。
> 37：    将直接回答样本 ((I, q), (c, y*)) 添加到 𝒟_internal。
> 38：    将原始交互 ξ 添加到 𝒟_agentic，并从损失中屏蔽所有返回的工具输出。
> 39：结束循环
> 40：初始化 π_θ ← π_RL，并在 𝒟_internal 和 𝒟_agentic 上最小化
>     ℒ_CI = ℒ_internal + λℒ_agentic。
> 41：返回 π_θ
> ```

> ---

> ## Page 18 / 第 18 页

> # B　Detailed Experimental Settings

> # B　详细实验设置

> ## B.1　Detailed Training Settings

> ## B.1　详细训练设置

> Para. 31: **Initial Models.** We conduct training on Qwen3.5-27B [35], Qwen3.6-35B-A3B [35], and Qwen3-VL-8B-Instruct [1] as the initial models. All final models in the SpatialCLI series are obtained from their respective initial models through the same sequence of Cold-Start SFT, agentic RL, and trajectory-guided capability internalization.

> Para. 31[CN]: **初始模型。** 我们以 Qwen3.5-27B [35]、Qwen3.6-35B-A3B [35] 和 Qwen3-VL-8B-Instruct [1] 作为初始模型进行训练。SpatialCLI 系列中的所有最终模型，均由各自的初始模型经过相同的冷启动 SFT、智能体 RL 和轨迹引导的能力内化序列获得。

> Para. 32: **Training Data.** All three stages draw their stage-specific samples from a shared pool of 37,000 training tasks: 5,000 from Vlaser [50], 10,000 from MindCube-Train [57], 10,000 from BOPASK-Trajectory, 10,000 from BOPASK-Object-Rearrangement [2], and 2,000 from RefSpatial [62]. We select these sources for their complementary spatial supervision: Vlaser contributes embodied question answering and grounding, MindCube-Train contributes multi-view spatial reasoning, the two BOPASK subsets contribute interaction-centric trajectory planning and object rearrangement, and RefSpatial contributes diverse 2D and 3D spatial referring. Together, they cover single- and multi-image inputs as well as localization, depth, pose, trajectory, and rearrangement reasoning. For Cold-Start SFT, we use Qwen3.5-397B-A17B [35] as the teacher model, equip it with the live agent loop described above, and sample approximately 5,000 tasks from this pool for tool-interaction annotation. After filtering invalid tool-call formats, failed tool executions, and incorrect final answers, we retain approximately 40% as high-quality correct trajectories, yielding approximately 2,000 SFT trajectories. Agentic RL samples approximately 10,000 tasks from the same shared pool while explicitly excluding all tasks used for Cold-Start SFT. Capability internalization uses approximately 42,000 successful tool-use trajectories collected by rolling out SpatialCLI-RL on tasks from this pool. Both the turn-wise evidence consolidator and the global trajectory verbalizer use Qwen3.5-397B-A17B, with the same sampling and maximum-generation-length parameters as the evaluation configuration in Section B.2. Because trajectory verbalization succeeds for nearly all retained trajectories, each trajectory produces one Capability-Internalization View sample and one Tool-Use View sample, yielding approximately 84,000 view-specific training samples. We ensure that the training data have no textual or visual overlap with any benchmark evaluated in this work and therefore pose no risk of text or image leakage into evaluation.

> Para. 32[CN]: **训练数据。** 三个阶段均从一个包含 37,000 个训练任务的共享池中抽取各阶段专用样本：5,000 个来自 Vlaser [50]，10,000 个来自 MindCube-Train [57]，10,000 个来自 BOPASK-Trajectory，10,000 个来自 BOPASK-Object-Rearrangement [2]，另有 2,000 个来自 RefSpatial [62]。我们选择这些来源，是因为它们提供了互补的空间监督：Vlaser 提供具身问答与定位，MindCube-Train 提供多视图空间推理，两个 BOPASK 子集提供以交互为中心的轨迹规划与物体重排，而 RefSpatial 提供多样化的二维和三维空间指代。它们共同覆盖单图像与多图像输入，以及定位、深度、位姿、轨迹和重排推理。对于冷启动 SFT，我们使用 Qwen3.5-397B-A17B [35] 作为教师模型，为其配备上述实时智能体循环，并从该池中抽取约 5,000 个任务进行工具交互标注。在过滤无效的工具调用格式、失败的工具执行和错误的最终答案后，我们保留约 40% 作为高质量正确轨迹，从而得到约 2,000 条 SFT 轨迹。智能体 RL 从同一个共享池中抽取约 10,000 个任务，同时明确排除所有用于冷启动 SFT 的任务。能力内化使用约 42,000 条成功的工具使用轨迹，这些轨迹通过在该池任务上运行 SpatialCLI-RL 收集。逐轮证据整合器和全局轨迹语言化器均使用 Qwen3.5-397B-A17B，其采样参数和最大生成长度参数与 B.2 节中的评估配置相同。由于几乎所有保留轨迹的轨迹语言化都能成功，因此每条轨迹产生一个“能力内化视图”样本和一个“工具使用视图”样本，从而得到约 84,000 个视图专用训练样本。我们确保训练数据与本工作评估的任何基准均不存在文本或视觉重叠，因此不会造成文本或图像泄漏到评估中的风险。

> Para. 33: **Agentic RL Objective.** For each task $x=(I,q,y^*)\sim\mathcal D_{\mathrm{RL}}$, the old policy $\pi_{\theta_{\mathrm{old}}}$ samples a group of $G$ complete interactions $\{\xi_i\}_{i=1}^{G}$ through live interaction with the spatial tools, and a task verifier assigns each interaction the outcome reward $R_i=V(y_i,y^*)$. Most training tasks are multiple-choice questions, for which a deterministic parser extracts the final answer choice and assigns reward 1 if it matches the ground truth and 0 otherwise. For BOPASK-Trajectory and BOPASK-Object-Rearrangement, we directly use the per-sample point-set score defined in Equation (3) as the trajectory reward. We maximize the GRPO [39] objective using the asymmetric Clip-Higher bounds and token-level policy-gradient reduction from DAPO [58]:

> Para. 33[CN]: **智能体 RL 目标。** 对于每个任务 $x=(I,q,y^*)\sim\mathcal D_{\mathrm{RL}}$，旧策略 $\pi_{\theta_{\mathrm{old}}}$ 通过与空间工具实时交互，采样一组 $G$ 个完整交互 $\{\xi_i\}_{i=1}^{G}$，任务验证器则为每个交互分配结果奖励 $R_i=V(y_i,y^*)$。大多数训练任务是多项选择题；对于这些任务，确定性解析器提取最终答案选项，如果其与真实答案匹配则分配奖励 1，否则分配 0。对于 BOPASK-Trajectory 和 BOPASK-Object-Rearrangement，我们直接使用式（3）中定义的逐样本点集分数作为轨迹奖励。我们使用非对称 Clip-Higher 边界和来自 DAPO [58] 的词元级策略梯度归约来最大化 GRPO [39] 目标：

> $J_{\mathrm{GRPO}}(\theta) = \mathbb{E}_{x\sim\mathcal D_{\mathrm{RL}},\{\xi_i\}_{i=1}^{G}\sim\pi_{\theta_{\mathrm{old}}}(\cdot\mid I,q)} \left[ \frac{1}{\sum_{i=1}^{G}|T_i|} \sum_{i=1}^{G}\sum_{\ell\in T_i} \min\!\left( \rho_{i,\ell}(\theta)\hat A_{i,\ell}, \operatorname{clip}\!\left(\rho_{i,\ell}(\theta),1-\epsilon_{\mathrm{low}},1+\epsilon_{\mathrm{high}}\right)\hat A_{i,\ell} \right) \right]. \tag{1}$

> Para. 34: Here, $\mu_{\theta_{\mathrm{old}}}$ is the rollout distribution induced by the old policy and tool execution, and $T_i$ contains only model-generated token positions in $\xi_i$—reasoning, tool calls, and the final answer—excluding returned tool outputs. For model-generated token $w_{i,\ell}$ with interaction history $h_{i,\ell}$, the token-level importance ratio is $\rho_{i,\ell}(\theta)=\pi_\theta(w_{i,\ell}\mid I,q,h_{i,\ell})/\pi_{\theta_{\mathrm{old}}}(w_{i,\ell}\mid I,q,h_{i,\ell})$. The trajectory-level reward is broadcast to every model-generated token in the same interaction. The resulting group-relative advantage is

> Para. 34[CN]: 这里，$\mu_{\theta_{\mathrm{old}}}$ 是由旧策略和工具执行诱导的 rollout 分布，而 $T_i$ 仅包含 $\xi_i$ 中由模型生成的词元位置——推理、工具调用和最终答案——不包括返回的工具输出。对于具有交互历史 $h_{i,\ell}$ 的模型生成词元 $w_{i,\ell}$，词元级重要性比率为 $\rho_{i,\ell}(\theta)=\pi_\theta(w_{i,\ell}\mid I,q,h_{i,\ell})/\pi_{\theta_{\mathrm{old}}}(w_{i,\ell}\mid I,q,h_{i,\ell})$。轨迹级奖励被广播到同一交互中的每个模型生成词元。由此得到的组相对优势为

> $\hat A_{i,\ell} = \frac{R_i-\operatorname{mean}(\{R_j\}_{j=1}^{G})} {\operatorname{std}(\{R_j\}_{j=1}^{G})}, \qquad \ell\in T_i. \tag{2}$

> Para. 35: **Training Configurations.** Tables 4 and 5 summarize the configurations shared by Cold-Start SFT and capability internalization, and the agentic RL configuration, respectively. The three initial models use the same hyperparameters. Cold-Start SFT and capability internalization both use full-parameter fine-tuning. Capability internalization uses the same settings as Cold-Start SFT, with the Tool-Use View loss weight set to $\lambda=0.5$. Training uses a fixed random seed of 42.

> Para. 35[CN]: **训练配置。** 表 4 和表 5 分别总结了冷启动 SFT 与能力内化共享的配置，以及智能体 RL 配置。三个初始模型使用相同的超参数。冷启动 SFT 和能力内化均采用全参数微调。能力内化使用与冷启动 SFT 相同的设置，并将工具使用视图损失权重设为 $\lambda=0.5$。训练使用固定随机种子 42。

> ---

> ## Page 19 / 第 19 页

> | Category | Configuration |
> |---|---|
> | Optimization | Optimizer: AdamW<br>Weight Decay: 0.1<br>Learning Rate: $2\times10^{-5}$<br>LR Scheduler: Cosine<br>Warmup Steps: 10 |
> | Training | Fine-Tuning Method: Full-Parameter<br>Batch Size: 64<br>Context Length: 32768<br>Epochs: 2 |

> | 类别 | 配置 |
> |---|---|
> | 优化 | 优化器：AdamW<br>权重衰减：0.1<br>学习率：$2\times10^{-5}$<br>学习率调度器：Cosine<br>预热步数：10 |
> | 训练 | 微调方法：全参数<br>批大小：64<br>上下文长度：32768<br>轮数：2 |

> Para. 36: **Table 4**　Training configuration shared by Cold-Start SFT and capability internalization.

> Para. 36[CN]: **表 4**　冷启动 SFT 与能力内化共享的训练配置。

> | Category | Configuration |
> |---|---|
> | Algorithm | RL Algorithm: GRPO<br>Group Size: 8<br>Clip Ratio Low: 0.20<br>Clip Ratio High: 0.28<br>Dual-Clip C: 3.0<br>Entropy Coef: 0<br>KL Loss Coef: 0<br>Loss Aggregation: Token Mean |
> | Rollout | Maximum Input Length: 32768<br>Maximum Output Length: 32768<br>Tool-Call Budget: 10<br>Temperature: 1.0<br>Top-P: 1.0<br>Top-K: −1<br>Rollout Precision: FP16 |
> | Training | Training Batch Size: 128<br>Mini Batch Size: 32<br>Optimizer: AdamW<br>Learning Rate: $1\times10^{-6}$<br>Weight Decay: 0.01<br>Gradient Clip: 1.0<br>Training Precision: FP16 |

> | 类别 | 配置 |
> |---|---|
> | 算法 | RL 算法：GRPO<br>组大小：8<br>低截断比率：0.20<br>高截断比率：0.28<br>Dual-Clip C：3.0<br>熵系数：0<br>KL 损失系数：0<br>损失聚合：词元均值 |
> | Rollout | 最大输入长度：32768<br>最大输出长度：32768<br>工具调用预算：10<br>温度：1.0<br>Top-P：1.0<br>Top-K：−1<br>Rollout 精度：FP16 |
> | 训练 | 训练批大小：128<br>小批大小：32<br>优化器：AdamW<br>学习率：$1\times10^{-6}$<br>权重衰减：0.01<br>梯度裁剪：1.0<br>训练精度：FP16 |

> Para. 37: **Table 5**　Agentic RL training configuration.

> Para. 37[CN]: **表 5**　智能体 RL 训练配置。

> ## B.2　Detailed Evaluation Settings

> ## B.2　详细评估设置

> Para. 38: **Evaluation Benchmarks.** We evaluate SpatialCLI on SpatialCLI-Bench, MindCube [57], selected subsets of MMSI [54], DA-2K [53], and selected subsets of BOPASK [2]. Specifically, we use Motion-Cam and Pos-Cam from MMSI and Trajectory and Object-Rearrangement from BOPASK. For the two BOPASK subsets, we use the same continuous point-set score during agentic RL and evaluation. Model outputs and references express 2D points on a 0–999 image-coordinate scale; before scoring, we divide both coordinates by 1000. Let $\hat{\mathcal P}$ and $\mathcal P^*$ be the resulting predicted and reference point sets. Their symmetric Chamfer distance and per-sample score are

> Para. 38[CN]: **评估基准。** 我们在 SpatialCLI-Bench、MindCube [57]、MMSI [54] 的选定子集、DA-2K [53] 以及 BOPASK [2] 的选定子集上评估 SpatialCLI。具体而言，我们使用 MMSI 中的 Motion-Cam 和 Pos-Cam，以及 BOPASK 中的 Trajectory 和 Object-Rearrangement。对于两个 BOPASK 子集，我们在智能体 RL 和评估期间使用相同的连续点集分数。模型输出和参考答案以 0–999 的图像坐标尺度表示二维点；在评分之前，我们将两个坐标均除以 1000。令 $\hat{\mathcal P}$ 和 $\mathcal P^*$ 分别为所得预测点集和参考点集。其对称 Chamfer 距离和逐样本分数为

> $d_{\mathrm{CD}}(\hat{\mathcal P},\mathcal P^*) = \frac{1}{2} \left[ \frac{1}{|\hat{\mathcal P}|} \sum_{\hat p\in\hat{\mathcal P}} \min_{p^*\in\mathcal P^*}\|\hat p-p^*\|_2 + \frac{1}{|\mathcal P^*|} \sum_{p^*\in\mathcal P^*} \min_{\hat p\in\hat{\mathcal P}}\|p^*-\hat p\|_2 \right],$

> $s_{\mathrm{BOPASK}}(\hat{\mathcal P},\mathcal P^*) = \max\left( 0,\, 1-\frac{d_{\mathrm{CD}}(\hat{\mathcal P},\mathcal P^*)}{0.15} \right). \tag{3}$

> Para. 39: If an output contains no valid predicted points, its per-sample score is zero. For each BOPASK subset, we report the mean per-sample score as a percentage. Under w/o Tools inference, no tools are registered and no system prompt is inserted; under w/ Tools inference, all evaluated models are provided with the same four spatial tools used to train SpatialCLI. We parse final answers with benchmark-specific deterministic parsers

> Para. 39[CN]: 如果输出不包含有效预测点，则其逐样本分数为零。对于每个 BOPASK 子集，我们将逐样本平均分数以百分比报告。在 w/o Tools 推理下，不注册任何工具，也不插入系统提示；在 w/ Tools 推理下，所有被评估模型均获得与训练 SpatialCLI 时使用的相同四种空间工具。我们使用特定于基准的确定性解析器解析最终答案

> ---

> ## Page 20 / 第 20 页

> Para. 40: and treat malformed or missing final answers as incorrect.

> Para. 40[CN]: 并将格式错误或缺失的最终答案视为错误答案。

> Para. 41: **Evaluation Configurations.** Unless a benchmark requires a different official setting, we use temperature 1.0, top-p 0.95, top-k 20, min-p 0.0, a presence penalty of 1.5, a repetition penalty of 1.0, and a maximum generation length of 40,960 tokens. All task-performance evaluations permit at most ten tool calls per sample. We report the mean over three evaluation runs, without fixing evaluation seeds.

> Para. 41[CN]: **评估配置。** 除非某个基准要求不同的官方设置，否则我们使用温度 1.0、top-p 0.95、top-k 20、min-p 0.0、存在惩罚 1.5、重复惩罚 1.0，以及 40,960 个词元的最大生成长度。所有任务性能评估允许每个样本最多调用十次工具。我们报告三次评估运行的平均值，且不固定评估种子。

> ## B.3　Hardware and Software Environment

> ## B.3　硬件与软件环境

> Para. 42: All experiments were conducted on a cluster whose nodes were equipped with 184 Intel Xeon CPU cores, 1.8 TiB of system memory, and 16 IPU-ZW810E accelerators, each with approximately 96 GiB of device memory. Both SFT and RL used four nodes. The software environment used Ubuntu 24.04.2 LTS, a CUDA 12.9-compatible toolchain, Python 3.12.3, PyTorch 2.9.0, Transformers 5.5.4, vLLM 0.18.0+ppu2.0.0, verl 0.9.0.dev0, and Ray 2.49.2.

> Para. 42[CN]: 所有实验均在一个集群上进行，其节点配备 184 个 Intel Xeon CPU 核心、1.8 TiB 系统内存和 16 个 IPU-ZW810E 加速器，每个加速器具有约 96 GiB 设备内存。SFT 和 RL 均使用四个节点。软件环境使用 Ubuntu 24.04.2 LTS、兼容 CUDA 12.9 的工具链、Python 3.12.3、PyTorch 2.9.0、Transformers 5.5.4、vLLM 0.18.0+ppu2.0.0、verl 0.9.0.dev0 和 Ray 2.49.2。

> # C　SpatialCLI-Bench

> # C　SpatialCLI-Bench

> ## C.1　Scope and Sample Format

> ## C.1　范围与样本格式

> Para. 43: SpatialCLI-Bench is a 516-example English six-choice visual question answering benchmark for evaluating tool-grounded compositional spatial reasoning. Each example contains one or two images, one question, and six answer choices with a unique correct answer. Each example has a private executable oracle tool plan of at most five steps, which is used for construction and auditing but is not exposed in the public question. Every example jointly evaluates at least two of three capability groups: grounding and 2D region relations (G), metric depth (D), and object pose or cross-view camera motion (P).

> Para. 43[CN]: SpatialCLI-Bench 是一个包含 516 个样例的英文六选一视觉问答基准，用于评估以工具为基础的组合式空间推理。每个样例包含一幅或两幅图像、一个问题和六个答案选项，并且只有一个正确答案。每个样例都有一个私有、可执行且最多包含五个步骤的预言机工具计划，该计划用于构建和审计，但不在公开问题中暴露。每个样例联合评估三个能力组中的至少两个：定位与二维区域关系（G）、度量深度（D），以及物体位姿或跨视图相机运动（P）。

> ## C.2　Data Provenance and Composition

> ## C.2　数据来源与构成

> Para. 44: Every example has a unique candidate ID and a unique upstream visual-source ID. No complete visual unit is duplicated, every example is associated with exactly one visual source, and both images of a two-image example come from the same source. The visual sources are MindCube [57], HOPE [44], LINEMOD [16], YCB-V [49], HANDAL [12], CA-1M [23], OpenImages [22], and RefSpatial-Blender [62]. The 195 MindCube-derived examples reuse image data from the existing MindCubeBench evaluation set. Table 6 gives the complete composition by visual source.

> Para. 44[CN]: 每个样例都有唯一的候选 ID 和唯一的上游视觉来源 ID。不存在重复的完整视觉单元，每个样例恰好对应一个视觉来源，并且双图像样例中的两幅图像来自同一来源。视觉来源包括 MindCube [57]、HOPE [44]、LINEMOD [16]、YCB-V [49]、HANDAL [12]、CA-1M [23]、OpenImages [22] 和 RefSpatial-Blender [62]。195 个源自 MindCube 的样例复用了现有 MindCubeBench 评估集中的图像数据。表 6 给出了按视觉来源划分的完整构成。

> | Visual Source | Count | Share |
> |---|---:|---:|
> | MindCube | 195 | 37.79% |
> | HOPE | 110 | 21.32% |
> | LINEMOD | 46 | 8.91% |
> | YCB-V | 5 | 0.97% |
> | HANDAL | 1 | 0.19% |
> | CA-1M | 116 | 22.48% |
> | OpenImages | 29 | 5.62% |
> | RefSpatial-Blender | 14 | 2.71% |

> | 视觉来源 | 数量 | 占比 |
> |---|---:|---:|
> | MindCube | 195 | 37.79% |
> | HOPE | 110 | 21.32% |
> | LINEMOD | 46 | 8.91% |
> | YCB-V | 5 | 0.97% |
> | HANDAL | 1 | 0.19% |
> | CA-1M | 116 | 22.48% |
> | OpenImages | 29 | 5.62% |
> | RefSpatial-Blender | 14 | 2.71% |

> Para. 45: **Table 6**　Visual-source provenance of the 516 SpatialCLI-Bench examples.

> Para. 45[CN]: **表 6**　516 个 SpatialCLI-Bench 样例的视觉来源。

> Para. 46: The benchmark contains 243 single-image examples (47.09%) and 273 two-image examples (52.91%).

> Para. 46[CN]: 该基准包含 243 个单图像样例（47.09%）和 273 个双图像样例（52.91%）。

> ## C.3　Capability Composition and Oracle Plans

> ## C.3　能力构成与预言机计划

> Para. 47: Table 7 summarizes the joint capability composition. Grounding appears in 414 examples (80.23%), depth in 403 (78.10%), and pose in 402 (77.91%), giving nearly balanced marginal coverage. All two-image examples include P through cross-view camera-motion or pose evidence.

> Para. 47[CN]: 表 7 总结了联合能力构成。定位出现在 414 个样例中（80.23%），深度出现在 403 个样例中（78.10%），位姿出现在 402 个样例中（77.91%），从而形成近乎均衡的边际覆盖。所有双图像样例都通过跨视图相机运动或位姿证据包含 P。

> ---

> ## Page 21 / 第 21 页

> | Capability Combination | Count | Share |
> |---|---:|---:|
> | GD | 114 | 22.09% |
> | GP | 113 | 21.90% |
> | DP | 102 | 19.77% |
> | GDP | 187 | 36.24% |

> | 能力组合 | 数量 | 占比 |
> |---|---:|---:|
> | GD | 114 | 22.09% |
> | GP | 113 | 21.90% |
> | DP | 102 | 19.77% |
> | GDP | 187 | 36.24% |

> Para. 48: **Table 7**　Joint capability composition of SpatialCLI-Bench.

> Para. 48[CN]: **表 7**　SpatialCLI-Bench 的联合能力构成。

> Para. 49: The 516 private oracle plans contain 1,964 tool steps, averaging 3.81 steps per example. There are 12 two-step, 156 three-step, 268 four-step, and 80 five-step plans. Across all plans, `query_segment`, `query_depth`, `query_pose`, and `query_locate` are invoked 862, 471, 404, and 227 times, respectively.

> Para. 49[CN]: 516 个私有预言机计划共包含 1,964 个工具步骤，平均每个样例 3.81 步。其中有 12 个两步计划、156 个三步计划、268 个四步计划和 80 个五步计划。在所有计划中，`query_segment`、`query_depth`、`query_pose` 和 `query_locate` 分别被调用 862、471、404 和 227 次。

> ## C.4　Multi-Stage Construction Pipeline

> ## C.4　多阶段构建流程

> Para. 50: **Frontier Multimodal Model Pre-Annotation.** A frontier multimodal model first builds a conservative structured inventory of uniquely referable visible entities for each candidate image or image pair. The inventory records each entity’s image index, visible description and attributes, a short tool query, and whether the entity is uncertain; rejected entities and their rejection reasons are recorded separately. We use Gemini 3.1 Pro [11] for this stage and retain only inventories with at least two reliable entities, including reliable coverage of both images for a two-image candidate.

> Para. 50[CN]: **前沿多模态模型预标注。** 前沿多模态模型首先为每幅候选图像或每个候选图像对，构建一个保守的、结构化的、由可唯一指代可见实体组成的清单。该清单记录每个实体的图像索引、可见描述和属性、简短工具查询，以及该实体是否不确定；被拒绝的实体及其拒绝原因另行记录。我们在这一阶段使用 Gemini 3.1 Pro [11]，并且只保留至少包含两个可靠实体的清单；对于双图像候选项，还要求可靠覆盖两幅图像。

> Para. 51: **Specialist-Vision-Model Fine Annotation.** Specialist vision models then collect capability-aligned evidence for up to four reliable entities. Locate and Segment establish entity positions and regions; Depth is queried at a representative point derived from localization or segmentation; Pose estimates cross-view camera motion for two-image candidates or object orientation for up to two entities in single-image candidates. Each response is stored with its exact tool arguments, and a candidate is rejected when a required service returns missing, explicit-error, or empty evidence.

> Para. 51[CN]: **专家视觉模型精细标注。** 随后，专家视觉模型为最多四个可靠实体收集与能力对齐的证据。Locate 和 Segment 确立实体的位置与区域；在由定位或分割得到的代表点处查询 Depth；Pose 为双图像候选项估计跨视图相机运动，或为单图像候选项中的最多两个实体估计物体方向。每个响应均连同其确切工具参数一起存储；当所需服务返回缺失、显式错误或空证据时，候选项将被拒绝。

> Para. 52: **Frontier Multimodal Model Fine Annotation.** Conditioned on the entity inventory and collected specialist evidence, Gemini 3.1 Pro generates the English question, one correct answer, five plausible distractors, a private evidence-grounded rationale, and a minimal reproducible oracle plan. The generation prompt requires every factual clause in the correct answer to be supported by specialist evidence and each distractor to be false for a specific evidence-grounded reason. Deterministic validation then enforces six unique choices, valid image indices and step dependencies, the five-step budget, exact capability–plan correspondence, and an exact match between every oracle step and a collected tool call; the choices are shuffled deterministically only after validation.

> Para. 52[CN]: **前沿多模态模型精细标注。** 在实体清单和已收集的专家证据条件下，Gemini 3.1 Pro 生成英文问题、一个正确答案、五个合理的干扰项、一个基于证据的私有理由，以及一个最小可复现的预言机计划。生成提示要求正确答案中的每个事实性从句都得到专家证据支持，并要求每个干扰项都因某个具体的、基于证据的原因而为假。随后，确定性验证会强制要求六个互异选项、有效的图像索引与步骤依赖关系、五步预算、能力与计划的精确对应，以及每个预言机步骤与已收集工具调用之间的精确匹配；仅在验证之后，才以确定性方式打乱选项。

> ## C.5　Independent Human Review and Filtering Yield

> ## C.5　独立人工审查与过滤产出率

> Para. 53: The automated construction pipeline described above initially generates 720 candidate questions. Human experts then answer each question independently without access to the answer generated by Gemini 3.1 Pro. The independent review is conducted by two graduate students with research backgrounds in embodied intelligence. The 516 candidates for which all independent human answers agree with the generated answer are retained in SpatialCLI-Bench, for an overall retention rate of 71.67%; the remaining 204 candidates are rejected because of answer disagreement. The supporting tool evidence and minimal executable tool plan are retained only as private audit metadata.

> Para. 53[CN]: 上述自动构建流程最初生成 720 个候选问题。随后，人类专家在无法访问 Gemini 3.1 Pro 所生成答案的情况下，独立回答每个问题。独立审查由两名具有具身智能研究背景的研究生进行。对于所有独立人工答案均与生成答案一致的 516 个候选项，我们将其保留在 SpatialCLI-Bench 中，总体保留率为 71.67%；其余 204 个候选项因答案存在分歧而被拒绝。支持性的工具证据和最小可执行工具计划仅作为私有审计元数据保留。

> # D　Spatial Tool Interfaces and Implementation

> # D　空间工具接口与实现

> ## D.1　Coordinate and Serialization Convention

> ## D.1　坐标与序列化约定

> Para. 54: Following the JSON grounding convention used by Qwen vision-language models [1], SpatialCLI represents points and boxes with `point_2d` and `bbox_2d`. All coordinates are integers in $[0,999]$, with the origin at the upper-left corner. We introduce `polygon_2d` as a SpatialCLI-specific extension for segmentation masks.

> Para. 54[CN]: 遵循 Qwen 视觉—语言模型 [1] 使用的 JSON 定位约定，SpatialCLI 使用 `point_2d` 和 `bbox_2d` 表示点和框。所有坐标均为 $[0,999]$ 内的整数，原点位于左上角。我们引入 `polygon_2d`，作为 SpatialCLI 针对分割掩码的专用扩展。

> ---

> ## Page 22 / 第 22 页

> Para. 55: A bounding box is serialized as $[x_{\min},y_{\min},x_{\max},y_{\max}]$. A point is serialized as $[x,y]$. A polygon is represented by an ordered list of boundary vertices, and multiple connected components are represented as a list of polygons. The Segment tool extracts external mask contours and represents each connected component with at most 16 vertices, targeting a rasterized mask IoU of 0.97 whenever feasible within this vertex budget. The polygon is rasterized at the original resolution whenever mask IoU is required.

> Para. 55[CN]: 边界框被序列化为 $[x_{\min},y_{\min},x_{\max},y_{\max}]$。点被序列化为 $[x,y]$。多边形由边界顶点的有序列表表示，而多个连通分量由多边形列表表示。Segment 工具提取外部掩码轮廓，并使用最多 16 个顶点表示每个连通分量；只要在该顶点预算内可行，目标栅格化掩码 IoU 就设为 0.97。每当需要掩码 IoU 时，都会在原始分辨率下栅格化多边形。

> ## D.2　Spatial Tool Interfaces

> ## D.2　空间工具接口

> Para. 56: The agent sees only four model-level interfaces: `query_locate`, `query_segment`, `query_depth`, and `query_pose`; it does not select the underlying specialist vision models. The service layer encapsulates six specialist vision models: Locate Anything [46] and Grounding DINO [28] for fused localization, SAM 3 [4] for segmentation, Depth Anything 3 [25] for metric depth, Orient Anything V2 [47] for object orientation, and VGGT [45] for multi-view camera motion. All four interfaces share the XML-wrapped JSON calling protocol and accept an optional `image_indices` field with one-based image or frame indices. At runtime, only responses matched by the fixed regular expression for this protocol are treated as tool calls; all unmatched responses, including those with malformed tool-call syntax, are treated as final answers. Their complete registrations are provided in Boxes D.1–D.4.

> Para. 56[CN]: 智能体只能看到四个模型级接口：`query_locate`、`query_segment`、`query_depth` 和 `query_pose`；它不会选择底层专家视觉模型。服务层封装了六个专家视觉模型：用于融合定位的 Locate Anything [46] 和 Grounding DINO [28]、用于分割的 SAM 3 [4]、用于度量深度的 Depth Anything 3 [25]、用于物体方向的 Orient Anything V2 [47]，以及用于多视图相机运动的 VGGT [45]。四个接口共享由 XML 包裹的 JSON 调用协议，并接受可选的 `image_indices` 字段，其中包含从一开始计数的图像或帧索引。在运行时，只有与该协议的固定正则表达式匹配的响应才被视为工具调用；所有不匹配的响应，包括工具调用语法格式错误的响应，均被视为最终答案。其完整注册信息见方框 D.1–D.4。

> Para. 57: **Locate.** Locate fuses detections from Locate Anything and Grounding DINO, while exposing only the fused boxes and center points to the agent. Both backends process the same image–query pair in parallel. Grounding DINO detections are filtered at a confidence threshold of 0.30 and suppressed using box NMS with an IoU threshold of 0.50. For a Locate Anything box $b_i^L$, we select the unmatched Grounding DINO box $b_{J^*(i)}^D$ with the largest IoU. If their IoU is at least 0.50, the cross-confirmed box is

> Para. 57[CN]: **Locate。** Locate 融合来自 Locate Anything 和 Grounding DINO 的检测结果，同时仅向智能体公开融合后的框和中心点。两个后端并行处理相同的图像—查询对。Grounding DINO 检测结果以 0.30 的置信度阈值进行过滤，并使用 IoU 阈值为 0.50 的框 NMS 进行抑制。对于 Locate Anything 框 $b_i^L$，我们选择具有最大 IoU 且尚未匹配的 Grounding DINO 框 $b_{J^*(i)}^D$。如果二者的 IoU 至少为 0.50，则交叉确认框为

> $b_i^F = \operatorname{round} \left( \frac{2b_i^L+b_{J^*(i)}^D}{3} \right), \tag{4}$

> Para. 58: which gives Locate Anything twice the coordinate weight of Grounding DINO. Unmatched predictions from either backend are retained to preserve recall. The combined candidates are greedily deduplicated: a candidate $b_i$ is removed if a retained box $b_j$ satisfies

> Para. 58[CN]: 这使 Locate Anything 的坐标权重为 Grounding DINO 的两倍。为保持召回率，来自任一后端的未匹配预测均被保留。对合并后的候选项进行贪心去重：如果某个已保留框 $b_j$ 满足以下条件，则删除候选框 $b_i$：

> $\operatorname{IoU}(b_i,b_j)\geq0.75 \qquad\text{or}\qquad \frac{|b_i\cap b_j|}{\min(|b_i|,|b_j|)}\geq0.90. \tag{5}$

> Para. 59: Here, $|b|$ denotes the area of box $b$. The second criterion removes near-contained duplicates that may have a modest box IoU because of their different areas. Backend identities, confidence scores, and cross-model IoUs remain internal.

> Para. 59[CN]: 这里，$|b|$ 表示框 $b$ 的面积。第二个准则会移除近乎被包含的重复框；由于面积不同，这些框的框 IoU 可能并不高。后端身份、置信度分数和跨模型 IoU 均保留在内部。

> ### Box D.1: Locate Tool Registration

> ### 方框 D.1：Locate 工具注册

> Para. 60:

> ```json
> {
>   "name": "query_locate",
>   "description": "Locate every visible instance matching a short language description. Use this when exact object positions, centers, boxes, counts, or left/right order depend on reliable grounding. Query a concrete visual category and attributes only. For 'closest', 'farthest', 'leftmost', or 'second' questions, do not put that relation in the query: locate all instances of the base category, then compare their returned centers or query their depths. All benchmark geometry and tool coordinates use the same normalized 0-999 image space. The tool returns bbox_2d and point_2d in that space; pass point_2d directly to query_depth when needed. It may return zero, one, or several instances; do not assume the first instance is the only one. Prefer this tool for answers that require explicit path points, object markers, or boxes. Answer simple categorical left/right yes-no questions directly when visually clear. It cannot infer five-point grasp-finger geometry or projected 3D cuboid corners from a 2D box, so do not treat its center or box corners as those answers. Tools are optional. In a multi-image or sampled-video task, omit image_indices to use all images, or provide one or more 1-based image/frame numbers to select a subset.",
>   "parameters": {
>     "type": "object",
>     "properties": {
>       "query": {
>         "type": "string",
>         "description": "Concrete visual category/attributes, without positional or depth superlatives."
>       },
> ```

> Para. 60[CN]:

> ```json
> {
>   "name": "query_locate",
>   "description": "定位与简短语言描述匹配的每个可见实例。当精确的物体位置、中心、框、数量或左右次序依赖可靠定位时，使用此工具。仅查询具体的视觉类别和属性。对于“最近”“最远”“最左”或“第二个”等问题，不要将该关系放入查询中：应定位基础类别的所有实例，然后比较其返回的中心，或查询其深度。所有基准几何和工具坐标均使用相同的归一化 0-999 图像空间。该工具在此空间中返回 bbox_2d 和 point_2d；需要时可将 point_2d 直接传给 query_depth。它可能返回零个、一个或多个实例；不要假定第一个实例就是唯一实例。对于需要显式路径点、物体标记或框的答案，优先使用此工具。当简单的类别型左右是非问题在视觉上清晰时，直接作答。它无法从二维框推断五点抓取手指几何或投影后的三维长方体角点，因此不要把其中心或框角点视为这些答案。工具是可选的。在多图像或采样视频任务中，省略 image_indices 可使用所有图像，或者提供一个或多个从 1 开始计数的图像/帧编号以选择子集。",
>   "parameters": {
>     "type": "object",
>     "properties": {
>       "query": {
>         "type": "string",
>         "description": "具体的视觉类别/属性，不含位置或深度最高级。"
>       },
> ```

> ---

> ## Page 23 / 第 23 页

> Para. 61:

> ```json
>       "image_indices": {
>         "type": "array",
>         "items": {"type": "integer", "minimum": 1},
>         "minItems": 1,
>         "uniqueItems": true,
>         "description": "Optional 1-based image/frame numbers. Omit to use the only image in a single-image task or all images jointly in a multi-image task."
>       }
>     },
>     "required": ["query"]
>   }
> }

> Example:
> <tool_call>
> {"name": "query_locate", "arguments": {"query": "red mug", "image_indices": [1]}}
> </tool_call>

> Possible return:
> {"count": 1, "result": [{"bbox_2d": [532, 470, 628, 675], "point_2d": [580, 572]}]}
> ```

> Para. 61[CN]:

> ```json
>       "image_indices": {
>         "type": "array",
>         "items": {"type": "integer", "minimum": 1},
>         "minItems": 1,
>         "uniqueItems": true,
>         "description": "可选的、从 1 开始计数的图像/帧编号。省略时，在单图像任务中使用唯一图像，在多图像任务中联合使用所有图像。"
>       }
>     },
>     "required": ["query"]
>   }
> }

> 示例：
> <tool_call>
> {"name": "query_locate", "arguments": {"query": "红色马克杯", "image_indices": [1]}}
> </tool_call>

> 可能的返回：
> {"count": 1, "result": [{"bbox_2d": [532, 470, 628, 675], "point_2d": [580, 572]}]}
> ```

> Para. 62: **Segment.** Segment uses a short text query to obtain SAM 3 masks and returns each reliable instance as a box, center point, and one or more polygonal connected components. Predictions with confidence at most 0.30 are removed, after which confidence-ordered mask suppression removes a candidate whose mask IoU with any retained instance is at least 0.90. For each retained mask, we extract pixel-level external contours, discard connected components smaller than 16 pixels², and order the remaining components by area. Because only external contours are serialized, holes inside a component are not represented explicitly.

> Para. 62[CN]: **Segment。** Segment 使用简短文本查询获得 SAM 3 掩码，并将每个可靠实例作为一个框、一个中心点以及一个或多个多边形连通分量返回。置信度不高于 0.30 的预测会被移除；随后，按置信度排序的掩码抑制会移除与任何已保留实例的掩码 IoU 至少为 0.90 的候选项。对于每个保留的掩码，我们提取像素级外部轮廓，丢弃小于 16 像素²的连通分量，并按面积排列其余分量。由于仅序列化外部轮廓，因此分量内部的孔洞不会被显式表示。

> Para. 63: Contour vertices are quantized into the shared integer coordinate space; adjacent duplicate vertices and an explicit closing vertex are removed. For a closed contour $\Gamma_k$ with perimeter $L_k$, we apply Douglas–Peucker simplification with tolerance $\epsilon_k(r)=rL_k$ over

> Para. 63[CN]: 轮廓顶点被量化到共享整数坐标空间；相邻的重复顶点和显式闭合顶点会被移除。对于周长为 $L_k$ 的闭合轮廓 $\Gamma_k$，我们使用容差 $\epsilon_k(r)=rL_k$ 进行 Douglas–Peucker 简化，其中

> $r\in\{0\}\cup\operatorname{LogSpace}(10^{-5},0.25,72). \tag{6}$

> Para. 64: Each candidate polygon $P$ is first quantized into the final integer coordinate space, mapped back to the original resolution, and rasterized as $\mathcal R(P)$. Its fidelity to the corresponding mask component $M_k$ is

> Para. 64[CN]: 每个候选多边形 $P$ 首先被量化到最终整数坐标空间，再映射回原始分辨率，并栅格化为 $\mathcal R(P)$。它与相应掩码分量 $M_k$ 的保真度为

> $Q(P;M_k) = \operatorname{IoU}(M_k,\mathcal R(P)) = \frac{|M_k\cap\mathcal R(P)|}{|M_k\cup\mathcal R(P)|}. \tag{7}$

> Para. 65: We choose the candidate with the fewest vertices subject to

> Para. 65[CN]: 我们在满足以下条件的候选项中选择顶点最少者：

> $Q(P;M_k)\geq0.97, \qquad 3\leq|P|\leq16, \tag{8}$

> Para. 66: breaking ties in favor of higher IoU. We then greedily attempt to remove low-contribution vertices in ascending order of

> Para. 66[CN]: 若出现并列，则优先选择 IoU 更高者。随后，我们按照以下量的升序，贪心地尝试移除贡献较低的顶点：

> $d_v=\left|(p_v-p_{v-1})\times(p_{v+1}-p_{v-1})\right|, \tag{9}$

> Para. 67: accepting a removal only if the rasterized IoU remains at least 0.97. If no polygon reaches the target within the 16-vertex budget, the bounded candidate with the highest IoU is returned instead; thus 0.97 is a target rather than an unconditional guarantee. The returned `point_2d` is the center of the SAM 3 predicted box, not the mask centroid, and need not lie inside the mask.

> Para. 67[CN]: 仅当栅格化 IoU 仍至少为 0.97 时才接受移除。如果没有任何多边形在 16 顶点预算内达到目标，则改为返回有界候选项中 IoU 最高者；因此，0.97 是目标，而不是无条件保证。返回的 `point_2d` 是 SAM 3 预测框的中心，而不是掩码质心，并且不一定位于掩码内部。

> ### Box D.2: Segment Tool Registration

> ### 方框 D.2：Segment 工具注册

> Para. 68:

> ```json
> {
>   "name": "query_segment",
>   "description": "Segment every visible instance matching a short language description. Use this for exact object boundaries, occupied regions, shapes, containment, overlap, or placement areas; use query_locate instead when centers, counts, or simple left/right order are sufficient. Pass a concrete visual category/attributes only, without closest/leftmost/second relations, and do not pass a box. All benchmark geometry and tool coordinates use the same normalized 0-999 image space. Each returned instance contains bbox_2d, point_2d, and polygon_2d in that space.
> ```

> Para. 68[CN]:

> ```json
> {
>   "name": "query_segment",
>   "description": "分割与简短语言描述匹配的每个可见实例。将此工具用于精确的物体边界、占用区域、形状、包含关系、重叠或放置区域；当中心、数量或简单的左右次序已足够时，应改用 query_locate。仅传入具体的视觉类别/属性，不包含最近/最左/第二个等关系，也不要传入框。所有基准几何和工具坐标均使用相同的归一化 0-999 图像空间。每个返回实例都在该空间中包含 bbox_2d、point_2d 和 polygon_2d。
> ```

> ---

> ## Page 24 / 第 24 页

> Para. 69:

> ```json
> The point is the mask bounding-box center and is easiest to use for paths or object markers. polygon_2d is a list because one mask may have disconnected parts. Prefer this tool for object markers, occupied regions, and boundary-sensitive coordinate tasks. Do not use a mask center or polygon as five-point grasp-finger geometry or projected 3D cuboid corners. Answer categorical yes-no and relative-depth questions directly unless an exact boundary is genuinely required. Tools are optional. In a multi-image or sampled-video task, omit image_indices to use all images, or provide one or more 1-based image/frame numbers to select a subset.",
>   "parameters": {
>     "type": "object",
>     "properties": {
>       "query": {
>         "type": "string",
>         "description": "Short description of the target instances."
>       },
>       "image_indices": {
>         "type": "array",
>         "items": {"type": "integer", "minimum": 1},
>         "minItems": 1,
>         "uniqueItems": true,
>         "description": "Optional 1-based image/frame numbers. Omit to use the only image in a single-image task or all images jointly in a multi-image task."
>       }
>     },
>     "required": ["query"]
>   }
> }

> Example:
> <tool_call>
> {"name": "query_segment", "arguments": {"query": "red mug"}}
> </tool_call>

> Possible return:
> {"count": 1, "result": [{"bbox_2d": [532, 470, 628, 675], "point_2d": [580, 572], "polygon_2d": [[[548, 475], [605, 472], [623, 516], [609, 670]]]}]}
> ```

> Para. 69[CN]:

> ```json
> 该点是掩码边界框中心，最便于用于路径或物体标记。polygon_2d 是一个列表，因为一个掩码可能包含彼此断开的部分。对于物体标记、占用区域和边界敏感的坐标任务，优先使用此工具。不要将掩码中心或多边形用作五点抓取手指几何或投影后的三维长方体角点。除非确实需要精确边界，否则应直接回答类别型是非问题和相对深度问题。工具是可选的。在多图像或采样视频任务中，省略 image_indices 可使用所有图像，或者提供一个或多个从 1 开始计数的图像/帧编号以选择子集。",
>   "parameters": {
>     "type": "object",
>     "properties": {
>       "query": {
>         "type": "string",
>         "description": "目标实例的简短描述。"
>       },
>       "image_indices": {
>         "type": "array",
>         "items": {"type": "integer", "minimum": 1},
>         "minItems": 1,
>         "uniqueItems": true,
>         "description": "可选的、从 1 开始计数的图像/帧编号。省略时，在单图像任务中使用唯一图像，在多图像任务中联合使用所有图像。"
>       }
>     },
>     "required": ["query"]
>   }
> }

> 示例：
> <tool_call>
> {"name": "query_segment", "arguments": {"query": "红色马克杯"}}
> </tool_call>

> 可能的返回：
> {"count": 1, "result": [{"bbox_2d": [532, 470, 628, 675], "point_2d": [580, 572], "polygon_2d": [[[548, 475], [605, 472], [623, 516], [609, 670]]]}]}
> ```

> Para. 70: **Depth.** Depth uses the DA3NESTED-GIANT-LARGE-1.1 metric backend to return camera-axis distance in meters at one or more selected image points. Inference uses a processing resolution of 504 pixels, and each query reads its corresponding depth-map pixel directly without spatial smoothing. Metric-scale alignment is made deterministic across workers. The returned `depth_m` is a monocular estimate of camera-axis Z-depth, rather than Euclidean range from the camera center or a physical sensor measurement.

> Para. 70[CN]: **Depth。** Depth 使用 DA3NESTED-GIANT-LARGE-1.1 度量后端，返回一个或多个选定图像点处以米为单位的相机轴向距离。推理使用 504 像素的处理分辨率，每个查询直接读取其对应的深度图像素，而不进行空间平滑。度量尺度对齐在不同工作进程之间保持确定性。返回的 `depth_m` 是相机轴向 Z 深度的单目估计，而不是从相机中心出发的欧氏距离，也不是物理传感器测量值。

> ### Box D.3: Depth Tool Registration

> ### 方框 D.3：Depth 工具注册

> Para. 71:

> ```json
> {
>   "name": "query_depth",
>   "description": "Query depth at one or more image points. Pass every point needed for a closer/farther, front/behind, or distance comparison in one call. Point coordinates are normalized to 0-999 and the number of points is unrestricted. For named objects, first use query_locate to obtain their center points, then query all centers together. Each result contains depth_m, an estimated camera-axis distance in meters; larger means farther. Monocular depth estimates can be noisy: answer directly when the relative depth is already visually clear, and call this tool only when depth is essential and genuinely ambiguous. In a multi-image or sampled-video task, omit image_indices to use all images, or provide one or more 1-based image/frame numbers to select a subset.",
>   "parameters": {
>     "type": "object",
>     "properties": {
>       "points": {
>         "type": "array",
>         "minItems": 1,
>         "description": "One or more [x, y] points in normalized 0-999 coordinates.",
>         "items": {
>           "type": "array",
>           "items": {"type": "number"},
>           "minItems": 2,
>           "maxItems": 2
>         }
> ```

> Para. 71[CN]:

> ```json
> {
>   "name": "query_depth",
>   "description": "查询一个或多个图像点处的深度。在一次调用中传入进行更近/更远、前方/后方或距离比较所需的每个点。点坐标被归一化到 0-999，点的数量不受限制。对于具名物体，首先使用 query_locate 获取其中心点，然后一起查询所有中心。每个结果都包含 depth_m，即以米为单位的估计相机轴向距离；数值越大表示越远。单目深度估计可能存在噪声：当相对深度在视觉上已经清晰时直接作答，仅在深度至关重要且确实存在歧义时调用此工具。在多图像或采样视频任务中，省略 image_indices 可使用所有图像，或者提供一个或多个从 1 开始计数的图像/帧编号以选择子集。",
>   "parameters": {
>     "type": "object",
>     "properties": {
>       "points": {
>         "type": "array",
>         "minItems": 1,
>         "description": "归一化 0-999 坐标中的一个或多个 [x, y] 点。",
>         "items": {
>           "type": "array",
>           "items": {"type": "number"},
>           "minItems": 2,
>           "maxItems": 2
>         }
> ```


> ## Page 25

> <span style="color:#3B82F6"><strong>Para. 82:</strong></span>

> ```text
> 17    },
> 18    "image_indices": {
> 19      "type": "array",
> 20      "items": {"type": "integer", "minimum": 1},
> 21      "minItems": 1,
> 22      "uniqueItems": true,
> 23      "description": "Optional 1-based image/frame numbers. Omit to use the only image in a single-image task or
>       all images jointly in a multi-image task."
> 24    }
> 25  },
> 26  "required": ["points"]
> 27 }
> 28 }
> 29
> 30 Example:
> 31 <tool_call>
> 32 {"name": "query_depth", "arguments": {"points": [[320, 480], [700, 510]]}}
> 33 </tool_call>
> 34
> 35 Possible return:
> 36 {"result": [{"point_2d": [320, 480], "depth_m": 2.41}, {"point_2d": [700, 510], "depth_m": 4.12}]}
> ```

> <span style="color:#F59E0B"><strong>Para. 82[CN]:</strong></span>

> ```text
> 17    },
> 18    "image_indices": {
> 19      "type": "array",
> 20      "items": {"type": "integer", "minimum": 1},
> 21      "minItems": 1,
> 22      "uniqueItems": true,
> 23      "description": "可选的、从 1 开始计数的图像/帧编号。在单图像任务中省略以使用唯一图像，或在
>       多图像任务中省略以联合使用所有图像。"
> 24    }
> 25  },
> 26  "required": ["points"]
> 27 }
> 28 }
> 29
> 30 示例：
> 31 <tool_call>
> 32 {"name": "query_depth", "arguments": {"points": [[320, 480], [700, 510]]}}
> 33 </tool_call>
> 34
> 35 可能的返回：
> 36 {"result": [{"point_2d": [320, 480], "depth_m": 2.41}, {"point_2d": [700, 510], "depth_m": 4.12}]}
> ```

> **Para. 2: Pose.** Pose routes a named-object query to Orient Anything V2 and the exact query camera motion to the multi-view VGGT camera-pose backend. For object orientation, Pose first invokes the fused Locate interface and enlarges every detected box by 10% of its width and height on each side, with a minimum padding of two pixels. The crop is resized with its aspect ratio preserved, padded to $518\times518$, and processed by Orient Anything V2, which predicts azimuth, elevation, and roll using 360, 180, and 360 discrete bins, respectively. Only the horizontal orientation is exposed to the agent. For azimuth $\varphi_{\mathrm{az}}$, its eight-direction sector is

> **Para. 2[CN]: 姿态。** Pose 将命名对象查询路由至 Orient Anything V2，并将精确的查询“camera motion”路由至多视图 VGGT 相机姿态后端。对于对象朝向，Pose 首先调用融合的 Locate 接口，并在每一侧将每个检测框扩大其宽度和高度的 10%，且最小填充为两个像素。裁剪区域在保持纵横比的情况下调整尺寸，填充至 $518\times518$，再由 Orient Anything V2 处理；该模型分别使用 360、180 和 360 个离散分箱预测方位角、仰角和滚转角。仅向智能体公开水平方向。对于方位角 $\varphi_{\mathrm{az}}$，其八方向扇区为

> <span style="color:#3B82F6"><strong>Para. 83:</strong></span>

> $\nu_{\mathrm{az}} = \left\lfloor \frac{(\varphi_{\mathrm{az}}+22.5^\circ)\bmod 360^\circ}{45^\circ} \right\rfloor . \tag{10}$

> <span style="color:#F59E0B"><strong>Para. 83[CN]:</strong></span>

> $\nu_{\mathrm{az}} = \left\lfloor \frac{(\varphi_{\mathrm{az}}+22.5^\circ)\bmod 360^\circ}{45^\circ} \right\rfloor . \tag{10}$

> <span style="color:#3B82F6"><strong>Para. 84:</strong></span> The sector is converted into the complementary fields `visible_side` and `facing_direction_camera`; in the latter, front points into the image and back points toward the camera.

> <span style="color:#F59E0B"><strong>Para. 84[CN]:</strong></span> 该扇区被转换为互补字段 `visible_side` 和 `facing_direction_camera`；在后一个字段中，front 指向图像内部，而 back 指向相机。

> <span style="color:#3B82F6"><strong>Para. 85:</strong></span> For camera motion, VGGT jointly estimates world-to-camera extrinsics $E_i=[R_i\mid t_i]$ for the selected views in their given order. The camera center and the adjacent-view translation expressed in the source-camera frame are

> <span style="color:#F59E0B"><strong>Para. 85[CN]:</strong></span> 对于相机运动，VGGT 按给定顺序联合估计所选视图的世界到相机外参 $E_i=[R_i\mid t_i]$。相机中心以及在源相机坐标系中表示的相邻视图平移为

> <span style="color:#3B82F6"><strong>Para. 86:</strong></span>

> $C_i=-R_i^{\mathsf T}t_i,\qquad \Delta_i=R_i(C_{i+1}-C_i),\qquad \hat{\Delta}_i= \frac{\Delta_i}{\lVert\Delta_i\rVert_2} \ \text{if }\lVert\Delta_i\rVert_2\ge 0.002. \tag{11}$

> <span style="color:#F59E0B"><strong>Para. 86[CN]:</strong></span>

> $C_i=-R_i^{\mathsf T}t_i,\qquad \Delta_i=R_i(C_{i+1}-C_i),\qquad \hat{\Delta}_i= \frac{\Delta_i}{\lVert\Delta_i\rVert_2} \ \text{若 }\lVert\Delta_i\rVert_2\ge 0.002. \tag{11}$

> <span style="color:#3B82F6"><strong>Para. 87:</strong></span> Before serializing $\hat{\Delta}_i$ as signed axes, we negate its $Y$ and $Z$ components to obtain the exposed convention of $+X$ right, $+Y$ up, and $-Z$ forward. The relative view rotation is

> <span style="color:#F59E0B"><strong>Para. 87[CN]:</strong></span> 在将 $\hat{\Delta}_i$ 序列化为带符号坐标轴之前，我们对其 $Y$ 和 $Z$ 分量取反，以得到公开使用的约定：$+X$ 向右、$+Y$ 向上、$-Z$ 向前。相对视图旋转为

> <span style="color:#3B82F6"><strong>Para. 88:</strong></span>

> $R_{i\rightarrow i+1}=R_{i+1}R_i^{\mathsf T}. \tag{12}$

> <span style="color:#F59E0B"><strong>Para. 88[CN]:</strong></span>

> $R_{i\rightarrow i+1}=R_{i+1}R_i^{\mathsf T}. \tag{12}$

> <span style="color:#3B82F6"><strong>Para. 89:</strong></span> Translation and view rotation are summarized separately using these right-handed camera axes. A translation norm below 0.002 is treated as the same position, while rotations below $2^\circ$ are suppressed. For $N_{\mathrm{view}}$ selected images, the tool returns $N_{\mathrm{view}}-1$ summaries for adjacent pairs rather than all pairwise relations. Only scale-independent motion directions and signed axes are exposed; metric translation magnitudes, continuous angles, and camera matrices remain internal.

> <span style="color:#F59E0B"><strong>Para. 89[CN]:</strong></span> 平移和视图旋转使用这些右手相机坐标轴分别进行概括。平移范数低于 0.002 时被视为位置相同，而低于 $2^\circ$ 的旋转则被抑制。对于所选的 $N_{\mathrm{view}}$ 幅图像，该工具返回相邻图像对的 $N_{\mathrm{view}}-1$ 个概括，而不是所有成对关系。仅公开与尺度无关的运动方向和带符号坐标轴；公制平移幅度、连续角度和相机矩阵仍保留在内部。

> **Para. 10: Box D.4: Pose Tool Registration**

> **Para. 10[CN]: 框 D.4：Pose 工具注册**

> <span style="color:#3B82F6"><strong>Para. 90:</strong></span>

> ```text
> 1  {
> 2    "name": "query_pose",
> 3    "description": "Query a named object's facing direction in one image, or camera motion across images. For an
>      object, pass only a short visible description. The result returns visible_side (the object's side facing the camera) and
>      facing_direction_camera, where front means deeper into the image, back means toward the camera, and left/right
>      are the viewer's image sides. For viewpoint change, pass exactly query='camera motion'. Each result describes
>      to_image relative to from_image. Use position only for questions about the camera's shooting location or movement;
>      use view_rotation only for questions about where the view turns. direction directly matches ordinary words such as
>      forward-right, left, up, or clockwise. position.axes uses signed right-handed coordinates where +X=right, +Y=up,
> ```

> <span style="color:#F59E0B"><strong>Para. 90[CN]:</strong></span>

> ```text
> 1  {
> 2    "name": "query_pose",
> 3    "description": "查询单幅图像中某个命名对象的朝向，或查询跨图像的相机运动。对于对象，
>      只传入简短的可见描述。结果返回 visible_side（对象面向相机的一侧）和
>      facing_direction_camera，其中 front 表示更深入图像，back 表示朝向相机，而 left/right
>      是观察者所见图像的左右两侧。对于视点变化，请准确传入 query='camera motion'。每个结果描述
>      to_image 相对于 from_image 的关系。仅在询问相机拍摄位置或移动时使用 position；
>      仅在询问视图转向何处时使用 view_rotation。direction 直接对应普通词语，例如
>      forward-right、left、up 或 clockwise。position.axes 使用带符号的右手坐标，其中 +X=right、+Y=up，
> ```

> ---

> ## Page 26

> <span style="color:#3B82F6"><strong>Para. 91:</strong></span>

> ```text
>      and -Z=forward. view_rotation.axes is the signed camera-pose rotation and should be used directly only when
>      answer choices explicitly mention positive/negative X/Y/Z axes; for ordinary turn words use view_rotation.direction.
>      same-position means no reliable translation. Omit image_indices for image 2 relative to image 1; reverse them only
>      when the question explicitly asks for image 1 relative to image 2. Use object mode only for object orientation and
>      camera-motion mode only for actual viewpoint change; otherwise answer directly. In a multi-image or sampled-video
>      task, omit image_indices to use all images, or provide one or more 1-based image/frame numbers to select a subset.",
> 4    "parameters": {
> 5      "type": "object",
> 6      "properties": {
> 7        "query": {
> 8          "type": "string",
> 9          "description": "Object description, or 'camera motion'."
> 10       },
> 11       "image_indices": {
> 12         "type": "array",
> 13         "items": {"type": "integer", "minimum": 1},
> 14         "minItems": 1,
> 15         "uniqueItems": true,
> 16         "description": "Optional 1-based image/frame numbers. Omit to use the only image in a single-image task or
>            all images jointly in a multi-image task."
> 17       }
> 18     },
> 19     "required": ["query"]
> 20   }
> 21 }
> 22
> 23 Object-orientation example:
> 24 <tool_call>
> 25 {"name": "query_pose", "arguments": {"query": "red mug", "image_indices": [1]}}
> 26 </tool_call>
> 27
> 28 Possible return:
> 29 {"result": [{"image_index": 1, "bbox_2d": [532, 470, 628, 675], "visible_side": "front-right",
>    "facing_direction_camera": "back-left"}]}
> 30
> 31 Camera-motion example:
> 32 <tool_call>
> 33 {"name": "query_pose", "arguments": {"query": "camera motion", "image_indices": [1, 2]}}
> 34 </tool_call>
> 35
> 36 Possible return:
> 37 {"result": [{"from_image": 1, "to_image": 2, "position": {"direction": "forward-right", "axes": ["+X", "-Z"]},
>    "view_rotation": {"direction": "right", "axes": ["+Y"]}, "dominant_axis": "+Y"}]}
> ```

> <span style="color:#F59E0B"><strong>Para. 91[CN]:</strong></span>

> ```text
>      且 -Z=forward。view_rotation.axes 是带符号的相机姿态旋转，只有当
>      答案选项明确提及正/负 X/Y/Z 轴时才应直接使用；对于普通的转向词语，请使用 view_rotation.direction。
>      same-position 表示不存在可靠平移。当查询图像 2 相对于图像 1 时省略 image_indices；仅当
>      问题明确询问图像 1 相对于图像 2 时才将其顺序反转。仅对对象朝向使用对象模式，并且
>      仅对实际视点变化使用相机运动模式；否则直接作答。在多图像或采样视频
>      任务中，省略 image_indices 以使用所有图像，或提供一个或多个从 1 开始的图像/帧编号来选择子集。",
> 4    "parameters": {
> 5      "type": "object",
> 6      "properties": {
> 7        "query": {
> 8          "type": "string",
> 9          "description": "对象描述，或 'camera motion'。"
> 10       },
> 11       "image_indices": {
> 12         "type": "array",
> 13         "items": {"type": "integer", "minimum": 1},
> 14         "minItems": 1,
> 15         "uniqueItems": true,
> 16         "description": "可选的、从 1 开始计数的图像/帧编号。在单图像任务中省略以使用唯一图像，或在
>            多图像任务中省略以联合使用所有图像。"
> 17       }
> 18     },
> 19     "required": ["query"]
> 20   }
> 21 }
> 22
> 23 对象朝向示例：
> 24 <tool_call>
> 25 {"name": "query_pose", "arguments": {"query": "red mug", "image_indices": [1]}}
> 26 </tool_call>
> 27
> 28 可能的返回：
> 29 {"result": [{"image_index": 1, "bbox_2d": [532, 470, 628, 675], "visible_side": "front-right",
>    "facing_direction_camera": "back-left"}]}
> 30
> 31 相机运动示例：
> 32 <tool_call>
> 33 {"name": "query_pose", "arguments": {"query": "camera motion", "image_indices": [1, 2]}}
> 34 </tool_call>
> 35
> 36 可能的返回：
> 37 {"result": [{"from_image": 1, "to_image": 2, "position": {"direction": "forward-right", "axes": ["+X", "-Z"]},
>    "view_rotation": {"direction": "right", "axes": ["+Y"]}, "dominant_axis": "+Y"}]}
> ```

> **Para. 13: Deployment and Runtime.** All six specialist-model services are jointly deployed on two GPUs. Compared with the central VLM, these specialist backends are generally compact and introduce modest runtime overhead. During long-running RL training, the observed mean latency per spatial-tool call was 2.916 seconds.

> **Para. 13[CN]: 部署与运行时。** 六个专家模型服务共同部署在两块 GPU 上。与中央 VLM 相比，这些专家后端通常较为紧凑，仅引入适度的运行时开销。在长时间运行的强化学习训练期间，观测到的每次空间工具调用平均延迟为 2.916 秒。

> **Para. 14: Cache Design.** Each specialist backend uses a content-addressed two-tier cache: a bounded in-process least-recently-used (LRU) cache backed by a persistent disk cache under `outputs/cache/`. Each key is a SHA-256 digest derived from the input-image content hashes rather than file paths, together with the request text or mode, the relevant model or checkpoint fingerprint, and all inference and post-processing settings that can affect the returned result. Consequently, identical image content can be reused across path aliases, whereas a changed image, model checkpoint, query, backend, or output-affecting parameter produces a different key. Lookup checks memory before disk and promotes a disk hit into the in-memory LRU. On a miss, the service executes the specialist model and atomically persists the successful result; failed requests are not cached, and per-process locks prevent concurrent duplicate inference.

> **Para. 14[CN]: 缓存设计。** 每个专家后端均使用按内容寻址的两级缓存：一个容量受限的进程内最近最少使用（LRU）缓存，以及位于 `outputs/cache/` 下、为其提供支持的持久化磁盘缓存。每个键都是一个 SHA-256 摘要，它由输入图像的内容哈希而非文件路径生成，同时还包括请求文本或模式、相关模型或检查点指纹，以及所有可能影响返回结果的推理和后处理设置。因此，相同图像内容可跨路径别名复用，而图像、模型检查点、查询、后端或影响输出的参数一旦改变，就会产生不同的键。查找时先检查内存，再检查磁盘，并将磁盘命中项提升到内存中的 LRU。发生未命中时，服务执行专家模型并以原子方式持久化成功结果；失败请求不予缓存，进程级锁则防止并发的重复推理。

> <span style="color:#3B82F6"><strong>Para. 92:</strong></span> The cache granularity follows each backend’s computation. Depth caches the full metric-depth map, intrinsics, confidence, image size, and scale factor per image, allowing different queried points on the same image to reuse one forward pass. Segment maintains both a two-entry image-state cache, which reuses the SAM 3 image encoding across text queries, and 128-entry result caches keyed by image, query, and segmentation settings. Locate and Pose each maintain 128-entry result LRUs; their disk entries store the corresponding

> <span style="color:#F59E0B"><strong>Para. 92[CN]:</strong></span> 缓存粒度遵循各后端的计算方式。Depth 为每幅图像缓存完整的公制深度图、内参、置信度、图像尺寸和尺度因子，使同一图像上的不同查询点能够复用一次前向传播。Segment 同时维护一个双条目的图像状态缓存，以便跨文本查询复用 SAM 3 图像编码，并维护按图像、查询和分割设置作为键的 128 条目结果缓存。Locate 和 Pose 各自维护 128 条目的结果 LRU；其磁盘条目存储相应的

> ---

> ## Page 27

> <span style="color:#3B82F6"><strong>Para. 93:</strong></span> structured outputs, while Pose additionally persists raw camera matrices for camera-motion requests. Pose keys distinguish the ordered image sequence, object-or-camera mode, selected camera backend, resolution, model fingerprints, and, for object orientation, the localization service. The equal-weight macro-average of the reported Depth, Segment, Pose, and Locate rates is approximately 58.8%; a request-weighted rate would additionally depend on the tool-call composition. The bounded LRU capacities limit memory growth, while cache hits bypass repeated specialist forward passes and therefore add negligible accelerator compute beyond lookup and output serialization. Table 8 reports the observed cache hit rates for each spatial tool.

> <span style="color:#F59E0B"><strong>Para. 93[CN]:</strong></span> 结构化输出，而 Pose 还会为相机运动请求持久化原始相机矩阵。Pose 的键区分有序图像序列、对象或相机模式、所选相机后端、分辨率、模型指纹，以及对象朝向所使用的定位服务。所报告的 Depth、Segment、Pose 和 Locate 命中率的等权宏平均值约为 58.8%；按请求加权的命中率还会取决于工具调用的组成。容量受限的 LRU 限制了内存增长，而缓存命中会绕过重复的专家模型前向传播，因此除了查找和输出序列化之外，几乎不会增加加速器计算量。表 8 报告了各空间工具观测到的缓存命中率。

> <span style="color:#3B82F6"><strong>Para. 94:</strong></span>

> | Tool or Mode | Specialist Backend / Scope | Hit Rate (%) |
> |---|---|---:|
> | Depth | Depth Anything 3 | $\approx 99.2$ |
> | Segment | SAM 3 | $\approx 49.4$ |
> | Pose | All Pose requests | $\approx 58.2$ |
> | ↳ Camera motion | VGGT, successful requests | 100.0 |
> | ↳ Object orientation | Orient Anything V2 | $\approx 43.8$ |
> | Locate | All Locate requests | $\approx 28.5$ |
> | Macro average | Four reported top-level paths | $\approx 58.8$ |

> <span style="color:#F59E0B"><strong>Para. 94[CN]:</strong></span>

> | 工具或模式 | 专家后端／范围 | 命中率（%） |
> |---|---|---:|
> | Depth | Depth Anything 3 | $\approx 99.2$ |
> | Segment | SAM 3 | $\approx 49.4$ |
> | Pose | 所有 Pose 请求 | $\approx 58.2$ |
> | ↳ 相机运动 | VGGT，成功请求 | 100.0 |
> | ↳ 对象朝向 | Orient Anything V2 | $\approx 43.8$ |
> | Locate | 所有 Locate 请求 | $\approx 28.5$ |
> | 宏平均 | 所报告的四条顶层路径 | $\approx 58.8$ |

> **Para. 18: Table 8** Observed cache hit rates for spatial-tool requests. Pose is also broken down by its camera-motion and object-orientation backends. The macro average uses the reported Depth, Segment, overall Pose, and Locate rates.

> **Para. 18[CN]: 表 8** 空间工具请求的观测缓存命中率。Pose 还按其相机运动后端和对象朝向后端进行了细分。宏平均使用所报告的 Depth、Segment、Pose 总体以及 Locate 命中率。

> **Para. 19: E Capability Internalization Metric**

> **Para. 19[CN]: E 能力内化指标**

> **Para. 20: E.1 Evaluation Data and Capability Coverage**

> **Para. 20[CN]: E.1 评估数据与能力覆盖**

> <span style="color:#3B82F6"><strong>Para. 95:</strong></span> The CII validation suite contains 1,000 held-out examples, balanced across five query types: 200 each for Locate, Segment, Depth, object orientation, and camera motion. The last two query types correspond to the two modes of the Pose interface. Each example contains the required image or image pair, a capability-specific request, and a structured reference output.

> <span style="color:#F59E0B"><strong>Para. 95[CN]:</strong></span> CII 验证套件包含 1,000 个留出样例，在五种查询类型之间保持均衡：Locate、Segment、Depth、对象朝向和相机运动各 200 个。最后两种查询类型对应 Pose 接口的两种模式。每个样例均包含所需的图像或图像对、特定于能力的请求，以及结构化参考输出。

> **Para. 22: E.2 Reference Construction and Evaluation Protocol**

> **Para. 22[CN]: E.2 参考构建与评估协议**

> <span style="color:#3B82F6"><strong>Para. 96:</strong></span> Candidate examples are converted into capability-specific requests, and the corresponding registered specialist tool is executed to produce each structured reference output. After the independent human verification described below, each retained tool output is serialized in the registered tool’s JSON result format. At evaluation time, the model receives only the image input and an instruction to return the requested tool format; no spatial tool is registered or executed. We use temperature 0.0, with a maximum of 512 output tokens for Locate, Depth, and both Pose modes, and 4,096 tokens for Segment because polygon serialization is substantially longer. A deterministic parser extracts the structured JSON response; a response from which no valid JSON object can be recovered receives zero similarity.

> <span style="color:#F59E0B"><strong>Para. 96[CN]:</strong></span> 候选样例被转换为特定于能力的请求，并执行对应的已注册专家工具，以生成各个结构化参考输出。经过下文所述的独立人工验证后，每个保留的工具输出都按已注册工具的 JSON 结果格式进行序列化。在评估时，模型仅接收图像输入和一条要求返回指定工具格式的指令；不会注册或执行任何空间工具。我们使用 0.0 的温度；对于 Locate、Depth 和 Pose 的两种模式，最大输出长度为 512 个 token；对于 Segment，则为 4,096 个 token，因为多边形序列化要长得多。确定性解析器提取结构化 JSON 响应；如果无法从某个响应中恢复任何有效 JSON 对象，则其相似度为零。

> **Para. 24: E.3 Independent Human Verification**

> **Para. 24[CN]: E.3 独立人工验证**

> <span style="color:#3B82F6"><strong>Para. 97:</strong></span> Two human experts independently verify each capability-specific request and its tool-produced reference against the image input. Neither expert can see the other’s judgment, and each checks that the request is unambiguous and the specialist-tool output is valid and consistent with the visual input. We retain a candidate only when both experts approve it; all other candidates are discarded. This independent agreement rule filters ambiguous requests and unreliable tool outputs before CII evaluation.

> <span style="color:#F59E0B"><strong>Para. 97[CN]:</strong></span> 两名人类专家分别将每个特定于能力的请求及其由工具生成的参考结果与图像输入进行核验。两名专家都无法看到对方的判断，并且各自检查请求是否无歧义，以及专家工具输出是否有效并与视觉输入一致。仅当两名专家均予以认可时，我们才保留该候选样例；其他所有候选样例均被丢弃。该独立一致性规则在 CII 评估之前过滤掉有歧义的请求和不可靠的工具输出。

> **Para. 26: E.4 Similarity Functions and Aggregation**

> **Para. 26[CN]: E.4 相似度函数与聚合**

> <span style="color:#3B82F6"><strong>Para. 98:</strong></span> We evaluate whether a model can reproduce spatial-tool outputs without executing external tools. For a capability type $\kappa\in\{\mathrm{Locate},\mathrm{Segment},\mathrm{Depth}\}$, let $\hat{o}_i$ be the model prediction and $o_i^*$ the corresponding

> <span style="color:#F59E0B"><strong>Para. 98[CN]:</strong></span> 我们评估模型能否在不执行外部工具的情况下复现空间工具输出。对于能力类型 $\kappa\in\{\mathrm{Locate},\mathrm{Segment},\mathrm{Depth}\}$，令 $\hat{o}_i$ 为模型预测，$o_i^*$ 为对应的

> ---

> ## Page 28

> <span style="color:#3B82F6"><strong>Para. 99:</strong></span> spatial-tool output. For each capability, samples are indexed locally by $i=1,\ldots,N_\kappa$. We define

> <span style="color:#F59E0B"><strong>Para. 99[CN]:</strong></span> 空间工具输出。对于每种能力，样例在该能力内按 $i=1,\ldots,N_\kappa$ 编号。我们定义

> <span style="color:#3B82F6"><strong>Para. 100:</strong></span>

> $\mathrm{CII}_{\kappa} = \frac{100}{N_\kappa} \sum_{i=1}^{N_\kappa} s_\kappa(\hat{o}_i,o_i^*),$

> <span style="color:#F59E0B"><strong>Para. 100[CN]:</strong></span>

> $\mathrm{CII}_{\kappa} = \frac{100}{N_\kappa} \sum_{i=1}^{N_\kappa} s_\kappa(\hat{o}_i,o_i^*),$

> <span style="color:#3B82F6"><strong>Para. 101:</strong></span> where $N_\kappa$ is the number of samples for capability $\kappa$ and $s_\kappa\in[0,1]$ is a capability-specific similarity function. Because the Pose interface supports both object orientation and camera motion, we evaluate these two modes separately and macro-average them as defined below. Unless stated otherwise, a malformed prediction or one missing a required field receives zero similarity.

> <span style="color:#F59E0B"><strong>Para. 101[CN]:</strong></span> 其中，$N_\kappa$ 是能力 $\kappa$ 的样例数，$s_\kappa\in[0,1]$ 是特定于能力的相似度函数。由于 Pose 接口同时支持对象朝向和相机运动，我们分别评估这两种模式，并按下文定义对其进行宏平均。除非另有说明，格式错误或缺少必需字段的预测会得到零相似度。

> **Para. 31: Locate.** Let $\hat{\mathcal B}_i$ and $\mathcal B_i^*$ be the predicted and reference box sets. We obtain a one-to-one Hungarian matching $M_i^{\mathrm{box}}$ that maximizes total pairwise IoU and define

> **Para. 31[CN]: Locate。** 令 $\hat{\mathcal B}_i$ 和 $\mathcal B_i^*$ 分别为预测框集合和参考框集合。我们获得一个使成对 IoU 总和最大的一对一匈牙利匹配 $M_i^{\mathrm{box}}$，并定义

> <span style="color:#3B82F6"><strong>Para. 102:</strong></span>

> $s_{\mathrm{Locate}}(\hat{o}_i,o_i^*) = \frac{\sum_{(m,n)\in M_i^{\mathrm{box}}} \operatorname{IoU}(\hat{b}_{i,m},b_{i,n}^*)} {\max(|\hat{\mathcal B}_i|,|\mathcal B_i^*|)}.$

> <span style="color:#F59E0B"><strong>Para. 102[CN]:</strong></span>

> $s_{\mathrm{Locate}}(\hat{o}_i,o_i^*) = \frac{\sum_{(m,n)\in M_i^{\mathrm{box}}} \operatorname{IoU}(\hat{b}_{i,m},b_{i,n}^*)} {\max(|\hat{\mathcal B}_i|,|\mathcal B_i^*|)}.$

> <span style="color:#3B82F6"><strong>Para. 103:</strong></span> This denominator assigns zero contribution to every unmatched prediction or reference box. If both sets are empty, the similarity is defined as one.

> <span style="color:#F59E0B"><strong>Para. 103[CN]:</strong></span> 该分母使每个未匹配的预测框或参考框贡献为零。如果两个集合均为空，则相似度定义为一。

> **Para. 34: Segment.** Let $\hat{\mathcal S}_i$ and $\mathcal S_i^*$ be the predicted and reference instance-mask sets after rasterizing each `polygon_2d` at the original image resolution. Using the IoU-maximizing Hungarian matching $M_i^{\mathrm{mask}}$, we define

> **Para. 34[CN]: Segment。** 令 $\hat{\mathcal S}_i$ 和 $\mathcal S_i^*$ 分别为在原始图像分辨率下栅格化每个 `polygon_2d` 后得到的预测实例掩码集合和参考实例掩码集合。使用使 IoU 最大的匈牙利匹配 $M_i^{\mathrm{mask}}$，我们定义

> <span style="color:#3B82F6"><strong>Para. 104:</strong></span>

> $s_{\mathrm{Segment}}(\hat{o}_i,o_i^*) = \frac{\sum_{(j,k)\in M_i^{\mathrm{mask}}} \operatorname{IoU}(\hat{m}_{i,j},m_{i,k}^*)} {\max(|\hat{\mathcal S}_i|,|\mathcal S_i^*|)}.$

> <span style="color:#F59E0B"><strong>Para. 104[CN]:</strong></span>

> $s_{\mathrm{Segment}}(\hat{o}_i,o_i^*) = \frac{\sum_{(j,k)\in M_i^{\mathrm{mask}}} \operatorname{IoU}(\hat{m}_{i,j},m_{i,k}^*)} {\max(|\hat{\mathcal S}_i|,|\mathcal S_i^*|)}.$

> <span style="color:#3B82F6"><strong>Para. 105:</strong></span> As in Locate, unmatched instances contribute zero, and two empty sets receive similarity one.

> <span style="color:#F59E0B"><strong>Para. 105[CN]:</strong></span> 与 Locate 一样，未匹配实例的贡献为零，两个空集合的相似度为一。

> **Para. 37: Depth.** Let $\mathcal P_i$ be the nonempty set of reference query points with valid metric-depth outputs, and let $\hat{d}_{i,p}$ and $d_{i,p}^*$ be the predicted and reference depths at point $p$. Predicted entries are matched to reference queries by `point_2d`. If a required point is missing or duplicated, or if the prediction contains an unrequested point, the sample receives zero similarity; otherwise, using $\epsilon_d=10^{-6}$ for numerical stability, we compute

> **Para. 37[CN]: Depth。** 令 $\mathcal P_i$ 为具有有效公制深度输出的非空参考查询点集合，并令 $\hat{d}_{i,p}$ 和 $d_{i,p}^*$ 分别为点 $p$ 处的预测深度和参考深度。预测条目通过 `point_2d` 与参考查询匹配。如果某个必需点缺失或重复，或者预测包含未请求的点，则该样例的相似度为零；否则，为保证数值稳定性，使用 $\epsilon_d=10^{-6}$，我们计算

> <span style="color:#3B82F6"><strong>Para. 106:</strong></span>

> $\mathrm{AbsRel}_i = \frac{1}{|\mathcal P_i|} \sum_{p\in\mathcal P_i} \frac{|\hat{d}_{i,p}-d_{i,p}^*|} {\max(d_{i,p}^*,\epsilon_d)}.$

> <span style="color:#F59E0B"><strong>Para. 106[CN]:</strong></span>

> $\mathrm{AbsRel}_i = \frac{1}{|\mathcal P_i|} \sum_{p\in\mathcal P_i} \frac{|\hat{d}_{i,p}-d_{i,p}^*|} {\max(d_{i,p}^*,\epsilon_d)}.$

> <span style="color:#3B82F6"><strong>Para. 107:</strong></span> Because lower AbsRel indicates better depth prediction, we convert it to a bounded similarity with

> <span style="color:#F59E0B"><strong>Para. 107[CN]:</strong></span> 由于较低的 AbsRel 表示更好的深度预测，我们将其转换为有界相似度：

> <span style="color:#3B82F6"><strong>Para. 108:</strong></span>

> $s_{\mathrm{Depth}}(\hat{o}_i,o_i^*)=\exp(-\mathrm{AbsRel}_i).$

> <span style="color:#F59E0B"><strong>Para. 108[CN]:</strong></span>

> $s_{\mathrm{Depth}}(\hat{o}_i,o_i^*)=\exp(-\mathrm{AbsRel}_i).$

> <span style="color:#3B82F6"><strong>Para. 109:</strong></span> Metric depth is evaluated directly without median or scale alignment.

> <span style="color:#F59E0B"><strong>Para. 109[CN]:</strong></span> 公制深度直接进行评估，不采用中位数或尺度对齐。

> **Para. 42: Pose.** The Pose interface has two modes whose outputs are discrete spatial directions rather than rotation matrices. For an object-orientation query, we evaluate the canonical `facing_direction_camera` field. We use the following circular angle mapping:

> **Para. 42[CN]: Pose。** Pose 接口有两种模式，其输出是离散空间方向而非旋转矩阵。对于对象朝向查询，我们评估规范的 `facing_direction_camera` 字段。我们使用以下圆周角映射：

> <span style="color:#3B82F6"><strong>Para. 110:</strong></span>

> ```text
> front : 0       front-right : π/4
> right : π/2     back-right : 3π/4
> back : π        back-left : 5π/4
> left : 3π/2     front-left : 7π/4
> ```

> <span style="color:#F59E0B"><strong>Para. 110[CN]:</strong></span>

> ```text
> front（前）: 0          front-right（右前）: π/4
> right（右）: π/2       back-right（右后）: 3π/4
> back（后）: π          back-left（左后）: 5π/4
> left（左）: 3π/2       front-left（左前）: 7π/4
> ```

> <span style="color:#3B82F6"><strong>Para. 111:</strong></span> Let $\hat{\phi}_i$ and $\phi_i^*$ be the predicted and reference angles, and define their circular distance as

> <span style="color:#F59E0B"><strong>Para. 111[CN]:</strong></span> 令 $\hat{\phi}_i$ 和 $\phi_i^*$ 分别为预测角和参考角，并将它们的圆周距离定义为

> <span style="color:#3B82F6"><strong>Para. 112:</strong></span>

> $\Delta\phi_i = \min\left( |\hat{\phi}_i-\phi_i^*|, 2\pi-|\hat{\phi}_i-\phi_i^*| \right).$

> <span style="color:#F59E0B"><strong>Para. 112[CN]:</strong></span>

> $\Delta\phi_i = \min\left( |\hat{\phi}_i-\phi_i^*|, 2\pi-|\hat{\phi}_i-\phi_i^*| \right).$

> <span style="color:#3B82F6"><strong>Para. 113:</strong></span> The object-orientation similarity is

> <span style="color:#F59E0B"><strong>Para. 113[CN]:</strong></span> 对象朝向相似度为

> <span style="color:#3B82F6"><strong>Para. 114:</strong></span>

> $s_{\mathrm{obj},i}=\max(0,\cos\Delta\phi_i).$

> <span style="color:#F59E0B"><strong>Para. 114[CN]:</strong></span>

> $s_{\mathrm{obj},i}=\max(0,\cos\Delta\phi_i).$

> ---

> ## Page 29

> <span style="color:#3B82F6"><strong>Para. 115:</strong></span> The auxiliary `visible_side` field and the returned box are not included in this score; localization is evaluated separately by Locate CII.

> <span style="color:#F59E0B"><strong>Para. 115[CN]:</strong></span> 辅助字段 `visible_side` 和返回的框不计入该分数；定位由 Locate CII 单独评估。

> <span style="color:#3B82F6"><strong>Para. 116:</strong></span> For a camera-motion query, we evaluate translation and view rotation separately from the signed axes returned by `position.axes` and `view_rotation.dominant_axis`. Let $\operatorname{vec}(\alpha)$ be the unit vector denoted by signed axis $\alpha$, where, for example, $\operatorname{vec}(+X)=(1,0,0)$ and $\operatorname{vec}(-Z)=(0,0,-1)$, and define

> <span style="color:#F59E0B"><strong>Para. 116[CN]:</strong></span> 对于相机运动查询，我们根据 `position.axes` 和 `view_rotation.dominant_axis` 返回的带符号坐标轴，分别评估平移和视图旋转。令 $\operatorname{vec}(\alpha)$ 表示带符号轴 $\alpha$ 所指代的单位向量；例如，$\operatorname{vec}(+X)=(1,0,0)$，$\operatorname{vec}(-Z)=(0,0,-1)$。定义

> <span style="color:#3B82F6"><strong>Para. 117:</strong></span>

> $\operatorname{dir}(A) = \frac{\sum_{\alpha\in A}\operatorname{vec}(\alpha)} {\left\lVert\sum_{\alpha\in A}\operatorname{vec}(\alpha)\right\rVert_2}.$

> <span style="color:#F59E0B"><strong>Para. 117[CN]:</strong></span>

> $\operatorname{dir}(A) = \frac{\sum_{\alpha\in A}\operatorname{vec}(\alpha)} {\left\lVert\sum_{\alpha\in A}\operatorname{vec}(\alpha)\right\rVert_2}.$

> <span style="color:#3B82F6"><strong>Para. 118:</strong></span> This mapping is defined only for a nonempty signed-axis set with a nonzero vector sum. Using $\hat{A}_i^{\mathrm{trans}}$ for the translation axes and the singleton $A_i^{\mathrm{rot}}$ containing the dominant rotation axis, we define

> <span style="color:#F59E0B"><strong>Para. 118[CN]:</strong></span> 该映射仅对向量和非零的非空带符号轴集合有定义。使用 $\hat{A}_i^{\mathrm{trans}}$ 表示平移轴，并使用包含主导旋转轴的单元素集合 $A_i^{\mathrm{rot}}$，我们定义

> <span style="color:#3B82F6"><strong>Para. 119:</strong></span>

> $s_{\mathrm{trans},i} = \max\left( 0, \operatorname{dir}(\hat{A}_i^{\mathrm{trans}})^{\mathsf T} \operatorname{dir}(A_i^{\mathrm{trans},*}) \right),$

> $s_{\mathrm{rot},i} = \max\left( 0, \operatorname{dir}(\hat{A}_i^{\mathrm{rot}})^{\mathsf T} \operatorname{dir}(A_i^{\mathrm{rot},*}) \right),$

> <span style="color:#F59E0B"><strong>Para. 119[CN]:</strong></span>

> $s_{\mathrm{trans},i} = \max\left( 0, \operatorname{dir}(\hat{A}_i^{\mathrm{trans}})^{\mathsf T} \operatorname{dir}(A_i^{\mathrm{trans},*}) \right),$

> $s_{\mathrm{rot},i} = \max\left( 0, \operatorname{dir}(\hat{A}_i^{\mathrm{rot}})^{\mathsf T} \operatorname{dir}(A_i^{\mathrm{rot},*}) \right),$

> <span style="color:#3B82F6"><strong>Para. 120:</strong></span> and

> <span style="color:#F59E0B"><strong>Para. 120[CN]:</strong></span> 以及

> <span style="color:#3B82F6"><strong>Para. 121:</strong></span>

> $s_{\mathrm{cam},i} = \frac{s_{\mathrm{trans},i}+s_{\mathrm{rot},i}}{2}.$

> <span style="color:#F59E0B"><strong>Para. 121[CN]:</strong></span>

> $s_{\mathrm{cam},i} = \frac{s_{\mathrm{trans},i}+s_{\mathrm{rot},i}}{2}.$

> <span style="color:#3B82F6"><strong>Para. 122:</strong></span> For Pose, an unrecognized direction label or an axis set for which $\operatorname{dir}(A)$ is undefined receives zero similarity. Finally, to prevent the more frequent query mode from dominating the metric, we compute

> <span style="color:#F59E0B"><strong>Para. 122[CN]:</strong></span> 对于 Pose，无法识别的方向标签，或使 $\operatorname{dir}(A)$ 无定义的轴集合，均得到零相似度。最后，为防止出现频率更高的查询模式主导该指标，我们计算

> <span style="color:#3B82F6"><strong>Para. 123:</strong></span>

> $\mathrm{CII}_{\mathrm{obj}} = \frac{100}{N_{\mathrm{obj}}} \sum_{i=1}^{N_{\mathrm{obj}}} s_{\mathrm{obj},i},$

> $\mathrm{CII}_{\mathrm{cam}} = \frac{100}{N_{\mathrm{cam}}} \sum_{i=1}^{N_{\mathrm{cam}}} s_{\mathrm{cam},i}.$

> $\mathrm{CII}_{\mathrm{Pose}} = \frac{\mathrm{CII}_{\mathrm{obj}}+\mathrm{CII}_{\mathrm{cam}}}{2}.$

> <span style="color:#F59E0B"><strong>Para. 123[CN]:</strong></span>

> $\mathrm{CII}_{\mathrm{obj}} = \frac{100}{N_{\mathrm{obj}}} \sum_{i=1}^{N_{\mathrm{obj}}} s_{\mathrm{obj},i},$

> $\mathrm{CII}_{\mathrm{cam}} = \frac{100}{N_{\mathrm{cam}}} \sum_{i=1}^{N_{\mathrm{cam}}} s_{\mathrm{cam},i}.$

> $\mathrm{CII}_{\mathrm{Pose}} = \frac{\mathrm{CII}_{\mathrm{obj}}+\mathrm{CII}_{\mathrm{cam}}}{2}.$

> <span style="color:#3B82F6"><strong>Para. 124:</strong></span> Here, $N_{\mathrm{obj}}>0$ and $N_{\mathrm{cam}}>0$ are the numbers of object-orientation and camera-motion samples, respectively. We additionally report the two components separately. The four-capability macro-average reported in the main paper is

> <span style="color:#F59E0B"><strong>Para. 124[CN]:</strong></span> 这里，$N_{\mathrm{obj}}>0$ 和 $N_{\mathrm{cam}}>0$ 分别是对象朝向样例数和相机运动样例数。我们还分别报告这两个组成部分。主论文中报告的四能力宏平均为

> <span style="color:#3B82F6"><strong>Para. 125:</strong></span>

> $\mathrm{CII}_{\mathrm{macro}} = \frac{ \mathrm{CII}_{\mathrm{Locate}} + \mathrm{CII}_{\mathrm{Segment}} + \mathrm{CII}_{\mathrm{Depth}} + \mathrm{CII}_{\mathrm{Pose}} }{4}.$

> <span style="color:#F59E0B"><strong>Para. 125[CN]:</strong></span>

> $\mathrm{CII}_{\mathrm{macro}} = \frac{ \mathrm{CII}_{\mathrm{Locate}} + \mathrm{CII}_{\mathrm{Segment}} + \mathrm{CII}_{\mathrm{Depth}} + \mathrm{CII}_{\mathrm{Pose}} }{4}.$

> <span style="color:#3B82F6"><strong>Para. 126:</strong></span> All capability-specific similarities lie in $[0,1]$ and equal one for an exact match; lower values indicate greater divergence from the spatial-tool output. Every capability-level CII and $\mathrm{CII}_{\mathrm{macro}}$ therefore lie in $[0,100]$, with a higher value indicating stronger internalization.

> <span style="color:#F59E0B"><strong>Para. 126[CN]:</strong></span> 所有特定于能力的相似度均位于 $[0,1]$ 内，精确匹配时等于一；较低的值表示与空间工具输出的偏离更大。因此，每个能力级 CII 和 $\mathrm{CII}_{\mathrm{macro}}$ 均位于 $[0,100]$ 内，数值越高表示内化越强。

> **Para. 60: F Additional Experiments**

> **Para. 60[CN]: F 附加实验**

> **Para. 61: F.1 Comparison with Direct Fine-Tuning**

> **Para. 61[CN]: F.1 与直接微调的比较**

> <span style="color:#3B82F6"><strong>Para. 127:</strong></span> Table 9 compares conventional Direct fine-tuning with inference-time tool augmentation, agentic fine-tuning, and capability internalization on SpatialCLI-Bench using Qwen3-VL-8B-Instruct. Every variant is evaluated both w/o Tools and w/ Tools. For Direct variants, w/ Tools evaluation exposes the same spatial-tool interfaces at inference time, even though their training does not include explicit tool-interaction supervision.

> <span style="color:#F59E0B"><strong>Para. 127[CN]:</strong></span> 表 9 使用 Qwen3-VL-8B-Instruct，在 SpatialCLI-Bench 上比较了传统直接微调、推理时工具增强、智能体式微调和能力内化。每个变体均在 w/o Tools 和 w/ Tools 两种条件下评估。对于 Direct 变体，w/ Tools 评估会在推理时公开相同的空间工具接口，尽管其训练不包含显式的工具交互监督。

> ---

> ## Page 30

> <span style="color:#3B82F6"><strong>Para. 128:</strong></span>

> | Stage | Conventional Direct Fine-Tuning: Variant | w/o Tools | w/ Tools | Agentic / SpatialCLI: Variant | w/o Tools | w/ Tools |
> |---|---|---:|---:|---|---:|---:|
> | Inference Only | Initial Model | 35.3 | 66.5 | Initial Model | 35.3 | 66.5 |
> | SFT | SFT w/o Tools | 41.3 | 40.3 | SFT w/ Tools | 41.1 | 86.4 |
> | RL w/o SFT | RL w/o Tools w/o SFT | 52.7 | 68.2 | RL w/ Tools w/o SFT | 37.2 | 90.5 |
> | RL + SFT | RL w/o Tools + SFT | 51.6 | 48.1 | RL w/ Tools + SFT | 40.1 | 91.3 |
> | Internalization | – | – | – | SpatialCLI-8B | **72.7** | **91.3** |

> <span style="color:#F59E0B"><strong>Para. 128[CN]:</strong></span>

> | 阶段 | 传统直接微调：变体 | 无工具 | 有工具 | 智能体式／SpatialCLI：变体 | 无工具 | 有工具 |
> |---|---|---:|---:|---|---:|---:|
> | 仅推理 | 初始模型 | 35.3 | 66.5 | 初始模型 | 35.3 | 66.5 |
> | SFT | 无工具 SFT | 41.3 | 40.3 | 有工具 SFT | 41.1 | 86.4 |
> | 无 SFT 的 RL | 无工具且无 SFT 的 RL | 52.7 | 68.2 | 有工具且无 SFT 的 RL | 37.2 | 90.5 |
> | RL + SFT | 无工具 RL + SFT | 51.6 | 48.1 | 有工具 RL + SFT | 40.1 | 91.3 |
> | 内化 | – | – | – | SpatialCLI-8B | **72.7** | **91.3** |

> **Para. 64: Table 9** Comparison with conventional Direct fine-tuning on SpatialCLI-Bench. Variant names specify training configurations, while w/o Tools and w/ Tools denote inference settings. SpatialCLI-8B is obtained by Dual-View Capability Internalization after RL w/ Tools + SFT.

> **Para. 64[CN]: 表 9** 在 SpatialCLI-Bench 上与传统直接微调进行比较。变体名称说明训练配置，而 w/o Tools 和 w/ Tools 表示推理设置。SpatialCLI-8B 是在 RL w/ Tools + SFT 之后通过双视图能力内化获得的。

> <span style="color:#3B82F6"><strong>Para. 129:</strong></span> The Inference Only row uses the same initial checkpoint on both sides; its Inference w/ Tools result denotes enabling the spatial tools without fine-tuning. Inference-time tool augmentation alone yields a clear improvement w/ Tools, showing that spatial tools effectively compensate for the fine-grained perceptual limitations of the initial model. SFT w/ Tools learns the basic tool-interaction protocol, while RL w/ Tools w/o SFT optimizes tool selection and termination from task feedback without Cold-Start SFT. SFT w/ Tools raises the w/ Tools score from 66.5 to 86.4, and RL w/ Tools + SFT further raises it to 91.3. Although RL w/ Tools w/o SFT eventually reaches 90.5, the training dynamics in Figure 3 show that it does so with substantially longer and more tool-intensive trajectories. Capability internalization then raises the w/o Tools score from 40.1 to 72.7 while preserving the 91.3 w/ Tools score reached by RL w/ Tools + SFT. In contrast, SFT w/o Tools, RL w/o Tools w/o SFT, and RL w/o Tools + SFT improve the w/o Tools score but do not acquire a comparably strong tool-use policy. The results therefore isolate complementary roles for the three stages: immediate perceptual support, stable tool-policy learning, and transfer of tool-supplied capabilities into w/o Tools inference.

> <span style="color:#F59E0B"><strong>Para. 129[CN]:</strong></span> Inference Only 行在两侧使用相同的初始检查点；其中 Inference w/ Tools 结果表示在不进行微调的情况下启用空间工具。仅进行推理时工具增强就能在 w/ Tools 条件下带来明显提升，这表明空间工具有效弥补了初始模型在细粒度感知方面的局限。SFT w/ Tools 学习基本的工具交互协议，而 RL w/ Tools w/o SFT 则在没有冷启动 SFT 的情况下，根据任务反馈优化工具选择和终止。SFT w/ Tools 将 w/ Tools 分数从 66.5 提升至 86.4，RL w/ Tools + SFT 又进一步将其提升至 91.3。尽管 RL w/ Tools w/o SFT 最终达到 90.5，但图 3 中的训练动态表明，它通过明显更长且工具使用更密集的轨迹才达到这一水平。随后，能力内化将 w/o Tools 分数从 40.1 提升至 72.7，同时保留 RL w/ Tools + SFT 达到的 91.3 w/ Tools 分数。相比之下，SFT w/o Tools、RL w/o Tools w/o SFT 和 RL w/o Tools + SFT 虽然提高了 w/o Tools 分数，却没有获得同等强大的工具使用策略。因此，这些结果分离出了三个阶段的互补作用：即时感知支持、稳定的工具策略学习，以及将工具提供的能力迁移至 w/o Tools 推理。

> **Para. 66: F.2 Tool-Set Ablation**

> **Para. 66[CN]: F.2 工具集消融**

> <span style="color:#3B82F6"><strong>Para. 130:</strong></span> To isolate the contribution of each spatial-tool group, we evaluate the initial Qwen3-VL-8B-Instruct checkpoint while varying only the registered tool set. The task inputs, shared agentic prompt template, decoding configuration, and evaluation protocol remain identical across variants. Each single-tool variant exposes only one of the Locate, Segment, Depth, or Pose interfaces, whereas All Tools exposes all four interfaces. The evaluated benchmarks, subsets, metrics, and reporting order exactly match those in the main-paper overall results (Table 1). Table 10 reports the resulting benchmark scores.

> <span style="color:#F59E0B"><strong>Para. 130[CN]:</strong></span> 为了分离每组空间工具的贡献，我们仅改变已注册工具集，对初始 Qwen3-VL-8B-Instruct 检查点进行评估。各变体的任务输入、共享智能体提示模板、解码配置和评估协议均保持相同。每个单工具变体仅公开 Locate、Segment、Depth 或 Pose 接口之一，而 All Tools 则公开全部四个接口。所评估的基准、子集、指标和报告顺序与主论文总体结果（表 1）完全一致。表 10 报告了所得基准分数。

> <span style="color:#3B82F6"><strong>Para. 131:</strong></span>

> | Model / Tool Set | SpatialCLI Bench | MindCube | MMSI Motion-Cam | MMSI Pos-Cam-Cam | DA-2K | BOPASK Traj. | BOPASK ObjRjr | Avg. |
> |---|---:|---:|---:|---:|---:|---:|---:|---:|
> | Qwen3-VL-8B-Instruct | 35.3 | 29.3 | 27.0 | 25.8 | 68.1 | 25.8 | 13.3 | 35.7 |
> | + Locate Only | 31.8 | 32.4 | 24.3 | 30.1 | 46.6 | 53.7 | 19.3 | 34.9 |
> | + Segment Only | 39.0 | 26.3 | 27.0 | 28.0 | 57.0 | 43.0 | **21.0** | 36.3 |
> | + Depth Only | 40.1 | 27.3 | 24.3 | 26.9 | **91.6** | 22.7 | 14.1 | 40.6 |
> | + Pose Only | 50.4 | 44.5 | 37.8 | 38.7 | 52.0 | 4.1 | 1.4 | 37.6 |
> | + All Tools | **66.5** | **47.2** | **41.9** | **39.8** | **91.6** | **54.3** | 20.6 | **56.7** |

> <span style="color:#F59E0B"><strong>Para. 131[CN]:</strong></span>

> | 模型／工具集 | SpatialCLI Bench | MindCube | MMSI Motion-Cam | MMSI Pos-Cam-Cam | DA-2K | BOPASK Traj. | BOPASK ObjRjr | 平均值 |
> |---|---:|---:|---:|---:|---:|---:|---:|---:|
> | Qwen3-VL-8B-Instruct | 35.3 | 29.3 | 27.0 | 25.8 | 68.1 | 25.8 | 13.3 | 35.7 |
> | + 仅 Locate | 31.8 | 32.4 | 24.3 | 30.1 | 46.6 | 53.7 | 19.3 | 34.9 |
> | + 仅 Segment | 39.0 | 26.3 | 27.0 | 28.0 | 57.0 | 43.0 | **21.0** | 36.3 |
> | + 仅 Depth | 40.1 | 27.3 | 24.3 | 26.9 | **91.6** | 22.7 | 14.1 | 40.6 |
> | + 仅 Pose | 50.4 | 44.5 | 37.8 | 38.7 | 52.0 | 4.1 | 1.4 | 37.6 |
> | + 所有工具 | **66.5** | **47.2** | **41.9** | **39.8** | **91.6** | **54.3** | 20.6 | **56.7** |

> **Para. 69: Table 10** Tool-set ablation of the initial Qwen3-VL-8B-Instruct model. Single-tool variants expose only the named interface, while All Tools exposes Locate, Segment, Depth, and Pose. Avg. follows the benchmark-level macro-averaging used in main-paper Table 1. The best result in each column is bolded, including ties.

> **Para. 69[CN]: 表 10** 初始 Qwen3-VL-8B-Instruct 模型的工具集消融。单工具变体仅公开所命名的接口，而 All Tools 公开 Locate、Segment、Depth 和 Pose。Avg. 遵循主论文表 1 使用的基准级宏平均。每列最佳结果均以粗体表示，包括并列结果。

> <span style="color:#3B82F6"><strong>Para. 132:</strong></span> The single-tool variants exhibit clear capability-aligned specialization. Depth alone matches All Tools on DA-2K (91.6); among the single-tool settings, Pose performs best on SpatialCLI-Bench, MindCube, and both MMSI subsets, while Locate and Segment are most effective on BOPASK-Trajectory and BOPASK-Object-Rearrangement, respectively. No single tool is uniformly beneficial across benchmarks. Jointly exposing all four tools raises the macro-average from 35.7 to 56.7 and achieves the best or tied-best result on six of the seven reported evaluations, supporting the complementarity of the four spatial interfaces.

> <span style="color:#F59E0B"><strong>Para. 132[CN]:</strong></span> 单工具变体表现出明显的能力对齐专门化。仅使用 Depth 在 DA-2K 上与 All Tools 持平（91.6）；在单工具设置中，Pose 在 SpatialCLI-Bench、MindCube 和两个 MMSI 子集上表现最佳，而 Locate 和 Segment 分别在 BOPASK-Trajectory 和 BOPASK-Object-Rearrangement 上最有效。没有任何单一工具能在所有基准上统一带来收益。联合公开全部四个工具将宏平均从 35.7 提升至 56.7，并在所报告的七项评估中的六项上取得最佳或并列最佳结果，从而支持四种空间接口之间的互补性。

> ---

> ## Page 31

> **Para. 71: F.3 Tool-Use Behavior across Internalization Variants**

> **Para. 71[CN]: F.3 各内化变体的工具使用行为**

> <span style="color:#3B82F6"><strong>Para. 133:</strong></span> To complement the score and output-length ablation in main-paper Table 3, Table 11 reports the actual tool invocations made by each capability-internalization variant w/ Tools across all evaluated benchmarks. We report the mean number of tool calls over all samples, the percentage of samples that invoke at least one tool, and the mean number of calls among those samples. To reveal each variant’s unconstrained calling tendency, this diagnostic retains the maximum generation length of 40,960 tokens but does not apply the ten-call cap used in the task-performance evaluations.

> <span style="color:#F59E0B"><strong>Para. 133[CN]:</strong></span> 为补充主论文表 3 中的分数和输出长度消融，表 11 报告了每个能力内化变体在所有已评估基准的 w/ Tools 条件下实际进行的工具调用。我们报告所有样例上的平均工具调用次数、至少调用一次工具的样例百分比，以及这些样例中的平均调用次数。为了揭示每个变体不受约束的调用倾向，该诊断保留 40,960 个 token 的最大生成长度，但不应用任务性能评估所使用的十次调用上限。

> <span style="color:#3B82F6"><strong>Para. 134:</strong></span>

> | Internalization Variant | Mean Tool Calls | Calling Samples (%) | Calls per Calling Sample |
> |---|---:|---:|---:|
> | Qwen3-VL-8B-Instruct | 2.00 | 99.3 | 2.02 |
> | Final Answer Only | 0.00 | 0.0 | 0.00 |
> | CoT + Answer | 0.01 | 0.4 | 1.95 |
> | Internalization View Only | 20.70 | 40.3 | 51.35 |
> | Tool-Use View Only | 1.28 | 81.0 | 1.58 |
> | Full Dual-View | 1.27 | 81.5 | 1.56 |

> <span style="color:#F59E0B"><strong>Para. 134[CN]:</strong></span>

> | 内化变体 | 平均工具调用次数 | 调用工具的样例（%） | 每个调用样例的调用次数 |
> |---|---:|---:|---:|
> | Qwen3-VL-8B-Instruct | 2.00 | 99.3 | 2.02 |
> | 仅最终答案 | 0.00 | 0.0 | 0.00 |
> | CoT + 答案 | 0.01 | 0.4 | 1.95 |
> | 仅内化视图 | 20.70 | 40.3 | 51.35 |
> | 仅工具使用视图 | 1.28 | 81.0 | 1.58 |
> | 完整双视图 | 1.27 | 81.5 | 1.56 |

> **Para. 74: Table 11** Tool-use behavior of capability-internalization variants averaged across all benchmarks evaluated in this paper w/ Tools.

> **Para. 74[CN]: 表 11** 在本文评估的所有基准上取平均的能力内化变体工具使用行为，评估条件为 w/ Tools。

> <span style="color:#3B82F6"><strong>Para. 135:</strong></span> The initial model calls tools on 99.3% of samples, averaging 2.00 calls per sample. Final Answer Only never calls a tool, while CoT + Answer does so on only 0.4% of samples. Internalization View Only calls tools on 40.3% of samples, but averages 51.35 calls within those samples and 20.70 calls overall. This excessive number of calls indicates unstable and repetitive tool use rather than effective interaction. By contrast, Tool-Use View Only and Full Dual-View exhibit nearly identical controlled behavior: they call tools on 81.0% and 81.5% of samples and average 1.28 and 1.27 calls overall, respectively. Thus, dual-view training preserves the tool-use behavior learned from the tool-use view while obtaining the score and compact w/o Tools reasoning benefits reported in main-paper Table 3.

> <span style="color:#F59E0B"><strong>Para. 135[CN]:</strong></span> 初始模型在 99.3% 的样例上调用工具，平均每个样例调用 2.00 次。Final Answer Only 从不调用工具，而 CoT + Answer 仅在 0.4% 的样例上调用工具。Internalization View Only 在 40.3% 的样例上调用工具，但在这些样例中平均调用 51.35 次，总体平均调用 20.70 次。如此过多的调用表明其工具使用不稳定且重复，而不是有效交互。相比之下，Tool-Use View Only 和 Full Dual-View 表现出几乎相同的受控行为：二者分别在 81.0% 和 81.5% 的样例上调用工具，总体平均调用次数分别为 1.28 和 1.27。因此，双视图训练在获得主论文表 3 所报告的分数提升和紧凑 w/o Tools 推理优势的同时，保留了从工具使用视图中学到的工具使用行为。

> **Para. 76: F.4 Sensitivity to the Tool-Use View Loss Weight**

> **Para. 76[CN]: F.4 对工具使用视图损失权重的敏感性**

> <span style="color:#3B82F6"><strong>Para. 136:</strong></span> To study the trade-off controlled by the Tool-Use View loss weight in $\mathcal L_{\mathrm{CII}}=\mathcal L_{\mathrm{internal}}+\lambda\mathcal L_{\mathrm{agentic}}$, we compare $\lambda\in\{0.2,0.5,1.0,1.5\}$ using Qwen3-VL-8B-Instruct. All variants use the same training data, optimization configuration, training steps, and checkpoint-selection protocol. We evaluate the four-capability macro-average CII together with w/o Tools and w/ Tools performance on SpatialCLI-Bench, thereby measuring both capability internalization and tool-use retention. Table 12 reports the resulting sensitivity analysis.

> <span style="color:#F59E0B"><strong>Para. 136[CN]:</strong></span> 为研究工具使用视图损失权重在 $\mathcal L_{\mathrm{CII}}=\mathcal L_{\mathrm{internal}}+\lambda\mathcal L_{\mathrm{agentic}}$ 中控制的权衡，我们使用 Qwen3-VL-8B-Instruct 比较 $\lambda\in\{0.2,0.5,1.0,1.5\}$。所有变体均使用相同的训练数据、优化配置、训练步数和检查点选择协议。我们同时评估四能力宏平均 CII，以及 SpatialCLI-Bench 上的 w/o Tools 和 w/ Tools 性能，从而同时衡量能力内化和工具使用保留。表 12 报告了所得敏感性分析。

> <span style="color:#3B82F6"><strong>Para. 137:</strong></span>

> | $\lambda$ | CII Macro | SpatialCLI-Bench w/o Tools | SpatialCLI-Bench w/ Tools |
> |---:|---:|---:|---:|
> | 0.2 | 60.8 | 72.5 | 89.2 |
> | **0.5 (Ours)** | 60.8 | 72.7 | 91.3 |
> | 1.0 | 60.5 | 72.3 | 91.4 |
> | 1.5 | 55.6 | 62.9 | 91.4 |

> <span style="color:#F59E0B"><strong>Para. 137[CN]:</strong></span>

> | $\lambda$ | CII 宏平均 | SpatialCLI-Bench 无工具 | SpatialCLI-Bench 有工具 |
> |---:|---:|---:|---:|
> | 0.2 | 60.8 | 72.5 | 89.2 |
> | **0.5（本文方法）** | 60.8 | 72.7 | 91.3 |
> | 1.0 | 60.5 | 72.3 | 91.4 |
> | 1.5 | 55.6 | 62.9 | 91.4 |

> **Para. 79: Table 12** Sensitivity to the Tool-Use View loss weight $\lambda$ with Qwen3-VL-8B-Instruct. CII Macro averages Locate, Segment, Depth, and Pose, where Pose macro-averages object orientation and camera motion.

> **Para. 79[CN]: 表 12** 使用 Qwen3-VL-8B-Instruct 时对工具使用视图损失权重 $\lambda$ 的敏感性。CII Macro 对 Locate、Segment、Depth 和 Pose 取平均，其中 Pose 对对象朝向和相机运动进行宏平均。

> <span style="color:#3B82F6"><strong>Para. 138:</strong></span> The results reveal a clear trade-off between capability internalization and tool-policy retention. Reducing $\lambda$ to 0.2 leaves CII and w/o Tools performance comparable to $\lambda=0.5$, but lowers w/ Tools performance from 91.3 to 89.2, suggesting that underweighting the Tool-Use View weakens retention of the learned tool-use policy. Increasing $\lambda$ to 1.0 maintains w/ Tools performance at 91.4 while slightly reducing CII and w/o Tools performance; further increasing it to 1.5 substantially lowers CII and w/o Tools performance to 55.6 and 62.9 without an additional w/ Tools gain. Therefore, $\lambda=0.5$ provides the most balanced trade-off rather than maximizing either training view alone.

> <span style="color:#F59E0B"><strong>Para. 138[CN]:</strong></span> 结果揭示了能力内化与工具策略保留之间的明确权衡。将 $\lambda$ 降至 0.2 时，CII 和 w/o Tools 性能仍与 $\lambda=0.5$ 相当，但 w/ Tools 性能从 91.3 降至 89.2，这表明对工具使用视图赋予过低权重会削弱对已学工具使用策略的保留。将 $\lambda$ 提高至 1.0，可使 w/ Tools 性能维持在 91.4，但会略微降低 CII 和 w/o Tools 性能；进一步提高至 1.5，则会使 CII 和 w/o Tools 性能显著降至 55.6 和 62.9，同时不会带来额外的 w/ Tools 收益。因此，$\lambda=0.5$ 提供了最均衡的权衡，而不是单独最大化任一训练视图。

> ---

> ## Page 32

> **Para. 81: G Prompt Templates**

> **Para. 81[CN]: G 提示模板**

> **Para. 82: G.1 Agentic Tool-Use Prompt Template**

> **Para. 82[CN]: G.1 智能体式工具使用提示模板**

> <span style="color:#3B82F6"><strong>Para. 139:</strong></span> The prompt injects the applicable tool registrations and examples into a shared calling protocol. The interaction permits at most ten executed tool calls per sample. After every tool result, SpatialCLI appends `[Tool-call budget: at most N more tool calls can be made.]`; when the budget reaches zero, it instead appends `[Tool-call budget exhausted: no more tool calls are allowed. Answer the question immediately using the available information.]`. In thinking mode, the complete thinking content is retained in the multi-turn history and passed back to the model in subsequent turns. The complete template is shown in Box G.1.

> <span style="color:#F59E0B"><strong>Para. 139[CN]:</strong></span> 该提示将适用的工具注册信息和示例注入共享调用协议。每个样例的交互最多允许执行十次工具调用。每次得到工具结果后，SpatialCLI 都会附加 `[Tool-call budget: at most N more tool calls can be made.]`；当预算降为零时，则改为附加 `[Tool-call budget exhausted: no more tool calls are allowed. Answer the question immediately using the available information.]`。在思考模式下，完整思考内容会保留在多轮历史记录中，并在后续轮次中再次传递给模型。完整模板见框 G.1。

> **Para. 84: Box G.1: Agentic Tool-Use Prompt Template**

> **Para. 84[CN]: 框 G.1：智能体式工具使用提示模板**

> <span style="color:#3B82F6"><strong>Para. 140:</strong></span>

> ```text
> 1  You have the following tools available.
> 2
> 3  Tool call format:
> 4  For each function call, return a JSON object with function name and arguments within <tool_call></tool_call>
>    XML tags:
> 5
> 6  <tool_call>
> 7  {"name": <function-name>, "arguments": <args-json-object>}
> 8  </tool_call>
> 9
> 10 Tool list:
> 11 <tools>
> 12 [
> 13   {tool_definitions}
> 14 ]
> 15 </tools>
> 16
> 17 Examples:
> 18 {tool_examples}
> ```

> <span style="color:#F59E0B"><strong>Para. 140[CN]:</strong></span>

> ```text
> 1  你可以使用以下工具。
> 2
> 3  工具调用格式：
> 4  对于每次函数调用，请在 <tool_call></tool_call> XML 标签内返回一个包含函数名称和参数的 JSON 对象：
> 5
> 6  <tool_call>
> 7  {"name": <function-name>, "arguments": <args-json-object>}
> 8  </tool_call>
> 9
> 10 工具列表：
> 11 <tools>
> 12 [
> 13   {tool_definitions}
> 14 ]
> 15 </tools>
> 16
> 17 示例：
> 18 {tool_examples}
> ```

> **Para. 86: G.2 Turn-Wise Evidence Consolidation Prompt**

> **Para. 86[CN]: G.2 逐轮证据整合提示**

> <span style="color:#3B82F6"><strong>Para. 141:</strong></span> This prompt implements the first stage of Progressive Evidence-Grounded Trajectory Verbalization by converting one newly completed tool interaction into an evidence–reasoning unit conditioned on the visual input, task instruction, and previously consolidated units, while withholding the correct answer. Its rules are designed to preserve every exposed specialist output and explicit visual observation without promoting plans, uncertain guesses, or answer-option analysis to observed facts. The tool catalog standardizes the interpretation of heterogeneous return fields, while calibrated wording and exact-value preservation retain the uncertainty and numerical fidelity of perceptual estimates. The complete template is shown in Box G.2.

> <span style="color:#F59E0B"><strong>Para. 141[CN]:</strong></span> 该提示实现渐进式证据落地轨迹言语化的第一阶段：它将一次新完成的工具交互转换为一个以视觉输入、任务指令和先前已整合单元为条件的证据—推理单元，同时隐藏正确答案。其规则旨在保留所有已公开的专家输出和明确视觉观察，同时避免将计划、不确定猜测或答案选项分析提升为已观察事实。工具目录对异构返回字段的解释进行标准化，而经过校准的措辞和精确数值保留则维持感知估计的不确定性和数值保真度。完整模板见框 G.2。

> **Para. 88: Box G.2: Turn-Wise Evidence Consolidation Prompt**

> **Para. 88[CN]: 框 G.2：逐轮证据整合提示**

> <span style="color:#3B82F6"><strong>Para. 142:</strong></span>

> ```text
> 1  You are preparing progressive evidence-grounded capability-internalization training data. Consolidate evidence from
>    one step of a successful visual tool-use trajectory. Given the visual task, the previously consolidated
>    evidence-reasoning units, and exactly one newly completed interaction, verbalize all information exposed by the
>    current tool result and record its logical update.
> 2
> 3  Be literal, detailed, and evidence-grounded. No correct answer is provided at this stage. Do not solve from an answer
>    key. Put the structured result in the requested XML sections.
> 4
> 5  Rules:
> 6  1. Every perceptual claim must be traceable to the current tool result, an explicit visual observation written in the
>    current original reasoning, or a previous unit. Do not turn a plan, a proposed tool action, answer-option analysis, or
>    an uncertain guess into an observed fact.
> 7  2. Exhaustively verbalize every item and every field exposed by the current tool result. Preserve the returned count,
>    every instance, image index, label, bounding box, point, polygon component and vertex, depth value, pose field,
>    motion field, direction, axis, error, and other returned value. Do not shorten, sample, merge, or omit returned
>    information merely because it is lengthy or irrelevant to the task. Express machine structures as readable
> ```

> <span style="color:#F59E0B"><strong>Para. 142[CN]:</strong></span>

> ```text
> 1  你正在准备渐进式、基于证据的能力内化训练数据。请整合成功视觉工具使用轨迹中
>    一个步骤的证据。给定视觉任务、先前已整合的证据—推理单元，以及恰好一次新完成的交互，
>    将当前工具结果公开的全部信息言语化，并记录其逻辑更新。
> 2
> 3  请保持字面、详尽且以证据为依据。此阶段不提供正确答案。不要依据答案
>    键求解。将结构化结果置于所要求的 XML 区段中。
> 4
> 5  规则：
> 6  1. 每项感知主张都必须可追溯至当前工具结果、当前原始推理中写明的明确视觉观察，
>    或先前单元。不要把计划、拟议的工具操作、答案选项分析或
>    不确定猜测转变为已观察事实。
> 7  2. 详尽言语化当前工具结果公开的每个项目和每个字段。保留返回的数量、
>    每个实例、图像索引、标签、边界框、点、多边形组成部分和顶点、深度值、姿态字段、
>    运动字段、方向、坐标轴、错误和其他返回值。不要因为返回信息冗长或与任务无关而对其
>    缩短、采样、合并或省略。将机器结构表达为可读的
> ```

> ---

> ## Page 33

> <span style="color:#3B82F6"><strong>Para. 143:</strong></span>

> ```text
> 8    natural-language statements rather than copying an unexplained machine serialization.
>    3. Preserve every explicit visual observation and absolute or relative visual-spatial relation from the current original
>    reasoning, even when it is unrelated to the current task. This includes left/right, above/below, front/behind,
>    near/far, overlap, containment, adjacency, occlusion, orientation, size, appearance, and count descriptions.
> 9  4. Use calibrated perceptual wording such as "is estimated at", "appears", "approximately", or "the result indicates"
>    where appropriate, because tool outputs are perception estimates. Keep every returned numeric value exactly as
>    given; do not round, alter, normalize again, or invent precision.
> 10 5. Explain how the new evidence confirms, revises, or extends prior evidence. Clearly resolve a prior visual estimate
>    when stronger tool evidence supersedes it.
> 11 6. Do not repeat unchanged evidence already preserved in a previous unit, but never discard newly returned or newly
>    stated visual information merely because it is task-irrelevant.
> 12 7. Empty evidence is valid only when the interaction failed or truly returned no information; preserve the failure or
>    empty-result details themselves.
> 13
> 14 Return the structured result in this form:
> 15 <evidence_unit>
> 16 <new_evidence>
> 17 Complete readable natural-language statements verbalizing all returned information.
> 18 </new_evidence>
> 19 <logical_update>
> 20 Natural-language updates to the accumulated evidence and reasoning state.
> 21 </logical_update>
> 22 </evidence_unit>
> 23
> 24 Tool catalog (field semantics only; not sample evidence):
> 25 Perception-tool semantics
> 26
> 27 The catalog below explains how to interpret fields. It is not evidence for the current sample. A claim is supported
>    only when the corresponding value actually appears in the current tool result or a previous consolidated unit.
> 28
> 29 1. query_locate — open-vocabulary 2D localization
> 30 - Input: a short visible object/category description and optional 1-based image_indices.
> 31 - Output: count and zero or more matched instances. Each instance may contain bbox_2d=[x1,y1,x2,y2] and
>    point_2d=[x,y].
> 32 - Coordinates use the normalized 0–999 image plane with origin at the top-left: x increases to the right and y
>    increases downward. Smaller y is higher; larger x is farther right.
> 33 - point_2d is the center used for geometric comparisons or as input to query_depth. bbox_2d describes 2D extent
>    only.
> 34 - This tool does not establish metric depth, segmentation boundaries, object orientation, or camera motion.
> 35
> 36 2. query_segment — open-vocabulary instance segmentation
> 37 - Input: a short visible object/category description and optional 1-based image_indices.
> 38 - The exposed segmentation result contains bbox_2d, point_2d, and polygon_2d. point_2d is derived from
>    bbox_2d rather than an independently estimated from the mask area.
> 39 - bbox_2d is the bounding box associated with that segmentation instance/mask and normally encloses all returned
>    polygon components. It is emitted as a separate result field; it is not recomputed as the mathematically tight
>    bounding box of the simplified polygon vertices, so small boundary differences are expected.
> 40 - point_2d is the rounded, clamped center of bbox_2d: [⌊x1+x2)/2⌋,⌊(y1+y2)/2⌋]. It is not the area centroid of the
>    mask or polygon, and for a non-convex or disconnected mask it may lie outside the occupied mask region.
> 41 - bbox_2d, point_2d, and polygon_2d all use the normalized 0–999 image coordinates. polygon_2d is a list of
>    simplified boundary components tracing the occupied image region; multiple disconnected components may belong to
>    one mask.
> 42 - polygon_2d supports boundary, shape, overlap, containment, free-space, and placement reasoning. Neither the bbox
>    center nor a polygon is a grasp pose, 3D cuboid, metric depth, or object orientation.
> 43
> 44 3. query_depth — metric camera-axis depth at image points
> 45 - Input: one or more normalized 0–999 points and optional 1-based image_indices.
> 46 - Output: one result per point with point_2d and depth_m.
> 47 - depth_m is estimated camera-axis distance in meters. Smaller depth_m means closer to the camera; larger means
>    farther.
> 48 - Compare the returned numeric values explicitly when relative depth is relevant. Do not confuse depth_m with
>    image-plane y, Euclidean object-to-object distance, or object size.
> 49 - Depth is an estimate and only supports claims at the queried points/images.
> 50
> 51 4. query_pose — object orientation or cross-view camera motion
> 52 - Object mode input: a short object description, optionally with image_indices. Output may include image_index,
>    bbox_2d, visible_side, and facing_direction_camera.
> ```

> <span style="color:#F59E0B"><strong>Para. 143[CN]:</strong></span>

> ```text
> 8    自然语言陈述，而不是复制一段未解释的机器序列化。
>    3. 保留当前原始推理中的每项明确视觉观察，以及每项绝对或相对视觉空间关系，
>    即使它与当前任务无关。这包括左/右、上/下、前/后、
>    近/远、重叠、包含、相邻、遮挡、朝向、尺寸、外观和数量描述。
> 9  4. 在适当情况下使用经过校准的感知措辞，例如“估计为”“似乎”“大约”或“结果表明”，
>    因为工具输出是感知估计。严格按返回形式保留每个数值；
>    不要舍入、修改、再次归一化或虚构精度。
> 10 5. 说明新证据如何确认、修正或扩展先前证据。当更强的工具证据取代先前的视觉估计时，
>    明确解决该先前估计。
> 11 6. 不要重复先前单元中已经保留且未发生变化的证据，但绝不能因为新返回或新陈述的
>    视觉信息与任务无关而将其丢弃。
> 12 7. 仅当交互失败或确实未返回任何信息时，空证据才有效；保留失败或
>    空结果本身的细节。
> 13
> 14 按以下形式返回结构化结果：
> 15 <evidence_unit>
> 16 <new_evidence>
> 17 将所有返回信息言语化的完整、可读自然语言陈述。
> 18 </new_evidence>
> 19 <logical_update>
> 20 对累积证据和推理状态的自然语言更新。
> 21 </logical_update>
> 22 </evidence_unit>
> 23
> 24 工具目录（仅说明字段语义；并非样例证据）：
> 25 感知工具语义
> 26
> 27 以下目录说明如何解释字段。它并非当前样例的证据。仅当相应值确实出现在
>    当前工具结果或先前已整合单元中时，一项主张才有支持。
> 28
> 29 1. query_locate — 开放词汇二维定位
> 30 - 输入：简短的可见对象/类别描述，以及可选的、从 1 开始计数的 image_indices。
> 31 - 输出：count 和零个或多个匹配实例。每个实例可包含 bbox_2d=[x1,y1,x2,y2] 和
>    point_2d=[x,y]。
> 32 - 坐标使用原点位于左上角的归一化 0–999 图像平面：x 向右增大，y
>    向下增大。较小的 y 更高；较大的 x 更靠右。
> 33 - point_2d 是用于几何比较或作为 query_depth 输入的中心。bbox_2d 仅描述二维范围。
> 34 - 该工具不能确定公制深度、分割边界、对象朝向或相机运动。
> 35
> 36 2. query_segment — 开放词汇实例分割
> 37 - 输入：简短的可见对象/类别描述，以及可选的、从 1 开始计数的 image_indices。
> 38 - 公开的分割结果包含 bbox_2d、point_2d 和 polygon_2d。point_2d 源自
>    bbox_2d，而不是根据掩码面积独立估计。
> 39 - bbox_2d 是与该分割实例/掩码关联的边界框，通常包围所有返回的
>    多边形组成部分。它作为单独的结果字段输出；不会被重新计算为简化多边形顶点在数学意义上的紧致
>    边界框，因此预计会出现细微的边界差异。
> 40 - point_2d 是 bbox_2d 经舍入和限幅后的中心：[⌊x1+x2)/2⌋,⌊(y1+y2)/2⌋]。它不是
>    掩码或多边形的面积质心；对于非凸或不连通掩码，它可能位于已占据掩码区域之外。
> 41 - bbox_2d、point_2d 和 polygon_2d 均使用归一化的 0–999 图像坐标。polygon_2d 是
>    描摹已占据图像区域的简化边界组成部分列表；多个不连通组成部分可能属于
>    同一个掩码。
> 42 - polygon_2d 支持边界、形状、重叠、包含、自由空间和放置推理。边界框
>    中心和多边形都不是抓取姿态、三维长方体、公制深度或对象朝向。
> 43
> 44 3. query_depth — 图像点处沿相机轴的公制深度
> 45 - 输入：一个或多个归一化 0–999 点，以及可选的、从 1 开始计数的 image_indices。
> 46 - 输出：每个点对应一个结果，包含 point_2d 和 depth_m。
> 47 - depth_m 是以米为单位估计的沿相机轴距离。较小的 depth_m 表示更接近相机；较大的值表示
>    更远。
> 48 - 当相对深度相关时，明确比较返回的数值。不要将 depth_m 与
>    图像平面 y、对象间欧氏距离或对象尺寸混淆。
> 49 - 深度是一种估计，仅支持有关所查询点/图像的主张。
> 50
> 51 4. query_pose — 对象朝向或跨视图相机运动
> 52 - 对象模式输入：简短的对象描述，可选择附带 image_indices。输出可包括 image_index、
>    bbox_2d、visible_side 和 facing_direction_camera。
> ```

> ---

> ## Page 34

> <span style="color:#3B82F6"><strong>Para. 144:</strong></span>

> ```text
> 53 - visible_side names the object's side seen by the camera. facing_direction_camera describes where the object's
>    front points in camera coordinates; these are related but not interchangeable. For facing direction, front means deeper
>    into the image, back means toward the camera, and left/right are the viewer's image sides.
> 54 - Camera-motion mode input uses query='camera motion'. Each result is directional from from_image to to_image.
> 55 - position.direction describes translation of the camera position. view_rotation.direction describes where the camera
>    view turns. Never substitute one for the other.
> 56 - Signed camera axes are +X right, +Y up, and -Z forward. Use ordinary direction strings for ordinary-language
>    questions and signed axes only when the task explicitly asks about axes.
> 57
> 58 For every tool: respect image_index/image_indices, zero-result and failure states. Never treat a tool description, an
>    input query, or the model's pre-call guess as observed evidence.
> 59
> 60 <visual_inputs>
> 61 {VISUAL_INPUTS}
> 62 </visual_inputs>
> 63
> 64 <task_instruction>
> 65 {TASK_INSTRUCTION}
> 66 </task_instruction>
> 67
> 68 <previous_evidence_units>
> 69 {PREVIOUS_EVIDENCE_UNITS}
> 70 </previous_evidence_units>
> 71
> 72 <current_reasoning>
> 73 {CURRENT_REASONING}
> 74 </current_reasoning>
> 75
> 76 <current_tool_call>
> 77 {CURRENT_TOOL_CALL}
> 78 </current_tool_call>
> 79
> 80 <current_tool_result>
> 81 {CURRENT_TOOL_RESULT}
> 82 </current_tool_result>
> ```

> <span style="color:#F59E0B"><strong>Para. 144[CN]:</strong></span>

> ```text
> 53 - visible_side 指明相机看到的对象一侧。facing_direction_camera 描述对象的
>    正面在相机坐标中指向何处；二者相关但不可互换。对于朝向，front 表示更深入
>    图像，back 表示朝向相机，而 left/right 是观察者所见图像的左右两侧。
> 54 - 相机运动模式输入使用 query='camera motion'。每个结果表示从 from_image 到 to_image 的方向关系。
> 55 - position.direction 描述相机位置的平移。view_rotation.direction 描述相机
>    视图转向何处。绝不要用二者相互替代。
> 56 - 带符号的相机坐标轴为 +X 向右、+Y 向上、-Z 向前。普通语言问题使用普通方向字符串；
>    只有当任务明确询问坐标轴时才使用带符号坐标轴。
> 57
> 58 对于每个工具：遵守 image_index/image_indices、零结果状态和失败状态。绝不要将工具描述、
>    输入查询或模型调用前的猜测视为已观察证据。
> 59
> 60 <visual_inputs>
> 61 {VISUAL_INPUTS}
> 62 </visual_inputs>
> 63
> 64 <task_instruction>
> 65 {TASK_INSTRUCTION}
> 66 </task_instruction>
> 67
> 68 <previous_evidence_units>
> 69 {PREVIOUS_EVIDENCE_UNITS}
> 70 </previous_evidence_units>
> 71
> 72 <current_reasoning>
> 73 {CURRENT_REASONING}
> 74 </current_reasoning>
> 75
> 76 <current_tool_call>
> 77 {CURRENT_TOOL_CALL}
> 78 </current_tool_call>
> 79
> 80 <current_tool_result>
> 81 {CURRENT_TOOL_RESULT}
> 82 </current_tool_result>
> ```

> **Para. 92: G.3 Global Trajectory Verbalization Prompt**

> **Para. 92[CN]: G.3 全局轨迹言语化提示**

> <span style="color:#3B82F6"><strong>Para. 145:</strong></span> This prompt implements the second stage by converting the ordered evidence–reasoning units into a single tool-free perceptual reasoning target conditioned on the correct final answer. The answer is introduced only after turn-wise evidence consolidation, so it can guide the organization of already extracted evidence without influencing its collection. The rules merge repeated or superseded statements in dependency order, prohibit unsupported additions and construction-process leakage, and require exact preservation of the final answer. The complete template is shown in Box G.3.

> <span style="color:#F59E0B"><strong>Para. 145[CN]:</strong></span> 该提示实现第二阶段：将有序的证据—推理单元转换为一个以正确最终答案为条件的、单一的无工具感知推理目标。答案仅在逐轮证据整合之后引入，因此它可以指导已提取证据的组织，而不会影响证据收集。规则按依赖顺序合并重复或已被取代的陈述，禁止添加无依据内容和泄露构建过程，并要求精确保留最终答案。完整模板见框 G.3。

> **Para. 94: Box G.3: Global Trajectory Verbalization Prompt**

> **Para. 94[CN]: 框 G.3：全局轨迹言语化提示**

> <span style="color:#3B82F6"><strong>Para. 146:</strong></span>

> ```text
> 1  You are preparing the final trajectory-verbalization target for capability internalization. Convert ordered, grounded
>    visual evidence into a tool-free reasoning target for vision-language SFT. Given the visual task, ordered
>    evidence-reasoning units, and the correct final answer, construct a perceptual reasoning chain explaining why the
>    evidence supports that answer.
> 2
> 3  Put the structured result in the requested XML sections. The target must read as direct visual reasoning and must
>    not mention tools, calls, observations, evidence-unit boundaries, confidence scores, prompts, or this conversion
>    process.
> 4
> 5  Rules:
> 6  1. Use only entities, attributes, values, and relations present in the evidence units.
> 7  2. Merge evidence in dependency order and remove repeated or superseded statements, but do not discard an explicit
>    visual or spatial fact merely because it is unnecessary for choosing the answer.
> 8  3. Preserve the concrete visual-spatial descriptions carried by the evidence units and include every essential inference
>    needed to support all clauses of the answer.
> 9  4. Write as direct visual reasoning. Never mention tools, calls, results, evidence units, confidence scores, or this
>    instruction.
> 10 5. Do not invent entities, attributes, measurements, or relations.
> ```

> <span style="color:#F59E0B"><strong>Para. 146[CN]:</strong></span>

> ```text
> 1  你正在准备能力内化的最终轨迹言语化目标。将有序且有依据的
>    视觉证据转换为用于视觉语言 SFT 的无工具推理目标。给定视觉任务、有序的
>    证据—推理单元和正确的最终答案，构建一条感知推理链，解释为何
>    证据支持该答案。
> 2
> 3  将结构化结果置于所要求的 XML 区段中。目标必须读起来像直接视觉推理，并且不得
>    提及工具、调用、观察、证据单元边界、置信度分数、提示或这一转换
>    过程。
> 4
> 5  规则：
> 6  1. 仅使用证据单元中存在的实体、属性、数值和关系。
> 7  2. 按依赖顺序合并证据，并移除重复或已被取代的陈述，但不要仅仅因为某项明确的
>    视觉或空间事实对于选择答案并非必需而将其丢弃。
> 8  3. 保留证据单元承载的具体视觉空间描述，并包括支持答案所有分句所需的
>    每项关键推断。
> 9  4. 写成直接视觉推理。绝不要提及工具、调用、结果、证据单元、置信度分数或本
>    指令。
> 10 5. 不要虚构实体、属性、测量值或关系。
> ```

> ---

> ## Page 35

> <span style="color:#3B82F6"><strong>Para. 147:</strong></span>

> ```text
> 11 6. Put reasoning and answer in separate XML sections. Copy the provided final answer exactly.
> 12
> 13 Return the structured result in this form:
> 14 <internalization_target>
> 15 <reasoning_chain>
> 16 Complete, detailed, tool-free perceptual reasoning.
> 17 </reasoning_chain>
> 18 <final_answer>
> 19 Exact provided final answer.
> 20 </final_answer>
> 21 </internalization_target>
> 22
> 23 <visual_inputs>
> 24 {VISUAL_INPUTS}
> 25 </visual_inputs>
> 26
> 27 <task_instruction>
> 28 {TASK_INSTRUCTION}
> 29 </task_instruction>
> 30
> 31 <evidence_reasoning_units>
> 32 {EVIDENCE_REASONING_UNITS}
> 33 </evidence_reasoning_units>
> 34
> 35 <correct_final_answer>
> 36 {CORRECT_FINAL_ANSWER}
> 37 </correct_final_answer>
> ```

> <span style="color:#F59E0B"><strong>Para. 147[CN]:</strong></span>

> ```text
> 11 6. 将推理和答案置于不同的 XML 区段中。精确复制所提供的最终答案。
> 12
> 13 按以下形式返回结构化结果：
> 14 <internalization_target>
> 15 <reasoning_chain>
> 16 完整、详尽、无工具的感知推理。
> 17 </reasoning_chain>
> 18 <final_answer>
> 19 精确的所提供最终答案。
> 20 </final_answer>
> 21 </internalization_target>
> 22
> 23 <visual_inputs>
> 24 {VISUAL_INPUTS}
> 25 </visual_inputs>
> 26
> 27 <task_instruction>
> 28 {TASK_INSTRUCTION}
> 29 </task_instruction>
> 30
> 31 <evidence_reasoning_units>
> 32 {EVIDENCE_REASONING_UNITS}
> 33 </evidence_reasoning_units>
> 34
> 35 <correct_final_answer>
> 36 {CORRECT_FINAL_ANSWER}
> 37 </correct_final_answer>
> ```

> **Para. 97: H Case Studies**

> **Para. 97[CN]: H 案例研究**

> <span style="color:#3B82F6"><strong>Para. 148:</strong></span> We present 2 w/o Tools versus w/ Tools comparisons for Qwen3.5-397B-A17B. The first examines depth comparison and camera view rotation, whereas the second examines instance-level bounding boxes and camera translation. Together, they show how the agent decomposes a question into grounding, measurement, and cross-checking steps and uses tool evidence to revise unreliable visual judgments. Section H.3 separately compares two correct SpatialCLI-8B results after capability internalization: direct answering and tool-augmented answering.

> <span style="color:#F59E0B"><strong>Para. 148[CN]:</strong></span> 我们为 Qwen3.5-397B-A17B 展示了 2 组 w/o Tools 与 w/ Tools 对比。第一组考察深度比较和相机视图旋转，第二组考察实例级边界框和相机平移。二者共同展示了智能体如何将问题分解为定位、测量和交叉核验步骤，并利用工具证据修正不可靠的视觉判断。H.3 节另外比较了能力内化后 SpatialCLI-8B 的两个正确结果：直接作答和工具增强作答。

> **Para. 99: H.1 Case 1: Two-Image Camera Rotation and Depth**

> **Para. 99[CN]: H.1 案例 1：双图像相机旋转与深度**

> <span style="color:#3B82F6"><strong>Para. 149:</strong></span> The task input and ground truth are shown in Box H.1. In the comparison below, the direct answer infers that the beige receptacle is closer from apparent size and image position. It therefore selects C despite correctly identifying the rightward view rotation. The tool-augmented agent first grounds the two receptacles, queries two-image camera motion, and then passes the grounded centers to Depth. The measured depths, 0.928 m for the beige receptacle and 0.776 m for the blue one, overturn the initial visual guess. Combining the blue receptacle’s right-side location with the rightward rotation returned by Pose yields D. The trajectory follows a ground–measure–cross-check–verify logic.

> <span style="color:#F59E0B"><strong>Para. 149[CN]:</strong></span> 任务输入和真实答案见框 H.1。在下方比较中，直接作答根据表观尺寸和图像位置推断米色垃圾桶更近。因此，尽管它正确识别出向右的视图旋转，仍选择了 C。工具增强智能体首先定位两个垃圾桶，查询双图像相机运动，然后将定位所得中心传给 Depth。测得的深度为：米色垃圾桶 0.928 m，蓝色垃圾桶 0.776 m；这些结果推翻了最初的视觉猜测。将蓝色垃圾桶位于右侧这一位置与 Pose 返回的向右旋转相结合，得到 D。该轨迹遵循“定位—测量—交叉核验—验证”的逻辑。

> ---

> ## Page 36

> **Para. 101: Box H.1: Task (SpatialCLI-Bench ID 269)**

> **Para. 101[CN]: 框 H.1：任务（SpatialCLI-Bench ID 269）**

> <span style="color:#3B82F6"><strong>Para. 150:</strong></span>

> | Image 1 | Image 2 |
> |---|---|
> | A beige waste receptacle with a black bag and a blue waste receptacle with a clear bag are shown in an office setting. | A blue recycling receptacle with a clear bag is shown beside white cabinets. |

> <span style="color:#F59E0B"><strong>Para. 150[CN]:</strong></span>

> | 图像 1 | 图像 2 |
> |---|---|
> | 办公环境中展示了一个套有黑色袋子的米色垃圾桶和一个套有透明袋子的蓝色垃圾桶。 | 一个套有透明袋子的蓝色回收垃圾桶位于白色柜子旁。 |

> <span style="color:#3B82F6"><strong>Para. 151:</strong></span> In the first image, there are two large plastic waste receptacles in the foreground: a beige one with a black bag and a blue one with a clear bag. Compare their distances from the camera to find the closer one. In the first image, is this closer receptacle located on the left or the right? Finally, when moving from the first image to the second image, what is the dominant direction of the camera’s view rotation?

> <span style="color:#F59E0B"><strong>Para. 151[CN]:</strong></span> 在第一幅图像中，前景里有两个大型塑料垃圾桶：一个是套有黑色袋子的米色垃圾桶，另一个是套有透明袋子的蓝色垃圾桶。比较它们与相机之间的距离，找出更近的一个。在第一幅图像中，这个更近的垃圾桶位于左侧还是右侧？最后，从第一幅图像移动到第二幅图像时，相机视图旋转的主导方向是什么？

> <span style="color:#3B82F6"><strong>Para. 152:</strong></span>

> ```text
> Options:
> A: The blue receptacle is closer; it is located on the right; the camera rotated to the left.
> B: The beige receptacle is closer; it is located on the left; the camera rotated to the left.
> C: The beige receptacle is closer; it is located on the left; the camera rotated to the right.
> D: The blue receptacle is closer; it is located on the right; the camera rotated to the right.
> E: The blue receptacle is closer; it is located on the left; the camera rotated to the right.
> F: The beige receptacle is closer; it is located on the right; the camera rotated to the left.
> ```

> <span style="color:#F59E0B"><strong>Para. 152[CN]:</strong></span>

> ```text
> 选项：
> A：蓝色垃圾桶更近；它位于右侧；相机向左旋转。
> B：米色垃圾桶更近；它位于左侧；相机向左旋转。
> C：米色垃圾桶更近；它位于左侧；相机向右旋转。
> D：蓝色垃圾桶更近；它位于右侧；相机向右旋转。
> E：蓝色垃圾桶更近；它位于左侧；相机向右旋转。
> F：米色垃圾桶更近；它位于右侧；相机向左旋转。
> ```

> <span style="color:#3B82F6"><strong>Para. 153:</strong></span> Before choosing, briefly state the relevant facts and verify every clause of the selected option against all evidence available during solving. For any depth observations, smaller values mean closer; do not retain an earlier visual guess after receiving stronger evidence. Please show your choice in the answer field with only the choice letter, e.g., `{"answer": "C"}`.

> <span style="color:#F59E0B"><strong>Para. 153[CN]:</strong></span> 在选择之前，请简要陈述相关事实，并根据求解过程中可用的所有证据核验所选选项的每个分句。对于任何深度观察，较小的值表示更近；在获得更强证据后，不要保留先前的视觉猜测。请在答案字段中仅用选项字母表示你的选择，例如 `{"answer": "C"}`。

> **Para. 106: Ground Truth**

> **Para. 106[CN]: 真实答案**

> <span style="color:#3B82F6"><strong>Para. 154:</strong></span> Correct option: D.

> <span style="color:#F59E0B"><strong>Para. 154[CN]:</strong></span> 正确选项：D。

> **Para. 108: w/o Tools (Incorrect)**

> **Para. 108[CN]: 无工具（错误）**

> <span style="color:#3B82F6"><strong>Para. 155:</strong></span>

> ```text
> <think>
> The user wants me to analyze two images and answer a
> multi-part question.
> **Part 1: Compare distances of the two large plastic waste
> receptacles in the first image.**
> - **Receptacle 1:** Beige/tan bin with a black bag. It’s on
> the left side of the foreground.
> - **Receptacle 2:** Blue bin with a clear/white bag. It’s on
> the right side of the foreground.
> - **Comparison:** Looking at the perspective and size, the
> beige bin appears larger and lower down in the frame relative
> to the blue bin next to it (though they are similar in height,
> the base of the beige bin is lower). Wait, let’s look closer.
> The beige bin is clearly in front of the blue bin behind it (the
> tall blue one with the lid). But there is another blue bin to
> the right. Let’s re-evaluate.
> - Actually, looking at the first image:
> - There is a beige bin on the left.
> - Behind it is a tall blue recycling bin with a lid.
> - To the right of the beige bin is a small black cart.
> - To the right of the black cart is another blue bin with a
> clear liner.
> - The prompt asks about "two large plastic waste receptacles
> in the foreground: a beige one with a black bag and a blue
> one with a clear bag."
> - Beige bin: Left foreground.
> - Blue bin (with clear bag): Right foreground.
> - Which is closer? The beige bin’s base is lower in the frame
> than the blue bin’s base. The beige bin obscures part of the
> view towards the back left. The blue bin on the right is also
> quite close. Let’s look at the perspective. The beige bin
> seems slightly closer to the camera lens because it feels more
> “in your face” and its bottom edge is lower. However, let’s
> look at the second image.
> - The second image shows *only* the blue bin with the
> recycling symbol. This is the bin that was on the right in the
> first image (blue bin, clear bag). Wait, let me check the
> details.
> - Image 1 Blue Bin (right): Blue, rectangular, clear/white bag.
> ```

> <span style="color:#F59E0B"><strong>Para. 155[CN]:</strong></span>

> ```text
> <think>
> 用户希望我分析两幅图像并回答一个
> 多部分问题。
> **第 1 部分：比较第一幅图像中两个大型塑料垃圾桶的距离。**
> - **垃圾桶 1：** 米色/棕褐色垃圾桶，套有黑色袋子。它位于
> 前景左侧。
> - **垃圾桶 2：** 蓝色垃圾桶，套有透明/白色袋子。它位于
> 前景右侧。
> - **比较：** 从透视和尺寸来看，米色垃圾桶相对于
> 旁边的蓝色垃圾桶显得更大，并且在画面中位置更低（尽管二者高度相近，
> 米色垃圾桶的底部更低）。等等，让我们看得更仔细些。
> 米色垃圾桶显然位于它后面的蓝色垃圾桶（
> 带盖子的高蓝色垃圾桶）前方。但右侧还有另一个蓝色垃圾桶。
> 让我们重新评估。
> - 实际上，观察第一幅图像：
> - 左侧有一个米色垃圾桶。
> - 它后面是一个带盖子的高蓝色回收垃圾桶。
> - 米色垃圾桶右侧是一辆小型黑色推车。
> - 黑色推车右侧是另一个套有
> 透明内衬的蓝色垃圾桶。
> - 提示询问的是“前景中的两个大型塑料垃圾桶：
> 一个套有黑色袋子的米色垃圾桶和一个套有透明袋子的蓝色
> 垃圾桶。”
> - 米色垃圾桶：左前景。
> - 蓝色垃圾桶（套有透明袋子）：右前景。
> - 哪一个更近？米色垃圾桶的底部在画面中的位置低于
> 蓝色垃圾桶的底部。米色垃圾桶遮挡了部分
> 通往左后方的视野。右侧的蓝色垃圾桶也
> 相当近。让我们看一下透视关系。米色垃圾桶
> 似乎稍微更接近相机镜头，因为它显得更
> “扑面而来”，并且底边更低。不过，让我们
> 看一下第二幅图像。
> - 第二幅图像中*只有*带有
> 回收标志的蓝色垃圾桶。这就是第一幅图像中位于右侧的
> 垃圾桶（蓝色垃圾桶，透明袋子）。等等，让我检查一下
> 细节。
> - 图像 1 中的蓝色垃圾桶（右侧）：蓝色、长方形、透明/白色袋子。
> ```

> **Para. 110: w/ Tools (Correct)**

> **Para. 110[CN]: 有工具（正确）**

> <span style="color:#3B82F6"><strong>Para. 156:</strong></span>

> ```text
> <think>
> The user wants me to analyze two images of an office setting,
> focusing on waste receptacles and camera movement.
> **Step 1: Identify the objects in the first image.**
> - There is a beige trash can with a black bag on the left side
> of the foreground.
> - There is a blue recycling bin with a clear bag on the right
> side of the foreground.
> - Behind the beige can, there is another blue bin (taller).
> **Step 2: Compare distances of the beige and blue receptacles
> in the first image.**
> - I need to determine which one is closer to the camera.
> - Visually, the beige can appears larger and lower in the
> frame, suggesting it might be closer. However, the blue bin on
> the right is also quite large.
> - Let’s use `query_locate` to get their bounding boxes and
> centers, then `query_depth` to check their actual distances.
> **Step 3: Determine the location (left/right) of the closer
> receptacle.**
> - Once I know which is closer, I need to state if it’s on the left
> or right.
> - Based on visual inspection:
>   - Beige can: Left side.
>   - Blue bin: Right side.
> **Step 4: Determine the camera’s view rotation from image 1
> to image 2.**
> - Image 1 shows the beige and blue bin side-by-side with a
> cabinet behind them.
> - Image 2 shows primarily the blue bin (with the recycling
> symbol visible now) and white cabinets to its right. The beige
> can is no longer visible or is out of frame to the left.
> - This suggests the camera turned to the right to focus on the
> blue bin and the cabinets next to it. Or did it turn left?
> - Let’s look at the background. In image 1, to the right of the
> blue bin, there are desks and shelves. In image 2, to the right
> of the blue bin, there are white cabinets. Wait, let’s look
> closer.
> - In image 1, the blue bin is on the right. To its right, further
> back, is a desk area.
> ```

> <span style="color:#F59E0B"><strong>Para. 156[CN]:</strong></span>

> ```text
> <think>
> 用户希望我分析两幅办公室环境图像，
> 重点关注垃圾桶和相机移动。
> **第 1 步：识别第一幅图像中的对象。**
> - 前景左侧有一个套有黑色袋子的米色垃圾桶。
> - 前景右侧有一个套有透明袋子的蓝色回收垃圾桶。
> - 米色垃圾桶后面还有另一个蓝色垃圾桶（更高）。
> **第 2 步：比较第一幅图像中米色和蓝色垃圾桶的距离。**
> - 我需要确定哪一个更接近相机。
> - 从视觉上看，米色垃圾桶显得更大且在画面中位置更低，
> 这表明它可能更近。不过，右侧的蓝色垃圾桶
> 也相当大。
> - 让我们使用 `query_locate` 获取它们的边界框和
> 中心，然后使用 `query_depth` 检查它们的实际距离。
> **第 3 步：确定较近垃圾桶的位置（左/右）。**
> - 知道哪一个更近后，我需要说明它位于左侧
> 还是右侧。
> - 根据视觉检查：
>   - 米色垃圾桶：左侧。
>   - 蓝色垃圾桶：右侧。
> **第 4 步：确定从图像 1 到图像 2 的相机视图旋转。**
> - 图像 1 显示米色和蓝色垃圾桶并排放置，
> 后面有柜子。
> - 图像 2 主要显示蓝色垃圾桶（现在可以看到
> 回收标志）和它右侧的白色柜子。米色
> 垃圾桶已不可见，或者位于画面左侧之外。
> - 这表明相机向右转，以聚焦
> 蓝色垃圾桶及其旁边的柜子。还是向左转了？
> - 让我们看一下背景。在图像 1 中，蓝色
> 垃圾桶右侧有桌子和架子。在图像 2 中，蓝色
> 垃圾桶右侧有白色柜子。等等，让我们
> 看得更仔细些。
> - 在图像 1 中，蓝色垃圾桶位于右侧。它的右侧、更靠
> 后的位置是一个办公桌区域。
> ```


> # Page 37

> - Image 2 Blue Bin: Blue, rectangular, white logo (recycling symbol), clear/white bag. This matches the bin on the right in Image 1.
> - In Image 2, this blue bin is now on the left side of the frame and very prominent. The camera has moved.
> - Let’s re-evaluate. The beige bin is on the left. The blue bin is on the right. The beige bin looks slightly closer because it is larger in apparent scale relative to what a standard bin looks like, and its bottom is lower. BUT, let’s look at the options.
> - Option A: Blue closer, right, rotate left.
> - Option B: Blue closer, left, rotate left.
> - Option C: Beige closer, left, rotate right.
> - Option D: Blue closer, right, rotate right.
> - Option E: Blue closer, left... (Blue is on the right in image 1).
> - Option F: Beige closer, right... (Beige is on the left in image 1).
> - Let’s look really closely at Image 1.
> - The beige bin is clearly the closest object. It is large and in the immediate foreground.
> - The blue bin on the right is also in the foreground but set slightly farther back or just to the side. Wait, actually, looking at the floor tiles, the beige bin is positioned further “down” (closer to bottom edge) than the blue bin on the right. Therefore, the beige bin is closer.
> - So, “The beige receptacle is closer.” And “it is located on the left.” This eliminates A, D, E, F.
> - We are left with B and C.
> - B: Camera rotated to the left.
> - C: Camera rotated to the right.
> - **Part 2: Determine camera rotation.**
> - **Image 1 View:** Shows the blue bin (left), black cart (center), blue bin (right). Background shows desks and cabinets.
> - **Image 2 View:** Shows the blue bin (from the right side of Image 1) now on the “left” side of the frame. To its right are white cabinets.
> - In Image 1, the blue bin is on the right. In Image 2, we are looking directly at the front/side of that same blue bin, and the objects that were to its right (the white cabinets/shelves) are now visible.
> - Wait, let’s look at the background of Image 1. To the right of the blue bin is a desk area.
> - In Image 2, to the right of the blue bin are white cabinets, where these white cabinets in Image 1? They are likely to the right of the blue bin, but in Image 1, to the right of the blue bin, we see a desk.
> - Let’s re-orient.
> - Image 1: Left = Beige bin. Center = Black cart. Right = Blue bin. Far Right = Desk and area.
> - Image 2: Left = Beige bin. Right = Blue bin. Right = White cabinets.
> - If I am looking at Image 1, and I want to see what is to the *right* of the scene (where the blue bin is), I would turn the camera to the **right**.
> - Let’s trace the objects.
> - Object X: Blue bin with clear bag. In Img 1, it’s on the right. In Img 2, it’s on the left/center. This implies the camera moved to the right, causing the object to shift left in the frame. Or the camera rotated right.
> - If I rotate right, objects on the right move towards the center/left. Yes.
> - Also, new objects appear on the right side. In Image 2, we see white cabinets on the right. In Image 1, looking at the blue bin, we see a desk area. Wait, let’s look at the white cabinets in Image 1. Behind the black cart and blue bin is a white wall/pillar. To the right of this is a desk.
> - Let’s look at Image 2 again. The white cabinets are tall, with handles. In Image 1, can we see these? Ah, look at the top right of Image 1. There is a desk. Underneath/behind it might be cabinets.
> - Actually, look at the transition.
> - Image 1: Beige bin (Left), Black Cart (Middle), Blue Bin (Right).
> - Image 2: Blue Bin (Left), White Cabinets (Right).
> - The camera has shifted focus from the group (Beige, Cart, Blue) to just the Blue bin and what is next to it.
> - The blue bin was on the right. Now it is on the left. This means the camera panned/rotated to the **right**. By turning right, the rightmost object (Blue bin) moves towards the center/left of the view, and we see what is to the right (the white cabinets).
> - So, rotation is to the right.
> - **Conclusion:**
>   - Closer receptacle: Beige (based on position lower in frame and general perspective).
>   - Location: Left.
>   - Rotation: Right.
>   - This matches Option C.
> - Let’s double check “Closer.”
> - In Image 1, the beige bin is very large. The blue bin on the right is also large.
> - Let’s look at the floor. The bottom of the beige bin is cut off by the bottom edge of the photo? No. It’s fully visible. The bottom of the blue bin is lower in the y-axis than the blue bin’s bottom. In perspective projection, lower on the ground plane usually means closer.
> - Therefore, Beige is closer.
> - Beige is on the left.
> - Camera moves from seen [Beige, Cart, Blue] to seeing [Blue, Cabinets].
> - This is a pan/rotation to the right.
> - So, Option C: “The beige receptacle is closer; it is located on the left; the camera rotated to the right.”
> - Let’s verify Option B just in case. “Camera rotated to the left.” If I rotated left, I would see more of the beige bin and whatever is to its left (the office chair area). I would lose the blue bin on the right. But Image 2 focuses on the blue bin. So it must be a rotation to the right. Therefore, C is the correct answer.

> Para. 1[CN]: 
> - 图像 2 中的蓝色垃圾桶：蓝色、矩形、带有白色标志（回收标志），装有透明/白色垃圾袋。这与图像 1 右侧的垃圾桶相符。
> - 在图像 2 中，这个蓝色垃圾桶现在位于画面左侧，并且非常突出。相机发生了移动。
> - 重新评估一下。米色垃圾桶在左侧。蓝色垃圾桶在右侧。米色垃圾桶看起来更近，因为相对于标准垃圾桶的外观，它的表观尺寸更大，而且底部位置更低。但我们还是看看选项。
> - 选项 A：蓝色垃圾桶更近、在右侧、向左旋转。
> - 选项 B：蓝色垃圾桶更近、在左侧、向左旋转。
> - 选项 C：米色垃圾桶更近、在左侧、向右旋转。
> - 选项 D：蓝色垃圾桶更近、在右侧、向右旋转。
> - 选项 E：蓝色垃圾桶更近、在左侧……（在图像 1 中蓝色垃圾桶位于右侧）。
> - 选项 F：米色垃圾桶更近、在右侧……（在图像 1 中米色垃圾桶位于左侧）。
> - 让我们非常仔细地看图像 1。
> - 米色垃圾桶显然是最近的物体。它很大，位于近处前景中。
> - 右侧的蓝色垃圾桶也在前景中，但位置稍微靠后，或者只是位于侧面。等等，实际上，观察地板砖，米色垃圾桶的位置比右侧蓝色垃圾桶更“向下”（更接近底部边缘）。因此，米色垃圾桶更近。
> - 所以，“米色垃圾桶更近”。并且“它位于左侧”。这排除了 A、D、E、F。
> - 剩下 B 和 C。
> - B：相机向左旋转。
> - C：相机向右旋转。
> - **第 2 部分：确定相机旋转方向。**
> - **图像 1 视图：**显示蓝色垃圾桶（左）、黑色推车（中）、蓝色垃圾桶（右）。背景中有桌子和柜子。
> - **图像 2 视图：**显示图像 1 右侧的蓝色垃圾桶，现在位于画面“左侧”。它的右侧是白色柜子。
> - 在图像 1 中，蓝色垃圾桶位于右侧。在图像 2 中，我们直接看到这个蓝色垃圾桶的正面/侧面，并且原本位于其右侧的物体（白色柜子/架子）现在可见。
> - 等等，让我们看看图像 1 的背景。蓝色垃圾桶的右侧是一个桌子区域。
> - 在图像 2 中，蓝色垃圾桶的右侧是白色柜子，这些白色柜子在图像 1 中在哪里？它们可能就在蓝色垃圾桶的右侧，但在图像 1 中，蓝色垃圾桶右侧看到的是一张桌子。
> - 重新确定方向。
> - 图像 1：左 = 米色垃圾桶。中 = 黑色推车。右 = 蓝色垃圾桶。最右 = 桌子和周围区域。
> - 图像 2：左 = 米色垃圾桶。右 = 蓝色垃圾桶。右侧 = 白色柜子。
> - 如果我正在看图像 1，并且想看到场景的*右侧*（蓝色垃圾桶所在的位置），我就会把相机向**右**转。
> - 追踪这些物体。
> - 物体 X：带透明袋的蓝色垃圾桶。在图像 1 中，它位于右侧。在图像 2 中，它位于左侧/中间。这意味着相机向右移动，导致物体在画面中向左移动。或者相机向右旋转。
> - 如果向右旋转，右侧的物体会向中间/左侧移动。是的。
> - 同时，右侧出现了新的物体。在图像 2 中，我们在右侧看到白色柜子。在图像 1 中，看到蓝色垃圾桶时，我们看到的是一个桌子区域。等等，让我们看看图像 1 中的白色柜子。在黑色推车和蓝色垃圾桶后面是一面白墙/柱子。其右侧可能就是桌子。
> - 再看图像 2。白色柜子很高，并且有把手。在图像 1 中，我们能看到这些吗？啊，看图像 1 的右上方。那里有一张桌子。其下方/后方可能有柜子。
> - 看看这个转换。
> - 图像 1：米色垃圾桶（左）、黑色推车（中）、蓝色垃圾桶（右）。
> - 图像 2：蓝色垃圾桶（左）、白色柜子（右）。
> - 相机的关注点从这一组物体（米色垃圾桶、推车、蓝色垃圾桶）转移到了蓝色垃圾桶以及它旁边的物体。
> - 蓝色垃圾桶原来在右侧。现在它在左侧。这意味着相机向**右**平移/旋转。向右转时，最右侧的物体（蓝色垃圾桶）会向视野的中间/左侧移动，同时我们会看到其右侧的物体（白色柜子）。
> - 因此，旋转方向是向右。
> - **结论：**
>   - 更近的垃圾桶：米色（根据它在画面中更低的位置以及总体透视关系）。
>   - 位置：左侧。
>   - 旋转：向右。
>   - 这与选项 C 相符。
> - 再次确认“更近”。
> - 图像 1 中的米色垃圾桶非常大。右侧的蓝色垃圾桶也很大。
> - 看看地面。米色垃圾桶的底部被照片底部边缘截断了吗？没有。它是完整可见的。蓝色垃圾桶的底部在 y 轴上的位置比蓝色垃圾桶底部更低。在透视投影中，地面上更低的位置通常意味着更近。
> - 因此，米色垃圾桶更近。
> - 米色垃圾桶在左侧。
> - 相机从看到[米色垃圾桶、推车、蓝色垃圾桶]移动到看到[蓝色垃圾桶、柜子]。
> - 这是向右的平移/旋转。
> - 所以选项 C：“米色垃圾桶更近；它位于左侧；相机向右旋转。”
> - 再确认一下选项 B，以防万一。“相机向左旋转。”如果我向左旋转，我会看到更多米色垃圾桶以及其左侧的物体（办公椅区域）。我会失去右侧的蓝色垃圾桶。但图像 2 聚焦于蓝色垃圾桶。因此一定是向右旋转。故 C 是正确答案。

> ```text
> <tool_response>
> {"count":1,"result":[{"bbox_2d":[203,176,418,872],"point_2d":[310,524]}]}
> [tool_response>
> Tool-call budget: at most 4 more tool calls may be made.
> </tool_response>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[606,289,940,997],"point_2d":[773,643]}]}
> [tool_response>
> Tool-call budget: at most 3 more tool calls may be made.
> </tool_response>

> <tool_response>
> {"result":[{"from_image":1,"to_image":2,"position":{"direction":"forward-right","axes":["+X","+Y","-Z"],"view_rotation":{"direction":"right","axes":["+X","+Y","-Z"],"dominant_axis":"Y"}}}]}
> [tool-call budget: at most 2 more tool calls may be made.]
> </tool_response>

> <think>
> Now I have the locations of both trash cans in image 1:
> - Beige trash can: point_2d [310, 524]
> - Blue trash can: point_2d [773, 643]
> I need to query the depth at these two points to determine which is closer to the camera. Let me also note that the beige one is on the left (x=310) and the blue one is on the right (x=773) in the image.
> The camera motion result shows view_rotation direction is "right" with dominant_axis "+Y".
> Let me query the depths to confirm which receptacle is closer.
> </think>

> <tool_call>
> {
>   "name": "query_depth",
>   "arguments": {
>     "points": [
>       [
>         310,
>         524
>       ],
>       [
>         773,
>         643
>       ]
>     ],
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"result":[{"point_2d":[310,524],"depth_m":0.928},{"point_2d":[773,643],"depth_m":0.776}]}
> [Tool-call budget: at most 1 more tool may be made.]
> </tool_response>

> Based on the tool results:
> 1. **Distance:** The depth query shows the beige receptacle point [310, 524] is at 0.928m* and the blue receptacle [point [773, 643] is at 0.776m. Since 0.776 < 0.928, the blue receptacle is closer.
> 2. **Location:** In the first image, the beige can is x=310 (left side) and the blue can is at x=773 (right side). Therefore, the closer receptacle (blue) is located on the *right*.
> 3. **Camera Motion:** The pose query for camera motion from image 1 to 2 indicates a "view_rotation" direction of **"right"**.
> Matching these facts to the options:
> Closer: Blue
> Location: Right
> Rotation: Right
> This corresponds to Option D.
> {"answer": "D"}
> ```

> Para. 2[CN]: 

> ```text
> <tool_response>
> {"count":1,"result":[{"bbox_2d":[203,176,418,872],"point_2d":[310,524]}]}
> [tool_response]
> 工具调用预算：最多还可进行 4 次工具调用。
> </tool_response>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[606,289,940,997],"point_2d":[773,643]}]}
> [tool_response]
> 工具调用预算：最多还可进行 3 次工具调用。
> </tool_response>

> <tool_response>
> {"result":[{"from_image":1,"to_image":2,"position":{"direction":"forward-right","axes":["+X","+Y","-Z"],"view_rotation":{"direction":"right","axes":["+X","+Y","-Z"],"dominant_axis":"Y"}}}]}
> 工具调用预算：最多还可进行 2 次工具调用。
> </tool_response>

> <think>
> 现在我已经获得了图像 1 中两个垃圾桶的位置：
> - 米色垃圾桶：point_2d [310, 524]
> - 蓝色垃圾桶：point_2d [773, 643]
> 我需要查询这两个点的深度，以确定哪一个离相机更近。同时注意，米色垃圾桶在左侧（x=310），蓝色垃圾桶在图像右侧（x=773）。
> 相机运动结果显示，视角旋转方向是“right”，主轴为“+Y”。
> 让我查询深度，以确认哪个垃圾桶更近。
> </think>

> <tool_call>
> {
>   "name": "query_depth",
>   "arguments": {
>     "points": [
>       [
>         310,
>         524
>       ],
>       [
>         773,
>         643
>       ]
>     ],
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"result":[{"point_2d":[310,524],"depth_m":0.928},{"point_2d":[773,643],"depth_m":0.776}]}
> 工具调用预算：最多还可进行 1 次工具调用。
> </tool_response>

> 根据工具结果：
> 1. **距离：**深度查询显示，米色垃圾桶点 [310, 524] 的深度为 0.928m*，蓝色垃圾桶[点 [773, 643] 的深度为 0.776m。由于 0.776 < 0.928，蓝色垃圾桶更近。
> 2. **位置：**在第一张图中，米色垃圾桶的 x=310（左侧），蓝色垃圾桶的 x=773（右侧）。因此，更近的垃圾桶（蓝色）位于*右侧*。
> 3. **相机运动：**从图像 1 到图像 2 的相机运动姿态查询显示视角旋转方向为**“right”**。
> 将这些事实与选项匹配：
> 更近者：蓝色
> 位置：右侧
> 旋转：向右
> 这对应于选项 D。
> {"answer": "D"}
> ```

> # Page 38

> ```text
> <tool_response>
> {"count":1,"result":[{"bbox_2d":[606,289,940,997],"point_2d":[773,643]}]}
> [tool-call budget: at most 3 more tool calls may be made.]
> </tool_response>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[145,507,784,855],"point_2d":[464,681]}]}
> [tool_response>
> {"count":0,"result":[]}
> [tool-call budget: at most 1 more tool call may be made.]
> </tool_response>

> <think>
> The query_locate returned only one bounding box for both sandals combined: [143,499,857,857]. This suggests the tool grouped them. I need to distinguish between the two individual sandals to find which has the larger maximum x-coordinate.
> Let me segment each sandal individually to get their separate bounding boxes.
> </think>

> <tool_call>
> {
>   "name": "query_segment",
>   "arguments": {
>     "query": "left white sandal with pearl strap",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_call>
> {
>   "name": "query_segment",
>   "arguments": {
>     "query": "right white sandal with pearl strap",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"count":2,"result":[{"bbox_2d":[145,507,784,855],"point_2d":[464,681]},{"bbox_2d":[155,252,583,662],"point_2d":[369,457]}]}
> </tool_response>

> <think>
> The query_locate returned only one bounding box likely encompasses both sandals together. The query_segment returned two instances, but looking at the boxes:
> First instance bbox_2d=[145,507,784,855], so max_x=784, so max_y=855
> Second instance bbox_2d=[156,493,759,746], so max_x=759, so max_y=746
> Wait, let me re-read the segment results carefully:
> Result 1: bbox_2d=[145,507,784,855], point_2d=[464,681]
> Result 2: bbox_2d=[156,493,759,746], point_2d=[458,620]
> For Result 1: min_x=145, min_y=507, max_x=784, max_y=855
> For Result 2: min_x=156, min_y=493, max_x=759, max_y=746
> The sandal with the larger maximum x-coordinate is Result 1 (x_max=784). Its maximum y-coordinate is 855. But wait, the options mention maximum y-coordinate of the sandal (Result 1 855). But the question asks for the sandal whose bounding box extends further to the right (larger maximum x-coordinate). So the answer should be C.
> </think>

> {"answer": "C"}
> ```

> Para. 3[CN]:

> ```text
> <tool_response>
> {"count":1,"result":[{"bbox_2d":[606,289,940,997],"point_2d":[773,643]}]}
> [tool-call budget: at most 3 more tool calls may be made.]
> </tool_response>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[145,507,784,855],"point_2d":[464,681]}]}
> [tool_response]
> {"count":0,"result":[]}
> [tool-call budget: at most 1 more tool call may be made.]
> </tool_response>

> <think>
> query_locate 只返回了两个凉鞋合并后的一个边界框：[143,499,857,857]。这说明工具将它们分组了。我需要区分两个单独的凉鞋，以找出哪个凉鞋具有更大的最大 x 坐标。
> 让我分别分割每个凉鞋，获得各自的边界框。
> </think>

> <tool_call>
> {
>   "name": "query_segment",
>   "arguments": {
>     "query": "left white sandal with pearl strap",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_call>
> {
>   "name": "query_segment",
>   "arguments": {
>     "query": "right white sandal with pearl strap",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"count":2,"result":[{"bbox_2d":[145,507,784,855],"point_2d":[464,681]},{"bbox_2d":[155,252,583,662],"point_2d":[369,457]}]}
> </tool_response>

> <think>
> query_locate 返回的只是一个边界框，可能涵盖了两个凉鞋。query_segment 返回了两个实例，但观察这些框：
> 第一个实例 bbox_2d=[145,507,784,855]，所以 max_x=784，因此 max_y=855。
> 第二个实例 bbox_2d=[156,493,759,746]，所以 max_x=759，因此 max_y=746。
> 等等，让我仔细重新读取分割结果：
> 结果 1：bbox_2d=[145,507,784,855]，point_2d=[464,681]
> 结果 2：bbox_2d=[156,493,759,746]，point_2d=[458,620]
> 对于结果 1：min_x=145，min_y=507，max_x=784，max_y=855
> 对于结果 2：min_x=156，min_y=493，max_x=759，max_y=746
> 最大 x 坐标更大的凉鞋是结果 1（x_max=784）。其最大 y 坐标是 855。但是，等等，选项提到的是凉鞋的最大 y 坐标（结果 1 为 855）。而问题询问的是边界框向右延伸更远（最大 x 坐标更大）的凉鞋。因此答案应为 C。
> </think>

> {"answer": "C"}
> ```

> ## H.2  Case 2: Two-Image Camera Translation and Instance Segmentation

> ## H.2  案例 2：双图像相机平移与实例分割

> Para. 4: The task input and ground truth are shown in Box H.2. In the comparison below, the direct answer approximately identifies the target sandal and its maximum vertical coordinate, but interprets the scale change in the second image as backward camera motion. It consequently predicts backward-left and selects C. The tool-augmented agent first obtains a coarse location and the camera motion from Locate and Pose. When Locate merges the pair into one box, the agent switches to Segment to recover two instances and compares their maximum horizontal and vertical coordinates. The instance-level result supports 856, while Pose returns forward-left, yielding E. This trajectory follows a coarse-grounding–granularity-check–instance-refinement–joint-decision–recheck pattern.

> Para. 4[CN]: 任务输入和真实答案显示在框 H.2 中。在下面的比较中，直接作答的模型大致识别出了目标凉鞋及其最大垂直坐标，但将第二张图中的尺度变化解释为相机向后移动。因此它预测相机向后左方移动，并选择 C。使用工具的智能体首先通过 Locate 和 Pose 获得粗略位置和相机运动。当 Locate 将这一对凉鞋合并为一个边界框时，智能体切换到 Segment，以恢复两个实例，并比较它们的最大水平和垂直坐标。实例级结果支持 856，而 Pose 返回 forward-left，因此选择 E。该轨迹遵循“粗定位—检查粒度—实例细化—联合决策—重新检查”的模式。

> > **Box H.2: Task (SpatialCLI-Bench ID 323)**  
> > **框 H.2：任务（SpatialCLI-Bench ID 323）**

> **Image 1**  
> **图像 1**

> **Image 2**  
> **图像 2**

> Para. 5: Consider the two white sandals with pearl straps in the first image. First, determine which of these two sandals has a bounding box that extends further to the right (has the larger maximum x-coordinate). What is the maximum y-coordinate of that same sandal’s bounding box, and what is the direction of the camera translation from the first image to the second?

> Para. 5[CN]: 请考虑第一张图中的两只带珍珠带的白色凉鞋。首先，确定这两只凉鞋中哪一只的边界框向右延伸得更远（具有更大的最大 x 坐标）。同一只凉鞋边界框的最大 y 坐标是多少？相机从第一张图到第二张图的平移方向是什么？

> - A: Maximum y-coordinate: 747; Camera translation: backward-left
> - B: Maximum y-coordinate: 747; Camera translation: forward-left
> - C: Maximum y-coordinate: 856; Camera translation: backward-left
> - D: Maximum y-coordinate: 856; Camera translation: forward-right
> - E: Maximum y-coordinate: 856; Camera translation: forward-left
> - F: Maximum y-coordinate: 856; Camera translation: forward-right

> Para. 6[CN]:

> - A：最大 y 坐标：747；相机平移：向后左方
> - B：最大 y 坐标：747；相机平移：向前左方
> - C：最大 y 坐标：856；相机平移：向后左方
> - D：最大 y 坐标：856；相机平移：向前右方
> - E：最大 y 坐标：856；相机平移：向前左方
> - F：最大 y 坐标：856；相机平移：向前右方

> Before choosing, briefly state the relevant facts and verify every clause of the selected option against all evidence available during solving. For any depth observations, smaller values mean closer; do not retain an earlier visual guess after receiving stronger evidence. Please show your choice in the answer field with only the choice letter, e.g., {"answer": "C"}.

> Para. 7[CN]: 在作出选择之前，简要陈述相关事实，并根据解题过程中获得的全部证据，核实所选选项的每一个条款。对于任何深度观察，数值越小表示越近；在获得更强证据后，不要保留早先的视觉猜测。请在答案字段中只填写选项字母，例如 `{"answer": "C"}`。

> **Ground Truth**  
> **真实答案**

> Correct option: E.

> Para. 8[CN]: 正确选项：E。

> ## w/o Tools (Incorrect)

> ## 不使用工具（错误）

> ```text
> <think>
> The user wants me to identify a specific sandal based on its bounding box and then determine camera movement.
> **1. Identify the target sandal.**
> - The prompt asks to consider “the two white sandals with pearl straps in the first image”.
> - I need to find the bounding boxes for these two sandals.
> - Sandal 1 (left/back): This is the one further back, slightly to the left. It’s strap has pearls.
> - Sandal 2 (right/front): This is the one closer to the front right. Its strap also has pearls. Wait, let’s look closer.
> - In Image 1:
>   - There is a sandal in the foreground [143, 508, 765, 856].
>   - There is a white sandal facing somewhat left. It has a pearl strap.
> - There is another sandal behind it/to the left [159, 492, 715, 747]. This one is to the left and slightly behind.
> - The question asks: “determine which of these two sandals has a bounding box that extends further to the right (has the larger maximum x-coordinate).”
> - Sandal 1 (front/right): Box is roughly [143, 508, 765, 856]. Max x is 765.
> - Sandal 2 (back/left): Box is roughly [159, 492, 715, 747]. Max x is 715.
> - Comparing max x: Sandal 1 (765) > Sandal 2 (715). So the target sandal is the front one.
> - The question asks for the “maximum y-coordinate of that sandal’s bounding box”.
> - For the front sandal [143, 508, 765, 856], the max y is 856.
> - Wait, let me check the options. Options have max y 747 or 856. Obviously it’s [y_min, y_max]. So max y is 856.
> - Since I identified the sandal extending further right as the front one, its maximum y is 856.
> - **3. Determine camera translation.**
> - Compare Image 1 and Image 2.
> - Image 1: Close-up of the shoes. See the headboard behind the shoes, which are large in the frame.
> - Image 2: The shoes are further away. We see the whole room, clothes rack, towels.
> - The camera has moved “backward” (away from the shoes) to capture more of the scene.
> - Also, the angle changes. In Image 1, we are looking slightly down and from the right. In Image 2, we are further back and more from the front.
> - Let’s look at the position of the shoes relative to the frame.
> - Image 1: Shoes are central/bottom.
> - Image 2: Shoes are central/bottom.
> - Wait, let’s look at the options.
> - Options involve “backward-left”, “forward-left”, “forward-right”.
> - “Backward” means moving away from the subject. Image 2 is definitely further away than Image 1. The shoes are much smaller. So “backward” is the primary movement.
> - Is there a lateral movement?
> - In Image 1, the black/white sneaker is on the far right.
> - The white sandals are to its left.
> - In Image 2, the white sandals are in the front center. The black/white sneaker is behind them.
> - This suggests a significant change in arrangement or camera angle.
> - Let’s look at the background.
> - Image 1: White headboard behind the shoes.
> - Image 2: A room with clothes rack and towels. The shoes are in the same way. Wait, looking at Image 2, the shoes are on a pink surface (Hello Kitty towel?). In Image 1, they are on the same pink surface.
> - In Image 1, the background is a white padded headboard.
> - In Image 2, the background is a room with a rack. The shoes are on a pink surface.
> - In Image 1, behind the shoes is a white curved object (headboard).
> - This implies the camera moved significantly.
> - Let’s infer the translation.
> - Image 1 is a close up. Image 2 is a wide shot. This is a “backward” movement (zoom out or physically move back).
> - Let’s look at the options again.
> - A: backward-left
> - B: backward-left
> - C: backward-left
> - D: forward-right
> - E: forward-left
> - F: forward-left
> - Only A and C have “backward”. Since Image 2 is clearly further away (objects are much smaller, more context visible), the camera must have moved backward.
> - So the answer must be A or C.
> - Both A and C say “backward-left”.
> - Wait, let’s check the Max Y coordinate again.
> - If the answer is A, Max Y is 747.
> - If the answer is C, Max Y is 856.
> - I determined earlier that the sandal extending further right has Max Y = 856.
> - Let’s re-verify the “further right” condition.
>   - Sandal 1 (far left/left): Box [159, 492, 715, 747]. Max X = 715.
>   - Sandal 2 (upright/right): Box [143, 508, 765, 856]. Max X = 765.
>   - 765 > 715, so Sandal 2 has larger max X.
>   - Max Y of Sandal 2 is 856.
> - So the answer should be C.
> - Let’s double check “backward-left” translation.
> - In Image 1, the camera is closer.
> - In Image 2, the camera is further back. So “backward” is correct.
> - “Why left?”
>   - In Image 1, the view is centered on the white sandals. The sneaker is cut off on the right.
>   - In Image 2, the view includes the sneaker fully behind the white sandals, and the camera seems to have moved back and perhaps slightly left to center the composition differently? Or maybe the objects were rearranged?
> - Let’s re-examine.
> - In Image 1, behind the shoes is a white headboard.
> - In Image 2, the background is a room. This suggests the “bed” in Image 1 has disappeared from the surface in Image 2, or the angle changed drastically.
> - Actually, looking closely at Image 2, the pink towel has “Relax” and “Love” on the pink towel under the shoes. So it’s the same surface.
> - In Image 1, the camera is close to the shoes. In Image 2, it is further away.
> - Let’s look at the options provided. They mention “forward-left”, “backward-left”, “forward-right”.
> - The camera movement is probably “backward-left” because the shoes become smaller and the framing shifts.
> - Therefore, answer C.
> {"answer": "C"}
> </think>
> ```

> Para. 9[CN]:

> ```text
> <think>
> 用户希望我根据边界框识别一只特定的凉鞋，然后确定相机运动。
> **1. 识别目标凉鞋。**
> - 提示要求考虑“第一张图中的两只带珍珠带的白色凉鞋”。
> - 我需要找到这两只凉鞋的边界框。
> - 凉鞋 1（左侧/后方）：这是位于更后面、稍微偏左的那只。它的带子上有珍珠。
> - 凉鞋 2（右侧/前方）：这是靠近右前方的那只。它的带子上也有珍珠。等等，让我再仔细看看。
> - 在图像 1 中：
>   - 前景中有一只凉鞋 [143, 508, 765, 856]。
>   - 有一只白色凉鞋大致朝左。它有珍珠带。
> - 还有另一只凉鞋在它后面/左侧 [159, 492, 715, 747]。这一只在左侧并且稍微靠后。
> - 问题询问：“确定这两只凉鞋中哪一只的边界框向右延伸得更远（具有更大的最大 x 坐标）。”
> - 凉鞋 1（前方/右侧）：边界框大约为 [143, 508, 765, 856]。最大 x 为 765。
> - 凉鞋 2（后方/左侧）：边界框大约为 [159, 492, 715, 747]。最大 x 为 715。
> - 比较最大 x：凉鞋 1（765）> 凉鞋 2（715）。因此目标凉鞋是前面那只。
> - 问题要求给出“该凉鞋边界框的最大 y 坐标”。
> - 对于前面的凉鞋 [143, 508, 765, 856]，最大 y 是 856。
> - 等等，让我核对选项。选项中的最大 y 是 747 或 856。显然它是 [y_min, y_max]。所以最大 y 是 856。
> - 既然我确定向右延伸更远的是前面的凉鞋，它的最大 y 是 856。
> - **3. 确定相机平移。**
> - 比较图像 1 和图像 2。
> - 图像 1：鞋子的特写。可以看到鞋子后面的床头板，鞋子在画面中很大。
> - 图像 2：鞋子距离更远。可以看到整个房间、衣架和毛巾。
> - 相机向“后方”移动了（远离鞋子），以捕捉更多场景。
> - 同时，角度发生了变化。在图像 1 中，我们略微从右侧向下看。在图像 2 中，我们在更远的位置，并且更接近从正面看。
> - 观察鞋子相对于画面的位置。
> - 图像 1：鞋子位于中间/底部。
> - 图像 2：鞋子位于中间/底部。
> - 等等，让我看看选项。
> - 选项包括“向后左方”“向前左方”“向前右方”。
> - “向后”意味着远离主体。图像 2 确实比图像 1 更远。鞋子小了很多。因此“向后”是主要运动。
> - 是否存在横向运动？
> - 在图像 1 中，黑白运动鞋位于最右侧。
> - 白色凉鞋在它的左侧。
> - 在图像 2 中，白色凉鞋位于前方中央。黑白运动鞋在它们后面。
> - 这表明构图或相机角度发生了显著变化。
> - 看看背景。
> - 图像 1：鞋子后面是白色床头板。
> - 图像 2：有衣架和毛巾的房间。鞋子还是以同样的方式出现。等等，观察图像 2，鞋子位于粉色表面上（Hello Kitty 毛巾？）。图像 1 中它们也位于相同的粉色表面上。
> - 图像 1 中，鞋子后面是白色软垫床头板。
> - 图像 2 中，背景是一个带架子的房间。鞋子位于粉色表面上。
> - 图像 1 中，鞋子后面是一个白色弯曲物体（床头板）。
> - 这说明相机发生了显著移动。
> - 推断平移方向。
> - 图像 1 是特写。图像 2 是广角图。这是“向后”移动（缩小镜头或实际向后移动）。
> - 再次看看选项。
> - A：向后左方
> - B：向后左方
> - C：向后左方
> - D：向前右方
> - E：向前左方
> - F：向前左方
> - 只有 A 和 C 包含“向后”。由于图像 2 明显更远（物体更小，能看到更多上下文），相机一定是向后移动。
> - 因此答案必须是 A 或 C。
> - A 和 C 都写着“向后左方”。
> - 等等，再检查一次最大 Y 坐标。
> - 如果答案是 A，最大 Y 是 747。
> - 如果答案是 C，最大 Y 是 856。
> - 我之前确定向右延伸更远的凉鞋最大 Y = 856。
> - 再次核实“更向右”这一条件。
>   - 凉鞋 1（最左/左侧）：边界框 [159, 492, 715, 747]。最大 X = 715。
>   - 凉鞋 2（直立/右侧）：边界框 [143, 508, 765, 856]。最大 X = 765。
>   - 765 > 715，因此凉鞋 2 的最大 X 更大。
>   - 凉鞋 2 的最大 Y 是 856。
> - 因此答案应为 C。
> - 再次确认“向后左方”平移。
> - 图像 1 中，相机距离更近。
> - 图像 2 中，相机向后退得更远。因此“向后”是正确的。
> - “为什么是左？”
>   - 图像 1 中，视野以白色凉鞋为中心。运动鞋在右侧被截断。
>   - 图像 2 中，白色凉鞋后面的运动鞋完整可见，而且相机似乎向后并可能略微向左移动，以不同方式使构图居中？或者物体被重新排列了？
> - 重新检查。
> - 图像 1 中，鞋子后面是白色床头板。
> - 图像 2 中，背景是房间。这说明图像 1 中的“床”在图像 2 中从表面上消失了，或者角度发生了剧烈变化。
> - 实际上，仔细看图像 2，粉色毛巾上有“Relax”和“Love”，鞋子就位于这条粉色毛巾上。因此是同一个表面。
> - 图像 1 中，相机靠近鞋子。图像 2 中，相机更远。
> - 看看给出的选项。它们包括“向前左方”“向后左方”“向前右方”。
> - 相机运动很可能是“向后左方”，因为鞋子变小了，构图也发生了偏移。
> - 因此，答案为 C。
> {"answer": "C"}
> </think>
> ```

> ## w/ Tools (Correct)

> ## 使用工具（正确）

> ```text
> <think>
> The user wants to analyze two images and answer three specific questions:
> **Task 1: Analyze the first image.**
> - Locate the "two white sandals with pearl straps".
> - Determine which one has a bounding box extending further to the right (larger max x-coordinate).
> - Find the maximum y-coordinate of that specific sandal’s bounding box.
> **Task 2: Analyze the camera motion.**
> - Determine the direction of the camera’s translation from the first image to the second image.
> **Step-by-step Plan:**
> 1. *Locate the sandals in Image 1:* I need to find the two white sandals. Looking at Image 1, there are two distinct white heeled sandals sitting on a pink cloth. They have pearl-like embellishments on the toe strap. One is slightly behind/left of the other. Wait, let’s look closer.
> - There is a pair of white strappy heels.
> - One is more towards the left/back (further away).
> - One is more towards the front/right (closer).
> - Actually, looking at the layout: There is a sandal whose heel is visible on the right side and toe pointing left. And another sandal behind it. Let’s use ‘query_locate’ to get precise bounding boxes for "white sandals with pearl straps" or similar.
> **Step 2: Determine the right-most sandal.** Compare the bbox_2d values. Specifically, look at x_max (the third value in [x_min, y_min, x_max, y_max]).
> - Sandal A (foreground): likely has a larger x_max because it’s more to the right.
> - Sandal B (background): likely has a smaller x_max.
> 3. **Find max y-coordinate.** Once the right-most sandal is identified, take its y_max (the fourth value in the bbox).
> 4. **Determine camera motion:** Use "query_pose" with "camera motion" from Image 1 to Image 2.
> - Image 1 shows a close-up of the shoes.
> - Image 2 shows the same shoes but from a different angle. The background has changed significantly. Wait, looking at Image 2, the shoes are on a pink surface (Hello Kitty towel?). In Image 1, they are on the same pink surface.
> - Let’s use the tool for specific camera motion (e.g., "backward-left", "forward-right").
> Let’s start with the tool calls.
> </think>

> <tool_call>
> {
>   "name": "query_locate",
>   "arguments": {
>     "query": "white sandals with pearl straps",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>
> ```

> Para. 10[CN]:

> ```text
> <think>
> 用户希望分析两张图像并回答三个具体问题：
> **任务 1：分析第一张图像。**
> - 定位“带珍珠带的两只白色凉鞋”。
> - 确定哪一只的边界框向右延伸得更远（最大 x 坐标更大）。
> - 找出这只特定凉鞋边界框的最大 y 坐标。
> **任务 2：分析相机运动。**
> - 确定相机从第一张图像到第二张图像的平移方向。
> **分步计划：**
> 1. *定位图像 1 中的凉鞋：*我需要找到两只白色凉鞋。观察图像 1，可以看到两只明显的白色高跟凉鞋，放在一块粉色布上。它们的鞋头带上有类似珍珠的装饰。一只在另一只的后面/左侧。等等，让我再仔细看看。
> - 有一双白色系带高跟鞋。
> - 一只更靠左/后方（距离更远）。
> - 一只更靠前/右方（距离更近）。
> - 实际上，观察布局：有一只凉鞋的鞋跟在右侧可见，鞋头指向左侧。还有一只凉鞋在它后面。让我们使用 `query_locate`，为“带珍珠带的白色凉鞋”或类似查询获取精确边界框。
> **第 2 步：确定最右侧的凉鞋。**比较 `bbox_2d` 的值。具体来说，观察 x_max（`[x_min, y_min, x_max, y_max]` 中的第三个值）。
> - 凉鞋 A（前景）：可能具有更大的 x_max，因为它更靠右。
> - 凉鞋 B（背景）：可能具有更小的 x_max。
> 3. **找出最大 y 坐标。**确定最右侧的凉鞋后，取其 y_max（边界框中的第四个值）。
> 4. **确定相机运动：**使用 `query_pose`，查询从图像 1 到图像 2 的“camera motion”。
> - 图像 1 展示鞋子的特写。
> - 图像 2 展示相同的鞋子，但角度不同。背景发生了显著变化。等等，观察图像 2，鞋子位于粉色表面上（Hello Kitty 毛巾？）。图像 1 中它们也位于同一粉色表面上。
> - 让我们使用工具查询具体的相机运动（例如“向后左方”“向前右方”）。
> 让我们开始调用工具。
> </think>

> <tool_call>
> {
>   "name": "query_locate",
>   "arguments": {
>     "query": "white sandals with pearl straps",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>
> ```

> # Page 39

> ```text
> <tool_response>
> {"count":1,"result":[{"bbox_2d":[143,499,857,857],"point_2d":[503,678]}]}
> [tool_call budget: at most 4 more tool calls may be made.]
> </tool_response>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[143,499,857,857],"point_2d":[503,678]}]}
> [tool_call budget: at most 4 more tool calls may be made.]
> </tool_response>

> <think>
> query_locate returned one bounding box for both sandals combined: [143, 499, 857, 857]. This suggests the tool grouped them. I need to distinguish the two individual sandals to find which has the larger maximum x-coordinate.
> Let me segment each sandal individually to get separate bounding boxes.
> </think>

> <tool_call>
> {
>   "name": "query_pose",
>   "arguments": {
>     "query": "camera motion",
>     "image_indices": [
>       1,
>       2
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[143,499,857,857],"point_2d":[503,678]}]}
> </tool_response>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[143,499,857,857],"point_2d":[503,678]}]}
> </tool_response>

> <think>
> query_locate returned only one bounding box for both sandals combined: [143,499,857,857]. This suggests the tool grouped them. I need to distinguish the two individual sandals to find which has the larger maximum x-coordinate.
> Let me segment each sandal individually to get separate bounding boxes.
> </think>
> ```

> Para. 11[CN]:

> ```text
> <tool_response>
> {"count":1,"result":[{"bbox_2d":[143,499,857,857],"point_2d":[503,678]}]}
> [工具调用预算：最多还可进行 4 次工具调用。]
> </tool_response>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[143,499,857,857],"point_2d":[503,678]}]}
> [工具调用预算：最多还可进行 4 次工具调用。]
> </tool_response>

> <think>
> query_locate 返回了一个涵盖两只凉鞋的边界框：[143, 499, 857, 857]。这说明工具将它们分组了。我需要区分两只单独的凉鞋，以找出哪一只具有更大的最大 x 坐标。
> 让我分别分割每只凉鞋，以获得各自的边界框。
> </think>

> <tool_call>
> {
>   "name": "query_pose",
>   "arguments": {
>     "query": "camera motion",
>     "image_indices": [
>       1,
>       2
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[143,499,857,857],"point_2d":[503,678]}]}
> </tool_response>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[143,499,857,857],"point_2d":[503,678]}]}
> </tool_response>

> <think>
> query_locate 只返回了一个涵盖两只凉鞋的边界框：[143,499,857,857]。这说明工具将它们分组了。我需要区分两只单独的凉鞋，以找出哪一只具有更大的最大 x 坐标。
> 让我分别分割每只凉鞋，以获得各自的边界框。
> </think>
> ```

> # Page 40

> ```text
> <tool_call>
> {
>   "name": "query_segment",
>   "arguments": {
>     "query": "left white sandal with pearl strap",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_call>
> {
>   "name": "query_segment",
>   "arguments": {
>     "query": "right white sandal with pearl strap",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"count":2,"result":[{"bbox_2d":[145,507,784,855],"point_2d":[464,681]},{"bbox_2d":[156,493,759,746],"point_2d":[458,620]}]}
> </tool_response>

> <think>
> The query_locate returned only one bounding box for both sandals combined: [143,499,857,857]. This suggests the tool grouped them. I need to distinguish between the two individual sandals to find which has the larger maximum x-coordinate.
> Let me segment each sandal individually to get their separate bounding boxes.
> </think>

> <tool_call>
> {
>   "name": "query_segment",
>   "arguments": {
>     "query": "left white sandal with pearl strap",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_call>
> {
>   "name": "query_segment",
>   "arguments": {
>     "query": "right white sandal with pearl strap",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"count":2,"result":[{"bbox_2d":[145,507,784,855],"point_2d":[464,681]},{"bbox_2d":[156,493,759,746],"point_2d":[458,620]}]}
> </tool_response>

> <think>
> The query_locate returned only one bounding box for both sandals combined: [143,499,857,857]. This suggests the tool grouped them. I need to distinguish between the two individual sandals to find which has the larger maximum x-coordinate.
> Let me segment each sandal individually to get their separate bounding boxes.
> </think>
> ```

> Para. 12[CN]:

> ```text
> <tool_call>
> {
>   "name": "query_segment",
>   "arguments": {
>     "query": "left white sandal with pearl strap",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_call>
> {
>   "name": "query_segment",
>   "arguments": {
>     "query": "right white sandal with pearl strap",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"count":2,"result":[{"bbox_2d":[145,507,784,855],"point_2d":[464,681]},{"bbox_2d":[156,493,759,746],"point_2d":[458,620]}]}
> </tool_response>

> <think>
> query_locate 只返回了两只凉鞋合并后的一个边界框：[143,499,857,857]。这说明工具将它们分组了。我需要区分两个单独的凉鞋，以找出哪个凉鞋具有更大的最大 x 坐标。
> 让我分别分割每个凉鞋，获得各自的边界框。
> </think>

> <tool_call>
> {
>   "name": "query_segment",
>   "arguments": {
>     "query": "left white sandal with pearl strap",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_call>
> {
>   "name": "query_segment",
>   "arguments": {
>     "query": "right white sandal with pearl strap",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"count":2,"result":[{"bbox_2d":[145,507,784,855],"point_2d":[464,681]},{"bbox_2d":[156,493,759,746],"point_2d":[458,620]}]}
> </tool_response>

> <think>
> query_locate 只返回了两只凉鞋合并后的一个边界框：[143,499,857,857]。这说明工具将它们分组了。我需要区分两个单独的凉鞋，以找出哪个凉鞋具有更大的最大 x 坐标。
> 让我分别分割每个凉鞋，获得各自的边界框。
> </think>
> ```

> # Page 41

> ```text
> <tool_response>
> {"count":2,"result":[{"bbox_2d":[145,507,784,855],"point_2d":[464,681]},{"bbox_2d":[156,493,759,746],"point_2d":[458,620]}]}
> </tool_response>

> <tool_response>
> {"count":0,"result":[]}
> </tool_response>
> [tool-call budget: at most 1 more tool call may be made.]

> <think>
> The query_locate returned only one bounding box likely encompasses both sandals together. The tool query_segment returned two instances, but looking at the boxes:
> First instance bbox_2d=[145,507,784,855], so max_x=784, so max_y=855
> Second instance bbox_2d=[156,493,759,746], so max_x=759, so max_y=746
> Wait, let me re-read the segment results more carefully:
> Result 1: bbox_2d=[145,507,784,855], point_2d=[464,681]
> Result 2: bbox_2d=[156,493,759,746], point_2d=[458,620]
> For Result 1: min_x=145, min_y=507, max_x=784, max_y=855
> For Result 2: min_x=156, min_y=493, max_x=759, max_y=746
> The sandal with the larger maximum x-coordinate is Result 1 (x_max=784). Its maximum y-coordinate is 855. But wait, the options mention maximum y-coordinate of the sandal (Result 1 855). So the answer should be E.
> </think>

> {"answer": "E"}
> ```

> Para. 13[CN]:

> ```text
> <tool_response>
> {"count":2,"result":[{"bbox_2d":[145,507,784,855],"point_2d":[464,681]},{"bbox_2d":[156,493,759,746],"point_2d":[458,620]}]}
> </tool_response>

> <tool_response>
> {"count":0,"result":[]}
> </tool_response>
> [工具调用预算：最多还可进行 1 次工具调用。]

> <think>
> query_locate 返回的一个边界框可能涵盖了两只凉鞋。工具 query_segment 返回了两个实例，但观察这些边界框：
> 第一个实例 bbox_2d=[145,507,784,855]，所以 max_x=784，因此 max_y=855。
> 第二个实例 bbox_2d=[156,493,759,746]，所以 max_x=759，因此 max_y=746。
> 等等，让我更仔细地重新读取分割结果：
> 结果 1：bbox_2d=[145,507,784,855]，point_2d=[464,681]
> 结果 2：bbox_2d=[156,493,759,746]，point_2d=[458,620]
> 对于结果 1：min_x=145，min_y=507，max_x=784，max_y=855
> 对于结果 2：min_x=156，min_y=493，max_x=759，max_y=746
> 最大 x 坐标更大的凉鞋是结果 1（x_max=784）。其最大 y 坐标是 855。但是等等，选项提到了凉鞋的最大 y 坐标（结果 1 为 855）。因此答案应为 E。
> </think>

> {"answer": "E"}
> ```

> # Page 42

> ```text
> <tool_call>
> {
>   "name": "query_depth",
>   "arguments": {
>     "points": [
>       [
>         310,
>         524
>       ],
>       [
>         773,
>         643
>       ]
>     ],
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"result":[{"point_2d":[310,524],"depth_m":0.928},{"point_2d":[773,643],"depth_m":0.776}]}
> </tool_response>

> <think>
> Now I have the locations of both trash cans in image 1:
> - Beige trash can: point_2d [310, 524]
> - Blue trash can: point_2d [773, 643]
> I need to query the depth at these two points to determine which is closer to the camera. Let me also note that the beige one is on the left (x=310) and the blue one is on the right (x=773) in the image.
> The camera motion result shows view_rotation direction is "right" with dominant_axis "+Y".
> Let me query the depths to confirm which receptacle is closer.
> </think>
> ```

> Para. 14[CN]:

> ```text
> <tool_call>
> {
>   "name": "query_depth",
>   "arguments": {
>     "points": [
>       [
>         310,
>         524
>       ],
>       [
>         773,
>         643
>       ]
>     ],
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"result":[{"point_2d":[310,524],"depth_m":0.928},{"point_2d":[773,643],"depth_m":0.776}]}
> </tool_response>

> <think>
> 现在我已经获得了图像 1 中两个垃圾桶的位置：
> - 米色垃圾桶：point_2d [310, 524]
> - 蓝色垃圾桶：point_2d [773, 643]
> 我需要查询这两个点的深度，以确定哪个更靠近相机。同时注意，米色垃圾桶在左侧（x=310），蓝色垃圾桶在右侧（x=773）。
> 相机运动结果显示，视角旋转方向是“right”，主轴为“+Y”。
> 让我查询深度，以确认哪个垃圾桶更近。
> </think>
> ```

> # Page 43

> ```text
> <tool_response>
> {"result":[{"point_2d":[310,524],"depth_m":0.928},{"point_2d":[773,643],"depth_m":0.776}]}
> </tool_response>

> <tool_response>
> {"result":[{"from_image":1,"to_image":2,"position":{"direction":"forward-right","axes":["+X","+Y","-Z"],"view_rotation":{"direction":"right","axes":["+X","+Y","-Z"],"dominant_axis":"Y"}}}]}
> </tool_response>

> <think>
> Now I have the locations of both trash cans in image 1:
> - Beige trash can: point_2d [310, 524]
> - Blue trash can: point_2d [773, 643]
> I need to query the depth at these two points to determine which is closer to the camera. Let me also note that the beige one is on the left (x=310) and the blue one is on the right (x=773) in the image.
> The camera motion result shows view_rotation direction is "right" with dominant_axis "+Y".
> Let me query the depths to confirm which receptacle is closer.
> </think>

> <tool_call>
> {
>   "name": "query_depth",
>   "arguments": {
>     "points": [
>       [
>         310,
>         524
>       ],
>       [
>         773,
>         643
>       ]
>     ],
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>
> ```

> Para. 15[CN]:

> ```text
> <tool_response>
> {"result":[{"point_2d":[310,524],"depth_m":0.928},{"point_2d":[773,643],"depth_m":0.776}]}
> </tool_response>

> <tool_response>
> {"result":[{"from_image":1,"to_image":2,"position":{"direction":"forward-right","axes":["+X","+Y","-Z"],"view_rotation":{"direction":"right","axes":["+X","+Y","-Z"],"dominant_axis":"Y"}}}]}
> </tool_response>

> <think>
> 现在我已经获得了图像 1 中两个垃圾桶的位置：
> - 米色垃圾桶：point_2d [310, 524]
> - 蓝色垃圾桶：point_2d [773, 643]
> 我需要查询这两个点的深度，以确定哪个更靠近相机。同时注意，米色垃圾桶在左侧（x=310），蓝色垃圾桶在右侧（x=773）。
> 相机运动结果显示，视角旋转方向是“right”，主轴为“+Y”。
> 让我查询深度，以确认哪个垃圾桶更近。
> </think>

> <tool_call>
> {
>   "name": "query_depth",
>   "arguments": {
>     "points": [
>       [
>         310,
>         524
>       ],
>       [
>         773,
>         643
>       ]
>     ],
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>
> ```

> # Page 44

> ## H.3  Case 3: SpatialCLI-8B after Capability Internalization

> ## H.3  案例 3：SpatialCLI-8B 能力内化之后

> Para. 16: The task input and ground truth are shown in Box H.3. The full-width traces below present, in order, the tool-free Qwen3-VL-8B-Instruct baseline, SpatialCLI-8B with tools, and SpatialCLI-8B without tools. The baseline correctly identifies the yellow ball as farther right and the camera translation as forward-left, but confuses the first-image depth relation while repeatedly reasoning from cross-image scale change; it therefore predicts that the yellow ball is closer and selects F. SpatialCLI-8B with tools first grounds the objects and then queries depth and camera motion. The returned horizontal centers are 329 and 644, the depths are 0.351 m and 0.637 m, and the translation is forward-left, so every clause supports E. Its final cross-image Locate call is a redundant verification after the answer is already determined and does not change the conclusion. Without tools, SpatialCLI-8B produces internalized estimates of 0.362 m and 0.615 m and the same forward-left motion, yielding E directly. The appendix qualitatively illustrates agreement between internalized direct answering and runtime tool verification on the same task.

> Para. 16[CN]: 任务输入和真实答案显示在框 H.3 中。下面的全宽轨迹依次展示了不使用工具的 Qwen3-VL-8B-Instruct 基线、使用工具的 SpatialCLI-8B，以及不使用工具的 SpatialCLI-8B。基线正确识别出黄色球位于更右侧，并正确判断相机向前左方平移，但混淆了第一张图中的深度关系，并反复根据跨图像尺度变化进行推理；因此它判断黄色球更近，并选择 F。使用工具的 SpatialCLI-8B 首先定位物体，然后查询深度和相机运动。返回的水平中心为 329 和 644，深度为 0.351 m 和 0.637 m，平移方向为 forward-left，因此每一条款都支持 E。它最后进行的跨图像 Locate 调用是在答案已经确定之后的冗余验证，并未改变结论。不使用工具时，SpatialCLI-8B 产生了 0.362 m 和 0.615 m 的内化估计，以及相同的 forward-left 运动，直接得到 E。附录定性地展示了在同一任务上，内化后的直接作答与运行时工具验证之间的一致性。

> > **Box H.3: Task (SpatialCLI-Bench ID 170)**  
> > **框 H.3：任务（SpatialCLI-Bench ID 170）**

> **Image 1**  
> **图像 1**

> **Image 2**  
> **图像 2**

> Para. 17: In the first image, which object is located further to the right between the clear plastic bottle and the yellow ball, which of the two is closer to the camera, and in which direction did the camera translate to capture the second image?  
> Options:  
> A: The yellow ball is further to the right, the clear plastic bottle is closer to the camera, and the camera translated backward-left.  
> B: The clear plastic bottle is further to the right, the yellow ball is closer to the camera, and the camera translated forward-left.  
> C: The clear plastic bottle is further to the right, the yellow ball is closer to the camera, and the camera translated forward-right.  
> D: The yellow ball is further to the right, the clear plastic bottle is closer to the camera, and the camera translated forward-right.  
> E: The yellow ball is further to the right, the clear plastic bottle is closer to the camera, and the camera translated forward-left.  
> F: The yellow ball is further to the right, the yellow ball is closer to the camera, and the camera translated forward-left.

> Para. 17[CN]: 在第一张图像中，在透明塑料瓶和黄色球之间，哪一个物体位于更右侧？两者中哪一个更靠近相机？相机以哪个方向平移以拍摄第二张图像？  
> 选项：  
> A：黄色球位于更右侧，透明塑料瓶更靠近相机，相机向后左方平移。  
> B：透明塑料瓶位于更右侧，黄色球更靠近相机，相机向前左方平移。  
> C：透明塑料瓶位于更右侧，黄色球更靠近相机，相机向前右方平移。  
> D：黄色球位于更右侧，透明塑料瓶更靠近相机，相机向前右方平移。  
> E：黄色球位于更右侧，透明塑料瓶更靠近相机，相机向前左方平移。  
> F：黄色球位于更右侧，黄色球更靠近相机，相机向前左方平移。

> Before choosing, briefly state the relevant facts and verify every clause of the selected option against all evidence available during solving. For any depth observations, smaller values mean closer; do not retain an earlier visual guess after receiving stronger evidence. Please show your choice in the answer field with only the choice letter, e.g., {"answer": "C"}.

> Para. 18[CN]: 在作出选择之前，简要陈述相关事实，并根据解题过程中获得的全部证据核实所选选项的每一个条款。对于任何深度观察，数值越小表示越近；在获得更强证据后，不要保留早先的视觉猜测。请在答案字段中只填写选项字母，例如 `{"answer": "C"}`。

> **Ground Truth**  
> **真实答案**

> Correct option: E.

> Para. 19[CN]: 正确选项：E。

> ## Qwen3-VL-8B-Instruct w/o Tools (Incorrect)

> ## Qwen3-VL-8B-Instruct 不使用工具（错误）

> ```text
> <think>
> To determine the correct option, I will analyze the spatial relationships and camera movement between the two images.
> **Step 1: Analyze relative positions in the first image.**
> In the first image, the clear plastic bottle is on the left side of the frame, and the yellow ball is to its right. The bottle is positioned closer to the foreground (and thus the camera) than the ball, as it appears larger and more detailed. Therefore:
> - The yellow ball is further to the right.
> - The clear plastic bottle is closer to the camera.
> **Step 2: Analyze camera translation from the first image to the second image.**
> In the first image, the bottle is prominent in the foreground. In the second image, the bottle is now on the far right edge of the frame and is much smaller, indicating it has been moved farther away from the camera's viewpoint. The yellow ball, which was to the right of the bottle in the first image, is now more centrally located and appears larger than before, suggesting it has also moved closer to the camera and/or the camera has moved toward it.
> The key observation for camera movement is that the bottle has moved from a dominant foreground position to a background position on the right. This implies the camera has moved backward (away from the bottle) and to the left (to reposition the bottle to the right edge of the frame). The yellow ball, being to the right image-wise, moved to the left relative to the bottle's new position, but since the camera moved left, the ball appears to shift to the scene. However, the ball is now more central and larger, so the camera moved forward (toward the ball) and to the left (to bring the ball into the center).
> Wait – let me reconsider this carefully.
> Actually, looking at the second image, the yellow ball is now more central, and the bottle is on the far right. The bottle is smaller in the second image, meaning the camera is closer to it? The ball is larger in the second image, meaning the camera is closer to the ball. But the ball is further to the right of the bottle in the first image, and now it is more central. Therefore, the camera must have moved to the left (so the bottle moves to the right edge) and forward (so the ball gets larger).
> This matches option E: "The yellow ball is further to the right, the clear plastic bottle is closer to the camera, and the camera translated forward-left."
> I need to verify the "further to the right" clause. In the first image, the bottle is on the left, the ball is on the right. That part is correct.
> The bottle is closer to the camera – correct, because the bottle moves to the right edge (camera moved left) and gets smaller (camera moved back), but the bottle was larger in the first image, so the camera must have moved back. Wait, if the camera moved left and the bottle got larger, and if it moves to the right edge, the bottle should move to the right edge. But in the second image, the bottle is on the right edge and smaller, and the ball is larger and more central. So yes, the camera moved forward and to the left.
> Let me check other options:
> A: Says camera translated backward-left – but if camera moved backward, the bottle should appear even smaller, which it does, but the ball should appear smaller too, which it doesn’t. Also, if camera moved backward-left, the ball would be moving to the left, not becoming more central. So A is wrong.
> B: Says clear plastic bottle is further to the right – again, no, in the first image, the bottle is on the left.
> C: Says clear plastic bottle is further to the right – again, no, in the first image, the bottle is on the left.
> D: Says camera translated forward-right – if camera moved forward-right, the bottle would be more to the right, which it is, but the ball would be larger and stay same size, not larger. So D is wrong. So D is wrong.
> F: Says yellow ball is closer to the camera – yes, it appears larger – but it also says “the camera translated forward-left” which is also true. But the question asks for the object that is further to the right and which is closer to the camera – the bottle is closer, not the ball. So F is incorrect because it incorrectly states that the yellow ball is closer to the camera. Wait, F says: "The yellow ball is further to the right, the yellow ball is closer to the camera, and the camera translated forward-left." This is factually incorrect because the bottle is closer to the camera, not the yellow ball. So F is wrong.
> Therefore, the answer is E.
> {"answer": "E"}
> ```

> Para. 20[CN]:

> ```text
> <think>
> 为了确定正确选项，我将分析两张图像之间的空间关系和相机运动。
> **第 1 步：分析第一张图像中的相对位置。**
> 在第一张图像中，透明塑料瓶位于画面左侧，黄色球位于它的右侧。瓶子更靠近前景（因此也更靠近相机），因为它看起来更大、细节更多。因此：
> - 黄色球位于更右侧。
> - 透明塑料瓶更靠近相机。
> **第 2 步：分析从第一张图像到第二张图像的相机平移。**
> 在第一张图像中，瓶子突出地位于前景。在第二张图像中，瓶子现在位于画面的最右边缘，并且小了很多，这表明它距离相机视点更远。黄色球在第一张图像中位于瓶子的右侧，现在位于更靠近中央的位置，并且看起来比以前更大，这表明它也更靠近相机了，和/或相机朝它移动了。
> 关于相机运动的关键观察是，瓶子从占据主导地位的前景位置移动到了右侧的背景位置。这意味着相机向后移动（远离瓶子），并向左移动（使瓶子重新定位到画面右边缘）。黄色球从图像位置上位于右侧，相对于瓶子的新位置向左移动，但由于相机向左移动，球看起来向场景的方向移动。然而，球现在更居中且更大，因此相机向前（朝向球）并向左移动（将球带到中央）。
> 等等——让我仔细重新考虑。
> 实际上，观察第二张图像，黄色球现在更靠中央，瓶子位于最右侧。第二张图像中的瓶子更小，这意味着相机离它更近吗？第二张图像中的球更大，这意味着相机离球更近。但球在第一张图像中位于瓶子的右侧，现在更靠中央。因此，相机一定是向左移动（使瓶子移到右边缘）并向前移动（使球变大）。
> 这与选项 E 相符：“黄色球位于更右侧，透明塑料瓶更靠近相机，相机向前左方平移。”
> 我需要核实“更右侧”这一条款。在第一张图像中，瓶子位于左侧，球位于右侧。这一部分正确。
> 瓶子更靠近相机——正确，因为瓶子移到了右边缘（相机向左移动）并且变小了（相机向后移动），但瓶子在第一张图像中更大，所以相机一定向后移动。等等，如果相机向左移动且瓶子变大，并且瓶子移到右侧边缘，那么瓶子应该移到右侧边缘。但在第二张图像中，瓶子位于右侧边缘并且更小，而球更大且更居中。因此，是的，相机向前并向左移动了。
> 让我检查其他选项：
> A：说相机向后左方平移——但如果相机向后移动，瓶子应该变得更小，这确实如此，但球也应该变小，而事实并非如此。另外，如果相机向后左方移动，球应该向左移动，而不是变得更居中。因此 A 错误。
> B：说透明塑料瓶位于更右侧——不，在第一张图像中瓶子在左侧。
> C：说透明塑料瓶位于更右侧——同样不，在第一张图像中瓶子在左侧。
> D：说相机向前右方平移——如果相机向前右方移动，瓶子应该更靠右，而事实确实如此，但球应该变大并保持相同尺寸，而不是变大。因此 D 错误。所以 D 错误。
> F：说黄色球更靠近相机——是的，它看起来更大——但它还说“相机向前左方平移”，这也是真的。但问题询问的是位于更右侧且更靠近相机的物体——更靠近相机的是瓶子，而不是球。因此 F 错误，因为它错误地说黄色球更靠近相机。等等，F 说：“黄色球位于更右侧，黄色球更靠近相机，相机向前左方平移。”这在事实上是错误的，因为瓶子更靠近相机，而不是黄色球。因此 F 错误。
> 所以，答案是 E。
> {"answer": "E"}
> ```

> ## SpatialCLI-8B w/ Tools (Correct)

> ## SpatialCLI-8B 使用工具（正确）

> ```text
> <think>
> The user wants me to analyze two images and answer three specific questions:
> 1. **Which object is further to the right in the first image?** (Clear plastic bottle vs. Yellow ball)
> 2. **Which object is closer to the camera in the first image?**
> 3. **In which direction did the camera translate to capture the second image?**
> Let’s break this down step-by-step.
> **Step 1: Analyze the first image for horizontal position (left/right).**
> - I need to locate the "clear plastic bottle" and "yellow ball" in Image 1.
> - At first glance, the clear plastic bottle is on the left side, very prominent in the foreground.
> - The yellow ball is further back and to the right.
> - Let’s use `query_locate` to get precise coordinates if needed, but visually it seems quite clear. The bottle is central-left, the ball is right-ish. Wait, let’s look closer.
> - In Image 1:
>   - Bottle: Occupies the left/center foreground.
>   - Ball: Located to the right of the bottle.
> - Therefore, the yellow ball is further to the right.
> **Step 2: Analyze the first image for depth (closer/further).**
> - I need to determine which is closer: the bottle or the ball.
> - Visually, the bottle is much larger and obscures the background. It is clearly in the immediate foreground.
> - The ball is smaller and sits further back on the patterned mat.
> - So, the clear plastic bottle is closer to the camera.
> - To be rigorous, I can use `query_depth`. I will locate both objects first to get their centers, then query depth.
> **Step 3: Analyze camera translation between Image 1 and Image 2.**
> - I need to determine the translation direction.
> - Image 1 shows the bottle prominently on the left.
> - Image 2 shows the bottle cut off on the far right edge (partially visible) and a toothbrush on a cloth on the left. The yellow ball is now more central/left.
> - Let’s look at the background features.
> - Image 1: Person standing in the distance center-right. White cabinet/shelf unit on the right.
> - Image 2: Glass door/window structure visible. Red box on the left. The person is still visible in the background but perspective has changed.
> - Let’s use `query_pose` with "camera motion" to get the exact translation/rotation direction.
> **Plan:**
> 1. Locate "clear plastic bottle" and "yellow ball" in Image 1 to confirm positions and get points for depth.
> 2. Query depth for the centers of these two objects in Image 1 to confirm which is closer.
> 3. Query "camera motion" between Image 1 and Image 2.
> **Execution:**
> 1. `query_locate` for "clear plastic bottle" and "yellow ball" in image 1.
> 2. `query_depth` using the points obtained.
> 3. `query_pose` with "camera motion".
> Let’s refine the queries.
> - Query 1: `query_locate` with query="clear plastic bottle", image_indices=[1]
> - Query 2: `query_locate` with query="yellow ball", image_indices=[1]
> - Query 3: `query_depth` using points from above.
> - Query 4: `query_pose` with query="camera motion", image_indices=[1, 2] (Wait, the tool description says “Omit image_indices if need to relate two images”. Since there are two images, I should probably just pass the query. Or maybe specify image_indices [1, 2]. The description says “In a multi-image... omit image_indices to use all images.” So I’ll omit it.)
> Let’s start.
> </think>
> ```

> Para. 21[CN]:

> ```text
> <think>
> 用户希望我分析两张图像并回答三个具体问题：
> 1. **第一张图像中哪个物体更靠右？**（透明塑料瓶还是黄色球）
> 2. **第一张图像中哪个物体更靠近相机？**
> 3. **相机以哪个方向平移以拍摄第二张图像？**
> 让我们逐步分析。
> **第 1 步：分析第一张图像中的水平位置（左/右）。**
> - 我需要定位图像 1 中的“透明塑料瓶”和“黄色球”。
> - 第一眼看，透明塑料瓶位于左侧，在前景中非常突出。
> - 黄色球更靠后并位于右侧。
> - 如果需要，可以使用 `query_locate` 获取精确坐标，但从视觉上看已经很清楚。瓶子位于中间偏左，球在偏右位置。等等，让我再仔细看看。
> - 在图像 1 中：
>   - 瓶子：占据左侧/中间的前景。
>   - 球：位于瓶子的右侧。
> - 因此，黄色球更靠右。
> **第 2 步：分析第一张图像中的深度（更近/更远）。**
> - 我需要确定哪个更近：瓶子还是球。
> - 从视觉上看，瓶子大得多，并遮挡了背景。它显然位于最近的前景中。
> - 球更小，位于有图案垫子上、位置更靠后。
> - 因此，透明塑料瓶更靠近相机。
> - 为了严谨起见，我可以使用 `query_depth`。我会先定位两个物体以获得它们的中心点，然后查询深度。
> **第 3 步：分析图像 1 和图像 2 之间的相机平移。**
> - 我需要确定平移方向。
> - 图像 1 展示瓶子突出地位于左侧。
> - 图像 2 展示瓶子被截断在最右侧边缘（部分可见），左侧是一块布上的牙刷。黄色球现在更靠中央/左侧。
> - 看看背景特征。
> - 图像 1：中间偏右的远处站着一个人。右侧有白色柜子/架子单元。
> - 图像 2：可以看到玻璃门/窗结构。左侧有红色盒子。背景中仍然可以看到那个人，但透视发生了变化。
> - 让我们使用 `query_pose` 并查询“camera motion”，以获得精确的平移/旋转方向。
> **计划：**
> 1. 在图像 1 中定位“透明塑料瓶”和“黄色球”，确认位置并获得用于深度查询的点。
> 2. 查询这两个物体在图像 1 中的中心点深度，以确认哪个更近。
> 3. 查询图像 1 和图像 2 之间的“camera motion”。
> **执行：**
> 1. 对图像 1 中的“clear plastic bottle”和“yellow ball”调用 `query_locate`。
> 2. 使用得到的点调用 `query_depth`。
> 3. 使用“camera motion”调用 `query_pose`。
> 让我们细化查询。
> - 查询 1：调用 `query_locate`，query="clear plastic bottle"，image_indices=[1]
> - 查询 2：调用 `query_locate`，query="yellow ball"，image_indices=[1]
> - 查询 3：使用上面获得的点调用 `query_depth`。
> - 查询 4：调用 `query_pose`，query="camera motion"，image_indices=[1, 2]（等等，工具描述说“如果需要关联两张图像，则省略 image_indices”。由于有两张图像，我可能应该只传入 query。或者也可以指定 image_indices [1, 2]。描述说“在多图像……中，省略 image_indices 以使用所有图像”。所以我将省略它。）
> 开始。
> </think>
> ```

> # Page 45

> ```text
> <tool_call>
> {
>   "name": "query_locate",
>   "arguments": {
>     "query": "clear plastic bottle",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_call>
> {
>   "name": "query_locate",
>   "arguments": {
>     "query": "yellow ball",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[127,0,531,834],"point_2d":[329,417]}]}
> </tool_response>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[560,283,729,414],"point_2d":[644,348]}]}
> </tool_response>

> <think>
> The clear plastic bottle center is at [329, 417] and the yellow ball center is at [644, 348]. Comparing x-coordinates: 644 > 329, so the yellow ball is further to the right.
> Now I need to determine which object is closer to the camera in image 1. Let me query the depth of both points.
> </think>

> <tool_call>
> {
>   "name": "query_depth",
>   "arguments": {
>     "points": [
>       [
>         329,
>         417
>       ],
>       [
>         644,
>         348
>       ]
>     ],
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"result":[{"point_2d":[329,417],"depth_m":0.351},{"point_2d":[644,348],"depth_m":0.637}]}
> </tool_response>

> <think>
> From the tool calls:
> - In image 1:
>   - The clear plastic bottle center is at [329, 417].
>   - The yellow ball center is at [644, 348].
>   - Comparing x-coordinates: 644 > 329, so the **yellow ball is further to the right**.
>   - Depth values (smaller = closer): bottle depth_m = 0.351, ball depth_m = 0.637. So the **clear plastic bottle is closer to the camera**.
> - Camera motion from image 1 to image 2:
>   - Image 1 shows the bottle prominently on the left.
>   - Image 2 shows the bottle mostly out of frame or just on the far right (actually, looking closely at image 2, the bottle is barely visible on the far right edge, and the ball is now more central-left).
>   - The red box which was not clearly visible or was further back/left is now visible.
>   - Actually, let’s re-examine the scene layout.
>   - Image 1: Bottle is close, bottom-left/center. Ball is behind it, to the right.
>   - Image 2: The view has shifted. The ball is now in the upper-left quadrant relative to the new frame. A red object (looks like a toy bus) is visible on the far left. The white cloth with green dots is in the foreground left.
>   - Let’s look at the background floor/wall features.
>   - In image 1, there is a person standing in the background hallway.
>   - In image 2, that same person is visible but lower in the frame, suggesting the camera moved forward and tilted down or moved upward? Wait, let’s look at the options provided. They mention “forward-left”, “backward-left”, “forward-right”.
>   - Let’s use the `query_pose` tool for camera motion between image 1 and 2.
> </think>

> <tool_call>
> {
>   "name": "query_pose",
>   "arguments": {
>     "query": "camera motion",
>     "image_indices": [
>       1,
>       2
>     ]
>   }
> }
> </tool_call>
> ```

> Para. 22[CN]:

> ```text
> <tool_call>
> {
>   "name": "query_locate",
>   "arguments": {
>     "query": "clear plastic bottle",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_call>
> {
>   "name": "query_locate",
>   "arguments": {
>     "query": "yellow ball",
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[127,0,531,834],"point_2d":[329,417]}]}
> </tool_response>

> <tool_response>
> {"count":1,"result":[{"bbox_2d":[560,283,729,414],"point_2d":[644,348]}]}
> </tool_response>

> <think>
> 透明塑料瓶的中心为 [329, 417]，黄色球的中心为 [644, 348]。比较 x 坐标：644 > 329，因此黄色球更靠右。
> 现在我需要确定图像 1 中哪个物体更靠近相机。让我查询这两个点的深度。
> </think>

> <tool_call>
> {
>   "name": "query_depth",
>   "arguments": {
>     "points": [
>       [
>         329,
>         417
>       ],
>       [
>         644,
>         348
>       ]
>     ],
>     "image_indices": [
>       1
>     ]
>   }
> }
> </tool_call>

> <tool_response>
> {"result":[{"point_2d":[329,417],"depth_m":0.351},{"point_2d":[644,348],"depth_m":0.637}]}
> </tool_response>

> <think>
> 根据工具调用：
> - 在图像 1 中：
>   - 透明塑料瓶中心为 [329, 417]。
>   - 黄色球中心为 [644, 348]。
>   - 比较 x 坐标：644 > 329，因此**黄色球更靠右**。
>   - 深度值（越小 = 越近）：瓶子的 depth_m = 0.351，球的 depth_m = 0.637。因此**透明塑料瓶更靠近相机**。
> - 从图像 1 到图像 2 的相机运动：
>   - 图像 1 展示瓶子突出地位于左侧。
>   - 图像 2 展示瓶子大部分位于画面之外，或者仅位于最右侧（实际上，仔细看图像 2，瓶子在最右侧边缘几乎不可见，而球现在更靠中央偏左）。
>   - 原来不清晰可见或位于更后方/左侧的红色盒子现在可见。
>   - 实际上，让我们重新检查场景布局。
>   - 图像 1：瓶子很近，位于左下/中间。球在它后面，位于右侧。
>   - 图像 2：视野发生了偏移。相对于新的画面，球现在位于左上象限。左侧最远处可以看到一个红色物体（看起来像玩具巴士）。左前景中有一块带绿色圆点的白布。
>   - 看看背景地面/墙面的特征。
>   - 图像 1 中，背景走廊里站着一个人。
>   - 图像 2 中，同一个人仍然可见，但在画面中的位置更低，这表明相机向前移动并向下倾斜，或者相机向上移动？等等，让我们看看给出的选项。它们提到“向前左方”“向后左方”“向前右方”。
>   - 让我们使用 `query_pose` 工具查询图像 1 和图像 2 之间的相机运动。
> </think>

> <tool_call>
> {
>   "name": "query_pose",
>   "arguments": {
>     "query": "camera motion",
>     "image_indices": [
>       1,
>       2
>     ]
>   }
> }
> </tool_call>
> ```

> # Page 46

> ```text
> <tool_response>
> {"result":[{"from_image":1,"to_image":2,"position":{"direction":"forward-left","axes":["-X","-Y","-Z"],"view_rotation":{"direction":"left","axes":["+X","-Y","-Z"],"dominant_axis":"Y"}}}]}
> </tool_response>

> <think>
> Let me verify the facts:
> 1. **Which object is further to the right?**
> - Clear plastic bottle center: [329, 417]
> - Yellow ball center: [644, 348]
> - Yellow ball center x-coordinate (644) is greater than the x-coordinate of the bottle (329), so the yellow ball is further to the right.
> 2. **Which object is closer to the camera?**
> - Bottle depth: 0.351 m
> - Ball depth: 0.637 m
> - Smaller depth means closer, so the clear plastic bottle (0.351 m) is closer to the camera than the yellow ball (0.637 m).
> 3. **Camera translation direction:**
> - The query pose result shows position.direction = "forward-left" when going from image 1 to image 2.
> So the correct option should state:
> - The yellow ball is further to the right ✓
> - The clear plastic bottle is closer to the camera ✓
> - Camera translated forward-left ✓
> This matches option E.
> </think>
> ```

> # Page 47

> Para. 23[CN]:

> ```text
> <tool_response>
> {"result":[{"from_image":1,"to_image":2,"position":{"direction":"forward-left","axes":["-X","-Y","-Z"],"view_rotation":{"direction":"left","axes":["+X","-Y","-Z"],"dominant_axis":"Y"}}}]}
> </tool_response>

> <think>
> 让我核实这些事实：
> 1. **哪个物体更靠右？**
> - 透明塑料瓶中心：[329, 417]
> - 黄色球中心：[644, 348]
> - 黄色球中心的 x 坐标（644）大于瓶子的 x 坐标（329），所以黄色球更靠右。
> 2. **哪个物体更靠近相机？**
> - 瓶子深度：0.351 m
> - 球深度：0.637 m
> - 深度越小表示越近，因此透明塑料瓶（0.351 m）比黄色球（0.637 m）更靠近相机。
> 3. **相机平移方向：**
> - query pose 的结果显示，从图像 1 到图像 2 时 position.direction = "forward-left"。
> 因此正确选项应当写明：
> - 黄色球更靠右 ✓
> - 透明塑料瓶更靠近相机 ✓
> - 相机向前左方平移 ✓
> 这与选项 E 相符。
> </think>
> ```

> # Page 48

> ## SpatialCLI-8B w/o Tools (Correct)

> ## SpatialCLI-8B 不使用工具（正确）

> ```text
> <think>
> The clear plastic bottle is located at a horizontal center x=331, while the yellow ball is at a horizontal center x=644. Since 644 > 331, the yellow ball is positioned further to the right in the first image. Depth measurements show the bottle is at 0.362 meters from the camera and the yellow ball is at 0.615 meters, meaning the bottle is closer to the camera and the yellow ball is farther away. Finally, analysis of the camera motion between the two images determines that the camera translated forward-left to capture the second image. Therefore, the yellow ball is further to the right, the clear plastic bottle is closer to the camera, and the camera moved forward-left.
> </think>

> {"answer": "E"}
> ```

> Para. 24[CN]:

> ```text
> <think>
> 透明塑料瓶的水平中心位于 x=331，而黄色球的水平中心位于 x=644。由于 644 > 331，黄色球在第一张图像中位于更右侧。深度测量显示，瓶子距离相机 0.362 米，而黄色球距离相机 0.615 米，这意味着瓶子更靠近相机，黄色球距离更远。最后，对两张图像之间相机运动的分析确定，相机向前左方平移以拍摄第二张图像。因此，黄色球更靠右，透明塑料瓶更靠近相机，相机向前左方移动。
> </think>

> {"answer": "E"}
> ```
