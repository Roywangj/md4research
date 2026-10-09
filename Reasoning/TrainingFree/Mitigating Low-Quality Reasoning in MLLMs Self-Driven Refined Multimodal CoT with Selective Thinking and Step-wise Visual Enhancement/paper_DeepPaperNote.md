---
tags:
  - papers/visually-grounded-reasoning
  - papers/multimodal-cot
  - papers/training-free
aliases:
  - "SDR-MCoT"
  - "Self-Driven Refined Multimodal CoT"
date: 2026
doi: 10.1609/aaai.v40i12.37919
---

# Mitigating Low-Quality Reasoning in MLLMs: Self-Driven Refined Multimodal CoT with Selective Thinking and Step-wise Visual Enhancement

## 核心信息

- 标题: Mitigating Low-Quality Reasoning in MLLMs: Self-Driven Refined Multimodal CoT with Selective Thinking and Step-wise Visual Enhancement
- 标题翻译: 缓解 MLLM 中的低质量推理：带选择性思考与逐步视觉增强的自驱精炼多模态思维链
- 作者: Chongjun Tu, Peng Ye, Dongzhan Zhou, Tao Chen, Wanli Ouyang
- 机构: Fudan University; Shanghai AI Laboratory; The Chinese University of Hong Kong; Shanghai Innovation Institute
- 发表时间: 2026
- 发表渠道: Proceedings of the AAAI Conference on Artificial Intelligence
- DOI: 10.1609/aaai.v40i12.37919
- 论文链接: https://doi.org/10.1609/aaai.v40i12.37919
- 代码 / 项目: 未公开
- 数据 / 资源: M3CoT；CoMT；ScienceQA；MMStar；A-OKVQA；V*；HallusionBench；MathVista；Qwen2-VL-7B；InternVL3-8B；LLaVA-1.5-7B/13B
- 论文类型: AI 方法；免训练多模态思维链；选择性思考；逐步视觉增强

## 原文摘要翻译

多模态大语言模型在视觉语言任务中越来越强，但现有多模态思维链方法仍常出现低质量推理。论文把问题拆成两类：第一，简单问题被迫进入长推理，导致冗余、噪声甚至错误；第二，困难问题虽然需要推理，却没有充分利用图像中的任务相关证据。

作者观察到，MLLM 本身已经有两个潜在能力：它能通过直接回答时的不确定性区分简单与困难样本，也能在注意力图中显露与任务相关的视觉区域。SDR-MCoT 的目标就是不训练模型，而是在推理时激活这两个能力。

方法包含两个模块。选择性思考用首标记熵判断是否需要逐步推理，低熵样本直接回答，高熵样本进入 CoT。逐步视觉增强则在每个推理步骤定位相关视觉 patch，并增强这些 patch 的注意力。实验显示，在八个基准上，SDR-MCoT 提升准确率，并显著减少生成标记消耗。

## 创新点

1. 论文把 MCoT 的失败定义得更细：不是“模型不会推理”，而是简单题过度推理、困难题视觉证据不足。
2. 选择性思考很轻量：只看直接回答首标记的概率熵，不需要额外 verifier 或训练数据。
3. 视觉增强不插入额外图像标记。它直接在注意力层增强相关视觉图块，因此比 ICoT 类插图方法更省上下文。
4. 相对注意力的设计处理了多选题的特殊噪声：带选项注意力容易被答案文本牵引，不带选项注意力又可能有边界偏置，二者结合后更接近题目需要看的区域。
5. 消融结果清楚地区分两个模块的角色：选择性思考节省标记，视觉增强提升准确率，组合后得到最好性价比。
6. 这篇是 `TrainingFree` 线里适合与 VisRef、PRCR 对照的一篇：VisRef 重注入视觉标记，PRCR 复用视觉缓存，SDR-MCoT 调整现有视觉注意力。

## 一句话总结

SDR-MCoT 的核心是：先用首标记熵判断“这题值不值得长思考”，再只对值得长思考的样本，在每一步推理中增强相关视觉 patch 的注意力。

## 研究问题

多模态 CoT 的常见假设是“复杂任务需要一步步想”。这对部分题成立，但论文指出，把所有题都强行放进 CoT 会带来两个问题。

