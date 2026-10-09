# Reasoning Insight（Fable 5 精读版）

> 写作说明：本文基于对 `Reasoning` 目录 17 篇论文的完整精读（16 篇笔记位于 `Reasoning`，DeepScan 沿用 `3dAgent` 目录笔记）。已有的 [Reasoning_insight](<Reasoning_insight.md>) 以"可验证工具轨迹 + 因果审计协议"为主轴，写得很好，我不重复它；本版走另一个切面：**把 17 篇按"证据重注入发生在推理栈的哪一层"重新组织**，并处理一个已有版本没有正面解决的矛盾——Position paper 的否定证据与 DeepEyes 自己的消融证据如何同时为真。由此得出本版的核心命题：**脚手架假说**（第 3 节）。

## 0. 四个最重要的判断（TL;DR）

**判断一：这批论文在打同一个敌人——长文本推理会稀释视觉证据，而且这个敌人是真实的、可量化的。** SDR-MCoT 实测普通 CoT 低于直接回答（Qwen2-VL 57.3 vs 59.0；InternVL3-8B 65.9 vs 70.3）；Qwen-LA 实测生成越长 CHAIR 越高、视觉注意力越低；VisRef 实测纯文本自反思不稳定甚至掉分。**"想更久"在多模态下默认是净负资产，除非同步刷新证据。**

**判断二：17 篇方法可以按"在推理栈哪一层重注入或重建证据"排成一个谱系（第 1 节的栈模型），层越深越便宜、越浅越可能带来新信息。** 隐藏状态重建层（LVR）→ 注意力层（SDR-MCoT）→ KV 缓存层（PRCR）→ 已有 token 重选层（ICoT/VisRef/MINT-CoT/IVT-LR）→ 重编码层（DaP-ICoT/Qwen-LA）→ 外部行动层（DeepEyes/Thyme/DeepEyesV2/DeepScan/REALM）。只有最后一层能产生原输入没有的信息，前五层做的都是"信息重组织"。

**判断三：Position paper 与工具训练论文的矛盾可以被一个假说统一：交错视觉行动主要是训练脚手架，不是推理机制。** 推理时删掉交错图像几乎不掉分（Position Table 1），但训练时有无视觉行动差别巨大（DeepEyes iMCoT vs text-only RL 在 HR-8K 上 72.6 vs 60.8）。两个证据同时为真的最简解释：工具训练的收益沉淀进了参数（更好的感知先验和输出分布），而不是留在推理时的工具调用里。这给出一个可检验预测和一个部署含义（第 3 节）。

**判断四：便宜的置信度信号是这个领域被低估的最大杠杆。** 首 token 熵（SDR-MCoT）、logit 间隔（DaP-ICoT）、答案熵（VisRef）三个零训练信号分别实现了 token -68%、-72.6%、自适应停止，且都同时涨准确率。**"何时看"比"怎么看"便宜一个数量级，而且没人把它们组合过。**

## 1. 证据地图：重注入栈模型

所有方法都在回答同一个问题："推理进行到第 t 步、视觉证据已被稀释，现在怎么办？"按干预位置从深到浅排列：

### L0 隐藏状态重建层（不插回 token）

| 论文 | 最硬的证据 | 我最不信的地方 |
|---|---|---|
| [Latent Visual Reasoning](<Train/Latent Visual Reasoning/paper_DeepPaperNote.md>) | 用 ROI 视觉 token 的 MSE 直接监督潜在状态后，Qwen2.5-VL-7B 的 MMVP 从 66.7 升到 72.0；直接对齐优于额外 MLP/GLU 头——**视觉教师目标可以写进连续隐藏状态，而不必显式插图或插 token** | 4/8/16 步收益不单调，学习式停止严重失败；`GRPO_latent` 只在部分设置增益；没有删除、交换或反事实替换隐藏状态，因而未证明潜在轨迹具有因果必要性 |

