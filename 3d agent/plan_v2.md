# 3D Agentic RL 项目计划 v2.1

> 基于 plan.md 的 7 条框架，综合 Overall.md、三版 3d_insight（GeoSkill-Agent → Oracle3D-Gym → 机制/脚手架判决）、Skill-3D / S-Agent 学习笔记与 GEM 实验线整理。
> v2.1：经 Mac codex（codex-cli 0.142.4）批判性审阅后修订，采纳/驳回记录见文末 §7。
> 目标：workshop 级别成果；训练在外部 GPU 机器完成；模型锚定 Qwen3-VL-4B。
> 日期：2026-07-08

---

## 0. 核心命题（thesis）

**用引擎真值建立 3D 工具调用的反事实审计协议：判定工具调用何时是因果机制、何时只是训练/推理脚手架；并在因果必要子集上，用最小可验证奖励的 GRPO 验证"答案门控 RL 能否改善 4B 模型的工具策略"。**

结构（单主干，不是三篇论文并列）：

- **主贡献**：engine-verified counterfactual audit protocol——推理时删除/扰动工具观察，测量答案翻转率，与表面 ETU 对照出"裂口表"。3D 领域没人做过这个自查。
- **验证实验（RL，项目硬要求）**：在协议判定的因果必要子集上训练 Qwen3-VL-4B，检验 RL 是否提升"该调时调、不该调时不调"的工具策略。协议决定 RL 优化什么，先判决后训练。
- **协议的自然产物**：Reference Frame Accuracy、No-Tool Calibration、反事实必要率、成本列——作为审计输出报告，不单独立为贡献。

注意措辞：不承诺"证明学到机制"。脚手架占主同样是有效结论（→ 蒸馏无工具部署版 + 最小工具链 agent，主打成本结论）。

为什么是这个命题：
- 三版 insight 已收敛：框架部件清单（Ctask 第 0 层、L3 翻译层、masking、负例、反事实指标）稳定复现，差异化在**真值底座 + 因果协议 + 训练配方**，不在再提一个新框架。
- 你的 GEM 线（"带解读键的表示有用、无解读键的裸坐标≈噪声"）提供机制级证据，直接决定 observation 表示设计，且被 S-Agent 的 L3 消融（+L2 仅 +0.8，+L3 +6.9）从架构层独立印证。
- Think3D-RL（SPAgent 仓库）+ Skill-3D 官方 4B 量级（4 卡、SFT ~3h + RL ~28h、500+1k 样本）证明训练在你的外部机器上可行。

**主张范围（诚实边界）**：论文对象限定为 Think3D-style 主动 3D 工具链 + Qwen3-VL-4B。Skill-3D / S-Agent 的数字作为文献语境引用，不作为自己拥有的 baseline——不用没跑过的 baseline 承担主论证。

---

## 1. 已有资产盘点（起点不是零）

| 资产                                 | 状态                   | 用途                                                                            |
| ---------------------------------- | -------------------- | ----------------------------------------------------------------------------- |
| SPAgent/Think3D 官方仓库（Linux 开发机）    | 已在手                  | agent 循环、Pi3/VGGT 工具、quick_eval（BLINK/MindCube/VSI）、ms-swift GRPO 脚本——训练与评测基建 |
| MMSI/VSI 评测 harness                | 已跑通，且发现过 scoring bug | 冻结子集锚点；先统一计分口径                                                                |
| GroundingDINO + DA3METRIC-LARGE 权重 | 本地 checkpoints/ 已下载  | noisy-tool 层的感知与深度                                                            |
| GEM training-free 机制结论             | 已有实验                 | typed evidence 字段设计依据；表示对照探针                                                  |
| 12 篇精读 + 三版 insight                | 已完成                  | related work 与 motivation 基本成稿                                                |
| 训练算力                               | 外部机器                 | 两臂 GRPO（带工具/不带工具）≈ 2×~30h 可承受                                                 |

---

