# Code2Worlds: Empowering Coding LLMs for 4D World Generation

**Authors:** Yi Zhang, Yunshuang Wang, Zeyu Zhang, Hao Tang  
**Source:** `Zhang 等 - 2026 - Code2Worlds Empowering Coding LLMs for 4D World Generation.pdf`  
**Detected source format:** selectable-text PDF (`pdf-text`)  
**Reader type:** full-paper Chinese-English Markdown reader with figure/table assets.

## Page / Section Index

| Section | Pages | Notes |
|---|---:|---|
| Abstract | pp.1-2 | bilingual body and related figures |
| 1 Introduction | p.2 | bilingual body |
| 2 Related Work | pp.2-3 | bilingual body |
| 3 The Proposed Method | pp.3-6 | bilingual body, equations, pipeline figures |
| 4 Experiments | pp.6-8 | bilingual body, comparison and ablation tables |
| 5 Conclusion / Impact Statements | pp.8-9 | bilingual body |
| References | pp.9-11 | bibliography preserved in the source PDF; not translated line-by-line |
| Appendix A-G | pp.11-28 | limitations, ablations, implementation, benchmark, library design, qualitative results, prompt design |

## Terminology Ledger

| Canonical term | Chinese rendering | Decision |
|---|---|---|
| Code2Worlds | Code2Worlds | 方法名，保持英文。 |
| 4D world generation | 4D 世界生成 | 指带时间维度的 3D 场景/物理仿真生成。 |
| language-to-simulation | language-to-simulation / 语言到仿真 | 本文核心任务表述；首次双写，后续可译为“语言到仿真”。 |
| coding LLM | 代码大语言模型 / coding LLM | 强调用 LLM 生成可执行程序。 |
| dual-stream architecture | 双流架构 | Object Stream 与 Scene Stream 的并行解耦。 |
| Object Stream | Object Stream / 对象流 | 负责目标动态对象的参数化生成。 |
| Scene Stream | Scene Stream / 场景流 | 负责全局环境规划与参数落地。 |
| Retrieval-Augmented Parametric Generation | 检索增强参数化生成 | 从参数库和代码库检索先验后再生成。 |
| Procedural Parameters Library | Procedural Parameters Library / 程序化参数库 | 记为 $L_{param}$。 |
| Reference Code Library | Reference Code Library / 参考代码库 | 记为 $L_{code}$。 |
| PostProcess Agent | PostProcess Agent / 后处理 Agent | 负责集成对象与场景，并写入动态物理效果。 |
| VLM-Critic | VLM-Critic | 对静态对象渲染图做语义反馈。 |
| VLM-Motion Critic | VLM-Motion Critic | 对视频 rollout 做动态/物理反馈。 |
| physical hallucination | 物理幻觉 | 代码语法可执行但运动违反物理规律。 |
| SGS | SGS | GPT-4o 评估的细粒度对象属性分数。 |
| HRS | HRS | GPT-4o 评估的视觉-物理合理性分数。 |
| Richness | Richness / 场景丰富度 | 评估场景对象种类、数量、细节和复杂度。 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Code2Worlds studies 4D world generation from language by moving beyond visually plausible frames toward executable world simulators grounded in physical laws. The authors argue that prior code-to-scene methods have progressed on static 3D generation, but they still face two obstacles when extended to dynamic 4D worlds: multi-scale context entanglement between local object detail and global scene layout, and a semantic-physical execution gap where open-loop code can produce physically invalid motion.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Code2Worlds 研究如何从语言生成 4D 世界，其目标不是只生成视觉上“像”的画面，而是生成受物理规律约束、可执行的世界仿真器。作者认为，已有 code-to-scene 方法已经推动了静态 3D 生成，但在扩展到动态 4D 世界时仍遇到两个障碍：其一是局部对象细节与全局场景布局之间的多尺度上下文纠缠；其二是语义-物理执行鸿沟，即开环代码虽然能运行，却可能产生违反物理规律的运动。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The paper introduces Code2Worlds as a language-to-simulation code generation framework. It first disentangles object generation and environmental orchestration with a dual-stream architecture. It then adds a physics-aware closed loop in which a PostProcess Agent scripts dynamics, while a VLM-Motion Critic inspects rendered rollouts and provides self-reflective feedback for code refinement.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 论文提出 Code2Worlds，将 4D 生成表述为 language-to-simulation 代码生成问题。方法首先用双流架构解耦对象生成与环境编排；随后加入物理感知闭环：PostProcess Agent 编写动态脚本，VLM-Motion Critic 检查渲染后的视频 rollout，并通过自反思反馈推动代码迭代修正。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> On the Code4D benchmark, Code2Worlds is reported to outperform prior baselines with a 41% gain in SGS and 49% higher Richness. A central claim is that the method uniquely combines editable procedural 3D worlds with instruction-grounded physics-aware dynamics, whereas prior code-centric methods are mostly static and diffusion-based video models often lack stable physical structure.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在 Code4D 基准上，Code2Worlds 相比已有基线取得了 41% 的 SGS 提升和 49% 的 Richness 提升。论文的核心主张是：该方法把可编辑的程序化 3D 世界与受指令约束的物理感知动态结合起来；相比之下，已有 code-centric 方法大多停留在静态场景，而视频扩散模型往往缺乏稳定的物理结构。

### Figure 1. Code2Worlds overview

![Figure 1](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_001_fig_figure_1.png)

**Caption:** Figure 1. Overview of Code2Worlds. The top part illustrates decomposition of intrinsic attributes such as lighting, color, and gray level. The bottom part shows a summer forest time-lapse with coherent atmospheric evolution from sunrise to noon and sunset.

**Caption[CN]:** 图 1：Code2Worlds 概览。上方展示对光照、颜色、灰度等内在属性的分解；下方展示夏季森林延时序列，体现从日出到正午再到日落的连贯大气演化。

