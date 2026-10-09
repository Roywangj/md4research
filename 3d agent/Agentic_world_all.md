# Agentic World 合并版：可投稿的分阶段实验路线（GPT 语法 × Fable 5 判决）

> 写作时间：2026-07-03。合并 [Agentic_world](<Agentic_world.md>)（GPT 版：架构语法与工程细节最完整）与 [Agentic_world_fable5](<Agentic_world_fable5.md>)（Fable 5 版：消融数字、代码审计、判决实验）。合并原则沿用 [3d_insight_with_reasoning_all](<3d_insight_with_reasoning_all.md>) 的做法：**冲突处逐项裁决而非平均**——GPT 版好的部分作为工程语法直接采纳，与证据冲突处明确修正（§1 裁决表）。本版新增两件事：①**3DCodeBench 已联网核实**（arXiv:2606.01057 + GitHub README 逐条核对），Fable 5 版的"命名勘误"作废；②全文按"最短路径到可投稿结果"重排成三个里程碑（§4），每个里程碑独立成文。

---

## 0. TL;DR

1. **两版共识，不再论证，直接执行**：代码是 4D 世界的中间介质；把 Code2Worlds 的固定 pipeline 拆成可选工具；LLM planner 输出轨迹；轨迹（成功+失败）训练 agent。GPT 版的四件工程语法全盘采纳：两层表示（backend-agnostic WorldSpec + backend 代码）、双记忆（World Memory / Agent Memory）、技能库、结构化 action JSON。
2. **3DCodeBench 核实为真，且它改变两个判断**。已核实：基于 Infinigen/Infinigen-Indoors 资产蒸馏成 **standalone Blender 5.0 脚本**、212 类、单轮 / 多轮（T=3 traceback 重试）/ coding-agent（Claude Code、Codex、Gemini CLI）三设置、指标含 executability/SigLIP-2/DINOv3/Chamfer/Uni3D/LLM-judge + 3DCodeArena 人类偏好。含义一：**对象层解耦有现成起点**——3DCodeData 本身就是"把 infinigen 从运行时依赖变成数据来源"的成品，Fable 5 版 §3.3 的 L2 反蒸馏从"二期研究项目"降级为"下载并适配"。含义二：它的失败分析（执行失败主因是 API mismatch；跑通的渲染仍有断连/漂浮几何）直接支持 critic 分层——**"能跑"和"形状对"是两个独立的 critic，traceback 反馈只修前者**。
3. **保留 Fable 5 版的五个判决**（证据见原文，不重复）：①库先验>planner（去检索 SGS 61.4→23.5 vs 去 critic →58.6）；②解耦是轨迹收集的前置条件（发布版动力学脚本强制 `USER_FILL` + 禁自动烘焙）；③planner 增益需判决实验，不能假设（工具序列熵审计）；④引擎即 oracle，Indoors 约束 DSL 是现成 reward 语言；⑤人类反馈放校准位不放主奖励位（Indoors 代理分数错位先例 86.20>80.84 但视觉更差）。
4. **对 GPT 版的三个不盲从**（§1 有完整裁决表）：①**拒绝五项固定权重奖励**（0.25/0.25/0.25/0.15/0.10）——多 λ 奖励每加一项都是被刷分的新面，改为阶段化最简奖励 + 审计驱动加项（§3）；②**Experiment 1 预设 planner 赢，改为双向判决实验**——可能的结论是"3D 部分低熵用固定骨架、4D 部分高熵才需要 agent"，这个结论本身可发表；③**补上它完全缺失的最近邻 SimWorld Studio 与弱 planner 警告**（S-Agent：8B 直接套框架 30.7 < 基座 31.1）——不补这两个，相关工作和结论在审稿时都站不住。
5. **投稿路径**：M1（第 1–8 周，零训练）= 判决实验 + AgenticWorld-Bench，投 benchmark/dataset track 或 workshop；M2（第 9–18 周）= 轨迹蒸馏 agent，投主会；M3（远期）= RL + 约束奖励 + 与理解端的共同演化飞轮。每个里程碑失败了也有可写的结论（§4 逐条给出"若失败意味着什么"）。

---

## 1. 对 GPT 版的逐项裁决表（不盲从的明账）

