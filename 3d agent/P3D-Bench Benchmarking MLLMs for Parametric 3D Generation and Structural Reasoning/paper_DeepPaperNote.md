---
tags:
  - papers/3d-agent
  - papers/benchmark
  - papers/parametric-3d
aliases:
  - P3D-Bench
  - 参数化三维生成基准
date: 2026-06-10
doi: 10.48550/arXiv.2606.11152
arxiv_id: 2606.11152
---

# P3D-Bench: Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning

## 核心信息

- 标题: P3D-Bench: Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning
- 标题翻译: P3D-Bench：面向参数化三维生成与结构推理的多模态大语言模型基准
- 作者: Yikang Yang, Zhanpeng Hu, Youtian Lin, Mengqi Zhou, Jingxi Xu, Feihu Zhang, Jiaheng Liu, Yao Yao
- 机构: Nanjing University; Envision
- 发表时间: 2026-06-10
- 发表渠道: arXiv preprint
- DOI: 10.48550/arXiv.2606.11152
- arXiv: 2606.11152
- 论文链接: https://arxiv.org/abs/2606.11152
- 代码 / 项目: https://spatiaos.github.io/projects/P3D-Bench
- 数据 / 资源: P3D-Dataset，项目页提供数据与评测入口
- 论文类型: 参数化 3D 生成 benchmark / dataset

## 原文摘要翻译

多模态大语言模型既能编写代码来生成复杂程序，也能使用程序进行 3D 建模，这为借助模型先验、世界知识和推理能力驱动 3D 生成开辟了新路径。然而，现有基准很少评估通过代码进行 3D 建模的能力。这类建模所要求的不只是可运行代码：模型需要根据文本或视觉规格生成在几何上精确、语义上对齐且装配一致的参数化 3D 程序。

作者提出 P3D-Bench，一个面向参数化 3D 生成的基准。与 3D 网格不同，参数化 3D 程序会显式呈现尺寸、构造操作和部件关系，因此能够揭示模型是否恢复了设计结构，而不只是复制了外观。在统一协议下，P3D-Bench 覆盖 Text-to-3D、Image-to-3D 和 Assembly-3D 三类任务，并从可执行性、几何保真度、拓扑、文本约束、多视图语义对齐和部件级结构等方面评价输出。

作者在 400 个文本案例、400 个图像案例和 203 个带标注装配体上评估前沿 MLLM 与纯文本 LLM，并把领域专用模型作为参照。实验得到三项发现：第一，装配体是最困难的设置，模型仍难以把多个部件组成连贯结构；第二，模型通常能恢复目标的整体形状与语义身份，却难以重建输入所指定的精确参数化几何；第三，装配体的部件级建模仍然薄弱，模型既不能准确恢复每个部件的几何，也不能恢复正确的部件数量。P3D-Bench 因而为评价参数化 3D 生成中的精确几何与部件级结构提供了一个基准。

## 创新点

1. **把评价对象从渲染结果推进到可执行设计程序。** 输出必须先在 minimal JSON、OpenSCAD、CadQuery 或 Three.js 中执行，再转换为几何接受评价。这样，代码语法、几何构造、尺寸精度与结构错误能被分别观察。
2. **把单部件、单图重建和装配结构统一进一个协议。** Text-to-3D 检查文本到单部件程序，Image-to-3D 检查单图到多部件对象，Assembly-3D 再加入装配级与部件级文本约束，形成从外观重建到结构推理的难度阶梯。
3. **建立 P3D-Dataset 的筛选—去重—标注—验证流水线。** 论文从 176,017 个 Text2CAD 程序和 8,251 个 Fusion 360 装配体中得到 400/400/203 个案例，并为描述性、参数化与部件级任务补齐输入规格。
4. **用四类评分桶拆开“能跑、像、准、结构对”。** Geo、Topo、Judge、Part 分别覆盖几何、网格拓扑、文本/视觉约束和部件结构；这比单独使用 CD、代码通过率或视觉模型偏好更有诊断性。
5. **给 agentic 修订提供了受控基线。** 论文不仅测试单轮程序生成，还比较最大思考预算和最多十轮的渲染反馈修订，揭示反馈是否有效取决于模型会不会真正持续修改。

