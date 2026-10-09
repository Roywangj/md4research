# Overall

| 论文                              | 方向               | 核心关键词                                         | 主链接                                                                                                                                                                                                                                                     |
| ------------------------------- | ---------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A4-Agent                        | 零样本可供性推理         | Dreamer / Thinker / Spotter；想象辅助；精确可操作区域      | [精读](<3d agent/A4-Agent An Agentic Framework for Zero-Shot Affordance Reasoning/paper_DeepPaperNote.md>) / [翻译](<3d agent/A4-Agent An Agentic Framework for Zero-Shot Affordance Reasoning/paper.md>)                                                                     |
| Code2Worlds                     | 物理感知 4D 世界生成     | 对象/场景双流；仿真代码；VLM 运动批评；闭环物理修正                  | [精读](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>) / [翻译](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper.md>)                                                                                  |
| CompassAD                       | 3D 可供性 grounding | 意图驱动；竞争物体；CompassNet；ICI / BCR                | [笔记](<CompassAD - Intent-Driven 3D Affordance Grounding in Functionally Competing Objects.md>)                                                                                                                                                          |
| DeepScan                        | 视觉落地推理           | 免训练；分层扫描；再聚焦；证据增强推理                           | [精读](<3d agent/DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models/paper_DeepPaperNote.md>) / [翻译](<3d agent/DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models/paper.md>) |
| Gamma-World                     | 多智能体世界模型         | 生成式多智能体视频；Simplex RoPE；Sparse Hub Attention   | [精读](<3d agent/Gamma-World Generative Multi-Agent World Modeling Beyond Two Players/paper_DeepPaperNote.md>) / [翻译](<3d agent/Gamma-World Generative Multi-Agent World Modeling Beyond Two Players/paper.md>)                                                               |
| Geometrically-Constrained Agent | 3D 空间推理 agent    | 形式化任务约束；参考系约束；受约束几何计算                         | [精读](<3d agent/Geometrically-Constrained Agent for Spatial Reasoning/paper_DeepPaperNote.md>) / [翻译](<3d agent/Geometrically-Constrained Agent for Spatial Reasoning/paper.md>)                                                                                           |
| MPMWorlds                       | 物理动力学推理          | MPM 仿真；视频外推；代码生成 vs 视频扩散                      | [精读](<3d agent/MPMWorlds Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics/paper_DeepPaperNote.md>) / [翻译](<3d agent/MPMWorlds Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics/paper.md>)              |
| P3D-Bench                       | 参数化 3D 生成评测      | Text-to-3D；Image-to-3D；Assembly-3D；可执行 CAD 代码 | [精读](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>) / [翻译](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper.md>)                                  |
| S-Agent                         | 连续多视图空间智能        | 分层空间工具；双记忆；时空证据累积；S-300K                      | [精读](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>) / [翻译](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper.md>)                                                               |
| SimWorld Studio                 | 具身环境生成与学习沙箱      | SimCoder；UE5；MCP 工具；自我演化；共同演化；Gym 接口           | [精读](<3d agent/SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning/paper_DeepPaperNote.md>) / [翻译](<3d agent/SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning/paper.md>) |
| Skill-3D                        | 场景感知工具技能         | Scene Memory；Skill Library；技能检索；agentic 后训练   | [精读](<3d agent/Skill-3D/paper_DeepPaperNote.md>) / [翻译](<3d agent/Skill-3D/paper.md>)                                                                                                                                                                                     |
| Think3D                         | 主动 3D 空间探索       | 3D CoT；点云重建；新视角渲染；Think3D-RL                  | [精读](<3d agent/Think3D/paper_DeepPaperNote.md>) / [翻译](<3d agent/Think3D/paper.md>)                                                                                                                                                                                       |
| Thyme                           | 图像操作与代码推理        | 自主生成代码；沙箱执行；SFT + RL；GRPO-ATS                 | [精读](<../Reasoning/Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>) / [翻译](<../Reasoning/Train/Thyme Think Beyond Images/paper.md>)                                                                                                                                                   |

