# SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning
**Authors:** Haoqiang Kang, Xiaokang Ye, Yuhan Liu, Siddhant Hitesh Mantri, Lingjun Mao, James Fleming, Drishti Regmi, Lianhui Qin  
**Source:** `Kang 等 - 2026 - SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Lear.pdf`  
**Detected source format:** selectable-text PDF (`pdf-text`)  
**Reader type:** full-paper Chinese-English Markdown reader with figure/table assets, generated with WJ `nature-reader`.

## Page / Section Index
| Section | Pages | Notes |
|---|---:|---|
| Abstract | pp.1-2 | bilingual body and related figure/table assets |
| 1 Introduction | pp.2-7 | bilingual body and related figure/table assets |
| 2 SimWorld Studio / SimCoder | pp.3-6 | bilingual body and related figure/table assets |
| 2.2 Co-Evolution | pp.6-7 | bilingual body and related figure/table assets |
| 3 Experiments Overview | pp.7-8 | bilingual body and related figure/table assets |
| 3.1 Case Study 1: Environment Generation Quality | pp.7-10 | bilingual body and related figure/table assets |
| 3.2 Case Study 2: Embodied Navigation Learning | pp.10-11 | bilingual body and related figure/table assets |
| 3.3 Case Study 3: Co-Evolution | pp.11-12 | bilingual body and related figure/table assets |
| 4 Related Work | p.12 | bilingual body and related figure/table assets |
| 5 Conclusion | p.12 | bilingual body and related figure/table assets |
| Limitations and Broader Impact | pp.21-30 | bilingual body and related figure/table assets |
| Appendix: Interface, Configuration, and Evaluation Details | pp.30-43 | bilingual body and related figure/table assets |
| References | pp.12-21 | bibliography preserved in source PDF; not translated line-by-line |

## Terminology Ledger
| Canonical term | Chinese rendering | Decision |
|---|---|---|
| SIMWORLD STUDIO | SIMWORLD STUDIO | 平台名，保持英文大写。 |
| SIMCODER | SIMCODER | 核心编码智能体，负责生成、验证、修复 UE5 环境。 |
| embodied learning environment | 具身学习环境 | 不是静态 3D 场景，而是可交互、可训练、可验证的环境。 |
| Unreal Engine 5 / UE5 | Unreal Engine 5 / UE5 | 底层渲染与物理引擎。 |
| MCP bridge | MCP 桥接 | Model Context Protocol 工具调用层。 |
| Skill/Tool Library | 技能/工具库 | 工具是可调用 Python 函数，技能是可复用组合程序。 |
| self-evolution | 自我演化 | 把一次性修复沉淀为可复用工具或技能。 |
| co-evolution | 共同演化 | 环境生成器根据具身智能体表现调整后续环境，智能体也从新环境中学习。 |
| Gymnasium-style environment | Gymnasium 风格环境 | 提供 reset/step 接口、观测、奖励与终止信号。 |
| PointNav / ObjectNav | PointNav / ObjectNav | 点导航与目标导航任务。 |
| SR / SPL / SoftSPL / nDTW | SR / SPL / SoftSPL / nDTW | 导航成功率、路径效率、软路径效率与轨迹相似度指标。 |
| adaptive curriculum | 自适应课程 | 根据学习者能力边界动态调节任务难度。 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> LLM/VLM-based digital agents have advanced quickly because coding, web-navigation, and computer-use sandboxes provide abundant interactive training grounds. Embodied agents, by contrast, still lack automatically generated 3D worlds that are diverse, interactive, physically grounded, and exportable as learning environments. SimWorld Studio addresses this gap with an open-source Unreal Engine 5 platform. Its core agent, SimCoder, writes and executes engine-level code, uses verifier feedback such as compilation errors, physics checks, and VLM critiques, and self-evolves by adding reusable tools and skills to its library. The generated worlds expose Gym-style interfaces for embodied learning, and the platform further supports co-evolution: downstream agent performance guides SimCoder to generate adaptive curricula near the learner's capability frontier. Across three navigation case studies, self-evolution improves generation reliability, generated environments improve embodied-agent performance and transfer, and co-evolution yields an 18-point success-rate gain over fixed-environment learning and a 40-point gain over an untrained agent.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 基于 LLM/VLM 的数字智能体之所以进展很快，是因为代码、网页导航、电脑使用等任务都有大量可交互的训练沙箱。相比之下，具身智能体仍缺少自动生成的 3D 世界：这些世界不仅要多样，还要可交互、物理合理，并且能直接导出为学习环境。SimWorld Studio 正是为了解决这个缺口而提出的开源 Unreal Engine 5 平台。它的核心智能体 SimCoder 会编写并执行引擎级代码，利用编译错误、物理检查、VLM 批评等验证反馈进行修复，并通过把修复沉淀为可复用工具和技能来实现自我演化。生成的世界会暴露 Gym 风格接口，用于具身智能体学习；平台还支持共同演化：下游智能体的表现会反过来指导 SimCoder 生成贴近学习者能力边界的自适应课程。三个导航案例显示，自我演化提高了生成可靠性，生成环境能提升具身智能体并迁移到外部基准，而共同演化相比固定环境训练带来 18 个百分点成功率提升，相比未训练智能体带来 40 个百分点提升。

### Fig. 1. SimWorld Studio 总览与共同演化效果

![Fig. 1](fig1_simworld_overview.png)

**Caption:** SIMWORLD STUDIO: (Left) SIMCODER automatically generates UE5 interactive environments with realistic 3D scenes, learning tasks, and Gym interfaces. (Right) Co-evolving environment generation with embodied learning substantially improves test success over both fixed-environment training and the untrained-agent baseline.

