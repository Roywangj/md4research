# Self-Evolving Neuro-Symbolic Skills for Tool-Augmented Spatial Reasoning

> **Detailed bilingual reader / 逐段中英对照详细阅读稿**
>
> **Source:** Shi-Yu Tian, Zhuo-Xia Wang, Xuan-Yi Zhu, Zhi Zhou, Xinwei Yang, Kun-Yang Yu, Ming Yang, Yang Chen, Yu-Feng Li. *Self-Evolving Neuro-Symbolic Skills for Tool-Augmented Spatial Reasoning*. arXiv:2608.07955v1, 8 Aug 2026. Supplied PDF: 25 pages.
>
> **覆盖声明（2026-08-27）：** 本文件按 PDF 25 页的源顺序组织，覆盖标题、摘要、引言、相关工作、方法（含公式）、实验、结论、参考文献及 Supplementary Material A–D。正文采用相邻英文原文与中文翻译对；表格转录为可搜索 Markdown，图注均保留英文与中文。PDF 中的示例代码、JSON 键、提示词占位符、工具标识符、数值和输出格式均保持原样。由于当前输出边界不允许从 PDF 复制二进制图像，图像内容以双语图注和可检索的表格/代码文字保留；未插入图片链接，因此不存在断链。参考文献保留原始英文书目信息以便检索。

## Page and section index / 页码与章节索引

- pp. 1–2: Abstract, Introduction, Related Work
- pp. 3–7: Method (problem setup, skill formulation, inference, evolution)
- pp. 7–11: Experiments and analysis
- pp. 11–13: Conclusion and References
- pp. 14–25: Supplementary Material A–D (implementation, cases, learned skills, prompts)

## Terminology ledger / 术语表

| English | Chinese | Note |
|---|---|---|
| Tool-Use Skill | 工具使用技能 | A reusable ordered workflow of controller-visible tool atoms. |
| Geometry Skill | 几何技能 | A reusable, verifiable numerical/code kernel. |
| atomic instruction | 原子指令 | Typed executable operation with a local verifier. |
| FTCS | 首次通过组合工具链成功率 | First-Pass Compositional Tool-Chain Success Rate. |
| prequential accuracy | 预quential（先预测后揭示标签）准确率 | Each prediction is evaluated before its label enters evolution. |
| LVLM | 大型视觉语言模型 | Large vision-language model. |
| skill evolution | 技能演化 | Analysis, fusion, and pruning between episodes. |

# Abstract / 摘要

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Large vision-language models have achieved strong performance in multimodal reasoning, but they remain unreliable on fine-grained spatial tasks that demand both precise spatial perception and fine-grained geometric computation beyond end-to-end generation. Tool augmentation offers a natural solution, while existing methods either plan tool calls from scratch without explicit dependency constraints or rely on fixed pipelines that are redundant and generalize poorly across spatial tasks.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 大型视觉语言模型在多模态推理方面已经取得了很强的性能，但在细粒度空间任务上仍不可靠：这类任务同时要求精确的空间感知，以及超越端到端生成能力的细粒度几何计算。工具增强提供了自然的解决方案；然而，现有方法要么在没有显式依赖约束的情况下从头规划工具调用，要么依赖固定流水线，因而在空间任务中产生冗余且泛化能力较差。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> An effective spatial reasoning agent should instead accumulate reusable experience and adaptively compose it for new problems. To this end, we propose NeSy-Spatial, a neuro-symbolic framework for self-evolving spatial skills. NeSy-Spatial abstracts tool interactions and geometric operations into typed executable atomic instructions and composes them into two complementary skill types: Tool-Use Skills for organizing tool execution and Geometry Skills for structured geometric reasoning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 有效的空间推理智能体应当积累可复用经验，并针对新问题自适应地组合这些经验。为此，我们提出 NeSy-Spatial，一种用于自演化空间技能的神经符号框架。NeSy-Spatial 将工具交互和几何操作抽象为带类型、可执行的原子指令，并将其组合为两类互补技能：用于组织工具执行的 Tool-Use Skills，以及用于结构化几何推理的 Geometry Skills。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> During inference, NeSy-Spatial retrieves and executes relevant skills in a closed-loop process. During evolution, it analyzes buffered successful and failed trajectories to refine skill structures and prune unreliable or inactive entries. Experiments on three spatial reasoning benchmarks show that NeSy-Spatial consistently improves reasoning accuracy with more precise tool utilization.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在推理阶段，NeSy-Spatial 以闭环方式检索并执行相关技能。在演化阶段，它分析缓冲区中的成功与失败轨迹，以改进技能结构，并剪除不可靠或不活跃的条目。在三个空间推理基准上的实验表明，NeSy-Spatial 能够在提高工具使用精确性的同时，持续提升推理准确率。

# 1 Introduction / 引言

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Large vision-language models (LVLMs) have made substantial progress in general visual understanding (OpenAI 2023), yet they remain unreliable for fine-grained spatial reasoning (Yang et al. 2025a; Chen et al. 2025c). Unlike generic visual understanding, spatial reasoning often requires explicit geometric reasoning and intermediate verification beyond end-to-end generation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 大型视觉语言模型（LVLM）在通用视觉理解方面取得了显著进展（OpenAI 2023），但在细粒度空间推理上仍然不可靠（Yang et al. 2025a；Chen et al. 2025c）。与一般视觉理解不同，空间推理通常要求显式的几何推理和中间结果验证，而不能只依靠端到端生成。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Such reasoning is difficult to accomplish using LVLMs alone, as it depends on precise visual perception and structured geometric computation. Tool augmentation has therefore emerged as an effective solution (Zhang et al. 2025; Yu et al. 2026; Tian et al. 2026), enabling LVLMs to leverage specialized vision models and external executors such as depth estimators (Yang et al. 2024) or reconstruction models (Wang et al. 2025a) to obtain reliable intermediate evidence for reasoning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 仅凭 LVLM 很难完成这类推理，因为它依赖精确的视觉感知和结构化的几何计算。因此，工具增强逐渐成为有效方案（Zhang et al. 2025；Yu et al. 2026；Tian et al. 2026）：它使 LVLM 能够调用专门的视觉模型和外部执行器，例如深度估计器（Yang et al. 2024）或重建模型（Wang et al. 2025a），从而获得可靠的中间证据。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Existing tool-augmented methods mainly follow two paradigms. One line dynamically plans tool calls from a general-purpose toolbox for each query, while another executes a manually designed pipeline tailored to a specific class of spatial reasoning tasks.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 现有工具增强方法主要遵循两种范式。一类方法针对每个查询，从通用工具箱中动态规划工具调用；另一类方法执行为某类空间推理任务手工设计的流水线。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Although dynamic planning is highly flexible, it lacks explicit constraints on tool dependencies and execution order. Agents may therefore generate invalid sequences—for example, invoking a Python interpreter before acquiring prerequisite grounded object coordinates or point-cloud representations. Fixed pipelines enforce a valid order but often invoke unnecessary tools regardless of task complexity, causing redundant computation and reduced efficiency.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 动态规划虽然非常灵活，却缺少对工具依赖关系和执行顺序的显式约束。因此，智能体可能生成无效序列，例如在获得必要的目标物体坐标或点云表示之前就调用 Python 解释器。固定流水线能够保证有效顺序，但往往不论任务复杂度都调用不必要的工具，造成冗余计算并降低效率。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Therefore, a spatial reasoning agent should abstract retrievable and composable skills from historical trajectories, rather than planning from scratch or relying on fixed templates. We identify two challenges: spatial skills involve both tool invocation and geometric processing; and skills are difficult to extract directly because successful trajectories may contain redundant steps while failed trajectories may still include locally effective operations.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 因此，空间推理智能体应当从历史轨迹中抽象出可检索、可组合的技能，而不是每次从头规划或依赖固定模板。这里有两个挑战：空间技能同时包含工具调用和几何处理；技能也难以直接从轨迹中提取，因为成功轨迹可能包含冗余步骤，而失败轨迹中仍可能包含局部有效的操作。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> To overcome this, we propose NeSy-Spatial, a neuro-symbolic framework for self-evolving skills in spatial reasoning. We define Tool-Use Skills, whose atomic instructions correspond to individual tool calls and whose high-level structures encode execution order and dependencies, and Geometry Skills, whose atomic instructions are executable functional code blocks for coordinate transformation, distance computation, and consistency checking.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 为解决上述问题，我们提出 NeSy-Spatial，一种用于空间推理自演化技能的神经符号框架。我们定义 Tool-Use Skills：其原子指令对应单个工具调用，高层结构编码执行顺序和依赖关系；同时定义 Geometry Skills：其原子指令是可执行的函数代码块，用于坐标变换、距离计算和一致性检查。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> NeSy-Spatial continuously learns and abstracts skills during online interaction. During inference it retrieves, instantiates, and executes relevant skills in a closed loop. During evolution it mines new atomic instructions and local rules from successful and failed trajectories, integrates them with existing skills, and removes unreliable or inactive entries according to verification results and usage patterns.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> NeSy-Spatial 在在线交互过程中持续学习和抽象技能。推理时，它以闭环方式检索、实例化并执行相关技能；演化时，它从成功和失败轨迹中挖掘新的原子指令与局部规则，将其与已有技能整合，并依据验证结果和使用模式删除不可靠或不活跃条目。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Our contributions are summarized as follows:
>
> - We introduce a neuro-symbolic definition of spatial skills that unifies tool invocation and geometric computation through typed executable atomic instructions.
> - We propose NeSy-Spatial, a skill self-evolution framework that updates atomic instructions and high-level Tool-Use and Geometry Skills from buffered trajectories through analysis, fusion, and pruning.
> - We evaluate NeSy-Spatial on multiple spatial reasoning benchmarks, showing improvements over base static tool-use agents and fixed-pipeline methods.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 本文贡献如下：
>
> - 提出空间技能的神经符号定义，通过带类型的可执行原子指令统一工具调用与几何计算；
> - 提出 NeSy-Spatial 技能自演化框架，通过分析、融合与剪枝，从轨迹缓冲区更新原子指令以及高层 Tool-Use Skills 和 Geometry Skills；
> - 在多个空间推理基准上评估 NeSy-Spatial，结果显示其优于静态工具使用智能体和固定流水线方法。

