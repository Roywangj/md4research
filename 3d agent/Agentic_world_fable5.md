# Agentic World：以代码为中间介质的自主 4D 世界生成 agent（Fable 5 版）

> 写作时间：2026-07-03。主线材料：[Code2Worlds 精读](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>)、[Infinigen 精读](<3d agent/Infinite Photorealistic Worlds using Procedural Generation/paper_DeepPaperNote.md>)、[Infinigen Indoors 精读](<3d agent/Infinigen Indoors Photorealistic Indoor Scenes using Procedural Generation/paper_DeepPaperNote.md>)、[MeshCoder 精读](<3d agent/MeshCoder LLM-Powered Structured Mesh Code Generation from Point Clouds/paper_DeepPaperNote.md>)；范式参照：[Skill-3D 精读](<3d agent/Skill-3D/paper_DeepPaperNote.md>)、[S-Agent 精读](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>)；最近邻对照：[SimWorld Studio 精读](<3d agent/SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning/paper_DeepPaperNote.md>)、[P3D-Bench 精读](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>)。另做了本地代码审计：`~/Downloads/reference_codes/{Code2Worlds, infinigen, MeshCoder}`。
>
> **与前作的关系**：[3d_insight_with_reasoning_all](<3d_insight_with_reasoning_all.md>) 及之前各版讨论的是**理解端** agent（看世界、答问题）；本篇讨论**生成端** agent（写代码、造世界）。两者共享同一套判决方法论（机制-脚手架、可验证奖励、反事实审计），第 7 节会说明它们如何闭合成一个飞轮。本篇不重复前作内容。
>
> **命名勘误（2026-07-03 更正）**：初版误判 "3DCodeBench" 不存在。后经联网核实它真实存在：arXiv:2606.01057《3DCodeBench: Benchmarking Agentic Procedural 3D Modeling Via Code》，基于 Infinigen/Indoors 蒸馏成 standalone Blender 5.0 脚本、212 类，库中暂无精读。核实细节与它对本方案的影响见 [Agentic_world_all](<Agentic_world_all.md>) §0.2/§7。本篇正文写作时以 P3D-Bench 代位，评测语法相关结论仍成立。

---

## 0. TL;DR：五个判断

1. **你的方案方向与证据一致，但证据指出的第一瓶颈不是 planner，而是库**。Code2Worlds 消融（Table 3）：去掉代码检索 SGS 从 61.4 崩到 23.5，去掉 VLM 反思只降到 58.6。当前系统的"智能"主要存在检索库里而非模型里——所以"把库升级成正式的工具层、把 pipeline 升级成规划空间"是对的，但工具层的质量决定上限，planner 只决定利用率。
2. **解耦不是工程洁癖，是轨迹收集的前置条件**。代码审计发现：发布版 Code2Worlds 的"场景代码"实为注入 infinigen 目录的 gin 配置；动力学脚本被系统提示**强制要求**留 `USER_FILL` 占位符（人工开 Blender 查物体名）且禁止自动烘焙。也就是说当前 pipeline 根本跑不出无人值守的完整轨迹——不解耦，你的"搜集轨迹训 agent"计划在第一步就会卡死（详见 §2.3）。
3. **"是否归纳成更结构化的物体代码"——答案是肯定的，且有自动化路径**。MeshCoder 证明部件化程序表示可以由 1B 模型学会（CD 0.063×10⁻² vs PLAD 1.87×10⁻²，Table 1），P3D-Bench 证明装配级/部件级恰是通用大模型最弱的地方（三大发现之二、三）。更重要的是 MeshCoder 给了一条"把 infinigen 从运行时依赖变成数据来源"的反蒸馏路线（§3.3）。
4. **"planner 比预定义 pipeline 更智能"不是免费成立的，需要判决实验**。这正是前作"机制还是脚手架"问题在生成端的镜像。支持你的证据：Think3D 裸工具只 +0.80、RL 后 +12.05，策略对照 Random 36.68 / Heuristic 38.69 / RL 47.11（训练 planner 确实比 prompt 强）。反对的警告：S-Agent 弱 planner 直接套框架反而降分（MMSI 30.7 < 基座 31.1）；且生成任务的工具序列熵可能很低——大多数提示走同一条链，此时 planner 是脚手架，智能应投在参数与修补上（§6 给出判决设计）。
5. **人类反馈应该放在校准位，不要放在主奖励位**。生成端相对理解端有一个结构性红利：**引擎即 oracle**。可执行世界自带免费可验证信号（执行成功、碰撞穿透、约束满足率），其中 Infinigen Indoors 的约束 DSL 是现成的、被严重低估的 **reward 语言**（§5.2）。人只看少量最终结果做偏好校准——Indoors 自己的教训是代理分数会与视觉质量错位（去掉离散移动评分反升 86.20>80.84 但视觉更差），所以纯自动奖励必须定期用人类偏好重锚。