第一是过度思考。简单题本来可以直接答，长 CoT 反而给模型制造了更多犯错机会。第二是视觉利用不足。困难题需要推理，但长文本轨迹会让模型越来越靠语言先验，视觉证据没有持续进入推理。

![Figure 1](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/images/page_001_fig_figure_1.png)
*论文原图编号：Figure 1。简单题直接答，困难题才进入带视觉增强的 CoT，是 SDR-MCoT 的基本路线。*

![Figure 2](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/images/page_002_fig_figure_2.png)
*论文原图编号：Figure 2。论文展示了低质量推理的两个面向：不必要的长 CoT，以及困难样本中视觉落地不足。*

这篇文章的真正问题不是“如何让 MLLM 多想几步”，而是“如何让 MLLM 自己决定该不该想，并且在需要想的时候真的看图”。这个问题意识和 3D agent 很接近：一个 agent 不应该每个任务都开全量规划，也不应该规划时丢掉当前场景证据。

## 数据与任务定义

任务输入是图像与文本问题，输出是最终答案。论文评测的不是单一数据集，而是八个视觉推理基准，覆盖科学问答、数学图表、视觉问答、幻觉识别和细粒度视觉推理。

| 类型 | 数据集 |
|---|---|
| 多模态推理 | M3CoT；CoMT |
| 科学与数学 | ScienceQA；MathVista |
| 综合视觉理解 | MMStar；A-OKVQA |
| 细粒度视觉 | V* |
| 幻觉与可靠性 | HallusionBench |

模型覆盖 Qwen2-VL-7B、InternVL3-8B 和 LLaVA 系列。

基线包括 No CoT、普通 CoT 和 DDCoT。

也包括 MMCoT、CCoT 和 ICoT。

评测时论文不仅看准确率，也看生成标记数。这个设计很重要，因为多模态 CoT 方法很容易通过极长输出隐藏推理成本。

## 方法主线

### 机制流程

![Figure 3](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/images/page_004_fig_figure_3.png)
*论文原图编号：Figure 3。SDR-MCoT 先做选择性思考，再在困难样本的每个推理步骤做视觉增强。*

SDR-MCoT 可以拆成四步。

1. 输入图像和问题后，先让模型生成一个词或短语形式的直接回答。
2. 从首个生成标记的概率分布中提取熵，得到样本级不确定性信号。
3. 若熵低于阈值，系统直接输出答案，并停止额外推理。
4. 若熵高于阈值，系统进入 CoT，逐步更新相关视觉图块的注意力并生成最终答案。

### 选择性思考

设首个生成标记的 logits 为 $z_i$，温度为 $T$，概率为：

$$
p_i=\frac{\exp(z_i/T)}{\sum_j \exp(z_j/T)}.
$$

首标记熵为：

$$
H=-\sum_i p_i\log p_i.
$$

若 $H<\theta$，样本走直接回答；若 $H\geq\theta$，样本走逐步推理。阈值 $\theta$ 由小样本平均熵自适应得到，而不是手写成一个固定常数。

这套设计的直觉是：如果模型首个回答标记的分布非常尖锐，它大概率已经知道答案；如果分布很平，说明答案空间不确定，继续推理更可能有价值。

> [!figure] Figure 4. Entropy correlation
> 建议位置：`方法主线 / 选择性思考`  
> 放置原因：图 4 是选择性思考的关键经验支撑，显示 M3CoT 上首标记熵越高，准确率整体越低。  
> 当前状态：抽图流程未得到干净完整图像；正文保留趋势。低熵组准确率约 `0.97`，高熵组降到约 `0.24-0.30`。

### 逐步视觉增强

视觉增强只在进入 CoT 的样本上使用。它不生成额外视觉标记，而是在当前解码的注意力分布上增强任务相关图块。

对多选题，论文先计算两种注意力：带选项的注意力和不带选项的注意力。带选项时，注意力容易被答案文本牵引；不带选项时，注意力能更接近问题本身，但可能有边界偏置。相对注意力试图从这两者中抽出真正和任务相关的区域。

