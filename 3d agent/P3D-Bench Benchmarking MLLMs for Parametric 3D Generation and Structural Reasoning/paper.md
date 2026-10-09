---
title: "P3D-Bench: Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning"
authors: "Yikang Yang, Zhanpeng Hu, Youtian Lin, Mengqi Zhou, Jingxi Xu, Feihu Zhang, Jiaheng Liu, Yao Yao"
source: "local PDF / arXiv:2606.11152v2"
source_path: "/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/6IK9XKXJ/Yang 等 - 2026 - P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning.pdf"
reader_type: "nature-reader bilingual markdown"
created: "2026-06-24"
---

# P3D-Bench: Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning

**Paper type:** benchmark / resource paper for parametric 3D generation, code-generating MLLMs, and structural reasoning.

**One-sentence map:** P3D-BENCH asks whether current LLM/MLLMs can write executable parametric 3D programs that are not only plausible-looking but also dimensionally precise, topologically valid, and structurally correct at the part/assembly level.

## Page / section index

| Pages | Section | What to look for |
|---|---|---|
| 1-3 | Title, Abstract, Introduction | Main gap: plausible executable 3D code still misses precise parametric geometry and part structure |
| 3-4 | Related Work | Why prior benchmarks do not jointly test executable code, parameters, spatial layout, assemblies, and parts |
| 4-8 | Tasks, Dataset, Evaluation | Three tasks, four output formats, P3D-Dataset construction, Geo/Topo/Judge/Part metrics |
| 9-16 | Experiments | Model tiers, OpenSCAD advantage, Judge/Part details, invalid-output taxonomy, thinking/multi-turn analyses |
| 17-20 | References | Bibliography |
| 21-30 | Appendix A-E | Preprocessing, annotation, metric implementation, shared-case comparison, decomposition fidelity, cost-quality, full metrics |
| 31-42 | Appendix F | Qualitative visualization galleries |

## Terminology ledger

| Canonical term | 中文对应 | Decision / note |
|---|---|---|
| P3D-BENCH | P3D-BENCH | 本文提出的参数化 3D 生成与结构推理基准；保留英文名。 |
| P3D-Dataset | P3D-Dataset | 由 Text2CAD v1.1 和 Fusion 360 Gallery 过滤、标注、验证得到的数据集。 |
| parametric 3D program | 参数化 3D 程序 | 以 JSON/OpenSCAD/CadQuery/Three.js 等代码表达几何、尺寸、构造操作与部件关系。 |
| Text-to-3D | 文本到 3D | 输入描述性或参数化文本，输出单部件 3D 程序。 |
| Image-to-3D | 图像到 3D | 输入单张渲染图，输出多部件对象。 |
| Assembly-3D | 装配体 3D | 输入图像、装配级和部件级文本，输出完整装配体。 |
| Geometry bucket / Geo | 几何保真度桶 | 由 CD、F-score、NC、IoU 等几何指标汇总。 |
| Topology bucket / Topo | 拓扑质量桶 | 由 NoOE、InvN、NM 等 mesh 拓扑指标汇总。 |
| Judge bucket | MLLM 评审桶 | 由 QA-S、QA-P 或 J-Sem/J-Geo/J-Aes 等 MLLM 评审指标汇总。 |
| Part bucket | 部件结构桶 | Assembly-3D 特有，关注 PartMatchF1 和 PartFS。 |
| Valid | 可执行有效率 | 生成程序可编译、执行并渲染成功的比例。 |
| CD | Chamfer Distance | 几何距离，越低越好。 |
| IoU / IoUC / IoUV | 交并比 | 单部件用 CSG IoU，装配任务用 voxel IoU；越高越好。 |
| NoOE | 无开放边分数 | no-open-edge score，衡量闭合表面比例；越高越好。 |
| InvN / NM | 反向法线 / 非流形边比例 | 拓扑错误指标；越低越好。 |
| QA-S / QA-P | 语义 QA / 参数 QA | 根据文本 specification 自动构造的问题库。 |
| J-Sem / J-Geo / J-Aes | 语义 / 几何 / 美学视觉评审 | MLLM 从多视图渲染打分。 |
| PartMatchF1 / PartFS | 部件匹配 F1 / 部件形状分数 | 衡量预测部件数目、匹配关系和 per-part geometry。 |

## Abstract and benchmark headline

### Fig. 1. 三类任务上的模型总分对比

![Fig. 1](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/fig1.png)

**Caption:** Figure 1: Scores of different models across the three tasks in P3D-BENCH. The Score is the average of the four bucket scores (Geo, Topo, Judge, Part; §3.3), rescaled to 0-100; per-bucket results are reported in Tables 3a-3c.

**Caption[CN]:** 图 1：不同模型在 P3D-BENCH 三类任务上的分数。Score 是四个 bucket 分数（Geo、Topo、Judge、Part）的平均值并缩放到 0-100；各 bucket 结果见表 3a-3c。

