# Mitigating Low-Quality Reasoning in MLLMs: Self-Driven Refined Multimodal CoT with Selective Thinking and Step-wise Visual Enhancement

> **中文题名：** 缓解 MLLM 中的低质量推理：带选择性思考与逐步视觉增强的自驱精炼多模态思维链  
> **作者：** Chongjun Tu, Peng Ye, Dongzhan Zhou, Tao Chen, Wanli Ouyang  
> **出处：** Proceedings of the AAAI Conference on Artificial Intelligence, 2026  
> **DOI：** 10.1609/aaai.v40i12.37919  
> **论文类型：** 方法 / training-free multimodal CoT / selective thinking / attention-level visual enhancement  
> **源文件：** `Mitigating Low-Quality Reasoning in MLLMs Self-Driven Refined Multimodal CoT with Selective Thinkin.pdf`  
> **阅读器：** 9 页完整英中对照详细阅读稿；覆盖公式 (1)–(4)、Figures 1–5、Tables 1–2、四模型八基准结果、致谢与完整可检索参考文献。

## Page / Section Index

- Abstract: page 1
- 1. Introduction: pages 1-3
- 2. Related Work: pages 3-4
- 3. Method: pages 4-6
- 4. Experiments: pages 6-7
- 5. Conclusion: pages 7-8
- References: pages 8-9

## Terminology Ledger

| Canonical term | 中文 | First-use decision |
|---|---|---|
| Multimodal Large Language Models (MLLMs) | 多模态大语言模型 | 保留 MLLM 缩写 |
| Multimodal Chain-of-Thought (MCoT) | 多模态思维链 | 保留 MCoT 缩写 |
| Self-Driven Refined Multimodal CoT (SDR-MCoT) | 自驱精炼多模态思维链 | 保留 SDR-MCoT 缩写 |
| Selective Thinking | 选择性思考 | 指按不确定性决定是否展开长推理 |
| Step-wise Visual Enhancement | 逐步视觉增强 | 指每个推理步骤的视觉注意力增强 |
| first-token entropy | 首标记熵 | 用直接回答的第一个生成标记估计难度 |
| relative attention | 相对注意力 | 用注意力差异突出任务相关视觉区域 |
| attention sink | 注意力汇点 | 与任务无关但吸收注意力的孤立区域 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Multimodal Large Language Models have become increasingly capable, but existing multimodal chain-of-thought methods often produce low-quality reasoning. Two common failure modes are unnecessary reasoning for simple queries and inefficient visual information use for difficult queries.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 多模态大语言模型的能力不断增强，但现有多模态思维链方法仍常产生低质量推理。两个典型失败模式是：简单问题被迫展开不必要推理，复杂问题又不能高效利用视觉信息。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The paper observes that MLLMs already possess latent abilities to distinguish simple from difficult queries and to enhance task-related visual information. These abilities, however, are not fully activated by standard prompting.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 论文观察到，MLLM 本身已经具备区分简单与困难问题、并增强任务相关视觉信息的潜在能力。但标准提示并没有充分激活这些能力。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> To address this, the authors propose SDR-MCoT, a training-free framework with Selective Thinking and Step-wise Visual Enhancement. It first decides whether a question needs step-by-step reasoning, then strengthens relevant visual evidence during each reasoning step.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 为此，作者提出 SDR-MCoT，一个免训练框架，包含选择性思考与逐步视觉增强。它先判断问题是否需要逐步推理，再在每个推理步骤强化相关视觉证据。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Experiments on eight benchmarks and several MLLMs show that SDR-MCoT improves average accuracy by more than 6% on Qwen2-VL-7B while reducing token consumption by about 60% compared with zero-shot CoT.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在八个基准和多个 MLLM 上的实验显示，相比零样本 CoT，SDR-MCoT 在 Qwen2-VL-7B 上平均准确率提升超过 6%，同时生成标记消耗减少约 60%。

## 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Chain-of-thought prompting has improved reasoning in language models, and multimodal CoT extends this idea to vision-language tasks by encouraging the model to reason step by step before answering.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 思维链提示提升了语言模型的推理能力，多模态 CoT 则把这一思想扩展到视觉语言任务，让模型在回答前先逐步推理。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Yet multimodal CoT is not always beneficial. When a query is easy, forcing a long rationale can introduce noise, delay, and even wrong intermediate assumptions.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 但多模态 CoT 并不总是有益。对于简单问题，强迫模型生成长理由可能引入噪声、增加延迟，甚至产生错误的中间假设。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> When a query is difficult, the opposite problem appears: the model may generate text-heavy reasoning while failing to keep attention on the visual evidence needed for the answer.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 对于困难问题，则会出现相反的问题：模型生成大量文本推理，却没有持续关注回答所需的视觉证据。

### Figure 1. Motivation of SDR-MCoT

![Figure 1](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/assets/page_001_fig_figure_1.png)

**Caption:** Simple questions benefit from direct answers, while difficult questions need step-by-step reasoning with visual evidence enhancement.

