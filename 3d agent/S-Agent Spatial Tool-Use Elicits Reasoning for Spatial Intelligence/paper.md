# S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence

> 阅读说明：英文 `Para.` 段落是基于论文原文的忠实清理与转述，不是逐字全文复制；中文 `Para.[CN]` 是对应翻译与解读。这样保留段落级对齐、图表位置和可追溯性，同时避免把整篇论文原样搬运到笔记中。

## Metadata

| Item | Value |
|---|---|
| Title | S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence |
| Authors | Yalun Dai, Hao Li, Shulin Tian, Runmao Yao, Yuhao Dong, Fangzhou Hong, Zhaoxi Chen, Fangfu Liu, Baoliang Tian, Dingwen Zhang, Tao Wang, Kim-Hui Yap, Ziwei Liu |
| Source | Local PDF |
| arXiv metadata in PDF | arXiv:2606.20515v1 [cs.CV], 18 Jun 2026 |
| PDF pages | 22 |
| Main topic | Agentic spatial reasoning for multi-view image/video VLMs |
| Output folder | `/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence` |

## Page index

| Pages | Content |
|---|---|
| 1 | Title, author list, abstract opening, Fig. 1 overview |
| 2–3 | Abstract continuation and Introduction |
| 3–4 | Method overview and S-Agent framework |
| 4 | Fig. 2 pipeline |
| 5–6 | Hierarchical spatial evidence and temporal memory |
| 6–7 | Training-time distillation, S-300K motivation |
| 7 | Fig. 3 dataset/tool statistics |
| 7–12 | Experiments, benchmarks, results, ablations, qualitative examples |
| 13 | Conclusion |
| 14–15 | References |
| 16–18 | Appendix A/B: related work and tool/expert details |
| 19 | Appendix C: S-300K construction and Table 6 |
| 20 | Appendix D: VSI-SUPER long-video experiment and Table 7 |
| 21–22 | Appendix E: additional qualitative visualizations |

## Terminology ledger

| Term                                  | 中文建议            | Note                           |
| ------------------------------------- | --------------- | ------------------------------ |
| spatial intelligence                  | 空间智能            | 理解对象、观察者、视角和三维环境关系的能力          |
| spatial tool-use                      | 空间工具调用 / 空间工具使用 | 让 VLM 主动调用检测、深度、3D、专家模块来补足几何证据 |
| semantic planner                      | 语义规划器           | 由 VLM 承担，决定下一步该看什么、算什么、问哪个工具   |
| spatio-temporal evidence accumulation | 时空证据累积          | 本文核心：跨空间层级、跨时间帧/视角逐步聚合证据       |
| hierarchical spatial evidence         | 层级化空间证据         | L1 二维感知、L2 三维提升、L3 空间专家        |
| Scene Memory                          | 场景记忆            | 保存实体、位置、关系等持续性场景状态             |
| Agent Memory                          | 智能体记忆           | 保存规划、工具调用、观察、失败和中间推理轨迹         |
| trajectory distillation               | 轨迹蒸馏            | 用强教师智能体产生工具调用轨迹，训练小模型模仿完整过程    |
| S-300K                                | S-300K 监督数据     | 由过滤后的完整轨迹、回合级轨迹和工具/专家轨迹组成      |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper argues that spatial reasoning in large vision-language models should not be treated as a single-shot recognition problem. S-Agent instead casts it as an active process in which a model gathers spatial evidence over both space and time, especially for continuous multi-view images and videos.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文认为，大视觉语言模型中的空间推理不应该被当成一次性的识别题。S-Agent 将其改写为一个主动收集证据的过程：模型需要在空间维度和时间维度上逐步积累证据，尤其面向连续多视角图像和视频场景。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The framework uses a VLM as a semantic planner, a hierarchy of spatial tools to ground objects and lift evidence into 3D, and a dual-memory mechanism to maintain evolving scene knowledge and reasoning history. It improves zero-shot VLM performance and can be distilled into an 8B model trained on S-300K trajectories.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 该框架让 VLM 充当语义规划器，用分层空间工具完成目标定位、三维证据提升和空间知识聚合，再用双记忆机制保存不断变化的场景知识与推理历史。它既能提升零样本 VLM，也能通过 S-300K 轨迹蒸馏成一个 8B 规模模型。

### Fig. 1. S-Agent 总览

![Fig. 1](3d%20agent/S-Agent%20Spatial%20Tool-Use%20Elicits%20Reasoning%20for%20Spatial%20Intelligence/assets/fig1_overview.png)

