# AlloSpatial: Agentic Harness Framework for Spatial Reasoning in Foundation Models

**Authors:** Shouwei Ruan, Bin Wang, Zhenyu Wu, Qihui Zhu, Yuxiang Zhang, Jingzhi Li, Yubin Wang, Xingxing Wei
**Source:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/QXAH89IU/Ruan 等 - 2026 - AlloSpatial Agentic Harness Framework for Spatial Reasoning in Foundation Models.pdf`
**Detected source format:** selectable-text PDF (`pdf-text`)
**Reader type:** complete 30-page Chinese-English adjacent paragraph-pair Markdown reader
**Version:** arXiv:2606.08952v1 [cs.AI], 8 June 2026
**One-file mode:** strict one-file mode. Images are not embedded; all figure captions, figure-like case captions, and searchable table transcriptions are preserved in this file.

## Page / Section Index

| PDF pages | Content |
|---|---|
| 1 | Title, authors, abstract, 1. Introduction (opening) |
| 2 | Figure 1, Introduction continued |
| 3 | 2. Related Work; 3. Methodology; 3.1 Problem Formulation; 3.2 World2Mind |
| 4 | 3.2.1 Geometry-Semantic Alignment Pipeline; 3.2.2 Allocentric Mapping; 3.3 Spatial Reasoning Harness |
| 5 | Table 1; 3.4 Internalizing the Spatial Reasoning Harness via Reinforcement Learning |
| 6 | Table 2; 4. Experiments; 4.1 Experimental Setup |
| 7 | Table 3; Figure 2; 4.2 Training-free proprietary-model results; Figure 3 |
| 8 | 4.3 Trained agents; Figure 4; Table 4 |
| 9 | 4.4 Ablation Studies and Additional Results; 5. Conclusion & Limitations |
| 10 | Conclusion end; References begin |
| 11-12 | References [1]-[48] |
| 13-14 | Appendix A. Training & Evaluation Configuration; Table 5; Appendix B. World2Mind Service Parallelization |
| 15 | Appendix C. Spatial Reasoning Harness Prompts (system message, tool interface, local tool-call schema, reasoning protocol) |
| 16-18 | Appendix D.1 Case 1: Metric Closest-Point Reasoning |
| 19-21 | Appendix D.2 Case 2: Viewpoint-Conditioned Navigation |
| 22 | Appendix E. Computational Costs in Training and Inference |
| 23-30 | Complete NeurIPS Paper Checklist, including initial instructions, 16 questions, answers, justifications, and guidelines |

## Terminology Ledger

| Canonical term | Chinese | Usage decision |
|---|---|---|
| AlloSpatial | AlloSpatial | 保留方法名称 |
| World2Mind | World2Mind | 保留工具/沙盒名称 |
| Multimodal Foundation Models (MFMs) | 多模态基础模型（MFMs） | 首次展开，后用 MFM/MFMs |
| allocentric | 非自我中心式 | 与 egocentric（自我中心式）相对 |
| egocentric | 自我中心式 | 统一译法 |
| Spatial Reasoning Harness | 空间推理 harness | 保留 `harness` 作为方法名核心术语 |
| cognitive mapping sandbox | 认知制图沙盒 | 统一译法 |
| Allocentric-Spatial Tree (AST) | 非自我中心空间树（AST） | 保留 AST |
| Landmark Cognitive Map | 地标认知地图 | 统一译法 |
| Route Cognitive Map | 路径认知地图 | 统一译法 |
| modality-decoupled cue collection | 模态解耦线索收集 | 统一译法 |
| geometry-semantics interleaved arbitration | 几何—语义交织仲裁 | 统一译法 |
| Group Sequence Policy Optimization (GSPO) | 组序列策略优化（GSPO） | 首次展开，后用 GSPO |
| Harness-Gated Trajectory Reward (HGTR) | Harness 门控轨迹奖励（HGTR） | 保留 HGTR |
| mean relative accuracy (MRA) | 平均相对准确率（MRA） | 统一译法 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Multimodal Foundation Models (MFMs) have made substantial progress, yet remain fragile in spatial reasoning over the physical world. A key bottleneck lies in their inability to transform local egocentric observations into a global allocentric spatial representation. To address this, we propose AlloSpatial, an agentic framework for allocentric spatial cognition in foundation models. AlloSpatial introduces World2Mind, a plug-and-play cognitive mapping sandbox that converts egocentric observations into structured allocentric priors, including Allocentric-Spatial Trees and route maps that support querying object topology, geometric relations, passability, and trajectories. To utilize these priors reliably under noisy reconstruction and ambiguous visual evidence, AlloSpatial introduces a Spatial Reasoning Harness for tool-use judgment, modality-decoupled cue collection, and geometry-semantic arbitration. We further internalize this process in Qwen3-VL through cold-start reinforcement learning with a harness-gated trajectory-level reward. Experiments on VSI-Bench and MindCube show that AlloSpatial improves proprietary models by 5%–18% in a training-free setting, while ASTs alone support strong spatial reasoning even when visual inputs are removed. The trained AlloSpatial agents further outperform larger general-purpose models and competitive spatial baselines, suggesting that structured allocentric representations, active tool use, and verifiable reasoning offer a promising route toward spatially capable foundation models. Our code: https://github.com/Heathcliff-saku/AlloSpatial

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 多模态基础模型（Multimodal Foundation Models, MFMs）已经取得了显著进展，但在物理世界中的空间推理仍然脆弱。一个关键瓶颈在于，它们无法把局部的自我中心观察转化为全局的非自我中心空间表征。为解决这一问题，我们提出 AlloSpatial，一个面向基础模型非自我中心空间认知的代理式框架。AlloSpatial 引入 World2Mind，这是一种即插即用的认知制图沙盒，可将自我中心观察转换为结构化的非自我中心先验，包括支持查询物体拓扑、几何关系、可通行性和轨迹的非自我中心空间树（AST）与路径地图。为了在重建噪声和视觉证据模糊的情况下可靠地利用这些先验，AlloSpatial 还引入了一个 Spatial Reasoning Harness，用于工具使用判断、模态解耦线索收集以及几何—语义仲裁。我们进一步通过带有 harness 门控轨迹级奖励的冷启动强化学习，将这一过程内化到 Qwen3-VL 中。在 VSI-Bench 和 MindCube 上的实验表明，AlloSpatial 在免训练设定下可将闭源模型性能提升 5%–18%；即使移除视觉输入，仅 AST 也能支持强空间推理能力。训练后的 AlloSpatial agents 还优于更大的通用模型以及有竞争力的空间推理基线，这表明结构化的非自我中心表征、主动工具使用与可验证推理，为构建具备空间能力的基础模型提供了一条很有前景的路径。代码地址：https://github.com/Heathcliff-saku/AlloSpatial

## 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Multimodal Foundation Models (MFMs) [1, 25, 32, 13, 33] have made substantial progress in cross-modal understanding and reasoning. Yet their ability to reason about 3D space in the physical world remains fragile [41, 35, 19, 17, 28]. A central limitation is that current MFMs largely operate over local, transient, and egocentric observations, lacking a mechanism to transform partial perceptual evidence into global, persistent, and queryable mental representations that reliably bridge semantic understanding and geometric relations [35, 33, 42].

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 多模态基础模型（MFMs）[1, 25, 32, 13, 33] 在跨模态理解与推理方面已取得显著进展。然而，它们在物理世界中进行三维空间推理的能力仍然脆弱 [41, 35, 19, 17, 28]。一个核心限制在于，现有 MFM 主要处理局部、瞬时、且自我中心式的观察，缺乏一种机制，无法把部分感知证据转化为全局、持久、可查询的心理表征，从而可靠地桥接语义理解与几何关系 [35, 33, 42]。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Existing approaches have improved spatial reasoning along three paradigms. Vision-centric methods post-train MFMs on large-scale 3D-grounded samples, encouraging models to infer depth, size, location, or spatial relations directly from limited visual observations [10, 7, 21, 39]. While effective under in-distribution settings, recent studies [27, 16, 40] indicate that their gains are often coupled to the statistics of the training distribution and may degrade under shifts in scene layout. Geometry-centric methods inject explicit spatial signals, such as depth maps, point clouds, or learned 3D representations, to compensate for the weak geometric grounding of 2D visual inputs [11, 8, 23, 38]. Although useful, such signals introduce nontrivial cross-modal alignment challenges [45] and often require geometry-rich paired data and costly training for specialized architectures. More recently, tool-augmented spatial reasoning enables models to call tools or task-specific models (e.g., 3D reconstruction, novel-view rendering, depth estimation, or pose estimation) for active evidence acquisition [46, 20, 9]. However, these tools typically return pixel-space observations or low-level geometric measurements, leaving the model to assemble high-level spatial structure through a long, error-prone reasoning chain. As a result, noisy or incomplete tool evidence can be absorbed rather than challenged, leading to incorrect reasoning results.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 现有提升空间推理的工作主要沿着三种范式展开。以视觉为中心的方法在大规模 3D-grounded 样本上对 MFM 进行后训练，鼓励模型直接从有限视觉观察中推断深度、大小、位置或空间关系 [10, 7, 21, 39]。尽管这类方法在分布内设定下有效，但近期研究 [27, 16, 40] 表明，其收益往往与训练分布的统计特征强耦合，并可能在场景布局发生变化时退化。以几何为中心的方法则注入显式空间信号，例如深度图、点云或学习到的 3D 表征，以弥补二维视觉输入几何 grounding 较弱的问题 [11, 8, 23, 38]。这些信号固然有用，但会带来非平凡的跨模态对齐挑战 [45]，并且通常需要几何信息丰富的配对数据以及面向专门架构的高成本训练。近期，工具增强的空间推理让模型能够调用工具或任务特定模型（如 3D 重建、新视角渲染、深度估计或位姿估计）来主动获取证据 [46, 20, 9]。然而，这些工具通常返回像素空间观察或低层几何测量，仍需模型通过一条漫长且易错的推理链来组装高层空间结构。因此，带噪或不完整的工具证据往往会被模型“吸收”而不是被质疑，最终导致错误推理结果。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Indeed, biological intelligence (BI) offers a natural blueprint for overcoming the spatial reasoning bottleneck. Decades of cognitive science research suggest that BI does not passively match each incoming egocentric observation in isolation; instead, it compresses local perceptual experience into stable allocentric cognitive maps [3], supporting mental simulation [24, 31, 2]. This suggests a sharper hypothesis: robust spatial reasoning is constrained not merely by coarse 2D perception or limited 3D supervision, but by the absence of an allocentric spatial cognition framework that can be actively invoked, precisely queried, and cross-validated by foundation models. Building on this view, we propose AlloSpatial, an agentic framework that enables reasoning over structured allocentric spatial representations rather than relying solely on egocentric observations.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 的确，生物智能（BI）为克服空间推理瓶颈提供了天然蓝图。几十年的认知科学研究表明，BI 并不会孤立地、被动地匹配每一次输入的自我中心观察；相反，它会把局部感知经验压缩为稳定的非自我中心认知地图 [3]，从而支持心理模拟 [24, 31, 2]。这指向了一个更尖锐的假设：稳健空间推理所受限的，并不仅仅是粗糙的二维感知或有限的三维监督，而是缺少一种可被基础模型主动调用、精确查询并交叉验证的非自我中心空间认知框架。基于这一观点，我们提出 AlloSpatial，一个让模型能够在结构化非自我中心空间表征上推理，而不只是依赖自我中心观察的代理式框架。

### Figure 1. AlloSpatial inference and training pipeline

**Image status:** Not embedded due to strict one-file mode.
**Image status[CN]:** 由于严格单文件模式，图像未嵌入。

**Caption:** Figure 1: AlloSpatial inference and training pipeline. A, At inference time, AlloSpatial takes egocentric videos or multi-view observations and follows a three-stage Spatial Reasoning Harness to invoke World2Mind, acquire allocentric spatial knowledge, and arbitrate evidence before answering. B, To internalize this harness, we distill and filter high-quality harness-following trajectories from proprietary models for supervised cold start, and further optimize the policy with live World2Mind interaction and a Harness-Gated Trajectory Reward.

**Caption[CN]:** 图 1：AlloSpatial 推理与训练流程。A，在推理时，AlloSpatial 接收自我中心视频或多视图观察，并遵循三阶段 Spatial Reasoning Harness 调用 World2Mind、获取非自我中心空间知识，并在作答前完成证据仲裁。B，为了将这一 harness 内化到模型中，我们从闭源模型中蒸馏并筛选高质量、遵循 harness 的轨迹用于监督式冷启动，随后再借助在线 World2Mind 交互以及 Harness-Gated Trajectory Reward 进一步优化策略。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> As illustrated in Fig. 1(A), at the core of AlloSpatial is World2Mind, a plug-and-play cognitive mapping sandbox that transforms egocentric videos or images into queryable allocentric spatial priors. Given semantic categories specified by the agent, World2Mind integrates a robust semantic-geometry alignment pipeline to construct a sparse semantic point cloud. It then distills this point cloud into two complementary cognitive maps: a Landmark Cognitive Map for object-centric topological reasoning and a Route Cognitive Map for traversability, passability, and trajectory reasoning. Its central representation is the proposed Allocentric-Spatial Tree (AST), a directed acyclic graph whose nodes correspond to stable environmental landmarks and whose attributes encode centroid, footprint, principal axes, orientation, height range, and hierarchical containment. Unlike grid maps that discard object identity [41, 35, 30] or abstract semantic graphs that omit metric geometry [15, 29], AST compresses noisy 3D reconstruction into compact and structured spatial memory.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 如图 1(A) 所示，AlloSpatial 的核心是 World2Mind，这是一种即插即用的认知制图沙盒，可将自我中心视频或图像转化为可查询的非自我中心空间先验。给定 agent 指定的语义类别，World2Mind 集成稳健的语义—几何对齐流程，以构建稀疏语义点云。随后，它把该点云蒸馏为两种互补的认知地图：用于以物体为中心的拓扑推理的 Landmark Cognitive Map，以及用于可遍历性、可通行性和轨迹推理的 Route Cognitive Map。其核心表征是提出的非自我中心空间树（AST），这是一种有向无环图，其节点对应于稳定的环境地标，而属性则编码质心、占地范围、主轴、朝向、高度范围和层级包含关系。不同于丢弃物体身份信息的网格地图 [41, 35, 30]，或忽略度量几何的抽象语义图 [15, 29]，AST 将带噪的 3D 重建压缩为紧凑而结构化的空间记忆。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> However, structured spatial priors alone do not guarantee reliable reasoning, especially when reconstruction drift and perception errors often occur. AlloSpatial therefore introduces a three-stage Spatial Reasoning Harness to regulate how models invoke tools, collect evidence, and arbitrate across modalities. The harness first determines whether a question truly requires cognitive mapping, then decouples evidence collection from raw visual inputs, AST-structured text, and optional top-down visualization maps produced by World2Mind, and finally performs geometry-semantics interleaved reasoning to identify conflicts and cross-validate the final answer. To internalize the reasoning harness, we train an AlloSpatial agent instantiated from Qwen3-VL (see Fig. 1(B)). We first use World2Mind within the harness prompt to distill high-quality trajectories from frontier proprietary models, and then apply supervised cold-start fine-tuning to bootstrap tool invocation and reasoning structure. The agent is subsequently optimized with Group Sequence Policy Optimization (GSPO) [48]. Since RL over long tool-use trajectories is vulnerable to reward hacking and redundant tool calls, we introduce a Harness-Gated Trajectory Reward (HGTR) that evaluates the trajectory as a whole rather than isolated actions. HGTR jointly accounts for answer correctness, harness compliance, tool-use validity, and response efficiency, while enforcing two key gates: answer accuracy is credited only when the trajectory follows the required reasoning structure, and tool-use rewards are granted only when valid tool calls contribute to a correct answer. This training strategy stabilizes optimization and enables the agent to acquire efficient and deliberate allocentric spatial reasoning behaviors.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 然而，结构化空间先验本身并不能保证可靠推理，尤其是在经常出现重建漂移和感知误差的情况下。因此，AlloSpatial 引入了一个三阶段 Spatial Reasoning Harness，用于规范模型如何调用工具、收集证据并跨模态进行仲裁。该 harness 首先判断一个问题是否真的需要认知制图；然后把证据收集从原始视觉输入、AST 结构化文本以及 World2Mind 生成的可选俯视可视化地图中解耦出来；最后执行几何—语义交织推理，以识别冲突并交叉验证最终答案。为了将这一推理 harness 内化，我们训练了一个以 Qwen3-VL 实例化的 AlloSpatial agent（见图 1(B)）。首先，我们在 harness prompt 中使用 World2Mind，从前沿闭源模型中蒸馏高质量轨迹；随后施加监督式冷启动微调，以引导工具调用和推理结构。之后，再用 Group Sequence Policy Optimization（GSPO）[48] 对 agent 进行优化。由于对长工具使用轨迹做 RL 容易遭受 reward hacking 和冗余工具调用，我们引入了 Harness-Gated Trajectory Reward（HGTR），按整条轨迹而非孤立动作进行评估。HGTR 同时考虑答案正确性、harness 合规性、工具使用有效性和响应效率，并施加两个关键门控：只有在轨迹遵循所需推理结构时，答案正确性才会获得奖励；只有当有效工具调用确实有助于得到正确答案时，工具使用奖励才会被授予。这一训练策略稳定了优化过程，并使 agent 学会高效且审慎的非自我中心空间推理行为。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> We evaluate AlloSpatial on VSI-Bench [41] and MindCube [35], covering various spatial reasoning tasks across egocentric videos and sparse multi-view images. As a training-free plug-in, World2Mind combined with the Spatial Reasoning Harness consistently improves frontier commercial models, including GPT-5.2, Claude-4.6, and Gemini-3, with overall gains of approximately 5%-18%. Under a “blind” setting in which visual inputs are removed, ASTs alone achieve strong 3D reasoning performance, suggesting that high-quality allocentric priors can elicit spatial mental simulation even without direct visual evidence. After cold-start RL, AlloSpatial agents instantiated from Qwen3-VL surpass larger frontier models and competitive methods across multiple tasks. In summary, our study indicates that coupling structured allocentric representations with an agentic reasoning harness offers a promising route toward overcoming the spatial cognition bottleneck of foundation models.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 我们在 VSI-Bench [41] 与 MindCube [35] 上评估 AlloSpatial，这两个基准覆盖了自我中心视频和稀疏多视图图像上的多种空间推理任务。作为一个免训练插件，World2Mind 与 Spatial Reasoning Harness 的结合，能够稳定提升 GPT-5.2、Claude-4.6 和 Gemini-3 等前沿商业模型，整体增益约为 5%–18%。在移除视觉输入的“blind”设定下，仅 AST 本身就能实现很强的三维推理性能，这说明高质量的非自我中心先验即使没有直接视觉证据，也能激发空间心理模拟。经过冷启动 RL 之后，以 Qwen3-VL 为基础的 AlloSpatial agents 在多项任务上超过了更大的前沿模型和有竞争力的方法。总之，我们的研究表明，将结构化的非自我中心表征与代理式推理 harness 耦合起来，为克服基础模型的空间认知瓶颈提供了一条很有前景的路径。

## 2. Related Work: Spatial Reasoning in Foundation Models

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Recent benchmarks have exposed spatial reasoning as a persistent weakness of MFMs. VSI-Bench [41] and VSI-Super [42] evaluate egocentric video-based spatial intelligence. MindCube [35] probes sparse multi-view cognitive mapping, while other benchmarks [19, 28] extend evaluation to broader text-based and multimodal scenarios. Together, these studies suggest that the bottleneck is not merely visual recognition, but the absence of reasoning-ready spatial mental representations.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 近期基准揭示出，空间推理是 MFM 持续存在的薄弱环节。VSI-Bench [41] 与 VSI-Super [42] 评估基于自我中心视频的空间智能；MindCube [35] 探测稀疏多视图认知制图能力；而其他基准 [19, 28] 则把评测扩展到更广泛的基于文本与多模态的场景。这些研究共同表明，瓶颈并不只是视觉识别，而是缺乏可直接用于推理的空间心理表征。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Vision-centric learning. Vision-centric methods improve spatial reasoning by post-training MFMs with large-scale 3D-grounded supervision. SpatialVLM [7], Cambrian-S [42], and related works [26, 35, 12] construct spatial VQA data from real-world images, videos, or 3D annotations to supervise spatial relation understanding. SpatialReasoner [21] and Spatial-MLLM [39] further introduce intermediate 3D representations or explicit reasoning traces to structure spatial inference. These methods show that spatially grounded supervision can improve benchmark performance. Still, their gains may remain coupled to training-distribution statistics and degrade under shifts in scene layout, viewpoint, or object composition. Recent analyses further suggest that MFMs can exploit semantic shortcuts rather than acquire robust spatial cognition [27, 16, 40].

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> Vision-centric learning。以视觉为中心的方法通过大规模 3D-grounded 监督对 MFM 进行后训练，从而提升空间推理能力。SpatialVLM [7]、Cambrian-S [42] 以及相关工作 [26, 35, 12] 从真实图像、视频或 3D 标注中构建空间 VQA 数据，以监督空间关系理解。SpatialReasoner [21] 和 Spatial-MLLM [39] 进一步引入中间 3D 表征或显式推理轨迹，以组织空间推断。这些方法表明，带空间 grounding 的监督可以提升基准表现。但它们的收益仍可能与训练分布统计特征耦合，并在场景布局、视角或物体组合发生变化时退化。近期分析还指出，MFM 可能只是利用了语义捷径，而不是真正获得了稳健的空间认知 [27, 16, 40]。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Geometry-centric learning. Geometry-centric methods compensate for the weak geometric grounding of 2D inputs by injecting explicit spatial signals. SpatialBot [4] uses RGB-D inputs and depth-centered QA data to improve metric spatial understanding. MM-Spatial [11] and SD-VLM [8] study how depth maps, multi-view observations, and depth-encoded visual features affect 3D reasoning, while N3D-VLM [38] integrates native 3D grounding into a unified MFM. Other works explore point-cloud-enhanced LLMs or reasoning-based segmentation for localization and scene understanding [23, 45]. Although explicit geometry provides useful spatial cues, directly conditioning MFMs on 3D modalities introduces cross-modal alignment challenges and often requires geometry-rich paired data, specialized architectures, and costly training.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Geometry-centric learning。以几何为中心的方法通过注入显式空间信号，来弥补二维输入几何 grounding 不足的问题。SpatialBot [4] 使用 RGB-D 输入和以深度为中心的问答数据来提升度量级空间理解能力。MM-Spatial [11] 和 SD-VLM [8] 研究深度图、多视图观察和深度编码视觉特征如何影响三维推理，而 N3D-VLM [38] 则把原生 3D grounding 融入统一的 MFM。其他工作还探索了点云增强的 LLM，或基于推理的分割方法，以用于定位和场景理解 [23, 45]。虽然显式几何能提供有用的空间线索，但直接让 MFM 以 3D 模态为条件，会引入跨模态对齐挑战，而且往往需要几何信息丰富的配对数据、专门化架构以及高成本训练。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Tool-augmented learning. Tool-augmented methods equip MFMs with external modules for active evidence acquisition. Think3D [46] and pySpatial [20] invoke 3D reconstruction, camera pose estimation, or novel-view rendering for interactive spatial exploration. SpaceTools [9] studies how models coordinate depth, segmentation, and pose tools through reinforcement learning, while SpatialDreamer [5] uses tool hints or visual imagination as intermediate evidence. These approaches mark an important shift from passive perception to active tool use. However, most remain observation-centric: tools typically return rendered views, masks, depth maps, or low-level measurements, leaving the model to assemble high-level spatial structure through long and error-prone reasoning chains. In contrast, AlloSpatial converts noisy 3D reconstructions into compact allocentric representations and couples them with a Spatial Reasoning Harness for tool invocation, modality-decoupled evidence collection, and geometry-semantics arbitration. This enables models to reason over structured allocentric spatial memory rather than isolated egocentric observations or low-level geometric cues.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> Tool-augmented learning。工具增强方法为 MFM 配备外部模块，以主动获取证据。Think3D [46] 和 pySpatial [20] 调用 3D 重建、相机位姿估计或新视角渲染，以进行交互式空间探索。SpaceTools [9] 研究模型如何通过强化学习协调深度、分割和位姿工具，而 SpatialDreamer [5] 则把工具提示或视觉想象作为中间证据。这些方法标志着从被动感知向主动工具使用的重要转变。然而，大多数方法仍然以观察为中心：工具通常返回渲染视图、掩码、深度图或低层测量值，仍需模型通过漫长且易错的推理链来组装高层空间结构。相比之下，AlloSpatial 将带噪的 3D 重建压缩为紧凑的非自我中心表征，并用一个 Spatial Reasoning Harness 将其与工具调用、模态解耦证据收集以及几何—语义仲裁耦合起来。这使模型能够在结构化的非自我中心空间记忆上推理，而非仅依赖孤立的自我中心观察或低层几何线索。

## 3. Methodology

### 3.1. Problem Formulation

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Given an egocentric observation sequence $I = \{I_t\}_{t=1}^{T}$ and a spatial question $q$, our goal is to produce a final answer $\hat{a}$ together with a verifiable spatial reasoning process. We formulate AlloSpatial as a harness-guided tool-using agent $(\pi_\theta, W, H)$, where $\pi_\theta$ denotes the foundation-model policy, $W$ is the proposed World2Mind cognitive mapping sandbox, and $H$ is the Spatial Reasoning Harness. Given $(q, I)$, the agent generates a multi-turn trajectory:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 给定一个自我中心观察序列 $I = \{I_t\}_{t=1}^{T}$ 和一个空间问题 $q$，我们的目标是输出最终答案 $\hat{a}$，并同时给出一个可验证的空间推理过程。我们将 AlloSpatial 形式化为一个由 harness 引导的工具使用 agent $(\pi_\theta, W, H)$，其中 $\pi_\theta$ 表示基础模型策略，$W$ 表示所提出的 World2Mind 认知制图沙盒，$H$ 表示 Spatial Reasoning Harness。给定 $(q, I)$，agent 会生成一条多轮轨迹：

$$
\tau = \langle h_0, u_0, o_0, h_1, u_1, o_1, \ldots, h_K, \hat{a} \rangle. \tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Here $h_k$ is the dialogue history at round $k$, and $u_k \sim \pi_\theta(\cdot \mid h_k)$ is either a natural-language reasoning step or a structured tool call. If $u_k$ is a valid tool call, World2Mind returns an allocentric spatial observation $o_k = W(u_k; I)$; otherwise, $o_k = \varnothing$. The final answer $\hat{a}$ is emitted within a predefined answer tag for reliable parsing and evaluation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 其中，$h_k$ 是第 $k$ 轮的对话历史，$u_k \sim \pi_\theta(\cdot \mid h_k)$ 要么是自然语言推理步骤，要么是结构化工具调用。若 $u_k$ 是有效工具调用，World2Mind 会返回一个非自我中心空间观察 $o_k = W(u_k; I)$；否则，$o_k = \varnothing$。最终答案 $\hat{a}$ 会被放在预定义的 answer tag 中输出，以便可靠地解析和评测。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The harness $H$ constrains the trajectory by specifying the required evidence channels, their ordering, and the cross-modal arbitration steps before final prediction. It therefore turns external allocentric priors into executable and inspectable reasoning evidence, rather than treating tool outputs as unverified context. For a training-free plug-in setting, $H$ is instantiated via prompting. While in the training process, $H$ defines the trajectory structure optimized during RL, as described in Sec. 3.4. Thus, $H$ serves both as an inference-time protocol and as a training-time inductive bias.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> harness $H$ 通过规定所需证据通道、它们的顺序，以及在最终预测之前的跨模态仲裁步骤，对轨迹进行约束。因此，它把外部的非自我中心先验转化为可执行、可检查的推理证据，而不是把工具输出仅仅视为未经验证的上下文。在免训练插件设定下，$H$ 通过 prompting 来实例化；而在训练过程中，$H$ 则定义了 RL 优化所针对的轨迹结构，如第 3.4 节所述。因此，$H$ 同时扮演推理时协议与训练时归纳偏置两种角色。

### 3.2. World2Mind: Allocentric Cognitive Mapping Sandbox

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Rather than reconstructing an exhaustive scene model, World2Mind exposes a query-conditioned cognitive mapping interface. Given an egocentric observation sequence $I$, an open-vocabulary category set $C$, a requested knowledge type $k \in \{\texttt{landmark}, \texttt{route}, \texttt{both}\}$, a footprint format $f \in \{\texttt{rectangle}, \texttt{ellipse}\}$, and a scene type $s \in \{\texttt{indoor}, \texttt{outdoor}\}$, World2Mind returns $M = W(I; C, k, f, s)$, where $M$ denotes the structured allocentric spatial knowledge.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> World2Mind 并不追求重建一个穷尽式的场景模型，而是暴露出一个查询条件化的认知制图接口。给定一个自我中心观察序列 $I$、一个开放词汇类别集合 $C$、请求的知识类型 $k \in \{\texttt{landmark}, \texttt{route}, \texttt{both}\}$、占地表示格式 $f \in \{\texttt{rectangle}, \texttt{ellipse}\}$，以及场景类型 $s \in \{\texttt{indoor}, \texttt{outdoor}\}$，World2Mind 返回 $M = W(I; C, k, f, s)$，其中 $M$ 表示结构化的非自我中心空间知识。

#### 3.2.1. Geometry-Semantic Alignment Pipeline

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We first align geometry and semantics across the egocentric sequence. For each frame $I_t \in \mathbb{R}^{H \times W}$, we estimates a dense depth map $D_t \in \mathbb{R}^{H \times W}$ and camera pose $T_t \in SE(3)$ using monocular geometry models [18, 34], and extracts open-vocabulary semantic masks $\{M_t^c\}_{c \in C}$ with SAM 3 [6]. To suppress unreliable geometry near object boundaries, textureless regions, and poorly reconstructed views, we apply a two-level confidence filter to the predicted confidence map $\Gamma_t \in [0, 1]^{H \times W}$:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们首先在自我中心序列上对齐几何与语义。对每一帧 $I_t \in \mathbb{R}^{H \times W}$，我们利用单目几何模型 [18, 34] 估计稠密深度图 $D_t \in \mathbb{R}^{H \times W}$ 和相机位姿 $T_t \in SE(3)$，并使用 SAM 3 [6] 提取开放词汇语义掩码 $\{M_t^c\}_{c \in C}$。为抑制物体边界附近、无纹理区域以及重建质量较差视图中的不可靠几何，我们对预测置信图 $\Gamma_t \in [0, 1]^{H \times W}$ 施加双层置信过滤：

$$
V_t(u, v) = \mathbf{1}\!\left[\Gamma_t(u, v) > \tau_{\mathrm{px}}\right] \cdot \mathbf{1}\!\left[\bar{\Gamma}_t > \tau_{\mathrm{frm}}\right], \qquad
\bar{\Gamma}_t = \frac{1}{HW} \sum_{u,v} \Gamma_t(u, v). \tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Here $(u, v)$ indexes an image pixel, $V_t(u, v) \in \{0, 1\}$ is the validity mask, and $\tau_{\mathrm{px}}$ and $\tau_{\mathrm{frm}}$ are the pixel- and frame-level confidence thresholds.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 其中，$(u, v)$ 表示图像像素坐标，$V_t(u, v) \in \{0, 1\}$ 是有效性掩码，而 $\tau_{\mathrm{px}}$ 与 $\tau_{\mathrm{frm}}$ 分别是像素级和帧级置信阈值。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Pixels satisfying both constraints are back-projected into the world coordinate system, where $p_t(u, v)$ denotes the 3D point obtained from $D_t(u, v)$ and $T_t$. Aggregating valid points, semantic labels, and colors across frames yields a global semantic point cloud $P = \{(p_i, s_i, rgb_i)\}_{i=1}^{N}$, where $p_i \in \mathbb{R}^{3}$, $s_i \in C$, and $N$ is the number of retained points. To remove sparse outliers caused by boundary leakage and multi-view misalignment, we compute a $K$-nearest-neighbor density score $\rho_i = \frac{1}{K} \sum_{j \in N_K(i)} \|p_i - p_j\|_2^{-1}$ for each point, where $N_K(i)$ denotes the $K$ nearest neighbors of $p_i$, and discard points below a category-specific density percentile. The resulting point cloud is sparse but geometrically reliable, serving as the substrate for allocentric map construction.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 满足两项约束的像素会被反投影到世界坐标系中，其中 $p_t(u, v)$ 表示由 $D_t(u, v)$ 和 $T_t$ 得到的三维点。将跨帧的有效点、语义标签与颜色汇聚起来，就得到全局语义点云 $P = \{(p_i, s_i, rgb_i)\}_{i=1}^{N}$，其中 $p_i \in \mathbb{R}^{3}$、$s_i \in C$，而 $N$ 是保留点的数量。为去除边界泄漏与多视图错位造成的稀疏离群点，我们对每个点计算一个 $K$ 近邻密度分数 $\rho_i = \frac{1}{K} \sum_{j \in N_K(i)} \|p_i - p_j\|_2^{-1}$，其中 $N_K(i)$ 表示 $p_i$ 的 $K$ 个最近邻，并丢弃低于类别特定密度分位数的点。最终得到的点云虽然稀疏，但几何上更可靠，可作为构建非自我中心地图的基础。

#### 3.2.2. Allocentric Mapping

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> World2Mind compresses the filtered $P$ into complementary allocentric representations.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> World2Mind 将过滤后的点云 $P$ 压缩为互补的非自我中心表征。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Landmark mapping with Allocentric-Spatial Tree. For each queried category $c \in C$, World2Mind applies adaptive DBSCAN to separate object instances. Each instance cluster is represented as a node in the Allocentric-Spatial Tree (AST) $T = (V, E)$, where $V$ denotes landmark nodes and $E$ encodes hierarchical containment or support relations. Unlike abstract scene graphs that omit metric geometry [15, 29] or grid maps that discard object identity [41, 35], AST preserves both object semantics and explicit spatial structure. For each node $v \in V$, World2Mind projects its supporting points onto the ground plane and fits a compact footprint:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 基于非自我中心空间树的地标制图。对于每一个查询类别 $c \in C$，World2Mind 使用自适应 DBSCAN 来分离物体实例。每个实例簇都被表示为非自我中心空间树（AST）$T = (V, E)$ 中的一个节点，其中 $V$ 表示地标节点，$E$ 编码层级包含关系或支撑关系。不同于忽略度量几何的抽象场景图 [15, 29]，或丢弃物体身份的网格地图 [41, 35]，AST 同时保留物体语义和显式空间结构。对于每个节点 $v \in V$，World2Mind 将其支持点投影到地平面上，并拟合一个紧凑的占地表示：

$$
\phi(v) = \big(c_x, c_z; a, b, \theta; h_{\min}, h_{\max}; A, n\big). \tag{3}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Here $(c_x, c_z)$ is the top-down centroid, $(a, b)$ are the semi-axes of the fitted ellipse, $\theta$ is its orientation, $(h_{\min}, h_{\max})$ denotes the vertical extent, $A$ is the footprint area, and $n$ is the number of supporting points, used as a confidence proxy. Elliptical footprints are used by default for stable coarse occupancy, while an axis-aligned rectangular format is returned when nearest-boundary computation is required. The resulting AST is serialized into YAML and included in the structured spatial map $M$. This representation turns noisy 3D reconstruction into compact, model-readable spatial memory: foundation models can directly parse object centers, sizes, orientations, and containment relations without specialized 3D adapters, while the coarse footprint parameterization remains robust to local reconstruction noise and reflects the compressed nature of cognitive maps [3, 2].

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 其中，$(c_x, c_z)$ 是俯视质心，$(a, b)$ 是拟合椭圆的半轴，$\theta$ 是其朝向，$(h_{\min}, h_{\max})$ 表示垂直范围，$A$ 是占地面积，$n$ 是支持点数量，可作为置信代理。默认情况下使用椭圆占地表示，以获得稳定的粗粒度占据描述；而当需要计算最近边界距离时，则返回轴对齐矩形格式。生成的 AST 会被序列化成 YAML，并包含在结构化空间图 $M$ 中。这种表征把带噪的 3D 重建转化为紧凑、模型可读的空间记忆：基础模型无需专门的 3D adapter，就能直接解析物体中心、大小、朝向和包含关系；同时，粗粒度占地参数化对局部重建噪声保持稳健，也契合认知地图“压缩式”表征的本质 [3, 2]。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Route mapping. For traversability and path-related queries, World2Mind voxelizes points associated with traversable categories, such as floors, and projects them onto a top-down grid. Each grid cell is labeled as traversable, occupied, or unknown. The camera trajectory $\{T_t\}_{t=1}^{T}$, where $T_t$ denotes the camera pose of frame $I_t$, is projected into the same coordinate system to encode observed motion history and support route-level reasoning.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 路径制图。对于与可遍历性和路径相关的查询，World2Mind 会将与可通行类别（如地面）相关的点体素化，并投影到俯视网格上。每个网格单元被标注为可通行、被占据或未知。相机轨迹 $\{T_t\}_{t=1}^{T}$（其中 $T_t$ 表示帧 $I_t$ 的相机位姿）也会被投影到同一坐标系中，以编码观察到的运动历史并支持路径级推理。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Optional visual rendering. Beyond structured text, World2Mind can return allocentric visualizations as auxiliary global observations, including top-down AST layouts, route maps, and semantic segmentation maps. These renderings provide a compact visual summary of the global scene layout and serve as additional evidence during geometry-semantics arbitration.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 可选视觉渲染。除了结构化文本之外，World2Mind 还可以返回非自我中心可视化结果，作为辅助性的全局观察，包括俯视 AST 布局、路径地图和语义分割地图。这些渲染为全局场景布局提供了紧凑的视觉摘要，并在几何—语义仲裁阶段充当额外证据。

### 3.3. Spatial Reasoning Harness

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Structured allocentric priors are useful but not self-verifying. Directly conditioning on World2Mind output $M$ can induce two failure modes: 1) modality lock-in, where the model prematurely commits to either visual appearance or AST text and ignores conflicting evidence [37, 22]; and 2) over-trust in tool results, where incomplete or noisy reconstructions are treated as ground truth. To mitigate these failures, we design the Spatial Reasoning Harness $H$ as a cyclic protocol:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 结构化的非自我中心先验是有用的，但它们并不会自动完成自我验证。直接以 World2Mind 输出 $M$ 为条件，可能导致两类失败模式：1）模态锁定（modality lock-in），即模型过早地执着于视觉外观或 AST 文本中的某一方，而忽视冲突证据 [37, 22]；2）过度信任工具结果，即把不完整或带噪的重建当成地面真实。为缓解这些问题，我们把 Spatial Reasoning Harness $H$ 设计为一个循环协议：

$$
H: \textsc{Judge} \rightarrow \textsc{Collect} \rightarrow \textsc{Arbitrate} \rightarrow \{\textsc{Refine}, \textsc{Answer}\}. \tag{4}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> At each cycle, the agent decides whether additional allocentric evidence is needed, collects evidence through decoupled channels, and arbitrates geometry-semantics conflicts before either refining the query or committing to the final answer.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在每个循环中，agent 都需要判断是否需要额外的非自我中心证据，随后通过解耦通道收集证据，并在精炼查询或提交最终答案之前，对几何—语义冲突进行仲裁。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Stage I: tool invocation judgment. At reasoning cycle $r$, the agent determines whether the current history $h_r$ is sufficient or whether World2Mind should be queried. Following the reason-then-act principle of ReAct-style agents [43], it first states a spatial hypothesis and the rationale for tool use:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 阶段 I：工具调用判断。在第 $r$ 个推理循环中，agent 需要判断当前历史 $h_r$ 是否已足够，或者是否应当查询 World2Mind。遵循 ReAct 风格 agent 的“先推理、后行动”原则 [43]，它首先陈述一个空间假设以及使用工具的理由：

$$
(d_r, \eta_r) = \textsc{Judge}(q, h_r), \qquad d_r \in \{\texttt{CALL}, \texttt{SKIP}\}. \tag{5}
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Here $d_r$ is the tool-use decision and $\eta_r$ is the current spatial hypothesis. The agent calls World2Mind only when the question requires metric measurement, route topology, viewpoint transformation, or other allocentric spatial evidence, preserving an initial hypothesis that can later be verified or rejected.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 其中，$d_r$ 是是否使用工具的决策，$\eta_r$ 是当前空间假设。只有当问题需要度量测量、路径拓扑、视角变换或其他非自我中心空间证据时，agent 才会调用 World2Mind，同时保留一个之后可以被验证或否决的初始假设。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Stage II: modality-decoupled cue collection. When $d_r = \texttt{CALL}$, the agent generates query parameters $\xi_r = (C_r, k_r, f_r, s_r)$ and obtains a structured spatial map $M_r = W(I; \xi_r)$, where $C_r$ is the queried category set, $k_r$ the requested knowledge type, $f_r$ the footprint format, and $s_r$ the scene type. Evidence is then collected separately from raw visual observations, AST-structured text, and optional top-down maps $\{e_r^{vis}, e_r^{ast}, e_r^{map}\}$. Here, $E_r$ denotes the evidence set at cycle $r$, and $e_r^{vis}$, $e_r^{ast}$, and $e_r^{map}$ denote visual, textual-allocentric, and rendered-map evidence, respectively. This decoupled collection prevents premature fusion and reduces reliance on a single evidence channel.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 阶段 II：模态解耦线索收集。当 $d_r = \texttt{CALL}$ 时，agent 会生成查询参数 $\xi_r = (C_r, k_r, f_r, s_r)$，并获得结构化空间图 $M_r = W(I; \xi_r)$，其中 $C_r$ 是查询类别集合，$k_r$ 是请求的知识类型，$f_r$ 是占地格式，$s_r$ 是场景类型。随后，证据会分别从原始视觉观察、AST 结构化文本以及可选俯视地图 $\{e_r^{vis}, e_r^{ast}, e_r^{map}\}$ 中独立收集。这里，$E_r$ 表示第 $r$ 个循环的证据集，$e_r^{vis}$、$e_r^{ast}$ 和 $e_r^{map}$ 分别表示视觉证据、文本型非自我中心证据和渲染地图证据。这种解耦式收集能够防止过早融合，并降低对单一证据通道的依赖。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Stage III: geometry-semantics interleaved arbitration. The agent then compares visual semantics with geometric evidence from AST and optional maps, identifies conflicts caused by reconstruction drift, missing instances, or false detections, etc., and then decides whether the evidence is sufficient:

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 阶段 III：几何—语义交织仲裁。接着，agent 会把视觉语义与来自 AST 及可选地图的几何证据进行比较，识别由重建漂移、实例缺失、误检等因素造成的冲突，并进一步判断现有证据是否足够：

$$
(\Delta_r, \omega_r, y_r) = \textsc{Arbitrate}(E_r), \qquad y_r \in \{\texttt{REFINE}, \texttt{ANSWER}\}. \tag{6}
$$

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Here $\Delta_r$ denotes detected cross-modal conflicts, $\omega_r$ represents confidence assignments over evidence channels, and $y_r$ is the next action. If $y_r = \texttt{REFINE}$, the agent updates $\xi_r$ and starts another cycle; if $y_r = \texttt{ANSWER}$, it emits the final response within the `<Answer>` tag. In this way, $H$ treats external cognitive maps as falsifiable evidence for reasoning rather than as direct pseudo-labels, enabling iterative, verifiable, and trainable allocentric spatial reasoning.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 其中，$\Delta_r$ 表示检测到的跨模态冲突，$\omega_r$ 表示在不同证据通道上的置信分配，而 $y_r$ 是下一步动作。如果 $y_r = \texttt{REFINE}$，agent 会更新 $\xi_r$ 并开始下一轮循环；如果 $y_r = \texttt{ANSWER}$，则在 `<Answer>` tag 中输出最终响应。通过这种方式，$H$ 把外部认知地图当作可证伪的推理证据，而不是直接的伪标签，从而实现迭代式、可验证、可训练的非自我中心空间推理。

### 3.4. Internalizing the Spatial Reasoning Harness via Reinforcement Learning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> While frontier proprietary models can often follow the Spatial Reasoning Harness $H$ through prompting, open-weight models [1, 36] do not naturally exhibit stable multi-turn tool-use behavior. In preliminary experiments, they frequently produce malformed tool calls, skip cross-modal arbitration, or degenerate into repetitive interaction. We therefore internalize $H$ into the open-weight policy $\pi_\theta$ with supervised cold start followed by RL with live World2Mind execution.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 尽管前沿闭源模型常常能通过 prompting 遵循 Spatial Reasoning Harness $H$，但开源权重模型 [1, 36] 并不会天然表现出稳定的多轮工具使用行为。在初步实验中，它们经常生成格式错误的工具调用、跳过跨模态仲裁，或退化为重复交互。因此，我们先通过监督式冷启动，再结合带实时 World2Mind 执行的 RL，将 $H$ 内化到开源权重策略 $\pi_\theta$ 中。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Supervised cold start. We first use World2Mind and the harness protocol to distill trajectories from proprietary models. We retain trajectories that are answer-correct, structurally valid, and contain non-trivial cross-modal arbitration. Supervised fine-tuning on these traces bootstraps tool-call syntax, AST and route-map parsing, harness stage ordering, and answer-tag formatting, thereby preparing the policy for subsequent optimization with Group Sequence Policy Optimization (GSPO) [48].

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 监督式冷启动。我们首先利用 World2Mind 和 harness 协议，从闭源模型中蒸馏轨迹。我们保留那些答案正确、结构有效，并且包含非平凡跨模态仲裁的轨迹。在这些轨迹上进行监督微调，可以引导模型掌握工具调用语法、AST 和 route map 解析、harness 阶段顺序以及 answer tag 格式，从而为后续使用 Group Sequence Policy Optimization（GSPO）[48] 的优化做好准备。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> GSPO with Harness-Gated Trajectory Reward. To stabilize reinforcement learning over long tool-use trajectories, we introduce a Harness-Gated Trajectory Reward (HGTR) that scores each complete trajectory $\tau$ rather than individual tokens. HGTR combines answer correctness, structural compliance, tool-use effectiveness, and response efficiency:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 带 Harness-Gated Trajectory Reward 的 GSPO。为了稳定对长工具使用轨迹进行强化学习，我们引入了 Harness-Gated Trajectory Reward（HGTR），它对每条完整轨迹 $\tau$ 评分，而非对单个 token 评分。HGTR 将答案正确性、结构合规性、工具使用效果和响应效率综合起来：

$$
R(\tau) = w_{\mathrm{acc}} \tilde{R}_{\mathrm{acc}}(\tau) + w_{\mathrm{str}} R_{\mathrm{str}}(\tau) + w_{\mathrm{tool}} R_{\mathrm{tool}}(\tau) + w_{\mathrm{len}} R_{\mathrm{len}}(\tau). \tag{7}
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Here $w_{\mathrm{acc}}$, $w_{\mathrm{str}}$, $w_{\mathrm{tool}}$, and $w_{\mathrm{len}}$ are reward weights. $R_{\mathrm{str}}(\tau)$ measures harness compliance, including valid tool-call tags, complete stage ordering, explicit arbitration, and the final answer tag. $R_{\mathrm{acc}}(\tau)$ measures answer quality, using exact match for multiple-choice questions and mean relative accuracy for numerical questions following [41]. To prevent malformed trajectories from receiving reward through accidental correct guesses, HGTR applies a structure-gated accuracy:

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 其中，$w_{\mathrm{acc}}$、$w_{\mathrm{str}}$、$w_{\mathrm{tool}}$ 和 $w_{\mathrm{len}}$ 是奖励权重。$R_{\mathrm{str}}(\tau)$ 用于衡量 harness 合规性，包括合法的工具调用标签、完整的阶段顺序、显式仲裁以及最终答案标签。$R_{\mathrm{acc}}(\tau)$ 衡量答案质量，对多选题采用 exact match，对数值题则遵循 [41] 使用平均相对准确率。为防止格式错误的轨迹仅因偶然猜中而获得奖励，HGTR 采用结构门控的准确性：

$$
\tilde{R}_{\mathrm{acc}}(\tau) = R_{\mathrm{acc}}(\tau) \cdot \mathbf{1}[R_{\mathrm{str}}(\tau) \ge \tau_s]. \tag{8}
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Thus, correctness is credited only when the trajectory satisfies the harness format. HGTR further uses a correctness-tied tool-use reward:

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 因此，只有当轨迹满足 harness 格式要求时，正确性才会获得奖励。HGTR 还进一步使用了与正确性绑定的工具使用奖励：

$$
R_{\mathrm{tool}}(\tau) = \alpha \, \tilde{R}_{\mathrm{acc}}(\tau)\mathbf{1}[\mathrm{ValidCall}(\tau)] - \gamma \max(0, n_W(\tau) - n^\star). \tag{9}
$$

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Here $\mathrm{ValidCall}(\tau)$ indicates whether World2Mind is invoked with valid syntax and task-relevant arguments, $n_W(\tau)$ is the number of calls, $n^\star$ is a soft call budget, and $\alpha, \gamma$ control the tool reward and overuse penalty. This reward grants tool-use credit only when a valid invocation contributes to a structurally valid and correct answer, while discouraging redundant reconstruction once sufficient allocentric evidence is available. Finally, $R_{\mathrm{len}}(\tau)$ penalizes excessive model-generated tokens while masking out tool-returned ASTs, route maps, and visualization metadata. Overall, HGTR guides the agent toward trajectories that are answer-correct, harness-compliant, tool-efficient, and verifiable.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 其中，$\mathrm{ValidCall}(\tau)$ 表示 World2Mind 是否被以合法语法和与任务相关的参数调用，$n_W(\tau)$ 表示调用次数，$n^\star$ 表示一个软调用预算，而 $\alpha, \gamma$ 控制工具奖励与过度使用惩罚。该奖励只有在有效调用确实帮助产生结构正确且答案正确的结果时才给予工具使用信用；一旦已有足够的非自我中心证据，则会抑制冗余重建。最后，$R_{\mathrm{len}}(\tau)$ 会惩罚过多的模型生成 token，同时屏蔽工具返回的 AST、路径地图和可视化元数据。总体而言，HGTR 会把 agent 引导到那些答案正确、harness 合规、工具高效且可验证的轨迹上。

## 4. Experiments

### 4.1. Experimental Setup

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Datasets. We evaluate AlloSpatial on the official Tiny split of VSI-Bench [41] and MindCube [35], containing 392 and 1,050 questions, respectively. For training, we sample data from VSI-590K and the MindCube training set. The cold-start stage distills multi-turn tool-use trajectories from GPT-5.2 and Claude-4.6-Opus with World2Mind and the Spatial Reasoning Harness, followed by filtering for answer correctness, harness compliance, and valid tool invocation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 数据集。我们在 VSI-Bench [41] 和 MindCube [35] 的官方 Tiny 划分上评估 AlloSpatial，二者分别包含 392 和 1,050 个问题。训练时，我们从 VSI-590K 和 MindCube 训练集中采样数据。冷启动阶段会借助 World2Mind 和 Spatial Reasoning Harness，从 GPT-5.2 与 Claude-4.6-Opus 蒸馏多轮工具使用轨迹，随后再依据答案正确性、harness 合规性以及工具调用有效性进行筛选。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Metrics. Following [41, 35], we report pass@1 accuracy for multiple-choice questions and mean relative accuracy (MRA) for numerical questions. The overall score is the unweighted average over all task types within each benchmark. For the training-free setting on VSI-Bench, we uniformly sample up to 32 frames from each video. For the post-trained AlloSpatial agents and other baselines, we follow the limited-observation setting of Think3D [46] and uniformly sample 7 frames, testing performance under sparse visual inputs. We further analyze the effect of frame number in Sec. 4.4.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 指标。遵循 [41, 35]，我们对多选题报告 pass@1 accuracy，对数值题报告平均相对准确率（MRA）。总体分数是各基准内所有任务类型的无权平均。对于 VSI-Bench 上的免训练设定，我们从每个视频中均匀采样最多 32 帧。对于后训练的 AlloSpatial agents 和其他基线，我们遵循 Think3D [46] 的有限观察设定，统一采样 7 帧，以测试稀疏视觉输入下的性能。我们还在第 4.4 节进一步分析了帧数的影响。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Baselines. We compare 1) Proprietary models including GPT-5.2, Claude-4.6-Opus, and Gemini-3-Pro; 2) Open-source models including Qwen3-VL [1], InternVL3.5 [36], and Gemma-4 [14]; 3) Specialized spatial models including Spatial-MLLM [39], Cambrian-S [42], and Think3D [46].

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 基线。我们比较三类方法：1）闭源模型，包括 GPT-5.2、Claude-4.6-Opus 和 Gemini-3-Pro；2）开源模型，包括 Qwen3-VL [1]、InternVL3.5 [36] 和 Gemma-4 [14]；3）专门的空间推理模型，包括 Spatial-MLLM [39]、Cambrian-S [42] 和 Think3D [46]。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Training details. We instantiate AlloSpatial from Qwen3-VL-4B-Instruct and Qwen3-VL-8B-Instruct [1]. The 4B and 8B agents are trained for 600 and 400 RL steps, respectively, using 4.8K and 2.4K unique prompts, with 8 sampled rollouts per prompt. Detailed hyperparameters, World2Mind service configuration, and computational costs are provided in the Appendices A, B, and E.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 训练细节。我们基于 Qwen3-VL-4B-Instruct 和 Qwen3-VL-8B-Instruct [1] 实例化 AlloSpatial。4B 和 8B agents 分别训练 600 和 400 个 RL step，使用 4.8K 和 2.4K 个 unique prompt，并且每个 prompt 采样 8 条 rollout。更详细的超参数、World2Mind 服务配置和计算成本见附录 A、B 与 E。

### Table 1. Results of AlloSpatial under the training-free setting on the VSI-Bench and MindCube benchmarks

**Image status:** Table image not embedded due to strict one-file mode; full searchable transcription is preserved below.
**Image status[CN]:** 由于严格单文件模式，表格截图未嵌入；下方保留完整可搜索转录。

**Caption:** Table 1: Results of AlloSpatial under the training-free setting on the VSI-Bench [41] and MindCube [35] benchmarks (tiny split). For VSI-Bench, we uniformly use 32 input frames.

**Caption[CN]:** 表 1：AlloSpatial 在 VSI-Bench [41] 和 MindCube [35] 基准（tiny split）上的免训练结果。对 VSI-Bench，我们统一使用 32 个输入帧。

| Models | VSI Overall | Obj. Count | Abs. Dist. | Obj. Size | Room Size | Rel. Dist. | Rel. Dir. | Route Plan | Appr. Order | MindCube Overall | Around | Among | Rotation |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Proprietary Foundation Models w/o. AlloSpatial** |  |  |  |  |  |  |  |  |  |  |  |  |  |
| GPT-5.2 | 46.7 | 52.5 | 34.9 | 67.5 | 50.6 | 42.0 | 40.7 | 34.7 | 51.0 | 49.9 | 62.4 | 45.2 | 48.5 |
| Claude-4.6-Opus | 38.4 | 46.9 | 18.5 | 62.1 | 26.8 | 40.0 | 47.2 | 34.7 | 30.6 | 48.5 | 58.8 | 50.7 | 29.0 |
| Gemini-3-Pro | 55.2 | 47.8 | 32.1 | 71.3 | 55.0 | 54.0 | 44.8 | 57.1 | 79.6 | 75.1 | 77.2 | 68.2 | 93.0 |
| **Proprietary Foundation Models w./ AlloSpatial** |  |  |  |  |  |  |  |  |  |  |  |  |  |
| GPT-5.2 | 54.0 (↑7.3) | 47.4 (↓5.1) | 33.4 (↓1.5) | 63.3 (↓4.2) | 52.4 (↑1.8) | 64.0 (↑22.0) | 41.1 (↑0.4) | 51.0 (↑16.3) | 79.6 (↑28.6) | 54.6 (↑4.7) | 60.4 (↓2.0) | 47.7 (↑2.5) | 68.0 (↑19.5) |
| Claude-4.6-Opus | 56.0 (↑17.7) | 59.0 (↑12.0) | 34.3 (↑15.8) | 67.3 (↑5.2) | 54.8 (↑28.0) | 64.0 (↑24.0) | 62.7 (↑15.6) | 65.3 (↑30.6) | 40.8 (↑10.2) | 62.9 (↑14.4) | 82.4 (↑23.6) | 60.8 (↑10.1) | 45.0 (↑16.0) |
| Gemini-3-Pro | 61.0 (↑5.8) | 51.8 (↑4.1) | 36.8 (↑4.7) | 57.7 (↓13.5) | 62.6 (↑7.6) | 62.0 (↑8.0) | 67.7 (↑22.9) | 65.3 (↑8.2) | 83.7 (↑4.1) | 81.6 (↑6.5) | 86.0 (↑8.8) | 75.8 (↑7.6) | 93.5 (↑0.5) |

### Table 2. Evaluation results on the VSI-Bench benchmark

**Image status:** Table image not embedded due to strict one-file mode; full searchable transcription is preserved below.
**Image status[CN]:** 由于严格单文件模式，表格截图未嵌入；下方保留完整可搜索转录。

**Caption:** Table 2: Evaluation results on the VSI-Bench benchmark (tiny split). Following the setting of Think3D [46], all models are evaluated with 7 input frames to assess spatial reasoning under limited egocentric observations. `†`: Results are directly taken from the original paper. Green shades denote the top-1, top-2, and top-3 performance within each metric.

**Caption[CN]:** 表 2：VSI-Bench 基准（tiny split）上的评测结果。遵循 Think3D [46] 的设定，所有模型都使用 7 个输入帧进行评测，以衡量有限自我中心观察下的空间推理能力。`†`：结果直接取自原论文。绿色阴影表示各指标中的前 1、前 2 和前 3 表现。

| Rank | Models | Overall | Avg. | Obj. Count | Abs. Dist. | Obj. Size | Room Size | Avg. Rel. Dist. | Rel. Dir. | Route Plan | Appr. Order |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 11 | GPT-5.2 | 37.7 | 36.4 | 28.6 | 24.3 | 52.3 | 40.6 | 39.0 | 42.0 | 28.4 | 42.9 |
| 8 | Gemini-2.5-Pro | 46.2 | 39.4 | 34.7 | 14.3 | 56.3 | 52.4 | 53.0 | 52.0 | 45.7 | 38.8 |
| 9 | Gemini-3-Pro | 45.2 | 32.2 | 29.4 | 12.6 | 38.3 | 48.4 | 58.3 | 56.0 | 52.7 | 49.0 |
| 12 | Gemma-4-E4B | 33.5 | 30.1 | 19.6 | 24.5 | 33.1 | 43.2 | 36.9 | 38.0 | 40.0 | 30.6 |
| 6 | InternVL3.5-4B | 48.8 | 50.9 | 77.3 | 19.4 | 60.4 | 46.4 | 46.8 | 38.0 | 47.1 | 40.8 |
| 10 | Qwen3-VL-4B | 45.1 | 47.7 | 44.3 | 34.5 | 64.4 | 47.8 | 42.4 | 36.0 | 37.8 | 24.5 |
| 7 | Qwen3-VL-8B | 48.5 | 51.5 | 50.4 | 40.2 | 67.5 | 48.0 | 45.5 | 36.0 | 44.1 | 30.6 |
| 3 | Qwen3-VL-32B | 53.1 | 55.3 | 60.6 | 35.1 | 71.5 | 54.0 | 50.9 | 46.0 | 51.4 | 36.7 |
| 5 | Spatial-MLLM-4B [39] | 49.1 | 53.0 | 76.5 | 27.0 | 57.9 | 50.6 | 45.2 | 44.0 | 40.9 | 38.8 |
| 4 | Cambrian-S-3B [42] | 49.5 | 51.7 | 67.1 | 22.6 | 73.8 | 43.2 | 47.3 | 54.0 | 37.1 | 26.5 |
| - | Think3D-4B† [46] | - | - | - | - | - | - | 45.4 | 44.7 | 39.0 | 36.7 |
| 2 | AlloSpatial-4B (Ours) | 53.5 | 56.3 | 54.1 | 42.3 | 68.8 | 60.0 | 50.8 | 50.0 | 59.3 | 34.7 |
| 1 | AlloSpatial-8B (Ours) | 54.2 | 47.8 | 46.1 | 26.0 | 65.6 | 53.4 | 60.6 | 52.0 | 64.1 | 46.9 |

### Table 3. Evaluation on the MindCube (tiny split)

**Image status:** Table image not embedded due to strict one-file mode; full searchable transcription is preserved below.
**Image status[CN]:** 由于严格单文件模式，表格截图未嵌入；下方保留完整可搜索转录。

**Caption:** Table 3: Evaluation on the MindCube (tiny split).

**Caption[CN]:** 表 3：MindCube（tiny split）上的评测。

| Rank | Models | Overall | Around | Among | Rotation |
|---|---|---:|---:|---:|---:|
| 2 | Gemini-2.5-Pro | 57.9 | 67.2 | 43.8 | 88.5 |
| 5 | Gemma-4-E4B | 37.3 | 37.6 | 38.0 | 35.0 |
| 6 | InternVL3.5-4B | 36.6 | 41.6 | 35.3 | 34.0 |
| 8 | Qwen3-VL-4B | 28.3 | 40.4 | 20.8 | 35.5 |
| 4 | Spatial-MLLM-4B [39] | 39.5 | 52.0 | 36.3 | 33.5 |
| 7 | Cambrian-S-3B [42] | 33.2 | 34.4 | 34.5 | 28.0 |
| 3 | Think3D-4B† [46] | 44.0 | 42.5 | 37.5 | 42.5 |
| 1 | AlloSpatial-4B (Ours) | 69.1 | 82.0 | 65.0 | 65.5 |

### Figure 2. VSI-Bench performance under different input-frame number

**Image status:** Not embedded due to strict one-file mode.
**Image status[CN]:** 由于严格单文件模式，图像未嵌入。

**Caption:** Figure 2: VSI-Bench performance under different input-frame number.

**Caption[CN]:** 图 2：不同输入帧数量下的 VSI-Bench 表现。

### Figure 3. Text-only spatial reasoning with allocentric priors

**Image status:** Not embedded due to strict one-file mode.
**Image status[CN]:** 由于严格单文件模式，图像未嵌入。

**Caption:** Figure 3: Text-only spatial reasoning with allocentric priors. VSI-Bench performance under the “blind” setting, where visual inputs are removed.

**Caption[CN]:** 图 3：利用非自我中心先验的纯文本空间推理。在移除视觉输入的“blind”设定下的 VSI-Bench 表现。

### 4.2. AlloSpatial Improves Proprietary Foundation Models for Spatial Reasoning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We first evaluate AlloSpatial as a training-free plug-in for proprietary models by exposing World2Mind $W$ and the Spatial Reasoning Harness $H$ through prompting.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们首先把 AlloSpatial 作为闭源模型的免训练插件来评估，即通过 prompting 将 World2Mind $W$ 与 Spatial Reasoning Harness $H$ 暴露给模型。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Consistent improvement across benchmarks. As shown in Tab. 1, AlloSpatial improves GPT-5.2, Claude-4.6-Opus, and Gemini-3-Pro on VSI-Bench by +7.3, +17.7, and +5.8 overall points, respectively, and on MindCube by +4.7, +14.4, and +6.5 points. The gains are concentrated on tasks that require allocentric structure, such as relative direction, route planning, and viewpoint-dependent rotation, while tasks solvable from local visual evidence show smaller or occasionally negative changes. This pattern suggests that World2Mind is most beneficial when direct egocentric perception is insufficient, and the model must reason over stable spatial relations beyond the observed view. A complete reasoning trace is shown in Fig. 4, and additional analysis for AlloSpatial’s reasoning cases are illustrated in Appendix D.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 跨基准的一致提升。如表 1 所示，AlloSpatial 在 VSI-Bench 上分别将 GPT-5.2、Claude-4.6-Opus 和 Gemini-3-Pro 的总体表现提升了 +7.3、+17.7 和 +5.8 个点；在 MindCube 上则分别提升 +4.7、+14.4 和 +6.5 个点。这些收益主要集中在需要非自我中心结构的任务上，例如相对方向、路径规划和依赖视角的旋转问题；而那些仅靠局部视觉证据即可解决的任务，提升较小，甚至偶尔出现负变化。这一模式说明，当直接的自我中心感知不足时，World2Mind 最能发挥作用，因为模型此时必须在超出当前观察视图的稳定空间关系上进行推理。完整推理轨迹见图 4，更多 AlloSpatial 推理案例分析见附录 D。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> ASTs provide effective allocentric reasoning evidence. We further test whether the gain comes from structured spatial knowledge itself by evaluating VSI-Bench in a text-only “blind” setting [41]. Fig. 3 shows that AST text substantially improves blind spatial reasoning over text-only baselines, especially on object size and route planning. This supports the role of AST as a compact allocentric prior that enables models to reason over spatial structure without directly observing the scene. Together with the full-input results, the blind setting suggests that the critical signal is not merely additional visual context, but the structured spatial organization supplied by World2Mind.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> AST 提供了有效的非自我中心推理证据。我们进一步通过在纯文本“blind”设定 [41] 下评估 VSI-Bench，来测试性能增益是否来自结构化空间知识本身。图 3 表明，相比纯文本基线，AST 文本能显著提升盲态空间推理，尤其是在物体大小和路径规划任务上。这支持了 AST 作为一种紧凑非自我中心先验的角色，即使不直接观察场景，它也能使模型在空间结构上进行推理。结合完整视觉输入时的结果来看，blind 设定说明真正关键的信号并不仅仅是额外的视觉上下文，而是 World2Mind 提供的结构化空间组织。

### 4.3. Trained AlloSpatial Agents Outperform General and Spatially Specialized Models

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We next compare the trained AlloSpatial agents with proprietary models, open-source MFMs, and specialized spatial reasoning models. As shown in Tab. 2, AlloSpatial-8B achieves the best overall score on VSI-Bench, while AlloSpatial-4B ranks second. Both variants outperform proprietary models such as GPT-5.2, Gemini-2.5-Pro, and Gemini-3-Pro. Notably, AlloSpatial-4B and AlloSpatial-8B also surpass Qwen3-VL-32B, despite using substantially smaller backbones. AlloSpatial also compares favorably with spatially specialized models. On VSI-Bench, AlloSpatial-8B improves over Spatial-MLLM-4B and Cambrian-S-3B by +5.1 and +4.7 overall points, respectively, while AlloSpatial-4B also exceeds both baselines. This is notable because Spatial-MLLM and Cambrian-S rely on large-scale spatial grounding data, whereas AlloSpatial uses a much smaller set of unique training prompts and acquires spatial competence through structured tool interaction and trajectory-level optimization. These results suggest that allocentric spatial memory and verifiable reasoning can improve data efficiency compared with purely supervision-driven spatial learning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 接下来，我们将训练后的 AlloSpatial agents 与闭源模型、开源 MFM 以及专门的空间推理模型进行比较。如表 2 所示，AlloSpatial-8B 在 VSI-Bench 上取得最佳总体分数，而 AlloSpatial-4B 排名第二。两种变体都优于 GPT-5.2、Gemini-2.5-Pro 和 Gemini-3-Pro 等闭源模型。值得注意的是，尽管所用 backbone 显著更小，AlloSpatial-4B 与 AlloSpatial-8B 仍然超过了 Qwen3-VL-32B。AlloSpatial 与专门的空间模型相比也表现出优势。在 VSI-Bench 上，AlloSpatial-8B 相比 Spatial-MLLM-4B 和 Cambrian-S-3B 的总体分数分别提高了 +5.1 和 +4.7，而 AlloSpatial-4B 也同样超过这两个基线。这一点尤为值得注意，因为 Spatial-MLLM 和 Cambrian-S 依赖大规模空间 grounding 数据，而 AlloSpatial 只使用了数量更小的 unique training prompts，并通过结构化工具交互和轨迹级优化获得空间能力。这些结果表明，相比纯监督驱动的空间学习，非自我中心空间记忆与可验证推理能够带来更高的数据效率。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Considering task-level performance, AlloSpatial shows greater improvements on relational and viewpoint-dependent tasks, such as relative direction, route planning, appearance order, and MindCube tasks. As illustrated in Tab. 3, AlloSpatial-4B reaches 69.1% overall accuracy on MindCube, clearly outperforming Gemini-2.5-Pro, Think3D-4B, Spatial-MLLM-4B, and Cambrian-S-3B, with particularly large gains on Around and Among. In contrast, improvements on precise numerical estimation tasks, such as absolute distance and object counting, are less uniform. This pattern is consistent with the design of World2Mind: the AST and route maps provide robust coarse allocentric structure for relational reasoning, but the current reconstruction pipeline still limits fine-grained metric accuracy. Overall, AlloSpatial agents are most effective when the task benefits from a stable allocentric organization rather than exact metric reconstruction.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 从任务级表现来看，AlloSpatial 在关系型任务和依赖视角的任务上提升更大，例如相对方向、路径规划、appearance order 以及 MindCube 任务。如表 3 所示，AlloSpatial-4B 在 MindCube 上达到 69.1% 的总体准确率，明显优于 Gemini-2.5-Pro、Think3D-4B、Spatial-MLLM-4B 和 Cambrian-S-3B，尤其在 Around 与 Among 上增益很大。相比之下，在绝对距离、物体计数等精确数值估计任务上的提升则没有那么一致。这一模式与 World2Mind 的设计是吻合的：AST 和 route maps 为关系推理提供了稳健的粗粒度非自我中心结构，但当前重建流程仍会限制细粒度度量精度。总体而言，当任务主要受益于稳定的非自我中心组织，而非精确度量重建时，AlloSpatial agents 的效果最好。

### Figure 4. Reasoning trace produced by AlloSpatial

**Image status:** Not embedded due to strict one-file mode.
**Image status[CN]:** 由于严格单文件模式，图像未嵌入。

**Caption:** Figure 4: Reasoning trace produced by AlloSpatial.

**Caption[CN]:** 图 4：AlloSpatial 生成的推理轨迹。

### Table 4. Ablation results of AlloSpatial-4B

**Image status:** Table image not embedded due to strict one-file mode; full searchable transcription is preserved below.
**Image status[CN]:** 由于严格单文件模式，表格截图未嵌入；下方保留完整可搜索转录。

**Caption:** Table 4: Ablation results of AlloSpatial-4B. We compare Qwen3-VL-4B variants using the same training data as QA pairs for SFT and RL, and report AlloSpatial-4B at Stage-1 (SFT cold start) and Stage-2 (RL).

**Caption[CN]:** 表 4：AlloSpatial-4B 的消融结果。我们比较使用相同训练数据、以 QA pairs 形式进行 SFT 和 RL 的 Qwen3-VL-4B 变体，并报告 AlloSpatial-4B 的 Stage-1（SFT 冷启动）和 Stage-2（RL）结果。

| Variants | VSI-Bench | MindCube | Tokens |
|---|---:|---:|---:|
| **Qwen3-VL-4B** |  |  |  |
| Instruct | 45.1 | 28.3 | - |
| Thinking | 45.5 (↑0.4) | 36.1 (↑7.8) | 1064 |
| w./ SFT on QAs | 43.1 (↓2.0) | 53.9 (↑25.6) | - |
| w./ RL on QAs | 46.2 (↑1.1) | 53.0 (↑24.7) | - |
| **AlloSpatial-4B** |  |  |  |
| Stage-1 (SFT) | 38.2 (↓6.9) | 52.0 (↑23.7) | - |
| Stage-2 (RL) | 53.5 (↑8.4) | 69.1 (↑40.8) | 358 |

### 4.4. Ablation Studies and Additional Results

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Effect of input-frame number. We study how AlloSpatial behaves under different observation budgets. Fig. 2 reports performance with 0, 3, 7, 15, and 24 uniformly sampled input frames. AlloSpatial shows the clearest advantage when visual observations are sparse. In the 0-frame setting, where the model relies only on structured AST text, AlloSpatial improves over Qwen3-VL by +18.2 points. With only 3 and 7 frames, it remains consistently stronger than both Qwen3-VL and GPT-5.2, reaching 50.0 and 53.5 overall, respectively. As the number of frames increases, the gap to Qwen3-VL narrows, suggesting that dense visual coverage can partially compensate for missing allocentric memory. This trend indicates that AlloSpatial is particularly effective under limited observations.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 输入帧数量的影响。我们研究了 AlloSpatial 在不同观察预算下的表现。图 2 报告了在 0、3、7、15 和 24 个均匀采样输入帧下的性能。当视觉观察稀疏时，AlloSpatial 的优势最明显。在 0 帧设定下，也就是模型仅依赖结构化 AST 文本时，AlloSpatial 相比 Qwen3-VL 提升了 +18.2 个点。在只有 3 帧和 7 帧时，它也持续强于 Qwen3-VL 和 GPT-5.2，总体分数分别达到 50.0 和 53.5。随着帧数增加，与 Qwen3-VL 的差距逐渐缩小，这说明稠密视觉覆盖可以在一定程度上弥补缺失的非自我中心记忆。这一趋势表明，AlloSpatial 在有限观察条件下尤其有效。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Comparison with general thinking mode. We next compare AlloSpatial with the general thinking of Qwen3-VL-4B. As shown in Tab. 4, enabling thinking improves Qwen3-VL-4B on MindCube from 28.3 to 36.1, but brings only a marginal gain on VSI-Bench (45.1 → 45.5) while increasing the average response length to 1064 tokens. In contrast, AlloSpatial-4B after RL reaches 53.5 on VSI-Bench and 69.1 on MindCube with only average 358 tokens. This suggests that the improvement does not come from longer chain-of-thought alone. Instead, the harnessed process provides a more efficient reasoning structure by grounding intermediate reasoning in explicit allocentric evidence.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 与通用 thinking mode 的比较。接着，我们将 AlloSpatial 与 Qwen3-VL-4B 的通用 thinking 模式进行比较。如表 4 所示，启用 thinking 能将 Qwen3-VL-4B 在 MindCube 上的表现从 28.3 提高到 36.1，但在 VSI-Bench 上仅带来边际提升（45.1 → 45.5），同时平均响应长度增加到 1064 个 token。相比之下，经过 RL 的 AlloSpatial-4B 在平均仅 358 个 token 的情况下，就在 VSI-Bench 上达到 53.5，在 MindCube 上达到 69.1。这说明性能提升并不仅仅来自更长的 chain-of-thought；更关键的是，harness 化过程通过把中间推理建立在显式的非自我中心证据之上，提供了更高效的推理结构。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Comparison with QA-only training. We further perform the same two-stage training schedule on standard QA pairs constructed from the same data, to isolate whether the gains of AlloSpatial come from direct answer supervision or potential benchmark leakage. As shown in Tab. 4, QA-only SFT substantially improves MindCube from 28.3 to 53.9, but decreases VSI-Bench from 45.1 to 43.1. This suggests that answer supervision alone can fit certain benchmark patterns, but does not consistently improve spatial reasoning. QA-only RL slightly improves VSI-Bench to 46.2 and maintains a strong MindCube score of 53.0, yet remains well below AlloSpatial Stage-2, which reaches 53.5 on VSI-Bench and 69.1 on MindCube. This gap indicates that RL over QA supervision alone is insufficient; the main improvement comes from optimizing complete tool-use trajectories that follow the Spatial Reasoning Harness and interact with World2Mind during reasoning.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 与仅 QA 训练的比较。我们进一步在由相同数据构建的标准 QA pairs 上执行相同的两阶段训练日程，以区分 AlloSpatial 的收益究竟来自直接答案监督，还是潜在的 benchmark leakage。如表 4 所示，仅 QA 的 SFT 能把 MindCube 从 28.3 大幅提升到 53.9，但却把 VSI-Bench 从 45.1 降到 43.1。这说明，仅靠答案监督可以拟合某些 benchmark 模式，但并不能稳定提升空间推理。仅 QA 的 RL 将 VSI-Bench 小幅提升到 46.2，同时保持了较强的 MindCube 分数 53.0，但仍明显低于 AlloSpatial Stage-2（后者在 VSI-Bench 上达到 53.5，在 MindCube 上达到 69.1）。这一差距表明，仅在 QA 监督上做 RL 是不够的；主要提升来自于优化那些遵循 Spatial Reasoning Harness、并在推理过程中与 World2Mind 交互的完整工具使用轨迹。

## 5. Conclusion & Limitations

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We presented AlloSpatial, an agentic framework that equips MFMs with allocentric spatial reasoning capability through the proposed World2Mind cognitive mapping sandbox and carefully designed spatial reasoning harness. Experiments on VSI-Bench and MindCube show that AlloSpatial improves proprietary models in a training-free setting and enables compact open-weight agents to outperform larger general-purpose and spatially specialized baselines. A remaining limitation of our study is numerical reasoning: current World2Mind representations provide robust allocentric structure, but reconstruction drift and imperfect metric calibration can still limit precise distance, size, and counting estimates. Future work may address this by incorporating stronger metric calibration and uncertainty-aware reconstruction into the cognitive mapping backend.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们提出了 AlloSpatial，这是一种代理式框架，通过所提出的 World2Mind 认知制图沙盒以及精心设计的空间推理 harness，为 MFM 赋予非自我中心空间推理能力。在 VSI-Bench 和 MindCube 上的实验表明，AlloSpatial 在免训练设定下能够提升闭源模型，并使紧凑的开源权重 agents 超过更大的通用基线与空间专门基线。我们研究中仍然存在的一个限制是数值推理：当前的 World2Mind 表征能够提供稳健的非自我中心结构，但重建漂移和不完美的度量校准仍会限制精确距离、大小与计数估计。未来工作可以通过在认知制图后端中引入更强的度量校准和不确定性感知重建来解决这一问题。

## References

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The source contains 48 references. Following the reader policy, bibliography entries are preserved in their original searchable form rather than translated line by line.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 原文共包含 48 条参考文献。按照 reader 规范，参考文献条目保留其原始、可搜索形式，不逐条翻译。

1. Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang Gao, Chunjiang Ge, et al. Qwen3-vl technical report. arXiv preprint arXiv:2511.21631, 2025.
2. Jacob LS Bellmund, Peter Gärdenfors, Edvard I Moser, and Christian F Doeller. Navigating cognition: Spatial codes for human thinking. Science, 362(6415):eaat6766, 2018.
3. Neil Burgess. Spatial memory: how egocentric and allocentric combine. Trends in cognitive sciences, 10(12):551–557, 2006.
4. Wenxiao Cai, Iaroslav Ponomarenko, Jianhao Yuan, Xiaoqi Li, Wankou Yang, Hao Dong, and Bo Zhao. Spatialbot: Precise spatial understanding with vision language models. In 2025 IEEE International Conference on Robotics and Automation (ICRA), pages 9490–9498. IEEE, 2025.
5. Meng Cao, Xingyu Li, Xue Liu, Ian Reid, and Xiaodan Liang. Spatialdreamer: Incentivizing spatial reasoning via active mental imagery. arXiv preprint arXiv:2512.07733, 2025.
6. Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath, Ronghang Hu, Didac Suris, Chaitanya Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew Huang, et al. Sam 3: Segment anything with concepts. arXiv preprint arXiv:2511.16719, 2025.
7. Boyuan Chen, Zhuo Xu, Sean Kirmani, Brain Ichter, Dorsa Sadigh, Leonidas Guibas, and Fei Xia. Spatialvlm: Endowing vision-language models with spatial reasoning capabilities. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 14455–14465, 2024.
8. Pingyi Chen, Yujing Lou, Shen Cao, Jinhui Guo, Lubin Fan, Yue Wu, Lin Yang, Lizhuang Ma, and Jieping Ye. Sd-vlm: Spatial measuring and understanding with depth-encoded vision-language models. arXiv preprint arXiv:2509.17664, 2025.
9. Siyi Chen, Mikaela Angelina Uy, Chan Hee Song, Faisal Ladhak, Adithyavairavan Murali, Qing Qu, Stan Birchfield, Valts Blukis, and Jonathan Tremblay. Spacetools: Tool-augmented spatial reasoning via double interactive rl. arXiv preprint arXiv:2512.04069, 2025.
10. An-Chieh Cheng, Hongxu Yin, Yang Fu, Qiushan Guo, Ruihan Yang, Jan Kautz, Xiaolong Wang, and Sifei Liu. Spatialrgpt: Grounded spatial reasoning in vision-language models. Advances in Neural Information Processing Systems, 37:135062–135093, 2024.
11. Erik Daxberger, Nina Wenzel, David Griffiths, Haiming Gang, Justin Lazarow, Gefen Kohavi, Kai Kang, Marcin Eichner, Yinfei Yang, Afshin Dehghan, et al. Mm-spatial: Exploring 3d spatial understanding in multimodal llms. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 7395–7408, 2025.
12. Nianchen Deng, Lixin Gu, Shenglong Ye, Yinan He, Zhe Chen, Songze Li, Haomin Wang, Xingguang Wei, Tianshuo Yang, Min Dou, et al. Internspatial: A comprehensive dataset for spatial reasoning in vision-language models. arXiv preprint arXiv:2506.18385, 2025.
13. Google. Gemini 3.1 pro: Best for complex tasks and bringing creative concepts to life. https://deepmind.google/models/gemini/pro/, 2026.
14. Google DeepMind. Gemma 4, 2026. URL https://deepmind.google/models/gemma/gemma-4/. Accessed: 2026-05-06.
15. Qiao Gu, Ali Kuwajerwala, Sacha Morin, Krishna Murthy Jatavallabhula, Bipasha Sen, Aditya Agarwal, Corban Rivera, William Paul, Kirsty Ellis, Rama Chellappa, et al. Conceptgraphs: Open-vocabulary 3d scene graphs for perception and planning. In 2024 IEEE International Conference on Robotics and Automation (ICRA), pages 5021–5028. IEEE, 2024.
16. Jiaxin Huang, Ziwen Li, Hanlve Zhang, Runnan Chen, Xiao He, Yandong Guo, Wenping Wang, Tongliang Liu, and Mingming Gong. Surprise3d: A dataset for spatial understanding and reasoning in complex 3d scenes. arXiv preprint arXiv:2507.07781, 2025.
17. Shuai Huang, Wenxuan Zhao, and Jun Gao. Si-bench: Benchmarking social intelligence of large language models in human-to-human conversations. arXiv preprint arXiv:2510.23182, 2025.
18. Haotong Lin, Sili Chen, Junhao Liew, Donny Y Chen, Zhenyu Li, Guang Shi, Jiashi Feng, and Bingyi Kang. Depth anything 3: Recovering the visual space from any views. arXiv preprint arXiv:2511.10647, 2025.
19. Jingli Lin, Runsen Xu, Shaohao Zhu, Sihan Yang, Peizhou Cao, Yunlong Ran, Miao Hu, Chenming Zhu, Yiman Xie, Yilin Long, et al. Mmsi-video-bench: A holistic benchmark for video-based spatial intelligence. arXiv preprint arXiv:2512.10863, 2025.
20. Zhanpeng Luo, Ce Zhang, Silong Yong, Cunxi Dai, Qianwei Wang, Haoxi Ran, Guanya Shi, Katia Sycara, and Yaqi Xie. pyspatial: Generating 3d visual programs for zero-shot spatial reasoning. arXiv preprint arXiv:2603.00905, 2026.
21. Wufei Ma, Yu-Cheng Chou, Qihao Liu, Xingrui Wang, Celso de Melo, Jianwen Xie, and Alan Yuille. Spatialreasoner: Towards explicit and generalizable 3d spatial reasoning. arXiv preprint arXiv:2504.20024, 2025.
22. Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. Self-refine: Iterative refinement with self-feedback. Advances in neural information processing systems, 36:46534–46594, 2023.
23. Zhenhua Ning, Zhuotao Tian, Shaoshuai Shi, Guangming Lu, Daojing He, Wenjie Pei, and Li Jiang. Enhancing spatial reasoning in multimodal large language models through reasoning-based segmentation. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 7851–7860, 2025.
24. John O’keefe and Lynn Nadel. The hippocampus as a cognitive map. Oxford university press, 1978.
25. OpenAI. Gpt-4v(ision) system card. https://cdn.openai.com/papers/GPTV_System_Card.pdf, 2023.
26. Kun Ouyang. Spatial-r1: Enhancing mllms in video spatial reasoning. arXiv e-prints, pages arXiv–2504, 2025.
27. Jianing Qi, Jiawei Liu, Hao Tang, and Zhigang Zhu. Beyond semantics: Rediscovering spatial awareness in vision-language models. arXiv preprint arXiv:2503.17349, 2025.
28. Santhosh Kumar Ramakrishnan, Erik Wijmans, Philipp Kraehenbuehl, and Vladlen Koltun. Does spatial cognition emerge in frontier models? arXiv preprint arXiv:2410.06468, 2024.
29. Krishan Rana, Jesse Haviland, Sourav Garg, Jad Abou-Chakra, Ian Reid, and Niko Suenderhauf. Sayplan: Grounding large language models using 3d scene graphs for scalable robot task planning. arXiv preprint arXiv:2307.06135, 2023.
30. Shouwei Ruan, Liyuan Wang, Caixin Kang, Qihui Zhu, Songming Liu, Xingxing Wei, and Hang Su. From reactive to cognitive: brain-inspired spatial intelligence for embodied agents. intelligence (AGI), 3(9):10, 2025.
31. Daniela Schiller, Howard Eichenbaum, Elizabeth A Buffalo, Lila Davachi, David J Foster, Stefan Leutgeb, and Charan Ranganath. Memory and space: towards an understanding of the cognitive map. Journal of Neuroscience, 35(41):13904–13911, 2015.
32. Aaditya Singh, Adam Fry, Adam Perelman, Adam Tart, Adi Ganesh, Ahmed El-Kishky, Aidan McLaughlin, Aiden Low, AJ Ostrow, Akhila Ananthram, et al. Openai gpt-5 system card. arXiv preprint arXiv:2601.03267, 2025.
33. Zhaochen Su, Peng Xia, Hangyu Guo, Zhenhua Liu, Yan Ma, Xiaoye Qu, Jiaqi Liu, Yanshu Li, Kaide Zeng, Zhengyuan Yang, et al. Thinking with images for multimodal reasoning: Foundations, methods, and future frontiers. arXiv preprint arXiv:2506.23918, 2025.
34. Jianyuan Wang, Minghao Chen, Nikita Karaev, Andrea Vedaldi, Christian Rupprecht, and David Novotny. Vggt: Visual geometry grounded transformer. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 5294–5306, 2025.
35. Qineng Wang, Baiqiao Yin, Pingyue Zhang, Jianshu Zhang, Kangrui Wang, Zihan Wang, Jieyu Zhang, Keshigeyan Chandrasegaran, Han Liu, Ranjay Krishna, et al. Mindcube: Spatial mental modeling from limited views. arXiv e-prints, pages arXiv–2506, 2025.
36. Weiyun Wang, Zhangwei Gao, Lixin Gu, Hengjun Pu, Long Cui, Xingguang Wei, Zhaoyang Liu, Linglin Jing, Shenglong Ye, Jie Shao, et al. Internvl3. 5: Advancing open-source multimodal models in versatility, reasoning, and efficiency. arXiv preprint arXiv:2508.18265, 2025.
37. Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le, Ed H Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. In The Eleventh International Conference on Learning Representations, 2023.
38. Yuxin Wang, Lei Ke, Boqiang Zhang, Tianyuan Qu, Hanxun Yu, Zhenpeng Huang, Meng Yu, Dan Xu, and Dong Yu. N3d-vlm: Native 3d grounding enables accurate spatial reasoning in vision-language models. arXiv preprint arXiv:2512.16561, 2025.
39. Diankun Wu, Fangfu Liu, Yi-Hsin Hung, and Yueqi Duan. Spatial-mllm: Boosting mllm capabilities in visual-based spatial intelligence. arXiv preprint arXiv:2505.23747, 2025.
40. Mingrui Wu, Zhaozhi Wang, Fangjinhua Wang, Jiaolong Yang, Marc Pollefeys, and Tong Zhang. From indoor to open world: Revealing the spatial reasoning gap in mllms. arXiv preprint arXiv:2512.19683, 2025.
41. Jihan Yang, Shusheng Yang, Anjali W Gupta, Rilyn Han, Li Fei-Fei, and Saining Xie. Thinking in space: How multimodal large language models see, remember, and recall spaces. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 10632–10643, 2025.
42. Shusheng Yang, Jihan Yang, Pinzhi Huang, Ellis Brown, Zihao Yang, Yue Yu, Shengbang Tong, Zihan Zheng, Yifan Xu, Muhan Wang, et al. Cambrian-s: Towards spatial supersensing in video. arXiv preprint arXiv:2511.04670, 2025.
43. Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. Re-act: Synergizing reasoning and acting in language models. In International Conference on Learning Representations (ICLR), 2023.
44. Kaichen Zhang, Bo Li, Peiyuan Zhang, Fanyi Pu, Joshua Adrian Cahyono, Kairui Hu, Shuai Liu, Yuanhan Zhang, Jingkang Yang, Chunyuan Li, and Ziwei Liu. Lmms-eval: Reality check on the evaluation of large multimodal models, 2024. URL https://arxiv.org/abs/2407.12772.
45. Weichen Zhang, Ruiying Peng, Chen Gao, Jianjie Fang, Xin Zeng, Kaiyuan Li, Ziyou Wang, Jinqiang Cui, Xin Wang, Xinlei Chen, et al. The point, the vision and the text: Does point cloud boost spatial reasoning of large language models? arXiv preprint arXiv:2504.04540, 2025.
46. Zaibin Zhang, Yuhan Wu, Lianjie Jia, Yifan Wang, Zhongbo Zhang, Yijiang Li, Binghao Ran, Fuxi Zhang, Zhuohan Sun, Zhenfei Yin, et al. Think3d: Thinking with space for spatial reasoning. arXiv preprint arXiv:2601.13029, 2026.
47. Yuze Zhao, Jintao Huang, Jinghan Hu, Xingjun Wang, Yunlin Mao, Daoze Zhang, Zeyinzi Jiang, Zhikai Wu, Baole Ai, Ang Wang, Wenmeng Zhou, and Yingda Chen. Swift:a scalable lightweight infrastructure for fine-tuning, 2024. URL https://arxiv.org/abs/2408.05517.
48. Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, et al. Group sequence policy optimization. arXiv preprint arXiv:2507.18071, 2025.

## Appendix A. Training & Evaluation Configuration

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> RL training configuration. AlloSpatial-4B and AlloSpatial-8B are initialized from their corresponding supervised cold-start checkpoints at step 240, after three epochs of SFT. We optimize both agents with GSPO using ms-swift framework [47] and DeepSpeed ZeRO-2. The RL prompts are sampled from a shared training pool of 59,981 examples, including 49,981 VSI-style examples from VSI-590K and 10,000 examples from the MindCube training split. Inline validation is performed on 1,442 held-out examples, consisting of 392 VSI-Bench-tiny questions and 1,050 MindCube-tiny questions. For each prompt, the policy samples 8 rollouts, with at most 5 tool-interaction turns per rollout. The maximum sequence length is 32,768 tokens, and generated completions are capped at 8,192 tokens. The trajectory reward follows HGTR, combining structural compliance, answer accuracy, tool-use effectiveness, and length control with weights 0.15, 0.60, 0.10, and 0.15, respectively. Validation rewards are logged for monitoring but are not used for optimization.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> RL 训练配置。AlloSpatial-4B 和 AlloSpatial-8B 都从各自监督式冷启动 checkpoint 的第 240 step 初始化，此时已完成 3 个 epoch 的 SFT。我们使用 ms-swift 框架 [47] 与 DeepSpeed ZeRO-2，通过 GSPO 来优化这两个 agent。RL prompts 采样自一个共享训练池，共 59,981 个样本，其中包括 49,981 个来自 VSI-590K 的 VSI 风格样本，以及 10,000 个来自 MindCube 训练划分的样本。在线验证在 1,442 个留出样本上进行，包括 392 个 VSI-Bench-tiny 问题和 1,050 个 MindCube-tiny 问题。对于每个 prompt，策略会采样 8 条 rollout，每条 rollout 最多允许 5 次工具交互。最大序列长度为 32,768 tokens，生成补全最长为 8,192 tokens。轨迹奖励采用 HGTR，将结构合规性、答案准确性、工具使用效果和长度控制分别以 0.15、0.60、0.10 和 0.15 的权重组合起来。验证奖励会被记录用于监控，但不会用于优化。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Both runs use cosine learning-rate decay with a warmup ratio of 0.005, freeze the vision tower and aligner modules, and adopt $\epsilon_{\mathrm{high}} = 0.28$ with overlong-completion filtering. The training scripts are epoch-based rather than hard-coded with a fixed maximum number of steps; the reported checkpoints are selected by validation performance and inference efficiency. Detailed configuration information is shown in Tab. 5.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 两个训练都使用余弦学习率衰减，warmup ratio 为 0.005，冻结 vision tower 与 aligner 模块，并采用 $\epsilon_{\mathrm{high}} = 0.28$ 以及过长补全过滤。训练脚本是基于 epoch 而非硬编码固定最大 step 数来运行的；文中报告的 checkpoint 根据验证性能和推理效率来选取。详细配置见表 5。

### Table 5. GSPO training configuration for the reported AlloSpatial checkpoints

**Image status:** Table image not embedded due to strict one-file mode; full searchable transcription is preserved below.
**Image status[CN]:** 由于严格单文件模式，表格截图未嵌入；下方保留完整可搜索转录。

**Caption:** Table 5: GSPO training configuration for the reported AlloSpatial checkpoints. The main paper reports the 600-step AlloSpatial-4B checkpoint and the 400-step AlloSpatial-8B checkpoint. Unique prompts are counted after grouping the 8 sampled rollouts per prompt.

**Caption[CN]:** 表 5：文中报告的 AlloSpatial checkpoints 的 GSPO 训练配置。正文报告的是 600-step 的 AlloSpatial-4B checkpoint 和 400-step 的 AlloSpatial-8B checkpoint。Unique prompts 的统计是在把每个 prompt 的 8 条 sampled rollout 分组之后进行的。

| Setting | AlloSpatial-4B | AlloSpatial-8B |
|---|---|---|
| Initialization | Qwen3-VL-4B SFT step 240 | Qwen3-VL-8B SFT step 240 |
| Reported RL checkpoint | step 600 | step 400 |
| Trainer processes | 4 | 6 |
| Per-device train batch | 4 | 2 |
| Gradient accumulation | 4 | 4 |
| Generated trajectories/update | 64 | 48 |
| Unique prompts/update | 8 | 6 |
| Rollouts per prompt | 8 | 8 |
| Unique prompts to reported ckpt. | 4.8K | 2.4K |
| Learning rate | $1 \times 10^{-6}$ | $5 \times 10^{-7}$ |
| Precision / attention | bf16 / FlashAttention | bf16 / FlashAttention |
| Trainable modules | language modules | language modules |
| Optimizer infrastructure | full tuning + ZeRO-2 | full tuning + ZeRO-2 |
| Sampling temperature | 1.0 | 1.0 |
| KL coefficient $\beta$ | 0.01 | 0.0 |
| Eval / save interval | 100 steps | 50 steps |

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Evaluation configuration. For trained local agents, we evaluate AlloSpatial with lmms-eval framework [44]. The evaluator parses final responses from predefined answer tags, uses temperature 1.0, allows up to 8 reasoning turns, and caps each completion at 8,192 new tokens. For VSI-Bench, the main post-trained evaluation follows the limited-observation setting with 7 uniformly sampled frames, while the frame-budget ablation evaluates 0, 3, 7, 15, and 24 input frames. For training-free proprietary-model evaluation, we uniformly sample up to 32 frames to provide sufficient observations for external cognitive mapping. MindCube is evaluated using the provided multi-view images.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 评测配置。对于训练后的本地 agents，我们使用 lmms-eval 框架 [44] 评估 AlloSpatial。评测器会从预定义 answer tags 中解析最终响应，使用 temperature 1.0，允许最多 8 个推理轮次，并将每次 completion 限制在 8,192 个新 token 以内。对于 VSI-Bench，主要的后训练评测遵循有限观察设定，使用 7 个均匀采样帧；而帧预算消融则测试 0、3、7、15 和 24 个输入帧。对于免训练的闭源模型评测，我们统一最多采样 32 帧，以为外部认知制图提供足够观察。MindCube 则使用其提供的多视图图像进行评测。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Across local-agent experiments, World2Mind uses the same default cognitive mapping pipeline, including monocular depth and pose estimation, SAM3-based open-vocabulary segmentation, confidence filtering, semantic point-cloud construction, AST serialization, and optional top-down map rendering. During evaluation, tool calls generated by the model are executed online, and the returned ASTs, route maps, or visualizations are inserted into the dialogue context for subsequent harness-guided reasoning.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在所有本地 agent 实验中，World2Mind 都使用相同的默认认知制图流程，包括单目深度与位姿估计、基于 SAM3 的开放词汇分割、置信过滤、语义点云构建、AST 序列化以及可选的俯视地图渲染。在评测过程中，模型生成的工具调用会被在线执行，而返回的 AST、路径地图或可视化结果会被插入到对话上下文中，供后续 harness 引导推理使用。

## Appendix B. World2Mind Service Parallelization

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> RL rollout generation can produce many concurrent World2Mind calls, while a single World2Mind process would serialize reconstruction and mapping requests. We therefore deploy World2Mind as a multi-process HTTP service during training and local evaluation. Each service process is assigned to an independent NPU worker and initializes the same cognitive mapping pipeline, including monocular geometry estimation, SAM3 segmentation, semantic point-cloud construction, AST generation, and route-map rendering. In our main configuration, eight World2Mind workers are launched in parallel to support concurrent tool execution.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> RL rollout 生成会产生大量并发的 World2Mind 调用，而单个 World2Mind 进程会串行处理重建和制图请求。因此，我们在训练和本地评测期间，将 World2Mind 部署为一个多进程 HTTP 服务。每个服务进程都被分配给独立的 NPU worker，并初始化相同的认知制图流程，包括单目几何估计、SAM3 分割、语义点云构建、AST 生成和路径地图渲染。在我们的主配置中，会并行启动 8 个 World2Mind workers，以支持并发工具执行。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Within each worker, NPU-intensive depth estimation and segmentation are executed under a worker-level lock, while downstream mapping, AST construction, and route-map generation proceed after NPU computation and are controlled by CPU-side concurrency limits. This separation prevents concurrent rollouts from over-subscribing NPU memory while allowing lightweight mapping operations to proceed efficiently.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在每个 worker 内部，高 NPU 开销的深度估计和分割会在 worker 级锁下执行；而后续的制图、AST 构建和路径地图生成则在 NPU 计算完成后继续，并由 CPU 侧并发限制进行控制。这样的分离既能防止并发 rollout 过度占用 NPU 内存，又能让较轻量的制图操作高效推进。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Rollout and evaluation clients dispatch each `cognitive_map` request to an available World2Mind worker using a simple load-balancing strategy based on current in-flight requests. Failed or unavailable workers are skipped and requests are retried on another endpoint when possible. This service design improves throughput and tail-latency stability under concurrent rollout generation, while keeping the World2Mind reconstruction pipeline and AST semantics unchanged.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> rollout 与评测客户端会依据当前正在处理的请求数，使用一个简单的负载均衡策略，将每个 `cognitive_map` 请求分发给可用的 World2Mind worker。失效或不可用的 worker 会被跳过，并在可能时把请求重试到其他 endpoint 上。这样的服务设计在并发 rollout 生成时提升了吞吐和尾延迟稳定性，同时保持了 World2Mind 重建流程与 AST 语义本身不变。

## Appendix C. Spatial Reasoning Harness Prompts

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The Spatial Reasoning Harness is implemented with three coupled components: a system message, a machine-readable tool interface, and a user-side reasoning protocol. For proprietary models, the tool interface is passed through function-calling schemas. For locally trained agents, the same interface is serialized as `<tool_call>` blocks containing a JSON object with name and arguments. Visual tokens are placed before the reasoning protocol, ensuring that the model observes the frames or multi-view images before receiving step-by-step instructions.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Spatial Reasoning Harness 由三个耦合组件实现：system message、机器可读的工具接口，以及用户侧推理协议。对于闭源模型，工具接口通过 function-calling schema 传递；对于本地训练的 agents，同一接口会被序列化为 `<tool_call>` 块，其中包含带有 `name` 和 `arguments` 的 JSON 对象。视觉 tokens 被放在推理协议之前，以确保模型在接收逐步指令之前，已经先观察到视频帧或多视图图像。

### C.1. System Message

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The source system message is reproduced verbatim below.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 下方按原文逐字保留系统消息。

```text
Role. You are a spatial intelligence assistant that analyzes videos and images to answer spatial questions.
Available tools.
 • world2mind: builds an allocentric cognitive map and returns per-instance spatial data, including coordinates, sizes, and object relations.
 • view_image: renders cognitive-map visualizations, including top-down landmark maps, route maps, semantic maps, and point-cloud views.
