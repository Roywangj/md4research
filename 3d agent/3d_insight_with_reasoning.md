# 3D Agent × Reasoning Insight：学习可验证、因果依赖的 3D 工具轨迹

> 主线：3D agent 如何主动获取、组织和验证空间证据。
>
> 支线：reasoning 模型如何生成工具调用轨迹，并证明轨迹中的工具观察确实参与了答案。
>
> 与 [3d_insight](<3d_insight.md>) 的关系：前者已经提出 `Ctask → evidence need → tool program → relation expert → verifier` 的 GeoSkill-Agent 雏形；本文进一步加入 **belief update、训练型 reasoning trace、反事实证据审计和最小实验闭环**。
>
> 证据范围：基于本地 `3dAgent` 与 `Reasoning` collection 的精读笔记、实验表格及 source anchors。论文结论、跨论文综合和新研究假设分别标注为“直接证据”“综合推断”和“研究假设”。

## 0. 最核心的 thesis

我认为最值得推进的方向可以压缩成一句话：

> **3D agent 不应学习“调用哪个 API”，而应学习在显式参考系下执行一条可验证的空间测量程序；reasoning trace 不应只记录 thought/tool/observation，而应记录每次工具调用解决了什么不确定性、产生了什么新证据，以及删除或篡改该证据后答案是否按预期变化。**

暂定项目名：

- `GeoTrace-Agent: Learning Verifiable 3D Tool Trajectories for Spatial Reasoning`
- `CausalGeoAgent: Evidence-Causal Tool Use for 3D Spatial Intelligence`
- `GeoSkill-R: Reference-Frame-Aware Reasoning over 3D Tools`

我更喜欢 `GeoTrace-Agent`：它把相对现有工作的差异落在“轨迹是什么、怎样训练、怎样证明”上。

## 1. 两条文献线汇合后，真正缺的是什么

### 1.1 3D Agent 主线已经分别解决了六个局部问题

| 问题层                              | 代表论文                                                                                                                                                                                                                                                                                                                                                                            | 已给出的答案                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| 如何获得新空间观察                        | [Think3D](<3d agent/Think3D/paper_DeepPaperNote.md>)                                                                                                                                                                                                                                                                                                                                     | 重建点云、选择相机锚点、渲染新视角；RL 学习视角策略                      |
| 如何先定义问题                          | [GCA](<3d agent/Geometrically-Constrained Agent for Spatial Reasoning/paper_DeepPaperNote.md>)                                                                                                                                                                                                                                                                                           | `Ctask=(CR,CO)`，先固定参考系和目标，再调用工具与代码               |
| 如何把原始几何变成可用证据                    | [S-Agent](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>)                                                                                                                                                                                                                                                                         | L1 二维感知、L2 三维提升、L3 空间专家；双记忆累积时空证据                |
| 如何复用成功/失败经验                      | [Skill-3D](<3d agent/Skill-3D/paper_DeepPaperNote.md>)                                                                                                                                                                                                                                                                                                                                   | Scene Memory、Skill Library、失败 lesson、技能检索与后训练    |
| 如何把 2D reasoning 回连到 3D identity | [REALM](<../Reasoning/TrainingFree/REALM An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting/paper_DeepPaperNote.md>)                                                                                                                                                                                                            | 多视角投票、3D feature field、global-to-local grounding |
| 如何验证 3D 输出不只是“看起来像”              | [P3D-Bench](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>)、[Code2Worlds](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>)、[SimWorld Studio](<3d agent/SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning/paper_DeepPaperNote.md>) | 执行、几何、拓扑、部件、物理/规则 verifier 与迭代修正                 |

### 1.2 Reasoning 支线已经给出工具策略的训练方法和警报

