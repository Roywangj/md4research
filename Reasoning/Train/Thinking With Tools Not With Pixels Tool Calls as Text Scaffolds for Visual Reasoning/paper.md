---
tags:
  - papers/reasoning
  - papers/multimodal
  - papers/train
aliases:
  - TextCall
  - Thinking With Tools Not With Pixels
arxiv_id: 2608.09682
---
# Thinking With Tools, Not With Pixels: Tool Calls as Text Scaffolds for Visual Reasoning

## 论文信息
- 作者：Jiahao Shao, Yuanbo Yang, Yiyi Liao, Yujun Shen, Ceyuan Yang, Yinghao Xu
- arXiv：2608.09682v1（2026-08-10）
- 项目页：https://textcall.github.io/
- 分类：Train

## 摘要 / Abstract
> Tool-augmented vision-language models increasingly “think with images” by calling crop, zoom, or code tools and reasoning over returned pixels. This paper asks whether those pixels are necessary. TextCall preserves the tool-call scaffold but replaces every returned image with the fixed text sentinel `[Image output skipped]`, during both training and inference. Across LoRA, full fine-tuning, and reinforcement learning, TextCall matches or exceeds thinking-with-images on the evaluated suite; a matched scaffold-only audit also recovers image-level accuracy. Decompositions show that reasoning text and spatial code both contribute. TextCall reduces latency by 29–46% and removes image-return execution overhead, but the claim is limited to the tested model, corpus, and perception-heavy benchmarks.
>
> 工具增强的视觉语言模型越来越多地通过调用裁剪、缩放或代码工具来“用图像思考”，并在后续推理中读取返回的像素。本文研究这些像素是否真的必要。TextCall 在训练和推理阶段都保留工具调用脚手架，只把每次返回图像替换为固定文本标记 `[Image output skipped]`。在 LoRA、全量微调和强化学习设置下，TextCall 在所评测基准上达到或超过图像返回方案；匹配的“仅脚手架”审计也恢复了与图像相当的准确率。分解实验显示，推理文本与空间代码均有贡献。TextCall 将延迟降低 29–46%，并消除图像返回的执行开销；但结论只适用于本文测试的模型、数据和偏感知任务基准。

## 核心方法
### 1. 问题与假设
> The paper separates two coupled channels in thinking-with-images: the text emitted before a tool return and the returned image after execution. It hypothesizes that tool name, target description, intent, and coordinates already tell the model where to look and what to find.
>
> 论文把“用图像思考”拆成两个耦合通道：工具执行前生成的文本，以及执行后返回的图像。作者假设，工具名称、目标描述、调用意图和坐标已经向模型说明了应该看哪里、寻找什么，因此返回像素可能只是承载这些结构化信息的冗余载体。

### 2. TextCall：训练对齐的载体替换
> Standard training returns a crop or edited image after the code block. TextCall keeps the same tool call and execution confirmation, but returns `[Image output skipped]`. The replacement is made during both SFT/RL training and evaluation, avoiding the train–test mismatch of an inference-only ablation.
>
> 标准训练在代码块之后返回裁剪图或编辑图。TextCall 保留完全相同的工具调用和执行确认，但返回 `[Image output skipped]`。替换同时发生在 SFT/RL 训练与评测中，从而避免只在推理时移除图像造成的训练—测试分布偏移。

### 3. 机制流程
1. 输入问题和原图，模型生成 `<think>` 推理与工具调用；
2. 工具调用包含工具名、目标描述、空间坐标和操作意图；
3. 传统方案返回像素，TextCall 返回固定文本占位符；
4. 模型继续生成并输出答案，训练协议与测试协议保持一致。

## 实验设置
> The backbone is Qwen2.5-VL-7B-Instruct. The SFT data are DeepEyesV2 multi-turn tool trajectories: 9.5K for LoRA ablations and 65K for full fine-tuning. The core suite contains V*Bench, HR-Bench-4K, HR-Bench-8K, MMStar, CV-Bench-2D, and CV-Bench-3D; BLINK, ChartQA, CharXiv, PixmoCount, and MME-RealWorld form an extended suite.
>
> 主干模型为 Qwen2.5-VL-7B-Instruct。SFT 数据来自 DeepEyesV2 多轮工具轨迹：LoRA 消融使用 9.5K，完整微调使用 65K。核心套件包括 V*Bench、HR-Bench-4K、HR-Bench-8K、MMStar、CV-Bench-2D 和 CV-Bench-3D；BLINK、ChartQA、CharXiv、PixmoCount 和 MME-RealWorld 构成扩展套件。

