# MLLM-4D: Towards Visual-based Spatial-Temporal Intelligence

> **Source identity:** Yin et al., *MLLM-4D: Towards Visual-based Spatial-Temporal Intelligence*, arXiv:2603.00515v1 [cs.CV], 28 February 2026; preprint dated 3 March 2026. The supplied PDF has 21 pages (PDF pages 1–21; printed pages 1–21).
>
> **阅读说明：** 本文件按原文顺序保留英文，并在每个实质性段落后紧接中文翻译。模型、数据集、指标、变量、代码标记、JSON 键和输出标签保留英文原文；参考文献按可检索的原始书目保留。

## Contents / 内容索引

1. Abstract / 摘要 — PDF p. 1
2. Introduction / 引言 — PDF pp. 1–2
3. Related Works / 相关工作 — PDF pp. 2–3
4. Scalable Spatial-Temporal Data Curation / 可扩展的时空数据整理 — PDF pp. 3–5
5. MLLM-4D Framework / MLLM-4D 框架 — PDF pp. 5–7
6. Experiments / 实验 — PDF pp. 7–8
7. Conclusion / 结论 — PDF p. 8
8. Impact Statement / 影响声明 — PDF p. 9
9. References / 参考文献 — PDF pp. 9–11
10. Appendix / 附录 — PDF pp. 12–21

## Terminology ledger / 术语表

| English | 中文 | Usage |
|---|---|---|
| spatial-temporal / spatiotemporal | 空间-时间的 / 时空的 | Keep the distinction in compound names where useful. |
| visual-based 4D spatial-temporal intelligence | 基于视觉的 4D 时空智能 | 4D means 3D space + time. |
| Supervised Fine-Tuning (SFT) | 监督微调 | Keep SFT. |
| Reinforcement Fine-Tuning (RFT) | 强化微调 | Keep RFT. |
| Spatiotemporal Chain of Thought (ST-CoT) | 时空思维链 | Keep ST-CoT. |
| Spatiotemporal reward (ST-reward) | 时空奖励 | Keep ST-reward. |
| Group Relative Policy Optimization (GRPO) | 群组相对策略优化 | Keep GRPO. |
| camera ego-motion | 相机自运动 | Camera displacement/orientation. |
| Object-Camera Dynamics | 物体-相机动态 | One MLLM4D task category. |
| Mean Euclidean Error (MEE) | 平均欧氏误差 | Keep MEE. |

# Abstract / 摘要

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Humans are born with vision-based 4D spatial-temporal intelligence, which enables us to perceive and reason about the evolution of 3D space over time from purely visual inputs. Despite its importance, this capability remains a significant bottleneck for current multimodal large language models (MLLMs). To tackle this challenge, we introduce <em>MLLM-4D</em>, a comprehensive framework designed to bridge the gaps in training data curation and model post-training for spatiotemporal understanding and reasoning. On the data front, we develop a cost-efficient data curation pipeline that repurposes existing stereo video datasets into high-quality 4D spatiotemporal instructional data. This results in the <em>MLLM4D-2M</em> and <em>MLLM4D-R1-30k</em> datasets for Supervised Fine-Tuning (SFT) and Reinforcement Fine-Tuning (RFT), alongside <em>MLLM4D-Bench</em> for comprehensive evaluation. Regarding model training, our post-training strategy establishes a foundational 4D understanding via SFT and further catalyzes 4D reasoning capabilities by employing Group Relative Policy Optimization (GRPO) with specialized <em>Spatiotemporal Chain of Thought (ST-CoT)</em> prompting and <em>Spatiotemporal reward (ST-reward)</em> functions without involving the modification of architecture. Extensive experiments demonstrate that MLLM-4D achieves state-of-the-art spatial-temporal understanding and reasoning capabilities from purely 2D RGB inputs. Project page: https://github.com/GVCLab/MLLM-4D.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 人类天生具备基于视觉的 4D 空间-时间智能，使我们能够仅凭视觉输入感知并推理三维空间随时间的演化。尽管这一能力十分重要，但它仍是当前多模态大语言模型（MLLM）的重要瓶颈。为应对这一挑战，我们提出 <em>MLLM-4D</em>，一个旨在弥合时空理解与推理中训练数据整理和模型后训练两方面差距的综合框架。在数据方面，我们开发了一条高效的数据整理流水线，将现有立体视频数据集重新用于生成高质量的 4D 时空指令数据，由此得到用于监督微调（SFT）和强化微调（RFT）的 <em>MLLM4D-2M</em> 与 <em>MLLM4D-R1-30k</em> 数据集，以及用于综合评估的 <em>MLLM4D-Bench</em>。在模型训练方面，我们的后训练策略通过 SFT 建立基础的 4D 理解能力，并通过带有专门的 <em>Spatiotemporal Chain of Thought (ST-CoT)</em> 提示和 <em>Spatiotemporal reward (ST-reward)</em> 函数的群组相对策略优化（GRPO），进一步激发 4D 推理能力，且无需修改模型架构。大量实验表明，仅使用纯 2D RGB 输入，MLLM-4D 就能达到最先进的时空理解与推理能力。项目主页：https://github.com/GVCLab/MLLM-4D。

**Authors / 作者:** Xingyilang Yin, Chengzhengxu Li, Jiahao Chang, Chi-Man Pun, Xiaodong Cun. * indicates equal contribution; affiliations: 1 University of Macau, 2 GVC Lab, Great Bay University, 3 Xi’an Jiaotong University, 4 The Chinese University of Hong Kong, Shenzhen. Correspondence: Chi-Man Pun <cmpun@um.edu.mo>, Xiaodong Cun <cun@gbu.edu.cn>.

# 1. Introduction / 引言

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Humans possess an innate 4D spatiotemporal intelligence that extends beyond the perception of static 3D geometry to integrate time as an intrinsic cognitive dimension. This ability to reason about the world in 4D (3D space + time) allows us to navigate and act effectively within constantly changing environments using purely visual inputs. Such ability is critical to interactive AI systems, including robotics, VR, and embodied agents, where navigating dynamic scenes requires a continuous understanding of evolving spatial relationships. While Multimodal Large Language Models (MLLMs) have demonstrated remarkable general intelligence (Hurst et al., 2024; Comanici et al., 2025) in image (Liu et al., 2023; Li et al., 2024), video (Bai et al., 2025b;a), and audio (Chu et al., 2024; Xu et al., 2025a), their abilities for this spatiotemporal understanding and reasoning remain largely underexplored.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 人类天生具有 4D 时空智能，它超越了对静态三维几何的感知，将时间作为内在的认知维度纳入其中。这种在 4D（3D 空间加时间）中推理世界的能力，使我们能够仅凭视觉输入在不断变化的环境中有效导航并采取行动。这种能力对于机器人、VR 和具身智能体等交互式 AI 系统至关重要，因为动态场景中的导航要求系统持续理解不断演化的空间关系。尽管多模态大语言模型（MLLM）已经在图像（Liu et al., 2023; Li et al., 2024）、视频（Bai et al., 2025b;a）和音频（Chu et al., 2024; Xu et al., 2025a）上展现出显著的通用智能（Hurst et al., 2024; Comanici et al., 2025），但它们在这种时空理解与推理方面的能力仍未得到充分探索。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Recent works mainly focus on spatial reasoning within static scenes (Yang et al., 2025a; Dihan et al., 2025; Yang et al., 2025b; Azuma et al., 2022; Ma et al., 2022; Zhang et al., 2025) and struggle to understand and reason about evolving relationships within 4D space, as illustrated in Fig. 1. For dynamic scenarios, manual annotations can only collect small benchmark-size datasets (Zhou et al., 2025b; Li et al., 2025) and are challenging to scale for current MLLM training. On the other hand, current methods enhance 3D spatial intelligence of MLLMs using additional spatial encoders (Zheng et al., 2025; Fan et al., 2025; Huang et al., 2024; Deng et al., 2025; Zhu et al., 2025; Liu et al., 2025). However, these 3D expertise MLLMs often fail in dynamic reasoning tasks, as their learned knowledge is constrained to static environments with immobile objects.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 近期工作主要聚焦于静态场景中的空间推理（Yang et al., 2025a; Dihan et al., 2025; Yang et al., 2025b; Azuma et al., 2022; Ma et al., 2022; Zhang et al., 2025），难以理解和推理 4D 空间中不断演化的关系，如图 1 所示。对于动态场景，人工标注只能构建规模较小的基准级数据集（Zhou et al., 2025b; Li et al., 2025），难以扩展到当前 MLLM 的训练中。另一方面，现有方法通过增加空间编码器来增强 MLLM 的三维空间智能（Zheng et al., 2025; Fan et al., 2025; Huang et al., 2024; Deng et al., 2025; Zhu et al., 2025; Liu et al., 2025）。然而，这些具有 3D 专长的 MLLM 往往无法完成动态推理任务，因为它们学到的知识受限于物体静止不动的静态环境。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> We thus introduce MLLM-4D, a novel and comprehensive framework for boosting MLLM capabilities for visual-based spatiotemporal intelligence by addressing two critical bottlenecks introduced above: (i) the scarcity of large-scale and high-quality 4D instructional data. We develop an automated data engine that repurposes existing stereo video datasets (Shao et al., 2024) into high-quality 4D spatiotemporal instructional data. Our pipeline integrates several advanced vision primitives to decompose these scenes into per-frame camera poses, object-level 3D points and corresponding semantic descriptions, capturing the rich 4D evolution of the entire scene. By applying rigorous physics-based spatiotemporal computations to this metadata, we generate a large-scale MLLM4D-2M dataset for Supervised Fine-Tuning (SFT), MLLM4D-R1-30k dataset for Reinforcement Fine-Tuning (RFT), and MLLM4D-Bench for comprehensive evaluation, respectively. (ii) the lack of specialized and scalable 4D-aware MLLMs. Contrary to prior works that rely on auxiliary spatial encoders, we demonstrate that standard MLLM architectures can achieve robust spatiotemporal reasoning when scaled with high-quality 4D data. Our framework utilizes a hierarchical post-training approach to associate pixel-level video observations with 4D physical reasoning. In the first stage, SFT establishes a foundational 4D understanding, ensuring the model can correctly identify spatial-temporal anchors. In the second stage, we catalyze advanced 4D reasoning capabilities through Group Relative Policy Optimization (GRPO) (Liu et al., 2024a).

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 因此，我们提出 MLLM-4D，这是一个通过解决上述两个关键瓶颈来提升 MLLM 基于视觉的时空智能能力的新型综合框架：(i) 大规模、高质量 4D 指令数据的稀缺。我们开发了一个自动化数据引擎，将现有立体视频数据集（Shao et al., 2024）重新用于高质量 4D 时空指令数据。该流水线结合多种先进视觉原语，将场景分解为逐帧相机位姿、物体级 3D 点及相应语义描述，从而捕获整个场景丰富的 4D 演化。我们对这些元数据应用严格的基于物理的时空计算，分别生成用于监督微调（SFT）的 MLLM4D-2M、用于强化微调（RFT）的 MLLM4D-R1-30k，以及用于综合评估的 MLLM4D-Bench。(ii) 缺乏专门且可扩展的 4D 感知 MLLM。不同于依赖辅助空间编码器的既有工作，我们证明，在高质量 4D 数据的支持下，标准 MLLM 架构经过规模化训练即可实现稳健的时空推理。我们的框架采用分层后训练方法，将像素级视频观测与 4D 物理推理关联起来。第一阶段通过 SFT 建立基础 4D 理解，确保模型能够正确识别时空锚点；第二阶段通过群组相对策略优化（GRPO）（Liu et al., 2024a）催化高级 4D 推理能力。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> We introduce a specialized five-step Spatiotemporal Chain of Thought (ST-CoT) prompting that forces the model to act as a visual physics engine, focusing on temporal anchoring, 3D state parsing, and physical motion. We move beyond standard accuracy reward and format reward by introducing Spatiotemporal reward (ST-reward) functions. This reward serves as a physical regularizer, penalizing the model for hallucinated motion that contradicts the actual spatiotemporal evolution of the scene. Extensive experiments demonstrate that MLLM-4D achieves state-of-the-art 4D spatiotemporal understanding and reasoning performance.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 我们提出专门的五步时空思维链（ST-CoT）提示，迫使模型充当视觉物理引擎，重点关注时间锚定、3D 状态解析和物理运动。我们通过引入时空奖励（ST-reward）函数，超越标准的准确率奖励和格式奖励。该奖励充当物理正则项，对与场景实际时空演化相矛盾的幻觉运动进行惩罚。大量实验表明，MLLM-4D 达到了最先进的 4D 时空理解与推理性能。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Our main contributions are summarized as follows:
>
> - We introduce MLLM-4D, a novel and comprehensive framework that significantly enhances the spatial-temporal intelligence of MLLMs, demonstrating strong 4D understanding and reasoning capabilities without requiring architectural modifications.
> - We develop an automated data curation pipeline to generate high-quality 4D spatiotemporal instructional data by repurposing the existing stereoscopic video datasets. Leveraging this pipeline, we propose the MLLM4D-2M and MLLM4D-R1-30k datasets for SFT and RFT, alongside MLLM4D-Bench for comprehensive evaluation.
> - In our training framework, we propose specialized ST-CoT prompting strategies and physics-grounded ST-reward. These are integrated into GRPO to systematically improve the model’s capacity for verifiable 4D spatiotemporal reasoning in dynamic scenes.
> - Extensive experiments demonstrate that our MLLM-4D achieves state-of-the-art 4D understanding and reasoning performance with only RGB video input.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 我们的主要贡献总结如下：
>
> - 我们提出 MLLM-4D，这是一个新型综合框架，显著增强了 MLLM 的时空智能；它无需修改架构即可展现强大的 4D 理解和推理能力。
> - 我们开发了自动化数据整理流水线，通过重新利用现有立体视频数据集生成高质量 4D 时空指令数据。借助该流水线，我们提出用于 SFT 和 RFT 的 MLLM4D-2M 与 MLLM4D-R1-30k 数据集，以及用于综合评估的 MLLM4D-Bench。
> - 在训练框架中，我们提出专门的 ST-CoT 提示策略和物理约束的 ST-reward，并将其集成到 GRPO 中，系统性提升模型在动态场景中进行可验证 4D 时空推理的能力。
> - 大量实验表明，仅使用 RGB 视频输入，我们的 MLLM-4D 就达到了最先进的 4D 理解与推理性能。

## Figure 1 / 图 1

**Caption:** We propose MLLM-4D, a method that advances MLLMs for the visual-based spatial-temporal intelligence. MLLM-4D is capable of understanding and reasoning about the evolution of 3D space over time from only 2D video input.

**Caption[CN]:** 我们提出 MLLM-4D，一种推进 MLLM 基于视觉的时空智能能力的方法。MLLM-4D 能够仅从 2D 视频输入理解并推理三维空间随时间的演化。

> **Source anchor:** PDF p. 1. The figure includes the example question “What is the approximate distance (in meters) between the camera location in frame 3 and the nearest point of the man on the skateboard with black grip tape in frame 6?” with options A. 0.8 meters, B. 2.4 meters, C. 1.4 meters, D. 1.9 meters, and an ST-CoT example whose answer is B.

# 2. Related Works / 相关工作

### Multimodal Large Language Models / 多模态大语言模型

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Multimodal Large Language Models (MLLMs) (Liu et al., 2023; Li et al., 2023; Zhang et al., 2024; Hurst et al., 2024; Tong et al., 2024; Wang et al., 2025e; Zhou et al., 2025a; Comanici et al., 2025) have achieved remarkable success across diverse 2D visual tasks. Recent advancements, such as Qwen3-VL (Bai et al., 2025a) achieve strong visual modeling across images and video by integrating interleaved-MRoPE, multi-level visual features, and text-based time alignment. Despite these strides, even the state-of-the-art MLLMs struggle to interpret the complex underlying 4D scene from video. Our proposed MLLM-4D is designed to bridge this gap, achieving visual-based spatiotemporal intelligence inspired by human innate cognition. Much like the innate ability of human brain to perceive 2D visual signals yet reason about 3D physical relationships over time, MLLM-4D enables deeper structural understanding of the dynamic world.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 多模态大语言模型（MLLM）（Liu et al., 2023; Li et al., 2023; Zhang et al., 2024; Hurst et al., 2024; Tong et al., 2024; Wang et al., 2025e; Zhou et al., 2025a; Comanici et al., 2025）已经在各种 2D 视觉任务中取得显著成功。近期进展（如 Qwen3-VL（Bai et al., 2025a））通过整合 interleaved-MRoPE、多层级视觉特征和基于文本的时间对齐，在图像和视频上实现了强大的视觉建模能力。尽管取得了这些进展，即使是最先进的 MLLM 也难以从视频中解释复杂的底层 4D 场景。我们提出的 MLLM-4D 旨在弥合这一差距，实现受人类先天认知启发的基于视觉的时空智能。正如人脑天生能够感知 2D 视觉信号、却能推理随时间变化的 3D 物理关系一样，MLLM-4D 使模型能够更深入地结构化理解动态世界。

