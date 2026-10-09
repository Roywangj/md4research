# 3D Agent Insight：基于 Skill-3D 教会模型调用 3D 工具

> 写作目标：基于 `Skill-3D` 思考一个可以推进成论文/项目的 3D agent 方向：不是简单“给模型更多工具”，而是训练模型学会在 3D 空间推理中**何时需要证据、需要什么证据、调用哪个 3D 工具、如何验证工具结果**。

## 0. 一句话 thesis

我认为最值得做的方向是：

> **把 Skill-3D 的“场景感知技能库”升级成“可验证的几何工具策略”：模型不直接学习调用 API，而是学习从问题生成 `参考系约束 → 证据需求 → 工具程序 → 关系专家输出 → 验证/回退` 的闭环。**

换句话说，真正要教会模型的不是“会用 GroundingDINO / Depth Anything / Pi3 / 渲染器”，而是：

1. 当前问题到底缺什么空间证据；
2. 这个证据必须在哪个参考系下定义；
3. 哪个工具链能以最低成本产生这个证据；
4. 工具返回的原始几何如何变成模型可读的关系；
5. 如果证据不够、矛盾或代价太高，应该如何回退。

这个方向可以暂命名为：

- `GeoSkill-Agent: Learning Verifiable 3D Tool Skills for Spatial Reasoning`
- `Skill3D-ToolGym: Teaching MLLMs to Call 3D Tools via Geometry-Grounded Skills`
- `3D Tool-Use Policy Learning for Agentic Spatial Reasoning`

我个人最喜欢第一个，短、直、像论文名。

## 1. 证据底座：现有论文各自给了什么

| Paper | 我从中提取的可复用部件 | 对这个方向的启发 |
|---|---|---|
| [Skill-3D](<3d agent/Skill-3D/paper_DeepPaperNote.md>) | Scene Memory、Skill Library、成功轨迹蒸馏、失败 lesson、ETU | 工具调用应当沉淀为可检索技能，而不是每道题临时规划。 |
| [Think3D](<3d agent/Think3D/paper_DeepPaperNote.md>) | 点云重建、新视角渲染、离散 3D 观察动作、RL 学视角策略 | 3D 工具最好被包装成语言模型可控制的离散观察动作。 |
| [S-Agent](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>) | L1/L2/L3 分层工具、双记忆、时空证据累积、S-300K 轨迹蒸馏 | 原始几何证据要经过专家转成任务化关系，否则会干扰模型。 |
| [Geometrically-Constrained Agent](<3d agent/Geometrically-Constrained Agent for Spatial Reasoning/paper_DeepPaperNote.md>) | `Ctask = (CR, CO)`，参考系约束、目标约束、变量绑定、公式库 | 3D tool-use 的第一步不是选工具，而是固定参考系和目标对象。 |
| [Thyme](<../Reasoning/Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>) | SFT + RL 两阶段、沙箱执行、外部观察不参与 loss、无需工具样本、工具成本约束 | 3D 工具调用训练可以照搬“协议冷启动 + 在线 RL 优化策略”的配方。 |
| [P3D-Bench](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>) | 可执行 3D 程序、几何/拓扑/结构分桶评测 | 如果输出是 3D 程序或结构，不能只看答案，要诊断几何与部件正确性。 |
| [Code2Worlds](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>) | 代码生成、仿真执行、视觉/运动 critic、闭环修正 | 3D agent 可以把工具结果放进可执行环境中反复 rollout 与修正。 |

### 关键判断

这些论文拼起来以后，最自然的下一步不是“Skill-3D + 更多工具”，而是：

> **把工具调用行为变成可训练、可验证、可诊断的中间策略。**

Skill-3D 已经证明了“技能检索 + 失败 lesson”能改善有效工具使用率；但它的技能更像自然语言 SOP。GCA 说明空间推理必须先有参考系契约；S-Agent 说明工具输出必须被转换成关系级证据；Thyme 说明工具策略需要专门训练，而不是只会生成代码/API。把这四件事合起来，就是一个更强的 3D agent 研究点。

## 2. 当前 gap：为什么 Skill-3D 还没有把问题做完

### Gap 1：技能是 SOP，但不是严格可执行的几何契约

Skill-3D 的技能可以告诉模型“这类场景通常先检测、再深度、再重建”，但空间问题里最容易错的是参考系。比如“坐在沙发上看电视，杯子在左边还是右边”，如果没有先定义：

