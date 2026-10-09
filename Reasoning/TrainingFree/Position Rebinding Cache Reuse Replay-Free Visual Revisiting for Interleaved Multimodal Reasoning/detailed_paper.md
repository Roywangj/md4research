# Position Rebinding Cache Reuse: Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning

> **中文题名：** 位置重绑定缓存复用：面向交错式多模态推理的免回放视觉回看  
> **作者：** Mengzhao Wang, Yanli Ji, Wangmeng Zuo, Peng Ye, Chongjun Tu  
> **来源：** arXiv:2606.26631v1，2026-06-25；DOI: 10.48550/arXiv.2606.26631  
> **原始文献：** `Wang 等 - 2026 - Position Rebinding Cache Reuse Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning.pdf`（14 页）  
> **阅读说明：** 本文件按原论文顺序提供逐段英中对照。正文、14 个编号公式、Algorithm 1、Tables 1–3、Figures 1–8、局限性与 42 条参考文献均已保留。参考文献为确保可检索性而保留原始英文书目信息，不逐条翻译。

## Page / Section Index

- Abstract: p. 1
- 1 Introduction: pp. 1–3
- 2 Why Direct KV Cache Reuse Fails: pp. 3–4
- 3 Method: pp. 4–7
- 4 Experiment: pp. 7–10
- 5 Related Work: pp. 10–11
- 6 Conclusion: p. 11
- 7 Limitations and Future Work: p. 11
- References: pp. 12–14

## Terminology Ledger

| Canonical term | 中文译法 | 说明 |
|---|---|---|
| Position Rebinding Cache Reuse (PRCR) | 位置重绑定缓存复用 | 保留 PRCR |
| replay-free visual revisiting | 免回放视觉回看 | 不重新前向视觉 token |
| Token-Replay | Token 回放 | 将选中视觉 token 再次送入模型 |
| Direct KV Cache Reuse | 直接 KV 缓存复用 | 不修正位置而直接追加历史缓存 |
| Raw Visual Evidence Memory (RVEM) | 原始视觉证据记忆 | 存储 pre-RoPE K/V 与原始坐标 |
| Position Reassignment for Cache Reinsertion | 缓存重插入的位置重分配 | 为选中缓存分配兼容坐标 |
| Position-Consistent Reinsertion (PCR) | 位置一致重插入 | 论文正文采用的全称；保留 PCR |
| Linear Position Appending (LPA) | 线性位置追加 | 将条目依次置于当前文本之后 |
| Uniform Interval Reinsertion (UIR) | 均匀区间重插入 | 压缩到相邻文本位置之间 |
| stale positional binding | 过期位置绑定 | 历史 key 与原始位置绑定 |
| stuck rate | 卡死率 | 陷入重复 token 解码循环的比例 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Interleaved multimodal reasoning improves visual grounding by revisiting visual evidence during multi-step generation, yet existing methods typically rely on token replay, repeatedly forwarding selected visual tokens. A natural shortcut is to reuse historical visual key-value (KV) cache directly. However, we identify a critical failure mode of this strategy: cached visual keys are already bound to their original positional context. Such stale positional binding distorts attention under later decoding contexts and can trigger severe autoregressive decoding collapse. This failure suggests that effective cache reuse requires reconstructing visual evidence under positions compatible with the current decoding state, rather than directly copying position-bound historical cache entries.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 交错式多模态推理通过在多步生成期间回看视觉证据来改善视觉落地，但现有方法通常依赖 Token 回放，即反复前向传播选中的视觉 token。一个自然的捷径是直接复用历史视觉键值（KV）缓存。然而，本文发现该策略存在一种关键失效模式：缓存的视觉 key 已经绑定到其原始位置上下文。此类过期位置绑定会在后续解码上下文中扭曲注意力，并可能触发严重的自回归解码崩溃。这表明，有效的缓存复用需要在与当前解码状态兼容的位置下重建视觉证据，而不是直接复制带有位置绑定的历史缓存条目。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> To this end, we propose Position Rebinding Cache Reuse (PRCR), a cache-level framework for replay-free visual revisiting. PRCR stores raw visual KV cache together with their original spatial coordinates, then reassigns position-compatible coordinates to select entries and rebinds their keys before injecting the reconstructed cache into the active decoder cache. This design reuses historical visual evidence while preserving textual positional continuity and relative visual structure. Experiments across multiple multimodal reasoning benchmarks show that PRCR achieves replay-level or better performance, improving average accuracy by 2–5% and reducing visual-revisiting computation by up to tens of thousands of times.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 为此，本文提出位置重绑定缓存复用（PRCR），一种面向免回放视觉回看的缓存级框架。PRCR 将原始视觉 KV 缓存与其原始空间坐标共同存储，随后为选中的条目重新分配位置兼容的坐标，并在把重建缓存注入活动解码器缓存之前重新绑定其 key。该设计既复用了历史视觉证据，又保持了文本位置连续性和相对视觉结构。多个多模态推理基准上的实验表明，PRCR 达到 Token 回放水平或更优的性能，将平均准确率提高 2–5%，并把视觉回看计算最多降低数万倍。

## 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Multimodal large language models (MLLMs) [1, 3, 4, 20, 21, 30] have demonstrated strong performance across a wide range of vision-language tasks [16, 29, 31, 36]. However, in multimodal chain-of-thought reasoning, intermediate reasoning still largely relies on textual rationales, with limited explicit revisiting of fine-grained visual evidence [8, 26, 34, 39]. This weakens visual grounding during multi-step reasoning, especially when the answer depends on local details, cross-region relations, or multiple pieces of visual evidence.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 多模态大语言模型（MLLM）[1, 3, 4, 20, 21, 30] 已在广泛的视觉—语言任务上展现出强大性能 [16, 29, 31, 36]。然而，在多模态思维链推理中，中间推理仍主要依赖文本理由，对细粒度视觉证据的显式回看十分有限 [8, 26, 34, 39]。这会削弱多步推理过程中的视觉落地，尤其当答案依赖局部细节、跨区域关系或多项视觉证据时。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Interleaved multimodal chain-of-thought [6, 9, 14, 23, 28] reasoning mitigates this issue by inserting visual evidence during decoding. Existing methods typically adopt a replay mechanism: relevant visual tokens or regions are selected according to the current reasoning state and fed back into the model for computation. While replay helps restore visual grounding, it introduces substantial redundancy, since the same visual evidence has already been encoded during multimodal prefill but must be forwarded again whenever it is revisited. This raises a natural question: can historical visual KV cache replace token replay for later visual revisiting?

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 交错式多模态思维链 [6, 9, 14, 23, 28] 通过在解码期间插入视觉证据来缓解这一问题。现有方法通常采用回放机制：依据当前推理状态选取相关视觉 token 或区域，再将其送回模型计算。回放虽然有助于恢复视觉落地，却引入大量冗余，因为同一视觉证据在多模态预填充阶段已经编码，却在每次回看时都必须再次前向传播。由此产生一个自然问题：历史视觉 KV 缓存能否取代 Token 回放，以支持后续视觉回看？

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> To investigate this issue, we adopt Qwen3-VL-8B-Instruct [4] as the baseline model. For Token-Replay, we follow ICoT [14] and use the same attention-driven selection (ADS) mechanism to identify the visual evidence to revisit. The selected original visual tokens are reinserted into the current decoding context and forwarded again. Direct KV Cache Reuse instead retrieves the historical KV cache corresponding to the same ADS-selected evidence from the multimodal prefill cache and directly appends it to the current decoder cache.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 为研究该问题，本文采用 Qwen3-VL-8B-Instruct [4] 作为基线模型。Token-Replay 遵循 ICoT [14]，使用相同的注意力驱动选择（ADS）机制识别需要回看的视觉证据，再把选中的原始视觉 token 重新插入当前解码上下文并再次前向传播。直接 KV 缓存复用则从多模态预填充缓存中检索与同一 ADS 证据对应的历史 KV 缓存，并将其直接追加到当前解码器缓存中。

### Figure 1. Motivation and efficiency of PRCR

![Figure 1](Reasoning/TrainingFree/Position%20Rebinding%20Cache%20Reuse%20Replay-Free%20Visual%20Revisiting%20for%20Interleaved%20Multimodal%20Reasoning/assets/page_002_fig_fig_1.png)