## 1 Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper positions world generation as a step toward spatial intelligence. Generative models have moved from images to high-fidelity videos, but the authors emphasize that spatial intelligence requires simulators governed by causal physical laws, not only surface-level pixel dynamics. Procedural code is attractive in this setting because executable programs expose explicit control over 3D geometry, scene semantics, and later physical manipulation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文把世界生成定位为空间智能的一步。生成模型已经从图像发展到高保真视频，但作者强调，真正的空间智能需要受因果物理规律约束的仿真器，而不只是表层像素动态。程序化代码在这里很有吸引力，因为可执行程序能显式控制 3D 几何、场景语义以及后续物理操作。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The first challenge is multi-scale context entanglement. A world-generation prompt simultaneously asks for fine local structures and coherent global layouts. For example, a realistic tree needs detailed bark, leaf, and branch geometry, while the whole forest also needs terrain, lighting, vegetation density, and atmosphere. A monolithic generation pass can easily favor global coherence while leaving target objects too coarse for later physical actuation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 第一个挑战是多尺度上下文纠缠。一个世界生成 prompt 往往同时要求细粒度局部结构与连贯的全局布局。例如，一棵真实的树需要树皮、树叶和枝干几何细节，而整个森林还需要地形、光照、植被密度和大气效果。单次整体生成很容易偏向全局一致性，却让关键对象过于粗糙，难以支持后续物理驱动。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The second challenge is the execution gap between static 3D content and dynamic simulation. A prompt such as “leaves trembling” must be translated into concrete simulation parameters including vertex weights, wind forces, turbulence fields, collision handling, and temporal constraints. Without visual feedback, the coding LLM acts like a blind engineer: it can produce syntactically valid scripts that hallucinate physics, such as distorted rigid bodies or particles that ignore gravity.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 第二个挑战是静态 3D 内容与动态仿真之间的执行鸿沟。像 “leaves trembling” 这样的提示必须被翻译成具体仿真参数，包括顶点权重、风力、湍流场、碰撞处理和时间约束。如果没有视觉反馈，coding LLM 就像一个“盲人工程师”：它能写出语法正确的脚本，却可能产生物理幻觉，例如刚体被扭曲，或者粒子无视重力。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Code2Worlds addresses these issues with two linked design choices. The dual-stream architecture separates the focal object from the environmental background so object-level structural detail can be generated with retrieval-augmented parametric priors. A closed-loop refinement mechanism then renders the result, lets a VLM critic judge object appearance or motion, and feeds natural-language feedback back into the code-generation loop.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> Code2Worlds 用两个相互关联的设计应对这些问题。双流架构把焦点对象与环境背景分开，使对象级结构细节可以借助检索增强的参数化先验来生成。随后，闭环细化机制渲染结果，让 VLM critic 判断对象外观或运动，并把自然语言反馈重新送回代码生成循环。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The paper claims three contributions: a factorized language-to-simulation architecture, a physics-aware closed-loop correction mechanism, and the Code4D benchmark for evaluating 4D scene generation across object quality, scene richness, temporal stability, and physical plausibility.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 论文声称的贡献有三点：第一，提出分解式 language-to-simulation 架构；第二，引入物理感知的闭环纠错机制；第三，构建 Code4D 基准，用于从对象质量、场景丰富度、时间稳定性和物理合理性等角度评估 4D 场景生成。

## 2 Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In 3D and 4D content generation, the paper traces a path from early procedural generation and layout optimization to learning-based text-to-3D systems such as DreamFusion and Magic3D. It notes that 4D generation adds new difficulty because dynamic scenes must remain temporally coherent and physically consistent. Dynamic NeRF and Gaussian-based methods improve efficiency or visual quality, but full-scale 4D scene generation remains challenging.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在 3D 与 4D 内容生成方面，论文回顾了从早期程序化生成、布局优化到 DreamFusion、Magic3D 等学习式 text-to-3D 系统的发展路径。作者指出，4D 生成进一步增加了难度，因为动态场景必须保持时间一致性和物理一致性。Dynamic NeRF 与 Gaussian-based 方法提升了效率或视觉质量，但大规模 4D 场景生成仍然困难。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In LLM-driven procedural modeling, code-to-scene systems use LLMs to generate executable scripts for 3D software. Prior systems such as 3D-GPT, Infinigen, SceneCraft, RPG, LL3M, and VULCAN contribute planning, self-improvement, decomposition, or retrieval. However, the paper argues that this line of work remains predominantly optimized for static 3D scenes rather than dynamic physical environments.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在 LLM 驱动的程序化建模中，code-to-scene 系统利用 LLM 为 3D 软件生成可执行脚本。3D-GPT、Infinigen、SceneCraft、RPG、LL3M、VULCAN 等工作分别提供了规划、自我改进、任务分解或检索增强能力。然而，论文认为这一方向主要仍针对静态 3D 场景优化，而不是动态物理环境。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> In multi-agent coordination and reflection, prior work shows that multiple specialized agents can decompose complex tasks more robustly than a monolithic model. Closed-loop feedback can reduce error propagation. Code2Worlds adapts this idea to 4D generation by using parallel object and scene generation plus dual visual reflection: object-level reflection for appearance and motion-level reflection for temporal physics.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在多 agent 协作与反思方面，已有工作表明，多个专门化 agent 比单一模型更擅长分解复杂任务；闭环反馈也能减少错误传播。Code2Worlds 将这一思路迁移到 4D 生成：一方面并行进行对象生成与场景生成，另一方面使用双重视觉反思，即对象级反思负责外观，运动级反思负责时间物理。