**Reading note:** 这张图给出论文最重要的纵览：Text-to-3D 分数整体最高，Image-to-3D 明显下降，Assembly-3D 对多数模型最困难；GPT-5.5 与 Gemini 3.1 Pro 处于第一梯队。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Multimodal large language models can write code to produce complex programs as well as use programs to do 3D modeling, which opens up a new avenue for 3D generation powered by their priors, world knowledge and reasoning. Yet existing benchmarks rarely evaluate 3D modeling through code.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 多模态大语言模型既能写复杂程序，也能利用程序进行 3D 建模，这为由模型先验、世界知识和推理能力驱动的 3D 生成开辟了新路线。但现有基准很少从“通过代码进行 3D 建模”的角度评估这些能力。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Such modeling demands more than runnable code: from a text or visual specification, a model must generate a parametric 3D program that is geometrically precise, semantically aligned and assembly-consistent. P3D-BENCH evaluates parametric 3D generation through explicit dimensions, construction operations and part relations rather than only mesh appearance.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 这种建模不只是代码能跑：给定文本或视觉规格，模型需要生成一个几何精确、语义对齐、装配一致的参数化 3D 程序。P3D-BENCH 评估的是显式尺寸、构造操作和部件关系，而不仅是 mesh 外观。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Under a unified protocol, P3D-BENCH covers three task families—Text-to-3D, Image-to-3D and Assembly-3D—and scores each output for executability, geometric fidelity, topology, text-grounded constraints, multiview semantic alignment and part-level structure.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在统一协议下，P3D-BENCH 覆盖三类任务：Text-to-3D、Image-to-3D 和 Assembly-3D，并从可执行性、几何保真度、拓扑、文本约束、多视角语义对齐和部件级结构等方面评分。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The authors evaluate frontier MLLMs and text-only LLMs on 400 text cases, 400 image cases and 203 annotated assemblies, with domain-specific models as reference points. The results show that assemblies are hardest, global shape and semantics are easier than precise parametric geometry, and part-level modeling remains weak.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 作者在 400 个文本案例、400 个图像案例和 203 个带标注装配体上评估 frontier MLLMs 与 text-only LLMs，并把 domain-specific 模型作为参考。结果表明：装配体最难；恢复整体形状和语义身份比精确参数化几何容易；部件级建模仍然薄弱。

## 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> MLLMs can combine executable-code writing with visual shape reasoning. Given a text prompt or a reference image, a model such as GPT-5.5 can write CadQuery or Three.js code that executes into a target 3D object. Compared with mesh prediction, program generation is explicit and editable: dimensions, construction steps and part decomposition are written in code.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> MLLM 可以把可执行代码生成和视觉形状推理结合起来。给定文本提示或参考图，GPT-5.5 这类模型可以写出 CadQuery 或 Three.js 代码，并执行成目标 3D 对象。与直接预测 mesh 相比，生成程序是一种显式、可编辑表示：尺寸、构造步骤和部件分解都写在代码中。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> No existing benchmark evaluates parametric 3D generation as a whole. Code benchmarks test whether programs compile; spatial benchmarks test layout and object relations; text-to-3D benchmarks test visual quality. Parametric 3D generation requires these jointly: the program must compile, infer part structure and assembly relations, and produce visually plausible yet geometrically precise output.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 现有基准没有把参数化 3D 生成作为整体来评估。代码基准看程序是否编译，空间基准看布局和物体关系，text-to-3D 基准看生成形状的视觉质量。参数化 3D 生成则需要这些能力共同成立：程序要可编译，还要推断部件结构和装配关系，并生成视觉合理且几何精确的结果。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> P3D-BENCH contains three tasks. Text-to-3D gives a text description and asks for a single part. Image-to-3D gives a rendered image and asks for a multi-part object, requiring inference of hidden geometry and part layout. Assembly-3D adds assembly-level and part-level annotations and asks for the full assembly.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> P3D-BENCH 包含三类任务：Text-to-3D 给文本描述，要求生成单个部件；Image-to-3D 给单张渲染图，要求生成多部件对象，因此需要推断不可见几何和部件布局；Assembly-3D 进一步加入装配级和部件级标注，要求生成完整装配体。

### Fig. 2. P3D-BENCH 评估流程总览

![Fig. 2](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/fig2.png)

**Caption:** Figure 2: Overview of the P3D-BENCH evaluation. Given a task input—a text specification, a single image, or an image with assembly-level and part-level annotations—a model writes a program in one of four formats (JSON, OpenSCAD, CadQuery, Three.js). P3D-BENCH executes and renders each program, reports validity, and scores Geometry, Topology, Judge and Part.

**Caption[CN]:** 图 2：P3D-BENCH 评估流程总览。给定任务输入（文本规格、单张图像，或带装配/部件级标注的图像），模型用 JSON、OpenSCAD、CadQuery 或 Three.js 之一写程序。P3D-BENCH 执行并渲染程序，报告有效性，并从 Geometry、Topology、Judge 和 Part 四个维度打分。

**Reading note:** 这张图是整篇论文的主流程图：输入任务、模型类别、输出格式、执行渲染和四类评分 bucket 全部在一张图中。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span>
> - A unified benchmark with three tasks and four code formats under one execution-and-rendering protocol.
> - A new P3D-Dataset construction pipeline that filters, annotates and verifies Text2CAD and Fusion 360 sources into 400 text, 400 image and 203 assembly cases.
> - A structured evaluation protocol with Geo, Topo, Judge and Part scores beyond executable validity.
> - A broad evaluation of frontier MLLMs, text-only LLMs and domain-specific models, showing that plausible executable programs still fail to recover correct parametric geometry.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span>
> - 统一基准：三类任务、四种代码格式，并用同一套执行与渲染协议比较。
> - 新的 P3D-Dataset 构建流程：从 Text2CAD 和 Fusion 360 过滤、标注、验证出 400 个文本、400 个图像和 203 个装配体案例。
> - 结构化评估协议：在可执行有效性之外，提供 Geo、Topo、Judge、Part 四类评分。
> - 对 frontier MLLMs、text-only LLMs 和 domain-specific 模型进行广泛评估，揭示“可执行且看起来合理”的程序仍常常无法恢复正确参数化几何。

