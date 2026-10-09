---
tags:
  - papers/visually-grounded-reasoning
  - papers/multimodal-cot
  - papers/training-free
aliases:
  - "DaP-ICoT"
  - "Let's Think with Images Efficiently"
date: 2026-03-23
doi: 10.48550/arXiv.2603.21754
arxiv_id: 2603.21754
---

# Let's Think with Images Efficiently! An Interleaved-Modal Chain-of-Thought Reasoning Framework with Dynamic and Precise Visual Thoughts

## 核心信息

- 标题: Let's Think with Images Efficiently! An Interleaved-Modal Chain-of-Thought Reasoning Framework with Dynamic and Precise Visual Thoughts
- 标题翻译: 让我们高效地用图像思考：带有动态与精确视觉思考的交错模态思维链推理框架
- 作者: Xu Liu, Yongheng Zhang, Qiguang Chen, Yao Li, Sheng Wang, Libo Qin
- 机构: Harbin Institute of Technology, Shenzhen; Central South University; Text Computing and Cognitive Intelligence Ministry of Education Engineering Research Center, Guizhou University; Shanghai Aviation Electric Co., Ltd
- 发表时间: 2026-03-23
- 发表渠道: arXiv
- DOI: 10.48550/arXiv.2603.21754
- arXiv: 2603.21754
- 论文链接: http://arxiv.org/abs/2603.21754
- 代码 / 项目: https://github.com/67L1/DaP-ICoT
- 数据 / 资源: M3CoT；ScienceQA；MME；Chameleon-7B；LLaVA-V1.5-7B/13B；Qwen2-VL-2B/7B
- 论文类型: AI 方法；免训练多模态推理；高效交错视觉思维链

## 原文摘要翻译

近期，交错模态思维链通过同时利用多模态输入与输出，在视觉推理中取得了明显进展。但当前 ICoT 方法仍有两个关键限制：第一，视觉思考的位置是静态的，通常在固定步骤插入视觉信息，导致推理僵硬且计算开销偏大；第二，视觉思考的表示是破碎的，插入的视觉标记常常不连续，也缺少语义连贯性。

为解决这些问题，作者提出 DaP-ICoT，即带有动态与精确视觉思考的交错模态思维链。方法包含两个模块：动态视觉思考集成根据推理需要自适应引入视觉输入，从而减少冗余并提升效率；精确视觉思考引导则保证被插入的视觉表示在语义上完整、在上下文上对齐。

在多个基准和多种模型上的实验表明，DaP-ICoT 取得了领先性能。同时，它显著减少了插入图像数量，使标记消耗下降 72.6%，从而实现更高效的 ICoT 推理。

## 创新点

1. 把 ICoT 的问题拆成两个更具体的失败模式：视觉插入位置固定，以及插入视觉表示破碎。这比单纯说“ICoT 很贵”更准确。
2. 用 logit 间隔作为内部置信度信号，决定下一步是否需要视觉思考。这个设计让视觉插入从固定调度变成按需调度。
3. 用 SAM2 先生成对象级候选，再根据当前文本理由选择最相关对象图像，避免把零散视觉标记直接插入推理序列。
4. 将效果和效率放在同一个论证里。论文不仅报告 M3CoT、ScienceQA、MME 上的准确率，还统计标记消耗、图像插入频率和置信度变化。
5. 方法不更新 MLLM 参数，因此属于 `TrainingFree` 路线；但它依赖外部分割工具，不能理解为完全无视觉工具。
6. 相对 ICoT，它的贡献更像“推理时视觉证据控制器”：什么时候取证、取哪一块、取完后怎么插回推理。

## 一句话总结

DaP-ICoT 的核心不是让模型更频繁地“用图思考”，而是让模型只在低置信度时插入一个完整、相关的对象图像；它是 ICoT 之后更强调效率和视觉表示质量的免训练改造。

## 研究问题

ICoT 的出发点是对的：纯文本思维链很难精确表达“这一步推理对应图中哪一块证据”。但早期 ICoT 有一个很直接的副作用：它倾向于在每一步后都插入视觉内容。这样做会带来大量视觉标记开销，而且很多插入内容其实并没有被当前推理真正需要。