## 3 The Proposed Method

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Code2Worlds takes a natural-language instruction as input and produces a dynamic 4D scene. The pipeline has four stages: user instruction parsing, Object Stream, Scene Stream, and final integration with physical post-processing. The Object Stream creates high-fidelity target objects; the Scene Stream creates a coherent environment; the PostProcess Agent combines both and scripts dynamics under feedback from VLM-based critics.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Code2Worlds 以自然语言指令为输入，输出动态 4D 场景。整个流程包含四个阶段：用户指令解析、Object Stream、Scene Stream，以及带物理后处理的最终集成。Object Stream 生成高保真目标对象；Scene Stream 生成连贯环境；PostProcess Agent 将二者合并，并在 VLM-based critic 的反馈下编写动态脚本。

### Figure 2. Code2Worlds execution pipeline

![Figure 2](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_003_fig_figure_2.png)

**Caption:** Figure 2. Code2Worlds generates 4D scenes with a dual-stream architecture: retrieval-augmented object generation with object self-reflection, hierarchical environmental orchestration, and a PostProcess Agent with self-reflection for final dynamics.

**Caption[CN]:** 图 2：Code2Worlds 通过双流架构生成 4D 场景：对象流使用检索增强对象生成与对象自反思，场景流使用分层环境编排，最终由带自反思的 PostProcess Agent 生成动态效果。

### 3.1 Overview

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The overview is intentionally modular. Instead of asking one LLM to write a complete dynamic Blender scene at once, the framework splits the problem into object fidelity, environmental consistency, and dynamic physical behavior. This separation is the paper’s main defense against the multi-scale conflict between local geometry and global scene design.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 方法概览刻意采用模块化设计。框架不是让一个 LLM 一次性写完整的动态 Blender 场景，而是把问题拆成对象保真度、环境一致性和动态物理行为三个部分。这种分离是论文用来对抗局部几何与全局场景设计之间多尺度冲突的核心手段。

### 3.2 Object Stream: Parametric Object Generation

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The Object Stream avoids raw 3D generation from scratch. It uses Retrieval-Augmented Parametric Generation built on procedural priors from Infinigen. The stream maps semantic instructions into parameter spaces, then generates executable procedural code so the target object has detailed 3D shape, texture, and material attributes.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Object Stream 避免从零直接生成原始 3D 结构，而是使用基于 Infinigen 程序化先验的检索增强参数化生成。该流把语义指令映射到参数空间，再生成可执行程序化代码，使目标对象具备细致的 3D 形状、纹理和材质属性。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The ObjSelect Agent first identifies which entity in the instruction requires dynamic interaction. For example, in a prompt about drifting leaves, the target object is the leaf. Global environmental changes such as lighting shifts are not handled here; they are deferred to the later dynamic post-processing stage.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> ObjSelect Agent 首先识别指令中哪个实体需要动态交互。例如，在描述飘落树叶的 prompt 中，目标对象是 leaf。光照变化等全局环境变化不在这里处理，而是推迟到后续动态后处理阶段。

$$
e_{target} = \arg\max_{e \in E(I)} P_{dyn}(e \mid I)
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> After selecting the target object, the system queries a Procedural Parameters Library $L_{param}$ to retrieve a structured parameter schema $S_{ref}$. This schema organizes parameters into structural shape, surface texture, and material semantics. The authors augment the schema with semantic exemplars that pair natural-language descriptions with parameter configurations, allowing the LLM to infer quantitative values through in-context analogy.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 选定目标对象后，系统查询 Procedural Parameters Library $L_{param}$，检索结构化参数 schema $S_{ref}$。该 schema 将参数组织为结构形状、表面纹理和材质语义三类。作者还用语义样例增强 schema，把自然语言描述与参数配置配对，使 LLM 能通过上下文类比推断定量参数值。

$$
S_{ref} \leftarrow Retrieve(L_{param}, e_{target}), \quad
S \leftarrow ObjParam(S_{ref}, I, F_{obj})
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The ObjGenerate Agent then retrieves a verified reference implementation $C_{ref}$ from the Reference Code Library $L_{code}$ and combines it with the predicted parameters $S$. This retrieval step matters because Infinigen factories often require parameters to be passed through specific constructors or factory fields, not arbitrary assignments.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 接着，ObjGenerate Agent 从 Reference Code Library $L_{code}$ 中检索经过验证的参考实现 $C_{ref}$，并将其与预测参数 $S$ 结合。这个检索步骤很关键，因为 Infinigen 的 factory 往往要求参数通过特定构造器或 factory 字段传入，而不是任意变量赋值。

$$
C_{ref} \leftarrow Retrieve(L_{code}, e_{target}), \quad
C_{obj} \leftarrow ObjGenerate(C_{ref}, S)
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Object Self-Reflection closes the object loop. The system renders a 2D snapshot of the generated object and asks a VLM-Critic to compare it with the original instruction. If the object is valid, it moves to scene integration. If not, the critic returns natural-language feedback $F_{obj}$, which is sent back to the parameter-generation agent for another iteration.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> Object Self-Reflection 闭合了对象生成循环。系统渲染生成对象的 2D 快照，并让 VLM-Critic 将其与原始指令比较。如果对象满足要求，就进入场景集成；否则 critic 返回自然语言反馈 $F_{obj}$，再把反馈送回参数生成 agent 进行下一轮迭代。

### 3.3 Scene Stream: Hierarchical Environmental Orchestration

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The Scene Stream orchestrates the global environment through a hierarchical manifest. It separates planning from execution so that sparse user intent can first be expanded into a rich scene specification and only later translated into concrete procedural parameters.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Scene Stream 通过分层 manifest 编排全局环境。它把规划与执行分开：先把稀疏用户意图扩展为丰富的场景规格，再把这些规格转成具体程序化参数。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In semantic decomposition, the Environment Planner infers latent context that the user did not explicitly state. A request for a “spooky forest” may imply autumn, heavy fog, dim lighting, dense understory, and a particular terrain mood. The planner outputs a manifest $M$ describing atmosphere, terrain morphology, vegetation density, and related ecosystem elements.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在语义分解阶段，Environment Planner 推断用户未显式说明的潜在上下文。例如，“spooky forest” 可能意味着秋季、浓雾、昏暗光照、密集林下植被和特定地形氛围。Planner 输出 manifest $M$，描述大气、地形形态、植被密度和相关生态元素。

