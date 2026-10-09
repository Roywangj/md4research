# World2Mind: Cognition Toolkit for Allocentric Spatial Reasoning in Foundation Models

## 文献信息 / Paper Metadata

- **Authors:** Shouwei Ruan, Bin Wang, Zhenyu Wu, Qihui Zhu, Yuxiang Zhang, Hang Su, Yubin Wang (corresponding author)
- **Affiliations:** Institute of Artificial Intelligence, Beihang University; Huawei Noah’s Ark Lab; Department of Computer Science and Technology, Institute for AI, Tsinghua-Bosch Joint ML Center, THBI Lab, BNRist Center, Tsinghua University
- **Source:** arXiv:2603.09774v1 [cs.AI], 10 March 2026
- **Source length:** 6 pages
- **Reader status:** Complete bilingual reader of all substantive source content. Because this is a strict one-file deliverable, no local figure assets or image links are included; all three figure captions, the substantive text visible in Figures 1 and 3, and both tables are retained in searchable form.
- **Reference policy:** References are retained in their original searchable bibliographic form. They are not translated because names, titles, venues, URLs, and arXiv identifiers function as lookup literals.

## 章节索引 / Section Index

1. Abstract
2. Introduction
3. Method Overview
   - 2.1 Geometry-Semantic Alignment Pipeline
   - 2.2 Allocentric Cognitive Mapping
   - 2.3 Geometry-Semantics Interwoven Reasoning
4. Experiment
   - 3.1 Experimental Setup
   - 3.2 Main Results and Analysis
   - 3.3 Ablation and Case Study
5. References

## 术语表 / Terminology Ledger

| English term | 中文译法 | Note |
|---|---|---|
| Multimodal Foundation Model (MFM) | 多模态基础模型 | 保留缩写 MFM/MFMs |
| allocentric | 非自我中心的 / 异中心的 | 相对于 egocentric；本文主要译作“非自我中心” |
| egocentric | 自我中心的 | 以观察者当前视角为参照 |
| Biological Intelligence (BI) | 生物智能 | 保留缩写 BI |
| spatial cognitive map | 空间认知地图 | 世界的结构化空间表征 |
| Allocentric-Spatial Tree (AST) | 非自我中心空间树 | 保留缩写 AST |
| Landmark Cognitive Map | 地标认知地图 | 面向物体拓扑与几何属性 |
| Route Cognitive Map | 路线认知地图 | 面向可通行性与轨迹 |
| geometry-semantics interwoven reasoning | 几何—语义交织推理 | 三阶段推理链 |
| modality-decoupled cue collection | 模态解耦线索收集 | 各模态独立取证以避免早期偏置 |

# Abstract / 摘要

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Achieving robust spatial reasoning remains a fundamental challenge for current Multimodal Foundation Models (MFMs). Existing methods either overfit statistical shortcuts via 3D grounding data or remain confined to 2D visual perception, limiting both spatial reasoning accuracy and generalization in unseen scenarios. Inspired by the spatial cognitive mapping mechanisms of biological intelligence, we propose **World2Mind**, a training-free spatial intelligence toolkit. At its core, World2Mind leverages 3D reconstruction and instance segmentation models to construct structured spatial cognitive maps, empowering MFMs to proactively acquire targeted spatial knowledge regarding interested landmarks and routes of interest. To provide robust geometric-topological priors, World2Mind synthesizes an **Allocentric-Spatial Tree (AST)** that uses elliptical parameters to model the top-down layout of landmarks accurately. To mitigate the inherent inaccuracies of 3D reconstruction, we introduce a three-stage reasoning chain comprising tool invocation assessment, modality-decoupled cue collection, and geometry-semantics interwoven reasoning. Extensive experiments demonstrate that World2Mind boosts the performance of frontier models, such as GPT-5.2, by 5%–18%. Astonishingly, relying solely on the AST-structured text, purely text-only foundation models can perform complex 3D spatial reasoning, achieving performance approaching that of advanced multimodal models.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 对当前多模态基础模型（MFMs）而言，实现稳健的空间推理仍是一项根本性挑战。现有方法要么通过 3D grounding 数据过拟合统计捷径，要么仍局限于二维视觉感知，从而同时限制了空间推理的准确性及其在未见场景中的泛化能力。受生物智能空间认知制图机制启发，我们提出 **World2Mind**，一种无需训练的空间智能工具包。World2Mind 的核心是利用 3D 重建与实例分割模型构建结构化空间认知地图，使 MFM 能够主动获取与目标地标和关注路线有关的定向空间知识。为提供稳健的几何—拓扑先验，World2Mind 构建了**非自我中心空间树（AST）**，使用椭圆参数准确建模地标的俯视布局。为缓解 3D 重建固有的不准确性，我们引入一条由工具调用评估、模态解耦线索收集以及几何—语义交织推理构成的三阶段推理链。大量实验表明，World2Mind 可将 GPT-5.2 等前沿模型的性能提升 5%–18%。令人惊讶的是，仅依赖 AST 的结构化文本，纯文本基础模型也能执行复杂的 3D 空间推理，其性能接近先进多模态模型。

