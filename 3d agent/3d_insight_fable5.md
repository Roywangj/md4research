# 3D Agent Insight（Fable 5 精读版）

> 写作说明：本文基于对 `3dAgent` 目录下 12 篇 DeepPaperNote 精读笔记与 CompassAD 短笔记的完整重读，独立给出我的判断。它与已有两版洞察（[3d_insight](<3d_insight.md>) 的 GeoSkill-Agent、[3d_insight_with_reasoning](<3d_insight_with_reasoning.md>) 的 GeoTrace-Agent）的关系在第 4 节明确说明：核心方向我同意，但我认为两版共享一个未被指出的结构性盲点——**数据与评测底座**。第 5 节是我基于全部 12 篇（而不只是空间问答 5 篇）给出的主推方向。

## 0. 三个最重要的判断（TL;DR）

**判断一：这批论文最可靠的共同发现只有一个——原始几何不是证据，"确定性翻译层"才是。** S-Agent、GCA、Skill-3D、Think3D、DeepScan、Thyme 六篇免训练/轻训练框架，收益全部来自在"工具输出的原始几何"和"语言模型的推理"之间插入一层确定性转换（专家/约束/锚点/掩蔽）。这是全场收敛的机制，数字证据见第 2.1 节。

**判断二：整个领域的最大评测漏洞是"工具因果性"从未被测量过。** 所有论文（包括提出 ETU 的 Skill-3D 自己）都承认：没人验证过"移除或扰动某个工具输出后，答案是否真的改变"。加上教师模型 / 评审模型 / 被测模型的同源耦合（第 3.2 节列了四篇的具体证据），当前所有"agent 学会了用工具"的主张都建立在近似指标上。

**判断三：目录里被当作背景的生成线（SimWorld Studio / Code2Worlds / MPMWorlds / P3D-Bench），恰好是修补上述两个漏洞的钥匙。** 仿真引擎里每个几何事实都有真值：参考系、距离、计数、遮挡都不需要 GPT-5.4 当 oracle。把生成线变成工具使用线的**真值底座与反事实评测台**，是我认为比继续在现有 benchmark 上做蒸馏更高杠杆的方向（第 5 节）。

## 1. 十二篇论文的证据地图

按四条线组织。每篇给出：贡献所在层（问题/方法/数据/评测/工程）、精读后我认为**最硬的一个证据**、以及**我最不信的一个地方**。

### 1.1 空间推理 agent 线（核心线）

| 论文 | 贡献层 | 最硬的证据 | 我最不信的地方 |
|---|---|---|---|
| [Skill-3D](<3d agent/Skill-3D/paper_DeepPaperNote.md>) | 方法（技能记忆）+ 评测（ETU） | ETU 从 39.2% → 78.7%（VSI），且比 Think3D 快（20.8s vs 35.1s）——收益来自证据路由而非堆工具 | 训练/测试拆分是作者自拆的 30%/70% 同源题目；技能库由 GPT-5.4 蒸馏，"泛化"是题目级不重叠，不是分布外 |
| [Think3D](<3d agent/Think3D/paper_DeepPaperNote.md>) | 方法（主动 3D 观察接口） | 消融显示无相机锚点时给点云反而掉分；RL 后小模型工具收益从 +0.8 → +12.05——学到的是视角策略而非答题能力 | RL 训练只用 MindCube 977 条样本，且全是多选题；视角偏好可能与题型强耦合 |
| [S-Agent](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>) | 方法（分层工具+双记忆）+ 数据（S-300K） | 消融：加 L2 原始 3D 证据只 +0.8（49.0→49.8），加 L3 专家 +6.9（→56.7）——原始几何会干扰模型 | 核心消融只在一个 benchmark（ViewSpatial）一个规划器（GPT-5.4）上做过；全文无时延/轮数/成本报告 |
| [GCA](<3d agent/Geometrically-Constrained Agent for Spatial Reasoning/paper_DeepPaperNote.md>) | 方法（形式化任务约束） | 工具+代码+反馈合计只到 40.1，加 `Ctask` 再 +7.5 到 47.6；去 `CR` 掉 6.6 点、去 `CO` 只掉 1.2 点——参考系是空间语言的头号歧义源 | 错误归因显示约 70% 错误仍在 `Fcompute`（感知/代码/参数）；约束解决的是规划一半，工具链脆弱性原样保留 |
| [Thyme](<../Reasoning/Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>) | 方法（工具策略训练配方，2D） | 奖励消融：加过程奖励反而从 63.59 掉到 62.91，一致性奖励最高 65.68——工具频率不能进奖励 | GRPO-ATS（双温度）没有独立消融；训练成本报告自相矛盾（224 vs 1200+ GPU 小时） |