### MLLMs for Spatial Intelligence / 面向空间智能的 MLLM

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Recent advances (Ma et al., 2025; Shen et al., 2025; Xu et al., 2025b; Ouyang et al., 2025; Yang et al., 2026) have sparked interest in extending MLLMs to encompass 3D spatial understanding and reasoning. While some methods rely on auxiliary 3D geometric input (Huang et al., 2024; Deng et al., 2025) or 2.5D depth information (Zhu et al., 2025; Liu et al., 2025), recent studies including VG-LLM (Zheng et al., 2025), SpatialMLLM (Wu et al., 2025), and VLM-3R (Fan et al., 2025) attempt to perceive the 3D world directly from video by leveraging 3D reconstruction priors (Wang et al., 2025a;b). However, these 3D expertise MLLMs remain largely constrained to static scenes with immobile objects and struggle to learn the evolving relationships within a 4D spatiotemporal manifold. In contrast, our MLLM-4D establishes a foundational 4D understanding and reasoning capabilities with our dataset and designed training recipes.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 近期进展（Ma et al., 2025; Shen et al., 2025; Xu et al., 2025b; Ouyang et al., 2025; Yang et al., 2026）引发了将 MLLM 扩展到 3D 空间理解与推理的兴趣。一些方法依赖辅助 3D 几何输入（Huang et al., 2024; Deng et al., 2025）或 2.5D 深度信息（Zhu et al., 2025; Liu et al., 2025），而 VG-LLM（Zheng et al., 2025）、SpatialMLLM（Wu et al., 2025）和 VLM-3R（Fan et al., 2025）等近期研究则尝试利用 3D 重建先验（Wang et al., 2025a;b）直接从视频感知三维世界。然而，这些 3D 专长 MLLM 仍大多受限于物体静止的静态场景，难以学习 4D 时空流形中的演化关系。相比之下，我们的 MLLM-4D 借助所构建的数据集和设计的训练方案，建立了基础的 4D 理解与推理能力。

### Visual-based 4D Spatial-Temporal Intelligence / 基于视觉的 4D 时空智能

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Visual-based spatial-temporal intelligence focuses on enabling video MLLMs to understand and reason about 4D spatiotemporal relationships directly from visual input. Previous works mainly focus on improving the spatial intelligence of MLLMs through 3D QA datasets (Azuma et al., 2022; Ma et al., 2022; Zhang et al., 2025) on static 3D spatial reasoning benchmarks (Yang et al., 2025a; Dihan et al., 2025; Yang et al., 2025b; Jia et al., 2025). More recently, efforts (Zhou et al., 2025b; Li et al., 2025) such as VLM4D (Zhou et al., 2025b) have begun to evaluate the spatiotemporal reasoning capabilities of MLLMs. However, these benchmarks are limited to a few thousand QA pairs and rely on manual annotation, which lacks the scalability required for MLLM fine-tuning. To address the data constraints, we propose an automated data curation pipeline to generate large-scale training and evaluation datasets, establishing a high-quality foundation for 4D spatiotemporal intelligence learning.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 基于视觉的时空智能关注使视频 MLLM 能够直接从视觉输入理解和推理 4D 时空关系。以往工作主要通过 3D QA 数据集（Azuma et al., 2022; Ma et al., 2022; Zhang et al., 2025），在静态 3D 空间推理基准（Yang et al., 2025a; Dihan et al., 2025; Yang et al., 2025b; Jia et al., 2025）上提升 MLLM 的空间智能。近期，VLM4D（Zhou et al., 2025b）等工作（Zhou et al., 2025b; Li et al., 2025）开始评估 MLLM 的时空推理能力。然而，这些基准仅包含数千个 QA 对并依赖人工标注，缺乏 MLLM 微调所需的可扩展性。为解决数据约束，我们提出自动化数据整理流水线以生成大规模训练和评估数据集，为 4D 时空智能学习建立高质量基础。

# 3. Scalable Spatial-Temporal Data Curation / 可扩展的时空数据整理

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We utilize the question-answer (QA) pair as the fundamental training type to enhance the spatial-temporal understanding and reasoning of MLLM. However, current 4D instructional datasets (Zhou et al., 2025b; Li et al., 2025) are typically limited to benchmark-scale samples (e.g., about 2k in VLM4D), as they rely on manual annotations with unstructured types, which are not scalable for training MLLMs.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们将问答（QA）对作为增强 MLLM 时空理解与推理的基本训练类型。然而，当前 4D 指令数据集（Zhou et al., 2025b; Li et al., 2025）通常仅限于基准规模的样本（例如 VLM4D 约 2k），因为它们依赖类型不结构化的人工标注，无法扩展到 MLLM 训练。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Thus, we first define the included scope of the spatial-temporal intelligence from the decoupling aspect of camera and object movement. As shown in Fig. 2, which includes three distinct categories:
>
> (i) **Independent Object Motion** has one type of question, which aims to ask about the objects’ absolute distance changes over time (frames).
>
> (ii) **Camera Ego-Motion** assesses the camera’s displacement and orientation changes through two metrics: camera absolute distance, which measures the physical span of the camera’s movement among frames, and camera relative direction, which tracks the angular trajectory of the camera over temporal dimension (frames).
>
> (iii) **Object-Camera Dynamics.** This category characterizes the intricate spatial interplay between the camera and moving objects. It encompasses three core dimensions: the absolute distance between the two, their relative distance change, and their relative angular orientation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 因此，我们首先从相机运动和物体运动解耦的角度定义时空智能的覆盖范围。如图 2 所示，它包括三个不同类别：
>
> (i) **Independent Object Motion（独立物体运动）**包含一种问题类型，询问物体随时间（帧）变化的绝对距离。
>
> (ii) **Camera Ego-Motion（相机自运动）**通过两个指标评估相机的位移和方向变化：相机绝对距离衡量相机在帧之间移动的物理跨度；相机相对方向跟踪相机在时间维度（帧）上的角度轨迹。
>
> (iii) **Object-Camera Dynamics（物体-相机动态）**刻画相机与运动物体之间复杂的空间交互，包括两者之间的绝对距离、相对距离变化和相对角方向三个核心维度。

## Figure 2 / 图 2

**Caption:** The components of our MLLM4D-Bench.

**Caption[CN]:** 我们的 MLLM4D-Bench 的组成部分。

| Category | Subtask | Share shown |
|---|---|---:|
| Independent Object Motion | Object absolute distance | 16.7% |
| Camera Ego-Motion | Camera absolute distance; Camera relative direction | 33.4%; 16.7% + 16.7% |
| Object-Camera Dynamics | Object-Camera absolute distance; Object-Camera relative distance; Object-Camera relative direction | 50.0%; 16.7% + 16.7% + 16.7% |

> **Source anchor:** PDF p. 3; six subtasks and the percentages above are transcribed from the figure.

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> To automatically obtain the scalable and accurate question-answer pairs, we predict the spatial-temporal metadata from the video and obtain the answer via physical laws. This metadata contains the per-frame camera poses, object-level 3D point clouds, and fine-grained semantic descriptions, which constitutes a comprehensive 4D representation of dynamic scenes. However, directly processing monocular videos through 4D tracking models (Xiao et al., 2025; Badki et al., 2025) often suffers from depth ambiguity and accuracy issues. Instead, we introduce an automated pipeline that extracts precise 4D spatiotemporal information from existing stereoscopic video datasets (Jin et al., 2025). After obtaining the metadata, we utilize the physical-based formulations to solve for exact spatiotemporal relationships and obtain the thinking process via the MLLM-based CoT generation pipeline, alongside the MLLM4D-Bench for evaluation. Below, we give the details of each part.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 为了自动获得可扩展且准确的问答对，我们从视频中预测时空元数据，并通过物理定律获得答案。这些元数据包含逐帧相机位姿、物体级 3D 点云和细粒度语义描述，构成动态场景的完整 4D 表示。然而，直接通过 4D 跟踪模型（Xiao et al., 2025; Badki et al., 2025）处理单目视频，往往会受到深度歧义和精度问题的影响。为此，我们提出一条自动化流水线，从现有立体视频数据集（Jin et al., 2025）中提取精确的 4D 时空信息。获得元数据后，我们利用基于物理的公式求解精确的时空关系，并通过基于 MLLM 的 CoT 生成流水线获得思维过程，同时构建 MLLM4D-Bench 进行评估。下面详述各部分。

### 4D Spatial-Temporal Metadata from Stereo Videos / 来自立体视频的 4D 时空元数据

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> As illustrated in Fig. 3, giving the stereoscopic video from Stereo4D (Jin et al., 2025), we obtain the K left-rectified video frames $\{I_i\}_{i=1}^{K}$; processed camera pose (Schonberger & Frahm, 2016) $\{C_i\}_{i=1}^{K}$, where $C_i=[R_i|t_i]$ consists of a $3\times3$ rotation matrix $R_i$ and a $3\times1$ translation vector $t_i$; per-frame metric 3D points (Doersch et al., 2024) $\{P_i\}_{i=1}^{K}$ from metric stereo depth (Wang et al., 2024) to obtain the stereo metadata. This is followed by a robust filtering stage to filter out the low-quality estimations.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 如图 3 所示，给定来自 Stereo4D（Jin et al., 2025）的立体视频，我们获得 $K$ 个左校正视频帧 $\{I_i\}_{i=1}^{K}$；获得处理后的相机位姿（Schonberger & Frahm, 2016）$\{C_i\}_{i=1}^{K}$，其中 $C_i=[R_i|t_i]$ 由 $3\times3$ 旋转矩阵 $R_i$ 和 $3\times1$ 平移向量 $t_i$ 组成；并从度量立体深度（Wang et al., 2024）中获得逐帧度量 3D 点（Doersch et al., 2024）$\{P_i\}_{i=1}^{K}$，以构成立体元数据。随后执行稳健过滤阶段，滤除低质量估计。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> After that, to obtain the instance-level semantic annotation from a question-answer pair, we employ a video MLLM, i.e. Gemini-2.5-flash (Comanici et al., 2025), to identify all moving entities and extract their corresponding noun categories (see Appendix 8.2 for details). We then utilize GroundedSAM2 (Ren et al., 2024; Ravi et al., 2025; Liu et al., 2024b) for instance segmentation and tracking, yielding temporally consistent 2D masks across the sequence. Finally, the scene-level 4D points $\{P_i\}_{i=1}^{K}$ are projected onto these 2D masks $\{mask_{im}\}_{i=1,...,K;m=1,...,M}$ to isolate per-frame, object-level 4D points for $M$ distinct objects, denoted as $\{P_{im}\}_{i=1,...,K;m=1,...,M}$. To enrich these representations, the video frames and their associated 2D masks are fed into a region-level MLLM, PixelRefer (Yuan et al., 2025), to generate fine-grained semantic descriptions $\{T_m\}_{m=1}^{M}$ for each object. The camera pose, fine-grained description, and the instance-level 3D points build the general form of the metadata for further spatial-temporal relationship solver via physical laws.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 随后，为了从问答对中获得实例级语义标注，我们使用视频 MLLM Gemini-2.5-flash（Comanici et al., 2025）识别所有运动实体并提取其对应名词类别（详见附录 8.2）。接着使用 GroundedSAM2（Ren et al., 2024; Ravi et al., 2025; Liu et al., 2024b）进行实例分割和跟踪，得到序列中时间一致的 2D 掩码。最后，将场景级 4D 点 $\{P_i\}_{i=1}^{K}$ 投影到这些 2D 掩码 $\{mask_{im}\}_{i=1,...,K;m=1,...,M}$ 上，从而分离出 $M$ 个不同物体的逐帧、物体级 4D 点，记为 $\{P_{im}\}_{i=1,...,K;m=1,...,M}$。为丰富这些表示，我们将视频帧及其对应的 2D 掩码输入区域级 MLLM PixelRefer（Yuan et al., 2025），为每个物体生成细粒度语义描述 $\{T_m\}_{m=1}^{M}$。相机位姿、细粒度描述和实例级 3D 点共同构成元数据的一般形式，供后续通过物理定律求解时空关系。

## Figure 3 / 图 3

**Caption:** Our scalable curation pipeline for instructional spatiotemporal data. Our automated pipeline leverages several advanced vision techniques to extract 4D spatiotemporal information from stereoscopic videos, including per-frame camera poses, object-level 3D point clouds, and semantic descriptions. These data are then processed through a physics-based spatiotemporal relation solver to generate 4D QA pairs, and our specialized ST-CoT prompting strategy synthesizes the corresponding reasoning trajectories.

**Caption[CN]:** 我们用于指令时空数据的可扩展整理流水线。该自动化流水线利用多种先进视觉技术从立体视频中提取 4D 时空信息，包括逐帧相机位姿、物体级点云和语义描述。随后，这些数据经过基于物理的时空关系求解器处理以生成 4D QA 对，而专门的 ST-CoT 提示策略则合成相应的推理轨迹。

### Physical-based Spatial-Temporal Relationship Solver / 基于物理的时空关系求解器

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> To generate high-fidelity QA pairs, we derive ground-truth results through rigorous physics-based spatial-temporal computation. For instance, to determine the Camera Relative Direction between any two frames $i$ and $j$: we first compute the world-space displacement $\Delta t=t_j-t_i$. To determine the movement relative to the camera’s perspective at frame $i$, we project this vector into the local camera coordinate system: $d_{cam\_rel\_dir}=R_i^T\cdot\Delta t$. The resulting vector $d_{cam\_rel\_dir}=[d_x,d_y,d_z]$ is interpreted according to standard camera conventions, where $+X,+Y,+Z$ correspond to the right, down, and forward directions, respectively. Please refer to Appendix 8.2 for more details about other spatiotemporal relation solver implementations.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 为生成高保真 QA 对，我们通过严格的基于物理的时空计算推导真值结果。例如，为确定任意两帧 $i$ 和 $j$ 之间的相机相对方向，先计算世界空间位移 $\Delta t=t_j-t_i$。为了确定相对于第 $i$ 帧相机视角的运动，将该向量投影到局部相机坐标系：$d_{cam\_rel\_dir}=R_i^T\cdot\Delta t$。所得向量 $d_{cam\_rel\_dir}=[d_x,d_y,d_z]$ 按标准相机约定解释，其中 $+X,+Y,+Z$ 分别对应右、下和前方向。其他时空关系求解器的实现细节请参阅附录 8.2。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> **MLLM4D-2M Dataset.** After calculating the ground-truth values, we apply templates to formulate the final QA pairs. Please refer to the Appendix 8.2 for more details about templates and data filtering details. After filtering, we retain 2M high-quality QA pairs across approximately 100k videos, forming the large-scale MLLM4D-2M dataset for supervised fine-tuning (SFT).

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> **MLLM4D-2M 数据集。** 计算真值后，我们应用模板构造最终 QA 对。模板和数据过滤的更多细节见附录 8.2。过滤后，我们在约 100k 个视频中保留 2M 个高质量 QA 对，形成用于监督微调（SFT）的大规模 MLLM4D-2M 数据集。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> **MLLM4D-Bench.** We report the composition and evaluation settings of our MLLM4D-Bench in Fig. 2, which comprise 6k questions organized into six specialized subtasks. Our benchmark distinguishes itself from existing evaluation suites in several key dimensions: (1) Dynamic Scene Complexity: Unlike current 3D spatial benchmarks (Yang et al., 2025a;b; Jia et al., 2025) which focus on reasoning within static environments, MLLM4D-Bench evaluates dynamic scenes involving both moving camera perspectives and multiple moving objects; (2) Structured 4D Motion Categorization: Compared to existing 4D benchmarks (Zhou et al., 2025b; Li et al., 2025), we provide a more rigorous decomposition of 4D motion into three logical categories: Independent Object Motion, Camera Ego-Motion, and Object-Camera Dynamics; (3) Fine-Grained Temporal Evaluation: Our benchmark features fine-grained, framewise temporal tagging. This enables the precise evaluation of 4D spatiotemporal reasoning between any two arbitrary frames in a video, which is absent in previous benchmark.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **MLLM4D-Bench。** 我们在图 2 中报告 MLLM4D-Bench 的组成和评估设置，其中包含组织为六个专门子任务的 6k 个问题。该基准在几个关键方面区别于现有评估套件：(1) **动态场景复杂度：** 不同于聚焦静态环境推理的当前 3D 空间基准（Yang et al., 2025a;b; Jia et al., 2025），MLLM4D-Bench 评估同时包含运动相机视角和多个运动物体的动态场景；(2) **结构化 4D 运动分类：** 相比现有 4D 基准（Zhou et al., 2025b; Li et al., 2025），我们将 4D 运动更严格地分解为三个逻辑类别：独立物体运动、相机自运动和物体-相机动态；(3) **细粒度时间评估：** 我们的基准采用细粒度、逐帧时间标记，可以精确评估视频中任意两帧之间的 4D 时空推理，这是以往基准所不具备的。

