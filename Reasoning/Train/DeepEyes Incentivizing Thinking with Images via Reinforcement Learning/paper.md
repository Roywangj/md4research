# DeepEyes: Incentivizing "Thinking with Images" via Reinforcement Learning

> **中文题名：** DeepEyes：通过强化学习激励模型“用图像思考”  
> **作者：** Ziwei Zheng, Michael Yang, Jack Hong, Chenxiao Zhao, Guohai Xu, Le Yang, Chao Shen, Xing Yu  
> **出处：** ICLR 2026 / arXiv:2505.14362  
> **论文类型：** 方法 / train / active perception / reinforcement learning  
> **源文件：** `Zheng 等 - 2026 - DeepEyes Incentivizing Thinking with Images via Reinforcement Learning.pdf`  
> **阅读器：** 全文英中对照式阅读件；源格式为 `pdf-text`；图表按首次实质讨论位置重排。页码与稳定块 ID 见 `source_map.json`。

## Page / Section Index

- Abstract: page 1
- Introduction: pages 1-3
- Related Work: pages 3-4
- Method: pages 4-6
- Experiment and Analysis: pages 6-10
- Appendix examples and data: pages 17-24
- Limitations and Future Work: pages 24-25

## Terminology Ledger

| Canonical term | 中文 | First-use decision |
|---|---|---|
| DeepEyes | DeepEyes | 方法名保留 |
| active perception | 主动感知 | 模型主动裁剪或缩放图像获取新观察 |
| iMCoT | 交错多模态思维链 | 文本推理和视觉观察交错 |
| zoom-in operation | 放大观察操作 | 根据边界框裁剪局部图像 |
| conditional tool reward | 条件工具奖励 | 仅在答对且调用感知工具时奖励 |
| GRPO | GRPO | 组相对策略优化 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Large vision-language models perform well on multimodal understanding, but they still struggle to integrate visual information into mostly text-based reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 大型视觉语言模型在多模态理解上表现很强，但仍难以把视觉信息深度整合进以文本为主的推理过程。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> DeepEyes learns to think with images through end-to-end reinforcement learning, without requiring pre-collected reasoning data for cold-start supervised fine-tuning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> DeepEyes 通过端到端强化学习学会用图像思考，不需要预先收集推理数据来做冷启动监督微调。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The model uses active perception: it strategically grounds reasoning in visual information by deciding when to inspect image regions.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 模型使用主动感知：它会决定何时查看图像区域，从而把推理有策略地 grounding 到视觉信息上。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> DeepEyes improves general perception, reasoning, grounding, hallucination mitigation, and mathematical reasoning, while showing a training dynamic from exploration to efficient exploitation.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> DeepEyes 提升了通用感知、推理、grounding、幻觉缓解和数学推理，并呈现出从探索到高效利用的训练动态。

## Introduction

### Figure 1. Interleaved Multimodal CoT

![Figure 1](Reasoning/Train/DeepEyes%20Incentivizing%20Thinking%20with%20Images%20via%20Reinforcement%20Learning/assets/page_002_fig_figure_1.png)

**Caption:** DeepEyes performs active perception during reasoning and inserts visual observations into the trajectory.

**Caption[CN]:** DeepEyes 在推理过程中执行主动感知，并把视觉观察插入推理轨迹。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper argues that human-like visual reasoning often involves looking again, zooming into details, and checking hypotheses against new visual evidence.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文认为，类人的视觉推理常常需要再次观察、放大细节，并用新的视觉证据检查假设。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Existing workflow methods can do this through hand-designed pipelines, but DeepEyes asks whether the behavior can be incentivized by RL itself.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 现有工作流方法可以通过手工设计流程实现这一点，但 DeepEyes 追问这种行为能否由 RL 自身激励出来。

## Method

### Figure 2. DeepEyes Overview

![Figure 2](assets/page_004_fig_figure_2.png)

**Caption:** The model decides whether to answer or perform a second perception operation after reasoning steps.

**Caption[CN]:** 模型在推理步骤后自行决定是回答，还是执行第二次视觉感知操作。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Given an image and a question, DeepEyes can either continue textual reasoning, call a zoom-in operation, or produce the final answer.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 给定图像和问题后，DeepEyes 可以继续文本推理，也可以调用放大观察操作，或者直接给出最终答案。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The zoom-in operation receives bounding boxes and returns cropped images. These crops are appended to the trajectory as new visual observations.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 放大观察操作接收边界框并返回局部裁剪图。这些裁剪图作为新的视觉观察追加到推理轨迹中。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The iMCoT state contains both generated text tokens and image observation tokens.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> iMCoT 的状态同时包含已生成文本 token 和图像观察 token。

$$
s_t=\{(X_0,I_0),(X_1,I_1),\ldots,(X_t,I_t)\}=\{X_{\le t};I_{\le t}\}.
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The reward contains answer accuracy, format reward, and a conditional tool reward granted only when the answer is correct and active perception is used.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 奖励包含答案准确率、格式奖励，以及仅在答对且使用主动感知时给出的条件工具奖励。

$$
R(\tau)=R_{\text{acc}}(\tau)+R_{\text{format}}(\tau)+\mathbf{1}_{R_{\text{acc}}(\tau)>0}R_{\text{tool}}(\tau).
$$

## Training Data

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The training corpus combines three sources: V* for fine-grained perception, ArxivQA for charts, and ThinkLite-VL for challenging reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 训练语料由三部分组成：V* 提供细粒度感知，ArxivQA 提供图表，ThinkLite-VL 提供复杂推理。