| 问题层          | 代表论文                                                                                                                                                                                                                                                                                                                               | 对 3D agent 的迁移                        |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| 是否值得启动昂贵推理   | [SDR-MCoT](<../Reasoning/TrainingFree/Mitigating Low-Quality Reasoning in MLLMs Self-Driven Refined Multimodal CoT with Selective Thinking and Step-wise Visual Enhancement/paper_DeepPaperNote.md>)                                                                                                                               | 先做低成本不确定性路由，再决定是否重建/渲染/多轮搜索           |
| 如何学习主动观察     | [DeepEyes](<../Reasoning/Train/DeepEyes Incentivizing Thinking with Images via Reinforcement Learning/paper_DeepPaperNote.md>)                                                                                                                                                                                                     | 条件工具奖励：只有工具帮助答对才奖励，而不是奖励调用本身          |
| 如何学习通用工具组合   | [DeepEyesV2](<../Reasoning/Train/DeepEyesV2 Toward Agentic Multimodal Model/paper_DeepPaperNote.md>)、[Thyme](<../Reasoning/Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>)                                                                                                                                                                   | cold-start SFT 建协议，再用 RL 学何时调用、组合和停止  |
| 如何表示证据轨迹     | [PFlowNet](<../Reasoning/Train/Perceptual Flow Network for Visually Grounded Reasoning/paper_DeepPaperNote.md>)                                                                                                                                                                                                                    | 把“看哪里”和“证据是什么”绑定；专家作为支持约束而非唯一动作真值     |
| 如何复用长轨迹中的旧证据 | [VisRef](<../Reasoning/TrainingFree/VisRef Visual Refocusing while Thinking Improves Test-Time Scaling in Multi-Modal Large Reasoning Models/paper_DeepPaperNote.md>)、[PRCR](<../Reasoning/TrainingFree/Position Rebinding Cache Reuse Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning/paper_DeepPaperNote.md>) | 选择相关且互补的旧视角证据，并带坐标/位置 provenance 安全回看 |
| 如何证明工具不是装饰   | [Position paper](<../Reasoning/TrainingFree/Position Your VLM May Not Be Thinking with Interleaved Images/paper_DeepPaperNote.md>)                                                                                                                                                                                                 | 必须做 no-observation、轨迹置换、遮挡和反事实证据测试    |

### 1.3 汇合后的核心缺口

现有 3D agent 往往已经能生成一条合理轨迹，但还没有同时证明四件事：

1. 轨迹中的参考系是正确的；
2. 每次工具调用都对应一个明确的证据缺口；
3. 工具观察被转换为答案级几何证据并更新了场景 belief；
4. 删除、置换或篡改观察会让答案按几何规律变化。

因此最自然的下一步不是继续加工具，而是：

> **把 3D 工具轨迹从 workflow 提升成 evidence-causal program。**

## 2. 关键证据：为什么这个 gap 不是想象出来的

### 2.1 有 3D 工具，不等于会用 3D 工具

**直接证据。** Think3D 中，普通 Qwen3-VL-4B 接上工具平均只提升约 `0.8`；经过 Think3D-RL 后，工具带来的增益达到约 `12.05`。随机、启发式和学习型探索策略的对比中，学习策略明显更好。S-Agent 也报告，弱 8B 规划器未经训练直接套 agent 框架时，部分基准甚至低于基座。

**综合推断。** 工具价值取决于策略容量：模型必须知道什么观察有信息量、怎样解释返回结果，以及何时停止。对弱模型而言，新增观察本身会增加上下文噪声。

### 2.2 原始 3D 数值不是模型可直接消费的“证据”

**直接证据。** S-Agent 的消融中，加入 Level-2 原始三维证据只从 `49.0` 到 `49.8`；加入 Level-3 任务专家后跃升到 `56.7`。这说明相机位姿、深度和点云需要先被转换为距离、方向、计数或对象视角等任务级关系。

**综合推断。** 3D agent 的中间语言不应是巨量坐标，也不应只是自由文本总结，而应是带单位、参考系、对象 identity 和来源的 typed evidence，例如：

```text
relation: left_front
target_id: cup_02
reference_id: sofa_01
frame: origin=sofa_01; forward=sofa_01→tv_01; up=gravity
support: view_2 bbox + metric_depth + orientation
confidence: 0.83
```