## Figure 4 / 图 4

**Caption:** Our RFT pipeline. Given the input video and question, the MLLM-4D model generates multiple rollouts using the ST-CoT reasoning format. Within each group, relative advantages are computed based on accuracy reward, format reward and ST-reward. The model parameters are then updated via the GRPO objective, which incorporates a KL penalty relative to the frozen reference model.

**Caption[CN]:** 我们的 RFT 流水线。给定输入视频和问题，MLLM-4D 模型使用 ST-CoT 推理格式生成多条 rollout。在每个组内，根据准确率奖励、格式奖励和 ST-reward 计算相对优势；随后通过 GRPO 目标更新模型参数，该目标相对于冻结的参考模型包含 KL 惩罚。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **4D Reasoning Data Generation.** We synthesize detailed thinking processes to align the model for 4D spatiotemporal reasoning. By prompting Gemini-2.5-Pro with video frames, corresponding QA pairs, 4D physical values, and spatiotemporal CoT guideline, we generate specialized spatiotemporal CoT data (See Sec. 4.2, Fig. 11 and Appendix 8.3 for details). This process yields 7k cold-start samples and the MLLM4D-R1-30k, which contains 30k QA pairs with significant 4D motion and ground-truth solutions designed for large-scale Reinforcement Fine-Tuning.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **4D 推理数据生成。** 我们合成详细的思维过程，以使模型适应 4D 时空推理。通过向 Gemini-2.5-Pro 提供视频帧、对应 QA 对、4D 物理值和时空 CoT 指南，我们生成专门的时空 CoT 数据（详见第 4.2 节、图 11 和附录 8.3）。这一过程产生 7k 个冷启动样本和 MLLM4D-R1-30k；后者包含 30k 个具有显著 4D 运动及真值解答、面向大规模强化微调的 QA 对。

# 4. MLLM-4D Framework / MLLM-4D 框架

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Previous works involve additional spatial encoders (Zheng et al., 2025; Fan et al., 2025; Wu et al., 2025) to boost spatial understanding. Notably, we find that using a pure 2D visual encoder and retaining the standard MLLM architecture already achieves state-of-the-art performance when supported by our scalable, high-quality spatial-temporal datasets and optimized post-training framework. We propose a two-stage post-training framework for both understanding and reasoning. In the first stage, we conduct SFT on our MLLM4D-2M dataset to establish foundational 4D understanding (Sec. 4.1). To further enhance 4D reasoning, we utilize a cold start phase to align the model’s output with our specialized Spatiotemporal Chain of Thought (ST-CoT) (Sec. 4.2). This is followed by the second stage in which we employ Group Relative Policy Optimization (GRPO), leveraging the ST-CoT prompting and our spatiotemporal reward (ST-reward) functions on our MLLM4D-R1-30k dataset (Sec. 4.3).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 以往工作引入额外的空间编码器（Zheng et al., 2025; Fan et al., 2025; Wu et al., 2025）来增强空间理解。值得注意的是，我们发现，在可扩展、高质量时空数据集和优化的后训练框架支持下，使用纯 2D 视觉编码器并保留标准 MLLM 架构，就已经能够达到最先进的性能。我们提出一个同时面向理解与推理的两阶段后训练框架。第一阶段在 MLLM4D-2M 数据集上进行 SFT，以建立基础 4D 理解（第 4.1 节）；为进一步增强 4D 推理，我们使用冷启动阶段使模型输出与专门的时空思维链（ST-CoT）对齐（第 4.2 节）；随后在第二阶段中，在 MLLM4D-R1-30k 数据集上利用 ST-CoT 提示和时空奖励（ST-reward）函数执行群组相对策略优化（GRPO）（第 4.3 节）。

## 4.1. Supervised Fine-Tuning for 4D Understanding / 用于 4D 理解的监督微调

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Leveraging the proposed MLLM4D-2M dataset, we first perform supervised fine-tuning (SFT) to establish foundational 4D spatiotemporal comprehension. To ensure efficient adaptation while preserving the model’s pre-trained multimodal knowledge, we utilize the Low-Rank Adaptation (LoRA) (Hu et al., 2022) technique, where trainable rank-decomposition matrices are injected into the linear layers of Transformers. During this stage, we employ the standard cross-entropy loss $\mathcal{L}_{ce}$ between the model-generated answer sequences and the ground-truth annotations:

$$\mathcal{L}_{ce}=-\sum_j \log P\left(o^{(j)}\mid o^{(1:j-1)},q,\{I_i\}_{i=1}^{N_k}\right). \tag{1}$$

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 借助提出的 MLLM4D-2M 数据集，我们首先执行监督微调（SFT），建立基础的 4D 时空理解。为确保高效适配并保留模型预训练的多模态知识，我们采用低秩适配（LoRA）（Hu et al., 2022）技术，将可训练的秩分解矩阵注入 Transformer 的线性层。在此阶段，我们在模型生成的答案序列与真值标注之间使用标准交叉熵损失 $\mathcal{L}_{ce}$：

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Here $\{I_i\}_{i=1}^{N_k}$ denotes the sequence of $N_k$ input video frames, $q$ represents the concatenated system prompt and scenario-specific question, $o^{(i)}$ denotes the $i$-th token in the target reasoning-answer trajectory, and $o^{(1:i-1)}$ denotes the preceding tokens. This foundational phase ensures the model internalizes the prerequisite spatial-temporal alignment necessary for subsequent high-level reasoning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 这里，$\{I_i\}_{i=1}^{N_k}$ 表示由 $N_k$ 个输入视频帧构成的序列，$q$ 表示拼接后的系统提示和场景特定问题，$o^{(i)}$ 表示目标推理-答案轨迹中的第 $i$ 个 token，而 $o^{(1:i-1)}$ 表示此前的 token。该基础阶段确保模型内化后续高级推理所必需的时空对齐能力。

## 4.2. Cold-Start Alignment for 4D Reasoning / 用于 4D 推理的冷启动对齐

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> As shown in Fig. 4, to transition from basic perception to complex 4D analysis, we introduce the Spatiotemporal Chain-of-Thought (ST-CoT), a reasoning paradigm designed to associate 2D pixel-level observations with 4D world-state representations (See Fig. 11 for detail prompting settings). Unlike conventional CoT approaches (Wei et al., 2022) that primarily navigate linguistic logic, ST-CoT compels the model to operate as a 3D perception engine, grounding its internal reasoning in visual physics and motion dynamics over time. We utilize this framework to curate a specialized cold-start dataset (see Appendix 8.3 for details). By performing cold-start alignment on this structured data using the same LoRA parameter and loss objective $\mathcal{L}_{ce}$ as the SFT stage, we establish a policy initialization that serves as a stable foundation for subsequent reinforcement learning. The ST-CoT guideline follows the five-step logical flow:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 如图 4 所示，为从基础感知过渡到复杂 4D 分析，我们引入时空思维链（ST-CoT），一种旨在将 2D 像素级观测与 4D 世界状态表示关联起来的推理范式（详细提示设置见图 11）。不同于主要处理语言逻辑的传统 CoT 方法（Wei et al., 2022），ST-CoT 迫使模型作为 3D 感知引擎运行，将其内部推理建立在随时间变化的视觉物理和运动动力学之上。我们利用该框架整理专门的冷启动数据集（细节见附录 8.3）。在结构化数据上执行冷启动对齐时，使用与 SFT 阶段相同的 LoRA 参数和损失目标 $\mathcal{L}_{ce}$，从而建立可作为后续强化学习稳定基础的策略初始化。ST-CoT 指南遵循五步逻辑流程：

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Step 1: Objective Alignment and Temporal Anchoring:** The reasoning process begins by explicitly defining the spatiotemporal objective $O_{obj}$. The model identifies the query’s intent and locks onto critical temporal boundaries (the start frame $t_{start}$ and end frame $t_{end}$), which prevent computational drift during video processing.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **步骤 1：目标对齐与时间锚定：** 推理过程首先明确规定时空目标 $O_{obj}$。模型识别问题意图，并锁定关键时间边界（起始帧 $t_{start}$ 和结束帧 $t_{end}$），防止视频处理过程中的计算漂移。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Step 2: Start frame 3D State Parsing and Anchoring:** At the start frame $t_{start}$, the model performs a joint visual and geometric analysis to output the initial spatial state $S_{t_{start}}$. By anchoring the camera center, object center, and scene descriptions, the model establishes a quantitative baseline for all subsequent motion estimations.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **步骤 2：起始帧 3D 状态解析与锚定：** 在起始帧 $t_{start}$，模型执行视觉与几何联合分析，输出初始空间状态 $S_{t_{start}}$。通过锚定相机中心、物体中心和场景描述，模型为后续所有运动估计建立定量基线。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Step 3: Temporal Progression and Visual Cue Collection:** Rather than relying on implicit visual flow, the model rationalizes the physical shift between boundaries. It analyzes visual transformations, such as scale expansion and perspective distortion, to infer underlying geometric deltas $T_{motion}$, creating a causal bridge between visual observation and 4D physical motion.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **步骤 3：时间推进与视觉线索收集：** 模型不依赖隐含的视觉流，而是对边界之间的物理位移进行推理。它分析尺度扩张和透视畸变等视觉变换，以推断底层几何变化 $T_{motion}$，在视觉观测与 4D 物理运动之间建立因果桥梁。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Step 4: End frame 3D State Verification:** Upon reaching $t_{end}$, the model generates the terminal spatial state $S_{t_{end}}$ and a corresponding visual summary. This serves as a consistency check; by comparing $S_{t_{end}}$ with $S_{t_{start}}$, the model validates the continuity of the spatiotemporal trajectory and minimizes temporal hallucinations.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **步骤 4：结束帧 3D 状态验证：** 到达 $t_{end}$ 后，模型生成终止空间状态 $S_{t_{end}}$ 及对应的视觉摘要。这充当一致性检查：通过将 $S_{t_{end}}$ 与 $S_{t_{start}}$ 比较，模型验证时空轨迹的连续性并减少时间幻觉。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Step 5: Evidence-Based Synthesis and Probabilistic Inference:** Finally, the model synthesizes the accumulated visual evidence into a comprehensive trajectory. We formally define the ST-CoT as the coherent sequence $T_{ST}=\{O_{obj},S_s,T_{motion},S_e\}$, aggregating the objective $O_{obj}$, spatial anchors ($S_s$ & $S_e$), and temporal motion ($T_{motion}$). The final answer $\hat a$ is derived through a maximum a posteriori estimation, conditioned strictly on this reconstructed 4D trajectory and the raw video input $V$:

$$\hat a=\arg\max_{a\in A}P\left(a\mid O_{obj},S_s,T_{motion},S_e\ \middle|\ T_{ST},V;\theta\right). \tag{2}$$

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **步骤 5：基于证据的综合与概率推断：** 最后，模型将累积的视觉证据综合为完整轨迹。我们将 ST-CoT 正式定义为连贯序列 $T_{ST}=\{O_{obj},S_s,T_{motion},S_e\}$，汇总目标 $O_{obj}$、空间锚点（$S_s$ 与 $S_e$）和时间运动（$T_{motion}$）。最终答案 $\hat a$ 通过最大后验估计得到，并严格以重建的 4D 轨迹和原始视频输入 $V$ 为条件：

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> This formulation ensures that the final output is not a hallucinated guess but a logical derivative of the explicit 4D progression. By forcing the model to justify its answer through the established trajectory $T_{ST}$, we enhance the interpretability and capability of the 4D reasoning task.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 该形式确保最终输出不是幻觉式猜测，而是明确 4D 演化的逻辑推导。通过迫使模型依据已建立的轨迹 $T_{ST}$ 解释答案，我们增强了 4D 推理任务的可解释性和能力。

## 4.3. Reinforcement Fine-Tuning for 4D Reasoning / 用于 4D 推理的强化微调

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Building upon the policy initialization from the cold-start phase, we employ GRPO (Shao et al., 2024; Liu et al., 2024a) to further enhance the model’s reasoning capabilities, leveraging the proposed MLLM4D-R1-30k dataset. Unlike traditional Actor-Critic frameworks, GRPO eliminates the need for a separate value function by utilizing the relative rewards within a sampled group. For each input $q$, we sample a group of $G$ outputs $\{o_1,o_2,\ldots,o_G\}$ from the current policy $\pi_\theta$. The training objective is to maximize the following surrogate loss:

$$\mathcal{L}_{grpo}=\mathbb{E}\left[\frac{1}{G}\sum_{g=1}^{G}\min\left(\rho_gA_g,\operatorname{clip}(\rho_g,1-\epsilon,1+\epsilon)A_g\right)-\beta D_{KL}(\pi_\theta\Vert\pi_{ref})\right]. \tag{3}$$

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 基于冷启动阶段得到的策略初始化，我们利用 GRPO（Shao et al., 2024; Liu et al., 2024a）并借助提出的 MLLM4D-R1-30k 数据集，进一步增强模型的推理能力。不同于传统 Actor-Critic 框架，GRPO 利用采样组内的相对奖励，不再需要单独的价值函数。对于每个输入 $q$，我们从当前策略 $\pi_\theta$ 中采样一组 $G$ 个输出 $\{o_1,o_2,\ldots,o_G\}$。训练目标是最大化以下替代损失：

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> where $\rho_g=\frac{\pi_\theta(o_g|q)}{\pi_{old}(o_g|q)}$ is the importance sampling ratio, and $\pi_{ref}$ is the reference model (the cold-start checkpoint in our work). The advantage $A_g$ is computed by normalizing the rewards within the group: $A_g=\frac{r_g-\operatorname{mean}(r)}{\operatorname{std}(r)}$. While conventional reinforcement learning relies on format and accuracy-based rewards, the specialization of our model for 4D environments hinges upon our proposed Spatiotemporal Reward (ST-Reward). This reward mechanism serves as a critical supervisor, grounding the ST-CoT reasoning trajectories in precise spatial and temporal physical quantities to ensure logical consistency. As illustrated in Fig. 4, the integration of ST-Reward facilitates the emergence of sophisticated 4D analysis by refining the policy’s ability to generate physically-grounded thoughts.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 其中，$\rho_g=\frac{\pi_\theta(o_g|q)}{\pi_{old}(o_g|q)}$ 是重要性采样比率，$\pi_{ref}$ 是参考模型（本文中为冷启动检查点）。优势 $A_g$ 通过对组内奖励归一化计算：$A_g=\frac{r_g-\operatorname{mean}(r)}{\operatorname{std}(r)}$。传统强化学习依赖格式和准确率奖励，而我们模型针对 4D 环境的专门化能力依赖提出的时空奖励（ST-Reward）。该奖励机制充当关键监督器，将 ST-CoT 推理轨迹锚定在精确的空间和时间物理量上，以确保逻辑一致性。如图 4 所示，ST-Reward 的集成通过改进策略生成物理约束思维的能力，促进了复杂 4D 分析的形成。

### Accuracy and Format Reward / 准确率与格式奖励

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The accuracy reward $R_{Acc}$ evaluates the correctness of the final prediction, reinforcing alignment with ground-truth labels:

$$
R_{Acc}=\begin{cases}1,&\text{if answer is right},\\0,&\text{if answer is wrong}.\end{cases} \tag{4}
$$

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 准确率奖励 $R_{Acc}$ 评估最终预测是否正确，强化其与真值标签的一致性：

$$R_{Acc}=\begin{cases}1,&\text{若答案正确},\\0,&\text{若答案错误}。
\end{cases} \tag{4}$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The format reward complements the accuracy reward by enforcing strict adherence to the predefined response structure. We utilize regular expressions to verify that the generated trajectories follow the required structure: `<thinking> Textual Reasoning... Object Center:[...] Camera Center:[...] Textual Reasoning...</thinking> <answer>Final Answer</answer>`.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 格式奖励通过强制严格遵循预定义的回答结构来补充准确率奖励。我们使用正则表达式验证生成轨迹是否遵循所需结构：`<thinking> Textual Reasoning... Object Center:[...] Camera Center:[...] Textual Reasoning...</thinking> <answer>Final Answer</answer>`。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The total format reward is decomposed as $R_{Fmt}=\lambda_1R_{Stru\_fmt}+\lambda_2R_{ST\_fmt}$, where $R_{Stru\_fmt}\in\{0,1\}$ indicates whether the response is correctly encapsulated within `<thinking>` and `<answer>` tags, fostering a standardized CoT workflow. More importantly, we introduce $R_{ST\_fmt}$ rewards the explicit provision of Object Center and Camera Center coordinates in bracketed array formats. This structural constraint serves as a prerequisite, ensuring the reasoning process is parsable for subsequent spatiotemporal reward computation. \tag{5}$

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 总格式奖励分解为 $R_{Fmt}=\lambda_1R_{Stru\_fmt}+\lambda_2R_{ST\_fmt}$，其中 $R_{Stru\_fmt}\in\{0,1\}$ 表示回答是否正确封装在 `<thinking>` 和 `<answer>` 标签内，从而形成标准化 CoT 流程。更重要的是，我们引入 $R_{ST\_fmt}$，奖励以方括号数组格式明确提供 Object Center 和 Camera Center 坐标。该结构约束是后续计算时空奖励的前提，确保推理过程可被解析。

### Spatiotemporal Reward / 时空奖励

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> To constrain reasoning trajectories within a physically plausible 4D world state, we introduce the ST-reward. This reward ensures the model’s internal reasoning is grounded in a physically plausible 4D world state rather than mere 2D pixel displacement. It quantitatively evaluates the model’s ability to localize the camera and object at critical temporal anchors, specifically the start and end frames of the video sequence.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 为将推理轨迹约束在物理上合理的 4D 世界状态内，我们引入 ST-reward。该奖励确保模型内部推理建立在物理上合理的 4D 世界状态之上，而非仅仅依据 2D 像素位移。它定量评估模型在关键时间锚点（具体为视频序列的起始帧和结束帧）定位相机和物体的能力。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> The camera and object rewards are computed by mapping the Mean Euclidean Error (MEE) between predicted coordinates $p_i$ and ground-truth centers $g_i$ to a normalized range $[0,1]$ via an exponential decay function:

$$R_{Cam/Obj}=\exp\left(-\frac{1}{n}\sum_{i=1}^{n}\lVert p_i-g_i\rVert_2\right). \tag{6}$$

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 相机和物体奖励通过指数衰减函数，将预测坐标 $p_i$ 与真值中心 $g_i$ 之间的平均欧氏误差（MEE）映射到归一化范围 $[0,1]$：

$$R_{Cam/Obj}=\exp\left(-\frac{1}{n}\sum_{i=1}^{n}\lVert p_i-g_i\rVert_2\right). \tag{6}$$

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> where $\lVert\cdot\rVert_2$ denotes the $L_2$ norm. A reward of 1.0 indicates perfect spatial-temporal alignment. Thus the final ST-reward is a composite signal defined as $R_{ST}=\lambda_{Cam}R_{Cam}+\lambda_{Obj}R_{Obj}$. By enforcing explicit coordinate prediction, $R_{ST}$ serves as a physical regularizer, effectively mitigating spatiotemporal hallucinations and ensuring the reasoning process adheres to the underlying 4D dynamics. Consequently, the total reward $R$ for GRPO training is defined as $R=\lambda_{Acc}R_{Acc}+\lambda_{Fmt}R_{Fmt}+\lambda_{ST}R_{ST}$. \tag{7–8}$

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 其中 $\lVert\cdot\rVert_2$ 表示 $L_2$ 范数。奖励为 1.0 表示完美的时空对齐。因此，最终 ST-reward 是复合信号：$R_{ST}=\lambda_{Cam}R_{Cam}+\lambda_{Obj}R_{Obj}$。通过强制显式预测坐标，$R_{ST}$ 充当物理正则项，有效减轻时空幻觉并确保推理过程遵循底层 4D 动力学。因此，GRPO 训练的总奖励定义为 $R=\lambda_{Acc}R_{Acc}+\lambda_{Fmt}R_{Fmt}+\lambda_{ST}R_{ST}$。

# 5. Experiments / 实验

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Please refer to the Appendix for the experimental setup, such as implementation details, and the comparison baselines.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 实验设置（例如实现细节和比较基线）请参阅附录。

## Table 1 / 表 1

![Table 1](assets/table_1.svg)

**Caption:** Comparison of different models on MLLM4D-Bench. Bold font indicates the best performance.

**Caption[CN]:** 不同模型在 MLLM4D-Bench 上的比较。粗体表示最佳性能。

| Models | Camera Abs. Dis. | Camera Rel. Dir. | Object Abs. Dis. | Object Abs. Dis. (Object & Camera) | Object Rel. Dis. | Object Rel. Dir. | Avg. |
|---|---:|---:|---:|---:|---:|---:|---:|
| GPT-4o | 34.8 | 57.6 | 32.7 | 36.7 | 56.7 | 51.0 | 44.9 |
| Gemini2.5-Flash | 35.2 | 59.4 | 24.1 | 37.8 | 55.3 | 50.6 | 43.8 |
| Gemini2.5-Pro | 37.4 | 57.5 | 31.1 | 38.6 | 60.1 | 55.0 | 46.6 |
| Qwen2.5-VL-7B | 25.0 | 58.0 | 24.6 | 25.0 | 42.5 | 30.6 | 34.3 |
| Qwen2.5-VL-32B | 32.2 | 52.0 | 31.0 | 30.0 | 3.2 | 9.1 | 26.2 |
| Qwen3-VL-8B | 36.0 | 60.4 | 33.8 | 27.2 | 26.4 | 28.2 | 35.3 |
| Qwen3-VL-32B | 40.4 | 60.8 | 35.1 | 35.2 | 39.5 | 37.0 | 41.3 |
| LLaVA-NeXT-Video-7B | 22.6 | 26.0 | 24.6 | 24.3 | 33.4 | 32.6 | 27.3 |
| InternVideo2.5-8B | 9.4 | 48.2 | 9.5 | 9.3 | 22.3 | 18.6 | 19.6 |
| InternVL2.5-8B | 27.5 | 43.4 | 5.8 | 7.2 | 21.0 | 16.1 | 20.2 |
| InternVL2.5-38B | 7.7 | 16.4 | 9.4 | 14.1 | 24.0 | 17.4 | 14.8 |
| InternVL3.5-8B | 34.5 | 55.9 | 33.7 | 34.3 | 41.2 | 36.0 | 39.3 |
| InternVL3.5-38B | 24.3 | 22.6 | 24.0 | 40.9 | 40.7 | 37.1 | 31.6 |
| VLM-3R (LLaVA-Video-7B) | 29.0 | 56.0 | 24.6 | 29.2 | 20.4 | 24.6 | 30.6 |
| VG-LLM (Qwen2.5-VL-7B) | 54.9 | 55.7 | 55.6 | 55.7 | 61.8 | 54.3 | 56.3 |
| **Our MLLM-4D (Qwen2.5-VL-7B)** | **73.3** | **68.1** | **75.7** | **73.0** | **70.9** | **60.4** | **70.2** |
| **Our MLLM-4D (Qwen3-VL-8B)** | **73.4** | **71.9** | **76.3** | **74.3** | 69.2 | **70.9** | **72.7** |

> **Column note / 列说明：** The PDF groups the six task columns under Camera, Object, and Object & Camera; the searchable transcription retains the displayed numeric order and labels. Source anchor: PDF p. 7.

## 5.1. Comparisons on MLLM4D-Bench / 在 MLLM4D-Bench 上的比较

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We compare our MLLM-4D with baselines for 4D spatial-temporal reasoning on MLLM4D-Bench. As shown in Table 1, MLLM-4D significantly outperforms all proprietary models, open-source and 3D spatial reasoning MLLMs. Specifically, our MLLM-4D (Qwen3-VL-8B) variant achieves a state-of-the-art average score of 72.7%, surpassing high-performing proprietary models like Gemini 2.5 Pro (46.6%) by a substantial margin. Qualitative comparisons provided in Fig. 12, Fig. 13 and Fig. 14 further highlight our model’s superiority. Beyond simply providing accurate final answers, MLLM-4D demonstrates interpretable 4D reasoning by explicitly modeling the Spatiotemporal Chain-of-Thought (ST-CoT). In contrast, baseline models, including open-source models like Qwen3-VL-8B and 3D spatial reasoning models like VG-LLM, often lack a fundamental understanding of 4D spatiotemporal dynamics. These baselines rely on guesswork or 2D visual cues, leading to incorrect results in 4D reasoning tasks.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们在 MLLM4D-Bench 上将 MLLM-4D 与 4D 时空推理基线进行比较。如表 1 所示，MLLM-4D 显著优于所有专有模型、开源模型和 3D 空间推理 MLLM。具体而言，我们的 MLLM-4D（Qwen3-VL-8B）版本取得 72.7% 的最先进平均分，大幅超过 Gemini 2.5 Pro（46.6%）等高性能专有模型。图 12、图 13 和图 14 的定性比较进一步凸显了我们模型的优势。MLLM-4D 不仅提供准确的最终答案，还通过显式建模时空思维链（ST-CoT）展现可解释的 4D 推理。相比之下，包括 Qwen3-VL-8B 等开源模型和 VG-LLM 等 3D 空间推理模型在内的基线，往往缺乏对 4D 时空动力学的基础理解。这些基线依赖猜测或 2D 视觉线索，导致在 4D 推理任务中得到错误结果。

## 5.2. Comparisons on VLM4D Benchmark / 在 VLM4D 基准上的比较

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> To demonstrate the generalizability of our model on out-of-distribution datasets, we further evaluate performance on VLM4D benchmark (Zhou et al., 2025b). As shown in Table 2, MLLM-4D maintains superior performance, outperforming based model (Qwen3-VL-8B and Qwen2.5-VL-7B) and specialized 3D spatial reasoning models (VLM-3R and VG-LLM) by a significant margin. Qualitative results provided in Fig. 15 to Fig. 17 illustrate that by leveraging the ST-CoT reasoning paradigm, the 4D spatiotemporal intelligence of MLLM-4D can effectively translate to diverse environments beyond our training distribution.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 为展示模型在分布外数据集上的泛化性，我们进一步在 VLM4D 基准（Zhou et al., 2025b）上评估性能。如表 2 所示，MLLM-4D 保持更优性能，以显著幅度超过基础模型（Qwen3-VL-8B 和 Qwen2.5-VL-7B）以及专门的 3D 空间推理模型（VLM-3R 和 VG-LLM）。图 15 至图 17 的定性结果表明，借助 ST-CoT 推理范式，MLLM-4D 的 4D 时空智能能够有效迁移到训练分布之外的多样环境。

## Table 2 / 表 2

![Table 2](assets/table_2.svg)

**Caption:** Evaluation on VLM4D benchmark.

**Caption[CN]:** 在 VLM4D 基准上的评估。

| Models | Real | Synthetic | Overall |
|---|---:|---:|---:|
| GPT-4o | 60.0 | 49.9 | 57.5 |
| Gemini-2.5-Pro | 63.5 | 57.3 | 62.0 |
| Qwen2.5-VL-7B | 43.3 | 45.6 | 43.8 |
| Qwen2.5-VL-72B | 53.1 | 52.6 | 53.0 |
| Qwen3-VL-8B | 52.1 | 52.4 | 52.2 |
| InternVideo2.5-8B | 52.7 | 44.5 | 50.7 |
| LLaVA-NeXT-Video-7B | 38.2 | 29.9 | 36.2 |
| VLM-3R (LLaVA-NeXT-Video-7B) | 36.9 (0.9↓) | 24.7 (5.2↓) | 33.9 (2.3↓) |
| VG-LLM (Qwen2.5-VL-7B) | 49.5 (6.2↑) | 37.3 (8.3↓) | 46.5 (2.7↑) |
| Our MLLM-4D (Qwen2.5-VL-7B) | 59.4 (16.1↑) | 49.7 (4.1↑) | 57.0 (13.2↑) |
| Our MLLM-4D (Qwen3-VL-8B) | 63.1 (11.0↑) | 54.4 (2.0↑) | 61.0 (8.8↑) |

> **Source anchor:** PDF p. 8. Parenthetical arrows are the comparative changes printed in the source table.

## 5.3. Ablation Studies / 消融研究

### Scalability of Training Data / 训练数据的可扩展性

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> To evaluate the data scalability of MLLM4D-2M, we evaluate performance across training subsets of 10K, 50K, 200K, 1M, and 2M QA pairs using real-world videos of the VLM4D benchmark. As illustrated in Fig. 5 (a), the model exhibits a rapid performance surge in the initial scaling phase, with accuracy rising from a 52.1% baseline to 57.7% when using 200K samples. Beyond this threshold, performance continues to scale consistently, reaching 59.7% at 2M samples. This sustained upward trajectory confirms that the MLLM4D-2M dataset effectively captures increasingly complex 4D spatial-temporal patterns as the data volume expands. We further analyze the scaling behavior during the RFT stage using subsets of MLLM4D-R1-30k ranging from 1K to 30K pairs. As shown in Fig. 5 (b), despite a minor initial fluctuation at 1K due to the model adapting to the reasoning format, the model exhibits a robust scaling trend beyond 3K samples. Accuracy improves from 59.8% to a peak of 63.1% at 30K samples, highlighting the scalability of our MLLM4D-R1-30k dataset.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 为评估 MLLM4D-2M 的数据可扩展性，我们使用 VLM4D 基准的真实视频，在 10K、50K、200K、1M 和 2M 个 QA 对的训练子集上评估性能。如图 5(a) 所示，模型在初始规模化阶段性能快速提升：使用 200K 样本时，准确率从 52.1% 基线升至 57.7%。超过这一阈值后，性能继续稳定扩展，在 2M 样本时达到 59.7%。这一持续上升趋势证实，随着数据量增加，MLLM4D-2M 数据集有效捕获了日益复杂的 4D 时空模式。我们进一步使用 1K 至 30K 的 MLLM4D-R1-30k 子集分析 RFT 阶段的规模化行为。如图 5(b) 所示，尽管模型因适应推理格式在 1K 处出现轻微初始波动，但在超过 3K 样本后表现出稳健的规模化趋势；准确率从 59.8% 提升到 30K 样本时的峰值 63.1%，体现了 MLLM4D-R1-30k 数据集的可扩展性。

## Figure 5 / 图 5

**Caption:** Scalability of training data on SFT and RFT stage.

**Caption[CN]:** SFT 和 RFT 阶段训练数据的可扩展性。