- 谁是观察者；
- 朝向是什么；
- 左右相对于哪个局部坐标系；
- 杯子/电视/沙发分别绑定到哪个检测框或点云实例；

那么后面的深度和重建只是更精确地执行了一个可能错误的计划。

因此，Skill-3D 的 `skill` 应该升级为：

```text
skill = {
  trigger: 场景/任务触发条件,
  ctask: 参考系约束 CR + 目标约束 CO,
  evidence_need: 需要哪些证据,
  tool_program: 工具调用序列与参数,
  relation_expert: 如何把原始几何转成关系,
  verifier: 如何判断证据足够/一致,
  lesson: 失败模式与回退规则
}
```

这比“工具调用轨迹摘要”更接近可复用的空间推理程序。

### Gap 2：模型不擅长直接消费原始 3D 证据

S-Agent 的关键启发是：深度、点云、相机位姿本身不等于答案证据。很多时候，模型看到一堆坐标反而更乱。真正对 VLM 有用的是 L3 专家输出的任务化关系，例如：

- `object_A is 0.73m left-front of object_B under sofa-facing-TV frame`
- `candidate_2 is closer to the sink boundary than candidate_1`
- `the same chair appears in view_1 and view_3; do not double count`
- `the fridge is behind-right relative to the dishwasher-to-sink direction`

所以要教模型调用 3D 工具，不能只训练它输出工具名，还要训练它请求“答案级证据”。

### Gap 3：训练样本常常缺少 no-tool、wrong-tool、over-tool 的负例

3D 工具很贵，而且错误工具会制造强噪声。Thyme 的经验很重要：必须保留大量“无需工具，直接回答”的样本，否则模型会学到“调用工具 = 正确”的伪规律。

对 3D agent 来说，负例至少要包括：

- 不需要 3D 工具的问题；
- 用 2D 检测就够、不需要重建的问题；
- 必须重建/深度，检测框不够的问题；
- 参考系选错导致答案翻转的问题；
- 重复调用同一个视角但没有新增证据的问题；
- 工具输出正确但没有被最终答案使用的问题；
- 工具输出错误时，模型没有质疑而继续推理的问题。

这些负例比单纯增加成功轨迹更像“教会模型克制与诊断”。

### Gap 4：最终准确率不足以说明模型真的学会了工具调用

Skill-3D 的 ETU 是很好的起点，但还可以更细。一个 3D 工具 agent 至少应同时报告：

| Metric | 想测什么 |
|---|---|
| Answer Accuracy | 最终答对没有。 |
| Effective Tool Usage / ETU | 工具输出是否有效且被后续推理使用。 |
| Reference Frame Accuracy | 参考系是否定义正确，尤其是左右/前后/朝向问题。 |
| Evidence Sufficiency | 工具证据是否足以支持答案，而不是碰巧答对。 |
| Tool Cost / Latency | 平均工具调用次数、运行时间、重建次数。 |
| Counterfactual Tool Causality | 移除某个工具输出后答案是否改变，用来估计工具因果贡献。 |
| No-Tool Calibration | 简单问题上是否能不调用工具。 |
| Failure Taxonomy | 错在 formalize、grounding、depth、pose、code、verification 哪一步。 |

我会把 `Reference Frame Accuracy` 和 `No-Tool Calibration` 作为最容易形成差异化的两个指标。

## 3. 可投稿主线：GeoSkill-Agent

### 3.1 核心 idea

`GeoSkill-Agent` 的核心假设是：

> **3D 空间工具调用的可学习单元不是单个 tool call，而是“几何约束下的证据获取技能”。**

一个完整推理循环可以写成：

```text
Question + multi-view images/video
    → Scene/task parser
    → Ctask: reference frame CR + object constraint CO
    → Evidence need: distance / orientation / count / visibility / path / support / collision
    → Skill retrieval and selection
    → Tool program: detection / segmentation / depth / pose / point cloud / render / code
    → Relation expert: convert raw geometry into answer-grade relation
    → Verifier: enough? consistent? cheap enough?
    → Answer or fallback / lesson
```

这条链路的重点是中间的 `Ctask + evidence_need + verifier`。没有它，Skill-3D 容易退化成经验检索；有了它，技能就变成“可检查的空间工作流”。

### 3.2 系统结构

建议把工具分成四层，而不是一个扁平工具池：

