---
title: "DiM-WAM: World Action Modeling with Diverse Historical Event Memory"
title_cn: "DiM-WAM：具有多样化历史事件记忆的世界—动作建模"
authors: "Kai Wang, Zhaopeng Gu, Yixiang Chen, Yuan Xu, Qisen Ma, Jiabing Yang, Zhaowen Li, Yan Huang, Liang Wang, Peng Su"
source: "/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/ZX4VLCU3/Wang 等 - 2026 - DIM-WAM World-Action Modeling with Diverse Historical Event Memory.pdf"
pages: 8
---

# DiM-WAM：具有多样化历史事件记忆的世界—动作建模

> 本阅读稿逐段保留原文与中文译文；公式、算法、图表和参考文献均据所给 8 页 PDF 整理。`source_map.json` 提供页码、稳定块 ID、视觉对象与放置关系。

## 页面与章节索引

| PDF 页 | 内容 |
|---|---|
| 1 | 摘要、引言、Fig. 1 |
| 2 | 相关工作；方法概览、DHEM 记忆库，公式 (1)–(3) |
| 3 | Fig. 2；事件写入与压缩，公式 (4)–(10) |
| 4 | 融合、协作读取、Algorithm 1，公式 (11)–(15) |
| 5 | Fig. 3、Table I、进度训练和实验设置，公式 (16)–(19) |
| 6 | Fig. 4、Fig. 5、仿真与真实机器人实验 |
| 7 | Table II–IV、消融、跨库分析与结论 |
| 8 | Fig. 6、References [1]–[38] |

## 摘要

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> World action models (WAMs) jointly predict future visual states and actions, but short local context limits temporally dependent tasks. We introduce DiM-WAM, which augments a WAM with Diverse Historical Event Memory (DHEM). DHEM uses bank-conditioned candidate features, novelty-aware selection, and accumulated-mass-weighted fusion to retain complementary event tokens in bounded memory; these tokens condition video and action denoising, while auxiliary supervision encourages coarse progress cues. In a training-matched comparison with LingBot-VA on RMBench, DiM-WAM improves the average full-task success rate from 34.8% to 69.8%. Under the same demonstration and evaluation protocol on four real-world tasks, it improves the average stage success ratio from 70.6% to 93.5% and the average full-task success rate from 52.5% to 90.0%. Project page: https://wangkai-casia.github.io/dim-wam/.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 世界—动作模型（WAM）联合预测未来视觉状态和动作，但短局部上下文限制了其处理时间依赖任务的能力。本文提出 DiM-WAM：以多样化历史事件记忆（DHEM）增强 WAM。DHEM 通过由记忆库条件化的候选特征、新颖性感知选择和累积质量加权融合，在有界内存中保留互补事件 token；这些 token 为视频和动作去噪提供条件，辅助监督则鼓励模型编码粗粒度进度线索。在 RMBench 上与 LingBot-VA 的训练匹配比较中，DiM-WAM 将平均完整任务成功率从 34.8% 提升至 69.8%。在四项真实世界任务中，在相同演示与评测协议下，其平均阶段成功率从 70.6% 提升至 93.5%，平均完整任务成功率从 52.5% 提升至 90.0%。项目主页：https://wangkai-casia.github.io/dim-wam/。

# I. Introduction / 引言

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Vision-language-action models (VLAs) learn robot policies by predicting actions from language instructions and visual observations [1]–[5]. This action-centric formulation enables scalable policy learning, but sparse action labels provide limited supervision for fine-grained manipulation dynamics. WAMs alleviate this limitation by jointly predicting executable actions and future visual states, where future visual prediction provides dense temporal supervision [6]–[8]. However, existing WAMs remain limited in long-horizon tasks, where correct actions often cannot be inferred from current observations or short local contexts alone.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 视觉—语言—动作模型（VLA）从语言指令和视觉观测预测动作，以学习机器人策略 [1]–[5]。这种以动作为中心的形式支持可扩展策略学习，但稀疏动作标签对细粒度操作动力学提供的监督有限。WAM 通过联合预测可执行动作和未来视觉状态来缓解这一局限，其中未来视觉预测提供稠密的时间监督 [6]–[8]。然而，现有 WAM 在长时程任务中仍受限：正确动作往往无法仅由当前观测或短局部上下文推断。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Consider the water-dispenser task in Fig. 1. When the robot reaches for the same switch, the observations immediately before the turn-on and turn-off actions can appear visually similar, particularly when transparent water is difficult to perceive. Nevertheless, the required actions differ: the robot should interact with the switch at one stage but avoid or reverse the interaction at another. A WAM relying only on current observations or short contexts may therefore execute incorrect actions or stop at the wrong stage. Resolving this ambiguity requires access to key historical events and task-progress cues.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 考虑 Fig. 1 的饮水机任务。当机器人伸向同一个开关时，打开与关闭动作之前的观测在视觉上可能相似，尤其是透明水难以被感知时。然而，所需动作不同：机器人在一个阶段应操作开关，在另一阶段则应避免或反向该交互。仅依赖当前观测或短上下文的 WAM 因而可能执行错误动作，或在错误阶段停止。消解这一歧义需要访问关键历史事件和任务进度线索。

### Fig. 1. 饮水机任务中的时间歧义

![Fig. 1](WorldModel/DIM-WAM%20World-Action%20Modeling%20with%20Diverse%20Historical%20Event%20Memory/assets/fig1.png)

**Caption:** Temporal ambiguity in the water-dispenser task: similar local observations near the switch require different actions depending on interaction history and task progress.
**Caption[CN]:** 饮水机任务中的时间歧义：开关附近相似的局部观测会因交互历史和任务进度不同而需要不同动作。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Long-horizon manipulation requires retaining different types of task-relevant events across tasks and stages. For example, some events indicate whether an interaction has occurred or a subtask has been completed, while others preserve information about layouts, target identities, or object-state changes needed later. Such diversity motivates a memory mechanism that can discover and preserve complementary event patterns.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 长时程操作要求跨任务和跨阶段保留不同类型的任务相关事件。例如，有些事件指示某次交互是否发生或子任务是否完成；另一些事件则保留后续所需的布局、目标身份或物体状态变化信息。这种多样性要求记忆机制能够发现并保存互补的事件模式。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Simply enlarging the local context increases computational cost and may dilute attention to sparse but task-critical events. Memory-augmented VLAs demonstrate the value of history [9]–[12], but action-centric supervision provides limited signals for discovering and organizing heterogeneous historical events. In contrast, WAMs couple action learning with future visual prediction, providing richer supervision over both robot actions and environmental changes. This visual-action signal facilitates learning diverse historical event representations and enables the memory module to implicitly preserve complementary event patterns for prediction and control.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 简单扩大局部上下文会增加计算成本，并可能稀释对稀疏但任务关键事件的注意力。记忆增强 VLA 证明了历史信息的价值 [9]–[12]，但以动作为中心的监督对发现和组织异质历史事件提供的信号有限。相比之下，WAM 将动作学习与未来视觉预测耦合，对机器人动作和环境变化均提供更丰富的监督。这种视觉—动作信号有助于学习多样的历史事件表征，使记忆模块能隐式保存用于预测和控制的互补事件模式。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Inspired by the multiple memory subsystems (MMSS) view of human cognition, where functionally distinct memory systems may cooperate or compete [13], we organize historical information into multiple memory banks. Rather than assigning predefined semantics to individual banks, we allow them to specialize implicitly in complementary event patterns while sharing a bounded capacity. Based on this design, we propose DiM-WAM, a memory-augmented WAM with Diverse Historical Event Memory (DHEM). DHEM preserves informative event tokens through novelty-aware selection, compresses redundancy via accumulated-mass-weighted fusion, and encourages task-stage representations through progress-aware training. The resulting memory tokens are combined with the local WAM context to condition video and action denoising. Experiments on RMBench [14] and four real-world Franka tasks show gains over the in-house WAM baselines, including a 90.0% average full-task success rate in the real-world evaluation.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 受人类认知的多记忆子系统（MMSS）观点启发——功能不同的记忆系统可以协作或竞争 [13]——作者将历史信息组织到多个记忆库中。他们并不为各库指定预定义语义，而是让各库在共享有界容量时隐式专化于互补事件模式。基于此设计，本文提出带有 DHEM 的记忆增强 WAM——DiM-WAM。DHEM 通过新颖性感知选择保留信息性事件 token，以累积质量加权融合压缩冗余，并通过进度感知训练鼓励任务阶段表征。得到的记忆 token 与局部 WAM 上下文结合，为视频和动作去噪提供条件。在 RMBench [14] 和四项真实 Franka 任务上的实验显示其优于内部 WAM 基线；真实评测中的平均完整任务成功率达到 90.0%。