# 2 Related Work / 相关工作

## 2.1 Spatial Reasoning / 空间推理

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Spatial reasoning is the ability to interpret geometric relationships between objects and their environment. It is fundamental to robotic perception and embodied intelligence, as well as autonomous driving. Recent benchmarks extend earlier static settings to multi-view observations, viewpoint changes, scale estimation, and dynamic scenes, including BLINK, CVBench, VSI-Bench, and STI-Bench. Our evaluation covers MMSI, MindCube, and OmniSpatial.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 空间推理是理解物体及其环境之间几何关系的能力，是机器人感知、具身智能以及自动驾驶的基础。近期基准将早期的静态设置扩展到多视角观测、视点变化、尺度估计和动态场景，包括 BLINK、CVBench、VSI-Bench 与 STI-Bench。本文评估 MMSI、MindCube 和 OmniSpatial。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Despite advances in general perception, vision-language models still struggle with multi-step spatial inference, precise scale estimation, and viewpoint-dependent reasoning. Existing solutions include task-specific fine-tuning, progressive training, 3D-aware representations, and modular systems that invoke visual tools for detection, depth estimation, reconstruction, or geometric measurement.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 尽管通用感知能力不断进步，视觉语言模型在多步空间推断、精确尺度估计和依赖视点的推理方面仍然困难。现有方案包括任务特定微调、渐进式训练、3D 感知表示，以及调用检测、深度估计、重建或几何测量工具的模块化系统。

## 2.2 Skill Self-evolution / 技能自演化

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Skill self-evolution enables agents to abstract reusable knowledge from past interactions to improve future task solving. Reflection-based methods revise reasoning through feedback, self-critique, or external validation, while experience-driven methods retrieve knowledge abstracted from historical trajectories. Skill-memory systems maintain reusable skills or workflows to guide future actions.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 技能自演化使智能体能够从过去的交互中抽象可复用知识，从而改进未来的任务求解。基于反思的方法通过反馈、自我批评或外部验证修正推理；经验驱动的方法检索从历史轨迹中抽象的知识；技能记忆系统则维护可复用技能或工作流来指导后续行动。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Prior studies largely address text reasoning, web navigation, coding, or games, representing skills as instructions, workflows, or programs. Tool-augmented spatial reasoning instead requires coordination among visual perception, geometric computation, and multi-step inference. It therefore calls for reusable procedures that specify when to invoke tools, how to interpret their outputs, and how to transfer successful geometric reasoning across spatial tasks.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 以往研究主要处理文本推理、网页导航、编程或游戏，并将技能表示为指令、工作流或程序。工具增强的空间推理则要求协调视觉感知、几何计算和多步推断。因此，它需要可复用的过程：明确何时调用工具、如何解释工具输出，以及如何将成功的几何推理迁移到不同空间任务。

# 3 Method / 方法

## 3.1 Problem Setup / 问题设定

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We study online tool-augmented spatial reasoning. At episode $t$, the agent receives $x_t=(I_t,q_t)\in\mathcal I\times\mathcal Q$ and predicts $\hat y_t\in\mathcal Y$ using a tool set $\mathcal T=\mathcal T_{vis}\cup\mathcal T_{py}$ and a skill library $Lib_t=(A_t,S_t)$. The Python executor is exposed as a single tool-level atomic instruction, while its internal geometric computation is constructed from reusable Geometry Skills.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们研究在线工具增强空间推理。在第 $t$ 个 episode 中，智能体接收 $x_t=(I_t,q_t)\in\mathcal I\times\mathcal Q$，并使用工具集合 $\mathcal T=\mathcal T_{vis}\cup\mathcal T_{py}$ 与技能库 $Lib_t=(A_t,S_t)$ 预测 $\hat y_t\in\mathcal Y$。Python 执行器在工具层面被暴露为一个原子指令，而其内部几何计算由可复用的 Geometry Skills 构造。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> At reasoning step $k$, working memory $M_{t,k}$ maintains accumulated evidence, symbolic variables, execution history, verifier outcomes, and an answer hypothesis. During an episode, $Lib_t$ is fixed. Each prediction is recorded exactly once before the ground-truth answer is revealed; the label is used only to evaluate that prediction and assess the completed trajectory $\tau_t$, which is appended to the trajectory buffer $B_t$.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在推理步骤 $k$，工作记忆 $M_{t,k}$ 保存累积证据、符号变量、执行历史、验证器结果以及答案假设。在一个 episode 内，$Lib_t$ 保持不变。每个预测都在揭示真实答案之前恰好记录一次；标签只用于评估该预测和已完成轨迹 $\tau_t$，随后将轨迹加入轨迹缓冲区 $B_t$。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Once the buffer reaches $N_{buf}$, self-evolution extracts and integrates reusable structures and prunes unreliable or inactive entries to obtain $Lib_{t+1}$; otherwise, the library remains unchanged. Thus all library updates occur between episodes.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 当缓冲区达到 $N_{buf}$ 后，自演化过程会提取并整合可复用结构，同时剪除不可靠或不活跃条目，得到 $Lib_{t+1}$；否则技能库保持不变。因此，所有技能库更新都发生在 episode 之间。

## 3.2 Neuro-Symbolic Skill Formulation / 神经符号技能形式化

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Spatial reasoning must couple learned perception with verifiable geometric computation. At a fixed episode, we omit the time index and write the skill library as $Lib=(A,S),\qquad S=S_{tool}\cup S_{geo}$.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 空间推理必须将学习得到的感知与可验证的几何计算结合起来。在固定的 episode 中省略时间下标，技能库写作 $Lib=(A,S),\qquad S=S_{tool}\cup S_{geo}$。其中 $A$ 是可执行原子指令集合，$S_{tool}$ 和 $S_{geo}$ 分别包含 Tool-Use Skills 与 Geometry Skills。两类技能都由原子动作节点、有序边和实例化上下文表示。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> An atomic instruction is a typed executable operation with a local verifier: $a=(e_a,v_a),\qquad e_a:U_a\rightarrow O_a,\qquad v_a:O_a\rightarrow\{0,1\}$. Here $e_a$ maps typed inputs $U_a$ to outputs $O_a$, and $v_a$ validates the output. We partition $A$ into controller-visible tool atoms $A_{tool}$ and internal geometry atoms $A_{geo}$. Geometry atoms execute inside the Python tool rather than being selected as independent controller actions.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 原子指令是带有局部验证器的、带类型的可执行操作：上式中 $e_a$ 将带类型输入 $U_a$ 映射为输出 $O_a$，而 $v_a$ 验证输出。我们将 $A$ 划分为控制器可见的工具原子 $A_{tool}$ 与内部几何原子 $A_{geo}$。几何原子在 Python 工具内部执行，而不是作为独立的控制器动作被选择。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Each high-level skill is a node–edge–context structure $s=(V,E,\kappa)$, where $V\subseteq A$, $E\subseteq V\times V$ specifies execution dependencies, and $\kappa$ stores the context required for instantiation. Tool-Use Skills organize controller-visible tool atoms into reusable workflows; Geometry Skills provide reusable and verifiable implementations for Python calls.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 每个高层技能都是节点—边—上下文结构 $s=(V,E,\kappa)$，其中 $V\subseteq A$，$E\subseteq V\times V$ 指定执行依赖关系，$\kappa$ 保存实例化所需上下文。Tool-Use Skills 将控制器可见的工具原子组织成可复用工作流；Geometry Skills 为 Python 调用提供可复用且可验证的实现。

## 3.3 Skill-Guided Spatial Reasoning / 技能引导的空间推理

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> During inference, each iteration follows four stages: Skill Retrieval, Action Selection, Tool/Code Execution, and State Update. The loop repeats until the accumulated state is sufficient to produce an answer.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 推理期间，每次迭代依次包含四个阶段：技能检索、动作选择、工具/代码执行和状态更新。该循环持续进行，直到累积状态足以产生答案。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Skill Retrieval converts the question and current state into a structured decision context and queries the skill library for a small candidate set: $C_{t,k}=LLMRetrieve(I_t,q_t,M_{t,k};S_t)$.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 技能检索阶段将问题和当前状态转换为结构化决策上下文，并从技能库中查询少量候选技能。候选集合 $C_{t,k}$ 可以包含 Tool-Use Skills 或 Geometry Skills；检索接口通过任务特定模板暴露目标对象、参照对象、关系、现有证据和所需几何操作。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Given the retrieved candidates and current state, the controller selects the next action: $u_{t,k}=LLMSelect(I_t,q_t,M_{t,k},C_{t,k})$, with $u_{t,k}\in\{stop\}\cup(C_{t,k}\cap S_{tool,t})\cup A_{tool,t}$.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 给定检索到的候选技能与当前状态，控制器选择下一动作。它可以终止并返回当前答案、激活或恢复一个 Tool-Use Skill，或直接调用兼容的工具原子。Geometry Skills 不是独立控制器动作，而是在 Python 原子内部实例化。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The selected action executes either a single tool atom or the next dependency-ready node of an active Tool-Use Skill. Visual tool atoms return perceptual evidence directly. When execution reaches the Python atom, the agent binds required artifacts from $M_{t,k}$ and instantiates a compatible retrieved Geometry Skill. Its code blocks execute in dependency order and return numerical outputs and verifier outcomes.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 所选动作要么执行单个工具原子，要么执行当前 Tool-Use Skill 中下一个依赖就绪的节点。视觉工具原子直接返回感知证据。当执行到 Python 原子时，智能体从 $M_{t,k}$ 绑定所需对象，并实例化兼容的 Geometry Skill；其代码块按依赖顺序执行，同时返回数值输出和验证器结果。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> For a non-terminal action, the complete iteration is $(I_t,q_t,M_{t,k})\rightarrow C_{t,k}\rightarrow u_{t,k}\rightarrow(o_{t,k},\nu_{t,k})\rightarrow M_{t,k+1}$, where $o_{t,k}$ is the execution output and $\nu_{t,k}\in\{0,1\}$ indicates whether execution and local verification succeed.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 对于非终止动作，完整迭代如上式所示，其中 $o_{t,k}$ 是执行输出，$\nu_{t,k}\in\{0,1\}$ 表示执行和局部验证是否成功。除非控制器选择停止，否则更新后的状态会启动下一轮检索；最终答案评估完成后，完整轨迹会被保存以供批量自演化。