**Caption[CN]:** 简单题更适合直接回答，困难题则需要带视觉证据增强的逐步推理。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The paper calls these failures low-quality reasoning. The key insight is that improving MCoT is not simply a matter of making the reasoning longer; the model must decide when to reason and how to use vision while reasoning.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 论文把这些失败称为低质量推理。核心洞察是，改进 MCoT 不是简单让推理变长；模型必须决定何时推理，以及推理时如何使用视觉信息。

### Figure 2. Overthinking and Visual Underuse

![Figure 2](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/assets/page_002_fig_figure_2.png)

**Caption:** The paper contrasts unnecessary reasoning on easy samples with insufficient visual grounding on difficult samples.

**Caption[CN]:** 论文对比了简单样本上的过度思考，以及困难样本上视觉落地不足的问题。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> SDR-MCoT is designed as a self-driven refinement process. It does not train a new model; instead, it uses the model's own uncertainty and attention patterns to control reasoning.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> SDR-MCoT 被设计为一种自驱精炼流程。它不训练新模型，而是利用模型自身的不确定性与注意力模式来控制推理。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The two modules have different roles. Selective Thinking reduces unnecessary reasoning, and Step-wise Visual Enhancement improves grounding when reasoning is needed.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 两个模块承担不同角色。选择性思考减少不必要推理，逐步视觉增强则在需要推理时改善视觉落地。

## 2. Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Related work includes general MLLMs, multimodal chain-of-thought prompting, and recent methods that insert visual evidence or guide visual reasoning during inference.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 相关工作包括通用 MLLM、多模态思维链提示，以及近期在推理中插入视觉证据或引导视觉推理的方法。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Many multimodal CoT methods assume that longer reasoning is helpful, but the authors argue that this assumption breaks down when the question is already easy or when the generated rationale drifts away from the image.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 许多多模态 CoT 方法默认更长推理更有用，但作者认为，当问题本身很简单，或者生成理由偏离图像时，这一假设会失效。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Compared with approaches that add visual crops or extra image tokens, SDR-MCoT aims to preserve token efficiency by modifying attention during reasoning rather than expanding the visual context.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 相比加入视觉裁剪或额外图像标记的方法，SDR-MCoT 希望通过修改推理中的注意力来保持标记效率，而不是扩大视觉上下文。

## 3. Method

### Figure 3. SDR-MCoT Framework

![Figure 3](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/assets/page_004_fig_figure_3.png)

**Caption:** SDR-MCoT first performs entropy-based route selection, then applies visual enhancement during step-by-step reasoning for difficult samples.

**Caption[CN]:** SDR-MCoT 先用熵进行路径选择，再对困难样本的逐步推理过程做视觉增强。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The method begins with a direct-answer prompt. The model is asked to answer using a single word or phrase, and the entropy of the first generated token is computed from the logits.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 方法从直接回答提示开始。模型被要求用一个词或短语回答，并从输出 logits 中计算第一个生成标记的熵。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Given vocabulary size $V$, logits $z_i$, and generation temperature $T$, the first-token entropy and token probabilities are:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 给定词表大小 $V$、logit $z_i$ 与生成温度 $T$，第一个生成 token 的熵及其概率为：

$$
H=-\sum_{i=1}^{V}p_i\log p_i,\qquad p_i=\frac{\exp(z_i/T)}{\sum_{j=1}^{V}\exp(z_j/T)}. \tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Entropy is computed from one forward pass under the exact instruction `Answer the question using a single word or phrase.` Samples are sorted by entropy into ten equal-size groups; lower entropy strongly correlates with higher accuracy.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 熵由精确指令 `Answer the question using a single word or phrase.` 下的一次前向传播计算。样本按熵排序并分为十个等规模组；熵越低，准确率整体越高。英文字面量保持原样。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> If $H<\theta$, the model's direct-answer distribution is considered confident and the system returns the direct answer. If $H\geq\theta$, the sample is routed into step-by-step reasoning.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 若 $H<\theta$，说明模型的直接回答分布足够自信，系统返回直接答案。若 $H\geq\theta$，样本会进入逐步推理。

$$
\mathrm{Strategy}=\begin{cases}
\text{Direct Answer}, & H<\theta,\\
\text{Step-by-Step Reasoning}, & H\geq\theta.
\end{cases} \tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The threshold $\theta$ is estimated adaptively from a small sampled subset by averaging entropy values, rather than fixed as a universal constant.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 阈值 $\theta$ 不是固定通用常数，而是从一个小采样子集的平均熵中自适应估计。

### Figure 4. Correlation between entropy and performance

**Caption:** On Qwen2-VL-7B/M³CoT, ten equal-size entropy groups have centers `0.00, 0.03, 0.15, 0.37, 0.59, 0.74, 0.88, 1.01, 1.15, 1.31` and approximate accuracies `0.97, 0.92, 0.79, 0.59, 0.52, 0.46, 0.39, 0.28, 0.30, 0.24`. No clean standalone asset exists; all searchable values are retained here.

