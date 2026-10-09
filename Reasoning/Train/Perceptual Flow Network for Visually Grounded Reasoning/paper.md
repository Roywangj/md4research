---
title: Perceptual Flow Network for Visually Grounded Reasoning
title_cn: 面向视觉落地推理的感知流网络
authors: Yangfu Li, Yuning Gong, Hongjian Zhan, Teng Li, Yuanhuiyi Lyu, Tianyi Chen, Qi Liu, Ziyuan Huang, Zhihang Zhong, Dandan Zheng, Yue Lu
venue: ICML 2026
arxiv: 2605.02730
doi: 10.48550/arXiv.2605.02730
source_type: selectable-text PDF
pages: 36
reader_mode: full-paper bilingual
---

# Perceptual Flow Network for Visually Grounded Reasoning

**中文标题：** 面向视觉落地推理的感知流网络  
**作者：** Yangfu Li, Yuning Gong, Hongjian Zhan, Teng Li, Yuanhuiyi Lyu, Tianyi Chen, Qi Liu, Ziyuan Huang, Zhihang Zhong, Dandan Zheng, Yue Lu  
**机构：** ECNU, SCU, HKUST, SJTU, Ant Group, Shanghai AI Laboratory  
**状态：** Accepted to ICML 2026  
**来源：** arXiv:2605.02730v1, 4 May 2026  

## 页面与章节索引

| 页码 | 内容 |
|---|---|
| 1 | 摘要；引言起始 |
| 2-3 | 几何精度探测；问题形式化；感知流定义 |
| 4-7 | PFlowNet 架构；数据构造；变分 RFT；奖励与几何塑形 |
| 7-8 | 理论分析 |
| 8-11 | 主实验、效率、测试时扩展与消融 |
| 12-13 | 相关工作、结论与局限 |
| 13-17 | 参考文献 |
| 17-27 | 附录 A：理论定义、推导、引理与证明 |
| 27-30 | 附录 B：数据、训练、奖励并行计算与提示词 |
| 30-32 | 附录 C：基准、基线与评测协议 |
| 33-36 | 附录 D：测试时扩展、失败案例与更多示例 |

## Abstract / 摘要

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Despite the success of Large Vision-Language Models (LVLMs), general optimization objectives such as standard maximum-likelihood estimation fail to constrain visual trajectories, leading to language bias and hallucination. Current methods mitigate this problem by adding geometric priors from visual experts as supervision. However, such supervision is usually suboptimal because it is biased toward geometric precision and provides limited reasoning utility.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 尽管大型视觉语言模型已经取得成功，标准最大似然估计等通用优化目标仍无法约束视觉轨迹，因而容易产生语言偏置与幻觉。现有方法通常引入视觉专家的几何先验作为额外监督，但这种监督往往并非最优：它偏向几何精度，却只能提供有限的推理效用。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> To bridge this gap, we propose Perceptual Flow Network (PFlowNet), which avoids rigid alignment with expert priors and achieves interpretable yet more effective visual reasoning. PFlowNet decouples perception from reasoning to establish a self-conditioned generation process, and integrates multi-dimensional rewards with vicinal geometric shaping through variational reinforcement learning. It provides a theoretical performance guarantee and reaches 90.6% on V* Bench and 67.0% on MME-RealWorld-Lite.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 为弥合这一差距，作者提出感知流网络 PFlowNet。该方法放弃与专家先验的刚性对齐，在保持可解释性的同时实现更有效的视觉推理。PFlowNet 将感知与推理解耦，形成自条件生成过程，并通过变分强化学习把多维奖励与邻域几何塑形结合起来。作者给出理论性能保证，并在 V* Bench 与 MME-RealWorld-Lite 上分别达到 90.6% 和 67.0%。

## 1. Introduction / 引言

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> LVLMs extend pretrained language models with vision encoders and cross-modal alignment, and have achieved strong performance on many visual tasks. Nevertheless, interpretability and hallucination remain difficult, especially in fine-grained visual understanding. Recent grounded reinforcement-learning methods distill geometric priors from experts such as GroundingDINO and maximize consistency between model predictions and expert regions.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 大型视觉语言模型通过视觉编码器和跨模态对齐扩展预训练语言模型，在多种视觉任务上取得了较强表现。然而，可解释性与幻觉问题仍然突出，尤其是在细粒度视觉理解中。近期的视觉落地强化学习方法从 GroundingDINO 等专家中蒸馏几何先验，并最大化模型预测与专家区域的一致性。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> A critical question remains: visual experts were designed primarily for object detection, so are their geometric priors truly optimal for reasoning? To probe this issue, the authors use the Qwen2.5-VL family on V* and isotropically expand expert annotations from their centers. Models answer questions using only these evidence crops rather than the full image.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 这里留下了一个关键问题：视觉专家最初主要为对象检测设计，因此它们给出的几何先验是否真的最适合推理？作者在 V* 上使用 Qwen2.5-VL 系列进行探测，从专家标注中心出发等比例扩展区域，并让模型只依据这些裁剪证据而非完整图像回答问题。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The result is counterintuitive: the most geometrically precise prior, namely the expert annotation, is not always the most useful for reasoning. Experts optimize strict localization, but a tight region can induce tunnel vision by excluding contextual evidence needed for comprehensive understanding. The optimal region is also highly instance-specific, making fixed heuristic expansion rules impractical.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 结果与直觉相反：几何上最精确的先验，即专家标注框，并不总是最有利于推理。视觉专家优化严格定位，但过紧区域会排除完整理解所需的上下文，从而产生“隧道视野”。而且最优区域具有很强的样本依赖性，固定扩框规则并不可行。

### Figure 1. Geometric precision versus reasoning utility / 几何精度与推理效用

![Figure 1](Reasoning/Train/Perceptual%20Flow%20Network%20for%20Visually%20Grounded%20Reasoning/assets/page_002_fig_figure_1.png)

**Caption:** Impact of evidence geometric precision (IoU with respect to expert annotations) on reasoning performance. The minimum-precision evidence is the full image, while the maximum-precision evidence is the expert annotation.

**Caption[CN]:** 证据几何精度（相对专家标注的 IoU）对推理准确率的影响。精度最低的证据是完整图像，精度最高的证据是专家标注框。

**Reading note:** 曲线的关键不是“框越大越好”，而是准确率与 IoU 并非单调关系；上下文需求随样本而变。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> PFlowNet replaces rigid alignment with a self-parameterized variational distribution that approximates the posterior of ideal perceptual behaviors. Samples from the optimized distribution condition the model's subsequent reasoning, producing outputs that remain grounded but are more accurate.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> PFlowNet 不再让视觉轨迹刚性贴合静态专家先验，而是使用自参数化变分分布去逼近理想感知行为的后验。模型从优化后的分布中采样轨迹，并用它们调节后续推理，从而在保持视觉落地的同时提高答案准确率。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The method has three components: a structured Perceptual Flow that represents visual behavior; a decoupled framework that separates optimizable perception from answer reasoning; and a variational reinforcement fine-tuning strategy with multi-dimensional rewards and vicinal geometric shaping.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 方法包含三个核心组件：用于描述视觉行为的结构化感知流；将可优化感知与答案推理解耦的框架；以及结合多维奖励与邻域几何塑形的变分强化微调策略。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The authors provide theoretical analyses in Theorems 3.1 and 3.4 and evaluate the method on general and fine-grained visual tasks. Relative to Qwen3-VL-8B, PFlowNet improves V* Bench, TreeBench, and MME-RealWorld-Lite by 13.1, 10.4, and 18.4 percentage points respectively, while also showing favorable efficiency and test-time scaling.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 作者在定理 3.1 与 3.4 中给出理论分析，并在通用与细粒度视觉任务上评测方法。相对 Qwen3-VL-8B，PFlowNet 在 V* Bench、TreeBench 和 MME-RealWorld-Lite 上分别提高 13.1、10.4 和 18.4 个百分点，同时表现出较好的效率与测试时扩展能力。

## 2. Background and Motivation / 背景与动机