# II. Related Work / 相关工作

## A. WAMs

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Prior WAMs use future visual prediction to provide dense temporal supervision for robot policies. Early video-based approaches formulate decision making as conditional future-video generation and recover actions from predicted visual trajectories [15]–[17]. More recent methods strengthen visual-action coupling by jointly predicting future observations and actions, or unify action prediction with visual or proprioceptive state prediction and value estimation [6]–[8], [18], [19]. Efficiency-oriented variants compress predicted futures, separate joint video training from test-time generation, or decode only actions during inference [20]–[22]. Existing WAMs improve future prediction, visual-action coupling, and inference efficiency, but do not address task-relevant history storage and retrieval under bounded memory. Our work complements them by introducing observation-grounded long-term memory into WAMs.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 既有 WAM 使用未来视觉预测为机器人策略提供稠密时间监督。早期视频方法把决策写成条件未来视频生成，并从预测视觉轨迹恢复动作 [15]–[17]。较新的方法联合预测未来观测与动作，以强化视觉—动作耦合；或将动作预测与视觉/本体感觉状态预测及价值估计统一 [6]–[8], [18], [19]。面向效率的方法则压缩预测未来、将联合视频训练与测试时生成分离，或仅在推理时解码动作 [20]–[22]。这些方法改善了未来预测、视觉—动作耦合和推理效率，但未处理有界内存下任务相关历史的存储与检索；本文以观测驱动的长期记忆补足这一点。

## B. Memory-Augmented Vision-Language-Action Models

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Memory-augmented VLAs incorporate historical information into policy inference through several complementary designs. SAM2Act reuses object-centric visual traces [9], while MemoryVLA separates perceptual and cognitive memory for low-level evidence and high-level task context [10]. Other methods organize history across multiple temporal scales [11], maintain context through recurrent queries [12], selectively retain event-driven evidence [23], or combine memory with imagination-based temporal modeling [24]. These methods improve temporal reasoning in VLA policies, but primarily target action inference rather than memory design for joint prediction and control in WAMs.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 记忆增强 VLA 通过若干互补设计把历史信息纳入策略推理。SAM2Act 复用以对象为中心的视觉轨迹 [9]；MemoryVLA 则为低层证据与高层任务上下文分离感知记忆和认知记忆 [10]。其他方法在多时间尺度上组织历史 [11]、用循环查询维持上下文 [12]、选择性保留事件驱动证据 [23]，或把记忆与基于想象的时间建模结合 [24]。这些方法改善了 VLA 策略的时间推理，但主要面向动作推理，而不是 WAM 联合预测与控制所需的记忆设计。

## C. Memory-Augmented Long Video Generation

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Long-video generation faces a related challenge: extending fixed-context models to longer horizons while preserving temporal consistency. Existing methods improve sequence efficiency through state-space models, block scans, or linear attention [25]–[27]. Others compress or organize history with recurrent memory vectors, key-value (KV) cache compression, local-global caches, retrieval, or entity-centric memory [28]–[33]. Long-video memory mainly targets visual consistency, whereas WAM memory must encode task progress, object states, and action consequences for closed-loop control.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 长视频生成面临相近挑战：在维持时间一致性的同时，将固定上下文模型扩展至更长时程。现有方法通过状态空间模型、块扫描或线性注意力提高序列效率 [25]–[27]；另一些方法采用循环记忆向量、键值（KV）缓存压缩、局部—全局缓存、检索或实体中心记忆来压缩或组织历史 [28]–[33]。长视频记忆主要服务于视觉一致性，而 WAM 记忆还必须为闭环控制编码任务进度、物体状态和动作后果。

# III. Method / 方法

## A. Overview: Multi-Scale World Action Modeling / 概览：多尺度世界—动作建模

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> As shown in Fig. 2(a), at decision segment $i$, DiM-WAM takes language instruction $c$, local key–value (KV) context $C_i$ from the sliding-window WAM cache, and persistent long-term memory state $M_i$. The valid event tokens in $M_i$ form the readable memory-token sequence $R_i$ defined in Sec. III-D. The model predicts future visual latents and actions over prediction horizon $H$. The memory-token sequence conditions both denoising branches, while an auxiliary progress objective supervises the memory readout during training.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 如 Fig. 2(a) 所示，在决策片段 $i$，DiM-WAM 接收语言指令 $c$、来自滑动窗口 WAM 缓存的局部键值（KV）上下文 $C_i$，以及持久化长期记忆状态 $M_i$。$M_i$ 中的有效事件 token 构成 III-D 节定义的可读记忆 token 序列 $R_i$。模型在预测时域 $H$ 内预测未来视觉潜变量和动作。该记忆 token 序列同时为两个去噪分支提供条件，辅助进度目标则在训练时监督记忆读出。

$$
I_i = (H_i^{\mathrm{short}}, H_i^{\mathrm{long}}, F_i^{\mathrm{short}}, G_i^{\mathrm{prog}}). \tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For bookkeeping, Eq. (1) summarizes the temporal evidence available to the model: short-term history from the sliding-window KV cache, long-term history from DHEM, predicted short-term video-action evolution, and coarse task-progress information.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 为便于记号，式 (1) 汇总模型可获得的时间证据：来自滑动窗口 KV 缓存的短期历史、来自 DHEM 的长期历史、预测的短期视频—动作演化，以及粗粒度任务进度信息。

$$
(\hat z_{i:i+H-1},\hat a_{i:i+H-1}) = f_\theta(C_i,c;M_i). \tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> During inference, Eq. (2) predicts future visual latents and actions from the language instruction, local context, and long-term memory. $f_\theta$ maps the local context, instruction, and readable representation of $M_i$ to future visual latents $\hat z$ and actions $\hat a$. The local context captures recent motion and visual cues, while persistent memory provides cross-stage evidence such as past interactions and object-state changes.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 推理时，式 (2) 根据语言指令、局部上下文和长期记忆预测未来视觉潜变量与动作。$f_\theta$ 将局部上下文、指令和 $M_i$ 的可读表征映射为未来视觉潜变量 $\hat z$ 与动作 $\hat a$。局部上下文捕捉近期运动和视觉线索，持久记忆则提供过去交互、物体状态变化等跨阶段证据。

### Fig. 2. DiM-WAM 总览

![Fig. 2](WorldModel/DIM-WAM%20World-Action%20Modeling%20with%20Diverse%20Historical%20Event%20Memory/assets/fig2.png)

**Caption:** Overview of DiM-WAM: (a) the DHEM-conditioned WAM framework, (b) task-progress supervision, and (c) redundancy-based memory merging.
**Caption[CN]:** DiM-WAM 概览：(a) 由 DHEM 条件化的 WAM 框架，(b) 任务进度监督，(c) 基于冗余的记忆合并。

## B. Diverse Historical Event Memory Banks / 多样化历史事件记忆库

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Historical events in long-horizon tasks have different semantic roles and retention needs. If all events share one bank, heterogeneous but temporally adjacent events compete for slots and may be destructively mixed by similarity-based merging. We therefore use multiple parallel memory banks to maintain complementary evidence.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 长时程任务中的历史事件具有不同语义角色和保留需求。若所有事件共享一个记忆库，异质但时间相邻的事件会竞争槽位，并可能在基于相似度的合并中发生破坏性混合。因此，作者使用多个并行记忆库来维持互补证据。