$$
M \leftarrow Planner(I)
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> In parameter concretization, the Parameter Resolver turns qualitative descriptors into numeric and logical settings. It converts phrases such as “dense forest” into concrete density values and also enforces logical consistency: for example, a rainforest should suppress snow-layer parameters, while coupled parameters such as air density and dust density should be calibrated together.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在参数具体化阶段，Parameter Resolver 将定性描述转成数值和逻辑设置。它把 “dense forest” 这样的短语转换为具体密度值，同时强制逻辑一致性：例如 rainforest 应该关闭 snow-layer 参数；air density 与 dust density 等耦合参数也需要一起校准。

$$
D \leftarrow Resolver(M)
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> In 3D scene realization, the Scene Realization module acts as a domain-specific compiler. It maps high-level scene flags and parameter dictionaries into valid Infinigen-compatible execution code, then invokes Infinigen to instantiate the procedural 3D environment.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在 3D 场景落地阶段，Scene Realization 模块相当于一个领域专用编译器。它将高级场景标志和参数字典映射为兼容 Infinigen 的有效执行代码，再调用 Infinigen 实例化程序化 3D 环境。

$$
C_{env} \leftarrow Realizer(D)
$$

### Figure 3. Detailed workflow

![Figure 3](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_005_fig_figure_3.png)

**Caption:** Figure 3. Detailed workflow for 4D scene generation, including environmental scene generation, object generation, parameter retrieval, code generation, VLM feedback, and post-processing.

**Caption[CN]:** 图 3：4D 场景生成的详细流程，涵盖环境场景生成、对象生成、参数检索、代码生成、VLM 反馈和后处理。

### 3.4 Physics-Aware 4D Scene Generation

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The terminal stage integrates the generated object and global scene, then adds dynamics through the PostProcess Agent. The agent translates kinetic cues in the language instruction into simulation constraints. For example, “peacefully” can become a weak wind coefficient, while tree motion can require gradient masks that keep roots anchored while allowing branches to sway.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 最终阶段把生成对象与全局场景整合起来，再通过 PostProcess Agent 添加动态。该 agent 将语言指令中的运动线索翻译为仿真约束。例如，“peacefully” 可以变成较弱的风力系数；树木运动则可能需要梯度 mask，使树根固定而树枝可以摆动。

$$
P_{phys} \leftarrow INFERPHYSICS(I, F_{dyn}), \quad
W_{dyn} \leftarrow ACTUATE(W_{static}, P_{phys})
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Dynamic Effects Self-Reflection extends visual feedback from static objects to videos. The system renders a video rollout $V_{video}$, and VLM-Motion evaluates whether the temporal effects match the instruction. If a gentle breeze produces violent thrashing, the VLM identifies a magnitude error and the system recalibrates physics hyperparameters.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> Dynamic Effects Self-Reflection 将视觉反馈从静态对象扩展到视频。系统渲染视频 rollout $V_{video}$，由 VLM-Motion 判断时间动态是否符合指令。如果“微风”却产生剧烈摇晃，VLM 会识别为幅度错误，系统据此重新校准物理超参数。

$$
F_{dyn}, valid \leftarrow VLM\text{-}MOTION(V_{video}, I)
$$

### Table 1. Capability comparison under Code4D criteria

![Table 1](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_006_fig_table_1.png)

**Caption:** Table 1 compares methods by text control, static layout, object details, dynamics, temporal consistency, and self-reflection.

**Caption[CN]:** 表 1 从文本控制、静态布局、对象细节、动态、时间一致性和自反思六个维度比较方法。Code2Worlds 是表中唯一同时覆盖这些维度的方法。

## 4 Experiments

### 4.1 Benchmark and Metrics

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Code4D evaluates generation across object, scene, and dynamic dimensions. The paper compares Code2Worlds with code-centric 3D methods and text-to-video generation models. Qualitative demonstrations are placed in the appendix, while the main paper focuses on quantitative object quality, scene quality, temporal stability, and physics failure rate.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Code4D 从对象、场景和动态三个维度评估生成能力。论文将 Code2Worlds 与 code-centric 3D 方法和 text-to-video 生成模型比较。定性展示放在 appendix 中，主文重点报告对象质量、场景质量、时间稳定性和物理失败率等定量结果。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The evaluation protocol has four parts. CLIP-based scores measure semantic and stylistic alignment for objects and scenes. VBench measures temporal coherence and video stability with Motion Smoothness, Subject Consistency, Background Consistency, and Temporal Flickering. GPT-4o evaluates perceptual fidelity with SGS, HRS, and Richness. Manual inspection reports physics Failure Rate, including interpenetration, gravity mistakes, and collision errors.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 评估协议包含四部分。基于 CLIP 的分数衡量对象与场景的语义/风格对齐。VBench 用 Motion Smoothness、Subject Consistency、Background Consistency 和 Temporal Flickering 衡量时间一致性与视频稳定性。GPT-4o 用 SGS、HRS 和 Richness 评估感知保真度。人工检查则报告物理 Failure Rate，包括穿模、重力错误和碰撞处理错误。

### Table 2. Main quantitative results

![Table 2](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_007_fig_table_2.png)

**Caption:** Table 2 compares Code2Worlds with code-centric static generation methods and video diffusion models. Code2Worlds obtains O-CLIP 0.2655, SGS 61.4, Style-CLIP 0.6734, S-CLIP 0.2432, Failure Rate 10%, HRS 55.4, and Richness 62.3 in the reported table.

**Caption[CN]:** 表 2 将 Code2Worlds 与 code-centric 静态生成方法、视频扩散模型比较。报告数值中，Code2Worlds 获得 O-CLIP 0.2655、SGS 61.4、Style-CLIP 0.6734、S-CLIP 0.2432、Failure Rate 10%、HRS 55.4 和 Richness 62.3。