# 1. Introduction / 引言

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Although multimodal foundation models (MFMs) [1, 12, 24, 28] excel in general visual understanding and cross-modal reasoning [29], they struggle significantly in embodied AI and complex spatial reasoning tasks requiring physical interaction [15, 17, 18, 26, 34]. This deficiency stems from their over-reliance on egocentric observations and lacking the capacity to abstract global spatial topology [18, 34], trapping MFMs in an insurmountable “semantic-geometry gap” in tasks like distance estimation, viewpoint transformation, and path planning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 尽管多模态基础模型（MFMs）[1, 12, 24, 28] 擅长通用视觉理解和跨模态推理 [29]，但在需要物理交互的具身 AI 与复杂空间推理任务中仍面临显著困难 [15, 17, 18, 26, 34]。这一缺陷源于模型过度依赖自我中心观察，并且缺乏抽象全局空间拓扑的能力 [18, 34]，使 MFM 在距离估计、视角变换和路径规划等任务中陷入难以逾越的“语义—几何鸿沟”。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Current efforts to enhance MFMs’ spatial reasoning primarily follow two paradigms. Training-based methods [6, 9, 20] fine-tune models on massive 3D-grounded QA pairs. However, this forces models to overfit statistical shortcuts [14, 25] rather than acquiring genuine spatial cognition, leading to poor generalization in out-of-distribution scenarios [33]. Alternatively, introducing explicit 3D modalities [7, 10, 21, 31] exacerbates inter-modal alignment challenges [35]. Meanwhile, recent tool-based methods [8, 19, 36] rely on active rendering under large-scale 3D reconstruction. These are severely bottlenecked by reconstruction quality and remain tethered to low-level visual perception, failing to abstract geometric data into structured semantics for high-level logical reasoning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 当前增强 MFM 空间推理的工作主要遵循两种范式。基于训练的方法 [6, 9, 20] 使用海量具有 3D grounding 的问答对微调模型。然而，这会迫使模型过拟合统计捷径 [14, 25]，而非获得真正的空间认知，导致其在分布外场景中泛化不佳 [33]。另一条路线引入显式 3D 模态 [7, 10, 21, 31]，却加剧了模态间对齐挑战 [35]。与此同时，近期基于工具的方法 [8, 19, 36] 依赖大规模 3D 重建下的主动渲染。这些方法受到重建质量的严重制约，且仍束缚于低层视觉感知，无法将几何数据抽象为可支持高层逻辑推理的结构化语义。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Biological Intelligence (BI) offers an ideal blueprint to break the shackles of egocentric observation. Rather than reacting passively to transient visual inputs, the biological brain intrinsically transforms egocentric views into an allocentric perspective [4]. Supported by place cells in the hippocampus [3, 11, 22] and grid cells in the entorhinal cortex [13], mammals construct a global cognitive map entirely independent of their egocentric viewpoint [23, 27]. This map forms the cornerstone for strategic mental simulation and advanced reasoning [2].

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 生物智能（BI）为摆脱自我中心观察的束缚提供了理想蓝图。生物大脑并非被动响应短暂的视觉输入，而是内在地将自我中心视图转化为非自我中心视角 [4]。在海马体位置细胞 [3, 11, 22] 与内嗅皮层网格细胞 [13] 的支持下，哺乳动物构建出完全独立于自身当前视角的全局认知地图 [23, 27]。该地图构成战略性心理模拟与高级推理的基石 [2]。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> To bridge this gap between foundation models and BI in spatial representation and reasoning, we propose **World2Mind**, a plug-and-play spatial cognition toolkit that equips models with human-like mental simulation capabilities. World2Mind integrates an efficient geometry-semantics alignment pipeline, leveraging pre-trained visual geometry [16, 30, 32] and instance segmentation models [5] to extract semantic voxel grids. From these, it constructs two core representations: 1) a Route Cognitive Map for passability prediction, and 2) a Landmark Cognitive Map for object topology. Encapsulated as an accessible toolset, World2Mind enables models to dynamically specify parameters (e.g., instances of interest, required spatial knowledge, and map visualizations) to proactively acquire targeted allocentric spatial knowledge on demand.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 为弥合基础模型与 BI 在空间表征和推理方面的差距，我们提出即插即用的空间认知工具包 **World2Mind**，赋予模型类人的心理模拟能力。World2Mind 集成了一条高效的几何—语义对齐流水线，利用预训练视觉几何模型 [16, 30, 32] 和实例分割模型 [5] 提取语义体素网格，并由此构建两种核心表征：1）用于预测可通行性的路线认知地图；2）用于表示物体拓扑的地标认知地图。World2Mind 被封装为易用工具集，使模型能够动态指定参数（例如感兴趣实例、所需空间知识和地图可视化），从而按需主动获取定向的非自我中心空间知识。

### Figure 1. World2Mind 总览 / Overview of World2Mind

**Searchable figure transcription:** Ego-Centric Input: video or multi-view images; spatial-related question: “Measuring from the closest point of each object, what is the distance between the door and the telephone (in meters)?” Step 1, Tool Invocation Judgment: “I need use the world2mind tool to get precise spatial measurements between these objects.” Step 2, Modality-Decoupled Cue Collection: visual clues and map clues including `telephone_01 <Center: (-3.187, -0.371), Width: 0.109>`. Step 3, Geometry-Semantics Interwoven Reasoning: shortest Euclidean distance between `telephone_01` and `door_02`; `Distance = (Minimum X of door_02) - (Maximum X of telephone_01) = 0.507 - (-3.1325) = 3.6395 meters`; answer `3.64m`, ground truth `3.8m`. Tool parameters include instances of interest, map type (`Landmark` or `Route`), and whether to return visualization. The pipeline uses Depth Anything V3 and Segment Anything V3 to produce a point cloud and semantic grid, followed by projecting and rendering Landmark/Route Cognitive Maps.

**Caption:** Figure 1. **Overview of foundation models performing allocentric spatial reasoning via the proposed World2Mind toolkit.** Given egocentric video or multi-view observations, the model first assesses the necessity of tool invocation and subsequently passes key parameters (e.g., instances of interest) to World2Mind to drive the generation of spatial cognitive maps. World2Mind integrates an efficient pipeline for 3D reconstruction and semantic-geometry alignment, returning the required structured spatial knowledge through targeted projection and rendering mechanisms. Furthermore, the model conducts geometry-semantics interwoven reasoning based on both the raw visual observations and the geometric cues provided by World2Mind, ultimately yielding highly reliable answers.