### 2.3 参考系错误发生在工具之前，后续工具无法自动补救

**直接证据。** GCA 在 MMSI 消融中，无约束工具为 `40.1`，完整形式化约束达到 `47.6`；删除目标约束只下降 `1.2`，删除参考系约束下降 `6.6`。Think3D 的相机锚点消融也表明，点云和视角操作必须有稳定的坐标语义。

**综合推断。** 参考系不是一个附加 prompt，而是整个工具程序的类型系统。`left/right/front/behind/distance` 等专家都必须显式接收 `CR`；不满足 frame contract 的 observation 不应进入答案。

### 2.4 多视角数量不如视角选择和 3D identity 绑定重要

**直接证据。** REALM 中，去掉结构化相机选择时结果会大幅下降；全局多视角负责选择对象 identity，局部视角负责边界细化。它的 3D feature field 则保证不同 2D mask 回连到同一个 3D 对象。

**综合推断。** 3D reasoning trace 必须保存 persistent object identity。否则“多视角”只是多张独立图片，模型无法判断 view-1 的杯子和 view-3 的杯子是否同一对象，也无法安全去重或累计属性。

### 2.5 工具轨迹看起来合理，不等于答案依赖工具观察

**直接证据。** Reasoning 的 Position paper 删除多种 thinking-with-images 方法的交错图像后，多个基准变化很小；普通 SFT 也能获得类似涨点。它提醒我们，轨迹文本、微调分布和 benchmark 先验可能解释相当部分收益。

**研究判断。** 3D agent 论文如果只展示“模型渲染了三个视角后答对”，证据还不够。必须证明：

- 不给新渲染图时答不对；
- 换入错误视角/深度/位姿时会失败或触发 verifier；
- 按几何规律编辑观察时，答案也按规律改变；
- 等成本的纯文本 self-refine 不能取得相同收益。

## 3. 重新定义 3D reasoning trace

### 3.1 从动作日志变成 belief-update program

建议把一条轨迹写成：

$$
\tau=\{z_t\}_{t=0}^{T},\qquad
z_t=(B_t,C_t,U_t,N_t,A_t,O_t,E_t,V_t).
$$

| 符号 | 含义 | 例子 |
|---|---|---|
| $B_t$ | 当前场景 belief / entity memory | cup_02 在 view-2 可见，身份已跨视角绑定 |
| $C_t$ | 几何任务契约 `Ctask=(CR,CO)` | 以沙发为原点、朝电视为 forward |
| $U_t$ | 未决不确定性 | 杯子深度未知；左右不能由图像坐标判断 |
| $N_t$ | 证据需求 | 目标 3D 坐标 + sofa→TV 朝向 |
| $A_t$ | 工具动作及参数 | detect → metric depth → orientation expert |
| $O_t$ | 原始环境观察 | boxes、mask、depth、pose、render |
| $E_t$ | 任务级证据 | cup 在局部 frame 的 x 坐标为负 |
| $V_t$ | verifier 结果 | identity 一致；跨视角关系稳定；证据充分 |

状态更新为：

$$
B_{t+1}=\mathrm{Merge}(B_t,E_t,\mathrm{provenance}(O_t)),
$$

下一动作由：

$$
A_{t+1}\sim\pi_\theta(q,B_{t+1},C_t,U_{t+1},\mathcal{S}),
$$

其中 $\mathcal{S}$ 是检索到的场景技能集合。

### 3.2 这一定义带来的变化

- `Think3D` 的视角动作成为 $A_t$，而不是整个 reasoning；
- `GCA` 的 `Ctask` 成为贯穿轨迹的不可变/可版本化契约；
- `S-Agent` 的双记忆成为 $B_t$ 与过程 history 的分离；
- `Skill-3D` 的技能不再只保存工具顺序，而保存 `N_t → A_t → E_t → V_t`；
- `PFlowNet` 的“区域 + 证据描述”被扩展成“3D observation + typed relation”；
- Position paper 的审计变成对 $O_t/E_t$ 的干预，而不是只看轨迹是否流畅。