## 一句话总结

P3D-Bench 最有价值的结论不是“哪个 MLLM 排第一”，而是量化了一个很容易被漂亮渲染掩盖的事实：**程序可执行、对象语义像、尺寸几何准和部件结构正确，是四件不同的事。**

## 研究问题

参数化 3D 生成的目标不是输出一张“看起来像”的图，也不只是生成一段能编译的代码，而是恢复一个可编辑、可复用的设计程序。程序中的尺寸、布尔操作、构造顺序、部件数量和相对位置都应与输入约束一致。现有评价通常只覆盖其中一层：代码基准看通过率，空间基准看语言答案，文本到 3D 基准看视觉质量，CAD 基准又常只看单部件的几何相似。

论文因此把问题写成条件程序重建。给定任务条件 $c$ 和目标格式 $\phi$，模型策略 $\pi$ 生成程序

$$
f_{\pi}=\pi(c,\phi),
$$

再由格式对应的确定性执行器生成 3D 输出

$$
y_{\pi}=E_{\phi}(f_{\pi}).
$$

一个评测样本由条件、源程序和真实输出组成：

$$
x=(c,f^{\star},y^{\star}).
$$

其中，第二项是源程序，第三项是由它得到的真实几何与可用部件结构。真正要回答的问题是：通用大模型能否把文本或单视图中的空间知识落实成**可执行、精确、拓扑合理、部件一致**的三维程序？

![Table 1](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/images/page_004_fig_table_1.png)
*Table 1. P3D-Bench 与代码、空间推理、网格生成及 CAD 基准的覆盖范围比较；它同时覆盖执行、参数、空间、装配和部件级评价。*

## 数据与任务定义

### 三类任务与四种程序表示

| 任务 | 输入 | 目标结构 | 支持格式 | 主要难点 |
|---|---|---|---|---|
| Text-to-3D | 描述性或参数化文本 | 单部件 | minimal JSON、OpenSCAD | 把自然语言形状与显式尺寸转成构造操作 |
| Image-to-3D | 单张渲染图 | 多部件对象 | OpenSCAD、CadQuery、Three.js | 推断不可见几何、部件分解和空间布局 |
| Assembly-3D | 图像、装配级文本、部件级文本 | 完整装配体 | OpenSCAD、CadQuery | 同时满足部件身份、数量、几何和相对关系 |

![Figure 2](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/images/page_003_fig_figure_2.png)
*Fig. 2. P3D-Bench 的统一评测版图：任务输入、通用/领域模型、四种输出格式与四类质量 bucket。*

四种表示并不等价。minimal JSON 与 Text2CAD 的源表示最接近，但表达多部件装配体的能力有限；OpenSCAD 是较直接的 CSG 语言。
CadQuery 通过 Python API 与 OpenCascade 几何内核表达工业 CAD 操作。
Three.js 更接近三角网格与渲染对象，不天然保证封闭实体或干净的部件实体。

### 数据来源、筛选与标注

P3D-Dataset 的原始来源互补：Text2CAD v1.1 有 176,017 个单部件 sketch-extrude 程序，Fusion 360 Gallery 有 8,251 个多部件装配体。原数据不能直接作为基准，原因包括空形状、零深度拉伸、过于简单或近重复的零件、视角含混的装配体，以及缺少描述性、参数化和部件级文本。

![Figure 3](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/images/page_005_fig_figure_3.png)
*Fig. 3. P3D-Dataset 构建流程：确定性预处理、MLLM 复核、DINOv2 去近重复、复杂度平衡采样，以及文本/部件标注与验证。*

过滤阶段先删除不可执行或不可评价样本，再由 Gemini 3.1 Pro 结合渲染、面/边等几何元数据和少量示例判断语义类别、可信度与复杂度。
DINOv2 的渲染 CLS 特征用于去近重复，最后按易、中、难三个等级平衡采样。
Text-to-3D 的 400 个案例按复杂度分为 50/200/150，Image-to-3D 的 400 个案例为 80/160/160。

