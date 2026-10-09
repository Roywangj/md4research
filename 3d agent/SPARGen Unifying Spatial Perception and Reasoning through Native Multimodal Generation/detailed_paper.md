---
tags:
  - papers/3d-agent
  - papers/spatial-perception
  - papers/spatial-reasoning
aliases:
  - SPARGen
  - Unifying Spatial Perception and Reasoning through Native Multimodal Generation
arxiv_id: 2608.14138
---

<!-- Page 1 -->

# SPARGen: Unifying Spatial Perception and Reasoning through Native Multimodal Generation

# SPARGen：通过原生多模态生成统一空间感知与推理

**Jinsheng Quan¹˒², Jianhua Li², Siyi Xie²˒³, Xuanke Shi², Kewang Deng², Zukai Chen², Feifei Shao¹, Lei Yang², Quan Wang²\*, Yawei Luo¹\***

**金圣全¹˒²，李建华²，谢思怡²˒³，史炫科²，邓科旺²，陈祖凯²，邵菲菲¹，杨磊²，王泉²\*，罗亚威¹\***

¹Zhejiang University  
²SenseTime Research  
³Peking University

¹浙江大学  
²商汤研究  
³北京大学

**arXiv:2608.14138v1 [cs.CV] 14 Aug 2026**

## Figure 1 — In-figure transcription

- **Input image tokens:** $I$
- **Input text tokens:** $T$
- **Output dense tokens:** $D$
- **Output sequence tokens:** $S$
- **SPARGen — One Unified Model, Native Generation**
- **Geometry:** Depth; Camera Pose; Point Map
- **Correspondence:** Temporal Optical Flow; Cross-view Optical Flow (Sampled)
- **Reasoning:** Understanding; Spatial Reasoning
- **Text instruction:** “Recover the scene’s depth, camera poses, point cloud, and optical flow, and describe its spatial layout.”
- **Understanding output:** “A red-hatted dwarf holding a lantern stands beside a wooden chest and a brown sofa in a brick-walled room.”
- **Spatial-reasoning question:** “If I were standing where the two single sofas are and facing forward in the same direction, what would be on the right side of the white table?”
- **Spatial-reasoning answer:** “The leather two-seater sofa.”

- **输入图像词元：** $I$
- **输入文本词元：** $T$
- **输出稠密词元：** $D$
- **输出序列词元：** $S$
- **SPARGen——一个统一模型，原生生成**
- **几何：** 深度；相机位姿；点图
- **对应关系：** 时序光流；跨视图光流（采样）
- **推理：** 理解；空间推理
- **文本指令：**“恢复场景的深度、相机位姿、点云和光流，并描述其空间布局。”
- **理解输出：**“一个戴红帽、手持灯笼的矮人站在一个木箱和一张棕色沙发旁边，房间有砖墙。”
- **空间推理问题：**“如果我站在两张单人沙发所在的位置，并朝相同方向向前看，那么白色桌子的右侧会有什么？”
- **空间推理答案：**“皮革双人沙发。”

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Figure 1: **SPARGen unifies spatial perception and reasoning through native multimodal generation.** Conditioned on visual observations and natural-language instructions, a single model generates dense geometric fields and token sequences for 3D reconstruction, correspondence estimation, visual understanding, and spatial reasoning, without task-specific modules.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 图1：**SPARGen 通过原生多模态生成统一空间感知与推理。** 在视觉观测和自然语言指令的条件约束下，单一模型无需任务专用模块，即可为三维重建、对应关系估计、视觉理解和空间推理生成稠密几何场与词元序列。

## Abstract

## 摘要

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Spatial perception and reasoning from visual observations require recovering geometric structure, establishing correspondences, and understanding spatial relations. Existing approaches typically address these capabilities separately using task-specific architectures or external geometric modules, limiting knowledge transfer among complementary representations of the same physical scene. We introduce SPARGen, a unified multimodal framework that casts 3D reconstruction, dense correspondence, and spatial reasoning as instruction-conditioned generation tasks. SPARGen serializes compact structured and linguistic outputs as token sequences while generating dense geometric fields in image-aligned forms, enabling spatial supervision to jointly shape shared representations within a native multimodal generative model. Experiments across benchmarks for 3D reconstruction, correspondence, and spatial reasoning show that SPARGen achieves competitive performance across heterogeneous spatial tasks within a single native multimodal generative framework.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 从视觉观测中进行空间感知与推理，需要恢复几何结构、建立对应关系并理解空间关系。现有方法通常使用任务专用架构或外部几何模块分别处理这些能力，从而限制了同一物理场景的互补表征之间的知识迁移。我们提出 SPARGen，这是一个统一的多模态框架，将三维重建、稠密对应关系和空间推理表述为以指令为条件的生成任务。SPARGen 将紧凑的结构化输出和语言输出序列化为词元序列，同时以图像对齐形式生成稠密几何场，使空间监督能够在原生多模态生成模型中共同塑造共享表征。三维重建、对应关系和空间推理基准上的实验表明，SPARGen 能够在单一原生多模态生成框架内，对异构空间任务取得有竞争力的性能。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> \*Corresponding author.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> \*通讯作者。

---

<!-- Page 2 -->

## 1 Introduction

## 1 引言

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Recovering the geometry of a 3D scene and reasoning about it are complementary capabilities for perceiving and interacting with the physical world. Recent advances have made substantial progress in geometric reconstruction (Wang et al. 2024a, 2025a; Lin et al. 2025a), correspondence estimation (Zhang et al. 2025c; Edstedt et al. 2024; Huang et al. 2022), and spatial reasoning (Chen et al. 2024a; Azuma et al. 2022; Ma et al. 2025). These capabilities play different but interconnected roles: reconstruction recovers scene structure, correspondence associates evidence across views or time, and reasoning converts spatial representations into task-relevant conclusions.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 恢复三维场景的几何结构并对其进行推理，是感知物理世界并与之交互的两种互补能力。近期研究在几何重建（Wang et al. 2024a, 2025a；Lin et al. 2025a）、对应关系估计（Zhang et al. 2025c；Edstedt et al. 2024；Huang et al. 2022）和空间推理（Chen et al. 2024a；Azuma et al. 2022；Ma et al. 2025）方面取得了显著进展。这些能力承担不同但相互关联的作用：重建恢复场景结构，对应关系关联跨视图或跨时间的证据，而推理则将空间表征转化为与任务相关的结论。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Unifying these capabilities is desirable because they provide complementary supervision for the same underlying physical scene. Depth, camera motion, point maps, and optical flow jointly characterize scene structure and its variation across observations, while spatial question answering requires abstracting such geometric evidence into semantic relations. Learning these tasks together therefore has the potential to promote knowledge transfer across tasks, improve the consistency of spatial predictions, and connect geometric scene understanding with high-level reasoning.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 统一这些能力是有益的，因为它们能够针对同一潜在物理场景提供互补监督。深度、相机运动、点图和光流共同刻画场景结构及其在不同观测之间的变化，而空间问答则要求将此类几何证据抽象为语义关系。因此，联合学习这些任务有望促进任务间的知识迁移、提高空间预测的一致性，并将几何场景理解与高层推理连接起来。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> However, existing approaches address only parts of this problem. Feed-forward geometry models provide accurate depth, point maps, camera poses, or correspondences, but generally do not support spatial question answering through the same model (Lin et al. 2025a; Wang et al. 2025b,d; Cong et al. 2026). Multimodal models offer flexible instruction following and spatial reasoning, yet typically receive limited supervision from dense geometry and correspondences (Huang et al. 2024; Chen et al. 2024b; Deng et al. 2025b). Recent unified models combine geometric perception with multimodal understanding, but often introduce geometry-specific encoders, regression heads, or external modules (Qi et al. 2024; Hu et al. 2026; Xu et al. 2025). Consequently, existing systems provide limited opportunities for dense geometric, correspondence, and semantic supervision to jointly shape shared spatial representations.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 然而，现有方法只解决了该问题的一部分。前馈几何模型能够提供准确的深度、点图、相机位姿或对应关系，但通常无法通过同一个模型支持空间问答（Lin et al. 2025a；Wang et al. 2025b,d；Cong et al. 2026）。多模态模型能够灵活地遵循指令并进行空间推理，但通常只能从稠密几何和对应关系中获得有限监督（Huang et al. 2024；Chen et al. 2024b；Deng et al. 2025b）。近期的统一模型将几何感知与多模态理解相结合，但往往引入几何专用编码器、回归头或外部模块（Qi et al. 2024；Hu et al. 2026；Xu et al. 2025）。因此，现有系统只能有限地让稠密几何、对应关系和语义监督共同塑造共享空间表征。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> In this paper, we present SPARGen, a unified framework for spatial perception and reasoning, as illustrated in Fig. 1. Our design is motivated by a simple view: spatial intelligence is not merely a collection of isolated tasks, but a process of constructing spatial representations from observations and using them to answer conditioned queries. Accordingly, SPARGen formulates geometric reconstruction, correspondence estimation, and spatial reasoning as instruction-conditioned generation tasks within a single multimodal model. Built on Bagel (Deng et al. 2025a), SPARGen predicts depth maps, camera poses, and point maps for 3D reconstruction; optical flow for dense correspondence estimation; and textual answers for spatial question answering.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 本文提出 SPARGen，这是一个统一的空间感知与推理框架，如图1所示。我们的设计源于一个简单观点：空间智能并非仅仅是若干孤立任务的集合，而是一个从观测中构建空间表征、并使用这些表征回答条件查询的过程。因此，SPARGen 将几何重建、对应关系估计和空间推理表述为单一多模态模型中的指令条件生成任务。SPARGen 构建于 Bagel（Deng et al. 2025a）之上，可预测用于三维重建的深度图、相机位姿和点图，用于稠密对应关系估计的光流，以及用于空间问答的文本答案。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> To accommodate these heterogeneous outputs, SPARGen adopts two complementary generative formulations. Dense spatial fields, including depth maps, point maps, and optical flow, are encoded as image-like representations and generated through the model’s native image-generation pathway. Compact structured outputs, such as camera poses, as well as answers to spatial questions, are serialized as token sequences and generated through the autoregressive pathway. Both generative pathways are integrated within a shared Mixture-of-Transformer-Experts (MoT) backbone, allowing geometric, correspondence, and semantic supervision to jointly shape the model’s multimodal representations. SPARGen thus provides a shared instruction interface for constructing and using spatial representations without introducing task-specific regression heads or external geometric prediction modules.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 为适应这些异构输出，SPARGen 采用两种互补的生成表述。包括深度图、点图和光流在内的稠密空间场被编码为类图像表征，并通过模型原生的图像生成路径生成。相机位姿等紧凑结构化输出以及空间问题的答案则被序列化为词元序列，并通过自回归路径生成。两条生成路径集成于共享的混合 Transformer 专家（MoT）骨干网络中，使几何、对应关系和语义监督能够共同塑造模型的多模态表征。因此，SPARGen 提供了一个用于构建和使用空间表征的共享指令接口，而无需引入任务专用回归头或外部几何预测模块。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> This native generative formulation distinguishes SPARGen by how spatial capabilities are incorporated into a foundation model. Prior approaches typically specialize in either dense geometric prediction or language-based spatial reasoning (Wang et al. 2025a; Lin et al. 2025a; Chen et al. 2024a; Wu et al. 2026). SPARGen instead supports both within a single instruction-conditioned multimodal architecture. More closely related to our work, G²VLM (Hu et al. 2026) unifies language understanding and geometric prediction by introducing geometry-specific components. In contrast, SPARGen starts from a pretrained unified multimodal model and represents heterogeneous spatial targets in forms that can be directly produced by its native image-generation and autoregressive pathways. This design enables dense geometric fields, dense correspondences, and structured spatial answers to be learned through a shared generative interface, without task-specific prediction heads or external geometric modules. Our main contributions are as follows:

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 这种原生生成表述使 SPARGen 在将空间能力融入基础模型的方式上独具特色。先前方法通常专注于稠密几何预测或基于语言的空间推理之一（Wang et al. 2025a；Lin et al. 2025a；Chen et al. 2024a；Wu et al. 2026）。相比之下，SPARGen 在单一指令条件多模态架构中同时支持二者。与我们工作更密切相关的 G²VLM（Hu et al. 2026）通过引入几何专用组件来统一语言理解和几何预测。SPARGen 则从一个预训练统一多模态模型出发，将异构空间目标表示为其原生图像生成路径和自回归路径能够直接产生的形式。这一设计使稠密几何场、稠密对应关系和结构化空间答案能够通过共享生成接口进行学习，而无需任务专用预测头或外部几何模块。我们的主要贡献如下：

- **Para. 10:** We formulate 3D reconstruction, dense correspondence, and spatial reasoning as instruction-conditioned generation tasks, representing dense outputs as image-aligned fields and structured outputs as token sequences.
- **Para. 10[CN]:** 我们将三维重建、稠密对应关系和空间推理表述为指令条件生成任务，将稠密输出表示为图像对齐场，并将结构化输出表示为词元序列。

- **Para. 11:** We instantiate this formulation in SPARGen, which leverages the native image-generation and autoregressive pathways of a shared MoT backbone to support heterogeneous spatial tasks without external geometric modules.
- **Para. 11[CN]:** 我们在 SPARGen 中实例化这一表述，利用共享 MoT 骨干网络的原生图像生成路径和自回归路径，在无需外部几何模块的情况下支持异构空间任务。

- **Para. 12:** Experiments demonstrate that a single SPARGen model achieves competitive performance across visual-geometry, optical flow, and spatial-reasoning benchmarks. Ablations further reveal positive interactions among heterogeneous supervision.
- **Para. 12[CN]:** 实验表明，单一 SPARGen 模型在视觉几何、光流和空间推理基准上取得了有竞争力的性能。消融实验进一步揭示了异构监督之间的正向相互作用。

## 2 Related Work

## 2 相关工作

### 3D Reconstruction and Dense Correspondence