## 主要结果
| 设置 | V* | HR-4K | HR-8K | MME-RW | CV-2D | CV-3D | MMStar | BLINK | ChartQA | CharXiv |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 9.5K 图像返回 SFT（LoRA）|71.73|63.00|54.00|57.73|74.48|66.92|53.53|56.20|49.50|48.36|
| 9.5K TextCall SFT（LoRA）|76.96|71.50|67.00|61.02|70.93|68.42|50.05|56.93|51.29|53.84|
| 65K 图像返回 SFT|78.53|69.25|64.38|61.01|73.37|72.17|56.93|61.33|53.13|64.48|
| 65K TextCall SFT|78.01|73.12|67.50|62.05|72.32|73.67|55.04|62.73|54.29|66.24|
| 65K TextCall SFT+GRPO|81.68|73.88|70.62|64.51|67.32|56.83|57.12|65.53|45.98|85.20|

> At 9.5K LoRA, TextCall gains 5.23 points on V*Bench. At 65K full fine-tuning, the six-benchmark mean is 1.39 points higher for TextCall, with four gains and two small reversals. The paper does not claim that RL is necessary for the carrier-swap result; SFT already establishes parity.
>
> 在 9.5K LoRA 设置下，TextCall 在 V*Bench 上高出 5.23 个百分点。65K 全量微调时，TextCall 的六基准平均分高 1.39 个百分点，四项提升、两项小幅回落。论文没有声称强化学习是载体替换成立的必要条件；SFT 已足以建立两者的性能相当。

## 为什么有效：脚手架审计
> On 1,000 paired trajectories, a Gemini-3-Flash judge obtains 51.20% from the question alone, 73.50% from image plus question, 73.10% from scaffold plus question, and 79.40% from image plus scaffold. Scaffold-only minus image-only is −0.40 points with 95% CI [−3.20,+2.40], passing a 5-point non-inferiority margin.
>
> 在 1,000 条配对轨迹上，Gemini-3-Flash 评审器仅看问题得到 51.20%，看问题和图像得到 73.50%，看问题和脚手架得到 73.10%，同时看图像和脚手架得到 79.40%。仅脚手架相对仅图像差 −0.40 个百分点，95% 置信区间为 [−3.20,+2.40]，通过 5 个百分点的非劣性界限。

脚手架的增益分解为：57% 是图像和脚手架都能恢复的冗余增益，22% 是图像独有，21% 是脚手架独有；两者同时正确占 62.8%，仅图像正确 10.7%，仅脚手架正确 10.3%，两者都错 16.2%。作者明确指出，这部分是机制解释而非独立因果证明。

## 组件分解
| 变体 | V* | HR-4K | CV-2D | 平均 |
|---|---:|---:|---:|---:|
| 完整脚手架（推理+代码）|76.96|71.50|70.93|73.13|
| 仅推理（代码替换为 pass）|67.02|72.12|59.81|66.32|
| 仅代码（清空推理）|64.92|65.50|55.08|61.83|
| 仅骨架（推理和代码都空）|79.06|72.62|63.21|71.63|

> Reasoning text supplies the “why”; code supplies the “where”. Removing reasoning causes the largest drop, while removing code particularly hurts V*Bench and CV-2D. A later coordinate-precision ablation finds that shuffled numeric coordinates are statistically equivalent to correct coordinates, suggesting that code format and procedural commitment matter more than coordinate accuracy at post-training time.
>
> 推理文本提供“为什么看”，代码提供“看哪里”。删除推理文本造成最大下降，删除代码尤其伤害 V*Bench 和 CV-2D。后续坐标精度实验发现，随机打乱的数值坐标与正确坐标统计等价，说明在后训练阶段，代码格式和“先指定区域再继续推理”的程序性约束可能比坐标数值本身更重要。