| Layer | 工具/模块 | 输出 |
|---|---|---|
| L0: Task formalizer | 参考系解析、目标约束、任务类型分类 | `Ctask`, `evidence_need` |
| L1: Perception | keyframe search, GroundingDINO, SAM, OCR/label, object proposal | boxes, masks, candidates |
| L2: Geometry lifting | Depth Anything, Pi3/VGGT, camera pose, point cloud, new-view rendering | depth, pose, 3D coordinates, rendered view |
| L3: Spatial experts | distance, left/right/front/back, orientation, counting dedup, visibility, path/collision | answer-grade relation / scalar |
| L4: Verifier & memory | evidence sufficiency, contradiction check, cost check, failure lesson | final support or fallback |

这里的 L0 是我认为相对 Skill-3D 最应该补的一层。它把 GCA 的 `Ctask` 放在所有工具之前，避免 agent 在错误参考系里调用正确工具。

### 3.3 轨迹格式

训练样本可以采用统一的 agentic trace：

```xml
<scene_task>
  task_type: relative_direction
  objects: sofa, tv, cup
  evidence_need: object grounding + local reference frame + relative position
</scene_task>

<ctask>
  CR: origin = sofa_center; forward = sofa_to_tv_vector; right = cross(up, forward)
  CO: target = cup_instance; reference = sofa_instance
</ctask>

<skill_choice>
  skill_id: local_reference_relative_direction_v1
  reason: left/right depends on observer-facing frame, not image frame
</skill_choice>

<tool_call name="detect_objects">
  query: sofa, tv, cup
</tool_call>
<observation>
  external tool result, masked from language-model loss
</observation>

<tool_call name="estimate_depth_pose">
  targets: detected boxes
</tool_call>
<observation>
  external tool result, masked from language-model loss
</observation>

<expert_call name="relative_direction">
  reference_frame: sofa_to_tv
  target: cup
</expert_call>

<verify>
  evidence sufficient: yes
  no conflicting candidate: yes
  tool cost acceptable: yes
</verify>

<answer>
  The cup is on the left side relative to sitting on the sofa facing the TV.
</answer>
```

关键训练原则：`<observation>` 是环境返回，不应该让模型预测。SFT 时训练模型预测规划、工具调用、验证和答案；工具输出本身要 mask 掉。这一点直接借鉴 Thyme。

## 4. 数据构造：怎么教会模型

### 4.1 数据来源

我建议三路并行，不要只依赖 benchmark 题目：

| 来源 | 作用 | 最小可行规模 |
|---|---|---:|
| Existing benchmark trajectories | 在 VSI / MMSI / BLINK-MV / CV-3D 上生成 teacher 轨迹 | 1k-5k 条 |
| Synthetic 3D scenes | 自动得到真值坐标、参考系、遮挡、关系、工具正确答案 | 5k-20k 条 |
| Failure and counterfactual traces | 教模型识别错工具、错参考系、过度调用、证据不足 | 1k-3k 条 |

如果资源有限，我会先做一个 `500 sample debug set`：每类任务 50-100 条，保证能完整跑通工具、轨迹、评测和可视化。先把闭环做扎实，比堆数据更重要。

### 4.2 样本类型

数据要覆盖四类行为：

1. **Direct-answer samples**：不需要工具，训练 no-tool calibration。
2. **Single-tool samples**：检测、深度、朝向等单证据足够的问题。
3. **Multi-tool compositional samples**：必须检测 + 深度 + 参考系变换 + 专家计算的问题。
4. **Recovery samples**：第一次 grounding / depth / pose / reference frame 失败，agent 需要换工具或请求新视角。

其中第 4 类最有研究味道。很多工具 agent 只展示成功路径，但真正的 agent 能力来自“知道何时不信当前证据”。

### 4.3 Skill library 如何生成

从成功轨迹抽取：

```json
{
  "skill_id": "local_reference_relative_direction_v1",
  "trigger": {
    "task_type": "relative_direction",
    "language_cues": ["left", "right", "front", "behind", "facing", "from the viewpoint of"],
    "scene_cues": ["two or more anchored objects"]
  },
  "ctask_template": {
    "CR": "origin = reference object; forward = reference-to-anchor or object orientation",
    "CO": "bind target and reference objects to instances"
  },
  "tool_program": [
    "ground target/reference/anchor objects",
    "estimate 3D positions or depth",
    "construct local coordinate frame",
    "call relative_direction_expert"
  ],
  "verifier": [
    "all required objects grounded",
    "reference frame vector has non-trivial length",
    "target has unique instance or resolved candidate",
    "relation expert returns stable answer"
  ],
  "failure_lessons": [
    "do not answer left/right in image coordinates when language specifies a viewer/object frame",
    "if multiple candidate cups exist, ask detection+segmentation or choose by task constraint"
  ]
}
```

