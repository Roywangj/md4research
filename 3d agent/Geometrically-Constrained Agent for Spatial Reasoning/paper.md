# Geometrically-Constrained Agent for Spatial Reasoning

**Authors:** Zeren Chen, Xiaoya Lu, Zhijie Zheng, Pengrui Li, Lehan He, Yijin Zhou, Jing Shao, Bohan Zhuang, Lu Sheng  
**Source:** `Chen 等 - 2025 - Geometrically-Constrained Agent for Spatial Reasoning.pdf`  
**Detected source format:** selectable-text PDF (`pdf-text`)  
**Reader type:** full-paper Chinese-English Markdown reader with figure/table assets.

## Page / Section Index

| Section | Pages | Notes |
|---|---:|---|
| Abstract | p.1 | bilingual body |
| 1 Introduction | pp.1-2 | motivation, research question, contribution |
| 2 Related Work | pp.2-3 | spatial reasoning, tool agents, constraint-guided reasoning |
| 3 Methodology | pp.3-5 | GCA, `Ctask`, formalization, constrained computation |
| 3.4 Discussion | p.5 | why the two-stage design matters |
| 4 Experiments | pp.5-8 | benchmarks, main results, ablations, error analysis |
| 5 Conclusion | pp.8-9 | conclusion and high-level limitations |
| Appendix / References | pp.9-27 | references, extra ablations, prompts, case studies |

## Terminology Ledger

| Canonical term | Chinese rendering | Decision |
|---|---|---|
| Geometrically-Constrained Agent | 几何约束代理 | 方法名；首次写作 `GCA` 后可直接使用缩写。 |
| semantic-to-geometric gap | 语义到几何的鸿沟 | 本文核心问题。 |
| formal task constraint | 形式化任务约束 | 保留符号 `Ctask`。 |
| Reference Frame Constraint | 参考系约束 | 保留符号 `CR`。 |
| Objective Constraint | 目标约束 | 保留符号 `CO`。 |
| semantic analyst | 语义分析者 | 模型在形式化阶段的角色。 |
| task solver | 任务求解器 | 模型在计算阶段的角色。 |
| constrained geometric computation | 受约束几何计算 | 工具与代码均受 `Ctask` 约束。 |
| knowledge-augmented code generation | 知识增强代码生成 | 保留缩写 `KACG`。 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Vision Language Models exhibit a fundamental semantic-to-geometric gap in spatial reasoning. They are strong at qualitative semantic inference, but their reasoning takes place in a lossy semantic space that is misaligned with high-fidelity geometry. Existing training-based methods suffer from an oracle paradox, learning flawed spatial logic from imperfect oracles. Existing tool-integrated methods constrain final computation but leave the VLM planning process unconstrained.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 视觉语言模型在空间推理中存在根本性的语义到几何鸿沟。它们擅长定性语义推断，但推理发生在有损的语义空间中，和高保真几何并不对齐。已有训练方法会遭遇 oracle 悖论，从不完美的 oracle 中学习有缺陷的空间逻辑；已有工具集成方法虽然约束了最后计算，却没有约束模型的规划过程。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The paper proposes Geometrically-Constrained Agent, a training-free agentic paradigm. The VLM is decoupled into two roles. First, as a semantic analyst, it translates an ambiguous user query into a formal and verifiable task constraint that defines the reference frame and objective. Second, as a task solver, it generates and executes tool calls strictly within the deterministic bounds of that constraint.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 论文提出几何约束代理 `GCA`，这是一个无需训练的代理式范式。模型被拆成两个角色。第一，它作为语义分析者，把用户模糊查询翻译成形式化、可验证的任务约束，定义参考系和目标。第二，它作为任务求解器，在该约束规定的确定性边界内生成并执行工具调用。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> This strategy provides a robust and verifiable reasoning pathway for spatial reasoning. Experiments show that GCA achieves state-of-the-art performance on multiple spatial reasoning benchmarks and surpasses existing training-based and tool-integrated methods by around 27%.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 这种策略为空间推理提供了稳健且可验证的推理路径。实验表明，`GCA` 在多个空间推理基准上达到新的最佳表现，并相对已有训练方法和工具集成方法提升约 `27%`。