![Figure 1](Reasoning/TrainingFree/Lets%20Think%20with%20Images%20Efficiently%20An%20Interleaved-Modal%20Chain-of-Thought%20Reasoning%20Framework%20with%20Dynamic%20and%20Precise%20Visual%20Thoughts/images/page_001_fig_figure_1.png)
*论文原图编号：Figure 1。当前 ICoT 固定插入视觉思考，且视觉表示可能破碎；DaP-ICoT 只在低置信度时插入更完整的分割视觉内容。*

第二个问题更隐蔽：早期方法常从图像中选择离散视觉标记。离散标记在空间上可能不连续，在语义上也可能不是完整对象。模型后续看到的不是“一个完整路牌”或“一把伞”，而是一组被注意力选出来的碎片。这样的视觉思考虽然形式上是视觉的，实际可能难以提供稳定证据。

所以 DaP-ICoT 的问题定义可以概括为：视觉思考不应该越多越好，也不应该越细越好。更合理的目标是，在推理不确定时插入一个语义完整、上下文相关、成本可控的视觉证据。

## 数据与任务定义

### 输入与输出

输入是图像、问题和提示。输出是交错的文本理由与视觉思考，最终给出答案。与 ICoT 不同，DaP-ICoT 不默认每一步都加入视觉内容，而是根据当前文本理由的置信度决定下一步是否需要视觉输入。

### 基准与指标

| 基准 | 任务重点 | 指标 |
|---|---|---|
| M3CoT | 多领域、多步、多模态思维链推理 | accuracy |
| ScienceQA | 科学问答与视觉语言推理 | accuracy |
| MME | 综合多模态感知与认知评测 | perception + cognition score |

### 模型与对比方法

作者评估了五个骨干：

- `Chameleon-7B`。
- `LLaVA-V1.5` 的 7B 和 13B。
- `Qwen2-VL` 的 2B 和 7B。

对比方法包括 Direct、MMCoT、DDCoT、SCAFFOLD、CCoT 和 ICoT。

所有方法用官方开源实现复现实验一次，并在零样本与单样本设置下评估。DaP-ICoT 的置信度阈值 $\tau$ 在 M3CoT 验证集上从 $[0,1]$ 范围搜索得到。

## 方法主线

### 机制流程

1. 输入图像、问题和当前提示，模型先生成文本理由 $T_t$。
2. DVTI 提取每个位置第一候选与第二候选的 logit 间隔，得到整段理由的置信度 $C_t$。
3. 若 $C_t<\tau$，PVTG 提取 SAM2 对象候选并与当前理由对齐；否则直接继续文本推理。
4. 将选中对象图像拼接进推理序列，更新上下文并生成下一步理由和最终答案。

![Figure 2](Reasoning/TrainingFree/Lets%20Think%20with%20Images%20Efficiently%20An%20Interleaved-Modal%20Chain-of-Thought%20Reasoning%20Framework%20with%20Dynamic%20and%20Precise%20Visual%20Thoughts/images/page_003_fig_figure_2.png)
*论文原图编号：Figure 2。DaP-ICoT 总体流程：左侧用 logit 间隔估计是否需要视觉输入，右侧用 SAM2 候选和相关性匹配选择精确视觉思考。*

### DVTI：何时需要视觉思考

DVTI 的置信度来自 logit 间隔。对当前文本理由 $T_t$ 的第 $i$ 个解码位置，局部置信度是：

$$
\delta_i=\ell_{i,w(1)}-\ell_{i,w(2)}.
$$

这里 $\ell_{i,w(1)}$ 和 $\ell_{i,w(2)}$ 分别是第一候选与第二候选的 logit。间隔越大，说明模型对当前标记选择越果断。

整段理由的置信度是平均 logit 间隔：

$$
C_t=\frac{1}{|T_t|}\sum_{i=1}^{|T_t|}\delta_i.
$$

视觉插入规则为：

$$
I_{t+1}=
\begin{cases}
I_{\mathrm{vision}}, & C_t<\tau,\\
\varnothing, & \mathrm{otherwise}.
\end{cases}
$$

