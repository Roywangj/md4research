# Skill-3D: Evolving Scene-Aware Skills for Agentic 3D Spatial Reasoning
**Authors:** Haoyuan Li, Zhengdong Hu, Jun Wang, Hehe Fan, Yi Yang  
**Source:** `Li 等 - 2026 - Skill-3D Evolving Scene-Aware Skills for Agentic 3D Spatial Reasoning.pdf`  
**Detected source format:** selectable-text PDF (`pdf-text`)  
**Reader type:** full-paper Chinese-English Markdown reader with figure/table assets.

## Page / Section Index
| Section | Pages | Notes |
|---|---:|---|
| Abstract | p.1 | bilingual body and related figures/tables |
| 1 Introduction | pp.1-2 | bilingual body and related figures/tables |
| 2 Related Work | pp.2-3 | bilingual body and related figures/tables |
| 3 Method | pp.3-5 | bilingual body and related figures/tables |
| 4 Experiments | pp.5-8 | bilingual body and related figures/tables |
| 5 Conclusion and Limitations | pp.8-9 | bilingual body and related figures/tables |
| Appendix A. LLM Usage Claim | p.14 | bilingual body and related figures/tables |
| Appendix B. More Experimental Results | p.14 | bilingual body and related figures/tables |
| Appendix C. Experimental Details | pp.14-15 | bilingual body and related figures/tables |
| Appendix D. Qualitative Results | pp.15-17 | bilingual body and related figures/tables |
| Appendix E. Prompt Design | pp.18-21 | bilingual body and related figures/tables |
| References | pp.9-13 | bibliography preserved in the source PDF; not translated line-by-line |

## Terminology Ledger
| Canonical term | Chinese rendering | Decision |
|---|---|---|
| Skill-3D | Skill-3D | 本文方法名；保持英文。 |
| agentic 3D spatial reasoning | agentic 3D 空间推理 | 通过 agent 和外部工具完成 3D 空间理解。 |
| MLLM | 多模态大语言模型（MLLM） | 首次展开后保持 MLLM。 |
| Scene Memory | Scene Memory | 保存场景上下文、工具轨迹、证据与失败模式的记忆。 |
| Skill Library | Skill Library | 保存 static skills 与 dynamic skills 的技能库。 |
| scene-aware skill | 场景感知技能 | 由相似场景成功轨迹蒸馏出的工具工作流。 |
| static skill | 静态技能 | 固定任务级先验。 |
| dynamic skill | 动态技能 | 可被成功/失败 rollout 合并、修补和更新的技能。 |
| rollout / trajectory | rollout / 轨迹 | 一次完整问题求解过程，包括推理、工具调用和答案。 |
| failure lesson | failure lesson / 失败教训 | 从失败轨迹中提取并附着到技能的纠错信息。 |
| effective tool usage (ETU) | 有效工具使用率（ETU） | 有效且被后续推理使用的工具调用比例。 |
| agentic SFT | agentic SFT | 在技能引导轨迹上学习结构化交互格式的监督微调。 |
| GRPO | Group Relative Policy Optimization（GRPO） | 组内相对优势优化方法。 |
| Pi3 | Pi3 | 论文使用的 3D 重建/视觉几何工具。 |
| GroundingDINO | GroundingDINO | 目标检测/grounding 工具。 |
| SAM3 | SAM3 | 分割工具。 |
| Depth Anything 3 | Depth Anything 3 | 深度估计工具。 |
| Orient Anything v2 | Orient Anything v2 | 朝向估计工具。 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This paper explores agentic 3D spatial understanding, i.e., MLLM agents performing 3D reasoning through tool use. Existing methods often misuse tools and exhibit biased tool preferences under 3D scenario, leaving the agentic paradigm with only marginal gains over non-agentic strategies. We reveal that 3D spatial reasoning tasks are heterogeneous across scenes, while these agents apply a uniform tool-use strategy to all scenes rather than selecting tools according to the specific scene and task. To address this, we propose Skill-3D, a framework that learns self-evolving scene-aware skills. Specifically, Skill-3D identifies the task scene and records the agent’s tool-use trajectory into a Scene Memory, where successful trajectories from similar scenes are aggregated and distilled into a reusable scene-aware skill, with failed ones attached to the skill as lessons. During training, once a similar scene recurs, the corresponding skill is injected to guide the agent, producing new trajectories whose successes and failures further refine the skill, forming a loop in which the memory and the skill library co-evolve. Experiments show that Skill-3D substantially improves tool utilization in 3D spatial reasoning (from 39% to 78% on VSI-Bench), driving the agent toward correct and sufficient tool use. For instance, it improves Gemini-3-Flash by 67% on MMSI-Bench. Furthermore, we conduct agentic post-training over skill-guided trajectories, which boosts Qwen3-VL-8B by 60% on VSI-Bench.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本文探索 agentic 3D 空间理解，即 MLLM agent 通过工具使用执行 3D 推理。现有方法在 3D 场景中经常误用工具，并表现出有偏的工具偏好，使得 agentic 范式相对于非 agentic 策略仅带来有限增益。我们揭示，3D 空间推理任务跨场景具有异质性，而这些 agent 对所有场景采用统一的工具使用策略，而非根据具体场景和任务选择工具。为此，我们提出 Skill-3D——一个学习自演化场景感知技能的框架。具体而言，Skill-3D 识别任务场景，并将 agent 的工具使用轨迹记录到 Scene Memory 中；其中，相似场景的成功轨迹被聚合并蒸馏为可复用的场景感知技能，失败轨迹则作为 lessons 附着于该技能。在训练期间，一旦相似场景再次出现，就注入相应技能以引导 agent，产生新的轨迹；其成功与失败会进一步细化该技能，从而形成记忆和技能库共同演化的循环。实验表明，Skill-3D 显著改善了 3D 空间推理中的工具利用（VSI-Bench 上从 39% 提升至 78%），驱动 agent 进行正确且充分的工具使用。例如，它使 Gemini-3-Flash 在 MMSI-Bench 上提升 67%。此外，我们在技能引导轨迹上进行 agentic 后训练，使 Qwen3-VL-8B 在 VSI-Bench 上提升 60%。

## 1 Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Agentic 3D spatial reasoning aims to enable multimodal large language model (MLLM) agents to solve indoor 3D understanding tasks through external tool use, by which they can acquire spatial and geometric evidence that is difficult to infer from the MLLM alone (Wu et al., 2025a; Zhang et al., 2026c). Recent methods explore this paradigm by iteratively invoking tools within a per-question reasoning loop, e.g., object detection and segmentation for 2D perception, depth estimation and 3D reconstruction for geometric grounding (Zhang et al., 2026c; Luo et al., 2026; Yuan et al., 2026; Ropero et al., 2026). However, these methods often fail to realize the potential of tool use in 3D reasoning and exhibit preferences toward a few dominant tools, regardless of what each scene actually requires. As a result, adding tools to an MLLM does not improve spatial reasoning, and yields only marginal gains over non-agentic baselines under some scenarios.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Agentic 3D 空间推理旨在使多模态大语言模型（MLLM）agent 能够通过外部工具使用来解决室内 3D 理解任务；借此，它们可以获得仅凭 MLLM 难以推断的空间和几何证据（Wu et al., 2025a; Zhang et al., 2026c）。近期方法通过在逐问题推理循环中迭代调用工具来探索这一范式，例如，将目标检测和分割用于 2D 感知，将深度估计和 3D 重建用于几何 grounding（Zhang et al., 2026c; Luo et al., 2026; Yuan et al., 2026; Ropero et al., 2026）。然而，这些方法通常未能实现工具使用在 3D 推理中的潜力，并且无论每个场景实际需要什么，都偏向少数主导工具。因此，向 MLLM 添加工具并不能改善空间推理，在某些场景下相对非 agentic 基线仅产生边际增益。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> We attribute this limitation to the scene heterogeneity of indoor 3D reasoning, where required evidence and tool workflows vary across scenes. As shown in Fig. 1(a), the “object-to-object distance estimation” question requires depth evidence. However, existing methods often adopt a uniform tool strategy and rely on object detection and 3D reconstruction, which mainly provide relative spatial relationships rather than the depth grounding needed for absolute distance estimation. Sec. 4.3 confirms that this failure consistently occurs across diverse 3D scenes.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 我们将这一局限归因于室内 3D 推理的场景异质性：不同场景所需的证据和工具工作流不同。如图 1(a) 所示，“物体到物体距离估计”问题需要深度证据。然而，现有方法通常采用统一的工具策略，并依赖目标检测和 3D 重建；这些工具主要提供相对空间关系，而非绝对距离估计所需的深度 grounding。第 4.3 节证实，该失败会在多样的 3D 场景中持续发生。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> In this work, we propose Skill-3D, a framework that equips MLLM agents with reusable scene-aware skills. As illustrated in Fig. 1(b), given the same “object-to-object distance estimation” question, Skill-3D identifies the scene-task context, retrieves a relevant skill, and invokes suitable perception tools such as depth estimation. It learns these skills by constructing a Scene Memory and co-evolving a Skill Library on top of it.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在这项工作中，我们提出 Skill-3D，一个为 MLLM agent 配备可复用场景感知技能的框架。如图 1(b) 所示，面对同样的“物体到物体距离估计”问题，Skill-3D 识别场景—任务上下文，检索相关技能，并调用深度估计等合适的感知工具。它通过构建 Scene Memory，并在其上共同演化 Skill Library 来学习这些技能。

### Fig. 1. 动机与 Skill-3D 概览

![Fig. 1](fig1_motivation_overview.png)

**Caption:** Figure 1: Motivation and overview of Skill-3D. (a) Scene-agnostic tool calls can yield mismatched evidence and unreliable answers. (b) Skill-3D retrieves scene-aware skills to guide tool-use workflows, e.g., detection, depth, 3D reconstruction. (c) Skill-3D improves over strong MLLM baselines across diverse spatial reasoning dimensions.

**Caption[CN]:** 图 1：Skill-3D 的动机与总体概览。(a) 与场景无关的工具调用会产生不匹配的证据和不可靠答案。(b) Skill-3D 检索场景感知技能来指导工具使用流程，例如检测、深度估计和 3D 重建。(c) Skill-3D 在多种空间推理维度上优于强 MLLM 基线。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> During training, an MLLM agent identifies each question’s scene and stores the corresponding tool-use trajectory together with its outcome into the Scene Memory. On top of this memory, the Skill Library aggregates successful trajectories from similar scenes and distills them into reusable scene-aware skills, with failed ones attached to the corresponding skill as lessons. Critically, once a skill is formed, it is injected back to guide the agent on subsequent questions from similar scenes, producing new trajectories whose successes and failures are updated back to refine the same skill. Through this loop, the Scene Memory and the Skill Library co-evolve until the skills are reliable enough to serve as scene-conditioned tool-use priors at inference.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在训练期间，MLLM agent 识别每个问题的场景，并将相应工具使用轨迹及其结果写入 Scene Memory。在这一记忆之上，Skill Library 聚合相似场景的成功轨迹，并将其蒸馏为可复用的场景感知技能，失败轨迹则作为 lessons 附着到相应技能。关键是，一旦形成技能，就会将其重新注入以引导 agent 处理来自相似场景的后续问题，产生新的轨迹；其成功和失败会被回写以细化同一技能。通过该循环，Scene Memory 和 Skill Library 共同演化，直至技能足够可靠，可在推理时充当场景条件化的工具使用先验。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> This design offers two practical benefits. 1) Skills are dynamically updated: under a similar scene, the agent’s new trajectories are written back to broaden the skill’s coverage. This prevents the skill from overfitting to a narrow slice of its scene (e.g., kitchen depth-estimation vs. living room depth-estimation). 2) The Scene Memory and the Skill Library evolve together, with neither predefined upfront, allowing both to become more discriminative as the agent encounters more diverse 3D tasks.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 该设计提供两个实际优势。1）技能被动态更新：在相似场景下，agent 的新轨迹被回写，从而扩展技能覆盖范围。这避免技能对其场景的狭窄切片过拟合（例如厨房深度估计与客厅深度估计）。2）Scene Memory 与 Skill Library 共同演化，二者都不是预先定义的；随着 agent 遇到更多样的 3D 任务，它们都能变得更具判别性。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Additionally, we further introduce skill-guided agentic post-training. We first apply supervised fine-tuning on skill-guided trajectories to teach the policy the format of skill retrieval, tool invocation, and evidence accumulation. We then perform Group Relative Policy Optimization (GRPO) (DeepSeek-AI et al., 2025; Shao et al., 2024b) with a composite reward that jointly captures answer correctness, skill-guided tool-use quality, and structured output, encouraging the policy to internalize the scene-aware tool-use behavior that the skill library encodes.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 此外，我们进一步引入技能引导的 agentic 后训练。我们首先在技能引导轨迹上实施监督微调，教会策略技能检索、工具调用和证据积累的格式。随后，我们利用 Group Relative Policy Optimization（GRPO）（DeepSeek-AI et al., 2025; Shao et al., 2024b）及一个联合刻画答案正确性、技能引导工具使用质量和结构化输出的复合奖励，鼓励策略内化技能库编码的场景感知工具使用行为。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> We evaluate Skill-3D on multiple 3D spatial reasoning benchmarks. As shown in Fig. 1(c), Skill-3D consistently outperforms strong MLLM baselines across representative 3D reasoning dimensions, improving effective tool usage from 39% to 78%. It lifts Gemini-3-Flash by 67% on MMSI-Bench, while skill-guided agentic post-training further boosts Qwen3-VL-8B (QwenTeam, 2025) by 43% on VSI-Bench (Yang et al., 2025a). Our contributions are threefold:
>
> - We propose Skill-3D, which constructs a Scene Memory and co-evolves a Skill Library on top of it during training, yielding scene-aware skills that generalize across scene-internal variations.
> - We propose skill-guided agentic reinforcement learning under a composite reward, internalizing scene-aware tool-use behavior into the policy.
> - Extensive experiments across closed- and open-source MLLMs on multiple 3D spatial reasoning benchmarks validate the effectiveness of Skill-3D and its substantial improvement in tool usage.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 我们在多个 3D 空间推理基准上评估 Skill-3D。如图 1(c) 所示，Skill-3D 在代表性的 3D 推理维度上稳定超过强 MLLM 基线，将有效工具使用从 39% 提升至 78%。它使 Gemini-3-Flash 在 MMSI-Bench 上提升 67%，而技能引导的 agentic 后训练进一步使 Qwen3-VL-8B（QwenTeam, 2025）在 VSI-Bench（Yang et al., 2025a）上提升 43%。我们的贡献有三点：
>
> - 我们提出 Skill-3D：它在训练期间构建 Scene Memory 并在其上共同演化 Skill Library，产生能跨场景内部变化泛化的场景感知技能。
> - 我们在复合奖励下提出技能引导的 agentic 强化学习，将场景感知工具使用行为内化到策略中。
> - 在多个 3D 空间推理基准上、跨闭源和开源 MLLM 的广泛实验，验证了 Skill-3D 的有效性及其对工具使用的显著改善。

