---
title: "RMBench: Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design"
authors: "Tianxing Chen et al."
source_pdf: "/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/3LV8CCM8/Chen 等 - 2026 - RMBench Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design.pdf"
source_type: pdf-text
pages: 16
arxiv: "2603.01229v3"
website: "https://RMBench.github.io"
code: "https://github.com/robotwin-Platform/rmbench"
---

# RMBench：具备记忆依赖的机器人操作基准，以及对策略设计的洞见

## 阅读索引

- pp. 1–2：摘要、引言与相关工作
- pp. 3–4：RMBench、任务记忆复杂度（TMC）与任务设计
- pp. 4–6：Mem-0 的规划、执行与终止分类器
- pp. 6–9：仿真/真实实验、消融与结论
- pp. 9–11：References（完整 38 条）
- pp. 12–16：Appendix A–C（任务说明、训练细节、失败分析）

## Abstract（p. 1）

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Robotic manipulation policies have made rapid progress in recent years, yet most existing approaches give limited consideration to memory capabilities. Consequently, they struggle to solve tasks that require reasoning over historical observations and maintaining task-relevant information over time, which are common requirements in real-world manipulation scenarios. Although several memory-aware policies have been proposed, systematic evaluation of memory-dependent manipulation remains underexplored, and the relationship between architectural design choices and memory performance is still not well understood.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 近年来，机器人操作策略取得了快速进展；但大多数现有方法对记忆能力考虑有限。因此，它们难以解决那些需要基于历史观测推理、并长期维护任务相关信息的任务，而这正是真实世界操作场景中的常见要求。尽管已有若干记忆感知策略被提出，记忆依赖型操作的系统评估仍不充分，架构设计选择与记忆性能之间的关系也尚未得到充分理解。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> To address this gap, we introduce RMBench, a simulation benchmark comprising 9 manipulation tasks that span multiple levels of memory complexity, enabling systematic evaluation of policy memory capabilities. We further propose Mem-0, a modular manipulation policy with explicit memory components designed to support controlled ablation studies. Through extensive simulation and real-world experiments, we identify memory-related limitations in existing policies and provide empirical insights into how architectural design choices influence memory performance.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 为弥补这一缺口，作者提出 RMBench：一个包含 9 项操作任务的仿真基准，覆盖多个记忆复杂度层级，可系统评估策略的记忆能力。作者还提出 Mem-0，一种带有显式记忆组件、可支持受控消融研究的模块化操作策略。通过广泛的仿真和真实世界实验，论文识别出现有策略的记忆相关局限，并就架构设计选择如何影响记忆性能给出实证洞见。

# 1. Introduction（pp. 1–2）

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Recent progress in robotic manipulation has demonstrated strong capabilities across a wide range of tasks. Modern policies such as Pi0.6 and RDT2 achieve impressive performance in flexible object manipulation and fine-grained skills, including complex activities like coffee making. Nevertheless, most existing robotic policies are primarily designed for short-horizon tasks and fine-grained manipulation. These approaches typically rely on a fixed-length window of recent observations, implicitly assuming that the underlying decision process is approximately Markovian.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 机器人操作的最新进展已在广泛任务上展现出很强能力。Pi0.6、RDT2 等现代策略在柔性物体操作、精细技能乃至咖啡制作等复杂活动中取得了出色表现。然而，大多数既有机器人策略主要面向短时程任务和精细操作；它们通常依赖固定长度的近期观测窗口，隐含地假定底层决策过程近似为马尔可夫过程。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In contrast, memory-dependent tasks are ubiquitous in real-world robotic applications. Such tasks are inherently non-Markovian, as past observations and actions may influence future decisions over extended temporal horizons. Examples include remembering the location of previously placed objects or reasoning over multiple attempts after forgetting a password. These tasks are both challenging and practically important, as they require robots to retain, retrieve, and utilize information beyond short-term sensory inputs.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 相比之下，记忆依赖型任务在真实机器人应用中无处不在。这类任务本质上是非马尔可夫的：过去的观测和动作可能跨越很长的时间范围影响未来决策。例如，记住先前放置物体的位置，或在忘记密码后针对多次尝试进行推理。这些任务既困难又有实践价值，因为机器人必须保留、检索和利用超出短期感知输入的信息。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Motivated by this challenge, several recent works have begun to explore memory-aware robotic policies. Approaches such as MemoryVLA, MemER, CronusVLA, and SAM2Act incorporate explicit memory mechanisms to address long-horizon and memory-dependent decision making. Despite these efforts, the field currently lacks a systematically designed experimental platform for evaluating and analyzing robotic policies under long-term memory requirements. In particular, there is limited understanding of the underlying mechanisms that make memory strategies effective for robotic manipulation.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 受此挑战驱动，近期工作开始探索记忆感知机器人策略。MemoryVLA、MemER、CronusVLA 与 SAM2Act 等方法均引入显式记忆机制，以处理长时程和记忆依赖的决策。尽管如此，该领域目前仍缺少一个经系统设计、可在长期记忆需求下评估和分析机器人策略的实验平台；尤其是，人们对何种底层机制使记忆策略在机器人操作中有效仍知之有限。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Existing benchmarks only partially bridge this gap. MemoryBench comprises seven single-arm manipulation tasks that involve memory, yet only three can be reliably reproduced in simulation and the benchmark provides limited guidance on principled task design. MIKASA introduces 32 memory-related manipulation tasks, but its formulation is largely tailored to reinforcement learning rather than general imitation learning. LIBERO-Long offers ten long-horizon tasks, though these tasks do not explicitly demand memory since all task-relevant information remains observable throughout execution.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 既有基准只能部分弥合这一缺口。MemoryBench 包含七项涉及记忆的单臂操作任务，但只有三项能在仿真中稳定复现，且其对原则化任务设计的指导有限。MIKASA 提出 32 项记忆相关操作任务，但其表述主要为强化学习而非一般模仿学习量身定制。LIBERO-Long 提供十项长时程任务，但由于所有任务相关信息在执行期间始终可观测，它们并不显式要求记忆。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> To address these limitations, we first introduce Task Memory Complexity, a principled metric for characterizing memory requirements in robotic manipulation tasks. This metric provides a systematic way to classify memory-dependent tasks and serves as a guideline for task design. Based on this formulation, we propose RMBench, a robotic manipulation benchmark built on RoboTwin 2.0. RMBench consists of 9 dual-arm manipulation tasks spanning different levels of task memory complexity, enabling large-scale and controlled studies of memory retention and utilization in robotic manipulation.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 为解决这些局限，论文首先引入任务记忆复杂度（Task Memory Complexity，TMC），这是刻画机器人操作任务记忆需求的原则化度量。该度量提供了分类记忆依赖任务的系统方法，并可作为任务设计指南。在此表述之上，作者构建了基于 RoboTwin 2.0 的机器人操作基准 RMBench。RMBench 含 9 项双臂操作任务，跨越不同 TMC 层级，从而支持大规模、受控地研究机器人操作中的记忆保留与利用。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Furthermore, we propose Mem-0, a novel memory-oriented robotic policy designed with modular components that can be easily replaced or reconfigured. Mem-0 adopts a dual-system architecture with a task-phase classifier that explicitly distinguishes different stages of a task, allowing structured memory usage across long horizons. Through systematic ablation studies of Mem-0, we analyze which design components are critical for effective memory in robotic manipulation and derive insights for future policy design.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 此外，论文提出新的面向记忆的机器人策略 Mem-0，其模块化组件可方便替换或重配置。Mem-0 采用带任务阶段分类器的双系统架构，显式区分任务的不同阶段，使长时程中的记忆使用具备结构性。借助对 Mem-0 的系统消融，作者分析了哪些设计组件对机器人操作中的有效记忆至关重要，并由此导出对未来策略设计的启示。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Our main contributions are: (i) Task Memory Complexity and RMBench, a nine-task simulation benchmark organized around that metric; (ii) Mem-0, a memory-oriented policy with a task-phase classifier and dual-system architecture for flexible memory use; and (iii) comprehensive evaluation of representative state-of-the-art policies and detailed Mem-0 ablations, revealing mechanisms most beneficial to memory in robotic manipulation.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 论文的主要贡献为：（i）提出任务记忆复杂度以及围绕该度量组织、含九项任务的仿真基准 RMBench；（ii）提出 Mem-0，一种带任务阶段分类器、采用双系统架构以灵活使用记忆的面向记忆策略；（iii）全面评估代表性 SOTA 策略并细致消融 Mem-0，揭示了最有利于机器人操作记忆能力的机制。

# 2. Related Work（p. 2）

## 2.1. Robotic Manipulation Benchmarks

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Physics-based simulators underpin modern robotic manipulation research, and numerous simulation benchmarks have been proposed in recent years. RoboTwin, RoboCasa, ManiSkill3, AutoBio, UniVTAC, DexGarmentLab, BEHAVIOR-1K, and SIMPLER provide diverse manipulation tasks, yet most scenarios emphasize short-horizon interactions or can be solved without relying on historical observations. MemoryBench includes a limited number of memory-dependent tasks but suffers from poor reproducibility and lacks clear task-design principles. MIKASA is primarily tailored to reinforcement learning; LIBERO-Long and RoboCerebra feature long-horizon tasks whose relevant information remains observable. In contrast, RMBench explicitly stratifies manipulation-task memory requirements, enabling systematic analysis across task difficulty levels.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 基于物理的模拟器支撑着现代机器人操作研究，近年来已提出诸多仿真基准。RoboTwin、RoboCasa、ManiSkill3、AutoBio、UniVTAC、DexGarmentLab、BEHAVIOR-1K 和 SIMPLER 提供了多样操作任务，但多数场景强调短时程交互，或不依赖历史观测即可解决。MemoryBench 的记忆依赖任务数量有限、可复现性不足，且缺乏清晰的任务设计原则；MIKASA 主要面向强化学习；LIBERO-Long 和 RoboCerebra 虽具长时程任务，但相关信息仍保持可观测。相比之下，RMBench 显式分层操作任务的记忆需求，从而支持跨难度级别的系统分析。