### L1 注意力权重层（不加任何 token）

| 论文 | 最硬的证据 | 我最不信的地方 |
|---|---|---|
| [SDR-MCoT](<TrainingFree/Mitigating Low-Quality Reasoning in MLLMs Self-Driven Refined Multimodal CoT with Selective Thinking and Step-wise Visual Enhancement/paper_DeepPaperNote.md>)（AAAI 2026） | 消融干净：仅选择性思考 token 212→74 但准确率涨幅有限，仅视觉增强准确率明显升但 token 不降，组合后 token 最少且三项最高——**预算控制器和落地增强器是两个正交部件** | 首 token 熵只适用于短答案/多选；相对注意力（带/不带选项对照）依赖注意力图可靠性，强压缩视觉 token 的模型未必成立 |

### L2 KV 缓存层（复用已编码证据）

| 论文 | 最硬的证据 | 我最不信的地方 |
|---|---|---|
| [PRCR](<TrainingFree/Position Rebinding Cache Reuse Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning/paper_DeepPaperNote.md>) | 先证明"直接复用会崩"（66.44→23.50，卡死率 81%），再定位到 RoPE 过期位置绑定，重绑定后追平甚至略超 token 回放，FLOPs 从 7.75T 降到 125.83M（32B, K=128）——**视觉记忆 = 内容 + 空间坐标 + 解码位置，三者可分离** | 只能复用预填充时已进入模型的证据；需要局部放大/变尺度重编码时无对应条目。代码未公开 |

### L3 已有 token 重选层（从原始视觉 token 中选子集插回）

| 论文 | 最硬的证据 | 我最不信的地方 |
|---|---|---|
| [ICoT](<TrainingFree/Interleaved-Modal Chain-of-Thought/paper_DeepPaperNote.md>) | w/o ADS 消融明确掉分（32.3→29.2 M3CoT）；KV-Copy 变体略差，作者归因于位置无关化——与 PRCR 的发现互为印证 | one-shot 强结果依赖人工设计示例；换行符触发机制脆；patch 数固定 n=64 不自适应 |
| [VisRef](<TrainingFree/VisRef Visual Refocusing while Thinking Improves Test-Time Scaling in Multi-Modal Large Reasoning Models/paper_DeepPaperNote.md>) | 随机选 token ≈ 不选（Table 7），仅相关性有提升，DPP 相关+多样最好（79.3 vs 77.4 vs 75.6）；与训练型 Look-Back 可叠加（83.1 > 各自单独）——**证明重注入的价值全在选择质量** | 延迟 +1.1s/题；token 级证据无对象完整性；需要白盒访问视觉嵌入和文本隐状态 |
| [MINT-CoT](<Train/MINT-CoT Enabling Interleaved Visual Tokens in Mathematical Chain-of-Thought Reasoning/paper_DeepPaperNote.md>)（训练版） | 全篇最有价值的一张表：整图交错使 MathVista-Math 从 64.07 **暴跌到 40.37**，选择性 token 交错升到 67.78——插错证据比不插更糟 | Table 4 显示最大跃迁来自纯文本 CoT SFT（41→64），视觉 token 只贡献后两阶段增量；无因果删除实验 |
| [IVT-LR](<Train/Reasoning in the Dark Interleaved Vision-Text Reasoning in Latent Space/paper_DeepPaperNote.md>)（潜在版） | 去掉潜在视觉掉 25.2 点（M3CoT），大于去掉整个潜在部分（-13.8）；自回归步数 185.7→10，时延 2.63s→0.65s | 中间轨迹完全不可读，无法审计；Table 1/2 数字不一致（94.6 vs 94.1）；固定 3 步潜在深度不自适应 |

### L4 重编码层（新的视觉编码进入上下文）