### 4.2 Main Results

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The capability analysis emphasizes that existing methods each cover only part of the desired 4D-generation capability. Infinigen provides strong procedural detail but lacks natural-language control and reflection. Text-driven code-to-scene systems such as MeshCoder, 3D-GPT, and SceneCraft are mostly static. ImmerseGen attempts dynamics but lacks temporal consistency. Code2Worlds is presented as bridging these gaps through text control, high-fidelity layouts, physics-aware dynamics, and self-reflection.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 能力分析强调，现有方法各自只覆盖 4D 生成能力的一部分。Infinigen 有较强程序化细节，但缺乏自然语言控制和反思机制。MeshCoder、3D-GPT、SceneCraft 等 text-driven code-to-scene 系统主要是静态的。ImmerseGen 尝试建模动态，但时间一致性不足。Code2Worlds 则被描述为通过文本控制、高保真布局、物理感知动态和自反思弥合这些缺口。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For object generation, Code2Worlds is compared with procedural, reconstruction-based, and agent-centric baselines. MeshCoder has weak robustness when augmented for point-cloud-to-script conversion. ImmerseGen improves over some baselines but still lacks structural detail. Code2Worlds reaches SGS 61.4, which the authors interpret as evidence that retrieval, parameters, and iterative reflection jointly ground language in high-fidelity 3D structure.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在对象生成方面，Code2Worlds 与程序化、重建式和 agent-centric 基线比较。MeshCoder 在被增强为 point-cloud-to-script 转换时鲁棒性较弱。ImmerseGen 相比部分基线有所提升，但结构细节仍不足。Code2Worlds 达到 SGS 61.4，作者将其解释为检索、参数化和迭代反思共同把语言 grounding 到高保真 3D 结构上的证据。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> For scene generation, Code2Worlds obtains the highest reported Richness score of 62.3 and an S-CLIP score of 0.2432. The paper argues that the Scene Stream does not merely place sparse assets; it populates environments with dense ecological and atmospheric detail. The dynamic advantage is also important: code-centric methods are static, while Code2Worlds reports HRS 55.4 and a physics Failure Rate of 10%.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在场景生成方面，Code2Worlds 获得表中最高 Richness 62.3，以及 S-CLIP 0.2432。论文认为 Scene Stream 不只是稀疏摆放 asset，而是能用密集生态元素和大气细节填充环境。动态优势也很关键：code-centric 方法是静态的，而 Code2Worlds 报告 HRS 55.4 和 10% 的物理 Failure Rate。

### Figure 4. Environmental effects

![Figure 4](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_007_fig_figure_4.png)

**Caption:** Figure 4 shows environmental effects including relighting, water spill, leaf fall, jellyfish movement, and fire.

**Caption[CN]:** 图 4 展示不同场景中的环境效果，包括重光照、水流溢出、落叶、水母运动和火焰。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> For video generation, the authors compare against Stable Video Diffusion, AnimateDiff, CogVideoX, and Hunyuan. Code2Worlds reports high Motion Smoothness and low physics Failure Rate. The paper attributes this to deterministic 3D rendering and explicit executable simulation, whereas diffusion-based video models can preserve local appearance but still suffer from texture boiling, inconsistent 3D structure, or implausible motion.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在视频生成方面，作者与 Stable Video Diffusion、AnimateDiff、CogVideoX 和 Hunyuan 比较。Code2Worlds 报告较高 Motion Smoothness 和较低物理 Failure Rate。论文将这一点归因于确定性 3D 渲染和显式可执行仿真；相比之下，视频扩散模型可以保持局部外观，却仍可能出现纹理沸腾、3D 结构不一致或运动不合理。

### Algorithm 1. Unified 4D Scene Generation Framework

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Algorithm 1 summarizes the framework as three loops. In Phase 1, the Object Stream selects the target entity, retrieves parameter and code references, generates object parameters and code, renders an image, and repeats until the VLM-Critic validates the object. In Phase 2, the Scene Stream plans a manifest, resolves parameters, and realizes the 3D scene. In Phase 3, the system unifies object and environment, infers physics, actuates the static world, renders video, and repeats until VLM-Motion validates the dynamics.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> Algorithm 1 将框架概括为三个循环。第一阶段 Object Stream 选择目标实体，检索参数和代码参考，生成对象参数与代码，渲染图像，并反复迭代直到 VLM-Critic 验证对象。第二阶段 Scene Stream 规划 manifest，解析参数并实现 3D 场景。第三阶段系统合并对象和环境，推断物理参数，驱动静态世界，渲染视频，并反复迭代直到 VLM-Motion 验证动态。

### 4.3 Ablation Study

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The object ablation in Table 3 shows that retrieval is central. Removing retrieval drops SGS to 23.5, while removing the structured parameter library also reduces fidelity. The interpretation is that LLMs need both canonical script references and a well-defined controllable parameter space to reliably map language to procedural geometry.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 表 3 的对象消融显示，检索是核心组件。去掉 retrieval 后 SGS 降到 23.5；去掉结构化参数库也会降低保真度。作者的解释是，LLM 需要规范脚本参考和定义良好的可控参数空间，才能稳定地把语言映射到程序化几何。

![Table 3](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_008_fig_table_3.png)

**Caption:** Table 3. Ablation on object generation components.

**Caption[CN]:** 表 3：对象生成组件消融。去掉 retrieval 的性能下降最大。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The reflection ablation in Table 4 separates object-level and motion-level feedback. Removing VLM-Critic reduces static object quality. Removing VLM-Motion causes physics Failure Rate to rise from 10% to 60% and reduces HRS. This supports the paper’s claim that temporal feedback is not a cosmetic add-on but a necessary mechanism for correcting simulation artifacts.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 表 4 的反思消融区分了对象级反馈和运动级反馈。去掉 VLM-Critic 会降低静态对象质量。去掉 VLM-Motion 会使物理 Failure Rate 从 10% 升至 60%，并降低 HRS。这支持论文的主张：时间反馈不是装饰性附加模块，而是修正仿真伪影的必要机制。

