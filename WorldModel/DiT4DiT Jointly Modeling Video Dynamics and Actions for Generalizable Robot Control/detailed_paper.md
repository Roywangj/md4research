---
title: "DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control"
title_zh: "DiT4DiT：联合建模视频动力学与动作，实现可泛化机器人控制"
authors: [Teli Ma, Jia Zheng, Zifan Wang, Chunli Jiang, Andy Cui, Junwei Liang, Shuo Yang]
year: 2026
version: "arXiv:2603.10448v2 (22 Mar 2026)"
source_pdf: "/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/KWEE8R4V/Ma 等 - 2026 - DiT4DiT Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control.pdf"
source_sha256: "64f21b940ff2ee1bccf4e1e7910dc22c207c0cb87ba4e6e16456610c5606b9cd"
page_count: 22
status: complete
---

# Source Identity and Coverage / 来源身份与覆盖范围

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Authoritative source.** This reader is grounded in the 22-page arXiv v2 PDF dated 22 March 2026, identified as arXiv:2603.10448v2 and SHA-256 `64f21b940ff2ee1bccf4e1e7910dc22c207c0cb87ba4e6e16456610c5606b9cd`. The complete PDF text layer, rendered pages, source manifest, and existing verified figure/table assets were cross-checked. The source inventory contains the title/authors, Abstract, Sections 1–6, 10 numbered figures, 5 numbered tables, 2 algorithms, equations (1)–(10), 51 references, and Appendix A.1–A.4.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **权威来源。** 本阅读稿以 2026 年 3 月 22 日发布的 22 页 arXiv v2 PDF 为依据，版本标识为 arXiv:2603.10448v2，SHA-256 为 `64f21b940ff2ee1bccf4e1e7910dc22c207c0cb87ba4e6e16456610c5606b9cd`。制作时交叉核对了完整 PDF 文本层、渲染页面、源清单以及已有并经验证的图表资产。源文 inventory 包含题名与作者、摘要、第 1–6 节、10 幅编号图、5 个编号表、2 个算法、公式（1）–（10）、51 条参考文献，以及附录 A.1–A.4。

## Page and Section Index / 页码与章节索引

| Source pages | Content |
|---|---|
| 1 | Title, authors, affiliations, Abstract, Section 1 begins |
| 1–2 | 1. Introduction; Figure 1 |
| 3 | 2. Related Works; 3. Scaling Proxy begins |
| 4 | 3. Scaling Proxy; Figure 2; Section 4 begins |
| 5–8 | 4.1–4.4 Method; equations (1)–(10); Figures 3; Algorithms 1–2 |
| 8–15 | 5. Experiments; Figures 4–8; Tables 1–3 |
| 15 | 6. Conclusion; References begin |
| 15–18 | References |
| 19–21 | Appendix A.1–A.4; Tables 4–5; Figure 9 |
| 22 | Figure 10 |

## Terminology Ledger / 术语表

| Source term | Consistent Chinese rendering |
|---|---|
| Video-Action Model (VAM) | 视频-动作模型 |
| video Diffusion Transformer / video DiT | 视频扩散 Transformer / 视频 DiT |
| action Diffusion Transformer / action DiT | 动作扩散 Transformer / 动作 DiT |
| flow matching | 流匹配（保留英文标识时写作 flow matching） |
| intermediate denoising features | 中间去噪特征 |
| feature-extraction/interception timestep | 特征提取/截取时间步 |
| proprioceptive state | 本体感知状态 |
| rollout | rollout（轨迹评估轮次） |
| from scratch | 从头训练；按表注特指未使用当前基准外的动作数据 |
| zero-shot generalization | 零样本泛化 |

# DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control

## Title, Authors, and Affiliations / 标题、作者与单位

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Title:** DiT4DiT: Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **标题：** DiT4DiT：联合建模视频动力学与动作，实现可泛化机器人控制

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Authors:** Teli Ma$^{1,2}$; Jia Zheng$^{1,2}$; Zifan Wang$^{1,2}$; Chunli Jiang$^{1}$; Andy Cui$^{1}$; Junwei Liang$^{2,3,*}$; Shuo Yang$^{1,*}$

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **作者：** Teli Ma$^{1,2}$；Jia Zheng$^{1,2}$；Zifan Wang$^{1,2}$；Chunli Jiang$^{1}$；Andy Cui$^{1}$；Junwei Liang$^{2,3,*}$；Shuo Yang$^{1,*}$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Affiliations:**
>
> 1. Mondo Robotics
> 2. HKUST(GZ)
> 3. HKUST
>
> $^*$Corresponding author, Co-advising

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **作者单位：**
>
> 1. Mondo Robotics
> 2. 香港科技大学（广州）（HKUST(GZ)）
> 3. 香港科技大学（HKUST）
>
> $^*$通讯作者，共同指导

## Abstract / 摘要

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Vision-Language-Action (VLA) models have emerged as a promising paradigm for robot learning, but their representations are still largely inherited from static image-text pretraining, leaving physical dynamics to be learned from comparatively limited action data. Generative video models, by contrast, encode rich spatiotemporal structure and implicit physics, making them a compelling foundation for robotic manipulation. But their potentials are not fully explored in the literature. To bridge the gap, we introduce DiT4DiT, an end-to-end Video-Action Model that couples a video Diffusion Transformer with an action Diffusion Transformer in a unified cascaded framework. Instead of relying on reconstructed future frames, DiT4DiT extracts intermediate denoising features from the video generation process and uses them as temporally grounded conditions for action prediction. We further propose a dual flow-matching objective with decoupled timesteps and noise scales for video prediction, hidden-state extraction, and action inference, enabling coherent joint training of both modules. Across simulation and real-world benchmarks, DiT4DiT achieves state-of-the-art results, reaching average success rates of 98.6% on LIBERO and 50.8% on RoboCasa GR1 while using substantially less training data. On the Unitree G1 robot, it also delivers superior real-world performance and strong zero-shot generalization. Importantly, DiT4DiT improves sample efficiency by over 10× and speeds up convergence by up to 7×, demonstrating that video generation can serve as an effective scaling proxy for robot policy learning. We release code and models at https://dit4dit.github.io/.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 视觉-语言-动作（Vision-Language-Action，VLA）模型已成为一种很有前景的机器人学习范式，但其表征仍主要继承自静态图文预训练，使得物理动力学只能从相对有限的动作数据中学习。相比之下，生成式视频模型编码了丰富的时空结构与隐式物理规律，因此可作为机器人操作极具吸引力的基础。然而，其潜力在现有文献中尚未得到充分探索。为弥合这一差距，我们提出 DiT4DiT：一种端到端视频-动作模型，它在统一的级联框架中将视频扩散 Transformer 与动作扩散 Transformer 耦合起来。DiT4DiT 不依赖重建后的未来帧，而是从视频生成过程中提取中间去噪特征，并将其用作具有时间语义基础的动作预测条件。我们进一步提出一种双重流匹配目标，为视频预测、隐藏状态提取和动作推理设置解耦的时间步与噪声尺度，从而实现两个模块的一致联合训练。在仿真和真实世界基准上，DiT4DiT 取得了最先进的结果：在使用显著更少训练数据的同时，于 LIBERO 和 RoboCasa GR1 上分别达到 98.6% 和 50.8% 的平均成功率。在 Unitree G1 机器人上，它也展现出更优的真实世界性能与强大的零样本泛化能力。尤为重要的是，DiT4DiT 将样本效率提高了 10 倍以上，并将收敛速度最高提升至 7 倍，表明视频生成能够成为机器人策略学习的一种有效扩展代理。我们在 https://dit4dit.github.io/ 发布代码与模型。

## 1. Introduction / 引言

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Vision-Language-Action (VLA) models (Brohan et al., 2023b;a; Kim et al., 2024; Black et al., 2024; Intelligence et al., 2025a; Bjorck et al., 2025; NVIDIA et al., 2025b), built upon the success of Vision-Language Models (VLMs) (Achiam et al., 2023; Touvron et al., 2023; Karamcheti et al., 2024; Bai et al., 2025), have demonstrated remarkable capabilities across a wide range of robotic tasks. Yet most existing VLA systems inherit backbones pretrained primarily on static image-text data, leaving spatiotemporal structure and physical dynamics to be learned only during downstream policy training. In parallel, video generation models (VGMs) (Wan et al., 2025; NVIDIA et al., 2025a; Ali et al., 2025; Cai et al., 2025) have emerged as a promising alternative: by synthesizing temporally coherent and physically plausible future video frames, they learn rich motion priors, causal structure, and implicit physical dynamics. This suggests a broader opportunity for robotics: beyond serving as auxiliary models, video generators may provide a strong foundation model backbone for robot control.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 视觉-语言-动作（VLA）模型（Brohan et al., 2023b;a; Kim et al., 2024; Black et al., 2024; Intelligence et al., 2025a; Bjorck et al., 2025; NVIDIA et al., 2025b）建立在视觉-语言模型（VLM）（Achiam et al., 2023; Touvron et al., 2023; Karamcheti et al., 2024; Bai et al., 2025）的成功之上，已在广泛的机器人任务中展现出卓越能力。然而，大多数现有 VLA 系统继承的骨干网络主要在静态图文数据上预训练，因此时空结构与物理动力学只能在下游策略训练期间学习。与此同时，视频生成模型（VGM）（Wan et al., 2025; NVIDIA et al., 2025a; Ali et al., 2025; Cai et al., 2025）已成为一种很有前景的替代方案：通过合成时间一致且物理上合理的未来视频帧，它们能够学习丰富的运动先验、因果结构与隐式物理动力学。这为机器人学带来了更广泛的机会：视频生成器不仅能充当辅助模型，还可能为机器人控制提供强大的基础模型骨干。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Recent works (Unitree, 2025; Liang et al., 2025; Feng et al., 2025; Liao et al., 2025; Wang et al., 2025; Li et al., 2025a; Bi et al., 2025; Kim et al., 2026; Pai et al., 2025) have begun exploring this direction, typically by using video models to synthesize additional training data or by extracting latent representations to train inverse dynamics models for action prediction. While encouraging, these approaches are often multi-stage rather than end-to-end, making control indirect and leaving open the central question of how video generative models should be integrated to serve as a principled backbone for policy learning. In this work, we take a step toward that goal by answering two questions: (1) can video generation itself serve as an effective training objective for robust action policies? and (2) how should the spatiotemporal representations learned by video models be extracted and coupled with action generation?

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 近期工作（Unitree, 2025; Liang et al., 2025; Feng et al., 2025; Liao et al., 2025; Wang et al., 2025; Li et al., 2025a; Bi et al., 2025; Kim et al., 2026; Pai et al., 2025）已开始探索这一方向，通常利用视频模型合成额外训练数据，或提取潜在表征来训练用于动作预测的逆动力学模型。这些方法虽令人鼓舞，却往往是多阶段而非端到端的，使控制过程较为间接，并留下一个核心问题：应如何整合视频生成模型，使其成为策略学习的一种有原则的骨干网络？在本工作中，我们通过回答两个问题向这一目标迈进一步：(1) 视频生成本身能否成为鲁棒动作策略的有效训练目标？(2) 应如何提取视频模型学得的时空表征，并将其与动作生成耦合？

### Figure 1. Proxy Objectives for Scalable Robot Policy Learning / 可扩展机器人策略学习的代理目标

![Figure 1](file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_002_fig_figure_1.png)

**Caption:** Figure 1: Proxy objectives for scalable robot policy learning. Left: Comparison of three representative training paradigms: Grounding (object-level semantic alignment), FLARE-style (Zheng et al., 2025) latent modeling (VLM-to-future-frame feature prediction), and Video generation (learning physically plausible future dynamics). Right: Video generation serves as the strongest scaling proxy, yielding higher sample efficiency (up to > 10×), faster convergence (up to 7×), and more favorable scaling trends across data regimes, with consistently better downstream manipulation success than semantic-centric baselines. All results are reported as the average success rate over 24 tasks in the RoboCasa-GR1 tabletop benchmark (Nasiriany et al., 2024; Bjorck et al., 2025).

**Caption[CN]:** 图 1：面向可扩展机器人策略学习的代理目标。左：三种代表性训练范式的比较：Grounding（物体级语义对齐）、FLARE-style（Zheng et al., 2025）潜在建模（VLM 到未来帧的特征预测），以及 Video generation（学习物理上合理的未来动力学）。右：视频生成是最强的扩展代理，能够带来更高的样本效率（最高 > 10×）、更快的收敛速度（最高 7×），以及在不同数据规模下更有利的扩展趋势；与以语义为中心的基线相比，其下游操作成功率始终更高。所有结果均报告为 RoboCasa-GR1 桌面基准 24 项任务的平均成功率（Nasiriany et al., 2024; Bjorck et al., 2025）。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> We first examine whether video generation can serve as an effective proxy objective for policy learning. The strong dependence on action-labeled data has long constrained the scaling of VLA models. Prior attempts to leverage visual supervision through auxiliary tasks (e.g., grounding and VLM-centric latent feature modeling) are often sample-inefficient. For instance, methods like FLARE (Zheng et al., 2025) attempt to align current-future representations with pre-trained VLMs, but struggle to capture continuous pixel-level physical dynamics. In contrast, we find that video generation is a highly effective unsupervised pre-training signal. As shown in Fig. 1, our video-dynamics objective converges faster and achieves higher final success rates than both Grounding and FLARE-style baselines.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 我们首先考察视频生成能否作为策略学习的有效代理目标。长期以来，对动作标注数据的高度依赖一直限制着 VLA 模型的扩展。此前试图通过辅助任务利用视觉监督的方法（例如 grounding 和以 VLM 为中心的潜在特征建模）往往样本效率较低。例如，FLARE（Zheng et al., 2025）等方法尝试将当前与未来表征同预训练 VLM 对齐，但难以捕捉连续的像素级物理动力学。相比之下，我们发现视频生成是一种非常有效的无监督预训练信号。如图 1 所示，我们的视频动力学目标比 Grounding 和 FLARE-style 基线收敛得更快，并取得更高的最终成功率。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> To this end, we introduce DiT4DiT, a unified end-to-end Video-Action Model (VAM) with a dual-DiT architecture. Unlike prior methods built on visual-language autoregressive backbones, our framework adopts a bidirectional Video Diffusion Transformer (DiT) (Peebles & Xie, 2023). During denoising, we extract compact latent features from future-frame generation and use them to condition action learning, so the policy is grounded in the generative visual dynamics that govern physical interaction. To avoid disjoint multi-stage optimization, we further propose a unified joint-training paradigm based on dual flow-matching, which optimizes video and action generation in one framework. The method assigns separate timesteps and noise scales to the two modules, enabling either independent or coupled updates while transferring denoised multi-stage video latents into the action latent space. This design streamlines the training workflow and significantly shortens the convergence cycle.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 为此，我们提出 DiT4DiT：一种采用双 DiT 架构的统一端到端视频-动作模型（VAM）。与建立在视觉-语言自回归骨干上的既有方法不同，我们的框架采用双向视频扩散 Transformer（DiT）（Peebles & Xie, 2023）。在去噪过程中，我们从未来帧生成中提取紧凑的潜在特征，并用其调节动作学习，使策略扎根于支配物理交互的生成式视觉动力学。为避免彼此割裂的多阶段优化，我们进一步提出一种基于双重流匹配的统一联合训练范式，在同一框架中优化视频生成与动作生成。该方法为两个模块分配独立的时间步与噪声尺度，从而既可进行独立更新，也可进行耦合更新，同时把多阶段去噪后的视频潜变量迁移到动作潜在空间。这一设计简化了训练流程，并显著缩短了收敛周期。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> We evaluate our method extensively across both simulation and real-world settings to demonstrate its efficacy in translating generative physical priors into precise robotic control. As an end-to-end policy, DiT4DiT achieves a new state-of-the-art on both the LIBERO (Liu et al., 2024) and RoboCasa-GR1 (Nasiriany et al., 2024) Tabletop simulation benchmarks (98.6% and 50.8% average success rates, respectively). It demonstrates exceptional extended-horizon capabilities on LIBERO, outperforming recent strong VLA models like $\pi_{0.5}$ (Intelligence et al., 2025b) and CogVLA (Li et al., 2025b). On the challenging 24-task RoboCasa-GR1 suite, it decisively surpasses highly optimized, pre-trained policies like the GR00T series (Bjorck et al., 2025; NVIDIA et al., 2025b) by substantial margins. In real-world Unitree G1 deployments, DiT4DiT maintains clear advantages over both pre-trained (GR00T-N1.5 (Bjorck et al., 2025)) and parameter-matched baselines. Remarkably, relying on only a single egocentric camera, our framework extracts rich spatial reasoning capabilities, achieving the high accuracy required for precision-critical tasks such as Arrange Flower and Stack Cup. Furthermore, DiT4DiT exhibits robust zero-shot generalization under severe distribution shifts, successfully adapting to unseen objects, category changes, and quantity variations in both simulation and physical reality.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 我们在仿真与真实世界环境中广泛评估所提出的方法，以展示其将生成式物理先验转化为精确机器人控制的有效性。作为一种端到端策略，DiT4DiT 在 LIBERO（Liu et al., 2024）和 RoboCasa-GR1（Nasiriany et al., 2024）桌面仿真基准上均取得新的最先进水平（平均成功率分别为 98.6% 和 50.8%）。它在 LIBERO 上展现出卓越的长时域能力，超过了 $\pi_{0.5}$（Intelligence et al., 2025b）和 CogVLA（Li et al., 2025b）等近期强大的 VLA 模型。在具有挑战性的 24 任务 RoboCasa-GR1 套件上，它以显著优势明确超过了 GR00T 系列（Bjorck et al., 2025; NVIDIA et al., 2025b）等经过高度优化的预训练策略。在真实世界 Unitree G1 部署中，DiT4DiT 相较预训练基线（GR00T-N1.5（Bjorck et al., 2025））和参数匹配基线均保持明显优势。值得注意的是，我们的框架仅依赖一台第一视角相机，便提取出丰富的空间推理能力，达到 Arrange Flower 和 Stack Cup 等精度关键型任务所需的高准确率。此外，DiT4DiT 在严重分布偏移下展现出鲁棒的零样本泛化能力，能够在仿真和物理现实中成功适应未见物体、类别变化与数量变化。