## 2. 阶段计划（约 14 周，第 6 周硬门控）

### Phase 0 · 基建与基线（第 1–3 周）→ 原计划第 1 条

- SPAgent 仓库跑通 Think3D 评测：mock 冒烟 → 部署 Pi3 → Qwen3-VL-4B 复现 BLINK-MV / MindCube 趋势。
- 用已有权重搭 L3 专家最小版：**只做相对方向 + 度量距离两类**（计数、朝向推迟，见 §5 砍单）。
- MMSI 统一计分口径（对照你记录的 harness bug）；确定冻结真实域子集（VSI/MMSI/MindCube 各固定 ~100–200 题），**只在里程碑测**（Phase 1 末、Phase 3 末），不随每个实验跑。
- 训练机运维打底：环境镜像、数据同步方式、checkpoint/seed/失败重跑预算（列为工程风险，见 §4）。
- **产出**：同一模型、同一计分的 baseline 表（no-tool / Think3D-style / L3-expert-style）。
- **成功标准**：复现"4B 裸工具增益 ≈ +0~1"（Think3D 论文观察）——RL 的动机实验，直接进论文。

### Phase 1 · 零训练反事实审计（第 3–6 周）★ 论文分析主体

- Blender/Infinigen 脚本生成 100–200 个场景：完整几何真值 + 由真值反向生成的问题 + 证据规范（参考系、所需几何量、最小工具链）+ 四类免费负例（no-tool/wrong-tool/over-tool/wrong-frame）。不碰 UE5。
- **双层感知设置（分表报告，不许混）**：
  - **oracle-perception 层**：把真值检测/深度直接喂给工具链，隔离"工具因果性"本身——测机制上限；
  - **noisy-tool 层**：真实 GroundingDINO + DA3——测现实退化。
  - 理由：若渲染质量差导致感知工具崩溃，混测会把"感知失败"误判成"工具无因果"。
- 三组干预（对成功轨迹）：
  1. **推理时删除工具观察** → 答案翻转率；
  2. **程序化扰动**：深度置换 ±20%、参考系旋转 90°、实例错绑 → 敏感性；
  3. **表示对照**：同一几何证据以"无解读键裸坐标 vs typed evidence"两种形式注入（GEM 探针正式化）。
- **主指标用二分**：counterfactually necessary vs not。(a) 构造性必要 /(b) 分辨率必要 /(c) 便利性 只作为分析标签（(b)(c) 依赖模型先验，无法仅凭几何真值自动判）。(a) 类子集仍按构造保证（遮挡/背面题），供 Phase 4 使用。
- **答案先验控制**：选择题选项做 label balancing，报告高于随机基线的净增益，防"删观察靠猜分不掉"的假阴性。
- **产出**：裂口表（表面 ETU vs 反事实翻转率）× 双层设置 + 表示对照曲线 + 冻结真实域子集上的迁移快照。
- **发表前提（不预设"必可发表"）**：协议严（扰动有应然标签）、baseline 公平（同模型同口径）、双层分表——三者是 Phase 1 的验收标准。
- **决策点 D1**：审计结果决定 RL 优化目标——机制占主 → 训"视角/工具选择"；脚手架占主 → 训"门控/停止 + 蒸馏无工具版"。

### ⛔ 硬门控（第 6 周末）

**若"场景真值 → 问题 → 工具轨迹 → 反事实扰动 → 自动评分"闭环仍不稳定：立即砍掉 RL，Phase 1 扩写为 analysis paper 收尾。**这是 codex 审稿的核心建议，采纳为不可协商的止损线。

### Phase 2 · 轨迹数据构造（第 6–8 周）→ 原计划第 2、3 条