### 三维重建与稠密对应关系

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> Visual geometry systems recover camera motion and scene structure (Schönberger and Frahm 2016). More recently, feed-forward reconstruction models have moved toward broader geometric representations. DUSt3R casts uncalibrated stereo reconstruction as pointmap regression (Wang et al. 2024b; Yang et al. 2025). VGGT jointly predicts camera poses, depth, point maps, and tracks from one or multiple views (Wang et al. 2025a), while VGGT-Ω scales this paradigm to substantially larger models and datasets and extends it to dynamic scenes (Wang et al. 2026). A complementary line of work repurposes generative priors for dense prediction: Marigold adapts a diffusion model for depth estimation (Ke et al. 2024), and Edit2Perceive uses an image-editing model for depth estimation, surface-normal estimation, and matting (Shi, Song, and Shou 2026). Similarly, learning-based matching methods replace individual stages of traditional correspondence pipelines: LoFTR performs detector-free matching with transformers (Sun et al. 2021), while DKM (Edstedt et al. 2023) and RoMa (Edstedt et al. 2024) directly predict dense correspondences for robust two-view geometry. These methods demonstrate increasingly general geometric perception, but typically expose their capabilities through fixed pipelines and geometric objectives. In contrast, SPARGen casts both reconstruction and correspondence estimation as instruction-conditioned behaviors of a multimodal generative model.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> 视觉几何系统用于恢复相机运动和场景结构（Schönberger and Frahm 2016）。近年来，前馈重建模型开始转向更广泛的几何表征。DUSt3R 将无标定立体重建表述为点图回归（Wang et al. 2024b；Yang et al. 2025）。VGGT 从一个或多个视图中联合预测相机位姿、深度、点图和轨迹（Wang et al. 2025a），而 VGGT-Ω 将这一范式扩展到规模显著更大的模型和数据集，并将其延伸到动态场景（Wang et al. 2026）。另一条互补研究路线将生成先验重新用于稠密预测：Marigold 将扩散模型适配于深度估计（Ke et al. 2024），Edit2Perceive 则使用图像编辑模型进行深度估计、表面法线估计和抠图（Shi, Song, and Shou 2026）。类似地，基于学习的匹配方法取代了传统对应关系流水线中的单独阶段：LoFTR 使用 Transformer 执行无检测器匹配（Sun et al. 2021），而 DKM（Edstedt et al. 2023）和 RoMa（Edstedt et al. 2024）直接预测稠密对应关系，以实现稳健的双视图几何。这些方法展现出日益通用的几何感知能力，但通常通过固定流水线和几何目标来提供这些能力。相比之下，SPARGen 将重建和对应关系估计均表述为多模态生成模型的指令条件行为。

---

<!-- Page 3 -->

## Figure 2 — In-figure transcription

| Component | English | 中文 |
|---|---|---|
| Input | $I$ | 输入 $I$ |
| Instruction | $p$ | 指令 $p$ |
| Text instruction examples | Estimate per-pixel relative depth. / Reconstruct 3D pointmaps from these images. / Predict the optical flow of adjacent frames. / Estimate camera pose: quaternion, offset and scale. / What’s in front of the sofa to the right? | 估计逐像素相对深度。/ 从这些图像重建三维点图。/ 预测相邻帧的光流。/ 估计相机位姿：四元数、偏移和尺度。/ 右侧沙发前方有什么？ |
| Dense field output | $y_{\text{field}}$: Depth; Flow; Point map | 稠密场输出 $y_{\text{field}}$：深度；光流；点图 |
| Sequence output | $y_{\text{seq}}$: Pose: “quat” + “quat” + “offset” + “offset” + “scale”; The chest is in front of the sofa on the right. | 序列输出 $y_{\text{seq}}$：位姿：“四元数”+“四元数”+“偏移”+“偏移”+“尺度”；箱子位于右侧沙发的前方。 |
| Sequence pathway | Autoregressive Decoding; FFN; Multi-modal Self Attention; QKV; Text Tokenizer; ViT Encoder | 序列路径：自回归解码；FFN；多模态自注意力；QKV；文本分词器；ViT 编码器 |
| Dense-field pathway | VAE Decoder; FFN; Multi-modal Self Attention; QKV; VAE Encoder; Noise | 稠密场路径：VAE 解码器；FFN；多模态自注意力；QKV；VAE 编码器；噪声 |
| Outputs | $\hat y_{\text{seq}}$, $\hat y_{\text{field}}$ | 输出 $\hat y_{\text{seq}}$、$\hat y_{\text{field}}$ |
| Repetition | $\times N$ | 重复 $\times N$ |
| Training-only input | $y_{\text{field}}$, Train | 仅训练阶段输入：$y_{\text{field}}$，训练 |

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> Figure 2: **Overview of SPARGen.** Given a sequence of RGB images and a language instruction, SPARGen represents spatial outputs as sequences or image-aligned fields. These two output formats are generated through the native autoregressive and rectified-flow pathways of a shared MoT backbone. The dashed box denotes the training-only encoding of target fields.

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> 图2：**SPARGen 概览。** 给定一组 RGB 图像和一条语言指令，SPARGen 将空间输出表示为序列或图像对齐场。这两种输出格式分别通过共享 MoT 骨干网络的原生自回归路径和整流流路径生成。虚线框表示仅在训练阶段使用的目标场编码。

### Geometry-Aware Spatial Reasoning

### 几何感知空间推理

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> Vision-language models acquire strong semantic knowledge but remain unreliable in recovering geometric structure. SpatialVLM addresses this limitation by training on large-scale spatial question-answering data (Chen et al. 2024a), whereas SpatialRGPT combines region-level supervision with a plug-in depth representation (Cheng et al. 2024). Other approaches inject stronger reconstruction priors. VLM-3R derives implicit spatial and camera tokens from a geometry encoder for monocular video reasoning (Fan et al. 2026), and Spatial-MLLM combines semantic and geometry-oriented visual encoders (Ma et al. 2025). More tightly coupled designs learn geometry within the multimodal model: G²VLM adopts dedicated geometric and semantic transformer experts with shared attention to support reconstruction and spatial reasoning (Hu et al. 2026). Collectively, these works establish that explicit geometry benefits spatial reasoning. Nevertheless, geometric information is commonly provided by an external encoder or modeled through dedicated experts or output heads, and most systems combine language reasoning with only a limited set of geometric capabilities. SPARGen instead places spatial perception and reasoning under the same instruction-conditioned training interface.

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> 视觉语言模型能够习得强大的语义知识，但在恢复几何结构方面仍不可靠。SpatialVLM 通过在大规模空间问答数据上训练来解决这一局限（Chen et al. 2024a），而 SpatialRGPT 将区域级监督与可插拔深度表征相结合（Cheng et al. 2024）。其他方法则注入更强的重建先验。VLM-3R 从几何编码器中提取隐式空间词元和相机词元，用于单目视频推理（Fan et al. 2026）；Spatial-MLLM 则结合面向语义和几何的视觉编码器（Ma et al. 2025）。耦合更紧密的设计直接在多模态模型内部学习几何：G²VLM 采用专用的几何与语义 Transformer 专家，并共享注意力，以支持重建和空间推理（Hu et al. 2026）。总体而言，这些工作证明了显式几何有益于空间推理。然而，几何信息通常由外部编码器提供，或通过专用专家或输出头建模；大多数系统也仅将语言推理与有限的几何能力相结合。SPARGen 则将空间感知和推理置于同一个指令条件训练接口之下。

### Unified Multimodal Understanding and Generation

### 统一多模态理解与生成

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> Recent multimodal foundation models seek to replace separate understanding and generation systems with a shared model. Chameleon represents images and text as interleaved discrete tokens in an early-fusion architecture (Chameleon Team 2024); Show-o combines autoregressive language modeling with discrete diffusion in a single transformer (Xie et al. 2025); and Janus decouples the visual encoding pathways for understanding and generation while retaining a shared autoregressive backbone (Wu et al. 2025). Bagel further scales unified pretraining on interleaved text and image data, exhibiting broad multimodal reasoning and generation capabilities (Deng et al. 2025a). These models are primarily developed for semantic understanding, content generation, and image editing, leaving precise geometric prediction and dense correspondence comparatively underexplored.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> 近期多模态基础模型试图以共享模型取代彼此分离的理解系统和生成系统。Chameleon 在早期融合架构中将图像和文本表示为交错的离散词元（Chameleon Team 2024）；Show-o 在单一 Transformer 中结合自回归语言建模与离散扩散（Xie et al. 2025）；Janus 则将用于理解和生成的视觉编码路径解耦，同时保留共享自回归骨干网络（Wu et al. 2025）。Bagel 进一步在交错文本—图像数据上扩展统一预训练，展现出广泛的多模态推理和生成能力（Deng et al. 2025a）。这些模型主要面向语义理解、内容生成和图像编辑，而对精确几何预测和稠密对应关系的探索相对不足。

## 3 Method

## 3 方法

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> We first introduce the problem formulation and provide an overview of SPARGen in Sec. 3.1. We then describe its architecture and two native output representations in Sec. 3.2, followed by the corresponding training objectives in Sec. 3.3.

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> 我们首先在第3.1节介绍问题表述并概述 SPARGen。随后在第3.2节描述其架构和两种原生输出表征，并在第3.3节介绍相应的训练目标。

### 3.1 Problem Formulation and Overview

### 3.1 问题表述与概览

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> Given a sequence of RGB images $\mathcal I=\{I_i\}_{i=1}^{N}$, where $I_i\in\mathbb R^{H\times W\times3}$, and a tokenized natural-language instruction $p=(p_l)_{l=1}^{L_p}\in\mathcal V^{L_p}$, our goal is to predict a target $Y_\tau$ for a spatial task $\tau\in\mathcal T=\mathcal T_{\mathrm{seq}}\cup\mathcal T_{\mathrm{field}}$. Here, $\mathcal V$ denotes the tokenizer vocabulary, and $\mathcal T_{\mathrm{seq}}$ and $\mathcal T_{\mathrm{field}}$ denote the sets of token-sequence and dense-field generation tasks, respectively.

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> 给定一组 RGB 图像 $\mathcal I=\{I_i\}_{i=1}^{N}$，其中 $I_i\in\mathbb R^{H\times W\times3}$，以及词元化自然语言指令 $p=(p_l)_{l=1}^{L_p}\in\mathcal V^{L_p}$，我们的目标是为某个空间任务 $\tau\in\mathcal T=\mathcal T_{\mathrm{seq}}\cup\mathcal T_{\mathrm{field}}$ 预测目标 $Y_\tau$。其中，$\mathcal V$ 表示分词器词表，$\mathcal T_{\mathrm{seq}}$ 和 $\mathcal T_{\mathrm{field}}$ 分别表示词元序列生成任务集合和稠密场生成任务集合。

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> Rather than introducing a separate module for each task, SPARGen represents spatial targets using two native generative formats:

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> SPARGen 并不为每项任务引入单独模块，而是使用两种原生生成格式来表示空间目标：

$$
\mathcal R_\tau(Y_\tau)=
\begin{cases}
\mathcal S_\tau(Y_\tau)\in\mathcal V^{L_\tau}, & \tau\in\mathcal T_{\mathrm{seq}},\$$2mm]
\Phi_\tau(Y_\tau)\in\mathbb R^{M_\tau\times H\times W\times3}, & \tau\in\mathcal T_{\mathrm{field}}.
\end{cases}
\tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> Here, $\mathcal S_\tau$ serializes a sequence target into $L_\tau$ discrete tokens, whereas $\Phi_\tau$ encodes a dense target as $M_\tau$ image-aligned fields. The conditional generative model is defined as:

> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> 其中，$\mathcal S_\tau$ 将序列目标序列化为 $L_\tau$ 个离散词元，而 $\Phi_\tau$ 将稠密目标编码为 $M_\tau$ 个图像对齐场。条件生成模型定义为：

$$
p_\theta\bigl(\mathcal R_\tau(Y_\tau)\mid\mathcal I,p\bigr).
\tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> This formulation unifies diverse spatial tasks while preserving the structural properties of their respective outputs.

> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> 这一表述在统一多种空间任务的同时，保留了各类输出各自的结构属性。

---

<!-- Page 4 -->

> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> As illustrated in Fig. 2, SPARGen builds on the MoT architecture of Bagel (Deng et al. 2025a). The input images are encoded into visual-understanding tokens by a ViT encoder, while the instruction is represented as text tokens. Text and visual tokens interact through joint multimodal self-attention. Sequence targets are generated autoregressively, whereas dense fields are generated in the VAE latent space through rectified flow. During training, the frozen VAE encoder maps the target fields to clean target latents, which are interpolated with Gaussian noise to construct noisy visual tokens for rectified-flow training.

> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> 如图2所示，SPARGen 构建于 Bagel 的 MoT 架构之上（Deng et al. 2025a）。输入图像由 ViT 编码器编码为视觉理解词元，指令则表示为文本词元。文本词元和视觉词元通过联合多模态自注意力进行交互。序列目标以自回归方式生成，而稠密场则通过整流流在 VAE 潜空间中生成。训练期间，冻结的 VAE 编码器将目标场映射为干净的目标潜变量，再将其与高斯噪声插值，以构造用于整流流训练的含噪视觉词元。

### 3.2 Unified Generative Architecture

### 3.2 统一生成架构

#### Unified Architecture for Spatial Generation

#### 空间生成的统一架构

> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> SPARGen adopts the MoT architecture, which consists of an understanding expert and a generation expert. The two token streams use modality-specific projections and feed-forward networks but interact through joint multimodal self-attention. This design allows semantic and geometric information to interact throughout the backbone while retaining their respective generation mechanisms.

> <span style="color:#F59E0B"><strong>Para. 23[CN]:</strong></span> SPARGen 采用由理解专家和生成专家组成的 MoT 架构。两条词元流使用模态专用投影和前馈网络，但通过联合多模态自注意力进行交互。这一设计使语义信息和几何信息能够在整个骨干网络中交互，同时保留各自的生成机制。

> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> Given an image sequence $\mathcal I$ and an instruction $p$, the conditioning contexts for token-sequence and dense-field generation are constructed as