## 2. Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Most 3D generation produces visual geometry such as NeRFs, radiance fields, signed distance fields or meshes. Parametric 3D generation differs because it targets construction logic: operations, dimensions and part structure are explicit and editable.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 大多数 3D 生成输出的是视觉几何，例如 NeRF、radiance fields、signed distance fields 或 meshes。参数化 3D 生成不同：它面向的是构造逻辑，操作、尺寸和部件结构都是显式且可编辑的。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Recent work fine-tunes code LLMs or VLMs to produce executable CAD code, often CadQuery, and agentic loops increasingly draft, execute and revise CAD or Blender scripts under visual feedback. However, there is still no unified benchmark for general-purpose LLMs/MLLMs and domain-specific models across executable parametric correctness and structure.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 近期工作会微调 code LLM 或 VLM 来生成可执行 CAD 代码，常见格式是 CadQuery；agentic loops 也会在视觉反馈下起草、执行并修复 CAD 或 Blender 脚本。但仍缺少一个统一基准来同时评估 general-purpose LLM/MLLM 和 domain-specific 模型的可执行参数化正确性与结构恢复能力。

### Table 1. 代表性基准比较

![Table 1](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/table1.png)

**Caption:** Table 1: Comparison of representative benchmarks. The table compares task type, model type coverage, executability, parametric accuracy, spatial evaluation, assemblies and part-level structure.

**Caption[CN]:** 表 1：代表性基准比较。该表比较任务类型、模型类型覆盖、是否执行输出、是否评估参数准确性、空间关系、装配体和部件级结构。

**Reading note:** P3D-BENCH 的独特性在于同时覆盖 LLM/MLLM、domain-specific models、可执行 3D、参数检查、空间布局、装配体和部件级评分。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Prior 3D/code benchmarks verify pieces of the problem: executability, spatial reasoning, visual quality or CAD code similarity. Most do not explicitly check specified dimensions or correct part structure; several focus on CadQuery or single parts. P3D-BENCH evaluates multiple formats and includes multi-part assemblies with explicit part-level modeling.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 以往 3D/code 基准只覆盖问题的局部：可执行性、空间推理、视觉质量或 CAD 代码相似性。多数不会显式检查指定尺寸或正确部件结构；一些只关注 CadQuery 或单个部件。P3D-BENCH 则跨多种格式评估，并包含具有显式部件级建模的多部件装配体。

## 3. P3D-BENCH: tasks, dataset and evaluation

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Parametric 3D generation is formulated as code-based reconstruction from a condition c and target format phi. A policy writes a program f_pi = pi(c, phi), where phi is JSON, OpenSCAD, CadQuery or Three.js. A deterministic executor compiles, executes and renders the program into a 3D output.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文把参数化 3D 生成定义为从条件 c 和目标格式 phi 出发的基于代码的重建。策略模型写出程序 f_pi = pi(c, phi)，其中 phi 可以是 JSON、OpenSCAD、CadQuery 或 Three.js。确定性执行器负责编译、执行并渲染该程序为 3D 输出。

### Fig. 3. P3D-Dataset 构建流程

![Fig. 3](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/fig3.png)

**Caption:** Figure 3: Overview of our P3D-Dataset. The filter pipeline draws from Text2CAD and Fusion 360 Gallery, filters candidates with a review MLLM, removes near-duplicates, and samples Text-to-3D and Image-to-3D cases. The annotation pipeline then produces descriptive/parametric text specifications and assembly/part annotations, checked by a verification MLLM.

**Caption[CN]:** 图 3：P3D-Dataset 总览。过滤流程从 Text2CAD 和 Fusion 360 Gallery 取样，用 review MLLM 筛选、去近重复，并采样 Text-to-3D 与 Image-to-3D 案例。标注流程生成描述性/参数化文本规格以及装配/部件标注，并由 verification MLLM 检查。

**Reading note:** 重点看右侧 split：Text-to-3D 400 cases，Image-to-3D 400 cases，Assembly-3D 203 cases；这就是后续评测的样本基础。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> P3D-Dataset is built from two open CAD sources: Text2CAD v1.1 with 176,017 single-part sketch-extrude programs and Fusion 360 Gallery with 8,251 multi-part assemblies. The raw sources are not directly usable because they contain unevaluable, simple, near-duplicate or underspecified examples and lack required annotations.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> P3D-Dataset 来自两个开放 CAD 数据源：Text2CAD v1.1 包含 176,017 个单部件 sketch-extrude 程序，Fusion 360 Gallery 包含 8,251 个多部件装配体。原始数据不能直接作为基准，因为其中有不可评估、过简单、近重复或规格不足的样本，也缺少任务所需标注。

### Fig. 4. Text-to-3D 与 Image-to-3D 过滤后 400-case 集合

![Fig. 4](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/fig4.png)

**Caption:** Figure 4: The Text-to-3D and Image-to-3D 400-case filtered sets.

**Caption[CN]:** 图 4：Text-to-3D 与 Image-to-3D 过滤后各 400 个案例集合。

**Reading note:** 上半部展示 easy/medium/hard 复杂度样例；下半部展示类别分布。Text-to-3D 以 support mounting 为主，Image-to-3D 以 mechanical system 和 vehicle 等装配类对象为主。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Filtering keeps cases that are executable and renderable, visually interpretable, non-redundant and balanced across complexity. Deterministic checks remove unevaluable records; a review MLLM rejects ambiguous or non-reconstructable cases and labels category/complexity; DINOv2 render embeddings remove near-duplicates; complexity-balanced sampling yields 400 text and 400 image cases.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 过滤阶段保留可执行、可渲染、视觉可解释、非冗余且复杂度均衡的案例。确定性检查移除不可评估记录；review MLLM 剔除模糊或不可重建案例并标注类别/复杂度；DINOv2 渲染嵌入用于去近重复；复杂度均衡采样得到 400 个文本和 400 个图像案例。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Annotation supplies the task-specific inputs missing from the raw sources. Text-to-3D gets both descriptive and parametric specifications. Image-to-3D/Assembly-3D first label parts, then create assembly-level descriptions, and a verification MLLM checks consistency and render alignment. The final Assembly-3D set has 203 annotated cases.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 标注阶段补全原始数据缺失的任务输入。Text-to-3D 同时获得 descriptive specification 和 parametric specification。Image-to-3D/Assembly-3D 先标注部件，再生成装配级描述，并由 verification MLLM 检查一致性和渲染对齐。最终 Assembly-3D 有 203 个带标注案例。

