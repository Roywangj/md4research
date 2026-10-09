# 3D Agent × Reasoning Insight(合并版:判决框架 × 系统蓝图)

> 本文合并 [3d_insight_with_reasoning](<3d_insight_with_reasoning.md>)(GeoTrace-Agent 路线,给出了轨迹的**语法**——表示、系统、训练、审计)与 [3d_insight_with_reasoning_fable5](<3d_insight_with_reasoning_fable5.md>)(机制-脚手架路线,给出了轨迹的**判决**——哪些调用值得存在、存在于训练时还是推理时)。
>
> 合并原则:**判决先行,蓝图随后**。两版冲突处不和稀泥,我给出裁决并说明理由(第 9 节有逐项裁决表);两版都没有的内容在第 8 节(五个发散启示)。第 10 节是独立专章:以 Skill-3D / Think3D / S-Agent 为核心 baseline 的完整落地方案——它只依赖前文结论,不改动前文结构。

## 0. 五个最重要的判断(TL;DR)

**判断一:全领域唯一的强收敛结论是"原始几何不是证据,确定性翻译层才是"。** 六篇论文六种实现同一模式:S-Agent 原始 3D 证据 +0.8 vs L3 专家 +6.9;GCA 无约束 40.1 vs `Ctask` 47.6;Think3D 裸点云掉分、锚点化后持续上升;Skill-3D ETU 39.2%→78.7%;DeepScan 83.8→90.6;Thyme 观察掩蔽是关键恢复步骤。VLM 与几何世界之间需要的是编译器,不是提示词。

**判断二:但翻译层收益与"推理时新观察"的收益是两个可分离的主张,只有前者被证实过。** Reasoning 线的 [Position paper](<../Reasoning/TrainingFree/Position Your VLM May Not Be Thinking with Interleaved Images/paper_DeepPaperNote.md>) 证明后者在 2D 大面积不成立(删交错图像不掉分,DeepEyes V* 84.3→84.3;普通 SFT 追平;遮挡后仍高分),而**没有任何 3D agent 论文做过推理时删除工具观察的自查**。由此得到本文的判决框架——3D 工具调用三分:(a) 构造性必要 / (b) 分辨率必要 / (c) 便利性调用,只有 (a) 是不可拆的推理机制,(c) 是训练后可拆的脚手架(第 3 节)。

**判断三:轨迹的正确语法是 belief-update program(GeoTrace 版的核心贡献,采纳),但要打三个补丁。** 动作空间必须包含"栈层降级"动作(先复用已编码证据,再升级到外部调用——3D 线全部活在重注入栈最贵的 L5 层,L1-L4 是空白);观察永远先过翻译层再入上下文(MINT-CoT 整图交错 64.07→40.37 的教训);TNG 指标只测量了 2×2 矩阵的一行,删观察不掉分 ≠ 训练白费,可能只是部署方式错了。

**判断四:训练与评测的底座应从"benchmark + GPT 裁判"换成"引擎 + 真值"。** 教师/评审/被测模型同源耦合是行业病(Skill-3D、S-Agent、P3D-Bench、Code2Worlds 各有一处);两版旧洞察的关键新指标(参考系正确性、证据充分性、反事实因果)在真实图像上没有真值可标。Oracle3D-Gym(引擎当 oracle)一次性解掉因果测量、同源耦合、分布外测试、成本标注四个问题。

**判断五:合并后的研究程序是一条单线。** Step 1 审计(推理时删除+扰动,测三 baseline 的 (a)(b)(c) 构成与"表面 ETU vs 反事实翻转率"裂口)→ Step 2 四象限判决({训练有/无工具}×{推理有/无工具},引擎 (a) 类题保底)→ Step 3 判决驱动:脚手架占主则蒸馏无工具部署,机制占主则投资门控与停止策略。核心 baseline 就是 Skill-3D / Think3D / S-Agent——三者恰好覆盖三条正交能力轴与三种范式,且工具栈、benchmark、训练配方全部已知(第 10 节专章)。

## 1. 两条文献线汇合后,真正缺的是什么

### 1.1 3D 主线已分别解决六个局部问题(采纳 GeoTrace 版的地图,数字校准)

| 问题层 | 代表论文 | 已给出的答案 | 关键数字 |
|---|---|---|---|
| 如何先定义问题 | [GCA](<3d agent/Geometrically-Constrained Agent for Spatial Reasoning/paper_DeepPaperNote.md>) | `Ctask=(CR,CO)`,先固定参考系再调工具 | 去 `CR` -6.6,去 `CO` 仅 -1.2 |
| 如何获得新空间观察 | [Think3D](<3d agent/Think3D/paper_DeepPaperNote.md>) | 重建点云、相机锚点、渲染新视角;RL 学视角策略 | 裸工具 +0.8 → RL 后 +12.05 |
| 如何把原始几何变成证据 | [S-Agent](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>) | L1 感知→L2 提升→L3 专家;双记忆 | L2 +0.8 vs L3 +6.9 |
| 如何复用成功/失败经验 | [Skill-3D](<3d agent/Skill-3D/paper_DeepPaperNote.md>) | 场景记忆+技能库+失败教训 | ETU 39.2%→78.7%,20.8s vs Think3D 35.1s |
| 如何回连 3D identity | [REALM](<../Reasoning/TrainingFree/REALM An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting/paper_DeepPaperNote.md>) | 多视角投票、global-to-local grounding | 去视角选择 mIoU 0.95→0.38 |
| 如何验证 3D 输出 | [P3D-Bench](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>) / [Code2Worlds](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>) / [SimWorld Studio](<3d agent/SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning/paper_DeepPaperNote.md>) | 执行/几何/拓扑/物理 verifier | J-Sem 0.8 vs J-Geo 0.35;去 Motion Critic 失败率 10%→60% |