$$
M_i=\{M_i^k\}_{k=1}^{K},\qquad M_i^k=\{e_{i,k,n}\}_{n=1}^{N},\qquad e_{i,k,n}=(m_{i,k,n},t_{i,k,n},\alpha_{i,k,n},v_{i,k,n}). \tag{3}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Before decision segment $i$, DHEM's long-term memory state $M_i$ contains $K$ parallel memory banks, each with $N$ bounded slots. $m_{i,k,n}\in\mathbb{R}^d$ is a $d$-dimensional event token, $t_{i,k,n}$ its timestamp, $\alpha_{i,k,n}$ its accumulated mass, and $v_{i,k,n}\in\{0,1\}$ its validity indicator. Thus every memory event stores token, time, mass, and validity, for total cost $O(KN)$. Bank roles are not predefined: bank-specific learnable summary queries induce different observation views during writing, bank-local maintenance produces different retention trajectories, the diversity loss discourages collapse, and bank-identity embeddings label sources during reading.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在决策片段 $i$ 之前，DHEM 的长期记忆状态 $M_i$ 由 $K$ 个并行记忆库组成，每库有 $N$ 个有界槽位。$m_{i,k,n}\in\mathbb{R}^d$ 是 $d$ 维事件 token，$t_{i,k,n}$ 是时间戳，$\alpha_{i,k,n}$ 是累积质量，$v_{i,k,n}\in\{0,1\}$ 是有效性指示符。因此每个记忆事件存储 token、时间、质量和有效性，总成本为 $O(KN)$。记忆库角色不预先设定：库特定的可学习摘要查询在写入时产生不同观测视角，库内维护形成不同保留轨迹，多样性损失防止塌缩，读取时的库身份嵌入标识 token 来源。

## C. Writing and Maintenance of Historical Events / 历史事件的写入与维护

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> After extracting a bank-conditioned candidate event feature from the current observation collected from the environment, each bank independently updates its bounded memory using novelty-aware retention and redundancy-based compression. After segment $i$, the observation is encoded as visual features $X_i=[x_{i,j}]_{j=1}^{L_i}$, where $L_i$ is the number of visual tokens. Each bank uses its learnable summary query $q_k$ to extract a candidate event feature.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 从环境采集的当前观测中提取出由记忆库条件化的候选事件特征后，每个库使用新颖性感知保留和基于冗余的压缩，独立更新其有界记忆。片段 $i$ 之后，观测被编码为视觉特征 $X_i=[x_{i,j}]_{j=1}^{L_i}$，其中 $L_i$ 为视觉 token 数。每个库利用其可学习摘要查询 $q_k$ 提取候选事件特征。

$$
h_{i,j}=\mathrm{LN}_x(x_{i,j}),\qquad r_k=\mathrm{LN}_q(q_k). \tag{4}
$$

$$
a_{i,k,j}=\mathrm{Softmax}_j\left(\frac{(W_qr_k)^\top(W_hh_{i,j})}{\sqrt{d_r}}\right),\qquad
s_{i,k}=\sum_{j=1}^{L_i}a_{i,k,j}h_{i,j},\qquad
\tilde u_{i,k}=s_{i,k}+\mathrm{FFN}(\mathrm{LN}_o(s_{i,k})). \tag{5}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> With shared query and key projections of projection dimension $d_r$, Eq. (5) produces token weights $a_{i,k,j}$, attended summary $s_{i,k}$, and candidate event feature $\tilde u_{i,k}$. LN denotes layer normalization and FFN a feed-forward network. All banks observe the same features but yield different candidate features; persistent memory stores event tokens derived from these features, not generated predictions.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 通过投影维度为 $d_r$ 的共享查询和键投影，式 (5) 得到 token 权重 $a_{i,k,j}$、注意力摘要 $s_{i,k}$ 与候选事件特征 $\tilde u_{i,k}$。LN 表示层归一化，FFN 表示前馈网络。所有记忆库观察同一组特征，但产生不同候选特征；持久记忆保存由这些特征导出的事件 token，而不是模型生成的预测。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> In each bank, slot 1 is a fixed initial-state anchor, slot $N$ is the latest event, and slots $2,\ldots,N-1$ hold compressed history. Omitting segment and bank indices, redundancy priority for two valid events $p,q$ is defined as follows; a high priority means nearby semantic redundancy, namely low relative novelty.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在每个记忆库中，槽位 1 是固定初始状态锚点，槽位 $N$ 是最新事件，槽位 $2,\ldots,N-1$ 存放压缩历史。省略片段和库索引后，两个有效事件 $p,q$ 的冗余优先级定义如下；高优先级表示语义相近的时间邻近冗余，即相对新颖性低。

$$
\rho_k(p,q)=\frac{1+\cos(m_p,m_q)}{2}\exp\left(-\frac{|t_p-t_q|}{\tau}\right). \tag{6}
$$

$$
\mathcal A_{i,k}=\{(s,s+1)\mid 2\le s\le N-2,\ v_{k,s}v_{k,s+1}=1\}. \tag{7}
$$

$$
(p^\star,q^\star)=\arg\max_{(p,q)\in\mathcal A_{i,k}}\rho_k(p,q). \tag{8}
$$

$$
\rho^{\mathrm{new}}_{i,k}=\frac{1+\cos(m_{k,N},\tilde u_{i,k})}{2}\exp\left(-\frac{|t_{k,N}-i|}{\tau}\right). \tag{9}
$$

$$
\rho^{\mathrm{new}}_{i,k}\ge\rho_k(p^\star,q^\star). \tag{10}
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> When a bank is full, only adjacent middle-history pairs in Eq. (7) are eligible. Eq. (8) selects the most redundant candidate pair; Eq. (9) measures redundancy between the incoming candidate and latest event. Under Eq. (10), the incoming candidate is discarded if its redundancy with the latest event is no smaller than the maximum redundancy of eligible historical pairs, because retaining it would sacrifice a less redundant pair. Otherwise $(p^\star,q^\star)$ is merged to make room.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 当记忆库已满时，只有式 (7) 的相邻中段历史对可被选择。式 (8) 选择冗余最高的候选对；式 (9) 度量新到候选与最新事件之间的冗余。若满足式 (10)，新候选与最新事件的冗余不小于可选历史对的最大冗余，因此丢弃该候选，因为保留它会牺牲一个更不冗余的历史对；否则合并 $(p^\star,q^\star)$ 以腾出空间。

## D. Cooperative Memory Reading / 协作式记忆读取

$$
m_{pq}=\frac{\alpha_pm_p+\alpha_qm_q}{\alpha_p+\alpha_q},\qquad
t_{pq}=\frac{\alpha_pt_p+\alpha_qt_q}{\alpha_p+\alpha_q},\qquad
\alpha_{pq}=\alpha_p+\alpha_q. \tag{11}
$$

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The merged event in Eq. (11) preserves accumulated evidence via mass-weighted fusion. $m_{pq}$, $t_{pq}$, and $\alpha_{pq}$ are its token, timestamp, and accumulated mass. The mass-weighted timestamp may be noninteger and is interpreted as a continuous representative time in Eq. (6). As it lies between the adjacent input timestamps, compacting after merging preserves chronological order. Algorithm 1 summarizes one bank update. The same similarity function and $\tau=N-1$ are used in every bank, but banks diverge because Eq. (5) supplies bank-specific candidates and updates depend on each bank’s retained state. Initialization fills all slots with valid copies of the first event; copies whose timestamp equals the fixed anchor ($t_r=t_1$) are evicted before the normal rule. Slot 1 remains anchor, slot $N$ latest, and middle history remains chronologically ordered; memory cost is $O(KN)$ independent of trajectory length.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 式 (11) 中的合并事件通过质量加权融合保留累积证据。$m_{pq}$、$t_{pq}$ 和 $\alpha_{pq}$ 分别为其 token、时间戳和累积质量。质量加权时间戳可以是非整数，并在式 (6) 中被解释为连续代表时间；其位于相邻输入的时间戳之间，因此合并后的压紧保持时间顺序。算法 1 总结单个记忆库的更新。每个库使用相同相似度函数和 $\tau=N-1$，但因式 (5) 提供库特定候选、更新又依赖各库保留状态而发生分化。初始化用首个事件的有效副本填满所有槽位；时间戳等于固定锚点的副本（$t_r=t_1$）在普通规则前被驱逐。槽位 1 始终为锚点、槽位 $N$ 始终为最新事件，中段历史始终按时间排序；内存成本不依赖轨迹长度，为 $O(KN)$。

### Algorithm 1. Update of bank $k$ at segment $i$ / 在片段 $i$ 更新记忆库 $k$