### Effectiveness of MLLM-4D / MLLM-4D 的有效性

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Based on the ablation study presented in Table 3, our post-training framework progressively enhances 4D spatiotemporal reasoning capabilities of MLLM across both the MLLM4D-Bench and VLM4D benchmarks. The results highlight the following key insights: (1) Impact of SFT: the transition from the Baseline to SFT version of MLLM-4D yields a substantial performance leap, particularly on the MLLM4D-Bench, where scores nearly double from 35.3% to 70.1%. This confirms that the MLLM4D-2M dataset effectively establishes a robust foundational 4D understanding. (2) Scalable Spatial-temporal Data Curation: we compared our primary data curation pipeline against an alternative method based on monocular videos (see details in Appendix 8.4). While both large-scale 4D datasets drive significant improvements, the pipeline proposed in Sec. 3 yields superior results. This suggests that our pipeline provides higher-quality data, whereas monocular-based pipelines often suffer from depth ambiguity and diminished spatial accuracy. (3) Benefits of RFT: applying GRPO with standard accuracy and format rewards provides robust performance gains over SFT. (4) Advantage of ST-reward: the full post-training, including the ST-reward, achieves the highest performance (72.7% on MLLM4D-Bench and 63.1% on VLM4D). This validates that grounding the reasoning process in 4D physical quantities through ST-reward functions significantly boosts the model’s capacity for complex spatiotemporal reasoning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 根据表 3 的消融研究，我们的后训练框架在 MLLM4D-Bench 和 VLM4D 两个基准上逐步增强了 MLLM 的 4D 时空推理能力。结果带来以下关键认识：(1) **SFT 的影响：** 从 Baseline 到 MLLM-4D 的 SFT 版本带来显著性能跃升，尤其在 MLLM4D-Bench 上，分数几乎从 35.3% 翻倍至 70.1%。这证实 MLLM4D-2M 数据集有效建立了稳健的基础 4D 理解。(2) **可扩展的时空数据整理：** 我们将主要数据整理流水线与基于单目视频的替代方法进行比较（详见附录 8.4）。尽管两个大规模 4D 数据集都带来显著提升，第 3 节提出的流水线结果更优。这说明我们的流水线提供了更高质量的数据，而基于单目的流水线往往受到深度歧义和空间精度下降的影响。(3) **RFT 的收益：** 使用标准准确率和格式奖励的 GRPO 相比 SFT 带来稳健的性能提升。(4) **ST-reward 的优势：** 包括 ST-reward 在内的完整后训练达到最高性能（MLLM4D-Bench 上 72.7%，VLM4D 上 63.1%）。这验证了通过 ST-reward 函数将推理过程建立在 4D 物理量上，能显著提升模型进行复杂时空推理的能力。

## Table 3 / 表 3

![Table 3](assets/table_3.svg)

**Caption:** Ablation study of MLLM-4D framework.

**Caption[CN]:** MLLM-4D 框架的消融研究。

| Setting | MLLM4D-Bench | VLM4D |
|---|---:|---:|
| Baseline | 35.3 | 52.1 |
| SFT (w/o data in Sec. 3) | 59.9 | 56.2 |
| SFT (w/ data in Sec. 3) | 70.1 | 59.7 |
| GRPO (w/o ST-reward) | 70.5 | 61.4 |
| GRPO (w/ ST-reward) | 72.7 | 63.1 |

# 6. Conclusion / 结论

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We present MLLM-4D, a comprehensive framework designed to advance the 4D spatiotemporal reasoning capabilities of MLLMs. To address the scarcity of high-quality data, we introduce an automated curation pipeline for large-scale 4D instructional pairs. We bridge the gap in specialized 4D-aware modeling by establishing foundational 4D understanding via SFT and subsequently unlocking advanced 4D reasoning capabilities by employing GRPO with specialized ST-CoT and ST-reward functions. We hope that our data, models, and methodology inspire future research into 4D spatiotemporal intelligence and facilitate the development of interactive AI systems in the real world.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们提出 MLLM-4D，一个旨在推进 MLLM 4D 时空推理能力的综合框架。为解决高质量数据稀缺问题，我们引入大规模 4D 指令对的自动化整理流水线。我们通过 SFT 建立基础 4D 理解，随后采用带有专门 ST-CoT 和 ST-reward 函数的 GRPO，释放高级 4D 推理能力，从而弥合专门 4D 感知建模方面的差距。我们希望我们的数据、模型和方法能够启发未来关于 4D 时空智能的研究，并促进现实世界交互式 AI 系统的发展。

# 7. Impact Statement / 影响声明

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> MLLM-4D provides a comprehensive framework designed to boost the spatial-temporal intelligence of MLLMs. This advancement is particularly beneficial for interactive AI systems such as VR/AR, autonomous driving, and robotics. In varied application scenarios, it is essential to follow the corresponding usage guidelines to ensure its proper and ethical application, minimizing any potential risks.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> MLLM-4D 提供了一个旨在增强 MLLM 时空智能的综合框架。这一进展尤其有益于 VR/AR、自动驾驶和机器人等交互式 AI 系统。在不同应用场景中，遵循相应的使用指南对于确保其适当且合乎伦理的应用、尽量降低潜在风险十分重要。

# References / 参考文献

> <span style="color:#3B82F6"><strong>Para. R:</strong></span> The following references are retained in the source’s searchable bibliographic form, as permitted by the reader contract; citation keys and bibliographic literals are not translated.

> <span style="color:#F59E0B"><strong>Para. R[CN]:</strong></span> 以下参考文献按原文可检索书目形式保留，符合本阅读稿约定；引用键和书目中的精确文字不翻译。

1. Azuma, D., Miyanishi, T., Kurita, S., and Kawanabe, M. Scanqa: 3d question answering for spatial scene understanding. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pp. 19129–19139, 2022.
2. Badki, A., Su, H., Wen, B., and Gallo, O. L4p: Low-level 4d vision perception unified. *arXiv preprint arXiv:2502.13078*, 2025.
3. Bai, S., Cai, Y., Chen, R., Chen, K., Chen, X., Cheng, Z., Deng, L., Ding, W., Gao, C., Ge, C., Ge, W., Guo, Z., Huang, Q., Huang, J., Huang, F., Hui, B., Jiang, S., Li, Z., Li, M., Li, M., Li, K., Lin, Z., Lin, J., Liu, X., Liu, J., Liu, C., Liu, Y., Liu, D., Liu, S., Lu, D., Luo, R., Lv, C., Men, R., Meng, L., Ren, X., Ren, X., Song, S., Sun, Y., Tang, J., Tu, J., Wan, J., Wang, P., Wang, P., Wang, Q., Wang, Y., Xie, T., Xu, Y., Xu, H., Xu, J., Yang, Z., Yang, M., Yang, J., Yang, A., Yu, B., Zhang, F., Zhang, H., Zhang, X., Zheng, B., Zhong, H., Zhou, J., Zhou, F., Zhou, J., Zhu, Y., and Zhu, K. Qwen3-vl technical report. *arXiv preprint arXiv:2511.21631*, 2025a.
4. Bai, S., Chen, K., Liu, X., Wang, J., Ge, W., Song, S., Dang, K., Wang, P., Wang, S., Tang, J., Zhong, H., Zhu, Y., Yang, M., Li, Z., Wan, J., Wang, P., Ding, W., Fu, Z., Xu, Y., Ye, J., Zhang, X., Xie, T., Cheng, Z., Zhang, H., Yang, Z., Xu, H., and Lin, J. Qwen2.5-vl technical report. *arXiv preprint arXiv:2502.13923*, 2025b.
5. Chen, Z., Wang, W., Cao, Y., Liu, Y., Gao, Z., Cui, E., Zhu, J., Ye, S., Tian, H., Liu, Z., et al. Expanding performance boundaries of open-source multimodal models with model, data, and test-time scaling. *arXiv preprint arXiv:2412.05271*, 2024.
6. Chu, Y., Xu, J., Yang, Q., Wei, H., Wei, X., Guo, Z., Leng, Y., Lv, Y., He, J., Lin, J., et al. Qwen2-audio technical report. *arXiv preprint arXiv:2407.10759*, 2024.
7. Comanici, G., Bieber, E., Schaekermann, M., Pasupat, I., Sachdeva, N., Dhillon, I., Blistein, M., Ram, O., Zhang, D., Rosen, E., et al. Gemini 2.5: Pushing the frontier with advanced reasoning, multimodality, long context, and next generation agentic capabilities. *arXiv preprint arXiv:2507.06261*, 2025.
8. Deng, J., He, T., Jiang, L., Wang, T., Dayoub, F., and Reid, I. 3d-llava: Towards generalist 3d lmms with omni superpoint transformer. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pp. 3772–3782, 2025.
9. Dihan, M. L., Hassan, M. T., PARVEZ, M. T., Hasan, M. H., Alam, M. A., Cheema, M. A., Ali, M. E., and Parvez, M. R. Mapeval: A map-based evaluation of geo-spatial reasoning in foundation models. In *International Conference on Machine Learning*, 2025.
10. Doersch, C., Luc, P., Yang, Y., Gokay, D., Koppula, S., Gupta, A., Heyward, J., Rocco, I., Goroshin, R., Carreira, J., et al. Bootstap: Bootstrapped training for tracking-any-point. In *Proceedings of the Asian Conference on Computer Vision*, pp. 3257–3274, 2024.
11. Fan, Z., Zhang, J., Li, R., Zhang, J., Chen, R., Hu, H., Wang, K., Qu, H., Wang, D., Yan, Z., et al. Vlm-3r: Vision-language models augmented with instruction-aligned 3d reconstruction. *arXiv preprint arXiv:2505.20279*, 2025.
12. Hu, E. J., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., Chen, W., et al. Lora: Low-rank adaptation of large language models. In *International Conference on Learning Representations*, 2022.
13. Huang, H., Chen, Y., Wang, Z., Huang, R., Xu, R., Wang, T., Liu, L., Cheng, X., Zhao, Y., Pang, J., et al. Chat-scene: Bridging 3d scene and large language models with object identifiers. *Advances in Neural Information Processing Systems*, pp. 113991–114017, 2024.
14. Hurst, A., Lerer, A., Goucher, A. P., Perelman, A., Ramesh, A., Clark, A., Ostrow, A., Welihinda, A., Hayes, A., Radford, A., et al. Gpt-4o system card. *arXiv preprint arXiv:2410.21276*, 2024.
15. Jia, M., Qi, Z., Zhang, S., Zhang, W., Yu, X., He, J., Wang, H., and Yi, L. Omnispatial: Towards comprehensive spatial reasoning benchmark for vision language models. *arXiv preprint arXiv:2506.03135*, 2025.
16. Jin, L., Tucker, R., Li, Z., Fouhey, D., Snavely, N., and Holynski, A. Stereo4d: Learning how things move in 3d from internet stereo videos. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pp. 10497–10509, 2025.
17. Li, B., Zhang, Y., Guo, D., Zhang, R., Li, F., Zhang, H., Zhang, K., Zhang, P., Li, Y., Liu, Z., et al. Llavaonevision: Easy visual task transfer. *arXiv preprint arXiv:2408.03326*, 2024.
18. Li, J., Li, D., Savarese, S., and Hoi, S. Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models. In *International Conference on Machine Learning*, pp. 19730–19742, 2023.
19. Li, Y., Zhang, Y., Lin, T., Liu, X., Cai, W., Liu, Z., and Zhao, B. Sti-bench: Are mllms ready for precise spatial-temporal world understanding? In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pp. 5622–5632, 2025.
20. Liu, A., Feng, B., Xue, B., Wang, B., Wu, B., Lu, C., Zhao, C., Deng, C., Zhang, C., Ruan, C., et al. Deepseekv3 technical report. *arXiv preprint arXiv:2412.19437*, 2024a.
21. Liu, H., Li, C., Wu, Q., and Lee, Y. J. Visual instruction tuning. *Advances in Neural Information Processing Systems*, pp. 34892–34916, 2023.
22. Liu, S., Zeng, Z., Ren, T., Li, F., Zhang, H., Yang, J., Jiang, Q., Li, C., Yang, J., Su, H., et al. Grounding dino: Marrying dino with grounded pre-training for open-set object detection. In *European Conference on Computer Vision*, pp. 38–55, 2024b.
23. Liu, Y., Ma, M., Yu, X., Ding, P., Zhao, H., Sun, M., Huang, S., and Wang, D. Ssr: Enhancing depth perception in vision-language models via rationale-guided spatial reasoning. *Advances in Neural Information Processing Systems*, 2025.
24. Ma, W., Chou, Y.-C., Liu, Q., Wang, X., de Melo, C., Xie, J., and Yuille, A. Spatialreasoner: Towards explicit and generalizable 3d spatial reasoning. *Advances in Neural Information Processing Systems*, 2025.
25. Ma, X., Yong, S., Zheng, Z., Li, Q., Liang, Y., Zhu, S.-C., and Huang, S. Sqa3d: Situated question answering in 3d scenes. *arXiv preprint arXiv:2210.07474*, 2022.
26. Ouyang, K., Liu, Y., Wu, H., Liu, Y., Zhou, H., Zhou, J., Meng, F., and Sun, X. Spacer: Reinforcing mllms in video spatial reasoning. *arXiv preprint arXiv:2504.01805*, 2025.
27. Ravi, N., Gabeur, V., Hu, Y.-T., Hu, R., Ryali, C., Ma, T., Khedr, H., Rä dle, R., Rolland, C., Gustafson, L., et al. Sam 2: Segment anything in images and videos. In *International Conference on Learning Representations*, 2025.
28. Ren, T., Liu, S., Zeng, A., Lin, J., Li, K., Cao, H., Chen, J., Huang, X., Chen, Y., Yan, F., et al. Grounded sam: Assembling open-world models for diverse visual tasks. *arXiv preprint arXiv:2401.14159*, 2024.
29. Schonberger, J. L. and Frahm, J.-M. Structure-from-motion revisited. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition*, pp. 4104–4113, 2016.
30. Shao, Z., Wang, P., Zhu, Q., Xu, R., Song, J., Bi, X., Zhang, H., Zhang, M., Li, Y., Wu, Y., et al. Deepseekmath: Pushing the limits of mathematical reasoning in open language models. *arXiv preprint arXiv:2402.03300*, 2024.
31. Shen, Y., Liu, Y., Zhu, J., Cao, X., Zhang, X., He, Y., Ye, W., Rehg, J. M., and Lourentzou, I. Fine-grained preference optimization improves spatial reasoning in vlms. *Advances in Neural Information Processing Systems*, 2025.
32. Tong, P., Brown, E., Wu, P., Woo, S., IYER, A. J. V., Akula, S. C., Yang, S., Yang, J., Middepogu, M., Wang, Z., et al. Cambrian-1: A fully open, vision-centric exploration of multimodal llms. *Advances in Neural Information Processing Systems*, pp. 87310–87356, 2024.
33. Wang, J., Chen, M., Karaev, N., Vedaldi, A., Rupprecht, C., and Novotny, D. Vggt: Visual geometry grounded transformer. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pp. 5294–5306, 2025a.
34. Wang, Q., Zhang, Y., Holynski, A., Efros, A. A., and Kanazawa, A. Continuous 3d perception model with persistent state. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pp. 10510–10522, 2025b.
35. Wang, R., Xu, S., Dong, Y., Deng, Y., Xiang, J., Lv, Z., Sun, G., Tong, X., and Yang, J. Moge-2: Accurate monocular geometry with metric scale and sharp details. *Advances in Neural Information Processing Systems*, 2025c.
36. Wang, W., Gao, Z., Gu, L., Pu, H., Cui, L., Wei, X., Liu, Z., Jing, L., Ye, S., Shao, J., et al. Internvl3.5: Advancing open-source multimodal models in versatility, reasoning, and efficiency. *arXiv preprint arXiv:2508.18265*, 2025d.
37. Wang, Y., Lipson, L., and Deng, J. Sea-raft: Simple, efficient, accurate raft for optical flow. In *European Conference on Computer Vision*, pp. 36–54, 2024.
38. Wang, Y., Li, X., Yan, Z., He, Y., Yu, J., Zeng, X., Wang, C., Ma, C., Huang, H., Gao, J., et al. Internvideo2.5: Empowering video mllms with long and rich context modeling. *arXiv preprint arXiv:2501.12386*, 2025e.
39. Wei, J., Wang, X., Schuurmans, D., Bosma, M., Xia, F., Chi, E., Le, Q. V., Zhou, D., et al. Chain-of-thought prompting elicits reasoning in large language models. *Advances in Neural Information Processing Systems*, pp. 24824–24837, 2022.
40. Wu, D., Liu, F., Hung, Y.-H., and Duan, Y. Spatial-mllm: Boosting mllm capabilities in visual-based spatial intelligence. *Advances in Neural Information Processing Systems*, 2025.
41. Xiao, Y., Wang, J., Xue, N., Karaev, N., Makarov, Y., Kang, B., Zhu, X., Bao, H., Shen, Y., and Zhou, X. Spatialtrackerv2: Advancing 3d point tracking with explicit camera motion. In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pp. 6726–6737, 2025.
42. Xu, J., Guo, Z., He, J., Hu, H., He, T., Bai, S., Chen, K., Wang, J., Fan, Y., Dang, K., et al. Qwen2.5-omni technical report. *arXiv preprint arXiv:2503.20215*, 2025a.
43. Xu, R., Wang, W., Tang, H., Chen, X., Wang, X., Chu, F.-J., Lin, D., Feiszli, M., and Liang, K. J. Multi-spatialmllm: Multi-frame spatial understanding with multi-modal large language models. *arXiv preprint arXiv:2505.17015*, 2025b.
44. Yang, J., Yang, S., Gupta, A. W., Han, R., Fei-Fei, L., and Xie, S. Thinking in space: How multimodal large language models see, remember, and recall spaces. In *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition*, pp. 10632–10643, 2025a.
45. Yang, S., Xu, R., Xie, Y., Yang, S., Li, M., Lin, J., Zhu, C., Chen, X., Duan, H., Yue, X., et al. Mmsi-bench: A benchmark for multi-image spatial intelligence. *arXiv preprint arXiv:2505.23764*, 2025b.
46. Yang, S., Yang, J., Huang, P., Brown II, E. L., Yang, Z., Yu, Y., Tong, S., Zheng, Z., Xu, Y., Wang, M., et al. Towards spatial supersensing in video. In *International Conference on Learning Representations*, 2026.
47. Yuan, Y., Zhang, W., Li, X., Wang, S., Li, K., Li, W., Xiao, J., Zhang, L., and Ooi, B. C. Pixelrefer: A unified framework for spatio-temporal object referring with arbitrary granularity. *arXiv*, 2025.
48. Zhang, J., Chen, Y., Xu, Y., Huang, Z., Mei, J., Chen, J., Zhou, Y., Yuan, Y.-J., Cai, X., Huang, G., Quan, X., Xu, H., and Zhang, L. From flatland to space: Teaching vision-language models to perceive and reason in 3d. *Advances in Neural Information Processing Systems*, 2025.
49. Zhang, Y., Li, B., Liu, H., Lee, Y. J., Gui, L., Fu, D., Feng, J., Liu, Z., and Li, C. Llava-next: A strong zero-shot video understanding model, 2024.
50. Zheng, D., Huang, S., Li, Y., and Wang, L. Learning from videos for 3d world: Enhancing mllms with 3d vision geometry priors. *Advances in Neural Information Processing Systems*, 2025.
51. Zhou, H., Peng, X., Kendre, S., Ryoo, M. S., Savarese, S., Xiong, C., and Niebles, J. C. Strefer: Empowering video llms with space-time referring and reasoning via synthetic instruction data. In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pp. 4289–4300, 2025a.
52. Zhou, S., Vilesov, A., He, X., Wan, Z., Zhang, S., Nagachandra, A., Chang, D., Chen, D., Wang, X. E., and Kadambi, A. Vlm4d: Towards spatiotemporal awareness in vision language models. In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pp. 8600–8612, 2025b.
53. Zhu, C., Wang, T., Zhang, W., Pang, J., and Liu, X. Llava3d: A simple yet effective pathway to empowering lmms with 3d capabilities. In *Proceedings of the IEEE/CVF International Conference on Computer Vision*, pp. 4295–4305, 2025.