## 2.2. Robotic Manipulation Policies

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Recent advances in generative models and imitation learning have produced a wide range of robotic manipulation policies that achieve strong performance on individual tasks. Inspired by visual foundation models, many approaches use Vision-Language-Action (VLA) formulations, pretraining policies on large robot datasets for improved generalization; examples include Pi0.5, Pi0.6, RDT2, and X-VLA, as well as future-observation-prediction methods such as Motus, CogACT, and CronusVLA.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 生成模型和模仿学习的进展催生出大量在单项任务上表现优异的机器人操作策略。受视觉基础模型启发，许多方法采用视觉—语言—动作（VLA）范式，在大规模机器人数据集上预训练策略以提升泛化性，例如 Pi0.5、Pi0.6、RDT2、X-VLA，以及采用未来观测预测的 Motus、CogACT、CronusVLA。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Despite these advances, most existing policies rely on fixed-length observation histories, limiting selective retention of task-relevant information over long horizons. This limitation motivates memory-aware approaches including MemoryVLA, MemER, and SAM2Act. Building on this line of work, we propose Mem-0 as a modular memory-enabled policy intended to facilitate systematic ablation and analysis of memory components and architectural choices.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 尽管存在这些进展，多数既有策略仍依赖固定长度的观测历史，这限制了它们跨长时程选择性保留任务相关信息的能力。这一局限推动了 MemoryVLA、MemER、SAM2Act 等记忆感知方法。论文沿此脉络提出 Mem-0：一个模块化、具备记忆能力的策略，旨在促进对记忆组件和架构选择的系统性消融与分析。

# 3. RMBench（pp. 2–4）

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This section introduces Task Memory Complexity, a principled criterion for characterizing memory requirements in robotic manipulation tasks and guiding benchmark design. Based on it, RMBench is a simulation benchmark of nine manipulation tasks with varying memory demands, designed for controlled evaluation across levels of task memory complexity.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本节介绍任务记忆复杂度：一种刻画机器人操作任务记忆需求并指导基准设计的原则化准则。RMBench 以此为基础，是一个由九项记忆需求不同的操作任务构成的仿真基准，旨在支持跨 TMC 层级的受控评估。

### Fig. 1. RMBench 的九项记忆依赖任务

![Fig. 1](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/fig1.png)

**Caption:** Figure 1. RMBench Tasks. We illustrate the nine memory-dependent tasks in RMBench along with their key execution steps. Tasks detailed description are shown in Appendix. A.

**Caption[CN]:** 图 1. RMBench 任务。图中展示 RMBench 的九项记忆依赖任务及其关键执行步骤。任务的详细说明见附录 A。

## 3.1. Task Memory Complexity (TMC)

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Robotic manipulation often operates under partial observability, where the current observation alone may be insufficient to determine task progress or the correct next action without access to past information. Such partial observability may arise from occlusions, delayed effects, or state aliasing. The required past information need not be a contiguous sequence of recent observations, but can be a small set of task-relevant observations at arbitrary timesteps. Existing benchmarks commonly assess memory through particular policy architectures, but lack a task-centric criterion for how much task-relevant information must be retained. TMC measures the minimal amount of past information required for optimal decision-making.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 机器人操作常在部分可观测条件下运行：没有过去信息时，仅凭当前观测可能不足以判断任务进展或正确的下一动作。这种部分可观测性可能来自遮挡、延迟效应或状态混叠。所需的过去信息未必是连续的近期观测序列，也可能是一小组发生在任意时间步、与任务相关的观测。既有基准常通过特定策略架构考察记忆，却缺少以任务为中心、刻画必须保留多少任务相关信息的准则。TMC 衡量最优决策所需的最小过去信息量。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Setup. We model a manipulation task as a partially observable Markov decision process (POMDP) with latent state $s_t \in \mathcal{S}$, observation $o_t \in \mathcal{O}$, and action $a_t \in \mathcal{A}$. Let the full interaction history up to time $t$ be:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 设定。作者将操作任务建模为部分可观测马尔可夫决策过程（POMDP），其中潜在状态为 $s_t \in \mathcal{S}$，观测为 $o_t \in \mathcal{O}$，动作为 $a_t \in \mathcal{A}$。截至时间 $t$ 的完整交互历史定义为：

$$
h_t=(o_{1:t},a_{1:t-1}). \tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Rather than assuming access to the full history, we consider a memory state that summarizes task-relevant information from past observations. Let $M_t$ denote a memory representation constructed from $h_t$, and let $M_t^{(k)}$ denote a memory state encoding information from at most $k$ task-relevant past observations.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 作者不假定系统可访问完整历史，而是考虑一个汇总过去观测中任务相关信息的记忆状态。令 $M_t$ 表示由 $h_t$ 构建的记忆表征，$M_t^{(k)}$ 表示至多编码 $k$ 个任务相关过去观测信息的记忆状态。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Definition. Task Memory Complexity is the smallest integer $m\geq0$ for which an optimal policy $\pi^*$ exists whose action at time $t$ depends only on $M_t^{(m)}$:

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 定义。任务记忆复杂度是满足如下条件的最小整数 $m\geq0$：存在一个最优策略 $\pi^*$，其在时间 $t$ 的动作仅依赖 $M_t^{(m)}$：

$$
\exists\,\pi^*\ \mathrm{s.t.}\ \pi^*(a_t\mid h_t)=\pi^*(a_t\mid M_t^{(m)}),\quad\forall t. \tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Task Annotation. Tasks are annotated as $M(0)$, $M(1)$, or more generally $M(n)$, where the index indicates how many task-relevant past observations must be retained to solve the task optimally. $M(0)$ is memory-free: the current observation uniquely determines progress and the optimal action. $M(1)$ requires one task-relevant past observation to disambiguate the current state. More generally, $M(n)$ requires retaining $n$ such observations and captures non-local, multi-step temporal dependencies.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 任务标注。任务按 $M(0)$、$M(1)$ 或更一般的 $M(n)$ 标注；下标表示要最优解决任务必须保留的任务相关过去观测数量。$M(0)$ 是无记忆任务：当前观测唯一确定进展和最优动作。$M(1)$ 要求保留一个任务相关的过去观测以消除当前状态歧义。更一般地，$M(n)$ 需保留 $n$ 个此类观测，刻画非局部、多步时间依赖。

## 3.2. RMBench System Design

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> RMBench is developed within the RoboTwin 2.0 system framework. It is built on the SAPIEN simulation engine and supports automated data synthesis and integrated policy evaluation in a unified pipeline. This enables scalable data generation and consistent, reproducible benchmarking. Fine-grained language annotations align with every action-observation pair, assigning explicit linguistic descriptions to low-level interactions and state transitions and supplying structured, dense supervision for high-level reasoning or memory modules.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> RMBench 在 RoboTwin 2.0 系统框架内开发，构建于 SAPIEN 仿真引擎之上，并在统一流水线中支持自动数据合成和集成式策略评估。这使可扩展数据生成以及一致、可复现的基准测试成为可能。细粒度语言标注与每个动作—观测对对齐，为低层交互和状态转换赋予显式语言描述，向高层推理或记忆模块提供结构化、稠密的监督信号。

## 3.3. RMBench Benchmark Tasks

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Based on TMC, we design nine memory-dependent manipulation tasks, divided into five $M(1)$ tasks and four $M(n)$ tasks. Figure 1 gives representative key frames, and Appendix A gives detailed specifications. The $M(1)$ tasks are Observe and Pick Up, Rearrange Blocks, Put Back Block, Swap Blocks, and Swap T. They require one past observation or a fixed limited number of historical frames; success depends on dynamically attending to task-relevant information at different stages.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 基于 TMC，作者设计了九项记忆依赖型操作任务，分为五项 $M(1)$ 任务与四项 $M(n)$ 任务。图 1 给出代表性关键帧，附录 A 给出详细规格。$M(1)$ 任务包括 Observe and Pick Up、Rearrange Blocks、Put Back Block、Swap Blocks 和 Swap T；它们需保留一个过去观测或固定且有限数量的历史帧，成功取决于在任务不同阶段动态关注任务相关信息。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The $M(n)$ tasks are Blocks Ranking Try, Press Button, Cover Blocks, and Battery Try. They require repeated active exploration, trial-and-error interactions, or repeated execution for a task-specific number of attempts, often guided by external feedback. Thus they demand strong long-term memory retention and effective retrieval to accumulate and use historical information over extended horizons.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> $M(n)$ 任务包括 Blocks Ranking Try、Press Button、Cover Blocks 和 Battery Try。它们要求重复的主动探索、试错交互，或按任务特定次数重复执行，且通常由外部反馈引导。因此，这些任务要求强大的长期记忆保留与有效检索，以跨扩展时程累积和利用历史信息。

# 4. Mem-0 Policy（pp. 4–6）

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Mem-0 is a modular memory-oriented policy for systematic analysis of memory mechanisms. As shown in Fig. 2, it comprises a Planning Module that performs subtask-level reasoning from key memory, an Execution Module that executes subtasks using sliding-window and anchor memories, and a Subtask End Classifier connecting them for closed-loop planning and execution. This modularity supports fine-grained analysis of individual memory components.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Mem-0 是用于系统分析记忆机制的模块化、面向记忆的策略。如图 2 所示，它包括：基于关键记忆进行子任务级推理的规划模块；利用滑动窗口记忆和锚点记忆执行子任务的执行模块；以及连接二者、实现闭环规划与执行的子任务终止分类器。该模块化设计支持对各记忆组件进行细粒度分析。

