# Interleaved-Modal Chain-of-Thought

> **中文题名：** 交错模态思维链  
> **作者：** Jun Gao, Yongqi Li, Ziqiang Cao, Wenjie Li  
> **出处：** arXiv:2411.19488v2，2025-03-17  
> **论文类型：** 方法 / training-free multimodal CoT prompting  
> **源文件：** `Gao 等 - 2025 - Interleaved-Modal Chain-of-Thought.pdf`  
> **阅读器：** 全文英中对照；源格式为 `pdf-text`；图表按首次实质讨论位置重排。页码与稳定块 ID 见 `source_map.json`。

## 阅读导航

- [术语表](#术语表)
- [Abstract](#abstract)
- [1. Introduction](#1-introduction)
- [2. Related Work](#2-related-work)
- [3. Methodology](#3-methodology)
- [4. Experiments](#4-experiments)
- [5. Case Study](#5-case-study)
- [6. Conclusion](#6-conclusion)
- [Supplementary Material](#supplementary-material)
- [Critical Reading Notes](#critical-reading-notes)

## 术语表

| Canonical term | 中文 | First-use definition / 决策 |
|---|---|---|
| Chain-of-Thought (CoT) | 思维链 | 生成最终答案前的中间推理步骤 |
| multimodal CoT | 多模态思维链 | 在视觉语言任务中使用中间推理 |
| text-only rationales | 纯文本理由 | 只用文字描述图像证据的中间步骤 |
| Interleaved-modal Chain-of-Thought (ICoT) | 交错模态思维链 | 中间步骤由视觉理由和文本理由配对组成 |
| Attention-driven Selection (ADS) | 注意力驱动选择 | 用 VLM attention map 选择原图局部 patch |
| visual rationales | 视觉理由 | 插入推理序列的原图局部视觉 token / patch |
| textual rationales | 文本理由 | 与视觉理由配对的自然语言推理文本 |
| Fine-grained Visual Information (FVI) | 细粒度视觉信息 | few-shot demonstration 中人工选择的局部视觉证据 |
| signal token | 信号 token | 触发 ADS 选择视觉 patch 的预定义 token |
| KV Cache copy | KV 缓存复制 | 试图用缓存复制替代重新插入视觉 token 的效率变体 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Chain-of-Thought prompting asks large language models to produce intermediate reasoning steps before the final answer. When this idea is transferred to vision-language models, however, text-only rationales have difficulty expressing fine-grained associations with the original image.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 思维链提示会要求大语言模型在给出最终答案前生成中间推理步骤。但当这一思想迁移到视觉语言模型时，纯文本理由很难准确表达与原图中细粒度视觉区域之间的关联。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The paper proposes Interleaved-modal Chain-of-Thought, or ICoT, an image-incorporated multimodal CoT format. ICoT generates sequential reasoning steps made of paired visual and textual rationales, and uses these interleaved steps to infer the final answer.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 论文提出 Interleaved-modal Chain-of-Thought，即 ICoT。它是一种把图像内容纳入中间推理过程的多模态思维链格式，每个推理步骤由视觉理由和文本理由配对组成，再通过这些交错步骤推导最终答案。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Current VLMs cannot fully generate fine-grained interleaved-modal content. Since the required visual information is usually already part of the input image, the authors propose Attention-driven Selection to realize ICoT over existing VLMs by inserting selected image regions into the reasoning sequence.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 现有 VLM 并不能完整生成这种细粒度交错模态内容。由于所需视觉信息通常已经存在于输入图像中，作者提出注意力驱动选择，用它在现有 VLM 上实现 ICoT：不生成新图，而是把原图中被选中的局部区域插入推理序列。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> ADS uses only VLM attention maps and requires no extra parameterization, so it is plug-and-play. Experiments on Chameleon and Qwen2-VL across three benchmarks show performance gains up to 14% and better interpretability compared with existing multimodal CoT prompting methods.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> ADS 只依赖 VLM 自身的注意力图，不需要额外参数，因此是即插即用策略。作者在 Chameleon 和 Qwen2-VL 两种架构、三个基准上实验，显示相较现有多模态思维链提示方法，ICoT 最高带来 14% 的性能提升，并增强推理可解释性。

## 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> CoT prompting improves LLM reasoning by eliciting a sequence of intermediate natural-language steps. It has been effective in arithmetic, commonsense, and symbolic reasoning, and has become an important route toward stronger reasoning systems.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 思维链提示通过诱导模型生成一系列自然语言中间步骤来增强 LLM 推理能力。它已在算术、常识和符号推理中表现有效，也成为构建更强推理系统的重要路径。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> As VLMs develop, multimodal CoT becomes important for vision-language reasoning. Existing methods usually train or prompt models to produce text-only rationales. CCoT uses scene graphs, DDCoT decomposes problems, and SCAFFOLD overlays coordinates, but the resulting reasoning steps still describe visual evidence only in text.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 随着 VLM 发展，多模态思维链成为视觉语言推理的重要方向。已有方法通常训练或提示模型生成纯文本理由。CCoT 使用场景图，DDCoT 分解问题，SCAFFOLD 叠加坐标网格，但这些中间步骤本质上仍只用文字描述视觉证据。

### Figure 1. 纯文本理由与交错模态理由

![Figure 1](Reasoning/TrainingFree/Interleaved-Modal%20Chain-of-Thought/assets/page_002_fig_figure_1.png)

**Caption:** Text-only rationales use rough position descriptions, while ICoT inserts selected image regions and pairs them with textual rationales.

**Caption[CN]:** 纯文本理由只能用粗略位置描述图像证据；ICoT 会插入被选择的图像局部区域，并将其与文本理由配对。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Figure 1 illustrates the central limitation. A text-only rationale may say “at the top,” but such a phrase is too coarse to uniquely associate words with fine-grained regions such as grapes, orange, banana, and apple. ICoT instead inserts the selected regions into the reasoning process.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Figure 1 展示了核心限制。纯文本理由可能说“在上方”，但这种表达太粗，无法把文字精确绑定到葡萄、橙子、香蕉、苹果等细粒度区域。ICoT 则把被选中的图像局部直接插入推理过程。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> ICoT is conceptually appealing but hard for current models. Perceiver-style VLMs such as Qwen2-VL understand images through visual embeddings but cannot generate multimodal outputs, while unified-modeling VLMs can generate multimodal content but do so at fixed resolution and show inertia toward multimodal generation.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> ICoT 在概念上很自然，但现有模型很难直接实现。Qwen2-VL 这类感知器式 VLM 通过视觉嵌入理解图像，却不能生成多模态输出；统一建模 VLM 虽能生成多模态内容，但通常固定分辨率，且存在不愿生成多模态内容的惯性。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> ADS avoids the need to generate images. At the beginning of each textual rationale, it uses the VLM attention map to select patches from the input image, inserts their visual tokens into the current generation sequence, and then resumes autoregressive text generation.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> ADS 绕开了生成图像的要求。在每个文本理由开始时，它用 VLM 的注意力图从输入图像中选择局部 patch，把这些视觉 token 插入当前生成序列，然后继续原本的自回归文本生成。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The authors evaluate ADS-based ICoT on Chameleon and Qwen2-VL using M3CoT, ScienceQA, and LLaVA-W. They claim three contributions: interleaved-modal CoT, a training-free ADS implementation, and empirical gains over existing multimodal CoT methods.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 作者在 Chameleon 和 Qwen2-VL 上，用 M3CoT、ScienceQA 和 LLaVA-W 评估基于 ADS 的 ICoT。论文贡献包括：提出交错模态思维链，提出免训练的 ADS 实现，并在实验上超过现有多模态思维链方法。

## 2. Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Most VLMs are built from a language model, a visual module, and a vision-language adapter. The visual encoder turns images into dense representations, the adapter converts them into LLM-readable visual tokens, and the LLM predicts the next token.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 大多数 VLM 由语言模型、视觉模块和视觉语言适配器组成。视觉编码器把图像转成稠密表示，适配器将其转换为 LLM 可读的视觉 token，最后由 LLM 执行下一个 token 预测。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Unified-modeling VLMs such as Chameleon, Unified-IO 2, and Emu3 tokenize images into discrete visual tokens and train on both vision and text. They are expected to improve multimodal understanding, but they still do not directly solve fine-grained interleaved rationale generation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> Chameleon、Unified-IO 2 和 Emu3 等统一建模 VLM 会把图像 token 化为离散视觉 token，并在视觉和文本信息上共同训练。它们有望提升多模态理解，但仍不能直接解决细粒度交错理由生成。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Existing multimodal CoT methods try to strengthen VLM reasoning with detailed descriptions, scene graphs, decomposed sub-questions, object marks, or coordinate overlays. Their common limitation is that the intermediate rationale remains text-only.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 现有多模态思维链方法通过详细描述、场景图、子问题分解、对象标记或坐标叠加来增强 VLM 推理。它们共同的限制是：中间理由仍然是纯文本。

## 3. Methodology

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The method section first formalizes ordinary VLM prediction and multimodal CoT, then defines ICoT, and finally introduces ADS as a plug-and-play realization for existing VLMs.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 方法部分先形式化普通 VLM 预测和多模态思维链，再定义 ICoT，最后提出 ADS 作为现有 VLM 上即插即用的实现方式。

### 3.1 Preliminaries

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> A standard VLM takes an image and instruction and directly predicts an answer:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 标准 VLM 接收图像和指令，并直接预测答案：

$$
answer = VLM(Image, Instruction).
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Multimodal CoT adds a prompt so that the VLM generates intermediate textual rationales before the answer:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 多模态思维链额外加入提示，使 VLM 在答案前生成中间文本理由：

$$
r_1, r_2, ..., answer = VLM(Prompt, Image, Instruction).
$$

### 3.2 Interleaved-modal Chain-of-Thought

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> ICoT replaces text-only intermediate steps with paired image and textual rationales. The visual rationale is a fine-grained crop or visual-token subset from the original image, and it is interleaved with the following textual rationale.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> ICoT 用图像理由和文本理由的配对替代纯文本中间步骤。视觉理由是原图中的细粒度局部或视觉 token 子集，并与随后的文本理由交错出现。

$$
r_1, x^v_1, r_2, x^v_2, ..., answer = VLM(Prompt, Image, Instruction).
$$

### 3.3 Attention-driven Selection

### Figure 2. ADS 工作流

![Figure 2](assets/page_004_fig_figure_2.png)

**Caption:** ADS uses signal-token attention over visual tokens to select fine-grained visual information and insert it before generating the next textual rationale.

**Caption[CN]:** ADS 使用信号 token 对视觉 token 的注意力来选择细粒度视觉信息，并在生成下一个文本理由前插入这些信息。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> ADS turns image generation into image selection. The VLM caches visual tokens extracted by its visual encoder. When the model emits a predefined signal token $S$, ADS is triggered:

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> ADS 把图像生成问题改成图像选择问题。VLM 先缓存视觉编码器提取的视觉 token。当模型生成预定义信号 token $S$ 时，ADS 被触发：

$$
do\ selection =
\begin{cases}
True, & predicted\ tokens[-1]=S,\\
False, & otherwise.
\end{cases}
$$

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> ADS averages the attention between the signal token and visual tokens across layers, takes the Top-K visual tokens, restores their relative spatial order, and concatenates them with the predicted text embeddings.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> ADS 会跨层平均信号 token 与视觉 token 之间的注意力，选择 Top-K 视觉 token，恢复它们在原图中的相对空间顺序，再与已生成文本的嵌入拼接。

$$
V_{selected}=\{f_v[i]\mid i\in TopK(A_t,n)\}.
$$

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> After obtaining $V_{selected}$, the VLM continues generation with the concatenated multimodal context:

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 得到 $V_{selected}$ 后，VLM 在拼接后的多模态上下文上继续生成：

$$
next\ token = VLM(Cat(predicted\ tokens, V_{selected})).
$$

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> In zero-shot ICoT, the method can inherit ordinary CoT instructions such as “Let’s think step by step.” In few-shot ICoT, each demonstration consists of an image, textual rationales, and visual rationales.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 在 zero-shot ICoT 中，方法可以继承普通 CoT 的提示，例如“Let’s think step by step”。在 few-shot ICoT 中，每个示例由图像、文本理由和视觉理由组成。

## 4. Experiments

### 4.1 Datasets and Baselines

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> M3CoT focuses on multi-domain, multi-step multimodal reasoning. It contains 267 categories from science, mathematics, and commonsense, and its rationales average 293 tokens, making it suitable for testing fine-grained visual information.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> M3CoT 关注多领域、多步多模态推理，包含科学、数学和常识领域的 267 个类别。其理由平均长度为 293 个 token，因此适合测试细粒度视觉信息是否真正有用。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> ScienceQA provides a general reasoning benchmark, while LLaVA-W evaluates detailed long-form visual answers whose references are produced by GPT-4V. The baselines are No-CoT, Multimodal CoT, CCoT, DDCoT, and SCAFFOLD.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> ScienceQA 提供通用推理评测，LLaVA-W 评估详细长答案，其参考答案由 GPT-4V 产生。对比方法包括 No-CoT、Multimodal CoT、CCoT、DDCoT 和 SCAFFOLD。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The method is implemented on Chameleon-7B and Qwen2-VL-7B-Instruct. The signal token is the newline token by default. ADS selects visual tokens at a granularity of 64; for Qwen2-VL the practical number is set to 16 due to its merge mechanism.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 方法在 Chameleon-7B 和 Qwen2-VL-7B-Instruct 上实现。默认信号 token 是换行符。ADS 按 64 的粒度选择视觉 token；由于 Qwen2-VL 有 merge 机制，实际选择数量设为 16。

### Table 1. 主结果

![Table 1](Reasoning/TrainingFree/Interleaved-Modal%20Chain-of-Thought/assets/page_006_fig_table_1.png)

**Caption:** ICoT outperforms baselines on Chameleon and Qwen2-VL under zero-shot and one-shot settings.

**Caption[CN]:** ICoT 在 Chameleon 和 Qwen2-VL 上，在 zero-shot 与 one-shot 设置中均超过基线。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> On Chameleon-7B, ICoT reaches 29.8 / 51.0 / 25.2 in zero-shot M3CoT, ScienceQA, and LLaVA-W, and 32.3 / 53.4 / 27.6 in one-shot. The largest relative gain is 14.0% on LLaVA-W zero-shot and 11.7% on LLaVA-W one-shot.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在 Chameleon-7B 上，ICoT 在 zero-shot 的 M3CoT、ScienceQA、LLaVA-W 上达到 29.8 / 51.0 / 25.2，在 one-shot 上达到 32.3 / 53.4 / 27.6。最大相对提升来自 LLaVA-W：zero-shot 为 14.0%，one-shot 为 11.7%。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> On Qwen2-VL-7B, ICoT reaches 44.1 / 56.8 / 34.2 in zero-shot and 46.0 / 65.4 / 35.7 in one-shot. The gains are smaller than on Chameleon but remain consistent across benchmarks.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 在 Qwen2-VL-7B 上，ICoT 在 zero-shot 达到 44.1 / 56.8 / 34.2，在 one-shot 达到 46.0 / 65.4 / 35.7。提升幅度小于 Chameleon，但在三个基准上保持一致。

### Table 2. 消融结果

![Table 2](Reasoning/TrainingFree/Interleaved-Modal%20Chain-of-Thought/assets/page_007_fig_table_2.png)

**Caption:** Removing ADS or fine-grained visual information degrades one-shot ICoT on Chameleon-7B.

**Caption[CN]:** 移除 ADS 或示例中的细粒度视觉信息，都会降低 Chameleon-7B 上 one-shot ICoT 的性能。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Table 2 shows that ICoT obtains 32.3 / 53.4 / 27.6 on M3CoT, ScienceQA, and LLaVA-W. Removing ADS drops the scores to 29.2 / 52.4 / 24.5; removing FVI drops them to 30.6 / 52.8 / 25.9; removing both drops them to 29.1 / 51.0 / 23.0.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> Table 2 显示 ICoT 在 M3CoT、ScienceQA、LLaVA-W 上得到 32.3 / 53.4 / 27.6。去掉 ADS 后降为 29.2 / 52.4 / 24.5；去掉 FVI 后降为 30.6 / 52.8 / 25.9；两者都去掉后降为 29.1 / 51.0 / 23.0。

### Table 3 and Table 4. KV 缓存与 demonstration 设计

![Table 3](assets/page_007_fig_table_3.png)

**Caption:** Copying KV Cache is cheaper but slightly worse than inserting selected visual patches.

**Caption[CN]:** 复制 KV 缓存更省计算，但性能略低于直接插入被选中的视觉 patch。

![Table 4](assets/page_007_fig_table_4.png)

**Caption:** Human-written demonstrations outperform model-written demonstrations.

**Caption[CN]:** 人工设计的 demonstration 优于模型自动生成的 demonstration。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> KV-Copy is consistently lower than ICoT: for example, in one-shot it reaches 31.5 / 52.9 / 27.0, while ICoT reaches 32.3 / 53.4 / 27.6. The authors explain that copied KV cache makes visual information position-agnostic and weakens the intended interleaving.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> KV-Copy 始终略低于 ICoT：例如 one-shot 下它为 31.5 / 52.9 / 27.0，而 ICoT 为 32.3 / 53.4 / 27.6。作者认为复制 KV 缓存会让视觉信息变得位置无关，从而削弱交错模态理由的设计初衷。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Human-written demonstrations also outperform model-written ones. The authors attribute this to the difficulty of forming a continuous sub-image through ADS; discrete patches may introduce extra noise.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 人工写的 demonstration 也优于模型自动生成的版本。作者认为原因在于：通过 ADS 形成连续子图并不容易，离散 patch 可能引入额外噪声。

## 5. Case Study

### Figure 3. 三类文本理由失败案例

![Figure 3](assets/page_008_fig_figure_3.png)

**Caption:** ICoT improves over text-only rationales in cases of misunderstanding, overgeneralization, and hallucination.

**Caption[CN]:** ICoT 在误解、过度泛化和幻觉三类文本理由失败案例中优于纯文本思维链。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The case study shows three typical failures of text-only rationales. In one case, text-only CoT misidentifies different objects as colored pencils even when the final answer is correct. ICoT first recognizes the actual objects and then infers their common property.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> case study 展示了纯文本理由的三类典型失败。第一个例子中，纯文本 CoT 把不同对象误认为彩色铅笔，即使最终答案碰巧正确；ICoT 则先识别真实对象，再推断共同属性。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In another example, text-only CoT overgeneralizes from a person flying a kite to a kite festival. ICoT uses selected visual evidence to notice kites in the sky and infer that the scene is windy. The third example shows hallucination caused by relying too much on language priors.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 另一个例子中，纯文本 CoT 从“有人放风筝”过度泛化为“风筝节”；ICoT 借助被选中的视觉证据注意到空中风筝，从而推断天气有风。第三个例子展示了过度依赖语言先验导致的幻觉。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The paper also notes a downside: ADS is triggered by a predefined signal token. If this token is generated too frequently, the model may insert patches too often and produce low-quality responses.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 论文也指出一个风险：ADS 由预定义信号 token 触发。如果该 token 出现过于频繁，模型可能过度插入 patch，导致回复质量下降。

## 6. Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper proposes ICoT, which generates interleaved-modal rationales for final-answer inference, and ADS, a parameter-free strategy that selects optimal image patches from attention maps.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文提出 ICoT，通过交错模态理由进行最终答案推理；同时提出 ADS，用无参数方式从注意力图中选择最合适的图像 patch。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Experiments on Chameleon-7B and Qwen2-VL-7B-Instruct show substantial gains over existing multimodal CoT methods. The authors also explore KV-cache copying as a more efficient but slightly weaker implementation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在 Chameleon-7B 和 Qwen2-VL-7B-Instruct 上的实验显示，ICoT 明显超过现有多模态思维链方法。作者还探索了 KV 缓存复制作为更高效但略弱的实现。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The authors acknowledge remaining limitations: ADS needs attention-score storage, which brings extra memory overhead, and the fixed number of selected patches is suboptimal. They plan to use segmentation or grounding techniques for a more robust ICoT implementation.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 作者承认仍有局限：ADS 需要存储注意力分数，带来额外显存开销；固定选择 patch 数量也不是最优。未来可结合分割或 grounding 技术，使 ICoT 实现更稳健。

## Supplementary Material

### Figure 4. patch 数量敏感性

![Figure 4](assets/page_011_fig_figure_4.png)

**Caption:** ICoT is sensitive to the number of selected patches; 64 selected patches is relatively better in the reported validation experiments.

**Caption[CN]:** ICoT 对选择 patch 数量敏感；在报告的验证实验中，选择 64 个 patch 相对更好。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The supplementary material studies the number of selected patches. Too many selected patches are dispersed and noisy; too few may miss necessary fine-grained information. The authors report that $n=64$ works relatively well.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 补充材料分析了被选 patch 的数量。选择太多会分散且引入噪声，选择太少又可能缺失必要细粒度信息。作者报告 $n=64$ 相对更好。

### Table 5. 一般任务是否退化

![Table 5](Reasoning/TrainingFree/Interleaved-Modal%20Chain-of-Thought/assets/page_011_fig_table_5.png)

**Caption:** ICoT also improves captioning and VQA in the reported one-shot general benchmarks.

**Caption[CN]:** 在报告的 one-shot 一般基准上，ICoT 对 captioning 和 VQA 也有提升。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> On Flickr30k and OKVQA, Chameleon improves from 22.3 to 23.6 CIDEr and from 26.2 to 28.2 VQA accuracy after adding ICoT, suggesting that ICoT does not obviously hurt weaker-reasoning tasks in this limited test.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在 Flickr30k 和 OKVQA 上，加入 ICoT 后 Chameleon 从 22.3 提升到 23.6 CIDEr，从 26.2 提升到 28.2 VQA 准确率。这说明在该有限测试中，ICoT 没有明显伤害弱推理任务。

## Critical Reading Notes

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> ICoT is best read as a test-time visual-evidence insertion strategy, not as a new model. Its core contribution is to make intermediate reasoning steps visually grounded by inserting selected visual tokens from the original image.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> ICoT 最适合理解为一种测试时视觉证据插入策略，而不是新模型。它的核心贡献是从原图中选取视觉 token 并插入中间推理步骤，让推理过程更视觉落地。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The most important evidence is not only the main-table gain, but the ablation showing that both ADS and fine-grained visual information in demonstrations are necessary. This supports the claim that the inserted visual evidence is doing real work.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 最重要的证据不只是主表涨点，而是消融表明 ADS 和 demonstration 中的细粒度视觉信息都必要。这支持“插入的视觉证据确实在起作用”这一主张。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The main caveat is that ADS uses a simple signal-token trigger and a fixed number of selected patches. This makes the method elegant and training-free, but also brittle when the model emits signal tokens too often or when the needed visual region has variable size.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 主要风险在于 ADS 使用简单的信号 token 触发，并固定选择 patch 数。这让方法简洁且免训练，但当模型过于频繁地产生信号 token，或目标视觉区域大小变化很大时，方法会变脆。

## References

References are retained in the source PDF and indexed in `source_map.json`. This reader focuses on the main paper argument, method, figures, tables, experiments, and supplementary results rather than translating every bibliography entry line by line.

参考文献保留在源 PDF 中，并已在 `source_map.json` 中记录。本阅读器重点翻译主文论证、方法、图表、实验和补充结果，不逐条翻译参考文献。
