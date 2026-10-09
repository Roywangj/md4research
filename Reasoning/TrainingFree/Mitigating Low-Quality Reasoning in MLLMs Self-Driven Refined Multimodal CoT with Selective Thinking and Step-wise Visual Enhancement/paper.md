# Mitigating Low-Quality Reasoning in MLLMs: Self-Driven Refined Multimodal CoT with Selective Thinking and Step-wise Visual Enhancement

> **中文题名：** 缓解 MLLM 中的低质量推理：带选择性思考与逐步视觉增强的自驱精炼多模态思维链  
> **作者：** Chongjun Tu, Peng Ye, Dongzhan Zhou, Tao Chen, Wanli Ouyang  
> **出处：** Proceedings of the AAAI Conference on Artificial Intelligence, 2026  
> **DOI：** 10.1609/aaai.v40i12.37919  
> **论文类型：** 方法 / training-free multimodal CoT / selective thinking / attention-level visual enhancement  
> **源文件：** `Mitigating Low-Quality Reasoning in MLLMs Self-Driven Refined Multimodal CoT with Selective Thinkin.pdf`  
> **阅读器：** 全文英中对照；源格式为 `pdf-text`；图表按首次实质讨论位置重排。页码与稳定块 ID 见 `source_map.json`。

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

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Given logits $z_i$ and temperature $T$, the probability of candidate token $i$ is:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 给定 logits $z_i$ 和温度 $T$，候选标记 $i$ 的概率为：

$$
p_i=\frac{\exp(z_i/T)}{\sum_j \exp(z_j/T)}.
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The first-token entropy is then:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 首标记熵计算为：

$$
H=-\sum_i p_i\log p_i.
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> If $H<\theta$, the model's direct-answer distribution is considered confident and the system returns the direct answer. If $H\geq\theta$, the sample is routed into step-by-step reasoning.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 若 $H<\theta$，说明模型的直接回答分布足够自信，系统返回直接答案。若 $H\geq\theta$，样本会进入逐步推理。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The threshold $\theta$ is estimated adaptively from a small sampled subset by averaging entropy values, rather than fixed as a universal constant.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 阈值 $\theta$ 不是固定通用常数，而是从一个小采样子集的平均熵中自适应估计。

> [!figure] Figure 4. Entropy and Accuracy
> 建议位置: `3. Method / Selective Thinking`  
> 放置原因: 该图显示首标记熵越高，M3CoT 上准确率整体越低，是选择性思考的经验支撑。  
> 当前状态: 自动抽图没有得到干净完整的独立图像；正文保留趋势描述。图中准确率从低熵组约 `0.97` 逐步降到高熵组约 `0.24-0.30`。

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
A_{\mathrm{amp}}=A_{\mathrm{curr}}\odot A_{\mathrm{rel}}.
$$

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> The amplified map is filtered by morphological erosion to remove isolated attention-sink points. The remaining high-attention patches are selected as task-related visual evidence.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 放大后的注意力图会经过形态学腐蚀，以移除孤立的注意力汇点。剩余高注意力 patch 被选为任务相关视觉证据。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> The selected visual patches then receive a multiplicative attention enhancement factor. The post-softmax attention distribution is renormalized so that the total attention mass remains valid.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 被选中的视觉 patch 随后获得乘法式注意力增强因子。增强发生在 softmax 后，并重新归一化，使总注意力质量保持有效。

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

## References

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The references cover multimodal large language models, chain-of-thought prompting, multimodal reasoning benchmarks, hallucination evaluation, and visual grounding methods.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 参考文献覆盖多模态大语言模型、思维链提示、多模态推理基准、幻觉评测和视觉落地方法。
