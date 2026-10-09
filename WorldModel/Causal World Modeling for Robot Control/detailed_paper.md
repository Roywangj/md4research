# Causal World Modeling for Robot Control

## Metadata and source identity

| Field | Value |
|---|---|
| Title | **Causal World Modeling for Robot Control** |
| Authors | Lin Li$^{*}$; Qihang Zhang$^{*\dagger}$; Yiming Luo$^{*}$; Shuai Yang; Ruilin Wang; Fei Han; Mingrui Yu; Zelin Gao; Nan Xue; Xing Zhu; Yujun Shen; Yinghao Xu$^{\ddagger}$ |
| Author notes | $^{*}$Equal Contribution; $^{\dagger}$Project Lead; $^{\ddagger}$Corresponding Author |
| Identifier | arXiv:2601.21998v2 [cs.CV] |
| Version date | 22 Mar 2026 |
| Length | 31 PDF pages |
| Primary source | `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/ECJKCB63/Li 等 - 2026 - Causal World Modeling for Robot Control.pdf` |
| Structured extraction | `/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal World Modeling for Robot Control/.pipeline/deep_causal/causal_world_modeling_full_text.md` |
| Raw text cross-check | `/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal World Modeling for Robot Control/.pipeline/reader_causal/paper_raw.txt` |
| Project website | https://technology.robbyant.com/lingbot-va |
| GitHub | https://github.com/robbyant/lingbot-va |
| Checkpoints | https://huggingface.co/robbyant/lingbot-va |
| Reader policy | English source paragraph followed immediately by a faithful Chinese translation; formulas use Markdown math; references retain searchable original English bibliography. |

## Source coverage inventory

| Source unit | Required / present in this reader |
|---|---|
| PDF pages | **31 / 31** |
| Main sections | Abstract; 1 Introduction; 2 Preliminary; 3 Method; 4 Experiments; 5 Related Work; 6 Conclusion |
| Subsections | 2.1–2.2; 3.1–3.4; 4.1–4.5.3 |
| Figures | **10 / 10**: Fig. 1–10 |
| Main tables | **3 / 3**: Tables 1–3 |
| Supplementary tables | **7 / 7**: Tables S1–S7 |
| Total figure/table cards | **20 / 20** |
| Algorithms | **2 / 2**: Algorithms 1–2, all steps |
| Numbered equations | **13 / 13**: Eqs. (1)–(13) |
| Appendix | **Appendix A / present** |
| References | **97 / 97**, full English entries |
| Acknowledgment | Full acknowledgment present |

## Page / section index

| PDF pages | Source content |
|---|---|
| 1–2 | Title, abstract, 1 Introduction, Fig. 1 |
| 3–4 | 2 Preliminary (2.1–2.2), Eqs. (1)–(4), Fig. 2; 3.1 begins |
| 4–6 | 3.1–3.2, Eqs. (5)–(9) |
| 6–8 | 3.3, Fig. 3, Eq. (10), Algorithm 1, Eqs. (11)–(12) |
| 8–10 | 3.4, Fig. 4, Algorithm 2, Eq. (13) |
| 10–12 | 4.1–4.3.1, Figs. 5–6 |
| 13–14 | 4.3.2, Tables 1–2 |
| 14–15 | 4.4, Table 3, Fig. 7 |
| 15–17 | 4.5.1–4.5.3, Figs. 8–10 |
| 17–18 | 5 Related Work; 6 Conclusion; Acknowledgment |
| 18–23 | References [1]–[97] |
| 23–24 | Appendix A protocol and metrics |
| 25 | Table S1 |
| 26–31 | Tables S2–S7, one per page |

## Terminology ledger

| English term / literal | 中文统一译法 | Editorial decision |
|---|---|---|
| LingBot-VA | LingBot-VA | Model name unchanged |
| Vision-Language-Action (VLA) | 视觉-语言-动作（VLA） | Expand at first use |
| video-action world model | 视频-动作世界模型 | Keep “world model” as 世界模型 |
| causal world modeling | 因果世界建模 | Causality is across the temporal sequence/chunks |
| autoregressive (AR) | 自回归（AR） | Chunk-internal tokens may still be parallel |
| flow matching | 流匹配 | Preserve flow time $s$ and all symbols |
| conditional flow matching | 条件流匹配 | Preserve conditioning notation |
| inverse dynamics model (IDM) | 逆动力学模型（IDM） | Infers actions from desired visual transitions |
| Forward Dynamics Model (FDM) | 前向动力学模型（FDM） | Grounds asynchronous prediction in feedback |
| Mixture-of-Transformers (MoT/MOT) | Transformer 混合架构（MoT/MOT） | Preserve source capitalization where quoted |
| latent / latent token | 潜变量 / 潜变量 token | Keep `latent` where helpful for identifiers |
| KV cache | KV 缓存 | Identifier unchanged |
| teacher forcing | 教师强制 | Ground-truth history during training |
| Noisy History Augmentation | 噪声历史增强 | Method-module name retained on first use |
| chunk / chunk size $K$ | 分块 / 分块大小 $K$ | A chunk contains $K$ video frames and $\tau K$ actions |
| partial denoising | 部分去噪 | Inference may stop before $s=1$ for video |
| closed-loop rollout | 闭环展开 | Incorporates real observations |
| progress score (PS) | 进度分数（PS） | Partial step credit |
| success rate (SR) | 成功率（SR） | Full-trial completion |
| Easy / Hard | Easy / Hard | Benchmark split literals unchanged |
| ID / OOD | 分布内（ID）/ 分布外（OOD） | Preserve abbreviations |

---

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This work highlights that video world modeling, alongside vision-language pre-training, establishes a fresh and independent foundation for robot learning. Intuitively, video world models provide the ability to “imagine” the near future by understanding the causality between actions and visual dynamics. Inspired by this, we introduce LingBot-VA, an autoregressive diffusion framework that learns frame prediction and policy execution simultaneously. Our model features three carefully crafted designs: (1) a shared latent space, integrating vision and action tokens, driven by a Mixture-of-Transformers (MoT) architecture, (2) a closed-loop rollout mechanism, allowing for ongoing acquisition of environmental feedback with ground-truth observations, (3) an asynchronous inference pipeline, parallelizing action prediction and motor execution to support efficient control. We evaluate our model on both simulation benchmarks and real-world scenarios, where it shows significant promise in long-horizon manipulation, data efficiency in post-training, and strong generalizability to novel configurations. The code and model are made publicly available to facilitate the community.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本文强调，视频世界建模与视觉-语言预训练一道，为机器人学习建立了一种全新且独立的基础。直观而言，视频世界模型通过理解动作与视觉动态之间的因果关系，获得“想象”近期未来的能力。受此启发，我们提出 LingBot-VA：一种同时学习帧预测与策略执行的自回归扩散框架。该模型包含三项精心设计：（1）由 Transformer 混合架构（MoT）驱动、整合视觉 token 与动作 token 的共享潜变量空间；（2）闭环展开机制，利用真实观测持续获取环境反馈；（3）异步推理流水线，通过并行动作预测与电机执行来支持高效控制。我们在仿真基准和现实场景中评估该模型；结果显示，它在长时序操作、后训练数据效率以及对新配置的强泛化方面具有显著潜力。代码和模型均已公开，以促进社区研究。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Website: https://technology.robbyant.com/lingbot-va  
> Github: https://github.com/robbyant/lingbot-va  
> Checkpoints: https://huggingface.co/robbyant/lingbot-va

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 项目网站：https://technology.robbyant.com/lingbot-va  
> Github：https://github.com/robbyant/lingbot-va  
> 模型权重：https://huggingface.co/robbyant/lingbot-va

## 1 Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robotic manipulation [7, 11, 12, 34], demonstrating impressive capabilities in grounding linguistic instructions into visual perceptions across diverse objects and unstructured environments. However, beneath their apparent success lies a significant challenge: representation entanglement. Most existing VLAs adopt a feedforward paradigm that maps current observations to action sequences [17, 91], requiring a single neural network to simultaneously learn visual scene understanding, physical dynamics, and motor control from a unified supervision signal. This entanglement can create a bottleneck—the model must compress heterogeneous knowledge, ranging from high-dimensional visual semantics to low-dimensional motor commands, into a shared representation space. This often leads to limited sample efficiency and suboptimal generalization. Without explicit modeling of environmental evolution [25, 26, 82], reactive policies may rely on pattern matching rather than a principled understanding of physical dynamics.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 视觉-语言-动作（VLA）模型已成为通用机器人操作的一种有前景范式 [7, 11, 12, 34]，展现出将语言指令落地到多样物体和非结构化环境的视觉感知中的出色能力。然而，在表面成功之下存在一项重大挑战：表征纠缠。多数现有 VLA 采用把当前观测映射到动作序列的前馈范式 [17, 91]，要求单个神经网络从统一监督信号中同时学习视觉场景理解、物理动力学和运动控制。这种纠缠可能形成瓶颈——模型必须把从高维视觉语义到低维运动命令的异质知识压缩进共享表征空间。这往往导致样本效率有限、泛化并非最优。若不显式建模环境演化 [25, 26, 82]，反应式策略可能依赖模式匹配，而非对物理动力学的原则性理解。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Recent attempts to bring world modeling into robotic policies span interactive neural simulators (e.g., UniSim [86]), chunk-based video-action diffusion models (e.g., UVA [40] and UWM [97]), and offline video generators for subgoal synthesis (e.g. Gen2Act [4], Act2Goal [95]). While conceptually appealing, these approaches face three primary limitations for effective closed-loop control. First, the reactivity gap: chunk/open-loop generation often rolls out long segments without incorporating real-time feedback, making it hard to adapt to disturbances. Second, limited long-term memory: chunk-wise generation can introduce inconsistencies over long horizons when history is not persistently cached. Third, causality: bidirectional attention within a segment allows future tokens to influence past predictions, which diverges from the causal nature of physical reality where the present depends only on the past. These observations motivate an autoregressive formulation for robust closed-loop reasoning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 近期将世界建模引入机器人策略的尝试包括交互式神经模拟器（如 UniSim [86]）、分块视频-动作扩散模型（如 UVA [40] 和 UWM [97]），以及用于子目标合成的离线视频生成器（如 Gen2Act [4]、Act2Goal [95]）。这些方法在概念上颇具吸引力，但要实现有效闭环控制仍面临三项主要限制。第一，反应性缺口：分块/开环生成常常在不纳入实时反馈的情况下展开很长片段，因而难以适应扰动。第二，长期记忆有限：若历史未被持续缓存，逐块生成会在长时序中引入不一致。第三，因果性：片段内双向注意力允许未来 token 影响过去预测，这偏离了物理现实中“现在只依赖过去”的因果本质。这些观察促使我们采用自回归形式来实现稳健的闭环推理。

### Figure 1. LingBot-VA：面向机器人操作的自回归世界模型

![Figure 1](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/fig01_overview.png)

**Caption:** Figure 1. LingBot-VA : An Autoregressive World Model for Robotic Manipulation. (1) Pretraining: LingBot-VA is pretrained on diverse in-the-wild videos and robot action data, enabling strong generalization across scenes and objects. (2) Comprehensive Evaluation: We conduct extensive experiments on real-world tasks (long-horizon, deformable objects, and precision manipulation) and simulation benchmarks, significantly outperforming state-of-the-art methods including $\pi_{0.5}$. (3) Versatile Capabilities: Beyond policy learning, our model supports visual dynamics prediction and inverse dynamics inference from robot videos. (4) Emergent Properties: Our causal world modeling approach exhibits long-range temporal memory and strong few-shot adaptation ability.

**Caption[CN]:** 图 1. LingBot-VA：面向机器人操作的自回归世界模型。（1）预训练：LingBot-VA 在多样的自然场景视频和机器人动作数据上进行预训练，从而获得跨场景、跨物体的强泛化能力。（2）全面评估：我们在现实任务（长时序、可变形物体与精细操作）和仿真基准上开展广泛实验，显著优于包括 $\pi_{0.5}$ 在内的最先进方法。（3）多用途能力：除策略学习之外，模型还支持视觉动态预测以及从机器人视频进行逆动力学推断。（4）涌现性质：我们的因果世界建模方法展现出长程时间记忆与强少样本适应能力。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> We propose LingBot-VA, an autoregressive diffusion world model that addresses these limitations through a unified video-action framework. Unlike autoregressive language models that predict discrete tokens, our model operates in a continuous latent space via flow matching [46, 50], autoregressively generating chunks of video and action representations through iterative denoising. While our approach conceptually separates visual dynamics prediction and action decoding [22, 27], the key architectural insight is to interleave video and action tokens into a single autoregressive sequence. Both modalities are jointly processed through a Mixture-of-Transformers (MoT) architecture [43] with shared attention. Within this unified autoregressive generation process, latent imagination and action inference occur jointly: at each autoregressive step, the model generates predicted future visual states through iterative denoising while simultaneously decoding the corresponding actions, allowing both streams to mutually condition on one another. This integration, built upon a large-scale pretrained video diffusion backbone [79], offers several advantages: (i) Reactive AR loop: because video and action tokens form a unified sequence, each autoregressive step allows the system to recalibrate based on the latest real-world observation, enabling timely adjustments to both the predicted future and motor commands; (ii) Persistent context through KV-cache: the cached key-value pairs preserve the interleaved video-action trajectory, providing a rich context that helps mitigate temporal drift; (iii) Causal consistency: causal attention masking over the unified sequence ensures that both predicted visual states and action commands are governed by preceding states, respecting the temporal arrow of physical dynamics. By incorporating real-world observations at each step, this formulation helps mitigate the distribution drift that often affects open-loop methods in long-horizon tasks.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 我们提出 LingBot-VA，这是一种通过统一视频-动作框架解决上述限制的自回归扩散世界模型。不同于预测离散 token 的自回归语言模型，我们的模型借助流匹配 [46, 50] 在连续潜变量空间中运行，通过迭代去噪，以自回归方式生成视频和动作表征分块。尽管本方法在概念上区分视觉动态预测与动作解码 [22, 27]，其关键架构洞见是把视频 token 和动作 token 交错排入一条自回归序列。两种模态由带共享注意力的 Transformer 混合架构（MoT）[43] 联合处理。在这一统一自回归生成过程中，潜变量想象与动作推断共同发生：在每个自回归步骤，模型一边通过迭代去噪生成预测的未来视觉状态，一边解码相应动作，使两条流可以彼此提供条件。该整合建立在大规模预训练视频扩散骨干 [79] 之上，带来若干优势：（i）反应式 AR 循环：因为视频和动作 token 构成统一序列，每个自回归步骤都能让系统依据最新真实观测重新校准，并及时调整预测未来和运动命令；（ii）通过 KV 缓存获得持久上下文：缓存的键值对保留交错的视频-动作轨迹，提供丰富上下文以帮助减轻时间漂移；（iii）因果一致性：统一序列上的因果注意力掩码确保预测视觉状态和动作命令均由先前状态支配，尊重物理动力学的时间箭头。该形式在每一步纳入真实观测，从而有助于减轻开环方法在长时序任务中常见的分布漂移。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> A primary challenge in deploying large-scale autoregressive video-action models is inference latency; generating high-fidelity video tokens through iterative denoising is computationally intensive. We address this through two complementary strategies. First, we introduce Noisy History Augmentation, a training scheme that enables partial denoising at inference time. The key insight is that action decoding does not always require pixel-perfect reconstruction; instead, it can rely on robust semantic structures. By training the action decoder to predict from partially noisy latent representations, we significantly reduce the computational overhead while maintaining precise action prediction. Second, we design an asynchronous coordination pipeline that overlaps computation with execution: while the robot executes current actions, the world model predicts future visual states and plans subsequent sequences. This parallelized architecture, combined with variable chunk-size training, facilitates high-frequency closed-loop control without compromising prediction quality.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 部署大规模自回归视频-动作模型的一个首要挑战是推理延迟：通过迭代去噪生成高保真视频 token 的计算开销很大。我们采用两项互补策略应对这一问题。第一，我们提出噪声历史增强（Noisy History Augmentation），这项训练方案使推理时能够进行部分去噪。其关键洞见是，动作解码并不总是需要像素级完美重建，而可以依赖稳健的语义结构。通过训练动作解码器从部分带噪的潜变量表征进行预测，我们在维持精确动作预测的同时显著降低计算开销。第二，我们设计异步协调流水线，使计算与执行重叠：机器人执行当前动作时，世界模型同步预测未来视觉状态并规划后续序列。这种并行架构结合可变分块大小训练，可以在不损害预测质量的情况下实现高频闭环控制。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> We evaluate LingBot-VA across diverse manipulation tasks in both simulation and real-world environments. Our method demonstrates competitive performance compared to state-of-the-art VLA policies, particularly in long-horizon tasks requiring temporal consistency. Our contributions are summarized as follows:
>
> - **Autoregressive Video-Action World Modeling:** We introduce an autoregressive diffusion framework that architecturally unifies visual dynamics prediction and action inference within a single interleaved sequence while maintaining their conceptual distinction. This formulation supports persistent memory through KV cache and causal consistency via attention masking.
> - **Mixture-of-Transformers Architecture with Asynchronous Execution:** We design a dual-stream MoT architecture with asymmetric capacity and introduce a partial denoising strategy combined with asynchronous coordination to enable efficient robotic control.
> - **Superior Long-Horizon and Precision Performance:** Extensive real-world and simulation experiments demonstrate consistent state-of-the-art performance, with particularly strong improvements on long-horizon and high-precision manipulation tasks. Our method also achieves significantly improved sample efficiency and strong generalization to novel scenes and object configurations.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 我们在仿真和现实环境中的多样操作任务上评估 LingBot-VA。与最先进的 VLA 策略相比，本方法表现出有竞争力的性能，尤其是在要求时间一致性的长时序任务上。我们的贡献概括如下：
>
> - **自回归视频-动作世界建模：** 我们提出一种自回归扩散框架，在架构上把视觉动态预测与动作推断统一到一条交错序列中，同时保留二者的概念区分。该形式通过 KV 缓存支持持久记忆，并通过注意力掩码保证因果一致性。
> - **带异步执行的 Transformer 混合架构：** 我们设计具有非对称容量的双流 MoT 架构，并提出把部分去噪与异步协调相结合的策略，以实现高效机器人控制。
> - **更优的长时序和精细操作性能：** 广泛的实机与仿真实验表明，该方法持续取得最先进性能，尤其在长时序和高精度操作任务上提升显著。本方法还显著提高了样本效率，并对新场景和物体配置展现出强泛化能力。

## 2 Preliminary

### 2.1 Flow Matching

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Flow matching [46, 50, 75] is a continuous-time generative modeling framework that learns to transform a simple source distribution (e.g., Gaussian noise) to a target data distribution through a continuous flow. Given a data sample $x_1$ and a noise sample $\epsilon \sim \mathcal{N}(0, I)$, flow matching defines a time-dependent vector field $v_s : \mathbb{R}^d \times [0, 1] \rightarrow \mathbb{R}^d$ that describes the instantaneous velocity of particles flowing from $\epsilon$ to $x_1$. The trajectory $x(s)$ evolves according to the ordinary differential equation (ODE):

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 流匹配 [46, 50, 75] 是一种连续时间生成建模框架，它学习通过连续流把简单源分布（例如高斯噪声）变换为目标数据分布。给定数据样本 $x_1$ 和噪声样本 $\epsilon \sim \mathcal{N}(0, I)$，流匹配定义随时间变化的向量场 $v_s : \mathbb{R}^d \times [0, 1] \rightarrow \mathbb{R}^d$，描述粒子从 $\epsilon$ 流向 $x_1$ 时的瞬时速度。轨迹 $x(s)$ 依照下列常微分方程（ODE）演化：

$$
\frac{d x(s)}{d s}=v_s(x(s)), \qquad x(0)=\epsilon\sim\mathcal{N}(0,I), \tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> where $s \in [0, 1]$ denotes the flow time. The model is trained to predict this vector field by minimizing:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 其中，$s \in [0, 1]$ 表示流时间。模型通过最小化下式来学习预测该向量场：

$$
\mathcal{L}_{\mathrm{FM}}=\mathbb{E}_{s,\epsilon,x_1}\!\left[\left\|v_\theta(x(s),s)-\dot{x}(s)\right\|^2\right], \tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> where $\dot{x}(s)$ is the true velocity along the interpolation path, typically defined as $x(s)=(1-s)\epsilon+s x_1$, giving $\dot{x}(s)=x_1-\epsilon$. At inference, samples are generated by solving the learned ODE from $s=0$ to $s=1$:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 其中，$\dot{x}(s)$ 是插值路径上的真实速度；该路径通常定义为 $x(s)=(1-s)\epsilon+s x_1$，因此 $\dot{x}(s)=x_1-\epsilon$。推理时，通过从 $s=0$ 到 $s=1$ 求解学习到的 ODE 生成样本：

$$
x_1=\epsilon+\int_0^1 v_\theta(x(s),s)\,d s. \tag{3}
$$

### 2.2 Video Generation with Conditional Flow Matching

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Recent video generation models [23, 35, 54, 79] leverage flow matching to generate videos conditioned on text or images. These models operate in the latent space of pretrained video autoencoders, where visual observations are encoded as latent representations $z_t=E(o_t)$ using encoder $E$ (e.g., from video diffusion models). Given a conditioning signal $c$ (text prompt or initial image), the flow matching model learns to generate a sequence of latent video frames $z=\{z_1,\ldots,z_T\}$ by predicting the vector field:

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 近期视频生成模型 [23, 35, 54, 79] 利用流匹配生成以文本或图像为条件的视频。这些模型运行在预训练视频自编码器的潜变量空间中，视觉观测由编码器 $E$（例如来自视频扩散模型的编码器）编码为潜变量表征 $z_t=E(o_t)$。给定条件信号 $c$（文本提示或初始图像），流匹配模型通过预测下列向量场，学习生成潜变量视频帧序列 $z=\{z_1,\ldots,z_T\}$：

$$
v_\theta(z(s),s\mid c)=\frac{d}{d s}z(s), \tag{4}
$$

### Figure 2. 框架概览

![Figure 2](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/fig02_framework.png)

**Caption:** Figure 2. Framework overview: LingBot-VA is conditioned by autoregressive diffusion for unified video-action world modeling. We leverage a dual-stream Mixture-of-Transformers (MoT) architecture that interleaves video and action tokens within a single sequence. At each autoregressive step, the video stream (initialized from Wan2.2-5B) first predicts future latent visual states via flow matching. Then the action stream decodes corresponding actions through inverse dynamics conditioning on the predicted visual transitions.