| GPT 版组件 | 裁决 | 理由 / 补丁 |
|---|---|---|
| WorldSpec 两层表示 + YAML 示例（§3.1） | **采纳** | 与 Fable 5 版 §3.2 的场景 IR 同构且更具体。补丁：`validation.required_checks` 字段升格为奖励接口（每条 prompt 预注册引擎可验证检查，M1 benchmark 的核心字段） |
| 工具分层 L0–L4（S-Agent 映射，§3.2） | **采纳** | 与 Fable 5 版 t1–t14 工具清单合并；L4（技能/策略记忆）注明"RL 期间冻结"（Skill-3D Fig 5：在线更新技能库导致非平稳） |
| 双记忆 World/Agent Memory（§5.3） | **采纳** | 正确移植 S-Agent 的 Merge/Append 语义 |
| 技能库 YAML（§5.4） | **采纳 + 补丁** | 补：技能是检索式脚手架，蒸馏进参数后要测仪式化率（前作 [3d_insight_with_reasoning_all](<3d_insight_with_reasoning_all.md>) §8.2 的预测：检索范式的仪式化率高于 RL 范式，生成端可顺带验证） |
| 结构化 action JSON（§5.2） | **采纳** | `thought_summary` 保留但不进损失主项 |
| `USER_FILL` → 三个场景自省工具（§7.3） | **采纳** | 两版独立收敛于同一方案（inspect_scene_objects / match_semantic_target / select_support_surface），可信度高，M1 第一周就做 |
| backend capabilities 配置（§7.2） | **采纳** | planner 读 capabilities 不读路径 |
| 双几何（visual / collision_proxy / semantic_parts，§7.4） | **采纳** | 与 Fable 5 版保真度阶梯是同一件事的几何面和渲染面，合并为"粗糙优先"总原则 |
| 五项固定权重奖励（§6.2） | **修正** | 见 §3。Thyme/DeepEyes 有逐项失效先例；Skill-3D 的成功配方就是最简三项 R_ans+R_fmt+R_tool，且防刷分靠冻结解析器而非权重调平 |
| Experiment 1：pipeline vs planner（§8） | **修正** | 从"证明 planner 更好"改成双向判决：加测工具序列熵与 ETU-G，预注册两种结果的解释（§4 E2） |
| Experiment 2：局部 patch vs 全量重写（§8） | **采纳并前置** | 全文性价比最高的实验：便宜、高信号、直接验证 IR 的核心卖点，进 M1 主菜 |
| Experiment 3：轨迹 SFT（§8） | **采纳 + 配方补丁** | 补 S-300K 细节：三粒度分解（51,596 条→292,391 样本的杠杆）、合格率预算（S-Agent 从 800K 源数据只留 51.6K 条，生成端按 <30% 合格率规划 rollout 预算）、SFT 前不发布弱 planner 版本 |
| Experiment 4：技能库（§8） | **采纳**，放 M2 | 对照组设计沿用 Skill-3D 消融行（无技能/仅静态/仅动态/全量） |
| 3DCodeBench 用法（§1.4） | **采纳 + 升级** | GPT 版只当评测与错误分析用；实际上 3DCodeData（standalone 脚本语料）是对象工具库的现成种子——这是本次核实带来的最大增量 |
| 风险四条（§10） | **采纳 + 补数字** | 补成本硬数字：Infinigen 3.5 h/立体对、24 GB、1600 万面；低成本模式清单两版合并 |
| 论文叙事 AgenticWorld（§9） | **采纳 + 补最近邻** | 必须补 SimWorld Studio 差异化（下表），否则 novelty 会被审稿人用它打掉 |
| （缺）SimWorld Studio 定位 | **补** | 见 §2 末表 |
| （缺）消融硬数字与引用纪律 | **补** | 全文数字以 Fable 5 版为准（每个数字落到具体消融表） |
| （缺）引擎即 oracle / 约束 DSL 奖励 | **补** | Fable 5 版 §5.2，是 M3 的核心差异化，M1 就开始埋点（required_checks） |

---

## 2. 统一方案（一页版）

架构 = GPT 版语法 + Fable 5 版补丁，细节看两个父文档，这里只写定版决定：