| English pseudocode | 中文伪代码 |
|---|---|
| **Require:** Bank $M^k$, features $X_i$, query $q_k$, time $i$; **Ensure:** updated bank $M^k$. | **输入：**记忆库 $M^k$、特征 $X_i$、查询 $q_k$、时间 $i$；**输出：**更新后的 $M^k$。 |
| 1–3. $r_k\leftarrow\mathrm{LN}_q(q_k)$; $\tilde u_{i,k}\leftarrow\mathrm{BankSummarize}(X_i;r_k)$ by Eq. (5); $e_{\mathrm{new}}\leftarrow(\tilde u_{i,k},i,1,1)$. | 1–3. 计算归一化查询；按式 (5) 汇总候选；建立新事件。 |
| 4–7. If uninitialized, fill all slots with $e_{\mathrm{new}}$, fix $e_1$ as anchor, and return. | 4–7. 若未初始化，用新事件填满所有槽位，固定 $e_1$ 为锚点后返回。 |
| 8–11. If $t_N=t_1$, assign $e_N\leftarrow e_{\mathrm{new}}$ and return. | 8–11. 若最新槽是初始化副本，则以新事件替换最新槽并返回。 |
| 12–16. If a middle slot $e_r$ has $t_r=t_1$, remove it, compact middle slots, move $e_N$ to $N-1$, write $e_N\leftarrow e_{\mathrm{new}}$, and return. | 12–16. 若中段存在初始化副本，删除、压紧中段，将旧最新事件移到 $N-1$，写入新事件并返回。 |
| 17–21. If an invalid middle slot exists, move $e_N$ to the first such slot, set $e_N\leftarrow e_{\mathrm{new}}$, and return. | 17–21. 若存在无效中段槽，将旧最新事件移入第一个无效槽，再写入新事件并返回。 |
| 22–32. Find $(p^\star,q^\star)$ by Eq. (8). If Eq. (10) holds, retain previous $e_N$ and return; otherwise save $e_N$, merge $e_{p^\star},e_{q^\star}$ by Eq. (11), compact the middle slots, move saved $e_N$ to $N-1$, write the new event to $N$, and return. | 22–32. 按式 (8) 找到最高优先级相邻对。若满足式 (10)，保留旧 $e_N$ 并返回；否则保存旧 $e_N$，按式 (11) 合并所选对、压紧中段、将旧最新事件移至 $N-1$、向 $N$ 写入新事件并返回。 |

$$
\pi_{i,n}=\pi_i^{\mathrm{cur}}-2(N-1-n). \tag{12}
$$

$$
R_i=\mathrm{RoPE}_{\pi}\left(\mathrm{Flat}_{n,k}\left[(m_{i,k,n}+b_k,\pi_{i,n})\right]_{v_{i,k,n}=1}\right). \tag{13}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> After bank-local writing, valid event tokens are flattened in slot-major, bank-minor order. Each is augmented with bank-identity embedding $b_k$. RoPE injects slot-relative temporal order without changing persistent content: slots are zero-indexed $n\in\{0,\ldots,N-1\}$ and assigned Eq. (12), whose two-coordinate step is a fixed implementation convention. All banks at a slot share $\pi_{i,n}$; $b_k$ distinguishes source. Eq. (13) forms the Transformer-readable sequence $R_i$. Slot recency, bank source, and event content are visible during prediction, while writing stays bank-local. RoPE follows retained slot order rather than reordering events by mass-weighted timestamps. As Fig. 3 shows, event tokens condition current denoising but are not appended to persistent KV cache; persistent memory updates only from later environment observations.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 库内写入后，有效事件 token 按“槽位优先、记忆库次序”展平；每个 token 加入库身份嵌入 $b_k$。RoPE 在不改变持久内容的情况下引入相对槽位时间顺序：槽位以 $n\in\{0,\ldots,N-1\}$ 从零编号，并按式 (12) 赋坐标，步长为 2 的坐标单位只是固定实现约定。处于同一槽位的所有记忆库共享 $\pi_{i,n}$，$b_k$ 区分来源。式 (13) 形成 Transformer 可读取序列 $R_i$。预测时槽位新近性、库来源和事件内容共同可见，而写入仍局限于各库。RoPE 遵循保留槽位顺序，而非按质量加权时间戳重排。Fig. 3 显示事件 token 为当前去噪提供条件，但不被追加到持久 KV 缓存；持久记忆只由后续环境观测更新。

### Fig. 3. 去噪过程中的 token 可见性

![Fig. 3](WorldModel/DIM-WAM%20World-Action%20Modeling%20with%20Diverse%20Historical%20Event%20Memory/assets/fig3.png)

**Caption:** Visibility among memory, video-latent, and action tokens during denoising.
**Caption[CN]:** 去噪过程中记忆、视频潜变量和动作 token 之间的可见性关系。

## E. Task-Progress-Aware Training / 任务进度感知训练

$$
p_i=\mathrm{Softmax}(h_{\mathrm{prog}}(\mathrm{Pool}(R_i))),\qquad p_i\in\Delta^{B-1}. \tag{14}
$$

$$
r_i=\begin{cases}\dfrac{i}{T-1},&T>1,\\0,&T=1.\end{cases} \tag{15}
$$

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> As Fig. 2(b) illustrates, an auxiliary head predicts a coarse progress bin during training, encouraging memory representations to encode trajectory-progress cues without acting as an explicit planner. In Eq. (14), $h_{\mathrm{prog}}$ is the progress head, $B$ the number of bins, $\Delta^{B-1}$ the probability simplex, and Pool mean pooling over valid event tokens. For a demonstration with $T$ decision segments and zero-indexed $i\in\{0,\ldots,T-1\}$, Eq. (15) safely defines normalized completion ratio.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 如 Fig. 2(b) 所示，一个辅助头在训练时预测粗粒度进度分箱，从而鼓励记忆表征编码轨迹进度线索，而不将其作为显式规划器。在式 (14) 中，$h_{\mathrm{prog}}$ 为进度头，$B$ 为进度分箱数，$\Delta^{B-1}$ 为概率单纯形，Pool 表示对有效事件 token 的均值池化。对于含 $T$ 个决策片段、索引从零开始的演示 $i\in\{0,\ldots,T-1\}$，式 (15) 安全地定义归一化完成比例。

$$
y_i=\min(\lfloor Br_i\rfloor,B-1),\qquad \mathcal L_{\mathrm{prog}}=-\log p_{i,y_i}. \tag{16}
$$

$$
\mu_{i,k}=\frac{1}{|V_{i,k}|}\sum_{n\in V_{i,k}}m_{i,k,n},\qquad \bar\mu_{i,k}=\frac{\mu_{i,k}}{\|\mu_{i,k}\|_2}. \tag{17}
$$

$$
\mathcal L_{\mathrm{div}}=\frac{1}{|\mathcal P|}\sum_{(k,l)\in\mathcal P}(\bar\mu_{i,k}^{\top}\bar\mu_{i,l})^2. \tag{18}
$$

$$
\mathcal L=\mathcal L_{\mathrm{video}}+\mathcal L_{\mathrm{action}}+\lambda_{\mathrm{div}}\mathcal L_{\mathrm{div}}+\lambda_{\mathrm{prog}}\mathcal L_{\mathrm{prog}}. \tag{19}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Eq. (16) defines target progress bin $y_i$ and loss; the head is an auxiliary training objective and does not participate in inference decisions. It encourages coarse trajectory-progress encoding rather than long-horizon planning. To discourage bank collapse, $V_{i,k}=\{n\mid v_{i,k,n}=1\}$ is the valid-slot set and Eq. (17) defines a normalized bank mean. With $\mathcal P=\{(k,l)\mid1\le k<l\le K\}$, minimizing Eq. (18)'s squared cosine similarity permits roles to emerge from bank-specific queries and state-dependent maintenance. Eq. (19) combines diffusion denoising mean-squared errors for future visual latents and masked action prediction (each unit weight) with diversity and progress losses balanced by $\lambda_{\mathrm{div}}$ and $\lambda_{\mathrm{prog}}$.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 式 (16) 定义目标进度分箱 $y_i$ 和损失；该头仅是训练辅助目标，不参与推理时决策。它鼓励编码粗粒度轨迹进度，而非进行长时程规划。为抑制记忆库塌缩，$V_{i,k}=\{n\mid v_{i,k,n}=1\}$ 是有效槽位集合，式 (17) 定义归一化库均值。令 $\mathcal P=\{(k,l)\mid1\le k<l\le K\}$，最小化式 (18) 的平方余弦相似度，使角色可从库特定查询和状态依赖维护中涌现。式 (19) 将未来视觉潜变量的扩散去噪均方误差和掩码动作预测误差（各自单位权重）与多样性、进度损失结合，后两者由 $\lambda_{\mathrm{div}}$ 和 $\lambda_{\mathrm{prog}}$ 平衡。