### 2.1 Problem Formulation / 问题形式化

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Let $M_\theta$ be an LVLM. For multimodal input $X$ and output tokens $Y=(y_1,\ldots,y_T)$, the model defines an autoregressive distribution $p_\theta(Y\mid X)=\prod_t p_\theta(y_t\mid X,y_{<t})$. Conventional training maximizes the data likelihood $\mathbb{E}_{(X,Y)\sim P_{data}}\log p_\theta(Y\mid X)$.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 设 $M_\theta$ 为大型视觉语言模型。对于多模态输入 $X$ 与输出序列 $Y=(y_1,\ldots,y_T)$，模型定义自回归分布 $p_\theta(Y\mid X)=\prod_t p_\theta(y_t\mid X,y_{<t})$。传统训练最大化数据似然 $\mathbb{E}_{(X,Y)\sim P_{data}}\log p_\theta(Y\mid X)$。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Standard likelihood training does not guarantee that the latent visual reasoning trajectory is valid. The paper therefore treats the sequence of regions or visual actions as a latent variable $Z$. Hallucination can then be viewed as an ill-posed posterior $P(Z\mid X,Y)$ that assigns probability to invalid trajectories.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 标准似然训练无法保证潜在视觉推理轨迹有效。因此，论文把区域或视觉动作序列视为潜变量 $Z$。从这一角度看，幻觉源于后验 $P(Z\mid X,Y)$ 定义不良，把概率质量分配给了无效轨迹。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Given a golden visual trajectory $G$ that mediates $X\rightarrow Y$, the valid support $S_V$ is defined as a $\sigma$-neighborhood of $G$ under a deviation metric. Visually grounded reasoning should generate the correct answer while restricting latent visual rationales to this valid support.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 给定连接 $X\rightarrow Y$ 的理想视觉轨迹 $G$，有效支持集 $S_V$ 被定义为偏差度量下 $G$ 的 $\sigma$ 邻域。视觉落地推理既应生成正确答案，也应把潜在视觉依据限制在这一有效支持内。

### Figure 2. Feasible support and optimization objectives / 可行支持集与优化目标

![Figure 2](Reasoning/Train/Perceptual%20Flow%20Network%20for%20Visually%20Grounded%20Reasoning/assets/page_003_fig_figure_2.png)

**Caption:** Existing methods imitate expert trajectories by maximizing geometric consistency. PFlowNet combines a reasoning-oriented reward with vicinal geometric shaping to explore valid, high-efficacy trajectories.

**Caption[CN]:** 现有方法通过最大化几何一致性模仿专家轨迹；PFlowNet 将面向推理的奖励与邻域几何塑形结合，在有效支持内探索高效用轨迹。

**Reading note:** 左侧对应严格专家对齐，右侧对应“效用驱动 + 邻域约束”；专家轨迹与理想轨迹之间允许存在偏差。

### 2.2 Reasoning over Perceptual Flow / 在感知流上推理

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Because the golden trajectory is intractable, previous methods use visual experts to synthesize a proxy. Those experts optimize grounding rather than downstream reasoning, so their trajectories are biased toward geometric precision. PFlowNet instead approximates the valid posterior $P_V(Z\mid X,Y)$ with a variational distribution $p_\theta(Z\mid X)$.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 理想轨迹无法直接获得，因此以往方法用视觉专家合成代理轨迹。但这些专家优化的是定位而非下游推理，所以轨迹偏向几何精度。PFlowNet 改为使用变分分布 $p_\theta(Z\mid X)$ 逼近有效后验 $P_V(Z\mid X,Y)$。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> A Perceptual Flow is a structured latent trajectory $Z=(z_0\rightarrow z_1\rightarrow\cdots\rightarrow z_K)$. The planning state $z_0$ is a language sequence enclosed by analysis tags; it decomposes the query and identifies candidate evidence. Each perceptual state $z_k=\langle r_k,c_k\rangle$ contains an RoI in relative coordinates and a caption describing the evidence.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 感知流是结构化潜在轨迹 $Z=(z_0\rightarrow z_1\rightarrow\cdots\rightarrow z_K)$。规划状态 $z_0$ 是由分析标签包围的语言序列，用于分解问题并识别候选证据。每个感知状态 $z_k=\langle r_k,c_k\rangle$ 包含一个相对坐标区域和一段描述该证据的文本。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The model uses Sub-Trajectory Balance, a hierarchical variational objective that compares probability flow across every sub-trajectory. Unlike PPO-style reinforcement learning with only terminal supervision, this formulation supplies dense intermediate signals and can preserve diverse perceptual behaviors.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 模型采用子轨迹平衡目标，对任意子轨迹上的概率流进行一致性约束。与主要依赖终端回报的 PPO 式强化学习不同，该目标能提供稠密的中间监督，并保留多样感知行为。

## 3. Perceptual Flow Network / 感知流网络

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For input $X=\langle I,T\rangle$, PFlowNet first samples a perceptual flow $Z$ from its intrinsic distribution and then produces grounded output $Y$ through self-conditioned generation. The joint model factorizes as $p_\theta(Y,Z\mid X)=p_\theta(Z\mid X)p_\theta(Y\mid Z,\langle X,I_{RoI}\rangle)$.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 对输入 $X=\langle I,T\rangle$，PFlowNet 先从自身分布中采样感知流 $Z$，再通过自条件生成得到视觉落地输出 $Y$。联合分布分解为 $p_\theta(Y,Z\mid X)=p_\theta(Z\mid X)p_\theta(Y\mid Z,\langle X,I_{RoI}\rangle)$。

### Figure 3. Overall architecture / 整体架构

![Figure 3](Reasoning/Train/Perceptual%20Flow%20Network%20for%20Visually%20Grounded%20Reasoning/assets/page_004_fig_figure_3.png)

**Caption:** PFlowNet contains two decoupled stages: flow generation and flow-guided reasoning. A frozen reward model evaluates quality, reasoning efficacy, and geometric reliability.

**Caption[CN]:** PFlowNet 包含两个解耦阶段：感知流生成与感知流引导推理。冻结奖励模型评估证据质量、推理效用和几何可靠性。

**Reading note:** 训练主要优化前半段的轨迹分布；推理时把预测区域重新裁剪编码，再与文本流共同生成答案。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Training is progressive. A tailored data pipeline first synthesizes fine-grained trajectories while weakening the inductive bias of visual experts. Supervised fine-tuning bootstraps flow generation, after which variational reinforcement fine-tuning optimizes a reward shaped by both task utility and expert-centered geometric support.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 训练采用渐进策略。定制数据流水线先合成细粒度轨迹，并减弱视觉专家的归纳偏置；监督微调建立生成感知流的初始能力；随后，变分强化微调使用同时考虑任务效用和专家中心几何支持的奖励继续优化。

### 3.1 Training Data Curation and Cold Start / 训练数据整理与冷启动

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Data collection follows two principles. First, tasks should span fine-grained understanding and general-purpose visual reasoning. Second, RoIs should be spatially diverse; cross-expert annotations are used and samples with broad region coverage are retained to reduce overfitting to a narrow spatial pattern.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 数据收集遵循两个原则。第一，任务同时覆盖细粒度理解与通用视觉推理。第二，区域应具有空间多样性；作者使用交叉专家标注，并保留区域覆盖较广的样本，以减少对单一空间模式的过拟合。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For every sample with expert RoIs, each region is randomly expanded. Teacher models such as Gemini3flash and GPT-4o identify critical visual content as the planning state and produce a detailed caption for every expanded region. The planning state and all region-caption pairs are concatenated into a synthetic perceptual flow $Z_s$.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 对每个带专家区域的样本，作者先随机扩展各个区域。Gemini3flash 与 GPT-4o 等教师模型识别关键视觉内容，生成规划状态，并为每个扩展区域撰写详细证据描述。规划状态与所有区域—描述对共同组成合成感知流 $Z_s$。

### Figure 4. Perceptual-flow synthesis / 感知流合成

![Figure 4](assets/page_005_clean_figure_4.png)

**Caption:** Data pipeline for perceptual-flow synthesis.