**Caption:** Paraphrased from the paper: S-Agent combines a VLM planner, hierarchical spatial tools, scene/agent memory, and trajectory distillation to support multi-view spatial reasoning.

**Caption[CN]:** 图 1 展示 S-Agent 的整体范式：VLM 规划器、层级空间工具、场景/智能体记忆，以及通过工具调用轨迹蒸馏出小模型。

**Reading note:** 这张图是全文论证地图：左侧指出当前空间 VLM 的训练范式问题，中间给出 S-Agent 的主动工具调用框架，右侧给出零样本和蒸馏后的性能收益。

## 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Spatial intelligence is framed as the ability to reason about geometric relations among objects, observers, and 3D environments. The authors connect this capability to robotics, embodied AI, augmented reality, autonomous driving, and other settings where agents must act in physical space.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文把空间智能定义为理解对象、观察者和三维环境之间几何关系的能力。作者强调，这种能力直接关系到机器人、具身智能、增强现实、自动驾驶等需要在物理空间中行动的应用。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Current VLMs have gained impressive semantic recognition ability from large-scale image-text training, but they still struggle with geometry-heavy tasks such as relative direction, object orientation, metric distance, size, and route planning across views.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 现有 VLM 通过大规模图文训练获得了很强的语义识别能力，但在几何推理任务上仍然薄弱，例如相对方向、物体朝向、度量距离、尺寸关系，以及跨视角路线规划。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The key diagnosis is a semantic-to-geometric gap. Models trained mostly on passive 2D observations can describe what appears in an image, yet they do not automatically build persistent 3D evidence about the scene behind the image stream.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 作者的核心诊断是“语义到几何”的断裂。依赖被动二维图像训练的模型可以描述图像里有什么，但不会自然形成关于图像流背后三维场景的持续性证据。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Prior agentic VLM work has shown that external tools, programs, and geometric modules can help visual reasoning. However, many existing approaches focus on isolated images or static observations, while real-world spatial reasoning often depends on hidden, changing, multi-view evidence.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 过去的 agentic VLM 研究已经证明，外部工具、程序和几何模块可以增强视觉推理。但很多方法仍聚焦于单张图像或静态观测，而真实世界的空间推理往往依赖隐藏、变化、跨视角的证据。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> S-Agent is proposed as an evidence-accumulation paradigm. A VLM planner decomposes the question, selects spatial tools, observes their outputs, and updates memory so that later steps can reason from an enriched scene state rather than from the raw frames alone.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> S-Agent 被提出为一种“证据累积”范式。VLM 规划器会分解问题、选择空间工具、读取工具输出，并更新记忆，使后续推理不再只依赖原始帧，而是依赖不断增强的场景状态。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The paper’s empirical claim has two layers: the training-free S-Agent procedure improves strong closed and open VLMs on spatial benchmarks, and the generated trajectories can train S-Agent-8B, a smaller model that learns to imitate evidence-seeking spatial reasoning.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 论文的实验主张有两层：一是无需训练的 S-Agent 流程能提升强闭源和开源 VLM 在空间 benchmark 上的表现；二是由此生成的轨迹能训练 S-Agent-8B，让小模型学会模仿这种寻找证据的空间推理方式。

## 2. Method

### 2.1 S-Agent framework

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The method models a spatial reasoning problem as a question $q$ paired with visual observations $F$. Instead of requiring the VLM to answer immediately, S-Agent maintains a scene memory $S_t$ and an agent memory $H_t$ across iterative reasoning steps.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 方法把空间推理问题表示为问题 $q$ 与视觉观测 $F$ 的组合。S-Agent 不要求 VLM 立刻回答，而是在迭代推理过程中维护场景记忆 $S_t$ 和智能体记忆 $H_t$。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> At step $t$, the VLM planner reads the question, frames, scene memory, and agent history, then decides the next request $r_t$: which object to ground, which relation to verify, which 3D signal to compute, or whether enough evidence has been collected.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在第 $t$ 步，VLM 规划器读取问题、帧序列、场景记忆和智能体历史，然后决定下一条请求 $r_t$：要定位哪个对象、验证哪种关系、计算哪类三维信号，或者是否已经有足够证据作答。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The planner can be abstracted as:

$$
r_t = \pi_\theta(q, F, S_t, H_t)
$$

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 规划器可以抽象为上式：它不是直接输出最终答案，而是基于问题、视觉输入与两类记忆，产生下一步动作或工具调用请求。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Once a tool or expert returns an observation $o_t$, S-Agent updates both memories:

$$
(S_{t+1}, H_{t+1}) = \operatorname{Update}(S_t, H_t, r_t, o_t)
$$

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 工具或专家返回观测 $o_t$ 后，S-Agent 同时更新场景记忆和智能体记忆。这个循环让推理过程逐步“带着证据前进”，而不是每一步重新看一遍原始输入。

### Fig. 2. S-Agent 推理管线

![Fig. 2](fig2_pipeline.png)

**Caption:** Paraphrased from the paper: S-Agent uses the VLM as an agentic planner, queries tools and experts for scene-specific spatial evidence, and stores evolving 3D state in memory.

**Caption[CN]:** 图 2 说明完整流程：VLM 不再只看图回答，而是作为规划器调用空间工具、专家和记忆模块，逐步形成可用于回答问题的三维场景状态。

**Reading note:** 这张图的关键不是“工具很多”，而是工具、记忆、规划器之间形成闭环；如果只把工具输出一次性塞给模型，就没有本文所强调的时空证据累积。

### 2.1.1 Hierarchical spatial evidence

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper organizes spatial evidence into three levels. Level 1 handles 2D perception, Level 2 lifts or aligns observations into 3D, and Level 3 aggregates high-level spatial knowledge through specialized experts.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文把空间证据组织成三个层级：L1 处理二维感知，L2 将观测提升或对齐到三维空间，L3 通过专门专家聚合更高层空间知识。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> A tool observation can be written as:

$$
o_t = T^{(k)}(r_t, F, S_t), \quad k \in \{1,2,3\}
$$

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 这表示第 $t$ 步的观测由第 $k$ 层工具产生，工具输入包括规划器请求、视觉帧以及已有场景记忆。工具并不是固定流水线，而是被问题条件化地调用。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Level 1 tools include keyframe search, visual grounding, open-vocabulary detection, verification, and lightweight depth cues. Their job is to turn ambiguous visual references into concrete image-level evidence such as boxes, labels, visibility, and approximate positions.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> L1 工具包括关键帧搜索、视觉定位、开放词表检测、验证和轻量深度线索。它们的作用是把模糊的视觉指称转成具体的图像级证据，例如框、标签、可见性和粗略位置。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Level 2 tools lift 2D evidence into multi-view or metric 3D context. The framework uses depth, 3D coordinates, camera poses, bird’s-eye or novel-view evidence so that objects can be compared in a shared spatial frame.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> L2 工具把二维证据提升到多视角或度量三维上下文中。框架利用深度、三维坐标、相机位姿、鸟瞰或新视角证据，使不同对象能够在共享空间坐标中比较。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Level 3 experts answer structured spatial subproblems, such as counting, relative direction, orientation, metric measurement, and object-centric view reasoning. Their outputs are meant to be readable evidence for the planner rather than hidden latent features.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> L3 专家负责结构化空间子问题，例如计数、相对方向、朝向、度量测量和以物体为中心的视角推理。它们输出的是规划器可读的显式证据，而不是不可解释的隐向量。

### 2.1.2 Temporal memory

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The memory design separates persistent scene facts from procedural reasoning history. This separation lets S-Agent remember what has been established about the scene while also tracking how that evidence was obtained.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 记忆设计把持续性场景事实与过程性推理历史分开。这样 S-Agent 既能记住已经确认的场景信息，也能追踪这些证据是如何获得的。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Scene Memory stores question-relevant entities, attributes, positions, relations, and multi-view observations. It is not a full dense reconstruction; it is a compact, evolving representation of the spatial state needed for the task.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 场景记忆保存与问题相关的实体、属性、位置、关系和多视角观测。它不是完整稠密重建，而是为当前任务服务的紧凑、动态空间状态表示。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Agent Memory records planner thoughts, tool calls, observations, failures, and intermediate conclusions. This history helps avoid repeated tool calls, supports error recovery, and gives the final answer a chain of evidence.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 智能体记忆记录规划器思路、工具调用、观测结果、失败情况和中间结论。它能减少重复调用，支持错误恢复，并为最终答案提供证据链。