- 任务套件（合成域）：**相对方向 + 度量距离**各 150–200 题；计数/朝向留作 future work。
- **500 条 debug 轨迹**：~150 no-tool + ~200 single-tool + ~150 multi-tool；recovery 轨迹降为**少量定性案例**（不作为主数据比例）。
- 轨迹格式：XML trace——`<ctask> → <tool_call> → <observation>（typed evidence，mask 出 loss）→ <verify> → <answer>`。
- **typed evidence 的准确定义**（对 codex 意见的澄清，与 GEM 结论一致）：关系词 **+ 带单位/参考系/来源/置信度的标量**（如 `dist(A,B)=1.4m, frame=cam2, src=DA3, conf=0.87`）。禁止的是**无解读键的裸坐标矩阵**，不是数值本身——距离/尺度任务必须有数。原始渲染图不进上下文。
- **监督分阶段**（codex 意见与可行域思想的调和）：
  - SFT 阶段：teacher 给 **canonical 完整轨迹**（行为克隆，4B 需要稳定格式冷启动）；
  - RL 阶段：teacher 降级为**可行域约束**（奖励只查必要证据满足 + 禁止行为，不强制工具顺序）。
- teacher 轨迹用**引擎真值过滤**（不是用更强模型过滤）——规避 GPT 同源耦合。
- S-300K 三粒度放大：**砍掉**，列 future work。

### Phase 3 · SFT + 两臂 GRPO（第 8–11 周，训练机）→ 原计划第 4 条 + RL 核心

- **SFT**：canonical 轨迹行为克隆；observation mask；验收：tool-call 格式成功率、参考系解析准确率、no-tool calibration、平均调用次数。
- **GRPO 两臂**（这同时就是缩减版四象限的训练轴）：
  - 臂 A：带工具训练（主实验）；
  - 臂 B：无工具标准 GRPO（对照，Think3D 论文本来就需要这个 control）。
  - 推理轴 {±工具观察删除} 是纯评测操作，零训练成本——四象限由 2 次训练 + 4 次评测构成，不是 4 次训练。
- **奖励从最小版起步**（codex 意见采纳，防多项 λ 的 hacking 空间）：

  ```
  R = R_ans · 1[必要证据满足] − λ·Cost_tools
  ```

  R_frame / 冗余惩罚 / R_fmt 先作为 **hard constraint 或诊断字段**；完整门控复合奖励 `R_ans·(1+λ1·R_frame+λ2·R_exec)+...` 降为**一条消融**而非默认。必要证据由**冻结解析器 + 引擎真值**判定（防 reward hacking）。
- 训练细节：8 rollouts、KL β≈0.05、预计算所有场景几何（训练时零重建）、observation token mask。
- 健康信号：调用频率下降 + 方差保留（不是调用变多）；预期"先降轮数掉分、再学会花轮数换正确率"的动态。
- **砍掉**：8B 规模趋势。**engine-reward vs GPT-裁判-reward 对照降为 P2**：仅当第 9 周前臂 A 已稳定收敛才做小规模版（500 样本单次），否则写 future work——它是好问题，但不承担本篇主论证。

### Phase 4 · 判决评测与消融（第 11–13 周）→ 原计划第 5、6 条

- **缩减版四象限**：{臂 A / 臂 B} × {推理时保留/删除工具观察}，分别在 (a) 类保证组与普通组上测。预期"普通组删观察不掉分 + (a) 类组显著掉分"同时出现是最好结局；任一单边结果也可解释。
- **核心消融只保 4 个**：−typed evidence（退回裸坐标）/ −no-tool 负例 / −observation masking / 最小奖励 vs 门控复合奖励。其余（−Ctask、−成本项、SFT-only）作为诊断字段顺带报告，不单独跑全表。
- 逐题诊断面板（task_type / reference_frame_correct / tools_called / tool_cost_sec / evidence_used / verifier_pass / answer_correct / failure_type）+ failure taxonomy。
- **成本列必报**：平均工具秒数/轮数/token（领域沉默项；锚点：Pi3 ~21s vs 深度 ~1s）。熵门控的"省 60–70% token"**不引用为本项目主张**，除非自己实测。

### Phase 5 · 写作与查新（第 13–14 周）→ 原计划第 7 条

