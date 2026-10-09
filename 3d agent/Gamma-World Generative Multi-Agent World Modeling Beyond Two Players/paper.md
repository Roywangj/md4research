---
title: "Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players"
authors: "Fangfu Liu, Kai He, Tianchang Shen, Tianshi Cao, Sanja Fidler, Yueqi Duan, Jun Gao, Igor Gilitschenski, Zian Wang, Xuanchi Ren"
source: "local PDF / arXiv:2605.28816v1"
source_path: "/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/3IADU9J6/Liu 等 - 2026 - Gamma-World Generative Multi-Agent World Modeling Beyond Two Players.pdf"
reader_type: "nature-reader bilingual markdown"
created: "2026-06-24"
---

# Gamma-World: Generative Multi-Agent World Modeling Beyond Two Players

**Paper type:** 方法/算法论文，目标是可实时交互的生成式多智能体视频世界模型。

**One-sentence map:** 这篇论文把“多玩家/多机器人共享世界”作为世界模型的新基本单位，用单纯形 RoPE 保持智能体身份的可交换性，用 hub attention 控制跨智能体通信成本，再用 teacher-student/self-forcing distillation 做 24 FPS 级实时 rollout。

## Page / section index

| Pages | Section | What to look for |
|---|---|---|
| 1 | Title, Fig. 1, Abstract | Problem framing and the three design claims |
| 2-3 | Introduction, Related Work, Method start | Why multi-agent world modeling differs from single-agent video prediction |
| 4-7 | Method | Fig. 2, Simplex Rotary Agent Encoding, Sparse Hub Attention, teacher-student training |
| 8-10 | Experiments | Tables 1-2, Fig. 3-4, quantitative/qualitative evaluation |
| 11 | Discussion | Fig. 5-6, four-agent zero-shot scaling, robotics examples, limitations |
| 12-17 | Appendix | Proof, action design, architecture/training details, extra ablations |
| 18-21 | References | Bibliography preserved in original form |

## Terminology ledger

| Canonical term | 中文对应 | Decision / note |
|---|---|---|
| γ-World | γ-World | 本文提出的生成式多智能体世界模型；保留希腊字母命名。 |
| generative multi-agent world model | 生成式多智能体世界模型 | 生成多个智能体视角下未来视频/观测的交互式模拟模型。 |
| Simplex Rotary Agent Encoding | 单纯形旋转智能体编码 | 参数-free 的智能体身份编码，把智能体放在 RoPE 角度空间的正单纯形顶点。 |
| Sparse Hub Attention | 稀疏枢纽注意力 | 用少量 hub tokens 作为共享通信状态，避免跨智能体 dense all-to-all attention。 |
| permutation-symmetric / exchangeable | 置换对称 / 可交换 | 智能体身份不应因 slot 顺序而被赋予结构性偏差。 |
| RoPE | 旋转位置编码 | Rotary Position Embedding；本文从 3D RoPE 扩展到带 agent 轴的 4D RoPE。 |
| DiT | 扩散 Transformer | Diffusion Transformer；论文以 latent video diffusion transformer 为基础。 |
| Diffusion Forcing | 扩散强制 | 将 next-token 式自回归与全序列扩散结合的训练框架。 |
| Self-Forcing | 自强制蒸馏 | 让学生模型在自己的 rollout 历史上训练，减少训练-测试暴露偏差。 |
| KV cache | 键值缓存 | 流式自回归推理中缓存历史 token 的 key/value 状态。 |
| FVD / FID | 视频/图像分布距离指标 | 越低越好；用于评估生成质量。 |
| LPIPS / PSNR / SSIM | 感知/像素级质量指标 | LPIPS 越低越好，PSNR/SSIM 越高越好。 |
| DMD | 分布匹配蒸馏 | Distribution Matching Distillation，用于 few-step 生成蒸馏。 |

## Title figure and Abstract

### Fig. 1. 从虚拟游戏到真实世界的多智能体世界模型

![Fig. 1](3d%20agent/Gamma-World%20Generative%20Multi-Agent%20World%20Modeling%20Beyond%20Two%20Players/assets/fig1.png)

**Caption:** Figure 1: We propose γ-World, a novel generative multi-agent world model from virtual games to real-world environments. More results and video demos are available on our project page.

**Caption[CN]:** 图 1：作者提出 γ-World，这是一种从虚拟游戏到真实世界环境的生成式多智能体世界模型。更多结果和视频演示见项目主页。

**Reading note:** 先看两件事：上半部分展示多玩家游戏中的多视角同步生成，下半部分展示真实机器人协作场景；这正对应论文的两个应用域。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> World models for interactive video generation have largely focused on single-agent settings, where future observations are generated from a single control signal. However, many generated environments require multi-agent interaction: multiple players, robots, or embodied agents act simultaneously within a shared space. Scaling world models to such settings requires a principled multi-agent design: agents should remain independently controllable, permutation-symmetric, and support efficient inference while maintaining consistency across time and perspectives. In this paper, we present γ-World, a generative multi-agent world model for interactive simulation. γ-World introduces Simplex Rotary Agent Encoding, a parameter-free extension of 3D RoPE that represents agents as vertices of a regular simplex in rotary angle space. This gives each agent a distinct phase while making all agents permutation-equivalent, enabling scalable agent identity without learned per-slot identities or a fixed agent ordering. To avoid dense all-to-all attention across agents, we further propose Sparse Hub Attention, where learnable hub tokens mediate token-interaction across agents, reducing cross-agent attention cost from quadratic to linear in the number of agents. For real-time rollout, we distill a full-context diffusion teacher into a causal student that generates temporal blocks sequentially with KV caching, enabling action-responsive generation at 24 FPS. Experiments in multiplayer virtual environments show that γ-World improves video fidelity, action controllability, and inter-agent consistency over slot-based and dense-attention baselines, while generalizing from two to four players without additional training.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 交互式视频生成的世界模型长期主要关注单智能体设定：未来观测由单一路径的控制信号驱动。但许多可生成环境天然需要多智能体互动：多个玩家、机器人或具身智能体会在同一共享空间中同时行动。把世界模型扩展到这种设定，需要一个有原则的多智能体设计：每个智能体要能独立控制，身份表示要满足置换对称，并且推理要高效，同时还要维持时间维度和多视角之间的一致性。本文提出 γ-World，一种用于交互式模拟的生成式多智能体世界模型。γ-World 引入 Simplex Rotary Agent Encoding，这是 3D RoPE 的一种无参数扩展，它把智能体表示为旋转角空间中正单纯形的顶点。这样每个智能体都有独立相位，同时所有智能体在置换意义下等价，从而不需要 learned per-slot identity 或固定 agent 顺序。为避免智能体之间的 dense all-to-all attention，作者进一步提出 Sparse Hub Attention，用可学习 hub tokens 作为跨智能体 token 交互的中介，将跨智能体注意力成本从随智能体数二次增长降为线性增长。为了实时 rollout，作者把 full-context diffusion teacher 蒸馏成 causal student，使其通过 KV cache 顺序生成时间块，从而实现对动作响应的 24 FPS 生成。多人虚拟环境实验显示，γ-World 相比 slot-based 和 dense-attention baseline，在视频保真度、动作可控性和跨智能体一致性上都有提升，并能在不额外训练的情况下从两玩家泛化到四玩家。