**Caption[CN]:** SIMWORLD STUDIO：（左）SIMCODER 自动生成 UE5 交互环境，包括真实 3D 场景、学习任务和 Gym 接口。（右）环境生成与具身学习共同演化，相比固定环境训练和未训练基线显著提高测试成功率。

**Reading note:** 这张图把论文的两条主线放在一起：左边是可执行环境生成，右边是环境-智能体共同演化。

## 1 Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Large language and vision models have become increasingly capable digital agents: they can write and debug code, operate interfaces, browse the web, and solve multi-step software tasks. The paper argues that an important reason for this progress is not only model scale, but the existence of scalable interactive sandboxes where agents can act, receive feedback, and improve from experience. Embodied agents do not yet enjoy the same environmental abundance, even though LLMs and VLMs already provide useful priors for 3D perception, planning, and reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 大语言模型和视觉语言模型已经逐渐成为能力很强的数字智能体：它们能写代码、调试、操作界面、浏览网页，并完成多步软件任务。论文认为，这种进展的重要原因不只是模型规模，而是数字任务拥有可扩展的交互式沙箱，智能体可以在其中行动、获得反馈并从经验中改进。具身智能体还没有同等丰富的环境来源，尽管 LLM 和 VLM 已经为 3D 感知、规划和推理提供了有用先验。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The central bottleneck is environment simulation at scale. Existing embodied platforms such as AI2-THOR, Habitat, CARLA, ThreeDWorld, and iGibson provide valuable infrastructure, but they mostly depend on manually authored scene collections. Procedural generators improve scale, yet their diversity remains bounded by hand-written templates and rules. Recent LLM- or coding-agent-based 3D generation systems are more open-ended, but they typically generate static scenes and are evaluated as visual or geometric artifacts rather than deployable environments.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 核心瓶颈在于如何大规模模拟具身环境。AI2-THOR、Habitat、CARLA、ThreeDWorld、iGibson 等平台提供了重要基础设施，但大多依赖人工构建的场景库。程序化生成器提高了规模，但多样性仍受人工模板和规则限制。近期基于 LLM 或 coding agent 的 3D 生成系统更加开放，但通常只生成静态场景，并以视觉或几何产物的质量进行评估，而不是作为可部署环境来评估。
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The authors emphasize a distinction between scene generation and environment generation. For embodied learning, a generated world must let an agent perceive, act, receive task feedback, and be evaluated through a standard interface. It should define verifiable tasks, rewards, observations, and action spaces without manual integration. Moreover, the generator should adapt as the embodied agent improves, so environment generation becomes an adaptive curriculum rather than one-shot content creation.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 作者强调“场景生成”和“环境生成”的区别。对于具身学习而言，一个生成世界必须允许智能体感知、行动、获得任务反馈，并通过标准接口接受评估。它需要定义可验证任务、奖励、观测和动作空间，而不应依赖人工集成。更进一步，随着具身智能体变强，生成器也应随之调整，使环境生成从一次性内容创作变成自适应课程。
> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> SimWorld Studio is proposed as an Unreal Engine 5 platform for automatically generating evolving interactive embodied-learning environments. Its core component is SimCoder, a tool-augmented coding agent that creates realistic and physically grounded UE5 worlds from natural-language prompts, image guidance, and editing instructions. SimCoder does not merely place static assets; it writes engine-level code and iteratively repairs the scene using compilation, collision, physics, and VLM-verifier signals.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> SimWorld Studio 被提出为一个基于 Unreal Engine 5 的平台，用来自动生成会演化的交互式具身学习环境。核心组件是 SimCoder：一个工具增强的编码智能体，可以根据自然语言提示、图像指导和编辑指令创建真实且物理合理的 UE5 世界。SimCoder 不只是摆放静态资产；它会编写引擎级代码，并利用编译、碰撞、物理和 VLM 验证信号迭代修复场景。

### Fig. 2. SimCoder 自我演化生成循环

![Fig. 2](fig2_simcoder_loop.png)

**Caption:** SIMCODER turns a user prompt into an interactive environment through an automatic self-evolving loop: it writes tools, creates reusable skills, reuses them across iterations, and refines the scene with verifier feedback. NavMesh-based tools are used to generate solvable navigation tasks. SIMCODER further uses embodied-agent feedback to autonomously adapt environment difficulty and co-evolve with the embodied agent.

**Caption[CN]:** SIMCODER 通过自动自我演化循环把用户提示转化为交互环境：它编写工具、创建可复用技能、在迭代中复用它们，并通过验证器反馈细化场景。基于 NavMesh 的工具用于生成可解导航任务。SIMCODER 还利用具身智能体反馈自主调整环境难度，并与具身智能体共同演化。

**Reading note:** 重点看工具、技能、验证和紫色共同演化闭环的连接方式。
> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Every generated environment can be exported as a Gymnasium-style embodied environment with reset(), step(), task-dependent observations, action spaces, and reward signals. In the paper, navigation is used as the representative downstream task. Tasks are derived automatically from scene structure, including traversable regions, obstacles, goals, and spatial relations, so both LLM-based and conventional embodied agents can be deployed directly in generated worlds.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 每个生成环境都可以导出为 Gymnasium 风格的具身环境，包含 reset()、step()、任务相关观测、动作空间和奖励信号。论文以导航作为代表性下游任务。任务会从场景结构中自动派生，包括可通行区域、障碍物、目标和空间关系，因此基于 LLM 的策略和传统具身智能体都能直接部署到生成世界中。
> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The platform also closes the loop between environment generation and embodied learning. Signals from the learner, such as success, failure modes, and exploration coverage, are fed back to SimCoder. This lets future worlds target the learner's current weaknesses and remain near the frontier of its capability. In this sense, SimWorld Studio is not only a source of training environments, but an adaptive platform where the generator and the embodied agent improve together.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 平台还闭合了环境生成与具身学习之间的循环。学习者的成功率、失败模式、探索覆盖等信号会反馈给 SimCoder，使后续世界能够针对学习者当前弱点，并保持在其能力边界附近。因此，SimWorld Studio 不只是训练环境来源，而是一个生成器和具身智能体共同改进的自适应平台。
> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> The paper evaluates three linked claims. First, SimCoder can generate physically valid and prompt-aligned environments, and structured tools, verification, and self-evolution each contribute to quality. Second, embodied agents trained in generated environments improve and generalize to unseen navigation benchmarks. Third, co-evolution via an adaptive curriculum yields substantially better learning than fixed or random environment curricula.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 论文评估了三个相互关联的主张。第一，SimCoder 能生成物理有效且与提示对齐的环境，结构化工具、验证循环和自我演化都对质量有贡献。第二，在生成环境中训练的具身智能体会提升，并能泛化到未见过的导航基准。第三，通过自适应课程实现的共同演化显著优于固定环境或随机环境课程。