## 1 Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Spatial reasoning requires precise geometric grounding. VLMs can often infer qualitative relations, but spatial questions frequently depend on viewpoint, coordinate frame, direction, distance, or object orientation. When visual information is translated into a textual semantic space, many geometric details are lost or distorted.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 空间推理需要精确的几何 grounding。视觉语言模型往往能推断定性关系，但空间问题经常取决于视角、坐标系、方向、距离或物体朝向。当视觉信息被转成文本语义空间时，许多几何细节会丢失或变形。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The paper illustrates this with perspective-dependent questions. If the query asks from the perspective of a user sitting on a sofa, an unconstrained VLM may default to the image camera viewpoint. The answer can then be wrong before any tool is invoked, because the plan is already grounded in the wrong reference frame.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 论文用视角依赖问题说明这一点。如果问题要求从坐在沙发上的用户视角回答，无约束模型可能默认采用图片相机视角。这样在调用任何工具之前，计划已经被锚定到错误参考系，后续计算自然会错。

### Figure 1. Overview

![Figure 1](3d%20agent/Geometrically-Constrained%20Agent%20for%20Spatial%20Reasoning/assets/page_002_fig_figure_1.png)

**Caption:** Figure 1 explains the semantic-geometric gap and the proposed geometrically-constrained reasoning path. The formal task constraint becomes a deterministic bridge between ambiguous semantics and geometric computation.

**Caption[CN]:** 图 1 展示语义到几何的鸿沟，以及本文提出的几何约束推理路径。形式化任务约束成为模糊语义和几何计算之间的确定性桥梁。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The central research question is how to bridge the VLM’s semantic-to-geometric gap. The authors argue that the solution is not to force the VLM to compute high-fidelity geometry directly. Instead, the VLM should use its semantic commonsense to define a formal task constraint for subsequent deterministic computation.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 本文的核心问题是如何弥合模型的语义到几何鸿沟。作者认为，解决方案不是强迫模型直接计算高保真几何，而是让模型用语义常识定义一个形式化任务约束，再交给后续确定性计算。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The formal task constraint must satisfy three requirements. It should be grammatically rich enough to represent complex spatial concepts such as viewpoints, semantically clear enough for the VLM to generate, and geometrically sound enough to provide deterministic and verifiable constraints for computation.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 形式化任务约束需要满足三个要求。它要有足够语法表达能力，能描述视角等复杂空间概念；要足够语义清晰，使模型可以生成；还要几何上合理，为后续计算提供确定且可验证的约束。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> GCA therefore decouples the reasoning process into task formalization and constrained geometric computation. In the first stage, the VLM defines what to solve. In the second stage, it solves the defined problem through tool calls and code under immutable constraints.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 因此，`GCA` 把推理拆成任务形式化和受约束几何计算。第一阶段，模型定义要解什么；第二阶段，模型在不可变约束下通过工具和代码解决已经定义好的问题。

## 2 Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Recent VLMs have improved on spatial reasoning through larger backbones, spatial VQA data, explicit grounding, visual chain-of-thought, 3D reconstruction, code-driven reasoning, and mental simulation. However, precise 3D spatial reasoning remains difficult because it requires coordinate-aware geometric computation rather than only semantic recognition.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 近期视觉语言模型通过更大 backbone、空间问答数据、显式 grounding、视觉思维链、3D 重建、代码驱动推理和心理模拟提升空间能力。但精确 3D 空间推理仍然困难，因为它需要坐标敏感的几何计算，而不只是语义识别。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Training-based methods attempt to improve spatial reasoning by learning from annotated or generated data. The paper argues that these methods may inherit flawed spatial logic from imperfect supervision. This is described as an oracle paradox: the model learns from an oracle that is not actually geometrically reliable.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 基于训练的方法试图从标注或生成数据中学习空间推理。论文认为，这些方法可能继承不完美监督中的错误空间逻辑。作者称之为 oracle 悖论：模型向一个几何上并不可靠的 oracle 学习。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Tool-integrated agents add modules such as reconstruction, detection, segmentation, depth estimation, and code execution. These tools can constrain the final computation, but the VLM may still create a geometrically flawed plan before computation begins. The paper positions GCA as a method that constrains planning itself.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 工具集成代理接入重建、检测、分割、深度估计和代码执行等模块。这些工具可以约束最后计算，但模型可能在计算开始前已经生成几何错误的计划。本文把 `GCA` 定位为一种约束规划本身的方法。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The paper also relates to constraint-guided reasoning. Classical formalisms such as PDDL are good at discrete symbolic states but cannot easily express continuous, relative, and viewpoint-dependent spatial concepts. GCA therefore introduces a spatially grounded constraint representation centered on reference frames.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 论文也和约束引导推理相关。传统形式如 PDDL 擅长离散符号状态，却难以表达连续、相对和视角依赖的空间概念。因此，`GCA` 提出一种以参考系为核心的空间约束表示。