**Caption[CN]:** 图 2. 框架概览：LingBot-VA 以自回归扩散为条件进行统一视频-动作世界建模。我们采用双流 Transformer 混合架构（MoT），在单一序列中交错视频 token 和动作 token。在每个自回归步骤，由 Wan2.2-5B 初始化的视频流首先通过流匹配预测未来视觉潜变量状态；随后，动作流以预测的视觉转移为条件，通过逆动力学解码相应动作。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> where $s \in [0, 1]$ is the flow time and $z(s)$ represents the latent video at flow step $s$. The generation process starts from noise $z(0)=\epsilon\sim\mathcal{N}(0,I)$ and integrates the learned vector field to obtain the final latent video $z(1)$, which is then decoded to pixel space. This bidirectional generation framework enables flexible synthesis from text descriptions or seed images.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 其中，$s \in [0,1]$ 是流时间，$z(s)$ 表示流步骤 $s$ 时的潜变量视频。生成过程从噪声 $z(0)=\epsilon\sim\mathcal{N}(0,I)$ 开始，对学习到的向量场积分，得到最终潜变量视频 $z(1)$，随后将其解码到像素空间。这一双向生成框架支持从文本描述或种子图像进行灵活合成。

## 3 Method

### 3.1 Problem Statement & Approach Overview

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We study robotic manipulation as a sequential decision-making problem under partial observability. At each timestep $t$, the agent receives a visual observation $o_t\in\mathcal{O}$ and executes an action $a_t\in\mathcal{A}$, which induces a transition in the underlying physical world and produces the next observation $o_{t+1}$.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们把机器人操作研究为部分可观测条件下的序贯决策问题。在每个时间步 $t$，智能体接收视觉观测 $o_t\in\mathcal{O}$ 并执行动作 $a_t\in\mathcal{A}$；该动作会在底层物理世界中引发转移，并产生下一观测 $o_{t+1}$。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Vision-Language-Action (VLA) Policies.** Most existing VLA policies learn a direct, reactive mapping from observation history to actions:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **视觉-语言-动作（VLA）策略。** 多数现有 VLA 策略学习从观测历史到动作的直接反应式映射：

$$
a_t\sim\pi_\theta(\cdot\mid o_t), \tag{5}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> through imitation learning on robot demonstration data. While this end-to-end approach has shown impressive results, it suffers from a fundamental coupling problem: the model must simultaneously learn visual scene understanding, physical dynamics, and motor control from a single supervision signal of paired observations and actions. This entanglement leads to poor sample efficiency and limited generalization, as the model struggles to disentangle visual reasoning from action prediction without explicit dynamics modeling.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 该映射通过机器人示范数据上的模仿学习获得。尽管这种端到端方法已取得出色结果，它仍受一个根本耦合问题影响：模型必须从成对观测与动作构成的单一监督信号中，同时学习视觉场景理解、物理动力学和运动控制。由于缺少显式动力学建模，模型难以把视觉推理与动作预测解耦，这种纠缠导致样本效率不佳且泛化有限。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Our Approach.** Unlike VLA policies that directly learn action distributions, we adopt a world modeling perspective: instead of learning $\pi(a_t\mid o_t)$, we predict how the visual world will evolve, then infer actions based on these predictions. Our approach operates in two stages:

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **我们的方法。** 不同于直接学习动作分布的 VLA 策略，我们采用世界建模视角：不是学习 $\pi(a_t\mid o_t)$，而是先预测视觉世界将如何演化，再依据这些预测推断动作。本方法分两个阶段运行：

$$
\begin{aligned}
\text{(Stage 1) Visual dynamics prediction:}\quad &o_{t+1}\sim p_\theta(\cdot\mid o_{\le t}),\\
\text{(Stage 2) Inverse dynamics:}\quad &a_t\sim g_\psi(\cdot\mid o_t,o_{t+1}).
\end{aligned} \tag{6}
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Stage 1 learns to predict future visual observations given observation history. Stage 2 uses an inverse dynamics model to decode actions from desired visual transitions. This decomposition enables Stage 1 to leverage large-scale video data for learning physical priors, while Stage 2 only requires robot demonstrations to ground visual predictions in executable actions.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 第一阶段学习在给定观测历史时预测未来视觉观测。第二阶段使用逆动力学模型，从期望视觉转移中解码动作。这种分解使第一阶段可以利用大规模视频数据学习物理先验，而第二阶段只需要机器人示范，就能把视觉预测落地为可执行动作。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Method Overview.** Figure 2 illustrates the details of our framework. Our method consists of three key components, detailed in the following subsections: (§3.2) Autoregressive Video-Action World Modeling describes how we model visual dynamics in latent space and decode actions from predicted state transitions—this is the core formulation of our approach; (§3.3) LingBot-VA: Unified Architecture & Training presents our unified model for video-action pretraining, including the architecture design and training objective—this is the instantiation of our formulation; (§3.4) Real-time Deployment & Asynchronous Inference introduces our deployment strategy that enables real-time control through parallelized prediction and execution—this is the practical realization for robotic control.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **方法概览。** 图 2 展示了框架细节。本方法由三项关键组成部分构成，后续小节分别详述：（§3.2）自回归视频-动作世界建模说明如何在潜变量空间中建模视觉动态，并从预测状态转移解码动作——这是本方法的核心形式；（§3.3）LingBot-VA：统一架构与训练介绍用于视频-动作预训练的统一模型，包括架构设计与训练目标——这是该形式的具体实现；（§3.4）实时部署与异步推理介绍通过并行预测和执行实现实时控制的部署策略——这是其面向机器人控制的实践实现。

### 3.2 Autoregressive Video-Action World Modeling

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Previous video world models either focus on open-ended video prediction [54] or learn action-conditioned interactive environments [13, 56] primarily for game or simulation domains, which may not directly transfer to precise robotic manipulation. To leverage rich visual dynamics priors from video data for robot manipulation, we propose a unified video-action world modeling framework that jointly models visual observations and robot actions within a single autoregressive process. Unlike prior approaches that either decouple video prediction from action inference [16, 27] or rely on bidirectional diffusion within segments [97], our method unifies video and action within a single causal autoregressive framework, enabling persistent memory through KV cache and seamless integration of real-time observations.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 既有视频世界模型要么聚焦开放式视频预测 [54]，要么学习以动作为条件的交互环境 [13, 56]，且主要面向游戏或仿真领域，因此未必能直接迁移到精细机器人操作。为把视频数据中丰富的视觉动态先验用于机器人操作，我们提出统一的视频-动作世界建模框架，在单一自回归过程中联合建模视觉观测和机器人动作。不同于将视频预测与动作推断解耦 [16, 27] 或依赖片段内双向扩散 [97] 的既有方法，本方法在单一因果自回归框架中统一视频与动作，通过 KV 缓存获得持久记忆，并无缝纳入实时观测。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> **World Dynamics with Autoregressive Modeling.** Recent world models for robotics often adopt bidirectional video generation approaches [4, 20, 24, 42] or learn interactive simulators [86], which face fundamental limitations for closed-loop control. Open-loop methods that generate entire long sequences in one shot incur prohibitive computational cost and cannot incorporate real-time feedback for error correction. Chunk-based diffusion methods that generate video segments sequentially [22, 97] suffer from two critical issues: (1) they lack persistent memory across chunks, as each chunk is generated independently without access to the full history, leading to temporal inconsistencies and drift over long horizons; (2) the bidirectional attention within each chunk violates causality, preventing seamless integration with real-time observations during execution.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **采用自回归建模的世界动态。** 近期机器人世界模型常采用双向视频生成 [4, 20, 24, 42] 或学习交互式模拟器 [86]，但这些方法在闭环控制中面临根本限制。一次性生成整条长序列的开环方法计算成本高得难以接受，也无法纳入实时反馈进行纠错。顺序生成视频片段的分块扩散方法 [22, 97] 存在两个关键问题：（1）分块间缺乏持久记忆，因为每个分块都在无法访问完整历史的情况下独立生成，从而在长时序中导致时间不一致与漂移；（2）每个分块内的双向注意力违反因果性，阻碍执行过程中对实时观测的无缝整合。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> The physical world, however, is inherently causal and autoregressive: the present state depends only on the past, and we cannot observe the future before it occurs. This fundamental property motivates our autoregressive world modeling approach, which offers three critical advantages over chunk-based diffusion for robotic control: (1) **Persistent Memory:** by explicitly conditioning on the complete observation history through causal attention and KV cache, the model maintains long-term context and temporal coherence across the entire trajectory, avoiding the “amnesia” problem of chunk-based methods; (2) **Causal Consistency:** the unidirectional dependency structure naturally aligns with closed-loop execution, where new observations can be seamlessly incorporated as they arrive; (3) **Efficiency:** chunk-wise prediction with parallel generation within each chunk balances computational efficiency with autoregressive flexibility, enabling high-frequency control with real-time error correction.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 然而，物理世界在本质上具有因果性和自回归性：当前状态只依赖过去，而我们无法在未来发生之前观察它。这一基本性质促使我们采用自回归世界建模；相较分块扩散，它为机器人控制带来三项关键优势：（1）**持久记忆：** 通过因果注意力与 KV 缓存显式地以完整观测历史为条件，模型在整条轨迹上维持长期上下文和时间连贯性，避免分块方法的“失忆”问题；（2）**因果一致性：** 单向依赖结构天然契合闭环执行，新观测到达时可被无缝纳入；（3）**效率：** 逐块预测并在每个分块内并行生成，在计算效率与自回归灵活性之间取得平衡，从而以实时纠错支持高频控制。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> We formalize this as an autoregressive process: at each step, the world model predicts the next chunk of $K$ video frames using conditional flow matching:

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 我们将其形式化为自回归过程：在每一步，世界模型使用条件流匹配预测接下来包含 $K$ 帧的视频分块：

$$
o_{t+1:t+K}\sim p_\theta(\cdot\mid o_{\le t}), \tag{7}
$$

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> where tokens within each chunk are generated in parallel via bidirectional attention, while maintaining causal structure across chunks. This chunk-wise formulation balances generation efficiency with autoregressive flexibility for closed-loop correction.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> 其中，每个分块内部的 token 通过双向注意力并行生成，同时分块之间保持因果结构。这种逐块形式在生成效率和用于闭环修正的自回归灵活性之间取得平衡。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> **Video-Action State Encoding.** Operating directly on pixel-level video observations is computationally prohibitive due to the high dimensionality and redundancy of raw visual data. We leverage a causal video VAE [79] to compress visual observations into compact latent tokens $z_t=E(o_t\mid o_{<t})\in\mathbb{R}^{N\times C}$, where $N$ is the number of spatial tokens after passing into video VAE, and $C$ is the channel number. By conditioning on previous latent states, the encoder maintains temporal coherence while processing observations sequentially, naturally aligning with our autoregressive world modeling framework. To align robot actions with visual tokens, we project action vectors to token embeddings $a_t\in\mathbb{R}^{D}$ via a lightweight MLP $\phi(\cdot)$ where $D$ is the dimension of the video token after patchfication, enabling unified interleaving of visual and action tokens as in prior approaches [5, 22].

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> **视频-动作状态编码。** 由于原始视觉数据维度高且存在冗余，直接在像素级视频观测上运行会产生难以承受的计算开销。我们采用因果视频 VAE [79]，把视觉观测压缩为紧凑潜变量 token $z_t=E(o_t\mid o_{<t})\in\mathbb{R}^{N\times C}$，其中 $N$ 是输入视频 VAE 后的空间 token 数，$C$ 是通道数。编码器以先前潜变量状态为条件，在顺序处理观测时维持时间连贯性，从而天然契合自回归世界建模框架。为使机器人动作与视觉 token 对齐，我们通过轻量 MLP $\phi(\cdot)$ 把动作向量投影为 token 嵌入 $a_t\in\mathbb{R}^{D}$，其中 $D$ 是 patchfication 后视频 token 的维度；由此可以像既有方法 [5, 22] 一样统一交错视觉与动作 token。

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> **Latent Video State Transition.** While standard video generation models predict future frames based solely on visual history, robotic manipulation requires accounting for the embodiment’s physical state and interaction with the environment. During deployment, the robot’s state evolves through continuous interaction: each action modifies the embodiment’s configuration (e.g., gripper position, joint angles), which in turn influences how the scene evolves.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> **潜变量视频状态转移。** 标准视频生成模型仅依据视觉历史预测未来帧，而机器人操作还必须考虑机器人本体的物理状态及其与环境的交互。部署期间，机器人状态会通过持续交互演化：每个动作改变本体配置（例如夹爪位置、关节角度），继而影响场景如何演化。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> In many manipulation settings, actions encode absolute pose information (e.g., end-effector poses in world coordinates), so the action history $a_{<t}$ effectively captures the trajectory of the embodiment’s configuration. Conditioning on action history thus provides knowledge of how the robot has moved and interacted with objects, consistent with prior action-conditioned video/world models [22, 86, 97]. We extend our autoregressive formulation to condition on both observation and action histories:

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> 在许多操作设置中，动作编码绝对位姿信息（例如世界坐标中的末端执行器位姿），因此动作历史 $a_{<t}$ 实际上记录了本体配置的轨迹。以动作历史为条件，便能获知机器人如何运动并与物体交互，这与既有动作条件视频/世界模型 [22, 86, 97] 一致。我们扩展自回归形式，使其同时以观测历史和动作历史为条件：

$$
z_{t+1:t+K}\sim p_\theta(\cdot\mid z_{\le t},a_{<t}), \tag{8}
$$

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> where $z_t$ is the latent visual state and $a_t$ is the action token. This enables the world model to ground predictions in the embodiment’s state, ensuring that predicted observations reflect the robot’s physical interaction with the scene.

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> 其中，$z_t$ 是视觉潜变量状态，$a_t$ 是动作 token。这使世界模型能够把预测建立在本体状态上，确保预测观测反映机器人与场景的物理交互。

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> **Inverse Dynamics for Action Decoding.** Once the world model predicts future visual states, we leverage these predictions to plan actions. Rather than directly predicting actions from current observations, we employ an inverse dynamics model that infers actions by conditioning on desired future observations, enabling the policy to reason about what action leads to a desired visual outcome.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> **用于动作解码的逆动力学。** 世界模型预测未来视觉状态后，我们利用这些预测来规划动作。与直接从当前观测预测动作不同，我们采用以期望未来观测为条件来推断动作的逆动力学模型，使策略能够推理“什么动作会产生期望视觉结果”。

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> However, simply conditioning on the current and next states $(z_t,z_{t+1})$ is insufficient for accurate action prediction. The action history $a_{<t}$ encodes the embodiment’s state trajectory for determining feasible actions, while the observation history $z_{<t}$ provides temporal context for multi-step interactions (e.g., whether an object was previously grasped). We therefore formulate inverse dynamics as:

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> 然而，仅以当前状态和下一状态 $(z_t,z_{t+1})$ 为条件不足以准确预测动作。动作历史 $a_{<t}$ 编码用于判断动作可行性的本体状态轨迹，而观测历史 $z_{<t}$ 为多步交互提供时间上下文（例如此前是否已经抓住某物体）。因此，我们将逆动力学形式化为：

$$
a_{t:t+K-1}\sim g_\psi(\cdot\mid \hat{z}_{t+1:t+K},z_{\le t},a_{<t}), \tag{9}
$$

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> where the inverse dynamics model $g_\psi$ takes as input the predicted chunk of visual states $\hat{z}_{t+1:t+K}$ inferred by Eq. 8, observation history $z_{\le t}$, and action history $a_{<t}$. This mirrors recent IDM-based policies [1, 20, 22, 55, 73] that leverage future targets to infer feasible actions while maintaining consistency with embodiment dynamics.

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> 其中，逆动力学模型 $g_\psi$ 的输入包括由式（8）推断的预测视觉状态分块 $\hat{z}_{t+1:t+K}$、观测历史 $z_{\le t}$ 和动作历史 $a_{<t}$。这与近期基于 IDM 的策略 [1, 20, 22, 55, 73] 相呼应：它们利用未来目标推断可行动作，同时保持与本体动力学的一致性。

### 3.3 LingBot-VA: Unified Architecture & Training

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> **Architecture.** To jointly model video and action generation, we leverage a dual-stream diffusion transformer architecture that performs conditional flow matching for autoregressive prediction. Our model consists of two parallel transformer backbones: a video stream initialized from Wan2.2-5B (a large-scale pretrained video generation model with dimension $d_v$ [79]), and an action stream with same depth but significantly smaller width $d_a\ll d_v$. This asymmetric design is motivated by the observation that action distributions are inherently simpler than visual data requiring fewer parameters to model effectively while maintaining expressive capacity for visual dynamics.

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> **架构。** 为联合建模视频与动作生成，我们采用双流扩散 Transformer 架构，执行条件流匹配以进行自回归预测。模型包含两个并行 Transformer 骨干：一条视频流由 Wan2.2-5B（维度为 $d_v$ 的大规模预训练视频生成模型 [79]）初始化；另一条动作流深度相同，但宽度 $d_a\ll d_v$，显著更小。该非对称设计源于如下观察：动作分布在本质上比视觉数据简单，使用更少参数即可有效建模，同时仍为视觉动态保留足够表达能力。

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> **Video Sparsification.** Video frames exhibit significant temporal redundancy, especially in robotic manipulation where scenes evolve gradually. We sparsify the video sequence by temporally downsampling frames by a factor of $\tau=4$, reducing visual tokens while improving efficiency [5]. Since actions evolve at higher frequency than visual changes, we interleave the downsampled video tokens with action tokens in temporal order: for each video frame $o_t$, we associate $\tau$ consecutive actions $\{a_{t,1},a_{t,2},\ldots,a_{t,\tau}\}$, forming a unified sequence $[z_t,a_{t,1},a_{t,2},\ldots,a_{t,\tau},z_{t+1},\ldots]$ for joint modeling. This design means that predicting $K$ video frames corresponds to generating $\tau K$ actions, enabling high-frequency control while maintaining efficient video generation.

> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> **视频稀疏化。** 视频帧具有显著时间冗余，尤其是在场景逐渐演化的机器人操作中。我们在时间维度以 $\tau=4$ 的倍率下采样视频帧，使视频序列稀疏化，从而减少视觉 token 并提高效率 [5]。由于动作变化频率高于视觉变化，我们按时间顺序把下采样后的视频 token 与动作 token 交错排列：对于每个视频帧 $o_t$，关联 $\tau$ 个连续动作 $\{a_{t,1},a_{t,2},\ldots,a_{t,\tau}\}$，形成用于联合建模的统一序列 $[z_t,a_{t,1},a_{t,2},\ldots,a_{t,\tau},z_{t+1},\ldots]$。因此，预测 $K$ 个视频帧对应生成 $\tau K$ 个动作，在保持高效视频生成的同时实现高频控制。

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> **Mixture-of-Transformer Block.** To enable interaction while preserving modality-specific feature spaces, we employ a Mixture-of-Transformers (MOT) architecture [5, 19, 43], where video and action tokens are processed by separate transformer blocks at each layer, then fused via cross-modal attention [5]. At each layer, the video and action streams independently compute their query, key, and value matrices using separate QKV projection matrices, maintaining distinct feature spaces for each modality. To align dimensions for cross-modal fusion, action tokens are first projected to the video dimension via a linear layer, participate in joint self-attention, then projected back to their original dimension via a residual connection that preserves the action-specific representations. This MOT design allows video and action to mutually influence each other through attention while maintaining separate parameterizations, preventing interference between modality-specific feature representations. For action decoding, the final action stream outputs are mapped to low-dimensional action vectors via a linear projection head.

> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> **Mixture-of-Transformer 模块。** 为在保留模态特定特征空间的同时实现交互，我们采用 Transformer 混合（MOT）架构 [5, 19, 43]：每一层分别用不同 Transformer 模块处理视频 token 与动作 token，再通过跨模态注意力融合 [5]。在每一层中，视频流和动作流分别使用独立 QKV 投影矩阵计算各自的 query、key 和 value 矩阵，从而为每种模态维持不同特征空间。为对齐跨模态融合所需的维度，动作 token 先通过线性层投影到视频维度，参与联合自注意力，然后再通过保留动作特定表征的残差连接投影回原维度。这种 MOT 设计允许视频和动作通过注意力彼此影响，同时维持独立参数化，避免模态特定特征表征之间相互干扰。动作解码时，最终动作流输出通过线性投影头映射为低维动作向量。

> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> **Action Network Initialization.** Proper initialization of the action stream is critical for training stability and convergence. We find that training the action network from scratch leads to unstable optimization and slow convergence, as the action tokens’ output distribution initially diverges significantly from the video distribution, disrupting the joint attention mechanism. To address this, we initialize the action network weights by interpolating the pretrained video weights according to the action dimension, then apply a scaling factor $\alpha=\sqrt{d_v/d_a}$ to preserve output variance, where $d_v$ and $d_a$ are the video and action dimensions. This initialization strategy ensures that action tokens start with output distributions comparable to video tokens, stabilizing early-stage training and accelerating convergence.

> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> **动作网络初始化。** 动作流的恰当初始化对训练稳定性与收敛至关重要。我们发现，从头训练动作网络会导致优化不稳定、收敛缓慢，因为动作 token 的初始输出分布与视频分布存在显著差异，扰乱联合注意力机制。为此，我们根据动作维度对预训练视频权重进行插值，以其初始化动作网络权重，然后施加缩放因子 $\alpha=\sqrt{d_v/d_a}$ 来保持输出方差，其中 $d_v$ 和 $d_a$ 分别是视频维度与动作维度。该初始化策略确保动作 token 一开始就具有与视频 token 可比的输出分布，从而稳定早期训练并加快收敛。

> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> **Variable Chunk Size Training.** To enable flexible deployment, we randomly sample the chunk size $K$ from a predefined range during training. By training with variable chunk sizes (e.g., $K\in[1,8]$), the model learns to generate coherent predictions across different temporal horizons. At inference time, this allows freely selecting the chunk size to balance computational efficiency and planning horizon—larger chunks reduce the number of autoregressive steps but require longer per-step computation, while smaller chunks enable more frequent closed-loop correction. In our experiments, we use $K=4$ for deployment as a practical trade-off.

> <span style="color:#F59E0B"><strong>Para. 23[CN]:</strong></span> **可变分块大小训练。** 为支持灵活部署，我们在训练期间从预定义范围内随机采样分块大小 $K$。通过用可变分块大小训练（例如 $K\in[1,8]$），模型学会在不同时间跨度上生成连贯预测。推理时可以自由选择分块大小，以平衡计算效率和规划跨度——较大分块减少自回归步骤数，但每一步计算更久；较小分块则能进行更频繁的闭环修正。实验中，我们采用 $K=4$ 进行部署，作为一种实践折中。

> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> **Teacher Forcing for Unified Video-Action Training.** In §3.2, we formulated both visual dynamics prediction (Eq. 7) and inverse dynamics (Eq. 8) as autoregressive modeling problems, where each prediction conditions on the history of observations and actions. This unified autoregressive formulation enables a natural training strategy: we can treat the interleaved video-action sequence as a single unified sequence and train the model using standard next-token prediction, analogous to language modeling in NLP [76].

> <span style="color:#F59E0B"><strong>Para. 24[CN]:</strong></span> **用于统一视频-动作训练的教师强制。** 在 §3.2 中，我们把视觉动态预测（式（7））和逆动力学（式（8））都表述为自回归建模问题，其中每项预测均以观测历史和动作历史为条件。这种统一自回归形式自然导出一种训练策略：可以把交错的视频-动作序列视为单一统一序列，并像 NLP 的语言建模 [76] 一样，采用标准下一 token 预测训练模型。

### Figure 3. 教师强制注意力掩码

![Figure 3](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/fig03_attention_mask.png)

**Caption:** Figure 3. Teacher Forcing Attention Mask: Causal attention mask for unified video-action pretraining. Each token can only attend to preceding tokens in the temporal sequence.

**Caption[CN]:** 图 3. 教师强制注意力掩码：用于统一视频-动作预训练的因果注意力掩码。每个 token 只能关注时间序列中位于其之前的 token。

> <span style="color:#3B82F6"><strong>Para. 25:</strong></span> Specifically, given an episode with interleaved tokens, we train the model to predict each token conditioned on all preceding tokens in the sequence. This is implemented via teacher forcing: during training, we use ground-truth tokens from the dataset as context for predicting subsequent tokens, rather than model-generated predictions. The causal dependency structure is enforced through attention masking (Figure 3)—each token can only attend to tokens that appear earlier in the temporal sequence.

> <span style="color:#F59E0B"><strong>Para. 25[CN]:</strong></span> 具体而言，给定包含交错 token 的 episode，我们训练模型以序列中所有先前 token 为条件预测每个 token。这通过教师强制实现：训练期间使用数据集中的真实 token 作为预测后续 token 的上下文，而不是使用模型生成的预测。注意力掩码（图 3）强制执行因果依赖结构——每个 token 只能关注时间序列中更早出现的 token。

> <span style="color:#3B82F6"><strong>Para. 26:</strong></span> Importantly, teacher forcing is particularly well-suited for robotic manipulation: unlike pure generative modeling where it leads to train-test distribution mismatch, robot policies naturally retrieve real-world observations during deployment, directly matching the training regime. This formulation offers two key benefits: (1) unifying video and action prediction under a single training objective enables end-to-end learning of world dynamics and action inference; (2) by processing episodes in parallel with causal attention masking, we efficiently optimize both components across all timesteps in a single forward pass.

> <span style="color:#F59E0B"><strong>Para. 26[CN]:</strong></span> 重要的是，教师强制特别适合机器人操作：在纯生成建模中，它会造成训练—测试分布失配；而机器人策略部署时天然会重新获取现实观测，这与训练范式直接匹配。该形式有两项关键收益：（1）在单一训练目标下统一视频预测与动作预测，使世界动态和动作推断能够端到端学习；（2）利用因果注意力掩码并行处理 episode，可在一次前向传播中高效优化所有时间步上的两个组成部分。

> <span style="color:#3B82F6"><strong>Para. 27:</strong></span> **Noisy History Augmentation.** The primary bottleneck during inference remains video token generation—the number of video tokens are much larger than action tokens, and each requires multiple denoising steps through the flow matching process. To address this, we introduce a noise augmentation strategy during training that enables partial denoising at test time. The key insight is that action prediction does not require fully denoised video representations; the inverse dynamics model can learn to extract action-relevant information from partially noisy video states. Specifically, during training, we randomly augment the video history $z_{\le t}$ with noise following the same interpolation scheme as flow matching:

> <span style="color:#F59E0B"><strong>Para. 27[CN]:</strong></span> **噪声历史增强。** 推理期间的首要瓶颈仍是视频 token 生成——视频 token 数远大于动作 token，且每个 token 都需要在流匹配过程中经历多步去噪。为解决这一问题，我们在训练中引入噪声增强策略，使测试时可以部分去噪。其关键洞见是，动作预测不要求完全去噪的视频表征；逆动力学模型可以学习从部分带噪的视频状态中提取与动作相关的信息。具体而言，训练期间我们按照与流匹配相同的插值方案，随机用噪声增强视频历史 $z_{\le t}$：

$$
\tilde z_{\le t}=\begin{cases}
(1-s_{\mathrm{aug}})\epsilon+s_{\mathrm{aug}}z_{\le t}, & p=0.5,\quad s_{\mathrm{aug}}\in[0.5,1],\ \epsilon\sim\mathcal{N}(0,I),\\
z_{\le t}, & 1-p=0.5.
\end{cases} \tag{10}
$$

> <span style="color:#3B82F6"><strong>Para. 28:</strong></span> This augmentation trains the action decoder to predict actions from partially noisy video representations. At inference time, this enables a significant speedup: instead of fully denoising video tokens from $s=0$ to $s=1$, we only need to denoise to $s=0.5$, halving the number of denoising steps for video generation while maintaining action prediction quality.

> <span style="color:#F59E0B"><strong>Para. 28[CN]:</strong></span> 这种增强训练动作解码器从部分带噪的视频表征预测动作。推理时，它带来显著加速：视频 token 不再需要从 $s=0$ 完全去噪至 $s=1$，而只需去噪至 $s=0.5$；这样在保持动作预测质量的同时，将视频生成的去噪步骤数减半。

#### Algorithm 1. KV Cache Inference

> <span style="color:#3B82F6"><strong>Para. 29:</strong></span> **Algorithm 1 — KV Cache Inference**  
> **Require:** Initial observation $o_0$, chunk size $K$, KV cache $C$.
>
> 1. $z_0\leftarrow E(o_0)$, $C\leftarrow\{z_0\}$.
> 2. $t\leftarrow0$.
> 3. **loop**
> 4. Sample $\epsilon\sim\mathcal{N}(0,I)$.
> 5. **Generate video chunk (integrate to $s=0.5$):** $\tilde z_{t+1:t+K}\leftarrow\epsilon+\int_0^{0.5}v_\theta(z^{(s)}_{t+1:t+K},s\mid C)\,ds$.
> 6. Sample $\epsilon\sim\mathcal{N}(0,I)$.
> 7. **Generate action chunk (integrate to $s=1$):** $a_{t:t+K-1}\leftarrow\epsilon+\int_0^1v_\psi(a^{(s)}_{t:t+K-1},s\mid\tilde z_{t:t+K},C)\,ds$.
> 8. **for** $i=t$ **to** $t+K-1$ **do**
> 9. Execute $a_i$, receive $o_{i+1}$. **Execute and collect observations.**
> 10. $z_{i+1}\leftarrow E(o_{i+1})$.
> 11. **end for**
> 12. $C\leftarrow C\cup\{z_{t+1:t+K},a_{t:t+K-1}\}$. **Update KV cache.**
> 13. $t\leftarrow t+K$.
> 14. **end loop**

> <span style="color:#F59E0B"><strong>Para. 29[CN]:</strong></span> **算法 1——KV 缓存推理**  
> **输入要求：** 初始观测 $o_0$、分块大小 $K$、KV 缓存 $C$。
>
> 1. $z_0\leftarrow E(o_0)$，$C\leftarrow\{z_0\}$。
> 2. $t\leftarrow0$。
> 3. **循环**
> 4. 采样 $\epsilon\sim\mathcal{N}(0,I)$。
> 5. **生成视频分块（积分至 $s=0.5$）：** $\tilde z_{t+1:t+K}\leftarrow\epsilon+\int_0^{0.5}v_\theta(z^{(s)}_{t+1:t+K},s\mid C)\,ds$。
> 6. 采样 $\epsilon\sim\mathcal{N}(0,I)$。
> 7. **生成动作分块（积分至 $s=1$）：** $a_{t:t+K-1}\leftarrow\epsilon+\int_0^1v_\psi(a^{(s)}_{t:t+K-1},s\mid\tilde z_{t:t+K},C)\,ds$。
> 8. **对** $i=t$ **至** $t+K-1$ **执行循环**
> 9. 执行 $a_i$，接收 $o_{i+1}$。**执行动作并收集观测。**
> 10. $z_{i+1}\leftarrow E(o_{i+1})$。
> 11. **结束循环**
> 12. $C\leftarrow C\cup\{z_{t+1:t+K},a_{t:t+K-1}\}$。**更新 KV 缓存。**
> 13. $t\leftarrow t+K$。
> 14. **结束总循环**

> <span style="color:#3B82F6"><strong>Para. 30:</strong></span> **Training Objective.** We jointly optimize both video and action using flow matching with the noisy history augmentation described above. For video tokens $z_t$, the dynamics loss supervises velocity field prediction conditioned on (potentially noisy) history:

> <span style="color:#F59E0B"><strong>Para. 30[CN]:</strong></span> **训练目标。** 我们采用流匹配并结合上述噪声历史增强，对视频和动作进行联合优化。对于视频 token $z_t$，动力学损失监督以（可能带噪的）历史为条件的速度场预测：

$$
\mathcal{L}_{\mathrm{dyn}}=\mathbb{E}_{t,s,z_{t+1},\epsilon}\!\left[\left\|v_\theta(z_{t+1}^{(s)},s,\tilde z_{\le t},a_{<t}\mid c)-\dot z_{t+1}^{(s)}\right\|^2\right]. \tag{11}
$$

> <span style="color:#3B82F6"><strong>Para. 31:</strong></span> Here $s\in[0,1]$ is flow time, $z_{t+1}^{(s)}=(1-s)\epsilon+s z_{t+1}$ with $\epsilon\sim\mathcal{N}(0,I)$, $\dot z_{t+1}^{(s)}=z_{t+1}-\epsilon$, $\tilde z_{\le t}$ is the augmented history (Eq. 10), and $c$ is the language instruction. For action tokens $a_t$, the inverse dynamics loss conditions on current and next observations:

> <span style="color:#F59E0B"><strong>Para. 31[CN]:</strong></span> 这里，$s\in[0,1]$ 为流时间，$z_{t+1}^{(s)}=(1-s)\epsilon+s z_{t+1}$ 且 $\epsilon\sim\mathcal{N}(0,I)$，$\dot z_{t+1}^{(s)}=z_{t+1}-\epsilon$，$\tilde z_{\le t}$ 是增强历史（式（10）），$c$ 是语言指令。对于动作 token $a_t$，逆动力学损失以当前观测和下一观测为条件：

$$
\mathcal{L}_{\mathrm{inv}}=\mathbb{E}_{t,s,a_t,\epsilon}\!\left[\left\|v_\psi(a_t^{(s)},s,\tilde z_{\le t+1},a_{<t}\mid c)-\dot a_t^{(s)}\right\|^2\right]. \tag{12}
$$

> <span style="color:#3B82F6"><strong>Para. 32:</strong></span> Here $a^{(s)}=(1-s)\epsilon+s a_t$ with $\epsilon\sim\mathcal{N}(0,I)$, $\tilde z_t,\tilde z_{t+1}$ are the (potentially noisy) current and next video tokens, and $c$ is the language instruction. The complete objective is $\mathcal{L}=\mathcal{L}_{\mathrm{dyn}}+\lambda\mathcal{L}_{\mathrm{inv}}$.

> <span style="color:#F59E0B"><strong>Para. 32[CN]:</strong></span> 这里，$a^{(s)}=(1-s)\epsilon+s a_t$ 且 $\epsilon\sim\mathcal{N}(0,I)$，$\tilde z_t,\tilde z_{t+1}$ 是（可能带噪的）当前视频 token 和下一视频 token，$c$ 是语言指令。完整目标为 $\mathcal{L}=\mathcal{L}_{\mathrm{dyn}}+\lambda\mathcal{L}_{\mathrm{inv}}$。

### 3.4 Real-time Deployment & Asynchronous Inference

> <span style="color:#3B82F6"><strong>Para. 33:</strong></span> **KV Cache for Efficient Autoregressive Inference.** Our autoregressive formulation naturally enables KV cache acceleration during inference. Since each prediction step conditions on the history of observations and actions, we cache the key-value pairs from previous tokens to avoid redundant computation. At each autoregressive step, only the new tokens (current observation and predicted actions) require full attention computation, while cached history tokens are reused. Algorithm 1 describes the complete inference procedure with KV cache.

> <span style="color:#F59E0B"><strong>Para. 33[CN]:</strong></span> **用于高效自回归推理的 KV 缓存。** 自回归形式天然支持在推理时使用 KV 缓存加速。由于每个预测步骤以观测与动作历史为条件，我们缓存先前 token 的键值对，以避免冗余计算。每个自回归步骤只有新 token（当前观测和预测动作）需要完整注意力计算，而历史 token 直接复用缓存。算法 1 给出使用 KV 缓存的完整推理流程。

> <span style="color:#3B82F6"><strong>Para. 34:</strong></span> **Asynchronous Prediction and Execution.** Despite the efficiency gains from KV cache and partial denoising, autoregressive prediction still incurs non-negligible latency that can violate real-time control requirements. To address this, we introduce an asynchronous inference strategy that pipelines action prediction with execution, effectively hiding prediction latency. We illustrate the difference between synchronous and asynchronous inference in Fig. 4.

> <span style="color:#F59E0B"><strong>Para. 34[CN]:</strong></span> **异步预测与执行。** 尽管 KV 缓存和部分去噪提高了效率，自回归预测仍会产生不可忽略的延迟，可能不满足实时控制要求。为此，我们提出异步推理策略，把动作预测与执行组成流水线，从而有效隐藏预测延迟。图 4 展示同步推理与异步推理的差异。

> <span style="color:#3B82F6"><strong>Para. 35:</strong></span> The key insight is to overlap computation with execution (Fig. 4B): While the robot executes the current action chunk $a_t$, the model simultaneously predicts the subsequent action chunk $a_{t+1}$ conditioned on the most recent real observation $z_{t-1}$ (received after the execution of $a_{t-1}$). For simplicity, we use $z_t$ to denote latent observations (ignoring the video VAE compression) instead of $o_t$ in this section. We discard all history data before timestamp $t-1$ and use the hat notation $\hat{\ }$ to mark predicted visual content. Consequently, the model’s active context is limited to the executed action chunk $a_{t-1}$, the recent ground-truth observation $z_{t-1}$, the currently executing action $a_t$, and its corresponding visual forecast $\hat z_t$. A naive auto-regressive implementation (Fig. 4B-1) is to store these tokens into the KV cache and predict $\hat z_{t+1}$. However, we observed that such a design frequently leads to open-loop degradation and trajectory drift. Because the video generative model inherently favors temporal smoothness, it tends to “continue” the hallucinated video $\hat z_t$ while ignoring the critical physical feedback provided by the real observation $z_{t-1}$, eventually causing the model to lose its capacity to react to the environment.

> <span style="color:#F59E0B"><strong>Para. 35[CN]:</strong></span> 关键洞见是让计算与执行重叠（图 4B）：机器人执行当前动作分块 $a_t$ 时，模型同时以最近的真实观测 $z_{t-1}$（在执行 $a_{t-1}$ 后收到）为条件，预测后续动作分块 $a_{t+1}$。为简化表述，本节使用 $z_t$ 表示潜变量观测（忽略视频 VAE 压缩），而不再使用 $o_t$。我们丢弃时间戳 $t-1$ 以前的所有历史数据，并用帽号 $\hat{\ }$ 标记预测视觉内容。因此，模型的活动上下文仅限于已执行动作分块 $a_{t-1}$、最近的真实观测 $z_{t-1}$、当前正在执行的动作 $a_t$，以及对应视觉预测 $\hat z_t$。一种朴素自回归实现（图 4B-1）是把这些 token 存入 KV 缓存并预测 $\hat z_{t+1}$。然而，我们观察到这种设计常导致开环退化和轨迹漂移。因为视频生成模型天然偏好时间平滑，它倾向于“延续”幻觉视频 $\hat z_t$，同时忽略真实观测 $z_{t-1}$ 提供的关键物理反馈，最终使模型失去对环境作出反应的能力。

### Figure 4. 异步流水线设计概览

![Figure 4](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/fig04_async_pipeline.png)

**Caption:** Figure 4. Asynchronous pipeline design overview: The traditional synchronous pipeline (A) suffers from delays caused by blocked computations, while the asynchronous pipeline (B) addresses this issue by enabling parallel computation and execution. However, a naive asynchronous implementation (B-1) relies on outdated visual predictions. In contrast, we improve and refine asynchronous prediction through forward dynamic prediction (B-2), which updates stale predictions with recent real-world observations.

**Caption[CN]:** 图 4. 异步流水线设计概览：传统同步流水线（A）会因计算阻塞而产生延迟，异步流水线（B）通过并行计算与执行解决该问题。然而，朴素异步实现（B-1）依赖过时的视觉预测。相比之下，我们通过前向动态预测（B-2）改进并细化异步预测，使用最近的真实观测更新陈旧预测。

#### Algorithm 2. Asynchronous Inference and Execution

> <span style="color:#3B82F6"><strong>Para. 36:</strong></span> **Algorithm 2 — Asynchronous Inference and Execution**  
> **Require:** Initial observation $o_0$, chunk size $K$, KV cache $C$.
>
> 1. $z_0\leftarrow E(o_0)$; $C\leftarrow\{z_0\}$.
> 2. $\tilde z_{1:K},a_{0:K-1}\leftarrow\operatorname{PREDICT}(C)$. **Cold Start.**
> 3. $\mathrm{ObsQueue}\leftarrow\varnothing$. **Thread-safe queue for incoming real observations.**
> 4. $t\leftarrow0$.
> 5. **loop**
> 6. **parallel:**
>    - **Branch A: Robot Execution.** `async EXECUTOR`$(a_{t:t+K-1},\mathrm{ObsQueue})$. **Execute pre-computed actions.**
>    - **Branch B: Inference with FDM Grounding.**
>      1. **if** $t>0$ **then**
>      2. $o_{t-K+1:t}\leftarrow\mathrm{ObsQueue.dequeue}()$. **Get real observation.**
>      3. $z_{t-K+1:t}\leftarrow E(o_{t-K+1:t})$.
>      4. $C\leftarrow C\cup\{z_{t-K+1,t},a_{t-K:t-1}\}$. **Cache feedback.**
>      5. **end if**
>      6. $C_{\mathrm{tmp}}\leftarrow C\cup\{a_{t:t+K-1}\}$. **Cache action being executed.**
>      7. $z_{t+1:t+K}\leftarrow\operatorname{FDM}(C_{\mathrm{tmp}})$. **Imagine visual outcome.**
>      8. $C_{\mathrm{tmp}}\leftarrow C_{\mathrm{tmp}}\cup\{z_{t+1:t+K}\}$. **Update cache.**
>      9. $\tilde z_{t+K+1:t+2K},a_{t+K:t+2K-1}\leftarrow\operatorname{PREDICT}(C_{\mathrm{tmp}})$.
> 7. $t\leftarrow t+K$.
> 8. **end loop**

> <span style="color:#F59E0B"><strong>Para. 36[CN]:</strong></span> **算法 2——异步推理与执行**  
> **输入要求：** 初始观测 $o_0$、分块大小 $K$、KV 缓存 $C$。
>
> 1. $z_0\leftarrow E(o_0)$；$C\leftarrow\{z_0\}$。
> 2. $\tilde z_{1:K},a_{0:K-1}\leftarrow\operatorname{PREDICT}(C)$。**冷启动。**
> 3. $\mathrm{ObsQueue}\leftarrow\varnothing$。**用于接收真实观测的线程安全队列。**
> 4. $t\leftarrow0$。
> 5. **循环**
> 6. **并行执行：**
>    - **分支 A：机器人执行。** `async EXECUTOR`$(a_{t:t+K-1},\mathrm{ObsQueue})$。**执行预计算动作。**
>    - **分支 B：带 FDM grounding 的推理。**
>      1. **若** $t>0$ **则**
>      2. $o_{t-K+1:t}\leftarrow\mathrm{ObsQueue.dequeue}()$。**获取真实观测。**
>      3. $z_{t-K+1:t}\leftarrow E(o_{t-K+1:t})$。
>      4. $C\leftarrow C\cup\{z_{t-K+1,t},a_{t-K:t-1}\}$。**缓存反馈。**
>      5. **结束条件分支**
>      6. $C_{\mathrm{tmp}}\leftarrow C\cup\{a_{t:t+K-1}\}$。**缓存正在执行的动作。**
>      7. $z_{t+1:t+K}\leftarrow\operatorname{FDM}(C_{\mathrm{tmp}})$。**想象视觉结果。**
>      8. $C_{\mathrm{tmp}}\leftarrow C_{\mathrm{tmp}}\cup\{z_{t+1:t+K}\}$。**更新缓存。**
>      9. $\tilde z_{t+K+1:t+2K},a_{t+K:t+2K-1}\leftarrow\operatorname{PREDICT}(C_{\mathrm{tmp}})$。
> 7. $t\leftarrow t+K$。
> 8. **结束循环**

> <span style="color:#3B82F6"><strong>Para. 37:</strong></span> To mitigate this, we introduce a Forward Dynamics Model (FDM) grounded step into our inference pipeline (Fig. 4B-2). Instead of relying on stale forecasts, we replace it by executing a forward dynamics pass: the model uses the recent feedback $z_{t-1}$ and “imagines” the resulting visual state $z_t$ after applying action $a_t$. By caching this feedback-grounded prediction instead of a stale forecast, we force the model to re-align with environmental feedback before predicting $z_{t+1}$. This design enhances our asynchronous algorithm into a robust closed-loop system, enabling the robot to effectively perceive and react to real-world changes.

> <span style="color:#F59E0B"><strong>Para. 37[CN]:</strong></span> 为缓解该问题，我们在推理流水线中引入基于前向动力学模型（FDM）的 grounding 步骤（图 4B-2）。我们不再依赖陈旧预测，而以一次前向动力学传播替代它：模型利用最近反馈 $z_{t-1}$，“想象”施加动作 $a_t$ 后得到的视觉状态 $z_t$。缓存这种以反馈为 grounding 的预测，而非陈旧预测，迫使模型在预测 $z_{t+1}$ 之前重新与环境反馈对齐。该设计把异步算法增强为稳健闭环系统，使机器人能够有效感知现实世界变化并作出反应。