**这条线的合并读法**：四篇 3D 论文各解决闭环的一段——GCA 管"在哪个坐标系里算"（工具之前），Think3D 管"下一步从哪里看"（观察动作），S-Agent 管"原始几何如何变成可用关系 + 跨帧状态"（工具之后），Skill-3D 管"这类场景该走哪条证据链 + 经验如何沉淀"（跨问题）。Thyme 提供把这一切变成可训练策略的配方（观察掩蔽、no-tool 样本、结果中心奖励）。**它们不互斥，而是同一条 pipeline 的五段，这也是为什么两版已有 insight 都收敛到"合成一个系统"。**

### 1.2 视觉证据落地线

| 论文 | 贡献层 | 最硬的证据 | 我最不信的地方 |
|---|---|---|---|
| [DeepScan](<3d agent/DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models/paper_DeepPaperNote.md>) | 方法（自底向上证据搜索） | 同专家条件下自底向上 vs 一次性定位：90.6 vs 83.8；TreeBench 比较推理子项 43.2 与原始模型持平——**定位更准 ≠ 推理更强**，边界画得很诚实 | 证据完整性由被增强的同一个 VLM 自评，判断器校准误差未测量；确认偏差风险真实存在 |
| [A4-Agent](<3d agent/A4-Agent An Agentic Framework for Zero-Shot Affordance Reasoning/paper_DeepPaperNote.md>) | 方法（测试时多模型编排） | Table 6：仅 Spotter 45.9 → 加 Thinker 62.3 → 加 Dreamer 63.9——结构增益主要来自"部件选择独立于检测器"，想象图只是辅助 | 正文与表格数字冲突（71.83 vs 70.52）；无逐阶段错误归因、无成本报告；"想象图"可能制造伪证据但无拒绝机制 |
| [CompassAD](<CompassAD - Intent-Driven 3D Affordance Grounding in Functionally Competing Objects.md>) | 问题+数据（功能竞争消歧） | query-dependent supervision：同场景不同意图对应不同真值——把 affordance 从"识别功能"推进到"任务条件下选择" | ICI 依赖实例可分性；遮挡/堆叠场景下边界假设脆弱（笔记为摘要级精读，证据核对不如其他篇充分） |

**合并读法**：这条线回答的是空间 agent 闭环的第一步——"问题到底关于图里哪块证据"。DeepScan 的 TreeBench 结果是给整条 3D agent 线的一盆冷水：**grounding 提升会被误写成 reasoning 提升**，这也解释了为什么 S-Agent 需要 L3 专家、GCA 需要公式库——找到证据之后的那段推理仍是模型短板。

### 1.3 生成 / 世界模型 / 评测线