### 1.2 Reasoning 支线给出的是工具轨迹的训练方法与警报(按重注入栈重排)

| 栈层 | 论文 | 对 3D 的迁移 | 3D 目录现状 |
|---|---|---|---|
| L1 注意力增强 | [SDR-MCoT](<../Reasoning/TrainingFree/Mitigating Low-Quality Reasoning in MLLMs Self-Driven Refined Multimodal CoT with Selective Thinking and Step-wise Visual Enhancement/paper_DeepPaperNote.md>) | 推理步对相关视角的再加权;首 token 熵路由 | 空白 |
| L2 KV 重绑定 | [PRCR](<../Reasoning/TrainingFree/Position Rebinding Cache Reuse Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning/paper_DeepPaperNote.md>) | 多视角证据免回放回看(FLOPs 7.75T→125.83M) | 空白(S-Agent 双记忆存文本,不存可复用编码) |
| L3 token 核心集重选 | [VisRef](<../Reasoning/TrainingFree/VisRef Visual Refocusing while Thinking Improves Test-Time Scaling in Multi-Modal Large Reasoning Models/paper_DeepPaperNote.md>) | 从已编码视角选对象级子集,替代重渲染 | 空白 |
| L4 重编码 | [DaP-ICoT](<../Reasoning/TrainingFree/Lets Think with Images Efficiently An Interleaved-Modal Chain-of-Thought Reasoning Framework with Dynamic and Precise Visual Thoughts/paper_DeepPaperNote.md>) | 局部放大/变尺度;logit 间隔门控 | 部分(DeepScan 的 crop) |
| L5 外部行动 | [DeepEyes](<../Reasoning/Train/DeepEyes Incentivizing Thinking with Images via Reinforcement Learning/paper_DeepPaperNote.md>) / [DeepEyesV2](<../Reasoning/Train/DeepEyesV2 Toward Agentic Multimodal Model/paper_DeepPaperNote.md>) / [Thyme](<../Reasoning/Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>) | 条件奖励、冷启动协议、观察掩蔽 | **3D 全部集中在此层** |
| L6 表示训练 | [PFlowNet](<../Reasoning/Train/Perceptual Flow Network for Visually Grounded Reasoning/paper_DeepPaperNote.md>) | 可行域监督(专家轨迹=约束不=真值) | 空白 |
| 审计(横切) | [Position paper](<../Reasoning/TrainingFree/Position Your VLM May Not Be Thinking with Interleaved Images/paper_DeepPaperNote.md>) | no-observation / 遮挡 / 等成本对照 | **空白——无人自查** |

### 1.3 汇合后的核心缺口(GeoTrace 版四件事之前还有第 0 件)

GeoTrace 版指出现有 3D agent 未同时证明四件事:参考系正确、每次调用对应证据缺口、观察更新了 belief、干预观察答案按几何规律变化。我在它前面加第 0 件:**没人证明工具观察在推理时被使用过**——第 0 件不成立时,后四件的工程投入方向会完全不同(该蒸馏拆除的部件不值得配 verifier)。所以正确的顺序是:先判决(第 3 节),再按判决结果实施蓝图(第 4-6 节)。

## 2. 关键证据:为什么这个 gap 不是想象出来的

五条证据,前四条采纳 GeoTrace 版的组织、数字按精读笔记校准,第五条是本版的重新归因:

**2.1 有 3D 工具 ≠ 会用 3D 工具。** Think3D:Qwen3-VL-4B 裸工具 +0.80(路线规划和相对距离子任务甚至下降),Think3D-RL 后 +12.05;随机/启发式/RL 视角策略 36.68/38.69/47.11。S-Agent:未训练 8B 规划器套框架,MMSI 30.7 低于基座 31.1。工具收益的大头在策略,不在工具。

**2.2 原始 3D 数值不是可消费的证据。** S-Agent 消融:49.0→49.8(+L2)→56.7(+L3)。中间语言应是带单位、参考系、identity、来源的 typed evidence,不是坐标堆。

**2.3 参考系错误发生在所有工具之前,下游无法补救。** GCA:`CR` -6.6 vs `CO` -1.2;S-Agent 在 ViewSpatial 人物视角上 +20.5 是同一件事的旁证。参考系解析是 pipeline 第 0 层,产出必须是可检查的结构化对象。

**2.4 视角数量不如视角选择与 identity 绑定。** REALM 去 K-means 视角选择 mIoU 0.95→0.38;多视角若无持久 identity 只是多张独立图片。

