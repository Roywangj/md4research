# Reasoning in the Dark: Interleaved Vision-Text Reasoning in Latent Space

> **中文题名：** 暗中推理：潜在空间中的交错视觉—文本推理  
> **作者：** Chao Chen, Zhixin Ma, Yongqi Li, Yupeng Hu, Yinwei Wei, Wenjie Li, Liqiang Nie  
> **单位：** The Hong Kong Polytechnic University; Singapore Management University; Shandong University; Harbin Institute of Technology (Shenzhen)  
> **通讯作者：** Yongqi Li  
> **联系邮箱：** ochenchaoo@outlook.com; liyongqi0@gmail.com  
> **来源：** arXiv:2510.12603v2 [cs.CV], 28 January 2026; PDF header dated 2026-1-29  
> **项目主页：** https://github.com/ModalityDance/IVT-LR  
> **权威文本：** 12-page arXiv v2 PDF supplied by the user  
> **阅读器范围：** Complete paragraph-level English–Chinese bilingual reader; figures, tables, algorithm, references, and Appendix A included.

## Page / Section Index

| PDF pages | Content |
|---|---|
| 1 | Metadata, Abstract, Section 1 Introduction begins |
| 2 | Section 1 Introduction; Figure 1; Section 2 Related Work begins |
| 3 | Sections 2.1–2.2; Section 3 Method begins |
| 4 | Figure 2; Section 3.1; Section 3.2 begins |
| 5 | Figure 3; Algorithm 1; Sections 3.2–3.3 |
| 6 | Table 1; Section 3.3 concludes; Sections 4.1–4.2 begin |
| 7 | Section 4.2; Table 2; Sections 4.3–4.4 begin |
| 8 | Figure 4; Table 3; Section 4.4 and Equations (1)–(2) |
| 9 | Figure 5; Section 4.4 concludes; Section 5 Conclusion; References begin |
| 10 | References [6]–[27] |
| 11 | References [27]–[31]; Appendix A.1 and A.2 begin |
| 12 | Figure 6; Tables 4–5 |

## Terminology Ledger

| Canonical term / literal | 中文译法 | Consistency decision |
|---|---|---|
| Interleaved Vision-Text Latent Reasoning (IVT-LR) | 交错视觉—文本潜在推理 | 首次保留全称与缩写，后文保留 IVT-LR |
| multimodal latent reasoning | 多模态潜在推理 | 指视觉与文本信息在潜在空间中的联合推理 |
| latent text | 潜在文本 | 指前一步的隐藏状态；保留变量名不译 |
| latent vision | 潜在视觉 | 指按注意力选择的图像嵌入；保留变量名不译 |
| explicit reasoning | 显式推理 | 指生成可见中间推理步骤的过程 |
| reasoning trajectory | 推理轨迹 | 与 rationale（推理依据）区分 |
| autoregressive step / # AR Steps | 自回归步 / 自回归步数 | 表格中的 `# AR Steps` 原样保留 |
| Attention Ratio | 注意力比率 | 视觉部分相对于文本部分的注意力分配比率 |
| Attention Focus | 注意力集中度 | 以逆熵衡量；变量 $F$ 原样保留 |
| progressive multi-stage training | 渐进式多阶段训练 | 按阶段逐步用潜在步骤替换显式步骤 |
| `<latent>`, `<pause>`, `<plan>` | 原样保留 | 方法中的特殊标记不翻译 |
| M3CoT, ScienceQA, Qwen2-VL-7B, Chameleon-7B | 原样保留 | 数据集和模型名称不翻译 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Multimodal reasoning aims to enhance the capabilities of MLLMs by incorporating intermediate reasoning steps before reaching the final answer. It has evolved from text-only reasoning to the integration of visual information, enabling the thought process to be conveyed through both images and text. Despite its effectiveness, current multimodal reasoning methods depend on explicit reasoning steps that require labor-intensive vision-text annotations and inherently introduce significant inference latency. To address these issues, we introduce multimodal latent reasoning with the advantages of multimodal representation, reduced annotation, and inference efficiency. To facilitate it, we propose Interleaved Vision-Text Latent Reasoning (IVT-LR), which injects both visual and textual information in the reasoning process within the latent space. Specifically, IVT-LR represents each reasoning step by combining two implicit parts: latent text (the hidden states from the previous step) and latent vision (a set of selected image embeddings). We further introduce a progressive multi-stage training strategy to enable MLLMs to perform the above multimodal latent reasoning steps. Experiments on M3CoT and ScienceQA demonstrate that our IVT-LR method achieves an average performance increase of 5.45% in accuracy, while simultaneously achieving a speed increase of over 5 times compared to existing approaches.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 多模态推理旨在通过在得出最终答案之前加入中间推理步骤，增强多模态大语言模型（MLLM）的能力。它已经从纯文本推理发展到整合视觉信息，使思考过程能够同时通过图像和文本来表达。尽管这种方法有效，当前的多模态推理方法仍依赖显式推理步骤；这些步骤需要劳动密集型的视觉—文本标注，并且天然会带来显著的推理时延。为解决这些问题，我们引入多模态潜在推理，使其兼具多模态表征、减少标注和高推理效率等优势。为实现这一点，我们提出交错视觉—文本潜在推理（Interleaved Vision-Text Latent Reasoning, IVT-LR），在潜在空间内的推理过程中同时注入视觉与文本信息。具体而言，IVT-LR 将每个推理步骤表示为两个隐式部分的组合：潜在文本（前一步的隐藏状态）和潜在视觉（一组选定的图像嵌入）。我们还提出一种渐进式多阶段训练策略，使 MLLM 能够执行上述多模态潜在推理步骤。在 M3CoT 和 ScienceQA 上的实验表明，我们的 IVT-LR 方法在准确率上平均提升 5.45%，同时相较现有方法实现了超过 5 倍的速度提升。

## 1 Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Over the past few years, the capabilities of large language models (LLMs) have been further unlocked through advancements in reasoning. Researchers have sought to enhance the reasoning abilities of LLMs, initially through prompting techniques such as Chain-of-Thought prompting [1], and more recently by developing large reasoning models using reinforcement learning, like GPT-4o [2] and Deepseek-R1 [3]. Building on the success of reasoning in LLMs, there has been growing interest in the research community to extend these reasoning capabilities to multimodal LLMs (MLLMs). This has brought the promising topic of multimodal reasoning, aiming to improve the performance of models on multimodal tasks, such as VQA, through reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在过去几年中，推理技术的进步进一步释放了大语言模型（LLM）的能力。研究人员一直致力于增强 LLM 的推理能力：最初采用思维链提示（Chain-of-Thought prompting）[1] 等提示技术，近来则通过强化学习开发 GPT-4o [2] 和 Deepseek-R1 [3] 等大型推理模型。在 LLM 推理取得成功的基础上，研究界日益关注如何将这些推理能力扩展到多模态大语言模型（MLLM）。由此产生了前景广阔的多模态推理议题，其目标是通过推理提高模型在 VQA 等多模态任务上的表现。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Current multimodal reasoning approaches can be broadly categorized into the following progressive steps: 1) Text-only reasoning. Early multimodal reasoning methods primarily focused on pure text-based reasoning, where MLLMs perform textual reasoning before generating the final answer. These approaches [4, 5] could seamlessly apply LLMs methodologies to MLLMs. 2) Vision-text involved reasoning. Some studies [6, 7, 8] highlight that the intermediate reasoning steps also require the involvement of visual information. For instance, Gao et al. [9] enhances reasoning by generating sequential steps that interleave visual information with textual rationales via selected image patches. In a related direction, Zheng et al. [10] trains models through end-to-end reinforcement learning to autonomously zoom in on image regions for fine-grained visual inspection during the reasoning process. Alternatively, Li et al. [11] enables MLLMs to actively “think visually” by generating explicit image visualizations of their reasoning traces, thereby significantly enhancing performance on complex spatial reasoning tasks.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 当前的多模态推理方法大致可以归纳为以下递进步骤：1）纯文本推理。早期的多模态推理方法主要关注纯文本推理，即 MLLM 在生成最终答案之前先进行文本推理。这些方法 [4, 5] 可以将 LLM 的方法体系无缝应用于 MLLM。2）视觉—文本参与的推理。一些研究 [6, 7, 8] 强调，中间推理步骤同样需要视觉信息参与。例如，Gao 等人 [9] 通过生成连续步骤来增强推理，其中利用选定的图像 patch 将视觉信息与文本推理依据交错起来。沿着相关方向，Zheng 等人 [10] 通过端到端强化学习训练模型，使其在推理过程中自主放大图像区域，以进行细粒度视觉检查。作为另一种方案，Li 等人 [11] 让 MLLM 通过生成其推理轨迹的显式图像可视化来主动“进行视觉思考”，从而显著提升复杂空间推理任务上的表现。

### Figure 1. Interleaved vision-text latent reasoning / 交错视觉—文本潜在推理

![Figure 1](Reasoning/Train/Reasoning%20in%20the%20Dark%20Interleaved%20Vision-Text%20Reasoning%20in%20Latent%20Space/assets/page_002_fig_figure_1.png)

**Caption:** An example of interleaved vision-text latent reasoning, where the intermediate reasoning steps are carried out entirely within the multimodal latent space.