## 3.4 Skill Self-Evolution / 技能自演化

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The trajectory produced by episode $t$ is $\tau_t=((M_{t,k},u_{t,k},o_{t,k},\nu_{t,k})_{k=1}^{K_t},\hat y_t)$ and $B_{t+1}=B_t\cup\{\tau_t\}$. Self-evolution is triggered only when $|B_{t+1}|\ge N_{buf}$; otherwise $Lib_{t+1}=Lib_t$ and the buffer is retained.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 第 $t$ 个 episode 产生的轨迹如上式所示，其中 $K_t$ 是执行的节点级步骤数，$\hat y_t$ 是最终答案。只有当 $|B_{t+1}|\ge N_{buf}$ 时才触发自演化；否则 $Lib_{t+1}=Lib_t$，并保留缓冲区。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Trajectory Analysis decomposes each buffered trajectory into executed operations, arguments, produced artifacts, consumed variables, and local outcomes. It aggregates recurring dependency patterns and returns atomic-instruction updates together with supported and invalid skill fragments: $\Delta A_t,G_t^+,G_t^-=LLMAnalyze(B_{t+1})$. Supported fragments may require an atom $a_i$ before $a_j$; invalid fragments record transitions that repeatedly cause execution or verifier failures.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 轨迹分析将每条缓冲轨迹分解为执行操作、参数、产生的工件、消耗的变量和局部结果，聚合反复出现的依赖模式，并返回原子指令更新以及受支持和无效的技能片段。受支持片段可能要求先执行原子 $a_i$ 再执行 $a_j$；无效片段则记录反复导致执行或验证失败的转移。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Skill Fusion compares extracted atoms and fragments with the unified library and produces a structurally revised library: $Lib^{fuse}_{t+1}=LLMFusion(Lib_t,\Delta A_t,G_t^+,G_t^-)$. Fusion reconciles new instructions with existing implementations, then edits high-level skills by adding a supported fragment, deleting a redundant or incompatible dependency, or replacing an affected subgraph while preserving the remainder.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 技能融合将提取出的原子与片段和统一技能库比较，并产生结构修订后的库。融合首先协调新指令与已有实现，然后通过添加受支持片段、删除冗余或不兼容依赖，或在保留其余部分的同时替换受影响子图，编辑高层技能。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> For each $z\in A^{fuse}_{t+1}\cup S^{fuse}_{t+1}$, let $n_t(z)$ be its invocation count and $ER_t(z)$ the fraction of invocations ending in execution or local-verifier failure. Define inactivity age $Age_t(z)=t-t_{last}(z)$ and tenure $Tenure_t(z)=t-t_{add}(z)$. With error threshold $\rho_{err}$, inactivity limit $T_{idle}$, and minimum support $n_{min}$, prune when

$$n_t(z)\ge n_{min}\land ER_t(z)>w_t(z)\rho_{err}\quad\lor\quad Age_t(z)>w_t(z)T_{idle},$$

where

$$w_t(z)=1+\lambda\frac{Tenure_t(z)}{1+Tenure_t(z)},$$

and $\lambda\ge0$ is chosen so that $(1+\lambda)\rho_{err}\le1$.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 对每个技能条目 $z$，$n_t(z)$ 表示调用次数，$ER_t(z)$ 表示以执行失败或局部验证失败结束的调用比例；$Age_t(z)$ 和 $Tenure_t(z)$ 分别表示不活跃年龄与留存时长。给定错误率阈值、非活跃上限和最小支持次数，若错误率超过经留存时间调整的阈值，或不活跃年龄超过调整后的上限，则剪除该条目。留存因子 $w_t(z)$ 随技能存续时间从 1 增长到 $1+\lambda$，而 $n_{min}$ 防止技能因少量噪声失败而过早被剪除。删除被标记的原子和技能后，系统修复或丢弃依赖已剪除原子的技能，得到 $Lib_{t+1}$。

## Equation and notation ledger / 方程与符号清单

> <span style="color:#3B82F6"><strong>Para. M.1:</strong></span> The following display equations preserve the source notation and equation order. They are collected here in addition to their explanatory paragraph context so that every mathematical definition remains searchable and independently auditable.

> <span style="color:#F59E0B"><strong>Para. M.1[CN]:</strong></span> 以下显示方程保留原文符号和编号顺序。除方法正文中的解释性段落外，这里集中列出全部数学定义，以便检索和独立核验。

$$
Lib=(A,S),\qquad S=S_{tool}\cup S_{geo}. \tag{1}
$$

$$
a=(e_a,v_a),\qquad e_a:U_a\rightarrow O_a,\qquad v_a:O_a\rightarrow\{0,1\}. \tag{2}
$$

$$
s=(V,E,\kappa),\qquad V\subseteq A,\qquad E\subseteq V\times V. \tag{3}
$$

$$
C_{t,k}=LLMRetrieve(I_t,q_t,M_{t,k};S_t). \tag{4}
$$

$$
u_{t,k}=LLMSelect(I_t,q_t,M_{t,k},C_{t,k}),\qquad u_{t,k}\in\{stop\}\cup(C_{t,k}\cap S_{tool,t})\cup A_{tool,t}. \tag{5}
$$

$$
(I_t,q_t,M_{t,k})\xrightarrow{\mathrm{Retrieve}}C_{t,k}\xrightarrow{\mathrm{Select}}u_{t,k}\xrightarrow{\mathrm{Exec}}(o_{t,k},\nu_{t,k})\xrightarrow{\mathrm{Update}}M_{t,k+1}. \tag{6}
$$

$$
\tau_t=\left(((M_{t,k},u_{t,k},o_{t,k},\nu_{t,k})_{k=1}^{K_t},\hat y_t)\right),\qquad B_{t+1}=B_t\cup\{\tau_t\}. \tag{7}
$$

$$
(\Delta A_t,\hat G_t^+,\hat G_t^-)=LLMAnalyze(B_{t+1}). \tag{8}
$$

$$
Lib_{t+1}^{fuse}=LLMFusion(Lib_t,\Delta A_t,\hat G_t^+,\hat G_t^-). \tag{9}
$$

$$
Prune_t(z)=\left[n_t(z)\ge n_{min}\land ER_t(z)>w_t(z)\rho_{err}\right]\lor\left[Age_t(z)>w_t(z)T_{idle}\right]. \tag{10}
$$

$$
w_t(z)=1+\lambda\frac{Tenure_t(z)}{1+Tenure_t(z)},\qquad \lambda\ge0,\qquad (1+\lambda)\rho_{err}\le1.
$$

# 4 Experiments / 实验

## 4.1 Experimental Setup / 实验设置

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We evaluate NeSy-Spatial on MMSI, MindCube, and OmniSpatial using GPT-5.4 and Gemini 2.5 Pro. MMSI uses Attribute, Motion, Positional Relation, and Multi-Step Reasoning (MSR); MindCube uses Rotation, Around, and Among; OmniSpatial uses Dynamic Reasoning and Perspective Taking.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们使用 GPT-5.4 和 Gemini 2.5 Pro，在 MMSI、MindCube 与 OmniSpatial 上评估 NeSy-Spatial。MMSI 包含 Attribute、Motion、Positional Relation 和 Multi-Step Reasoning（MSR）；MindCube 包含 Rotation、Around 和 Among；OmniSpatial 包含 Dynamic Reasoning 和 Perspective Taking。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> We compare with general inductive agents AWM and ASI, and with spatial agents SpaAge-PE, SpaAge-ReAct, GCA, and LAST. SpaAge methods let the LVLM plan tool calls directly; GCA first maps each problem into a unified geometric formalization; LAST uses predefined spatial skills. All methods use the same tool set and interface configuration.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 我们将方法与通用归纳智能体 AWM、ASI，以及空间智能体 SpaAge-PE、SpaAge-ReAct、GCA 和 LAST 比较。SpaAge 允许 LVLM 直接规划工具调用；GCA 先将问题映射到统一的几何形式化；LAST 使用预定义空间技能。所有方法使用相同的工具集和接口配置。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> We report prequential answer accuracy, where each prediction is evaluated before its label is used for skill evolution. Tool execution is measured by First-Pass Compositional Tool-Chain Success Rate (FTCS) and Python success rate. For samples invoking at least two distinct task tools, FTCS is the fraction of samples for which all task-tool calls succeed without a failed attempt. Python success rate is the fraction of successful `PythonTool.code` calls, counting retries separately.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 我们报告预quential 答案准确率：每个预测都在其标签用于技能演化之前进行评估。工具执行用首次通过组合工具链成功率（FTCS）和 Python 成功率衡量。对于至少调用两个不同任务工具的样本，FTCS 是所有任务工具调用均成功且没有失败尝试的样本比例；Python 成功率是成功的 `PythonTool.code` 调用比例，重试分别计数。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> We initialize $N_{seed}=3$ seed skills for MMSI and MindCube, and $N_{seed}=4$ for OmniSpatial. Evolution is triggered every $N_{buf}=20$ completed trajectories. We use $n_{min}=5$, $\rho_{err}=0.4$, $T_{idle}=100$, and $\lambda=0.5$, satisfying $(1+\lambda)\rho_{err}\le1$. The same hyperparameters are used across datasets and backbones.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> MMSI 和 MindCube 初始化 $N_{seed}=3$ 个种子技能，OmniSpatial 初始化 $N_{seed}=4$ 个。每完成 $N_{buf}=20$ 条轨迹后触发演化。剪枝设置为 $n_{min}=5$、$\rho_{err}=0.4$、$T_{idle}=100$、$\lambda=0.5$，满足 $(1+\lambda)\rho_{err}\le1$。所有数据集和骨干模型使用相同超参数。