### Fig. 2. Mem-0 流水线

![Fig. 2](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/fig2.png)

**Caption:** Figure 2. Mem-0 Pipeline. Mem-0 comprises a Planning Module and an Execution Module linked by a Subtask End Classifier. The Planning Module generates high-level subtasks from task instructions, observations, and key-frame memory, while the Execution Module produces low-level actions using the current observation, the subtask, and fused anchor and sliding memories in a diffusion-based policy. Upon subtask completion, a key frame is stored to enable iterative planning and execution until task completion.

**Caption[CN]:** 图 2. Mem-0 流水线。Mem-0 包含由子任务终止分类器连接的规划模块和执行模块。规划模块根据任务指令、观测和关键帧记忆生成高层子任务；执行模块在基于扩散的策略中利用当前观测、子任务及融合后的锚点/滑动记忆产生低层动作。子任务完成后会保存一个关键帧，使规划和执行能够迭代至任务完成。

## 4.1. Planning Module

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In long-horizon manipulation, end-to-end VLA models are prone to error accumulation and trajectory drift. Subtask decomposition alleviates this but is insufficient in memory-dependent $M(n)$ tasks, where inferring the correct subtask can require reasoning over multiple completed subtasks, for example tracking the number of button presses. Mem-0 therefore introduces a key-memory-window module in the Planning Module that aggregates completed subtasks for memory-aware subtask reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在长时程操作中，端到端 VLA 模型容易在推理期间产生误差累积和轨迹漂移。子任务分解可缓解该问题，但在记忆依赖的 $M(n)$ 任务中仍不充分：正确的子任务推断可能需要基于多个已完成子任务推理，例如追踪按钮按压次数。因此 Mem-0 在规划模块中引入关键记忆窗口，聚合已完成子任务以支持记忆感知的子任务推理。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> At planning step $t$, a vision-language model receives the initial observation $o_0$, task goal $g$, and memory state $M_{t-1}$, then predicts the next subtask:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在规划步 $t$，视觉语言模型接收初始观测 $o_0$、任务目标 $g$ 和记忆状态 $M_{t-1}$，随后预测下一个子任务：

$$
s_t=V_{\mathrm{plan}}(o_0,g,M_{t-1}). \tag{3}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Here $o_0\in\mathbb{R}^{H\times W\times3}$ is the initial RGB observation and $g\in\mathcal{T}$ is the global instruction. The finished-task memory, or key-memory window, aggregates all previously completed subtasks:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 其中，$o_0\in\mathbb{R}^{H\times W\times3}$ 为回合开始时的初始 RGB 观测，$g\in\mathcal{T}$ 为全局任务指令。已完成任务记忆（即关键记忆窗口）聚合此前所有完成的子任务：

$$
M_{t-1}=\{(s_i,o_i^{\mathrm{end}})\}_{i=1}^{t-1}. \tag{4}
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> In this definition, $s_i\in\mathcal{T}$ is the textual description of the $i$-th subtask and $o_i^{\mathrm{end}}\in\mathbb{R}^{H\times W\times3}$ is its termination RGB observation. Conditioning on $M_{t-1}$ lets the VLM reason explicitly over executed subtasks and visual outcomes, beyond single-frame planning. Unlike methods planning at every frame with $O(T)$ calls, this module plans only at classifier-detected termination; with $N\ll T$ subtasks it uses $O(N)$ planning calls, reducing overhead and allowing high-frequency execution within a subtask.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 其中 $s_i\in\mathcal{T}$ 是第 $i$ 个子任务的文本描述，$o_i^{\mathrm{end}}\in\mathbb{R}^{H\times W\times3}$ 是其终止时的 RGB 观测。以 $M_{t-1}$ 为条件，VLM 可显式推理已经执行的子任务及其视觉结果，超越单帧规划。不同于每帧规划、需 $O(T)$ 次调用的方法，本模块只在分类器检测到终止时规划；若长任务有 $N\ll T$ 个子任务，则仅需 $O(N)$ 次规划调用，减少开销且使子任务内的高频执行成为可能。

## 4.2. Execution Module

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Some tasks are not suited to explicit subtask decomposition. In $M(1)$ tasks such as Swap T, a target T-object orientation cannot be reliably specified in language, while over-fine decomposition increases annotation work and planning latency. The Execution Module therefore maintains persistent anchor memory together with short-term sliding memory, allowing it to solve $M(1)$ tasks without further decomposition.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 某些任务并不适合显式子任务分解。在 Swap T 等 $M(1)$ 任务中，T 形物体的目标放置朝向不能通过语言可靠指定；过细的分解还会增加标注工作与规划延迟。因此，执行模块同时维持持久锚点记忆与短期滑动记忆，从而无需进一步分解即可处理 $M(1)$ 任务。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> A VLM $V_{\mathrm{exec}}(\cdot)$ encodes current RGB observation $o_t$ and subtask instruction $s_t$ into image and text token embeddings:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 视觉语言模型 $V_{\mathrm{exec}}(\cdot)$ 将当前 RGB 观测 $o_t$ 与子任务指令 $s_t$ 编码为图像和文本 token 嵌入：

$$
(Z_t^{\mathrm{img}},Z_t^{\mathrm{text}})=V_{\mathrm{exec}}(o_t,s_t). \tag{5}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Mean pooling produces compact representations $z_t^{\mathrm{img}}=\mathrm{MeanPool}(Z_t^{\mathrm{img}})$ and $z_t^{\mathrm{text}}=\mathrm{MeanPool}(Z_t^{\mathrm{text}})$. The image latent attends to anchor memory $A$ and sliding-memory window $S_t$ through cross-attention:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 均值池化得到紧凑表征 $z_t^{\mathrm{img}}=\mathrm{MeanPool}(Z_t^{\mathrm{img}})$ 和 $z_t^{\mathrm{text}}=\mathrm{MeanPool}(Z_t^{\mathrm{text}})$。图像潜变量经交叉注意力关注锚点记忆 $A$ 和滑动记忆窗口 $S_t$：

$$
\tilde z_t^l=\mathrm{CrossAttn}(z_t^{\mathrm{img}},M_t^l)+z_t^{\mathrm{img}},\quad l\in\{\mathrm{anchor},\mathrm{slide}\}, \tag{6}
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Here $M_t^{\mathrm{anchor}}=A$ and $M_t^{\mathrm{slide}}=S_t$. The two fused tokens and text token give $c_t=[\tilde z_t^{\mathrm{anchor}};\tilde z_t^{\mathrm{slide}};z_t^{\mathrm{text}}]$. After attention, the image latent is appended to sliding memory:

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 其中 $M_t^{\mathrm{anchor}}=A$、$M_t^{\mathrm{slide}}=S_t$。两个融合 token 与文本 token 共同构成 $c_t=[\tilde z_t^{\mathrm{anchor}};\tilde z_t^{\mathrm{slide}};z_t^{\mathrm{text}}]$。注意力计算后，将图像潜变量追加进滑动记忆：

$$
S_{t+1}=\mathrm{Trunc}_K(S_t\cup\{z_t^{\mathrm{img}}\}). \tag{7}
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> $\mathrm{Trunc}_K$ keeps the most recent $K$ elements. At a subtask start, $z_0^{\mathrm{img}}$ is stored as fixed anchor memory $A=\{z_0^{\mathrm{img}}\}$; at termination both buffers reset, $A\leftarrow\varnothing,S_t\leftarrow\varnothing$. For action generation, a DiT with fixed horizon $H=30$ predicts a denoised action sequence from a noisy sequence, state, and conditioning:

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> $\mathrm{Trunc}_K$ 保留最近的 $K$ 个元素。子任务开始时，$z_0^{\mathrm{img}}$ 被存储为固定锚点记忆 $A=\{z_0^{\mathrm{img}}\}$；终止时两个缓冲区重置，即 $A\leftarrow\varnothing,S_t\leftarrow\varnothing$。在动作生成中，固定动作时程为 $H=30$ 的 DiT 根据带噪动作序列、状态和条件生成去噪动作序列：

$$
\hat a_{t:t+H-1}=\mathrm{DiT}(a_{\epsilon,t:t+H-1},x_t,c_t). \tag{8}
$$

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> $a_{\epsilon,t:t+H-1}\in\mathbb{R}^{H\times d_a}$ is obtained by Gaussian-noise perturbation of a ground-truth action sequence, and $\hat a_{t:t+H-1}$ is the model’s denoised prediction. A prefix $\hat a_{t:t+\Delta-1}$, $1\leq\Delta\leq H$, is executed before the next replanning step.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> $a_{\epsilon,t:t+H-1}\in\mathbb{R}^{H\times d_a}$ 是由高斯噪声扰动真实动作序列得到的，$\hat a_{t:t+H-1}$ 是模型对应的去噪预测。预测序列的前缀 $\hat a_{t:t+\Delta-1}$（$1\leq\Delta\leq H$）会在下一次重规划前作为控制指令执行。

## 4.3. Subtask End Classifier

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> To enable closed-loop interaction, Mem-0 uses a lightweight multilayer perceptron operating on $c_t$. It outputs a binary signal $C_{\mathrm{end}}(c_t)\in\{0,1\}$ indicating whether the current subtask is ongoing or terminated at time $t$. To avoid transient-noise premature termination, a subtask completes only if termination is predicted for $L=8$ consecutive timesteps:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 为实现闭环交互，Mem-0 使用一个作用于 $c_t$ 的轻量多层感知器。它输出二元信号 $C_{\mathrm{end}}(c_t)\in\{0,1\}$，表示当前子任务在时间 $t$ 是继续还是终止。为避免瞬时噪声导致的过早终止，仅当连续 $L=8$ 个时间步预测为终止时，子任务才算完成：