![Table 4](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_008_fig_table_4.png)

**Caption:** Table 4. Ablation on self-reflection mechanisms.

**Caption[CN]:** 表 4：自反思机制消融。VLM-Motion 对物理失败率影响最大。

## 5 Conclusion and Impact Statements

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The conclusion presents Code2Worlds as a bridge between static code generation and 4D physical simulation. The dual-stream architecture improves structural fidelity by separating object and scene generation, while VLM-driven closed-loop refinement improves dynamic consistency. On Code4D, the method is reported to generate more diverse and physics-aware environments than the baselines.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 结论将 Code2Worlds 定位为连接静态代码生成与 4D 物理仿真的桥梁。双流架构通过分离对象与场景生成来提升结构保真度，VLM 驱动的闭环细化则提升动态一致性。在 Code4D 上，该方法相比基线生成了更多样、也更具物理感知能力的环境。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The impact statement emphasizes safer sim-to-real transfer for embodied AI because physically consistent 4D simulations can support training and evaluation. The authors also acknowledge computational overhead from rigorous physics engines and iterative VLM feedback, as well as potential biases introduced by large language models.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 影响声明强调，该工作有助于具身 AI 中更安全的 sim-to-real 迁移，因为物理一致的 4D 仿真可以支持训练与评估。作者也承认，严格物理引擎和迭代 VLM 反馈会带来计算开销，而大语言模型本身也可能引入偏差。

## Appendix A. Limitation and Future Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The appendix states that Code2Worlds faces a fidelity-latency trade-off. The method relies on rigorous physics engines and iterative VLM feedback, which creates a computational bottleneck and prevents real-time generation. The proposed future direction is neural physics distillation, using learned approximations to accelerate simulation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 附录指出 Code2Worlds 面临保真度与延迟之间的权衡。该方法依赖严格物理引擎和迭代 VLM 反馈，形成计算瓶颈，因此难以实时生成。作者提出的未来方向是 neural physics distillation，即用学习式近似来加速仿真。

## Appendix B. Ablation Study

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The additional scene-composition ablation compares removing the Planner and Solver with removing the whole Scene Stream. Without Planner and Solver, S-CLIP falls to 0.2251; without the Scene Stream, Richness collapses to 26.4. The result supports the claim that hierarchical planning and global environmental orchestration are necessary for dense, coherent scenes.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 额外的场景组合消融比较了去掉 Planner & Solver 与去掉整个 Scene Stream 的影响。没有 Planner 和 Solver 时，S-CLIP 降到 0.2251；没有 Scene Stream 时，Richness 崩到 26.4。该结果支持论文主张：分层规划和全局环境编排对于生成密集、连贯场景是必要的。

![Table 5](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_011_fig_table_5.png)

**Caption:** Table 5. Ablation on scene composition components.

**Caption[CN]:** 表 5：场景组合组件消融。去掉 Scene Stream 对 Richness 的伤害最大。

## Appendix C. Implementation Details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The implementation uses Gemini 3 as the core reasoning engine across the VLM-Critic, VLM-Motion Critic, ObjSelect, ObjParam, ObjGenerate, Environmental Planner, Parameter Solver, Scene Realization, and PostProcess Agent. All 3D assets and 4D simulations are executed in Blender 4.3 through the `bpy` Python API.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 实现部分使用 Gemini 3 作为整个框架的核心推理引擎，覆盖 VLM-Critic、VLM-Motion Critic、ObjSelect、ObjParam、ObjGenerate、Environmental Planner、Parameter Solver、Scene Realization 和 PostProcess Agent。所有 3D asset 与 4D 仿真都通过 Blender 4.3 的 `bpy` Python API 执行。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Rendering uses the Cycles path-tracing engine. Nature scenes are rendered at 1920 × 1080 with 240 frames and 128 samples per frame; indoor scenes are rendered at the same resolution with 120 frames and 196 samples per frame. OpenImageDenoise is used for noise reduction.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 渲染使用 Cycles 路径追踪引擎。自然场景以 1920 × 1080 分辨率渲染 240 帧，每帧 128 samples；室内场景同样为 1920 × 1080，但渲染 120 帧，每帧 196 samples。输出使用 OpenImageDenoise 降噪。

## Appendix D. Benchmark Details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Code4D is designed for physically grounded 4D environments rather than static text-to-3D. The benchmark covers temporal evolution, physical interaction, and atmospheric change. It includes both natural and indoor scenes, semantically dense instructions, long-context reasoning requirements, and physical phenomena such as fluids, particles, rigid bodies, soft bodies, cloth, and lighting or atmosphere evolution.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Code4D 面向受物理约束的 4D 环境，而不是静态 text-to-3D。该基准覆盖时间演化、物理交互和大气变化，包含自然场景与室内场景、语义密集指令、长上下文推理要求，以及流体、粒子、刚体、软体、布料、光照/大气演化等物理现象。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The paper promises to release the full Code4D benchmark, including prompt texts and evaluation scripts, upon acceptance. This is framed as a transparency measure so future text-to-simulation systems can be compared against consistent baselines.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 论文承诺在接收后发布完整 Code4D 基准，包括 prompt 文本和评估脚本。这被表述为一种透明性措施，使未来 text-to-simulation 系统能够在一致基线上比较。

### Table 6. Example prompts in Code4D

![Table 6 crop](page_012_fig_table_6.png)