| 论文 | 最硬的证据 | 我最不信的地方 |
|---|---|---|
| [DaP-ICoT](<TrainingFree/Lets Think with Images Efficiently An Interleaved-Modal Chain-of-Thought Reasoning Framework with Dynamic and Precise Visual Thoughts/paper_DeepPaperNote.md>) | 双模块消融对称且大（w/o PVTG -13.8/-20.4，w/o DVTI -14.4/-20.8）；token -72.6%，插图 2.6→1.2 张/样本；插入后置信度提升率 80.7% vs ICoT 46.4% | "token 降 72.6%"不含 SAM2 分割和候选匹配的成本，端到端时延未报；阈值 τ=0.2 在 M3CoT 验证集上搜的 |
| [Qwen-LA](<Train/Qwen Look Again Guiding Vision-Language Reasoning Models to Re-attention Visual Information/paper_DeepPaperNote.md>)（训练版） | 消融显示行为与证据缺一不可：无 BRPO 时 VTC/VTR 反而掉准确率，无 VTC/VTR 时幻觉降不下来；CHAIRi 9.4→3.7 是全目录最强的幻觉结果 | 附录承认需要更强因果消融；COPY 版长度 268→1811，时延 8.7s→22.3s，开销不小 |

### L5 外部行动层（产生原上下文没有的观察）

| 论文 | 最硬的证据 | 我最不信的地方 |
|---|---|---|
| [DeepEyes](<Train/DeepEyes Incentivizing Thinking with Images via Reinforcement Learning/paper_DeepPaperNote.md>)（ICLR 2026） | 条件工具奖励消融（条件 > 无条件 > 无，HR-4K 75.1/72.1/53.4）；**iMCoT vs text-only RL 在 HR-8K 上 72.6 vs 60.8**——分辨率瓶颈处图像不可替代 | "无冷启动"依赖精心的 perception-utility 数据过滤；POPE adversarial 反而降；被 Position paper 点名审计 |
| [DeepEyesV2](<Train/DeepEyesV2 Toward Agentic Multimodal Model/paper_DeepPaperNote.md>) | pioneer experiment：直接 RL 两种失败模式（无工具奖励→退回文本 CoT；有工具奖励→占位式代码）——**RL 选择行为，不发明协议**；RL 后调用频率下降但方差保留 | RealX-Bench 仅 300 题；InfoSeek 负增益说明搜索并非必胜；工具安全未展开 |
| [Thyme](<Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>) | 奖励消融：过程奖励、代码奖励均低于结果+一致性（62.9/64.5 vs 65.7）——工具表演不能进奖励 | 训练成本口径冲突；OCRBench/ChartQA 退化未归因；被 Position paper 审计后 HR-8K 删图不掉分 |
| [DeepScan](<TrainingFree/DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models/paper_DeepPaperNote.md>)（CVPR 2026） | 同专家条件下自底向上 vs 一次性定位 90.6 vs 83.8；TreeBench 比较推理子项与基座持平——**定位增益 ≠ 推理增益** | 证据完整性由同一 VLM 自评；标准实现 24.5s/题 |
| [REALM](<TrainingFree/REALM An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting/paper_DeepPaperNote.md>)（3D 旁支） | w/o K-means 视角选择 mIoU 0.95→0.38——多视角投票的价值全在视角选择；2D 推理必须回连持久 3D identity | 单查询 83s；REALM3D 标注依赖 Qwen2.5-VL/SAM，与方法调用的模型同源；refinement 500 步反而退化（0.95→0.79） |

### L6 中间表示训练层（把"看哪里"写成可监督对象）

