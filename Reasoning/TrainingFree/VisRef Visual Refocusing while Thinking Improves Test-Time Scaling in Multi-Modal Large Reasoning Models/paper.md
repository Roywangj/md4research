# VisRef: Visual Refocusing while Thinking Improves Test-Time Scaling in Multi-Modal Large Reasoning Models

> **中文题名：** VisRef：边思考边视觉再聚焦，提升多模态大推理模型的测试时扩展  
> **作者：** Soumya Suvra Ghosal, Youngeun Kim, Zhuowei Li, Ritwick Chaudhry, Linghan Xu, Hongjing Zhang, Jakub Zablocki, Yifan Xing, Qin Zhang  
> **出处：** arXiv:2603.00207v1，2026-02-27  
> **论文类型：** 方法 / training-free visual refocusing / test-time scaling  
> **源文件：** `Ghosal 等 - 2026 - VisRef Visual Refocusing while Thinking Improves Test-Time Scaling in Multi-Modal Large Reasoning M.pdf`  
> **阅读器：** 全文英中对照；源格式为 `pdf-text`；图表按首次实质讨论位置重排。页码与稳定块 ID 见 `source_map.json`。

## Page / Section Index

- Abstract: page 1
- 1. Introduction: pages 1-3
- 2. Related Works: pages 2-3
- 3. Preliminaries: pages 3-4
- 4. Proposed Framework: pages 3-6
- 5. Experiments: pages 6-7
- 6. Discussion: pages 7-8
- 7. Conclusion: pages 8-9
- Appendix: pages 12-16

## Terminology Ledger

| Canonical term | 中文 | First-use decision |
|---|---|---|
| Multi-modal Large Reasoning Models (MLRMs) | 多模态大推理模型 | 保留 MLRM 缩写 |
| test-time scaling | 测试时扩展 | 指推理时增加计算或轨迹 |
| visual refocusing | 视觉再聚焦 | 指推理中重新注入视觉证据 |
| visual token dilution | 视觉标记稀释 | 长文本推理中视觉注意力衰减 |
| textual self-reflection | 文本自反思 | 只用文本继续思考 |
| visual token coreset | 视觉标记核心集 | 每步选择的紧凑视觉标记子集 |
| Determinantal Point Process (DPP) | 行列式点过程 | 用于平衡相关性与多样性 |
| adaptive stopping criterion | 自适应停止准则 | 基于答案分布熵终止推理 |
| Standard Thinking (ST) | 标准思考 | 单条推理轨迹基线 |
| Textual Self-Reflection (TSR) | 文本自反思 | 文本-only 延长推理基线 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Large reasoning models can improve complex reasoning by scaling test-time compute through extended reasoning. However, in vision-dependent tasks, longer textual reasoning can hurt performance because models gradually lose attention to visual tokens and rely more on textual priors.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 大推理模型可以通过延长推理来扩大测试时计算，从而提升复杂推理能力。但在依赖视觉的任务中，更长的文本推理反而可能损害表现，因为模型会逐渐减少对视觉标记的关注，并更多依赖文本先验。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Prior methods use reinforcement-learning fine-tuning to route visual tokens or introduce refocusing mechanisms, but these methods require expensive data generation and policy optimization.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 既有方法会通过强化学习微调来路由视觉标记，或在推理中加入再聚焦机制，但这类方法需要昂贵的数据生成和策略优化。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> VisRef is a visually grounded test-time scaling framework. It reinjects a coreset of visual tokens that are relevant to the current reasoning context while remaining diverse and globally representative of the image.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> VisRef 是一个视觉落地的测试时扩展框架。它在推理过程中重新注入一组视觉标记核心集，这些标记既与当前推理上下文相关，又保持多样性，并能代表图像的全局内容。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Experiments on three visual reasoning benchmarks with state-of-the-art MLRMs show that, under fixed test-time compute budgets, VisRef outperforms existing test-time scaling approaches by up to 6.4%.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在三个视觉推理基准和先进 MLRM 上的实验表明，在固定测试时计算预算下，VisRef 相比现有测试时扩展方法最高提升 6.4%。