# IV. Experiments / 实验

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We evaluate temporally dependent long-horizon tasks in simulation and on real-world robots, analyze the roles of DHEM and progress supervision, and investigate whether the banks learn distinct behaviors.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 作者在仿真和真实机器人上评估时间依赖的长时程任务，分析 DHEM 与进度监督的作用，并考察各记忆库是否学到不同的行为。

### Table I. RMBench `put_back_block` 的评测协议审计

![Table I](WorldModel/DIM-WAM%20World-Action%20Modeling%20with%20Diverse%20Historical%20Event%20Memory/assets/table1.png)

| Camera views | Window | Stride | Initial state visible | Chance (%) | Success (%) |
|---|---:|---:|---|---:|---:|
| front + wrist + head | 30 | 1 | No | 25 | 86 |
| head + front | 30 | 1 | No | 25 | 41 |
| head + front | 60 | 1 | No | 25 | 49 |
| head + front | 120 | 1 | Yes | 100 | 88 |
| front + wrist + head | 30 | 4 | Yes | 100 | 100 |
| head + front | 30 | 4 | Yes | 100 | 98 |

**Caption:** Protocol audit for the RMBench `put_back_block` task. “Chance” denotes the ideal target-choice accuracy based only on locally visible target information and is not a full-task upper bound.
**Caption[CN]:** RMBench `put_back_block` 任务的协议审计。“Chance”表示仅基于局部可见目标信息时的理想目标选择准确率，并非完整任务的上界。

## A. Experimental Setup / 实验设置

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> DiM-WAM extends LingBot-VA [7], preserving its original video-and-action input–output interface and augmenting it with DHEM. RMBench [14], built on RoboTwin 2.0, includes five $M(1)$ tasks that rely on a few key historical observations and four $M(n)$ tasks requiring history accumulated across interaction steps. In `put_back_block` (Fig. 4), the robot moves a block to the center, presses a button, then returns it to its original one-of-four location; distinct initial states can yield similar intermediate observations, so failure occurs if the relevant historical event is not retained.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> DiM-WAM 在保留 LingBot-VA [7] 原始视频—动作输入输出接口的同时加入 DHEM。RMBench [14] 基于 RoboTwin 2.0 构建，包括五个依赖少数关键历史观测的 $M(1)$ 任务，以及四个需要跨交互步骤累积历史的 $M(n)$ 任务。在 `put_back_block`（Fig. 4）中，机器人将方块移至中心、按下按钮，然后把它送回四个可能初始位置之一；不同初始状态可产生相似的中间观测，若未保留相关历史事件，策略便可能失败。

### Fig. 4. `put_back_block` 任务关键帧

![Fig. 4](WorldModel/DIM-WAM%20World-Action%20Modeling%20with%20Diverse%20Historical%20Event%20Memory/assets/fig4.png)

**Caption:** Key frames of the RMBench `put_back_block` task. Similar intermediate observations may require different final target locations depending on the initial state.
**Caption[CN]:** RMBench `put_back_block` 任务的关键帧。相似的中间观测会因初始状态不同而要求不同的最终目标位置。

## B. Evaluation-Protocol Audit / 评测协议审计

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Table I audits whether camera views and temporal coverage expose the initial location to the local policy on `put_back_block`. Window is the number of input frames, and stride the input-frame subsampling interval rather than action horizon. The audit uses LingBot-VA with its official training parameters and varies only camera views, window, and stride. The wrist view raises success from 41% to 86% even though the initial state lies outside the local window, suggesting pose-dependent leakage. The authors therefore use head + front views, a 30-frame window, and stride 1 for the $M(1)$ runs marked † in Table II; because only `put_back_block` was audited, residual leakage in other tasks cannot be ruled out.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Table I 审计相机视角和时间覆盖是否会在 `put_back_block` 中向局部策略暴露初始位置。窗口是输入帧数量，步幅是输入帧子采样间隔而非动作时域。审计采用官方训练参数的 LingBot-VA，仅改变相机视角、窗口和步幅。尽管初始状态位于局部窗口之外，腕部视角仍将成功率从 41% 提升至 86%，表明存在随姿态变化的信息泄漏。因此作者为 Table II 中标 † 的 $M(1)$ 实验使用头部 + 前方视角、30 帧窗口和步幅 1；由于审计仅覆盖 `put_back_block`，其他任务中仍不能排除残余泄漏。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Following this audit, Fast-WAM, LingBot-VA, and DiM-WAM use the same RMBench protocol: head + front views, 30-frame window, $128\times128$ inputs, and strides 1 and 2 for $M(1)$ and $M(n)$ respectively. LingBot-VA and DiM-WAM are a training-matched controlled comparison: 50 demonstrations, identical non-method optimization settings, 1,500 steps, and 100 evaluation rollouts per task; only DHEM, progress supervision, and their objective terms differ. Fast-WAM [21] follows its official recipe as an additional protocol-matched in-house WAM baseline.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 依照此审计，Fast-WAM、LingBot-VA 和 DiM-WAM 使用相同 RMBench 协议：头部 + 前方视角、30 帧窗口、$128\times128$ 输入，$M(1)$ 和 $M(n)$ 分别采用步幅 1 与 2。LingBot-VA 与 DiM-WAM 构成训练匹配的对照：每任务 50 个演示、相同的非方法优化设置、1,500 个训练步骤及 100 次评测 rollout；仅 DHEM、进度监督和相关目标项不同。Fast-WAM [21] 按其官方配方训练，作为额外的协议匹配内部 WAM 基线。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> DiM-WAM uses AdamW with learning rate $10^{-5}$, batch size 1, gradient accumulation over 10 steps, and 1,500 optimization steps. DHEM uses $\lambda_{\mathrm{div}}=10^{-3}$, $\lambda_{\mathrm{prog}}=10^{-2}$, eight 12-slot banks, $B=10$, clean-KV dropout 0.3, and four-segment truncated backpropagation. Each task-specific model trains on eight NVIDIA H800 GPUs; comparisons are not compute matched. Real-robot experiments use one third-person camera at $224\times224$; LingBot-VA and DiM-WAM otherwise retain simulation configuration. Fast-WAM and $\pi_{0.5}$ use recommended recipes of 150 epochs and 20,000 steps. All methods predict seven absolute joint positions and one binary gripper state.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> DiM-WAM 使用 AdamW，学习率 $10^{-5}$、批大小 1、梯度累积 10 步、共 1,500 个优化步骤。DHEM 设置为 $\lambda_{\mathrm{div}}=10^{-3}$、$\lambda_{\mathrm{prog}}=10^{-2}$、8 个各含 12 槽位的记忆库、$B=10$、clean-KV dropout 为 0.3，以及四片段截断反向传播。每个任务特定模型在八张 NVIDIA H800 GPU 上训练；比较并非算力匹配。真实机器人实验使用一台 $224\times224$ 的第三人称相机，LingBot-VA 与 DiM-WAM 其余设置保持仿真配置。Fast-WAM 与 $\pi_{0.5}$ 分别使用推荐的 150 epoch 和 20,000 步配方。所有方法预测七个绝对关节位置和一个二值夹爪状态。

## C. Simulation Experiments / 仿真实验

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Fast-WAM, LingBot-VA, and DiM-WAM are evaluated under the audit-guided protocol. The LingBot-VA versus DiM-WAM comparison isolates DHEM and progress supervision under matched training, while Fast-WAM is an additional baseline. DP [36], ACT [37], $\pi_{0.5}$ [35], X-VLA [38], and Mem-0 [14] are RMBench-reported contextual reference points only. Thus only LingBot-VA versus DiM-WAM supports attribution to the proposed memory design.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Fast-WAM、LingBot-VA 和 DiM-WAM 均在审计引导的协议下评估。训练匹配的 LingBot-VA 对 DiM-WAM 比较用于隔离 DHEM 与进度监督的影响，Fast-WAM 是额外基线。DP [36]、ACT [37]、$\pi_{0.5}$ [35]、X-VLA [38] 和 Mem-0 [14] 仅作为 RMBench 报告的上下文参照。因此，只有 LingBot-VA 与 DiM-WAM 的比较支持把性能差异归因于所提记忆设计。