## 2. Related Works / 相关工作

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This work connects advances in generalist robot policies with recent progress in generative world modeling. We therefore review two complementary lines of research: Visual-language-based models and video-generation-based models.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本工作将通用机器人策略的进展与生成式世界建模的近期发展联系起来。因此，我们回顾两条互补的研究路线：基于视觉-语言的模型与基于视频生成的模型。

### 2.1 Vision-Language-Action Models / 视觉-语言-动作模型

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The emergence of Vision-Language-Action (VLA) models has established a transformative paradigm for generalist robot learning. By co-fine-tuning VLMs on robotic trajectories, models such as RT-2 (Brohan et al., 2023a), OpenVLA (Kim et al., 2024), UniVLA (Bu et al., 2025), CogVLA (Li et al., 2025b), GR00T (Bjorck et al., 2025; NVIDIA et al., 2025b) and the $\pi$ (Black et al., 2024; Intelligence et al., 2025b) family successfully transfer semantic priors to embodied control. By inheriting the extensive visual and linguistic representations of their backbones, these policies demonstrate remarkable zero-shot generalization to novel instructions and semantic concepts that are otherwise absent from standard robotic datasets.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 视觉-语言-动作（VLA）模型的兴起为通用机器人学习确立了一种变革性范式。通过在机器人轨迹上共同微调 VLM，RT-2（Brohan et al., 2023a）、OpenVLA（Kim et al., 2024）、UniVLA（Bu et al., 2025）、CogVLA（Li et al., 2025b）、GR00T（Bjorck et al., 2025; NVIDIA et al., 2025b）以及 $\pi$ 系列（Black et al., 2024; Intelligence et al., 2025b）等模型成功地将语义先验迁移到具身控制。通过继承其骨干网络广泛的视觉与语言表征，这些策略对标准机器人数据集中原本缺失的新指令与语义概念展现出卓越的零样本泛化能力。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Despite their impressive semantic proficiency, a critical limitation of current VLAs stems from their foundational architecture: they rely on representations learned almost exclusively from static image-text pairs. Consequently, the heavy burden of learning low-level physical interactions and temporal state transitions falls entirely on the downstream robotic fine-tuning phase, which requires thousands of hours of training data. In contrast to these static VLA paradigms, our approach is built upon a pre-trained video diffusion model. Having been optimized to predict future frames across internet-scale video datasets, video generative models (Kong et al., 2024; Zheng et al., 2024; Ali et al., 2025; NVIDIA et al., 2025a; Wan et al., 2025) naturally internalize the complex, continuous physical dynamics of the real world. We hypothesize that harnessing these rich, pre-existing spatiotemporal and physical priors offers a fundamentally superior foundation for learning robust, low-level robotic control policies.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 尽管现有 VLA 具备令人印象深刻的语义能力，但它们的一项关键局限来自其基础架构：这些模型所依赖的表征几乎完全从静态图文对中学习。因此，学习低层物理交互与时间状态转移的沉重负担完全落在下游机器人微调阶段，而该阶段需要数千小时的训练数据。与这些静态 VLA 范式不同，我们的方法建立在预训练视频扩散模型之上。视频生成模型（Kong et al., 2024; Zheng et al., 2024; Ali et al., 2025; NVIDIA et al., 2025a; Wan et al., 2025）已在互联网规模的视频数据集上针对未来帧预测进行优化，因此会自然地内化真实世界复杂而连续的物理动力学。我们假设，利用这些丰富的既有时空与物理先验，能够为学习鲁棒的低层机器人控制策略提供根本上更优越的基础。

### 2.2 Video Generation in Robotics / 机器人学中的视频生成

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> To overcome the physical blindness of static VLMs, recent research has increasingly turned to generative video models, which naturally encapsulate rich spatiotemporal priors and complex physical dynamics (Hu et al., 2024; Ye et al., 2024; Liang et al., 2025; Feng et al., 2025; Liao et al., 2025; Wang et al., 2025; Zhong et al., 2025; Cen et al., 2025; Feng et al., 2025; Bi et al., 2025; Li et al., 2026). Historically, video prediction in robotics was primarily utilized for visual foresight, enabling model-based planning by “imagining” future states (Finn & Levine, 2017; Ebert et al., 2018; Yang et al., 2023; Du et al., 2023). However, with the advent of high-fidelity diffusion transformers, a new frontier has emerged that directly integrates video generation into policy learning.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 为克服静态 VLM 的“物理盲区”，近期研究日益转向生成式视频模型；此类模型天然包含丰富的时空先验与复杂物理动力学（Hu et al., 2024; Ye et al., 2024; Liang et al., 2025; Feng et al., 2025; Liao et al., 2025; Wang et al., 2025; Zhong et al., 2025; Cen et al., 2025; Feng et al., 2025; Bi et al., 2025; Li et al., 2026）。历史上，机器人学中的视频预测主要用于视觉预见，通过“想象”未来状态来支持基于模型的规划（Finn & Levine, 2017; Ebert et al., 2018; Yang et al., 2023; Du et al., 2023）。然而，随着高保真扩散 Transformer 的出现，一个将视频生成直接整合进策略学习的新前沿已经形成。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> A recent line of work (Shen et al., 2025; Li et al., 2025a; Bi et al., 2025; Li et al., 2026) has explored projecting both visual dynamics and control signals into a shared latent space. These models effectively consolidate versatile capabilities (such as forward simulation and inverse dynamics) into a single learned system. Building upon this trend of explicit unification, Cosmos Policy (Kim et al., 2026) further simplifies the adaptation by fine-tuning a pre-trained video diffusion model to directly output robot actions and future expected values, encoding them as contiguous latent frames within the native video diffusion process. The most closely related work, mimic-video (Pai et al., 2025), pairs a pre-trained video backbone with a separate flow-matching action decoder and conditions the policy on partially denoised video latents at an intermediate flow time. In contrast, we explore joint training of video and action generation, enabling the action model to learn how to extract effective features across different stages of the video generation process, yielding more robust representations.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 近期一系列工作（Shen et al., 2025; Li et al., 2025a; Bi et al., 2025; Li et al., 2026）探索了将视觉动力学与控制信号共同投影到一个共享潜在空间中。这些模型实际上把多种能力（例如正向仿真和逆动力学）整合到一个学习系统中。在这种显式统一趋势的基础上，Cosmos Policy（Kim et al., 2026）通过微调预训练视频扩散模型，使其直接输出机器人动作与未来期望值，并将二者编码为原生视频扩散过程中的连续潜在帧，从而进一步简化适配。与本文最相关的工作 mimic-video（Pai et al., 2025）将预训练视频骨干与独立的流匹配动作解码器配对，并以中间流时间上部分去噪的视频潜变量作为策略条件。相比之下，我们探索视频生成与动作生成的联合训练，使动作模型能够学习如何从视频生成过程的不同阶段提取有效特征，从而得到更鲁棒的表征。

## 3. Validation of Video Generation as a Scaling Proxy / 验证视频生成作为扩展代理的有效性

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> A core hypothesis of this work is that video generation is an effective proxy task for robot control. Hence, we first test it to ensure that the design choices are grounded in empirical evidence. We conduct a comparative study against two paradigms. The first is object-level grounding as (Bjorck et al., 2025), training the VLM with an auxiliary detection head to drive the VLM to understand “what” and “where” objects are for VLA. The other one is the implicit world modeling method based on VLM like FLARE-style. FLARE (Zheng et al., 2025) attends features from VLM with learnable queries and aligns the queries with latent embeddings of future observations. We abandon the diffusion process of the queries in FLARE to perform FLARE-like pre-training here. We use Qwen3-2B (Bai et al., 2025) and Cosmos-Predict2.5-2B (Ali et al., 2025) as the VLM and Video backbone to ensure that the scale of trainable parameters remains consistent.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本工作的一项核心假设是，视频生成是机器人控制的一种有效代理任务。因此，我们首先对其进行检验，以确保相关设计选择具有实证依据。我们与两种范式开展比较研究。第一种是（Bjorck et al., 2025）采用的物体级 grounding：使用一个辅助检测头训练 VLM，促使 VLM 理解 VLA 中物体“是什么”以及“在哪里”。另一种是类似 FLARE-style、基于 VLM 的隐式世界建模方法。FLARE（Zheng et al., 2025）使用可学习查询对 VLM 特征进行注意力操作，并将这些查询与未来观测的潜在嵌入对齐。在这里，为实施类似 FLARE 的预训练，我们舍弃了 FLARE 中查询的扩散过程。我们分别采用 Qwen3-2B（Bai et al., 2025）和 Cosmos-Predict2.5-2B（Ali et al., 2025）作为 VLM 与视频骨干，以确保可训练参数规模保持一致。

### Figure 2. Overview of the Proposed DiT4DiT Framework / DiT4DiT 框架概览

![Figure 2](file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_004_fig_figure_2.png)

**Caption:** Figure 2: Overview of the proposed DiT4DiT framework. Top: Given the current observation and language goal, the video DiT predicts future dynamics and exposes intermediate generative features at the specific flow timestep; these features condition the action DiT to infer control trajectories. The two models are jointly optimized with a dual flow-matching objective for video generation and action prediction. Below: Generated visual plans via video DiT (More examples are shown in Fig. 10).

**Caption[CN]:** 图 2：所提出 DiT4DiT 框架的概览。上：给定当前观测和语言目标，视频 DiT 预测未来动力学，并在特定流时间步公开中间生成特征；这些特征对动作 DiT 进行条件化，使其推断控制轨迹。两个模型通过针对视频生成和动作预测的双重流匹配目标进行联合优化。下：由视频 DiT 生成的视觉规划（更多示例见图 10）。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> We validate on 24 tabletop manipulation tasks involving the GR1 humanoid robot (Nasiriany et al., 2024; Bjorck et al., 2025) in the RoboCasa simulation. To more effectively evaluate the efficacy of the proxy task, we decouple the pre-training phase from the downstream training of the action expert across all three experimental settings. The VLM and Video backbones are trained on the target dataset in a self-supervised manner (except that the grounding task uses pre-annotated bounding boxes), and then kept frozen during the fine-tuning of the action expert. The empirical results (see Fig. 1) showcase the superiority of the video generation objective in training efficiency and scalability. The generative proxy task allows the model to converge to high-performance policies much faster (up to 7×), capturing essential manipulation cues early in the training process. Also, it demonstrates a robust scaling behavior: demonstrating significantly higher data efficiency (up to 10×) than semantic-centric based methods and maintaining a consistent performance improvement as the data volume increases. This validates video generation not only as an efficient training task but as a viable scaling proxy for generalizable robot control.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 我们在 RoboCasa 仿真环境中涉及 GR1 人形机器人（Nasiriany et al., 2024; Bjorck et al., 2025）的 24 项桌面操作任务上进行验证。为更有效地评估代理任务的效力，我们在全部三种实验设置中将预训练阶段与下游动作专家训练解耦。VLM 与视频骨干以自监督方式在目标数据集上训练（但 grounding 任务使用预标注边界框），随后在微调动作专家期间保持冻结。实证结果（见图 1）展示了视频生成目标在训练效率与可扩展性方面的优越性。生成式代理任务使模型能够更快地（最高 7×）收敛到高性能策略，并在训练早期捕捉关键操作线索。此外，它还展现出鲁棒的扩展行为：相较以语义为中心的方法，其数据效率显著更高（最高 10×），且随着数据量增加仍保持一致的性能提升。这证明视频生成不仅是一项高效的训练任务，也是可泛化机器人控制的一种可行扩展代理。

## 4. DiT4DiT: Unleashing the Potential of Video Model / DiT4DiT：释放视频模型的潜力

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This section details DiT4DiT, an integrated Video-Action Model (VAM) designed for the joint optimization of Video and Action DiTs. By employing a dual flow-matching objective, our framework concurrently refines video synthesis and action prediction. This synergy allows the action policy to derive trajectories directly from the joint distribution, effectively grounding robotic control in the generative dynamics of the video backbone.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本节详细介绍 DiT4DiT，这是一种为视频 DiT 与动作 DiT 的联合优化而设计的一体化视频-动作模型（VAM）。通过采用双重流匹配目标，我们的框架能够同时改进视频合成与动作预测。二者的协同使动作策略可以直接从联合分布中导出轨迹，从而有效地将机器人控制建立在视频骨干的生成动力学之上。

### 4.1 Preliminaries / 预备知识

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Flow matching.** Flow Matching (FM) aims to regress a time-dependent velocity field $v_\theta(x,\tau)$ that transports samples along a probability path between a noise distribution $p_1=\mathcal{N}(0,I)$ and the data distribution $p_0$ (Lipman et al., 2022). Specifically, consider a conditional probability path $p_\tau(x\mid x_0)$ constructed via an optimal transport displacement map. The interpolation path is defined as:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **流匹配。** 流匹配（Flow Matching，FM）旨在回归一个随时间变化的速度场 $v_\theta(x,\tau)$，该速度场沿噪声分布 $p_1=\mathcal{N}(0,I)$ 与数据分布 $p_0$ 之间的一条概率路径传输样本（Lipman et al., 2022）。具体而言，考虑一条通过最优传输位移映射构造的条件概率路径 $p_\tau(x\mid x_0)$。其插值路径定义为：

$$
x_\tau=(1-\tau)\cdot x_0+\tau\cdot z,\qquad \tau\in[0,1].
\tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> where $x_0\sim p_{\mathrm{data}}$ and $z\sim\mathcal{N}(0,I)$. Under this formulation, $\tau=0$ corresponds to the clean data point $x_0$, while $\tau=1$ denotes pure Gaussian noise $z$. The target velocity (ground truth flow) that generates this linear interpolation is the time derivative:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 其中，$x_0\sim p_{\mathrm{data}}$，且 $z\sim\mathcal{N}(0,I)$。在这一形式化定义下，$\tau=0$ 对应干净数据点 $x_0$，而 $\tau=1$ 表示纯高斯噪声 $z$。生成该线性插值的目标速度（真实流）为其时间导数：

$$
v^*(x_\tau,\tau)=\frac{dx_\tau}{d\tau}=z-x_0.
\tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The training objective of flow matching is to minimize the expected $L_2$ distance between the predicted velocity field $v_\theta$ and the target velocity:

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 流匹配的训练目标是最小化预测速度场 $v_\theta$ 与目标速度之间的期望 $L_2$ 距离：

$$
\mathcal{L}_{\mathrm{FM}}
=
\mathbb{E}_{x_0,z,\tau}
\left[
\left\|v_\theta(x_\tau,\tau)-(z-x_0)\right\|_2^2
\right].
\tag{3}
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> where $\tau$ is sampled uniformly from $\mathcal{U}[0,1]$. During inference, sampling is performed by solving the Ordinary Differential Equation (ODE) associated with the learned velocity field $v_\theta$. This process involves integrating $v_\theta$ starting from the noise distribution at $\tau=1$ toward the data distribution at $\tau=0$:

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 其中，$\tau$ 从 $\mathcal{U}[0,1]$ 中均匀采样。推理期间，通过求解与学习到的速度场 $v_\theta$ 对应的常微分方程（ODE）来进行采样。该过程从 $\tau=1$ 时的噪声分布开始，对 $v_\theta$ 进行积分，并朝 $\tau=0$ 时的数据分布推进：

$$
\frac{dx}{d\tau}=v_\theta(x,\tau),\qquad x_1\sim\mathcal{N}(0,I).
\tag{4}
$$

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> We employ a first-order Euler discretization to perform the numerical integration. Given a total of $N$ sampling steps and a constant step size $\Delta\tau=1/N$, the iterative update rule is formulated as:

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 我们采用一阶 Euler 离散化执行数值积分。给定总计 $N$ 个采样步以及恒定步长 $\Delta\tau=1/N$，迭代更新规则写为：

$$
x_{\tau-\Delta\tau}=x_\tau-\Delta\tau\cdot v_\theta(x_\tau,\tau).
\tag{5}
$$

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> **Problem statement.** Instead of current VLA policies that map directly from observations to actions as $\pi_\theta(a_t\mid o_t,l)$ ($l$ is the language goal), DiT4DiT follows a paradigm of predicting video dynamics-inverse dynamics. Specifically, the task is to sample video dynamics from inference of video DiT, and predict the actions by reversing the video dynamics sampled. We formulate the process as:

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> **问题陈述。** 当前 VLA 策略以 $\pi_\theta(a_t\mid o_t,l)$（$l$ 为语言目标）的形式直接将观测映射到动作；与之不同，DiT4DiT 遵循预测视频动力学-逆动力学的范式。具体而言，该任务从视频 DiT 的推理中采样视频动力学，再通过反演所采样的视频动力学来预测动作。我们将这一过程形式化为：

$$
o_{t+1}\sim p_v(\cdot\mid o_t,l),
\tag{6}
$$