$$
\sum_{i=t-L+1}^{t}C_{\mathrm{end}}(c_i)=L. \tag{9}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> When this condition holds, the final observation $o_t^{\mathrm{end}}$ and subtask description $s_t$ are passed to Planning to trigger the next subtask-level reasoning round. This establishes a closed loop between high-level planning and low-level execution for coordinated, iterative inference and execution.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 满足该条件后，最终观测 $o_t^{\mathrm{end}}$ 与子任务描述 $s_t$ 被传递给规划模块，触发下一轮子任务级推理。这就在高层规划与低层执行间建立了闭环，以实现协调、迭代的推理和执行。

# 5. Experiment（pp. 6–9）

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We design experiments to: evaluate existing policies and Mem-0 across RMBench difficulty levels; ablate Mem-0 to analyze the effects of module designs on memory-intensive manipulation; and conduct real-world experiments to assess effectiveness and generalization beyond simulation. In addition to SAPIEN, RMBench is also implemented on NVIDIA Isaac Lab - Arena.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 作者设计实验以：（1）评估现有策略与 Mem-0 跨 RMBench 难度层级的性能；（2）消融 Mem-0，以分析模块设计对记忆密集型操作的影响；（3）开展真实世界实验，评估其在仿真外的有效性和泛化性。除 SAPIEN 外，RMBench 也在 NVIDIA Isaac Lab - Arena 上实现。

## 5.1. Evaluation of Policies on RMBench

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We benchmark non-pretrained methods, pretrained methods, and the memory-centric Mem-0. DP and ACT are non-pretrained baselines; Pi0.5 and X-VLA are pretrained approaches. Under both $M(1)$ and $M(n)$ settings, every model is trained with 50 expert demonstrations and evaluated over 100 rollout episodes.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 作者对非预训练方法、预训练方法以及记忆中心的 Mem-0 进行基准测试。DP 和 ACT 是非预训练基线；Pi0.5 和 X-VLA 是预训练方法。在 $M(1)$ 和 $M(n)$ 两种设置下，每个模型均使用 50 条专家演示训练，并在 100 个 rollout 回合上评估。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For $M(1)$ tasks, Mem-0 does not decompose subtasks, so results primarily reflect the Execution Module. For $M(n)$ tasks, decomposition occurs at key decisions and results reflect the joint Planning–Execution system. All baselines train without decomposition; Table 1 reports all success rates.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 对 $M(1)$ 任务，Mem-0 不进行子任务分解，因此结果主要反映执行模块。对 $M(n)$ 任务，系统在关键决策点分解子任务，结果反映规划—执行系统的联合表现。所有基线均在不分解子任务的条件下训练；表 1 报告完整成功率。

### Table 1. RMBench benchmark results

![Table 1](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/table1.png)

**Caption:** Table 1. RMBench benchmark results. RMBench includes nine manipulation tasks across the $M(1)$ and $M(n)$ levels of Task Memory Complexity. We report success rates for five policies, each trained with 50 synthesized demonstrations and evaluated over 100 rollouts. (Bold: best; Underlined: second-best; Green: relative improvement over the second-best).

**Caption[CN]:** 表 1. RMBench 基准结果。RMBench 包含覆盖任务记忆复杂度 $M(1)$ 和 $M(n)$ 层级的九项操作任务。表中报告五种策略的成功率；每种策略均以 50 条合成演示训练、在 100 次 rollout 上评估。（粗体：最优；下划线：次优；绿色：相对次优的提升。）

| Tasks | TMC | DP | ACT | Pi0.5 | X-VLA | Mem-0 (ours) |
|---|---|---:|---:|---:|---:|---:|
| Observe and Pick Up | $M(1)$ | 1% | 1% | 9% | 9% | 4% |
| Rearrange Blocks | $M(1)$ | 0% | 29% | 13% | 13% | 89% |
| Put Back Block | $M(1)$ | 0% | 0% | 11% | 18% | 90% |
| Swap Blocks | $M(1)$ | 11% | 2% | 24% | 16% | 67% |
| Swap T | $M(1)$ | 20% | 2% | 15% | 3% | 14% |
| Average | $M(1)$ | 6.4% | 6.8% | 14.4% | 11.8% | 52.8% (+38.4%) |
| Battery Try | $M(n)$ | 10% | 19% | 16% | 26% | 28% |
| Blocks Ranking Try | $M(n)$ | 10% | 0% | 6% | 1% | 18% |
| Cover Blocks | $M(n)$ | 0% | 0% | 0% | 2% | 68% |
| Press Button | $M(n)$ | 0% | 0% | 0% | 0% | 0% |
| Average | $M(n)$ | 5% | 4.8% | 5.5% | 7.3% | 28.5% (+21.2%) |
| **Total Average** | / | 5.8% | 5.9% | 10.4% | 9.8% | 42.0% (+31.6%) |

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Both non-pretrained and pretrained baselines consistently underperform on memory-dependent tasks. Most are designed under a Markovian assumption in which the next action depends only on the current observation; on RMBench’s non-Markovian tasks, without task-relevant past information they cannot infer correct actions and performance substantially degrades. Figure 3 gives representative failures.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 非预训练和预训练基线在记忆依赖任务上都持续表现不佳。大多数模型基于马尔可夫假设设计，即下一动作仅依赖当前观测；在 RMBench 的非马尔可夫任务上，若没有任务相关的过去信息，它们无法推断正确动作，性能显著下降。图 3 给出代表性失败。

### Fig. 3. 基线典型错误的可视化

![Fig. 3](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/fig3.png)

**Caption:** Figure 3. Visualization of Baseline Typical Error. Because the baseline predicts the next action solely from the current observation, it struggles to perform reliably on non-Markovian tasks that require persistent memory over time.

**Caption[CN]:** 图 3. 基线典型错误的可视化。基线仅根据当前观测预测下一动作，因此难以在需要持续时间记忆的非马尔可夫任务中可靠执行。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> In contrast, Mem-0 substantially improves most tasks, showing the effectiveness of explicit memory mechanisms. Relative to baselines, Mem-0 improves average success rates by 38.4% on $M(1)$ tasks and 21.2% on $M(n)$ tasks, underscoring the importance of memory modules for RMBench manipulation.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 相比之下，Mem-0 在绝大多数任务上显著提升，表明显式记忆机制有效。相较基线，Mem-0 在 $M(1)$ 任务上的平均成功率提高 38.4%，在 $M(n)$ 任务上提高 21.2%，强调了记忆模块对 RMBench 操作的重要性。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Mem-0 nevertheless remains limited on semantically demanding Observe and Pick Up, where large-scale-pretrained models retain an advantage; on fine-grained Swap T, placement accuracy is limited; and in Press Button, small presses make reliable termination difficult, so the classifier can cause repeated presses or missed contacts and zero success. More visualization and analysis are in Appendix C and supplementary material, while the overall trend supports explicit memory modeling.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 但 Mem-0 仍受限于语义要求很高的 Observe and Pick Up（大规模预训练模型仍有优势）；在精细的 Swap T 中其放置精度有限；在 Press Button 中，微小按压使可靠终止检测困难，分类器可能导致重复按压或漏接触，成功率为零。更多可视化分析见附录 C 和补充材料；总体趋势仍支持显式记忆建模。

## 5.2. Analysis on Memory-Related Module

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> To understand effective memory-module design, the authors ablate: (1) w/o Anchor, removing anchor-memory fusion in Execution; (2) w/o Sliding, removing historical sliding-memory fusion; (3) w/o Key, removing Planning’s key-memory window so inference uses only one frame; and (4) GT Classifier, removing the learned classifier and using simulator ground-truth termination.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 为理解有效的记忆模块设计，作者进行四种消融：（1）w/o Anchor：移除执行模块的锚点记忆融合；（2）w/o Sliding：移除历史滑动记忆融合；（3）w/o Key：移除规划模块的关键记忆窗口，使推断只依赖单帧；（4）GT Classifier：移除学习得到的分类器，改用仿真器真实终止信号。

### Table 2. Ablation studies

![Table 2](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/table2.png)

**Caption:** Table 2. Ablation Studies. (Bold: the best results; Underlined: the second-best results).

**Caption[CN]:** 表 2. 消融研究。（粗体：最佳结果；下划线：第二佳结果。）

| $M(1)$ Tasks | Observe and Pick Up | Rearrange Blocks | Put Back Block | Swap Blocks | Swap T | Average |
|---|---:|---:|---:|---:|---:|---:|
| Vanilla (ours) | 4% | 89% | 90% | 67% | 14% | 52.8% |
| w/o Anchor | 4% | 73% | 35% | 15% | 7% | 26.8% |
| w/o Sliding | 3% | 62% | 78% | 39% | 20% | 40.4% |