---

## 1. 证据地图：每篇论文提供拼图的哪一块

| 论文                                                                                                                                                  | 提供什么                                                      | 关键数字                                                                  | 缺什么（对你的方案而言）                                    |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------- |
| [Infinigen](<3d agent/Infinite Photorealistic Worlds using Procedural Generation/paper_DeepPaperNote.md>)                                                    | 资产程序底座：182 个生成器、1070 个可解释自由度、50 个材质生成器，全程序化、带真值           | 成本硬数字：3.5 h/立体对、约 24 GB 内存、场景均值 1600 万面                               | 一次性执行的整体 pipeline，没有增量/局部再生成接口                  |
| [Infinigen Indoors](<3d agent/Infinigen Indoors Photorealistic Indoor Scenes using Procedural Generation/paper_DeepPaperNote.md>)                            | 声明式约束 DSL + 求解器：约束计算图（示例 1058 节点、11 硬 + 25 软）、每房间约 15 行约束 | 求解 2280.68 s vs 未优化 6308.92 s；UE 60 FPS / Isaac 50 FPS 导出链            | 约束由人写；没人把它当 reward 用（这是机会，§5.2）                 |
| [MeshCoder](<3d agent/MeshCoder LLM-Powered Structured Mesh Code Generation from Point Clouds/paper_DeepPaperNote.md>)                                       | 逆向通道（世界→代码）：点云→部件化 Blender 脚本；千万级部件对自动造监督                 | 部件操作 IoU：基本体 94.81 / 布尔 96.13 / 阵列 78.90（Table 4）；36% 对象因部件失败被筛除      | 单向单次映射，无执行反馈闭环；合成域内测试                           |
| [Code2Worlds](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>)                                                  | 正向通道（语言→代码→4D）：双流 + 库检索 + 双 critic 闭环                     | 检索消融 SGS 61.4→23.5；运动 critic 消融失败率 10%→60%（Table 3/4）；Code4D 仅 10 条提示 | 强耦合 infinigen、人在环节点、无训练（纯 prompt 编排）            |
| [P3D-Bench](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>)                            | 评测语法：可执行性/几何/拓扑/部件四桶分离；装配任务阶梯                             | 三发现：装配最难；整体形状易、精确参数化几何难；部件级最弱                                         | 偏机械 CAD 域（支撑安装件占 67.2%），无动态维度                   |
| [Skill-3D](<3d agent/Skill-3D/paper_DeepPaperNote.md>)                                                                                                       | 范式 A：轨迹→技能库演化 + 工具效率奖励                                    | ETU 39.2%→78.7%；R_tool = R_exec − \|A\|/B，冻结解析器防刷分；Fig 5：RL 期间冻结技能库   | 面向问答不面向生成（需移植，§4.1）                             |
| [S-Agent](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>)                                             | 范式 B：教师轨迹合成→过滤→三粒度分解→SFT                                  | S-300K：51,596 条合格轨迹拆成 292,391 样本；弱 planner 反向（30.7<31.1）；SFT 后 +10.5  | 同上；且无时延报告                                       |
| [SimWorld Studio](<3d agent/SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning/paper_DeepPaperNote.md>) | **你的方案的最近邻**：UE5 编码 agent + 验证器 + 技能沉淀 + 共同演化             | 组件阶梯 0.16→0.45(工具)→0.55(验证)→0.76(自演化)；共同演化 90% vs 固定环境 72%            | 资产靠库检索非程序生成；无 4D 物理；演化留在上下文里，不训练模型（差异化定位见 §4.3） |