**Caption[CN]:** 感知流合成的数据流水线。

**Reading note:** 随机扩框用于打破“最紧专家框唯一正确”的偏置；真正决定样本是否保留的是后续验证器。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Candidate flows are verified in two settings: answering without $Z_s$, and answering with $Z_s$ plus zoomed evidence. Trivial samples and samples with unreliable flows are rejected. The remaining items are split between the cold-start and RFT sets according to how much the synthetic flow improves verifier success.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 候选感知流在两种设置下接受验证：不提供 $Z_s$ 直接回答，以及提供 $Z_s$ 和放大证据后回答。过于简单的样本和感知流不可靠的样本会被删除；其余样本根据合成流对验证器成功率的提升幅度，被分配到冷启动集或强化微调集。

### Table 1. Verification and difficulty split / 验证与难度切分

![Table 1](assets/page_005_clean_table_1.png)

**Caption:** Verifier-based filtering and difficulty-aware splitting. $k_{pass}$ is the minimum sampling budget required for a correct answer.

**Caption[CN]:** 基于验证器的过滤与难度切分。$k_{pass}$ 表示首次得到正确答案所需的最小采样预算。

**Reading note:** 冷启动集要求合成流能稳定带来帮助；强化集保留仍有探索空间的困难样本。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> For each cold-start pair $(X,Z_s)$, the policy is initialized by minimizing cross-entropy between $p_\theta(Z\mid X)$ and the synthetic flow. This teaches the model to produce perceptual trajectories that are useful for later reasoning before reinforcement learning begins.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 对每个冷启动样本 $(X,Z_s)$，策略通过最小化 $p_\theta(Z\mid X)$ 与合成流之间的交叉熵进行初始化。这样，模型在进入强化学习前先学会生成对后续推理有帮助的感知轨迹。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The cold-start statistics show that samples contain one to seven or more RoIs. As RoI count increases, planning-state length stays comparatively stable, whereas the perceptual-state portion grows substantially. This indicates that additional regions mainly expand grounded evidence rather than global planning text.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 冷启动统计显示，每个样本包含一个到七个或更多区域。随着区域数量增加，规划状态长度相对稳定，而感知状态部分显著增长。这说明额外区域主要扩展视觉证据，而不是增加全局规划文字。

### 3.2 Variational Reinforcement Fine-tuning / 变分强化微调

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Heuristic flow synthesis cannot determine a unique golden flow for every sample. Variational RFT therefore optimizes a distribution over flows. For any terminated prefix $z_{0:i}^{\top}$, the scalar flow is defined from the shaped reward and the policy's termination probability; SubTB then compares every pair of prefixes within sampled trajectories.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 启发式感知流合成无法为每个样本确定唯一黄金轨迹，因此变分强化微调优化的是感知流分布。对任意终止前缀 $z_{0:i}^{\top}$，标量流量由塑形奖励和策略终止概率共同定义；子轨迹平衡目标再比较采样轨迹中的任意前缀对。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The multi-dimensional reward has two components. The quality term multiplies positive-to-negative caption likelihood ratios, where the positive likelihood conditions on the cropped RoI and the negative likelihood conditions on the complementary image region. The efficacy term is the reward model likelihood of the target answer given the perceptual-flow prefix.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 多维奖励包含两个部分。质量项累乘证据描述的正负似然比：正似然以裁剪区域为条件，负似然以区域外的互补图像为条件。效用项则是奖励模型在给定感知流前缀后对目标答案赋予的似然。

$$
R(z_{0:k}^{\top})=
\left[\prod_{i=1}^{k}\frac{p_\phi(c_i\mid I_{r_i})}{p_\phi(c_i\mid I\setminus I_{r_i})}\right]
p_\phi(Y\mid z_{0:k}^{\top},X).
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Maximizing the contrastive caption term pulls the policy-induced caption distribution toward a privileged teacher conditioned on zoomed evidence and pushes it away from a noisy distribution conditioned on less informative context. This encourages visually specific descriptions and suppresses generic language-prior captions or reward hacking.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 最大化对比式描述项，会让策略产生的描述分布接近以放大证据为条件的特权教师，同时远离以低信息背景为条件的噪声分布。这样可以鼓励视觉特异描述，并压制由语言先验或奖励投机产生的泛化表述。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The efficacy term measures how much information the sampled flow contributes to the target response. For a fixed $(X,Y)$ and frozen reward model, $\log p_\phi(Y\mid X)$ is constant, so maximizing $\log p_\phi(Y\mid z_{0:k}^{\top},X)$ favors flows that make the correct answer more likely.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 效用项衡量采样感知流对目标回答提供了多少信息。对于固定的 $(X,Y)$ 和冻结奖励模型，$\log p_\phi(Y\mid X)$ 是常数，因此最大化 $\log p_\phi(Y\mid z_{0:k}^{\top},X)$ 会偏好真正提高正确答案似然的感知流。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Utility alone can encourage excessive exploration outside valid visual support. PFlowNet defines a symmetrized Chamfer-IoU distance between predicted and expert RoI sets, then constructs an $\epsilon$-vicinity around the expert evidence. Trajectories outside this vicinity receive an exponential penalty with intensity $\lambda$.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 仅优化效用可能鼓励模型探索到有效视觉支持之外。PFlowNet 在预测区域集与专家区域集之间定义对称 Chamfer-IoU 距离，并以专家证据为中心构造 $\epsilon$ 邻域。越出该邻域的轨迹会受到强度为 $\lambda$ 的指数惩罚。

$$
\omega_\lambda(z_{0:k},E)=
\exp\left[-\lambda\,\mathbf{1}\left(d_{IoU}(r_{1:k},E)>\epsilon\right)\right],
\qquad R_\lambda=R\,\omega_\lambda.
$$

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Unlike strict alignment, vicinal shaping acts only when a trajectory leaves the expert neighborhood. It therefore retains a reliability prior while permitting controlled exploration of regions that may contain more reasoning context than the expert box.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 与严格对齐不同，邻域塑形只在轨迹离开专家邻域时发挥作用。它既保留视觉可靠性先验，也允许模型在受控范围内探索比专家框包含更多推理上下文的区域。

### 3.3 Theoretical Analysis / 理论分析

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The analysis defines valid support $S_V$ around golden evidence $G$, an expert vicinity $B_\epsilon(E)$, their posterior masses $s_V$ and $s_B$, and coverage ratio $q=s_B/s_V$. A $\lambda$-shaped posterior reweights trajectories inside and outside the expert vicinity with normalizer $Z_\lambda=s_B+e^{-\lambda}(1-s_B)$.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 理论分析围绕理想证据 $G$ 定义有效支持集 $S_V$，围绕专家证据定义邻域 $B_\epsilon(E)$，并记两者的后验质量为 $s_V$ 与 $s_B$、覆盖率为 $q=s_B/s_V$。经 $\lambda$ 塑形的后验对专家邻域内外轨迹重新加权，归一化常数为 $Z_\lambda=s_B+e^{-\lambda}(1-s_B)$。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Theorem 3.1 bounds the total-variation distance between the optimized policy and the ideal valid posterior under assumptions of support regularity, model expressiveness, and global optimization. As $\lambda\rightarrow0$, geometric constraints vanish and the bound approaches the MLE regime. As $\lambda\rightarrow\infty$, the method collapses toward expert-guided RLVR and becomes limited by expert bias.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 定理 3.1 在支持集规则性、模型表达能力与全局优化等假设下，给出优化策略与理想有效后验之间的总变差距离上界。当 $\lambda\rightarrow0$ 时，几何约束消失，上界退化到最大似然情形；当 $\lambda\rightarrow\infty$ 时，方法趋向专家引导的强化学习，其上限受专家偏差限制。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The radius $\epsilon$ controls expert-vicinity coverage. A radius that is too small makes the geometric signal uninformative, whereas enlarging it inside valid support improves coverage and tightens the bound. Once the vicinity extends beyond valid support, it can include invalid trajectories and weaken the guidance.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 半径 $\epsilon$ 控制专家邻域的覆盖范围。半径过小时，几何信号缺乏信息；只要邻域仍位于有效支持内，增大半径就能提高覆盖并收紧上界。一旦邻域越出有效支持，它也会纳入无效轨迹，从而削弱引导。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Theorem 3.4 states that, for a valid radius, there exists a shaping intensity $\lambda^*$ whose idealized bound is no worse than either limiting baseline. The paper interprets this as a guaranteed improvement over standard MLE and expert-guided RLVR when all stated assumptions hold.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 定理 3.4 表明：对于有效半径，存在塑形强度 $\lambda^*$，使理想化上界不劣于两个极端基线。论文把它解释为：在所有所列假设成立时，PFlowNet 相对标准最大似然和专家引导强化学习具有保证改进。

