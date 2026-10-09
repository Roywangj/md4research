# 3D Insight 合并版：GeoSkill 骨架 × Oracle 底座，按最短投稿路径重排

> 写作时间：2026-07-03。合并 [3d_insight](<3d_insight.md>)（GPT 版：GeoSkill-Agent，框架语法最全）与 [3d_insight_fable5](<3d_insight_fable5.md>)（Fable 5 版：Oracle-Grounded 3D Tool-Use，判决与底座）。合并原则沿用本目录各 `_all` 版的做法：逐项裁决，不平均（§1）。
>
> **与其他文档的分工**：[3d_insight_with_reasoning_all](<3d_insight_with_reasoning_all.md>) 是 3D×Reasoning 融合的判决书 + Skill-3D/Think3D/S-Agent 三 baseline 落地专章；[Agentic_world_all](<Agentic_world_all.md>) 是生成端路线。本篇是**理解端主线两版的裁决合并 + 投稿时间表**。三份文档现在指向同一个第一实验（§0.4），这不是巧合，是收敛。

---

## 0. TL;DR：五个判断

1. **两版真正的分歧只有一处，必须裁决而不能并存**：GPT 版把主贡献押在 agent 框架（GeoSkill-Agent：技能=可验证几何契约），我押在底座（Oracle3D-Gym：引擎替代 GPT 当 oracle）。裁决：**框架当骨架用，底座当贡献卖**。理由：框架部件（Ctask 第 0 层、L3 专家、observation masking、no-tool 负例、反事实指标）已被三次独立综合收敛到同一清单——收敛意味着稳健，也意味着 novelty 弱；而底座一次性解决四个系统性弱点（工具因果从未被测、教师/评审/被测同源耦合、泛化主张普遍弱于表述、成本沉默），且是唯一能让 GPT 版自己提出的新指标变得可测的东西（见第 3 条）。
2. **GPT 版三件最有价值的资产，全盘采纳**：①技能的结构化契约 `{trigger, ctask, evidence_need, tool_program, relation_expert, verifier, lesson}`——这是两版的最大公约数，比 Skill-3D 的自然语言 SOP 强一档；②四类样本税表（direct-answer / single-tool / multi-tool / **recovery**），其中 recovery（第一次 grounding/depth/frame 失败后换路）最有研究味，且现有工作只展示成功路径；③逐题诊断面板（frame 对错 / 所选技能 / 工具链 / 成本 / verifier / 失败类型）——它把论文从"报一个准确率表"变成"agent 机制研究"。
3. **两个不盲从**。①**拒绝七项 λ 奖励**（R_answer + λ1..λ7）：Thyme 自己的消融就是反例——加过程奖励从 63.59 掉到 62.91，一致性奖励反而最高 65.68（Table 5/6）；Skill-3D 的成功配方是最简三项 `R_ans + R_fmt + (R_exec − |A|/B)` 加**冻结解析器**防刷分。GPT 版想奖励的东西（frame 正确、证据被用、无幻觉证据）不该做成 λ 项，该做成引擎判定的 `R_exec` 内容。②**数据主路必须换**：GPT 版以"VSI/MMSI 上生成 teacher 轨迹"为主路，这恰好落进同源耦合（Skill-3D/S-Agent 已做过同样的事，第三次做差异化为零）和 benchmark 风格过拟合两个坑；更致命的是 GPT 版自己提出的 Reference Frame Accuracy / Evidence Sufficiency / Counterfactual Tool Causality **在真实图像上没有真值可标**，落地必然回到"请 GPT 当裁判"，指标的公信力在出生时就被抵消。这些指标只有在引擎底座上才是可自动计算的量。
4. **三份文档收敛于同一个第一实验**：反事实翻转率 vs 表面 ETU 的裂口测量（fable5 版 §5.4 第 1 步 = with_reasoning_all §10.2 Experiment 1 的 H3 = GPT 版 Counterfactual Tool Causality 指标的落地形态）。零训练、用现成 agent 和本地已有权重（GroundingDINO、DA3METRIC-LARGE），无论结果如何都可发表：裂口大→底座必要性成立（analysis paper）；裂口小→ETU 已够用，是一个正面校准结果，且为 M2 的训练路线扫清依据。
5. **投稿阶梯**：M1（第 1–6 周，零训练 analysis paper：裂口测量 + Oracle3D-Gym v0）→ M2（第 7–18 周，主会：GeoSkill 骨架 + 引擎奖励训练 + 引擎-vs-裁判奖励对照）→ M3（停止/验证策略——目前无人占的方法点 + Gym 正式发布）。与生成线（Agentic_world_all）共享同一批 Blender 基建，一次投入两线复用（§2 末）。