**一句话综合**：正向通道（Code2Worlds）、逆向通道（MeshCoder）、资产底座（Infinigen×2）、评测语法（P3D-Bench）、训练范式（Skill-3D/S-Agent）、系统参照（SimWorld Studio）都已存在——**还没人把"生成 4D 世界"本身当成一个可训练的工具调用策略问题**。这就是你的位置。

---

## 2. 主线批判：Code2Worlds 到底证明了什么、卡在哪

### 2.1 它证明的：库先验 ≫ 反思闭环

消融的量级排序非常清楚（Table 3/4/5）：代码检索（SGS −37.9）＞ 场景流整体（Richness −35.9）＞ 运动 critic（失败率 +50 个百分点）＞ 参数库（SGS −12.6）＞ 静态 critic（SGS −2.8）。**大模型在验证过的模板和显式参数空间里做组合，而不是从零写领域代码**——这是全文最硬的机制结论，也直接支持你"把每个步骤当工具"的改法：这些"工具"事实上已经存在（模板+参数 schema），缺的只是把它们从 prompt 附件升格为带类型契约的接口。

### 2.2 它没证明的：双流分解本身的贡献

对象流/场景流的消融只能证明"组件合起来有效"，没有同预算单流对照（精读笔记已指出）。【推断】对你的方案这意味着：不要继承"双流"这个架构决定，把它降级为 planner 的两条可选子链——如果判决实验（§6）发现工具序列熵低，双流可以合并。

### 2.3 代码审计：论文没写的三层耦合 + 一个致命事实

本地仓库(`reference_codes/Code2Worlds`)的量化画像：agent 层 11 个文件约 2,400 行（每个 100–440 行的薄 LLM 封装），library 层 5 个文件 5,285 行 + 一个 1,128 行的 `nature_example.py`。三层耦合从松到紧：

- **L1（对象）**：生成的对象代码 = 向 infinigen Factory 注入参数。模板硬编码 `sys.path.append(r"D:\infinigen")`、`from infinigen.assets.objects.leaves.leaf_v2 import LeafFactoryV2`，甚至用 monkey-patch `np.random.binomial` 来锁定病斑随机性。耦合点：Factory 类签名 + genome dict 键名。
- **L2（场景）**：`scene_stream/realizer.py` 的输出目标是 `./infinigen/infinigen_examples/configs_nature/scene_types/generated_scene.gin`——所谓"场景代码"其实是**写进 infinigen 配置目录的 gin 覆盖**，真正执行的是那个 1,128 行的 fork 主脚本（20+ 个 `infinigen.core/assets/terrain` 深层 import）。场景生成是"整锅一次执行"，没有逐部分生成可言。
- **L3（动态）**：`postprocess_agent.py` 的系统提示**明文要求**生成 `USER_FILL` 占位（"打开 blend 文件在 outliner 里找物体名"）并禁止 auto-bake（"打印手动烘焙说明"）。**发布版的 4D 环节设计上就是人在环的**。

这最后一点是本篇最重要的代码级发现：**你要收集"planner 调工具→出结果→人打分"的完整轨迹，前提是轨迹能无人值守跑通**；而当前系统在 4D 这一步结构性地断开。所以解耦的第一优先级不是"摆脱 infinigen"这个笼统目标，而是三件具体的事：①对象命名与场景状态必须程序可查（一个 scene graph JSON，物体 ID 稳定），②物理烘焙必须可编程触发，③各步骤之间用文件/JSON 传状态改为用显式类型化的中间表示传状态。

---

## 3. 解耦方案：三档递进，代码作中间介质的正确形态

### 3.1 L0（一周量级）：把 infinigen 封成黑盒工具