## 4. Experiment / 实验

### 4.1 Main Results / 主结果

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> PFlowNet is initialized from Qwen3-VL-8B and evaluated against representative baselines on general-purpose and fine-grained visual tasks. On TreeBench it improves the base model by 10.4 percentage points, and on MME-RealWorld-Lite by 18.4 points. The gains are especially pronounced on reasoning-heavy subsets.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> PFlowNet 以 Qwen3-VL-8B 初始化，并在通用与细粒度视觉任务上与代表性基线比较。它在 TreeBench 上比基座提高 10.4 个百分点，在 MME-RealWorld-Lite 上提高 18.4 个百分点；推理密集子集上的增益尤其明显。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> PFlowNet reaches 55.3 overall on TreeBench and 67.0 on MME-RealWorld-Lite, outperforming the nearest competing methods by 5.3 and 12.6 points respectively. It obtains the best result on 17 of 19 reported subtasks, suggesting that the improvement is not confined to a single question type.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> PFlowNet 在 TreeBench 上达到 55.3，在 MME-RealWorld-Lite 上达到 67.0，分别领先最近竞争方法 5.3 和 12.6 个百分点。在论文报告的 19 个子任务中，它有 17 个取得最佳结果，说明增益并非只集中于一种题型。

### Table 2. General-purpose benchmarks / 通用视觉基准

![Table 2](assets/page_008_clean_table_2.png)

**Caption:** Comparison on TreeBench and MME-RealWorld-Lite.

**Caption[CN]:** TreeBench 与 MME-RealWorld-Lite 上的比较。

**Reading note:** 表中最值得关注的是推理类子任务的增益，以及 PFlowNet 同时超过严格落地强化方法和多轮代理方法。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> On fine-grained tasks, PFlowNet sets a new reported result of 90.6 on V* Bench. It also scores 80.4 and 76.9 on HR-Bench 4K and 8K, and 95.1 and 61.8 on ScreenSpot v2 and ScreenSpot Pro. These tasks test visual search, high-resolution understanding, and GUI grounding rather than only general question answering.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在细粒度任务上，PFlowNet 在 V* Bench 达到论文所报告的新最佳结果 90.6。它在 HR-Bench 4K 与 8K 上分别达到 80.4 和 76.9，在 ScreenSpot v2 与 ScreenSpot Pro 上分别达到 95.1 和 61.8。这些任务覆盖视觉搜索、高分辨率理解和图形界面定位，而不只是通用问答。

### Table 3. Fine-grained visual tasks / 细粒度视觉任务

![Table 3](assets/page_009_fig_table_3.png)

**Caption:** Performance on visual search, high-resolution VQA, and GUI grounding.

**Caption[CN]:** 视觉搜索、高分辨率问答与图形界面定位任务上的性能。

**Reading note:** 不同评测对“区域”的定义不同，但 PFlowNet 的结构化感知流在三类任务上都能产生收益。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The authors compare performance, context length, and latency with TreeVGR, DeepEyesV2, and Thyme. PFlowNet achieves a favorable performance-efficiency trade-off because perceptual behavior is internalized in a structured two-stage generation rather than repeatedly invoking external tools.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 作者进一步比较 PFlowNet、TreeVGR、DeepEyesV2 与 Thyme 的性能、上下文长度和时延。PFlowNet 取得较好的性能—效率折中，因为感知行为被内化到结构化两阶段生成中，而不需要反复调用外部工具。

### Figure 6. Performance-efficiency trade-off / 性能—效率折中

![Figure 6](assets/page_009_fig_figure_6.png)

**Caption:** Performance-efficiency trade-offs among Qwen3-VL-8B, PFlowNet, TreeVGR, DeepEyesV2, and Thyme.

**Caption[CN]:** Qwen3-VL-8B、PFlowNet、TreeVGR、DeepEyesV2 与 Thyme 的性能—效率折中。

**Reading note:** 该图支持“单位推理预算更有效”，但不同框架仍可能受实现、后端和硬件配置影响。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Pass@$k$ curves show that PFlowNet continues to improve as the number of sampled responses rises from 1 to 8. TreeVGR grows more slowly, which the authors attribute to perceptual mode collapse near expert trajectories. Variational training appears to preserve multiple valid visual paths that can be exploited at test time.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> Pass@$k$ 曲线显示，当采样回答数从 1 增加到 8 时，PFlowNet 仍持续提升。TreeVGR 的增长更慢，作者把它归因于专家轨迹附近的感知模式坍缩。变分训练似乎保留了多条有效视觉路径，因而能在测试时利用额外采样预算。

### Figure 7. Test-time scaling / 测试时扩展

![Figure 7](assets/page_010_fig_figure_7.png)

**Caption:** Pass@$k$ curves for different methods with $k\in[1,8]$.

**Caption[CN]:** 不同方法在 $k\in[1,8]$ 时的 Pass@$k$ 曲线。

**Reading note:** 曲线衡量“多次采样后至少一次正确”，不能直接替代单次推理吞吐量。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Qualitative examples show that PFlowNet tends to choose regions that are precise enough to anchor the answer while retaining contextual relations. Ungrounded models can rely on language priors, and rigidly grounded models can miss evidence outside an overly narrow box.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 定性示例表明，PFlowNet 往往选择既足以锚定答案、又保留关系上下文的区域。未落地模型容易依赖语言先验，而刚性落地模型可能遗漏过窄框之外的关键证据。

### Figure 8. Qualitative comparison / 定性比较

![Figure 8](Reasoning/Train/Perceptual%20Flow%20Network%20for%20Visually%20Grounded%20Reasoning/assets/page_010_fig_figure_8.png)

**Caption:** Qualitative comparison of visual reasoning across different methods.

**Caption[CN]:** 不同方法的视觉推理定性比较。

**Reading note:** 图中同时呈现语言偏置、证据遗漏与 PFlowNet 的区域—描述链条，适合与 Table 4 的结构消融一起阅读。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> RoI statistics reveal that PFlowNet often uses fewer output characters than the synthetic cold-start flows. On V* and MME-RealWorld-Lite, the model reduces the character count substantially after RFT while retaining task performance, suggesting that reinforcement learning compresses the flow toward task-relevant evidence.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 区域统计显示，PFlowNet 的输出通常比冷启动合成流更短。在 V* 与 MME-RealWorld-Lite 上，强化微调后字符数显著下降，同时仍保持任务性能，说明强化学习把感知流压缩到与任务更相关的证据上。

### Figure 9. RoI and output-length statistics / 区域与输出长度统计

![Figure 9](assets/page_010_fig_figure_9.png)

**Caption:** RoI distributions and character-level output length across benchmark types.

**Caption[CN]:** 不同基准上的区域数量分布与字符级输出长度。

**Reading note:** 图中“after RFT”比合成流更短，支持变分强化微调不仅加分，也在压缩冗余感知文本。