| $M(n)$ Tasks | Battery Try | Blocks Ranking Try | Cover Blocks | Press Button | Average |
|---|---:|---:|---:|---:|---:|
| Vanilla (ours) | 28% | 18% | 68% | 0% | 28.5% |
| w/o Key | 13% | 1% | 5% | 0% | 4.8% |
| w/o Anchor | 14% | 0% | 92% | 1% | 26.8% |
| w/o Sliding | 17% | 0% | 84% | 0% | 25.3% |
| GT Classifier | 30% | 45% | 92% | 14% | 45.3% |

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Since Mem-0 does not decompose $M(1)$ tasks, their ablation includes only w/o Anchor and w/o Sliding. Removing anchor memory substantially reduces success on most tasks: relevant information is eventually evicted despite an active sliding window, causing loss of essential cues and errors like those in Fig. 3. Reliable completion thus requires explicitly identifying and retaining task-critical information throughout execution.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 由于 Mem-0 不分解 $M(1)$ 任务，该组仅包含 w/o Anchor 与 w/o Sliding。移除锚点记忆会让多数任务成功率大幅下降：即使滑动窗口仍活跃，相关信息终会被驱逐，造成关键线索丢失和类似图 3 的错误。因此，可靠完成要求在整个执行过程中显式识别并保留任务关键信息。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Sliding Memory primarily captures short-term motion trends. Removing it degrades most tasks even with anchor information; qualitative results show unstable, oscillatory behavior, e.g. an agent cannot tell from one frame whether a button was pressed and makes premature or redundant actions. Interestingly, w/o Sliding outperforms vanilla on Swap T, likely because fixed training motions and sensitivity to T orientation make transient motion cues interfere; this demonstrates that sliding memory can facilitate or interfere and must be coordinated with anchor memory.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 滑动记忆主要捕捉短期运动趋势。即使存在锚点信息，移除它仍会降低多数任务性能；定性结果显示不稳定、振荡行为，例如智能体不能从一帧判断按钮是否已按下，继而过早终止或执行冗余动作。有趣的是，w/o Sliding 在 Swap T 上优于原始模型，可能是因为固定训练运动和对 T 朝向的敏感性使瞬时运动线索形成干扰；这表明滑动记忆既可促进也可干扰，必须与锚点记忆协调。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> With w/o Key, single-frame subtask inference sharply reduces success. For $M(n)$ tasks requiring long-term information for later motion decisions, Planning cannot reliably infer the next subtask from only the current observation. The classifier has two roles: it triggers costly high-level reasoning only as needed, and simplifies tasks through decomposition. Mem-0 plans at about 5–10 Hz, compared with MemER’s 1–2 Hz. GT Classifier performance validates decomposition but shows the current classifier is too simple and transition timing can impair Planning; more refined termination signals are needed.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在 w/o Key 中，单帧子任务推断使成功率显著下降。对于需长期信息指导后续运动决策的 $M(n)$ 任务，规划模块无法仅从当前观测可靠推断下一子任务。分类器有两个作用：只在必要时触发昂贵的高层推理，以及借由分解简化任务。Mem-0 的规划频率约 5–10 Hz，而 MemER 是 1–2 Hz。GT Classifier 的表现验证了分解的价值，但也显示现有分类器过于简单、转换时机可能损害规划；需要更精细的终止信号。

## 5.3. Real World Experiment

### Table 3. Real-world experiment results

![Table 3](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/table3.png)

**Caption:** Table 3. Real-world Experiment results.

**Caption[CN]:** 表 3. 真实世界实验结果。

| Tasks | ACT | Pi0.5 | Mem-0 (ours) |
|---|---:|---:|---:|
| Put Back Block | 0.0% | 10.0% | 17.5% |
| Rearrange Blocks | 0.0% | 7.5% | 37.5% |
| Cover Blocks | 0.0% | 0.0% | 12.5% |
| Average | 0.00% | 5.83% | 22.50% |

### Fig. 4. 真实世界实验任务

![Fig. 4](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/fig4.png)

**Caption:** Figure 4. Real-world Experiment Tasks. The real-world experimental setup is illustrated above.

**Caption[CN]:** 图 4. 真实世界实验任务。图中展示真实世界实验设置。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> To assess real-world Mem-0, the authors evaluate Put Back Blocks, Rearrange Blocks, and Cover Blocks on an X-One dual-arm platform, comparing ACT and Pi0.5. Each task has 100 real-world demonstrations; trained policies are evaluated in 40 rollout trials and success rate is the primary metric.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 为评估真实世界的 Mem-0，作者在 X-One 双臂平台上测试 Put Back Blocks、Rearrange Blocks、Cover Blocks，并与 ACT、Pi0.5 对比。每项任务有 100 条真实世界演示；训练策略在 40 个 rollout 试验中评估，以成功率为主要指标。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Mem-0 outperforms both baselines in real-world experiments. Most failures come from imprecise block manipulation, not high-level planning, likely because diverse human data make low-level skills harder to learn consistently and because Mem-0 lacks dedicated robotics-manipulation pretraining. Better low-level pretraining and more structured real-world collection are future directions.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> Mem-0 在真实世界实验中优于两种基线。大多数失败来自不精确的方块操作而非高层规划，这可能因为多样的人类数据使一致地学习低层技能更加困难，也因为 Mem-0 缺乏专门的机器人操作预训练。更好的低层预训练和更结构化的真实数据采集是未来方向。

# 6. Conclusion（p. 9）

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We present RMBench and Mem-0 to systematically evaluate memory in robotic manipulation, revealing memory limitations in existing policies and the effects of anchor, sliding, and key-memory design choices. This gives preliminary insight into principled integration of memory mechanisms for memory-dependent manipulation. Promising future directions are better memory representation/fusion, more robust subtask-termination criteria, and pretraining to improve semantic understanding and generalization. The authors hope RMBench fosters principled progress toward scalable, memory-aware robotic manipulation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本文提出 RMBench 与 Mem-0，系统评估机器人操作中的记忆能力，揭示现有策略的记忆局限以及锚点、滑动和关键记忆设计选择的影响。这为在记忆依赖操作中以原则化方式整合记忆机制提供初步洞见。有前景的未来方向包括更好的记忆表征/融合、更稳健的子任务终止准则，以及提升语义理解和泛化能力的预训练。作者希望 RMBench 推动可扩展、记忆感知机器人操作的原则性进展。

## Acknowledgements

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We would like to thank Xspark AI for supporting our real-world experiments, and D-Robotics for providing the computing resources. Also thank NVIDIA Isaac Lab - Arena Team for technical support.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 作者感谢 Xspark AI 对真实世界实验的支持、D-Robotics 提供计算资源，并感谢 NVIDIA Isaac Lab - Arena 团队提供技术支持。

## Impact Statement

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This paper presents work whose goal is to advance the field of Machine Learning. There are many potential societal consequences of our work, none which we feel must be specifically highlighted here.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本文工作的目标是推进机器学习领域。该工作可能产生多种潜在社会影响，但作者认为没有任何一项需要在此特别强调。

# References（pp. 9–11；38 entries）

1. Bi, H., Tan, H., Xie, S., Wang, Z., Huang, S., Liu, H., Zhao, R., Feng, Y., Xiang, C., Rong, Y., et al. Motus: A unified latent action world model. arXiv:2512.13030, 2025.  
   中文：Motus：统一的潜在动作世界模型。
2. Chen, B., Wan, W., Chen, T., Guo, X., Xu, C., Qi, Y., Zhang, H., Wu, L., Xu, T., Li, Z., et al. Univtac: A unified simulation platform for visuo-tactile manipulation data generation, learning, and benchmarking. arXiv:2602.10093, 2026.  
   中文：UniVTAC：用于视觉—触觉操作数据生成、学习与基准测试的统一仿真平台。
3. Chen, T., Chen, Z., Chen, B., Cai, Z., Liu, Y., Li, Z., Liang, Q., Lin, X., Ge, Y., Gu, Z., et al. Robotwin 2.0: A scalable data generator and benchmark with strong domain randomization for robust bimanual robotic manipulation. arXiv:2506.18088, 2025a.  
   中文：RobotWin 2.0：具强域随机化、面向鲁棒双臂机器人操作的可扩展数据生成器与基准。
4. Chen, T., Mu, Y., Liang, Z., Chen, Z., Peng, S., Chen, Q., Xu, M., Hu, R., Zhang, H., Li, X., et al. G3Flow: Generative 3D semantic flow for pose-aware and generalizable object manipulation. CVPR, pp. 1735–1744, 2025b.  
   中文：G3Flow：用于姿态感知、可泛化物体操作的生成式三维语义流。
5. Cherepanov, E., Kachaev, N., Kovalev, A. K., and Panov, A. I. Memory, benchmark & robots: A benchmark for solving complex tasks with reinforcement learning. arXiv:2502.10550, 2025.  
   中文：记忆、基准与机器人：用于以强化学习解决复杂任务的基准。
6. Chi, C., Xu, Z., Feng, S., Cousineau, E., Du, Y., Burchfiel, B., Tedrake, R., and Song, S. Diffusion policy: Visuomotor policy learning via action diffusion. IJRR, 44(10–11):1684–1704, 2025.  
   中文：Diffusion Policy：通过动作扩散进行视觉运动策略学习。
7. Fang, H., Grotz, M., Pumacay, W., Wang, Y. R., Fox, D., Krishna, R., and Duan, J. SAM2Act: Integrating visual foundation model with a memory architecture for robotic manipulation. arXiv:2501.18564, 2025.  
   中文：SAM2Act：将视觉基础模型与记忆架构结合用于机器人操作。
8. Han, S., Qiu, B., Liao, Y., Huang, S., Gao, C., Yan, S., and Liu, S. RoboCerebra: A large-scale benchmark for long-horizon robotic manipulation evaluation. arXiv:2506.06677, 2025.  
   中文：RoboCerebra：用于长时程机器人操作评估的大规模基准。
9. Physical Intelligence et al. $\pi^*_ {0.6}$: a VLA that learns from experience, 2025a. URL: https://arxiv.org/abs/2511.14759.  
   中文：$\pi^*_{0.6}$：从经验中学习的 VLA。
10. Physical Intelligence et al. $\pi_{0.5}$: a vision-language-action model with open-world generalization, 2025b. URL: https://arxiv.org/abs/2504.16054.  
    中文：$\pi_{0.5}$：具有开放世界泛化能力的视觉—语言—动作模型。