---

## 1. 对 GPT 版（GeoSkill-Agent）的逐项裁决表

| GPT 版组件 | 裁决 | 理由 / 补丁 |
|---|---|---|
| 主命题：GeoSkill-Agent 框架为主贡献 | **降级为骨架** | 部件三方收敛=稳健但不新；审稿人会用 Skill-3D+GCA+S-Agent 的组合拳打"增量拼装"。框架照建，但论文卖点放在协议与底座 |
| skill 七字段几何契约（§2 Gap1） | **采纳** | 两版最大公约数；GCA 的 CR −6.6 vs CO −1.2 消融直接支持把参考系放进 trigger 之后的第一字段 |
| L0–L4 分层（L0 任务形式化前置） | **采纳** | L0 是相对 Skill-3D 最该补的一层，判断正确 |
| XML 轨迹格式 + observation masking | **采纳** | masking 是 Thyme 验证过的关键恢复步骤；工具参数低温解码、规划保留采样的细节也对 |
| 数据三来源（benchmark teacher 轨迹为主路） | **修正：主路换引擎** | 见 §0.3②；teacher-on-VSI/MMSI 降为迁移验证辅路。补充（我的判断）：GPT 版列的七类负例（no-tool/wrong-tool/over-tool/wrong-frame…）在真实数据上要人工构造，在引擎里是**免费副产品**——知道最小工具链就自动知道什么是过度调用 |
| 四类样本 + recovery 样本 | **采纳** | recovery 是四类中最稀缺的研究对象 |
| 七项 λ 奖励（§5.2） | **修正为最简三项** | Thyme 消融反例（63.59→62.91）；R_frame/R_evidence/R_verification 不做奖励项，做引擎判定的通过条件（进 R_exec）；`Hallucinated_evidence` 保留为硬惩罚（引擎可判：声称的数值不在任何工具返回里） |
| Stage 1/2/3 训练（冷启动 SFT → GRPO → 离线技能迭代） | **采纳** | 与 Skill-3D Fig 5"RL 期间冻结技能库"的教训一致，`library → policy → rollout → library` 离线循环的表述正确 |
| 八项机制消融设计（§6.2） | **采纳** | "少一个中间机制而非少一个工具"的设计思想是对的，全部保留进 M2 |
| 诊断面板（§6.3） | **采纳 + 升级** | 面板字段在引擎上全部有真值列（frame 真值、最小工具链真值、证据充分性真值），从"人工/GPT 标注面板"升级为"自动面板" |
| 新指标四件套（RFA / Evidence Sufficiency / No-Tool Calibration / Counterfactual Causality） | **采纳 + 换底座** | 指标设计好，测量位置错：真实 benchmark 上无真值 → 必须在引擎上测，再看真实域相关性 |
| 四个贡献点排序（框架>证据>配方>诊断） | **重排为：协议>底座>配方>框架** | 反事实协议最锋利且确定无人做过；框架排最后 |
| 周计划（W1 Ctask 原型 → W2-3 500 条 → W4 SFT → W5+ RL） | **修正首步** | W1 不该做 Ctask 原型（GCA 已证明 Ctask 有效，+7.5 到 47.6，复验它不产生新知识）；W1-2 应该做反事实裂口实验（无人做过、直接决定后续路线）。训练整体推迟到 M2 |
| 风险表 | **采纳 + 合并**（§4） | 两版风险表互补：GPT 版偏工程（机制太重/成本），我版偏方法学（合成-真实 gap/被评价为造数据集） |

---

## 2. 定版方案（一页）

**主张句**：agent 框架用收敛清单照建（GeoSkill 骨架），论文贡献押在两件无人做过的事上——**反事实工具因果协议**（把"工具是否真的起作用"第一次变成可测量的量）和 **Oracle3D-Gym**（首个对参考系/证据/因果/成本逐项给真值的 3D 工具使用训练评测环境）。

**骨架**（GPT 版 §3.1 保留）：`Question → L0 任务形式化（Ctask: CR+CO）→ 证据需求 → 技能检索/选择 → 工具程序（检测/深度/位姿/点云/渲染）→ L3 关系专家（答案级证据）→ verifier（充分?一致?便宜?）→ 答案或回退`。