## RL 动态与成本
> With matched GRPO (batch 128, learning rate 1×10⁻⁶, 64 GPUs, about one epoch), the image-return model reaches 0% tool-call rate at step 800, while TextCall recovers from a transient collapse at step 200 and reaches 75.2% mean tool-call rate at step 800. The authors caution that this is an internally matched 65K/no-Long-CoT contrast, not a contradiction of DeepEyesV2’s stable RL result using a larger corpus and different recipe.
>
> 在匹配的 GRPO 设置下（batch 128、学习率 1×10⁻⁶、64 张 GPU、约一个 epoch），图像返回模型在 step 800 的工具调用率为 0%；TextCall 在 step 200 短暂崩溃后恢复，step 800 的平均工具调用率为 75.2%。作者强调，这只是 65K、无 Long-CoT 条件下的内部匹配对比，并不否定 DeepEyesV2 在更大语料和不同训练配方下获得稳定 RL 的结果。

| 方法 | V*Bench | 六基准均值 | 工具调用 | 平均延迟 | P50 |
|---|---:|---:|---:|---:|---:|
| TextCall（sandbox）|78.01|71.23|0|2.91 s|2.49 s|
| 图像返回|78.53|69.84|1.8|4.12 s|3.10 s|
| TextCall（不执行，仅延迟）|—|—|0|2.22 s|1.73 s|

图像返回每轮约增加 498 ms 的视觉 token 预填充；TextCall 在测量锚点上降低 29%，在不执行工具的延迟下界上降低 46%。训练资源包括 9.5K LoRA（8×H20 约 1 小时）、65K 全量 SFT（64×H20 约 13 小时）、GRPO（64×H20 约 25–30 小时）。

## 边界、局限与过度主张风险
1. 证据只覆盖一个 7B 主干、一个 DeepEyesV2 轨迹语料、一个随机种子和偏感知基准，不能推出所有视觉推理任务都不需要像素。
2. 图像独有增益仍占 22%，且细粒度视觉差异、视觉模拟、陌生对象和视觉先验缺口可能让返回像素重新成为负载信号。
3. RL 中图像返回崩溃可能与奖励函数（0.8 准确率 + 0.2 格式）和数据规模有关；不能直接解释为像素本身必然有害。
4. Visual Jigsaw 只有 50 个样本，置信区间很宽，只能作为跨工具族一致性检查。
5. 坐标精度结论特指后训练阶段；不能否定视觉预训练中准确空间标注的作用。
6. TextCall 保留了原图编码和模型的视觉先验；它不是无视觉模型，也不能证明模型真正“看到了”每个目标。

## 复现清单
- 使用 Qwen2.5-VL-7B-Instruct，严格区分 9.5K LoRA 与 65K 全量微调。
- 训练和推理均把返回图像替换为精确字符串 `[Image output skipped]`，不提供 caption 或 oracle。
- 保持工具调用、执行确认、runner、judge、Agent Mode 设置一致。
- 复现 1,000 样本四条件审计、脚手架组件分解、坐标打乱、GRPO 工具调用率曲线和延迟测量。
- 报告完整六基准均值、扩展五基准结果、训练步数、工具调用率和硬件，而非只报告最好分数。

## 结论
> The paper’s strongest result is not “pixels never matter”, but that a training-aligned carrier swap exposes a cheaper sufficient signal in the evaluated distribution: structured pre-return text. TextCall should therefore be read as a causal audit and deployment option, not as a universal replacement for visual feedback.
>
> 论文最强的结论不是“像素永远不重要”，而是：在所评测的数据分布中，训练对齐的载体替换揭示了一个更便宜且足够的信号——返回前生成的结构化文本。因此，TextCall 应被理解为一种因果审计方法和部署选项，而不是视觉反馈的普适替代品。

## 附录覆盖说明
本文正文与附录 A–J 的方法、表格、图注和边界结论均已在本读本中按主题重排并保留关键数字：A 为硬件与计算，B 为 1,000 条轨迹审计，C 为脚手架分解，D 为固定占位符设计，E 为 V* 定性案例，F 为 Visual Jigsaw，G 为像素可能重新成为负载信号的任务，H 为既有诊断证据，I 为 RL 动态，J 为坐标精度。参考文献沿用原文编号，可由原 PDF 逐条核对。