- **表示**：上层 `WorldSpec`（objects/parts/materials/layout-constraints/dynamics-events/cameras/validation/artifacts），下层后端代码（infinigen gin、bpy 脚本、MeshCoder part-code、3DCodeData standalone 脚本）。WorldSpec 是 planner、记忆、critic、训练共用的唯一状态；后端代码是工具产物。
- **工具箱 v0（约 15 个）**：GPT 版 §5.1 表为准（analyze_task / retrieve_world_skill / init_worldspec / generate_object_spec / generate_scene_layout / generate_material_lighting / generate_dynamics / execute_world / critic_execution / critic_visual_object / critic_layout / critic_motion / critic_physics_numeric / patch_worldspec / export_trajectory），加 Fable 5 版三个场景自省工具替换 `USER_FILL`。对象生成工具的代码来源优先级：3DCodeData standalone 脚本 > infinigen Factory 包装 > MeshCoder part-code（点云输入时）。
- **critic 栈按错误类型分层**（3DCodeBench 的失败分析 + Code2Worlds 双 critic 消融共同支持）：traceback（能跑）→ 几何/连通性（形状对，3DCodeBench 指标直接复用：Chamfer/Uni3D/断连检测）→ 布局约束（Indoors DSL 满足率）→ 运动语义（VLM-Motion，消融证据：去掉后失败率 10%→60%）→ 人类偏好（校准位）。
- **防刷分**：所需证据/检查由**冻结的提示解析器**决定（Skill-3D 的 R_exec 细节），不由 planner 自己声明。
- **与最近邻的差异化定位**（写论文时的 related work 骨架）：

| 维度 | Code2Worlds | 3DCodeBench | SimWorld Studio | 本方案 |
|---|---|---|---|---|
| 对象 | 世界（4D） | 单对象（3D） | 环境（导航任务） | 世界（4D） |
| 控制流 | 固定 pipeline | 单轮/多轮重试/现成 coding-agent | 编码 agent + 验证器 | **可训练的工具调用策略** |
| 中间表示 | gin+散落 JSON | standalone 脚本 | UE5 场景+技能文档 | **统一 WorldSpec IR** |
| 学习 | 无（prompt 编排） | 无（评测） | 上下文演化，权重不动 | **轨迹 SFT→RL 进参数** |
| 评测 | 10 条提示+GPT 判分 | 212 类+执行/几何指标 | 规则+VLM+下游导航 | **引擎 required_checks+轨迹级指标** |

---

## 3. 奖励设计：阶段化最简主义（对 GPT 版的最大修正）

GPT 版一步到位给了 `R = 0.25·R_exec + 0.25·R_semantic + 0.25·R_dynamic + 0.15·R_structure + 0.10·R_efficiency`。拒绝理由：①五个权重没有任何一个有证据支撑；②每个奖励项都是一个可被策略钻空子的面，Reasoning 目录的先例是加项越多越难归因（前作 all 版 §6 规则 2 的同一判决）；③Skill-3D 拿到 +60% 后训练收益用的就是最简三项。改为：

| 阶段 | 奖励构成 | 升级条件 |
|---|---|---|
| R0（M1，零训练） | 无奖励，只做轨迹过滤：执行成功 ∧ required_checks 通过 ∧（抽样）人评合格 | — |
| R1（M2，SFT/初期 RL） | `R_ans`（required_checks 通过率，含约束 DSL 满足率）`+ R_fmt`（IR 合法性）`+ (R_exec − |A|/B)`（Skill-3D 原式，冻结解析器判定所需产物） | 审计发现刷分模式 |
| R2（M3） | R1 + 门控的 `R_dynamic`（仅当 R_ans>0 时计入运动语义分，避免"动得好看但世界是错的"） | R1 审计显示动态项系统性偷懒 |
| 审计指标（永不进奖励，只做监控） | 代码结构分、工具效率、轨迹熵、ETU-G、仪式化率 | 若监控显示恶化再讨论升格 |

人类反馈的固定协议：每轮训练抽高奖励轨迹盲评，奖励-偏好相关性下降即触发重校准（Indoors 错位先例是这条协议的存在理由）。

---

## 4. 实验阶梯：三个里程碑，每个独立可投稿

### M1（第 1–8 周，零训练）：解耦 + 判决 + AgenticWorld-Bench

**W1–2 解耦冲刺**（验收标准就是实验 E0）：
- 包装 Code2Worlds 现有 11 个组件为 JSON 工具（GPT 版 §7.1 的映射表照做）；
- `USER_FILL` 三工具替换；物理烘焙可编程触发；backend 路径进 capabilities 配置；
- **E0 指标：无人值守率**——同一批提示，改造前后能全自动跑完的比例。这是第一个可报告数字，也是解耦主张的直接证据。