**Caption[CN]:** 交错视觉—文本潜在推理的一个示例，其中中间推理步骤完全在多模态潜在空间内执行。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Recently, latent reasoning has emerged as a new paradigm in LLMs, which eliminates the need for explicit and lengthy textual reasoning by leveraging implicit latent vectors [12]. Inspired by this, we believe that latent reasoning holds even greater potential for facilitating vision-text interleaved intermediate reasoning steps due to the following reasons: 1) Multimodal representation potential. Latent reasoning enables the reasoning process to occur entirely within a hidden space, offering a greater capacity to represent rich, multimodal information during reasoning. 2) Reduced Annotation. Introducing latent reasoning will lessen reliance on heavily annotated vision-text interleaved reasoning data, as reasoning steps no longer need to be fully observable or linguistically aligned. 3) Inference efficiency. By avoiding long chains of explicit multimodal representation in the reasoning step, it will significantly improve efficiency.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 近来，潜在推理已成为 LLM 中一种新的范式；它通过利用隐式潜在向量，消除了对显式且冗长的文本推理的需求 [12]。受此启发，我们认为，潜在推理在促进视觉—文本交错的中间推理步骤方面潜力更大，原因如下：1）多模态表征潜力。潜在推理使推理过程能够完全发生在隐藏空间中，因而在推理期间具有更强的能力来表征丰富的多模态信息。2）减少标注。引入潜在推理将减少对重度标注的视觉—文本交错推理数据的依赖，因为推理步骤不再需要完全可观察或在语言上对齐。3）推理效率。通过避免推理步骤中冗长的显式多模态表征链，它将显著提高效率。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> In this work, we propose the Interleaved Vision-Text Latent Reasoning (IVT-LR) method, which enables both textual and visual modalities to perform reasoning entirely in latent space. As shown in Figure 1, in our framework, each latent reasoning step consists of two parts: latent text and latent vision. At each reasoning step, we use the hidden state from the previous step to replace explicit text as the latent text component. Afterwards, for latent vision part, a certain number of image embeddings are selected based on their attention scores then concatenated with the hidden state to serve as input for the subsequent reasoning step. To effectively blend the latent text and latent vision components for joint reasoning in the latent space, we introduce a progressive, multi-stage training strategy that gradually substitutes explicit CoT steps with latent reasoning steps, where supervision is focused on the remaining future steps and the final answer to ensure accurate inference.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在本工作中，我们提出交错视觉—文本潜在推理（IVT-LR）方法，使文本模态和视觉模态都能完全在潜在空间中进行推理。如图 1 所示，在我们的框架中，每个潜在推理步骤由两部分组成：潜在文本和潜在视觉。在每个推理步骤中，我们用前一步的隐藏状态代替显式文本，将其作为潜在文本部分。随后，对于潜在视觉部分，根据注意力分数选择一定数量的图像嵌入，再将其与隐藏状态拼接，作为后续推理步骤的输入。为了有效融合潜在文本与潜在视觉部分并在潜在空间中进行联合推理，我们引入一种渐进式多阶段训练策略，逐渐以潜在推理步骤替代显式 CoT 步骤；监督聚焦于剩余的后续步骤和最终答案，以确保推断准确。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The key contributions are summarized:
>
> - We introduce IVT-LR, the first framework to achieve fully unified multimodal latent reasoning. Unlike prior methods, our approach enables both textual and visual information to be reasoned with in the latent space, eliminating the need for intermediate explicit text or image generation.
> - Our method presents a novel training paradigm that is both data-efficient and computationally efficient, without requiring explicit annotations for intermediate visual reasoning steps. By reasoning in latent space, it also drastically reduces the number of autoregressive steps required for inference.
> - We validate the effectiveness of IVT-LR through extensive experiments on challenging visual question answering benchmarks, including M3COT and ScienceQA, where our model establishes new state-of-the-art performance in accuracy and significantly improves inference efficiency, as measured by fewer autoregressive steps and lower inference latency.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 主要贡献概括如下：
>
> - 我们提出 IVT-LR，这是首个实现完全统一的多模态潜在推理框架。与先前方法不同，我们的方法使文本信息和视觉信息都能够在潜在空间中参与推理，从而不再需要生成显式的中间文本或图像。
> - 我们的方法提出了一种兼具数据效率与计算效率的新训练范式，并且不需要对中间视觉推理步骤进行显式标注。通过在潜在空间中推理，它还大幅减少了推理所需的自回归步数。
> - 我们通过在具有挑战性的视觉问答基准（包括 M3COT 和 ScienceQA）上开展广泛实验，验证了 IVT-LR 的有效性；我们的模型在准确率上建立了新的最先进表现，并以更少的自回归步数和更低的推理时延显著提升了推理效率。

## 2 Related Work

### 2.1 Multimodal Reasoning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Multimodal reasoning focuses on enabling models to reason over information from different modalities to solve complex tasks. Existing approaches can be roughly divided into text-only reasoning and interleaved reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 多模态推理关注使模型能够针对来自不同模态的信息进行推理，以解决复杂任务。现有方法大致可分为纯文本推理和交错推理。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Text-only reasoning.** Early works attempt to convert visual information into text before reasoning, using tools or visual experts to generate textual representations to guide LLMs. Hu et al. [4] first introduced the concept of captions, extracting visual content as textual captions and concatenating them to the input to enhance reasoning. Inspired by this, subsequent works pursued a fine-grained understanding of images to improve textual expressiveness. Zheng et al. [13] generates a rationale that incorporates image information from visual-text inputs, which is then used for reasoning. Other works [14, 5] leverage graph structures to identify entities in images and construct relationships among them, enhancing reasoning based on these inter-entity connections.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **纯文本推理。** 早期工作尝试在推理前将视觉信息转换为文本，利用工具或视觉专家生成文本表征来引导 LLM。Hu 等人 [4] 首先引入 caption 的概念，将视觉内容提取为文本 caption，并将其拼接到输入中以增强推理。受此启发，后续工作追求对图像进行细粒度理解，以提高文本的表达能力。Zheng 等人 [13] 根据视觉—文本输入生成融入图像信息的推理依据，随后用它进行推理。其他工作 [14, 5] 利用图结构识别图像中的实体并构建实体间关系，从而基于这些实体间联系增强推理。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Vision-text involved reasoning.** This line of work emphasizes using images together with text during the rationale generation and reasoning process. Building on the reasoning paradigm of large language models, Zhang et al. [15] first proposed decoupling rationale generation from answer generation in the Vision-Text Reasoning field. Subsequently, Shao et al. [16] annotates key regions of the original image in intermediate steps, training models to focus on image regions relevant to the answer. While some works [9, 17] further extract key image regions progressively during reasoning, combining visual information with textual reasoning to generate the final answer. Moreover, new methods [6, 7] emulate human thought by sketching images during reasoning, focusing on core concepts, structures, and relationships while ignoring redundant details. Other works [11, 8] generate new images during reasoning, combining them with text to improve reasoning in complex scenarios. To completely decouple reasoning from language and amplify the role of images, Xu et al. [18] proposes reasoning solely with newly generated images, achieving substantial improvements in visual navigation tasks.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **视觉—文本参与的推理。** 这一路线强调在推理依据生成与推理过程中同时使用图像和文本。基于大语言模型的推理范式，Zhang 等人 [15] 首次提出在视觉—文本推理领域将推理依据生成与答案生成解耦。随后，Shao 等人 [16] 在中间步骤中标注原始图像的关键区域，训练模型关注与答案相关的图像区域。另一些工作 [9, 17] 则在推理过程中逐步提取关键图像区域，将视觉信息与文本推理结合起来生成最终答案。此外，新方法 [6, 7] 通过在推理期间绘制草图来模拟人类思考，关注核心概念、结构和关系，同时忽略冗余细节。其他工作 [11, 8] 在推理过程中生成新图像，并将它们与文本结合，以改进复杂情景下的推理。为了使推理与语言完全解耦并放大图像的作用，Xu 等人 [18] 提出仅利用新生成的图像进行推理，在视觉导航任务上取得了显著提升。

### 2.2 Latent Reasoning

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Latent reasoning refers to internal, non-linguistic thinking performed in a hidden latent space before generating the final answer. Early methods used special tokens to guide latent reasoning. Goyal et al. [19] introduces learnable `<pause>` tokens, giving the model opportunities to internally update information before generating an answer, while Wang et al. [20] uses `<plan>` tokens to guide reasoning.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 潜在推理是指在生成最终答案之前，于隐藏的潜在空间中进行的内部、非语言思考。早期方法使用特殊标记来引导潜在推理。Goyal 等人 [19] 引入可学习的 `<pause>` 标记，使模型有机会在生成答案前于内部更新信息；Wang 等人 [20] 则使用 `<plan>` 标记引导推理。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Later, some works exploit the model’s continuous hidden states to replace explicit reasoning steps. Hao et al. [12] pioneers continuous latent space reasoning by feeding the last hidden states as input embeddings for the next step without generating intermediate tokens, significantly reducing reasoning tokens and improving efficiency. Inspired by this, subsequent methods improve the quality of intermediate representations. Cheng and Van Durme [21] uses variable-length contemplation tokens for latent reasoning, addressing quality degradation caused by fixed-length embeddings. Shen et al. [22] employs self-distillation to align student and teacher hidden activations under CoT supervision, constraining latent reasoning paths.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 随后，一些工作利用模型的连续隐藏状态来替代显式推理步骤。Hao 等人 [12] 开创了连续潜在空间推理：不生成中间标记，而是将最后的隐藏状态作为下一步的输入嵌入，从而显著减少推理标记并提高效率。受此启发，后续方法进一步改善中间表征的质量。Cheng 和 Van Durme [21] 使用可变长度的思考标记进行潜在推理，以解决固定长度嵌入造成的质量下降。Shen 等人 [22] 采用自蒸馏，在 CoT 监督下对齐学生模型与教师模型的隐藏激活，从而约束潜在推理路径。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> In the multimodal domain, latent reasoning has also been introduced. Unlike traditional LLMs, VLMs emphasize how image features interact with the latent space. Some efforts [23, 24, 25] have been made to integrate visual "thoughts" into the latent space for reasoning. However, these existing works focus solely on single-modal latent reasoning. Combining text and vision for multimodal latent reasoning in the latent space remains unexplored.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 在多模态领域中，潜在推理也已被引入。与传统 LLM 不同，VLM 强调图像特征如何与潜在空间交互。一些工作 [23, 24, 25] 已尝试将视觉“思维”整合进潜在空间以进行推理。然而，这些现有工作只关注单模态潜在推理。在潜在空间中结合文本与视觉来进行多模态潜在推理，仍未得到探索。