### Fig. 4. 三个案例研究

![Fig. 4](fig4_case_studies.png)

**Caption:** Three case studies evaluating SIMWORLD STUDIO. Case 1 evaluates SIMCODER’s scene generation quality across settings and LLM backbones. Case 2 trains embodied navigation agents in generated environments. Case 3 studies co-evolution where SIMCODER and the embodied agent iteratively improve each other.

**Caption[CN]:** 评估 SIMWORLD STUDIO 的三个案例研究。案例 1 评估 SIMCODER 在不同设置和 LLM backbone 下的场景生成质量。案例 2 在生成环境中训练具身导航智能体。案例 3 研究 SIMCODER 与具身智能体迭代互相改进的共同演化。

**Reading note:** 这张图是实验阅读路线图：生成质量、下游学习、闭环共同演化。

## 2 SimWorld Studio / SimCoder

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> SimWorld Studio is built on the open-source Unreal Engine 5 SimWorld library, inheriting its assets, runtime, and Python wrapper. The method has two main contributions: automatic environment generation, where a coding agent synthesizes executable 3D scenes and exports them as Gym-compatible environments; and co-evolution, where embodied-agent performance is fed back into generation so that new environments target current weaknesses.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> SimWorld Studio 构建在开源 Unreal Engine 5 的 SimWorld 库之上，继承其资产、运行时和 Python wrapper。方法上有两个主要贡献：一是自动环境生成，即编码智能体合成可执行 3D 场景，并将其导出为 Gym 兼容环境；二是共同演化，即把具身智能体表现反馈给环境生成，使新环境针对当前弱点。

### Fig. 3. SimWorld Studio 工作区界面

![Fig. 3](fig3_workspace.png)

**Caption:** The workspace supports the full environment-generation workflow in a single view. The top pipeline bar tracks progress across scene generation, task generation, agent training, and co-evolution. The left panel combines natural-language interaction with SIMCODER, executable scene and agent-control skills, and quick editing actions. The central viewport streams the live Unreal Engine scene, while the bottom asset browser exposes scene assets and saved versions. The right Scene Inspector shows scene health, summary, and VLM-based verification.

**Caption[CN]:** 工作区在单一视图中支持完整环境生成流程。顶部流程条跟踪场景生成、任务生成、智能体训练和共同演化进度。左侧面板结合与 SIMCODER 的自然语言交互、可执行场景/智能体控制技能和快速编辑操作。中央视口实时显示 Unreal Engine 场景，底部资产浏览器展示场景资产和保存版本，右侧 Scene Inspector 展示场景健康状态、摘要和 VLM 验证。

**Reading note:** 这张图说明 SimWorld Studio 是一个工程平台，而不只是一个离线生成算法。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The system contains three interacting parts: SimCoder, the LLM coding agent that drives generation; tool and skill libraries exposed through a Model Context Protocol bridge; and verifiers that return rule-based and VLM-based signals. Given a user prompt, SimCoder issues tool calls or retrieves skills, the backend executes them in UE5, and the resulting scene state or verifier feedback becomes the next observation for the coding agent.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 系统由三个交互部分组成：驱动生成的 LLM 编码智能体 SimCoder；通过 Model Context Protocol 桥接暴露的工具库和技能库；以及返回规则验证与 VLM 验证信号的验证器。给定用户提示后，SimCoder 发出工具调用或检索技能，UE5 后端执行这些操作，生成的场景状态或验证反馈会成为编码智能体的下一步观测。
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> MCP tools are Python function calls that operate on the UE backend. The primitive inventory includes fixed operations for actor management, environment management, asset management, and scene evaluation. Extensible tools are created when a useful one-off Python script becomes a recurring pattern; self-evolution promotes that script into a named wrapper registered as a first-class MCP tool.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> MCP 工具是作用于 UE 后端的 Python 函数调用。原始工具库包含 actor 管理、环境管理、资产管理和场景评估等固定操作。可扩展工具来自那些反复出现的一次性 Python 脚本：当某个模式被证明有用时，自我演化会把脚本提升为命名 wrapper，并注册成一等 MCP 工具。
> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Skills sit above tools. A skill is a Markdown document that records how to compose one or more tools to achieve a higher-level scene-construction goal. Primitive skills cover common composition goals such as building placement, city layout, and screenshot capture for the VLM judge. Extensible skills accumulate over time when SimCoder turns a successful repair or construction pattern into a reusable procedure.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 技能位于工具之上。一个技能是 Markdown 文档，记录如何组合一个或多个工具来达成更高层的场景构建目标。原始技能覆盖常见组合目标，例如建筑摆放、城市布局、为 VLM judge 截图等。可扩展技能则随着时间积累：当 SimCoder 把成功的修复或构建模式沉淀为可复用过程时，技能库就会成长。
> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The verification loop combines physical and semantic checks. A rule-based verifier computes scene-graph metrics such as collision, support, and in-bounds placement after actor-modifying calls. A VLM verifier captures multi-view screenshots and scores semantic alignment to the prompt, returning structured critiques. These critiques are not merely final evaluation; they re-enter the generation trajectory and guide the next repair step.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 验证循环结合物理检查和语义检查。规则验证器在修改 actor 的调用后计算场景图指标，如碰撞、支撑和是否在边界内。VLM 验证器捕获多视角截图，评估与提示的语义对齐，并返回结构化批评。这些批评不只是最终评估，而是重新进入生成轨迹，指导下一步修复。
> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Self-evolution turns repeated failures into permanent capabilities. When a verifier failure recurs, SimCoder restates the issue as a class of cases and authors a new tool or skill that addresses the class, not just the current instance. In the maze example, after detecting blockers and poor navigability, SimCoder writes a reusable clear_maze skill that can remove redundant blockers from future container layouts.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 自我演化把反复出现的失败变成永久能力。当某类验证失败重复出现时，SimCoder 会把问题重新表述为一类情况，并编写一个针对该类情况的新工具或技能，而不是只修补当前样例。在迷宫示例中，系统检测到阻挡物过多和可通行性差之后，SimCoder 写出可复用的 clear_maze 技能，用于未来容器布局中移除冗余障碍。