**Caption:** Motivation and efficiency of PRCR. (a) Category-level results on M³CoT show that Direct KV Cache Reuse collapses compared with the baseline. Here, NS, SC, PC, and ALL denote the reported M³CoT subsets and the overall score, respectively. (b) Overall M³CoT accuracy shows that PRCR avoids this collapse and achieves Token-Replay or better performance. (c) Under the same selected token budget, PRCR (32B model) achieves about 3,300× fewer visual-revisiting FLOPs than Token-Replay (2B model).

**Caption[CN]:** PRCR 的动机与效率。(a) M³CoT 的类别级结果表明，直接 KV 缓存复用相较基线发生崩溃；NS、SC、PC 和 ALL 分别表示所报告的 M³CoT 子集与总分。(b) M³CoT 总体准确率表明，PRCR 避免了这种崩溃，并达到 Token-Replay 水平或更优性能。(c) 在相同选中 token 预算下，PRCR（32B 模型）的视觉回看 FLOPs 比 Token-Replay（2B 模型）少约 3,300 倍。

### Figure 2. Decoding collapse under direct historical KV reuse

![Figure 2](assets/page_002_fig_fig_2.png)

**Caption:** Decoding collapse under direct historical KV reuse. (a) Example generation trajectories for Token-Replay and Direct KV Cache Reuse. (b) Failure-type pie charts, showing direct KV reuse mainly causes stuck decoding. (c) Token probabilities over generation steps, with repeated-token loops after failure onset. (d) Token entropy over generation steps; direct KV reuse collapses to low-entropy states, while Token-Replay remains stable.

**Caption[CN]:** 直接复用历史 KV 时的解码崩溃。(a) Token-Replay 与直接 KV 缓存复用的生成轨迹示例。(b) 失效类型饼图，表明直接 KV 复用主要导致解码卡死。(c) 各生成步骤的 token 概率，失效开始后出现重复 token 循环。(d) 各生成步骤的 token 熵；直接 KV 复用坍缩到低熵状态，而 Token-Replay 保持稳定。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> This naive cache-level shortcut leads to catastrophic failure. Compared with the baseline, Direct KV Cache Reuse causes overall M³CoT accuracy to drop from 66.4% to 23.5%, with consistent degradation across representative subsets. Historical visual caches cannot be treated as ordinary entries and copied into a later context: their visual keys are already bound to the original positional context, which conflicts with current text positions and the active cache structure and disrupts autoregressive decoding.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 这种朴素的缓存级捷径会造成灾难性失效。相较基线，直接 KV 缓存复用使 M³CoT 总体准确率从 66.4% 骤降至 23.5%，且各代表性子集均出现退化。历史视觉缓存不能被视为普通缓存条目并复制到后续上下文：其视觉 key 已经与原始位置上下文绑定，会与当前文本位置及活动缓存结构冲突，从而破坏自回归解码。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> PRCR stores raw visual KV cache before positional encoding together with original spatial coordinates. When evidence is revisited, it reassigns positions, rebinds keys with positional encoding, and reconstructs the visual cache in the active decoder cache. PRCR avoids Direct KV Cache Reuse collapse, recovers replay-level or better accuracy, and substantially reduces visual-revisiting FLOPs across token budgets and model scales.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> PRCR 在位置编码前存储原始视觉 KV 缓存及其原始空间坐标。回看证据时，它重新分配位置、使用位置编码重绑 key，并在活动解码器缓存中重建视觉缓存。PRCR 避免了直接 KV 缓存复用的崩溃，恢复到回放水平或更优准确率，并在不同 token 预算和模型尺度下显著减少视觉回看 FLOPs。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The contributions are: (1) identifying that position-bound visual cache entries can trigger severe autoregressive collapse when inserted into a later decoding context; (2) proposing PRCR as a replay-free cache-reuse framework for efficient visual revisiting; and (3) introducing Raw Visual Evidence Memory and Position Reassignment for Cache Reinsertion to reconstruct position-compatible visual cache with replay-level or better accuracy and substantially lower computation.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 本文贡献包括：(1) 发现带位置绑定的视觉缓存条目插入后续解码上下文时可能触发严重的自回归崩溃；(2) 提出 PRCR，作为高效视觉回看的免回放缓存复用框架；(3) 引入原始视觉证据记忆与缓存重插入的位置重分配，以重建位置兼容的视觉缓存，在显著降低计算量的同时达到回放水平或更优准确率。

## 2. Why Direct KV Cache Reuse Fails

### 2.1 Preliminaries on ICoT Reasoning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Conventional multimodal chain-of-thought (CoT) [8, 33, 39] extends language CoT reasoning to vision-language tasks. Given an input image $x^v$ and textual instruction $x^t$, the model produces a purely textual reasoning trajectory:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 常规多模态思维链（CoT）[8, 33, 39] 将语言 CoT 推理扩展到视觉—语言任务。给定输入图像 $x^v$ 和文本指令 $x^t$，模型产生纯文本推理轨迹：

$$
S_{\mathrm{text}}=\{r_1,r_2,\ldots,r_N,a\}. \tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Here $r_n$ is the intermediate textual rationale at step $n$, $N$ is the total number of reasoning steps, and $a$ is the final answer. Interleaved multimodal chain-of-thought (ICoT) [9, 14, 23] interleaves visual evidence with textual rationales:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 其中，$r_n$ 是第 $n$ 个推理步骤的中间文本理由，$N$ 是推理步骤总数，$a$ 是最终答案。交错式多模态思维链（ICoT）[9, 14, 23] 将视觉证据与文本理由交错组织：

$$
S_{\mathrm{interleaved}}=\{r_1,e_1,r_2,e_2,\ldots,r_N,e_N,a\}. \tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Let $e_\tau$ be evidence revisited at decoding step $\tau$, and $\mathcal V=\{v_m\}_{m=1}^{M}$ be the $M$ visual tokens from $x^v$. At a trigger step, ADS ranks them by relevance to the current decoding context and selects $K_\tau$ tokens:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 令 $e_\tau$ 表示解码步骤 $\tau$ 回看的证据，$\mathcal V=\{v_m\}_{m=1}^{M}$ 表示从 $x^v$ 提取的 $M$ 个视觉 token。在触发步骤，ADS 按其与当前解码上下文的相关性排序，并选择 $K_\tau$ 个 token：

$$
\mathcal I_\tau=\{m_1,\ldots,m_{K_\tau}\}\subseteq\{1,\ldots,M\},\qquad
e_\tau=\{v_{m_j}\}_{j=1}^{K_\tau}. \tag{3}
$$

### 2.2 Collapse of Autoregressive Token Distributions

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> At trigger step $\tau$, Direct KV Cache Reuse retrieves prefilled entries indexed by $\mathcal I_\tau$ and appends them to the decoder cache without replaying the selected tokens. This causes a sharp performance collapse. It is not merely a prediction error but a systematic decoding breakdown: direct reuse frequently enters repeated-token loops; after failure onset, repeated-token probability saturates and output entropy collapses, indicating a low-entropy self-reinforcing regime.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在触发步骤 $\tau$，直接 KV 缓存复用检索由 $\mathcal I_\tau$ 索引的预填充条目，并在不回放选中 token 的情况下将其追加到解码器缓存。这会造成显著性能崩溃，而且并非普通预测误差，而是系统性的解码故障：直接复用频繁进入重复 token 循环；失效开始后，重复 token 概率迅速饱和，输出熵坍缩，形成低熵、自我强化的解码状态。

### 2.3 Stale Positional Binding Perturbs Attention Routing

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Attention maps show that Direct KV Cache Reuse perturbs attention over both previous text and reused visual evidence, whereas Token-Replay preserves a stable pattern. Modern MLLMs bind visual keys to original spatial coordinates through RoPE. For visual token $v_m$ with coordinate $\mathbf p_m=(h_m,w_m)$ and pre-RoPE projections $k_m^{\mathrm{raw}},v_m^{\mathrm{raw}}$, the historical entry is:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 注意力图显示，直接 KV 缓存复用会同时扰乱先前文本和复用视觉证据上的注意力，而 Token-Replay 保持稳定模式。现代 MLLM 通过 RoPE 将视觉 key 绑定到原始空间坐标。对于坐标为 $\mathbf p_m=(h_m,w_m)$、pre-RoPE 投影为 $k_m^{\mathrm{raw}},v_m^{\mathrm{raw}}$ 的视觉 token $v_m$，历史缓存条目为：