## 3 Methodology

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> A generic ReAct-style agent can be written as a policy that takes the query, visual information, tool set, and previous reasoning state, then produces the next reasoning step. The authors argue that this policy is unconstrained and unreliable for deterministic spatial reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 一般 ReAct 式代理可以写成一个策略：输入问题、视觉信息、工具集合和上一轮推理状态，然后产生下一步推理。作者认为，这种策略没有约束，因此在确定性空间推理中不可靠。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> GCA replaces this generic policy with two stages:

$$
C_{\mathrm{task}}\leftarrow F_{\mathrm{formalize}}(q,v)
$$

$$
r_t=F_{\mathrm{compute}}(C_{\mathrm{task}},T,r_{t-1})
$$

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> `GCA` 用两个阶段替换通用策略。第一阶段生成形式化任务约束 `Ctask`；第二阶段在该约束、工具集合和上一轮状态下进行受约束计算。

### 3.1 Formal Task Constraint

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The task constraint is defined as a tuple:

$$
C_{\mathrm{task}}=(C_R,C_O)
$$

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 任务约束由两个子约束组成：参考系约束 `CR` 和目标约束 `CO`。`CR` 定义回答问题时使用的坐标系，`CO` 定义在该坐标系下要测量或判断的目标。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The reference frame is a 3D Cartesian coordinate system with an origin and three orthogonal basis vectors. It follows the OpenCV convention: the positive z-axis points forward, the positive y-axis points down, and the positive x-axis follows the right-hand rule.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 参考系是一个三维笛卡尔坐标系，包括原点和三条正交基向量。它遵循 OpenCV 约定：正 z 轴指向前方，正 y 轴指向下方，正 x 轴按右手规则确定。

### Figure 3. Reference Frame

![Figure 3](3d%20agent/Geometrically-Constrained%20Agent%20for%20Spatial%20Reasoning/assets/page_004_fig_figure_3.png)

**Caption:** Figure 3 illustrates the three types of reference frames: object-based, camera-based, and direction-based.

**Caption[CN]:** 图 3 展示三种参考系：物体参考系、相机参考系和方向参考系。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> In an object-based frame, the coordinate system is defined by the intrinsic axes of an object. In a camera-based frame, it is defined by a specific camera viewpoint. In a direction-based frame, it is defined by a vector connecting two locations.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 物体参考系由物体自身轴向定义；相机参考系由特定相机视角定义；方向参考系由连接两个位置的向量定义。三者共同覆盖了许多静态空间问题中的视角和方向表达。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The objective constraint specifies what must be measured relative to the established reference frame. For example, in a question asking whether a chair is west of a toaster, the toaster can define the reference frame, while the chair-to-toaster positional relation defines the objective.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 目标约束规定在已建立参考系下要测量什么。例如，如果问题问椅子是否在烤面包机西侧，烤面包机可以定义参考系，而椅子相对烤面包机的位置关系就是目标。

### 3.2 Automated Formalization

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> The VLM acts as a semantic analyst. It uses qualitative interpretation of the query and visual context to generate `Ctask`. The key design choice is procedural: the model must complete formalization before any computation begins.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 模型在这一阶段作为语义分析者。它利用问题和视觉上下文的定性理解生成 `Ctask`。关键设计是流程性的：模型必须在任何计算开始前完成形式化。