Reliability note. The cognitive map is produced from monocular reconstruction and may contain missing objects, ghost instances, coordinate drift, or segmentation errors. Treat tool outputs as supplementary evidence rather than ground truth, and cross-validate them against direct visual observations before answering.
Answer format. Wrap the final answer in <Answer></Answer> tags.
```

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Chinese rendering of the system message. Role: You are a spatial intelligence assistant that analyzes videos and images to answer spatial questions. Available tools: `world2mind` builds an allocentric cognitive map and returns per-instance spatial data, including coordinates, sizes, and object relations; `view_image` renders cognitive-map visualizations, including top-down landmark maps, route maps, semantic maps, and point-cloud views. Reliability note: the cognitive map is produced from monocular reconstruction and may contain missing objects, ghost instances, coordinate drift, or segmentation errors. Tool outputs should be treated as supplementary evidence rather than ground truth, and should be cross-validated against direct visual observations before answering. Answer format: wrap the final answer in `<Answer></Answer>` tags.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 系统消息的中文释义如下。角色：你是一个空间智能助手，负责分析视频和图像并回答空间问题。可用工具：`world2mind` 用于构建非自我中心认知地图，并返回逐实例空间数据，包括坐标、大小和物体关系；`view_image` 用于渲染认知地图可视化，包括俯视地标图、路径图、语义图和点云视图。可靠性说明：认知地图来自单目重建，可能包含缺失物体、幽灵实例、坐标漂移或分割错误。在回答前，应将工具输出视为补充证据而非地面真实，并与直接视觉观察交叉验证。答案格式：将最终答案包裹在 `<Answer></Answer>` tags 中。

### C.2. Tool Interface

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> `world2mind`. Generate a query-conditioned cognitive map from the current visual input. The tool automatically analyzes the video frames or images already provided in the conversation; the model does not provide file paths.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> `world2mind`。从当前视觉输入生成一个查询条件化的认知地图。该工具会自动分析对话中已经提供的视频帧或图像；模型无需提供文件路径。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Returned knowledge. `Landmark` knowledge (`knowledge_type=landmark` or `both`): detected instances, metric coordinates, footprint size, and object relations. `Route` knowledge (`knowledge_type=route` or `both`): traversable regions, camera trajectory, and grid-based route information.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 返回知识。`Landmark` 知识（`knowledge_type=landmark` 或 `both`）：检测到的实例、度量坐标、占地尺寸以及物体关系。`Route` 知识（`knowledge_type=route` 或 `both`）：可通行区域、相机轨迹以及基于网格的路径信息。

| Parameter | Requirement | Meaning |
|---|---|---|
| categories | required; list of strings | Object categories to detect as landmarks, e.g., `chair`, `table`, `door`. |
| scene_type | required; `indoor` or `outdoor` | Selects scene-specific reconstruction settings. |
| knowledge_type | required; `landmark`, `route`, or `both` | Chooses landmark-only, route-only, or complete cognitive-map output. |
| output_format | required; `rectangle` or `ellipse` | Specifies the landmark footprint representation. |
| traversable_categories | required for `route` or `both` | Ground or surface categories used to infer passable regions, e.g., `floor`, `carpet`, `road`. |

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> `view_image`. Inspect a visualization generated by the most recent `world2mind` call. The required parameter `visualization_type` must be selected from the available visualizations returned by `world2mind`, such as `landmark_vis`, `route_vis`, `pointcloud_rgb_topdown`, or `pointcloud_semantic_topdown`. The model should call `view_image` when the YAML output is ambiguous, when object layout requires visual verification, or when map evidence must be checked against raw observations.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> `view_image`。查看最近一次 `world2mind` 调用生成的可视化。必需参数 `visualization_type` 必须从 `world2mind` 返回的可用可视化中选择，例如 `landmark_vis`、`route_vis`、`pointcloud_rgb_topdown` 或 `pointcloud_semantic_topdown`。当 YAML 输出含糊、物体布局需要视觉确认，或者需要将地图证据与原始观察进行核对时，模型应调用 `view_image`。

### C.3. Text-Form Tool Calls for Local Agents

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For local SFT/GSPO agents, tool calls are serialized as text while preserving the same schema:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 对于本地 SFT/GSPO agents，工具调用会以文本形式序列化，但保持相同的 schema：

```json
<tool_call>
{
  "name": "world2mind",
  "arguments": {
    "categories": ["chair", "table", "door"],
    "scene_type": "indoor",
    "knowledge_type": "both",
    "output_format": "rectangle",
    "traversable_categories": ["floor", "carpet"]
  }
}
</tool_call>
```

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The schema requires `categories`, `scene_type`, `knowledge_type`, and `output_format`. Malformed calls are returned as tool-error messages when applicable and are not treated as valid spatial evidence.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 该 schema 要求必须包含 `categories`、`scene_type`、`knowledge_type` 和 `output_format`。在适用时，格式错误的调用会以 tool-error message 的形式返回，并且不会被视为有效的空间证据。

### C.4. User-Side Reasoning Protocol

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Visual tokens. The video frames or multi-view images are placed before the textual instructions.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 视觉 tokens。视频帧或多视图图像会被放在文字指令之前。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Step 1: Visual Clues. Describe concrete visual observations before any tool call, including visible objects, relative positions, spatial relations, and a preliminary answer when possible.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 步骤 1：Visual Clues。在任何工具调用之前，先描述具体视觉观察，包括可见物体、相对位置、空间关系，以及在可能时给出初步答案。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Step 2.1: `world2mind` Tool Call. Call `world2mind` only when the question requires information that vision alone cannot reliably provide, such as metric distance, 3D coordinates, route layout, viewpoint transformation, or complex spatial relations.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 步骤 2.1：`world2mind` Tool Call。只有当问题需要纯视觉无法可靠提供的信息时，才调用 `world2mind`，例如度量距离、三维坐标、路径布局、视角变换或复杂空间关系。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Step 2.2: Map Clues. If `world2mind` is called, summarize map evidence only: detected instances, coordinates, sizes, containment relations, route cells, trajectories, or camera orientations. Do not reconcile it with visual clues yet.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 步骤 2.2：Map Clues。如果调用了 `world2mind`，则只总结地图证据：检测到的实例、坐标、大小、包含关系、路径单元、轨迹或相机朝向。此时不要先把它与视觉线索调和。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Step 3.1: `view_image` Tool Call. If the structured map is ambiguous or layout verification is needed, call `view_image` using one of the available visualization types returned by `world2mind`.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 步骤 3.1：`view_image` Tool Call。如果结构化地图含糊，或者需要验证布局，则应使用 `world2mind` 返回的某个可用可视化类型来调用 `view_image`。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Step 3.2: Visualization Clues. Describe the rendered cognitive-map visualization, such as top-down layout, object arrangement, route trajectory, or conflicts with the raw visual input.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 步骤 3.2：Visualization Clues。描述渲染出的认知地图可视化，例如俯视布局、物体排列、路径轨迹，或与原始视觉输入之间的冲突。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Step 4: Cross-Validation. Compare visual evidence, map evidence, and visualization evidence. Identify conflicts caused by reconstruction drift, missing objects, false detections, or visual ambiguity, and decide which evidence should dominate.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 步骤 4：Cross-Validation。比较视觉证据、地图证据和可视化证据。识别由重建漂移、物体缺失、误检或视觉歧义带来的冲突，并决定哪类证据应占主导。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Step 5: Final Answer. Integrate the validated evidence and provide the conclusion. For single-word, numeric, or option questions, place only the final value inside the answer tag.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 步骤 5：Final Answer。整合通过验证的证据并给出结论。对于单词、数值或选项类问题，只需把最终值放在 answer tag 内。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Question. `{query}`

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 问题：`{query}`

## Appendix D. Case Analysis

### D.1. Case 1: Metric Closest-Point Reasoning

#### User Turn: Input Observation and Query

### Figure-like Case Block D.1-A. Observation contact sheet

**Image status:** Not embedded due to strict one-file mode.
**Image status[CN]:** 由于严格单文件模式，图像未嵌入。

**Caption:** Observation. The input is a video of a kitchen. Eight approximately uniformly sampled frames are shown below as a two-row, four-column contact sheet.

**Caption[CN]:** 观察。输入是一个厨房视频。原文在此处给出了大约均匀采样得到的 8 帧，并排成两行四列的 contact sheet。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question. Determine the shortest distance between the towel and the refrigerator in meters. Please answer using a single word or phrase.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题。请确定毛巾与冰箱之间的最短距离（单位：米）。请用单个单词或短语作答。

#### Assistant Turn 1: Visual Clues and World2Mind Call

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Visual clues. The model first observes a green patterned towel hanging on the oven door and a white refrigerator in other frames. Because the two objects are not visible in a single calibrated view, it estimates that direct visual inspection is insufficient for precise metric distance.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Visual clues。模型首先观察到一条挂在烤箱门上的绿色花纹毛巾，以及在其他帧中出现的一台白色冰箱。由于这两个物体并未在同一个经过标定的视图中同时可见，它判断直接视觉检查不足以精确估计度量距离。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Tool call.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 工具调用如下。

```json
<tool_call>
{
  "name": "world2mind",
  "arguments": {
    "categories": ["towel", "refrigerator", "stove", "oven"],
    "knowledge_type": "landmark",
    "output_format": "rectangle",
    "scene_type": "indoor",
    "traversable_categories": ["floor"]
  }
}
</tool_call>
```

#### Tool Result 1: World2Mind Landmark AST

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> World2Mind returns a JSON tool result with `success=true`, scene id `scene0220_01_c70da29e-5e7`, available visualization `landmark_vis`, and the following AST in the `landmark_yaml` field.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> World2Mind 返回了一个 JSON 工具结果，其中 `success=true`，scene id 为 `scene0220_01_c70da29e-5e7`，可用可视化为 `landmark_vis`，并且在 `landmark_yaml` 字段中给出如下 AST。

```yaml
Map_Metadata:
  Coordinate_System: 2D Absolute Grid (meters)
  Origin_Ref: (-3.129, -1.293)
  AST_Format: Rectangle (center, width, height)
