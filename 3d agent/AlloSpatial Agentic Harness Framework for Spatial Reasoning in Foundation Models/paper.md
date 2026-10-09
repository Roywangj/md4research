# AlloSpatial: Agentic Harness Framework for Spatial Reasoning in Foundation Models

**Authors:** Shouwei Ruan, Bin Wang, Zhenyu Wu, Qihui Zhu, Yuxiang Zhang, Jingzhi Li, Yubin Wang, Xingxing Wei  
**Source:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/QXAH89IU/Ruan 等 - 2026 - AlloSpatial Agentic Harness Framework for Spatial Reasoning in Foundation Models.pdf`  
**Detected source format:** selectable-text PDF (`pdf-text`)  
**Reader type:** complete source-order English–Chinese full-paper reader with traceable figures, tables, equations, prompts, examples, references, appendices, and checklist.

## Page / Section Index

| Pages | Section |
|---:|---|
| 1 | Title, Authors, and Affiliations |
| 1 | Abstract |
| 1-3 | 1 Introduction |
| 3-4 | 2 Related Work: Spatial Reasoning in Foundation Models |
| 4-7 | 3 Methodology |
| 7-9 | 4 Experiments |
| 9-10 | 5 Conclusion & Limitations |
| 11-13 | References |
| 13-14 | Appendix A — Training & Evaluation Configuration |
| 14 | Appendix B — World2Mind Service Parallelization |
| 15-16 | Appendix C — Spatial Reasoning Harness Prompts |
| 16-22 | Appendix D — Case Analysis |
| 22 | Appendix E — Computational Costs in Training and Inference |
| 23-30 | NeurIPS Paper Checklist |

## Terminology Ledger

| English term | 中文 | Usage note |
|---|---|---|
| allocentric | 非自我中心 / 他心中心 | 相对于观察者自身坐标系的全局环境坐标表征；本文统一译为“非自我中心”。 |
| egocentric | 自我中心 | 以当前观察者/相机为参照的局部视角。 |
| AlloSpatial | AlloSpatial | 论文框架名称，不翻译。 |
| World2Mind | World2Mind | 即插即用认知建图沙盒，不翻译。 |
| Allocentric-Spatial Tree (AST) | 非自我中心空间树（AST） | 保留 AST 缩写。 |
| Spatial Reasoning Harness | 空间推理 Harness | Harness 表示约束工具调用、证据收集与仲裁的协议；保留英文以免弱化机制含义。 |
| Landmark Cognitive Map | 地标认知地图 | 用于对象拓扑与度量关系。 |
| Route Cognitive Map | 路线认知地图 | 用于可遍历性、可通行性与轨迹推理。 |
| geometry-semantic arbitration | 几何—语义仲裁 | 比较、发现冲突并交叉验证两类证据。 |
| modality-decoupled cue collection | 模态解耦的线索收集 | 先分别收集视觉、AST 文本与地图证据，再融合。 |
| Harness-Gated Trajectory Reward (HGTR) | Harness 门控轨迹奖励（HGTR） | 以轨迹整体为单位的结构与正确性门控奖励。 |
| Group Sequence Policy Optimization (GSPO) | 组序列策略优化（GSPO） | 强化学习算法名称。 |
| footprint | 占地轮廓 | 对象在地平面上的矩形或椭圆近似。 |
| traversability / passability | 可遍历性 / 可通行性 | 路线地图中的地面与通道属性。 |
| mean relative accuracy (MRA) | 平均相对准确率（MRA） | 用于数值问答的指标。 |
| cold start | 冷启动 | 先用蒸馏轨迹做监督微调，再进入 RL。 |
| blind setting | 盲测设置 | 移除视觉输入，只向模型提供结构化 AST 文本。 |
| trajectory | 轨迹 | 包含历史、推理/工具动作、工具观察与最终答案的完整多轮序列。 |

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> AlloSpatial: Agentic Harness Framework for Spatial Reasoning in Foundation Models


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> AlloSpatial：面向基础模型空间推理的智能体式 Harness 框架


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Shouwei Ruan¹, Bin Wang², Zhenyu Wu¹, Qihui Zhu¹, Yuxiang Zhang², Jingzhi Li³, Yubin Wang²*, Xingxing Wei¹†. ¹ Institute of Artificial Intelligence, Beihang University; ² Huawei Noah’s Ark Lab; ³ University of Science and Technology Beijing. * Project leader. † Corresponding author.


> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> Shouwei Ruan¹、Bin Wang²、Zhenyu Wu¹、Qihui Zhu¹、Yuxiang Zhang²、Jingzhi Li³、Yubin Wang²*、Xingxing Wei¹†。¹ 北京航空航天大学人工智能研究院；² 华为诺亚方舟实验室；³ 北京科技大学。* 项目负责人。† 通讯作者。


## Abstract


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Multimodal Foundation Models (MFMs) have made substantial progress, yet remain fragile in spatial reasoning over the physical world. A key bottleneck lies in their inability to transform local egocentric observations into a global allocentric spatial representation. To address this, we propose AlloSpatial, an agentic framework for allocentric spatial cognition in foundation models. AlloSpatial introduces World2Mind, a plug-and-play cognitive mapping sandbox that converts egocentric observations into structured allocentric priors, including Allocentric-Spatial Trees and route maps that support querying object topology, geometric relations, passability, and trajectories. To utilize these priors reliably under noisy reconstruction and ambiguous visual evidence, AlloSpatial introduces a Spatial Reasoning Harness for tool-use judgment, modality-decoupled cue collection, and geometry-semantic arbitration. We further internalize this process in Qwen3-VL through cold-start reinforcement learning with a harness-gated trajectory-level reward. Experiments on VSI-Bench and MindCube show that AlloSpatial improves proprietary models by 5%–18% in a training-free setting, while ASTs alone support strong spatial reasoning even when visual inputs are removed. The trained AlloSpatial agents further outperform larger general-purpose models and competitive spatial baselines, suggesting that structured allocentric representations, active tool use, and verifiable reasoning offer a promising route toward spatially capable foundation models. Our code: https://github.com/Heathcliff-saku/AlloSpatial


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 多模态基础模型（MFM）已取得显著进展，但在对物理世界进行空间推理时仍很脆弱。一个关键瓶颈在于，它们无法把局部的自我中心观察转化为全局的非自我中心空间表征。为此，我们提出 AlloSpatial：一种让基础模型具备非自我中心空间认知能力的智能体式框架。AlloSpatial 引入即插即用的认知建图沙盒 World2Mind，把自我中心观察转化为结构化的非自我中心先验，其中包括可查询对象拓扑、几何关系、可通行性与轨迹的 Allocentric-Spatial Tree（AST）和路线图。为了在重建噪声和视觉证据含混的情况下可靠利用这些先验，AlloSpatial 又提出 Spatial Reasoning Harness，用于工具使用判断、模态解耦的线索收集以及几何—语义仲裁。我们进一步通过冷启动强化学习，并采用 harness 门控的轨迹级奖励，把这一过程内化到 Qwen3-VL 中。在 VSI-Bench 和 MindCube 上的实验表明：在免训练设置中，AlloSpatial 可使专有模型提升 5%–18%；即使移除视觉输入，仅 AST 也能支持强大的空间推理。训练后的 AlloSpatial 智能体还超过了规模更大的通用模型和有竞争力的空间基线，说明结构化非自我中心表征、主动工具使用与可验证推理，为构建具有空间能力的基础模型提供了一条有前景的道路。代码：https://github.com/Heathcliff-saku/AlloSpatial


## 1 Introduction


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Multimodal Foundation Models (MFMs) [1, 25, 32, 13, 33] have made substantial progress in cross-modal understanding and reasoning. Yet their ability to reason about 3D space in the physical world remains fragile [41, 35, 19, 17, 28]. A central limitation is that current MFMs largely operate over local, transient, and egocentric observations, lacking a mechanism to transform partial perceptual evidence into global, persistent, and queryable mental representations that reliably bridge semantic understanding and geometric relations [35, 33, 42].


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 多模态基础模型（MFM）[1, 25, 32, 13, 33] 在跨模态理解和推理方面取得了显著进展。然而，它们对物理世界三维空间进行推理的能力仍很脆弱 [41, 35, 19, 17, 28]。一个核心局限是，现有 MFM 主要处理局部、短暂且以自我为中心的观察，缺少一种机制来把部分感知证据转化为全局、持久且可查询的心智表征，从而可靠地连接语义理解与几何关系 [35, 33, 42]。


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Existing approaches have improved spatial reasoning along three paradigms. Vision-centric methods post-train MFMs on large-scale 3D-grounded samples, encouraging models to infer depth, size, location, or spatial relations directly from limited visual observations [10, 7, 21, 39]. While effective under in-distribution settings, recent studies [27, 16, 40] indicate that their gains are often coupled to the statistics of the training distribution and may degrade under shifts in scene layout. Geometry-centric methods inject explicit spatial signals, such as depth maps, point clouds, or learned 3D representations, to compensate for the weak geometric grounding of 2D visual inputs [11, 8, 23, 38]. Although useful, such signals introduce nontrivial cross-modal alignment challenges [45] and often require geometry-rich paired data and costly training for specialized architectures. More recently, tool-augmented spatial reasoning enables models to call tools or task-specific models (e.g., 3D reconstruction, novel-view rendering, depth estimation, or pose estimation) for active evidence acquisition [46, 20, 9]. However, these tools typically return pixel-space observations or low-level geometric measurements, leaving the model to assemble high-level spatial structure through a long, error-prone reasoning chain. As a result, noisy or incomplete tool evidence can be absorbed rather than challenged, leading to incorrect reasoning results.


> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 已有工作沿三种范式改进空间推理。以视觉为中心的方法使用大规模三维落地样本对 MFM 进行后训练，促使模型直接从有限视觉观察中推断深度、尺寸、位置或空间关系 [10, 7, 21, 39]。这类方法在同分布设置中有效，但近期研究 [27, 16, 40] 表明，其增益往往与训练分布统计规律耦合，并可能在场景布局变化时下降。以几何为中心的方法注入深度图、点云或学习得到的三维表征等显式空间信号，以弥补二维视觉输入几何落地不足的问题 [11, 8, 23, 38]。这些信号虽有帮助，却带来不容忽视的跨模态对齐挑战 [45]，并且往往需要几何信息丰富的配对数据和针对专用架构的高成本训练。最近，工具增强的空间推理使模型能够调用工具或任务特定模型（如三维重建、新视角渲染、深度估计或姿态估计）来主动获取证据 [46, 20, 9]。然而，这些工具通常返回像素空间观察或低层几何测量，仍需模型通过冗长且易错的推理链组装高层空间结构。因此，模型可能直接吸收而非质疑带噪或不完整的工具证据，最终得到错误的推理结果。


> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Indeed, biological intelligence (BI) offers a natural blueprint for overcoming the spatial reasoning bottleneck. Decades of cognitive science research suggest that BI does not passively match each incoming egocentric observation in isolation; instead, it compresses local perceptual experience into stable allocentric cognitive maps [3], supporting mental simulation [24, 31, 2]. This suggests a sharper hypothesis: robust spatial reasoning is constrained not merely by coarse 2D perception or limited 3D supervision, but by the absence of an allocentric spatial cognition framework that can be actively invoked, precisely queried, and cross-validated by foundation models. Building on this view, we propose AlloSpatial, an agentic framework that enables reasoning over structured allocentric spatial representations rather than relying solely on egocentric observations.


> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 事实上，生物智能（BI）为突破空间推理瓶颈提供了天然蓝图。数十年的认知科学研究表明，生物智能并不会孤立地、被动匹配每个新到来的自我中心观察；相反，它把局部感知经验压缩为稳定的非自我中心认知地图 [3]，以支持心智模拟 [24, 31, 2]。由此可提出一个更明确的假设：制约稳健空间推理的，不只是粗糙的二维感知或有限的三维监督，而是缺少一个可由基础模型主动调用、精确查询并交叉验证的非自我中心空间认知框架。基于这一观点，我们提出 AlloSpatial，使模型能够在结构化的非自我中心空间表征上推理，而不再只依赖自我中心观察。


> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> As illustrated in Fig. 1(A), at the core of AlloSpatial is World2Mind, a plug-and-play cognitive mapping sandbox that transforms egocentric videos or images into queryable allocentric spatial priors. Given semantic categories specified by the agent, World2Mind integrates a robust semantic-geometry alignment pipeline to construct a sparse semantic point cloud. It then distills this point cloud into two complementary cognitive maps: a Landmark Cognitive Map for object-centric topological reasoning and a Route Cognitive Map for traversability, passability, and trajectory reasoning. Its central representation is the proposed Allocentric-Spatial Tree (AST), a directed acyclic graph whose nodes correspond to stable environmental landmarks and whose attributes encode centroid, footprint, principal axes, orientation, height range, and hierarchical containment. Unlike grid maps that discard object identity [41, 35, 30] or abstract semantic graphs that omit metric geometry [15, 29], AST compresses noisy 3D reconstruction into compact and structured spatial memory.


> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 如图 1(A) 所示，AlloSpatial 的核心是 World2Mind：一个即插即用的认知建图沙盒，可把自我中心视频或图像转化为可查询的非自我中心空间先验。给定智能体指定的语义类别，World2Mind 集成稳健的语义—几何对齐流水线来构建稀疏语义点云；随后把点云提炼成两种互补的认知地图：用于以对象为中心拓扑推理的 Landmark Cognitive Map，以及用于可遍历性、可通行性和轨迹推理的 Route Cognitive Map。其核心表征是作者提出的 Allocentric-Spatial Tree（AST），一种有向无环图：节点对应稳定的环境地标，属性编码质心、占地轮廓、主轴、方向、高度范围与层级包含关系。不同于丢弃对象身份的栅格地图 [41, 35, 30] 或省略度量几何的抽象语义图 [15, 29]，AST 把有噪声的三维重建压缩为紧凑、结构化的空间记忆。


### Figure 1

![AlloSpatial inference and training pipeline](figure_1_pipeline.png)

**Caption:** Figure 1: AlloSpatial inference and training pipeline. A, At inference time, AlloSpatial takes egocentric videos or multi-view observations and follows a three-stage Spatial Reasoning Harness to invoke World2Mind, acquire allocentric spatial knowledge, and arbitrate evidence before answering. B, To internalize this harness, we distill and filter high-quality harness-following trajectories from proprietary models for supervised cold start, and further optimize the policy with live World2Mind interaction and a Harness-Gated Trajectory Reward.

**Caption[CN]:** 图 1：AlloSpatial 的推理与训练流水线。A，在推理时，AlloSpatial 接收自我中心视频或多视图观察，遵循三阶段 Spatial Reasoning Harness 调用 World2Mind、获取非自我中心空间知识，并在作答前仲裁证据。B，为把该 harness 内化到模型中，我们从专有模型中蒸馏并筛选高质量的遵循 harness 的轨迹，用于监督式冷启动；随后借助实时 World2Mind 交互和 Harness-Gated Trajectory Reward 进一步优化策略。


> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> However, structured spatial priors alone do not guarantee reliable reasoning, especially when reconstruction drift and perception errors often occur. AlloSpatial therefore introduces a three-stage Spatial Reasoning Harness to regulate how models invoke tools, collect evidence, and arbitrate across modalities. The harness first determines whether a question truly requires cognitive mapping, then decouples evidence collection from raw visual inputs, AST-structured text, and optional top-down visualization maps produced by World2Mind, and finally performs geometry-semantics interleaved reasoning to identify conflicts and cross-validate the final answer. To internalize the reasoning harness, we train an AlloSpatial agent instantiated from Qwen3-VL (see Fig. 1(B)). We first use World2Mind within the harness prompt to distill high-quality trajectories from frontier proprietary models, and then apply supervised cold-start fine-tuning to bootstrap tool invocation and reasoning structure. The agent is subsequently optimized with Group Sequence Policy Optimization (GSPO) [48]. Since RL over long tool-use trajectories is vulnerable to reward hacking and redundant tool calls, we introduce a Harness-Gated Trajectory Reward (HGTR) that evaluates the trajectory as a whole rather than isolated actions. HGTR jointly accounts for answer correctness, harness compliance, tool-use validity, and response efficiency, while enforcing two key gates: answer accuracy is credited only when the trajectory follows the required reasoning structure, and tool-use rewards are granted only when valid tool calls contribute to a correct answer. This training strategy stabilizes optimization and enables the agent to acquire efficient and deliberate allocentric spatial reasoning behaviors.


> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 然而，仅有结构化空间先验并不能保证推理可靠，尤其是在经常出现重建漂移和感知错误时。因此，AlloSpatial 引入三阶段 Spatial Reasoning Harness，用以规范模型如何调用工具、收集证据并在模态间进行仲裁。Harness 首先判断问题是否确实需要认知建图，随后分别从原始视觉输入、AST 结构化文本和 World2Mind 生成的可选俯视可视化地图收集证据，最后执行几何—语义交错推理，以发现冲突并交叉验证最终答案。为内化这一推理 harness，作者以 Qwen3-VL 为基础训练 AlloSpatial 智能体（见图 1(B)）。首先在 harness 提示中使用 World2Mind，从前沿专有模型蒸馏高质量轨迹；再通过监督式冷启动微调来启动工具调用与推理结构。随后使用 Group Sequence Policy Optimization（GSPO）[48] 优化智能体。长工具使用轨迹上的 RL 容易遭遇奖励投机和冗余调用，因此作者提出 Harness-Gated Trajectory Reward（HGTR），从整体上评价轨迹而非孤立动作。HGTR 联合考虑答案正确性、harness 合规性、工具使用有效性和响应效率，并实施两道关键门控：只有轨迹遵循所要求的推理结构时才计入答案准确性；只有有效工具调用促成正确答案时才给予工具使用奖励。该训练策略稳定了优化，并使智能体获得高效、审慎的非自我中心空间推理行为。


> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> We evaluate AlloSpatial on VSI-Bench [41] and MindCube [35], covering various spatial reasoning tasks across egocentric videos and sparse multi-view images. As a training-free plug-in, World2Mind combined with the Spatial Reasoning Harness consistently improves frontier commercial models, including GPT-5.2, Claude-4.6, and Gemini-3, with overall gains of approximately 5%–18%. Under a “blind” setting in which visual inputs are removed, ASTs alone achieve strong 3D reasoning performance, suggesting that high-quality allocentric priors can elicit spatial mental simulation even without direct visual evidence. After cold-start RL, AlloSpatial agents instantiated from Qwen3-VL surpass larger frontier models and competitive methods across multiple tasks. In summary, our study indicates that coupling structured allocentric representations with an agentic reasoning harness offers a promising route toward overcoming the spatial cognition bottleneck of foundation models.


> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 作者在 VSI-Bench [41] 和 MindCube [35] 上评估 AlloSpatial，覆盖自我中心视频和稀疏多视图图像中的多种空间推理任务。作为免训练插件，World2Mind 与 Spatial Reasoning Harness 的组合持续提升 GPT-5.2、Claude-4.6 和 Gemini-3 等前沿商业模型，总体增益约为 5%–18%。在移除视觉输入的“盲测”设置中，仅凭 AST 也能取得很强的三维推理表现，说明即使没有直接视觉证据，高质量非自我中心先验也能诱发空间心智模拟。经过冷启动 RL 后，基于 Qwen3-VL 的 AlloSpatial 智能体在多项任务上超过规模更大的前沿模型和有竞争力的方法。总之，本研究表明，把结构化非自我中心表征与智能体式推理 harness 结合，是突破基础模型空间认知瓶颈的一条有前景的路径。


## 2 Related Work: Spatial Reasoning in Foundation Models


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Recent benchmarks have exposed spatial reasoning as a persistent weakness of MFMs. VSI-Bench [41] and VSI-Super [42] evaluate egocentric video-based spatial intelligence. MindCube [35] probes sparse multi-view cognitive mapping, while other benchmarks [19, 28] extend evaluation to broader text-based and multimodal scenarios. Together, these studies suggest that the bottleneck is not merely visual recognition, but the absence of reasoning-ready spatial mental representations.


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 近期基准揭示，空间推理是 MFM 长期存在的弱点。VSI-Bench [41] 和 VSI-Super [42] 评估基于自我中心视频的空间智能；MindCube [35] 探测稀疏多视图认知建图；其他基准 [19, 28] 则把评估扩展到更广泛的纯文本与多模态情境。这些研究共同表明，瓶颈不只是视觉识别，而是缺少可直接用于推理的空间心智表征。


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Vision-centric learning. Vision-centric methods improve spatial reasoning by post-training MFMs with large-scale 3D-grounded supervision. SpatialVLM [7], Cambrian-S [42], and related works [26, 35, 12] construct spatial VQA data from real-world images, videos, or 3D annotations to supervise spatial relation understanding. SpatialReasoner [21] and Spatial-MLLM [39] further introduce intermediate 3D representations or explicit reasoning traces to structure spatial inference. These methods show that spatially grounded supervision can improve benchmark performance. Still, their gains may remain coupled to training-distribution statistics and degrade under shifts in scene layout, viewpoint, or object composition. Recent analyses further suggest that MFMs can exploit semantic shortcuts rather than acquire robust spatial cognition [27, 16, 40].


> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 以视觉为中心的学习。此类方法通过大规模三维落地监督对 MFM 进行后训练，从而改进空间推理。SpatialVLM [7]、Cambrian-S [42] 及相关工作 [26, 35, 12] 从真实世界图像、视频或三维标注构造空间 VQA 数据，以监督空间关系理解。SpatialReasoner [21] 和 Spatial-MLLM [39] 进一步引入中间三维表征或显式推理轨迹来组织空间推断。这些方法说明，空间落地监督能改善基准表现；但其增益仍可能与训练分布统计规律耦合，并在场景布局、视角或对象组成发生变化时下降。近期分析还表明，MFM 可能利用语义捷径，而非获得稳健的空间认知 [27, 16, 40]。


> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Geometry-centric learning. Geometry-centric methods compensate for the weak geometric grounding of 2D inputs by injecting explicit spatial signals. SpatialBot [4] uses RGB-D inputs and depth-centered QA data to improve metric spatial understanding. MM-Spatial [11] and SD-VLM [8] study how depth maps, multi-view observations, and depth-encoded visual features affect 3D reasoning, while N3D-VLM [38] integrates native 3D grounding into a unified MFM. Other works explore point-cloud-enhanced LLMs or reasoning-based segmentation for localization and scene understanding [23, 45]. Although explicit geometry provides useful spatial cues, directly conditioning MFMs on 3D modalities introduces cross-modal alignment challenges and often requires geometry-rich paired data, specialized architectures, and costly training.


> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 以几何为中心的学习。此类方法通过注入显式空间信号来弥补二维输入几何落地较弱的问题。SpatialBot [4] 使用 RGB-D 输入和以深度为中心的 QA 数据提升度量空间理解。MM-Spatial [11] 与 SD-VLM [8] 研究深度图、多视图观察和深度编码视觉特征如何影响三维推理；N3D-VLM [38] 则把原生三维落地集成到统一 MFM 中。其他工作探索点云增强 LLM，或使用基于推理的分割来完成定位与场景理解 [23, 45]。显式几何虽能提供有用的空间线索，但让 MFM 直接以三维模态为条件会带来跨模态对齐挑战，并且通常需要富含几何信息的配对数据、专用架构和高成本训练。


> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Tool-augmented learning. Tool-augmented methods equip MFMs with external modules for active evidence acquisition. Think3D [46] and pySpatial [20] invoke 3D reconstruction, camera pose estimation, or novel-view rendering for interactive spatial exploration. SpaceTools [9] studies how models coordinate depth, segmentation, and pose tools through reinforcement learning, while SpatialDreamer [5] uses tool hints or visual imagination as intermediate evidence. These approaches mark an important shift from passive perception to active tool use. However, most remain observation-centric: tools typically return rendered views, masks, depth maps, or low-level measurements, leaving the model to assemble high-level spatial structure through long and error-prone reasoning chains. In contrast, AlloSpatial converts noisy 3D reconstructions into compact allocentric representations and couples them with a Spatial Reasoning Harness for tool invocation, modality-decoupled evidence collection, and geometry-semantics arbitration. This enables models to reason over structured allocentric spatial memory rather than isolated egocentric observations or low-level geometric cues.


> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 工具增强学习。此类方法为 MFM 配备外部模块，以主动获取证据。Think3D [46] 和 pySpatial [20] 调用三维重建、相机姿态估计或新视角渲染来开展交互式空间探索。SpaceTools [9] 研究模型如何通过强化学习协调深度、分割与姿态工具；SpatialDreamer [5] 则把工具提示或视觉想象作为中间证据。这些方法标志着从被动感知到主动工具使用的重要转变。不过，大多数方法仍以观察为中心：工具通常返回渲染视图、掩码、深度图或低层测量，仍需模型通过冗长且易错的推理链组装高层空间结构。相比之下，AlloSpatial 把有噪声的三维重建转换为紧凑的非自我中心表征，并与用于工具调用、模态解耦证据收集和几何—语义仲裁的 Spatial Reasoning Harness 结合，使模型在结构化非自我中心空间记忆上推理，而非依赖孤立的自我中心观察或低层几何线索。


## 3 Methodology


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> 3.1 Problem Formulation


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 3.1 问题形式化


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Given an egocentric observation sequence I = {I_t}_{t=1}^T and a spatial question q, our goal is to produce a final answer â together with a verifiable spatial reasoning process. We formulate AlloSpatial as a harness-guided tool-using agent (π_θ, W, H), where π_θ denotes the foundation-model policy, W is the proposed World2Mind cognitive mapping sandbox, and H is the Spatial Reasoning Harness. Given (q, I), the agent generates a multi-turn trajectory:


> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 给定自我中心观察序列 $I=\{I_t\}_{t=1}^{T}$ 和空间问题 $q$，目标是输出最终答案 $\hat a$，并给出可验证的空间推理过程。作者把 AlloSpatial 形式化为由 harness 引导的工具使用智能体 $(\pi_\theta,W,H)$，其中 $\pi_\theta$ 表示基础模型策略，$W$ 是提出的 World2Mind 认知建图沙盒，$H$ 是 Spatial Reasoning Harness。给定 $(q,I)$，智能体生成多轮轨迹：


**Equation (1)**

$$
\tau=\left(h_0,u_0,o_0,h_1,u_1,o_1,\ldots,h_K,\hat a\right).
$$


> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Multi-turn trajectory generated by the agent.


> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 智能体生成的多轮轨迹。


> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Here h_k is the dialogue history at round k, and u_k ~ π_θ(· | h_k) is either a natural-language reasoning step or a structured tool call. If u_k is a valid tool call, World2Mind returns an allocentric spatial observation o_k = W(u_k; I); otherwise, o_k = ∅. The final answer â is emitted within a predefined answer tag for reliable parsing and evaluation.


> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 其中，$h_k$ 是第 $k$ 轮的对话历史，$u_k\sim\pi_\theta(\cdot\mid h_k)$ 可以是自然语言推理步骤，也可以是结构化工具调用。若 $u_k$ 是有效工具调用，World2Mind 返回非自我中心空间观察 $o_k=W(u_k;I)$；否则 $o_k=\varnothing$。最终答案 $\hat a$ 在预定义答案标签内输出，以便可靠解析和评估。


> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The harness H constrains the trajectory by specifying the required evidence channels, their ordering, and the cross-modal arbitration steps before final prediction. It therefore turns external allocentric priors into executable and inspectable reasoning evidence, rather than treating tool outputs as unverified context. For a training-free plug-in setting, H is instantiated via prompting. While in the training process, H defines the trajectory structure optimized during RL, as described in Sec. 3.4. Thus, H serves both as an inference-time protocol and as a training-time inductive bias.


> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> Harness $H$ 通过规定所需证据通道、通道顺序以及最终预测前的跨模态仲裁步骤来约束轨迹。因此，它把外部非自我中心先验转化为可执行、可检查的推理证据，而不是把工具输出当作未经核验的上下文。在免训练插件设置中，$H$ 通过提示实例化；在训练过程中，$H$ 则定义 RL 要优化的轨迹结构，详见第 3.4 节。因此，$H$ 既是推理时协议，也是训练时归纳偏置。


> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> 3.2 World2Mind: Allocentric Cognitive Mapping Sandbox


> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 3.2 World2Mind：非自我中心认知建图沙盒


> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Rather than reconstructing an exhaustive scene model, World2Mind exposes a query-conditioned cognitive mapping interface. Given an egocentric observation sequence I, an open-vocabulary category set C, a requested knowledge type k ∈ {landmark, route, both}, a footprint format f ∈ {rectangle, ellipse}, and a scene type s ∈ {indoor, outdoor}, World2Mind returns M = W(I; C, k, f, s), where M denotes the structured allocentric spatial knowledge.


> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> World2Mind 并不重建穷尽式场景模型，而是提供以查询为条件的认知建图接口。给定自我中心观察序列 $I$、开放词汇类别集合 $C$、请求的知识类型 $k\in\{\text{landmark},\text{route},\text{both}\}$、占地轮廓格式 $f\in\{\text{rectangle},\text{ellipse}\}$ 和场景类型 $s\in\{\text{indoor},\text{outdoor}\}$，World2Mind 返回 $M=W(I;C,k,f,s)$，其中 $M$ 表示结构化非自我中心空间知识。


> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> 3.2.1 Geometry-Semantic Alignment Pipeline


> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 3.2.1 几何—语义对齐流水线


> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> We first align geometry and semantics across the egocentric sequence. For each frame I_t ∈ R^{H×W}, we estimate a dense depth map D_t ∈ R^{H×W} and camera pose T_t ∈ SE(3) using monocular geometry models [18, 34], and extract open-vocabulary semantic masks {M_t^c}_{c∈C} with SAM 3 [6]. To suppress unreliable geometry near object boundaries, textureless regions, and poorly reconstructed views, we apply a two-level confidence filter to the predicted confidence map Γ_t ∈ [0,1]^{H×W}:


> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 首先在自我中心序列范围内对齐几何与语义。对每帧 $I_t\in\mathbb{R}^{H\times W}$，作者使用单目几何模型 [18, 34] 估计稠密深度图 $D_t\in\mathbb{R}^{H\times W}$ 和相机姿态 $T_t\in SE(3)$，并用 SAM 3 [6] 提取开放词汇语义掩码 $\{M_t^c\}_{c\in C}$。为抑制对象边界附近、无纹理区域和重建不佳视图中的不可靠几何，作者对预测置信图 $\Gamma_t\in[0,1]^{H\times W}$ 使用两级置信度过滤：


**Equation (2)**

$$
V_t(u,v)=\mathbf{1}[\Gamma_t(u,v)>\tau_{\mathrm{px}}]\cdot\mathbf{1}[\bar\Gamma_t>\tau_{\mathrm{frm}}],\qquad \bar\Gamma_t=\frac{1}{HW}\sum_{u,v}\Gamma_t(u,v).
$$


> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> Pixel- and frame-level confidence filtering.


> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 像素级与帧级置信度过滤。


> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> Here (u, v) indexes an image pixel, V_t(u, v) ∈ {0, 1} is the validity mask, and τ_px and τ_frm are the pixel- and frame-level confidence thresholds.


> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> 其中，$(u,v)$ 表示图像像素索引，$V_t(u,v)\in\{0,1\}$ 是有效性掩码，$\tau_{\mathrm{px}}$ 和 $\tau_{\mathrm{frm}}$ 分别是像素级与帧级置信度阈值。


> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> Pixels satisfying both constraints are back-projected into the world coordinate system, where p_t(u, v) denotes the 3D point obtained from D_t(u, v) and T_t. Aggregating valid points, semantic labels, and colors across frames yields a global semantic point cloud P = {(p_i, s_i, rgb_i)}_{i=1}^N, where p_i ∈ R^3, s_i ∈ C, and N is the number of retained points. To remove sparse outliers caused by boundary leakage and multi-view misalignment, we compute a K-nearest-neighbor density score ρ_i = (1/K ∑_{j∈N_K(i)} ||p_i-p_j||_2)^{-1} for each point, where N_K(i) denotes the K nearest neighbors of p_i, and discard points below a category-specific density percentile. The resulting point cloud is sparse but geometrically reliable, serving as the substrate for allocentric map construction.


> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 同时满足两项约束的像素会被反投影到世界坐标系中，其中 $p_t(u,v)$ 表示由 $D_t(u,v)$ 和 $T_t$ 得到的三维点。跨帧聚合有效点、语义标签与颜色，得到全局语义点云 $P=\{(p_i,s_i,rgb_i)\}_{i=1}^{N}$，其中 $p_i\in\mathbb{R}^3$、$s_i\in C$，$N$ 为保留点数。为了去除边界泄漏和多视图错位造成的稀疏离群点，作者为每个点计算 $K$ 近邻密度分数 $\rho_i=(\frac1K\sum_{j\in\mathcal N_K(i)}\|p_i-p_j\|_2)^{-1}$，其中 $\mathcal N_K(i)$ 表示 $p_i$ 的 $K$ 个最近邻，并丢弃低于类别特定密度百分位数的点。所得点云虽然稀疏，却在几何上可靠，可作为构建非自我中心地图的底层基础。


> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> 3.2.2 Allocentric Mapping


> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> 3.2.2 非自我中心建图


> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> World2Mind compresses the filtered P into complementary allocentric representations.


> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> World2Mind 把过滤后的 $P$ 压缩为互补的非自我中心表征。


> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> Landmark mapping with Allocentric-Spatial Tree. For each queried category c ∈ C, World2Mind applies adaptive DBSCAN to separate object instances. Each instance cluster is represented as a node in the Allocentric-Spatial Tree (AST) T = (V, E), where V denotes landmark nodes and E encodes hierarchical containment or support relations. Unlike abstract scene graphs that omit metric geometry [15, 29] or grid maps that discard object identity [41, 35], AST preserves both object semantics and explicit spatial structure. For each node v ∈ V, World2Mind projects its supporting points onto the ground plane and fits a compact footprint:


> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> 使用 Allocentric-Spatial Tree 的地标建图。对每个查询类别 $c\in C$，World2Mind 使用自适应 DBSCAN 分离对象实例。每个实例簇表示为 Allocentric-Spatial Tree（AST）$T=(V,E)$ 中的一个节点，其中 $V$ 表示地标节点，$E$ 编码层级包含或支撑关系。不同于省略度量几何的抽象场景图 [15, 29] 或丢弃对象身份的栅格地图 [41, 35]，AST 同时保留对象语义和显式空间结构。对每个节点 $v\in V$，World2Mind 把其支撑点投影到地平面，并拟合紧凑的占地轮廓：


**Equation (3)**

$$
\phi(v)=\left(c_x,c_z; a,b,\theta; h_{\min},h_{\max}; A,n\right).
$$


> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> Compact landmark footprint and attributes.


> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> 紧凑地标占地轮廓及其属性。


> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> Here (c_x, c_z) is the top-down centroid, (a, b) are the semi-axes of the fitted ellipse, θ is its orientation, (h_min, h_max) denotes the vertical extent, A is the footprint area, and n is the number of supporting points, used as a confidence proxy. Elliptical footprints are used by default for stable coarse occupancy, while an axis-aligned rectangular format is returned when nearest-boundary computation is required. The resulting AST is serialized into YAML and included in the structured spatial map M. This representation turns noisy 3D reconstruction into compact, model-readable spatial memory: foundation models can directly parse object centers, sizes, orientations, and containment relations without specialized 3D adapters, while the coarse footprint parameterization remains robust to local reconstruction noise and reflects the compressed nature of cognitive maps [3, 2].


> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> 其中，$(c_x,c_z)$ 是俯视质心，$(a,b)$ 是拟合椭圆的半轴，$\theta$ 是其方向，$(h_{\min},h_{\max})$ 表示垂直范围，$A$ 是占地面积，$n$ 是支撑点数量并作为置信度代理。默认使用椭圆占地轮廓来获得稳定的粗粒度占用；需要计算最近边界时，则返回轴对齐矩形格式。所得 AST 被序列化为 YAML，并纳入结构化空间地图 $M$。该表征把有噪声的三维重建转化为紧凑、模型可读的空间记忆：基础模型无需专用三维适配器，就能直接解析对象中心、尺寸、方向和包含关系；粗粒度占地参数化对局部重建噪声保持稳健，也体现了认知地图的压缩性质 [3, 2]。


> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> Route mapping. For traversability and path-related queries, World2Mind voxelizes points associated with traversable categories, such as floors, and projects them onto a top-down grid. Each grid cell is labeled as traversable, occupied, or unknown. The camera trajectory {T_t}_{t=1}^T, where T_t denotes the camera pose of frame I_t, is projected into the same coordinate system to encode observed motion history and support route-level reasoning.


> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> 路线建图。对于可遍历性和路径相关查询，World2Mind 将与地板等可遍历类别关联的点体素化，并投影到俯视栅格。每个栅格单元被标为可遍历、已占用或未知。相机轨迹 $\{T_t\}_{t=1}^{T}$（$T_t$ 表示帧 $I_t$ 的相机姿态）也被投影到同一坐标系，以编码已观察到的运动历史并支持路线级推理。


> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> Optional visual rendering. Beyond structured text, World2Mind can return allocentric visualizations as auxiliary global observations, including top-down AST layouts, route maps, and semantic segmentation maps. These renderings provide a compact visual summary of the global scene layout and serve as additional evidence during geometry-semantics arbitration.


> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> 可选视觉渲染。除了结构化文本，World2Mind 还可返回非自我中心可视化作为辅助全局观察，包括俯视 AST 布局、路线图和语义分割图。这些渲染结果提供全局场景布局的紧凑视觉摘要，并在几何—语义仲裁期间充当额外证据。


> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> 3.3 Spatial Reasoning Harness


> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> 3.3 空间推理 Harness


> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> Structured allocentric priors are useful but not self-verifying. Directly conditioning on World2Mind output M can induce two failure modes: 1) modality lock-in, where the model prematurely commits to either visual appearance or AST text and ignores conflicting evidence [37, 22]; and 2) over-trust in tool results, where incomplete or noisy reconstructions are treated as ground truth. To mitigate these failures, we design the Spatial Reasoning Harness H as a cyclic protocol:


> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> 结构化非自我中心先验有用，却不能自我验证。直接以 World2Mind 输出 $M$ 为条件会诱发两种失败模式：1）模态锁定，即模型过早认定视觉外观或 AST 文本之一，并忽略冲突证据 [37, 22]；2）过度信任工具结果，即把不完整或有噪声的重建视为真值。为缓解这些失败，作者把 Spatial Reasoning Harness $H$ 设计为循环协议：


**Equation (4)**

$$
H:\quad \mathrm{JUDGE}\rightarrow\mathrm{COLLECT}\rightarrow\mathrm{ARBITRATE}\rightarrow\{\mathrm{REFINE},\mathrm{ANSWER}\}.
$$


> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> Cyclic Spatial Reasoning Harness.


> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> 循环式空间推理 Harness。


> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> At each cycle, the agent decides whether additional allocentric evidence is needed, collects evidence through decoupled channels, and arbitrates geometry-semantics conflicts before either refining the query or committing to the final answer.


> <span style="color:#F59E0B"><strong>Para. 23[CN]:</strong></span> 在每个循环中，智能体先判断是否需要额外的非自我中心证据，再通过解耦通道收集证据，并在细化查询或提交最终答案之前仲裁几何—语义冲突。


> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> Stage I: tool invocation judgment. At reasoning cycle r, the agent determines whether the current history h_r is sufficient or whether World2Mind should be queried. Following the reason-then-act principle of ReAct-style agents [43], it first states a spatial hypothesis and the rationale for tool use:


> <span style="color:#F59E0B"><strong>Para. 24[CN]:</strong></span> 阶段 I：工具调用判断。在推理循环 $r$ 中，智能体判断当前历史 $h_r$ 是否充分，或者是否应查询 World2Mind。遵循 ReAct 风格智能体 [43] 的“先推理、后行动”原则，它先陈述空间假设和使用工具的理由：


**Equation (5)**

$$
(d_r,\eta_r)=\mathrm{JUDGE}(q,h_r),\qquad d_r\in\{\mathrm{CALL},\mathrm{SKIP}\}.
$$


> <span style="color:#3B82F6"><strong>Para. 25:</strong></span> Tool-use decision and current spatial hypothesis.


> <span style="color:#F59E0B"><strong>Para. 25[CN]:</strong></span> 工具使用决策与当前空间假设。


> <span style="color:#3B82F6"><strong>Para. 26:</strong></span> Here d_r is the tool-use decision and η_r is the current spatial hypothesis. The agent calls World2Mind only when the question requires metric measurement, route topology, viewpoint transformation, or other allocentric spatial evidence, preserving an initial hypothesis that can later be verified or rejected.


> <span style="color:#F59E0B"><strong>Para. 26[CN]:</strong></span> 其中，$d_r$ 是工具使用决策，$\eta_r$ 是当前空间假设。只有当问题需要度量测量、路线拓扑、视角变换或其他非自我中心空间证据时，智能体才调用 World2Mind；同时保留初始假设，以便之后验证或否定。


### Table 1

**Caption:** Table 1: Results of AlloSpatial under the training-free setting on VSI-Bench and MindCube (tiny split). For VSI-Bench, 32 input frames are uniformly used.

**Caption[CN]:** 表 1：免训练设置下 AlloSpatial 在 VSI-Bench 与 MindCube（tiny split）上的结果。VSI-Bench 统一使用 32 个输入帧。

| Model | VSI Overall | Avg Obj Count | Abs Dist | Avg Obj Size | Room Size | Avg Rel Dist | Rel Dir | Route Plan | Appr Order | MindCube Overall | Around | Among | Rotation |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| GPT-5.2 w/o AlloSpatial | 46.7 | 52.5 | 34.9 | 67.5 | 50.6 | 42.0 | 40.7 | 34.7 | 51.0 | 49.9 | 62.4 | 45.2 | 48.5 |
| Claude-4.6-Opus w/o AlloSpatial | 38.4 | 46.9 | 18.5 | 62.1 | 26.8 | 40.0 | 47.2 | 34.7 | 30.6 | 48.5 | 58.8 | 50.7 | 29.0 |
| Gemini-3-Pro w/o AlloSpatial | 55.2 | 47.8 | 32.1 | 71.3 | 55.0 | 54.0 | 44.8 | 57.1 | 79.6 | 75.1 | 77.2 | 68.2 | 93.0 |
| GPT-5.2 w/ AlloSpatial | 54.0 (↑7.3) | 47.4 (↓5.1) | 33.4 (↓1.5) | 63.3 (↓4.2) | 52.4 (↑1.8) | 64.0 (↑22.0) | 41.1 (↑0.4) | 51.0 (↑16.3) | 79.6 (↑28.6) | 54.6 (↑4.7) | 60.4 (↓2.0) | 47.7 (↑2.5) | 68.0 (↑19.5) |
| Claude-4.6-Opus w/ AlloSpatial | 56.0 (↑17.7) | 59.0 (↑12.0) | 34.3 (↑15.8) | 67.3 (↑5.2) | 54.8 (↑28.0) | 64.0 (↑24.0) | 62.7 (↑15.6) | 65.3 (↑30.6) | 40.8 (↑10.2) | 62.9 (↑14.4) | 82.4 (↑23.6) | 60.8 (↑10.1) | 45.0 (↑16.0) |
| Gemini-3-Pro w/ AlloSpatial | 61.0 (↑5.8) | 51.8 (↑4.1) | 36.8 (↑4.7) | 57.7 (↓13.5) | 62.6 (↑7.6) | 62.0 (↑8.0) | 67.7 (↑22.9) | 65.3 (↑8.2) | 83.7 (↑4.1) | 81.6 (↑6.5) | 86.0 (↑8.8) | 75.8 (↑7.6) | 93.5 (↑0.5) |

**中文表格：**

| 模型 | VSI 总体 | 平均对象计数 | 绝对距离 | 平均对象尺寸 | 房间尺寸 | 平均相对距离 | 相对方向 | 路线规划 | 出现顺序 | MindCube 总体 | 环绕 | 位于……之间 | 旋转 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| GPT-5.2 不使用 AlloSpatial | 46.7 | 52.5 | 34.9 | 67.5 | 50.6 | 42.0 | 40.7 | 34.7 | 51.0 | 49.9 | 62.4 | 45.2 | 48.5 |
| Claude-4.6-Opus 不使用 AlloSpatial | 38.4 | 46.9 | 18.5 | 62.1 | 26.8 | 40.0 | 47.2 | 34.7 | 30.6 | 48.5 | 58.8 | 50.7 | 29.0 |
| Gemini-3-Pro 不使用 AlloSpatial | 55.2 | 47.8 | 32.1 | 71.3 | 55.0 | 54.0 | 44.8 | 57.1 | 79.6 | 75.1 | 77.2 | 68.2 | 93.0 |
| GPT-5.2 使用 AlloSpatial | 54.0 (↑7.3) | 47.4 (↓5.1) | 33.4 (↓1.5) | 63.3 (↓4.2) | 52.4 (↑1.8) | 64.0 (↑22.0) | 41.1 (↑0.4) | 51.0 (↑16.3) | 79.6 (↑28.6) | 54.6 (↑4.7) | 60.4 (↓2.0) | 47.7 (↑2.5) | 68.0 (↑19.5) |
| Claude-4.6-Opus 使用 AlloSpatial | 56.0 (↑17.7) | 59.0 (↑12.0) | 34.3 (↑15.8) | 67.3 (↑5.2) | 54.8 (↑28.0) | 64.0 (↑24.0) | 62.7 (↑15.6) | 65.3 (↑30.6) | 40.8 (↑10.2) | 62.9 (↑14.4) | 82.4 (↑23.6) | 60.8 (↑10.1) | 45.0 (↑16.0) |
| Gemini-3-Pro 使用 AlloSpatial | 61.0 (↑5.8) | 51.8 (↑4.1) | 36.8 (↑4.7) | 57.7 (↓13.5) | 62.6 (↑7.6) | 62.0 (↑8.0) | 67.7 (↑22.9) | 65.3 (↑8.2) | 83.7 (↑4.1) | 81.6 (↑6.5) | 86.0 (↑8.8) | 75.8 (↑7.6) | 93.5 (↑0.5) |


> <span style="color:#3B82F6"><strong>Para. 27:</strong></span> Stage II: modality-decoupled cue collection. When d_r = CALL, the agent generates query parameters ξ_r = (C_r, k_r, f_r, s_r) and obtains a structured spatial map M_r = W(I; ξ_r), where C_r is the queried category set, k_r the requested knowledge type, f_r the footprint format, and s_r the scene type. Evidence is then collected separately from raw visual observations, AST-structured text, and optional top-down maps {e_r^vis, e_r^ast, e_r^map}. Here, E_r denotes the evidence set at cycle r, and e_r^vis, e_r^ast, and e_r^map denote visual, textual-allocentric, and rendered-map evidence, respectively. This decoupled collection prevents premature fusion and reduces reliance on a single evidence channel.


> <span style="color:#F59E0B"><strong>Para. 27[CN]:</strong></span> 阶段 II：模态解耦的线索收集。当 $d_r=\mathrm{CALL}$ 时，智能体生成查询参数 $\xi_r=(C_r,k_r,f_r,s_r)$，并获得结构化空间地图 $M_r=W(I;\xi_r)$，其中 $C_r$ 是查询类别集合，$k_r$ 是请求的知识类型，$f_r$ 是占地轮廓格式，$s_r$ 是场景类型。随后分别从原始视觉观察、AST 结构化文本和可选俯视地图 $\{e_r^{vis},e_r^{ast},e_r^{map}\}$ 收集证据。$E_r$ 表示循环 $r$ 的证据集合，$e_r^{vis}$、$e_r^{ast}$ 和 $e_r^{map}$ 分别表示视觉证据、文本式非自我中心证据和渲染地图证据。这种解耦收集可避免过早融合，并减少对单一证据通道的依赖。


> <span style="color:#3B82F6"><strong>Para. 28:</strong></span> Stage III: geometry-semantics interleaved arbitration. The agent then compares visual semantics with geometric evidence from AST and optional maps, identifies conflicts caused by reconstruction drift, missing instances, or false detections, etc., and then decides whether the evidence is sufficient:


> <span style="color:#F59E0B"><strong>Para. 28[CN]:</strong></span> 阶段 III：几何—语义交错仲裁。智能体把视觉语义与 AST 及可选地图中的几何证据进行比较，识别由重建漂移、实例缺失或误检等造成的冲突，然后判断证据是否充分：


**Equation (6)**

$$
(\Delta_r,\omega_r,y_r)=\mathrm{ARBITRATE}(E_r),\qquad y_r\in\{\mathrm{REFINE},\mathrm{ANSWER}\}.
$$


> <span style="color:#3B82F6"><strong>Para. 29:</strong></span> Cross-modal conflict, evidence confidence, and next action.


> <span style="color:#F59E0B"><strong>Para. 29[CN]:</strong></span> 跨模态冲突、证据置信分配与下一步动作。


> <span style="color:#3B82F6"><strong>Para. 30:</strong></span> Here Δ_r denotes detected cross-modal conflicts, ω_r represents confidence assignments over evidence channels, and y_r is the next action. If y_r = REFINE, the agent updates ξ_r and starts another cycle; if y_r = ANSWER, it emits the final response within the <Answer> tag. In this way, H treats external cognitive maps as falsifiable evidence for reasoning rather than as direct pseudo-labels, enabling iterative, verifiable, and trainable allocentric spatial reasoning.


> <span style="color:#F59E0B"><strong>Para. 30[CN]:</strong></span> 其中，$\Delta_r$ 表示检测到的跨模态冲突，$\omega_r$ 表示对各证据通道的置信度分配，$y_r$ 是下一步动作。若 $y_r=\mathrm{REFINE}$，智能体更新 $\xi_r$ 并开始下一轮循环；若 $y_r=\mathrm{ANSWER}$，则在 `<Answer>` 标签内输出最终响应。由此，$H$ 把外部认知地图视为可证伪的推理证据，而不是直接伪标签，从而实现迭代式、可验证且可训练的非自我中心空间推理。


> <span style="color:#3B82F6"><strong>Para. 31:</strong></span> 3.4 Internalizing the Spatial Reasoning Harness via Reinforcement Learning


> <span style="color:#F59E0B"><strong>Para. 31[CN]:</strong></span> 3.4 通过强化学习内化 Spatial Reasoning Harness


> <span style="color:#3B82F6"><strong>Para. 32:</strong></span> While frontier proprietary models can often follow the Spatial Reasoning Harness H through prompting, open-weight models [1, 36] do not naturally exhibit stable multi-turn tool-use behavior. In preliminary experiments, they frequently produce malformed tool calls, skip cross-modal arbitration, or degenerate into repetitive interaction. We therefore internalize H into the open-weight policy π_θ with supervised cold start followed by RL with live World2Mind execution.


> <span style="color:#F59E0B"><strong>Para. 32[CN]:</strong></span> 前沿专有模型往往能通过提示遵循 Spatial Reasoning Harness $H$，但开放权重模型 [1, 36] 并不会自然表现出稳定的多轮工具使用行为。在初步实验中，它们经常生成格式错误的工具调用、跳过跨模态仲裁，或退化为重复交互。因此，作者先进行监督式冷启动，再采用实时执行 World2Mind 的 RL，把 $H$ 内化到开放权重策略 $\pi_\theta$ 中。


> <span style="color:#3B82F6"><strong>Para. 33:</strong></span> Supervised cold start. We first use World2Mind and the harness protocol to distill trajectories from proprietary models. We retain trajectories that are answer-correct, structurally valid, and contain non-trivial cross-modal arbitration. Supervised fine-tuning on these traces bootstraps tool-call syntax, AST and route-map parsing, harness stage ordering, and answer-tag formatting, thereby preparing the policy for subsequent optimization with Group Sequence Policy Optimization (GSPO) [48].


> <span style="color:#F59E0B"><strong>Para. 33[CN]:</strong></span> 监督式冷启动。首先使用 World2Mind 和 harness 协议从专有模型蒸馏轨迹。只保留答案正确、结构有效且含有非平凡跨模态仲裁的轨迹。对这些轨迹进行监督微调，以启动工具调用语法、AST 与路线图解析、harness 阶段排序和答案标签格式，使策略为后续的 Group Sequence Policy Optimization（GSPO）[48] 优化做好准备。


> <span style="color:#3B82F6"><strong>Para. 34:</strong></span> GSPO with Harness-Gated Trajectory Reward. To stabilize reinforcement learning over long tool-use trajectories, we introduce a Harness-Gated Trajectory Reward (HGTR) that scores each complete trajectory τ rather than individual tokens. HGTR combines answer correctness, structural compliance, tool-use effectiveness, and response efficiency:


> <span style="color:#F59E0B"><strong>Para. 34[CN]:</strong></span> 采用 Harness-Gated Trajectory Reward 的 GSPO。为稳定长工具使用轨迹上的强化学习，作者提出 Harness-Gated Trajectory Reward（HGTR），它对每条完整轨迹 $\tau$ 而非单个 token 评分。HGTR 结合答案正确性、结构合规性、工具使用有效性和响应效率：


**Equation (7)**

$$
R(\tau)=w_{\mathrm{acc}}\widetilde R_{\mathrm{acc}}(\tau)+w_{\mathrm{str}}R_{\mathrm{str}}(\tau)+w_{\mathrm{tool}}R_{\mathrm{tool}}(\tau)+w_{\mathrm{len}}R_{\mathrm{len}}(\tau).
$$


> <span style="color:#3B82F6"><strong>Para. 35:</strong></span> Harness-Gated Trajectory Reward.


> <span style="color:#F59E0B"><strong>Para. 35[CN]:</strong></span> Harness 门控的轨迹奖励。


> <span style="color:#3B82F6"><strong>Para. 36:</strong></span> Here w_acc, w_str, w_tool, and w_len are reward weights. R_str(τ) measures harness compliance, including valid tool-call tags, complete stage ordering, explicit arbitration, and the final answer tag. R_acc(τ) measures answer quality, using exact match for multiple-choice questions and mean relative accuracy for numerical questions following [41]. To prevent malformed trajectories from receiving reward through accidental correct guesses, HGTR applies a structure-gated accuracy:


> <span style="color:#F59E0B"><strong>Para. 36[CN]:</strong></span> 其中，$w_{acc}$、$w_{str}$、$w_{tool}$ 与 $w_{len}$ 是奖励权重。$R_{str}(\tau)$ 衡量 harness 合规性，包括有效工具调用标签、完整阶段顺序、显式仲裁和最终答案标签。$R_{acc}(\tau)$ 衡量答案质量：多项选择题使用精确匹配，数值题按照 [41] 使用平均相对准确率。为防止格式错误的轨迹凭偶然猜对获得奖励，HGTR 使用结构门控准确性：


**Equation (8)**

$$
\widetilde R_{\mathrm{acc}}(\tau)=R_{\mathrm{acc}}(\tau)\cdot\mathbf{1}[R_{\mathrm{str}}(\tau)\ge\tau_s].
$$


> <span style="color:#3B82F6"><strong>Para. 37:</strong></span> Structure-gated answer accuracy.


> <span style="color:#F59E0B"><strong>Para. 37[CN]:</strong></span> 由结构合规性门控的答案准确性。


> <span style="color:#3B82F6"><strong>Para. 38:</strong></span> Here τ_s is the threshold and 1[·] is the indicator function. Thus, correctness is credited only when the trajectory satisfies the harness format. HGTR further uses a correctness-tied tool-use reward:


> <span style="color:#F59E0B"><strong>Para. 38[CN]:</strong></span> 其中，$\tau_s$ 是阈值，$\mathbf{1}[\cdot]$ 是指示函数。因此，只有轨迹满足 harness 格式时才记入正确性。HGTR 进一步采用与正确性绑定的工具使用奖励：


**Equation (9)**

$$
R_{\mathrm{tool}}(\tau)=\alpha\widetilde R_{\mathrm{acc}}(\tau)\mathbf{1}[\mathrm{ValidCall}(\tau)]-\gamma\max(0,n_W(\tau)-n^\star).
$$


> <span style="color:#3B82F6"><strong>Para. 39:</strong></span> Correctness-tied valid-tool reward with overuse penalty.


> <span style="color:#F59E0B"><strong>Para. 39[CN]:</strong></span> 与正确性绑定的有效工具奖励及过度调用惩罚。


> <span style="color:#3B82F6"><strong>Para. 40:</strong></span> Here ValidCall(τ) indicates whether World2Mind is invoked with valid syntax and task-relevant arguments, n_W(τ) is the number of calls, n* is a soft call budget, and α, γ control the tool reward and overuse penalty. This reward grants tool-use credit only when a valid invocation contributes to a structurally valid and correct answer, while discouraging redundant reconstruction once sufficient allocentric evidence is available. Finally, R_len(τ) penalizes excessive model-generated tokens while masking out tool-returned ASTs, route maps, and visualization metadata. Overall, HGTR guides the agent toward trajectories that are answer-correct, harness-compliant, tool-efficient, and verifiable.


> <span style="color:#F59E0B"><strong>Para. 40[CN]:</strong></span> 其中，$\mathrm{ValidCall}(\tau)$ 表示 World2Mind 是否以有效语法和与任务相关的参数被调用，$n_W(\tau)$ 是调用次数，$n^\star$ 是软调用预算，$\alpha$、$\gamma$ 控制工具奖励和过度使用惩罚。只有当有效调用促成结构有效且答案正确的轨迹时，该奖励才给予工具使用得分；获得充分非自我中心证据后，它会抑制冗余重建。最后，$R_{len}(\tau)$ 对过多的模型生成 token 施加惩罚，同时屏蔽工具返回的 AST、路线图和可视化元数据。总体而言，HGTR 引导智能体生成答案正确、符合 harness、工具高效且可验证的轨迹。


## 4 Experiments


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> 4.1 Experimental Setup


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 4.1 实验设置


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Datasets. We evaluate AlloSpatial on the official Tiny split of VSI-Bench [41] and MindCube [35], containing 392 and 1,050 questions, respectively. For training, we sample data from VSI-590K and the MindCube training set. The cold-start stage distills multi-turn tool-use trajectories from GPT-5.2 and Claude-4.6-Opus with World2Mind and the Spatial Reasoning Harness, followed by filtering for answer correctness, harness compliance, and valid tool invocation.


> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 数据集。作者在 VSI-Bench [41] 和 MindCube [35] 的官方 Tiny 划分上评估 AlloSpatial，两者分别包含 392 和 1,050 个问题。训练数据从 VSI-590K 和 MindCube 训练集采样。冷启动阶段使用 World2Mind 与 Spatial Reasoning Harness，从 GPT-5.2 和 Claude-4.6-Opus 蒸馏多轮工具使用轨迹，随后根据答案正确性、harness 合规性和工具调用有效性进行筛选。


> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Metrics. Following [41, 35], we report pass@1 accuracy for multiple-choice questions and mean relative accuracy (MRA) for numerical questions. The overall score is the unweighted average over all task types within each benchmark. For the training-free setting on VSI-Bench, we uniformly sample up to 32 frames from each video. For the post-trained AlloSpatial agents and other baselines, we follow the limited-observation setting of Think3D [46] and uniformly sample 7 frames, testing performance under sparse visual inputs. We further analyze the effect of frame number in Sec. 4.4.


> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 指标。遵循 [41, 35]，多项选择题报告 pass@1 准确率，数值题报告平均相对准确率（MRA）。总体分数是每个基准内所有任务类型的无权平均。VSI-Bench 免训练设置从每段视频均匀采样至多 32 帧；后训练 AlloSpatial 智能体和其他基线则遵循 Think3D [46] 的有限观察设置，均匀采样 7 帧，以测试稀疏视觉输入下的表现。第 4.4 节进一步分析帧数影响。


> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Baselines. We compare 1) proprietary models including GPT-5.2, Claude-4.6-Opus, and Gemini-3-Pro; 2) open-source models including Qwen3-VL [1], InternVL3.5 [36], and Gemma-4 [14]; and 3) specialized spatial models including Spatial-MLLM [39], Cambrian-S [42], and Think3D [46].


> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 基线。比较对象包括：1）GPT-5.2、Claude-4.6-Opus 和 Gemini-3-Pro 等专有模型；2）Qwen3-VL [1]、InternVL3.5 [36] 和 Gemma-4 [14] 等开源模型；3）Spatial-MLLM [39]、Cambrian-S [42] 和 Think3D [46] 等空间专用模型。


> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Training details. We instantiate AlloSpatial from Qwen3-VL-4B-Instruct and Qwen3-VL-8B-Instruct [1]. The 4B and 8B agents are trained for 600 and 400 RL steps, respectively, using 4.8K and 2.4K unique prompts, with 8 sampled rollouts per prompt. Detailed hyperparameters, World2Mind service configuration, and computational costs are provided in Appendices A, B, and E.


> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 训练细节。作者分别从 Qwen3-VL-4B-Instruct 与 Qwen3-VL-8B-Instruct [1] 实例化 AlloSpatial。4B 和 8B 智能体分别训练 600 与 400 个 RL 步骤，使用 4.8K 与 2.4K 个唯一提示，每个提示采样 8 条 rollout。详细超参数、World2Mind 服务配置和计算成本见附录 A、B、E。


> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> 4.2 AlloSpatial Improves Proprietary Foundation Models for Spatial Reasoning


> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 4.2 AlloSpatial 提升专有基础模型的空间推理能力


> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> We first evaluate AlloSpatial as a training-free plug-in for proprietary models by exposing World2Mind W and the Spatial Reasoning Harness H through prompting.


> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 首先通过提示向专有模型开放 World2Mind $W$ 和 Spatial Reasoning Harness $H$，把 AlloSpatial 作为免训练插件进行评估。


> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Consistent improvement across benchmarks. As shown in Tab. 1, AlloSpatial improves GPT-5.2, Claude-4.6-Opus, and Gemini-3-Pro on VSI-Bench by +7.3, +17.7, and +5.8 overall points, respectively, and on MindCube by +4.7, +14.4, and +6.5 points. The gains are concentrated on tasks that require allocentric structure, such as relative direction, route planning, and viewpoint-dependent rotation, while tasks solvable from local visual evidence show smaller or occasionally negative changes. This pattern suggests that World2Mind is most beneficial when direct egocentric perception is insufficient, and the model must reason over stable spatial relations beyond the observed view. A complete reasoning trace is shown in Fig. 4, and additional analysis for AlloSpatial’s reasoning cases is illustrated in Appendix D.


> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 跨基准的稳定提升。如表 1 所示，AlloSpatial 使 GPT-5.2、Claude-4.6-Opus 和 Gemini-3-Pro 在 VSI-Bench 上的总体分数分别提升 +7.3、+17.7 和 +5.8 点，在 MindCube 上分别提升 +4.7、+14.4 和 +6.5 点。增益主要集中于需要非自我中心结构的任务，如相对方向、路线规划和视角相关旋转；可由局部视觉证据解决的任务则增益较小，偶尔甚至下降。这一模式说明，当直接的自我中心感知不足、模型必须在观察视野之外的稳定空间关系上推理时，World2Mind 最有帮助。图 4 给出完整推理轨迹，附录 D 进一步分析 AlloSpatial 的推理案例。

### Figure 4

![AlloSpatial chair-size reasoning trace with tool calls and cross-validation](figure_4_reasoning_trace.png)

**Caption:** Figure 4: Reasoning trace produced by AlloSpatial.

**Caption[CN]:** 图 4：AlloSpatial 生成的推理轨迹。


> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> ASTs provide effective allocentric reasoning evidence. We further test whether the gain comes from structured spatial knowledge itself by evaluating VSI-Bench in a text-only “blind” setting [41]. Fig. 3 shows that AST text substantially improves blind spatial reasoning over text-only baselines, especially on object size and route planning. This supports the role of AST as a compact allocentric prior that enables models to reason over spatial structure without directly observing the scene. Together with the full-input results, the blind setting suggests that the critical signal is not merely additional visual context, but the structured spatial organization supplied by World2Mind.


> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> AST 提供有效的非自我中心推理证据。作者进一步在纯文本“盲测”设置 [41] 中评估 VSI-Bench，以检验增益是否来自结构化空间知识本身。图 3 表明，AST 文本相对纯文本基线显著改善盲测空间推理，尤其是在对象尺寸和路线规划任务上。这支持把 AST 视为紧凑非自我中心先验：模型无需直接观察场景，也能在空间结构上推理。结合完整输入结果，盲测设置表明关键不只是额外视觉上下文，而是 World2Mind 提供的结构化空间组织。


### Figure 3

![Bar chart of blind text-only reasoning with AST priors](figure_3_blind_ast.png)

**Caption:** Figure 3: Text-only spatial reasoning with allocentric priors. VSI-Bench performance under the “blind” setting, where visual inputs are removed.

**Caption[CN]:** 图 3：使用非自我中心先验进行纯文本空间推理。在移除视觉输入的“盲测”设置下的 VSI-Bench 表现。


> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> 4.3 Trained AlloSpatial Agents Outperform General and Spatially Specialized Models


> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 4.3 训练后的 AlloSpatial 智能体超过通用模型与空间专用模型


> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> We next compare the trained AlloSpatial agents with proprietary models, open-source MFMs, and specialized spatial reasoning models. As shown in Tab. 2, AlloSpatial-8B achieves the best overall score on VSI-Bench, while AlloSpatial-4B ranks second. Both variants outperform proprietary models such as GPT-5.2, Gemini-2.5-Pro, and Gemini-3-Pro. Notably, AlloSpatial-4B and AlloSpatial-8B also surpass Qwen3-VL-32B, despite using substantially smaller backbones. AlloSpatial also compares favorably with spatially specialized models. On VSI-Bench, AlloSpatial-8B improves over Spatial-MLLM-4B and Cambrian-S-3B by +5.1 and +4.7 overall points, respectively, while AlloSpatial-4B also exceeds both baselines. This is notable because Spatial-MLLM and Cambrian-S rely on large-scale spatial grounding data, whereas AlloSpatial uses a much smaller set of unique training prompts and acquires spatial competence through structured tool interaction and trajectory-level optimization. These results suggest that allocentric spatial memory and verifiable reasoning can improve data efficiency compared with purely supervision-driven spatial learning.


> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> 接下来，把训练后的 AlloSpatial 智能体与专有模型、开源 MFM 和空间推理专用模型比较。如表 2 所示，AlloSpatial-8B 在 VSI-Bench 上取得最佳总体分数，AlloSpatial-4B 排名第二；两者都超过 GPT-5.2、Gemini-2.5-Pro 和 Gemini-3-Pro 等专有模型。值得注意的是，尽管骨干小得多，AlloSpatial-4B 和 AlloSpatial-8B 也超过 Qwen3-VL-32B。AlloSpatial 与空间专用模型相比同样占优：在 VSI-Bench 上，AlloSpatial-8B 相对 Spatial-MLLM-4B 和 Cambrian-S-3B 的总体分数分别提升 +5.1 和 +4.7 点，AlloSpatial-4B 也超过这两个基线。这一点尤其值得注意，因为 Spatial-MLLM 和 Cambrian-S 依赖大规模空间落地数据，而 AlloSpatial 使用的唯一训练提示数量小得多，通过结构化工具交互和轨迹级优化获得空间能力。结果说明，相比纯监督驱动的空间学习，非自我中心空间记忆和可验证推理能够提升数据效率。

### Table 2

**Caption:** Table 2: VSI-Bench tiny-split results with 7 input frames. † denotes results taken from the original paper.

**Caption[CN]:** 表 2：使用 7 个输入帧时在 VSI-Bench tiny 划分上的结果。† 表示直接取自原论文的结果。

| Rank | Model | Overall | Avg. Numerical | Obj Count | Abs Dist | Obj Size | Room Size | Avg. MC | Rel Dist | Rel Dir | Route Plan | Appr Order |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 11 | GPT-5.2 | 37.7 | 36.4 | 28.6 | 24.3 | 52.3 | 40.6 | 39.0 | 42.0 | 28.4 | 42.9 | 42.9 |
| 8 | Gemini-2.5-Pro | 46.2 | 39.4 | 34.7 | 14.3 | 56.3 | 52.4 | 53.0 | 52.0 | 45.7 | 38.8 | 75.5 |
| 9 | Gemini-3-Pro | 45.2 | 32.2 | 29.4 | 12.6 | 38.3 | 48.4 | 58.3 | 56.0 | 52.7 | 49.0 | 75.5 |
| 12 | Gemma-4-E4B | 33.5 | 30.1 | 19.6 | 24.5 | 33.1 | 43.2 | 36.9 | 38.0 | 40.0 | 30.6 | 38.8 |
| 6 | InternVL3.5-4B | 48.8 | 50.9 | 77.3 | 19.4 | 60.4 | 46.4 | 46.8 | 38.0 | 47.1 | 40.8 | 61.2 |
| 10 | Qwen3-VL-4B | 45.1 | 47.7 | 44.3 | 34.5 | 64.4 | 47.8 | 42.4 | 36.0 | 37.8 | 24.5 | 71.4 |
| 7 | Qwen3-VL-8B | 48.5 | 51.5 | 50.4 | 40.2 | 67.5 | 48.0 | 45.5 | 36.0 | 44.1 | 30.6 | 71.4 |
| 3 | Qwen3-VL-32B | 53.1 | 55.3 | 60.6 | 35.1 | 71.5 | 54.0 | 50.9 | 46.0 | 51.4 | 36.7 | 69.4 |
| 5 | Spatial-MLLM-4B [39] | 49.1 | 53.0 | 76.5 | 27.0 | 57.9 | 50.6 | 45.2 | 44.0 | 40.9 | 38.8 | 57.1 |
| 4 | Cambrian-S-3B [42] | 49.5 | 51.7 | 67.1 | 22.6 | 73.8 | 43.2 | 47.3 | 54.0 | 37.1 | 26.5 | 71.4 |
| – | Think3D-4B† [46] | – | – | – | – | – | – | 45.4 | 44.7 | 39.0 | 36.7 | 61.2 |
| 2 | **AlloSpatial-4B (Ours)** | **53.5** | **56.3** | **54.1** | **42.3** | **68.8** | **60.0** | **50.8** | **50.0** | **59.3** | **34.7** | **59.2** |
| 1 | **AlloSpatial-8B (Ours)** | **54.2** | **47.8** | **46.1** | **26.0** | **65.6** | **53.4** | **60.6** | **52.0** | **64.1** | **46.9** | **79.6** |

**中文表格：**

| 排名 | 模型 | 总体 | 数值题平均 | 对象计数 | 绝对距离 | 对象尺寸 | 房间尺寸 | 选择题平均 | 相对距离 | 相对方向 | 路线规划 | 出现顺序 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 11 | GPT-5.2 | 37.7 | 36.4 | 28.6 | 24.3 | 52.3 | 40.6 | 39.0 | 42.0 | 28.4 | 42.9 | 42.9 |
| 8 | Gemini-2.5-Pro | 46.2 | 39.4 | 34.7 | 14.3 | 56.3 | 52.4 | 53.0 | 52.0 | 45.7 | 38.8 | 75.5 |
| 9 | Gemini-3-Pro | 45.2 | 32.2 | 29.4 | 12.6 | 38.3 | 48.4 | 58.3 | 56.0 | 52.7 | 49.0 | 75.5 |
| 12 | Gemma-4-E4B | 33.5 | 30.1 | 19.6 | 24.5 | 33.1 | 43.2 | 36.9 | 38.0 | 40.0 | 30.6 | 38.8 |
| 6 | InternVL3.5-4B | 48.8 | 50.9 | 77.3 | 19.4 | 60.4 | 46.4 | 46.8 | 38.0 | 47.1 | 40.8 | 61.2 |
| 10 | Qwen3-VL-4B | 45.1 | 47.7 | 44.3 | 34.5 | 64.4 | 47.8 | 42.4 | 36.0 | 37.8 | 24.5 | 71.4 |
| 7 | Qwen3-VL-8B | 48.5 | 51.5 | 50.4 | 40.2 | 67.5 | 48.0 | 45.5 | 36.0 | 44.1 | 30.6 | 71.4 |
| 3 | Qwen3-VL-32B | 53.1 | 55.3 | 60.6 | 35.1 | 71.5 | 54.0 | 50.9 | 46.0 | 51.4 | 36.7 | 69.4 |
| 5 | Spatial-MLLM-4B [39] | 49.1 | 53.0 | 76.5 | 27.0 | 57.9 | 50.6 | 45.2 | 44.0 | 40.9 | 38.8 | 57.1 |
| 4 | Cambrian-S-3B [42] | 49.5 | 51.7 | 67.1 | 22.6 | 73.8 | 43.2 | 47.3 | 54.0 | 37.1 | 26.5 | 71.4 |
| – | Think3D-4B† [46] | – | – | – | – | – | – | 45.4 | 44.7 | 39.0 | 36.7 | 61.2 |
| 2 | **AlloSpatial-4B （本文）** | **53.5** | **56.3** | **54.1** | **42.3** | **68.8** | **60.0** | **50.8** | **50.0** | **59.3** | **34.7** | **59.2** |
| 1 | **AlloSpatial-8B （本文）** | **54.2** | **47.8** | **46.1** | **26.0** | **65.6** | **53.4** | **60.6** | **52.0** | **64.1** | **46.9** | **79.6** |


> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> Considering task-level performance, AlloSpatial shows greater improvements on relational and viewpoint-dependent tasks, such as relative direction, route planning, appearance order, and MindCube tasks. As illustrated in Tab. 3, AlloSpatial-4B reaches 69.1% overall accuracy on MindCube, clearly outperforming Gemini-2.5-Pro, Think3D-4B, Spatial-MLLM-4B, and Cambrian-S-3B, with particularly large gains on AROUND and AMONG. In contrast, improvements on precise numerical estimation tasks, such as absolute distance and object counting, are less uniform. This pattern is consistent with the design of World2Mind: the AST and route maps provide robust coarse allocentric structure for relational reasoning, but the current reconstruction pipeline still limits fine-grained metric accuracy. Overall, AlloSpatial agents are most effective when the task benefits from a stable allocentric organization rather than exact metric reconstruction.


> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 从任务级表现看，AlloSpatial 在关系与视角相关任务上的提升更大，例如相对方向、路线规划、出现顺序及 MindCube 任务。如表 3 所示，AlloSpatial-4B 在 MindCube 上达到 69.1% 的总体准确率，明显超过 Gemini-2.5-Pro、Think3D-4B、Spatial-MLLM-4B 和 Cambrian-S-3B，并在 AROUND 与 AMONG 上取得特别大的增益。相比之下，对绝对距离和对象计数等精确数值估计任务的改进不够一致。这一模式与 World2Mind 的设计相符：AST 和路线图为关系推理提供稳健的粗粒度非自我中心结构，但现有重建流水线仍限制细粒度度量准确性。总体而言，当任务受益于稳定的非自我中心组织而非精确度量重建时，AlloSpatial 智能体最为有效。

### Table 3

**Caption:** Table 3: Evaluation on the MindCube (tiny split).

**Caption[CN]:** 表 3：MindCube（tiny 划分）评估结果。

| Rank | Model | Overall | Around | Among | Rotation |
|---:|---|---:|---:|---:|---:|
| 2 | Gemini-2.5-Pro | 57.9 | 67.2 | 43.8 | 88.5 |
| 5 | Gemma-4-E4B | 37.3 | 37.6 | 38.0 | 35.0 |
| 6 | InternVL3.5-4B | 36.6 | 41.6 | 35.3 | 34.0 |
| 8 | Qwen3-VL-4B | 28.3 | 40.4 | 20.8 | 35.5 |
| 4 | Spatial-MLLM-4B [39] | 39.5 | 52.0 | 36.3 | 33.5 |
| 7 | Cambrian-S-3B [42] | 33.2 | 34.4 | 34.5 | 28.0 |
| 3 | Think3D-4B† [46] | 44.0 | 42.5 | 37.5 | 42.5 |
| 1 | **AlloSpatial-4B (Ours)** | **69.1** | **82.0** | **65.0** | **65.5** |

**中文表格：**

| 排名 | 模型 | 总体 | 环绕 | 位于……之间 | 旋转 |
|---:|---|---:|---:|---:|---:|
| 2 | Gemini-2.5-Pro | 57.9 | 67.2 | 43.8 | 88.5 |
| 5 | Gemma-4-E4B | 37.3 | 37.6 | 38.0 | 35.0 |
| 6 | InternVL3.5-4B | 36.6 | 41.6 | 35.3 | 34.0 |
| 8 | Qwen3-VL-4B | 28.3 | 40.4 | 20.8 | 35.5 |
| 4 | Spatial-MLLM-4B [39] | 39.5 | 52.0 | 36.3 | 33.5 |
| 7 | Cambrian-S-3B [42] | 33.2 | 34.4 | 34.5 | 28.0 |
| 3 | Think3D-4B† [46] | 44.0 | 42.5 | 37.5 | 42.5 |
| 1 | **AlloSpatial-4B （本文）** | **69.1** | **82.0** | **65.0** | **65.5** |


> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> Figure 4 trace. Question: “What is the longest length of the chair (in centimeters)?” The model visually estimates a standard office chair at roughly 90–110 cm and calls world2mind with categories chair and desk and landmark knowledge. The tool detects chair_01 with a 0.535 m vertical extent and chair_02 with a 0.951 m vertical extent. A landmark visualization associates chair_02 with the visible office chair. Cross-validation judges the tool’s 95.1 cm estimate consistent with a typical office chair and rejects chair_01 as a partial detection. Final Answer: 95 cm.


> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> 图 4 轨迹。问题：“椅子的最长长度是多少（厘米）？”模型先从视觉上估计标准办公椅约为 90–110 cm，并以 chair、desk 为类别、landmark 为知识类型调用 world2mind。工具检测到 chair_01 的垂直范围为 0.535 m，chair_02 的垂直范围为 0.951 m。地标可视化把 chair_02 与可见办公椅对应起来。交叉验证认为工具给出的 95.1 cm 与典型办公椅一致，并把 chair_01 判定为部分检测。最终答案：95 cm。


> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> 4.4 Ablation Studies and Additional Results


> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> 4.4 消融研究与补充结果


> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> Effect of input-frame number. We study how AlloSpatial behaves under different observation budgets. Fig. 2 reports performance with 0, 3, 7, 15, and 24 uniformly sampled input frames. AlloSpatial shows the clearest advantage when visual observations are sparse. In the 0-frame setting, where the model relies only on structured AST text, AlloSpatial improves over Qwen3-VL by +18.2 points. With only 3 and 7 frames, it remains consistently stronger than both Qwen3-VL and GPT-5.2, reaching 50.0 and 53.5 overall, respectively. As the number of frames increases, the gap to Qwen3-VL narrows, suggesting that dense visual coverage can partially compensate for missing allocentric memory. This trend indicates that AlloSpatial is particularly effective under limited observations.


> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> 输入帧数的影响。作者研究 AlloSpatial 在不同观察预算下的行为。图 2 报告均匀采样 0、3、7、15 和 24 个输入帧时的表现。视觉观察稀疏时，AlloSpatial 的优势最明显。在 0 帧设置中，模型只依赖结构化 AST 文本，AlloSpatial 比 Qwen3-VL 高 +18.2 点。只有 3 帧和 7 帧时，它仍持续强于 Qwen3-VL 与 GPT-5.2，总体分数分别达到 50.0 和 53.5。随着帧数增加，与 Qwen3-VL 的差距缩小，说明密集视觉覆盖可以部分补偿非自我中心记忆的缺失。这一趋势表明，AlloSpatial 在有限观察下尤其有效。


### Figure 2

![Line chart of VSI-Bench performance versus number of input frames](figure_2_frame_budget.png)

**Caption:** Figure 2: VSI-Bench performance under different input-frame numbers.

**Caption[CN]:** 图 2：不同输入帧数下的 VSI-Bench 表现。


> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> Comparison with general thinking mode. We next compare AlloSpatial with the general thinking mode of Qwen3-VL-4B. As shown in Tab. 4, enabling thinking improves Qwen3-VL-4B on MindCube from 28.3 to 36.1, but brings only a marginal gain on VSI-Bench (45.1 → 45.5) while increasing the average response length to 1064 tokens. In contrast, AlloSpatial-4B after RL reaches 53.5 on VSI-Bench and 69.1 on MindCube with only 358 tokens on average. This suggests that the improvement does not come from longer chain-of-thought alone. Instead, the harnessed process provides a more efficient reasoning structure by grounding intermediate reasoning in explicit allocentric evidence.


> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> 与通用 thinking 模式比较。作者把 AlloSpatial 与 Qwen3-VL-4B 的通用 thinking 模式比较。如表 4 所示，启用 thinking 使 Qwen3-VL-4B 在 MindCube 上从 28.3 提升到 36.1，但在 VSI-Bench 上仅有边际提升（45.1→45.5），同时平均响应长度增至 1064 token。相比之下，RL 后的 AlloSpatial-4B 仅用平均 358 token，就在 VSI-Bench 和 MindCube 上分别达到 53.5 与 69.1。这说明提升并非仅源于更长的思维链；harness 过程通过把中间推理落地到显式非自我中心证据，提供了更高效的推理结构。

### Table 4

**Caption:** Table 4: Ablation results of AlloSpatial-4B using the same training data as QA pairs for SFT and RL; Stage-1 is SFT cold start and Stage-2 is RL.

**Caption[CN]:** 表 4：AlloSpatial-4B 消融结果。比较使用相同训练数据构成 QA 对进行 SFT 和 RL 的 Qwen3-VL-4B 变体；Stage-1 为 SFT 冷启动，Stage-2 为 RL。

| Variant | VSI-Bench | MindCube | Tokens |
|---|---:|---:|---:|
| Qwen3-VL-4B Instruct | 45.1 | 28.3 | – |
| Qwen3-VL-4B Thinking | 45.5 (↑0.4) | 36.1 (↑7.8) | 1064 |
| Qwen3-VL-4B w/ SFT on QAs | 43.1 (↓2.0) | 53.9 (↑25.6) | – |
| Qwen3-VL-4B w/ RL on QAs | 46.2 (↑1.1) | 53.0 (↑24.7) | – |
| AlloSpatial-4B Stage-1 (SFT) | 38.2 (↓6.9) | 52.0 (↑23.7) | – |
| **AlloSpatial-4B Stage-2 (RL)** | **53.5 (↑8.4)** | **69.1 (↑40.8)** | **358** |

**中文表格：**

| 变体 | VSI-Bench | MindCube | Token 数 |
|---|---:|---:|---:|
| Qwen3-VL-4B 指令模式 | 45.1 | 28.3 | – |
| Qwen3-VL-4B 思考模式 | 45.5 (↑0.4) | 36.1 (↑7.8) | 1064 |
| Qwen3-VL-4B 在 QA 上 SFT | 43.1 (↓2.0) | 53.9 (↑25.6) | – |
| Qwen3-VL-4B 在 QA 上 RL | 46.2 (↑1.1) | 53.0 (↑24.7) | – |
| AlloSpatial-4B Stage-1 (SFT) | 38.2 (↓6.9) | 52.0 (↑23.7) | – |
| **AlloSpatial-4B Stage-2 (RL)** | **53.5 (↑8.4)** | **69.1 (↑40.8)** | **358** |


> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> Comparison with QA-only training. We further perform the same two-stage training schedule on standard QA pairs constructed from the same data, to isolate whether the gains of AlloSpatial come from direct answer supervision or potential benchmark leakage. As shown in Tab. 4, QA-only SFT substantially improves MindCube from 28.3 to 53.9, but decreases VSI-Bench from 45.1 to 43.1. This suggests that answer supervision alone can fit certain benchmark patterns, but does not consistently improve spatial reasoning. QA-only RL slightly improves VSI-Bench to 46.2 and maintains a strong MindCube score of 53.0, yet remains well below AlloSpatial Stage-2, which reaches 53.5 on VSI-Bench and 69.1 on MindCube. This gap indicates that RL over QA supervision alone is insufficient; the main improvement comes from optimizing complete tool-use trajectories that follow the Spatial Reasoning Harness and interact with World2Mind during reasoning.


> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> 与仅 QA 训练比较。作者还在由同一数据构造的标准 QA 对上执行相同的两阶段训练日程，以区分 AlloSpatial 的增益来自直接答案监督还是潜在基准泄漏。如表 4 所示，仅 QA 的 SFT 使 MindCube 从 28.3 大幅升至 53.9，却使 VSI-Bench 从 45.1 降至 43.1。这说明仅用答案监督可以拟合某些基准模式，却不能持续改善空间推理。仅 QA 的 RL 把 VSI-Bench 小幅提升到 46.2，并保持 53.0 的较高 MindCube 分数，但仍远低于 AlloSpatial Stage-2 的 53.5 与 69.1。该差距说明，仅在 QA 监督上做 RL 并不充分；主要增益来自优化遵循 Spatial Reasoning Harness、且在推理期间与 World2Mind 交互的完整工具使用轨迹。


## 5 Conclusion & Limitations


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We presented AlloSpatial, an agentic framework that equips MFMs with allocentric spatial reasoning capability through the proposed World2Mind cognitive mapping sandbox and carefully designed spatial reasoning harness. Experiments on VSI-Bench and MindCube show that AlloSpatial improves proprietary models in a training-free setting and enables compact open-weight agents to outperform larger general-purpose and spatially specialized baselines. A remaining limitation of our study is numerical reasoning: current World2Mind representations provide robust allocentric structure, but reconstruction drift and imperfect metric calibration can still limit precise distance, size, and counting estimates. Future work may address this by incorporating stronger metric calibration and uncertainty-aware reconstruction into the cognitive mapping backend.


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本文提出 AlloSpatial：一种通过 World2Mind 认知建图沙盒和精心设计的空间推理 harness，让 MFM 获得非自我中心空间推理能力的智能体式框架。VSI-Bench 与 MindCube 上的实验表明，AlloSpatial 在免训练设置中提升专有模型，并使紧凑的开放权重智能体超过规模更大的通用基线与空间专用基线。本研究仍有一项局限，即数值推理：现有 World2Mind 表征提供稳健的非自我中心结构，但重建漂移和不完善的度量校准仍会限制精确的距离、尺寸与计数估计。未来可在认知建图后端引入更强的度量校准和不确定性感知重建来解决这一问题。


## References


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> [1] Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang Gao, Chunjiang Ge, et al. Qwen3-VL technical report. arXiv preprint arXiv:2511.21631, 2025.


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> [1] Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang Gao, Chunjiang Ge, et al。Qwen3-VL 技术报告。 出版信息与原文一致：arXiv preprint arXiv:2511.21631, 2025.


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> [2] Jacob LS Bellmund, Peter Gärdenfors, Edvard I Moser, and Christian F Doeller. Navigating cognition: Spatial codes for human thinking. Science, 362(6415):eaat6766, 2018.


> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> [2] Jacob LS Bellmund, Peter Gärdenfors, Edvard I Moser, and Christian F Doeller。导航认知：人类思维的空间编码。 出版信息与原文一致：Science, 362(6415):eaat6766, 2018.


> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> [3] Neil Burgess. Spatial memory: how egocentric and allocentric combine. Trends in Cognitive Sciences, 10(12):551–557, 2006.


> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> [3] Neil Burgess。空间记忆：自我中心与非自我中心如何结合。 出版信息与原文一致：Trends in Cognitive Sciences, 10(12):551–557, 2006.


> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> [4] Wenxiao Cai, Iaroslav Ponomarenko, Jianhao Yuan, Xiaoqi Li, Wankou Yang, Hao Dong, and Bo Zhao. SpatialBot: Precise spatial understanding with vision language models. In 2025 IEEE International Conference on Robotics and Automation (ICRA), pages 9490–9498. IEEE, 2025.


> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> [4] Wenxiao Cai, Iaroslav Ponomarenko, Jianhao Yuan, Xiaoqi Li, Wankou Yang, Hao Dong, and Bo Zhao。SpatialBot：用视觉语言模型实现精确空间理解。 出版信息与原文一致：In 2025 IEEE International Conference on Robotics and Automation (ICRA), pages 9490–9498. IEEE, 2025.


> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> [5] Meng Cao, Xingyu Li, Xue Liu, Ian Reid, and Xiaodan Liang. SpatialDreamer: Incentivizing spatial reasoning via active mental imagery. arXiv preprint arXiv:2512.07733, 2025.


> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> [5] Meng Cao, Xingyu Li, Xue Liu, Ian Reid, and Xiaodan Liang。SpatialDreamer：通过主动心智意象激励空间推理。 出版信息与原文一致：arXiv preprint arXiv:2512.07733, 2025.


> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> [6] Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath, Ronghang Hu, Didac Suris, Chaitanya Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew Huang, et al. SAM 3: Segment anything with concepts. arXiv preprint arXiv:2511.16719, 2025.


> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> [6] Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath, Ronghang Hu, Didac Suris, Chaitanya Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew Huang, et al。SAM 3：使用概念分割万物。 出版信息与原文一致：arXiv preprint arXiv:2511.16719, 2025.


> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> [7] Boyuan Chen, Zhuo Xu, Sean Kirmani, Brain Ichter, Dorsa Sadigh, Leonidas Guibas, and Fei Xia. SpatialVLM: Endowing vision-language models with spatial reasoning capabilities. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 14455–14465, 2024.


> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> [7] Boyuan Chen, Zhuo Xu, Sean Kirmani, Brain Ichter, Dorsa Sadigh, Leonidas Guibas, and Fei Xia。SpatialVLM：赋予视觉语言模型空间推理能力。 出版信息与原文一致：In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 14455–14465, 2024.


> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> [8] Pingyi Chen, Yujing Lou, Shen Cao, Jinhui Guo, Lubin Fan, Yue Wu, Lin Yang, Lizhuang Ma, and Jieping Ye. SD-VLM: Spatial measuring and understanding with depth-encoded vision-language models. arXiv preprint arXiv:2509.17664, 2025.


> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> [8] Pingyi Chen, Yujing Lou, Shen Cao, Jinhui Guo, Lubin Fan, Yue Wu, Lin Yang, Lizhuang Ma, and Jieping Ye。SD-VLM：使用深度编码视觉语言模型进行空间测量与理解。 出版信息与原文一致：arXiv preprint arXiv:2509.17664, 2025.


> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> [9] Siyi Chen, Mikaela Angelina Uy, Chan Hee Song, Faisal Ladhak, Adithyavairavan Murali, Qing Qu, Stan Birchfield, Valts Blukis, and Jonathan Tremblay. SpaceTools: Tool-augmented spatial reasoning via double interactive RL. arXiv preprint arXiv:2512.04069, 2025.


> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> [9] Siyi Chen, Mikaela Angelina Uy, Chan Hee Song, Faisal Ladhak, Adithyavairavan Murali, Qing Qu, Stan Birchfield, Valts Blukis, and Jonathan Tremblay。SpaceTools：通过双重交互式 RL 实现工具增强空间推理。 出版信息与原文一致：arXiv preprint arXiv:2512.04069, 2025.


> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> [10] An-Chieh Cheng, Hongxu Yin, Yang Fu, Qiushan Guo, Ruihan Yang, Jan Kautz, Xiaolong Wang, and Sifei Liu. SpatialRGPT: Grounded spatial reasoning in vision-language models. Advances in Neural Information Processing Systems, 37:135062–135093, 2024.


> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> [10] An-Chieh Cheng, Hongxu Yin, Yang Fu, Qiushan Guo, Ruihan Yang, Jan Kautz, Xiaolong Wang, and Sifei Liu。SpatialRGPT：视觉语言模型中的落地空间推理。 出版信息与原文一致：Advances in Neural Information Processing Systems, 37:135062–135093, 2024.


> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> [11] Erik Daxberger, Nina Wenzel, David Griffiths, Haiming Gang, Justin Lazarow, Gefen Kohavi, Kai Kang, Marcin Eichner, Yinfei Yang, Afshin Dehghan, et al. MM-Spatial: Exploring 3D spatial understanding in multimodal LLMs. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 7395–7408, 2025.


> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> [11] Erik Daxberger, Nina Wenzel, David Griffiths, Haiming Gang, Justin Lazarow, Gefen Kohavi, Kai Kang, Marcin Eichner, Yinfei Yang, Afshin Dehghan, et al。MM-Spatial：探索多模态 LLM 的三维空间理解。 出版信息与原文一致：In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 7395–7408, 2025.


> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> [12] Nianchen Deng, Lixin Gu, Shenglong Ye, Yinan He, Zhe Chen, Songze Li, Haomin Wang, Xingguang Wei, Tianshuo Yang, Min Dou, et al. InternSpatial: A comprehensive dataset for spatial reasoning in vision-language models. arXiv preprint arXiv:2506.18385, 2025.


> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> [12] Nianchen Deng, Lixin Gu, Shenglong Ye, Yinan He, Zhe Chen, Songze Li, Haomin Wang, Xingguang Wei, Tianshuo Yang, Min Dou, et al。InternSpatial：面向视觉语言模型空间推理的综合数据集。 出版信息与原文一致：arXiv preprint arXiv:2506.18385, 2025.


> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> [13] Google. Gemini 3.1 Pro: Best for complex tasks and bringing creative concepts to life. https://deepmind.google/models/gemini/pro/, 2026.


> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> [13] Google。Gemini 3.1 Pro：最适合复杂任务并把创意概念带入现实。 出版信息与原文一致：https://deepmind.google/models/gemini/pro/, 2026.


> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> [14] Google DeepMind. Gemma 4, 2026. URL https://deepmind.google/models/gemma/gemma-4/. Accessed: 2026-05-06.


> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> [14] Google DeepMind。Gemma 4；访问日期：2026-05-06。 出版信息与原文一致：URL https://deepmind.google/models/gemma/gemma-4/. Accessed: 2026-05-06.


> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> [15] Qiao Gu, Ali Kuwajerwala, Sacha Morin, Krishna Murthy Jatavallabhula, Bipasha Sen, Aditya Agarwal, Corban Rivera, William Paul, Kirsty Ellis, Rama Chellappa, et al. ConceptGraphs: Open-vocabulary 3D scene graphs for perception and planning. In 2024 IEEE International Conference on Robotics and Automation (ICRA), pages 5021–5028. IEEE, 2024.


> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> [15] Qiao Gu, Ali Kuwajerwala, Sacha Morin, Krishna Murthy Jatavallabhula, Bipasha Sen, Aditya Agarwal, Corban Rivera, William Paul, Kirsty Ellis, Rama Chellappa, et al。ConceptGraphs：用于感知与规划的开放词汇三维场景图。 出版信息与原文一致：In 2024 IEEE International Conference on Robotics and Automation (ICRA), pages 5021–5028. IEEE, 2024.


> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> [16] Jiaxin Huang, Ziwen Li, Hanlve Zhang, Runnan Chen, Xiao He, Yandong Guo, Wenping Wang, Tongliang Liu, and Mingming Gong. Surprise3D: A dataset for spatial understanding and reasoning in complex 3D scenes. arXiv preprint arXiv:2507.07781, 2025.


> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> [16] Jiaxin Huang, Ziwen Li, Hanlve Zhang, Runnan Chen, Xiao He, Yandong Guo, Wenping Wang, Tongliang Liu, and Mingming Gong。Surprise3D：复杂三维场景中的空间理解与推理数据集。 出版信息与原文一致：arXiv preprint arXiv:2507.07781, 2025.


> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> [17] Shuai Huang, Wenxuan Zhao, and Jun Gao. SI-Bench: Benchmarking social intelligence of large language models in human-to-human conversations. arXiv preprint arXiv:2510.23182, 2025.


> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> [17] Shuai Huang, Wenxuan Zhao, and Jun Gao。SI-Bench：在人与人对话中基准测试大语言模型的社交智能。 出版信息与原文一致：arXiv preprint arXiv:2510.23182, 2025.


> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> [18] Haotong Lin, Sili Chen, Junhao Liew, Donny Y Chen, Zhenyu Li, Guang Shi, Jiashi Feng, and Bingyi Kang. Depth Anything 3: Recovering the visual space from any views. arXiv preprint arXiv:2511.10647, 2025.


> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> [18] Haotong Lin, Sili Chen, Junhao Liew, Donny Y Chen, Zhenyu Li, Guang Shi, Jiashi Feng, and Bingyi Kang。Depth Anything 3：从任意视图恢复视觉空间。 出版信息与原文一致：arXiv preprint arXiv:2511.10647, 2025.


> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> [19] Jingli Lin, Runsen Xu, Shaohao Zhu, Sihan Yang, Peizhou Cao, Yunlong Ran, Miao Hu, Chenming Zhu, Yiman Xie, Yilin Long, et al. MMSI-Video-Bench: A holistic benchmark for video-based spatial intelligence. arXiv preprint arXiv:2512.10863, 2025.


> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> [19] Jingli Lin, Runsen Xu, Shaohao Zhu, Sihan Yang, Peizhou Cao, Yunlong Ran, Miao Hu, Chenming Zhu, Yiman Xie, Yilin Long, et al。MMSI-Video-Bench：基于视频空间智能的整体性基准。 出版信息与原文一致：arXiv preprint arXiv:2512.10863, 2025.


> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> [20] Zhanpeng Luo, Ce Zhang, Silong Yong, Cunxi Dai, Qianwei Wang, Haoxi Ran, Guanya Shi, Katia Sycara, and Yaqi Xie. pySpatial: Generating 3D visual programs for zero-shot spatial reasoning. arXiv preprint arXiv:2603.00905, 2026.


> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> [20] Zhanpeng Luo, Ce Zhang, Silong Yong, Cunxi Dai, Qianwei Wang, Haoxi Ran, Guanya Shi, Katia Sycara, and Yaqi Xie。pySpatial：为零样本空间推理生成三维视觉程序。 出版信息与原文一致：arXiv preprint arXiv:2603.00905, 2026.


> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> [21] Wufei Ma, Yu-Cheng Chou, Qihao Liu, Xingrui Wang, Celso de Melo, Jianwen Xie, and Alan Yuille. SpatialReasoner: Towards explicit and generalizable 3D spatial reasoning. arXiv preprint arXiv:2504.20024, 2025.


> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> [21] Wufei Ma, Yu-Cheng Chou, Qihao Liu, Xingrui Wang, Celso de Melo, Jianwen Xie, and Alan Yuille。SpatialReasoner：迈向显式且可泛化的三维空间推理。 出版信息与原文一致：arXiv preprint arXiv:2504.20024, 2025.


> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> [22] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. Self-Refine: Iterative refinement with self-feedback. Advances in Neural Information Processing Systems, 36:46534–46594, 2023.


> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> [22] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al。Self-Refine：通过自反馈进行迭代式改进。 出版信息与原文一致：Advances in Neural Information Processing Systems, 36:46534–46594, 2023.


> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> [23] Zhenhua Ning, Zhuotao Tian, Shaoshuai Shi, Guangming Lu, Daojing He, Wenjie Pei, and Li Jiang. Enhancing spatial reasoning in multimodal large language models through reasoning-based segmentation. In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 7851–7860, 2025.


> <span style="color:#F59E0B"><strong>Para. 23[CN]:</strong></span> [23] Zhenhua Ning, Zhuotao Tian, Shaoshuai Shi, Guangming Lu, Daojing He, Wenjie Pei, and Li Jiang。通过基于推理的分割增强多模态大语言模型空间推理。 出版信息与原文一致：In Proceedings of the IEEE/CVF International Conference on Computer Vision, pages 7851–7860, 2025.


> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> [24] John O’Keefe and Lynn Nadel. The hippocampus as a cognitive map. Oxford University Press, 1978.


> <span style="color:#F59E0B"><strong>Para. 24[CN]:</strong></span> [24] John O’Keefe and Lynn Nadel。把海马体视为认知地图。 出版信息与原文一致：Oxford University Press, 1978.


> <span style="color:#3B82F6"><strong>Para. 25:</strong></span> [25] OpenAI. GPT-4V(ision) system card. https://cdn.openai.com/papers/GPTV_System_Card.pdf, 2023.


> <span style="color:#F59E0B"><strong>Para. 25[CN]:</strong></span> [25] OpenAI。GPT-4V(ision) 系统卡。 出版信息与原文一致：https://cdn.openai.com/papers/GPTV_System_Card.pdf, 2023.


> <span style="color:#3B82F6"><strong>Para. 26:</strong></span> [26] Kun Ouyang. Spatial-R1: Enhancing MLLMs in video spatial reasoning. arXiv e-prints, pages arXiv–2504, 2025.


> <span style="color:#F59E0B"><strong>Para. 26[CN]:</strong></span> [26] Kun Ouyang。Spatial-R1：增强 MLLM 的视频空间推理。 出版信息与原文一致：arXiv e-prints, pages arXiv–2504, 2025.


> <span style="color:#3B82F6"><strong>Para. 27:</strong></span> [27] Jianing Qi, Jiawei Liu, Hao Tang, and Zhigang Zhu. Beyond semantics: Rediscovering spatial awareness in vision-language models. arXiv preprint arXiv:2503.17349, 2025.


> <span style="color:#F59E0B"><strong>Para. 27[CN]:</strong></span> [27] Jianing Qi, Jiawei Liu, Hao Tang, and Zhigang Zhu。超越语义：重新发现视觉语言模型的空间感知。 出版信息与原文一致：arXiv preprint arXiv:2503.17349, 2025.


> <span style="color:#3B82F6"><strong>Para. 28:</strong></span> [28] Santhosh Kumar Ramakrishnan, Erik Wijmans, Philipp Kraehenbuehl, and Vladlen Koltun. Does spatial cognition emerge in frontier models? arXiv preprint arXiv:2410.06468, 2024.


> <span style="color:#F59E0B"><strong>Para. 28[CN]:</strong></span> [28] Santhosh Kumar Ramakrishnan, Erik Wijmans, Philipp Kraehenbuehl, and Vladlen Koltun。空间认知是否在前沿模型中涌现？ 出版信息与原文一致：Does spatial cognition emerge in frontier models? arXiv preprint arXiv:2410.06468, 2024.


> <span style="color:#3B82F6"><strong>Para. 29:</strong></span> [29] Krishan Rana, Jesse Haviland, Sourav Garg, Jad Abou-Chakra, Ian Reid, and Niko Suenderhauf. SayPlan: Grounding large language models using 3D scene graphs for scalable robot task planning. arXiv preprint arXiv:2307.06135, 2023.


> <span style="color:#F59E0B"><strong>Para. 29[CN]:</strong></span> [29] Krishan Rana, Jesse Haviland, Sourav Garg, Jad Abou-Chakra, Ian Reid, and Niko Suenderhauf。SayPlan：利用三维场景图落地大语言模型，以实现可扩展机器人任务规划。 出版信息与原文一致：arXiv preprint arXiv:2307.06135, 2023.


> <span style="color:#3B82F6"><strong>Para. 30:</strong></span> [30] Shouwei Ruan, Liyuan Wang, Caixin Kang, Qihui Zhu, Songming Liu, Xingxing Wei, and Hang Su. From reactive to cognitive: Brain-inspired spatial intelligence for embodied agents. Intelligence (AGI), 3(9):10, 2025.


> <span style="color:#F59E0B"><strong>Para. 30[CN]:</strong></span> [30] Shouwei Ruan, Liyuan Wang, Caixin Kang, Qihui Zhu, Songming Liu, Xingxing Wei, and Hang Su。从反应式到认知式：面向具身智能体的脑启发空间智能。 出版信息与原文一致：Intelligence (AGI), 3(9):10, 2025.


> <span style="color:#3B82F6"><strong>Para. 31:</strong></span> [31] Daniela Schiller, Howard Eichenbaum, Elizabeth A Buffalo, Lila Davachi, David J Foster, Stefan Leutgeb, and Charan Ranganath. Memory and space: Towards an understanding of the cognitive map. Journal of Neuroscience, 35(41):13904–13911, 2015.


> <span style="color:#F59E0B"><strong>Para. 31[CN]:</strong></span> [31] Daniela Schiller, Howard Eichenbaum, Elizabeth A Buffalo, Lila Davachi, David J Foster, Stefan Leutgeb, and Charan Ranganath。记忆与空间：迈向对认知地图的理解。 出版信息与原文一致：Journal of Neuroscience, 35(41):13904–13911, 2015.


> <span style="color:#3B82F6"><strong>Para. 32:</strong></span> [32] Aaditya Singh, Adam Fry, Adam Perelman, Adam Tart, Adi Ganesh, Ahmed El-Kishky, Aidan McLaughlin, Aiden Low, AJ Ostrow, Akhila Ananthram, et al. OpenAI GPT-5 system card. arXiv preprint arXiv:2601.03267, 2025.


> <span style="color:#F59E0B"><strong>Para. 32[CN]:</strong></span> [32] Aaditya Singh, Adam Fry, Adam Perelman, Adam Tart, Adi Ganesh, Ahmed El-Kishky, Aidan McLaughlin, Aiden Low, AJ Ostrow, Akhila Ananthram, et al。OpenAI GPT-5 系统卡。 出版信息与原文一致：arXiv preprint arXiv:2601.03267, 2025.


> <span style="color:#3B82F6"><strong>Para. 33:</strong></span> [33] Zhaochen Su, Peng Xia, Hangyu Guo, Zhenhua Liu, Yan Ma, Xiaoye Qu, Jiaqi Liu, Yanshu Li, Kaide Zeng, Zhengyuan Yang, et al. Thinking with images for multimodal reasoning: Foundations, methods, and future frontiers. arXiv preprint arXiv:2506.23918, 2025.


> <span style="color:#F59E0B"><strong>Para. 33[CN]:</strong></span> [33] Zhaochen Su, Peng Xia, Hangyu Guo, Zhenhua Liu, Yan Ma, Xiaoye Qu, Jiaqi Liu, Yanshu Li, Kaide Zeng, Zhengyuan Yang, et al。用图像思考以进行多模态推理：基础、方法与未来前沿。 出版信息与原文一致：arXiv preprint arXiv:2506.23918, 2025.


> <span style="color:#3B82F6"><strong>Para. 34:</strong></span> [34] Jianyuan Wang, Minghao Chen, Nikita Karaev, Andrea Vedaldi, Christian Rupprecht, and David Novotny. VGGT: Visual Geometry Grounded Transformer. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 5294–5306, 2025.


> <span style="color:#F59E0B"><strong>Para. 34[CN]:</strong></span> [34] Jianyuan Wang, Minghao Chen, Nikita Karaev, Andrea Vedaldi, Christian Rupprecht, and David Novotny。VGGT：视觉几何落地 Transformer。 出版信息与原文一致：In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 5294–5306, 2025.


> <span style="color:#3B82F6"><strong>Para. 35:</strong></span> [35] Qineng Wang, Baiqiao Yin, Pingyue Zhang, Jianshu Zhang, Kangrui Wang, Zihan Wang, Jieyu Zhang, Keshigeyan Chandrasegaran, Han Liu, Ranjay Krishna, et al. MindCube: Spatial mental modeling from limited views. arXiv e-prints, pages arXiv–2506, 2025.


> <span style="color:#F59E0B"><strong>Para. 35[CN]:</strong></span> [35] Qineng Wang, Baiqiao Yin, Pingyue Zhang, Jianshu Zhang, Kangrui Wang, Zihan Wang, Jieyu Zhang, Keshigeyan Chandrasegaran, Han Liu, Ranjay Krishna, et al。MindCube：从有限视图进行空间心智建模。 出版信息与原文一致：arXiv e-prints, pages arXiv–2506, 2025.


> <span style="color:#3B82F6"><strong>Para. 36:</strong></span> [36] Weiyun Wang, Zhangwei Gao, Lixin Gu, Hengjun Pu, Long Cui, Xingguang Wei, Zhaoyang Liu, Linglin Jing, Shenglong Ye, Jie Shao, et al. InternVL3.5: Advancing open-source multimodal models in versatility, reasoning, and efficiency. arXiv preprint arXiv:2508.18265, 2025.


> <span style="color:#F59E0B"><strong>Para. 36[CN]:</strong></span> [36] Weiyun Wang, Zhangwei Gao, Lixin Gu, Hengjun Pu, Long Cui, Xingguang Wei, Zhaoyang Liu, Linglin Jing, Shenglong Ye, Jie Shao, et al。InternVL3.5：提升开源多模态模型的通用性、推理与效率。 出版信息与原文一致：arXiv preprint arXiv:2508.18265, 2025.


> <span style="color:#3B82F6"><strong>Para. 37:</strong></span> [37] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le, Ed H Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. In The Eleventh International Conference on Learning Representations, 2023.


> <span style="color:#F59E0B"><strong>Para. 37[CN]:</strong></span> [37] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V Le, Ed H Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou。自洽性改善语言模型中的思维链推理。 出版信息与原文一致：In The Eleventh International Conference on Learning Representations, 2023.


> <span style="color:#3B82F6"><strong>Para. 38:</strong></span> [38] Yuxin Wang, Lei Ke, Boqiang Zhang, Tianyuan Qu, Hanxun Yu, Zhenpeng Huang, Meng Yu, Dan Xu, and Dong Yu. N3D-VLM: Native 3D grounding enables accurate spatial reasoning in vision-language models. arXiv preprint arXiv:2512.16561, 2025.


> <span style="color:#F59E0B"><strong>Para. 38[CN]:</strong></span> [38] Yuxin Wang, Lei Ke, Boqiang Zhang, Tianyuan Qu, Hanxun Yu, Zhenpeng Huang, Meng Yu, Dan Xu, and Dong Yu。N3D-VLM：原生三维落地实现视觉语言模型的精确空间推理。 出版信息与原文一致：arXiv preprint arXiv:2512.16561, 2025.


> <span style="color:#3B82F6"><strong>Para. 39:</strong></span> [39] Diankun Wu, Fangfu Liu, Yi-Hsin Hung, and Yueqi Duan. Spatial-MLLM: Boosting MLLM capabilities in visual-based spatial intelligence. arXiv preprint arXiv:2505.23747, 2025.


> <span style="color:#F59E0B"><strong>Para. 39[CN]:</strong></span> [39] Diankun Wu, Fangfu Liu, Yi-Hsin Hung, and Yueqi Duan。Spatial-MLLM：提升 MLLM 的视觉空间智能能力。 出版信息与原文一致：arXiv preprint arXiv:2505.23747, 2025.


> <span style="color:#3B82F6"><strong>Para. 40:</strong></span> [40] Mingrui Wu, Zhaozhi Wang, Fangjinhua Wang, Jiaolong Yang, Marc Pollefeys, and Tong Zhang. From indoor to open world: Revealing the spatial reasoning gap in MLLMs. arXiv preprint arXiv:2512.19683, 2025.


> <span style="color:#F59E0B"><strong>Para. 40[CN]:</strong></span> [40] Mingrui Wu, Zhaozhi Wang, Fangjinhua Wang, Jiaolong Yang, Marc Pollefeys, and Tong Zhang。从室内到开放世界：揭示 MLLM 的空间推理差距。 出版信息与原文一致：arXiv preprint arXiv:2512.19683, 2025.


> <span style="color:#3B82F6"><strong>Para. 41:</strong></span> [41] Jihan Yang, Shusheng Yang, Anjali W Gupta, Rilyn Han, Li Fei-Fei, and Saining Xie. Thinking in space: How multimodal large language models see, remember, and recall spaces. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 10632–10643, 2025.


> <span style="color:#F59E0B"><strong>Para. 41[CN]:</strong></span> [41] Jihan Yang, Shusheng Yang, Anjali W Gupta, Rilyn Han, Li Fei-Fei, and Saining Xie。在空间中思考：多模态大语言模型如何观察、记忆与回忆空间。 出版信息与原文一致：In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 10632–10643, 2025.


> <span style="color:#3B82F6"><strong>Para. 42:</strong></span> [42] Shusheng Yang, Jihan Yang, Pinzhi Huang, Ellis Brown, Zihao Yang, Yue Yu, Shengbang Tong, Zihan Zheng, Yifan Xu, Muhan Wang, et al. Cambrian-S: Towards spatial supersensing in video. arXiv preprint arXiv:2511.04670, 2025.


> <span style="color:#F59E0B"><strong>Para. 42[CN]:</strong></span> [42] Shusheng Yang, Jihan Yang, Pinzhi Huang, Ellis Brown, Zihao Yang, Yue Yu, Shengbang Tong, Zihan Zheng, Yifan Xu, Muhan Wang, et al。Cambrian-S：迈向视频中的空间超感知。 出版信息与原文一致：arXiv preprint arXiv:2511.04670, 2025.


> <span style="color:#3B82F6"><strong>Para. 43:</strong></span> [43] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. ReAct: Synergizing reasoning and acting in language models. In International Conference on Learning Representations (ICLR), 2023.


> <span style="color:#F59E0B"><strong>Para. 43[CN]:</strong></span> [43] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao。ReAct：在语言模型中协同推理与行动。 出版信息与原文一致：In International Conference on Learning Representations (ICLR), 2023.


> <span style="color:#3B82F6"><strong>Para. 44:</strong></span> [44] Kaichen Zhang, Bo Li, Peiyuan Zhang, Fanyi Pu, Joshua Adrian Cahyono, Kairui Hu, Shuai Liu, Yuanhan Zhang, Jingkang Yang, Chunyuan Li, and Ziwei Liu. LMMs-Eval: Reality check on the evaluation of large multimodal models, 2024. URL https://arxiv.org/abs/2407.12772.


> <span style="color:#F59E0B"><strong>Para. 44[CN]:</strong></span> [44] Kaichen Zhang, Bo Li, Peiyuan Zhang, Fanyi Pu, Joshua Adrian Cahyono, Kairui Hu, Shuai Liu, Yuanhan Zhang, Jingkang Yang, Chunyuan Li, and Ziwei Liu。LMMs-Eval：对大型多模态模型评估进行现实核验。 出版信息与原文一致：URL https://arxiv.org/abs/2407.12772.


> <span style="color:#3B82F6"><strong>Para. 45:</strong></span> [45] Weichen Zhang, Ruiying Peng, Chen Gao, Jianjie Fang, Xin Zeng, Kaiyuan Li, Ziyou Wang, Jinqiang Cui, Xin Wang, Xinlei Chen, et al. The point, the vision and the text: Does point cloud boost spatial reasoning of large language models? arXiv preprint arXiv:2504.04540, 2025.


> <span style="color:#F59E0B"><strong>Para. 45[CN]:</strong></span> [45] Weichen Zhang, Ruiying Peng, Chen Gao, Jianjie Fang, Xin Zeng, Kaiyuan Li, Ziyou Wang, Jinqiang Cui, Xin Wang, Xinlei Chen, et al。点、视觉与文本：点云是否提升大语言模型的空间推理？ 出版信息与原文一致：The point, the vision and the text: Does point cloud boost spatial reasoning of large language models? arXiv preprint arXiv:2504.04540, 2025.


> <span style="color:#3B82F6"><strong>Para. 46:</strong></span> [46] Zaibin Zhang, Yuhan Wu, Lianjie Jia, Yifan Wang, Zhongbo Zhang, Yijiang Li, Binghao Ran, Fuxi Zhang, Zhuohan Sun, Zhenfei Yin, et al. Think3D: Thinking with space for spatial reasoning. arXiv preprint arXiv:2601.13029, 2026.


> <span style="color:#F59E0B"><strong>Para. 46[CN]:</strong></span> [46] Zaibin Zhang, Yuhan Wu, Lianjie Jia, Yifan Wang, Zhongbo Zhang, Yijiang Li, Binghao Ran, Fuxi Zhang, Zhuohan Sun, Zhenfei Yin, et al。Think3D：用空间思考以进行空间推理。 出版信息与原文一致：arXiv preprint arXiv:2601.13029, 2026.


> <span style="color:#3B82F6"><strong>Para. 47:</strong></span> [47] Yuze Zhao, Jintao Huang, Jinghan Hu, Xingjun Wang, Yunlin Mao, Daoze Zhang, Zeyinzi Jiang, Zhikai Wu, Baole Ai, Ang Wang, Wenmeng Zhou, and Yingda Chen. SWIFT: A scalable lightweight infrastructure for fine-tuning, 2024. URL https://arxiv.org/abs/2408.05517.


> <span style="color:#F59E0B"><strong>Para. 47[CN]:</strong></span> [47] Yuze Zhao, Jintao Huang, Jinghan Hu, Xingjun Wang, Yunlin Mao, Daoze Zhang, Zeyinzi Jiang, Zhikai Wu, Baole Ai, Ang Wang, Wenmeng Zhou, and Yingda Chen。SWIFT：用于微调的可扩展轻量基础设施。 出版信息与原文一致：URL https://arxiv.org/abs/2408.05517.


> <span style="color:#3B82F6"><strong>Para. 48:</strong></span> [48] Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, et al. Group sequence policy optimization. arXiv preprint arXiv:2507.18071, 2025.


> <span style="color:#F59E0B"><strong>Para. 48[CN]:</strong></span> [48] Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, et al。组序列策略优化。 出版信息与原文一致：arXiv preprint arXiv:2507.18071, 2025.


## Appendix A — Training & Evaluation Configuration


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> RL training configuration. AlloSpatial-4B and AlloSpatial-8B are initialized from their corresponding supervised cold-start checkpoints at step 240, after three epochs of SFT. We optimize both agents with GSPO using the ms-swift framework [47] and DeepSpeed ZeRO-2. The RL prompts are sampled from a shared training pool of 59,981 examples, including 49,981 VSI-style examples from VSI-590K and 10,000 examples from the MindCube training split. Inline validation is performed on 1,442 held-out examples, consisting of 392 VSI-Bench-tiny questions and 1,050 MindCube-tiny questions. For each prompt, the policy samples 8 rollouts, with at most 5 tool-interaction turns per rollout. The maximum sequence length is 32,768 tokens, and generated completions are capped at 8,192 tokens. The trajectory reward follows HGTR, combining structural compliance, answer accuracy, tool-use effectiveness, and length control with weights 0.15, 0.60, 0.10, and 0.15, respectively. Validation rewards are logged for monitoring but are not used for optimization.


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> RL 训练配置。AlloSpatial-4B 与 AlloSpatial-8B 在完成三轮 SFT 后，均从各自第 240 步的监督式冷启动检查点初始化。作者使用 ms-swift 框架 [47] 和 DeepSpeed ZeRO-2，以 GSPO 优化两个智能体。RL 提示从包含 59,981 个样本的共享训练池采样，其中包括 VSI-590K 的 49,981 个 VSI 风格样本，以及 MindCube 训练划分的 10,000 个样本。在线验证在 1,442 个留出样本上进行，包括 392 个 VSI-Bench-tiny 问题和 1,050 个 MindCube-tiny 问题。每个提示由策略采样 8 条 rollout，每条 rollout 最多 5 轮工具交互。最大序列长度为 32,768 token，生成补全上限为 8,192 token。轨迹奖励遵循 HGTR，以 0.15、0.60、0.10、0.15 的权重分别组合结构合规性、答案准确性、工具使用有效性与长度控制。验证奖励只记录用于监控，不用于优化。


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Both runs use cosine learning-rate decay with a warmup ratio of 0.005, freeze the vision tower and aligner modules, and adopt ε_high = 0.28 with overlong-completion filtering. The training scripts are epoch-based rather than hard-coded with a fixed maximum number of steps; the reported checkpoints are selected by validation performance and inference efficiency. Detailed configuration information is shown in Tab. 5.


> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 两次训练均采用余弦学习率衰减，warmup 比率为 0.005，冻结视觉塔和对齐器模块，并使用 $\epsilon_{high}=0.28$ 与超长补全过滤。训练脚本以 epoch 为基础，而非硬编码固定的最大步数；报告的检查点根据验证表现与推理效率选择。详细配置见表 5。


### Table 5

**Caption:** Table 5: GSPO training configuration for the reported AlloSpatial checkpoints. The main paper reports the 600-step AlloSpatial-4B checkpoint and the 400-step AlloSpatial-8B checkpoint. Unique prompts are counted after grouping the 8 sampled rollouts per prompt.

**Caption[CN]:** 表 5：所报告 AlloSpatial 检查点的 GSPO 训练配置。正文报告 AlloSpatial-4B 的 600 步检查点与 AlloSpatial-8B 的 400 步检查点。唯一提示数在把每个提示采样的 8 条 rollout 分组后计数。

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
| Unique prompts to reported checkpoint | 4.8K | 2.4K |
| Learning rate | 1 × 10⁻⁶ | 5 × 10⁻⁷ |
| Precision / attention | bf16 / FlashAttention | bf16 / FlashAttention |
| Trainable modules | language modules | language modules |
| Optimizer infrastructure | full tuning + ZeRO-2 | full tuning + ZeRO-2 |
| Sampling temperature | 1.0 | 1.0 |
| KL coefficient β | 0.01 | 0.0 |
| Eval / save interval | 100 steps | 50 steps |

**中文表格：**

| 设置 | AlloSpatial-4B | AlloSpatial-8B |
|---|---|---|
| 初始化 | Qwen3-VL-4B SFT 步 240 | Qwen3-VL-8B SFT 步 240 |
| 报告的 RL 检查点 | 步 600 | 步 400 |
| 训练进程 | 4 | 6 |
| 每设备训练批量 | 4 | 2 |
| 梯度累积 | 4 | 4 |
| 每次更新生成轨迹数 | 64 | 48 |
| 每次更新唯一提示数 | 8 | 6 |
| 每提示 rollout 数 | 8 | 8 |
| 到报告检查点的唯一提示数 | 4.8K | 2.4K |
| 学习率 | 1 × 10⁻⁶ | 5 × 10⁻⁷ |
| 精度 / 注意力 | bf16 / FlashAttention | bf16 / FlashAttention |
| 可训练模块 | 语言模块 | 语言模块 |
| 优化器基础设施 | 全参数微调 + ZeRO-2 | 全参数微调 + ZeRO-2 |
| 采样温度 | 1.0 | 1.0 |
| KL 系数 β | 0.01 | 0.0 |
| 评估 / 保存间隔 | 100 步s | 50 步s |


> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Evaluation configuration. For trained local agents, we evaluate AlloSpatial with the lmms-eval framework [44]. The evaluator parses final responses from predefined answer tags, uses temperature 1.0, allows up to 8 reasoning turns, and caps each completion at 8,192 new tokens. For VSI-Bench, the main post-trained evaluation follows the limited-observation setting with 7 uniformly sampled frames, while the frame-budget ablation evaluates 0, 3, 7, 15, and 24 input frames. For training-free proprietary-model evaluation, we uniformly sample up to 32 frames to provide sufficient observations for external cognitive mapping. MindCube is evaluated using the provided multi-view images.


> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 评估配置。对于训练后的本地智能体，作者使用 lmms-eval 框架 [44] 评估 AlloSpatial。评估器从预定义答案标签解析最终响应，温度设为 1.0，最多允许 8 轮推理，每次补全上限为 8,192 个新 token。VSI-Bench 的主要后训练评估遵循有限观察设置，均匀采样 7 帧；帧预算消融则评估 0、3、7、15、24 个输入帧。免训练专有模型评估均匀采样至多 32 帧，为外部认知建图提供充分观察。MindCube 使用所提供的多视图图像进行评估。


> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Across local-agent experiments, World2Mind uses the same default cognitive mapping pipeline, including monocular depth and pose estimation, SAM3-based open-vocabulary segmentation, confidence filtering, semantic point-cloud construction, AST serialization, and optional top-down map rendering. During evaluation, tool calls generated by the model are executed online, and the returned ASTs, route maps, or visualizations are inserted into the dialogue context for subsequent harness-guided reasoning.


> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在所有本地智能体实验中，World2Mind 使用相同的默认认知建图流水线，包括单目深度与姿态估计、基于 SAM3 的开放词汇分割、置信度过滤、语义点云构建、AST 序列化和可选俯视地图渲染。评估时，模型生成的工具调用会在线执行；返回的 AST、路线图或可视化会插入对话上下文，供之后的 harness 引导推理使用。


## Appendix B — World2Mind Service Parallelization


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> RL rollout generation can produce many concurrent World2Mind calls, while a single World2Mind process would serialize reconstruction and mapping requests. We therefore deploy World2Mind as a multi-process HTTP service during training and local evaluation. Each service process is assigned to an independent NPU worker and initializes the same cognitive mapping pipeline, including monocular geometry estimation, SAM3 segmentation, semantic point-cloud construction, AST generation, and route-map rendering. In our main configuration, eight World2Mind workers are launched in parallel to support concurrent tool execution.


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> RL rollout 生成可能产生大量并发 World2Mind 调用，而单个 World2Mind 进程会串行处理重建与建图请求。因此，在训练和本地评估期间，作者把 World2Mind 部署为多进程 HTTP 服务。每个服务进程分配给独立 NPU worker，并初始化同一认知建图流水线，包括单目几何估计、SAM3 分割、语义点云构建、AST 生成和路线图渲染。主要配置并行启动 8 个 World2Mind worker，以支持并发工具执行。


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Within each worker, NPU-intensive depth estimation and segmentation are executed under a worker-level lock, while downstream mapping, AST construction, and route-map generation proceed after NPU computation and are controlled by CPU-side concurrency limits. This separation prevents concurrent rollouts from over-subscribing NPU memory while allowing lightweight mapping operations to proceed efficiently.


> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在每个 worker 内，NPU 密集的深度估计和分割在 worker 级锁下执行；下游建图、AST 构建和路线图生成在 NPU 计算完成后进行，并受 CPU 侧并发限制控制。这样的分离既防止并发 rollout 过度占用 NPU 内存，又让轻量建图操作能够高效执行。


> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Rollout and evaluation clients dispatch each cognitive_map request to an available World2Mind worker using a simple load-balancing strategy based on current in-flight requests. Failed or unavailable workers are skipped and requests are retried on another endpoint when possible. This service design improves throughput and tail-latency stability under concurrent rollout generation, while keeping the World2Mind reconstruction pipeline and AST semantics unchanged.


> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Rollout 与评估客户端根据当前在途请求，采用简单负载均衡策略，把每个 `cognitive_map` 请求分派到可用的 World2Mind worker。失败或不可用的 worker 会被跳过，并在可能时将请求重试到另一端点。该服务设计在并发 rollout 生成下改善吞吐量和尾延迟稳定性，同时保持 World2Mind 重建流水线与 AST 语义不变。


## Appendix C — Spatial Reasoning Harness Prompts


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The Spatial Reasoning Harness is implemented with three coupled components: a system message, a machine-readable tool interface, and a user-side reasoning protocol. For proprietary models, the tool interface is passed through function-calling schemas. For locally trained agents, the same interface is serialized as <tool_call> blocks containing a JSON object with name and arguments. Visual tokens are placed before the reasoning protocol, ensuring that the model observes the frames or multi-view images before receiving step-by-step instructions.


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Spatial Reasoning Harness 由三个耦合组件实现：系统消息、机器可读工具接口和用户侧推理协议。对于专有模型，工具接口通过函数调用 schema 传入；对于本地训练智能体，同一接口序列化为包含 `name` 和 `arguments` JSON 对象的 `<tool_call>` 块。视觉 token 放在推理协议之前，以确保模型先观察视频帧或多视图图像，再接收逐步指令。


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> System Message — Role. You are a spatial intelligence assistant that analyzes videos and images to answer spatial questions. Available tools: • world2mind: builds an allocentric cognitive map and returns per-instance spatial data, including coordinates, sizes, and object relations. • view_image: renders cognitive-map visualizations, including top-down landmark maps, route maps, semantic maps, and point-cloud views. Reliability note. The cognitive map is produced from monocular reconstruction and may contain missing objects, ghost instances, coordinate drift, or segmentation errors. Treat tool outputs as supplementary evidence rather than ground truth, and cross-validate them against direct visual observations before answering. Answer format. Wrap the final answer in <Answer></Answer> tags.


> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 系统消息——角色。你是一名空间智能助手，通过分析视频和图像回答空间问题。可用工具：• `world2mind`：构建非自我中心认知地图，并返回逐实例空间数据，包括坐标、尺寸和对象关系。• `view_image`：渲染认知地图可视化，包括俯视地标图、路线图、语义图和点云视图。可靠性说明。认知地图由单目重建生成，可能包含对象缺失、幽灵实例、坐标漂移或分割错误。应把工具输出视为补充证据而非真值，并在作答前与直接视觉观察交叉验证。答案格式。把最终答案包在 `<Answer></Answer>` 标签中。


> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Tool Interface — world2mind. Generate a query-conditioned cognitive map from the current visual input. The tool automatically analyzes the video frames or images already provided in the conversation; the model does not provide file paths. Returned knowledge: • Landmark knowledge (knowledge_type=landmark or both): detected instances, metric coordinates, footprint size, and object relations. • Route knowledge (knowledge_type=route or both): traversable regions, camera trajectory, and grid-based route information.


> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 工具接口——`world2mind`。从当前视觉输入生成以查询为条件的认知地图。工具自动分析对话中已经提供的视频帧或图像；模型不提供文件路径。返回知识：• 地标知识（`knowledge_type=landmark` 或 `both`）：检测到的实例、度量坐标、占地尺寸和对象关系。• 路线知识（`knowledge_type=route` 或 `both`）：可遍历区域、相机轨迹和基于栅格的路线信息。


### World2Mind parameter schema.

**Caption:** World2Mind parameter schema.

**Caption[CN]:** World2Mind 参数 schema。

| Parameter | Requirement | Meaning |
|---|---|---|
| `categories` | required; list of strings | Object categories to detect as landmarks, e.g., chair, table, door. |
| `scene_type` | required; `indoor` or `outdoor` | Selects scene-specific reconstruction settings. |
| `knowledge_type` | required; `landmark`, `route`, or `both` | Chooses landmark-only, route-only, or complete cognitive-map output. |
| `output_format` | required; `rectangle` or `ellipse` | Specifies the landmark footprint representation. |
| `traversable_categories` | required for `route` or `both` | Ground or surface categories used to infer passable regions, e.g., floor, carpet, road. |

**中文表格：**

| 参数 | 要求 | 含义 |
|---|---|---|
| `categories` | 必填；字符串列表 | 要作为地标检测的对象类别，例如 chair、table、door。 |
| `scene_type` | 必填；`indoor` 或 `outdoor` | 选择场景特定的重建设置。 |
| `knowledge_type` | 必填；`landmark`、`route` 或 `both` | 选择仅地标、仅路线或完整认知地图输出。 |
| `output_format` | 必填；`rectangle` 或 `ellipse` | 指定地标占地轮廓表征。 |
| `traversable_categories` | `route` 或 `both` 时必填 | 用于推断可通行区域的地面或表面类别，例如 floor、carpet、road。 |


> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> view_image. Inspect a visualization generated by the most recent world2mind call. The required parameter visualization_type must be selected from the available visualizations returned by world2mind, such as landmark_vis, route_vis, pointcloud_rgb_topdown, or pointcloud_semantic_topdown. The model should call view_image when the YAML output is ambiguous, when object layout requires visual verification, or when map evidence must be checked against raw observations.


> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> `view_image`。检查最近一次 `world2mind` 调用生成的可视化。必填参数 `visualization_type` 必须从 `world2mind` 返回的可用可视化中选择，例如 `landmark_vis`、`route_vis`、`pointcloud_rgb_topdown` 或 `pointcloud_semantic_topdown`。当 YAML 输出含混、对象布局需要视觉验证，或必须依据原始观察核验地图证据时，模型应调用 `view_image`。


> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Text-Form Tool Calls for Local Agents. For local SFT/GSPO agents, tool calls are serialized as text while preserving the same schema:


> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 本地智能体的文本形式工具调用。对于本地 SFT/GSPO 智能体，工具调用被序列化为文本，同时保留相同 schema：


> <span style="color:#3B82F6"><strong>Para. 6:</strong></span>
>
> ```text
<tool_call>
> {
>   "name": "world2mind",
>   "arguments": {
>     "categories": ["chair", "table", "door"],
>     "scene_type": "indoor",
>     "knowledge_type": "both",
>     "output_format": "rectangle",
>     "traversable_categories": ["floor", "carpet"]
>   }
> }
> </tool_call>
```


> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span>
>
> ```text
以下代码保持机器可读键和值不变：
> <tool_call>
> {
>   "name": "world2mind",
>   "arguments": {
>     "categories": ["chair", "table", "door"],
>     "scene_type": "indoor",
>     "knowledge_type": "both",
>     "output_format": "rectangle",
>     "traversable_categories": ["floor", "carpet"]
>   }
> }
> </tool_call>
```


> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> The schema requires categories, scene_type, knowledge_type, and output_format. Malformed calls are returned as tool-error messages when applicable and are not treated as valid spatial evidence.


> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 该 schema 要求提供 `categories`、`scene_type`、`knowledge_type` 和 `output_format`。格式错误的调用在适用时会以工具错误消息返回，并且不被视为有效空间证据。


> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> User-Side Reasoning Protocol. Visual tokens. The video frames or multi-view images are placed before the textual instructions. Step 1: Visual Clues. Describe concrete visual observations before any tool call, including visible objects, relative positions, spatial relations, and a preliminary answer when possible. Step 2.1: world2mind Tool Call. Call world2mind only when the question requires information that vision alone cannot reliably provide, such as metric distance, 3D coordinates, route layout, viewpoint transformation, or complex spatial relations. Step 2.2: Map Clues. If world2mind is called, summarize map evidence only: detected instances, coordinates, sizes, containment relations, route cells, trajectories, or camera orientations. Do not reconcile it with visual clues yet. Step 3.1: view_image Tool Call. If the structured map is ambiguous or layout verification is needed, call view_image using one of the available visualization types returned by world2mind. Step 3.2: Visualization Clues. Describe the rendered cognitive-map visualization, such as top-down layout, object arrangement, route trajectory, or conflicts with the raw visual input. Step 4: Cross-Validation. Compare visual evidence, map evidence, and visualization evidence. Identify conflicts caused by reconstruction drift, missing objects, false detections, or visual ambiguity, and decide which evidence should dominate. Step 5: Final Answer. Integrate the validated evidence and provide the conclusion. For single-word, numeric, or option questions, place only the final value inside the answer tag. Question. {query}


> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 用户侧推理协议。视觉 token：视频帧或多视图图像放在文本指令之前。步骤 1：视觉线索。在任何工具调用之前描述具体视觉观察，包括可见对象、相对位置、空间关系，并在可能时给出初步答案。步骤 2.1：`world2mind` 工具调用。仅当问题需要视觉单独无法可靠提供的信息时调用 `world2mind`，例如度量距离、三维坐标、路线布局、视角变换或复杂空间关系。步骤 2.2：地图线索。若调用 `world2mind`，只总结地图证据：检测到的实例、坐标、尺寸、包含关系、路线单元、轨迹或相机方向；此时不要与视觉线索调和。步骤 3.1：`view_image` 工具调用。若结构化地图含混或需要验证布局，则使用 `world2mind` 返回的某种可用可视化类型调用 `view_image`。步骤 3.2：可视化线索。描述渲染后的认知地图可视化，例如俯视布局、对象排列、路线轨迹，或它与原始视觉输入的冲突。步骤 4：交叉验证。比较视觉证据、地图证据和可视化证据；识别由重建漂移、对象缺失、误检或视觉含混造成的冲突，并判断哪类证据应占主导。步骤 5：最终答案。整合经过验证的证据并给出结论。对于单词、数值或选项问题，只在答案标签内放置最终值。问题：`{query}`。


## Appendix D — Case Analysis


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> D.1 Case 1: Metric Closest-Point Reasoning


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> D.1 案例 1：度量最近点推理


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> User Turn: Input Observation and Query. Observation. The input is a video of a kitchen. Eight approximately uniformly sampled frames are shown below as a two-row, four-column contact sheet. Question. Determine the shortest distance between the towel and the refrigerator in meters. Please answer using a single word or phrase.


> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 用户轮次：输入观察与查询。观察：输入是一段厨房视频。下方以两行四列的接触表展示 8 个近似均匀采样的帧。问题：确定毛巾与冰箱之间的最短距离，单位为米。请用一个词或短语作答。


### Appendix D.1 input

![Kitchen video contact sheet for towel-to-refrigerator distance case](appendix_case1_input.png)

**Caption:** Appendix D.1 input: eight uniformly sampled kitchen frames and the closest-distance query.

**Caption[CN]:** 附录 D.1 输入：8 个均匀采样的厨房帧与最近距离查询。


> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Assistant Turn 1: Visual Clues and World2Mind Call. Visual clues. The model first observes a green patterned towel hanging on the oven door and a white refrigerator in other frames. Because the two objects are not visible in a single calibrated view, it estimates that direct visual inspection is insufficient for precise metric distance. Tool call:


> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 助手轮次 1：视觉线索与 World2Mind 调用。视觉线索：模型先在部分帧中观察到挂在烤箱门上的绿色花纹毛巾，在其他帧中观察到白色冰箱。由于两个对象没有同时出现在一个经过标定的视图中，模型判断直接视觉检查不足以提供精确度量距离。工具调用：


> <span style="color:#3B82F6"><strong>Para. 4:</strong></span>
>
> ```text
<tool_call>
> {
>   "name": "world2mind",
>   "arguments": {
>     "categories": ["towel", "refrigerator", "stove", "oven"],
>     "knowledge_type": "landmark",
>     "output_format": "rectangle",
>     "scene_type": "indoor",
>     "traversable_categories": ["floor"]
>   }
> }
> </tool_call>
```


> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span>
>
> ```text
机器可读调用保持原样；其含义是请求室内场景中 towel、refrigerator、stove、oven 的矩形地标地图，并把 floor 指定为可遍历类别：
> <tool_call>
> {
>   "name": "world2mind",
>   "arguments": {
>     "categories": ["towel", "refrigerator", "stove", "oven"],
>     "knowledge_type": "landmark",
>     "output_format": "rectangle",
>     "scene_type": "indoor",
>     "traversable_categories": ["floor"]
>   }
> }
> </tool_call>
```


> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Tool Result 1: World2Mind Landmark AST. World2Mind returns a JSON tool result with success=true, scene id scene0220_01_c70da29e-5e7, available visualization landmark_vis, and the following AST in the landmark_yaml field.


> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 工具结果 1：World2Mind 地标 AST。World2Mind 返回一个 JSON 工具结果，其中 `success=true`，场景 ID 为 `scene0220_01_c70da29e-5e7`，可用可视化为 `landmark_vis`，并在 `landmark_yaml` 字段给出以下 AST。


> <span style="color:#3B82F6"><strong>Para. 6:</strong></span>
>
> ```text
Map_Metadata:
>   Coordinate_System: 2D Absolute Grid (meters)
>   Origin_Ref: (-3.129, -1.293)
>   AST_Format: Rectangle (center, width, height)
> Spatial_Hierarchy:
> - Node_ID: floor_01
>   Spatial_Pose:
>     Center: (-0.087, 1.449)
>     Width: 4.117
>     Height: 2.838
>   Attributes:
>     Height_Range: (1.179, 1.585)
>     Area_m2: 7.1149
>     Point_Count: 15383
> - Node_ID: refrigerator_01
>   Spatial_Pose:
>     Center: (0.474, 1.475)
>     Width: 0.924
>     Height: 0.866
>   Attributes:
>     Height_Range: (-0.234, 1.525)
>     Area_m2: 0.5815
>     Point_Count: 2674
> - Node_ID: stove_01
>   Spatial_Pose:
>     Center: (2.106, 0.691)
>     Width: 0.65
>     Height: 0.731
>   Attributes:
>     Height_Range: (0.554, 1.585)
>     Area_m2: 0.4324
>     Point_Count: 3588
>   Contains_Children:
>   - Node_ID: towel_01
>     Spatial_Pose:
>       Center: (1.918, 0.634)
>       Width: 0.052
>       Height: 0.304
>     Attributes:
>       Height_Range: (0.839, 1.207)
>       Area_m2: 0.0102
>       Point_Count: 1136
>     Relation_To_Parent: Inside
```


> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span>
>
> ```text
以下 AST 保留全部机器可读键和数值。它表示二维绝对米制栅格：floor_01、refrigerator_01 和 stove_01 的中心、宽高、高度范围、面积与点数；towel_01 是 stove_01 的 Inside 子节点：
> Map_Metadata:
>   Coordinate_System: 2D Absolute Grid (meters)
>   Origin_Ref: (-3.129, -1.293)
>   AST_Format: Rectangle (center, width, height)
> Spatial_Hierarchy:
> - Node_ID: floor_01
>   Spatial_Pose:
>     Center: (-0.087, 1.449)
>     Width: 4.117
>     Height: 2.838
>   Attributes:
>     Height_Range: (1.179, 1.585)
>     Area_m2: 7.1149
>     Point_Count: 15383
> - Node_ID: refrigerator_01
>   Spatial_Pose:
>     Center: (0.474, 1.475)
>     Width: 0.924
>     Height: 0.866
>   Attributes:
>     Height_Range: (-0.234, 1.525)
>     Area_m2: 0.5815
>     Point_Count: 2674
> - Node_ID: stove_01
>   Spatial_Pose:
>     Center: (2.106, 0.691)
>     Width: 0.65
>     Height: 0.731
>   Attributes:
>     Height_Range: (0.554, 1.585)
>     Area_m2: 0.4324
>     Point_Count: 3588
>   Contains_Children:
>   - Node_ID: towel_01
>     Spatial_Pose:
>       Center: (1.918, 0.634)
>       Width: 0.052
>       Height: 0.304
>     Attributes:
>       Height_Range: (0.839, 1.207)
>       Area_m2: 0.0102
>       Point_Count: 1136
>     Relation_To_Parent: Inside
```


> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Assistant Turn 2: Map Calculation and Visualization Request. Map clues. The model reads towel_01 center (1.918, 0.634) m and refrigerator_01 center (0.474, 1.475) m. The center-to-center distance is about 1.671 m, but the question asks for nearest-point distance. Using rectangle half-extents, the horizontal gap is 1.444 − (0.026 + 0.462) = 0.956 m and the vertical gap is 0.841 − (0.152 + 0.433) = 0.256 m. The nearest-boundary distance is therefore √(0.956² + 0.256²) ≈ 0.990 m. Visualization request. The trajectory then requests a map visualization to verify the geometric layout before finalizing the answer.


> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 助手轮次 2：地图计算与可视化请求。地图线索：模型读取到 `towel_01` 中心为 $(1.918,0.634)$ m，`refrigerator_01` 中心为 $(0.474,1.475)$ m。中心到中心距离约 1.671 m，但问题询问最近点距离。利用矩形半尺寸，水平间隙为 $1.444-(0.026+0.462)=0.956$ m，垂直间隙为 $0.841-(0.152+0.433)=0.256$ m。因此最近边界距离为 $\sqrt{0.956^2+0.256^2}\approx0.990$ m。可视化请求：轨迹随后请求地图可视化，在最终作答前核验几何布局。


> <span style="color:#3B82F6"><strong>Para. 8:</strong></span>
>
> ```text
<tool_call>
> {
>   "name": "view_image",
>   "arguments": {"visualization_type": "landmark_vis"}
> }
> </tool_call>
```


> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span>
>
> ```text
调用 `view_image` 检查 `landmark_vis`；机器可读代码保持原样：
> <tool_call>
> {
>   "name": "view_image",
>   "arguments": {"visualization_type": "landmark_vis"}
> }
> </tool_call>
```


> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Tool Result 2: Landmark Visualization. The returned landmark_vis image provides a top-down check of the refrigerator and stove/towel layout.


> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 工具结果 2：地标可视化。返回的 `landmark_vis` 图像从俯视角度核验冰箱与炉灶/毛巾的布局。


### Appendix D.1 landmark visualization

![Top-down landmark map for case 1](appendix_case1_map.png)

**Caption:** Appendix D.1 landmark visualization: top-down refrigerator and stove/towel layout.

**Caption[CN]:** 附录 D.1 地标可视化：冰箱与炉灶/毛巾的俯视布局。


> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> Assistant Turn 3: Cross-Validation, Final Answer, and Ground Truth. Visualization clues. The top-down landmark visualization places the refrigerator and stove/towel on different sides of the kitchen, with a gap consistent with the rectangle-derived estimate. Cross-validation. The raw visual evidence suggests a short, plausible kitchen-scale separation, and the map does not introduce a visible contradiction. The agent therefore trusts the AST-derived nearest-point estimate. Final answer. Prediction: <Answer>0.99 m</Answer>. Ground truth (VSI): 1.1 m. Absolute error: 0.11 m.


> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 助手轮次 3：交叉验证、最终答案与真值。可视化线索：俯视地标图把冰箱和炉灶/毛巾放在厨房两侧，间隙与矩形推导的估计一致。交叉验证：原始视觉证据表明两者间隔较短，符合厨房尺度；地图没有引入可见矛盾。因此，智能体信任由 AST 推导的最近点估计。最终答案：预测 `<Answer>0.99 m</Answer>`；VSI 真值 1.1 m；绝对误差 0.11 m。


> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> D.2 Case 2: Viewpoint-Conditioned Navigation


> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> D.2 案例 2：以视角为条件的导航


> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> User Turn: Input Observations and Query. Observation. The input consists of four wall-aligned views of the same black chair: front, left, back, and right. Question. If the observer stands at the same spot and faces the same direction as image 4, then turns left and moves forward, will the observer get closer to the grey sofa? A. No. B. Yes.


> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 用户轮次：输入观察与查询。观察：输入包含同一把黑色椅子的四个沿墙对齐视图：正面、左侧、背面和右侧。问题：如果观察者站在与图像 4 相同的位置并朝向相同方向，然后左转并前进，观察者是否会更接近灰色沙发？A. 否。B. 是。


### Appendix D.2 input

![Four chair views for viewpoint-conditioned navigation](appendix_case2_input.png)

**Caption:** Appendix D.2 input: four wall-aligned views of the black chair.

**Caption[CN]:** 附录 D.2 输入：黑色椅子的四个沿墙对齐视图。


> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> Assistant Turn 1: Visual Clues and World2Mind Call. Visual clues. The model identifies image 1 as the front view of the chair, image 2 as the left view, image 3 as the back view, and image 4 as the right view. The grey sofa is clearly visible in image 3. From image 4, turning left appears to rotate the observer toward the direction where the sofa may lie, but the view transformation is ambiguous enough to benefit from an allocentric map.


> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> 助手轮次 1：视觉线索与 World2Mind 调用。视觉线索：模型把图像 1 识别为椅子正视图，图像 2 为左视图，图像 3 为后视图，图像 4 为右视图。灰色沙发在图像 3 中清晰可见。从图像 4 看，左转似乎会让观察者朝向沙发可能所在的方向，但该视角变换足够含混，因此可从非自我中心地图受益。


> <span style="color:#3B82F6"><strong>Para. 14:</strong></span>
>
> ```text
<tool_call>
> {
>   "name": "world2mind",
>   "arguments": {
>     "categories": ["black chair", "grey sofa", "desk", "plant", "bag", "window"],
>     "knowledge_type": "both",
>     "output_format": "rectangle",
>     "scene_type": "indoor",
>     "traversable_categories": ["floor", "carpet", "tile flooring"]
>   }
> }
> </tool_call>
```


> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span>
>
> ```text
机器可读调用保持原样；它请求室内场景中 black chair、grey sofa、desk、plant、bag、window 的矩形地标与路线知识，并把 floor、carpet、tile flooring 指定为可遍历类别：
> <tool_call>
> {
>   "name": "world2mind",
>   "arguments": {
>     "categories": ["black chair", "grey sofa", "desk", "plant", "bag", "window"],
>     "knowledge_type": "both",
>     "output_format": "rectangle",
>     "scene_type": "indoor",
>     "traversable_categories": ["floor", "carpet", "tile flooring"]
>   }
> }
> </tool_call>
```


> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> Tool Result 1: World2Mind AST and Route Knowledge. World2Mind returns both landmark and route knowledge for scene images_4_816b9d06-732. The complete AST and route fields are shown below.


> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> 工具结果 1：World2Mind AST 与路线知识。World2Mind 为场景 `images_4_816b9d06-732` 同时返回地标与路线知识。完整 AST 和路线字段如下。


> <span style="color:#3B82F6"><strong>Para. 16:</strong></span>
>
> ```text
AST.
> Map_Metadata:
>   Coordinate_System: 2D Absolute Grid (meters)
>   Origin_Ref: (-2.281, -0.401)
>   AST_Format: Rectangle (center, width, height)
>   Camera_Views:
>   - Frame: frame_000000
>     Image: image 1
>     Position: (-0.975, 0.668)
>     Heading_Deg: 56.2
>   - Frame: frame_000001
>     Image: image 2
>     Position: (0.921, 0.676)
>     Heading_Deg: -57.6
>   - Frame: frame_000002
>     Image: image 3
>     Position: (-0.0, 0.0)
>     Heading_Deg: 0.3
>   - Frame: frame_000003
>     Image: image 4
>     Position: (-0.17, 1.443)
>     Heading_Deg: 161.8
> Spatial_Hierarchy:
> - Node_ID: grey sofa_01
>   Spatial_Pose:
>     Center: (1.524, 1.234)
>     Width: 0.708
>     Height: 1.022
>   Attributes:
>     Height_Range: (-0.654, 0.881)
>     Area_m2: 0.4026
>     Point_Count: 640
> - Node_ID: black chair_01
>   Spatial_Pose:
>     Center: (-0.077, 1.314)
>     Width: 0.532
>     Height: 0.333
>   Attributes:
>     Height_Range: (-0.529, 0.49)
>     Area_m2: 0.1173
>     Point_Count: 2911
> - Node_ID: bag_01
>   Spatial_Pose:
>     Center: (0.32, 1.278)
>     Width: 0.412
>     Height: 0.185
>   Attributes:
>     Height_Range: (0.311, 0.672)
>     Area_m2: 0.0523
>     Point_Count: 296
> - Node_ID: plant_01
>   Spatial_Pose:
>     Center: (0.214, 1.863)
>     Width: 0.307
>     Height: 0.22
>   Attributes:
>     Height_Range: (-0.187, 0.221)
>     Area_m2: 0.0419
>     Point_Count: 516
```


> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span>
>
> ```text
以下 AST 保留全部机器可读键与数值。它记录四个相机视图的坐标与朝向，并给出 grey sofa_01、black chair_01、bag_01、plant_01 的中心、宽高、高度范围、面积和点数：
> AST.
> Map_Metadata:
>   Coordinate_System: 2D Absolute Grid (meters)
>   Origin_Ref: (-2.281, -0.401)
>   AST_Format: Rectangle (center, width, height)
>   Camera_Views:
>   - Frame: frame_000000
>     Image: image 1
>     Position: (-0.975, 0.668)
>     Heading_Deg: 56.2
>   - Frame: frame_000001
>     Image: image 2
>     Position: (0.921, 0.676)
>     Heading_Deg: -57.6
>   - Frame: frame_000002
>     Image: image 3
>     Position: (-0.0, 0.0)
>     Heading_Deg: 0.3
>   - Frame: frame_000003
>     Image: image 4
>     Position: (-0.17, 1.443)
>     Heading_Deg: 161.8
> Spatial_Hierarchy:
> - Node_ID: grey sofa_01
>   Spatial_Pose:
>     Center: (1.524, 1.234)
>     Width: 0.708
>     Height: 1.022
>   Attributes:
>     Height_Range: (-0.654, 0.881)
>     Area_m2: 0.4026
>     Point_Count: 640
> - Node_ID: black chair_01
>   Spatial_Pose:
>     Center: (-0.077, 1.314)
>     Width: 0.532
>     Height: 0.333
>   Attributes:
>     Height_Range: (-0.529, 0.49)
>     Area_m2: 0.1173
>     Point_Count: 2911
> - Node_ID: bag_01
>   Spatial_Pose:
>     Center: (0.32, 1.278)
>     Width: 0.412
>     Height: 0.185
>   Attributes:
>     Height_Range: (0.311, 0.672)
>     Area_m2: 0.0523
>     Point_Count: 296
> - Node_ID: plant_01
>   Spatial_Pose:
>     Center: (0.214, 1.863)
>     Width: 0.307
>     Height: 0.22
>   Attributes:
>     Height_Range: (-0.187, 0.221)
>     Area_m2: 0.0419
>     Point_Count: 516
```


> <span style="color:#3B82F6"><strong>Para. 17:</strong></span>
>
> ```text
Route knowledge.
> Route_Knowledge_Metadata:
>   Coordinate_System: Grid (NxN cells)
>   Grid_Divisions: 10
>   Cell_Size: (0.474, 0.427)
>   Scene_Bounds:
>     Min: (-2.281, -0.401)
>     Max: (2.458, 3.865)
>   Total_Traversable_Cells: 32
>   Estimated_Floor_Area_m2: 6.47
>   Trajectory_Length: 4
>   Note: Estimated_Floor_Area_m2 is the traversable floor area only. Actual room area approximately Floor_Area + furniture footprint area. Do NOT use Scene_Bounds to calculate room area -- Scene_Bounds is the axis-aligned bounding box of the entire 3D reconstruction and always significantly overestimates room size.
>   Description: Route knowledge map showing traversable areas and camera movement path
>   Scene: images_4_816b9d06-732
> Traversable_Grid:
> - (0, 3)
> - (1, 3)
> - (1, 4)
> - (1, 6)
> - (1, 7)
> - (1, 8)
> - (2, 3)
> - (2, 6)
> - (2, 7)
> - (3, 2)
> - (3, 3)
> - (3, 4)
> - (3, 5)
> - (3, 6)
> - (3, 7)
> - (4, 2)
> - (4, 3)
> - (4, 4)
> - (4, 5)
> - (4, 6)
> - (4, 7)
> - (5, 3)
> - (5, 4)
> - (5, 5)
> - (5, 6)
> - (6, 3)
> - (6, 4)
> - (6, 5)
> - (6, 6)
> - (7, 3)
> - (7, 5)
> - (7, 6)
> Camera_Trajectory: (2, 2) --> (2, 6) --> (0, 4) --> (4, 4)
> Camera_Orientations:
> - Frame: frame_000000
>   Image: image 1
>   Position: (-0.975, 0.668)
>   Heading_Deg: 56.2
> - Frame: frame_000001
>   Image: image 2
>   Position: (0.921, 0.676)
>   Heading_Deg: -57.6
> - Frame: frame_000002
>   Image: image 3
>   Position: (-0.0, 0.0)
>   Heading_Deg: 0.3
> - Frame: frame_000003
>   Image: image 4
>   Position: (-0.17, 1.443)
>   Heading_Deg: 161.8
```


> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span>
>
> ```text
以下路线知识完整保留原机器可读字段、32 个可遍历栅格单元、相机轨迹与四帧相机朝向。说明字段强调：`Estimated_Floor_Area_m2` 只表示可遍历地面面积；实际房间面积约等于地面面积加家具占地面积；不得使用 `Scene_Bounds` 计算房间面积，因为它是整个三维重建的轴对齐包围盒，会显著高估房间尺寸。
> Route knowledge.
> Route_Knowledge_Metadata:
>   Coordinate_System: Grid (NxN cells)
>   Grid_Divisions: 10
>   Cell_Size: (0.474, 0.427)
>   Scene_Bounds:
>     Min: (-2.281, -0.401)
>     Max: (2.458, 3.865)
>   Total_Traversable_Cells: 32
>   Estimated_Floor_Area_m2: 6.47
>   Trajectory_Length: 4
>   Note: Estimated_Floor_Area_m2 is the traversable floor area only. Actual room area approximately Floor_Area + furniture footprint area. Do NOT use Scene_Bounds to calculate room area -- Scene_Bounds is the axis-aligned bounding box of the entire 3D reconstruction and always significantly overestimates room size.
>   Description: Route knowledge map showing traversable areas and camera movement path
>   Scene: images_4_816b9d06-732
> Traversable_Grid:
> - (0, 3)
> - (1, 3)
> - (1, 4)
> - (1, 6)
> - (1, 7)
> - (1, 8)
> - (2, 3)
> - (2, 6)
> - (2, 7)
> - (3, 2)
> - (3, 3)
> - (3, 4)
> - (3, 5)
> - (3, 6)
> - (3, 7)
> - (4, 2)
> - (4, 3)
> - (4, 4)
> - (4, 5)
> - (4, 6)
> - (4, 7)
> - (5, 3)
> - (5, 4)
> - (5, 5)
> - (5, 6)
> - (6, 3)
> - (6, 4)
> - (6, 5)
> - (6, 6)
> - (7, 3)
> - (7, 5)
> - (7, 6)
> Camera_Trajectory: (2, 2) --> (2, 6) --> (0, 4) --> (4, 4)
> Camera_Orientations:
> - Frame: frame_000000
>   Image: image 1
>   Position: (-0.975, 0.668)
>   Heading_Deg: 56.2
> - Frame: frame_000001
>   Image: image 2
>   Position: (0.921, 0.676)
>   Heading_Deg: -57.6
> - Frame: frame_000002
>   Image: image 3
>   Position: (-0.0, 0.0)
>   Heading_Deg: 0.3
> - Frame: frame_000003
>   Image: image 4
>   Position: (-0.17, 1.443)
>   Heading_Deg: 161.8
```


> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> Assistant Turn 2: Map Clues and View-Image Call. Map clues. The map places the grey sofa at (1.524, 1.234) and the black chair at (−0.077, 1.314). Image 4 has camera position (−0.170, 1.443) and heading 161.8°. Turning left changes the heading to approximately 71.8°, which points toward increasing x. Since the sofa has a much larger x coordinate than the image-4 camera, moving forward after the left turn should reduce the distance to the sofa.


> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> 助手轮次 2：地图线索与查看图像调用。地图线索：地图把灰色沙发置于 $(1.524,1.234)$，黑色椅子置于 $(-0.077,1.314)$。图像 4 的相机位置为 $(-0.170,1.443)$，朝向 161.8°。左转后朝向约变为 71.8°，指向 $x$ 增大的方向。由于沙发的 $x$ 坐标远大于图像 4 相机的 $x$ 坐标，左转后前进应缩短与沙发的距离。


> <span style="color:#3B82F6"><strong>Para. 19:</strong></span>
>
> ```text
<tool_call>
> {
>   "name": "view_image",
>   "arguments": {"visualization_type": "landmark_vis"}
> }
> </tool_call>
```


> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span>
>
> ```text
调用 `view_image` 查看 `landmark_vis`；机器可读代码保持原样：
> <tool_call>
> {
>   "name": "view_image",
>   "arguments": {"visualization_type": "landmark_vis"}
> }
> </tool_call>
```


> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> Tool Result 2: Landmark Visualization. The returned landmark visualization provides an explicit top-down check of the chair, sofa, and image-4 camera pose.


> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> 工具结果 2：地标可视化。返回的地标可视化从俯视角度明确核验椅子、沙发与图像 4 相机姿态。


### Appendix D.2 landmark visualization

![Top-down landmark map for case 2](appendix_case2_map.png)

**Caption:** Appendix D.2 landmark visualization: chair, sofa, and image-4 camera pose.

**Caption[CN]:** 附录 D.2 地标可视化：椅子、沙发与图像 4 相机姿态。


> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> Assistant Turn 3: Visualization Clues, Cross-Validation, Final Answer, and Ground Truth. Visualization clues. The map shows the black chair near the center and the grey sofa to the right/east of the image-4 camera position. This agrees with the coordinate-level reading. Cross-validation. Visual evidence from image 3 shows the sofa behind the chair, while image 4 is the right-side view. The map evidence shows that a left turn from heading 161.8° points approximately toward heading 71.8°, which moves toward the sofa’s larger x coordinate. The visual and allocentric cues therefore agree. Final answer. Prediction: <Answer>B</Answer>. Ground truth (MindCube): B (Yes).


> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> 助手轮次 3：可视化线索、交叉验证、最终答案与真值。可视化线索：地图显示黑色椅子靠近中心，灰色沙发位于图像 4 相机位置的右侧/东侧，这与坐标级解读一致。交叉验证：图像 3 的视觉证据显示沙发位于椅子后方，而图像 4 是右侧视图。地图证据表明，从朝向 161.8° 左转后大致指向 71.8°，会朝沙发更大的 $x$ 坐标移动。因此，视觉与非自我中心线索一致。最终答案：预测 `<Answer>B</Answer>`；MindCube 真值为 B（是）。


## Appendix E — Computational Costs in Training and Inference


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Training cost. In our setup, both AlloSpatial-4B and AlloSpatial-8B are trained on 8 HUAWEI Ascend 910B NPUs, taking approximately 60 and 40 NPU-hours, respectively, to reach the reported checkpoints. The 4B and 8B agents use 4 and 6 trainer processes, respectively. Around the reported checkpoints, one GSPO update typically takes 4–6 minutes, including multi-turn rollout generation, live World2Mind execution, reward computation, and policy optimization. The exact update time varies with the tool-use rate, the number of sampled World2Mind calls, and the reconstruction difficulty of each rollout batch.


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 训练成本。在作者的设置中，AlloSpatial-4B 与 AlloSpatial-8B 均使用 8 个 HUAWEI Ascend 910B NPU 训练，到达所报告检查点分别约需 60 和 40 NPU 小时。4B 与 8B 智能体分别使用 4 个和 6 个训练进程。在所报告检查点附近，一次 GSPO 更新通常耗时 4–6 分钟，其中包括多轮 rollout 生成、实时 World2Mind 执行、奖励计算和策略优化。确切更新时间随工具使用率、采样的 World2Mind 调用数量和每个 rollout 批次的重建难度而变化。


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Inference cost. Inference cost is determined primarily by the number of input frames and the number of World2Mind calls. Each AlloSpatial query may involve multiple reasoning turns, and each valid World2Mind call can trigger depth and pose estimation, segmentation, semantic alignment, AST construction, and optional route-map rendering. With the parallel World2Mind service, VSI-Bench-tiny evaluation takes roughly 12 minutes for 392 questions with concurrent evaluation and 8 World2Mind workers.


> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 推理成本。推理成本主要由输入帧数和 World2Mind 调用次数决定。每个 AlloSpatial 查询可能涉及多轮推理；每次有效 World2Mind 调用都可能触发深度与姿态估计、分割、语义对齐、AST 构建以及可选路线图渲染。使用并行 World2Mind 服务，在并发评估与 8 个 World2Mind worker 的条件下，对 VSI-Bench-tiny 的 392 个问题完成评估约需 12 分钟。


## NeurIPS Paper Checklist


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The checklist is designed to encourage best practices for responsible machine learning research, addressing issues of reproducibility, transparency, research ethics, and societal impact. Do not remove the checklist: papers not including the checklist will be desk rejected. The checklist should follow the references and the optional supplemental material and does not count toward the page limit.


> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 该清单旨在鼓励负责任机器学习研究的最佳实践，处理可复现性、透明度、研究伦理和社会影响等问题。请勿删除清单：不含清单的论文将被直接拒稿。清单应放在参考文献和可选补充材料之后，并且不计入页数限制。


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Please read the checklist guidelines carefully. For each question: • Answer [Yes], [No], or [N/A]. • [N/A] means the question is not applicable to this paper or the relevant information is not available. • Provide a short 1–2 sentence justification immediately after the answer, including for [N/A].


> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 请仔细阅读清单指南。对每个问题：• 回答 [Yes]、[No] 或 [N/A]。• [N/A] 表示该问题不适用于本文，或相关信息不可获得。• 在答案后立即给出 1–2 句简短理由，包括选择 [N/A] 时。


> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The checklist answers are an integral part of the paper submission. They are visible to reviewers, area chairs, senior area chairs, and ethics reviewers. Authors will also include it after revisions in the final paper, and its final version will be published with the paper. Reviewers will use the checklist as one factor in evaluation. Although [Yes] is generally preferable to [No], [No] is acceptable with proper justification. In general, [No] or [N/A] is not grounds for rejection. The true answer is often nuanced, so authors should use their best judgment and elaborate in the justification. Supporting evidence may appear in the main paper or appendix. A [Yes] justification should point to the relevant sections.


> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 清单答案是论文投稿不可分割的一部分，审稿人、领域主席、高级领域主席和伦理审稿人都能看到。作者还需在最终修订后把清单纳入论文，最终版本会与论文一同发表。审稿人会把清单作为评价因素之一。虽然通常 [Yes] 优于 [No]，但只要理由充分，回答 [No] 完全可以接受。一般而言，[No] 或 [N/A] 并不构成拒稿理由。真实答案往往更细腻，因此作者应使用最佳判断并在理由中展开说明。支持证据可出现在正文或附录中；回答 [Yes] 时，理由应指出相关章节。


> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> IMPORTANT: • Delete this instruction block, but keep the section heading “NeurIPS Paper Checklist”. • Keep the checklist subsection headings, questions/answers, and guidelines below. • Do not modify the questions and only use the provided macros for answers.


> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 重要：• 删除本说明块，但保留“NeurIPS Paper Checklist”章节标题。• 保留下方清单的小节标题、问题/答案与指南。• 不得修改问题，并且只能使用所提供的宏作答。


> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> 1. Claims. Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope? Answer: [Yes]. Justification: The abstract and introduction state the paper’s main contributions: AlloSpatial, World2Mind, the Spatial Reasoning Harness, and the RL-based internalization into open-weight agents. The claims are supported by evaluations on VSI-Bench and MindCube, including training-free proprietary-model results, trained Qwen3-VL-based agents, ablations, and limitations. Guidelines: • The answer [N/A] means that the abstract and introduction do not include the claims made in the paper. • The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A [No] or [N/A] answer to this question will not be perceived well by the reviewers. • The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings. • It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper.


> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 1. Claims。问题：摘要和引言中的主要主张是否准确反映论文的贡献与范围？答案：[Yes]。理由：摘要和引言陈述论文的主要贡献：AlloSpatial、World2Mind、Spatial Reasoning Harness，以及基于 RL 把该过程内化到开放权重智能体。VSI-Bench 和 MindCube 上的评估支持这些主张，其中包括免训练专有模型结果、训练后的 Qwen3-VL 智能体、消融和局限。指南：• [N/A] 表示摘要和引言不包含论文提出的主张。• 摘要和/或引言应清楚陈述论文主张，包括论文贡献及重要假设与局限。审稿人不会很好地看待对本题回答 [No] 或 [N/A]。• 提出的主张应与理论和实验结果匹配，并反映结果可以在多大程度上泛化到其他设置。• 可以把愿景目标作为动机，只要明确说明论文尚未实现这些目标。


> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> 2. Limitations. Question: Does the paper discuss the limitations of the work performed by the authors? Answer: [Yes]. Justification: The paper discusses limitations in the Conclusion and Limitations section, especially the remaining weakness on fine-grained numerical spatial reasoning due to reconstruction drift and imperfect metric calibration. The appendix also reports computational costs and implementation constraints of online World2Mind execution. Guidelines: • The answer [N/A] means that the paper has no limitation while the answer [No] means that the paper has limitations, but those are not discussed in the paper. • The authors are encouraged to create a separate “Limitations” section in their paper. • The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be. • The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated. • The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon. • The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size. • If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness. • While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations.


> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 2. Limitations。问题：论文是否讨论作者所开展工作的局限？答案：[Yes]。理由：论文在“结论与局限”中讨论局限，尤其指出重建漂移和不完善的度量校准使细粒度数值空间推理仍较弱。附录还报告在线执行 World2Mind 的计算成本和实现约束。指南：• [N/A] 表示论文没有局限；[No] 表示论文存在局限，但未在文中讨论。• 鼓励作者在论文中单设“Limitations”章节。• 论文应指出任何强假设，以及结果在违反这些假设时的稳健性（例如独立性假设、无噪声设置、模型设定正确、只在局部成立的渐近近似）。作者应反思这些假设在实践中可能如何被违反，以及会产生什么影响。• 作者应反思主张范围，例如方法是否只在少量数据集或少数运行上测试。一般而言，经验结果常依赖应被明确说明的隐含假设。• 作者应反思影响方法表现的因素。例如，面部识别算法可能在图像分辨率低或低光照拍摄时表现不佳；语音转文字系统可能因无法处理技术术语，而不能可靠地为在线讲座提供闭字幕。• 作者应讨论所提算法的计算效率以及随数据集规模的扩展方式。• 在适用时，作者应讨论其方法在处理隐私与公平问题上的可能局限。• 作者可能担心完全坦诚地说明局限会被审稿人当作拒稿理由，但更糟的情况是审稿人发现论文未承认的局限。作者应作出最佳判断，并认识到支持透明度的个人行动对形成维护共同体诚信的规范很重要。审稿人会被特别要求不得因作者诚实说明局限而进行惩罚。


> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> 3. Theory assumptions and proofs. Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof? Answer: [N/A]. Justification: The paper does not present theoretical theorems or formal proofs. Guidelines: • The answer [N/A] means that the paper does not include theoretical results. • All the theorems, formulas, and proofs in the paper should be numbered and cross-referenced. • All assumptions should be clearly stated or referenced in the statement of any theorems. • The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition. • Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material. • Theorems and Lemmas that the proof relies upon should be properly referenced.


> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 3. Theory assumptions and proofs。问题：对每项理论结果，论文是否给出完整假设集合以及完整且正确的证明？答案：[N/A]。理由：论文没有提出理论定理或形式证明。指南：• [N/A] 表示论文不含理论结果。• 论文中的所有定理、公式和证明均应编号并交叉引用。• 所有假设都应在任何定理陈述中清楚说明或引用。• 证明可以出现在正文或补充材料中；若在补充材料中，鼓励作者在正文给出简短证明概要以提供直觉。• 反过来，正文中的任何非形式证明都应由附录或补充材料中的形式证明补足。• 证明所依赖的定理与引理应得到恰当引用。


> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> 4. Experimental result reproducibility. Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)? Answer: [Yes]. Justification: The paper describes the benchmarks, data splits, metrics, frame-sampling protocols, baselines, training stages, reward design, evaluation settings, prompt format, and World2Mind service configuration. Additional hyperparameters, computational costs, and case analyses are provided in the appendix. Guidelines: • The answer [N/A] means that the paper does not include experiments. • If the paper includes experiments, a [No] answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not. • If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable. • Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general, releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed. • While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example: (a) If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm. (b) If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully. (c) If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset). (d) We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results.


> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 4. Experimental result reproducibility。问题：无论是否提供代码和数据，论文是否充分披露了在影响主要主张和/或结论的范围内复现主要实验结果所需的全部信息？答案：[Yes]。理由：论文描述基准、数据划分、指标、帧采样协议、基线、训练阶段、奖励设计、评估设置、提示格式和 World2Mind 服务配置。附录提供额外超参数、计算成本和案例分析。指南：• [N/A] 表示论文不包含实验。• 若论文包含实验，回答 [No] 不会给审稿人留下好印象：无论是否提供代码与数据，让论文可复现都很重要。• 若贡献是数据集和/或模型，作者应说明为使结果可复现或可验证而采取的步骤。• 复现方式取决于贡献。例如，若贡献是新架构，完整描述架构可能已足够；若贡献是具体模型及经验评估，则可能需要让他人能够用同一数据集复现模型，或提供模型访问。通常，发布代码和数据是一种好方法，但也可以通过详细复现指令、托管模型访问（如大语言模型）、发布模型检查点，或其他适合该研究的方式提供可复现性。• NeurIPS 不要求发布代码，但要求所有投稿提供某种合理的复现路径，具体取决于贡献性质。例如：(a) 若贡献主要是新算法，论文应明确如何复现算法。(b) 若贡献主要是新模型架构，论文应清楚完整地描述架构。(c) 若贡献是新模型（如大语言模型），则应能访问模型以复现结果，或能复现模型（如使用开源数据集或数据集构造指令）。(d) 某些情况下复现很棘手，作者可说明其提供复现性的具体方式。对闭源模型，访问可能以某种方式受限（如仅注册用户），但其他研究者仍应有某种复现或验证结果的路径。


> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> 5. Open access to data and code. Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material? Answer: [No]. Justification: The paper uses public benchmarks and datasets where available and provides detailed implementation, training, and evaluation settings in the appendix. Code and checkpoints are not included in the anonymous submission; we plan to release reproducibility materials subject to licensing and anonymization constraints. Guidelines: • The answer [N/A] means that paper does not include experiments requiring code. • Please see the NeurIPS code and data submission guidelines (https://neurips.cc/public/guides/CodeSubmissionPolicy) for more details. • While we encourage the release of code and data, we understand that this might not be possible, so [No] is an acceptable answer. Papers cannot be rejected simply for not including code, unless this is central to the contribution (e.g., for a new open-source benchmark). • The instructions should contain the exact command and environment needed to run to reproduce the results. See the NeurIPS code and data submission guidelines for more details. • The authors should provide instructions on data access and preparation, including how to access the raw data, preprocessed data, intermediate data, and generated data, etc. • The authors should provide scripts to reproduce all experimental results for the new proposed method and baselines. If only a subset of experiments are reproducible, they should state which ones are omitted from the script and why. • At submission time, to preserve anonymity, the authors should release anonymized versions (if applicable). • Providing as much information as possible in supplemental material (appended to the paper) is recommended, but including URLs to data and code is permitted.


> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 5. Open access to data and code。问题：论文是否开放访问数据和代码，并按照补充材料中的说明提供足够指令，以忠实复现主要实验结果？答案：[No]。理由：论文在可用时采用公共基准和数据集，并在附录中提供详细实现、训练与评估设置。匿名投稿未包含代码和检查点；作者计划在许可与匿名化约束下发布复现材料。指南：• [N/A] 表示论文不包含需要代码的实验。• 详情参见 NeurIPS 代码与数据投稿指南（https://neurips.cc/public/guides/CodeSubmissionPolicy）。• 鼓励发布代码和数据，但理解这可能不可行，因此回答 [No] 可以接受。除非代码是贡献核心（例如新开源基准），否则不能仅因未附代码而拒稿。• 指令应包含复现实验所需运行的准确命令与环境；详情参见 NeurIPS 代码与数据投稿指南。• 作者应提供数据访问与准备指令，包括如何访问原始、预处理、中间与生成数据等。• 作者应提供复现所提新方法和基线全部实验结果的脚本。若只有部分实验可复现，应说明脚本省略哪些实验以及原因。• 投稿时，为保持匿名，作者应在适用情况下发布匿名版本。• 建议在附加到论文的补充材料中尽可能提供信息，同时允许提供数据与代码 URL。


> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> 6. Experimental setting/details. Question: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer) necessary to understand the results? Answer: [Yes]. Justification: The main paper specifies datasets, benchmarks, metrics, frame budgets, baselines, model variants, and the two-stage training procedure. The appendix provides GSPO training configurations, reward weights, rollout settings, evaluation parameters, World2Mind parallelization, and computational costs. Guidelines: • The answer [N/A] means that the paper does not include experiments. • The experimental setting should be presented in the core of the paper to a level of detail that is necessary to appreciate the results and make sense of them. • The full details can be provided either with the code, in appendix, or as supplemental material.


> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 6. Experimental setting/details。问题：论文是否规定理解结果所必需的全部训练和测试细节（例如数据划分、超参数、其选择方式和优化器类型）？答案：[Yes]。理由：正文规定数据集、基准、指标、帧预算、基线、模型变体与两阶段训练流程。附录提供 GSPO 训练配置、奖励权重、rollout 设置、评估参数、World2Mind 并行化和计算成本。指南：• [N/A] 表示论文不包含实验。• 正文应以理解和解释结果所必需的细节层级呈现实验设置。• 完整细节可随代码、在附录或补充材料中提供。


> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> 7. Experiment statistical significance. Question: Does the paper report error bars suitably and correctly defined or other appropriate information about the statistical significance of the experiments? Answer: [No]. Justification: The paper reports benchmark scores on official Tiny subsets and controlled ablations, but does not report error bars or confidence intervals. Repeating full RL training and proprietary-model evaluations multiple times would be computationally expensive; instead, the paper provides task-level breakdowns, ablations, and comparisons across multiple model families. Guidelines: • The answer [N/A] means that the paper does not include experiments. • The authors should answer [Yes] if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that support the main claims of the paper. • The factors of variability that the error bars are capturing should be clearly stated (for example, train/test split, initialization, random drawing of some parameter, or overall run with given experimental conditions). • The method for calculating the error bars should be explained (closed form formula, call to a library function, bootstrap, etc.). • The assumptions made should be given (e.g., Normally distributed errors). • It should be clear whether the error bar is the standard deviation or the standard error of the mean. • It is OK to report 1-sigma error bars, but one should state it. The authors should preferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesis of Normality of errors is not verified. • For asymmetric distributions, the authors should be careful not to show in tables or figures symmetric error bars that would yield results that are out of range (e.g., negative error rates). • If error bars are reported in tables or plots, the authors should explain in the text how they were calculated and reference the corresponding figures or tables in the text.


> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> 7. Experiment statistical significance。问题：论文是否报告恰当且定义正确的误差条，或其他关于实验统计显著性的适当信息？答案：[No]。理由：论文报告官方 Tiny 子集上的基准分数和受控消融，但没有报告误差条或置信区间。多次重复完整 RL 训练和专有模型评估的计算成本很高；论文改为提供任务级分解、消融与跨多个模型家族的比较。指南：• [N/A] 表示论文不包含实验。• 若至少对支持主要主张的实验，结果配有误差条、置信区间或统计显著性检验，应回答 [Yes]。• 应清楚说明误差条捕获的变异因素，例如训练/测试划分、初始化、某参数的随机抽取，或给定实验条件下的完整运行。• 应解释误差条计算方法，例如闭式公式、库函数调用或 bootstrap。• 应给出所作假设，例如误差服从正态分布。• 应明确误差条表示标准差还是均值标准误。• 可以报告 1-sigma 误差条，但应说明；若未验证误差正态性，最好报告 2-sigma 误差条，而不要声称得到 96% 置信区间。• 对非对称分布，作者应避免在表图中显示会产生越界结果（如负误差率）的对称误差条。• 若表格或图中报告误差条，作者应在正文解释其计算方式，并引用相应图表。


> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> 8. Experiments compute resources. Question: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproduce the experiments? Answer: [Yes]. Justification: The appendix reports the training infrastructure, including 8 NVIDIA H200 GPUs, trainer process counts, GSPO update time, approximate wall-clock training time for AlloSpatial-4B and AlloSpatial-8B, World2Mind service workers, and inference throughput. Guidelines: • The answer [N/A] means that the paper does not include experiments. • The paper should indicate the type of compute workers CPU or GPU, internal cluster, or cloud provider, including relevant memory and storage. • The paper should provide the amount of compute required for each of the individual experimental runs as well as estimate the total compute. • The paper should disclose whether the full research project required more compute than the experiments reported in the paper (e.g., preliminary or failed experiments that didn’t make it into the paper).


> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 8. Experiments compute resources。问题：对每项实验，论文是否提供复现实验所需计算资源（计算 worker 类型、内存、执行时间）的充分信息？答案：[Yes]。理由：附录报告训练基础设施，包括 8 张 NVIDIA H200 GPU、训练进程数、GSPO 更新时间、AlloSpatial-4B 与 AlloSpatial-8B 的近似墙钟训练时间、World2Mind 服务 worker 和推理吞吐量。指南：• [N/A] 表示论文不包含实验。• 论文应说明计算 worker 的类型（CPU 或 GPU）、内部集群或云服务商，并包括相关内存与存储。• 论文应给出每次单独实验运行所需算力，并估计总算力。• 论文应披露完整研究项目是否需要比论文所报实验更多的算力，例如未写入论文的初步或失败实验。


> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> 9. Code of ethics. Question: Does the research conducted in the paper conform, in every respect, with the NeurIPS Code of Ethics https://neurips.cc/public/EthicsGuidelines? Answer: [Yes]. Justification: The work uses public benchmarks, existing foundation models, and generated tool-use trajectories for spatial reasoning research. It does not involve deception, human-subject experimentation, private personal data collection, or unsafe data release. Guidelines: • The answer [N/A] means that the authors have not reviewed the NeurIPS Code of Ethics. • If the authors answer [No], they should explain the special circumstances that require a deviation from the Code of Ethics. • The authors should make sure to preserve anonymity (e.g., if there is a special consideration due to laws or regulations in their jurisdiction).


> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> 9. Code of ethics。问题：论文开展的研究是否在所有方面遵守 NeurIPS 伦理守则 https://neurips.cc/public/EthicsGuidelines？答案：[Yes]。理由：本工作使用公共基准、现有基础模型和生成的工具使用轨迹开展空间推理研究，不涉及欺骗、人类受试者实验、私人个人数据收集或不安全数据发布。指南：• [N/A] 表示作者尚未审阅 NeurIPS 伦理守则。• 若回答 [No]，作者应解释需要偏离伦理守则的特殊情形。• 作者应确保保持匿名，例如其司法辖区法律或法规造成特殊考虑时。


> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> 10. Broader impacts. Question: Does the paper discuss both potential positive societal impacts and negative societal impacts of the work performed? Answer: [Yes]. Justification: The paper discusses AlloSpatial as foundational research toward more spatially capable multimodal and embodied agents. It also notes that incorrect spatial reasoning or over-trusting reconstructed maps can be harmful in safety-critical settings, motivating the harness-based cross-validation design and the limitation discussion on metric reliability. Guidelines: • The answer [N/A] means that there is no societal impact of the work performed. • If the authors answer [N/A] or [No], they should explain why their work has no societal impact or why the paper does not address societal impact. • Examples of negative societal impacts include potential malicious or unintended uses (e.g., disinformation, generating fake profiles, surveillance), fairness considerations (e.g., deployment of technologies that could make decisions that unfairly impact specific groups), privacy considerations, and security considerations. • The conference expects that many papers will be foundational research and not tied to particular applications, let alone deployments. However, if there is a direct path to any negative applications, the authors should point it out. For example, it is legitimate to point out that an improvement in the quality of generative models could be used to generate Deepfakes for disinformation. On the other hand, it is not needed to point out that a generic algorithm for optimizing neural networks could enable people to train models that generate Deepfakes faster. • The authors should consider possible harms that could arise when the technology is being used as intended and functioning correctly, harms that could arise when the technology is being used as intended but gives incorrect results, and harms following from intentional or unintentional misuse of the technology. • If there are negative societal impacts, the authors could also discuss possible mitigation strategies (e.g., gated release of models, providing defenses in addition to attacks, mechanisms for monitoring misuse, mechanisms to monitor how a system learns from feedback over time, improving the efficiency and accessibility of ML).


> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> 10. Broader impacts。问题：论文是否同时讨论所开展工作的潜在正面社会影响和负面社会影响？答案：[Yes]。理由：论文把 AlloSpatial 讨论为迈向更具空间能力的多模态与具身智能体的基础研究；同时指出，在安全关键场景中，错误空间推理或过度信任重建地图可能有害，这促成基于 harness 的交叉验证设计和对度量可靠性的局限讨论。指南：• [N/A] 表示所开展工作没有社会影响。• 若回答 [N/A] 或 [No]，作者应解释为何工作没有社会影响，或论文为何不讨论社会影响。• 负面社会影响的例子包括潜在恶意或非预期用途（如虚假信息、生成伪造个人资料、监控）、公平问题（如部署会作出对特定群体产生不公平影响之决策的技术）、隐私问题和安全问题。• 会议预期许多论文属于基础研究，未必与特定应用相关，更遑论部署。然而，若存在直接通往任何负面应用的路径，作者应指出。例如，指出生成模型质量的改进可用于生成用于虚假信息的 Deepfake 是合理的；另一方面，无需指出一个通用神经网络优化算法可能让人更快训练生成 Deepfake 的模型。• 作者应考虑技术按预期使用且正常运行时可能产生的危害、按预期使用但给出错误结果时可能产生的危害，以及有意或无意误用带来的危害。• 若存在负面社会影响，作者还可讨论可能的缓解策略，例如门控发布模型、在攻击之外同时提供防御、监控滥用的机制、监控系统如何随时间从反馈学习的机制，以及提升 ML 的效率和可及性。


> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> 11. Safeguards. Question: Does the paper describe safeguards that have been put in place for responsible release of data or models that have a high risk for misuse (e.g., pre-trained language models, image generators, or scraped datasets)? Answer: [N/A]. Justification: The paper does not introduce a scraped dataset, image generator, or high-risk pretrained foundation model release. The proposed method is evaluated as a spatial reasoning framework, and any future release of code or checkpoints will follow the licenses and usage restrictions of the underlying models and datasets. Guidelines: • The answer [N/A] means that the paper poses no such risks. • Released models that have a high risk for misuse or dual-use should be released with necessary safeguards to allow for controlled use of the model, for example by requiring that users adhere to usage guidelines or restrictions to access the model or implementing safety filters. • Datasets that have been scraped from the Internet could pose safety risks. The authors should describe how they avoided releasing unsafe images. • We recognize that providing effective safeguards is challenging, and many papers do not require this, but we encourage authors to take this into account and make a best faith effort.


> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> 11. Safeguards。问题：论文是否描述为负责任地发布高误用风险数据或模型（如预训练语言模型、图像生成器或抓取数据集）所采取的保障措施？答案：[N/A]。理由：论文没有引入抓取数据集、图像生成器或高风险预训练基础模型发布。所提方法作为空间推理框架评估；未来发布任何代码或检查点时，将遵循底层模型和数据集的许可及使用限制。指南：• [N/A] 表示论文不带来此类风险。• 对高误用风险或双重用途模型，应随必要保障措施一起发布，以允许受控使用，例如要求用户遵守使用指南、限制模型访问或实施安全过滤器。• 从互联网抓取的数据集可能造成安全风险；作者应说明如何避免发布不安全图像。• 我们承认有效保障措施很难提供，许多论文也不需要，但鼓励作者考虑这一点并尽最大善意努力。


> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> 12. Licenses for existing assets. Question: Are the creators or original owners of assets (e.g., code, data, models), used in the paper, properly credited and are the license and terms of use explicitly mentioned and properly respected? Answer: [Yes]. Justification: The paper cites the existing datasets, benchmarks, foundation models, geometry models, segmentation models, and spatial reasoning baselines used in the study. We use these assets for research evaluation and training under their respective terms and do not redistribute restricted proprietary models or datasets. Guidelines: • The answer [N/A] means that the paper does not use existing assets. • The authors should cite the original paper that produced the code package or dataset. • The authors should state which version of the asset is used and, if possible, include a URL. • The name of the license (e.g., CC-BY 4.0) should be included for each asset. • For scraped data from a particular source (e.g., website), the copyright and terms of service of that source should be provided. • If assets are released, the license, copyright information, and terms of use in the package should be provided. For popular datasets, paperswithcode.com/datasets has curated licenses for some datasets. Their licensing guide can help determine the license of a dataset. • For existing datasets that are re-packaged, both the original license and the license of the derived asset (if it has changed) should be provided. • If this information is not available online, the authors are encouraged to reach out to the asset’s creators.


> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> 12. Licenses for existing assets。问题：论文所用资产（如代码、数据、模型）的创作者或原所有者是否得到恰当署名，且许可与使用条款是否被明确说明并妥善遵守？答案：[Yes]。理由：论文引用研究所用的现有数据集、基准、基础模型、几何模型、分割模型和空间推理基线。作者依照各自条款把这些资产用于研究评估和训练，不再分发受限的专有模型或数据集。指南：• [N/A] 表示论文未使用现有资产。• 作者应引用产生代码包或数据集的原始论文。• 作者应说明使用的资产版本，并在可能时包含 URL。• 每项资产应包含许可名称，例如 CC-BY 4.0。• 对从特定来源（如网站）抓取的数据，应提供该来源的版权和服务条款。• 若发布资产，软件包中应提供许可、版权信息与使用条款。对于常用数据集，paperswithcode.com/datasets 为一些数据集整理了许可；其许可指南可帮助确定数据集许可。• 对重新打包的现有数据集，应同时提供原始许可与衍生资产许可（若许可发生变化）。• 若网上没有这些信息，鼓励作者联系资产创作者。


> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> 13. New assets. Question: Are new assets introduced in the paper well documented and is the documentation provided alongside the assets? Answer: [Yes]. Justification: The paper introduces AlloSpatial, World2Mind, the Spatial Reasoning Harness, and trained AlloSpatial agents. The method, prompts, tool schema, reward design, training configuration, evaluation setup, and service parallelization are documented in the main paper and appendix; release of code or checkpoints will follow anonymization and licensing constraints. Guidelines: • The answer [N/A] means that the paper does not release new assets. • Researchers should communicate the details of the dataset/code/model as part of their submissions via structured templates. This includes details about training, license, limitations, etc. • The paper should discuss whether and how consent was obtained from people whose asset is used. • At submission time, remember to anonymize your assets (if applicable). You can either create an anonymized URL or include an anonymized zip file.


> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> 13. New assets。问题：论文引入的新资产是否得到充分文档说明，并随资产提供文档？答案：[Yes]。理由：论文引入 AlloSpatial、World2Mind、Spatial Reasoning Harness 和训练后的 AlloSpatial 智能体。正文与附录记录方法、提示、工具 schema、奖励设计、训练配置、评估设置和服务并行化；代码或检查点发布将遵循匿名化和许可约束。指南：• [N/A] 表示论文不发布新资产。• 研究者应通过结构化模板，在投稿中说明数据集/代码/模型细节，包括训练、许可、局限等。• 论文应讨论是否以及如何获得资产所涉及人员的同意。• 投稿时应记得在适用情况下匿名化资产，可创建匿名 URL 或包含匿名 zip 文件。


> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> 14. Crowdsourcing and research with human subjects. Question: For crowdsourcing experiments and research with human subjects, does the paper include the full text of instructions given to participants and screenshots, if applicable, as well as details about compensation (if any)? Answer: [N/A]. Justification: The paper does not involve crowdsourcing experiments or research with human subjects. All evaluations are performed on existing benchmarks and generated model trajectories. Guidelines: • The answer [N/A] means that the paper does not involve crowdsourcing nor research with human subjects. • Including this information in the supplemental material is fine, but if the main contribution of the paper involves human subjects, then as much detail as possible should be included in the main paper. • According to the NeurIPS Code of Ethics, workers involved in data collection, curation, or other labor should be paid at least the minimum wage in the country of the data collector.


> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> 14. Crowdsourcing and research with human subjects。问题：对众包实验和人类受试者研究，论文是否包含提供给参与者的完整指令文本与截图（如适用），以及报酬细节（如有）？答案：[N/A]。理由：论文不涉及众包实验或人类受试者研究；所有评估均在现有基准和生成的模型轨迹上进行。指南：• [N/A] 表示论文不涉及众包或人类受试者研究。• 可把这些信息放在补充材料中；但若论文主要贡献涉及人类受试者，则应尽可能在正文提供细节。• 按 NeurIPS 伦理守则，参与数据收集、整理或其他劳动的工作者所得报酬至少应达到数据收集者所在国家的最低工资。


> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> 15. Institutional review board (IRB) approvals or equivalent for research with human subjects. Question: Does the paper describe potential risks incurred by study participants, whether such risks were disclosed to the subjects, and whether Institutional Review Board (IRB) approvals (or an equivalent approval/review based on the requirements of your country or institution) were obtained? Answer: [N/A]. Justification: The paper does not involve human-subject research, user studies, or collection of participant data. Therefore, IRB approval or equivalent review is not applicable. Guidelines: • The answer [N/A] means that the paper does not involve crowdsourcing nor research with human subjects. • Depending on the country in which research is conducted, IRB approval (or equivalent) may be required for any human subjects research. If you obtained IRB approval, you should clearly state this in the paper. • We recognize that the procedures for this may vary significantly between institutions and locations, and we expect authors to adhere to the NeurIPS Code of Ethics and the guidelines for their institution. • For initial submissions, do not include any information that would break anonymity (if applicable), such as the institution conducting the review.


> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> 15. Institutional review board (IRB) approvals or equivalent for research with human subjects。问题：论文是否描述研究参与者面临的潜在风险、是否向受试者披露这些风险，以及是否获得机构审查委员会（IRB）批准，或依所在国家/机构要求取得等效批准/审查？答案：[N/A]。理由：论文不涉及人类受试者研究、用户研究或参与者数据收集，因此 IRB 批准或等效审查不适用。指南：• [N/A] 表示论文不涉及众包或人类受试者研究。• 取决于研究所在国家，任何人类受试者研究都可能需要 IRB 或等效批准；如已获得，应在论文中清楚说明。• 我们承认不同机构和地点的流程可能差异很大，并期望作者遵循 NeurIPS 伦理守则与所在机构指南。• 初次投稿不得包含会破坏匿名性的信息，例如开展审查的机构。


> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> 16. Declaration of LLM usage. Question: Does the paper describe the usage of LLMs if it is an important, original, or non-standard component of the core methods in this research? Note that if the LLM is used only for writing, editing, or formatting purposes and does not impact the core methodology, scientific rigor, or originality of the research, declaration is not required. Answer: [Yes]. Justification: LLMs and MFMs are core components of the research. The paper describes the use of proprietary models for training-free evaluation and trajectory distillation, Qwen3-VL as the open-weight backbone for AlloSpatial agents, and LLM-based multi-turn tool-use reasoning as part of the proposed method. Guidelines: • The answer [N/A] means that the core method development in this research does not involve LLMs as any important, original, or non-standard components. • Please refer to our LLM policy in the NeurIPS handbook for what should or should not be described.


> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> 16. Declaration of LLM usage。问题：若 LLM 是本研究核心方法的重要、原创或非标准组件，论文是否描述了 LLM 的使用？请注意，若 LLM 仅用于写作、编辑或格式化，且不影响核心方法、科学严谨性或研究原创性，则无需声明。答案：[Yes]。理由：LLM 和 MFM 是研究的核心组件。论文描述了用于免训练评估和轨迹蒸馏的专有模型、作为 AlloSpatial 智能体开放权重骨干的 Qwen3-VL，以及作为所提方法组成部分、基于 LLM 的多轮工具使用推理。指南：• [N/A] 表示本研究核心方法开发不把 LLM 作为任何重要、原创或非标准组件。• 关于应或不应描述的内容，请参阅 NeurIPS 手册中的 LLM 政策。