### Fig. 5. SimCoder 组件消融

![Fig. 5](fig5_ablation.png)

**Caption:** Ablation study results for SIMCODER in Case Study 1.

**Caption[CN]:** 案例研究 1 中 SIMCODER 的消融结果。

**Reading note:** 从 vanilla 到 MCP tools、verification、self-evolution 的逐步提升，是支持方法设计的关键证据。
> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Task generation is performed on top of the constructed scene. For navigation, SimCoder queries scene structure such as the NavMesh, samples start and goal positions, checks connectivity, and creates either PointNav or ObjectNav tasks. Solvability is enforced through NavMesh connectivity, and task success can be verified by querying the agent pose and target location during execution.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 任务生成发生在已构建场景之上。对于导航任务，SimCoder 查询 NavMesh 等场景结构，采样起点和目标点，检查连通性，并创建 PointNav 或 ObjectNav 任务。可解性通过 NavMesh 连通性保证；执行时则通过查询智能体位姿和目标位置来验证任务是否成功。
> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> A compiled environment exposes a standard Gymnasium interface: reset() and step(action) return RGB-D observations, agent pose, reward, termination, truncation, and info. Because the interface is standard, both off-the-shelf reinforcement-learning algorithms such as PPO and training-free LLM policies such as ReAct can be connected without changing the generated scene.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 编译后的环境暴露标准 Gymnasium 接口：reset() 和 step(action) 返回 RGB-D 观测、智能体位姿、奖励、终止、截断和 info。由于接口是标准的，PPO 等现成强化学习算法和 ReAct 等免训练 LLM 策略都可以直接接入，而不必修改生成场景。

## 2.2 Co-Evolution

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In the open-loop setting, the generator produces environments without knowing how the embodied agent performs in them. Co-evolution closes this loop. One round alternates between two updates: the embodied agent trains on a batch of SimCoder-generated environments, and SimCoder receives performance feedback before producing the next batch. The two agents update through different mechanisms, but their data flows are coupled.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在开环设置中，生成器并不知道具身智能体在生成环境中的表现。共同演化闭合了这个循环。每一轮在两个更新之间交替：具身智能体在一批 SimCoder 生成环境上训练；随后 SimCoder 接收表现反馈，再生成下一批环境。两个智能体通过不同机制更新，但数据流被耦合起来。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For the embodied agent, co-evolution looks like a changing environment distribution. The update rule itself does not need to change: an RL policy can still optimize rewards through standard policy gradients, while an LLM-based policy can update via reflection, incremental rules, or memory. The novelty is that the distribution of future scenes is no longer fixed; it is shaped by what the agent has or has not mastered.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 对具身智能体而言，共同演化表现为环境分布不断变化。更新规则本身不必改变：RL 策略仍然可以通过标准 policy gradient 优化奖励；基于 LLM 的策略也可以通过反思、增量规则或记忆更新。新意在于未来场景分布不再固定，而是由智能体已经掌握或尚未掌握的能力塑造。
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> For SimCoder, the update is in-context rather than weight-based. Between rounds, the embodied agent's performance is supplied as context, and SimCoder reweights skill retrievals and tool invocations. It can increase difficulty where success rates plateau, reduce it where the agent stalls, or oversample structural features that the agent has not yet mastered. Feedback can be scene-level, outcome-level, or trajectory-level.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 对 SimCoder 而言，更新是上下文内更新，而不是修改模型权重。每轮之间，具身智能体的表现会作为上下文提供给 SimCoder，后者重新调整技能检索和工具调用：在成功率停滞处提高难度，在智能体卡住处降低难度，或过采样智能体尚未掌握的结构特征。反馈可以是场景级、结果级或轨迹级。

## 3 Experiments Overview

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The experiments are organized as three case studies of increasing scope. Case Study 1 asks whether SimCoder can generate valid and diverse environments from text, image-plus-text, and scene-editing prompts. Case Study 2 asks whether embodied agents can learn useful navigation abilities from generated environments and transfer to unseen scenes. Case Study 3 asks whether SimCoder and the embodied agent can co-evolve through an adaptive curriculum.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 实验按范围递增组织成三个案例研究。案例 1 问 SimCoder 是否能从文本、图像加文本、场景编辑提示中生成有效且多样的环境。案例 2 问具身智能体是否能从生成环境中学习有用导航能力，并迁移到未见场景。案例 3 问 SimCoder 和具身智能体是否能通过自适应课程共同演化。