标注阶段中，GPT-5.5 根据 Text2CAD 的结构化几何记录和渲染生成描述性与参数化规格；数值和特征再由静态验证器核对。
Fusion 360 的唯一部件由 Claude Opus 4.6 根据 STEP 几何和渲染描述，装配级说明则结合部件文本、装配渲染、包围盒、孔和接触关系生成。
为控制上下文，只保留去重后不超过 20 个部件的装配体，最终得到 203 个 Assembly-3D 案例。

![Figure 12](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/images/page_022_fig_figure_12.png)
*Fig. 12. Text-to-3D 的描述性/参数化规格与 Assembly-3D 的装配级/部件级标注实例。*

数据分布仍偏机械设计：Text-to-3D 中支撑安装件占 67.2%，Image-to-3D 中机械系统占 33.2%、车辆占 15.2%。这有利于测 CAD 结构，却限制了结论向有机对象、室内场景和材质丰富资产的外推。

## 方法主线

### 机制流程

1. **生成并执行。** 模型根据输入和目标格式生成程序；格式执行器编译、运行并导出 mesh。不能执行的输出计入 Valid 失败，并在下游指标中取最差值。
2. **对齐并测几何/拓扑。** 预测网格经过归一化、平移、旋转和有界尺度/位置细化，以最小化双向 Chamfer 距离。Text-to-3D 参数化任务保留显式尺度，只做平移和旋转。
   Geo 汇总 CD、IoU、F-score 与 NC；Topo 汇总开边、翻转法线和非流形边。
3. **检查文本与视觉约束。** Judge 使用预生成的 QA-S/QA-P 问题库检查语义和参数约束。
   Gemini 3.1 Pro 只观察多视图渲染，并给出 J-Sem、J-Geo 和 J-Aes。
4. **拆解装配体并匹配部件。** Claude Opus 4.6 把有效装配程序分解为每个部件的程序；保真门验证重组后的联合几何没有被重新设计，再去重、姿态对齐并与真实部件做匈牙利匹配。

![Figure 5](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/images/page_007_fig_figure_5.png)
*Fig. 5. 评审评分同时包含规格驱动的 QA-S/QA-P 与多视图驱动的 J-Sem/J-Geo/J-Aes。*

### Part bucket 的关键公式

若预测部件数为 $m$，真实部件数为 $n$，成功匹配数为 $M$，则

$$
P=\frac{M}{m},\qquad R=\frac{M}{n},\qquad
\mathrm{PartMatchF1}=\frac{2PR}{P+R}.
$$

PartFS 对全部一对一匹配部件的局部 F-score 取均值。论文用真实部件包围盒对角线的 5% 作为匹配尺度，并以 $F_{\min}=0.7$ 判定成功匹配。
分解保真门只在 $D_{dec}>5\times10^{-4}$ 且 $IoU^V_{dec}<0.95$ 同时成立时拒绝该分解；这避免把分解模型自己的重设计错误算到被测模型头上。

![Figure 6](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/images/page_008_fig_figure_6.png)
*Fig. 6. Assembly-3D 的部件评价：程序分解、联合几何保真门、重复部件折叠、姿态对齐和一对一匹配。*

### 指标设计的一个重要细节

所有子指标先统一到 $[0,1]$ 且越高越好，再在评分桶内等权平均。无界的 Chamfer 距离用 $\max(0,1-CD/0.01)$ 截断归一化。
图像与装配任务的体素 IoU 只在预测表面封闭时计算。这个协议的优点是无效程序会受到明确惩罚。
代价是格式的执行难度会同时进入 Geo、Topo 与 Judge，因此不能把评分差异纯粹解释成“空间推理能力”。

### 多轮 agent 流程

额外实验从单轮输出出发，每一轮把参考图、当前代码和当前输出的多视图渲染重新交给模型，让它修改代码或停止，最多十轮。它仍是非常轻量的视觉反馈 agent：没有 API 文档检索、编译器错误定位、约束求解器或显式部件图。

> [!figure] Table 5. 多轮 agent 与单轮生成比较
> 建议位置：机制流程
> 放置原因：该表给出多轮反馈是否真正改善 Image-to-3D/OpenSCAD 的直接证据。
> 当前状态：自动候选裁图将表 4 的表体与表 5 的图注拼接在一起，替代裁图又混入下一段正文，无法安全插入；关键数值已在“思考预算与多轮反馈”中完整转录。