这一步是论文最关键的效率来源。ICoT 的默认策略是“每一步后插入”，DaP-ICoT 的策略是“置信度不足时再插入”。因此它天然会减少视觉标记进入上下文的次数。

### PVTG：插入什么视觉思考

PVTG 处理的是另一个问题：如果确实需要视觉输入，应该插入怎样的视觉内容。作者用 SAM2 对原图做对象级分割，得到候选对象集合：

$$
O=\{O_1,O_2,\ldots,O_N\}.
$$

当 DVTI 判断第 $t$ 步需要视觉输入时，PVTG 计算当前文本理由 $T_t$ 与每个候选对象图像 $O_i$ 的相关性：

$$
s_i=f_{\mathrm{attn}}(T_t,O_i).
$$

然后选择最高分对象：

$$
\hat{O}=\arg\max_{O_i\in O}s_i.
$$

最后把对象图像插入当前推理序列：

$$
R_{t\to v}=R_t\oplus\hat{O},
$$

并继续生成：

$$
R_{t+1}=\arg\max_R P(R\mid Q,R_{t\to v},P_{t\to v}).
$$

这一步的思想是“用完整对象替代破碎标记”。如果 ICoT 的视觉思考是从注意力中拿出若干不连续碎片，PVTG 则希望给模型一个语义上更可解释的对象证据。

## 关键结果

### 主结果与强基线

![Table 1](Reasoning/TrainingFree/Lets%20Think%20with%20Images%20Efficiently%20An%20Interleaved-Modal%20Chain-of-Thought%20Reasoning%20Framework%20with%20Dynamic%20and%20Precise%20Visual%20Thoughts/images/page_004_fig_table_1.png)
*论文原图编号：Table 1。DaP-ICoT 在五个 MLLM、三个基准、零样本与单样本设置下与多种多模态 CoT 方法比较。*

表 1 的主要信号是：DaP-ICoT 在不同骨干上都比较稳定，不是只对单一模型有效。

| Model | Setting | M3CoT | ScienceQA | MME |
|---|---|---:|---:|---:|
| Chameleon-7B | 0-shot | 41.0 | 57.1 | 832.3 |
| Chameleon-7B | 1-shot | 41.9 | 62.9 | 1013.0 |
| Qwen2-VL-2B | 0-shot | 47.3 | 68.4 | 1378.9 |
| Qwen2-VL-2B | 1-shot | 51.0 | 73.6 | 1862.4 |
| Qwen2-VL-7B | 0-shot | 57.2 | 75.9 | 2012.2 |
| Qwen2-VL-7B | 1-shot | 58.7 | 78.5 | 2076.0 |

Chameleon-7B 上最直观的对比是 M3CoT 零样本：DaP-ICoT 为 `41.0`，SCAFFOLD 为 `31.0`，ICoT 为 `26.1`。这说明在较弱或早期统一建模骨干上，动态和精确视觉思考带来的收益很明显。

Qwen2-VL-7B 上，DaP-ICoT 也达到 M3CoT `57.2 / 58.7`、ScienceQA `75.9 / 78.5`、MME `2012.2 / 2076.0`。这支持作者的模型无关性主张，但仍要注意：表格展示的是同一套推理框架在多个模型上的结果，不等于证明阈值或分割质量完全不需要重新调。

### 消融到底说明了什么

![Figure 3](Reasoning/TrainingFree/Lets%20Think%20with%20Images%20Efficiently%20An%20Interleaved-Modal%20Chain-of-Thought%20Reasoning%20Framework%20with%20Dynamic%20and%20Precise%20Visual%20Thoughts/images/page_005_fig_figure_3.png)
*论文原图编号：Figure 3。Qwen2-VL-7B 上的消融实验：移除 PVTG 或 DVTI 都会显著降低 M3CoT 与 ScienceQA 表现。*

在 Qwen2-VL-7B 上：

| Method | M3CoT | ScienceQA |
|---|---:|---:|
| DaP-ICoT | 57.2 | 75.9 |
| w/o PVTG | 43.4 | 55.5 |
| w/o DVTI | 42.8 | 55.1 |

这个消融很重要。去掉 PVTG 以后，模型仍可动态决定是否插入视觉内容，但插入内容不再是精确对象，结果下降 `13.8` 和 `20.4`。去掉 DVTI 以后，模型仍可拿到对象级视觉内容，但调度又变得不够自适应，结果下降 `14.4` 和 `20.8`。