| 论文 | 贡献层 | 最硬的证据 | 我最不信的地方 |
|---|---|---|---|
| [P3D-Bench](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>) | 评测（四层拆分：能跑/像/准/结构对） | J-Sem 0.79–0.84 vs J-Geo 0.34–0.37；PartMatchF1 ≈ 0.5——语义像、几何准、结构对是三件事；多轮实验里 GPT-5.5 平均 1.5 轮就停、Gemini 7.9 轮持续修——**停止策略本身是 agent 能力** | 标注器/评审器/被测模型高度同源（Gemini 评审 Gemini、Claude 分解 Claude）；数据域窄（67% 是机械支撑件） |
| [Code2Worlds](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>) | 方法（双流+分类型 critic） | 去掉 Motion Critic 物理失败率 10% → 60%；去掉检索 SGS 61.4 → 23.5——能力来自"程序库先验+执行器+反馈协议"，不是裸 LLM | Code4D 只有 10 条提示；SGS/HRS/Richness 由 GPT-4o 评分而系统由 Gemini 3 驱动；视觉闭环校正表象、不做系统辨识 |
| [MPMWorlds](<3d agent/MPMWorlds Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics/paper_DeepPaperNote.md>) | 评测（诊断坐标系）+ 分析 | 代码路线 vs 视频路线严格互补：VLM 异常率 0.371 vs VDM 0.862，但 mIoU 反过来 0.512 vs 0.611；前缀质量 gate 把异常率压到 0.001——**状态估计和动力学外推是两种能力** | 数据是 2D 合成 MPM 且由真值代码生成，天然偏向代码路线；VDM 只测了一个 14B baseline |
| [Gamma-World](<3d agent/Gamma-World Generative Multi-Agent World Modeling Beyond Two Players/paper_DeepPaperNote.md>) | 方法（多智能体归纳偏置） | Simplex RoPE + Sparse Hub：身份要"可区分但可交换"，通信成本从 P² 降到线性；两人训练零样本泛化到四人 | 无任务成功率/物理接触指标，只有 FVD/FID 类分布指标；机器人部分是概念验证；32×GB200 的复现门槛 |
| [SimWorld Studio](<3d agent/SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning/paper_DeepPaperNote.md>) | 系统（环境生成→Gym 接口→共同演化） | 机制消融 0.16 → 0.45（MCP 工具）→ 0.55（验证循环）→ 0.76（自我演化）；共同演化课程比固定环境 +18 点、比不训练 +40 点 | 具身任务只覆盖导航；9 个评估场景的量化规模小；VLM 验证器会把评审偏好写进生成分布 |

**合并读法**：这条线内部有一个漂亮的三角——Code2Worlds 证明"可以从语言生成可执行物理世界"，MPMWorlds 证明"可执行世界赢在长时序稳定、输在视觉状态估计"，P3D-Bench 证明"可执行 ≠ 正确，结构要单独测"。SimWorld Studio 再把生成的世界接上 `reset()/step()/reward`，变成能训练 agent 的基础设施。**这条线的每一篇都在说同一句话：真值来自执行器，不来自评审模型。**

### 1.4 阅读优先级建议

如果要给后来者排序：**必精读** Skill-3D、GCA、S-Agent（方法主线三支柱）+ P3D-Bench（评测方法论范本）；**重点读消融** Think3D（Table 3/6）、Thyme（Table 5/6）、DeepScan（Table 7）、Code2Worlds（Table 3/4）、SimWorld Studio（Fig. 5）；**按需读** Gamma-World（做多智能体才需要）、MPMWorlds（做物理外推才需要）、A4/CompassAD（做 affordance 才需要）。

## 2. 跨论文收敛的四个机制性结论

这是精读 12 篇之后最值钱的部分：单篇看是各自的 trick，放在一起是同一个机制的四个侧面。

### 2.1 原始几何不是证据，确定性翻译层才是（全场最强收敛）

六篇论文用完全不同的实现给出了同一个数字模式：

| 论文 | "翻译层"是什么 | 无它 → 有它 |
|---|---|---|
| S-Agent | L3 空间专家（把深度/位姿转成任务化标量） | 原始 3D 证据只 +0.8，加专家 +6.9 |
| GCA | `Ctask` 约束 + 固定几何公式库 | 工具自由发挥 40.1，约束锁定 47.6 |
| Think3D | 相机锚点 + 离散视角动作 | 裸点云反而掉分，锚点化后持续上升 |
| Skill-3D | 技能 =（触发条件+证据需求+工具顺序），而非长轨迹 | ETU 39% → 79%，且比重建中心路线快 |
| DeepScan | 点式代理 + 形态学后处理 + 完整性奖励 | 一次性定位 83.8 → 自底向上 90.6 |
| Thyme | 沙箱协议 + 观察掩蔽（工具输出不进 loss） | 掩蔽是朴素混合训练后最关键的恢复步骤 |

我的表述：**VLM 与几何世界之间需要一个"编译器"，而不是一个"提示词"。** GCA 的附录直接证明了这一点——把 `Ctask` 只当文本提示、不绑定工具变量，收益仅 +0.9。所有把几何数值直接塞进上下文的做法都在重复同一个错误。

推论（我的推断，非论文原话）：这层翻译器是**确定性程序**而非学习组件，是它有效的原因也是它的天花板——它把误差从"模型幻觉"转移到"工具链脆弱性"（GCA 的 70% 剩余错误、Skill-3D 的"高效地走错路线"）。下一代工作的竞争点会是这个翻译层本身的覆盖率和可验证性。