> <span style="color:#3B82F6"><strong>Para. 38:</strong></span> Algorithm 2 formalizes this asynchronous pipeline. During post training, we additionally incorporate a forward dynamics prediction loss:

> <span style="color:#F59E0B"><strong>Para. 38[CN]:</strong></span> 算法 2 形式化了这一异步流水线。在后训练期间，我们还加入前向动力学预测损失：

$$
\mathcal{L}_{\mathrm{fdm}}=\mathbb{E}_{t,s,\hat z_{t+1},\epsilon}\!\left[\left\|v_\psi(\tilde z_{t+1},s,z_t,a_t,\tilde z_{<t},\hat a_{<t}\mid c)-\dot z_{t+1}^{(s)}\right\|^2\right]. \tag{13}
$$

## 4 Experiments

### 4.1 Dataset Curation and Preprocessing

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We curate a large-scale training corpus by aggregating existing public robot manipulation datasets. All datasets undergo preprocessing to ensure consistency in data format and annotation quality, and are split into 90% training and 10% validation per dataset to monitor training dynamics.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们汇集现有公开机器人操作数据集，构建大规模训练语料。所有数据集均经过预处理，以确保数据格式和标注质量的一致性；每个数据集按 90% 训练集、10% 验证集划分，用于监控训练动态。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Unified Action Representation.** To achieve cross-embodiment generalization, we define a universal action interface to adapt to different datasets. We use a dual-arm representation where each robotic arm is characterized by both end-effector pose (EEF) and joint angles. The end-effector pose consists of XYZ coordinates and a rotation quaternion (7 dimensions). For joint angles, we support a maximum of 7 degrees of freedom for single-arm embodiments; if a robot has fewer than 7 joint dimensions, we pad the missing dimensions with zeros to maintain a unified 7-dimensional representation. Each arm also has one gripper action dimension. Therefore, the total action dimensionality for dual-arm systems is: $7_{\mathrm{EEF}}+7_{\mathrm{joints}}+1_{\mathrm{gripper}}$ per arm, resulting in $(7+7+1)\times2=30$ dimensions.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **统一动作表征。** 为实现跨本体泛化，我们定义通用动作接口，以适配不同数据集。我们采用双臂表征，每条机械臂同时由末端执行器位姿（EEF）和关节角度刻画。末端执行器位姿由 XYZ 坐标和旋转四元数组成（7 维）。对于关节角度，单臂本体最多支持 7 个自由度；若某机器人少于 7 个关节维度，则用零填充缺失维度，以保持统一的 7 维表征。每条机械臂另有一个夹爪动作维度。因此，双臂系统的总动作维数为：每条手臂 $7_{\mathrm{EEF}}+7_{\mathrm{joints}}+1_{\mathrm{gripper}}$，合计 $(7+7+1)\times2=30$ 维。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Training Data Composition.** We aggregate data from six sources spanning diverse embodiments, environments, and task categories:
>
> - **Agibot [2]:** Large-scale dataset with diverse manipulation tasks from mobile manipulators.
> - **RoboMind [81]:** Multi-embodiment manipulation demonstrations.
> - **InternData-A1 [74]:** Large-scale simulation dataset for sim-to-real transfer.
> - **OXE [53]:** Multi-embodiment dataset; we use the OpenVLA subset.
> - **UMI Data [18, 45, 48, 51, 60, 92]:** Human demonstration dataset collected via universal manipulation interface, excluding DexUMI. https://umi-data.github.io/
> - **RoboCOIN [84]:** Cross-embodiment bimanual robotics data.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **训练数据组成。** 我们汇集六个来源的数据，覆盖多样本体、环境和任务类别：
>
> - **Agibot [2]：** 来自移动操作机器人的大规模多样操作任务数据集。
> - **RoboMind [81]：** 多本体操作示范。
> - **InternData-A1 [74]：** 面向 sim-to-real 迁移的大规模仿真数据集。
> - **OXE [53]：** 多本体数据集；我们使用 OpenVLA 子集。
> - **UMI Data [18, 45, 48, 51, 60, 92]：** 通过通用操作接口采集的人类示范数据集，不包括 DexUMI。https://umi-data.github.io/
> - **RoboCOIN [84]：** 跨本体双臂机器人数据。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> In total, our training corpus comprises approximately 16K hours of robot manipulation data across diverse tasks and environments, including internally collected demonstrations.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 总计而言，我们的训练语料包含约 16K 小时的机器人操作数据，覆盖多样任务与环境，其中也包括内部采集的示范。

### 4.2 Implementation & Training Details

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Implementation Details.** We use Wan2.2-5B as the backbone for the video stream, with hidden dimension $d_v=3072$ and 30 transformer layers. The action stream shares the same depth but uses a reduced hidden dimension $d_a=768$ (4$\times$ smaller), resulting in approximately 350M additional parameters and a total model size of 5.3B parameters. Both streams employ RoPE positional encoding and are connected via the MoT architecture described in §3.3. We adopt the Wan2.2 causal VAE for tokenization with a $4\times16\times16$ (temporal $\times$ height $\times$ width) compression ratio, combined with a patchify operation that further reduces spatial dimensions by 2. The encoded views are concatenated along the width dimension, resulting in a total of $N=192$ spatial tokens per frame. The action encoder $\phi$ and decoder are implemented as single-layer MLPs with hidden dimension 256. We normalize actions using per-dimension quantile normalization statistics computed from the training set. Task instructions are encoded using a frozen T5 text encoder [59] and injected via cross-attention. During training, chunk size $K$ is randomly sampled from $[1,4]$.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **实现细节。** 视频流使用 Wan2.2-5B 作为骨干，其隐藏维度 $d_v=3072$，包含 30 个 Transformer 层。动作流深度相同，但隐藏维度缩减为 $d_a=768$（小 4$\times$），因此额外增加约 350M 参数，模型总规模为 5.3B 参数。两条流都采用 RoPE 位置编码，并通过 §3.3 所述 MoT 架构连接。我们采用 Wan2.2 因果 VAE 进行 token 化，压缩比为 $4\times16\times16$（时间 $\times$ 高度 $\times$ 宽度），再结合 patchify 操作把空间维度进一步缩小 2 倍。编码后的各视图沿宽度维连接，使每帧共有 $N=192$ 个空间 token。动作编码器 $\phi$ 与解码器均实现为隐藏维度 256 的单层 MLP。动作使用根据训练集计算的逐维分位数归一化统计量进行归一化。任务指令使用冻结的 T5 文本编码器 [59] 编码，并通过跨注意力注入。训练期间，分块大小 $K$ 从 $[1,4]$ 中随机采样。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> For inference, we use Euler solver with 3 steps for video tokens (integrating to $s=0.6$) and 10 steps for action tokens (integrating to $s=1.0$). Video CFG scale is set to 5.0, while action CFG scale is set to 1.0. During training, noise augmentation is applied with probability $p=0.5$ and $s_{\mathrm{aug}}\sim\mathrm{Uniform}[0.5,1.0]$. Following LLM practices, we pack multiple episodes into long sequences (up to 10K tokens) with attention masks.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 推理时，视频 token 使用 3 步 Euler 求解器（积分至 $s=0.6$），动作 token 使用 10 步 Euler 求解器（积分至 $s=1.0$）。视频 CFG scale 设为 5.0，动作 CFG scale 设为 1.0。训练期间，以概率 $p=0.5$ 应用噪声增强，且 $s_{\mathrm{aug}}\sim\mathrm{Uniform}[0.5,1.0]$。遵循 LLM 实践，我们使用注意力掩码，把多个 episode 打包成长序列（最多 10K token）。

### Figure 5. 实机部署结果

![Figure 5](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/fig05_real_world_results.png)

**Caption:** Figure 5. Real-world deployment results. We evaluate LingBot-VA on six manipulation tasks across three categories: long-horizon tasks (Make Breakfast, Pick Screws), precision tasks (Insert Tubes, Unpack Delivery), and deformable & articulated object manipulation (Fold Clothes, Fold Pants). Our method achieves state-of-the-art performance on both metrics.

**Caption[CN]:** 图 5. 实机部署结果。我们在三类共六项操作任务上评估 LingBot-VA：长时序任务（Make Breakfast、Pick Screws）、精细操作任务（Insert Tubes、Unpack Delivery），以及可变形和关节物体操作（Fold Clothes、Fold Pants）。本方法在两项指标上均取得最先进性能。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> **Pre-Training Details.** We pretrain LingBot-VA on the curated dataset for 1.4T tokens. We use the AdamW optimizer with peak learning rate $1\times10^{-4}$, weight decay 0.01, and cosine annealing schedule with linear warmup. Training is conducted in bfloat16 mixed precision with gradient clipping at 2.0. We apply classifier-free guidance with text dropout rate 0.1. The loss weight $\lambda$ for inverse dynamics is set to 1. The dataset is sampled uniformly across all sources to ensure balanced learning. We monitor convergence using flow matching loss on the validation set. We use uniform SNR sampler for video model. For both video and action model, we use a uniform SNR sampler.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> **预训练细节。** 我们在整理的数据集上对 LingBot-VA 预训练 1.4T token。优化器采用 AdamW，峰值学习率 $1\times10^{-4}$、权重衰减 0.01，并使用带线性 warmup 的余弦退火调度。训练以 bfloat16 混合精度进行，梯度裁剪阈值为 2.0。我们使用 classifier-free guidance，文本 dropout rate 为 0.1。逆动力学损失权重 $\lambda$ 设为 1。为保证平衡学习，从所有数据来源均匀采样。我们以验证集上的流匹配损失监控收敛。视频模型使用均匀 SNR 采样器；视频模型和动作模型均使用均匀 SNR 采样器。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> **Post-Training Details.** While the pretrained model exhibits zero-shot generalization to seen embodiments, adapting to novel robot platforms requires a small amount of task-specific data. We find that post-training with as few as 50 demonstrations is sufficient for effective deployment. We use a reduced learning rate of $1\times10^{-5}$ and train for 3K steps, which yields robust performance. Alternatively, a higher learning rate of $1\times10^{-4}$ with 1K steps also produces reasonable results, though slightly inferior, offering a faster adaptation option when computational resources are limited.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **后训练细节。** 尽管预训练模型对训练中见过的本体展现出零样本泛化，但适配新机器人平台仍需要少量任务特定数据。我们发现，只需 50 条示范进行后训练就足以有效部署。我们把学习率降低到 $1\times10^{-5}$，训练 3K 步，从而获得稳健性能。另一种方案是使用更高学习率 $1\times10^{-4}$ 训练 1K 步，也能得到合理但略逊的结果；当计算资源有限时，这提供了更快适配选项。

### 4.3 Main Results

#### 4.3.1 Real-world Deployment

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **Experimental Setup.** To validate the real-world effectiveness of LingBot-VA, we deploy our model on a physical robot platform and evaluate across six diverse manipulation tasks spanning three challenging categories. (1) **Long-horizon Tasks:** We evaluate on Make Breakfast and Unpack Delivery, which require sequential multi-step reasoning and sustained task execution over extended time horizons. (2) **Precision Tasks:** We test on Insert Tubes and Pick Screws, demanding accurate positioning and fine-grained motor control for successful completion. (3) **Deformable Objects:** We include Fold Clothes and Fold Pants, which involve manipulating non-rigid materials that present unique control challenges. The detailed task procedures are summarized in Fig. 6. These tasks are only collected with 50 real-world demos for model training. We finetune the model for 500 steps with a learning rate of $1\times10^{-4}$ and a sequence length of 150,000.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **实验设置。** 为验证 LingBot-VA 的现实有效性，我们把模型部署到实体机器人平台，在横跨三类挑战的六项多样操作任务上评估。（1）**长时序任务：** 评估 Make Breakfast 和 Unpack Delivery，它们要求顺序多步推理，并在较长时间跨度上持续执行任务。（2）**精细操作任务：** 测试 Insert Tubes 和 Pick Screws，成功完成要求精确定位和细粒度运动控制。（3）**可变形物体：** 包括 Fold Clothes 和 Fold Pants，它们涉及操作非刚性材料，带来独特控制挑战。详细任务流程见图 6。训练这些任务时仅采集 50 条实机示范。我们以 $1\times10^{-4}$ 的学习率、150,000 的序列长度微调模型 500 步。

### Figure 6. 六项实机任务的详细进程和关键执行步骤

![Figure 6](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/fig06_task_progressions.png)

**Caption:** Figure 6. Detailed task progressions and key execution steps of the six real-world tasks. Each task involves a sequence of manipulation primitives, with scoring criteria detailed in Tables S2 through S4.

**Caption[CN]:** 图 6. 六项实机任务的详细任务进程和关键执行步骤。每项任务都包含一系列操作原语，评分标准详见表 S2 至 S4。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> **Results.** As shown in Fig. 5, LingBot-VA consistently achieves state-of-the-art performance across all six tasks and both evaluation metrics (success rate and progress score), substantially outperforming strong baseline $\pi_{0.5}$.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> **结果。** 如图 5 所示，LingBot-VA 在六项任务以及两项评估指标（成功率与进度分数）上均持续取得最先进性能，显著优于强基线 $\pi_{0.5}$。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> We highlight several key observations that validate our design choices: (1) The superior performance on long-horizon tasks demonstrates that our video-action world model possesses strong temporal memory capabilities. By jointly modeling video and action sequences, the model effectively maintains task context over extended horizons, enabling coherent multi-step reasoning without losing track of intermediate goals. (2) The strong results on precision tasks validate the effectiveness of our unified latent space design. By aligning video and action representations within a shared embedding space, our model achieves tighter coupling between visual perception and motor control, resulting in more accurate and fine-grained action predictions. (3) The robust performance on deformable objects highlights the value of video generation as implicit guidance. The generated video futures provide rich predictive signals about object dynamics and state transitions, which inform the action model to produce more physically plausible manipulation trajectories for challenging non-rigid materials.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> 我们强调若干验证设计选择的关键观察：（1）长时序任务上的更优性能表明，视频-动作世界模型具有强时间记忆能力。通过联合建模视频和动作序列，模型在较长时间跨度上有效维持任务上下文，从而在不遗忘中间目标的情况下进行连贯多步推理。（2）精细操作任务上的强结果验证了统一潜变量空间设计的有效性。通过在共享嵌入空间中对齐视频与动作表征，模型使视觉感知与运动控制结合得更紧密，从而得到更准确、更细粒度的动作预测。（3）可变形物体上的稳健性能突出了视频生成作为隐式指导的价值。生成的未来视频为物体动力学和状态转移提供丰富预测信号，引导动作模型为具有挑战性的非刚性材料生成更符合物理规律的操作轨迹。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> These results collectively demonstrate that our video-action world model effectively transfers to real-world deployment, exhibiting robust performance across diverse manipulation scenarios.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 这些结果共同表明，我们的视频-动作世界模型能够有效迁移到实机部署，并在多样操作场景中表现稳健。

#### 4.3.2 Simulation Evaluation

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> **Experimental Setup.** We evaluate LingBot-VA on two widely-used simulation benchmarks: RoboTwin 2.0 [15] and LIBERO [47], covering diverse manipulation tasks across different robot embodiments.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> **实验设置。** 我们在两个广泛使用的仿真基准 RoboTwin 2.0 [15] 和 LIBERO [47] 上评估 LingBot-VA，它们覆盖不同机器人本体上的多样操作任务。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> (1) In RoboTwin 2.0, we adopt a multi-task training setup [5] where all models are trained on 2,500 demonstrations collected in clean scenes (50 per task) plus 25,000 demonstrations from heavily randomized scenes (500 per task). We downsample the original 50 Hz video to 12.5 Hz while maintaining the action frequency at 50Hz. The model is trained for 50K steps with a learning rate of $1\times10^{-5}$. To facilitate a clearer comparison of performance, we categorize the 50 RoboTwin tasks according to their horizons (e.g., Place Dual Shoes has two steps, and Stack Blocks Three has three steps). The detailed horizons are listed in Tab. S1.

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> （1）在 RoboTwin 2.0 中，我们采用多任务训练设置 [5]：所有模型都在干净场景采集的 2,500 条示范（每项任务 50 条）加上高度随机场景的 25,000 条示范（每项任务 500 条）上训练。我们把原始 50 Hz 视频下采样到 12.5 Hz，同时把动作频率维持在 50Hz。模型以 $1\times10^{-5}$ 的学习率训练 50K 步。为更清晰地比较性能，我们根据 horizon 对 50 项 RoboTwin 任务分类（例如 Place Dual Shoes 有两个步骤，Stack Blocks Three 有三个步骤）。详细 horizon 见表 S1。

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> (2) In LIBERO, we train our model on four LIBERO suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long. Each suite contains 10 tasks with 50 demonstrations per task (500 total). Following OpenVLA [34], we filter unsuccessful demonstrations before training. The model is finetuned for 4K steps with a learning rate of $1\times10^{-5}$ and a sequence length of $1\times10^5$. Specifically, we report the average success rate over three random seeds, with each seed comprising 500 evaluation trials (totally $3\times500=1500$) for every task suite.

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> （2）在 LIBERO 中，我们在四个套件上训练模型：LIBERO-Spatial、LIBERO-Object、LIBERO-Goal 和 LIBERO-Long。每个套件包含 10 项任务，每项任务 50 条示范（总计 500 条）。遵循 OpenVLA [34]，训练前过滤失败示范。模型以 $1\times10^{-5}$ 的学习率和 $1\times10^5$ 的序列长度微调 4K 步。具体而言，我们报告三个随机种子的平均成功率；对每个任务套件，每个种子包含 500 次评估试验（合计 $3\times500=1500$ 次）。

### Table 1. RoboTwin 2.0 仿真评估（Easy vs Hard，50 项任务）

![Table 1](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/table01_robotwin_summary.png)

**Caption:** Table 1. Evaluation on RoboTwin 2.0 Simulation (Easy vs Hard, 50 tasks). RoboTwin 2.0 is a challenging bimanual manipulation benchmark requiring coordinated dual-arm control. Easy uses fixed initial configurations while Hard involves randomized object poses and scene layouts. $^{*}$Results for X-VLA are adopted from Motus [5]. Improvements in parentheses indicate gains over the second-best method (underlined).

**Caption[CN]:** 表 1. RoboTwin 2.0 仿真评估（Easy vs Hard，50 项任务）。RoboTwin 2.0 是要求双臂协调控制的高难度双臂操作基准。Easy 使用固定初始配置，Hard 则包含随机化物体位姿和场景布局。$^{*}$X-VLA 结果取自 Motus [5]。括号中的提升表示相对第二优方法（下划线）的增益。

| Metric | X-VLA$^{*}$ Easy | X-VLA$^{*}$ Hard | $\pi_0$ Easy | $\pi_0$ Hard | $\pi_{0.5}$ Easy | $\pi_{0.5}$ Hard | Motus Easy | Motus Hard | LingBot-VA (Ours) Easy | LingBot-VA (Ours) Hard |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Average Horizon = 1 | 81.6 | 82.5 | 66.5 | 61.6 | 85.1 | 80.2 | 91.0 | 90.6 | **94.18 (+3.2)** | **93.56 (+3.0)** |
| Average Horizon = 2 | 59.3 | 55.9 | 66.1 | 54.7 | 79.3 | 73.0 | 85.2 | 80.9 | **90.35 (+5.2)** | **86.95 (+6.1)** |
| Average Horizon = 3 | 61.2 | 66.0 | 61.6 | 50.2 | 78.6 | 67.4 | 85.0 | 84.2 | **93.22 (+8.2)** | **93.28 (+9.1)** |
| Average 50 Tasks | 72.9 | 72.8 | 65.9 | 58.4 | 82.7 | 76.8 | 88.7 | 87.0 | **92.93 (+4.2)** | **91.55 (+4.6)** |

### Table 2. LIBERO 基准评估

![Table 2](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/table02_libero.png)

**Caption:** Table 2. Evaluation on LIBERO benchmarks. LIBERO tests manipulation across four task suites: Spatial, Object, Goal, and Long-horizon. Our method achieves new state-of-the-art on LIBERO-Object (99.6%), LIBERO-Long (98.5%), LIBERO-Spatial (98.5%), and overall average (98.5%). Baseline results are adopted from [93].

**Caption[CN]:** 表 2. LIBERO 基准评估。LIBERO 在 Spatial、Object、Goal 和 Long-horizon 四个任务套件上测试操作能力。本方法在 LIBERO-Object（99.6%）、LIBERO-Long（98.5%）、LIBERO-Spatial（98.5%）以及总体平均值（98.5%）上取得新的最先进结果。基线结果取自 [93]。

