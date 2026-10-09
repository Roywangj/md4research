# 3D Agent × Reasoning Insight(Fable 5 融合版)

> 主线:3D agent 如何获取、组织、验证空间证据(12 篇,见 [3d_insight_fable5](<3d_insight_fable5.md>))。
> 支线:reasoning 模型如何生成工具调用轨迹、以及这些轨迹的收益到底来自哪里(16 篇,见 [Reasoning_insight_fable5](<../Reasoning/Reasoning_insight_fable5.md>))。
>
> 与已有融合版 [3d_insight_with_reasoning](<3d_insight_with_reasoning.md>)(GeoTrace-Agent 路线)的关系:它回答的是"一条好的 3D 工具轨迹长什么样、怎样训练、怎样审计",我基本同意且不重复(第 5 节逐条说明采纳与分歧)。本版回答一个它之前的问题:**轨迹里的工具调用,哪些是推理机制、哪些是训练脚手架、哪些只是便利仪式?** 这个三分决定了 GeoTrace 式系统的每个部件应该放在训练时还是推理时——放错位置,同样的部件清单会得到一个贵十倍且不更准的系统。
>
> 本版不是我两份单目录洞察的拼接。那两份各自给出一个命题(引擎当 oracle;重注入栈+脚手架假说);本版给出的是**两个命题相乘之后才出现的东西**:3D 工具调用的机制-脚手架分解(第 2 节)、3D 目录收敛证据的重新归因(第 3 节)、以及一篇合成论文的完整形状(第 6 节)。

## 0. 四个最重要的判断(TL;DR)

**判断一:两个目录的最强结论放在一起,暴露出 3D agent 线一个无人自查的裂缝。** 3D 线的收敛证据(六篇论文的"确定性翻译层",[3d_insight_fable5](<3d_insight_fable5.md>) 第 2.1 节)证明的是**证据组织形式**的价值;Reasoning 线的 [Position paper](<../Reasoning/TrainingFree/Position Your VLM May Not Be Thinking with Interleaved Images/paper_DeepPaperNote.md>) 证明的是**推理时新观察**的价值常常不存在(删交错图像不掉分、普通 SFT 追平、遮挡后仍高分)。这是两个可分离的主张——3D 目录只证实了前者,却默认了后者。**没有任何一篇 3D agent 论文做过推理时删除工具观察的自查。**

**判断二:3D 工具调用可以按信息论必要性分为三类,三类的正确处置完全不同。** (a) 构造性必要——答案依赖初始视角原理上不含的信息(遮挡背面、新视角几何、度量深度);(b) 分辨率必要——信息在原图但超出编码分辨率(DeepEyes 的 HR-8K 场景);(c) 便利性调用——信息已在上下文,调用只是重组织。脚手架假说预测:(c) 类训练后可拆,(b) 类常被参数先验补偿,只有 (a) 类是不可拆的推理机制。**3D 是唯一能按构造保证 (a) 类题目存在的领域——这是 3D 对整个 thinking-with-images 研究的独特价值,反过来也是 Reasoning 线给 3D 的判决工具。**

**判断三:3D agent 全部活在重注入栈最贵的一层,栈的下面四层在 3D 目录是空白。** Reasoning 线已把注意力增强、KV 重绑定、token 核心集重选、门控路由做熟(PRCR 把回看成本从 7.75T FLOPs 降到 125.83M;三个免费门控信号各自省 token 60-70% 且涨准确率),而 3D 线的每次"回看"都是重新调用工具(Pi3 重建单次约 21 秒)。多视角输入天然有巨大的"证据已在上下文"复用空间,没人用。

**判断四:主推动作是把 Oracle3D-Gym 和四象限脚手架检验合成一篇论文。** 引擎真值保证 (a) 类题目的信息瓶颈,{训练有/无工具}×{推理有/无工具} 四象限给出机制/脚手架判决,判决直接决定部署架构:脚手架占主则"工具训练、无工具部署"(省掉全部推理时工具成本),机制占主则投资门控与停止策略(两条线共同的方法空位)。无论判决偏向哪边都是可发表且两个阵营都需要引用的结论(第 6 节)。