### 2.2 参考系错误发生在所有工具之前，且无法被下游补救

GCA 的 `CR`（-6.6）vs `CO`（-1.2）消融是整个目录里我认为信息量最大的单个数字：空间语言最危险的歧义不是"要测什么"，而是"在谁的坐标系里测"。Think3D 的相机锚点消融、S-Agent 在 ViewSpatial 人物视角任务上 +20.5 点的最大单项优势，都是同一件事的旁证。这条结论的工程含义很直接：**参考系解析应该是 pipeline 的第 0 层，且应该产出可检查的结构化对象（原点、朝向向量、实例绑定），而不是一段推理文字。**

### 2.3 "何时调用、何时停止"是能力，必须被训练和被测量

四篇论文从不同方向撞到同一堵墙：

- Think3D：小模型直接接工具 +0.8，RL 学策略后 +12.05；随机/启发式/RL 视角策略 = 36.7 / 38.7 / 47.1——**工具收益的大头在策略，不在工具**。
- Thyme：10 万条 no-tool 样本 + 结果中心奖励，防止"调用工具 = 正确"的伪规律；直接奖励代码执行反而掉分。
- P3D-Bench：同样十轮预算，GPT-5.5 62% 第一轮就停（+0.002），Gemini 51% 用满十轮（+0.030）——**停止策略差异比模型排名差异更有研究价值**。
- MPMWorlds：前缀重建质量 gate 就能把时间异常率从 0.371/0.862 压到 0.001——"当前证据是否可信"有可测的代理信号。

合并结论：3D 工具 agent 的策略空间是三元的——调用什么、还要不要继续、要不要相信当前结果。现有工作只训练了第一元；第二、三元（停止与验证）目前只有观察性证据，没有专门方法。**这是一个明确的空位。**

### 2.4 可执行世界赢在状态推进，输在状态估计——所以两条线必须合流

MPMWorlds 把这一点测成了干净的对照：代码路线动力学稳（异常率 0.37 vs 0.86）但看不准初始几何（mIoU 0.51 vs 0.61）；视频路线正好相反。Code2Worlds 的 Motion Critic（失败率 10%↔60%）和 P3D-Bench 的 J-Sem/J-Geo 裂口（0.8 vs 0.35）是同一短板的两个投影：**语言模型能维持"语义像"，维持不了"数值准"**。

这与 2.1 是同一枚硬币：理解侧要"几何→语言"的翻译层，生成侧要"语言→几何"的编译层 + 执行反馈。两侧的失败都集中在翻译边界上。

## 3. 领域的系统性弱点（审稿人视角）

### 3.1 工具因果性从未被测量

ETU（Skill-3D）已是全目录最好的过程指标，但它测的是"工具输出有效且出现在后续推理中"，不是"答案因它而改变"。Skill-3D 自己在局限里承认需要反事实删除实验；Thyme 的失败案例里明确出现"裁剪了无关区域，却靠已有知识碰巧答对"。**当前没有任何一篇做过：把某个工具观察替换为扰动值/空值，测答案翻转率。** 这个实验便宜（推理时干预，无需训练），却能直接检验整个领域的核心主张。

### 3.2 教师 / 评审 / 被测模型同源耦合是普遍现象

| 论文 | 耦合点 |
|---|---|
| Skill-3D | GPT-5.4 蒸馏技能 + 生成 SFT 数据，又是被比较的规划器之一 |
| S-Agent | GPT-5.4 作 teacher 规划器生成 S-300K，蒸馏到 8B |
| P3D-Bench | Gemini 3.1 Pro 做数据复核+QA+评分，Claude 做部件标注+分解，二者同时在排行榜上 |
| Code2Worlds | 系统由 Gemini 3 驱动，SGS/HRS/Richness 由 GPT-4o 评分 |
| SimWorld Studio | VLM 验证器的审美会写进生成分布（作者自己警告） |

单看每篇都有缓解措施，合起来看是行业性风险：**"agent 能力"的相当部分可能是模型家族方言的对齐度。** 任何后续工作只要能把真值来源从"更强的模型"换成"执行器/引擎"，就在方法学上高一档——这直接引向第 5 节。