| 论文 | 最硬的证据 | 我最不信的地方 |
|---|---|---|
| [PatchCue](<Train/PatchCue Enhancing Vision-Language Model Reasoning with Patch-Based Visual Cues/paper_DeepPaperNote.md>) | 表示消融：patch-bbox 71.6 > pixel-bbox/point 70.4 > label-only 70.1（≈基线）——**线索要贴近模型输入单位，不是人类标注单位**；cue-only 训练伤泛化 | 平均提升温和（+1~2）；cue 由 GPT-4o 抽取+三模型验证，数据管线依赖强模型 |
| [PFlowNet](<Train/Perceptual Flow Network for Visually Grounded Reasoning/paper_DeepPaperNote.md>)（ICML 2026） | 扩框探测：专家框最紧 ≠ 最有用，几何精度与答案准确率非单调；λ→0 退化为 MLE、λ→∞ 退化为专家模仿，中间最优——**把专家标注从行为真值降级为可行域约束**是全目录最深的监督设计 | 质量/效用奖励均由冻结模型似然估计，可能共享盲点；16×H200 两阶段，复现贵；固定四段流程对简单题过度计算 |

### 机制审计（横切所有层）

| 论文 | 最硬的证据 | 边界 |
|---|---|---|
| [Position paper](<TrainingFree/Position Your VLM May Not Be Thinking with Interleaved Images/paper_DeepPaperNote.md>)（ICML 2026） | 三连击：推理时删交错图像几乎不掉分（DeepEyes V* 84.3→84.3）；普通 SFT 宏平均追平 DeepEyes（65.8 vs 65.3）；**遮挡目标后微调模型仍远超基座（37.7-40.8 vs 28.8）**——benchmark 可被语言先验解出 | 它否定的是"生成了中间图像 = 使用了中间图像"这个过强归因，不是否定视觉工具；attention rollout 非因果证明；未提供替代 benchmark |

## 2. 跨论文收敛的五个机制性结论

### 2.1 重注入内容存在明确的质量层级，插错比不插更糟

四篇论文的消融拼出同一个排序：

> **整图重注入（有害，MINT-CoT 64.07→40.37）< 随机 token（≈无效，VisRef Table 7）< 仅相关 token（有效但冗余，VisRef 77.4）< 相关+多样核心集（VisRef 79.3）≈ 完整语义对象（DaP-ICoT，破碎 token 的修复项）**

这和 3dAgent 目录 S-Agent 的 L2→L3 结论（原始几何需专家翻译）是同构的：**证据的价值不在于存在，而在于粒度与组织形式匹配当前推理步骤**。工程含义：任何"把 X 塞回上下文"的设计，第一个消融应该是随机 X 对照。

### 2.2 视觉记忆是三元组：内容、空间坐标、解码位置——混淆任何两个都会崩

PRCR 的崩溃实验（直接 KV 复用卡死率 81%）证明 RoPE 后的键不是可搬运的内容向量；ICoT 的 KV-Copy 变体变差是同一现象的轻度版本；PatchCue 的 patch 坐标 > 像素坐标则说明连"坐标用什么单位表达"都影响可学习性。三篇独立工作共同指向：**证据表示必须显式分离"是什么、在哪里、现在被绑定到推理的哪一步"**。这直接支持已有版本 Insight 7 的三层记忆设计，并给了它此前没有的机制级证据。

### 2.3 "何时看"的门控信号已经成熟且几乎免费，但从未被组合

| 信号 | 论文 | 成本 | 效果 |
|---|---|---|---|
| 首 token 熵 | SDR-MCoT | 一次前向 | token -68%，准确率 +4.7（Qwen2-VL 平均） |
| top1-top2 logit 间隔 | DaP-ICoT | 解码副产品 | token -72.6%，插图 -54% |
| 答案分布熵 | VisRef | 每步一次估计 | 自适应停止，固定预算下 +6% |
| 前缀重建质量 | MPMWorlds（3dAgent 目录） | 一次比对 | 异常率 0.37/0.86→0.001 |

四个信号分别管路由、插入时机、停止、可信度，处在推理循环的不同位置，理论上完全可组合——**没有任何一篇同时用两个以上**。这是最便宜的空白（第 6 节方向一）。

### 2.4 RL 不发明协议，只在已有行为邻域内做选择——冷启动共识已完全成型