**指标真值化**（本篇相对两个父文档的核心增量表）：

| 指标 | GPT 版的测法（问题） | 引擎底座上的测法 |
|---|---|---|
| Reference Frame Accuracy | 无真值，需 GPT 判 CR 是否正确 | 场景程序里参考系是构造量，逐题真值免费 |
| Evidence Sufficiency | "碰巧答对"无法识别 | 证据规范（该题需要哪些几何量）随题生成，可判"答对但证据不足" |
| Counterfactual Tool Causality | 提出了但没有可操作定义 | 置换深度 ±20% / 旋转参考系 90° / 错绑实例 → 真值告诉我们答案**应该**翻转还是不变 → 翻转率是自动标量 |
| No-Tool Calibration | 靠人工标"简单题" | 最小工具链真值为空集的题即 no-tool 题，标注免费 |
| ETU@Cost | 成本可测但"必要性"不可测 | 最小工具链真值直接定义冗余调用 |

**与生成线共享基建**（资源论证，重要）：Oracle3D-Gym v0 需要的东西——场景程序、几何真值导出、可编程执行——与 [Agentic_world_all](<Agentic_world_all.md>) M1 的解耦冲刺（WorldSpec、场景自省工具、可编程烘焙）是**同一批 Blender/Infinigen 工程**。生成线造世界、理解线在世界里出题评测，一次工程投入喂两条投稿线。这也是把两条线放在同一个组里做的最强理由。

---

## 3. 投稿阶梯：三个里程碑

### M1（第 1–6 周，零训练）：裂口测量 + Oracle3D-Gym v0 → analysis paper

与 [3d_insight_with_reasoning_all](<3d_insight_with_reasoning_all.md>) §10.2 的 Experiment 1 是同一个实验，H1–H3 预注册沿用（H1：Skill-3D 检索范式的翻转率低于 Think3D-RL；H2：相机运动类任务翻转率高于计数/尺寸类；H3：至少一个 baseline 存在 ETU-翻转率显著裂口）。

- **W1–2**：Gym v0——100–200 个 Blender/Infinigen 合成场景，脚本化导出几何真值（位姿/尺寸/朝向/可见性/实例身份）+ 按真值反向生成四类空间题（相对方向/距离/计数/朝向）+ 每题证据规范与最小工具链真值。刻意"视觉丑但几何真"，渲染质量不是目标。
- **W3–4**：在三 baseline（Skill-3D 复现 / Think3D 开源代码 / S-Agent 按笔记重实现，工具栈用本地已有 GroundingDINO + DA3METRIC-LARGE 权重）上跑成功轨迹，做三种干预，产出核心图：**表面 ETU vs 反事实翻转率散点 + 裂口**。执行前核对 [[skill3d-mmsi-harness-scoring-bug]] 的计分口径问题。
- **W5–6**：写作。逐题归因用 GPT 版诊断面板（自动真值版）。
- **投稿位**：analysis track / workshop / benchmark track 均可容纳。**双向可发**：裂口大 = 底座必要性成立 + 现有 agent 的"工具使用"有仪式化成分；裂口小 = ETU 是工具因果的良好代理（正面校准结论），M2 可以放心用 ETU 型奖励。

### M2（第 7–18 周）：GeoSkill 骨架 + 引擎奖励训练 → 主会论文

- **数据**：引擎主路（Gym 扩到 3–5k 题，含 GPT 版四类样本与七类负例——负例由真值自动生成）+ VSI/MMSI teacher 轨迹辅路（只用于真实域迁移，不进主奖励循环）。
- **训练**：GPT 版 Stage 1/2/3 照做（冷启动 SFT 学格式与路由 → GRPO 学成本敏感策略 → 离线技能迭代），模型 Qwen3-VL-4B/8B。奖励用最简三项，`R_exec` 的通过条件由引擎判定（frame 正确 ∧ 证据充分 ∧ 无幻觉证据），解析器冻结。
- **核心对照（方法论卖点，直击同源耦合）**：同模型同数据，**引擎奖励 vs GPT 裁判奖励**两组训练，比较 VSI/MMSI/BLINK-MV 真实域迁移。若引擎组更好或相当，"用引擎替代 GPT 当 oracle"从主张变成实验结论。
- **消融**：GPT 版八项机制消融全保留（w/o Ctask、w/o L3 专家、w/o failure lessons、w/o no-tool 样本、w/o masking、w/o cost 项、w/o verifier、SFT vs SFT+RL），每项预期暴露的错误类型照 GPT 版表。
- **量级预期**（不是承诺）：Think3D 的先例是裸工具 +0.8 → RL +12.05；Skill-3D 后训练相对提升约 60%。若 M2 达到同量级且引擎奖励组迁移不差于裁判组，就是完整的主会故事。