**Caption[CN]:** 图 1. **基础模型通过所提出的 World2Mind 工具包执行非自我中心空间推理的总览。** 给定自我中心视频或多视图观察，模型首先评估调用工具的必要性，随后将关键参数（例如感兴趣实例）传递给 World2Mind，以驱动空间认知地图的生成。World2Mind 集成了一条高效的 3D 重建与语义—几何对齐流水线，通过定向投影和渲染机制返回所需的结构化空间知识。此外，模型基于原始视觉观察与 World2Mind 提供的几何线索开展几何—语义交织推理，最终得到高度可靠的答案。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> To provide robust geometric-topological priors, we formally define the Allocentric-Spatial Tree (AST) as the core spatial representation in World2Mind. The AST is a directed acyclic graph utilizing geometrically stable landmarks (e.g., beds, tables) as core nodes to hierarchically associate surrounding smaller instances. Crucially, to approximate the fuzzy nature of human cognition, the AST models spatial footprints using rectangle-elliptical parameters (bounding boxes, major/minor axes, eccentricity, and rotation angles). These designs equip models with robust, dense, and highly actionable geometric-topological priors.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 为提供稳健的几何—拓扑先验，我们将非自我中心空间树（AST）正式定义为 World2Mind 的核心空间表征。AST 是一种有向无环图，它将几何上稳定的地标（例如床、桌子）用作核心节点，并分层关联其周围较小的实例。关键的是，为近似人类认知的模糊特性，AST 使用矩形—椭圆参数（边界框、长/短轴、偏心率和旋转角）建模空间占用范围。这些设计为模型提供了稳健、稠密且高度可操作的几何—拓扑先验。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> However, merely offering spatial representation is insufficient to guarantee robust reasoning. In complex physical scenarios, reconstruction quality often suffers severe corruption due to occlusions or restricted viewpoints, leading to conflicts with objective geometric laws and raw visual observations. To mitigate this risk, we integrate a rigorous spatial reasoning chain into World2Mind: 1) Difficulty Assessment and Tool Invocation, preventing over-computation on simple superficial queries; 2) Modality-Decoupled Cue Collection, independently extracting information from egocentric vision, AST structured text, and map visualizations; and 3) Geometry-Semantics Interwoven Reasoning, guiding the model to resolve cross-modal conflicts proactively and ultimately yield reliable spatial decisions.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 然而，仅提供空间表征并不足以保证稳健推理。在复杂物理场景中，遮挡或受限视角往往会严重破坏重建质量，进而导致重建结果与客观几何规律及原始视觉观察相冲突。为降低这一风险，我们将一条严格的空间推理链集成进 World2Mind：1）难度评估与工具调用，避免对简单表层问题进行过量计算；2）模态解耦线索收集，分别从自我中心视觉、AST 结构化文本和地图可视化中独立提取信息；3）几何—语义交织推理，引导模型主动解决跨模态冲突并最终做出可靠的空间决策。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Extensive evaluations across various spatial reasoning benchmarks demonstrate that World2Mind yields stable performance improvements of 6%–18% for frontier models like GPT-5.2, while maintaining exceptional efficiency and reasoning interpretability. Astonishingly, leveraging the pure, high-density allocentric priors provided by the AST, text-only foundation models can execute complex 3D reasoning directly within their parameter space simply by reading the AST representation, approaching the performance of advanced multimodal models. Our findings offer a highly promising pathway to overcome the spatial cognition bottleneck in foundation models.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 在多种空间推理基准上的广泛评测表明，World2Mind 能为 GPT-5.2 等前沿模型带来稳定的 6%–18% 性能提升，同时保持出色的效率和推理可解释性。令人惊讶的是，借助 AST 提供的纯净、高密度非自我中心先验，纯文本基础模型仅需读取 AST 表征，便可直接在其参数空间内执行复杂 3D 推理，性能接近先进多模态模型。我们的发现为突破基础模型的空间认知瓶颈提供了一条非常有前景的路径。

# 2. Method Overview / 方法概览

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This section details the technical overview of the proposed World2Mind, as illustrated in Fig. 1.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本节详细介绍所提出 World2Mind 的技术概览，如图 1 所示。

## 2.1. Geometry-Semantic Alignment Pipeline / 几何—语义对齐流水线

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Given an egocentric video sequence or multi-view image set $\{I_t\}_{t=1}^{T}$, our primary objective is to transcend the limitations of 2D vision and construct a robust 3D semantic representation of the physical world.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 给定自我中心视频序列或多视图图像集合 $\{I_t\}_{t=1}^{T}$，我们的首要目标是超越二维视觉的局限，构建物理世界的稳健 3D 语义表征。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **❶ Depth Estimation & Semantic Extraction.** We employ Depth Anything V3 [16] for monocular depth estimation, obtaining the depth map $D_t \in \mathbb{R}^{H\times W}$ and camera pose $T_t \in SE(3)$. Concurrently, we utilize SAM3 [5] to extract open-vocabulary semantic masks $M_t$ based on a user-specified category list $C$. To suppress the accumulation of long-tail errors inherent in depth estimation, we introduce a dual-level filtering mechanism based on the predicted confidence map $C_t \in [0,1]^{H\times W}$. Specifically, we formulate a binary validity mask $V_t \in \{0,1\}^{H\times W}$ as follows:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **❶ 深度估计与语义提取。** 我们采用 Depth Anything V3 [16] 进行单目深度估计，得到深度图 $D_t \in \mathbb{R}^{H\times W}$ 和相机位姿 $T_t \in SE(3)$。与此同时，我们使用 SAM3 [5]，根据用户指定的类别列表 $C$ 提取开放词汇语义掩码 $M_t$。为抑制深度估计固有长尾误差的累积，我们基于预测置信图 $C_t \in [0,1]^{H\times W}$ 引入双层过滤机制。具体而言，二值有效性掩码 $V_t \in \{0,1\}^{H\times W}$ 定义如下：

