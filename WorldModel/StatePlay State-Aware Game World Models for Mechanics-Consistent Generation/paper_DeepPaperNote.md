# StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation

## 核心信息

- **论文要解决的问题：** 游戏世界模型会生成“像游戏”的视频，却可能违反状态依赖规则：HP 为零后继续攻击、技能槽不足仍放超必杀、胜负画面缺失或颠倒。
- **核心答案：** 将计时器、双方 HP、双方 skill meter 作为显式低维状态，与视频 latent 并行预测；通过共享 joint attention 交换信息，但保留状态/视觉专家分支。
- **规模与数据：** Street Fighter 3；10,000 个 5 秒片段、20 FPS；状态关键片段 40%，普通片段 60%；StatePlay 总参数 5.759B，其中状态分支 0.76B。
- **主要结果：** state alignment 0.947；Gemini-3.1-Pro 机制保真度 82.3±0.5%，GPT-5.5 为 78.3±0.5%；相对最佳无显式状态基线，机制保真度提升 18.6%。

## 原文摘要翻译

StatePlay 将视觉内容和游戏状态联合预测，在保留视觉质量和动作可控性的同时，把生成从像素逼真推进到机制忠实。它的关键主张不是“状态 token 能让视频更好看”，而是内部状态提供了像素监督难以稳定恢复的规则变量，能在终局、技能激活等稀有但关键事件上约束生成。

## 创新点

1. **问题定义前移：** 将 playable 不再等同于视觉逼真与 action-conditioned，而要求生成结果遵守内部状态驱动的机制。
2. **状态–帧–动作数据闭环：** 从 emulator memory 读出 timer、HP、skill meter，并与帧和动作同步；再用状态关键类别平衡数据。
3. **MoT 式模态分工：** 视觉分支处理高维视频 latent，状态分支处理低维规则变量，joint attention 做双向交换。
4. **损失与变量性质匹配：** 视频用 flow matching，状态用 Smooth L1 regression；不是把所有连续量都交给同一种扩散目标。
5. **机制评测显式化：** 用固定决策优先级、参考图和 Gemini/GPT 视觉评审来判定 result_win/result_lose/macro_success/macro_fail/normal。

## 一句话总结

StatePlay 的真实贡献是把游戏世界模型从“动作控制的像素预测器”改造成“由显式状态轨迹约束的机制生成器”，并用模态专门化避免状态学习被视觉生成吞没。

## 研究问题

论文实际回答三个问题：

- 仅靠视觉微调，模型能否学会 HP、技能槽和终局规则？结果是视觉质量可以提升，但机制保真度仍明显不足。
- 显式状态是否能改善帧生成，而不只是提高状态预测分数？StatePlay 在 Gemini/GPT 机制评审上分别达到 82.3%/78.3%，证明状态信号影响了生成行为。
- 状态应该如何接入？MoT 独立专家 + joint attention 优于完全共享 backbone；状态回归优于 flow matching。

## 数据与任务定义

每个训练样本是 5 秒、20 FPS 的 SF3 clip，包含视频帧、11 维玩家动作、五类内部状态（timer、player HP、NPC HP、player skill meter、NPC skill meter）和 NPC 自然语言策略描述。动作空间为 4 个移动、6 个普通攻击、1 个超必杀。

数据分为：result win、result lose、macro success、macro fail 各 1k；normal 6k。分类要求视觉和状态条件同时满足。例如 result win 需要最终帧出现 “You Win” 且 player HP > 0、NPC HP = 0；macro success 要有宏动作、实际超必杀执行且 player skill meter ≥ τ。这个设计把机制边界样本从自然 gameplay 分布中人为抬高，避免模型只学到常见普通帧。

NPC 标签分 offense、control、defense，并要求评审只使用可见行为，不推断隐藏意图。这是控制条件的扩展，使模型不只学“玩家动作→画面”，也能按文本改变 NPC 行为。

## 方法主线

### 机制流程

1. VAE 将视频编码为 $x_0$；状态序列为 $s_0$。
2. 训练时分别加入独立高斯噪声，得到 $x_t$ 与 $s_t$；推理时第一帧状态是条件，其余状态从噪声预测。
3. 视觉分支：VAE latent → visual self-attention → text cross-attention，得到 $H_v$。
4. 状态分支：state encoder → state self-attention，得到 $H_s$。
5. 动作 $A$ 经 action encoder 变为 $A'$，在 token embedding 后同时注入两分支。
6. joint attention 双向交换：视觉 query 读取状态 key/value；状态 query 读取视觉 key/value。
7. 各自 FFN/decoder 输出；视觉用 flow-matching 速度场，状态用回归解码。
8. 训练目标：$\mathcal{L}_{train}=\lambda_{state}\mathcal{L}_{state}+\lambda_{video}\mathcal{L}_{video}$，实验中两个权重均为 1。

![StatePlay 状态—视觉双分支与联合注意力](WorldModel/StatePlay%20State-Aware%20Game%20World%20Models%20for%20Mechanics-Consistent%20Generation/images/page_004_fig_figure_3.png)

