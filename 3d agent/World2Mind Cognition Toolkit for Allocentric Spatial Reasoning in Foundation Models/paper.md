# World2Mind: Cognition Toolkit for Allocentric Spatial Reasoning in Foundation Models

**Authors:** Shouwei Ruan, Bin Wang, Zhenyu Wu, Qihui Zhu, Yuxiang Zhang, Hang Su, Yubin Wang
**Source:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/VJJ4MCVA/Ruan 等 - 2026 - World2Mind Cognition Toolkit for Allocentric Spatial Reasoning in Foundation Models.pdf`
**Detected source format:** selectable-text PDF (`pdf-text`)
**Reader type:** full-paper Chinese-English Markdown reader with figure/table assets
**Version:** arXiv:2603.09774v1 [cs.AI], 10 March 2026

## Page / Section Index

| PDF pages | Content |
|---|---|
| 1 | Abstract; 1. Introduction |
| 2 | Figure 1; Introduction continued; 2. Method Overview; 2.1 Geometry-Semantic Alignment Pipeline |
| 3 | Tables 1–2; 2.1 continued; 2.2 Allocentric Cognitive Mapping; 2.3 Geometry-Semantics Interwoven Reasoning |
| 4 | Figures 2–3; 2.3 continued; 3. Experiment |
| 5–6 | Experiment conclusion; References |

## Terminology Ledger

| Canonical term | Chinese | Usage decision |
|---|---|---|
| World2Mind | World2Mind | 保留工具包名称 |
| Multimodal Foundation Model (MFM) | 多模态基础模型（MFM） | 首次展开，后用 MFM |
| allocentric | 非自我中心式 | 与 egocentric（自我中心式）相对 |
| spatial cognitive map | 空间认知地图 | 统一译法 |
| Allocentric-Spatial Tree (AST) | 非自我中心空间树（AST） | 保留 AST |
| Landmark Cognitive Map | 地标认知地图 | 统一译法 |
| Route Cognitive Map | 路径认知地图 | 统一译法 |
| geometry-semantic alignment | 几何—语义对齐 | 统一译法 |
| geometry-semantics interwoven reasoning | 几何—语义交织推理 | 统一译法 |
| modality-decoupled cue collection | 模态解耦线索收集 | 统一译法 |
| Biological Intelligence (BI) | 生物智能（BI） | 首次展开，后用 BI |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Achieving robust spatial reasoning remains a fundamental challenge for current Multimodal Foundation Models (MFMs). Existing methods either overfit statistical shortcuts via 3D grounding data or remain confined to 2D visual perception, limiting both spatial reasoning accuracy and generalization in unseen scenarios. Inspired by the spatial cognitive mapping mechanisms of biological intelligence, we propose World2Mind, a training-free spatial intelligence toolkit. At its core, World2Mind leverages 3D reconstruction and instance segmentation models to construct structured spatial cognitive maps, empowering MFMs to proactively acquire targeted spatial knowledge regarding landmarks and routes of interest. To provide robust geometric-topological priors, World2Mind synthesizes an Allocentric-Spatial Tree (AST) that uses elliptical parameters to model the top-down layout of landmarks accurately. To mitigate the inherent inaccuracies of 3D reconstruction, we introduce a three-stage reasoning chain comprising tool invocation assessment, modality-decoupled cue collection, and geometry-semantics interwoven reasoning. Extensive experiments demonstrate that World2Mind boosts the performance of frontier models, such as GPT-5.2, by 5%–18%. Astonishingly, relying solely on AST-structured text, purely text-only foundation models can perform complex 3D spatial reasoning, achieving performance approaching that of advanced multimodal models.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 对当前多模态基础模型（Multimodal Foundation Models, MFMs）而言，实现稳健的空间推理仍是一项基础性挑战。现有方法要么通过 3D grounding 数据过拟合统计捷径，要么仍局限于二维视觉感知，因而同时限制了空间推理的准确性以及在未见场景中的泛化能力。受生物智能空间认知制图机制启发，我们提出 World2Mind，一个无需训练的空间智能工具包。World2Mind 的核心是利用 3D 重建与实例分割模型构建结构化空间认知地图，使 MFM 能主动获取与感兴趣地标及路径有关的目标空间知识。为提供稳健的几何—拓扑先验，World2Mind 构建非自我中心空间树（Allocentric-Spatial Tree, AST），用椭圆参数准确刻画地标的俯视布局。为缓解 3D 重建固有的不准确性，我们引入由工具调用评估、模态解耦线索收集和几何—语义交织推理组成的三阶段推理链。大量实验表明，World2Mind 可将 GPT-5.2 等前沿模型的性能提升 5%–18%。尤其值得注意的是，仅依靠 AST 结构化文本，纯文本基础模型也能执行复杂的 3D 空间推理，其性能接近先进多模态模型。

## 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Although multimodal foundation models (MFMs) [1, 12, 24, 28] excel in general visual understanding and cross-modal reasoning [29], they struggle significantly in embodied AI and complex spatial reasoning tasks requiring physical interaction [15, 17, 18, 26, 34]. This deficiency stems from their over-reliance on egocentric observations and lack of capacity to abstract global spatial topology [18, 34], trapping MFMs in an insurmountable “semantic-geometry gap” in tasks such as distance estimation, viewpoint transformation, and path planning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 尽管多模态基础模型（MFM）[1, 12, 24, 28] 擅长通用视觉理解与跨模态推理 [29]，但在具身 AI 以及需要物理交互的复杂空间推理任务中仍表现困难 [15, 17, 18, 26, 34]。这一缺陷源于模型过度依赖自我中心式观察，且缺乏抽象全局空间拓扑的能力 [18, 34]，使 MFM 在距离估计、视角变换与路径规划等任务中陷入难以跨越的“语义—几何鸿沟”。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Current efforts to enhance MFMs’ spatial reasoning primarily follow two paradigms. Training-based methods [6, 9, 20] fine-tune models on massive 3D-grounded QA pairs. However, this forces models to overfit statistical shortcuts [14, 25] rather than acquire genuine spatial cognition, leading to poor generalization in out-of-distribution scenarios [33]. Alternatively, introducing explicit 3D modalities [7, 10, 21, 31] exacerbates inter-modal alignment challenges [35]. Meanwhile, recent tool-based methods [8, 19, 36] rely on active rendering under large-scale 3D reconstruction. These methods are severely bottlenecked by reconstruction quality and remain tethered to low-level visual perception, failing to abstract geometric data into structured semantics for high-level logical reasoning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 当前增强 MFM 空间推理能力的工作主要遵循两种范式。基于训练的方法 [6, 9, 20] 使用海量 3D-grounded 问答对微调模型，但这会迫使模型过拟合统计捷径 [14, 25]，而非获得真正的空间认知，导致其在分布外场景中泛化不佳 [33]。另一类方法引入显式 3D 模态 [7, 10, 21, 31]，却进一步加剧了模态间对齐难题 [35]。与此同时，近期基于工具的方法 [8, 19, 36] 依赖大规模 3D 重建下的主动渲染，受到重建质量的严重制约，并仍束缚于低层视觉感知，无法将几何数据抽象成可供高层逻辑推理使用的结构化语义。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Biological Intelligence (BI) offers an ideal blueprint for breaking the shackles of egocentric observation. Rather than reacting passively to transient visual inputs, the biological brain intrinsically transforms egocentric views into an allocentric perspective [4]. Supported by place cells in the hippocampus [3, 11, 22] and grid cells in the entorhinal cortex [13], mammals construct a global cognitive map entirely independent of their egocentric viewpoint [23, 27]. This map forms the cornerstone for strategic mental simulation and advanced reasoning [2].

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 生物智能（Biological Intelligence, BI）为摆脱自我中心式观察的束缚提供了理想蓝图。生物大脑并非被动响应短暂的视觉输入，而是会内在地将自我中心视图转换为非自我中心视角 [4]。在海马体位置细胞 [3, 11, 22] 和内嗅皮层网格细胞 [13] 的支持下，哺乳动物能够构建完全独立于自身观察视点的全局认知地图 [23, 27]。这张地图构成策略性心理模拟与高级推理的基石 [2]。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> To bridge this gap between foundation models and BI in spatial representation and reasoning, we propose World2Mind, a plug-and-play spatial cognition toolkit that equips models with human-like mental simulation capabilities. World2Mind integrates an efficient geometry-semantics alignment pipeline, leveraging pre-trained visual geometry [16, 30, 32] and instance segmentation models [5] to extract semantic voxel grids. From these, it constructs two core representations: (1) a Route Cognitive Map for passability prediction, and (2) a Landmark Cognitive Map for object topology. Encapsulated as an accessible toolset, World2Mind enables models to dynamically specify parameters—such as instances of interest, required spatial knowledge, and map visualizations—to proactively acquire targeted allocentric spatial knowledge on demand.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 为弥合基础模型与 BI 在空间表征和推理方面的差距，我们提出即插即用的空间认知工具包 World2Mind，为模型赋予类人的心理模拟能力。World2Mind 集成高效的几何—语义对齐流程，利用预训练视觉几何模型 [16, 30, 32] 与实例分割模型 [5] 提取语义体素网格，并据此构建两种核心表征：（1）用于通行性预测的路径认知地图；（2）用于物体拓扑建模的地标认知地图。World2Mind 被封装为易用工具集，使模型能够动态指定感兴趣实例、所需空间知识和地图可视化等参数，按需主动获取目标化的非自我中心空间知识。

### Figure 1. World2Mind overview

![Figure 1](3d%20agent/World2Mind%20Cognition%20Toolkit%20for%20Allocentric%20Spatial%20Reasoning%20in%20Foundation%20Models/assets/figure_1.png)

**Caption:** Overview of foundation models performing allocentric spatial reasoning via the proposed World2Mind toolkit. Given egocentric video or multi-view observations, the model first assesses the necessity of tool invocation and subsequently passes key parameters (e.g., instances of interest) to World2Mind to drive the generation of spatial cognitive maps. World2Mind integrates an efficient pipeline for 3D reconstruction and semantic-geometry alignment, returning the required structured spatial knowledge through targeted projection and rendering mechanisms. Furthermore, the model conducts geometry-semantics interwoven reasoning based on both the raw visual observations and the geometric cues provided by World2Mind, ultimately yielding highly reliable answers.

**Caption[CN]:** 基础模型通过所提出的 World2Mind 工具包执行非自我中心空间推理的概览。给定自我中心视频或多视图观察，模型首先判断是否需要调用工具，随后将关键参数（如感兴趣实例）传给 World2Mind，以驱动空间认知地图的生成。World2Mind 集成高效的 3D 重建与语义—几何对齐流程，并通过目标化投影和渲染机制返回所需的结构化空间知识。模型进一步结合原始视觉观察与 World2Mind 提供的几何线索进行几何—语义交织推理，最终给出高可靠答案。

**Reading note:** 图中完整保留了“问题—工具判断—视觉/地图线索—交叉验证—答案”的示例流程，以及 Landmark/Route 两类地图与 API 参数。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> To provide robust geometric-topological priors, we formally define the Allocentric-Spatial Tree (AST) as the core spatial representation in World2Mind. The AST is a directed acyclic graph using geometrically stable landmarks (e.g., beds and tables) as core nodes to hierarchically associate surrounding smaller instances. Crucially, to approximate the fuzzy nature of human cognition, the AST models spatial footprints using rectangle-elliptical parameters (bounding boxes, major/minor axes, eccentricity, and rotation angles). These designs equip models with robust, dense, and highly actionable geometric-topological priors.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 为提供稳健的几何—拓扑先验，我们正式将非自我中心空间树（AST）定义为 World2Mind 的核心空间表征。AST 是一种有向无环图，以几何上稳定的地标（如床和桌子）作为核心节点，并以层级方式关联周围较小的实例。关键在于，为贴近人类认知的模糊性，AST 使用矩形—椭圆参数（边界框、长/短轴、偏心率和旋转角）对空间占用范围建模。这些设计为模型提供稳健、稠密且高度可操作的几何—拓扑先验。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> However, merely offering spatial representation is insufficient to guarantee robust reasoning. In complex physical scenarios, reconstruction quality often suffers severe corruption due to occlusions or restricted viewpoints, leading to conflicts with objective geometric laws and raw visual observations. To mitigate this risk, we integrate a rigorous spatial reasoning chain into World2Mind: (1) Difficulty Assessment and Tool Invocation, preventing over-computation on simple superficial queries; (2) Modality-Decoupled Cue Collection, independently extracting information from egocentric vision, AST-structured text, and map visualizations; and (3) Geometry-Semantics Interwoven Reasoning, guiding the model to resolve cross-modal conflicts proactively and ultimately yield reliable spatial decisions.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 然而，仅提供空间表征不足以保证稳健推理。在复杂物理场景中，遮挡或受限视角常会严重破坏重建质量，从而使重建结果与客观几何规律和原始视觉观察发生冲突。为降低这一风险，我们在 World2Mind 中集成严格的空间推理链：（1）难度评估与工具调用，避免在简单表层问题上进行过度计算；（2）模态解耦线索收集，分别从自我中心视觉、AST 结构化文本和地图可视化中独立提取信息；（3）几何—语义交织推理，引导模型主动化解跨模态冲突，最终做出可靠的空间决策。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Extensive evaluations across various spatial reasoning benchmarks demonstrate that World2Mind yields stable performance improvements of 6%–18% for frontier models such as GPT-5.2, while maintaining exceptional efficiency and reasoning interpretability. Astonishingly, by leveraging the pure, high-density allocentric priors provided by the AST, text-only foundation models can execute complex 3D reasoning directly within their parameter space simply by reading the AST representation, approaching the performance of advanced multimodal models. Our findings offer a highly promising pathway to overcome the spatial cognition bottleneck in foundation models.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 在多种空间推理基准上的广泛评测表明，World2Mind 能为 GPT-5.2 等前沿模型带来稳定的 6%–18% 性能提升，同时保持出色的效率与推理可解释性。尤为惊人的是，借助 AST 提供的纯净、高密度非自我中心先验，纯文本基础模型只需读取 AST 表征，就能直接在参数空间内执行复杂的 3D 推理，性能接近先进多模态模型。该发现为突破基础模型的空间认知瓶颈提供了一条很有希望的路径。

## 2. Method Overview

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This section details the technical overview of the proposed World2Mind, as illustrated in Fig. 1.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本节结合图 1 详细介绍所提出 World2Mind 的技术概览。

### 2.1. Geometry-Semantic Alignment Pipeline

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Given an egocentric video sequence or multi-view image set $\{I_t\}_{t=1}^{T}$, our primary objective is to transcend the limitations of 2D vision and construct a robust 3D semantic representation of the physical world.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 给定自我中心视频序列或多视图图像集合 $\{I_t\}_{t=1}^{T}$，我们的首要目标是超越二维视觉的限制，为物理世界构建稳健的 3D 语义表征。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Depth Estimation & Semantic Extraction.** We employ Depth Anything V3 [16] for monocular depth estimation, obtaining the depth map $D_t \in \mathbb{R}^{H\times W}$ and camera pose $T_t \in SE(3)$. Concurrently, we utilize SAM3 [5] to extract open-vocabulary semantic masks $M_t$ based on a user-specified category list $C$. To suppress the accumulation of long-tail errors inherent in depth estimation, we introduce a dual-level filtering mechanism based on the predicted confidence map $C_t \in [0,1]^{H\times W}$. Specifically, we formulate a binary validity mask $V_t \in \{0,1\}^{H\times W}$ as follows:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **深度估计与语义提取。** 我们采用 Depth Anything V3 [16] 进行单目深度估计，得到深度图 $D_t \in \mathbb{R}^{H\times W}$ 与相机位姿 $T_t \in SE(3)$。与此同时，我们使用 SAM3 [5]，依据用户指定的类别列表 $C$ 提取开放词汇语义掩码 $M_t$。为抑制深度估计固有长尾误差的累积，我们基于预测置信度图 $C_t \in [0,1]^{H\times W}$ 引入双层过滤机制。具体而言，二值有效性掩码 $V_t \in \{0,1\}^{H\times W}$ 定义如下：

$$
V_t(u,v)=\mathbb{I}(C_t(u,v)>\tau_{\mathrm{pixel}})\cdot\mathbb{I}(\mu_t>\tau_{\mathrm{frame}}). \tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Here $\mu_t=\frac{1}{HW}\sum_{x=1}^{H}\sum_{y=1}^{W}C_t(x,y)$ denotes the global spatial confidence of frame $t$, and $\mathbb{I}(\cdot)$ is the indicator function that returns 1 if the condition is met and 0 otherwise. The variables $\tau_{\mathrm{pixel}}$ and $\tau_{\mathrm{frame}}$ represent the pixel-level and frame-level thresholds, respectively. A pixel is incorporated into subsequent reconstruction only when $V_t(u,v)=1$.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 其中，$\mu_t=\frac{1}{HW}\sum_{x=1}^{H}\sum_{y=1}^{W}C_t(x,y)$ 表示第 $t$ 帧的全局空间置信度，$\mathbb{I}(\cdot)$ 为指示函数：条件成立时返回 1，否则返回 0。$\tau_{\mathrm{pixel}}$ 与 $\tau_{\mathrm{frame}}$ 分别表示像素级和帧级阈值。仅当 $V_t(u,v)=1$ 时，相应像素才会被纳入后续重建。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Point Cloud Mapping & Density Filtering.** Qualifying 2D pixels are back-projected into the world coordinate system via camera intrinsic matrix $K$, generating a global point cloud $\mathcal{P}=\{(\mathbf{p}_i,s_i,\mathrm{rgb}_i)\}_{i=1}^{M}$ carrying semantic labels $s_i\in C$. To address boundary outliers inherent in depth estimation, we propose a core-region extraction strategy: for each point, we calculate its $K$-nearest-neighbor local density $\rho_i=\frac{1}{K}\sum_{j\in\mathcal{N}_K(i)}\|\mathbf{p}_i-\mathbf{p}_j\|^{-1}$, and eliminate low-density “tail” points based on density percentiles. This yields an exceptionally pure geometry-semantic substrate.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **点云映射与密度过滤。** 符合条件的二维像素通过相机内参矩阵 $K$ 反投影到世界坐标系，生成携带语义标签 $s_i\in C$ 的全局点云 $\mathcal{P}=\{(\mathbf{p}_i,s_i,\mathrm{rgb}_i)\}_{i=1}^{M}$。针对深度估计固有的边界离群点，我们提出核心区域提取策略：对每个点计算其 $K$ 近邻局部密度 $\rho_i=\frac{1}{K}\sum_{j\in\mathcal{N}_K(i)}\|\mathbf{p}_i-\mathbf{p}_j\|^{-1}$，并依据密度百分位去除低密度“尾部”点，由此获得高度纯净的几何—语义基底。

### 2.2. Allocentric Cognitive Mapping

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Inspired by the spatial mapping mechanisms of BI, we distill the unstructured point cloud into two highly abstract cognitive maps, enabling the model to proactively acquire spatial knowledge on demand via tool invocation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 受 BI 空间制图机制启发，我们将无结构点云提炼为两种高度抽象的认知地图，使模型能够通过工具调用，按需主动获取空间知识。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Landmark Cognitive Mapping.** Traditional methods rely on ambiguous relative relations or simplified grid representations [18, 34]. To overcome this, we formally define the Allocentric-Spatial Tree (AST), which reorganizes spatial entities as a directed acyclic graph within an absolute coordinate system. Specifically, we perform adaptive DBSCAN clustering on each semantic category within the point cloud to separate distinct instances. For each instance node, the AST discards traditional bounding boxes and instead fits a minimum bounding ellipse in the top-down view (X–Z plane), extracting centroid $(x_c,z_c)$, major and minor axes $a$ and $b$, and rotation angle $\theta$. This parameterization (1) significantly enhances robustness against reconstruction boundary noise and (2) aligns with the fuzzy probabilistic nature of human spatial-footprint perception. Output as dense structured text (e.g., YAML), the AST explicitly encodes hierarchical containment relationships among entities together with multidimensional geometric attributes.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **地标认知制图。** 传统方法依赖模糊的相对关系或简化网格表征 [18, 34]。为克服这一问题，我们正式定义 AST，将空间实体在绝对坐标系中重组为有向无环图。具体而言，我们对点云中每个语义类别执行自适应 DBSCAN 聚类，以分离不同实例。对于每个实例节点，AST 不采用传统边界框，而是在俯视图（X–Z 平面）中拟合最小外接椭圆，提取质心 $(x_c,z_c)$、长短轴 $a,b$ 与旋转角 $\theta$。该参数化方式：（1）显著增强对重建边界噪声的稳健性；（2）契合人类对空间占用范围进行模糊概率感知的特性。AST 以稠密结构化文本（如 YAML）输出，显式编码实体间的层级包含关系及多维几何属性。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Route Cognitive Mapping.** For navigation-oriented tasks, World2Mind also extracts masks of traversable categories (e.g., floors), back-projects and voxelizes them, and then partitions them into an $N\times N$ grid map on the top-down plane. Combined with the mapped camera trajectory sequence $\{T_t\}$, this route map provides explicit priors regarding passability and the human observer’s motion trajectory.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **路径认知制图。** 对面向导航的任务，World2Mind 还会提取可通行类别（如地面）的掩码，对其进行反投影和体素化，再在俯视平面划分为 $N\times N$ 网格地图。结合映射后的相机轨迹序列 $\{T_t\}$，该路径地图为模型提供有关可通行性与人类观察者运动轨迹的显式先验。

### 2.3. Geometry-Semantics Interwoven Reasoning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In physical scenarios, 2D visual observations are susceptible to occlusions and adverse viewpoints, while 3D reconstruction information may contain local errors. To resolve potential contradictions between these two modalities, we design a rigorous three-stage interwoven reasoning chain.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在物理场景中，二维视觉观察容易受到遮挡与不利视角影响，而 3D 重建信息也可能包含局部误差。为解决两种模态之间的潜在矛盾，我们设计了一条严格的三阶段交织推理链。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Stage 1: Tool Invocation Judgement.** To reduce unnecessary computational overhead, the model must first evaluate the spatial relevance of the query. It should proactively invoke World2Mind only when the task explicitly involves spatial reasoning, such as occlusion inference, distance estimation, or path planning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **阶段 1：工具调用判断。** 为减少不必要的计算开销，模型必须首先评估问题与空间的相关性。仅当任务明确涉及遮挡推断、距离估计或路径规划等空间推理时，模型才应主动调用 World2Mind。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Stage 2: Modality-Decoupled Cue Collection.** We force the model to extract information independently to prevent early modality bias. It must simultaneously gather corroborating evidence from three independent sources: egocentric vision, AST text returned by World2Mind, and optional 2D top-down map visualizations.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **阶段 2：模态解耦线索收集。** 为防止早期模态偏置，我们要求模型独立提取信息。模型必须同时从三个相互独立的来源收集彼此印证的证据：自我中心视觉、World2Mind 返回的 AST 文本，以及可选的二维俯视地图可视化。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Stage 3: Conflict Resolution and Cross-Validation.** This is the crux of the reasoning chain. The model must proactively coordinate evidence across modalities and identify cross-modal conflicts, such as missing objects caused by visual truncation or coordinate drift caused by depth errors. By cross-validating objective AST geometric parameters against subjective visual appearances, the model can dynamically weigh the credibility of visual illusions versus reconstruction artifacts, ultimately producing highly reliable and logically interpretable decisions.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **阶段 3：冲突消解与交叉验证。** 这是推理链的核心。模型需要主动协调不同模态的证据，并识别跨模态冲突，例如视觉截断造成的物体缺失，或深度误差造成的坐标漂移。通过将 AST 的客观几何参数与主观视觉外观交叉验证，模型可以动态权衡视觉错觉和重建伪影的可信度，最终给出高度可靠且逻辑可解释的决策。

## 3. Experiment

### 3.1. Experimental Setup

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We conduct evaluations on two challenging spatial reasoning benchmarks: VSI-Bench [34], which focuses on video-based reasoning in real-world physical scenes, and MindCube [18], which emphasizes multi-view cognitive mapping and mental simulation. Our evaluation primarily targets frontier multimodal foundation models, including GPT, Claude, and Gemini, given their exceptional proficiency in tool invocation and instruction following.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们在两个具有挑战性的空间推理基准上进行评测：VSI-Bench [34] 聚焦真实物理场景中的视频推理；MindCube [18] 强调多视图认知制图与心理模拟。鉴于 GPT、Claude 和 Gemini 在工具调用与指令遵循方面表现出色，评测主要面向这些前沿多模态基础模型。

### 3.2. Main Results and Analysis

### Table 1. Main results on VSI-Bench (Tiny subset)

![Table 1](3d%20agent/World2Mind%20Cognition%20Toolkit%20for%20Allocentric%20Spatial%20Reasoning%20in%20Foundation%20Models/assets/table_1.png)

**Caption:** Main results on the VSI-Bench [34] benchmark (Tiny subset).

**Caption[CN]:** VSI-Bench [34] 基准 Tiny 子集上的主要结果。

| Models | Avg. | Obj. Count | Abs. Dist. | Obj. Size | Room Size | Rel. Dist. | Rel. Dir. | Route Plan | Appr. Order |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Without World2Mind** ||||||||||
| GPT-5.2 | 46.7 | 52.5 | 34.9 | 67.5 | 50.6 | 42.0 | 40.7 | 34.7 | 51.0 |
| Claude-4.6-Opus | 38.4 | 46.9 | 18.5 | 62.1 | 26.8 | 40.0 | 47.2 | 34.7 | 30.6 |
| Gemini-3-Pro | 55.2 | 47.8 | 32.1 | 71.3 | 55.0 | 54.0 | 44.8 | 57.1 | 79.6 |
| **With World2Mind** ||||||||||
| GPT-5.2 | 54.0 (↑7.3) | 47.4 (↓5.1) | 33.4 (↓1.5) | 63.3 (↓4.2) | 52.4 (↑1.8) | 64.0 (↑22.0) | 41.1 (↑0.4) | 51.0 (↑16.3) | 79.6 (↑28.6) |
| Claude-4.6-Opus | 56.0 (↑17.7) | 59.0 (↑12.0) | 34.3 (↑15.8) | 67.3 (↑5.2) | 54.8 (↑28.0) | 64.0 (↑24.0) | 62.7 (↑15.6) | 65.3 (↑30.6) | 40.8 (↑10.2) |
| Gemini-3-Pro | 61.0 (↑5.8) | 51.8 (↑4.1) | 36.8 (↑4.7) | 57.7 (↓13.5) | 62.6 (↑7.6) | 62.0 (↑8.0) | 67.7 (↑22.9) | 65.3 (↑8.2) | 83.7 (↑4.1) |

### Table 2. Results on MindCube-Tiny

![Table 2](3d%20agent/World2Mind%20Cognition%20Toolkit%20for%20Allocentric%20Spatial%20Reasoning%20in%20Foundation%20Models/assets/table_2.png)

**Caption:** Results on the MindCube-Tiny [18] benchmark.

**Caption[CN]:** MindCube-Tiny [18] 基准上的结果。

| Models | Avg. | Around | Among | Rotation |
|---|---:|---:|---:|---:|
| **Without World2Mind** ||||
| GPT-5.2 | 49.9 | 62.4 | 45.2 | 48.5 |
| Claude-4.6-Opus | 48.5 | 58.8 | 50.7 | 29.0 |
| Gemini-3-Pro | 75.1 | 77.2 | 68.2 | 93.0 |
| **With World2Mind** ||||
| GPT-5.2 | 54.6 (↑4.7) | 60.4 (↓2.0) | 47.7 (↑2.5) | 68.0 (↑19.5) |
| Claude-4.6-Opus | 62.9 (↑14.4) | 82.4 (↑23.6) | 60.8 (↑10.1) | 45.0 (↑16.0) |
| Gemini-3-Pro | 81.6 (↑6.5) | 86.0 (↑8.8) | 75.8 (↑7.6) | 93.5 (↑0.5) |

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Evaluation on VSI-Bench.** As shown in Tab. 1, seamless integration of World2Mind yields a substantial leap in average performance across all frontier models. Specifically, GPT-5.2 improves by 7.3%, while Claude-4.6-Opus improves by 17.7%. In-depth subtask analysis reveals that gains are most striking in categories that rely heavily on allocentric priors. For Claude-4.6-Opus, Relative Direction, Route Planning, and Relative Distance improve by 15.6%, 30.6%, and 24.0%, respectively. This demonstrates the critical role of allocentric spatial knowledge from World2Mind in bridging the spatial reasoning gap.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **VSI-Bench 评测。** 如表 1 所示，无缝集成 World2Mind 后，所有前沿模型的平均性能均显著提升。具体而言，GPT-5.2 提升 7.3%，Claude-4.6-Opus 提升 17.7%。深入分析各子任务可见，性能增益在高度依赖非自我中心先验的类别中最为显著。Claude-4.6-Opus 在相对方向、路径规划和相对距离任务上分别提升 15.6%、30.6% 和 24.0%。这有力说明 World2Mind 提供的非自我中心空间知识对弥合空间推理差距具有关键作用。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Evaluation on MindCube.** The results in Tab. 2 further corroborate the universality and robustness of our framework under sparse multi-view inputs. Even for Gemini-3-Pro, whose native spatial reasoning is already top-tier (baseline Avg. 75.1%), World2Mind pushes average accuracy to 81.6% (+6.5%). Notably, on “Rotation,” which severely tests 3D spatial imagination, GPT-5.2 improves by 19.5% because it can perform logical deduction grounded in the AST.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **MindCube 评测。** 表 2 的结果进一步验证了框架在稀疏多视图输入下的普适性与稳健性。即使 Gemini-3-Pro 原生空间推理能力已处于顶尖水平（基线平均分 75.1%），World2Mind 仍将其平均准确率推至 81.6%（+6.5%）。尤其在严苛考验 3D 空间想象的 “Rotation” 任务上，GPT-5.2 因能够基于 AST 进行逻辑推演而提升 19.5%。

### 3.3. Ablation and Case Study

### Figure 2. Text-only (“blind”) comparison

![Figure 2](3d%20agent/World2Mind%20Cognition%20Toolkit%20for%20Allocentric%20Spatial%20Reasoning%20in%20Foundation%20Models/assets/figure_2.png)

**Caption:** Performance comparison under the text-only model (“blind”) setting. The figure reports the performance gap on the VSI-Bench Tiny subset between foundation models relying solely on commonsense reasoning and those leveraging World2Mind to acquire structured spatial knowledge for allocentric reasoning.

**Caption[CN]:** 纯文本模型（“blind”）设定下的性能比较。该图报告 VSI-Bench Tiny 子集上，仅依赖常识推理的基础模型与借助 World2Mind 获取结构化空间知识进行非自我中心推理的模型之间的性能差距。

### Figure 3. Complete World2Mind reasoning trace

![Figure 3](3d%20agent/World2Mind%20Cognition%20Toolkit%20for%20Allocentric%20Spatial%20Reasoning%20in%20Foundation%20Models/assets/figure_3.png)

**Caption:** Complete reasoning trace under World2Mind.

**Caption[CN]:** World2Mind 下的完整推理轨迹。

**Prompt / trace transcription:**

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Question:** “What is the longest length of the chair (in centimeters)?” **Initial visual reasoning:** “I see a black office chair in the closet area (and another chair at the desk with a jacket draped over it). The chair’s longest ‘side’ likely refers to the largest dimension of the chair as seen from the side—typically the height from the floor to the top of the backrest. Visually, it looks like a standard office chair, roughly around 90–110 cm tall. To answer in centimeters more reliably, metric estimation from a spatial tool would help.” **Tool Call:** `world2mind`. **Arguments:** `{"categories": ["chair", "desk"], "knowledge_type": "landmark"}`.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **问题：**“椅子最长的长度是多少（厘米）？” **初始视觉推理：**“我在壁橱区域看到一把黑色办公椅（书桌旁还有另一把搭着夹克的椅子）。椅子最长的‘边’很可能指从侧面观察时的最大尺寸——通常是从地面到椅背顶部的高度。视觉上看，它像一把标准办公椅，高度约 90–110 厘米。为了更可靠地以厘米作答，借助空间工具进行度量估计会有帮助。” **工具调用：**`world2mind`。**参数：**`{"categories": ["chair", "desk"], "knowledge_type": "landmark"}`。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Map clues:** The tool detected two chairs. `chair_01`: rectangle width 0.611 m, height 0.45 m (this “height” is a footprint dimension in the 2D map, not vertical); vertical `Height_Range` 1.093–1.628 m, giving an extent of approximately 0.535 m. `chair_02`: width 0.12 m, height 0.329 m; `Height_Range` 0.648–1.599 m, giving an extent of approximately 0.951 m. The “longest side” most plausibly corresponds to the largest dimension, namely `chair_02` at about 0.951 m = 95.1 cm. **Tool Call:** `world2mind`. **Arguments:** `{"visualization_type": "landmark_vis"}`.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **地图线索：**工具检测到两把椅子。`chair_01`：矩形宽 0.611 m、高 0.45 m（这里的“高”是二维地图中的占地尺寸，并非垂直高度）；垂直 `Height_Range` 为 1.093–1.628 m，因此垂直跨度约 0.535 m。`chair_02`：宽 0.12 m、高 0.329 m；`Height_Range` 为 0.648–1.599 m，因此跨度约 0.951 m。“最长边”最合理地对应最大尺寸，即 `chair_02` 的约 0.951 m = 95.1 cm。**工具调用：**`world2mind`。**参数：**`{"visualization_type": "landmark_vis"}`。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Visualization clues and cross-validation:** The landmark visualization indicates that one chair aligns with the closet/desk-chair region and the other is smaller or partial. The larger-vertical-extent instance (`chair_02`) corresponds to the office-chair shape. Visually, an office-chair height around 1 m is plausible; the tool’s 95.1 cm estimate is consistent with a typical office chair. The alternative (`chair_01`) appears to be a partial detection with a smaller vertical extent. **Final answer:** 95 cm.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **可视化线索与交叉验证：**地标可视化表明，一个椅子实例与壁橱/书桌椅区域对齐，另一个实例更小或仅被部分检测。垂直跨度更大的实例（`chair_02`）对应办公椅形状。从视觉上看，办公椅高度约 1 m 是合理的；工具估计的 95.1 cm 也符合典型办公椅。备选实例 `chair_01` 看起来是垂直跨度更小的局部检测。**最终答案：**95 cm。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> To explore how far AST-structured text can empower the spatial cognition of large language models, we follow [34] and conduct ablations in the text-only (“blind”) setting (Fig. 2). With visual inputs removed, foundation models relying only on commonsense priors degrade to near-random guessing on spatial tasks. When equipped with World2Mind, however, GPT-5.2 and Claude-4.6-Opus show a remarkable rebound in the blind state. On core tasks such as Object Size and Route Planning, their scores approach those achieved with full visual inputs. This indicates that pure, high-quality allocentric geometric priors are sufficient to ignite strong 3D mental reconstruction and simulation capabilities in text-based foundation-model reasoning.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 为探究 AST 结构化文本能够在多大程度上增强大语言模型的空间认知，我们遵循 [34]，在纯文本（“blind”）设定下进行消融实验（图 2）。完全移除视觉图像输入后，仅依赖常识先验的基础模型在空间任务上会退化到接近随机猜测。然而，配备 World2Mind 后，GPT-5.2 与 Claude-4.6-Opus 在盲测状态下均显著回升。在 Object Size、Route Planning 等核心推理任务上，它们的得分接近具有完整视觉输入时的水平。这说明，纯净且高质量的非自我中心几何先验足以在基于文本的基础模型推理中激活强大的 3D 心理重建与模拟能力。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Furthermore, Fig. 3 visualizes the complete reasoning traces powered by World2Mind, clearly demonstrating that the interwoven reasoning process exhibits exceptional robustness and logical interpretability when resolving cross-modal conflicts.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 此外，图 3 展示了 World2Mind 支持下的完整推理轨迹，清楚表明这种交织推理过程在解决跨模态冲突时具有出色的稳健性与逻辑可解释性。

## References

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The source contains 36 references. Following the WJ reader policy, bibliography entries are preserved in their original language rather than translated line by line. Page-number suffixes emitted by the PDF bibliography style are omitted below.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 原文共含 36 条参考文献。按照 WJ reader 规范，书目条目保留原文，不逐条翻译；PDF 参考文献样式附带的正文引用页码后缀在下列清单中省略。

1. Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang Gao, Chunjiang Ge, et al. “Qwen3-VL Technical Report.” arXiv:2511.21631, 2025.
2. Jacob L. S. Bellmund, Peter Gärdenfors, Edvard I. Moser, and Christian F. Doeller. “Navigating Cognition: Spatial Codes for Human Thinking.” *Science* 362(6415):eaat6766, 2018.
3. Nicola J. Broadbent, Larry R. Squire, and Robert E. Clark. “Spatial Memory, Recognition Memory, and the Hippocampus.” *PNAS* 101(40):14515–14520, 2004.
4. Neil Burgess. “Spatial Memory: How Egocentric and Allocentric Combine.” *Trends in Cognitive Sciences* 10(12):551–557, 2006.
5. Nicolas Carion et al. “SAM 3: Segment Anything with Concepts.” arXiv:2511.16719, 2025.
6. Boyuan Chen et al. “SpatialVLM: Endowing Vision-Language Models with Spatial Reasoning Capabilities.” CVPR, pp. 14455–14465, 2024.
7. Pingyi Chen et al. “SD-VLM: Spatial Measuring and Understanding with Depth-Encoded Vision-Language Models.” arXiv:2509.17664, 2025.
8. Siyi Chen et al. “SpaceTools: Tool-Augmented Spatial Reasoning via Double Interactive RL.” arXiv:2512.04069, 2025.
9. An-Chieh Cheng et al. “SpatialRGPT: Grounded Spatial Reasoning in Vision-Language Models.” *NeurIPS* 37:135062–135093, 2024.
10. Erik Daxberger et al. “MM-Spatial: Exploring 3D Spatial Understanding in Multimodal LLMs.” ICCV, pp. 7395–7408, 2025.
11. Howard Eichenbaum. “The Role of the Hippocampus in Navigation Is Memory.” *Journal of Neurophysiology* 117(4):1785–1796, 2017.
12. Google. “Gemini 3.1 Pro: Best for Complex Tasks and Bringing Creative Concepts to Life.” https://deepmind.google/models/gemini/pro/, 2026.
13. Torkel Hafting et al. “Microstructure of a Spatial Map in the Entorhinal Cortex.” *Nature* 436(7052):801–806, 2005.
14. Jiaxin Huang et al. “Surprise3D: A Dataset for Spatial Understanding and Reasoning in Complex 3D Scenes.” arXiv:2507.07781, 2025.
15. Shuai Huang, Wenxuan Zhao, and Jun Gao. “SI-Bench: Benchmarking Social Intelligence of Large Language Models in Human-to-Human Conversations.” arXiv:2510.23182, 2025.
16. Haotong Lin et al. “Depth Anything 3: Recovering the Visual Space from Any Views.” arXiv:2511.10647, 2025.
17. Jingli Lin et al. “MMSI-Video-Bench: A Holistic Benchmark for Video-Based Spatial Intelligence.” arXiv:2512.10863, 2025.
18. Fangzheng Liu, Don Derek Haddad, and Joe Paradiso. “MindCube: An Interactive Device for Gauging Emotions.” UIST Adjunct, pp. 1–2, 2024.
19. Zhanpeng Luo et al. “PySpatial: Generating 3D Visual Programs for Zero-Shot Spatial Reasoning.” arXiv:2603.00905, 2026.
20. Wufei Ma et al. “SpatialReasoner: Towards Explicit and Generalizable 3D Spatial Reasoning.” arXiv:2504.20024, 2025.
21. Zhenhua Ning et al. “Enhancing Spatial Reasoning in Multimodal Large Language Models through Reasoning-Based Segmentation.” ICCV, pp. 7851–7860, 2025.
22. John O’Keefe and Jonathan Dostrovsky. “The Hippocampus as a Spatial Map: Preliminary Evidence from Unit Activity in the Freely-Moving Rat.” *Brain Research*, 1971.
23. John O’Keefe and Lynn Nadel. *The Hippocampus as a Cognitive Map*. Oxford University Press, 1978.
24. OpenAI. “GPT-4V(ision) System Card.” https://cdn.openai.com/papers/GPTV_System_Card.pdf, 2023.
25. Jianing Qi, Jiawei Liu, Hao Tang, and Zhigang Zhu. “Beyond Semantics: Rediscovering Spatial Awareness in Vision-Language Models.” arXiv:2503.17349, 2025.
26. Santhosh Kumar Ramakrishnan, Erik Wijmans, Philipp Kraehenbuehl, and Vladlen Koltun. “Does Spatial Cognition Emerge in Frontier Models?” arXiv:2410.06468, 2024.
27. Daniela Schiller et al. “Memory and Space: Towards an Understanding of the Cognitive Map.” *Journal of Neuroscience* 35(41):13904–13911, 2015.
28. Aaditya Singh et al. “OpenAI GPT-5 System Card.” arXiv:2601.03267, 2025.
29. Zhaochen Su et al. “Thinking with Images for Multimodal Reasoning: Foundations, Methods, and Future Frontiers.” arXiv:2506.23918, 2025.
30. Jianyuan Wang et al. “VGGT: Visual Geometry Grounded Transformer.” CVPR, pp. 5294–5306, 2025.
31. Yuxin Wang et al. “N3D-VLM: Native 3D Grounding Enables Accurate Spatial Reasoning in Vision-Language Models.” arXiv:2512.16561, 2025.
32. Yifan Wang et al. “Permutation-Equivariant Visual Geometry Learning.” arXiv:2507.13347, 2025.
33. Mingrui Wu et al. “From Indoor to Open World: Revealing the Spatial Reasoning Gap in MLLMs.” arXiv:2512.19683, 2025.
34. Jihan Yang et al. “Thinking in Space: How Multimodal Large Language Models See, Remember, and Recall Spaces.” CVPR, pp. 10632–10643, 2025.
35. Weichen Zhang et al. “The Point, the Vision and the Text: Does Point Cloud Boost Spatial Reasoning of Large Language Models?” arXiv:2504.04540, 2025.
36. Zaibin Zhang et al. “Think3D: Thinking with Space for Spatial Reasoning.” arXiv:2601.13029, 2026.

## Appendix / Supplementary Material Status

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> No appendix or supplementary section is present in the supplied six-page arXiv PDF. The document ends with Reference [36].

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 所提供的六页 arXiv PDF 不含附录或补充材料章节；文档以参考文献 [36] 结束。

## Critical Reading Notes

- World2Mind 的主要贡献是把外部 3D 重建结果压缩为 MFM/LLM 易读的 AST 与路径地图，并用三阶段链条显式处理视觉与重建证据的冲突；它不是新的端到端空间基础模型。
- 表 1 显示增益并非处处为正：GPT-5.2 的 Object Count、Absolute Distance、Object Size 下降，Gemini-3-Pro 的 Object Size 也下降。因此“稳定提升”更准确地指平均分及多数强依赖 allocentric prior 的子任务，而不是每个子任务都单调改善。
- “blind”结果支持结构化几何文本本身具有强信息密度，但不能证明模型获得了内生空间认知：AST 由外部视觉几何与分割系统生成，能力仍依赖工具链质量。
- 论文仅报告两个 benchmark 的 Tiny 设置，且实验细节（样本规模、提示词模板、工具预算、运行成本与显著性分析）有限；结论的广泛泛化仍需更完整评测支持。
- 原文在 MindCube 段落写“Tab. 1”，但对应结果实际位于 Table 2；本 reader 按实际表号写为 Tab. 2，并在 `translation_notes.md` 记录。
