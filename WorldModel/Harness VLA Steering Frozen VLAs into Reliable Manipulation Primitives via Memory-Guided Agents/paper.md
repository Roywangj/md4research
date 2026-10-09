# Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents

> **Source / 来源**：Yixian Zhang et al., *Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents*, arXiv:2607.08448v3, 15 July 2026. User-supplied PDF, 39 pages.

> **Status / 状态**：PDF 全文源文本保全的双语详细阅读稿草案。每个可提取源页面块均按英文原文后紧邻中文位置标记；由于当前会话的翻译输出容量限制，中文占位明确标记为未完成，绝不将占位误报为完整译文。

## Document map / 文档索引

The source is preserved in PDF page order below; all headings, tables, figures, appendices, prompts, JSON literals, numbers, and references are retained in the source blocks.

下面按 PDF 页面顺序保留源文；所有标题、表格、图、附录、提示词、JSON 字面量、数字和参考文献均保留在源文本块中。

## Figures / 图

Rendered source pages are available as `assets/page-01.jpg` through `assets/page-39.jpg`; page captures are used rather than cropped figures so no figure material is silently removed.


### Source page 1 / 源页面 1


> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Harness VLA: Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents Yixian Zhang1,∗ Huanming Zhang1,∗ Feng Gao2 Xiao Li3 Zhihao Liu4 Chunyang Zhu5 Jiaxing Qiu5 Yuchen Yan5 Jiyuan Liu7 Wenhao Tang1 Zhengru Fang6 Yi Nie1,2 Changxu Wei1 Yu Wang1 Wenbo Ding1,† Chao Yu1,† Tsinghua University 2 Striding AI 3 Purdue University Institute of Automation, Chinese Academy of Sciences 5 Infinigence AI Hong Kong University of Science and Technology 7 Zhongguancun Academy ∗ Equal contribution. † Corresponding author Website: https://harnessvla.github.io/ arXiv:2607.08448v3 [cs.RO] 15 Jul 2026 Figure 1: Harness VLA system overview. Given a task description, RGB-D observations, and robot state, the agentic planner selects structured calls from a fixed primitive library rather than emitting low-level ac- tions directly. The library exposes the frozen VLA as VLA ACT for contact-rich behaviors and uses analytic primitives such as MOVE TO, ROTATE, and SET GRIPPER for perception-conditioned staging, transport, pos- ture adjustment, and release. Task Specific Memory stores successful command traces from reference-seed exploration for few-shot re-grounding, while Global Memory stores reusable success rules and failure mod- els. The right panels summarize gains over the relevant strongest baselines, and the bottom strip illustrates a rollout that alternates sparse VLA invocations with analytic control.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Harness VLA：通过记忆引导智能体将冻结的 VLA 引导为可靠的操作基元。作者为 Yixian Zhang、Huanming Zhang、Feng Gao、Xiao Li、Zhihao Liu、Chunyang Zhu、Jiaxing Qiu、Yuchen Yan、Jiyuan Liu、Wenhao Tang、Zhengru Fang、Yi Nie、Changxu Wei、Yu Wang、Wenbo Ding 和 Chao Yu，单位包括清华大学、Striding AI、普渡大学、中国科学院自动化研究所、Infinigence AI、香港科技大学和中关村学院。* 表示共同贡献，† 表示通讯作者。项目网站为 https://harnessvla.github.io/，论文版本为 arXiv:2607.08448v3（2026 年 7 月 15 日）。

图 1 展示 Harness VLA 系统概览。给定任务描述、RGB-D 观测和机器人状态，智能体规划器从固定基元库中选择结构化调用，而不是直接输出低层动作。该库将冻结 VLA 暴露为用于接触密集行为的 VLA ACT，并使用 MOVE TO、ROTATE 和 SET GRIPPER 等解析基元执行由感知条件化的定位、运输、姿态调整和释放。任务特定记忆保存参考种子探索得到的成功命令轨迹，用于少样本重新落地；全局记忆保存可复用的成功规则和失败模型。右侧面板汇总相对于相关最强基线的增益，底部条带展示了稀疏调用 VLA 与解析控制交替进行的一次 rollout。


### Source page 2 / 源页面 2


> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Abstract Language-conditioned manipulation requires both precise contact-rich control and robust reasoning over language, scenes, and long horizons. End-to-end Vision-Language-Action (VLA) models pro- vide strong local visuomotor skills, but they are trained on in-distribution task trajectories and often degrade under deployment perturbations such as semantic retargeting, goal re-binding, spatial-layout shifts, and unstable local contacts. LLM coding agents provide complementary semantic and composi- tional reasoning, but purely analytic primitives struggle with irregular grasping, constrained placement, and articulated-object interaction. We present Harness VLA, a memory-augmented agentic framework that exposes a frozen VLA as a retryable contact-rich primitive and composes it with a small fixed library of analytic primitives for grounding, staging, transport, navigation, and release. Rather than expanding the skill library, the harness learns the operating range of these fixed primitives from task-specific execu- tion traces, global success rules, and failure models. By lifting semantic re-grounding, non-contact exe- cution, and VLA re-staging to the planner while reserving the frozen VLA for local contact-rich phases, Harness VLA extends pretrained VLAs beyond their original trajectory distribution without fine-tuning. Across perturbed tabletop, household kitchen, and clean-to-randomized bimanual manipulation, Harness VLA improves over the strongest relevant baselines by 38.6 and 25.4 percentage points on LIBERO-Pro and RoboCasa365, respectively, and reaches 58.4% on RoboTwin C2R. 1    Introduction A long-standing goal of robotic manipulation is a system that reliably executes free-form natural-language instructions across changing objects, layouts, and embodiments. Two dominant paradigms approach this goal from opposite directions. End-to-end Vision-Language-Action (VLA) models learn contact-rich vi- suomotor control directly from robot trajectories, while LLM coding agents use language-model reasoning to compose explicit perception-and-control APIs. Each paradigm is powerful, but each assigns the wrong component too much responsibility: monolithic VLAs must absorb language grounding, long-horizon com- position, and low-level control inside a single policy, whereas coding agents must realize physically delicate interactions through hand-designed or agent-generated APIs. Figure 2 visualizes our response: use analytic primitives to traverse deployment perturbations and invoke the VLA only inside local contact-rich regions where its training distribution is informative. End-to-end VLA models have advanced rapidly, from generalist robot policies [1, 2] to flow-matching and action-reasoning architectures [3–6]. Their strength is local, image-conditioned contact: grasping irreg- ular objects, placing with tight tolerances, or actuating fixtures that are brittle for analytic controllers. Their weakness is deployment outside the trajectory distribution on which they were trained. A model trained on in-distribution task trajectories may know how to grasp a milk carton or turn a faucet, yet fail when semantic targets are redirected, goal predicates are re-bound, object layouts shift, or short skills must be composed into longer routines. Under such deployment perturbations, the policy may repeat a familiar training-time behavior even when the instruction or scene binding has changed [2, 4, 7]; a single unstable contact failure can also derail the entire monolithic rollout. LLM coding agents and harnesses provide complementary semantic and compositional reasoning. Systems such as Code as Policies and ProgPrompt synthesize executable programs over curated perception and control APIs [8, 9], and recent multimodal or agentic variants extend this idea with richer perception, tool use, feedback, and persistent execution state [10–13]. More broadly, coding-agent harnesses wrap model outputs in a structured runtime with tool interfaces, memory, validators, execution loops, and feed- back channels, allowing an agent to revise decisions, write successful traces or failure diagnoses back into memory, and orchestrate heterogeneous tools under a common control surface [14–17]. Yet in robot manip- ulation, scaling such systems often still means expanding the primitive or skill library, while purely analytic primitives–deterministic kinematic or model-based controllers such as IK transport, wrist rotation, base mo- tion, gripper opening, and release–remain poorly suited to irregular grasping, constrained placement, and

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **摘要。** 语言条件下的操作既需要精确的接触密集控制，也需要对语言、场景和长时域过程进行稳健推理。端到端视觉-语言-动作（VLA）模型具有很强的局部视觉运动技能，但它们在分布内任务轨迹上训练，遇到部署扰动（例如语义目标重定向、目标重新绑定、空间布局变化和局部接触不稳定）时往往退化。LLM 编码智能体提供互补的语义和组合推理能力，但纯解析基元难以处理不规则抓取、受限放置和关节物体交互。我们提出 Harness VLA，一种记忆增强的智能体框架：它将冻结 VLA 暴露为可重试的接触密集基元，并与一个小型固定解析基元库组合，用于目标落地、定位、运输、导航和释放。该 harness 不扩展技能库，而是从任务特定执行轨迹、全局成功规则和失败模型中学习固定基元的适用范围。通过将语义重新落地、非接触执行和 VLA 重新定位提升到规划器层面，同时只在局部接触密集阶段调用冻结 VLA，Harness VLA 无需微调即可使预训练 VLA 超越原始轨迹分布。在受扰动的桌面操作、家庭厨房操作以及从干净环境到随机化环境的双臂操作中，Harness VLA 相比相关最强基线在 LIBERO-Pro 和 RoboCasa365 上分别提高 38.6 和 25.4 个百分点，并在 RoboTwin C2R 上达到 58.4%。

**1 引言。** 机器人操作长期以来的目标，是构建一个能够在物体、布局和具身形态不断变化时可靠执行自由形式自然语言指令的系统。两种主流范式从相反方向接近这一目标：端到端 VLA 模型直接从机器人轨迹中学习接触密集的视觉运动控制，而 LLM 编码智能体利用语言模型推理来组合显式的感知与控制 API。两种范式都很强，但都把过多责任分配给了不合适的组件：单体 VLA 必须在一个策略中同时吸收语言落地、长时域组合和低层控制；编码智能体则必须通过人工设计或智能体生成的 API 实现物理上细腻的交互。图 2 以可视化方式呈现我们的回应：使用解析基元穿越部署扰动，并只在其训练分布仍然有信息的局部接触密集区域内调用 VLA。

端到端 VLA 模型发展迅速，从通用机器人策略 [1, 2] 发展到 flow matching 和动作推理架构 [3–6]。它们的优势在于局部、由图像条件化的接触：抓取不规则物体、以很小容差进行放置，或驱动解析控制器难以稳定处理的装置。它们的弱点则是超出训练轨迹分布后的部署。一个在分布内任务轨迹上训练的模型可能知道如何抓取牛奶盒或旋转水龙头，但当语义目标被重定向、目标谓词重新绑定、物体布局变化，或多个短技能必须组成更长流程时，就可能失败。在这类部署扰动下，即使指令或场景绑定已经改变，策略仍可能重复训练时熟悉的行为 [2, 4, 7]；一次不稳定的接触失败也可能使整个单体 rollout 失效。

LLM 编码智能体和 harness 提供了互补的语义与组合推理能力。Code as Policies、ProgPrompt 等系统在经过整理的感知和控制 API 上合成可执行程序 [8, 9]；近期多模态或智能体变体又加入了更丰富的感知、工具使用、反馈和持久执行状态 [10–13]。更广泛地说，编码智能体 harness 将模型输出包裹在具有工具接口、记忆、验证器、执行循环和反馈通道的结构化运行时中，使智能体能够修订决策、将成功轨迹或失败诊断写回记忆，并在统一控制面上编排异构工具 [14–17]。然而在机器人操作中，扩展这类系统往往仍意味着扩大基元或技能库；而纯解析基元——例如 IK 运输、腕部旋转、底座运动、夹爪开合和释放等确定性的运动学或模型控制器——仍不适合不规则抓取、受限放置和关节物体操作。


### Source page 3 / 源页面 3


> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> articulated-object manipulation. Harness VLA instantiates this coding-agent harness view for robot manipulation: keep the primitive li- brary fixed and small, and let the agent learn how to orchestrate it. The planner composes analytic primitives for non-contact structure such as target grounding, free-space transport, posture adjustment, mobile staging, re-staging after failed attempts, and release. For contact-rich phases, it invokes a frozen VLA through a sin- gle learned primitive, VLA ACT. This converts the VLA from a monolithic trajectory policy into a reusable contact specialist, extending it to the tasks outside its original trajectory distribution without fine-tuning or deployment-time primitive expansion. The key is not only exposing VLA ACT, but learning when and how Figure 2: Primitive composition extends a frozen VLA beyond its trajectory distribution. Deployment perturbations expand the possible task configurations beyond the in-distribution trajectories covered by the frozen VLA. A direct VLA rollout may attempt to bridge the perturbed space and fail before reaching the target. Harness VLA instead decomposes the task into local contact-rich VLA invocations and analytic primitive control: analytic primitives perceive the current target, re-ground task bindings, and move the robot between VLA-compatible local regions, while VLA ACT is invoked only for contact-rich phases inside those regions. to use it. Harness VLA treats VLA execution as a retryable local attempt: the planner can stage the robot into a favorable local observation, invoke the VLA, inspect the contact outcome, and re-stage if needed. Two memory modules support this process inside the agentic harness [14, 15, 18]: task-specific traces store successful primitive compositions for few-shot re-grounding, while global memory stores reusable success rules and failure models. Rather than adding more skills, the harness teaches the planner the operating range of each fixed primitive: which subproblems should be handled analytically, when VLA ACT is appropriate, and how failed contact attempts should be re-staged. Our core contributions are: • A memory-augmented agentic framework for using a frozen VLA as a primitive. Harness VLA com- poses VLA ACT with fixed analytic primitives, extending a pretrained VLA from local contact-rich control to long-horizon, perturbed manipulation without fine-tuning the VLA or expanding the prim- itive vocabulary at deployment time. • An empirical analysis showing why a small fixed primitive library is sufficient when the planner learns how to use it. Repeated planner-staged invocations can reframe brittle VLA attempts, while analytic primitives solve much of the non-contact structure around each contact-rich phase.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 关节物体操作。Harness VLA 将这种编码智能体 harness 观点实例化到机器人操作中：保持基元库小而固定，让智能体学习如何编排它。规划器使用解析基元处理非接触结构，例如目标落地、自由空间运输、姿态调整、移动定位、失败后的重新定位和释放。在接触密集阶段，规划器通过一个单独的学习型基元 VLA ACT 调用冻结 VLA。这样，VLA 从单体轨迹策略变成了可复用的接触专家；无需微调，也无需在部署时扩充基元词汇，就能处理原始轨迹分布之外的任务。

图 2：基元组合使冻结 VLA 超越其轨迹分布。部署扰动将可能的任务配置扩展到冻结 VLA 所覆盖的分布内轨迹之外。直接进行 VLA rollout 时，策略可能试图跨越整个扰动空间，并在到达目标前失败。Harness VLA 则将任务分解为局部接触密集型 VLA 调用和解析基元控制：解析基元感知当前目标、重新绑定任务，并在 VLA 兼容的局部区域之间移动机器人；VLA ACT 只在这些区域内的接触密集阶段被调用。

关键不仅在于暴露 VLA ACT，还在于学习何时以及如何使用它。Harness VLA 将 VLA 执行视为可重试的局部尝试：规划器可以把机器人定位到有利的局部观测状态，调用 VLA，检查接触结果，并在需要时重新定位。智能体 harness 中的两个记忆模块支持这一过程 [14, 15, 18]：任务特定轨迹保存成功的基元组合，用于少样本重新落地；全局记忆保存可复用的成功规则与失败模型。该 harness 不是增加更多技能，而是让规划器理解每个固定基元的工作范围：哪些子问题应由解析方法处理、何时适合调用 VLA ACT，以及失败的接触尝试应如何重新定位。

本文的核心贡献包括：

- 提出一种将冻结 VLA 用作基元的记忆增强智能体框架。Harness VLA 将 VLA ACT 与固定解析基元组合，使预训练 VLA 从局部接触密集控制扩展到长时域、受扰动的操作，而无需微调 VLA，也无需在部署时扩充基元词汇。
- 通过实证分析说明，当规划器学会使用基元时，一个小型固定基元库已经足够。规划器分阶段重复调用可以重新构造脆弱的 VLA 尝试，而解析基元能够解决每个接触密集阶段周围的大部分非接触结构。


### Source page 4 / 源页面 4


> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> • Strong benchmark results across standard and perturbed tabletop manipulation, household kitchen ma- nipulation, and clean-to-randomized transfer. Harness VLA preserves competitive standard LIBERO performance, improves over the strongest relevant baselines by 38.6 and 25.4 percentage points on LIBERO-Pro and RoboCasa365, respectively, and reaches 58.4% on RoboTwin C2R. 2     The Harness VLA Framework Our agentic framework for language-conditioned manipulation follows the system view in Figure 1. A task description, RGB-D observations, and robot state are passed to an agentic planner, which reasons over a fixed primitive library and retrieves context from Task Specific Memory and Global Memory. The agentic harness (Section 2.2) couples this planner to the simulator through a JSON-serialized primitive interface, drives the turn-based execution loop, and writes successful exploration traces into Task Specific Memory while committing generalized heuristics to Global Memory. The primitive library (Section 2.3) defines the only operations the planner is allowed to invoke: a small set of analytic primitives together with a structurally special VLA primitive that encapsulates a pretrained visuomotor policy for contact-rich interactions. Section 2.1 first formalises the task and the iterative execution loop on which these components are built. 2.1    Problem Formulation and Agentic Execution Loop Task setup. We consider language-conditioned robotic manipulation within an environment E driven by a rigid-body physics engine (e.g., MuJoCo via Robosuite). At each timestep t, the environment exposes a rgb                                                     rgb multimodal observation tuple ot = (It , Itd , qt ) comprising an agent-view RGB image It , a co-aligned metric depth map Itd , and a robot proprioceptive state qt (concatenating the end-effector pose and gripper state). A task is defined by a natural-language description ℓ alongside a binary completion predicate G, exposed solely as a sparse success signal at episode termination. Agentic execution loop. As illustrated by the rollout strip in Figure 1, a task rollout is formulated as an autoregressive, turn-based interaction between a high-level agentic planner Π and the underlying physics engine. Instead of treating the visuomotor policy as a separate hierarchical tier, we unify all low-level control mechanisms—including the frozen pretrained VLA fθ and all deterministic operational-space controllers— into a single, predefined primitive library P. At each execution turn t, the planner Π processes the current multimodal observation ot , the task de- scription ℓ, and the retrieved context from both the Task Specific Memory and Global Memory. Operating as the sole cognitive orchestrator, Π emits a structured JSON invocation for a selected primitive ct ∈ P. The physics engine directly receives this invocation and executes the corresponding physical motions in the simulator until the primitive’s internal post-condition is met. Upon primitive termination, the engine yields the subsequent observation ot+1 and updated robot state qt+1 . This environment-planner loop iterates continuously until the goal predicate G is satisfied or a maximum step budget is exhausted. 2.2    The Harness VLA Architecture Motivated by recent coding agents, which make model decisions executable through harnessed execution- feedback loops [14–16], Harness VLA packages robot manipulation in the same REPL-style form. The harness is the runtime contract between the planner and the environment: it exposes primitive schemas, serializes decisions as JSON commands, executes primitives, refreshes RGB-D and proprioceptive observa- tions, logs traces, retrieves Task Specific Memory and Global Memory, enforces reset and budget policies, and checks progress through the benchmark predicate [17].

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> - 在标准和受扰动桌面操作、家庭厨房操作以及从干净到随机化的迁移上取得强基准结果。Harness VLA 在标准 LIBERO 上保持竞争力，在 LIBERO-Pro 和 RoboCasa365 上分别超过相关最强基线 38.6 和 25.4 个百分点，并在 RoboTwin C2R 上达到 58.4%。

**2 Harness VLA 框架。** 我们的语言条件操作智能体框架遵循图 1 所示的系统视图。任务描述、RGB-D 观测和机器人状态被传递给智能体规划器；规划器在固定基元库上推理，并从任务特定记忆和全局记忆中检索上下文。智能体 harness（第 2.2 节）通过 JSON 序列化的基元接口将规划器连接到模拟器，驱动轮流执行循环，把成功的探索轨迹写入任务特定记忆，并将一般化启发式规则提交到全局记忆。基元库（第 2.3 节）定义了规划器唯一可以调用的操作：少量解析基元，以及一个结构上特殊的 VLA 基元，后者封装了用于接触密集交互的预训练视觉运动策略。第 2.1 节首先形式化任务和这些组件所依赖的迭代执行循环。

**2.1 问题形式化与智能体执行循环。** **任务设置。** 我们考虑由刚体物理引擎（例如通过 Robosuite 使用 MuJoCo）驱动的环境 E 中的语言条件机器人操作。在每个时间步 t，环境提供多模态观测元组 o_t=(I_t^{rgb}, I_t^d, q_t)，其中包括智能体视角的 RGB 图像 I_t^{rgb}、与其对齐的度量深度图 I_t^d，以及机器人本体感知状态 q_t（由末端执行器位姿和夹爪状态拼接而成）。任务由自然语言描述 ℓ 和二值完成谓词 G 定义；后者只在 episode 终止时以稀疏成功信号暴露。

**智能体执行循环。** 如图 1 的 rollout 条带所示，任务 rollout 被形式化为高层智能体规划器 Π 与底层物理引擎之间的自回归、轮流交互。我们不把视觉运动策略视为独立的层级，而是将所有低层控制机制——包括冻结的预训练 VLA f_θ 和所有确定性的操作空间控制器——统一为一个预定义的基元库 P。在每个执行回合 t，规划器 Π 处理当前多模态观测 o_t、任务描述 ℓ，以及从任务特定记忆和全局记忆检索到的上下文。作为唯一的认知编排器，Π 为所选基元 c_t∈P 输出结构化 JSON 调用。物理引擎直接接收该调用，并在模拟器中执行相应的物理运动，直到该基元的内部后置条件满足。基元终止后，引擎返回下一观测 o_{t+1} 和更新后的机器人状态 q_{t+1}。环境—规划器循环持续迭代，直到目标谓词 G 满足或最大步数预算耗尽。

**2.2 Harness VLA 架构。** 受近期编码智能体的启发——这类智能体通过 harness 化的执行—反馈循环使模型决策可执行 [14–16]——Harness VLA 以相同的 REPL 形式封装机器人操作。Harness 是规划器与环境之间的运行时契约：它暴露基元 schema，将决策序列化为 JSON 命令，执行基元，刷新 RGB-D 和本体感知观测，记录轨迹，检索任务特定记忆与全局记忆，执行重置和预算策略，并通过基准谓词检查进度 [17]。


### Source page 5 / 源页面 5


> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Because this harness delegates all fine-grained execution to the primitive library, the agentic planner Π is freed to focus entirely on compositional reasoning. To do so, it relies heavily on the multimodal observation channel: the RGB image supports qualitative scene reasoning (e.g., clutter, semantic identity), while the co-aligned depth map and proprioception supply metric spatial data for precise localization. We structure the agent’s lifecycle within this harness into two distinct phases: an exploratory bootstrap- ping phase and a rigorous deployment evaluation phase. Exploratory Bootstrapping Phase. Operating on a single reference instantiation of a task, the agent autonomously interacts with the environment to discover a working solution. During this phase, the planner Π is uniquely granted access to a RESET primitive and operates under a generous wall-clock budget. Because the primitive vocabulary is fixed, the exploration focuses entirely on iterative composition: discovering the optimized orchestration of the learned VLA primitive and the deterministic analytic primitives. The planner Π repeatedly trials different staging orders, pre-contact poses, invocation timings for VLA ACT, and early- return termination thresholds. It observes the physical effects of each primitive call and corrects course upon failure. Upon successful task completion, the agent systematically abstracts its experience into the two memory modules shown in Figure 1. First, the verified sequence of primitive invocations is serialized into a JSONL format. This file explicitly records the successful step-by-step primitive calls, parameterizing them by re- placing concrete spatial coordinates with symbolic perception queries to make the sequence reusable across different spatial layouts. This parameterized JSONL trace is stored in the Task Specific Memory to serve as a structural prior for subsequent generalization tests. Second, the agent extracts generalized heuristics from the exploration process and commits them to a persistent Global Memory. This shared repository explicitly aggregates success rules, such as optimal prompting strategies that utilize the full task instruction. It con- currently documents critical failure models, including the identification of empty-grasp executions and false success detections. This aggregation ensures the planner avoids repeating historical pitfalls across different tasks. Deployment Evaluation Phase. During formal evaluation on unseen environment variations, including position swaps, instruction redirections, and testing across multiple initial state seeds, the harness imposes a strict execution regime. The RESET primitive is completely disabled, and the operational step budget is significantly shortened. To solve the perturbed tasks, the planner Π retrieves the pre-computed JSONL trace from the Task Specific Memory and grounds it dynamically using the live RGB-D observation. By referencing the success rules and failure models accumulated in the Global Memory, the agent executes the trajectory deterministically. The performance achieved under this strict phase directly constitutes our reported benchmark results, validating the overall effectiveness of the Harness VLA framework. 2.3   Unified Primitive Interface The primitive library P is the only action interface exposed to the planner. Each primitive is invoked by a single JSON object, executes inside the environment until an internal post-condition is reached, and then returns control together with a refreshed observation. Example JSON invocations are shown at the end of this subsection. The planner therefore never emits low-level torques, joint targets, or action chunks directly; it selects a primitive and binds its arguments from language, RGB-D observations, proprioception, and memory. We organize P into two manipulation families. Analytic primitives are deterministic, model-based con- trollers specified from robot kinematics and require no training data. They split into composite primitives, which take a world-frame spatial goal and run an embedded solver to coordinate multiple degrees of free- dom, and atomic primitives, which drive one intrinsic channel such as wrist orientation, gripper state, or base velocity to a parametric set-point. The VLA primitive, VLA ACT, is a learned policy call that maps a prompt and live cameras to action chunks for local contact-rich behavior. The exploratory RESET utility is

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 由于 harness 将所有细粒度执行委托给基元库，智能体规划器 Π 可以完全专注于组合推理。RGB 图像支持定性的场景推理（例如杂乱程度和语义身份），而对齐的深度图和本体感知为精确定位提供度量空间数据。我们将智能体在该 harness 中的生命周期划分为两个阶段：探索式引导阶段和严格的部署评估阶段。

**探索式引导阶段。** 智能体在一个任务的单一参考实例上运行，并自主与环境交互以发现可行解。在此阶段，规划器 Π 被特别授予访问 RESET 基元的权限，并拥有充足的墙钟时间预算。由于基元词汇固定，探索完全聚焦于迭代组合：发现学习型 VLA 基元与确定性解析基元的最优编排。规划器反复尝试不同的定位顺序、接触前姿态、VLA ACT 调用时机和提前返回终止阈值；它观察每次基元调用的物理效果，并在失败后修正方向。

任务成功完成后，智能体将经验系统抽象到图 1 所示的两个记忆模块中。首先，已验证的基元调用序列被序列化为 JSONL。该文件记录逐步的基元调用，并用符号化感知查询替换具体空间坐标，从而可以在不同布局中复用。这个参数化 JSONL 轨迹被存入任务特定记忆，作为后续泛化测试的结构先验。其次，智能体提取一般化启发式规则并提交到持久化全局记忆。该仓库汇总成功规则（例如使用完整任务指令的最优提示策略），并记录失败模型（包括空抓取执行和错误成功检测）。这种汇总帮助规划器避免在不同任务中重复历史陷阱。

**部署评估阶段。** 在位置交换、指令重定向以及多个初始状态种子等未见环境变化上进行正式评估时，harness 施加严格的执行制度：RESET 被禁用，操作步数预算显著缩短。为了求解受扰动任务，规划器 Π 从任务特定记忆中检索预先计算的 JSONL 轨迹，并使用实时 RGB-D 观测动态地将其落地。通过参考全局记忆中的成功规则和失败模型，智能体确定性地执行轨迹。该严格阶段的性能直接构成论文报告的基准结果，从而验证 Harness VLA 框架的整体有效性。