> <span style="color:#F59E0B"><strong>Para. 24[CN]:</strong></span> 给定图像序列 $\mathcal I$ 和指令 $p$，用于词元序列生成和稠密场生成的条件上下文构造为

$$
C_{\mathrm{seq}}
=
\operatorname{Concat}\bigl(E_{\mathrm{text}}(p),E_{\mathrm{vit}}(\mathcal I)\bigr),
$$

$$
C_{\mathrm{field}}
=
\operatorname{Concat}\bigl(E_{\mathrm{text}}(p),E_{\mathrm{vit}}(\mathcal I),E_{\mathrm{vae}}(\mathcal I)\bigr),
\tag{3}
$$

> <span style="color:#3B82F6"><strong>Para. 25:</strong></span> where $E_{\mathrm{text}}$ denotes the text embedding module, $E_{\mathrm{vit}}$ denotes the visual-understanding encoder, and $E_{\mathrm{vae}}$ denotes the frozen VAE encoder. Thus, dense-field generation is conditioned on both the ViT and VAE tokens of the input images.

> <span style="color:#F59E0B"><strong>Para. 25[CN]:</strong></span> 其中，$E_{\mathrm{text}}$ 表示文本嵌入模块，$E_{\mathrm{vit}}$ 表示视觉理解编码器，$E_{\mathrm{vae}}$ 表示冻结的 VAE 编码器。因此，稠密场生成同时以输入图像的 ViT 词元和 VAE 词元为条件。

> <span style="color:#3B82F6"><strong>Para. 26:</strong></span> For a token-sequence task $\tau\in\mathcal T_{\mathrm{seq}}$, let $\mathcal S_\tau(Y_\tau)=(s_1,\ldots,s_{L_\tau})$ denote its serialized target. The model generates the sequence autoregressively:

> <span style="color:#F59E0B"><strong>Para. 26[CN]:</strong></span> 对于词元序列任务 $\tau\in\mathcal T_{\mathrm{seq}}$，令 $\mathcal S_\tau(Y_\tau)=(s_1,\ldots,s_{L_\tau})$ 表示其序列化目标。模型以自回归方式生成该序列：

$$
p_\theta\bigl(\mathcal S_\tau(Y_\tau)\mid\mathcal I,p\bigr)
=
\prod_{j=1}^{L_\tau}
p_\theta\bigl(s_j\mid C_{\mathrm{seq}},s_{<j}\bigr).
\tag{4}
$$

> <span style="color:#3B82F6"><strong>Para. 27:</strong></span> For a dense-field task $\tau\in\mathcal T_{\mathrm{field}}$, the target is first mapped to a clean latent by the frozen VAE encoder $z_0=E_{\mathrm{vae}}(\Phi_\tau(Y_\tau))$. We then construct a linear rectified-flow path between the clean latent $z_0$ and Gaussian noise $\epsilon$:

> <span style="color:#F59E0B"><strong>Para. 27[CN]:</strong></span> 对于稠密场任务 $\tau\in\mathcal T_{\mathrm{field}}$，首先由冻结的 VAE 编码器将目标映射为干净潜变量 $z_0=E_{\mathrm{vae}}(\Phi_\tau(Y_\tau))$。随后，我们在干净潜变量 $z_0$ 和高斯噪声 $\epsilon$ 之间构造一条线性整流流路径：

$$
z_t=(1-t)z_0+t\epsilon,\qquad
t\sim\mathcal U(0,1),\qquad
\epsilon\sim\mathcal N(0,\mathbf I).
\tag{5}
$$

> <span style="color:#3B82F6"><strong>Para. 28:</strong></span> The target velocity is $u_t=\epsilon-z_0$. Conditioned on the multimodal context, the generation pathway predicts the velocity field $\hat v_t=v_\theta(z_t,t;C_{\mathrm{field}})$, which is trained to match $u_t$.

> <span style="color:#F59E0B"><strong>Para. 28[CN]:</strong></span> 目标速度为 $u_t=\epsilon-z_0$。在多模态上下文条件下，生成路径预测速度场 $\hat v_t=v_\theta(z_t,t;C_{\mathrm{field}})$，并训练其匹配 $u_t$。

> <span style="color:#3B82F6"><strong>Para. 29:</strong></span> At inference time, sampling starts from $z_1\sim\mathcal N(0,\mathbf I)$ and integrates the predicted velocity field from $t=1$ to $t=0$. The resulting latent $\hat z_0$ is decoded by the frozen VAE decoder.

> <span style="color:#F59E0B"><strong>Para. 29[CN]:</strong></span> 推理时，采样从 $z_1\sim\mathcal N(0,\mathbf I)$ 开始，并从 $t=1$ 到 $t=0$ 对预测速度场进行积分。所得潜变量 $\hat z_0$ 由冻结的 VAE 解码器解码。

#### Sparse and Structured Outputs as Sequences

#### 作为序列的稀疏与结构化输出

> <span style="color:#3B82F6"><strong>Para. 30:</strong></span> For each task $\tau\in\mathcal T_{\mathrm{seq}}$, the serializer $\mathcal S_\tau$ maps its target $Y_\tau$ to a canonical token sequence that is generated autoregressively and deterministically deserialized.

> <span style="color:#F59E0B"><strong>Para. 30[CN]:</strong></span> 对于每项任务 $\tau\in\mathcal T_{\mathrm{seq}}$，序列化器 $\mathcal S_\tau$ 将其目标 $Y_\tau$ 映射为规范词元序列；该序列以自回归方式生成，并通过确定性过程反序列化。

> <span style="color:#3B82F6"><strong>Para. 31:</strong></span> **Textual Answers and Sparse Geometric States.** Some spatial QA tasks require only a small number of query-specific geometric quantities rather than a dense field. We serialize these quantities, such as depths at queried points and numerical spatial attributes, in the order specified by the instruction, followed by the final answer when applicable. Text-only QA directly uses the answer tokens. This design provides sparse geometric supervision while retaining standard autoregressive decoding.

> <span style="color:#F59E0B"><strong>Para. 31[CN]:</strong></span> **文本答案与稀疏几何状态。** 某些空间问答任务只需要少量与查询相关的几何量，而非稠密场。我们按照指令指定的顺序序列化这些量，例如查询点处的深度和数值空间属性，并在适用时附加最终答案。纯文本问答直接使用答案词元。这一设计在保留标准自回归解码的同时提供稀疏几何监督。

> <span style="color:#3B82F6"><strong>Para. 32:</strong></span> **Structured Camera Poses.** For structured outputs like camera poses, we use special tokens to represent them. We parameterize a camera pose $(R,t)$ as

> <span style="color:#F59E0B"><strong>Para. 32[CN]:</strong></span> **结构化相机位姿。** 对于相机位姿等结构化输出，我们使用特殊词元进行表示。相机位姿 $(R,t)$ 被参数化为

$$
q=\operatorname{Quat}(R),\qquad
d=\frac{t}{\lVert t\rVert_2},\qquad
r=\lVert t\rVert_2,
\tag{6}
$$

> <span style="color:#3B82F6"><strong>Para. 33:</strong></span> where $q$ is the rotation quaternion, and $(d,r)$ denote the translation direction and magnitude, respectively. Their scalar components are quantized with a resolution of $10^{-3}$, mapped to dedicated numerical tokens, and serialized in a fixed order.

> <span style="color:#F59E0B"><strong>Para. 33[CN]:</strong></span> 其中，$q$ 是旋转四元数，$(d,r)$ 分别表示平移方向和幅值。它们的标量分量以 $10^{-3}$ 的分辨率量化，映射到专用数值词元，并按固定顺序序列化。

#### Dense Outputs as Image-Aligned Fields

#### 作为图像对齐场的稠密输出

> <span style="color:#3B82F6"><strong>Para. 34:</strong></span> For each task $\tau\in\mathcal T_{\mathrm{field}}$, the deterministic transform $\Phi_\tau$ maps $Y_\tau$ to image-aligned fields. These fields follow the shape of RGB images while encoding geometric quantities. Before VAE encoding, each field is rescaled to the input range of the VAE.

> <span style="color:#F59E0B"><strong>Para. 34[CN]:</strong></span> 对于每项任务 $\tau\in\mathcal T_{\mathrm{field}}$，确定性变换 $\Phi_\tau$ 将 $Y_\tau$ 映射为图像对齐场。这些场沿用 RGB 图像的形状，同时编码几何量。在进行 VAE 编码之前，每个场都被重新缩放到 VAE 的输入范围。

> <span style="color:#3B82F6"><strong>Para. 35:</strong></span> **Depth.** Given a depth map $D$, we normalize its values as

> <span style="color:#F59E0B"><strong>Para. 35[CN]:</strong></span> **深度。** 给定深度图 $D$，其值归一化为

$$
\hat D
=
1-\frac{D-d_{\min}}{d_{\max}-d_{\min}+\epsilon},
\tag{7}
$$

> <span style="color:#3B82F6"><strong>Para. 36:</strong></span> where $d_{\min}$ and $d_{\max}$ denote the minimum and maximum depths in the image. Nearby and distant regions are mapped toward 1 and 0, respectively, and the resulting relative-depth representation is replicated across three channels.

> <span style="color:#F59E0B"><strong>Para. 36[CN]:</strong></span> 其中，$d_{\min}$ 和 $d_{\max}$ 分别表示图像中的最小深度和最大深度。近处区域和远处区域分别映射至接近 1 和 0，所得相对深度表征复制到三个通道。

> <span style="color:#3B82F6"><strong>Para. 37:</strong></span> **Point Maps.** All point maps $\{P_i\}_{i=1}^{N}$ are expressed in a common coordinate system whose origin is the first camera. We normalize them using a center and scale shared across the sequence:

> <span style="color:#F59E0B"><strong>Para. 37[CN]:</strong></span> **点图。** 所有点图 $\{P_i\}_{i=1}^{N}$ 均表示在以第一台相机为原点的公共坐标系中。我们使用在整个序列中共享的中心和尺度进行归一化：

$$
c=\frac{1}{2N}\sum_{i=1}^{N}
\left(
\min_{p\in\Omega}P_i(p)+
\max_{p\in\Omega}P_i(p)
\right),
$$

$$
s=\max_{i,p\in\Omega}\lVert P_i(p)-c\rVert_\infty,
\qquad
\hat P_i=\frac{P_i-c}{s+\epsilon}.
\tag{8}
$$

> <span style="color:#3B82F6"><strong>Para. 38:</strong></span> where the minimum and maximum are computed element-wise over pixels. The three channels of $\hat P_i$ encode the normalized Cartesian coordinates $(X,Y,Z)$. Sharing $c$ and $s$ across the sequence preserves relative geometry across views.

> <span style="color:#F59E0B"><strong>Para. 38[CN]:</strong></span> 其中，最小值和最大值在像素范围内按元素计算。$\hat P_i$ 的三个通道编码归一化笛卡尔坐标 $(X,Y,Z)$。在整个序列中共享 $c$ 和 $s$ 可保留跨视图的相对几何关系。

> <span style="color:#3B82F6"><strong>Para. 39:</strong></span> **Optical Flow.** Given an optical flow field $(u,v)$, we normalize the displacements by the image dimensions and apply a signed square-root transform:

> <span style="color:#F59E0B"><strong>Para. 39[CN]:</strong></span> **光流。** 给定光流场 $(u,v)$，我们按照图像尺寸对位移进行归一化，并应用带符号平方根变换：

$$
\hat u=\rho\!\left(\frac{u}{W}\right),\qquad
\hat v=\rho\!\left(\frac{v}{H}\right),\qquad
\rho(x)=\operatorname{sgn}(x)\sqrt{|x|},
\tag{9}
$$

> <span style="color:#3B82F6"><strong>Para. 40:</strong></span> where only the first two channels are used for decoding and the third channel encodes the flow magnitude.

> <span style="color:#F59E0B"><strong>Para. 40[CN]:</strong></span> 解码时仅使用前两个通道，第三个通道编码光流幅值。

> <span style="color:#3B82F6"><strong>Para. 41:</strong></span> Additionally, we design an optical flow refinement procedure. At inference time, SPARGen refines optical flow through a predict–warp–predict procedure. Given the current estimate $F$, we align the second frame to the first as $I'_2(x)=I_2(x+F(x))$, and predict a residual flow $\Delta F$ between $I_1$ and $I'_2$. The estimated flow is given by $F+\Delta F$.

> <span style="color:#F59E0B"><strong>Para. 41[CN]:</strong></span> 此外，我们设计了一种光流细化过程。推理时，SPARGen 通过“预测—变形—再预测”过程细化光流。给定当前估计 $F$，我们以 $I'_2(x)=I_2(x+F(x))$ 将第二帧与第一帧对齐，并预测 $I_1$ 与 $I'_2$ 之间的残差光流 $\Delta F$。最终估计光流为 $F+\Delta F$。

---

<!-- Page 5 -->

### 3.3 Training Objectives

### 3.3 训练目标

> <span style="color:#3B82F6"><strong>Para. 42:</strong></span> SPARGen is jointly trained on a mixture of token-sequence and dense-field generation tasks.

> <span style="color:#F59E0B"><strong>Para. 42[CN]:</strong></span> SPARGen 在词元序列生成任务和稠密场生成任务的混合数据上进行联合训练。

> <span style="color:#3B82F6"><strong>Para. 43:</strong></span> **Sequence Generation Objective.** For a task $\tau\in\mathcal T_{\mathrm{seq}}$, let $\mathcal S_\tau(Y_\tau)=(s_1,\ldots,s_{L_\tau})$ denote its serialized target. We minimize the average cross-entropy over the target tokens:

> <span style="color:#F59E0B"><strong>Para. 43[CN]:</strong></span> **序列生成目标。** 对于任务 $\tau\in\mathcal T_{\mathrm{seq}}$，令 $\mathcal S_\tau(Y_\tau)=(s_1,\ldots,s_{L_\tau})$ 表示其序列化目标。我们最小化目标词元上的平均交叉熵：

$$
\mathcal L_{\mathrm{seq}}
=
-\frac{1}{L_\tau}
\sum_{j=1}^{L_\tau}
\log p_\theta(s_j\mid C_{\mathrm{seq}},s_{<j}).
\tag{10}
$$