**Caption[CN]:** 在 Qwen2-VL-7B/M³CoT 上，十个等规模熵分组的中心为 `0.00, 0.03, 0.15, 0.37, 0.59, 0.74, 0.88, 1.01, 1.15, 1.31`，近似准确率为 `0.97, 0.92, 0.79, 0.59, 0.52, 0.46, 0.39, 0.28, 0.30, 0.24`。没有干净独立素材，因此在此保留全部可检索数值。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Step-wise Visual Enhancement is applied only when the sample is routed to CoT. It aims to strengthen image patches that are relevant to the current reasoning step without creating extra generated tokens.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 逐步视觉增强只在样本进入 CoT 后使用。它的目标是在不产生额外生成标记的前提下，强化与当前推理步骤相关的图像 patch。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> For multiple-choice questions, the paper computes attention with answer options and attention without answer options. Their relative pattern helps remove option-induced noise and boundary-biased attention.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 对多选题，论文分别计算带选项的注意力和不带选项的注意力。二者的相对模式有助于去除选项诱导噪声和边界注意力偏置。

### Figure 5. Relative Attention

![Figure 5](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/assets/page_005_fig_figure_5.png)

**Caption:** Option-aware attention can be dispersed; option-free attention can contain edge bias; relative attention focuses more cleanly on task-relevant regions.

**Caption[CN]:** 带选项注意力可能分散，不带选项注意力可能有边界偏置；相对注意力能更干净地聚焦任务相关区域。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> At each reasoning step, SDR-MCoT combines the current attention map with the relative attention map by element-wise amplification.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 在每个推理步骤，SDR-MCoT 将当前注意力图与相对注意力图做逐元素放大组合。

$$
A_{\mathrm{amp}}=A_{\mathrm{curr}}\odot A_{\mathrm{rel}}. \tag{3}
$$

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> The amplified map is filtered by morphological erosion to remove isolated attention-sink points. The remaining high-attention patches are selected as task-related visual evidence.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 放大后的注意力图会经过形态学腐蚀，以移除孤立的注意力汇点。剩余高注意力 patch 被选为任务相关视觉证据。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> The selected visual patches then receive a multiplicative attention enhancement factor. The post-softmax attention distribution is renormalized so that the total attention mass remains valid.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 被选中的视觉 patch 随后获得乘法式注意力增强因子。增强发生在 softmax 后，并重新归一化，使总注意力质量保持有效。

$$
a'_k=\begin{cases}
\displaystyle \frac{\alpha a_k}{\sum_{i\notin S}a_i+\sum_{j\in S}\alpha a_j}, & k\in S,\\
\displaystyle \frac{a_k}{\sum_{i\notin S}a_i+\sum_{j\in S}\alpha a_j}, & k\notin S.
\end{cases}\qquad \sum_k a'_k=1. \tag{4}
$$

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> The four stages are region amplification, morphological erosion of isolated attention sinks, adaptive token selection from remaining high-attention patches, and post-softmax enhancement by factor $\alpha$ with normalization.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 四个阶段依次为：区域放大、腐蚀孤立注意力汇点、根据剩余高注意力 patch 自适应选择 token，以及在 softmax 后乘以 $\alpha$ 并归一化。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> This design differs from visual-token insertion methods. SDR-MCoT does not add image crops or extra tokens; it changes how much the current decoding step attends to the already available visual tokens.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> 这一设计不同于视觉标记插入方法。SDR-MCoT 不添加图像裁剪或额外标记，而是改变当前解码步骤对已有视觉标记的关注强度。

## 4. Experiments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The experiments cover eight benchmarks: M3CoT, CoMT, ScienceQA, MMStar, A-OKVQA, V*, HallusionBench, and MathVista.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 实验覆盖八个基准：M3CoT、CoMT、ScienceQA、MMStar、A-OKVQA、V*、HallusionBench 与 MathVista。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The evaluated backbones include Qwen2-VL-7B, InternVL3-8B, LLaVA-1.5-7B, and LLaVA-1.5-13B. Baselines include No CoT, CoT, DDCoT, MMCoT, CCoT, and ICoT.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 评测骨干包括 Qwen2-VL-7B、InternVL3-8B、LLaVA-1.5-7B 和 LLaVA-1.5-13B。基线包括 No CoT、CoT、DDCoT、MMCoT、CCoT 与 ICoT。

### Table 1. Main Results

![Table 1](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/assets/page_006_fig_table_1.png)

**Caption:** SDR-MCoT improves average accuracy while using fewer generated tokens than most CoT-style baselines.

**Caption[CN]:** SDR-MCoT 提升平均准确率，同时比大多数 CoT 式基线消耗更少生成标记。

