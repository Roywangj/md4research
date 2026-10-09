# MINT-CoT: Enabling Interleaved Visual Tokens in Mathematical Chain-of-Thought Reasoning

> **中文题名：** MINT-CoT：在数学思维链推理中启用交错视觉标记  
> **作者：** Xinyan Chen, Renrui Zhang, Dongzhi Jiang, Aojun Zhou, Shilin Yan, Weifeng Lin, Hongsheng Li  
> **出处：** arXiv:2506.05331，2025-06-05  
> **论文类型：** 方法 / train / mathematical visual reasoning / interleaved visual tokens  
> **源文件：** `Chen 等 - 2025 - MINT-CoT Enabling Interleaved Visual Tokens in Mathematical Chain-of-Thought Reasoning.pdf`  
> **阅读器：** 全文英中对照式阅读件；源格式为 `pdf-text`；图表按首次实质讨论位置重排。页码与稳定块 ID 见 `source_map.json`。

## Page / Section Index

- Abstract: page 1
- Introduction: pages 1-3
- Related Work: pages 3-4
- Method: pages 4-7
- Experiments: pages 7-10
- Conclusion: pages 10-11
- Appendix: pages 18-22

## Terminology Ledger

| Canonical term | 中文 | First-use decision |
|---|---|---|
| MINT-CoT | MINT-CoT | 方法名保留 |
| Mathematical INterleaved Tokens | 数学交错标记 | 保留 MINT 缩写 |
| Interleave Token | 交错标记 | 触发视觉 token 选择的特殊 token |
| visual token | 视觉标记 | 指视觉编码器输出 token |
| interleaved CoT | 交错思维链 | 文本步骤和视觉 token 交替出现 |
| post interleave projector | 交错后投影器 | 用于映射交错标记隐藏状态 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Chain-of-thought has improved mathematical reasoning in language models, but extending it to multimodal mathematical reasoning remains difficult.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 思维链显著增强了语言模型的数学推理，但把它扩展到多模态数学推理仍然困难。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Existing methods either use text-only reasoning for images or interleave coarse visual regions, but they depend on box-shaped regions, limited vision encoders, or external visual editing.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 现有方法要么对图像采用纯文本推理，要么插入粗粒度视觉区域，但它们依赖框形区域、受限视觉编码器，或外部视觉修改能力。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> MINT-CoT introduces mathematical interleaved tokens. It uses an Interleave Token to select relevant visual tokens of arbitrary shapes inside mathematical figures.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> MINT-CoT 引入数学交错标记。它用交错标记在数学图形中选择任意形状的相关视觉 token。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The authors build a 54K dataset aligning reasoning steps with token-level visual regions and train MINT-CoT-7B through text-only CoT SFT, interleaved CoT SFT, and interleaved CoT RL.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 作者构建了 54K 数据集，把每个推理步骤与 token 级视觉区域对齐，并通过纯文本 CoT 监督微调、交错 CoT 监督微调和交错 CoT 强化学习训练 MINT-CoT-7B。

## Introduction

### Figure 1. Three Reasoning Paradigms

![Figure 1](Reasoning/Train/MINT-CoT%20Enabling%20Interleaved%20Visual%20Tokens%20in%20Mathematical%20Chain-of-Thought%20Reasoning/assets/page_002_fig_figure_1.png)

**Caption:** Text-only CoT, box-shaped visual CoT, and visual interleaved CoT for mathematical reasoning.

**Caption[CN]:** 数学推理中的纯文本 CoT、框形视觉 CoT 和视觉交错 CoT。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Mathematical figures often require linking symbols, lines, angles, and regions to each step of reasoning. Text-only CoT cannot expose this link.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 数学图形常常要求把符号、线段、角度和区域连接到每一步推理。纯文本 CoT 无法显式展示这种连接。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Box-shaped visual regions are also limited because the useful evidence in mathematical diagrams can be sparse, symbolic, and irregularly shaped.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 框形视觉区域也有局限，因为数学图中的有用证据可能很稀疏、符号化，而且形状并不规则。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The paper's core idea is to let the model insert selected visual tokens directly into the reasoning sequence before the textual step that needs them.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 论文的核心想法是让模型在需要视觉证据的文本步骤之前，直接把选中的视觉 token 插入推理序列。

## Method

### Figure 2. MINT-CoT Framework

![Figure 2](assets/page_004_fig_figure_2.png)

**Caption:** The Interleave Token selects visual tokens through similarity scores and inserts them before reasoning steps.

**Caption[CN]:** 交错标记通过相似度分数选择视觉 token，并把它们插入到推理步骤之前。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The visual encoder produces visual features $V=\{v_\tau\}_{\tau=1}^N$. Standard CoT then generates only text reasoning steps.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 视觉编码器产生视觉特征 $V=\{v_\tau\}_{\tau=1}^N$。标准 CoT 随后只生成文本推理步骤。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> MINT-CoT adds an Interleave Token before each reasoning step. Its hidden state is projected and compared with projected visual token states.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> MINT-CoT 在每个推理步骤前加入交错标记。该标记的隐藏状态经过投影后，与视觉 token 状态的投影结果比较。