### Table II. RMBench 长时程任务主要仿真结果（成功率 %）

![Table II](WorldModel/DIM-WAM%20World-Action%20Modeling%20with%20Diverse%20Historical%20Event%20Memory/assets/table2.png)

| Task | TMC | DP | ACT | $\pi_{0.5}$ | X-VLA | Mem-0 | Fast-WAM† | LingBot-VA† | DiM-WAM† |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Observe and Pick Up | $M(1)$ | 1.0 | 1.0 | 9.0 | 9.0 | 4.0 | 2.0 | 4.0 | 13.0 |
| Rearrange Blocks | $M(1)$ | 0.0 | 29.0 | 13.0 | 13.0 | 89.0 | 0.0 | 63.0 | 99.0 |
| Put Back Block | $M(1)$ | 0.0 | 0.0 | 11.0 | 18.0 | 90.0 | 0.0 | 41.0 | 98.0 |
| Swap Blocks | $M(1)$ | 11.0 | 2.0 | 24.0 | 16.0 | 67.0 | 3.0 | 38.0 | 96.0 |
| Swap T | $M(1)$ | 20.0 | 2.0 | 15.0 | 3.0 | 14.0 | 9.0 | 25.0 | 97.0 |
| $M(1)$ Average | – | 6.4 | 6.8 | 14.4 | 11.8 | 52.8 | 2.8 | 34.2 | 80.6 |
| Battery Try | $M(n)$ | 10.0 | 19.0 | 16.0 | 26.0 | 28.0 | 5.0 | 33.0 | 48.0 |
| Blocks Ranking Try | $M(n)$ | 10.0 | 0.0 | 6.0 | 1.0 | 18.0 | 17.0 | 48.0 | 87.0 |
| Cover Blocks | $M(n)$ | 0.0 | 0.0 | 0.0 | 2.0 | 68.0 | 0.0 | 42.0 | 56.0 |
| Press Button | $M(n)$ | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 19.0 | 34.0 |
| $M(n)$ Average | – | 5.0 | 4.8 | 5.5 | 7.3 | 28.5 | 5.5 | 35.5 | 56.3 |
| Overall Average | – | 5.8 | 5.9 | 10.4 | 9.8 | 42.0 | 4.0 | 34.8 | 69.8 |

**Caption:** Main simulation results on RMBench long-horizon tasks. Values are success rates in percent. TMC denotes the RMBench $M(1)/M(n)$ task-memory category. DP, ACT, $\pi_{0.5}$, X-VLA, and Mem-0 are benchmark-reported results. The † columns are protocol-matched in-house WAM evaluations; LingBot-VA and DiM-WAM additionally form a training-matched comparison.
**Caption[CN]:** RMBench 长时程任务主要仿真结果。数值为百分比成功率。TMC 表示 RMBench 的 $M(1)/M(n)$ 任务记忆类别。DP、ACT、$\pi_{0.5}$、X-VLA 和 Mem-0 为基准报告结果。标 † 的列为协议匹配的内部 WAM 评测；LingBot-VA 与 DiM-WAM 还构成训练匹配比较。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> DiM-WAM achieves the highest reported success rate on eight of the nine RMBench tasks in Table II and exceeds benchmark-reported Mem-0 by 27.8 percentage points in overall average success. In the training-matched LingBot-VA comparison, it improves average success from 34.8% to 69.8%, with gains in both $M(1)$ (34.2% to 80.6%) and $M(n)$ (35.5% to 56.3%).

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> DiM-WAM 在 Table II 的九项 RMBench 任务中有八项取得最高报告成功率，整体平均成功率比基准报告的 Mem-0 高 27.8 个百分点。在训练匹配的 LingBot-VA 比较中，它将平均成功率从 34.8% 提升至 69.8%，$M(1)$ 从 34.2% 提升至 80.6%，$M(n)$ 从 35.5% 提升至 56.3%。

## D. Real-World Experiments / 真实世界实验

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The four multi-stage Franka Panda tasks require prior spatial state, event order, or target identity: Find Blue Block, Line Swap, Triangle Swap, and Press Twice (Fig. 5). For every task, $\pi_{0.5}$ [35], Fast-WAM [21], LingBot-VA [7], and DiM-WAM train on the same 15–25 demonstrations and are evaluated in 10 full-task trials. Stage success ratio (SSR) is completed stages divided by all evaluated stages; full-task success rate (SR) is the fraction of trials completing the task. Table III reports counts and percentage averages.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 四项多阶段 Franka Panda 任务要求利用先前空间状态、事件顺序或目标身份：Find Blue Block、Line Swap、Triangle Swap 和 Press Twice（Fig. 5）。对每项任务，$\pi_{0.5}$ [35]、Fast-WAM [21]、LingBot-VA [7] 和 DiM-WAM 都使用同一组 15–25 个演示训练，并进行 10 次完整任务试验。阶段成功率（SSR）是已完成阶段数除以所有评估阶段数；完整任务成功率（SR）是完成该任务的试验比例。Table III 报告计数及百分比平均值。

### Fig. 5. 真实世界任务

![Fig. 5](WorldModel/DIM-WAM%20World-Action%20Modeling%20with%20Diverse%20Historical%20Event%20Memory/assets/fig5.png)

**Caption:** Real-world tasks, listed in the order used in Table III.
**Caption[CN]:** 真实世界任务，排列顺序与 Table III 一致。

### Table III. 真实世界 Franka Panda 结果

![Table III](WorldModel/DIM-WAM%20World-Action%20Modeling%20with%20Diverse%20Historical%20Event%20Memory/assets/table3.png)

| Method | Find Blue Block SSR/SR | Line Swap SSR/SR | Triangle Swap SSR/SR | Press Twice SSR/SR | Avg. SSR | Avg. SR |
|---|---|---|---|---|---:|---:|
| $\pi_{0.5}$ | 0/40, 0/10 | 3/60, 0/10 | 0/60, 0/10 | 0/30, 0/10 | 1.3 | 0.0 |
| Fast-WAM | 0/40, 0/10 | 0/60, 0/10 | 0/60, 0/10 | 0/30, 0/10 | 0.0 | 0.0 |
| LingBot-VA | 21/40, 1/10 | 47/60, 6/10 | 31/60, 4/10 | 30/30, 10/10 | 70.6 | 52.5 |
| DiM-WAM (ours) | 39/40, 9/10 | 55/60, 9/10 | 51/60, 8/10 | 30/30, 10/10 | 93.5 | 90.0 |

**Caption:** Real-world Franka Panda results. Task entries are success counts over total attempts. SSR denominators are 40 for Find Blue Block, 60 for each swap task, and 30 for Press Twice; all SR denominators are 10. Average values are percentages.
**Caption[CN]:** 真实世界 Franka Panda 结果。任务项为成功次数/总尝试次数。Find Blue Block 的 SSR 分母为 40，每个交换任务为 60，Press Twice 为 30；所有 SR 分母均为 10。平均值为百分比。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> DiM-WAM raises average SSR from 70.6% to 93.5% and average SR from 52.5% to 90.0%. The largest SR gains occur for Find Blue Block (+80.0 points, 10.0% to 90.0%) and Triangle Swap (+40.0 points, 40.0% to 80.0%), which require cross-stage identity or spatial memory. $\pi_{0.5}$ and Fast-WAM have no full-task successes. Qualitative inspection finds their shared failure mode: task-progress confusion under visually similar local observations, where using an action belonging to the wrong stage fails the task.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> DiM-WAM 将平均 SSR 从 70.6% 提升至 93.5%，平均 SR 从 52.5% 提升至 90.0%。最大的 SR 增益出现在需要跨阶段身份或空间记忆的 Find Blue Block（+80.0 点，10.0%→90.0%）和 Triangle Swap（+40.0 点，40.0%→80.0%）。$\pi_{0.5}$ 与 Fast-WAM 没有完整任务成功。定性检查发现两者共有失败模式：在视觉上相似的局部观测下混淆任务进度，选择属于错误阶段的动作会导致任务失败。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Press Twice is included for completeness but has a ceiling effect: the local window covers approximately 85% of each demonstration, and both LingBot-VA and DiM-WAM attain 100% full-task success. The authors therefore do not interpret this task as evidence of a memory-specific advantage. With 10 trials per task, the real-world results are point estimates.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Press Twice 为完整性而纳入，但具有天花板效应：局部窗口覆盖每条演示约 85%，LingBot-VA 与 DiM-WAM 均达到 100% 完整任务成功。因此作者不将该任务解释为记忆特定优势的证据。每任务仅有 10 次试验，真实世界结果是点估计。