| Base model | Method | Tokens | M³CoT | CoMT | ScienceQA | MMStar | A-OKVQA | V* | HalBench | MathVista | Avg. |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Qwen2-VL-7B | No CoT | 35.54 | 46.81 | 28.08 | 76.15 | 51.22 | 83.12 | 68.06 | 65.34 | 53.2 | 59.00 |
| Qwen2-VL-7B | CoT | 172.08 | 45.90 | 28.37 | 72.19 | 53.62 | 80.02 | 67.54 | 63.76 | 47.3 | 57.34 |
| Qwen2-VL-7B | DDCoT | 760.41 | 53.36 | 31.35 | 76.25 | 51.52 | 81.04 | 62.75 | 65.54 | 50.5 | 59.04 |
| Qwen2-VL-7B | MMCoT | 189.15 | 54.01 | 31.56 | 78.83 | 55.08 | 85.21 | 70.16 | 66.14 | 53.0 | 61.75 |
| Qwen2-VL-7B | CCoT | 920.35 | 50.65 | 27.67 | 69.41 | 52.79 | 70.42 | 67.02 | 66.44 | 54.0 | 57.30 |
| Qwen2-VL-7B | ICoT | 237.54 | 46.50 | 29.30 | 72.46 | 53.47 | 79.72 | 68.59 | 65.87 | 49.1 | 58.13 |
| Qwen2-VL-7B | SDR-MCoT | 67.94 | 56.17 | 32.39 | 81.01 | 56.39 | 86.67 | 70.68 | 69.12 | 57.1 | 63.69 |
| InternVL3-8B | No CoT | 65.40 | 56.54 | 45.95 | 92.58 | 66.58 | 87.95 | 74.73 | 80.09 | 57.8 | 70.28 |
| InternVL3-8B | CoT | 224.46 | 47.90 | 44.39 | 89.24 | 65.07 | 83.67 | 70.37 | 78.97 | 47.6 | 65.90 |
| InternVL3-8B | DDCoT | 1839.78 | 60.82 | 42.69 | 90.50 | 63.27 | 85.31 | 64.25 | 76.96 | 66.0 | 68.73 |
| InternVL3-8B | MMCoT | 406.92 | 61.52 | 45.40 | 91.42 | 66.67 | 88.47 | 73.37 | 76.46 | 63.8 | 70.89 |
| InternVL3-8B | CCoT | 1077.70 | 52.00 | 40.82 | 86.02 | 65.13 | 84.72 | 70.43 | 74.72 | 57.2 | 66.38 |
| InternVL3-8B | ICoT | 511.57 | 48.60 | 39.55 | 85.55 | 44.00 | 73.97 | 72.61 | 75.00 | 32.2 | 58.94 |
| InternVL3-8B | SDR-MCoT | 100.33 | 61.25 | 46.21 | 95.38 | 67.00 | 89.09 | 75.81 | 79.78 | 68.4 | 72.87 |
| LLaVA-1.5-7B | No CoT | 11.76 | 39.01 | 26.24 | 59.87 | 33.06 | 77.09 | 43.98 | 45.96 | 23.1 | 43.54 |
| LLaVA-1.5-7B | CoT | 104.77 | 37.75 | 23.06 | 61.62 | 31.91 | 73.99 | 40.57 | 49.27 | 24.5 | 42.83 |
| LLaVA-1.5-7B | DDCoT | 832.25 | 34.95 | 24.79 | 53.41 | 30.33 | 68.99 | 42.41 | 49.55 | 23.5 | 40.99 |
| LLaVA-1.5-7B | MMCoT | 169.64 | 35.29 | 24.89 | 55.47 | 32.61 | 73.70 | 37.37 | 42.51 | 23.2 | 40.63 |
| LLaVA-1.5-7B | CCoT | 1112.41 | 37.85 | 25.25 | 59.65 | 32.15 | 76.24 | 39.47 | 51.23 | 23.5 | 43.17 |
| LLaVA-1.5-7B | ICoT | 148.82 | 38.55 | 23.26 | 62.38 | 35.16 | 76.22 | 43.98 | 52.22 | 23.2 | 44.37 |
| LLaVA-1.5-7B | SDR-MCoT | 59.40 | 40.15 | 27.90 | 62.65 | 35.51 | 78.51 | 44.62 | 51.93 | 25.2 | 45.81 |
| LLaVA-1.5-13B | No CoT | 23.58 | 36.28 | 24.83 | 66.63 | 33.27 | 81.64 | 46.07 | 53.24 | 29.2 | 46.40 |
| LLaVA-1.5-13B | CoT | 114.24 | 36.18 | 24.28 | 62.47 | 33.69 | 78.56 | 46.25 | 49.89 | 23.9 | 44.15 |
| LLaVA-1.5-13B | DDCoT | 818.94 | 37.50 | 24.33 | 64.40 | 34.88 | 77.23 | 45.55 | 45.75 | 23.8 | 44.18 |
| LLaVA-1.5-13B | MMCoT | 268.81 | 37.41 | 26.96 | 62.17 | 34.68 | 75.38 | 49.17 | 47.65 | 26.6 | 45.00 |
| LLaVA-1.5-13B | CCoT | 1012.06 | 36.01 | 27.33 | 66.98 | 35.53 | 80.49 | 44.50 | 57.96 | 25.8 | 46.20 |
| LLaVA-1.5-13B | ICoT | 197.34 | 37.80 | 26.11 | 62.38 | 34.96 | 78.61 | 43.83 | 52.34 | 23.9 | 44.99 |
| LLaVA-1.5-13B | SDR-MCoT | 63.76 | 39.31 | 27.37 | 67.56 | 36.01 | 84.23 | 49.44 | 55.03 | 29.6 | 48.57 |

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> On Qwen2-VL-7B, SDR-MCoT reaches an average accuracy of 63.69, compared with 59.00 for No CoT, 57.34 for CoT, and 61.75 for MMCoT.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在 Qwen2-VL-7B 上，SDR-MCoT 的平均准确率为 63.69，而 No CoT 为 59.00，CoT 为 57.34，MMCoT 为 61.75。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The token cost is also much lower. In the Qwen2-VL-7B setting, SDR-MCoT uses 67.94 generated tokens on average, compared with 172.08 for CoT, 760.41 for DDCoT, 189.15 for MMCoT, 920.35 for CCoT, and 237.54 for ICoT.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 生成标记成本也明显更低。在 Qwen2-VL-7B 设置下，SDR-MCoT 平均使用 67.94 个生成标记，而 CoT 为 172.08，DDCoT 为 760.41，MMCoT 为 189.15，CCoT 为 920.35，ICoT 为 237.54。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> On InternVL3-8B, SDR-MCoT improves average accuracy to 72.87, above No CoT at 70.28, CoT at 65.90, and MMCoT at 70.89.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 在 InternVL3-8B 上，SDR-MCoT 的平均准确率提升到 72.87，高于 No CoT 的 70.28、CoT 的 65.90 和 MMCoT 的 70.89。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> On LLaVA-1.5-7B and LLaVA-1.5-13B, SDR-MCoT also improves the average score over No CoT, reaching 45.81 and 48.57 respectively.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 在 LLaVA-1.5-7B 和 LLaVA-1.5-13B 上，SDR-MCoT 也超过 No CoT，平均分分别达到 45.81 和 48.57。