## 3 Method

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In this section, we present IVT-LR, the first VLM framework that unifies textual and visual representations in the latent space and implements multimodal latent reasoning. Given a text sequence $X=(x_1,\ldots,x_I)$ and a set of visual embeddings $Z=(z_1,\ldots,z_J)$ from a visual encoder, a standard VLM encodes the text sequence into embeddings, incorporates visual features, and predicts a conditional distribution over the next token:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在本节中，我们介绍 IVT-LR，这是首个在潜在空间中统一文本表征与视觉表征并实现多模态潜在推理的 VLM 框架。给定文本序列 $X=(x_1,\ldots,x_I)$ 和来自视觉编码器的一组视觉嵌入 $Z=(z_1,\ldots,z_J)$，标准 VLM 将文本序列编码为嵌入、融入视觉特征，并预测下一个标记的条件分布：

$$
e^{\mathrm{text}}_{1:t}=g(x_{1:t})\in\mathbb{R}^{t\times d},
$$

$$
e^{\mathrm{fused}}_{t}=f(e^{\mathrm{text}}_{1:t},Z)\in\mathbb{R}^{d},
$$

$$
M(x_{t+1}\mid x_{1:t},Z)=\operatorname{softmax}(W\cdot e^{\mathrm{fused}}_{t}),
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> where $g(\cdot)$ denotes the text embedding function, $f(\cdot)$ is a function that generates the hidden state for the next token based on the textual embeddings and visual fatures, and $W\in\mathbb{R}^{|V|\times d}$ is trained to project the fused representation to a distribution over the vocabulary. This formulation illustrates how a VLM predicts the next token conditioned on both textual context and visual information.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 其中，$g(\cdot)$ 表示文本嵌入函数，$f(\cdot)$ 是一个根据文本嵌入和视觉特征为下一个标记生成隐藏状态的函数，而 $W\in\mathbb{R}^{|V|\times d}$ 被训练用于将融合表征投影为词表上的分布。该形式化说明了 VLM 如何在文本上下文与视觉信息的共同条件下预测下一个标记。

### Figure 2. IVT-LR framework / IVT-LR 框架

![Figure 2](assets/page_004_fig_figure_2.png)

**Caption:** Overview of our Interleaved Vision-Text Latent Reasoning (IVT-LR) framework. At each step, reasoning is performed entirely in the latent space by fusing latent text (the hidden state from the previous step) and latent vision (dynamically selected image embeddings based on attention scores).

**Caption[CN]:** 我们的交错视觉—文本潜在推理（IVT-LR）框架概览。在每一步中，通过融合潜在文本（前一步的隐藏状态）与潜在视觉（依据注意力分数动态选择的图像嵌入），完全在潜在空间中执行推理。

### 3.1 Multimodal Latent Reasoning

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Figure 2 provides an overview of our approach. In IVT-LR, the latent reasoning is conducted over both latent text and latent vision. Following [12], the textual modality bypasses explicit token prediction: instead of using the embedding of the previous explicit text token, we represent the latent text with the hidden state $h^{\mathrm{hidden}}_{t-1}$, which effectively encodes the necessary reasoning logic and preserves richer intermediate information in a continuous latent space. Meanwhile, the latent vision is designed to model the dynamic focus on the visual features at each step. Specifically, we extend latent reasoning to visual modality by selecting the $k$ most relevant visual features from the image embedding set. Thus, an attention-based selection mechanism is designed to choose a fixed number of image embeddings from the full set $[z_1,z_2,\ldots,z_J]$. We utilize the sum of attention weights across all layers to identify the $k$ image embedding positions with the highest cumulative scores.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 图 2 给出了我们方法的概览。在 IVT-LR 中，潜在推理同时在潜在文本和潜在视觉之上进行。遵循 [12]，文本模态绕过显式标记预测：我们不使用前一个显式文本标记的嵌入，而是用隐藏状态 $h^{\mathrm{hidden}}_{t-1}$ 表示潜在文本；该状态有效编码了必要的推理逻辑，并在连续潜在空间中保留更丰富的中间信息。与此同时，潜在视觉旨在建模每一步对视觉特征的动态关注。具体而言，我们从图像嵌入集合中选择 $k$ 个最相关的视觉特征，将潜在推理扩展到视觉模态。因此，我们设计了一种基于注意力的选择机制，从完整集合 $[z_1,z_2,\ldots,z_J]$ 中选择固定数量的图像嵌入。我们利用所有层注意力权重之和，确定累积得分最高的 $k$ 个图像嵌入位置。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The selected features are appended to the hidden states $h^{\mathrm{hidden}}_{t-1}$, resulting in a multimodal latent representation $[h^{\mathrm{latent}}_{t-1},z^{\mathrm{selected}}_{t-1}]$. The input to the model at step $t$ thus consists of all prior hidden states and their selected visual features, along with any preceding question embeddings, which can be written as

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 选定的特征被附加到隐藏状态 $h^{\mathrm{hidden}}_{t-1}$ 上，形成多模态潜在表征 $[h^{\mathrm{latent}}_{t-1},z^{\mathrm{selected}}_{t-1}]$。因此，模型在第 $t$ 步的输入由所有先前隐藏状态及其选定的视觉特征，以及此前的全部问题嵌入组成，可写为

$$
E_t=[e_1,\ldots,e_N,h^{\mathrm{latent}}_1,z^{\mathrm{selected}}_1,\ldots,h^{\mathrm{latent}}_{t-1},z^{\mathrm{selected}}_{t-1}].
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The model fuses these multimodal representations to obtain $e^{\mathrm{fused}}_t=f(E_t)$, which is projected through the output head to yield the next-token distribution $M(x_{t+1}\mid E_t)=\operatorname{softmax}(W\cdot e^{\mathrm{fused}}_t)$. This design allows the model to perform step-wise multimodal latent reasoning without generating intermediate reasoning sequences.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 模型融合这些多模态表征以得到 $e^{\mathrm{fused}}_t=f(E_t)$，再通过输出头投影，产生下一个标记的分布 $M(x_{t+1}\mid E_t)=\operatorname{softmax}(W\cdot e^{\mathrm{fused}}_t)$。该设计使模型无需生成中间推理序列，即可执行逐步的多模态潜在推理。

### 3.2 Training Procedure.

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The objective of IVT-LR is to enable multimodal reasoning within the latent space. Inspired by Deng et al. [26], we adopt a multi-stage training strategy to progressively boost the model’s reasoning capability. In the preprocessing stage, each reasoning trajectory is segmented into up to $N$ steps, followed by the final answer. At stage 0, as shown in Figure 3, the model is trained with standard CoT supervision, where all reasoning steps are explicitly generated to strengthen symbolic reasoning ability. Afterwards, the latent reasoning steps are progressively introduced within the $N$ stages: at each stage, one additional explicit reasoning step is replaced by a latent reasoning step, denoted by the special token `<latent>`, beginning with the first step. In this way, the model learns to progressively substitute explicit reasoning using latent textual and visual representations while still being supervised on the final answer.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> IVT-LR 的目标是使多模态推理能够在潜在空间中进行。受 Deng 等人 [26] 启发，我们采用多阶段训练策略，逐步增强模型的推理能力。在预处理阶段，每条推理轨迹被划分为最多 $N$ 个步骤，之后是最终答案。在阶段 0，如图 3 所示，模型采用标准 CoT 监督进行训练，显式生成全部推理步骤，以增强符号推理能力。随后，在 $N$ 个阶段中逐步引入潜在推理步骤：从第一步开始，每个阶段额外用一个潜在推理步骤替换一个显式推理步骤，并用特殊标记 `<latent>` 表示。通过这种方式，模型学习使用潜在文本与视觉表征逐步替代显式推理，同时仍接受最终答案的监督。

### Figure 3. Multi-stage progressive training strategy / 多阶段渐进训练策略

![Figure 3](Reasoning/Train/Reasoning%20in%20the%20Dark%20Interleaved%20Vision-Text%20Reasoning%20in%20Latent%20Space/assets/page_005_fig_figure_3.png)