$$
\widetilde{k}_m=\mathrm{RoPE}(k_m^{\mathrm{raw}},\mathbf p_m),\qquad
\widetilde{v}_m=v_m^{\mathrm{raw}}. \tag{4}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Although the value is not position-encoded, the key is bound to $\mathbf p_m$. At step $\tau$, let $q_\tau^{\mathrm{raw}}$ be the current raw text query and $\mathbf p_\tau^{\mathrm{txt}}=(p_\tau^{\mathrm{txt}},p_\tau^{\mathrm{txt}})$ its HW position. Direct reuse produces:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> value 虽未经过位置编码，但 key 已绑定到 $\mathbf p_m$。在步骤 $\tau$，令 $q_\tau^{\mathrm{raw}}$ 为当前原始文本 query，$\mathbf p_\tau^{\mathrm{txt}}=(p_\tau^{\mathrm{txt}},p_\tau^{\mathrm{txt}})$ 为其 HW 位置。直接复用得到：

$$
s_m^{\mathrm{direct}}
=\left\langle \mathrm{RoPE}(q_\tau^{\mathrm{raw}},\mathbf p_\tau^{\mathrm{txt}}),\widetilde{k}_m\right\rangle
=\left\langle q_\tau^{\mathrm{raw}},R(\mathbf p_m-\mathbf p_\tau^{\mathrm{txt}})k_m^{\mathrm{raw}}\right\rangle. \tag{5}
$$

### Figure 3. Attention perturbation under direct historical KV cache reuse

![Figure 3](assets/page_004_fig_fig_3.png)

**Caption:** Attention perturbation under direct historical KV cache reuse. The heatmap shows how Direct KV Cache Reuse disturbs attention across the active decoding context. Green shading indicates attention weight (low to high).

**Caption[CN]:** 直接复用历史 KV 缓存时的注意力扰动。热图展示直接 KV 缓存复用如何扰乱整个活动解码上下文的注意力；绿色阴影表示由低到高的注意力权重。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Equation (5) uses a stale relative offset between the current text position and original visual coordinate. Normalization with active cache entries lets these stale scores reshape attention over the entire context. The failure chain is therefore: stale positional binding perturbs attention routing, shifts token prediction, and is autoregressively amplified into a low-entropy repeated-token loop.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 公式 (5) 使用当前文本位置与原始视觉坐标之间的过期相对偏移。与活动缓存条目共同归一化后，这些过期分数会重塑整个上下文的注意力。因此，失效链条是：过期位置绑定扰乱注意力路由，引起 token 预测偏移，再经自回归放大成为低熵重复 token 循环。

## 3. Method

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Historical visual cache can be reused only after stale positional binding is removed and position-compatible entries are reconstructed. PRCR comprises Raw Visual Evidence Memory (RVEM), Position Reassignment for Cache Reinsertion, and Replay-Free Cache Decoding.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 只有移除过期位置绑定并重建位置兼容条目后，历史视觉缓存才能被安全复用。PRCR 包含原始视觉证据记忆（RVEM）、缓存重插入的位置重分配和免回放缓存解码三个部分。

### Figure 4. Overview of Position Rebinding Cache Reuse

![Figure 4](assets/page_005_fig_fig_4.png)

**Caption:** Overview of Position Rebinding Cache Reuse (PRCR). PRCR enables replay-free visual revisiting through three stages: (a) store pre-RoPE visual KV cache with original positions; (b) reassign compatible coordinates to selected entries; (c) rebind keys with RoPE and inject the reconstructed cache for subsequent decoding.

**Caption[CN]:** 位置重绑定缓存复用（PRCR）概览。PRCR 通过三个阶段实现免回放视觉回看：(a) 存储带原始位置的 pre-RoPE 视觉 KV 缓存；(b) 为选中条目重分配兼容坐标；(c) 使用 RoPE 重绑 key，并注入重建缓存以继续解码。

### 3.1 Raw Visual Evidence Memory

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Standard decoder caches store position-bound keys and values. RVEM instead stores raw key/value projections before RoPE, together with original positions. Let $\mathcal L$ be transformer layers and $h_{m,\ell}$ the hidden representation entering layer $\ell$:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 标准解码器缓存存储带位置绑定的 key 和 value。RVEM 则存储 RoPE 之前的原始键值投影及其原始位置。令 $\mathcal L$ 为 Transformer 层集合，$h_{m,\ell}$ 为进入第 $\ell$ 层的隐藏表示：

$$
k_{m,\ell}^{\mathrm{raw}}=W_\ell^K h_{m,\ell},\qquad
v_{m,\ell}^{\mathrm{raw}}=W_\ell^V h_{m,\ell},\quad m=1,\ldots,M,\ \ell\in\mathcal L. \tag{6}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> These projections are stored before the key is tied to positional encoding. RVEM over all visual tokens is:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 这些投影在 key 绑定到特定位置编码之前存储。覆盖所有视觉 token 的 RVEM 为：

$$
\mathcal M=\left\{\left(\{(k_{m,\ell}^{\mathrm{raw}},v_{m,\ell}^{\mathrm{raw}})\}_{\ell\in\mathcal L},\mathbf p_m\right)\right\}_{m=1}^{M}. \tag{7}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> At trigger step $\tau$, the entries selected by $\mathcal I_\tau$ form $\mathcal M_\tau=\mathcal M[\mathcal I_\tau]$.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在触发步骤 $\tau$，由 $\mathcal I_\tau$ 选中的条目构成 $\mathcal M_\tau=\mathcal M[\mathcal I_\tau]$。

### 3.2 Position Reassignment for Cache Reinsertion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> LPA places entries sequentially after the current text token and shifts subsequent text positions. UIR keeps text positions unchanged but compresses all entries between two consecutive text tokens, potentially losing discriminative coordinates and spatial structure. PCR instead fixes the next text position, extends the reinsertion interval locally to $(p_\tau^{\mathrm{txt}}-L,p_\tau^{\mathrm{txt}}+1)$, and re-anchors selected entries by normalized relative positions.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> LPA 将条目依次置于当前文本 token 之后，会移动后续文本位置。UIR 保持文本位置不变，却把所有条目压缩到两个连续文本 token 之间，可能损失可区分坐标和空间结构。PCR 则固定下一文本位置，将重插入区间向左局部扩展到 $(p_\tau^{\mathrm{txt}}-L,p_\tau^{\mathrm{txt}}+1)$，并依据归一化相对位置重新锚定选中条目。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For each spatial axis $a\in\{h,w\}$, PCR computes the selected coordinate range:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 对每个空间轴 $a\in\{h,w\}$，PCR 计算选中子集的坐标范围：

$$
p_{\tau,\min}^{(a)}=\min_{m\in\mathcal I_\tau}p_m^{(a)},\qquad
p_{\tau,\max}^{(a)}=\max_{m\in\mathcal I_\tau}p_m^{(a)}. \tag{8}
$$

### Algorithm 1. Position Rebinding Cache Reuse (PRCR)

![Algorithm 1](assets/page_006_fig_algorithm_1.png)

**Caption:** Position Rebinding Cache Reuse (PRCR). The algorithm retrieves selected raw memory, normalizes and re-anchors its coordinates, rebinds keys with RoPE, reuses values, concatenates the reconstructed cache with the decoder cache, and continues decoding.