### 2.2 Training-time distillation

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Beyond the training-free agent, the paper uses S-Agent as a teacher to create tool-use trajectories. The goal is to transfer spatial evidence-seeking behavior into a compact open model rather than relying only on a large closed-source planner at inference time.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 除了免训练智能体，论文还把 S-Agent 当作教师来生成工具调用轨迹。目标是把“主动寻找空间证据”的行为迁移到较小的开源模型中，而不是推理时一直依赖大型闭源规划器。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The authors start from a large spatial-instruction source and choose samples that are difficult or likely to benefit from tools. A strong teacher planner then generates multi-step trajectories containing tool requests, observations, reasoning turns, and final answers.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 作者从大规模空间指令数据源中挑选困难或可能需要工具的样本，再用强教师规划器生成多步轨迹，轨迹包含工具请求、观测结果、推理回合和最终答案。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The generated traces are filtered for answer validity and correctness. The paper keeps successful trajectories, decomposes them into final-answer, turn-level, and tool/expert supervision formats, and uses them to fine-tune an 8B Qwen3-VL backbone.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 生成轨迹会按答案有效性和正确性过滤。论文保留成功轨迹，并将其拆成完整最终答案轨迹、回合级轨迹和工具/专家监督样本，用来微调 8B 的 Qwen3-VL 骨干模型。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The authors emphasize that the raw tool trace is valuable supervision. It exposes the student to when tools should be called, how noisy observations should be interpreted, and how intermediate spatial evidence should be folded into a final answer.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 作者强调，原始工具轨迹本身就是重要监督。它让学生模型学习什么时候该调用工具、如何处理噪声观测，以及怎样把中间空间证据整合成最终答案。

### Fig. 3. S-300K 数据组成与工具调用统计

![Fig. 3](fig3_s300k_statistics.png)

**Caption:** Paraphrased from the paper: S-300K is built from quality-filtered trajectories and includes a distribution over data formats and tool/expert invocations.

**Caption[CN]:** 图 3 展示 S-300K 的数据组成与工具/专家调用分布，包括质量过滤后的数据比例、不同监督格式，以及各类工具专家调用占比。

**Reading note:** 图 3 提醒我们，S-Agent-8B 学到的不只是最终答案格式，更是“哪些空间问题需要哪些工具”的行为分布。

## 3. Experiments

### 3.1 Setup

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The experiments cover three main spatial reasoning benchmarks: MMSI-Bench, ViewSpatial-Bench, and ReVSI. The appendix also reports a long-video comparison on VSI-SUPER.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 实验主要覆盖三个空间推理基准：MMSI-Bench、ViewSpatial-Bench 和 ReVSI。附录还在 VSI-SUPER 上报告长视频比较。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The baseline set includes proprietary VLMs, open-weight general VLMs, and spatially specialized models. Zero-shot S-Agent is evaluated by wrapping strong VLM planners with spatial tools and memory.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 对比模型包括闭源 VLM、开源通用 VLM 和空间专用模型。零样本 S-Agent 的评估方式是把强 VLM 规划器包进空间工具和记忆闭环中。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> For the distilled model, the paper fine-tunes Qwen3-VL-8B-Instruct with S-300K using LLaMA-Factory, a sequence length of 8192, a learning rate of $5 \times 10^{-5}$, cosine decay, 3% warmup, and one epoch on 8 B200 GPUs.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 对蒸馏模型，论文使用 S-300K 微调 Qwen3-VL-8B-Instruct：训练框架为 LLaMA-Factory，序列长度 8192，学习率 $5 \times 10^{-5}$，余弦衰减、3% warmup，在 8 张 B200 GPU 上训练 1 个 epoch。

### 3.2 MMSI-Bench

### Table 1. MMSI-Bench 详细结果

![Table 1](table1_mmsi_bench.png)

**Caption:** Paraphrased from the paper: MMSI-Bench is grouped into positional relationship, geometric attribute, motion perception, and multi-step reasoning dimensions, with top results highlighted.

**Caption[CN]:** 表 1 按 MMSI-Bench 的空间能力类别展示结果，包括位置关系、几何属性、运动感知和多步推理等维度。

**Reading note:** 这张表是全文最核心的零样本证据：S-Agent 的平均分为 46.4，高于 Gemini 3 Pro 的 45.2 和 GPT-5.4 的 41.9。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> On MMSI-Bench, S-Agent achieves the best average score among the reported systems. Its improvement is especially meaningful because the benchmark mixes object/camera/region relations, size and distance attributes, motion, and multi-step spatial reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在 MMSI-Bench 上，S-Agent 获得报告系统中的最高平均分。这个提升有意义，是因为该基准混合了对象/相机/区域关系、尺寸与距离属性、运动感知和多步空间推理。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The paper reports that S-Agent improves GPT-5.4 by 4.5 average points and surpasses Gemini 3 Pro by 1.2 points. The gains are not uniform across all subcategories, which suggests that tool use helps most when explicit geometric evidence is accessible.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 论文报告 S-Agent 比 GPT-5.4 平均高 4.5 分，比 Gemini 3 Pro 高 1.2 分。不同子类的增益并不完全一致，这说明工具调用最能帮助那些可以获取显式几何证据的题目。