不改 infinigen，只写包装层：每个 `infinigen/assets/objects/` 下的 Factory 目录（本地仓库有约 30 类：trees、leaves、creatures、seating、tables、appliances……）包一个 `make_asset(category, params) -> asset_handle`；地形/天气/光照包成 `make_terrain/set_weather/set_lighting`；`nature_example.py` 拆成 stage 函数（它内部本来就是 `RandomStageExecutor` 逐 stage 跑的，拆分有自然缝）。**产出：工具池 v0，够收集第一批轨迹。**

### 3.2 L1（一两个月）：引擎无关的场景 IR

定义类型化场景程序作为所有工具的输入输出：

```
World := { assets: [AssetSpec],      # 类别+参数+位姿，MeshCoder 式部件语法
           layout: [Constraint],     # Indoors 约束 DSL 子集
           env: EnvParams,           # 地形/天气/光照字典（即 Code2Worlds 的 D）
           dynamics: [Event],        # (对象ID, 物理类型, 参数, 时间区间)
           camera: CameraSpec }
```

工具变成 IR 上的变换（生成、修改、校验、执行），bpy/infinigen 降级为 IR 的**一个后端**。这不是空想：Code2Worlds 已经有三个隐式 IR（对象 schema、环境 manifest+参数字典、物理参数），只是它们以 prompt 文本和散落 JSON 的形态存在；Indoors 的导出链（UE 60 FPS / Isaac 50 FPS）证明"同一世界、多个后端"工程上通。【推断】IR 的最大红利在训练端：轨迹里的每个动作变成"对 IR 的一次类型化编辑"，可以做静态校验（不执行就能拒掉一批坏动作）、可以 diff（负轨迹自动构造）、可以局部重放（反事实审计便宜）。

### 3.3 L2（研究项目）：反蒸馏——把 infinigen 从运行时依赖变成数据来源

MeshCoder 的配方反过来用：它用 Infinigen Indoors 资产当**监督源**训练"点云→干净部件程序"（千万部件对、只留全部件 CD<5×10⁻³ 的对象）。同样地，可以让 infinigen Factory 批量出资产 + 参数真值，蒸馏出一个**不依赖 infinigen 的参数化对象程序库**（纯 bpy 原语或 MeshCoder 的几何 API）。此后 infinigen 版本升级、Windows 路径、gin 语法全部与你无关。风险同 MeshCoder 的教训：36% 筛除率意味着教师表达不了的长尾会系统性缺席——所以 L2 是二期，L0/L1 先行。

### 3.4 回答你的开放问题：要不要"归纳整理成更结构化的场景物体代码"

**要，且这是决定天花板的选择。** 三条证据链：①P3D-Bench 三发现——通用大模型能恢复"整体像"，恢复不了"精确参数化几何"和"部件结构"，说明自由代码生成在结构维度不可靠，结构必须由表示承担；②MeshCoder Table 4——结构化操作的可学性有梯度（基本体 94.81 > 布尔 96.13 > 桥接 89.16 > 扫掠 83.45 > 阵列 78.90），即结构化语言的每个原语都可以被单独度量与课程化；③Code2Worlds 自己的检索消融（61.4→23.5）——离开结构化先验，性能不是降一点而是崩。【推断】正确粒度是**部件级参数化函数**（MeshCoder 语法）+ **对象级 Factory**（infinigen 语法）双层，场景层则用约束而非坐标（Indoors 语法）——三种"结构化"各管一层，不要试图用一种语法通吃。

---

## 4. 工具化与范式移植

### 4.1 工具清单与可选性

把 Code2Worlds pipeline + Infinigen 组件拆成工具池（v0 约 14 个）：