## E. Ablation Studies / 消融研究

### Table IV. 记忆结构和进度监督的消融

![Table IV](WorldModel/DIM-WAM%20World-Action%20Modeling%20with%20Diverse%20Historical%20Event%20Memory/assets/table4.png)

| Variant | Swap T | Swap Blocks | Avg. |
|---|---:|---:|---:|
| $1\times32$ memory | 71.0 | 80.0 | 75.5 |
| $4\times8$ memory | 88.0 | 92.0 | 90.0 |
| $8\times12$ memory | 97.0 | 96.0 | 96.5 |
| $8\times12$ w/o prog head | 92.0 | 89.0 | 90.5 |

**Caption:** Ablation study on memory structure and progress supervision. Values are success rates in percent.
**Caption[CN]:** 关于记忆结构与进度监督的消融研究。数值为百分比成功率。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Table IV ablates bank structure and progress supervision on Swap T and Swap Blocks. At fixed total capacity 32, replacing one bank with four improves average success from 75.5% to 90.0%, supporting multi-bank structure. Increasing to $8\times12$ further raises the average to 96.5%, although this changes both bank number and capacity. Removing the progress head from $8\times12$ reduces the average to 90.5%.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Table IV 在 Swap T 和 Swap Blocks 上消融了记忆库结构和进度监督。在总容量固定为 32 时，将一个库换成四个库可使平均成功率从 75.5% 升至 90.0%，支持多库结构的益处。增至 $8\times12$ 后平均值进一步升至 96.5%，但该比较同时改变了记忆库数量和总容量。从 $8\times12$ 中移除进度头会将平均值降至 90.5%。

## F. Cross-Bank Behavior Analysis / 跨记忆库行为分析

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Fig. 6 qualitatively illustrates retained events and event-token distributions in one successful `put_back_block` episode. The visualization is consistent with, but does not by itself establish, complementary cross-bank behavior. In this episode, banks retain different event positions, retained mass often concentrates near transitions, and PCA shows distinct but overlapping bank distributions; these observations do not establish a general trend.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Fig. 6 定性展示一个成功 `put_back_block` 回合中的保留事件和事件 token 分布。该可视化与互补的跨库行为一致，但本身并不能确立这种行为。在该回合中，不同库保留不同事件位置，保留质量常集中于转变附近，PCA 显示不同但重叠的记忆库分布；这些观测不能证明一般性趋势。

### Fig. 6. 单个成功回合中的跨库行为

![Fig. 6](WorldModel/DIM-WAM%20World-Action%20Modeling%20with%20Diverse%20Historical%20Event%20Memory/assets/fig6.png)

**Caption:** Cross-bank behavior in one successful episode: (a) retained memory events over task progress and (b) PCA of event tokens by bank.
**Caption[CN]:** 单个成功回合中的跨库行为：(a) 随任务进度变化的保留记忆事件，(b) 按记忆库划分的事件 token 主成分分析（PCA）。

# V. Conclusion / 结论

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> DiM-WAM is a memory-augmented WAM with DHEM for long-horizon robot manipulation. It reaches a 90.0% average full-task success rate across four real-world memory-dependent tasks.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> DiM-WAM 是用于长时程机器人操作、配备 DHEM 的记忆增强 WAM。在四项依赖记忆的真实世界任务上，它达到 90.0% 的平均完整任务成功率。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Limitations and future work. DHEM is evaluated primarily on memory-dependent manipulation tasks, so effectiveness across broader task distributions, robot embodiments, and observation settings remains to be established. Although ablations support multi-bank organization and progress supervision, they do not independently isolate every component of memory maintenance. Progress supervision uses a coarse trajectory-position proxy rather than semantic task states, which may be less reliable when stage durations vary substantially. The qualitative analysis provides only episode-level evidence of differentiated retention and does not establish stable semantic specialization across banks, tasks, or episodes. Future work will investigate adaptive memory mechanisms, richer progress representations, and broader real-world evaluations.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 局限与未来工作。DHEM 主要在依赖记忆的操作任务上评估，其在更广任务分布、机器人形态和观测设置中的有效性仍待确立。尽管消融支持多库组织与进度监督，但并未独立隔离记忆维护策略的每个组成部分。进度监督使用粗粒度轨迹位置代理，而非语义任务状态；当阶段时长差异很大时，该代理可能不够可靠。定性分析仅提供按回合区分保留的证据，未能确立跨记忆库、任务或回合的稳定语义专化。未来将研究自适应记忆机制、更丰富的进度表征和更广泛的真实世界评估。

# References / 参考文献