$$
a_t\sim p_a\!\left(\cdot\mid o_t,H(o_{t+1}^{\tau_v})\right),
\qquad
o_{t+1}^{\tau_v}\xrightarrow{\tau_v\to0}o_{t+1}.
\tag{7}
$$

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> where $p_v$ and $p_a$ denote the probability distributions of video generation and action generation, respectively. $o_{t+1}^{\tau_v}$ means the intermediate state of the future frame at flow step $\tau_v$, reflecting its degree of generation, and $H$ means the process of extracting hidden states from the generation of $o_{t+1}^{\tau_v}$. The training task is to model the joint probability distribution $p_{va}$ of $p_v$ and $p_a$ like:

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 其中，$p_v$ 与 $p_a$ 分别表示视频生成和动作生成的概率分布。$o_{t+1}^{\tau_v}$ 表示流时间步 $\tau_v$ 上未来帧的中间状态，反映其生成程度；$H$ 表示从 $o_{t+1}^{\tau_v}$ 的生成过程中提取隐藏状态的过程。训练任务是如下建模 $p_v$ 与 $p_a$ 的联合概率分布 $p_{va}$：

$$
o_{t+1},a_t\sim p_{va}(\cdot\mid o_t,l).
\tag{8}
$$

### 4.2 Dual-DiT Architecture / 双 DiT 架构

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Let $o_t\in\mathbb{R}^{T_{\mathrm{cond}}\times3\times H\times W}$ denote the observation frames (conditional input, $T_{\mathrm{cond}}$ denote the number of condition frames) and $o_{t+1}\in\mathbb{R}^{T_v\times3\times H\times W}$ denote the ground truth future frames, where $T_v$ represents the horizon of future frames.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 令 $o_t\in\mathbb{R}^{T_{\mathrm{cond}}\times3\times H\times W}$ 表示观测帧（条件输入，$T_{\mathrm{cond}}$ 表示条件帧数量），令 $o_{t+1}\in\mathbb{R}^{T_v\times3\times H\times W}$ 表示真实未来帧，其中 $T_v$ 表示未来帧的预测时域。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> **Video DiT.** We use the Cosmos-Predict2.5-2B (Ali et al., 2025) as the initialization of our video backbone. This backbone consists of two primary components: a causal video VAE and a video diffusion transformer. The spatio-temporal VAE serves as the initial compression stage, mapping high-dimensional pixel-space observations $o_t,o_{t+1}$ into a compact latent space via significant spatial and temporal downsampling, denoted as $z_t^0,z_{t+1}^0$. The normalized latents $z_t^0$ are then processed by the DiT, which utilizes a flow-prediction parameterization and is conditioned on language instructions via multi-layer embeddings from Cosmos-Reason1 (Azzolini et al., 2025). Crucially, rather than utilizing the final denoised video output, we repurpose the DiT (Peebles & Xie, 2023) as a feature extractor: a forward hook mechanism intercepts intermediate hidden activations in flow timestep $\tau_f$—either from a specific deep transformer block or averaged across all layers—converting the generative process into rich visual tokens for downstream tasks. This process is formulated as:

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> **视频 DiT。** 我们使用 Cosmos-Predict2.5-2B（Ali et al., 2025）初始化视频骨干。该骨干由两个主要组件构成：因果视频 VAE 与视频扩散 Transformer。时空 VAE 充当初始压缩阶段，通过显著的空间与时间下采样，将高维像素空间观测 $o_t,o_{t+1}$ 映射到紧凑的潜在空间，记为 $z_t^0,z_{t+1}^0$。随后，归一化潜变量 $z_t^0$ 由 DiT 处理；该 DiT 采用流预测参数化，并通过 Cosmos-Reason1（Azzolini et al., 2025）的多层嵌入以语言指令为条件。关键在于，我们不使用最终去噪后的视频输出，而是将 DiT（Peebles & Xie, 2023）重新用作特征提取器：前向 hook 机制在流时间步 $\tau_f$ 截取中间隐藏激活——这些激活可以取自特定的深层 Transformer 块，也可以在所有层上求平均——从而将生成过程转化为面向下游任务的丰富视觉 token。该过程形式化为：

$$
h^{\tau_f}
=
H\!\left[
v_{\mathrm{video}}\!\left(z_{t+1}^{\tau_f},\tau_f\mid z_t^0,l\right)
\right],
\qquad
z_{t+1}^{\tau_f}\xrightarrow{\tau_f\to0}z_{t+1}^0.
\tag{9}
$$

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> where $H$ denotes the hook operator that extracts the internal hidden states during the forward pass of the velocity network $v_{\mathrm{video}}$, and $z_{t+1}^{\tau_f}\xrightarrow{\tau_f\to0}z_{t+1}^0$ indicates the probability flow toward the clean future latent.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> 其中，$H$ 表示 hook 算子，它在速度网络 $v_{\mathrm{video}}$ 的前向传播过程中提取内部隐藏状态；$z_{t+1}^{\tau_f}\xrightarrow{\tau_f\to0}z_{t+1}^0$ 表示朝向干净未来潜变量的概率流。

### Figure 3. Asymmetric Tri-timestep Design / 非对称三时间步设计

![Figure 3](file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_006_fig_figure_3.png)

**Caption:** Figure 3: Asymmetric tri-timestep design. We decouple the diffusion timesteps to optimize joint video-action generation. The video module uses uniform sampling ($\tau_v$) to capture the full denoising trajectory, while the action module uses Beta sampling ($\tau_a$) to focus on critical control phases. Meanwhile, stable visual conditions are extracted at a fixed deterministic timestep ($\tau_f$) from the evolving hidden states ($h_t^1\to h_t^0$).

**Caption[CN]:** 图 3：非对称三时间步设计。我们解耦扩散时间步，以优化视频-动作联合生成。视频模块使用均匀采样（$\tau_v$）捕捉完整去噪轨迹，而动作模块使用 Beta 采样（$\tau_a$）聚焦关键控制阶段。与此同时，从不断演化的隐藏状态（$h_t^1\to h_t^0$）中，在一个固定的确定性时间步（$\tau_f$）提取稳定的视觉条件。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> **Action DiT.** To decode these visual representations into continuous robot control commands, we employ a dedicated action diffusion transformer adapted from the GR00T-N1 (Bjorck et al., 2025). This component operates as a separate flow-matching model composed of a stack of transformer blocks, each utilizing Adaptive Layer Normalization (AdaLN) (Peebles & Xie, 2023) to inject diffusion timestep information and cross-attention layers to attend to the visual features $h^{\tau_f}$ extracted by the video backbone. The input sequence to this DiT is a concatenation of proprioceptive state embeddings, encoded noisy action trajectories, and a set of learnable “future tokens” that serve as compressed queries for the motion planning task. Through the cross-attention mechanism, the action head fuses the spatiotemporal visual context with the robot’s state, refining the noisy inputs into a coherent trajectory. The network terminates with a linear projection that predicts the velocity vector field of the action sequence, allowing the final trajectory to be synthesized via iterative numerical integration during inference.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> **动作 DiT。** 为将这些视觉表征解码为连续的机器人控制指令，我们采用一个改造自 GR00T-N1（Bjorck et al., 2025）的专用动作扩散 Transformer。该组件作为独立的流匹配模型运行，由一组 Transformer 块堆叠而成；每个块均使用自适应层归一化（AdaLN）（Peebles & Xie, 2023）注入扩散时间步信息，并使用交叉注意力层关注视频骨干提取的视觉特征 $h^{\tau_f}$。该 DiT 的输入序列由本体感知状态嵌入、编码后的含噪动作轨迹，以及一组充当运动规划任务压缩查询的可学习“未来 token”拼接而成。通过交叉注意力机制，动作头将时空视觉上下文与机器人状态融合，把含噪输入逐步改进为一致轨迹。网络最后通过线性投影预测动作序列的速度向量场，从而可在推理期间通过迭代数值积分合成最终轨迹。

### 4.3 Joint Training of Video and Action / 视频与动作的联合训练

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> To operationalize the simultaneous modeling of latent representations for both video and action, we propose a Dual Flow-Matching mechanism. This approach unifies the generative video prediction and the inverse dynamics of action inference into a single learning paradigm, optimizing both DiTs through a joint objective.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> 为实现视频与动作潜在表征的同步建模，我们提出一种双重流匹配机制。该方法将生成式视频预测与动作推理的逆动力学统一为单一学习范式，并通过联合目标优化两个 DiT。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> **Tri-timestep scheme.** A core challenge in this joint optimization is balancing the divergent requirements of generative modeling and feature extraction. To address this and achieve the simultaneous modeling of latent representations for both video and action, we adopt an asymmetric tri-timestep scheme that decouples the diffusion process of the visual backbone from that of the action module, as shown in Fig. 3.

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> **三时间步方案。** 这一联合优化的核心挑战是平衡生成建模与特征提取彼此不同的需求。为解决该问题，并实现视频与动作潜在表征的同步建模，我们采用非对称三时间步方案，将视觉骨干的扩散过程与动作模块的扩散过程解耦，如图 3 所示。

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> For the video generation module, we follow the standard diffusion training (NVIDIA et al., 2025a; Ali et al., 2025) paradigm. At each training step, the prediction timestep $\tau_v$ is randomly sampled from a uniform distribution, $\tau_v\sim\mathcal{U}[0,1]$. This exposes the model to all noise levels, forcing it to learn the full denoising trajectory required to synthesize future frames.

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> 对于视频生成模块，我们遵循标准扩散训练范式（NVIDIA et al., 2025a; Ali et al., 2025）。在每个训练步，预测时间步 $\tau_v$ 从均匀分布中随机采样，即 $\tau_v\sim\mathcal{U}[0,1]$。这使模型接触所有噪声水平，迫使其学习合成未来帧所需的完整去噪轨迹。

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> Conversely, the feature extraction process requires deterministic and consistent representations across iterations to ensure the downstream action module receives a stable input signal. Therefore, when extracting the intermediate representation $h_t^{\tau_f}$, we forward the context frames through the denoising backbone at a fixed timestep, denoted as $\tau_f$. This fixed timestep acts as a conditioning signal, selecting a specific “operating point” of the backbone: while early diffusion stages emphasize global structure, later stages attend to fine-grained details. By fixing this value, we stabilize the latent representations, yielding features that are consistently informative for downstream action prediction during both training and inference.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> 相反，特征提取过程要求各次迭代中的表征具有确定性和一致性，以确保下游动作模块接收到稳定的输入信号。因此，在提取中间表征 $h_t^{\tau_f}$ 时，我们在记为 $\tau_f$ 的固定时间步，让上下文帧通过去噪骨干。该固定时间步充当条件信号，用于选定骨干的某个特定“工作点”：扩散早期阶段强调全局结构，而后期阶段关注细粒度细节。通过固定该值，我们使潜在表征保持稳定，从而在训练与推理期间都得到能够持续为下游动作预测提供信息的特征。

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> Finally, the action DiT relies on a third, independent timestep, $\tau_a$. Unlike the video generation module which employs uniform sampling, $\tau_a$ is drawn from a Beta distribution during training ($\tau_a=1-\sigma$, where $\sigma\sim\operatorname{Beta}(\alpha,\beta)$). This biased continuous-time sampling strategy allocates more training capacity to the most critical stages of the flow trajectory. This complete decoupling allows the action decoder to independently learn the optimal inverse dynamics—mapping pure noise to precise actions—while remaining continuously conditioned on the stable visual features provided by the fixed feature-extraction timestep $\tau_f$.

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> 最后，动作 DiT 依赖第三个独立时间步 $\tau_a$。视频生成模块采用均匀采样，而 $\tau_a$ 在训练期间从 Beta 分布中抽取（$\tau_a=1-\sigma$，其中 $\sigma\sim\operatorname{Beta}(\alpha,\beta)$）。这种有偏连续时间采样策略将更多训练容量分配给流轨迹中最关键的阶段。完全解耦使动作解码器能够独立学习最优逆动力学——把纯噪声映射为精确动作——同时持续以固定特征提取时间步 $\tau_f$ 所提供的稳定视觉特征为条件。

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> **Training.** The video and action DiTs are jointly fine-tuned to achieve simultaneous modeling of latent representations for both video and action, as detailed in Algorithm 1. During training, the text encoder and visual VAE are frozen, restricting the parameter updates entirely to the DiT modules to adapt them to the target domain. Building upon this dual-timestep design, the overall training objective is formulated as a joint flow-matching loss:

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> **训练。** 视频 DiT 与动作 DiT 进行联合微调，以实现视频和动作潜在表征的同步建模，详见算法 1。训练期间，文本编码器和视觉 VAE 保持冻结，从而把参数更新完全限制在 DiT 模块内，使其适应目标域。在这一双时间步设计的基础上，总体训练目标被表述为联合流匹配损失：

$$
\begin{aligned}
\mathcal{L}_{\mathrm{total}}
={}&
\underbrace{
\mathbb{E}_{\tau_a,\epsilon}
\left[
\left\|
v_{\mathrm{action}}\!\left(a_t^{\tau_a},\tau_a\mid h_t^{\tau_f},s\right)
-\left(\epsilon-a_t^0\right)
\right\|_2^2
\right]
}_{\text{Action Flow Matching Loss}}
\\
&+
\lambda
\underbrace{
\mathbb{E}_{\tau_v,z}
\left[
\left\|
v_{\mathrm{video}}\!\left(z_{t+1}^{\tau_v},\tau_v\mid z_t^0,l\right)
-\left(z-z_{t+1}^0\right)
\right\|_2^2
\right]
}_{\text{Video Flow Matching Loss}} .
\end{aligned}
\tag{10}
$$

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> where $\lambda$ is a scalar coefficient that balances the two learning signals. For the video flow-matching objective, the video DiT is trained to predict the velocity via $v_{\mathrm{video}}$ that transports the current observation $z_t^0$ and language goal $l$ toward the future latent state. For the action flow-matching objective, the action DiT learns to map the noisy action to the target action velocity $\epsilon-a_t^0$. Crucially, this action prediction is conditioned on the robot’s proprioceptive state $s$ and the hidden features $h^{\tau_f}$ extracted from the video backbone in timestep $\tau_f$ as shown in Eqn. 9. By jointly minimizing these objectives, the framework ensures that the generative dynamics of the visual world inherently scaffold the execution of complex robotic actions.

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> 其中，$\lambda$ 是平衡两种学习信号的标量系数。对于视频流匹配目标，训练视频 DiT 通过 $v_{\mathrm{video}}$ 预测速度，将当前观测 $z_t^0$ 和语言目标 $l$ 朝未来潜在状态传输。对于动作流匹配目标，动作 DiT 学习把含噪动作映射到目标动作速度 $\epsilon-a_t^0$。关键在于，如式 9 所示，该动作预测以机器人本体感知状态 $s$，以及在时间步 $\tau_f$ 从视频骨干提取的隐藏特征 $h^{\tau_f}$ 为条件。通过联合最小化这些目标，该框架确保视觉世界的生成动力学能够内在地支撑复杂机器人动作的执行。

### Algorithm 1. Joint Training of Video and Action DiT / 视频与动作 DiT 的联合训练

![Algorithm 1](file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_007_fig_algorithm_1.png)

**Caption:** Algorithm 1: Joint Training of Video and Action DiT

**Caption[CN]:** 算法 1：视频与动作 DiT 的联合训练

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> **Algorithm 1: Joint Training of Video and Action DiT**
>
> **Require:** Observation $o_t$, future frame $o_{t+1}$, action $a^0$, state $s$, language goal $l$, action mask $M$
>
> **Ensure:** Updated parameters $\theta$ (Video DiT), $\phi$ (Action DiT)
>
> 1: <code>// ===== Video DiT Forward =====</code>
>
> 2: $z_t^0\leftarrow\operatorname{VAE}_{\mathrm{enc}}(o_t)$ $\triangleright$ Encode observation
>
> 3: $z_{t+1}^0\leftarrow\operatorname{VAE}_{\mathrm{enc}}(o_{t+1})$ $\triangleright$ Encode future frames
>
> 4: $\tau_v\sim\mathcal{U}[0,1]$ $\triangleright$ Sample video timestep
>
> 5: $z\sim\mathcal{N}(0,I)$ $\triangleright$ Sample video noise
>
> 6: $z_{t+1}^{\tau_v}\leftarrow(1-\tau_v)\cdot z_{t+1}^0+\tau_v\cdot z$ $\triangleright$ Noisy future latent
>
> 7: $\hat v_{\mathrm{video}}\leftarrow v_{\mathrm{video}}(z_{t+1}^{\tau_v},\tau_v\mid z_t^0,l)$ $\triangleright$ Predict velocity
>
> 8: $v_{\mathrm{video}}^*\leftarrow z-z_{t+1}^0$ $\triangleright$ Target velocity
>
> 9: $\mathcal{L}_{\mathrm{video}}\leftarrow\|\hat v_{\mathrm{video}}-v_{\mathrm{video}}^*\|^2$ $\triangleright$ Video loss
>
> 10: <code>// ===== Extract Hidden States =====</code>
>
> 11: $\tau_f\sim\mathcal{U}\{0/T,1/T,\ldots,T/T\}$ $\triangleright$ Sample hidden extracting timestep
>
> 12: $\hat z_{t+1}\sim\mathcal{N}(0,I)$ $\triangleright$ Sample future noise
>
> 13: $h^{\tau_f}\leftarrow H(\theta,\hat z_{t+1},\tau_f,z_t^0,l)$ $\triangleright$ Extract hidden states
>
> 14: <code>// ===== Action DiT Forward =====</code>
>
> 15: $\sigma\sim\operatorname{Beta}(\alpha,\beta)$; $\tau_a\leftarrow1-\sigma$ $\triangleright$ Sample action timestep
>
> 16: $\epsilon\sim\mathcal{N}(0,I)$ $\triangleright$ Sample action noise
>
> 17: $a^{\tau_a}\leftarrow(1-\tau_a)\cdot a_t^0+\tau_a\cdot\epsilon$ $\triangleright$ Noisy action
>
> 18: $\hat v_{\mathrm{action}}\leftarrow v_{\mathrm{action}}(a_t^{\tau_a},\tau_a\mid h_t^{\tau_f},s)$ $\triangleright$ Predict velocity
>
> 19: $v_{\mathrm{action}}^*\leftarrow\epsilon-a^0$ $\triangleright$ Target velocity
>
> 20: $\mathcal{L}_{\mathrm{action}}\leftarrow\|(\hat v_{\mathrm{action}}-v_{\mathrm{action}}^*)\odot M\|^2/\|M\|_1$ $\triangleright$ Masked action loss
>
> 21: <code>// ===== Backward =====</code>
>
> 22: $\mathcal{L}_{\mathrm{total}}\leftarrow\mathcal{L}_{\mathrm{action}}+\lambda\cdot\mathcal{L}_{\mathrm{video}}$
>
> 23: Update $\theta,\phi$ via $\nabla\mathcal{L}_{\mathrm{total}}$

> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> **算法 1：视频与动作 DiT 的联合训练**
>
> **输入要求：** 观测 $o_t$、未来帧 $o_{t+1}$、动作 $a^0$、状态 $s$、语言目标 $l$、动作掩码 $M$
>
> **输出保证：** 更新后的参数 $\theta$（视频 DiT）、$\phi$（动作 DiT）
>
> 1: <code>// ===== 视频 DiT 前向传播 =====</code>
>
> 2: $z_t^0\leftarrow\operatorname{VAE}_{\mathrm{enc}}(o_t)$ $\triangleright$ 编码观测
>
> 3: $z_{t+1}^0\leftarrow\operatorname{VAE}_{\mathrm{enc}}(o_{t+1})$ $\triangleright$ 编码未来帧
>
> 4: $\tau_v\sim\mathcal{U}[0,1]$ $\triangleright$ 采样视频时间步
>
> 5: $z\sim\mathcal{N}(0,I)$ $\triangleright$ 采样视频噪声
>
> 6: $z_{t+1}^{\tau_v}\leftarrow(1-\tau_v)\cdot z_{t+1}^0+\tau_v\cdot z$ $\triangleright$ 含噪未来潜变量
>
> 7: $\hat v_{\mathrm{video}}\leftarrow v_{\mathrm{video}}(z_{t+1}^{\tau_v},\tau_v\mid z_t^0,l)$ $\triangleright$ 预测速度
>
> 8: $v_{\mathrm{video}}^*\leftarrow z-z_{t+1}^0$ $\triangleright$ 目标速度
>
> 9: $\mathcal{L}_{\mathrm{video}}\leftarrow\|\hat v_{\mathrm{video}}-v_{\mathrm{video}}^*\|^2$ $\triangleright$ 视频损失
>
> 10: <code>// ===== 提取隐藏状态 =====</code>
>
> 11: $\tau_f\sim\mathcal{U}\{0/T,1/T,\ldots,T/T\}$ $\triangleright$ 采样隐藏状态提取时间步
>
> 12: $\hat z_{t+1}\sim\mathcal{N}(0,I)$ $\triangleright$ 采样未来噪声
>
> 13: $h^{\tau_f}\leftarrow H(\theta,\hat z_{t+1},\tau_f,z_t^0,l)$ $\triangleright$ 提取隐藏状态
>
> 14: <code>// ===== 动作 DiT 前向传播 =====</code>
>
> 15: $\sigma\sim\operatorname{Beta}(\alpha,\beta)$；$\tau_a\leftarrow1-\sigma$ $\triangleright$ 采样动作时间步
>
> 16: $\epsilon\sim\mathcal{N}(0,I)$ $\triangleright$ 采样动作噪声
>
> 17: $a^{\tau_a}\leftarrow(1-\tau_a)\cdot a_t^0+\tau_a\cdot\epsilon$ $\triangleright$ 含噪动作
>
> 18: $\hat v_{\mathrm{action}}\leftarrow v_{\mathrm{action}}(a_t^{\tau_a},\tau_a\mid h_t^{\tau_f},s)$ $\triangleright$ 预测速度
>
> 19: $v_{\mathrm{action}}^*\leftarrow\epsilon-a^0$ $\triangleright$ 目标速度
>
> 20: $\mathcal{L}_{\mathrm{action}}\leftarrow\|(\hat v_{\mathrm{action}}-v_{\mathrm{action}}^*)\odot M\|^2/\|M\|_1$ $\triangleright$ 掩码动作损失
>
> 21: <code>// ===== 反向传播 =====</code>
>
> 22: $\mathcal{L}_{\mathrm{total}}\leftarrow\mathcal{L}_{\mathrm{action}}+\lambda\cdot\mathcal{L}_{\mathrm{video}}$
>
> 23: 通过 $\nabla\mathcal{L}_{\mathrm{total}}$ 更新 $\theta,\phi$

### 4.4 Inference / 推理

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> During inference, the DiT4DiT framework demonstrates highly flexible generative capabilities, equipped to perform both video generation and action prediction. It executes a decoupled sampling procedure that can synthesize future visual dynamics, infer precise robot control commands, or perform both tasks concurrently, as detailed in Algorithm 2.

> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> 推理期间，DiT4DiT 框架展现出高度灵活的生成能力，能够同时执行视频生成与动作预测。它采用解耦的采样过程，可以合成未来视觉动力学、推断精确的机器人控制指令，或同时执行两项任务，详见算法 2。

> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> **Video DiT Sampling.** When tasked with synthesizing future visual dynamics, the framework activates the video generation pathway. The current observation $o_t$ is compressed into a latent representation $z_t^0$ via the frozen VAE encoder. Starting from a standard Gaussian noise distribution $\hat z_{t+1}\sim\mathcal{N}(0,I)$, the video model iteratively updates the latent over $N_v$ discrete steps. At each flow step $\tau_v$, the network predicts the velocity field $\hat v$ conditioned on the initial observation $z_t^0$ and the language goal $l$. The latent is updated using the Euler step rule until it reaches the clean future state, which is subsequently projected back to pixel space via the VAE decoder to yield the predicted future frame $\hat o_{t+1}$.

> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> **视频 DiT 采样。** 当任务要求合成未来视觉动力学时，框架会激活视频生成路径。当前观测 $o_t$ 通过冻结的 VAE 编码器压缩为潜在表征 $z_t^0$。视频模型从标准高斯噪声分布 $\hat z_{t+1}\sim\mathcal{N}(0,I)$ 出发，在 $N_v$ 个离散步中迭代更新潜变量。在每个流时间步 $\tau_v$，网络以初始观测 $z_t^0$ 和语言目标 $l$ 为条件预测速度场 $\hat v$。潜变量按照 Euler 步进规则更新，直至到达干净的未来状态；随后通过 VAE 解码器将其投影回像素空间，得到预测未来帧 $\hat o_{t+1}$。

> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> **Action DiT Sampling.** Rather than relying on the intermediate states of the full video generation loop, the action conditioning requires only a single, deterministic feature extraction step. We sample a new noise latent and perform a single forward pass through the video backbone evaluated strictly at the fixed feature-extraction timestep $\tau_f$. This step intercepts the intermediate activations via the hook mechanism $H$, yielding a stable and deterministic hidden representation $h_t^{\tau_f}$. With the visual context established, the action trajectory is initialized from noise $\hat a_t\sim\mathcal{N}(0,I)$. Over $N_a$ numerical integration steps, the Action DiT predicts the action velocity field conditioned on the extracted generative features $h^{\tau_f}$ and the robot’s proprioceptive state $s$. The trajectory is refined iteratively, ultimately yielding the precise predicted action $\hat a_t$.

> <span style="color:#F59E0B"><strong>Para. 23[CN]:</strong></span> **动作 DiT 采样。** 动作条件不依赖完整视频生成循环的中间状态，只需进行一次确定性的特征提取。我们采样一个新的噪声潜变量，并让视频骨干严格在固定特征提取时间步 $\tau_f$ 上执行单次前向传播。该步骤通过 hook 机制 $H$ 截取中间激活，得到稳定且确定性的隐藏表征 $h_t^{\tau_f}$。在建立视觉上下文后，动作轨迹从噪声 $\hat a_t\sim\mathcal{N}(0,I)$ 初始化。在 $N_a$ 个数值积分步中，动作 DiT 以所提取的生成特征 $h^{\tau_f}$ 和机器人本体感知状态 $s$ 为条件，预测动作速度场。轨迹通过迭代逐步改进，最终得到精确的预测动作 $\hat a_t$。

### Algorithm 2. DiT4DiT Inference / DiT4DiT 推理

> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> **Algorithm 2: DiT4DiT Inference**
>
> **Require:** Observation $o_t$, state $s$, language goal $l$
>
> **Require:** $N_v$: video sampling steps, $N_a$: action sampling steps
>
> **Ensure:** Predicted action $\hat a_t$, predicted future frame $\hat o_{t+1}$
>
> 1: <code>// ===== Video DiT Sampling =====</code>
>
> 2: $z_t^0\leftarrow\operatorname{VAE}_{\mathrm{enc}}(o_t)$
>
> 3: $\hat z_{t+1}\sim\mathcal{N}(0,I)$ $\triangleright$ Initialize from noise
>
> 4: $\Delta\tau_v\leftarrow1/N_v$
>
> 5: **for** $i=0,1,\ldots,N_v-1$ **do**
>
> 6: $\quad\tau_v\leftarrow1-i\cdot\Delta\tau_v$
>
> 7: $\quad\hat v\leftarrow v_{\mathrm{video}}(\hat z_{t+1},\tau_v\mid z_t^0,l)$
>
> 8: $\quad\hat z_{t+1}\leftarrow\hat z_{t+1}-\Delta\tau_v\cdot\hat v$ $\triangleright$ Euler step backward
>
> 9: **end for**
>
> 10: $\hat o_{t+1}\leftarrow\operatorname{VAE}_{\mathrm{dec}}(\hat z_{t+1})$
>
> 11: <code>// ===== Action DiT Sampling =====</code>
>
> 12: $\hat a_t\sim\mathcal{N}(0,I)$ $\triangleright$ Initialize from noise
>
> 13: $\hat z_{t+1}\sim\mathcal{N}(0,I)$ $\triangleright$ Initialize from noise
>
> 14: $h^{\tau_f}\leftarrow H(\theta,\hat z_{t+1},\tau_f,z_t^0,l)$ $\triangleright$ Extract hidden states
>
> 15: $\Delta\tau\leftarrow1/N_a$
>
> 16: **for** $i=0,1,\ldots,N_a-1$ **do**
>
> 17: $\quad\tau_a\leftarrow1-i\cdot\Delta\tau_a$
>
> 18: $\quad\hat v\leftarrow v_{\mathrm{action}}(\hat a_t,\tau_a\mid h_t^{\tau_f},s)$
>
> 19: $\quad\hat a_t\leftarrow\hat a_t-\Delta\tau\cdot\hat v$ $\triangleright$ Euler step backward
>
> 20: **end for**
>
> 21: **return** $\hat a_t,\hat o_{t+1}$

> <span style="color:#F59E0B"><strong>Para. 24[CN]:</strong></span> **算法 2：DiT4DiT 推理**
>
> **输入要求：** 观测 $o_t$、状态 $s$、语言目标 $l$
>
> **输入要求：** $N_v$：视频采样步数，$N_a$：动作采样步数
>
> **输出保证：** 预测动作 $\hat a_t$、预测未来帧 $\hat o_{t+1}$
>
> 1: <code>// ===== 视频 DiT 采样 =====</code>
>
> 2: $z_t^0\leftarrow\operatorname{VAE}_{\mathrm{enc}}(o_t)$
>
> 3: $\hat z_{t+1}\sim\mathcal{N}(0,I)$ $\triangleright$ 从噪声初始化
>
> 4: $\Delta\tau_v\leftarrow1/N_v$
>
> 5: **对于** $i=0,1,\ldots,N_v-1$ **执行**
>
> 6: $\quad\tau_v\leftarrow1-i\cdot\Delta\tau_v$
>
> 7: $\quad\hat v\leftarrow v_{\mathrm{video}}(\hat z_{t+1},\tau_v\mid z_t^0,l)$
>
> 8: $\quad\hat z_{t+1}\leftarrow\hat z_{t+1}-\Delta\tau_v\cdot\hat v$ $\triangleright$ Euler 反向步进
>
> 9: **结束循环**
>
> 10: $\hat o_{t+1}\leftarrow\operatorname{VAE}_{\mathrm{dec}}(\hat z_{t+1})$
>
> 11: <code>// ===== 动作 DiT 采样 =====</code>
>
> 12: $\hat a_t\sim\mathcal{N}(0,I)$ $\triangleright$ 从噪声初始化
>
> 13: $\hat z_{t+1}\sim\mathcal{N}(0,I)$ $\triangleright$ 从噪声初始化
>
> 14: $h^{\tau_f}\leftarrow H(\theta,\hat z_{t+1},\tau_f,z_t^0,l)$ $\triangleright$ 提取隐藏状态
>
> 15: $\Delta\tau\leftarrow1/N_a$
>
> 16: **对于** $i=0,1,\ldots,N_a-1$ **执行**
>
> 17: $\quad\tau_a\leftarrow1-i\cdot\Delta\tau_a$
>
> 18: $\quad\hat v\leftarrow v_{\mathrm{action}}(\hat a_t,\tau_a\mid h_t^{\tau_f},s)$
>
> 19: $\quad\hat a_t\leftarrow\hat a_t-\Delta\tau\cdot\hat v$ $\triangleright$ Euler 反向步进
>
> 20: **结束循环**
>
> 21: **返回** $\hat a_t,\hat o_{t+1}$

**Caption:** Algorithm 2: DiT4DiT Inference

**Caption[CN]:** 算法 2：DiT4DiT 推理


# 5. Experiments / 实验

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We evaluate DiT4DiT to address three primary questions: (1) how DiT4DiT compares with state-of-the-art VLM-based policies in both simulation and real-world deployment; (2) whether a VAM with a video-generative backbone offers advantages over a parameter-matched VLM-based VLA baseline; and (3) how well DiT4DiT generalizes under distribution shifts. To answer these questions, we conduct a comprehensive experimental suite covering benchmark comparison, real-world evaluation, zero-shot generalization, and ablation/efficiency analysis across different tasks and robot embodiments.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们评估 DiT4DiT，以回答三个主要问题：（1）在仿真和真实世界部署中，DiT4DiT 与最先进的基于 VLM 的策略相比表现如何；（2）采用视频生成骨干网络的 VAM 是否优于参数量匹配、基于 VLM 的 VLA 基线；以及（3）DiT4DiT 在分布偏移下的泛化能力如何。为回答这些问题，我们开展了一套全面的实验，涵盖基准比较、真实世界评估、零样本泛化，以及跨不同任务和机器人本体的消融/效率分析。

## 5.1 Experiment Setup / 实验设置

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **LIBERO benchmark.** LIBERO benchmark (Liu et al., 2024) focuses on manipulation tasks performed by a Franka Emika Panda manipulator. The evaluation spans four distinct suites—LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-Long—designed to systematically test a model’s proficiency in generalizing to novel spatial configurations, interacting with unseen objects, interpreting language instructions, and executing extended-horizon behaviors, respectively. The standard dataset for each category contains exactly 500 demonstration trajectories, distributed evenly across 10 unique tasks.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **LIBERO 基准。** LIBERO 基准（Liu et al., 2024）聚焦于由 Franka Emika Panda 机械臂执行的操作任务。评估涵盖四个不同的套件——LIBERO-Spatial、LIBERO-Object、LIBERO-Goal 和 LIBERO-Long——分别用于系统测试模型对新空间配置的泛化能力、与未见物体交互的能力、理解语言指令的能力，以及执行长时程行为的能力。每个类别的标准数据集都恰好包含 500 条演示轨迹，并均匀分布在 10 个不同任务上。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **RoboCasa-GR1 tabletop benchmark.** To further evaluate our approach on a more complex embodiment, we adopt the RoboCasa-GR1 tabletop benchmark (Bjorck et al., 2025; Nasiriany et al., 2024). Built upon the RoboCasa simulation framework, this benchmark features the Fourier GR1 humanoid robot equipped with two 7-DoF arms, two 6-DoF Fourier dexterous hands, and a 3-DoF waist, resulting in a 29-dimensional action space. For visual observations, our policy relies exclusively on the robot’s egocentric (ego-view) camera. The suite encompasses 24 distinct household manipulation tasks, designed to assess a policy’s ability to handle diverse activities ranging from articulated object interaction (e.g., opening microwaves or cabinets) to complex pick-and-place behaviors with novel objects. The standard dataset provides an extensive collection of teleoperated demonstrations, supplying exactly 1,000 human-collected trajectories for each of the 24 tasks. During evaluation, each task is tested over 50 rollouts with a maximum episode horizon of 720 environment steps. We report the average success rate (%) across rollouts for each task and the overall average across all 24 tasks.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **RoboCasa-GR1 桌面基准。** 为了在更复杂的机器人本体上进一步评估我们的方法，我们采用 RoboCasa-GR1 桌面基准（Bjorck et al., 2025; Nasiriany et al., 2024）。该基准构建于 RoboCasa 仿真框架之上，使用 Fourier GR1 人形机器人；该机器人配备两条 7-DoF 手臂、两只 6-DoF Fourier 灵巧手和一个 3-DoF 腰部，从而形成 29 维动作空间。对于视觉观测，我们的策略完全依赖机器人的第一人称（ego-view）相机。该套件包含 24 个不同的家庭操作任务，旨在评估策略处理多样活动的能力，这些活动从关节物体交互（例如打开微波炉或橱柜）到使用新物体执行复杂的抓取放置行为。标准数据集提供了大量遥操作演示，为 24 个任务中的每一个都恰好提供 1,000 条人类采集的轨迹。在评估期间，每个任务测试 50 次 rollout，最大 episode horizon 为 720 个环境步。我们报告每个任务在各次 rollout 上的平均成功率（%），以及全部 24 个任务的总体平均值。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Real-world G1 tasks.** To validate the real-world applicability of our approach, we deploy our policy on a Unitree G1 humanoid robot. The robotic system features a continuous 16-DoF action space, driven by two 7-DoF arms and ALOHA2 grippers, and relies exclusively on the robot’s egocentric (ego-view) camera for visual observations. To comprehensively assess the model’s robustness across diverse physical interactions and spatial reasoning challenges, we construct a benchmark suite comprising seven distinct household manipulation tasks. As illustrated in Fig. 4, these include: pick and place, arrange the flower, stack up the cups, insert plate into the rack, box packaging, move the spoon, and drawer interaction. For each task, we collected a dataset of exactly 200 human demonstration episodes. During the evaluation phase, performance is measured over 20 independent real-world rollouts per task, with the success rate reported as the primary metric.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **真实世界 G1 任务。** 为验证我们的方法在真实世界中的适用性，我们将策略部署到 Unitree G1 人形机器人上。该机器人系统具有连续的 16-DoF 动作空间，由两条 7-DoF 手臂和 ALOHA2 夹爪驱动，并且视觉观测完全依赖机器人的第一人称（ego-view）相机。为了全面评估模型面对多样物理交互和空间推理挑战时的鲁棒性，我们构建了一个包含七个不同家庭操作任务的基准套件。如图 4 所示，这些任务包括：pick and place、arrange the flower、stack up the cups、insert plate into the rack、box packaging、move the spoon 和 drawer interaction。对于每个任务，我们都采集了一个恰好包含 200 个真人演示 episode 的数据集。在评估阶段，每个任务通过 20 次相互独立的真实世界 rollout 衡量性能，并将成功率作为主要指标报告。