## 1. 主线的现状与它未审计的假设

3D agent 闭环的部件清单已经收敛(证据详见 [3d_insight_fable5](<3d_insight_fable5.md>) 第 1-2 节,此处只列骨架):

| 闭环环节 | 论文 | 关键数字 |
|---|---|---|
| 第 0 层:参考系形式化 | [GCA](<3d agent/Geometrically-Constrained Agent for Spatial Reasoning/paper_DeepPaperNote.md>) | 去 `CR` 掉 6.6,去 `CO` 只掉 1.2 |
| 观察动作:视角策略 | [Think3D](<3d agent/Think3D/paper_DeepPaperNote.md>) | 裸工具 +0.8,RL 策略后 +12.05 |
| 工具之后:几何→语言翻译 | [S-Agent](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>) | 原始 3D 证据 +0.8,L3 专家 +6.9 |
| 跨问题:技能与经验 | [Skill-3D](<3d agent/Skill-3D/paper_DeepPaperNote.md>) | ETU 39.2%→78.7%,且快于重建中心路线 |
| 训练配方 | [Thyme](<../Reasoning/Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>) | 观察掩蔽+结果中心奖励;过程奖励掉分 |

这条闭环隐含一个从未被检验的假设:**每次工具调用产生的观察参与了最终答案**。Skill-3D 的 ETU 测的是"工具输出有效且出现在后续推理中",不是"答案因它而变";Thyme 的失败案例里明确出现"裁剪了无关区域、靠已有知识碰巧答对"。而支线的 Position paper 恰好证明:在 2D thinking-with-images 里,这个假设大面积不成立(DeepEyes V* 删图 84.3→84.3;Thyme HR-8K 删图 72.3→72.4)。

**3D 不天然免疫。** VSI/MMSI 全是多选题,与 Position paper 审计的 benchmark 同一格式;S-Agent 和 Skill-3D 的训练数据同样来自强 teacher 蒸馏(与 Position paper 指出的"普通 SFT 追平"机制完全对齐);Think3D 弱模型裸工具只 +0.8,说明观察本身在小模型上几乎不产生增益——增益在 RL 改变的行为分布里,这正是脚手架收益的特征。

## 2. 核心命题:3D 工具调用的机制-脚手架分解

支线给出的脚手架假说(详见 [Reasoning_insight_fable5](<../Reasoning/Reasoning_insight_fable5.md>) 第 3 节):Position paper 的推理时删图不掉分与 DeepEyes 的训练时消融(iMCoT vs text-only RL,HR-8K 72.6 vs 60.8)同时为真的最简解释是——**交错视觉行动的收益在训练期沉淀进参数,推理时的调用在多数 benchmark 上已是仪式**。

把这个假说带进 3D,得到本版的核心命题:

> **3D 工具调用应按"答案对推理时新观察的信息论依赖"分为三类,每类的正确工程处置不同:**
>
> | 类别 | 定义 | 3D 例子 | 预测 | 处置 |
> |---|---|---|---|---|
> | (a) 构造性必要 | 初始编码原理上不含答案所需信息 | 遮挡背面的物体关系;需新视角才可见的几何;精确度量深度 | 删除观察必掉分——真机制 | 保留推理时调用,投资门控/停止策略 |
> | (b) 分辨率必要 | 信息在原图但超出编码分辨率 | 远处小物体计数;细小部件朝向 | 常被参数先验部分补偿(Position 遮挡实验:微调模型仍高出基座 9-12 点) | 训练时保留,推理时按门控信号选择性调用 |
> | (c) 便利性调用 | 信息已在上下文,调用只做重组织 | 对已见视角重新渲染;对已有点云重复查询;多视角下的冗余 crop | 训练后可完全拆除——纯脚手架 | 蒸馏进参数,或降层到 L1-L4 廉价复用 |

三个直接推论:

**推论一(对评测):现有 3D benchmark 的类别构成未知,这使所有"agent 学会了用工具"的主张不可解释。** 如果 VSI/MMSI 被 (c) 类主导——多视角输入已含答案、单视角先验可解——那么 Skill-3D 的 ETU 79% 测量的主要是轨迹格式合规性,Think3D RL 的 +12.05 主要是行为分布收益。这不是说这些工作错了,而是说它们的数字**无法归因**。测量类别构成本身就是一篇 analysis paper(第 6 节 Step 1)。

**推论二(对训练):翻译层和观察是两种资产,前者已被证实、后者未被证实。** 3D 目录六篇的收敛证据(S-Agent L3、GCA 约束、Think3D 锚点、Skill-3D 技能、DeepScan 自底向上、Thyme 掩蔽)全部是关于"证据进入上下文之后如何被组织"的——这层收益与"观察是否新"无关,删图实验不会否定它。**所以即使脚手架假说在 3D 成立,翻译层的投资也不会白费;白费的会是昂贵的重建-渲染循环。** 这是对 3D 线最有安慰性也最有指导性的一条边界。

**推论三(对部署):3D agent 的成本结构可能被高估了一个数量级。** 若 (c) 类占主,正确的部署形态是"工具轨迹训练 + 无工具推理"(Position 的 SFT 实验间接支持),Pi3 的 21 秒、S-Agent 未报告的多轮时延、A4-Agent 串四个大模型的成本大部分可以省掉。当前没有任何一篇论文的成本报告能支持或反驳这一点([3d_insight_fable5](<3d_insight_fable5.md>) 第 3.4 节:成本是系统性沉默项)。

## 3. 支线注入主线:重注入栈在 3D 的重映射

Reasoning 线按"证据重注入发生在推理栈哪一层"排出 L1-L6 谱系。把它映射到 3D,空白一目了然:

| 栈层 | Reasoning 线的成熟做法 | 3D 对应物 | 3D 目录现状 |
|---|---|---|---|
| L1 注意力增强 | [SDR-MCoT](<../Reasoning/TrainingFree/Mitigating Low-Quality Reasoning in MLLMs Self-Driven Refined Multimodal CoT with Selective Thinking and Step-wise Visual Enhancement/paper_DeepPaperNote.md>) 逐步视觉增强 | 推理步对相关视角/区域的注意力再加权 | **空白** |
| L2 KV 重绑定 | [PRCR](<../Reasoning/TrainingFree/Position Rebinding Cache Reuse Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning/paper_DeepPaperNote.md>) 免回放回看(FLOPs -5 个数量级) | 多视角证据回看:视角特征+相机位姿+推理步绑定的三元组记忆 | **空白**(S-Agent 双记忆存文本证据,不存可复用编码) |
| L3 token 核心集重选 | [VisRef](<../Reasoning/TrainingFree/VisRef Visual Refocusing while Thinking Improves Test-Time Scaling in Multi-Modal Large Reasoning Models/paper_DeepPaperNote.md>) DPP 相关+多样(79.3 vs 随机 75.6) | 从已编码多视角中选对象级证据子集,替代重新渲染 | **空白** |
| L4 重编码 | [DaP-ICoT](<../Reasoning/TrainingFree/Lets Think with Images Efficiently An Interleaved-Modal Chain-of-Thought Reasoning Framework with Dynamic and Precise Visual Thoughts/paper_DeepPaperNote.md>) 对象级插入,logit 间隔门控 | 局部放大/变尺度重编码已有视角 | 部分存在(DeepScan 的 crop 属于此层) |
| L5 外部行动 | [DeepEyes](<../Reasoning/Train/DeepEyes Incentivizing Thinking with Images via Reinforcement Learning/paper_DeepPaperNote.md>)/[DeepEyesV2](<../Reasoning/Train/DeepEyesV2 Toward Agentic Multimodal Model/paper_DeepPaperNote.md>)/Thyme | 检测/深度/重建/渲染/仿真 | **3D 目录全部集中在这里** |
| L6 表示训练 | [PFlowNet](<../Reasoning/Train/Perceptual Flow Network for Visually Grounded Reasoning/paper_DeepPaperNote.md>) 可行域监督 | 把"看哪个视角/哪个对象"训成中间表示 | **空白**(Think3D-RL 最接近,但监督的是动作不是表示) |