**Caption[CN]:** 位置重绑定缓存复用（PRCR）。算法检索选中的原始记忆，归一化并重新锚定其坐标，使用 RoPE 重绑 key、复用 value，将重建缓存与解码器缓存拼接，然后继续解码。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Require:** visual memory $\mathcal M$; selected indices $\mathcal I_\tau=\{m_1,\ldots,m_{K_\tau}\}$; current text position $p_\tau^{\mathrm{txt}}$; left extension length $L$; existing decoder cache $\{\mathcal C_{\tau,\ell}^{\mathrm{ctx}}\}_{\ell\in\mathcal L}$. **Ensure:** active decoder cache $\{\mathcal C_{\tau,\ell}^{\mathrm{act}}\}_{\ell\in\mathcal L}$.
>
> 1. Retrieve $\mathcal M_\tau\leftarrow\mathcal M[\mathcal I_\tau]$.
> 2. For each $a\in\{h,w\}$, compute $p_{\tau,\min}^{(a)}$ and $p_{\tau,\max}^{(a)}$ over $\mathcal I_\tau$.
> 3. For $j=1,\ldots,K_\tau$, normalize $u_{\tau,j}^{(a)}$ by Eq. (9) and assign $\hat p_{\tau,j}^{(a)}$ by Eq. (10).
> 4. Form $\hat{\mathbf p}_{\tau,j}=(\hat p_{\tau,j}^{(h)},\hat p_{\tau,j}^{(w)})$ and stack them as $\widehat{\mathbf P}_\tau$.
> 5. For each $\ell\in\mathcal L$, collect $(K_{\tau,\ell}^{\mathrm{raw}},V_{\tau,\ell}^{\mathrm{raw}})$ from $\mathcal M_\tau$.
> 6. Rebind keys and reuse values: $\widehat K_{\tau,\ell}^{\mathrm{vis}}\leftarrow\mathrm{RoPE}(K_{\tau,\ell}^{\mathrm{raw}},\widehat{\mathbf P}_\tau)$; $\widehat V_{\tau,\ell}^{\mathrm{vis}}\leftarrow V_{\tau,\ell}^{\mathrm{raw}}$.
> 7. Concatenate: $\mathcal C_{\tau,\ell}^{\mathrm{act}}\leftarrow\mathrm{Concat}(\mathcal C_{\tau,\ell}^{\mathrm{ctx}},\widehat{\mathcal C}_{\tau,\ell}^{\mathrm{vis}})$.
> 8. Continue autoregressive decoding with $\{\mathcal C_{\tau,\ell}^{\mathrm{act}}\}_{\ell\in\mathcal L}$.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **输入要求：** 视觉记忆 $\mathcal M$；选中索引 $\mathcal I_\tau=\{m_1,\ldots,m_{K_\tau}\}$；当前文本位置 $p_\tau^{\mathrm{txt}}$；左扩展长度 $L$；现有解码器缓存 $\{\mathcal C_{\tau,\ell}^{\mathrm{ctx}}\}_{\ell\in\mathcal L}$。**输出保证：** 活动解码器缓存 $\{\mathcal C_{\tau,\ell}^{\mathrm{act}}\}_{\ell\in\mathcal L}$。
>
> 1. 检索 $\mathcal M_\tau\leftarrow\mathcal M[\mathcal I_\tau]$。
> 2. 对每个 $a\in\{h,w\}$，在 $\mathcal I_\tau$ 上计算 $p_{\tau,\min}^{(a)}$ 和 $p_{\tau,\max}^{(a)}$。
> 3. 对 $j=1,\ldots,K_\tau$，由公式 (9) 归一化 $u_{\tau,j}^{(a)}$，再由公式 (10) 分配 $\hat p_{\tau,j}^{(a)}$。
> 4. 构造 $\hat{\mathbf p}_{\tau,j}=(\hat p_{\tau,j}^{(h)},\hat p_{\tau,j}^{(w)})$，并堆叠为 $\widehat{\mathbf P}_\tau$。
> 5. 对每个 $\ell\in\mathcal L$，从 $\mathcal M_\tau$ 收集 $(K_{\tau,\ell}^{\mathrm{raw}},V_{\tau,\ell}^{\mathrm{raw}})$。
> 6. 重绑 key 并复用 value：$\widehat K_{\tau,\ell}^{\mathrm{vis}}\leftarrow\mathrm{RoPE}(K_{\tau,\ell}^{\mathrm{raw}},\widehat{\mathbf P}_\tau)$；$\widehat V_{\tau,\ell}^{\mathrm{vis}}\leftarrow V_{\tau,\ell}^{\mathrm{raw}}$。
> 7. 拼接缓存：$\mathcal C_{\tau,\ell}^{\mathrm{act}}\leftarrow\mathrm{Concat}(\mathcal C_{\tau,\ell}^{\mathrm{ctx}},\widehat{\mathcal C}_{\tau,\ell}^{\mathrm{vis}})$。
> 8. 使用 $\{\mathcal C_{\tau,\ell}^{\mathrm{act}}\}_{\ell\in\mathcal L}$ 继续自回归解码。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> For the non-degenerate case $p_{\tau,\max}^{(a)}>p_{\tau,\min}^{(a)}$, normalize and re-anchor each selected entry as:

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 对非退化情形 $p_{\tau,\max}^{(a)}>p_{\tau,\min}^{(a)}$，每个选中条目按下式归一化并重新锚定：

$$
u_{\tau,j}^{(a)}=\frac{p_{m_j}^{(a)}-p_{\tau,\min}^{(a)}}{p_{\tau,\max}^{(a)}-p_{\tau,\min}^{(a)}},\qquad a\in\{h,w\}. \tag{9}
$$

$$
\hat p_{\tau,j}^{(a)}=(p_\tau^{\mathrm{txt}}-L)+(L+1)\frac{1+(K_\tau-1)u_{\tau,j}^{(a)}}{K_\tau+1},\qquad a\in\{h,w\}. \tag{10}
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Each reinserted entry lies inside $(p_\tau^{\mathrm{txt}}-L,p_\tau^{\mathrm{txt}}+1)$, while the next text token remains at $p_\tau^{\mathrm{txt}}+1$. Thus PCR preserves text-position progression and, through normalized relative positions, the spatial layout of the selected subset.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 每个重插入条目都位于 $(p_\tau^{\mathrm{txt}}-L,p_\tau^{\mathrm{txt}}+1)$ 内，而下一文本 token 仍位于 $p_\tau^{\mathrm{txt}}+1$。因此，PCR 既保持文本位置推进，又通过归一化相对位置保留选中子集的空间布局。

### 3.3 Replay-Free Cache Decoding

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For each layer $\ell$, selected raw projections are collected as:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 对每一层 $\ell$，选中的原始投影整理为：

$$
(K_{\tau,\ell}^{\mathrm{raw}},V_{\tau,\ell}^{\mathrm{raw}})=
([k_{m_1,\ell}^{\mathrm{raw}};\ldots;k_{m_{K_\tau},\ell}^{\mathrm{raw}}],
[v_{m_1,\ell}^{\mathrm{raw}};\ldots;v_{m_{K_\tau},\ell}^{\mathrm{raw}}]). \tag{11}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Stack positions as $\widehat{\mathbf P}_\tau=[\hat{\mathbf p}_{\tau,1};\ldots;\hat{\mathbf p}_{\tau,K_\tau}]\in\mathbb R^{K_\tau\times2}$. Reconstruct cache by rebinding keys and directly reusing values:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 将位置堆叠为 $\widehat{\mathbf P}_\tau=[\hat{\mathbf p}_{\tau,1};\ldots;\hat{\mathbf p}_{\tau,K_\tau}]\in\mathbb R^{K_\tau\times2}$。通过重绑 key 并直接复用 value 重建缓存：

$$
\widehat K_{\tau,\ell}^{\mathrm{vis}}=\mathrm{RoPE}(K_{\tau,\ell}^{\mathrm{raw}},\widehat{\mathbf P}_\tau),\qquad
\widehat V_{\tau,\ell}^{\mathrm{vis}}=V_{\tau,\ell}^{\mathrm{raw}}. \tag{12}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Values require no positional rebinding, whereas keys must match current reassigned positions. With existing cache $\mathcal C_{\tau,\ell}^{\mathrm{ctx}}=(K_{\tau,\ell}^{\mathrm{ctx}},V_{\tau,\ell}^{\mathrm{ctx}})$, the active cache is:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> value 不需要位置重绑定，而 key 必须匹配当前重分配位置。令现有缓存为 $\mathcal C_{\tau,\ell}^{\mathrm{ctx}}=(K_{\tau,\ell}^{\mathrm{ctx}},V_{\tau,\ell}^{\mathrm{ctx}})$，则活动缓存为：