## 4.2 Main Results / 主要结果

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> NeSy-Spatial improves spatial reasoning performance and achieves state-of-the-art results. In Table 1 it achieves the best Overall accuracy in five of six backbone–dataset settings. With GPT-5.4 it reaches 49.50 on MMSI and 71.50 on MindCube, outperforming the strongest baselines by 1.50 and 0.49 percentage points, while remaining competitive on OmniSpatial (60.27 versus 61.00). With Gemini 2.5 Pro it achieves the highest Overall accuracy on all three benchmarks, with margins of 0.50, 10.12, and 3.97 points.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> NeSy-Spatial 提升了空间推理性能并取得了当前最佳结果。如表 1 所示，在六个骨干模型—数据集设置中的五个设置上，它取得最高 Overall 准确率。使用 GPT-5.4 时，MMSI 和 MindCube 得分分别为 49.50 和 71.50，比最强基线高 1.50 和 0.49 个百分点；在 OmniSpatial 上也具有竞争力（60.27 对 61.00）。使用 Gemini 2.5 Pro 时，三个基准上均取得最高 Overall 准确率，优势分别为 0.50、10.12 和 3.97 个百分点。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> NeSy-Spatial also improves tool utilization. With GPT-5.4 it obtains average FTCS 94.56 and Python success rate 95.45, exceeding the strongest baseline averages by 7.17 and 6.67 points. With Gemini 2.5 Pro it obtains the best average FTCS and Python success rate, exceeding baselines by 0.21 and 7.76 points.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> NeSy-Spatial 也改善了工具利用。使用 GPT-5.4 时，平均 FTCS 和 Python 成功率分别为 94.56 和 95.45，比最强基线平均值高 7.17 和 6.67 个百分点。使用 Gemini 2.5 Pro 时，它同样取得最佳平均 FTCS 和 Python 成功率，分别超过基线 0.21 和 7.76 个百分点。

### Table 1. Average accuracy (%) / 表 1：平均准确率（%）

**Caption:** Average accuracy (%) over the online stream, broken down by dataset-specific subtasks and capability groups. The best and second-best results within each backbone block are highlighted in bold and underlined, respectively.

**Caption[CN]:** 在线流上的平均准确率（%），按数据集特定子任务和能力组拆分。每个骨干模型区块中的最佳和次佳结果分别以粗体和下划线标示。

| Backbone | Method | MMSI Attr. | Motion | Pos. Rel. | MSR | Overall | MindCube Rot. | Ard. | Amg. | Overall | OmniSpatial Dyn. | Persp. | Overall |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| GPT-5.4 | SpaAge-PE | 38.24 | 48.00 | 37.50 | 40.00 | 39.50 | 57.14 | 64.71 | 57.99 | 58.50 | 55.42 | 53.85 | 54.50 |
| GPT-5.4 | SpaAge-ReAct | 54.92 | 52.00 | 59.38 | 42.22 | 44.00 | 71.43 | 58.52 | 52.66 | 54.50 | 59.04 | 53.85 | 56.00 |
| GPT-5.4 | LAST | 37.64 | 51.00 | 42.37 | 48.79 | 44.09 | 48.92 | 60.23 | 68.24 | 66.21 | 60.24 | 55.63 | 57.54 |
| GPT-5.4 | GCA | 35.29 | 52.00 | 48.96 | 53.33 | 48.00 | 64.29 | 52.94 | 73.37 | 71.01 | 63.89 | 58.97 | 61.00 |
| GPT-5.4 | AWM | 31.25 | 54.24 | 45.64 | 40.00 | 43.01 | 53.85 | 38.46 | 57.93 | 56.14 | 65.43 | 52.88 | 58.38 |
| GPT-5.4 | ASI | 38.71 | 52.17 | 31.18 | 42.50 | 37.43 | 42.86 | 41.18 | 50.89 | 49.50 | 63.86 | 52.99 | 57.50 |
| GPT-5.4 | NeSy-Spatial | 41.18 | 56.00 | 52.08 | 46.67 | 49.50 | 64.29 | 58.82 | 73.37 | 71.50 | 66.27 | 55.56 | 60.27 |
| Gemini 2.5 Pro | SpaAge-PE | 41.21 | 47.96 | 52.13 | 57.82 | 51.00 | 71.52 | 58.91 | 69.79 | 69.08 | 51.82 | 59.81 | 56.37 |
| Gemini 2.5 Pro | SpaAge-ReAct | 44.11 | 48.00 | 57.29 | 51.13 | 52.50 | 64.19 | 58.83 | 74.50 | 72.38 | 59.02 | 55.53 | 57.08 |
| Gemini 2.5 Pro | LAST | 30.67 | 48.00 | 58.23 | 54.28 | 51.38 | 68.04 | 70.78 | 60.14 | 61.60 | 60.25 | 53.64 | 56.38 |
| Gemini 2.5 Pro | GCA | 32.35 | 52.00 | 60.42 | 48.89 | 52.00 | 85.67 | 76.47 | 62.13 | 65.03 | 61.45 | 61.54 | 61.53 |
| Gemini 2.5 Pro | AWM | 55.88 | 60.00 | 65.62 | 55.56 | 61.00 | 78.57 | 64.71 | 61.54 | 63.00 | 65.06 | 68.38 | 66.97 |
| Gemini 2.5 Pro | ASI | 50.00 | 68.00 | 64.58 | 51.11 | 59.70 | 85.71 | 70.58 | 59.76 | 62.50 | 63.86 | 64.10 | 64.01 |
| Gemini 2.5 Pro | NeSy-Spatial | 52.94 | 72.03 | 66.67 | 53.33 | 61.50 | 85.73 | 64.71 | 84.02 | 82.50 | 67.47 | 73.50 | 70.94 |

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The full Table 1 reports each subtask rather than only the aggregate values. Within the GPT-5.4 block, NeSy-Spatial is strongest on MMSI Motion and Positional Relation, MindCube Overall, and OmniSpatial Dynamic Reasoning, while GCA remains strongest on MMSI MSR and OmniSpatial Overall. Within the Gemini 2.5 Pro block, NeSy-Spatial is strongest on MMSI Motion and Positional Relation, MindCube Rotation, Among and Overall, and both OmniSpatial subtasks and Overall.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 表 1 的完整结果报告了各个子任务，而不仅是总体值。在 GPT-5.4 区块中，NeSy-Spatial 在 MMSI 的 Motion 与 Positional Relation、MindCube Overall 以及 OmniSpatial Dynamic Reasoning 上最强；GCA 在 MMSI MSR 与 OmniSpatial Overall 上仍最强。在 Gemini 2.5 Pro 区块中，NeSy-Spatial 在 MMSI Motion 与 Positional Relation、MindCube Rotation、Among 与 Overall，以及 OmniSpatial 的两个子任务和 Overall 上最强。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The library expands from 3 to 17 skills on MindCube, from 3 to 9 on MMSI, and from 4 to 20 on OmniSpatial. Growth is not monotonic: pruning removes unreliable or inactive skills, preventing unbounded accumulation and balancing incorporation of new reusable experience with retention of useful skills.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 技能库在 MindCube 上从 3 个扩展到 17 个，在 MMSI 上从 3 个扩展到 9 个，在 OmniSpatial 上从 4 个扩展到 20 个。增长并非单调：剪枝会移除不可靠或不活跃技能，防止技能无限累积，并在吸收新经验与保留有用技能之间形成动态平衡。

## 4.3 Further Analysis / 进一步分析

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Figure 6 compares cumulative prequential accuracy of NeSy-Spatial with Frozen, whose initial skill library remains fixed. After 10 samples, the curves are displayed from 5% stream progress. NeSy-Spatial establishes sustained gains over Frozen across all three benchmarks. By the end, it is 12.5, 3.5, and 2.5 points higher on MindCube, MMSI, and OmniSpatial, respectively; the macro average improves from 54.2% to 60.3%.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 图 6 比较了 NeSy-Spatial 与 Frozen 的累积预quential 准确率；Frozen 的初始技能库在整个流中保持固定。处理 10 个样本后，从流进度的 5% 开始显示曲线。NeSy-Spatial 在三个基准上都持续优于 Frozen。流结束时，MindCube、MMSI 和 OmniSpatial 分别高出 12.5、3.5 和 2.5 个百分点；宏平均从 54.2% 提升至 60.3%。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Ablation shows complementary roles. Disabling evolution reduces accuracy by 12.50, 3.50, and 2.78 points on MindCube, MMSI, and OmniSpatial. Removing Tool-Use Skills causes drops of 11.50, 6.00, and 2.68 points; removing Geometry Skills lowers accuracy by 2.00, 2.50, and 2.27 points. The full configuration is best on all three benchmarks.

### Table 2. Ablation study / 表 2：消融实验

**Caption:** Ablation study of skill evolution, Tool-Use Skills, and Geometry Skills using GPT-5.4. Accuracy is reported as percentages.

**Caption[CN]:** 使用 GPT-5.4 对技能演化、Tool-Use Skills 和 Geometry Skills 进行消融实验。准确率以百分比报告。

| Tool-Use Skill | Geometry Skill | Evolution | MindCube | MMSI | OmniSpatial |
|---|---|---|---:|---:|---:|
| ✓ | ✓ | — | 59.00 | 46.00 | 57.49 |
| — | ✓ | ✓ | 60.00 | 43.50 | 57.59 |
| ✓ | — | ✓ | 69.50 | 47.00 | 58.00 |
| ✓ | ✓ | ✓ | 71.50 | 49.50 | 60.27 |

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The ablation rows retain the same benchmark and backbone settings as the main experiment. The first row freezes evolution while retaining both skill types; the second and third rows remove Tool-Use Skills and Geometry Skills, respectively; the last row is the complete NeSy-Spatial configuration.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 消融各行与主实验使用相同的基准和骨干模型设置。第一行保留两类技能但冻结演化；第二、三行分别移除 Tool-Use Skills 和 Geometry Skills；最后一行是完整的 NeSy-Spatial 配置。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This paper presented NeSy-Spatial, a self-evolving neuro-symbolic framework for tool-augmented spatial reasoning. It organizes typed atomic instructions for tool interaction and geometric computation into interruptible Tool-Use Skills and reusable Geometry Skills. Across three benchmarks and two LVLM backbones, NeSy-Spatial achieves the best aggregate accuracy in five of six settings and the highest average FTCS and Python success rate. Online results show sustained accuracy gains with experience, while library-size changes indicate that pruning removes unreliable or inactive skills instead of allowing indiscriminate growth. Evaluation is limited to selected benchmarks and tool environments; future work will examine broader tasks and transfer to unseen settings.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本文提出了 NeSy-Spatial，一种用于工具增强空间推理的自演化神经符号框架。它将工具交互和几何计算的带类型原子指令组织成可中断的 Tool-Use Skills 与可复用的 Geometry Skills。在三个基准和两种 LVLM 骨干模型上，NeSy-Spatial 在六个设置中的五个取得最佳总体准确率，并取得最高平均 FTCS 和 Python 成功率。在线结果显示准确率随经验持续提升；技能库规模的变化表明，剪枝会移除不可靠或不活跃技能，而不是允许技能无差别增长。评估仍局限于选定的基准和工具环境；未来将研究更广泛任务以及向未见设置的迁移。