## 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The worlds we wish to simulate are populated, not solitary. Players cooperate and compete in the same game, robot arms coordinate around shared objects, and embodied agents act under mutual physical and visual constraints. Controllable multi-agent world modeling is therefore a necessary step toward multiplayer game generation, interactive simulation, and embodied AI.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 作者从问题定义开始：我们希望模拟的世界不是“孤立单体”的，而是由多个行动者共同占据的。玩家在同一游戏中协作或竞争，机械臂围绕共享物体协调动作，具身智能体也会受到彼此的物理和视觉约束。因此，可控的多智能体世界建模，是多人游戏生成、交互式模拟和具身 AI 的必要一步。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Most video world models remain single-agent simulators: they roll out future observations conditioned on one action stream, one user input, or one controllable viewpoint. Moving from single-agent to multi-agent simulation raises a new consistency requirement: generated observations must be consistent not only across time, but also across agent perspectives, since all agents share and act upon the same evolving world.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 现有多数视频世界模型仍是单智能体模拟器：它们根据一条动作流、一个用户输入或一个可控视角来生成未来观测。从单智能体推进到多智能体，会带来新的“一致性”要求：生成的观测不仅要在时间上连贯，还要在不同智能体视角之间一致，因为所有智能体都在同一个不断演化的世界中观察和行动。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Solaris is a concurrent effort that builds a multiplayer Minecraft world model by combining dense joint attention over all agent tokens with learned per-player ID embeddings. This works in the two-player setting, but has two structural limitations: dense joint attention grows quadratically with the number of agents, and learned per-slot IDs violate the exchangeability of agents while tying the model to a fixed roster.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 论文把 Solaris 作为最接近的并行工作：它通过对所有 agent tokens 做 dense joint attention，并叠加 learned per-player ID embedding，构建多人 Minecraft 世界模型。这个设计在两玩家设定下有效，但有两个结构性限制：第一，dense joint attention 的成本随智能体数量二次增长，难以扩展到两人以上的实时 rollout；第二，共享世界中的智能体本质上是可交换的，而 learned per-slot ID 会破坏这种对称性，并把模型绑定到固定玩家列表。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> γ-World addresses whether a video world model can represent multiple agents in a way that is individually controllable, permutation-symmetric, and scalable beyond two players. It extends 3D RoPE with an explicit agent axis through Simplex Rotary Agent Encoding: agents are placed at the vertices of a regular simplex in rotary angle space, so every pair is permutation-equivalent while each agent retains a distinct phase.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> γ-World 试图回答一个核心问题：视频世界模型能否同时做到多智能体独立可控、置换对称，并能扩展到两人以上？作者用 Simplex Rotary Agent Encoding 在 3D RoPE 上加入显式 agent 轴：把智能体放在旋转角空间中正单纯形的顶点上。这样任意智能体对之间的几何关系等价，同时每个智能体仍保留不同相位。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Sparse Hub Attention complements the symmetric agent representation. Within each causal block, agent tokens attend to their own stream and to a small set of learnable hub tokens. Hub tokens aggregate information across agents and broadcast it back, preserving a shared communication pathway without dense pairwise interaction and reducing the dominant cross-agent cost from quadratic to linear in the number of agents.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> Sparse Hub Attention 与对称 agent 表示配套使用。在每个 causal block 内，agent tokens 只关注自身流和少量可学习 hub tokens；hub tokens 负责聚合来自多个智能体的信息并广播回去。这样仍保留共享通信通道，但避免了密集成对交互，把主导的跨智能体成本从二次增长降为线性增长。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> To make the model deployable as a real-time interactive simulator, the authors distill a bidirectional multi-agent teacher into a block-causal student with KV caching, enabling 24-FPS streaming autoregressive rollouts that respond to newly issued actions.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 为了让模型成为可部署的实时交互模拟器，作者把一个 bidirectional multi-agent teacher 蒸馏成带 KV cache 的 block-causal student，使其能够以 24 FPS 进行流式自回归 rollout，并响应新给出的动作。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> The evaluation covers two- and four-player multiplayer virtual environments involving movement, mining, combat, and building. γ-World improves video fidelity, action controllability, and inter-agent consistency, and scaling studies show two-to-four-player generalization without additional training.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 实验覆盖两玩家和四玩家的多人虚拟环境，包括移动、挖掘、战斗和建造等情境。结果显示 γ-World 提升了视频保真度、动作可控性和跨智能体一致性；扩展实验进一步显示模型可在不额外训练的情况下从两玩家泛化到四玩家。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span>
> - Simplex Rotary Agent Encoding: a parameter-free rotary identity encoding that preserves permutation symmetry while maintaining distinct agent identities.
> - Sparse Hub Attention: a cross-agent communication mechanism that reduces cross-agent attention cost from quadratic to linear in the number of agents.
> - Effective multi-agent simulation in two- and four-player environments, with ablations validating the agent encoding and efficiency design.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span>
> - 单纯形旋转智能体编码：一种无参数 rotary identity encoding，在保持不同智能体身份的同时维持置换对称。
> - 稀疏枢纽注意力：一种跨智能体通信机制，把跨智能体注意力成本从随智能体数二次增长降为线性增长。
> - 在两玩家和四玩家环境中实现有效多智能体模拟，并用消融实验证实 agent 编码与效率设计的作用。

## 2. Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Video generation. Diffusion-based generative models have become a leading approach for video generation. Latent diffusion improves efficiency, autoregressive video generation supports arbitrary-length sequences, and large-scale video generation systems have begun to show emergent zero-shot abilities to understand, model, and manipulate the visual world.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 视频生成方面，扩散式生成模型已经成为主流路线。Latent diffusion 提高了高质量视频合成的效率，自回归视频生成让任意长度序列成为可能，大规模视频生成系统也开始表现出对视觉世界进行理解、建模和操控的 zero-shot 能力。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Video world models repurpose video diffusion models as visual simulators that directly model future visual observations through generative video prediction. Representative applications span robotics, video games, autonomous driving, and physical simulation, and recent work moves from open-loop rollout toward interactive and temporally consistent world modeling.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 视频世界模型把视频扩散模型改造为视觉模拟器，直接通过生成式视频预测来建模未来视觉观测。代表性应用包括机器人、视频游戏、自动驾驶和物理模拟。近期工作也从 open-loop video rollout 逐渐走向能够响应用户或智能体动作、并保持长期时序一致性的交互式世界模型。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Real-time generation is crucial for world models. Video diffusion distillation accelerates sampling through few-step inference. CausVid transfers a bidirectional diffusion teacher to a causal student for real-time autoregressive generation, and Self-Forcing further reduces exposure bias during long-horizon rollout.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 实时生成是世界模型落地的关键。视频扩散模型蒸馏通过 few-step inference 加速采样；CausVid 把 bidirectional diffusion teacher 的知识转移到 causal student 上，用于实时自回归生成；Self-Forcing 则进一步减少长时 rollout 中累积的 exposure bias。

## 3. Method

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The task is synchronized action-conditioned multi-agent video generation. Formally, the model learns γ-World($\{o^p_{1:t}\}_{p=1}^P$, $\{a^p_{1:t}\}_{p=1}^P$), taking past observations and actions for $P$ agents and producing the next observation set $\{o^p_{t+1}\}_{p=1}^P$. The observations $\{o^p_t\}_{p=1}^P$ correspond to different perspectives of the same underlying world state.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 任务是同步的、动作条件化的多智能体视频生成。形式上，模型学习 γ-World($\{o^p_{1:t}\}_{p=1}^P$, $\{a^p_{1:t}\}_{p=1}^P$)：输入 $P$ 个智能体的历史观测和动作，输出下一时刻所有智能体的观测 $\{o^p_{t+1}\}_{p=1}^P$。这里的 $\{o^p_t\}_{p=1}^P$ 是同一个底层世界状态在不同智能体视角下的观测。

### Fig. 2. γ-World 方法总览：同步输入、单纯形 RoPE、稀疏 hub attention 与 causal student

![Fig. 2](3d%20agent/Gamma-World%20Generative%20Multi-Agent%20World%20Modeling%20Beyond%20Two%20Players/assets/fig2.png)

**Caption:** Figure 2: Method overview. γ-World takes synchronized observations and actions from multiple agents as input, tokenizes each agent stream with shared visual and action encoders, and generates future multi-agent rollouts with a causal multi-agent DiT. We formulate the input with an explicit synchronized agent axis, encode exchangeable agent identity using Simplex Rotary Agent Encoding (§3.2), and route cross-agent information through Sparse Hub Attention (§3.2). During streaming inference, the causal student uses KV caches for past visual tokens and hub states to preserve block-causal generation while scaling efficiently with the number of agents (§3.3).

**Caption[CN]:** 图 2：方法总览。γ-World 输入多个智能体的同步观测和动作，用共享视觉编码器与动作编码器分别 tokenize 每条 agent stream，再用 causal multi-agent DiT 生成未来多智能体 rollout。作者用显式同步 agent 轴组织输入，用 Simplex Rotary Agent Encoding 表示可交换的智能体身份，并用 Sparse Hub Attention 路由跨智能体信息。流式推理时，causal student 对历史视觉 token 和 hub 状态使用 KV cache，以保持 block-causal 生成并随智能体数量高效扩展。