11. Kwon, W., Li, Z., Zhuang, S., Sheng, Y., Zheng, L., Yu, C. H., Gonzalez, J. E., Zhang, H., and Stoica, I. Efficient memory management for large language model serving with PagedAttention. SOSP, 2023.  
    中文：利用 PagedAttention 进行大语言模型服务的高效内存管理。
12. Lan, Z., Jiang, Y., Wang, R., Xie, X., Zhang, R., Zhu, Y., Li, P., Yang, T., Chen, T., Gao, H., et al. AutoBio: A simulation and benchmark for robotic automation in digital biology laboratory. arXiv:2505.14030, 2025.  
    中文：AutoBio：数字生物实验室机器人自动化仿真与基准。
13. Li, C., Zhang, R., Wong, J., Gokmen, C., Srivastava, S., Martín-Martín, R., Wang, C., Levine, G., Ai, W., Martinez, B., et al. Behavior-1K: A human-centered, embodied AI benchmark with 1,000 everyday activities and realistic simulation. arXiv:2403.09227, 2024a.  
    中文：BEHAVIOR-1K：含 1,000 项日常活动和真实仿真的以人为中心具身 AI 基准。
14. Li, H., Yang, S., Chen, Y., Tian, Y., Yang, X., Chen, X., Wang, H., Wang, T., Zhao, F., Lin, D., et al. CronusVLA: Transferring latent motion across time for multi-frame prediction in manipulation. arXiv:2506.19816, 2025.  
    中文：CronusVLA：跨时间迁移潜在运动以进行操作中的多帧预测。
15. Li, Q., Liang, Y., Wang, Z., Luo, L., Chen, X., Liao, M., Wei, F., Deng, Y., Xu, S., Zhang, Y., et al. CogACT: A foundational VLA model for synergizing cognition and action in robotic manipulation. arXiv:2411.19650, 2024b.  
    中文：CogACT：协同机器人操作中认知与动作的基础 VLA 模型。
16. Li, X., Hsu, K., Gu, J., Pertsch, K., Mees, O., Walke, H. R., Fu, C., Lunawat, I., Sieh, I., Kirmani, S., et al. Evaluating real-world robot manipulation policies in simulation, 2024c. URL: https://arxiv.org/abs/2405.05941.  
    中文：在仿真中评估真实世界机器人操作策略。
17. Liang, Z., Li, Y., Yang, T., Wu, C., Mao, S., Nian, T., Pei, L., Zhou, S., Yang, X., Pang, J., et al. Discrete diffusion VLA: Bringing discrete diffusion to action decoding in vision-language-action policies. arXiv:2508.20072, 2025.  
    中文：离散扩散 VLA：将离散扩散引入 VLA 策略的动作解码。
18. Lin, M., Ding, P., Wang, S., Zhuang, Z., Liu, Y., Tong, X., Song, W., Lyu, S., Huang, S., and Wang, D. HiF-VLA: Hindsight, insight and foresight through motion representation for VLA models. arXiv:2512.09928, 2025.  
    中文：HiF-VLA：通过运动表征为 VLA 提供后见、洞见和前瞻。
19. Liu, B., Zhu, Y., Gao, C., Feng, Y., Liu, Q., Zhu, Y., and Stone, P. LIBERO: Benchmarking knowledge transfer for lifelong robot learning, 2023. URL: https://arxiv.org/abs/2306.03310.  
    中文：LIBERO：为终身机器人学习评测知识迁移。
20. Lu, G., Gao, Z., Chen, T., Dai, W., Wang, Z., Ding, W., and Tang, Y. ManiCM: Real-time 3D diffusion policy via consistency model for robotic manipulation. arXiv:2406.01586, 2024.  
    中文：ManiCM：利用一致性模型实现面向机器人操作的实时三维扩散策略。
21. Mu, Y., Chen, T., Chen, Z., Peng, S., Lan, Z., Gao, Z., Liang, Z., Yu, Q., Zou, Y., Xu, M., et al. RoboTwin: Dual-arm robot benchmark with generative digital twins. CVPR, pp. 27649–27660, 2025.  
    中文：RoboTwin：带生成式数字孪生的双臂机器人基准。
22. Nasiriany, S., Maddukuri, A., Zhang, L., Parikh, A., Lo, A., Joshi, A., Mandlekar, A., and Zhu, Y. RoboCasa: Large-scale simulation of everyday tasks for generalist robots. arXiv:2406.02523, 2024.  
    中文：RoboCasa：通用机器人的大规模日常任务仿真。
23. Shen, W., Liu, Y., Wu, Y., Liang, Z., Gu, S., Wang, D., Nian, T., Xu, L., Qin, Y., Pang, J., et al. Expertise need not monopolize: Action-specialized mixture of experts for vision-language-action learning. arXiv:2510.14300, 2025.  
    中文：专长无需垄断：面向 VLA 学习的动作专门化专家混合。
24. Shi, H., Xie, B., Liu, Y., Sun, L., Liu, F., Wang, T., Zhou, E., Fan, H., Zhang, X., and Huang, G. MemoryVLA: Perceptual-cognitive memory in vision-language-action models for robotic manipulation. arXiv:2508.19236, 2025.  
    中文：MemoryVLA：机器人操作 VLA 模型中的感知—认知记忆。
25. Sridhar, A., Pan, J., Sharma, S., and Finn, C. MemER: Scaling up memory for robot control via experience retrieval. arXiv:2510.20328, 2025.  
    中文：MemER：通过经验检索扩展机器人控制记忆。
26. Su, Y., Zhan, X., Fang, H., Xue, H., Fang, H.-S., Li, Y.-L., Lu, C., and Yang, L. Dense Policy: Bidirectional autoregressive learning of actions. arXiv:2503.13217, 2025.  
    中文：Dense Policy：动作的双向自回归学习。
27. Tao, S., Xiang, F., Shukla, A., Qin, Y., Hinrichsen, X., Yuan, X., Bao, C., Lin, X., Liu, Y., kai Chan, T., et al. ManiSkill3: GPU parallelized robotics simulation and rendering for generalizable embodied AI, 2025. URL: https://arxiv.org/abs/2410.00425.  
    中文：ManiSkill3：面向可泛化具身 AI 的 GPU 并行机器人仿真与渲染。
28. Team, R. RDT2: Enabling zero-shot cross-embodiment generalization by scaling up UMI data, September 2025. URL: https://github.com/thu-ml/RDT2.  
    中文：RDT2：通过扩展 UMI 数据实现零样本跨具身泛化。
29. Wang, Y., Wu, R., Chen, Y., Wang, J., Liang, J., Zhu, Z., Geng, H., Malik, J., Abbeel, P., and Dong, H. DexGarmentLab: Dexterous garment manipulation environment with generalizable policy, 2025. URL: https://arxiv.org/abs/2505.11032.  
    中文：DexGarmentLab：具有可泛化策略的灵巧衣物操作环境。
30. Wen, J., Zhu, Y., Zhu, M., Tang, Z., Li, J., Zhou, Z., Liu, X., Shen, C., Peng, Y., and Feng, F. DiffusionVLA: Scaling robot foundation models via unified diffusion and autoregression. ICML, 2025.  
    中文：DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型。
31. Wen, J., Zhu, M., Zhu, Y., Tang, Z., Li, J., Zhou, Z., Li, C., Liu, X., Peng, Y., Shen, C., and Feng, F. DiffusionVLA: Scaling robot foundation models via unified diffusion and autoregression. arXiv:None, 2024.  
    中文：DiffusionVLA：通过统一扩散与自回归扩展机器人基础模型。
32. Wen, J., Zhu, Y., Li, J., Tang, Z., Shen, C., and Feng, F. DexVLA: Vision-language model with plug-in diffusion expert for general robot control. arXiv:2502.05855, 2025a.  
    中文：DexVLA：用于通用机器人控制、带插件式扩散专家的视觉语言模型。
33. Wen, J., Zhu, Y., Li, J., Zhu, M., Tang, Z., Wu, K., Xu, Z., Liu, N., Cheng, R., Shen, C., et al. TinyVLA: Towards fast, data-efficient vision-language-action models for robotic manipulation. RA-L, 2025b.  
    中文：TinyVLA：迈向快速、数据高效的机器人操作视觉—语言—动作模型。
34. Xiang, F., Qin, Y., Mo, K., Xia, Y., Zhu, H., Liu, F., Liu, M., Jiang, H., Yuan, Y., Wang, H., et al. SAPIEN: A simulated part-based interactive environment. CVPR, pp. 11097–11107, 2020.  
    中文：SAPIEN：模拟的基于部件的交互环境。
35. Ze, Y., Zhang, G., Zhang, K., Hu, C., Wang, M., and Xu, H. 3D Diffusion Policy: Generalizable visuomotor policy learning via simple 3D representations. arXiv:2403.03954, 2024.  
    中文：3D Diffusion Policy：通过简单三维表征实现可泛化视觉运动策略学习。
36. Zhao, T. Z., Kumar, V., Levine, S., and Finn, C. Learning fine-grained bimanual manipulation with low-cost hardware, 2023. URL: https://arxiv.org/abs/2304.13705.  
    中文：利用低成本硬件学习精细双臂操作。
37. Zheng, J., Li, J., Wang, Z., Liu, D., Kang, X., Feng, Y., Zheng, Y., Zou, J., Chen, Y., Zeng, J., et al. X-VLA: Soft-prompted transformer as scalable cross-embodiment vision-language-action model, 2025. URL: https://arxiv.org/abs/2510.10274.  
    中文：X-VLA：作为可扩展跨具身 VLA 模型的软提示 Transformer。
38. Zheng, Y., Zhang, R., Zhang, J., Ye, Y., Luo, Z., Feng, Z., and Ma, Y. LLaMAFactory: Unified efficient fine-tuning of 100+ language models. ACL Demonstrations, Bangkok, 2024. URL: http://arxiv.org/abs/2403.13372.  
    中文：LLaMAFactory：100 余种语言模型的统一高效微调。

