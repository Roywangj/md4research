---
tags:
  - papers/3d-spatial-reasoning
  - papers/agentic-tool-use
  - comparisons
aliases:
  - World2Mind vs Skill-3D
---

# World2Mind vs Skill-3D：世界状态编译器与技能演化代理的证据化比较

> [!info] 证据约定
> - **[论文证据]**：来自两篇论文正文、表格或论文制品。
> - **[代码证据]**：来自本地 `/Users/roywangj/Desktop/Skill-3D`；引用格式为绝对路径与行号。
> - **[本地复现实验]**：来自该仓库已保存的复现日志与结果汇总，不等同于论文官方结果。
> - **[推断]**：由上述证据推出、尚需实验验证。
>
> 主要本地入口：[World2Mind 论文原文](paper_full_text.md) · [World2Mind 精读](3d%20agent/World2Mind%20Cognition%20Toolkit%20for%20Allocentric%20Spatial%20Reasoning%20in%20Foundation%20Models/paper_DeepPaperNote.md) · [Skill-3D 论文阅读稿](3d%20agent/Skill-3D/paper.md) · [Skill-3D 精读](3d%20agent/Skill-3D/paper_DeepPaperNote.md) · [Skill-3D 原始 PDF](file:///Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/IJEAHRZU/Li%20等%20-%202026%20-%20Skill-3D%20Evolving%20Scene-Aware%20Skills%20for%20Agentic%203D%20Spatial%20Reasoning.pdf)

## 1 分钟结论

1. **二者解决的不是同一层问题。** **[论文证据]** World2Mind 是一个**无需更新基础模型参数的外部空间状态编译器**：用 Depth Anything V3、SAM3、点云过滤、实例聚类，把自我中心视频/多视图编译成 Allocentric-Spatial Tree（AST）、landmark map 与 route map，再交给基础模型推理。Skill-3D 是一个**可训练的工具编排代理**：从轨迹构建 Scene Memory，抽取/检索场景感知技能，调用六类工具，并以 agentic SFT + GRPO 把行为迁移进 Qwen3-VL-4B/8B。
2. **它们互补而非替代。** **[推断]** World2Mind 最自然的落点不是替换 Skill-3D，而是成为其中一个高层工具/技能：当问题需要全局对象拓扑、度量关系或可通行路线时一次性生成任务相关世界状态；Skill-3D 决定是否调用、查询哪些对象/地图、何时回退到 DA3、Pi3、检测或分割。
3. **World2Mind 的优势是表示，短板是证据与复现。** **[论文证据]** 它在 VSI-Bench-Tiny 上使 GPT-5.2 `46.7→54.0`、Claude-4.6-Opus `38.4→56.0`、Gemini-3-Pro `55.2→61.0`；MindCube-Tiny 分别 `49.9→54.6`、`48.5→62.9`、`75.1→81.6`。但存在明确负结果：GPT 的对象计数 `52.5→47.4`、绝对距离 `34.9→33.4`、对象尺寸 `67.5→63.3`，Gemini 房间尺寸 `71.3→57.7`，GPT MindCube Around `62.4→60.4`。仅评 Tiny 子集，未给代码、完整提示、关键阈值、token/延迟/显存/API 成本或同预算工具基线。
4. **Skill-3D 的优势是工具路由与程序性记忆，短板是发布物不闭环。** **[论文证据]** Qwen3-VL-4B 的 VSI 平均分 `30.4→49.1`，8B `36.7→58.8`；ETU 在 VSI `39.2%→78.7%`、BLINK `36.4%→79.2%`、CV-3D `31.8%→87.5%`、MMSI `30.5%→80.3%`。**[代码证据]** 本地仓库有实质性的 agent、分层 memory、skill retrieval、tool wrapper 与评测代码，但 GRPO 脚本引用缺失的 `plugin/plugin_all_angles.py`（`/Users/roywangj/Desktop/Skill-3D/train/train_grpo.sh:141-148`），README 自己也把 generated Scene Memory/Skill Library 与 optional plugins 列为本地必需制品（`/Users/roywangj/Desktop/Skill-3D/README.md:256-266`）；当前本地未发现生成的 memory/`learned_skills.json`，也未发现论文 ETU 的可执行实现。
5. **本地分数不能当作功能工具复现。** **[本地复现实验]** 已保存运行明确是 released GRPO-4B 的“无功能工具”诊断：BLINK `47.31% (44/93)`、MMSI-PR 修正 scorer 后 `31.78% (116/365)`、CV-3D Depth-Order `88.1%`、Rel-Distance `75.5%`、VSI `30.8%`。VSI 与论文 base w/o Tools `30.4` 几乎相同，距 full Skill-3D-4B `49.1` 仍差 `18.3` 点；因此它诊断 checkpoint 的无工具行为，不能验证论文工具链、记忆演化或 ETU。

## 总览比较表

| 维度 | World2Mind | Skill-3D | 判断 |
|---|---|---|---|
| 核心层级 | **[论文证据]** 感知结果 → 分配中心世界状态的外部编译器 | **[论文证据]** 场景/任务 → 技能检索 → 工具工作流的代理策略 | 表示层 vs 控制层 |
| 输入 | 视频/多视图、问题、兴趣类别、map type、可选 visualization | 图像/7 帧视频、问题、候选技能、工具结果与历史轨迹 | Skill-3D 上下文更长、更迭代 |
| 输出 | AST YAML、landmark/route map、可视化与最终答案 | 技能选择、若干 tool calls、中间证据、最终答案；训练时还产出轨迹/记忆 | World2Mind 输出“状态”，Skill-3D 输出“行动链” |
| 世界表示 | 绝对坐标、实例层次、椭圆 footprint、高度范围、可通行栅格、相机轨迹 | Scene Memory/Skill Library 主要保存问题模式、工具序列、成功率、失败 lessons；工具的 3D 输出作为临时证据 | World2Mind 更“world-centric”；Skill-3D 更“procedure-centric” |
| 工具粒度 | 对基础模型暴露一个高层 `world2mind` 接口；内部是 DA3+SAM3+点云/AST/route pipeline | 六类论文工具：DA3、SAM3、GroundingDINO、Pi3、SwinIR、Orient Anything v2 | 高层复合工具 vs 原子/中粒度专家工具 |
| 控制流 | 三阶段：是否调用 → 模态解耦取证 → 几何—语义交织/冲突消解 | 多轮：场景任务解析 → 检索/选择 skill → 调工具 → 证据整合/回退 → 记忆更新 | 前者重证据融合，后者重策略选择 |
| 记忆/演化 | **[论文证据]** 静态场景聚合；没有跨任务长期记忆或技能演化 | **[论文证据]** 成功轨迹蒸馏 skill，失败轨迹挂 lesson；阶段式共演化 | Skill-3D 独有，但在线演化不稳定 |
| 训练 | training-free（仅指不训练基础模型；依赖预训练视觉工具） | 500 SFT + 1k GRPO 样本；4×RTX PRO 6000 Blackwell；约 3h + 28h | 前者免后训练，后者把策略内化 |
| 论文评测 | VSI-Tiny、MindCube-Tiny；三种 frontier model | VSI、BLINK、CV-3D、MMSI；闭源与 Qwen 4B/8B | Skill-3D 范围更大；协议仍是作者自建 30/70 split |
| 代码可得性 | **[代码证据]** 本地只见论文 artifacts，未见 World2Mind 实现 | **[代码证据]** 大量 inference/memory/retrieval/tool/evaluation 代码 | Skill-3D 可审计性明显更好，但关键产物缺失 |
| 已知失败 | 计数/尺度等子项可负增益；重建误差被结构化后可能放大 | 无工具时 VSI 不内化；memory、plugin、ETU 缺口阻断忠实复现 | 两者失败面不同 |
| 最合理组合 | 作为按需的 high-level allocentric state tool | 负责路由、预算、回退、技能积累 | 组合优先于二选一 |

## 1. 任务、输入与输出

### World2Mind

**[论文证据]** 目标是把视频/多视图中的自我中心观察转换为可计算的分配中心知识，覆盖计数、绝对/相对距离、对象/房间尺寸、相对方向、路线规划、接近顺序以及 MindCube 的 Around/Among/Rotation。输入为图像序列与问题；模型还需给工具提供兴趣实例、`landmark`/`route` map 类型和可选 visualization。输出不是另一个视觉 embedding，而是 AST 结构化文本、俯视地图/投影，以及由基础模型交叉验证后的答案。

**[推断]** 其接口更像 query-conditioned compiler：只为问题相关类别建图，可减少全场景语义点云进入上下文的成本，但也可能因类别漏指定而永久漏掉关键对象。

### Skill-3D

**[论文证据]** 目标不是发明新的几何 estimator，而是解决“不同问题却走同一工具路线”的错配。输入除图像/视频与问题外，还包括 Scene Memory 检索出的 skill cards、工具输出和中间交互；输出是结构化 `<skill_choice>`、`<tool_call>`、证据推理和答案。

**[代码证据]** 本地 agent 允许配置 symbolic/hybrid memory、retrieval top-k、自动/模型技能选择与强制工具约束（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/agent.py:49-107`），并把检索候选、最终排序、skill choice、tool chain 与正确性写入 trace（同文件 `137-166`）。这不是空 README：控制状态真实存在于实现中。

## 2. Allocentric / world representation

### World2Mind：显式、对象级、绝对坐标

**[论文证据]** DA3 预测深度、相机位姿和置信度，SAM3 提供开放词汇 mask；有效像素反投影到统一世界坐标，经 KNN 密度滤除边界尾点，再按语义类别用 adaptive DBSCAN 分实例。Landmark AST 在俯视 X–Z 平面用中心 `(xc, zc)`、长短轴 `a,b`、旋转角 `θ`、高度范围及包含关系压缩实例；route map 则将可通行区域体素化为 `N×N` 网格并叠加相机轨迹。

它真正有价值的是把三层隐变量显式化：跨帧坐标对齐、实例对应、对象级几何。纯文本 blind 结果（GPT 平均约 `6.0→18.2`，Claude `23.1→52.2`）只证明“视觉工具预计算出的结构化几何文本可被文本模型消费”，不证明文本模型无感知地产生了 3D 世界模型。

### Skill-3D：程序性记忆，不是统一世界模型

**[代码证据]** `SkillMemoryUnit` 保存 task pattern、trigger、strategy、tool candidates、fallbacks、failure memory、view policy、success/correct/reward 与 maturity，而不是稳定的全局对象坐标图（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/skill_retrieval.py:89-109`）。动态 skill 从 memory 的 tool sequence、failure memory 和统计量构造（同文件 `204-245`）。

**[代码证据]** 本地 `AdaptiveSkillManager` 虽然扩展出 working/episode/evidence/rule 等层，并在 episode 中保存 scene signature、有效工具序列、对象、关系与 provenance（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/skill_learning.py:221-247,286-347`），但它仍以“检索与复用过程”为核心，不等于维护一个跨时间一致、可查询的 metric world state。

**[推断]** 因而 World2Mind 可以补上 Skill-3D 最缺的中间层：不是再给它一张 Pi3 render，而是给一个对象级、带坐标/不确定性的 world-state artifact。

## 3. 工具粒度

### World2Mind：一个高层复合工具

**[论文证据]** 对 LLM 而言主要调用 `world2mind(categories, knowledge_type, visualization_type)`；DA3、SAM3、点云映射、过滤、聚类、椭圆拟合与栅格生成都封装在内部。优点是减少 LLM 在低层工具间传参和拼接几何的负担；缺点是内部任一环节错误可能以“精确 YAML”外观传播，且无法从论文单独定位误差来源。

### Skill-3D：六类可编排专家工具

**[论文证据]** 论文工具池为：Depth Anything 3（度量深度）、SAM3（分割）、GroundingDINO（开放词汇检测）、Pi3（多视图 3D 重建）、SwinIR（超分/恢复）、Orient Anything v2（朝向）。论文的关键主张不是“六个工具更强”，而是按证据需求选择它们。

**[代码证据]** README 为六项服务规定端口和启动接口（`/Users/roywangj/Desktop/Skill-3D/README.md:116-166`）；agent 对 seed skill 绑定 detection/depth/Pi3/segmentation 等 required tools（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/agent.py:318-364`）。

**[推断]** 组合时不要把 World2Mind 再拆成十几个 LLM-visible 微工具；应暴露一个高层工具，并保留 DA3/Pi3 等廉价或直接基线。否则 Skill-3D 的路由搜索空间、token 和失败状态都会膨胀。

## 4. Agent control flow

### World2Mind 的三阶段协议

**[论文证据]** (1) 判断问题是否值得调用，避免简单问题过计算；(2) 独立抽取原始视觉、AST 文本、可选 map visualization 的线索，延迟融合；(3) 检查截断漏物、深度坐标漂移等冲突，几何计算与视觉语义交叉验证。它强调一次/少数次复合调用后的证据融合，没有轨迹级策略学习。

### Skill-3D 的迭代协议

**[论文证据]** 场景任务解析 → 检索 top-k skills → MLLM 选择紧凑技能 → 调工具 → 消费输出/传给下游工具 → 回退或回答。GRPO 轨迹奖励为答案、格式和工具三项。

**[代码证据]** 本地 agent 会自动从 `retrieved_skills`/`focus_skills` 选 skill，并将其与模型显式选择合并（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/agent.py:255-315`）；还可检查 must-try tool 是否执行（同文件 `447-482`）。这说明发布代码的控制流比论文概述更繁复，也引入较多环境变量和行为开关，复现时必须冻结配置。

## 5. Memory 与 skill evolution

**[论文证据]** Skill-3D 将成功 rollout 抽成触发条件、证据需求、工具顺序/参数、答案映射；失败 rollout 作为 lesson 或 failure-aware dynamic skill。消融的 VSI 前四数值任务平均：full `69.9`；去 failure lessons `68.1 (-1.8)`；去 dynamic skills `67.8 (-2.1)`；去 static skills `65.6 (-4.3)`；去 MLLM selection `65.5 (-4.4)`；去 retrieval `64.1 (-5.8)`。这支持“检索与选择重要”，但只在 GPT-5.4 与选定四子任务上验证。

**[论文证据]** GRPO 中 offline frozen library + SFT cold start 最稳定；online 更新引入 policy 与 retrieval target 同时变化的 non-stationarity。因此“self-evolving”更准确地说是**阶段式演化并在评测/后训练时冻结**，不是已证明的部署期无限在线学习。

**[代码证据]** 本地实现确实提供成功门控：episode 必须成功、reward `≥0.3` 且有有效工具序列才 promotion（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/skill_learning.py:349-393`）。但当前公开 skeleton 没有生成的 `learned_skills.json`/memory，故无法核查论文实际 skill 数量、内容、失败 lesson 或检索分布。

**[论文证据]** World2Mind 没有相应长期演化机制；它对当前输入构建静态聚合地图。**[推断]** 若组合，World2Mind 输出不应原样长期塞进 Skill Library；skill 应只记“何时查询何类 AST/route 信息”，world state 则应有独立的场景缓存、时间戳、置信度与失效策略。

## 6. 训练

### World2Mind

**[论文证据]** training-free 指不微调基础模型；并不表示零模型、零数据或零 GPU。它依赖预训练 DA3 与 SAM3，推理时还需点云/聚类/地图生成和 frontier-model 调用。论文未报告训练之外的这些成本。

### Skill-3D

**[论文证据]** GPT-5.4 用于教师 rollout/技能蒸馏；SFT `500` 样本、GRPO `1,000` 样本，Qwen3-VL-4B/8B，4×RTX PRO 6000 Blackwell，SFT 约 `3 h`、RL 约 `28 h`，各一 epoch。GRPO group size `8`、batch size `16`、LR `1e-6`、KL `0.05`；SFT LR `1e-5`。

**[代码证据]** 本地 `train_grpo.sh` 与论文超参相符：默认 4 GPU、8 generations、generation batch 16、LR `1e-6`、beta `0.05`（`/Users/roywangj/Desktop/Skill-3D/train/train_grpo.sh:41-74`）。但它硬引用 `plugin/plugin_all_angles.py` 与其中 scheduler/reward functions（同文件 `141-148`），而该 plugin 在本地仓库缺失，故 shell template 不是可直接运行的完整 GRPO 实现。

## 7. 评测与结果：精确读法

### World2Mind 主结果与负结果

| Benchmark | Model | Baseline | +World2Mind | Δ |
|---|---|---:|---:|---:|
| VSI-Tiny | GPT-5.2 | 46.7 | 54.0 | +7.3 |
| VSI-Tiny | Claude-4.6-Opus | 38.4 | 56.0 | +17.7 |
| VSI-Tiny | Gemini-3-Pro | 55.2 | 61.0 | +5.8 |
| MindCube-Tiny | GPT-5.2 | 49.9 | 54.6 | +4.7 |
| MindCube-Tiny | Claude-4.6-Opus | 48.5 | 62.9 | +14.4 |
| MindCube-Tiny | Gemini-3-Pro | 75.1 | 81.6 | +6.5 |

**[论文证据]** 增益最大的细项与 allocentric representation 对齐：Claude VSI route `+30.6`、relative distance `+24.0`、relative direction `+15.6`；GPT MindCube rotation `48.5→68.0 (+19.5)`。但上述平均增益不能掩盖开头列出的五个负结果。论文无 AST/route/ellipse/filter 等组件消融，因此不能把增益唯一归因于 AST。

### Skill-3D 论文结果

| Qwen backbone | 方法 | VSI Avg | BLINK MV | CV Depth | CV RelDist | MMSI PR |
|---|---|---:|---:|---:|---:|---:|
| 4B | w/o Tools | 30.4 | 35.6 | 59.7 | 58.6 | 26.3 |
| 4B | w/ Tools | 38.1 | 48.5 | 73.9 | 72.3 | 31.4 |
| 4B | Think3D | 40.1 | 48.7 | 75.3 | 73.4 | 33.8 |
| 4B | Skill-3D | **49.1** | **60.8** | **79.0** | **77.2** | **38.2** |
| 8B | w/o Tools | 36.7 | 43.8 | 68.8 | 66.5 | 31.0 |
| 8B | w/ Tools | 44.4 | 57.4 | 82.9 | 80.7 | 36.6 |
| 8B | Think3D | 49.6 | 61.7 | 85.0 | 83.3 | 41.2 |
| 8B | Skill-3D | **58.8** | **68.5** | **89.6** | **87.4** | **42.8** |

**[论文证据]** 闭源最醒目的结果是 Gemini-3-Flash MMSI `32.7→54.8`（约 `+67.6%` relative）。GPT-5.4 的 Skill-3D 在表中达到 BLINK `82.0`、CV Depth `96.9`、CV RelDist `93.7`、MMSI `60.4`。

**[论文证据]** 效率表（GPT-5.4, VSI）：w/o tools `52.1`, `0 s`；direct tools `58.2`, `1.2` calls, ETU `39.2%`, `13.2 s`；Think3D `64.7`, `1.8` calls, ETU `58.5%`, `35.1 s`；Skill-3D `70.0`, `2.6` calls, ETU `78.7%`, retrieval `0.5 s`, total `20.8 s`。论文另报 Pi3 七帧约 `21.35 s`，segmentation `0.77 s`、depth `1.51 s`、orientation `0.88 s`。这支持“路由可避开昂贵重建”，但未计教师生成、memory 构建和服务常驻成本。

### 本地无功能工具诊断

| Benchmark | N | 本地 released GRPO-4B | 论文 full Skill-3D-4B | 差值 |
|---|---:|---:|---:|---:|
| BLINK MV | 93 | 47.31% (44/93) | 60.8 | -13.5 |
| MMSI-PR | 365 | 31.78% (116/365) | 38.2 | -6.4 |
| CV Depth-Order | 420 | 88.1% | 79.0 | +9.1 |
| CV Rel-Distance | 420 | 75.5% | 77.2 | -1.7 |
| VSI | 1654 | 30.8% | 49.1 | -18.3 |

**[本地复现实验]** 这些运行的工具服务关闭/调用失败，只保留 checkpoint 与静态 seed skills。MMSI harness 原始 `3.01%` 是整串答案与金标字母比较的 scorer bug，按首字母重算为 `31.78%`。CV-3D 是粗粒度二选任务，无工具 checkpoint 甚至超过论文 full 数字，提示 benchmark/harness/模型内化或运行差异，不能反推工具无用。最关键的负结果是 VSI `30.8≈30.4 w/o Tools`：对视频度量与全局几何，checkpoint 没有替代工具链。

## 8. 代码与论文的差异

### 发布代码比论文更丰富的部分

- **[代码证据]** agent 有检索 trace、自动 skill selection、must-try tools、工具失败计数等诊断（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/agent.py:137-166,255-315,447-498`）。
- **[代码证据]** memory 实现不仅有论文的 Scene Memory/Skill Library，还加入 working、episode、evidence、rule 等多层兼容结构（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/skill_learning.py:221-247`）。
- **[代码证据]** retrieval 可用 Qwen3-Embedding-0.6B，并在加载失败时退化到 hashing embedding（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/skill_retrieval.py:323-364`）。这会显著改变检索质量，复现报告必须记录实际 backend。
- **[代码证据]** evaluation 保存逐题 skill choice、tool call、timing profile 与 normalized score（`/Users/roywangj/Desktop/Skill-3D/examples/evaluation/skill3d_evaluation.py:210-279,336-420`）。

### 关键缺失与不可核查部分

- **GRPO plugin 缺失。** **[代码证据]** shell 指向 `plugin/plugin_all_angles.py`（`train_grpo.sh:141-148`），本地路径不存在；奖励和 multi-turn scheduler 无法由当前 checkout 重建。
- **生成 memory 缺失。** **[代码证据]** README 明确要求 generated Scene Memory and Skill Library（`README.md:256-266`），默认运行又指向 `statics/skill3d_shared/learned_skills.json` 与 `memory`（`README.md:305-314`），当前均不存在。只能退化到代码内 seed skills，不能复现论文 dynamic skills/lessons。
- **ETU implementation 缺失。** **[代码证据]** 在排除文档/第三方噪声后未找到论文式 `Valid(a) ∧ Used(a)` 的评测实现。现有代码能记录 tool success/use trace，但这不等于作者论文中 ETU 判定器，因此本地无法独立复算 `78.7%`。
- **World2Mind 无本地代码。** **[代码证据]** 提供的 vault 目录只有论文、JSON artifacts 与图片，没有实现仓库；故其 AST schema、过滤参数、坐标约定和成本无法代码审计。

### 本地 Skill-3D 是个人 fork，不是干净官方 checkout

**[代码证据]** Git remote 为 `git@github.com:Roywangj/skill-3d.git`，不是 README 的 `skill-3d/Skill-3D` 官方 URL；本地 `main` 在个人提交 `57b419f update_wj`。因此所有代码结论都应标为“本地 fork 证据”，不能无条件归因给论文作者发布版。

**[代码证据]** 本地相对 `origin/main` 还有明确用户修改：为修复模型 hallucinate `temp_frames/...`，加入 per-solve image-path binding，按 session 输入顺序校正 `image_index`/`*_frame_N` 并拒绝不可绑定的多图调用（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/agent.py:88-91,500-754`），随后在 solve 开始绑定合法路径（同文件 `1637-1641`）。这修复了本地 B1 阻塞，但它不是论文方法贡献，比较或复现时必须单列。

## 9. 可复现性与成本

### World2Mind

**优势：** **[论文证据]** 无需收集 SFT/RL 数据或更新 foundation model，理论上可跨 GPT/Claude/Gemini 即插即用。

**缺口：** **[论文证据]** 未公开 $\tau_{\text{pixel}}$、$\tau_{\text{frame}}$、KNN K/分位数、adaptive DBSCAN 参数、尺度/坐标规则、AST YAML schema、route voxel/grid 参数、prompt、sampling、Tiny 样本清单、重试策略、延迟、VRAM、token 与 API 成本。所谓 training-free 不能替代端到端成本报告。

### Skill-3D

**优势：** **[代码证据]** Apache-2.0；工具服务、端口、checkpoint layout、inference shell、SFT/GRPO template 和评测框架已发布。README 估计 DA3 `10–14 GB`、SAM3 `14–20 GB`、GroundingDINO `3–5 GB`、Pi3 `18–28 GB`、SwinIR `2–6 GB`、Orient `3–6 GB`（`/Users/roywangj/Desktop/Skill-3D/README.md:168-205`）。

**缺口：** **[本地复现实验]** 忠实功能工具复现至少被四点阻塞：模型会 hallucinate 图像路径（个人修改已尝试修复）；生成 skill library 缺失；单张 32 GB GPU 难同时放 vLLM+depth+SAM3+Pi3；工具依赖/服务未齐。再加缺失 GRPO plugin 与 ETU evaluator，当前仓库能支持 agent/inference 诊断，却不能一键复现论文完整训练与所有机制指标。

## 10. 优势与弱点

### World2Mind

**优势**
- **[论文证据]** 把 allocentric geometry 变成可检查、可计算、可供文本模型读取的中间表示，而不是只生成更多 render。
- **[论文证据]** landmark AST 与 route grid 分工清晰，分别面向对象度量/拓扑与通行/路径。
- **[论文证据]** 延迟融合和冲突核验承认重建并不可靠，比盲信单一 3D 输出更合理。

**弱点**
- **[论文证据]** Tiny-only、无置信区间、无核心组件消融、无同预算工具横评。
- **[论文证据]** 计数与尺度任务存在明显退化；“5%–18%”平均收益不是单调安全增益。
- **[代码证据]** 无本地实现，复现成熟度低。

### Skill-3D

**优势**
- **[论文证据]** 把“哪个工具能跑”提升为“哪个证据链适合当前场景任务”，ETU 和工具分布直接对准机制。
- **[论文证据]** 成功 workflow + failure lesson 是比原始 trajectory replay 更紧凑的程序性记忆。
- **[代码证据]** 本地有大量可审计 inference/memory/retrieval/tool/evaluation 逻辑，不只是概念图。

**弱点**
- **[论文证据]** 需要 GPT-5.4 teacher、四卡后训练、多项常驻专家工具；其成本不是只有 `20.8 s/query`。
- **[论文证据]** online evolution 不稳定；当前证据更支持 frozen staged evolution。
- **[代码证据]** 关键 plugin、生成 memory 和 ETU evaluator 缺失，论文—发布物闭环不完整。
- **[本地复现实验]** 无功能工具 VSI 基本无内化收益，说明实际部署仍高度依赖工具健康度。

## 11. 各自真正贡献了什么

### World2Mind 的 genuine contribution

**[推断，受论文证据支持]** 真正新意不是“用了 DA3+SAM3”，也不是“让 LLM 看俯视图”，而是设计了一个**面向语言/代理的 allocentric state compiler**：以对象级几何参数和路线拓扑替代稠密点云/纯 render，并配套 query-conditioned 调用和跨模态冲突协议。尚未被充分证明的是：椭圆 AST 是否优于普通 OBB/scene graph、三阶段 prompt 是否是独立增益源。

### Skill-3D 的 genuine contribution

**[推断，受论文与代码证据支持]** 真正新意不是六个工具、GRPO 或 RAG 单件，而是将 3D 工具经验压缩为**scene/task-conditioned procedural skill**，把成功与失败证据、工具成本和回退写成可检索控制先验，再用这些轨迹后训练小模型。最可信的实证支持是 ETU、工具分布、retrieval/selection ablation 与效率折中；最薄弱的是公开 artifacts 尚不能独立复算这些机制指标。

## 12. 什么时候用谁

- **用 World2Mind：** **[推断]** 已有强 foundation model，不想后训练；问题依赖跨帧全局坐标、对象间 metric/topology、route/passability；愿意承担一次复合重建并需要可审计世界状态。
- **用 Skill-3D：** **[推断]** 任务异质、工具很多且成本差异大；需要长期积累“何时用什么证据”的经验；有 teacher/data/GPU 预算，或至少愿意使用 frozen skill retrieval。
- **两者都不用：** **[推断]** 单图简单相对关系、低延迟边缘部署、工具启动成本高于任务价值时，直接 VLM 或单个便宜工具更合理。
- **两者组合：** **[推断]** 视频/多视图中既要全局地图，又要在 DA3、Pi3、检测、分割、朝向和高层地图间进行成本感知选择时。

## 13. 如何组合

建议把 World2Mind 注册为一个 Skill-3D 高层工具，而不是替换整个 tool pool：

1. **Skill card trigger：** `multi-view + global metric/topology/route`，或已有原子工具证据冲突。
2. **参数：** `categories`、`knowledge_type={landmark,route}`、`visualization_type`、frame subset、最大 token/compute budget。
3. **返回：** AST/route 的紧凑 JSON/YAML、字段置信度、来源帧、缺失类别、尺度状态、构建时间；不要只返回无不确定性的精确坐标。
4. **路由基线：** DA3-only 用于单对象/对象对度量；Pi3-only 用于多视图布局/render；World2Mind 用于对象级 allocentric state；检测/分割用于实例核验。
5. **fallback：** AST 漏实例则 detection/SAM3；尺度漂移则 DA3 metric 或已知尺度校准；route 不连通则 Pi3/视觉回看。
6. **memory：** Skill Library 只保存何时调用、查询模板、成功/失败与成本；AST 放 scene-state cache，不与 skill 文本混为一体。

**[推断]** 最大风险是“双重计算”：World2Mind 内部已跑 DA3/SAM3，Skill-3D 又独立跑它们。组合实现必须共享缓存，按工具 DAG 去重，而不是把高层工具当黑盒重复推理。

## 14. 检验组合的最小实验

### E0：先打通正确性与记账（10–20 题 smoke）

- **条件：** direct VLM、DA3-only、Pi3-only、World2Mind-only、Skill-3D routing + World2Mind。
- **记录：** 每题答案、tool success、实际使用证据、调用次数、端到端时间、GPU-seconds、输入/输出 token、API 成本、AST token。
- **成功门槛：** World2Mind tool 可被稳定调用且结果路径/对象 ID 不丢；不把本地无功能工具结果混入正式对比。

### E1：冻结同一感知缓存的表示对照

- **[推断]** 对同一批 DA3/SAM3/Pi3 缓存，仅改变给模型的表示：raw depth/pose、Pi3 render、对象坐标表、OBB scene graph、ellipse AST、route grid。
- **目的：** 区分“底层视觉工具更强”与“AST 编译更好”；这是 World2Mind 当前最缺的归因实验。
- **指标：** accuracy/MRA、负增益样本数、token、算术/坐标错误率。

### E2：路由与预算消融

- 固定任务集，比较：always World2Mind；always Pi3；Skill-3D 在 `{DA3,Pi3,World2Mind}` 路由；oracle router。
- 至少设置等工具调用数、等 wall-clock 或等 GPU-second 三种预算之一，并报告其余两项。
- **关键对照：** DA3 与 Pi3 必须保留；否则无法判断 World2Mind 是表示贡献还是更高计算预算。

### E3：聚焦论文已知正/负任务

- 正向 strata：relative direction、relative distance、route、rotation。
- 负向 strata：object count、absolute distance、object size、room size、Around。
- **判据：** 组合不仅提高均值，还应减少 World2Mind 已报告的负增益；对每题做 paired bootstrap/McNemar，并公开退化案例。

### E4：memory 是否真的学会调用 World2Mind

- 条件：无 skill；static trigger；dynamic skill；dynamic + failure lesson。
- 冻结模型与工具，检验路由 precision/recall、ETU、World2Mind 调用率、重复 DA3/SAM3 比例、总成本。
- **最低要求：** 独立实现并公开 ETU 的 `Valid`/`Used` 判定，同时做“移除该工具输出后答案是否改变”的反事实指标，避免只靠文字提及判定 used。

### E5：小规模严谨集

- 先各取 VSI 的 direction/distance/route/count 各 25 题（总 100），同一题配对运行所有条件。
- 固定 frame、模型 snapshot、temperature/seed、最大 turns、top-k、tool timeout；缓存底层感知。
- 只有在组合相对最强单方法达到预注册门槛（例如平均分至少 `+3` points，且 GPU-second/token 不超过 `1.25×`）后，再扩展完整测试集。门槛数值是**[推断]**的工程建议，不是论文标准。

## 15. 最终 takeaways

1. **[论文证据]** World2Mind 把“看见多帧”转为“读取可计算的全局状态”；Skill-3D 把“拥有六个工具”转为“按场景检索可复用证据链”。
2. **[推断]** 前者最适合作为后者的高层 tool/skill；架构关系应是 `Skill-3D controller → World2Mind state compiler → AST/route evidence`，而非串联两个完整代理。
3. **[论文证据]** World2Mind 的平均增益真实但范围仅 Tiny 且伴随计数/尺度负结果；Skill-3D 的主表、ETU 和效率更系统，但依赖 teacher、后训练和工具服务。
4. **[代码证据]** 本地 Skill-3D 有真实的 agent/memory/retrieval 实现，却缺 GRPO plugin、生成 memory 与 ETU evaluator；本地还是带 image-path binding 修改的个人 fork。代码可读不等于论文已可端到端复现。
5. **[本地复现实验]** 当前本地结果只能称“无功能工具 checkpoint 诊断”：尤其 VSI `30.8` 对论文 w/o Tools `30.4`，直接否定“checkpoint 已内化完整工具能力”的说法。
6. **[推断]** 下一步最值钱的不是直接大规模融合训练，而是冻结同一 DA3/Pi3/SAM3 感知缓存，公平比较 raw geometry、Pi3 render、OBB scene graph 与 AST，并对 compute/token 设硬预算。只有表示增益与路由增益都单独成立，组合才有可信的新贡献。