## 2 Related Work

### 2.1 MLLMs for Spatial Reasoning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Multimodal Large Language Models (MLLMs) have shown growing capability in spatial reasoning, driven by stronger backbones (Yang et al., 2023; Wake et al., 2024; Shao et al., 2024a; Liu et al., 2025a; Lee et al., 2025b) and dedicated benchmarks (Yang et al., 2025a; Wu et al., 2025b; Chow et al., 2025; Cai et al., 2025; Majumdar et al., 2024; Liu et al., 2026b; Zhang et al., 2026b). Recent methods improve fine-grained spatial understanding by incorporating 3D reconstruction, depth cues, spatial VQA data, and explicit grounding (Cheng et al., 2024; Chen et al., 2024; Fan et al., 2025b; Roy et al., 2025; Qi et al., 2025; Huang et al., 2024; Wang et al., 2023; Balazadeh et al., 2024; Zhang et al., 2025a; Wu et al., 2025c). Other works enhance spatial reasoning through prompting, mental simulation, visual chain-of-thought, reinforcement learning, code-driven 3D reasoning, and generative imagination of 3D space (Taguchi et al., 2025; Marsili et al., 2025; Tang et al., 2025a; Lee et al., 2025b; Fan et al., 2025a; Wang et al., 2025d,e; Chen et al., 2025c; Luo et al., 2026; Yang et al., 2025d). These capabilities have also been extended to embodied and robotic settings (Ji et al., 2025; Team et al., 2025a,b; Abdolmaleki et al., 2025; Zhou et al., 2025a, 2024; Zhao et al., 2026).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 多模态大语言模型（MLLM）在空间推理中已展现出不断增强的能力，这得益于更强的骨干网络（Yang et al., 2023; Wake et al., 2024; Shao et al., 2024a; Liu et al., 2025a; Lee et al., 2025b）和专用基准（Yang et al., 2025a; Wu et al., 2025b; Chow et al., 2025; Cai et al., 2025; Majumdar et al., 2024; Liu et al., 2026b; Zhang et al., 2026b）。近期方法通过纳入 3D 重建、深度线索、空间 VQA 数据和显式 grounding 来改进细粒度空间理解（Cheng et al., 2024; Chen et al., 2024; Fan et al., 2025b; Roy et al., 2025; Qi et al., 2025; Huang et al., 2024; Wang et al., 2023; Balazadeh et al., 2024; Zhang et al., 2025a; Wu et al., 2025c）。其他工作通过 prompting、心智模拟、视觉思维链、强化学习、代码驱动的 3D 推理和对 3D 空间的生成式想象增强空间推理（Taguchi et al., 2025; Marsili et al., 2025; Tang et al., 2025a; Lee et al., 2025b; Fan et al., 2025a; Wang et al., 2025d,e; Chen et al., 2025c; Luo et al., 2026; Yang et al., 2025d）。这些能力还已扩展到具身和机器人场景（Ji et al., 2025; Team et al., 2025a,b; Abdolmaleki et al., 2025; Zhou et al., 2025a, 2024; Zhao et al., 2026）。

### 2.2 MLLM Agents

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Tool augmentation extends MLLM by allowing them to invoke external modules through prompting, structured APIs, or code generation. Representative systems demonstrate that external tools can compensate for limitations of end-to-end multimodal models (Shen et al., 2023; Wu et al., 2023; Surís et al., 2023). Recent tool-augmented VLM agents have been developed for long-video understanding, high-resolution image analysis, medical diagnosis, and general visual reasoning (Chen et al., 2025a; Zhang et al., 2025b; Taguchi et al., 2025; Yang et al., 2025e; Zhu et al., 2025; Lee et al., 2025a; Yang et al., 2025b; Lyu et al., 2025; Liu et al., 2025b; Su et al., 2025). A complementary line of work trains VLMs to use tools through supervised fine-tuning or reinforcement learning (Liu et al., 2024a; Wang et al., 2025a; Han et al., 2025; Tang et al., 2025b; Wu et al., 2024; Lin et al., 2025b; Wu et al., 2025d; Zheng et al., 2025; Chen et al., 2025b; Dong et al., 2025; Zhou et al., 2025b). Recent 3D agentic methods further introduce reconstruction-based reasoning loops for limited-view spatial understanding (Zhang et al., 2026c), but they often rely on uniform tool-use workflows across heterogeneous scenes.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 工具增强通过允许 MLLM 经由 prompting、结构化 API 或代码生成调用外部模块来扩展 MLLM。代表性系统表明，外部工具能够弥补端到端多模态模型的局限（Shen et al., 2023; Wu et al., 2023; Surís et al., 2023）。近期开发的工具增强 VLM agent 面向长视频理解、高分辨率图像分析、医学诊断和通用视觉推理（Chen et al., 2025a; Zhang et al., 2025b; Taguchi et al., 2025; Yang et al., 2025e; Zhu et al., 2025; Lee et al., 2025a; Yang et al., 2025b; Lyu et al., 2025; Liu et al., 2025b; Su et al., 2025）。一条互补研究路线通过监督微调或强化学习训练 VLM 使用工具（Liu et al., 2024a; Wang et al., 2025a; Han et al., 2025; Tang et al., 2025b; Wu et al., 2024; Lin et al., 2025b; Wu et al., 2025d; Zheng et al., 2025; Chen et al., 2025b; Dong et al., 2025; Zhou et al., 2025b）。近期 3D agentic 方法进一步为有限视角空间理解引入基于重建的推理循环（Zhang et al., 2026c），但它们经常在异质场景中依赖统一工具使用工作流。

### 2.3 Agent Skills

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Memory-based agents store trajectories for reflection or experience replay (Zhao et al., 2024; Shinn et al., 2024), but raw trajectories are often long, redundant, and noisy (Chhikara et al., 2025; Yan et al., 2025). Recent work therefore studies skills: reusable behavioral primitives distilled from historical interactions (Xu and Yan, 2026; Li et al., 2026a; He et al., 2026; Yang et al., 2026). Skills can serve as procedural memory for decision-time guidance (Li et al., 2026b; Liu et al., 2026a; Liang et al., 2026; Jiang et al., 2026; Zhang et al., 2026a; Ye et al., 2026) and can also provide high-level priors for reinforcement learning (Xia et al., 2026; Wang et al., 2025b; Jiao et al., 2026; Ouyang et al., 2026; Fan et al., 2026). Existing skill-based agents mainly study general task automation, skill retrieval, or policy improvement. In contrast, Skill-3D studies skills for 3D spatial reasoning, where skills must encode perception-grounded tool workflows involving objects, geometry, and multi-view evidence.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 基于记忆的 agent 保存轨迹以进行反思或经验回放（Zhao et al., 2024; Shinn et al., 2024），但原始轨迹通常很长、冗余且有噪声（Chhikara et al., 2025; Yan et al., 2025）。因此，近期工作研究技能：从历史交互中蒸馏出的可复用行为原语（Xu and Yan, 2026; Li et al., 2026a; He et al., 2026; Yang et al., 2026）。技能可作为决策时指导的程序性记忆（Li et al., 2026b; Liu et al., 2026a; Liang et al., 2026; Jiang et al., 2026; Zhang et al., 2026a; Ye et al., 2026），也可为强化学习提供高层先验（Xia et al., 2026; Wang et al., 2025b; Jiao et al., 2026; Ouyang et al., 2026; Fan et al., 2026）。现有基于技能的 agent 主要研究通用任务自动化、技能检索或策略改进。相比之下，Skill-3D 研究用于 3D 空间推理的技能；此类技能必须编码涉及对象、几何和多视角证据的、以感知为 grounding 的工具工作流。

## 3 Method

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In this section, we present Skill-3D, a scene-aware skill learning framework for agentic 3D spatial reasoning. As shown in Fig. 2, Skill-3D consists of three stages. First, it records completed rollouts into Scene Memory and evolves a Skill Library from both successes and failures. The Scene Memory stores rollouts collected across benchmarks, allowing dynamic skills to be formed from heterogeneous spatial reasoning cases rather than being restricted to a single benchmark. Second, Skill-3D retrieves scene-task-relevant skills to guide inference-time tool-use planning. Third, it uses skill-guided trajectories to post-train compact agents through agentic Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本节介绍 Skill-3D——一个用于 agentic 3D 空间推理的场景感知技能学习框架。如图 2 所示，Skill-3D 包含三个阶段。首先，它将完成的 rollout 记录到 Scene Memory 中，并从成功和失败两方面演化出 Skill Library。Scene Memory 存储跨基准收集的 rollout，使动态技能可以从异质空间推理案例中形成，而非局限于单一基准。其次，Skill-3D 检索与场景—任务相关的技能，以引导推理时的工具使用规划。第三，它使用技能引导轨迹，通过 agentic Supervised Fine-Tuning（SFT）和 Reinforcement Learning（RL）对紧凑 agent 进行后训练。

### Fig. 2. Skill-3D 框架

![Fig. 2](fig2_skill3d_framework.png)

**Caption:** Figure 2: Overview of Skill-3D. (a) Skill-3D records scene-task rollouts into Scene Memory, which stores scene context, tool evidence, and failure patterns. Successful rollouts are distilled into dynamic skills, while failed rollouts are attached as lessons, enabling Scene Memory and the Skill Library to co-evolve. (b) Given a new query, Skill-3D identifies the scene-task context, retrieves relevant static and dynamic skills, and selects a compact skill set to guide tool-use workflow and evidence acquisition. (c) Skill-guided trajectories are used for agentic SFT and GRPO, encouraging compact agents to internalize skill selection, tool use, and evidence-grounded spatial reasoning.

**Caption[CN]:** 图 2：Skill-3D 概览。(a) Skill-3D 将场景—任务 rollout 记录到 Scene Memory，其中存储场景上下文、工具证据和失败模式。成功 rollout 被蒸馏为动态技能，失败 rollout 作为 lessons 附着，使 Scene Memory 与 Skill Library 共同演化。(b) 给定新查询，Skill-3D 识别场景—任务上下文，检索相关静态和动态技能，并选择紧凑技能集来引导工具使用工作流和证据获取。(c) 技能引导轨迹用于 agentic SFT 和 GRPO，鼓励紧凑 agent 内化技能选择、工具使用和以证据为 grounding 的空间推理。

### 3.1 Scene-Aware Skill Extraction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Given a spatial question $q$ and a set of visual observations $O = \{o_i\}_{i=1}^N$ from an indoor scene, an MLLM agent predicts an answer $\hat{y}$ by optionally invoking tools from tool sets $T$. The tool sets include external perception and geometry modules, e.g., object detection, segmentation, depth estimation, orientation estimation, super-resolution, and 3D reconstruction. A rollout contains the question, observations, reasoning trace, selected skills, tool calls, tool outputs, and final answer. Skill-3D updates the Skill Library after each completed rollout. Successful rollouts provide reusable tool-use patterns, while failed rollouts provide diagnostic signals for future correction.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 给定空间问题 $q$ 和来自室内场景的一组视觉观测 $O = \{o_i\}_{i=1}^N$，MLLM agent 通过可选地调用工具集合 $T$ 中的工具来预测答案 $\hat{y}$。该工具集合包括外部感知和几何模块，例如目标检测、分割、深度估计、朝向估计、超分辨率和 3D 重建。一次 rollout 包含问题、观测、推理轨迹、所选技能、工具调用、工具输出和最终答案。Skill-3D 在每次 rollout 完成后更新 Skill Library。成功 rollout 提供可复用的工具使用模式，失败 rollout 则为未来纠正提供诊断信号。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Successes as Workflows.** For each successful rollout, Skill-3D extracts a reusable tool-use routine, including its trigger condition, required evidence, tool order, key arguments, and evidence-to-answer mapping. The routine is promoted to a new dynamic skill if no compatible skill exists; otherwise, it is merged into an existing skill only when it adds useful coverage, such as a new scene condition, stronger evidence source, or lower-cost workflow. If it provides no new information, Skill-3D only updates the success statistics of the matched skill. This keeps the Skill Library compact while expanding the coverage of existing skills.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **成功即工作流。** 对每个成功 rollout，Skill-3D 提取可复用的工具使用例程，包括其触发条件、所需证据、工具顺序、关键参数以及证据到答案的映射。若不存在兼容技能，该例程被提升为新的动态技能；否则，只有当其增加有用覆盖时才与现有技能合并，例如新的场景条件、更强的证据来源或成本更低的工作流。若其不提供新信息，Skill-3D 仅更新匹配技能的成功统计。这在扩展已有技能覆盖范围的同时，使 Skill Library 保持紧凑。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Failures as Lessons.** Failed rollouts are not discarded. Skill-3D diagnoses each failure from its Scene Context and Tool Usage, with typical error types including wrong tool selection, missing evidence, invalid tool input, ignored tool output, and redundant tool calls. Evidence-supported failures are attached to the related skill as lessons. When a failure suggests a reliable correction, the corresponding dynamic skill is patched with a fallback rule. When similar failures repeatedly occur under a static skill, Skill-3D creates a failure-aware dynamic skill to handle that recurring case.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **失败即 lessons。** 失败 rollout 不会被丢弃。Skill-3D 根据其 Scene Context 和 Tool Usage 诊断每次失败，典型错误类型包括工具选择错误、证据缺失、无效工具输入、忽略工具输出和冗余工具调用。有证据支持的失败被作为 lessons 附着到相关技能。当失败提示可靠的纠正措施时，对应动态技能会以 fallback rule 修补。当相似失败在静态技能下反复发生时，Skill-3D 创建失败感知的动态技能以处理该重复案例。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Skill Maintenance.** The Skill Manager keeps the active Skill Library compact and reliable by filtering noisy rollouts and deciding whether each candidate update should be inserted, merged, patched, or rejected. An update is accepted only when it is evidence-supported and consistent with previous successful cases. Successful updates are promoted to new dynamic skills or merged into compatible ones, while failure updates are attached as lessons or converted into fallback rules. Static skills remain fixed as task-level priors, whereas dynamic skills evolve through validated merges and patches. Thus, the library stores reusable scene-aware procedures rather than raw trajectories. Please see Appendix E for detailed prompt design.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **技能维护。** Skill Manager 通过过滤噪声 rollout，并决定每个候选更新应被插入、合并、修补还是拒绝，使活跃 Skill Library 保持紧凑和可靠。只有在更新有证据支持且与先前成功案例一致时，才会接受该更新。成功更新会被提升为新的动态技能或合并到兼容技能中，失败更新则被附着为 lessons 或转换为 fallback rules。静态技能作为任务级先验保持固定，而动态技能通过已验证的合并和修补演化。因此，技能库存储的是可复用的场景感知过程，而非原始轨迹。详细提示词设计见附录 E。