### 3.3 Constrained Geometric Computation

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Once `Ctask` is established, the VLM becomes a constrained task solver. The execution is not a one-shot generation. It is an iterative closed-loop process involving data acquisition, ambiguity resolution, and augmented computation.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 一旦 `Ctask` 建立，模型就变成受约束任务求解器。执行不是一次性生成，而是包含数据获取、歧义消解和增强计算的闭环过程。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Data acquisition is dictated by `Ctask`. If an object-based frame is defined by a sink, the system must acquire the sink orientation. If an objective mentions a leftmost chair, the model must resolve which detected chair corresponds to that phrase.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 数据获取由 `Ctask` 决定。如果物体参考系由水槽定义，系统就必须取得水槽朝向。如果目标提到“最左边的椅子”，模型就必须在多个检测候选中确定哪一个对应这个短语。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> For final computation, the system uses knowledge-augmented code generation. Instead of expecting the coder to invent geometric formulas from memory, a fixed library of verified formulas is injected according to the bound variable types.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 最后计算使用知识增强代码生成。系统不会期待代码器凭记忆发明几何公式，而是根据已绑定变量类型注入固定且验证过的公式库。

### Figure 2. Overall Paradigm

![Figure 2](3d%20agent/Geometrically-Constrained%20Agent%20for%20Spatial%20Reasoning/assets/page_003_fig_figure_2.png)

**Caption:** Figure 2 shows the complete GCA paradigm: task formalization first, then constrained geometric computation with tools and code.

**Caption[CN]:** 图 2 展示完整 `GCA` 范式：先任务形式化，再通过工具和代码进行受约束几何计算。

## 3.4 Discussion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The discussion emphasizes that GCA addresses two deficiencies at once. The formalization stage prevents flawed planning in lossy semantic space. The computation stage grounds tool calls and code execution in an immutable constraint.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 讨论部分强调，`GCA` 同时解决两个缺陷。形式化阶段防止模型在有损语义空间中生成错误计划；计算阶段则把工具调用和代码执行绑定到不可变约束上。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The method therefore separates what to solve from how to solve it. This separation is especially important for spatial reasoning, where a wrong reference frame can invalidate every later computation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 因此，方法把“要解什么”和“怎么解”分开。这对空间推理尤其重要，因为错误参考系会让后续每一步计算都失去意义。

## 4 Experiments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The experiments evaluate GCA on several spatial reasoning benchmarks, including MMSI-Bench, MindCube-tiny, OmniSpatial, SPBench, and CV-Bench. The current toolbox is primarily designed for image-based inputs, so the evaluation focuses on single-image and multi-image spatial logic.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 实验在多个空间推理基准上评测 `GCA`，包括 `MMSI-Bench`、`MindCube-tiny`、`OmniSpatial`、`SPBench` 和 `CV-Bench`。当前工具箱主要面向图像输入，因此评测集中在单图和多图空间逻辑。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The primary VLM is Qwen3-VL-Thinking. The authors also evaluate generalizability across models such as GLM-4.5V, GPT-4o, and Gemini-2.5-Pro. Open-source models are deployed with vLLM, and the agent architecture uses Ray and LangGraph.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 主实验使用 `Qwen3-VL-Thinking`。作者还在 `GLM-4.5V`、`GPT-4o` 和 `Gemini-2.5-Pro` 等模型上评估泛化性。开源模型通过 vLLM 部署，代理架构使用 Ray 和 LangGraph。

### Table 1. Main Results

![Table 1](3d%20agent/Geometrically-Constrained%20Agent%20for%20Spatial%20Reasoning/assets/page_006_fig_table_1.png)

**Caption:** Table 1 reports benchmark results. The automatic crop is narrow, so the key values are transcribed below.

**Caption[CN]:** 表 1 报告主实验结果。自动裁剪较窄，因此关键数字在下文转写。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> GCA achieves an average accuracy of around 64.8% in the main text, while the table average column shows 65.1. It surpasses the strongest foundation VLM baseline, Gemini-2.5-Pro, by around 12%, SpatialLadder by around 27%, and TIGeR by around 38%.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 正文报告 `GCA` 平均准确率约为 `64.8%`，表格平均列显示为 `65.1`。它相对最强基础模型 `Gemini-2.5-Pro` 提升约 `12%`，相对 `SpatialLadder` 提升约 `27%`，相对 `TIGeR` 提升约 `38%`。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> On MMSI-Bench, GCA reaches 47.6%, while many counterparts remain close to the random-guess level of a four-choice benchmark. On MindCube-tiny, GCA reaches 64.2%. The paper attributes this improvement to preventing VLMs from defaulting to flawed semantic shortcuts.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在 `MMSI-Bench` 上，`GCA` 达到 `47.6%`，而许多对比方法接近四选一随机猜测水平。在 `MindCube-tiny` 上，`GCA` 达到 `64.2%`。论文认为，这来自防止模型默认采用错误语义捷径。