从失败轨迹抽取：

- `wrong_reference_frame`
- `missing_object_binding`
- `depth_noise`
- `pose_inconsistent`
- `duplicate_counting`
- `unnecessary_reconstruction`
- `ignored_tool_output`
- `tool_output_not_answer_supporting`

这些 failure lessons 应进入检索和 reward，而不是只留在日志里。

## 5. 训练方案

### 5.1 Stage 1：协议冷启动 SFT

目标：让模型稳定输出结构化的 `Ctask / skill / tool_call / verify / answer`。

训练内容：

- 任务类型判断；
- 参考系约束生成；
- 工具选择和参数；
- 读取工具观察后的下一步规划；
- 最终答案格式；
- no-tool 决策。

注意：

- 外部工具观察要 mask；
- 多轮轨迹可以只监督最后一轮决策，降低上下文噪声；
- 工具参数、代码、JSON 应使用低温或确定性解码；
- 自然语言规划可以保留采样，用于探索多种工具路径。

### 5.2 Stage 2：GRPO / RL 学策略

目标：让模型在成本、证据和答案之间学权衡。

奖励可以设计为：

```text
R = R_answer
  + λ1 R_reference_frame
  + λ2 R_evidence_usage
  + λ3 R_verification
  + λ4 R_no_tool_calibration
  - λ5 Cost_tools
  - λ6 Redundant_calls
  - λ7 Hallucinated_evidence
```

各项含义：

| Reward | 说明 |
|---|---|
| `R_answer` | 最终答案正确。 |
| `R_reference_frame` | `CR` 是否匹配题目参考系。 |
| `R_evidence_usage` | 工具证据是否被最终推理实际使用，类似 ETU。 |
| `R_verification` | 证据足够性和一致性检查是否通过。 |
| `R_no_tool_calibration` | 简单题不调用昂贵工具也给奖励。 |
| `Cost_tools` | 重建、渲染、多轮工具调用成本惩罚。 |
| `Redundant_calls` | 重复调用没有新增证据的工具。 |
| `Hallucinated_evidence` | 声称看到/算到工具没有返回的证据。 |

这比只用最终答案奖励更稳，因为最终答案奖励很容易让模型学到 benchmark 偏置，而不是学会工具策略。

### 5.3 Stage 3：技能迭代，但不要在线无限更新

Skill-3D 的训练稳定性提示：在线更新技能库会引入非平稳性。我的建议是阶段式迭代：

1. 固定 skill library 训练一版 policy；
2. 用 policy rollout 新轨迹；
3. 离线筛选成功/失败轨迹，更新 skill library；
4. 再训练下一版 policy。

也就是 `library → policy → rollout → library` 的离线循环，而不是训练过程中边跑边改检索对象。

## 6. 实验设计

### 6.1 最近 baseline

| Baseline | 要比较什么 |
|---|---|
| No tool VLM | 基础空间推理能力。 |
| Direct tool prompting | 给工具但无技能/无约束。 |
| Think3D-style active view | 是否主要来自新视角/点云操作。 |
| Skill-3D-style skill retrieval | 是否主要来自技能检索。 |
| GCA-style constraint only | 是否主要来自参考系形式化。 |
| S-Agent-style layered experts | 是否主要来自 L1/L2/L3 专家化证据。 |
| GeoSkill-Agent full | 技能 + 约束 + 专家 + 验证 + RL 是否互补。 |

### 6.2 Ablation

最关键的消融不是“少一个工具”，而是少一个中间机制：

| Ablation | 预期暴露的问题 |
|---|---|
| w/o `Ctask` | 左右/前后/朝向类问题明显下降。 |
| w/o L3 relation expert | 原始深度/点云难以被 VLM 正确使用。 |
| w/o failure lessons | 同类错误反复出现，尤其 duplicate count / wrong frame。 |
| w/o no-tool samples | 工具过度调用，简单题成本上升甚至退化。 |
| w/o observation masking | 模型浪费容量预测工具输出，策略边界混乱。 |
| w/o cost reward | 准确率可能升但延迟和重建次数不可接受。 |
| w/o verifier | 工具输出错误时更容易被盲信。 |
| SFT only vs SFT+RL | 是否真的学到成本敏感的工具策略。 |