## 3.1 Case Study 1: Environment Generation Quality

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The first case study evaluates whether SimCoder can generate physically plausible 3D environments from language prompts, reference images, and editing instructions. The settings are S1 text-to-scene, S2 image-plus-text-to-scene, and S3 scene editing. Each setting is tested at easy, medium, and hard difficulty, producing 9 evaluation scenes. The evaluation combines rule-based metrics for physical validity and VLM-as-judge metrics for semantic alignment.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 第一个案例研究评估 SimCoder 是否能根据语言提示、参考图像和编辑指令生成物理合理的 3D 环境。设置包括 S1 文本到场景、S2 图像加文本到场景、S3 场景编辑。每个设置测试 easy、medium、hard 三个难度，共 9 个评估场景。评估结合规则指标衡量物理有效性，并用 VLM-as-judge 指标衡量语义对齐。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The model comparison isolates the underlying coding model while keeping the Claude Code agent framework, MCP tool interface, verification loop, and skill library fixed. The paper compares Claude Opus 4.6, Claude Sonnet 4.6, Qwen3.5-27B, and Qwen3.5-9B. In the averaged results, stronger coding models generate higher-quality scenes: Opus 4.6 reaches average scores of 0.77, 0.79, and 0.75 across S1, S2, and S3, while Sonnet 4.6 reaches 0.70, 0.73, and 0.74.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 模型比较固定 Claude Code agent 框架、MCP 工具接口、验证循环和技能库，只改变底层编码模型。论文比较 Claude Opus 4.6、Claude Sonnet 4.6、Qwen3.5-27B 和 Qwen3.5-9B。平均结果显示，更强的编码模型能生成更高质量场景：Opus 4.6 在 S1、S2、S3 的平均分分别为 0.77、0.79、0.75；Sonnet 4.6 分别为 0.70、0.73、0.74。
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> A compact reading of Table 1 is that physical validity becomes strong once the coding model and tool interface are capable enough, while semantic quality still scales with model size and input modality. Image guidance helps smaller models by anchoring layout, as shown by Qwen3.5-27B improving from 0.59 in text-to-scene to 0.67 in image-plus-text-to-scene.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 对表 1 的紧凑读法是：当编码模型和工具接口足够强时，物理有效性会变得很高；但语义质量仍随模型规模和输入模态变化。图像指导能通过锚定布局帮助较小模型，例如 Qwen3.5-27B 从文本到场景的 0.59 提升到图像加文本到场景的 0.67。
> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The ablation study separates three platform components beyond a vanilla coding agent: MCP tools, verification, and self-evolution. A vanilla agent scores only 0.16. Adding customized MCP tools raises quality to 0.45, adding the verification loop further improves quality by 0.10, and adding self-evolution contributes another 0.21. The key message is that structured tool access is a prerequisite, while self-evolution provides the largest incremental gain by converting experience into reusable knowledge.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 消融实验拆分了 vanilla coding agent 之外的三个平台组件：MCP 工具、验证循环和自我演化。vanilla agent 只有 0.16 分；加入定制 MCP 工具后提升到 0.45；再加入验证循环提升 0.10；最后加入自我演化又提升 0.21。核心信息是：结构化工具访问是硬前提，而自我演化通过把经验转化为可复用知识，带来最大的增量收益。
> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The qualitative medieval-village example shows what the platform actually produces. Given a rich prompt describing a cobblestone lane, timbered houses, a tavern, clutter, barrels, a well, market canopies, and villagers, SimCoder uses tools and skills to create comparable UE5 scenes across backbones. The example also exposes the intermediate abstraction levels: a Python MCP tool, a Markdown skill for packing buildings, and generated Python code for arranging the scene.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 中世纪村庄的定性例子展示了平台实际生成的内容。给定一个复杂提示，要求鹅卵石道路、木架房屋、酒馆、杂物、桶、水井、市场棚和村民，SimCoder 会利用工具和技能，在不同 backbone 上生成可比较的 UE5 场景。该例子还展示了中间抽象层：Python MCP 工具、用于排列建筑的 Markdown 技能，以及用于布置场景的生成式 Python 代码。

### Fig. 6. 中世纪村庄生成案例

![Fig. 6](fig6_medieval_scene.png)

**Caption:** Qualitative medieval village scene comparison. Each generated scene is paired with its corresponding text-to-scene evaluation scores. Scores are normalized to [0, 1]; higher is better.

**Caption[CN]:** 中世纪村庄场景的定性比较。每个生成场景都配有相应的文本到场景评估分数。分数归一化到 [0, 1]，越高越好。

**Reading note:** 可以直观看到不同编码模型在同一复杂提示下的布局、物体密度和物理合理性差异。