**Reading note:** 这张图是全文的“电路图”：左侧是多 agent 同步输入，中间是 action/observation tokenization，右上是 causal student，底部显示 agent-axis simplex RoPE 和 hub attention mask。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The model builds on transformer-based latent video diffusion adapted for autoregressive generation. Standard spatial and temporal rotary position embeddings are modified to account for agent identities, and a multi-agent-aware attention mask reduces computation. Training proceeds in two steps conceptually: a bidirectional teacher is first trained, then distilled into a causal student that supports streaming.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 模型建立在可自回归生成的 transformer-based latent video diffusion 之上。作者修改原有的时空 RoPE，使其能够编码智能体身份；同时设计面向多智能体的 attention mask 来降低计算量。训练在概念上分为两步：先训练高质量 bidirectional teacher，再将其蒸馏为支持流式生成的 causal student。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Latent video diffusion. Let $z_0 \in \mathbb{R}^{T\times H\times W\times C_z}$ denote a clean video latent. With noise $\epsilon \sim \mathcal{N}(0,I)$ and noise level $\sigma \in [0,1]$, the flow-matching interpolant is $z_\sigma=(1-\sigma)z_0+\sigma\epsilon$, and the model trains a velocity field $v_\theta$ to regress $\epsilon-z_0$ under conditioning signals such as initial observations and agent actions.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 潜空间视频扩散。令 $z_0 \in \mathbb{R}^{T\times H\times W\times C_z}$ 表示干净视频 latent。给定噪声 $\epsilon \sim \mathcal{N}(0,I)$ 和噪声水平 $\sigma \in [0,1]$，flow-matching 插值为 $z_\sigma=(1-\sigma)z_0+\sigma\epsilon$；模型训练速度场 $v_\theta$ 去回归 $\epsilon-z_0$，条件信号包括初始观测和智能体动作。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Causal autoregressive video generation partitions the latent sequence into temporal blocks. Each block has an independent noise level, and each query attends only to keys from the same or earlier blocks. Attention remains bidirectional within a block, matching streaming inference where the current block is denoised conditioned on generated history.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 因果自回归视频生成把 latent 序列划分为时间块。每个块有独立噪声水平，每个 query 只能关注同一块或更早块的 key；块内部仍保持双向注意力。这与流式推理一致：当前块在已有生成历史条件下被反复去噪。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Standard video diffusion transformers use 3D RoPE to inject relative position into attention along time, height, and width. γ-World extends this coordinate system with an agent axis, turning the clean multi-agent latent into $Z_0 \in \mathbb{R}^{P\times T\times H\times W\times C_z}$.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 标准视频扩散 Transformer 使用 3D RoPE，在时间、高度、宽度三个轴上向 self-attention 注入相对位置信息。γ-World 在这个坐标系统中加入 agent 轴，将干净多智能体 latent 表示为 $Z_0 \in \mathbb{R}^{P\times T\times H\times W\times C_z}$。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Action conditioning uses a shared action encoder across agents. Each agent action $a^p_t$ is mapped to a hidden action feature $u^p_t=f_a(a^p_t)\in\mathbb{R}^D$. At transformer block $\ell$, this feature is projected into a layer-specific bias $\beta^p_{\ell,t}$ and broadcast to all spatial tokens for the corresponding agent and frame.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 动作条件化使用跨智能体共享的 action encoder。每个智能体动作 $a^p_t$ 被映射为隐藏动作特征 $u^p_t=f_a(a^p_t)\in\mathbb{R}^D$。在第 $\ell$ 个 transformer block 中，该特征被投影为层特定偏置 $\beta^p_{\ell,t}$，再广播到对应智能体与帧的所有空间 tokens 上。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> A scalar agent phase such as $\theta_p=p\omega$ places exchangeable agents on a one-dimensional line, making some pairwise distances different and some slots structurally special. Learned per-slot embeddings have another failure mode: they tie identity to a fixed roster and break permutation symmetry.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 如果直接使用标量 agent 相位（例如 $\theta_p=p\omega$），可交换智能体会被放在一条一维线上，导致不同智能体对的距离不一样，并让某些 slot 产生结构性特殊地位。learned per-slot embeddings 则有另一个问题：它把身份绑定到固定 roster，并破坏置换对称。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Simplex Rotary Agent Encoding represents agents as vertices of a regular simplex in rotary angle space. For a simplex pool of size $V$, the vertices are constructed in a $d_p/2$-dimensional agent-angle space as normalized centered one-hot vectors. The resulting vertices have unit norm and equal pairwise distance, so all distinct agent pairs are geometrically equivalent.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> Simplex Rotary Agent Encoding 把智能体表示为旋转角空间中正单纯形的顶点。给定大小为 $V$ 的 simplex pool，作者在 $d_p/2$ 维 agent-angle 空间中用归一化的 centered one-hot vectors 构造顶点。得到的顶点具有单位范数和相同的两两距离，因此任意不同智能体对在几何上都是等价的。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> For a batch with $P\le V$ active agents, an injective assignment maps each active agent to one unused simplex vertex. The agent-band rotation angles are $\theta_p=\alpha s_{\pi(p)}$, where $\alpha$ controls separation strength. This gives a parameter-free, permutation-symmetric 4D rotary operator with time, agent, height, and width bands.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 对于包含 $P\le V$ 个活跃智能体的 batch，作者用一个单射把每个智能体分配到未使用的 simplex 顶点。agent-band 的旋转角为 $\theta_p=\alpha s_{\pi(p)}$，其中 $\alpha$ 控制身份分离强度。这样得到一个无参数、置换对称的 4D rotary operator，包含 time、agent、height、width 四个 band。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> The simplex pool provides a mechanism for agent-count scaling. During training, active agents are randomly assigned to distinct vertices, discouraging slot-specific overfitting. At inference, additional agents can be activated by selecting unused vertices from the same pool without changing the transformer architecture.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> simplex pool 提供了智能体数量扩展机制。训练时，活跃智能体会被随机分配到不同顶点，从而减少对特定 slot 的过拟合。推理时，可以从同一个 pool 中选择额外未用顶点来激活更多智能体，而无需改变 Transformer 架构。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> Sparse Hub Attention replaces dense cross-agent attention. With $L=HW$ tokens per frame and $P$ agents, dense attention over a block of $n$ frames costs $\mathcal{O}(P^2 n^2 L^2)$. γ-World instead adds $K$ learnable hub tokens per latent frame, so agent tokens attend to their own stream and hubs, while hub tokens attend to all agents and other hubs.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> Sparse Hub Attention 替代了 dense cross-agent attention。令每帧 token 数为 $L=HW$、智能体数为 $P$，在 $n$ 帧 block 上做 dense attention 的成本为 $\mathcal{O}(P^2 n^2 L^2)$。γ-World 改为每个 latent frame 加入 $K$ 个可学习 hub tokens：agent tokens 只关注自身流和 hubs，而 hub tokens 关注所有智能体和其他 hub。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> The hub-and-spoke topology masks direct attention between distinct agent streams, so cross-agent information flows through a two-hop path: agent → hub → agent. Composed with the block-causal mask, this preserves temporal causality while maintaining a shared interaction pathway.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 这种 hub-and-spoke 拓扑会屏蔽不同 agent streams 之间的直接注意力，因此跨智能体信息通过两跳路径流动：agent → hub → agent。它再与 block-causal mask 组合，在保留时间因果性的同时维持共享交互通道。

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> For fixed block size $n$, spatial length $L$, and hub count $K$, the Sparse Hub Attention cost is linear in the number of agents $P$. Hub tokens reuse the temporal RoPE phase of their frame while staying neutral with respect to agent identity and spatial position.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> 在固定 block size $n$、空间长度 $L$ 和 hub 数 $K$ 下，Sparse Hub Attention 的成本对智能体数 $P$ 近似线性增长。hub tokens 复用其对应帧的 temporal RoPE 相位，但在 agent identity 和 spatial position 上保持中性。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> The training target is a conditional few-step causal generator for real-time multi-agent rollout. A bidirectional diffusion model offers high quality and cross-agent consistency but cannot be used online because it attends to future frames; a causal model supports KV-cached streaming but suffers from train-test mismatch under autoregressive rollout.

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> 训练目标是一个用于实时多智能体 rollout 的条件化 few-step causal generator。bidirectional diffusion model 有高视觉质量和跨智能体一致性，但因为会关注未来帧，不能直接用于在线生成；causal model 支持 KV-cached streaming，但在自回归 rollout 中会有训练-测试不匹配。

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> The authors therefore use a three-stage recipe: train a high-quality bidirectional teacher, train a block-causal multi-step student with Sparse Hub Attention and Diffusion Forcing, and finally distill the causal student into a conditional few-step generator for low-latency streaming inference.

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> 因此作者采用三阶段方案：先训练高质量 bidirectional teacher；再训练结合 Sparse Hub Attention 与 Diffusion Forcing 的 block-causal multi-step student；最后把 causal student 蒸馏为条件化 few-step generator，用于低延迟流式推理。

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> The bidirectional teacher processes the full multi-agent sequence with dense bidirectional attention and a shared noise level. It is conditioned on first-frame observations and per-agent actions, and provides the high-quality conditional multi-agent distribution used during distillation.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> bidirectional teacher 用 dense bidirectional attention 和共享噪声水平处理完整多智能体序列。它以首帧观测和每个智能体的动作序列为条件，提供蒸馏阶段所需的高质量条件多智能体分布。

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> The causal student combines block-causal attention with the Sparse Hub Attention mask. Each temporal block receives an independently sampled noise level, each query attends only to current or previous blocks, and agents communicate through hubs rather than dense pairwise attention.

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> causal student 将 block-causal attention 与 Sparse Hub Attention mask 结合。每个时间块有独立采样的噪声水平，每个 query 只能关注当前或更早块，智能体之间通过 hubs 而不是 dense pairwise attention 通信。

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> Conditional Self-Forcing distillation initializes the few-step student from the trained multi-step causal model, uses the bidirectional teacher as a high-quality conditional distribution-matching target, and trains under autoregressive self-rollout: generated blocks are written into the KV cache and reused as history for later blocks.

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> Conditional Self-Forcing distillation 将 few-step student 初始化为已训练的 multi-step causal model，并用 bidirectional teacher 作为高质量条件分布匹配目标。训练时采用 autoregressive self-rollout：生成出来的 blocks 写入 KV cache，并作为后续 blocks 的历史。

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> Interactive world models must preserve the initial observation and respond to actions. The same conditioning package, including first-frame observations and per-agent actions, is therefore provided to both teacher and student during distillation to prevent drift from the specified initial state or action controls.

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> 交互式世界模型必须保持初始观测并响应动作。因此在蒸馏时，teacher 和 student 都接收同一套条件输入，包括首帧观测和每个智能体动作，以防 few-step model 偏离指定初始状态或动作控制。

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> At inference time, the distilled few-step student generates one temporal block at a time and streams rollout at 24 FPS. Separate KV caches are maintained for each agent stream and a shared cache for hub tokens, so cross-agent information still flows only through the hub under cached histories.

> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> 推理时，蒸馏后的 few-step student 一次生成一个时间块，并以 24 FPS 流式输出 rollout。系统为每个 agent stream 维护独立 KV cache，并为 hub tokens 维护共享 KV cache；因此即便使用缓存历史，跨智能体信息仍只通过 hub 流动。

## 4. Experiments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For virtual-game environments, the authors construct synchronized multi-agent Minecraft trajectories using controllable episode scripts, coordinated bots, and aligned visual-action recording. The dataset includes two-agent episodes and extends the same collection pipeline to four-agent scenes. Evaluation uses FVD, FID, LPIPS, PSNR, and SSIM, and scalability is measured by DiT latency, self-attention latency, and self-attention FLOPs.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在虚拟游戏环境中，作者用可控 episode scripts、协同 bots 和对齐的视频-动作记录构建同步多智能体 Minecraft trajectories。数据集以两智能体 episode 为主，并将同一采集流程扩展到四智能体场景。评估指标包括 FVD、FID、LPIPS、PSNR 和 SSIM；扩展性则用 DiT latency、self-attention latency 和 self-attention FLOPs 衡量。

### Table 1. 与 Solaris 在多智能体评测协议上的比较

![Table 1](3d%20agent/Gamma-World%20Generative%20Multi-Agent%20World%20Modeling%20Beyond%20Two%20Players/assets/table1.png)

**Caption:** Table 1: Comparison with Solaris across multi-agent evaluation protocols. FID and FVD are lower better (↓). Best per column in bold.

**Caption[CN]:** 表 1：与 Solaris 在多智能体评测协议上的比较。FID 和 FVD 越低越好；每列最优值加粗。

**Reading note:** γ-World 在 Memory、Grounding、Movement、Building、Consistency 五类任务中 FVD/FID 均明显低于 Frame concat 和 Solaris；这是论文最直接的主结果表。

Structured table:

| Method | Memory FVD↓ | Memory FID↓ | Grounding FVD↓ | Grounding FID↓ | Movement FVD↓ | Movement FID↓ | Building FVD↓ | Building FID↓ | Consistency FVD↓ | Consistency FID↓ |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Frame concat | 450.6 | 69.8 | 528.3 | 63.2 | 556.9 | 65.0 | 551.8 | 87.3 | 576.0 | 123.2 |
| Solaris | 333.8 | 51.7 | 301.9 | 36.1 | 311.1 | 36.3 | 448.6 | 71.0 | 443.1 | 94.8 |
| γ-World | **184.1** | **24.8** | **199.3** | **24.0** | **191.5** | **21.2** | **264.5** | **32.1** | **280.0** | **46.9** |

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Compared with frame concatenation, γ-World avoids compressing multiple agents into one undifferentiated visual stream, improving interaction modeling and viewpoint preservation. Compared with Solaris, the order-free identity encoding and hub-based information exchange yield more reliable memory, grounding, building, and cross-view consistency.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 与 frame concatenation 相比，γ-World 不把多个智能体压进一个无差别视觉流中，因此更能保留每个智能体视角并建模交互。与 Solaris 相比，order-free identity encoding 和 hub-based information exchange 在 memory、grounding、building 以及跨视角一致性任务上带来更可靠结果。

### Table 2. 架构设计消融：输入组织、agent encoding 与交互机制

![Table 2](3d%20agent/Gamma-World%20Generative%20Multi-Agent%20World%20Modeling%20Beyond%20Two%20Players/assets/table2.png)

**Caption:** Table 2: Architecture design. All metrics are averaged over the test scenarios in the game environment.

**Caption[CN]:** 表 2：架构设计消融。所有指标都在游戏环境测试场景上取平均。

**Reading note:** 这个表拆开了三个设计选择：空间拼接 vs 序列拼接、learned view embedding vs simplex encoding、dense interaction vs Sparse Hub。完整 γ-World 在 FVD/PSNR/SSIM 上最好，FID/LPIPS 也非常接近最优。

Structured table:

| Setting | Composition | Agent Encoding | Interaction | FVD↓ | FID↓ | LPIPS↓ | PSNR↑ | SSIM↑ |
|---|---|---|---|---:|---:|---:|---:|---:|
| Spatial Concat | Spatial concat | None | Full | 312.4 | 38.7 | 0.326 | 24.8 | 0.782 |
| Sequence Concat | Sequence concat | None | Full | 285.6 | 35.2 | 0.298 | 25.6 | 0.798 |
| View Embedding | Sequence concat | View emb. | Full | 256.3 | 32.4 | 0.281 | 26.4 | 0.815 |
| Simplex Encoding | Sequence concat | Simplex | Full | 228.5 | **29.6** | **0.265** | 27.5 | 0.830 |
| γ-World (Full) | Sequence concat | Simplex | Sparse Hub | **223.4** | 30.2 | 0.269 | **27.7** | **0.836** |

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The architecture ablations show that sequence concatenation is more scalable than spatial concatenation because it keeps per-agent spatial resolution fixed. Simplex Rotary Agent Encoding improves over learned view embeddings by avoiding a privileged slot order, and Sparse Hub Attention provides an efficient shared interaction pathway without sacrificing the main quality metrics.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 架构消融表明，sequence concatenation 比 spatial concatenation 更可扩展，因为它保持每个智能体的空间分辨率不变。Simplex Rotary Agent Encoding 相比 learned view embeddings 更好，因为它避免了特权 slot 顺序；Sparse Hub Attention 则在不显著牺牲主要质量指标的前提下提供了高效共享交互路径。

### Fig. 3. dense cross-agent attention 与 Sparse Hub Attention 的效率对比

![Fig. 3](3d%20agent/Gamma-World%20Generative%20Multi-Agent%20World%20Modeling%20Beyond%20Two%20Players/assets/fig3.png)

**Caption:** Figure 3: Efficiency comparison between dense cross-agent attention and Sparse Hub Attention across 2, 4, and 8 agents. Sparse Hub Attention achieves significantly lower latency and FLOPs as the number of agents increases.

**Caption[CN]:** 图 3：在 2、4、8 个智能体下比较 dense cross-agent attention 与 Sparse Hub Attention 的效率。随着智能体数量增加，Sparse Hub Attention 显著降低延迟和 FLOPs。

**Reading note:** 红线代表 dense attention，蓝线代表 sparse hub；关键观察是 agent 数越多，dense 的 self-attention latency/FLOPs 上升越快。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The efficiency study directly tests the scaling motivation: dense all-to-all interaction grows quadratically with the number of agents, whereas Sparse Hub Attention routes interaction through a compact shared state. DiT latency, self-attention latency, and analytical FLOPs all show substantially better scaling for the hub design.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 效率实验直接检验论文的扩展性动机：dense all-to-all interaction 会随智能体数量二次增长，而 Sparse Hub Attention 将交互路由到一个紧凑共享状态。DiT latency、self-attention latency 和解析 FLOPs 都显示 hub 设计具有更好的扩展性。

### Fig. 4. 两智能体交互的定性示例

![Fig. 4](3d%20agent/Gamma-World%20Generative%20Multi-Agent%20World%20Modeling%20Beyond%20Two%20Players/assets/fig4.png)

**Caption:** Figure 4: Qualitative examples of two-agent interaction. Each row shows a different task.

**Caption[CN]:** 图 4：两智能体交互的定性示例。每一行对应一个不同任务。