## 4. 建议系统：GeoTrace-Agent

```text
Question + multi-view images / video / 3D scene
    ↓
[1] Task compiler
    Ctask = reference frame CR + target constraint CO
    ↓
[2] Belief & uncertainty manager
    persistent entities + unresolved spatial variables
    ↓
[3] Evidence-need predictor
    visibility / identity / depth / orientation / metric / path / physics
    ↓
[4] Skill retriever & tool router
    direct answer / reuse memory / cheap 2D / 3D lifting / new view / simulator
    ↓
[5] Tool executor
    detection / segmentation / depth / pose / point cloud / render / code / physics
    ↓
[6] Observation compiler
    raw observation → typed, frame-aware, provenance-linked evidence
    ↓
[7] Verifier
    geometry consistency + cross-view identity + evidence sufficiency + cost
    ↓
answer ← sufficient
    or
belief update → retry / fallback / new skill lesson
```

### 4.1 Task compiler：先把空间语言变成几何契约

输出至少包括：

```yaml
task_type: relative_direction
CR:
  origin: sofa_01.center
  forward: normalize(tv_01.center - sofa_01.center)
  up: gravity
  right: cross(forward, up)
CO:
  target: cup_02
  reference: sofa_01
  output_space: [left, right, front, behind]
```

对动态任务，必须允许 `CR(t)` 随相机或 agent 状态变化；这是 GCA 当前静态参考系的自然扩展。

### 4.2 Evidence-need predictor：不要从问题直接跳到工具名

同一证据可以由不同工具产生。例如相对距离可以来自：

- 单目深度 + 框中心；
- 多视角重建 + 最近点；
- 已有场景 memory；
- 仿真世界的 ground-truth query。

因此先预测 `evidence_need`，再让 router 在准确率、时延和失败风险之间选工具。这也让技能跨工具迁移：换掉 Depth Anything 或 Pi3，不必重写任务逻辑。

### 4.3 Observation compiler：把原始输出转成 typed evidence

输出应同时带：

- 值与单位；
- reference frame；
- object identity；
- source view/time/tool；
- 不确定性与失败标志；
- 可回放的原始 observation 指针。

这一层是 S-Agent 的 Level-3 专家、REALM 的 3D identity 和 PFlowNet 的证据文本的统一接口。

### 4.4 Verifier：至少需要四类检查

| Verifier | 检查内容 | 失败后的动作 |
|---|---|---|
| Frame verifier | 坐标轴、相机/对象/方向 frame 是否与问题一致 | 回到 task compiler 修正 `CR` |
| Identity verifier | 跨视角对象是否同一实例，候选是否唯一 | 增加分割、近景或 identity vote |
| Geometry verifier | 深度、位姿、距离、关系是否跨视角一致 | 换工具/视角，或降级为区间答案 |
| Evidence sufficiency verifier | 现有证据是否足以排除其他答案 | 获取新证据或声明不确定 |

P3D-Bench 和 SimWorld Studio 进一步提醒：如果输出进入 3D 生成/交互，还要加入执行、拓扑、碰撞、支撑、导航可达性和物理 verifier。

## 5. 训练轨迹的具体格式

```xml
<task>
  question: ...
  task_type: relative_direction
</task>

<ctask>
  CR: origin=sofa_01; forward=sofa_01_to_tv_01; up=gravity
  CO: compare cup_02 against sofa_01 in local frame
</ctask>

<belief_before>
  sofa_01 and tv_01 grounded; cup candidate unresolved
</belief_before>

<uncertainty>
  image left/right is not the requested observer frame
</uncertainty>

<evidence_need>
  unique cup identity; 3D positions; sofa-facing-TV orientation
</evidence_need>

<skill_choice id="local_frame_relative_direction_v1" />

<tool_call name="ground_and_segment">
  targets: [sofa, tv, cup]
</tool_call>
<observation loss_mask="true">
  external boxes/masks/IDs
</observation>

<tool_call name="metric_depth_pose" />
<observation loss_mask="true">
  external depth/pose/coordinates
</observation>

<evidence>
  cup_02 has negative local-x under CR; stable across view_2/view_4
</evidence>

<verify>
  frame_valid: true
  identity_consistent: true
  evidence_sufficient: true
</verify>

<answer>left</answer>
```