1. A. Brohan et al., “RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control,” in *Proceedings of the 7th Conference on Robot Learning*, ser. Proceedings of Machine Learning Research, vol. 229. PMLR, 2023, pp. 2165–2183. 中文：RT-2：将网络知识迁移至机器人控制的视觉—语言—动作模型。
2. M. J. Kim et al., “OpenVLA: An Open-Source Vision-Language-Action Model,” in *Proceedings of the 8th Conference on Robot Learning*, 2024. 中文：OpenVLA：开源视觉—语言—动作模型。
3. K. Black et al., “$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control,” in *Proceedings of Robotics: Science and Systems*, 2025. 中文：$\pi_0$：通用机器人控制的视觉—语言—动作流模型。
4. NVIDIA et al., “GR00T N1: An Open Foundation Model for Generalist Humanoid Robots,” *arXiv preprint* arXiv:2503.14734, 2025. 中文：GR00T N1：通用人形机器人的开放基础模型。
5. P. Li et al., “BridgeVLA: Input-Output Alignment for Efficient 3D Manipulation Learning with Vision-Language Models,” in *Advances in Neural Information Processing Systems*, 2025. 中文：BridgeVLA：面向高效三维操作学习的视觉语言模型输入输出对齐。
6. C.-L. Cheang et al., “GR-2: A Generative Video-Language-Action Model with Web-Scale Knowledge for Robot Manipulation,” *arXiv preprint* arXiv:2410.06158, 2024. 中文：GR-2：用于机器人操作、具有网络规模知识的生成式视频—语言—动作模型。
7. L. Li et al., “Causal World Modeling for Robot Control,” *arXiv preprint* arXiv:2601.21998, 2026. 中文：用于机器人控制的因果世界建模。
8. S. Ye et al., “World Action Models are Zero-Shot Policies,” *arXiv preprint* arXiv:2602.15922, 2026. 中文：世界—动作模型是零样本策略。
9. H. Fang et al., “SAM2Act: Integrating Visual Foundation Model with A Memory Architecture for Robotic Manipulation,” in *International Conference on Machine Learning*, ser. Proceedings of Machine Learning Research, vol. 267, 2025. 中文：SAM2Act：将视觉基础模型与机器人操作记忆架构结合。
10. H. Shi et al., “MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation,” in *International Conference on Learning Representations*, 2026. 中文：MemoryVLA：机器人操作视觉—语言—动作模型中的感知—认知记忆。
11. M. Torne et al., “MEM: Multi-Scale Embodied Memory for Vision Language Action Models,” *arXiv preprint* arXiv:2603.03596, 2026. 中文：MEM：视觉语言动作模型的多尺度具身记忆。
12. H. Li et al., “ReMem-VLA: Empowering Vision-Language-Action Model with Memory via Dual-Level Recurrent Queries,” *arXiv preprint* arXiv:2603.12942, 2026. 中文：ReMem-VLA：通过双层循环查询以记忆增强视觉—语言—动作模型。
13. B. E. Sherman, N. B. Turk-Browne, and E. V. Goldfarb, “Multiple Memory Subsystems: Reconsidering Memory in the Mind and Brain,” *Perspectives on Psychological Science*, vol. 19, no. 1, pp. 103–125, 2024. 中文：多记忆子系统：重新思考心智和大脑中的记忆。
14. T. Chen et al., “RMBench: Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design,” *arXiv preprint* arXiv:2603.01229, 2026. 中文：RMBench：具有策略设计洞见的记忆依赖机器人操作基准。
15. Y. Du et al., “Learning Universal Policies via Text-Guided Video Generation,” in *Advances in Neural Information Processing Systems*, vol. 36, 2023. 中文：通过文本引导视频生成学习通用策略。
16. S. Zhou, Y. Du, J. Chen, Y. Li, D.-Y. Yeung, and C. Gan, “RoboDreamer: Learning Compositional World Models for Robot Imagination,” in *International Conference on Machine Learning*, ser. Proceedings of Machine Learning Research, vol. 235, 2024. 中文：RoboDreamer：为机器人想象学习组合式世界模型。
17. H. Bharadhwaj et al., “Gen2Act: Human Video Generation in Novel Scenarios Enables Generalizable Robot Manipulation,” *arXiv preprint* arXiv:2409.16283, 2024. 中文：Gen2Act：新场景中的人类视频生成支持可泛化机器人操作。
18. M. J. Kim et al., “Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning,” *arXiv preprint* arXiv:2601.16163, 2026. 中文：Cosmos Policy：为视觉运动控制与规划微调视频模型。
19. T. Ma et al., “DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control,” *arXiv preprint* arXiv:2603.10448, 2026. 中文：DiT4DiT：为可泛化机器人控制联合建模视频动力学和动作。
20. Y. Su et al., “World Guidance: World Modeling in Condition Space for Action Generation,” *arXiv preprint* arXiv:2602.22010, 2026. 中文：World Guidance：在条件空间进行世界建模以生成动作。
21. T. Yuan, Z. Dong, Y. Liu, and H. Zhao, “Fast-WAM: Do World Action Models Need Test-Time Future Imagination?” *arXiv preprint* arXiv:2603.16666, 2026. 中文：Fast-WAM：世界—动作模型是否需要测试时未来想象？
22. A. Ye et al., “GigaWorld-Policy: An Efficient Action-Centered World-Action Model,” *arXiv preprint* arXiv:2603.17240, 2026. 中文：GigaWorld-Policy：高效的动作中心世界—动作模型。
23. G. Yang et al., “EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies,” *arXiv preprint* arXiv:2606.20092, 2026. 中文：EventVLA：面向长时程视觉—语言—动作策略的事件驱动视觉证据记忆。
24. H. Shi et al., “MemoryVLA++: Temporal Modeling via Memory and Imagination in Vision-Language-Action Models,” *arXiv preprint* arXiv:2606.09827, 2026. 中文：MemoryVLA++：视觉—语言—动作模型中经由记忆与想象的时间建模。
25. Y. Oshima, S. Taniguchi, M. Suzuki, and Y. Matsuo, “SSM Meets Video Diffusion Models: Efficient Long-Term Video Generation with Structured State Spaces,” in *ICLR Workshop*, 2024. 中文：SSM 遇见视频扩散模型：利用结构化状态空间的高效长视频生成。
26. R. Po et al., “Long-Context State-Space Video World Models,” *arXiv preprint* arXiv:2505.20171, 2025. 中文：长上下文状态空间视频世界模型。
27. J. Chen et al., “SANA-Video: Efficient Video Generation with Block Linear Diffusion Transformer,” in *International Conference on Learning Representations*, 2026. 中文：SANA-Video：采用块线性扩散 Transformer 的高效视频生成。
28. S. Yu et al., “MALT Diffusion: Memory-Augmented Latent Transformers for Any-Length Video Generation,” in *CVPR Workshop on AI for Content Creation*, 2025. 中文：MALT Diffusion：用于任意长度视频生成的记忆增强潜变量 Transformer。
29. Y. Yu et al., “VideoSSM: Autoregressive Long Video Generation with Hybrid State-Space Memory,” *arXiv preprint* arXiv:2512.04519, 2025. 中文：VideoSSM：采用混合状态空间记忆的自回归长视频生成。
30. Z. Zhao, Y. Lu, Z. Liu, J. Song, J. Deng, and I. Patras, “Relax Forcing: Relaxed KV-Memory for Consistent Long Video Generation,” *arXiv preprint* arXiv:2603.21366, 2026. 中文：Relax Forcing：用于一致长视频生成的松弛 KV 记忆。
31. S. Ji, X. Chen, S. Yang, X. Tao, P. Wan, and H. Zhao, “MemFlow: Flowing Adaptive Memory for Consistent and Efficient Long Video Narratives,” *arXiv preprint* arXiv:2512.14699, 2025. 中文：MemFlow：用于一致且高效长视频叙事的流动自适应记忆。
32. J. Zhou et al., “VideoMemory: Toward Consistent Video Generation via Memory Integration,” *arXiv preprint* arXiv:2601.03655, 2026. 中文：VideoMemory：通过记忆整合迈向一致视频生成。
33. W. Dou, H. Li, J. Cui, L. Zhou, J. Wang, and S. Zhu, “SlotMemory: Object-Centric KV Memory for Streaming Long-Video Generation,” *arXiv preprint* arXiv:2605.31033, 2026. 中文：SlotMemory：面向流式长视频生成的对象中心 KV 记忆。
34. J. Su, Y. Lu, S. Pan, A. Murtadha, B. Wen, and Y. Liu, “RoFormer: Enhanced Transformer with Rotary Position Embedding,” *arXiv preprint* arXiv:2104.09864, 2021. 中文：RoFormer：带旋转位置嵌入的增强 Transformer。
35. Physical Intelligence et al., “$\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization,” *arXiv preprint* arXiv:2504.16054, 2025. 中文：$\pi_{0.5}$：具有开放世界泛化能力的视觉—语言—动作模型。
36. C. Chi et al., “Diffusion Policy: Visuomotor Policy Learning via Action Diffusion,” in *Proceedings of Robotics: Science and Systems*, 2023. 中文：Diffusion Policy：通过动作扩散进行视觉运动策略学习。
37. T. Z. Zhao, V. Kumar, S. Levine, and C. Finn, “Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware,” in *Proceedings of Robotics: Science and Systems*, 2023. 中文：用低成本硬件学习细粒度双臂操作。
38. J. Zheng et al., “X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model,” *arXiv preprint* arXiv:2510.10274, 2025. 中文：X-VLA：作为可扩展跨具身视觉—语言—动作模型的软提示 Transformer。

# 术语表 / Terminology Ledger

| Canonical term | 中文统一译法 | First-use definition / 说明 |
|---|---|---|
| World Action Model (WAM) | 世界—动作模型 | 联合预测未来视觉状态和动作的模型 |
| Vision-Language-Action (VLA) | 视觉—语言—动作 | 从视觉和语言条件预测机器人动作的模型 |
| Diverse Historical Event Memory (DHEM) | 多样化历史事件记忆 | DiM-WAM 使用的多记忆库长期记忆模块 |
| memory bank | 记忆库 | 有界事件槽位的并行集合；不预设语义角色 |
| event token | 事件 token | 由观测特征导出的持久记忆单元 |
| accumulated mass | 累积质量 | 合并事件时用于加权 token 和时间戳的量 |
| novelty-aware retention | 新颖性感知保留 | 根据候选与已有事件冗余决定保留/丢弃 |
| RoPE | 旋转位置嵌入（RoPE） | 对可读记忆序列注入相对槽位位置 |
| stage success ratio (SSR) | 阶段成功率 | 已完成阶段数除以被评估阶段总数 |
| full-task success rate (SR) | 完整任务成功率 | 完成完整任务的试验比例 |

# 阅读提示 / Critical reading notes

- 训练匹配、可归因的主比较是 LingBot-VA 对 DiM-WAM；其他 RMBench 数值被作者明确定位为上下文参照。
- `put_back_block` 的协议审计发现腕部视角可能泄漏初始状态；作者据此报告调整后的协议，但未能排除其他任务的残余泄漏。
- 多库可视化仅为单回合定性证据；作者在结论中明确不将其视为稳定语义专化的证明。
