# Light-WAM: Efficient World Action Models with State-Fusion Action Decoding

**Authors:** Ziang Li, Dongzhou Cheng, Yibin Wang, Shiyue Wang, Xiaoyang Xu, Lingxuan Weng, Juan Wang, Jiaqi Wang  
**Source:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/S7BIWD7S/Li 等 - 2026 - Light-WAM Efficient World Action Models with State-Fusion Action Decoding.pdf`  
**Detected source format:** selectable-text PDF (`pdf-text`)  
**Reader type:** full-paper Chinese-English Markdown reader with figure/table assets  
**arXiv:** 2606.08242v1 · 6 June 2026  
**Code:** https://github.com/L1ziang/Light-WAM

## Page / Section Index

| Pages | Section |
|---|---|
| 1 | Abstract |
| 1–2 | 1. Introduction |
| 2–3 | 2. Related Work |
| 3–5 | 3. Methodology |
| 5–8 | 4. Experiments |
| 8–9 | Conclusion and Limitations |
| 9–12 | References |
| 12–15 | Appendices: algorithms, training details, parameters, full RoboTwin results, real-world rollouts |

## Terminology Ledger

| English term | 中文译法 | Note |
|---|---|---|
| World Action Model (WAM) | 世界动作模型 | 以未来视频预测辅助机器人策略学习 |
| future-video co-training | 未来视频协同训练 | 只在训练时使用的视频预测监督 |
| StateFusionActionExpert | 状态融合动作专家 | 论文提出的单次前向动作解码器 |
| adapted state | 适配后状态 | 经 LoRA 与 WAM adapter 修改的骨干隐藏状态 |
| learned-query pooling | 可学习查询池化 | 用少量 query 压缩密集视频 token |
| query bottleneck | 查询瓶颈 | 控制视频表征进入动作头的信息带宽 |
| latent caching | 潜变量缓存 | 训练前缓存 VAE latent，避免在线编码 |
| embodied pretraining (EPT) | 具身预训练 | 使用大规模机器人动作数据进行预训练 |
| action chunk | 动作块 | 一次输出未来 $K$ 步动作 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> World Action Models extend robot policy learning by adding future prediction as a training objective, encouraging policy representations to encode task-relevant temporal structure. Existing WAMs often use large generative architectures, which bring high training cost and inference latency and make efficient closed-loop deployment difficult.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 世界动作模型通过加入未来预测目标扩展机器人策略学习，促使策略表征编码与任务有关的时间结构。现有 WAM 往往依赖大型生成架构，带来高昂的训练成本和推理延迟，使高效闭环部署变得困难。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> We propose Light-WAM, a lightweight WAM for efficient robot manipulation. It uses a compact video backbone and applies future-video supervision in a spatially downsampled latent space, reducing video co-training cost while retaining its representation-learning benefit.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 本文提出面向高效机器人操作的轻量级世界动作模型 Light-WAM。它使用紧凑的视频骨干，并在空间下采样后的潜空间中施加未来视频监督，从而降低视频协同训练成本，同时保留其表征学习收益。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> For action prediction, the StateFusionActionExpert reads adapted states from multiple backbone layers, compresses them through learned-query pooling, and predicts action chunks in one forward pass. This avoids a heavy generative action expert. Light-WAM uses 0.44B trainable parameters, reaches 72.03 ms latency with 4.1 GiB peak GPU memory, and remains competitive on LIBERO while achieving usable 50-task performance on RoboTwin 2.0.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在动作预测方面，StateFusionActionExpert 从多个骨干层读取适配后状态，经由可学习查询池化进行压缩，并在一次前向中预测动作块，因此无需重型生成式动作专家。Light-WAM 只有 0.44B 可训练参数，推理延迟为 72.03 ms、峰值显存为 4.1 GiB；它在 LIBERO 上保持竞争力，并在 RoboTwin 2.0 的 50 项任务上获得可用表现。

## 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Vision-Language-Action models map visual observations and language instructions to robot actions. WAMs add future-video prediction, providing supervision for object motion, interaction dynamics, and task progress. The benefit is richer temporal representation; the cost is that many current systems couple video and action generation inside large generative architectures.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 视觉—语言—动作模型把视觉观测和语言指令映射为机器人动作。WAM 在此基础上加入未来视频预测，为物体运动、交互动力学和任务进度提供监督。其收益是更丰富的时间表征，代价则是许多现有系统把视频与动作生成耦合在大型生成架构中。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Recent evidence suggests that future-video generation need not be executed at test time for strong policy performance. This implies that the principal value of video prediction may lie in training-time representation learning rather than explicit online imagination. Light-WAM asks whether this training benefit can be retained in a substantially cheaper policy.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 近期研究表明，强策略性能并不一定要求测试时执行未来视频生成。这意味着视频预测的主要价值可能来自训练阶段的表征学习，而不是在线显式想象。Light-WAM 进一步追问：能否在显著降低策略成本的同时保留这种训练收益？

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Light-WAM adopts Wan2.1-T2V-1.3B as a frozen video backbone and adds lightweight adaptation modules. Future-video supervision is performed on downsampled latents. At inference, the model receives only the current observation and directly predicts an action chunk; it neither rolls out a future video nor iteratively denoises an action trajectory.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Light-WAM 使用冻结的 Wan2.1-T2V-1.3B 作为视频骨干，并添加轻量适配模块。未来视频监督作用在下采样的潜变量上。推理时，模型只接收当前观测并直接预测动作块：既不展开未来视频，也不对动作轨迹进行迭代去噪。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The proposed StateFusionActionExpert samples adapted hidden states from several backbone depths, pools dense tokens with learned queries, fuses the pooled states, and maps them to horizon-indexed actions. The paper evaluates both performance and the full training/inference cost, emphasizing a performance-efficiency trade-off rather than state-of-the-art success alone.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 所提出的 StateFusionActionExpert 从多个骨干深度取得适配后的隐藏状态，以可学习 query 汇聚密集 token，融合得到的状态，并映射为按时域位置索引的动作。论文同时评估任务性能以及完整的训练/推理成本，关注的是性能—效率权衡，而不只是最高成功率。

## 2. Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Efficient VLA policies such as SmolVLA and VLA-Adapter reduce the cost of adapting vision-language representations to action prediction. However, these methods are primarily optimized with action supervision, so temporal task structure must be learned implicitly from demonstrations.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> SmolVLA 和 VLA-Adapter 等高效 VLA 策略降低了视觉—语言表征适配到动作预测的成本。不过，这类方法主要依靠动作监督优化，因此任务的时间结构只能从示范中隐式学习。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> WAMs instead couple action learning with a future-video target. Motus, LingBot-VA, Fast-WAM, and related systems demonstrate the value of this temporal supervision, but many use large video-action generators or expensive action experts. Light-WAM follows Fast-WAM's observation that the video branch can be training-only, then focuses on making the entire WAM pipeline smaller and faster.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> WAM 则把动作学习与未来视频目标结合。Motus、LingBot-VA、Fast-WAM 等系统证明了这种时间监督的价值，但许多方法使用大型视频—动作生成器或昂贵的动作专家。Light-WAM 延续 Fast-WAM“视频分支可以只在训练时使用”的观察，并进一步把重点放在整个 WAM 流水线的轻量化与加速上。

### Figure 1. Light-WAM overall architecture

![Figure 1](assets/page_003_fig_figure_1.png)

**Caption:** Light-WAM shares an adapted video backbone between video co-training and action prediction. The video branch uses downsampled future-video latents during training; the action branch uses the full-resolution current observation in training and inference. Multi-level adapted states are fused through learned-query pooling for single-pass action decoding.

**Caption[CN]:** Light-WAM 在视频协同训练与动作预测之间共享一个经过适配的视频骨干。训练时，视频分支使用下采样的未来视频潜变量；训练和推理中的动作分支均使用原分辨率当前观测。多层适配状态通过可学习查询池化进行融合，并以单次前向解码动作。

**Reading note:** 左支路是训练期的时间监督，右支路才是在线策略路径；两者共享骨干，但使用的输入分辨率与执行阶段不同。

## 3. Methodology

### 3.1 Overview

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Given observation $o$, instruction $l$, and proprioceptive state $p$, Light-WAM predicts an action sequence with the following composition.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 给定观测 $o$、指令 $l$ 和本体状态 $p$，Light-WAM 按下面的组合关系预测动作序列。

$$
\hat A=\pi_\phi\bigl(h_\theta(o,l,p)\bigr),
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Here $h_\theta$ denotes multi-level features from the adapted video backbone and $\pi_\phi$ is the StateFusionActionExpert. The backbone supplies a video prior, while the action expert forms a direct, non-iterative control interface.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 其中，$h_\theta$ 表示适配视频骨干产生的多层特征，$\pi_\phi$ 是 StateFusionActionExpert。视频骨干提供视频先验，动作专家则构成直接、非迭代的控制接口。

### 3.2 Video Backbone Adaptation

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The VAE latent $z$ is converted to a token state $H_0=\mathrm{PatchEmbed}(z)\in\mathbb R^{B\times N\times d}$. Text tokens and the projected proprioceptive token are concatenated as cross-attention context $C=[c_1,\ldots,c_L,c_{\mathrm{prop}}]$.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> VAE 潜变量 $z$ 经 patch embedding 转为 $H_0\in\mathbb R^{B\times N\times d}$。文本 token 与投影后的本体状态 token 拼接成交叉注意力上下文 $C=[c_1,\ldots,c_L,c_{\mathrm{prop}}]$。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The original Wan backbone remains frozen. LoRA updates are applied to self-attention, cross-attention, and feed-forward projections throughout the backbone. Additional bottleneck WAM adapters are inserted only at selected depths $\mathcal I=\{8,16,24\}$:

$$
U_\ell=F_\ell(H_{\ell-1},C),\qquad
H_\ell=
\begin{cases}
U_\ell+A_\ell(U_\ell),&\ell\in\mathcal I,\\
U_\ell,&\text{otherwise}.
\end{cases}
$$

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 原始 Wan 骨干保持冻结。模型在各层的自注意力、交叉注意力和前馈投影上施加 LoRA 更新，并只在 $\mathcal I=\{8,16,24\}$ 三个深度插入瓶颈式 WAM adapter。这样，LoRA 提供全骨干范围的低秩适配，稀疏 adapter 则为机器人领域提供额外容量。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The action branch reads only the selected adapted states $\mathcal H=\{H_\ell\}_{\ell\in\mathcal I}$. This sparse multi-level interface exposes different visual granularities without forwarding every backbone activation to the action decoder.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 动作分支只读取选定的适配状态 $\mathcal H=\{H_\ell\}_{\ell\in\mathcal I}$。这种稀疏多层接口让动作解码器接触不同粒度的视觉信息，同时避免传递骨干的全部中间激活。

### 3.3 Efficient Latent Video Co-training

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Let $\bar z_{\mathrm{vid}}=D(z_{\mathrm{vid}})$ denote the spatially downsampled video latent and $\bar z_t$ its flow-matching perturbation. The training-only video branch minimizes

$$
\mathcal L_{\mathrm{video}}=
\left\|G^{\mathrm{vid}}_\theta(\bar z_t,t,C)-u_t\right\|_2^2.
$$

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 令 $\bar z_{\mathrm{vid}}=D(z_{\mathrm{vid}})$ 表示空间下采样的视频潜变量，$\bar z_t$ 表示其 flow-matching 扰动。只在训练阶段启用的视频分支用上式学习对应的速度目标 $u_t$。首个潜在帧同样经过下采样，并在扰动中保持固定，作为当前观测锚点。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The action path does not use this additionally downsampled future-video input. It takes the original-resolution current latent $z_{\mathrm{act}}=z^{(0)}_{\mathrm{vid}}$. Consequently, temporal supervision is made cheaper, while the policy retains the spatial detail of the current observation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 动作路径并不使用额外下采样的未来视频输入，而是读取原分辨率的当前潜变量 $z_{\mathrm{act}}=z^{(0)}_{\mathrm{vid}}$。因此，模型以较低成本获得时间监督，同时让策略保留当前观测中的空间细节。

### 3.4 Query-Bottlenecked State Fusion and Action Decoding

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For every selected state $H_\ell$, the action expert maintains $N_q$ learned query tokens $Q_\ell$. They attend to dense video tokens, after which the query outputs are averaged and normalized:

$$
P_\ell=\mathrm{MHA}(Q_\ell,H_\ell,H_\ell),\qquad
s_\ell=\mathrm{LN}\left(\frac{1}{N_q}\sum_{j=1}^{N_q}P_{\ell,j}\right).
$$

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 对每个选中状态 $H_\ell$，动作专家维护 $N_q$ 个可学习查询 $Q_\ell$。这些 query 对密集视频 token 做注意力，所得查询输出再取平均并归一化。它形成一个受控信息瓶颈：query 太少会损失操作细节，太多则削弱压缩作用并增加动作头负担。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Level-wise states are projected, concatenated, fused, and processed by a lightweight trunk:

$$
h=\phi_{\mathrm{trunk}}\left(\phi_{\mathrm{fuse}}([M_\ell(s_\ell)]_{\ell\in\mathcal I})\right).
$$

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 各层状态先投影，再拼接和融合，最后由轻量 trunk 处理得到统一状态 $h$。默认配置中，第 8、16、24 层分别使用 16 个 query 和 8 头注意力；每层池化状态投影为 4608 维，拼接后映射为 6144 维融合状态。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> A step embedding $e_k$ identifies each action position. The model adds its projection to the fused state and directly regresses the corresponding action:

$$
r_k=h+\psi(e_k),\qquad
\hat a_k=\phi_{\mathrm{out}}(\mathrm{LN}(r_k)),\qquad
\hat A=[\hat a_1,\ldots,\hat a_K].
$$

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 步位置嵌入 $e_k$ 标识动作块中的每个时间位置。其投影与融合状态相加后，输出头直接回归对应动作。RoboTwin 2.0 的默认输出是 $24\times14$ 动作块，不需要扩散或 flow-based 动作去噪。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The complete objective is

$$
\mathcal L=\mathcal L_{\mathrm{video}}+\lambda\mathcal L_{\mathrm{action}}(\hat A,A).
$$

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 总目标由未来视频 flow-matching 损失和动作回归损失组成。推理时删除视频监督支路，只运行当前观测骨干前向与直接动作解码。

## 4. Experiments

### 4.1 Experimental Setup

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> LIBERO evaluation uses the four official suites: Spatial, Object, Goal, and Long. RoboTwin 2.0 trains one policy over 50 bimanual tasks using 2,500 clean demonstrations and 25,000 randomized demonstrations, and reports clean and randomized success rates.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> LIBERO 评估使用 Spatial、Object、Goal、Long 四个官方套件。RoboTwin 2.0 则用 2,500 条干净示范和 25,000 条随机化示范训练一个覆盖 50 项双臂任务的统一策略，并分别报告干净环境和随机化环境成功率。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The default model inserts adapters at layers $\{8,16,24\}$, uses 16 queries per layer, and downsamples video latents by $2\times$. It has 1.99B total and 0.44B trainable parameters. Training uses AdamW, learning rate $10^{-4}$, weight decay $10^{-2}$, and four H100 GPUs; inference is measured on one RTX 4090 48GB GPU.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 默认模型在第 $\{8,16,24\}$ 层插入 adapter，每层使用 16 个 query，并将视频潜变量做 $2\times$ 空间下采样。模型共有 1.99B 参数，其中 0.44B 可训练。训练使用 AdamW、$10^{-4}$ 学习率、$10^{-2}$ 权重衰减和 4 张 H100；推理在单张 RTX 4090 48GB 上测量。

### 4.2 LIBERO Results

### Table 1. LIBERO success rates

![Table 1](WorldModel/Light-WAM%20Efficient%20World%20Action%20Models%20with%20State-Fusion%20Action%20Decoding/assets/page_006_fig_table_1.png)

**Caption:** Success rates on four LIBERO suites, including ranks among methods without embodied pretraining and among all compared methods.

**Caption[CN]:** 四个 LIBERO 套件上的成功率，同时报告无具身预训练方法排名与总体排名。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Light-WAM reaches 98.2 on Spatial, 99.6 on Object, 97.8 on Goal, and 93.0 on Long, averaging 97.2. It ranks first among methods without embodied pretraining and third overall. Motus and LingBot-VA are stronger on Long, indicating that model capacity and embodied pretraining remain useful for difficult long-horizon behavior.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Light-WAM 在 Spatial、Object、Goal、Long 上分别达到 98.2、99.6、97.8、93.0，平均 97.2。它在无具身预训练方法中排名第一，总体排名第三。Motus 和 LingBot-VA 在 Long 上更强，说明模型容量与具身预训练对困难的长时程行为仍然有帮助。

### 4.3 Multi-task Learning on RoboTwin 2.0

### Table 2. RoboTwin 2.0 success rates

![Table 2](assets/page_006_fig_table_2_clean.png)

**Caption:** Clean, randomized, and average success across 50 RoboTwin 2.0 tasks.

**Caption[CN]:** RoboTwin 2.0 的 50 项任务在干净环境、随机化环境及二者平均值上的成功率。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Light-WAM obtains 76.4% clean, 76.3% randomized, and 76.4% average success. It outperforms $\pi_0$ and X-VLA and is close to Motus without embodied pretraining, but it remains below $\pi_{0.5}$, LingBot-VA, and Fast-WAM. The result is therefore evidence of usable performance under a small trainable budget, not state-of-the-art RoboTwin accuracy.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Light-WAM 在干净环境、随机化环境和平均成功率上分别为 76.4%、76.3%、76.4%。它超过 $\pi_0$ 与 X-VLA，接近无具身预训练的 Motus，但低于 $\pi_{0.5}$、LingBot-VA 和 Fast-WAM。因此，这一结果证明的是小可训练参数预算下的可用性能，而非 RoboTwin 上的最高准确率。

### Figure 2. Efficiency–performance trade-off

![Figure 2](assets/page_006_fig_figure_2.png)

**Caption:** RoboTwin 2.0 average success plotted against overall latency, with peak memory encoded by color.

**Caption[CN]:** RoboTwin 2.0 平均成功率与总体延迟的关系，颜色表示峰值显存。

**Reading note:** Light-WAM 位于低延迟、低显存区域；Fast-WAM 成功率更高，但延迟和显存也更高。

### 4.4 Efficiency Analysis

### Table 3. Training efficiency

![Table 3](assets/page_007_fig_table_3.png)

**Caption:** Training cost decomposition on four H100 GPUs with effective global batch size 64.

**Caption[CN]:** 在 4 张 H100、有效全局 batch size 64 条件下的训练成本分解。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Relative to Fast-WAM, the complete Light-WAM reduces loaded parameters from 6.73B to 1.99B, trainable parameters from 6.02B to 0.44B, and peak per-GPU memory from 70.7 to 43.1 GiB. Throughput increases from 0.49 to 2.08 steps/s, or 4.25 times the Fast-WAM reference.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 相比 Fast-WAM，完整 Light-WAM 把训练时加载参数从 6.73B 降至 1.99B，把可训练参数从 6.02B 降至 0.44B，把单卡峰值显存从 70.7 GiB 降至 43.1 GiB。吞吐从 0.49 steps/s 提升到 2.08 steps/s，即 Fast-WAM 的 4.25 倍。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> A compact video backbone alone is insufficient: the Light-WAM variant with a DiT action head runs at only 0.43 steps/s, slightly slower than Fast-WAM. Replacing the action head with StateFusion raises normalized throughput to 1.14 times; latent caching raises it to 1.76 times; adding $2\times$ video downsampling reaches 4.25 times. The efficiency gain is therefore a pipeline result, not merely a smaller-backbone result.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 仅使用紧凑视频骨干并不够：带 DiT 动作头的 Light-WAM 变体只有 0.43 steps/s，甚至略慢于 Fast-WAM。将动作头替换为 StateFusion 后，归一化吞吐升至 1.14 倍；加入潜变量缓存后升至 1.76 倍；再加入 $2\times$ 视频下采样才达到 4.25 倍。因此，效率提升来自整条流水线，而不只是更小的骨干。

### Table 4. Inference efficiency

![Table 4](assets/page_007_fig_table_4.png)

**Caption:** Per-query inference latency and peak memory on one RTX 4090 48GB GPU with cached language context.

**Caption[CN]:** 在单张 RTX 4090 48GB、缓存语言上下文时，每次动作查询的推理延迟和峰值显存。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Light-WAM spends 12.7 ms on VAE encoding, 56.5 ms on the visual branch, and only 2.1 ms on the action branch. Overall latency is 72.03 ms with 4.1 GiB peak memory. Fast-WAM requires 404.62 ms and 12.7 GiB, mainly because its action branch takes 356.8 ms. Simulator and I/O overhead are excluded.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Light-WAM 的 VAE 编码、视觉分支和动作分支分别耗时 12.7 ms、56.5 ms、2.1 ms，总延迟为 72.03 ms，峰值显存为 4.1 GiB。Fast-WAM 则需要 404.62 ms 和 12.7 GiB，其中动作分支独占 356.8 ms。上述测量不包含仿真器和 I/O 开销。

### 4.5 Ablation Studies

### Table 5. Design ablations

![Table 5](assets/page_007_fig_table_5.png)

**Caption:** Ablations on LIBERO-Spatial for video downsampling, adapter depth, and query capacity.

**Caption[CN]:** 在 LIBERO-Spatial 上对视频下采样、adapter 层数和 query 容量进行消融。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Full-resolution video supervision improves success from 98.2 to 99.0 but increases training cost. Adding two more adapter layers changes success from 98.2 to 98.0, showing no clear gain. Reducing learned queries from 16 to 8 lowers success to 95.4, a 2.8-point drop, indicating that the query bottleneck needs sufficient capacity.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 使用原分辨率视频监督可将成功率从 98.2 提升到 99.0，但会显著增加训练成本。额外增加两个 adapter 层后，成功率从 98.2 变为 98.0，没有明确收益。将每层 query 数从 16 减少到 8，则成功率降至 95.4，下降 2.8 个百分点，说明查询瓶颈必须保留足够容量。

### 4.6 Qualitative Analysis

### Figure 3. Future-video and learned-query visualizations

![Figure 3](assets/page_008_fig_figure_3.png)

**Caption:** Top: predicted future frames versus rollout references at offsets $\{+8,+16,+24,+32\}$. Bottom: learned-query attention visualizations from layers 8, 16, and 24.

**Caption[CN]:** 上：在 $\{+8,+16,+24,+32\}$ 时间偏移处比较预测未来帧与环境轨迹参考帧。下：第 8、16、24 层可学习查询的注意力可视化。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Downsampled-latent predictions are smoother than reference frames, but preserve the dominant motion and scene changes. Query attention from different backbone levels emphasizes complementary regions such as manipulated objects, grippers, and targets. These visualizations are consistent with the intended temporal supervision and multi-level fusion, though they are qualitative rather than causal evidence.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 下采样潜空间产生的预测比参考帧更平滑，但保留了主要运动和场景变化。不同骨干层的查询注意力会强调被操作物体、夹爪和目标区域等互补位置。这些现象与时间监督和多层融合的设计意图一致，但仍是定性证据，而非因果证明。

### 4.7 Real-world Evaluation

### Figure 4. IMETA Y1 dual-arm evaluation

![Figure 4](assets/page_008_fig_figure_4.png)

**Caption:** Three real-world dual-arm tasks with 50 training demonstrations per task, comparing Light-WAM with $\pi_{0.5}$.

**Caption[CN]:** 三项真实双臂任务，每项使用 50 条训练示范，并比较 Light-WAM 与 $\pi_{0.5}$。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> On clearing a paper ball into a trash bin, stacking bowls and placing them in a basket, and handing off a water bottle into a basket, Light-WAM reaches 67%, 87%, and 53%, while $\pi_{0.5}$ reaches 80%, 93%, and 60%. Light-WAM is therefore usable on the three real tasks but does not outperform the baseline. The paper does not state the number of evaluation trials in the main text.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在把纸团清入垃圾桶、叠碗后放入篮子、把水瓶交接并放入篮子三项任务中，Light-WAM 分别达到 67%、87%、53%，而 $\pi_{0.5}$ 为 80%、93%、60%。因此，Light-WAM 在三项真机任务上具备可用性，但没有超过基线。正文没有说明每项任务的评估试验次数。

## 5. Conclusion and Limitations

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Light-WAM combines a compact frozen video backbone, downsampled latent future-video supervision, and direct state-fusion action decoding. The result is a favorable efficiency-performance trade-off across LIBERO, RoboTwin 2.0, and three dual-arm tasks.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Light-WAM 结合紧凑且冻结的视频骨干、下采样潜空间的未来视频监督，以及直接的状态融合动作解码，在 LIBERO、RoboTwin 2.0 和三项双臂任务上形成了较好的性能—效率权衡。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Larger WAMs and embodied-pretrained policies remain more accurate in challenging multi-task settings. The study also does not evaluate benchmarks designed specifically for robustness and policy generalization, such as LIBERO-Plus. The authors propose data augmentation and robustness-oriented training as future directions.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在困难的多任务环境中，更大的 WAM 与具身预训练策略仍然更准确。论文也没有在 LIBERO-Plus 等专门面向鲁棒性和策略泛化的基准上评测。作者将数据增强与鲁棒性导向训练列为后续方向。

## Appendix A. Algorithmic Details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Training on RoboTwin constructs a canvas from three camera streams and subsamples observations $I_{0:32}$ with stride four, producing frames $[I_0,I_4,\ldots,I_{32}]$. Cached Wan VAE latents are used when available. The downsampled future-video latent receives flow-matching noise while its first latent frame remains fixed; the original-resolution first frame is separately passed through the adapted backbone for action prediction.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> RoboTwin 训练把三路相机图像组成一个画布，并以步长 4 对 $I_{0:32}$ 进行抽帧，得到 $[I_0,I_4,\ldots,I_{32}]$。若缓存可用，则直接读取 Wan VAE 潜变量。下采样未来视频潜变量接受 flow-matching 加噪，同时固定首个潜在帧；原分辨率首帧则另行通过适配骨干用于动作预测。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> At inference, the current multi-camera observation is encoded as a single-frame latent. The model builds context from 128 language tokens and the proprioceptive token, performs one adapted-backbone forward pass, collects layers $\{8,16,24\}$, predicts a complete action chunk, and executes it. No future video is generated.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 推理时，当前多相机观测被编码成单帧潜变量。模型用 128 个语言 token 和本体状态 token 构造上下文，执行一次适配骨干前向，收集第 $\{8,16,24\}$ 层状态，预测完整动作块并执行。整个过程不生成未来视频。

## Appendix B. Training and Parameters

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The bottleneck width of each WAM adapter is 256 and its residual scale is $\gamma=1$. Training uses a cosine learning-rate schedule with 1,000 warmup steps. LIBERO checkpoints are selected at 60K steps for Spatial and Goal, 12.5K for Object, and 80K for Long; RoboTwin evaluation uses the 460K-step checkpoint.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 每个 WAM adapter 的瓶颈宽度为 256，残差缩放系数为 $\gamma=1$。训练采用含 1,000 个 warmup step 的余弦学习率日程。LIBERO 的 Spatial/Goal、Object、Long 分别选择 60K、12.5K、80K step 的 checkpoint；RoboTwin 使用 460K-step checkpoint。

### Table 6. Parameter breakdown

![Table 6](assets/page_014_fig_table_6.png)

**Caption:** Total, trainable, and frozen parameter counts by component.

**Caption[CN]:** 各组件的总参数、可训练参数与冻结参数。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The total model contains 1,986.82M parameters, of which 441.03M are trainable and 1,545.79M are frozen. StateFusionActionExpert contributes 351.03M trainable parameters and LoRA contributes 87.49M; the sparse WAM adapters themselves contain only 2.37M.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 模型共含 1,986.82M 参数，其中 441.03M 可训练、1,545.79M 冻结。StateFusionActionExpert 自身包含 351.03M 可训练参数，LoRA 包含 87.49M；稀疏 WAM adapter 只有 2.37M。因此，“轻量”主要是相对重型生成动作专家而言，并不意味着动作头非常小。

## Appendix C. Full RoboTwin 2.0 Results

### Table 7. Per-task results

![Table 7](assets/page_014_fig_table_7.png)

**Caption:** Clean and randomized success rates for all 50 RoboTwin 2.0 tasks.

**Caption[CN]:** RoboTwin 2.0 全部 50 项任务在干净和随机化环境下的成功率。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Per-task results show that Light-WAM is perfect or near-perfect on several short, visually clear interactions, but falls far behind Fast-WAM on tasks such as Hanging Mug, Move Stapler Pad, Stack Blocks Three, and Turn Switch. The average gap is therefore distributed across many difficult tasks rather than caused by one isolated failure.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 逐任务结果显示，Light-WAM 在若干较短、视觉目标明确的交互中接近满分，但在 Hanging Mug、Move Stapler Pad、Stack Blocks Three、Turn Switch 等任务上明显落后于 Fast-WAM。因此，平均性能差距来自多项困难任务的累积，而不是某个孤立失败。

## Appendix D. Real-World Rollouts

### Figure 5. Additional real-world rollouts

![Figure 5](assets/page_015_fig_figure_5.png)

**Caption:** Rollout frames for three dual-arm tasks and predicted future frames compared with ground-truth futures.

**Caption[CN]:** 三项双臂任务的执行轨迹，以及预测未来帧与真实未来帧的对比。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The rollout panels confirm that the policy can complete coordinated dual-arm behaviors. The training-only future predictions are noticeably blurred because of latent downsampling, yet preserve rough object and arm motion. Since these frames are not generated online for action selection, their value is representational rather than photorealistic.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 执行轨迹表明策略能够完成协调的双臂行为。由于潜变量下采样，训练期未来预测存在明显模糊，但仍保留大致的物体与机械臂运动。因为这些帧不会在动作选择时在线生成，所以它们的价值在于塑造表征，而不是追求照片级真实感。

## References

参考文献共 38 条，见原 PDF 第 9–12 页。为保持阅读连续性，本读者版不逐条翻译书目，但保留正文中对 VLA、WAM、LoRA、flow matching、query pooling 与各基线的归属关系。

## Critical Reading Notes

1. Light-WAM 的核心贡献是把 WAM 拆成“训练期低成本视频监督”和“推理期直接动作解码”，而不是提出更强的未来视频生成器。
2. 4.25 倍训练吞吐来自 StateFusion、潜变量缓存与视频下采样的叠加；只换小视频骨干并不会自动加速。
3. 0.44B 是可训练参数，不是总参数；模型部署仍需加载约 1.99B 参数。
4. RoboTwin 与真机结果都低于更强基线，因此本文的结论应表述为更优效率—性能折中，而非全面性能领先。
5. LIBERO 接近饱和，且各 suite 使用不同 checkpoint；论文没有报告多 seed 方差，97.2 与 97.0 等小差异不宜过度解释。
6. 真机实验只覆盖三项任务、每项 50 条训练示范，正文未报告评估试验次数，无法判断柱状图差异的统计稳定性。