![Figure 5](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/images/page_005_fig_figure_5.png)
*论文原图编号：Figure 5。相对注意力比单独的带选项或不带选项注意力更集中到相关区域。*

在推理步骤内，当前注意力 $A_{\mathrm{curr}}$ 与相对注意力 $A_{\mathrm{rel}}$ 做逐元素组合：

$$
A_{\mathrm{amp}}=A_{\mathrm{curr}}\odot A_{\mathrm{rel}}.
$$

然后使用形态学腐蚀去掉孤立注意力汇点，保留成片的高注意力区域。被选中的视觉 patch 会乘上增强因子，最后重新归一化 post-softmax 注意力，使总和仍为 1。

这一步的关键点是“增强已有视觉标记”，不是“插入新证据”。因此 SDR-MCoT 和 ICoT、DaP-ICoT 的差异很清楚：后者把图像区域显式放回上下文，前者在内部注意力上让模型多看相关图块。

## 关键结果

### 主结果

![Table 1](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/images/page_006_fig_table_1.png)
*论文原图编号：Table 1。SDR-MCoT 在多个 backbone 上提升平均准确率，并大幅降低 CoT 式方法的生成标记数。*

| Backbone | Method | Avg. accuracy | Avg. tokens |
|---|---|---:|---:|
| Qwen2-VL-7B | No CoT | 59.00 | 35.54 |
| Qwen2-VL-7B | CoT | 57.34 | 172.08 |
| Qwen2-VL-7B | MMCoT | 61.75 | 189.15 |
| Qwen2-VL-7B | SDR-MCoT | 63.69 | 67.94 |
| InternVL3-8B | No CoT | 70.28 | 45.68 |
| InternVL3-8B | CoT | 65.90 | 224.46 |
| InternVL3-8B | MMCoT | 70.89 | 232.88 |
| InternVL3-8B | SDR-MCoT | 72.87 | 100.33 |
| LLaVA-1.5-7B | No CoT | 43.54 | 25.93 |
| LLaVA-1.5-7B | SDR-MCoT | 45.81 | 59.40 |
| LLaVA-1.5-13B | No CoT | 46.40 | 28.23 |
| LLaVA-1.5-13B | SDR-MCoT | 48.57 | 63.76 |

这里最值得注意的不是单个基准的涨点，而是 CoT 本身经常低于直接回答。

例如在 Qwen2-VL-7B 上，CoT 平均 57.34，低于直接回答的 59.00。

InternVL3-8B 上，CoT 65.90，也低于直接回答的 70.28。这正好支持论文的基本判断：长推理不是免费午餐。

SDR-MCoT 在 Qwen2-VL-7B 上同时获得最高平均准确率和较低标记成本。它比 MMCoT 高 1.94 个点，但标记数从 189.15 降到 67.94。

### 消融实验

![Table 2](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/images/page_007_fig_table_2.png)
*论文原图编号：Table 2。选择性思考主要节省标记，视觉增强主要提升准确率，组合效果最好。*

| Selective Thinking | Visual Enhancement | Tokens | CoMT | MMStar | HallusionBench |
|---|---|---:|---:|---:|---:|
| no | no | 212.91 | 28.37 | 53.62 | 63.76 |
| yes | no | 74.07 | 29.25 | 54.47 | 67.39 |
| no | yes | 216.57 | 31.24 | 54.91 | 67.76 |
| yes | yes | 69.84 | 32.39 | 56.39 | 69.12 |

消融非常清楚。只加选择性思考，token 从 212.91 降到 74.07，但准确率涨幅有限。只加视觉增强，token 基本不降，但准确率明显上升。两个模块同时用，token 最少且三项准确率最高。

这说明 SDR-MCoT 不是一个单点技巧。它其实有一个预算控制器和一个视觉落地增强器：前者决定推理成本，后者决定推理质量。

## 深度分析

这篇论文的强处在于把“长推理是否有用”拆成了可操作的路由问题。很多多模态推理论文默认所有样本都要展开 CoT，但 SDR-MCoT 说明，推理长度应该是样本级决策，而不是方法级常量。

