---
tags:
  - papers/WorldModel
  - RMBench
  - benchmark
  - memory
  - paper-comparison
aliases:
  - RMBench SOTA 与 Insight 对比
date: 2026-08-05
status: synthesis
last_verified: 2026-08-05
---

哈喽青林，我想请教一下：有没有把 VLM 做子任务规划、再接到 WAM 或其他 action model 上的论文，是比较推荐的？我现在主要卡在长程任务的语言怎么用，想先看看已有做法。

我目前主要基于ImageWAM做开发，这是从 Fast-WAM 这条线过来的：Fast-WAM 是比较 vanilla 的 world-action model，用当前观察同时预测未来视频和动作 chunk，没有单独的语言模块。ImageWAM 还是这个思路，骨干换成了 FLUX.2。LIBERO 这类短程任务，数据里通常只有一个 goal，我们就是把整句 task 文本 embedding 进模型。目前在做RMBench，这是一个长程任务，一条 demo 既有整局 goal，又有逐帧 subtask_text，过程会拆成好几段，所以除了整局指令，还能取出当前窗的 Current 和之前的 Previous。（不过ImageWAM FastWAM的codebase并没有用上）

我试语言时把标注里的 GT 子任务句拼进 prompt，作为 DiT 的文本条件去学动作，基本上没啥用偶尔还会掉点。

所以想问一下有没有比较推荐的「VLM 规划子任务 → 底层 WAM / policy 只执行当前子任务」这类工作？不一定限于 WAM，接到别的 action model 上的也可以。


# RMBench 相关论文实验与 Insight 对比

> [!abstract] 结论先行
> 我逐一筛查了本目录下 **26 个同时具有翻译与精读笔记的论文目录**。明确在 RMBench 上进行实质实验的共有 **4 篇**：RMBench 原始论文、WLA、MemoryWAM、DiM-WAM。
>
> - 若只看作者各自论文表中的**九任务总体成功率**，当前最高报告值是 **MemoryWAM 83.0%**；但它与 DiM-WAM 的审计后协议并不完全一致，不能写成严格统一榜单。
> - 若只看四个 $M(n)$ 任务，MemoryWAM 的表中结果最高（按逐项结果重算为 **81.5%**）；WLA 与 DiM-WAM 分别为 **56.5%** 和 **56.3%**，均值接近但强项完全不同。
> - 四篇工作的真正演进不是“窗口越来越长”，而是：**显式分层记忆 → 语言化进度记忆 → 多保真度视觉缓存 → 有界的多样事件记忆**。

## 1. 全库筛选结果

| 论文 | RMBench 实验范围 | 方法 | 精读 / 翻译 |
|---|---|---|---|
| *RMBench: Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design* | 全部 9 任务：5 个 $M(1)$ + 4 个 $M(n)$ | Mem-0 | [精读](<RMBench Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design/paper_DeepPaperNote.md>) · [翻译](<RMBench Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design/paper.md>) |
| *World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis* | 仅 4 个 $M(n)$ 任务 | WLA-0 | [精读](<World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis/paper_DeepPaperNote.md>) · [翻译](<World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis/paper.md>) |
| *MemoryWAM: Efficient World Action Modeling with Persistent Memory* | 全部 9 任务 | MemoryWAM | [精读](<MemoryWAM Efficient World Action Modeling with Persistent Memory/paper_DeepPaperNote.md>) · [翻译](<MemoryWAM Efficient World Action Modeling with Persistent Memory/paper.md>) |
| *DiM-WAM: World Action Modeling with Diverse Historical Event Memory* | 全部 9 任务；使用作者审计、调整后的相机与采样协议 | DiM-WAM | [精读](<DIM-WAM World-Action Modeling with Diverse Historical Event Memory/paper_DeepPaperNote.md>) · [翻译](<DIM-WAM World-Action Modeling with Diverse Historical Event Memory/paper.md>) |

其余 22 个论文目录的 `paper.md`、`detailed_paper.md` 与 `paper_DeepPaperNote.md` 中均未发现 RMBench 实验。目录顶层的调研/设计文档不计作论文；仅讨论 RoboTwin、LIBERO 或一般长时程任务，也不计为 RMBench 实验。

## 2. 作者报告结果账本

以下均为成功率（%）。数值用于定位论文内证据，**不是协议完全统一的第三方排行榜**。