### 3.3 ViewSpatial-Bench

### Table 2. ViewSpatial-Bench 结果

![Table 2](table2_viewspatial_bench.png)

**Caption:** Paraphrased from the paper: ViewSpatial-Bench evaluates camera-perspective and person-perspective orientation, relative direction, and scene-simulation direction questions.

**Caption[CN]:** 表 2 展示 ViewSpatial-Bench 的五类题：相机视角物体朝向、相机视角相对方向、人视角物体朝向、人视角相对方向和人视角场景模拟相对方向。

**Reading note:** ViewSpatial 是 S-Agent 最显著的零样本胜场之一，平均 60.0，比 GPT-5.4 的 45.6 高 14.4 分。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> ViewSpatial-Bench directly tests viewpoint-dependent reasoning. S-Agent obtains an average score of 60.0 and shows strong gains on person-perspective relative direction and scene-simulation questions.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> ViewSpatial-Bench 直接测试依赖视角的空间推理。S-Agent 平均分达到 60.0，尤其在人视角相对方向和场景模拟类问题上提升明显。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The table supports the paper’s central intuition: when the answer depends on imagined viewpoint transformation or relative orientation, explicit spatial tools and memory can compensate for the VLM’s unstable internal geometry.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 这张表支撑了论文的核心直觉：当答案依赖想象视角转换或相对朝向时，显式空间工具和记忆可以弥补 VLM 内部几何表征不稳定的问题。

### 3.4 ReVSI

### Table 3. ReVSI leaderboard

![Table 3](table3_revsi_leaderboard.png)

**Caption:** Paraphrased from the paper: ReVSI evaluates numerical, multi-choice, and multi-step reasoning dimensions, including room size, relative direction, route planning, and other spatial skills.

**Caption[CN]:** 表 3 展示 ReVSI 排行榜，覆盖数值题、多选题、多步问题，以及房间尺寸、相对方向、路线规划等空间能力。

**Reading note:** S-Agent 平均 58.8，低于 Gemini 3 Pro 的 60.9，但在 relative direction 和 route planning 等子项上表现突出。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> On ReVSI, S-Agent ranks second overall among the compared systems. Its strongest categories include relative direction and route planning, two settings where accumulated scene evidence is naturally useful.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在 ReVSI 上，S-Agent 总体排名第二。它最强的类别包括相对方向和路线规划，这两类任务天然需要累积场景证据。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The ReVSI result is also a useful caution: S-Agent is not a universal dominance claim. It helps substantially on geometry-driven subskills but still depends on the quality of perception, tool outputs, and planner decisions.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> ReVSI 结果也提供了一个重要提醒：S-Agent 并不是全项目碾压。它在几何驱动子能力上帮助明显，但仍依赖感知质量、工具输出和规划器决策。

### 3.5 Trajectory distillation

### Table 4. 轨迹蒸馏结果

![Table 4](table4_trajectory_distillation.png)

**Caption:** Paraphrased from the paper: S-Agent-8B is compared with proprietary models, open-weight backbones, and the base Qwen3-VL-8B wrapped with S-Agent tools.

**Caption[CN]:** 表 4 比较 S-Agent-8B、闭源模型、开源骨干模型，以及直接把 Qwen3-VL-8B 放入 S-Agent 工具框架后的结果。

**Reading note:** 最值得看的是 S-Agent-8B 相比 Qwen3-VL-8B-Instruct 的提升：MMSI 31.1 到 41.6，ViewSpatial 42.2 到 46.8，ReVSI 49.1 到 52.8。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The distilled S-Agent-8B improves over the base Qwen3-VL-8B-Instruct on all three main benchmarks. This indicates that supervision from trajectories transfers more than just final answer style; it transfers a procedure for using evidence.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 蒸馏后的 S-Agent-8B 在三个主要基准上都超过基础 Qwen3-VL-8B-Instruct。这说明轨迹监督迁移的不只是最终答案格式，而是使用证据的过程。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The paper also observes that simply wrapping the base 8B planner with tools does not guarantee improvement. Tool use requires planning competence, noise handling, and memory integration; otherwise extra observations can confuse the model.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 论文还观察到，直接把基础 8B 规划器接入工具并不一定带来提升。工具调用需要规划能力、噪声处理和记忆整合；否则额外观测反而可能干扰模型。