它的第二个价值是把视觉落地放在注意力层处理。这样做的代价是需要访问模型内部，但好处是不会把上下文长度继续拉长。对推理系统而言，这比反复插图或回放视觉标记更接近低成本控制器。

最需要谨慎的是首标记熵的适用范围。短答案和多选题很适合这种信号；开放式描述、长答案规划或多步工具调用任务里，首个生成标记未必能代表整体难度。因此它更适合做快速路由，而不是最终置信度估计。

## 局限

论文没有给出很长的限制讨论，但从方法本身可以看出几个边界。

第一，方法需要访问首标记 logits 和模型内部注意力。如果部署环境只暴露文本 API，SDR-MCoT 很难直接实现。

第二，熵阈值虽然是自适应估计，但仍然依赖采样子集。如果任务分布、提示格式或答案空间变化很大，阈值需要重新校准。

第三，视觉增强依赖注意力图能反映有效视觉证据。对某些架构、推理内核或强压缩视觉标记的模型，注意力图可能不稳定。

第四，方法主要评测闭集或短答案基准。对于开放式 agent 任务、长交互任务和 3D 场景推理，是否还能用首标记熵作为可靠难度信号，需要进一步验证。

## 我的笔记

### 和 3D 智能体方向的关系

这篇对 3D agent 很有启发。很多 3D agent pipeline 也有类似问题：有些任务一句话就能由单视角回答，却被强行送进多视角搜索和长规划；另一些任务真的需要空间证据，但规划链越长，越容易忘掉当前视角或几何证据。

SDR-MCoT 可以迁移成两个模块。

第一是 selective planning。先用便宜的不确定性信号判断是否需要多视角检索、局部渲染或工具调用。低不确定性任务直接答，高不确定性任务再打开重规划。

第二是 step-wise evidence enhancement。对于需要多步推理的任务，每一步都显式强化当前问题相关的视角、点云区域或 3DGS 局部 render，而不是让语言计划自己漂。

它和 3D 智能体文件夹里的整体脉络也能对齐：DeepScan 是先找证据，VisRef 是重注入视觉标记，PRCR 是让回看更省算力，SDR-MCoT 则回答一个更前置的问题：什么时候该启动这些昂贵的视觉推理过程。

### 个人判断

如果我要把这篇用于自己的系统，我不会直接照搬注意力增强，而会先照搬“低成本路由”这个思想。也就是说，在每次多视角检索、局部渲染或工具调用前，先问一个便宜的不确定性问题：这一步真的需要额外视觉计算吗？

## 术语表

| English | 中文 | 备注 |
|---|---|---|
| low-quality reasoning | 低质量推理 | 包含过度思考和视觉利用不足 |
| overthinking | 过度思考 | 简单题生成冗余 CoT |
| Selective Thinking | 选择性思考 | 由首标记熵控制路由 |
| Step-wise Visual Enhancement | 逐步视觉增强 | 每个推理步骤增强视觉注意力 |
| relative attention | 相对注意力 | 减少选项与边缘噪声 |
| attention sink | 注意力汇点 | 孤立但吸收注意力的无关点 |
| token consumption | 标记消耗 | 评估推理成本的重要指标 |

## 引用

- 论文: Chongjun Tu, Peng Ye, Dongzhan Zhou, Tao Chen, Wanli Ouyang. *Mitigating Low-Quality Reasoning in MLLMs: Self-Driven Refined Multimodal CoT with Selective Thinking and Step-wise Visual Enhancement*. Proceedings of the AAAI Conference on Artificial Intelligence, 2026. DOI: 10.1609/aaai.v40i12.37919.
- 全文对照翻译: [paper.md](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/paper.md)
- 来源映射: [source_map.json](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/source_map.json)
- 阅读计划: [paper_DeepPaperNote.plan.json](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/paper_DeepPaperNote.plan.json)
- 来源清单: [paper_DeepPaperNote.source_manifest.json](paper_DeepPaperNote.source_manifest.json)
- 证据包: [paper_DeepPaperNote.bundle.json](paper_DeepPaperNote.bundle.json)
- 图表决策: [paper_DeepPaperNote.figure_decisions.json](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/paper_DeepPaperNote.figure_decisions.json)