- 主线标题方向：*Mechanism or Scaffold? An Engine-Verified Counterfactual Audit of 3D Tool-Use (with an RL Case Study)*。
- 叙事骨架：动机（4B 裸工具 +0.8）→ 审计协议与裂口表（双层设置）→ 判决 → 在判决子集上的两臂 RL 验证 → 成本诚实。
- **投稿前系统查新**：arXiv/OpenReview/项目页扫"counterfactual tool-use / 3D agent audit"——"确定没人做"不写死，撞车则差异化锚定引擎真值 + 训练侧判决。
- 降级方案已在第 6 周门控内建：analysis paper 收尾。

---

## 3. 关键设计决策速查

| 决策 | 依据 |
|---|---|
| 先判决后训练：协议决定 RL 优化什么 | 修正 v2 的逻辑倒置（codex 审稿#1） |
| oracle-perception / noisy-tool 双层分表 | 防止感知崩溃污染因果结论（codex #4） |
| 主指标二分（必要/非必要），(a)(b)(c) 降为标签 | (b)(c) 依赖模型先验不可自动标（codex #5） |
| SFT 冷启动必须有，且用 canonical 轨迹 | DeepEyesV2 直接 RL 失败；4B 格式稳定性（codex 反对意见采纳） |
| 可行域监督放 RL 阶段，不放 SFT | 调和 PFlowNet 思想与冷启动需要 |
| 奖励最小版起步，复合门控为消融 | 多项 λ 有 hacking 空间（codex #6）；工具奖励仍须被答案门控（DeepEyes 75.1 vs 72.1） |
| observation = typed evidence（关系词+带解读键标量），禁裸坐标矩阵 | GEM 结论 + S-Agent L3 消融 + MINT-CoT 64→40 |
| teacher 轨迹引擎真值过滤 | 解 GPT 同源耦合 |
| RL 期间冻结解析器/技能配置 | Skill-3D Fig 5 非平稳性 |
| 真实域 = 冻结子集、里程碑测 | 保迁移证据但不拖节奏（codex 意见折中） |
| observation token mask 出 loss | 防伪造证据 |

## 4. 风险与对策（含 codex 补充）

| 风险 | 对策 |
|---|---|
| 合成→真实 gap（最大风险） | 双层设置 + 冻结真实域子集里程碑测；引擎真值与真实 benchmark 标签空间不一致时，只主张协议结论、不主张迁移增益 |
| Phase 0–1 工程量被低估 | 时间线已放宽（0 用 3 周、1 用 3 周）+ 第 6 周硬门控止损 |
| 多模态 GRPO 工程风险（ms-swift + tool trace masking + XML 稳定性） | Phase 0 即在训练机做 8 样本 dry-run；XML 解析失败率纳入 SFT 验收 |
| 训练机运维（环境/同步/checkpoint/seed/重跑预算） | Phase 0 打底；每臂预留 1 次完整重跑预算 |
| 选择题答案先验抬高 no-observation 分数 | label balancing + 报告高于随机的净增益 |
| reward hacking | 最小奖励 + 冻结解析器判定必要证据 + 负例进训练集 |
| 弱 planner 反向（4B 套框架掉分） | 先 SFT 再上框架；Phase 0 先确认基线现象 |
| 计分口径污染对照 | Phase 0 统一 MMSI 口径 |
| 工程量失控 | 只 Blender 脚本化；任务只做两类；500 条 debug 先行 |
| "只是造了数据集"的评审风险 | 主贡献锚定反事实协议的分析性结论 |
| 撞车 | 投稿前系统查新；差异化=引擎真值+训练侧判决 |

## 5. 明确砍掉 / 降级清单（scope cut）