# Figures, algorithms, prompts, and supplementary material / 图、算法、提示词与补充材料

## Figure captions / 图注

### Figure 1. Limitations of tool-augmented spatial reasoning agents

**Caption:** Limitations of tool-augmented spatial reasoning agents: dynamic planning may violate tool dependencies, while fixed pipelines can be redundant and generalize poorly.

**Caption[CN]:** 工具增强空间推理智能体的局限：动态规划可能违反工具依赖关系，而固定流水线可能产生冗余且泛化能力较差。

### Figure 2. Overview of NeSy-Spatial

**Caption:** Left: the agent retrieves and executes skills for closed-loop spatial reasoning. Center top: the Skill Library organizes atomic instructions into reusable high-level skills. Center bottom: execution trajectories record the shared reasoning process. Right: trajectory analysis, skill fusion, and pruning enable continual self-evolution.

**Caption[CN]:** 左：智能体检索并执行技能，进行闭环空间推理。中上：技能库将原子指令组织成可复用高层技能。中下：执行轨迹记录共享的推理过程。右：轨迹分析、技能融合和剪枝实现持续自演化。

### Figure 3. Skill-guided spatial reasoning and evolution

**Caption:** Qualitative example of skill-guided spatial reasoning and skill evolution. Left: NeSy-Spatial composes visual and geometric tools to solve a perspective-taking question. Right: failure diagnosis identifies missing grounding dependencies, updates the Tool-Use Skill, and enables the revised pipeline to produce the correct answer on a subsequent sample.

**Caption[CN]:** 技能引导空间推理与技能演化的定性示例。左：NeSy-Spatial 组合视觉工具和几何工具解决视角变换问题。右：失败诊断识别缺失的 grounding 依赖，更新 Tool-Use Skill，使修订后的流水线在后续样本上产生正确答案。

### Figure 4. Tool-Use and Geometry Skills

**Caption:** Examples of Tool-Use and Geometry Skills. The Tool-Use example uses `VGGT.reconstruct` followed by `PythonTool.code`; the Geometry example computes a camera-frame direction with `RobustCenter`, `WorldToCamera`, `Normalize`, and `MatchOption`.

**Caption[CN]:** Tool-Use Skills 和 Geometry Skills 示例。Tool-Use 示例依次使用 `VGGT.reconstruct` 与 `PythonTool.code`；Geometry 示例使用 `RobustCenter`、`WorldToCamera`、`Normalize` 和 `MatchOption` 计算相机坐标系方向。

### Figure 5. Tool success and retained skills

**Caption:** Left: FTCS and Python success rate across spatial reasoning benchmarks; the best and second-best results within each block are highlighted in bold and underlined, respectively. Right: the evolution of the number of retained skills throughout the online stream.

**Caption[CN]:** 左：各空间推理基准上的 FTCS 与 Python 成功率；每个区块内最佳和次佳结果分别以粗体和下划线标示。右：在线流过程中保留技能数量的变化。

### Figure 6. Cumulative prequential accuracy

**Caption:** Cumulative prequential accuracy of NeSy-Spatial and Frozen throughout the online stream. Frozen keeps the initial skill library fixed without online evolution.

**Caption[CN]:** NeSy-Spatial 与 Frozen 在在线流过程中的累积预quential 准确率。Frozen 固定初始技能库，不进行在线演化。

### Figures 7–8. Case-study input images

**Caption:** Figure 7 shows the two input views for the MindCube camera-motion case; the task asks for camera motion from the first view to the second. Figure 8 shows the MMSI grounded-direction case; the painting is grounded in Image 1 and evaluated relative to the observer in Image 2.

**Caption[CN]:** 图 7 展示 MindCube 相机运动案例的两个输入视图，任务是判断从第一视图到第二视图的相机运动。图 8 展示 MMSI grounding 方向案例；画作在图像 1 中定位，并相对于图像 2 中的观察者进行评估。

## Supplementary A–D / 补充材料 A–D

> <span style="color:#3B82F6"><strong>Para. A.1:</strong></span> Section A reports implementation settings, native tools, and skill representations. The shared settings include MMSI seed skills 3, MindCube seed skills 3, OmniSpatial seed skills 4, warm-up trajectories 10, same-family trace batch 5, repeated-failure support 2, pending-trace fallback threshold 40, candidate fusion batch 2, maximum traces per induction prompt 20, prototype trace window 80, maximum selected skills per query 4, maximum mutable-library skills 24, zero-correct retirement support 2, minimum invocation support 5, minimum retained accuracy 0.4, and inactivity threshold 100.

> <span style="color:#F59E0B"><strong>Para. A.1[CN]:</strong></span> A 节报告实现设置、原生工具和技能表示。共享设置包括：MMSI 种子技能 3 个、MindCube 种子技能 3 个、OmniSpatial 种子技能 4 个、预热轨迹 10 条、同族轨迹批大小 5、重复失败支持 2、待处理轨迹回退阈值 40、候选融合批大小 2、每个 induction prompt 最多 20 条轨迹、原型轨迹窗口 80、每个查询最多选择 4 个技能、可变技能库最多 24 个技能、零正确率退休支持 2、最小调用支持 5、最小保留准确率 0.4，以及非活跃阈值 100。

### Table 3. Shared settings / 表 3：共享设置

**Caption:** Shared settings for initialization, online induction, selection, and empirical maintenance.

**Caption[CN]:** 初始化、在线归纳、选择和经验维护的共享设置。

| Setting | Value |
|---|---:|
| **Initialization** | |
| MMSI seed skills | 3 |
| MindCube seed skills | 3 |
| OmniSpatial seed skills | 4 |
| **Online induction and fusion** | |
| Warm-up trajectories | 10 |
| Same-family trace batch | 5 |
| Repeated-failure support | 2 |
| Pending-trace fallback threshold | 40 |
| Candidate fusion batch | 2 |
| Maximum traces per induction prompt | 20 |
| Prototype trace window | 80 |
| **Skill selection and capacity** | |
| Maximum selected skills per query | 4 |
| Maximum skills in mutable library | 24 |
| **Empirical maintenance** | |
| Zero-correct retirement support | 2 |
| Minimum invocation support | 5 |
| Minimum retained accuracy | 0.4 |
| Inactivity threshold | 100 |

### Table 4. Dataset-specific inference settings / 表 4：数据集特定推理设置

**Caption:** Dataset-specific inference settings.

**Caption[CN]:** 数据集特定的推理设置。

| Dataset | Maximum turns | Wave size |
|---|---:|---:|
| MMSI | 12 | 5 |
| MindCube | 8 | 5 |
| OmniSpatial | 8 | 5 |

> <span style="color:#3B82F6"><strong>Para. A.1b:</strong></span> Runtime and inference settings use the simple agent runtime, process queries in waves of five, and allow a larger reasoning budget for MMSI because its questions typically require longer multi-view geometric pipelines. GroundingDINO is fixed as the object-detection backend across LVLM backbones, preventing the reasoning model and visual grounding component from changing simultaneously.

> <span style="color:#F59E0B"><strong>Para. A.1b[CN]:</strong></span> 运行时与推理设置采用简单智能体运行时，以五个查询为一批处理查询；由于 MMSI 问题通常需要更长的多视角几何流水线，因此为其允许更大的推理预算。所有 LVLM 骨干模型均固定使用 GroundingDINO 作为目标检测后端，避免推理模型和视觉 grounding 组件同时发生变化。
> <span style="color:#3B82F6"><strong>Para. A.2:</strong></span> > <span style="color:#3B82F6"><strong>Para. A.2:</strong></span> The native tool library is fixed across benchmarks. It includes `SemanticDetector.detect`, `GeometricReconstructor.reconstruct`, `GeometricReconstructor.project_box_to_3d_points`, `ObjPoseEstimator.predict_obj_pose`, `MetricScaleEstimator.estimate_scale`, `EasyOCR.ocr`, `LanguageToCamera.visualize_camera_layout`, and `PythonTool.code`. GroundingDINO, VGGT, MoGe, and the object-pose backend are internal visual backends rather than planner-visible tool atoms.

> <span style="color:#F59E0B"><strong>Para. A.2[CN]:</strong></span> 原生工具库在所有基准上固定不变，包括上述八个工具原子。GroundingDINO、VGGT、MoGe 和 object-pose 后端作为内部视觉后端存在，而不是规划器可见的工具原子。

### Table 5. Native tool atoms / 表 5：原生工具原子

**Caption:** Native tool atoms available to the agent.

**Caption[CN]:** 智能体可用的原生工具原子。

| Tool atom | Function |
|---|---|
| `SemanticDetector.detect` | Localizes named objects or regions and returns learned 2D bounding boxes. |
| `GeometricReconstructor.reconstruct` | Recovers camera extrinsics, dense 3D points, confidence maps, and depth from one or more images. |
| `GeometricReconstructor.project_box_to_3d_points` | Lifts a selected 2D bounding box into a set of corresponding points in the reconstructed 3D scene. |
| `ObjPoseEstimator.predict_obj_pose` | Estimates an object-centric position and orientation from a selected object box. |
| `MetricScaleEstimator.estimate_scale` | Estimates conversion from reconstruction coordinates to metric units. |
| `EasyOCR.ocr` | Reads visible text that may provide identity, ordering, or metric cues. |
| `LanguageToCamera.visualize_camera_layout` | Converts caller-provided numeric view angles and labels into a symbolic camera-layout representation. |
| `PythonTool.code` | Generates and executes Python code over workspace variables for deterministic geometric computation. |