### Fig. 5. Judge bucket 指标流程

![Fig. 5](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/fig5.png)

**Caption:** Figure 5: Overview of the Judge bucket metrics. The Judge bucket combines QA metrics and visual Judge metrics. QA-S and QA-P are derived from specifications, while J-Sem/J-Geo/J-Aes score rendered views directly.

**Caption[CN]:** 图 5：Judge bucket 指标总览。Judge bucket 结合 QA 指标和 visual Judge 指标。QA-S 与 QA-P 来自文本规格问题库，J-Sem/J-Geo/J-Aes 直接对渲染视图评分。

**Reading note:** Judge bucket 的作用是弥补纯几何/拓扑指标不足：它看模型是否满足语义与参数约束。

### Fig. 6. Assembly-3D Part bucket 指标流程

![Fig. 6](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/fig6.png)

**Caption:** Figure 6: Overview of the Assembly-3D Part bucket metrics. Part scoring decomposes predicted assemblies into parts, applies a fidelity gate, deduplicates and pose-aligns parts, and computes PartFS and PartMatchF1.

**Caption[CN]:** 图 6：Assembly-3D Part bucket 指标总览。Part scoring 将预测装配体分解为部件，通过 fidelity gate，去重并对齐姿态，然后计算 PartFS 和 PartMatchF1。

**Reading note:** 这张图解释了为什么 Assembly-3D 比 Image-to-3D 更难：不仅要整体像，还要可分解为正确的部件集合。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> P3D-BENCH compiles each generated program, exports a mesh and aligns it to the ground truth before scoring. Valid is reported separately, while downstream sub-metrics are grouped into four buckets: Geometry, Topology, Judge and Part. Failed Valid checks receive worst downstream values.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> P3D-BENCH 会编译每个生成程序、导出 mesh，并在评分前与 ground truth 对齐。Valid 单独报告；下游指标分为 Geometry、Topology、Judge 和 Part 四个 bucket。未通过 Valid 的预测在下游指标上取最差值。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Geometry uses CD, F-scores, normal consistency and IoU; Topology uses NoOE, InvN and NM. Judge uses QA banks for text-based semantic/parametric constraints and visual scores for semantic, geometric and aesthetic alignment. Part metrics evaluate matched part shape and part-count recovery through PartFS and PartMatchF1.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> Geometry 使用 CD、F-scores、normal consistency 和 IoU；Topology 使用 NoOE、InvN 与 NM。Judge 用 QA banks 检查文本语义/参数约束，并用视觉评分衡量语义、几何和美学对齐。Part 指标通过 PartFS 和 PartMatchF1 评估匹配部件形状与部件数量恢复。

## 4. Experiments

### Table 2. 被评估模型列表

![Table 2](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/table2.png)

**Caption:** Table 2: Models evaluated in P3D-BENCH, grouped by model type. Size is reported as total parameters with active parameters for MoE; domain-specific baselines keep their native I/O contracts.

**Caption[CN]:** 表 2：P3D-BENCH 中被评估的模型，按模型类型分组。MoE 模型报告总参数和每 token 激活参数；domain-specific baselines 使用其原生输入/输出协议。

**Reading note:** 模型覆盖 8 个 multimodal LLM、3 个 text-only LLM，以及 Text2CAD、CADRILLE、CAD-CODER 三个领域模型。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The evaluated general-purpose models include Claude Opus 4.6, Gemini 3.1 Pro, GPT-5.5, Qwen3.6-Plus, GLM-5.1/5V Turbo, Doubao Seed 2.0 Pro, Kimi K2.6, DeepSeek V4 Pro and Xiaomi MiMo models. Text-only models are only run on Text-to-3D. Domain-specific models are run from released checkpoints under original I/O contracts.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 评估的通用模型包括 Claude Opus 4.6、Gemini 3.1 Pro、GPT-5.5、Qwen3.6-Plus、GLM-5.1/5V Turbo、Doubao Seed 2.0 Pro、Kimi K2.6、DeepSeek V4 Pro 和 Xiaomi MiMo 系列。text-only 模型只跑 Text-to-3D。domain-specific 模型用公开 checkpoint，并保持原始 I/O 协议。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The tasks use seven task-format combinations. Text-to-3D uses minimal JSON and OpenSCAD; Image-to-3D uses OpenSCAD, CadQuery and Three.js; Assembly-3D uses OpenSCAD and CadQuery because Three.js triangulated meshes are difficult to decompose into per-part solids.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 三类任务共形成七种 task-format 组合。Text-to-3D 使用 minimal JSON 和 OpenSCAD；Image-to-3D 使用 OpenSCAD、CadQuery 和 Three.js；Assembly-3D 使用 OpenSCAD 和 CadQuery，因为 Three.js 的三角网格难以分解为逐部件实体。

### Table 3. P3D-BENCH 主结果表

![Table 3](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/table3.png)

**Caption:** Table 3: P3D-BENCH per-task results by output format, with cross-format averages. Metrics include Valid, Geo, Topo, Judge and Part when applicable.

**Caption[CN]:** 表 3：P3D-BENCH 按任务和输出格式的主结果，并给出跨格式平均。指标包括 Valid、Geo、Topo、Judge，以及 Assembly-3D 中的 Part。

**Reading note:** 主结论：GPT-5.5/Gemini 3.1 Pro 领先；Assembly-3D 明显更难；OpenSCAD 整体更稳；domain-specific 模型即使在原生任务/格式上也落后于强通用模型。

### Fig. 7. 三类任务的 OpenSCAD 定性重建