$$
\mathcal C_{\tau,\ell}^{\mathrm{act}}=
(\mathrm{Concat}[K_{\tau,\ell}^{\mathrm{ctx}},\widehat K_{\tau,\ell}^{\mathrm{vis}}],
\mathrm{Concat}[V_{\tau,\ell}^{\mathrm{ctx}},\widehat V_{\tau,\ell}^{\mathrm{vis}}]). \tag{13}
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Decoding continues at $p^{\mathrm{next}}=p_\tau^{\mathrm{txt}}+1$, with layer-wise output:

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 解码在 $p^{\mathrm{next}}=p_\tau^{\mathrm{txt}}+1$ 处继续，逐层输出为：

$$
o_{\mathrm{next},\ell}=\mathrm{softmax}\left(
\frac{\mathrm{RoPE}(q_{\mathrm{next},\ell}^{\mathrm{raw}},\mathbf p_{\mathrm{next}})(K_{\tau,\ell}^{\mathrm{act}})^\top}{\sqrt{d_k}}
\right)V_{\tau,\ell}^{\mathrm{act}}. \tag{14}
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The selected evidence is thus reused through reconstructed cache entries rather than token replay, and its keys are rebound to current positions rather than copied from stale cache. Standard autoregressive generation can continue with position-compatible evidence.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 因此，选中证据通过重建缓存条目而非 Token 回放来复用；其 key 被重绑到当前位置，而不是从过期缓存直接复制。解码器由此可携带位置兼容的视觉证据继续标准自回归生成。

## 4. Experiment

### 4.1 Experimental Settings

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Experiments use Qwen3-VL-8B/32B-Instruct [4] and InternVL3.5-8B/14B [30]. Token-Replay re-forwards ADS-selected visual tokens; Direct KV Cache Reuse and PRCR use the same selected evidence so that only the reuse mechanism changes.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 实验采用 Qwen3-VL-8B/32B-Instruct [4] 和 InternVL3.5-8B/14B [30]。Token-Replay 重新前向传播 ADS 选中的视觉 token；直接 KV 缓存复用和 PRCR 使用相同的选中证据，从而仅改变证据复用机制。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Benchmarks are M³CoT [8], MathVista [25], MMStar [7], and MMMU [37]. M³CoT reports category and overall accuracy; NS, SS, LS, TC, and MS denote Natural Science, Social Science, Language Science, Temporal Commonsense, and Mathematics.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 基准包括 M³CoT [8]、MathVista [25]、MMStar [7] 和 MMMU [37]。M³CoT 报告类别级与总体准确率；NS、SS、LS、TC、MS 分别表示自然科学、社会科学、语言科学、时间常识和数学。

### Table 1. Quantitative comparison across multimodal reasoning benchmarks

![Table 1](Reasoning/TrainingFree/Position%20Rebinding%20Cache%20Reuse%20Replay-Free%20Visual%20Revisiting%20for%20Interleaved%20Multimodal%20Reasoning/assets/page_007_fig_table_1.png)

**Caption:** M³CoT is evaluated with category-wise and overall accuracy; MathVista, MMStar, and MMMU use overall accuracy. The best and second-best scores are bold and underlined in the source.

**Caption[CN]:** M³CoT 采用类别级和总体准确率；MathVista、MMStar 与 MMMU 采用总体准确率。原表以粗体和下划线分别标出最佳与次佳结果。

| Model | #Params | Method | NS | SS | LS | TC | MS | M³CoT ALL | MathVista | MMStar | MMMU |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Qwen3-VL | 8B | Baseline | 73.05 | 56.37 | 88.15 | **93.50** | 21.99 | 66.44 | 71.50 | 65.95 | 55.22 |
| Qwen3-VL | 8B | Token-Replay | 75.48 | 59.71 | **89.10** | 91.87 | **24.90** | 68.46 | 72.60 | 68.42 | 59.45 |
| Qwen3-VL | 8B | PRCR (Ours) | **75.86** | **60.19** | 88.63 | 92.68 | 24.07 | **68.68** | **72.80** | **68.96** | **60.07** |
| InternVL3.5 | 8B | Baseline | 67.05 | 51.27 | 90.52 | 85.37 | 31.95 | 64.06 | 73.70 | 68.36 | 65.05 |
| InternVL3.5 | 8B | Token-Replay | 67.94 | 49.36 | **91.94** | **90.24** | 34.44 | 64.75 | 74.30 | 69.05 | 65.82 |
| InternVL3.5 | 8B | PRCR (Ours) | **68.45** | **52.71** | 91.00 | 86.99 | **34.85** | **65.40** | **74.60** | **69.32** | **66.14** |
| InternVL3.5 | 14B | Baseline | 66.16 | 47.93 | 84.83 | 86.99 | 47.72 | 64.28 | 71.90 | 66.76 | 62.02 |
| InternVL3.5 | 14B | Token-Replay | 67.28 | 49.18 | **85.50** | 88.21 | 49.06 | 65.50 | 72.70 | 67.45 | 62.88 |
| InternVL3.5 | 14B | PRCR (Ours) | **67.84** | **49.85** | 85.26 | **88.62** | **49.75** | **65.93** | **73.00** | **67.82** | **63.20** |
| Qwen3-VL | 32B | Baseline | 80.59 | 65.76 | 96.21 | 94.31 | 43.57 | 75.28 | 78.50 | 72.43 | 63.68 |
| Qwen3-VL | 32B | Token-Replay | 82.12 | 67.52 | 96.21 | 95.12 | 45.23 | 76.49 | **79.40** | 73.54 | 64.73 |
| Qwen3-VL | 32B | PRCR (Ours) | **82.45** | **68.10** | **96.44** | **95.53** | **45.80** | **76.86** | 79.20 | **73.91** | **64.89** |

### 4.2 Main Results

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> PRCR achieves comparable or better performance without replay. On Qwen3-VL-8B, M³CoT ALL rises from 66.44% to 68.68%, 2.24 points over baseline and 0.22 over Token-Replay. On InternVL3.5-8B it rises from 64.06% to 65.40%. Gains are consistent across overall scores and extend to most M³CoT categories.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> PRCR 在不回放视觉 token 的情况下取得相当或更优性能。在 Qwen3-VL-8B 上，M³CoT ALL 从 66.44% 提升到 68.68%，较基线高 2.24 点、较 Token-Replay 高 0.22 点；在 InternVL3.5-8B 上则从 64.06% 提升至 65.40%。总体得分上的增益具有一致性，并覆盖多数 M³CoT 类别。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Beyond M³CoT, PRCR remains strong on MathVista, MMStar, and MMMU. For Qwen3-VL-8B it improves the baseline by 1.30, 3.01, and 4.85 points, respectively, preserving the reasoning benefit of replay without repeated forwarding.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在 M³CoT 之外，PRCR 在 MathVista、MMStar 和 MMMU 上同样表现强劲。对 Qwen3-VL-8B，它分别较基线提升 1.30、3.01 和 4.85 点，在免除重复前向传播的同时保留了回放的推理收益。

### Table 2. Effect of position reinsertion strategies on M³CoT

![Table 2](Reasoning/TrainingFree/Position%20Rebinding%20Cache%20Reuse%20Replay-Free%20Visual%20Revisiting%20for%20Interleaved%20Multimodal%20Reasoning/assets/page_008_fig_table_2.png)

**Caption:** Different cache reinsertion strategies. Stuck rate is the fraction of generations collapsing into repeated-token loops.

**Caption[CN]:** 不同缓存重插入策略。卡死率表示坍缩到重复 token 解码循环的生成比例。

| Method | Raw Visual KV Cache | Position Rebinding | Relative Positions | Accuracy ↑ | Stuck Rate ↓ |
|---|:---:|:---:|:---:|---:|---:|
| Direct KV Reuse |  |  |  | 23.50 | 81.04 |
| PRCR w/ LPA | ✓ | ✓ |  | 63.03 | 7.93 |
| PRCR w/ UIR | ✓ | ✓ |  | 67.45 | **0.00** |
| PRCR w/ PCR | ✓ | ✓ | ✓ | **68.68** | **0.00** |

