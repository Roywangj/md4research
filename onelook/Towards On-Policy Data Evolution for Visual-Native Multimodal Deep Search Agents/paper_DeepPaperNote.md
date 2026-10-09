# Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents

## 核心信息

- **论文定位：** 多模态深度搜索 agent 的 workspace 与训练数据共同设计。
- **核心组件：** Visual-Native Agent Harness、Image Bank Reference Protocol、On-policy Data Evolution (ODE)。
- **结果：** 在统一 agent workflow 下，Qwen3-VL-8B 平均准确率由 24.9% 提升至 39.0%；30B 由 30.6% 提升至 41.5%。8B 超过 Gemini-2.5 Pro 的 37.9% 平均分。
- **源文件：** `detailed_paper.md`（全文双语读者，25 页 PDF）。

## 原文摘要翻译

多模态深度搜索要求 agent 在不断变化的文本和视觉上下文中串联搜索、工具使用与视觉推理，以解决开放世界问题。现有系统受两个瓶颈限制：工具返回的图像通常被视为临时输出，后续工具不能再次消费中间视觉证据；训练数据多按照固定配方构建，无法跟踪目标 agent 能力的演化。论文提出以 Image Bank Reference Protocol 为中心的视觉原生 agent 工具框架，将每个工具返回图像注册为可寻址引用，使中间视觉证据可被后续工具复用；并提出 ODE，让数据生成器根据正在训练的策略 rollout 在多轮闭环中自我改进。ODE 同时支持多样的 SFT 数据与面向策略的 RL 数据。在 8 个 benchmark 上，Qwen3-VL-8B 平均分由 24.9% 提升至 39.0%，30B 由 30.6% 提升至 41.5%。

## 创新点

1. **视觉状态持久化，而不是仅暴露视觉观测。** 初始图像和每次工具产生的图像都进入共享 Image Bank，并通过 `<image:N>` 句柄被后续 `zoom_in`、`visual_search` 等工具引用。
2. **把数据合成变成 on-policy 优化。** ODE 的每轮流程是 seed proposal → web exploration → graph organization → task curation → policy rollout → rubric trace analysis → configuration update。
3. **SFT 与 RL 使用不同的反馈目标。** SFT 优化 teacher trace 的视觉依赖、工具质量和策略多样性；RL 优化 capability requirement、difficulty match 与 learning utility。
4. **用消融解释机制。** Image Bank 复用收益与 secondary image-use rate 相关；演化数据产生更多视觉密集、多步、多工具轨迹，并构造更贴近当前策略学习前沿的 RL 任务。

## 一句话总结

ODE 的真正贡献不是“合成更多多模态数据”，而是让数据生成器观察目标策略的失败模式，并持续把视觉搜索数据推向该策略当前最需要学习的区域；Image Bank 则让这些数据真正包含可复用的中间视觉状态。

## 研究问题

1. 工具返回的图像能否成为后续搜索与变换的持久证据，而不是一次性 observation？
2. 固定数据合成配方是否会脱离目标 policy 的学习前沿？
3. rollout-level rubric feedback 能否分别改善 SFT teacher traces 与 RL task quality？

## 数据与任务定义

任务写作 $T=(q,I,a)$：$q$ 是需要跨模态收集证据的开放世界查询，$I$ 是放入 image bank 的初始视觉上下文，$a$ 是用于验证的参考答案。ODE 覆盖 11 个主题域、4 种能力组合（perception-only、perception+search、perception+reasoning、perception+search+reasoning）和 easy/medium/hard/expert 四种难度。

实验 benchmark：MM-BrowseComp (MMBC)、HLE-VL、BC-VL、VDR、MMSearch、MMSearch+、SimpleVQA (SVQA)、FVQA。训练 backbone 为 Qwen3-VL-8B-Instruct 与 Qwen3-VL-30B-A3B-Instruct。

## 方法主线

### 机制流程

1. **Forward curation：** seed proposer 选择带有可读标签、数字、日期或图例的实体-图像 seed；explorer 用九个工具构建文本、视觉、数值事实节点；graph organizer 将节点组织为多模态证据图 $G$，并增加 reasoning/perception derived nodes；curator 从连通证据簇合成不泄漏工具策略的可验证问题。
2. **Backward optimization：** rollout model 执行候选任务，LLM judge 判断最终答案，analyzer 对轨迹评分并把失败归因到四个 forward stage，optimizer 修改下一轮 $C_{t+1}$。
3. **模式差异：** SFT 选择“可教”的 teacher trajectory；RL 选择位于当前 policy learning frontier 附近、既可验证又有明确纠错信号的任务。

### Visual-Native Agent Harness

九个工具为 web search、image search、scholar search、visit/browsing、visual search（Google Lens）、zoom-in、rotation、flip、Python execution。关键协议把图像登记为 `<image:N>`，例如先对 `<image:0>` `zoom_in` 得到 `<image:1>`，再对 `<image:1>` 做 `visual_search`，把返回图像作为 `<image:3>`，随后用 web search 验证候选实体并继续 zoom-in。

### ODE 的 rubric

共享维度：Information Complexity、Visual Dependency、Shortcut Leakage、Verifiability。SFT 特有：Step Appropriateness、Tool Usage Quality、Tool Pattern Diversity。RL 特有：Capability Requirement、Difficulty Match、Learning Utility。每维为 −5 到 +5 的序数分，并返回 stage attribution。RL 的 difficulty 标签包括 `[too_easy]`、`[good_match]`、`[too_hard]`、`[fake_hard]`、`[infra_failure]`。