### 3.6 Ablation

### Table 5. ViewSpatial 上的组件消融

![Table 5](table5_ablation_viewspatial.png)

**Caption:** Paraphrased from the paper: The ablation adds Level 1, Level 2, Level 3 evidence and memory modules step by step under a GPT-5.4 planner.

**Caption[CN]:** 表 5 在 GPT-5.4 规划器下逐步加入 L1、L2、L3 空间证据和两类记忆，展示各组件贡献。

**Reading note:** 最大跳跃来自 L3 专家：从 L1+L2 的 49.8 到加入 L3 后的 56.7；两类记忆进一步把 Full S-Agent 推到 60.0。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The ablation shows that raw 2D and 3D signals help, but high-level spatial experts provide the largest step. This matches the design goal: VLMs benefit from tools most when tool outputs are structured into task-relevant relations.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 消融表明，原始二维和三维信号有帮助，但高层空间专家带来最大增益。这符合设计目标：当工具输出被组织成任务相关关系时，VLM 最容易受益。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Scene Memory and Agent Memory each improve the result, and the full combination is best. This supports the claim that spatial reasoning needs both persistent world state and procedural trace.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 场景记忆和智能体记忆各自提升结果，完整组合最好。这支撑了本文主张：空间推理既需要持续世界状态，也需要过程性证据轨迹。

### 3.7 Qualitative analysis

### Fig. 4. 工具支撑的空间推理案例

![Fig. 4](fig4_tool_grounded_reasoning.png)

**Caption:** Paraphrased from the paper: A qualitative example shows S-Agent resolving a spatial relation by grounding objects and using depth-guided position evidence, while a vanilla VLM answers from incomplete visual cues.

**Caption[CN]:** 图 4 展示一个工具支撑推理案例：普通 VLM 因视觉线索不完整而误判，S-Agent 通过目标定位、深度和相对位置专家得到正确空间关系。

**Reading note:** 这个例子很好地说明了“为什么不是让 VLM 多看几张图就够了”：关键是把视觉证据转成可比较的三维关系。

### Fig. 5. 更多代表性空间推理可视化

![Fig. 5](fig5_qualitative_main.png)

**Caption:** Paraphrased from the paper: Additional examples show S-Agent across object counting, relative position, multi-step reasoning, and other spatial tasks.

**Caption[CN]:** 图 5 展示更多代表性任务，包括目标计数、相对位置、多步推理等。

**Reading note:** 图 5 的价值在于展示工具链的多样性：不同问题会触发不同证据路径，而不是一套固定提示词。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In the main qualitative example, a question asks about a shelf and a telephone from a first-person video. The vanilla VLM chooses an answer from incomplete cues, while S-Agent grounds the objects, estimates depth/positions, and uses a relative-position expert before answering.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 主文定性例子中，问题要求判断第一人称视频里架子和电话的空间关系。普通 VLM 依据不完整线索直接选择答案，而 S-Agent 先定位对象、估计深度/位置，再调用相对位置专家后作答。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The qualitative examples make the framework interpretable: the reader can see which object was grounded, which tool produced which evidence, and why the final option follows from that evidence.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 这些定性例子让框架具有可解释性：读者能看到哪个目标被定位、哪个工具产生了哪类证据，以及最终选项为什么由这些证据推出。

## 4. Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The conclusion restates S-Agent as a training-free framework for spatial reasoning in continuous multi-view images and videos. Its core is the coupling of a VLM planner, hierarchical spatial tools, and temporal memory.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 结论再次把 S-Agent 定位为面向连续多视角图像和视频的免训练空间推理框架。其核心是 VLM 规划器、层级空间工具和时间记忆的耦合。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The paper’s broader message is that spatial intelligence may require VLMs to behave less like passive image captioners and more like agents that decide what evidence to acquire and how to preserve it over time.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 论文更深层的信息是：空间智能可能要求 VLM 不再像被动图像描述器，而要像能够主动决定获取什么证据、如何随时间保存证据的智能体。