$$
V_t(u,v)=\mathbb{I}\big(C_t(u,v)>\tau_{\mathrm{pixel}}\big)\cdot\mathbb{I}\big(\mu_t>\tau_{\mathrm{frame}}\big). \tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Here $\mu_t=\frac{1}{HW}\sum_{x=1}^{H}\sum_{y=1}^{W} C_t(x,y)$ denotes the global spatial confidence of frame $t$, and $\mathbb{I}(\cdot)$ is the indicator function that returns 1 if the condition is met and 0 otherwise. The variables $\tau_{\mathrm{pixel}}$ and $\tau_{\mathrm{frame}}$ represent the pixel-level and frame-level thresholds, respectively. A pixel is incorporated into the subsequent reconstruction only when $V_t(u,v)=1$.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 其中，$\mu_t=\frac{1}{HW}\sum_{x=1}^{H}\sum_{y=1}^{W} C_t(x,y)$ 表示第 $t$ 帧的全局空间置信度，$\mathbb{I}(\cdot)$ 是指示函数：条件满足时返回 1，否则返回 0。变量 $\tau_{\mathrm{pixel}}$ 和 $\tau_{\mathrm{frame}}$ 分别表示像素级与帧级阈值。仅当 $V_t(u,v)=1$ 时，相应像素才会被纳入后续重建。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **❷ Point Cloud Mapping & Density Filtering.** Qualifying 2D pixels are back-projected into the world coordinate system via the camera intrinsic matrix $K$, generating a global point cloud $P=\{(p_i,s_i,\mathrm{rgb}_i)\}_{i=1}^{M}$ carrying semantic labels $s_i\in C$. Addressing the boundary outliers inherent in depth estimation, we propose a core region extraction strategy: for each point, we calculate its $K$-nearest-neighbor local density $\rho_i=\frac{1}{K}\sum_{j\in\mathcal{N}_K(i)}\lVert p_i-p_j\rVert^{-1}$, and eliminate low-density “tail” points based on density percentiles. This yields an exceptionally pure geometry-semantic substrate.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **❷ 点云映射与密度过滤。** 符合条件的二维像素通过相机内参矩阵 $K$ 反投影到世界坐标系中，生成携带语义标签 $s_i\in C$ 的全局点云 $P=\{(p_i,s_i,\mathrm{rgb}_i)\}_{i=1}^{M}$。针对深度估计固有的边界离群点，我们提出核心区域提取策略：对每个点计算其 $K$ 近邻局部密度 $\rho_i=\frac{1}{K}\sum_{j\in\mathcal{N}_K(i)}\lVert p_i-p_j\rVert^{-1}$，再依据密度百分位去除低密度“尾部”点。由此可获得极为纯净的几何—语义基底。

## 2.2. Allocentric Cognitive Mapping / 非自我中心认知制图

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Inspired by the spatial mapping mechanisms of BI, we distill the unstructured point cloud into two highly abstract cognitive maps, enabling the model to proactively acquire spatial knowledge on demand via tool invocation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 受 BI 空间制图机制启发，我们将非结构化点云提炼为两种高度抽象的认知地图，使模型能够通过工具调用按需主动获取空间知识。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **❶ Landmark Cognitive Mapping.** Traditional methods rely on ambiguous relative relations or simplified grid representation [18, 34]. To overcome this, we formally define the **Allocentric-Spatial Tree (AST)**, which reorganizes spatial entities as a directed acyclic graph within an absolute coordinate system. Specifically, we perform adaptive DBSCAN clustering on each semantic category within the point cloud to separate distinct instances. For each instance node, the AST discards traditional bounding boxes and instead fits a minimum bounding ellipse in the top-down view (X-Z plane), extracting the centroid $(x_c,z_c)$, major and minor axes $a$ and $b$, and rotation angle $\theta$. This parameterization: 1) significantly enhances robustness against reconstruction boundary noise; 2) perfectly aligns with the fuzzy probability nature of human spatial footprint perception. Output as dense structured text (e.g., YAML), the AST explicitly encodes hierarchical containment relationships among entities along with multi-dimensional geometric attributes.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **❶ 地标认知制图。** 传统方法依赖含糊的相对关系或简化的网格表征 [18, 34]。为克服这一问题，我们正式定义了**非自我中心空间树（AST）**，它在绝对坐标系中将空间实体重组为有向无环图。具体而言，我们对点云中的每个语义类别执行自适应 DBSCAN 聚类，以分离不同实例。对于每个实例节点，AST 放弃传统边界框，转而在俯视图（X-Z 平面）中拟合最小外接椭圆，提取质心 $(x_c,z_c)$、长短轴 $a$ 和 $b$ 以及旋转角 $\theta$。该参数化方式：1）显著增强了对重建边界噪声的稳健性；2）与人类对空间占用范围感知所具有的模糊概率特性高度一致。AST 以稠密结构化文本（例如 YAML）输出，显式编码实体之间的分层包含关系和多维几何属性。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **❷ Route Cognitive Mapping.** For navigation-oriented tasks, World2Mind also enables extracting the masks of traversable categories (e.g., floors), back-projects and voxelizes them, and subsequently partitions them into an $N\times N$ grid map on the top-down plane. Combined with the mapping of the camera trajectory sequence $\{T_t\}$, this route map provides the model with explicit priors regarding passability and the human observer’s motion trajectory.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **❷ 路线认知制图。** 对于面向导航的任务，World2Mind 还可提取可通行类别（例如地面）的掩码，对其进行反投影与体素化，随后在俯视平面上划分为 $N\times N$ 网格地图。结合相机轨迹序列 $\{T_t\}$ 的映射，该路线地图向模型提供有关可通行性及人类观察者运动轨迹的显式先验。