两条工程规则从这张表直接掉出来:

**规则一:降层优先(descend before ascend)。** 每次需要证据时,先检查栈下层能否满足——已编码视角的重绑定回看(L2)、对象级核心集重选(L3)——只有门控信号确认"上下文确实不含所需信息"时才升到 L5 调用昂贵工具。三个免费门控信号(首 token 熵、top1-top2 logit 间隔、答案分布熵)分别省 token 68%/72.6%/自适应停止且都涨准确率,放在 Pi3 重建的 21 秒面前,这个路由的性价比在 3D 比在 2D 高一个数量级。**这与 GeoTrace 版用 reward 惩罚控制成本的思路不同:门控是免训练的推理时机制,不占用 RL 的优化预算。**

**规则二:渲染结果不进上下文,翻译后才进。** MINT-CoT 的整图交错使 MathVista-Math 从 64.07 暴跌到 40.37——插错粒度的证据比不插更糟。3D 的对应禁令:新渲染的视角图不应整幅塞回轨迹,应先过 S-Agent L3 式翻译层变成对象级/关系级 typed evidence。两条线在这里严丝合缝:Reasoning 线的重注入质量层级(整图<随机 token<相关 token<相关+多样≈完整对象)就是 S-Agent L2→L3 结论(+0.8 vs +6.9)的 2D 版本。

## 4. 支线给 3D 轨迹生成的七条已验证规则

这是"reasoning 生成调用工具的轨迹"支线的主体——每条规则都有 Reasoning 目录的消融背书,右列是 3D 落点:

| # | 规则 | 支线证据 | 3D 落点 |
|---|---|---|---|
| 1 | RL 不发明协议,只在已有行为邻域选择;冷启动必须建协议 | DeepEyesV2 pioneer experiment:直接 RL 两种失败(退回文本 CoT / 占位式代码) | S-300K 式 SFT 是必要投资;RL 阶段的健康信号是调用频率下降+方差保留,不是调用变多 |
| 2 | 奖励条件化,工具分只在答对时发;过程/频率/执行奖励有害 | DeepEyes 条件 75.1 vs 无条件 72.1 vs 无 53.4;Thyme 过程奖励 62.9 vs 结果+一致性 65.7 | Skill-3D 式 GRPO 中 `R_exec`/`R_frame` 必须被 `R_ans` 门控 |
| 3 | 工具观察掩蔽出 loss,防伪造 | Thyme 消融:掩蔽是朴素混合训练后最关键的恢复步骤 | GeoTrace 版已采纳(`loss_mask="true"`),沿用 |
| 4 | 重注入粒度决定成败,整图有害 | MINT-CoT 64.07→40.37;VisRef 随机≈不选 | 第 3 节规则二;轨迹里的 `<observation>` 应是 typed evidence 不是原始渲染 |
| 5 | teacher 轨迹降级为可行域,不当行为真值 | PFlowNet:专家框最紧≠最有用;λ 中间最优,两端分别退化为 MLE/纯模仿 | 直接解 3D 线同源耦合病([3d_insight_fable5](<3d_insight_fable5.md>) 第 3.2 节):GPT-5.4 轨迹只给必要证据集合+禁止行为,工具顺序留给策略探索 |
| 6 | 视觉记忆=内容+空间坐标+解码位置,缺一即崩 | PRCR 直接复用 66.44→23.50、卡死率 81%,重绑定后追平回放 | 多视角 provenance memory 的实现规范:视角特征+相机位姿+当前推理步绑定;这是 GeoTrace 版 `B_t` 的系统层实现方案 |
| 7 | "何时看"的免费信号成熟且从未被组合 | 首 token 熵/logit 间隔/答案熵三信号,零训练,各自省 60-70% | 昂贵 3D 工具前的三级路由;Oracle3D-Gym 的最小工具链真值可逐样本标定门控信号的召回率——**这是引擎底座对门控研究的独特贡献:2D 里门控只能对答案对错校准,3D 引擎里能对"是否真的需要这次调用"校准** |

## 5. 对已有融合版(GeoTrace-Agent)的评估