### 3.2 Skill-Guided Inference

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Given a new query, Skill-3D first identifies the scene-task context, including the task category, target entities, scene signature, and required evidence. This context determines whether the agent should seek object-level evidence, boundary evidence, depth cues, orientation cues, multi-view geometry, or a combination of them.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 给定新查询，Skill-3D 首先识别场景—任务上下文，包括任务类别、目标实体、场景签名和所需证据。该上下文决定 agent 应寻求物体级证据、边界证据、深度线索、朝向线索、多视角几何，还是它们的组合。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Scene-Task Skill Retrieval.** Skill-3D performs top-$k$ retrieval over the Skill Library to obtain candidate static and dynamic skills. Each skill is indexed by its trigger condition, applicable scene context, required evidence type, and historical metadata. Given the current scene-task context, we score each skill by its semantic alignment with the query category, target entities, scene signature, and evidence requirement, e.g., whether the task requires object boundaries, depth cues, orientation evidence, or multi-view geometry. The ranking also incorporates metadata including historical success rate, attached failure lessons, and estimated tool cost. This retrieval step returns a compact set of potentially useful skills without injecting the entire Skill Library into the prompt.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **场景—任务技能检索。** Skill-3D 在 Skill Library 上执行 top-$k$ 检索，以获得候选静态和动态技能。每个技能由其触发条件、适用场景上下文、所需证据类型和历史元数据索引。给定当前场景—任务上下文，我们根据技能与查询类别、目标实体、场景签名和证据需求的语义对齐程度为其评分，例如任务是否需要对象边界、深度线索、朝向证据或多视角几何。排序还纳入历史成功率、附着的失败 lessons 和估计工具成本等元数据。此检索步骤返回紧凑的潜在有用技能集合，而不将整个 Skill Library 注入 prompt。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Skill Selection.** The candidate skills may contain redundant or overlapping workflows. Skill-3D therefore uses the policy to select a compact subset of skills for the current query. The selected skills are expected to cover the required evidence while avoiding unnecessary tool calls. The selector also generates short fallback rules, e.g., switching from detection to segmentation when closest-point boundaries are required, or using multi-view evidence when single-view localization is ambiguous.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **技能选择。** 候选技能可能包含冗余或重叠的工作流。因此，Skill-3D 使用策略为当前查询选择紧凑的技能子集。所选技能应覆盖所需证据，同时避免不必要的工具调用。选择器还会生成简短的 fallback rules，例如，当需要最近点边界时从检测切换到分割，或当单视角定位有歧义时使用多视角证据。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Tool-Use Workflow.** Conditioned on the selected skill, the agent performs iterative tool reasoning. At each step, the model decides whether to invoke a tool, incorporate returned evidence, continue reasoning, or stop and answer. Tool outputs are appended to the reasoning history and used to update the accumulated evidence. Compared with direct tool invocation, skill-guided tool-use workflow constrains both evidence acquisition and evidence usage. The agent is guided to collect the evidence required by the scene-task context and to ground the final answer in the returned tool outputs.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **工具使用工作流。** 在所选技能的条件下，agent 进行迭代式工具推理。每一步中，模型决定是否调用工具、吸收返回证据、继续推理，或停止并作答。工具输出被附加到推理历史，并用于更新累积证据。与直接工具调用相比，技能引导的工具使用工作流同时约束证据获取和证据使用。agent 被引导去收集场景—任务上下文所要求的证据，并将最终答案 grounding 在返回的工具输出上。

### 3.3 Skill-Guided Agentic Post-Training

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Skill-3D further transfers scene-aware tool-use behavior into compact MLLM agents. During agentic post-training, the Skill Library is frozen to avoid non-stationarity. Each training sample contains the question and observations, available skill candidates, the selected skill sequence, tool calls and outputs, intermediate evidence, and final answer.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Skill-3D 进一步将场景感知工具使用行为迁移到紧凑 MLLM agent。在 agentic 后训练期间，Skill Library 被冻结以避免非平稳性。每个训练样本包含问题与观测、可用技能候选、所选技能序列、工具调用及输出、中间证据和最终答案。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Agentic SFT.** We first perform SFT on skill-guided trajectories. This stage teaches the model the complete structured interaction pattern. Importantly, the SFT target is not only to imitate tool calls, but also to learn when and how to select suitable skills from the Skill Library according to the scene-task context. This provides a stable initialization so that the policy can execute skill selection, tool-use workflow, and evidence integration before RL.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **Agentic SFT。** 我们首先在技能引导轨迹上进行 SFT。该阶段教会模型完整的结构化交互模式。重要的是，SFT 目标不仅是模仿工具调用，还要学习何时以及如何依据场景—任务上下文从 Skill Library 中选择合适技能。这提供稳定初始化，使策略在 RL 之前即可执行技能选择、工具使用工作流和证据整合。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Agentic RL.** We further optimize the skill-augmented policy with Group Relative Policy Optimization (GRPO) (DeepSeek-AI et al., 2025; Shao et al., 2024b). For each scene-task query, the policy first observes the question, visual observations, and retrieved skill candidates. It then samples a group of $G$ complete trajectories $\{\tau^{(1)}, \ldots, \tau^{(G)}\}$, where each trajectory contains the model’s own skill choices, tool calls, tool outputs, reasoning steps, and final answer. Each trajectory receives a scalar reward:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **Agentic RL。** 我们进一步使用 Group Relative Policy Optimization（GRPO）（DeepSeek-AI et al., 2025; Shao et al., 2024b）优化技能增强策略。对于每个场景—任务查询，策略首先观察问题、视觉观测和检索到的技能候选。然后它采样一组 $G$ 条完整轨迹 $\{\tau^{(1)}, \ldots, \tau^{(G)}\}$，其中每条轨迹包含模型自身的技能选择、工具调用、工具输出、推理步骤和最终答案。每条轨迹获得一个标量奖励：

$$
R(\tau) = R_{\mathrm{ans}}(\tau) + R_{\mathrm{fmt}}(\tau) + R_{\mathrm{tool}}(\tau), \tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> where $R_{\mathrm{ans}}$ measures answer correctness, $R_{\mathrm{fmt}}$ measures structured-format compliance, and $R_{\mathrm{tool}}$ measures tool-use efficiency, i.e., whether the selected tools provide useful evidence with minimal redundant calls. Specifically, we define $R_{\mathrm{tool}}$ as:

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 其中，$R_{\mathrm{ans}}$ 衡量答案正确性，$R_{\mathrm{fmt}}$ 衡量结构化格式合规性，$R_{\mathrm{tool}}$ 衡量工具使用效率，即所选工具是否以最少冗余调用提供有用证据。具体地，我们将 $R_{\mathrm{tool}}$ 定义为：

$$
R_{\mathrm{tool}}(\tau) = R_{\mathrm{exec}}(\tau) - \frac{|A|}{B}, \tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> where $A$ is the set of tool calls in trajectory $\tau$, $B$ is the maximum tool budget. In practice, $R_{\mathrm{exec}}$ is a binary reward assigned to 1 only when the trajectory obtains the required evidence specified by the benchmark task type and the frozen scene-task parser. The required evidence is not determined by the model-selected skill, which prevents the policy from selecting easier skills to obtain higher tool-use reward. We provide additional objective details in Appendix C.3.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 其中，$A$ 是轨迹 $\tau$ 中工具调用的集合，$B$ 是最大工具预算。在实践中，$R_{\mathrm{exec}}$ 是一个二值奖励，仅当轨迹获得由基准任务类型和冻结的场景—任务解析器指定的所需证据时才赋值为 1。所需证据不由模型选择的技能决定，这防止策略通过选择更容易的技能来获得更高的工具使用奖励。我们在附录 C.3 中提供更多目标细节。

## 4 Experiments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The experiments evaluate Skill-3D on VSI-Bench, BLINK, CV-3D, and MMSI-Bench. VSI-Bench covers eight indoor spatial reasoning categories, including object counting, distance estimation, size estimation, route planning, and appearance order. BLINK evaluates multi-view reasoning, CV-3D evaluates depth ordering and relative distance, and MMSI-Bench evaluates positional relationship reasoning. The authors follow Think3D to randomly sample 30% of questions from each category as training data and use the remaining disjoint samples as the test set.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 实验在 VSI-Bench、BLINK、CV-3D 和 MMSI-Bench 上评估 Skill-3D。VSI-Bench 覆盖八类室内空间推理，包括目标计数、距离估计、尺寸估计、路线规划和出现顺序。BLINK 评估多视角推理，CV-3D 评估深度排序和相对距离，MMSI-Bench 评估位置关系推理。作者沿用 Think3D，从每个类别随机抽取 30% 问题作为训练集，其余问题级不重叠样本作为测试集。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For closed-source agents, the paper evaluates GPT-4o, GPT-5.4, Gemini-2.5-Pro, and Gemini-3-Flash under four settings: w/o Tools, w/ Tools, Think3D, and Skill-3D. For open-source agents, it evaluates Qwen3-VL-4B and Qwen3-VL-8B under the same settings, where Skill-3D-4B and Skill-3D-8B denote skill-guided post-trained models.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 对闭源 agent，论文评估 GPT-4o、GPT-5.4、Gemini-2.5-Pro 和 Gemini-3-Flash，并比较四种设置：w/o Tools、w/ Tools、Think3D 和 Skill-3D。对开源 agent，论文在相同设置下评估 Qwen3-VL-4B 和 Qwen3-VL-8B，其中 Skill-3D-4B 和 Skill-3D-8B 表示技能引导后训练模型。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Implementation uses external tools including Pi3, GroundingDINO, SAM3, Orient Anything v2, SwinIR, and the indoor metric-depth variant of Depth Anything 3. Qwen3-VL-4B/8B are base models, while GPT-5.4 is the teacher for skill distillation and SFT data generation. The training set contains 500 SFT samples and 1k GRPO samples. Training uses a composite reward with weights 0.6 for answer correctness, 0.2 for tool-use efficiency, and 0.2 for skill-tool format rewards, on 4 NVIDIA RTX PRO 6000 Blackwell GPUs.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 实现使用 Pi3、GroundingDINO、SAM3、Orient Anything v2、SwinIR，以及 Depth Anything 3 的室内 metric-depth 版本等外部工具。Qwen3-VL-4B/8B 作为基础模型，GPT-5.4 作为技能蒸馏和 SFT 数据生成的 teacher。训练集包含 500 个 SFT 样本和 1k 个 GRPO 样本。训练在 4 块 NVIDIA RTX PRO 6000 Blackwell GPU 上进行，复合奖励权重为答案正确性 0.6、工具使用效率 0.2、技能-工具格式奖励 0.2。

### Table 1. 闭源模型主结果

![Table 1](table1_closed_source_results.png)

**Caption:** Table 1: Comprehensive evaluation on VSI-Bench, BLINK, CV-3D, and MMSI-Bench. Representative spatial reasoning metrics are reported across multiple benchmarks. MV denotes multi-view. PR denotes positional relationship. Higher values indicate better performance, and all metrics are obtained on the test set.

**Caption[CN]:** 表 1：在 VSI-Bench、BLINK、CV-3D 与 MMSI-Bench 上的综合评测。表中报告多个基准上的代表性空间推理指标；MV 表示 multi-view，PR 表示 positional relationship。数值越高越好，所有指标均来自测试集。

| Model | Method | VSI Obj. Cnt. | VSI Abs. Dist. | VSI Obj. Size | VSI Room Size | VSI Rel. Dist. | VSI Rel. Dir. | VSI Route Plan | VSI Appr. Order | BLINK MV | CV-3D Depth Order | CV-3D Rel. Dist. | MMSI PR |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| GPT-4o | w/o Tools | 38.1 | 7.9 | 29.6 | 37.4 | 36.5 | 35.6 | 26.3 | 28.2 | 47.9 | 72.6 | 70.9 | 28.7 |
| GPT-4o | w/ Tools | 48.7 | 12.1 | 47.0 | 40.9 | 41.6 | 44.0 | 34.3 | 29.7 | 60.8 | 86.6 | 84.9 | 34.6 |
| GPT-4o | Think3D | 50.4 | 32.7 | 50.5 | 61.4 | 47.9 | 52.6 | 55.9 | 29.2 | 62.7 | 88.3 | 86.1 | 38.4 |
| GPT-4o | Skill-3D | 56.8 | 42.6 | 58.1 | 69.5 | 53.4 | 59.2 | 62.7 | 35.4 | 72.4 | 92.0 | 90.5 | 43.2 |
| GPT-5.4 | w/o Tools | 55.8 | 43.6 | 67.3 | 55.7 | 48.4 | 50.5 | 49.1 | 73.2 | 73.4 | 91.6 | 89.8 | 42.7 |
| GPT-5.4 | w/ Tools | 58.0 | 47.8 | 69.3 | 58.2 | 51.7 | 53.3 | 52.5 | 74.6 | 75.1 | 92.5 | 90.1 | 48.1 |
| GPT-5.4 | Think3D | 61.1 | 55.0 | 70.8 | 69.9 | 58.3 | 61.8 | 66.5 | 73.8 | 78.3 | 93.0 | 91.7 | 53.4 |
| GPT-5.4 | Skill-3D | 66.2 | 61.5 | 74.9 | 77.6 | 62.7 | 67.0 | 71.4 | 78.1 | 82.0 | 96.9 | 93.7 | 60.4 |
| Gemini-2.5-Pro | w/o Tools | 45.9 | 37.6 | 62.2 | 42.8 | 60.5 | 45.9 | 42.7 | 70.4 | 70.6 | 90.7 | 90.3 | 36.9 |
| Gemini-2.5-Pro | w/ Tools | 48.4 | 41.5 | 66.0 | 46.3 | 62.6 | 51.2 | 49.5 | 72.7 | 72.3 | 91.4 | 91.2 | 44.3 |
| Gemini-2.5-Pro | Think3D | 58.2 | 53.1 | 69.5 | 66.4 | 64.8 | 59.5 | 65.8 | 72.2 | 76.0 | 92.7 | 91.6 | 51.0 |
| Gemini-2.5-Pro | Skill-3D | 62.4 | 58.0 | 73.1 | 72.8 | 67.6 | 64.2 | 69.0 | 76.4 | 79.2 | 94.0 | 92.8 | 56.7 |
| Gemini-3-Flash | w/o Tools | 45.3 | 9.2 | 45.7 | 39.8 | 38.7 | 42.2 | 33.8 | 31.3 | 59.1 | 84.6 | 82.8 | 32.7 |
| Gemini-3-Flash | w/ Tools | 48.2 | 13.7 | 48.8 | 42.1 | 42.3 | 44.2 | 36.4 | 32.8 | 61.3 | 86.2 | 83.7 | 36.8 |
| Gemini-3-Flash | Think3D | 56.8 | 52.3 | 68.0 | 66.3 | 56.5 | 60.8 | 64.2 | 69.3 | 75.2 | 91.8 | 91.0 | 49.2 |
| Gemini-3-Flash | Skill-3D | 60.9 | 56.1 | 71.2 | 71.8 | 60.4 | 63.0 | 67.5 | 73.4 | 77.6 | 93.2 | 92.1 | 54.8 |


> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> For closed-source agents, Skill-3D consistently outperforms non-agentic, direct tool-use, and Think3D baselines across all four backbones. Because Skill-3D uses a single shared Skill Library built from heterogeneous spatial reasoning benchmarks, reusable skills learned from one benchmark can transfer to others when similar scene-task contexts occur. Averaged over four closed-source agents, the VSI-Bench average improves from 42.9 to 64.5, a 50.3% relative gain over the w/o Tools baseline.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 对闭源 agent，Skill-3D 在四个 backbone 上都稳定超过非 agentic、直接工具使用和 Think3D 基线。由于 Skill-3D 使用由异质空间推理基准构建的单一共享 Skill Library，当其他基准出现相似场景-任务上下文时，一个基准学到的可复用技能可以迁移过去。四个闭源 agent 平均来看，VSI-Bench 平均分从 42.9 提升到 64.5，相对 w/o Tools 基线提升 50.3%。

### Table 2. 开源模型主结果

![Table 2](table2_open_source_results.png)

**Caption:** Table 2: Open-source evaluation on VSI-Bench, BLINK, CV-3D, and MMSI-Bench. Representative spatial reasoning metrics are reported across multiple benchmarks. MV denotes multi-view. PR denotes positional relationship. Higher values indicate better performance, and all metrics are obtained on the test set.

**Caption[CN]:** 表 2：开源模型在 VSI-Bench、BLINK、CV-3D 与 MMSI-Bench 上的评测。表中报告多个空间推理指标；MV 表示 multi-view，PR 表示 positional relationship。数值越高越好，所有指标均来自测试集。

| Model | Method | VSI Obj. Cnt. | VSI Abs. Dist. | VSI Obj. Size | VSI Room Size | VSI Rel. Dist. | VSI Rel. Dir. | VSI Route Plan | VSI Appr. Order | BLINK MV | CV-3D Depth Order | CV-3D Rel. Dist. | MMSI PR |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Qwen3-VL-4B | w/o Tools | 26.6 | 19.1 | 22.8 | 35.2 | 34.8 | 35.0 | 29.4 | 40.1 | 35.6 | 59.7 | 58.6 | 26.3 |
| Qwen3-VL-4B | w/ Tools | 38.4 | 23.7 | 41.2 | 39.3 | 37.6 | 42.8 | 36.5 | 45.3 | 48.5 | 73.9 | 72.3 | 31.4 |
| Qwen3-VL-4B | Think3D-4B | 41.5 | 29.4 | 44.2 | 48.7 | 29.6 | 44.1 | 30.8 | 52.2 | 48.7 | 75.3 | 73.4 | 33.8 |
| Qwen3-VL-4B | Skill-3D-4B | 48.6 | 36.8 | 50.2 | 57.4 | 43.5 | 50.4 | 48.8 | 56.7 | 60.8 | 79.0 | 77.2 | 38.2 |
| Qwen3-VL-8B | w/o Tools | 32.5 | 24.3 | 30.8 | 41.6 | 40.2 | 41.6 | 35.5 | 47.3 | 43.8 | 68.8 | 66.5 | 31.0 |
| Qwen3-VL-8B | w/ Tools | 44.7 | 27.8 | 48.1 | 46.0 | 44.7 | 48.4 | 43.2 | 52.6 | 57.4 | 82.9 | 80.7 | 36.6 |
| Qwen3-VL-8B | Think3D-8B | 48.3 | 38.5 | 51.2 | 58.1 | 41.6 | 52.9 | 45.4 | 60.8 | 61.7 | 85.0 | 83.3 | 41.2 |
| Qwen3-VL-8B | Skill-3D-8B | 56.5 | 48.6 | 59.8 | 67.9 | 52.0 | 60.1 | 58.4 | 66.8 | 68.5 | 89.6 | 87.4 | 42.8 |


> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> For open-source agents, Skill-3D transfers effectively to compact models. On VSI-Bench, Skill-3D-4B achieves a 59.7% relative gain over the w/o Tools baseline, and Skill-3D-8B achieves a 60.3% relative gain. The stronger 8B results suggest that larger base models exploit retrieved skills and tool evidence better, while the consistent 4B gains show that smaller agents can still learn scene-aware skills through post-training.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 对开源 agent，Skill-3D 能有效迁移到小型模型。在 VSI-Bench 上，Skill-3D-4B 相对 w/o Tools 基线提升 59.7%，Skill-3D-8B 提升 60.3%。更强的 8B 结果说明更大基础模型能更好利用检索技能和工具证据，而稳定的 4B 提升说明较小 agent 也能通过后训练学习场景感知技能。

### Fig. 3. 有效工具使用率分析

![Fig. 3](fig3_effective_tool_usage.png)

**Caption:** Figure 3: Effective tool usage analysis. The figure reports the percentage of tool calls that contribute valid, relevant evidence to the final answer across VSI-Bench, BLINK, CV-3D, and MMSI-Bench.

**Caption[CN]:** 图 3：有效工具使用率分析。该图报告在 VSI-Bench、BLINK、CV-3D 和 MMSI-Bench 上，真正为最终答案提供有效且相关证据的工具调用比例。


> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The ablation first examines effective tool usage, defined as the fraction of tool calls that return valid evidence and are actually used by the agent. A tool output is counted as used when it is referenced later, passed to downstream tools, or supports the final answer. ETU is computed after the full rollout, so both execution validity and downstream usage are assessed.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 消融实验首先考察 effective tool usage，即返回有效证据并被 agent 实际使用的工具调用比例。当工具输出在后续推理中被引用、传给下游工具，或用于支撑最终答案时，才算被使用。ETU 在完整 rollout 结束后计算，因此同时评估工具执行有效性和下游证据使用。

$$
ETU = (1 / |A|) Σa∈A I[Valid(a) ∧ Used(a)]
$$

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Skill-3D substantially improves ETU over direct Tool-Use: from 39.2% to 78.7% on VSI-Bench, 36.4% to 79.2% on BLINK, 31.8% to 87.5% on CV-3D, and 30.5% to 80.3% on MMSI-Bench. Since ETU is normalized by the total number of tool calls, the gains indicate that Skill-3D does not simply invoke more tools; it selects evidence-producing tools and integrates the returned evidence.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 相比直接 Tool-Use，Skill-3D 显著提升 ETU：VSI-Bench 从 39.2% 到 78.7%，BLINK 从 36.4% 到 79.2%，CV-3D 从 31.8% 到 87.5%，MMSI-Bench 从 30.5% 到 80.3%。由于 ETU 按总工具调用次数归一化，这些提升表明 Skill-3D 并非只是调用更多工具，而是选择能产生证据的工具，并整合返回证据。

### Fig. 4. 工具使用分布

![Fig. 4](fig4_tool_distribution.png)

**Caption:** Figure 4: Tool usage distribution analysis. The figure illustrates the tool usage distributions of GPT-5.4, Think3D, and Skill-3D across two different kinds of problems on VSI-Bench.

**Caption[CN]:** 图 4：工具使用分布分析。该图展示 GPT-5.4、Think3D 和 Skill-3D 在 VSI-Bench 两类问题上的工具调用分布。


> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Tool usage distribution shows that GPT-5.4 and Think3D have clear tool-selection biases: Think3D heavily relies on Pi3 for depth-, distance-, and size-related tasks, while GPT-5.4 mostly calls GroundingDINO. Skill-3D shifts tool distribution toward the evidence needed by the task: Depth Anything 3 for depth, distance, and size, and Orient Anything v2 for spatial relation and direction reasoning, while still using Pi3, GroundingDINO, and SAM3 for layout, localization, and boundary verification.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 工具使用分布显示，GPT-5.4 和 Think3D 都有明显工具选择偏置：Think3D 在深度、距离和尺寸相关任务中过度依赖 Pi3，而 GPT-5.4 主要调用 GroundingDINO。Skill-3D 会把工具分布转向任务所需证据：对深度、距离和尺寸使用 Depth Anything 3，对空间关系和方向推理使用 Orient Anything v2，同时仍适度使用 Pi3、GroundingDINO 和 SAM3 进行布局、定位和边界验证。

### Table 3. 模块消融

![Table 3](table3_ablation.png)

**Caption:** Table 3: Module ablation of Skill-3D on VSI-Bench. Delta Avg. denotes the performance drop compared with the full Skill-3D pipeline. All experiments are conducted using GPT-5.4, and all metrics are obtained on the test set.

**Caption[CN]:** 表 3：Skill-3D 在 VSI-Bench 上的模块消融。Delta Avg. 表示相对完整 Skill-3D 流程的平均性能下降。所有实验使用 GPT-5.4，所有指标均来自测试集。

| Setting | Obj. Cnt. | Abs. Dist. | Obj. Size | Room Size | Avg. | Δ Avg. |
|---|---:|---:|---:|---:|---:|---:|
| Ours - Full Pipeline | 66.2 | 61.5 | 74.9 | 77.6 | 69.9 | – |
| w/o Failure Lessons | 65.0 | 59.4 | 72.9 | 75.9 | 68.1 | -1.8 |
| w/o Dynamic Skills | 64.1 | 59.2 | 72.7 | 75.8 | 67.8 | -2.1 |
| w/o Static Skills | 62.8 | 56.8 | 70.9 | 74.2 | 65.6 | -4.3 |
| w/o MLLM Skill Selection | 62.5 | 56.4 | 70.2 | 73.5 | 65.5 | -4.4 |
| w/o Skill Retrieval | 60.8 | 54.9 | 68.7 | 72.1 | 64.1 | -5.8 |


> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Module ablations show complementary roles for static skills, dynamic workflows, and failure lessons. Removing failure lessons reduces the average score from 69.9 to 68.1; removing dynamic skills reduces it to 67.8; removing static skills drops it to 65.6. Thus static skills provide general task-level priors, dynamic skills adapt them to scene-specific contexts, and failure lessons help avoid recurring error modes.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 模块消融显示 static skills、dynamic workflows 和 failure lessons 作用互补。去掉 failure lessons 平均分从 69.9 降到 68.1；去掉 dynamic skills 降到 67.8；去掉 static skills 降到 65.6。因此，static skills 提供通用任务级先验，dynamic skills 将其适配到特定场景上下文，failure lessons 则帮助避免重复出现的错误模式。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> Retrieval and selection are also complementary. Removing MLLM skill selection lowers the average score from 69.9 to 65.5, suggesting that top-k retrieval alone can include redundant or partially matched skills. Removing skill retrieval further drops the score to 64.1, showing that scene-task-relevant skills are crucial for effective tool planning.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 检索与选择同样互补。去掉 MLLM skill selection 后，平均分从 69.9 降到 65.5，说明仅靠 top-k 检索可能引入冗余或部分匹配技能。去掉 skill retrieval 后进一步降到 64.1，说明与场景-任务相关的技能对有效工具规划至关重要。

### Fig. 5. 技能更新与冷启动

![Fig. 5](fig5_skill_updating_cold_start.png)

**Caption:** Figure 5: Effect of skill updating and cold start during GRPO training. Experiments are conducted using Qwen3-VL-8B as the base model.

**Caption[CN]:** 图 5：GRPO 训练期间技能更新与冷启动的影响。实验以 Qwen3-VL-8B 为基础模型。


> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> For GRPO training, the paper compares Offline, Online, and Offline without cold start. Offline freezes the dynamic Skill Library during GRPO; Online updates dynamic skills during training; Offline without cold start removes the agentic SFT warm-up and directly applies GRPO. The offline variant with SFT cold start achieves the most stable and highest reward trajectory, while online updating introduces non-stationarity and removing cold start leads to early degradation and slower convergence.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> 对于 GRPO 训练，论文比较 Offline、Online 和 Offline without cold start。Offline 在 GRPO 期间冻结 dynamic Skill Library；Online 在训练中更新 dynamic skills；Offline without cold start 去掉 agentic SFT warm-up，直接做 GRPO。带 SFT cold start 的 offline 变体得到最稳定且最高的奖励曲线；在线更新会引入非平稳性，去掉 cold start 会导致早期退化和收敛更慢。

## 5 Conclusion and Limitations

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper presents Skill-3D as a framework for agentic 3D spatial reasoning with reusable scene-aware skills. Existing tool-augmented MLLM agents often apply uniform tool-use strategies across heterogeneous 3D scenes, leading to biased tool preferences and insufficient evidence acquisition. Skill-3D constructs a Scene Memory of tool-use trajectories and evolves a Skill Library where successful trajectories are distilled into reusable skills and failed trajectories are retained as lessons. Retrieved skills guide tool planning, evidence collection, and answer grounding, and skill-guided post-training transfers this behavior into compact agents.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文提出 Skill-3D：一个使用可复用场景感知技能进行 agentic 3D 空间推理的框架。现有工具增强 MLLM agent 往往在异质 3D 场景中采用统一工具策略，导致工具偏置和证据获取不足。Skill-3D 构建工具使用轨迹的 Scene Memory，并演化 Skill Library：成功轨迹被蒸馏为可复用技能，失败轨迹被保留为 lessons。检索到的技能指导工具规划、证据收集和答案 grounding，而技能引导后训练把这种行为迁移到小型 agent 中。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The limitation is that the current evaluation focuses on indoor 3D spatial reasoning. Transferring the framework to outdoor scenes, embodied navigation, or real-time robotic interaction may require new tool interfaces, scene signatures, and safety constraints.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 局限性在于当前评测集中在室内 3D 空间推理。若要迁移到室外场景、具身导航或实时机器人交互，可能需要新的工具接口、场景签名和安全约束。