> <span style="color:#3B82F6"><strong>Para. A.2b:</strong></span> Tool outputs are stored as typed workspace variables and can be consumed by later steps. A detector output can be passed to 3D projection, projected points can be combined with camera extrinsics, and a Geometry Skill can use those variables to compute the final spatial decision. The visual foundations supporting these tools are treated as internal backends rather than planner-visible atoms.

> <span style="color:#F59E0B"><strong>Para. A.2b[CN]:</strong></span> 工具输出以带类型的工作区变量保存，可由后续步骤消费。检测器输出可以传给 3D 投影，投影点可以与相机外参组合，Geometry Skill 则可以利用这些变量计算最终空间决策。支撑这些工具的视觉基础模型被视为内部后端，而非规划器可见的原子。
> <span style="color:#3B82F6"><strong>Para. A.3:</strong></span> > <span style="color:#3B82F6"><strong>Para. A.3:</strong></span> A Tool-Use skill is a high-level pipeline whose docstring states when it should be retrieved, whose ordered steps specify tool atoms and semantic responsibilities, and whose `stopping_condition` states when sufficient evidence has been collected. A Geometry skill is a self-contained computational kernel stored as Python code lines, with usage constraints, helper routines, a high-level decision function, and empirical statistics such as `seen`, `matched`, `used`, `correct_after_use`, and `incorrect_after_use`.

> <span style="color:#F59E0B"><strong>Para. A.3[CN]:</strong></span> Tool-Use Skill 是高层流水线：其 docstring 说明何时检索，ordered steps 指定工具原子及其语义职责，`stopping_condition` 指定何时收集到足够证据。Geometry Skill 是以 Python 代码行存储的自包含计算内核，包含使用约束、辅助函数、高层决策函数，以及 `seen`、`matched`、`used`、`correct_after_use` 和 `incorrect_after_use` 等经验统计量。

### Table 6. Overview of the two reusable skill types / 表 6：两类可复用技能概览

**Caption:** Overview of the two reusable skill types.

**Caption[CN]:** 两类可复用技能类型概览。

| Aspect | Tool-Use skill | Geometry skill |
|---|---|---|
| Represents | Executable evidence-collection pipeline | Deterministic numerical decision kernel |
| Retrieved for | Tool ordering and semantic-role completion | Reference-frame computation and option selection |
| Stored as | Ordered atoms, bindings, and a stopping condition | Python helpers, usage constraints, and decision function |
| Produces | Structured workspace evidence | A serializable decision or diagnostic |

> <span style="color:#3B82F6"><strong>Para. A.3b:</strong></span> A Tool-Use skill is stored as a high-level pipeline. Its docstring specifies when it should be retrieved, its ordered tool atoms specify responsibilities, and its stopping condition says when enough evidence has been collected to return control to the planner. A Geometry skill is stored as executable code with applicability conditions and a reusable decision function.

> <span style="color:#F59E0B"><strong>Para. A.3b[CN]:</strong></span> Tool-Use skill 以高层流水线存储。其 docstring 指定何时检索，按顺序排列的工具原子指定各自职责，stopping condition 则说明何时收集到足够证据、可以将控制权交还规划器。Geometry skill 以带适用条件的可执行代码和可复用决策函数存储。> <span style="color:#3B82F6"><strong>Para. B:</strong></span> > <span style="color:#3B82F6"><strong>Para. B:</strong></span> Section B presents end-to-end inference cases. In the MindCube camera-motion case, the agent retrieves a reconstruction pipeline, calls `GeometricReconstructor.reconstruct`, retrieves `camera0_motion_option_from_extrinsics`, computes the second camera displacement in camera-0 coordinates, and returns option C, diagonally forward-left. In the MMSI grounded-object case, it reconstructs the scene, detects “the painting with a black frame and white background,” projects the selected box into 3D, and uses `camera_frame_object_quadrant_choice` to select the unique answer.

> <span style="color:#F59E0B"><strong>Para. B[CN]:</strong></span> B 节给出端到端推理案例。在 MindCube 相机运动案例中，智能体检索重建流水线，调用 `GeometricReconstructor.reconstruct`，检索 `camera0_motion_option_from_extrinsics`，在 camera-0 坐标中计算第二台相机的位移，并返回选项 C（斜向前方左侧）。在 MMSI grounding 物体案例中，它重建场景，检测“黑色边框和白色背景的画作”，将选定框投影到 3D，再使用 `camera_frame_object_quadrant_choice` 选择唯一答案。

> <span style="color:#3B82F6"><strong>Para. B.1:</strong></span> Case 1 asks: “Based on these two views in Figure 7 showing the same scene, in which direction did I move from the first view to the second view?” The options are (A) diagonally forward and right; (B) directly right; (C) diagonally forward and left; and (D) directly left. The retrieved Tool-Use skill reconstructs the shared scene and the Geometry skill compares the second camera pose in the first camera’s frame, producing C.

> <span style="color:#F59E0B"><strong>Para. B.1[CN]:</strong></span> 案例 1 的问题是：“图 7 的两个视图展示同一场景；从第一视图到第二视图，我朝哪个方向移动？”选项为：（A）斜向前右方；（B）正右方；（C）斜向前左方；（D）正左方。检索到的 Tool-Use skill 重建共享场景，Geometry skill 在第一台相机坐标系中比较第二台相机姿态，得到 C。

> <span style="color:#3B82F6"><strong>Para. B.2:</strong></span> Case 2 asks where the painting in Image 1 is with respect to the observer in Image 2, with options (A) right, (B) left, (C) front-left, and (D) directly left. The pipeline reconstructs both views, grounds the painting using `SemanticDetector.detect`, projects its selected box with `GeometricReconstructor.project_box_to_3d_points`, and resolves the camera-frame relation with a Geometry skill; the result is front-left, option C.

> <span style="color:#F59E0B"><strong>Para. B.2[CN]:</strong></span> 案例 2 询问图像 1 中画作相对于图像 2 中观察者的位置，选项为：（A）右；（B）左；（C）左前方；（D）正左方。流水线重建两个视图，使用 `SemanticDetector.detect` 定位画作，使用 `GeometricReconstructor.project_box_to_3d_points` 投影选定框，再用 Geometry skill 判断相机坐标系关系；结果为左前方，即选项 C。

> <span style="color:#3B82F6"><strong>Para. B.3:</strong></span> Case 3 is an allocentric OmniSpatial question: in Figure 9, where is the electric fan as seen from the projection screen’s viewpoint? The pipeline keeps the screen and fan as distinct semantic roles, reconstructs the scene, estimates the screen’s object pose, lifts both detections into 3D, and classifies the fan in the screen-centric frame as right, option A.

> <span style="color:#F59E0B"><strong>Para. B.3[CN]:</strong></span> 案例 3 是 OmniSpatial 的自中心问题：从投影屏幕的视点看，图 9 中的电风扇在哪里？流水线将屏幕和风扇保持为不同语义角色，重建场景，估计屏幕的物体姿态，将两次检测结果提升到 3D，并在以屏幕为中心的坐标系中将风扇分类为右侧，即选项 A。

> <span style="color:#3B82F6"><strong>Para. B.4:</strong></span> Case 4 shows Tool-Use evolution for a four-view turn-and-move family. The initial `four_view_turn_move_symbolic_layout_root` reconstructs the scene and resolves the post-turn view, but an unsuccessful trajectory stops without grounding the named destination or comparing forward distance. Analysis identifies those missing operations; fusion preserves the parent and adds a `four_view_turn_move_target_grounding_branch`. A later execution grounds the smoking machine, compares distance after the turn, repairs an initial Python syntax error, and returns “A. Yes.”

> <span style="color:#F59E0B"><strong>Para. B.4[CN]:</strong></span> 案例 4 展示四视图“转向与移动”任务族中的 Tool-Use 演化。初始的 `four_view_turn_move_symbolic_layout_root` 能够重建场景并解析转向后的视图，但一次失败轨迹在未定位命名目标、未比较前进距离时就停止。分析识别出这两个缺失操作；融合保留父技能，并加入 `four_view_turn_move_target_grounding_branch`。后续执行定位吸烟机，比较转向后的距离，修复首次 Python 语法错误，并返回“A. Yes.”。

> <span style="color:#3B82F6"><strong>Para. B.5:</strong></span> Case 5 shows Geometry-Skill evolution. Several trajectories implement the same camera-motion computation with slightly different programs. Induction factors them into `camera0_motion_option_from_extrinsics`, whose contract requires valid extrinsics, a first-camera reference frame, current option semantics, and diagnostic guards for malformed evidence. On later reuse, the kernel computes the displacement in the first camera frame and selects option C.

> <span style="color:#F59E0B"><strong>Para. B.5[CN]:</strong></span> 案例 5 展示 Geometry-Skill 演化。多条轨迹用略有不同的程序实现相同的相机运动计算；归纳过程将它们提炼为 `camera0_motion_option_from_extrinsics`，其契约要求有效外参、以第一台相机为参照系、当前选项语义，以及针对格式错误证据的诊断保护。在后续复用中，该内核在第一台相机坐标系中计算位移，并选择选项 C。

> <span style="color:#3B82F6"><strong>Para. C:</strong></span> Section C summarizes retained learned skills. The records preserve exact fields including `id`, `rule_type`, `level`, `docstring`, `steps`, `code_lines`, `usage`, `stopping_condition`, `status`, and `empirical_stats`; pruning and promotion statistics are retained for auditability.

> <span style="color:#F59E0B"><strong>Para. C[CN]:</strong></span> C 节总结保留的学习技能。记录保留 `id`、`rule_type`、`level`、`docstring`、`steps`、`code_lines`、`usage`、`stopping_condition`、`status` 和 `empirical_stats` 等精确字段；剪枝和晋升统计也被保留，以保证可审计性。