### 4.2 Ablation Study / 消融实验

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Supervised fine-tuning alone improves TreeBench, V*, and MME-RW from 44.9/77.5/46.0 to 48.3/83.7/54.2. The complete method reaches 55.3/90.6/67.0, showing that synthetic flows provide a useful start but variational RFT supplies a large additional gain.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 仅监督微调就把 TreeBench、V* 和 MME-RW 从 44.9/77.5/46.0 提高到 48.3/83.7/54.2。完整方法达到 55.3/90.6/67.0，说明合成感知流提供了有效起点，而变分强化微调带来更大增益。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Removing the explicit perceptual flow causes a severe drop to 49.2 on TreeBench, 83.8 on V*, and 52.1 on MME-RW, whereas adding only external RoI visual features yields limited benefit. The text flow is therefore a semantic anchor that connects region selection, evidence description, and answer generation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 去掉显式感知流后，TreeBench、V* 与 MME-RW 分别降至 49.2、83.8 和 52.1，而仅增加外部区域视觉特征的收益有限。因此，文本感知流是连接区域选择、证据描述与答案生成的语义锚点。

### Table 4. Training and reward ablations / 训练与奖励消融

![Table 4](assets/page_011_fig_table_4.png)

**Caption:** Ablation of the training recipe, reward design, geometric shaping, perceptual flow, and RoI features.

**Caption[CN]:** 对训练配方、奖励设计、几何塑形、感知流与区域特征的消融。

**Reading note:** 最关键一行是去掉感知流：性能下降远大于单独去掉区域特征，说明方法不是普通的 zoom-in 模块。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The geometric-shaping sweep shows that both overly weak and overly strong shaping are suboptimal. The selected configuration is $\lambda=4.5$ and $\epsilon=0.5$, matching the paper's theoretical picture of a middle regime between unconstrained MLE and rigid expert imitation.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 几何塑形扫描显示，约束过弱或过强都不是最优。论文选择 $\lambda=4.5$、$\epsilon=0.5$，与理论上处于无约束最大似然和刚性专家模仿之间的中间状态相呼应。

### Figure 10. Geometric-shaping sweep / 几何塑形扫描

![Figure 10](assets/page_011_fig_figure_10.png)

**Caption:** Ablation study on the geometric shaping scheme.

**Caption[CN]:** 邻域几何塑形的消融实验。

**Reading note:** 这张图为“受控探索”提供直接证据：邻域半径与惩罚强度都存在中间最优区间。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Cross-scale evaluation extends the recipe to Qwen3-VL 4B and 32B. Under shorter SFT and RFT schedules, both model sizes gain after supervised training and improve further after RFT. The result supports scale robustness within the same model family, although it does not establish transfer to unrelated architectures.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 跨尺度实验把同一配方扩展到 Qwen3-VL 4B 与 32B。在更短的监督和强化训练日程下，两种规模都先因监督训练提升，再因强化微调进一步提高。该结果支持同一模型家族内的尺度稳健性，但尚不能证明对不同架构家族同样有效。

### Table 5. Cross-scale gains / 跨尺度收益

![Table 5](Reasoning/Train/Perceptual%20Flow%20Network%20for%20Visually%20Grounded%20Reasoning/assets/page_011_fig_table_5.png)

**Caption:** Cross-scale gains of PFlowNet across general and fine-grained visual tasks.

**Caption[CN]:** PFlowNet 在通用与细粒度视觉任务上的跨尺度收益。

**Reading note:** 4B 与 32B 都遵循“基座 < SFT < RFT”的趋势，但附录说明它们使用了更短训练日程。

## 5. Related Work / 相关工作

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Agentic frameworks enhance LVLMs through multi-turn image manipulation, code execution, or sandboxed tools. Methods such as Thyme, Visual Sketchpad, VaCoT, and DeepEyes can acquire evidence dynamically, but tool use increases latency and creates a trade-off with intrinsic reasoning capability.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 代理式框架通过多轮图像操作、代码执行或沙箱工具增强大型视觉语言模型。Thyme、Visual Sketchpad、VaCoT 与 DeepEyes 等方法能够动态获取证据，但工具调用会增加时延，并可能与模型自身推理能力形成权衡。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Training-free visual-search methods such as V*, DyFo, and DeepScan use zooming, search, or region refinement without retraining the base model. They are flexible at inference time but can require repeated model calls and do not directly learn a reusable distribution over perceptual trajectories.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> V*、DyFo 与 DeepScan 等免训练视觉搜索方法在不重新训练基座模型的情况下使用缩放、搜索或区域细化。它们在推理时较灵活，但通常需要重复调用模型，也不会直接学习可复用的感知轨迹分布。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Grounded RLVR methods represent perception through boxes or points and optimize answer accuracy together with geometric consistency. The authors argue that rigid alignment to sparse, biased expert priors can compromise reasoning and overlook semantic coherence between visual rationales and surrounding text. PFlowNet addresses this with multi-dimensional reward and vicinal shaping.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 视觉落地可验证奖励强化学习方法用框或点表示感知，并联合优化答案准确率与几何一致性。作者认为，刚性对齐稀疏且有偏的专家先验可能损害推理，并忽视视觉依据与周围文本之间的语义连贯性。PFlowNet 用多维奖励和邻域塑形缓解这一问题。

### Figure 11. Framework comparison / 框架比较

![Figure 11](assets/page_012_fig_figure_11.png)

**Caption:** Agentic frameworks use multi-turn tools; grounded RLVR integrates perception and reasoning in one turn; PFlowNet decouples perception and reasoning through a two-stage perceptual flow.

**Caption[CN]:** 代理框架依赖多轮工具；视觉落地强化学习在单轮中混合感知与推理；PFlowNet 则通过两阶段感知流将二者解耦。

**Reading note:** 三种范式分别强调外部工具、单轮严格轨迹和训练内化的自条件轨迹。

## 6. Conclusion and Limitations / 结论与局限

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> PFlowNet uses structured perceptual flows to support high-quality and interpretable visual reasoning. Its reinforcement fine-tuning combines a task-aware reward with vicinal geometric shaping, allowing LVLMs to explore reasoning-oriented yet valid perceptual behaviors. Experiments support gains on both general-purpose and fine-grained tasks.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> PFlowNet 使用结构化感知流实现高质量且可解释的视觉推理。其强化微调把任务感知奖励与邻域几何塑形结合，使大型视觉语言模型能够探索面向推理且仍然有效的感知行为。实验支持它在通用和细粒度任务上的收益。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The theoretical claims rest on idealized assumptions A.1 and A.2 and on regularity of the valid support, which may not hold exactly in practice. The optimal $\epsilon$ and $\lambda$ can vary across models and domains, so the bound is best interpreted as a qualitative guide rather than a direct predictor of empirical performance.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 理论结论依赖理想化假设 A.1、A.2 以及有效支持集的规则性，这些条件在实践中未必严格成立。最优 $\epsilon$ 与 $\lambda$ 也可能随模型和领域变化，因此理论上界更适合作为定性指南，而非实际性能的直接预测器。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> PFlowNet currently lacks adaptive perception and uses the same structured format for questions of different type and difficulty. This format helps difficult visual reasoning, but can add overhead to simple or STEM-oriented questions where evidence is already salient. It can also shift model capacity from direct problem solving toward following the prescribed structure.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> PFlowNet 目前缺少自适应感知，对不同类型和难度的问题都使用相同结构。该格式有利于复杂视觉推理，但对证据已经明显的简单题或部分理工题会增加额外开销，也可能把部分模型容量从直接求解转移到遵循规定结构。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> A future system should dynamically adjust whether and how deeply to invoke perception according to question difficulty and task context. The paper also points readers to Appendix D.2 for representative failure cases.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 未来系统应根据问题难度和任务上下文，动态决定是否启动感知以及感知应进行多深。论文还在附录 D.2 中专门分析了代表性失败案例。

## References / 参考文献

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The bibliography contains 66 entries spanning LVLM backbones, hallucination benchmarks, visual search, grounded reinforcement learning, GUI grounding, GFlowNet/SubTB, optimization, serving, and the datasets used for training and evaluation. Bibliographic titles and author names are preserved in their original language in the source PDF.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 参考文献共 66 条，覆盖大型视觉语言模型基座、幻觉基准、视觉搜索、视觉落地强化学习、图形界面定位、GFlowNet/子轨迹平衡、优化与推理服务，以及本文训练和评测所用数据集。文献题名和作者名在源 PDF 中保留原始语言，本阅读器不对书目元数据逐条翻译。