| Prompt content | Scene type | Primary dynamics |
|---|---|---|
| A breeze stirs through the autumn forest, gently swaying the entire tree as leaves dance in the wind. | Nature | Soft Body / Wind |
| A 10-second time-lapse of a summer forest day with sunrise, midday sun, sunset, moonlit night, and light mist. | Nature | Lighting / Atmosphere |
| Several narrow, curved, slightly withered yellow leaves detach, fall, spin, and rest on a pile of fallen leaves. | Nature | Rigid Body / Gravity |
| A thick-walled ceramic cup lies tipped on a coffee table and spills water across and over the tabletop. | Indoor | Fluid Dynamics |
| A lush green forest in heavy rain with diagonal rain streaks and wind-swaying branches. | Nature | Particle (Rain) / Wind |
| A translucent bioluminescent jellyfish drifts underwater while its bell pulsates. | Nature | Soft Body / Deformation |
| A brown glass bottle rolls slowly across a sunlit living-room floor. | Indoor | Rigid Body (Rolling) |
| Steam rises from a ceramic coffee cup in a warm bedroom. | Indoor | Particle (Steam) |
| A burning weathered tree stump emits flames, embers, ash, and dynamic shadows. | Nature | Particle (Fire/Smoke) |
| Sand flows like liquid silk down the leeward side of a desert dune. | Nature | Particle (Sand/Granular) |

**Caption[CN]:** 表 6：Code4D 中的代表性 prompt。该表覆盖风、光照/大气、重力、流体、雨粒子、软体变形、刚体滚动、蒸汽、火/烟和沙粒等动态类型。PDF 中该表跨页/版面较复杂，正文这里用 Markdown 表格转写以保证完整可读。

## Appendix E. Library Design

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The library design appendix explains that $L_{param}$ maps linguistic categories to procedural parameter values by analyzing high-quality scripts from Infinigen. It supports semantic-to-parameter grounding for assets such as leaves, jellyfish, cups, and bowls. In parallel, $L_{code}$ stores reusable code snippets that can instantiate procedural objects once the parameters are chosen.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Library Design 附录说明，$L_{param}$ 通过分析 Infinigen 中的高质量脚本，把语言类别映射到程序化参数值。它支持叶子、水母、杯子、碗等 asset 的语义到参数 grounding。同时，$L_{code}$ 保存可复用代码片段，在参数确定后用于实例化程序化对象。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Example parameter entries expose low-level controllable fields. For leaves, the library includes contour control points, midrib length, vein angle, vein density, serration depth, wave control points, HSV blade color, vein contrast, and blight weights. For jellyfish, it includes bell geometry, transparency materials, tentacle length, deformation, twist, and animation frequencies.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 参数库样例暴露了底层可控字段。对于叶片，库中包含轮廓控制点、主脉长度、叶脉角度、叶脉密度、锯齿深度、波形控制点、HSV 叶片颜色、叶脉对比度和枯斑权重。对于水母，库中包含伞盖几何、透明材质、触手长度、变形、扭转和动画频率等。

![Figure 7](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_016_fig_figure_7.png)

**Caption:** Figure 7. Example cup and bowl parameters.

**Caption[CN]:** 图 7：杯子与碗的参数样例。它展示了如何把语义描述落到形状、尺度、厚度和把手等具体控制项。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The code-library examples show the other half of the retrieval design. Rather than asking the LLM to invent the entire Blender/Infinigen script, the system retrieves canonical code for a given factory and asks the LLM to fill or adapt the relevant parameters. This reduces syntactic errors and keeps the generated code aligned with Infinigen’s API conventions.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 代码库样例展示了检索设计的另一半。系统不是让 LLM 凭空发明完整 Blender/Infinigen 脚本，而是为给定 factory 检索规范代码，再让 LLM 填充或调整相关参数。这样可以减少语法错误，并让生成代码符合 Infinigen API 约定。

![Figure 8](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_017_fig_figure_8.png)

**Caption:** Figure 8. Example leaf code.

**Caption[CN]:** 图 8：叶片生成代码样例，展示了如何设置 LeafFactory 的 genome 参数、颜色参数和枯斑控制。

![Figure 9](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_018_fig_figure_9.png)

**Caption:** Figure 9. Example jellyfish code.

**Caption[CN]:** 图 9：水母生成代码样例，展示了如何设置 JellyfishFactory 的材质、伞盖、触手和动画相关参数。

![Figure 10](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_019_fig_figure_10.png)

**Caption:** Figure 10. Example cup and bowl code.

**Caption[CN]:** 图 10：杯子与碗的生成代码样例，展示 tableware factory 的尺度、厚度、轮廓和内表面等配置。

## Appendix F. Additional Qualitative Results

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The qualitative appendix shows selected frames from ten dynamic simulations. The purpose is to demonstrate progression over time, including object deformation, collision handling, environmental changes, and scene-level physical interactions. These examples correspond closely to the representative prompts in Table 6.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 定性附录展示了十个动态仿真的关键帧。其目的是展示随时间推进的变化，包括对象变形、碰撞处理、环境变化和场景级物理交互。这些样例与表 6 中的代表性 prompt 基本对应。

![Figure 11](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_020_fig_figure_11.png)

**Caption:** Figure 11. Key frames of the wind scene.

**Caption[CN]:** 图 11：风场景关键帧，展示秋季森林中树木和树叶随风摆动。

![Figure 12](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_020_fig_figure_12.png)

**Caption:** Figure 12. Key frames of the relighting scene.

**Caption[CN]:** 图 12：重光照场景关键帧，展示夏季森林从日出、正午、日落到月夜薄雾的时间变化。

![Figure 13](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_021_fig_figure_13.png)

**Caption:** Figure 13. Key frames of the falling leaves scene.

**Caption[CN]:** 图 13：落叶场景关键帧，展示叶片脱落、旋转下降并落到地面的过程。

![Figure 14](3d%20agent/Code2Worlds%20Empowering%20Coding%20LLMs%20for%204D%20World%20Generation/assets/page_021_fig_figure_14.png)

**Caption:** Figure 14. Key frames of the rainy forest scene.

**Caption[CN]:** 图 14：雨林场景关键帧，展示斜向雨线与风雨中轻微摆动的树枝树叶。