[3d_insight_with_reasoning](<3d_insight_with_reasoning.md>) 是三版旧洞察里最完整的一份,先说采纳:belief-update 轨迹表示(§3)、typed evidence 格式(§2.2)、四类正样本+五类负轨迹(§6)、以及最重要的——**它的反事实矩阵和 TNG/CGF/IER 三指标(§8)先于我提出了因果审计的完整设计**,我在 [3d_insight_fable5](<3d_insight_fable5.md>) 的反事实协议与它同构,应当明确承认这一点。

三个分歧,按重要性排序:

**分歧一:TNG 的解释学需要修正。** GeoTrace 版把 `TNG = Acc_full − Acc_no-observation` 当作工具价值的判决指标,隐含"TNG 低 → 工具没用 → 训练方向错了"。脚手架假说给出第三种读法:**TNG 低可能意味着工具在训练时有用、推理时冗余——训练没有白费,是部署方式错了。** 区分这两种情况必须加训练侧对照(四象限的另一轴),单靠推理时删除无法判决。这不是否定 TNG,是指出它只测量了 2×2 矩阵的一行。

**分歧二:轨迹表示整个活在 L5,缺降层复用。** GeoTrace 的 `A_t` 全是外部工具动作,回看旧证据靠 memory lookup(文本层);它没有 L2 的编码级复用和 L3 的核心集重选,成本控制完全押在 reward 惩罚上。第 3 节的两条规则可以直接作为它的修正案:evidence-need predictor 之后加一个"栈层路由器",cheap 分支不是"便宜的工具"而是"不调工具"。

**分歧三:底座问题(与 [3d_insight_fable5](<3d_insight_fable5.md>) 第 4 节相同,不展开)。** 它的数据主路仍是现有 benchmark 上的 teacher 轨迹,关键新指标(Reference Frame Accuracy、CGF)在真实图像上没有真值可标,最终还是要请 GPT 当裁判。规则 5(可行域监督)+引擎真值是目前最好的组合解。

## 6. 合成主推:一篇论文的完整形状

把两条线的两个主命题相乘,得到我认为当前最值得写的一篇:

> **《Mechanism or Scaffold? Disentangling Tool-Use Gains in 3D Spatial Reasoning》**
> 底座:Oracle3D-Gym(引擎真值,[3d_insight_fable5](<3d_insight_fable5.md>) §5)。判决工具:四象限+反事实([Reasoning_insight_fable5](<../Reasoning/Reasoning_insight_fable5.md>) §6 方向二)。判决对象:第 2 节的 (a)(b)(c) 三分。

**Step 1(2-3 周,纯推理时干预,零训练):测量现有 3D benchmark 的类别构成。** 在 100-200 个 Blender 场景 + VSI/MMSI 子集上,对现成 pipeline(GCA/S-Agent 风格复现)的每条成功轨迹做两种干预:推理时删除工具观察(Position 协议)、程序化扰动工具输出(深度 ±20%/参考系旋转/实例错绑,引擎真值判定答案应否翻转)。产出一张表:每个 benchmark 上 (a)(b)(c) 三类调用的实测占比 + 表面 ETU 与反事实翻转率的裂口。**这张表无论长什么样都是独立可发表的 analysis paper,且是后续一切的选题依据。**

**Step 2(1-2 月,小规模训练):四象限判决。** 构造两组引擎题——(a) 类保证组(遮挡背面/新视角依赖,按构造"不调工具无法作答")和普通组。Qwen3-VL-4B/8B 上做 {训练有/无工具}×{推理有/无工具} 四格,训练侧用规则 1-5 的收敛配方。预期:普通组上"训练有+推理无"接近"训练有+推理有"(脚手架),(a) 类组上推理时删图首次显著掉分(机制)。**两个结果同时出现是最好的结局:它把 Position paper 的批评和工具训练的价值同时安放在正确的位置上。**

**Step 3(判决驱动,二选一):**
- 脚手架占主 → 蒸馏无工具部署版 + 只保留 (a) 类调用的最小 agent,主打成本结论(推论三);
- 机制占主 → 投资门控与停止策略(两条线共同的方法空位:Think3D 只训了"调用什么",P3D-Bench 的停止差异、MPMWorlds 的前缀 gate 都只有观察性证据),用 Oracle3D-Gym 的最小工具链真值直接监督"还要不要再调一次"。