### 4.3 Efficiency and Memory Cost

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Token-Replay forwards selected visual tokens through the full decoder whenever evidence is revisited. PRCR only rebinds keys and concatenates cache. With Qwen3-VL-8B and $K=32$, Token-Replay requires 483.18G FLOPs versus 14.16M for PRCR. With Qwen3-VL-32B and $K=128$, the comparison is 7.75T versus 125.83M FLOPs.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Token-Replay 每次回看证据都要让选中视觉 token 通过完整解码器；PRCR 只需重绑 key 并拼接缓存。Qwen3-VL-8B、$K=32$ 时，Token-Replay 需要 483.18G FLOPs，而 PRCR 仅需 14.16M；Qwen3-VL-32B、$K=128$ 时，两者分别为 7.75T 和 125.83M FLOPs。

### Figure 5. Effect of left extension length $L$

![Figure 5](assets/page_008_fig_fig_5.png)

**Caption:** Effect of left extension length $L$ in PRCR. Accuracy on M³CoT and MathVista peaks at $L=2$.

**Caption[CN]:** PRCR 中左扩展长度 $L$ 的影响。M³CoT 与 MathVista 的准确率均在 $L=2$ 时达到峰值。

### Table 3. Efficiency and memory cost of PRCR

![Table 3](assets/page_009_fig_table_3.png)

**Caption:** Representative visual-revisiting FLOPs and additional raw visual KV memory overhead. PRCR substantially reduces replay computation with small memory overhead.

**Caption[CN]:** 代表性视觉回看 FLOPs 与额外原始视觉 KV 内存开销。PRCR 以较小内存开销显著减少回放计算。

| Model | $K$ | Token-Replay FLOPs | PRCR FLOPs | Extra Memory |
|---|---:|---:|---:|---:|
| Qwen3-VL-8B | 32 | 483.18G | 14.16M | 108MB / 0.64% |
| Qwen3-VL-8B | 128 | 1.93T | 56.62M | 108MB / 0.64% |
| Qwen3-VL-32B | 32 | 1.94T | 31.46M | 192MB / 0.30% |
| Qwen3-VL-32B | 128 | 7.75T | 125.83M | 192MB / 0.30% |

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Raw visual KV storage adds 108MB (0.64%) for Qwen3-VL-8B and 192MB (0.30%) for Qwen3-VL-32B, a moderate and practical cost.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 原始视觉 KV 存储为 Qwen3-VL-8B 增加 108MB（0.64%），为 Qwen3-VL-32B 增加 192MB（0.30%），属于适中且实用的开销。

### Figure 6. Qualitative results of baseline and PRCR

![Figure 6](assets/page_009_fig_fig_6.png)

**Caption:** The baseline predicts 0 inches, whereas PRCR revisits the visual evidence and outputs the correct answer of 2.

**Caption[CN]:** 基线预测 0 英寸，而 PRCR 回看视觉证据并输出正确答案 2。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Exact example text.** Question: `Move the ruler to measure the length of the twig to the nearest inch. The twig is about (_) inches long.` Ground truth: `2`. The baseline judges the twig to run from just after 0 to just before 1 inch and outputs `The final answer is: 0`. PRCR inserts the visual supplement `the endpoints align near 0.2 and 2.2 inches, giving about 2 inches`, reasons that the twig extends from approximately 0.2 to 2.2 inches, and outputs `The final answer is: 2`.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **示例精确文本。** 问题：`移动尺子，将树枝长度测量到最接近的整数英寸。树枝长约 (_) 英寸。` 标准答案：`2`。基线判断树枝从略高于 0 英寸处延伸到略低于 1 英寸处，并输出 `最终答案是：0`。PRCR 插入视觉补充信息 `端点大约与 0.2 和 2.2 英寸对齐，因此长度约为 2 英寸`，推断树枝从约 0.2 英寸延伸到 2.2 英寸，并输出 `最终答案是：2`。英文输出字面量已在前文原样保留。

### 4.4 Ablation Study

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Direct reuse reaches 23.50% accuracy with 81.04% stuck rate. LPA raises accuracy to 63.03% but leaves 7.93% stuck rate because appended entries shift text positions. UIR preserves text continuity and reaches 67.45% with zero stuck rate, but its one-dimensional placement loses relative 2D layout. PCR preserves both and reaches 68.68% with zero stuck rate.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 直接复用的准确率仅 23.50%，卡死率达 81.04%。LPA 将准确率提高到 63.03%，但因追加条目移动文本位置，仍有 7.93% 卡死率。UIR 保持文本连续性，以零卡死率达到 67.45%，但一维放置会丢失相对二维布局。PCR 同时保留两者，以零卡死率达到 68.68%。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Accuracy first improves with $L$ and peaks at $L=2$. Smaller values leave too little space for relative layout; larger values put evidence farther from the current decoding position. The default is therefore $L=2$.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 准确率随 $L$ 增大先上升，并在 $L=2$ 时达到峰值。较小值无法为相对布局提供足够空间，较大值则使证据远离当前解码位置。因此默认设置为 $L=2$。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Leftward re-anchoring consistently outperforms rightward re-anchoring on M³CoT and MathVista. It places reconstructed cache in historical context before the next text token, whereas rightward placement competes with future text positions. PRCR therefore uses leftward re-anchoring.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在 M³CoT 和 MathVista 上，向左重锚定始终优于向右重锚定。前者把重建缓存置于下一文本 token 之前的历史上下文中，后者则会与未来文本位置竞争。因此 PRCR 默认采用向左重锚定。

### 4.5 Qualitative Results

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In Figure 6, the baseline identifies the ruler and twig but mislocalizes endpoints and predicts 0 inches. PRCR revisits evidence, aligns endpoints with the ruler, and obtains about 2 inches, improving intermediate visual grounding rather than merely correcting the final answer.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在 Figure 6 中，基线识别出尺子和树枝，却错误定位端点并预测 0 英寸。PRCR 回看证据，将端点与尺子对齐并得到约 2 英寸，说明它改善的是中间视觉落地，而非仅修正最终答案。

### Figure 7. Effect of PRCR on next-token generation

![Figure 7](assets/page_010_fig_fig_7.png)

**Caption:** (a) Next-token probabilities after inserting the visual KV cache at token 80. (b) Corresponding output entropy. Shaded areas show changes due to the cache.

**Caption[CN]:** (a) 在第 80 个 token 插入视觉 KV 缓存后的下一 token 概率。(b) 相应输出熵。阴影区域表示缓存插入造成的变化。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> PRCR triggers ADS at token 80. After insertion, next-token probabilities rise and entropy falls, indicating stabilized predictions and reduced uncertainty. Position-compatible reinsertion therefore improves both fine-grained correction and subsequent generation stability.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> PRCR 在第 80 个 token 处触发 ADS。插入后，下一 token 概率上升、熵下降，表明预测更稳定且不确定性降低。因此，位置兼容重插入既改善细粒度纠错，也提高后续生成稳定性。

### 4.6 Visualization and Analysis of PRCR Attention

### Figure 8. Attention visualization for PRCR

![Figure 8](assets/page_011_fig_fig_8.png)

**Caption:** (a) Token-Replay: attention over inserted visual tokens. (b) PRCR: attention over reconstructed visual KV cache. Green shading indicates attention weight (low to high).

**Caption[CN]:** (a) Token-Replay：插入视觉 token 上的注意力。(b) PRCR：重建视觉 KV 缓存上的注意力。绿色阴影表示由低到高的注意力权重。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Token-Replay maintains stable attention over inserted visual tokens and generated text but repeatedly computes visual inputs. PRCR integrates reconstructed visual KV while preserving stable attention over reasoning text without recomputation. It eliminates stale-binding interference, produces more focused and less noisy attention, and greatly lowers visual-revisiting computation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Token-Replay 在插入视觉 token 和生成文本上保持稳定注意力，却需要重复计算视觉输入。PRCR 无需重算即可整合重建视觉 KV，并保持推理文本上的稳定注意力。它消除了过期位置绑定的干扰，使注意力更集中、噪声更低，同时显著减少视觉回看计算。

## 5. Related Work