| # | 工具 | 来源 | 必要性 |
|---|---|---|---|
| t1 | 提示解析/动态目标选择 | Code2Worlds ObjSelect | 常驻（它已内含分支：纯全局变化跳过对象流——你的"步骤非强制"思想在原系统里已有雏形） |
| t2 | 对象 schema 检索 | 参数库 L_param | 视提示 |
| t3 | 对象参数生成 | ObjParam | 视提示 |
| t4 | 对象代码生成+执行 | ObjGenerate + bpy | 视提示 |
| t5 | 静态渲染检查 | VLM-Critic | 可选（廉价档先用规则检查） |
| t6 | 环境 manifest 规划 | Planner | 视提示 |
| t7 | 参数解析（含耦合/互斥） | Resolver | 视提示 |
| t8 | 场景实现 | Realizer→后端 | 有环境时必须 |
| t9 | 布局约束求解 | **Indoors solver** | 室内/多对象时 |
| t10 | 对象-环境融合 | PostProcess 前半 | 视提示 |
| t11 | 物理参数推断 + 动力学脚本 | PostProcess 后半 | 4D 时必须 |
| t12 | 仿真执行+烘焙（须先解耦 L3） | bpy | 4D 时必须 |
| t13 | 运动检查 | VLM-Motion Critic | 4D 时强烈建议（消融：去掉后失败率 10%→60%） |
| t14 | 导出（UE/Isaac/视频） | Indoors 导出链 | 按下游 |

### 4.2 Skill-3D 范式 → 生成端

- **ETU 的生成端版本（ETU-G）**：一次工具调用"有效"，当且仅当其输出出现在最终 IR 里且扰动它会改变最终世界。这直接沿用了前作 all 版 §8.1 的反事实门控思想，而且生成端更便宜——扰动后重执行、diff 两个 IR，全程序可测，不需要 GPT 裁判。
- **奖励移植**：`R = R_ans + R_fmt + (R_exec − |A|/B)` 整体照搬，其中防刷分的关键细节必须保留——Skill-3D 用**冻结的场景任务解析器**决定"该拿到哪些证据"，生成端对应"冻结的提示解析器决定该产出哪些 IR 字段"（要求风效果的提示必须有 dynamics 事件，纯光照提示不得有对象流调用）。
- **技能库演化**：成功轨迹蒸馏为"触发条件+工具顺序+参数要点+失败教训"，失败轨迹挂教训。**但 Fig 5 的教训要记住：RL 期间冻结技能库**，在线更新会带来非平稳（策略和检索对象同时漂移）。SimWorld Studio 用同样机制（重复修复→沉淀为命名工具/Markdown 技能）拿到了 0.55→0.76 的最大单项增益，两个独立系统在这一点上收敛，可信度高。

### 4.3 S-Agent 范式 → 轨迹合成；以及与 SimWorld Studio 的差异化

**轨迹合成配方直接照搬 S-300K**：强教师（闭源模型做 planner）跑工具池 → 结果过滤（生成端用引擎检查代替 MRA≥0.6）→ **三粒度分解**（整轨迹 / 回合级 / 单工具级——一条轨迹放大成约 5.7 倍监督样本，51,596→292,391 的杠杆）→ SFT 小模型。两个警告：①S-Agent 的过滤合格率不高（800K 源数据最终 51.6K 条轨迹），生成端每条轨迹还要执行渲染，预算要按合格率 <20% 规划；②**不要在 SFT 之前发布 planner 版产品**——弱 planner 套 agent 框架反而降分（30.7<31.1），这对"先拿 prompt 版给人看效果"的路线是明确警告。

**与 SimWorld Studio 的差异化**（这是写论文时必须回答的"最近邻问题"）：

| 维度 | SimWorld Studio | 你的方案 |
|---|---|---|
| 资产 | UE5 资产库检索摆放 | **参数化程序生成**（infinigen/MeshCoder 语法，资产本身可控可编辑） |
| 动态 | 静态环境+导航任务 | **4D 物理动态是一等公民**（刚体/流体/粒子/大气） |
| 学习 | 演化留在上下文（技能=Markdown，LLM 权重不动） | **轨迹训练进参数**（SFT+RL），小模型可部署 |
| 反馈 | 规则+VLM 验证器 | 规则+VLM+**约束 DSL 满足率**+人类偏好校准 |

【推断】SimWorld 的共同演化结果（90% vs 72% vs 50%）反而是你方案的助攻证据：环境生成 agent 的价值最终由"下游学习者是否变强"度量——这正好接到 §7 的飞轮。

---

## 5. 反馈与奖励：引擎即 oracle，人类只做校准

### 5.1 为什么"人观察结果打分"不能当主奖励