DeepEyesV2 的 pioneer experiment 是最直接的证据（直接 RL 两种失败模式），DeepEyes 的"无 SFT"其实靠数据过滤兜底，MINT-CoT/PatchCue/Qwen-LA/Thyme 全部采用 SFT→RL 两段式。奖励设计也收敛了：**条件化（答对才给工具分，DeepEyes）、一致性（Thyme）有效；过程奖励、无条件工具奖励、代码执行奖励全部失效或有害**（Thyme 62.9/64.5 vs 65.7；DeepEyes 无条件 72.1 vs 条件 75.1）。

PFlowNet 在此之上多走了一步，值得单独记：它把专家监督从"轨迹真值"改成"可行域中心+越界惩罚"（邻域塑形），让任务效用决定可行域内的具体路径。这是对"teacher bias 写进轨迹"问题（已有版本 Insight 6）目前最好的技术答案。

### 2.5 定位增益不等于推理增益，幻觉降低不等于能力提升

DeepScan 的 TreeBench 比较子项持平、Qwen-LA 的准确率涨幅（+1.7）远小于幻觉降幅（CHAIRi -60%）、PatchCue 的温和平均提升，共同说明：这批方法主要修复的是**证据供给**，不是**证据消费**。找到对的证据之后那段推理，仍然是基座模型能力，不被这些机制改变。写论文时把 grounding 提升写成 reasoning 提升，是这个领域最常见的过度声明。

## 3. 核心矛盾及其解决：脚手架假说

这是本版最想立住的一个命题。先摆出矛盾：

- **Position paper**：推理时删除 DeepEyes/Pixel-Reasoner/Thyme 的交错图像，分数几乎不变（Thyme HR-8K 72.3→72.4 甚至略升）；注意力主要流向原图；普通 SFT 追平；遮挡目标后微调模型仍高出基座 9-12 点。
- **DeepEyes 自己的消融**：训练时有无视觉观察差别巨大——iMCoT 训练 vs text-only RL 训练，HR-8K 72.6 vs 60.8。

注意两个实验的干预位置不同：Position paper 删的是**推理时**的图像，DeepEyes 比的是**训练时**的轨迹形态。两者同时为真的最简解释：

> **脚手架假说：交错视觉行动的主要作用是在训练期把"感知-验证"的行为分布刻进参数；训练完成后，推理时的工具调用及其返回图像在多数 benchmark 上已是冗余的仪式。工具是脚手架，大楼建好后拆掉不影响结构。**

这个假说解释了全部四组观察：(a) 推理时删图不掉分——参数里已经有了；(b) 普通 SFT 能追平——分布对齐可以走捷径达成；(c) 遮挡后仍高分——先验被写进参数的副作用；(d) Hide 实验（更好上下文 + 微调先验叠加最优）——两种收益来源可分离。

**可检验预测**：把工具训练模型蒸馏成推理时无工具的版本，应保留绝大部分收益（Position 的 SFT 实验是间接支持）；反之，在"答案可证明无法从初始编码恢复"的任务上（输入强降采样、必须 crop 重编码才能获得的像素），删图应该显著掉分——如果仍不掉，脚手架假说升级为更强的"仪式假说"。

**部署含义**（如果假说成立）：可以用工具轨迹训练、无工具部署，省掉推理时的全部工具成本——这会改变这个领域的成本计算方式。

**对研究的含义**：当前 benchmark 无法区分"脚手架收益"和"推理时证据收益"，因为几乎没有题目在信息论意义上必须依赖推理时的新观察。这正是需要构造信息瓶颈 benchmark 的原因（第 6 节方向二），也与我在 [3d_insight_fable5](<3d_insight_fable5.md>) 提出的 Oracle3D-Gym（引擎真值 + 反事实协议）直接互补：引擎场景可以按构造保证"不调用工具就无法作答"。

## 4. 领域的系统性弱点（审稿人视角）