## 关键结果

### 主结果与强基线

![Figure 1](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/images/page_001_fig_figure_1.png)
*Fig. 1. 不同模型在三类任务上的总体得分；GPT-5.5 与 Gemini 3.1 Pro 处于第一梯队。*

| 模型 | Text-to-3D | Image-to-3D | Assembly-3D |
|---|---:|---:|---:|
| GPT-5.5 | 84.7 | 67.5 | 68.0 |
| Gemini 3.1 Pro | 83.5 | 66.7 | 65.9 |
| Claude Opus 4.6 | 83.1 | 62.0 | 60.0 |
| Kimi K2.6 | 79.7 | 59.2 | 55.2 |

通用模型大致形成三层：GPT-5.5/Gemini 领先，Claude/Kimi 居中，其余模型明显落后。
领域模型 Text2CAD、CADRILLE 和 CAD-CODER 即使在自己的原生输入输出格式上也没有超过前沿通用模型。但这不是同训练数据、参数规模和推理成本下的模型能力消融，只能说明“当前可用系统”的端到端表现。

![Table 2](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/images/page_009_fig_table_2.png)
*Table 2. 被测模型覆盖 8 个多模态通用模型、3 个纯文本模型和 3 个领域模型。*

![Table 3](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/images/page_010_fig_table_3.png)
*Table 3. 三类任务、各输出格式的 Geo、Topo、Judge、Part 与 Valid 主结果；此处使用完整三子表版本。*

图 1 的跨任务总分不能直接当成同构难度标尺，因为三类任务使用的评分桶数量不同。
更可靠的诊断来自各项分布：跨模型平均值从 Text-to-3D 参数任务的 Geo 0.67、Topo 0.98、Judge 0.73，下降到 Image-to-3D 的 0.46/0.84/0.35。
Assembly-3D 又降至 Geo 0.41、Topo 0.78、Judge 0.28、Part 0.47。任务越接近装配结构，模型差距也越大。

![Figure 8](page_012_fig_figure_8.png)
*Fig. 8. 跨任务评分分布与 GPT-5.5 的跨格式表现；OpenSCAD 最平衡，装配任务的 Judge 与 Part 明显偏低。*

### 语义像，不代表参数和几何准

最强模型的 J-Sem 在图像与装配任务上约为 0.79–0.84，而 J-Geo 只有约 0.34–0.37。
对参数化 Text-to-3D，CadQuery、OpenSCAD 和 Three.js 的 QA-P 平均约 0.84，低于 QA-S 的约 0.90。
加入参数细节后，语义 QA-S 又从描述规格的约 0.93 降到参数规格的约 0.86。模型需要同时维持大量尺寸、偏移和构造关系时，会牺牲整体形状语义。

JSON 是一个需要谨慎解释的例外：它的 QA-P 可能高于 QA-S，因为参数文本本来就是从 minimal JSON 派生，模型可以复制数值，却不一定构造出正确几何。这说明 QA 正确率本身也可能被表示同源性“抬高”。

![Figure 9](page_013_fig_figure_9.png)
*Fig. 9. Judge 子指标及案例：语义分高、几何分低的差距在定量与定性结果中同时出现。*

![Table 8](page_028_fig_table_8.png)
*Table 8. Text-to-3D 的完整子指标；描述性语义、参数 QA 和真实几何精度之间并不同步。*

![Table 9](page_029_fig_table_9.png)
*Table 9. Image-to-3D 在 CadQuery、OpenSCAD、Three.js 中的几何、拓扑与 Judge 子指标。*

### 部件结构仍是最硬的短板

GPT-5.5 的 Assembly-3D PartFS 约 0.73，但 PartMatchF1 只有约 0.5；精度和召回也都在 0.5 左右。也就是说，即使成功匹配到的部件形状尚可，预测部件集合仍会同时漏掉真实部件并产生错误部件。部件数量、身份与几何没有被一个整体渲染分数可靠捕获。

![Table 10](page_030_fig_table_10.png)
*Table 10. Assembly-3D 的几何、拓扑、Judge 和 Part 子指标；候选图覆盖 CadQuery 子表，完整 OpenSCAD 数值同时由正文证据核对。*