> <span style="color:#3B82F6"><strong>Para. D:</strong></span>> <span style="color:#3B82F6"><strong>Para. D:</strong></span> Section D provides complete prompt templates for inference and evolution. The prompts preserve exact JSON keys, placeholders, allowed outputs, tool names, stop conditions, retry restrictions, and output-only requirements.

> <span style="color:#F59E0B"><strong>Para. D[CN]:</strong></span> D 节提供推理和演化的完整提示词模板。提示词中的 JSON 键、占位符、允许输出、工具名、停止条件、重试限制和仅输出要求均保持精确不变。由于 PDF 文本抽取会交错双栏布局，原生提示词/代码块保存在配套抽取文件中。

### Figure 9. Allocentric relation case / 图 9：自中心关系案例

**Caption:** Original input image for the OmniSpatial allocentric case. The electric fan is localized relative to the projection screen’s object-centric viewpoint.

**Caption[CN]:** OmniSpatial 自中心案例的原始输入图像。电风扇相对于投影屏幕的物体中心视点进行定位。

### Figure 10. Four-view turn-and-move case / 图 10：四视图转向与移动案例

**Caption:** Original four-view input for the evolved Tool-Use skill.

**Caption[CN]:** 演化后 Tool-Use skill 所用的四视图原始输入。

### Table 7. Evolved skill inventory for MindCube / 表 7：MindCube 的演化技能清单

**Caption:** Evolved skill inventory for MindCube. Initial seed skills are excluded.

**Caption[CN]:** MindCube 的演化技能清单；初始种子技能不计入其中。

| Skill type | Skill name |
|---|---|
| Tool-Use | Four-View Behind-Me Camera Layout |
| Tool-Use | Explicit Turn-View Symbolic Layout |
| Tool-Use | Four-View Turn-and-Move Symbolic Layout |
| Tool-Use | Behind-Me Camera Layout with Behind-View Option Grounding |
| Tool-Use | Behind-Me Resolved-View Option Grounding |
| Tool-Use | Query-View Candidate Grounding with a Target-Pose Frame |
| Tool-Use | Four-View Turn-and-Move Target Grounding |
| Tool-Use | Query-View Candidate Grounding with a Query-View Target Pose |
| Tool-Use | Behind-Me Symbolic Layout followed by Option Grounding |
| Tool-Use | Turned-View Target Grounding |
| Tool-Use | Turned-View Target Grounding V2 |
| Geometry | Camera-0 Motion from Extrinsics |
| Geometry | Right-Turn Distance Change to a Target |
| Geometry | Left-Turn Proximity in the Camera Frame |

### Table 8. Evolved skill inventory for MMSI / 表 8：MMSI 的演化技能清单

**Caption:** Evolved skill inventory for MMSI. Initial seed skills are excluded.

**Caption[CN]:** MMSI 的演化技能清单；初始种子技能不计入其中。

| Skill type | Skill name |
|---|---|
| Tool-Use | Single-Anchor Grounding with Camera-Layout Binding |
| Tool-Use | Reconstruction and Camera-Layout Reasoning for Egomotion |
| Tool-Use | Dual-Landmark Grounding for Observer-Relative Comparison |
| Geometry | Object-Side Reasoning from Pose Bearing |
| Geometry | Camera-Frame Object-Quadrant Selection |
| Geometry | Absolute Camera-Position-Side Reasoning from a Reference View |

### Table 9. Evolved skill inventory for OmniSpatial / 表 9：OmniSpatial 的演化技能清单

**Caption:** Evolved skill inventory for OmniSpatial. Initial seed skills are excluded.

**Caption[CN]:** OmniSpatial 的演化技能清单；初始种子技能不计入其中。

| Skill type | Skill name |
|---|---|
| Tool-Use | Refined Entity Detection after Grounding Review |
| Tool-Use | Camera-Arrival Grounding Review |
| Tool-Use | Detection and Grounding Ambiguity Review |
| Tool-Use | Allocentric Pairwise Grounding-Readiness Review |
| Tool-Use | Egocentric Relation Failure Review |
| Tool-Use | Allocentric Egocentric-Relation Review |
| Tool-Use | Reference-Frame Relation Counting |
| Tool-Use | Grounding-Consistency Review |
| Tool-Use | Viewpoint-Conditioned Region Membership |
| Tool-Use | Allocentric Axial-Relation Review |
| Geometry | Camera-Relative Travel-Time Selection |
| Geometry | Allocentric Left–Right Reasoning from Reference Pose |

> <span style="color:#3B82F6"><strong>Para. C.1:</strong></span> The retained inventories are readable names for the skills that survived online evolution. They show that the library stores both tool-organizing procedures and geometry kernels, including camera layout, grounding review, reference-frame relations, object pose, camera motion, and allocentric reasoning.

> <span style="color:#F59E0B"><strong>Para. C.1[CN]:</strong></span> 保留清单给出了在线演化后幸存技能的可读名称，表明技能库同时保存工具组织过程和几何内核，覆盖相机布局、grounding 复核、参照系关系、物体姿态、相机运动与自中心推理。

# D Prompt Templates / D 提示词模板

> <span style="color:#3B82F6"><strong>Para. D.1:</strong></span> The Skill Retrieval Prompt selects a small set of reusable rules relevant to the current task and workspace context. At this stage the selector sees only compact rule descriptions.

> <span style="color:#F59E0B"><strong>Para. D.1[CN]:</strong></span> Skill Retrieval Prompt 用于选择与当前任务和工作区上下文相关的一小组可复用规则。在此阶段，选择器只能看到紧凑的规则描述。

```text
SKILL RETRIEVAL PROMPT
Purpose. Select a small set of reusable rules that are relevant to the current task and workspace context. The selector sees only compact rule descriptions at this stage.
Inputs.
• <TASK_INSTRUCTION>
• <CONTEXT_SUMMARY>
• <RULE_TYPE>
• <TARGET_ACTION_IF_APPLICABLE>
• <SELECTION_CONTEXT>
• <CANDIDATE_RULES_JSON>
• <MAX_RULES>
• optional <ERROR_FEEDBACK>
Instructions.
1. Select only rules whose docstring fits the current task and context.
2. Use structure_hint only to distinguish otherwise similar rules.
3. Do not select a rule merely because one word or one tool overlaps.
4. It is valid to select no rules if none are specific enough.
5. Return at most <MAX_RULES> rule ids.
Strict output format.
{
  "selected_rule_ids": [
    "rule_id_if_useful"
  ],
  "rationale": "brief reason for the selection, or why none apply"
}
If no rule is useful, return:
{
  "selected_rule_ids": [],
  "rationale": "no candidate rule is specific enough for this task"
}
```

> <span style="color:#3B82F6"><strong>Para. D.2:</strong></span> The Inference Planner Prompt instructs the planner to make exactly one top-level decision at each turn: use one complete Tool-Use skill, execute one immediate tool action, or return the final answer. A block rule is a semantically complete reusable procedure rather than an arbitrary fragment.

> <span style="color:#F59E0B"><strong>Para. D.2[CN]:</strong></span> Inference Planner Prompt 要求规划器在每一轮恰好作出一个顶层决定：使用一个完整的 Tool-Use skill、执行一个即时工具动作，或返回最终答案。block rule 是语义完整的可复用过程，而非任意片段。

```text
INFERENCE PLANNER PROMPT
Purpose. Act as the planner for a tool-using spatial reasoning agent. At each turn, choose exactly one top-level decision: use one complete Tool-Use skill, execute one immediate tool action, or return the final answer.
Inputs.
• <TASK_INSTRUCTION>
• <WORKSPACE_SUMMARY>
• <RECENT_OBSERVATIONS>
• <CANDIDATE_BLOCK_RULES>
• <AVAILABLE_TOOL_SCHEMAS>
• optional <ERROR_FEEDBACK>
Instructions.
1. Choose exactly one decision type:
   • decision_type="rule": select one reusable high-level rule by id;
   • decision_type="action": emit one immediate tool action or the final answer.
2. A block rule is a semantically complete reusable procedure, not an arbitrary tool-call fragment.
3. The executor does not decide final answers; return a final answer only when workspace evidence is sufficient.
4. Use missing_information to list unresolved semantic roles, such as the reference frame, reference entity, target, candidate set, requested relation, or option mapping.
5. One aggregate detection cannot fill multiple semantic roles.
6. Prefer one small tool action at a time unless multiple calls are clearly independent.
7. For spatial direction, distance, or orientation, prefer explicit geometry and deterministic computation.
8. For an object-centric viewpoint, use object-pose evidence to establish the reference orientation.
```

```json
Rule decision:
{
  "decision_type": "rule",
  "use_rule": true,
  "selected_rule_id": "exact_rule_id",
  "selected_rule_reason": "why this complete rule matches the current need",
  "missing_information": ["unresolved semantic role"],
  "tool_calls": [],
  "final_answer": null
}
Immediate action:
{
  "decision_type": "action",
  "use_rule": false,
  "selected_rule_id": null,
  "selected_rule_reason": "why an immediate action is needed",
  "missing_information": ["unresolved semantic role"],
  "tool_calls": [
    {
      "tool_name": "Tool.method",
      "output_variable": "workspace_name",
      "args": {}
    }
  ],
  "final_answer": null
}
Final answer:
{
  "decision_type": "action",
  "use_rule": false,
  "selected_rule_id": null,
  "selected_rule_reason": "the workspace already satisfies the task",
  "missing_information": [],
  "tool_calls": [],
  "final_answer": "answer derived from workspace evidence"
}
```

> <span style="color:#3B82F6"><strong>Para. D.3:</strong></span> The Tool-Use Skill Induction Prompt infers at most one reusable pipeline extension from a batch of compact traces. It distinguishes a branch from a new root, records only missing or replaced semantic operations, and rejects incomplete fragments, tool invention, and Geometry skills embedded inside Tool-Use pipelines.

> <span style="color:#F59E0B"><strong>Para. D.3[CN]:</strong></span> Tool-Use Skill Induction Prompt 从一批紧凑轨迹中至多归纳一个可复用流水线扩展。它区分 branch 与 new root，只记录缺失或替换的语义操作，并拒绝不完整片段、虚构工具以及嵌入 Tool-Use 流水线中的 Geometry skill。