# 8. Appendix / 附录

## 8.1. Implementation Details / 实现细节

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Training Details.** MLLM-4D is built on Qwen3-VL-8B-Instruct (Bai et al., 2025a) and Qwen2.5-VL-7B-Instruct (Bai et al., 2025b). During training, we utilize LoRA (Hu et al., 2022) configured with an update matrix rank of 128 and an adaptation scaling parameter of 256, and we limit video frames to 32. In the SFT stage, we train the model using Adam optimizer for one epoch (30k steps). We employ a cosine learning rate schedule with a peak learning rate of $2\times10^{-5}$, a warmup ratio of 0.01, and a global batch size of 8. In the cold start stage, we use a similar setting as in the SFT stage to train the model for about 200 steps. In the RFT stage, we perform 12 rollouts per question and set the default sampling temperature to 1. The $\lambda_{Acc}$, $\lambda_{Fmt}$, $\lambda_{ST}$, $\lambda_1$, $\lambda_2$, $\lambda_{Cam}$, $\lambda_{Obj}$ are set to 0.5, 0.2, 0.3, 0.5, 0.5, 0.5, 0.5, respectively. We train the model for 15k steps with a KL divergence coefficient $\beta$ of 0.1 and a learning rate of $5\times10^{-5}$. All experiments were conducted on 8 H100 80G GPUs; the training takes 12 hours for the SFT and cold start stage, and 50 hours for the RFT stage.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **训练细节。** MLLM-4D 构建于 Qwen3-VL-8B-Instruct（Bai et al., 2025a）和 Qwen2.5-VL-7B-Instruct（Bai et al., 2025b）之上。训练期间，我们使用 LoRA（Hu et al., 2022），其更新矩阵秩设为 128，适配缩放参数设为 256，并将视频帧数限制为 32。SFT 阶段使用 Adam 优化器训练模型一个 epoch（30k 步）。我们采用余弦学习率调度，峰值学习率为 $2\times10^{-5}$，预热比例为 0.01，全局批大小为 8。冷启动阶段采用与 SFT 阶段相似的设置，训练约 200 步。RFT 阶段每个问题执行 12 次 rollout，默认采样温度设为 1。$\lambda_{Acc}$、$\lambda_{Fmt}$、$\lambda_{ST}$、$\lambda_1$、$\lambda_2$、$\lambda_{Cam}$、$\lambda_{Obj}$ 分别设为 0.5、0.2、0.3、0.5、0.5、0.5、0.5。我们以 KL 散度系数 $\beta=0.1$ 和学习率 $5\times10^{-5}$ 训练模型 15k 步。所有实验在 8 张 H100 80G GPU 上进行；SFT 和冷启动阶段耗时 12 小时，RFT 阶段耗时 50 小时。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Comparison Baselines.** We compare our MLLM-4D with a comprehensive suite of state-of-the-art MLLMs. For proprietary models, we include GPT-4o (Hurst et al., 2024), Gemini2.5-Flash (Comanici et al., 2025) and Gemini2.5-Pro (Comanici et al., 2025). Regarding open-source MLLMs, we consider various scales of Qwen2.5-VL (Bai et al., 2025b), Qwen3-VL (Bai et al., 2025a), LLaVA-NeXT-Video (Zhang et al., 2024), InternVideo2.5 (Wang et al., 2025e), InternVL2.5 (Chen et al., 2024), and InternVL3.5 (Wang et al., 2025d) series. We also include specialized 3D spatial reasoning models, such as VG-LLM (Zheng et al., 2025) and VLM-3R (Fan et al., 2025).

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **比较基线。** 我们将 MLLM-4D 与全面的最先进 MLLM 套件进行比较。专有模型包括 GPT-4o（Hurst et al., 2024）、Gemini2.5-Flash（Comanici et al., 2025）和 Gemini2.5-Pro（Comanici et al., 2025）。对于开源 MLLM，我们考虑 Qwen2.5-VL（Bai et al., 2025b）、Qwen3-VL（Bai et al., 2025a）、LLaVA-NeXT-Video（Zhang et al., 2024）、InternVideo2.5（Wang et al., 2025e）、InternVL2.5（Chen et al., 2024）和 InternVL3.5（Wang et al., 2025d）系列的不同规模。我们还加入 VG-LLM（Zheng et al., 2025）和 VLM-3R（Fan et al., 2025）等专门的 3D 空间推理模型。

## 8.2. Details of MLLM4D-2M and MLLM4D-R1-30k Dataset Construction / 数据集构建细节

### Moving Object Noun Categories Extraction / 运动物体名词类别提取

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Given the video sequence $\{I_i\}_{i=1}^{K}$, we employ a video MLLM, i.e. Gemini-2.5-flash (Comanici et al., 2025) using the prompt shown in Fig. 6, to identify all moving entities and extract their corresponding noun categories.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 给定视频序列 $\{I_i\}_{i=1}^{K}$，我们使用视频 MLLM Gemini-2.5-flash（Comanici et al., 2025）及图 6 所示提示，识别所有运动实体并提取其对应名词类别。

### QA Pair Generation / QA 对生成

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> We organize the extracted information into a structured meta-data format. This encompasses per-frame camera poses $\{C_i\}_{i=1}^{K}$, where $C_i=[R_i|t_i]$ consists of a $3\times3$ rotation matrix $R_i$ and a $3\times1$ translation vector $t_i$; object-level metric 3D points $\{P_{i,m}\}_{i=1,...,K;m=1,...,M}$; and their corresponding semantic descriptions $\{T_m\}_{m=1}^{M}$.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 我们将提取的信息组织为结构化元数据格式，包括逐帧相机位姿 $\{C_i\}_{i=1}^{K}$（其中 $C_i=[R_i|t_i]$ 由 $3\times3$ 旋转矩阵 $R_i$ 和 $3\times1$ 平移向量 $t_i$ 组成）、物体级度量 3D 点 $\{P_{i,m}\}_{i=1,...,K;m=1,...,M}$，以及对应语义描述 $\{T_m\}_{m=1}^{M}$。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Using physical-based spatial-temporal computation, we subsequently generate QA pairs of different tasks across several spatiotemporal reasoning tasks:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 随后，我们利用基于物理的时空计算，在多种时空推理任务中生成不同任务的 QA 对：

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Camera Absolute Distance:** Measures the movement of camera between any two frames $i$ and $j$. We first compute the camera center in world coordinates as $Center_i=-R_i^Tt_i$. Then the absolute distance $d_{cam\_abs\_dis}$ is the $L_2$ norm: $d_{cam\_abs\_dis}=\lVert Center_j-Center_i\rVert_2=\sqrt{\sum_{k=1}^{3}(Center_{j,k}-Center_{i,k})^2}$. Question template: “Approximately how far (in meters) did the camera move between < frame i > and < frame j >?”

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **相机绝对距离：** 衡量相机在任意两帧 $i$ 和 $j$ 之间的移动。首先计算世界坐标中的相机中心 $Center_i=-R_i^Tt_i$。绝对距离 $d_{cam\_abs\_dis}$ 为 $L_2$ 范数：$d_{cam\_abs\_dis}=\lVert Center_j-Center_i\rVert_2=\sqrt{\sum_{k=1}^{3}(Center_{j,k}-Center_{i,k})^2}$。问题模板：“Approximately how far (in meters) did the camera move between < frame i > and < frame j >?”

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Camera Relative Direction:** Determines movement relative to the camera’s orientation at frame $i$ between any two frames $i$ and $j$. We first compute the world-space displacement $\Delta t=t_j-t_i$. To determine the movement relative to the camera’s perspective at frame $i$, we project this vector into the local camera coordinate system using the transpose of the rotation matrix $R_i^T$: $d_{cam\_rel\_dir}=R_i^T\cdot\Delta t$. The resulting vector $d_{cam\_rel\_dir}=[d_x,d_y,d_z]$ is interpreted via standard camera conventions, where $+X,+Y,+Z$ correspond to right, down, and forward direction, respectively. Question template: “During the sequence between < frame i > and < frame j >, what was the primary consistent translation of the camera’s movement relative to its position at the start?”

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **相机相对方向：** 确定任意两帧 $i$ 和 $j$ 之间相对于第 $i$ 帧相机方向的运动。首先计算世界空间位移 $\Delta t=t_j-t_i$。为了确定相对于第 $i$ 帧相机视角的运动，使用旋转矩阵转置 $R_i^T$ 将该向量投影到局部相机坐标系：$d_{cam\_rel\_dir}=R_i^T\cdot\Delta t$。所得向量 $d_{cam\_rel\_dir}=[d_x,d_y,d_z]$ 按标准相机约定解释，其中 $+X,+Y,+Z$ 分别对应右、下和前方向。问题模板：“During the sequence between < frame i > and < frame j >, what was the primary consistent translation of the camera’s movement relative to its position at the start?”

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Object Absolute Distance:** Computes the movement distance of an object between any two frames $i$ and $j$. We define the object centroid at frame $i$ as $\bar P_i=\frac{1}{M}\sum_{m=1}^{M}P_{i,m}$. Then, the object absolute distance $d_{obj\_abs\_dis}$ is calculated as the $L_2$ norm of the vector connecting their centroids: $d_{obj\_abs\_dis}=\lVert\bar P_j-\bar P_i\rVert_2=\sqrt{\sum_{k=1}^{3}(\bar P_{j,k}-\bar P_{i,k})^2}$. Question template: “Approximately how far (in meters) did < object m description > move between < frame i > and < frame j >?”

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **物体绝对距离：** 计算物体在任意两帧 $i$ 和 $j$ 之间的移动距离。将第 $i$ 帧物体质心定义为 $\bar P_i=\frac{1}{M}\sum_{m=1}^{M}P_{i,m}$。物体绝对距离 $d_{obj\_abs\_dis}$ 计算为连接两个质心的向量的 $L_2$ 范数：$d_{obj\_abs\_dis}=\lVert\bar P_j-\bar P_i\rVert_2=\sqrt{\sum_{k=1}^{3}(\bar P_{j,k}-\bar P_{i,k})^2}$。问题模板：“Approximately how far (in meters) did < object m description > move between < frame i > and < frame j >?”

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> **Object-Camera Absolute Distance:** Computes the proximity of an object at frame $j$ to the camera at frame $i$. We first compute the camera center in world coordinates as $Center_i=-R_i^Tt_i$. Then the absolute distance $d_{obj-cam\_abs}$ between the camera and the object is defined as the minimum distance from the camera center to any point within the object’s point set: $d_{obj-cam\_abs}=\min\lVert P_{j,m}-Center_i\rVert_2$. Question template: “What is the approximate distance (in meters) between the camera (or the observer filming) in < frame i > and the nearest point of the < object m description > in < frame j >?”

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> **物体-相机绝对距离：** 计算第 $j$ 帧物体与第 $i$ 帧相机之间的接近程度。首先计算世界坐标中的相机中心 $Center_i=-R_i^Tt_i$。然后，相机与物体之间的绝对距离 $d_{obj-cam\_abs}$ 定义为相机中心到物体点集内任意点的最小距离：$d_{obj-cam\_abs}=\min\lVert P_{j,m}-Center_i\rVert_2$。问题模板：“What is the approximate distance (in meters) between the camera (or the observer filming) in < frame i > and the nearest point of the < object m description > in < frame j >?”

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> **Object-Camera Relative Distance:** Determines whether the camera and object are converging or diverging between any two frames $i$ and $j$. We first find the camera center to any point within the object’s point set: $d_i=\min\lVert P_{i,m}-Center_i\rVert_2$. Then the relative change in distance, $\Delta d$, is the difference between the instantaneous distances at frame $j$ and frame $i$: $\Delta d=d_j-d_i$. Based on a distance threshold $\tau$, the relative movement is classified into a discrete state $S=$ farther if $\Delta d>\tau$; closer if $\Delta d<-\tau$; otherwise not moving. Question template: “During the sequence between < frame i > and < frame j >, is the distance between < object m description > and the camera (or the observer filming) getting closer or farther away?”

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **物体-相机相对距离：** 确定相机与物体在任意两帧 $i$ 和 $j$ 之间是在接近还是远离。首先计算相机中心到物体点集内任意点的距离：$d_i=\min\lVert P_{i,m}-Center_i\rVert_2$。然后，相对距离变化 $\Delta d$ 是第 $j$ 帧和第 $i$ 帧瞬时距离之差：$\Delta d=d_j-d_i$。依据距离阈值 $\tau$，将相对运动分类为离散状态：若 $\Delta d>\tau$，则为 farther；若 $\Delta d<-\tau$，则为 closer；否则为 not moving。问题模板：“During the sequence between < frame i > and < frame j >, is the distance between < object m description > and the camera (or the observer filming) getting closer or farther away?”

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **Object-Camera Relative Direction:** determine the relative direction between the camera and the moving object between is getting left/right or closer/farther between any two frames $i$ and $j$. We first transform the object points from both time steps into the camera’s local coordinate system at frame $i$: $P^c_i=R_iP_i+t_i$. Then we calculate the centroid of the object in the camera’s coordinate space for both sets: $\bar P^c_i=\frac{1}{M}\sum_{m=1}^{M}(R_iP_{i,m}+t_i)$, $\bar P^c_j=\frac{1}{M}\sum_{m=1}^{M}(R_iP_{j,m}+t_i)$. We then classify the lateral change $\Delta x=\bar P^c_{j,x}-\bar P^c_{i,x}$ (left/right) and the longitudinal change $\Delta z=\bar P^c_{j,z}-\bar P^c_{i,z}$ (closer/farther) using threshold $\tau$. Question template: “During the sequence between < frame i > and < frame j >, is < object m description > getting left or right from the camera (or the observer filming) relative to camera’s position at the start?” or “During the sequence between < frame i > and < frame j >, is < object m description > getting closer or farther away from the camera (or the observer filming) relative to camera’s position at the start?”

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **物体-相机相对方向：** 确定相机与运动物体在任意两帧 $i$ 和 $j $之间的相对方向，即物体相对于相机是向左/右移动，还是接近/远离。首先将两个时刻的物体点变换到第 $i$ 帧相机的局部坐标系：$P^c_i=R_iP_i+t_i$。然后分别在相机坐标空间中计算物体质心：$\bar P^c_i=\frac{1}{M}\sum_{m=1}^{M}(R_iP_{i,m}+t_i)$，$\bar P^c_j=\frac{1}{M}\sum_{m=1}^{M}(R_iP_{j,m}+t_i)$。再使用阈值 $\tau$ 分类横向变化 $\Delta x=\bar P^c_{j,x}-\bar P^c_{i,x}$（左/右）和纵向变化 $\Delta z=\bar P^c_{j,z}-\bar P^c_{i,z}$（接近/远离）。问题模板保留为：“During the sequence between < frame i > and < frame j >, is < object m description > getting left or right from the camera (or the observer filming) relative to camera’s position at the start?” 或 “During the sequence between < frame i > and < frame j >, is < object m description > getting closer or farther away from the camera (or the observer filming) relative to camera’s position at the start?”