**2.5(本版重新归因)以上四条全部是"证据组织形式"的收益,与"推理时新观察是否被使用"无关。** 翻译层、参考系、identity 绑定的消融都不涉及删除观察本身。唯一接近的是 Think3D 的 Self-Refine 对照(多轮纯文本反思收益远小于工具且 token 成本相当)——这是 3D 线目前**唯一**指向"新观察有净贡献"的证据,但它是整体对照,没有逐调用归因。Position paper 的三连击(删图不掉分/SFT 追平/遮挡仍高分)在 2D 已经证明:轨迹文本+微调分布可以解释大部分收益。3D 的多选 benchmark(VSI/MMSI/MindCube)与被审计的 2D benchmark 同一格式,**不天然免疫**。

## 3. 判决框架:3D 工具调用的机制-脚手架三分

支线的脚手架假说:Position paper 的推理时删图不掉分与 DeepEyes 的训练时消融(iMCoT vs text-only RL,HR-8K 72.6 vs 60.8)同时为真的最简解释——**交错视觉行动的收益在训练期沉淀进参数,推理时的调用在多数 benchmark 上已是仪式**。带进 3D:

| 类别 | 定义 | 3D 例子 | 预测 | 处置 |
|---|---|---|---|---|
| (a) 构造性必要 | 初始编码原理上不含答案所需信息 | 遮挡背面的关系;需新视角的几何;精确度量深度 | 删除观察必掉分——真机制 | 保留推理时调用,投资门控/停止策略 |
| (b) 分辨率必要 | 信息在原图但超出编码分辨率 | 远处小物体计数;细小部件朝向 | 常被参数先验部分补偿(Position 遮挡实验:微调模型仍高出基座 9-12 点) | 训练时保留,推理时按门控选择性调用 |
| (c) 便利性调用 | 信息已在上下文,调用只做重组织 | 重渲染已见视角;重复查询已有点云;冗余 crop | 训练后可完全拆除——纯脚手架 | 蒸馏进参数,或降层到 L1-L4 廉价复用 |

三个推论:

**推论一(对评测):现有 benchmark 的 (a)(b)(c) 构成未知,使所有"agent 学会了用工具"的主张不可归因。** 若 VSI/MMSI 被 (c) 主导,Skill-3D 的 ETU 79% 主要测轨迹格式合规,Think3D 的 +12.05 主要是行为分布收益。测量构成本身即一篇 analysis paper。

**推论二(对训练):即使脚手架假说在 3D 成立,翻译层投资不白费——白费的是昂贵的重建-渲染循环。** 这是对 3D 线最有指导性的边界:第 2 节四条收敛证据在任何判决下都站得住。

**推论三(对部署):3D agent 成本可能被高估一个数量级。** 若 (c) 占主,正确形态是"工具轨迹训练+无工具推理"(Position 的 SFT 实验间接支持),Pi3 的 21.35 秒、S-Agent 未报告的多轮时延大部分可省。成本是 3D 线的系统性沉默项(仅 Skill-3D 与 DeepScan 认真报了折中)。

## 4. 轨迹的正确语法:belief-update program(采纳 + 三补丁)

采纳 GeoTrace 版的轨迹定义——这是它最好的贡献:

$$\tau=\{z_t\}_{t=0}^{T},\qquad z_t=(B_t,C_t,U_t,N_t,A_t,O_t,E_t,V_t)$$

其中 $B_t$ 场景 belief、$C_t$ 几何契约 `Ctask`、$U_t$ 未决不确定性、$N_t$ 证据需求、$A_t$ 工具动作、$O_t$ 原始观察、$E_t$ 任务级证据、$V_t$ verifier 结果;$B_{t+1}=\mathrm{Merge}(B_t,E_t,\mathrm{provenance}(O_t))$。它正确地把 GCA 的契约、S-Agent 的双记忆、Skill-3D 的技能(`N_t→A_t→E_t→V_t`)、Think3D 的视角动作统一进一个状态机。

三个补丁(均来自支线证据,GeoTrace 版没有):

**补丁一:$A_t$ 的动作空间必须包含栈层降级动作。** GeoTrace 的动作全是 L5 外部调用,回看旧证据靠文本层 memory lookup。应加入:L2 重绑定回看(已编码视角特征免回放复用)、L3 核心集重选(从已有视角 token 选对象级子集)。"cheap 分支"的正确含义不是便宜的工具,而是**不调工具**。

**补丁二:$O_t$ 永远不直接入上下文,先过翻译层变成 $E_t$。** MINT-CoT 整图交错 64.07→40.37、VisRef 随机 token ≈ 不选——重注入质量层级(整图<随机<相关<相关+多样≈完整对象)是 S-Agent L2→L3 结论的 2D 镜像。新渲染视角图不整幅塞回轨迹。

**补丁三:$B_t$ 的实现规范是 PRCR 三元组。** 视觉记忆=内容+空间坐标+解码位置,混淆任何两个都崩(直接 KV 复用 66.44→23.50,卡死率 81%)。场景记忆的条目应存:视角特征+相机位姿+当前推理步绑定,这让补丁一的 L2 回看成为可能。

## 5. 系统蓝图(GeoTrace 七段 pipeline + 栈层路由器)

