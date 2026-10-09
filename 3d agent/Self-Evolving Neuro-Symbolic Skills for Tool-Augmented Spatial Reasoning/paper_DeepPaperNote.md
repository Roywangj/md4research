# Self-Evolving Neuro-Symbolic Skills for Tool-Augmented Spatial Reasoning

> **WJ DeepPaperNote｜基于原始 PDF 的精读记录**  
> Source: Shi-Yu Tian, Zhuo-Xia Wang, Xuan-Yi Zhu, Zhi Zhou, Xinwei Yang, Kun-Yang Yu, Ming Yang, Yang Chen, Yu-Feng Li. *Self-Evolving Neuro-Symbolic Skills for Tool-Augmented Spatial Reasoning*. arXiv:2608.07955v1, 8 Aug 2026.  
> PDF used: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/S7EUAMC6/Tian 等 - 2026 - Self-Evolving Neuro-Symbolic Skills for Tool-Augmented Spatial Reasoning.pdf` (25 pages).

## 核心信息

这篇工作的真正贡献不是“让 LVLM 多调用几个视觉工具”，而是把工具增强空间推理中最容易失控的两件事拆开并固化：**Tool-Use Skill** 管理“先收集什么证据、工具按什么依赖顺序执行”，**Geometry Skill** 管理“如何在明确参照系和输入契约下做可验证的坐标变换、距离计算和选项判定”。NeSy-Spatial 用带类型输入/输出和局部 verifier 的原子指令表达二者，再把它们组织成可中断的高层技能。

推理阶段是 Skill Retrieval → Action Selection → Tool/Code Execution → State Update 的闭环；演化阶段以 test-then-update 的在线轨迹为输入，做 trajectory analysis、skill fusion 和 skill pruning。这样，失败轨迹不会只变成“答案错了”的标签，而可以暴露缺失的 grounding、错误的执行依赖、硬编码选项解析或无效几何证据。

在 MMSI、MindCube、OmniSpatial 三个基准和 GPT-5.4、Gemini 2.5 Pro 两个 LVLM 上，NeSy-Spatial 的总体准确率在 6 个设置中 5 个最佳；GPT-5.4 的平均 FTCS/Python success 为 94.56/95.45，Gemini 2.5 Pro 为 88.67/96.21（PDF pp. 5–7）。但证据边界仍很清楚：实验依赖固定工具接口、封闭模型和三个空间基准，没有证明跨工具、开放场景或真实机器人部署中的迁移。

## 原文摘要翻译

大型视觉语言模型在多模态推理方面已经取得很强的性能，但在同时要求精确空间感知与细粒度几何计算的空间任务上仍不可靠。工具增强是自然的解决方案；然而，已有方法要么从头规划工具调用而没有显式依赖约束，要么依赖固定流水线，因而会冗余并且难以跨空间任务泛化。

NeSy-Spatial 是一个用于自演化空间技能的神经符号框架。它把工具交互和几何操作抽象为带类型、可执行的原子指令，并组合为两种互补技能：组织工具执行的 Tool-Use Skills，以及进行结构化几何推理的 Geometry Skills。推理时，系统以闭环方式检索和执行相关技能；演化时，系统分析缓冲的成功和失败轨迹，修订技能结构，并剪除不可靠或不活跃条目。三个空间推理基准的实验表明，NeSy-Spatial 能同时提升推理准确率和工具使用的精确性（PDF p. 1）。

## 创新点

1. **统一而不混淆工具与几何。** 原子指令统一采用 typed executable operation + local verifier 的形式，但 Tool-Use Skill 是控制器可见的证据收集图，Geometry Skill 是 Python 内部可复用计算内核。
2. **把依赖变成结构。** 高层技能不是一段自然语言建议，而是节点、依赖边和实例化上下文组成的结构；Tool-Use 的边表达工具执行依赖，Geometry 的边表达数据依赖。
3. **让失败具有可学习结构。** 轨迹分析同时寻找成功的重复子链和失败的局部转移，融合时可以添加缺失后缀、删除冗余依赖或替换受影响子图，而不是简单重写整个 workflow。
4. **在线演化有保护机制。** 预测先于标签揭示；技能库只在 episode 之间更新；调用支持、错误率、非活跃年龄和 tenure-aware 阈值共同决定剪枝。
5. **两阶段检索控制上下文。** 第一阶段只看紧凑 docstring/结构提示，第二阶段只展开被选技能的完整定义、绑定和停止条件，降低把整库塞给 LVLM 的成本（Supplementary D）。

## 一句话总结

NeSy-Spatial 把“工具调用顺序”和“工具输出如何成为几何结论”分别编码为可检索、可验证、可演化的技能，再用在线成功/失败轨迹修补技能库。

## 研究问题

### 现有工具增强为什么仍然不可靠

论文把现有方法归纳为两种极端（PDF pp. 1–2，Fig. 1）：

- **从工具箱动态规划。** 灵活，但没有显式依赖和执行顺序约束，可能在获得目标坐标、点云或相机姿态之前就调用 Python，产生无效序列。
- **固定手工流水线。** 顺序可靠，但不论问题是否需要都会调用一整套工具，增加冗余计算，且难以覆盖不同空间任务。

因此，问题不是“有没有工具”，而是能否从历史轨迹中抽象出**可组合的证据链**。空间技能尤其难抽取：成功轨迹可能有冗余，失败轨迹也可能包含局部有效的感知、绑定或几何操作。

### 作者的工作假设

如果将工具依赖、参照系、输入/输出契约和停止条件显式化，并让演化过程由局部验证和历史使用统计约束，那么过去的空间推理经验可以变成下一次推理的可执行结构，而不是只能由模型重新阅读的长轨迹。

## 数据与任务定义

### 在线 test-then-update 协议

第 $t$ 个 episode 输入 $x_t=(I_t,q_t)\in\mathcal I\times\mathcal Q$，输出预测 $\hat y_t\in\mathcal Y$。工具集合为 $\mathcal T=\mathcal T_{vis}\cup\mathcal T_{py}$，技能库为 $Lib_t=(A_t,S_t)$。工作记忆 $M_{t,k}$ 保存当前证据、符号变量、执行历史、verifier 结果和答案假设（PDF p. 3）。

关键防泄漏约束是：每个预测在 ground truth 揭示前恰好记录一次；标签只用于评价该预测、判断完整轨迹 $\tau_t$，随后才写入轨迹缓冲区 $B_t$。一个 episode 内 $Lib_t$ 固定；只有当缓冲区达到 $N_{buf}$ 时，库才在 episode 之间更新为 $Lib_{t+1}$。因此这是在线自适应评估，不是把当前样本答案直接反馈给当前样本的循环。

### 基准和子任务

- **MMSI：** Attribute、Motion、Positional Relation、Multi-Step Reasoning (MSR)。
- **MindCube：** Rotation、Around、Among。
- **OmniSpatial：** Dynamic Reasoning、Perspective Taking。

这些任务共同覆盖多视图、相机运动、对象相对位置、参照系切换、动态/视角相关推理，而不是单纯的单图物体识别。

### 指标

- **Prequential answer accuracy：** 每个预测先评估，再把标签用于技能演化。
- **FTCS (First-Pass Compositional Tool-Chain Success Rate)：** 对至少调用两个不同任务工具的样本，所有任务工具调用均成功且没有失败尝试的样本比例。
- **Python success rate：** 成功的 `PythonTool.code` 调用比例，重试分别计数。

FTCS 衡量的是组合链的首次执行可靠性，不等价于最终答案正确；Python success 也只说明代码调用成功，不能单独证明输入感知证据或几何结论正确。

## 方法主线

### 神经符号技能形式化

技能库写为

$$Lib=(A,S),\qquad S=S_{tool}\cup S_{geo}.$$

原子指令为

$$a=(e_a,v_a),\qquad e_a:U_a\rightarrow O_a,\qquad v_a:O_a\rightarrow\{0,1\},$$

其中 $e_a$ 将带类型输入 $U_a$ 映射到输出 $O_a$，$v_a$ 对输出做局部验证。$A$ 分成控制器可见的 $A_{tool}$ 和只在 Python 内执行的 $A_{geo}$；后者不是独立的控制器动作。

每个高层技能为

$$s=(V,E,\kappa),\qquad V\subseteq A,\quad E\subseteq V\times V,$$

$E$ 表达依赖，$\kappa$ 保存实例化所需的对象绑定、参数、参照系、单位、谓词和证据条件。

### Tool-Use Skill

Tool-Use Skill 是控制器可见的有序 pipeline：

- docstring 说明何时应该检索；
- ordered steps 指定工具原子和语义职责；
- bindings 将当前问题的对象、视图和参数接入步骤；
- stopping condition 指明证据何时足够；
- 状态可为 `seed`、`active` 等，并记录 `seen`、`matched`、`used`、`correct_after_use` 等经验统计。

论文给出的原生工具库（Supplementary A.2，PDF pp. 14–15）包括 `SemanticDetector.detect`、`GeometricReconstructor.reconstruct`、`GeometricReconstructor.project_box_to_3d_points`、`ObjPoseEstimator.predict_obj_pose`、`MetricScaleEstimator.estimate_scale`、`EasyOCR.ocr`、`LanguageToCamera.visualize_camera_layout` 和 `PythonTool.code`。GroundingDINO、VGGT、MoGe 与 object-pose backend 是固定的内部视觉后端，不作为 planner-visible atom，因此比较方法共享工具接口时仍然共享底层感知组件。

### Geometry Skill

Geometry Skill 是 Python 内部的自包含、可验证计算内核。它可以封装：

- 3D 点的稳健中心估计；
- world-to-camera 坐标变换；
- 相机位移和朝向归一化；
- 单位/尺度转换；
- 距离和距离变化比较；
- 将自然语言选项解析为可比较的方向向量；
- 一致性检查和诊断返回。

重要约束是 Geometry Skill 不能只存某个样本的答案或对象名；必须声明输入绑定、形状、参照系、适用条件和 failure guard。缺失或不可比证据应返回 diagnostic，而不是用默认选项伪造答案。

### 机制流程

每次推理迭代为四步（PDF pp. 3–4，Fig. 2）：

1. **Skill Retrieval：**
   $$C_{t,k}=LLMRetrieve(I_t,q_t,M_{t,k};S_t).$$
   将问题和工作状态压缩为结构化 decision context，只返回少量候选技能。
2. **Action Selection：**
   $$u_{t,k}=LLMSelect(I_t,q_t,M_{t,k},C_{t,k}),$$
   其中动作可以是 `stop`、激活/恢复一个 Tool-Use Skill，或直接调用兼容的工具 atom。
3. **Tool/Code Execution：** 单个视觉工具原子直接产生感知证据；到达 Python atom 后，从 $M_{t,k}$ 绑定所需工件，并实例化兼容 Geometry Skill。代码块按依赖顺序执行，返回数值输出和 verifier 结果。
4. **State Update：** 对非终止动作，完整迭代为
   $$ (I_t,q_t,M_{t,k})\rightarrow C_{t,k}\rightarrow u_{t,k}\rightarrow(o_{t,k},\nu_{t,k})\rightarrow M_{t,k+1}, $$
   其中 $\nu_{t,k}\in\{0,1\}$ 表示执行和局部验证是否成功。证据不足就继续检索；足够时返回答案并保存完整轨迹。

这里“可中断”很重要：一个高层 Tool-Use Skill 的下一个节点只有在依赖就绪时执行，控制器可以在技能中途停止、恢复或转入另一个可兼容动作，而不是被固定模板强制跑完。

### 自演化：analysis → fusion → pruning

完整轨迹为

$$\tau_t=((M_{t,k},u_{t,k},o_{t,k},\nu_{t,k})_{k=1}^{K_t},\hat y_t),\qquad B_{t+1}=B_t\cup\{\tau_t\}.$$

当 $|B_{t+1}|<N_{buf}$ 时，库不变；达到阈值才触发演化。

**Trajectory Analysis。** 分解每条轨迹的操作、参数、产生的 artifacts、消费的变量和局部结果，聚合重复的依赖模式，产生 $\Delta A_t$、支持片段 $G_t^+$ 和无效片段 $G_t^-$：

$$\Delta A_t,G_t^+,G_t^-=LLMAnalyze(B_{t+1}).$$

支持片段可能表达“先执行 $a_i$ 才能执行 $a_j$”；无效片段记录反复导致执行或 verifier 失败的转移。成功轨迹贡献可复用结构，失败轨迹贡献缺失依赖和 failure guard。

**Skill Fusion。** 将候选原子/片段与统一库比较：

$$Lib^{fuse}_{t+1}=LLMFusion(Lib_t,\Delta A_t,G_t^+,G_t^-).$$

可添加支持片段、删除冗余或不兼容依赖、替换受影响子图并保留其余结构。共享工具组织的片段进入 Tool-Use Skill；数值变换和验证片段进入 Geometry Skill。融合并非让每个样本生成一个永久技能，而是要求跨轨迹有重复结构、完整停止条件和可观察 workspace 结果。

**Skill Pruning。** 对每个原子或高层技能 $z$，记录调用次数 $n_t(z)$、失败率 $ER_t(z)$、不活跃年龄 $Age_t(z)=t-t_{last}(z)$、存续时间 $Tenure_t(z)=t-t_{add}(z)$。剪枝条件为

$$n_t(z)\ge n_{min}\land ER_t(z)>w_t(z)\rho_{err}\quad\lor\quad Age_t(z)>w_t(z)T_{idle},$$

其中

$$w_t(z)=1+\lambda\frac{Tenure_t(z)}{1+Tenure_t(z)},$$

且选取 $\lambda\ge0$ 使 $(1+\lambda)\rho_{err}\le1$。$n_{min}$ 防止少量噪声导致新技能过早删除；tenure 让长期存活且有历史的条目拥有更宽松的错误率/不活跃保护。删除原子后，依赖它的技能要被修复或丢弃。

## 关键结果

### 主结果与强基线

论文比较 AWM、ASI、SpaAge-PE、SpaAge-ReAct、GCA 和 LAST；所有方法使用相同工具集和接口配置。SpaAge 让 LVLM 直接规划调用，GCA 先统一几何形式化，LAST 使用预定义空间技能（PDF p. 5）。

| Backbone | Method | MMSI Overall | MindCube Overall | OmniSpatial Overall |
|---|---|---:|---:|---:|
| GPT-5.4 | NeSy-Spatial | 49.50 | 71.50 | 60.27 |
| GPT-5.4 | strongest baseline | 48.00 | 71.01 | 61.00 |
| Gemini 2.5 Pro | NeSy-Spatial | 61.50 | 82.50 | 70.94 |
| Gemini 2.5 Pro | strongest baseline | 61.00 | 72.38 | 66.97 |

GPT-5.4 上，NeSy-Spatial 在 MMSI 和 MindCube 分别超过最强基线 1.50 和 0.49 个百分点，在 OmniSpatial 为 60.27，对比 GCA 的 61.00 略低。Gemini 2.5 Pro 上三个基准均为最高，差距为 +0.50、+10.12、+3.97。这里必须以 PDF Table 1 的 **70.94** 为 Gemini OmniSpatial Overall；目录中已有的旧摘要把该值误写成 73.50，不能作为证据使用。

按子任务看，GPT-5.4 的 NeSy-Spatial 在 MMSI 的 Motion 56.00、Positional Relation 52.08，在 MindCube 的 Among 73.37，在 OmniSpatial 的 Dynamic Reasoning 66.27；Gemini 2.5 Pro 的对应优势包括 MMSI Motion 72.03、Positional Relation 66.67，MindCube Rotation 85.73、Among 84.02，以及 OmniSpatial Perspective 73.50（PDF Table 1, p. 5）。

### 工具利用和执行可靠性

NeSy-Spatial 的平均指标（PDF Fig. 5，p. 6）为：

- GPT-5.4：平均 FTCS **94.56**，Python success **95.45**；比最强基线平均值分别高 **7.17** 和 **6.67** 个百分点。
- Gemini 2.5 Pro：平均 FTCS **88.67**，Python success **96.21**；比基线分别高 **0.21** 和 **7.76** 个百分点。

解释上，Tool-Use Skill 主要减少首轮工具链中的错误顺序和不必要调用；Geometry Skill 主要让 Python 内部计算复用同一套参照系、输入契约与诊断逻辑。FTCS 的改善比最终 accuracy 更直接地支持“技能改善了工具链”，但仍不能证明每个工具输出因果上被正确使用。

### 在线演化的持续收益

Fig. 6 将在线演化的 NeSy-Spatial 与固定初始库的 Frozen 比较。经过最初 10 个样本后绘制累积预quential 曲线；流结束时 NeSy-Spatial 比 Frozen 高：MindCube **12.5**、MMSI **3.5**、OmniSpatial **2.5** 个百分点，宏平均从 **54.2%** 到 **60.3%**（PDF p. 7）。

Fig. 5 右侧显示技能数量并非单调增长：MindCube 从 3 到 17，MMSI 从 3 到 9，OmniSpatial 从 4 到 20；中间下降阶段对应剪枝。它支持“在线演化不是无条件记忆所有经验”，但没有单独给出长期库污染、遗忘或跨数据集迁移的统计。

### 消融到底说明了什么

Table 2（PDF p. 7）报告 Tool-Use Skill、Geometry Skill 与 Evolution 的组合：完整配置为 MindCube **71.50**、MMSI **49.50**、OmniSpatial **60.27**。冻结演化但保留两类技能为 **59.00/46.00/57.49**，移除 Tool-Use Skill 为 **60.00/43.50/57.59**，移除 Geometry Skill 为 **69.50/47.00/58.00**（顺序均为 MindCube/MMSI/OmniSpatial）。相对完整配置的下降分别是：

- 禁用 Evolution：−12.50/−3.50/−2.78；
- 移除 Tool-Use Skill：−11.50/−6.00/−2.68；
- 移除 Geometry Skill：−2.00/−2.50/−2.27。

因此，在线演化是 MindCube 上最大收益源，Tool-Use Skill 对证据收集尤其关键，Geometry Skill 的边际收益较小但在三个基准上稳定为正。消融没有把“LLM 的分析/融合质量”“固定视觉后端”“技能库规模”和“阈值调参”完全解耦，所以不能把每个差值解释成纯粹的单模块因果效应。

## 补充案例：方法如何真正工作

### MindCube：相机运动（Supplementary B.1，Fig. 7，PDF pp. 16–17）

问题给出同一场景的两张视图，询问第二台相机相对第一台相机是左/右、前/后或斜向移动。系统先检索并执行 `GeometricReconstructor.reconstruct`，恢复共享 3D 场景和相机外参；随后取 `camera0_motion_option_from_extrinsics` Geometry Skill，把第二台相机位移变换到 camera-0 frame，解析选项方向并输出 **C：diagonally forward-left**。

这个案例说明 Geometry Skill 的价值不是替代重建，而是固定 reference-frame convention、外参归一化、相机中心恢复和选项映射；同一套数值逻辑可以在后续相机运动样本中重用。

### MMSI：grounded object 与相机框架方向（Supplementary B.1，Fig. 8，PDF pp. 17–18）

问题先在 Image 1 中定位“黑色边框、白色背景的画”，再问它相对于 Image 2 观察者的方向。Tool-Use Skill 组织 `reconstruct` → `detect` → `project_box_to_3d_points`；检测框被投影到共享 3D 空间后，Geometry Skill `camera_frame_object_quadrant_choice` 在指定相机 frame 中选择唯一答案，结果为 **C：front-left**。

这里的关键是不能把 Image 1 中的视觉方位直接当作 Image 2 观察者的方位；必须保留跨视图的绑定和参照系转换。

### OmniSpatial：allocentric relation（Supplementary B.1，Fig. 9，PDF pp. 18–19）

问题以投影屏作为参考实体，以屏幕的物体中心视角询问电风扇在左还是右。系统分别检测屏幕和风扇，用 `ObjPoseEstimator.predict_obj_pose` 获取参考物体朝向，再把两个检测框 lift 到同一 3D 重建中，最后执行 `allocentric_left_right_from_reference_pose` Geometry Skill。结果是风扇在屏幕中心 frame 的 **right**。

这个例子是对“参照对象是谁”的检验：屏幕不是默认的相机，且 object-centric frame 需要显式姿态证据；这比单纯的像素左/右启发式更受约束。

### Skill evolution：turn-then-move（Supplementary B.2，Fig. 10，PDF pp. 19–20）

初始 Four-view Tool-Use Skill 能重建场景并解析转向，但在失败轨迹中发现它在“转向后视角恢复”后就停止，缺少“在新视角中 grounding 目标”和“比较前进后是否更接近目标”。轨迹分析把这两个缺失操作识别为 residual extension，融合时保留父 pipeline 并增加专用 branch；新 stopping condition 要求 turned-facing view、destination grounding 和 forward-motion comparison 都成功。后来同类问题可检索该分支，而纯视点问题仍使用父技能。

这是一种比“把失败样本写进记忆”更具体的学习：失败被转换成缺失依赖和条件化分支。

### Geometry evolution：相机运动内核（Supplementary B.2，Fig. 10，PDF pp. 20–21）

多个样本中的 Python 程序重复做同一操作，却有硬编码选项标签、无效外参默认回答、方向解析错误等问题。系统归纳出可复用内核 `camera0_motion_option_from_extrinsics`：先归一化和验证外参栈，恢复两个 camera centers，在第一相机 frame 中表达位移，解析当前问题选项，若证据无效则返回 diagnostic。补充实例输出选项 **C**（diagonal-forward-left）。

## 深度分析

### 真正贡献是什么

论文把“经验”规定成了可执行的形状：

- 工具经验是带 semantic role、dependency edge、binding、stopping condition 的有序图；
- 几何经验是带 reference-frame、unit、input contract 和 failure guard 的代码内核；
- 轨迹经验被分解到操作、工件和变量消费关系，而不是只保留自然语言总结；
- 演化动作是受支持片段添加、冗余边删除和局部子图替换，而不是无约束的整库重写。

因此，相对普通 reflection 或 episodic memory，NeSy-Spatial 的可复用性来自**结构化执行约束**，而不仅是模型“记得曾经怎么做”。

### 为什么结果成立

1. **证据链更短且更正确。** Tool-Use Skill 把 detector、reconstructor、projection、Python 等操作按数据依赖连接，减少先算后取证据的错误。
2. **几何代码跨样本复用。** Geometry Skill 把参照系转换和选项解析从样本级临时 Python 中抽离，减少硬编码和重复生成。
3. **失败暴露缺失后缀。** turn-then-move 例子显示，失败并非整条路径无用；局部成功前缀可保留，缺失的 grounding/comparison 后缀可加为条件分支。
4. **库增长受到经验门控。** 20 条轨迹才演化，且剪枝受最小支持、错误率和不活跃阈值约束，解释了曲线的增长—下降而不是无限膨胀。
5. **检索上下文有边界。** 先给 compact descriptions，选中后再展开完整定义，避免技能库变大后立即淹没 planner。

### 容易误读的地方

- **“state-of-the-art”是局部结论。** 仅在三个 benchmark、固定原生工具、两个 API backbone 和本论文的 online stream 设置内成立。
- **不是形式化证明系统。** verifier 是局部执行/输出检查；LLM 仍负责候选检索、轨迹分析和技能融合，几何内核的正确性也依赖工具输出和假设。
- **不是当前样本标签泄漏。** test-then-update 防止当前预测读取当前标签，但过去样本的标签会改变后续技能库，所以结果是在线适应设置，不是静态 iid 测试。
- **库变大不等于技能更通用。** retained skill 数量达到 17/9/20 只说明更多条目通过经验维护，并不证明语义稳定、无冲突或可跨 benchmark 迁移。
- **FTCS/Python success 不是答案因果度量。** 工具成功并且被调用，不保证该输出是最终判断所必需的，也不保证检测/重建误差已被纠正。

### 复现注意点

Supplementary A 给出了主要设置（PDF pp. 14–15）：

- 初始化种子技能：MMSI 3、MindCube 3、OmniSpatial 4；
- warm-up trajectories 10；same-family trace batch 5；repeated-failure support 2；pending-trace fallback threshold 40；candidate fusion batch 2；每个 induction prompt 最多 20 条轨迹；prototype trace window 80；
- 每个 query 最多选择 4 个技能；mutable library 上限 24；zero-correct retirement support 2；minimum invocation support 5；minimum retained accuracy 0.4；inactivity threshold 100；
- 主实验演化设置：$N_{buf}=20$、$n_{min}=5$、$\rho_{err}=0.4$、$T_{idle}=100$、$\lambda=0.5$；
- 推理 wave size 为 5；MMSI 最大 12 turns，MindCube/OmniSpatial 最大 8 turns（Supplementary A.1）。

复现所需不仅是 LLM API，还包括固定的视觉后端、跨视图重建、物体检测/姿态估计、Python 执行环境、完整 selector/planner/induction/fusion prompts 和 benchmark 数据。论文说明完整 prompts 会在 code release 后提供；仅凭 PDF 无法保证独立复现全部实现细节。论文也没有报告总 token、每样本调用数、延迟、GPU/CPU 成本或演化阶段 LLM 成本。

### 复杂度与扩展性

短期内技能检索降低了每轮上下文长度，但长期库的候选管理仍需要维护。融合和剪枝是额外的 LLM 调用；$N_{buf}=20$ 意味着演化并非每个样本更新，能够减少非平稳性但也延迟新技能可用时间。若把方法扩展到 unseen tools，必须解决 atom schema、输出类型、依赖图和 verifier 的兼容性，而不只是把新工具名加入 prompt。

## 局限

1. **任务范围窄。** 只评估三个空间推理基准；没有真实机器人闭环、室外场景、导航、长期操作或高安全约束任务。
2. **感知误差是外部瓶颈。** GroundingDINO、VGGT、MoGe、object-pose 或重建出错时，技能主要改善调度和诊断，不能保证修复错误证据。
3. **LLM 归纳质量不可忽略。** 错误轨迹分析或融合可能把样本特例固化成技能；论文没有大规模长期污染/遗忘实验。
4. **依赖固定工具接口。** 所有基线共享工具接口有利于比较，但也使结论更接近“在给定工具池上的调度/结构化收益”。
5. **评测信号不完整。** 没有 token、延迟、调用成本、反事实工具移除、跨 benchmark transfer 或不同工具质量下的敏感性分析。
6. **提示词与实现尚未完全开放。** Supplementary D 给出模板的目的、输入、输出格式和限制，但完整可执行 prompts 仍依赖后续 code release。

## 我的笔记

### 放进 3D/agent 局部地图的位置

它位于“tool-augmented spatial reasoning agent”与“experience/skill memory”交叉处：不是新 3D 重建模型，也不是具身控制策略，而是把视觉工具、共享 3D 证据和几何程序组织成可演化 agent skill。与固定 pipeline 的差异是动态中有显式依赖；与普通 memory agent 的差异是记忆被压缩成可执行图和代码内核；与纯 LLM reflection 的差异是局部操作有 verifier 和 typed workspace。

### 我认为最值得复用的设计

1. 把“工具输出是否真的被后续决策消费”作为独立审计对象，而非只看最终答案。
2. 在技能记录中强制加入触发条件、输入绑定、reference frame、unit、stopping condition 和 failure guard。
3. 对失败轨迹做 step decoupling：分离有效前缀、错误参数、缺失依赖和失败后缀，再决定是修补父技能还是创建分支。
4. 在线 RL/持续学习时先区分“策略变化”和“技能库变化”；本论文将库更新放在 episode 之间，避免同一 episode 内库漂移。
5. 未来可把 pruning 从经验阈值升级为类型检查、schema 检查和反事实证据贡献度检查。

### 后续问题

- 统一库跨 MMSI、MindCube、OmniSpatial 迁移时，哪些 geometry kernels 真正保持 reference-frame/单位不变？
- 能否以“移除某个工具输出后答案是否改变”的反事实测试替代单纯 FTCS？
- 如何用静态图类型系统阻止 fusion 生成缺失绑定、错误维度或混用 camera/world frame 的技能？
- 当失败标签本身含噪时，如何避免错误 failure lesson 污染高成功率父技能？
- 对真实机器人导航，技能的 stopping condition 还需要加入时间、碰撞、可见性和安全约束。

## 引用

Tian, Shi-Yu, et al. “Self-Evolving Neuro-Symbolic Skills for Tool-Augmented Spatial Reasoning.” arXiv preprint arXiv:2608.07955v1, 8 Aug 2026.

## 图表证据与材料说明

原 PDF 中的 Fig. 1–10 和 Table 1–9 均已逐页阅读并在本笔记对应段落中引用。由于当前工作区不允许通过未获批准的 PDF 渲染命令另行生成二进制裁剪图，本次不写入图片文件，也不插入断开的 Markdown 图片链接；Table 1/2 的关键数值、Fig. 5/6 的曲线结论、Supplementary Fig. 7–10 的案例流程均已转写。`paper_DeepPaperNote.figure_decisions.json` 记录每个图/表的 placeholder 决策，`paper_DeepPaperNote.lint.json` 记录零图片链接和结构检查结果。