## Appendix A. Omitted Technical Details / 附录 A：补充技术细节

### A.1 Preliminaries / 预备定义

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The appendix first formalizes variables and flow notation, then derives the SubTB objective, states the assumptions needed for tractable analysis, proves two auxiliary lemmas, and finally proves Theorems 3.1 and 3.4. The bridge is an exponentially tilted posterior $P_\lambda$: the shaped reward is proportional to it, and the ideal global policy optimum recovers it.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 附录先形式化变量与感知流记号，再推导子轨迹平衡目标，列出使分析可处理的假设，证明两个辅助引理，最后证明定理 3.1 与 3.4。核心桥梁是指数倾斜后验 $P_\lambda$：塑形奖励与它成比例，理想全局最优策略会恢复这一分布。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> A training sample is $(X,Y,E)\sim P_{data}$, where $X=\langle I,T\rangle$ is image and instruction, $Y$ is the verifier response conditioned on a synthetic flow, and $E$ is the reference RoI set. The latent flow is $Z=(z_0\rightarrow\cdots\rightarrow z_K)$, with normalized box coordinates and a terminal symbol $\top$.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 一个训练样本记为 $(X,Y,E)\sim P_{data}$，其中 $X=\langle I,T\rangle$ 是图像与指令，$Y$ 是验证器在合成感知流条件下生成的回答，$E$ 是参考区域集。潜在感知流为 $Z=(z_0\rightarrow\cdots\rightarrow z_K)$，区域坐标归一化，并使用终止符号 $\top$。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The analysis conditions on a fixed flow length for each input while allowing the geometric precision and traversal order of RoIs to vary. PFlowNet induces an autoregressive forward transition kernel over planning and perceptual states. Structural hypotheses assume a deterministic planning state, captions that depend on the image through cropped evidence, and a neutral contrastive boundary at $z_0$.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 分析对每个输入固定感知流长度，但允许区域的几何精度与遍历顺序变化。PFlowNet 在规划状态和感知状态上诱导自回归前向转移核。结构假设包括：规划状态由输入唯一决定；描述通过裁剪证据依赖图像；在 $z_0$ 处，对比项采用中性边界。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The expert vicinity $B_\epsilon(E)$ is assumed to lie inside the valid support $S_V$. Its mass $s_B$ and the valid mass $s_V$ define $q=s_B/s_V$. Shaping assigns weight 1 inside the vicinity and $e^{-\lambda}$ outside, producing normalizer $Z_\lambda=s_B+e^{-\lambda}(1-s_B)$ and target valid posterior $P_V$.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 理论假设专家邻域 $B_\epsilon(E)$ 位于有效支持集 $S_V$ 内。邻域质量 $s_B$ 与有效质量 $s_V$ 定义覆盖率 $q=s_B/s_V$。塑形在邻域内赋权 1，在邻域外赋权 $e^{-\lambda}$，从而得到归一化常数 $Z_\lambda=s_B+e^{-\lambda}(1-s_B)$ 和目标有效后验 $P_V$。

### A.2 Derivation of the Variational Objective / 变分目标推导

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The SubTB loss begins from a squared log-ratio comparing scalar flow and forward/backward transition probabilities for every sub-trajectory $z_{i:j}$. Because perceptual-flow generation forms an autoregressive tree, the backward path is deterministic and its transition probability collapses to one, while the forward transition is the product of policy token probabilities.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 子轨迹平衡损失从平方对数比开始，对每个子轨迹 $z_{i:j}$ 比较标量流量与前向、后向转移概率。由于感知流生成形成自回归树，后向路径是确定的，其转移概率退化为 1；前向转移则是策略 token 概率的乘积。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The scalar flow at state $z_k$ is instantiated as $F(z_k)=R_\lambda(z_{0:k}^{\top})/p_\theta(\top\mid z_{0:k})$. Substituting this term into all valid prefix pairs yields the paper's variational RFT objective, averaged over data and $L$ sampled perceptual flows. The construction supplies training signals to shared prefixes rather than only complete trajectories.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 状态 $z_k$ 的标量流量被定义为 $F(z_k)=R_\lambda(z_{0:k}^{\top})/p_\theta(\top\mid z_{0:k})$。把该定义代入所有有效前缀对，再对数据与 $L$ 条采样感知流取平均，就得到论文的变分强化微调目标。该构造能为共享前缀提供训练信号，而不只监督完整轨迹。

### A.3 Assumptions and Auxiliary Lemmas / 假设与辅助引理

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Assumption A.1 uses a uniform prior over admissible unordered RoI bags and over their traversal permutations. Assumption A.2 requires captions to be faithful under the cropped evidence and non-informative under the complementary context. These assumptions are analytically convenient but substantially stronger than what can be verified for a real LVLM.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 假设 A.1 对可接受的无序区域集合及其遍历排列采用均匀先验。假设 A.2 要求描述在裁剪证据条件下保持忠实，而在互补背景条件下不携带信息。这些假设便于分析，但显著强于真实大型视觉语言模型中可以验证的条件。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Lemma A.3 shows that, under A.1 and A.2, the shaped multi-dimensional reward is proportional to the tilted posterior $P_\lambda(Z\mid X,Y,E)$. The proof uses the uniform support and ordering terms to cancel constants and identifies the remaining caption likelihood, answer likelihood, and geometric weight with the posterior factorization.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 引理 A.3 证明，在 A.1 与 A.2 成立时，塑形后的多维奖励与倾斜后验 $P_\lambda(Z\mid X,Y,E)$ 成比例。证明利用均匀支持和顺序先验消去常数，并把剩余的描述似然、答案似然与几何权重对应到后验分解。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Lemma A.4 assumes an expressive policy and a global minimum with zero SubTB loss. Exact balance across every prefix pair then makes the policy probability of a complete terminated trajectory proportional to the shaped reward, and therefore proportional to $P_\lambda$.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 引理 A.4 假设策略具有充分表达能力，并达到子轨迹平衡损失为零的全局最优。此时，每个前缀对之间的精确平衡，使完整终止轨迹的策略概率与塑形奖励成比例，进而与 $P_\lambda$ 成比例。

### A.4 Proofs of the Main Theorems / 主定理证明

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Theorem 3.1 partitions trajectory space into the expert vicinity, valid support outside that vicinity, and invalid support. Integrating the absolute density difference over these three regions yields the total-variation bound. The proof explicitly notes that an actual policy cannot analytically condition on $Y$ and $E$ at inference; equality with $P_\lambda$ characterizes an ideal optimum for a training instance.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 定理 3.1 把轨迹空间分为专家邻域、邻域外的有效支持和无效支持三部分。在这三个区域上积分密度绝对差，就得到总变差上界。证明还明确指出，真实推理策略无法解析地依赖 $Y$ 与 $E$；与 $P_\lambda$ 的相等只刻画单个训练实例上的理想最优状态。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Theorem 3.4 studies the bound as a function of $u=e^{-\lambda}$. The continuous bound connects the MLE endpoint and the expert-guided endpoint, and an interior choice can be no worse than the smaller endpoint. For fixed calibrated intensity, increasing valid expert coverage $q$ strictly tightens the bound as long as $B_\epsilon(E)\subseteq S_V$ remains true.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 定理 3.4 把上界视为 $u=e^{-\lambda}$ 的函数。连续上界连接最大似然端点与专家引导端点，内部取值可以不劣于两端中较小者。对固定且校准后的强度，只要 $B_\epsilon(E)\subseteq S_V$ 仍成立，提高有效专家覆盖率 $q$ 就会严格收紧上界。

## Appendix B. Implementation Details / 附录 B：实现细节