**Caption:** Overview of the Multi-Stage Progressive Training Strategy used for IVT-LR. The strategy begins with full explicit CoT and then gradually substitutes one explicit reasoning step with latent text and latent vision. Training loss is calculated exclusively over the remaining explicit steps and the final answer.

**Caption[CN]:** IVT-LR 所采用的多阶段渐进训练策略概览。该策略从完整的显式 CoT 开始，随后逐渐用潜在文本和潜在视觉替换一个显式推理步骤。训练损失仅在剩余的显式步骤和最终答案上计算。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Training is optimized using negative log-likelihood (NLL) loss, with supervision applied only to reasoning steps and the final answer. Latent reasoning steps and question tokens are masked out. This design ensures that the supervision signal is placed only on the reasoning steps and the final answer, distinguishing our approach from standard knowledge distillation. Unlike distillation, which enforces alignment between student hidden states and a teacher’s explicit reasoning trajectory, our method avoids imposing a strict linear path. By avoiding excessive alignment between latent representations and explicit rationales, the model learns to internalize reasoning trajectories in latent space with essential image features, while still being driven toward correct final predictions. Compared to single-step fine-tuning, the proposed multi-stage training introduces additional stages but reuses the same backbone and training data, resulting in a moderate increase in training cost that remains practical and acceptable.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 训练使用负对数似然（NLL）损失进行优化，监督仅施加于推理步骤和最终答案。潜在推理步骤与问题标记均被屏蔽。该设计确保监督信号只落在推理步骤和最终答案上，从而将我们的方法与标准知识蒸馏区分开来。蒸馏会强制学生模型的隐藏状态与教师模型的显式推理轨迹对齐，而我们的方法避免施加严格的线性路径。通过避免潜在表征与显式推理依据之间的过度对齐，模型学习在潜在空间中将包含必要图像特征的推理轨迹内化，同时仍被引导至正确的最终预测。与单步微调相比，所提出的多阶段训练增加了额外阶段，但复用了相同的主干模型和训练数据，因此训练成本仅适度增加，仍然实际且可接受。

### Algorithm 1. IVT-LR

![Algorithm 1](assets/page_005_fig_algorithm_1.png)

**Caption:** Algorithm 1: IVT-LR.

**Caption[CN]:** 算法 1：IVT-LR。

| Line | Searchable source transcription | 中文对照 |
|---:|---|---|
| 1 | **Input:** Text input embeddings $\mathcal{E}=[e_1,\ldots,e_I]$, Image input embeddings $\mathcal{Z}=[z_1,\ldots,z_J]$, Whole input embeddings $\mathcal{Q}=\mathcal{E}+\mathcal{Z}=[q_1,\ldots,q_m]$, Latent step positions $\mathcal{L}=[l_1,\ldots,l_N]$, Number of selected embeddings $k$ | **输入：** 文本输入嵌入 $\mathcal{E}=[e_1,\ldots,e_I]$，图像输入嵌入 $\mathcal{Z}=[z_1,\ldots,z_J]$，完整输入嵌入 $\mathcal{Q}=\mathcal{E}+\mathcal{Z}=[q_1,\ldots,q_m]$，潜在步骤位置 $\mathcal{L}=[l_1,\ldots,l_N]$，选定嵌入数量 $k$ |
| 2 | **for** $i=1$ to $N$ **do** | **对于** $i=1$ 到 $N$，**执行** |
| 3 | $h_i\leftarrow\operatorname{LastHiddenState}(q_{1:l_i-1})$ | $h_i\leftarrow\operatorname{LastHiddenState}(q_{1:l_i-1})$（取得最后的隐藏状态） |
| 4 | $\mathcal{Z}_{sel}\leftarrow\operatorname{AttentionSelect}(\mathcal{Z},k)$ | $\mathcal{Z}_{sel}\leftarrow\operatorname{AttentionSelect}(\mathcal{Z},k)$（按注意力选择嵌入） |
| 5 | $latent[i]\leftarrow[h_i,\mathcal{Z}_{sel}]$ | $latent[i]\leftarrow[h_i,\mathcal{Z}_{sel}]$（组成第 $i$ 个潜在单元） |
| 6 | $\mathcal{Q}\leftarrow\operatorname{Concat}(\mathcal{Q},latent[i])$ | $\mathcal{Q}\leftarrow\operatorname{Concat}(\mathcal{Q},latent[i])$（将潜在单元拼接到输入） |
| 7 | $l_n\leftarrow l_n+(k+1)$ &nbsp; **for** $n>i$ | 对所有 $n>i$，令 $l_n\leftarrow l_n+(k+1)$ |
| 8 | **end for** | **结束循环** |
| 9 | $q_{:end}\leftarrow\operatorname{PredictToEnd}(q_{:l_N})$ | $q_{:end}\leftarrow\operatorname{PredictToEnd}(q_{:l_N})$（预测至末尾） |
| 10 | $Answer\leftarrow\operatorname{Decode}(q_{l_N+1:})$ | $Answer\leftarrow\operatorname{Decode}(q_{l_N+1:})$（解码答案） |
| 11 | **return** $Answer$ | **返回** $Answer$ |

### 3.3 Inference Process.

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Since all rationales in training have been segmented into a certain number of steps, at inference time, the same number of `<latent>` tokens are appended after the question and image inputs. This setup ensures that reasoning is fully conducted in latent space and no explicit reasoning steps are produced before the final answer.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 由于训练中的所有推理依据都已被划分为一定数量的步骤，因此在推理时，会在问题和图像输入之后附加相同数量的 `<latent>` 标记。该设置确保推理完全在潜在空间中进行，并且在最终答案之前不会产生显式推理步骤。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> To evaluate the intermediate models at stage $n$, inference uses $n$ latent tokens, yielding mixed explicit-latent reasoning consistent with the training stage. Importantly, latent text and latent vision co-exist only during the latent reasoning phase, where visual evidence is integrated into the hidden trajectory. Outside this phase, the model operates in a purely linguistic generation mode.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 为评估阶段 $n$ 的中间模型，推理使用 $n$ 个潜在标记，从而得到与该训练阶段一致的显式—潜在混合推理。重要的是，潜在文本和潜在视觉仅在潜在推理阶段共存；在这一阶段，视觉证据被整合进隐藏轨迹。离开这一阶段后，模型以纯语言生成模式运行。

## 4 Experiments

### 4.1 Experimental Setup.

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Datasets and Evaluation.** We evaluate our method on two widely used multimodal reasoning benchmarks: M3CoT [28] and ScienceQA [29]. M3CoT is a large-scale benchmark focusing on multimodal chain-of-thought reasoning, where models must combine both visual and textual inputs to perform multi-step reasoning. ScienceQA is a diverse dataset covering natural science, language science, and social science, with many questions accompanied by diagrams or images. We evaluate using exact-match answer accuracy, along with the average number of autoregressive steps and the average response time per question. These metrics capture both correctness and reasoning efficiency.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **数据集与评估。** 我们在两个广泛使用的多模态推理基准上评估所提出的方法：M3CoT [28] 和 ScienceQA [29]。M3CoT 是一个聚焦多模态思维链推理的大规模基准，其中模型必须结合视觉输入与文本输入来执行多步推理。ScienceQA 是一个多样化的数据集，涵盖自然科学、语言科学和社会科学，其中许多问题附有图示或图像。我们使用精确匹配答案准确率进行评估，同时衡量平均自回归步数以及每个问题的平均响应时间。这些指标同时刻画正确性与推理效率。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Baselines and Implementation Details** We compare IVT-LR against six representative methods, including text-only reasoning: CCoT [14]; vision-text involved reasoning: Chain-of-Focus [17], SCAFFOLD [27], ICoT [9], Multimodal-CoT [15]; and No-CoT that directly predicts answers without generating intermediate steps.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **基线与实现细节** 我们将 IVT-LR 与六种代表性方法进行比较，其中包括纯文本推理方法 CCoT [14]；视觉—文本参与的推理方法 Chain-of-Focus [17]、SCAFFOLD [27]、ICoT [9]、Multimodal-CoT [15]；以及不生成中间步骤、直接预测答案的 No-CoT。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> For fair comparison, we evaluate IVT-LR and all baselines with Qwen2-VL-7B [30] and Chameleon-7B [31] backbones. In IVT-LR training, we use a stage number ($N$) of four (detailed discussion provided in Appendix A) , a batch size of four, and train with the Adam optimizer where the learning rate is set to $4\times10^{-5}$ and $\beta_1$ is set to $0.9$. All experiments run on four NVIDIA A6000 GPUs (48GB VRAM each).

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 为进行公平比较，我们使用 Qwen2-VL-7B [30] 和 Chameleon-7B [31] 主干模型评估 IVT-LR 及所有基线。在 IVT-LR 训练中，我们将阶段数（$N$）设为 4（详细讨论见附录 A），批量大小设为 4，并使用 Adam 优化器训练，其中学习率设为 $4\times10^{-5}$，$\beta_1$ 设为 $0.9$。所有实验均在 4 张 NVIDIA A6000 GPU 上运行（每张具有 48GB VRAM）。

### Table 1. Main comparison / 主要比较

![Table 1](Reasoning/Train/Reasoning%20in%20the%20Dark%20Interleaved%20Vision-Text%20Reasoning%20in%20Latent%20Space/assets/page_006_fig_table_1.png)