> <span style="color:#3B82F6"><strong>Para. 44:</strong></span> Cross-entropy is evaluated only at target-token positions.

> <span style="color:#F59E0B"><strong>Para. 44[CN]:</strong></span> 交叉熵仅在目标词元位置上计算。

> <span style="color:#3B82F6"><strong>Para. 45:</strong></span> **Dense Field Generation Objective.** For a task $\tau\in\mathcal T_{\mathrm{field}}$, we optimize the rectified-flow matching objective

> <span style="color:#F59E0B"><strong>Para. 45[CN]:</strong></span> **稠密场生成目标。** 对于任务 $\tau\in\mathcal T_{\mathrm{field}}$，我们优化整流流匹配目标

$$
\mathcal L_{\mathrm{field}}
=
\mathbb E_{t,\epsilon}
\left[
\frac{1}{d_\tau}
\left\|
v_\theta(z_t,t;C_{\mathrm{field}})-u_t
\right\|_2^2
\right],
\tag{11}
$$

> <span style="color:#3B82F6"><strong>Para. 46:</strong></span> where $t\sim\mathcal U(0,1)$, $\epsilon\sim\mathcal N(0,\mathbf I)$, and $d_\tau$ denotes the total number of scalar elements in the target latent representation.

> <span style="color:#F59E0B"><strong>Para. 46[CN]:</strong></span> 其中，$t\sim\mathcal U(0,1)$、$\epsilon\sim\mathcal N(0,\mathbf I)$，而 $d_\tau$ 表示目标潜表征中标量元素的总数。

> <span style="color:#3B82F6"><strong>Para. 47:</strong></span> Each training example activates the objective associated with its target representation. The per-example loss is

> <span style="color:#F59E0B"><strong>Para. 47[CN]:</strong></span> 每个训练样本激活与其目标表征相对应的目标函数。单样本损失为

$$
\mathcal L_\tau=
\begin{cases}
\lambda\mathcal L_{\mathrm{seq}}, & \tau\in\mathcal T_{\mathrm{seq}},\\
\mathcal L_{\mathrm{field}}, & \tau\in\mathcal T_{\mathrm{field}},
\end{cases}
\tag{12}
$$

> <span style="color:#3B82F6"><strong>Para. 48:</strong></span> where $\lambda$ controls the weight of the sequence generation objective. The overall training objective is $\mathcal L=\mathbb E_{(\mathcal I,p,Y_\tau,\tau)\sim\mathcal D}[\mathcal L_\tau]$, where $\mathcal D$ denotes the training distribution.

> <span style="color:#F59E0B"><strong>Para. 48[CN]:</strong></span> 其中，$\lambda$ 控制序列生成目标的权重。总体训练目标为 $\mathcal L=\mathbb E_{(\mathcal I,p,Y_\tau,\tau)\sim\mathcal D}[\mathcal L_\tau]$，其中 $\mathcal D$ 表示训练分布。

## 4 Experiments

## 4 实验

### 4.1 Experimental Settings

### 4.1 实验设置

> <span style="color:#3B82F6"><strong>Para. 49:</strong></span> **Training Datasets.** We train SPARGen using three groups of supervision: spatial understanding, visual geometry, and optical flow. 1) For spatial reasoning, following G²VLM (Hu et al. 2026), we use the official training splits of MindCube, OmniSpatial, OST-Bench, SPAR-7M and general VQA dataset LLaVA-OneVision. 2) For visual geometry, including relative-depth estimation, camera pose prediction, and multi-view point map reconstruction, we aggregate training data from ASE, BlendedMVS, CO3D, DeMoN, DL3DV, Hypersim, IRS, MegaSynth, MVS-Synth, Objaverse, OmniObject3D, ScanNet v2, ScanNet++, SceneNet RGB-D, Taskonomy, and WildRGB-D. Depending on the available annotations, each sample may supervise one or more visual-geometry tasks. Although several datasets provide metric geometric annotations, we normalize the depth and point map targets and train the model in a relative-scale coordinate system. For samples with sparse or incomplete geometric annotations, we additionally use MoGe (Wang et al. 2025c) to generate dense, image-aligned geometric pseudo-labels for training the dense-field pathway. 3) For optical flow estimation, we use TartanAir, AutoFlow, FlyingChairs, FlyingChairs2, FlyingThings3D, Monkaa, Kubric-4D, ParallelDomain-4D, and Spring.

> <span style="color:#F59E0B"><strong>Para. 49[CN]:</strong></span> **训练数据集。** 我们使用三类监督训练 SPARGen：空间理解、视觉几何和光流。1）对于空间推理，我们沿用 G²VLM（Hu et al. 2026）的设置，使用 MindCube、OmniSpatial、OST-Bench、SPAR-7M 的官方训练划分，以及通用 VQA 数据集 LLaVA-OneVision。2）对于视觉几何，包括相对深度估计、相机位姿预测和多视图点图重建，我们汇总 ASE、BlendedMVS、CO3D、DeMoN、DL3DV、Hypersim、IRS、MegaSynth、MVS-Synth、Objaverse、OmniObject3D、ScanNet v2、ScanNet++、SceneNet RGB-D、Taskonomy 和 WildRGB-D 的训练数据。根据可用标注，每个样本可监督一项或多项视觉几何任务。尽管若干数据集提供度量几何标注，我们仍对深度和点图目标进行归一化，并在相对尺度坐标系中训练模型。对于几何标注稀疏或不完整的样本，我们还使用 MoGe（Wang et al. 2025c）生成稠密、图像对齐的几何伪标签，以训练稠密场路径。3）对于光流估计，我们使用 TartanAir、AutoFlow、FlyingChairs、FlyingChairs2、FlyingThings3D、Monkaa、Kubric-4D、ParallelDomain-4D 和 Spring。

> <span style="color:#3B82F6"><strong>Para. 50:</strong></span> **Benchmarks.** We follow the evaluation protocol of G²VLM (Hu et al. 2026), the most closely related baseline. 1) For visual-geometry evaluation, we use Sintel (Bozic et al. 2021) and NYU-v2 (Silberman et al. 2012) for depth estimation, 7Scenes (Shotton et al. 2013) and ETH3D (Schöps et al. 2017) for 3D reconstruction, and CO3D v2 (Reizenstein et al. 2021) for camera pose estimation. 2) For spatial reasoning, we evaluate on the official test sets of MindCube Tiny (Yin et al. 2025), OmniSpatial (Jia et al. 2025), OST-Bench (Lin et al. 2025b), and SPAR-Bench (Zhang et al. 2025a). 3) For optical flow estimation, we evaluate zero-shot transfer on the KITTI training set (Geiger et al. 2013), without fine-tuning on the benchmark.

> <span style="color:#F59E0B"><strong>Para. 50[CN]:</strong></span> **基准。** 我们遵循最相关基线 G²VLM（Hu et al. 2026）的评估协议。1）对于视觉几何评估，我们使用 Sintel（Bozic et al. 2021）和 NYU-v2（Silberman et al. 2012）评估深度估计，使用 7Scenes（Shotton et al. 2013）和 ETH3D（Schöps et al. 2017）评估三维重建，并使用 CO3D v2（Reizenstein et al. 2021）评估相机位姿。2）对于空间推理，我们在 MindCube Tiny（Yin et al. 2025）、OmniSpatial（Jia et al. 2025）、OST-Bench（Lin et al. 2025b）和 SPAR-Bench（Zhang et al. 2025a）的官方测试集上进行评估。3）对于光流估计，我们在 KITTI 训练集（Geiger et al. 2013）上评估零样本迁移，不在该基准上进行微调。

> <span style="color:#3B82F6"><strong>Para. 51:</strong></span> **Baselines and Metrics.** We organize our comparisons into three task groups. 1) For visual geometry, we compare SPARGen with the specialized models DUSt3R (Wang et al. 2024b), FLARE (Zhang et al. 2025b), and VGGT (Wang et al. 2025a), as well as the unified model G²VLM (Hu et al. 2026). We report AbsRel and $\delta_1$ for depth estimation; reconstruction accuracy error (Acc.) and completeness error (Comp.) for 3D reconstruction; and relative rotation accuracy (RRA), relative translation accuracy (RTA), and area under the curve (AUC) for camera pose estimation. 2) For optical flow, we compare with RAFT (Teed and Deng 2020), GMFlow (Xu et al. 2022), and FlowFormer (Huang et al. 2022), reporting end-point error (EPE) and F1-all. 3) For spatial reasoning, we compare with the proprietary models GPT-4o (Hurst et al. 2024) and Claude Sonnet 4.6 (Anthropic 2026); general-purpose vision-language models Qwen2.5-VL-7B/72B (Bai et al. 2025), LLaVA-Video (Zhang et al. 2024), and LLaVA-OneVision (Li et al. 2024); the spatial-specialist models Spatial-MLLM (Ma et al. 2025) and VLM3R-7B (Fan et al. 2026); and the unified model G²VLM (Hu et al. 2026). We report answer accuracy on each benchmark.

> <span style="color:#F59E0B"><strong>Para. 51[CN]:</strong></span> **基线与指标。** 我们将比较划分为三类任务。1）对于视觉几何，我们将 SPARGen 与专用模型 DUSt3R（Wang et al. 2024b）、FLARE（Zhang et al. 2025b）、VGGT（Wang et al. 2025a）以及统一模型 G²VLM（Hu et al. 2026）进行比较。深度估计报告 AbsRel 和 $\delta_1$；三维重建报告重建准确度误差（Acc.）和完整度误差（Comp.）；相机位姿估计报告相对旋转准确率（RRA）、相对平移准确率（RTA）和曲线下面积（AUC）。2）对于光流，我们与 RAFT（Teed and Deng 2020）、GMFlow（Xu et al. 2022）和 FlowFormer（Huang et al. 2022）比较，并报告端点误差（EPE）和 F1-all。3）对于空间推理，我们与专有模型 GPT-4o（Hurst et al. 2024）和 Claude Sonnet 4.6（Anthropic 2026），通用视觉语言模型 Qwen2.5-VL-7B/72B（Bai et al. 2025）、LLaVA-Video（Zhang et al. 2024）和 LLaVA-OneVision（Li et al. 2024），空间专用模型 Spatial-MLLM（Ma et al. 2025）和 VLM3R-7B（Fan et al. 2026），以及统一模型 G²VLM（Hu et al. 2026）进行比较。我们报告各基准上的答案准确率。

> <span style="color:#3B82F6"><strong>Para. 52:</strong></span> **Implementation Details.** We initialize SPARGen from the pretrained Bagel weights and jointly optimize the token-sequence and dense-field generation objectives. The VAE encoder and decoder are frozen, while all other model parameters are fine-tuned for 100K iterations using AdamW on 64 NVIDIA H100 GPUs. For depth estimation, point map reconstruction, and optical flow estimation, the maximum ViT input resolutions are set to 518, 448, and 980, respectively, and the corresponding maximum VAE input resolutions are 1024, 512, and 1024. We set the sequence-loss weight in Eq. 12 to $\lambda=0.25$ and use a learning rate of $2.5\times10^{-5}$. SPARGen predicts normalized depth and point maps, and therefore, like VGGT (Wang et al. 2025a) and G²VLM (Hu et al. 2026), cannot recover metric scale. We follow their standard scale-aligned evaluation protocol.

> <span style="color:#F59E0B"><strong>Para. 52[CN]:</strong></span> **实现细节。** 我们使用预训练 Bagel 权重初始化 SPARGen，并联合优化词元序列生成目标和稠密场生成目标。VAE 编码器和解码器保持冻结，其余所有模型参数使用 AdamW、在 64 块 NVIDIA H100 GPU 上微调 100K 次迭代。对于深度估计、点图重建和光流估计，最大 ViT 输入分辨率分别设为 518、448 和 980，相应的最大 VAE 输入分辨率分别为 1024、512 和 1024。我们将式（12）中的序列损失权重设为 $\lambda=0.25$，学习率设为 $2.5\times10^{-5}$。SPARGen 预测归一化深度和点图，因此与 VGGT（Wang et al. 2025a）和 G²VLM（Hu et al. 2026）一样，无法恢复度量尺度。我们遵循它们的标准尺度对齐评估协议。

> <span style="color:#3B82F6"><strong>Para. 53:</strong></span> More details can be found in the appendix.

> <span style="color:#F59E0B"><strong>Para. 53[CN]:</strong></span> 更多细节见附录。

### 4.2 Comparisons with Prior Work

### 4.2 与先前工作的比较

> <span style="color:#3B82F6"><strong>Para. 54:</strong></span> We compare SPARGen with specialized models and spatially unified models across visual geometry, spatial reasoning, and optical flow benchmarks. SPARGen remains competitive with specialized geometry and flow models, and achieves the strongest spatial-reasoning performance among the compared models. These results demonstrate that spatial capabilities can be supported within a native multimodal model.

> <span style="color:#F59E0B"><strong>Para. 54[CN]:</strong></span> 我们在视觉几何、空间推理和光流基准上，将 SPARGen 与专用模型和空间统一模型进行比较。SPARGen 与专用几何模型和光流模型相比仍具有竞争力，并在参与比较的模型中取得最强的空间推理性能。这些结果表明，原生多模态模型能够支持空间能力。

> <span style="color:#3B82F6"><strong>Para. 55:</strong></span> **Visual Geometry.** Table 1 reports results on depth estimation, point map reconstruction, and camera pose estimation. Compared with the most relevant spatially unified baseline, G²VLM, SPARGen performs better on most metrics. In particular, it improves both depth metrics on Sintel, reduces AbsRel while matching $\delta_1$ on NYU-v2, and achieves better reconstruction results on 7Scenes. It also improves camera pose estimation across all three CO3D v2 metrics. Although specialized geometry models such as VGGT retain an advantage on several reconstruction metrics, SPARGen substantially narrows the gap with the native unified model.