```text
TOOL-USE SKILL INDUCTION PROMPT
Purpose. Infer one reusable pipeline extension from a batch of compact traces. The goal is to grow a narrower child pipeline from an existing reusable trunk whenever possible.
Inputs.
• <ATOM_CONTRACTS_JSON>
• <CURRENT_PIPELINE_KB_JSON>
• <TRACE_BATCH_JSON>
• optional <ERROR_FEEDBACK>
Instructions.
1. Group traces by task family and required computation.
2. A valid family must contain at least two traces with the same semantic roles, evidence needs, and decision pattern, including at least one correct trace.
3. Generate at most one candidate from one supported family.
4. Use operation="branch" when an existing parent pipeline supplies a reusable trunk.
5. Record only the missing or replaced semantic operation(s); fusion will materialize the complete child.
6. Use operation="new_root" only when no reusable parent exists.
7. Do not generate incomplete fragments such as reconstruction-only, retry-only, or isolated detection/projection steps.
8. Do not invent tools, and do not place Geometry skill ids inside a Tool-Use pipeline.
9. The stopping_condition must describe a semantically complete and observable workspace state.
```

```json
{
  "candidate_rules": [
    {
      "id": "short_snake_case_extension",
      "rule_type": "pipeline_delta",
      "operation": "branch",
      "parent_rule_id": "existing_pipeline_id",
      "docstring": "narrow task family and evidence need",
      "extension_steps": [
        {
          "atom": "Tool.method",
          "instruction": "missing semantic operation",
          "bindings": {
            "required_arg": "$semantic_workspace_slot",
            "output": "semantic_output_name"
          },
          "stopping_condition": "semantically complete child result"
        }
      ],
      "rationale": "supporting trace family and recurring gap"
    }
  ]
}
If no supported reusable program exists:
{
  "candidate_rules": [],
  "rationale": "no supported reusable program exists"
}
```

> <span style="color:#3B82F6"><strong>Para. D.4:</strong></span> The Geometry Skill Induction Prompt groups code traces by the same computation and requires at least two traces, including one correct execution. It generalizes a complete decision computation, preserves required variables and reference-frame assumptions, and returns a diagnostic rather than a fabricated answer when evidence is missing or malformed.

> <span style="color:#F59E0B"><strong>Para. D.4[CN]:</strong></span> Geometry Skill Induction Prompt 按相同计算对代码轨迹分组，并要求至少两条轨迹且其中一条执行正确。它概括完整决策计算，保留所需变量和参照系假设；证据缺失或格式错误时返回诊断，而不是编造答案。

```text
GEOMETRY SKILL INDUCTION PROMPT
Purpose. Induce a reusable geometry kernel for PythonTool.code from execution records. The induced rule should capture a complete recurring computation, together with its applicability conditions and failure guards.
Inputs.
• <CURRENT_CODE_CONTROL_KB_JSON>
• <PYTHON_TRACE_BATCH_JSON>
• optional <ERROR_FEEDBACK>
Instructions.
1. Group records by the same computation, required variables, reference frame, and output decision.
2. A valid family must contain at least two traces, including at least one correct execution.
3. Prefer families where correct and incorrect traces expose a concrete reusable difference.
4. Generalize the complete decision computation rather than a trivial helper or a shared code substring.
5. usage must specify required variables, shapes, reference-frame assumptions, and per-call bindings.
6. code_lines must define one self-contained reusable kernel, possibly with helper functions and one decision function.
7. Missing or malformed evidence must return a diagnostic rather than a fabricated answer.
8. Do not encode sample ids, one-off object names, option letters, or sample-specific answers.
```

```json
{
  "candidate_rules": [
    {
      "id": "short_snake_case_kernel",
      "rule_type": "code_control",
      "level": "high_level",
      "docstring": "narrow coding scenario and evidence conditions",
      "usage": [
        "required inputs, frames, modes, and bindings",
        "conditions under which the kernel must be used"
      ],
      "code_lines": [
        "def reusable_decision(required_values, mode):",
        "    # complete reusable computation",
        "    return result"
      ],
      "rationale": "why the traces share one reusable computation"
    }
  ]
}
If unsupported, return:
{
  "candidate_rules": [],
  "rationale": "no supported reusable computation exists"
}
```

> <span style="color:#3B82F6"><strong>Para. D.5:</strong></span> The Skill Fusion Prompt fuses candidates into the mutable main library. Parent pipelines are read-only references; a branch is materialized as a complete child, unsupported or overly broad records are discarded, and trace-supported fusion supplies a proof entry for every changed pipeline.

> <span style="color:#F59E0B"><strong>Para. D.5[CN]:</strong></span> Skill Fusion Prompt 将候选项融合进可变主库。父流水线是只读引用；branch 会被实例化为完整子流水线；不受支持或过于宽泛的记录会被丢弃；启用轨迹支持的融合时，每个发生新增或实质变化的流水线都要提供 proof 条目。

```text
SKILL FUSION PROMPT
Purpose. Fuse the mutable main library and the candidate library into a bounded active library. For Tool-Use skills, fusion materializes complete child pipelines; for Geometry skills, it merges reusable kernels.
Inputs.
• <MAX_RULES>
• <READ_ONLY_PARENT_RULES_JSON>
• <MUTABLE_MAIN_KB_JSON>
• <CANDIDATE_KB_JSON>
• <TRACE_PROOF_RESERVOIR_JSON>
• optional <ERROR_FEEDBACK>
Instructions.
1. Preserve the schema of Tool-Use pipelines and Geometry kernels.
2. Parent pipelines are read-only references and must not be rewritten.
3. For pipeline_delta candidates with operation="branch", preserve the reusable parent trunk and materialize the extension where it semantically belongs.
4. Never emit pipeline_delta directly into the active library; always materialize a complete child.
5. Merge duplicate children and discard unsupported, overly broad, or sample-specific records.
6. Discard children that still fail to reach the evidence state claimed by their docstring.
7. Tool-Use pipelines may reference only native tool atoms and planner reasoning tools.
8. When trace-supported fusion is enabled, provide one pipeline_proofs entry for every new or materially changed pipeline.
```

> <span style="color:#3B82F6"><strong>Para. D.6:</strong></span> The Geometry-Guided Code Generation Prompt generates the executable Python wrapper after a reusable Geometry skill is selected. It binds current workspace values, does not redefine the selected helper block, adapts only the wrapper, option mapping, indices, thresholds, and return format, and requires a serializable result.

> <span style="color:#F59E0B"><strong>Para. D.6[CN]:</strong></span> Geometry-Guided Code Generation Prompt 在选定可复用 Geometry skill 后生成可执行 Python 封装器。它绑定当前工作区值，不重新定义已选辅助代码块，只调整封装器、选项映射、索引、阈值和返回格式，并要求结果可序列化。

```text
GEOMETRY-GUIDED CODE GENERATION PROMPT
Purpose. Generate the executable wrapper for PythonTool.code. The code generator receives the current variables, their schemas, the reference-frame requirements, and optionally a retrieved Geometry skill.
Inputs.
• <USER_REQUEST>
• <REFERENCE_FRAME_DESCRIPTION>
• <COMPUTATIONAL_OBJECTIVE>
• <CONTEXT_DESCRIPTION>
• <VARIABLE_SCHEMAS_AND_DOCUMENTATION>
• <SELECTED_CODE_CONTROL_DOCSTRING>
• <SELECTED_CODE_CONTROL_USAGE>
• <SELECTED_REUSABLE_KERNEL>
• optional <PREVIOUS_EXECUTION_ERROR>
Instructions.
1. Write one Python function that implements the requested computation.
2. Use only a reusable kernel whose input contract matches the current variables and objective.
3. Bind kernel inputs to current workspace values.
4. Do not redefine the selected helper block.
5. Adapt only the wrapper, option mapping, indices, thresholds, and return format.
6. Verify the computation using the supplied variable documentation.
7. For multiple-choice questions, evaluate the current options rather than relying on fixed option letters.
8. Missing or incomparable evidence should result in a diagnostic rather than a fabricated answer.
9. The returned result must be serializable.
```

```python
When a reusable Geometry kernel is selected:
{
  "use_code_blocks": ["exact_geometry_skill.kernel"],
  "execute_code": "def execute(current_variables):\\n    result = reusable_decision(...)\\n    return result"
}
Otherwise, return exactly one Python code block defining:
def execute(current_variables):
    import ...
    ...
    return serializable_value
```

# References / 参考文献

The reference section is retained in searchable original bibliographic form in the source PDF and represented above by author/year/title inventory where the two-column page is not safely recoverable as a lossless text stream. No local image assets are embedded because the permitted output boundary excludes binary extraction; all figure/table captions and all substantive table values are preserved above. The only material caveat is that the PDF’s visual illustrations are described rather than copied as image files.

参考文献以可检索的英文书目信息保留；对于双栏页面无法安全恢复为无损文本流的部分，上文至少保留作者、年份和题名清单。由于允许的输出边界不包含二进制抽取，未嵌入本地图像；所有图注/表注及实质性表格数值均已在上文保留。唯一的实质性说明是：PDF 中的视觉插图采用文字描述，而没有复制为图像文件。

# Source coverage and limitations / 来源覆盖与限制

This reader is a complete bilingual text-and-structure rendering of the supplied 25-page PDF, with the source’s main sections, equations, tables 1–9, figures 1–10 captions, supplementary sections A–D, case-study descriptions, skill inventories, prompt templates, exact JSON keys/placeholders, and technical identifiers represented in source order. Visual image binaries are intentionally not copied; therefore captions and searchable content are retained without local image links. The page and section index at the beginning records the inspected 25-page span and the translation notes record this asset limitation.

本阅读稿是所提供 25 页 PDF 的完整双语文本与结构呈现，按源顺序保留正文各节、方程、表 1–9、图 1–10 图注、补充材料 A–D、案例描述、技能清单、提示词模板、精确 JSON 键/占位符和技术标识符。视觉图像二进制文件有意未复制，因此保留图注和可检索内容但不创建本地图片链接。开头的页码与章节索引记录了已检查的 25 页范围，翻译说明记录了这一资源限制。