Spatial_Hierarchy:
- Node_ID: floor_01
  Spatial_Pose:
    Center: (-0.087, 1.449)
    Width: 4.117
    Height: 2.838
  Attributes:
    Height_Range: (1.179, 1.585)
    Area_m2: 7.1149
    Point_Count: 15383
- Node_ID: refrigerator_01
  Spatial_Pose:
    Center: (0.474, 1.475)
    Width: 0.924
    Height: 0.866
  Attributes:
    Height_Range: (-0.234, 1.525)
    Area_m2: 0.5815
    Point_Count: 2674
- Node_ID: stove_01
  Spatial_Pose:
    Center: (2.106, 0.691)
    Width: 0.65
    Height: 0.731
  Attributes:
    Height_Range: (0.554, 1.585)
    Area_m2: 0.4324
    Point_Count: 3588
  Contains_Children:
  - Node_ID: towel_01
    Spatial_Pose:
      Center: (1.918, 0.634)
      Width: 0.052
      Height: 0.304
    Attributes:
      Height_Range: (0.839, 1.207)
      Area_m2: 0.0102
      Point_Count: 1136
    Relation_To_Parent: Inside
```

#### Assistant Turn 2: Map Calculation and Visualization Request

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Map clues. The model reads `towel_01` center `(1.918, 0.634)` m and `refrigerator_01` center `(0.474, 1.475)` m. The center-to-center distance is about `1.671` m, but the question asks for nearest-point distance. Using rectangle half-extents, the horizontal gap is `1.444 - (0.026 + 0.462) = 0.956` m and the vertical gap is `0.841 - (0.152 + 0.433) = 0.256` m. The nearest-boundary distance is therefore $\sqrt{0.956^2 + 0.256^2} \approx 0.990$ m.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Map clues。模型读取到 `towel_01` 的中心为 `(1.918, 0.634)` m，`refrigerator_01` 的中心为 `(0.474, 1.475)` m。中心到中心距离约为 `1.671` m，但问题要求的是最近点距离。使用矩形半边长后，水平间隔为 `1.444 - (0.026 + 0.462) = 0.956` m，垂直间隔为 `0.841 - (0.152 + 0.433) = 0.256` m。因此，最近边界距离为 $\sqrt{0.956^2 + 0.256^2} \approx 0.990$ m。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Visualization request. The trajectory then requests a map visualization to verify the geometric layout before finalizing the answer.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 可视化请求。随后，该轨迹请求地图可视化，以便在给出最终答案之前验证几何布局。

```json
<tool_call>
{
  "name": "view_image",
  "arguments": {"visualization_type": "landmark_vis"}
}
</tool_call>
```

#### Tool Result 2: Landmark Visualization

### Figure-like Case Block D.1-B. Top-down landmark visualization

**Image status:** Not embedded due to strict one-file mode.
**Image status[CN]:** 由于严格单文件模式，图像未嵌入。

**Caption:** The returned `landmark_vis` image provides a top-down check of the refrigerator and stove/towel layout.

**Caption[CN]:** 返回的 `landmark_vis` 图像提供了对冰箱与炉灶/毛巾布局的俯视核验。

#### Assistant Turn 3: Cross-Validation, Final Answer, and Ground Truth

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Visualization clues. The top-down landmark visualization places the refrigerator and stove/towel on different sides of the kitchen, with a gap consistent with the rectangle-derived estimate.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Visualization clues。该俯视地标可视化把冰箱与炉灶/毛巾放在厨房两侧，中间间隔与依据矩形推导出的估计是一致的。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Cross-validation. The raw visual evidence suggests a short, plausible kitchen-scale separation, and the map does not introduce a visible contradiction. The agent therefore trusts the AST-derived nearest-point estimate.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> Cross-validation。原始视觉证据表明这是一段短而合理、符合厨房尺度的间距，而地图并未引入明显矛盾。因此，agent 采信了由 AST 推导出的最近点估计。

```text
Prediction: <Answer>0.99 m</Answer>
Ground truth (VSI): 1.1 m
Absolute error: 0.11 m
```

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The prediction is `<Answer>0.99 m</Answer>`, the VSI ground truth is `1.1 m`, and the absolute error is `0.11 m`.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 该案例的预测为 `<Answer>0.99 m</Answer>`，VSI 的真实答案为 `1.1 m`，绝对误差为 `0.11 m`。

### D.2. Case 2: Viewpoint-Conditioned Navigation

#### User Turn: Input Observations and Query

### Figure-like Case Block D.2-A. Four wall-aligned chair views

**Image status:** Not embedded due to strict one-file mode.
**Image status[CN]:** 由于严格单文件模式，图像未嵌入。

**Caption:** Observation. The input consists of four wall-aligned views of the same black chair: front, left, back, and right.

**Caption[CN]:** 观察。输入由同一把黑色椅子的四个贴墙对齐视图组成：正面、左侧、背面和右侧。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question. If the observer stands at the same spot and faces the same direction as image 4, then turns left and moves forward, will the observer get closer to the grey sofa? `A. No` `B. Yes`.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题。如果观察者站在与 image 4 相同的位置，并面向相同方向，然后向左转并向前移动，观察者会更靠近灰色沙发吗？`A. No` `B. Yes`。

#### Assistant Turn 1: Visual Clues and World2Mind Call

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Visual clues. The model identifies image 1 as the front view of the chair, image 2 as the left view, image 3 as the back view, and image 4 as the right view. The grey sofa is clearly visible in image 3. From image 4, turning left appears to rotate the observer toward the direction where the sofa may lie, but the view transformation is ambiguous enough to benefit from an allocentric map.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Visual clues。模型把 image 1 识别为椅子的正面视图，image 2 为左视图，image 3 为背面视图，image 4 为右视图。灰色沙发在 image 3 中清晰可见。从 image 4 出发，向左转似乎会把观察者旋转到沙发所在方向，但这种视图变换仍然足够模糊，因此值得借助非自我中心地图。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Tool call.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 工具调用如下。

```json
<tool_call>
{
  "name": "world2mind",
  "arguments": {
    "categories": ["black chair", "grey sofa", "desk", "plant", "bag", "window"],
    "knowledge_type": "both",
    "output_format": "rectangle",
    "scene_type": "indoor",
    "traversable_categories": ["floor", "carpet", "tile flooring"]
  }
}
</tool_call>
```

#### Tool Result 1: World2Mind AST and Route Knowledge

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> World2Mind returns both landmark and route knowledge for scene `images_4_816b9d06-732`. The complete AST and route fields are shown below.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> World2Mind 为场景 `images_4_816b9d06-732` 返回了地标知识和路径知识。完整的 AST 与 route 字段如下所示。

```yaml
Map_Metadata:
  Coordinate_System: 2D Absolute Grid (meters)
  Origin_Ref: (-2.281, -0.401)
  AST_Format: Rectangle (center, width, height)
  Camera_Views:
  - Frame: frame_000000
    Image: image 1
    Position: (-0.975, 0.668)
    Heading_Deg: 56.2
  - Frame: frame_000001
    Image: image 2
    Position: (0.921, 0.676)
    Heading_Deg: -57.6
  - Frame: frame_000002
    Image: image 3
    Position: (-0.0, 0.0)
    Heading_Deg: 0.3
  - Frame: frame_000003
    Image: image 4
    Position: (-0.17, 1.443)
    Heading_Deg: 161.8