分解 MLLM 并不是主要排名来源。只要预测程序能运行，重组部件通常能较好保持原联合几何；Table 7 中多数 $D_{dec}$ 处于 $10^{-4}$–$10^{-3}$，差异远小于 Valid 的 22%–99%。因此模型间最显著的差别首先是程序能否执行，其次才是分解保真度。

![Table 7](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/images/page_026_fig_table_7.png)
*Table 7. 分解保真度诊断；此处使用去除后续 Cost-quality 正文污染的独立表格裁图。*

### 输出格式决定失败位置

OpenSCAD 是最稳健、最均衡的表示。
CadQuery 在强模型上很有表达力，但弱模型常在 Python API 参数、布尔运算和几何内核阶段失败。
Three.js 的三角网格能得到不错的整体几何和语义，却不保证封闭、流形或可分解实体，因此 Topo 与 Part 受损。

无效输出的类别进一步支持这一点：Text-to-3D 的失败主要是语法错误，描述规格占 73%，参数规格占 50%。
图像与装配任务的 CadQuery 失败中，参数错误分别约占 55% 和 54%，几何构造错误分别约占 24% 和 27%。
这不是单纯“不会写代码”，而是错误会沿表示链向后移动：简单格式先死在解析，复杂 CAD API 更容易死在参数语义与几何构造。

![Figure 11](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/images/page_015_fig_figure_11.png)
*Fig. 11. 不同任务和格式的执行失败类别：Syntax、Undefined Reference、Parameter 与 Geometry。*

### 思考预算与多轮反馈

![Table 4](page_016_fig_table_4.png)
*Table 4. 最大思考预算相对无显式思考预算的变化；平均收益较小，且 CadQuery 有效率可能下降。*

最大思考预算在五个模型、三个格式上的平均收益只有 +0.034。
Kimi K2.6 提升最大，为 +0.106；MiMo v2 Omni 略降 -0.006。
更长推理并不自动带来更好的 CAD 程序：四个模型在 CadQuery 上的有效率反而下降，额外推理可能生成更复杂、也更脆弱的 API 调用。

| 模型 | 单轮 Avg | 多轮 Avg | 平均轮数 | 解释 |
|---|---:|---:|---:|---|
| GPT-5.5 | 0.720 | 0.722 | 1.5 | 62% 第一轮后停止，几乎没有利用反馈 |
| Gemini 3.1 Pro | 0.715 | 0.745 | 7.9 | 51% 达到十轮上限，持续修订带来明显收益 |

这不是“Gemini 更会看反馈”这么简单，而是说明 agent 的停止策略本身就是能力的一部分。给模型多轮预算，如果它过早停止，预算等于不存在；如果它机械地迭代到上限，也可能只增加成本。更强的 CAD agent 应把编译错误、约束违反和部件匹配反馈结构化，而不是只回传渲染图。

### 更多装配文本没有自动变成更好几何

在同一 203 个案例和 CadQuery/OpenSCAD 格式上，论文只比较 Geo、Topo、Judge 三项共享评分。
Assembly-3D 相比 Image-to-3D 的跨格式平均变化为 -0.040。八个模型中七个下降，只有 GPT-5.5 小幅上升 +0.008；GLM 5V Turbo 在 CadQuery 上下降 -0.206。

![Table 6](page_025_fig_table_6.png)
*Table 6. 共享案例上的 Image-to-3D 与 Assembly-3D 对照；更多部件文本通常没有改善可执行几何。*

这组结果很关键：Assembly-3D 的困难并不只是“输入信息不够”，而是模型不会把部件描述、数量和相互关系绑定到同一程序结构中。结构化上下文越多，约束冲突、指代绑定与程序规划的负担也越大。

### 成本—质量不是小问题

![Figure 13](3d%20agent/P3D-Bench%20Benchmarking%20MLLMs%20for%20Parametric%203D%20Generation%20and%20Structural%20Reasoning/images/page_027_fig_figure_13.png)
*Fig. 13. 三类任务的质量—完整任务成本曲线；横轴为对数尺度。*