#### Figure 4. Real-world evaluation suite / 真实世界评估套件

![Figure 4](<file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_009_fig_figure_4.png>)

**Caption:** Figure 4: Real-world evaluation suite on the Unitree G1 humanoid robot. The selected tasks evaluate distinct dimensions of robotic proficiency, ranging from high-precision spatial manipulation (e.g., stack up the cups, insert plate into the rack, arrange the flower) to complex, extended-horizon execution (e.g., box packing, drawer interaction).

**Caption[CN]:** 图 4：Unitree G1 人形机器人上的真实世界评估套件。所选任务评估机器人能力的不同维度，范围从高精度空间操作（例如叠杯、将盘子插入架子、插花）到复杂的长时程执行（例如装箱、抽屉交互）。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Policy Setup and Baselines.** To rigorously evaluate the proposed DiT4DiT framework, we benchmark it against a diverse set of state-of-the-art policies, primarily focusing on the established GR00T series (Bjorck et al., 2025; NVIDIA et al., 2025b) and a custom, parameter-matched baseline denoted as Qwen3DiT. This baseline method combines Qwen3-VL (Bai et al., 2025) 2B foundation model with the same action DiT used in DiT4DiT.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **策略设置与基线。** 为了严格评估所提出的 DiT4DiT 框架，我们将其与多种最先进的策略进行基准比较，主要聚焦于成熟的 GR00T 系列（Bjorck et al., 2025; NVIDIA et al., 2025b）以及一个名为 Qwen3DiT 的自定义参数量匹配基线。该基线方法将 Qwen3-VL（Bai et al., 2025）2B 基础模型与 DiT4DiT 中使用的同一个 action DiT 相结合。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> For the simulated experiments, we train both DiT4DiT and Qwen3DiT entirely from scratch. This guarantees a strictly fair comparison of their inherent architectural efficiency and learning capabilities, while the remaining external baselines are evaluated using their official open-sourced pre-trained weights.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 对于仿真实验，我们将 DiT4DiT 和 Qwen3DiT 都完全从头训练。这保证了对两者内在架构效率和学习能力的严格公平比较，而其余外部基线则使用其官方开源的预训练权重进行评估。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> For the real-world experiments, we employ a two-stage training pipeline. DiT4DiT is first pre-trained on a subset of the simulated GR1 dataset (Bjorck et al., 2025), comprising 241,450 episodes, to acquire fundamental spatiotemporal priors, followed by fine-tuning on the teleoperated real-world G1 demonstrations. Under this setting, we compare our approach against GR00T-N1.5 (Bjorck et al., 2025) and Qwen3DiT. To provide a stringent ablation, Qwen3DiT is subjected to the exact same pre-training and fine-tuning pipeline as DiT4DiT. In contrast, GR00T-N1.5 is initialized from its official pre-trained weights, benefiting from a significantly larger scale of prior data before being fine-tuned on our target real-world tasks. Specifically, our pre-training data volume is merely $\sim$15% of the scale of training data leveraged by the official GR00T-N1.5 model.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 对于真实世界实验，我们采用两阶段训练流程。DiT4DiT 首先在仿真 GR1 数据集（Bjorck et al., 2025）的一个子集上进行预训练，该子集包含 241,450 个 episode，用于获取基础时空先验；随后在遥操作的真实世界 G1 演示上进行微调。在此设置下，我们将本方法与 GR00T-N1.5（Bjorck et al., 2025）和 Qwen3DiT 进行比较。为了提供严格的消融，Qwen3DiT 接受与 DiT4DiT 完全相同的预训练和微调流程。相比之下，GR00T-N1.5 从其官方预训练权重初始化，在我们的目标真实世界任务上微调之前，受益于规模显著更大的先验数据。具体而言，我们的预训练数据量仅约为官方 GR00T-N1.5 模型所用训练数据规模的 $\sim$15%。

## 5.2 Comparison Against State-of-the-Art Policies / 与最先进策略的比较

#### Table 1. LIBERO simulation benchmark / LIBERO 仿真基准

![Table 1](<file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_010_fig_table_1.png>)

**Caption:** Table 1: Success rates (%) on the four evaluation suites of the LIBERO simulation benchmark. Bold numbers indicate the highest performance in each category. In this context, from scratch implies that the model was trained without using any action data outside of the current benchmark.

**Caption[CN]:** 表 1：LIBERO 仿真基准四个评估套件上的成功率（%）。粗体数字表示各类别中的最高性能。在此语境中，from scratch 表示模型训练时未使用当前基准之外的任何动作数据。

| Method | Spatial SR (%) | Object SR (%) | Goal SR (%) | Long SR (%) | Average SR (%) |
|---|---:|---:|---:|---:|---:|
| Diffusion Policy (Chi et al., 2023) | 78.3 | 92.5 | 68.3 | 50.5 | 72.4 |
| Dita (Hou et al., 2025) | 97.4 | 94.8 | 93.2 | 83.6 | 92.3 |
| $\pi_0$ (Black et al., 2024) | 96.8 | 98.8 | 95.8 | 85.2 | 94.2 |
| UniVLA (Bu et al., 2025) | 96.5 | 96.8 | 95.6 | 92.0 | 95.2 |
| $\pi_{0.5}$ (Intelligence et al., 2025b) | **98.8** | 98.2 | 98.0 | 92.4 | 96.9 |
| OpenVLA-OFT (Kim et al., 2025) | 97.6 | 98.4 | 97.9 | 94.5 | 97.1 |
| CogVLA (Li et al., 2025b) | 98.6 | 98.8 | 96.6 | 95.4 | 97.4 |
| GR00T-N1.5 (Bjorck et al., 2025) | 96.2 | 94.0 | 96.0 | 90.0 | 94.1 |
| Qwen3DiT (from scratch) | 98.0 | 98.8 | 96.0 | 93.6 | 96.6 |
| DiT4DiT (from scratch) | 98.4 | **99.6** | **98.6** | **97.6** | **98.6** |

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> **LIBERO benchmark results.** Table 1 presents the quantitative evaluation of our method alongside state-of-the-art baselines on the LIBERO (Liu et al., 2024) simulation benchmark. Overall, our proposed DiT4DiT trained from scratch achieves a new state-of-the-art average success rate of 98.6%, outperforming previous VLA models pre-trained in large-scale action datasets.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **LIBERO 基准结果。** 表 1 给出了我们的方法与最先进基线在 LIBERO（Liu et al., 2024）仿真基准上的定量评估。总体而言，我们提出的、从头训练的 DiT4DiT 取得了新的最先进平均成功率 98.6%，优于此前在大规模动作数据集上预训练的 VLA 模型。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> When analyzing the distinct suites, DiT4DiT demonstrates exceptional generalization capabilities across novel objects and language instructions, achieving the highest success rates in the LIBERO-Object (99.6%) and LIBERO-Goal (98.6%) suites. Furthermore, our method exhibits a particularly striking advantage on the LIBERO-Long suite, which evaluates extended-horizon behaviors. DiT4DiT attains a 97.6% success rate on this challenging suite, significantly surpassing the next best method. This robust long-horizon performance strongly validates our design choice: by explicitly modeling the spatiotemporal dynamics through the video DiT backbone, our policy gains a deeper understanding of physical state transitions, which is crucial for executing complex, multi-stage manipulation tasks. Finally, compared to our direct baseline, Qwen3DiT (96.6% average), DiT4DiT yields consistent improvements across all four categories, confirming that our decoupled generative inverse dynamics and feature extraction mechanism successfully translate rich video priors into precise robotic control.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 分析各个不同套件时，DiT4DiT 在新物体和语言指令方面展现出卓越的泛化能力，在 LIBERO-Object（99.6%）和 LIBERO-Goal（98.6%）套件上取得最高成功率。此外，我们的方法在评估长时程行为的 LIBERO-Long 套件上表现出尤为显著的优势。DiT4DiT 在这一高难度套件上达到 97.6% 的成功率，显著超过次优方法。这种稳健的长时程性能有力验证了我们的设计选择：通过借助 video DiT 骨干网络显式建模时空动力学，我们的策略能够更深入地理解物理状态转移，而这对于执行复杂的多阶段操作任务至关重要。最后，与直接基线 Qwen3DiT（平均 96.6%）相比，DiT4DiT 在全部四个类别上都取得了一致提升，这证实我们解耦的生成式逆动力学与特征提取机制成功地将丰富的视频先验转化为精确的机器人控制。

#### Table 2. RoboCasa-GR1 tabletop tasks / RoboCasa-GR1 桌面任务

![Table 2](<file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_011_fig_table_2.png>)

**Caption:** Table 2: RoboCasa-GR1 tabletop tasks evaluation results (success rate (%)). Bold numbers indicate the highest performance in each category. from scratch implies that the model was trained without using any action data outside of the current benchmark. While the GR00T models are fine-tuned from their pre-trained weights, they are trained for the exact same number of steps as Qwen3DiT and DiT4DiT, which are trained from scratch.

**Caption[CN]:** 表 2：RoboCasa-GR1 桌面任务评估结果（成功率（%））。粗体数字表示各类别中的最高性能。from scratch 表示模型训练时未使用当前基准之外的任何动作数据。尽管 GR00T 模型从其预训练权重进行微调，但它们与从头训练的 Qwen3DiT 和 DiT4DiT 使用完全相同的训练步数。

| Task | GR00T-N1.5 (Bjorck et al., 2025) | GR00T-N1.6 (NVIDIA et al., 2025b) | Qwen3DiT (from scratch) | DiT4DiT (from scratch) |
|---|---:|---:|---:|---:|
| BottleToCabinetClose | 40.0 | 36.0 | **50.0** | 48.0 |
| CanToDrawerClose | 56.0 | 28.0 | 48.0 | **74.0** |
| CupToDrawerClose | 50.0 | 12.0 | 42.0 | **52.0** |
| MilkToMicrowaveClose | **52.0** | 20.0 | 38.0 | 50.0 |
| PotatoToMicrowaveClose | 22.0 | 28.0 | 18.0 | **36.0** |
| WineToCabinetClose | **44.0** | 18.0 | 28.0 | 42.0 |
| FromCuttingboardToBasket | 46.0 | 42.0 | 42.0 | **52.0** |
| FromCuttingboardToCardboardbox | 44.0 | 40.0 | 30.0 | **48.0** |
| FromCuttingboardToPan | 58.0 | 62.0 | 50.0 | **76.0** |
| FromCuttingboardToPot | 48.0 | 60.0 | 44.0 | **62.0** |
| FromCuttingboardToTieredbasket | 28.0 | 48.0 | 36.0 | **50.0** |
| FromPlacematToBasket | 32.0 | 42.0 | 14.0 | **50.0** |
| FromPlacematToBowl | 52.0 | 34.0 | 28.0 | **56.0** |
| FromPlacematToPlate | **42.0** | **42.0** | 40.0 | 32.0 |
| FromPlacematToTieredshelf | 26.0 | 24.0 | **30.0** | 18.0 |
| FromPlateToBowl | 38.0 | 48.0 | 36.0 | **56.0** |
| FromPlateToCardboardbox | 40.0 | 44.0 | 36.0 | **58.0** |
| FromPlateToPan | 56.0 | 48.0 | 34.0 | **68.0** |
| FromPlateToPlate | 50.0 | **66.0** | 44.0 | 58.0 |
| FromTrayToCardboardbox | 36.0 | 42.0 | **48.0** | 38.0 |
| FromTrayToPlate | 54.0 | 52.0 | 44.0 | **56.0** |
| FromTrayToPot | 36.0 | **64.0** | 34.0 | 54.0 |
| FromTrayToTieredbasket | 34.0 | 42.0 | 36.0 | **46.0** |
| FromTrayToTieredshelf | 22.0 | **38.0** | 18.0 | **38.0** |
| Average | 41.8 | 40.8 | 36.2 | **50.8** |

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> **RoboCasa-GR1 tabletop benchmark results.** We evaluate on 24 challenging manipulation tasks from the RoboCasa-GR1 tabletop suite (Nasiriany et al., 2024). As summarized in Table 2, DiT4DiT achieves a new state-of-the-art average success rate of 50.8%. This significantly outperforms established, highly optimized policies, exceeding GR00T-N1.5 and GR00T-N1.6 by a substantial margin of 9.0 and 10.0 absolute percentage points, respectively.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> **RoboCasa-GR1 桌面基准结果。** 我们在 RoboCasa-GR1 桌面套件（Nasiriany et al., 2024）的 24 个高难度操作任务上进行评估。如表 2 所示，DiT4DiT 取得了新的最先进平均成功率 50.8%。这一结果显著优于已有的高度优化策略，分别以 9.0 和 10.0 个绝对百分点的大幅优势超过 GR00T-N1.5 和 GR00T-N1.6。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> Crucially, we compare DiT4DiT against our parameter-matched direct baseline, Qwen3DiT (36.2%). DiT4DiT demonstrates a remarkable 14.6% absolute improvement over Qwen3DiT. This substantial leap strongly validates our core hypothesis: substituting static image-text priors with the implicit spatiotemporal dynamics of a generative video model provides a superior conditioning signal for learning complex inverse dynamics.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> 关键的是，我们将 DiT4DiT 与参数量匹配的直接基线 Qwen3DiT（36.2%）进行比较。DiT4DiT 相比 Qwen3DiT 实现了显著的 14.6% 绝对提升。这一大幅跃升有力验证了我们的核心假设：用生成式视频模型的隐式时空动力学取代静态图文先验，能够为学习复杂逆动力学提供更优的条件信号。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> Examining individual tasks, DiT4DiT exhibits dominant performance, achieving the highest success rate in 16 out of the 24 evaluated tasks. The performance gains are particularly pronounced in tasks demanding precise spatial coordination and complex physical interaction. For instance, on CanToDrawerClose (74.0% vs. 56.0%), FromCuttingboardToPan (76.0% vs. 62.0%), and FromPlateToPan (68.0% vs. 56.0%), our method eclipses the strongest baselines by margins exceeding 12%.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 考察各个任务时，DiT4DiT 展现出主导性表现，在所评估的 24 个任务中有 16 个取得最高成功率。在要求精确空间协调和复杂物理交互的任务中，性能增益尤其明显。例如，在 CanToDrawerClose（74.0% vs. 56.0%）、FromCuttingboardToPan（76.0% vs. 62.0%）和 FromPlateToPan（68.0% vs. 56.0%）上，我们的方法以超过 12% 的优势超越最强基线。

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> **Real-world G1 task results.** We report the quantitative success rates across the seven real-world tasks in Fig. 5. Overall, DiT4DiT demonstrates dominant and robust performance, comprehensively outperforming both the pre-trained GR00T-N1.5 (Bjorck et al., 2025) and our baseline, Qwen3DiT.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> **真实世界 G1 任务结果。** 我们在图 5 中报告七个真实世界任务的定量成功率。总体而言，DiT4DiT 展现出占主导且稳健的性能，全面优于预训练的 GR00T-N1.5（Bjorck et al., 2025）和我们的基线 Qwen3DiT。

#### Figure 5. Real-world evaluation results / 真实世界评估结果

![Figure 5](<file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_012_fig_figure_5.png>)

**Caption:** Figure 5: Real-world evaluation results on the Unitree G1 robot. Success rates are reported across seven diverse household tasks. DiT4DiT comprehensively outperforms both the pre-trained GR00T-N1.5 (Bjorck et al., 2025) and the parameter-matched Qwen3DiT baseline, highlighting the efficiency and efficacy of our framework.