Spatial_Hierarchy:
- Node_ID: grey sofa_01
  Spatial_Pose:
    Center: (1.524, 1.234)
    Width: 0.708
    Height: 1.022
  Attributes:
    Height_Range: (-0.654, 0.881)
    Area_m2: 0.4026
    Point_Count: 640
- Node_ID: black chair_01
  Spatial_Pose:
    Center: (-0.077, 1.314)
    Width: 0.532
    Height: 0.333
  Attributes:
    Height_Range: (-0.529, 0.49)
    Area_m2: 0.1173
    Point_Count: 2911
- Node_ID: bag_01
  Spatial_Pose:
    Center: (0.32, 1.278)
    Width: 0.412
    Height: 0.185
  Attributes:
    Height_Range: (0.311, 0.672)
    Area_m2: 0.0523
    Point_Count: 296
- Node_ID: plant_01
  Spatial_Pose:
    Center: (0.214, 1.863)
    Width: 0.307
    Height: 0.22
  Attributes:
    Height_Range: (-0.187, 0.221)
    Area_m2: 0.0419
    Point_Count: 516
```

```yaml
Route_Knowledge_Metadata:
  Coordinate_System: Grid (NxN cells)
  Grid_Divisions: 10
  Cell_Size: (0.474, 0.427)
  Scene_Bounds:
    Min: (-2.281, -0.401)
    Max: (2.458, 3.865)
  Total_Traversable_Cells: 32
  Estimated_Floor_Area_m2: 6.47
  Trajectory_Length: 4
  Note: Estimated_Floor_Area_m2 is the traversable floor area only. Actual room area
    approximately Floor_Area + furniture footprint area. Do NOT use Scene_Bounds to
     calculate
    room area -- Scene_Bounds is the axis-aligned bounding box of the entire 3D
     reconstruction
    and always significantly overestimates room size.
  Description: Route knowledge map showing traversable areas and camera movement path
  Scene: images_4_816b9d06-732