### Data Filtering and Balancing Protocols / 数据过滤与平衡协议

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> After calculating the ground-truth values, we apply templates to formulate the final QA pairs. We implement several filtering and balancing protocols to ensure quality: we limit the number of QA pairs per video to maintain scene diversity and shuffle multiple-choice options to eliminate positional bias. Additionally, the distractors for numerical options are randomly generated within 25%–175% of the true value to prevent unrealistic shifts. After filtering, we retain 2M high-quality QA pairs across approximately 100k videos, forming the large-scale MLLM4D-2M dataset for supervised fine-tuning.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 计算真值后，我们应用模板构造最终 QA 对。为保证质量，我们实施多项过滤和平衡协议：限制每个视频的 QA 对数量以保持场景多样性，并打乱多选项以消除位置偏差。此外，数值选项的干扰项在真实值的 25%–175% 范围内随机生成，以避免不现实的偏移。过滤后，我们在约 100k 个视频中保留 2M 个高质量 QA 对，形成用于监督微调的大规模 MLLM4D-2M 数据集。

## 8.3. Details of Cold Start / 冷启动细节

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> To align the model’s output with the desired reasoning format, we conducted a brief cold-start fine-tuning phase consisting of 200 steps before GRPO training, following the same hyperparameters as SFT. The cornerstone of this phase involves constructing a reasoning dataset with Chain-of-Thought (CoT) annotations derived from pre-collected question-answer pairs. The construction process is detailed as follows:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 为使模型输出与期望的推理格式对齐，我们在 GRPO 训练前进行了包含 200 步的短暂冷启动微调阶段，使用与 SFT 相同的超参数。该阶段的核心是利用预先收集的问答对构建带有思维链（CoT）标注的推理数据集。构建过程如下：

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Subset Sampling.** We begin by sampling a subset $D_0=\bigcup_{s=1}^{7}D_s$ from the MLLM4D-2M dataset, which is constructed by drawing samples across all 7 distinct scenarios covered in the original dataset. Specifically, $D_s=\{I^s_i\}_{i=1}^{N}=\{\langle Q^s_i,A^s_i,V^s_i\rangle\}_{i=1}^{N}$, where each instance is uniformly sourced from the diverse scenario pool.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **子集采样。** 我们从 MLLM4D-2M 数据集中采样子集 $D_0=\bigcup_{s=1}^{7}D_s$；该数据集从原始数据集覆盖的全部 7 个不同场景中抽取样本构成。具体而言，$D_s=\{I^s_i\}_{i=1}^{N}=\{\langle Q^s_i,A^s_i,V^s_i\rangle\}_{i=1}^{N}$，其中每个实例均从多样场景池中均匀抽取。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Multi-path CoT Generation.** For each sample $I^s_i\in D_0$, we utilize Gemini-2.5-Pro (Comanici et al., 2025) to generate $K$ independent reasoning processes $\hat T^s_{i,k}$ and corresponding answers $\hat A^s_{i,k}$. We then compute the reward $r^s_{i,k}=Reward(\hat A^s_{i,k},A^s_i)$ for each reasoning-answer pair, where $Reward(\cdot,\cdot)$ is the reward function described in Sec. 4.3. Consequently, we obtain a set of outputs $O^s_i=\{\langle\hat T^s_{i,k},\hat A^s_{i,k},r^s_{i,k}\rangle\}_{k=1}^{K}$ for each $I^s_i\in D_0$.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **多路径 CoT 生成。** 对于每个样本 $I^s_i\in D_0$，我们使用 Gemini-2.5-Pro（Comanici et al., 2025）生成 $K$ 个独立推理过程 $\hat T^s_{i,k}$ 及对应答案 $\hat A^s_{i,k}$。随后为每个推理-答案对计算奖励 $r^s_{i,k}=Reward(\hat A^s_{i,k},A^s_i)$，其中 $Reward(\cdot,\cdot)$ 是第 4.3 节描述的奖励函数。因此，对于每个 $I^s_i\in D_0$，我们得到输出集合 $O^s_i=\{\langle\hat T^s_{i,k},\hat A^s_{i,k},r^s_{i,k}\rangle\}_{k=1}^{K}$。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Scenario-specific Filtering.** Since the generative quality of Gemini-2.5-Pro (Comanici et al., 2025) may vary across different data distributions, applying a global reward threshold can lead to an imbalance across scenarios. To mitigate this, we adopt a scenario-specific filtering strategy. For each sample $I^s_i\in D_0$, we first identify the output with the highest reward, denoted as $\hat r^s_i=\max_k r^s_{i,k}$. We then compute a scenario-dependent threshold $\tau_s$ by averaging the maximum rewards within each scenario:

$$\tau_s=\frac{1}{N}\sum_{i=1}^{N}\hat r^s_i,\quad s\in\{1,\ldots,7\}. \tag{9}$$

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **场景特定过滤。** 由于 Gemini-2.5-Pro（Comanici et al., 2025）的生成质量可能随数据分布而变化，应用全局奖励阈值可能导致场景之间不平衡。为减轻这一问题，我们采用场景特定过滤策略。对于每个样本 $I^s_i\in D_0$，首先找出奖励最高的输出，记为 $\hat r^s_i=\max_k r^s_{i,k}$。随后通过对每个场景内的最高奖励取平均，计算场景相关阈值：$\tau_s=\frac{1}{N}\sum_{i=1}^{N}\hat r^s_i$，其中 $s\in\{1,\ldots,7\}$。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> An item $I^s_i$ is preserved in the final cold-start set if and only if $\hat r^s_i\ge\tau_s$. This strategy ensures that the model learns from the top-performing generations relative to each scenario’s complexity, maintaining a balanced representation of all 7 scenarios in the reasoning dataset. This rule preserves approximately the top 50% of generations per question type while discarding degenerate (zero-reward) outputs. In practice, we set $N=2000$ and $K=3$, and finally, we get 7000 samples in the cold start set. We provide a pseudocode for this process in Algorithm 1.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 当且仅当 $\hat r^s_i\ge\tau_s$ 时，样本 $I^s_i$ 才会保留在最终冷启动集合中。该策略确保模型学习相对于各场景复杂度表现最佳的生成结果，并在推理数据集中保持全部 7 个场景的平衡表示。该规则保留每种问题类型约前 50% 的生成结果，同时丢弃退化（零奖励）输出。实践中设 $N=2000$、$K=3$，最终得到冷启动集合中的 7000 个样本。该过程的伪代码见算法 1。

### Algorithm 1 / 算法 1

**Scenario-Adaptive Cold-Start Construction / 场景自适应冷启动构建**

```text
1: Input: Initial subset D0 = ⋃s=1^7 Ds, Model M, Reward function R(·)
2: Output: Filtered cold-start dataset Dcold
3: Dcold ← ∅
4: for each scenario s ∈ {1, …, 7} do
5:   {Step 1: Multi-path Generation}
6:   for each sample Isi ∈ Ds do
7:     Get K paths: {⟨T̂si,k, Âis,k, ris,k⟩}k=1K using M
8:   end for
9:   {Step 2: Scenario-specific Filtering}
10:  Compute scenario mean reward as threshold:
    τs ← (1/N) Σi=1N r̂is = (1/N) Σi=1N arg maxk ris,k
11:  for each sample i and path k in scenario s do
12:    if ris,k ≥ τs and ris,k > 0 then
13:      Dcold ← Dcold ∪ {⟨Isi, T̂si,k, Âis,k⟩}
14:    end if
15:  end for
16: end for
17: Return: Dcold
```

> **Source anchor:** PDF p. 14. The displayed algorithm preserves the source’s variable names and loop structure; superscripts/subscripts are normalized for Markdown readability.

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Other Details.** Figure 10 presents the prompts used in the SFT, Cold Start, and GRPO stages. For the SFT stage, we adopt the default system prompt of Qwen3-VL (Bai et al., 2025a), namely, “You are a helpful assistant.” In the Cold Start and GRPO stage, we use specially designed system prompts to guide the model’s output of 4D information.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **其他细节。** 图 10 展示 SFT、Cold Start 和 GRPO 阶段所使用的提示。在 SFT 阶段，我们采用 Qwen3-VL（Bai et al., 2025a）的默认系统提示，即 “You are a helpful assistant.” 在 Cold Start 和 GRPO 阶段，我们使用专门设计的系统提示来引导模型输出 4D 信息。

## 8.4. Details of data curation pipeline based on monocular videos / 基于单目视频的数据整理流水线细节

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We also implement an alternative pipeline based on monocular videos, as shown in Fig. 9. First, we employ Gemini-2.5-flash, to identify all moving entities and extract their corresponding noun categories. We then utilize GroundedSAM2 for instance segmentation and tracking, yielding temporally consistent 2D masks across the sequence. These semantic descriptions are further enriched using PixelRefer. We sample pixels in each region and apply a 4D tracking method, such as SpatialTrackerV2 (Xiao et al., 2025) to track points in 4D space. Since 4D tracking method typically produces depth at a relative-scale, we incorporate a metric-scale depth estimation method, such as MoGe-2 (Wang et al., 2025c), to align the final per-frame object-level points. This monocular-based pipeline often faces challenges with depth ambiguity and diminished spatial accuracy inherent in 4D tracking and monocular depth estimation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 如图 9 所示，我们还实现了一条基于单目视频的替代流水线。首先使用 Gemini-2.5-flash 识别所有运动实体并提取其对应名词类别；然后使用 GroundedSAM2 进行实例分割和跟踪，得到序列中时间一致的 2D 掩码；再使用 PixelRefer 丰富这些语义描述。我们在每个区域采样像素，并应用 SpatialTrackerV2（Xiao et al., 2025）等 4D 跟踪方法在 4D 空间中跟踪点。由于 4D 跟踪方法通常产生相对尺度的深度，我们加入 MoGe-2（Wang et al., 2025c）等度量尺度深度估计方法，以对齐最终逐帧物体级点。这条基于单目的流水线往往面临 4D 跟踪和单目深度估计固有的深度歧义与空间精度降低问题。

## 8.5. Limitations and Future Work / 局限性与未来工作

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Although MLLM-4D demonstrates strong visual-based spatial-temporal intelligence compared to existing MLLMs across various 4D reasoning tasks, it still faces constraints in processing long-duration video sequences. Due to the inherent input length limitations of current architectures, our model relies on frame sampling. A compelling direction for the future work would lie in exploring long-context 4D spatiotemporal reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 尽管与现有 MLLM 相比，MLLM-4D 在各种 4D 推理任务中展现出较强的基于视觉的时空智能，但它在处理长时段视频序列方面仍受到限制。由于当前架构固有的输入长度限制，我们的模型依赖帧采样。未来一个有吸引力的方向是探索长上下文 4D 时空推理。

# Figures 6–17 / 图 6–17

The following figure captions and the source-native prompt/demo literals are retained in source order. The figures are located on PDF pp. 13–21; the prompt text is transcribed below so that the exact constraints remain searchable.

## Figure 6 / 图 6

**Caption:** Illustration of the prompt used to identify all moving entities and extract their corresponding noun categories.

**Caption[CN]:** 用于识别所有运动实体并提取其对应名词类别的提示示意图。

```text
User Prompt:
You are a specialized video entity recognizer. Your role is to accurately identify and compile "active" entities from the video. An "active" entity is any visible object that shows dynamic behaviors, such as movement, action, or interaction with other objects. Ignore background elements and any inactive entities.

⚠ Output Requirement:
1. Every entity must include a description.
3. Return the results strictly in format as follows:
{
  "active": [
    {
      "en": "entity name (e.g., man)",
      "cat": "broad category (e.g., person, vehicle, animal, or other appropriate category)",
    },
    {
      "en": "entity name (e.g., gril)",
      "cat": "broad category (e.g., person, vehicle, animal, or other appropriate category)",
    }
  ]
}
```

> **Literal note / 字面量说明：** The source figure visibly numbers the output requirements “1.” and “3.” and contains the example literal “gril”; both are retained exactly rather than silently corrected.

## Figure 7 / 图 7

**Caption:** The components of our MLLM4D-2M.

**Caption[CN]:** 我们的 MLLM4D-2M 的组成部分。

| Category | Subtask | Share shown |
|---|---|---:|
| Inde. Obj Motion | Object absolute distance | 14.3% |
| Camera Ego-Motion | Camera absolute distance; Camera relative direction | 28.6%; 14.3% + 14.3% |
| Obj-Cam Dynamics | Object-Camera absolute distance; Object-Camera relative distance; Object-Camera relative direction | 57.1%; 14.3% + 14.3% + 28.5% |

> **Source anchor:** PDF p. 13; the source visualization displays the rounded category shares.

## Figure 8 / 图 8

**Caption:** The components of our MLLM4D-R1-30k.

**Caption[CN]:** 我们的 MLLM4D-R1-30k 的组成部分。

| Category | Subtask | Share shown |
|---|---|---:|
| Inde. Obj Motion | Object absolute distance | 20.0% |
| Camera Ego-Motion | Camera absolute distance; Camera relative direction | 35.9%; 19.2% + 16.7% |
| Obj-Cam Dynamics | Object-Camera absolute distance; Object-Camera relative distance; Object-Camera relative direction | 44.1%; 19.2% + 16.7% + 8.3% |

> **Source anchor:** PDF p. 14; the source visualization displays the rounded category shares.

## Figure 9 / 图 9

**Caption:** An alternative data pipeline based on monocular videos.

**Caption[CN]:** 基于单目视频的替代数据流水线。

> **Source anchor:** PDF p. 14. The pipeline labels are preserved: Monocular Videos; Gemini; SAM2; Grounded; Object Noun; SpatialTrackerV2; 4D Tracking; MoGe-2; Metric Depth Estimation; PixelRefer; Instance-level Caption; Meta Data; Per-frame Object 3D points, camera poses, descriptions.

## Figure 10 / 图 10

**Caption:** Detailed system prompt and user prompt setting for our SFT, Cold Start and GRPO stage.

**Caption[CN]:** 我们的 SFT、Cold Start 和 GRPO 阶段的详细系统提示与用户提示设置。