### B.1 Dataset / 数据集

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The training corpus aggregates LLaVA official training data, VGR, ArxivQA, VLM-R3, and ThinkLite-VL. Filtering by difficulty, task type, and evidence distribution leaves 95k visual question-answer pairs. Of these, 53k are processed for flow generation; 45k high-quality flows are retained for cold start and the remaining 42k samples are used for variational RFT.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 训练语料汇集 LLaVA 官方训练集、VGR、ArxivQA、VLM-R3 与 ThinkLite-VL。按难度、任务类型和证据分布过滤后得到 95k 个视觉问答样本。其中 53k 个进入感知流生成，45k 个高质量感知流用于冷启动，其余 42k 个样本用于变分强化微调。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> To reduce contamination risk, the authors check question-answer overlap between training data and 15 evaluation benchmarks and report zero overlap. This test addresses literal or near-literal duplication, but it does not by itself rule out broader visual or semantic similarity.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 为降低数据污染风险，作者检查训练数据与 15 个评测基准之间的问答文本重叠，并报告零重叠。该检查能够发现直接或近似文本重复，但本身不能排除更广泛的视觉或语义相似性。

### B.2 Training Recipe / 训练配方

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Supervised fine-tuning starts from Qwen3-VL-8B-Instruct and runs for three epochs on 16 H200 GPUs, with global batch size 256 and peak learning rate $10^{-5}$. Variational RFT runs for five epochs on 16 H200 GPUs using vLLM, TRL, hybrid data parallelism, and ZeRO-3.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 监督微调从 Qwen3-VL-8B-Instruct 出发，在 16 张 H200 上训练 3 个周期，全局批量为 256，峰值学习率为 $10^{-5}$。变分强化微调在 16 张 H200 上训练 5 个周期，使用 vLLM、TRL、混合数据并行与 ZeRO-3。

### Table 6. Variational RFT hyperparameters / 变分强化微调超参数

![Table 6](assets/page_028_clean_table_6.png)

**Caption:** Hyperparameters for variational reinforcement fine-tuning.

**Caption[CN]:** 变分强化微调的超参数。

**Reading note:** 关键配置包括 $\lambda=4.5$、$\epsilon=0.5$、每样本 8 条探索轨迹、最大感知流长度 4096，以及响应级全局批量 1024。

### B.3 Exploration and Exploitation / 探索与利用

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Rollouts use a temperature schedule rather than a single fixed temperature. Multiple trajectories are sampled for each input, and the geometry term restricts unsafe exploration while the task reward favors useful alternatives. This makes exploration a property of the learned flow distribution rather than only a decoding-time trick.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 轨迹采样采用温度调度，而不是单一固定温度。每个输入采样多条轨迹，几何项限制不可靠探索，任务奖励则偏好有用的替代路径。因此，探索成为学习到的感知流分布的性质，而不仅是解码时技巧。

### B.4 Reward Calculation / 奖励计算

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Directly evaluating every terminated prefix would repeat large amounts of computation. The implementation packs shared flow prefixes and assigns explicit position IDs and attention masks so transition probabilities and termination probabilities for many prefixes can be obtained in parallel.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 若逐个评估每个终止前缀，会产生大量重复计算。实现把共享感知流前缀打包，并显式设置位置编号和注意力掩码，从而并行获得多个前缀的转移概率与终止概率。

### Figure 12. Parallel terminal probabilities / 并行计算终止概率

![Figure 12](assets/page_029_fig_figure_12.png)

**Caption:** Parallel computation of $\log p_\theta(\top\mid z_{0:i})$ with explicit position IDs and attention masks.

**Caption[CN]:** 使用显式位置编号与注意力掩码，并行计算 $\log p_\theta(\top\mid z_{0:i})$。

**Reading note:** 不同终止位置共享同一次前向计算中的前缀 token，减少对子轨迹逐个运行模型的开销。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Efficacy rewards are also parallelized. Each flow prefix is paired with the target answer under an attention pattern that prevents one branch from leaking future states into another. The reward model can then score $\log p_\phi(Y\mid X,z_{0:i},\top)$ for all prefixes in a packed batch.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 推理效用奖励也采用并行计算。每个感知流前缀与目标答案配对，并通过注意力模式阻止一个分支泄露另一分支的未来状态。奖励模型由此可在一个打包批次中计算所有前缀的 $\log p_\phi(Y\mid X,z_{0:i},\top)$。

### Figure 13. Parallel efficacy rewards / 并行计算效用奖励

![Figure 13](assets/page_030_fig_figure_13.png)

**Caption:** Parallel computation of efficacy reward with an explicit attention mask.

**Caption[CN]:** 使用显式注意力掩码并行计算推理效用奖励。

**Reading note:** 黑色边界分隔感知流与答案 token；每个答案分支只读取对应前缀。

### B.5 Prompt / 提示模板

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The system prompt requires a fixed four-part behavior: analyze the question, localize one or more regions with normalized coordinates, describe visual evidence for each region, and then reason to the final answer. During inference, generation stops at the end of the localization block, RoIs are parsed and re-encoded, and the same prompt is used for continued answer generation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 系统提示要求固定的四部分行为：分析问题；用归一化坐标定位一个或多个区域；描述每个区域的视觉证据；最后推理得到答案。推理时，生成在定位块结束处暂停，系统解析并重新编码区域，再使用同一提示继续生成答案。

## Appendix C. Evaluation Details / 附录 C：评测细节

### C.1 Benchmarks and Metrics / 基准与指标

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> TreeBench evaluates traceable visual grounding and reasoning across multiple categories. MME-RealWorld-Lite targets high-resolution real-world scenes and contains perception-heavy and reasoning-heavy subsets. V* Bench measures guided visual search and fine-grained attribute or relation understanding.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> TreeBench 评估多类别下可追踪的视觉落地与推理。MME-RealWorld-Lite 面向高分辨率真实场景，包含感知密集与推理密集子集。V* Bench 衡量引导式视觉搜索，以及细粒度属性和关系理解。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> HR-Bench evaluates high-resolution visual question answering at 4K and 8K settings. ScreenSpot v2 and ScreenSpot Pro evaluate GUI grounding, where a predicted point or region must fall inside the target interface element. Together these benchmarks test whether the same flow representation transfers across different evidence granularities.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> HR-Bench 在 4K 与 8K 设置下评估高分辨率视觉问答。ScreenSpot v2 与 ScreenSpot Pro 评估图形界面定位，预测点或区域必须落在目标界面元素内。它们共同检验同一感知流表征能否迁移到不同证据粒度。

### C.2 Baselines / 基线

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Baselines include instruction-tuned open LVLMs at several scales and frontier proprietary systems. Agentic baselines use multi-turn planning, zooming, code, or sandboxed tools. Grounded RLVR baselines train spatial tokens with answer and localization rewards, while GUI-specific systems predict interaction targets directly from screenshots.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 基线包括多个规模的开源指令微调视觉语言模型和前沿闭源系统。代理式基线使用多轮规划、缩放、代码或沙箱工具；视觉落地强化学习基线联合答案与定位奖励训练空间 token；图形界面专用系统则直接从截图预测交互目标。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Representative comparisons include TreeVGR, Pixel-Reasoner, ZoomRefine, DyFo, Thyme, DeepEyes/DeepEyesV2, VaCoT, SeeClick, OS-Atlas, UGround, and UI-TARS. The appendix describes what type of external perception, training objective, or GUI supervision each baseline uses.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 代表性比较包括 TreeVGR、Pixel-Reasoner、ZoomRefine、DyFo、Thyme、DeepEyes/DeepEyesV2、VaCoT、SeeClick、OS-Atlas、UGround 与 UI-TARS。附录说明了各基线采用的外部感知方式、训练目标或图形界面监督类型。

### C.3 Evaluation Protocol / 评测协议

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Baselines are reproduced with their official evaluation pipelines and default configurations. For performance-efficiency and scaling analyses, TreeVGR and Thyme are migrated to VLMEvalKit with the vLLM backend; DeepEyes already uses this stack. All latency and memory measurements are run on an NVIDIA H200 to reduce infrastructure differences.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 基线使用官方评测流水线与默认配置复现。为进行性能—效率与扩展分析，TreeVGR 和 Thyme 被迁移到使用 vLLM 后端的 VLMEvalKit；DeepEyes 原本就使用该技术栈。所有时延与内存测量均在 NVIDIA H200 上运行，以减少基础设施差异。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Standard evaluation uses greedy decoding. Test-time scaling uses $k$ independent stochastic responses with temperature 1.0 and top-$p$ 0.95. PFlowNet stops when the perceptual-flow end token appears, parses the RoIs, extracts fine-grained visual features, concatenates them with the initial flow, and resumes generation under the same system prompt.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 标准评测使用贪心解码。测试时扩展为每个样本生成 $k$ 个独立随机回答，温度为 1.0，top-$p$ 为 0.95。PFlowNet 在感知流结束 token 出现时暂停，解析区域并提取细粒度视觉特征，再把它们与初始感知流拼接，在同一系统提示下继续生成。