**W3–6 两个判决实验**：
- **E1（局部 patch vs 全量重写**，GPT 版 Exp2 前置）：注入 5 类错误（对象外观 / 布局穿插 / 刚体不动 / 流体不显 / API 报错），比较 patch_worldspec 与整段重写。指标：修复成功率、新增错误率（回归）、修改量、重跑成本。预期 patch 显著占优——**这是 WorldSpec IR 价值的直接证明，也是最便宜的正结果**。若失败：说明 IR 粒度设计错了，比训练失败便宜一百倍地暴露问题。
- **E2（固定 pipeline vs 教师 planner vs 单轮 bpy**，判决版）：60–100 条提示，六类（outdoor 光照天气 / indoor 静态 / 刚体接触 / 流体粒子 / 风驱植被 / 对象 only），三个系统同预算对比。常规指标（执行成功率、required_checks 通过率、人评、成本、不必要调用率）之外，加两个判决指标：**工具序列熵**（每类提示的轨迹骨架分布）与 **ETU-G**（扰动工具输出后最终世界是否变化）。预注册双向假设：若熵低（≥90% 轨迹共享骨架），结论是"固定骨架 + 学习的跳步门控 + 学习的修补策略"，全自由规划是脚手架；若熵高（尤其 4D 部分），才支持全自由 planner。**两种结果都可写**——"什么时候需要 agent"比"agent 更好"是更稀缺的结论。

**W6–8 打包 benchmark**：
- **AgenticWorld-Bench v0**：Code4D 的 10 条扩到 60–100 条，每条带 WorldSpec 真值骨架 + 引擎可验证 `required_checks`（执行/碰撞/接触/运动方向/约束满足）+ 分层 critic 报告格式。与 3DCodeBench 的差异化写明：它测对象级 3D 代码，我们测世界级 4D 轨迹；它的 212 类 standalone 脚本反过来是我们对象工具的语料。
- **投稿位**：datasets & benchmarks track / workshop。内容 = E0+E1+E2 审计结论 + bench。零训练、8 周、纯判决性论文，这是短期最稳的出手点。

### M2（第 9–18 周）：轨迹蒸馏 agent（主会目标）

- **轨迹收集**：强教师 planner 跑 bench 提示的训练拆分，目标 200–500 条合格轨迹；按合格率 <30% 预算 rollout（S-Agent 的过滤先例），全程低保真档（Eevee 低采样 + proxy 几何 + 短 rollout + 关键帧渲染），R0 过滤。
- **三粒度分解 SFT**（S-300K 配方）：整轨迹 / 回合级 / 单工具级，一条轨迹放大约 5 倍监督；失败轨迹不进 next-action SFT，只进 critic-to-patch 训练与技能教训（GPT 版 §10.4 与 Skill-3D 失败教训在此合流）。
- **E3（蒸馏有效性）**：Skill-3D/S-Agent 式对照——基座 vs 基座+框架（**预期反向**，复现弱 planner 警告即是一个结果）vs SFT 后。判据：SFT 小模型达到教师通过率的目标百分比、ETU-G、平均轮数与成本。
- **E4（技能库）**：无技能 / 检索技能 / SFT 内化，测失败类型复发率与仪式化率（顺带验证前作 all 版 §8.2 的检索-vs-RL 仪式化预测）。
- 若 E3 失败（小模型学不会）：回退结论仍可写——"生成端轨迹的可蒸馏性低于理解端"，配熵审计解释原因。

### M3（远期）：RL + 约束奖励 + 飞轮

- R1→R2 奖励阶梯上 GRPO（Think3D 的量级预期：裸工具 +0.80 vs RL +12.05，策略对照 Random 36.68 / Heuristic 38.69 / RL 47.11）；
- 反事实门控奖励（扰动工具输出→重执行→diff 最终世界，生成端全程序可测）；
- 与理解端闭环：生成的世界自带真值 → 出可验证空间 QA/导航任务 → 理解端 agent（Skill-3D/Think3D/S-Agent 线）训练评测 → 失败分布反哺"下一批生成什么世界"（SimWorld 共同演化 +18 个百分点的先例）。

---