**Caption:** Comparison of IVT-LR with various multimodal reasoning baselines on the M³CoT and ScienceQA benchmarks. The reported metrics include: Answer Accuracy (Acc.), Average number of Autoregressive Steps (# AR Steps), and Average Generation Time (Avg. Time). Experiments are conducted using two backbone models: Qwen2-VL-7B and Chameleon-7B.

**Caption[CN]:** IVT-LR 与多种多模态推理基线在 M³CoT 和 ScienceQA 基准上的比较。报告的指标包括：答案准确率（Acc.）、平均自回归步数（# AR Steps）和平均生成时间（Avg. Time）。实验采用 Qwen2-VL-7B 与 Chameleon-7B 两种主干模型。

| Backbone | Methods | M3CoT Acc.(%) ↑ | M3CoT # AR Steps ↓ | M3CoT Avg. Time(s) ↓ | ScienceQA Acc.(%) ↑ | ScienceQA # AR Steps ↓ | ScienceQA Avg. Time(s) ↓ |
|---|---|---:|---:|---:|---:|---:|---:|
| Qwen2-VL | No-CoT | 45.4 | - | - | 64.4 | - | - |
| Qwen2-VL | Multimodal CoT[15] | 42.5 | 106.3 | 3.10 | 58.3 | 83.9 | 2.44 |
| Qwen2-VL | CCoT[14] | 44.1 | 177.2 | 5.31 | 63.8 | 164.0 | 5.23 |
| Qwen2-VL | ICoT[9] | 46.0 | 96.5 | 2.86 | 65.4 | 77.4 | 2.28 |
| Qwen2-VL | SCAFFOLD[27] | 44.9 | 170.8 | 5.14 | 62.5 | 162.3 | 4.91 |
| Qwen2-VL | Chain-of-Focus[17] | 64.3 | 185.7 | 2.63 | 91.2 | 162.3 | 2.09 |
| Qwen2-VL | **IVT-LR** | **71.8** | **10.0** | **0.65** | **94.6** | **11.0** | **0.67** |
| Chameleon | No-CoT | 28.4 | - | - | 48.5 | - | - |
| Chameleon | Multimodal CoT[15] | 30.6 | 110.5 | 3.62 | 50.7 | 98.7 | 3.33 |
| Chameleon | CCoT[14] | 31.4 | 168.4 | 5.35 | 51.3 | 174.2 | 5.39 |
| Chameleon | ICoT[9] | 32.3 | 110.9 | 5.43 | 53.4 | 92.4 | 4.62 |
| Chameleon | SCAFFOLD[27] | 31.1 | 194.3 | 6.12 | 47.5 | 160.6 | 6.03 |
| Chameleon | Chain-of-Focus[17] | 36.5 | 739.4 | 3.09 | 61.2 | 717.1 | 2.56 |
| Chameleon | **IVT-LR** | **41.8** | **10.0** | **1.13** | **64.0** | **11.0** | **1.14** |

### 4.2 Main Results.

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The results on M3CoT and ScienceQA are summarized in Table 1. Analyzing these outcomes, we draw the following key observations:

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> M3CoT 和 ScienceQA 上的结果汇总于表 1。通过分析这些结果，我们得到以下关键观察：

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Multimodal Reasoning Accuracy.** IVT-LR achieves the highest accuracy on both the M3CoT and ScienceQA benchmarks, consistently outperforming all baselines with both Qwen2-VL and Chameleon backbones. Compared to the strongest baseline, Chain-of-Focus, IVT-LR yields improvements of 5% (Chameleon backbone) to 7.5% (Qwen2-VL backbone) on M3CoT. Similar gains are observed on the ScienceQA benchmark. Beyond this, IVT-LR surpasses other methods by margins of 10% to 25%, depending on the backbone and task. These results demonstrate that IVT-LR enables more effective cross-modal interaction in the latent space, leading to stronger multimodal reasoning capability on complex tasks.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **多模态推理准确率。** IVT-LR 在 M3CoT 和 ScienceQA 两个基准上均取得最高准确率，并在 Qwen2-VL 与 Chameleon 两种主干模型上持续优于所有基线。与最强基线 Chain-of-Focus 相比，IVT-LR 在 M3CoT 上取得 5%（Chameleon 主干）至 7.5%（Qwen2-VL 主干）的提升。在 ScienceQA 基准上也观察到了类似增益。除此之外，根据主干模型和任务的不同，IVT-LR 以 10% 至 25% 的幅度超过其他方法。这些结果表明，IVT-LR 能够在潜在空间中实现更有效的跨模态交互，从而在复杂任务上获得更强的多模态推理能力。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Reasoning Efficiency.** Beyond accuracy, a critical advantage of IVT-LR is its significantly enhanced inference efficiency, which is quantified by fewer autoregressive steps and lower inference latency compared to baselines. 1) Fewer autoregressive steps. Across both backbones, IVT-LR achieves at least a $9\times$ reduction in the number of autoregressive steps required for generation compared to most baselines. This efficiency is achieved by conducting reasoning in the latent space, avoiding the need for lengthy, explicitly generated rationales required by other methods. 2) Lower Inference Latency. With the Qwen model, IVT-LR achieves an average inference time of approximately 0.66s, making it 3 to 8 times faster than all other baselines. A similar trend of significant speedup holds true for the Chameleon backbone. While No-CoT achieves the absolute lowest latency by completely sacrificing deep reasoning (around 0.35s), IVT-LR delivers state-of-the-art accuracy at an inference speed only marginally longer than the minimal No-CoT, demonstrating superior efficiency in the high-accuracy setting.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **推理效率。** 除准确率外，IVT-LR 的一项关键优势是显著增强的推理效率；与基线相比，这体现为更少的自回归步数与更低的推理时延。1）更少的自回归步数。在两种主干模型上，与大多数基线相比，IVT-LR 将生成所需的自回归步数至少减少到原来的 $1/9$。这种效率来自在潜在空间中进行推理，从而无需生成其他方法所需的冗长显式推理依据。2）更低的推理时延。使用 Qwen 模型时，IVT-LR 的平均推理时间约为 0.66s，比所有其他基线快 3 至 8 倍。在 Chameleon 主干上也呈现类似的显著加速趋势。尽管 No-CoT 通过完全牺牲深度推理获得了绝对最低时延（约 0.35s），IVT-LR 仍以仅略长于最简 No-CoT 的推理速度实现最先进的准确率，表明其在高准确率设置下具有卓越效率。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> In summary, IVT-LR demonstrates both superior accuracy and improved reasoning efficiency in VQA tasks. By performing multi-step reasoning in latent space, the model not only achieves the highest accuracy among all baselines but also significantly reduces the number of autoregressive steps and achieves a substantially lower inference latency. These results highlight the effectiveness of latent reasoning in combining textual and visual info.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 总之，IVT-LR 在 VQA 任务中同时展现出更高的准确率和更好的推理效率。通过在潜在空间中执行多步推理，该模型不仅在所有基线中取得最高准确率，还显著减少了自回归步数，并实现了大幅降低的推理时延。这些结果凸显了潜在推理在结合文本信息和视觉信息方面的有效性。

### 4.3 Ablation Study.

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> To verify the necessity of IVT-LR’s two key components, latent text and latent vision, we conducted a series of ablation experiments on visual reasoning tasks. Specifically, we evaluated the effects of removing latent text, latent vision, and both components simultaneously.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 为验证 IVT-LR 两个关键组成部分——潜在文本与潜在视觉——的必要性，我们在视觉推理任务上开展了一系列消融实验。具体而言，我们评估了移除潜在文本、移除潜在视觉以及同时移除这两个组成部分所产生的影响。

### Table 2. Latent-component ablation / 潜在组件消融

![Table 2](Reasoning/Train/Reasoning%20in%20the%20Dark%20Interleaved%20Vision-Text%20Reasoning%20in%20Latent%20Space/assets/page_007_fig_table_2.png)

**Caption:** Accuracy comparison of IVT-LR on Qwen2-VL, showing the performance impact with and without its core latent components (latent text and/or latent vision). Values in parentheses indicate performance drop relative to full IVT-LR.

**Caption[CN]:** IVT-LR 在 Qwen2-VL 上的准确率比较，展示保留或移除其核心潜在组件（潜在文本和/或潜在视觉）时对性能的影响。括号内数值表示相对于完整 IVT-LR 的性能下降。