1. **成本报告货币不统一，无法横向比较。** DaP-ICoT 报 token（-72.6%，但不含 SAM2）；VisRef 报时延（+1.1s）；PRCR 报 FLOPs（-5 个数量级）；Qwen-LA 报长度+时间；DeepScan 报两套协议；SDR-MCoT 报 token。没有一篇同时报 token/FLOPs/wall-clock/显存四项——而这四项在不同方法间的排序可能完全不同。
2. **白盒依赖普遍且很少声明为限制。** SDR-MCoT 要首 token logits + 注意力图，DaP-ICoT 要 top-2 logits，VisRef 要视觉嵌入+文本隐状态，PRCR 要 RoPE 前 KV，ICoT 要 eager attention。整条 TrainingFree 线对闭源 API 几乎全军覆没，"免训练"≠"可部署于任意服务"。
3. **因果审计仍然只有 Position paper 一篇在做。** 其余 16 篇中只有 ICoT（w/o ADS）、IVT-LR（去潜在视觉）、DeepEyes（iMCoT vs text-only）做了接近因果的消融；LVR 虽有 ROI 重建目标，却没有对潜在状态做删除、交换或反事实替换。没有任何训练型论文主动做完整的推理时证据依赖自查。Position paper 提出的检查清单成本极低，不做只能理解为激励问题。
4. **评测几乎全是短答案/多选。** 首 token 熵、答案熵、精确匹配都依赖这个格式；开放式生成、长程 agent 任务下，这批方法的信号和结论都需要重新验证。IVT-LR 的不可读轨迹在多选题上是效率优势，在需要审计的场景是致命缺陷。
5. **数据管线的强模型依赖是训练线的普遍暗账。** PatchCue（GPT-4o 抽取+三模型验证）、MINT-CoT（GPT-4o 对齐网格）、PFlowNet（Gemini/GPT-4o 合成流）、Qwen-LA（GPT-4o 插反思+人工校正）——与 3dAgent 目录的同源耦合问题（3d_insight_fable5 第 3.2 节）完全同构。

## 5. 对已有版本的评估

[Reasoning_insight](<Reasoning_insight.md>) 的因果审计协议（第 9 节七项审计 + 三指标）是两个目录全部洞察文档里最锋利的单项贡献，我完全采纳并且认为它应该直接变成实验代码。它的六阶段工具策略分解、belief-update 轨迹表示也与本版 2.2/2.4 相互支持。

本版补充的三点它没有覆盖：(1) **栈模型**——它按"解决什么问题"分层，我按"干预推理栈哪一层"分层，后者能直接推出组合性与成本结构；(2) **脚手架假说**——它把 Position paper 当作审计工具，我把 Position paper 与 DeepEyes 消融的矛盾当作待解释现象，并给出统一解释和可检验预测；(3) **门控信号的组合空白**（2.3）——它的 router 是设计提案，我指出四个现成信号已经存在且零组合。

一个分歧：已有版本把"外部测量/交互工具"（第三类）列为对 3D agent 最有研究价值的方向，我同意方向但按脚手架假说加一个警告——**除非任务在信息论上强制依赖新观察，否则 3D 工具轨迹训练出的模型同样可能把工具变成仪式**。3D 不天然免疫 Position paper 的批评，只是更容易构造免疫的任务。

## 6. 最值得做的三个方向

### 方向一（最便宜，4-6 周）：全免训练推理栈的组合实验

**空白**：2.3 节的四个门控信号 + L1-L3 的三种重注入机制全部免训练、全部白盒可实现，且已证明两两不冲突（VisRef+Look-Back 可叠加，SDR-MCoT 两模块正交），但没有任何工作把它们组成一个完整控制器：

```text
首token熵路由(SDR-MCoT) → 直接回答 | 进入推理
  推理中: logit间隔触发(DaP-ICoT) → 需要证据?
    已编码证据 → PRCR 重绑定回看(免回放)
    需要重选   → DPP 核心集(VisRef)
  每步: 答案熵停止(VisRef)
```