Traversable_Grid:
 - (0, 3)
 - (1, 3)
 - (1, 4)
 - (1, 6)
 - (1, 7)
 - (1, 8)
 - (2, 3)
 - (2, 6)
 - (2, 7)
 - (3, 2)
 - (3, 3)
 - (3, 4)
 - (3, 5)
 - (3, 6)
 - (3, 7)
 - (4, 2)
 - (4, 3)
 - (4, 4)
 - (4, 5)
 - (4, 6)
 - (4, 7)
 - (5, 3)
 - (5, 4)
 - (5, 5)
 - (5, 6)
 - (6, 3)
 - (6, 4)
 - (6, 5)
 - (6, 6)
 - (7, 3)
 - (7, 5)
 - (7, 6)
Camera_Trajectory: (2, 2) --> (2, 6) --> (0, 4) --> (4, 4)
Camera_Orientations:
 - Frame: frame_000000
   Image: image 1
   Position: (-0.975, 0.668)
   Heading_Deg: 56.2
 - Frame: frame_000001
   Image: image 2
   Position: (0.921, 0.676)
   Heading_Deg: -57.6
 - Frame: frame_000002
   Image: image 3
   Position: (-0.0, 0.0)
   Heading_Deg: 0.3
 - Frame: frame_000003
   Image: image 4
   Position: (-0.17, 1.443)
   Heading_Deg: 161.8