## 3.2 Case Study 2: Embodied Navigation Learning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The second case study uses navigation as a functional probe of environment quality. The tasks are PointNav, where the agent navigates to a target coordinate, and ObjectNav, where it navigates to a target object category. Episodes are generated on SimWorld Studio maps through UE5 NavMesh by sampling start-goal pairs, computing shortest-path references, and filtering by reachability and path length.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 第二个案例研究把导航作为环境质量的功能性探针。任务包括 PointNav，即智能体导航到目标坐标；以及 ObjectNav，即智能体导航到目标物体类别。episodes 通过 UE5 NavMesh 在 SimWorld Studio 地图上生成：采样起点和目标，计算最短路径参考，并按可达性和路径长度过滤。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For each task, the authors sample 1.2K training episodes and evaluate on 329 held-out SimWorld Studio episodes. They additionally test cross-benchmark transfer on SimWorld-MMNav. To study diversity, they vary the number of distinct training environments from 1 to 30 while holding the total training budget fixed at 200 episodes.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 对每个任务，作者采样 1.2K 个训练 episode，并在 329 个 held-out SimWorld Studio episode 上评估。他们还在 SimWorld-MMNav 上测试跨基准迁移。为了研究多样性，作者把不同训练环境数量从 1 增加到 30，同时保持总训练预算为 200 个 episode。
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The reported metrics include Success Rate for task completion, SPL and SoftSPL for path efficiency, and nDTW for trajectory fidelity. The evaluated policies are Qwen3.5-2B, Qwen3.5-9B, and Qwen3.5-27B, with and without an agent memory mechanism inspired by Generative Agents and ExpeL. The memory updates at step, trajectory, and task granularities so strategies can be retrieved at the right scope during inference.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 报告指标包括衡量任务完成的成功率 SR，衡量路径效率的 SPL 和 SoftSPL，以及衡量轨迹相似度的 nDTW。评估策略包括 Qwen3.5-2B、Qwen3.5-9B、Qwen3.5-27B，并比较有无 agent memory。该记忆机制受 Generative Agents 和 ExpeL 启发，在 step、trajectory 和 task 三个粒度更新，使策略能在推理时以合适范围检索经验。
> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> On held-out generated environments, training in SimWorld Studio improves every model scale. For Qwen3.5-27B, PointNav SR rises from 20.21 to 26.76 and ObjectNav SR from 22.56 to 31.59. For Qwen3.5-9B, ObjectNav SR rises from 0.00 to 14.62. For Qwen3.5-2B, ObjectNav SR rises from 0.24 to 4.58. These gains indicate that the generated environments provide usable navigation experience rather than only visually pleasing scenes.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在 held-out 生成环境上，SimWorld Studio 训练提升了所有模型规模。Qwen3.5-27B 的 PointNav SR 从 20.21 提升到 26.76，ObjectNav SR 从 22.56 提升到 31.59。Qwen3.5-9B 的 ObjectNav SR 从 0.00 提升到 14.62。Qwen3.5-2B 的 ObjectNav SR 从 0.24 提升到 4.58。这说明生成环境提供的是可用于导航学习的经验，而不仅是视觉上好看的场景。

### Table 2. 生成环境上的具身导航结果

![Table 2](table2_navigation_results.png)

**Caption:** Embodied navigation on generated environments. The table reports SR, SPL, SoftSPL, and nDTW for Point Navigation and Object Navigation.

**Caption[CN]:** 生成环境上的具身导航结果。表格报告 Point Navigation 和 Object Navigation 的 SR、SPL、SoftSPL 和 nDTW。

**Reading note:** 最关键的是同一模型从 baseline 到 +Memory 的提升，说明生成环境可以产生可学习经验。
> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The diversity analysis connects environment generation to generalization. With the same number of total training episodes, more distinct SimWorld Studio environments yield higher test success. The effect is especially visible for Qwen3.5-27B, where success improves by 5.5 percentage points. Transfer to SimWorld-MMNav further suggests that the agents acquire reusable navigation behavior rather than memorizing the generated maps.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 多样性分析把环境生成和泛化联系起来。在总训练 episode 数相同的情况下，更多不同的 SimWorld Studio 环境会带来更高测试成功率。这个效果在 Qwen3.5-27B 上尤其明显，成功率提升 5.5 个百分点。迁移到 SimWorld-MMNav 的结果进一步说明，智能体学到的是可复用导航行为，而不是记住生成地图。

## 3.3 Case Study 3: Co-Evolution

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The third case study instantiates a performance-gated adaptive curriculum. Navigation difficulty is parameterized by two axes, path length and obstacle density, jointly quantized into eight levels. In each round, SimCoder generates a batch of episodes at the current difficulty; the embodied agent attempts them and distills failed trajectories into prioritized decision rules; then SimCoder advances difficulty if the agent passes a mastery threshold or holds the current level if the agent struggles.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 第三个案例研究实例化了一种基于表现门控的自适应课程。导航难度由两条轴刻画：路径长度和障碍物密度，二者共同量化成 8 个难度等级。每轮中，SimCoder 在当前难度生成一批 episode；具身智能体尝试这些任务，并把失败轨迹蒸馏成优先级决策规则；随后，如果智能体超过掌握阈值，SimCoder 就提升难度，否则保持当前难度等待智能体追上。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The evaluation uses Qwen3.5-9B on the external SimWorld-MMNav benchmark and compares four settings: the full co-evolving environment, a fixed-difficulty environment held at level 3, a random-difficulty environment sampling levels 0 to 7, and the base model without embodied learning. The design tests whether adaptively matching difficulty to the learner is better than simply adding generated experience.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 评估在外部 SimWorld-MMNav 基准上使用 Qwen3.5-9B，比较四种设置：完整共同演化环境、固定在 level 3 的固定难度环境、从 level 0 到 7 随机采样的随机难度环境，以及不进行具身学习的基础模型。这个设计检验的是：把难度自适应匹配到学习者，是否优于简单增加生成经验。
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The co-evolving system shows a drop-and-recover training pattern: success drops when SimCoder introduces harder tasks, then recovers as the embodied agent transfers distilled strategies to the new tier. The final test success reaches 90% on SimWorld-MMNav, compared with 72% for fixed-environment learning and 50% for the untrained base model. This is the paper's strongest evidence that environment generation is more valuable when shaped by learner feedback.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 共同演化系统呈现“下降再恢复”的训练动态：当 SimCoder 引入更难任务时，成功率会下降；随后，具身智能体把蒸馏出的策略迁移到新难度层级，成功率又恢复。最终在 SimWorld-MMNav 上测试成功率达到 90%，而固定环境学习为 72%，未训练基础模型为 50%。这是论文中最强的证据：当环境生成被学习者反馈塑造时，其价值会更高。
> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The platform comparison table positions SimWorld Studio among simulators, generative scene-construction systems, and co-evolution methods. Its claimed differentiator is the simultaneous support for diverse generation, high physical/visual realism through UE5, a standard Gym interface, self-evolution from verifier feedback, and co-evolution from downstream agent performance. Most earlier platforms cover only a subset of these columns.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 平台比较表把 SimWorld Studio 放在具身模拟器、生成式场景构建系统和环境-智能体共同演化方法之间。它声称的差异点是同时支持多样化生成、通过 UE5 获得较高物理/视觉真实感、标准 Gym 接口、来自验证反馈的自我演化，以及来自下游智能体表现的共同演化。多数已有平台只覆盖其中一部分列。