## 2.3. Geometry-Semantics Interwoven Reasoning / 几何—语义交织推理

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In physical scenarios, 2D visual observations are susceptible to occlusions and adverse viewpoints, while 3D reconstruction information may contain local errors. To resolve potential contradictions between these two modalities, we design a rigorous three-stage interwoven reasoning chain.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在物理场景中，二维视觉观察容易受到遮挡和不利视角影响，而 3D 重建信息又可能包含局部误差。为解决这两种模态之间潜在的矛盾，我们设计了一条严格的三阶段交织推理链。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Stage 1: Tool Invocation Judgement.** To reduce unnecessary computational overhead, the model must first evaluate the spatial relevance of the query. The model should proactively invoke World2Mind only when the task explicitly involves spatial reasoning, such as occlusion inference, distance estimation, or path planning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **阶段 1：工具调用判断。** 为减少不必要的计算开销，模型必须首先评估查询与空间的相关性。只有当任务明确涉及空间推理（例如遮挡推断、距离估计或路径规划）时，模型才应主动调用 World2Mind。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Stage 2: Modality-Decoupled Cue Collection.** We force the model to extract information independently to prevent early modality bias. The model must simultaneously gather corroborating evidence from three independent sources: egocentric vision, the AST text returned by World2Mind, and optional 2D top-down map visualizations.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **阶段 2：模态解耦线索收集。** 我们强制模型独立提取信息，以避免早期模态偏置。模型必须同时从三个独立来源收集能够相互印证的证据：自我中心视觉、World2Mind 返回的 AST 文本，以及可选的二维俯视地图可视化。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Stage 3: Conflict Resolution and Cross-Validation.** This is the crux of the reasoning chain. The model needs to proactively coordinate evidence across different modalities and identify cross-modal conflicts, such as missing objects due to visual truncation or coordinate drift caused by depth errors. By cross-validating the objective geometric parameters of the AST against subjective visual appearances, the model can dynamically weigh the credibility between visual illusions and reconstruction artifacts, ultimately outputting highly reliable and logically interpretable decisions.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **阶段 3：冲突消解与交叉验证。** 这是推理链的核心。模型需要主动协调不同模态的证据，并识别跨模态冲突，例如因视觉截断造成的物体缺失，或因深度误差引起的坐标漂移。通过将 AST 的客观几何参数与主观视觉外观进行交叉验证，模型可以动态权衡视觉错觉与重建伪影的可信度，最终输出高度可靠且逻辑可解释的决策。

# 3. Experiment / 实验

## 3.1. Experimental Setup / 实验设置

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We conduct evaluations on two challenging spatial reasoning benchmarks: VSI-Bench [34], which focuses on video-based reasoning in real-world physical scenes, and MindCube [18], which emphasizes multi-view cognitive mapping and mental simulation. Our evaluation primarily targets the most frontier multimodal foundation models, including GPT, Claude, and Gemini, given their exceptional proficiency in tool invocation and instruction-following.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们在两个具有挑战性的空间推理基准上开展评测：VSI-Bench [34] 聚焦真实物理场景中的视频推理；MindCube [18] 强调多视图认知制图与心理模拟。鉴于 GPT、Claude 和 Gemini 在工具调用及指令遵循方面表现出色，我们的评测主要面向这些最前沿的多模态基础模型。

## 3.2. Main Results and Analysis / 主要结果与分析

### Table 1. VSI-Bench（Tiny 子集）主要结果 / Main results on VSI-Bench (Tiny subset)

**Caption:** Table 1. **Main results on the VSI-Bench [34] benchmark (Tiny subset).**

**Caption[CN]:** 表 1. **VSI-Bench [34] 基准（Tiny 子集）上的主要结果。**

| Setting | Models | Avg. | Obj. Count | Abs. Dist. | Obj. Size | Room Size | Rel. Dist. | Rel. Dir. | Route Plan | Appr. Order |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| w/o World2Mind | GPT-5.2 | 46.7 | 52.5 | 34.9 | 67.5 | 50.6 | 42.0 | 40.7 | 34.7 | 51.0 |
| w/o World2Mind | Claude-4.6-Opus | 38.4 | 46.9 | 18.5 | 62.1 | 26.8 | 40.0 | 47.2 | 34.7 | 30.6 |
| w/o World2Mind | Gemini-3-Pro | 55.2 | 47.8 | 32.1 | **71.3** | 55.0 | 54.0 | 44.8 | 57.1 | 79.6 |
| w/ World2Mind | GPT-5.2 | 54.0 (↑7.3) | 47.4 (↓5.1) | 33.4 (↓1.5) | 63.3 (↓4.2) | 52.4 (↑1.8) | **64.0 (↑22.0)** | 41.1 (↑0.4) | 51.0 (↑16.3) | 79.6 (↑28.6) |
| w/ World2Mind | Claude-4.6-Opus | 56.0 (↑17.7) | **59.0 (↑12.0)** | 34.3 (↑15.8) | 67.3 (↑5.2) | 54.8 (↑28.0) | **64.0 (↑24.0)** | 62.7 (↑15.6) | **65.3 (↑30.6)** | 40.8 (↑10.2) |
| w/ World2Mind | Gemini-3-Pro | **61.0 (↑5.8)** | 51.8 (↑4.1) | **36.8 (↑4.7)** | 57.7 (↓13.5) | **62.6 (↑7.6)** | 62.0 (↑8.0) | **67.7 (↑22.9)** | **65.3 (↑8.2)** | **83.7 (↑4.1)** |