![Fig. 7](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/fig7.png)

**Caption:** Figure 7: Qualitative OpenSCAD reconstructions across the three P3D-BENCH tasks for six representative models. Two cases per task group are shown, and each cell prints per-case scores above the rendered output.

**Caption[CN]:** 图 7：六个代表性模型在三类 P3D-BENCH 任务上的 OpenSCAD 定性重建。每个任务组展示两个案例，每个模型格子上方打印该案例的分数。

**Reading note:** 这张图能直观看到同一输入下不同模型的结构错误：有些输出语义像，但几何/部件明显错。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Across tasks, general-purpose models fall into roughly three tiers: GPT-5.5 and Gemini 3.1 Pro lead; Claude Opus 4.6 and Kimi K2.6 form a second tier; GLM, DeepSeek, Qwen, MiMo and Doubao form the third. Domain-specific models fall behind even on their native tasks and formats.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 跨任务来看，通用模型大致分为三档：GPT-5.5 与 Gemini 3.1 Pro 领先；Claude Opus 4.6 与 Kimi K2.6 是第二梯队；GLM、DeepSeek、Qwen、MiMo 和 Doubao 构成第三梯队。domain-specific 模型即使在原生任务和格式上也落后。

### Fig. 8. 跨模型 bucket 分布与 GPT-5.5 跨格式分数

![Fig. 8](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/fig8.png)

**Caption:** Figure 8: Per-task cross-model bucket score distributions and GPT-5.5 cross-format bucket scores.

**Caption[CN]:** 图 8：各任务跨模型 bucket 分数分布，以及 GPT-5.5 在不同格式上的 bucket 分数。

**Reading note:** 最重要的趋势是任务越复杂，模型间差距越大；OpenSCAD 在 GPT-5.5 上整体最均衡，JSON 在装配任务上弱，Three.js 在拓扑/部件上吃亏。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> OpenSCAD is the strongest output format overall: it is balanced across buckets and avoids clear weaknesses. JSON is weakest for assembly tasks. CadQuery and Three.js are close to OpenSCAD on Geo/Judge, but CadQuery has more invalid programs and Three.js triangulated meshes score poorly on Topology and Part.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> OpenSCAD 是整体最强输出格式：各 bucket 较均衡，没有明显短板。JSON 在装配任务上最弱。CadQuery 和 Three.js 在 Geo/Judge 上接近 OpenSCAD，但 CadQuery 更容易出现无效程序，Three.js 的三角网格在 Topology 和 Part 上得分较差。

### Fig. 9. Judge bucket 子指标细节

![Fig. 9](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/fig9.png)

**Caption:** Figure 9: Judge bucket details. It reports GPT-5.5 Judge submetric scores across tasks and output formats, plus qualitative cases with QA/Judge explanations.

**Caption[CN]:** 图 9：Judge bucket 细节。图中报告 GPT-5.5 在不同任务和格式上的 Judge 子指标，并展示带 QA/Judge 解释的定性案例。

**Reading note:** 核心观察：J-Sem 明显高于 J-Geo，说明模型常能认出对象并生成语义合理形状，但精确几何对齐仍差。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For GPT-5.5, parametric QA-P is generally below QA-S, so recovering exact parameters is harder than matching part semantics. In assembly tasks, J-Sem stays around 0.79-0.84 while J-Geo stays near 0.34-0.37: even the strongest model is semantically plausible but geometrically imprecise.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 对 GPT-5.5 来说，参数化 QA-P 通常低于 QA-S，说明恢复精确参数比匹配部件语义更难。在装配任务中，J-Sem 约为 0.79-0.84，而 J-Geo 仅约 0.34-0.37：即使最强模型也常常语义合理但几何不准。

### Fig. 10. Part bucket 子指标与部件匹配示例

![Fig. 10](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/fig10.png)

**Caption:** Figure 10: Part bucket details. Part submetrics are averaged across CadQuery and OpenSCAD, and qualitative examples show part-match results with per-part F-scores.

**Caption[CN]:** 图 10：Part bucket 细节。Part 子指标跨 CadQuery 和 OpenSCAD 平均，定性案例展示部件匹配结果和每个部件的 F-score。

**Reading note:** PartFS 最高约 0.73，PartMatchF1 最高也只有约 0.5，说明当前模型既难恢复正确部件几何，也难恢复正确部件数量。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> PartFS reaches only about 0.73 for the strongest model, and PartMatchF1 reaches only about 0.5. PartMatch precision and recall are both near 0.5, meaning roughly half of predicted parts and half of ground-truth parts form successful matches.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 最强模型的 PartFS 也只有约 0.73，PartMatchF1 约 0.5。PartMatch precision 和 recall 都接近 0.5，意味着预测部件中只有约一半能成功匹配，真实部件中也只有约一半被成功恢复。

### Fig. 11. 执行阶段无效输出分类

![Fig. 11](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/fig11.png)

**Caption:** Figure 11: Execute-stage invalid breakdown across tasks, output formats and models. Invalid outputs are classified as Syntax, Undefined Reference, Parameter or Geometry failures.

**Caption[CN]:** 图 11：跨任务、输出格式和模型的执行阶段无效输出分解。无效输出被分为 Syntax、Undefined Reference、Parameter 和 Geometry 四类。

**Reading note:** 失败模式按格式分化：Text-to-3D 中 JSON/OpenSCAD 多是 parser/syntax 问题；CadQuery 常在 parameter 或 geometry construction 阶段失败。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Invalid outputs are grouped into Syntax, Undefined Reference, Parameter and Geometry failures. Text-to-3D fails mostly on Syntax; CadQuery failures in Image-to-3D and Assembly-3D are dominated by malformed parameters and geometry-kernel construction failures.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 无效输出分为 Syntax、Undefined Reference、Parameter 和 Geometry 四类。Text-to-3D 主要失败在 Syntax；Image-to-3D 和 Assembly-3D 中 CadQuery 的失败主要来自参数错误和几何内核构造失败。

