# AlloSpatial vs. Skill-3D：异心控制策略与程序性技能记忆的对照

## 一分钟结论

- [AlloSpatial论文证据] **AlloSpatial 的核心对象是“怎样可靠消费一个异心地图工具”**：World2Mind 将自我中心帧编译为异心空间树（AST）/路线图，Harness 强制执行 `JUDGE → COLLECT → ARBITRATE → REFINE/ANSWER`，再以冷启动、GSPO 和 Harness-Gated Trajectory Reward（HGTR）把这套控制协议内化进 Qwen3-VL。
- [Skill-3D论文证据] **Skill-3D 的核心对象是“怎样按场景复用和演化异构工具工作流”**：成功轨迹蒸馏为静态/动态技能，失败轨迹成为 lesson，推理时检索、选择技能并路由 Depth Anything 3、SAM3、GroundingDINO、Pi3、SwinIR、Orient Anything v2 等工具，随后用 SFT 与 GRPO 后训练。
- [推断] 两者不是同一层的直接替代品：AlloSpatial 更像**围绕 World2Mind/AST 的已学习控制策略**，Skill-3D 更像**跨任务的程序性长期记忆与工具编排层**。最佳组合不是把两个 agent loop 串成双重决策，而是让 Skill-3D 只负责检索“何时/以何种参数调用 World2Mind 或其他工具”的技能，让 AlloSpatial Harness 负责本轮证据治理和停止决策。
- [AlloSpatial论文证据] AlloSpatial 最强的实证信号来自稀疏观测：7 帧下 AlloSpatial-4B 在 VSI-Bench Tiny 为 53.5，基座为 45.1；但 15/24 帧时为 51.8/55.9，反而低于基座 53.3/56.3，说明它不是无条件增益。
- [Skill-3D论文证据] Skill-3D 最强的机制信号是 ETU：VSI-Bench 从 39.2% 到 78.7%，且 GPT-5.4 设置下平均运行时间为 20.8 s，低于 Think3D 的 35.1 s；但 ETU 只证明证据被使用，并不等于严格因果贡献。
- [Skill-3D代码证据] 本地 `/Users/roywangj/Desktop/Skill-3D` 是个人 fork（`origin=git@github.com:Roywangj/skill-3d.git`，本地 `main` 比 `origin/main` 多 1 个提交），而且存在用户侧图像路径绑定修复（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/agent.py:88-90,500-741`）。
- [本地复现实验] 本地已完成的是 released GRPO-4B 在**无功能工具**条件下的诊断，不是论文完整系统复现：VSI 30.8、BLINK-MV 47.31%、MMSI-PR 修正后 31.78%、CV-3D 81.79%；因此不能用它们否定或确认论文 full-tool 数字。

## 紧凑总表

| 轴 | AlloSpatial | Skill-3D |
| --- | --- | --- |
| 核心瓶颈 | [AlloSpatial论文证据] 自我中心观测缺少持久异心表示，且模型会误信带噪地图 | [Skill-3D论文证据] 场景异质性导致统一工具策略、工具偏置与无效证据链 |
| 主要表示 | [AlloSpatial论文证据] 查询条件化 AST、对象足迹、路线图、俯视渲染 | [Skill-3D论文证据] Scene Memory、静态技能、动态技能、失败 lesson |
| 工具范围 | [AlloSpatial论文证据] 主要是 World2Mind，加 `view_image` 查看地图 | [Skill-3D论文证据] 六类感知/几何专家工具组成异构池 |
| 控制循环 | [AlloSpatial论文证据] 判断、模态解耷取证、几何—语义仲裁、细化/回答 | [Skill-3D论文证据] 场景分析、技能检索与选择、工具执行、证据整合、记忆更新 |
| 学习 | [AlloSpatial论文证据] 教师轨迹冷启动 + 在线 World2Mind + GSPO/HGTR | [Skill-3D论文证据] 技能演化 + agentic SFT + GRPO；RL 时冻结技能库更稳 |
| 长期适应 | [AlloSpatial论文证据] 主要内化在策略参数；论文未提出跨任务持续技能库 | [Skill-3D论文证据] 成功/失败轨迹更新程序性记忆，但在线更新会造成非平稳性 |
| 最强证据 | [AlloSpatial论文证据] 零帧/帧预算、盲 AST、QA-only/Stage-1 对照 | [Skill-3D论文证据] ETU、静态/动态/失败 lesson、检索/选择消融、效率 |
| 主要风险 | [AlloSpatial论文证据] 重建漂移、精细度量下降、帧预算混淆、模块归因不足 | [Skill-3D论文证据] 任务解析和技能检索错配、工具质量上限、教师/基准风格依赖 |
| 本地可复现性 | [推断] 未在本地识别到 AlloSpatial 代码；只有论文阅读制品，不能声称代码复现 | [Skill-3D代码证据] 有 agent、memory、retrieval、tools、evaluation、SFT/GRPO 模板，但关键生成制品/插件/权重不完整 |

## 谱系：World2Mind → AlloSpatial

[AlloSpatial论文证据] 这里必须把**工具本体**与**控制/训练框架**分开：World2Mind 接收帧、类别、知识类型、足迹格式和场景类型，完成深度/位姿、开放词汇分割、语义点云、实例聚类，并返回 AST 或路线知识；AlloSpatial 在其上增加何时调用、怎样分离视觉/树/地图证据、怎样仲裁冲突、何时重试或停止，以及怎样通过完整轨迹训练策略。可直接对照 [AlloSpatial `paper.md`](<3d agent/AlloSpatial Agentic Harness Framework for Spatial Reasoning in Foundation Models/paper.md>)、[`detailed_paper.md`](<3d agent/AlloSpatial Agentic Harness Framework for Spatial Reasoning in Foundation Models/detailed_paper.md>) 与 [`paper_DeepPaperNote.md`](<3d agent/AlloSpatial Agentic Harness Framework for Spatial Reasoning in Foundation Models/paper_DeepPaperNote.md>)。

[推断] 因而更准确的谱系是：**World2Mind/AST = 结构化空间证据生产器；AlloSpatial = 证据生产器之上的控制政策、交互协议与后训练方法**。不能把 World2Mind 训练自由的 32 帧结果重新命名为“训练后的 AlloSpatial 模型结果”，也不能把 World2Mind 的原始数值直接拿来和 Skill-3D 的 1,654 题测试集横比。

## 任务、输入与输出

- [AlloSpatial论文证据] AlloSpatial 评测 VSI-Bench Tiny（392 题）和 MindCube Tiny（1,050 题）；前者含计数、绝对/相对距离、物体/房间尺寸、相对方向、路线和出现顺序，后者含 around、among、rotation。输出既包括最终答案，也包括多轮 World2Mind 调用与可审计推理轨迹。
- [Skill-3D论文证据] Skill-3D 评测其按类别随机划分的 VSI-Bench（708 train/1,654 test）、MMSI（157/345）、CV-3D（360/840）和 BLINK-MV（40/93）；输入是问题与图像/7 帧视频观测，输出为技能选择、异构工具调用、工具证据和答案。
- [推断] 两篇论文的 VSI 数字**不可直接排位**：AlloSpatial 用官方 Tiny 392 题且主模型表采用 7 帧，Skill-3D 用作者自建的 1,654 题 held-out split；题集、划分和模型基线均不同。

## 表示与状态

### AlloSpatial

[AlloSpatial论文证据] World2Mind 将对象节点编码为中心、椭圆/矩形足迹、朝向、垂直范围、面积和支持点数，并以 YAML AST 表示包含/支撑关系；路线分支把可通行空间和相机轨迹投影到俯视栅格。该状态是**当前问题条件化的场景级认知地图**，而非跨问题积累的经验库。

[推断] AST 的优势是把坐标与点云变成语言模型可解析的对象关系；代价是椭圆/矩形压缩丢失精细形状，且全局坐标依赖位姿与度量校准。

### Skill-3D

[Skill-3D论文证据] Scene Memory 保存轨迹，Skill Library 把成功经验压缩为触发条件、证据需求、工具顺序、参数与回退，并把失败挂为 lesson；静态技能提供任务先验，动态技能提供场景适配。

[Skill-3D代码证据] 本地实现确有分层状态和检索单元：`AdaptiveSkillManager` 定义 rule/working/episode/evidence 层并保存 episode provenance（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/skill_learning.py:96-148,222-347`）；`SkillMemoryUnit` 包含工具候选、fallback、failure memory、成功率与成熟度（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/skill_retrieval.py:89-123`）。

[Skill-3D代码证据] 但仓库跟踪的 `statics/skill3d_shared` 只有 skeleton；README 明说 generated JSON/JSONL 和动态技能不进 git（`/Users/roywangj/Desktop/Skill-3D/statics/skill3d_shared/README.md:1-18`），本地也没有 `learned_skills.json`，故论文使用的真实演化技能库并未随此 checkout 完整提供。

## 工具与 agent loop

### AlloSpatial Harness

[AlloSpatial论文证据] Harness 为 `JUDGE → COLLECT → ARBITRATE → {REFINE, ANSWER}`：先写空间假设并判断工具需求；再将原始视觉、AST 文本和地图渲染作为分离通道；随后显式检查漏检、ghost、坐标漂移和语义冲突；不足时改类别/知识类型/足迹并重查，足够时回答。

[推断] 它的本质是**单一高价值空间工具的证据治理器**，不是通用工具市场路由器；优势是可反驳地图，弱点是所有分支仍共享 World2Mind 后端故障。

### Skill-3D loop

[Skill-3D论文证据] Skill-3D 先解析场景—任务上下文，召回 top-k 静态/动态技能，由 MLLM 再筛为紧凑集合，执行对应工具链，把有效输出用于后续工具或答案；训练阶段再将成功/失败反馈写回记忆。

[Skill-3D代码证据] 本地 `SPAgent` 注册工具与 `AdaptiveSkillManager`，支持自动检索技能、模型显式 `<skill_choice>`、必需工具约束、工具参数修复与多轮执行（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/agent.py:41-130,169-364`）。