*Numerical Answer (%): Obj. Count, Abs. Dist., Obj. Size, Room Size. Multiple-Choice Answer (%): Rel. Dist., Rel. Dir., Route Plan, Appr. Order.*

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Evaluation on VSI-Bench.** As shown in Tab. 1, the seamless integration of World2Mind yields a substantial leap in the average performance (Avg.) across all frontier models. Specifically, GPT-5.2 achieves a 7.3% improvement, while Claude-4.6-Opus achieves a staggering 17.7% improvement. In-depth analysis of the subtasks reveals that the performance gains are most striking in task categories that rely heavily on allocentric priors. For instance, on Relative Direction, Route Planning, and Relative Distance, the performance of Claude-4.6-Opus skyrockets by 15.6%, 30.6%, and 24.0%, respectively. This compellingly demonstrates the critical role of the allocentric spatial knowledge provided by World2Mind in bridging the spatial reasoning gap.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **VSI-Bench 评测。** 如表 1 所示，无缝集成 World2Mind 后，所有前沿模型的平均性能（Avg.）均显著跃升。具体而言，GPT-5.2 提升 7.3%，Claude-4.6-Opus 则大幅提升 17.7%。对子任务的深入分析表明，性能增益在高度依赖非自我中心先验的任务类别中最为显著。例如，在相对方向、路线规划和相对距离任务上，Claude-4.6-Opus 的性能分别飙升 15.6%、30.6% 和 24.0%。这有力证明了 World2Mind 提供的非自我中心空间知识在弥合空间推理鸿沟方面的关键作用。

### Table 2. MindCube-Tiny 结果 / Results on MindCube-Tiny

**Caption:** Table 2. **Results on the MindCube-Tiny [18] benchmark.**

**Caption[CN]:** 表 2. **MindCube-Tiny [18] 基准上的结果。**

| Setting | Models | Avg. | Around | Among | Rotation |
|---|---|---:|---:|---:|---:|
| w/o World2Mind | GPT-5.2 | 49.9 | 62.4 | 45.2 | 48.5 |
| w/o World2Mind | Claude-4.6-Opus | 48.5 | 58.8 | 50.7 | 29.0 |
| w/o World2Mind | Gemini-3-Pro | 75.1 | 77.2 | 68.2 | 93.0 |
| w/ World2Mind | GPT-5.2 | 54.6 (↑4.7) | 60.4 (↓2.0) | 47.7 (↑2.5) | 68.0 (↑19.5) |
| w/ World2Mind | Claude-4.6-Opus | 62.9 (↑14.4) | 82.4 (↑23.6) | 60.8 (↑10.1) | 45.0 (↑16.0) |
| w/ World2Mind | Gemini-3-Pro | **81.6 (↑6.5)** | **86.0 (↑8.8)** | **75.8 (↑7.6)** | **93.5 (↑0.5)** |

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Evaluation on MindCube.** The results in Tab. 2 further corroborate the universality and robustness of our framework in sparse multi-view inputs. Even for Gemini-3-Pro, whose native spatial reasoning capability is already top-tier (with a baseline Avg. of 75.1%), World2Mind successfully shatters its performance ceiling, pushing its average accuracy to 81.6% (+6.5%). Notably, in tasks like “Rotation” that severely test 3D spatial imagination, the model achieves a remarkable performance breakthrough (GPT-5.2 improves by 19.5%) due to its ability to perform logical deduction grounded in the AST.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **MindCube 评测。** 表 2 的结果进一步证实了我们的框架在稀疏多视图输入下具有普适性与稳健性。即便 Gemini-3-Pro 原生空间推理能力已处于顶尖水平（基线 Avg. 为 75.1%），World2Mind 仍成功突破其性能上限，将平均准确率推至 81.6%（+6.5%）。值得注意的是，在“Rotation”这类严格考验 3D 空间想象的任务中，模型凭借基于 AST 进行逻辑推演的能力取得显著突破（GPT-5.2 提升 19.5%）。

## 3.3. Ablation and Case Study / 消融实验与案例研究

### Figure 2. 纯文本（“blind”）设置下的性能比较 / Performance under the text-only (“blind”) setting

**Caption:** Figure 2. **Performance comparison under the text-only model (“blind”) setting.** We report the performance gap on the VSI-Bench (Tiny subset) between foundation models relying solely on commonsense reasoning and those leveraging World2Mind to acquire structured spatial knowledge for allocentric reasoning.

**Caption[CN]:** 图 2. **纯文本模型（“blind”）设置下的性能比较。** 我们报告 VSI-Bench（Tiny 子集）上两类基础模型之间的性能差距：一类仅依赖常识推理，另一类利用 World2Mind 获取用于非自我中心推理的结构化空间知识。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> To explore the limits of how structured text of AST empowers the spatial cognition of large language models, we follow [34] to conduct ablation studies under the text-only (“blind”) setting (see Fig. 2). When visual image inputs are completely stripped away, foundation models that rely solely on commonsense priors degrade to near-random guessing on spatial tasks. Astonishingly, however, when equipped with World2Mind, both GPT-5.2 and Claude-4.6-Opus exhibit a remarkable performance rebound in the “blind” state. On core reasoning tasks such as Object Size and Route Planning, their scores closely approach those achieved with full visual inputs. This profound finding indicates that pure, high-quality allocentric geometric priors are entirely sufficient to ignite powerful 3D mental reconstruction and simulation capabilities of foundation models under text-based reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 为探索 AST 结构化文本赋能大语言模型空间认知的能力边界，我们遵循 [34]，在纯文本（“blind”）设置下开展消融研究（见图 2）。当视觉图像输入被完全移除时，仅依赖常识先验的基础模型在空间任务上的表现下降到接近随机猜测。然而令人惊讶的是，配备 World2Mind 后，GPT-5.2 和 Claude-4.6-Opus 在“blind”状态下均出现显著的性能回升。在物体大小和路线规划等核心推理任务上，其得分接近使用完整视觉输入时的水平。这一深刻发现表明，纯净、高质量的非自我中心几何先验完全足以在基于文本的推理中激活基础模型强大的 3D 心理重建与模拟能力。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Furthermore, we visualize the complete reasoning traces powered by World2Mind in Fig. 3, which clearly demonstrate that the interwoven reasoning process exhibits exceptional robustness and logical interpretability when resolving cross-modal conflicts.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 此外，我们在图 3 中可视化了由 World2Mind 驱动的完整推理轨迹；该轨迹清楚表明，交织推理过程在解决跨模态冲突时展现出出色的稳健性与逻辑可解释性。