## Appendix D. Additional Qualitative Analysis / 附录 D：补充定性分析

### D.1 Test-Time Scaling Behaviors / 测试时扩展行为

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Under repeated sampling, TreeVGR's predicted boxes overlap almost completely across multiple reasoning paths. The appendix interprets this as mode collapse around expert trajectories: additional computation does not produce genuinely different visual hypotheses, and an erroneous region can be repeated without self-correction.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在重复采样下，TreeVGR 在多条推理路径中预测的框几乎完全重叠。附录把这解释为专家轨迹附近的模式坍缩：增加计算并不会产生真正不同的视觉假设，错误区域也会在缺少自我修正的情况下反复出现。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> PFlowNet produces more diverse RoIs while remaining near reliable evidence. This qualitative behavior is consistent with the rising Pass@$k$ curve: variational optimization allocates probability to multiple valid paths rather than forcing all samples to imitate a single expert trajectory.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> PFlowNet 在保持接近可靠证据的同时产生更多样的区域。这一定性行为与持续上升的 Pass@$k$ 曲线一致：变分优化把概率分配给多条有效路径，而不是迫使所有样本模仿单一专家轨迹。

### Figure 14. Grounding diversity under scaling / 扩展采样下的落地区域多样性

![Figure 14](assets/page_033_fig_figure_14.png)

**Caption:** TreeVGR shows severe mode collapse, whereas PFlowNet explores diverse but reliable regions across four benchmarks.

**Caption[CN]:** TreeVGR 表现出严重模式坍缩；PFlowNet 在四个基准上探索多样但仍可靠的区域。

**Reading note:** 蓝框高度重合，红框在目标附近形成多样覆盖；该图为 Figure 7 的 Pass@$k$ 差异提供内部机制解释。

### D.2 Failure Case Analysis / 失败案例分析

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The first failure is a trade-off between geometric reliability and fine-grained counting. Because PFlowNet is rewarded for diverse and reliable boxes, it can merge adjacent objects to preserve context. In counting tasks, the subsequent reasoning can then be primed by the number or grouping of boxes and produce an incorrect count.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 第一类失败来自几何可靠性与细粒度计数之间的权衡。由于 PFlowNet 被鼓励输出多样且可靠的区域，它有时会合并相邻对象以保留上下文。在计数任务中，后续推理可能受到框数量或分组方式的启动效应影响，从而给出错误计数。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The second failure concerns the planning state, which has no direct supervision and is optimized only indirectly through sub-flow efficacy. In difficult or out-of-distribution cases, incorrect decomposition of required evidence propagates into confusing localization and wrong reasoning. Adding more fine-grained visual features cannot fully correct this because the textual flow strongly primes the answer stage.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 第二类失败涉及规划状态。规划状态没有直接监督，只通过子感知流的效用项被动优化。在困难或分布外场景中，对所需证据的错误分解会传播到混乱定位和错误推理。由于文本感知流会强烈启动答案阶段，单纯补充更细粒度视觉特征也无法完全修正这一问题。

### Figure 15. Counting and planning failures / 计数与规划失败

![Figure 15](assets/page_034_fig_figure_15.png)

**Caption:** Additional qualitative results highlighting a tree-counting error and a planning/decomposition error.

**Caption[CN]:** 补充定性结果，展示树木计数错误与规划分解错误。

**Reading note:** 上例定位到了三个区域却漏计对象；下例在规划阶段误解“steps”，说明错误可在区域裁剪前就发生。

### D.3 More Examples / 更多示例

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In a road-counting example, the base model relies on the most salient paved surface and TreeVGR localizes only one path. PFlowNet explicitly searches both foreground and background and recovers two distinct road regions, leading to the correct answer.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在道路计数示例中，基座模型依赖最显眼的铺装表面，TreeVGR 也只定位一条道路。PFlowNet 明确搜索前景与背景，找到两个不同道路区域，因此得到正确答案。

### Figure 16. Recovering missing road evidence / 找回遗漏的道路证据

![Figure 16](assets/page_035_fig_figure_16.png)

**Caption:** PFlowNet identifies both foreground and background road evidence that other methods miss.

**Caption[CN]:** PFlowNet 找到其他方法遗漏的前景与背景道路证据。

**Reading note:** 该例强调上下文扩展的益处：第二条道路远离最显眼的前景路径。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In a deliberately misleading map, world knowledge says the Rocky Mountains are in North America, but the diagram places the label inside the landmass marked Asia. The base model and TreeVGR follow geographic priors; PFlowNet grounds its answer in the diagram and follows the benchmark's visual evidence.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在一张故意误导的地图中，常识认为落基山脉位于北美，但图示把相应标签画在标有亚洲的陆块内。基座模型和 TreeVGR 遵循地理常识；PFlowNet 则依据图中证据回答，符合该基准的视觉设定。

### Figure 17. Visual evidence versus world knowledge / 视觉证据与世界知识

![Figure 17](assets/page_036_fig_figure_17.png)

**Caption:** PFlowNet follows the diagram's internal evidence while other models default to world knowledge.

**Caption[CN]:** PFlowNet 遵循图示内部证据，而其他模型默认采用世界知识。

**Reading note:** 这是视觉落地任务的典型冲突：目标不是纠正图示，而是根据图示本身作答。

## 术语表

| English term | 统一译法 | 说明 |
|---|---|---|
| Perceptual Flow | 感知流 | 由规划状态与若干区域—描述状态组成的结构化潜在轨迹 |
| Planning State | 规划状态 | 分解问题并提出候选视觉证据的文本状态 $z_0$ |
| Perceptual State | 感知状态 | 区域 $r_k$ 与证据描述 $c_k$ 的组合 |
| Visually Grounded Reasoning | 视觉落地推理 | 既回答正确，又把中间视觉依据限制在有效支持内 |
| reasoning utility | 推理效用 | 中间证据提高正确答案似然的程度 |
| geometric precision | 几何精度 | 区域与专家标注的空间一致程度 |
| Sub-Trajectory Balance | 子轨迹平衡 | 对共享前缀与子轨迹施加稠密概率流一致性约束 |
| variational RFT | 变分强化微调 | 用变分目标优化感知流分布的强化微调阶段 |
| vicinal geometric shaping | 邻域几何塑形 | 仅惩罚离开专家邻域的轨迹，而非逐框模仿 |
| Chamfer-IoU distance | Chamfer-IoU 距离 | 对两个区域集合进行双向匹配后得到的对称距离 |
| tunnel vision | 隧道视野 | 过紧区域删除推理所需上下文的现象 |
| test-time scaling | 测试时扩展 | 通过增加采样预算提高至少一次答对的概率 |

## 阅读提示

1. 本文最重要的区分是“视觉可靠性”与“推理充分性”：IoU 高只说明区域贴近标注，不保证它包含回答问题所需的全部上下文。
2. 理论结果是条件性保证。假设 A.1、A.2、支持集规则性、模型表达能力与全局最优缺一不可，不能直接理解为真实训练的无条件定理。
3. Table 4 是判断机制的核心证据。去掉文本感知流的损失远大于单独去掉区域特征，说明方法的关键是结构化语义轨迹，而不是简单裁剪图像。
4. 附录 D 的失败案例提醒：感知流具有强启动效应。错误规划或错误区域分组一旦写入流，后续加入更多像素也未必能纠正答案。
5. 这是一篇训练方法论文。其可复用部分主要是数据筛选、潜变量轨迹表征、多维奖励、邻域支持约束与共享前缀并行计算。