> <span style="color:#F59E0B"><strong>Para. 55[CN]:</strong></span> **视觉几何。** 表1报告了深度估计、点图重建和相机位姿估计结果。与最相关的空间统一基线 G²VLM 相比，SPARGen 在多数指标上表现更好。具体而言，它改善了 Sintel 上的两个深度指标，在 NYU-v2 上降低 AbsRel 并取得相同的 $\delta_1$，同时在 7Scenes 上取得更好的重建结果。它还改善了 CO3D v2 的全部三项相机位姿指标。尽管 VGGT 等专用几何模型在若干重建指标上仍具有优势，SPARGen 已显著缩小原生统一模型与它们之间的差距。

---

<!-- Page 6 -->

## Table 1

| Model | Sintel AbsRel↓ | Sintel $\delta_1$↑ | NYU-v2 AbsRel↓ | NYU-v2 $\delta_1$↑ | 7Scenes Acc.↓ | 7Scenes Comp.↓ | ETH3D Acc.↓ | ETH3D Comp.↓ | CO3Dv2 RRA@30↑ | CO3Dv2 RTA@30↑ | CO3Dv2 AUC@30↑ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| *Specialized Geometry Models* |  |  |  |  |  |  |  |  |  |  |  |
| FLARE (Zhang et al. 2025b) | 0.409 | 0.438 | 0.164 | 0.740 | 0.035 | 0.043 | 0.470 | 0.667 | 97.08 | 94.31 | 77.99 |
| DUSt3R (Wang et al. 2024b) | 0.362 | 0.557 | 0.134 | 0.833 | 0.026 | 0.035 | 0.360 | 0.401 | 98.34 | 94.09 | 79.33 |
| VGGT (Wang et al. 2025a) | **0.265** | **0.676** | **0.065** | **0.938** | **0.022** | **0.032** | **0.311** | **0.372** | **98.79** | **96.89** | **89.78** |
| *Spatial Unified Models* |  |  |  |  |  |  |  |  |  |  |  |
| G²VLM (Hu et al. 2026) | 0.257 | 0.674 | 0.079 | **0.935** | 0.062 | 0.031 | 0.539 | **0.355** | 96.69 | 92.22 | 56.85 |
| **SPARGen (Ours)** | **0.235** | **0.725** | **0.071** | **0.935** | **0.034** | **0.028** | **0.393** | 0.445 | **96.84** | **94.33** | **74.32** |

> <span style="color:#3B82F6"><strong>Para. 56:</strong></span> Table 1: Comparison across depth estimation, point map estimation, and camera pose estimation benchmarks. **Bold** indicates the best performance within each model group.

> <span style="color:#F59E0B"><strong>Para. 56[CN]:</strong></span> 表1：深度估计、点图估计和相机位姿估计基准上的比较。**粗体**表示每个模型组内的最佳性能。

## Table 2

| Model | MindCube Avg. | Rotation | Among | Around | OmniSpatial Avg. | SI | PT | OST Avg. | A. State | A. Info | AO. | SPAR Avg. | Low | Medium | High |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| *Proprietary Models* |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| GPT-4o (Hurst et al. 2024) | 41.52 | 34.50 | 41.67 | 46.80 | 42.39 | 48.67 | 39.04 | 51.42 | 40.93 | 68.38 | 39.25 | 37.88 | 35.36 | 28.40 | 43.27 |
| Claude Sonnet 4.6 (Anthropic 2026) | 44.19 | 42.50 | 43.00 | 48.40 | 53.89 | 67.00 | 46.88 | 42.18 | 35.84 | 63.30 | 29.35 | 37.55 | 36.63 | 35.33 | 39.20 |
| *Open-Source Models* |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Qwen2.5-VL-7B (Bai et al. 2025) | 36.00 | 37.50 | 32.33 | 43.60 | 45.99 | 54.67 | 41.35 | 40.08 | 38.48 | 50.20 | 31.27 | 34.84 | 26.36 | 36.09 | 41.97 |
| Qwen2.5-VL-72B (Bai et al. 2025) | 41.71 | 40.50 | 40.67 | 45.20 | 52.03 | 61.33 | 47.06 | 49.23 | 39.05 | 65.78 | 37.37 | 39.34 | 34.29 | 36.84 | 44.80 |
| LLaVA-Video-7B (Zhang et al. 2024) | 43.24 | 36.50 | 43.50 | 48.00 | 49.71 | 55.33 | 46.70 | 44.54 | 32.31 | 62.25 | 32.29 | 34.09 | 24.99 | 31.77 | 43.10 |
| LLaVA-OneVision-7B (Li et al. 2024) | 40.86 | 33.50 | 37.17 | 55.60 | 46.92 | 52.67 | 43.85 | 35.87 | 24.97 | 44.85 | 31.22 | 29.47 | 19.88 | 30.49 | 37.66 |
| Bagel-7B (Deng et al. 2025a) | 41.20 | 36.50 | 39.50 | 52.40 | 45.29 | 49.33 | 43.14 | 32.73 | 42.87 | 26.49 | 35.11 | 39.51 | 34.59 | 36.19 | 45.15 |
| *Spatial Expert Models* |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| VLM3R-7B (Fan et al. 2026) | 37.90 | 36.50 | 42.50 | 28.00 | 46.69 | 49.33 | 45.28 | <u>51.03</u> | 38.32 | <u>68.30</u> | <u>39.35</u> | <u>41.89</u> | 36.36 | 28.38 | <u>51.92</u> |
| Spatial-MLLM-7B (Ma et al. 2025) | <u>66.19</u> | <u>41.00</u> | <u>66.83</u> | <u>74.80</u> | <u>45.30</u> | <u>47.00</u> | <u>44.39</u> | 39.90 | 32.28 | 46.80 | 36.08 | 33.92 | 23.90 | 33.74 | 42.95 |
| *Spatial Unified Models* |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| G²VLM-7B (Hu et al. 2026) | 28.48 | 25.50 | 30.17 | 26.80 | 42.62 | 44.33 | 41.71 | 28.80 | 27.13 | 35.43 | 23.24 | 38.73 | <u>51.24</u> | 28.82 | 31.27 |
| **SPARGen-7B (Ours)** | **76.04** | **63.50** | **79.16** | **78.60** | **54.00** | **55.33** | **53.29** | **56.02** | **47.10** | **72.30** | **43.98** | **66.60** | **49.35** | **74.04** | **79.25** |

> <span style="color:#3B82F6"><strong>Para. 57:</strong></span> Table 2: Results on spatial-reasoning benchmarks. **Bold** and <u>underlined</u> values indicate the best and second-best results among non-proprietary models.

> <span style="color:#F59E0B"><strong>Para. 57[CN]:</strong></span> 表2：空间推理基准上的结果。**粗体**和<u>下划线</u>数值分别表示非专有模型中的最佳和次佳结果。

## Table 3

| Model | KITTI EPE↓ | KITTI F1-all↓ |
|---|---:|---:|
| RAFT (Teed and Deng 2020) | 5.03 | 17.45 |
| GMFlow (Xu et al. 2022) | 7.77 | 23.40 |
| FlowFormer (Huang et al. 2022) | 4.10 | 14.51 |
| SPARGen w/o refinement | 5.26 | 21.82 |
| **SPARGen (Ours)** | **4.09** | **13.34** |

> <span style="color:#3B82F6"><strong>Para. 58:</strong></span> Table 3: Zero-shot optical flow results on KITTI. **Bold** values indicate the best performance.

> <span style="color:#F59E0B"><strong>Para. 58[CN]:</strong></span> 表3：KITTI 上的零样本光流结果。**粗体**数值表示最佳性能。

## Table 4

| Model | 7Scenes Acc.↓ | 7Scenes Comp.↓ | KITTI EPE↓ | KITTI F1-all↓ | SPAR Avg.↑ | Low↑ | Med.↑ | High↑ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| w/o Geometry | – | – | 4.29 | 14.73 | 62.41 | 45.97 | 66.49 | 75.59 |
| w/o Flow | 0.040 | 0.038 | – | – | 65.92 | 48.41 | 73.52 | 78.75 |
| w/o Reasoning | 0.037 | 0.031 | **4.06** | **13.01** | – | – | – | – |
| **SPARGen (Ours)** | **0.034** | **0.028** | 4.09 | 13.34 | **66.60** | **49.35** | **74.04** | **79.25** |

> <span style="color:#3B82F6"><strong>Para. 59:</strong></span> Table 4: Ablation of geometry, optical flow, and spatial-reasoning supervision. **Bold** values indicate the best performance.

> <span style="color:#F59E0B"><strong>Para. 59[CN]:</strong></span> 表4：几何、光流和空间推理监督的消融实验。**粗体**数值表示最佳性能。

> <span style="color:#3B82F6"><strong>Para. 60:</strong></span> **Spatial Understanding and Reasoning.** As shown in Table 2, SPARGen achieves the highest average score on all four spatial-reasoning benchmarks and ranks first in 13 of the 15 reported categories among the compared non-proprietary models. Relative to the strongest competing result on each benchmark, SPARGen improves the average score by 9.85 points on MindCube, 1.97 points on OmniSpatial, 4.99 points on OST, and 24.71 points on SPAR. The gains are particularly pronounced on the medium and high subsets of SPAR. While SPARGen benefits from a 7B foundation backbone, its gains cannot be attributed solely to model scale, as it also outperforms substantially larger open-source baselines such as Qwen2.5-VL-72B.

> <span style="color:#F59E0B"><strong>Para. 60[CN]:</strong></span> **空间理解与推理。** 如表2所示，SPARGen 在全部四个空间推理基准上取得最高平均分，并在所比较的非专有模型中，于报告的15个类别中的13个类别排名第一。相对于每个基准上的最强竞争结果，SPARGen 在 MindCube、OmniSpatial、OST 和 SPAR 上的平均分分别提高 9.85、1.97、4.99 和 24.71 分。SPAR 的中等与高难度子集上的增益尤其显著。尽管 SPARGen 受益于 7B 基础骨干网络，但其提升不能仅归因于模型规模，因为它也显著优于 Qwen2.5-VL-72B 等规模大得多的开源基线。

> <span style="color:#3B82F6"><strong>Para. 61:</strong></span> **Optical Flow Estimation.** Table 3 reports zero-shot optical flow results on KITTI. SPARGen achieves an EPE of 4.09 and an F1-all score of 13.34, outperforming the compared methods on both metrics. These results show that SPARGen can learn effective dense correspondence estimation through its native generation pathway.

> <span style="color:#F59E0B"><strong>Para. 61[CN]:</strong></span> **光流估计。** 表3报告了 KITTI 上的零样本光流结果。SPARGen 取得 4.09 的 EPE 和 13.34 的 F1-all，在两项指标上均优于参与比较的方法。这些结果表明，SPARGen 能够通过其原生生成路径学习有效的稠密对应关系估计。

---

<!-- Page 7 -->

## Figure 3 — In-figure transcription

- Input images
- Predicted point maps
- Input frame 1
- Input frame 2
- Initial flow prediction
- Refined flow prediction
- Initial endpoint error
- Refined endpoint error
- Input image
- Predicted depth

- 输入图像
- 预测点图
- 输入帧1
- 输入帧2
- 初始光流预测
- 细化光流预测
- 初始端点误差
- 细化端点误差
- 输入图像
- 预测深度

> <span style="color:#3B82F6"><strong>Para. 62:</strong></span> Figure 3: Qualitative results of SPARGen on point map reconstruction, optical flow estimation, and depth estimation. For optical flow, we show the predictions and error maps before and after refinement.

> <span style="color:#F59E0B"><strong>Para. 62[CN]:</strong></span> 图3：SPARGen 在点图重建、光流估计和深度估计上的定性结果。对于光流，我们展示了细化前后的预测结果和误差图。

> <span style="color:#3B82F6"><strong>Para. 63:</strong></span> **Qualitative Results.** Figure 3 presents representative predictions for 3D reconstruction, optical flow estimation, and depth estimation. For 3D reconstruction, SPARGen recovers coherent global layouts in both indoor and outdoor scenes. Its optical flow predictions capture the dominant motion of foreground vehicles while producing relatively consistent estimates over static background regions. The refinement stage further corrects residual misalignments in the initial predictions. For depth estimation, SPARGen recovers the overall near-to-far structure of the scene and preserves the boundaries of major objects.

> <span style="color:#F59E0B"><strong>Para. 63[CN]:</strong></span> **定性结果。** 图3展示了三维重建、光流估计和深度估计的代表性预测。对于三维重建，SPARGen 在室内和室外场景中均能恢复连贯的全局布局。其光流预测能够捕获前景车辆的主要运动，同时在静态背景区域产生相对一致的估计。细化阶段进一步纠正初始预测中的残余错位。对于深度估计，SPARGen 能够恢复场景整体的由近及远结构，并保留主要物体的边界。

> <span style="color:#3B82F6"><strong>Para. 64:</strong></span> Overall, SPARGen improves over the existing unified baseline on visual geometry, achieves the strongest spatial-reasoning results, and remains competitive with specialized optical flow methods, all within a shared instruction-conditioned generative framework.

> <span style="color:#F59E0B"><strong>Para. 64[CN]:</strong></span> 总体而言，SPARGen 在视觉几何方面优于现有统一基线，取得最强的空间推理结果，并与专用光流方法保持竞争力；所有这些能力均包含在共享的指令条件生成框架内。

### 4.3 Ablation Studies and Analysis

### 4.3 消融研究与分析

> <span style="color:#3B82F6"><strong>Para. 65:</strong></span> To examine whether the results are consistent with complementary effects among different supervision types, we train variants with one supervision category removed at a time.

> <span style="color:#F59E0B"><strong>Para. 65[CN]:</strong></span> 为检验这些结果是否与不同监督类型之间的互补效应一致，我们训练了每次移除一种监督类别的模型变体。

> <span style="color:#3B82F6"><strong>Para. 66:</strong></span> **(1) Removing Geometry Supervision.** We remove geometry supervision. This ablation examines whether 3D supervision provides transferable structural information for dense correspondence and spatial reasoning.

> <span style="color:#F59E0B"><strong>Para. 66[CN]:</strong></span> **（1）移除几何监督。** 我们移除几何监督。该消融实验考察三维监督是否能够为稠密对应关系和空间推理提供可迁移的结构信息。