**最小实验**：Qwen3-VL-8B（PRCR 已验证的骨干）上，在 M3CoT/MathVista/MMStar 复现各单项，再逐步组合，报告统一货币的成本（token+FLOPs+时延）。**预期贡献**：要么得到免训练 SOTA 的 accuracy@cost 前沿，要么发现组合冲突（本身就是发现）。风险低，可发 workshop 或 efficiency track。

### 方向二（主线，与 Oracle3D-Gym 合流）：信息瓶颈 benchmark + 脚手架假说检验

**空白**：第 3 节的可检验预测没人测过。构造两类题：(a) 输入强降采样、目标细节只能通过 crop-and-reencode 获得；(b) 引擎生成场景、答案依赖初始视角看不到的几何（遮挡背面、需要新视角渲染）。每题附"删除工具观察后应答错"的真值。然后对 DeepEyes/Thyme 类模型做四象限测量：{训练有/无工具} × {推理有/无工具}。

**预期结果**：如果脚手架假说成立，现有模型在 (a)(b) 类题上推理时删图会首次显著掉分，且"训练有+推理无"象限在普通 benchmark 上接近"训练有+推理有"。这一张四象限表可以同时回应 Position paper 和为工具训练正名——两边都会引用。

### 方向三（训练线，中期）：把 PFlowNet 的可行域监督与条件工具奖励合并

**空白**：PFlowNet 的邻域塑形（专家框=可行域中心）目前只用于区域选择；DeepEyes 的条件工具奖励只用于调用决策。两者合并即"工具调用的可行域 RL"：teacher 轨迹给出必要证据集合与禁止行为，策略在边界内探索更低成本的调用序列，奖励由结果+一致性门控。这是已有版本"Support-constrained trajectory RL"方向的具体化，现在有了 PFlowNet 的完整技术模板（λ/ε 塑形、子轨迹平衡目标）可以直接迁移。

## 7. 对 3D Agent 项目的直接迁移

与 [3d_insight_fable5](<3d_insight_fable5.md>) 的对接点，按栈层对应：

| Reasoning 目录机制          | 3D 迁移形态                                  | 对接                                           |
| ----------------------- | ---------------------------------------- | -------------------------------------------- |
| 门控信号（2.3）               | 昂贵 3D 工具（Pi3 重建 21s）前的路由：先问"这题需要重建吗"     | Oracle3D-Gym 的最小工具链真值可直接标定门控信号的召回            |
| PRCR 三元组记忆（2.2）         | 多视角证据回看：存原始视角特征+相机位姿+区域坐标，回看时重绑定到当前推理步   | GeoTrace/GeoSkill 的 provenance memory 的系统层实现 |
| 重注入质量层级（2.1）            | 不要把整幅渲染图塞回上下文；选对象级/关系级证据                 | 与 S-Agent L3 专家结论同构，互为 2D/3D 证据              |
| 脚手架假说（3）                | 3D 工具轨迹训练同样可能产出"仪式化调用"；反事实协议必须进评测        | Oracle3D-Gym 的反事实翻转率就是脚手架假说在 3D 的检验器         |
| REALM 的 global/local 分解 | "选哪个对象"和"边界多准"分开优化；2D 推理必须回连 3D identity | 可直接作为 3D 证据前端组件                              |

## 8. 结论

这个目录讲的故事比 3dAgent 目录更收敛：敌人只有一个（视觉稀释），武器按栈分层，门控信号已成熟，训练配方已收敛（冷启动+条件化奖励），监督设计的前沿是可行域约束（PFlowNet）。**领域真正悬而未决的只有一件事：推理时的视觉行动到底是机制还是仪式。** Position paper 把问题问对了，但没有构造能回答它的任务；DeepEyes 的 HR-8K 消融给了"存在机制性收益"的孤证。第 6 节方向二的四象限实验是我认为当前性价比最高的一篇论文——它便宜（全部推理时干预 + 少量可控训练）、两边都需要它、且无论结果偏向哪边都改变这个领域的默认叙事。如果只做一件事，先做它。