### Figure 3. World2Mind 完整推理轨迹 / Complete reasoning trace under World2Mind

**Searchable figure transcription:** Question: `What is the longest length of the chair (in centimeters)?` Initial GPT-5.2 visual reasoning identifies a black office chair, estimates roughly `90–110 cm`, and requests metric estimation. Tool call: `world2mind`; arguments: `{ "categories": ["chair, desk"], "knowledge_type": "landmark" }`. Map clues report two chairs: `chair_01` has rectangle width `0.611 m`, footprint height `0.45 m`, and `Height_Range` from `1.093 m` to `1.628 m`, giving vertical extent approximately `0.535 m`; `chair_02` has width `0.12 m`, footprint height `0.329 m`, and `Height_Range` from `0.648 m` to `1.599 m`, giving vertical extent approximately `0.951 m`. The trace identifies `chair_02` as the most plausible longest dimension, converts `0.951 m = 95.1 cm`, calls `world2mind` again with `{ "visualization_type": "landmark_vis" }`, cross-validates the instance against the visualized office-chair region, and gives `Final Answer: 95 cm`.

**Caption:** Figure 3. **Complete reasoning trace under World2Mind.**

**Caption[CN]:** 图 3. **World2Mind 下的完整推理轨迹。**

# References / 参考文献

> References are preserved verbatim in searchable bibliographic form; citation-page indicators printed by the PDF layout are omitted because they are not part of the cited works.

[1] Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang Gao, Chunjiang Ge, et al. Qwen3-vl technical report. *arXiv preprint arXiv:2511.21631*, 2025.

[2] Jacob LS Bellmund, Peter Gärdenfors, Edvard I Moser, and Christian F Doeller. Navigating cognition: Spatial codes for human thinking. *Science*, 362(6415):eaat6766, 2018.

[3] Nicola J Broadbent, Larry R Squire, and Robert E Clark. Spatial memory, recognition memory, and the hippocampus. *Proceedings of the National Academy of Sciences*, 101(40):14515–14520, 2004.

[4] Neil Burgess. Spatial memory: how egocentric and allocentric combine. *Trends in Cognitive Sciences*, 10(12):551–557, 2006.

[5] Nicolas Carion, Laura Gustafson, Yuan-Ting Hu, Shoubhik Debnath, Ronghang Hu, Didac Suris, Chaitanya Ryali, Kalyan Vasudev Alwala, Haitham Khedr, Andrew Huang, et al. Sam 3: Segment anything with concepts. *arXiv preprint arXiv:2511.16719*, 2025.

[6] Boyuan Chen, Zhuo Xu, Sean Kirmani, Brain Ichter, Dorsa Sadigh, Leonidas Guibas, and Fei Xia. Spatialvlm: Endowing vision-language models with spatial reasoning capabilities. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pages 14455–14465, 2024.

[7] Pingyi Chen, Yujing Lou, Shen Cao, Jinhui Guo, Lubin Fan, Yue Wu, Lin Yang, Lizhuang Ma, and Jieping Ye. Sd-vlm: Spatial measuring and understanding with depth-encoded vision-language models. *arXiv preprint arXiv:2509.17664*, 2025.

[8] Siyi Chen, Mikaela Angelina Uy, Chan Hee Song, Faisal Ladhak, Adithyavairavan Murali, Qing Qu, Stan Birchfield, Valts Blukis, and Jonathan Tremblay. Spacetools: Tool-augmented spatial reasoning via double interactive rl. *arXiv preprint arXiv:2512.04069*, 2025.

[9] An-Chieh Cheng, Hongxu Yin, Yang Fu, Qiushan Guo, Ruihan Yang, Jan Kautz, Xiaolong Wang, and Sifei Liu. Spatial-rgpt: Grounded spatial reasoning in vision-language models. *Advances in Neural Information Processing Systems*, 37:135062–135093, 2024.

[10] Erik Daxberger, Nina Wenzel, David Griffiths, Haiming Gang, Justin Lazarow, Gefen Kohavi, Kai Kang, Marcin Eichner, Yinfei Yang, Afshin Dehghan, et al. Mm-spatial: Exploring 3d spatial understanding in multimodal llms. In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pages 7395–7408, 2025.

[11] Howard Eichenbaum. The role of the hippocampus in navigation is memory. *Journal of Neurophysiology*, 117(4):1785–1796, 2017.

[12] Google. Gemini 3.1 pro: Best for complex tasks and bringing creative concepts to life. https://deepmind.google/models/gemini/pro/, 2026.

[13] Torkel Hafting, Marianne Fyhn, Sturla Molden, May-Britt Moser, and Edvard I Moser. Microstructure of a spatial map in the entorhinal cortex. *Nature*, 436(7052):801–806, 2005.

[14] Jiaxin Huang, Ziwen Li, Hanlve Zhang, Runnan Chen, Xiao He, Yandong Guo, Wenping Wang, Tongliang Liu, and Mingming Gong. Surprise3d: A dataset for spatial understanding and reasoning in complex 3d scenes. *arXiv preprint arXiv:2507.07781*, 2025.

[15] Shuai Huang, Wenxuan Zhao, and Jun Gao. Si-bench: Benchmarking social intelligence of large language models in human-to-human conversations. *arXiv preprint arXiv:2510.23182*, 2025.