$$
\alpha^{(i)}=\gamma\cdot \cos(P_{\text{post\_intlv}}(h^{(i)}_{\text{post\_intlv}}),P_{\text{post\_vis}}(h_{\text{post\_vis}})).
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Visual tokens with similarity scores above a threshold are selected and inserted before the corresponding reasoning step.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 相似度高于阈值的视觉 token 会被选中，并插入到对应推理步骤之前。

$$
\{v^{(i)}\}=\{v\mid \alpha^{(i)}>\theta\}.
$$

### Figure 3. Dataset Construction

![Figure 3](assets/page_006_fig_figure_3.png)

**Caption:** Grid images, OCR, keyword extraction, and keyword-to-grid annotation create visual interleaved CoT data.

**Caption[CN]:** 通过网格图像、OCR、关键词抽取和关键词到网格的标注，构造视觉交错 CoT 数据。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The dataset is built from mathematical problems. The pipeline grids images, applies OCR, extracts step-level keywords, and annotates the corresponding grid indices.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 数据集来自数学题。管线先把图像网格化，再做 OCR，抽取每步推理中的关键词，并标注对应网格索引。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The final dataset contains 54K samples. Each sample includes a problem, an image, and a visual interleaved CoT response.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 最终数据集包含 54K 样本。每个样本包括问题、图像和一条视觉交错 CoT 回答。

## Training Strategy

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Stage 1 trains the base model with text-only CoT data so it learns the general reasoning format.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 第一阶段用纯文本 CoT 数据训练基础模型，让它先学会通用推理格式。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Stage 2 uses interleaved CoT SFT. The loss combines textual next-token cross entropy and a binary cross-entropy loss for visual token selection.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 第二阶段使用交错 CoT 监督微调。损失同时包含文本 next-token 交叉熵，以及视觉 token 选择的二元交叉熵。

$$
L=L_{\text{CE}}+L_{\text{BCE}}.
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Stage 3 applies GRPO. The reward is answer correctness, and the advantage is computed through group-wise comparison.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 第三阶段使用 GRPO。奖励来自答案正确性，优势值通过组内比较计算。

## Experiments

### Table 1. MathVista-Math

![Table 1](Reasoning/Train/MINT-CoT%20Enabling%20Interleaved%20Visual%20Tokens%20in%20Mathematical%20Chain-of-Thought%20Reasoning/assets/page_008_fig_table_1.png)

**Caption:** MINT-CoT-7B reaches the best open-source result on the mathematical subset of MathVista.

**Caption[CN]:** MINT-CoT-7B 在 MathVista 数学子集上取得列出的最佳开源结果。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> MINT-CoT-7B reaches 73.70 on MathVista-Math All, compared with 41.11 for the Qwen2-VL-7B-Instruct baseline.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> MINT-CoT-7B 在 MathVista-Math All 上达到 73.70，而 Qwen2-VL-7B-Instruct 基线为 41.11。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> On GeoQA, MINT-CoT-7B reaches 64.72, compared with 37.80 for the baseline. On MMStar-Math, it reaches 69.6, compared with 46.4.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在 GeoQA 上，MINT-CoT-7B 达到 64.72，基线为 37.80。在 MMStar-Math 上，它达到 69.6，基线为 46.4。

### Table 4. Training Stage Ablation

![Table 4](assets/page_009_fig_table_4.png)

**Caption:** Text-only SFT, interleaved SFT, and interleaved RL each add performance.

**Caption[CN]:** 纯文本监督微调、交错监督微调和交错强化学习分别带来增益。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Text-only CoT SFT raises MathVista-Math All from 41.11 to 64.07. Interleaved CoT SFT raises it to 67.78. Interleaved CoT RL raises it to 73.70.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 纯文本 CoT 监督微调把 MathVista-Math All 从 41.11 提升到 64.07。交错 CoT 监督微调进一步到 67.78。交错 CoT 强化学习最终提升到 73.70。

### Table 5. Interleaving Method Ablation

![Table 5](assets/page_009_fig_table_5.png)

**Caption:** Original-image interleaving is much weaker than selected visual token interleaving.

**Caption[CN]:** 插入原图远弱于选择性视觉 token 交错。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Original Image CoT SFT drops MathVista-Math All to 40.37, while Interleaved CoT SFT reaches 67.78.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> Original Image CoT SFT 在 MathVista-Math All 上降到 40.37，而 Interleaved CoT SFT 达到 67.78。

### Figure 5. Qualitative Result

![Figure 5](assets/page_010_fig_figure_5.png)

**Caption:** The baseline gives a wrong geometry answer, while MINT-CoT selects relevant visual tokens during reasoning.

**Caption[CN]:** 基线给出错误几何答案，而 MINT-CoT 在推理中选择相关视觉 token。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The qualitative example shows that selected visual tokens can align with a specific reasoning step, rather than serving as a generic image reminder.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 定性示例显示，被选中的视觉 token 可以对齐到具体推理步骤，而不是泛泛地提醒模型“看图”。

## Critical Reading Notes

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The key lesson is that visual interleaving must be selective. Re-inserting the whole image can be worse than not interleaving at all.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 关键启发是视觉交错必须选择性进行。把整张图反复插回去，可能比完全不交错还差。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For 3D reasoning, the analogous move would be selecting task-relevant view tokens, object tokens, or spatial memory cells before each reasoning step.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 对 3D reasoning 来说，对应做法是在每个推理步骤前选择任务相关的视角 token、对象 token 或空间记忆单元。