### Figure 4. Formalization Ablation

![Figure 4](3d%20agent/Geometrically-Constrained%20Agent%20for%20Spatial%20Reasoning/assets/page_007_fig_figure_4.png)

**Caption:** Figure 4 compares CoT-only, unconstrained tool use, prompted tool use, GCA, and human-annotated task constraints.

**Caption[CN]:** 图 4 比较纯 CoT、无约束工具、弱提示工具、`GCA` 和人工标注任务约束。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The formalization ablation is central. CoT-only obtains 32.6. Unconstrained tool integration obtains 40.1. Prompting the model to pay attention to the reference frame and objective obtains 41.9. GCA obtains 47.6. Human-annotated oracle constraints obtain 49.5.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 形式化消融是论文最核心的证据。纯 CoT 为 `32.6`；无约束工具集成为 `40.1`；提示模型注意参考系和目标为 `41.9`；`GCA` 为 `47.6`；人工标注 oracle 约束为 `49.5`。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The small gap between GCA and the oracle suggests that task formalization is largely within current VLM capability. The larger gap between GCA and prompted tools suggests that formal constraints must be operationally bound to computation rather than merely stated as hints.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> `GCA` 和 oracle 的差距较小，说明当前模型大体具备任务形式化能力。`GCA` 和弱提示工具之间差距更大，说明约束不能只是提示语，而必须被绑定到后续计算流程。

### Figure 5. Generalizability

![Figure 5](3d%20agent/Geometrically-Constrained%20Agent%20for%20Spatial%20Reasoning/assets/page_007_fig_figure_5.png)

**Caption:** Figure 5 reports generalizability across foundation VLMs. The extracted image includes neighboring content; use this only as a visual reference.

**Caption[CN]:** 图 5 报告跨基础模型泛化。该自动裁剪图包含相邻内容，只作为视觉参考。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> GCA improves all tested foundation VLMs, with an average relative improvement of around 37%. Gemini-2.5-Pro has the strongest CoT-only baseline at 36.9 on MMSI-Bench and rises to 55.0 under GCA, corresponding to a relative improvement of around 49%.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> `GCA` 提升了所有被测试的基础模型，平均相对提升约 `37%`。`Gemini-2.5-Pro` 在 `MMSI-Bench` 上有最强 CoT 基线 `36.9`，使用 `GCA` 后升到 `55.0`，相对提升约 `49%`。

### Table 2. Component Ablation

![Table 2](3d%20agent/Geometrically-Constrained%20Agent%20for%20Spatial%20Reasoning/assets/page_008_fig_table_2.png)

**Caption:** Table 2 ablates tool integration, knowledge-augmented code generation, feedback, and `Ctask`.

**Caption[CN]:** 表 2 消融工具集成、知识增强代码生成、反馈消歧和 `Ctask`。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Component ablation shows two levels of improvement. Tool integration, knowledge-augmented code generation, and feedback improve from 32.6 to 40.1. Adding `Ctask` further improves accuracy to 47.6. Thus, the formal constraint contributes as much as the whole standard tool-integrated stack in this ablation.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 组件消融显示两层增益。工具集成、知识增强代码生成和反馈消歧把结果从 `32.6` 提升到 `40.1`。加入 `Ctask` 后进一步提升到 `47.6`。因此，在这个消融中，形式化约束的贡献接近整个标准工具集成栈的贡献。

### Figure 6. Error Attribution

![Figure 6](3d%20agent/Geometrically-Constrained%20Agent%20for%20Spatial%20Reasoning/assets/page_008_fig_figure_6.png)

**Caption:** Figure 6 analyzes failure modes in formalization and computation.