[Skill-3D代码证据] 本地检索不是论文一句话描述的黑盒：它能加载静态/动态单元，用 Qwen3-Embedding-0.6B 或 hashing fallback 建索引并点积召回（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/skill_retrieval.py:25-34,261-295,323-364,374-472`）；这证明“有实现”，不证明它复现论文使用的同一索引与技能内容。

## 学习与训练：Harness/GSPO/HGTR 对静态—动态技能/SFT/GRPO

### AlloSpatial

- [AlloSpatial论文证据] GPT-5.2 与 Claude-4.6-Opus 生成完整 World2Mind 轨迹，筛除答案错误、结构不合规、调用无效或缺少非平凡仲裁的样本，作为 Qwen3-VL-4B/8B 冷启动。
- [AlloSpatial论文证据] GSPO 以整条序列为单位；HGTR 权重为结构 0.15、答案 0.60、工具 0.10、长度 0.15。答案奖励受结构门控，工具奖励又绑定有效调用与最终正确，并惩罚超预算调用。
- [AlloSpatial论文证据] 4B/8B 均从 SFT step 240 开始，报告 RL step 600/400；每提示 8 rollout，累计独立提示 4.8K/2.4K，学习率 `1e-6/5e-7`，bf16、FlashAttention、全量语言模块、ZeRO-2，冻结视觉塔与 aligner。

### Skill-3D

- [Skill-3D论文证据] GPT-5.4 从训练样本生成技能/轨迹；500 个 SFT 样本与 1k 个 GRPO 样本，奖励权重为答案 0.6、格式 0.2、工具 0.2；4 张 RTX PRO 6000 Blackwell，SFT 约 3 小时，RL 约 28 小时。
- [Skill-3D论文证据] 论文区分静态技能、动态技能和失败 lesson，并显示 RL 时**离线冻结**技能库优于在线同步更新；这意味着论文中的“evolving”主要是阶段式构库，不是策略训练期间持续无约束演化。
- [Skill-3D代码证据] 本地 SFT 脚本是可参数化的 ms-swift 模板，默认 4 GPU、full tuning、bf16、FlashAttention、ZeRO-2（`/Users/roywangj/Desktop/Skill-3D/train/train_sft.sh:15-28,43-65,115-145`）。
- [Skill-3D代码证据] 本地 GRPO 脚本声明三项 reward 与 0.6/0.2/0.2 权重、8 generations、4 GPU，并硬引用 `plugin/plugin_all_angles.py`（`/Users/roywangj/Desktop/Skill-3D/train/train_grpo.sh:30-74,91-103,137-180`）；该 plugin 在当前 checkout 缺失，所以模板不能按默认命令端到端启动。

[推断] 两者训练目标重叠在“答案 + 格式 + 工具效率”，但归纳偏置不同：AlloSpatial 奖励**按 Harness 顺序消费 AST**，Skill-3D 奖励**按技能选择合适工具链**。若简单相加两套奖励，会把工具选择、AST 质量、Harness 合规和答案正确同时改变，无法归因。

## 记忆与适应

- [AlloSpatial论文证据] AlloSpatial 的“记忆”主要是当前场景 AST/路线图与对话轨迹；训练后适应主要进入模型参数，论文没有跨部署 episode 的持久技能检索与更新机制。
- [Skill-3D论文证据] Skill-3D 明确把轨迹变成程序性长期层：成功流程可合并/晋升，失败成为回退 lesson，并报告单基准动态技能跨基准迁移；All Benchmarks 构库结果为 VSI 69.9、BLINK 82.0、CV-3D 95.3、MMSI 60.4。
- [Skill-3D代码证据] 本地代码支持关闭更新和冻结评测；evaluation 在 solve 时 `auto_update_skills=False`，只在显式 `enable_skill_update` 后用延迟标签反馈更新（`/Users/roywangj/Desktop/Skill-3D/examples/evaluation/skill3d_evaluation.py:507-555,658-700`）。
- [推断] Skill-3D 的长期层更适合记录“厨房距离题先深度、失败后切边界分割”这类程序经验；AST 更适合保存“本场景桌椅的坐标/拓扑”。两类状态不应混入同一个向量库，否则程序知识与瞬时场景事实会互相污染。

## 评测协议与精确结果

### AlloSpatial：协议先于数字

[AlloSpatial论文证据] 训练自由闭源实验在 VSI-Bench Tiny 最多 32 帧；训练后主比较统一 7 帧；帧预算消融为 0/3/7/15/24；MindCube 使用提供的多视图。故 32 帧闭源结果不能减去 7 帧训练后结果来估算训练收益。

| 设置 | 精确结果与边界 |
| --- | --- |
| 闭源、训练自由 | [AlloSpatial论文证据] GPT-5.2：VSI 46.7→54.0，MindCube 49.9→54.6；Claude-4.6-Opus：38.4→56.0，48.5→62.9；Gemini-3-Pro：55.2→61.0，75.1→81.6。 |
| 负任务结果 | [AlloSpatial论文证据] GPT-5.2 的计数/绝对距离/物体尺寸分别下降 5.1/1.5/4.2；Gemini-3-Pro 的物体尺寸下降 13.5。 |
| 7 帧训练后 VSI | [AlloSpatial论文证据] Qwen3-VL-4B 45.1、Qwen3-VL-32B 53.1、Think3D-4B 45.4、AlloSpatial-4B 53.5、AlloSpatial-8B 54.2。 |
| MindCube | [AlloSpatial论文证据] AlloSpatial-4B 总分 69.1；Around/Among/Rotation 为 82.0/65.0/65.5；同一数据的 QA-only SFT 已达 53.9，存在任务格式适配混淆。 |
| 帧预算 | [AlloSpatial论文证据] 0 帧：30.7 vs 48.9；3 帧：40.6 vs 50.0；7 帧：45.1 vs 53.5；15 帧：53.3 vs 51.8；24 帧：56.3 vs 55.9（前者基座、后者 AlloSpatial）。 |
| 训练负结果 | [AlloSpatial论文证据] Stage-1 SFT 在 VSI 从 45.1 降到 38.2；QA-only SFT 从 45.1 降到 43.1；完整 Stage-2 才到 53.5。 |
| 长思考对照 | [AlloSpatial论文证据] 普通 thinking 为 VSI 45.5/MindCube 36.1、平均 1,064 tokens；Stage-2 为 53.5/69.1、平均 358 tokens。 |

[AlloSpatial论文证据] “0 帧”只表示回答模型不看原始帧，AST 仍由 World2Mind 从视觉重建；它不是无视觉系统。

### Skill-3D：论文结果

[Skill-3D论文证据] 以下 VSI 均值是八个子任务的均值；其 test split 为 1,654 题，不能与 AlloSpatial Tiny 的 392 题直接横比。

| Qwen3-VL 设置 | VSI 均值 | BLINK-MV | CV-3D Depth | CV-3D RelDist | MMSI-PR |
| --- | ---: | ---: | ---: | ---: | ---: |
| [Skill-3D论文证据] 4B w/o Tools | 30.4 | 35.6 | 59.7 | 58.6 | 26.3 |
| [Skill-3D论文证据] 4B w/ Tools | 38.1 | 48.5 | 73.9 | 72.3 | 31.4 |
| [Skill-3D论文证据] Think3D-4B | 40.1 | 48.7 | 75.3 | 73.4 | 33.8 |
| [Skill-3D论文证据] Skill-3D-4B | **49.1** | **60.8** | **79.0** | **77.2** | **38.2** |
| [Skill-3D论文证据] 8B w/o Tools | 36.7 | 43.8 | 68.8 | 66.5 | 31.0 |
| [Skill-3D论文证据] Skill-3D-8B | **58.8** | **68.5** | **89.6** | **87.4** | **42.8** |

- [Skill-3D论文证据] ETU：VSI 39.2→78.7%，BLINK 36.4→79.2%，CV-3D 31.8→87.5%，MMSI 30.5→80.3%。
- [Skill-3D论文证据] GPT-5.4 的模块消融（只取 VSI 的 Obj.Count/Abs.Dist/Obj.Size/Room Size 均值）：Full 69.9；去 failure lesson 68.1；去动态技能 67.8；去静态技能 65.6；去 MLLM skill selection 65.5；去 retrieval 64.1。
- [Skill-3D论文证据] 效率表（GPT-5.4）中 w/Tools/Think3D/Skill-3D 的平均调用为 1.2/1.8/2.6，平均运行 13.2/35.1/20.8 s，Skill-3D 检索开销 0.5 s；不同工具链构成不同，不能把运行时间差只归于检索。
- [推断] Skill-3D 没有与 AlloSpatial 做同协议直接对照；任何“58.8 高于 54.2，因此 Skill-3D 更强”的结论都混淆了测试集、划分、模型、工具池和协议。

### 本地 Skill-3D 诊断与负结果

| Benchmark | 本地 released GRPO-4B、无功能工具 |
| --- | ---: |
| [本地复现实验] BLINK-MV（93） | 47.31%（44/93） |
| [本地复现实验] MMSI-PR（365） | 31.78%（116/365，修正首字母 scorer 后） |
| [本地复现实验] CV-3D Depth / RelDist / overall（840） | 88.1% / 75.5% / 81.79% |
| [本地复现实验] VSI（1,654，7 帧） | 30.8 |

- [本地复现实验] VSI 运行中工具调用即时失败且没有有效 Pi3 调用，因此 30.8 约等于论文 w/o Tools 的 30.4，离论文 full Skill-3D-4B 的 49.1 差 18.3 分；这是“checkpoint 不能替代工具”的诊断，不是 full pipeline reproduction。
- [本地复现实验] MMSI 原 scorer 给出 3.01%，因为把 `(B: Billiards area)` 整串与 `B` 比；按首字母重打分后为 31.78%，说明低于随机线的结果必须先审计 harness。
- [本地复现实验] 工具复现阻塞包括：模型生成错误图像路径、缺 `learned_skills.json`、单卡 32 GB 无法同时容纳 vLLM 与多工具、工具包/权重未齐。

## 论文主张与 Skill-3D 代码现实

| 论文主张 | 本地代码现实 |
| --- | --- |
| [Skill-3D论文证据] Scene Memory 与 Skill Library 从成功/失败轨迹演化 | [Skill-3D代码证据] `AdaptiveSkillManager` 与动态 skill unit 的逻辑存在，但公开 checkout 只有 memory skeleton，无论文生成库（`/Users/roywangj/Desktop/Skill-3D/statics/skill3d_shared/README.md:6-18`）。 |
| [Skill-3D论文证据] 推理检索并选择场景技能 | [Skill-3D代码证据] dense/hybrid/symbolic 检索、rerank 和 agent 侧 auto/model choice 均有代码（`/Users/roywangj/Desktop/Skill-3D/skill3d/core/agent.py:93-107,255-364`），但缺真实库时只剩 8 个 seed 静态技能。 |
| [Skill-3D论文证据] GRPO 联合答案、格式与工具奖励 | [Skill-3D代码证据] shell 声明三 reward，但依赖缺失的 `/Users/roywangj/Desktop/Skill-3D/plugin/plugin_all_angles.py`（`/Users/roywangj/Desktop/Skill-3D/train/train_grpo.sh:141-149`），所以当前 repo 不能证明 reward/scheduler 可执行。 |
| [Skill-3D论文证据] ETU 衡量 Valid 且 Used 的调用 | [Skill-3D代码证据] 在本地 Python/sh 搜索未识别到论文 ETU 的独立可执行 scorer；README/infos 有定义和数字，因此当前 checkout 不能直接重算论文 ETU。 |
| [Skill-3D论文证据] 六工具 full pipeline | [Skill-3D代码证据] wrappers/server 入口存在，但 checkpoint 目录仅有 `.gitkeep`，外部工具需单独依赖与权重；README 也把 generated memory、运行服务和 optional plugin 列为未跟踪前提（`/Users/roywangj/Desktop/Skill-3D/README.md:256-266`）。 |
| [Skill-3D论文证据] 官方系统行为 | [Skill-3D代码证据] 本地 repo 是个人 fork，且最新本地提交含图像路径修复；因此本地结果带有用户修改的 provenance，不能无条件称为原作者原样代码。 |

[推断] 对 AlloSpatial 则只有本地阅读制品与论文中给出的 GitHub 项目地址；本次搜索未在本地工作区识别到 AlloSpatial 源码 checkout。除非之后直接取得代码、配置、权重和服务脚本，否则只能评价论文可复现性，不能声称本地代码验证。

## 代码、复现性与成本

### AlloSpatial

- [AlloSpatial论文证据] 训练使用 8 张 Ascend 910B；4B/8B 到报告检查点约 60/40 NPU 小时；World2Mind 以 8 个独立 worker 提供在线服务，单次更新约 4–6 分钟。
- [AlloSpatial论文证据] VSI Tiny 392 题并发评测约 12 分钟，但每题可多轮重建，论文没有给单设备尾延迟、能耗或完整代码环境成功率。
- [推断] 没有本地代码时，提示、表格和服务描述足以复核方法逻辑，不足以复核深度/位姿阈值、SAM3 后处理、请求重试、HGTR 实现及全部数字。

### Skill-3D

- [Skill-3D论文证据] 论文训练成本为 4×RTX PRO 6000 Blackwell，SFT 约 3 h、GRPO 约 28 h；full-tool 推理的成本随技能路由变化，Pi3 七帧约 21.35 s，而分割/深度/朝向约 0.77/1.51/0.88 s。
- [Skill-3D代码证据] 本地 agent/evaluation 代码较完整并包含 checkpoint resume、指标归一化、延迟分解与图像路径绑定，但训练数据、生成记忆、GRPO plugin、专家 checkpoints 尚不完整；所以当前最可信的复现范围是无工具诊断和局部组件测试。
- [推断] 若目标只是研究程序性记忆，Skill-3D 的 memory/retrieval 模块可低成本单测；若目标是复现论文 49.1/58.8 与 ETU，必须恢复同一数据 split、技能库、全部工具、教师轨迹、reward plugin 与模型权重。

## 真正的新意

1. [AlloSpatial论文证据] AlloSpatial 真正新意不是“再接一个 3D 重建器”，而是把低层重建压缩成**可查询、可反驳的异心中间表示**，并用结构门控的完整轨迹奖励学习怎样消费它。
2. [Skill-3D论文证据] Skill-3D 真正新意不是“检索几条历史”，而是把经验压缩成**触发条件—证据需求—工具顺序—回退/失败 lesson**的程序性记忆，并用 ETU 直接诊断工具证据链。
3. [推断] 两者共同揭示的原则是：3D agent 的瓶颈不仅是感知工具精度，而是**表示接口与控制策略**；原始点云/坐标、错误工作流或未验证地图都可能让更强工具带来负增益。

## 优势与弱点

### AlloSpatial

- [AlloSpatial论文证据] **优势**：AST 可在回答模型不看原始帧时独立提供证据；稀疏帧收益清晰；Stage-1、QA-only、长思考和帧预算暴露了若干真实负结果。
- [AlloSpatial论文证据] **弱点**：Tiny 规模、无置信区间/多次训练；15/24 帧优势消失；精细距离/尺寸/计数受重建漂移限制；Harness、AST、在线执行和 HGTR 没有逐项拆分。

### Skill-3D

- [Skill-3D论文证据] **优势**：覆盖四个 benchmark；直接评估 ETU；检索/选择、静态/动态/失败 lesson 有细粒度消融；成本表显示避免盲目 Pi3 可改善准确率—延迟折中。
- [Skill-3D论文证据] **弱点**：随机 30% 类别内划分并非官方 split；教师与所有 benchmark 训练池可能学习格式；在线技能更新反而不稳；ETU 的 Used 判定不是反事实因果。
- [Skill-3D代码证据] **额外工程弱点**：本地公开形态缺生成记忆、plugin 和 checkpoints，导致论文最关键的动态技能、GRPO 与 ETU 链路不能开箱验证。

## 该用哪个

- [推断] **优先 AlloSpatial**：任务是稀疏室内视频/多视图，核心问题是跨视角对象拓扑、路线或视点旋转，而且愿意部署统一的 World2Mind 地图服务并审计地图冲突。
- [推断] **优先 Skill-3D**：已有多个异构工具，主要痛点是不同问题应选不同证据链、需要复用成功 workflow/失败教训，且可维护阶段式技能库。
- [推断] **都不应直接用**：要求高精度测量、动态对象、室外大尺度、机器人实时闭环，或无法承担多 GPU/NPU 工具服务；两篇论文都没有充分证明这些场景。

## 能否组合、怎样组合

### 推荐的三层架构

1. [推断] **程序性长期层（Skill-3D）**：输入问题类型、粗场景签名、历史成功率与成本，检索技能卡；只输出工具族、World2Mind 参数模板、预算和 fallback，不直接决定答案。
2. [推断] **空间工具层（World2Mind/AST + 其他专家）**：World2Mind 生成 AST/路线图；若技能指定精细尺寸或边界，再补 Depth Anything/segmentation，而不是默认全工具并发。
3. [推断] **本轮控制层（AlloSpatial Harness）**：根据视觉、AST 和额外工具证据执行 JUDGE/COLLECT/ARBITRATE；发现技能路由遗漏时允许一次受预算约束的反检索或 fallback，最终停止。

### 重叠与混淆

- [推断] **重叠 1：两者都做工具决策。** Skill selector 与 Harness JUDGE 若同时决定“是否调用”，会产生双重门控；实验中应固定职责：selector 只给候选/参数，Harness 保留最终执行权。
- [推断] **重叠 2：两者都用失败信息。** Skill lesson 是跨 episode 的程序记忆，Harness arbitration 是单 episode 的证据冲突；二者应使用不同存储和时间尺度。
- [推断] **混淆 1：工具质量。** 技能路由变好但 AST 变差，或 AST 变好但技能没选对，都可能改变准确率；必须缓存同一工具输出做配对评测。
- [推断] **混淆 2：训练目标。** 同时加入技能 token、Harness token、在线工具和新 reward 后，无法判断收益来自表示、检索、协议还是训练；需要阶梯式消融。
- [推断] **混淆 3：预算。** Skill-3D 论文是 7 帧，AlloSpatial 闭源是最多 32 帧而训练后为 7 帧；组合实验必须锁定帧数、工具调用上限、重建缓存和 token budget。

## 最小受控实验

1. [推断] **同一基座、同一 7 帧、同一 392 题 Tiny**：Qwen3-VL-4B 分别跑无工具、World2Mind-only、固定 AlloSpatial Harness、Skill retrieval→World2Mind、完整三层组合；所有条件缓存同一 World2Mind 输出。
2. [推断] **职责消融**：固定候选技能后比较 selector 执行权、Harness 执行权和双重门控；主指标为准确率、无效调用率、重试率、平均/95 分位延迟。
3. [推断] **表示因果实验**：在同一轨迹替换为正确 AST、删除 AST、坐标随机置换 AST、对象名保留但几何替换 AST；测答案翻转和仲裁是否识别冲突。
4. [推断] **记忆增量实验**：只静态技能 → 加成功动态技能 → 加失败 lesson；固定 World2Mind 结果，报告 ETU、正确率和每题成本，避免把地图随机性算进记忆收益。
5. [推断] **参数路由实验**：比较固定全类别 AST 与技能选择 categories/knowledge type/footprint；记录对象召回、调用时间和答案，验证技能是否真减少无关重建。
6. [推断] **帧预算矩阵**：3/7/15/24 帧 × 无技能/有技能 × 无 Harness/有 Harness；检验 Skill-3D 是否只在稀疏帧帮助，或能缓解 AlloSpatial 在密集帧下的负增益。
7. [推断] **至少三 seed + 题目级 bootstrap**：AlloSpatial 4B/8B 仅差 0.7 分且两文都缺充分统计；报告置信区间而不是只报单点。

## 最终判决

[推断] **研究判断：二者应被视为互补的两种“agent substrate”创新。** AlloSpatial 更深地解决“空间证据应以什么结构出现、策略怎样验证它”，Skill-3D 更广地解决“不同场景应调用哪条工具程序、经验怎样长期复用”。如果只能选一个做近期复现，当前本地条件下应先用 Skill-3D 做 memory/retrieval 与无工具诊断，因为已有代码；但若目标是形成更有研究新意的系统，应把 **AlloSpatial Harness 作为 learned control policy、World2Mind/AST 作为空间工具、Skill-3D retrieval/memory 作为程序性长期层**，并按上述缓存和职责消融控制重叠与混淆。

[推断] **证据强度判决：** AlloSpatial 对“稀疏观测下 AST 有用”证据较强，对“每个 Harness/HGTR 组件必要”证据不足；Skill-3D 对“技能化工具路由提高 ETU 与 benchmark 准确率”证据较强，对“开放世界持续演化”及“本地 checkout 可完整复现”证据不足。现阶段不应宣称任何一方普遍优于另一方。

## 本地来源索引

- [AlloSpatial论文证据] [`AlloSpatial/paper.md`](<3d agent/AlloSpatial Agentic Harness Framework for Spatial Reasoning in Foundation Models/paper.md>)；[`detailed_paper.md`](<3d agent/AlloSpatial Agentic Harness Framework for Spatial Reasoning in Foundation Models/detailed_paper.md>)；[`paper_DeepPaperNote.md`](<3d agent/AlloSpatial Agentic Harness Framework for Spatial Reasoning in Foundation Models/paper_DeepPaperNote.md>)；[`allospatial_full_text.md`](<allospatial_full_text.md>)；[`source_map.json`](<3d agent/AlloSpatial Agentic Harness Framework for Spatial Reasoning in Foundation Models/source_map.json>)；[`allospatial_note_plan.json`](<allospatial_note_plan.json>)；[`allospatial_note_lint.json`](<allospatial_note_lint.json>)；[`allospatial_evidence.json`](<allospatial_evidence.json>)；[`allospatial_figures.json`](<allospatial_figures.json>)。
- [Skill-3D论文证据] [`Skill-3D/paper.md`](3d%20agent/Skill-3D/paper.md)；[`paper_DeepPaperNote.md`](3d%20agent/Skill-3D/paper_DeepPaperNote.md)；[`source_map.json`](3d%20agent/Skill-3D/source_map.json)；原始 PDF：`/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/IJEAHRZU/Li 等 - 2026 - Skill-3D Evolving Scene-Aware Skills for Agentic 3D Spatial Reasoning.pdf`。
- [Skill-3D代码证据] 本地个人 fork 根目录：`/Users/roywangj/Desktop/Skill-3D`。
- [本地复现实验] `/Users/roywangj/Desktop/Skill-3D/infos/results.md:1-57,188-197` 及其列出的原始 JSON/日志。