## 研究洞察入口

| 文档 | 作用 | 核心判断 | 链接 |
|---|---|---|---|
| 3D Agent Insight | 基于 Skill-3D 设计自己的 3D agent 研究路线 | 不要只给模型更多 3D 工具，而要训练它学习 `Ctask → evidence need → tool program → relation expert → verifier` 的可验证几何工具策略。 | [3d_insight](<3d_insight.md>) |

## 总体脉络

当前 `3dAgent` 目录里的论文和项目洞察大致可以分成五条线：

1. **空间推理 agent 线**：`Think3D`、`S-Agent`、`Skill-3D`、`Geometrically-Constrained Agent` 都在回答“VLM 如何通过工具获得更可靠的 3D 空间推理”。它们的区别在于：`Think3D` 强调主动 3D 视角探索，`S-Agent` 强调连续多视图 / 视频中的时空证据累积，`Skill-3D` 强调按场景演化和检索工具技能，`GCA` 强调先把空间问题形式化为参考系和目标约束。
2. **视觉证据落地线**：`DeepScan` 和 `A4-Agent` 都不满足于让 VLM 直接回答，而是先把问题落到可检查的视觉证据上。`DeepScan` 面向通用细粒度视觉问答，强调自底向上的证据扫描；`A4-Agent` 面向 embodied affordance，强调先想象交互，再定位可操作区域。
3. **3D / 物理生成与评测线**：`Code2Worlds`、`P3D-Bench`、`MPMWorlds`、`Gamma-World`、`SimWorld Studio` 更偏 generation、benchmark、simulation 或 world modeling。它们分别关注文本到可执行 4D 仿真代码、参数化 3D 代码评测、物理动力学外推、多智能体可控世界模型，以及可训练具身智能体的自动生成环境。
4. **工具化多模态推理线**：`Thyme` 是更通用的“模型主动写代码处理图像和计算”范式，可作为 3D agent 工具使用能力的外围参考；它关注的是自主决定何时裁剪、旋转、增强、计算，而不是某个具体 3D 任务。
5. **项目洞察线**：`3d_insight.md` 把 `Skill-3D`、`GCA`、`S-Agent` 和 `Thyme` 拼成一个可做的研究方向：把场景感知技能升级为带参考系约束、证据需求、工具程序、关系专家和验证器的 3D tool-use policy，而不是继续堆工具。

## 各论文简要概括

### A4-Agent: An Agentic Framework for Zero-Shot Affordance Reasoning

A4-Agent 面向 embodied AI 中的可供性预测：给定图像和任务指令，模型要找出对象上真正可操作的区域。它把传统端到端 affordance 预测拆成三段：`Dreamer` 用生成模型想象交互后的状态，`Thinker` 用 VLM 判断应操作哪个物体部件，`Spotter` 用检测与分割模型把部件精确落到 mask / box / keypoint。

这篇的核心价值是把“高层任务推理”和“低层视觉定位”解耦。它说明可供性任务不一定要靠专门训练一个单体模型，也可以通过测试时编排多个基础模型实现强零样本泛化。

链接：[精读](<3d agent/A4-Agent An Agentic Framework for Zero-Shot Affordance Reasoning/paper_DeepPaperNote.md>) / [翻译](<3d agent/A4-Agent An Agentic Framework for Zero-Shot Affordance Reasoning/paper.md>)

### CompassAD: Intent-Driven 3D Affordance Grounding in Functionally Competing Objects

CompassAD 关注一个更细的 3D affordance 难题：场景里多个物体都具有相似功能，但只有一个真正符合当前任务意图。比如“切苹果”应选择刀而不是剪刀，“喝咖啡”应选择杯子而不是碗；模型不能只看 affordance 是否存在，还要理解语言意图和竞争物体之间的差异。