```text
Question + multi-view images / video / 3D scene
    ↓
[1] Task compiler         → Ctask = (CR, CO),结构化、可检查
    ↓
[2] Belief & uncertainty  → 持久实体 + 未决空间变量(PRCR 三元组存储)
    ↓
[3] Evidence-need predictor → 先预测证据需求,不直接跳工具名
    ↓
[3.5] 栈层路由器(本版新增) → 免费门控信号三级判定:
      直接作答(首 token 熵低) | 降层复用(L2 重绑定/L3 重选,证据已在上下文)
      | 升层观察(logit 间隔确认上下文确实缺信息,才进 [4])
    ↓
[4] Skill retriever & tool router → 便宜(检测/深度)优先,重建/渲染最后
    ↓
[5] Tool executor
    ↓
[6] Observation compiler  → 原始输出 → typed, frame-aware, provenance-linked evidence
    ↓
[7] Verifier              → frame / identity / geometry / sufficiency 四检查
    ↓
answer ← sufficient   或   belief update → retry / fallback / 新技能 lesson
```

路由器的三个信号全部免训练:首 token 熵(SDR-MCoT,token -68%)、top1-top2 logit 间隔(DaP-ICoT,token -72.6%)、答案分布熵(VisRef,自适应停止)。放在 Pi3 重建 21.35 秒面前,这个路由在 3D 的性价比比 2D 高一个数量级——**与 GeoTrace 用 reward 惩罚控成本的思路不同,门控不占 RL 优化预算**。四类 verifier(frame/identity/geometry/sufficiency)采纳 GeoTrace 原表,不重复。

## 6. 训练配方(合并两版,七条规则为纲)

轨迹格式采纳 GeoTrace 版的 XML 骨架(`ctask/uncertainty/evidence_need/skill_choice/tool_call/observation[loss_mask]/evidence/verify/answer`),数据采纳它的四类正样本(direct-answer/memory-reuse/new-observation/recovery)与五类负轨迹(wrong_frame/wrong_identity/stale/redundant/fabricated)。在此之上,支线的七条已验证规则:

| # | 规则 | 支线证据 | 对蓝图的修正 |
|---|---|---|---|
| 1 | 冷启动建协议,RL 只做选择 | DeepEyesV2 pioneer experiment:直接 RL 两种失败模式 | Stage 1 SFT 不可省;RL 健康信号=调用频率降+方差留 |
| 2 | 奖励条件化,禁过程/频率/执行奖励 | DeepEyes 条件 75.1 vs 无条件 72.1 vs 无 53.4;Thyme 过程奖励 62.9 vs 65.7 | **修正 GeoTrace 的多 λ 奖励:先只用 `R_ans + 1[R_ans>0]·R_evidence`,其余项等 Step 1 审计指出缺什么再加**——每个 λ 都是 reward hacking 的新表面 |
| 3 | 工具观察掩蔽出 loss | Thyme:掩蔽是最关键恢复步骤 | GeoTrace 已采纳,沿用 |
| 4 | 重注入粒度决定成败 | MINT-CoT 64.07→40.37 | 补丁二 |
| 5 | teacher 轨迹降级为可行域 | PFlowNet:专家框最紧≠最有用;λ 中间最优 | **修正 GeoTrace 的数据主路**:teacher 只给必要证据集合+禁止行为,工具顺序留给策略探索——这同时解同源耦合病 |
| 6 | 视觉记忆三元组 | PRCR 卡死率 81% | 补丁三 |
| 7 | 免费门控组合 | 三信号零训练、无人组合过 | 第 5 节路由器;引擎最小工具链真值可标定门控召回 |

训练阶段沿用 GeoTrace 的 Stage 0-3(先验证轨迹可执行→SFT→RL→离线技能演化),其中 Stage 3 的"离线阶段式演化"有 Skill-3D Figure 5 的直接证据支持(在线更新技能库导致非平稳,冷启动+冻结库最稳),采纳。

## 7. 评测:反事实矩阵 + 四象限修正

GeoTrace 版的反事实矩阵(no-tool / no-observation / shuffle / coordinate perturbation / identity swap / irrelevant perturbation / matched-compute self-refine / trace-language swap)与三指标(TNG/CGF/IER)是三版旧洞察里最锋利的设计,采纳为审计协议的主体。两个修正:

**修正一:TNG 只测量了 2×2 矩阵的一行。** `TNG = Acc_full − Acc_no-observation` 是推理时干预;它低,可能是"工具没用",也可能是"工具在训练时有用、推理时冗余"。判决需要训练轴:{训练有/无工具}×{推理有/无工具} 四象限。DeepEyes 的 HR-8K 消融(72.6 vs 60.8)就是"训练轴差异大、推理轴差异小"的实例——按旧解释学它会被误判为工具无用。

**修正二:指标真值必须来自引擎,不能来自 GPT 裁判。** Reference Frame Accuracy、Evidence Sufficiency、CGF 在真实图像上没有真值可标,最终请 GPT 裁判就回到了同源耦合。Oracle3D-Gym(场景程序+完整几何真值+由真值反向生成的问题+证据规范)让反事实翻转的"应然方向"可程序化判定,最小工具链真值让"过度调用"与"no-tool 校准"有非启发式标注。

## 8. 发散:五个两版都没有的启示

**8.1 反事实门控奖励(把因果性直接训进去)。** DeepEyes 把工具奖励条件化于答案正确;引擎底座允许更强的条件化——**工具分只发给"扰动其输出后答案按几何真值方向翻转"的调用**。这把奖励从相关(调了且答对)推进到因果(答案确实依赖它),是对 reward hacking 最根本的封堵。风险:可能训出对一切扰动过敏的策略,需配 IER(无关扰动稳定性)做对偶正则。这个奖励在真实数据上不可实现(无翻转真值),是引擎底座独有的方法学红利——如果 Oracle3D-Gym 只能支撑一个新方法点,应该是它。