### Table 4. thinking-level effort 对 Image-to-3D 的影响

![Table 4](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/table4.png)

**Caption:** Table 4: Comparison of mean bucket scores by thinking-level effort on Image-to-3D for models with Non-think and Think Max runs.

**Caption[CN]:** 表 4：对具有 Non-think 和 Think Max 设置的模型，比较 thinking-level effort 对 Image-to-3D 平均 bucket 分数的影响。

**Reading note:** 更高 thinking effort 平均只带来 +0.034 的小幅提升；Kimi 提升最大，但 CadQuery 的 Valid% 在多数模型上反而下降。

### Table 5. 多轮 agentic workflow 与 single-shot 对比

![Table 5](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/table5.png)

**Caption:** Table 5: Multi-turn agentic workflow vs. single-shot generation on Image-to-3D/OpenSCAD.

**Caption[CN]:** 表 5：Image-to-3D/OpenSCAD 上 multi-turn agentic workflow 与 single-shot generation 对比。

**Reading note:** Gemini 3.1 Pro 多轮提升明显，GPT-5.5 几乎不变；关键差异是 Gemini 更愿意持续修订，GPT-5.5 常第一轮后停止。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Increasing thinking effort yields a modest mean gain of +0.034 across formats, with Kimi improving most and MiMo slightly regressing. Multi-turn feedback helps both evaluated models in principle, but Gemini 3.1 Pro improves more because it keeps revising longer, whereas GPT-5.5 often stops after one turn.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 提高 thinking effort 的平均收益只有 +0.034；Kimi 提升最大，MiMo 略有回退。多轮反馈原则上能帮助模型，但 Gemini 3.1 Pro 受益更明显，因为它会持续修订更久；GPT-5.5 往往一轮后就停止。

## 5. Conclusion and Future Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> P3D-BENCH exposes a consistent gap: programs that execute and look plausible often have imprecise parametric geometry and incorrect structure. Models recover coarse shape more reliably than precise dimensions, feature placement, topology and part structure; the strongest model reaches about 0.8 semantic alignment but only about 0.35 geometric alignment.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> P3D-BENCH 揭示了一个稳定差距：能够执行且看起来合理的程序，常常具有不精确的参数化几何和错误结构。模型更容易恢复粗略形状，而在精确尺寸、特征位置、拓扑和部件结构上仍不可靠；最强模型语义对齐约 0.8，但几何对齐只有约 0.35。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Future work will broaden data sources and output formats, including Blender and Unreal Engine, and evaluate coding agents such as Codex, Claude Code and Gemini CLI that iteratively write, execute and revise programs.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 未来工作会扩展数据源和输出格式，包括 Blender 与 Unreal Engine，并评估 Codex、Claude Code、Gemini CLI 等能迭代写、执行和修订程序的 coding agents。

## Appendix A-B. Dataset and evaluation implementation details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The appendix expands source preprocessing, filtering and annotation. Text2CAD records with missing programs, zero-depth extrusions or empty shapes are removed; a complexity score is built from sketch/extrude operations and face count. Fusion 360 assemblies enter the common filtering pipeline directly.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 附录扩展了源数据预处理、过滤和标注细节。Text2CAD 中缺失程序、零深度拉伸或空形状的记录会被移除；复杂度分数由 sketch/extrude 操作数量和 face count 构成。Fusion 360 装配体则直接进入通用过滤流程。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The review MLLM is Gemini 3.1 Pro, prompted with renders, geometric metadata and few-shot examples to assign semantic category, confidence and complexity tier. Near-duplicate removal uses DINOv2 render embeddings and a cosine-similarity threshold to remove the more redundant endpoint in highly similar pairs.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> review MLLM 使用 Gemini 3.1 Pro，以渲染图、几何元数据和 few-shot 示例为输入，标注语义类别、置信度和复杂度等级。近重复移除使用 DINOv2 渲染嵌入和余弦相似度阈值，在高度相似的样本对中移除更冗余的一端。

### Fig. 12. 两条数据源标注轨道示例

![Fig. 12](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/fig12.png)

**Caption:** Figure 12: Example annotations from the two data sources. Text2CAD examples are converted into descriptive and parametric specifications; Fusion 360 assembly examples are paired with assembly-level and part-level descriptions.

**Caption[CN]:** 图 12：两个数据源的标注示例。Text2CAD 示例被转换为描述性和参数化规格；Fusion 360 装配体示例配有装配级和部件级描述。