### 3.3 泛化主张普遍弱于表述

Skill-3D 的拆分是同 benchmark 内 30/70 自拆；Think3D 的 RL 只用 977 条 MindCube 多选题；S-Agent 核心消融单基准单规划器；GCA 明确不覆盖动态参考系 `CR(t)` 和抽象区域参考系；Code4D 仅 10 条提示。**没有一篇提供合成→真实、或跨题型（多选→开放式）的迁移证据。** 各家在"局限"一节都写了，但拼起来才看清：这批方法的适用域边界比引言的叙事窄得多。

### 3.4 成本是系统性沉默项

S-Agent 无时延/轮数报告；A4-Agent 串四个大模型无成本数据；Thyme 训练成本口径冲突；只有 Skill-3D（20.8s vs 35.1s）和 DeepScan（24.5s → 优化后 3.1s）认真报了准确率-成本折中。鉴于 Pi3 重建单次约 21 秒而深度/朝向估计约 1 秒（Skill-3D 附录），**成本敏感的证据路由不是工程细节，而是这个范式能否部署的前提**。

## 4. 对已有两版 insight 的评估

[GeoSkill-Agent](<3d_insight.md>)（技能=可验证几何契约）和 [GeoTrace-Agent](<3d_insight_with_reasoning.md>)（轨迹=belief-update program）方向上我都同意，且两版的部件选择（Ctask 第 0 层、L3 专家、observation masking、no-tool 负例、反事实指标）与我第 2 节的收敛结论一致——这说明结论稳健，三次独立综合都指向同一处。

但两版共享一个未言明的前提：**训练与评测仍站在现有 benchmark + 强 teacher 蒸馏的底座上。** 具体来说：

1. 两版的数据方案都以"在 VSI/MMSI 上生成 teacher 轨迹"为主路、合成数据为辅路——这恰好落进 3.2（teacher 偏置）和 3.3（benchmark 风格过拟合）两个坑。Skill-3D 和 S-Agent 已经这么做了，第三次做同样的事差异化有限。
2. 两版提出的关键新指标（Reference Frame Accuracy、Evidence Sufficiency、Counterfactual Tool Causality）在真实图像 benchmark 上**根本没有真值可标**——参考系是否正确、证据是否充分，最终还是要请 GPT 当裁判，回到 3.2。
3. 两版都把仿真/生成线放在"辅助数据来源"或"high-risk 远期"的位置。精读完 SimWorld Studio（共同演化 +18 点、验证循环消融）和 MPMWorlds（四种输入条件的诊断设计）之后，我认为这个定位低估了：**生成线不是辅助数据源，而是唯一能提供"逐步骤真值"的评测与奖励底座。**

所以我的版本不再重复提出第三个 agent 框架命名，而是把主贡献押在底座上。

## 5. 我的主推方向：Oracle-Grounded 3D Tool-Use（把生成线变成工具使用线的真值底座）

### 5.1 核心主张

> **3D 工具使用研究的瓶颈已经不在 agent 框架设计（部件清单三篇论文加两版 insight 已收敛），而在于没有一个能对"参考系、证据、因果、成本"逐项给出真值的训练与评测环境。用引擎当 oracle，替换掉用 GPT 当 oracle。**

具体形态：一个建立在可执行 3D 环境（Blender/Infinigen 起步，SimWorld Studio 式 UE5 为扩展）之上的工具使用训练-评测闭环，暂名 `Oracle3D-Gym`。每个样本 = 场景程序 + 完整几何真值（所有物体的位姿/尺寸/朝向/可见性/实例身份）+ 由真值反向生成的空间问题 + 该问题的**证据规范**（哪个参考系、需要哪些几何量、最小工具链是什么）。

### 5.2 它一次性解决第 3 节的四个弱点