## 9. 来源

**Train**：[DeepEyes](<Train/DeepEyes Incentivizing Thinking with Images via Reinforcement Learning/paper_DeepPaperNote.md>)（2505.14362, ICLR 2026）· [DeepEyesV2](<Train/DeepEyesV2 Toward Agentic Multimodal Model/paper_DeepPaperNote.md>)（2511.05271）· [MINT-CoT](<Train/MINT-CoT Enabling Interleaved Visual Tokens in Mathematical Chain-of-Thought Reasoning/paper_DeepPaperNote.md>)（2506.05331）· [PatchCue](<Train/PatchCue Enhancing Vision-Language Model Reasoning with Patch-Based Visual Cues/paper_DeepPaperNote.md>)（2603.05869）· [PFlowNet](<Train/Perceptual Flow Network for Visually Grounded Reasoning/paper_DeepPaperNote.md>)（2605.02730, ICML 2026）· [Qwen-LA](<Train/Qwen Look Again Guiding Vision-Language Reasoning Models to Re-attention Visual Information/paper_DeepPaperNote.md>)（2505.23558）· [IVT-LR](<Train/Reasoning in the Dark Interleaved Vision-Text Reasoning in Latent Space/paper_DeepPaperNote.md>)（2510.12603）· [LVR](<Train/Latent Visual Reasoning/paper_DeepPaperNote.md>)（2509.24251）· [Thyme](<Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>)（2508.11630）

**TrainingFree**：[DeepScan](<TrainingFree/DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models/paper_DeepPaperNote.md>)（2603.03857, CVPR 2026）· [ICoT](<TrainingFree/Interleaved-Modal Chain-of-Thought/paper_DeepPaperNote.md>)（2411.19488）· [DaP-ICoT](<TrainingFree/Lets Think with Images Efficiently An Interleaved-Modal Chain-of-Thought Reasoning Framework with Dynamic and Precise Visual Thoughts/paper_DeepPaperNote.md>)（2603.21754）· [SDR-MCoT](<TrainingFree/Mitigating Low-Quality Reasoning in MLLMs Self-Driven Refined Multimodal CoT with Selective Thinking and Step-wise Visual Enhancement/paper_DeepPaperNote.md>)（AAAI 2026）· [PRCR](<TrainingFree/Position Rebinding Cache Reuse Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning/paper_DeepPaperNote.md>)（2606.26631）· [Position paper](<TrainingFree/Position Your VLM May Not Be Thinking with Interleaved Images/paper_DeepPaperNote.md>)（ICML 2026）· [REALM](<TrainingFree/REALM An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting/paper_DeepPaperNote.md>)（2510.16410）· [VisRef](<TrainingFree/VisRef Visual Refocusing while Thinking Improves Test-Time Scaling in Multi-Modal Large Reasoning Models/paper_DeepPaperNote.md>)（2603.00207）

**关联文档**：[Reasoning_insight](<Reasoning_insight.md>)（已有版本，因果审计协议）· [Overall](<Reasoning/Overall.md>)· [3d_insight_fable5](<3d_insight_fable5.md>)（Oracle3D-Gym 方向）

> 证据边界声明：全部数字引自上述本地精读笔记，未重新访问原始 PDF。IVT-LR 的 94.6/94.1 不一致、Thyme 成本口径冲突等原文问题按笔记保留。"脚手架假说"是我基于 Position paper Table 1/3/4 与 DeepEyes Table 9 的综合推断，论文均未如此表述；其中 Position paper 的删图实验与 DeepEyes 的训练消融干预位置不同（推理时 vs 训练时），这一区分是假说成立的前提，也是它最需要被检验的地方。