训练时应预测 `ctask / uncertainty / evidence_need / skill_choice / tool_call / evidence / verify / answer`；外部 observation 必须 mask，避免模型学习伪造工具输出。

## 6. 数据：不能只有成功轨迹

### 6.1 四类正样本

| 样本 | 目的 | 例子 |
|---|---|---|
| Direct-answer | 学会不调用工具 | 单视角已清楚、无参考系歧义的简单关系 |
| Memory-reuse | 学会回看旧证据而非重复执行 | 目标坐标已在 scene memory 中 |
| New-observation | 学会主动获取新信息 | 遮挡、深度歧义、新视角、动态 reference frame |
| Recovery | 学会发现错误并回退 | 第一次 grounding/pose/reconstruction 失败 |

### 6.2 五类反事实/负轨迹

1. `wrong_reference_frame`：把相机 frame 当作人/物体 frame；
2. `wrong_identity`：换入同类别另一实例的 mask/坐标；
3. `stale_observation`：使用过期帧或物体移动前的证据；
4. `redundant_tool`：重复渲染没有新增覆盖的视角；
5. `ignored_or_fabricated_evidence`：工具返回与答案无关，或答案引用不存在的数值。

负轨迹不应只作为丢弃样本，而应生成：失败类型、检测信号、修复动作和是否可形成新 skill lesson。

### 6.3 数据来源建议

| 来源 | 优点 | 风险 | 适合阶段 |
|---|---|---|---|
| VSI / MMSI / BLINK / MindCube / ViewSpatial teacher traces | 与现有 benchmark 可直接比较 | 容易学题型和 benchmark 先验 | MVP 与主实验 |
| Blender / UE5 / SimWorld Studio 合成场景 | 有真值坐标、identity、遮挡、碰撞，可自动造反事实 | sim-to-real gap；资产分布偏 | 轨迹预训练与因果审计 |
| 真实多视角/视频 | 更接近开放世界 | 真值与反事实成本高 | 后期泛化 |
| P3D/Code2Worlds 类可执行程序 | 可检查结构、拓扑和物理 | 任务从问答扩展到生成，工程变大 | 第二篇/扩展 |

最小起步建议：先构造 `500` 条 debug set，保证每个阶段都能被单独评估；闭环稳定后再扩到 `5k–20k` 轨迹。

## 7. 训练方案

### Stage 0：冻结工具，先验证轨迹可执行

先不训练模型，使用强 teacher 生成轨迹并执行；只保留：

- 工具可执行；
- `Ctask` 可自动/人工检查；
- 证据能回连到对象与 reference frame；
- 最终答案正确；
- counterfactual pair 的答案变化符合几何真值。

这一阶段能排除“轨迹文本看起来对、工具链实际上不可运行”的数据污染。

### Stage 1：cold-start SFT 建立协议

训练目标：

- formalize `Ctask`；
- 输出 evidence need；
- 学结构化工具调用；
- 从 observation 生成 typed evidence；
- 做 verifier 与 no-tool 决策。

必须包含大量 direct-answer 和 cheap-tool 样本，避免模型把“重建”学成固定动作。

### Stage 2：RL 优化选择、组合、恢复和停止

建议奖励：

$$
\begin{aligned}
R(\tau)=&\ R_{ans}+\lambda_fR_{frame}+\lambda_iR_{identity}\\
&+\mathbf{1}[R_{ans}>0]\left(\lambda_eR_{evidence}+\lambda_vR_{verify}\right)\\
&+\lambda_{rec}R_{recovery}-\lambda_cC_{tool}-\lambda_rR_{redundant}.
\end{aligned}
$$