**Reading note:** 这张图很适合理解 P3D-BENCH 的输入不是随便写的 prompt，而是从几何记录和渲染图经 MLLM 标注、校验得到的任务规格。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Text-to-3D specifications are generated by parsing minimal JSON into a structured geometric record, passing it with the render to GPT-5.5, and validating every number and feature against the record. Fusion 360 part labels are produced by Claude Opus 4.6 from STEP geometry and renders; only assemblies with at most 20 deduplicated parts are kept.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Text-to-3D 规格通过把 minimal JSON 解析为结构化几何记录，再连同渲染图交给 GPT-5.5 生成，并用静态验证器检查文本中的每个数字和特征。Fusion 360 部件标签由 Claude Opus 4.6 根据 STEP 几何和渲染图生成；只保留最多 20 个去重部件的装配体。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Evaluation first aligns predicted and ground-truth meshes through normalization, translation, rotation and bounded scale/position refinement. Text-to-3D parametric specification preserves explicit scale and only applies translation/rotation. Single-part IoU uses CSG solids, whereas Image-to-3D and Assembly-3D use voxel IoU.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 评估先通过归一化、平移、旋转以及受限尺度/位置优化来对齐预测 mesh 与 ground truth mesh。Text-to-3D 参数规格保留显式尺度，只做平移/旋转。单部件 IoU 使用 CSG solids，而 Image-to-3D 和 Assembly-3D 使用 voxel IoU。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> QA banks are synthesized by Gemini 3.1 Pro: QA-S produces semantic multiple-choice questions and QA-P produces parametric questions about dimensions, counts, holes, arrays and placements. Visual Judge uses multiview renders only and rates semantic, geometric and aesthetic axes on a 1-10 scale.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> QA banks 由 Gemini 3.1 Pro 合成：QA-S 生成语义多选题，QA-P 生成关于尺寸、数量、孔、阵列和位置的参数问题。Visual Judge 只看多视角渲染图，在语义、几何和美学轴上以 1-10 分评分。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Assembly decomposition uses Claude Opus 4.6 to decompose a predicted whole assembly program into per-part programs. A fidelity gate keeps cases only when the reassembled decomposition matches the original prediction closely enough; Part metrics are measured only when this evaluator decomposition is faithful.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 装配体分解使用 Claude Opus 4.6 将预测的整体装配程序拆成逐部件程序。fidelity gate 只有在重新装配后的分解结果与原始预测足够接近时才保留该案例；Part 指标只在评估器分解可靠时测量。

## Appendix C-D. Additional analyses

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Assembly-3D adds richer part-level and assembly-level annotations, but this does not broadly improve executable geometry. On 203 shared cases and shared buckets, seven of eight models drop from Image-to-3D to Assembly-3D on the CadQuery/OpenSCAD average, with mean change -0.040.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Assembly-3D 增加了更丰富的部件级和装配级标注，但这并没有普遍提升可执行几何质量。在 203 个共享案例和共享 bucket 上，8 个模型中有 7 个从 Image-to-3D 到 Assembly-3D 的 CadQuery/OpenSCAD 平均分下降，平均变化为 -0.040。

### Table 6. 203 个共享案例上 Image-to-3D 与 Assembly-3D 对比

![Table 6](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/table6.png)

**Caption:** Table 6: Image-to-3D vs. Assembly-3D comparison on the 203 shared cases, using shared Geo/Topo/Judge buckets and CadQuery/OpenSCAD formats.

**Caption[CN]:** 表 6：在 203 个共享案例上比较 Image-to-3D 和 Assembly-3D，仅使用共享的 Geo/Topo/Judge bucket 以及 CadQuery/OpenSCAD 格式。

**Reading note:** 丰富 assembly 标注没有自动转化为更好几何；GPT-5.5 仅小幅正增益，Gemini 基本持平，其余多数下降。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The decomposition-fidelity diagnostic shows that once a predicted assembly compiles, the fixed decomposition step reproduces its union geometry tightly for nearly every model. The main separator is therefore whether the predicted assembly compiles, not whether the evaluator can later decompose it.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 分解保真度诊断显示：一旦预测装配体能够编译，固定分解步骤几乎对所有模型都能紧密复现其 union geometry。真正区分模型的是预测装配体是否能编译，而不是评估器之后能否分解它。

### Table 7. Assembly-3D 分解保真度诊断

![Table 7](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/table7.png)

**Caption:** Table 7: Decomposition fidelity diagnostic per evaluated model and output format, reporting Valid%, decomposition Chamfer Distance, decomposition voxel IoU and gate exclusions.

**Caption[CN]:** 表 7：按模型和输出格式给出的分解保真度诊断，报告 Valid%、分解 Chamfer Distance、分解 voxel IoU 和 gate 排除数量。

**Reading note:** OpenSCAD 在所有模型上 Valid% 更高（94%-99%），CadQuery 则从 22%-99% 差异很大；这再次说明格式/可执行性是关键变量。

### Fig. 13. 任务分数与完整运行成本关系

![Fig. 13](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/fig13.png)

**Caption:** Figure 13: Per-task quality score and cost to run the full task for each evaluated model. The x-axis is full-task USD cost on a log scale and the y-axis is the P3D-BENCH task score.

**Caption[CN]:** 图 13：每个模型在各任务上的质量分数与完整运行成本。横轴是完整任务运行成本（美元，对数尺度），纵轴是 P3D-BENCH 任务分数。

**Reading note:** 成本分析显示 GPT-5.5 分数最高但最贵，Gemini 3.1 Pro 在 grounded tasks 上接近 GPT-5.5 且成本约为其四分之一。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Cost-quality analysis shows three patterns: GPT-5.5 scores highest but is most expensive; Gemini 3.1 Pro tracks GPT-5.5 closely at much lower cost, especially on Image-to-3D and Assembly-3D; low-cost models show a clear quality gap, and the gap widens on grounded and assembly tasks.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 成本-质量分析显示三点：GPT-5.5 分数最高但最贵；Gemini 3.1 Pro 以显著更低成本接近 GPT-5.5，尤其在 Image-to-3D 和 Assembly-3D 上；低成本模型有明显质量差距，而且该差距在 grounded 和 assembly 任务上更大。

## Appendix E-F. Full metrics and qualitative galleries

### Table 8. 完整 Text-to-3D 指标

![Table 8](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/table8.png)

**Caption:** Table 8: Full Text-to-3D metrics on the 400-case set, including descriptive and parametric specifications across JSON and OpenSCAD.

**Caption[CN]:** 表 8：400-case Text-to-3D 集合上的完整指标，覆盖 JSON 和 OpenSCAD 下的描述性与参数化规格。

**Reading note:** OpenSCAD 在语义 QA 与几何/拓扑方面通常优于 JSON；Text2CAD 作为领域模型在原生 JSON 格式下仍落后于强通用模型。

### Table 9. 完整 Image-to-3D 子指标

![Table 9](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/table9.png)