## References

Bibliographic metadata is retained in its original language.

1. Abbas Abdolmaleki, Saminda Abeyruwan, Joshua Ainslie, Jean-Baptiste Alayrac, Montserrat Gonzalez Arenas, Ashwin Balakrishna, Nathan Batchelor, Alex Bewley, Jeff Bingham, Michael Bloesch, and 1 others. 2025. Gemini robotics 1.5: Pushing the frontier of generalist robots with advanced embodied reasoning, thinking, and motion transfer. arXiv preprint arXiv:2510.03342.
2. Vahid Balazadeh, Mohammadmehdi Ataei, Hyunmin Cheong, Amir Hosein Khasahmadi, and Rahul G Krishnan. 2024. Synthetic vision: Training vision-language models to understand physics. arXiv e-prints, pages arXiv–2412.
3. Wenxiao Cai, Iaroslav Ponomarenko, Jianhao Yuan, Xiaoqi Li, Wankou Yang, Hao Dong, and Bo Zhao. 2025. Spatialbot: Precise spatial understanding with vision language models. In 2025 IEEE International Conference on Robotics and Automation (ICRA), pages 9490–9498. IEEE.
4. Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath, Ronghang Hu, Didac Suris, Chaithanya Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew Huang, and 1 others. 2025. Sam 3: Segment anything with concepts. arXiv preprint arXiv:2511.16719.
5. Boyu Chen, Zhengrong Yue, Siran Chen, Zikang Wang, Yang Liu, Peng Li, and Yali Wang. 2025a. Lvagent: Long video understanding by multi-round dynamical collaboration of mllm agents. arXiv preprint arXiv:2503.10200.
6. Boyuan Chen, Zhuo Xu, Sean Kirmani, Brain Ichter, Dorsa Sadigh, Leonidas Guibas, and Fei Xia. 2024. Spatialvlm: Endowing vision-language models with spatial reasoning capabilities. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 14455–14465.
7. Yang Chen, Yufan Shen, Wenxuan Huang, Sheng Zhou, Qunshu Lin, Xinyu Cai, Zhi Yu, Jiajun Bu, Botian Shi, and Yu Qiao. 2025b. Learning only with images: Visual reinforcement learning with reasoning, rendering, and visual feedback. arXiv preprint arXiv:2507.20766.
8. Zeren Chen, Xiaoya Lu, Zhijie Zheng, Pengrui Li, Lehan He, Yijin Zhou, Jing Shao, Bohan Zhuang, and Lu Sheng. 2025c. Geometrically-constrained agent for spatial reasoning. arXiv preprint arXiv:2511.22659.
9. An-Chieh Cheng, Hongxu Yin, Yang Fu, Qiushan Guo, Ruihan Yang, Jan Kautz, Xiaolong Wang, and Sifei Liu. 2024. Spatialrgpt: Grounded spatial reasoning in vision-language models. Advances in Neural Information Processing Systems, 37:135062–135093.
10. Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, and Deshraj Yadav. 2025. Mem0: Building production-ready ai agents with scalable long-term memory. arXiv preprint arXiv:2504.19413.
11. Wei Chow, Jiageng Mao, Boyi Li, Daniel Seita, Vitor Guizilini, and Yue Wang. 2025. Physbench: Benchmarking and enhancing vision-language models for physical world understanding. arXiv preprint arXiv:2501.16411.
12. Gheorghe Comanici, Eric Bieber, Mike Schaekermann, Ice Pasupat, Noveen Sachdeva, Inderjit Dhillon, Marcel Blistein, Ori Ram, Dan Zhang, Evan Rosen, and 1 others. 2025. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. arXiv preprint arXiv:2507.06261.
13. DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Jun-Mei Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiaoling Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, and 179 others. 2025. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. ArXiv, abs/2501.12948.
14. Guanting Dong, Hangyu Mao, Kai Ma, Licheng Bao, Yifei Chen, Zhongyuan Wang, Zhongxia Chen, Jiazhen Du, Huiyang Wang, Fuzheng Zhang, and 1 others. 2025. Agentic reinforced policy optimization. arXiv preprint arXiv:2507.19849.
15. Kaixuan Fan, Kaituo Feng, Manyuan Zhang, Tianshuo Peng, Zhixun Li, Yilei Jiang, Shuang Chen, Peng Pei, Xunliang Cai, and Xiangyu Yue. 2026. Exploring reasoning reward model for agents. arXiv preprint arXiv:2601.22154.
16. Yue Fan, Xuehai He, Diji Yang, Kaizhi Zheng, Ching-Chen Kuo, Yuting Zheng, Sravana Jyothi Narayanaraju, Xinze Guan, and Xin Eric Wang. 2025a. Grit: Teaching mllms to think with images. arXiv preprint arXiv:2505.15879.
17. Zhiwen Fan, Jian Zhang, Renjie Li, Junge Zhang, Runjin Chen, Hezhen Hu, Kevin Wang, Huaizhi Qu, Dilin Wang, Zhicheng Yan, and 1 others. 2025b. Vlm-3r: Vision-language models augmented with instruction-aligned 3d reconstruction. arXiv preprint arXiv:2505.20279.
18. Xingyu Fu, Yushi Hu, Bangzheng Li, Yu Feng, Haoyu Wang, Xudong Lin, Dan Roth, Noah A Smith, Wei-Chiu Ma, and Ranjay Krishna. 2024. Blink: Multimodal large language models can see but not perceive. In European Conference on Computer Vision, pages 148–166. Springer.
19. Google. 2025. A new era of intelligence with gemini 3.
20. Yi Han, Cheng Chi, Enshen Zhou, Shanyu Rong, Jingkun An, Pengwei Wang, Zhongyuan Wang, Lu Sheng, and Shanghang Zhang. 2025. Tiger: Tool-integrated geometric reasoning in vision-language models for robotics. arXiv preprint arXiv:2510.07181.
21. Chaoyue He, Xin Zhou, Di Wang, Hong Xu, Wei Liu, and Chunyan Miao. 2026. Openclaw as language infrastructure: A case-centered survey of a public agent ecosystem in the wild.
22. Haifeng Huang, Yilun Chen, Zehan Wang, Rongjie Huang, Runsen Xu, Tai Wang, Luping Liu, Xize Cheng, Yang Zhao, Jiangmiao Pang, and 1 others. 2024. Chat-scene: Bridging 3d scene and large language models with object identifiers. In The Thirty-eighth Annual Conference on Neural Information Processing Systems.
23. Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, and 1 others. 2024. Gpt-4o system card. arXiv preprint arXiv:2410.21276.
24. Yuheng Ji, Huajie Tan, Jiayu Shi, Xiaoshuai Hao, Yuan Zhang, Hengyuan Zhang, Pengwei Wang, Mengdi Zhao, Yao Mu, Pengju An, and 1 others. 2025. Robobrain: A unified brain model for robotic manipulation from abstract to concrete. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 1724–1734.
25. Guanyu Jiang, Zhaochen Su, Xiaoye Qu, and Yi R Fung. 2026. Xskill: Continual learning from experience and skills in multimodal agents. arXiv preprint arXiv:2603.12056.
26. Zhengbo Jiao, Shaobo Wang, Zifan Zhang, Xuan Ren, Wei Wang, Bing Zhao, Hu Wei, and Linfeng Zhang. 2026. Agentic proposing: Enhancing large language model reasoning via compositional skill synthesis. arXiv preprint arXiv:2602.03279.
27. Jaeseong Lee, Yeeun Choi, Heechan Choi, Hanjung Kim, and Seonjoo Kim. 2025a. A training-free, task-agnostic framework for enhancing mllm performance on high-resolution images. arXiv preprint arXiv:2507.10202.
28. Phillip Y Lee, Jihyeon Je, Chanho Park, Mikaela Angelina Uy, Leonidas Guibas, and Minhyuk Sung. 2025b. Perspective-aware reasoning in vision-language models via mental imagery simulation. arXiv preprint arXiv:2504.17207.
29. Hao Li, Chunjiang Mu, Jianhao Chen, Siyue Ren, Zhiyao Cui, Yiqun Zhang, Lei Bai, and Shuyue Hu. 2026a. Organizing, orchestrating, and benchmarking agent skills at ecosystem scale. arXiv preprint arXiv:2603.02176.
30. Xiangyi Li, Wenbo Chen, Yimin Liu, Shenghan Zheng, Xiaokun Chen, Yifeng He, Yubo Li, Bingran You, Haotian Shen, Jiankai Sun, and 1 others. 2026b. Skillsbench: Benchmarking how well agent skills work across diverse tasks. arXiv preprint arXiv:2602.12670.
31. Jingyun Liang, Jiezhang Cao, Guolei Sun, Kai Zhang, Luc Van Gool, and Radu Timofte. 2021. Swinir: Image restoration using swin transformer. In Proceedings of the IEEE/CVF international conference on computer vision, pages 1833–1844.
32. Yuan Liang, Ruobin Zhong, Haoming Xu, Chen Jiang, Yi Zhong, Runnan Fang, Jia-Chen Gu, Shumin Deng, Yunzhi Yao, Mengru Wang, and 1 others. 2026. Skillnet: Create, evaluate, and connect ai skills. arXiv preprint arXiv:2603.04448.
33. Haotong Lin, Sili Chen, Junhao Liew, Donny Y Chen, Zhenyu Li, Guang Shi, Jiashi Feng, and Bingyi Kang. 2025a. Depth anything 3: Recovering the visual space from any views. arXiv preprint arXiv:2511.10647.
34. Yuanze Lin, Yunsheng Li, Dongdong Chen, Weijian Xu, Ronald Clark, and Philip Torr. 2025b. Olympus: A universal task router for computer vision tasks. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 14235–14246.
35. Benlin Liu, Yuhao Dong, Yiqin Wang, Zixian Ma, Yansong Tang, Luming Tang, Yongming Rao, Wei-Chiu Ma, and Ranjay Krishna. 2025a. Coarse correspondences boost spatial-temporal reasoning in multimodal language model. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 3783–3792.
36. Chang Liu, Sibo Tian, Xiao Liang, and Minghui Zheng. 2026a. Self-vla: A skill enhanced agentic vision-language-action framework for contact-rich disassembly. arXiv preprint arXiv:2603.11080.
37. Jiale Liu, Huan Wang, Yue Zhang, Xiaoyu Luo, Jiaxiang Hu, Zhiliang Liu, and Min Xie. 2025b. Insightx agent: An lmm-based agentic framework with integrated tools for reliable x-ray ndt analysis. arXiv preprint arXiv:2507.14899.
38. Jianhui Liu, Haoze Sun, Wenbo Li, Yanbing Zhang, Rui Yang, Zhiliang Zhu, Yijun Yang, Shenghe Zheng, Nan Jiang, Jiaxiu Jiang, and 1 others. 2026b. Openspatial: A principled data engine for empowering spatial intelligence. arXiv preprint arXiv:2604.07296.
39. Shilong Liu, Hao Cheng, Haotian Liu, Hao Zhang, Feng Li, Tianhe Ren, Xueyan Zou, Jianwei Yang, Hang Su, Jun Zhu, and 1 others. 2024a. Llava-plus: Learning to use tools for creating multimodal agents. In European conference on computer vision, pages 126–142. Springer.
40. Shilong Liu, Zhaoyang Zeng, Tianhe Ren, Feng Li, Hao Zhang, Jie Yang, Qing Jiang, Chunyuan Li, Jianwei Yang, Hang Su, and 1 others. 2024b. Grounding dino: Marrying dino with grounded pre-training for open-set object detection. In European conference on computer vision, pages 38–55. Springer.
41. Zhanpeng Luo, Ce Zhang, Silong Yong, Cunxi Dai, Qianwei Wang, Haoxi Ran, Guanya Shi, Katia Sycara, and Yaqi Xie. 2026. pyspatial: Generating 3d visual programs for zero-shot spatial reasoning. In The Fourteenth International Conference on Learning Representations.
42. Xinheng Lyu, Yuci Liang, Wenting Chen, Meidan Ding, Jiaqi Yang, Guolin Huang, Daokun Zhang, Xiangjian He, and Linlin Shen. 2025. Wsi-agents: A collaborative multi-agent system for multi-modal whole slide image analysis. arXiv preprint arXiv:2507.14680.
43. Arjun Majumdar, Anurag Ajay, Xiaohan Zhang, Pranav Putta, Sriram Yenamandra, Mikael Henaff, Sneha Silwal, Paul Mcvay, Oleksandr Maksymets, Sergio Arnaud, and 1 others. 2024. Openeqa: Embodied question answering in the era of foundation models. In Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages 16488–16498.
44. Damiano Marsili, Rohun Agrawal, Yisong Yue, and Georgia Gkioxari. 2025. Visual agentic ai for spatial reasoning with a dynamic api. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 19446–19455.
45. OpenAI. 2025. Introducing gpt-5.4.
46. Siru Ouyang, Jun Yan, Yanfei Chen, Rujun Han, Zifeng Wang, Bhavana Dalvi Mishra, Rui Meng, Chun-Liang Li, Yizhu Jiao, Kaiwen Zha, and 1 others. 2026. Skillos: Learning skill curation for self-evolving agents. arXiv preprint arXiv:2605.06614.
47. Zhangyang Qi, Zhixiong Zhang, Ye Fang, Jiaqi Wang, and Hengshuang Zhao. 2025. Gpt4scene: Understand 3d scenes from videos with vision-language models. arXiv:2501.01428.
48. QwenTeam. 2025. Qwen3-vl: Sharper vision, deeper thought, broader action. https://qwen.ai/blog?id=99f0335c4ad9ff6153e517418d48535ab6d8afef&from=research.latest-advancements-list.
49. Fernando Ropero, Erkin Turkoz, Daniel Matos, Junqing Du, Antonio Ruiz, Yanfeng Zhang, Lu Liu, Mingwei Sun, and Yongliang Wang. 2026. Riemind: Geometry-grounded spatial agent for scene understanding. arXiv preprint arXiv:2603.15386.
50. Rajarshi Roy, Devleena Das, Ankesh Banerjee, Arjya Bhattacharjee, Kousik Dasgupta, and Subarna Tripathi. 2025. Bydeway: Boost your multimodal llm with depth prompting in a training-free way. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 6058–6064.
51. Hao Shao, Shengju Qian, Han Xiao, Guanglu Song, Zhuofan Zong, Letian Wang, Yu Liu, and Hongsheng Li. 2024a. Visual cot: Advancing multimodal language models with a comprehensive dataset and benchmark for chain-of-thought reasoning. Advances in Neural Information Processing Systems, 37:8612–8642.
52. Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, YK Li, Yang Wu, and 1 others. 2024b. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300.
53. Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, and Yueting Zhuang. 2023. Hugging-gpt: Solving ai tasks with chatgpt and its friends in hugging face. Advances in Neural Information Processing Systems, 36:38154–38180.
54. Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. 2024. Reflexion: Language agents with verbal reinforcement learning, 2023. URL https://arxiv.org/abs/2303.11366, 8.
55. Zhaochen Su, Linjie Li, Mingyang Song, Yunzhuo Hao, Zhengyuan Yang, Jun Zhang, Guanjie Chen, Jiawei Gu, Juntao Li, Xiaoye Qu, and 1 others. 2025. Openthinkimg: Learning to think with images via visual tool reinforcement learning. arXiv preprint arXiv:2505.08617.
56. Dídac Surís, Sachit Menon, and Carl Vondrick. 2023. Vipergpt: Visual inference via python execution for reasoning. In Proceedings of the IEEE/CVF international conference on computer vision, pages 11888–11898.
57. Shun Taguchi, Hideki Deguchi, Takumi Hamazaki, and Hiroyuki Sakai. 2025. Spatialprompting: Keyframe-driven zero-shot spatial reasoning with off-the-shelf multimodal large language models. arXiv preprint arXiv:2505.04911.
58. Haoran Tang, Meng Cao, Ruyang Liu, Xiaoxi Liang, Linglong Li, Ge Li, and Xiaodan Liang. 2025a. Video spatial reasoning with object-centric 3d rollout. arXiv preprint arXiv:2511.13190.
59. Zitian Tang, Shijie Wang, Junho Cho, Jaewook Yoo, and Chen Sun. 2025b. How can objects help video-language understanding? arXiv preprint arXiv:2504.07454.
60. BAAI RoboBrain Team, Mingyu Cao, Huajie Tan, Yuheng Ji, Xiansheng Chen, Minglan Lin, Zhiyu Li, Zhou Cao, Pengwei Wang, Enshen Zhou, and 1 others. 2025a. Robobrain 2.0 technical report. arXiv preprint arXiv:2507.02029.
61. Gemini Robotics Team, Saminda Abeyruwan, Joshua Ainslie, Jean-Baptiste Alayrac, Montserrat Gonzalez Arenas, Travis Armstrong, Ashwin Balakrishna, Robert Baruch, Maria Bauza, Michiel Blokzijl, and 1 others. 2025b. Gemini robotics: Bringing ai into the physical world. arXiv preprint arXiv:2503.20020.
62. Shengbang Tong, Ellis Brown, Penghao Wu, Sanghyun Woo, Manoj Middepogu, Sai C Akula, Jihan Yang, Shusheng Yang, Adithya Iyer, Xichen Pan, and 1 others. 2024. Cambrian-1: A fully open, vision-centric exploration of multimodal llms. Advances in Neural Information Processing Systems, 37:87310–87356.
63. Naoki Wake, Atsushi Kanehira, Kazuhiro Sasabuchi, Jun Takamatsu, and Katsushi Ikeuchi. 2024. Gpt-4v(ision) for robotics: Multimodal task planning from human demonstration. IEEE Robotics and Automation Letters.
64. Chenyu Wang, Weixin Luo, Sixun Dong, Xiaohua Xuan, Zhengxin Li, Lin Ma, and Shenghua Gao. 2025a. Mllm-tool: A multimodal large language model for tool agent learning. In 2025 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV), pages 6678–6687. IEEE.
65. Jiongxiao Wang, Qiaojing Yan, Yawei Wang, Yijun Tian, Soumya Smruti Mishra, Zhichao Xu, Megha Gandhi, Panpan Xu, and Lin Lee Cheong. 2025b. Reinforcement learning for self-improving agent with skill library. arXiv preprint arXiv:2512.17102.
66. Yifan Wang, Jianjun Zhou, Haoyi Zhu, Wenzheng Chang, Yang Zhou, Zizun Li, Junyi Chen, Jiangmiao Pang, Chunhua Shen, and Tong He. 2025c. pi3: Scalable permutation-equivariant visual geometry learning. arXiv e-prints, pages arXiv–2507.
67. Yikun Wang, Siyin Wang, Qinyuan Cheng, Zhaoye Fei, Liang Ding, Qipeng Guo, Dacheng Tao, and Xipeng Qiu. 2025d. Visuothink: Empowering lvlm reasoning with multimodal tree search. arXiv preprint arXiv:2504.09130.
68. Zehan Wang, Haifeng Huang, Yang Zhao, Ziang Zhang, and Zhou Zhao. 2023. Chat-3d: Data-efficiently tuning large language model for universal dialogue of 3d scenes. arXiv preprint arXiv:2308.08769.
69. Zehan Wang, Ziang Zhang, Jiayang Xu, Jialei Wang, Tianyu Pang, Chao Du, Hengshuang Zhao, and Zhou Zhao. 2026. Orient anything v2: Unifying orientation and rotation understanding. arXiv preprint arXiv:2601.05573.
70. Zhenhailong Wang, Xuehang Guo, Sofia Stoica, Haiyang Xu, Hongru Wang, Hyeonjeong Ha, Xiusi Chen, Yangyi Chen, Ming Yan, Fei Huang, and 1 others. 2025e. Perception-aware policy optimization for multimodal reasoning. arXiv preprint arXiv:2507.06448.
71. Chenfei Wu, Shengming Yin, Weizhen Qi, Xiaodong Wang, Zecheng Tang, and Nan Duan. 2023. Visual chatgpt: Talking, drawing and editing with visual foundation models. arXiv preprint arXiv:2303.04671.
72. Diankun Wu, Fangfu Liu, Yi-Hsin Hung, and Yueqi Duan. 2025a. Spatial-mllm: Boosting mllm capabilities in visual-based spatial intelligence. arXiv preprint arXiv:2505.23747.
73. Haoning Wu, Xiao Huang, Yaohui Chen, Ya Zhang, Yanfeng Wang, and Weidi Xie. 2025b. Spatialscore: Towards unified evaluation for multimodal spatial understanding. arXiv preprint arXiv:2505.17012.
74. Junfei Wu, Jian Guan, Kaituo Feng, Qiang Liu, Shu Wu, Liang Wang, Wei Wu, and Tieniu Tan. 2025c. Reinforcing spatial reasoning in vision-language models with interwoven thinking and visual drawing. arXiv preprint arXiv:2506.09965.
75. Mingyuan Wu, Jingcheng Yang, Jize Jiang, Meitang Li, Kaizhuo Yan, Hanchao Yu, Minjia Zhang, Chengxiang Zhai, and Klara Nahrstedt. 2025d. Vtool-r1: Vlms learn to think with images via reinforcement learning on multimodal tool use. arXiv preprint arXiv:2505.19255.
76. Yixuan Wu, Yizhou Wang, Shixiang Tang, Wenhao Wu, Tong He, Wanli Ouyang, Philip Torr, and Jian Wu. 2024. Dettoolchain: A new prompting paradigm to unleash detection ability of mllm. In European Conference on Computer Vision, pages 164–182. Springer.
77. Peng Xia, Jianwen Chen, Hanyang Wang, Jiaqi Liu, Kaide Zeng, Yu Wang, Siwei Han, Yiyang Zhou, Xujiang Zhao, Haifeng Chen, and 1 others. 2026. Skillrl: Evolving agents via recursive skill-augmented reinforcement learning. arXiv preprint arXiv:2602.08234.
78. Renjun Xu and Yang Yan. 2026. Agent skills for large language models: Architecture, acquisition, security, and the path forward. arXiv preprint arXiv:2602.12430.
79. Sikuan Yan, Xiufeng Yang, Zuchao Huang, Ercong Nie, Zifeng Ding, Zonggen Li, Xiaowen Ma, Jinhe Bi, Kristian Kersting, Jeff Z Pan, and 1 others. 2025. Memory-r1: Enhancing large language model agents to manage and utilize memories via reinforcement learning. arXiv preprint arXiv:2508.19828.
80. Jihan Yang, Shusheng Yang, Anjali W Gupta, Rilyn Han, Li Fei-Fei, and Saining Xie. 2025a. Thinking in space: How multimodal large language models see, remember, and recall spaces. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 10632–10643.
81. Senqiao Yang, Junyi Li, Xin Lai, Bei Yu, Hengshuang Zhao, and Jiaya Jia. 2025b. Visionthink: Smart and efficient vision language model via reinforcement learning. arXiv preprint arXiv:2507.13348.
82. Sihan Yang, Runsen Xu, Yiman Xie, Sizhe Yang, Mo Li, Jingli Lin, Chenming Zhu, Xiaochen Chen, Haodong Duan, Xiangyu Yue, Dahua Lin, Tai Wang, and Jiangmiao Pang. 2025c. Mmsi-bench: A benchmark for multi-image spatial intelligence. In ICLR.
83. Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, and Chong Luo. 2026. Skillopt: Executive strategy for self-evolving agent skills. Preprint, arXiv:2605.23904.
84. Yuncong Yang, Jiageng Liu, Zheyuan Zhang, Siyuan Zhou, Reuben Tan, Jianwei Yang, Yilun Du, and Chuang Gan. 2025d. Mindjourney: Test-time scaling with world models for spatial reasoning. arXiv preprint arXiv:2507.12508.
85. Zeyuan Yang, Delin Chen, Xueyang Yu, Maohao Shen, and Chuang Gan. 2025e. Vca: Video curious agent for long video understanding. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 20168–20179.
86. Zhengyuan Yang, Linjie Li, Jianfeng Wang, Kevin Lin, Ehsan Azarnasab, Faisal Ahmed, Zicheng Liu, Ce Liu, Michael Zeng, and Lijuan Wang. 2023. Mm-react: Prompting chatgpt for multimodal reasoning and action. arXiv preprint arXiv:2303.11381.
87. Haoran Ye, Xuning He, Vincent Arak, Haonan Dong, and Guojie Song. 2026. Meta context engineering via agentic skill evolution. arXiv preprint arXiv:2601.21557.
88. Jiangye Yuan, Gowri Kumar, and Baoyuan Wang. 2026. Boosting mllm spatial reasoning with geometrically referenced 3d scene representations. arXiv preprint arXiv:2603.08592.
89. Haoyu Zhang, Meng Liu, Zaijing Li, Haokun Wen, Weili Guan, Yaowei Wang, and Liqiang Nie. 2025a. Spatial understanding from videos: Structured prompts meet simulation data. arXiv preprint arXiv:2506.03642.
90. Haozhen Zhang, Quanyu Long, Jianzhu Bao, Tao Feng, Weizhi Zhang, Haodong Yue, and Wenya Wang. 2026a. Memskill: Learning and evolving memory skills for self-evolving agents. arXiv preprint arXiv:2602.02474.
91. Xiaoyi Zhang, Zhaoyang Jia, Zongyu Guo, Jiahao Li, Bin Li, Houqiang Li, and Yan Lu. 2025b. Deep video discovery: Agentic search with tool use for long-form video understanding. arXiv preprint arXiv:2505.18079.
92. Yiming Zhang, Jiacheng Chen, Jiaqi Tan, Yongsen Mao, Wenhu Chen, and Angel X. Chang. 2026b. Revsi: Rebuilding visual spatial intelligence evaluation for accurate assessment of vlm 3d reasoning. arXiv preprint arXiv:2604.24300.
93. Zaibin Zhang, Yuhan Wu, Lianjie Jia, Yifan Wang, Zhongbo Zhang, Yijiang Li, Binghao Ran, Fuxi Zhang, Zhuohan Sun, Zhenfei Yin, and 1 others. 2026c. Think3d: Thinking with space for spatial reasoning. arXiv preprint arXiv:2601.13029.
94. Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, and Gao Huang. 2024. Expel: Llm agents are experiential learners. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pages 19632–19642.
95. Haoyu Zhao, Akide Liu, Zeyu Zhang, Weijie Wang, Feng Chen, Ruihan Zhu, Gholamreza Haffari, and Bohan Zhuang. 2026. Cov: Chain-of-view prompting for spatial reasoning. arXiv preprint arXiv:2601.05172.
96. Weicheng Zheng, Xiaofei Mao, Nanfei Ye, Pengxiang Li, Kun Zhan, Xianpeng Lang, and Hang Zhao. 2025. Driveagent-r1: Advancing vlm-based autonomous driving with hybrid thinking and active perception. arXiv e-prints, pages arXiv–2507.
97. Enshen Zhou, Jingkun An, Cheng Chi, Yi Han, Shanyu Rong, Chi Zhang, Pengwei Wang, Zhongyuan Wang, Tiejun Huang, Lu Sheng, and 1 others. 2025a. Roborefer: Towards spatial referring with reasoning in vision-language models for robotics. arXiv preprint arXiv:2506.04308.
98. Gengze Zhou, Yicong Hong, and Qi Wu. 2024. Navgpt: Explicit reasoning in vision-and-language navigation with large language models. In Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pages 7641–7649.
99. Zetong Zhou, Dongping Chen, Zixian Ma, Zhihan Hu, Mingyang Fu, Sinan Wang, Yao Wan, Zhou Zhao, and Ranjay Krishna. 2025b. Reinforced visual perception with tools. arXiv preprint arXiv:2509.01656.
100. Muzhi Zhu, Yuzhuo Tian, Hao Chen, Chunluan Zhou, Qingpei Guo, Yang Liu, Ming Yang, and Chunhua Shen. 2025. Segagent: Exploring pixel understanding capabilities in mllms by imitating human annotator trajectories. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 3686–3696.