**Caption[CN]:** 图 5：Unitree G1 机器人上的真实世界评估结果。报告了七个多样化家庭任务的成功率。DiT4DiT 全面优于预训练的 GR00T-N1.5（Bjorck et al., 2025）和参数量匹配的 Qwen3DiT 基线，突显了我们框架的效率与有效性。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> The Qwen3DiT baseline suffers a near-total collapse in the real world. It fails to exceed a 10% success rate on any task and scores 0% on Drawer Interaction, Arrange Flower, and Box Packing. This failure underscores the limitation of static image-text priors: without massive real-world trajectory data, VLMs struggle to ground visual semantics into continuous 3D physical actions. In stark contrast, DiT4DiT successfully abstracts robust, physics-aware representations from the simulated pre-training phase, enabling highly effective transfer to the physical robot.

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> Qwen3DiT 基线在真实世界中几乎完全崩溃。它在任何任务上的成功率都未能超过 10%，并且在 Drawer Interaction、Arrange Flower 和 Box Packing 上得分为 0%。这一失败凸显了静态图文先验的局限：在缺乏海量真实世界轨迹数据时，VLM 难以将视觉语义落地为连续的 3D 物理动作。与此形成鲜明对比的是，DiT4DiT 成功地从仿真预训练阶段抽象出稳健、具备物理感知能力的表征，从而实现向实体机器人的高效迁移。

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> When compared against GR00T-N1.5 (which benefits from a significantly larger scale of pre-training data), DiT4DiT still maintains a consistent lead, with particularly massive margins in tasks demanding high-precision spatial coordination. For example, in the Arrange Flower task, which requires delicate alignment to insert a thin stem into a vase, DiT4DiT achieves a 75% success rate, outperforming GR00T-N1.5 (25%). We observe similarly compelling gaps in Stack Cup (60% vs. 25%) and Move Spoon (40% vs. 15%). We hypothesize that the generative video backbone, by learning to predict future visual representations, inherently preserves more fine-grained visual details than standard VLA policy.

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> 与 GR00T-N1.5（其受益于规模显著更大的预训练数据）相比，DiT4DiT 仍然保持一致领先，并且在要求高精度空间协调的任务中优势尤其巨大。例如，在需要精细对准、将细茎插入花瓶的 Arrange Flower 任务中，DiT4DiT 达到 75% 的成功率，优于 GR00T-N1.5（25%）。我们在 Stack Cup（60% vs. 25%）和 Move Spoon（40% vs. 15%）中也观察到同样显著的差距。我们推测，生成式视频骨干网络通过学习预测未来视觉表征，相较标准 VLA 策略会内在地保留更细粒度的视觉细节。

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> Furthermore, DiT4DiT excels in extended-horizon and multi-stage reasoning tasks. On Drawer Interaction and Box Packing, which require the robot to sequence multiple distinct sub-goals (e.g., opening a flap, inserting an object, and retreating), DiT4DiT achieves 90% and 50% success rates, respectively. By intercepting intermediate denoising features that naturally encode future dynamic transitions, our tri-timestep mechanism equips the action policy with superior temporal consistency, ensuring stable execution over long physical horizons.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> 此外，DiT4DiT 在长时程和多阶段推理任务中表现出色。在 Drawer Interaction 和 Box Packing 上，机器人需要依序完成多个不同的子目标（例如打开翻盖、插入物体并后退），DiT4DiT 分别取得 90% 和 50% 的成功率。通过截取自然编码未来动态转移的中间去噪特征，我们的三时间步机制赋予动作策略更优的时间一致性，确保在很长的物理时域内稳定执行。

## 5.3 Generalization Capability / 泛化能力

#### Figure 6. Qualitative real-world generalization rollouts / 真实世界泛化定性 rollout

![Figure 6](<file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_012_fig_figure_6.png>)

**Caption:** Figure 6: Qualitative rollouts of real-world generalization tasks. We evaluate the policy’s zero-shot robustness against severe out-of-distribution physical variations. These include semantic and geometric shifts in Category (unseen cups and vases), complete object substitution in Object (packing corn instead of an eggplant), and scene clutter in Number (stacking four cups instead of three).

**Caption[CN]:** 图 6：真实世界泛化任务的定性 rollout。我们评估策略面对严重分布外物理变化时的零样本鲁棒性。这些变化包括 Category 中的语义与几何偏移（未见过的杯子和花瓶）、Object 中的完整物体替换（装入玉米而非茄子），以及 Number 中的场景杂乱（堆叠四个杯子而非三个）。

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> We evaluate DiT4DiT in both simulation and real-world physical deployments to demonstrate its robust generalization.

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> 我们在仿真和真实世界物理部署中评估 DiT4DiT，以证明其稳健的泛化能力。

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> In the simulator, we designed a targeted object-substitution experiment within the RoboCasa (Nasiriany et al., 2024) environment. Specifically, we restricted the training distribution to three tasks involving only a single object category: BottleToDrawerClose, BottleToCabinetClose, and BottleToMicrowaveClose. During evaluation, we completely removed the bottle and tested the policies zero-shot on four unseen objects: Can, Cup, Milk, and Wine. DiT4DiT exhibits a remarkably stronger ability to generalize to novel objects compared to the parameter-matched Qwen3DiT baseline, as shown in the left panel of Fig. 7. Across all three tasks, our approach maintains robust performance. Most notably, in the ToDrawerClose tasks, DiT4DiT achieves an impressive 54.5% success rate with the unseen objects, exceeding Qwen3DiT by a massive 22.5%. We observe similarly substantial margins in ToCabinetClose (34.0% vs. 24.5%) and ToMicrowaveClose (30.5% vs. 17.0%).

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> 在仿真器中，我们在 RoboCasa（Nasiriany et al., 2024）环境内设计了一个有针对性的物体替换实验。具体而言，我们将训练分布限制为只涉及单一物体类别的三个任务：BottleToDrawerClose、BottleToCabinetClose 和 BottleToMicrowaveClose。在评估期间，我们完全移除 bottle，并在四种未见物体 Can、Cup、Milk 和 Wine 上对策略进行零样本测试。如图 7 左图所示，与参数量匹配的 Qwen3DiT 基线相比，DiT4DiT 展现出显著更强的新物体泛化能力。在全部三个任务上，我们的方法都保持稳健性能。最值得注意的是，在 ToDrawerClose 任务中，DiT4DiT 面对未见物体时取得了令人瞩目的 54.5% 成功率，以 22.5% 的巨大优势超过 Qwen3DiT。我们在 ToCabinetClose（34.0% vs. 24.5%）和 ToMicrowaveClose（30.5% vs. 17.0%）中也观察到同样显著的优势。

#### Figure 7. Quantitative zero-shot generalization / 零样本泛化定量结果

![Figure 7](<file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_013_fig_figure_7.png>)

**Caption:** Figure 7: Quantitative results of zero-shot generalization. (Left) Success rates in the simulated RoboCasa-GR1 environment when evaluated on entirely unseen objects. (Right) Success rates on the real-world Unitree G1 robot across four challenging out-of-distribution scenarios, testing category variations, novel object substitutions, and distractor quantities. DiT4DiT demonstrates superior robustness and physical abstraction compared to both the parameter-matched Qwen3DiT baseline and the pre-trained GR00T-N1.5 (Bjorck et al., 2025).

**Caption[CN]:** 图 7：零样本泛化的定量结果。（左）在完全未见物体上评估时，仿真 RoboCasa-GR1 环境中的成功率。（右）真实世界 Unitree G1 机器人在四种高难度分布外场景中的成功率，测试类别变化、新物体替换和干扰物数量。与参数量匹配的 Qwen3DiT 基线和预训练的 GR00T-N1.5（Bjorck et al., 2025）相比，DiT4DiT 展现出更强的鲁棒性和物理抽象能力。

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> To further validate these findings under complex physical dynamics, we introduced four challenging zero-shot generalization scenarios on the real-world Unitree G1 robot (visualized in Fig. 6). These tasks evaluate three distinct dimensions of generalization:
>
> - **Category generalization:** In Stack Cup (Category) and Arrange Flower (Category), we drastically alter the material, shape, and visual appearance of the interactive objects (e.g., swapping standard plastic cups for metallic/glass variants, and changing both the vase and the flower).
> - **Object substitution:** In Box Packing (Object), the target item is completely replaced with a novel, out-of-distribution object (e.g., swapping an eggplant for corn).
> - **Quantity variation:** In Stack Cup (Number), we test whether the policy can handle a different number of objects than seen during training, evaluating its resistance to distractors and novel scene clutter.

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> 为了在复杂物理动力学下进一步验证这些发现，我们在真实世界 Unitree G1 机器人上引入了四种高难度零样本泛化场景（见图 6）。这些任务评估三个不同的泛化维度：
>
> - **类别泛化：** 在 Stack Cup (Category) 和 Arrange Flower (Category) 中，我们大幅改变交互物体的材质、形状和视觉外观（例如，将标准塑料杯换成金属/玻璃变体，并同时更换花瓶和花）。
> - **物体替换：** 在 Box Packing (Object) 中，目标物品被一种新的分布外物体完全替换（例如，将茄子换成玉米）。
> - **数量变化：** 在 Stack Cup (Number) 中，我们测试策略能否处理与训练期间所见数量不同的物体，以评估其抵抗干扰物和新场景杂乱的能力。

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> As shown in the right panel of Fig. 7, DiT4DiT demonstrates dominant zero-shot transfer capabilities in the physical world. The performance of the parameter-matched Qwen3DiT baseline completely collapses when faced with real-world visual shifts, scoring 0% on three out of the four tasks. In contrast, DiT4DiT successfully abstracts the underlying physical interactions, such as the spatial constraints of inserting a stem into a vase or aligning cups. Notably, on the Arrange Flower (Category) task, DiT4DiT achieves a 70% success rate, outperforming the Qwen3DiT (0%) the pre-trained GR00T-N1.5 (10%) by large margins. Even when modifying the quantity of objects in Stack Cup (Number), DiT4DiT maintains a 50% success rate, proving that the generative video representations provide a robust, physics-aware understanding of the scene that is fundamentally invariant to surface-level visual changes or distractor counts.

> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> 如图 7 右图所示，DiT4DiT 在物理世界中展现出占主导的零样本迁移能力。参数量匹配的 Qwen3DiT 基线在面对真实世界视觉偏移时性能完全崩溃，在四个任务中的三个上得分为 0%。相比之下，DiT4DiT 成功抽象出底层物理交互，例如将花茎插入花瓶或对齐杯子时的空间约束。值得注意的是，在 Arrange Flower (Category) 任务中，DiT4DiT 取得 70% 的成功率，以巨大优势超过 Qwen3DiT（0%）和预训练的 GR00T-N1.5（10%）。即使改变 Stack Cup (Number) 中的物体数量，DiT4DiT 仍保持 50% 的成功率，这证明生成式视频表征能够提供一种稳健、具备物理感知能力的场景理解，并且这种理解从根本上不受表层视觉变化或干扰物数量影响。

## 5.4 Ablations / 消融实验

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> **Choice of feature extraction layer.** To determine the optimal visual representation for action conditioning, we evaluate the impact of extracting hidden states from different transformer blocks within the Video DiT. We conduct our experiments on five tasks selected from the RoboCasa-GR1 benchmark (CanToDrawerClose, FromCuttingboardToBasket, FromPlacematToBowl, FromPlateToCardboardbox, FromTrayToPot). As illustrated in Figure 8(a), the choice of extraction layer significantly influences the downstream success rate. Features from early layers (e.g., layers 2–8) yield poor performance, likely because they primarily encode low-level visual textures lacking actionable semantics. Performance steadily improves and peaks at layer 18, suggesting that middle-to-deep blocks strike the optimal balance, capturing the rich spatiotemporal physics and high-level scene understanding required for control. Interestingly, extracting from the final layers (layers 24–28) leads to a drastic performance collapse. The result suggests these terminal layers become overly specialized for the immediate video denoising and pixel-level reconstruction objective, thereby discarding abstract, control-relevant representations. Finally, while averaging features across all layers (“all”) yields highly competitive results, it falls slightly short of the single best layer. Consequently, we select layer 18 as the default extraction point for our framework.

> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> **特征提取层的选择。** 为了确定用于动作条件化的最优视觉表征，我们评估了从 Video DiT 内不同 transformer block 提取隐藏状态所产生的影响。我们在从 RoboCasa-GR1 基准中选出的五个任务上开展实验（CanToDrawerClose、FromCuttingboardToBasket、FromPlacematToBowl、FromPlateToCardboardbox、FromTrayToPot）。如图 8(a) 所示，提取层的选择会显著影响下游成功率。来自早期层（例如第 2–8 层）的特征表现较差，可能是因为它们主要编码缺乏可行动语义的低层视觉纹理。性能随后稳定提升，并在第 18 层达到峰值，这表明中层到深层 block 实现了最优平衡，能够捕获控制所需的丰富时空物理信息和高层场景理解。有趣的是，从最后几层（第 24–28 层）提取特征会导致性能急剧崩溃。该结果表明，这些末端层对即时视频去噪和像素级重建目标变得过度专门化，从而丢弃了抽象的控制相关表征。最后，尽管对所有层（“all”）的特征取平均能够获得极具竞争力的结果，但仍略逊于单个最优层。因此，我们选择第 18 层作为框架的默认提取点。

#### Figure 8. DiT4DiT architectural ablations / DiT4DiT 架构消融

![Figure 8](<file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_014_fig_figure_8.png>)

**Caption:** Figure 8: Ablation studies on the DiT4DiT architecture. (a) Feature extraction layer: Success rate across different hidden layers of the video backbone, with performance peaking at layer 18. (b) Denoising steps: Impact of the number of iterative denoising steps used for action conditioning. A single forward step yields the highest success rate, preventing over-commitment to pixel-level reconstruction. (c) Representation learning: t-SNE visualization of latent features colored by the execution phase (Early, Middle, Late). Supported by a roughly twofold increase in the silhouette score (Rousseeuw, 1987), our joint training objective successfully induces smooth temporal flows within each task cluster, transitioning fluidly from the Early (blue) through the Middle (yellow) to the Late (red) phases.

**Caption[CN]:** 图 8：DiT4DiT 架构的消融研究。(a) 特征提取层：视频骨干网络不同隐藏层上的成功率，性能在第 18 层达到峰值。(b) 去噪步数：用于动作条件化的迭代去噪步数所产生的影响。单次前向步获得最高成功率，避免对像素级重建过度投入。(c) 表征学习：按执行阶段（Early、Middle、Late）着色的潜在特征 t-SNE 可视化。轮廓系数（Rousseeuw, 1987）大约提升两倍，为此提供了支持；我们的联合训练目标成功地在每个任务簇内诱导出平滑的时间流，从 Early（蓝色）经 Middle（黄色）流畅过渡到 Late（红色）阶段。

> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> **Denoise steps for hidden features.** We investigate the impact of the number of iterative denoising steps used to extract the visual hidden features for the action policy. As shown in Figure 8(b), we evaluate the average success rate across the five selected RoboCasa tasks while varying the denoising steps from 1 to 32. Interestingly, a single denoising step yields the highest performance, with the success rate monotonically degrading as the number of steps increases. The reason could be that excessive iterative denoising forces the hidden states to over-commit to the pixel-level details of a specific reconstructed future. So generalized robust action priors start to lose information with more steps. This intuition aligns with findings in recent work (Pai et al., 2025), but this phenomenon is significantly more pronounced in our model, manifesting as a strict monotonic decline. We hypothesize that this extreme sensitivity is a direct consequence of our joint training paradigm: because the video and action generation are updated simultaneously, the action loss heavily regularizes the latent space to extract actionable semantics immediately at the first step, making it highly susceptible to the over-commitment of any subsequent denoising iterations. Crucially, this finding validates that high-frequency control can be achieved through a single forward pass, entirely bypassing the computational bottleneck of multi-step video generation.

> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> **隐藏特征的去噪步数。** 我们研究用于为动作策略提取视觉隐藏特征的迭代去噪步数所产生的影响。如图 8(b) 所示，我们在五个选定 RoboCasa 任务上评估平均成功率，同时将去噪步数从 1 改变到 32。有趣的是，单步去噪取得最高性能，并且成功率随步数增加而单调下降。原因可能在于，过度的迭代去噪迫使隐藏状态对某个特定重建未来的像素级细节投入过多。因此，随着步数增加，泛化且稳健的动作先验开始丢失信息。这一直觉与近期工作（Pai et al., 2025）的发现一致，但该现象在我们的模型中明显更加突出，表现为严格的单调下降。我们推测，这种极端敏感性是联合训练范式的直接后果：由于视频生成和动作生成同时更新，动作损失对潜在空间施加强正则化，使其在第一步就立即提取可行动语义，因此任何后续去噪迭代造成的过度投入都会对其产生很大影响。至关重要的是，这一发现验证了高频控制可以通过单次前向传播实现，从而完全绕过多步视频生成的计算瓶颈。

> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> **Joint v.s. decouple training.** Finally, we analyze the representational benefits of our joint optimization paradigm. Figure 8(c) provides a t-SNE visualization of the extracted hidden features, color-coded by their temporal phase within an episode (Early, Middle, Late). Under a decoupled training scheme, where the video generative model and the action policy are optimized independently, the features form clusters but exhibit fragmented and entangled temporal distributions within those clusters. Quantitatively, this enhanced temporal separation is reflected by a nearly twofold improvement in the silhouette score (increasing from 0.09 to 0.17). Visually, the latent features within each cluster exhibit relatively clear boundaries as they progress from the Early to Middle to Late phases. This qualitative evidence strongly corroborates our core hypothesis: joint training forces the visual backbone to embed a continuous, physics-aware temporal progression, directly empowering the action policy to reason about long-horizon execution and state transitions.

> <span style="color:#F59E0B"><strong>Para. 23[CN]:</strong></span> **联合训练 v.s. 解耦训练。** 最后，我们分析联合优化范式在表征方面的收益。图 8(c) 给出了所提取隐藏特征的 t-SNE 可视化，并按照它们在一个 episode 中的时间阶段（Early、Middle、Late）着色。在解耦训练方案下，视频生成模型和动作策略各自独立优化；特征虽然形成了簇，但在这些簇内呈现碎片化且相互纠缠的时间分布。定量而言，这种更强的时间分离表现为轮廓系数几乎提升两倍（从 0.09 增至 0.17）。从视觉上看，每个簇内的潜在特征在从 Early 向 Middle 再向 Late 阶段推进时，呈现出相对清晰的边界。这一定性证据有力支持了我们的核心假设：联合训练迫使视觉骨干网络嵌入连续、具备物理感知能力的时间进程，从而直接赋予动作策略对长时程执行和状态转移进行推理的能力。