| 弱点 | 引擎底座怎么解 |
|---|---|
| 3.1 工具因果性 | 工具输出可被程序化替换为扰动值（深度 ±20%、参考系旋转 90°、实例错绑），真值告诉我们答案**应该**翻转还是不变——反事实 ETU 变成可自动计算的标量 |
| 3.2 同源耦合 | Reference Frame Accuracy、Evidence Sufficiency 逐样本有引擎真值，奖励与评测不再需要 GPT 裁判；teacher 轨迹可以用真值过滤而非用更强模型过滤 |
| 3.3 泛化 | 场景程序可控扰动（材质/布局/遮挡/相机分布），能真正做"同任务分布外"测试；再迁移到 VSI/MMSI 作真实域验证 |
| 3.4 成本 | 每个工具调用的真实耗时和"该证据是否必要"（最小工具链真值）都可记录，`ETU@Cost` 和 no-tool calibration 有了非启发式的标注 |

Thyme 强调的四类负例（no-tool / wrong-tool / over-tool / wrong-frame）在真实数据上要人工构造，在引擎里是**免费副产品**：知道最小工具链，就自动知道什么是过度调用；知道真参考系，就自动能生成参考系翻转的对抗题。

### 5.3 与最近工作的差异（novelty 检查）

- vs SimWorld Studio：它生成的是**具身导航**环境（reset/step/导航奖励），服务于策略学习；我提议的是**空间问答工具链**的真值环境，服务于工具策略训练与诊断。共享基础设施思想，任务层完全不同。
- vs MPMWorlds：它诊断的是"世界模型能否外推物理"；我诊断的是"agent 能否正确获取与使用几何证据"。可以直接借它的方法论（同一前缀 + 分级旁路信息的诊断设计、prefix gate）。
- vs Skill-3D/S-Agent 的合成辅路：它们把合成数据当 SFT 增量；这里合成环境是**奖励函数和评测协议的定义域**，这是定位差异而非规模差异。
- 风险自查：如果 6-12 个月内出现"带真值的 3D 工具使用 gym"同类工作，主贡献要提前锚定在**反事实工具因果协议**上——这一层目前确定没人做（3.1）。

### 5.4 最小验证路径（不训练，先证明底座有信息量）

**第 1 步（1-2 周）：反事实诊断复用现成 agent。** 在 100-200 个 Blender 合成场景上跑一个 GCA 风格或 S-Agent 风格的现成 pipeline（工具栈按 S-Agent 笔记，GroundingDINO + Depth-Anything-3 权重仓库里已有），对每条成功轨迹做三种干预：置换深度、旋转参考系、错绑实例。产出一张表：`表面 ETU vs 反事实翻转率`。
成功标准：两者出现显著裂口（比如 ETU 80% 的轨迹里只有 50% 对干预敏感）——这本身就是一篇 analysis paper 的核心图，同时证明底座必要。

**第 2 步（2-4 周）：500 条带证据规范的样本 + 逐步骤奖励。** 每类任务（相对方向/距离/计数/朝向）100 余条，含最小工具链真值与参考系真值。用它复算 Skill-3D 式的 GRPO 奖励，但 `R_exec`、`R_frame` 由引擎判定。对照实验：同一小模型（Qwen3-VL-4B/8B），引擎奖励 vs GPT 裁判奖励，看真实 benchmark（VSI/MMSI）上的迁移差异。

**第 3 步（之后）：接第 2.3 节的空位。** 在同一底座上训练停止/验证策略（P3D-Bench 观察 + MPMWorlds gate 信号），这是框架收敛之后下一个没人占的方法点。

### 5.5 可写成论文的贡献点排序

1. **反事实工具因果协议 + 表面 ETU 与真实因果的裂口测量**（最便宜、最锋利，独立成文）。
2. **Oracle3D-Gym：首个逐步骤真值的 3D 工具使用训练评测环境**（主论文，吃掉 1）。
3. **引擎奖励 vs 裁判奖励的训练对照**（方法论贡献，直击 3.2）。
4. 合成→真实迁移曲线（支撑性实验，不单独成文）。

## 6. 其他三个可落地 idea

| 优先级 | 方向 | 假设 | 最小实验 | 成本/风险 |
|---|---|---|---|---|
| 高 | 停止/验证策略学习（接 2.3 空位） | "还要不要再调一次工具"可以从前缀证据质量学出来，比固定轮数上限更优 | 在 Think3D 设置里加一个 MPMWorlds 式 gate 头，对比固定 3 轮 vs 学习停止的 accuracy@cost | 低/中 |
| 中 | Affordance 线与空间线合流 | A4 的部件掩码 + CompassAD 的意图消歧需要 GCA 式参考系才能进 3D 操作（"从把手侧抓"依赖物体坐标系） | 把 A4 输出的 2D 部件掩码经深度提升到点云物体坐标系，在 CompassAD 上测意图消歧是否受益于显式朝向 | 中/中 |
| 低 | 多智能体空间推理评测 | Gamma-World 只测生成质量；"两个 agent 对同一场景的参考系互指"（你的左边=我的右边）没有 benchmark | 用 Oracle3D-Gym 的双相机场景生成互指视角题，先测现有 VLM 的失败率 | 低/高（可能只是 GCA 的换皮） |