## 5. 风险与成本（两版合并）

| 风险 | 证据 | 对策 |
|---|---|---|
| 后端太重，rollout 撑不起训练 | Infinigen 3.5 h/立体对、24 GB、1600 万面、10000 spp | 保真度阶梯常驻：IR 静态校验（免费）→ Eevee 低采样 → 低 substep 物理 → Cycles 只留最终交付；"粗糙动态世界"是产品定位不是妥协 |
| 只学会 Infinigen quirks | 轨迹全来自单后端 | WorldSpec 抽象 + 3DCodeData standalone 脚本混入 + 后端迁移评测（同一 WorldSpec 编译到两个后端） |
| 自动 critic ≠ 真实物理 | Code2Worlds 精读：VLM 只判"看起来合理"，不同参数组合可产生相似视频 | claim 控制在 "engine-executed, visually/semantically plausible"；不声称系统辨识 |
| 代理奖励被钻空子 | Indoors 86.20>80.84 但视觉更差 | §3 的人类校准协议 + 审计指标永不进奖励 |
| 失败轨迹教坏模型 | GPT 版 §10.4 判断正确 | 失败只进 patch 训练与教训，不进 next-action SFT |
| 长尾被过滤复制进 agent | MeshCoder 36% 筛除先例 | 保留"失败但可修复"轨迹层；bench 里保留无解提示做拒绝行为评测 |

---

## 6. 一句话

**GPT 版给了正确的机器（WorldSpec + 工具箱 + 双记忆 + 技能库），Fable 5 版给了正确的顺序（先解耦、先判决、先最简奖励、先零训练出一篇）。合并后的路线是：8 周拿到判决数字和 benchmark 出第一篇，18 周拿到蒸馏 agent 出主会，远期用引擎奖励和飞轮做旗舰——每一步的失败都预注册了它的可发表解释。**

---

## 7. Sources 与证据边界

- 两个父文档：[Agentic_world](<Agentic_world.md>)（GPT 版）、[Agentic_world_fable5](<Agentic_world_fable5.md>)（含全部消融数字出处与本地代码审计细节）
- **3DCodeBench 核实记录（2026-07-03）**：arXiv:2606.01057《3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code》（Gao et al.）+ github.com/gaoypeng/3dcodebench README。已核实：Infinigen/Indoors 蒸馏 → standalone Blender 5.0 脚本、212 类、单轮 / 多轮（T=3 traceback）/ coding-agent（Claude Code、Codex、Gemini CLI）、指标 executability/SigLIP-2/DINOv3/Chamfer/Uni3D/LLM-judge、3DCodeArena 人类偏好平台；摘要级发现：执行失败主因 API mismatch，跑通的渲染仍有断连/漂浮几何，test-time scaling（思考预算、多轮修正）整体有帮助。**未核实**：GPT 版"full coding-agent harness 提升执行率但形状质量不变好"的具体结论未在摘要与 README 中找到，采用前需读正文；库中无该论文精读，建议入库补一篇 DeepPaperNote。
- 精读笔记：[Code2Worlds](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>)、[Infinigen](<3d agent/Infinite Photorealistic Worlds using Procedural Generation/paper_DeepPaperNote.md>)、[Infinigen Indoors](<3d agent/Infinigen Indoors Photorealistic Indoor Scenes using Procedural Generation/paper_DeepPaperNote.md>)、[MeshCoder](<3d agent/MeshCoder LLM-Powered Structured Mesh Code Generation from Point Clouds/paper_DeepPaperNote.md>)、[Skill-3D](<3d agent/Skill-3D/paper_DeepPaperNote.md>)、[S-Agent](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>)、[SimWorld Studio](<3d agent/SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning/paper_DeepPaperNote.md>)、[P3D-Bench](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>)、[Think3D](<3d agent/Think3D/paper_DeepPaperNote.md>)
- 本地代码：`~/Downloads/reference_codes/{Code2Worlds, infinigen, MeshCoder}`
- **边界声明**：§4 各实验的"预期"是预注册假设不是结论；M1/M2/M3 的周数按单人 + 一台多卡机估计，未含引擎工程债的意外；工具序列熵、ETU-G、仪式化率三个指标是本路线自定义的，投稿前需在 related work 中对齐已有度量（ETU 出自 Skill-3D，其余两个是前作提出的新指标）。