**2.3 统一基元接口。** 基元库 P 是暴露给规划器的唯一动作接口。每个基元由一个 JSON 对象调用，在环境中执行直到内部后置条件满足，然后在刷新观测后将控制权返回。规划器从不直接输出低层力矩、关节目标或动作块；它依据语言、RGB-D 观测、本体感知和记忆选择基元并绑定参数。我们将 P 划分为两类操作基元：解析基元是根据机器人运动学定义的确定性模型控制器，不需要训练数据；它们又分为复合基元和原子基元。复合基元接收世界坐标系中的空间目标，并运行内嵌求解器以协调多个自由度；原子基元则把腕部方向、夹爪状态或底座速度等单一通道驱动到参数化设定点。VLA 基元 VLA ACT 将提示词和实时相机输入映射为局部接触密集行为的动作块。探索用 RESET 只在引导阶段使用，不计为操作基元。


### Source page 6 / 源页面 6


> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Table 1: Primitive vocabulary. The same primitive names are used throughout the paper; RoboCasa365 additionally uses mobile-base primitives for kitchen-scale staging. Primitive               Type                  Role MOVE TO                 Composite             Move an end-effector to a world-frame Cartesian target us- ing the environment’s embedded solver. MOVE POSE               Composite             Move the end-effector while co-varying pose variables such as pitch for reach-limited configurations. ROTATE WRIST            Atomic                Apply a wrist-yaw set-point while holding the current spa- tial position. ROTATE PITCH            Atomic                Apply a wrist-pitch set-point while holding the current spa- tial position. SET GRIPPER             Atomic                Drive the gripper to an open or closed set-point for a fixed number of steps. RELEASE                 Atomic                Open the gripper under a release post-condition. VLA ACT                 VLA                   Execute a frozen VLA in short bursts for local contact-rich interaction. NAVIGATE TO             Composite             Drive the mobile base to a world-frame location for (RoboCasa365)         kitchen-scale staging. MOVE BASE               Atomic                Apply an open-loop local base-velocity set-point for fine (RoboCasa365)         repositioning. used only during bootstrapping and is not counted as a manipulation primitive. Table 1 gives the primitive vocabulary used throughout the paper. The shared manipulation interface contains six analytic primitives and one VLA primitive; RoboCasa365 additionally uses two mobile-base primitives, NAVIGATE TO and MOVE BASE, for kitchen-scale staging. Details of RoboTwin bimanual exe- cution are provided in Appendix B. Crucially, the primitive vocabulary is fixed before evaluation; the planner cannot invent new primitives at deployment time. The compact JSON contract below illustrates the shared interface; Appendix B gives the benchmark- specific availability and implementation notes using the same primitive names. {"action": "move_to",     "xyz": [<x>,<y>,<z>], ...} {"action": "move_pose",   "xyz": [<x>,<y>,<z>], "pose": <orientation>, ...} {"action": "rotate_wrist","target_yaw": <float>, ...} {"action": "rotate_pitch","target_pitch": <float>, ...} {"action": "set_gripper", "gripper": <open|close>, ...} {"action": "release",     ...} {"action": "navigate_to", "xy": [<x>,<y>], ...} {"action": "move_base",   "forward": <float>, "lateral": <float>, "turn": < float>, ...} {"action": "vla_act",     "prompt": <str>, "max_chunks": <int>, "stop": <predicate>} VLA-backed contact primitive. VLA ACT is the learned primitive for contact-rich interaction. Across benchmarks, VLA ACT covers grasping, constrained placement, fixture actuation, button pressing, drawer or door manipulation, insertion, and embodiment-specific contact behaviors. The planner supplies a task- conditioned prompt and an early-return predicate τ . The frozen VLA fθ then emits action chunks until τ is satisfied or the chunk budget is exhausted. This keeps the VLA as a local contact specialist while semantic grounding, spatial re-binding, navigation, re-staging, and long-horizon composition remain under planner

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **表 1：基元词汇。** 论文全程使用相同的基元名称；RoboCasa365 额外使用移动底座基元进行厨房尺度定位。MOVE TO 是复合基元，使用环境内嵌求解器将末端执行器移动到世界坐标系笛卡尔目标；MOVE POSE 是复合基元，在移动末端执行器的同时共同改变 pitch 等姿态变量；ROTATE WRIST 是原子基元，在保持当前空间位置的同时施加腕部 yaw 设定；ROTATE PITCH 是原子基元，在保持空间位置的同时施加腕部 pitch 设定；SET GRIPPER 是原子基元，在固定步数内将夹爪驱动到打开或闭合设定；RELEASE 是带释放后置条件的打开夹爪基元；VLA ACT 是 VLA 基元，以短脉冲执行冻结 VLA，用于局部接触密集交互；NAVIGATE TO（RoboCasa365）是复合基元，将移动底座驱动到世界坐标位置以进行厨房尺度定位；MOVE BASE（RoboCasa365）是原子基元，施加开环局部底座速度设定以精细重新定位。RESET 只在引导阶段使用，不计为操作基元。共享操作接口包含六个解析基元和一个 VLA 基元；RoboCasa365 额外使用 NAVIGATE TO 和 MOVE BASE。RoboTwin 双臂执行细节见附录 B。基元词汇在评估前固定，规划器不能在部署时发明新基元。

共享 JSON 契约为：

- `{"action": "move_to", "xyz": [<x>,<y>,<z>], ...}`
- `{"action": "move_pose", "xyz": [<x>,<y>,<z>], "pose": <orientation>, ...}`
- `{"action": "rotate_wrist", "target_yaw": <float>, ...}`
- `{"action": "rotate_pitch", "target_pitch": <float>, ...}`
- `{"action": "set_gripper", "gripper": <open|close>, ...}`
- `{"action": "release", ...}`
- `{"action": "navigate_to", "xy": [<x>,<y>], ...}`
- `{"action": "move_base", "forward": <float>, "lateral": <float>, "turn": <float>, ...}`
- `{"action": "vla_act", "prompt": <str>, "max_chunks": <int>, "stop": <predicate>}`

**由 VLA 支持的接触基元。** VLA ACT 是用于接触密集交互的学习型基元。在各个基准中，它覆盖抓取、受限放置、装置驱动、按按钮、抽屉或门操作、插入以及具身特定的接触行为。规划器提供任务条件化提示词和提前返回谓词 τ。冻结 VLA f_θ 持续输出动作块，直到满足 τ 或动作块预算耗尽。这样 VLA 只作为局部接触专家，而语义落地、空间重新绑定、导航、重新定位和长时域组合仍由规划器控制。


### Source page 7 / 源页面 7


> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> control. 3     Experiments We organize the empirical study around two deployment regimes and three mechanism analyses. In the few-shot regime, Harness VLA follows the memory-backed workflow in Section 2.2: the agent performs task-level bootstrapping on one reference seed, stores the successful primitive trace in Task Specific Mem- ory, and re-grounds that trace under new seeds or perturbations. In the zero-shot regime, the agent must solve without retrieving Task Specific Memory or Global Memory for the target setting, testing how far online planner reasoning and the frozen primitive interface transfer without task-specific harness memory. Section 3.1 details the configuration, Section 3.2 presents few-shot and zero-shot benchmark performance, and Section 3.3 analyzes the mechanisms behind the gains. 3.1   Experimental Setup We evaluate Harness VLA on four benchmark families. The tabletop suites are LIBERO [19] and LIBERO- Pro [20]; the household and bimanual suites are RoboCasa365 [21] and RoboTwin C2R [22], respectively. We defer benchmark-specific task splits and seed protocols to Appendix C, and focus here on the main empirical outcomes. Across all evaluations, the planner operates over the same frozen primitive vocabulary P (Section 2.3) and is not allowed to introduce new primitives at deployment time. The VLA primitive is instantiated with benchmark-specific frozen policies while preserving a unified VLA ACT interface: the RLinf-released pi05 libero130 fullshot π0.5 -SFT checkpoint, denoted πRLinf [23], for LIBERO and LIBERO-Pro, the frozen RLDX-1 RoboCasa checkpoint [24] for RoboCasa365, and our post-trained LingBot-VLA checkpoint [25] for RoboTwin C2R. In the tables below, Harness VLA (Codex) and Har- ness VLA (CC) denote the same harness instantiated with Codex and Claude Code planners, respectively; CC abbreviates Claude Code. The πRLinf , RLDX-1, and LingBot-VLA rows serve as direct frozen-VLA baselines for their corresponding benchmarks. 3.2   Overall Benchmark Performance Few-shot evaluation with Task Specific Memory. We first evaluate Harness VLA after task-level boot- strapping has populated Task Specific Memory. This setting tests whether the harness can reuse the prim- itive organization discovered on a reference seed while grounding all spatial arguments from the current observations. We evaluate whether this memory-backed execution preserves strong in-distribution manipu- lation performance on standard LIBERO, remains robust under LIBERO-Pro instruction-redirection (T) and position-swap (S) perturbations, and extends the same primitive interface to household kitchen manipulation in RoboCasa365. Standard LIBERO. Table 2 reports results on the four standard LIBERO suites. Harness VLA (CC) achieves an aggregate success rate of 96.0% (384/400), including 100.0% on O BJECT and 93.0% on LIBERO-10. Compared with the frozen πRLinf checkpoint used inside VLA ACT, which obtains 95.3% overall, Harness VLA preserves competitive standard-suite performance while exposing the same policy through a controllable primitive interface for the perturbed evaluations below. LIBERO-Pro. Table 3 reports aggregate results on LIBERO-Pro, spanning S PATIAL, O BJECT, G OAL, and LIBERO-10 under instruction-redirection (T) and position-swap (S) perturbations. Existing end-to- end VLA models degrade sharply under these distribution shifts, and RATS is the strongest reported prior baseline with 43.8% overall on its reported cells. Harness VLA reaches 72.1% with Codex and 82.4% with CC, improving over RATS by 38.6 percentage points in the headline comparison. The direct πRLinf baseline reaches 50.0% overall under our protocol, showing that the gain does not simply come from the frozen VLA

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> **控制。** 我们围绕两种部署制度和三项机制分析组织实证研究。在少样本制度下，Harness VLA 遵循第 2.2 节的记忆支持工作流：智能体在一个参考种子上进行任务级引导，将成功基元轨迹存入任务特定记忆，并在新种子或扰动下重新落地该轨迹。在零样本制度下，目标设置不检索任务特定记忆或全局记忆，用以测试在没有任务特定 harness 记忆时，在线规划器推理和冻结基元接口能够迁移多远。第 3.1 节介绍配置，第 3.2 节报告少样本和零样本基准性能，第 3.3 节分析增益背后的机制。

**3.1 实验设置。** 我们在四类基准上评估 Harness VLA：LIBERO [19]、LIBERO-Pro [20]、RoboCasa365 [21] 和 RoboTwin C2R [22]。任务划分和种子协议放在附录 C；此处聚焦主要实证结果。所有评估中，规划器都在同一个冻结基元词汇 P（第 2.3 节）上运行，且部署时不得引入新基元。VLA 基元使用各基准的冻结策略实例化：LIBERO 和 LIBERO-Pro 使用 RLinf 发布的 pi05 libero130 fullshot π0.5-SFT 检查点，记为 π_RLinf [23]；RoboCasa365 使用冻结的 RLDX-1 RoboCasa 检查点 [24]；RoboTwin C2R 使用我们后训练的 LingBot-VLA 检查点 [25]。下表中的 Harness VLA (Codex) 与 Harness VLA (CC) 分别表示使用 Codex 和 Claude Code 规划器实例化的同一 harness；CC 是 Claude Code 的缩写。π_RLinf、RLDX-1 和 LingBot-VLA 行是对应基准的直接冻结 VLA 基线。

**3.2 总体基准性能。** **使用任务特定记忆的少样本评估。** 首先，我们在任务级引导已经填充任务特定记忆后评估 Harness VLA。该设置测试 harness 能否复用参考种子上发现的基元组织方式，同时从当前观测中落地全部空间参数。我们考察这种记忆支持的执行是否能在标准 LIBERO 上保持强分布内操作性能，在 LIBERO-Pro 指令重定向（T）和位置交换（S）扰动下保持稳健，并将同一基元接口扩展到 RoboCasa365 的家庭厨房操作。

**标准 LIBERO。** 表 2 报告四个标准 LIBERO 套件的结果。Harness VLA (CC) 的总体成功率为 96.0%（384/400），其中 OBJECT 达到 100.0%，LIBERO-10 达到 93.0%。VLA ACT 内部使用的冻结 π_RLinf 检查点总体达到 95.3%。因此，Harness VLA 在保持标准套件竞争力的同时，通过可控的基元接口暴露同一个策略，为下面的扰动评估提供接口。

**LIBERO-Pro。** 表 3 报告 LIBERO-Pro 在 SPATIAL、OBJECT、GOAL 和 LIBERO-10 上的聚合结果，覆盖指令重定向（T）和位置交换（S）扰动。现有端到端 VLA 模型在这类分布变化下显著退化；已报告基线中，RATS 在其报告单元上的总体成功率最高，为 43.8%。Harness VLA 使用 Codex 达到 72.1%，使用 CC 达到 82.4%；在标题性比较中比 RATS 高 38.6 个百分点。直接 π_RLinf 基线在我们的协议下总体达到 50.0%，说明增益并不只是来自冻结 VLA 主干。


### Source page 8 / 源页面 8


> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Table 2: Success rate (%) on standard LIBERO. πRLinf [23] and Harness VLA (CC) are evaluated by us on 100 trials per suite (10 tasks × 10 seeds). Harness VLA uses the same RLinf-released pi05 libero130 fullshot π0.5 -SFT checkpoint inside VLA ACT. Bold marks the best method in each suite or overall column. Method               Spatial   Object         Goal   LIBERO-10   Overall OpenVLA [2]           84.7      88.4          79.2      53.7      76.5 NORA [5]              85.6      89.4          80.0      63.0      79.5 π0 [3]                96.8      98.8          95.8      85.2      94.2 πRLinf                99.0      96.0          97.0      89.0      95.3 AtomVLA [26]          96.4      99.6          97.6      94.4      97.0 Harness VLA (CC)      97.0     100.0          94.0      93.0      96.0 Table 3: Aggregate LIBERO-Pro success rates (%) across S PATIAL, O BJECT, G OAL, and LIBERO-10 under instruction-redirection (T) and position-swap (S) perturbations. Each cell aggregates 100 trials (10 tasks × 10 seeds); “/” indicates an unavailable or unreported cell. Cap-X and RATS report only the six non-LIBERO-10 cells, so their overall values average over reported cells only. πRLinf and Harness VLA are evaluated by us using the RLinf-released pi05 libero130 fullshot π0.5 -SFT checkpoint [23]; Harness VLA exposes this frozen checkpoint through the VLA ACT primitive. Bold marks the best reported method in each evaluation cell or overall column. Method                  Spat-T Spat-S Obj-T Obj-S Goal-T Goal-S L10-T L10-S Overall OpenVLA [2]              0.0      0.0      0.0       0.0        0.0    0.0      0.0      0.0    0.0 π0 [3]                   0.0      0.0      0.0        2.0      0.0     0.0      0.0      0.0   0.3 π0.5 [4]                 1.0     20.0      1.0       17.0      2.0     38.0     1.0      8.0   11.0 MolmoAct [6]             0.0      0.0      0.0       6.0       0.0     0.0      6.0      0.0    1.5 NORA [5]                 0.0      0.0      0.0       0.0       0.0     0.0      0.0      0.0    0.0 X-VLA [27]               0.0      0.0      8.0       2.0       9.0     1.0     10.0      0.0    3.8 AtomVLA [26]             1.0     16.0      0.0       10.0      11.0    2.0      9.0      1.0    6.3 Cap-X [12]               14.0    12.0   18.0         22.0      17.0    26.0     /         /    18.2 RATS [13]                31.0    29.0   63.0         61.0      36.0    43.0     /         /    43.8 πRLinf                   42.0    59.0   71.0         78.0      45.0    42.0    49.0    14.0    50.0 Harness VLA (Codex)      81.0    69.0   94.0         91.0      75.0    66.0    52.0    49.0    72.1 Harness VLA (CC)         94.0    80.0   88.0         90.0      87.0    87.0    71.0    62.0    82.4

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **表 2：标准 LIBERO 上的成功率（%）。** π_RLinf [23] 和 Harness VLA (CC) 由我们评估，每个套件进行 100 次试验（10 个任务 × 10 个种子）。Harness VLA 在 VLA ACT 内部使用同一个 RLinf 发布的 pi05 libero130 fullshot π0.5-SFT 检查点。加粗表示每个套件或总体列中的最佳方法。

| 方法 | Spatial | Object | Goal | LIBERO-10 | Overall |
|---|---:|---:|---:|---:|---:|
| OpenVLA [2] | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 |
| NORA [5] | 85.6 | 89.4 | 80.0 | 63.0 | 79.5 |
| π0 [3] | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 |
| π_RLinf | 99.0 | 96.0 | 97.0 | 89.0 | 95.3 |
| AtomVLA [26] | 96.4 | 99.6 | 97.6 | 94.4 | 97.0 |
| Harness VLA (CC) | 97.0 | 100.0 | 94.0 | 93.0 | 96.0 |

**表 3：LIBERO-Pro 聚合成功率（%）。** 结果覆盖 SPATIAL、OBJECT、GOAL 和 LIBERO-10 在指令重定向（T）及位置交换（S）扰动下的表现。每个单元聚合 100 次试验（10 个任务 × 10 个种子）；“/”表示不可用或未报告的单元。Cap-X 和 RATS 只报告六个非 LIBERO-10 单元，因此它们的总体值只在已报告单元上取平均。π_RLinf 和 Harness VLA 使用 RLinf 发布的 pi05 libero130 fullshot π0.5-SFT 检查点 [23] 由我们评估；Harness VLA 通过 VLA ACT 基元暴露该冻结检查点。加粗表示每个评估单元或总体列中已报告方法的最佳结果。

| 方法 | Spat-T | Spat-S | Obj-T | Obj-S | Goal-T | Goal-S | L10-T | L10-S | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| OpenVLA [2] | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| π0 [3] | 0.0 | 0.0 | 0.0 | 2.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.3 |
| π0.5 [4] | 1.0 | 20.0 | 1.0 | 17.0 | 2.0 | 38.0 | 1.0 | 8.0 | 11.0 |
| MolmoAct [6] | 0.0 | 0.0 | 0.0 | 6.0 | 0.0 | 0.0 | 6.0 | 0.0 | 1.5 |
| NORA [5] | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| X-VLA [27] | 0.0 | 0.0 | 8.0 | 2.0 | 9.0 | 1.0 | 10.0 | 0.0 | 3.8 |
| AtomVLA [26] | 1.0 | 16.0 | 0.0 | 10.0 | 11.0 | 2.0 | 9.0 | 1.0 | 6.3 |
| Cap-X [12] | 14.0 | 12.0 | 18.0 | 22.0 | 17.0 | 26.0 | / | / | 18.2 |
| RATS [13] | 31.0 | 29.0 | 63.0 | 61.0 | 36.0 | 43.0 | / | / | 43.8 |
| π_RLinf | 42.0 | 59.0 | 71.0 | 78.0 | 45.0 | 42.0 | 49.0 | 14.0 | 50.0 |
| Harness VLA (Codex) | 81.0 | 69.0 | 94.0 | 91.0 | 75.0 | 66.0 | 52.0 | 49.0 | 72.1 |
| Harness VLA (CC) | 94.0 | 80.0 | 88.0 | 90.0 | 87.0 | 87.0 | 71.0 | 62.0 | 82.4 |


### Source page 9 / 源页面 9


> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> backbone. The gains across both instruction-redirection and position-swap settings show that the few-shot harness has learned a reusable division of labor over the fixed primitive library: the planner can re-bind targets, use analytic primitives to re-stage the scene and handle non-contact execution, and invoke the VLA only for local contact-rich manipulation. RoboCasa365. RoboCasa365 extends the evaluation from tabletop manipulation to household kitchen tasks with mobile staging, articulated fixtures, and longer composite routines. Table 4 compares Harness VLA against results reported in prior RoboCasa365 papers and the RLDX-1 baseline used for the headline comparison. RLDX-1 reaches a task-weighted overall success rate of 30.0%, while Harness VLA reaches 55.4% with Codex and 48.6% with CC; the Codex instantiation therefore improves over RLDX-1 by 25.4 percentage points. These gains are consistent with the intended decomposition: the planner handles nav- igation, staging, and re-staging after local failures, while the frozen VLA remains the local contact-rich primitive. Table 4: RoboCasa365 success rates (%). Baseline rows above the separator are results reported in the cor- responding prior papers on ATOMIC -S EEN, C OMPOSITE -S EEN, and C OMPOSITE -U NSEEN, with RLDX-1 evaluated as the direct frozen-VLA baseline under our protocol. Harness VLA uses one reference seed only for bootstrapping; reported evaluation uses ten held-out seeds for ATOMIC -S EEN and five held-out seeds for C OMPOSITE -S EEN and C OMPOSITE -U NSEEN. Bold marks the best method in each split. Method                   Atomic-Seen       Composite-Seen   Composite-Unseen RLDX-1 [24]                  60.0               21.3               5.0 WorldDreamer [28]            66.3               26.7               9.0 π0.5 [4]                     39.6               7.1                1.2 π0 [3]                       34.6               6.1                1.1 Harness VLA (Codex)          91.6              56.3               13.8 Harness VLA (CC)             79.4              47.5               15.0 Zero-shot evaluation without bootstrapped harness memory. LIBERO-Pro Goal. To separate online planner reasoning from bootstrapped harness memory, we evaluate LIBERO-P RO G OAL in a strict zero- shot setting where the agent does not retrieve the target-setting Task Specific Memory or the corresponding Global Memory. Table 5 shows that zero-shot Harness VLA (CC) outperforms Cap-X across both pertur- bation regimes, reaching 31.0% on position-swap (Pos-S) and 79.0% on instruction-redirection (Task-T), compared with Cap-X’s 25.6% and 16.8%. The comparison with the few-shot G OAL cells in Table 3 clar- ifies what bootstrapped harness memory contributes. Without this memory, the planner retains much of its semantic re-binding ability under instruction redirection (79.0% zero-shot versus 87.0% few-shot on Goal-T), but drops substantially under position swaps (31.0% zero-shot versus 87.0% few-shot on Goal-S). This gap indicates that spatially perturbed manipulation benefits strongly from the task-specific primitive organization discovered during exploration: analytic primitives supply localization, staging, transport, and release around the contact-rich phase, while VLA ACT is invoked at the learned interaction points and can be re-staged after failures. RoboTwin C2R. RoboTwin C2R evaluates zero-shot clean-to-randomized transfer: the agent obtains a Task Specific Memory trace from the clean setting and transfers it directly to randomized task instances, with no randomized-setting bootstrapping, additional task-level exploration, or VLA fine-tuning. The VLA ACT backend here is LingBot-VLA, our RoboTwin-specialized VLA checkpoint; after post-training, it is frozen for both the direct VLA baseline and Harness VLA evaluation. Table 6 compares C2R success rates against representative VLA baselines. Direct LingBot-VLA reaches 50.4%, while Harness VLA raises the same

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 冻结后端。指令重定向和位置交换设置中的增益表明，少样本 harness 学会了固定基元库上的可复用分工：规划器重新绑定目标，使用解析基元重新定位场景并处理非接触执行，只在局部接触密集操作中调用 VLA。

**RoboCasa365。** RoboCasa365 将评估从桌面操作扩展到家庭厨房任务，其中包含移动定位、关节装置和更长的复合流程。表 4 将 Harness VLA 与既有 RoboCasa365 论文报告的结果以及用于标题性比较的 RLDX-1 基线进行比较。RLDX-1 的任务加权总体成功率为 30.0%，Harness VLA 使用 Codex 达到 55.4%，使用 CC 达到 48.6%；因此 Codex 实例比 RLDX-1 提高 25.4 个百分点。这些增益符合预期分解：规划器处理导航、定位以及局部失败后的重新定位，而冻结 VLA 仍是局部接触密集基元。

**表 4：RoboCasa365 成功率（%）。** 分隔线以上的基线行是相应既有论文在 ATOMIC-SEEN、COMPOSITE-SEEN 和 COMPOSITE-UNSEEN 上报告的结果；RLDX-1 则按我们的协议作为直接冻结 VLA 基线评估。Harness VLA 只使用一个参考种子进行引导；报告的评估使用 ATOMIC-SEEN 的 10 个留出种子，以及 COMPOSITE-SEEN 和 COMPOSITE-UNSEEN 的 5 个留出种子。加粗表示每个划分中的最佳方法。

| 方法 | Atomic-Seen | Composite-Seen | Composite-Unseen |
|---|---:|---:|---:|
| RLDX-1 [24] | 60.0 | 21.3 | 5.0 |
| WorldDreamer [28] | 66.3 | 26.7 | 9.0 |
| π0.5 [4] | 39.6 | 7.1 | 1.2 |
| π0 [3] | 34.6 | 6.1 | 1.1 |
| Harness VLA (Codex) | 91.6 | 56.3 | 13.8 |
| Harness VLA (CC) | 79.4 | 47.5 | 15.0 |

**没有引导 harness 记忆的零样本评估。LIBERO-Pro Goal。** 为了区分在线规划器推理与引导得到的 harness 记忆，我们在严格零样本设置下评估 LIBERO-Pro GOAL，不检索目标设置的任务特定记忆或相应的全局记忆。表 5 显示，零样本 Harness VLA (CC) 在两种扰动制度下都超过 Cap-X：位置交换（Pos-S）达到 31.0%，指令重定向（Task-T）达到 79.0%，而 Cap-X 分别为 25.6% 和 16.8%。与表 3 的少样本 GOAL 单元比较，可以看出引导得到的 harness 记忆贡献了什么。没有该记忆时，指令重定向下规划器仍保留较强的语义重新绑定能力（Goal-T 零样本 79.0%，少样本 87.0%），但位置交换下显著下降（Goal-S 零样本 31.0%，少样本 87.0%）。这表明，空间扰动操作强烈受益于探索阶段发现的任务特定基元组织：解析基元在接触密集阶段周围提供定位、运输和释放，而 VLA ACT 在学习到的交互点被调用，并可在失败后重新定位。

**RoboTwin C2R。** RoboTwin C2R 评估零样本从干净环境到随机化环境的迁移：智能体从干净设置获得任务特定记忆轨迹，并将其直接迁移到随机化任务实例，不进行随机化设置引导、额外任务级探索或 VLA 微调。这里的 VLA ACT 后端是 LingBot-VLA，即 RoboTwin 专用 VLA 检查点；后训练后，该检查点在直接 VLA 基线和 Harness VLA 评估中都保持冻结。表 6 将 C2R 成功率与代表性 VLA 基线比较。直接 LingBot-VLA 达到 50.4%，而 Harness VLA 在同一冻结后端上使用 Codex 达到 58.0%，使用 CC 达到 58.4%。


### Source page 10 / 源页面 10


> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> Table 5: Per-task success rate (%) on LIBERO-P RO G OAL: zero-shot Harness VLA (CC) (no Task Specific Memory retrieval, 10 seeds/task) vs Cap-X [12]. Pos = swap (S), Task = instruction-redirection (T). Bold marks the winner within each setting and task or average column. Setting    Method             Task 0    Task 1    Task 2    Task 3   Task 4    Task 5   Task 6   Task 7   Task 8     Task 9   Average Pos (S)    Cap-X               0.0        4.0       0.0     36.0     22.0      60.0       4.0      2.0     62.0      66.0       25.6 Harness VLA (CC)    0.0       10.0       0.0     20.0     90.0       0.0      10.0     80.0    100.0       0.0       31.0 Task (T)   Cap-X               0.0       0.0       10.0      38.0    12.0       4.0      34.0     12.0     40.0       18.0      16.8 Harness VLA (CC)   10.0      100.0      90.0     100.0    20.0      80.0      90.0    100.0    100.0      100.0      79.0 frozen backend to 58.0% with Codex and 58.4% with CC. The table also reports external VLA baselines for context. Table 6: RoboTwin C2R success rates (%). LingBot-VLA is our post-trained RoboTwin VLA checkpoint evaluated directly without agent-level decomposition, and is also the frozen VLA ACT backend used by Harness VLA. Other VLA rows are representative external baselines. Harness VLA is evaluated on 50 tasks with 5 randomized seeds per task. Bold marks the best method. Benchmark        GR00T-N1.7 [29]     π0.5 [4]    StarVLA [30]    LingBot-VLA [25]       Harness VLA (Codex)        Harness VLA (CC) RoboTwin C2R          20.7             47.9          10.6               50.4                     58.0                    58.4 3.3    Experiment Analysis Obj Std           Obj-T πRLinf             Obj-T Ours             Goal Std            Goal-S πRLinf            Goal-S Ours Figure 3: Terminal-state frames for two LIBERO-Pro cells. The first triplet compares πRLinf on the standard O BJECT task, πRLinf on the task-perturbed O BJECT-P RO variant, and Harness VLA on the same perturbed task; when the task description redirects the target while the visual scene remains similar, πRLinf repeats the standard behavior instead of following the new instruction. The second triplet shows the analogous comparison for a swap-perturbed G OAL -P RO task; πRLinf blindly moves the object toward the training-time region after the layout changes, whereas Harness VLA re-grounds the target through the agentic planner Π, uses analytic primitives for staging, and invokes VLA ACT for the local contact-rich operation. We analyze the mechanisms behind these results through three distinct findings. Key Finding 1 focuses on semantic and scene re-grounding by the planner; Key Finding 2 studies planner-staged invocation and retry of VLA ACT; and Key Finding 3 studies how analytic primitives isolate non-contact execution from contact-rich control. Unless otherwise noted, the following analyses use Harness VLA (CC) as a represen- tative instantiation, without loss of generality: Codex and CC share the same harness, memory interface, primitive library, frozen VLA interface, and evaluation protocols, differing only in the planner backbone. LIBERO-family analyses use the same πRLinf checkpoint as the main evaluation, while non-LIBERO anal- yses use their benchmark-specific frozen VLA primitive.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> **表 5：LIBERO-Pro GOAL 零样本逐任务成功率（%）。** 这里比较不检索任务特定记忆、每个任务使用 10 个种子的零样本 Harness VLA (CC) 与 Cap-X [12]。Pos 表示交换（S），Task 表示指令重定向（T）；加粗表示每个设置及任务或平均列中的优胜者。

| 设置 | 方法 | Task 0 | Task 1 | Task 2 | Task 3 | Task 4 | Task 5 | Task 6 | Task 7 | Task 8 | Task 9 | 平均 |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Pos (S) | Cap-X | 0.0 | 4.0 | 0.0 | 36.0 | 22.0 | 60.0 | 4.0 | 2.0 | 62.0 | 66.0 | 25.6 |
| Pos (S) | Harness VLA (CC) | 0.0 | 10.0 | 0.0 | 20.0 | 90.0 | 0.0 | 10.0 | 80.0 | 100.0 | 0.0 | 31.0 |
| Task (T) | Cap-X | 0.0 | 0.0 | 10.0 | 38.0 | 12.0 | 4.0 | 34.0 | 12.0 | 40.0 | 18.0 | 16.8 |
| Task (T) | Harness VLA (CC) | 10.0 | 100.0 | 90.0 | 100.0 | 20.0 | 80.0 | 90.0 | 100.0 | 100.0 | 100.0 | 79.0 |

**3.3 实验分析。** 表 6 的 RoboTwin C2R 结果为：GR00T-N1.7 [29] 20.7，π0.5 [4] 47.9，StarVLA [30] 10.6，LingBot-VLA [25] 50.4，Harness VLA (Codex) 58.0，Harness VLA (CC) 58.4。图 3 展示两个 LIBERO-Pro 单元的终止状态帧。第一组三帧比较标准 OBJECT 任务上的 π_RLinf、任务扰动 OBJECT-Pro 上的 π_RLinf，以及同一扰动任务上的 Harness VLA；当任务描述重定向目标而视觉场景相近时，π_RLinf 重复标准行为而不遵循新指令。第二组三帧展示交换扰动的 GOAL-Pro：布局改变后，π_RLinf 盲目将物体移向训练时区域，而 Harness VLA 通过智能体规划器 Π 重新落地目标，使用解析基元定位，并调用 VLA ACT 完成局部接触密集操作。

我们通过三项发现分析这些结果背后的机制：关键发现 1 关注规划器进行的语义和场景重新落地；关键发现 2 研究规划器分阶段调用和重试 VLA ACT；关键发现 3 研究解析基元如何将非接触执行与接触密集控制隔离。除非另有说明，以下分析使用 Harness VLA (CC) 作为代表性实例，不影响一般性：Codex 与 CC 共享 harness、记忆接口、基元库、冻结 VLA 接口和评估协议，只有规划器主干不同。LIBERO 系列分析使用主实验中的同一 π_RLinf 检查点，非 LIBERO 分析使用各基准特定的冻结 VLA 基元。


### Source page 11 / 源页面 11


> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> Key Finding 1: Planner-level semantic re-grounding restores task-conditioned behavior. The mas- sive gap between Harness VLA and end-to-end VLAs in Table 3 is achieved without altering the visuomotor backbone. πRLinf already solves the standard variants of these tasks, but Figure 3 shows that its behavior is weakly conditioned on the task description and current scene binding. In the task-perturbed O BJECT- P RO case, the visual scene remains similar while the instruction redirects the target, yet πRLinf repeats the standard behavior instead of following the new task description. In the swap-perturbed G OAL -P RO case, the object layout changes, yet πRLinf still moves the object toward the training-time region. Harness VLA makes semantic grounding explicit at the planner level: the planner Π parses the task description, resolves the current contact target from the live RGB-D observation, uses analytic primitives for staging and repo- sitioning, and invokes or re-invokes VLA ACT only for the local contact-rich phase (Key Finding 2). Thus, semantic and scene-level reasoning is handled by the planner, while the frozen VLA remains responsible only for executing the contact-rich operation under the planner-provided binding. Key Finding 2: Planner-staged VLA invocation improves frozen-policy reliability. In Harness VLA, the planner does not call the VLA as a one-shot black box. Although the VLA is invoked sparsely rather than as a continuous controller, each call is a planner-chosen local contact-rich attempt whose staging can determine whether the frozen policy succeeds. The planner Π therefore treats VLA ACT as a local contact- rich primitive whose invocation can be re-staged and retried. Given a desired contact target (the object, fixture, or local interaction region to be acted on), the planner uses analytic primitives to place the robot in a feasible pre-contact configuration, invokes the VLA, observes the resulting contact state, and decides whether the next step should continue the task or reframe the local attempt. (a) LIBERO-P RO                      (b) ROBO C ASA 365                  (c) ROBOT WIN C2R Figure 4: Adaptive VLA invocation improves success across benchmarks. Each panel plots cumulative task success as a function of the maximum number of VLA primitive invocations allowed per episode. The blue dashed line marks the corresponding frozen-policy baseline, while the gray dashed line marks full Harness VLA performance with all planner-selected invocations. Across LIBERO-Pro, RoboCasa365, and RoboTwin C2R, success rises rapidly after the first few VLA calls and then saturates toward the full harness result, indicating that repeated planner-staged invocation is useful but remains sparse. First, staging restores a VLA-compatible local state. Under deployment perturbations such as semantic retargeting and spatial-layout shifts, the original VLA viewpoint or pre-contact pose may no longer expose the correct contact target in a familiar configuration. By re-staging the robot around the current scene, the agentic planner Π brings the target back into a VLA-compatible local observation while preserving the correct semantic binding. This mechanism explains why the harness can improve a frozen VLA without

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> **关键发现 1：规划器层面的语义重新落地恢复了任务条件行为。** 表 3 中 Harness VLA 与端到端 VLA 之间的巨大差距并非通过改变视觉运动主干获得。π_RLinf 已经能够解决这些任务的标准变体，但图 3 表明，其行为对任务描述和当前场景绑定的条件依赖较弱。在任务扰动 OBJECT-Pro 情况下，视觉场景相近而指令重定向了目标，π_RLinf 却重复标准行为而不是遵循新任务描述。在交换扰动 GOAL-Pro 情况下，物体布局发生变化，但 π_RLinf 仍将物体移向训练时区域。Harness VLA 在规划器层面显式完成语义落地：规划器 Π 解析任务描述，从实时 RGB-D 观测中确定当前接触目标，使用解析基元进行定位和重新定位，并只为局部接触密集阶段调用或再次调用 VLA ACT（关键发现 2）。因此，语义和场景层面的推理由规划器处理，而冻结 VLA 只负责在规划器提供的绑定下执行接触密集操作。

**关键发现 2：规划器分阶段调用 VLA 提高冻结策略的可靠性。** 在 Harness VLA 中，规划器不会把 VLA 当作一次性黑盒调用。虽然 VLA 是稀疏调用而非连续控制器，但每次调用都是规划器选择的局部接触密集尝试，其定位方式可能决定冻结策略能否成功。因此，规划器将 VLA ACT 视为可重新定位和重试的局部接触基元。给定期望接触目标（要操作的物体、装置或局部交互区域），规划器使用解析基元将机器人置于可行的接触前配置，调用 VLA，观察由此产生的接触状态，并决定下一步是继续任务还是重新构造局部尝试。

图 4：自适应 VLA 调用提高各基准上的成功率。每个面板以每个 episode 允许的 VLA 基元最大调用次数为函数，绘制累计任务成功率。蓝色虚线表示相应冻结策略基线，灰色虚线表示包含所有规划器选择调用的完整 Harness VLA 性能。在 LIBERO-Pro、RoboCasa365 和 RoboTwin C2R 上，前几次 VLA 调用后成功率快速上升，随后趋近完整 harness 结果，说明规划器分阶段重复调用有用但保持稀疏。

首先，定位可以恢复 VLA 兼容的局部状态。在语义目标重定向和空间布局变化等部署扰动下，原始 VLA 视角或接触前姿态可能无法再以熟悉配置暴露正确的接触目标。通过围绕当前场景重新定位，智能体规划器 Π 将目标带回 VLA 兼容的局部观测，同时保持正确的语义绑定。这解释了 harness 为何无需改变冻结 VLA 的参数就能改进它：harness 学习 VLA 应从哪里开始执行，而不是要求策略独自吸收完整分布变化。


### Source page 12 / 源页面 12


> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> changing its parameters: it learns where the VLA should begin acting, rather than asking the policy to absorb the full distribution shift by itself. Second, retry localizes contact failures. Because VLA execution is stochastic and short-horizon contact is physically brittle, a single failed attempt need not terminate the entire rollout. Harness VLA localizes such errors to the current contact-rich subtask: the planner can observe an incomplete or unstable outcome, re- stage the robot, and re-invoke VLA ACT, rather than letting a transient failure propagate through a monolithic long-horizon policy. Thus, repeated VLA calls are not continuous low-level control; they are sparse, planner- selected attempts that make contact-rich execution recoverable. Figure 5: Representative rollout frames for adaptive VLA invocation. Top row: a Harness VLA rollout on LIBERO-P RO O BJECT task 4. The planner repeatedly invokes VLA ACT around the milk carton after intermediate grasping or placement attempts leave the object outside or only partially inside the basket; after re-staging the end-effector and retrying the local contact-rich operation, the milk carton is finally placed stably inside the basket. Bottom row: a RoboCasa365 P RE S OAK PAN rollout. The planner adjusts the mobile base and arm pose around the pan, retries VLA ACT until a stable grasp is obtained, places the pan into the sink, and later invokes VLA ACT again to actuate the faucet. These examples show that repeated VLA calls are not continuous control, but planner-selected contact attempts embedded inside analytic navigation, staging, and verification. Figure 4 provides the aggregate evidence for this effect by capping the maximum number of VLA primitive invocations allowed in an episode. A small number of planner-selected invocations already exceeds the corresponding frozen-policy baseline, while additional invocations further improve success on longer or more contact-heavy tasks. Figure 5 gives representative case studies behind this curve: the planner observes an incomplete or unstable contact outcome, re-stages the robot or base, and calls VLA ACT again for the next local contact attempt. Together, these results show that the VLA is used sparsely, but the ability to re-stage and invoke it again is central to the robustness of the harness. Key Finding 3: Analytic primitives isolate non-contact execution from contact-rich control. Analytic primitives do not replace the VLA on contact-rich operations. Instead, they handle the surrounding non- contact structure of the task: free-space transport, pre-contact staging, wrist or base reorientation, retreat, and post-contact repositioning. This lets the planner reserve VLA ACT for the local contact-rich phases where learned visuomotor control is needed, including grasping, constrained placement, button pressing, faucet turning, drawer manipulation, and coffee-machine operation. Once the robot has established stable contact with the target, the planner Π can use analytic primitives to move, rotate, or navigate the robot toward the next relevant region, while invoking the VLA again when

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 改变其参数。其次，重试能够局部化接触失败。由于 VLA 执行具有随机性，短时域接触在物理上又很脆弱，一次失败尝试不必终止整个 rollout。Harness VLA 将这类错误局部化到当前接触密集子任务：规划器观察到不完整或不稳定结果后，重新定位机器人并再次调用 VLA ACT，而不是让暂时性失败沿着单体长时域策略传播。因此，重复的 VLA 调用不是连续的低层控制，而是由规划器选择的稀疏尝试，使接触密集执行具备恢复能力。

图 5：自适应 VLA 调用的代表性 rollout 帧。上排是 LIBERO-Pro OBJECT 任务 4 的 Harness VLA rollout：中间的抓取或放置尝试使牛奶盒位于篮子外部或仅部分进入篮子，规划器围绕牛奶盒反复调用 VLA ACT；重新定位末端执行器并重试局部接触操作后，牛奶盒最终稳定放入篮子。下排是 RoboCasa365 PRE SOAK PAN rollout：规划器围绕平底锅调整移动底座和机械臂姿态，反复调用 VLA ACT 直到获得稳定抓取，将平底锅放入水槽，随后再次调用 VLA ACT 操作水龙头。这些例子说明，重复 VLA 调用不是连续控制，而是嵌入解析导航、定位和验证中的规划器选择接触尝试。

图 4 通过限制每个 episode 允许的 VLA 基元最大调用次数，为这一效应提供总体证据。少量规划器选择的调用就已经超过相应冻结策略基线，更多调用则在更长或接触更多的任务上进一步提高成功率。图 5 给出了曲线背后的代表性案例：规划器观察到不完整或不稳定的接触结果，重新定位机器人或底座，再次调用 VLA ACT 进行下一次局部接触尝试。综合来看，VLA 的使用是稀疏的，但重新定位并再次调用它的能力是 harness 稳健性的核心。

**关键发现 3：解析基元将非接触执行与接触密集控制隔离。** 解析基元并不替代 VLA 执行接触密集操作，而是处理任务周围的非接触结构：自由空间运输、接触前定位、腕部或底座重新定向、撤退和接触后的重新定位。因此，规划器可以把 VLA ACT 保留给需要学习型视觉运动控制的局部接触密集阶段，包括抓取、受限放置、按按钮、旋转水龙头、抽屉操作和咖啡机操作。一旦机器人与目标建立稳定接触，规划器 Π 就可以用解析基元将机器人移动、旋转或导航到下一个相关区域，并在下一个接触密集阶段开始时再次调用 VLA。


### Source page 13 / 源页面 13


> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> the next contact-rich phase begins. Thus, the analytic vocabulary does not solve contact-rich manipulation by itself; it expands the conditions under which the same frozen VLA can be reused. By handling the non-contact context around each local interaction, the planner prevents the VLA from being responsible for long-horizon composition, scene-level grounding, and every intermediate motion in the rollout. Figure 6: Task completion attribution across benchmarks. Bars show the fraction of successful rollouts whose final benchmark completion predicate fires after an analytic primitive (blue) or after a VLA primitive (orange). LIBERO Pro-family tasks are mostly finished by analytic primitives after the VLA has established stable contact, whereas RoboCasa365 and RoboTwin C2R contain more terminal contact-rich operations such as fixture actuation, constrained placement, or bimanual object interaction. Figure 6 provides the aggregate attribution for this division of labor by separating successful rollouts according to the primitive class that triggers the final benchmark completion predicate. LIBERO Pro-family tasks are usually completed after analytic transport, release, or repositioning once contact has been estab- lished. In RoboCasa365 and RoboTwin C2R, the final predicate often depends directly on a contact-rich operation, so successful rollouts more frequently finish inside the VLA primitive. Figure 7 gives represen- tative examples: analytic primitives localize execution, expose failed or incomplete contacts, and move the robot back into a configuration where VLA ACT can be invoked again. The combined evidence supports the same division of labor: analytic primitives organize the task around contact-rich phases, while the VLA remains responsible for the phases where learned visuomotor control is needed. 4    Related Work Harness VLA sits at the intersection of three lines of work: end-to-end robot foundation policies, multimodal LLM agents, and programmatic robot-control systems. We review these areas through the role each assigns to learned policies and explicit control. This perspective clarifies our position: rather than fine-tuning a stronger VLA or expanding the primitive library, we study how a memory-guided agent can turn a frozen VLA into a controllable contact-rich primitive and compose it with fixed analytic controllers. VLA Models. End-to-end Vision-Language-Action (VLA) models map natural-language instructions and visual observations directly to low-level robot actions by extending pretrained vision-language backbones with an action head. The generalist-policy line opened by RT-1 [31] and Octo [32], scaled by RT-2 [1] and the Open X-Embodiment release [33], established the training pattern of co-training a large VLM with cross-embodiment robot demonstrations. OpenVLA [2] brought this paradigm into the open by combining a Prismatic-style VLM [34] with a Llama-2 action tokenizer, while the flow-matching π0 [3] and π0.5 [4] mod-

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> 解析词汇本身并不能解决接触密集操作；它扩展了同一冻结 VLA 可以被复用的条件。通过处理每个局部交互周围的非接触上下文，规划器避免让 VLA 承担长时域组合、场景级落地和 rollout 中的每一个中间运动。

图 6：各基准上的任务完成归因。柱状图显示成功 rollout 中最终基准完成谓词是在解析基元（蓝色）之后还是 VLA 基元（橙色）之后触发的比例。LIBERO Pro 系列任务通常在 VLA 建立稳定接触后由解析基元完成；RoboCasa365 和 RoboTwin C2R 则包含更多终端接触密集操作，例如装置驱动、受限放置或双臂物体交互。图 6 按触发最终基准完成谓词的基元类别划分成功 rollout，提供了这种分工的总体归因。LIBERO Pro 系列任务通常在建立接触后通过解析运输、释放或重新定位完成。在 RoboCasa365 和 RoboTwin C2R 中，最终谓词往往直接依赖接触密集操作，因此成功 rollout 更常在 VLA 基元内部结束。图 7 给出了代表性例子：解析基元定位执行、暴露失败或不完整接触，并将机器人带回可再次调用 VLA ACT 的配置。综合证据支持相同的分工：解析基元围绕接触密集阶段组织任务，VLA 负责需要学习型视觉运动控制的阶段。

**4 相关工作。** Harness VLA 位于三条研究线的交叉处：端到端机器人基础策略、多模态 LLM 智能体和程序化机器人控制系统。我们按照各方向对学习型策略和显式控制的分工来回顾它们。这一视角明确了本文的位置：我们不微调更强的 VLA，也不扩展基元库，而是研究记忆引导智能体如何将冻结 VLA 转化为可控的接触密集基元，并将其与固定解析控制器组合。

**VLA 模型。** 端到端视觉-语言-动作（VLA）模型通过在预训练视觉语言主干上增加动作头，将自然语言指令和视觉观测直接映射到机器人低层动作。RT-1 [31] 和 Octo [32] 开启了通用策略路线，RT-2 [1] 和 Open X-Embodiment [33] 将跨具身机器人示范的联合训练模式扩展到更大规模。OpenVLA [2] 将这一范式开放化，把 Prismatic 风格 VLM [34] 与 Llama-2 动作 tokenizer 结合；flow matching 的 π0 [3] 和 π0.5 [4] 则报告了通过异构数据和分布外语言联合训练获得的显著增益。


### Source page 14 / 源页面 14


> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> Figure 7: Representative rollout frames for analytic decomposition around contact-rich phases. Top row: on a LIBERO-10-P RO swap task, the agent first invokes VLA ACT and starts moving toward the basket, then detects during MOVE TO that the VLA has not actually grasped the cream-cheese box. The planner moves back, retries VLA ACT, and, after a successful grasp, completes the subtask with MOVE TO and RELEASE. Bottom row: on the RoboCasa S TEAM I N M ICROWAVE composite-seen task, the agent suc- cessfully grasps the bowl with VLA ACT, searches and repositions until the microwave is localized, invokes VLA ACT to place the bowl inside, pushes it in with MOVE TO, closes the door, and finally uses MOVE TO and NAVIGATE TO to press the switch. els reported substantial gains from co-training with heterogeneous data and out-of-distribution language. Recent large-scale systems such as GR00T [29] and Gemini Robotics [35] continue to scale this pattern to humanoid and general-purpose embodiments, alongside related lines on 3D-aware VLAs [36, 37], VLM- based imitation [38, 39], and CLIP-conditioned controllers [40–42]. Empirically, however, these models exhibit a sharp asymmetry: they are strongest at contact-rich visuomotor phases—in particular for irregu- lar grasping and fixture actuation that defeat analytic controllers—but degrade dramatically on instruction following, long-horizon composition, and out-of-distribution scenes [2, 4, 7]. This asymmetry motivates a factorization in which the VLA is delegated planner-selected contact-rich operations while a higher-level controller assumes responsibility for language interpretation, target grounding, transport, posture adjust- ment, navigation, and release. LLM-driven Multimodal Agent. Frontier multimodal large language models have rapidly closed the gap on dense perception, spatial reasoning, and long-horizon tool use. Recently, releases including GPT-5.2 [43], Gemini 3 [44], Qwen3-VL [45], the Claude 4 family (Sonnet 4.5 and Opus 4.7 [46]), and Llama 4 [47] have demonstrated qualitatively stronger physical-scene grounding than the GPT-4o [48] / Gemini 1.5 [49] generation, while open-weight models such as Molmo [50] and Qwen3-VL [45] make these capabilities broadly available. Targeted spatial benchmarks [51] and tool-augmented browsing agents [52–58] further show that, given a closed-loop interface, these backbones can sustain multi-hop perception and decision making over rich, partially observed environments. These advances make it increasingly viable to delegate semantic grounding and deterministic manipulation phases—language parsing, target localization, transport planning, posture adjustment, navigation, and release timing—to a frontier VLM at the top of the agent stack [18, 35, 59]. We build on this premise but, rather than driving the robot end-to-end with the VLM, place it inside an agentic harness that emits structured primitive calls, observes execution feedback, and iterates—reserving direct action prediction for planner-selected contact-rich phases.

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> 图 7：接触密集阶段周围解析分解的代表性 rollout 帧。上排是在 LIBERO-10-Pro 交换任务中，智能体首先调用 VLA ACT 并开始向篮子移动，随后在 MOVE TO 期间发现 VLA 实际上没有抓住奶油奶酪盒。规划器退回并重试 VLA ACT；成功抓取后，通过 MOVE TO 和 RELEASE 完成子任务。下排是在 RoboCasa STEAM IN MICROWAVE 的 composite-seen 任务中，智能体用 VLA ACT 成功抓取碗，搜索并重新定位直到找到微波炉，调用 VLA ACT 将碗放入其中，用 MOVE TO 将其推入，关上门，最后使用 MOVE TO 和 NAVIGATE TO 按下开关。

近期 GR00T [29] 和 Gemini Robotics [35] 等大规模系统继续将这一模式扩展到人形和通用具身形态，同时还出现了 3D 感知 VLA [36, 37]、VLM 监督模仿 [38, 39] 和 CLIP 条件控制器 [40–42] 等相关路线。然而从实证上看，这些模型表现出明显的不对称性：它们在接触密集的视觉运动阶段最强，尤其擅长解析控制器难以处理的不规则抓取和装置驱动；但在指令跟随、长时域组合和分布外场景中显著退化 [2, 4, 7]。这种不对称性促成了如下分解：将规划器选择的接触密集操作委托给 VLA，而由高层控制器负责语言解释、目标落地、运输、姿态调整、导航和释放。

**LLM 驱动的多模态智能体。** 前沿多模态大语言模型迅速缩小了在密集感知、空间推理和长时域工具使用方面的差距。近期发布的 GPT-5.2 [43]、Gemini 3 [44]、Qwen3-VL [45]、Claude 4 系列（Sonnet 4.5 和 Opus 4.7 [46]）以及 Llama 4 [47]，在物理场景落地方面表现出明显强于 GPT-4o [48] / Gemini 1.5 [49] 一代的能力；Molmo [50] 和 Qwen3-VL [45] 等开放权重模型则使这些能力更加广泛可用。针对性的空间基准 [51] 和工具增强浏览智能体 [52–58] 进一步表明，给定闭环接口后，这些主干可以在丰富且部分可观测的环境中持续进行多跳感知和决策。这些进展使得将语义落地和确定性操作阶段——语言解析、目标定位、运输规划、姿态调整、导航和释放时机——委托给智能体栈顶层的前沿 VLM 变得越来越可行 [18, 35, 59]。我们建立在这一前提上，但不让 VLM 端到端驱动机器人，而是将其放入一个输出结构化基元调用、观察执行反馈并不断迭代的智能体 harness 中；直接动作预测只保留给规划器选择的接触密集阶段。


### Source page 15 / 源页面 15


> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> Programmatic and Tool-Using Robot Agents. Code-as-policies systems recast robot control as program synthesis: the model writes an executable program that coordinates perception and motion APIs, leverag- ing the LLM’s compositional generalization while keeping low-level control deterministic. Beginning with Code-as-Policies [8], ProgPrompt [9], Instruct2Act [60], and ChatGPT-for-Robotics [61], this paradigm has been extended with multimodal program synthesis (RoboCodeX [62], ViperGPT [63], VisProg [10]), 3D value-map generation [64], VLM-supervised assembly [65], and long-horizon agentic frameworks [11, 66]. Harness VLA shares this literature’s goal of making language-model reasoning executable through explicit perception and control interfaces, but differs in the action representation: our agentic planner does not syn- thesize executable code or new control programs. It emits structured JSON primitive invocations inside a closed-loop harness, observes the execution outcome after each primitive, and re-binds the next primitive arguments from current RGB-D evidence and memory. Recent work also studies how agents can grow their own reusable skill libraries: ASPIRE [67] uses fine-grained execution traces to diagnose failures, synthesize validated repairs, and admit the resulting localization, navigation, motion, grasping, and debugging patterns into a continually expanding skill library. This direction is complementary to ours: ASPIRE expands the agent’s reusable skills, whereas Harness VLA deliberately keeps the primitive vocabulary fixed and stud- ies how memory-guided composition can extend a frozen VLA without deployment-time primitive expan- sion. A second strand draws on software-engineering agents: executable code is empirically a strong action representation for LLM agents [14], and systems such as SWE-agent [15] and OpenHands [16] formal- ize harnesses for iterative editing, execution, and feedback. We borrow the harness principle—structured interfaces, persistent state, execution feedback, and memory—rather than the requirement that actions be represented as code. Reliability is further improved by self-correction [68–70] and persistent symbolic state across steps [71], while LLM-driven planners [72–79] demonstrate that LLMs can sequence pretrained primitives or modules, ground 3D scenes, and recover from failures. Two limitations recur across this litera- ture, however. First, task-specific execution traces are rarely represented as reusable, parameterized memory that can be grounded again under new spatial layouts. Second, failure knowledge is seldom distilled into a Global Memory that prevents the planner from repeating known empty grasps, false successes, or unstable staging choices. Voyager [18] showed that persistent memory can improve embodied agents in a digital sandbox, but this memory-centric design has not been combined with a VLA-backed contact-rich primitive for physical manipulation. Our framework couples the two: a frozen VLA serves as a contact-rich special- ist invoked through a single primitive interface, successful primitive sequences are stored in Task Specific Memory, and reusable success rules and failure models are distilled into Global Memory. Together, these two design choices—VLA delegation for contact-rich operations, and memory-augmented primitive com- position for everything else—let a single memory-guided agentic planner cover the full task distribution exposed by a given environment, including paraphrased and re-targeted natural-language instructions that defeat monolithic VLAs whose language channel is largely vestigial [2, 4]. 5    Conclusion and Limitations We introduced Harness VLA, an asymmetric hierarchical framework that casts a frozen VLA as a single contact-rich primitive interface within an LLM-driven agent, delegating transport, posture, navigation, and release phases to the planner. From the perspective of agent harness engineering, Harness VLA shows that reliable manipulation can come not only from training a stronger policy, but also from surrounding a frozen policy with an auditable execution loop, fixed primitive contracts, memory, feedback, and task-level verification. Evaluations across standard and heavily perturbed benchmarks confirm that Harness VLA achieves state-of-the-art robustness. These results demonstrate that pretrained VLAs are most effective when isolated to contact-rich visuomotor control; abstracting semantic and spatial bindings away from the VLA prevents the catastrophic failures frequently observed in monolithic deployments.

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> **程序化与工具使用型机器人智能体。** Code-as-policies 系统将机器人控制重新表述为程序合成：模型编写协调感知和运动 API 的可执行程序，利用 LLM 的组合泛化，同时保持低层控制的确定性。从 Code-as-Policies [8]、ProgPrompt [9]、Instruct2Act [60] 和 ChatGPT-for-Robotics [61] 开始，这一范式扩展到多模态程序合成（RoboCodeX [62]、ViperGPT [63]、VisProg [10]）、3D 价值图生成 [64]、VLM 监督装配 [65] 和长时域智能体框架 [11, 66]。Harness VLA 与这些工作一样，目标是通过显式感知和控制接口使语言模型推理可执行，但动作表示不同：我们的智能体规划器不合成可执行代码或新的控制程序，而是在闭环 harness 内输出结构化 JSON 基元调用，观察每个基元后的执行结果，并根据当前 RGB-D 证据和记忆重新绑定下一个基元的参数。

近期工作还研究智能体如何扩展自己的可复用技能库。ASPIRE [67] 使用细粒度执行轨迹诊断失败、合成经验证的修复，并将由此产生的定位、导航、运动、抓取和调试模式纳入持续扩展的技能库。这一方向与本文互补：ASPIRE 扩展智能体的可复用技能，而 Harness VLA 有意保持基元词汇固定，研究记忆引导的组合如何在不于部署时扩充基元的情况下扩展冻结 VLA。另一条路线来自软件工程智能体：实证表明，可执行代码是 LLM 智能体的强动作表示 [14]，SWE-agent [15] 和 OpenHands [16] 等系统将迭代编辑、执行和反馈的 harness 形式化。我们借鉴的是 harness 原则——结构化接口、持久状态、执行反馈和记忆——而不是要求动作必须表示为代码。自我纠正 [68–70] 和跨步骤持久符号状态 [71] 进一步提高可靠性；LLM 驱动的规划器 [72–79] 也表明，LLM 可以排序预训练基元或模块、落地 3D 场景并从失败中恢复。

然而，这类工作反复存在两项局限。第一，任务特定执行轨迹很少被表示为可复用、参数化的记忆，以便在新的空间布局下再次落地。第二，失败知识很少被提炼为全局记忆，因而规划器无法避免重复已知的空抓取、错误成功或不稳定定位选择。Voyager [18] 表明持久记忆可以改进数字沙箱中的具身智能体，但这种以记忆为中心的设计尚未与物理操作中的 VLA 接触密集基元结合。我们的框架将二者结合：冻结 VLA 通过单一基元接口充当接触密集专家；成功的基元序列存入任务特定记忆；可复用的成功规则和失败模型提炼到全局记忆。两项设计选择——将接触密集操作委托给 VLA，以及为其他操作采用记忆增强的基元组合——使单个记忆引导智能体规划器能够覆盖给定环境暴露的完整任务分布，包括会击败语言通道基本上只是附属品的单体 VLA 的释义指令和重新定向自然语言指令 [2, 4]。

**5 结论与局限。** 我们提出 Harness VLA，这是一种非对称层级框架：在 LLM 驱动的智能体内部，将冻结 VLA 视为单一的接触密集基元接口，并把运输、姿态、导航和释放阶段委托给规划器。从智能体 harness 工程的角度看，可靠操作不仅可以来自训练更强的策略，也可以来自用可审计执行循环、固定基元契约、记忆、反馈和任务级验证包围冻结策略。在标准和强烈受扰动的基准上进行的评估证实，Harness VLA 具有最先进的稳健性。这些结果表明，预训练 VLA 在被隔离用于接触密集视觉运动控制时最有效；将语义和空间绑定抽离 VLA，可以避免单体部署中经常出现的灾难性失败。


### Source page 16 / 源页面 16


> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> Limitations and future work. Our current framework is limited by an open feedback loop between the high-level planner and low-level VLA. Additionally, the system lacks joint fine-tuning via environmen- tal rewards and human preferences—an issue necessitating future sample-efficient reinforcement learning (e.g., GRPO). Finally, the absence of fine-grained image captioning constrains structural reasoning in highly cluttered, long-horizon tasks. A complementary future direction is to combine our fixed-vocabulary com- position strategy with automatic skill-discovery systems such as ASPIRE [67]: when repeated primitive compositions reveal a missing abstraction, an agent could propose, validate, and admit a new reusable skill while retaining the auditable primitive interface and VLA-backed contact specialization studied here.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> **局限与未来工作。** 当前框架受限于高层规划器与低层 VLA 之间的开放反馈回路。此外，系统缺少通过环境奖励和人类偏好进行联合微调的能力，这一问题需要未来研究样本高效的强化学习方法（例如 GRPO）。最后，缺少细粒度图像描述限制了系统在高度杂乱、长时域任务中的结构推理。一个互补的未来方向是将固定词汇组合策略与 ASPIRE [67] 等自动技能发现系统结合：当重复的基元组合暴露出缺失的抽象时，智能体可以提出、验证并纳入一种新的可复用技能，同时保留本文研究的可审计基元接口和 VLA 支持的接触专门化。


### Source page 17 / 源页面 17


> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> References [1] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, X. Chen, K. Choromanski, T. Ding, D. Driess, A. Dubey, C. Finn, et al. RT-2: Vision-language-action models transfer web knowledge to robotic control. In Conference on Robot Learning (CoRL), 2023. [2] M. J. Kim, K. Pertsch, S. Karamcheti, T. Xiao, A. Balakrishna, S. Nair, R. Rafailov, E. Foster, G. Lam, P. Sanketi, et al. Openvla: An open-source vision-language-action model. arXiv preprint arXiv:2406.09246, 2024. [3] K. Black, N. Brown, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, L. Groom, K. Hausman, B. Ichter, et al. π0 : A vision-language-action flow model for general robot control. In Robotics: Science and Systems (RSS), 2025. [4] Physical Intelligence, K. Black, N. Brown, J. Darpinian, K. Dhabalia, D. Driess, A. Esmail, M. Equi, C. Finn, N. Fusai, M. Y. Galliker, D. Ghosh, L. Groom, K. Hausman, B. Ichter, S. Jakubczak, T. Jones, L. Ke, D. LeBlanc, S. Levine, A. Li-Bell, M. Mothukuri, S. Nair, K. Pertsch, A. Z. Ren, L. X. Shi, L. Smith, J. T. Springenberg, K. Stachowicz, J. Tanner, Q. Vuong, H. Walke, A. Walling, H. Wang, L. Yu, and U. Zhilinsky. π0.5 : a vision-language-action model with open-world generalization. arXiv preprint arXiv:2504.16054, 2025. [5] C.-Y. Hung, Q. Sun, P. Hong, A. Zadeh, C. Li, U. Tan, N. Majumder, S. Poria, et al. NORA: A small open-sourced generalist vision language action model for embodied tasks. arXiv preprint arXiv:2504.19854, 2025. [6] J. Lee, J. Duan, H. Fang, Y. Deng, S. Liu, B. Li, B. Fang, J. Zhang, Y. R. Wang, S. Lee, W. Han, W. Pumacay, A. Wu, R. Hendrix, K. Farley, E. VanderBilt, A. Farhadi, D. Fox, and R. Krishna. Mol- moAct: Action reasoning models that can reason in space. arXiv preprint arXiv:2508.07917, 2025. [7] J. Wang, M. Leonard, K. Daniilidis, D. Jayaraman, and E. S. Hu. Evaluating π0 in the wild: Strengths, problems, and the future of generalist robot policies. Online, 2025. [8] J. Liang, W. Huang, F. Xia, P. Xu, K. Hausman, B. Ichter, P. Florence, and A. Zeng. Code as policies: Language model programs for embodied control. In IEEE International Conference on Robotics and Automation (ICRA), 2023. [9] I. Singh, V. Blukis, A. Mousavian, A. Goyal, D. Xu, J. Tremblay, D. Fox, J. Thomason, and A. Garg. Progprompt: Generating situated robot task plans using large language models. In IEEE International Conference on Robotics and Automation (ICRA), 2023. [10] T. Gupta and A. Kembhavi. Visual programming: Compositional visual reasoning without training. In IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2023. [11] J. Shi, R. Yang, K. Chao, B. S. Wan, Y. S. Shao, J. Lei, J. Qian, L. Le, P. Chaudhari, K. Daniilidis, et al. Maestro: Orchestrating robotics modules with vision-language models for zero-shot generalist robots. In NeurIPS 2025 Workshop on Space in Vision, Language, and Embodied AI, 2025. [12] M. Fu, J. Yu, K. El-Refai, E. Kou, H. Xue, H. Huang, W. Xiao, G. Wang, F.-F. Li, G. Shi, et al. CaP-X: A framework for benchmarking and improving coding agents for robot manipulation. arXiv preprint arXiv:2603.22435, 2026. [13] J. Zhang, J. Ge, H. Yoo, L. Fu, Z. Yang, Y. Liu, R. Saravanan, S. Yin, J. Yu, D. Niu, et al. Playful agentic robot learning. arXiv preprint arXiv:2606.19419, 2026.

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> [1] A. Brohan、N. Brown、J. Carbajal、Y. Chebotar、X. Chen、K. Choromanski、T. Ding、D. Driess、A. Dubey、C. Finn 等。RT-2：视觉-语言-动作模型将网络知识迁移到机器人控制。在 Conference on Robot Learning（CoRL），2023。

[2] M. J. Kim、K. Pertsch、S. Karamcheti、T. Xiao、A. Balakrishna、S. Nair、R. Rafailov、E. Foster、G. Lam、P. Sanketi 等。OpenVLA：开源视觉-语言-动作模型。arXiv 预印本 arXiv:2406.09246，2024。

[3] K. Black、N. Brown、D. Driess、A. Esmail、M. Equi、C. Finn、N. Fusai、L. Groom、K. Hausman、B. Ichter 等。π0：用于通用机器人控制的视觉-语言-动作流模型。在 Robotics: Science and Systems（RSS），2025。

[4] Physical Intelligence、K. Black、N. Brown、J. Darpinian、K. Dhabalia、D. Driess、A. Esmail、M. Equi、C. Finn、N. Fusai、M. Y. Galliker、D. Ghosh、L. Groom、K. Hausman、B. Ichter、S. Jakubczak、T. Jones、L. Ke、D. LeBlanc、S. Levine、A. Li-Bell、M. Mothukuri、S. Nair、K. Pertsch、A. Z. Ren、L. X. Shi、L. Smith、J. T. Springenberg、K. Stachowicz、J. Tanner、Q. Vuong、H. Walke、A. Walling、H. Wang、L. Yu 和 U. Zhilinsky。π0.5：具有开放世界泛化能力的视觉-语言-动作模型。arXiv 预印本 arXiv:2504.16054，2025。

[5] C.-Y. Hung、Q. Sun、P. Hong、A. Zadeh、C. Li、U. Tan、N. Majumder、S. Poria 等。NORA：用于具身任务的小型开源通用视觉-语言-动作模型。arXiv 预印本 arXiv:2504.19854，2025。

[6] J. Lee、J. Duan、H. Fang、Y. Deng、S. Liu、B. Li、B. Fang、J. Zhang、Y. R. Wang、S. Lee、W. Han、W. Pumacay、A. Wu、R. Hendrix、K. Farley、E. VanderBilt、A. Farhadi、D. Fox 和 R. Krishna。MolmoAct：能够在空间中进行推理的动作推理模型。arXiv 预印本 arXiv:2508.07917，2025。

[7] J. Wang、M. Leonard、K. Daniilidis、D. Jayaraman 和 E. S. Hu。在真实环境中评估 π0：通用机器人策略的优势、问题与未来。Online，2025。

[8] J. Liang、W. Huang、F. Xia、P. Xu、K. Hausman、B. Ichter、P. Florence 和 A. Zeng。Code as Policies：用于具身控制的语言模型程序。在 IEEE International Conference on Robotics and Automation（ICRA），2023。

[9] I. Singh、V. Blukis、A. Mousavian、A. Goyal、D. Xu、J. Tremblay、D. Fox、J. Thomason 和 A. Garg。ProgPrompt：使用大语言模型生成具身机器人任务计划。在 IEEE International Conference on Robotics and Automation（ICRA），2023。

[10] T. Gupta 和 A. Kembhavi。Visual Programming：无需训练的组合式视觉推理。在 IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR），2023。

[11] J. Shi、R. Yang、K. Chao、B. S. Wan、Y. S. Shao、J. Lei、J. Qian、L. Le、P. Chaudhari、K. Daniilidis 等。Maestro：利用视觉-语言模型为零样本通用机器人编排机器人模块。在 NeurIPS 2025 Workshop on Space in Vision, Language, and Embodied AI，2025。

[12] M. Fu、J. Yu、K. El-Refai、E. Kou、H. Xue、H. Huang、W. Xiao、G. Wang、F.-F. Li、G. Shi 等。CaP-X：用于评测和改进机器人操作编码智能体的框架。arXiv 预印本 arXiv:2603.22435，2026。

[13] J. Zhang、J. Ge、H. Yoo、L. Fu、Z. Yang、Y. Liu、R. Saravanan、S. Yin、J. Yu、D. Niu 等。具身智能体的游戏化机器人学习。arXiv 预印本 arXiv:2606.19419，2026。


### Source page 18 / 源页面 18


> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> [14] X. Wang, Y. Chen, L. Yuan, Y. Zhang, Y. Li, H. Peng, and H. Ji. Executable code actions elicit better LLM agents. In International Conference on Machine Learning (ICML), 2024. [15] J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. R. Narasimhan, and O. Press. SWE-agent: Agent-computer interfaces enable automated software engineering. In Advances in Neural Information Processing Systems (NeurIPS), 2024. [16] X. Wang, B. Li, Y. Song, F. F. Xu, X. Tang, M. Zhuge, J. Pan, Y. Song, B. Li, J. Singh, H. H. Tran, F. Li, R. Ma, M. Zheng, B. Qian, Y. Shao, N. Muennighoff, Y. Zhang, B. Hui, J. Lin, R. Brennan, H. Peng, H. Ji, and G. Neubig. OpenHands: An open platform for AI software developers as generalist agents. In International Conference on Learning Representations (ICLR), 2025. [17] X. Ning, K. Tieu, D. Fu, T. Wei, Z. Li, Y. Bei, J. Zou, M. Ai, Z. Liu, T.-W. Li, et al. Code as agent harness. arXiv preprint arXiv:2605.18747, 2026. [18] G. Wang, Y. Xie, Y. Jiang, A. Mandlekar, C. Xiao, Y. Zhu, L. Fan, and A. Anandkumar. Voyager: An open-ended embodied agent with large language models. arXiv preprint arXiv:2305.16291, 2023. [19] B. Liu, Y. Zhu, C. Gao, Y. Feng, Q. Liu, Y. Zhu, and P. Stone. Libero: Benchmarking knowledge transfer for lifelong robot learning. Advances in Neural Information Processing Systems (NeurIPS), 36, 2023. [20] Y. Zhou et al. LIBERO-Pro: Towards realistic robotic manipulation benchmarks via systematic per- turbations. arXiv preprint arXiv:2510.03827, 2025. [21] S. Nasiriany, S. Nasiriany, A. Maddukuri, and Y. Zhu. RoboCasa365: A large-scale simulation frame- work for training and benchmarking generalist robots. arXiv preprint arXiv:2603.04356, 2026. [22] Y. Mu, T. Chen, Z. Chen, S. Peng, Z. Lan, Z. Gao, Z. Liang, Q. Yu, Y. Zou, M. Xu, et al. RoboTwin: Dual-arm robot benchmark with generative digital twins. In IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2025. [23] C. Yu, Y. Wang, Z. Guo, H. Lin, S. Xu, H. Zang, Q. Zhang, Y. Wu, C. Zhu, J. Hu, et al. Rlinf: Flexible and efficient large-scale reinforcement learning via macro-to-micro flow transformation. arXiv preprint arXiv:2509.15965, 2025. [24] D. Kim, H. Jang, M. Koo, S. Jang, T. Kim, B. Kim, B. Yoon, C. Jang, D. Choi, D. Han, et al. Rldx-1 technical report. arXiv preprint arXiv:2605.03269, 2026. [25] W. Wu, F. Lu, Y. Wang, S. Yang, S. Liu, F. Wang, Q. Zhu, H. Sun, Y. Wang, S. Ma, et al. A pragmatic VLA foundation model. arXiv preprint arXiv:2601.18692, 2026. [26] X. Sun, Z. Xu, C. Cao, Z. Liu, Y. Sun, J. Pang, R. Zhang, Z. Yang, K. Pang, D. He, et al. AtomVLA: Scalable post-training for robotic manipulation via predictive latent world models. arXiv preprint arXiv:2603.08519, 2026. [27] J. Zheng, J. Li, Z. Wang, D. Liu, X. Kang, Y. Feng, et al. X-VLA: Soft-prompted transformer as scalable cross-embodiment vision-language-action model. arXiv preprint arXiv:2510.10274, 2025. [28] X. Wang, Z. Zhu, G. Huang, B. Wang, X. Chen, and J. Lu. Worlddreamer: Towards general world models for video generation via predicting masked tokens. arXiv preprint arXiv:2401.09985, 2024.

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> [14] X. Wang、Y. Chen、L. Yuan、Y. Zhang、Y. Li、H. Peng 和 H. Ji。可执行代码动作能够激发更好的 LLM 智能体。在 International Conference on Machine Learning（ICML），2024。

[15] J. Yang、C. E. Jimenez、A. Wettig、K. Lieret、S. Yao、K. R. Narasimhan 和 O. Press。SWE-agent：智能体-计算机接口实现自动化软件工程。在 Advances in Neural Information Processing Systems（NeurIPS），2024。

[16] X. Wang、B. Li、Y. Song、F. F. Xu、X. Tang、M. Zhuge、J. Pan、Y. Song、B. Li、J. Singh、H. H. Tran、F. Li、R. Ma、M. Zheng、B. Qian、Y. Shao、N. Muennighoff、Y. Zhang、B. Hui、J. Lin、R. Brennan、H. Peng、H. Ji 和 G. Neubig。OpenHands：面向通用智能体的 AI 软件开发者开放平台。在 International Conference on Learning Representations（ICLR），2025。

[17] X. Ning、K. Tieu、D. Fu、T. Wei、Z. Li、Y. Bei、J. Zou、M. Ai、Z. Liu、T.-W. Li 等。Code as agent harness。arXiv 预印本 arXiv:2605.18747，2026。

[18] G. Wang、Y. Xie、Y. Jiang、A. Mandlekar、C. Xiao、Y. Zhu、L. Fan 和 A. Anandkumar。Voyager：一种使用大语言模型的开放式具身智能体。arXiv 预印本 arXiv:2305.16291，2023。

[19] B. Liu、Y. Zhu、C. Gao、Y. Feng、Q. Liu、Y. Zhu 和 P. Stone。LIBERO：面向终身机器人学习的知识迁移基准。Advances in Neural Information Processing Systems（NeurIPS），36，2023。

[20] Y. Zhou 等。LIBERO-Pro：通过系统化扰动迈向真实的机器人操作基准。arXiv 预印本 arXiv:2510.03827，2025。

[21] S. Nasiriany、S. Nasiriany、A. Maddukuri 和 Y. Zhu。RoboCasa365：用于训练和评测通用机器人的大规模仿真框架。arXiv 预印本 arXiv:2603.04356，2026。

[22] Y. Mu、T. Chen、Z. Chen、S. Peng、Z. Lan、Z. Gao、Z. Liang、Q. Yu、Y. Zou、M. Xu 等。RoboTwin：具有生成式数字孪生的双臂机器人基准。在 IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR），2025。

[23] C. Yu、Y. Wang、Z. Guo、H. Lin、S. Xu、H. Zang、Q. Zhang、Y. Wu、C. Zhu、J. Hu 等。RLinf：通过宏观到微观的流转换实现灵活高效的大规模强化学习。arXiv 预印本 arXiv:2509.15965，2025。

[24] D. Kim、H. Jang、M. Koo、S. Jang、T. Kim、B. Kim、B. Yoon、C. Jang、D. Choi、D. Han 等。RLDX-1 技术报告。arXiv 预印本 arXiv:2605.03269，2026。

[25] W. Wu、F. Lu、Y. Wang、S. Yang、S. Liu、F. Wang、Q. Zhu、H. Sun、Y. Wang、S. Ma 等。一种实用型 VLA 基础模型。arXiv 预印本 arXiv:2601.18692，2026。

[26] X. Sun、Z. Xu、C. Cao、Z. Liu、Y. Sun、J. Pang、R. Zhang、Z. Yang、K. Pang、D. He 等。AtomVLA：通过预测式潜在世界模型实现可扩展的机器人操作后训练。arXiv 预印本 arXiv:2603.08519，2026。

[27] J. Zheng、J. Li、Z. Wang、D. Liu、X. Kang、Y. Feng 等。X-VLA：作为可扩展跨具身视觉-语言-动作模型的软提示 Transformer。arXiv 预印本 arXiv:2510.10274，2025。

[28] X. Wang、Z. Zhu、G. Huang、B. Wang、X. Chen 和 J. Lu。WorldDreamer：通过预测掩码 token 迈向通用视频生成世界模型。arXiv 预印本 arXiv:2401.09985，2024。


### Source page 19 / 源页面 19


> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> [29] J. Bjorck, F. Castañeda, N. Cherniadev, X. Da, R. Ding, L. Fan, Y. Fang, D. Fox, F. Hu, S. Huang, et al. Gr00t n1: An open foundation model for generalist humanoid robots. arXiv preprint arXiv:2503.14734, 2025. [30] S. Community. Starvla: A lego-like codebase for vision-language-action model developing. arXiv preprint arXiv:2604.05014, 2026. [31] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, J. Dabis, C. Finn, K. Gopalakrishnan, K. Hausman, A. Herzog, J. Hsu, et al. Rt-1: Robotics transformer for real-world control at scale. arXiv preprint arXiv:2212.06817, 2022. [32] Octo Model Team, D. Ghosh, H. Walke, K. Pertsch, K. Black, O. Mees, S. Dasari, J. Hejna, C. Xu, J. Luo, T. Kreiman, Y. Tan, D. Sadigh, C. Finn, and S. Levine. Octo: An open-source generalist robot policy. Online, 2023. [33] Open X-Embodiment Collaboration. Open X-Embodiment: Robotic learning datasets and RT-X mod- els. Online, 2023. [34] S. Karamcheti, S. Nair, A. Balakrishna, P. Liang, T. Kollar, and D. Sadigh. Prismatic vlms: Investi- gating the design space of visually-conditioned language models. arXiv preprint arXiv:2402.07865, 2024. [35] Gemini Robotics Team, S. Abeyruwan, J. Ainslie, J.-B. Alayrac, M. G. Arenas, T. Armstrong, A. Bal- akrishna, R. Baruch, M. Bauza, M. Blokzijl, et al. Gemini robotics: Bringing ai into the physical world. arXiv preprint arXiv:2503.20020, 2025. [36] H. Zhen, X. Qiu, P. Chen, J. Yang, X. Yan, Y. Du, Y. Hong, and C. Gan. 3d-vla: 3d vision-language- action generative world model. arXiv preprint arXiv:2403.09631, 2024. [37] D. Driess, F. Xia, M. S. M. Sajjadi, C. Lynch, A. Chowdhery, B. Ichter, A. Wahid, J. Tompson, Q. Vuong, T. Yu, W. Huang, Y. Chebotar, P. Sermanet, D. Duckworth, S. Levine, V. Vanhoucke, K. Hausman, M. Toussaint, K. Greff, A. Zeng, I. Mordatch, and P. Florence. PaLM-E: An embodied multimodal language model. In International Conference on Machine Learning (ICML), 2023. [38] X. Li, M. Liu, H. Zhang, C. Yu, J. Xu, H. Wu, H. Dong, H. Hu, W. Zhan, H. Wu, Y. Han, and T. Kong. Vision-language foundation models as effective robot imitators. In International Conference on Learning Representations (ICLR), 2024. [39] J. Huang, S. Yong, X. Ma, X. Linghu, P. Li, Y. Wang, Q. Li, S.-C. Zhu, B. Jia, and S. Huang. An embodied generalist agent in 3d world. In International Conference on Machine Learning (ICML), 2024. [40] M. Shridhar, L. Manuelli, and D. Fox. Cliport: What and where pathways for robotic manipulation. In Conference on Robot Learning (CoRL), 2022. [41] C. Chi, S. Feng, Y. Du, Z. Xu, E. Cousineau, B. Burchfiel, and S. Song. Diffusion policy: Visuomotor policy learning via action diffusion. In Robotics: Science and Systems (RSS), 2023. [42] T. Z. Zhao, V. Kumar, S. Levine, and C. Finn. Learning fine-grained bimanual manipulation with low-cost hardware. In Robotics: Science and Systems (RSS), 2023. [43] OpenAI. Introducing GPT-5.2. Online, 2025.

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> [29] J. Bjorck、F. Castañeda、N. Cherniadev、X. Da、R. Ding、L. Fan、Y. Fang、D. Fox、F. Hu、S. Huang 等。GR00T N1：面向通用人形机器人的开放基础模型。arXiv 预印本 arXiv:2503.14734，2025。

[30] S. Community。StarVLA：用于开发视觉-语言-动作模型的乐高式代码库。arXiv 预印本 arXiv:2604.05014，2026。

[31] A. Brohan、N. Brown、J. Carbajal、Y. Chebotar、J. Dabis、C. Finn、K. Gopalakrishnan、K. Hausman、A. Herzog、J. Hsu 等。RT-1：面向大规模真实世界控制的 Robotics Transformer。arXiv 预印本 arXiv:2212.06817，2022。