# Appendix A. RMBench Tasks Description（p. 12）

### Table 4. Task descriptions of RMBench benchmark

![Table 4](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/table4.png)

**Caption:** Table 4. Task descriptions of RMBench benchmark.

**Caption[CN]:** 表 4. RMBench 基准的任务说明。

| Task | Description | 中文说明 |
|---|---|---|
| Observe and Pick Up | A reference object is placed on a shelf and multiple objects on the table. The robot first observes the reference object while stationary. After it is hidden, the robot must pick up the matching table object. | 货架上有一个参照物，桌上有多个物体。机器人静止观察参照物；其被隐藏后，机器人须从桌面拾取匹配物体。 |
| Rearrange Blocks | Two pads and a button are on the table. One block is between pads and another is on a pad. Move the middle block onto a pad, press the button, then move the other block to the middle. | 桌上有两个垫和一个按钮；一个方块在两垫之间，另一个在其中一垫上。机器人将中间方块移至一个垫上，按按钮，再将另一方块移到中间。 |
| Put Back Block | Four pads surround a center and one block is on a pad. Move it to the center, press the button, then return it to its original pad. | 四个垫围绕中心，方块位于其中一垫。将方块移至中心，按按钮，再放回原来的垫。 |
| Swap Block | Three pads and a button; two blocks occupy different pads. Use the empty pad to swap the two blocks and press the button. | 三个垫和一个按钮，两个方块占据不同垫。利用空垫交换两方块位置，再按按钮。 |
| Swap T | Two differently colored T-shaped blocks. Pick up both and swap their positions and orientations. | 两个不同颜色的 T 形方块。拾起两者并交换其位置和朝向。 |
| Battery Try | Two randomly oriented batteries and a dual-slot holder. Repeatedly try insertion orders and place both with correct orientation until success. | 两节随机朝向电池和双槽电池座。重复尝试不同插入顺序，以正确朝向将两节电池放入，直至成功。 |
| Blocks Ranking Try | Three colored blocks are randomly arranged with a button. Repeatedly try arrangements and press to confirm until the ordering is correct. | 三个不同颜色方块随机摆放，另有按钮。重复尝试不同排列并按按钮确认，直至顺序正确。 |
| Cover Blocks | Three colored blocks (red, green, blue) and three covers. Cover from left to right, uncover in red–green–blue order, then return covers. | 三个彩色方块（红、绿、蓝）和三个盖子。先从左到右盖住，之后按红—绿—蓝顺序揭开，并将盖子归位。 |
| Press Button | Three buttons (left, middle, right) and two single-digit number tiles. Press left according to the left digit, middle according to the right digit, then right to confirm. | 三个按钮（左、中、右）和两个单数字数字牌。按左数字的次数按左按钮，按右数字的次数按中按钮，最后按右按钮确认。 |

# Appendix B. Training Details（pp. 12–13）

## B.1. Planning Module

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In the Planning Module, we fine-tune Qwen3-VL-8B-Instruct with LoRA via LLaMAFactory to enable reasoning over key memories. After fine-tuning, we deploy it with vLLM for efficient loading and inference. Table 5 gives VLM hyperparameters. Training uses 8 NVIDIA A800 GPUs, and a single task takes about half an hour.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在规划模块中，作者经由 LLaMAFactory 使用 LoRA 微调 Qwen3-VL-8B-Instruct，以实现对关键记忆的推理。微调后使用 vLLM 部署，以高效加载和推理。表 5 给出 VLM 超参数。训练使用 8 张 NVIDIA A800 GPU，单项任务训练约半小时。

### Table 5. Hyperparameters for fine-tuning the Mem-0 Planning Module

![Table 5](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/table5.png)

**Caption:** Table 5. Hyperparameters for fine-tuning the Mem-0 Planning Module.

**Caption[CN]:** 表 5. Mem-0 规划模块微调的超参数。

| Configuration | Finetuning Type | LoRA Rank | Batch Size | Learning Rate | Epochs | LR Scheduler | Warmup Ratio | Dtype |
|---|---|---:|---:|---:|---:|---|---:|---|
| Value | LoRA | 8 | 16 | $1.0\times10^{-4}$ | 25 | Cosine | 0.1 | bf16 |

## B.2. Execution Module

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This appendix details the training infrastructure, organization strategy, and hyperparameter configuration for Mem-0’s Execution Module. The module uses single-task training from scratch per task, trained on 8 NVIDIA A800 GPUs with global batch size 448 for 30K iterations; one task takes approximately 18 hours.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本附录说明 Mem-0 执行模块的训练基础设施、训练组织策略与超参数配置。该模块对每项任务采用从头开始的单任务训练；使用 8 张 NVIDIA A800 GPU、全局 batch size 448、训练 30K iterations，单项任务约需 18 小时。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Forward Pass Strategy. For the memory-centric architecture, VLM token generation and DiT action-chunk generation run in parallel within each batch. Sliding- and anchor-memory fusion requires temporal data integrity, so it runs serially to keep all episode frames sequentially aligned. A global structure stores per-episode memory, enabling cross-batch token use.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 前向传播策略。针对以记忆为中心的架构，每个 batch 内的 VLM token 生成和基于 DiT 的动作块生成并行执行。滑动记忆和锚点记忆融合要求数据的时间完整性，因此串行处理以保证一个 episode 的所有帧保持顺序对齐。训练时维护全局数据结构保存每个 episode 的记忆，实现跨 batch token 利用。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Dataloader Implementation. The dataloader is custom-designed for this architecture. Episodes are distributed as evenly as possible over GPUs; each GPU processes assigned episodes with a specific worker number and independently resets its loader. As iterations progress, stochastic distribution temporally desynchronizes frames within a global batch, allowing simultaneous learning from varied timesteps.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Dataloader 实现。dataloader 为该架构专门设计。episode 尽可能均匀分配至各 GPU；每张 GPU 以特定数量 worker 处理所分配 episode，并独立管理 dataloader 重置。随着训练迭代，随机分配会使全局 batch 内的帧在时间上失同步，使模型可同时从跨越不同时间步的数据学习。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Table 6 summarizes training hyperparameters. To balance module-wise learning-rate needs, the authors use grouped learning rates, cosine scheduling with linear warm-up, bfloat16 for VLM and Memory Bank, float32 elsewhere, and 224 × 224 images with frame-independent ColorJitter for mild augmentation.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 表 6 汇总训练超参数。为平衡不同模块的学习率需求，作者采用分组学习率、带线性 warm-up 的余弦调度；VLM 和 Memory Bank 使用 bfloat16，其余模块使用 float32；图像缩放至 224 × 224，并采用帧独立 ColorJitter 进行轻度增强。

### Table 6. Hyperparameters for training the Mem-0 Execution Module

![Table 6](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/table6.png)

**Caption:** Table 6. Hyperparameters for training the Mem-0 Execution Module.

**Caption[CN]:** 表 6. Mem-0 执行模块训练的超参数。

| Configuration | Value | Configuration | Value |
|---|---:|---|---:|
| Batch Size | 448 | LR (Base) | $1.0\times10^{-5}$ |
| Iterations | 30,000 | LR (VLM) | $1.0\times10^{-5}$ |
| Max Grad. Norm | 2.5 | LR (Action Head) | $1.0\times10^{-4}$ |
| LR Scheduler | Cosine | LR (Classifier) | $1.0\times10^{-4}$ |
| Warmup Ratio | 0.05 | Min LR (Base) | $1.0\times10^{-6}$ |
| Optimizer | AdamW | Min LR (VLM) | $1.0\times10^{-6}$ |
| Momentum | $\beta_1,\beta_2=0.9,0.999$ | Min LR (Action Head) | $5.0\times10^{-6}$ |
| Weight Decay | 0.005 | Min LR (Classifier) | $5.0\times10^{-6}$ |
| Image Resize | $224\times224$ | Workers per GPU | 2 |
| Image Aug. | ColorJitter† | † Jitter | $(0.1,0.1,0.1,0)$ |

# Appendix C. Additional Visualizations and Analysis of Failure Cases in Mem-0（pp. 13–16）

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> While Mem-0 substantially improves on the baselines, its design still leaves extensive room for exploration. This section presents representative cases of suboptimal performance to provide insights for future research.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 尽管 Mem-0 相比基线有显著提升，其架构设计仍留有广阔探索空间。本节给出代表性的次优表现案例，旨在为未来研究提供启示。

### Fig. 5. Observe and Pick Up 的失败案例

![Fig. 5](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/fig5.png)

**Caption:** Figure 5. Failure examples of Observe and Pick Up. (Top) Confused by objects with similar colors and shapes. (Middle) Confused by identical object morphologies. (Bottom) General failure to identify the target, resulting in the robot grasping a mean position or unintended position.

**Caption[CN]:** 图 5. Observe and Pick Up 的失败案例。（上）被颜色和形状相近的物体混淆。（中）被形态相同的物体混淆。（下）未能识别目标，导致机器人抓取平均位置或非预期位置。

### Fig. 6. Swap Blocks 的失败案例

![Fig. 6](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/fig6.png)

**Caption:** Figure 6. Failure examples of Swap Blocks. (Top) Premature termination after a single subtask. (Middle) Premature termination after two subtasks. (Bottom) Failure to terminate on time, resulting in the initiation of a redundant subtask.

**Caption[CN]:** 图 6. Swap Blocks 的失败案例。（上）完成一个子任务后过早终止。（中）完成两个子任务后过早终止。（下）未能及时终止，导致启动冗余子任务。

### Fig. 7. Rearrange Blocks 的失败案例

![Fig. 7](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/fig7.png)