## 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> MLRMs extend chain-of-thought reasoning to vision-language tasks. They generate explicit thinking traces before final answers and show strong performance on visual mathematics, scientific problem solving, and multimodal understanding.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> MLRM 将思维链推理扩展到视觉语言任务。它们在给出最终答案前生成显式思考轨迹，并在视觉数学、科学问题求解和多模态理解中表现较强。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> A limitation appears when the reasoning trace becomes long: attention to visual information progressively diminishes, visual tokens are diluted in the expanding context, and the model increasingly relies on textual priors rather than actual image content.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 当推理轨迹变长时，一个关键限制会出现：模型对视觉信息的注意力逐步下降，视觉标记在不断扩展的上下文中被稀释，模型也越来越依赖文本先验，而不是实际图像内容。

### Figure 1. VisRef 的动机

![Figure 1](Reasoning/TrainingFree/VisRef%20Visual%20Refocusing%20while%20Thinking%20Improves%20Test-Time%20Scaling%20in%20Multi-Modal%20Large%20Reasoning%20Models/assets/page_001_fig_figure_1.png)

**Caption:** Textual self-reflection asks the model to think longer but loses visual grounding; VisRef dynamically reinjects reasoning-relevant visual cues.

**Caption[CN]:** 文本自反思让模型想得更久，但会丢失视觉落地；VisRef 动态重新注入与推理相关的视觉线索。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Human problem solving alternates between visual examination and abstract reasoning. Current MLRMs lack this feedback loop: once visual tokens are processed initially, they fade from attention as textual reasoning dominates.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 人类解决多模态问题时，会在查看图像和抽象推理之间来回切换。当前 MLRM 缺少这种反馈环路：视觉标记在初始处理后，随着文本推理占主导而逐渐淡出注意力。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The paper asks whether visual grounding can be restored entirely at test time, without retraining. VisRef answers by reinjecting carefully selected visual tokens at each reasoning step.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 论文提出的问题是：能否完全在测试时恢复视觉落地，而不做重新训练？VisRef 的回答是，在每个推理步骤重新注入经过选择的视觉标记。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The selection challenge is to avoid injecting all visual tokens, which would be too expensive. The authors formulate a coreset selection problem and use DPPs to balance relevance to the current reasoning state with diversity over the image.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 选择问题的难点在于不能把全部视觉标记都插回去，否则计算成本太高。作者把它形式化为核心集选择问题，并用 DPP 平衡当前推理相关性与图像覆盖多样性。

## 2. Related Works

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Related work covers multimodal large reasoning models, test-time scaling, and visual refocusing. Earlier multimodal CoT methods relied on prompting, while recent work uses reinforcement learning to induce deeper reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 相关工作覆盖多模态大推理模型、测试时扩展和视觉再聚焦。早期多模态思维链多依赖提示，近期工作则使用强化学习诱导更深的推理过程。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Test-time scaling increases inference computation through longer reasoning or self-verification. In multimodal settings, however, longer thinking can degrade visual attention.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 测试时扩展通过更长推理或自验证来增加推理时计算。但在多模态场景中，更长的思考可能降低视觉注意力。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Existing visual refocusing methods often require specialized data, retraining, tools, or architectural changes. VisRef is positioned as a plug-and-play test-time alternative.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 现有视觉再聚焦方法往往需要专门数据、重新训练、工具调用或架构改动。VisRef 则被定位为一种即插即用的测试时替代方案。

## 3. Preliminaries and Problem Setup

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> A standard MLRM thinking process can be written as $x_{\mathrm{input}}\to z\to y$, where $x_{\mathrm{input}}=[I,T]$ contains the image and textual prompt, $z$ is the generated reasoning trace, and $y$ is the final answer.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 标准 MLRM 思考过程可以写为 $x_{\mathrm{input}}\to z\to y$。其中 $x_{\mathrm{input}}=[I,T]$ 包含图像和文本提示，$z$ 是生成的推理轨迹，$y$ 是最终答案。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Textual self-reflection extends this into $x_{\mathrm{input}}\to z_1\to z_2\to\cdots\to z_k\to y$, using prompts such as "Wait" or "Think more" to keep generating text-only reasoning steps.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 文本自反思将这一过程扩展为 $x_{\mathrm{input}}\to z_1\to z_2\to\cdots\to z_k\to y$，通过“Wait”或“Think more”等提示继续生成纯文本推理步骤。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> VisRef instead represents a visual-integrated reasoning trajectory as $\tau_{1:k}=((z_1,V_1),(z_2,V_2),\ldots,(z_k,V_k))$, where $V_k$ is the subset of visual tokens reinjected at step $k$.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> VisRef 则把视觉整合后的推理轨迹表示为 $\tau_{1:k}=((z_1,V_1),(z_2,V_2),\ldots,(z_k,V_k))$，其中 $V_k$ 是第 $k$ 步重新注入的视觉标记子集。