| Method | Spatial | Object | Goal | Long | Avg |
|---|---:|---:|---:|---:|---:|
| Octo [72] | 78.9 | 85.7 | 84.6 | 51.1 | 75.1 |
| Seer [73] | — | — | — | — | 87.7 |
| MoDE [61] | — | — | — | — | 94.0 |
| SuSIE [9] | — | — | — | — | 76.3 |
| SpatialVLA [58] | 88.2 | 89.9 | 78.6 | 55.5 | 78.1 |
| TraceVLA [94] | 84.6 | 85.2 | 75.1 | 54.1 | 74.8 |
| CoT-VLA [90] | 87.5 | 91.6 | 87.6 | 69.0 | 81.1 |
| ThinkAct [28] | 88.3 | 91.4 | 87.1 | 70.9 | 84.4 |
| SmolVLA [67] | 93.0 | 94.0 | 91.0 | 77.0 | 88.8 |
| CronusVLA [37] | 97.3 | **99.6** | 96.9 | 94.0 | 97.0 |
| FLOWER [62] | 97.1 | 96.7 | 95.6 | 93.5 | 95.7 |
| GR00T-N1 [6] | 94.4 | 97.6 | 93.0 | 90.6 | 93.9 |
| $\pi_0$ [7] | 96.8 | 98.8 | 95.8 | 85.2 | 94.1 |
| $\pi_0$+FAST [57] | 96.4 | 96.8 | 88.6 | 60.2 | 85.5 |
| OpenVLA [34] | 84.7 | 88.4 | 79.2 | 53.7 | 76.5 |
| OpenVLA-OFT [32] | 97.6 | 98.4 | **97.9** | 94.5 | 97.1 |
| DD-VLA [44] | 97.2 | 98.6 | 97.4 | 92.0 | 96.3 |
| UniVLA [78] | 95.4 | 98.8 | 93.6 | 94.0 | 95.4 |
| X-VLA [93] | 98.2 | 98.6 | 97.8 | 97.6 | 98.1 |
| **LingBot-VA (Ours)** | **98.5 $\pm$ 0.3** | **99.6 $\pm$ 0.3** | 97.2 $\pm$ 0.2 | **98.5 $\pm$ 0.5** | **98.5** |

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> **Results.** RoboTwin 2.0 is a challenging bimanual manipulation benchmark featuring over 50 tasks that require coordinated dual-arm control. Unlike single-arm benchmarks, RoboTwin tasks demand precise synchronization between two manipulators, making it significantly more difficult for policy learning. We evaluate under both Easy (fixed initial configurations) and Hard (varied object poses and scene layouts) settings. As shown in Tab. 1, LingBot-VA achieves an average success rate of 92.9% (Easy) and 91.6% (Hard), substantially outperforming prior methods including $\pi_0$, $\pi_{0.5}$, X-VLA, and Motus. Notably, the improvement becomes more pronounced for longer-horizon tasks: at Horizon = 3, our method achieves gains of +8.2% (Easy) and +9.1% (Hard) over the second-best approach. This suggests that our autoregressive mechanism effectively maintains long-range temporal memory, enabling more robust performance as task complexity increases.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> **结果。** RoboTwin 2.0 是一项高难度双臂操作基准，包含 50 多项要求双臂协调控制的任务。不同于单臂基准，RoboTwin 任务要求两个机械臂精确同步，因此策略学习难度显著更高。我们同时在 Easy（固定初始配置）与 Hard（变化的物体位姿和场景布局）设置下评估。如表 1 所示，LingBot-VA 的平均成功率达到 92.9%（Easy）和 91.6%（Hard），显著优于 $\pi_0$、$\pi_{0.5}$、X-VLA 和 Motus 等既有方法。值得注意的是，任务 horizon 越长，提升越明显：在 Horizon = 3 时，本方法相对第二优方法提升 +8.2%（Easy）和 +9.1%（Hard）。这表明自回归机制能够有效维持长程时间记忆，使任务复杂度提高时仍可获得更稳健的性能。

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> We further evaluate on LIBERO benchmark (Tab. 2). On LIBERO, we obtain an average success rate of 98.5%, with particularly strong performance on LIBERO-Long (98.5%). These results establish new state-of-the-art performance in average success rates among foundational VLAs, demonstrating the effectiveness of our video-action world model for generalist robot control.

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> 我们还在 LIBERO 基准（表 2）上评估。在 LIBERO 上，平均成功率为 98.5%，其中 LIBERO-Long 表现尤其突出（98.5%）。这些结果在基础 VLA 的平均成功率上建立了新的最先进水平，证明视频-动作世界模型对通用机器人控制有效。

### 4.4 Ablation

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> **Asynchronous v.s. synchronous.** We compare our asynchronous video-action generation with a synchronous baseline on RoboTwin tasks. As shown in Tab. 3, both approaches achieve comparable success rates, but our asynchronous method completes tasks 2$\times$ faster by predicting future video and action sequences while executing current actions. This validates that asynchronous generation maintains task performance while significantly improving inference efficiency.

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> **异步 vs. 同步。** 我们在 RoboTwin 任务上比较异步视频-动作生成与同步基线。如表 3 所示，两种方法成功率相当，但异步方法在执行当前动作时预测未来视频和动作序列，因此完成任务快 2$\times$。这验证了异步生成可以在保持任务性能的同时显著提高推理效率。

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> **Pretrained LingBot-VA v.s. WAN.** To validate the design choices in our video-action architecture, we conduct a controlled ablation study comparing our pretrained LingBot-VA model with WAN (Wan2.2-5B) as the initialization baseline for fine-tuning on RoboTwin tasks. Both models are fine-tuned on the same RoboTwin dataset using identical post-training procedures (50 task-specific demonstrations, learning rate $1\times10^{-5}$, 3K steps).

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> **预训练 LingBot-VA vs. WAN。** 为验证视频-动作架构的设计选择，我们开展受控消融：把预训练 LingBot-VA 与 WAN（Wan2.2-5B）这一用于 RoboTwin 任务微调的初始化基线进行比较。两个模型都在同一 RoboTwin 数据集上使用完全相同的后训练流程微调（50 条任务特定示范、学习率 $1\times10^{-5}$、3K 步）。

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> As shown in Tab. 3, our pretrained LingBot-VA model substantially outperforms WAN fine-tuning across both Easy and Hard settings. Specifically, LingBot-VA achieves an average success rate of 92.10% (Easy) and 91.12% (Hard), while WAN fine-tuning yields significantly lower performance. This performance gap highlights the effectiveness of our joint video-action pretraining strategy, which endows the model with rich visual-motor priors that facilitate fast adaptation to complex bimanual manipulation tasks.

> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> 如表 3 所示，预训练 LingBot-VA 在 Easy 和 Hard 设置下都显著优于 WAN 微调。具体而言，LingBot-VA 的平均成功率为 92.10%（Easy）和 91.12%（Hard），而 WAN 微调性能显著更低。这一性能差距突出了视频-动作联合预训练策略的有效性：它为模型赋予丰富的视觉—运动先验，促进其快速适应复杂双臂操作任务。

### Table 3. RoboTwin 2.0（Easy）消融研究

![Table 3](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/table03_ablation.png)

**Caption:** Table 3. Ablation studies on RoboTwin 2.0 (Easy). We ablate three design choices: world modeling (AR vs. bidirectional), deployment mode (async vs. sync), and pretraining (Ours vs. WAN).

**Caption[CN]:** 表 3. RoboTwin 2.0（Easy）上的消融研究。我们消融三项设计选择：世界建模（AR vs. bidirectional）、部署模式（async vs. sync）以及预训练（Ours vs. WAN）。

| Group | Setting | Easy all | Easy Horizon = 1 | Easy Horizon = 2 | Easy Horizon = 3 |
|---|---|---:|---:|---:|---:|
| Baseline | LingBot-VA (Ours) | **92.9** | **94.2** | **90.4** | **93.2** |
| Deployment | FDM-grounded Async | 90.4 | 92.5 | 87.7 | 85.6 |
| Deployment | Naive Async | 74.3 | 83.3 | 70.3 | 32.9 |
| Pretrain | WAN | 80.6 | 84.9 | 76.3 | 67.6 |

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> **Action Network Initialization.** Proper initialization of the action stream is critical for training stability and convergence. We compare our curated initialization strategy (Section 3.3) with naive random initialization.

> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> **动作网络初始化。** 动作流的恰当初始化对训练稳定性和收敛至关重要。我们把精心设计的初始化策略（第 3.3 节）与朴素随机初始化进行比较。

### Figure 7. 不同动作网络初始化策略的训练动态比较

![Figure 7](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/fig07_initialization.png)

**Caption:** Figure 7. Training dynamic comparison between different action network initialization streategy: Random initialization leads to unstable optimization (high gradient norms) and slow convergence. Although re-using video network weights stabilizes training, the resulting performance is not optimal. Our approach, which initializes by copying pretrained video weights with proper scaling, proves to be the most effective, ensuring smooth training dynamics and faster convergence.

**Caption[CN]:** 图 7. 不同动作网络初始化策略的训练动态比较：随机初始化会导致优化不稳定（梯度范数高）和收敛缓慢。尽管复用视频网络权重能够稳定训练，但最终性能并非最优。我们的方法通过复制预训练视频权重并进行适当缩放来初始化，效果最佳，可确保训练动态平滑并加快收敛。

> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> As shown in Fig. 7, random initialization from scratch exhibits volatile training dynamics with significantly slower convergence. This instability arises because action tokens’ output distribution initially diverges dramatically from the video distribution, disrupting the joint attention mechanism in our unified architecture. In contrast, our curated initialization strategy—where action network weights are initialized by interpolating pretrained video weights with a scaling factor $\alpha=\sqrt{d_v/d_a}$—produces smooth convergence and substantially lower loss.

> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> 如图 7 所示，从头随机初始化会呈现剧烈波动的训练动态，收敛显著更慢。这种不稳定是因为动作 token 的初始输出分布与视频分布差异很大，扰乱了统一架构中的联合注意力机制。相比之下，我们精心设计的初始化策略——用经缩放因子 $\alpha=\sqrt{d_v/d_a}$ 缩放的预训练视频权重插值来初始化动作网络权重——可带来平滑收敛和显著更低的损失。

### 4.5 Analysis

#### 4.5.1 Sample Efficiency

> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> We investigate the data efficiency by exploring how LingBot-VA performs with limited post-training data compared to $\pi_{0.5}$. We conduct this evaluation on both real-world and simulation settings: the “Make Breakfast” long-horizon task and RoboTwin 2.0 Easy benchmarks, allowing us to assess data efficiency across diverse manipulation scenarios.

> <span style="color:#F59E0B"><strong>Para. 23[CN]:</strong></span> 我们通过考察 LingBot-VA 在有限后训练数据下相对 $\pi_{0.5}$ 的表现来研究数据效率。评估同时在现实与仿真设置上进行：长时序任务 “Make Breakfast” 和 RoboTwin 2.0 Easy 基准，从而评估不同操作场景下的数据效率。

### Figure 8. 样本效率比较

![Figure 8](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/fig08_sample_efficiency.png)

**Caption:** Figure 8. Sample efficiency comparison. LingBot-VA consistently outperforms $\pi_{0.5}$ across various data regimes on the “Make Breakfast” task, demonstrating superior data efficiency in the post-training stage.

**Caption[CN]:** 图 8. 样本效率比较。在 “Make Breakfast” 任务的多种数据规模下，LingBot-VA 均持续优于 $\pi_{0.5}$，表明其后训练阶段具有更优数据效率。

> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> As shown in Fig. 8, our method consistently outperforms $\pi_{0.5}$ across all data regimes on both real-world and simulation tasks. In the low-data regime (10 demonstrations), LingBot-VA achieves 15.6% higher progress score than $\pi_{0.5}$ on the “Make Breakfast” task and 10.3% higher on RoboTwin 2.0 Easy, demonstrating superior sample efficiency. These results demonstrate that our method learns more effectively from limited data across diverse manipulation scenarios.

> <span style="color:#F59E0B"><strong>Para. 24[CN]:</strong></span> 如图 8 所示，在现实和仿真任务的所有数据规模下，本方法都持续优于 $\pi_{0.5}$。在低数据设置（10 条示范）中，LingBot-VA 在 “Make Breakfast” 任务上的进度分数比 $\pi_{0.5}$ 高 15.6%，在 RoboTwin 2.0 Easy 上高 10.3%，显示出更优样本效率。这些结果表明，本方法在多样操作场景中能更有效地从有限数据学习。

> <span style="color:#3B82F6"><strong>Para. 25:</strong></span> We attribute this superior data efficiency to our video-action world model design. The jointly pretrained video generation backbone provides rich visual priors about physical dynamics and object interactions, which serve as implicit regularization during post-training. This allows the action model to leverage the world knowledge encoded in the video stream, effectively reducing the sample complexity required for adapting to new tasks. In contrast, VLA models like $\pi_{0.5}$ lack explicit modeling of visual dynamics and thus have no structured dynamics priors to guide learning, requiring more demonstrations to learn task-specific behaviors from scratch.

> <span style="color:#F59E0B"><strong>Para. 25[CN]:</strong></span> 我们把这种更优数据效率归因于视频-动作世界模型设计。联合预训练的视频生成骨干提供关于物理动力学与物体交互的丰富视觉先验，在后训练中发挥隐式正则化作用。这使动作模型能够利用视频流中编码的世界知识，有效降低适应新任务所需的样本复杂度。相比之下，$\pi_{0.5}$ 等 VLA 模型缺乏显式视觉动态建模，因此没有结构化动力学先验指导学习，需要更多示范才能从头学习任务特定行为。

#### 4.5.2 Temporal Memory

> <span style="color:#3B82F6"><strong>Para. 26:</strong></span> We design the following tasks that explicitly require maintaining state information across time to evaluate our model’s temporal memory capabilities, as shown in Figure 9.
>
> 1. **Wipe Plate**—the robot must wipe a plate exactly six times, requiring it to count and remember repeated actions.
> 2. **Search Box**—Two boxes (left and right) are in the scene, with only one containing a block. The robot opens them sequentially from right to left. In data collection, the block is equally likely to be in either box; at test time, it is always in the left box. Without memory, after finding the right box empty, the model has a 50% chance of re-opening it. With memory, it proceeds to search the left box.

> <span style="color:#F59E0B"><strong>Para. 26[CN]:</strong></span> 如图 9 所示，我们设计了下列显式要求跨时间维持状态信息的任务，用于评估模型的时间记忆能力。
>
> 1. **Wipe Plate**——机器人必须恰好擦拭盘子六次，需要计数并记住重复动作。
> 2. **Search Box**——场景中有两个盒子（左、右），只有一个装有积木。机器人从右到左依次打开盒子。采集数据时，积木位于任一盒子的概率相同；测试时则总在左盒。若没有记忆，模型发现右盒为空后有 50% 概率再次打开它；若有记忆，则会继续搜索左盒。

### Figure 9. 时间记忆评估

![Figure 9](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/fig09_memory.png)

**Caption:** Figure 9. Temporal memory evaluation. Left: Success rates on two memory tasks (Wipe Plate and Search Box). LingBot-VA significantly outperforms $\pi_{0.5}$ on both tasks, demonstrating superior temporal state tracking ability. Right: Visualization of evaluation environments.

**Caption[CN]:** 图 9. 时间记忆评估。左：两项记忆任务（Wipe Plate 和 Search Box）的成功率。LingBot-VA 在两项任务上均显著优于 $\pi_{0.5}$，表明其具有更优时间状态跟踪能力。右：评估环境可视化。

> <span style="color:#3B82F6"><strong>Para. 27:</strong></span> As shown in Fig. 9(a), LingBot-VA substantially outperforms $\pi_{0.5}$ on both memory tasks. We attribute this to the autoregressive nature of our world model: during training, teacher forcing conditions predictions on full history; during inference, KV-cache naturally preserves all historical information for persistent memory.

> <span style="color:#F59E0B"><strong>Para. 27[CN]:</strong></span> 如图 9(a) 所示，LingBot-VA 在两项记忆任务上均显著优于 $\pi_{0.5}$。我们把这一优势归因于世界模型的自回归性质：训练时，教师强制使预测以完整历史为条件；推理时，KV 缓存天然保留全部历史信息，从而形成持久记忆。

#### 4.5.3 Generalization

> <span style="color:#3B82F6"><strong>Para. 28:</strong></span> We evaluate generalization along two axes:
>
> 1. **Novel Object Generalization**—trained on pick-and-place with a single object, tested on different objects with varying shapes and textures;
> 2. **Spatial Generalization**—trained with fixed object positions in a localized region (denoted as in-distribution (ID)), tested on random placements especially in out-of-distribution (OOD) regions.

> <span style="color:#F59E0B"><strong>Para. 28[CN]:</strong></span> 我们沿两个轴评估泛化：
>
> 1. **新物体泛化**——在单一物体的取放任务上训练，在形状和纹理各异的不同物体上测试；
> 2. **空间泛化**——在局部区域中的固定物体位置上训练（称为分布内（ID）），在随机摆放位置上测试，尤其关注分布外（OOD）区域。

### Figure 10. 新物体与空间泛化

![Figure 10](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/fig10_generalization.png)

**Caption:** Figure 10. Novel object and spatial generalization. LingBot-VA successfully generalizes to objects with varying shapes, textures, and positions.

**Caption[CN]:** 图 10. 新物体与空间泛化。LingBot-VA 成功泛化到形状、纹理和位置各异的物体。

> <span style="color:#3B82F6"><strong>Para. 29:</strong></span> As shown in Fig. 10, our method demonstrates a stronger generalization in both both novel object and the out-of-distribution position. The world model learns transferable visual representations through video prediction, capturing object-agnostic physical priors that transfer to novel scenarios.

> <span style="color:#F59E0B"><strong>Para. 29[CN]:</strong></span> 如图 10 所示，本方法在新物体和分布外位置两方面均展现出更强泛化。世界模型通过视频预测学习可迁移视觉表征，捕获与具体物体无关、可迁移到新场景的物理先验。

## 5 Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Vision-Language-Action Policies.** Recent advancements in Embodied AI have witnessed a paradigm shift toward large-scale Vision-Language-Action (VLA) policies. By leveraging web-scale knowledge and diverse robot demonstrations, models such as $\pi_{0.5}$ [29], GR-3 [39], and GR00T-N1 [6] achieve remarkable generalizability across various manipulation tasks without relying on hand-crafted rules, modular priors, or restricted action abstractions, enabling a more direct and expressive end-to-end mapping from perception to control. These policies typically employ pre-trained Vision-Language Models (VLMs) as foundational backbones [6, 7, 11, 29, 34, 39, 87, 93], which provide superior cross-modal understanding and more generalizable action distributions compared to task-specific imitation policies like ACT [91] or Diffusion Policy [17]. Efforts have been further devoted to improving the deployability through lightweight backbones [49, 62, 67], efficient tokenization [57], real-time inference [8, 10, 70], or fine-tuning schemes [30, 32, 38]. However, despite their prowess in semantic reasoning, a fundamental limitation persists: the pre-training objectives and data distributions of standard VLMs largely overlook the fine-grained system dynamics and low-level trajectories essential for precision manipulation. While supervised fine-tuning on expensively collected large-scale robot datasets allows these models to approximate the marginal action distribution [3, 31, 53], they remain deficient in capturing the underlying transition dynamics—specifically, how the physical state of the environment should evolve and will evolve.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **视觉-语言-动作策略。** 具身 AI 的近期进展见证了向大规模视觉-语言-动作（VLA）策略的范式转移。通过利用网络规模知识和多样机器人示范，$\pi_{0.5}$ [29]、GR-3 [39]、GR00T-N1 [6] 等模型无需依赖手工规则、模块化先验或受限动作抽象，就能在多种操作任务上取得出色泛化，从而实现从感知到控制更直接、更具表达力的端到端映射。这些策略通常采用预训练视觉-语言模型（VLM）作为基础骨干 [6, 7, 11, 29, 34, 39, 87, 93]；相较 ACT [91] 或 Diffusion Policy [17] 等任务特定模仿策略，VLM 提供更优跨模态理解与更可泛化的动作分布。研究还通过轻量骨干 [49, 62, 67]、高效 token 化 [57]、实时推理 [8, 10, 70] 或微调方案 [30, 32, 38] 进一步改善可部署性。然而，尽管它们擅长语义推理，一项根本限制仍然存在：标准 VLM 的预训练目标和数据分布在很大程度上忽略了精细操作必需的细粒度系统动力学和低层轨迹。尽管在昂贵采集的大规模机器人数据集上进行监督微调，能让这些模型近似边缘动作分布 [3, 31, 53]，它们仍不善于捕获底层转移动力学——具体而言，即环境物理状态应当如何演化以及将会如何演化。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Furthermore, most current VLA methods formulate control as a purely reactive mapping from instantaneous observations to actions. This approach inherently fails to account for the historical context necessary to resolve ambiguities in non-Markovian environments. Additionally, the static image-text pre-training inherent in VLMs fails to instill essential temporal priors. Even when augmented with memory modules [37, 65, 68], such models remain unable to reason about the causal and sequential nature of physical interactions. To address these shortcomings, recent research has pivoted towards generalist robot policies grounded in world models and generative video modeling [1, 5, 40, 64, 97]. However, these methods typically generate predictions with bidirectional attention, which violates the causal structure of physical dynamics and lacks persistent long-term memory across the full execution history. Our LingBot-VA unifies autoregressive video prediction with action decoding under a strict causal temporal structure, where each prediction conditions exclusively on past observations and actions. By maintaining a persistent KV cache over the complete interaction history, LingBot-VA ensures long-range temporal consistency and allows the policy to synchronize physical execution with the predicted visual evolution of the environment.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 此外，多数当前 VLA 方法把控制表述为从瞬时观测到动作的纯反应式映射。该方法天然无法纳入解决非马尔可夫环境歧义所必需的历史上下文。VLM 固有的静态图像—文本预训练也无法赋予必要的时间先验。即使加入记忆模块 [37, 65, 68]，这类模型仍无法推理物理交互的因果与顺序本质。为解决这些缺陷，近期研究转向以世界模型和生成式视频建模为基础的通用机器人策略 [1, 5, 40, 64, 97]。然而，这些方法通常用双向注意力生成预测，违反物理动力学的因果结构，且无法在完整执行历史上维持持久长期记忆。LingBot-VA 在严格因果时间结构下统一自回归视频预测与动作解码，每项预测都只以过去观测和动作为条件。通过在完整交互历史上维持持久 KV 缓存，LingBot-VA 确保长程时间一致性，并允许策略同步物理执行与预测的环境视觉演化。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **World Models for Robotic Control.** Inspired by human reliance on intuitive physics to anticipate environmental changes, world models aim to facilitate effective planning by predicting future dynamics. Existing approaches are generally categorized into three groups based on their state representations. The first category operates in latent space [36, 41, 63, 80], encoding task-relevant features into compact vectors to predict evolution via probabilistic [36, 52, 83] or deterministic methods [63, 85]. The second category utilizes 3D point clouds [66, 69, 77], leveraging Graph Neural Networks (GNNs) to predict geometric evolution [88, 89], which is particularly effective for manipulating deformable objects [77, 89]. The third category focuses on 2D pixel space, directly predicting future keyframes or video sequences [21, 33, 95, 96]. Our work aligns with this third category. Within this domain, approaches range from co-training with video generation for representation learning [14, 40, 97] to serving as simulators for policy learning or evaluation [71]. Our research specifically targets methods that predict future frames during execution to condition action generation.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **用于机器人控制的世界模型。** 人类依靠直觉物理预测环境变化，受此启发，世界模型旨在通过预测未来动态促进有效规划。现有方法通常可按状态表征分为三类。第一类在潜变量空间中运行 [36, 41, 63, 80]，把任务相关特征编码为紧凑向量，再使用概率方法 [36, 52, 83] 或确定性方法 [63, 85] 预测演化。第二类采用 3D 点云 [66, 69, 77]，利用图神经网络（GNN）预测几何演化 [88, 89]，尤其适合操作可变形物体 [77, 89]。第三类聚焦 2D 像素空间，直接预测未来关键帧或视频序列 [21, 33, 95, 96]。本工作属于第三类。在该领域内，方法既包括与视频生成共同训练以学习表征 [14, 40, 97]，也包括充当用于策略学习或评估的模拟器 [71]。本研究特别关注在执行期间预测未来帧、以此为动作生成提供条件的方法。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> However, prior video-conditioned methods predominantly rely on open-loop generation [21, 95], presenting two significant challenges. First, the misalignment between generated videos and real-world dynamics, coupled with cumulative drift from execution errors, often leads to suboptimal performance. Second, the computational intensity of video generation imposes high latency, severely hindering real-time inference. Our method leverages KV Cache and causal masking to continuously update the model’s memory with real-world observations. This effectively transitions the system to a closed-loop control mechanism, mitigating error accumulation in long-horizon tasks. Furthermore, we introduce a partial denoising strategy, enabling action generation from intermediate representations without waiting for fully denoised frames.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 然而，既有视频条件方法主要依赖开环生成 [21, 95]，由此产生两项重大挑战。第一，生成视频与真实世界动态之间存在失配，再叠加执行误差造成的累积漂移，往往导致次优性能。第二，视频生成计算量巨大，带来高延迟，严重阻碍实时推理。本方法利用 KV 缓存和因果掩码，以真实观测持续更新模型记忆。这使系统有效转变为闭环控制机制，减轻长时序任务中的误差累积。此外，我们引入部分去噪策略，使模型无需等待帧完全去噪，就可从中间表征生成动作。