### 5.1 Multimodal Chain-of-Thought Reasoning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> MCoT [8, 10, 19, 24, 26, 34, 39] extends language CoT [32, 33, 35] to vision-language tasks by generating rationales conditioned on images. Progress is supported by Flamingo, BLIP-2, InstructBLIP, LLaVA, MiniGPT-4, Qwen-VL, and extensions [1, 3, 13, 20–22, 42]. These methods usually reason once in fixed visual context and cannot revisit evidence during generation; PRCR instead reuses already encoded evidence without re-encoding.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> MCoT [8, 10, 19, 24, 26, 34, 39] 通过生成以图像为条件的理由，将语言 CoT [32, 33, 35] 扩展到视觉—语言任务。Flamingo、BLIP-2、InstructBLIP、LLaVA、MiniGPT-4、Qwen-VL 及其扩展推动了这一进展 [1, 3, 13, 20–22, 42]。这些方法通常只在固定视觉上下文中推理一次，无法在生成期间回看证据；PRCR 则无需重新编码即可复用已编码证据。

### 5.2 Interleaved Multimodal Chain-of-Thought

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> ICoT inserts visual evidence into reasoning trajectories. Early methods use interleaved tokens or attention-driven selection [14]; dynamic visual-thought methods select evidence according to evolving state [9, 15, 23, 28]; other studies examine visual thoughts, chain-of-multimodal thought, action-oriented visual reasoning [10–12, 41], and generated or latent visual intermediates [5, 6, 18, 38, 40]. These methods demonstrate the value of revisiting but commonly require token replay, cropped regions, generated intermediates, latent reasoning, extra computation, or training. PRCR is complementary: given selected evidence, it reconstructs position-compatible cache entries for replay-free reuse.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> ICoT 将视觉证据插入推理轨迹。早期方法使用交错视觉 token 或注意力驱动选择 [14]；动态视觉思维方法依据不断演化的推理状态选择证据 [9, 15, 23, 28]；其他研究考察视觉思维、多模态思维链、面向动作的视觉推理 [10–12, 41]，以及生成式或潜空间视觉中间体 [5, 6, 18, 38, 40]。这些方法证明视觉回看有价值，却通常需要 Token 回放、裁剪区域、生成中间体、潜空间推理、额外计算或训练。PRCR 与其互补：给定选中证据，它重建位置兼容缓存条目以实现免回放复用。

## 6. Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Directly copying historical visual KV cache is not a valid substitute for replay because position-bound keys disrupt later autoregressive decoding. PRCR stores raw pre-RoPE visual KV and reconstructs position-compatible entries at revisiting time. It achieves replay-level or better benchmark performance while substantially reducing computation, establishing position rebinding as an effective principle for efficient visual evidence reuse.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 直接复制历史视觉 KV 缓存不能有效替代回放，因为带位置绑定的 key 会破坏后续自回归解码。PRCR 存储原始 pre-RoPE 视觉 KV，并在回看时重建位置兼容条目。它在显著降低计算量的同时达到回放水平或更优的基准性能，说明位置重绑定是高效视觉证据复用的一项有效原则。

## 7. Limitations and Future Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> PRCR fully relies on visual KV generated during multimodal prefill. Some replay methods crop regions and apply local scaling or zoom before re-encoding. Such scaled features have no corresponding prefill KV entries, so PRCR cannot reuse them. Under dynamic resolution adjustment or local zoom, cache reuse fails and its computational advantage is lost.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> PRCR 完全依赖多模态预填充期间生成的视觉 KV。一些回放方法先裁剪区域并执行局部缩放或放大，再重新编码。这些缩放特征没有对应的预填充 KV 条目，因此 PRCR 无法复用。在动态分辨率调整或局部放大场景中，缓存复用会失效，其计算优势也随之消失。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Two directions are proposed. Multi-scale KV Prefill generates cache entries at several resolutions for key regions so scaled tokens can reuse matching entries. Learned Scale-aware Rebinding uses a mapping network to project original KV onto visual tokens at different resolutions, enabling partial reuse while preserving attention and spatial consistency.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 论文提出两个方向。多尺度 KV 预填充为关键区域在多个分辨率下生成缓存条目，使缩放后的 token 能复用匹配条目。学习式尺度感知重绑定使用映射网络，将原始 KV 投影到不同分辨率的视觉 token 上，在保持注意力模式和空间一致性的同时实现部分缓存复用。

## References

> **Reference policy / 参考文献策略：** The 42 entries below are retained in their original searchable bibliographic form. Titles, author names, venues, page numbers, years, and arXiv identifiers are not translated, preventing ambiguity in literature retrieval. / 以下 42 条文献保留原始可检索书目信息；题名、作者、会议期刊、页码、年份和 arXiv 标识不翻译，以免影响检索。

1. Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, Iain Barr, Yana Hasson, Karel Lenc, Arthur Mensch, Katherine Millican, Malcolm Reynolds, et al. Flamingo: a visual language model for few-shot learning. *Advances in Neural Information Processing Systems*, 35:23716–23736, 2022.
2. Xiang An, Yin Xie, Kaicheng Yang, Wenkang Zhang, Xiuwei Zhao, Zheng Cheng, Yirui Wang, Songcen Xu, Changrui Chen, Chunsheng Wu, Huajie Tan, Chunyuan Li, Jing Yang, Jie Yu, Xiyao Wang, Bin Qin, Yumeng Wang, Zizhen Yan, Ziyong Feng, Ziwei Liu, Bo Li, and Jiankang Deng. LLaVA-OneVision-1.5: Fully open framework for democratized multimodal training. *arXiv:2509.23661*, 2025.
3. Jinze Bai, Shuai Bai, Shusheng Yang, Shijie Wang, Sinan Tan, Peng Wang, Junyang Lin, Chang Zhou, and Jingren Zhou. Qwen-VL: A versatile vision-language model for understanding, localization, text reading, and beyond. *arXiv:2308.12966*, 2023.
4. Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang Gao, Chunjiang Ge, et al. Qwen3-VL technical report. *arXiv:2511.21631*, 2025.
5. Mahtab Bigverdi, Zelun Luo, Cheng-Yu Hsieh, Ethan Shen, Dongping Chen, Linda G. Shapiro, and Ranjay Krishna. Perception tokens enhance visual reasoning in multimodal language models. *CVPR*, pp. 3836–3845, 2025.
6. Chao Chen, Zhixin Ma, Yongqi Li, Yupeng Hu, Yinwei Wei, Wenjie Li, and Liqiang Nie. Reasoning in the dark: Interleaved vision-text reasoning in latent space. *arXiv:2510.12603*, 2025.
7. Lin Chen, Jinsong Li, Xiaoyi Dong, Pan Zhang, Yuhang Zang, Zehui Chen, Haodong Duan, Jiaqi Wang, Yu Qiao, Dahua Lin, et al. Are we on the right way for evaluating large vision-language models? *NeurIPS*, 37:27056–27087, 2024.
8. Qiguang Chen, Libo Qin, Jin Zhang, Zhi Chen, Xiao Xu, and Wanxiang Che. M³CoT: A novel benchmark for multi-domain multi-step multi-modal chain-of-thought. *ACL*, pp. 8199–8221, 2024.
9. Xinyan Chen, Renrui Zhang, Dongzhi Jiang, Aojun Zhou, Shilin Yan, Weifeng Lin, and Hongsheng Li. MINT-CoT: Enabling interleaved visual tokens in mathematical chain-of-thought reasoning. *NeurIPS*, 2025.
10. Zihui Cheng, Qiguang Chen, Xiao Xu, Jiaqi Wang, Weiyun Wang, Hao Fei, Yidong Wang, Alex Jinpeng Wang, Zhi Chen, Wanxiang Che, and Libo Qin. Visual thoughts: A unified perspective of understanding multimodal chain-of-thought. *NeurIPS*, 2025.
11. Zihui Cheng, Qiguang Chen, Jin Zhang, Hao Fei, Xiaocheng Feng, Wanxiang Che, Min Li, and Libo Qin. Comt: A novel benchmark for chain of multi-modal thought on large vision-language models. *AAAI*, 39:23678–23686, 2025.
12. Charles Corbière, Simon Roburin, Syrielle Montariol, Antoine Bosselut, and Alexandre Alahi. Drivingvqa: A dataset for interleaved visual chain-of-thought in real-world driving scenarios. *Findings of EACL*, pp. 3309–3333, 2026.
13. Wenliang Dai, Junnan Li, Dongxu Li, Anthony Tiong, Junqi Zhao, Weisheng Wang, Boyang Li, Pascale N. Fung, and Steven Hoi. InstructBLIP: Towards general-purpose vision-language models with instruction tuning. Vol. 36, pp. 49250–49267, 2023.
14. Jun Gao, Yongqi Li, Ziqiang Cao, and Wenjie Li. Interleaved-modal chain-of-thought. *CVPR*, pp. 19520–19529, 2025.
15. Guangfu Guo, Xiaoqian Lu, Yue Feng, and Mingming Sun. Beyond static visual tokens: Structured sequential visual chain-of-thought reasoning. *arXiv:2603.26737*, 2026.
16. Yongxin Guo, Jingyu Liu, Mingda Li, Dingxin Cheng, Xiaoying Tang, Dianbo Sui, Qingbin Liu, Xi Chen, and Kevin Zhao. Vtg-llm: Integrating timestamp knowledge into video llms for enhanced video temporal grounding. *AAAI*, 39:3302–3310, 2025.
17. Wenyi Hong et al. GLM-4.1V-thinking: Towards versatile multimodal reasoning with scalable reinforcement learning. *arXiv:2507.01006*, 2025.
18. Chaoya Jiang, Yongrui Heng, Wei Ye, Han Yang, Haiyang Xu, Ming Yan, Ji Zhang, Fei Huang, and Shikun Zhang. Vlm-R3: Region recognition, reasoning, and refinement for enhanced multimodal chain-of-thought. *arXiv:2505.16192*, 2025.
19. Dongzhi Jiang, Renrui Zhang, Ziyu Guo, Yanwei Li, Yu Qi, Xinyan Chen, Liuhui Wang, Jianhan Jin, Claire Guo, Shen Yan, Bo Zhang, Chaoyou Fu, Peng Gao, and Hongsheng Li. MME-CoT: Benchmarking chain-of-thought in large multimodal models for reasoning quality, robustness, and efficiency. *ICML*, pp. 27793–27830, 2025.
20. Junnan Li, Dongxu Li, Silvio Savarese, and Steven C. H. Hoi. BLIP-2: Bootstrapping language-image pre-training with frozen image encoders and large language models. *ICML*, pp. 19730–19742, 2023.
21. Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee. Visual instruction tuning. *NeurIPS*, 36:34892–34916, 2023.
22. Haotian Liu, Chunyuan Li, Yuheng Li, and Yong Jae Lee. Improved baselines with visual instruction tuning. *CVPR*, pp. 26296–26306, 2024.
23. Xu Liu, Yongheng Zhang, Qiguang Chen, Yao Li, Sheng Wang, and Libo Qin. Let’s think with images efficiently! An interleaved-modal chain-of-thought reasoning framework with dynamic and precise visual thoughts. *AAAI*, 40:32213–32221, 2026.
24. Pan Lu, Swaroop Mishra, Tanglin Xia, Liang Qiu, Kai-Wei Chang, Song-Chun Zhu, Oyvind Tafjord, Peter Clark, and Ashwin Kalyan. Learn to explain: Multimodal reasoning via thought chains for science question answering. *NeurIPS*, 35:2507–2521, 2022.
25. Pan Lu, Hritik Bansal, Tony Xia, Jiacheng Liu, Chunyang Li, Hannaneh Hajishirzi, Hao Cheng, Kai-Wei Chang, Michel Galley, and Jianfeng Gao. MathVista: Evaluating mathematical reasoning of foundation models in visual contexts. *ICLR*, 2024.
26. Hao Shao, Shengju Qian, Han Xiao, Guanglu Song, Zhuofan Zong, Letian Wang, Yu Liu, and Hongsheng Li. Visual CoT: Advancing multi-modal language models with a comprehensive dataset and benchmark for chain-of-thought reasoning. *NeurIPS*, 37:8612–8642, 2024.
27. Kimi Team, Angang Du, Bohong Yin, Bowei Xing, Bowen Qu, Bowen Wang, Cheng Chen, Chenlin Zhang, Chenzhuang Du, Chu Wei, et al. Kimi-vl technical report. *arXiv:2504.07491*, 2025.
28. Chongjun Tu, Peng Ye, Dongzhan Zhou, Tao Chen, and Wanli Ouyang. Mitigating low-quality reasoning in MLLMs: Self-driven refined multimodal CoT with selective thinking and step-wise visual enhancement. *AAAI*, 40:9576–9584, 2026.
29. Mengzhao Wang, Huafeng Li, Yafei Zhang, Jinxing Li, Dapeng Tao, and Zhengtao Yu. Disentangling inter- and intra-video relations for multi-event video-text retrieval and grounding. *IEEE Transactions on Image Processing*, 34:7558–7571, 2025.
30. Weiyun Wang, Zhangwei Gao, Lixin Gu, Hengjun Pu, Long Cui, Xingguang Wei, Zhaoyang Liu, Linglin Jing, Shenglong Ye, Jie Shao, et al. InternVL3.5: Advancing open-source multimodal models in versatility, reasoning, and efficiency. *arXiv:2508.18265*, 2025.
31. Xizi Wang, Feng Cheng, Ziyang Wang, Huiyu Wang, Md Mohaiminul Islam, Lorenzo Torresani, Mohit Bansal, Gedas Bertasius, and David Crandall. TimeRefine: Temporal grounding with time refining video LLM. *WACV*, pp. 5067–5078, 2026.
32. Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought reasoning in language models. *ICLR*, 2023.
33. Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, Brian Ichter, Fei Xia, Ed H. Chi, Quoc V. Le, and Denny Zhou. Chain-of-thought prompting elicits reasoning in large language models. *NeurIPS*, 35:24824–24837, 2022.
34. Guowei Xu, Peng Jin, Ziang Wu, Hao Li, Yibing Song, Lichao Sun, and Li Yuan. LLaVA-CoT: Let vision language models reason step-by-step. *ICCV*, pp. 2087–2098, 2025.
35. Chenxiao Yang, Zhiyuan Li, and David Wipf. Chain-of-thought provably enables learning the (otherwise) unlearnable. *ICLR*, 2025.
36. Zuhao Yang, Yingchen Yu, Yunqing Zhao, Shijian Lu, and Song Bai. TimeExpert: An expert-guided video LLM for video temporal grounding. *ICCV*, pp. 24286–24296, 2025.
37. Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng, Ruoqi Liu, Ge Zhang, Samuel Stevens, Dongfu Jiang, Weiming Ren, Yuxuan Sun, et al. MMMU: A massive multi-discipline multimodal understanding and reasoning benchmark for expert AGI. *CVPR*, pp. 9556–9567, 2024.
38. Huanyu Zhang, Wenshan Wu, Chengzu Li, Ning Shang, Yan Xia, Yangyu Huang, Yifan Zhang, Li Dong, Zhang Zhang, Liang Wang, Tieniu Tan, and Furu Wei. Latent sketchpad: Sketching visual thoughts to elicit multimodal reasoning in MLLMs. *arXiv:2510.24514*, 2025.
39. Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao, George Karypis, and Alexander J. Smola. Multimodal chain-of-thought reasoning in language models. *arXiv:2302.00923*, 2023.
40. Kesen Zhao, Beier Zhu, Qianru Sun, and Hanwang Zhang. Unsupervised visual chain-of-thought reasoning via preference optimization. *ICCV*, pp. 2303–2312, 2025.
41. Qingqing Zhao, Yao Lu, Moo Jin Kim, Zipeng Fu, Zhuoyang Zhang, Yecheng Wu, Zhaoshuo Li, Qianli Ma, Song Han, Chelsea Finn, et al. CoT-VLA: Visual chain-of-thought reasoning for vision-language-action models. *CVPR*, pp. 1702–1713, 2025.
42. Deyao Zhu, Jun Chen, Xiaoqian Shen, Xiang Li, and Mohamed Elhoseiny. MiniGPT-4: Enhancing vision-language understanding with advanced large language models. *arXiv:2304.10592*, 2023.