所以论文不是只证明“对象 crop 有用”，也不是只证明“少插图有用”。更准确的结论是：什么时候插图和插入什么图必须配合起来，才能同时保证性能和效率。

### 效率结果

![Figure 4](Reasoning/TrainingFree/Lets%20Think%20with%20Images%20Efficiently%20An%20Interleaved-Modal%20Chain-of-Thought%20Reasoning%20Framework%20with%20Dynamic%20and%20Precise%20Visual%20Thoughts/images/page_005_fig_figure_4.png)
*论文原图编号：Figure 4。在 Qwen2-VL-7B 的 M3CoT 上，DaP-ICoT 平均标记消耗为 314，比 ICoT 的 1,146 低 72.6%。*

效率数字是这篇论文最清楚的卖点。M3CoT + Qwen2-VL-7B 上：

| Method | Average token consumption |
|---|---:|
| DaP-ICoT | 314 |
| ICoT | 1,146 |
| CCoT | 1,294 |
| SCAFFOLD | 934 |
| DDCoT | 1,426 |
| MCoT | 1,080 |

DaP-ICoT 相比 ICoT 降低 `72.6%`。这个幅度足够大，说明 DVTI 不是轻微剪枝，而是明显改变了视觉输入进入推理序列的频率。

![Figure 5](images/page_006_fig_figure_5.png)
*论文原图编号：Figure 5。DaP-ICoT 与 ICoT 的图像插入频率和插入图像标记消耗对比。*

论文进一步报告，DaP-ICoT 平均每个样本只插入约 `1.2` 张图像，而 ICoT 约为 `2.6` 张。DaP-ICoT 平均插入图像标记约为 `26`。这组数字解释了为什么 Figure 4 的总标记消耗会大幅下降。

### 置信度分析与阈值

![Figure 6](images/page_006_fig_figure_6.png)
*论文原图编号：Figure 6。DaP-ICoT 插入视觉内容后更常提升置信度，且平均提升幅度更大。*

作者还检查了视觉插入后模型置信度是否真的提高。平均来看，DaP-ICoT 让 `80.7%` 的样本置信度提升，而 ICoT 只有 `46.4%`。在三个基准上，DaP-ICoT 的置信度提升幅度也更稳定。

Figure 7 的裁剪质量不适合直接放主图，但其中关键结论是：在 Qwen2-VL-7B + M3CoT 上，阈值 $\tau=0.2$ 时表现最好，零样本为 `57.2%`，单样本为 `58.7%`。当阈值过高时，模型会更频繁请求视觉输入，反而破坏视觉与文本推理的平衡。

### 定性案例

![Figure 8](Reasoning/TrainingFree/Lets%20Think%20with%20Images%20Efficiently%20An%20Interleaved-Modal%20Chain-of-Thought%20Reasoning%20Framework%20with%20Dynamic%20and%20Precise%20Visual%20Thoughts/images/page_007_fig_figure_8.png)
*论文原图编号：Figure 8。当前 ICoT 因插入破碎视觉内容而回答“等待某人”；DaP-ICoT 使用 SAM2 分割和低置信度触发，回答“卖伞”。*

案例的价值在于把两个模块串起来：DVTI 先发现当前文本推理置信度不足，PVTG 再选择完整且相关的对象图像。这样模型不是在每一步都插入近似区域，而是在必要时插入能修正判断的证据。

## 深度分析

### 真正贡献是什么

DaP-ICoT 的真正贡献是把 ICoT 从“视觉内容固定回注”改成“推理时视觉证据调度”。这比单纯提出一个新的提示模板更有意义，因为它抓住了多模态长推理中的两个成本源：视觉输入太多，以及视觉输入太碎。

如果把 ICoT 看作视觉语言推理里的第一版“边想边看”，DaP-ICoT 更像第二版“需要时再看，而且看完整对象”。这也是它适合放在 `TrainingFree` 的原因：它不训练模型，而是在测试时控制视觉证据的进入时机和形态。

### 为什么结果成立

结果成立有三个原因。