**Caption:** Table 9: Image-to-3D sub-metrics composing Geo, Topo and Judge buckets across CadQuery, OpenSCAD and Three.js.

**Caption[CN]:** 表 9：Image-to-3D 中构成 Geo、Topo 和 Judge buckets 的子指标，覆盖 CadQuery、OpenSCAD 和 Three.js。

**Reading note:** 这个表可用于追查主表中的 bucket 分数来源，尤其是 J-Geo/J-Aes/J-Sem 与 Valid/NoOE 之间的差异。

### Table 10. 完整 Assembly-3D 子指标

![Table 10](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/assets/table10.png)

**Caption:** Table 10: Assembly-3D sub-metrics composing Geo, Topo, Judge and Part buckets across CadQuery and OpenSCAD.

**Caption[CN]:** 表 10：Assembly-3D 中构成 Geo、Topo、Judge 和 Part buckets 的子指标，覆盖 CadQuery 和 OpenSCAD。

**Reading note:** Assembly-3D 的关键在 PartMatch/PartFS：它能看出模型是否只是整体外观像，还是部件数量和每个部件几何都对。

### Fig. 14. Qualitative OpenSCAD gallery: Text-to-3D

![Fig. 14](fig14_text_to_3d.png)

**Caption:** Figure 14(a): Qualitative OpenSCAD outputs for Text-to-3D.

**Caption[CN]:** 图 14(a)：Text-to-3D 的 OpenSCAD 定性输出。

**Reading note:** 这是附录 qualitative gallery 的 Text-to-3D 部分，用于观察描述性/参数化输入下的模型差异。

### Fig. 15. Qualitative OpenSCAD gallery: Image-to-3D

![Fig. 15](fig14_image_to_3d.png)

**Caption:** Figure 14(b): Qualitative OpenSCAD outputs for Image-to-3D.

**Caption[CN]:** 图 14(b)：Image-to-3D 的 OpenSCAD 定性输出。

**Reading note:** 同一输入 render 下，不同模型在 visible-view fidelity 与全局几何上的错误非常直观。

### Fig. 16. Qualitative OpenSCAD gallery: Assembly-3D

![Fig. 16](fig14_assembly_3d.png)

**Caption:** Figure 14(c): Qualitative OpenSCAD outputs for Assembly-3D.

**Caption[CN]:** 图 14(c)：Assembly-3D 的 OpenSCAD 定性输出。

**Reading note:** 看 per-part recovery 和 inter-part placement error：这是 Assembly-3D 相比 Image-to-3D 的核心难点。

### Fig. 17. Text-to-3D 四种规格/格式组合定性样例

![Fig. 17](fig15_text_gallery.png)

**Caption:** Figure 15: Qualitative Text-to-3D outputs across specification and format combinations.

**Caption[CN]:** 图 15：跨规格与格式组合的 Text-to-3D 定性输出。

**Reading note:** 附录用固定目标部件和模型顺序，对比 descriptive/parametric 与 JSON/OpenSCAD 的效果。

### Fig. 18. Image-to-3D 三种格式定性样例

![Fig. 18](fig16_image_gallery.png)

**Caption:** Figure 16: Qualitative Image-to-3D outputs across CadQuery, OpenSCAD and Three.js.

**Caption[CN]:** 图 16：跨 CadQuery、OpenSCAD 和 Three.js 的 Image-to-3D 定性输出。

**Reading note:** 它展示同一输入案例在不同输出格式下的 visible-view fidelity 和全局几何错误。

### Fig. 19. Assembly-3D 两种格式定性样例

![Fig. 19](fig17_assembly_gallery.png)

**Caption:** Figure 17: Qualitative Assembly-3D outputs across CadQuery and OpenSCAD.

**Caption[CN]:** 图 17：跨 CadQuery 和 OpenSCAD 的 Assembly-3D 定性输出。

**Reading note:** 这是部件恢复和部件间位置错误的可视化对照，适合快速理解 Part bucket 为什么低。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Appendix E provides full submetric tables for all tasks and formats; Appendix F provides extended qualitative visualizations. These appendices are useful when diagnosing whether a model’s weakness comes from invalid execution, geometric misalignment, topology defects, judge disagreement or part-level mismatch.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 附录 E 提供所有任务和格式的完整子指标表；附录 F 提供扩展定性可视化。它们适合用于诊断模型弱点来自无效执行、几何错位、拓扑缺陷、Judge 不一致，还是部件级不匹配。

## References

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> References span parametric CAD generation, visual 3D generation, code benchmarks, spatial reasoning benchmarks, mesh metrics, and the evaluated model/system documents.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 参考文献覆盖参数化 CAD 生成、视觉 3D 生成、代码基准、空间推理基准、mesh 指标，以及被评估模型/系统文档。为避免扭曲书目信息，本文阅读笔记不逐条翻译参考文献；具体条目请查阅原 PDF 第 17-20 页。

## 阅读提示 / critical reading notes

- 这篇论文真正想测的不是“模型能不能画一个 3D 形状”，而是“模型能不能写出可执行、可编辑、结构正确的参数化 3D 程序”。
- 三个任务从单部件到多部件再到装配体逐步增加结构压力；Assembly-3D 的 Part bucket 是最能暴露模型弱点的部分。
- OpenSCAD 的稳定性值得注意：它在多任务/多模型上比 CadQuery 更少执行失败，也比 Three.js 更适合结构/部件评分。
- 一个很重要的结论是 semantic plausibility 与 geometric precision 脱钩：模型可能“知道这是个什么东西”，但无法恢复尺寸、孔位、部件数量和装配关系。
- 对你后续做 3D/code agent 评估有启发：single-shot MLLM 不是终点，论文未来工作也明确要测 Codex、Claude Code、Gemini CLI 这类能执行-反馈-修订的 coding agents。