设计原则：

- `R_evidence` 由正确答案门控；
- 不奖励工具次数或代码执行本身；
- expensive reconstruction / rendering 比检测、memory reuse 有更高成本；
- no-tool 答对同样是最优策略；
- observation 是环境输出，不计入策略动作长度和 loss；
- 文本规划可采样，工具 JSON/代码/相机参数宜低温或约束解码。

### Stage 3：离线技能演化与轨迹蒸馏

按照 Skill-3D 和 SimWorld Studio 的启发：

1. 冻结 policy 和 library 做 rollout；
2. 抽取成功程序与失败 lesson；
3. 离线合并/版本化 skill library；
4. 再做下一轮 SFT/RL。

不要在同一训练阶段同时快速更新 policy 和 skill library，否则检索目标与策略共同漂移，容易形成非平稳训练。

## 8. 因果评测：这是这条方向最重要的差异化

### 8.1 标准能力指标

| 指标 | 含义 |
|---|---|
| Answer Accuracy | 最终空间答案 |
| `Ctask` / Reference Frame Accuracy | 参考系与目标形式化是否正确 |
| Tool Execution Success | 调用是否成功 |
| ETU | 工具输出是否有效并被使用 |
| Typed Evidence Accuracy | 距离、方位、identity、计数等中间证据是否正确 |
| Recovery Success | 首次工具失败后能否修复 |
| Tool Cost / Latency | 调用次数、重建次数、时延、显存/算力 |
| No-Tool Calibration | 简单题能否克制调用 |

### 8.2 必做的反事实矩阵

| 干预 | 保留什么 | 改变什么 | 预期 |
|---|---|---|---|
| No-tool | 原始输入与同等 token 预算 | 移除全部工具 | 必须工具子集显著下降 |
| No-observation | 保留 tool-call narrative | 删除真实 observation | 如果轨迹依赖观察，性能应下降 |
| Observation shuffle | 保留轨迹结构 | 换入其他样本 observation | verifier 应拒绝或答案下降 |
| Coordinate perturbation | 保留视觉外观 | 改深度/pose/frame 数值 | 关系答案应按几何方向变化 |
| Identity swap | 保留类别 | 换同类实例 identity | 对实例敏感任务应改变答案 |
| Irrelevant view perturbation | 改无关视角/对象 | 保留关键证据 | 答案应稳定 |
| Matched-compute self-refine | 同 token/时延预算 | 工具换成纯文本多轮反思 | 新信息型工具应胜出 |
| Trace-language swap | 保留最终 observation | 换 thought narrative | 检查收益来自证据还是语言模板 |

### 8.3 建议新增三个核心指标

$$
\mathrm{TNG}=Acc_{full}-Acc_{no\mbox{-}observation}
$$

`Tool Necessity Gap (TNG)` 衡量工具观察对必须工具子集的净贡献。

`Counterfactual Geometric Faithfulness (CGF)`：定向改变坐标、identity 或 reference frame 后，答案按几何真值同步变化的比例。

`Irrelevant Evidence Robustness (IER)`：只扰动无关 observation 时，答案与关键证据保持稳定的比例。

理想系统应同时有高 TNG、高 CGF 和高 IER：既真正依赖关键工具证据，又不会被所有工具噪声牵着走。

## 9. 最小可行实验

### 9.1 先收窄任务，不要一开始做完整 embodied agent

建议只选四类任务：

1. reference-frame relative direction；
2. metric/ordinal distance；
3. cross-view identity + counting；
4. active view selection under occlusion。

它们分别对应 GCA、S-Agent、REALM/Skill-3D 和 Think3D 的强项，也最容易自动构造反事实。

### 9.2 最小工具池

```text
cheap: memory lookup / keyframe search / detection / segmentation
medium: orientation / monocular metric depth / object matching
expensive: multi-view reconstruction / novel-view render / geometry code
```