### Table 3. 平台能力比较

![Table 3](table3_platform_comparison.png)

**Caption:** Comparison with representative embodied simulation platforms, generative scene-construction systems, and environment-agent co-evolution methods.

**Caption[CN]:** 与代表性的具身模拟平台、生成式场景构建系统和环境-智能体共同演化方法比较。

**Reading note:** 看最后几列：Gym Interface、Self-Evolution、Co-Evolution 是论文希望同时占住的能力。

## 4 Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper divides embodied simulation platforms into hand-built simulators, procedural generators, and LLM-based scene synthesizers. Hand-built platforms support navigation, manipulation, driving, robotics, and language-grounded games, but fixed manual scene catalogs are expensive to extend. Procedural platforms scale the number of environments but remain constrained by templates. LLM-based scene synthesizers provide open-ended diversity, but often stop at static 3D content without tasks, interfaces, or learning signals.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文把具身模拟平台分成三类：人工构建模拟器、程序化生成器和基于 LLM 的场景合成器。人工平台支持导航、操作、驾驶、机器人和语言落地游戏，但固定人工场景库昂贵且难扩展。程序化平台能扩大环境数量，但仍受模板限制。基于 LLM 的场景合成器提供开放多样性，但往往停留在静态 3D 内容，没有任务、接口或学习信号。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For agent-environment co-evolution, prior unsupervised environment design methods edit parametric environments to keep difficulty near the agent's frontier. LLM-based extensions revise rewards, configurations, or task programs from agent feedback, but usually tune pre-built simulators rather than construct scenes. SimWorld Studio's claimed step is to synthesize photorealistic UE5 scenes through engine-level tool calls and reusable skills, then expose them through RGB-D observations, agent pose, and physical reward under a Gym contract.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在智能体-环境共同演化方面，已有无监督环境设计方法会编辑参数化环境，使难度保持在智能体能力边界附近。基于 LLM 的扩展会根据智能体反馈修订奖励、配置或任务程序，但通常是在预建模拟器中调参，而不是构建完整场景。SimWorld Studio 声称的推进是：通过引擎级工具调用和可复用技能合成照片级 UE5 场景，再通过 Gym 合约暴露 RGB-D 观测、智能体位姿和物理奖励。

## 5 Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The conclusion states the paper's central thesis: the bottleneck of static scene generation can be addressed by synthesizing scalable, interactive 3D environments for embodied learning. A self-evolving coding agent translates prompts into Gymnasium-compatible worlds, and a co-evolution loop adapts their difficulty according to embodied-agent performance. The authors frame this as a self-improving paradigm for embodied AI research.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 结论重申论文中心论点：静态场景生成的瓶颈可以通过合成可扩展、可交互的 3D 具身学习环境来缓解。一个自我演化的编码智能体把提示转换成 Gymnasium 兼容世界，而共同演化循环会根据具身智能体表现调整难度。作者将其定位为具身 AI 研究的一种自我改进范式。

## Limitations and Broader Impact

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> A current limitation is that SimWorld Studio remains bounded by the capability of the underlying coding agent. Complex 3D generation requires spatial reasoning over object placement, geometric constraints, physical plausibility, navigability, and long-range layout consistency. The current system can produce useful scenes, but failures may still occur when the task requires fine-grained spatial planning or precise multi-object arrangement.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 当前限制是 SimWorld Studio 仍受底层编码智能体能力约束。复杂 3D 生成需要对物体摆放、几何约束、物理合理性、可通行性和长程布局一致性进行空间推理。当前系统已经能生成有用场景，但当任务需要细粒度空间规划或精确多物体布置时，仍可能失败。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The broader-impact section highlights productivity benefits for 3D environment creation, especially in engines such as Unreal Engine where coding-agent support is still limited. By letting agents directly edit, validate, and reuse scene-building skills, the platform may reduce repetitive engineering work and make interactive environment construction more accessible to researchers and developers.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 更广泛影响部分强调了 3D 环境创作的生产力收益，尤其是在 Unreal Engine 这类现有 coding-agent 支持仍有限的复杂引擎中。通过让智能体直接编辑、验证并复用场景构建技能，平台可能减少重复工程工作，使研究者和开发者更容易构建交互环境。
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The same automation also introduces risks. More capable scene-generation agents can be misused to create deceptive, unsafe, or biased simulated worlds, or to produce environments that violate asset licenses. The paper therefore treats asset provenance, model access, and software licensing as part of the platform's practical deployment concerns rather than purely legal afterthoughts.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 同样的自动化也带来风险。更强的场景生成智能体可能被滥用于创建欺骗性、不安全或有偏见的模拟世界，或生成违反资产许可的环境。因此，论文把资产来源、模型访问和软件许可视为平台实际部署的一部分，而不是事后才考虑的法律细节。