## Appendix A. Related work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The related-work appendix situates S-Agent among spatial-intelligence benchmarks and models for VLMs. Prior work has increasingly tested direction, distance, navigation, multi-view consistency, and embodied reasoning rather than only object recognition.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 附录相关工作将 S-Agent 放在空间智能 benchmark 和 VLM 模型的发展脉络中。已有研究越来越关注方向、距离、导航、多视角一致性和具身推理，而不只是目标识别。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> A second line of work uses agentic reasoning and tools. These systems may invoke perception models, code, geometry, or external modules, but many remain limited to static images or do not maintain a persistent spatial memory.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 第二条相关线索是 agentic 推理与工具调用。这类系统会调用感知模型、代码、几何模块或外部工具，但很多仍局限于静态图像，或者没有持续空间记忆。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The paper also discusses long-video and multi-view understanding. Existing work often expands context length or samples frames, whereas S-Agent focuses on constructing and updating spatial evidence across observations.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 论文也讨论长视频和多视角理解。现有方法常通过扩展上下文长度或采样帧来处理视频，而 S-Agent 关注的是跨观测构建并更新空间证据。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The authors’ claimed distinction is the closed loop between evidence acquisition, spatial computation, and memory. This distinguishes S-Agent from approaches that merely append detector outputs or depth maps as extra context.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 作者声称的区别在于证据获取、空间计算和记忆之间形成闭环。这使 S-Agent 不同于仅仅把检测结果或深度图作为额外上下文拼接的方法。

## Appendix B. Tools and experts

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Level 1 includes object detection and grounding tools. The detection tool is based on an open-vocabulary detector and returns boxes, labels, confidence, and location-related information; the VLM grounding tool can use multi-frame visibility and then verify objects.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> L1 包括目标检测和定位工具。检测工具基于开放词表检测器，返回框、标签、置信度和位置信息；VLM 定位工具可以利用多帧可见性并进一步验证目标。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Keyframe selection is used to search a long visual stream for frames likely to contain relevant evidence. This avoids forcing the planner to reason over every frame equally.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 关键帧选择用于在长视觉流中寻找可能包含相关证据的帧，避免规划器把每一帧都同等处理。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Level 2 includes metric depth and 3D reconstruction-style tools. These tools return metric depth, 3D coordinates, camera poses, and visualizations that let the planner compare objects in a shared space.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> L2 包括度量深度和三维重建风格工具。它们返回度量深度、三维坐标、相机位姿和可视化，使规划器能在共享空间中比较对象。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The metric measurement expert estimates distances, object sizes, and other scalar spatial quantities from grounded objects and depth/3D evidence.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 度量测量专家根据已定位对象和深度/三维证据估计距离、物体尺寸等标量空间量。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The counting expert aggregates detections across frames or views and tries to avoid double-counting the same object instance.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 计数专家会跨帧或跨视角聚合检测结果，并尽量避免把同一物体实例重复计数。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Orientation, relative-position, and object-centric-view experts convert raw geometry into linguistic relations such as left/right, front/back, facing direction, and how an object would appear from another viewpoint.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 朝向、相对位置和物体中心视角专家会把原始几何信息转换成语言化关系，例如左/右、前/后、朝向，以及从另一个视角看物体会是什么样。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> This appendix is important because it reveals that S-Agent is a system design, not a single neural architecture. Its effectiveness depends on how planners, detectors, depth models, memory, and experts are wired together.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 这个附录很重要，因为它说明 S-Agent 是一个系统设计，而不是单一神经网络结构。它的效果取决于规划器、检测器、深度模型、记忆和专家如何被组织在一起。

## Appendix C. S-300K details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The S-300K construction pipeline begins with sampled spatial questions and teacher-agent trajectory generation. Each raw trace records planner responses, tool calls, tool observations, and the final answer.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> S-300K 的构建从采样空间问题和教师智能体轨迹生成开始。每条原始轨迹记录规划器回应、工具调用、工具观测和最终答案。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The filtering stage keeps only trajectories whose final answer is valid and correct under the corresponding answer type. Multiple-choice, numeric, and free-form text answers are checked differently.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 过滤阶段只保留最终答案在对应答案类型下有效且正确的轨迹。多选题、数值题和自由文本题采用不同检查方式。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> After filtering, each retained trajectory is decomposed into complementary supervision forms: one complete final-answer trajectory, multiple turn-level planner samples, and specialized tool/expert sub-samples when verifiable.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 过滤后，每条保留轨迹被拆成互补监督形式：完整最终答案轨迹、多个回合级规划器样本，以及可验证的工具/专家子样本。