[32] Octo Model Team、D. Ghosh、H. Walke、K. Pertsch、K. Black、O. Mees、S. Dasari、J. Hejna、C. Xu、J. Luo、T. Kreiman、Y. Tan、D. Sadigh、C. Finn 和 S. Levine。Octo：开源通用机器人策略。Online，2023。

[33] Open X-Embodiment Collaboration。Open X-Embodiment：机器人学习数据集与 RT-X 模型。Online，2023。

[34] S. Karamcheti、S. Nair、A. Balakrishna、P. Liang、T. Kollar 和 D. Sadigh。Prismatic VLM：研究视觉条件语言模型的设计空间。arXiv 预印本 arXiv:2402.07865，2024。

[35] Gemini Robotics Team、S. Abeyruwan、J. Ainslie、J.-B. Alayrac、M. G. Arenas、T. Armstrong、A. Balakrishna、R. Baruch、M. Bauza、M. Blokzijl 等。Gemini Robotics：将 AI 带入物理世界。arXiv 预印本 arXiv:2503.20020，2025。

[36] H. Zhen、X. Qiu、P. Chen、J. Yang、X. Yan、Y. Du、Y. Hong 和 C. Gan。3D-VLA：3D 视觉-语言-动作生成式世界模型。arXiv 预印本 arXiv:2403.09631，2024。

[37] D. Driess、F. Xia、M. S. M. Sajjadi、C. Lynch、A. Chowdhery、B. Ichter、A. Wahid、J. Tompson、Q. Vuong、T. Yu、W. Huang、Y. Chebotar、P. Sermanet、D. Duckworth、S. Levine、V. Vanhoucke、K. Hausman、M. Toussaint、M. Greff、A. Zeng、I. Mordatch 和 P. Florence。PaLM-E：具身多模态语言模型。在 International Conference on Machine Learning（ICML），2023。

[38] X. Li、M. Liu、H. Zhang、C. Yu、J. Xu、H. Wu、H. Dong、H. Hu、W. Zhan、H. Wu、Y. Han 和 T. Kong。视觉-语言基础模型作为有效的机器人模仿器。在 International Conference on Learning Representations（ICLR），2024。

[39] J. Huang、S. Yong、X. Ma、X. Linghu、P. Li、Y. Wang、Q. Li、S.-C. Zhu、B. Jia 和 S. Huang。3D 世界中的具身通用智能体。在 International Conference on Machine Learning（ICML），2024。

[40] M. Shridhar、L. Manuelli 和 D. Fox。Cliport：机器人操作中的“做什么”和“在哪里”通路。在 Conference on Robot Learning（CoRL），2022。

[41] C. Chi、S. Feng、Y. Du、Z. Xu、E. Cousineau、B. Burchfiel 和 S. Song。Diffusion Policy：通过动作扩散进行视觉运动策略学习。在 Robotics: Science and Systems（RSS），2023。

[42] T. Z. Zhao、V. Kumar、S. Levine 和 C. Finn。使用低成本硬件学习细粒度双臂操作。在 Robotics: Science and Systems（RSS），2023。

[43] OpenAI。介绍 GPT-5.2。Online，2025。


### Source page 20 / 源页面 20


> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> [44] S. Pichai, D. Hassabis, and K. Kavukcuoglu. A new era of intelligence with Gemini 3. Google Blog, 2025. [45] S. Bai, Y. Cai, R. Chen, K. Chen, X. Chen, Z. Cheng, L. Deng, W. Ding, C. Gao, C. Ge, W. Ge, Z. Guo, Q. Huang, J. Huang, F. Huang, B. Hui, et al. Qwen3-vl technical report. arXiv preprint arXiv:2511.21631, 2025. [46] Anthropic. Introducing Claude Sonnet 4.5. Online, 2025. [47] Meta. Llama 4 Herd. Meta Blog, 2025. [48] OpenAI. Gpt-4o system card. arXiv preprint arXiv:2410.21276, 2024. [49] Gemini Team, R. Anil, S. Borgeaud, J.-B. Alayrac, J. Yu, R. Soricut, J. Schalkwyk, A. M. Dai, A. Hauth, K. Millican, et al. Gemini: A family of highly capable multimodal models. arXiv preprint arXiv:2312.11805, 2023. [50] M. Deitke, C. Clark, S. Lee, R. Tripathi, Y. Yang, J. S. Park, M. Salehi, N. Muennighoff, K. Lo, L. Soldaini, et al. Molmo and pixmo: Open weights and open data for state-of-the-art vision-language models. In IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2025. [51] B. Chen, Z. Xu, S. Kirmani, B. Ichter, D. Sadigh, L. Guibas, and F. Xia. SpatialVLM: Endowing vision-language models with spatial reasoning capabilities. In IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2024. [52] OpenAI. Introducing deep research. OpenAI Blog, 2025. [53] Google. Gemini Deep Research. Google Blog, 2024. [54] J. Wu, Z. Deng, W. Li, Y. Liu, B. You, B. Li, Z. Ma, and Z. Liu. Mmsearch-r1: Incentivizing lmms to search. arXiv preprint arXiv:2506.20670, 2025. [55] X. Geng, P. Xia, Z. Zhang, X. Wang, Q. Wang, R. Ding, C. Wang, J. Wu, Y. Zhao, K. Li, et al. Webwatcher: Breaking new frontier of vision-language deep research agent. arXiv preprint arXiv:2508.05748, 2025. [56] W. Huang, Y. Zeng, Q. Wang, Z. Fang, S. Cao, Z. Chu, Q. Yin, S. Chen, Z. Yin, L. Chen, et al. Vision- deepresearch: Incentivizing deepresearch capability in multimodal large language models. arXiv preprint arXiv:2601.22060, 2026. [57] B. Jin, H. Zeng, Z. Yue, J. Yoon, S. Arik, D. Wang, H. Zamani, and J. Han. Search-r1: Training llms to reason and leverage search engines with reinforcement learning. arXiv preprint arXiv:2503.09516, 2025. [58] K. Li, Z. Zhang, H. Yin, L. Zhang, L. Ou, J. Wu, W. Yin, B. Li, Z. Tao, X. Wang, et al. Websailor: Navigating super-human reasoning for web agent. arXiv preprint arXiv:2507.02592, 2025. [59] G. R. Team, A. Abdolmaleki, S. Abeyruwan, J. Ainslie, J.-B. Alayrac, M. G. Arenas, A. Balakr- ishna, N. Batchelor, A. Bewley, J. Bingham, et al. Gemini robotics 1.5: Pushing the frontier of generalist robots with advanced embodied reasoning, thinking, and motion transfer. arXiv preprint arXiv:2510.03342, 2025. [60] S. Huang, Z. Jiang, H. Dong, Y. Qiao, P. Gao, and H. Li. Instruct2act: Mapping multi-modality instructions to robotic actions with large language model. arXiv preprint arXiv:2305.11176, 2023.

> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> [44] S. Pichai、D. Hassabis 和 K. Kavukcuoglu。借助 Gemini 3 开启智能新时代。Google Blog，2025。

[45] S. Bai、Y. Cai、R. Chen、K. Chen、X. Chen、Z. Cheng、L. Deng、W. Ding、C. Gao、C. Ge、W. Ge、Z. Guo、Q. Huang、J. Huang、F. Huang、B. Hui 等。Qwen3-VL 技术报告。arXiv 预印本 arXiv:2511.21631，2025。

[46] Anthropic。介绍 Claude Sonnet 4.5。Online，2025。

[47] Meta。Llama 4 Herd。Meta Blog，2025。

[48] OpenAI。GPT-4o 系统卡片。arXiv 预印本 arXiv:2410.21276，2024。

[49] Gemini Team、R. Anil、S. Borgeaud、J.-B. Alayrac、J. Yu、R. Soricut、J. Schalkwyk、A. M. Dai、A. Hauth、K. Millican 等。Gemini：一系列高能力多模态模型。arXiv 预印本 arXiv:2312.11805，2023。

[50] M. Deitke、C. Clark、S. Lee、R. Tripathi、Y. Yang、J. S. Park、M. Salehi、N. Muennighoff、K. Lo、L. Soldaini 等。Molmo 和 PixMo：面向先进视觉-语言模型的开放权重与开放数据。在 IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR），2025。

[51] B. Chen、Z. Xu、S. Kirmani、B. Ichter、D. Sadigh、L. Guibas 和 F. Xia。SpatialVLM：赋予视觉-语言模型空间推理能力。在 IEEE/CVF Conference on Computer Vision and Pattern Recognition（CVPR），2024。

[52] OpenAI。介绍 deep research。OpenAI Blog，2025。

[53] Google。Gemini Deep Research。Google Blog，2024。

[54] J. Wu、Z. Deng、W. Li、Y. Liu、B. You、B. Li、Z. Ma 和 Z. Liu。MMSearch-R1：激励 LMM 进行搜索。arXiv 预印本 arXiv:2506.20670，2025。

[55] X. Geng、P. Xia、Z. Zhang、X. Wang、Q. Wang、R. Ding、C. Wang、J. Wu、Y. Zhao、K. Li 等。WebWatcher：突破视觉-语言深度研究智能体的新前沿。arXiv 预印本 arXiv:2508.05748，2025。

[56] W. Huang、Y. Zeng、Q. Wang、Z. Fang、S. Cao、Z. Chu、Q. Yin、S. Chen、Z. Yin、L. Chen 等。Vision-DeepResearch：在多模态大语言模型中激励深度研究能力。arXiv 预印本 arXiv:2601.22060，2026。

[57] B. Jin、H. Zeng、Z. Yue、J. Yoon、S. Arik、D. Wang、H. Zamani 和 J. Han。Search-R1：通过强化学习训练 LLM 进行搜索引擎推理与利用。arXiv 预印本 arXiv:2503.09516，2025。

[58] K. Li、Z. Zhang、H. Yin、L. Zhang、L. Ou、J. Wu、W. Yin、B. Li、Z. Tao、X. Wang 等。WebSailor：探索超人类推理能力的网络智能体。arXiv 预印本 arXiv:2507.02592，2025。

[59] G. R. Team、A. Abdolmaleki、S. Abeyruwan、J. Ainslie、J.-B. Alayrac、M. G. Arenas、A. Balakrishna、N. Batchelor、A. Bewley、J. Bingham 等。Gemini Robotics 1.5：通过先进的具身推理、思考和运动迁移推动通用机器人的前沿。arXiv 预印本 arXiv:2510.03342，2025。

[60] S. Huang、Z. Jiang、H. Dong、Y. Qiao、P. Gao 和 H. Li。Instruct2Act：使用大语言模型将多模态指令映射到机器人动作。arXiv 预印本 arXiv:2305.11176，2023。


### Source page 21 / 源页面 21


> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> [61] S. Vemprala, R. Bonatti, A. Bucker, and A. Kapoor. ChatGPT for robotics: Design principles and model abilities. arXiv preprint arXiv:2306.17582, 2023. [62] Y. Mu, J. Chen, Q. Zhang, S. Chen, Q. Yu, C. Ge, R. Chen, Z. Liang, M. Hu, C. Tao, P. Sun, H. Yu, C. Yang, W. Shao, W. Wang, J. Dai, Y. Qiao, M. Ding, and P. Luo. RoboCodeX: Multimodal code generation for robotic behavior synthesis. arXiv preprint arXiv:2402.16117, 2024. [63] D. Surı́s, S. Menon, and C. Vondrick. ViperGPT: Visual inference via Python execution for reasoning. In IEEE/CVF International Conference on Computer Vision (ICCV), 2023. [64] W. Huang, C. Wang, R. Zhang, Y. Li, J. Wu, and L. Fei-Fei. Voxposer: Composable 3d value maps for robotic manipulation with language models. arXiv preprint arXiv:2307.05973, 2023. [65] A. Goldberg, K. Kondap, T. Qiu, Z. Ma, L. Fu, J. Kerr, H. Huang, K. Chen, K. Fang, and K. Goldberg. Blox-net: Generative design-for-robot-assembly using VLM supervision, physics simulation, and a robot with reset. In IEEE International Conference on Robotics and Automation (ICRA), 2025. [66] R. Li, Y. Zhou, Y. Zhu, K. Chen, J. Wang, S. Wang, K. Hu, M. Yu, B. Jiang, Z. Su, J. Ma, X. He, Y. Shen, Y. Yang, G. Ren, M. Yao, W. Wang, and Y. Mu. RoboClaw: An agentic framework for scalable long-horizon robotic tasks. arXiv preprint arXiv:2603.11558, 2026. [67] R. Lu, Y. Wu, E. Kou, L. Fu, W. Xiao, A. Mandlekar, Y. Xu, G. Shi, K. Goldberg, A. Chen, et al. ASPIRE: Agentic/skills discovery for robotics. arXiv preprint arXiv:2607.00272, 2026. [68] N. Shinn, F. Cassano, E. Berman, A. Gopinath, K. Narasimhan, and S. Yao. Reflexion: Language agents with verbal reinforcement learning. In Advances in Neural Information Processing Systems (NeurIPS), volume 36, 2023. [69] A. Madaan, N. Tandon, P. Gupta, S. Hallinan, L. Gao, S. Wiegreffe, U. Alon, N. Dziri, S. Prabhumoye, Y. Yang, et al. Self-refine: Iterative refinement with self-feedback. In Advances in Neural Information Processing Systems (NeurIPS), volume 36, 2023. [70] X. Chen, M. Lin, N. Schärli, and D. Zhou. Teaching large language models to self-debug. In Interna- tional Conference on Learning Representations (ICLR), 2024. [71] T. Yoneda, J. Fang, P. Li, H. Zhang, T. Jiang, S. Lin, B. Picker, D. Yunis, H. Mei, and M. R. Walter. Statler: State-maintaining language models for embodied reasoning and planning. In IEEE Interna- tional Conference on Robotics and Automation (ICRA), 2024. [72] M. Ahn, A. Brohan, N. Brown, Y. Chebotar, O. Cortes, B. David, C. Finn, C. Fu, K. Gopalakrishnan, K. Hausman, A. Herzog, D. Ho, J. Hsu, J. Ibarz, B. Ichter, A. Irpan, E. Jang, R. Jauregui Ruano, K. Jef- frey, S. Jesmonth, N. Joshi, R. Julian, D. Kalashnikov, Y. Kuang, K.-H. Lee, S. Levine, Y. Lu, L. Luu, C. Parada, P. Pastor, J. Quiambao, K. Rao, J. Reymann, M. Ryoo, G. Salazar, P. Sanketi, K. Sayed, J. Singh, S. Sontakke, A. Stone, C. Tan, H. Tran, V. Vanhoucke, S. Vega, Q. Vuong, C. Watkins, S. Welker, P. Wohlhart, J. Wu, F. Xia, T. Xiao, P. Xu, S. Xu, M. Yan, A. Zeng, and Y. Zheng. Do as I can, not as I say: Grounding language in robotic affordances. In Conference on Robot Learning (CoRL), 2022. [73] W. Huang, F. Xia, T. Xiao, H. Chan, J. Liang, P. Florence, A. Zeng, J. Tompson, I. Mordatch, Y. Cheb- otar, et al. Inner monologue: Embodied reasoning through planning with language models. arXiv preprint arXiv:2207.05608, 2022.

> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> [61] S. Vemprala、R. Bonatti、A. Bucker 和 A. Kapoor。ChatGPT for Robotics：设计原则与模型能力。arXiv 预印本 arXiv:2306.17582，2023。

[62] Y. Mu、J. Chen、Q. Zhang、S. Chen、Q. Yu、C. Ge、R. Chen、Z. Liang、M. Hu、C. Tao、P. Sun、H. Yu、C. Yang、W. Shao、W. Wang、J. Dai、Y. Qiao、M. Ding 和 P. Luo。RoboCodeX：用于机器人行为合成的多模态代码生成。arXiv 预印本 arXiv:2402.16117，2024。

[63] D. Surı́s、S. Menon 和 C. Vondrick。ViperGPT：通过 Python 执行进行视觉推理。在 IEEE/CVF International Conference on Computer Vision（ICCV），2023。

[64] W. Huang、C. Wang、R. Zhang、Y. Li、J. Wu 和 L. Fei-Fei。VoxPoser：使用语言模型为机器人操作组合 3D 价值图。arXiv 预印本 arXiv:2307.05973，2023。

[65] A. Goldberg、K. Kondap、T. Qiu、Z. Ma、L. Fu、J. Kerr、H. Huang、K. Chen、K. Fang 和 K. Goldberg。Blox-Net：利用 VLM 监督、物理仿真和带重置功能的机器人进行机器人装配生成式设计。在 IEEE International Conference on Robotics and Automation（ICRA），2025。

[66] R. Li、Y. Zhou、Y. Zhu、K. Chen、J. Wang、S. Wang、K. Hu、M. Yu、B. Jiang、Z. Su、J. Ma、X. He、Y. Shen、Y. Yang、G. Ren、M. Yao、W. Wang 和 Y. Mu。RoboClaw：用于可扩展长时域机器人任务的智能体框架。arXiv 预印本 arXiv:2603.11558，2026。

[67] R. Lu、Y. Wu、E. Kou、L. Fu、W. Xiao、A. Mandlekar、Y. Xu、G. Shi、K. Goldberg、A. Chen 等。ASPIRE：面向机器人的智能体式技能发现。arXiv 预印本 arXiv:2607.00272，2026。

[68] N. Shinn、F. Cassano、E. Berman、A. Gopinath、K. Narasimhan 和 S. Yao。Reflexion：具有言语强化学习的语言智能体。在 Advances in Neural Information Processing Systems（NeurIPS），第 36 卷，2023。

[69] A. Madaan、N. Tandon、P. Gupta、S. Hallinan、L. Gao、S. Wiegreffe、U. Alon、N. Dziri、S. Prabhumoye、Y. Yang 等。Self-Refine：利用自反馈进行迭代改进。在 Advances in Neural Information Processing Systems（NeurIPS），第 36 卷，2023。

[70] X. Chen、M. Lin、N. Schärli 和 D. Zhou。教导大语言模型进行自调试。在 International Conference on Learning Representations（ICLR），2024。

[71] T. Yoneda、J. Fang、P. Li、H. Zhang、T. Jiang、S. Lin、B. Picker、D. Yunis、H. Mei 和 M. R. Walter。Statler：用于具身推理和规划的状态维持语言模型。在 IEEE International Conference on Robotics and Automation（ICRA），2024。

[72] M. Ahn、A. Brohan、N. Brown、Y. Chebotar、O. Cortes、B. David、C. Finn、C. Fu、K. Gopalakrishnan、K. Hausman、A. Herzog、D. Ho、J. Hsu、J. Ibarz、B. Ichter、A. Irpan、E. Jang、R. Jauregui Ruano、K. Jeffrey、S. Jesmonth、N. Joshi、R. Julian、D. Kalashnikov、Y. Kuang、K.-H. Lee、S. Levine、Y. Lu、L. Luu、C. Parada、P. Pastor、J. Quiambao、K. Rao、J. Reymann、M. Ryoo、G. Salazar、P. Sanketi、K. Sayed、J. Singh、S. Sontakke、A. Stone、C. Tan、H. Tran、V. Vanhoucke、S. Vega、Q. Vuong、C. Watkins、S. Welker、P. Wohlhart、J. Wu、F. Xia、T. Xiao、P. Xu、S. Xu、M. Yan、A. Zeng 和 Y. Zheng。Do as I can, not as I say：将语言落地到机器人可供性。在 Conference on Robot Learning（CoRL），2022。

[73] W. Huang、F. Xia、T. Xiao、H. Chan、J. Liang、P. Florence、A. Zeng、J. Tompson、I. Mordatch、Y. Chebotar 等。Inner Monologue：通过使用语言模型进行规划实现具身推理。arXiv 预印本 arXiv:2207.05608，2022。


### Source page 22 / 源页面 22


> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> [74] Y. Mu, Q. Zhang, M. Hu, W. Wang, M. Ding, J. Jin, B. Wang, J. Dai, Y. Qiao, and P. Luo. Embod- iedGPT: Vision-language pre-training via embodied chain of thought. In Advances in Neural Informa- tion Processing Systems (NeurIPS), volume 36, 2023. [75] A. Zeng, M. Attarian, B. Ichter, K. Choromanski, A. Wong, S. Welker, F. Tombari, A. Purohit, M. Ryoo, V. Sindhwani, J. Lee, V. Vanhoucke, and P. Florence. Socratic models: Composing zero- shot multimodal reasoning with language. In International Conference on Learning Representations (ICLR), 2023. [76] B. Liu, Y. Jiang, X. Zhang, Q. Liu, S. Zhang, J. Biswas, and P. Stone. LLM+P: Empowering large language models with optimal planning proficiency. arXiv preprint arXiv:2304.11477, 2023. [77] Y. Chen, J. Arkin, C. Dawson, Y. Zhang, N. Roy, and C. Fan. AutoTAMP: Autoregressive task and motion planning with LLMs as translators and checkers. In IEEE International Conference on Robotics and Automation (ICRA), 2024. [78] K. Rana, J. Haviland, S. Garg, J. Abou-Chakra, I. Reid, and N. Suenderhauf. SayPlan: Grounding large language models using 3D scene graphs for scalable task planning. In Conference on Robot Learning (CoRL), 2023. [79] Z. Mandi, S. Jain, and S. Song. RoCo: Dialectic multi-robot collaboration with large language models. In IEEE International Conference on Robotics and Automation (ICRA), 2024.

> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> [74] Y. Mu、Q. Zhang、M. Hu、W. Wang、M. Ding、J. Jin、B. Wang、J. Dai、Y. Qiao 和 P. Luo。EmbodiedGPT：通过具身思维链进行视觉-语言预训练。在 Advances in Neural Information Processing Systems（NeurIPS），第 36 卷，2023。

[75] A. Zeng、M. Attarian、B. Ichter、K. Choromanski、A. Wong、S. Welker、F. Tombari、A. Purohit、M. Ryoo、V. Sindhwani、J. Lee、V. Vanhoucke 和 P. Florence。Socratic Models：将零样本多模态推理与语言组合。在 International Conference on Learning Representations（ICLR），2023。

[76] B. Liu、Y. Jiang、X. Zhang、Q. Liu、S. Zhang、J. Biswas 和 P. Stone。LLM+P：赋予大语言模型最优规划能力。arXiv 预印本 arXiv:2304.11477，2023。

[77] Y. Chen、J. Arkin、C. Dawson、Y. Zhang、N. Roy 和 C. Fan。AutoTAMP：将 LLM 作为翻译器和检查器的自回归任务与运动规划。在 IEEE International Conference on Robotics and Automation（ICRA），2024。

[78] K. Rana、J. Haviland、S. Garg、J. Abou-Chakra、I. Reid 和 N. Suenderhauf。SayPlan：使用 3D 场景图为可扩展任务规划落地大语言模型。在 Conference on Robot Learning（CoRL），2023。

[79] Z. Mandi、S. Jain 和 S. Song。RoCo：使用大语言模型进行辩证式多机器人协作。在 IEEE International Conference on Robotics and Automation（ICRA），2024。


### Source page 23 / 源页面 23


> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> A    File-Mediated REPL Protocol The harness of Section 2.2 implements the execution loop of Section 2.1 as a synchronous file-mediated Read-Eval-Print Loop (REPL). A long-running environment worker owns the live simulator state, while the planner Π interacts with it only through serialized primitive invocations and persisted observations. The planner does not access privileged simulator state, object poses, or controller internals. At turn t, the planner reads the current observation ot , the task language ℓ, and retrieved context from Task Specific Memory and Global Memory. It then emits one primitive invocation ct ∈ P by writing a JSON object to command.json. The object contains the primitive name in its action field and the corresponding keyword arguments. The worker consumes this file, executes the selected primitive in the live environment, and writes the next indexed observation ot+1 together with lightweight execution records. The planner waits for these files before selecting the next primitive. Thus, each physical action is followed by observation and diagnosis before the rollout continues. Table 7: Files used by the file-mediated REPL. The main text abstracts the observation as RGB-D and robot state; the appendix also lists diagnostic records used for synchronization and auditability. File or artifact                Role command.json               Planner-issued primitive invocation ct . state NN.json              Step-indexed task language, robot proprioception, and benchmark success signal. RGB-D / world-map files    Benchmark-specific perceptual evidence for semantic identification and metric re-grounding. log NN.json                Diagnostic record containing the accepted command, primitive status, step counts, and failure information when available. done NN.flag or terminal Synchronization signal indicating that the worker has finished the current file                       primitive. Task Specific Memory trace Append-only JSONL procedural memory for one task. Each line is one primitive command. Task Specific Memory sum- JSON semantic memory summarizing the outcome, strategy, recovery de- mary                       cisions, and failure modes. Global Memory              Cross-task success rules and failure models for using the primitive library. The index NN increases monotonically. The initial observation is written at NN=00; each executed primitive produces the next indexed state, perception files, and diagnostic log. These records make the rollout auditable without exposing oracle object coordinates to the planner. Task Specific Memory. Task Specific Memory stores the reusable structure of a solved task instance. It contains a procedural JSONL trace and a semantic JSON summary. The trace records what primitive invocations were issued; the summary records why the strategy worked and what should be avoided. A simplified summary is: {"task":"put the black bowl on the wooden tray", "success":true, "trace_file":"task_specific_memory_put_black_bowl_on_tray_s0.jsonl", "strategy":"use VLA for grasping, then analytic transport and release", "avoid":["do not reuse reference xyz values", "verify placement with the benchmark success signal"]} The paired procedural trace stores the primitive order:

> <span style="color:#F59E0B"><strong>Para. 23[CN]:</strong></span> **A 文件媒介 REPL 协议。** 第 2.2 节的 harness 以同步的、文件媒介 Read-Eval-Print Loop（REPL）实现第 2.1 节的执行循环。一个长期运行的环境工作器拥有仿真器的实时状态，而规划器 Π 只能通过序列化的基元调用和持久化观测与它交互。规划器无法访问特权仿真状态、物体位姿或控制器内部信息。在第 t 轮，规划器读取当前观测 $o_t$、任务语言 $\ell$，以及从任务特定记忆和全局记忆中检索的上下文。随后，它将一个基元调用 $c_t \in P$ 写入 `command.json`，以此发出调用。该对象在 `action` 字段中包含基元名称以及相应的关键字参数。工作器读取该文件，在实时环境中执行所选基元，并写入下一条带索引的观测 $o_{t+1}$ 及轻量级执行记录。规划器等待这些文件就绪后再选择下一个基元。因此，每个物理动作之后都会先进行观测和诊断，rollout 才会继续。

**表 7：文件媒介 REPL 使用的文件。** 正文将观测抽象为 RGB-D 和机器人状态；附录还列出了用于同步和可审计性的诊断记录。

| 文件或工件 | 作用 |
|---|---|
| `command.json` | 规划器发出的基元调用 $c_t$。 |
| `state_NN.json` | 按步索引的任务语言、机器人本体感知和基准成功信号。 |
| RGB-D / world-map 文件 | 用于语义识别和度量重新落地的、基准特定的感知证据。 |
| `log_NN.json` | 诊断记录，包含已接受的命令、基元状态、步数，以及可用时的失败信息。 |
| `done_NN.flag` 或 terminal 文件 | 表示工作器已完成当前基元的同步信号。 |
| Task Specific Memory trace | 单个任务的只追加 JSONL 程序记忆；每行是一个基元命令。 |
| Task Specific Memory summary | 总结结果、策略、恢复决策和失败模式的 JSON 语义记忆。 |
| Global Memory | 用于基元库的跨任务成功规则和失败模型。 |

索引 `NN` 单调递增。初始观测写入 `NN=00`；每个已执行基元都会产生下一条带索引的状态、感知文件和诊断日志。这些记录使 rollout 保持可审计，同时不会向规划器暴露预言式物体坐标。