### Table 2. Ablation

![Table 2](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/assets/page_007_fig_table_2.png)

**Caption:** Selective Thinking mainly reduces tokens; Visual Enhancement mainly improves accuracy; the full method combines both effects.

**Caption[CN]:** 选择性思考主要减少标记，视觉增强主要提升准确率；完整方法同时获得两种收益。

| ST | VE | Tokens | CoMT | MMStar | HallusionBench |
|:---:|:---:|---:|---:|---:|---:|
| ✗ | ✗ | 212.91 | 28.37 | 53.62 | 63.76 |
| ✓ | ✗ | 74.07 | 29.25 | 54.47 | 67.39 |
| ✗ | ✓ | 216.57 | 31.24 | 54.91 | 67.76 |
| ✓ | ✓ | 69.84 | 32.39 | 56.39 | 69.12 |

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Without either module, the ablation uses 212.91 tokens and obtains 28.37 on CoMT, 53.62 on MMStar, and 63.76 on HallusionBench.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 不使用两个模块时，消融设置消耗 212.91 个标记，在 CoMT、MMStar 与 HallusionBench 上分别得到 28.37、53.62 和 63.76。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> With Selective Thinking alone, token consumption drops to 74.07, while accuracy improves modestly to 29.25, 54.47, and 67.39.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 仅使用选择性思考时，标记消耗降到 74.07，准确率小幅提升到 29.25、54.47 和 67.39。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> With Visual Enhancement alone, token use remains high at 216.57, but accuracy rises to 31.24, 54.91, and 67.76.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 仅使用视觉增强时，标记消耗仍高达 216.57，但准确率提升到 31.24、54.91 和 67.76。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> The full SDR-MCoT uses 69.84 tokens and obtains the best ablation scores: 32.39 on CoMT, 56.39 on MMStar, and 69.12 on HallusionBench.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 完整 SDR-MCoT 只使用 69.84 个标记，并取得最佳消融结果：CoMT 为 32.39，MMStar 为 56.39，HallusionBench 为 69.12。

## 5. Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper concludes that low-quality multimodal reasoning should be handled by deciding when reasoning is necessary and by improving how visual evidence is used during reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文结论认为，低质量多模态推理需要同时处理两个问题：判断何时需要推理，以及改善推理过程中视觉证据的使用方式。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> SDR-MCoT provides a training-free solution by using entropy to select the reasoning route and attention-level enhancement to keep difficult reasoning grounded in the image.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> SDR-MCoT 提供了一种免训练方案：用熵选择推理路径，并用注意力层面的增强让困难推理保持图像落地。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The main practical message is that multimodal reasoning systems should not maximize chain length by default. They should match reasoning depth and visual use to sample difficulty.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 最重要的实践启发是，多模态推理系统不应默认最大化思维链长度，而应让推理深度和视觉使用方式匹配样本难度。