先固定工具版本，不同时优化工具精度。研究问题应是“同一工具池下，轨迹表示与训练是否更好”。

### 9.3 Baselines

| Baseline | 目的 |
|---|---|
| Base VLM / text CoT | 基础能力与纯文本预算 |
| Direct tool prompting | 工具可用但无技能/约束 |
| Think3D-style active view | 视角策略对照 |
| GCA-style formalization | 只加 `Ctask` |
| Skill-3D-style retrieval | 只加技能路由 |
| S-Agent-style experts | 只加分层 evidence compiler |
| GeoTrace-SFT | 检查轨迹监督本身 |
| GeoTrace-SFT + RL | 检查策略优化与克制调用 |

### 9.4 最有辨识力的消融

1. 去掉 `CR`，保留其他模块；
2. raw L2 3D evidence 直接喂模型 vs typed L3 evidence；
3. 轨迹只含 tool call vs 加 uncertainty/evidence need；
4. 去掉 verifier；
5. 去掉 no-tool/negative/counterfactual 数据；
6. 最终答案奖励 vs 条件 evidence reward；
7. 在线更新 skill library vs 离线阶段式更新；
8. 只报告 accuracy vs 加 TNG/CGF/IER 后重新排序模型。

第 8 项很可能产生最有意思的结论：某些模型 accuracy 很高，但工具因果性很低；另一些模型总分略低，却真正依赖并正确解释了 3D observation。

## 10. 研究方向优先级

| 方向 | 核心贡献 | 新颖性 | 可行性 | 影响 | 成本 | 风险 | 建议 |
|---|---|---:|---:|---:|---:|---:|---|
| **GeoTrace-Agent** | 学习 `Ctask → evidence need → tool → typed evidence → verifier`，并做反事实审计 | 5 | 4 | 5 | 3 | 3 | **主推** |
| 3D Tool Causality Benchmark | 系统构造 no-observation、frame/identity counterfactual | 5 | 5 | 4 | 2 | 2 | 可先做成资源/分析工作 |
| Dynamic Reference-Frame Agent | 学 `CR(t)` 与长视频/导航中的 frame transition | 5 | 3 | 5 | 4 | 4 | 第二阶段 |
| Provenance-aware 3D Memory | 对象 identity、view、pose、time、scale 的安全回看 | 4 | 3 | 5 | 4 | 3 | 与 S-Agent/PRCR 合流 |
| Physics-verifiable Tool Trajectory | 接 Code2Worlds/MPMWorlds/SimWorld 做物理 rollout | 5 | 2 | 5 | 5 | 5 | 高风险高回报，后续扩展 |

我建议先把 `GeoTrace-Agent + 3D Tool Causality Benchmark` 合成一篇：方法和评测互相支撑，避免只提出系统却无法证明工具真的被使用。

## 11. 论文叙事可以怎样成立

### Claim 1：3D spatial reasoning 的核心瓶颈是 evidence policy，而不只是模型容量

证据：普通小模型接工具收益有限；学习视角策略、技能路由或轨迹蒸馏后才显著提升。

### Claim 2：参考系和 typed evidence 是有效工具轨迹的必要中间表示

证据：GCA 的 `CR` 消融、S-Agent 的 L2→L3 跃升、REALM 的 persistent identity。

### Claim 3：现有 accuracy 不能证明模型使用了工具观察

证据：Reasoning Position paper；再用新建的 3D counterfactual suite 验证这一问题在空间任务中同样存在。

### Claim 4：GeoTrace 的训练同时改善答案、工具效率和证据因果性

需要实验同时支持：accuracy/ETU 提升、tool cost 下降、TNG/CGF/IER 提升，并在跨 benchmark 或跨工具替换中保持趋势。

### 最危险的过强主张

不要宣称“模型学会了通用 3D reasoning”或“轨迹是人类可解释因果链”。更安全、也更准确的表述是：