## 4. Proposed Framework

### Figure 2. VisRef 框架

![Figure 2](assets/page_004_fig_figure_2.png)

**Caption:** At each reasoning step, VisRef selects a DPP-based visual token coreset and reinjects it until the answer entropy is low enough to stop.

**Caption[CN]:** 在每个推理步骤，VisRef 选择基于 DPP 的视觉标记核心集并重新注入，直到答案熵低到可以停止。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> VisRef has two main components: visual token selection and adaptive stopping. The first decides which visual tokens to reinject, and the second decides when reasoning should terminate.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> VisRef 有两个主要组件：视觉标记选择与自适应停止。前者决定重新注入哪些视觉标记，后者决定推理何时终止。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Reinjecting all visual tokens would be expensive. In InternVL-3.5-8B on MathVista, the paper reports about 1,772 visual tokens versus about 615 text tokens per reasoning step, and injecting all visual tokens causes a 2.3 times latency increase.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 重新注入全部视觉标记代价很高。论文报告，在 MathVista 上使用 InternVL-3.5-8B 时，每步大约有 1,772 个视觉标记，而文本标记约为 615 个；若注入全部视觉标记，延迟会增加 2.3 倍。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The ideal objective is to select a subset $V_k$ that maximizes the expected final reward, but this is intractable because the true reward is only known after the final answer and the subset space is exponentially large.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 理想目标是选择一个能最大化最终期望奖励的子集 $V_k$，但这在测试时不可解，因为真实奖励只有最终答案生成后才知道，而且候选子集空间呈指数级增长。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The tractable approximation assumes that the utility of $V_k$ mainly depends on the current reasoning state $z_k$. The method therefore scores candidate subsets with $J(V_k\mid x_{\mathrm{input}},z_k)$.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 可解近似采用一个马尔可夫假设：$V_k$ 的效用主要依赖当前推理状态 $z_k$。因此，方法用 $J(V_k\mid x_{\mathrm{input}},z_k)$ 给候选子集打分。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Let $z_k=\{z_k^{(1)},\ldots,z_k^{(T_k)}\}$ be the text token embeddings in the current reasoning state. The reasoning subspace is summarized as:

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 设 $z_k=\{z_k^{(1)},\ldots,z_k^{(T_k)}\}$ 为当前推理状态中的文本标记嵌入。推理子空间被概括为：

$$
M_k=\sum_{j=1}^{T_k}z_k^{(j)}(z_k^{(j)})^\top.
$$

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The DPP kernel between visual tokens $v_i$ and $v_j$ is defined through their projection into this text-conditioned subspace:

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 视觉标记 $v_i$ 与 $v_j$ 之间的 DPP 核由它们投影到这一文本条件子空间后的相似度定义：

$$
L_k(v_i,v_j)=v_i^\top M_kv_j.
$$

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> The subset objective is the determinant of the restricted kernel matrix:

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 子集目标是受限核矩阵的行列式：

$$
\widetilde{V}_k=\arg\max_{V_k\subseteq V}\det(L_k^{V_k}).
$$

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> The log determinant decomposes into a relevance term and a diversity term. Relevance measures alignment with the current text state, while diversity penalizes redundant visual tokens.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> log determinant 可以分解为相关性项和多样性项。相关性衡量视觉标记与当前文本状态的对齐，多样性则惩罚冗余视觉标记。

$$
\log\det(L_k^{V_k})=
\sum_{v_i\in V_k}\log(r_i^2)+\log\det(\bar{L}_k^{V_k}).
$$

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Since the combinatorial objective is NP-hard, VisRef uses greedy selection under a token budget $m$. For stopping, it computes the entropy of the answer distribution and stops when $H_k<\delta_{\mathrm{entropy}}$.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 由于组合目标是 NP-hard，VisRef 在标记预算 $m$ 下使用贪心选择。对于停止规则，它计算答案分布的熵，并在 $H_k<\delta_{\mathrm{entropy}}$ 时停止。