> <span style="color:#3B82F6"><strong>Para. 67:</strong></span> **(2) Removing Optical Flow Supervision.** We remove optical flow supervision. This setting evaluates whether dense correspondence learning contributes to multi-view reconstruction and spatial reasoning.

> <span style="color:#F59E0B"><strong>Para. 67[CN]:</strong></span> **（2）移除光流监督。** 我们移除光流监督。该设置评估稠密对应关系学习是否有助于多视图重建和空间推理。

> <span style="color:#3B82F6"><strong>Para. 68:</strong></span> **(3) Removing Reasoning Supervision.** We remove spatial-reasoning and question-answering supervision. This ablation examines whether high-level semantic objectives can improve dense geometric perception.

> <span style="color:#F59E0B"><strong>Para. 68[CN]:</strong></span> **（3）移除推理监督。** 我们移除空间推理和问答监督。该消融实验考察高层语义目标是否能够改善稠密几何感知。

> <span style="color:#3B82F6"><strong>Para. 69:</strong></span> **Results & Analysis.** Table 4 presents the results. (1) Removing geometry supervision degrades both optical flow estimation and spatial reasoning, suggesting that explicit 3D supervision may provide structural information useful for dense correspondence and language-based reasoning. (2) Removing optical flow supervision increases the reconstruction accuracy and completeness errors on 7Scenes and reduces the average SPAR score, consistent with dense correspondence supervision benefiting cross-view consistency and spatial reasoning. (3) Removing reasoning supervision slightly degrades reconstruction, suggesting a possible benefit of high-level semantic supervision for geometric representation learning. However, optical flow performance improves slightly in the absence of reasoning supervision. We attribute this to a mild capacity competition in multi-task learning: while semantic reasoning aids static 3D structure, the autoregressive token generation slightly competes for the MoT backbone’s capacity against dynamic dense-field prediction.

> <span style="color:#F59E0B"><strong>Para. 69[CN]:</strong></span> **结果与分析。** 表4给出了实验结果。（1）移除几何监督会同时降低光流估计和空间推理性能，表明显式三维监督可以提供有助于稠密对应关系和基于语言推理的结构信息。（2）移除光流监督会增大 7Scenes 上的重建准确度误差和完整度误差，并降低 SPAR 平均分，这与稠密对应关系监督有益于跨视图一致性和空间推理的结论一致。（3）移除推理监督会使重建性能略微下降，表明高层语义监督可能有益于几何表征学习。然而，在没有推理监督时，光流性能略有提高。我们将其归因于多任务学习中的轻微容量竞争：虽然语义推理有助于静态三维结构，但自回归词元生成会与动态稠密场预测轻微竞争 MoT 骨干网络的容量。

## 5 Conclusion

## 5 结论

> <span style="color:#3B82F6"><strong>Para. 70:</strong></span> We present SPARGen, a unified multimodal framework that formulates spatial perception and reasoning as instruction-conditioned generation. SPARGen serializes compact structured and linguistic outputs as token sequences and represents dense geometric and correspondence fields as image-aligned outputs. It thereby uses the native autoregressive and rectified-flow pathways of a shared MoT backbone without external modules. Across visual-geometry, optical flow, and spatial-reasoning benchmarks, SPARGen remains competitive with specialized perception methods, and achieves strong spatial-reasoning performance. Our ablations provide preliminary evidence consistent with complementary effects among geometry, correspondence, and reasoning supervision. These findings demonstrate the feasibility of using native multimodal generation as a shared interface for spatial perception and reasoning tasks.

> <span style="color:#F59E0B"><strong>Para. 70[CN]:</strong></span> 我们提出 SPARGen，这是一个将空间感知与推理表述为指令条件生成的统一多模态框架。SPARGen 将紧凑的结构化输出和语言输出序列化为词元序列，并将稠密几何场和对应关系场表示为图像对齐输出。由此，它无需外部模块即可使用共享 MoT 骨干网络的原生自回归路径和整流流路径。在视觉几何、光流和空间推理基准上，SPARGen 与专用感知方法相比保持竞争力，并取得强大的空间推理性能。我们的消融实验提供了初步证据，表明几何、对应关系和推理监督之间存在互补效应。这些发现证明了使用原生多模态生成作为空间感知与推理任务共享接口的可行性。

> <span style="color:#3B82F6"><strong>Para. 71:</strong></span> **Limitations.** While leveraging a frozen VAE allows SPARGen to reuse pretrained multimodal generative pathways, VAE spatial compression inherently poses a bottleneck for geometric edges and high-precision physical quantities.

> <span style="color:#F59E0B"><strong>Para. 71[CN]:</strong></span> **局限性。** 尽管使用冻结的 VAE 使 SPARGen 能够复用预训练多模态生成路径，但 VAE 的空间压缩天然会对几何边缘和高精度物理量形成瓶颈。

---

<!-- Page 8 -->

# References

# 参考文献

> <span style="color:#3B82F6"><strong>Para. 72:</strong></span> Anthropic. 2026. Claude Sonnet 4.6 System Card. Technical report, Anthropic. Accessed: 2026-07-27.

> <span style="color:#F59E0B"><strong>Para. 72[CN]:</strong></span> Anthropic。2026。《Claude Sonnet 4.6 系统卡》。技术报告，Anthropic。访问日期：2026-07-27。

> <span style="color:#3B82F6"><strong>Para. 73:</strong></span> Azuma, D.; Miyanishi, T.; Kurita, S.; and Kawanabe, M. 2022. Scanqa: 3d question answering for spatial scene understanding. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, 19129–19139.

> <span style="color:#F59E0B"><strong>Para. 73[CN]:</strong></span> Azuma, D.; Miyanishi, T.; Kurita, S.; and Kawanabe, M. 2022。《ScanQA：面向空间场景理解的三维问答》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，19129–19139。

> <span style="color:#3B82F6"><strong>Para. 74:</strong></span> Bai, S.; Chen, K.; Liu, X.; Wang, J.; Ge, W.; Song, S.; Dang, K.; Wang, P.; Wang, S.; Tang, J.; Zhong, H.; Zhu, Y.; Yang, M.; Li, Z.; Wan, J.; Wang, P.; Ding, W.; Fu, Z.; Xu, Y.; Ye, J.; Zhang, X.; Xie, T.; Cheng, Z.; Zhang, H.; Yang, Z.; Xu, H.; and Lin, J. 2025. Qwen2.5-VL Technical Report. *arXiv preprint arXiv:2502.13923*.

> <span style="color:#F59E0B"><strong>Para. 74[CN]:</strong></span> Bai, S.; Chen, K.; Liu, X.; Wang, J.; Ge, W.; Song, S.; Dang, K.; Wang, P.; Wang, S.; Tang, J.; Zhong, H.; Zhu, Y.; Yang, M.; Li, Z.; Wan, J.; Wang, P.; Ding, W.; Fu, Z.; Xu, Y.; Ye, J.; Zhang, X.; Xie, T.; Cheng, Z.; Zhang, H.; Yang, Z.; Xu, H.; and Lin, J. 2025。《Qwen2.5-VL 技术报告》。*arXiv 预印本 arXiv:2502.13923*。

> <span style="color:#3B82F6"><strong>Para. 75:</strong></span> Bozic, A.; Palafox, P.; Thies, J.; Dai, A.; and Nießner, M. 2021. Transformerfusion: Monocular rgb scene reconstruction using transformers. *Advances in Neural Information Processing Systems*, 34: 1403–1414.

> <span style="color:#F59E0B"><strong>Para. 75[CN]:</strong></span> Bozic, A.; Palafox, P.; Thies, J.; Dai, A.; and Nießner, M. 2021。《TransformerFusion：使用 Transformer 的单目 RGB 场景重建》。*神经信息处理系统进展*，34：1403–1414。

> <span style="color:#3B82F6"><strong>Para. 76:</strong></span> Chameleon Team. 2024. Chameleon: Mixed-Modal Early-Fusion Foundation Models. *arXiv preprint arXiv:2405.09818*.

> <span style="color:#F59E0B"><strong>Para. 76[CN]:</strong></span> Chameleon Team。2024。《Chameleon：混合模态早期融合基础模型》。*arXiv 预印本 arXiv:2405.09818*。

> <span style="color:#3B82F6"><strong>Para. 77:</strong></span> Chen, B.; Xu, Z.; Kirmani, S.; Ichter, B.; Sadigh, D.; Guibas, L.; and Xia, F. 2024a. Spatialvlm: Endowing vision-language models with spatial reasoning capabilities. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 14455–14465.

> <span style="color:#F59E0B"><strong>Para. 77[CN]:</strong></span> Chen, B.; Xu, Z.; Kirmani, S.; Ichter, B.; Sadigh, D.; Guibas, L.; and Xia, F. 2024a。《SpatialVLM：赋予视觉语言模型空间推理能力》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，14455–14465。

> <span style="color:#3B82F6"><strong>Para. 78:</strong></span> Chen, Y.; Yang, S.; Huang, H.; Wang, T.; Xu, R.; Lyu, R.; Lin, D.; and Pang, J. 2024b. Grounded 3d-llm with referent tokens. *arXiv preprint arXiv:2405.10370*.

> <span style="color:#F59E0B"><strong>Para. 78[CN]:</strong></span> Chen, Y.; Yang, S.; Huang, H.; Wang, T.; Xu, R.; Lyu, R.; Lin, D.; and Pang, J. 2024b。《带有指称词元的具身三维大语言模型》。*arXiv 预印本 arXiv:2405.10370*。

> <span style="color:#3B82F6"><strong>Para. 79:</strong></span> Cheng, A.-C.; Yin, H.; Fu, Y.; Guo, Q.; Yang, R.; Kautz, J.; Wang, X.; and Liu, S. 2024. SpatialRGPT: Grounded Spatial Reasoning in Vision Language Models. In *Advances in Neural Information Processing Systems*.

> <span style="color:#F59E0B"><strong>Para. 79[CN]:</strong></span> Cheng, A.-C.; Yin, H.; Fu, Y.; Guo, Q.; Yang, R.; Kautz, J.; Wang, X.; and Liu, S. 2024。《SpatialRGPT：视觉语言模型中的具身空间推理》。载于 *神经信息处理系统进展*。

> <span style="color:#3B82F6"><strong>Para. 80:</strong></span> Cong, Z.; Zhao, Q.; Jeon, M.; and Tulsiani, S. 2026. Flow3r: Factored flow prediction for scalable visual geometry learning. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 438–447.

> <span style="color:#F59E0B"><strong>Para. 80[CN]:</strong></span> Cong, Z.; Zhao, Q.; Jeon, M.; and Tulsiani, S. 2026。《Flow3R：用于可扩展视觉几何学习的分解光流预测》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，438–447。

> <span style="color:#3B82F6"><strong>Para. 81:</strong></span> Deng, C.; Zhu, D.; Li, K.; Gou, C.; Li, F.; Wang, Z.; Zhong, S.; Yu, W.; Nie, X.; Song, Z.; et al. 2025a. Emerging properties in unified multimodal pretraining. *arXiv preprint arXiv:2505.14683*.

> <span style="color:#F59E0B"><strong>Para. 81[CN]:</strong></span> Deng, C.; Zhu, D.; Li, K.; Gou, C.; Li, F.; Wang, Z.; Zhong, S.; Yu, W.; Nie, X.; Song, Z.; et al. 2025a。《统一多模态预训练中的涌现属性》。*arXiv 预印本 arXiv:2505.14683*。

> <span style="color:#3B82F6"><strong>Para. 82:</strong></span> Deng, J.; He, T.; Jiang, L.; Wang, T.; Dayoub, F.; and Reid, I. 2025b. 3d-llava: Towards generalist 3d lmms with omni superpoint transformer. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, 3772–3782.

> <span style="color:#F59E0B"><strong>Para. 82[CN]:</strong></span> Deng, J.; He, T.; Jiang, L.; Wang, T.; Dayoub, F.; and Reid, I. 2025b。《3D-LLaVA：通过全能超点 Transformer 迈向通用三维大型多模态模型》。载于 *计算机视觉与模式识别会议论文集*，3772–3782。

> <span style="color:#3B82F6"><strong>Para. 83:</strong></span> Edstedt, J.; Athanasiadis, I.; Wadenbäck, M.; and Felsberg, M. 2023. DKM: Dense Kernelized Feature Matching for Geometry Estimation. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*.

> <span style="color:#F59E0B"><strong>Para. 83[CN]:</strong></span> Edstedt, J.; Athanasiadis, I.; Wadenbäck, M.; and Felsberg, M. 2023。《DKM：用于几何估计的稠密核化特征匹配》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*。

> <span style="color:#3B82F6"><strong>Para. 84:</strong></span> Edstedt, J.; Sun, Q.; Bökman, G.; Wadenbäck, M.; and Felsberg, M. 2024. Roma: Robust dense feature matching. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, 19790–19800.

> <span style="color:#F59E0B"><strong>Para. 84[CN]:</strong></span> Edstedt, J.; Sun, Q.; Bökman, G.; Wadenbäck, M.; and Felsberg, M. 2024。《RoMa：稳健的稠密特征匹配》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，19790–19800。

> <span style="color:#3B82F6"><strong>Para. 85:</strong></span> Fan, Z.; Zhang, J.; Li, R.; Zhang, J.; Chen, R.; Hu, H.; Wang, K.; Wang, P.; Qu, H.; Zhou, S.; et al. 2026. Vlm-3r: Vision-language models augmented with instruction-aligned 3d reconstruction. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 31054–31065.

> <span style="color:#F59E0B"><strong>Para. 85[CN]:</strong></span> Fan, Z.; Zhang, J.; Li, R.; Zhang, J.; Chen, R.; Hu, H.; Wang, K.; Wang, P.; Qu, H.; Zhou, S.; et al. 2026。《VLM-3R：通过指令对齐三维重建增强的视觉语言模型》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，31054–31065。

> <span style="color:#3B82F6"><strong>Para. 86:</strong></span> Geiger, A.; Lenz, P.; Stiller, C.; and Urtasun, R. 2013. Vision meets Robotics: The KITTI Dataset. *International Journal of Robotics Research (IJRR)*.