## 6 Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We present LingBot-VA, an autoregressive diffusion framework that unifies video dynamics prediction and action inference for robotic manipulation. By interleaving video and action tokens within a Mixture-of-Transformers architecture, our model captures the causal structure of physical interactions while enabling closed-loop control through continuous integration of real-world observations. Extensive evaluation demonstrates strong performance across simulation benchmarks (92.0% on RoboTwin 2.0, 98.5% on LIBERO) and real-world deployment, achieving over 20% improvement on challenging tasks compared to $\pi_{0.5}$ with only 50 demonstrations for adaptation. These results suggest that autoregressive video-action world modeling provides a principled foundation for learning generalizable manipulation policies, offering a compelling alternative to reactive VLA paradigms.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们提出 LingBot-VA，这是一种面向机器人操作、统一视频动态预测与动作推断的自回归扩散框架。通过在 Transformer 混合架构中交错视频 token 和动作 token，模型能够捕获物理交互的因果结构，并通过持续整合现实观测实现闭环控制。广泛评估表明，该模型在仿真基准（RoboTwin 2.0 上 92.0%，LIBERO 上 98.5%）和实机部署中均表现强劲；只用 50 条示范进行适配，就在高难度任务上相对 $\pi_{0.5}$ 提升超过 20%。这些结果表明，自回归视频-动作世界建模为学习可泛化操作策略提供了原则性基础，是反应式 VLA 范式的一项有力替代方案。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Future Work.** Future directions include developing more efficient video compression schemes to reduce computational overhead, and incorporating multi-modal sensory inputs (tactile, force, audio) for more robust manipulation in tasks with complex contact dynamics.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **未来工作。** 未来方向包括开发更高效的视频压缩方案来降低计算开销，以及纳入多模态传感输入（触觉、力觉、音频），以便在具有复杂接触动力学的任务中实现更稳健的操作。

### Acknowledgment

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Acknowledgment. We thank Kecheng Zheng for insightful discussions and Wei Wu for valuable assistance with dataset preparation. We also thank Fangyi Xu and Yishu Shen for their help with the post-training data collection.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 致谢。我们感谢 Kecheng Zheng 提供富有洞见的讨论，感谢 Wei Wu 在数据集准备方面给予宝贵协助。我们还感谢 Fangyi Xu 和 Yishu Shen 帮助采集后训练数据。

## References

**Reference policy note:** The following bibliography preserves all 97 original English entries in searchable form. Bibliographic entries are not given `Para.` labels and are not translated individually, so names, titles, venues, years, arXiv identifiers, and URLs remain standard and auditable.

[1] 1X Technologies. 1x world model: From video to action. https://www.1x.tech/discover/world-model-self-learning,
2025. Accessed 2026-01-18.
[2] AgiBot-World-Contributors, Qingwen Bu, Jisong Cai, Li Chen, Xiuqi Cui, Yan Ding, Siyuan Feng, Shenyuan Gao, Xindong
He, Xuan Hu, Xu Huang, Shu Jiang, Yuxin Jiang, Cheng Jing, Hongyang Li, et al. Agibot world colosseo: A large-scale
manipulation platform for scalable and intelligent embodied systems. arXiv preprint arXiv:2503.06669, 2025.
[3] Jose Barreiros, Andrew Beaulieu, Aditya Bhat, Rick Cory, Eric Cousineau, Hongkai Dai, Ching-Hsin Fang, Kunimatsu
Hashimoto, Muhammad Zubair Irshad, Masha Itkina, et al. A careful examination of large behavior models for multitask
dexterous manipulation. arXiv preprint arXiv:2507.05331, 2025.
[4] Homanga Bharadhwaj, Debidatta Dwibedi, Abhinav Gupta, Shubham Tulsiani, Carl Doersch, Ted Xiao, Dhruv Shah, Fei
Xia, Dorsa Sadigh, and Sean Kirmani. Gen2act: Human video generation in novel scenarios enables generalizable robot
manipulation. In Conference on Robot Learning (CoRL), 2024.
[5] Hongzhe Bi, Hengkai Tan, Shenghao Xie, Zeyuan Wang, Shuhe Huang, Haitian Liu, Ruowen Zhao, Yao Feng, Chendong
Xiang, Yinze Rong, Hongyan Zhao, Hanyu Liu, Zhizhong Su, Lei Ma, Hang Su, et al. Motus: A unified latent action world
model. arXiv preprint arXiv:2512.13030, 2025.
[6] Johan Bjorck, Fernando Castañeda, Nikita Cherniadev, Xingye Da, Runyu Ding, Linxi Jim Fan, Yu Fang, Dieter Fox, Fengyuan
Hu, Spencer Huang, Joel Jang, Zhenyu Jiang, Jan Kautz, Kaushil Kundalia, Lawrence Lao, et al. Gr00t n1: An open foundation
model for generalist humanoid robots. arXiv preprint arXiv:2503.14734, 2025.
[7] Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, Lachy Groom, Karol
Hausman, Brian Ichter, Szymon Jakubczak, Tim Jones, Liyiming Ke, Sergey Levine, Adrian Li-Bell, et al. π0: A vision-
language-action flow model for general robot control. In Robotics: Science and Systems, 2025.
[8] Kevin Black, Manuel Y. Galliker, and Sergey Levine. Real-time execution of action chunking flow policies. arXiv preprint
arXiv:2506.07339, 2025.
[9] Kevin Black, Mitsuhiko Nakamoto, Pranav Atreya, Homer Walke, Chelsea Finn, Aviral Kumar, and Sergey Levine. Zero-shot
robotic manipulation with pretrained image-editing diffusion models. In Int. Conf. Learn. Represent., 2024.
[10] Kevin Black, Allen Z Ren, Michael Equi, and Sergey Levine. Training-time action conditioning for efficient real-time chunking.
arXiv preprint arXiv:2512.05964, 2025.
[11] Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding, Danny
Driess, Avinava Dubey, Chelsea Finn, Pete Florence, Chuyuan Fu, Montse Gonzalez Arenas, Keerthana Gopalakrishnan,
Kehang Han, et al. Rt-2: Vision-language-action models transfer web knowledge to robotic control. In Conference on Robot
Learning (CoRL), 2023.
[12] Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Joseph Dabis, Chelsea Finn, Keerthana Gopalakrishnan,
Karol Hausman, Alex Herzog, Jasmine Hsu, Julian Ibarz, Brian Ichter, Alex Irpan, Tomas Jackson, Sally Jesmonth, et al. Rt-1:
Robotics transformer for real-world control at scale. In Robotics: Science and Systems, 2023.
[13] Jake Bruce, Michael Dennis, Ashley Edwards, Jack Parker-Holder, Yuge Shi, Edward Hughes, Matthew Lai, Aditi Mavalankar,
Richie Steigerwald, Chris Apps, Yusuf Aytar, Sarah Bechtle, Feryal Behbahani, Stephanie Chan, Nicolas Heess, et al. Genie:
Generative interactive environments. In Int. Conf. Mach. Learn., 2024.
[14] Qingwen Bu, Yanting Yang, Jisong Cai, Shenyuan Gao, Guanghui Ren, Maoqing Yao, Ping Luo, and Hongyang Li. Learning to
act anywhere with task-centric latent actions. arXiv preprint arXiv:2502.14420, 2025.
[15] Tianxing Chen, Zanxin Chen, Baijun Chen, Zijian Cai, Yibin Liu, Zixuan Li, Qiwei Liang, Xianliang Lin, Yiheng Ge, Zhenyu
Gu, Weiliang Deng, Yubin Guo, Tian Nian, Xuanbing Xie, Qiangyu Chen, et al. Robotwin 2.0: A scalable data generator and
benchmark with strong domain randomization for robust bimanual robotic manipulation. arXiv preprint arXiv:2506.18088,
2025.
[16] Yi Chen, Yuying Ge, Weiliang Tang, Yizhuo Li, Yixiao Ge, Mingyu Ding, Ying Shan, and Xihui Liu. Moto: Latent motion
token as the bridging language for robot manipulation. In Int. Conf. Comput. Vis., 2025.
[17] Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, and Shuran Song. Diffusion policy:
Visuomotor policy learning via action diffusion. In Robotics: Science and Systems, 2023.
[18] Cheng Chi, Zhenjia Xu, Chuer Pan, Eric Cousineau, Benjamin Burchfiel, Siyuan Feng, Russ Tedrake, and Shuran Song.
Universal manipulation interface: In-the-wild robot teaching without in-the-wild robots. In Robotics: Science and Systems,
2024.
[19] Chaorui Deng, Deyao Zhu, Kunchang Li, Chenhui Gou, Feng Li, Zeyu Wang, Shu Zhong, Weihao Yu, Xiaonan Nie, Ziang
Song, Guang Shi, and Haoqi Fan. Emerging properties in unified multimodal pretraining. arXiv preprint arXiv:2505.14683,
2025.
[20] Yilun Du, Mengjiao Yang, Bo Dai, Hanjun Dai, Ofir Nachum, Joshua B. Tenenbaum, Dale Schuurmans, and Pieter Abbeel.
Learning universal policies via text-guided video generation. In Adv. Neural Inform. Process. Syst., 2023.
[21] Yilun Du, Sherry Yang, Bo Dai, Hanjun Dai, Ofir Nachum, Josh Tenenbaum, Dale Schuurmans, and Pieter Abbeel. Learning
universal policies via text-guided video generation. Advances in neural information processing systems, 36:9156–9172, 2023.
[22] Yao Feng, Hengkai Tan, Xinyi Mao, Guodong Liu, Shuhe Huang, Chendong Xiang, Hang Su, and Jun Zhu. Vidar: Embodied
video diffusion model for generalist bimanual manipulation. arXiv preprint arXiv:2507.12898, 2025.
[23] Google DeepMind. Veo: A text-to-video generation system. Google DeepMind Technical Report, 2025.
[24] Yanjiang Guo, Yucheng Hu, Jianke Zhang, Yen-Jen Wang, Xiaoyu Chen, Chaochao Lu, and Jianyu Chen. Prediction with
action: Visual policy learning via joint denoising process. In Adv. Neural Inform. Process. Syst., 2024.
[25] Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, and Timothy Lillicrap. Mastering diverse control tasks through world models.
Nature, 2025.
[26] Nicklas Hansen, Hao Su, and Xiaolong Wang. Td-mpc2: Scalable, robust world models for continuous control. In Int. Conf.
Learn. Represent., 2024.
[27] Yucheng Hu, Yanjiang Guo, Pengchao Wang, Xiaoyu Chen, Yen-Jen Wang, Jianke Zhang, Koushil Sreenath, Chaochao Lu,
and Jianyu Chen. Video prediction policy: A generalist robot policy with predictive visual representations. In Int. Conf. Mach.
Learn., 2025.
[28] Chi-Pin Huang, Yueh-Hua Wu, Min-Hung Chen, Yu-Chiang Frank Wang, and Fu-En Yang. Thinkact: Vision-language-action
reasoning via reinforced visual latent planning. In Adv. Neural Inform. Process. Syst., 2025.
[29] Physical Intelligence et al. π0.5: A generalist robot policy with flow matching and world models. In Conference on Robot
Learning (CoRL), 2025.
[30] Dong Jing, Gang Wang, Jiaqi Liu, Weiliang Tang, Zelong Sun, Yunchao Yao, Zhenyu Wei, Yunhui Liu, Zhiwu Lu, and Mingyu
Ding. Mixture of horizons in action chunking. arXiv preprint arXiv:2511.19433, 2025.
[31] Alexander Khazatsky, Karl Pertsch, Suraj Nair, Ashwin Balakrishna, Sudeep Dasari, Siddharth Karamcheti, Soroush Nasiriany,
Mohan Kumar Srirama, Lawrence Yunliang Chen, Kirsty Ellis, Peter David Fagan, Joey Hejna, Masha Itkina, Marion Lepert,
Yecheng Jason Ma, et al. Droid: A large-scale in-the-wild robot manipulation dataset. In Robotics: Science and Systems, 2024.
[32] Moo Jin Kim, Chelsea Finn, and Percy Liang. Fine-tuning vision-language-action models: Optimizing speed and success. arXiv
preprint arXiv:2502.19645, 2025.
[33] Moo Jin Kim, Yihuai Gao, Tsung-Yi Lin, Yen-Chen Lin, Yunhao Ge, Grace Lam, Percy Liang, Shuran Song, Ming-Yu
Liu, Chelsea Finn, et al. Cosmos policy: Fine-tuning video models for visuomotor control and planning. arXiv preprint
arXiv:2601.16163, 2026.
[34] Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov, Ethan Foster,
Grace Lam, Pannag Sanketi, Quan Vuong, Thomas Kollar, Benjamin Burchfiel, Russ Tedrake, Dorsa Sadigh, et al. Openvla: An
open-source vision-language-action model. In Conference on Robot Learning (CoRL), 2024.
[35] Kuaishou. Kling ai. https://klingai.kuaishou.com/, 2024.
[36] Chenchang Li, Zihao Ai, Tong Wu, Xiaosa Li, Wenbo Ding, and Huazhe Xu. Deformnet: Latent space modeling and dynamics
prediction for deformable object manipulation. In 2024 IEEE International Conference on Robotics and Automation (ICRA),
pages 14770–14776. IEEE, 2024.
[37] Hao Li, Shuai Yang, Yilun Chen, Yang Tian, Xiaoda Yang, Xinyi Chen, Hanqing Wang, Tai Wang, Feng Zhao, Dahua Lin, et al.
Cronusvla: Transferring latent motion across time for multi-frame prediction in manipulation. arXiv preprint arXiv:2506.19816,
2025.
[38] Haozhan Li, Yuxin Zuo, Jiale Yu, Yuhao Zhang, Zhaohui Yang, Kaiyan Zhang, Xuekai Zhu, Yuchen Zhang, Tianxing Chen,
Ganqu Cui, et al. Simplevla-rl: Scaling vla training via reinforcement learning. arXiv preprint arXiv:2509.09674, 2025.
[39] Jiacheng Li, Mengzhou Sun, Bowen Zhang, Zhe Zhao, Xiu Liu, et al. Gr-3 technical report. arXiv preprint arXiv:2507.15493,
2025.
[40] Shuang Li, Yihuai Gao, Dorsa Sadigh, and Shuran Song. Unified video action model. In Robotics: Science and Systems, 2025.
[41] Yunzhu Li, Jiajun Wu, Jun-Yan Zhu, Joshua B Tenenbaum, Antonio Torralba, and Russ Tedrake. Propagation networks for
model-based control under partial observation. In 2019 International Conference on Robotics and Automation (ICRA), pages
1205–1211. IEEE, 2019.
[42] Junbang Liang, Ruoshi Liu, Ege Ozguroglu, Sruthi Sudhakar, Achal Dave, Pavel Tokmakov, Shuran Song, and Carl Vondrick.
Dreamitate: Real-world visuomotor policy learning via video generation. In Conference on Robot Learning (CoRL), 2024.
[43] Weixin Liang, LILI YU, Liang Luo, Srini Iyer, Ning Dong, Chunting Zhou, Gargi Ghosh, Mike Lewis, Wen tau Yih, Luke
Zettlemoyer, and Xi Victoria Lin. Mixture-of-transformers: A sparse and scalable architecture for multi-modal foundation
models. Transactions on Machine Learning Research, 2025.
[44] Zhixuan Liang, Yizhuo Li, Tianshuo Yang, Chengyue Wu, Sitong Mao, Tian Nian, Liuao Pei, Shunbo Zhou, Xiaokang
Yang, Jiangmiao Pang, Yao Mu, and Ping Luo. Discrete diffusion vla: Bringing discrete diffusion to action decoding in
vision-language-action policies. arXiv preprint arXiv:2508.20072, 2025.
[45] Fanqi Lin, Yingdong Hu, Pingyue Sheng, Chuan Wen, Jiacheng You, and Yang Gao. Data scaling laws in imitation learning for
robotic manipulation. In Int. Conf. Learn. Represent., 2025.
[46] Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel, and Matt Le. Flow matching for generative modeling.
In Int. Conf. Learn. Represent., 2023.
[47] Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, and Peter Stone. Libero: Benchmarking knowledge
transfer for lifelong robot learning. In Adv. Neural Inform. Process. Syst., 2023.
[48] Fangchen Liu, Chuanyu Li, Yihua Qin, Austin Shaw, Jing Xu, Pieter Abbeel, and Rui Chen. Vitamin: Learning contact-rich
tasks through robot-free visuo-tactile manipulation interface. arXiv preprint arXiv:2504.06156, 2025.
[49] Songming Liu, Lingxuan Wu, Bangguo Li, Hengkai Tan, Huayu Chen, Zhengyi Wang, Ke Xu, Hang Su, and Jun Zhu. Rdt-1b:
A diffusion foundation model for bimanual manipulation. In Int. Conf. Learn. Represent., 2025.
[50] Xingchao Liu, Chengyue Gong, and Qiang Liu. Flow straight and fast: Learning to generate and transfer data with rectified
flow. In Int. Conf. Learn. Represent., 2023.
[51] Zeyi Liu, Cheng Chi, Eric Cousineau, Naveen Kuppuswamy, Benjamin Burchfiel, and Shuran Song. Maniwav: Learning robot
manipulation from in-the-wild audio-visual data. arXiv preprint arXiv:2406.19464, 2024.
[52] Bethany Lusch, J Nathan Kutz, and Steven L Brunton. Deep learning for universal linear embeddings of nonlinear dynamics.
Nature communications, 9(1):4950, 2018.
[53] Open X-Embodiment Collaboration. Open x-embodiment: Robotic learning datasets and rt-x models. In IEEE International
Conference on Robotics and Automation (ICRA), 2024.
[54] OpenAI. Video generation models as world simulators. OpenAI Technical Report, 2024.
[55] Jonas Pai, Liam Achenbach, Victoriano Montesinos, Benedek Forrai, Oier Mees, and Elvis Nava. mimic-video: Video-action
models for generalizable robot control beyond vlas. arXiv preprint 2512.15692, 2025.
[56] Jack Parker-Holder, Philip Ball, Jake Bruce, Vibhavari Dasagi, Kristian Holsheimer, Christos Kaplanis, Alexandre
Moufarek, Guy Scully, Jeremy Shar, Jimmy Shi, Stephen Spencer, Jessica Yung, Michael Dennis, Sultan Kenjeyev,
Shangbang Long, et al. Genie 2: A large-scale foundation world model. https://deepmind.google/discover/blog/
genie-2-a-large-scale-foundation-world-model/, 2024.
[57] Karl Pertsch, Kyle Stachowicz, Brian Ichter, Danny Driess, Suraj Nair, Quan Vuong, Oier Mees, Chelsea Finn, and Sergey
Levine. Fast: Efficient action tokenization for vision-language-action models. In Robotics: Science and Systems, 2025.
[58] Delin Qu, Haoming Song, Qizhi Chen, Yuanqi Yao, Xinyi Ye, Yan Ding, Zhigang Wang, JiaYuan Gu, Bin Zhao, Dong Wang,
and Xuelong Li. Spatialvla: Exploring spatial representations for visual-language-action model. In Robotics: Science and
Systems, 2025.
[59] Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael Matena, Yanqi Zhou, Wei Li, and Peter J.
Liu. Exploring the limits of transfer learning with a unified text-to-text transformer. Journal of Machine Learning Research,
21(140):1–67, 2020.
[60] Omar Rayyan, John Abanes, Mahmoud Hafez, Anthony Tzes, and Fares Abu-Dakka. Mv-umi: A scalable multi-view interface
for cross-embodiment learning. arXiv preprint arXiv:2509.18757, 2025.
[61] Moritz Reuss, Jyothish Pari, Pulkit Agrawal, and Rudolf Lioutikov. Efficient diffusion transformer policies with mixture of
expert denoisers for multitask learning. In Int. Conf. Learn. Represent., 2025.
[62] Moritz Reuss, Hongyi Zhou, Marcel Rühle, Ömer Erdinç Ya˘gmurlu, Fabian Otto, and Rudolf Lioutikov. Flower: Democratizing
generalist robot policies with efficient vision-language-action flow policies. In Conference on Robot Learning (CoRL), 2025.
[63] Bokui Shen, Zhenyu Jiang, Christopher Choy, Silvio Savarese, Leonidas J Guibas, Anima Anandkumar, and Yuke Zhu. Action-
conditional implicit visual dynamics for deformable object manipulation. The International Journal of Robotics Research,
43(4):437–455, 2024.
[64] Yichao Shen, Fangyun Wei, Zhiying Du, Yaobo Liang, Yan Lu, Jiaolong Yang, Nanning Zheng, and Baining Guo. Videovla:
Video generators can be generalizable robot manipulators. arXiv preprint arXiv:2512.06963, 2025.
[65] Hao Shi, Bin Xie, Yingfei Liu, Lin Sun, Fengrong Liu, Tiancai Wang, Erjin Zhou, Haoqiang Fan, Xiangyu Zhang, and Gao
Huang. Memoryvla: Perceptual-cognitive memory in vision-language-action models for robotic manipulation. arXiv preprint
arXiv:2508.19236, 2025.
[66] Haochen Shi, Huazhe Xu, Zhiao Huang, Yunzhu Li, and Jiajun Wu. Robocraft: Learning to see, simulate, and shape elasto-
plastic objects in 3d with graph networks. The International Journal of Robotics Research, 43(4):533–549, 2024.
[67] Mustafa Shukor, Dana Aubakirova, Francesco Capuano, Pepijn Kooijmans, Steven Palma, Adil Zouitine, Michel Aractingi,
Caroline Pascal, Martino Russi, Andres Marafioti, Simon Alibert, Matthieu Cord, Thomas Wolf, and Remi Cadene. Smolvla: A
vision-language-action model for affordable and efficient robotics. arXiv preprint arXiv:2506.01844, 2025.
[68] Ajay Sridhar, Jennifer Pan, Satvik Sharma, and Chelsea Finn. Memer: Scaling up memory for robot control via experience
retrieval. arXiv preprint arXiv:2510.20328, 2025.
[69] Deborah Sulsky, Shi-Jian Zhou, and Howard L Schreyer. Application of a particle-in-cell method to solid mechanics. Computer
physics communications, 87(1-2):236–252, 1995.
[70] Jiaming Tang, Yufei Sun, Yilong Zhao, Shang Yang, Yujun Lin, Zhuoyang Zhang, James Hou, Yao Lu, Zhijian Liu, and Song
Han. Vlash: Real-time vlas via future-state-aware asynchronous inference. arXiv preprint arXiv:2512.01031, 2025.
[71] Gemini Robotics Team, Coline Devin, Yilun Du, Debidatta Dwibedi, Ruiqi Gao, Abhishek Jindal, Thomas Kipf, Sean Kirmani,
Fangchen Liu, Anirudha Majumdar, et al. Evaluating gemini robotics policies in a veo world simulator. arXiv preprint
arXiv:2512.10675, 2025.
[72] Octo Model Team, Dibya Ghosh, Homer Walke, Karl Pertsch, Kevin Black, Oier Mees, Sudeep Dasari, Joey Hejna, Tobias
Kreiman, Charles Xu, Jianlan Luo, You Liang Tan, Lawrence Yunliang Chen, Pannag Sanketi, Quan Vuong, et al. Octo: An
open-source generalist robot policy. In Robotics: Science and Systems, 2024.
[73] Yang Tian, Sizhe Yang, Jia Zeng, Ping Wang, Dahua Lin, Hao Dong, and Jiangmiao Pang. Seer: Predictive inverse dynamics
models are scalable learners for robotic manipulation. In Int. Conf. Learn. Represent., 2025.
[74] Yang Tian, Yuyin Yang, Yiman Xie, Zetao Cai, Xu Shi, Ning Gao, Hangxu Liu, Xuekun Jiang, Zherui Qiu, Feng Yuan, Yaping
Li, Ping Wang, Junhao Cai, Jia Zeng, Hao Dong, et al. Interndata-a1: Pioneering high-fidelity synthetic data for pre-training
generalist policy. arXiv preprint arXiv:2511.16651, 2025.
[75] Alexander Tong, Kilian Fatras, Nikolay Malkin, Guillaume Huguet, Yanlei Zhang, Jarrid Rector-Brooks, Guy Wolf, and Yoshua
Bengio. Improving and generalizing flow-based generative models with minibatch optimal transport. Transactions on Machine
Learning Research, 2024.
[76] Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Łukasz Kaiser, and Illia
Polosukhin. Attention is all you need. In Adv. Neural Inform. Process. Syst., 2017.
[77] Yixuan Wang, Yunzhu Li, Katherine Driggs-Campbell, Li Fei-Fei, and Jiajun Wu. Dynamic-resolution model learning for
object pile manipulation. arXiv preprint arXiv:2306.16700, 2023.
[78] Yuqi Wang, Xinghang Li, Wenxuan Wang, Junbo Zhang, Yingyan Li, Yuntao Chen, Xinlong Wang, and Zhaoxiang Zhang.
Unified vision-language-action model. arXiv preprint arXiv:2506.19850, 2025.
[79] WanTeam. Wan: Open and advanced large-scale video generative models. arXiv preprint arXiv:2503.20314, 2025.
[80] Manuel Watter, Jost Springenberg, Joschka Boedecker, and Martin Riedmiller. Embed to control: A locally linear latent
dynamics model for control from raw images. Advances in neural information processing systems, 28, 2015.
[81] Kun Wu, Chengkai Hou, Jiaming Liu, Zhengping Che, Xiaozhu Ju, Zhuqin Yang, Meng Li, Yinuo Zhao, Zhiyuan Xu, Guang
Yang, Shichao Fan, Xinhua Wang, Fei Liao, Zhen Zhao, Guangyu Li, et al. Robomind: Benchmark on multi-embodiment
intelligence normative data for robot manipulation. In Robotics: Science and Systems, 2025.
[82] Philipp Wu, Alejandro Escontrela, Danijar Hafner, Pieter Abbeel, and Ken Goldberg. Daydreamer: World models for physical
robot learning. In Conference on Robot Learning (CoRL), 2022.
[83] Philipp Wu, Alejandro Escontrela, Danijar Hafner, Pieter Abbeel, and Ken Goldberg. Daydreamer: World models for physical
robot learning. In Conference on robot learning, pages 2226–2240. PMLR, 2023.
[84] Shihan Wu, Xuecheng Liu, Shaoxuan Xie, Pengwei Wang, Xinghang Li, Bowen Yang, Zhe Li, Kai Zhu, Hongyu Wu, Yiheng
Liu, Zhaoye Long, Yue Wang, Chong Liu, Dihan Wang, Ziqiang Ni, et al. Robocoin: An open-sourced bimanual robotic data
collection for integrated manipulation. arXiv preprint arXiv:2511.17441, 2025.
[85] Zhenjia Xu, Jiajun Wu, Andy Zeng, Joshua B Tenenbaum, and Shuran Song. Densephysnet: Learning dense physical object
representations via multi-step dynamic interactions. arXiv preprint arXiv:1906.03853, 2019.
[86] Mengjiao Yang, Yilun Du, Kamyar Ghasemipour, Jonathan Tompson, Leslie Pack Kaelbling, Dale Schuurmans, and Pieter
Abbeel. Unisim: Learning interactive real-world simulators. In Int. Conf. Learn. Represent., 2024.
[87] Shuai Yang, Hao Li, Yilun Chen, Bin Wang, Yang Tian, Tai Wang, Hanqing Wang, Feng Zhao, Yiyi Liao, and Jiangmiao Pang.
Instructvla: Vision-language-action instruction tuning from understanding to manipulation. arXiv preprint arXiv:2507.17520,
2025.
[88] Kaifeng Zhang, Baoyu Li, Kris Hauser, and Yunzhu Li. Adaptigraph: Material-adaptive graph-based neural dynamics for
robotic manipulation. arXiv preprint arXiv:2407.07889, 2024.
[89] Kaifeng Zhang, Baoyu Li, Kris Hauser, and Yunzhu Li. Particle-grid neural dynamics for learning deformable object models
from rgb-d videos. arXiv preprint arXiv:2506.15680, 2025.
[90] Qingqing Zhao, Yao Lu, Moo Jin Kim, Zipeng Fu, Zhuoyang Zhang, Yecheng Wu, Zhaoshuo Li, Qianli Ma, Song Han, Chelsea
Finn, et al. Cot-vla: Visual chain-of-thought reasoning for vision-language-action models. In Proceedings of the Computer
Vision and Pattern Recognition Conference, pages 1702–1713, 2025.
[91] Tony Z. Zhao, Vikash Kumar, Sergey Levine, and Chelsea Finn. Learning fine-grained bimanual manipulation with low-cost
hardware. In Robotics: Science and Systems, 2023.
[92] Zhaxizhuoma, Kehui Liu, Chuyue Guan, Zhongjie Jia, Ziniu Wu, Xin Liu, Tianyu Wang, Shuai Liang, Pengan Chen, Pingrui
Zhang, Haoming Song, Delin Qu, Dong Wang, Zhigang Wang, Nieqing Cao, et al. Fastumi: A scalable and hardware-
independent universal manipulation interface. arXiv preprint arXiv:2409.19499, 2024.
[93] Jinliang Zheng, Jianxiong Li, Zhihao Wang, Dongxiu Liu, Xirui Kang, Yuchun Feng, Yinan Zheng, Jiayin Zou, Yilun Chen,
Jia Zeng, Ya-Qin Zhang, Jiangmiao Pang, Jingjing Liu, Tai Wang, and Xianyuan Zhan. X-vla: Soft-prompted transformer as
scalable cross-embodiment vision-language-action model. arXiv preprint arXiv:2510.10274, 2025.
[94] Ruijie Zheng, Yongyuan Liang, Shuaiyi Huang, Jianfeng Gao, Hal Daumé III, Andrey Kolobov, Furong Huang, and Jianwei
Yang. Tracevla: Visual trace prompting enhances spatial-temporal awareness for generalist robotic policies. arXiv preprint
arXiv:2412.10345, 2024.
[95] Pengfei Zhou, Liliang Chen, Shengcong Chen, Di Chen, Wenzhi Zhao, Rongjun Jin, Guanghui Ren, and Jianlan Luo. Act2goal:
From world model to general goal-conditioned policy. arXiv preprint arXiv:2512.23541, 2025.
[96] Siyuan Zhou, Yilun Du, Jiaben Chen, Yandong Li, Dit-Yan Yeung, and Chuang Gan. Robodreamer: Learning compositional
world models for robot imagination. arXiv preprint arXiv:2404.12377, 2024.
[97] Chuning Zhu, Raymond Yu, Siyuan Feng, Benjamin Burchfiel, Paarth Shah, and Abhishek Gupta. Unified world models:
Coupling video and action diffusion for pretraining on large robotic datasets. In Robotics: Science and Systems, 2025.