## Appendix A. LLM Usage Claim

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The authors state that large language models were used only for language polishing, grammar correction, and improving manuscript clarity. All method design, experimental settings, data analysis, and final claims were developed, verified, and approved by the authors.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 作者声明，大语言模型仅用于语言润色、语法纠正和提升稿件清晰度。所有方法设计、实验设置、数据分析和最终论断均由作者开发、验证并批准。

## Appendix B. More Experimental Results

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The efficiency analysis compares inference cost and tool-use quality on VSI-Bench. Direct tool use only slightly improves average score, with 39.2% effective tool usage. Think3D improves accuracy but incurs higher inference cost, requiring 35.1 seconds per query on average. Skill-3D achieves the best score of 70.0, raises effective tool usage to 78.7%, and reduces average inference time to 20.8 seconds with only 0.5 seconds of retrieval overhead.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 效率分析比较 VSI-Bench 上的推理成本和工具使用质量。直接工具使用只小幅提高平均分，有效工具使用率为 39.2%。Think3D 提升准确率，但推理成本更高，平均每个查询需要 35.1 秒。Skill-3D 得到最佳平均分 70.0，把有效工具使用率提升到 78.7%，并将平均推理时间降至 20.8 秒，其中检索开销仅 0.5 秒。

### Table B.1. 效率分析