| 论文 / 方法 | $M(1)$ 平均 | $M(n)$ 平均 | 九任务总体 | 最关键的同文对照 | 可比性说明 |
|---|---:|---:|---:|---|---|
| RMBench / Mem-0 | 52.8 | 28.5 | 42.0 | $\pi_{0.5}$ 总体 10.4 | 原始 benchmark 协议；$M(n)$ 的 Mem-0 额外使用子任务分解与终止分类器 |
| WLA / WLA-0 | — | **56.5** | — | 去掉 $L_{lang}$：56.5 → 17.3 | 仅评测 $M(n)$；每任务训练 30k 步，不能将 56.5 当作九任务总体分数 |
| MemoryWAM | 84.2¹ | **81.5¹** | **83.0** | LingBot-VA：78.2；Press Button 上 full attention 与 hybrid 均为 87 | 全九任务，但 Swap T 额外输入动作历史、Observe and Pick Up 使用预训练；跨模型 backbone/recipe 未完全对齐 |
| DiM-WAM | **80.6** | **56.3** | **69.8** | 训练匹配 LingBot-VA：34.8 → 69.8 | 作者发现腕部/姿态泄漏后调整 $M(1)$ 相机与步幅；与原始表及 MemoryWAM 不宜直接硬排 |

> ¹ MemoryWAM 论文只报告总体 83.0；84.2 与 81.5 是根据论文 Table 1 的五个 $M(1)$ 和四个 $M(n)$ 逐项成功率重算。

### 四个 $M(n)$ 任务的逐项报告值

| 方法 | Battery Try | Blocks Ranking Try | Cover Blocks | Press Button | 平均 |
|---|---:|---:|---:|---:|---:|
| Mem-0 | 28 | 18 | 68 | 0 | 28.5 |
| WLA-0 | 45 | 23 | 84 | 74 | 56.5 |
| MemoryWAM | 41 | **100** | **98** | **87** | **81.5¹** |
| DiM-WAM | **48** | 87 | 56 | 34 | 56.3 |

这个表最有价值的不是排序，而是暴露**不同记忆表征的偏好**：WLA 对有明确程序与计数结构的 Cover Blocks、Press Button 很强；DiM-WAM 在需要保存多次不同试错事件的 Blocks Ranking Try 上明显更强；MemoryWAM 则在后三项同时很高，说明连续视觉 gist 加完整 anchor/recent cache 能覆盖更宽的历史信息类型。由于相机、步幅、训练步数、动作历史和预训练设置不同，这些解释应视为跨论文假设，而不是已经完成的受控因果比较。

## 3. 各篇文章的核心 Insight

### 3.1 RMBench / Mem-0：先把“记忆”拆成可诊断职责

RMBench 的真正贡献不是 42.0% 这个分数，而是提出 Task Memory Complexity：$M(1)$ 表示至少需要一条任务相关历史观测，$M(n)$ 表示需要累计多条历史事件。Mem-0 进一步把记忆分成：保存子任务初始参照的 **anchor memory**、保存近期动态的 **sliding memory**、保存已完成子任务及终止画面的 **key memory**。

最重要的实验洞察是：长程失败不一定是“忘了”，也可能是“不知道何时切换”。使用模拟器真值终止信号后，$M(n)$ 从 28.5 提升到 45.3，说明终止检测是规划—执行闭环的显著瓶颈。Mem-0 因而更适合作为**诊断基线**，而不是最终统一架构。

### 3.2 WLA：把语言子任务当作可读写的进度状态

WLA 的核心不是保存更多视觉帧，而是让模型在每次动作生成前预测当前可执行的文本子任务，并把已执行子任务写回历史。语言因此同时承担三件事：任务分解、离散进度表示和可解释记忆接口。移除语言损失后，$M(n)$ 平均从 56.5 降到 17.3；Cover Blocks 从 84 降到 18，Press Button 从 74 降到 1，这是四篇中最强的单组件变化之一。

但该消融同时移除了子任务监督、改变了记忆内容和动作条件，不能进一步区分收益来自“语言表征”“人工/生成的子任务标签”还是“每步重推断进度”。因此 WLA 最可信的 Insight 是：**离散程序状态应与动作生成同步更新**；尚不能推出自然语言一定是最优载体。

### 3.3 MemoryWAM：按信息保真度分配视觉历史，而非全存或全丢

MemoryWAM 把视觉历史拆成三种保真度：初始事件边界保留完整 anchor frames，近期控制保留完整 sliding window，更早的每帧只永久追加少量 gist tokens。它让动作专家直接读取同一视频侧 KV cache，从而在不执行未来视频去噪的情况下利用持久历史。

其最有说服力的机制证据是：Press Button 上 hybrid memory 与 full attention 同为 87%，但单层延迟和显存更低；移除 gist 后 Press Button 从 87 降到 5，移除 anchor 后 Cover Blocks 从 98 降到 58。也就是说，**过程状态需要持续摘要，初始布局需要高保真锚点**，两者不可互换。