图 3 的可视化证据：状态与视频并不是共享同一串 token 后统一去噪，而是各自 self-attention 后通过 joint attention 进行双向读写；动作嵌入同时注入两支。

### 为什么状态必须显式输入

HP、技能槽和计时器不是普通的外观属性。相同的一帧外观可能对应不同的可行动作集合：技能槽满与不满会决定同一宏指令是超必杀还是普通攻击；HP 是否为 0 会决定后续是否必须进入终局。像素变化只给出了结果的局部证据，无法稳定提供“未来允许什么”的因果变量。StatePlay 用状态序列把这些变量直接放入生成轨迹。

### 为什么是 MoT，而不是完全共享

表 2 给出关键证据。共享 backbone + FM 的 state alignment 只有 0.804、Gemini 52.0%；共享 + Regression 变为 0.943、64.7%。MoT + FM 为 0.845、60.7%；MoT + Regression 达到 0.947、82.3%。因此提升不是单纯增加状态分支：模态专门化和正确状态损失都必要。

视觉 token 和状态 token 需要交互，但优化几何不同。视频是高维、感知细节密集的连续生成；状态是低维、规则敏感、时间结构强的变量。完全共享 latent 会让状态信号在视频目标中被稀释；完全隔离又不能让状态约束帧生成。MoT 的 joint attention 是折中。

### 为什么状态用回归而不是 flow matching

flow matching 对高维视频生成合适，但对状态变量会引入不必要的随机扰动和 transport-field 学习。HP 往往是攻击后的离散/分段下降，skill meter 是渐增并在超必杀后重置，转移主要由显式机制决定。Smooth L1 直接对齐目标状态轨迹，更符合这种低维、规则约束的结构。论文报告回归相对 FM 带来 state alignment +12.1%、mechanics fidelity +21.6%。

## 关键结果

### 主结果与强基线

零样本中 ReactiveGWM 的视觉质量最好（SSIM 0.340、LPIPS 0.457），但 Gemini/GPT 机制保真度仅 48.0%/43.3%。这说明视觉能力和机制能力明显分离。状态感知微调后 ReactiveGWM 的 Move-Acc/Att-Acc 很高（95.0/100.0），机制保真度升到 63.7/59.7，但仍远低于 StatePlay。

StatePlay 的 SSIM 0.378、LPIPS 0.424、Move-Acc 92.5、Att-Acc 95.0，state alignment 0.947，Gemini 82.3、GPT 78.3。它没有用牺牲动作控制或视觉质量换机制分数；相反，表中视觉指标也是最佳或并列最佳。

![图 4：状态一致性定性比较](images/page_007_fig_figure_4.png)

注意：主数值表位于 PDF 第 6 页，详见 `paper.md` 的可搜索表格转录；上图为状态一致性最直观的定性补充。

### 消融到底说明了什么

- **架构：** MoT + Regression 相对 Shared + Regression 的 mechanics fidelity 提升 17.6 个百分点；说明状态分支需要保留自己的表示。
- **损失：** 在 MoT 中 Regression 相对 FM 将 Gemini 从 60.7% 提到 82.3%，GPT 从 62.0% 提到 78.3%。
- **输入构造：** 表 5 中广播初始 clean state 得到 alignment 0.938、Gemini 78.3、GPT 76.0；加噪状态得到 0.947、82.3、78.3。加噪让状态输入具有与视频类似的时序演化，而不是每个时间步都看到静态初值。

### 定性证据

图 4(a) 中，技能槽满时 StatePlay 执行超必杀并在执行后重置为 0；ReactiveGWM 不触发，并出现角色纠缠。图 4(b) 中 NPC HP 归零后，ReactiveGWM 仍让 NPC 站立攻击；StatePlay 显示 “You Win”。图 4(c) 中玩家 HP 归零，ReactiveGWM 把玩家画成庆祝胜者，StatePlay 给出正确失败结果。附录图 7 进一步显示，ReactiveGWM 在终局后不显示结果或后续帧模糊，而 StatePlay 保持机制一致。

## 证据强度与评测审计

机制分数不是环境执行器中的硬规则验证，而是 Gemini-3.1-Pro 和 GPT-5.5 的视觉判断。Gemini 直接看视频，GPT 看 24 个均匀采样帧；三次运行报告均值和标准差。提示词强制要求只有可见 “YOU WIN/YOU LOSE” 才能判定胜负，K.O. 或 HP 耗尽本身不够；这减少了评审把视觉暗示当成结果的风险，但也引入评审器依赖。

动作控制由 SAM2.1 + Grounding DINO 跟踪，以及自定义 ClipAttackNet（ResNet-18 + 4-layer dilated TCN，约 5k clips，阈值 0.7）评估。State alignment 使用归一化状态轨迹距离，定义为 $1-$distance。测试集只有 100 个生成样本，机制类别均匀覆盖；因此 18.6% 是在窄领域和小测试集上的结果，不应直接外推到其他游戏。

## 深度分析

### 真正贡献是什么

工程上，StatePlay 是在 Wan2.2-TI2V-5B 上加 0.76B 状态分支、动作投影和联合注意力；概念上，真正重要的是把“机制一致”变成可监督、可评测的中间变量。它给出了一个可迁移接口：任何有 emulator/log state 的交互游戏都可以提供 $s_t$，再选择适合状态性质的目标。