**8.2 技能库是脚手架假说的免费测量仪——也可能是仪式的孵化器。** Skill-3D 的技能=固化的工具序列。若脚手架假说成立,健康的技能演化应表现为"每技能平均调用数随轮次单调下降、ETU-per-call 不降"——技能库漂移曲线就是脚手架拆除曲线,不需要额外实验。反过来一个可检验的新预测:**检索增强 agent(Skill-3D)的仪式化调用率应高于 RL agent(Think3D-RL)**,因为技能把工具序列固化成先验,而 RL 的调用每一步都被最终奖励重新审判。这直接给第 10 节的跨 baseline 审计一个具体假设。

**8.3 把门控、停止、奖励统一成一个量:每次调用的信息价值(VoI)。** VisRef 的答案分布熵实际上是逐步 VoI 估计器:调用前后各测一次答案熵,差值就是该观察的经验信息增益。引擎里 VoI 有真值(该观察在最小工具链里/不在)。于是三件事变成同一件:门控=预测 VoI>成本才调用;停止=预测剩余 VoI≈0;奖励=按实现的 VoI 分配。当前文献把这三者当三个部件设计(SDR-MCoT 管路由、VisRef 管停止、DeepEyes 管奖励),统一成 VoI 校准问题后,一个头可以同时做三件事——这可能是"停止/验证策略"空位的最优解法形态。

**8.4 一次训练,两个部署产品。** 四象限判决后不必二选一:同一次工具轨迹训练可产出 (i) 无工具蒸馏版,服务 (c) 主导的负载(多数 benchmark 与日常查询);(ii) 最小 agent 版,只保留 (a) 类调用+门控路由,服务真机制负载。前置一个"产品选择器"——预测该问题的最小工具链是否为空——引擎真值可直接监督它。这把"agent vs 蒸馏"的路线之争变成一个路由问题,部署成本结构随之改写。

**8.5 视频里的动态参考系是 (a) 类必要性的天然栖息地——而现有最强 agent 恰好在那里得分为零。** 构造 (a) 类题在静态场景要靠引擎;视频里它自然发生(运动+遮挡使初始编码可证不足,`CR(t)` 随相机演化)。关键观察:S-Agent 在 VSI-SUPER 长视频上靠帧选择大胜(VSR 超基线 37.2 点),但在**变化推理 VSC 子集上长时段几乎为 0**。这是全目录最被低估的一个数字:agent 赢在证据组织(帧选择、翻译),输在真正需要跨时间状态追踪的地方——与脚手架假说的预测严格一致(组织性收益可以蒸馏,状态追踪机制还不存在)。**VSC 类任务是"机制"判决最可能出现阳性结果的地方,也是 GeoTrace 的 `CR(t)` 扩展真正值得投入的场景。**

## 9. 对两份前作的逐项裁决(不盲从的账本)

| 来源          | 部件                                                                | 裁决          | 理由                                          |
| ----------- | ----------------------------------------------------------------- | ----------- | ------------------------------------------- |
| GeoTrace    | belief-update 轨迹 $(B,C,U,N,A,O,E,V)$                              | **采纳**      | 正确统一了四篇论文的部件;是轨迹语法的最优形态                     |
| GeoTrace    | typed evidence 格式、四类 verifier                                     | **采纳**      | 与 S-Agent L3/GCA 证据一致                       |
| GeoTrace    | 四类正样本+五类负轨迹                                                       | **采纳**      | 负轨迹分类学完整;引擎里五类负例是免费副产品                      |
| GeoTrace    | 反事实矩阵 + TNG/CGF/IER                                               | **采纳+修正**   | 协议主体保留;TNG 需扩为四象限(第 7 节修正一)                 |
| GeoTrace    | 多 λ 奖励 $R_{ans}+\lambda_f R_{frame}+\lambda_i R_{identity}+\dots$ | **修正**      | Thyme/DeepEyes 证据:每加一项都有失效先例;最简起步,审计驱动加项    |
| GeoTrace    | teacher 轨迹为数据主路                                                   | **修正**      | 落进同源耦合+benchmark 过拟合;PFlowNet 可行域监督替代(规则 5) |
| GeoTrace    | 动作空间=外部工具                                                         | **修正**      | 缺 L2-L4 降层动作(补丁一);成本控制应门控优先、reward 兜底       |
| GeoTrace    | 指标由 GPT 裁判标注                                                      | **搁置**      | 换引擎真值(第 7 节修正二)                             |
| GeoTrace    | Stage 0-3 训练阶段、离线技能演化                                             | **采纳**      | Skill-3D Fig.5 直接支持离线阶段式                    |
| fable5 融合版  | 机制-脚手架三分、三推论                                                      | **保留为判决框架** | 本文第 3 节                                     |
| fable5 融合版  | 栈层映射、七条规则                                                         | **保留并入蓝图**  | 第 5、6 节                                     |
| fable5 单目录版 | Oracle3D-Gym 底座、反事实协议                                             | **保留为底座**   | 第 7 节修正二;8.1 的奖励只能建在它上面                     |