### 6.3 指标和诊断面板

建议每次实验保存一个诊断表：

| Field | Example |
|---|---|
| question_id | `vsi_000123` |
| task_type | `relative_direction` |
| reference_frame_correct | yes/no |
| selected_skill | `local_reference_relative_direction_v1` |
| tools_called | `detect → depth → relation_expert` |
| tool_cost_sec | `4.3` |
| evidence_used | yes/no |
| verifier_pass | yes/no |
| answer_correct | yes/no |
| failure_type | `wrong_reference_frame / grounding_fail / over_tool / no_failure` |

这个诊断面板会让论文更像“agent 机制研究”，而不是只报一个准确率表。

## 7. Idea incubator：可以落地的四个方向

| Type | Direction | Hypothesis | Minimal experiment | Positive signal | Negative result meaning | Cost | Risk |
|---|---|---|---|---|---|---:|---:|
| Low-cost | `Skill-3D + Ctask` 中间表示 | 给 Skill-3D 加参考系约束能减少左右/朝向错误 | 在 100-300 个 VSI/MMSI 题上，让 teacher 先生成 `Ctask` 再选工具 | 方向/参考系子任务明显提升，错误类型从 wrong frame 下降 | 错误主要来自工具感知而非参考系 | low | med |
| Workshop-scale | `3D ToolGym` 小型合成训练集 | 合成场景能提供干净的工具真值和失败负例 | Blender/已有场景生成 1k-5k 带坐标真值的相对位置/距离/计数题 | 小模型学会 no-tool 与 tool-use 的切换 | 合成到真实 gap 太大，需要真实轨迹蒸馏 | med | med |
| Main-paper | `GeoSkill-Agent` | 几何约束技能 + L3 专家 + RL 比单独 Skill-3D/GCA/S-Agent 更稳 | Qwen-VL 4B/8B，SFT + GRPO，在 3-5 个 benchmark 上跑完整消融 | Accuracy、ETU、Reference Frame Accuracy、Cost 同时更优 | 多机制过重，收益可能被强 teacher 掩盖 | high | med |
| High-risk/high-reward | Online evolving 3D skill memory | agent 能在新环境中把失败转成可复用技能 | 长视频/机器人模拟环境中连续 rollout，阶段式更新技能库 | 新场景样本越多，工具失败率下降 | 非平稳、记忆污染、评测难 | high | high |

我建议优先做第 1 个和第 3 个之间的路线：先小规模验证 `Ctask` 是否能补 Skill-3D 的短板，再扩成完整 `GeoSkill-Agent`。

## 8. 最小验证计划

### Week 1：做一个离线诊断原型

目标不是训练，而是证明中间表示有用。

交付：

- 选 100-200 个空间推理样本；
- 手动/teacher 生成 `Ctask`；
- 记录原始 Skill-3D 风格工具流程；
- 加入 `reference_frame_expert` 和 `relative_direction_expert`；
- 对比有无 `Ctask` 的 wrong-frame 错误率。

成功标准：

- 左右/前后/朝向类问题的错误类型可解释下降；
- 日志能显示“原来错在图像坐标，现在转到对象/观察者坐标”。

### Week 2-3：构造 500 条 agentic trace

交付：

- 100 条 no-tool；
- 150 条 single-tool；
- 150 条 multi-tool；
- 100 条 recovery/failure；
- 每条都有 `Ctask / evidence_need / tool_call / observation / expert / verify / answer`。

成功标准：

- 轨迹能被自动 replay；
- 工具观察可 mask；
- 每条能归因到一个 success skill 或 failure lesson。

### Week 4：SFT 一个 4B/8B 小模型

目标：先看模型是否学会格式和基本工具路由。

指标：

- tool-call format success；
- reference-frame parse accuracy；
- no-tool calibration；
- average tool calls；
- answer accuracy。

### Week 5+：RL / GRPO

只在 SFT 稳定后做。不要一开始就 RL。RL 的作用是优化成本和证据使用，而不是救格式崩坏。

## 9. 我认为最可能写成论文的贡献点

### Contribution 1：Geometry-grounded skill representation

把 Skill-3D 的自然语言技能升级为包含 `Ctask / evidence_need / verifier / failure_lesson` 的结构化技能。

这能和已有工作形成清晰差异：