| 项 | 处置 |
|---|---|
| 8B 规模趋势 | 砍，future work |
| S-300K 三粒度放大 | 砍，future work |
| engine vs GPT-judge 奖励对照 | 降 P2：第 9 周前臂 A 稳定才做小版，否则 future work |
| 跨视角计数、朝向任务 | 推迟，先做相对方向+距离 |
| recovery 轨迹为主数据 | 降为定性案例 |
| 全量消融矩阵（7 项） | 核心 4 项，其余诊断字段 |
| 熵门控节省主张 | 不引用，除非实测 |
| 每实验全真实域覆盖 | 冻结子集、里程碑测 |
| Skill-3D 全量复现（技能库工程） | 不做；其数字作文献语境，主张范围收窄到 Think3D-style |

## 6. 与原 plan.md 七条的映射

| 原计划 | 落位 |
|---|---|
| 1. 复现 baseline | Phase 0（Think3D 官方仓库；L3 专家最小版；Skill-3D/S-Agent 仅文献引用） |
| 2. 自定义 3D 小任务 | Phase 1–2（两类任务 + 证据规范 + 负例） |
| 3. 构造轨迹数据 | Phase 2（500 debug，引擎过滤，分阶段监督） |
| 4. planner + tools + memory 原型 | Phase 0 planner+tools；memory 降为 provenance 记录 |
| 5. ablation | Phase 4（核心 4 项 + 缩减四象限） |
| 6. failure case 分析 | Phase 1 审计 + Phase 4 诊断面板 |
| 7. 技术报告 / workshop | Phase 5（主线 + 内建降级） |

## 7. codex 审阅的采纳/驳回记录（v2 → v2.1）

**采纳**：
1. 命题重写——不预设"证明是机制"，改为判定协议 +条件化 RL 验证（codex #1、内在一致性批评）；
2. 单主干结构——反事实协议为主贡献，指标降为协议产物（#2）；
3. 时间线放宽 + 第 6 周硬门控（#3）；
4. oracle-perception / noisy-tool 双层分表（#4，本轮最有价值的意见）；
5. 主指标二分，(a)(b)(c) 降为分析标签（#5）；
6. 奖励最小版起步，复合门控降为消融（#6）；
7. 主张范围收窄到 Think3D-style + 4B，不用没跑过的 baseline 承担论证（#7）；
8. 砍单全部采纳（8B、S-300K、任务收窄、recovery 降级、熵门控主张、消融收窄）；
9. SFT 用 canonical 轨迹，可行域监督移到 RL 阶段；
10. 补充风险：GRPO 工程、训练机运维、答案先验控制、标签空间不一致、投稿前查新；
11. "Phase 1 必可发表"改为带验收前提的条件判断。

**有保留（未照单全收）**：
1. **RL 不降为"最多 follow-up"**——项目硬要求是 3D agentic RL；折中为"协议主干上的核心验证实验"，两臂训练规模可控（2×~30h）；
2. **四象限保留缩减版**——codex 高估了成本：推理轴是纯评测，训练轴两臂本来就是实验组+对照组，实际 = 2 次训练 + 4 次评测；
3. **真实域迁移列不全砍**——sim2real 是自家笔记标注的最大风险，全砍会回到"只在合成域自嗨"；折中为冻结子集里程碑测；
4. **"关系词太绝对"是误读而非分歧**——GEM 原结论就是"带解读键的自然语言"，禁的是无解读键裸坐标矩阵；v2.1 把 typed evidence 定义写死（关系词 + 带单位/参考系/来源/置信度的标量），距离/尺度任务当然有数。

## 8. 本周可动手的三件事

1. SPAgent 仓库跑 mock 冒烟 + 部署 Pi3，在 MindCube 120 题上出第一行 4B baseline 数字；
2. 写第一个 Blender 场景脚本（3–5 个带朝向家具 + 真值 JSON + 4 个环拍视角），一条龙生成"相对方向"题——同时导出 oracle-perception 层所需的真值检测/深度通道；
3. 把 GEM 的 typed evidence JSON schema 定稿（相对方向/距离两类先行：关系词 + 单位 + 参考系 + 来源 + 置信度字段）——它是 Phase 1 表示对照的自变量和 Phase 2 的 observation 格式。