## Acknowledgments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Support includes China's National Key R&D Program 2022ZD0160101, Shanghai Natural Science Foundation 23ZR1402900, Explorer Program 24TS1401300, Shanghai Major Project 2021SHZDZX0103, JC STEM Lab, MTR Research Funding CHU-24003, and Hong Kong RGC CUHK14213224. Computation used Fudan University's CFFF platform.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 资助包括国家重点研发计划 2022ZD0160101、上海市自然科学基金 23ZR1402900、探索者项目 24TS1401300、上海市科技重大专项 2021SHZDZX0103、JC STEM Lab、港铁研究资助 CHU-24003 与香港研究资助局 CUHK14213224。计算使用复旦大学 CFFF 平台。

## References

> **Policy / 策略：** Complete references are retained below in original searchable English. / 完整参考文献以下按原始可检索英文保留。

```text
Alomrani, M. A.; Zhang, Y.; Li, D.; Sun, Q.; Pal, S.; Zhang,
Z.; Hu, Y.; Ajwani, R. D.; Valkanas, A.; Karimi, R.; et al.
2025. Reasoning on a Budget: A Survey of Adaptive and
Controllable Test-Time Compute in LLMs. arXiv preprint
arXiv:2507.02076.
Chen, L.; Li, J.; Dong, X.; Zhang, P.; Zang, Y.; Chen, Z.;
Duan, H.; Wang, J.; Qiao, Y.; Lin, D.; et al. 2024a. Are we
on the right way for evaluating large vision-language models? Advances in Neural Information Processing Systems,
37: 27056–27087.
Chen, Q.; Qin, L.; Zhang, J.; Chen, Z.; Xu, X.; and Che,
W. 2024b. M3CoT: A Novel Benchmark for Multi-Domain
Multi-step Multi-modal Chain-of-Thought. In Proceedings
of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 8199–8221.
Chen, X.; Xu, J.; Liang, T.; He, Z.; Pang, J.; Yu, D.; Song,
L.; Liu, Q.; Zhou, M.; Zhang, Z.; et al. 2024c. Do not think
that much for 2+ 3=? on the overthinking of o1-like llms.
arXiv preprint arXiv:2412.21187.
Cheng, Z.; Chen, Q.; Zhang, J.; Fei, H.; Feng, X.; Che, W.;
Li, M.; and Qin, L. 2025. Comt: A novel benchmark for
chain of multi-modal thought on large vision-language models. In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 39, 23678–23686.
Chu, X.; Chen, X.; Wang, G.; Tan, Z.; Huang, K.; Lv, W.;
Mo, T.; and Li, W. 2025. Qwen Look Again: Guiding
Vision-Language Reasoning Models to Re-attention Visual
Information. arXiv preprint arXiv:2505.23558.
Gao, J.; Li, Y.; Cao, Z.; and Li, W. 2025. Interleaved-modal
chain-of-thought. In Proceedings of the Computer Vision
and Pattern Recognition Conference, 19520–19529.
Guan, T.; Liu, F.; Wu, X.; Xian, R.; Li, Z.; Liu, X.; Wang,
X.; Chen, L.; Huang, F.; Yacoob, Y.; et al. 2024. Hallusionbench: an advanced diagnostic suite for entangled language
hallucination and visual illusion in large vision-language
models. In Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition, 14375–14385.
Han, T.; Wang, Z.; Fang, C.; Zhao, S.; Ma, S.; and Chen,
Z. 2024. Token-budget-aware llm reasoning. arXiv preprint
arXiv:2412.18547.
Hu, Y.; Shi, W.; Fu, X.; Roth, D.; Ostendorf, M.; Zettlemoyer, L.; Smith, N. A.; and Krishna, R. 2024. Visual
sketchpad: Sketching as a visual chain of thought for multimodal language models. Advances in Neural Information
Processing Systems, 37: 139348–139379.
Huang, S.; Wang, H.; Zhong, W.; Su, Z.; Feng, J.; Cao, B.;
and Fung, Y. R. 2025. AdaCtrl: Towards Adaptive and Controllable Reasoning via Difficulty-Aware Budgeting. arXiv
preprint arXiv:2505.18822.
Jiang, C.; Heng, Y.; Ye, W.; Yang, H.; Xu, H.; Yan,
M.; Zhang, J.; Huang, F.; and Zhang, S. 2025a. VLM-
R3
: Region Recognition, Reasoning, and Refinement for
Enhanced Multimodal Chain-of-Thought. arXiv preprint
arXiv:2505.16192.
Jiang, L.; Wu, X.; Huang, S.; Dong, Q.; Chi, Z.; Dong, L.;
Zhang, X.; Lv, T.; Cui, L.; and Wei, F. 2025b. Think only
when you need with large hybrid-reasoning models. arXiv
preprint arXiv:2505.14631.
Kang, S.; Kim, J.; Kim, J.; and Hwang, S. J. 2025. See
What You Are Told: Visual Attention Sink in Large Multimodal Models. In The Thirteenth International Conference
on Learning Representations.
Kojima, T.; Gu, S. S.; Reid, M.; Matsuo, Y.; and Iwasawa,
Y. 2022. Large language models are zero-shot reasoners. Advances in neural information processing systems, 35:
22199–22213.
Li, C.; Wu, W.; Zhang, H.; Xia, Y.; Mao, S.; Dong, L.;
Vulić, I.; and Wei, F. 2025a. Imagine while reasoning in
space: Multimodal visualization-of-thought. arXiv preprint
arXiv:2501.07542.
Li, Z.; Dong, Q.; Ma, J.; Zhang, D.; and Sui, Z. 2025b. Selfbudgeter: Adaptive token allocation for efficient llm reasoning. arXiv preprint arXiv:2505.11274.
Liang, G.; Zhong, L.; Yang, Z.; and Quan, X. 2025.
Thinkswitcher: When to think hard, when to think fast.
arXiv preprint arXiv:2505.14183.
Lin, J.; Zeng, X.; Zhu, J.; Wang, S.; Shun, J.; Wu, J.; and
Zhou, D. 2025. Plan and Budget: Effective and Efficient
Test-Time Scaling on Large Language Model Reasoning.
arXiv preprint arXiv:2505.16122.
Liu, H.; Li, C.; Wu, Q.; and Lee, Y. J. 2024a. Visual instruction tuning. Advances in neural information processing
systems, 36.
Liu, J.; Wang, Y.; Du, J.; Zhou, J.; and Liu, Z. 2024b. Med-
CoT: Medical Chain of Thought via Hierarchical Expert. In
Proceedings of the 2024 Conference on Empirical Methods
in Natural Language Processing, 17371–17389.
Lu, J.; Yu, H.; Xu, S.; Ran, S.; Tang, G.; Wang, S.; Shan, B.;
Fu, T.; Feng, H.; Tang, J.; et al. 2025. Prolonged reasoning
is not all you need: Certainty-based adaptive routing for efficient llm/mllm reasoning. arXiv preprint arXiv:2505.15154.
Lu, P.; Bansal, H.; Xia, T.; Liu, J.; Li, C.; Hajishirzi, H.;
Cheng, H.; Chang, K.-W.; Galley, M.; and Gao, J. 2024.
MathVista: Evaluating Mathematical Reasoning of Foundation Models in Visual Contexts. In The Twelfth International
Conference on Learning Representations.
9583Lu, P.; Mishra, S.; Xia, T.; Qiu, L.; Chang, K.-W.; Zhu, S.-
C.; Tafjord, O.; Clark, P.; and Kalyan, A. 2022. Learn to
explain: Multimodal reasoning via thought chains for science question answering. Advances in Neural Information
Processing Systems, 35: 2507–2521.
Man, Y.; Huang, D.-A.; Liu, G.; Sheng, S.; Liu, S.; Gui, L.-
Y.; Kautz, J.; Wang, Y.-X.; and Yu, Z. 2025. Argus: Vision-
Centric Reasoning with Grounded Chain-of-Thought. In
Proceedings of the Computer Vision and Pattern Recognition Conference, 14268–14280.
Mitra, C.; Huang, B.; Darrell, T.; and Herzig, R. 2024. Compositional chain-of-thought prompting for large multimodal
models. In Proceedings of the IEEE/CVF Conference on
Computer Vision and Pattern Recognition, 14420–14431.
Mondal, D.; Modi, S.; Panda, S.; Singh, R.; and Rao, G. S.
2024. Kam-cot: Knowledge augmented multimodal chainof-thoughts reasoning. In Proceedings of the AAAI conference on artificial intelligence, volume 38, 18798–18806.
Muennighoff, N.; Yang, Z.; Shi, W.; Li, X. L.; Fei-Fei, L.;
Hajishirzi, H.; Zettlemoyer, L.; Liang, P.; Candes, E.; and
Hashimoto, T. 2025. s1: Simple test-time scaling. In Workshop on Reasoning and Planning for Large Language Models.
Schwenk, D.; Khandelwal, A.; Clark, C.; Marino, K.; and
Mottaghi, R. 2022. A-okvqa: A benchmark for visual question answering using world knowledge. In European conference on computer vision, 146–162. Springer.
Shao, H.; Qian, S.; Xiao, H.; Song, G.; Zong, Z.; Wang, L.;
Liu, Y.; and Li, H. 2024. Visual cot: Advancing multi-modal
language models with a comprehensive dataset and benchmark for chain-of-thought reasoning. Advances in Neural
Information Processing Systems, 37: 8612–8642.
Shen, Y.; Zhang, J.; Huang, J.; Shi, S.; Zhang, W.; Yan, J.;
Wang, N.; Wang, K.; Liu, Z.; and Lian, S. 2025. Dast:
Difficulty-adaptive slow-thinking for large reasoning models. arXiv preprint arXiv:2503.04472.
Sun, Q.; Hong, P.; Pala, T. D.; Toh, V.; Tan, U.; Ghosal, D.;
Poria,S.;etal.2024. Emma-x:Anembodiedmultimodalaction model with grounded chain of thought and look-ahead
spatial reasoning. arXiv preprint arXiv:2412.11974.
Tu, C.; Ye, P.; Zhou, D.; Bai, L.; Yu, G.; Chen, T.; and
Ouyang, W. 2025. Attention reallocation: Towards zero-cost
and controllable hallucination mitigation of mllms. arXiv
preprint arXiv:2503.08342.
Wang, P.; Bai, S.; Tan, S.; Wang, S.; Fan, Z.; Bai, J.; Chen,
K.; Liu, X.; Wang, J.; Ge, W.; et al. 2024. Qwen2-vl: Enhancing vision-language model’s perception of the world at
any resolution. arXiv preprint arXiv:2409.12191.
Wu, P.; and Xie, S. 2024. V?: Guided visual search as
a core mechanism in multimodal llms. In Proceedings of
the IEEE/CVF Conference on Computer Vision and Pattern
Recognition, 13084–13094.
Wu, Y.; Wang, Y.; Ye, Z.; Du, T.; Jegelka, S.; and Wang, Y.
2025. When more is less: Understanding chain-of-thought
length in llms. arXiv preprint arXiv:2502.07266.
Xiang, V.; Blagden, C.; Rafailov, R.; Lile, N.; Truong, S.;
Finn, C.; and Haber, N. 2025. Just Enough Thinking: Efficient Reasoning with Adaptive Length Penalties Reinforcement Learning. arXiv preprint arXiv:2506.05256.
Xiao, W.; Gan, L.; Dai, W.; He, W.; Huang, Z.; Li, H.;
Shu, F.; Yu, Z.; Zhang, P.; Jiang, H.; et al. 2025. Fast-slow
thinking for large vision-language model reasoning. arXiv
preprint arXiv:2504.18458.
Xiao, Z.; Zhang, D.; Han, X.; Fu, X.; Yu, W. Y.; Zhong, T.;
Wu, S.; Wang, Y.; Yin, J.; and Chen, G. 2024. Enhancing
llm reasoning via vision-augmented prompting. Advances in
Neural Information Processing Systems, 37: 28772–28797.
Xu, G.; Liu, P.; Zhu, K.; Zhang, W.; Xu, C.; and Huang, Z.
2024. LLaVA-CoT: Let Vision Language Models Reason
Step-by-Step. arXiv preprint arXiv:2411.10440.
Yang, S.; Niu, Y.; Liu, Y.; Ye, Y.; Lin, B.; and Yuan, L. 2025.
Look-Back: Implicit Visual Re-focusing in MLLM Reasoning. arXiv preprint arXiv:2507.03019.
Yu, F.; Wan, H.; Cheng, Q.; Zhang, Y.; Chen, J.; Han, F.;
Wu, Y.; Yao, J.; Hu, R.; Ding, N.; et al. 2025. HiPhO:
How Far Are (M) LLMs from Humans in the Latest High
School Physics Olympiad Benchmark? arXiv preprint
arXiv:2509.07894.
Zhang, D.; Lei, J.; Li, J.; Wang, X.; Liu, Y.; Yang, Z.; Li,
J.; Wang, W.; Yang, S.; Wu, J.; et al. 2025a. Critic-v: Vlm
critics help catch vlm errors in multimodal reasoning. In
Proceedings of the Computer Vision and Pattern Recognition Conference, 9050–9061.
Zhang, J.; Lin, N.; Hou, L.; Feng, L.; and Li, J. 2025b.
Adaptthink: Reasoning models can learn when to think.
arXiv preprint arXiv:2505.13417.
Zhang, R.; Xiao, C.; and Cao, Y. 2025. Long or short
CoT? Investigating Instance-level Switch of Large Reasoning Models. arXiv preprint arXiv:2506.04182.
Zhang, Z.; Zhang, A.; Li, M.; Zhao, H.; Karypis, G.; and
Smola, A. 2023. Multimodal Chain-of-Thought Reasoning
in Language Models. In TMLR.
Zheng, G.; Yang, B.; Tang, J.; Zhou, H.-Y.; and Yang, S.
2023. Ddcot: Duty-distinct chain-of-thought prompting for
multimodal reasoning in language models. Advances in
Neural Information Processing Systems, 36: 5168–5191.
Zheng, S.; Cheng, Q.; Yao, J.; Wu, M.; He, H.; Ding, N.;
Cheng, Y.; Hu, S.; Bai, L.; Zhou, D.; et al. 2025a. Scaling
physical reasoning with the physics dataset. arXiv preprint
arXiv:2506.00022.
Zheng, Z.; Yang, M.; Hong, J.; Zhao, C.; Xu, G.; Yang,
L.; Shen, C.; and Yu, X. 2025b. DeepEyes: Incentivizing”
Thinking with Images” via Reinforcement Learning. arXiv
preprint arXiv:2505.14362.
Zhou, Q.; et al. 2024. Image-of-Thought Prompting for Visual Reasoning Refinement in Multimodal Large Language
Models. arXiv preprint arXiv:2405.13872.
Zhu, J.; Wang, W.; Chen, Z.; Liu, Z.; Ye, S.; Gu, L.; Tian,
H.; Duan, Y.; Su, W.; Shao, J.; et al. 2025. Internvl3: Exploring advanced training and test-time recipes for open-source
multimodal models. arXiv preprint arXiv:2504.10479.
9584
```