| Methods | M3CoT | ScienceQA |
|---|---:|---:|
| **IVT-LR** | **71.83** | **94.1** |
| w/o latent text | 52.20 (-19.63) | 84.7 (-9.8) |
| w/o latent vision | 46.64 (-25.19) | 82.3 (-11.8) |
| w/o the whole latent part | 58.02 (-13.81) | 86.4 (-7.7) |

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **Latent Text.** As shown in Table 2, removing latent text(w/o latent text) leads to a noticeable drop in accuracy on both M3CoT and ScienceQA. This demonstrates that latent text plays a crucial role in model performance: it provides a compact, continuous representation of intermediate reasoning states. This allows the model to internalize multi-step reasoning trajectories directly in the latent space, avoiding biases introduced by language-based alignment. Furthermore, operating in continuous hidden spaces, it effectively mitigates the amplification of errors typical in discrete, step-by-step textual reasoning.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **潜在文本。** 如表 2 所示，移除潜在文本（w/o latent text）会导致 M3CoT 和 ScienceQA 上的准确率均明显下降。这表明潜在文本对模型性能起着关键作用：它为中间推理状态提供紧凑、连续的表征。这使模型能够直接在潜在空间中内化多步推理轨迹，避免基于语言的对齐所引入的偏差。此外，由于在连续隐藏空间中运行，它有效缓解了离散、逐步文本推理中常见的误差放大。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> **Latent Vision.** Table 2 also shows that removing latent vision (w/o latent vision) also results in decreased performance. This indicates that incorporating the most informative visual cues is vital for precise multimodal reasoning. Without this mechanism, the model cannot focus on the critical regions of the image, reducing the effectiveness of each reasoning step. Besides, based on attention-driven integration, latent vision ensures that the latent space receives rich, contextually relevant visual information. It also mitigates interference from irrelevant image regions, leading to more accurate and robust reasoning.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> **潜在视觉。** 表 2 还表明，移除潜在视觉（w/o latent vision）同样会使性能下降。这说明，引入信息量最大的视觉线索对于精确的多模态推理至关重要。缺少这一机制时，模型无法聚焦图像的关键区域，从而降低每一步推理的有效性。此外，基于注意力驱动的整合，潜在视觉可确保潜在空间接收到丰富且与上下文相关的视觉信息。它也能缓解无关图像区域的干扰，从而带来更准确、更稳健的推理。

### 4.4 In-depth Analysis.

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> **Length of Latent vision** We investigate the impact of varying the latent vision length per step.As shown in Figure 4, accuracy steadily increases with this length, indicating that longer latent vision sequences provide richer visual cues necessary for complex reasoning. Since the latent vision is formed by adaptively selecting visual embeddings from the image, increasing the length of these selections allows the model to gradually approach full-image utilization (e.g., 32 embeddings over three steps roughly cover the whole image in Qwen2-VL). This ensures that essential visual details, often required for global comprehension, are not omitted. Moreover, because embeddings are selected step-by-step across the latent reasoning stages, the process achieves targeted and cumulative coverage: each round complements the previous ones, enabling the model to integrate both localized critical features and broader global context in a structured, effective manner.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> **潜在视觉的长度** 我们研究每一步采用不同潜在视觉长度所产生的影响。如图 4 所示，准确率随该长度稳定上升，这说明更长的潜在视觉序列提供了复杂推理所需的更丰富视觉线索。由于潜在视觉是通过从图像中自适应选择视觉嵌入形成的，增加这些选择的长度可使模型逐渐接近对整幅图像的利用（例如，在 Qwen2-VL 中，三个步骤共使用 32 个嵌入大致覆盖整幅图像）。这确保了全局理解经常需要的关键视觉细节不会被遗漏。此外，由于嵌入是在各潜在推理阶段逐步选择的，该过程实现了有针对性且累积式的覆盖：每一轮都对先前轮次形成补充，使模型能够以结构化、有效的方式同时整合局部关键特征与更广泛的全局上下文。

### Figure 4. Length of latent vision / 潜在视觉长度

![Figure 4](assets/page_008_fig_figure_4.png)

**Caption:** Accuracy comparison of IVT-LR on the length of latent vision per reasoning step across two reasoning benchmarks: (a) M³CoT and (b) ScienceQA.

**Caption[CN]:** IVT-LR 在两个推理基准上针对每个推理步骤中潜在视觉长度的准确率比较：（a）M³CoT；（b）ScienceQA。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> **Stages of Latent Reasoning** We evaluate models with 1, 2, and 3 latent reasoning steps to study the effect of progressively replacing explicit reasoning. As shown in Table 3, accuracy improves as more reasoning steps are conducted in latent space, showing that latent representations provide a more robust reasoning mechanism than explicit language. This is because latent states avoid errors from language alignment and allow smoother integration with image embeddings.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> **潜在推理的阶段数** 我们评估具有 1、2 和 3 个潜在推理步骤的模型，以研究逐步替换显式推理的效果。如表 3 所示，随着更多推理步骤在潜在空间中进行，准确率随之提高，表明潜在表征提供了比显式语言更稳健的推理机制。这是因为潜在状态避免了语言对齐带来的误差，并允许与图像嵌入进行更平滑的整合。

### Table 3. Latent reasoning stages / 潜在推理阶段

![Table 3](Reasoning/Train/Reasoning%20in%20the%20Dark%20Interleaved%20Vision-Text%20Reasoning%20in%20Latent%20Space/assets/page_008_fig_table_3.png)

**Caption:** Accuracy on M³CoT across different latent reasoning stages. Results are shown both overall and broken down by domain.

**Caption[CN]:** 不同潜在推理阶段在 M³CoT 上的准确率。结果同时给出总体准确率和按领域划分的准确率。

| Latent Stage | Science | Commonsense | Mathematics | Total |
|---:|---:|---:|---:|---:|
| 1 | 56.66% | 64.40% | 38.59% | 56.30% |
| 2 | 61.71% | 70.11% | 43.57% | 61.48% |
| **3** | **70.90%** | **79.78%** | **63.07%** | **71.83%** |

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> Domain-wise results show that science and mathematics benefit most from additional latent tokens, highlighting that structured reasoning tasks are particularly suited for latent-space inference. The accuracy in commonsense also improves, but with smaller gains, since it often relies less on multi-step deduction. Together, these findings confirm that latent reasoning scales effectively with task complexity, supporting both efficiency and accuracy.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> 分领域结果表明，科学与数学从额外的潜在标记中受益最多，这凸显了结构化推理任务尤其适合潜在空间推断。常识领域的准确率也有所提高，但增益较小，因为它往往较少依赖多步演绎。综合来看，这些发现证实潜在推理能够随任务复杂度有效扩展，同时支持效率与准确率。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> **Attention Shift over Step-wise Embeddings** To further investigate the internal mechanisms of IVT-LR, we analyze how the model allocates its attention to image embeddings under our method and explicit reasoning with selected image embeddings. We use Attention Ratio and Attention Focus as metrics to analyze the model’s focus.

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> **逐步嵌入上的注意力转移** 为进一步研究 IVT-LR 的内部机制，我们分析在我们的方法以及使用选定图像嵌入的显式推理中，模型如何将注意力分配给图像嵌入。我们使用注意力比率和注意力集中度作为指标来分析模型的关注方式。

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> (1) Attention Ratio:

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> （1）注意力比率：

$$
R=\frac{\sum_{j\in\mathcal{I}}\operatorname{Attn}(E_j)}{\sum_{i\in\mathcal{T}}\operatorname{Attn}(E_i)}.\tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> where $\mathcal{I}$ denotes the visual reasoning part, specifically the set of selected image embeddings, and $\mathcal{T}$ denotes the text tokens or the latent text part. This ratio reflects the relative allocation of attention between visual and textual information.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> 其中，$\mathcal{I}$ 表示视觉推理部分，具体指选定图像嵌入的集合；$\mathcal{T}$ 表示文本标记或潜在文本部分。该比率反映视觉信息与文本信息之间的相对注意力分配。

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> (2) Attention Focus (Inverse Entropy):

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> （2）注意力集中度（逆熵）：

$$
H=-\sum_k p_k\log p_k,\qquad p_k=\frac{\operatorname{Attn}(E_k)}{\sum_m\operatorname{Attn}(E_m)},
$$

$$
F=\frac{1}{H+\epsilon},\qquad \epsilon\ll 1.\tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> where $F$ is the Attention Focus. Higher $F$ indicates more concentrated attention, while lower $F$ reflects dispersed focus.

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> 其中，$F$ 为注意力集中度。较高的 $F$ 表示注意力更加集中，而较低的 $F$ 反映更分散的关注。

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> The result is shown in Figure 5. We found significant differences in model behavior between latent and explicit multimodal reasoning modes:

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> 结果如图 5 所示。我们发现，在潜在多模态推理模式与显式多模态推理模式之间，模型行为存在显著差异：

### Figure 5. Attention analysis / 注意力分析

![Figure 5](assets/page_009_fig_figure_5.png)

**Caption:** Attention analysis comparison between explicit and latent reasoning approaches. Left: attention ratios of visual part to textual part across reasoning steps. Right: attention focus measured by inverse entropy.

**Caption[CN]:** 显式推理方法与潜在推理方法之间的注意力分析比较。左：各推理步骤中视觉部分相对于文本部分的注意力比率。右：由逆熵衡量的注意力集中度。

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> **(1) Dynamic Attention Ratio: A Core of Visio-Linguistic Perception.** In the latent reasoning mode, the attention ratio exhibits a clear downward trend across reasoning steps. Initially, the model focuses predominantly on latent vision, but over subsequent steps, attention gradually shifts to its latent text for deeper textual reasoning. This dynamic adjustment demonstrates the model’s ability to prioritize the most informative visual cues and adaptively reallocate focus, reflecting enhanced visio-linguistic perception. In contrast, under explicit reasoning, the attention ratio remains largely unchanged and consistently below 1, indicating persistent focus on textual tokens. This suggests that, with interference from abundant textual information, explicit reasoning struggles to effectively filter and leverage critical visual features.

> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> **（1）动态注意力比率：视觉—语言感知的核心。** 在潜在推理模式下，注意力比率随推理步骤呈现清晰的下降趋势。最初，模型主要关注潜在视觉；但在后续步骤中，注意力逐渐转移到潜在文本，以进行更深入的文本推理。这种动态调整表明，模型能够优先处理信息量最大的视觉线索并自适应地重新分配关注，从而体现出增强的视觉—语言感知。相比之下，在显式推理下，注意力比率大体保持不变，并始终低于 1，表明模型持续关注文本标记。这说明，在大量文本信息的干扰下，显式推理难以有效筛选并利用关键视觉特征。

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> **(2) Rising Attention Focus: A Hallmark of Efficient Reasoning.** Beyond changes in attention ratio, our analysis of attention focus also reveals important insights. In latent reasoning, attention focus shows a progressively increasing trend, showing that the model’s attention becomes increasingly concentrated over reasoning steps. This suggests that at each step, the model effectively filters and refines multimodal information, gradually converging on the most critical and relevant cues—a pattern reminiscent of human problem-solving, where distractions are progressively eliminated and attention is concentrated on core evidence. In contrast, under explicit reasoning, attention focus is not only markedly lower than in implicit reasoning but also exhibits little change across steps. This indicates that explicit reasoning distributes attention more diffusely and lacks clear direction, processing substantial amounts of redundant or less relevant information, which reduces reasoning efficiency and limits the effective extraction of key visual-textual information.

> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> **（2）不断上升的注意力集中度：高效推理的标志。** 除注意力比率的变化外，我们对注意力集中度的分析也揭示了重要见解。在潜在推理中，注意力集中度呈逐步上升趋势，表明模型的注意力在推理步骤推进过程中越来越集中。这意味着在每一步中，模型都能有效筛选和提炼多模态信息，逐渐收敛到最关键、最相关的线索——这一模式类似于人类解决问题的过程：干扰被逐步排除，注意力集中到核心证据上。相比之下，在显式推理下，注意力集中度不仅显著低于隐式推理，而且在各步骤间几乎没有变化。这表明显式推理的注意力分配更为分散且缺乏清晰方向，会处理大量冗余或相关性较低的信息，从而降低推理效率，并限制对关键视觉—文本信息的有效提取。

## 5 Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In this work, we present IVT-LR, the first vision-language reasoning framework that performs multimodal latent reasoning. IVT-LR utilizes latent text and latent vision to internalize complex reasoning trajectories, thereby realizing comprehensive multimodal latent reasoning. This approach effectively mitigates the attention dilution problem present in existing methods that rely on explicit textual reasoning and full-image processing. On VQA and other visual reasoning tasks, IVT-LR significantly outperforms multiple strong baselines, achieving new state-of-the-art results in both reasoning accuracy and efficiency. Our findings demonstrate the potential of interleaved vision-text reasoning in latent space, offering a promising paradigm for building more efficient and perceptive vision-language models and inspiring future research on multimodal reasoning strategies.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在本工作中，我们提出 IVT-LR，这是首个执行多模态潜在推理的视觉—语言推理框架。IVT-LR 利用潜在文本和潜在视觉将复杂推理轨迹内化，从而实现全面的多模态潜在推理。该方法有效缓解了现有方法中因依赖显式文本推理与整图处理而出现的注意力稀释问题。在 VQA 和其他视觉推理任务上，IVT-LR 显著优于多个强基线，在推理准确率和效率两方面均取得新的最先进结果。我们的发现展示了潜在空间中交错视觉—文本推理的潜力，为构建更高效、感知能力更强的视觉—语言模型提供了一种前景广阔的范式，并启发未来对多模态推理策略的研究。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Future work could explore more dynamic ways of visual latent reasoning, such as adaptively determining the optimal number of latent steps based on the complexity of the question, rather than relying on a fixed stage number. Furthermore, this approach is highly promising for extending its application beyond pure reasoning to broader sequential multimodal tasks, including planning and complex decision-making in dynamic environments.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 未来工作可以探索更动态的视觉潜在推理方式，例如根据问题复杂度自适应地确定最佳潜在步数，而不是依赖固定的阶段数。此外，该方法在将应用从纯推理扩展到更广泛的序列多模态任务方面极具前景，其中包括动态环境中的规划与复杂决策。

## References

> **Reference policy:** All 31 bibliographic entries are retained individually in their original searchable English bibliographic form. Titles, author names, venues, years, page ranges, identifiers, and DOI strings are not translated.  
> **参考文献政策：** 下列 31 条书目均以原始、可检索的英文书目形式逐条保留；题名、作者名、出版物、年份、页码范围、标识符和 DOI 字符串不作翻译。

1. Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Fei Xia, Ed Chi, Quoc V Le, Denny Zhou, et al. Chain-of-thought prompting elicits reasoning in large language models. Advances in neural information processing systems, 35:24824–24837, 2022.

2. Aaron Hurst, Adam Lerer, Adam P Goucher, Adam Perelman, Aditya Ramesh, Aidan Clark, AJ Ostrow, Akila Welihinda, Alan Hayes, Alec Radford, et al. Gpt-4o system card. arXiv preprint arXiv:2410.21276, 2024.

3. Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Ruoyu Zhang, Runxin Xu, Qihao Zhu, Shirong Ma, Peiyi Wang, Xiao Bi, et al. Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv preprint arXiv:2501.12948, 2025.

4. Yushi Hu, Hang Hua, Zhengyuan Yang, Weijia Shi, Noah A Smith, and Jiebo Luo. Promptcap: Prompt-guided task-aware image captioning. arXiv preprint arXiv:2211.09699, 2022.

5. Debjyoti Mondal, Suraj Modi, Subhadarshi Panda, Rituraj Singh, and Godawari Sudhakar Rao. Kam-cot: Knowledge augmented multimodal chain-of-thoughts reasoning. In Proceedings of the AAAI conference on artificial intelligence, volume 38, pages 18798–18806, 2024. doi: 10.1609/aaai.v38i17.29844.

6. Yushi Hu, Weijia Shi, Xingyu Fu, Dan Roth, Mari Ostendorf, Luke Zettlemoyer, Noah A Smith, and Ranjay Krishna. Visual sketchpad: sketching as a visual chain of thought for multimodal language models. In Proceedings of the 38th International Conference on Neural Information Processing Systems, pages 139348–139379, 2024.

7. Dairu Liu, Ziyue Wang, Minyuan Ruan, Fuwen Luo, Chi Chen, Peng Li, and Yang Liu. Visual abstract thinking empowers multimodal reasoning. arXiv preprint arXiv:2505.20164, 2025.

8. Ethan Chern, Zhulin Hu, Steffi Chern, Siqi Kou, Jiadi Su, Yan Ma, Zhijie Deng, and Pengfei Liu. Thinking with generated images. arXiv preprint arXiv:2505.22525, 2025.

9. Jun Gao, Yongqi Li, Ziqiang Cao, and Wenjie Li. Interleaved-modal chain-of-thought. In Proceedings of the Computer Vision and Pattern Recognition Conference, pages 19520–19529, 2025. doi: 10.1109/CVPR52734.2025.01818.

10. Ziwei Zheng, Michael Yang, Jack Hong, Chenxiao Zhao, Guohai Xu, Le Yang, Chao Shen, and Xing Yu. Deepeyes: Incentivizing" thinking with images" via reinforcement learning. arXiv preprint arXiv:2505.14362, 2025.

11. Chengzu Li, Wenshan Wu, Huanyu Zhang, Yan Xia, Shaoguang Mao, Li Dong, Ivan Vulić, and Furu Wei. Imagine while reasoning in space: Multimodal visualization-of-thought. arXiv preprint arXiv:2501.07542, 2025.

12. Shibo Hao, Sainbayar Sukhbaatar, DiJia Su, Xian Li, Zhiting Hu, Jason Weston, and Yuandong Tian. Training large language models to reason in a continuous latent space. arXiv preprint arXiv:2412.06769, 2024.

13. Ge Zheng, Bin Yang, Jiajin Tang, Hong-Yu Zhou, and Sibei Yang. Ddcot: duty-distinct chain-of-thought prompting for multimodal reasoning in language models. In Proceedings of the 37th International Conference on Neural Information Processing Systems, pages 5168–5191, 2023.

14. Chancharik Mitra, Brandon Huang, Trevor Darrell, and Roei Herzig. Compositional chain-of-thought prompting for large multimodal models. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 14420–14431, 2024. doi: 10.1109/CVPR52733.2024.01367.

15. Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis, and Alex Smola. Multimodal chain-of-thought reasoning in language models. Transactions on Machine Learning Research, 2024, 2024.

16. Hao Shao, Shengju Qian, Han Xiao, Guanglu Song, Zhuofan Zong, Letian Wang, Yu Liu, and Hongsheng Li. Visual cot: advancing multi-modal language models with a comprehensive dataset and benchmark for chain-of-thought reasoning. In Proceedings of the 38th International Conference on Neural Information Processing Systems, pages 8612–8642, 2024.

17. Xintong Zhang, Zhi Gao, Bofei Zhang, Pengxiang Li, Xiaowen Zhang, Yang Liu, Tao Yuan, Yuwei Wu, Yunde Jia, Song-Chun Zhu, et al. Chain-of-focus: Adaptive visual search and zooming for multimodal reasoning via rl. arXiv preprint arXiv:2505.15436, 2025.

18. Yi Xu, Chengzu Li, Han Zhou, Xingchen Wan, Caiqi Zhang, Anna Korhonen, and Ivan Vulić. Visual planning: Let’s think only with images. arXiv preprint arXiv:2505.11409, 2025.