GPT-5.5 在三类任务上均最高，但也是最昂贵的模型。
Gemini 3.1 Pro 在 Image-to-3D 与 Assembly-3D 上只低 0.008 与 0.022，完整任务成本却约为 GPT-5.5 的四分之一。
这意味着部署或大规模基准测试时，模型排序之外还需要报告边际质量收益对应的实际执行成本。

## 深度分析

### 真正贡献是什么

这篇论文真正新颖的不是某个单独指标，而是把**程序、几何、渲染与部件**放进同一条可审计链。以往工作容易在两个方向上失真：一类只看程序是否运行，把“合法但错误”的 CAD 当成功；另一类只看渲染是否像，把尺寸、孔位、部件数量和相对关系错误藏在视觉相似之后。P3D-Bench 通过源程序和真实几何把这两类盲点连接起来。

对三维代理研究来说，它也提供了比语言空间问答更接近最终任务的评价：模型必须把空间推理落到可执行构造操作，而不是只说出“左边、上方、相交”之类关系。
它在本地文献图谱中的位置是：**程序化三维生成与结构推理基准**，可以作为 Code2Worlds、CAD 代理、Blender 代理和几何约束代理的下游诊断台。

### 为什么结果会呈现“语义强、几何弱”

MLLM 的世界知识足以从文字或图像识别“摩托车、支架、桶、齿轮”等类别，并生成视觉上合理的粗轮廓；精确 CAD 则要求跨多步操作维护同一坐标系、尺度、对称性、厚度、孔位和布尔关系。任何早期误差都会传递到后续构造。渲染语义可以容忍这些局部偏差，而参数化设计不能。

装配体进一步引入集合与关系问题：模型不只要生成每个部件，还要决定哪些部件重复、数量多少、怎样接触、怎样对齐，以及如何在程序中保持可分解结构。PartMatchF1 约 0.5 正好说明瓶颈不是最后的渲染，而是前面的结构规划与实体身份维护。

### 容易误读的地方

1. **Figure 1 的 Assembly 总分略高于 Image，并不否定装配更难。** 两个总分汇总的 bucket 不同；应看控制后的共享案例与各 bucket 分布，那里 Assembly 的平均下降更清楚。
2. **OpenSCAD 第一不等于它是最强工业 CAD 表示。** 它的语法和 CSG 结构更容易被当前模型稳定生成；CadQuery 表达力更强，也引入更多 API 与内核失败面。
3. **通用模型超过领域模型不等于领域训练无价值。** 这是当前发布系统的端到端比较，训练数据、模型规模、提示、推理预算和成本均未控制。
4. **Judge 高不等于尺寸正确。** J-Sem/J-Aes 更接近渲染观感；QA-P 和真实几何指标才更接近参数遵循。
5. **Part bucket 不是完全模型无关。** 它依赖 Claude Opus 4.6 的程序分解；论文用保真门隔离了明显重设计，但仍不能消除所有分解偏差。

### 评测器与标注器的耦合风险

论文大量使用闭源多模态模型：Gemini 3.1 Pro 参与数据复核、QA 生成和评分。
Claude Opus 4.6 参与部件标注与预测程序分解，GPT-5.5 参与 Text-to-3D 标注；这些模型又出现在排行榜中。
这会形成潜在的“方言对齐”或自偏好：被测模型可能更容易理解由同族模型生成的规格，评审模型也可能偏好相近的视觉或程序习惯。

论文用静态验证、几何指标和分解保真门减轻了问题，但没有彻底回答跨评审器稳定性。最有价值的补充实验应是：人工审计子集、多评审器投票、开源评审器复现，以及把标注模型和被测模型完全隔离。

### 复现注意点

- 必须固定每个闭源模型的具体版本、日期、温度、思考预算、生成长度上限、停止条件与失败重试策略；该论文的模型与价格均高度时效化。
- 四种执行环境要分别固定：minimal JSON 解释器、OpenSCAD 2021.01、CadQuery 2.7.0 与 Three.js 0.184.0。
  同时记录 OpenCascade、网格导出和渲染版本。