与三份前作的分工:GeoTrace 版给了轨迹的**语法**(表示与训练格式),3d_insight_fable5 给了**真值底座**,Reasoning_insight_fable5 给了**判决工具**;本篇论文是三者的最小交集——不需要实现完整 GeoTrace 系统,不需要建完整 Gym,只需要够回答一个问题的场景量和一次小训练。

## 7. 风险与边界

| 风险 | 判断 | 规避 |
|---|---|---|
| 四象限训练侧成本超预算 | 中;比纯推理干预贵一个量级 | Step 1 先行,若普通 benchmark 上删图已显著掉分(与 2D 结论相反),训练侧可缩减为单象限验证 |
| 脚手架假说在 3D 完全不成立 | 这不是风险,是"机制"判决——同样有信息量且更利好 3D 线 | 论文标题写成问句,两个方向都有预设结论段 |
| (a) 类题目被质疑人工设计痕迹重 | 中 | 遮挡/视角依赖用引擎的可见性真值程序化生成,附"单视角人类也答不对"的行为学对照 |
| 与 Position paper 撞车(他们做 3D 版) | 低-中;他们明确说了不提供新 benchmark | 我们的差异化在引擎真值+训练侧四象限,他们只做了推理侧 |
| 合成→真实 gap | 与 [3d_insight_fable5](<3d_insight_fable5.md>) §7 相同 | 每个实验带 VSI/MMSI 迁移列 |

## 8. 结论

主线与支线各自收敛到一句话:3D 线——部件清单已定,缺的是真值底座;Reasoning 线——武器已分层,缺的是机制/仪式的判决。相乘之后的结论:

> **3D agent 研究的下一步不是把轨迹造得更精致,而是先回答"轨迹里的工具调用是机制还是脚手架"。3D 是唯一能按构造回答这个问题的领域——引擎真值让 (a) 类题目可批量生成,让删除与扰动有客观判据。判决之前,继续在 L5 堆昂贵工具和继续用 GPT 当裁判一样,都是在未审计的假设上加杠杆;判决之后,无论哪个方向胜出,架构选择(蒸馏拆除 vs 门控调度)都会第一次有证据支撑。**

如果只做一件事:先做 Step 1 的类别构成测量。它同时是 [3d_insight_fable5](<3d_insight_fable5.md>) 反事实裂口实验的超集、GeoTrace 版 TNG 指标的正确化、和脚手架假说在 3D 的第一次落地——三份前作在这一个实验上会合。

## 9. 来源

**3dAgent 主线**（Thyme 位于 `Reasoning/Train`，其余位于本目录；arXiv ID 见 [3d_insight_fable5](<3d_insight_fable5.md>) §9）：[Skill-3D](<3d agent/Skill-3D/paper_DeepPaperNote.md>) · [Think3D](<3d agent/Think3D/paper_DeepPaperNote.md>) · [S-Agent](<3d agent/S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence/paper_DeepPaperNote.md>) · [GCA](<3d agent/Geometrically-Constrained Agent for Spatial Reasoning/paper_DeepPaperNote.md>) · [Thyme](<../Reasoning/Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>) · [DeepScan](<3d agent/DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models/paper_DeepPaperNote.md>) · [A4-Agent](<3d agent/A4-Agent An Agentic Framework for Zero-Shot Affordance Reasoning/paper_DeepPaperNote.md>) · [CompassAD](<CompassAD - Intent-Driven 3D Affordance Grounding in Functionally Competing Objects.md>) · [P3D-Bench](<3d agent/P3D-Bench Benchmarking MLLMs for Parametric 3D Generation and Structural Reasoning/paper_DeepPaperNote.md>) · [Code2Worlds](<3d agent/Code2Worlds Empowering Coding LLMs for 4D World Generation/paper_DeepPaperNote.md>) · [MPMWorlds](<3d agent/MPMWorlds Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics/paper_DeepPaperNote.md>) · [Gamma-World](<3d agent/Gamma-World Generative Multi-Agent World Modeling Beyond Two Players/paper_DeepPaperNote.md>) · [SimWorld Studio](<3d agent/SimWorld Studio Automatic Environment Generation with Evolving Coding Agent for Embodied Agent Learning/paper_DeepPaperNote.md>)