**Caption:** Figure 7. Failure examples of Rearrange Blocks. Mem-0 redundantly presses the button, resulting in task failure.

**Caption[CN]:** 图 7. Rearrange Blocks 的失败案例。Mem-0 冗余地按下按钮，导致任务失败。

## C.1. Failures Analysis for $M(1)$ Tasks

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For $M(1)$ tasks, beyond failures in Fig. 3, the authors summarize representative Mem-0 errors. In Observe and Pick Up, Fig. 5 shows failure to identify the target accurately. Fig. 6 shows misjudging termination of a swapping sequence, pressing the confirmation button at inappropriate times. These cases reveal Anchor Memory continuously affects the full task horizon: the model must consistently attend to it and intelligently control its contribution to action prediction. Ablations already show its large gains, particularly on Rearrange Blocks and Put Back Block.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 对于 $M(1)$ 任务，除图 3 所示失败外，作者总结了 Mem-0 的代表性错误。在 Observe and Pick Up 中，图 5 显示模型未能准确识别目标；图 6 显示模型误判交换序列的终止，以不合适的时机按确认按钮。这些案例说明锚点记忆持续影响整个任务时程：模型必须持续注意它，并智能控制其对动作预测的贡献。消融已表明锚点记忆带来显著收益，尤其在 Rearrange Blocks 和 Put Back Block 中。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Figure 7 shows excessive button pressing in Rearrange Blocks, attributed to Sliding Memory limitations. Ablations show a significant degradation without it, and video analysis finds redundant presses markedly increase when it is absent. The current sliding memory produces substantial gains but can be improved. Richer representation-fusion mechanisms could better use both anchor and sliding memory, while more powerful VLM visual processing should improve Observe and Pick Up.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 图 7 显示 Rearrange Blocks 中的过度按按钮，被归因于滑动记忆的局限。消融表明移除它后该任务显著退化，视频分析发现缺失滑动记忆时冗余按压显著增加。当前滑动记忆已带来可观收益，但仍可改进。更丰富的表征融合机制可能更好利用锚点和滑动记忆；更强的 VLM 视觉处理能力应可改善 Observe and Pick Up。

## C.2. Failures Analysis for $M(n)$ Tasks

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For $M(n)$ tasks, Mem-0 improves substantially over baselines but still has considerable room for improvement; the authors identify classifier performance and robustness as the primary challenge.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 对 $M(n)$ 任务，Mem-0 虽较基线有显著改进，仍有很大提升空间；作者认为分类器的性能和鲁棒性是首要挑战。

### Fig. 8. Cover Blocks 的失败案例

![Fig. 8](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/fig8.png)

**Caption:** Figure 8. Failure examples of Cover Blocks. The Classifier fails to accurately detect the completion of the Uncover xxx subtask, thereby preventing a subtask transition. As the instruction remains unchanged, the model is forced to operate under a wrong task context, leading to unintended and erratic behaviors.

**Caption[CN]:** 图 8. Cover Blocks 的失败案例。分类器未能准确检测 Uncover xxx 子任务完成，因此阻止子任务转换。由于指令保持不变，模型被迫在错误任务上下文下操作，导致非预期且不稳定的行为。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In Cover Blocks, the Classifier can fail to perceive ongoing progress accurately and cannot distinguish whether a state is subtask initiation or termination, as illustrated in Fig. 8. In Blocks Ranking Try, button pressing interferes with a hybrid task: the transition between pressing and block swapping is sometimes disrupted. A single execution error causes the whole task to fail, explaining its sensitivity in the ablations.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在 Cover Blocks 中，分类器有时不能准确感知当前任务进展，无法区分某状态是子任务开始还是结束，如图 8 所示。在 Blocks Ranking Try 中，按按钮会干扰混合任务：按压和方块交换之间的转换有时受阻。单次执行错误就会造成整个任务失败，这解释了其在消融中的敏感性。

### Fig. 9. Blocks Ranking Try 的失败案例

![Fig. 9](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/fig9.png)

**Caption:** Figure 9. Failure examples of Blocks Ranking Try. Upon pressing the button, the system is expected to transition to the next subtask to execute the swapping of designated blocks. However, the Classifier fails to trigger this transition promptly, causing the task to stall in the Press button state. This leads to a coordination conflict between the dual arms: the right hand attempts to initiate manipulation while the left hand remains tethered to the button-pressing instruction.

**Caption[CN]:** 图 9. Blocks Ranking Try 的失败案例。按下按钮后，系统应切换至下一子任务以交换指定方块。但分类器未及时触发转换，任务停留在 Press button 状态。这导致双臂协调冲突：右手尝试开始操作，左手仍受按按钮指令约束。

### Fig. 10. Press Button 的失败案例

![Fig. 10](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/fig10.png)

**Caption:** Figure 10. Failure examples of Press Button. (Top) Insufficient presses: the Classifier issues a false positive termination signal even when the button-press is unsuccessful. (Bottom) Excessive presses: the Classifier fails to recognize a successful subtask completion, leading to redundant execution of the same subtask.

**Caption[CN]:** 图 10. Press Button 的失败案例。（上）按压不足：即使按压未成功，分类器仍发出假阳性终止信号。（下）按压过多：分类器未识别子任务已成功完成，导致重复执行同一子任务。

### Fig. 11. Battery Try 的失败案例

![Fig. 11](WorldModel/RMBench%20Memory-Dependent%20Robotic%20Manipulation%20Benchmark%20with%20Insights%20into%20Policy%20Design/assets/fig11.png)

**Caption:** Figure 11. Failure examples of Battery Try. (Top) For the horizontally oriented cylindrical battery, a suboptimal grasp pose prevents a successful lift and causes significant displacement, leading the model into unforeseen observational states. (Bottom) The model fails to commit to a specific manipulation strategy during battery adjustment, resulting in a mean action that leads to improper placement in the slot.

**Caption[CN]:** 图 11. Battery Try 的失败案例。（上）对于水平放置的圆柱电池，次优抓取姿态使其无法成功提起并造成显著位移，使模型进入未预见的观测状态。（下）模型在调整电池时未能确定具体操作策略，产生平均动作，导致电池未能正确放入槽内。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Press Button exposes the intrinsic difficulty of dedicated button pressing. In Mem-0, pressed versus unpressed is visible only through extremely subtle cues, so VLM-backbone visual tokens lack the granularity to encode that information, creating a bottleneck for the downstream Classifier. Figure 10 shows representative failures. In Battery Try, suboptimal precision includes insertion errors and difficulty choosing a grasp strategy from subtle slot cues, shown in Fig. 11.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Press Button 揭示专用按钮按压的内在难度。在 Mem-0 中，已按与未按状态仅通过极细微线索反映在视觉输入中，因而 VLM 主干生成的视觉 token 缺乏编码这些细粒度信息的能力，形成下游分类器的瓶颈。图 10 给出代表性失败。Battery Try 中的次优精度包括插入错误，以及因插槽视觉线索极其微弱而难以选择抓取策略，如图 11 所示。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The authors posit that proprioceptive or tactile feedback could supply critical non-visual information to the Classifier. Since it is the most downstream module, improving upstream VLM-token extraction and Anchor/Sliding fusion is also promising: it could condition the classifier’s input distribution better and increase informational saliency. More interpretable tokens may improve synergy between subtasks, especially in Blocks Ranking Try. The current design is nevertheless validated across $M(n)$ tasks, notably yielding a substantial gain in Cover Blocks, and the analysis is intended to guide future improvements.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 作者认为，本体感觉或触觉反馈可为分类器提供关键的非视觉信息。由于分类器是最下游模块，改进上游 VLM token 提取和锚点/滑动融合也很有前景：它可改善分类器输入的条件分布并提高信息显著性。更可解释的 token 可能改善不同子任务的协同，尤其是在 Blocks Ranking Try 中。当前设计仍已在 $M(n)$ 任务上得到验证，特别是在 Cover Blocks 中取得显著增益；上述分析旨在指导未来改进。

# Terminology Ledger

| Canonical term | 中文译法 | First-use definition / note |
|---|---|---|
| RMBench | RMBench | Memory-Dependent Robotic Manipulation Benchmark |
| Task Memory Complexity (TMC) | 任务记忆复杂度 | 最优决策所需的任务相关过去观测最小量 |
| Mem-0 | Mem-0 | 作者的模块化记忆导向操作策略 |
| Planning Module | 规划模块 | 基于关键记忆进行子任务级推理 |
| Execution Module | 执行模块 | 用锚点与滑动记忆执行低层动作 |
| Anchor Memory | 锚点记忆 | 子任务开始时固定的视觉记忆 |
| Sliding Memory | 滑动记忆 | 保留最近 $K$ 个视觉潜变量的短期窗口 |
| Key Memory | 关键记忆 | 已完成子任务及其终止观测组成的窗口 |
| Subtask End Classifier | 子任务终止分类器 | 对 $c_t$ 输出继续/终止的 MLP |
| Vision-Language-Action (VLA) | 视觉—语言—动作 | 以视觉、语言条件产生动作的模型 |
| Diffusion Transformer (DiT) | 扩散 Transformer | Mem-0 的动作序列生成器 |

## 阅读提示

- TMC 是本文核心的“任务侧”定义：$M(1)$ 与 $M(n)$ 的区分不等同于网络记忆容量，而是最优解决任务所须保留的相关历史观测数量。
- 结合表 2 阅读模块作用：Anchor 对多数 $M(1)$ 任务关键；Key 对 $M(n)$ 的子任务推断关键；GT Classifier 与真实 Classifier 的差距直接定位了终止检测瓶颈。
- 附录 C 将失败定位为三类：语义/目标识别、短期动态状态判断、以及分类器驱动的子任务切换与精细接触问题。