```

#### Assistant Turn 2: Map Clues and View-Image Call

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Map clues. The map places the grey sofa at `(1.524, 1.234)` and the black chair at `(-0.077, 1.314)`. Image 4 has camera position `(-0.170, 1.443)` and heading `161.8°`. Turning left changes the heading to approximately `71.8°`, which points toward increasing $x$. Since the sofa has a much larger $x$ coordinate than the image-4 camera, moving forward after the left turn should reduce the distance to the sofa.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Map clues。地图将灰色沙发放在 `(1.524, 1.234)`，将黑色椅子放在 `(-0.077, 1.314)`。image 4 对应的相机位置为 `(-0.170, 1.443)`，朝向为 `161.8°`。向左转后，朝向会变为大约 `71.8°`，也就是指向 $x$ 增大的方向。由于沙发的 $x$ 坐标明显大于 image-4 相机的位置，因此向左转后再向前移动，应当会缩短与沙发之间的距离。

```json
<tool_call>
{
  "name": "view_image",
  "arguments": {"visualization_type": "landmark_vis"}
}
</tool_call>
```

#### Tool Result 2: Landmark Visualization

### Figure-like Case Block D.2-B. Top-down sofa-chair-camera check

**Image status:** Not embedded due to strict one-file mode.
**Image status[CN]:** 由于严格单文件模式，图像未嵌入。

**Caption:** The returned landmark visualization provides an explicit top-down check of the chair, sofa, and image-4 camera pose.

**Caption[CN]:** 返回的地标可视化为椅子、沙发以及 image-4 相机位姿提供了一个明确的俯视核验。

#### Assistant Turn 3: Visualization Clues, Cross-Validation, Final Answer, and Ground Truth

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Visualization clues. The map shows the black chair near the center and the grey sofa to the right/east of the image-4 camera position. This agrees with the coordinate-level reading.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Visualization clues。地图显示黑色椅子位于中央附近，而灰色沙发位于 image-4 相机位置的右侧/东侧。这与坐标层面的解读一致。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Cross-validation. Visual evidence from image 3 shows the sofa behind the chair, while image 4 is the right-side view. The map evidence shows that a left turn from heading `161.8°` points approximately toward heading `71.8°`, which moves toward the sofa’s larger $x$ coordinate. The visual and allocentric cues therefore agree.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> Cross-validation。image 3 的视觉证据表明沙发位于椅子后方，而 image 4 是右侧视图。地图证据则显示，从朝向 `161.8°` 向左转后会大致朝向 `71.8°`，即朝向沙发更大的 $x$ 坐标方向移动。因此，视觉线索与非自我中心线索是一致的。

```text
Prediction: <Answer>B</Answer>
Ground truth (MindCube): B (Yes)
```

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The prediction is `<Answer>B</Answer>`, and the MindCube ground truth is `B (Yes)`.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 该案例的预测为 `<Answer>B</Answer>`，MindCube 的真实答案为 `B (Yes)`。

## Appendix E. Computational Costs in Training and Inference

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Training cost. In our setup, both AlloSpatial-4B and AlloSpatial-8B are trained on 8 HUAWEI Ascend 910B NPUs, taking approximately 60 and 40 NPU-hours, respectively, to reach the reported checkpoints. The 4B and 8B agents use 4 and 6 trainer processes, respectively. Around the reported checkpoints, one GSPO update typically takes 4–6 minutes, including multi-turn rollout generation, live World2Mind execution, reward computation, and policy optimization. The exact update time varies with the tool-use rate, the number of sampled World2Mind calls, and the reconstruction difficulty of each rollout batch.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 训练成本。在我们的设定中，AlloSpatial-4B 和 AlloSpatial-8B 都使用 8 张 HUAWEI Ascend 910B NPU 进行训练，分别约需 60 和 40 NPU-hours 才能达到文中报告的 checkpoints。4B 和 8B agents 分别使用 4 个和 6 个 trainer process。在接近这些报告 checkpoint 的阶段，一次 GSPO update 通常需要 4–6 分钟，其中包括多轮 rollout 生成、在线 World2Mind 执行、奖励计算和策略优化。确切的 update 时间会随工具使用率、采样到的 World2Mind 调用数量，以及每个 rollout batch 的重建难度而变化。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Inference cost. Inference cost is determined primarily by the number of input frames and the number of World2Mind calls. Each AlloSpatial query may involve multiple reasoning turns, and each valid World2Mind call can trigger depth and pose estimation, segmentation, semantic alignment, AST construction, and optional route-map rendering. With the parallel World2Mind service, VSI-Bench-tiny evaluation takes roughly 12 minutes for 392 questions with concurrent evaluation and 8 World2Mind workers.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 推理成本。推理成本主要由输入帧数量和 World2Mind 调用次数决定。每个 AlloSpatial 查询都可能包含多个推理轮次，而每次有效的 World2Mind 调用都可能触发深度与位姿估计、分割、语义对齐、AST 构建以及可选的路径地图渲染。借助并行的 World2Mind 服务，在并发评测且使用 8 个 World2Mind workers 的情况下，VSI-Bench-tiny 上的 392 个问题大约需要 12 分钟完成评测。

## NeurIPS Paper Checklist

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The checklist is designed to encourage best practices for responsible machine learning research, addressing issues of reproducibility, transparency, research ethics, and societal impact. Do not remove the checklist: The papers not including the checklist will be desk rejected. The checklist should follow the references and follow the (optional) supplemental material. The checklist does NOT count towards the page limit.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 该清单旨在鼓励负责任机器学习研究中的最佳实践，涉及可复现性、透明性、研究伦理和社会影响等问题。请勿删除该清单：未包含该清单的论文将被直接 desk reject。该清单应放在参考文献之后，并位于（可选）补充材料之后。该清单不计入页数限制。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Please read the checklist guidelines carefully for information on how to answer these questions. For each question in the checklist:
>
> - You should answer `[Yes]`, `[No]`, or `[N/A]`.
> - `[N/A]` means either that the question is Not Applicable for that particular paper or the relevant information is Not Available.
> - Please provide a short (1–2 sentence) justification right after your answer (even for `[N/A]`).

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 请仔细阅读该清单的填写指南，以了解如何回答这些问题。对于清单中的每一个问题：
>
> - 你应回答 `[Yes]`、`[No]` 或 `[N/A]`。
> - `[N/A]` 表示该问题对该论文不适用，或者相关信息不可获得。
> - 请在答案后立即给出一段简短的理由说明（1–2 句话即可），即使答案是 `[N/A]` 也一样。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The checklist answers are an integral part of your paper submission. They are visible to the reviewers, area chairs, senior area chairs, and ethics reviewers. You will also be asked to include it (after eventual revisions) with the final version of your paper, and its final version will be published with the paper.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 清单答案是论文投稿的组成部分。审稿人、领域主席、高级领域主席以及伦理审稿人都可以看到这些答案。在论文最终定稿时（经过可能的修改之后），你也会被要求将其一并纳入最终版本中，并且清单最终版本会随论文一起公开发表。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The reviewers of your paper will be asked to use the checklist as one of the factors in their evaluation. While `[Yes]` is generally preferable to `[No]`, it is perfectly acceptable to answer `[No]` provided a proper justification is given (e.g., error bars are not reported because it would be too computationally expensive" or "we were unable to find the license for the dataset we used"). In general, answering `[No]` or `[N/A]` is not grounds for rejection. While the questions are phrased in a binary way, we acknowledge that the true answer is often more nuanced, so please just use your best judgment and write a justification to elaborate. All supporting evidence can appear either in the main paper or the supplemental material, provided in appendix. If you answer `[Yes]` to a question, in the justification please point to the section(s) where related material for the question can be found.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 论文审稿人会被要求将该清单作为评估因素之一。虽然一般来说 `[Yes]` 优于 `[No]`，但只要给出适当理由，回答 `[No]` 也是完全可以接受的（例如，“没有报告误差条是因为计算成本过高”，或者“我们未能找到所用数据集的许可证”）。通常而言，回答 `[No]` 或 `[N/A]` 并不会成为拒稿理由。尽管这些问题以二元方式提出，我们承认真实答案往往更加细致复杂，因此请依据你的最佳判断，并在理由说明中进一步阐释。所有支持性证据都可以出现在正文或附录形式的补充材料中。如果你对某个问题回答 `[Yes]`，请在理由中指出相关内容位于哪一节。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> IMPORTANT, please:
>
> - Delete this instruction block, but keep the section heading "NeurIPS Paper Checklist",
> - Keep the checklist subsection headings, questions/answers and guidelines below.
> - Do not modify the questions and only use the provided macros for your answers.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 重要说明：
>
> - 删除这一段说明文字，但保留章节标题“NeurIPS Paper Checklist”；
> - 保留下方清单的小节标题、问题/答案以及指南；
> - 不要修改问题内容，并且只使用提供的宏来填写答案。

### 1. Claims

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：摘要和引言中提出的主要主张，是否准确反映了本文的贡献和范围？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[Yes]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[Yes]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The abstract and introduction state the paper’s main contributions: AlloSpatial, World2Mind, the Spatial Reasoning Harness, and the RL-based internalization into open-weight agents. The claims are supported by evaluations on VSI-Bench and MindCube, including training-free proprietary-model results, trained Qwen3-VL-based agents, ablations, and limitations.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：摘要和引言明确陈述了论文的主要贡献：AlloSpatial、World2Mind、Spatial Reasoning Harness，以及将其通过 RL 内化到开源权重 agents 中。这些主张由 VSI-Bench 和 MindCube 上的实验支撑，包括免训练的闭源模型结果、基于 Qwen3-VL 训练的 agents、消融实验以及限制性讨论。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the abstract and introduction do not include the claims made in the paper.
> - The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A `[No]` or `[N/A]` answer to this question will not be perceived well by the reviewers.
> - The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings.
> - It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示摘要和引言中并未包含论文提出的主张。
> - 摘要和/或引言应清晰陈述论文中的主张，包括论文贡献以及重要假设和限制。对这个问题回答 `[No]` 或 `[N/A]`，通常不会给审稿人留下好印象。
> - 所提出的主张应与理论和实验结果相匹配，并反映这些结果在其他设定中的可泛化程度。
> - 可以把富有愿景的目标作为动机，只要明确说明这些目标并未由本文实现即可。

### 2. Limitations

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: Does the paper discuss the limitations of the work performed by the authors?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：论文是否讨论了作者所完成工作的局限性？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[Yes]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[Yes]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The paper discusses limitations in the Conclusion and Limitations section, especially the remaining weakness on fine-grained numerical spatial reasoning due to reconstruction drift and imperfect metric calibration. The appendix also reports computational costs and implementation constraints of online World2Mind execution.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：论文在 Conclusion and Limitations 一节中讨论了限制，特别指出，由于重建漂移和不完美的度量校准，细粒度数值空间推理仍然较弱。附录还报告了在线执行 World2Mind 时的计算成本和实现约束。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the paper has no limitation while the answer `[No]` means that the paper has limitations, but those are not discussed in the paper.
> - The authors are encouraged to create a separate “Limitations” section in their paper.
> - The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be.
> - The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated.
> - The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon.
> - The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size.
> - If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness.
> - While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示论文没有局限；回答 `[No]` 则表示论文有局限，但文中没有讨论。
> - 鼓励作者在论文中单独设置一个 “Limitations” 小节。
> - 论文应指出任何强假设，并说明当这些假设被破坏时，结果的稳健性如何（例如独立性假设、无噪声设定、模型正确设定、仅局部成立的渐近近似等）。作者应思考这些假设在实践中可能如何被破坏，以及后果是什么。
> - 作者应反思所提出主张的适用范围，例如方法是否只在少数数据集或少量实验运行上测试过。总体上，实证结果常常依赖隐含假设，这些都应被说明。
> - 作者应反思影响方法性能的因素。例如，一个人脸识别算法在图像分辨率低或光照不足时可能表现不佳；又如，一个语音转文字系统若无法处理技术术语，就可能不适合可靠地为在线讲座提供字幕。
> - 作者应讨论所提算法的计算效率，以及它们如何随数据集规模扩展。
> - 如适用，作者还应讨论该方法在应对隐私和公平性问题时可能存在的局限。
> - 作者或许担心诚实地写出限制会被审稿人当作拒稿理由，但更糟糕的情况可能是审稿人发现了文中未承认的限制。作者应运用最佳判断，并认识到，支持透明度的个体行动对于形成维护社区完整性的规范至关重要。审稿人会被明确要求不要因作者坦诚陈述限制而进行惩罚。

### 3. Theory assumptions and proofs

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：对于每一个理论结果，论文是否提供了完整的假设集合以及完整（且正确）的证明？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[N/A]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[N/A]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The paper does not present theoretical theorems or formal proofs.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：本文没有提出理论定理或形式化证明。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the paper does not include theoretical results.
> - All the theorems, formulas, and proofs in the paper should be numbered and cross-referenced.
> - All assumptions should be clearly stated or referenced in the statement of any theorems.
> - The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition.
> - Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material.
> - Theorems and Lemmas that the proof relies upon should be properly referenced.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示论文不包含理论结果。
> - 论文中的所有定理、公式和证明都应编号并可交叉引用。
> - 任何定理的陈述中，都应明确写出或引用其所依赖的全部假设。
> - 证明可以出现在正文或补充材料中；如果出现在补充材料中，鼓励作者给出简短的 proof sketch，以提供直观理解。
> - 反过来，正文中给出的任何非正式证明，也应由附录或补充材料中的正式证明加以补充。
> - 证明所依赖的定理和引理应被正确引用。

### 4. Experimental result reproducibility

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：论文是否充分披露了复现其主要实验结果所需的全部信息，只要这些信息会影响论文的主要主张和/或结论（无论是否提供了代码和数据）？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[Yes]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[Yes]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The paper describes the benchmarks, data splits, metrics, frame-sampling protocols, baselines, training stages, reward design, evaluation settings, prompt format, and World2Mind service configuration. Additional hyperparameters, computational costs, and case analyses are provided in the appendix.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：论文描述了基准、数据划分、指标、帧采样协议、基线、训练阶段、奖励设计、评测设定、prompt 格式以及 World2Mind 服务配置。附录中还提供了额外超参数、计算成本与案例分析。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the paper does not include experiments.
> - If the paper includes experiments, a `[No]` answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not.
> - If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable.
> - Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed.
> - While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example:
>   - (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm.
>   - (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully.
>   - (c) If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset).
>   - (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示论文不包含实验。
> - 如果论文包含实验，那么对该问题回答 `[No]` 通常不会给审稿人留下好印象：无论是否提供代码和数据，使论文可复现都是重要的。
> - 如果贡献是数据集和/或模型，作者应说明为了让结果可复现或可验证而采取了哪些步骤。
> - 根据贡献类型不同，可复现性可以通过多种方式实现。例如，如果贡献是新架构，完整描述该架构可能就足够；如果贡献是某个具体模型及其实证评测，那么就可能需要让他人能够在同一数据集上复现实验，或者提供对该模型的访问。一般而言，发布代码和数据通常是一种很好的做法，但也可以通过详细的复现实验说明、对托管模型的访问（例如大语言模型）、发布模型 checkpoint，或其他适合该研究的方式来提供可复现性。
> - 虽然 NeurIPS 不要求必须公开代码，但会议要求所有投稿都应提供某种合理的可复现路径，这取决于贡献的性质。例如：
>   - (a) 如果贡献主要是一个新算法，论文应清楚说明如何复现该算法。
>   - (b) 如果贡献主要是一个新模型架构，论文应清晰且完整地描述该架构。
>   - (c) 如果贡献是一个新模型（例如大型语言模型），那么应当要么提供访问该模型以复现实验结果的方式，要么提供复现该模型的方式（例如开放数据集，或说明如何构建数据集）。
>   - (d) 我们承认可复现性在某些情况下可能较难实现，因此作者可以说明其提供可复现性的具体方式。对于闭源模型，模型访问也许会受到某些限制（例如仅对注册用户开放），但其他研究者仍应当拥有某种复现或验证结果的途径。

### 5. Open access to data and code

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：论文是否提供了对数据和代码的开放访问，并附带足够说明，以便忠实复现主要实验结果（如补充材料所述）？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[No]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[No]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The paper uses public benchmarks and datasets where available and provides detailed implementation, training, and evaluation settings in the appendix. Code and checkpoints are not included in the anonymous submission; we plan to release reproducibility materials subject to licensing and anonymization constraints.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：论文在可用时使用公开基准和数据集，并在附录中提供了详细的实现、训练和评测设定。匿名投稿中未包含代码和 checkpoints；我们计划在满足许可证和匿名化约束的前提下，发布可复现材料。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that paper does not include experiments requiring code.
> - Please see the NeurIPS code and data submission guidelines (https://neurips.cc/public/guides/CodeSubmissionPolicy) for more details.
> - While we encourage the release of code and data, we understand that this might not be possible, so `[No]` is an acceptable answer. Papers cannot be rejected simply for not including code, unless this is central to the contribution (e.g., for a new open-source benchmark).
> - The instructions should contain the exact command and environment needed to run to reproduce the results. See the NeurIPS code and data submission guidelines (https://neurips.cc/public/guides/CodeSubmissionPolicy) for more details.
> - The authors should provide instructions on data access and preparation, including how to access the raw data, preprocessed data, intermediate data, and generated data, etc.
> - The authors should provide scripts to reproduce all experimental results for the new proposed method and baselines. If only a subset of experiments are reproducible, they should state which ones are omitted from the script and why.
> - At submission time, to preserve anonymity, the authors should release anonymized versions (if applicable).
> - Providing as much information as possible in supplemental material (appended to the paper) is recommended, but including URLs to data and code is permitted.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示论文不包含需要代码的实验。
> - 更多细节请参见 NeurIPS 代码与数据提交指南（https://neurips.cc/public/guides/CodeSubmissionPolicy）。
> - 我们鼓励发布代码和数据，但也理解这在某些情况下可能做不到，因此回答 `[No]` 是可以接受的。论文不会仅仅因为未提供代码而被拒，除非代码本身是贡献的核心（例如一个新的开源基准）。
> - 说明中应包含复现实验所需的精确命令和运行环境。更多细节请参见 NeurIPS 代码与数据提交指南（https://neurips.cc/public/guides/CodeSubmissionPolicy）。
> - 作者应提供数据访问和准备说明，包括如何获取原始数据、预处理数据、中间数据和生成数据等。
> - 作者应提供脚本，以复现新方法和基线的全部实验结果。如果只有部分实验可复现，则应说明脚本省略了哪些实验以及原因。
> - 在投稿时，为了保持匿名性，作者应发布匿名化版本（如适用）。
> - 建议在补充材料（附在论文后）中尽可能提供更多信息，但也允许包含数据和代码的 URL。

### 6. Experimental setting/details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer) necessary to understand the results?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：论文是否明确给出了理解实验结果所必需的所有训练和测试细节（例如数据划分、超参数、它们的选择方式、优化器类型）？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[Yes]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[Yes]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The main paper specifies datasets, benchmarks, metrics, frame budgets, baselines, model variants, and the two-stage training procedure. The appendix provides GSPO training configurations, reward weights, rollout settings, evaluation parameters, World2Mind parallelization, and computational costs.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：正文中明确给出了数据集、基准、指标、帧预算、基线、模型变体以及两阶段训练流程。附录提供了 GSPO 训练配置、奖励权重、rollout 设定、评测参数、World2Mind 并行化以及计算成本。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the paper does not include experiments.
> - The experimental setting should be presented in the core of the paper to a level of detail that is necessary to appreciate the results and make sense of them.
> - The full details can be provided either with the code, in appendix, or as supplemental material.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示论文不包含实验。
> - 实验设定应在正文中给出足够的细节，以便读者理解并正确解读实验结果。
> - 完整细节可以随代码提供，也可以放在附录或补充材料中。

### 7. Experiment statistical significance

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: Does the paper report error bars suitably and correctly defined or other appropriate information about the statistical significance of the experiments?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：论文是否恰当地报告了定义正确的误差条，或者提供了关于实验统计显著性的其他适当信息？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[No]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[No]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The paper reports benchmark scores on official Tiny subsets and controlled ablations, but does not report error bars or confidence intervals. Repeating full RL training and proprietary-model evaluations multiple times would be computationally expensive; instead, the paper provides task-level breakdowns, ablations, and comparisons across multiple model families.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：论文报告了官方 Tiny 子集上的基准分数和受控消融，但没有给出误差条或置信区间。多次重复完整 RL 训练和闭源模型评测会带来较高计算成本；因此，论文改为提供任务级拆解、消融结果以及跨多个模型家族的比较。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the paper does not include experiments.
> - The authors should answer `[Yes]` if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that support the main claims of the paper.
> - The factors of variability that the error bars are capturing should be clearly stated (for example, train/test split, initialization, random drawing of some parameter, or overall run with given experimental conditions).
> - The method for calculating the error bars should be explained (closed form formula, call to a library function, bootstrap, etc.)
> - The assumptions made should be given (e.g., Normally distributed errors).
> - It should be clear whether the error bar is the standard deviation or the standard error of the mean.
> - It is OK to report 1-sigma error bars, but one should state it. The authors should preferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesis of Normality of errors is not verified.
> - For asymmetric distributions, the authors should be careful not to show in tables or figures symmetric error bars that would yield results that are out of range (e.g., negative error rates).
> - If error bars are reported in tables or plots, the authors should explain in the text how they were calculated and reference the corresponding figures or tables in the text.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示论文不包含实验。
> - 如果结果附带误差条、置信区间或统计显著性检验，至少对支撑主要主张的实验如此，那么作者应回答 `[Yes]`。
> - 误差条所反映的变异来源应被清楚说明（例如训练/测试划分、初始化、某些参数的随机抽样，或在给定实验条件下的整体运行）。
> - 应解释误差条的计算方法（闭式公式、库函数调用、bootstrap 等）。
> - 还应给出所采用的假设（例如误差服从正态分布）。
> - 需要明确误差条表示的是标准差还是均值标准误。
> - 报告 1-sigma 误差条是可以的，但应明确说明。如果误差正态性假设并未被验证，那么与其说有 96% CI，不如优先报告 2-sigma 误差条。
> - 对于非对称分布，作者应注意不要在表格或图中画出会导致越界结果的对称误差条（例如出现负的错误率）。
> - 如果表格或图中报告了误差条，作者应在正文中说明其计算方式，并引用相应图表。

### 8. Experiments compute resources

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproduce the experiments?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：对于每个实验，论文是否提供了复现实验所需的充足计算资源信息（计算节点类型、内存、执行时间）？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[Yes]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[Yes]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The appendix reports the training infrastructure, including 8 NVIDIA H200 GPUs, trainer process counts, GSPO update time, approximate wall-clock training time for AlloSpatial-4B and AlloSpatial-8B, World2Mind service workers, and inference throughput.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：附录报告了训练基础设施，包括 8 张 NVIDIA H200 GPU、trainer process 数量、GSPO update 时间、AlloSpatial-4B 和 AlloSpatial-8B 的近似 wall-clock 训练时间、World2Mind service workers，以及推理吞吐。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the paper does not include experiments.
> - The paper should indicate the type of compute workers CPU or GPU, internal cluster, or cloud provider, including relevant memory and storage.
> - The paper should provide the amount of compute required for each of the individual experimental runs as well as estimate the total compute.
> - The paper should disclose whether the full research project required more compute than the experiments reported in the paper (e.g., preliminary or failed experiments that didn’t make it into the paper).

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示论文不包含实验。
> - 论文应说明计算资源类型，如 CPU 或 GPU、内部集群或云提供商，并给出相关内存和存储信息。
> - 论文应提供每一项具体实验运行所需的计算量，并估计总体计算量。
> - 论文还应披露整个研究项目是否使用了比文中报告实验更多的计算资源（例如未写入论文的初步实验或失败实验）。

### 9. Code of ethics

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: Does the research conducted in the paper conform, in every respect, with the NeurIPS Code of Ethics https://neurips.cc/public/EthicsGuidelines?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：本文所开展的研究是否在各方面都符合 NeurIPS Code of Ethics（https://neurips.cc/public/EthicsGuidelines）？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[Yes]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[Yes]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The work uses public benchmarks, existing foundation models, and generated tool-use trajectories for spatial reasoning research. It does not involve deception, human-subject experimentation, private personal data collection, or unsafe data release.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：该工作使用公开基准、现有基础模型以及生成的工具使用轨迹来开展空间推理研究。它不涉及欺骗、人类受试者实验、私人个人数据收集或不安全的数据发布。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the authors have not reviewed the NeurIPS Code of Ethics.
> - If the authors answer `[No]`, they should explain the special circumstances that require a deviation from the Code of Ethics.
> - The authors should make sure to preserve anonymity (e.g., if there is a special consideration due to laws or regulations in their jurisdiction).

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示作者尚未审阅 NeurIPS Code of Ethics。
> - 如果作者回答 `[No]`，应解释为何存在必须偏离该伦理规范的特殊情况。
> - 作者应确保维持匿名性（例如，如果其所在司法辖区的法律法规带来特殊考量）。

### 10. Broader impacts

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: Does the paper discuss both potential positive societal impacts and negative societal impacts of the work performed?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：论文是否同时讨论了该工作可能带来的正面社会影响和负面社会影响？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[Yes]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[Yes]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The paper discusses AlloSpatial as foundational research toward more spatially capable multimodal and embodied agents. It also notes that incorrect spatial reasoning or over-trusting reconstructed maps can be harmful in safety-critical settings, motivating the harness-based cross-validation design and the limitation discussion on metric reliability.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：论文将 AlloSpatial 讨论为一项基础性研究，目标是推动更具空间能力的多模态和具身 agents。同时，论文也指出，在安全关键场景中，错误的空间推理或对重建地图的过度信任可能造成危害，这正是 harness 式交叉验证设计和对度量可靠性限制进行讨论的动机。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that there is no societal impact of the work performed.
> - If the authors answer `[N/A]` or `[No]`, they should explain why their work has no societal impact or why the paper does not address societal impact.
> - Examples of negative societal impacts include potential malicious or unintended uses (e.g., disinformation, generating fake profiles, surveillance), fairness considerations (e.g., deployment of technologies that could make decisions that unfairly impact specific groups), privacy considerations, and security considerations.
> - The conference expects that many papers will be foundational research and not tied to particular applications, let alone deployments. However, if there is a direct path to any negative applications, the authors should point it out. For example, it is legitimate to point out that an improvement in the quality of generative models could be used to generate Deepfakes for disinformation. On the other hand, it is not needed to point out that a generic algorithm for optimizing neural networks could enable people to train models that generate Deepfakes faster.
> - The authors should consider possible harms that could arise when the technology is being used as intended and functioning correctly, harms that could arise when the technology is being used as intended but gives incorrect results, and harms following from (intentional or unintentional) misuse of the technology.
> - If there are negative societal impacts, the authors could also discuss possible mitigation strategies (e.g., gated release of models, providing defenses in addition to attacks, mechanisms for monitoring misuse, mechanisms to monitor how a system learns from feedback over time, improving the efficiency and accessibility of ML).

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示该工作没有社会影响。
> - 如果作者回答 `[N/A]` 或 `[No]`，则应解释为什么他们的工作没有社会影响，或者为什么论文没有讨论社会影响。
> - 负面社会影响的例子包括潜在的恶意或非预期用途（如虚假信息、生成假身份、监控）、公平性问题（例如部署可能对特定群体造成不公平影响的技术）、隐私问题以及安全问题。
> - 会议预期很多论文都是基础研究，并不直接绑定具体应用，更不用说实际部署。然而，如果存在直接通向负面应用的路径，作者应指出。例如，指出生成模型质量的提升可能被用于制造用于虚假信息传播的 Deepfakes 是合理的；但另一方面，没有必要指出一个通用神经网络优化算法会让人更快训练出生成 Deepfakes 的模型。
> - 作者应考虑如下几类可能伤害：技术按预期正常工作时可能带来的伤害；技术按预期使用但给出错误结果时可能带来的伤害；以及技术被（有意或无意）滥用时可能带来的伤害。
> - 如果存在负面社会影响，作者还可以讨论可能的缓解策略（例如受控发布模型、同时提供防御机制、监控滥用的机制、监控系统如何随着反馈学习的机制，以及提升机器学习效率和可及性的方法）。

### 11. Safeguards

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: Does the paper describe safeguards that have been put in place for responsible release of data or models that have a high risk for misuse (e.g., pre-trained language models, image generators, or scraped datasets)?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：论文是否说明了为负责任地发布高滥用风险数据或模型（例如预训练语言模型、图像生成器或爬取数据集）而采取的防护措施？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[N/A]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[N/A]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The paper does not introduce a scraped dataset, image generator, or high-risk pretrained foundation model release. The proposed method is evaluated as a spatial reasoning framework, and any future release of code or checkpoints will follow the licenses and usage restrictions of the underlying models and datasets.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：本文没有引入爬取数据集、图像生成器或高风险预训练基础模型的发布。所提出的方法被作为一个空间推理框架来评估，而未来若发布代码或 checkpoints，也将遵循底层模型和数据集的许可证与使用限制。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the paper poses no such risks.
> - Released models that have a high risk for misuse or dual-use should be released with necessary safeguards to allow for controlled use of the model, for example by requiring that users adhere to usage guidelines or restrictions to access the model or implementing safety filters.
> - Datasets that have been scraped from the Internet could pose safety risks. The authors should describe how they avoided releasing unsafe images.
> - We recognize that providing effective safeguards is challenging, and many papers do not require this, but we encourage authors to take this into account and make a best faith effort.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示论文不存在这类风险。
> - 对于具有高滥用风险或双重用途风险的已发布模型，应当配套必要的防护措施，以实现受控使用，例如要求用户遵守使用指南或访问限制，或实施安全过滤器。
> - 从互联网抓取的数据集可能带来安全风险。作者应说明他们如何避免发布不安全图像。
> - 我们认识到，提供有效的防护措施并不容易，而且许多论文并不需要这一点，但我们鼓励作者对此加以考虑，并尽最大努力做出善意尝试。

### 12. Licenses for existing assets

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: Are the creators or original owners of assets (e.g., code, data, models), used in the paper, properly credited and are the license and terms of use explicitly mentioned and properly respected?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：论文中使用的现有资产（如代码、数据、模型）的创建者或原始所有者，是否得到了适当致谢，并且其许可证和使用条款是否被明确说明并得到正确遵守？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[Yes]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[Yes]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The paper cites the existing datasets, benchmarks, foundation models, geometry models, segmentation models, and spatial reasoning baselines used in the study. We use these assets for research evaluation and training under their respective terms and do not redistribute restricted proprietary models or datasets.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：论文引用了研究中使用的现有数据集、基准、基础模型、几何模型、分割模型以及空间推理基线。我们在各自条款约束下使用这些资产进行研究评测和训练，并且不会重新分发受限制的闭源模型或数据集。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the paper does not use existing assets.
> - The authors should cite the original paper that produced the code package or dataset.
> - The authors should state which version of the asset is used and, if possible, include a URL.
> - The name of the license (e.g., `CC-BY 4.0`) should be included for each asset.
> - For scraped data from a particular source (e.g., website), the copyright and terms of service of that source should be provided.
> - If assets are released, the license, copyright information, and terms of use in the package should be provided. For popular datasets, `paperswithcode.com/datasets` has curated licenses for some datasets. Their licensing guide can help determine the license of a dataset.
> - For existing datasets that are re-packaged, both the original license and the license of the derived asset (if it has changed) should be provided.
> - If this information is not available online, the authors are encouraged to reach out to the asset’s creators.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示论文未使用现有资产。
> - 作者应引用产生该代码包或数据集的原始论文。
> - 作者应说明所使用资产的版本，并在可能时给出 URL。
> - 每项资产都应给出其许可证名称（例如 `CC-BY 4.0`）。
> - 对于来自特定来源（如网站）的爬取数据，应提供该来源的版权和服务条款。
> - 如果发布了资产，则应在包中提供许可证、版权信息和使用条款。对于常见数据集，`paperswithcode.com/datasets` 为其中一些数据集整理了许可证，其 licensing guide 可帮助确定数据集许可证。
> - 对于重新打包的现有数据集，应同时给出原始许可证和派生资产的许可证（如果发生了变化）。
> - 如果这些信息在线不可用，鼓励作者联系资产创建者。

### 13. New assets

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: Are new assets introduced in the paper well documented and is the documentation provided alongside the assets?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：论文引入的新资产是否有完善文档，并且这些文档是否与资产一同提供？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[Yes]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[Yes]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The paper introduces AlloSpatial, World2Mind, the Spatial Reasoning Harness, and trained AlloSpatial agents. The method, prompts, tool schema, reward design, training configuration, evaluation setup, and service parallelization are documented in the main paper and appendix; release of code or checkpoints will follow anonymization and licensing constraints.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：论文引入了 AlloSpatial、World2Mind、Spatial Reasoning Harness，以及训练后的 AlloSpatial agents。方法、prompts、工具 schema、奖励设计、训练配置、评测设定和服务并行化都已在正文和附录中记录；代码或 checkpoints 的发布将遵循匿名化与许可证约束。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the paper does not release new assets.
> - Researchers should communicate the details of the dataset/code/model as part of their submissions via structured templates. This includes details about training, license, limitations, etc.
> - The paper should discuss whether and how consent was obtained from people whose asset is used.
> - At submission time, remember to anonymize your assets (if applicable). You can either create an anonymized URL or include an anonymized zip file.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示论文不发布新资产。
> - 研究者应通过结构化模板，在投稿中传达数据集/代码/模型的细节。这包括训练、许可证、局限等信息。
> - 论文应讨论是否以及如何从相关资产所属人员那里获得同意。
> - 在投稿时，请记得对资产进行匿名化（如适用）。你可以创建匿名 URL，或者附上匿名压缩包。

### 14. Crowdsourcing and research with human subjects

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: For crowdsourcing experiments and research with human subjects, does the paper include the full text of instructions given to participants and screenshots, if applicable, as well as details about compensation (if any)?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：对于众包实验和涉及人类受试者的研究，论文是否包含提供给参与者的完整指令文本和截图（如适用），以及报酬细节（如果有）？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[N/A]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[N/A]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The paper does not involve crowdsourcing experiments or research with human subjects. All evaluations are performed on existing benchmarks and generated model trajectories.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：本文不涉及众包实验，也不涉及人类受试者研究。所有评测都在现有基准和生成的模型轨迹上进行。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the paper does not involve crowdsourcing nor research with human subjects.
> - Including this information in the supplemental material is fine, but if the main contribution of the paper involves human subjects, then as much detail as possible should be included in the main paper.
> - According to the NeurIPS Code of Ethics, workers involved in data collection, curation, or other labor should be paid at least the minimum wage in the country of the data collector.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示论文不涉及众包，也不涉及人类受试者研究。
> - 将这些信息放在补充材料中是可以的，但如果论文的主要贡献涉及人类受试者，则应尽可能在正文中包含详细信息。
> - 根据 NeurIPS Code of Ethics，参与数据收集、整理或其他劳动的工作人员，应至少获得其所在国家最低工资标准的报酬。

### 15. Institutional review board (IRB) approvals or equivalent for research with human subjects

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: Does the paper describe potential risks incurred by study participants, whether such risks were disclosed to the subjects, and whether Institutional Review Board (IRB) approvals (or an equivalent approval/review based on the requirements of your country or institution) were obtained?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：论文是否描述了研究参与者可能承担的风险、这些风险是否向受试者披露，以及是否获得了 Institutional Review Board (IRB) 批准（或依据所在国家/机构要求的等效批准/审查）？

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[N/A]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[N/A]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: The paper does not involve human-subject research, user studies, or collection of participant data. Therefore, IRB approval or equivalent review is not applicable.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：本文不涉及人类受试者研究、用户研究或参与者数据收集。因此，IRB 批准或等效审查不适用。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the paper does not involve crowdsourcing nor research with human subjects.
> - Depending on the country in which research is conducted, IRB approval (or equivalent) may be required for any human subjects research. If you obtained IRB approval, you should clearly state this in the paper.
> - We recognize that the procedures for this may vary significantly between institutions and locations, and we expect authors to adhere to the NeurIPS Code of Ethics and the guidelines for their institution.
> - For initial submissions, do not include any information that would break anonymity (if applicable), such as the institution conducting the review.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示论文不涉及众包，也不涉及人类受试者研究。
> - 视研究开展所在国家而定，任何人类受试者研究都可能需要 IRB 批准（或等效审查）。如果你获得了 IRB 批准，应在论文中明确写出。
> - 我们认识到，这一流程在不同机构和地区之间可能差异很大，并期望作者遵守 NeurIPS Code of Ethics 以及其所在机构的相关指南。
> - 对于初稿投稿，不要包含任何会破坏匿名性的信息（如适用），例如实施审查的机构名称。

### 16. Declaration of LLM usage

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Question: Does the paper describe the usage of LLMs if it is an important, original, or non-standard component of the core methods in this research? Note that if the LLM is used only for writing, editing, or formatting purposes and does not impact the core methodology, scientific rigor, or originality of the research, declaration is not required.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 问题：如果 LLM 是本研究核心方法中的重要、原创或非标准组成部分，论文是否描述了其使用方式？请注意，如果 LLM 仅用于写作、编辑或排版，且不影响研究的核心方法、科学严谨性或原创性，则无需声明。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Answer: `[Yes]`

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 回答：`[Yes]`

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Justification: LLMs and MFMs are core components of the research. The paper describes the use of proprietary models for training-free evaluation and trajectory distillation, Qwen3-VL as the open-weight backbone for AlloSpatial agents, and LLM-based multi-turn tool-use reasoning as part of the proposed method.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理由：LLM 和 MFM 是该研究的核心组成部分。论文描述了闭源模型在免训练评测和轨迹蒸馏中的作用、Qwen3-VL 作为 AlloSpatial agents 的开源权重 backbone，以及基于 LLM 的多轮工具使用推理如何构成所提方法的一部分。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Guidelines:
>
> - The answer `[N/A]` means that the core method development in this research does not involve LLMs as any important, original, or non-standard components.
> - Please refer to our LLM policy in the NeurIPS handbook for what should or should not be described.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 指南：
>
> - 回答 `[N/A]` 表示本研究的核心方法开发并未将 LLM 作为重要、原创或非标准组成部分。
> - 关于哪些内容应描述、哪些无需描述，请参见 NeurIPS handbook 中的 LLM policy。