## Appendix A. Real-world Evaluation Details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We present detailed evaluation results for all real-world manipulation tasks. Each task is evaluated with 20 trials for both our method and the baseline ($\pi_{0.5}$). To ensure fair comparison, we adopt an alternating evaluation protocol: one trial with $\pi_{0.5}$, followed by one trial with our method, and so on.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们给出全部实机操作任务的详细评估结果。每项任务都分别使用本方法和基线（$\pi_{0.5}$）进行 20 次试验。为确保公平比较，我们采用交替评估协议：先用 $\pi_{0.5}$ 进行一次试验，再用本方法进行一次试验，如此交替。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For each trial, we record the success status of every intermediate step. If a step requires a retry to succeed, we assign a score of 0.5; if it fails, the score is 0; if it succeeds on the first attempt, the score is 1. A trial is marked as successful only if all steps are completed (i.e., the total score equals the maximum possible score).

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 对每次试验，我们记录每个中间步骤的成功状态。若某步骤需要重试后才成功，记 0.5 分；若失败，记 0 分；若第一次尝试即成功，记 1 分。只有完成全部步骤（即总分等于最高可能分数）时，该次试验才标记为成功。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> We report two metrics:
>
> - **Progress Score (PS):** The average score across all trials divided by the maximum possible score, expressed as a percentage: $\mathrm{PS}=\frac{\mathrm{Average\ Progress}}{\mathrm{Max\ Steps}}\times100\%$.
> - **Success Rate (SR):** The number of successful trials divided by the total number of trials, expressed as a percentage: $\mathrm{SR}=\frac{\#\mathrm{Successful\ Trials}}{\#\mathrm{Total\ Trials}}\times100\%$.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 我们报告两项指标：
>
> - **进度分数（PS）：** 全部试验的平均得分除以最高可能分数，并表示为百分比：$\mathrm{PS}=\frac{\mathrm{Average\ Progress}}{\mathrm{Max\ Steps}}\times100\%$。
> - **成功率（SR）：** 成功试验次数除以试验总次数，并表示为百分比：$\mathrm{SR}=\frac{\#\mathrm{Successful\ Trials}}{\#\mathrm{Total\ Trials}}\times100\%$。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> We evaluate on six diverse real-world tasks: Make Breakfast (10 steps: preparing a complete breakfast including toasting bread, pouring water, and plating), Pick Screws (5 steps: picking up paper, pouring screws, and inserting three screws), Fold Clothes (6 steps: folding a shirt including sleeves and smoothing), Unpack Delivery (5 steps: opening a package using a utility knife), Insert Tubes (2 categories: grasping and inserting 3 tubes), and Fold Pants (3 steps: folding pants and placing them). These tasks span long-horizon sequential manipulation, precision control, and deformable object handling. The following tables present per-trial results for each task.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 我们在六项多样实机任务上评估：Make Breakfast（10 步：准备完整早餐，包括烤面包、倒水和装盘）、Pick Screws（5 步：拿起纸、倒出螺钉并插入三枚螺钉）、Fold Clothes（6 步：折叠衬衫，包括袖子折叠与展平）、Unpack Delivery（5 步：使用美工刀打开包裹）、Insert Tubes（2 类：抓取并插入 3 根管），以及 Fold Pants（3 步：折叠裤子并放置）。这些任务涵盖长时序顺序操作、精细控制与可变形物体处理。下列表格给出每项任务的逐试验结果。

### Table S1. RoboTwin 2.0 仿真逐任务评估（Easy vs Hard，50 项任务）

![Table S1](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/table_s1_robotwin_all_tasks.png)

**Caption:** Table S1. Evaluation on RoboTwin 2.0 Simulation (Easy vs Hard, 50 tasks). RoboTwin 2.0 is a challenging bimanual manipulation benchmark requiring coordinated dual-arm control. Easy uses fixed initial configurations while Hard involves randomized object poses and scene layouts.

**Caption[CN]:** 表 S1. RoboTwin 2.0 仿真评估（Easy vs Hard，50 项任务）。RoboTwin 2.0 是要求双臂协调控制的高难度双臂操作基准。Easy 使用固定初始配置，Hard 包含随机化物体位姿和场景布局。

| Simulation Task | Horizon | Ours Easy | Ours Hard | $\pi_0$ [7] Easy | $\pi_0$ [7] Hard | $\pi_{0.5}$ [7] Easy | $\pi_{0.5}$ [7] Hard | X-VLA [93] Easy | X-VLA [93] Hard | Motus [5] Easy | Motus [5] Hard |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Adjust Bottle | 1 | 90% | 94% | 99% | 95% | 100% | 99% | 100% | 99% | 89% | 93% |
| Beat Block Hammer | 1 | 96% | 98% | 79% | 84% | 96% | 93% | 92% | 88% | 95% | 88% |
| Blocks Ranking RGB | 3 | 99% | 98% | 80% | 63% | 92% | 85% | 83% | 83% | 99% | 97% |
| Blocks Ranking Size | 3 | 94% | 96% | 14% | 5% | 49% | 26% | 67% | 74% | 75% | 63% |
| Click Alarmclock | 1 | 99% | 100% | 77% | 68% | 98% | 89% | 99% | 99% | 100% | 100% |
| Click Bell | 1 | 100% | 100% | 71% | 48% | 99% | 66% | 100% | 100% | 100% | 100% |
| Dump Bin Bigbin | 1 | 89% | 96% | 88% | 83% | 92% | 97% | 79% | 77% | 95% | 91% |
| Grab Roller | 1 | 100% | 100% | 98% | 94% | 100% | 100% | 100% | 100% | 100% | 100% |
| Handover Block | 2 | 99% | 78% | 47% | 31% | 66% | 57% | 73% | 37% | 86% | 73% |
| Handover Mic | 2 | 94% | 96% | 97% | 97% | 98% | 97% | 0% | 0% | 78% | 63% |
| Hanging Mug | 2 | 40% | 28% | 14% | 11% | 18% | 17% | 23% | 27% | 38% | 38% |
| Lift Pot | 1 | 100% | 99% | 80% | 72% | 96% | 85% | 99% | 100% | 96% | 99% |
| Move Can Pot | 1 | 94% | 97% | 68% | 48% | 51% | 55% | 89% | 86% | 34% | 74% |
| Move Pillbottle Pad | 1 | 99% | 99% | 67% | 46% | 84% | 61% | 73% | 71% | 93% | 96% |
| Move Playingcard Away | 1 | 100% | 99% | 74% | 65% | 96% | 84% | 93% | 98% | 100% | 96% |
| Move Stapler Pad | 1 | 91% | 79% | 41% | 24% | 56% | 42% | 78% | 73% | 83% | 85% |
| Open Laptop | 1 | 92% | 94% | 71% | 81% | 90% | 96% | 93% | 100% | 95% | 91% |
| Open Microwave | 1 | 82% | 86% | 4% | 32% | 34% | 77% | 79% | 71% | 95% | 91% |
| Pick Diverse Bottles | 2 | 89% | 82% | 69% | 31% | 81% | 71% | 58% | 36% | 90% | 91% |
| Pick Dual Bottles | 2 | 100% | 99% | 59% | 37% | 93% | 63% | 47% | 36% | 96% | 90% |
| Place A2B Left | 1 | 97% | 93% | 43% | 47% | 87% | 82% | 48% | 49% | 82% | 79% |
| Place A2B Right | 1 | 97% | 95% | 39% | 34% | 87% | 84% | 36% | 36% | 90% | 87% |
| Place Bread Basket | 1 | 97% | 95% | 62% | 46% | 77% | 64% | 81% | 71% | 91% | 94% |
| Place Bread Skillet | 2 | 95% | 90% | 66% | 49% | 85% | 66% | 77% | 67% | 86% | 83% |
| Place Burger Fries | 2 | 97% | 95% | 81% | 76% | 94% | 87% | 94% | 94% | 98% | 98% |
| Place Can Basket | 2 | 81% | 84% | 55% | 46% | 62% | 62% | 49% | 52% | 81% | 76% |
| Place Cans Plasticbox | 2 | 100% | 99% | 63% | 45% | 94% | 84% | 97% | 98% | 98% | 94% |
| Place Container Plate | 1 | 99% | 97% | 97% | 92% | 99% | 95% | 97% | 95% | 98% | 99% |
| Place Dual Shoes | 2 | 94% | 89% | 59% | 51% | 75% | 75% | 79% | 88% | 93% | 87% |
| Place Empty Cup | 1 | 100% | 100% | 91% | 85% | 100% | 99% | 100% | 98% | 99% | 98% |
| Place Fan | 1 | 99% | 93% | 66% | 71% | 87% | 85% | 80% | 75% | 91% | 87% |
| Place Mouse Pad | 1 | 93% | 96% | 20% | 20% | 60% | 39% | 70% | 70% | 66% | 68% |
| Place Object Basket | 2 | 91% | 88% | 67% | 70% | 80% | 76% | 44% | 39% | 81% | 87% |
| Place Object Scale | 1 | 96% | 95% | 57% | 52% | 86% | 80% | 52% | 74% | 88% | 85% |
| Place Object Stand | 1 | 99% | 96% | 82% | 68% | 91% | 85% | 86% | 88% | 98% | 97% |
| Place Phone Stand | 1 | 97% | 97% | 49% | 53% | 81% | 81% | 88% | 87% | 87% | 86% |
| Place Shoe | 1 | 98% | 98% | 76% | 76% | 92% | 93% | 96% | 95% | 99% | 97% |
| Press Stapler | 1 | 85% | 82% | 44% | 37% | 87% | 83% | 92% | 98% | 93% | 98% |
| Put Bottles Dustbin | 3 | 87% | 91% | 65% | 56% | 84% | 79% | 74% | 77% | 81% | 79% |
| Put Object Cabinet | 2 | 85% | 87% | 73% | 60% | 80% | 79% | 46% | 48% | 88% | 71% |
| Rotate QRcode | 1 | 96% | 91% | 74% | 70% | 89% | 87% | 34% | 33% | 89% | 73% |
| Scan Object | 2 | 96% | 91% | 55% | 42% | 72% | 65% | 14% | 36% | 67% | 66% |
| Shake Bottle Horizontally | 1 | 100% | 99% | 98% | 92% | 99% | 99% | 100% | 100% | 100% | 98% |
| Shake Bottle | 1 | 100% | 97% | 94% | 91% | 99% | 97% | 99% | 100% | 100% | 97% |
| Stack Blocks Three | 3 | 99% | 98% | 72% | 52% | 91% | 76% | 6% | 10% | 91% | 95% |
| Stack Blocks Two | 2 | 100% | 98% | 93% | 79% | 97% | 100% | 92% | 87% | 100% | 98% |
| Stack Bowls Three | 3 | 86% | 83% | 77% | 75% | 77% | 71% | 76% | 86% | 79% | 87% |
| Stack Bowls Two | 2 | 94% | 98% | 94% | 95% | 95% | 96% | 96% | 93% | 98% | 98% |
| Stamp Seal | 1 | 96% | 97% | 46% | 33% | 79% | 55% | 76% | 82% | 93% | 92% |
| Turn Switch | 1 | 44% | 45% | 41% | 42% | 62% | 54% | 40% | 61% | 84% | 78% |
| **Average (%)** | — | **92.93** | **91.55** | 65.92 | 58.40 | 82.74 | 76.76 | 72.80 | 72.84 | 88.66 | 87.02 |

### Table S2. Make Breakfast 逐试验结果

![Table S2](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/table_s2_make_breakfast.png)

**Caption:** Table S2. Detailed evaluation results for Make Breakfast task (10 steps, max score 10).

**Caption[CN]:** 表 S2. Make Breakfast 任务的详细评估结果（10 个步骤，最高分 10）。

| Method | Trial | Succ. | Grasp Plate | Grasp Bread | Grasp Fork | Place Bread | Press Toaster | Grasp Cup | Grasp Kettle | Pour | Grasp Apple | Serve | Prog. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Ours | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 9 |
| Ours | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 |
| Ours | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 |
| Ours | 4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 |
| Ours | 5 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 |
| Ours | 6 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 |
| Ours | 7 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 9 |
| Ours | 8 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0.5 | 1 | 9.5 |
| Ours | 9 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 9 |
| Ours | 10 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 |
| Ours | 11 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 9 |
| Ours | 12 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 |
| Ours | 13 | 0 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 9 |
| Ours | 14 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 |
| Ours | 15 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 |
| Ours | 16 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 |
| Ours | 17 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0.5 | 1 | 9.5 |
| Ours | 18 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 |
| Ours | 19 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 |
| Ours | 20 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 10 |
| **Ours Avg** | — | **0.75** | **1.00** | **1.00** | **1.00** | **0.90** | **1.00** | **1.00** | **1.00** | **0.90** | **0.95** | **0.95** | **9.70** |
| $\pi_{0.5}$ | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| $\pi_{0.5}$ | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 9 |
| $\pi_{0.5}$ | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 9 |
| $\pi_{0.5}$ | 4 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 8 |
| $\pi_{0.5}$ | 5 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 7 |
| $\pi_{0.5}$ | 6 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 9 |
| $\pi_{0.5}$ | 7 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 8 |
| $\pi_{0.5}$ | 8 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 9 |
| $\pi_{0.5}$ | 9 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 | 0 | 0 | 5 |
| $\pi_{0.5}$ | 10 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 4 |
| $\pi_{0.5}$ | 11 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 8 |
| $\pi_{0.5}$ | 12 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 7 |
| $\pi_{0.5}$ | 13 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 7 |
| $\pi_{0.5}$ | 14 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 8 |
| $\pi_{0.5}$ | 15 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 1 | 8 |
| $\pi_{0.5}$ | 16 | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 1 | 8 |
| $\pi_{0.5}$ | 17 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 1 | 1 | 1 | 1 | 9 |
| $\pi_{0.5}$ | 18 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 | 0 | 1 | 1 | 8 |
| $\pi_{0.5}$ | 19 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 | 1 | 1 | 6 |
| $\pi_{0.5}$ | 20 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 5 |
| **$\pi_{0.5}$ Avg** | — | **0.70** | **1.00** | **1.00** | **0.80** | **0.75** | **0.55** | **0.35** | **0.80** | **0.50** | **0.80** | **0.75** | **7.30** |

| Method | Progress Score | Success Rate |
|---|---:|---:|
| Ours | 97.0% (= 9.70/10 $\times$ 100%) | 75.0% (= 15/20 $\times$ 100%) |
| $\pi_{0.5}$ | 73.0% (= 7.30/10 $\times$ 100%) | 70.0% (= 14/20 $\times$ 100%) |

### Table S3. Pick Screws 逐试验结果

![Table S3](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/table_s3_pick_screws.png)

**Caption:** Table S3. Detailed evaluation results for Pick Screws task (5 steps, max score 5).

**Caption[CN]:** 表 S3. Pick Screws 任务的详细评估结果（5 个步骤，最高分 5）。

| Method | Trial | Success | Grab Paper | Pour Screws | Screw 1 | Screw 2 | Screw 3 | Progress |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Ours | 1 | 1 | 1 | 1 | 0.5 | 0.5 | 1 | 4 |
| Ours | 2 | 0 | 1 | 0 | 1 | 1 | 0.5 | 3.5 |
| Ours | 3 | 1 | 1 | 1 | 1 | 0.5 | 0.5 | 4 |
| Ours | 4 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 5 | 1 | 1 | 1 | 1 | 1 | 0.5 | 4.5 |
| Ours | 6 | 1 | 1 | 1 | 0.5 | 1 | 0.5 | 4 |
| Ours | 7 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 8 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 9 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| Ours | 10 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 11 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 12 | 0 | 1 | 0 | 1 | 1 | 1 | 4 |
| Ours | 13 | 0 | 1 | 0 | 1 | 1 | 1 | 4 |
| Ours | 14 | 1 | 1 | 1 | 1 | 0.5 | 0.5 | 4 |
| Ours | 15 | 0 | 1 | 0 | 0 | 0.5 | 1 | 2.5 |
| Ours | 16 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 17 | 1 | 1 | 1 | 1 | 1 | 0.5 | 4.5 |
| Ours | 18 | 1 | 1 | 1 | 0.5 | 0.5 | 1 | 4 |
| Ours | 19 | 0 | 1 | 1 | 0 | 1 | 0.5 | 3.5 |
| Ours | 20 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| **Ours Avg** | — | **0.70** | **1.00** | **0.75** | **0.78** | **0.83** | **0.78** | **4.13** |
| $\pi_{0.5}$ | 1 | 0 | 1 | 0 | 1 | 1 | 1 | 4 |
| $\pi_{0.5}$ | 2 | 0 | 0.5 | 0 | 1 | 1 | 0.5 | 3 |
| $\pi_{0.5}$ | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| $\pi_{0.5}$ | 4 | 0 | 1 | 0 | 1 | 0.5 | 0.5 | 3 |
| $\pi_{0.5}$ | 5 | 1 | 1 | 1 | 0.5 | 1 | 0.5 | 4 |
| $\pi_{0.5}$ | 6 | 1 | 1 | 1 | 1 | 0.5 | 1 | 4.5 |
| $\pi_{0.5}$ | 7 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| $\pi_{0.5}$ | 8 | 1 | 1 | 1 | 0.5 | 0.5 | 1 | 4 |
| $\pi_{0.5}$ | 9 | 0 | 1 | 0 | 0.5 | 0.5 | 0 | 2 |
| $\pi_{0.5}$ | 10 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| $\pi_{0.5}$ | 11 | 1 | 1 | 1 | 0.5 | 1 | 1 | 4.5 |
| $\pi_{0.5}$ | 12 | 0 | 1 | 0 | 1 | 1 | 0.5 | 3.5 |
| $\pi_{0.5}$ | 13 | 0 | 1 | 1 | 1 | 0 | 0.5 | 3.5 |
| $\pi_{0.5}$ | 14 | 1 | 1 | 1 | 0.5 | 1 | 1 | 4.5 |
| $\pi_{0.5}$ | 15 | 0 | 1 | 1 | 1 | 1 | 0 | 4 |
| $\pi_{0.5}$ | 16 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| $\pi_{0.5}$ | 17 | 0 | 0 | 0 | 1 | 0.5 | 0.5 | 2 |
| $\pi_{0.5}$ | 18 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 19 | 0 | 1 | 0 | 1 | 0.5 | 0.5 | 3 |
| $\pi_{0.5}$ | 20 | 1 | 1 | 1 | 1 | 1 | 0.5 | 4.5 |
| **$\pi_{0.5}$ Avg** | — | **0.50** | **0.88** | **0.60** | **0.83** | **0.75** | **0.65** | **3.70** |

| Method | Progress Score | Success Rate |
|---|---:|---:|
| Ours | 82.5% (= 4.13/5 $\times$ 100%) | 70.0% (= 14/20 $\times$ 100%) |
| $\pi_{0.5}$ | 74.0% (= 3.70/5 $\times$ 100%) | 50.0% (= 10/20 $\times$ 100%) |

### Table S4. Fold Clothes 逐试验结果

![Table S4](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/table_s4_fold_clothes.png)

**Caption:** Table S4. Detailed evaluation results for Fold Clothes task (6 steps, max score 6).

**Caption[CN]:** 表 S4. Fold Clothes 任务的详细评估结果（6 个步骤，最高分 6）。

| Method | Trial | Success | Fold Half | Left Sleeve | Right Sleeve | Fold Again | Flatten | Place | Progress |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Ours | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| Ours | 2 | 0 | 1 | 1 | 0 | 0 | 0 | 0 | 2 |
| Ours | 3 | 1 | 1 | 1 | 1 | 1 | 0.5 | 0.5 | 5 |
| Ours | 4 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| Ours | 5 | 0 | 0.5 | 0 | 0 | 0 | 0 | 0 | 0.5 |
| Ours | 6 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ours | 7 | 0 | 0.5 | 0 | 0 | 0 | 0 | 0 | 0.5 |
| Ours | 8 | 1 | 1 | 1 | 1 | 1 | 0.5 | 0.5 | 5 |
| Ours | 9 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| Ours | 10 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| Ours | 11 | 0 | 0.5 | 0 | 0 | 0 | 0 | 0 | 0.5 |
| Ours | 12 | 0 | 0.5 | 0 | 0 | 0 | 0 | 0 | 0.5 |
| Ours | 13 | 0 | 0.5 | 0 | 0 | 0 | 0 | 0 | 0.5 |
| Ours | 14 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| Ours | 15 | 0 | 0.5 | 0 | 0 | 0 | 0 | 0 | 0.5 |
| Ours | 16 | 0 | 1 | 1 | 1 | 1 | 0.5 | 0 | 4.5 |
| Ours | 17 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| Ours | 18 | 0 | 1 | 1 | 1 | 0.5 | 0 | 0 | 3.5 |
| Ours | 19 | 0 | 0.5 | 0 | 0 | 0 | 0 | 0 | 0.5 |
| Ours | 20 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| **Ours Avg** | — | **0.35** | **0.73** | **0.55** | **0.50** | **0.48** | **0.38** | **0.30** | **2.93** |
| $\pi_{0.5}$ | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| $\pi_{0.5}$ | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| $\pi_{0.5}$ | 3 | 1 | 1 | 1 | 1 | 0.5 | 1 | 0.5 | 5 |
| $\pi_{0.5}$ | 4 | 0 | 1 | 1 | 1 | 0.5 | 1 | 0 | 4.5 |
| $\pi_{0.5}$ | 5 | 0 | 0.5 | 1 | 1 | 0.5 | 1 | 0 | 4 |
| $\pi_{0.5}$ | 6 | 0 | 1 | 1 | 0.5 | 1 | 1 | 0 | 4.5 |
| $\pi_{0.5}$ | 7 | 0 | 0.5 | 0 | 0 | 0 | 0 | 0 | 0.5 |
| $\pi_{0.5}$ | 8 | 0 | 0.5 | 0 | 0 | 0 | 0 | 0 | 0.5 |
| $\pi_{0.5}$ | 9 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| $\pi_{0.5}$ | 10 | 0 | 0.5 | 1 | 1 | 0.5 | 0 | 0 | 3 |
| $\pi_{0.5}$ | 11 | 0 | 0.5 | 0 | 0 | 0 | 0 | 0 | 0.5 |
| $\pi_{0.5}$ | 12 | 0 | 1 | 1 | 1 | 1 | 1 | 0 | 5 |
| $\pi_{0.5}$ | 13 | 0 | 1 | 1 | 0.5 | 0 | 0 | 0 | 2.5 |
| $\pi_{0.5}$ | 14 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| $\pi_{0.5}$ | 15 | 1 | 1 | 1 | 1 | 0.5 | 1 | 1 | 5.5 |
| $\pi_{0.5}$ | 16 | 0 | 1 | 1 | 1 | 0.5 | 0 | 0 | 3.5 |
| $\pi_{0.5}$ | 17 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 6 |
| $\pi_{0.5}$ | 18 | 0 | 1 | 1 | 1 | 0.5 | 1 | 0 | 4.5 |
| $\pi_{0.5}$ | 19 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 20 | 0 | 1 | 1 | 1 | 0 | 0 | 0 | 3 |
| **$\pi_{0.5}$ Avg** | — | **0.30** | **0.83** | **0.80** | **0.75** | **0.53** | **0.60** | **0.28** | **3.78** |

| Method | Progress Score | Success Rate |
|---|---:|---:|
| Ours | 48.8% (= 2.93/6 $\times$ 100%) | 35.0% (= 7/20 $\times$ 100%) |
| $\pi_{0.5}$ | 62.9% (= 3.78/6 $\times$ 100%) | 30.0% (= 6/20 $\times$ 100%) |

### Table S5. Unpack Delivery 逐试验结果

![Table S5](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/table_s5_unpack_delivery.png)

**Caption:** Table S5. Detailed evaluation results for Unpack Delivery task (5 steps, max score 5).

**Caption[CN]:** 表 S5. Unpack Delivery 任务的详细评估结果（5 个步骤，最高分 5）。

| Method | Trial | Success | Grab Knife | Push Blade | Handover | Cut Seal | Open Lid | Progress |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Ours | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 2 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 3 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 1 |
| Ours | 5 | 0 | 1 | 1 | 1 | 0.5 | 0 | 3.5 |
| Ours | 6 | 0 | 1 | 1 | 1 | 0 | 0 | 3 |
| Ours | 7 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 8 | 0 | 1 | 1 | 1 | 0 | 0 | 3 |
| Ours | 9 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 10 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 11 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 12 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 13 | 0 | 1 | 1 | 1 | 0 | 0 | 3 |
| Ours | 14 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 15 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 16 | 0 | 1 | 1 | 1 | 0 | 0 | 3 |
| Ours | 17 | 1 | 1 | 1 | 1 | 0.5 | 1 | 4.5 |
| Ours | 18 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| Ours | 19 | 0 | 1 | 1 | 1 | 0.5 | 0 | 3.5 |
| Ours | 20 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| **Ours Avg** | — | **0.65** | **1.00** | **0.95** | **0.95** | **0.68** | **0.65** | **4.23** |
| $\pi_{0.5}$ | 1 | 0 | 1 | 1 | 0.5 | 0.5 | 0 | 3 |
| $\pi_{0.5}$ | 2 | 0 | 1 | 1 | 1 | 0 | 0 | 3 |
| $\pi_{0.5}$ | 3 | 0 | 1 | 1 | 1 | 0.5 | 0 | 3.5 |
| $\pi_{0.5}$ | 4 | 0 | 1 | 1 | 1 | 0.5 | 0 | 3.5 |
| $\pi_{0.5}$ | 5 | 0 | 1 | 1 | 1 | 0.5 | 0 | 3.5 |
| $\pi_{0.5}$ | 6 | 0 | 1 | 1 | 1 | 0 | 0 | 3 |
| $\pi_{0.5}$ | 7 | 0 | 1 | 1 | 1 | 0 | 0 | 3 |
| $\pi_{0.5}$ | 8 | 1 | 1 | 1 | 1 | 0.5 | 1 | 4.5 |
| $\pi_{0.5}$ | 9 | 0 | 1 | 1 | 1 | 0.5 | 0 | 3.5 |
| $\pi_{0.5}$ | 10 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| $\pi_{0.5}$ | 11 | 0 | 1 | 1 | 1 | 0.5 | 0 | 3.5 |
| $\pi_{0.5}$ | 12 | 0 | 1 | 1 | 1 | 0.5 | 0 | 3.5 |
| $\pi_{0.5}$ | 13 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| $\pi_{0.5}$ | 14 | 0 | 1 | 1 | 1 | 0.5 | 0 | 3.5 |
| $\pi_{0.5}$ | 15 | 1 | 1 | 1 | 1 | 0.5 | 1 | 4.5 |
| $\pi_{0.5}$ | 16 | 0 | 1 | 1 | 1 | 0 | 0 | 3 |
| $\pi_{0.5}$ | 17 | 0 | 1 | 1 | 1 | 0 | 0 | 3 |
| $\pi_{0.5}$ | 18 | 0 | 1 | 1 | 1 | 0 | 0 | 3 |
| $\pi_{0.5}$ | 19 | 0 | 1 | 1 | 1 | 0.5 | 0 | 3.5 |
| $\pi_{0.5}$ | 20 | 1 | 1 | 1 | 1 | 1 | 1 | 5 |
| **$\pi_{0.5}$ Avg** | — | **0.25** | **1.00** | **1.00** | **0.98** | **0.43** | **0.25** | **3.65** |

| Method | Progress Score | Success Rate |
|---|---:|---:|
| Ours | 84.5% (= 4.23/5 $\times$ 100%) | 65.0% (= 13/20 $\times$ 100%) |
| $\pi_{0.5}$ | 73.0% (= 3.65/5 $\times$ 100%) | 25.0% (= 5/20 $\times$ 100%) |

### Table S6. Insert Tubes 逐试验结果

![Table S6](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/table_s6_insert_tubes.png)

**Caption:** Table S6. Detailed evaluation results for Insert Tubes task (2 categories: Grasp and Insert, max score 6).

**Caption[CN]:** 表 S6. Insert Tubes 任务的详细评估结果（2 类：Grasp 和 Insert，最高分 6）。

| Method | Trial | Success | Grasp (3) | Insert (3) | Progress |
|---|---:|---:|---:|---:|---:|
| Ours | 1 | 0 | 3 | 2 | 5 |
| Ours | 2 | 1 | 3 | 3 | 6 |
| Ours | 3 | 0 | 3 | 2 | 5 |
| Ours | 4 | 0 | 2 | 2 | 4 |
| Ours | 5 | 1 | 3 | 3 | 6 |
| Ours | 6 | 1 | 3 | 3 | 6 |
| Ours | 7 | 0 | 3 | 2 | 5 |
| Ours | 8 | 1 | 3 | 3 | 6 |
| Ours | 9 | 0 | 3 | 2 | 5 |
| Ours | 10 | 0 | 3 | 2 | 5 |
| Ours | 11 | 1 | 3 | 3 | 6 |
| Ours | 12 | 0 | 3 | 2 | 5 |
| Ours | 13 | 1 | 3 | 3 | 6 |
| Ours | 14 | 0 | 3 | 2 | 5 |
| Ours | 15 | 0 | 3 | 1 | 4 |
| Ours | 16 | 1 | 3 | 3 | 6 |
| Ours | 17 | 0 | 2 | 2 | 4 |
| Ours | 18 | 0 | 2 | 2 | 4 |
| Ours | 19 | 1 | 3 | 3 | 6 |
| Ours | 20 | 0 | 2 | 2 | 4 |
| **Ours Avg** | — | **0.40** | **2.80** | **2.35** | **5.15** |
| $\pi_{0.5}$ | 1 | 0 | 3 | 1 | 4 |
| $\pi_{0.5}$ | 2 | 0 | 3 | 1 | 4 |
| $\pi_{0.5}$ | 3 | 0 | 3 | 1 | 4 |
| $\pi_{0.5}$ | 4 | 0 | 3 | 1 | 4 |
| $\pi_{0.5}$ | 5 | 0 | 3 | 1 | 4 |
| $\pi_{0.5}$ | 6 | 0 | 3 | 1 | 4 |
| $\pi_{0.5}$ | 7 | 0 | 3 | 1 | 4 |
| $\pi_{0.5}$ | 8 | 0 | 3 | 2 | 5 |
| $\pi_{0.5}$ | 9 | 1 | 3 | 3 | 6 |
| $\pi_{0.5}$ | 10 | 1 | 3 | 3 | 6 |
| $\pi_{0.5}$ | 11 | 1 | 3 | 3 | 6 |
| $\pi_{0.5}$ | 12 | 0 | 2 | 1 | 3 |
| $\pi_{0.5}$ | 13 | 0 | 3 | 2 | 5 |
| $\pi_{0.5}$ | 14 | 0 | 2 | 2 | 4 |
| $\pi_{0.5}$ | 15 | 1 | 3 | 3 | 6 |
| $\pi_{0.5}$ | 16 | 1 | 3 | 3 | 6 |
| $\pi_{0.5}$ | 17 | 0 | 3 | 2 | 5 |
| $\pi_{0.5}$ | 18 | 0 | 2 | 2 | 4 |
| $\pi_{0.5}$ | 19 | 1 | 3 | 3 | 6 |
| $\pi_{0.5}$ | 20 | 0 | 3 | 2 | 5 |
| **$\pi_{0.5}$ Avg** | — | **0.30** | **2.85** | **1.90** | **4.75** |

| Method | Progress Score | Success Rate |
|---|---:|---:|
| Ours | 85.8% (= 5.15/6 $\times$ 100%) | 40.0% (= 8/20 $\times$ 100%) |
| $\pi_{0.5}$ | 79.2% (= 4.75/6 $\times$ 100%) | 30.0% (= 6/20 $\times$ 100%) |

### Table S7. Fold Pants 逐试验结果

![Table S7](/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Causal%20World%20Modeling%20for%20Robot%20Control/assets/table_s7_fold_pants.png)

**Caption:** Table S7. Detailed evaluation results for Fold Pants task (3 steps, max score 3).

**Caption[CN]:** 表 S7. Fold Pants 任务的详细评估结果（3 个步骤，最高分 3）。

| Method | Trial | Success | Fold 1 | Fold 2 | Place | Progress |
|---|---:|---:|---:|---:|---:|---:|
| Ours | 1 | 1 | 1 | 1 | 1 | 3 |
| Ours | 2 | 1 | 1 | 1 | 1 | 3 |
| Ours | 3 | 1 | 1 | 1 | 1 | 3 |
| Ours | 4 | 0 | 0 | 0 | 0 | 0 |
| Ours | 5 | 0 | 1 | 0 | 0 | 1 |
| Ours | 6 | 0 | 1 | 0 | 0 | 1 |
| Ours | 7 | 1 | 1 | 1 | 1 | 3 |
| Ours | 8 | 1 | 1 | 1 | 1 | 3 |
| Ours | 9 | 1 | 1 | 1 | 1 | 3 |
| Ours | 10 | 1 | 1 | 1 | 1 | 3 |
| Ours | 11 | 1 | 1 | 1 | 1 | 3 |
| Ours | 12 | 1 | 1 | 1 | 1 | 3 |
| Ours | 13 | 1 | 1 | 1 | 1 | 3 |
| Ours | 14 | 1 | 1 | 1 | 1 | 3 |
| Ours | 15 | 1 | 1 | 1 | 1 | 3 |
| Ours | 16 | 1 | 1 | 1 | 1 | 3 |
| Ours | 17 | 1 | 1 | 1 | 1 | 3 |
| Ours | 18 | 0 | 1 | 0 | 0 | 1 |
| Ours | 19 | 0 | 1 | 0 | 0 | 1 |
| Ours | 20 | 0 | 0 | 0 | 0 | 0 |
| **Ours Avg** | — | **0.70** | **0.90** | **0.70** | **0.70** | **2.30** |
| $\pi_{0.5}$ | 1 | 1 | 1 | 1 | 1 | 3 |
| $\pi_{0.5}$ | 2 | 1 | 1 | 1 | 1 | 3 |
| $\pi_{0.5}$ | 3 | 1 | 1 | 1 | 1 | 3 |
| $\pi_{0.5}$ | 4 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 5 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 6 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 7 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 8 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 9 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 10 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 11 | 1 | 1 | 1 | 1 | 3 |
| $\pi_{0.5}$ | 12 | 1 | 1 | 1 | 1 | 3 |
| $\pi_{0.5}$ | 13 | 1 | 1 | 1 | 1 | 3 |
| $\pi_{0.5}$ | 14 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 15 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 16 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 17 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 18 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 19 | 0 | 0 | 0 | 0 | 0 |
| $\pi_{0.5}$ | 20 | 0 | 0 | 0 | 0 | 0 |
| **$\pi_{0.5}$ Avg** | — | **0.30** | **0.30** | **0.30** | **0.30** | **0.90** |

| Method | Progress Score | Success Rate |
|---|---:|---:|
| Ours | 76.7% (= 2.30/3 $\times$ 100%) | 70.0% (= 14/20 $\times$ 100%) |
| $\pi_{0.5}$ | 30.0% (= 0.90/3 $\times$ 100%) | 30.0% (= 6/20 $\times$ 100%) |

---

## End-of-document coverage check

| Check | Count |
|---|---:|
| PDF pages represented | 31 |
| Figure cards | 10 |
| Table cards | 10 |
| Algorithms | 2 |
| Numbered equations | 13 |
| Appendix sections | 1 (Appendix A) |
| Searchable bibliography entries | 97 |