### Table 6. S-300K 统计

![Table 6](table6_s300k_statistics.png)

**Caption:** Paraphrased from the paper: S-300K contains final-answer, turn-level, and nontrivial tool/expert trajectories after quality filtering and decomposition.

**Caption[CN]:** 表 6 展示 S-300K 统计：51,596 条质量过滤轨迹，154,590 条回合级轨迹，86,205 条非平凡工具/专家轨迹，总计 292,391 条 SFT 样本。

**Reading note:** 这里的 “300K” 不是 30 万个独立问题，而是由 51,596 条有效轨迹拆解出的多种监督样本。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The dataset statistics show that 100,000 raw agent traces yield 51,596 quality-filtered trajectories and 292,391 supervised fine-tuning samples after decomposition.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 数据统计显示，100,000 条原始 agent 轨迹经过过滤后留下 51,596 条质量合格轨迹，拆解后形成 292,391 条监督微调样本。

## Appendix D. More experiments

### Table 7. VSI-SUPER 长视频比较

![Table 7](table7_vsi_super.png)

**Caption:** Paraphrased from the paper: The appendix compares S-Agent with long-video baselines on VSI-SUPER, reporting VSR and VSC under different video durations.

**Caption[CN]:** 表 7 在 VSI-SUPER 上比较 S-Agent 与长视频基线，分别报告不同视频时长下的 VSR 和 VSC。

**Reading note:** 论文提醒不要过度解读该 benchmark 的可靠性，但 S-Agent 在 VSR 上表现很强，尤其是 240 分钟设置。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The appendix reports that S-Agent performs strongly on the VSR part of VSI-SUPER, including long-duration settings, while the VSC scores remain very low for all compared systems.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 附录报告 S-Agent 在 VSI-SUPER 的 VSR 部分表现很强，包括长时长设置；但所有系统在 VSC 上分数都很低。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The authors caution that the benchmark may have limitations, so these numbers should be read as supplementary evidence rather than the main proof of the framework.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 作者提醒该 benchmark 可能存在局限，因此这些数字更适合作为补充证据，而不是框架有效性的主要证明。

## Appendix E. Additional qualitative visualizations

### Fig. 6. 附录定性案例一

![Fig. 6](fig6_appendix_qualitative.png)

**Caption:** Paraphrased from the paper: Additional appendix examples illustrate S-Agent on object counting and multi-step reasoning tasks.

**Caption[CN]:** 图 6 展示附录中的额外定性案例，包括目标计数和多步推理。

**Reading note:** 这些案例强调 S-Agent 会把不同工具输出汇总成最终选项，而不是让模型凭直觉猜。

### Fig. 7. 附录定性案例二

![Fig. 7](fig7_appendix_qualitative.png)

**Caption:** Paraphrased from the paper: More qualitative examples show evidence-driven spatial reasoning for relative position and route planning.

**Caption[CN]:** 图 7 展示更多证据驱动的空间推理，包括相对位置和路线规划。

**Reading note:** 图 7 对应 ReVSI 中 S-Agent 强项：相对方向与路线规划。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The appendix visualizations reinforce the paper’s qualitative argument: when the question requires counting, multi-step comparison, relative position, or route planning, explicit intermediate evidence makes the answer path more inspectable.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 附录可视化进一步强化论文的定性论点：当问题需要计数、多步比较、相对位置或路线规划时，显式中间证据让答案路径更可检查。

## My reading notes

### Core contribution

The paper’s real contribution is not a new detector, depth model, or VLM backbone. It is an agentic decomposition of spatial reasoning into planning, evidence acquisition, 3D/relational computation, and memory update. This is why the paper can claim both training-free gains and distillation gains.

### Why the idea is plausible

Spatial questions often fail because the model’s implicit geometry is brittle. S-Agent gives the model external handles: boxes for entities, depth/coordinates for metric structure, experts for converting geometry into language, and memory for keeping these facts alive across time.

### What to be careful about

The framework’s success depends on the quality of its tools. If object grounding is wrong, depth is noisy, or the planner chooses the wrong subquestion, the final answer can still fail. The ablation also shows that simply adding tools to a weak planner is not enough.

### Most useful takeaway for future work

For spatial VLM research, “better prompts” may be less important than “better evidence interfaces.” A strong follow-up direction is to make the planner learn when evidence is insufficient and which spatial expert can reduce uncertainty most efficiently.