它贡献了 CompassAD 数据集，并提出 CompassNet。方法上，`ICI` 把语言-几何对齐限制在实例内部，减少语义串台；`BCR` 在区域级和点级拉开目标区域与干扰区域。适合和 A4-Agent 放在一起比较：A4-Agent 偏零样本 agentic pipeline，CompassAD 偏 3D 点云场景中的意图区分与监督式建模。

链接：[笔记](<CompassAD - Intent-Driven 3D Affordance Grounding in Functionally Competing Objects.md>)

### Code2Worlds: Empowering Coding LLMs for 4D World Generation

Code2Worlds 把文本到四维世界生成表述为语言到仿真代码生成。对象流借助参数库与参考代码库生成细粒度程序化资产，场景流将稀疏环境描述分解为 manifest、数值参数和 Infinigen/Blender 场景；后处理智能体再统一两者，生成物理参数与时间动态。

它最关键的设计是把静态外观批评和动态运动批评分开。VLM-Motion Critic 观察渲染 rollout，并迭代修正仿真参数；消融中去掉它会使物理失败率从 `10%` 升到 `60%`。不过 Code4D 目前只列出 `10` 条提示，多项指标依赖 GPT-4o 评分，系统也受程序库覆盖和非实时仿真成本限制。

链接：[精读](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>) / [翻译](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper.md>)

### DeepScan: A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models

DeepScan 是免训练视觉落地推理框架，核心是让 LVLM 在回答前先找到证据。它不走“一次性检测完整证据区域”的自顶向下路线，而是先在局部图块中找关键线索，再用点式代理回到原图恢复证据，随后通过再聚焦选择最合适的上下文视图，最后把细粒度证据和粗粒度视图一起交给 LVLM 推理。

这篇对 3D agent 的启发是：工具增强不只是“多看几张图”，而是要控制证据的粒度和上下文范围。它的失败分析也有价值：证据找错会让答案有“看似有依据”的错误；证据相距很远时，简单合并视图又会引入大量噪声。

链接：[精读](<3d agent/DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models/paper_DeepPaperNote.md>) / [翻译](<3d agent/DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models/paper.md>)

### Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players

Gamma-World 是生成式多智能体世界模型，目标是在共享环境中同时建模多个可控 agent 的未来观测。它提出 `Simplex Rotary Agent Encoding`，用正单纯形方式表示 agent 身份，避免固定 slot 顺序；再用 `Sparse Hub Attention` 让 hub token 作为跨 agent 交互中介，把跨 agent 注意力从二次复杂度降到近似线性。

它和空间推理 agent 的关系不是“问答”，而是“可控世界模拟”。如果未来要做 embodied 3D agent 的 rollout、协作机器人或多人交互环境，这篇提供了多智能体一致性、身份置换对称和实时生成的结构参考。

链接：[精读](<3d agent/Gamma-World Generative Multi-Agent World Modeling Beyond Two Players/paper_DeepPaperNote.md>) / [翻译](<3d agent/Gamma-World Generative Multi-Agent World Modeling Beyond Two Players/paper.md>)

### Geometrically-Constrained Agent for Spatial Reasoning

GCA 认为 VLM 空间推理的核心问题是“语义到几何的鸿沟”：模型能理解语言，但在语义空间中会丢失参考系、方向、尺度等几何细节。它提出先生成形式化任务约束 `Ctask = (CR, CO)`，其中 `CR` 是参考系约束，`CO` 是目标约束；随后所有工具调用和代码计算都必须在这个几何约束下执行。

这篇和 `Think3D`、`S-Agent`、`Skill-3D` 的区别很清楚：它不首先问“用什么工具”，而先问“这个空间问题应该在哪个坐标系下被定义”。参考系消融显示 `CR` 比 `CO` 更关键，因此它很适合作为空间推理论文中“参考系形式化”的代表工作。