**Caption[CN]:** 图 6 分析形式化阶段和计算阶段的失败模式。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Error attribution shows that around 30% of errors occur in `Fformalize`, while the remaining 70% occur in `Fcompute`. Perception failures account for around 24%, Python tool errors for around 25%, and other issues for around 21%.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 错误归因显示，约 `30%` 错误发生在 `Fformalize`，其余 `70%` 发生在 `Fcompute`。感知失败约 `24%`，Python 工具错误约 `25%`，其他问题约 `21%`。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> This analysis is important because it clarifies that GCA does not eliminate tool-chain fragility. It makes the reasoning pathway more explicit and verifiable, but reconstruction, orientation, coordinate transformation, and parameter passing remain difficult.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 这个分析很重要，因为它说明 `GCA` 并没有消除工具链脆弱性。它让推理路径更显式、可验证，但重建、朝向、坐标变换和参数传递仍然困难。

## 5 Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper introduces GCA as a training-free agentic paradigm for bridging the semantic-to-geometric gap. The ambiguous spatial query is transformed into a constrained mathematical problem, preventing the VLM from relying on lossy internal geometric imagination.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文提出 `GCA`，一个无需训练的代理式范式，用来弥合语义到几何的鸿沟。模糊空间查询被转化为带约束的数学问题，从而避免模型依赖内部有损几何想象。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Experiments demonstrate strong performance across multiple benchmarks. The authors also note that GCA is more computationally demanding than simple CoT, and that the structured outputs of GCA may serve as supervision for more efficient future end-to-end spatial VLMs.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 实验证明 `GCA` 在多个基准上表现强。作者也指出，`GCA` 比简单 CoT 更耗计算；但它产生的结构化输出可以作为未来更高效端到端空间模型的监督信号。

## Appendix Highlights

### Table 3. Task Constraint Ablation

![Table 3](3d%20agent/Geometrically-Constrained%20Agent%20for%20Spatial%20Reasoning/assets/page_012_fig_table_3.png)

**Caption:** Table 3 ablates reference-frame and objective constraints.

**Caption[CN]:** 表 3 消融参考系约束和目标约束。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The appendix shows that removing the objective constraint only drops performance from 47.6 to 46.4. Removing the reference frame constraint drops performance to 41.0. Using `Ctask` as a text hint without tool integration gives only 33.5.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 附录显示，去掉目标约束只让结果从 `47.6` 降到 `46.4`。去掉参考系约束则降到 `41.0`。没有工具集成、只把 `Ctask` 当文本提示时，结果只有 `33.5`。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The appendix also reports stability over ten independent runs on MMSI-Bench: 47.6 ± 0.3. The low variance supports the claim that explicit constraints reduce stochastic ambiguity in later computation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 附录还报告了在 `MMSI-Bench` 上十次独立运行的稳定性：`47.6 ± 0.3`。低方差支持作者的说法：显式约束减少了后续计算中的随机歧义。

### Figure 10. Object-based Reference Frame Case

![Figure 10](3d%20agent/Geometrically-Constrained%20Agent%20for%20Spatial%20Reasoning/assets/page_024_fig_figure_10.png)

**Caption:** Figure 10 shows an object-based reference frame case study. The agent first formalizes the reference frame, then obtains object detections, orientation, point clouds, and code-based computation.

**Caption[CN]:** 图 10 展示物体参考系案例。代理先形式化参考系，再获取目标检测、朝向、点云和代码计算。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The case studies are useful for understanding what GCA operationally changes. Instead of answering from an implicit camera viewpoint, the agent constructs a reference frame from the problem statement and forces later perception and computation to respect it.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 案例有助于理解 `GCA` 实际改变了什么。代理不再默认从相机视角回答，而是从问题陈述中构造参考系，并强制后续感知和计算遵守这个参考系。

## Reading Notes

- The most reusable idea is to make the reference frame explicit before any tool planning.
- `Ctask` is not just a prompt. It must constrain tool calls, variable binding, and code execution.
- The main limitation is that computation-stage errors remain large, especially perception, reconstruction, orientation, and coordinate-transform mistakes.
- Compared with Skill-3D, this paper is less about reusable tool skills and more about per-query geometric contracts.
- Compared with Think3D-style reconstruction reasoning, this paper emphasizes that reconstruction alone is not enough if the problem has already been framed in the wrong coordinate system.