## 关键结果

### 主结果与强基线

| Setting / Model | Base Avg | +ODE-SFT | +ODE-RL | 最终提升 |
|---|---:|---:|---:|---:|
| 8B visual-native harness | 24.9 | 36.1 | **39.0** | +14.1 |
| 30B visual-native harness | 30.6 | 39.5 | **41.5** | +10.9 |
| Gemini-2.5 Pro agent workflow | 37.9 | — | — | — |

8B 的单 benchmark 增益在 VDR、MMSearch、MMSearch+、FVQA 等需要多步证据聚合的任务上最明显；ODE-8B-RL 在 MMSearch 达到 66.0，FVQA 达到 64.7。

### 消融到底说明了什么

去掉 tool-image reuse、但仍把工具返回图像显示给模型，会使 MMBC、HLE-VL、MMSearch+ 分别损失约 4.9、2.9、3.2 个百分点。性能收益与 secondary image reuse rate 同向，说明增益来自“图像可作为后续工具输入”，而不是简单增加视觉可见性。

### Static synthesis 对比

在相同数据规模下，evolved SFT traces 包含更多 intermediate tool-produced images、4+ tool images、2+ tool calls、visual+search 混合策略，以及更高的 tool-chain/strategy diversity。RL 对比也显示 evolved tasks 比固定初始配置有效，说明 policy-facing data 对难度校准特别敏感。

### 机制分析

SFT 演化后总体 tool calls 反而下降，但 dynamic images 与 image-input calls 增加：teacher trace 不是越长越好，而是让更多监督由中间视觉证据承担。RL 演化后 tool calls、dynamic images、image-input calls 都显著增加，任务更要求主动搜索而非从初始图像或一次检索直接作答。

## 深度分析

### 真正贡献是什么

真正贡献是一个可操作的闭环接口：图像句柄使“视觉证据的再消费”成为工具层原语；ODE 则把“模型失败”转成 generator configuration 的局部更新。两部分是耦合的：没有 image bank，rollout feedback 很难评价视觉证据是否被正确发现、裁剪和再检索；没有 ODE，持久视觉状态可能只提升 inference-time affordance，而不一定形成可学习的数据分布。

### 为什么结果成立

- **workspace 因素：** 中间图像会在轨迹中持续存在，支持 crop → visual search → web verification → further crop 的链式工作流。
- **数据因素：** ODE 把失败归因到 seed、exploration、graph 或 curation，而不是只筛选最终 reward；配置更新因此针对视觉证据质量、节点深度、推理/感知增强和难度。
- **训练因素：** SFT 传递完整 teacher trajectory；GRPO RL 在统一 harness 中使用策略面对的、可验证的任务。

### 容易误读的地方

1. 39.0% 不是单独由 ODE 产生：visual-native harness、ODE-SFT、ODE-RL 是累加组件。
2. “on-policy”主要发生在数据生成/任务校准层，不等于整个训练过程严格在线采样。
3. 所有模型由同一 LLM-as-judge 评估，judge bias 和 prompt sensitivity 仍可能影响绝对分数。
4. 论文强调超过 Gemini-2.5 Pro，但比较依赖统一 agent workflow 与调用预算；闭源模型的工具配置并非完全同构。

### 复现注意点

- 数据构建使用 GPT-5.2 进行大部分生成、分析和优化；SFT rollout 也使用 GPT-5.2。
- 演化最多 5 步，每步 32 个 curated tasks/traces；最终得到 8,855 个过滤后的 SFT examples，以及每个模型规模 4,000 个 RL examples。
- SFT：64k max sequence length、global batch 64、learning rate $2\times10^{-5}$、2 epochs。
- RL：GRPO + leave-one-out，异步 SGLang rollout，每 prompt 6 responses，batch 96，actor lr $2\times10^{-6}$，clip ratio 0.28，无 KL regularization；NVIDIA H20。
- 评估预算：temperature 0.6、top-p 0.95，最多 50 LLM calls、每 turn 8,192 tokens、总计 16,000 tokens。

## 局限

- 图像、网页和工具环境的时效性会影响可重复性；论文没有给出完整开放网络快照。
- 关键生成与 judge/analyzer 依赖闭源 GPT-5.2/LLM judge，复现需要替代模型或 API。
- 评价使用同一个 LLM-as-judge；虽然接受语义等价，但可能与人工评价存在系统差异。
- 25 页论文给出丰富工作例，但大规模数据过滤、工具失败率、成本和 wall-clock 细节仍不充分。
- 8 个 benchmark 的提升说明多模态搜索能力增强，但不等价于现实世界事实可靠性、长期自主性或物理 embodied 能力。

## 我的笔记

这篇工作应放在“多模态搜索 agent / agentic data synthesis / thinking with images”的交叉位置，而不是普通 vision-language model scaling。它最值得迁移到其他研究的抽象是：把中间状态显式命名、持久化，并让数据生成器对目标策略的失败进行结构化归因。后续若做 3D/embodied world model，可把 `<image:N>` 推广为带时间、相机、坐标系与来源的 observation handle，再让 ODE 的 rubric 评价几何一致性、可执行性和状态复用率。

## 引用

Huang, S. et al. “Towards On-Policy Data Evolution for Visual-Native Multimodal Deep Search Agents.” arXiv:2605.10832v2, 2026.