![Figure 15](page_022_fig_figure_15.png)

**Caption:** Figure 15. Key frames of the desert scene.

**Caption[CN]:** 图 15：沙漠场景关键帧，展示沙粒沿沙丘背风侧流动的效果。

![Figure 16](page_022_fig_figure_16.png)

**Caption:** Figure 16. Key frames of the moving jellyfish scene.

**Caption[CN]:** 图 16：水母运动场景关键帧，展示半透明发光水母在水中漂移和伞盖周期性收缩扩张。

![Figure 17](page_023_fig_figure_17.png)

**Caption:** Figure 17. Key frames of the burning tree scene.

**Caption[CN]:** 图 17：燃烧树桩场景关键帧，展示火焰、余烬、灰烬和动态阴影。

![Figure 18](page_023_fig_figure_18.png)

**Caption:** Figure 18. Key frames of the spilling water scene.

**Caption[CN]:** 图 18：水杯倾倒场景关键帧，展示杯中水流到桌面并向边缘流动、滴落。

![Figure 19](page_024_fig_figure_19.png)

**Caption:** Figure 19. Key frames of the rolling bottle scene.

**Caption[CN]:** 图 19：玻璃瓶滚动场景关键帧，展示瓶子在阳光照射的客厅地板上缓慢滚动。

![Figure 20](page_024_fig_figure_20.png)

**Caption:** Figure 20. Key frames of the coffee cup scene.

**Caption[CN]:** 图 20：咖啡杯蒸汽场景关键帧，展示暖光卧室里咖啡杯上升的柔和蒸汽。

## Appendix G. System Prompt Design

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The prompt-design appendix lists structured prompts used for generation, critique, and refinement. The Environment Planner prompt asks the LLM to infer latent variables from sparse instructions, enforce geomorphological consistency, populate ecosystems with understory details, and map weather or particle words to supported simulation elements.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Prompt Design 附录列出了用于生成、批评和细化的结构化 prompt。Environment Planner prompt 要求 LLM 从稀疏指令中推断潜在变量，强制地貌一致性，用林下植被等细节填充生态系统，并把天气或粒子词映射到支持的仿真元素。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The ObjSelect prompt asks the model to identify the single most critical dynamic object, returning a strict JSON object with `key_obj` and `reason`. It prioritizes actively moving, deforming, or physically affected objects, avoids static background elements, and normalizes the object name to a singular common noun.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> ObjSelect prompt 要求模型识别唯一最关键的动态对象，并用严格 JSON 返回 `key_obj` 和 `reason`。它优先选择主动运动、变形或受到物理作用的对象，避免选择静态背景元素，并把对象名称规范为单数普通名词。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The VFX Supervisor / Physics Simulation Evaluator prompt rates generated video quality from 0 to 100 along physics plausibility, visual aesthetics, and temporal stability. Low scores correspond to severe physics violations or unusable image quality; high scores require accurate nuanced physics and high-fidelity rendering.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> VFX Supervisor / Physics Simulation Evaluator prompt 从物理合理性、视觉美学和时间稳定性三个维度给生成视频打 0 到 100 分。低分对应严重物理违规或不可用画质；高分要求细腻准确的物理效果和高保真渲染。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The object-quality evaluation prompt rates how well a rendered 3D object matches the fine-grained attributes in the text prompt, while the Scene Richness prompt asks the model to ignore text alignment and focus only on visual richness, object variety, object count, detail level, and scene complexity.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 对象质量评估 prompt 评价渲染 3D 对象与文本中细粒度属性的匹配程度；Scene Richness prompt 则要求模型忽略文本对齐，只关注视觉丰富度、对象种类、对象数量、细节水平和场景复杂度。

![Figure 23](page_027_fig_figure_23.png)

**Caption:** Figure 23. Example physics/video quality evaluation prompt.

**Caption[CN]:** 图 23：物理/视频质量评估 prompt 样例，要求按物理合理性、视觉质量和时间稳定性输出 JSON 评分。

## References

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The reference list is preserved in the source PDF. This reader does not translate each bibliographic entry line-by-line because the entries are citation metadata rather than argumentative prose.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 参考文献列表保留在源 PDF 中。本阅读版不逐条翻译参考文献条目，因为这些条目属于引文元数据，而非论文论证正文。

## Critical Reading Notes

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The strongest idea in Code2Worlds is not simply “LLM writes Blender code.” It is the factorization of code generation into object-specific procedural priors, scene-level environmental planning, and motion-level visual feedback. This factorization turns a brittle one-shot coding problem into a staged control problem.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Code2Worlds 最强的点并不是简单的“LLM 写 Blender 代码”，而是把代码生成分解为对象级程序化先验、场景级环境规划和运动级视觉反馈。这个分解把脆弱的一次性代码生成问题变成了分阶段控制问题。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The main evidence risk is evaluation scale. Code4D contains representative prompts and diverse dynamics, but the paper’s reported benchmark examples are still small compared with the diversity of real physical environments. GPT-4o-based metrics are useful for perceptual scoring, yet they also make the evaluation partly dependent on another foundation model’s judgments.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 主要证据风险在于评估规模。Code4D 包含代表性 prompt 和多样动态，但论文展示的基准样例相对于真实物理环境的多样性仍然较小。基于 GPT-4o 的指标有助于感知评分，但也让评估部分依赖另一个基础模型的判断。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The most useful follow-up question for this line of work is whether the closed-loop mechanism can move from visual plausibility correction to quantitative physical calibration. Current VLM feedback can detect that “the leaves drift too fast,” but it may not yet estimate physically correct mass, drag, stiffness, or fluid parameters in a principled way.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 这个方向最值得追问的是：闭环机制能否从视觉合理性修正走向定量物理校准。当前 VLM 反馈可以发现“叶子飘得太快”，但未必能以严格方式估计真实合理的质量、阻力、刚度或流体参数。