> <span style="color:#F59E0B"><strong>Para. 86[CN]:</strong></span> Geiger, A.; Lenz, P.; Stiller, C.; and Urtasun, R. 2013。《视觉遇见机器人学：KITTI 数据集》。*国际机器人研究期刊（IJRR）*。

> <span style="color:#3B82F6"><strong>Para. 87:</strong></span> Hu, W.; Lin, J.; Long, Y.; Ran, Y.; Jiang, L.; Wang, Y.; Zhu, C.; Xu, R.; Wang, T.; and Pang, J. 2026. G²VLM: Geometry Grounded Vision Language Model with Unified 3D Reconstruction and Spatial Reasoning. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 9535–9546.

> <span style="color:#F59E0B"><strong>Para. 87[CN]:</strong></span> Hu, W.; Lin, J.; Long, Y.; Ran, Y.; Jiang, L.; Wang, Y.; Zhu, C.; Xu, R.; Wang, T.; and Pang, J. 2026。《G²VLM：统一三维重建与空间推理的几何具身视觉语言模型》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，9535–9546。

> <span style="color:#3B82F6"><strong>Para. 88:</strong></span> Huang, H.; Chen, Y.; Wang, Z.; Huang, R.; Xu, R.; Wang, T.; Liu, L.; Cheng, X.; Zhao, Y.; Pang, J.; et al. 2024. Chat-scene: Bridging 3d scene and large language models with object identifiers. *Advances in Neural Information Processing Systems*, 37: 113991–114017.

> <span style="color:#F59E0B"><strong>Para. 88[CN]:</strong></span> Huang, H.; Chen, Y.; Wang, Z.; Huang, R.; Xu, R.; Wang, T.; Liu, L.; Cheng, X.; Zhao, Y.; Pang, J.; et al. 2024。《Chat-Scene：使用物体标识符连接三维场景与大语言模型》。*神经信息处理系统进展*，37：113991–114017。

> <span style="color:#3B82F6"><strong>Para. 89:</strong></span> Huang, Z.; Shi, X.; Zhang, C.; Wang, Q.; Cheung, K. C.; Qin, H.; Dai, J.; and Li, H. 2022. Flowformer: A transformer architecture for optical flow. In *European conference on computer vision*, 668–685. Springer.

> <span style="color:#F59E0B"><strong>Para. 89[CN]:</strong></span> Huang, Z.; Shi, X.; Zhang, C.; Wang, Q.; Cheung, K. C.; Qin, H.; Dai, J.; and Li, H. 2022。《FlowFormer：用于光流的 Transformer 架构》。载于 *欧洲计算机视觉会议*，668–685。Springer。

> <span style="color:#3B82F6"><strong>Para. 90:</strong></span> Hurst, A.; Lerer, A.; Goucher, A. P.; Perelman, A.; Ramesh, A.; Clark, A.; Ostrow, A.; Welihinda, A.; Hayes, A.; Radford, A.; et al. 2024. Gpt-4o system card. *arXiv preprint arXiv:2410.21276*.

> <span style="color:#F59E0B"><strong>Para. 90[CN]:</strong></span> Hurst, A.; Lerer, A.; Goucher, A. P.; Perelman, A.; Ramesh, A.; Clark, A.; Ostrow, A.; Welihinda, A.; Hayes, A.; Radford, A.; et al. 2024。《GPT-4o 系统卡》。*arXiv 预印本 arXiv:2410.21276*。

> <span style="color:#3B82F6"><strong>Para. 91:</strong></span> Jia, M.; Qi, Z.; Zhang, S.; Zhang, W.; Yu, X.; He, J.; Wang, H.; and Yi, L. 2025. Omnispatial: Towards comprehensive spatial reasoning benchmark for vision language models. *arXiv preprint arXiv:2506.03135*.

> <span style="color:#F59E0B"><strong>Para. 91[CN]:</strong></span> Jia, M.; Qi, Z.; Zhang, S.; Zhang, W.; Yu, X.; He, J.; Wang, H.; and Yi, L. 2025。《OmniSpatial：迈向视觉语言模型的综合空间推理基准》。*arXiv 预印本 arXiv:2506.03135*。

> <span style="color:#3B82F6"><strong>Para. 92:</strong></span> Ke, B.; Obukhov, A.; Huang, S.; Metzger, N.; Daudt, R. C.; and Schindler, K. 2024. Repurposing Diffusion-Based Image Generators for Monocular Depth Estimation. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*.

> <span style="color:#F59E0B"><strong>Para. 92[CN]:</strong></span> Ke, B.; Obukhov, A.; Huang, S.; Metzger, N.; Daudt, R. C.; and Schindler, K. 2024。《将基于扩散的图像生成器重新用于单目深度估计》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*。

> <span style="color:#3B82F6"><strong>Para. 93:</strong></span> Li, B.; Zhang, Y.; Guo, D.; Zhang, R.; Li, F.; Zhang, H.; Zhang, K.; Zhang, P.; Li, Y.; Liu, Z.; et al. 2024. Llava-onevision: Easy visual task transfer. *arXiv preprint arXiv:2408.03326*.

> <span style="color:#F59E0B"><strong>Para. 93[CN]:</strong></span> Li, B.; Zhang, Y.; Guo, D.; Zhang, R.; Li, F.; Zhang, H.; Zhang, K.; Zhang, P.; Li, Y.; Liu, Z.; et al. 2024。《LLaVA-OneVision：简易视觉任务迁移》。*arXiv 预印本 arXiv:2408.03326*。

> <span style="color:#3B82F6"><strong>Para. 94:</strong></span> Lin, H.; Chen, S.; Liew, J.; Chen, D. Y.; Li, Z.; Shi, G.; Feng, J.; and Kang, B. 2025a. Depth anything 3: Recovering the visual space from any views. *arXiv preprint arXiv:2511.10647*.

> <span style="color:#F59E0B"><strong>Para. 94[CN]:</strong></span> Lin, H.; Chen, S.; Liew, J.; Chen, D. Y.; Li, Z.; Shi, G.; Feng, J.; and Kang, B. 2025a。《Depth Anything 3：从任意视图恢复视觉空间》。*arXiv 预印本 arXiv:2511.10647*。

> <span style="color:#3B82F6"><strong>Para. 95:</strong></span> Lin, J.; Zhu, C.; Xu, R.; Mao, X.; Liu, X.; Wang, T.; and Pang, J. 2025b. OST-Bench: Evaluating the Capabilities of MLLMs in Online Spatio-Temporal Scene Understanding. In *Advances in Neural Information Processing Systems*, volume 38.

> <span style="color:#F59E0B"><strong>Para. 95[CN]:</strong></span> Lin, J.; Zhu, C.; Xu, R.; Mao, X.; Liu, X.; Wang, T.; and Pang, J. 2025b。《OST-Bench：评估大型多模态模型的在线时空场景理解能力》。载于 *神经信息处理系统进展*，第38卷。

> <span style="color:#3B82F6"><strong>Para. 96:</strong></span> Ma, W.; Ye, L.; de Melo, C. M.; Yuille, A.; and Chen, J. 2025. Spatialllm: A compound 3d-informed design towards spatially-intelligent large multimodal models. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, 17249–17260.

> <span style="color:#F59E0B"><strong>Para. 96[CN]:</strong></span> Ma, W.; Ye, L.; de Melo, C. M.; Yuille, A.; and Chen, J. 2025。《SpatialLLM：面向空间智能大型多模态模型的复合三维信息设计》。载于 *计算机视觉与模式识别会议论文集*，17249–17260。

> <span style="color:#3B82F6"><strong>Para. 97:</strong></span> Qi, Z.; Fang, Y.; Sun, Z.; Wu, X.; Wu, T.; Wang, J.; Lin, D.; and Zhao, H. 2024. Gpt4point: A unified framework for point-language understanding and generation. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 26417–26427.

> <span style="color:#F59E0B"><strong>Para. 97[CN]:</strong></span> Qi, Z.; Fang, Y.; Sun, Z.; Wu, X.; Wu, T.; Wang, J.; Lin, D.; and Zhao, H. 2024。《GPT4Point：用于点—语言理解与生成的统一框架》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，26417–26427。

> <span style="color:#3B82F6"><strong>Para. 98:</strong></span> Reizenstein, J.; Shapovalov, R.; Henzler, P.; Sbordone, L.; Labatut, P.; and Novotny, D. 2021. Common objects in 3d: Large-scale learning and evaluation of real-life 3d category reconstruction. In *Proceedings of the IEEE/CVF international conference on computer vision*, 10901–10911.

> <span style="color:#F59E0B"><strong>Para. 98[CN]:</strong></span> Reizenstein, J.; Shapovalov, R.; Henzler, P.; Sbordone, L.; Labatut, P.; and Novotny, D. 2021。《三维中的常见物体：真实世界三维类别重建的大规模学习与评估》。载于 *IEEE/CVF 国际计算机视觉会议论文集*，10901–10911。

---

<!-- Page 9 -->

> <span style="color:#3B82F6"><strong>Para. 99:</strong></span> Schönberger, J. L.; and Frahm, J.-M. 2016. Structure-from-Motion Revisited. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*.

> <span style="color:#F59E0B"><strong>Para. 99[CN]:</strong></span> Schönberger, J. L.; and Frahm, J.-M. 2016。《重新审视运动恢复结构》。载于 *IEEE 计算机视觉与模式识别会议论文集*。

> <span style="color:#3B82F6"><strong>Para. 100:</strong></span> Schöps, T.; Schönberger, J. L.; Galliani, S.; Sattler, T.; Schindler, K.; Pollefeys, M.; and Geiger, A. 2017. A Multi-View Stereo Benchmark with High-Resolution Images and Multi-Camera Videos. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, 3260–3269.

> <span style="color:#F59E0B"><strong>Para. 100[CN]:</strong></span> Schöps, T.; Schönberger, J. L.; Galliani, S.; Sattler, T.; Schindler, K.; Pollefeys, M.; and Geiger, A. 2017。《包含高分辨率图像和多相机视频的多视图立体基准》。载于 *IEEE 计算机视觉与模式识别会议论文集*，3260–3269。

> <span style="color:#3B82F6"><strong>Para. 101:</strong></span> Shi, Y.; Song, Y.; and Shou, M. Z. 2026. Edit2Perceive: Image Editing Diffusion Models Are Strong Dense Perceivers. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*.

> <span style="color:#F59E0B"><strong>Para. 101[CN]:</strong></span> Shi, Y.; Song, Y.; and Shou, M. Z. 2026。《Edit2Perceive：图像编辑扩散模型是强大的稠密感知器》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*。

> <span style="color:#3B82F6"><strong>Para. 102:</strong></span> Shotton, J.; Glocker, B.; Zach, C.; Izadi, S.; Criminisi, A.; and Fitzgibbon, A. 2013. Scene coordinate regression forests for camera relocalization in RGB-D images. In *Proceedings of the IEEE conference on computer vision and pattern recognition*, 2930–2937.

> <span style="color:#F59E0B"><strong>Para. 102[CN]:</strong></span> Shotton, J.; Glocker, B.; Zach, C.; Izadi, S.; Criminisi, A.; and Fitzgibbon, A. 2013。《用于 RGB-D 图像相机重定位的场景坐标回归森林》。载于 *IEEE 计算机视觉与模式识别会议论文集*，2930–2937。

> <span style="color:#3B82F6"><strong>Para. 103:</strong></span> Silberman, N.; Hoiem, D.; Kohli, P.; and Fergus, R. 2012. Indoor segmentation and support inference from rgbd images. In *European conference on computer vision*, 746–760. Springer.

> <span style="color:#F59E0B"><strong>Para. 103[CN]:</strong></span> Silberman, N.; Hoiem, D.; Kohli, P.; and Fergus, R. 2012。《从 RGB-D 图像进行室内分割和支撑关系推断》。载于 *欧洲计算机视觉会议*，746–760。Springer。

> <span style="color:#3B82F6"><strong>Para. 104:</strong></span> Sun, J.; Shen, Z.; Wang, Y.; Bao, H.; and Zhou, X. 2021. LoFTR: Detector-Free Local Feature Matching with Transformers. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*.

> <span style="color:#F59E0B"><strong>Para. 104[CN]:</strong></span> Sun, J.; Shen, Z.; Wang, Y.; Bao, H.; and Zhou, X. 2021。《LoFTR：使用 Transformer 的无检测器局部特征匹配》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*。

> <span style="color:#3B82F6"><strong>Para. 105:</strong></span> Teed, Z.; and Deng, J. 2020. Raft: Recurrent all-pairs field transforms for optical flow. In *European conference on computer vision*, 402–419. Springer.

> <span style="color:#F59E0B"><strong>Para. 105[CN]:</strong></span> Teed, Z.; and Deng, J. 2020。《RAFT：用于光流的循环全对场变换》。载于 *欧洲计算机视觉会议*，402–419。Springer。

> <span style="color:#3B82F6"><strong>Para. 106:</strong></span> Wang, J.; Chen, M.; Karaca, N.; Vedaldi, A.; Rupprecht, C.; and Novotny, D. 2025a. Vggt: Visual geometry grounded transformer. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, 5294–5306.

> <span style="color:#F59E0B"><strong>Para. 106[CN]:</strong></span> Wang, J.; Chen, M.; Karaca, N.; Vedaldi, A.; Rupprecht, C.; and Novotny, D. 2025a。《VGGT：视觉几何具身 Transformer》。载于 *计算机视觉与模式识别会议论文集*，5294–5306。

> <span style="color:#3B82F6"><strong>Para. 107:</strong></span> Wang, J.; Chen, M.; Zhang, S.; Karaca, N.; Schönberger, J.; Labatut, P.; Bojanowski, P.; Novotny, D.; Vedaldi, A.; and Rupprecht, C. 2026. VGGT-Ω. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.