19. Sachin Goyal, Ziwei Ji, Ankit Singh Rawat, Aditya Krishna Menon, Sanjiv Kumar, and Vaishnavh Nagarajan. Think before you speak: Training language models with pause tokens. In The Twelfth International Conference on Learning Representations, 2024.

20. Xinyi Wang, Lucas Caccia, Oleksiy Ostapenko, Xingdi Yuan, William Yang Wang, and Alessandro Sordoni. Guiding language model reasoning with planning tokens. In First Conference on Language Modeling, 2024.

21. Jeffrey Cheng and Benjamin Van Durme. Compressed chain of thought: Efficient reasoning through dense representations. arXiv preprint arXiv:2412.13171, 2024.

22. Zhenyi Shen, Hanqi Yan, Linhai Zhang, Zhanghao Hu, Yali Du, and Yulan He. Codi: Compressing chain-of-thought into continuous space via self-distillation. arXiv preprint arXiv:2502.21074, 2025.

23. Zeyuan Yang, Xueyang Yu, Delin Chen, Maohao Shen, and Chuang Gan. Machine mental imagery: Empower multimodal reasoning with latent visual tokens. arXiv preprint arXiv:2506.17218, 2025.

24. Bangzheng Li, Ximeng Sun, Jiang Liu, Ze Wang, Jialian Wu, Xiaodong Yu, Hao Chen, Emad Barsoum, Muhao Chen, and Zicheng Liu. Latent visual reasoning. arXiv preprint arXiv:2509.24251, 2025.

25. Tan-Hanh Pham and Chris Ngo. Multimodal chain of continuous thought for latent-space reasoning in vision-language models. arXiv preprint arXiv:2508.12587, 2025.

26. Yuntian Deng, Yejin Choi, and Stuart Shieber. From explicit cot to implicit cot: Learning to internalize cot step by step. arXiv preprint arXiv:2405.14838, 2024.

27. Xuanyu Lei, Zonghan Yang, Xinrui Chen, Peng Li, and Yang Liu. Scaffolding coordinates to promote vision-language coordination in large multi-modal models. In Proceedings of the 31st International Conference on Computational Linguistics, pages 2886–2903, 2025.

28. Qiguang Chen, Libo Qin, Jin Zhang, Zhi Chen, Xiao Xu, and Wanxiang Che. M3cot: A novel benchmark for multi-domain multi-step multi-modal chain-of-thought. In Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 8199–8221, 2024. doi: 10.18653/v1/2024.acl-long.446.

29. Pan Lu, Swaroop Mishra, Tony Xia, Liang Qiu, Kai-Wei Chang, Song-Chun Zhu, Oyvind Tafjord, Peter Clark, and Ashwin Kalyan. Learn to explain: multimodal reasoning via thought chains for science question answering. In Proceedings of the 36th International Conference on Neural Information Processing Systems, pages 2507–2521, 2022.

30. Peng Wang, Shuai Bai, Sinan Tan, Shijie Wang, Zhihao Fan, Jinze Bai, Keqin Chen, Xuejing Liu, Jialin Wang, Wenbin Ge, et al. Qwen2-vl: Enhancing vision-language model’s perception of the world at any resolution. arXiv preprint arXiv:2409.12191, 2024.

31. Chameleon Team. Chameleon: Mixed-modal early-fusion foundation models. arXiv preprint arXiv:2405.09818, 2024.

## Appendix A. Training Data Construction

### A.1 Rationale for $N=4$ Training Stages

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In the IVT-LR training, we set the number of stages ($N$) to 4, which corresponds to three core reasoning steps ($N-1=3$). This design choice is not arbitrary; it is motivated by a statistical analysis of the native rationale lengths in the target datasets (M3CoT and ScienceQA).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在 IVT-LR 训练中，我们将阶段数（$N$）设为 4，对应三个核心推理步骤（$N-1=3$）。这一设计选择并非任意决定，而是由对目标数据集（M3CoT 和 ScienceQA）原生推理依据长度的统计分析所驱动。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> We first examined the distribution of rationale steps (segmented by sentence) in the two datasets. As shown in Figure 6, the median number of rationale steps for both datasets is around 10. Each subtask in the reasoning process usually requires about two to three sentences to complete a causal inference. Thus, a full rationale can be naturally divided into three major reasoning steps, each corresponding to a distinct subtask. Therefore, setting $N=4$ (three reasoning steps) provides a balanced and interpretable abstraction of the overall reasoning process.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 我们首先考察了两个数据集中推理依据步骤（按句子切分）的分布。如图 6 所示，两个数据集的推理依据步数中位数都约为 10。推理过程中的每个子任务通常需要大约两到三个句子来完成一次因果推断。因此，一条完整的推理依据可以自然划分为三个主要推理步骤，每个步骤对应一个不同的子任务。所以，将 $N=4$（三个推理步骤）设为阶段数，能够为整体推理过程提供一种平衡且可解释的抽象。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Moreover, the statistical analysis shows that over 70% of the samples in both datasets contain more than three reasoning steps, and their distributions are highly dispersed. This high dispersion mandates merging adjacent steps for standardization and enhanced computational efficiency. Critically, we simultaneously retain a portion of the original one- and two-step samples. This strategy is essential to preserve the model’s short reasoning ability and bolster generalization across varying reasoning depths, ensuring robust performance regardless of the input’s complexity.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 此外，统计分析表明，两个数据集中都有超过 70% 的样本包含三个以上的推理步骤，而且其分布高度分散。这种高度分散要求合并相邻步骤，以实现标准化并提高计算效率。至关重要的是，我们同时保留了部分原始的一步和两步样本。该策略对于保留模型的短程推理能力并增强其在不同推理深度上的泛化至关重要，可确保无论输入复杂度如何，模型都能保持稳健表现。

### Figure 6. Native rationale-step distribution / 原生推理依据步数分布

![Figure 6](assets/page_012_fig_figure_6.png)

**Caption:** Distribution of native rationale steps across the M3CoT and ScienceQA datasets.

**Caption[CN]:** M3CoT 和 ScienceQA 数据集中原生推理依据步数的分布。

| Dataset | Mean | Median | >3 steps |
|---|---:|---:|---:|
| ScienceQA | 10.56 | 10.00 | 74.3% |
| M3CoT | 9.23 | 8.00 | 92.6% |

### A.2 Examples of Merged Rationales

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Table 4 and 5 illustrates examples of consolidated rationales with step indices.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 表 4 和表 5 展示了带有步骤索引的合并推理依据示例。

### Table 4. Consolidated rationale example / 合并推理依据示例

![Table 4](assets/page_012_fig_table_4.png)

**Caption:** An example of consolidated rationales for clarity.

**Caption[CN]:** 为清楚说明而给出的合并推理依据示例。

| Field | Searchable original transcription | 中文对照 |
|---|---|---|
| Question | What is the purpose of the hairdryer in the adult’s hand? | 成人手中的吹风机有什么用途？ |
| Rationale | **Step 1:** According to the picture, the hair dryer in the adult’s hand is not pointed at the hair. This suggests it has other uses besides drying hair.<br><br>**Step 2:** There is a light ball in the air suggests that the air from the hairdryer is holding the ball up. Combined with the dancing little boy in the picture, this shows that the hairdryer is being used to entertain the little boy.<br><br>**Step 3:** Therefore, (C) “Entertaining the little boy” is the right answer. | **步骤 1：** 根据图片，成人手中的吹风机并没有朝向头发。这说明它除了吹干头发之外还有其他用途。<br><br>**步骤 2：** 空中有一个轻质球，这表明吹风机吹出的气流正把球托起来。结合图片中正在跳舞的小男孩，这说明吹风机被用来逗小男孩开心。<br><br>**步骤 3：** 因此，（C）“逗小男孩开心”是正确答案。 |

### Table 5. Consolidated rationale example / 合并推理依据示例

![Table 5](assets/page_012_fig_table_5.png)

**Caption:** Another example of consolidated rationales for clarity.

**Caption[CN]:** 另一个为清楚说明而给出的合并推理依据示例。

| Field | Searchable original transcription | 中文对照 |
|---|---|---|
| Question | What is the purpose of the metal pylon on the street near the brick apartment building? | 砖砌公寓楼附近街道上的金属路桩有什么用途？ |
| Rationale | **Step 1:** The metal pylon on the street indicates that cars are not allowed to drive in the pedestrian area. This inference is derived from the fact that the building next to it is an apartment building which suggests a residential area with high pedestrian traffic.<br><br>**Step 2:** Additionally, the presence of thick white stripes across the street indicates a pedestrian crosswalk. Therefore, it can be concluded that the metal pylon is placed to prevent any intrusion from cars into the area reserved for pedestrians.<br><br>**Step 3:** Therefore, option B is the correct answer. | **步骤 1：** 街道上的金属路桩表明汽车不得驶入步行区域。该推断来自这样一个事实：旁边的建筑是一栋公寓楼，这说明此处是行人流量很高的住宅区。<br><br>**步骤 2：** 此外，横跨街道的粗白色条纹表明这里有人行横道。因此可以得出结论：设置金属路桩是为了防止汽车闯入为行人保留的区域。<br><br>**步骤 3：** 因此，选项 B 是正确答案。 |