## 5.5 Efficiency Analysis / 效率分析

> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> To assess deployment feasibility, we compare trainable parameter count and real-world control frequency against core baselines (Table 3). DiT4DiT has 2.2B trainable parameters, comparable to Qwen3DiT (2.3B) and smaller than GR00T-N1.5 (2.7B), indicating that its gains do not come from larger model size. DiT4DiT runs at 6Hz on the physical robot, versus 9Hz for Qwen3DiT and 13Hz for GR00T-N1.5. Although slower, this trade-off is expected for a video-generative backbone that extracts temporally grounded features. Unlike the two baselines, DiT4DiT does not train the LLM component during policy learning; therefore, for fixed tasks, the LLM features remain constant and can be pre-extracted and cached to avoid repeated inference, which can further improve the effective deployment frequency.

> <span style="color:#F59E0B"><strong>Para. 24[CN]:</strong></span> 为评估部署可行性，我们将可训练参数量和真实世界控制频率与核心基线进行比较（表 3）。DiT4DiT 有 2.2B 个可训练参数，与 Qwen3DiT（2.3B）相当，并且少于 GR00T-N1.5（2.7B），说明其增益并非来自更大的模型规模。DiT4DiT 在实体机器人上以 6Hz 运行，而 Qwen3DiT 为 9Hz、GR00T-N1.5 为 13Hz。尽管速度更慢，但对于一个要提取具有时间落地特征的视频生成骨干网络而言，这种权衡符合预期。与两个基线不同，DiT4DiT 在策略学习期间不训练 LLM 组件；因此，对于固定任务，LLM 特征保持不变，可以预先提取并缓存，以避免重复推理，从而还可进一步提高有效部署频率。

#### Table 3. Deployment efficiency comparison / 部署效率比较

![Table 3](<file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_015_fig_table_3.png>)

**Caption:** Table 3: Deployment efficiency comparison. We report the trainable parameter count and real-world deployment frequency (Hz) for DiT4DiT and the primary baselines. While the video backbone introduces a computational trade-off yielding a 6Hz control rate (tested on a single NVIDIA A100 GPU), DiT4DiT remains the most parameter-efficient model and comfortably supports real-time closed-loop physical execution.

**Caption[CN]:** 表 3：部署效率比较。我们报告 DiT4DiT 和主要基线的可训练参数量与真实世界部署频率（Hz）。尽管视频骨干网络带来了计算权衡，使控制速率为 6Hz（在单张 NVIDIA A100 GPU 上测试），DiT4DiT 仍然是参数效率最高的模型，并且能够从容支持实时闭环物理执行。

| Model | Trainable Param Cnt | Deploy Frequency |
|---|---:|---:|
| GR00T-N1.5 | 2.7B | 13Hz |
| Qwen3DiT | 2.3B | 9Hz |
| DiT4DiT | 2.2B | 6Hz |

# 6. Conclusion / 结论

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We present DiT4DiT, an end-to-end Video-Action Model that unifies a video DiT and an action DiT through a dual flow-matching objective. Instead of depending on fully reconstructed future frames, our method leverages temporally grounded intermediate denoising features to condition action prediction, enabling physics-aware and stable continuous control. Across both simulation and real-world experiments, DiT4DiT consistently outperforms strong VLA baselines. It achieves state-of-the-art average success rates on LIBERO and RoboCasa-GR1 (98.6% and 50.8%), and maintains strong transfer performance on the Unitree G1 humanoid robot under real-world dynamics. Beyond aggregate performance, DiT4DiT shows improved robustness under challenging distribution shifts, including unseen object categories and object/scene variations. Overall, our results indicate that modeling video dynamics provides a more effective and data-efficient scaling proxy for policy learning than static image-text priors, offering a practical path toward more generalizable embodied agents.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们提出 DiT4DiT，这是一种端到端 Video-Action Model，通过双 flow-matching 目标将 video DiT 与 action DiT 统一起来。我们的方法不依赖完全重建的未来帧，而是利用在时间上落地的中间去噪特征对动作预测进行条件化，从而实现具备物理感知能力且稳定的连续控制。在仿真和真实世界实验中，DiT4DiT 始终优于强大的 VLA 基线。它在 LIBERO 和 RoboCasa-GR1 上取得了最先进的平均成功率（98.6% 和 50.8%），并且在真实世界动力学条件下的 Unitree G1 人形机器人上保持强劲的迁移性能。除总体性能之外，DiT4DiT 在具有挑战性的分布偏移下表现出更强的鲁棒性，其中包括未见物体类别以及物体/场景变化。总体而言，我们的结果表明，相较静态图文先验，视频动力学建模为策略学习提供了一种更有效且数据效率更高的扩展代理，为构建泛化能力更强的具身智能体提供了一条切实可行的路径。

# References / 参考文献

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> To preserve exact author names, titles, venues, years, URLs, and arXiv identifiers for search and citation matching, all reference entries below are retained in their complete searchable English form and are not translated item by item.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 中文政策说明：为保证作者姓名、题名、出版物、年份、URL 与 arXiv 标识符能够被准确检索并与引文匹配，以下参考文献均保留为完整、可检索的英文条目，不逐条翻译。

1. Josh Achiam, Steven Adler, Sandhini Agarwal, Lama Ahmad, Ilge Akkaya, Florencia Leoni Aleman, Diogo Almeida, Janko Altenschmidt, Sam Altman, Shyamal Anadkat, et al. Gpt-4 technical report. arXiv preprint arXiv:2303.08774, 2023.

2. Jorge Aldaco, Travis Armstrong, Robert Baruch, Jeff Bingham, Sanky Chan, Kenneth Draper, Debidatta Dwibedi, Chelsea Finn, Pete Florence, Spencer Goodrich, et al. Aloha 2: An enhanced low-cost hardware for bimanual teleoperation. arXiv preprint arXiv:2405.02292, 2024.

3. Arslan Ali, Junjie Bai, Maciej Bala, Yogesh Balaji, Aaron Blakeman, Tiffany Cai, Jiaxin Cao, Tianshi Cao, Elizabeth Cha, Yu-Wei Chao, et al. World simulation with video foundation models for physical ai. arXiv preprint arXiv:2511.00062, 2025.

4. Alisson Azzolini, Junjie Bai, Hannah Brandon, Jiaxin Cao, Prithvijit Chattopadhyay, Huayu Chen, Jinju Chu, Yin Cui, Jenna Diamond, Yifan Ding, et al. Cosmos-reason1: From physical common sense to embodied reasoning. arXiv preprint arXiv:2503.15558, 2025.

5. Shuai Bai, Yuxuan Cai, Ruizhe Chen, Keqin Chen, Xionghui Chen, Zesen Cheng, Lianghao Deng, Wei Ding, Chang Gao, Chunjiang Ge, et al. Qwen3-vl technical report. arXiv preprint arXiv:2511.21631, 2025.

6. Hongzhe Bi, Hengkai Tan, Shenghao Xie, Zeyuan Wang, Shuhe Huang, Haitian Liu, Ruowen Zhao, Yao Feng, Chendong Xiang, Yinze Rong, et al. Motus: A unified latent action world model. arXiv preprint arXiv:2512.13030, 2025.

7. Johan Bjorck, Fernando Castañeda, Nikita Cherniadev, Xingye Da, Runyu Ding, Linxi Fan, Yu Fang, Dieter Fox, Fengyuan Hu, Spencer Huang, et al. Gr00t n1: An open foundation model for generalist humanoid robots. arXiv preprint arXiv:2503.14734, 2025.

8. Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, Lachy Groom, Karol Hausman, Brian Ichter, et al. pi0: A vision-language-action flow model for general robot control. arXiv preprint arXiv:2410.24164, 2024.

9. Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding, Danny Driess, Avinava Dubey, Chelsea Finn, et al. Rt-2: Vision-language-action models transfer web knowledge to robotic control. arXiv preprint arXiv:2307.15818, 2023a.

10. Anthony Brohan, Yevgen Chebotar, Chelsea Finn, Karol Hausman, Alexander Herzog, Daniel Ho, Julian Ibarz, Alex Irpan, Eric Jang, Ryan Julian, et al. Do as i can, not as i say: Grounding language in robotic affordances. In Conference on robot learning, pp. 287–318. PMLR, 2023b.

11. Qingwen Bu, Yanting Yang, Jisong Cai, Shenyuan Gao, Guanghui Ren, Maoqing Yao, Ping Luo, and Hongyang Li. Univla: Learning to act anywhere with task-centric latent actions. arXiv preprint arXiv:2505.06111, 2025.

12. Huanqia Cai, Sihan Cao, Ruoyi Du, Peng Gao, Steven Hoi, Zhaohui Hou, Shijie Huang, Dengyang Jiang, Xin Jin, Liangchen Li, et al. Z-image: An efficient image generation foundation model with single-stream diffusion transformer. arXiv preprint arXiv:2511.22699, 2025.

13. Jun Cen, Chaohui Yu, Hangjie Yuan, Yuming Jiang, Siteng Huang, Jiayan Guo, Xin Li, Yibing Song, Hao Luo, Fan Wang, et al. Worldvla: Towards autoregressive action world model. arXiv preprint arXiv:2506.21539, 2025.

14. Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, and Shuran Song. Diffusion policy: Visuomotor policy learning via action diffusion. The International Journal of Robotics Research, pp. 02783649241273668, 2023.

15. Yilun Du, Sherry Yang, Bo Dai, Hanjun Dai, Ofir Nachum, Josh Tenenbaum, Dale Schuurmans, and Pieter Abbeel. Learning universal policies via text-guided video generation. Advances in neural information processing systems, 36:9156–9172, 2023.

16. Frederik Ebert, Chelsea Finn, Sudeep Dasari, Annie Xie, Alex Lee, and Sergey Levine. Visual foresight: Model-based deep reinforcement learning for vision-based robotic control. arXiv preprint arXiv:1812.00568, 2018.

17. Yao Feng, Hengkai Tan, Xinyi Mao, Guodong Liu, Shuhe Huang, Chendong Xiang, Hang Su, and Jun Zhu. Vidar: Embodied video diffusion model for generalist bimanual manipulation. arXiv preprint arXiv:2507.12898, 2025.

18. Chelsea Finn and Sergey Levine. Deep visual foresight for planning robot motion. In 2017 IEEE international conference on robotics and automation (ICRA), pp. 2786–2793. IEEE, 2017.

19. Zhi Hou, Tianyi Zhang, Yuwen Xiong, Haonan Duan, Hengjun Pu, Ronglei Tong, Chengyang Zhao, Xizhou Zhu, Yu Qiao, Jifeng Dai, et al. Dita: Scaling diffusion transformer for generalist vision-language-action policy. arXiv preprint arXiv:2503.19757, 2025.

20. Yucheng Hu, Yanjiang Guo, Pengchao Wang, Xiaoyu Chen, Yen-Jen Wang, Jianke Zhang, Koushil Sreenath, Chaochao Lu, and Jianyu Chen. Video prediction policy: A generalist robot policy with predictive visual representations. arXiv preprint arXiv:2412.14803, 2024.

21. Physical Intelligence, Ali Amin, Raichelle Aniceto, Ashwin Balakrishna, Kevin Black, Ken Conley, Grace Connors, James Darpinian, Karan Dhabalia, Jared DiCarlo, et al. a vla that learns from experience. arXiv preprint arXiv:2511.14759, 2025a.

22. Physical Intelligence, Kevin Black, Noah Brown, James Darpinian, Karan Dhabalia, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, et al. π0.5: a Vision-Language-Action Model with Open-World Generalization. arXiv preprint arXiv:2504.16054, 2025b.

23. Siddharth Karamcheti, Suraj Nair, Ashwin Balakrishna, Percy Liang, Thomas Kollar, and Dorsa Sadigh. Prismatic vlms: Investigating the design space of visually-conditioned language models. arXiv preprint arXiv:2402.07865, 2024.

24. Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael Rafailov, Ethan Foster, Grace Lam, Pannag Sanketi, et al. Openvla: An open-source vision-language-action model. arXiv preprint arXiv:2406.09246, 2024.

25. Moo Jin Kim, Chelsea Finn, and Percy Liang. Fine-tuning vision-language-action models: Optimizing speed and success. arXiv preprint arXiv:2502.19645, 2025.

26. Moo Jin Kim, Yihuai Gao, Tsung-Yi Lin, Yen-Chen Lin, Yunhao Ge, Grace Lam, Percy Liang, Shuran Song, Ming-Yu Liu, Chelsea Finn, et al. Cosmos policy: Fine-tuning video models for visuomotor control and planning. arXiv preprint arXiv:2601.16163, 2026.

27. Weijie Kong, Qi Tian, Zijian Zhang, Rox Min, Zuozhuo Dai, Jin Zhou, Jiangfeng Xiong, Xin Li, Bo Wu, Jianwei Zhang, et al. Hunyuanvideo: A systematic framework for large video generative models. arXiv preprint arXiv:2412.03603, 2024.

28. Lin Li, Qihang Zhang, Yiming Luo, Shuai Yang, Ruilin Wang, Fei Han, Mingrui Yu, Zelin Gao, Nan Xue, Xing Zhu, et al. Causal world modeling for robot control. arXiv preprint arXiv:2601.21998, 2026.

29. Shuang Li, Yihuai Gao, Dorsa Sadigh, and Shuran Song. Unified video action model. arXiv preprint arXiv:2503.00200, 2025a.

30. Wei Li, Renshan Zhang, Rui Shao, Jie He, and Liqiang Nie. Cogvla: Cognition-aligned vision-language-action model via instruction-driven routing & sparsification. arXiv preprint arXiv:2508.21046, 2025b.

31. Junbang Liang, Pavel Tokmakov, Ruoshi Liu, Sruthi Sudhakar, Paarth Shah, Rares Ambrus, and Carl Vondrick. Video generators are robot policies. arXiv preprint arXiv:2508.00795, 2025.

32. Yue Liao, Pengfei Zhou, Siyuan Huang, Donglin Yang, Shengcong Chen, Yuxin Jiang, Yue Hu, Jingbin Cai, Si Liu, Jianlan Luo, et al. Genie envisioner: A unified world foundation platform for robotic manipulation. arXiv preprint arXiv:2508.05635, 2025.

33. Yaron Lipman, Ricky TQ Chen, Heli Ben-Hamu, Maximilian Nickel, and Matt Le. Flow matching for generative modeling. arXiv preprint arXiv:2210.02747, 2022.

34. Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, and Peter Stone. Libero: Benchmarking knowledge transfer for lifelong robot learning. Advances in Neural Information Processing Systems, 36, 2024.

35. Soroush Nasiriany, Abhiram Maddukuri, Lance Zhang, Adeet Parikh, Aaron Lo, Abhishek Joshi, Ajay Mandlekar, and Yuke Zhu. Robocasa: Large-scale simulation of everyday tasks for generalist robots. arXiv preprint arXiv:2406.02523, 2024.

36. NVIDIA, :, Niket Agarwal, Arslan Ali, Maciej Bala, Yogesh Balaji, Erik Barker, Tiffany Cai, Prithvijit Chattopadhyay, Yongxin Chen, Yin Cui, Yifan Ding, Daniel Dworakowski, Jiaojiao Fan, Michele Fenzi, Francesco Ferroni, Sanja Fidler, Dieter Fox, Songwei Ge, Yunhao Ge, Jinwei Gu, Siddharth Gururani, Ethan He, Jiahui Huang, Jacob Huffman, Pooya Jannaty, Jingyi Jin, Seung Wook Kim, Gergely Klár, Grace Lam, Shiyi Lan, Laura Leal-Taixe, Anqi Li, Zhaoshuo Li, Chen-Hsuan Lin, Tsung-Yi Lin, Huan Ling, Ming-Yu Liu, Xian Liu, Alice Luo, Qianli Ma, Hanzi Mao, Kaichun Mo, Arsalan Mousavian, Seungjun Nah, Sriharsha Niverty, David Page, Despoina Paschalidou, Zeeshan Patel, Lindsey Pavao, Morteza Ramezanali, Fitsum Reda, Xiaowei Ren, Vasanth Rao Naik Sabavat, Ed Schmerling, Stella Shi, Bartosz Stefaniak, Shitao Tang, Lyne Tchapmi, Przemek Tredak, Wei-Cheng Tseng, Jibin Varghese, Hao Wang, Haoxiang Wang, Heng Wang, Ting-Chun Wang, Fangyin Wei, Xinyue Wei, Jay Zhangjie Wu, Jiashu Xu, Wei Yang, Lin Yen-Chen, Xiaohui Zeng, Yu Zeng, Jing Zhang, Qinsheng Zhang, Yuxuan Zhang, Qingqing Zhao, and Artur Zolkowski. Cosmos world foundation model platform for physical ai, 2025a. URL https://arxiv.org/abs/2501.03575.

37. NVIDIA, Johan Bjorck, Nikita Cherniadev Fernando Castañeda, Xingye Da, Runyu Ding, Linxi “Jim” Fan, Yu Fang, Dieter Fox, Fengyuan Hu, Spencer Huang, Joel Jang, Zhenyu Jiang, Jan Kautz, Kaushil Kundalia, Lawrence Lao, Zhiqi Li, Zongyu Lin, Kevin Lin, Guilin Liu, Edith Llontop, Loic Magne, Ajay Mandlekar, Avnish Narayan, Soroush Nasiriany, Scott Reed, You Liang Tan, Guanzhi Wang, Zu Wang, Jing Wang, Qi Wang, Jiannan Xiang, Yuqi Xie, Yinzhen Xu, Zhenjia Xu, Seonghyeon Ye, Zhiding Yu, Ao Zhang, Hao Zhang, Yizhou Zhao, Ruijie Zheng, and Yuke Zhu. GR00T N1: An open foundation model for generalist humanoid robots. In ArXiv Preprint, March 2025b.