![Table B.1](table_b1_efficiency.png)

**Caption:** Table B.1: Efficiency analysis on VSI-Bench. The table reports the average number of tool calls, effective tool usage, average inference time per query, and performance gain. All experiments are conducted using GPT-5.4.

**Caption[CN]:** 表 B.1：VSI-Bench 上的效率分析。该表报告平均工具调用次数、有效工具使用率、每个查询的平均推理时间和性能增益。所有实验使用 GPT-5.4。

| Method | Avg. Calls | Eff. Usage (%) | Retr. Time (s) | Avg. Runtime (s) | VSI Avg. |
|---|---:|---:|---:|---:|---:|
| w/o Tools | 0.0 | – | 0.0 | 0.0 | 52.1 |
| w/ Tools | 1.2 | 39.2 | 0.0 | 13.2 | 58.2 |
| Think3D | 1.8 | 58.5 | 0.0 | 35.1 | 64.7 |
| Skill-3D | 2.6 | 78.7 | 0.5 | 20.8 | 70.0 |


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The cross-benchmark transfer analysis evaluates whether dynamic skills generalize across benchmarks. Skills learned from VSI-Bench transfer to MMSI-Bench and CV-3D, while MMSI-Bench skills also improve VSI-Bench. Pooling all training benchmarks achieves the best results, suggesting that related spatial reasoning tasks share reusable tool-use procedures and that the Skill Library benefits from complementary scene-task knowledge.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 跨基准迁移分析评估 dynamic skills 是否能跨基准泛化。从 VSI-Bench 学到的技能可迁移到 MMSI-Bench 和 CV-3D，而 MMSI-Bench 技能也能提升 VSI-Bench。合并所有训练基准得到最佳结果，说明相关空间推理任务共享可复用工具流程，Skill Library 能从互补的场景-任务知识中获益。

### Table B.2. 跨基准技能迁移

![Table B.2](table_b2_transfer.png)

**Caption:** Table B.2: Cross-benchmark skill transfer. Dynamic skills are built from one source benchmark and evaluated on other target benchmarks. All settings use the same static skills and GPT-5.4.

**Caption[CN]:** 表 B.2：跨基准技能迁移。作者从一个源基准构建动态技能，并在其他目标基准上评估。所有设置使用相同静态技能与 GPT-5.4。

| Dynamic Skills Source | VSI Avg. | BLINK | CV-3D Avg. | MMSI-PR |
|---|---:|---:|---:|---:|
| w/o Dynamic Skills | 63.4 | 77.2 | 92.2 | 52.6 |
| VSI-Bench | 68.7 | 78.5 | 93.7 | 57.8 |
| BLINK | 63.9 | 80.6 | 92.8 | 53.4 |
| CV-3D | 64.8 | 77.5 | 94.2 | 55.7 |
| MMSI-Bench | 67.3 | 78.3 | 93.2 | 57.2 |
| All Benchmarks | 69.9 | 82.0 | 95.3 | 60.4 |


## Appendix C. Experimental Details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The dataset details clarify that VSI-Bench, BLINK, CV-3D, and MMSI-Bench do not provide official training splits for skill construction or post-training. The authors therefore use a category-wise random split and ensure question-level disjointness. VSI-Bench covers egocentric indoor visual spatial intelligence; BLINK uses a multi-view spatial subset; CV-3D focuses on geometric spatial reasoning; and MMSI-Bench focuses on positional relationship reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 数据集细节说明，VSI-Bench、BLINK、CV-3D 和 MMSI-Bench 都没有为技能构建或后训练提供官方训练划分。因此作者采用类别级随机划分，并确保问题级互斥。VSI-Bench 覆盖第一视角室内视觉空间智能；BLINK 使用多视角空间子集；CV-3D 聚焦几何空间推理；MMSI-Bench 聚焦位置关系推理。

### Table C.3. 数据集划分

![Table C.3](table_c3_dataset_split.png)

**Caption:** Table C.3: Dataset statistics and train/test split. The training set is used for skill construction and post-training, while all reported results are computed on the held-out test set.

**Caption[CN]:** 表 C.3：数据集统计与训练/测试划分。训练集用于技能构建和后训练，所有报告结果都在 held-out 测试集上计算。

| Dataset | #Tasks | #Total | #Train | #Test |
|---|---:|---:|---:|---:|
| VSI-Bench | 8 | 2362 | 708 | 1654 |
| MMSI-Bench | 1 | 502 | 157 | 345 |
| CV-3D | 2 | 1200 | 360 | 840 |
| BLINK | 1 | 133 | 40 | 93 |


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The hyperparameter table reports the post-training configuration. The foundation models are Qwen3-VL-4B/8B, max sequence length is 4096, training precision is bfloat16, optimizer is AdamW, SFT uses learning rate 1e-5 and batch size 16 for one epoch, while GRPO uses learning rate 1e-6, batch size 16, group size 8, gradient accumulation 4, clipping epsilon 0.2, and KL coefficient 0.05.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 超参数表报告后训练配置。基础模型为 Qwen3-VL-4B/8B，最大序列长度 4096，训练精度 bfloat16，优化器 AdamW。SFT 使用 1e-5 学习率、batch size 16、训练 1 个 epoch；GRPO 使用 1e-6 学习率、batch size 16、group size 8、梯度累积 4、clipping epsilon 0.2、KL 系数 0.05。

### Table C.4. 后训练超参数

![Table C.4](table_c4_hyperparameters.png)

**Caption:** Table C.4: Hyperparameter settings of Skill-3D.

**Caption[CN]:** 表 C.4：Skill-3D 的超参数设置。

| Parameter | Setting | Parameter | Setting |
|---|---|---|---|
| Foundation model | Qwen3-VL-4B/8B | SFT learning rate | $1 \times 10^{-5}$ |
| Number of GPUs | 4 | SFT batch size | 16 |
| Max sequence length | 4096 | SFT epochs | 1 |
| Training precision | bfloat16 | SFT warmup ratio | 0.03 |
| Flash Attention | True | GRPO learning rate | $1 \times 10^{-6}$ |
| Gradient checkpointing | True | GRPO batch size | 16 |
| Optimizer | AdamW | GRPO group size | 8 |
| Clipping epsilon | 0.2 | Gradient accumulation steps | 4 |
| GRPO training epochs | 1 | KL coefficient | 0.05 |


> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The appendix gives the full GRPO objective. For each query, the policy samples G complete trajectories from the current policy; rewards are normalized within the sampled group to compute relative advantages. The clipped surrogate objective uses the importance ratio between current and old policies, with a KL term to preserve SFT-learned skill-selection and tool-use behavior. This favors trajectories with higher task success, better tool-use efficiency, and valid outputs.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 附录给出了完整 GRPO 目标。对每个查询，策略从当前策略采样 G 条完整轨迹；奖励在组内归一化以计算相对 advantage。裁剪 surrogate objective 使用当前策略与旧策略之间的重要性比率，并加入 KL 项来保持 SFT 学到的技能选择和工具使用行为。这会偏好任务成功率更高、工具使用效率更好且输出有效的轨迹。

$$
Ai = (R(τi) - mean({R(τj)}j=1..G)) / std({R(τj)}j=1..G)
$$

$$
J(θ) = E[ (1/G) Σi=1..G min(ρi Ai, clip(ρi, 1 - ε, 1 + ε) Ai) - βKL DKL(πθ || πref) ]
$$

$$
ρi = πθ(τi | q, O, Scand) / πold(τi | q, O, Scand)
$$

## Appendix D. Qualitative Results

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper shows two representative cases: metric distance estimation and room-level object counting. In the distance case, Think3D calls Pi3 reconstruction and object detection but remains reconstruction-centric; because the table and bathtub appear in different partial views and closest boundaries are not explicitly grounded, it overestimates the distance as 1.5m. Skill-3D retrieves a depth-distance skill and combines Pi3, object detection, and depth estimation, grounding closest object boundaries and predicting the correct 0.9m.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文展示两个代表性案例：metric distance 估计和房间级目标计数。在距离案例中，Think3D 调用 Pi3 重建和目标检测，但仍以重建为中心；由于桌子和浴缸出现在不同局部视角中，最近边界没有被显式 grounding，它把距离高估为 1.5m。Skill-3D 检索 depth-distance 技能，并结合 Pi3、目标检测和深度估计，对最近物体边界进行 grounding，预测正确的 0.9m。

### Fig. E.1. 边界感知距离推理案例

![Fig. E.1](fig_e1_distance_case.png)

**Caption:** Figure E.1: Case study on boundary-aware metric distance reasoning. Colored highlights indicate different reasoning elements: red marks the question and incorrect answer, green marks the ground-truth or correct answer, teal marks invoked tools, purple marks retrieved skills, and yellow marks iteration or answer labels. Think3D relies on coarse reconstruction and object detection, but lacks boundary-aware depth evidence and overestimates the distance as 1.5m. Skill-3D retrieves a depth-distance skill and combines Pi3 reconstruction, object detection, and depth estimation, enabling the agent to align room-level geometry with local depth cues and output the correct 0.9m answer.

**Caption[CN]:** 图 E.1：边界感知 metric distance 推理案例。彩色高亮表示不同推理元素：红色为问题和错误答案，绿色为真值或正确答案，青色为调用工具，紫色为检索技能，黄色为迭代或答案标签。Think3D 依赖粗粒度重建和目标检测，但缺少边界感知深度证据，因此将距离高估为 1.5m。Skill-3D 检索 depth-distance 技能，并结合 Pi3 重建、目标检测和深度估计，使 agent 能把房间级几何与局部深度线索对齐，输出正确的 0.9m。


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In the counting case, Think3D mainly relies on Pi3 reconstruction and coarse cross-view matching, causing repeated observations of the same chair to be counted multiple times. Skill-3D retrieves a detection-counting skill and combines Pi3 layout consistency with object detection evidence, grounding chair instances across views and suppressing duplicates to obtain the correct count of four.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在计数案例中，Think3D 主要依赖 Pi3 重建和粗粒度跨视角匹配，导致同一把椅子的重复观测被多次计数。Skill-3D 检索 detection-counting 技能，并结合 Pi3 布局一致性和目标检测证据，在跨视角中 grounding 椅子实例并抑制重复，得到正确计数四。

### Fig. E.2. 多视角计数案例

![Fig. E.2](fig_e2_counting_case.png)

**Caption:** Figure E.2: Case study on multi-view object counting. Colored highlights indicate different reasoning elements: red marks the question and incorrect answer, green marks the ground-truth or correct answer, teal marks invoked tools, purple marks retrieved skills, and yellow marks iteration or answer labels. Think3D mainly relies on Pi3 reconstruction and coarse cross-view matching, causing repeated chair appearances across sampled views to be counted as distinct instances and leading to an over-count of five chairs. Skill-3D retrieves a detection-counting skill and combines Pi3 layout consistency with object detection, enabling instance-level grounding and cross-view de-duplication to produce the correct count of four chairs.

**Caption[CN]:** 图 E.2：多视角目标计数案例。彩色高亮含义同图 E.1。Think3D 主要依赖 Pi3 重建和粗粒度跨视角匹配，导致同一把椅子在相邻视角中被重复计数，得到错误的五把椅子。Skill-3D 检索 detection-counting 技能，并结合 Pi3 布局一致性与目标检测，从而完成实例级定位和跨视角去重，得到正确的四把椅子。


## Appendix E. Prompt Design

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Detailed prompt design for each phrase/stage of the framework provided in Fig~\ref{fig:p1}, Fig.~\ref{fig:p2}, Fig.~\ref{fig:p3} and Fig.~\ref{fig:p4}.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 图~\ref{fig:p1}、图~\ref{fig:p2}、图~\ref{fig:p3} 和图~\ref{fig:p4} 给出了该框架每个阶段/步骤的详细提示词设计。

### Fig. E.3. System Prompt

![Fig. E.3](fig_e3_system_prompt.png)

**Caption:** Figure E.3: System Prompt.

**Caption[CN]:** 图 E.3：系统提示词。


### Fig. E.4. System Prompt and Scene Context Prompt

![Fig. E.4](fig_e4_system_scene_context_prompt.png)

**Caption:** Figure E.4: System Prompt and Scene Context Prompt.

**Caption[CN]:** 图 E.4：系统提示词和场景上下文提示词。


### Fig. E.5. Skill Retrieval、Tool Planning 与 Tool Exclusion Prompt

![Fig. E.5](fig_e5_retrieval_planning_exclusion_prompt.png)

**Caption:** Figure E.5: Skill Retrieval Prompt, Tool Planning Prompt and Tool Exclusion Prompt.

**Caption[CN]:** 图 E.5：技能检索提示词、工具规划提示词和工具排除提示词。


### Fig. E.6. Tool Exclusion 与 Final Answer Prompt

![Fig. E.6](fig_e6_tool_final_prompts.png)

**Caption:** Figure E.6: Tool Exclusion Prompt and Final Answer Prompt.

**Caption[CN]:** 图 E.6：工具排除提示词和最终回答提示词。