**任务特定记忆。** Task Specific Memory 存储已解决任务实例的可复用结构。它包含一个程序化 JSONL 轨迹和一个语义 JSON 摘要。轨迹记录发出了哪些基元调用；摘要记录策略为何有效以及应当避免什么。一个简化的摘要为：

```json
{"task":"put the black bowl on the wooden tray", "success":true, "trace_file":"task_specific_memory_put_black_bowl_on_tray_s0.jsonl", "strategy":"use VLA for grasping, then analytic transport and release", "avoid":["do not reuse reference xyz values", "verify placement with the benchmark success signal"]}
```

配套的程序化轨迹存储基元顺序：


### Source page 24 / 源页面 24


> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> {"action":"vla_act","prompt":"grasp the black bowl","max_chunks":2} {"action":"move_to","xyz":[0.12,-0.08,0.92],"gripper":null} {"action":"release"} The trace is a task-level solution skeleton, not an open-loop trajectory. It records the ordering of an- alytic and VLA-backed primitives, the placement of VLA invocations, and the transition points between contact-rich execution, transport, release, and verification. Spatial arguments in the stored trace are treated as reference-scene bindings. At deployment time, the planner reuses the memory structure but re-grounds objects, fixtures, support surfaces, and target poses from the current observation. Global Memory. Global Memory stores task-independent operating knowledge for the primitive library. diagnose before retrying. A compact example is: Success rule: Use VLA primitives for contact-rich phases such as irregular grasping or fixture interaction. After a stable grasp, prefer analytic motion for long transport and precise placement. Failure model: If the gripper closes but the object does not move with the end effector, treat the attempt as an empty grasp. Re-localize the object and re-stage before retrying. Failure model: Do not terminate from visual proximity alone. Check the benchmark success signal and the latest execution record. Iterative memory construction. Memory is constructed during interaction rather than written only after the rollout. After each primitive, the planner reads the new observation and diagnostic record, then classifies the outcome as progress, recoverable failure, or unrecoverable failure. Successful rollouts are stored as Task Specific Memory. Recoverable failures remain in the trace and are explained in the semantic summary, so that subsequent steps document the correction. Failed attempts are also retained as negative evidence and may contribute failure models to Global Memory. Across attempts, the memory is refined rather than simply accumulated. A later attempt can replace the procedural trace if it yields a shorter or more reliable solution, while earlier failure observations remain useful as constraints on future planning. This separation lets Harness VLA transfer how a task should be solved without replaying where objects happened to be in the reference scene. B    Primitive Vocabulary and Environment-Specific Extensions This appendix expands the primitive vocabulary of Section 2.3. We use the same primitive names across all benchmarks. Differences across environments are expressed only through availability, arm binding, and implementation backend; they are not treated as new primitive names unless the embodiment exposes a new degree of freedom.

> <span style="color:#F59E0B"><strong>Para. 24[CN]:</strong></span> ```json
{"action":"vla_act","prompt":"grasp the black bowl","max_chunks":2}
{"action":"move_to","xyz":[0.12,-0.08,0.92],"gripper":null}
{"action":"release"}
```

该轨迹是任务级解决方案骨架，而不是开环轨迹。它记录了解析基元和 VLA 支持基元的顺序、VLA 调用的位置，以及接触密集执行、运输、释放和验证之间的转换点。存储轨迹中的空间参数被视为参考场景绑定。在部署时，规划器复用记忆结构，但从当前观测中重新落地物体、装置、支撑表面和目标位姿。

**全局记忆。** Global Memory 存储与任务无关的基元库操作知识。应在重试前进行诊断。一个简短示例如下：

**成功规则：** 对不规则抓取或装置交互等接触密集阶段使用 VLA 基元。获得稳定抓取后，长距离运输和精确放置优先使用解析运动。

**失败模型：** 如果夹爪闭合但物体没有随末端执行器移动，则将这次尝试视为空抓取。重新定位物体并重新定位机器人后再重试。

**失败模型：** 不要仅凭视觉接近就终止。检查基准成功信号和最新执行记录。

**迭代式记忆构建。** 记忆是在交互过程中构建的，而不是只在 rollout 结束后写入。每个基元执行后，规划器读取新的观测和诊断记录，然后将结果分类为进展、可恢复失败或不可恢复失败。成功 rollout 被存入 Task Specific Memory。可恢复失败保留在轨迹中，并在语义摘要中解释，使后续步骤记录纠正过程。失败尝试也会作为负面证据保留，并可能为 Global Memory 贡献失败模型。在多次尝试之间，记忆会被细化，而不是简单累积。如果后续尝试产生更短或更可靠的解决方案，可以替换程序化轨迹；同时，早期失败观测仍可作为未来规划的约束。这种分离使 Harness VLA 能够迁移“任务应该如何解决”，而无需重放物体在参考场景中恰好处于何处。

**B 基元词汇与环境特定扩展。** 本附录扩展第 2.3 节的基元词汇。所有基准使用相同的基元名称。环境之间的差异只通过可用性、机械臂绑定和实现后端表达；除非具身形态暴露了新的自由度，否则不将其视为新的基元名称。


### Source page 25 / 源页面 25


> <span style="color:#3B82F6"><strong>Para. 25:</strong></span> Table 8: Primitive availability across the three benchmark embodiments. The exploratory RESET utility supports bootstrapping and is not counted as a manipulation primitive. Primitive        LIBERO      RoboCasa365      RoboTwin C2R MOVE TO             yes           yes              yes MOVE POSE           yes     via composition         – ROTATE WRIST        yes            –               yes ROTATE PITCH        yes           yes               – SET GRIPPER         yes           yes              yes RELEASE             yes           yes              yes VLA ACT             yes           yes              yes NAVIGATE TO          –            yes               – MOVE BASE            –            yes               – arm binding          –             –               yes Universal analytic primitives. MOVE TO is the shared end-effector transport primitive: it takes a world- frame Cartesian target and delegates to the solver available in the current environment. The internal backend may be an operational-space servo, a Jacobian-based controller, or an IK planner, but the exposed primitive semantics are identical. MOVE POSE extends MOVE TO by co-varying position with an orientation com- ponent such as pitch; when an environment does not expose it directly, the same behavior is expressed as a short composition of ROTATE PITCH and MOVE TO. ROTATE WRIST and ROTATE PITCH apply yaw and pitch set-points while holding the current spatial position. SET GRIPPER drives the gripper to an open or closed state, and RELEASE is the corresponding open-gripper primitive with a release post-condition. Environment-specific gripper conventions are hidden behind the primitive interface. Mobile-base and bimanual details. RoboCasa365 adds two mobile-base primitives because kitchen- scale tasks require staging outside a fixed-arm workspace. NAVIGATE TO is a composite primitive that drives the base toward a world-frame planar goal, while MOVE BASE is an atomic primitive that applies a local base-velocity set-point for fine repositioning. RoboTwin C2R adds no new manipulation primitive name; instead, each primitive can be bound to the left arm, right arm, or a bimanual task pattern through the arm argument. Handover-style tasks are therefore represented as compositions of VLA ACT, analytic transport, and RELEASE under this dual-arm binding rather than as a separate primitive. VLA ACT . VLA ACT is the single learned primitive in the vocabulary. It binds to the frozen VLA used by the current benchmark and executes action chunks conditioned on a prompt and live observations. The planner configures a stop predicate τ , which may correspond to a lift-and-grasp condition, a contact-state condition, a benchmark predicate, or a chunk budget. The same primitive therefore covers grasping, place- ment, fixture actuation, insertion, and bimanual contact while preserving the planner’s responsibility for semantic grounding, spatial re-binding, navigation, and re-staging. JSON invocation examples.      All primitives share a compact JSON command format. Representative calls are: {"action": "move to",     "xyz": [-0.101, 0.202, 1.05], "arm": "auto", "gripper": "open", "tol": 0.012, "max_steps": 80} {"action": "navigate to", "xy": [1.20, -0.35], "tol": 0.05} {"action": "move base",   "forward": 0.10, "lateral": 0.00, "turn": -0.15, "steps": 12}

> <span style="color:#F59E0B"><strong>Para. 25[CN]:</strong></span> **表 8：三种基准具身形态中的基元可用性。** 探索性的 RESET 工具用于引导，不计为操作基元。

| 基元 | LIBERO | RoboCasa365 | RoboTwin C2R |
|---|---|---|---|
| MOVE TO | 是 | 是 | 是 |
| MOVE POSE | 是 | 通过组合实现 | — |
| ROTATE WRIST | 是 | — | 是 |
| ROTATE PITCH | 是 | 是 | — |
| SET GRIPPER | 是 | 是 | 是 |
| RELEASE | 是 | 是 | 是 |
| VLA ACT | 是 | 是 | 是 |
| NAVIGATE TO | — | 是 | — |
| MOVE BASE | — | 是 | — |
| 机械臂绑定 | — | — | 是 |

**通用解析基元。** MOVE TO 是共享的末端执行器运输基元：它接收世界坐标系中的笛卡尔目标，并委托给当前环境中可用的求解器。内部后端可以是操作空间伺服、基于 Jacobian 的控制器或 IK 规划器，但暴露的基元语义保持一致。MOVE POSE 通过共同改变位置和 pitch 等姿态分量扩展 MOVE TO；当环境不直接暴露该基元时，可用 ROTATE PITCH 与 MOVE TO 的短组合表达相同的行为。ROTATE WRIST 和 ROTATE PITCH 在保持当前空间位置的同时施加 yaw 和 pitch 设定值。SET GRIPPER 将夹爪驱动到打开或闭合状态，RELEASE 则是带释放后置条件的相应开夹爪基元。环境特定的夹爪约定被隐藏在基元接口之后。

**移动底座与双臂细节。** RoboCasa365 增加两个移动底座基元，因为厨房尺度任务需要在固定机械臂工作空间之外进行定位。NAVIGATE TO 是将底座驱动到世界坐标系平面目标附近的复合基元，MOVE BASE 是施加局部底座速度设定值以精细重新定位的原子基元。RoboTwin C2R 不增加新的操作基元名称；相反，每个基元都可以通过 `arm` 参数绑定到左臂、右臂或双臂任务模式。因此，交接类任务表示为在双臂绑定下组合 VLA ACT、解析运输和 RELEASE，而不是表示为独立基元。

**VLA ACT。** VLA ACT 是词汇中的唯一学习型基元。它绑定到当前基准所使用的冻结 VLA，并根据提示词和实时观测执行动作块。规划器配置停止谓词 τ，该谓词可以对应抬升并抓取条件、接触状态条件、基准谓词或动作块预算。因此，同一个基元可以覆盖抓取、放置、装置驱动、插入和双臂接触，同时保持规划器对语义落地、空间重新绑定、导航和重新定位的责任。

**JSON 调用示例。** 所有基元共享紧凑的 JSON 命令格式。代表性调用为：

```json
{"action": "move to", "xyz": [-0.101, 0.202, 1.05], "arm": "auto", "gripper": "open", "tol": 0.012, "max_steps": 80}
{"action": "navigate to", "xy": [1.20, -0.35], "tol": 0.05}
{"action": "move base", "forward": 0.10, "lateral": 0.00, "turn": -0.15, "steps": 12}
{"action": "vla act", "prompt": "grasp the black bowl", "arm": "auto", "max_chunks": 30, "stop": "object_lifted"}
```

具体数值容差和停止谓词因基准而异，但规划器始终通过这些基元名称交互。


### Source page 26 / 源页面 26


> <span style="color:#3B82F6"><strong>Para. 26:</strong></span> Figure 8: Overview of representative environments across the four benchmark families used in our evalua- tion. Each benchmark captures a distinct manipulation setting: structured tabletop manipulation (LIBERO), robustness under distribution shift (LIBERO-Pro), long-horizon kitchen manipulation (RoboCasa365), and bimanual manipulation under clean-to-randomized settings (RoboTwin C2R). {"action": "vla act",     "prompt": "grasp the black bowl", "arm": "auto", "max_chunks": 30, "stop": "object_lifted"} The exact numerical tolerances and stop predicates are benchmark-specific, but the planner always interacts through these primitive names. C     Details about the Evaluation Benchmark This appendix records the benchmark composition, task splits, rollout protocol, and success criteria used in our evaluation. We evaluate on four benchmark families: LIBERO, LIBERO-Pro, RoboCasa365, and RoboTwin C2R. LIBERO, LIBERO-Pro, and RoboCasa365 use a few-shot protocol in which seed s0 (seed 0) for each task serves only as the exploratory reference seed for Task Specific Memory construction. On this seed, the agent searches for a successful primitive sequence and stores the resulting audit summary and JSONL command trace as Task Specific Memory. Seed s0 is not counted in reported evaluation. Reported evaluation rollouts are run on held-out seeds that retrieve and re-ground the corresponding Task Specific Memory under new initial states. RoboTwin C2R uses a separate zero-shot clean-to-randomized protocol. Across all benchmarks, task success is determined by the benchmark-provided binary completion pred- icate. A rollout is counted as successful if the task completion predicate is satisfied before the episode horizon or maximum step budget is exhausted. Primitive-level post-conditions, such as the return condition of VLA ACT or RELEASE, only determine when an individual primitive returns control to the planner; they are not used as substitutes for the final task success predicate. C.1   LIBERO Evaluation Benchmark LIBERO [19] is a language-conditioned manipulation benchmark organized into multiple task suites. We evaluate on four standard suites: LIBERO-S PATIAL, LIBERO-O BJECT, LIBERO-G OAL, and LIBERO- 10. LIBERO-S PATIAL contains tasks that vary spatial relations, LIBERO-O BJECT varies the target object identity, LIBERO-G OAL varies the goal predicate under related scenes, and LIBERO-10 contains longer- horizon compositional manipulation tasks.

> <span style="color:#F59E0B"><strong>Para. 26[CN]:</strong></span> **图 8：评估中使用的四类基准环境代表性概览。** 每个基准对应不同的操作设置：结构化桌面操作（LIBERO）、分布变化下的稳健性（LIBERO-Pro）、长时域厨房操作（RoboCasa365），以及干净到随机化设置下的双臂操作（RoboTwin C2R）。

```json
{"action": "vla act", "prompt": "grasp the black bowl", "arm": "auto", "max_chunks": 30, "stop": "object_lifted"}
```

具体数值容差和停止谓词是基准特定的，但规划器始终通过这些基元名称交互。

**C 关于评估基准的细节。** 本附录记录评估中使用的基准组成、任务划分、rollout 协议和成功标准。我们在四类基准上进行评估：LIBERO、LIBERO-Pro、RoboCasa365 和 RoboTwin C2R。LIBERO、LIBERO-Pro 和 RoboCasa365 使用少样本协议：每个任务的种子 s0（种子 0）只作为构建任务特定记忆的探索参考种子。在该种子上，智能体搜索成功的基元序列，并将所得审计摘要和 JSONL 命令轨迹存储为任务特定记忆。种子 s0 不计入报告的评估。报告的评估 rollout 在留出种子上运行，这些种子会在新的初始状态下检索并重新落地相应的任务特定记忆。RoboTwin C2R 使用独立的零样本从干净到随机化协议。

在所有基准中，任务成功由基准提供的二值完成谓词决定。如果在 episode 时域结束或最大步数预算耗尽之前满足任务完成谓词，则该 rollout 计为成功。基元级后置条件，例如 VLA ACT 或 RELEASE 的返回条件，只决定单个基元何时将控制权返回规划器；它们不能替代最终任务成功谓词。

**C.1 LIBERO 评估基准。** LIBERO [19] 是一个语言条件操作基准，组织为多个任务套件。我们评估四个标准套件：LIBERO-SPATIAL、LIBERO-OBJECT、LIBERO-GOAL 和 LIBERO-10。LIBERO-SPATIAL 包含改变空间关系的任务，LIBERO-OBJECT 改变目标物体身份，LIBERO-GOAL 在相关场景中改变目标谓词，LIBERO-10 则包含更长时域的组合式操作任务。


### Source page 27 / 源页面 27


> <span style="color:#3B82F6"><strong>Para. 27:</strong></span> Each suite contains 10 language-conditioned tasks. For each task, seed s0 (seed 0) is used only to explore the task and construct Task Specific Memory. Reported evaluation uses ten held-out seeds, denoted s1 –s10 , which retrieve this Task Specific Memory and ground it under new initial states. Thus, each LIBERO suite contains 10 tasks × 10 evaluation seeds = 100 reported rollouts, and the four suites contain 400 reported rollouts in total. Table 9: LIBERO evaluation protocol. Suite                  Tasks    Eval seeds per task    Reported rollouts LIBERO-S PATIAL         10               10                   100 LIBERO-O BJECT          10               10                   100 LIBERO-G OAL            10               10                   100 LIBERO-10               10               10                   100 Total                   40                  –                 400 Success rates are computed using the predicate-based rule defined at the beginning of this appendix. C.2   LIBERO-Pro Evaluation Benchmark LIBERO-Pro [20] extends the LIBERO task families with controlled perturbations. We evaluate four task families: S PATIAL, O BJECT, G OAL, and LIBERO-10. Each task family is evaluated under two perturbation settings, denoted T and S. T refers to the task or instruction-redirection setting, where the instruction is redirected to another valid target object or goal condition. S refers to the swap or position-swap setting, where object initial positions are swapped or rearranged while the instruction remains fixed. We evaluate eight LIBERO-Pro cells: S PATIAL -T, S PATIAL -S, O BJECT-T, O BJECT-S, G OAL -T, G OAL - S, LIBERO-10-T, and LIBERO-10-S. Each cell contains 10 tasks. As in LIBERO, seed s0 (seed 0) is used only to explore the task and construct Task Specific Memory; reported evaluation uses seeds s1 –s10 , which retrieve the stored Task Specific Memory and ground it under new initial states. Each cell therefore contains 10 tasks × 10 evaluation seeds = 100 reported rollouts, for a total of 800 reported rollouts. Table 10: LIBERO-Pro evaluation protocol. Evaluation cell     Tasks     Eval seeds per task    Reported rollouts S PATIAL -T         10                10                  100 S PATIAL -S         10                10                  100 O BJECT-T           10                10                  100 O BJECT-S           10                10                  100 G OAL -T            10                10                  100 G OAL -S            10                10                  100 LIBERO-10-T         10                10                  100 LIBERO-10-S         10                10                  100 Total                80                –                   800 Success rates are computed using the predicate-based rule defined at the beginning of this appendix.

> <span style="color:#F59E0B"><strong>Para. 27[CN]:</strong></span> 每个套件包含 10 个语言条件任务。对于每个任务，种子 s0（种子 0）仅用于探索任务并构建任务特定记忆。报告的评估使用 10 个留出种子，记为 s1–s10；这些种子会检索任务特定记忆，并在新的初始状态下对其进行落地。因此，每个 LIBERO 套件包含 10 个任务 × 10 个评估种子 = 100 个报告 rollout，四个套件合计 400 个报告 rollout。

**表 9：LIBERO 评估协议。**

| 套件 | 任务数 | 每任务评估种子数 | 报告 rollout 数 |
|---|---:|---:|---:|
| LIBERO-SPATIAL | 10 | 10 | 100 |
| LIBERO-OBJECT | 10 | 10 | 100 |
| LIBERO-GOAL | 10 | 10 | 100 |
| LIBERO-10 | 10 | 10 | 100 |
| 总计 | 40 | — | 400 |

成功率使用本附录开头定义的基于谓词的规则计算。

**C.2 LIBERO-Pro 评估基准。** LIBERO-Pro [20] 通过受控扰动扩展 LIBERO 任务族。我们评估四个任务族：SPATIAL、OBJECT、GOAL 和 LIBERO-10。每个任务族都在两种扰动设置下评估，记为 T 和 S。T 表示任务或指令重定向设置，即指令被重定向到另一个有效的目标物体或目标条件。S 表示交换或位置交换设置，即在指令保持不变的同时交换或重新排列物体的初始位置。

我们评估八个 LIBERO-Pro 单元：SPATIAL-T、SPATIAL-S、OBJECT-T、OBJECT-S、GOAL-T、GOAL-S、LIBERO-10-T 和 LIBERO-10-S。每个任务族单元包含 10 个任务。与 LIBERO 一样，种子 s0（种子 0）仅用于探索任务并构建任务特定记忆；报告的评估使用种子 s1–s10，检索存储的任务特定记忆并在新的初始状态下对其进行落地。因此，每个单元包含 10 个任务 × 10 个评估种子 = 100 个报告 rollout，八个单元共计 800 个报告 rollout。

**表 10：LIBERO-Pro 评估协议。**

| 评估单元 | 任务数 | 每任务评估种子数 | 报告 rollout 数 |
|---|---:|---:|---:|
| SPATIAL-T | 10 | 10 | 100 |
| SPATIAL-S | 10 | 10 | 100 |
| OBJECT-T | 10 | 10 | 100 |
| OBJECT-S | 10 | 10 | 100 |
| GOAL-T | 10 | 10 | 100 |
| GOAL-S | 10 | 10 | 100 |
| LIBERO-10-T | 10 | 10 | 100 |
| LIBERO-10-S | 10 | 10 | 100 |
| 总计 | 80 | — | 800 |

成功率使用本附录开头定义的基于谓词的规则计算。


### Source page 28 / 源页面 28


> <span style="color:#3B82F6"><strong>Para. 28:</strong></span> C.3    RoboCasa Evaluation Benchmark RoboCasa365 extends the evaluation to kitchen household manipulation. We use the RoboCasa365 target50 split, which consists of three task groups: ATOMIC -S EEN, C OMPOSITE -S EEN, and C OMPOSITE -U NSEEN. ATOMIC -S EEN contains 18 atomic tasks corresponding to short-horizon kitchen operations. C OMPOSITE - S EEN contains 16 composite tasks whose templates are also present in the pretraining set. C OMPOSITE - U NSEEN contains 16 composite tasks whose templates are held out from pretraining and appear only in target evaluation. Here, “seen” and “unseen” refer to whether the task template appears in the pretraining set, not whether the exact episode, trajectory, or scene has been observed. RoboCasa365 uses a split-specific few-shot seed protocol. In each split, seed s0 (seed 0) is used only to explore the task and construct Task Specific Memory. Reported evaluation uses held-out seeds: ATOMIC - S EEN uses seeds s1 –s10 , while C OMPOSITE -S EEN and C OMPOSITE -U NSEEN use seeds s1 –s5 . These held-out seeds retrieve and ground the corresponding Task Specific Memory under new initial states. Thus, ATOMIC -S EEN contains 18×10 = 180 reported rollouts, C OMPOSITE -S EEN contains 16×5 = 80 reported rollouts, and C OMPOSITE -U NSEEN contains 16 × 5 = 80 reported rollouts. The RoboCasa365 target50 evaluation contains 340 reported rollouts under this split-specific few-shot protocol. Table 11: RoboCasa365 evaluation protocol. Split                      Tasks      Eval seeds per task   Reported rollouts ATOMIC -S EEN                 18                10                 180 C OMPOSITE -S EEN             16                5                  80 C OMPOSITE -U NSEEN           16                 5                  80 Total                         50                –                  340 Success rates are computed using the predicate-based rule defined at the beginning of this appendix. C.4    RoboTwin Clean-to-Randomized Evaluation Benchmark RoboTwin C2R is a bimanual manipulation benchmark with 50 tasks. The task set covers pick-and-place, stacking, ordering, handover, dual-arm transport, articulated-object interaction, pressing and clicking, rota- tion, scanning, and container-placement behaviors. RoboTwin C2R uses a separate Clean-to-Randomized protocol. For each task, the Task Specific Mem- ory trace is obtained from one official scripted-expert-verified seed in the demo clean setting. Evaluation is then performed directly in the official demo randomized setting on five scripted-expert-verified ran- domized seeds. The expert verification step is used only to ensure that the sampled task instances are feasible under the official task definition; it is independent of our method and does not use Harness VLA rollouts for seed selection. No additional trace search, fine-tuning, or task-level adaptation is performed in the ran- domized setting. This protocol evaluates zero-shot transfer from a clean-setting trace to randomized task instances. We evaluate all 50 RoboTwin C2R tasks. Each task is evaluated on 5 seeds in the demo randomized setting, resulting in 50 × 5 = 250 reported rollouts. Table 12: RoboTwin clean-to-randomized evaluation protocol. Protocol           Tasks       Eval seeds per task   Reported rollouts RoboTwin C2R         50                 5                  250

> <span style="color:#F59E0B"><strong>Para. 28[CN]:</strong></span> **C.3 RoboCasa 评估基准。** RoboCasa365 将评估扩展到家庭厨房操作。我们使用 RoboCasa365 target50 划分，其中包含三个任务组：ATOMIC-SEEN、COMPOSITE-SEEN 和 COMPOSITE-UNSEEN。ATOMIC-SEEN 包含 18 个对应短时域厨房操作的原子任务。COMPOSITE-SEEN 包含 16 个复合任务，其模板也出现在预训练集合中。COMPOSITE-UNSEEN 包含 16 个复合任务，其模板从预训练中留出，只在目标评估中出现。这里的“seen”和“unseen”指任务模板是否出现在预训练集合中，而不是指具体 episode、轨迹或场景是否曾被观测过。

RoboCasa365 使用按划分区分的少样本种子协议。在每个划分中，种子 s0（种子 0）仅用于探索任务并构建任务特定记忆。报告的评估使用留出种子：ATOMIC-SEEN 使用种子 s1–s10，而 COMPOSITE-SEEN 和 COMPOSITE-UNSEEN 使用种子 s1–s5。这些留出种子会在新的初始状态下检索并落地相应的任务特定记忆。因此，ATOMIC-SEEN 包含 18×10 = 180 个报告 rollout，COMPOSITE-SEEN 包含 16×5 = 80 个报告 rollout，COMPOSITE-UNSEEN 包含 16×5 = 80 个报告 rollout。RoboCasa365 target50 评估在该按划分区分的少样本协议下包含 340 个报告 rollout。

**表 11：RoboCasa365 评估协议。**

| 划分 | 任务数 | 每任务评估种子数 | 报告 rollout 数 |
|---|---:|---:|---:|
| ATOMIC-SEEN | 18 | 10 | 180 |
| COMPOSITE-SEEN | 16 | 5 | 80 |
| COMPOSITE-UNSEEN | 16 | 5 | 80 |
| 总计 | 50 | — | 340 |

成功率使用本附录开头定义的基于谓词的规则计算。

**C.4 RoboTwin 从干净到随机化的评估基准。** RoboTwin C2R 是一个包含 50 个任务的双臂操作基准。任务集合覆盖抓取与放置、堆叠、排序、交接、双臂运输、关节物体交互、按压与点击、旋转、扫描和容器放置行为。

RoboTwin C2R 使用独立的 Clean-to-Randomized 协议。对于每个任务，任务特定记忆轨迹来自 demo clean 设置中的一个官方脚本专家验证种子。随后直接在官方 demo randomized 设置的 5 个脚本专家验证随机化种子上进行评估。专家验证步骤仅用于确保采样任务实例在官方任务定义下可行；它独立于我们的方法，且不会使用 Harness VLA rollout 选择种子。在随机化设置中不进行额外轨迹搜索、微调或任务级适配。该协议评估从干净设置轨迹到随机化任务实例的零样本迁移。

我们评估全部 50 个 RoboTwin C2R 任务。每个任务在 demo randomized 设置下使用 5 个种子，得到 50 × 5 = 250 个报告 rollout。

**表 12：RoboTwin 从干净到随机化的评估协议。**

| 协议 | 任务数 | 每任务评估种子数 | 报告 rollout 数 |
|---|---:|---:|---:|
| RoboTwin C2R | 50 | 5 | 250 |


### Source page 29 / 源页面 29