### 为什么结果成立

第一，数据把稀有终局和宏动作样本提升到 40%，让状态信号在训练中有足够梯度。第二，状态与视觉之间是双向而非单向 conditioning：状态指导帧，帧也帮助状态利用视觉动态。第三，回归让低维状态沿目标轨迹学习，避免扩散噪声掩盖规则。第四，评测 prompt 直接针对最容易被误判的边界，区分“看起来 K.O.”和真正显示结果画面。

### 容易误读的地方

- 18.6% 是 mechanics fidelity 的相对改进表述，表格中 StatePlay 与 ReactiveGWM 的绝对差距依评审器为 18.6 或 18.6 个百分点；论文没有详细说明该百分比的统计口径，写作时应避免把它当成跨数据集普适提升。
- “first state-aware game world model” 是作者在其相关工作范围内的优先性主张；WildWorld 和 From Pixels to States 已有显式状态数据集，StatePlay 的新意更准确地说是把状态预测接入生成并证明机制收益。
- 机制评审器是外部 LLM，不等于真实游戏引擎的逐帧执行验证；GPT 只看 24 帧可能漏掉短暂机制。
- 结果来自单一格斗游戏 SF3；并未证明对 FPS 弹药、竞速速度、开放世界任务状态同样有效。

### 复现注意点

需要 Wan2.2-TI2V-5B、Wan2.2 VAE、UMT5-XXL、stable-retro/Gymnasium SF3 接口、emulator memory 地址或等价 state extractor、NPC 标注模型、SAM2.1、Grounding DINO、ClipAttackNet 和两种视觉评审器。训练为 40k steps、batch 4、lr $5\times10^{-5}$、分辨率 480×832。论文没有在正文给出完整代码、状态内存映射、随机种子、采样步数、生成成本或训练硬件，复现仍有明显缺口。

## 局限

1. **数据窄：** 只有 SF3，规则简单且状态变量固定；跨 genre 需要更多同步 state–frame–action 数据。
2. **像素与状态仍会冲突：** 附录 C 承认血条/技能槽偶尔不一致；多个机制同时发生（超必杀与比赛结束重叠）时视觉质量下降。
3. **评测依赖模型：** Gemini/GPT 的 prompt、视频输入能力和参考图影响分数；没有真实引擎状态执行作为唯一权威。
4. **测试规模小：** 100 个样本、三次运行可以给出初步趋势，但不足以支撑强泛化结论。
5. **开放性不明：** 文中未提供训练数据、状态抽取脚本、完整评测代码和所有生成配置，数据与工程复现成本较高。

## 与相关工作关系

在世界模型脉络中，Genie、ReactiveGWM、Incantation、MultiWorld、Lyra 2.0、HY-World 1.5 和 Matrix-Game 3.0 主要推进可交互视频生成、NPC/多实体交互、长时一致性和实时性。WAM/World Action Model 传统上联合视频和动作；StatePlay 把第三类量——内部状态——加入同一生成过程。

在状态建模脉络中，具身 AI 使用 proprioception，自动驾驶使用速度/加速度/占用状态，WildWorld 与 From Pixels to States 开始提供游戏状态标注。StatePlay 的定位不是替代这些数据工作，而是展示“显式 state → 机制一致 frame”这条因果链需要专门架构和损失。

## 可迁移洞见

- 对任何交互生成器，先问“哪些不可见变量决定合法未来”，再决定是否要加状态分支。
- 状态变量应按性质选目标：连续高维观察适合 flow/diffusion，低维规则轨迹可能更适合 regression、分类或约束解码。
- 训练数据要主动重采样规则边界（终局、阈值、失败动作），否则视觉常态会淹没机制梯度。
- 评测应把“视觉发生了什么”与“规则允许什么”分开，并报告 state accuracy、action control、visual quality、mechanics fidelity 四类证据。
- 对写作而言，最稳妥的 claim 是“在 SF3 上证明显式状态有助于机制保真”，而不是“已解决游戏世界模型的物理/规则一致性”。

## 我的笔记

这篇论文最值得保留的是一个研究设计模板：先从可读 emulator state 建立可验证的规则变量，再用双分支模型测试它是否改善生成。若迁移到机器人或 3D world model，可将 HP/技能槽替换为接触状态、可达性、任务 phase 或 object affordance；但必须同时解决状态标注成本和状态—像素不一致。下一步更有价值的实验不是继续堆更大视频模型，而是：(i) 用真实引擎逐帧状态验证替代部分 LLM judge；(ii) 跨至少三类游戏验证规则变量接口；(iii) 测试状态分支是否支持长时 rollout，而不仅是 5 秒片段；(iv) 做状态噪声、缺失状态和错误状态条件下的鲁棒性实验。

## 引用

Lin, Z., Wang, Z., Tan, C., Wen, B., & Jin, Y. (2026). *StatePlay: State-Aware Game World Models for Mechanics-Consistent Generation*. arXiv:2607.26754v1.