### System_Prompt

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span>
>
> ```text
> You are Skill-3D, a scene-aware multimodal spatial reasoning agent.
> Your goal is to answer visual spatial reasoning questions accurately by combining:
> 1. scene context memory,
> 2. static and dynamic skills,
> 3. external perception or geometry tools,
> 4. careful final reasoning grounded in tool evidence.
>
> You must not answer metric, boundary-sensitive, counting, localization, or
> orientation questions from RGB intuition alone when a relevant tool or skill is
> available.
> ## Core Procedure
> For each user question, follow this internal loop:
> 1. Scene understanding
>    - Identify the scene type, target objects, visible views, and whether the input is
>      single-view or multi-view.
>    - Classify the task type: object distance, absolute depth, relative depth, spatial
>      relation, object counting, object localization, orientation, object size,
>      affordance, occlusion, reconstruction, or view selection.
>    - Decide whether the question requires metric evidence, object boundaries, precise
>      points, multi-view geometry, OCR, or detection.
> 2. Skill retrieval
>    - Retrieve relevant dynamic skills from scene-aware memory when available.
>    - Retrieve static seed skills when no suitable dynamic skill exists.
>    - Prefer skills whose trigger condition matches the task type and whose historical
>      tool usage matches the needed evidence.
>    - If multiple similar skills are retrieved, choose the most specific skill and
>      ignore redundant ones.
> 3. Tool planning
>    - Use the selected skill to plan the minimum sufficient tool calls.
>    - For object identity or localization, use detection or grounding tools.
>    - For closest-point or boundary-sensitive questions, use segmentation and pointing
>      tools.
>    - For metric depth or distance, use depth estimation and, when needed, 3D
>      reconstruction.
>    - For multi-view or room-level geometry, use Pi3 or the available reconstruction
>      tool.
>    - For orientation questions, use orientation estimation tools.
>    - Avoid duplicate tool calls unless they verify a genuinely uncertain result.
> 4. Tool execution and adoption
>    - Execute planned tools when they are necessary.
>    - Treat a tool call as useful only if it successfully returns relevant evidence.
>    - Use tool outputs explicitly in reasoning. Do not ignore tool evidence after
>      calling a tool.
>    - If a tool result conflicts with RGB intuition, prefer the tool-backed evidence
>      unless the tool result is clearly invalid.
> 5. Final answer
>    - Answer the original question directly.
>    - For metric answers, provide the best approximate value and the unit requested by
>      the question.
>    - For multiple-choice answers, output the selected option and a short reason.
>    - Mention uncertainty only when the evidence is genuinely insufficient.
>    - Do not expose irrelevant implementation details.
> ```

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span>
>
> ```text
> 你是 Skill-3D，一个场景感知的多模态空间推理 agent。
> 你的目标是通过结合以下内容，准确回答视觉空间推理问题：
> 1. 场景上下文记忆，
> 2. 静态和动态技能，
> 3. 外部感知或几何工具，
> 4. 基于工具证据的审慎最终推理。
>
> 当相关工具或技能可用时，你不得仅凭 RGB 直觉回答度量、边界敏感、计数、定位或
> 朝向问题。
> ## 核心流程
> 对于每个用户问题，遵循以下内部循环：
> 1. 场景理解
>    - 识别场景类型、目标物体、可见视角，以及输入是
>      单视角还是多视角。
>    - 对任务类型分类：物体距离、绝对深度、相对深度、空间
>      关系、物体计数、物体定位、朝向、物体尺寸、
>      可供性、遮挡、重建，或视角选择。
>    - 判断问题是否需要度量证据、物体边界、精确
>      点、多视角几何、OCR 或检测。
> 2. 技能检索
>    - 在可用时，从场景感知记忆中检索相关动态技能。
>    - 当不存在合适动态技能时，检索静态种子技能。
>    - 优先选择其触发条件与任务类型匹配，且其历史
>      工具使用与所需证据匹配的技能。
>    - 如果检索到多个相似技能，选择最具体的技能，并
>      忽略冗余技能。
> 3. 工具规划
>    - 使用所选技能规划最小充分的工具调用。
>    - 对物体身份或定位，使用检测或 grounding 工具。
>    - 对最近点或边界敏感问题，使用分割和指点
>      工具。
>    - 对度量深度或距离，使用深度估计，并在需要时使用 3D
>      重建。
>    - 对多视角或房间级几何，使用 Pi3 或可用的重建
>      工具。
>    - 对朝向问题，使用朝向估计工具。
>    - 除非用于验证确有不确定性的结果，否则避免重复工具调用。
> 4. 工具执行与采纳
>    - 在必要时执行规划的工具。
>    - 仅当工具调用成功返回相关证据时，才将其视为有用。
>    - 在推理中显式使用工具输出。调用工具后不得忽略工具证据。
>    - 如果工具结果与 RGB 直觉冲突，除非工具结果明显无效，否则优先采用有工具支持的证据。
> 5. 最终回答
>    - 直接回答原始问题。
>    - 对度量答案，提供最佳近似值和问题要求的单位。
>    - 对多项选择答案，输出所选选项和简短理由。
>    - 仅当证据确实不足时才提及不确定性。
>    - 不要暴露无关实现细节。
> ```

### System_Prompt (continued)

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span>
>
> ```text
> ## Skill Selection Rules
> <skill_json>
> ## Required Reasoning Style
> Think in this order:
> 1. What is the question asking for?
> 2. What scene memory or retrieved skill applies?
> 3. What evidence is missing from raw images?
> 4. Which tool calls fill that evidence gap?
> 5. What answer follows from the tool evidence?
>
> Never skip tool use when:
> - the question asks for precise or approximate physical distance,
> - the answer depends on closest object boundaries,
> - the target objects appear in different views,
> - object identity or location is ambiguous,
> - the required answer is not directly visible from one image.
> ## Output Format
> When tools are available, use this format internally:
> <think>
> Task type: ...
> Scene context: ...
> Final reasoning: ...
> </think>
> <skill_choice>
> ...
> </skill_choice>
> <tool_call>
> ...
> </tool_call>
> <answer>
> ...
> </answer>
>
> If the runtime does not allow visible chain-of-thought, keep the same reasoning
> internal and only output:
> <answer>
> ...
> </answer>
> ```

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span>
>
> ```text
> ## 技能选择规则
> <skill_json>
> ## 必需推理风格
> 按以下顺序思考：
> 1. 问题要求什么？
> 2. 哪个场景记忆或检索到的技能适用？
> 3. 原始图像缺少什么证据？
> 4. 哪些工具调用能填补该证据缺口？
> 5. 工具证据能导出什么答案？
>
> 在以下情况下绝不能跳过工具使用：
> - 问题要求精确或近似的物理距离，
> - 答案依赖最近的物体边界，
> - 目标物体出现在不同视角中，
> - 物体身份或位置不明确，
> - 所需答案无法从一张图像直接看出。
> ## 输出格式
> 当工具可用时，内部使用以下格式：
> <think>
> Task type: ...
> Scene context: ...
> Final reasoning: ...
> </think>
> <skill_choice>
> ...
> </skill_choice>
> <tool_call>
> ...
> </tool_call>
> <answer>
> ...
> </answer>
>
> 如果运行时不允许可见的 chain-of-thought，则保持相同推理
> 在内部进行，并且只输出：
> <answer>
> ...
> </answer>
> ```

### Scene_Context_Prompt

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span>
>
> ```text
> You are given a 3D indoor scene and a spatial reasoning question.
> Your task is to analyze the scene before any tool selection.
> ## Inputs
> - Multi-view RGB frames
> - Key frames sampled from the trajectory
> - User question
> ## Objectives
> 1. Identify the scene type and visible target objects.
> 2. Determine the reasoning scope:
>    - single-view
>    - multi-view
>    - room-level
>    - object-to-object
> 3. Identify the required evidence types:
>    - object detection
>    - segmentation
>    - depth estimation
>    - orientation estimation
>    - 3D reconstruction
> 4. Determine whether RGB-only reasoning is sufficient.
> 5. Infer the expected geometric constraints of the question.
> ## Output Format
> <scene_context>
> Scene Type: ...
> Reasoning Scope: ...
> Target Objects: ...
> Required Evidence: ...
> RGB Sufficiency: ...
> Spatial Constraints: ...
> </scene_context>
> ```

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span>
>
> ```text
> 你获得一个 3D 室内场景和一个空间推理问题。
> 你的任务是在任何工具选择之前分析场景。
> ## 输入
> - 多视角 RGB 帧
> - 从轨迹中采样的关键帧
> - 用户问题
> ## 目标
> 1. 识别场景类型和可见目标物体。
> 2. 确定推理范围：
>    - 单视角
>    - 多视角
>    - 房间级
>    - 物体到物体
> 3. 识别所需证据类型：
>    - 目标检测
>    - 分割
>    - 深度估计
>    - 朝向估计
>    - 3D 重建
> 4. 判断仅用 RGB 推理是否充分。
> 5. 推断问题预期的几何约束。
> ## 输出格式
> <scene_context>
> Scene Type: ...
> Reasoning Scope: ...
> Target Objects: ...
> Required Evidence: ...
> RGB Sufficiency: ...
> Spatial Constraints: ...
> </scene_context>
> ```

### Skill_Retrieval_Prompt

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span>
>
> ```text
> You are given the scene context and the user question.
> Your task is to retrieve the most relevant scene-aware skills for tool orchestration.
> ## Available Static Skills
> - seed::object_counting                                      
> - seed::metric_distance_estimation                           
> - seed::relative_depth_ordering                              
> - seed::view_selection                                       
> - seed::detection_depth_fusion                               
> - seed::detection_segmentation_fusion                        
> - seed::orientation_estimation                              
> - seed::3d_reconstruction 
> ## Retrieval Rules
> - Prefer dynamic skills if a matched scene-aware workflow exists.
> - Otherwise, fallback to the corresponding static skill.
> ## Objectives
> 1. Match the current scene-task pair with relevant skills.
> 2. Select the minimum sufficient workflow.
> 3. Explain why the selected skills are relevant.
> ## Output Format
> <skill_choice>
> Selected Skills: ...
> Rationale: ...
> </skill_choice>
> ```

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span>
>
> ```text
> 你获得场景上下文和用户问题。
> 你的任务是检索最相关的场景感知技能以进行工具编排。
> ## 可用静态技能
> - seed::object_counting                                      
> - seed::metric_distance_estimation                           
> - seed::relative_depth_ordering                              
> - seed::view_selection                                       
> - seed::detection_depth_fusion                               
> - seed::detection_segmentation_fusion                        
> - seed::orientation_estimation                              
> - seed::3d_reconstruction 
> ## 检索规则
> - 如果存在匹配的场景感知工作流，优先选择动态技能。
> - 否则，回退到对应的静态技能。
> ## 目标
> 1. 将当前场景-任务对与相关技能匹配。
> 2. 选择最小充分工作流。
> 3. 解释所选技能为何相关。
> ## 输出格式
> <skill_choice>
> Selected Skills: ...
> Rationale: ...
> </skill_choice>
> ```

### Tool_Planning_Prompt

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span>
>
> ```text
> You are given the retrieved skills and the scene context.
> Your task is to generate the minimum sufficient tool workflow.
> ## Planning Principles
> - Avoid redundant tool calls.
> - Prefer geometric evidence over RGB intuition for metric reasoning.
> - Reuse previous evidence whenever possible.
> - Use segmentation when boundary precision matters.
> - Use 3D reconstruction for cross-view or room-level reasoning
> ## Available Tools
> - detect_objects_tool
> - segment_image_tool
> - depth_estimation_tool
> - orientation_estimation_tool
> - pi3_tool
> - super_resolution_tool
> ## Objectives
> 1. Generate an ordered tool plan.
> 2. Specify the purpose of each tool call.
> 3. Ensure that the workflow satisfies the selected skills.
> ## Output Format
> <tool_call>
> 1. Tool_1: ...
> 2. Tool_2: ...
> </tool_call>
> ```

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span>
>
> ```text
> 你获得检索到的技能和场景上下文。
> 你的任务是生成最小充分的工具工作流。
> ## 规划原则
> - 避免冗余工具调用。
> - 对度量推理，优先使用几何证据而非 RGB 直觉。
> - 尽可能复用先前证据。
> - 当边界精度重要时使用分割。
> - 对跨视角或房间级推理使用 3D 重建
> ## 可用工具
> - detect_objects_tool
> - segment_image_tool
> - depth_estimation_tool
> - orientation_estimation_tool
> - pi3_tool
> - super_resolution_tool
> ## 目标
> 1. 生成有序工具计划。
> 2. 指明每次工具调用的目的。
> 3. 确保工作流满足所选技能。
> ## 输出格式
> <tool_call>
> 1. Tool_1: ...
> 2. Tool_2: ...
> </tool_call>
> ```

### Tool_Exclusion_Prompt

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span>
>
> ```text
> Execute the planned tools and store all returned evidence.
> ## For Each Tool Call
> Record:
> - raw structured outputs
> - visualization paths
> - concise interpretation
> - uncertainty or failure notes
> ## Objectives
> 1. Preserve all geometric evidence.
> 2. Detect invalid or low-confidence outputs.
> 3. Track whether the evidence supports the current reasoning trajectory.
> 4. Record failures for future skill refinement.
> ## Output Format
> <tool_evidence>
> Tool: ...
> Raw Output: ...
> Visualization: ...
> Interpretation: ...
> Uncertainty: ...
> </tool_evidence>
> ```

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span>
>
> ```text
> 执行规划的工具并存储所有返回证据。
> ## 对每次工具调用
> 记录：
> - 原始结构化输出
> - 可视化路径
> - 简明解释
> - 不确定性或失败说明
> ## 目标
> 1. 保留所有几何证据。
> 2. 检测无效或低置信度输出。
> 3. 跟踪证据是否支持当前推理轨迹。
> 4. 记录失败以便未来技能细化。
> ## 输出格式
> <tool_evidence>
> Tool: ...
> Raw Output: ...
> Visualization: ...
> Interpretation: ...
> Uncertainty: ...
> </tool_evidence>
> ```

### Final_Answer_Prompt

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span>
>
> ```text
> Use the scene context, retrieved skills, and tool evidence to answer the question.
> ## Answering Rules
> - Do not answer metric questions from RGB intuition alone.
> - Prioritize geometric evidence over appearance cues.
> - Cite the relevant tool evidence.
> - Avoid overclaiming precision.
> - If uncertainty exists, provide the best approximate range.
> ## Objectives
> 1. Integrate multi-tool evidence consistently.
> 2. Produce a spatially grounded answer.
> 3. Ensure that the reasoning matches the selected skill workflow.
> ## Output Format
> <answer>...</answer>
> ```

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span>
>
> ```text
> 使用场景上下文、检索到的技能和工具证据回答问题。
> ## 回答规则
> - 不要仅凭 RGB 直觉回答度量问题。
> - 优先使用几何证据而非外观线索。
> - 引用相关工具证据。
> - 避免过度声称精度。
> - 若存在不确定性，给出最佳近似范围。
> ## 目标
> 1. 一致地整合多工具证据。
> 2. 生成有空间 grounding 的回答。
> 3. 确保推理与所选技能工作流一致。
> ## 输出格式
> <answer>...</answer>
> ```