两版共同的正确直觉值得记录:三次独立综合(GeoSkill、GeoTrace、机制-脚手架)都收敛到"参考系第 0 层、翻译层必须、观察掩蔽、no-tool 样本、反事实审计"——这五件事已经不是假设,是这批文献的定论。

## 10. 【专章】以 Skill-3D / Think3D / S-Agent 为核心 baseline 的落地方案

> 本章独立于前文:前文是"该做什么研究",本章是"用这三个系统怎么把它做出来"。三者当 baseline 的理由、统一 harness、三个实验、复现细节、产出映射,全部落到可执行粒度。

### 10.0 为什么恰好是这三个

它们覆盖三条正交能力轴 × 三种范式,且互相构成对照:

| Baseline | 能力轴 | 范式 | 对判决实验的独特价值 |
|---|---|---|---|
| [Skill-3D](<3d agent/Skill-3D/paper_DeepPaperNote.md>) | 跨问题经验沉淀(证据路由) | 检索增强 + 后训练(SFT 500 + GRPO 1k) | 自带 ETU 指标可直接对照反事实翻转率;技能库漂移=脚手架测量仪(8.2);**预测:仪式化率最高** |
| [Think3D](<3d agent/Think3D/paper_DeepPaperNote.md>) | 主动观察(视角策略) | 纯 RL(977 样本,无轨迹标注) | 唯一有 Self-Refine 等成本对照的;RL 策略 vs 随机/启发式三档现成;**预测:相机运动类任务上因果性最高** |
| [S-Agent](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>) | 工具后翻译+记忆(证据编译) | 分层专家 + 大规模蒸馏(S-300K) | L3 专家输出是确定性翻译,扰动传播路径最干净;双记忆支持 stale-observation 反事实;**预测:扰动敏感性最高、但 VSC 为 0 暴露机制缺失** |

GCA 不作第四 baseline,作**可插拔消融模块**:`Ctask` 形式化可以加到三者任何一个头上(它自己的消融已证明 +7.5 独立于工具收益)。

### 10.1 统一 harness(先做,所有实验共用)

**工具池取并集,版本冻结**:Pi3(重建,~21.35s/7 帧;VGGT 备胎,Think3D Table 4 证明可换)、GroundingDINO(检测)、SAM3(分割)、Depth-Anything-3 室内度量版(深度)、Orient Anything v2(朝向)、SwinIR(超分)、T* 关键帧搜索。**本地仓库已有 GroundingDINO 与 DA3METRIC-LARGE 权重**(S-Agent 笔记确认与 `checkpoints/` 对应),缺口是关键帧搜索与朝向专家的接线。

**Benchmark 分层**:
- 交集层(三者可比):VSI-Bench(统一 7 帧采样协议,Skill-3D/Think3D 已共用)、MMSI-Bench(Skill-3D 与 S-Agent 共用)、BLINK-MV(Skill-3D 与 Think3D 共用);
- 特长层(单 baseline 主场,用于验证复现):MindCube(Think3D RL 训练域)、ViewSpatial(S-Agent 消融主场)、CV-3D(Skill-3D);
- 判决层:Oracle3D-Gym 切片(100-200 个 Blender 场景起步,每题带最小工具链+参考系真值)+ ReVSI/VSI-SUPER 的 VSC 子集(8.5 的天然 (a) 类)。

**统一成本记账**(三篇论文口径不一,S-Agent 干脆没报):每调用记 wall-clock(已知锚点:Pi3 21.35s / 深度 1.51s / 分割 0.77s / 朝向 0.88s)、调用数、token、轮数。主表每格都是"准确率@成本"双值。

**两个已知的坑**:MMSI 计分是否按选项字母对齐要先核(仓库有过 harness 计分口径 bug 的记录,对比论文数字前必须过一遍);Skill-3D 的 30%/70% 拆分是作者自拆,复现要么拿到他们的拆分要么自己重拆并同时报两种。

**骨干统一**:可训练对比全部用 Qwen3-VL-4B/8B(三篇都用过,数字可锚);零样本行加一个强闭源规划器(GPT-5.4 或 Gemini 3 Pro,S-Agent/Skill-3D 的主设置)。

**代码现状**:Think3D 开源(github.com/zhangzaibin/spagent,含模型和数据,最省事);Skill-3D 有项目页(skill-3d.github.io,代码放出程度待查);S-Agent 只有项目页,大概率要按笔记的工具清单重实现——但它的工具栈与本地权重重合度最高,重实现成本主要在五类专家和双记忆的逻辑,不在模型。

### 10.2 实验一:三 baseline 审计(判决先行,零训练,2-3 周)

对每个 baseline 在交集层+判决层跑成功轨迹,做三种推理时干预:

1. **删除**(Position 协议):保留 tool-call 叙事,删真实观察 → 逐 baseline 的 TNG;
2. **扰动**(引擎判定应然方向):深度 ±20%、参考系旋转 90°、实例错绑 → 反事实翻转率,与表面 ETU 对照;
3. **等成本对照**:Think3D 的 Self-Refine 协议推广到三者(同 token/时延预算的纯文本多轮)。

产出一张主表:`baseline × {Acc, ETU, TNG, 翻转率, (a)(b)(c) 构成占比, Acc@Cost}`。三个预注册假设:

- **H1(仪式化排序)**:Skill-3D 翻转率 < Think3D-RL(技能固化序列 vs 逐步受审的策略,8.2);
- **H2(任务依赖)**:三者在相机运动/视角类任务(MindCube、ViewSpatial 人物视角)上翻转率显著高于计数/尺寸类(VSI)——即 (a) 类构成决定因果性,不是方法决定;
- **H3(裂口存在)**:至少一个 baseline 出现"ETU 高、翻转率低"的显著裂口(比如 ETU 80% 的轨迹只有一半对干预敏感)——裂口本身就是 analysis paper 的核心图。

**这张表无论长什么样都可发表**:H3 成立则证明底座必要;H3 不成立(ETU≈因果)则说明 ETU 已够用,全领域可以放心用便宜指标——同样是结论。

### 10.3 实验二:每个 baseline 一个最小升级(验证支线规则,3-4 周)

每个升级只动一个部件,可单独成为消融行:

| Baseline | 升级 | 验证的规则 | 现成对照 |
|---|---|---|---|
| Skill-3D | 技能检索前加**门控路由**(首 token 熵判"这题需要技能/工具吗") | 规则 7 | 它自己的 no-skill 消融行(64.1)+ 效率表(20.8s) |
| Think3D | 固定 3 轮改为**答案熵停止** | 停止策略空位 | 它自己的轮数消融(Fig.6:未 RL 模型加轮无益) |
| S-Agent | 场景记忆条目改存 **PRCR 三元组**(视角特征+位姿+步绑定),回看走重绑定不重调 L1/L2 | 规则 6 / 补丁三 | 它自己的记忆消融行(58.2/57.6→60.0) |

预期:三个升级都应在 Acc@Cost 前沿上向外推(准确率持平或升、成本显著降)。若某个升级失败,失败模式同样有信息量(比如门控信号在 3D 多选题上失准 → 界定门控的适用域)。

### 10.4 实验三:四象限判决(训练侧,1-2 月)

选成本最低的两条训练路径:

- **Think3D-RL 配方**(977 样本、8×H200、GRPO、配置全公开)——RL 象限;
- **Skill-3D 后训练配方**(500 SFT + 1k RL、4×RTX PRO 6000、SFT 3h + RL 28h,全目录最便宜的完整配方)——SFT+RL 象限;S-300K 太大,取其"难度采样+多粒度分解"配方做子集即可。

在两组题上各训四格:{训练有/无工具}×{推理有/无工具}。题组:(a) 类保证组(引擎生成:遮挡背面/新视角依赖,按构造不调工具无法作答)+ 普通组(VSI/MMSI 子集)。判决读法:

- 普通组上"训练有+推理无"≈"训练有+推理有" → 脚手架确认,走 8.4 的双产品部署;
- (a) 组上推理时删图显著掉分 → 机制确认,投资 8.3 的 VoI 统一头;
- **两者同时出现是最好结局**:Position paper 的批评与工具训练的价值各归其位。

### 10.5 产出映射与时间线

| 阶段 | 内容 | 产出 |
|---|---|---|
| Phase 0(1-2 周) | harness 统一、复现三 baseline 论文数字(容差内)、MMSI 计分核对 | 可信的对照基线 |
| Phase 1(2-3 周) | 实验一审计 | **Analysis paper**:「表面 ETU vs 反事实因果」+ (a)(b)(c) 构成测量 |
| Phase 2(3-4 周) | 实验二三升级 | 方法论文的消融主体;或独立 efficiency 短文 |
| Phase 3(1-2 月) | 实验三四象限 | **主论文**《Mechanism or Scaffold? Disentangling Tool-Use Gains in 3D Spatial Reasoning》 |

风险与规避:S-Agent 重实现量最大 → Phase 0 先只接 L1+L2+相对位置/度量两个专家,其余专家按审计需要增补;Skill-3D 技能蒸馏依赖 GPT-5.4 → 复用其公开技能库(若放出)或用可行域协议重蒸馏(规则 5,顺手完成方法升级);闭源 API 成本 → 零样本行只跑交集层的抽样子集;引擎 (a) 类题的人工痕迹质疑 → 附"单视角人类也答不对"的行为学对照。

### 10.6 本章一句话

三个 baseline 不是三个对手,是判决实验的三个测量通道:Skill-3D 测检索范式的仪式化上限,Think3D 测 RL 范式的因果性下限,S-Agent 测翻译层的扰动传播——三条通道汇到同一张四象限表上,3D 工具使用的"机制还是脚手架"第一次变成可测量的问题。

## 11. 结论

两版前作各自把一半问题做对了:GeoTrace 版给出了轨迹应有的语法(belief-update program + 反事实审计),机制-脚手架版给出了轨迹应受的判决(哪些调用值得存在、存在于何处)。合并后的完整主张:

> **先判决,再建造。用 Skill-3D / Think3D / S-Agent 三条测量通道 + 引擎真值,先回答"3D 工具调用是机制还是脚手架";判决结果决定 GeoTrace 蓝图的每个部件放在训练时(可蒸馏拆除)还是推理时(配门控与 verifier)。跳过判决直接建系统,是在未审计的假设上加杠杆——这正是当前所有 3D agent 论文共同的状态。**