链接：[精读](<3d agent/Geometrically-Constrained Agent for Spatial Reasoning/paper_DeepPaperNote.md>) / [翻译](<3d agent/Geometrically-Constrained Agent for Spatial Reasoning/paper.md>)

### MPMWorlds: Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics

MPMWorlds 构建了一个 2D Material Point Method 物理仿真数据集，用来研究模型能否从视频中推断物理动力学并向未来外推。论文比较了代码生成和视频扩散路线：代码生成能产生时间上更稳定、物理上更一致的外推，但很难从视觉输入中反推出物理参数；视频扩散更擅长捕捉几何外观，却容易产生物理上不合理的长期外推。

它对 3D agent 的意义在于提供了一个物理推理视角：当任务从静态空间关系走向动态物理外推时，单纯视觉预测和显式模拟各有短板。未来 agent 可能需要把视觉识别、参数反演和可执行物理模拟结合起来。

链接：[精读](<3d agent/MPMWorlds Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics/paper_DeepPaperNote.md>) / [翻译](<3d agent/MPMWorlds Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics/paper.md>)

### P3D-Bench: Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning

P3D-Bench 是参数化 3D 生成和结构推理 benchmark。它要求 LLM / MLLM 输出可执行的 JSON、OpenSCAD、CadQuery 或 Three.js 程序，并从几何、拓扑、判别和部件结构等维度评价结果，而不是只看程序能否运行或渲染是否好看。

这篇的重点是“可执行不等于正确”。许多模型能写出看起来合理的 3D 程序，但尺寸、部件关系、装配结构仍然错。它适合给 3D agent 研究提供评测参照：如果 agent 要生成或修改 3D 结构，必须检查参数化几何和结构正确性。

链接：[精读](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>) / [翻译](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper.md>)

### S-Agent: Spatial Tool-Use Elicits Reasoning for Spatial Intelligence

S-Agent 把空间推理从单帧静态问答改成连续多视图 / 视频中的时空证据累积。VLM 作为语义规划器决定需要什么证据，分层空间工具负责 2D 定位、3D 提升和高层空间知识聚合；双记忆机制分别保存演化场景状态和推理上下文。

这篇最适合作为“空间工具调用 + 记忆”的代表工作。它不仅能免训练增强强 VLM，还能把生成的空间轨迹蒸馏为 S-Agent-8B。和 Think3D 相比，它更强调跨帧状态维护；和 Skill-3D 相比，它更强调分层工具和双记忆，而不是技能库演化。

链接：[精读](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>) / [翻译](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper.md>)

### SimWorld Studio: Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning

SimWorld Studio 把 LLM coding agent 生成的三维内容变成可验证、可交互、可训练、可共同演化的具身学习沙箱。它的核心是 SimCoder：通过 UE5、MCP 工具、技能库、规则验证器和 VLM 验证器生成物理上可用的三维环境，并导出 Gymnasium 风格接口供具身智能体训练。

这篇最适合放在 `Code2Worlds`、`P3D-Bench` 和 `Skill-3D` 之间看：它不像 P3D-Bench 那样主要评参数化 3D 程序，也不像 Skill-3D 那样直接做空间问答工具调度，而是提供一个能持续产生环境、任务、奖励和反馈的具身训练平台。对后续 3D agent 研究，它的启发是环境本身可以成为训练工具调用策略和空间推理策略的沙箱。

链接：[精读](<3d agent/SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning/paper_DeepPaperNote.md>)

### Skill-3D: Evolving Scene-Aware Skills for Agentic 3D Spatial Reasoning

Skill-3D 关注工具增强 3D agent 中的工具误用问题。它认为不同场景和任务需要不同证据链，而现有 agent 常把同一套工具策略套到所有问题上。论文用 `Scene Memory` 记录轨迹，用 `Skill Library` 把相似场景的成功轨迹蒸馏为可复用技能，并把失败轨迹变成 lessons。