## 5. Experiments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The main experiments use MathVista testmini with 1,000 problems, MathVision with 304 visually grounded competition-style problems, and MM-Star with 1,500 vision-dependent questions.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 主实验使用 MathVista testmini 的 1,000 道题、MathVision 的 304 道视觉落地竞赛题，以及 MM-Star 的 1,500 个视觉依赖问题。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Models include InternVL3.5-8B, SAIL-VL2-Thinking, and Qwen-3-VL-8B-Thinking. Baselines are standard thinking and textual self-reflection. Main settings use $\delta_{\mathrm{entropy}}=0.25$, $m=\lfloor0.3|V|\rfloor$, and $K_{\max}=10$.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 模型包括 InternVL3.5-8B、SAIL-VL2-Thinking 和 Qwen-3-VL-8B-Thinking。基线为标准思考和文本自反思。主设置使用 $\delta_{\mathrm{entropy}}=0.25$、$m=\lfloor0.3|V|\rfloor$、$K_{\max}=10$。

### Table 1. 主结果

![Table 1](Reasoning/TrainingFree/VisRef%20Visual%20Refocusing%20while%20Thinking%20Improves%20Test-Time%20Scaling%20in%20Multi-Modal%20Large%20Reasoning%20Models/assets/page_006_fig_table_1.png)

**Caption:** Evaluation on MathVision, MathVista, and MM-Star across three MLRMs.

**Caption[CN]:** 三个 MLRM 在 MathVision、MathVista 与 MM-Star 上的评估结果。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> VisRef consistently outperforms both standard thinking and textual self-reflection. With InternVL3.5-8B, it improves over standard thinking by 5.4, 11.2, and 5.9 points on MathVision, MathVista, and MM-Star.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> VisRef 稳定超过标准思考和文本自反思。在 InternVL3.5-8B 上，它相对标准思考在 MathVision、MathVista 和 MM-Star 上分别提升 5.4、11.2 和 5.9 个百分点。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> On SAIL-VL2-8B, VisRef improves over standard thinking by 7.5, 5.1, and 7.6 points across the same three benchmarks, including a 6.4 point gain over textual self-reflection on MM-Star.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在 SAIL-VL2-8B 上，VisRef 相对标准思考在三个基准上分别提升 7.5、5.1 和 7.6 个百分点，其中在 MM-Star 上比文本自反思高 6.4 个百分点。

### Figure 3. 测试时扩展曲线

![Figure 3](assets/page_007_fig_figure_3.png)

**Caption:** VisRef generates multiple visual-integrated reasoning chains under fixed token budgets and outperforms text-only parallel thinking.

**Caption[CN]:** VisRef 在固定标记预算下生成多条视觉整合推理链，并超过纯文本并行思考。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The test-time scaling analysis generates multiple parallel visual-integrated reasoning traces under a fixed token budget and aggregates answers by majority voting. VisRef is better than text-only parallel thinking for the same budget.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 测试时扩展分析在固定标记预算下生成多条视觉整合推理轨迹，并通过多数投票聚合答案。在相同预算下，VisRef 优于纯文本并行思考。

### Table 2. 与训练型 Look-Back 的比较

![Table 2](Reasoning/TrainingFree/VisRef%20Visual%20Refocusing%20while%20Thinking%20Improves%20Test-Time%20Scaling%20in%20Multi-Modal%20Large%20Reasoning%20Models/assets/page_007_fig_table_2.png)

**Caption:** VisRef is training-free and competitive with Look-Back; combining both gives the best result.

**Caption[CN]:** VisRef 不训练模型且可与 Look-Back 竞争；二者结合取得最好结果。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Compared with Look-Back, a training-based visual refocusing method, VisRef is competitive without training. Combining Look-Back and VisRef gives the best scores: 83.1 on MathVista, 48.2 on MathVision, and 66.0 on MM-Star.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 相比训练型视觉再聚焦方法 Look-Back，VisRef 在不训练的情况下达到有竞争力的结果。Look-Back 与 VisRef 结合后最好：MathVista 83.1，MathVision 48.2，MM-Star 66.0。

## 6. Discussion

### Table 3. 相关性与多样性

![Table 3](Reasoning/TrainingFree/VisRef%20Visual%20Refocusing%20while%20Thinking%20Improves%20Test-Time%20Scaling%20in%20Multi-Modal%20Large%20Reasoning%20Models/assets/page_008_fig_table_3.png)

**Caption:** Ablation of relevance and diversity terms in the DPP scoring function.