### Figure 6. Data Distribution

![Figure 6](assets/page_017_fig_figure_6.png)

**Caption:** Training data includes 47% visual search, 30% chart data, and 23% reasoning data.

**Caption[CN]:** 训练数据包括 47% 视觉搜索、30% 图表数据和 23% 推理数据。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The data pipeline removes examples that are either too easy or too hard, then keeps samples where active perception can provide useful information.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 数据管线移除过易或过难样本，然后保留主动感知能够提供有用信息的样本。

## Experiments

### Table 1. High-Resolution Benchmarks

![Table 1](Reasoning/Train/DeepEyes%20Incentivizing%20Thinking%20with%20Images%20via%20Reinforcement%20Learning/assets/page_006_fig_table_1.png)

**Caption:** DeepEyes improves V* and HR-Bench over Qwen2.5-VL-7B.

**Caption[CN]:** DeepEyes 在 V* 和 HR-Bench 上超过 Qwen2.5-VL-7B。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> DeepEyes reaches 90.1 on V* Overall, compared with 71.2 for Qwen2.5-VL-7B. On HR-Bench 8K Overall, it reaches 72.6, compared with 65.3.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> DeepEyes 在 V* Overall 上达到 90.1，而 Qwen2.5-VL-7B 为 71.2。在 HR-Bench 8K Overall 上，它达到 72.6，基线为 65.3。

### Table 2 to Table 4. General Perception and Reasoning

![Table 2](assets/page_006_fig_table_2.png)

![Table 3](assets/page_006_fig_table_3.png)

![Table 4](assets/page_006_fig_table_4.png)

**Caption:** DeepEyes improves MME-RealWorld-Lite and several reasoning benchmarks, while grounding and hallucination results are mixed but generally stronger.

**Caption[CN]:** DeepEyes 提升 MME-RealWorld-Lite 和多个推理基准；grounding 与幻觉指标整体更强但并非每列都提升。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> On MME-RealWorld-Lite Overall, DeepEyes reaches 53.2, compared with 42.3 for Qwen2.5-VL. On MathVista, it reaches 70.1, compared with 68.3 for the reproduced baseline.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在 MME-RealWorld-Lite Overall 上，DeepEyes 达到 53.2，而 Qwen2.5-VL 为 42.3。在 MathVista 上，它达到 70.1，复现基线为 68.3。

## Training Dynamics and Ablations

### Figure 3. Training Dynamics

![Figure 3](assets/page_007_fig_figure_3.png)

**Caption:** Training evolves from ineffective exploration to high-frequency engagement and then efficient active perception.

**Caption[CN]:** 训练从低效探索，过渡到高频使用，再到高效主动感知。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper identifies three stages: initial exploration, high-frequency engagement, and efficient utilization. Tool count and response length first rise, then become more selective.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文识别出三个阶段：初始探索、高频使用和高效利用。工具调用次数和回答长度先上升，随后变得更有选择性。

### Table 5. Tool Reward

![Table 5](assets/page_008_fig_table_5.png)

**Caption:** Conditional tool reward outperforms no tool reward and unconditional reward.

**Caption[CN]:** 条件工具奖励优于无工具奖励和无条件工具奖励。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Without tool reward, results are V* 87.4, HR-4K 53.4, and HR-8K 55.4. Conditional reward reaches 90.1, 75.1, and 72.6.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 没有工具奖励时，V* 为 87.4，HR-4K 为 53.4，HR-8K 为 55.4。条件奖励分别达到 90.1、75.1 和 72.6。

### Table 9. iMCoT Ablation

![Table 9](assets/page_008_fig_table_9.png)

**Caption:** iMCoT is especially important on HR-8K.

**Caption[CN]:** iMCoT 在 HR-8K 上尤其重要。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> RL with text-only CoT reaches 60.8 on HR-8K, while DeepEyes with iMCoT reaches 72.6.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> text-only CoT 的 RL 在 HR-8K 上为 60.8，而带 iMCoT 的 DeepEyes 达到 72.6。

### Figure 5. Hallucination Mitigation

![Figure 5](assets/page_009_fig_figure_5.png)

**Caption:** Active perception lets the model re-check visual evidence and correct a language-prior hallucination.

**Caption[CN]:** 主动感知让模型重新检查视觉证据，并纠正语言先验导致的幻觉。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The case study shows a baseline hallucinating "rocks" from beach context, while DeepEyes zooms in and identifies a clock.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 案例中基线受海滩语境影响幻觉出“rocks”，而 DeepEyes 放大观察后识别出 clock。

## Limitations and Future Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The authors state that DeepEyes still has shortcuts, insufficient reasoning richness, and inaccurate target localization.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 作者指出，DeepEyes 仍存在 shortcut、推理过程不够丰富、目标定位不准确等问题。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The current visual reasoning process only includes crop. Future extensions could add richer tools and stronger foundation models.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 当前视觉推理过程只包含 crop。未来可以扩展到更丰富的工具和更强基础模型。

## Critical Reading Notes

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> DeepEyes is important because it studies the emergence of active perception under RL, not just a supervised format for visual references.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> DeepEyes 的重要性在于它研究 RL 下主动感知如何涌现，而不只是监督出一种视觉引用格式。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The main caution is that crop is only one tool. For 3D agents, the analogous operation may be rendering a new view, querying a spatial memory, or inspecting an object-level region.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 主要 caveat 是 crop 只是一个工具。对 3D agent 来说，对应操作可能是渲染新视角、查询空间记忆，或检查对象级局部区域。