## Appendix: Interface, Configuration, and Evaluation Details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The appendix provides representative interface views. The light-theme main interface integrates user-agent interaction, UE scene rendering, asset/backend management, Gym environment APIs, and embodied-agent monitoring. Dark-theme panels further show skill management, tool abstraction, and direct embodied interaction, allowing users to move beyond text-only prompting and inspect generated environments through controllable agents.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 附录给出了代表性界面视图。浅色主题主界面集成了用户-智能体交互、UE 场景渲染、资产/后端管理、Gym 环境 API 和具身智能体监控。深色主题面板进一步展示技能管理、工具抽象和直接具身交互，使用户不止能文本提示，还能通过可控智能体检查生成环境。

### Fig. 10. 代表性界面视图

![Fig. 10](fig10_interface_views.png)

**Caption:** Representative interface views of SIMWORLD STUDIO. The light-theme main interface provides an integrated workspace for user-agent interaction, UE scene rendering, asset/backend management, Gym environment APIs, and embodied-agent monitoring. The dark-theme panels show specialized views for skill management, tool abstraction, and direct embodied interaction.

**Caption[CN]:** SIMWORLD STUDIO 的代表性界面视图。浅色主题主界面提供集成工作区，支持用户-智能体交互、UE 场景渲染、资产/后端管理、Gym 环境 API 和具身智能体监控。深色主题面板展示技能管理、工具抽象和直接具身交互等专门视图。

**Reading note:** 这张附录图帮助理解平台在真实使用时如何组织工具、技能和交互。
> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The running-configuration appendix lists practical requirements: Linux with Ubuntu 20.04+ recommended, an NVIDIA GPU with at least 8GB VRAM, NVIDIA driver version 525+ with Vulkan support, Node.js 18+, Python 3.9+, and roughly 40GB free disk space. This matters because the method is not just a model prompt; it depends on a full UE5 backend, asset library, Python execution, and rendering/physics stack.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 运行配置附录列出了实际需求：Linux，推荐 Ubuntu 20.04+；至少 8GB VRAM 的 NVIDIA GPU；支持 Vulkan 的 525+ NVIDIA 驱动；Node.js 18+；Python 3.9+；以及约 40GB 可用磁盘空间。这一点重要，因为该方法不是单纯的模型提示，而依赖完整 UE5 后端、资产库、Python 执行以及渲染/物理栈。
> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The assets, licenses, and model-access appendix records the external software, model APIs, and assets used by the platform. This is an important reproducibility layer: because SimWorld Studio generates environments by invoking code, tools, engines, models, and asset libraries, reproducibility depends on software versions and access permissions as much as on algorithmic descriptions.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 资产、许可和模型访问附录记录了平台使用的外部软件、模型 API 和资产。这是重要的可复现层：因为 SimWorld Studio 通过调用代码、工具、引擎、模型和资产库来生成环境，可复现性不仅取决于算法描述，也取决于软件版本和访问权限。
> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The evaluation appendices provide detailed metric definitions and breakdowns. For scene generation, they expand rule-based metrics such as object count, diversity, collision, gravity, path-finding, spatial-relation fidelity, and layout aesthetics. For navigation, they define SR, SPL, SoftSPL, and nDTW, and include extra ablations over observation modalities, diversity, and adaptive difficulty.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 评估附录提供了详细指标定义和分项结果。对于场景生成，附录展开了物体数量、多样性、碰撞、重力、路径可达、空间关系保真和布局美学等规则/VLM 指标。对于导航，附录定义了 SR、SPL、SoftSPL 和 nDTW，并包含观测模态、多样性和自适应难度的额外消融。
> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The prompt-example appendix is especially useful for reproducing the paper's task distribution. It includes hard text-to-scene prompts such as generating a full residential neighborhood, image-plus-text prompts grounded in aerial photos, and scene-editing prompts that expand an existing plaza into a larger district. These examples clarify that the benchmark is not limited to toy rooms; it stresses spatial layout, object counts, roads, vegetation, obstacles, and task-relevant navigability.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 提示样例附录对复现任务分布特别有用。它包括困难文本到场景提示，例如生成完整住宅街区；基于航拍照片的图像加文本提示；以及把已有广场扩展成更大街区的场景编辑提示。这些样例说明，基准并不限于玩具房间，而是在考察空间布局、物体数量、道路、植被、障碍和任务相关可通行性。

## Compact Table: Scene Generation Average Scores

| LLM | S1 Text-to-Scene Avg | S2 Image+Text Avg | S3 Scene Editing Avg |
|---|---:|---:|---:|
| Qwen3.5-9B | 0.36 | 0.45 | 0.34 |
| Qwen3.5-27B | 0.59 | 0.67 | 0.52 |
| Claude Sonnet 4.6 | 0.70 | 0.73 | 0.74 |
| Claude Opus 4.6 | 0.77 | 0.79 | 0.75 |

**Table note[CN]:** 这是从原表中抽出的平均分读法；完整多指标表保留在源 PDF 与 `source_map.json` 的说明中。

## Reading Notes

- 这篇论文的关键不是“生成一个好看的 3D 场景”，而是把生成结果变成一个可训练、可验证、可共同演化的具身学习环境。
- 对 3D agent 研究最有用的连接点是：SimCoder 的工具/技能库可以看成 Skill-3D 的环境生成版；验证器反馈可以看成让技能库自我修补的监督信号。
- 评价时不要只看 scene quality，还要看下游 embodied policy 是否真的学到可迁移能力；这也是 SimWorld Studio 比静态 text-to-3D 更贴近 agent training 的地方。
- 当前最明显短板是 coding agent 的空间规划能力和平台工程成本；如果要复用这条线，建议优先抽象可验证的 3D 工具接口，而不是一开始就追求完整 UE5 平台。