> <span style="color:#3B82F6"><strong>Para. 29:</strong></span> Success rates are computed using the predicate-based rule defined at the beginning of this appendix, with the completion predicate provided by the official RoboTwin C2R task-specific evaluator. C.5   Benchmark Summary Table 13 summarizes the scale of each evaluation benchmark. LIBERO and LIBERO-Pro use seed s0 (seed 0) only to construct Task Specific Memory and report evaluation on ten held-out seeds s1 –s10 per task. RoboCasa365 uses the same reference-seed convention with split-specific evaluation seeds: s1 –s10 for ATOMIC -S EEN and s1 –s5 for the two composite splits. RoboTwin C2R uses clean-to-randomized evaluation where the Task Specific Memory is obtained from one expert-verified demo clean seed and evaluated on expert-verified demo randomized seeds. Table 13: Summary of evaluation benchmarks. Benchmark          Tasks    Trials/task   Reported rollouts LIBERO               40         10              400 LIBERO-Pro           80         10              800 RoboCasa365          50       10/5/5            340 RoboTwin C2R         50          5              250 D     VLA Model Instantiations We instantiate different vision-language-action models across benchmarks, which are uniformly abstracted as the single contact-rich primitive VLA ACT within the Harness VLA framework. D.1   πRLinf : RLinf-released LIBERO checkpoint For LIBERO and LIBERO-Pro, we use the RLinf-released pi05 libero130 fullshot checkpoint, denoted πRLinf , as the frozen vision-language-action policy. It is based on the π0.5 architecture, and we directly adopt this official π0.5 -SFT checkpoint as a frozen VLA ACT contact-rich execution primitive within the Harness VLA framework. Architecture. πRLinf follows the π0.5 vision-language-action architecture, which encodes multimodal in- puts including visual observations It , language instructions ℓ, and robot state qt into a unified transformer representation. The model is initialized from a pretrained vision-language backbone and aligned to robot action spaces via supervised learning. Consistent with π0.5 , πRLinf supports hierarchical inference, where high-level semantic subtask predic- tion and low-level action generation are jointly modeled within a single policy. Action Modeling. πRLinf adopts the two-stage inference paradigm introduced in π0.5 . Given an obser- vation and language instruction, the model first predicts a high-level subtask ℓ̂ (e.g., “pick up the plate”), which is then used to condition low-level action generation. The low-level policy produces continuous action chunks at:t+H , represented either via FAST tokeniza- tion or flow-based continuous modeling, enabling stable contact-rich manipulation.

> <span style="color:#F59E0B"><strong>Para. 29[CN]:</strong></span> 成功率使用本附录开头定义的基于谓词的规则计算，完成谓词由官方 RoboTwin C2R 任务特定评估器提供。

**C.5 基准汇总。** 表 13 汇总了各评估基准的规模。LIBERO 和 LIBERO-Pro 仅使用种子 s0（种子 0）构建任务特定记忆，并报告每个任务在 10 个留出种子 s1–s10 上的评估结果。RoboCasa365 使用相同的参考种子约定，并按划分设置评估种子：ATOMIC-SEEN 使用 s1–s10，两个复合划分使用 s1–s5。RoboTwin C2R 使用从干净到随机化的评估：任务特定记忆来自一个专家验证的 demo clean 种子，并在专家验证的 demo randomized 种子上评估。

**表 13：评估基准汇总。**

| 基准 | 任务数 | 每任务试验数 | 报告 rollout 数 |
|---|---:|---:|---:|
| LIBERO | 40 | 10 | 400 |
| LIBERO-Pro | 80 | 10 | 800 |
| RoboCasa365 | 50 | 10/5/5 | 340 |
| RoboTwin C2R | 50 | 5 | 250 |

**D VLA 模型实例化。** 我们在不同基准上实例化不同的视觉-语言-动作模型，并在 Harness VLA 框架内将它们统一抽象为单一的接触密集基元 VLA ACT。

**D.1 π_RLinf：RLinf 发布的 LIBERO 检查点。** 对于 LIBERO 和 LIBERO-Pro，我们使用 RLinf 发布的 pi05 libero130 fullshot 检查点，记为 π_RLinf，作为冻结的视觉-语言-动作策略。该检查点基于 π0.5 架构；在 Harness VLA 框架中，我们直接将官方 π0.5-SFT 检查点作为冻结的 VLA ACT 接触密集执行基元使用。

**架构。** π_RLinf 遵循 π0.5 的视觉-语言-动作架构，将视觉观测 $I_t$、语言指令 $\ell$ 和机器人状态 $q_t$ 等多模态输入编码为统一的 Transformer 表示。模型从预训练视觉-语言主干初始化，并通过监督学习与机器人动作空间对齐。与 π0.5 一致，π_RLinf 支持层级推理：高层语义子任务预测与低层动作生成在同一策略中联合建模。

**动作建模。** π_RLinf 采用 π0.5 引入的两阶段推理范式。给定观测和语言指令，模型首先预测高层子任务 $\hat{\ell}$（例如“拿起盘子”），再以此为条件生成低层动作。低层策略产生连续动作块 $a_{t:t+H}$，可通过 FAST tokenization 或基于 flow 的连续建模表示，从而实现稳定的接触密集操作。


### Source page 30 / 源页面 30


> <span style="color:#3B82F6"><strong>Para. 30:</strong></span> Training. The model is supervised fine-tuned on the LIBERO-130 dataset following the π0.5 training protocol, resulting in the official π0.5 -SFT checkpoint. In this work, no additional training or adaptation is performed, and the model is used in a fully frozen manner during evaluation. Performance. On the LIBERO benchmark, πRLinf achieves a success rate of 95.3%, demonstrating strong in-distribution manipulation capability. On LIBERO-Pro, which introduces instruction perturbations and compositional variations, performance drops to 50.0%, indicating sensitivity to distribution shifts. Role in This Work. In this paper, πRLinf is used as a frozen low-level execution module within the Harness VLA framework, serving as the contact-rich manipulation primitive for LIBERO and LIBERO-Pro tasks. D.2   RLDX-1 RLDX-1 is used in RoboCasa365 for kitchen manipulation tasks. It is a large-scale vision-language-action (VLA) foundation model designed for general dexterous manipulation across diverse robotic embodiments. In this work, we directly use the official RLDX-1 checkpoint and keep the model fully frozen during evalu- ation, treating it as a VLA ACT contact-rich execution primitive within the Harness VLA framework. Architecture. RLDX-1 adopts a Multi-Stream Action Transformer (MSAT) as its core action modeling architecture. The system first encodes multi-frame video observations and language instructions using a Vision-Language Model (VLM) based on Qwen3-VL 8B, and extracts action-relevant representations via cognition tokens. A memory module is further introduced to aggregate historical cognition features, producing history- aware representations. The action model builds on MSAT, which decouples cognition and action streams and optionally introduces a physics stream when physical signals are available. These streams are jointly modeled via cross-stream self-attention, enabling unified processing of vision, language, state, and physical signals. Action Modeling. RLDX-1 is trained using a flow-matching diffusion transformer for continuous action prediction. The model learns a velocity field that maps noisy action trajectories to clean action sequences, and generates future actions via iterative denoising. During inference, the model produces action chunks in a chunk-wise manner and executes partial chunks sequentially to enable stable closed-loop control. The model also jointly models physical signals when available, improving contact-rich manipulation capability. Training. This work directly uses the official RLDX-1 checkpoint and keeps all parameters frozen during evaluation, without any additional training or fine-tuning. The model has already undergone multi-stage training in its original pipeline and is used here as a unified execution policy. Performance. On the RoboCasa365 benchmark, RLDX-1 achieves 60.0% on Atomic-Seen tasks, 21.3% on Composite-Seen tasks, and 5.0% on Composite-Unseen tasks, with an overall weighted success rate of 30.0%. These results show strong performance on atomic contact-rich manipulation tasks, while perfor- mance significantly degrades on compositional and out-of-distribution settings. Role in This Work. In this paper, RLDX-1 is used as a frozen low-level execution module within the Harness VLA framework, serving as the contact-rich manipulation primitive for RoboCasa365 kitchen ma- nipulation.

> <span style="color:#F59E0B"><strong>Para. 30[CN]:</strong></span> **训练。** 模型遵循 π0.5 训练协议，在 LIBERO-130 数据集上进行监督微调，得到官方 π0.5-SFT 检查点。在本文中不进行额外训练或适配；评估期间模型完全冻结。

**性能。** 在 LIBERO 基准上，π_RLinf 达到 95.3% 的成功率，展现出较强的分布内操作能力。在引入指令扰动和组合变化的 LIBERO-Pro 上，性能下降至 50.0%，表明其对分布变化敏感。

**在本文中的作用。** 在本文中，π_RLinf 作为 Harness VLA 框架内冻结的低层执行模块，为 LIBERO 和 LIBERO-Pro 任务提供接触密集操作基元。

**D.2 RLDX-1。** RLDX-1 用于 RoboCasa365 厨房操作任务。它是一种大规模视觉-语言-动作（VLA）基础模型，旨在跨多种机器人具身形态进行通用灵巧操作。在本文中，我们直接使用官方 RLDX-1 检查点，并在评估期间保持模型完全冻结，将其视为 Harness VLA 框架内的 VLA ACT 接触密集执行基元。

**架构。** RLDX-1 采用 Multi-Stream Action Transformer（MSAT）作为核心动作建模架构。系统首先使用基于 Qwen3-VL 8B 的视觉-语言模型（VLM）编码多帧视频观测和语言指令，并通过 cognition tokens 提取与动作相关的表示。系统进一步引入记忆模块聚合历史 cognition 特征，生成包含历史信息的表示。动作模型建立在 MSAT 之上：它解耦 cognition 流和 action 流，并在物理信号可用时选择性地引入 physics 流。这些流通过跨流自注意力联合建模，从而统一处理视觉、语言、状态和物理信号。

**动作建模。** RLDX-1 使用 flow-matching diffusion Transformer 训练连续动作预测。模型学习将带噪动作轨迹映射为干净动作序列的速度场，并通过迭代去噪生成未来动作。推理时，模型以动作块方式生成动作，并依次执行部分动作块，以实现稳定的闭环控制。在物理信号可用时，模型还联合建模这些信号，从而提升接触密集操作能力。

**训练。** 本文直接使用官方 RLDX-1 检查点，并在评估期间冻结全部参数，不进行额外训练或微调。该模型已经在其原始流程中经过多阶段训练；本文将其作为统一执行策略使用。

**性能。** 在 RoboCasa365 基准上，RLDX-1 在 Atomic-Seen 任务上达到 60.0%，在 Composite-Seen 任务上达到 21.3%，在 Composite-Unseen 任务上达到 5.0%，总体加权成功率为 30.0%。这些结果表明，它在原子接触密集操作任务上表现较强，但在组合式和分布外设置下性能显著下降。

**在本文中的作用。** 在本文中，RLDX-1 作为 Harness VLA 框架内冻结的低层执行模块，为 RoboCasa365 厨房操作提供接触密集操作基元。


### Source page 31 / 源页面 31


> <span style="color:#3B82F6"><strong>Para. 31:</strong></span> D.3   LingBot-VLA LingBot-VLA [25] is the vision-language-action model behind our RoboTwin backend for bimanual ma- nipulation. It is a large-scale VLA foundation model designed for continuous robotic control across diverse real-world embodiments. In this work, we use our RoboTwin-post-trained LingBot-VLA checkpoint as a frozen low-level execution module within the Harness VLA framework. Architecture. The model is built upon a pre-trained Qwen2.5-VL vision-language backbone and is ex- tended with a Mixture-of-Transformers (MoT) architecture that separates vision-language reasoning and ac- tion generation into dedicated transformer pathways. These pathways are coupled via shared self-attention, enabling unified multimodal sequence modeling while mitigating cross-modal interference. An action ex- pert module is introduced to predict continuous control signals conditioned on multimodal embeddings. Action Modeling. LingBot-VLA adopts a flow-matching formulation for continuous action prediction. To improve temporal consistency in long-horizon manipulation, it employs chunked action decoding, where a fixed-length action sequence is predicted autoregressively in a single forward pass. The chunk size is set to T = 50, enabling stable and temporally coherent control. Training. The model is first pre-trained on large-scale real-world dual-arm teleoperation data collected across 9 robotic embodiments, providing broad cross-embodiment generalization. It is then further adapted via supervised fine-tuning (SFT) on RoboTwin manipulation trajectories to specialize in bimanual manipu- lation tasks. After this post-training stage, the checkpoint is kept frozen in all direct VLA and Harness VLA evaluations. Training Configuration. We summarize the key hyperparameters governing post-training in Table 14. These parameters correspond to the configuration used for all LingBot-VLA post-training experiments re- ported in this work. Performance. Under the RoboTwin randomized evaluation setting, LingBot-VLA achieves a 50.4% suc- cess rate in the direct frozen-agent configuration (i.e., as a standalone policy without agent-level decompo- sition or external planning). This direct baseline differs from the external π0.5 comparison in the main table: LingBot-VLA is the RoboTwin-specialized frozen VLA backend used by Harness VLA, whereas π0.5 is a representative external VLA baseline. The result indicates that LingBot-VLA already provides a strong and stable contact-rich manipulation capability before agent-level decomposition. Role in This Work. In this paper, LingBot-VLA is used as a frozen execution module within Harness VLA, serving as the low-level contact-rich manipulation primitive for RoboTwin bimanual control. D.4   Unified Abstraction Across all benchmarks, heterogeneous vision-language-action models are uniformly abstracted as inter- changeable contact-rich execution primitives. The LLM planner is responsible for semantic grounding, spatial decomposition, and long-horizon task planning, while each VLA is invoked solely for localized interaction execution conditioned on the current observation.

> <span style="color:#F59E0B"><strong>Para. 31[CN]:</strong></span> **D.3 LingBot-VLA。** LingBot-VLA [25] 是我们用于双臂操作的 RoboTwin 后端视觉-语言-动作模型。它是一种面向多种真实世界具身形态连续机器人控制的大规模 VLA 基础模型。在本文中，我们使用经过 RoboTwin 后训练的 LingBot-VLA 检查点，作为 Harness VLA 框架内冻结的低层执行模块。

**架构。** 该模型建立在预训练 Qwen2.5-VL 视觉-语言主干之上，并扩展为 Mixture-of-Transformers（MoT）架构，将视觉-语言推理和动作生成分到专用 Transformer 路径中。这些路径通过共享自注意力耦合，在缓解跨模态干扰的同时实现统一的多模态序列建模。系统引入 action expert 模块，根据多模态嵌入预测连续控制信号。

**动作建模。** LingBot-VLA 采用 flow-matching 形式进行连续动作预测。为了提高长时域操作中的时间一致性，它使用分块动作解码：在一次前向传播中自回归地预测固定长度的动作序列。动作块大小设为 $T=50$，从而实现稳定且时间连贯的控制。

**训练。** 模型首先在跨 9 种机器人具身形态收集的大规模真实世界双臂遥操作数据上进行预训练，获得广泛的跨具身泛化能力。随后，在 RoboTwin 操作轨迹上通过监督微调（SFT）进一步适配，使其专门用于双臂操作任务。完成这一后训练阶段后，该检查点在所有直接 VLA 和 Harness VLA 评估中都保持冻结。

**训练配置。** 表 14 汇总后训练所使用的关键超参数。这些参数对应本文报告的全部 LingBot-VLA 后训练实验配置。

**性能。** 在 RoboTwin 随机化评估设置下，LingBot-VLA 在直接冻结智能体配置中达到 50.4% 的成功率，即将其作为独立策略使用，不进行智能体层分解或外部规划。该直接基线不同于主表中的外部 π0.5 比较：LingBot-VLA 是 Harness VLA 使用的 RoboTwin 专用冻结 VLA 后端，而 π0.5 是代表性的外部 VLA 基线。该结果表明，在智能体层分解之前，LingBot-VLA 已经提供了强而稳定的接触密集操作能力。

**在本文中的作用。** 在本文中，LingBot-VLA 作为 Harness VLA 内的冻结执行模块，为 RoboTwin 双臂控制提供低层接触密集操作基元。

**D.4 统一抽象。** 在所有基准中，不同的视觉-语言-动作模型都被统一抽象为可互换的接触密集执行基元。LLM 规划器负责语义落地、空间分解和长时域任务规划，而每个 VLA 只根据当前观测为局部交互执行而被调用。


### Source page 32 / 源页面 32


> <span style="color:#3B82F6"><strong>Para. 32:</strong></span> Table 14: Post-training configuration of LingBot-VLA on RoboTwin. Category                  Configuration Optimization Optimizer                 AdamW Learning rate             1 × 10−4 Vision encoder LR         1 × 10−6 Weight decay              0 Loss function             L1 Flow Matching (L1 FM) Sequence Modeling Chunk size                50 Max sequence length       2048 Flow steps                10 Max action dimension      75 Max state dimension       75 Training Setup Global batch size         256 Image resolution          224 × 224 Camera views              top + wrist left + wrist right System Precision                 mixed precision (bf16/fp32) Distributed training      FSDP2 E     Agent Prompt Specification This appendix specifies the task prompts used by the LLM planner in Harness VLA. The prompt is not merely a natural-language task instruction. It is the operating manual given to the agent before each rollout: it defines the file-mediated interaction protocol, the observation files that may be used for perception, the allowed primitive vocabulary, the interface to the frozen VLA primitive, the use of Task Specific Memory, and the output artifacts that must be written for reproducibility. All benchmark prompts follow a shared-core design. A single benchmark-independent prompt template defines the agent’s responsibilities, and each benchmark instantiates the slots corresponding to the success predicate, robot embodiment, camera files, primitive schemas, VLA backend, Task Specific Memory paths, and known recovery rules. This shared structure is important because the empirical comparison in the paper evaluates the same agentic harness across LIBERO / LIBERO-Pro, RoboCasa365, and RoboTwin C2R rather than hand-crafting unrelated controllers for each environment. E.1   Shared Prompt Core The shared prompt is written in the second person because it is directly addressed to the agent. Its first paragraph defines the agent role: You are an LLM-in-the-loop hybrid manipulation agent for {BENCHMARK}. A benchmark driver is already running and waiting for your commands. Your job is to complete the task by reading the task state, localizing objects from perception, choosing and executing available primitives, invoking the VLA when contact-rich behavior is needed, and writing a

> <span style="color:#F59E0B"><strong>Para. 32[CN]:</strong></span> **表 14：RoboTwin 上 LingBot-VLA 的后训练配置。**

| 类别 | 配置 |
|---|---|
| 优化器 | AdamW |
| 学习率 | $1 \times 10^{-4}$ |
| 视觉编码器学习率 | $1 \times 10^{-6}$ |
| 权重衰减 | 0 |
| 损失函数 | L1 Flow Matching（L1 FM） |
| 序列建模：动作块大小 | 50 |
| 最大序列长度 | 2048 |
| Flow 步数 | 10 |
| 最大动作维度 | 75 |
| 最大状态维度 | 75 |
| 全局批次大小 | 256 |
| 图像分辨率 | 224 × 224 |
| 相机视角 | top + wrist left + wrist right |
| 系统精度 | 混合精度（bf16/fp32） |
| 分布式训练 | FSDP2 |

**E 智能体提示词规范。** 本附录规定 Harness VLA 中 LLM 规划器使用的任务提示词。提示词并不只是自然语言任务指令，而是每次 rollout 前提供给智能体的操作手册：它定义文件媒介交互协议、可用于感知的观测文件、允许的基元词汇、与冻结 VLA 基元的接口、任务特定记忆的使用方式，以及为保证可复现性必须写入的输出工件。所有基准提示词都遵循共享核心设计。一个与基准无关的提示词模板定义智能体的职责，每个基准再填充成功谓词、机器人具身形态、相机文件、基元模式、VLA 后端、任务特定记忆路径和已知恢复规则等槽位。该共享结构十分重要，因为本文的实证比较在 LIBERO / LIBERO-Pro、RoboCasa365 和 RoboTwin C2R 上评估同一个智能体 harness，而不是为每个环境手工制作互不相关的控制器。

**E.1 共享提示词核心。** 共享提示词使用第二人称，因为它直接面向智能体。其第一段定义智能体角色：

```text
You are an LLM-in-the-loop hybrid manipulation agent for {BENCHMARK}. A benchmark driver is already running and waiting for your commands. Your job is to complete the task by reading the task state, localizing objects from perception, choosing and executing available primitives, invoking the VLA when contact-rich behavior is needed, and writing a
```


### Source page 33 / 源页面 33


> <span style="color:#3B82F6"><strong>Para. 33:</strong></span> reproducible audit. The remainder of the shared prompt is organized into the modules summarized in Table 15. Each module is present in all benchmark prompts, while benchmark-specific prompts fill in concrete fields such as state.libero terminated, state.success, eval success, camera names, and primitive schemas. Table 15: Shared modules in the agent task prompt. Each benchmark-specific prompt keeps this structure and fills in environment-specific details. Prompt module             Information given to the agent Role and success signal Closed-loop control; optimize the benchmark predicate, not a visual guess. Perception isolation    No ground-truth poses or simulator internals; localize from RGB-D and world maps. File-based REPL         Write one JSON command, wait for execution, read refreshed artifacts, then iterate. Primitive vocabulary    Allowed primitive schemas and controller semantics, including gripper, arm, and step conventions. VLA division of labor   VLA for contact-rich phases; analytic primitives for grounding, staging, trans- port, release, and recovery. Task language           State-file task language is authoritative; do not infer tasks from filenames or indices. Seed 0 Task Specific JSON audit for strategy and failure modes; JSONL trace for primitive execution Memory                  order. Global Memory           Reusable success rules and failure observations that provide additional context beyond seed 0 Task Specific Memory. Closed-loop recovery    Verify state, logs, RGB, and geometry after every primitive; diagnose before retrying. Budget and reset policy Track budget and reset policy; reset is disabled in strict evaluation. Output discipline       Write audit and command trace for both successful and failed rollouts. E.2     Perception and File-Mediated Control The shared prompt makes perception isolation explicit, explicitly prohibiting access to privileged informa- tion (e.g., ground-truth object poses or simulator internal states) to enforce a realistic partial-observation setting and prevent any reliance on oracle-level environment access during decision making. The agent receives object names and proprioception from the state file, but not object coordinates. It must localize en- tities by choosing pixels in RGB images and indexing the corresponding precomputed world map, thereby grounding all spatial reasoning in perceptual inputs rather than hidden state variables. The common local- ization instruction is: 1. Identify the relevant object, fixture, target surface, or relation landmark from RGB. 2. Pick pixels on the visible surface of that entity. 3. Index the matching precomputed world map at those pixels. 4. Sample multiple stable pixels and use a robust statistic, typically the median. 5. Avoid rims, object edges, table gaps, holes, reflections, and background pixels. 6. Re-localize whenever the robot, camera, object, base, fixture, or grasp state changes.

> <span style="color:#F59E0B"><strong>Para. 33[CN]:</strong></span> 可复现审计。共享提示词的其余部分组织为表 15 所概括的模块。每个模块都存在于所有基准提示词中，而基准特定提示词填入 `state.libero_terminated`、`state.success`、`eval_success`、相机名称和基元模式等具体字段。

**表 15：智能体任务提示词中的共享模块。** 每个基准特定提示词都保留这一结构，并填入环境特定的细节。

| 提示词模块 | 提供给智能体的信息 |
|---|---|
| 角色与成功信号 | 闭环控制；优化基准谓词，而不是视觉猜测。 |
| 感知隔离 | 不提供真实位姿或仿真器内部信息；从 RGB-D 和世界地图中进行定位。 |
| 基于文件的 REPL | 写入一个 JSON 命令，等待执行，读取刷新的工件，然后迭代。 |
| 基元词汇 | 允许的基元模式和控制器语义，包括夹爪、机械臂和步数约定。 |
| VLA 分工 | VLA 用于接触密集阶段；解析基元用于落地、定位、运输、释放和恢复。 |
| 任务语言 | 状态文件中的任务语言具有权威性；不要从文件名或索引推断任务。 |
| 种子 0 任务特定记忆 | JSON 审计用于记录策略和失败模式；JSONL 轨迹用于记录基元执行顺序。 |
| 全局记忆 | 可复用的成功规则和失败观测，为种子 0 任务特定记忆之外提供额外上下文。 |
| 闭环恢复 | 每个基元之后验证状态、日志、RGB 和几何信息；先诊断，再重试。 |
| 预算与重置策略 | 跟踪预算和重置策略；严格评估中禁用重置。 |
| 输出规范 | 为成功和失败 rollout 都写入审计记录和命令轨迹。 |

**E.2 感知与文件媒介控制。** 共享提示词明确规定感知隔离，明确禁止访问特权信息（例如真实物体位姿或仿真器内部状态），以强制采用真实的部分观测设置，并防止决策依赖预言式环境访问。智能体从状态文件接收物体名称和本体感知，但不接收物体坐标。它必须通过在 RGB 图像中选择像素并索引对应的预计算世界地图来定位实体，从而将所有空间推理建立在感知输入上，而不是隐藏状态变量上。

通用定位指令为：

1. 从 RGB 中识别相关物体、装置、目标表面或关系地标。
2. 在该实体的可见表面上选择像素。
3. 用这些像素索引匹配的预计算世界地图。
4. 采样多个稳定像素并使用稳健统计量，通常为中位数。
5. 避开边沿、物体边缘、桌面缝隙、孔洞、反射区域和背景像素。
6. 每当机器人、相机、物体、底座、装置或抓取状态发生变化时，重新定位。


### Source page 34 / 源页面 34


> <span style="color:#3B82F6"><strong>Para. 34:</strong></span> This perception rule is paired with the same REPL-style execution contract used throughout the paper: 1. Write one JSON command to {WORKDIR}/command.json. 2. Wait until the driver finishes that primitive, typically via done_NN.flag, log_NN.json, or a benchmark-specific terminal file. 3. Read the new state_NN.json, log_NN.json, images, depth maps, and world maps. 4. Decide the next command from the new evidence. Thus, the prompt enforces the same closed-loop behavior used in the framework description: every primitive call is treated as an experiment whose result must be observed before the next command is issued. E.3    Seed 0 Task Specific Memory The most important memory-related part of the prompt is the instruction for using seed 0 Task Specific Memory. Task Specific Memory is not a plain demonstration to replay. It is a structured memory object that separates semantic strategy from concrete primitive execution. Across benchmarks, the prompt tells the agent to look for two complementary files: {TASK}\_s0.json (Task Specific Memory audit JSON) {TASK}\_s0.jsonl (Task Specific Memory command JSONL) The JSON file is the audit and strategy summary for the seed 0 rollout. It records the outcome of the reference run and provides high-level notes about the solution strategy, useful primitive choices, recovery decisions, and failure modes observed during exploration. It is not replayed as an action trace; instead, the agent uses it to interpret the reference solution before consulting the JSONL command trace for the concrete primitive order. Depending on the benchmark, this JSON includes the rollout outcome, success status, command or step counts, strategy notes, failure observations, and a summary of the final state. The JSONL file is the executable command trace. Each line stores one JSON primitive issued by the agent during the reference rollout. The agent reads this trace to recover the procedural structure of the solution: the ordering of primitive calls, the choice of analytic versus VLA-backed actions, the number and placement of VLA invocations, and the transition points between perception, staging, contact-rich execution, transport, release, and verification. The trace is used as a structural prior rather than a trajectory to replay; all spatial arguments are re-grounded from the current observation before execution. The prompt gives the agent the following rule: Use the JSON audit to understand why the strategy worked and what to avoid. Use the JSONL trace to understand what was executed and in what order. Reuse the Task Specific Memory procedural structure, but never replay literal coordinates. Previous xyz, xy, quat, pixel locations, base poses, and fixture coordinates belong to the seed 0 scene. Re-localize every current object, destination, support surface, relation landmark, and fixture from the current images and world maps. This rule is the prompt-level implementation of Task Specific Memory in Section 2.2. It lets the planner transfer the structure of a successful solution while grounding all geometry in the current rollout. E.4    Global Memory Global Memory complements seed 0 Task Specific Memory. Task Specific Memory is task-specific procedu- ral context: it records the JSON audit and JSONL command trace for one reference rollout. Global Memory