**Reading note:** 重点看两个 agent 的视角是否同步，以及一个 agent 的动作是否在另一个 agent 的观测里产生对应变化。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> In two-agent rollouts, paired streams remain synchronized: actions by one agent are reflected in the other agent’s observation when they interact in the shared environment. The model also maintains object and agent grounding when agents temporarily leave each other’s field of view, suggesting a shared latent world state.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 在两智能体 rollout 中，成对视频流保持同步：当智能体在共享环境中交互时，一个智能体的动作会反映到另一个智能体的观测里。即使智能体暂时离开彼此视野，模型也能维持物体和智能体 grounding，这说明它更像是在跟踪共享 latent world state，而不是生成彼此独立的视频。

### Fig. 5. 从两玩家训练零样本扩展到四玩家 rollout

![Fig. 5](3d%20agent/Gamma-World%20Generative%20Multi-Agent%20World%20Modeling%20Beyond%20Two%20Players/assets/fig5.png)

**Caption:** Figure 5: Qualitative example of scaling beyond two players. The first frame in each row shows the initial state for one agent, followed by synchronized rollouts across four agents.

**Caption[CN]:** 图 5：扩展到两玩家以上的定性示例。每一行的第一帧是一个智能体的初始状态，后面是四个智能体的同步 rollout。

**Reading note:** 这是 simplex encoding 的核心卖点：训练主要在两 agent 上，但通过未用 simplex 顶点可以激活四 agent 推理。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Zero-shot four-agent rollouts are generated from a model trained only on two-agent data. The same checkpoint produces synchronized visual streams for multiple players without architecture changes, enabled by Simplex Rotary Agent Encoding and Sparse Hub Attention.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 作者展示了从只在两智能体数据上训练的模型生成零样本四智能体 rollout。同一个 checkpoint 在不改架构的情况下为多个玩家生成同步视觉流，这依赖 Simplex Rotary Agent Encoding 的未固定 slot 身份，以及 Sparse Hub Attention 的共享通信路径。

### Fig. 6. 真实世界机器人协作定性示例

![Fig. 6](3d%20agent/Gamma-World%20Generative%20Multi-Agent%20World%20Modeling%20Beyond%20Two%20Players/assets/fig6.png)

**Caption:** Figure 6: Qualitative examples of real-world robotic coordination.

**Caption[CN]:** 图 6：真实世界机器人协作的定性示例。

**Reading note:** 这里左、右机械臂被视作两个交互智能体，用来说明方法不只限于 Minecraft 游戏视角。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> For real-world robotics, the authors use the RealOmin-Open Dataset and treat the left and right robot arms as two interacting agents. γ-World generates future frames that preserve coordinated multi-robot motion and scene layout, suggesting that the same multi-agent formulation can transfer from virtual games to physical scenes.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 在真实机器人实验中，作者使用 RealOmin-Open Dataset，并把左、右机械臂视为两个交互智能体。γ-World 生成的未来帧能保持多机器人协同运动和场景空间布局，说明同一套多智能体生成公式有潜力从虚拟游戏迁移到真实物理场景。

## 5. Discussion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> γ-World combines Simplex Rotary Agent Encoding for distinct yet permutation-symmetric identities with Sparse Hub Attention for efficient hub-mediated cross-agent communication. Together with conditional teacher-student distillation and KV-cached streaming inference, these components enable real-time action-responsive rollouts that remain consistent across time and agent perspectives.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> γ-World 将“身份不同但置换对称”的 Simplex Rotary Agent Encoding，与“高效 hub-mediated 跨智能体通信”的 Sparse Hub Attention 结合起来。再配合 conditional teacher-student distillation 和 KV-cached streaming inference，这些组件让模型可以实时响应动作，并在时间和智能体视角之间保持一致。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Limitations remain. Evaluation focuses primarily on gaming environments and robotics examples; broader validation in more complex, heterogeneous, and long-horizon settings is future work. Very large populations may require larger rotary agent bands or hierarchical grouping, and long rollouts may accumulate inconsistencies because 3D geometry and physical constraints are not explicitly enforced.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 局限性也很明确：当前评估主要集中在游戏环境和机器人示例，更复杂、异质、长时程的场景还需要进一步验证。非常大的智能体群体可能需要更大的 rotary agent band 或层级化 agent grouping；此外，由于模型没有显式约束 3D 几何或物理规律，长 rollout 仍可能逐渐积累不一致。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Acknowledgements. The authors thank Product Managers Aditya Mahajan and Matt Cragun for support and guidance, Jingnan Gao for proof discussion, and Yixin Hong for demo creation.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 致谢部分：作者感谢产品经理 Aditya Mahajan 和 Matt Cragun 的支持与指导，感谢 Jingnan Gao 关于证明的讨论，以及 Yixin Hong 对 demo 制作的帮助。

## Appendix A. More Visualizations

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The appendix notes that extended 24-second multi-agent rollouts, qualitative baseline comparisons, and real-world robotic coordination videos are included in the supplementary video, offering a more intuitive demonstration of the method.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 附录 A 说明，补充视频中包含扩展的 24 秒多智能体 rollout、与 baseline 的定性比较，以及真实机器人协作视频，用更直观的方式展示方法效果。

## Appendix B. Proof of Simplex Equidistance

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The proof constructs simplex vertices in $\mathbb{R}^V$ and embeds them into the $(d_p/2)$-dimensional agent angle space, where $d_p$ is the agent rotary band size and $V\le d_p/2+1$. The centered vector is $\bar{s}_p=e_p-\frac{1}{V}\mathbf{1}$, which lies in the zero-mean subspace.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 证明先在 $\mathbb{R}^V$ 中构造 simplex vertices，再把它们嵌入到 $(d_p/2)$ 维 agent angle space 中，其中 $d_p$ 是 agent rotary band size，且 $V\le d_p/2+1$。centered vector 定义为 $\bar{s}_p=e_p-\frac{1}{V}\mathbf{1}$，它位于 zero-mean subspace。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The centered vectors have squared norm $(V-1)/V$ and pairwise inner product $-1/V$ for different agents. After normalization by $\sqrt{V/(V-1)}$, the vertices $s_p$ have unit norm and inner product $-1/(V-1)$ for $p\ne q$.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> centered vectors 的平方范数为 $(V-1)/V$，不同智能体之间的内积为 $-1/V$。经过 $\sqrt{V/(V-1)}$ 归一化后，顶点 $s_p$ 具有单位范数，并且当 $p\ne q$ 时内积为 $-1/(V-1)$。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Therefore every pair of distinct simplex vertices has the same squared distance: $\lVert s_p-s_q\rVert_2^2 = 2V/(V-1)$. With agent angle $\theta_p=\alpha s_p$, all different-agent pairs receive the same separation in the underlying angle space.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 因此任意两个不同 simplex vertices 的平方距离相同：$\lVert s_p-s_q\rVert_2^2 = 2V/(V-1)$。由于 agent angle 定义为 $\theta_p=\alpha s_p$，所有不同智能体对在底层 angle space 中获得相同的分离量。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The proof further analyzes the induced complex RoPE representation $\Phi_p=\exp(i\theta_p)$. For sufficiently small $\alpha$, the approximation $1-\cos x\approx x^2/2$ shows that complex-space distances are approximately equal; in the common zero-padded centered-one-hot implementation, the complex-space distance is also identical across distinct agent pairs because pairwise difference vectors share the same non-zero coordinate pattern up to permutation.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 证明还分析了诱导出的 complex RoPE representation $\Phi_p=\exp(i\theta_p)$。当 $\alpha$ 足够小时，用近似 $1-\cos x\approx x^2/2$ 可知 complex-space distances 近似相等；在常见的 zero-padded centered-one-hot 实现中，不同智能体对的 complex-space distance 也相同，因为任意两两差分向量在置换意义下拥有相同的非零坐标模式。

## Appendix C. More Architecture

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The action design uses explicit per-agent action traces as conditioning signals. Actions are synchronized with video frames and provided separately for different agents. The game domain uses player control commands, while the robot domain uses continuous end-effector state.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 动作设计使用显式的 per-agent action traces 作为条件信号。动作与视频帧同步，并按不同智能体分别提供。游戏域使用玩家控制命令，机器人域使用连续的末端执行器状态。

### Table 3. 游戏动作格式：每帧 25 维 action vector

![Table 3](3d%20agent/Gamma-World%20Generative%20Multi-Agent%20World%20Modeling%20Beyond%20Two%20Players/assets/table3.png)

**Caption:** Table 3: Game action format. Each frame stores a 25-field action vector for each agent.

**Caption[CN]:** 表 3：游戏动作格式。每帧为每个智能体存储一个 25 字段动作向量。

**Reading note:** 23 个离散玩家控制 + 2 个连续相机控制，是 Minecraft-style 控制输入。

Structured table:

| Index | Field | Description |
|---|---|---|
| 0 | inventory | Open inventory |
| 1 | ESC | Exit or cancel current menu |
| 2-10 | hotbar.1-hotbar.9 | Select hotbar slot 1-9 |
| 11-14 | forward, back, left, right | Locomotion controls |
| 15-17 | jump, sneak, sprint | Movement modifiers |
| 18 | swapHands | Swap held item between hands |
| 19-22 | attack, use, pickItem, drop | Interaction and item manipulation |
| 23-24 | cameraX, cameraY | Horizontal yaw and vertical pitch motion |

### Table 4. 机器人动作格式：每帧 10 维连续 action vector

![Table 4](3d%20agent/Gamma-World%20Generative%20Multi-Agent%20World%20Modeling%20Beyond%20Two%20Players/assets/table4.png)

**Caption:** Table 4: Robot action format. Each frame stores a 10-field continuous action vector for each robot.

**Caption[CN]:** 表 4：机器人动作格式。每帧为每个机器人存储一个 10 字段连续动作向量。

**Reading note:** 机器人动作由末端位置、6D 姿态和 gripper 开合值组成，左右机械臂各有一条时间对齐的动作序列。

Structured table:

| Index | Field | Description |
|---|---|---|
| 0-2 | pos_x, pos_y, pos_z | End-effector position |
| 3-8 | rot_6d_0-rot_6d_5 | End-effector orientation |
| 9 | gripper | Gripper opening value |

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For Minecraft-style game videos, each frame action contains 25 fields: inventory interaction, hotbar selection, movement, item manipulation, mouse-button actions, and continuous horizontal and vertical camera motion. For robot videos, each action contains 3D end-effector position, 6D orientation, and gripper value, with aligned action sequences for left and right robots.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 对于 Minecraft-style 游戏视频，每帧动作包含 25 个字段：库存交互、快捷栏选择、移动、物品操作、鼠标按键，以及连续的水平/垂直相机运动。对于机器人视频，每个动作包含 3D 末端位置、6D 姿态和 gripper 值，左右机器人各有时间对齐的动作序列。

## Appendix D. Additional Implementation Details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Both the bidirectional teacher and causal student are based on Cosmos-Predict2.5-2B, with hidden dimension $D=2048$, 28 transformer blocks, 16 attention heads, MLP ratio 4, and AdaLN-LoRA rank 256. Simplex Rotary Agent Encoding partitions the head dimension as $(64,32,16,16)$ across time, agent, height, and width axes.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> bidirectional teacher 和 causal student 都基于 Cosmos-Predict2.5-2B，隐藏维度 $D=2048$，28 个 transformer blocks，16 个 attention heads，MLP ratio 为 4，AdaLN-LoRA rank 为 256。Simplex Rotary Agent Encoding 将 head dimension 按 $(64,32,16,16)$ 分配到 time、agent、height、width 四个轴。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The implementation uses a simplex pool of size 4 over 2 active runtime slots. At every training step, the model randomly samples 2 of the 4 vertices and permutes agent slot order, forcing player disambiguation through the simplex marker and allowing the same checkpoint to serve up to 4 players at inference.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 实现中使用大小为 4 的 simplex pool，但训练时只有 2 个活跃 runtime slots。每个训练 step 随机抽取 4 个顶点中的 2 个，并额外置换 agent slot 顺序，迫使模型只能通过 simplex marker 区分玩家，从而让同一个 checkpoint 在推理时支持最多 4 个玩家。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The shared action encoder has two MLP branches for a 23-dimensional keyboard one-hot and a 2-dimensional camera vector, lifts each to 128 dimensions, fuses them through an MLP and a 4-stride 1D temporal convolution, and projects to $D=2048$. Sparse Hub Attention uses $K=8$ learnable global hub tokens per latent frame, and local windowed attention keeps the most recent 24 latent frames per view in the KV cache.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 共享 action encoder 包含两个 MLP 分支，分别处理 23 维键盘 one-hot 和 2 维相机向量，并将每个模态升到 128 维；随后通过 fusion MLP、stride 为 4 的 1D temporal convolution，以及最终投影到 $D=2048$。Sparse Hub Attention 每个 latent frame 使用 $K=8$ 个可学习 global hub tokens；local windowed attention 只在 KV cache 中保留每个视角最近 24 个 latent frames。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Stages 1 and 2 initialize both models from Cosmos-Predict2.5-2B TI2V and train on 2-agent gameplay at $320\times480$ per view. The teacher is trained on 93-frame clips for 10,000 iterations and fine-tuned on 189-frame clips for 6,000 iterations; the causal student is pretrained on 93-frame clips for 15,000 iterations. Both use AdamW, learning rate $3\times10^{-5}$, weight decay $10^{-3}$, and 32 NVIDIA GB200s.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 第 1、2 阶段都从 Cosmos-Predict2.5-2B TI2V 初始化，并在每视角 $320\times480$ 的两智能体游戏数据上训练。teacher 先用 93-frame clips 训练 10,000 iterations，再用 189-frame clips fine-tune 6,000 iterations；causal student 用 93-frame clips 预训练 15,000 iterations。两者都使用 AdamW，学习率 $3\times10^{-5}$，weight decay $10^{-3}$，训练资源为 32 张 NVIDIA GB200。

### Table 5. causal、bidirectional 与 distilled 训练阶段对比

![Table 5](3d%20agent/Gamma-World%20Generative%20Multi-Agent%20World%20Modeling%20Beyond%20Two%20Players/assets/table5.png)

**Caption:** Table 5: Comparison of causal, bidirectional, and distilled variants of our model.

**Caption[CN]:** 表 5：模型 causal、bidirectional 和 distilled 变体的比较。

**Reading note:** Bidirectional 质量最好但不适合在线推理；Causal 可流式但质量下降；Distilled 在保留 causal 结构的同时恢复了相当多 teacher 质量。

Structured table:

| Variant | FVD↓ | FID↓ | LPIPS↓ | PSNR↑ | SSIM↑ |
|---|---:|---:|---:|---:|---:|
| Bidirectional | 227.3 | 31.0 | 0.272 | 27.7 | 0.828 |
| Causal | 266.4 | 34.4 | 0.277 | 26.2 | 0.805 |
| Distilled | 239.7 | 30.9 | 0.273 | 26.8 | 0.811 |

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Stage 3 Self-Forcing distillation couples three networks: the trainable student, a frozen real score from the Stage-1 teacher, and a trainable fake score initialized from the Stage-1 teacher. The student is optimized with DMD on 189-frame clips using four denoising timesteps per block and writes denoised blocks into the KV cache before proceeding.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 第 3 阶段 Self-Forcing distillation 包含三个网络：可训练 student、来自 Stage-1 teacher 的冻结 real score，以及同样从 Stage-1 teacher 初始化但可训练的 fake score。student 在 189-frame clips 上用 DMD 优化，每个 block 使用四个 denoising timesteps，并在进入下一块前把去噪后的 block 写入 KV cache。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The generator and critic are updated alternately at a 1:4 ratio. Distillation runs for 400 iterations on 32 NVIDIA GB200s. At inference, the student uses the same 4-step denoising schedule and rolling local-attention window of 24 latent frames per view, decoupling sequence length from cache memory.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> generator 和 critic 以 1:4 比例交替更新；蒸馏在 32 张 NVIDIA GB200 上运行 400 iterations。推理时，student 使用同样的 4-step denoising schedule，并采用每个视角 24 latent frames 的 rolling local-attention window，从而让生成序列长度与 cache memory 解耦。

## Appendix E-F. Additional Ablations and More Experimental Results

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The appendix compares causal, bidirectional, and distilled variants and reports FVD, FID, LPIPS, PSNR, and SSIM. The bidirectional teacher has access to full temporal context and therefore achieves the best overall performance; the causal model enables streaming but degrades because it can only attend to past frames; the distilled model recovers much of the teacher’s quality while retaining the causal structure.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 附录进一步比较 causal、bidirectional 和 distilled 三个变体，并报告 FVD、FID、LPIPS、PSNR 和 SSIM。bidirectional teacher 可以访问完整时序上下文，因此总体性能最好；causal model 可流式推理，但因为只能看过去帧而性能下降；distilled model 在保留 causal 结构的同时恢复了相当多 teacher 质量。

### Table 6. Sparse Hub Attention 中 hub token 数量消融

![Table 6](3d%20agent/Gamma-World%20Generative%20Multi-Agent%20World%20Modeling%20Beyond%20Two%20Players/assets/table6.png)

**Caption:** Table 6: Ablation on the number of hub tokens in Sparse Hub Attention. We vary the hub token count K and report generation quality, perceptual quality, and pixel-level quality.

**Caption[CN]:** 表 6：Sparse Hub Attention 中 hub token 数量的消融。作者改变 hub token 数 $K$，并报告生成质量、感知质量和像素级质量。

**Reading note:** 从 K=1 到 K=128，指标逐步改善，但 K=8 已经取得较好折中；主模型选择 K=8 更偏向效率/质量平衡。

Structured table:

| Hub Tokens (K) | FVD↓ | FID↓ | LPIPS↓ | PSNR↑ | SSIM↑ |
|---:|---:|---:|---:|---:|---:|
| 1 | 250.9 | 31.5 | 0.271 | 27.3 | 0.825 |
| 8 | 223.4 | 30.2 | 0.269 | 27.7 | 0.836 |
| 32 | 221.8 | 29.8 | 0.267 | 27.9 | 0.838 |
| 128 | 220.5 | 29.5 | 0.266 | 28.0 | 0.839 |

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Hub tokens serve as the compact shared state through which agents exchange information, so $K$ controls the capacity of the cross-agent communication bottleneck. Too small a $K$ limits the hub’s ability to summarize multi-agent state, while larger $K$ allows richer communication at extra cost.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> hub tokens 是智能体交换信息的紧凑共享状态，因此 $K$ 控制跨智能体通信瓶颈容量。如果 $K$ 太小，hub 总结多智能体状态的能力受限；增大 $K$ 可以提供更丰富通信，但会带来额外计算成本。

## References (原文保留)

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> [1] N. Agarwal, A. Ali, M. Bala, Y. Balaji, E. Barker, T. Cai, P. Chattopadhyay, Y. Chen, Y. Cui, Y. Ding, et al. Cosmos world foundation model platform for physical ai. arXiv preprint arXiv:2501.03575, 2025. 3 [2] A. Ali, J. Bai, M. Bala, Y. Balaji, A. Blakeman, T. Cai, J. Cao, T. Cao, E. Cha, Y.-W. Chao, et al. World simulation with video foundation models for physical ai. arXiv preprint arXiv:2511.00062, 2025. 2, 15 [3] E. Alonso, A. Jelley, V. Micheli, A. Kanervisto, A. Storkey, T. Pearce, and F. Fleuret. Diffusion for world modeling: Visual details matter in atari. NeurIPS, 37:58757–58791, 2024. 2, 3 [4] A. Bar, G. Zhou, D. Tran, T. Darrell, and Y. LeCun. Navigation world models. In CVPR, pages 15791–15801, 2025. 3 [5] J. Bruce, M. D. Dennis, A. Edwards, J. Parker-Holder, Y. Shi, E. Hughes, M. Lai, A. Mavalankar, R. Steigerwald, C. Apps, et al. Genie: Generative interactive environments. In Forty-first International Conference on Machine Learning, 2024. 2 [6] B. Chen, D. Martí Monsó, Y. Du, M. Simchowitz, R. Tedrake, and V. Sitzmann. Diffusion forcing: Next-token prediction meets full-sequence diffusion. Advances in Neural Information Processing Systems, 37:24081–24125, 2024. 3, 5, 7 [7] H. Chen, Y. Zhang, X. Cun, M. Xia, X. Wang, C. Weng, and Y. Shan. Videocrafter2: Overcoming data limitations for high-quality video diffusion models. In CVPR, pages 7310–7320, 2024. 3 [8] G. Deepmind. Veo3 video model, 2025. https://deepmind.google/models/veo/. 3 [9] Enigma-team. Introducing Multiverse: The first AI multiplayer world model. Enigma Blog, 2025. 8, 9 [10] L. Fan, G. Wang, Y. Jiang, A. Mandlekar, Y. Yang, H. Zhu, A. Tang, D.-A. Huang, Y. Zhu, and A. Anandkumar. Minedojo: Building open-ended embodied agents with internet-scale knowledge. Advances in Neural Information Processing Systems, 35:18343–18362, 2022. 3 [11] Z. Feng, R. Xue, L. Yuan, Y. Yu, N. Ding, M. Liu, B. Gao, J. Sun, X. Zheng, and G. Wang. Multi-agent embodied ai: Advances and future directions. Science China Information Sciences, 69(5):151202, 2026. 2 [12] K. Frans, D. Hafner, S. Levine, and P. Abbeel. One step diffusion via shortcut models. arXiv preprint arXiv:2410.12557, 2024. 3 [13] P. Fung, Y. Bachrach, A. Celikyilmaz, K. Chaudhuri, D. Chen, W. Chung, E. Dupoux, H. Gong, H. Jégou, A. Lazaric, et al. Embodied ai agents: Modeling the world. arXiv preprint arXiv:2506.22355, 2025. 2 [14] S. Gao, W. Liang, K. Zheng, A. Malik, S. Ye, S. Yu, W.-C. Tseng, Y. Dong, K. Mo, C.-H. Lin, et al. Dreamdojo: A generalist robot world model from large-scale human videos. arXiv preprint arXiv:2602.06949, 2026. 3 [15] Y. Gao, H. Guo, T. Hoang, W. Huang, L. Jiang, F. Kong, H. Li, J. Li, L. Li, X. Li, et al. Seedance 1.0: Exploring the boundaries of video generation models. arXiv preprint arXiv:2506.09113, 2025. 3 [16] Gen Robot. 10kh-realomin-opendata, 2025. 10

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 参考文献 [1]-[16] 为书目信息，按原文保留；中文阅读时主要用于定位本文引用的相关工作谱系，不对作者名、题名和 venue 做逐条意译。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> [17] Z. Geng, M. Deng, X. Bai, J. Z. Kolter, and K. He. Mean flows for one-step generative modeling. arXiv preprint arXiv:2505.13447, 2025. 3 [18] Y. Guo, C. Yang, A. Rao, Z. Liang, Y. Wang, Y. Qiao, M. Agrawala, D. Lin, and B. Dai. Animatediff: Animate your personalized text-to-image diffusion models without specific tuning. In ICLR, 2024. 3 [19] X. He, C. Peng, Z. Liu, B. Wang, Y. Zhang, Q. Cui, F. Kang, B. Jiang, M. An, Y. Ren, et al. Matrix-game 2.0: An open-source real-time and streaming interactive world model. arXiv preprint arXiv:2508.13009, 2025. 2, 3 [20] R. Henschel, L. Khachatryan, H. Poghosyan, D. Hayrapetyan, V. Tadevosyan, Z. Wang, S. Navasardyan, and H. Shi. Streamingt2v: Consistent, dynamic, and extendable long video generation from text. In CVPR, pages 2568–2577, 2025. 3 [21] J. Ho, A. Jain, and P. Abbeel. Denoising diffusion probabilistic models. Advances in neural information processing systems, 33:6840–6851, 2020. 3 [22] A. Hu, L. Russell, H. Yeo, Z. Murez, G. Fedoseev, A. Kendall, J. Shotton, and G. Corrado. Gaia-1: A generative world model for autonomous driving. arXiv preprint arXiv:2309.17080, 2023. 3 [23] X. Huang, Z. Li, G. He, M. Zhou, and E. Shechtman. Self forcing: Bridging the train-test gap in autoregressive video diffusion. arXiv preprint arXiv:2506.08009, 2025. 3, 5, 7, 16 [24] T. HunyuanWorld. Hy-world 1.5: A systematic framework for interactive world modeling with real-time latency and geometric consistency. arXiv preprint, 2025. 2, 3 [25] M. Kang, R. Zhang, C. Barnes, S. Paris, S. Kwak, J. Park, E. Shechtman, J.-Y. Zhu, and T. Park. Distilling diffusion models into conditional gans. In ECCV, pages 428–447, 2024. 3 [26] J. Kim, J. Kang, J. Choi, and B. Han. Fifo-diffusion: Generating infinite videos from text without training. Advances in Neural Information Processing Systems, 37:89834–89868, 2024. 3 [27] W. Kong, Q. Tian, Z. Zhang, R. Min, Z. Dai, J. Zhou, J. Xiong, X. Li, B. Wu, J. Zhang, et al. Hunyuanvideo: A systematic framework for large video generative models. arXiv preprint arXiv:2412.03603, 2024. 3 [28] Kuaishou. Kling video model, 2024. https://klingai.com/global/. 3 [29] C. Li, O. Michel, X. Pan, S. Liu, M. Roberts, and S. Xie. Pisa experiments: Exploring physics post-training for video diffusion models by watching stuff drop. arXiv preprint arXiv:2503.09595, 2025. 3 [30] C. Li, Y. Yang, J. Shao, H. Zhou, K. Schwarz, and Y. Liao. Rerope: Repurposing rope for relative camera control. arXiv preprint arXiv:2602.08068, 2026. 6 [31] L. Li, Q. Zhang, Y. Luo, S. Yang, R. Wang, F. Han, M. Yu, Z. Gao, N. Xue, X. Zhu, et al. Causal world modeling for robot control. arXiv preprint arXiv:2601.21998, 2026. 3 [32] S. Li, Y. Gao, D. Sadigh, and S. Song. Unified video action model. arXiv preprint arXiv:2503.00200, 2025. 3

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 参考文献 [17]-[32] 为书目信息，按原文保留；中文阅读时主要用于定位本文引用的相关工作谱系，不对作者名、题名和 venue 做逐条意译。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> [33] J. Liang, R. Liu, E. Ozguroglu, S. Sudhakar, A. Dave, P. Tokmakov, S. Song, and C. Vondrick. Dreamitate: Real-world visuomotor policy learning via video generation. arXiv preprint arXiv:2406.16862, 2024. 3 [34] S. Lin, A. Wang, and X. Yang. Sdxl-lightning: Progressive adversarial diffusion distillation. arXiv preprint arXiv:2402.13929, 2024. 3 [35] S. Lin, X. Xia, Y. Ren, C. Yang, X. Xiao, and L. Jiang. Diffusion adversarial post-training for one-step video generation. In ICML, 2025. 3 [36] S. Lin, C. Yang, H. He, J. Jiang, Y. Ren, X. Xia, Y. Zhao, X. Xiao, and L. Jiang. Autoregressive adversarial post-training for real-time interactive video generation. arXiv preprint arXiv:2506.09350, 2025. 3 [37] Y. Lipman, R. T. Chen, H. Ben-Hamu, M. Nickel, and M. Le. Flow matching for generative modeling. In ICLR, 2023. 3, [38] Y. Lu, Y. Ren, X. Xia, S. Lin, X. Wang, X. Xiao, A. J. Ma, X. Xie, and J.-H. Lai. Adversarial distribution matching for diffusion distillation towards efficient image and video synthesis. In ICCV, pages 16818–16829, 2025. 3 [39] R. Mereu, A. Scannell, Y. Hou, Y. Zhao, A. Jitta, A. Dominguez, L. Acerbi, A. Storkey, and P. Chang. Generative world modelling for humanoids: 1x world model challenge technical report. arXiv preprint arXiv:2510.07092, 2025. 3 [40] OpenAI. Sora video model, 2024. https://sora.chatgpt.com/. 3 [41] W. Peebles and S. Xie. Scalable diffusion models with transformers. In ICCV, pages 4195–4205, 2023. 3, 4 [42] X. Ren, Y. Lu, T. Cao, R. Gao, S. Huang, A. Sabour, T. Shen, T. Pfaff, J. Z. Wu, R. Chen, et al. Cosmos-drive-dreams: Scalable synthetic driving data generation with world foundation models. arXiv preprint arXiv:2506.09042, 2025. 2 [43] R. Rombach, A. Blattmann, D. Lorenz, P. Esser, and B. Ommer. High-resolution image synthesis with latent diffusion models. In CVPR, 2022. 3 [44] T. Salimans and J. Ho. Progressive distillation for fast sampling of diffusion models. arXiv preprint arXiv:2202.00512, 2022. 3 [45] A. Sauer, F. Boesel, T. Dockhorn, A. Blattmann, P. Esser, and R. Rombach. Fast high-resolution image synthesis with latent adversarial diffusion distillation. In SIGGRAPH Asia, pages 1–11, 2024. 3 [46] A. Sauer, D. Lorenz, A. Blattmann, and R. Rombach. Adversarial diffusion distillation. In ECCV, pages 87–103, 2024. [47] G. Savva, O. Michel, D. Lu, S. Waiwitlikhit, T. Meehan, D. Mishra, S. Poddar, J. Lu, and S. Xie. Solaris: Building a multiplayer video world model in minecraft. arXiv preprint arXiv:2602.22208, 2026. 2, 6, 8, 9 [48] Y. Song, J. Sohl-Dickstein, D. P. Kingma, A. Kumar, S. Ermon, and B. Poole. Score-based generative modeling through stochastic differential equations. In ICLR, 2021. 3

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 参考文献 [33]-[48] 为书目信息，按原文保留；中文阅读时主要用于定位本文引用的相关工作谱系，不对作者名、题名和 venue 做逐条意译。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> [49] J. Su, M. Ahmed, Y. Lu, S. Pan, W. Bo, and Y. Liu. Roformer: Enhanced transformer with rotary position embedding. Neurocomputing, 568:127063, 2024. 5 [50] W. Sun, H. Zhang, H. Wang, J. Wu, Z. Wang, Z. Wang, Y. Wang, J. Zhang, T. Wang, and C. Guo. Worldplay: Towards long-term geometric consistency for real-time interactive world model. arXiv preprint, 2025. 2, 3 [51] D. Valevski, Y. Leviathan, M. Arar, and S. Fruchter. Diffusion models are real-time game engines. arXiv preprint arXiv:2408.14837, 2024. 2, 3 [52] T. Wan, A. Wang, B. Ai, B. Wen, C. Mao, C.-W. Xie, D. Chen, F. Yu, H. Zhao, J. Yang, et al. Wan: Open and advanced large-scale video generative models. arXiv preprint arXiv:2503.20314, 2025. 3, 4 [53] Z. Wang, C. Lu, Y. Wang, F. Bao, C. Li, H. Su, and J. Zhu. Prolificdreamer: High-fidelity and diverse text-to-3d generation with variational score distillation. NeurIPS, 36:8406–8441, 2023. 3 [54] T. Wiedemer, Y. Li, P. Vicol, S. S. Gu, N. Matarese, K. Swersky, B. Kim, P. Jaini, and R. Geirhos. Video models are zero-shot learners and reasoners. arXiv preprint arXiv:2509.20328, 2025. 3 [55] Z. Xiao, Y. Lan, Y. Zhou, W. Ouyang, S. Yang, Y. Zeng, and X. Pan. Worldmem: Long-term consistent world simulation with memory. arXiv preprint arXiv:2504.12369, 2025. 2, 3 [56] M. Yang, Y. Du, K. Ghasemipour, J. Tompson, D. Schuurmans, and P. Abbeel. Learning interactive real-world simulators. arXiv preprint arXiv:2310.06114, 2023. 3 [57] Z. Yang, Y. Chen, J. Wang, S. Manivasagam, W.-C. Ma, A. J. Yang, and R. Urtasun. Unisim: A neural closed-loop sensor simulator. In CVPR, pages 1389–1399, 2023. 3 [58] Z. Yang, J. Teng, W. Zheng, M. Ding, S. Huang, J. Xu, Y. Yang, W. Hong, X. Zhang, G. Feng, et al. Cogvideox: Text-to-video diffusion models with an expert transformer. In ICLR, 2024. 3 [59] S. Ye, Y. Ge, K. Zheng, S. Gao, S. Yu, G. Kurian, S. Indupuru, Y. L. Tan, C. Zhu, J. Xiang, et al. World action models are zero-shot policies. arXiv preprint arXiv:2602.15922, 2026. 3 [60] T. Yin, M. Gharbi, T. Park, R. Zhang, E. Shechtman, F. Durand, and B. Freeman. Improved distribution matching distillation for fast image synthesis. NeurIPS, 37:47455–47487, 2024. 3 [61] T. Yin, M. Gharbi, R. Zhang, E. Shechtman, F. Durand, W. T. Freeman, and T. Park. One-step diffusion with distribution matching distillation. In CVPR, pages 6613–6623, 2024. 3, 8, 16 [62] T. Yin, Q. Zhang, R. Zhang, W. T. Freeman, F. Durand, E. Shechtman, and X. Huang. From slow bidirectional to fast autoregressive video diffusion models. In CVPR, pages 22963–22974, 2025. 3, 7 [63] J. Yu, J. Bai, Y. Qin, Q. Liu, X. Wang, P. Wan, D. Zhang, and X. Liu. Context as memory: Scene-consistent interactive long video generation with memory retrieval. arXiv preprint arXiv:2506.03141, 2025. 2, 3 [64] J. Yuan, X. Zhang, F. Friedrich, N. Beltran-Velez, M. Hall, R. Askari-Hemmat, X. Han, N. Ballas, M. Drozdzal, and A. Romero-Soriano. Inference-time physics alignment of video generative models with latent world models. arXiv preprint arXiv:2601.10553, 2026. 3

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 参考文献 [49]-[64] 为书目信息，按原文保留；中文阅读时主要用于定位本文引用的相关工作谱系，不对作者名、题名和 venue 做逐条意译。

## 阅读提示 / critical reading notes

- 这篇论文的真正核心不是“视频质量又高一点”，而是给多智能体世界模型补上三个结构属性：独立可控、置换对称、可扩展推理。
- Simplex Rotary Agent Encoding 解决的是 identity symmetry；Sparse Hub Attention 解决的是 cross-agent communication cost；Self-Forcing distillation 解决的是实时 causal rollout 的质量与延迟。
- 如果你要复现实验，最关键的隐藏成本在数据：同步多 agent 视觉-动作轨迹、agent slot 随机化、以及 teacher/student/distillation 三阶段训练。
- 方法的边界也清楚：没有显式几何/物理约束，长时 rollout 仍可能 drift；很大规模 agent 群体可能需要层级化通信或更大的 agent rotary band。