- Skill-3D：技能检索与演化；
- GCA：单题几何约束；
- 你的方向：把几何约束放进可学习技能，使工具策略可复用、可验证。

### Contribution 2：Answer-grade 3D evidence

证明原始 3D 输出不如“关系专家输出”有效。也就是：

> depth/point cloud/pose are not the evidence; task-conditioned relations are the evidence.

这个可以通过 w/o L3 expert 消融验证。

### Contribution 3：Tool-use policy training recipe for 3D

借鉴 Thyme，但把二维代码工具换成 3D 工具：

- observation masking；
- no-tool data；
- deterministic tool parameters；
- cost-aware reward；
- consistency / verifier reward；
- failure lessons。

如果能把这套训练配方讲清楚，就不是简单拼工具，而是一篇“如何训练 3D tool-use agent”的方法论文。

### Contribution 4：Better diagnostics beyond accuracy

提出或系统化一组 3D tool-use 诊断指标：

- `Reference Frame Accuracy`
- `Evidence Sufficiency`
- `No-Tool Calibration`
- `Counterfactual Tool Causality`
- `ETU@Cost`

这会让文章更容易说服人，因为很多 agent 论文最大的问题就是“最后答对了，但不知道工具有没有真的起作用”。

## 10. 风险与规避

| Risk | 为什么危险 | 规避 |
|---|---|---|
| 工具质量决定上限 | 深度/重建错了，技能再好也会错 | 记录工具置信度，加入 verifier 与 fallback。 |
| 机制太重 | Skill + Ctask + expert + verifier + RL 可能显得复杂 | 先用 ablation 证明每层解决不同错误。 |
| teacher bias | 轨迹可能学到强 teacher 的偏好 | 加合成真值、负例和 counterfactual。 |
| benchmark leakage/style | 技能可能过拟合 VSI/MMSI 题型 | 做跨 benchmark 和合成到真实迁移。 |
| 成本过高 | 3D 重建/渲染慢 | 报 ETU@Cost，奖励中惩罚昂贵工具。 |
| no-tool 能力退化 | 模型误以为 agent 必须调用工具 | 数据中保留大量 direct-answer 样本。 |

## 11. 我现在的结论

如果要基于 Skill-3D 做自己的 3D agent，我不会把主创新放在“再接一个更强的 3D 工具”上。更好的切入点是：

> **教模型把空间问题分解为可验证的几何证据需求，并学习成本敏感的工具策略。**

具体来说，我会做：

1. 用 GCA 的 `Ctask` 锁住参考系；
2. 用 Skill-3D 的 `Skill Library` 复用工具工作流；
3. 用 S-Agent 的 L3 专家把原始几何变成答案级关系；
4. 用 Thyme 的 SFT + RL 配方训练“何时调用/何时不调用/何时回退”；
5. 用 ETU、Reference Frame Accuracy、No-Tool Calibration 和 Cost 证明不是工具崇拜。

这个方向的卖点很清楚：

> **从“工具增强 3D 推理”推进到“可训练的 3D 工具使用策略”。**

它和 Skill-3D 足够近，容易承接；又和 Skill-3D 不完全重合，因为你的核心会落在“几何约束 + 证据验证 + 策略训练”。

## 12. 来源与链接

- Skill-3D: [本地精读](<3d agent/Skill-3D/paper_DeepPaperNote.md>)；arXiv: [2606.07436](https://arxiv.org/abs/2606.07436)；项目页: [skill-3d.github.io](https://skill-3d.github.io/)
- Think3D: [本地精读](<3d agent/Think3D/paper_DeepPaperNote.md>)；arXiv: [2601.13029](https://arxiv.org/abs/2601.13029)
- S-Agent: [本地精读](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>)；arXiv: [2606.20515](https://arxiv.org/abs/2606.20515)
- Geometrically-Constrained Agent: [本地精读](<3d agent/Geometrically-Constrained Agent for Spatial Reasoning/paper_DeepPaperNote.md>)；arXiv: [2511.22659](https://arxiv.org/abs/2511.22659)
- Thyme: [本地精读](<../Reasoning/Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>)；arXiv: [2508.11630](https://arxiv.org/abs/2508.11630)；项目页: [thyme-vl.github.io](https://thyme-vl.github.io/)
- P3D-Bench: [本地精读](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>)；arXiv: [2606.11152](https://arxiv.org/abs/2606.11152)
- Code2Worlds: [本地精读](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>)