Code2Worlds 的评测配置就是反面教材：SGS/HRS/Richness 靠 GPT-4o 评分、物理失败率靠人工检查，而系统本身由 Gemini 3 驱动——模型偏好互相污染，且 Code4D 只有 10 条提示。人工逐轨迹打分贵、慢、噪声大，撑不起 RL 需要的密度。

### 5.2 被低估的资产：Indoors 约束 DSL 是现成的 reward 语言

Infinigen Indoors 的约束计算图（语义筛选→几何算子→硬约束/软评分，示例 1058 节点）本来是布局求解器的目标函数。换个用法：**让它给任意生成的场景打分**——约束满足率是稠密、可微调粒度、完全可验证的奖励，覆盖"通道不堵、器具前留操作空间、对称、可达"这类人类难以逐条口头反馈的规范。加上引擎免费信号（执行成功率、碰撞/穿透检测、导航网格连通性——SimWorld 的规则验证器清单可直接抄），生成端的可验证奖励密度远高于理解端。这是本篇相对前作最大的新增红利：前作要为 QA agent **建**一个 Oracle3D-Gym，生成 agent 的 oracle **就是它的执行引擎本身**。

### 5.3 人类反馈的正确位置 + 错位教训

人只做两件事：①稀疏的成对偏好（校准 VLM-critic 和软约束权重），②验收判例（新技能入库前的抽检）。必须定期重锚的理由是 Indoors 的实测错位：去掉离散移动后代理评分更高（86.20>80.84）但视觉质量更差——**任何代理奖励跑久了都会被策略钻空子**，这在 RL 语境下只会更严重。【推断】操作化：每 N 轮 RL 抽一批高奖励轨迹给人做盲评，奖励-偏好相关性下降即触发奖励模型重校准。

---

## 6. 判决实验：不要假设 planner 赢，去测量

你的假设"LLM planner 选工具 + 训练 > 写死 pipeline + prompt"由两个可分离的命题组成，分开判决：

- **H1（训练有益）**：同一工具池上，训练过的 planner > prompt 的 planner。先验概率高——Think3D 的策略对照（Random 36.68 / Heuristic 38.69 / RL 47.11）和 Skill-3D 后训练（Qwen3-VL-8B VSI 相对 +60.3%）都支持。预注册指标：Code4D 式提示集上的约束满足率 + 物理失败率 + ETU-G。
- **H2（规划有益）**：训练过的自由 planner > 训练过的固定 pipeline（同预算）。**这条不保证成立**。生成任务可能是低熵的：大多数提示都走 t1→t2..t5→t6..t8→t11..t13。判决方法：先跑教师轨迹审计，测**工具序列熵**——若 90% 轨迹共享同一骨架，则 planner 的真实价值只在跳步（省成本）和修补循环（提质量）两处，架构上应改成"固定骨架 + 学习的跳步门控 + 学习的修补策略"，而不是全自由规划。这比全自由规划省一个数量级的探索预算。【推断】我预期结果介于两者之间：静态部分低熵、动态部分（物理类型×参数×修补）高熵——即"4D 才需要 agent，3D 只需要 pipeline"。若证实，这本身就是一个可发表的结论。
- **H3（结构化库有益）**：L1 IR 工具池 > L0 黑盒包装（同 planner）。度量：轨迹合格率、静态校验拦截率、每合格轨迹的执行成本。

**最小验证路径**（Phase 0，2–3 周，零训练）：L0 包装 → 强教师跑 50–100 条提示（扩充 Code4D 的 10 条）→ 全程无人值守率、工具序列熵、引擎奖励与 VLM 评分的相关性。这一步同时产出：第一批 SFT 种子轨迹、H2 的判决数据、解耦清单的验收。

---

## 7. 成本、风险与飞轮

**成本现实**：Infinigen 单场景 3.5 h/立体对、24 GB 内存、1600 万面、10000 spp——全保真 RL rollout 完全不可行。对策是**保真度阶梯**：IR 静态校验（免费）→ Eevee 低采样代理渲染（秒级）→ 低 substep 物理预览 → 完整 Cycles 只留给最终交付和人类评审。你"粗糙动态世界"的定位在这里从妥协变成优势：目标本来就不是照片级，低保真档就是产品档，训练信号密度反而更高。