它的核心贡献是把工具调用从“临时规划”推进到“可检索、可演化的场景感知技能”。和 GCA 相比，Skill-3D 主要解决工具流程选择；和 S-Agent 相比，它更强调技能长期演化与后训练。

链接：[精读](<3d agent/Skill-3D/paper_DeepPaperNote.md>) / [翻译](<3d agent/Skill-3D/paper.md>)

### Think3D: Thinking with Space for Spatial Reasoning

Think3D 把 VLM 从被动看图推理改造成主动三维探索。它让 agent 重建 3D 点云、渲染新视角，并在多轮过程中操作空间观察，从而获得类似三维思维链的能力。对闭源强模型，它可以作为零样本插件；对小模型，论文进一步提出 Think3D-RL，让模型学习更有效的空间探索策略。

这篇是当前目录里最直接的“3D active perception”代表。它适合和 S-Agent、Skill-3D、GCA 串起来：Think3D 提供主动视角探索，S-Agent 提供跨帧证据记忆，Skill-3D 提供技能检索，GCA 提供参考系约束。

链接：[精读](<3d agent/Think3D/paper_DeepPaperNote.md>) / [翻译](<3d agent/Think3D/paper.md>)

### Thyme: Think Beyond Images

Thyme 不是专门的 3D 论文，但它是重要的工具化多模态推理参考。它让 MLLM 自主生成并执行 Python 代码，对图像进行裁剪、缩放、旋转、对比度增强和数学计算，并由沙箱返回结果进入下一轮推理。训练上，它先用大规模 SFT 冷启动，再用 RL 优化“何时用代码、如何用代码”。

对 3D agent 来说，Thyme 的启发是：工具不一定必须是固定 API，也可以是模型动态生成的可执行程序；但这要求沙箱、奖励和温度策略足够稳。它可以作为 Think3D/GCA 中代码计算模块的外围参考。

链接：[精读](<../Reasoning/Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>) / [翻译](<../Reasoning/Train/Thyme Think Beyond Images/paper.md>)

## 横向比较速记

| 比较维度 | 代表论文 | 一句话判断 |
|---|---|---|
| 主动 3D 探索 | Think3D | 通过重建点云和渲染新视角，让 VLM 主动“用空间想”。 |
| 连续多视图证据 | S-Agent | 把空间推理改成跨帧、跨工具、跨记忆的证据累积过程。 |
| 工具流程学习 | Skill-3D | 从成功/失败轨迹中演化场景感知工具技能。 |
| 几何任务形式化 | GCA | 先定义参考系和目标，再让工具与代码在约束下计算。 |
| 可训练 3D 工具策略 | [3d_insight](<3d_insight.md>) | 将 Skill-3D 的技能库、GCA 的参考系约束、S-Agent 的关系专家和 Thyme 的训练配方合成 GeoSkill-Agent 方向。 |
| 视觉证据落地 | DeepScan | 自底向上找视觉证据，减少注意力漂移和噪声上下文。 |
| 交互区域定位 | A4-Agent / CompassAD | 前者用 agentic pipeline 零样本定位，后者处理 3D 竞争物体和意图区分。 |
| 3D 生成评测 | P3D-Bench | 检查可执行程序背后的参数、结构和装配正确性。 |
| 动态物理 / 世界模型 | MPMWorlds / Gamma-World | 前者关注物理外推，后者关注多智能体可控世界生成。 |
| 可执行 4D 世界生成 | Code2Worlds | 用对象/场景双流和 VLM 运动反馈生成可编辑的 Blender 物理仿真。 |
| 具身学习环境生成 | SimWorld Studio | 用 SimCoder 在 UE5 中生成可验证 Gym 环境，并让环境生成与具身智能体学习共同演化。 |
| 通用代码工具使用 | Thyme | 让 MLLM 自主写代码处理图像和计算，为工具化推理提供通用范式。 |