### M3（远期）：停止/验证策略 + Gym 正式发布

- 2.3 空位（fable5 版判断，无人占）：现有工作只训练"调用什么"，没人训练"还要不要继续、要不要相信当前结果"。证据：P3D-Bench 观察到 GPT-5.5 平均 1.5 轮就停而 Gemini 用满十轮持续修；MPMWorlds 的前缀质量 gate 把异常率从 0.371/0.862 压到 0.001——停止信号可学。
- 最小版本：在 Think3D 设置里加一个 gate 头，对比固定 3 轮 vs 学习停止的 accuracy@cost。
- 同期把 Gym（含反事实协议、证据规范格式、自动诊断面板）打包发布，吃掉 M1。

---

## 4. 风险与规避（两版合并）

| 风险 | 来源 | 规避 |
|---|---|---|
| 合成→真实 gap 使底座结论不迁移 | fable5 版（最大风险） | 每个实验带 VSI/MMSI 迁移列；合成域"几何真优先于视觉美"；M2 的引擎-vs-裁判对照本身就是迁移检验 |
| 被评为"只是造了个数据集" | fable5 版 | 主贡献锚定在反事实协议与裂口测量（分析性结论），Gym 是载体 |
| 机制太重（skill+Ctask+expert+verifier+RL） | GPT 版 | 八项消融证明每层解决不同错误类型；M1 不带任何机制，天然轻 |
| 工具质量决定上限 | 两版一致 | verifier + fallback + 工具置信度记录；引擎底座还能单独量化每个工具在分布内的误差谱（我的补充） |
| teacher bias / benchmark 风格过拟合 | 两版一致 | 数据主路已换引擎；teacher 轨迹只做辅路 |
| no-tool 能力退化 | GPT 版 | 负例自动生成保证比例；no-tool calibration 进诊断面板常驻 |
| 同类 Gym 工作 6–12 个月内出现 | fable5 版 | 贡献提前锚定在反事实协议（确定无人做）；M1 先发制人 |

---

## 5. 一句话

**GPT 版给了正确的机器（几何契约技能 + L0–L4 骨架 + 轨迹格式 + 消融设计），Fable 5 版给了正确的裁决（框架已收敛不值钱、底座与因果协议才是空位）。合并后的路线：6 周用现成 agent 和本地权重跑出裂口测量发第一篇，18 周用引擎奖励训练出 GeoSkill 骨架发主会，远期占住"停止/验证策略"这个没人碰的方法点——且所有 Blender 工程与生成线（Agentic_world_all）共享，一次投入养两条线。**

---

## 6. 来源与证据边界

- 两个父文档：[3d_insight](<3d_insight.md>)（GeoSkill-Agent 全部框架细节、轨迹格式、消融与周计划）、[3d_insight_fable5](<3d_insight_fable5.md>)（四个收敛机制、四个系统性弱点、Oracle3D-Gym 论证与全部消融数字出处）
- 关联文档：[3d_insight_with_reasoning_all](<3d_insight_with_reasoning_all.md>)（三 baseline 统一 harness 与 H1–H3 细则，M1 执行时以它为准）、[Agentic_world_all](<Agentic_world_all.md>)（共享基建的生成线）
- 关键数字出处（均见本目录精读笔记）：GCA CR −6.6 / CO −1.2、40.1→47.6；S-Agent L2 +0.8 / L3 +6.9；Skill-3D ETU 39.2%→78.7%、20.8s vs 35.1s；Think3D +0.8→+12.05、36.7/38.7/47.1；Thyme 63.59→62.91、65.68；P3D-Bench J-Sem 0.79–0.84 vs J-Geo 0.34–0.37、停止行为 1.5 轮 vs 7.9 轮；MPMWorlds 0.371/0.862→0.001；本地权重与 MMSI 计分注意事项见项目记忆
- **边界声明**：M1 的 H1–H3 是预注册假设；M2 的量级预期引自他人论文先例，非本方案承诺；"停止/验证策略无人占位"的判断基于库内 13 篇与两版 insight 的覆盖，未做全网检索，投稿前需补 related work 扫描；所有裁决为我的判断，标注在 §1 表内，两个父文档原文未改动。