它的局限也很清楚：gist 是逐帧追加，所以缓存仍是 $O(N/d)$ 而非常数；效率曲线只测单层前向，83.0 的主表又不是完全 equal-backbone。因此应把它称为当前本地论文集中**最强的作者报告全九任务结果与高效持久缓存方案**，而不是已被统一协议验证的绝对 SOTA。

### 3.4 DiM-WAM：把有限容量用于“不同事件”，而不是均匀压缩时间

DiM-WAM 的 DHEM 使用多个有界记忆库，从当前观察抽取不同候选事件；容量满时，以新颖性决定保留或丢弃，并用累计质量加权合并相邻冗余历史。训练期的进度头则迫使记忆编码任务阶段。相比 MemoryWAM 的逐帧 append-only gist，它更接近**固定预算下的事件选择与压缩**。

最可信的总体证据是训练匹配的 LingBot-VA 对照：34.8 → 69.8。固定总容量 32 时，1×32 到 4×8 将两任务均值从 75.5 提升到 90.0，也支持多库优于单库。但新颖性筛选、相邻合并、质量加权、库身份和多样性损失没有被逐项隔离；8×12 还同时增加库数和总容量。

这篇论文另一个重要 Insight 是**基准治理本身属于方法证据**：作者发现腕部视角可通过机械臂姿态泄漏初始位置，于是收紧相机和步幅。遗憾的是审计只覆盖一个任务，说明 RMBench 后续 SOTA 比较必须先做逐任务可见性与姿态泄漏测试。

## 4. 横向比较：四条不同的记忆路线

| 维度 | Mem-0 | WLA | MemoryWAM | DiM-WAM |
|---|---|---|---|---|
| 记忆单位 | 手工定义的起点、近期帧、子任务事件 | 文本子任务与已执行进度 | 完整视觉 KV + 每帧 gist KV | 多库事件 tokens |
| 时间结构 | 显式层级：子任务内 / 子任务间 | 每次动作前重推断离散进度 | 连续时间、逐帧追加 | 连续写入、事件级选择与合并 |
| 长期容量 | key memory 随子任务增长 | 文本历史随子任务增长 | 随帧数线性增长，但斜率压缩约 15 倍 | 固定 $K\times N$ 槽位 |
| 最强归纳偏置 | 不同时间尺度分工 | 语言化程序状态 | 不同历史位置采用不同保真度 | 多样性、新颖性与有界压缩 |
| 主要风险 | 终止分类器成为单点故障 | 强依赖子任务监督质量 | gist 不可解释，且仍非定长 | 写入规则贡献未拆开；进度可能学到示范节拍 |

综合来看，RMBench 任务需要的并不是一种单一“长记忆”：

1. **$M(1)$ 更需要高保真、不会被驱逐的参照。** Mem-0 的 anchor 消融和 MemoryWAM 的 anchor 消融都支持这一点。
2. **$M(n)$ 更需要阶段状态与事件选择。** WLA 用语言显式表示进度，DiM-WAM 用进度监督组织事件，MemoryWAM 则让连续 gist 自行保存过程状态。
3. **写入策略比单纯扩大窗口更关键。** 四篇共同否定了“只增加 recent frames 就能解决长程任务”。真正的问题是何时写、写什么、以何种保真度保留、何时切换与清空。
4. **记忆收益必须与视觉语义、低层精度和终止检测分开。** Observe and Pick Up、Swap T、Press Button 的失败说明，记住历史并不会自动解决对象辨识、精细接触或阶段终止。

## 5. 如何选基线与下一步实验

- **要复现 RMBench 的诊断框架**：从 Mem-0 开始，因为它最容易把 anchor、sliding、key 与 termination 分开解释。
- **要研究语言规划与进度追踪**：以 WLA 为核心对照，但必须补做标签来源、错误子任务注入和非语言离散状态对照。
- **要做全九任务的高性能、高效持久 WAM**：优先看 MemoryWAM；真正需要补的是统一 backbone 下的 sliding/full/hybrid 端到端延迟—显存—成功率曲线。
- **要做严格固定预算的长期事件记忆**：DiM-WAM 的方向最合适；应先补固定总槽数的 bank 数消融、各写入规则消融和逐任务泄漏审计。

一个可信的统一复评至少应固定：相机集合、图像分辨率、历史采样步幅、动作历史是否输入、预训练数据、每任务 demonstrations、训练更新步数、动作块与去噪步数、100-rollout 随机种子，以及 episode reset/termination 规则。在完成这组控制前，最准确的表述不是“谁绝对 SOTA”，而是：

> **MemoryWAM 给出本地论文集中最高的全九任务作者报告总体值；WLA 证明语言化进度对 $M(n)$ 很有效；DiM-WAM 提供最明确的训练匹配增益和有界事件记忆方案；Mem-0 则定义了后续工作仍在解决的诊断问题。**