**主要风险**：①工具本身的质量上限（Skill-3D 教训：调度改善不了坏证据；infinigen 覆盖不了的资产类别，planner 再聪明也生成不出）；②技能库/奖励被 VLM 审美俘获（SimWorld 精读笔记明确警告验证器会塑造生成分布）；③长尾筛除偏差沿轨迹过滤复制进 agent（MeshCoder 的 36% 教训——建议保留一部分"失败但可修复"轨迹做修补训练，而不是只学成功路径）。

**飞轮（公司主线叙事）**：生成 agent 造出的每个世界自带完整几何/物理真值 → 它就是前作呼吁的 Oracle3D-Gym 的**供给侧**：可以按需出可验证空间 QA、导航、操作任务 → 理解端 agent（Skill-3D/Think3D/S-Agent 线）在其中训练与评测 → 理解端的失败分布反过来指定下一批该生成什么世界（SimWorld 的共同演化，+18 个百分点的先例）。两条线在数据接口上闭合：**理解端消费世界，生成端消费失败**。MeshCoder 的逆向通道再把真实扫描拉进来（真实世界→代码→可编辑仿真），三个方向共用同一个场景 IR。这是"以代码为中间介质"最强的版本：代码不只是生成格式，是理解、生成、评测三方共享的世界表示。

**候选论文形态**【推断】：《From Pipeline to Policy: Learning Tool-Use Trajectories for Autonomous 4D World Generation》——贡献点：场景 IR + 工具化解耦（H3）、引擎奖励 + 约束 DSL 奖励语言（§5.2）、planner 判决(H2 的熵审计本身就是分析章节)、S-300K 式轨迹蒸馏出的可部署小模型。每一块都有明确的最近邻可引可比（Code2Worlds、SimWorld Studio、Skill-3D、S-Agent）。

---

## 8. 来源

- Code2Worlds (arXiv:2602.11757, ICML 2026) — [精读](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>) ｜ 代码已开源：github.com/AIGeeksGroup/Code2Worlds（本地：`reference_codes/Code2Worlds`）
- Infinigen (CVPR 2023, arXiv:2306.09310) — [精读](<3d agent/Infinite Photorealistic Worlds using Procedural Generation/paper_DeepPaperNote.md>) ｜ 本地：`reference_codes/infinigen`
- Infinigen Indoors (CVPR 2024, arXiv:2406.11824) — [精读](<3d agent/Infinigen Indoors Photorealistic Indoor Scenes using Procedural Generation/paper_DeepPaperNote.md>)
- MeshCoder (arXiv:2508.14879) — [精读](<3d agent/MeshCoder LLM-Powered Structured Mesh Code Generation from Point Clouds/paper_DeepPaperNote.md>) ｜ 本地：`reference_codes/MeshCoder`（llama_recipes 训练栈 + blender_scripts API）
- Skill-3D (arXiv:2606.07436) — [精读](<3d agent/Skill-3D/paper_DeepPaperNote.md>)；S-Agent (arXiv:2606.20515) — [精读](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>)
- SimWorld Studio (arXiv:2605.09423) — [精读](<3d agent/SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning/paper_DeepPaperNote.md>)；P3D-Bench (arXiv:2606.11152) — [精读](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>)
- Think3D 数字引自 [精读](<3d agent/Think3D/paper_DeepPaperNote.md>)（Table 6 策略对照）；理解端方法论引自 [3d_insight_with_reasoning_all](<3d_insight_with_reasoning_all.md>)
- **证据边界声明**：§2.3 的三层耦合与 USER_FILL 事实来自本地代码审计（realizer.py / postprocess_agent.py / obj_nature_generate.txt 逐行核对），非论文声明；§6 的 H1–H3 是预注册假设不是结论；所有标注【推断】处为我的判断，未经实验验证；"3DCodeBench" 未能定位到确切论文，本篇以 P3D-Bench 代位。