[16] Haotong Lin, Sili Chen, Junhao Liew, Donny Y Chen, Zhenyu Li, Guang Shi, Jiashi Feng, and Bingyi Kang. Depth anything 3: Recovering the visual space from any views. *arXiv preprint arXiv:2511.10647*, 2025.

[17] Jingli Lin, Runsen Xu, Shaohao Zhu, Sihan Yang, Peizhou Cao, Yunlong Ran, Miao Hu, Chenming Zhu, Yiman Xie, Yilin Long, et al. Mmsi-video-bench: A holistic benchmark for video-based spatial intelligence. *arXiv preprint arXiv:2512.10863*, 2025.

[18] Fangzheng Liu, Don Derek Haddad, and Joe Paradiso. Mindcube: an interactive device for gauging emotions. In *Adjunct Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology*, pages 1–2, 2024.

[19] Zhanpeng Luo, Ce Zhang, Silong Yong, Cunxi Dai, Qianwei Wang, Haoxi Ran, Guanya Shi, Katia Sycara, and Yaqi Xie. pyspatial: Generating 3d visual programs for zero-shot spatial reasoning. *arXiv preprint arXiv:2603.00905*, 2026.

[20] Wufei Ma, Yu-Cheng Chou, Qihao Liu, Xingrui Wang, Celso de Melo, Jianwen Xie, and Alan Yuille. Spatialreasoner: Towards explicit and generalizable 3d spatial reasoning. *arXiv preprint arXiv:2504.20024*, 2025.

[21] Zhenhua Ning, Zhuotao Tian, Shaoshuai Shi, Guangming Lu, Daojing He, Wenjie Pei, and Li Jiang. Enhancing spatial reasoning in multimodal large language models through reasoning-based segmentation. In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pages 7851–7860, 2025.

[22] John O’Keefe and Jonathan Dostrovsky. The hippocampus as a spatial map: preliminary evidence from unit activity in the freely-moving rat. *Brain Research*, 1971.

[23] John O’Keefe and Lynn Nadel. *The hippocampus as a cognitive map*. Oxford University Press, 1978.

[24] OpenAI. Gpt-4v(ision) system card. https://cdn.openai.com/papers/GPTV_System_Card.pdf, 2023.

[25] Jianing Qi, Jiawei Liu, Hao Tang, and Zhigang Zhu. Beyond semantics: Rediscovering spatial awareness in vision-language models. *arXiv preprint arXiv:2503.17349*, 2025.

[26] Santhosh Kumar Ramakrishnan, Erik Wijmans, Philipp Kraehenbuehl, and Vladlen Koltun. Does spatial cognition emerge in frontier models? *arXiv preprint arXiv:2410.06468*, 2024.

[27] Daniela Schiller, Howard Eichenbaum, Elizabeth A Buffalo, Lila Davachi, David J Foster, Stefan Leutgeb, and Charan Ranganath. Memory and space: towards an understanding of the cognitive map. *Journal of Neuroscience*, 35(41):13904–13911, 2015.

[28] Aaditya Singh, Adam Fry, Adam Perelman, Adam Tart, Adi Ganesh, Ahmed El-Kishky, Aidan McLaughlin, Aiden Low, AJ Ostrow, Akhila Ananthram, et al. Openai gpt-5 system card. *arXiv preprint arXiv:2601.03267*, 2025.

[29] Zhaochen Su, Peng Xia, Hangyu Guo, Zhenhua Liu, Yan Ma, Xiaoye Qu, Jiaqi Liu, Yanshu Li, Kaide Zeng, Zhengyuan Yang, et al. Thinking with images for multimodal reasoning: Foundations, methods, and future frontiers. *arXiv preprint arXiv:2506.23918*, 2025.

[30] Jianyuan Wang, Minghao Chen, Nikita Karaev, Andrea Vedaldi, Christian Rupprecht, and David Novotny. Vggt: Visual geometry grounded transformer. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, pages 5294–5306, 2025.

[31] Yuxin Wang, Lei Ke, Boqiang Zhang, Tianyuan Qu, Hanxun Yu, Zhenpeng Huang, Meng Yu, Dan Xu, and Dong Yu. N3d-vlm: Native 3d grounding enables accurate spatial reasoning in vision-language models. *arXiv preprint arXiv:2512.16561*, 2025.

[32] Yifan Wang, Jianjun Zhou, Haoyi Zhu, Wenzheng Chang, Yang Zhou, Zizun Li, Junyi Chen, Jiangmiao Pang, Chunhua Shen, and Tong He. Permutation-equivariant visual geometry learning. *arXiv preprint arXiv:2507.13347*, 2025.

[33] Mingrui Wu, Zhaozhi Wang, Fangjinhua Wang, Jiaolong Yang, Marc Pollefeys, and Tong Zhang. From indoor to open world: Revealing the spatial reasoning gap in mllms. *arXiv preprint arXiv:2512.19683*, 2025.

[34] Jihan Yang, Shusheng Yang, Anjali W Gupta, Rilyn Han, Li Fei-Fei, and Saining Xie. Thinking in space: How multimodal large language models see, remember, and recall spaces. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, pages 10632–10643, 2025.

[35] Weichen Zhang, Ruiying Peng, Chen Gao, Jianjie Fang, Xin Zeng, Kaiyuan Li, Ziyou Wang, Jinqiang Cui, Xin Wang, Xinlei Chen, et al. The point, the vision and the text: Does point cloud boost spatial reasoning of large language models? *arXiv preprint arXiv:2504.04540*, 2025.

[36] Zaibin Zhang, Yuhan Wu, Lianjie Jia, Yifan Wang, Zhongbo Zhang, Yijiang Li, Binghao Ran, Fuxi Zhang, Zhuohan Sun, Zhenfei Yin, et al. Think3d: Thinking with space for spatial reasoning. *arXiv preprint arXiv:2601.13029*, 2026.