## 7. 风险与规避

| 风险 | 判断 | 规避 |
|---|---|---|
| 合成→真实 gap 使底座结论不迁移 | 最大风险。MPMWorlds 自己承认合成基准偏向代码路线 | 每个实验都带 VSI/MMSI 迁移列；把合成域刻意做"视觉丑但几何真"（重点在几何真值而非渲染质量） |
| 被评价为"只是造了个数据集" | 中等 | 主贡献锚定在反事实协议和裂口测量（分析性结论），环境是载体 |
| 工程量失控（UE5 路线） | 中等 | 先 Blender/Infinigen 脚本化（Code2Worlds 已证明可行），UE5/共同演化列为扩展而非依赖 |
| 框架部件与前人重叠 | 低但要写清楚 | 明确不主张新 agent 框架；agent 用现成的（GCA/S-Agent 复现），贡献在底座与协议 |

## 8. 结论

这批论文合起来讲了一个完整的故事：空间推理 agent 的部件清单已经收敛（参考系约束 → 证据搜索 → 几何翻译层 → 记忆/技能 → 策略训练），生成线则证明了执行器能提供语言模型给不了的真值。**下一步最高杠杆的动作不是提出第三个框架，而是把两条线接起来——让引擎替代 GPT 成为 oracle，让"工具是否真的起了作用"第一次变成可测量的量。** 先用两周做反事实裂口实验（5.4 第 1 步），它便宜、可独立发表、且无论结果如何都有信息量：裂口大则底座必要性成立，裂口小则说明 ETU 已够用、可以放心走两版 insight 的训练路线。

## 9. 来源

本地精读笔记（Thyme 位于 `Reasoning/Train`，其余位于本目录）：[Skill-3D](<3d agent/Skill-3D/paper_DeepPaperNote.md>)（arXiv:2606.07436）· [Think3D](<3d agent/Think3D/paper_DeepPaperNote.md>)（2601.13029）· [S-Agent](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>)（2606.20515）· [GCA](<3d agent/Geometrically-Constrained Agent for Spatial Reasoning/paper_DeepPaperNote.md>)（2511.22659）· [Thyme](<../Reasoning/Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>)（2508.11630）· [DeepScan](<3d agent/DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models/paper_DeepPaperNote.md>)（2603.03857，CVPR 2026）· [A4-Agent](<3d agent/A4-Agent An Agentic Framework for Zero-Shot Affordance Reasoning/paper_DeepPaperNote.md>)（2512.14442）· [CompassAD](<CompassAD - Intent-Driven 3D Affordance Grounding in Functionally Competing Objects.md>) · [P3D-Bench](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>)（2606.11152）· [Code2Worlds](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>)（2602.11757）· [MPMWorlds](<3d agent/MPMWorlds Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics/paper_DeepPaperNote.md>)（2606.01538）· [Gamma-World](<3d agent/Gamma-World Generative Multi-Agent World Modeling Beyond Two Players/paper_DeepPaperNote.md>)（2605.28816）· [SimWorld Studio](<3d agent/SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning/paper_DeepPaperNote.md>)（2605.09423）

已有洞察版本：[3d_insight](<3d_insight.md>)（GeoSkill-Agent）· [3d_insight_with_reasoning](<3d_insight_with_reasoning.md>)（GeoTrace-Agent）· 总览：[Overall](<3d agent/Overall.md>)

> 证据边界声明：本文全部数字引自上述本地精读笔记（笔记本身经过 grounding 核对）；未重新访问原始 PDF/arXiv。A4-Agent 的 70.52/71.83 冲突、Thyme 的训练成本口径冲突等原文问题按笔记记录保留。标注"我的推断"处为个人判断，非论文主张。