第一，logit 间隔虽然简单，但能作为一个低成本不确定性信号。模型在某一步文本理由上越犹豫，top-1 与 top-2 的差距通常越小。此时补充视觉证据更可能有用。

第二，SAM2 对象候选提供了比离散视觉标记更稳定的语义单位。对象图像保留轮廓、纹理和上下文局部关系，后续语言模型更容易把它和当前理由对齐。

第三，DaP-ICoT 把“少插图”与“插对图”绑定起来。如果只是少插图，可能损失信息；如果只是插完整对象，可能增加成本。两者结合才解释了消融和效率结果。

### 容易误读的地方

不要把 72.6% 标记降低理解成完整系统延迟同等降低。PVTG 需要 SAM2 分割和候选匹配，这些额外步骤也有运行成本。论文主要报告的是标记消耗和图像插入次数，不是端到端 wall-clock latency。

也不要把 DaP-ICoT 理解成模型内部已经学会主动视觉搜索。它仍是外部推理流程：置信度由解码 logit 计算，候选对象由 SAM2 产生，选择过程由相关性匹配完成。模型参数本身没有被训练成“会主动看回来”。

### 复现注意点

1. 需要能访问生成过程中的 top-1 与 top-2 logits，否则 DVTI 的置信度估计无法实现。
2. 需要 SAM2 或等价分割器生成对象候选；分割质量会直接影响 PVTG。
3. 阈值 $\tau$ 是在 M3CoT 验证集上搜索的，复现其他数据集时不能默认 `0.2` 永远最优。
4. 表 1 中所有方法只复现实验一次，若要做稳定比较，最好报告多随机种子或置信区间。
5. 如果实际部署关心成本，应同时记录标记消耗、分割耗时、候选数量和总推理延迟。

## 局限

1. 阈值依赖验证集搜索。论文展示了 $\tau=0.2$ 在 M3CoT 上最优，但没有充分说明跨基准、跨模型时的校准稳定性。
2. PVTG 依赖 SAM2。方法虽然不训练 MLLM，但需要外部对象分割工具；在小目标、遮挡或低质量图像中，候选质量可能成为瓶颈。
3. 效率评估偏向标记层。标记消耗降低很有价值，但还不能完全代表端到端延迟和显存占用。
4. 定性案例数量有限。Figure 8 说明方法可能修正破碎视觉表示，但还不足以系统刻画失败模式。
5. 论文没有深入分析不同类型问题何时更需要视觉思考，例如计数、文字识别、空间关系和常识题可能需要不同触发策略。

## 我的笔记

这篇可以看作 ICoT 的直接后续：ICoT 证明“把视觉局部插回推理”有用，DaP-ICoT 追问“每一步都插是否必要、插碎片是否合理”。这个问题在 3D agent 里也会出现：agent 不应该每一步都重新渲染所有视角，而应该在不确定时请求新的视图、局部 crop 或对象级证据。

和 DeepScan 相比，DaP-ICoT 的证据获取更轻：它不做分层扫描和再聚焦，而是在已有图像中通过分割候选选对象。和 REALM 相比，它没有 3DGS 或多视角场景建模，仍然是 2D 图像内的视觉证据插入。

我觉得最可复用的设计是 DVTI。很多 agent 流程都需要一个“何时调用工具”的门控信号。logit 间隔未必是最好信号，但它非常便宜，而且不需要额外监督。未来可以把这个思想迁移到：何时做局部裁剪、何时做文字识别、何时请求三维渲染、何时调用视觉专家。

PVTG 的启发则是证据粒度。对于多模态推理，证据单位最好是“完整语义对象”，而不是模型内部注意力随手抓出来的一组碎片。这一点和三维分割、视觉落地、对象中心记忆都有共通性。

## 引用

- 推荐引用键: `liu2026let`
- arXiv: http://arxiv.org/abs/2603.21754
- DOI: https://doi.org/10.48550/arXiv.2603.21754
- Code: https://github.com/67L1/DaP-ICoT
- Source PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/VZYTSXMW/Liu 等 - 2026 - Let's Think with Images Efficiently! An Interleaved-Modal Chain-of-Thought Reasoning Framework with.pdf`