**Caption[CN]:** DPP 打分函数中相关性项与多样性项的消融。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Relevance alone is not enough. On InternVL3.5-8B, the full DPP objective scores 79.3, 44.6, and 63.1, while relevance-only selection scores 77.4, 42.9, and 62.8.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 只有相关性并不够。在 InternVL3.5-8B 上，完整 DPP 目标得到 79.3、44.6 和 63.1；只用相关性选择则为 77.4、42.9 和 62.8。

### Figure 4. 超参数消融

![Figure 4](Reasoning/TrainingFree/VisRef%20Visual%20Refocusing%20while%20Thinking%20Improves%20Test-Time%20Scaling%20in%20Multi-Modal%20Large%20Reasoning%20Models/assets/page_007_fig_figure_4.png)

**Caption:** Entropy threshold and token budget ablations; the main setting uses $\delta_{\mathrm{entropy}}=0.25$ and $m=30\%$.

**Caption[CN]:** 熵阈值和标记预算消融；主设置使用 $\delta_{\mathrm{entropy}}=0.25$ 和 $m=30\%$。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The entropy threshold controls overthinking and under-reasoning. The authors select $\delta_{\mathrm{entropy}}=0.25$ because it balances accuracy and inference efficiency.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 熵阈值控制过度思考和推理不足。作者选择 $\delta_{\mathrm{entropy}}=0.25$，因为它在准确率和推理效率之间取得平衡。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Token budget analysis shows that accuracy increases from 76.1% to 79.2% as $m$ grows from 20% to 30%, but does not improve further at 40%.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 标记预算分析显示，当 $m$ 从 20% 增加到 30% 时，准确率从 76.1% 提升到 79.2%；继续增加到 40% 不再带来收益。

### Figure 5. 注意力可视化

![Figure 5](assets/page_008_fig_figure_5.png)

**Caption:** Visual reinjection makes attention maps more focused on task-critical objects during multi-step reasoning.

**Caption[CN]:** 视觉重新注入使多步推理中的注意力图更集中到任务关键对象。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The qualitative attention maps show diffuse attention before refocusing and more coherent focus on relevant visual regions after VisRef reinjects selected tokens.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 定性注意力图显示，再聚焦前注意力较分散；VisRef 重新注入选中标记后，注意力更集中到相关视觉区域。

## 7. Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> VisRef preserves visual grounding during extended test-time reasoning by selecting compact visual token subsets with a DPP-based objective and stopping with an entropy criterion.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> VisRef 通过基于 DPP 的目标选择紧凑视觉标记子集，并用熵准则停止推理，从而在延长测试时推理中保持视觉落地。

## Appendix Highlights

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The limitations section states that VisRef introduces additional computational overhead because DPP-based token selection is applied at every reasoning step.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 局限部分指出，VisRef 会引入额外计算开销，因为每个推理步骤都要应用基于 DPP 的标记选择。

### Table 5. 延迟

![Table 5](assets/page_014_fig_table_5.png)

**Caption:** Latency per prompt on MathVista.

**Caption[CN]:** MathVista 上每个提示的延迟。

### Table 6. 模型规模泛化

![Table 6](assets/page_014_fig_table_6.png)

**Caption:** VisRef improves MathVista accuracy across InternVL model scales.

**Caption[CN]:** VisRef 在不同规模的 InternVL 模型上提升 MathVista 准确率。

### Table 7. 选择策略比较

![Table 7](assets/page_015_fig_table_7.png)

**Caption:** DPP selection outperforms random and relevance-only token selection.

**Caption[CN]:** DPP 选择优于随机选择和只看相关性的选择。

### Table 8. 权重消融

![Table 8](assets/page_015_fig_table_8.png)

**Caption:** Balanced relevance-diversity weighting peaks at $\lambda=0.5$.

**Caption[CN]:** 相关性与多样性平衡时，$\lambda=0.5$ 表现最好。

## Critical Reading Notes

1. VisRef 的核心不是“多想几步”，而是把每一步思考重新接到视觉证据上。
2. DPP 目标的价值在于同时约束相关性和多样性，避免只反复选同一区域。
3. 熵停止规则让方法不至于无限延长，但阈值仍是需要调的超参数。
4. 这篇和 ICoT/DaP-ICoT 的差别是：VisRef 不插入对象图像，而是在视觉标记层重注入核心集。
5. 论文承认会增加推理延迟；因此“更好地测试时扩展”不等于“零成本增强”。