```text
Question Example:
Question: "What is the approximate distance (in meters) between the camera (or the observer filming) in frame 14 and the nearest point of the A dolphin with a streamlined body, a prominent dorsal fin, and a tail fluke, swimming in water in frame 15 of 31?\nOptions:\nA. 2.5\nB. 12.7\nC. 15.2\nD. 9.6"

SFT Stage
System Prompt:
"You are a helpful assistant."
User Prompt:
"{Video Frames}+<video>These are frames of a video.\n"+{Question}+ "\nAnswer with the option's letter from the given choices directly."

Cold Start & GRPO Stage
System Prompt:
"You are a video analysis assistant. Your goal is to solve the user's question by performing a detailed spatial-temporal analysis of the video content. The response must follow a strict structure:
1. **Reasoning Process**: Enclosed within <thinking></thinking> tags.
2. **Final Answer**: Enclosed within <answer></answer> tags.
3. **Internal Reasoning Requirements:** Inside the <thinking> tags, you must explicitly document your perception of the physical state at the start and the end of the relevant video segment. Use the following structured format for Spatial State:
**Spatial State (Initial Frame):**
- Camera Center: [x, y, z] or null
- Object Center: [x, y, z] or null
**Spatial State (Final Frame):**
- Camera Center: [x, y, z] or null
- Object Center: [x, y, z] or null
If any specific value is unavailable or cannot be inferred, output `null`. Ensure the reasoning leads logically from these physical states to the final answer."
User Prompt:
"{Video Frames}+<video>\n"+{Question}+"\nOutput the thinking process in <thinking></thinking> and \n final answer in <answer></answer> tags."
```

## Figure 11 / 图 11

**Caption:** Detailed structure of the Spatiotemporal Chain of Thought (ST-CoT) Generation Prompt. The prompt is color-coded into four functional modules: ■ System Role & Task defines the AI persona and core mission; ■ Input Data & Mandatory Rules enforces visual-driven reasoning and constraints; ■ CoT Structure provides the step-by-step requirements for the reasoning chain; ■ Output Format specifies the data placeholders and JSON schema.

**Caption[CN]:** 时空思维链（ST-CoT）生成提示的详细结构。该提示以颜色编码分为四个功能模块：■ System Role & Task 定义 AI 角色和核心任务；■ Input Data & Mandatory Rules 强制视觉驱动的推理与约束；■ CoT Structure 提供推理链的分步要求；■ Output Format 指定数据占位符和 JSON 模式。

```text
"""
You are a high-performance Spatio-Temporal AI. You are currently processing a video stream and your internal 3D perception engine is active.
## TASK
Analyze the visual movement in the video to answer the Question. Your output must be a Chain of Thought (CoT) that prioritizes **visual narrative**. You must derive the answer solely from **observable evidence** in the video frames.
## INPUT DATA (FOR INTERNAL SENSOR REFERENCE)
1. **Question**: [QUESTION_PLACEHOLDER]
2. **Options**: [OPTIONS_PLACEHOLDER]
3. **Internal Target**: [GROUND_TRUTH_PLACEHOLDER]
4. **Sensor Log**: [PHYSICS_DATA_PLACEHOLDER]
*(Note: This log contains raw Camera Center and Object Center. If solving this problem does not require some data, they are set 'null')*
## MANDATORY RULES
1. **Strict "Spatial State" Formatting**: You must provide a snapshot of your perception at the beginning and the end. If a value is missing, output `null`.
**Spatial State (Frame X):**
- Camera Center: [x, y, z] or null
- Object Center: [x, y, z] or null
2. **Visual-Driven Reasoning (No Math in Text)**:
* **PROHIBITED**: "Because the X-coordinate changed...", "Based on the provided sensor log...".
* **REQUIRED**: Use optical flow cues. (e.g., "The target object expands in the field of view, indicating a decrease in relative distance," or "The parallactic shift of the background suggests the camera is translating right.")
3. **Evidence-Based Conclusion (NO GUESSING)**:
* When stating the final answer, you must justify it by summarizing the **visual trajectory**.
* **DO NOT** simply state the answer. You must say: "Given that we observed [specific visual event] during the sequence, the only plausible value among the options is [Answer]."
## COT STRUCTURE REQUIREMENT
- **Step 1: Objective**: Define the goal.
- **Step 2: Start Frame Perception**: Describe the initial visual scene and initial position. Follow with **Spatial State**.
- **Step 3: Temporal progression & Evidence Collection**: This is the most important part. Describe the sequence of movement.
- *Example*: "From Frame 16 to 20, the entity's feet are seen moving in a walking gait, and its silhouette becomes larger against the static doorframe, confirming positive forward velocity."
- **Step 4: End Frame Perception**: Describe the final visual state. Follow with **Spatial State**.
- **Step 5: Final Synthesis & Verification**: Summarize the **total visual change** and explain why it leads to the chosen option. Select the option that best fits the visual evidence.
## OUTPUT FORMAT (JSON ONLY)
```json
{
  "chain_of_thought": "The objective is to... \\n\\nIn Frame [Start], visually, we see... [Initial Evidence].\\n**Spatial State (Frame [Start]):**\\n- Object Center: [ ... ]\\n- Camera Center: [ ... ]\\n\\nAnalyzing the temporal flow, the visual evidence shows [Specific Evidence 1] followed by [Specific Evidence 2]. We see the distance gap closing because [Visual Clue]...\\n\\nBy Frame [End], the visual evidence confirms [Final State]...\\n**Spatial State (Frame [End]):**\\n- Object Center: [ ... ]\\n- Camera Center: [ ... ]\\n\\nSynthesizing the motion trajectory: the [Object] moved [Direction/Relative Distance] while the Camera [Ego-motion]. This visual progression directly supports the choice of [Answer] as the most accurate estimation."
}
```
"""
```

## Figures 12–17 / 图 12–17: Qualitative comparison records

The following records preserve the source questions, choices, model answers, and the substantive qualitative outputs shown in the PDF. The associated rendered panels occupy PDF pp. 16–21.

### Figure 12 / 图 12

**Caption:** Qualitative comparison on MLLM4D-Bench.

**Caption[CN]:** MLLM4D-Bench 上的定性比较。

**Question:** “Approximately how far (in meters) did the camera move between frame 0 and frame 26 of 31? Options: A. 1.2 B. 0.4 C. 0.8 D. 1.6?” **Right Answer: A.**

- **MLLM-4D:** The visual trajectory describes continuous forward translation: foreground steps and the fence expand, background elements recede, and the final estimate is **1.2 meters**, `<answer>A</answer>`.
- **VG-LLM:** Estimates the observed spacing as **0.8 meters**, `<answer>0.8</answer>`.
- **Qwen3-VL:** Considers 1.2 plausible but selects **C. 0.8**, citing slow movement.

### Figure 13 / 图 13

**Caption:** Qualitative comparison on MLLM4D-Bench.

**Caption[CN]:** MLLM4D-Bench 上的定性比较。

**Question:** “Approximately how far (in meters) did the woman in the red jacket and black pants move between frame 14 and frame 29 of 31? Options: A. 1.7 meters B. 1.0 meters C. 0.4 meters D. 1.3 meters.” **Right Answer: D.**

- **MLLM-4D:** The woman moves right-to-left, becomes smaller, and largely exits the frame; the estimate is **1.3 meters**, `<answer>D</answer>`.
- **VG-LLM:** Selects **A. 1.7**.
- **Qwen3-VL:** Estimates approximately 0.75–1.0 meters and selects **B. 1.0**.

### Figure 14 / 图 14

**Caption:** Qualitative comparison on MLLM4D-Bench.

**Caption[CN]:** MLLM4D-Bench 上的定性比较。

**Question:** “What is the approximate distance (in meters) between the camera (or the observer filming) in frame 4 and the nearest point of the girl wearing a white dress in frame 21 of 31? Options: A. 4.1 B. 5.4 C. 8.9 D. 6.8.” **Right Answer: B.**

- **MLLM-4D:** The camera remains stable; the performer maintains size and position on the stage; the estimate is **5.4**, `<answer>B</answer>`.
- **VG-LLM:** Estimates **4.1 meters**, `<answer>A</answer>`.
- **Qwen3-VL:** Estimates **6.8 meters**, `<answer>D. 6.8</answer>`.

### Figure 15 / 图 15

**Caption:** Qualitative comparison on VLM4D benchmark.

**Caption[CN]:** VLM4D 基准上的定性比较。

**Question:** “Is the swan spinning clockwise or counter-clockwise? A: counter-clockwise B: both ways C: clockwise D: not spinning.” **Right Answer: D.**

- **MLLM-4D:** The swan’s head, neck, body, and feather profile retain a stable orientation; no rotation is visible, so it selects **D. not spinning**.
- **VG-LLM:** Selects **B**, saying the motion does not specify clockwise or counter-clockwise.
- **Qwen3-VL:** Describes a slight clockwise turn and selects **C**.

### Figure 16 / 图 16

**Caption:** Qualitative comparison on VLM4D benchmark.

**Caption[CN]:** VLM4D 基准上的定性比较。

**Question:** “From the camera perspective, what direction is the boy moving towards? A: left B: not moving C: right D: towards the camera.” **Right Answer: A in the source panel’s MLLM-4D response.**

- **MLLM-4D:** Tracks a boy on a bicycle approaching the camera’s original viewpoint and outputs `<answer>A</answer>`.
- **VG-LLM:** Says right and outputs **C**.
- **Qwen3-VL:** Says right/away from the initial camera position and outputs **C**.

> **Caveat:** The PDF panel’s prose says “towards the camera” while the printed right-answer marker is A; this apparent label/prose inconsistency is preserved rather than silently resolved.

### Figure 17 / 图 17

**Caption:** Qualitative comparison on VLM4D benchmark.

**Caption[CN]:** VLM4D 基准上的定性比较。

> <span style="color:#3B82F6"><strong>Para. F17.1:</strong></span> **Question:** What direction is the person holding the girl moving towards? **Options:** A: left; B: not moving; C: staying in place; D: right. **Right Answer: C.**

> <span style="color:#F59E0B"><strong>Para. F17.1[CN]:</strong></span> **问题：** 抱着女孩的人正朝哪个方向移动？**选项：**A：向左；B：不动；C：停留在原地；D：向右。**正确答案：C。**

> <span style="color:#3B82F6"><strong>Para. F17.2:</strong></span> **MLLM-4D:** "<thinking>The objective is to determine the direction of movement of the person holding the girl during the sequence. In the initial frame, we observe the person holding the girl positioned towards the left side of the performance area. The girl is balanced on the person's shoulders, and their combined figure is relatively static against the background of the circus tent. **Spatial State (Frame 0.000):** - Object Center: [-0.2448, 0.2527, 3.5453] - Camera Center: [-0.0293, -0.0022, 0.0011] Analyzing the temporal flow, the visual evidence shows that the person holding the girl maintains a remarkably consistent position throughout the sequence. There is no discernible lateral shift of their overall body mass across the stage. Their feet remain planted in a similar spot on the blue and red mat, and their upper body orientation relative to the stage and the background elements, such as the distant audience and the circus props, does not change significantly. While the girl performs a slight adjustment in her posture, the base person holding her exhibits no noticeable translation or rotation that would indicate movement in any cardinal direction. By the final frame, the visual evidence confirms that the person holding the girl is still in a nearly identical spatial location as observed at the beginning. The background elements appear static, and the person's silhouette occupies the same general area of the stage. **Spatial State (Frame 2.999):** - Object Center: [-0.2426, 0.2452, 3.5385] - Camera Center: [-0.0293, -0.0022, 0.0011] Synthesizing the motion trajectory: the person holding the girl demonstrates a lack of significant translational movement across the stage. Their position remains largely fixed, with no observable drift to the left, right, or forward/backward. This visual progression directly supports the choice of "staying in place" as the most accurate estimation.</thinking><answer>C</answer>"

> <span style="color:#F59E0B"><strong>Para. F17.2[CN]:</strong></span> **MLLM-4D：** “<thinking>本段序列的目标是确定抱着女孩的人朝哪个方向移动。在初始帧中，我们看到抱着女孩的人位于表演区域的左侧。女孩平衡地坐在这个人的肩膀上，他们组成的整体相对于马戏帐篷背景基本保持静止。**空间状态（帧 0.000）：**- 物体中心：[-0.2448, 0.2527, 3.5453]；- 相机中心：[-0.0293, -0.0022, 0.0011]。分析时间变化可见，抱着女孩的人在整个序列中保持了极其稳定的位置。他们整体身体质量在舞台上没有可辨别的横向位移。双脚始终踩在蓝红相间垫子的相近位置，上半身相对于舞台和背景元素（如远处的观众与马戏道具）的朝向也没有明显变化。虽然女孩略微调整了姿势，但托举她的底部人物没有表现出任何能够指示其朝某个基本方向移动的明显平移或旋转。到最后一帧，视觉证据确认抱着女孩的人仍处于与开始时几乎相同的空间位置。背景元素看起来保持静止，该人物的轮廓仍占据舞台上大致相同的区域。**空间状态（帧 2.999）：**- 物体中心：[-0.2426, 0.2452, 3.5385]；- 相机中心：[-0.0293, -0.0022, 0.0011]。综合运动轨迹可知，抱着女孩的人在舞台上没有显著的平移运动。其位置基本固定，没有可观察到的向左、向右或向前/向后的漂移。这一视觉进程直接支持将“停留在原地”作为最准确的估计。</thinking><answer>C</answer>”

> <span style="color:#3B82F6"><strong>Para. F17.3:</strong></span> **VG-LLM:** "The person holding the girl is moving towards the right side of the frame. The girl is being held above their head and then lowered down. This movement is consistent throughout the video. Therefore, the final answer is: D."

> <span style="color:#F59E0B"><strong>Para. F17.3[CN]:</strong></span> **VG-LLM：**“抱着女孩的人正朝画面右侧移动。女孩先被举过头顶，随后被放低。这一运动在整个视频中保持一致。因此，最终答案是：D。”

> <span style="color:#3B82F6"><strong>Para. F17.4:</strong></span> **Qwen3-VL:** "Step 1: Observe the person holding the girl in the video frames. In the initial frames, the person holding the girl is standing still, holding her up. Step 2: As the video progresses, the person holding the girl begins to move. Specifically, they start to move to the right side of the frame, as seen from 0:02 to 0:03. Step 3: The movement is clear and consistent towards the right side of the stage. Step 4: Therefore, the person holding the girl is moving towards the right. Therefore, the final answer is: D."

> <span style="color:#F59E0B"><strong>Para. F17.4[CN]:</strong></span> **Qwen3-VL：**“步骤 1：观察视频帧中抱着女孩的人。在初始帧中，抱着女孩的人站立不动，将她托举起来。步骤 2：随着视频推进，抱着女孩的人开始移动。具体而言，从 0:02 到 0:03 可以看到他们开始向画面右侧移动。步骤 3：这一运动清晰且持续地朝舞台右侧进行。步骤 4：因此，抱着女孩的人正向右移动。因此，最终答案是：D。”

> **Source anchor:** PDF p. 21. Figure 17 is the final physical page’s qualitative comparison; the question, answer choices, right-answer marker, and all three model-output records shown in the panel are transcribed above.

---

## Translation notes / 翻译备注

- The source was a 21-page PDF. Text was recovered from the local Zotero full-text cache and checked against rendered PDF page images available through the PDF reader, especially the first page, section transitions, table pages, appendix boundaries, prompt pages, and final pages (physical pp. 19–21).
- Mathematical notation from the PDF’s extracted text was re-typeset in reader-facing Markdown using `$...$` and `$$...$$`. OCR/extraction had split summation limits, superscripts, subscripts, and equation layout; symbols were normalized only where the surrounding PDF equation made the intended notation clear.
- The PDF’s figure panels contain dense raster text and qualitative examples. Their captions, source anchors, prompts, questions, answer choices, model-answer summaries, and all visible exact prompt literals needed for the method are retained here. No unsupported numeric values were added to figure panels.
- Reference entries remain in English bibliographic form by design. One source figure visibly contains the literal “gril” and skips output requirement number 2; those literals are preserved and called out rather than corrected.
- Figure 16 contains an apparent inconsistency between the answer-letter marker/prose and the option text; the inconsistency is explicitly retained in the reader.
- Asset limitation: the PDF reader exposed the source pages for visual inspection but did not permit raster crop export in this environment. Consequently, no invented or misleading image crops are linked. Substantive tables are transcribed in searchable Markdown, and every figure has a bilingual caption plus a PDF-page anchor.
- Coverage: PDF pp. 1–21, including abstract, sections 1–7, references, appendix sections 8.1–8.5, Algorithm 1, Figures 1–17, Tables 1–3, prompt/code blocks, qualitative comparisons, limitations, and exact numerical/model literals.