38. Jonas Pai, Liam Achenbach, Victoriano Montesinos, Benedek Forrai, Oier Mees, and Elvis Nava. mimic-video: Video-action models for generalizable robot control beyond vlas. arXiv preprint arXiv:2512.15692, 2025.

39. William Peebles and Saining Xie. Scalable diffusion models with transformers. In Proceedings of the IEEE/CVF international conference on computer vision, pp. 4195–4205, 2023.

40. Peter J Rousseeuw. Silhouettes: a graphical aid to the interpretation and validation of cluster analysis. Journal of computational and applied mathematics, 20:53–65, 1987.

41. Yichao Shen, Fangyun Wei, Zhiying Du, Yaobo Liang, Yan Lu, Jiaolong Yang, Nanning Zheng, and Baining Guo. Videovla: Video generators can be generalizable robot manipulators. arXiv preprint arXiv:2512.06963, 2025.

42. Hugo Touvron, Louis Martin, Kevin Stone, Peter Albert, Amjad Almahairi, Yasmine Babaei, Nikolay Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti Bhosale, et al. Llama 2: Open foundation and fine-tuned chat models. arXiv preprint arXiv:2307.09288, 2023.

43. Unitree. Unifolm-wma-0: A world-model-action (wma) framework under unifolm family, 2025.

44. Team Wan, Ang Wang, Baole Ai, Bin Wen, Chaojie Mao, Chen-Wei Xie, Di Chen, Feiwu Yu, Haiming Zhao, Jianxiao Yang, Jianyuan Zeng, Jiayu Wang, Jingfeng Zhang, Jingren Zhou, Jinkai Wang, Jixuan Chen, Kai Zhu, Kang Zhao, Keyu Yan, Lianghua Huang, Mengyang Feng, Ningyi Zhang, Pandeng Li, Pingyu Wu, Ruihang Chu, Ruili Feng, Shiwei Zhang, Siyang Sun, Tao Fang, Tianxing Wang, Tianyi Gui, Tingyu Weng, Tong Shen, Wei Lin, Wei Wang, Wei Wang, Wenmeng Zhou, Wente Wang, Wenting Shen, Wenyuan Yu, Xianzhong Shi, Xiaoming Huang, Xin Xu, Yan Kou, Yangyu Lv, Yifei Li, Yijing Liu, Yiming Wang, Yingya Zhang, Yitong Huang, Yong Li, You Wu, Yu Liu, Yulin Pan, Yun Zheng, Yuntao Hong, Yupeng Shi, Yutong Feng, Zeyinzi Jiang, Zhen Han, Zhi-Fan Wu, and Ziyu Liu. Wan: Open and advanced large-scale video generative models. arXiv preprint arXiv:2503.20314, 2025.

45. Yiqi Wang, Mrinal Verghese, and Jeff Schneider. Latent policy steering with embodiment-agnostic pretrained world models. arXiv preprint arXiv:2507.13340, 2025.

46. Ze Yang, Yun Chen, Jingkang Wang, Sivabalan Manivasagam, Wei-Chiu Ma, Anqi Joyce Yang, and Raquel Urtasun. Unisim: A neural closed-loop sensor simulator. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pp. 1389–1399, 2023.

47. Seonghyeon Ye, Joel Jang, Byeongguk Jeon, Sejune Joo, Jianwei Yang, Baolin Peng, Ajay Mandlekar, Reuben Tan, Yu-Wei Chao, Bill Yuchen Lin, et al. Latent action pretraining from videos. arXiv preprint arXiv:2410.11758, 2024.

48. Zhigen Zhao, Liuchuan Yu, Ke Jing, and Ning Yang. Xrobotoolkit: A cross-platform framework for robot teleoperation. arXiv preprint arXiv:2508.00097, 2025.

49. Ruijie Zheng, Jing Wang, Scott Reed, Johan Bjorck, Yu Fang, Fengyuan Hu, Joel Jang, Kaushil Kundalia, Zongyu Lin, Loic Magne, et al. Flare: Robot learning with implicit world modeling. arXiv preprint arXiv:2505.15659, 2025.

50. Zangwei Zheng, Xiangyu Peng, Tianji Yang, Chenhui Shen, Shenggui Li, Hongxin Liu, Yukun Zhou, Tianyi Li, and Yang You. Open-sora: Democratizing efficient video production for all. arXiv preprint arXiv:2412.20404, 2024.

51. Zhide Zhong, Haodong Yan, Junfeng Li, Xiangchen Liu, Xin Gong, Wenxuan Song, Jiayi Chen, and Haoang Li. Flowvla: Thinking in motion with a visual chain of thought. arXiv preprint arXiv:2508.18269, 2025.

# Appendix A / 附录 A

## A.1 Model & Training Configurations / 模型与训练配置

#### Table 4. Model & training configurations / 模型与训练配置

![Table 4](<file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_019_fig_table_4.png>)

**Caption:** Table 4: Model & training configurations

**Caption[CN]:** 表 4：模型与训练配置

| Parameter | Value |
|---|---|
| **Video DiT** |  |
| Base VGM | Cosmos-Predict2.5-2B (Ali et al., 2025) |
| Attention Implementation | flash attention 2 |
| Hidden Feature Dim | 2048 |
| Extract Layer | 18 |
| **Action DiT** |  |
| Action Model Type | DiT-B |
| Hidden Size | 2560 |
| Add Positional Embedding | True |
| Max Sequence Length | 1024 |
| Action Dim | 32 |
| State Dim | 64 |
| Future Action Window Size | 15 |
| Action Horizon | 16 |
| Past Action Window Size | 0 |
| Cross Attention Dim | 2048 |
| Dropout | 0.2 |
| Final Dropout | True |
| Interleave Self Attention | True |
| Norm Type | AdaLN |
| Num Layers | 16 |
| Output Dim | 2560 |
| Repeated Diffusion Steps (train) | 4 |
| Noise β (α) | 1.5 |
| Noise β (β) | 1.0 |
| Noise s | 0.999 |
| Num Timestep Buckets | 1000 |
| Num Inference Timesteps | 4 |
| **Training Configurations** |  |
| Per Device Batch Size | 8 |
| Num of GPUs | 32 |
| Max Train Steps | 100000 |
| Num Warmup Steps | 5000 |
| Warmup Ratio | 0.1 |
| VGM LR | $1 \times 10^{-5}$ |
| Action Model LR | $1 \times 10^{-4}$ |
| LR Scheduler | cosine_with_min_lr |
| Min LR | $5 \times 10^{-7}$ |
| Gradient Clipping | 1.0 |
| Gradient Accumulation Steps | 1 |
| Optimizer | AdamW |
| $\beta_1, \beta_2$ | (0.9, 0.95) |
| $\epsilon$ | $1 \times 10^{-8}$ |
| Weight Decay | $1 \times 10^{-8}$ |

## A.2 Dataset Configuration / 数据集配置

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We detail the composition and configuration of the datasets used to train and evaluate the DiT4DiT framework, as summarized in Table 5. To rigorously assess both fundamental learning capabilities and physical deployability, our dataset usage is strategically partitioned into two distinct pipelines: one for simulated benchmark evaluation and another for real-world deployment.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们详细说明用于训练和评估 DiT4DiT 框架的数据集组成与配置，汇总见表 5。为了严格评估基础学习能力和物理部署能力，我们从策略上将数据集使用划分为两条不同的流程：一条用于仿真基准评估，另一条用于真实世界部署。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Simulated benchmark data:** To evaluate our framework in simulated environments, we train the models directly on the target datasets. For the RoboCasa-GR1 (Nasiriany et al., 2024) tabletop tasks, we utilize the Fourier GR1 Unified 1K dataset (Bjorck et al., 2025), which consists of 24,000 demonstration episodes collected using the highly complex 29-DoF GR1 humanoid embodiment. For the LIBERO (Liu et al., 2024) benchmark, we use its official dataset comprising 1,693 episodes based on a 7-DoF Franka Emika Panda robotic arm. Training from scratch on these datasets ensures a strictly fair evaluation against baseline methods in simulation as we do not have access to all pre-training datasets of various methods.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **仿真基准数据：** 为了在仿真环境中评估我们的框架，我们直接在目标数据集上训练模型。对于 RoboCasa-GR1（Nasiriany et al., 2024）桌面任务，我们使用 Fourier GR1 Unified 1K 数据集（Bjorck et al., 2025）；该数据集由 24,000 个演示 episode 组成，这些 episode 使用高度复杂的 29-DoF GR1 人形机器人本体采集。对于 LIBERO（Liu et al., 2024）基准，我们使用其官方数据集，其中包含基于 7-DoF Franka Emika Panda 机械臂的 1,693 个 episode。由于我们无法获得各种方法的全部预训练数据集，在这些数据集上从头训练能够确保仿真中相对于基线方法的严格公平评估。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Pre-training data for real-world tasks:** To facilitate robust physical deployment, DiT4DiT undergoes a crucial pre-training phase to acquire fundamental spatiotemporal and physical priors. For this stage, we utilize the scaled Fourier GR1 Pretrain 10K dataset (Bjorck et al., 2025), comprising 241,450 episodes of the 29-DoF GR1 embodiment. As highlighted in our main text, this pre-training corpus represents merely 15% of the massive data volume leveraged by baselines like GR00T-N1.5, heavily emphasizing the data efficiency of our generative video backbone.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **真实世界任务的预训练数据：** 为了促进稳健的物理部署，DiT4DiT 经历一个关键的预训练阶段，以获取基础时空先验和物理先验。在这一阶段，我们使用扩展后的 Fourier GR1 Pretrain 10K 数据集（Bjorck et al., 2025），其中包含 29-DoF GR1 机器人本体的 241,450 个 episode。正如正文所强调的，该预训练语料仅相当于 GR00T-N1.5 等基线所用海量数据规模的 15%，有力凸显了我们生成式视频骨干网络的数据效率。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Real-world fine-tuning data:** Following pre-training, the model is fine-tuned to adapt its generative priors to the target physical robot. For this stage, we employ our custom real-robot dataset, consisting of 1,400 high-quality, teleoperated demonstration episodes (200 episodes for each task). This dataset is specifically tailored for the Unitree G1 humanoid robot, operating with a continuous 16-DoF action space. This crucial fine-tuning phase successfully grounds the broad simulation-based physical dynamics into precise, real-world continuous control commands.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **真实世界微调数据：** 预训练之后，对模型进行微调，使其生成先验适配目标实体机器人。在这一阶段，我们采用自定义真实机器人数据集，其中包含 1,400 个高质量遥操作演示 episode（每个任务 200 个 episode）。该数据集专门针对 Unitree G1 人形机器人定制，使用连续的 16-DoF 动作空间。这一关键微调阶段成功地将广泛的仿真物理动力学落地为精确的真实世界连续控制指令。

#### Table 5. Details of the used datasets / 所用数据集详情

![Table 5](<file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_020_fig_table_5.png>)

**Caption:** Table 5: Details of the used datasets. We report the episode count, embodiment type, and degrees of freedom.

**Caption[CN]:** 表 5：所用数据集的详情。我们报告 episode 数量、机器人本体类型和自由度。

| Dataset | Episode Cnt | Embodiment | DoF |
|---|---:|---|---:|
| Fourier_GR1_Unified_1K (Bjorck et al., 2025) | 24,000 | GR1 humanoid | 29 |
| Fourier_GR1_Pretrain_10K (Bjorck et al., 2025) | 241,450 | GR1 humanoid | 29 |
| LIBERO (Liu et al., 2024) | 1,693 | Franka Emika Panda | 7 |
| Real Robot | 1,400 | G1 humanoid | 16 |

## A.3 Real-World Experiment Setting / 真实世界实验设置

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> As shown in fig. 9, our real-world experimental system is built upon the Unitree G1 humanoid robot, featuring a 16-DoF action space driven by dual 7-DoF arms. Each arm is equipped with an ALOHA 2 (Aldaco et al., 2024) gripper to facilitate high-precision bimanual manipulation. For visual perception, an Intel RealSense D435i camera is mounted on the robot’s head to capture egocentric RGB observations at a resolution of 640x480. The real-time inference is executed on a workstation with a single NVIDIA GeForce RTX 4090 GPU.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 如图 9 所示，我们的真实世界实验系统建立在 Unitree G1 人形机器人之上，具有由两条 7-DoF 手臂驱动的 16-DoF 动作空间。每条手臂都配备一个 ALOHA 2（Aldaco et al., 2024）夹爪，以支持高精度双臂操作。在视觉感知方面，机器人的头部安装了一台 Intel RealSense D435i 相机，以 640x480 的分辨率捕获第一人称 RGB 观测。实时推理由配备单张 NVIDIA GeForce RTX 4090 GPU 的工作站执行。

#### Figure 9. Robot system setups / 机器人系统设置

![Figure 9](<file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_020_fig_figure_9.png>)

**Caption:** Figure 9: Visualization of the robot system setups. The experimental platform consists of a Unitree G1 humanoid robot equipped with dual ALOHA 2 (Aldaco et al., 2024) grippers and an Intel RealSense D435i camera. A human operator utilizes a PICO VR headset and the XRoboToolkit (Zhao et al., 2025) framework to perform teleoperated demonstrations for high-quality data collection.

**Caption[CN]:** 图 9：机器人系统设置的可视化。实验平台由一台 Unitree G1 人形机器人组成，该机器人配备两个 ALOHA 2（Aldaco et al., 2024）夹爪和一台 Intel RealSense D435i 相机。人类操作员使用 PICO VR 头显和 XRoboToolkit（Zhao et al., 2025）框架执行遥操作演示，以采集高质量数据。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Data collection is performed via a VR-based teleoperation pipeline using a PICO VR headset and handheld controllers. This setup allows a human operator to provide natural demonstrations by mapping motion directly to the robot’s joints. The XRoboToolkit (Zhao et al., 2025) framework manages the entire software stack, ensuring precise synchronization of multimodal sensor data and high-quality recording of demonstration trajectories. This integrated environment supports a seamless transition from human-led data collection to autonomous policy deployment.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 数据采集通过基于 VR 的遥操作流程完成，该流程使用 PICO VR 头显和手持控制器。这一设置通过将动作直接映射到机器人关节，使人类操作员能够提供自然演示。XRoboToolkit（Zhao et al., 2025）框架管理整个软件栈，确保多模态传感器数据的精确同步和演示轨迹的高质量记录。这一集成环境支持从人类主导的数据采集无缝过渡到自主策略部署。

## A.4 Limitations and Discussion / 局限与讨论

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> While DiT4DiT demonstrates exceptional capabilities in bridging generative video priors and continuous robotic control, limitations present exciting avenues for future research.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 尽管 DiT4DiT 在连接生成式视频先验与连续机器人控制方面展现出卓越能力，但现有局限也为未来研究提供了令人振奋的方向。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Our current physical deployment relies exclusively on a single egocentric (ego-view) camera. While this highlights the remarkable spatial reasoning capabilities of our video representations, single-view setups are fundamentally susceptible to severe visual occlusions. In complex bimanual tasks, the robot’s own arms or larger objects can temporarily block the camera’s line of sight, potentially disrupting the temporal continuity of the visual features. Future iterations could explore the integration of auxiliary sensory inputs, such as wrist-mounted cameras or tactile feedback, fusing these modalities with the video DiT backbone to maintain robust state estimation during severe occlusions.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 我们当前的物理部署完全依赖单个第一人称（ego-view）相机。尽管这凸显了我们视频表征卓越的空间推理能力，但单视角设置从根本上容易受到严重视觉遮挡的影响。在复杂双臂任务中，机器人自身的手臂或较大物体可能暂时阻挡相机视线，从而可能破坏视觉特征的时间连续性。未来版本可以探索整合辅助传感输入，例如腕部相机或触觉反馈，并将这些模态与 video DiT 骨干网络融合，以便在严重遮挡期间维持稳健的状态估计。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Our real-world experiments achieved state-of-the-art zero-shot generalization using a pre-training corpus that represents merely 15% of the data volume utilized by contemporary large-scale models like GR00T. A natural and promising next step is to drastically scale the pre-training data across diverse robotic embodiments (e.g., varying kinematics, grippers, and camera parameters). Given the data-efficient nature of our dual flow-matching objective, scaling DiT4DiT with massive, cross-embodiment datasets could yield a highly generalized robotic foundation model, further solidifying video generation as the optimal scaling proxy for embodied intelligence.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 我们的真实世界实验使用的预训练语料仅相当于 GR00T 等当代大规模模型所用数据量的 15%，却实现了最先进的零样本泛化。自然而又前景广阔的下一步，是在多样化机器人本体之间大幅扩展预训练数据（例如改变运动学结构、夹爪和相机参数）。鉴于双 flow-matching 目标具备数据高效特性，使用海量跨本体数据集扩展 DiT4DiT，可能产生高度泛化的机器人基础模型，并进一步巩固视频生成作为具身智能最优扩展代理的地位。

#### Figure 10. Future video rollouts / 未来视频 rollout

![Figure 10](<file:///Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/DiT4DiT%20Jointly%20Modeling%20Video%20Dynamics%20and%20Actions%20for%20Generalizable%20Robot%20Control/assets/page_022_fig_figure_10.png>)

**Caption:** Figure 10: Future video rollouts generated by DiT4DiT.

**Caption[CN]:** 图 10：DiT4DiT 生成的未来视频 rollout。