- 需要公开任务提示、规范生成提示、QA 生成/回答提示、Judge 提示、多视图相机、对齐流程、最差值填充规则和 bucket 归一化常数。
- DINOv2 去重需要复现候选渲染、CLS 特征、相似度阈值 $\tau$ 和贪心删除顺序；否则 400-case split 不能精确重建。
- Part 评价需要复现分解提示、24 个旋转搜索、几何指纹去重、$\tau_g=0.05\,\mathrm{diag}_g$、$F_{\min}=0.7$ 与保真门。
- 单图任务存在多解。复现时应区分“与唯一真实程序不一致”和“几何上合理但设计不同”，最好额外做人工合理性审计。

## 局限

1. **数据域窄。** 两个源数据集都偏机械 CAD，且 Text-to-3D 类别极不均衡；结论不能直接扩展到有机对象、完整场景、材质、动画和关节功能。
2. **自动标注与自动评价高度依赖闭源模型。** 排名可能随 API 版本变化，且标注器、评审器与被测模型之间存在同源偏置。
3. **唯一真实几何低估单视图多解。** Image-to-3D 的不可见部分可能有多个合理构造，Chamfer/IoU 会惩罚与数据集真实程序不同但工程上可行的解。
4. **格式比较混合了语言与工具链难度。** CadQuery 的低分既可能来自空间推理，也可能来自 Python 语法、API 记忆、依赖、OpenCascade 布尔失败和导出错误。
5. **Part 分母不完全固定。** 无效预测取最差值，但有效预测若分解失败或未过保真门会从 Part 均值中排除；不同模型被排除的案例数不同。
6. **多轮 agent 设置过于简单。** 最多十轮渲染反馈不能代表拥有终端、文档检索、单元测试、几何约束与长期记忆的真实 coding agent。
7. **成本与模型结论易过时。** 论文使用 2026 年的前沿闭源模型与定价，未来模型更新后排行榜和成本—质量前沿都会移动。
8. **没有检验功能与制造性。** 精确几何和部件结构仍不等同于可制造、可装配、可运动或满足工程公差。

## 我的笔记

这篇适合被当作 3D agent 研究中的“评价骨架”，而不是又一个排行榜。后续如果做 Code2Worlds、Blender agent 或 CAD agent，我会直接复用它的四层拆分：

1. **Execution 层：** 程序能否运行、是否稳定导出。
2. **Geometry 层：** 整体表面、体积、尺度和局部特征是否一致。
3. **Structure 层：** 对象/部件数量、身份、层级、接触与相对姿态是否正确。
4. **Constraint 层：** 文本参数、用户意图、功能与可编辑性是否被满足。

我尤其认同两个实验。第一，203 个共享案例说明“给更多结构化文字”并不会自动改善结构生成，信息利用本身需要显式绑定机制；这与很多代理工作中把场景图或记忆直接塞进上下文却不验证其使用方式的问题相同。
第二，Gemini 与 GPT-5.5 的多轮差异说明停止策略是代理性能的一部分，不能只报告“最多迭代十轮”。

下一步最自然的研究方向不是继续扩大单次 MLLM，而是构建一个受约束的闭环：先把输入解析成显式部件图与参数表，再生成程序，通过编译器、几何内核和部件匹配器返回结构化错误，最后只修改受影响的局部程序。这样的 agent 才有机会同时提升 Valid、J-Geo 与 PartMatchF1，而不是只让渲染越来越像。

如果要把 P3D-Bench 扩展到更广义的 3D Agent，我会增加三类指标：关节/自由度与接触功能、跨视图和交互后的状态一致性、以及编辑请求后的参数局部性。它们能把“静态 CAD 结构正确”推进到“可交互世界模型正确”。

## 引用

- Yang, Y., Hu, Z., Lin, Y., Zhou, M., Xu, J., Zhang, F., Liu, J., & Yao, Y. (2026). *P3D-Bench: Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning*. arXiv:2606.11152. https://arxiv.org/abs/2606.11152
- DOI: https://doi.org/10.48550/arXiv.2606.11152
- 项目页: https://spatiaos.github.io/projects/P3D-Bench
- Zotero 条目: `RTBIM5RW`
- 本地 PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/6IK9XKXJ/Yang 等 - 2026 - P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning.pdf`