> <span style="color:#F59E0B"><strong>Para. 107[CN]:</strong></span> Wang, J.; Chen, M.; Zhang, S.; Karaca, N.; Schönberger, J.; Labatut, P.; Bojanowski, P.; Novotny, D.; Vedaldi, A.; and Rupprecht, C. 2026。《VGGT-Ω》。载于 *IEEE/CVF 计算机视觉与模式识别会议（CVPR）论文集*。

> <span style="color:#3B82F6"><strong>Para. 108:</strong></span> Wang, J.; Karaca, N.; Rupprecht, C.; and Novotny, D. 2024a. Yggsfm: Visual geometry grounded deep structure from motion. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, 21686–21697.

> <span style="color:#F59E0B"><strong>Para. 108[CN]:</strong></span> Wang, J.; Karaca, N.; Rupprecht, C.; and Novotny, D. 2024a。《YggSfM：视觉几何具身的深度运动恢复结构》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，21686–21697。

> <span style="color:#3B82F6"><strong>Para. 109:</strong></span> Wang, Q.; Zhang, Y.; Holynski, A.; Efros, A. A.; and Kanazawa, A. 2025b. Continuous 3d perception model with persistent state. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, 10510–10522.

> <span style="color:#F59E0B"><strong>Para. 109[CN]:</strong></span> Wang, Q.; Zhang, Y.; Holynski, A.; Efros, A. A.; and Kanazawa, A. 2025b。《具有持久状态的连续三维感知模型》。载于 *计算机视觉与模式识别会议论文集*，10510–10522。

> <span style="color:#3B82F6"><strong>Para. 110:</strong></span> Wang, R.; Xu, S.; Dai, C.; Xiang, J.; Deng, Y.; Tong, X.; and Yang, J. 2025c. Moge: Unlocking accurate monocular geometry estimation for open-domain images with optimal training supervision. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, 5261–5271.

> <span style="color:#F59E0B"><strong>Para. 110[CN]:</strong></span> Wang, R.; Xu, S.; Dai, C.; Xiang, J.; Deng, Y.; Tong, X.; and Yang, J. 2025c。《MoGe：通过最优训练监督实现开放域图像的准确单目几何估计》。载于 *计算机视觉与模式识别会议论文集*，5261–5271。

> <span style="color:#3B82F6"><strong>Para. 111:</strong></span> Wang, S.; Leroy, V.; Cabon, Y.; Chidlovskii, B.; and Revaud, J. 2024b. Dust3r: Geometric 3d vision made easy. In *Proceedings of the IEEE/CVF conference on computer vision and pattern recognition*, 20697–20709.

> <span style="color:#F59E0B"><strong>Para. 111[CN]:</strong></span> Wang, S.; Leroy, V.; Cabon, Y.; Chidlovskii, B.; and Revaud, J. 2024b。《DUSt3R：让几何三维视觉变得简单》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，20697–20709。

> <span style="color:#3B82F6"><strong>Para. 112:</strong></span> Wang, Y.; Zhou, J.; Zhu, H.; Chang, W.; Zhou, Y.; Li, Z.; Chen, J.; Pang, J.; Shen, C.; and He, T. 2025d. $\pi^3$: Permutation-Equivariant Visual Geometry Learning. *arXiv preprint arXiv:2507.13347*.

> <span style="color:#F59E0B"><strong>Para. 112[CN]:</strong></span> Wang, Y.; Zhou, J.; Zhu, H.; Chang, W.; Zhou, Y.; Li, Z.; Chen, J.; Pang, J.; Shen, C.; and He, T. 2025d。《$\pi^3$：置换等变视觉几何学习》。*arXiv 预印本 arXiv:2507.13347*。

> <span style="color:#3B82F6"><strong>Para. 113:</strong></span> Wu, C.; Chen, X.; Wu, Z.; Ma, Y.; Liu, X.; Pan, Z.; Liu, W.; Xie, Z.; Yu, X.; Ruan, C.; and Luo, P. 2025. Janus: Decoupling Visual Encoding for Unified Multimodal Understanding and Generation. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*.

> <span style="color:#F59E0B"><strong>Para. 113[CN]:</strong></span> Wu, C.; Chen, X.; Wu, Z.; Ma, Y.; Liu, X.; Pan, Z.; Liu, W.; Xie, Z.; Yu, X.; Ruan, C.; and Luo, P. 2025。《Janus：为统一多模态理解与生成解耦视觉编码》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*。

> <span style="color:#3B82F6"><strong>Para. 114:</strong></span> Wu, D.; Liu, F.; Hung, Y.-H.; and Duan, Y. 2026. Spatial-mllm: Boosting mllm capabilities in visual-based spatial intelligence. *Advances in neural information processing systems*, 38: 13569–13597.

> <span style="color:#F59E0B"><strong>Para. 114[CN]:</strong></span> Wu, D.; Liu, F.; Hung, Y.-H.; and Duan, Y. 2026。《Spatial-MLLM：提升大型多模态模型的视觉空间智能能力》。*神经信息处理系统进展*，38：13569–13597。

> <span style="color:#3B82F6"><strong>Para. 115:</strong></span> Xie, J.; Mao, W.; Bai, Z.; Zhang, D. J.; Wang, W.; Lin, K. Q.; Gu, Y.; Chen, Z.; Yang, Z.; and Shou, M. Z. 2025. Show-o: One Single Transformer to Unify Multimodal Understanding and Generation. In *International Conference on Learning Representations*.

> <span style="color:#F59E0B"><strong>Para. 115[CN]:</strong></span> Xie, J.; Mao, W.; Bai, Z.; Zhang, D. J.; Wang, W.; Lin, K. Q.; Gu, Y.; Chen, Z.; Yang, Z.; and Shou, M. Z. 2025。《Show-o：使用单一 Transformer 统一多模态理解与生成》。载于 *国际学习表征会议*。

> <span style="color:#3B82F6"><strong>Para. 116:</strong></span> Xu, H.; Zhang, J.; Cai, J.; Rezatofighi, H.; and Tao, D. 2022. GMFlow: Learning Optical Flow via Global Matching. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, 8121–8130.

> <span style="color:#F59E0B"><strong>Para. 116[CN]:</strong></span> Xu, H.; Zhang, J.; Cai, J.; Rezatofighi, H.; and Tao, D. 2022。《GMFlow：通过全局匹配学习光流》。载于 *IEEE/CVF 计算机视觉与模式识别会议论文集*，8121–8130。

> <span style="color:#3B82F6"><strong>Para. 117:</strong></span> Xu, Y.; Zhang, J.; Huang, Z.; Chen, Y.; Zhou, Y.; Chen, Z.; Yuan, Y.-J.; Xia, P.; Huang, G.; Cai, X.; et al. 2025. Unigg: Unified 3d understanding and generation via geometric-semantic encoding. *arXiv preprint arXiv:2508.11952*.

> <span style="color:#F59E0B"><strong>Para. 117[CN]:</strong></span> Xu, Y.; Zhang, J.; Huang, Z.; Chen, Y.; Zhou, Y.; Chen, Z.; Yuan, Y.-J.; Xia, P.; Huang, G.; Cai, X.; et al. 2025。《UniGG：通过几何—语义编码统一三维理解与生成》。*arXiv 预印本 arXiv:2508.11952*。

> <span style="color:#3B82F6"><strong>Para. 118:</strong></span> Yang, J.; Sax, A.; Liang, K. J.; Henaff, M.; Tang, H.; Cao, A.; Chai, J.; Meier, F.; and Feiszli, M. 2025. Fast3R: Towards 3D Reconstruction of 1000+ Images in One Forward Pass. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.

> <span style="color:#F59E0B"><strong>Para. 118[CN]:</strong></span> Yang, J.; Sax, A.; Liang, K. J.; Henaff, M.; Tang, H.; Cao, A.; Chai, J.; Meier, F.; and Feiszli, M. 2025。《Fast3R：迈向单次前向传播重建 1000 多幅图像的三维场景》。载于 *IEEE/CVF 计算机视觉与模式识别会议（CVPR）论文集*。

> <span style="color:#3B82F6"><strong>Para. 119:</strong></span> Yin, B.; Wang, Q.; Zhang, P.; Zhang, J.; Wang, K.; Wang, Z.; Zhang, J.; Chandrasegaran, K.; Liu, H.; Krishna, R.; et al. 2025. Spatial mental modeling from limited views. In *Structural Priors for Vision Workshop at ICCV’25*.

> <span style="color:#F59E0B"><strong>Para. 119[CN]:</strong></span> Yin, B.; Wang, Q.; Zhang, P.; Zhang, J.; Wang, K.; Wang, Z.; Zhang, J.; Chandrasegaran, K.; Liu, H.; Krishna, R.; et al. 2025。《从有限视图进行空间心理建模》。载于 *ICCV’25 视觉结构先验研讨会*。

> <span style="color:#3B82F6"><strong>Para. 120:</strong></span> Zhang, J.; Chen, Y.; Zhou, Y.; Xu, Y.; Huang, Z.; Mei, J.; Chen, J.; Yuan, Y.-J.; Cai, X.; Huang, G.; Quan, X.; Xu, H.; and Zhang, L. 2025a. From Flatland to Space: Teaching Vision-Language Models to Perceive and Reason in 3D. In *Advances in Neural Information Processing Systems*, volume 38.

> <span style="color:#F59E0B"><strong>Para. 120[CN]:</strong></span> Zhang, J.; Chen, Y.; Zhou, Y.; Xu, Y.; Huang, Z.; Mei, J.; Chen, J.; Yuan, Y.-J.; Cai, X.; Huang, G.; Quan, X.; Xu, H.; and Zhang, L. 2025a。《从平面世界到空间：教视觉语言模型在三维环境中感知与推理》。载于 *神经信息处理系统进展*，第38卷。

> <span style="color:#3B82F6"><strong>Para. 121:</strong></span> Zhang, S.; Wang, J.; Xu, Y.; Xue, N.; Rupprecht, C.; Zhou, X.; Shen, Y.; and Wetzstein, G. 2025b. Flare: Feed-forward geometry, appearance and camera estimation from uncalibrated sparse views. In *Proceedings of the Computer Vision and Pattern Recognition Conference*, 21936–21947.

> <span style="color:#F59E0B"><strong>Para. 121[CN]:</strong></span> Zhang, S.; Wang, J.; Xu, Y.; Xue, N.; Rupprecht, C.; Zhou, X.; Shen, Y.; and Wetzstein, G. 2025b。《FLARE：从无标定稀疏视图进行前馈式几何、外观和相机估计》。载于 *计算机视觉与模式识别会议论文集*，21936–21947。

> <span style="color:#3B82F6"><strong>Para. 122:</strong></span> Zhang, Y.; Keetha, N. V.; Lyu, C.; Jhamb, B.; Chen, Y.; Qiu, Y.; Karhade, J.; Jha, S.; Hu, Y.; Ramana, D.; et al. 2025c. UFM: A Simple Path towards Unified Dense Correspondence with Flow. In *The Thirty-ninth Annual Conference on Neural Information Processing Systems*.

> <span style="color:#F59E0B"><strong>Para. 122[CN]:</strong></span> Zhang, Y.; Keetha, N. V.; Lyu, C.; Jhamb, B.; Chen, Y.; Qiu, Y.; Karhade, J.; Jha, S.; Hu, Y.; Ramana, D.; et al. 2025c。《UFM：利用光流迈向统一稠密对应关系的简单路径》。载于 *第三十九届神经信息处理系统年会*。

> <span style="color:#3B82F6"><strong>Para. 123:</strong></span> Zhang, Y.; Wu, J.; Li, W.; Li, B.; Ma, Z.; Liu, Z.; and Li, C. 2024. Video Instruction Tuning With Synthetic Data. *arXiv:2410.02713*.

> <span style="color:#F59E0B"><strong>Para. 123[CN]:</strong></span> Zhang, Y.; Wu, J.; Li, W.; Li, B.; Ma, Z.; Liu, Z.; and Li, C. 2024。《使用合成数据进行视频指令微调》。*arXiv:2410.02713*。


## Figure and table captions

**Caption:** Figure 1. SPARGen unifies spatial perception and reasoning through native multimodal generation.

**Caption[CN]:** 图 1。SPARGen 通过原生多模态生成统一空间感知与推理。

**Caption:** Figure 2. Overview of SPARGen. Given a sequence of RGB images and a language instruction, SPARGen represents spatial outputs as sequences or image-aligned fields. These two output formats are generated through the native autoregressive and rectified-flow pathways of a shared MoT backbone. The dashed box denotes the training-only encoding of target fields.

**Caption[CN]:** 图 2。SPARGen 总览。给定 RGB 图像序列和语言指令，SPARGen 将空间输出表示为序列或图像对齐场；两种输出格式分别由共享 MoT 主干的原生自回归路径和矫正流路径生成，虚线框表示仅用于训练的目标场编码。

**Caption:** Figure 3. Qualitative results of SPARGen on point map reconstruction, optical flow estimation, and depth estimation. For optical flow, predictions and error maps are shown before and after refinement.

**Caption[CN]:** 图 3。SPARGen 在点图重建、光流估计和深度估计上的定性结果；光流展示 refinement 前后的预测结果和误差图。

**Caption:** Table 1. Comparison across depth estimation, point map estimation, and camera pose estimation benchmarks. Bold indicates the best performance within each model group.

**Caption[CN]:** 表 1。深度估计、点图估计和相机位姿估计基准的比较；粗体表示各模型组中的最佳性能。

**Caption:** Table 2. Results on spatial-reasoning benchmarks. Bold and underlined values indicate the best and second-best results among non-proprietary models.

**Caption[CN]:** 表 2。空间推理基准上的结果；粗体和下划线数值分别表示非专有模型中的最佳和次佳结果。

**Caption:** Table 3. Zero-shot optical flow results on KITTI. Bold values indicate the best performance.

**Caption[CN]:** 表 3。KITTI 上的零样本光流结果；粗体数值表示最佳性能。

**Caption:** Table 4. Ablation of geometry, optical flow, and spatial-reasoning supervision. Bold values indicate the best performance.

**Caption[CN]:** 表 4。几何、光流和空间推理监督的消融；粗体数值表示最佳性能。