> 模型学会了在所测任务与工具池中生成更可执行、更节制、对关键 3D observation 更敏感的证据获取程序。

## 12. 失败模式与提前防御

| 风险 | 可能表现 | 防御 |
|---|---|---|
| Benchmark shortcut | 不看 observation 也答对 | hidden-target、no-observation、跨场景切分 |
| Tool reward hacking | 频繁调用便宜工具刷分 | 正确性门控 + evidence use + cost |
| Reference-frame hallucination | `CR` 文本合理但对象/轴绑定错 | 自动坐标真值检查 + frame counterfactual |
| Tool-chain error propagation | 错 mask/pose 被后续精确放大 | uncertainty、cross-view verifier、fallback |
| Teacher imitation | 只复制固定工具顺序 | 支持约束、同题多种有效轨迹、跨工具替换 |
| Skill library pollution | 失败经验被错误泛化 | 离线版本化、成功率/适用域/回退规则 |
| Synthetic overfitting | 在仿真坐标上强，真实图像弱 | 真值预训练 + 真实视频小规模校准 |
| 成本失控 | 重建和渲染吞掉所有收益 | 分层工具价格、selective planning、memory reuse |

## 13. 其余 3D 文献怎样接入这条主线

这些工作不是 GeoTrace-Agent 的首轮核心 baseline，但能自然形成后续任务分支：

| 工作 | 可接入位置 | 对主线的补充 |
|---|---|---|
| [A4-Agent](<3d agent/A4-Agent An Agentic Framework for Zero-Shot Affordance Reasoning/paper_DeepPaperNote.md>) | `intent → evidence need → part grounding` | 将高层任务意图与低层可操作区域解耦；适合把 typed evidence 从空间关系扩展到交互部件 |
| [CompassAD](<CompassAD - Intent-Driven 3D Affordance Grounding in Functionally Competing Objects.md>) | object/region identity verifier | 检查多个功能相似物体中，agent 是否根据意图绑定了正确实例与区域 |
| [DeepScan](<3d agent/DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models/paper_DeepPaperNote.md>) | L1 evidence search | 在启动昂贵 3D lifting 前，先提高二维局部证据的信噪比 |
| [MPMWorlds](<3d agent/MPMWorlds Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics/paper_DeepPaperNote.md>) | physics evidence / world-model verifier | 把“视觉状态估计”和“动力学外推”分开评测；避免漂亮视频掩盖物体坍缩与物理错误 |
| [Gamma-World](<3d agent/Gamma-World Generative Multi-Agent World Modeling Beyond Two Players/paper_DeepPaperNote.md>) | multi-agent identity / rollout memory | 当任务扩展到多智能体时，研究身份置换、交互一致性和跨 agent evidence routing |

它们共同说明，GeoTrace 的 typed evidence 不应永远局限于 `left/right/distance`。未来可以逐步扩展为：`affordance region`、`contact/support`、`material/dynamics`、`agent identity` 和 `counterfactual rollout outcome`。但首篇工作最好先守住静态/多视角空间证据，避免把创新点摊得太薄。

## 14. 最终 insight

把两组论文放在一起看，最重要的变化不是从 2D 走到 3D，而是从“回答问题”走到“管理证据”：

1. 3D 工具的独特价值，是能够产生原视图中没有的新观察；
2. 新观察必须锚定到 reference frame、object identity 和时间；
3. 原始几何必须被编译成任务级 typed evidence；
4. 轨迹训练必须包含 no-tool、失败、恢复和反事实样本；
5. reward 必须围绕答案与证据，不围绕工具表演；
6. 最终必须通过干预证明：模型不是在“演工具调用”，而是在用 3D observation 更新 belief。

因此，我对这条研究线的最终判断是：

> **下一代 3D agent 的核心资产不是更大的工具箱，而是一种可学习、可执行、可回放、可反事实审计的空间证据轨迹。**

这比“3D CoT”更严格，也更像一个可以被真正验证的研究对象。