> <span style="color:#F59E0B"><strong>Para. 34[CN]:</strong></span> 该感知规则与全文使用的同一 REPL 式执行契约配套：

1. 将一个 JSON 命令写入 `{WORKDIR}/command.json`。
2. 等待驱动器完成该基元，通常通过 `done_NN.flag`、`log_NN.json` 或基准特定的终端文件完成同步。
3. 读取新的 `state_NN.json`、`log_NN.json`、图像、深度图和世界地图。
4. 根据新证据决定下一条命令。

因此，提示词强制执行与框架描述相同的闭环行为：每次基元调用都被视为一次实验，必须在发出下一条命令之前观测其结果。

**E.3 种子 0 任务特定记忆。** 提示词中与记忆相关的最重要部分，是关于使用种子 0 任务特定记忆的指令。Task Specific Memory 不是简单重放的示范，而是将语义策略与具体基元执行分离开的结构化记忆对象。跨所有基准，提示词要求智能体寻找两个互补文件：

- `{TASK}\_s0.json`（任务特定记忆审计 JSON）
- `{TASK}\_s0.jsonl`（任务特定记忆命令 JSONL）

JSON 文件是种子 0 rollout 的审计和策略摘要。它记录参考运行的结果，并提供关于解决策略、有用基元选择、恢复决策以及探索期间观测到的失败模式的高层说明。它不会作为动作轨迹重放；相反，智能体先使用它理解参考解决方案，再查阅 JSONL 命令轨迹以获得具体的基元顺序。根据基准不同，该 JSON 包含 rollout 结果、成功状态、命令或步数统计、策略说明、失败观测以及最终状态摘要。

JSONL 文件是可执行的命令轨迹。每行存储智能体在参考 rollout 中发出的一个 JSON 基元。智能体读取该轨迹以恢复解决方案的程序结构：基元调用的顺序、解析动作与 VLA 支持动作的选择、VLA 调用的次数和位置，以及感知、定位、接触密集执行、运输、释放和验证之间的转换点。该轨迹被用作结构先验，而不是待重放的轨迹；所有空间参数都在执行前根据当前观测重新落地。

提示词向智能体给出如下规则：使用 JSON 审计理解策略为何有效以及应当避免什么；使用 JSONL 轨迹理解执行了什么以及执行顺序。复用任务特定记忆的程序结构，但绝不重放字面坐标。之前的 xyz、xy、quat、像素位置、底座位姿和装置坐标都属于种子 0 场景。必须从当前图像和世界地图中重新定位当前物体、目的地、支撑表面、关系地标和装置。

该规则是第 2.2 节任务特定记忆在提示词层面的实现。它使规划器能够迁移成功解决方案的结构，同时根据当前 rollout 对所有几何信息重新落地。

**E.4 全局记忆。** Global Memory 补充种子 0 任务特定记忆。任务特定记忆是任务相关的程序上下文，记录一次参考 rollout 的 JSON 审计和 JSONL 命令轨迹；Global Memory


### Source page 35 / 源页面 35


> <span style="color:#3B82F6"><strong>Para. 35:</strong></span> is task-independent. It stores reusable success rules and failure models for the fixed primitive library, in- cluding known VLA operating conditions, empty-grasp failures, false visual success, unstable staging, and recovery patterns. It is used as contextual guidance during closed-loop execution, not as an action trace to replay. Use Global Memory to check: 1. known success rules for VLA and analytic primitives; 2. known failure models before repeating or repairing an action; 3. empty grasps, wrong-object attempts, false visual success, and unstable staging; E.5    Benchmark-Specific Prompt Instantiations Tables 16 and 17 summarize how the shared prompt is instantiated for each benchmark. We separate the instantiation into interface-level fields and environment-context fields. The former specifies the success predicate, frozen VLA entry point, and required audit artifacts; the latter records the embodiment and control assumptions that specialize the shared prompt for each benchmark. Table 16: Interface-level prompt instantiations across benchmarks. In the main text, the heterogeneous VLA primitive names are abstracted as the unified VLA ACT interface. Benchmark             Success signal               VLA interface                         Output artifacts LIBERO / LIBERO- libero terminated                  VLA ACT                              Command      JSONL;     audit Pro                                                                                      JSON RoboCasa365           success                       VLA ACT                              Command      JSONL;     audit JSON RoboTwin C2R          eval success                  VLA ACT                              Command      JSONL;     audit JSON Table 17: Environment context supplied by the benchmark-specific prompts. Benchmark             Environment-specific prompt specialization LIBERO / LIBERO- Single-arm tabletop manipulation; fixed agentview and moving wrist RGB-D/world-map observa- Pro              tions; agent-side transport, release, and visual verification after contact-rich steps. RoboCasa365           Mobile kitchen manipulation; base motion is available for reaching distant fixtures; the agent re- localizes after base movement; fixture-facing staging and continuation of capped but progressing contact attempts are treated as part of the operating policy. RoboTwin C2R          Dual-arm manipulation; manual motion commands are bound to a specified arm; head and left/right wrist observations provide perception; manual primitives support observation refresh, non-grasp motion, release, termination, and recovery around contact-rich attempts. LIBERO / LIBERO-Pro.          The LIBERO-family prompt is shared by standard LIBERO and LIBERO-Pro: You are an LLM-in-the-loop hybrid driver for the LIBERO PRO/LIBERO benchmark.

> <span style="color:#F59E0B"><strong>Para. 35[CN]:</strong></span> 与任务无关。它为固定基元库存储可复用的成功规则和失败模型，包括已知的 VLA 工作条件、空抓取失败、错误视觉成功、不稳定定位和恢复模式。它在闭环执行期间作为上下文指导使用，而不是作为待重放的动作轨迹。

使用 Global Memory 检查：

1. VLA 和解析基元的已知成功规则；
2. 在重复或修复动作之前检查已知失败模型；
3. 空抓取、错误物体尝试、错误视觉成功和不稳定定位。

**E.5 基准特定提示词实例化。** 表 16 和表 17 总结共享提示词如何针对各基准实例化。我们将实例化分为接口层字段和环境上下文字段。前者规定成功谓词、冻结 VLA 入口点和所需的审计工件；后者记录使共享提示词适配各基准的具身形态与控制假设。

**表 16：跨基准的接口层提示词实例化。** 在正文中，不同的 VLA 基元名称被抽象为统一的 VLA ACT 接口。

| 基准 | 成功信号 | VLA 接口 | 输出工件 |
|---|---|---|---|
| LIBERO / LIBERO-Pro | `libero_terminated` | VLA ACT | Command JSONL；audit JSON |
| RoboCasa365 | `success` | VLA ACT | Command JSONL；audit JSON |
| RoboTwin C2R | `eval_success` | VLA ACT | Command JSONL；audit JSON |

**表 17：基准特定提示词提供的环境上下文。**

| 基准 | 环境特定的提示词专门化 |
|---|---|
| LIBERO / LIBERO-Pro | 单臂桌面操作；固定 agentview 和移动 wrist 的 RGB-D/世界地图观测；接触密集步骤之后由智能体负责运输、释放和视觉验证。 |
| RoboCasa365 | 移动厨房操作；底座运动可用于到达远处装置；智能体在底座移动后重新定位；面向装置的定位，以及对虽达到上限但仍在取得进展的接触尝试的继续，被视为操作策略的一部分。 |
| RoboTwin C2R | 双臂操作；手动运动命令绑定到指定机械臂；头部和左右腕部观测提供感知；手动基元支持围绕接触密集尝试进行观测刷新、非抓取运动、释放、终止和恢复。 |

**LIBERO / LIBERO-Pro。** LIBERO 系列提示词由标准 LIBERO 和 LIBERO-Pro 共享：

```text
You are an LLM-in-the-loop hybrid driver for the LIBERO PRO/LIBERO benchmark.
```


### Source page 36 / 源页面 36


> <span style="color:#3B82F6"><strong>Para. 36:</strong></span> This instantiation specializes the shared prompt for single-arm tabletop manipulation. It defines the LIBERO observation files used for perception-based grounding, including the fixed agentview RGB-D/world- map files and the moving wrist-camera files used for close-range re-localization. The unified VLA ACT in- terface is used for contact-rich steps, including grasping and closed-loop articulated-object, button, or knob manipulation. After contact is established, the agent remains responsible for target identification, scene re-localization, free-space transport, release, and progress verification. RoboCasa365.      The RoboCasa prompt instantiates the shared structure for mobile kitchen manipulation: You are an LLM-in-the-loop hybrid driver for the RoboCasa365 kitchen benchmark. This instantiation adds mobile-base staging to the shared manipulation loop. The agent grounds objects and fixtures from RGB-D/world-map observations, uses navigate to for coarse base placement, and uses move base for small local corrections. Because base motion changes the robot viewpoint and the relative arm workspace, the prompt emphasizes re-localization after navigation before continuing manipulation. The unified VLA ACT interface provides the contact-rich primitive. The VLA instruction is the full task language, and the planner decides whether to invoke it after local staging or during broader whole- body interaction. A capped but still-progressing VLA call is handled as a continuation case rather than an immediate failure, so the same VLA call can be continued instead of being interrupted by manual commands. RoboTwin C2R.       The RoboTwin prompt instantiates the shared core for dual-arm manipulation: You are an LLM-in-the-loop hybrid manipulation agent for the RoboTwin benchmark. This instantiation specializes the prompt for a dual-arm setting. Manual motion commands include explicit left/right arm binding, and the observation stream includes head and left/right wrist views with corresponding depth and world-map files. The driver reports the official RoboTwin success signal through eval success and writes a terminal final.json when the rollout exits. The contact-rich interface is exposed as VLA ACT. This primitive is used for grasp formation, re- grasping, handover grasps, bimanual grasp formation, and other contact-rich phases. Manual primitives are used around these VLA attempts for observation refresh, non-grasp motion, release, termination, and recovery. RoboTwin additionally requires a diagnosis Markdown file for post-hoc analysis. E.6    Compact Prompt Skeleton For completeness, the following listing shows the compact shared skeleton underlying all four prompt files. The benchmark-specific prompts fill the bracketed slots with the concrete values described above. You are an LLM-in-the-loop hybrid manipulation agent for {BENCHMARK}. The benchmark driver is already running in {WORKDIR}. Complete the task by reading state and perception files, localizing task entities from RGB and world maps, invoking only the allowed primitives, using the frozen VLA for contact-rich behavior, and writing a reproducible audit. 1. ROLE AND SUCCESS SIGNAL You are a closed-loop controller. Optimize {SUCCESS_SIGNAL}, not a visual guess. Continue until success, budget exhaustion, or unrecoverability.

> <span style="color:#F59E0B"><strong>Para. 36[CN]:</strong></span> 该实例化将共享提示词专门化为单臂桌面操作。它定义了用于基于感知进行落地的 LIBERO 观测文件，包括固定的 agentview RGB-D/世界地图文件，以及用于近距离重新定位的移动腕部相机文件。统一的 VLA ACT 接口用于接触密集步骤，包括抓取以及闭环的关节物体、按钮或旋钮操作。建立接触后，智能体仍负责目标识别、场景重新定位、自由空间运输、释放和进度验证。

**RoboCasa365。** RoboCasa 提示词将共享结构实例化为移动厨房操作：

```text
You are an LLM-in-the-loop hybrid driver for the RoboCasa365 kitchen benchmark.
```

该实例化将移动底座定位加入共享操作循环。智能体从 RGB-D/世界地图观测中落地物体和装置，使用 `navigate to` 进行粗粒度底座定位，并使用 `move base` 进行小范围局部修正。由于底座运动会改变机器人视点和相对机械臂工作空间，提示词强调导航后重新定位，再继续操作。统一的 VLA ACT 接口提供接触密集基元。VLA 指令使用完整任务语言，规划器决定是在局部定位后还是在更广泛的全身交互过程中调用它。达到上限但仍在取得进展的 VLA 调用被视为继续情形，而不是立即失败，因此可以继续同一次 VLA 调用，而不会被手动命令打断。

**RoboTwin C2R。** RoboTwin 提示词将共享核心实例化为双臂操作智能体：

```text
You are an LLM-in-the-loop hybrid manipulation agent for the RoboTwin benchmark.
```

该实例化针对双臂设置进行专门化。手动运动命令包含明确的左右机械臂绑定，观测流包含头部和左右腕部视角以及相应的深度图和世界地图文件。驱动器通过 `eval_success` 报告官方 RoboTwin 成功信号，并在 rollout 退出时写入终端 `final.json`。接触密集接口以 VLA ACT 形式暴露。该基元用于抓取形成、重新抓取、交接抓取、双臂抓取形成和其他接触密集阶段。手动基元用于围绕这些 VLA 尝试进行观测刷新、非抓取运动、释放、终止和恢复。RoboTwin 还要求一个诊断 Markdown 文件，用于事后分析。

**E.6 紧凑提示词骨架。** 为完整起见，下面列出四个提示词文件所共同使用的紧凑骨架。基准特定提示词将方括号槽位填入上述具体值。

```text
You are an LLM-in-the-loop hybrid manipulation agent for {BENCHMARK}. The benchmark driver is already running in {WORKDIR}. Complete the task by reading state and perception files, localizing task entities from RGB and world maps, invoking only the allowed primitives, using the frozen VLA for contact-rich behavior, and writing a reproducible audit.

1. ROLE AND SUCCESS SIGNAL
You are a closed-loop controller. Optimize {SUCCESS_SIGNAL}, not a visual guess. Continue until success, budget exhaustion, or unrecoverability.
```


### Source page 37 / 源页面 37


> <span style="color:#3B82F6"><strong>Para. 37:</strong></span> 2. PERCEPTION ISOLATION Do not query simulator object poses or hidden task initialization. Use RGB for semantic identity and depth/world maps for metric localization. Re-localize after every object, camera, robot, base, or grasp change. 3. FILE-BASED REPL Write one JSON command to {WORKDIR}/command.json. Wait for the driver result. Read state_NN.json, log_NN.json, images, depth maps, and world maps. Then decide the next command. 4. PRIMITIVE VOCABULARY Use only {PRIMITIVE_SCHEMAS}. Preserve exact syntax and controller semantics, including gripper sign, arm binding, chunk budgets, and step costs. 5. DIVISION OF LABOR BETWEEN YOU AND THE VLA Use {VLA_PRIMITIVE} for grasping, re-grasping, articulated contact, insertion, pressing, seating, and other contact-rich phases. Use analytic primitives for grounding, staging, free-space transport, release, verification, and recovery. 6. TASK LANGUAGE Read task_language from the state file. It is authoritative. Do not infer the task from filenames, object lists, task indices, or neighboring Task Specific Memory files. 7. SEED 0 TASK SPECIFIC MEMORY AND GLOBAL MEMORY Read the task-matched seed 0 Task Specific Memory audit JSON to understand why the task-specific strategy worked and what failed. Read the seed 0 Task Specific Memory JSONL to recover what was executed and in what order. Read Global Memory for cross-task success rules and failure models. Use Task Specific Memory as the task-specific procedural skeleton, but use Global Memory and current perception to decide when to re-ground, verify, recover, or stop. Never replay literal coordinates. 8. CLOSED-LOOP VERIFICATION AND RECOVERY After every command, inspect state, logs, RGB, and world maps. Diagnose wrong-object selection, poor stance, VLA miss, short placement, hidden predicate failure, or unrecoverable displacement before acting again. 9. BUDGET, RESET, AND TERMINATION Track the benchmark budget and reset policy. Do not reset in strict evaluation. Stop only on success, budget exhaustion, or unrecoverability. 10. OUTPUT DISCIPLINE Write the required audit JSON and command-trace JSONL. The audit JSON records the benchmark success status and the final outcome fields used for evaluation and success-rate computation. The JSONL trace records the agent’s executed primitive commands in order, enabling inspection and analysis of the agent’s decision process. 11. OPERATING LOOP

> <span style="color:#F59E0B"><strong>Para. 37[CN]:</strong></span> **2. 感知隔离（PERCEPTION ISOLATION）** 不要查询仿真器物体位姿或隐藏的任务初始化。使用 RGB 获取语义身份，使用深度图/世界地图进行度量定位。每当物体、相机、机器人、底座或抓取状态发生变化时，重新定位。

**3. 基于文件的 REPL（FILE-BASED REPL）** 将一个 JSON 命令写入 `{WORKDIR}/command.json`。等待驱动器结果。读取 `state_NN.json`、`log_NN.json`、图像、深度图和世界地图。然后决定下一条命令。

**4. 基元词汇（PRIMITIVE VOCABULARY）** 只使用 `{PRIMITIVE_SCHEMAS}`。保留精确语法和控制器语义，包括夹爪符号、机械臂绑定、动作块预算和步数成本。

**5. 你与 VLA 之间的分工（DIVISION OF LABOR BETWEEN YOU AND THE VLA）** 使用 `{VLA_PRIMITIVE}` 进行抓取、重新抓取、关节接触、插入、按压、就位和其他接触密集阶段。使用解析基元进行落地、定位、自由空间运输、释放、验证和恢复。

**6. 任务语言（TASK LANGUAGE）** 从状态文件读取 `task_language`。它具有权威性。不要根据文件名、物体列表、任务索引或相邻的任务特定记忆文件推断任务。

**7. 种子 0 任务特定记忆与全局记忆（SEED 0 TASK SPECIFIC MEMORY AND GLOBAL MEMORY）** 读取与任务匹配的种子 0 任务特定记忆审计 JSON，以理解任务特定策略为何有效以及失败之处。读取种子 0 任务特定记忆 JSONL，以恢复执行了什么以及执行顺序。读取 Global Memory，获得跨任务成功规则和失败模型。使用任务特定记忆作为任务相关的程序骨架，但使用 Global Memory 和当前感知决定何时重新落地、验证、恢复或停止。绝不重放字面坐标。

**8. 闭环验证与恢复（CLOSED-LOOP VERIFICATION AND RECOVERY）** 每个命令之后检查状态、日志、RGB 和世界地图。在再次行动之前，诊断错误物体选择、姿态不佳、VLA 未命中、放置过短、隐藏谓词失败或不可恢复的位移。

**9. 预算、重置与终止（BUDGET, RESET, AND TERMINATION）** 跟踪基准预算和重置策略。严格评估中不要重置。只有在成功、预算耗尽或不可恢复时才停止。

**10. 输出规范（OUTPUT DISCIPLINE）** 写入所需的审计 JSON 和命令轨迹 JSONL。审计 JSON 记录基准成功状态以及用于评估和成功率计算的最终结果字段。JSONL 轨迹按顺序记录智能体执行的基元命令，以便检查和分析智能体的决策过程。

**11. 操作循环（OPERATING LOOP）**


### Source page 38 / 源页面 38


> <span style="color:#3B82F6"><strong>Para. 38:</strong></span> Read prompt, state, task language, perception, Task Specific Memory, and Global Memory. Localize entities. Execute one primitive. Observe. Recover. Repeat. Write outputs. This structured prompt design keeps the common Harness VLA operating protocol separate from benchmark- specific assumptions, providing a reusable template for constructing agent prompts in additional manipula- tion benchmarks. F    Primitive Usage Statistics Table 18 aggregates the primitive calls issued by Harness VLA (CC) across LIBERO Pro-family, RoboTwin C2R, and RoboCasa365 runs. We report canonical primitive names following the taxonomy and availabil- ity summary in Table 8: all backend-specific VLA calls are merged into the unified VLA ACT primitive, implementation-level motion macros are folded into their exposed analytic primitive, and non-manipulation helpers such as rendering, reset, notes, and no-ops are excluded. Percentages are computed within each environment’s total manipulation-primitive calls. The usage pattern supports the intended asymmetric decomposition. In LIBERO, analytic primitives dominate: MOVE TO alone accounts for 61.8% of calls, while VLA ACT accounts for 15.8%. This matches the tabletop structure of the tasks: the VLA is used primarily to establish contact-rich grasps or fixture interactions, after which analytic transport, gripper control, and release complete much of the rollout. RoboCasa365 shifts the mix toward mobile staging and longer-horizon interaction: NAVIGATE TO and MOVE BASE together account for 19.4% of calls, while VLA ACT rises to 35.3% because kitchen tasks require learned grasps, fixture actuation, and constrained placements across larger scenes. RoboTwin C2R has the highest VLA share (47.4%), reflecting bimanual grasping and handover-like contact, yet analytic primitives still provide a slight majority of calls for planned arm motion, release, and final arrangement. Table 19 summarizes the same evidence at the class level. Across all three embodiments, the frozen VLA is not used as a monolithic end-to-end controller; it is invoked as a contact-rich primitive inside a larger analytic scaffold. The exact ratio changes with embodiment and task family, but the qualitative division remains stable: analytic primitives handle reproducible geometry and staging, while VLA ACT supplies the learned local interactions that are difficult to script. Table 18: Canonical primitive usage across benchmark environments. Each cell reports count and per- centage of manipulation-primitive calls within that environment. A dash indicates that the primitive is not exposed in the corresponding environment. Canonical primitive Kind                            LIBERO          RoboTwin C2R RoboCasa365 MOVE TO                  Analytic composite       6263 (61.8%)        685 (40.9%)        3004 (38.7%) MOVE POSE                Analytic composite        203 (2.0%)              –                   – NAVIGATE TO              Analytic composite             –                  –              701 (9.0%) ROTATE WRIST             Analytic atomic            44 (0.4%)          1 (0.1%)                – ROTATE PITCH             Analytic atomic            58 (0.6%)              –               66 (0.8%) SET GRIPPER              Analytic atomic          1137 (11.2%)         71 (4.2%)          371 (4.8%) RELEASE                  Analytic atomic           831 (8.2%)         124 (7.4%)           76 (1.0%) MOVE BASE                Analytic atomic                –                  –             808 (10.4%) VLA ACT                  VLA                      1598 (15.8%)        794 (47.4%)        2746 (35.3%) Total                                           10134 (100.0%)       1675 (100.0%)      7772 (100.0%)

> <span style="color:#F59E0B"><strong>Para. 38[CN]:</strong></span> 读取提示词、状态、任务语言、感知、Task Specific Memory 和 Global Memory。定位实体。执行一个基元。观测。恢复。重复。写入输出。

这种结构化提示词设计将通用 Harness VLA 操作协议与基准特定假设分离开来，为在其他操作基准中构造智能体提示词提供了可复用模板。

**F 基元使用统计。** 表 18 汇总 Harness VLA (CC) 在 LIBERO Pro 系列、RoboTwin C2R 和 RoboCasa365 运行中发出的基元调用。我们遵循表 8 中的分类和可用性汇总报告规范的基元名称：所有后端特定的 VLA 调用合并为统一的 VLA ACT 基元，实施层运动宏折叠到其暴露的解析基元中，渲染、重置、备注和 no-op 等非操作辅助调用被排除。百分比在每个环境的操作基元调用总数内计算。

使用模式支持预期的非对称分解。在 LIBERO 中，解析基元占主导：仅 MOVE TO 就占调用的 61.8%，而 VLA ACT 占 15.8%。这与桌面任务的结构一致：VLA 主要用于建立接触密集抓取或装置交互，随后解析运输、夹爪控制和释放完成 rollout 的大部分过程。RoboCasa365 的调用组合转向移动定位和更长时域交互：NAVIGATE TO 与 MOVE BASE 合计占 19.4%，而 VLA ACT 升至 35.3%，因为厨房任务需要在更大场景中进行学习型抓取、装置驱动和受限放置。RoboTwin C2R 的 VLA 占比最高（47.4%），反映了双臂抓取和类似交接的接触操作，但解析基元仍因计划性的机械臂运动、释放和最终整理而略占多数。

表 19 在类别层面总结相同证据。在三种具身形态中，冻结 VLA 都没有作为单体端到端控制器使用；它是在更大解析支架内作为接触密集基元被调用。具体比例随具身形态和任务族变化，但定性分工保持稳定：解析基元处理可复现的几何和定位，VLA ACT 提供难以脚本化的学习型局部交互。

**表 18：各基准环境中的规范基元使用情况。** 每个单元报告该环境内操作基元调用的数量和百分比。短横线表示相应环境未暴露该基元。

| 规范基元 | 类型 | LIBERO | RoboTwin C2R | RoboCasa365 |
|---|---|---:|---:|---:|
| MOVE TO | 解析复合 | 6263 (61.8%) | 685 (40.9%) | 3004 (38.7%) |
| MOVE POSE | 解析复合 | 203 (2.0%) | — | — |
| NAVIGATE TO | 解析复合 | — | — | 701 (9.0%) |
| ROTATE WRIST | 解析原子 | 44 (0.4%) | 1 (0.1%) | — |
| ROTATE PITCH | 解析原子 | 58 (0.6%) | — | 66 (0.8%) |
| SET GRIPPER | 解析原子 | 1137 (11.2%) | 71 (4.2%) | 371 (4.8%) |
| RELEASE | 解析原子 | 831 (8.2%) | 124 (7.4%) | 76 (1.0%) |
| MOVE BASE | 解析原子 | — | — | 808 (10.4%) |
| VLA ACT | VLA | 1598 (15.8%) | 794 (47.4%) | 2746 (35.3%) |
| 总计 |  | 10134 (100.0%) | 1675 (100.0%) | 7772 (100.0%) |


### Source page 39 / 源页面 39


> <span style="color:#3B82F6"><strong>Para. 39:</strong></span> Table 19: Primitive usage grouped by class. Analytic primitives include both composite goal-reaching controllers and atomic set-point commands. Primitive class             LIBERO          RoboTwin C2R       RoboCasa365 Analytic primitives        8536 (84.2%)      881 (52.6%)       5026 (64.7%) VLA primitive, VLA ACT     1598 (15.8%)      794 (47.4%)       2746 (35.3%)

> <span style="color:#F59E0B"><strong>Para. 39[CN]:</strong></span> **表 19：按类别汇总的基元使用情况。** 解析基元包括复合目标到达控制器和原子设定值命令。

| 基元类别 | LIBERO | RoboTwin C2R | RoboCasa365 |
|---|---:|---:|---:|
| 解析基元 | 8536 (84.2%) | 881 (52.6%) | 5026 (64.7%) |
| VLA 基元，VLA ACT | 1598 (15.8%) | 794 (47.4%) | 2746 (35.3%) |


## Material-level caveat / 材料级 caveat

The supplied PDF is extractable and all 39 pages have been preserved above in source order. This file is **not complete as a Chinese translation**: the Chinese side is explicitly marked unfinished because the current API/output window did not permit reliable paragraph-by-paragraph translation of all 39 pages in one pass. No missing prose, table value, prompt, equation, or reference has been invented. The rendered page assets provide visual authority for extraction ambiguities. A future continuation should replace each marked `[CN]` block with a faithful Chinese translation while retaining the paired English source block.

所提供 PDF 可以提取文本，且 39 页均已按源顺序保存在上方。本文件的中文部分**尚未达到完整翻译**：由于当前 API/输出窗口无法在单次处理中可靠完成 39 页逐段翻译，所有中文侧均明确标注为未完成。没有编造任何缺失正文、表格数值、提示词、公式或参考文献。渲染页面资源可用于核对提取歧义；后续续作应逐一将标记的 `[CN]` 块替换为忠实中文译文，同时保留配对的英文源块。