最先做的一件事不变:Phase 1 的审计实验。它便宜、零训练、三个预注册假设无论真假都可发表,且是后续一切选题的依据。

## 12. 来源

**核心 baseline**:[Skill-3D](<3d agent/Skill-3D/paper_DeepPaperNote.md>)(arXiv:2606.07436,项目页 skill-3d.github.io)· [Think3D](<3d agent/Think3D/paper_DeepPaperNote.md>)(arXiv:2601.13029,代码 github.com/zhangzaibin/spagent)· [S-Agent](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>)(arXiv:2606.20515,S-300K)

**3D 主线其余**:[GCA](<3d agent/Geometrically-Constrained Agent for Spatial Reasoning/paper_DeepPaperNote.md>) · [Thyme](<../Reasoning/Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>) · [DeepScan](<3d agent/DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models/paper_DeepPaperNote.md>) · [A4-Agent](<3d agent/A4-Agent An Agentic Framework for Zero-Shot Affordance Reasoning/paper_DeepPaperNote.md>) · [CompassAD](<CompassAD - Intent-Driven 3D Affordance Grounding in Functionally Competing Objects.md>) · [P3D-Bench](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>) · [Code2Worlds](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>) · [MPMWorlds](<3d agent/MPMWorlds Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics/paper_DeepPaperNote.md>) · [Gamma-World](<3d agent/Gamma-World Generative Multi-Agent World Modeling Beyond Two Players/paper_DeepPaperNote.md>) · [SimWorld Studio](<3d agent/SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning/paper_DeepPaperNote.md>)

**Reasoning 支线**:[DeepEyes](<../Reasoning/Train/DeepEyes Incentivizing Thinking with Images via Reinforcement Learning/paper_DeepPaperNote.md>) · [DeepEyesV2](<../Reasoning/Train/DeepEyesV2 Toward Agentic Multimodal Model/paper_DeepPaperNote.md>) · [MINT-CoT](<../Reasoning/Train/MINT-CoT Enabling Interleaved Visual Tokens in Mathematical Chain-of-Thought Reasoning/paper_DeepPaperNote.md>) · [PatchCue](<../Reasoning/Train/PatchCue Enhancing Vision-Language Model Reasoning with Patch-Based Visual Cues/paper_DeepPaperNote.md>) · [PFlowNet](<../Reasoning/Train/Perceptual Flow Network for Visually Grounded Reasoning/paper_DeepPaperNote.md>) · [Qwen-LA](<../Reasoning/Train/Qwen Look Again Guiding Vision-Language Reasoning Models to Re-attention Visual Information/paper_DeepPaperNote.md>) · [IVT-LR](<../Reasoning/Train/Reasoning in the Dark Interleaved Vision-Text Reasoning in Latent Space/paper_DeepPaperNote.md>) · [ICoT](<../Reasoning/TrainingFree/Interleaved-Modal Chain-of-Thought/paper_DeepPaperNote.md>) · [DaP-ICoT](<../Reasoning/TrainingFree/Lets Think with Images Efficiently An Interleaved-Modal Chain-of-Thought Reasoning Framework with Dynamic and Precise Visual Thoughts/paper_DeepPaperNote.md>) · [SDR-MCoT](<../Reasoning/TrainingFree/Mitigating Low-Quality Reasoning in MLLMs Self-Driven Refined Multimodal CoT with Selective Thinking and Step-wise Visual Enhancement/paper_DeepPaperNote.md>) · [PRCR](<../Reasoning/TrainingFree/Position Rebinding Cache Reuse Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning/paper_DeepPaperNote.md>) · [Position paper](<../Reasoning/TrainingFree/Position Your VLM May Not Be Thinking with Interleaved Images/paper_DeepPaperNote.md>) · [REALM](<../Reasoning/TrainingFree/REALM An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting/paper_DeepPaperNote.md>) · [VisRef](<../Reasoning/TrainingFree/VisRef Visual Refocusing while Thinking Improves Test-Time Scaling in Multi-Modal Large Reasoning Models/paper_DeepPaperNote.md>)

**洞察文档谱系**:[3d_insight](<3d_insight.md>)(GeoSkill-Agent)· [3d_insight_with_reasoning](<3d_insight_with_reasoning.md>)(GeoTrace-Agent,本文语法来源)· [3d_insight_fable5](<3d_insight_fable5.md>)(Oracle3D-Gym)· [3d_insight_with_reasoning_fable5](<3d_insight_with_reasoning_fable5.md>)(机制-脚手架,本文判决来源)· [Reasoning_insight](<../Reasoning/Reasoning_insight.md>) · [Reasoning_insight_fable5](<../Reasoning/Reasoning_insight_fable5.md>) · 总览:[Overall](<3d agent/Overall.md>)

> 证据边界声明:全部数字引自本地精读笔记(经 grounding 核对),未重访原始 PDF。第 8 节五个启示、第 10.2 节三个预注册假设(H1-H3)均为我的推断,任何论文未如此表述;其中 8.1 反事实门控奖励未经任何实验验证,8.2 的"检索范式仪式化率更高"是可证伪假设而非结论。工具耗时数字(Pi3 21.35s 等)取自 Skill-3D 附录的特定硬件环境,迁移到本地环境需重测。