**Reasoning 支线**(arXiv ID 见 [Reasoning_insight_fable5](<../Reasoning/Reasoning_insight_fable5.md>) §9):[DeepEyes](<../Reasoning/Train/DeepEyes Incentivizing Thinking with Images via Reinforcement Learning/paper_DeepPaperNote.md>) · [DeepEyesV2](<../Reasoning/Train/DeepEyesV2 Toward Agentic Multimodal Model/paper_DeepPaperNote.md>) · [MINT-CoT](<../Reasoning/Train/MINT-CoT Enabling Interleaved Visual Tokens in Mathematical Chain-of-Thought Reasoning/paper_DeepPaperNote.md>) · [PatchCue](<../Reasoning/Train/PatchCue Enhancing Vision-Language Model Reasoning with Patch-Based Visual Cues/paper_DeepPaperNote.md>) · [PFlowNet](<../Reasoning/Train/Perceptual Flow Network for Visually Grounded Reasoning/paper_DeepPaperNote.md>) · [Qwen-LA](<../Reasoning/Train/Qwen Look Again Guiding Vision-Language Reasoning Models to Re-attention Visual Information/paper_DeepPaperNote.md>) · [IVT-LR](<../Reasoning/Train/Reasoning in the Dark Interleaved Vision-Text Reasoning in Latent Space/paper_DeepPaperNote.md>) · [ICoT](<../Reasoning/TrainingFree/Interleaved-Modal Chain-of-Thought/paper_DeepPaperNote.md>) · [DaP-ICoT](<../Reasoning/TrainingFree/Lets Think with Images Efficiently An Interleaved-Modal Chain-of-Thought Reasoning Framework with Dynamic and Precise Visual Thoughts/paper_DeepPaperNote.md>) · [SDR-MCoT](<../Reasoning/TrainingFree/Mitigating Low-Quality Reasoning in MLLMs Self-Driven Refined Multimodal CoT with Selective Thinking and Step-wise Visual Enhancement/paper_DeepPaperNote.md>) · [PRCR](<../Reasoning/TrainingFree/Position Rebinding Cache Reuse Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning/paper_DeepPaperNote.md>) · [Position paper](<../Reasoning/TrainingFree/Position Your VLM May Not Be Thinking with Interleaved Images/paper_DeepPaperNote.md>) · [REALM](<../Reasoning/TrainingFree/REALM An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting/paper_DeepPaperNote.md>) · [VisRef](<../Reasoning/TrainingFree/VisRef Visual Refocusing while Thinking Improves Test-Time Scaling in Multi-Modal Large Reasoning Models/paper_DeepPaperNote.md>)

**洞察文档谱系**:[3d_insight](<3d_insight.md>)(GeoSkill-Agent)· [3d_insight_with_reasoning](<3d_insight_with_reasoning.md>)(GeoTrace-Agent,本版的直接对话对象)· [3d_insight_fable5](<3d_insight_fable5.md>)(Oracle3D-Gym)· [Reasoning_insight](<../Reasoning/Reasoning_insight.md>)(因果审计协议)· [Reasoning_insight_fable5](<../Reasoning/Reasoning_insight_fable5.md>)(重注入栈+脚手架假说)· 总览:[Overall](<3d agent/Overall.md>)

> 证据边界声明:全部数字引自两个目录的本地精读笔记(笔记经 grounding 核对),未重新访问原始 PDF。"机制-脚手架三分"、"翻译层收益与观察收益可分离"、"TNG 只测量了 2×2 矩阵的一行"均为我的综合推断,任何论文都未如此表述;其中三分类的 (b) 类边界((b) 与 (c) 在多视角输入下的划分)依赖"初始编码保留了什么信息"这一目前无法直接测量的量,是本框架最需要被实验检验的部分。
