# World Action Models are Zero-shot Policies

## Metadata / 元数据

| Field | Value |
|---|---|
| Paper | **World Action Models are Zero-shot Policies** |
| System | **DreamZero**, a 14B World Action Model (WAM) |
| Authors | Seonghyeon Ye†; Yunhao Ge*; Kaiyuan Zheng*; Shenyuan Gao*; Sihyun Yu*; George Kurian*; Suneel Indupuru*; You Liang Tan*; Chuning Zhu; Jiannan Xiang; Ayaan Malik; Kyungmin Lee; William Liang; Nadun Ranawaka; Jiasheng Gu; Yinzhen Xu; Guanzhi Wang; Fengyuan Hu; Avnish Narayan; Johan Bjorck; Jing Wang; Gwanghyun Kim; Dantong Niu; Ruijie Zheng; Yuqi Xie; Jimmy Wu; Qi Wang; Ryan Julian; Danfei Xu; Yilun Du; Yevgen Chebotar; Scott Reed; Jan Kautz; Yuke Zhu†; Linxi “Jim” Fan†; Joel Jang† |
| Affiliation | NVIDIA |
| Roles | † Project Leads; * Core Contributors |
| arXiv | [arXiv:2602.15922v1](https://arxiv.org/abs/2602.15922), `[cs.RO]`, submitted 17 February 2026 |
| DOI | `10.48550/arXiv.2602.15922` |
| PDF build date shown in source | 2026-02-19 |
| Length | 36 pages |
| Project page | <https://dreamzero0.github.io> |
| Code | <https://github.com/dreamzero0/dreamzero> |

**Asset policy / 资源策略：** This reader reuses the existing read-only `assets/` directory in this paper folder. No image asset was created, copied, renamed, or modified. / 本阅读稿复用论文文件夹中现有的只读 `assets/` 目录，未创建、复制、重命名或修改任何图片资源。

## Page / Section Index

| PDF pages | Source structure | Reader anchor |
|---:|---|---|
| 1–2 | Title, Figure 1, Abstract | [Abstract](#abstract) |
| 2–4 | 1. Introduction | [1. Introduction](#1-introduction) |
| 4–6 | 2. Related Work | [2. Related Work](#2-related-work) |
| 6–10 | 3. DreamZero | [3. DreamZero](#3-dreamzero) |
| 10–13 | 4. Experimental Setup | [4. Experimental Setup](#4-experimental-setup) |
| 13–18 | 5. Experimental Results | [5. Experimental Results](#5-experimental-results) |
| 18–19 | 6. Discussion and Future Work | [6. Discussion and Future Work](#6-discussion-and-future-work) |
| 19 | 7. Acknowledgment | [7. Acknowledgment](#7-acknowledgment) |
| 20 | Appendix A. Alternative World Model Architectures | [Appendix A](#appendix-a-comparison-with-alternative-world-model-architectures) |
| 20–21 | Appendix B. Bidirectional vs. Autoregressive WAMs | [Appendix B](#appendix-b-bidirectional-vs-autoregressive-wams) |
| 21–22 | Appendix C. Model and Training Details; Algorithms 1–2 | [Appendix C](#appendix-c-model-and-training-details) |
| 22–24 | Appendix D. Real-time Execution Details; Equations (4)–(6) | [Appendix D](#appendix-d-real-time-execution-details) |
| 24–25 | Appendix E. AgiBot Diverse Data Collection Strategy | [Appendix E](#appendix-e-agibot-diverse-data-collection-strategy) |
| 25–28 | Appendices F–G. AgiBot and DROID Evaluation Details; Tables 5–7b | [Appendix F](#appendix-f-agibot-evaluation-details) / [Appendix G](#appendix-g-droid-evaluation-details) |
| 28–29 | Appendix H. Failure Case Analysis; Figure 16 | [Appendix H](#appendix-h-failure-case-analysis) |
| 30–36 | References [1]–[92] | [References](#references) |

## Terminology Ledger

| Canonical term / identifier | 中文统一译法 | Scope note |
|---|---|---|
| World Action Model (WAM) | 世界动作模型 | Jointly predicts a future world state and actions; `WAM` is retained. |
| Vision-Language-Action model (VLA) | 视觉—语言—动作模型 | Extends a VLM to motor-action prediction; `VLA` is retained. |
| DreamZero | DreamZero | The paper's 14B autoregressive WAM. |
| DreamZero-Flash | DreamZero-Flash | Decoupled video/action noise scheduling for few-step or one-step action denoising. |
| inverse dynamics model (IDM) | 逆动力学模型 | Maps visual state changes or visual futures to actions; `IDM` is retained. |
| embodiment | 机器人形态 | Refers to the robot body/action interface, not generic “embodied AI.” |
| task progress | 任务进度 | Partial-completion metric; it is not automatically equivalent to success rate. |
| success rate | 成功率 | Fraction of fully successful rollouts. |
| flow matching | 流匹配 | Joint video–action denoising objective. |
| teacher forcing | 教师强制 | Denoises a noisy current chunk conditioned on clean prior chunks. |
| action chunk | 动作块 | A contiguous control sequence predicted and asynchronously executed. |
| KV cache | KV 缓存 | Autoregressive visual history, refreshed with ground-truth observations. |
| DiT | 扩散 Transformer | Identifier `DiT` is retained. |
| proprioceptive state | 本体感受状态 | Robot joint/state signal, denoted by $q$. |
| bidirectional (BD) | 双向 | `BD` is retained in tables. |
| autoregressive (AR) | 自回归 | `AR` is retained in tables. |

## Figure 1. Overview / 总览

![Figure 1](WorldModel/World%20Action%20Models%20are%20Zero-shot%20Policies/assets/page_001_fig_figure_1.png)

**Caption:** Overview. By jointly predicting video and action, World Action Models (WAMs) inherit world physics priors that enable 1) effective learning from diverse, non-repetitive data, 2) open-world generalization, 3) cross-embodiment learning from video-only data, and 4) few-shot adaptation to new robots.

**Caption[CN]:** 总览。通过联合预测视频与动作，世界动作模型（WAM）继承了世界物理先验，从而实现：1）从多样、非重复数据中有效学习；2）开放世界泛化；3）利用纯视频数据实现跨机器人形态学习；以及 4）对新机器人进行少样本适配。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The overview contrasts diverse, non-repetitive pretraining data (bimanual mobile manipulation and single-arm manipulation) with task repetition; shows generalization after post-training on fruit packing and table bussing; depicts task transfer via cross-embodiment videos from a bimanual arm and a human; lists zero-shot tasks in unseen environments (“Untie the box,” “Press elevator button,” “Fan the burger,” and “Depress the lever on the toaster”); and shows few-shot adaptation to a new embodiment with only 30 minutes of play data (“Pick up the teddy bear,” “Put orange in pumpkin,” “Put noodle in paper bag,” and “Put banana in shelf”).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 该总览图将多样、非重复预训练数据（双臂移动操作与单臂操作）同任务重复进行对比；展示了在水果装袋与清理餐桌任务上经过后训练仍保留的泛化；描绘了借助双臂机器人和人类视频进行跨机器人形态任务迁移；列出了新环境中的零样本任务（“解开盒子”、“按电梯按钮”、“给汉堡煽风”和“向下压烤面包机的拨杆”）；并展示仅用 30 分钟自由操作数据对新机器人形态进行少样本适配（“拿起泰迪熊”、“把橙子放进南瓜”、“把方便面放进纸袋”和“把香蕉放进架子”）。

# Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> State-of-the-art Vision-Language-Action (VLA) models excel at semantic generalization but struggle to generalize to unseen physical motions in novel environments. We introduce DreamZero, a World Action Model (WAM) built upon a pretrained video diffusion backbone. Unlike VLAs, WAMs learn physical dynamics by predicting future world states and actions, using video as a dense representation of how the world evolves. By jointly modeling video and action, DreamZero learns diverse skills effectively from heterogeneous robot data without relying on repetitive demonstrations. This results in over 2× improvement in generalization to new tasks and environments compared to state-of-the-art VLAs in real-robot experiments. Crucially, through model and system optimizations, we enable a 14B autoregressive video diffusion model to perform real-time closed-loop control at 7Hz. Finally, we demonstrate two forms of cross-embodiment transfer: video-only demonstrations from other robots or humans yield a relative improvement of over 42% on unseen task performance with just 10–20 minutes of data. More surprisingly, DreamZero enables few-shot embodiment adaptation, transferring to a new embodiment with only 30 minutes of play data while retaining zero-shot generalization.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 最先进的视觉—语言—动作（VLA）模型擅长语义泛化，却难以在新环境中泛化到未见过的物理运动。我们提出 DreamZero，这是一种建立在预训练视频扩散骨干上的世界动作模型（WAM）。与 VLA 不同，WAM 通过预测未来世界状态和动作来学习物理动力学，并把视频作为世界演化过程的稠密表示。通过联合建模视频与动作，DreamZero 无须依赖重复示范，即可从异构机器人数据中有效学会多种技能。在真实机器人实验中，其对新任务和新环境的泛化能力较最先进 VLA 提高了 2 倍以上。关键的是，借助模型与系统优化，我们使一个 14B 自回归视频扩散模型能以 7Hz 执行实时闭环控制。最后，我们展示了两种跨机器人形态迁移：只需 10–20 分钟来自其他机器人或人类的纯视频示范，未见任务性能便可相对提升 42% 以上。更令人惊讶的是，DreamZero 支持少样本机器人形态适配：仅用 30 分钟自由操作数据即可迁移到新形态，同时保留零样本泛化能力。

# 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Recent robotic foundation models, termed Vision-Language Action models (VLAs), extend pretrained Vision-Language Models (VLMs) to predict motor actions (Bjorck et al., 2025; Black et al., 2024; Brohan et al., 2023; Gemini Robotics Team, 2025; Kim et al., 2024). While VLAs successfully inherit linguistic priors to generalize across diverse language instructions, especially manipulating diverse objects (Brohan et al., 2023), their generalization to novel environments and, more critically, to new motions or skills remains limited (Guruprasad et al., 2025; Zhou et al., 2025). For example, VLAs can successfully execute “move coke can to Taylor Swift” (Brohan et al., 2023) by leveraging the web knowledge acquired during VLM pretraining to identify the target location, and connecting it to the learned move skill from the robot data. However, they fail at a task like “untie the shoelace” if that specific skill was not present in the robot training data. Although VLM priors encode what to do at a semantic level, they lack representations of how actions should be executed with precise spatial awareness, aligned with geometry, dynamics, and motor control (Chen et al., 2024; Feng et al., 2025). As a result, VLAs often struggle to adapt to new environments or generalize to novel tasks beyond the distribution of expert demonstrations, without explicitly collecting large-scale task- and environment-specific action data.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 近年来的机器人基础模型被称为视觉—语言—动作模型（VLA），它们把预训练视觉—语言模型（VLM）扩展到运动动作预测（Bjorck et al., 2025; Black et al., 2024; Brohan et al., 2023; Gemini Robotics Team, 2025; Kim et al., 2024）。尽管 VLA 成功继承了语言先验，能泛化到多样的语言指令，尤其能操作多种物体（Brohan et al., 2023），但它们对新环境的泛化，以及更关键的对新运动或新技能的泛化仍然有限（Guruprasad et al., 2025; Zhou et al., 2025）。例如，VLA 可利用 VLM 预训练期间获得的网络知识识别目标位置，再将其与机器人数据中学到的搬运技能连接，从而成功执行“把可乐罐移到 Taylor Swift 那里”（Brohan et al., 2023）。然而，如果机器人训练数据中没有特定技能，它们便会在“解开鞋带”这类任务上失败。虽然 VLM 先验在语义层面编码了“做什么”，却缺乏“如何执行”的表示：后者需要精确的空间感知，并与几何、动力学及运动控制对齐（Chen et al., 2024; Feng et al., 2025）。因此，如果不显式采集大规模、任务专用且环境专用的动作数据，VLA 往往难以适应新环境，或泛化到超出专家示范分布的新任务。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In this paper, we present DreamZero, a 14B robot foundation model built upon a pretrained image-to-video diffusion backbone (Team Wan, 2025). We term this architecture a World Action Model (WAM)—a foundation model designed to predict both actions and visual future states in an aligned manner. Initialized from video diffusion models trained on web-scale video data, WAMs leverage rich spatiotemporal priors to jointly generate future frames and actions conditioned on language instructions and observations. This shifts action learning from dense state–action imitation to inverse dynamics—aligning motor commands with predicted visual futures. Consequently, we observe that this enables (1) effective learning from robot data that are heterogeneous trajectories collected during the execution of useful behaviors in real-world settings, rather than relying solely on carefully repeated demonstrations, (2) zero-shot generalization to new tasks in new environments, and (3) efficient cross-embodiment transfer.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 本文提出 DreamZero：一个建立在预训练图生视频扩散骨干上的 14B 机器人基础模型（Team Wan, 2025）。我们将这种架构称为世界动作模型（WAM），即以对齐方式同时预测动作和视觉未来状态的基础模型。WAM 由在 web-scale 视频数据上训练的视频扩散模型初始化，利用丰富的时空先验，在语言指令和观测条件下联合生成未来帧与动作。这将动作学习从稠密的状态—动作模仿转变为逆动力学，也就是把运动指令与预测的视觉未来对齐。因此，我们观察到该方法可实现：（1）从机器人数据中有效学习；这些数据是机器人在真实场景执行有用行为时采集到的异构轨迹，而不只是精心重复的示范；（2）零样本泛化到新环境中的新任务；以及（3）高效的跨机器人形态迁移。

## Figure 2. Joint Video and Action Prediction / 联合视频与动作预测

![Figure 2](WorldModel/World%20Action%20Models%20are%20Zero-shot%20Policies/assets/page_003_fig_figure_2.png)

**Caption:** Joint Video and Action Prediction. DreamZero jointly generates video and action. We observe that the predicted actions closely align with the generated video. The examples are from totally unseen tasks.

**Caption[CN]:** 联合视频与动作预测。DreamZero 联合生成视频和动作。我们观察到，预测动作与生成视频高度对齐。这些示例均来自完全未见任务。

> <span style="color:#3B82F6"><strong>Para. 2a:</strong></span> The two visible unseen-task instructions are “Hit the Cymbal” and “Fry vegetables in pan with spatula”; each example juxtaposes generated futures with real-world execution.

> <span style="color:#F59E0B"><strong>Para. 2a[CN]:</strong></span> 图中可见的两条未见任务指令是“敲钹”与“用锅铲在锅中炒蔬菜”；每个示例都将生成未来与真实世界执行并置。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> This approach yields three core advancements that distinguish DreamZero from prior work, including other WAMs (Kim et al., 2026; Liang et al., 2025; Pai et al., 2025). First, DreamZero unlocks new generalization capabilities beyond traditional VLAs and previous WAMs—across environments, across tasks, and across embodiments (Figure 2 and Figure 3). Compared to the state-of-the-art pretrained VLAs, we observe more than a 2× improvement in average task progress on environment and task generalization benchmarks. Second, DreamZero demonstrates that generalist policies can be learned effectively from diverse, heterogeneous data, breaking away from the conventional wisdom that generalist robot policies require multiple repeated demonstrations per task. Although other WAMs show that priors learned from video prediction improve sample efficiency for action learning compared to VLAs (Liao et al., 2025; Pai et al., 2025), most works still focus on repeated demonstrations. Moreover, the environment generalization of DreamZero is retained even after task-specific post-training, outperforming state-of-the-art VLAs by 10% on average task progress. Lastly, we demonstrate two forms of cross-embodiment transfer. First, video-only demonstrations from another robot (YAM) or humans yield a relative improvement of over 42% on unseen task performance for the target robot (AgiBot G1) with just 10–20 minutes of data. Second, and more surprisingly, we show that DreamZero enables few-shot embodiment adaptation: a model pretrained on AgiBot G1 adapts to an entirely new robot (YAM) with only 30 minutes of play data, retaining zero-shot generalization. To the best of our knowledge, this sets a new benchmark for data-efficient embodiment adaptation.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 这一方法带来了三项核心进展，使 DreamZero 区别于包括其他 WAM 在内的既有工作（Kim et al., 2026; Liang et al., 2025; Pai et al., 2025）。首先，DreamZero 解锁了超越传统 VLA 和先前 WAM 的新泛化能力，涵盖环境、任务与机器人形态（Figure 2 和 Figure 3）。同最先进的预训练 VLA 相比，我们在环境与任务泛化 benchmark 上观察到平均任务进度提升了 2 倍以上。其次，DreamZero 证明通用策略可以从多样、异构数据中有效学会，突破了“通用机器人策略要求每个任务必须有多次重复示范”的传统观念。尽管其他 WAM 已经表明，与 VLA 相比，从视频预测中学到的先验可提高动作学习的样本效率（Liao et al., 2025; Pai et al., 2025），但大多数工作仍聚焦于重复示范。此外，DreamZero 在任务专用后训练之后仍保留环境泛化性，其平均任务进度比最先进 VLA 高 10%。最后，我们展示了两种跨机器人形态迁移。其一，仅用 10–20 分钟来自另一机器人（YAM）或人类的纯视频示范，目标机器人（AgiBot G1）的未见任务性能便可相对提升 42% 以上。其二，也更令人惊讶的是，DreamZero 支持少样本机器人形态适配：在 AgiBot G1 上预训练的模型只需 30 分钟自由操作数据，即可适应全新机器人 YAM，同时保留零样本泛化。据我们所知，这为数据高效的机器人形态适配树立了新 benchmark。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> DreamZero is a 14B autoregressive diffusion transformer trained with a teacher-forcing chunk-wise video denoising objective. Our architectural analysis reveals that larger pretrained video diffusion models produce higher-quality video predictions, which directly translates to superior downstream action execution—indicating that policy performance is fundamentally tied to video generation quality. We further find that a diverse distribution of the training data is essential for generalization, outperforming multi-task repetitive data with the same amount of hours. Furthermore, we observe that autoregressive architectures lead to smoother robot motions and higher modality alignment between predicted videos and executed actions.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> DreamZero 是一个 14B 自回归扩散 Transformer，使用教师强制的分块视频去噪目标进行训练。我们的架构分析表明，更大的预训练视频扩散模型会产生更高质量的视频预测，这又会直接转化为更优的下游动作执行；这说明策略性能从根本上与视频生成质量相关。我们还发现，多样的训练数据分布对泛化至关重要；在数据时长相同的情况下，它优于多任务重复数据。此外，我们观察到自回归架构可使机器人运动更平滑，并提高预测视频与实际动作之间的模态对齐。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> To address the computational overhead inherent to video diffusion models, we introduce a suite of optimizations spanning three categories: (1) algorithmic improvements, including decoupled video and action denoising schedules (DreamZero-Flash); (2) system-level parallelism and caching strategies; and (3) low-level optimizations such as quantization and CUDA kernel tuning. Collectively, these techniques achieve a 38× inference speedup without degrading performance, enabling DreamZero to generate action chunks at approximately 7Hz for smooth, real-time robotic control.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 为解决视频扩散模型固有的计算开销，我们提出了一系列涵盖三类的优化：（1）算法改进，包括视频与动作的解耦去噪日程（DreamZero-Flash）；（2）系统级并行与缓存策略；以及（3）量化和 CUDA 内核调优等底层优化。这些技术合起来在不降低性能的前提下实现了 38 倍推理加速，使 DreamZero 能以约 7Hz 生成动作块，用于平滑的实时机器人控制。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Our main contributions are:
>
> - We introduce DreamZero, a 14B WAM that jointly predicts video and actions, enabling effective learning from diverse, non-repetitive robot data.
> - We demonstrate over 2× improvement in zero-shot generalization to unseen verbs and motions compared to state-of-the-art VLAs, while retaining generalization across objects and environments.
> - We present model and system optimizations achieving 38× inference speedup, enabling real-time closed-loop control at 7Hz.
> - We demonstrate cross-embodiment transfer: video-only data from humans (12 minutes) or other robots (20 minutes) yields a relative improvement of over 42% on unseen tasks, and introduce few-shot embodiment adaptation—DreamZero pretrained on AgiBot G1 adapts to an entirely new robot (YAM) with only 30 minutes of play data, enabling zero-shot generalization.
> - We open-source our model weights, inference code, and code to run publicly available real-world (RoboArena) and simulation benchmarks (PolaRiS and Genie Sim 3.0) at <https://github.com/dreamzero0/dreamzero>.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 我们的主要贡献如下：
>
> - 我们提出 DreamZero：一个联合预测视频与动作的 14B WAM，可从多样、非重复机器人数据中有效学习。
> - 与最先进 VLA 相比，我们在对未见动词和运动的零样本泛化上实现了 2 倍以上的改进，同时保留跨物体和环境的泛化。
> - 我们提出实现 38 倍推理加速的模型与系统优化，从而以 7Hz 进行实时闭环控制。
> - 我们展示了跨机器人形态迁移：来自人类（12 分钟）或其他机器人（20 分钟）的纯视频数据使未见任务性能相对提升 42% 以上；我们还引入了少样本机器人形态适配，使在 AgiBot G1 上预训练的 DreamZero 仅用 30 分钟自由操作数据便可适应全新机器人 YAM，并实现零样本泛化。
> - 我们在 <https://github.com/dreamzero0/dreamzero> 开源模型权重、推理代码，以及运行公开真实世界 benchmark（RoboArena）和仿真 benchmark（PolaRiS 与 Genie Sim 3.0）的代码。

## Figure 3. Free-form Evaluation / 自由形式评测

![Figure 3](WorldModel/World%20Action%20Models%20are%20Zero-shot%20Policies/assets/page_004_fig_figure_3.png)

**Caption:** Free-form Evaluation. DreamZero performs a diverse range of tasks when conditioned on natural language instructions, including object manipulation, tool use, and human-robot interaction.

**Caption[CN]:** 自由形式评测。在自然语言指令条件下，DreamZero 可执行多种任务，包括物体操作、工具使用以及人机交互。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> The visible free-form prompts are: “Stack green bowl on the blue bowl”; “Throw trash into trash can”; “Pick up juice box and insert into cup”; “Push rolling chair back under desk”; “Pick a card from the deck”; “Pass spatula from right arm to left arm”; “Grab the sauce bottle and pour into cup”; “Move cube in the direction of the arrow”; “Pull the cart”; “Pick up tool and hand it to human”; “Slide the box”; “Fold the shorts”; “Place bag in basket”; “Grab eraser and wipe whiteboard”; “Pull wipe and wipe the table”; “Reach inside the box to grab pear”; “Unplug the cable”; “Fist bump the human”; “Pick up mango and put on tray”; and “Flip light switch off.”

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 图中可见的自由形式指令为：“把绿色碗叠在蓝色碗上”；“把垃圾扔进垃圾桶”；“拿起果汁盒并插入杯中”；“把带轮椅推回桌子下方”；“从牌堆中抽一张牌”；“将锅铲从右臂交给左臂”；“抓起酱汁瓶并倒入杯中”；“沿箭头方向移动方块”；“拉车”；“拿起工具并递给人”；“滑动盒子”；“折叠短裤”；“把袋子放进篮子”；“拿橡皮擦白板”；“抽出擦巾并擦桌子”；“伸进盒子里拿梨”；“拔掉电缆”；“与人碰拳”；“拿起芒果放到托盘上”；以及“关掉电灯开关”。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> **Footnote 1.** Despite only being trained on $\sim$500 hours of real-world data, DreamZero shows non-trivial performance on Genie Sim 3.0, which is a simulation benchmark comprised of 100 different tasks, without being explicitly trained on the 10k hours of simulation training data.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **脚注 1。** 尽管仅在约 500 小时真实世界数据上训练，DreamZero 在 Genie Sim 3.0 上仍展现出不可忽略的性能。Genie Sim 3.0 是一个包含 100 个不同任务的仿真 benchmark，而 DreamZero 并未在其 10k 小时仿真训练数据上进行显式训练。

# 2. Related Work

## 2.1. Vision Language Action Models

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Utilizing Foundation Models for Robotics.** Developing foundation models (Bommasani et al., 2021) for physical artificial intelligence has emerged as a significant research frontier. One line of work involves using existing, pre-trained foundation models as “black-box” reasoners to handle high-level task planning. These works usually involve modular systems, where the foundation models generate sequences of instructions, visual traces, or affordances that are subsequently executed by specialized, low-level robotic policies or controllers (Brohan et al., 2023; Driess et al., 2023; Huang et al., 2023; Kumar et al., 2026; Singh et al., 2023). While this modularity simplifies complex planning and enables stronger generalization (Kaelbling and Lozano-Pérez; Lee et al., 2025; Li et al., 2025) and efficiency (Dreczkowski et al., 2025), it is contingent upon having a pre-existing library of low-level skills and a robust interface to bridge the gap between abstract reasoning and physical execution. Additionally, these decoupled systems face the risk of compounding errors across modules.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **将基础模型用于机器人。** 为物理人工智能开发基础模型（Bommasani et al., 2021）已成为重要研究前沿。其中一条路线把现有预训练基础模型当作“黑箱”推理器，用于高层任务规划。这类工作通常采用模块化系统：基础模型生成指令序列、视觉轨迹或可供性，随后由专用的底层机器人策略或控制器执行（Brohan et al., 2023; Driess et al., 2023; Huang et al., 2023; Kumar et al., 2026; Singh et al., 2023）。尽管这种模块化可简化复杂规划，并带来更强的泛化性（Kaelbling and Lozano-Pérez; Lee et al., 2025; Li et al., 2025）与更高的效率（Dreczkowski et al., 2025），但它依赖于一个预先存在的底层技能库，以及能弥合抽象推理与物理执行之间差距的稳健接口。此外，这些解耦系统还面临错误在模块间累积的风险。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **VLAs.** On the other hand, end-to-end models such as Vision-Language-Action models (VLAs) (Bjorck et al., 2025; Black et al., 2024; Brohan et al., 2022, 2023; Bu et al., 2025; Gemini Robotics Team, 2025; Kim et al., 2024; Physical Intelligence, 2025; Yang et al., 2025; Ye et al., 2025; Zheng et al., 2025) have gained popularity by moving away from a rigid hierarchy of planning and control, combining language-conditioned semantics and low-level robot actions within the same model. VLAs are often initialized from large vision-language (VLM) models pre-trained on web-scale datasets. While pushing the frontier on visual-semantic knowledge transfer, these models are pre-trained on static image-text datasets, which limits their ability to inherit spatiotemporal priors required to transfer knowledge to new physical skills.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **VLA。** 另一方面，视觉—语言—动作模型（VLA）等端到端模型（Bjorck et al., 2025; Black et al., 2024; Brohan et al., 2022, 2023; Bu et al., 2025; Gemini Robotics Team, 2025; Kim et al., 2024; Physical Intelligence, 2025; Yang et al., 2025; Ye et al., 2025; Zheng et al., 2025）逐渐流行起来：它们摆脱僵硬的规划—控制层次，将语言条件语义与底层机器人动作结合在同一模型中。VLA 往往由在 web-scale 数据集上预训练的大型视觉—语言模型（VLM）初始化。尽管它们推进了视觉—语义知识迁移的前沿，但这些模型预训练于静态图像—文本数据集，因此很难继承将知识迁移到新物理技能所需的时空先验。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Generalization in VLAs.** Generalization in VLAs has been mostly demonstrated at the object and semantic level (Brohan et al., 2023; Gao et al., 2025), while generalization to completely new skills and environments has remained limited. In particular, existing work utilizing VLAs achieves environment generalization by collecting human teleoperation data across hundreds of diverse environments for specific tasks (Physical Intelligence, 2025). Furthermore, while current VLAs attempt to achieve task generalization by covering a large library of language-conditioned motion primitives (Gemini Robotics Team, 2025), this approach is fundamentally constrained by the impracticality of capturing the vast amount of possible physical interactions and motions with a fixed set of episode-level language-conditioned tasks. In contrast, video-based world models learn from every consecutive frame pair in the data, while also leveraging large-scale video pretraining to understand physical dynamics.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **VLA 中的泛化。** VLA 的泛化主要在物体层面和语义层面得到证明（Brohan et al., 2023; Gao et al., 2025），但其向完全全新的技能和环境泛化的能力仍然有限。特别是，现有 VLA 工作通过针对特定任务，在数百个多样环境中采集人类遥操数据来实现环境泛化（Physical Intelligence, 2025）。此外，尽管当前 VLA 试图通过覆盖大量语言条件运动原语来实现任务泛化（Gemini Robotics Team, 2025），但固定数量的 episode 级语言条件任务不可能捕获数量庞大的潜在物理交互与运动，这从根本上限制了该方法。相比之下，基于视频的世界模型从数据中的每对连续帧学习，同时还能利用大规模视频预训练理解物理动力学。

## 2.2. Video Model-based Robot Policies

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Video Generation in Robotics.** Prior works show that video generation models can be used to synthesize robot trajectories and extract executable actions at test-time through various approaches: inverse-dynamics models (Du et al., 2023; Zhou et al., 2024), optical flow as dense correspondence (Ko et al., 2024), or trajectory prediction as high-level planning (Du et al., 2024; Yang et al., 2024). Other works generate human videos—either with 3D tracking (Liang et al., 2024) or for novel scenes and motions (Bharadhwaj et al., 2024; Chen et al., 2025)—and train policies using point tracking objectives. Most recently, Jang et al. (2025) and Luo et al. (2025) demonstrated that video generation models can produce synthetic robot data for unseen behaviors in novel environments, leveraging the strong generalization capabilities of these models.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **机器人中的视频生成。** 既有工作表明，视频生成模型可用于合成机器人轨迹，并在测试时通过多种方法提取可执行动作：逆动力学模型（Du et al., 2023; Zhou et al., 2024）、作为稠密对应的光流（Ko et al., 2024），或作为高层规划的轨迹预测（Du et al., 2024; Yang et al., 2024）。另一些工作生成人类视频，或者配合 3D 跟踪（Liang et al., 2024），或者生成新场景和新动作（Bharadhwaj et al., 2024; Chen et al., 2025），再利用点跟踪目标训练策略。最近，Jang et al. (2025) 和 Luo et al. (2025) 证明，借助视频生成模型的强泛化能力，可以为新环境中的未见行为生成合成机器人数据。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Joint Video and Action Generation.** Another line of work couples video and action generation for end-to-end learning. These methods demonstrate that incorporating a world modeling objective alongside action prediction improves multi-task performance, sample efficiency, and generalization to novel scenes and objects. Previous work (Cheang et al., 2024; Li et al., 2025; Won et al., 2025; Wu et al., 2024; Zhao et al., 2025; Zheng et al., 2025; Zhu et al., 2025) learns joint world modeling and action prediction from scratch or from VLAs, while more recent work (Hu et al., 2024; Kim et al., 2026; Liang et al., 2025; Liao et al., 2025; Pai et al., 2025) leverages pretrained video diffusion models to inherit rich visual dynamics priors. We refer to these models collectively as World Action Models (WAMs), since they leverage world modeling capability (predicting the future state) for action prediction. We use the term World Action Models (WAMs) rather than Video Action Models (VAMs) to reflect that video is just one possible world modeling objective—future WAMs may align actions with other predictive modalities such as tactile sensing, force feedback, or learned latent representations. In contrast to prior WAMs, DreamZero systematically explores data diversity and scale to expose the full generalization potential of WAMs, adopts an autoregressive architecture better suited for long-horizon world–action modeling, achieves state-of-the-art generalization across both novel tasks and environments, and achieves state-of-the-art cross-embodiment transfer, both learning from different embodiments (video only) and few-shot adaptation to a new embodiment.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **联合视频与动作生成。** 另一条路线把视频生成与动作生成耦合起来进行端到端学习。这些方法表明，在动作预测之外加入世界建模目标，可提升多任务性能、样本效率，以及对新场景与新物体的泛化。早期工作（Cheang et al., 2024; Li et al., 2025; Won et al., 2025; Wu et al., 2024; Zhao et al., 2025; Zheng et al., 2025; Zhu et al., 2025）从零开始或从 VLA 初始化，联合学习世界建模与动作预测；较新的工作（Hu et al., 2024; Kim et al., 2026; Liang et al., 2025; Liao et al., 2025; Pai et al., 2025）则利用预训练视频扩散模型，以继承丰富的视觉动力学先验。我们将这些模型统称为世界动作模型（WAM），因为它们利用世界建模能力（预测未来状态）来预测动作。我们使用 World Action Model（WAM）而非 Video Action Model（VAM）这一名称，旨在表明视频只是可能的世界建模目标之一；未来 WAM 也可以将动作与触觉感知、力反馈或学到的潜在表示等其他预测模态对齐。与既有 WAM 不同，DreamZero 系统探索数据多样性与规模，以揭示 WAM 的完整泛化潜力；采用更适合长时域世界—动作建模的自回归架构；在新任务和新环境上都实现最先进泛化；并在纯视频异形态学习和对新形态的少样本适配两方面均实现最先进的跨机器人形态迁移。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Why WAMs.** WAMs built upon video diffusion backbones inherit rich spatiotemporal priors from web-scale data, capturing the best of both paradigms: the seamless gradient flow of end-to-end VLAs and dense world modeling supervision for planning. Unlike latent world models (Assran et al., 2025; Hafner et al., 2019, 2020, 2023), which learn dynamics from scratch in compact latent spaces, WAMs leverage pretrained video representations that already encode physical dynamics from internet-scale data. Central to this approach is learning the joint distribution of video and action—DreamZero simultaneously learns both modalities, with video prediction serving as an implicit visual planner that guides action generation. This formulation not only means that improving robotic capabilities reduces to improving video generation, but also enables three capabilities that elude current VLAs: zero-shot generalization to novel tasks, effective learning from heterogeneous robot data, and extremely efficient cross-embodiment transfer from videos. We provide further discussion about the differences between WAMs and alternative world model architectures (e.g., latent-space, 3D point cloud) in Appendix A.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **为何选择 WAM。** 基于视频扩散骨干的 WAM 从 web-scale 数据中继承丰富的时空先验，因而结合了两种范式的优点：端到端 VLA 的无缝梯度流，以及面向规划的稠密世界建模监督。与在紧凑潜在空间中从零学习动力学的潜在世界模型（Assran et al., 2025; Hafner et al., 2019, 2020, 2023）不同，WAM 利用预训练视频表示，后者已经编码了互联网规模数据中的物理动力学。该方法的核心是学习视频与动作的联合分布：DreamZero 同时学习两种模态，视频预测则作为隐式视觉规划器指导动作生成。这一形式化不仅意味着“提升机器人能力”可归结为“提升视频生成”，还带来当前 VLA 所不具备的三种能力：对新任务的零样本泛化、从异构机器人数据中有效学习，以及基于视频的极高效跨机器人形态迁移。附录 A 将进一步讨论 WAM 与其他世界模型架构（例如潜在空间、3D 点云）的区别。

## Figure 4. Model Architecture of DreamZero / DreamZero 的模型架构

![Figure 4](WorldModel/World%20Action%20Models%20are%20Zero-shot%20Policies/assets/page_006_fig_figure_4.png)

**Caption:** Model Architecture of DreamZero. The model takes three inputs: visual context (encoded via a VAE), language instructions (via a text encoder), and proprioceptive state (via a state encoder). These are processed by an autoregressive DiT backbone using flow matching, which jointly predicts future video frames and actions through separate decoders. During training (left), for each chunk, the model denoises noisy video and action latents conditioned on clean video context. During inference (right), predictions are executed asynchronously in the real world, and ground-truth observations are fed back into the KV cache to prevent error accumulation.

**Caption[CN]:** DreamZero 的模型架构。模型接收三种输入：视觉上下文（通过 VAE 编码）、语言指令（通过文本编码器）以及本体感受状态（通过状态编码器）。它们由使用流匹配的自回归 DiT 骨干处理，再经不同解码器联合预测未来视频帧和动作。训练时（左），对于每个块，模型都在干净视频上下文条件下对含噪视频与动作潜变量去噪。推理时（右），预测在真实世界中异步执行，并将真值观测反馈到 KV 缓存中，以防止错误累积。

# 3. DreamZero

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Pretrained video diffusion models offer rich spatiotemporal priors from web-scale data, making them attractive backbones for robot policies. However, converting these models into effective World Action Models (WAMs) presents three key challenges: (1) **Video-action alignment:** jointly predicting video and actions requires tight coupling between visual futures and motor commands, yet naively combining separate video and action heads can lead to misalignment; (2) **Architectural design:** it remains unclear whether bidirectional or autoregressive architectures are better suited for WAMs, with implications in modality alignment, error accumulation, and inference efficiency; and (3) **Real-time inference:** video diffusion models require iterative denoising across high-dimensional latent spaces, making them prohibitively slow for closed-loop control.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 预训练视频扩散模型从 web-scale 数据中获得丰富的时空先验，因而很适合作为机器人策略的骨干。然而，将这些模型转化为有效的世界动作模型（WAM）需要面对三项关键挑战：（1）**视频—动作对齐：**联合预测视频和动作要求视觉未来与运动指令紧密耦合，但朴素地组合彼此分离的视频头和动作头可能导致错位；（2）**架构设计：**双向架构还是自回归架构更适合 WAM 仍不清楚，而这会影响模态对齐、错误累积和推理效率；以及（3）**实时推理：**视频扩散模型需在高维潜在空间中迭代去噪，因而对闭环控制而言过于缓慢。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> DreamZero addresses these challenges through three design choices. First, we train a single end-to-end model that jointly denoises video and action with a shared objective, ensuring deep integration between modalities. Second, we adopt an autoregressive architecture and exploit the closed-loop setting: after each action chunk is executed, we replace predicted frames with ground-truth observations in the KV cache, eliminating compounding errors while enabling efficient inference via KV caching and preserving native frame rates for precise modality alignment (see the right side of Figure 4). Third, we introduce a suite of system-, implementation-, and model-level optimizations that achieve a 38× inference speedup, enabling real-time control at 7Hz. We detail the model architecture in Section 3.1 and real-time execution in Section 3.2.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> DreamZero 通过三项设计选择应对这些挑战。首先，我们训练单一端到端模型，使其用共享目标联合对视频和动作去噪，从而保证模态间的深度整合。其次，我们采用自回归架构并利用闭环设定：执行完每个动作块后，我们在 KV 缓存中用真值观测替换预测帧，从而在消除错误累积的同时，通过 KV 缓存进行高效推理，并保留原生帧率以实现精确模态对齐（见 Figure 4 右侧）。第三，我们提出一系列系统级、实现级和模型级优化，实现 38 倍推理加速，从而支持 7Hz 实时控制。我们将在第 3.1 节详述模型架构，并在第 3.2 节详述实时执行。

## 3.1. Model Architecture

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Problem Formulation.** DreamZero jointly predicts video $o_{l:l+H}$ and actions $a_{l:l+H}$ conditioned on language instruction $c$, proprioceptive state $q_l$, and visual observations including the current and past history $o_{0:l}$, where $H>0$ is a fixed horizon and $l$ is a random index sampled from a trajectory. Note that joint prediction of video and action is a decomposition of (1) autoregressive video prediction and (2) action prediction from an inverse-dynamics model (IDM):

$$
\underbrace{\pi_0\!\left(o_{l:l+H},a_{l:l+H}\mid o_{0:l},c,q_l\right)}_{\text{DreamZero}}
=
\underbrace{\pi_0\!\left(o_{l:l+H}\mid o_{0:l},c,q_l\right)}_{\text{video prediction}}
\underbrace{\pi_0\!\left(a_{l:l+H}\mid o_{0:l+H},q_l\right)}_{\text{IDM}}.
\tag{1}
$$

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **问题形式化。** DreamZero 在语言指令 $c$、本体感受状态 $q_l$ 以及包括当前时刻和过去历史在内的视觉观测 $o_{0:l}$ 条件下，联合预测视频 $o_{l:l+H}$ 和动作 $a_{l:l+H}$，其中 $H>0$ 是固定时域，$l$ 是从一条轨迹中随机采样的索引。注意，视频与动作的联合预测可分解为：（1）自回归视频预测；以及（2）来自逆动力学模型（IDM）的动作预测，如式（1）所示。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Instead of using two separate models (a video prediction model and an inverse dynamics model) to model the decomposed objective (Li et al., 2026; Pai et al., 2025), we train a single model end-to-end with a joint prediction objective. We believe that this end-to-end design enables better video-action alignment through deep integration between the two modalities. Since pretrained video models are already optimized on the video prediction objective on diverse web-scale video data, DreamZero only needs to additionally learn to predict videos for robot embodiment videos and extract corresponding actions from the generated videos. We further hypothesize that this encourages better generalization than the conventional practice of training a VLA from a VLM, as our approach explicitly learns temporal dynamics from video frames used both as conditioning inputs and prediction targets.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 我们不是使用两个分离的模型（视频预测模型和逆动力学模型）建模这一分解目标（Li et al., 2026; Pai et al., 2025），而是用联合预测目标端到端训练单一模型。我们认为，这种端到端设计通过两种模态的深度整合，可实现更好的视频—动作对齐。由于预训练视频模型已经在多样的 web-scale 视频数据上针对视频预测目标做过优化，DreamZero 只需进一步学会预测机器人形态视频，并从生成视频中提取对应动作。我们进一步假设，这比常规的“从 VLM 训练 VLA”做法更有利于泛化，因为我们的方法从同时用作条件输入和预测目标的视频帧中显式学习时间动力学。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Model Architecture.** The model architecture is shown in Figure 4. To retain the generalization capability of video models, we introduce minimal additional parameters: state encoders, action encoders, and decoders. For robot training data that contains multiple views, we concatenate all views into a single frame instead of making architectural changes to the backbone model.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **模型架构。** 模型架构如 Figure 4 所示。为保留视频模型的泛化能力，我们只引入了少量额外参数：状态编码器、动作编码器和解码器。对于包含多个视角的机器人训练数据，我们把所有视角拼接为单帧，而不改变骨干模型架构。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> In particular, DreamZero is trained to predict video frames and corresponding actions autoregressively. Autoregressive generation possesses the following advantages: (1) it enables faster inference by utilizing KV-cache; (2) the policy model can leverage visual observation history as guidance for the next generation; and (3) it avoids the modality-alignment challenges (video, action, and language alignment) inherent to bidirectional models. Concretely, bidirectional diffusion typically requires processing fixed-length sequences, which often necessitates video subsampling that distorts native FPS, potentially harming video-action alignment. On the other hand, autoregressive generation leverages KV caching to support arbitrarily long contexts within a single forward pass. This preserves the native frame rate, ensuring precise alignment between video frames and robot actions. Further illustration of this difference is provided in Appendix B.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 具体而言，DreamZero 被训练为以自回归方式预测视频帧和对应动作。自回归生成有如下优势：（1）可利用 KV 缓存实现更快的推理；（2）策略模型可利用视觉观测历史来指导下一次生成；以及（3）可避免双向模型固有的模态对齐难题（视频、动作与语言对齐）。具体来说，双向扩散通常需要处理固定长度序列，因此往往必须对视频进行子采样，这会扭曲原生 FPS，并可能损害视频—动作对齐。相反，自回归生成利用 KV 缓存，在单次前向计算中支持任意长上下文。这保留了原生帧率，保证视频帧与机器人动作精确对齐。附录 B 将进一步说明这一差异。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> We introduce autoregressive modeling only for the video modality to avoid error propagation coming from closed-loop action prediction. DreamZero is trained to predict video frames in a chunk-wise manner; each chunk has a fixed number of latent frames $K$ to match the action horizon. Chunk-wise generation enables training on videos of variable length, similar to how LLMs are trained on language-token sequences of variable length. We provide more details on the QKV attention-masking strategy for the different modalities in Appendix C.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 我们只为视频模态引入自回归建模，以避免来自闭环动作预测的错误传播。DreamZero 以分块方式预测视频帧；每个块都含有固定数量的潜在帧 $K$，用以匹配动作时域。分块生成使模型能在变长视频上训练，类似于 LLM 在变长语言 token 序列上训练的方式。附录 C 提供了不同模态 QKV 注意力遮罩策略的更多细节。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Training Objective.** Similar to recent video diffusion models and VLAs, we employ flow matching (Albergo et al., 2023; Lipman et al., 2022; Liu et al., 2022) as the training objective (Ali et al., 2025; Team Wan, 2025; Teng et al., 2025). Unlike recent WAMs (Kim et al., 2026; Li et al., 2025; Liao et al., 2025; Zhu et al., 2025), DreamZero shares the denoising timestep between the video and action modalities for faster convergence at the beginning of training. We also apply teacher forcing (Gao et al., 2024; Jin et al., 2024) as a training objective: the model is trained to denoise the noisy current chunk conditioned on clean previous chunks.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **训练目标。** 与近期视频扩散模型和 VLA 类似，我们使用流匹配（Albergo et al., 2023; Lipman et al., 2022; Liu et al., 2022）作为训练目标（Ali et al., 2025; Team Wan, 2025; Teng et al., 2025）。与近期 WAM（Kim et al., 2026; Li et al., 2025; Liao et al., 2025; Zhu et al., 2025）不同，DreamZero 使视频与动作模态共享去噪时间步，以在训练初期更快收敛。我们还把教师强制（Gao et al., 2024; Jin et al., 2024）用作训练目标：模型在干净历史块条件下，学习对当前含噪块去噪。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Formally, given a chunk index $k>0$ and denoising timestep $t_k\in[0,1]$, we denote the corresponding noisy video latent vector for original video $o^k$ as $z^k_{t_k}$ and noisy normalized actions as $a^k_{t_k}$. All frames within the same chunk share the same timestep $t_k$, while different chunks are assigned independent timesteps. Our model denoises $z^k_{t_k}$ and $a^k_{t_k}$, defined as linear interpolations between clean vectors and random Gaussian noises:

$$
z^k_{t_k}=t_k z^k_1+(1-t_k)z^k_0,
\qquad
a^k_{t_k}=t_k a^k_1+(1-t_k)a^k_0.
\tag{2}
$$

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 形式化地说，给定块索引 $k>0$ 和去噪时间步 $t_k\in[0,1]$，我们将原始视频 $o^k$ 所对应的含噪视频潜向量记为 $z^k_{t_k}$，将含噪归一化动作记为 $a^k_{t_k}$。同一块内的所有帧共享同一时间步 $t_k$，不同块则被赋予相互独立的时间步。模型对 $z^k_{t_k}$ 和 $a^k_{t_k}$ 去噪，两者按式（2）定义为干净向量与随机高斯噪声之间的线性插值。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Here $z^k_0\sim\mathcal{N}(0,I)$, $a^k_0\sim\mathcal{N}(0,I)$, and $z^k_1$ and $a^k_1$ are a clean video latent vector and a normalized action, respectively. Thus, the clean context from previous chunks can be denoted as $\mathcal{C}_k=\{(z^j_1,a^j_1)\}_{j=1}^{k-1}$. We train the model $u_\theta$ to predict the joint velocity for both modalities using the following flow-matching objective:

$$
\mathcal{L}(\theta)
=
\mathbb{E}_{z,a,\{t_k\}}
\left[
\frac{1}{K}\sum_{k=1}^{K}
w(t_k)
\left\|
u_\theta\!\left([z^k_{t_k},a^k_{t_k}];\mathcal{C}_k,c,q_k,t_k\right)-v_k
\right\|^2
\right].
\tag{3}
$$

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 其中 $z^k_0\sim\mathcal{N}(0,I)$、$a^k_0\sim\mathcal{N}(0,I)$，而 $z^k_1$ 和 $a^k_1$ 分别是干净视频潜向量与归一化动作。因此，来自之前各块的干净上下文可记为 $\mathcal{C}_k=\{(z^j_1,a^j_1)\}_{j=1}^{k-1}$。我们用式（3）的流匹配目标训练模型 $u_\theta$，使其预测两种模态的联合速度。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Here $w(t_k)>0$ is a predefined weight function for $t_k$, $c$ is the text condition, $q_k$ is the proprioceptive state of the $k$-th chunk, and the velocity is $v_k:=[z^k_1,a^k_1]-[z^k_0,a^k_0]$. To enable efficient training, we perform trajectory-level updates and apply attention masking (see, e.g., Figure 14 for details) so that the current noisy chunk can attend to clean context from previous chunks. We provide pseudocode in Algorithm 1.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 其中 $w(t_k)>0$ 是针对 $t_k$ 预定义的权重函数，$c$ 是文本条件，$q_k$ 是第 $k$ 个块的本体感受状态，速度为 $v_k:=[z^k_1,a^k_1]-[z^k_0,a^k_0]$。为了高效训练，我们进行轨迹级更新，并应用注意力遮罩（例如详见 Figure 14），使当前含噪块可以关注之前各块的干净上下文。Algorithm 1 给出了伪代码。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> **Model Inference.** As shown in Figure 4, during inference DreamZero jointly denoises video and action chunks, leveraging KV caching for efficiency (Huang et al., 2025; Teng et al., 2025; Yin et al., 2025). Unlike pure video generation, our closed-loop setting allows ground-truth observations to replace generated frames in the KV cache after each action execution (see Figure 14). This eliminates the compounding-error problem inherent to autoregressive video generation—a key advantage unique to WAMs. Moreover, as a stateful policy, DreamZero can leverage visual history for tasks requiring memory. We provide inference pseudocode in Algorithm 2.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> **模型推理。** 如 Figure 4 所示，推理期间 DreamZero 联合对视频块和动作块去噪，并利用 KV 缓存提高效率（Huang et al., 2025; Teng et al., 2025; Yin et al., 2025）。与纯视频生成不同，我们的闭环设定允许在每次执行动作后，以真值观测替换 KV 缓存中的生成帧（见 Figure 14）。这消除了自回归视频生成固有的错误累积问题，是 WAM 独有的关键优势。此外，作为有状态策略，DreamZero 可利用视觉历史完成需要记忆的任务。Algorithm 2 给出了推理伪代码。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> **Footnote 2.** In this work, we do not explicitly evaluate or post-train DreamZero on tasks that can only succeed with memory. We leave this for future work.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> **脚注 2。** 在本工作中，我们并未在只有依靠记忆才能成功的任务上显式评测或后训练 DreamZero。我们将此留作未来工作。

## 3.2. Real-time Execution of DreamZero

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Diffusion-based WAMs inherit powerful generalization from video foundation models, but their iterative denoising process creates a fundamental tension with reactive robotic control. We address two questions: (1) What prevents WAMs from being reactive policies? (2) How do we resolve this for real-time control?

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 基于扩散的 WAM 从视频基础模型继承了强大泛化能力，但其迭代去噪过程与反应式机器人控制之间存在根本性张力。我们回答两个问题：（1）是什么阻止 WAM 成为反应式策略？（2）我们如何解决这一问题以实现实时控制？

### 3.2.1. The Reactivity Gap

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Reactive policies must respond to environmental changes within tens of milliseconds. A naive implementation of DreamZero on a single GPU requires approximately 5.7 seconds per action chunk due to three bottlenecks: (1) iterative denoising across 16 diffusion steps required for smooth actions, (2) the computational cost of a 14B-parameter DiT backbone, and (3) sequential execution that blocks robot motion during inference. This latency makes closed-loop control infeasible.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 反应式策略必须在数十毫秒内响应环境变化。DreamZero 在单张 GPU 上的朴素实现每个动作块大约需要 5.7 秒，源于三个瓶颈：（1）平滑动作需要 16 个扩散步的迭代去噪；（2）14B 参数 DiT 骨干的计算成本；以及（3）推理期间阻塞机器人运动的串行执行。这一延迟使闭环控制无法实现。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Footnote 3.** One might expect that generating only actions (not video) would accelerate inference, but at 14B scale we empirically found that the speed gain is minimal—the number of diffusion steps and the number of DiT blocks dominate latency. Moreover, because video and action are jointly trained for strong cross-modal alignment, naively reducing action denoising steps degrades quality. This motivates DreamZero-Flash.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **脚注 3。** 人们可能预期只生成动作（而不生成视频）会加快推理，但我们通过实验发现，在 14B 规模上，这样做的速度收益很小：扩散步数和 DiT block 数量主导延迟。此外，由于视频和动作为强跨模态对齐而联合训练，朴素地减少动作去噪步数会降低质量。这一现象促成了 DreamZero-Flash。

### 3.2.2. Asynchronous Closed-Loop Execution

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Our first step toward resolving this is asynchronous execution that decouples inference from action execution. Rather than waiting for each inference to complete, the motion controller continuously executes the most recent action chunk while inference runs concurrently on the latest observation. This structure transforms the latency constraint from “inference must complete before the robot moves” to “inference must complete before the current action chunk expires.” In our experiments, we deploy policies at an action horizon of 48 steps at a 30Hz control frequency (1.6 seconds per chunk) for bimanual manipulation robots. Hence, we target inference latency below approximately 200ms to ensure sufficient overlap for smooth, reactive control.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 我们解决这一问题的第一步是使用异步执行，将推理与动作执行解耦。运动控制器不再等待每次推理完成，而是持续执行最新动作块，同时针对最新观测并发推理。这一结构把延迟约束从“机器人运动前必须完成推理”转变为“当前动作块到期前必须完成推理”。在实验中，我们为双臂操作机器人部署动作时域为 48 步、控制频率为 30Hz 的策略（每块 1.6 秒）。因此，我们把推理延迟目标设为约 200ms 以下，以保证有足够重叠来进行平滑、反应式控制。

### 3.2.3. System-level Optimizations

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Given the asynchronous execution structure, we optimize inference throughput through parallelism and caching.
>
> - **CFG Parallelism.** Classifier-free guidance (Ho and Salimans, 2022) requires two forward passes (conditional and unconditional). We distribute these across two GPUs, reducing per-step latency by 47%.
> - **DiT Caching.** We exploit the directional consistency of velocity predictions during flow matching. When cosine similarity between successive velocities exceeds a threshold, we reuse cached velocities, reducing effective DiT steps from 16 to 4 with minimal quality loss on action prediction.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 在这一异步执行结构下，我们通过并行与缓存优化推理吞吐量。
>
> - **CFG 并行。** 无分类器引导（Ho and Salimans, 2022）需要两次前向计算（有条件和无条件）。我们将其分布在两张 GPU 上，使每步延迟减少 47%。
> - **DiT 缓存。** 我们利用流匹配过程中速度预测的方向一致性。当相邻速度之间的余弦相似度超过阈值时，我们复用已缓存速度，把有效 DiT 步数从 16 减至 4，而动作预测质量损失很小。

### 3.2.4. Implementation-level Optimizations

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> We further reduce latency through compiler and kernel enhancements.
>
> - **Torch Compile and CUDA Graphs.** We apply `torch.compile` with CUDA Graphs to eliminate CPU overhead and fuse operators. Static shapes cause recompilations only during the first trajectory.
> - **Post-Training Quantization.** On Blackwell architecture, we quantize weights and activations to NVFP4 while keeping sensitive operations (QKV, Softmax) in FP8 and nonlinear operations in FP16.
> - **Kernel and Scheduler Enhancements.** We use the cuDNN backend for attention and migrate scheduler operations to GPU to eliminate CPU–GPU synchronization stalls.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 我们进一步通过编译器与内核增强减少延迟。
>
> - **Torch Compile 与 CUDA Graphs。** 我们将 `torch.compile` 与 CUDA Graphs 结合，以消除 CPU 开销并融合算子。静态 shape 使重新编译只发生在第一条轨迹期间。
> - **训练后量化。** 在 Blackwell 架构上，我们将权重与激活量化为 NVFP4，同时使敏感操作（QKV、Softmax）保持 FP8，非线性操作保持 FP16。
> - **内核与调度器增强。** 我们使用 cuDNN 后端计算注意力，并将调度器操作迁移至 GPU，以消除 CPU–GPU 同步停顿。

## Figure 5. Decoupled Noise Schedules / 解耦噪声日程

![Figure 5](assets/page_009_fig_figure_5.png)

**Caption:** Decoupled Noise Schedules. DreamZero (blue) uses coupled noise for video and action (both uniform). DreamZero-Flash (red) biases video toward high-noise states via a Beta distribution while keeping action noise uniform, training the model to predict clean actions from noisy visual context.

**Caption[CN]:** 解耦噪声日程。DreamZero（蓝色）对视频和动作使用耦合噪声（二者均均匀）。DreamZero-Flash（红色）通过 Beta 分布使视频偏向高噪声状态，同时保持动作噪声均匀，从而训练模型从含噪视觉上下文预测干净动作。

### 3.2.5. Model-level Optimizations: DreamZero-Flash

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Even with system optimizations, the number of diffusion steps remains the primary latency bottleneck. However, naively reducing steps degrades action quality because residual visual noise propagates into action predictions. DreamZero-Flash addresses this by decoupling video and action noise schedules during training. The key insight is that, at inference time, actions should denoise to their final values while being conditioned on a still-noisy video representation within the current chunk, since with very few denoising steps (e.g., fewer than 4), the generated video tokens may remain inaccurate and thus provide a noisy conditioning signal. Standard DreamZero samples a shared timestep $t_k\sim\mathcal{U}(0,1)$ for both modalities. This creates a train–test mismatch: during training, the model learns to predict actions when video and action are at the same noise level, but few-step or single-step inference requires predicting clean actions while video remains partially noisy.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 即使经过系统优化，扩散步数仍是主要延迟瓶颈。然而，朴素地减少步数会降低动作质量，因为残留视觉噪声会传播到动作预测。DreamZero-Flash 通过在训练时解耦视频与动作噪声日程来解决此问题。关键洞察是：推理时，动作应在当前块内仍然含噪的视频表示条件下去噪至最终值；这是因为当去噪步数很少（例如少于 4）时，生成视频 token 仍可能不准确，从而产生带噪条件信号。标准 DreamZero 为两种模态采样共享时间步 $t_k\sim\mathcal{U}(0,1)$。这会造成训练—测试错配：训练时，模型学习在视频和动作处于同一噪声水平时预测动作；但少步或单步推理要求在视频仍部分含噪时预测干净动作。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> DreamZero-Flash closes this gap by biasing video timesteps toward high-noise states via $t^{\mathrm{video}}=1-\eta$, where $\eta\sim\mathrm{Beta}(\alpha,\beta)$ with $\alpha>\beta$. In practice, we use $\mathrm{Beta}(7,1)$ as an example configuration, yielding $\mathbb{E}[t^{\mathrm{video}}]=0.125$ (predominantly noisy), while action timesteps remain uniform (Figure 5). During training, this exposes the model to configurations where it must predict clean actions from noisy visual context, directly matching the few-step or single-step inference regime. As a result, we reduce diffusion steps from four to one, cutting inference from $\sim$350ms to $\sim$150ms with minimal performance loss (Table 3). Moreover, the Flash formulation enables flexible training configurations—such as varying the noise-sampling ratios of video and action—to better align training with different few-step or single-step inference regimes. In practice, we mainly apply Flash training as the final stage following the main DreamZero model training.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> DreamZero-Flash 通过 $t^{\mathrm{video}}=1-\eta$ 使视频时间步偏向高噪声状态，从而弥合这一差距；其中 $\eta\sim\mathrm{Beta}(\alpha,\beta)$ 且 $\alpha>\beta$。实际中，我们以 $\mathrm{Beta}(7,1)$ 作为示例配置，得到 $\mathbb{E}[t^{\mathrm{video}}]=0.125$（主要处于高噪声），动作时间步则保持均匀（Figure 5）。训练期间，模型因而会遇到必须从含噪视觉上下文预测干净动作的配置，这直接匹配少步或单步推理情形。因此，我们把扩散步数从 4 减少到 1，将推理时间从约 350ms 降至约 150ms，而性能损失很小（Table 3）。此外，Flash 形式允许灵活训练配置，例如改变视频和动作的噪声采样比例，以便训练能更好地对齐不同少步或单步推理情形。实际中，我们主要把 Flash 训练作为主 DreamZero 模型训练之后的最终阶段。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **Action Chunk Smoothing.** To suppress high-frequency noise in generated actions, we upsample chunks to $2\times$ resolution, apply a Savitzky–Golay filter, and downsample to the original resolution.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **动作块平滑。** 为抑制生成动作中的高频噪声，我们先将块上采样到 $2\times$ 分辨率，应用 Savitzky–Golay 滤波器，然后下采样回原始分辨率。

### 3.2.6. Summary

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> Table 1 summarizes cumulative speedups. System and implementation optimizations yield $\sim$9× speedup on H100 and $\sim$16× on GB200; adding DreamZero-Flash achieves 38× on GB200, reducing latency from 5.7s to 150ms. With the exception of DiT caching and quantization, all system- and implementation-level optimizations are mathematically equivalent to the baseline and show no measurable performance degradation.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> Table 1 汇总了累计加速比。系统与实现优化在 H100 上实现约 9 倍加速，在 GB200 上实现约 16 倍加速；加入 DreamZero-Flash 后，GB200 上达到 38 倍，将延迟从 5.7s 降至 150ms。除 DiT 缓存和量化之外，所有系统级与实现级优化都在数学上与 baseline 等价，且未显示可测量的性能下降。

## Table 1. Cumulative inference speedups / 累计推理加速比

| Optimization / 优化 | H100 | GB200 |
|---|---:|---:|
| Baseline | 1× | 1.1× |
| *System-level* / *系统级* |  |  |
| + CFG Parallelism | 1.9× | 1.8× |
| + DiT Caching | 5.5× | 5.4× |
| *Implementation-level* / *实现级* |  |  |
| + Torch Compile + CUDA Graphs | 8.9× | 10.9× |
| + Kernel & Scheduler Opts. | 9.6× | 14.8× |
| + Quantization (NVFP4) | — | 16.6× |
| *Model-level* / *模型级* |  |  |
| + DreamZero-Flash | — | 38× |

**Caption:** Cumulative inference speedups. Each row includes all optimizations above it. Entries marked “—” indicate features not applicable to that hardware.

**Caption[CN]:** 累计推理加速比。每一行均包含该行之上的全部优化。标记为“—”的项表示该功能不适用于相应硬件。

# 4. Experimental Setup

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We validate our main hypotheses about learning from diverse data on two robot embodiments: the AgiBot G1 mobile bimanual manipulator and the Franka single-arm robot. We pretrain separately for each embodiment, leaving multi-embodiment training for future work. For cross-embodiment experiments, we utilize both the YAM robot and human egocentric data. The experimental setup for AgiBot G1 is illustrated in Figure 7.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们在两种机器人形态上验证有关“从多样数据中学习”的主要假设：AgiBot G1 移动双臂操作机器人与 Franka 单臂机器人。我们针对每一形态分别进行预训练，将多形态联合训练留作未来工作。在跨机器人形态实验中，我们使用 YAM 机器人和人类第一视角数据。AgiBot G1 的实验设置如 Figure 7 所示。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> We compare against two state-of-the-art Vision-Language-Action models (VLAs): GR00T N1.6 (Bjorck et al., 2025) and $\pi_{0.5}$ (Physical Intelligence, 2025). For each baseline, we evaluate two initialization strategies: (1) **from-scratch**, using pretrained VLM weights without prior robot-data training for a fair apple-to-apple comparison with DreamZero, and (2) **from-pretrained**, using official checkpoints pretrained on thousands of hours of cross-embodiment robot data. Both variants are then trained on identical data as DreamZero: $\sim$500 hours of teleoperation data we collected for AgiBot G1, and DROID (Khazatsky et al., 2024) for Franka. We keep the compute budget comparable across all methods by matching total batch size and gradient steps.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 我们与两个最先进的视觉—语言—动作模型（VLA）比较：GR00T N1.6（Bjorck et al., 2025）和 $\pi_{0.5}$（Physical Intelligence, 2025）。对于每个 baseline，我们评估两种初始化策略：（1）**from-scratch**：使用预训练 VLM 权重，但之前不进行机器人数据训练，以便同 DreamZero 进行公平的同类比较；（2）**from-pretrained**：使用在数千小时跨机器人形态数据上预训练的官方 checkpoint。随后，这两种变体在与 DreamZero 完全相同的数据上训练：对 AgiBot G1 使用我们收集的约 500 小时遥操数据，对 Franka 使用 DROID（Khazatsky et al., 2024）。我们通过匹配总 batch size 和梯度步数，使所有方法的计算预算可比。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Footnote 4.** For from-pretrained baselines, this constitutes continual training on top of the official weights.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **脚注 4。** 对于 from-pretrained baseline，这构成了在官方权重之上进行的持续训练。

## 4.1. Pretraining

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Data.** Our data-collection philosophy differs from that of existing VLAs. While recent works have shown that VLAs can learn effective policies from moderate-sized datasets, these approaches typically rely on structured, task-focused demonstrations to ensure consistent behavior. We hypothesize that learning only to predict actions without encoding knowledge about future world states makes it challenging to leverage highly heterogeneous, non-repetitive data effectively, as the model must implicitly infer dynamics from noisy state–action pairs. In contrast, we hypothesize that DreamZero's world-modeling objective enables effective learning from diverse demonstrations, allowing us to prioritize breadth and utility over repetition during data collection.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **数据。** 我们的数据收集理念与现有 VLA 不同。尽管近期工作表明 VLA 可从中等规模数据集中学到有效策略，但这些方法通常依赖结构化、聚焦于特定任务的示范来保证行为一致性。我们假设，如果只学习预测动作，却不编码有关未来世界状态的知识，便很难有效利用高度异构、非重复数据，因为模型必须从含噪状态—动作对中隐式推断动力学。相比之下，我们假设 DreamZero 的世界建模目标能从多样示范中有效学习，因而允许我们在数据收集时把广度与效用置于重复性之上。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Using AgiBot G1, we collect approximately 500 hours of teleoperation data across 22 unique environments (see Figure 15), including homes, restaurants, supermarkets, coffee shops, and offices—prioritizing task diversity and real-world utility over task-specific repetition. As shown in Figure 6, each episode averages around 4.4 minutes and encompasses approximately 42 subtasks—significantly longer-horizon than typical robotic manipulation datasets (Khazatsky et al., 2024; Walke et al., 2023). The skill distribution reflects real-world deployment requirements: navigation enables movement between workspaces, while torso adjustments allow interaction with objects at varying heights (shelves, cabinets). Additional details on the data-collection pipeline are provided in Appendix E.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 我们使用 AgiBot G1 在 22 个独立环境中收集了约 500 小时遥操数据（见 Figure 15），涵盖住宅、餐厅、超市、咖啡馆和办公室；数据收集优先考虑任务多样性和真实世界效用，而非任务专用重复。如 Figure 6 所示，每个 episode 平均持续约 4.4 分钟，并包含约 42 个子任务；这比典型机器人操作数据集的时域长得多（Khazatsky et al., 2024; Walke et al., 2023）。技能分布反映了真实部署需求：导航支持机器人在工作区之间移动，躯干调整则支持其与不同高度处（架子、柜子）的物体交互。数据收集流程的更多细节见附录 E。

## Figure 6. AgiBot pretraining-corpus statistics / AgiBot 预训练语料统计

![Figure 6](assets/page_011_fig_figure_6.png)

**Caption:** Distribution statistics for the AgiBot pretraining corpus: episode durations, subtask density, and skill coverage across 7.2K episodes ($\sim$500 hours).

**Caption[CN]:** AgiBot 预训练语料的分布统计：7.2K 个 episode（约 500 小时）的 episode 时长、子任务密度与技能覆盖。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Figure 6 reports a total of 7,193 episodes, a mean episode duration of 4.4 minutes, and a mean of 42.4 subtasks per episode.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Figure 6 报告了共 7,193 个 episode；平均 episode 时长为 4.4 分钟，每个 episode 平均包含 42.4 个子任务。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> We also validate DreamZero on the Franka single-arm robot using DROID (Khazatsky et al., 2024), one of the most heterogeneous publicly available robotic datasets, to demonstrate the effectiveness of WAMs on diverse, open-source data and enable reproducibility before the release of our in-house AgiBot dataset. We open-source the checkpoint and inference code to run some DROID simulation evaluations in PolaRiS (Jain et al., 2025).

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 我们还使用 DROID（Khazatsky et al., 2024）在 Franka 单臂机器人上验证 DreamZero。DROID 是异构性最强的公开机器人数据集之一；这一设置旨在证明 WAM 在多样开源数据上的有效性，并在我们内部 AgiBot 数据集发布前支持可复现性。我们开源 checkpoint 和推理代码，用于在 PolaRiS（Jain et al., 2025）中运行部分 DROID 仿真评估。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Footnotes 5–6.** We plan to open-source the AgiBot dataset in upcoming releases; some samples are available at <https://dreamzero0.github.io/training_data_gallery>. The DROID checkpoint and inference code are available at <https://github.com/dreamzero0/dreamzero>.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **脚注 5–6。** 我们计划在后续版本中开源 AgiBot 数据集；部分样例可见 <https://dreamzero0.github.io/training_data_gallery>。DROID checkpoint 与推理代码可见 <https://github.com/dreamzero0/dreamzero>。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Training.** We use Wan2.1-I2V-14B-480P (Team Wan, 2025), a 14B image-to-video diffusion model, as the backbone for DreamZero. We train for 100K steps with a global batch size of 128 for AgiBot and 100K steps with a global batch size of 128 for DROID. We update all DiT blocks, the state encoder, action encoder, and action decoder, while freezing the text encoder, image encoder, and VAE. For both datasets, we filter out idle actions and use relative joint positions as the default action representation. We also conduct ablations (Section 5.2) initialized from Wan2.1-I2V-5B-480P to study the effect of model size (5B versus 14B).

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **训练。** 我们使用 Wan2.1-I2V-14B-480P（Team Wan, 2025）作为 DreamZero 骨干，这是一个 14B 图生视频扩散模型。在 AgiBot 数据上训练 100K 步、global batch size 为 128；在 DROID 数据上同样训练 100K 步、global batch size 为 128。我们更新所有 DiT block、状态编码器、动作编码器与动作解码器，同时冻结文本编码器、图像编码器和 VAE。对两个数据集，我们均过滤空闲动作，并默认使用相对关节位置作为动作表示。我们还进行了从 Wan2.1-I2V-5B-480P 初始化的消融实验（第 5.2 节），以研究模型规模（5B 与 14B）的影响。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> **Footnote 7.** We experimented with LoRA (Hu et al., 2022) but found that it led to suboptimal results.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> **脚注 7。** 我们尝试了 LoRA（Hu et al., 2022），但发现它会导致次优结果。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> **Evaluation Protocol.** We evaluate models out of the box after pretraining. Our default evaluation setting is unseen environments and unseen objects—because our pretraining and post-training data were collected in a different geographic location from our evaluation sites, every benchmark inherently tests out-of-distribution generalization rather than interpolation within the training distribution. We evaluate on two categories: seen and unseen tasks. We define the granularity of a task as a combination of the motion required for the task and the object type. For example, if the training data contain folding a red shirt and we evaluate the model on folding a black shirt of a different size, it is considered a seen task. On the other hand, folding socks is considered an unseen task because the motion required to fold socks differs from folding a shirt (see samples in Figure 7).

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **评估协议。** 预训练完成后，我们直接评估模型。默认评估设定是未见环境和未见物体：由于预训练和后训练数据的收集地点在地理上与评估地点不同，每个 benchmark 都天然测试分布外泛化，而非训练分布内插值。我们评估两类任务：已见任务和未见任务。我们将任务粒度定义为该任务所需运动与物体类型的组合。例如，如果训练数据包含折叠红色衬衫，而评估时要求模型折叠尺寸不同的黑色衬衫，则这被视为已见任务。反之，折叠袜子被视为未见任务，因为折袜子所需的运动与折衬衫不同（样例见 Figure 7）。

## Figure 7. AgiBot Evaluation Set-up / AgiBot 评估设置

![Figure 7](assets/page_012_fig_figure_7.png)

**Caption:** AgiBot Evaluation Set-up. We are first-citizens of generalization evals, where the default setting is unseen environment and unseen objects.

**Caption[CN]:** AgiBot 评估设置。我们将泛化评估放在首位，其默认设定是未见环境与未见物体。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **AgiBot Evaluation Protocol.** For seen tasks, we select 10 tasks from the pretraining distribution, including pick-and-place variants, stacking, wiping, and folding; we run 8 rollouts per task across 4 robots, each in different environments and with different objects (80 rollouts total per checkpoint). We divide the 10 seen tasks into three categories: **PnP-Easy** (pick and place fruit, wipe the mess, take fruit out of a bag), **PnP-Hard** (pick and place fork/spoon, put the pen in the pen holder, put the cup on the coaster, stack bowls/cups in a row), and **Contact-Rich Manipulation** (fold shirts, fold shorts, stack clothes). For unseen tasks, we evaluate 10 tasks absent from training—such as ironing, painting, pulling carts, cube stacking, removing a hat from a mannequin, and untying shoelaces—with 8 rollouts per task across 4 robots (80 rollouts total per checkpoint). The complete initial frame and prompt for every evaluation rollout are provided in Appendix F.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **AgiBot 评估协议。** 对于已见任务，我们从预训练分布中选择 10 个任务，包括抓放变体、堆叠、擦拭和折叠；每个任务在 4 台机器人上共运行 8 次 rollout，且每台机器人所在环境不同、物体不同（每个 checkpoint 总计 80 次 rollout）。我们把这 10 个已见任务分为三类：**PnP-Easy**（抓放水果、擦拭污渍、从袋中取出水果）；**PnP-Hard**（抓放叉子/勺子、把笔放进笔筒、把杯子放在杯垫上、将碗/杯堆成一排）；以及 **Contact-Rich Manipulation**（折衬衫、折短裤、叠衣物）。对于未见任务，我们评估 10 个训练中不存在的任务，例如熨衣、绘画、拉车、方块堆叠、从人台上摘帽子以及解鞋带；每个任务在 4 台机器人上运行 8 次 rollout（每个 checkpoint 总计 80 次）。每次评估 rollout 的完整初始帧与提示详见附录 F。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> **Footnote 8.** Main evaluation rollouts are available at <https://dreamzero0.github.io>, and an accumulation of unique evaluation rollouts is available at <https://dreamzero0.github.io/evals_gallery>.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> **脚注 8。** 主要评估 rollout 可见 <https://dreamzero0.github.io>，持续汇集的独特评估 rollout 可见 <https://dreamzero0.github.io/evals_gallery>。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> **DROID Evaluation Protocol.** We evaluate on 20 seen tasks and 20 unseen tasks (verbs absent from DROID), performing 2 rollouts per task, for a total of 80 evaluation rollouts across 40 tasks for each checkpoint. We compare DreamZero against the publicly released $\pi_{0.5}$-DROID and an internally trained GR00T N1.6-DROID checkpoint. Object positions are fixed across checkpoints to ensure fairness. Each rollout is scored from 0 to 1.0 based on partial task completion; full details are provided in Appendix G.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> **DROID 评估协议。** 我们评估 20 个已见任务和 20 个未见任务（动词未出现于 DROID），每个任务执行 2 次 rollout，因此每个 checkpoint 在 40 个任务上共有 80 次评估 rollout。我们将 DreamZero 与公开发布的 $\pi_{0.5}$-DROID 以及内部训练的 GR00T N1.6-DROID checkpoint 比较。为保证公平，不同 checkpoint 之间的物体位置保持固定。每次 rollout 根据部分任务完成程度在 0 到 1.0 之间评分；完整细节见附录 G。

## 4.2. Post-training

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Beyond pretraining, we evaluate whether WAMs improve fine-tuning performance on task-specific data using the AgiBot robot.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 除了预训练，我们还使用 AgiBot 机器人评估 WAM 是否能提高在任务专用数据上的微调性能。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Data.** We collect post-training data on three downstream tasks:
>
> - **Shirt folding (33 hrs):** Fold a flattened T-shirt through 5 sequential stages. We randomize the initial shirt position across 2 shirt types.
> - **Fruit packing (12 hrs):** Pack 10 fruits from a table into a bag. We randomize fruit combinations and the positions of the fruits and bag.
> - **Table bussing (40 hrs):** Clear 5 pieces of trash into a trash bin and 5 pieces of dishware (dish, bowl, fork, and spoon) into a dish bin. We randomize object types, combinations, and positions.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **数据。** 我们为三个下游任务收集后训练数据：
>
> - **折叠衬衫（33 小时）：**通过 5 个连续阶段折叠一件铺平的 T 恤。我们在 2 种衬衫类型上随机化衬衫的初始位置。
> - **水果装袋（12 小时）：**把桌上的 10 个水果装入袋中。我们随机化水果组合以及水果和袋子的位置。
> - **清理餐桌（40 小时）：**把 5 件垃圾放进垃圾桶，并把 5 件餐具（盘子、碗、叉子和勺子）放入餐具箱。我们随机化物体类型、组合与位置。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Training.** We post-train for 50K steps per task. As in pretraining, we update all parameters except the text encoder, image encoder, and VAE.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **训练。** 我们对每个任务后训练 50K 步。与预训练一样，除文本编码器、图像编码器和 VAE 之外，我们更新所有参数。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Evaluation Protocol.** We measure average task progress across 10 rollouts per task. Task progress is defined as: (1) folding stages completed out of 5 for shirt folding, (2) fruits successfully packed out of 10 for fruit packing, and (3) items cleared for table bussing. Following Barreiros et al. (2025), we apply an image overlay to the initial scene to reduce variance.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **评估协议。** 我们对每个任务运行 10 次 rollout，并测量平均任务进度。任务进度定义为：（1）折衬衫时，5 个折叠阶段中完成的阶段数；（2）水果装袋时，10 个水果中成功装入的数量；（3）清理餐桌时，已清走的物品数。遵循 Barreiros et al. (2025)，我们对初始场景应用图像叠加，以减少方差。

# 5. Experimental Results

## 5.1. Main Results

## Figure 8. Seen Task Evaluation / 已见任务评估

![Figure 8](assets/page_013_fig_figure_8.png)

**Caption:** Seen Task Evaluation. DreamZero effectively learns from diverse data and generalizes to new environments, outperforming VLAs across all task categories. VLAs trained *from scratch* achieve near-zero success, while *pretrained* VLAs show modest performance—likely benefiting from embodiment-specific knowledge acquired through repetitive demonstrations during pretraining.

**Caption[CN]:** 已见任务评估。DreamZero 能从多样数据中有效学习并泛化到新环境，在所有任务类别上都优于 VLA。从零开始训练的 VLA 成功率接近于零，而预训练 VLA 表现中等；这些模型可能得益于在预训练重复示范中获得的形态专用知识。

| Embodiment / metric | Category | GR00T N1.6 (Scratch) | GR00T N1.6 (Pretrained) | $\pi_{0.5}$ (Scratch) | $\pi_{0.5}$ (Pretrained) | DreamZero (Scratch) |
|---|---|---:|---:|---:|---:|---:|
| AgiBot G1 / Task Progress | PnP Easy | 2.1 | 17.6 | 0 | 52.1 | 93.8 |
| AgiBot G1 / Task Progress | PnP Hard | 0 | 4.7 | 0 | 22.7 | 48.4 |
| AgiBot G1 / Task Progress | Contact-Rich | 0 | 4.2 | 0 | 9.2 | 49.0 |
| AgiBot G1 / Task Progress | AVG | 0.6 | 8.4 | 0 | 27.4 | 62.2 |
| DROID-Franka / Task Progress | AVG | — | 62 | — | 69 | 82 |
| DROID-Franka / Success Rate | AVG | — | 42 | — | 42 | 75 |

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We evaluate the zero-shot generalization performance of DreamZero against baseline models and investigate the following research questions.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们将 DreamZero 的零样本泛化性能与 baseline 模型比较，并研究以下问题。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Q1. Do WAMs learn better from diverse, non-repetitive data?** We evaluate pretrained models out of the box on tasks present in the pretraining data but in zero-shot environments with unseen objects. Results are shown in Figure 8.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **Q1. WAM 能否更好地从多样、非重复数据中学习？** 我们直接评估预训练模型：任务本身出现过在预训练数据中，但环境是零样本环境，物体也未见。结果见 Figure 8。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> On AgiBot G1, from-scratch VLAs achieve near-zero task-progress scores across all categories. Even on simple pick-and-place tasks (PnP Easy), VLAs occasionally reach toward the correct object but fail to interact accurately with unseen objects in novel environments. In contrast, DreamZero successfully learns from heterogeneous data, achieving 62.2% average task progress—over 2× higher than the best pretrained VLA baseline (27.4%), despite those baselines being pretrained on thousands of hours of cross-embodiment robot data before continued training on our data mixture. On DROID-Franka, we find a similar result: DreamZero, trained only on the DROID dataset, outperforms pretrained baseline models trained on multiple robot embodiments.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在 AgiBot G1 上，from-scratch VLA 在所有类别中的任务进度都接近零。即使对简单的抓放任务（PnP Easy），VLA 偶尔会伸向正确物体，却无法在新环境中准确与未见物体交互。相比之下，DreamZero 成功从异构数据中学习，平均任务进度达 62.2%，比最强预训练 VLA baseline（27.4%）高 2 倍以上；而后者在我们的混合数据上继续训练前，已在数千小时跨机器人形态数据上预训练。在 DROID-Franka 上也有类似结果：仅在 DROID 数据集上训练的 DreamZero，优于在多种机器人形态上训练的预训练 baseline。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> We attribute this gap to the joint video-action formulation: while VLAs require massive robot data to learn direct observation-to-action mappings, WAMs leverage video generation as a strong prior for action prediction, enabling effective learning from diverse data and generalization to unseen environments. Notably, we observe tight alignment between generated videos and real-world execution, even for suboptimal behaviors (Figure 16). Most DreamZero failures stem from video-generation errors rather than action prediction—the policy faithfully executes whatever trajectory the video predicts. This suggests that improvements to the video backbone would directly translate into better WAM performance.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 我们把这一差距归因于联合视频—动作形式：VLA 需要海量机器人数据来学习直接观测到动作的映射，而 WAM 利用视频生成作为动作预测的强先验，因而能从多样数据中有效学习并泛化到未见环境。值得注意的是，即使对次优行为，我们也观察到生成视频与真实世界执行严密对齐（Figure 16）。DreamZero 的大多数失败源于视频生成错误，而非动作预测；策略会忠实执行视频所预测的任何轨迹。这表明，改进视频骨干会直接转化为更好的 WAM 性能。

## Figure 9. Zero-shot Generalization to Unseen Tasks / 向未见任务的零样本泛化

![Figure 9](assets/page_014_fig_figure_9.png)

**Caption:** Zero-shot Generalization to Unseen Tasks. DreamZero achieves non-trivial task progress on 10 tasks absent from training, while VLAs struggle across both embodiments.

**Caption[CN]:** 向未见任务的零样本泛化。DreamZero 在 10 个训练中不存在的任务上取得不可忽略的任务进度，而 VLA 在两种机器人形态上都表现困难。

| AgiBot G1 unseen task / 未见任务 | GR00T N1.6 (Scratch) | GR00T N1.6 (Pretrained) | $\pi_{0.5}$ (Scratch) | $\pi_{0.5}$ (Pretrained) | DreamZero (Scratch) |
|---|---:|---:|---:|---:|---:|
| 1. Untie Shoelaces | 0 | 0.1 | 0 | 9.4 | 28.1 |
| 2. Remove Hat from Mannequin | 0 | 12.5 | 0 | 42.9 | 85.7 |
| 3. Draw with Pen | 0 | 0 | 0 | 14.3 | 35.7 |
| 4. Take Out Straw | 0 | 6.2 | 0 | 18.8 | 46.9 |
| 5. Cube Stacking | 0 | 0 | 0 | 6.2 | 23.9 |
| 6. Painting w/ Brush | 0 | 6.2 | 0 | 17.9 | 28.6 |
| 7. Ironing | 7.1 | 0 | 0 | 14.3 | 28.6 |
| 8. Shake Hands | 0 | 18.8 | 0 | 25 | 59.2 |
| 9. Fold Map | 0 | 0 | 0 | 0 | 8.2 |
| 10. Pulling Cart | 0 | 0 | 0 | 14.3 | 50 |
| **AVG Task Progress** | **0.7** | **5** | **0** | **16.3** | **39.5** |

| DROID-Franka unseen-task aggregate | GR00T N1.6 (Pretrained) | $\pi_{0.5}$ (Pretrained) | DreamZero (Scratch) |
|---|---:|---:|---:|
| AVG Task Progress | 31 | 33 | 49 |
| AVG Success Rate | 12.5 | 7.5 | 22.5 |

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Q2. Do WAMs generalize to unseen tasks?** Figure 9 evaluates generalization to 10 tasks entirely absent from the pretraining distribution, including untying shoelaces, ironing, painting with a brush, and shaking hands.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **Q2. WAM 能否泛化到未见任务？** Figure 9 评估了对 10 个完全不存在于预训练分布的任务的泛化，包括解鞋带、熨衣、用画笔绘画和握手。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> On AgiBot G1, from-scratch VLAs achieve near-zero task progress ($<1\%$), while DreamZero reaches 39.5% on average—with strong performance on tasks such as “Remove Hat from Mannequin” (85.7%) and “Shake Hands” (59.2%). DreamZero also significantly outperforms pretrained VLA baselines (39.5% versus 16.3%), even though those baselines may have encountered some of these tasks during cross-embodiment pretraining. On the DROID-Franka setup, DreamZero also significantly outperforms other pretrained baselines: 49% task progress and 22.5% success rate, compared with 31% task progress and 12.5% success rate for GR00T N1.6 and 33% task progress and 7.5% success rate for $\pi_{0.5}$.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 在 AgiBot G1 上，from-scratch VLA 的任务进度接近零（$<1\%$），而 DreamZero 平均达到 39.5%，并在“从人台上摘帽子”（85.7%）和“握手”（59.2%）等任务上表现强劲。DreamZero 也显著优于预训练 VLA baseline（39.5% 对 16.3%），尽管后者在跨机器人形态预训练期间可能已经见过部分此类任务。在 DROID-Franka 设置中，DreamZero 同样显著优于其他预训练 baseline：任务进度 49%、成功率 22.5%；GR00T N1.6 的任务进度为 31%、成功率为 12.5%，$\pi_{0.5}$ 则分别为 33% 和 7.5%。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Qualitatively, we observe that pretrained VLAs often reach toward objects and attempt grasping regardless of the instruction, suggesting that they overfit dominant training behaviors (e.g., pick-and-place) rather than understanding novel task semantics. This accounts for their partial task progress despite failing to complete the intended tasks. In contrast, DreamZero performs visual planning for unseen tasks and executes them successfully, with strong alignment between generated videos and real-world actions.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 在定性观察中，预训练 VLA 往往无论指令如何都会伸向物体并尝试抓取，这表明它们过拟合了主导训练行为（例如抓放），而非真正理解新任务语义。这也解释了为何它们即使未能完成预定任务，仍会获得部分任务进度。相比之下，DreamZero 会针对未见任务进行视觉规划并成功执行，生成视频与真实世界动作高度对齐。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Beyond structured evaluation, we conduct free-form testing on more than 100 additional tasks, including “Pop the ballon” and “Press elevator button,” through free-form prompting with verbal instructions.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 除结构化评估之外，我们还通过口头指令的自由形式提示，在 100 个以上的其他任务上进行自由形式测试，包括“Pop the ballon”和“Press elevator button”。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **Footnote 9.** Rollouts of these tasks are provided at <https://dreamzero0.github.io/evals_gallery/>.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **脚注 9。** 这些任务的 rollout 见 <https://dreamzero0.github.io/evals_gallery/>。

## Figure 10. Posttraining Results / 后训练结果

![Figure 10](assets/page_015_fig_figure_10.png)

**Caption:** Posttraining Results. WAMs enable stronger post-training results across three tasks, indicating that environment generalization of DreamZero is retained after post-training.

**Caption[CN]:** 后训练结果。WAM 在三个任务上带来更强的后训练结果，表明 DreamZero 的环境泛化能力在后训练之后得以保留。

| Average Task Progress (%) | GR00T N1.6 (Scratch) | GR00T N1.6 (Pretrained) | $\pi_{0.5}$ (Scratch) | $\pi_{0.5}$ (Pretrained) | DreamZero (Scratch) |
|---|---:|---:|---:|---:|---:|
| Shirt Folding | 2.5 | 65 | 1.5 | 92.5 | 92.5 |
| Fruit Packing | 27 | 56 | 0 | 71 | 96 |
| Table Bussing | 0 | 39 | 0 | 76 | 83 |
| **AVG** | **9.8** | **53.3** | **0.5** | **79.8** | **90.5** |

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> **Q3. Do WAMs improve post-training performance?** We investigate whether WAMs retain their generalization even after fine-tuning on task-specific data. Figure 10 shows results on three tasks with varying distribution diversity.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> **Q3. WAM 能否提高后训练性能？** 我们研究 WAM 在任务专用数据上微调后是否仍保留泛化能力。Figure 10 展示了三个分布多样性不同的任务上的结果。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> DreamZero matches or outperforms VLA baselines across all tasks: it performs comparably on shirt folding and table bussing while significantly outperforming on fruit packing. Similar to the findings from Figure 8 and Figure 9, from-scratch baselines fail to learn accurate motions for grasping target objects; this means that from-scratch VLAs tend to overfit to the training data and fail to generalize to scenarios in which table height, table distance, objects, and object placements vary, largely because the evaluation site is in a different geographic location (see Figure 7 for samples). Although pretraining on multiple robot embodiments with repetitive data greatly boosts post-training generalization for pretrained baselines, DreamZero still matches or outperforms pretrained VLA baselines without cross-embodiment pretraining. Because post-training evaluation still uses unseen environments, this implies that DreamZero's environment generalization is retained after post-training.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> DreamZero 在所有任务上均达到或超过 VLA baseline：在折衬衫和清理餐桌上性能可比，在水果装袋上则显著更优。与 Figure 8 和 Figure 9 的发现类似，from-scratch baseline 无法学会准确的目标物体抓取动作；这意味着 from-scratch VLA 倾向于过拟合训练数据，并无法泛化到桌子高度、桌子距离、物体和物体摆放发生变化的情形；其主要原因是评估地点在地理上不同（样例见 Figure 7）。尽管在多种机器人形态的重复数据上预训练会大幅提高预训练 baseline 的后训练泛化性能，但 DreamZero 在不进行跨机器人形态预训练的情况下，仍达到或超过预训练 VLA baseline。由于后训练评估仍在未见环境中进行，这意味着 DreamZero 的环境泛化性在后训练之后得到保留。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> **Q4. Do WAMs enable strong cross-embodiment transfer to unseen tasks?** Having shown that WAMs generalize to unseen tasks (Figure 9), we now investigate whether this generalization can be improved further by leveraging video data from different embodiments performing the same tasks. Crucially, we use only the video-prediction objective for cross-embodiment data (no actions), while maintaining the joint video-action objective for the AgiBot pretraining data; cross-embodiment data therefore serve as additional visual experience that strengthens the world model's understanding of task dynamics and expected behavior.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> **Q4. WAM 能否针对未见任务实现强跨机器人形态迁移？** 在证明 WAM 可泛化到未见任务（Figure 9）后，我们进一步研究是否能利用不同机器人形态执行相同任务的视频数据，来继续提升这一泛化性。关键的是，对于跨机器人形态数据，我们只使用视频预测目标（不使用动作），同时对 AgiBot 预训练数据继续使用联合视频—动作目标。因此，跨机器人形态数据充当附加视觉经验，用以加强世界模型对任务动力学和预期行为的理解。

## Figure 11. Cross-Embodiment Transfer / 跨机器人形态迁移

![Figure 11](assets/page_015_fig_figure_11.png)

**Caption:** Cross-Embodiment Transfer. We explore robot-to-robot (YAM $\rightarrow$ AgiBot) and human-to-robot embodiment transfer to unseen tasks.

**Caption[CN]:** 跨机器人形态迁移。我们探索针对未见任务的机器人到机器人（YAM $\rightarrow$ AgiBot）与人类到机器人的形态迁移。

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> We explore two settings (Figure 11): (1) robot-to-robot transfer using the bimanual YAM robot, and (2) human-to-robot transfer using egocentric human demonstrations. For each setting, we collect 72 multiview trajectories of the 9 unseen tasks (8 demonstrations per task, 20 minutes for YAM, 12 minutes for humans). We then co-train from the DreamZero-AgiBot checkpoint on a 1:1 mixture with pretraining data for 10K steps.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> 我们探索两种设定（Figure 11）：（1）使用双臂 YAM 机器人进行机器人到机器人迁移；（2）使用人类第一视角示范进行人类到机器人迁移。在每种设定中，我们针对 9 个未见任务收集 72 条多视角轨迹（每任务 8 个示范；YAM 数据总时长 20 分钟，人类数据总时长 12 分钟）。随后，我们从 DreamZero-AgiBot checkpoint 开始，将这些数据与预训练数据按 1:1 混合，联合训练 10K 步。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> **Footnote 10.** We exclude the Pulling Cart task because data collection through teleoperation was infeasible with our bimanual YAM robot setup.

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> **脚注 10。** 我们排除了 Pulling Cart 任务，因为在双臂 YAM 机器人设置下，无法通过遥操收集该任务数据。

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> Results on the 9 unseen tasks (Table 2) show that both transfer settings improve performance over baseline DreamZero. Robot-to-robot transfer yields the largest gain (38.3% $\rightarrow$ 55.4%), likely because the embodiment gap is narrower; both YAM and AgiBot use bimanual parallel grippers. Human-to-robot transfer also improves performance (38.3% $\rightarrow$ 54.3%), despite the larger morphological gap and dynamic egocentric viewpoints.

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> 9 个未见任务上的结果（Table 2）表明，两种迁移设定都超过 baseline DreamZero。机器人到机器人迁移带来最大收益（38.3% $\rightarrow$ 55.4%），这可能是因为形态差距较小；YAM 和 AgiBot 都使用双臂平行夹爪。尽管存在更大的形态差距和动态第一视角，人类到机器人迁移同样提高了性能（38.3% $\rightarrow$ 54.3%）。

## Table 2. Cross-Embodiment Transfer Results / 跨机器人形态迁移结果

| Method | Task Progress |
|---|---:|
| DreamZero | 38.3% $\pm$ 7.6% |
| DreamZero + Human2Robot Transfer | 54.3% $\pm$ 10.4% |
| DreamZero + Robot2Robot Transfer | 55.4% $\pm$ 9.5% |

**Caption:** Cross-Embodiment Transfer Results. Average task progress on unseen tasks ($\pm$ standard error). Both transfer settings improve over baseline (result from Table 9) using only 10–20 minutes of video-only demonstration data.

**Caption[CN]:** 跨机器人形态迁移结果。未见任务上的平均任务进度（$\pm$ 标准误）。两种迁移设定均在仅使用 10–20 分钟纯视频示范数据的情况下超过 baseline（结果来自 Table 9）。

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> These results point to a promising property of WAMs: unlike recent VLA approaches to embodiment transfer (Kareer et al., 2025; Team, 2025), our method relies solely on visual information without action labels. While current success rates remain moderate, the consistent improvement from just 10–20 minutes of video-only data provides an early signal that cross-embodiment visual experience transfers meaningfully. This opens a potential scaling pathway: abundant human video data—orders of magnitude larger than robot datasets—could enable WAMs to acquire diverse skills without action annotation, pending further research into strengthening the transfer mechanism.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> 这些结果指向 WAM 的一项很有前景的性质：与近期 VLA 机器人形态迁移方法（Kareer et al., 2025; Team, 2025）不同，我们的方法只依赖视觉信息，无需动作标签。尽管当前成功率仍然中等，但仅 10–20 分钟纯视频数据就带来了一致改进，这一早期信号表明跨机器人形态的视觉经验能够进行有意义的迁移。这开辟了潜在的规模化路径：人类视频数据非常丰富，规模比机器人数据集高出数个数量级；它们可能使 WAM 无需动作标注即可获得多样技能，但仍需进一步研究如何强化迁移机制。

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> **Q5. Do WAMs enable few-shot new-embodiment adaptation?** We post-train the DreamZero-AgiBot checkpoint on a new bimanual manipulator (the YAM robot) using only 55 trajectories across 11 unique tasks ($\sim$30 minutes of data). As illustrated in Figure 12, despite limited data and diversity, the post-trained policy retains strong language-following ability, even generalizing to novel objects unseen during training, including pumpkins, teddy bears, pens, cup noodles, and paper bags. Even with minimal data, we observe tight video-action alignment, demonstrating highly efficient cross-embodiment transfer.

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> **Q5. WAM 能否实现对新机器人形态的少样本适配？** 我们在一个新的双臂操作机器人（YAM）上对 DreamZero-AgiBot checkpoint 进行后训练，只使用 11 个独立任务上的 55 条轨迹（约 30 分钟数据）。如 Figure 12 所示，尽管数据量和多样性有限，后训练策略仍保留了强语言遵循能力，甚至能泛化到训练中未见的新物体，包括南瓜、泰迪熊、笔、杯面和纸袋。即使仅有极少数据，我们也观察到严密的视频—动作对齐，表明跨机器人形态迁移效率极高。

## Figure 12. Few-shot Embodiment Adaptation / 少样本机器人形态适配

![Figure 12](assets/page_016_fig_figure_12.png)

**Caption:** Few-shot Embodiment Adaptation. We explore few-shot embodiment adaptation by post-training on 30 minutes of new-embodiment play data and evaluating on pick-and-place variants requiring strong language following.

**Caption[CN]:** 少样本机器人形态适配。我们在 30 分钟新形态自由操作数据上进行后训练，并在需要强语言遵循能力的抓放变体上评估，以探索少样本机器人形态适配。

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> The visible evaluation instructions are: “Put the cup noodles in the paper bag”; “Pick up the teddy bear”; “Put the orange in the pumpkin”; and “Put banana in wooden shelf.”

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> 图中可见的评估指令为：“把杯面放进纸袋”；“拿起泰迪熊”；“把橙子放进南瓜”；以及“把香蕉放入木质架子”。

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> **Footnote 11.** We visualize the entire 30 minutes of play data at <https://dreamzero0.github.io/yam_gallery/>.

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> **脚注 11。** 我们在 <https://dreamzero0.github.io/yam_gallery/> 可视化了完整 30 分钟自由操作数据。

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> We hypothesize that two factors enable this efficiency: (1) the visual similarity of the AgiBot G1 and YAM embodiments (both equipped with bimanual parallel grippers), and (2), more fundamentally, learning an implicit IDM from predicted videos may be inherently more sample-efficient than direct policy learning—the model only needs to learn the mapping from visual futures to actions while leveraging the pretrained video model's existing understanding of physical dynamics. Consistent with our AgiBot findings, failures primarily stem from video-prediction errors rather than action extraction, suggesting that increasing task diversity during post-training could improve performance further.

> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> 我们假设有两个因素带来了这种效率：（1）AgiBot G1 和 YAM 的形态在视觉上相似（二者都配备双臂平行夹爪）；（2）更根本地说，从预测视频学习隐式 IDM 可能在本质上比直接策略学习更具样本效率；模型只需学习视觉未来到动作的映射，同时利用预训练视频模型已有的物理动力学理解。与我们在 AgiBot 上的发现一致，失败主要源于视频预测错误而非动作提取；这表明提高后训练中的任务多样性可能进一步改善性能。

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> **Footnote 12.** In this specific post-training experiment, we used only 11 short, global language annotations, one unique annotation for each task. We hypothesize that diversifying language could also enable stronger transfer, but leave further investigation to future work.

> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> **脚注 12。** 在这一特定后训练实验中，我们只使用了 11 条简短的全局语言标注，每个任务对应一条唯一标注。我们假设增加语言多样性也能带来更强迁移，但将进一步研究留作未来工作。

> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> **Q6. Does DreamZero-Flash maintain performance with fewer denoising steps?** We evaluate whether DreamZero-Flash can maintain task performance under aggressive single-step denoising. As shown in Table 3, reducing DreamZero from 4 denoising steps to 1 step drops task progress substantially (83% $\rightarrow$ 52%) on table bussing. In contrast, DreamZero-Flash achieves a higher average task progress (74%) with single-step inference, only 9% below the 4-step baseline while being $\sim$2× faster. This suggests that decoupled noise scheduling offers a more effective speed–accuracy trade-off for real-time deployment.

> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> **Q6. DreamZero-Flash 在减少去噪步数时能否保持性能？** 我们评估 DreamZero-Flash 在激进的单步去噪下能否保持任务性能。如 Table 3 所示，在清理餐桌任务上，将 DreamZero 从 4 个去噪步减少到 1 个会使任务进度大幅下降（83% $\rightarrow$ 52%）。相比之下，DreamZero-Flash 在单步推理时实现了更高的平均任务进度（74%），只比 4 步 baseline 低 9%，却快约 2 倍。这表明，解耦噪声调度为实时部署提供了更有效的速度—准确性权衡。

## Table 3. DreamZero-Flash Evaluation / DreamZero-Flash 评估

| Method | Denoising steps | Task Progress | Inference speed | $\times$ Speed up |
|---|---:|---:|---:|---:|
| DreamZero | 4 | 83% $\pm$ 6.1% | 350ms | 1 |
| DreamZero | 1 | 52% $\pm$ 10.2% | 150ms | 2.33× |
| DreamZero-Flash | 1 | 74% $\pm$ 10.1% | 150ms | 2.33× |

**Caption:** DreamZero-Flash Evaluation. Task progress on table bussing with varying denoising steps ($\pm$ standard error). DreamZero-Flash recovers most of the 4-step performance using only 1 denoising step.

**Caption[CN]:** DreamZero-Flash 评估。不同去噪步数下的清理餐桌任务进度（$\pm$ 标准误）。DreamZero-Flash 仅用 1 个去噪步便恢复了 4 步性能的大部分。

## 5.2. Model and Data Ablations

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We conduct ablations to isolate the contributions of data diversity, model scale, and architecture. Because of computational constraints, all ablation models are trained for 50K steps with batch size 32 and evaluated on PnP Easy tasks for consistent comparison.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们进行消融实验，以隔离数据多样性、模型规模与架构各自的贡献。由于计算约束，所有消融模型均训练 50K 步，batch size 为 32，并在 PnP Easy 任务上评估，以保证比较一致。

## Table 4. Model and Data Ablations / 模型与数据消融

| Question | Architecture | Model Size | Data | Task Progress |
|---|---|---:|---|---:|
| Q1. Data Diversity | DreamZero (AR) | 14B | Repetitive | 33% $\pm$ 4.2% |
| Q1. Data Diversity | DreamZero (AR) | 14B | Diverse | 50% $\pm$ 6.3% |
| Q2. Model Scale | DreamZero (AR) | 5B | Diverse | 21% $\pm$ 4.2% |
| Q2. Model Scale | DreamZero (AR) | 14B | Diverse | 50% $\pm$ 6.3% |
| Q2. Model Scale | VLA | 5B | Diverse | 0% $\pm$ 0.0% |
| Q2. Model Scale | VLA | 14B | Diverse | 0% $\pm$ 0.0% |
| Q3. Architecture (Bidirectional vs. AR) | DreamZero (BD) | 14B | Diverse | 50% $\pm$ 14.4% |
| Q3. Architecture (Bidirectional vs. AR) | DreamZero (AR) | 14B | Diverse | 50% $\pm$ 6.3% |

**Caption:** Model and Data Ablations. Task progress on PnP Easy tasks ($\pm$ standard error). AR = autoregressive, BD = bidirectional. All models trained with 50K steps and batch size 32.

**Caption[CN]:** 模型与数据消融。PnP Easy 任务上的任务进度（$\pm$ 标准误）。AR = 自回归，BD = 双向。所有模型均训练 50K 步，batch size 为 32。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Q1. Does data diversity improve generalization?** We compare DreamZero trained on 500 hours of diverse data with DreamZero trained on 500 hours of repetitive data, where the latter contains 70 tasks with many repeated demonstrations per task using similar object positions and configurations. As shown in Table 4, diverse data substantially improve generalization (33% $\rightarrow$ 50%), even on simple pick-and-place tasks. We hypothesize that this reflects WAM learning dynamics: because video prediction is largely inherited from pretraining, the key challenge is learning inverse dynamics. A robust IDM requires diverse state-action correspondences across varied contexts, which repetitive data inherently lack.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **Q1. 数据多样性能否提高泛化？** 我们将在 500 小时多样数据上训练的 DreamZero 与在 500 小时重复数据上训练的 DreamZero 进行比较；后者包含 70 个任务，每个任务都有多次重复示范，且物体位置和配置相似。如 Table 4 所示，多样数据显著提高了泛化（33% $\rightarrow$ 50%），即使在简单抓放任务上也是如此。我们假设这反映了 WAM 的学习动力学：由于视频预测在很大程度上继承自预训练，关键挑战是学习逆动力学。稳健 IDM 需要多种上下文下的多样状态—动作对应，而重复数据天然缺少这种多样性。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Q2. Does WAM performance scale with model size?** For VLAs, scaling model size improves semantic reasoning but not necessarily action prediction. We find that WAMs exhibit clearer scaling behavior: the 14B model significantly outperforms the 5B model (50% versus 21%), with the smaller model prone to visual hallucinations that propagate into erroneous actions.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **Q2. WAM 性能是否随模型规模而扩展？** 对 VLA 而言，增大模型规模会提高语义推理，却不一定提高动作预测。我们发现 WAM 表现出更清晰的扩展行为：14B 模型显著优于 5B 模型（50% 对 21%），较小模型容易产生视觉幻觉，并将其传播为错误动作。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> To ensure a fair comparison, we also scale VLA baselines to match DreamZero's size by initializing from 8B and 32B pretrained VLMs (Yang et al., 2025), truncating to the first half of the transformer blocks, and attaching DiT-based action modules following Bjorck et al. (2025). As shown in Table 4, larger VLAs still fail to learn from diverse data (0% task progress), often hovering near objects without making contact. This suggests that scaling model capacity alone does not address VLAs' difficulty with diverse data distributions.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 为保证公平比较，我们还将 VLA baseline 扩展到与 DreamZero 匹配的规模：从 8B 和 32B 预训练 VLM（Yang et al., 2025）初始化，保留 transformer block 的前一半，并按照 Bjorck et al. (2025) 附加基于 DiT 的动作模块。如 Table 4 所示，更大的 VLA 仍无法从多样数据中学习（任务进度为 0%），它们常常在物体附近徘徊，却不与之接触。这表明，仅扩展模型容量不能解决 VLA 难以处理多样数据分布的问题。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Q3. Does an autoregressive architecture outperform a bidirectional one?** We compare DreamZero's autoregressive (AR) architecture with a bidirectional (BD) variant. Although task progress is similar (Table 4), the AR model produces substantially smoother motions—backpropagating through entire action sequences enables better temporal consistency. In addition, AR inference is 3–4× faster because of KV caching.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **Q3. 自回归架构是否优于双向架构？** 我们将 DreamZero 的自回归（AR）架构与一个双向（BD）变体比较。尽管任务进度相似（Table 4），AR 模型生成的动作要平滑得多；在完整动作序列上反向传播使时间一致性更好。此外，由于 KV 缓存，AR 推理速度快 3–4 倍。

# 6. Discussion and Future Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Scaling Laws of WAMs.** We have found that leveraging a larger video backbone model and training on diverse data boost downstream performance in Table 4. However, we still lack evidence for scaling laws for robot foundation models, specifically for WAMs. Similar to scaling laws for language models (Kaplan et al., 2020), WAM scaling laws as functions of model size, dataset size, and training compute need to be explored to determine the optimal configuration for extracting the maximum capability of WAMs. We expect WAM scaling trends to differ from those of VLAs, showing a more direct scaling law for actions. We leave a deep investigation of WAM scaling laws to future work.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **WAM 的扩展定律。** 我们已经发现，利用更大的视频骨干模型并在多样数据上训练，会提升 Table 4 中的下游性能。然而，我们仍缺乏机器人基础模型、尤其是 WAM 的扩展定律证据。与语言模型的扩展定律（Kaplan et al., 2020）类似，我们需要探索 WAM 随模型规模、数据集规模与训练计算量变化的扩展定律，以确定尽可能释放 WAM 能力的最优配置。我们预期 WAM 的扩展趋势与 VLA 不同，对动作会表现出更直接的扩展定律。我们将 WAM 扩展定律的深入研究留作未来工作。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Learning from In-the-wild Human Data.** Although we have investigated egocentric human data for boosting performance on unseen tasks (Section 5), our experiments remain constrained to small-scale in-lab data (only 12 minutes). Recently, a large amount of human video data with a more diverse distribution than robot data has been released (Chen et al., 2026; Grauman et al., 2022; Hoque et al., 2025). Because WAMs are pretrained on diverse internet video data, we hypothesize that using large-scale egocentric human videos related to robot-manipulation tasks would transfer to downstream robot tasks more strongly than current VLAs. We leave this direction to future work.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **从野外人类数据中学习。** 尽管我们已经研究了利用人类第一视角数据提高未见任务性能（第 5 节），但实验仍受限于小规模实验室内数据（仅 12 分钟）。近期已发布大量人类视频数据，其分布比机器人数据更多样（Chen et al., 2026; Grauman et al., 2022; Hoque et al., 2025）。由于 WAM 预训练于多样互联网视频数据，我们假设，使用与机器人操作任务相关的大规模人类第一视角视频，对下游机器人任务的迁移会比当前 VLA 更强。我们将这一方向留作未来工作。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Faster Inference.** Through model and system optimizations, we enable DreamZero to run at 7Hz using 2 GB200s. However, compared with current VLAs that run at more than 20Hz on consumer GPUs, DreamZero remains computationally expensive because of its large parameter count and the iterative denoising nature of video models. In the future, if smaller video backbone models also possess strong generalization, WAMs could potentially serve as real-time System 1 models on lightweight edge devices.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **更快的推理。** 借助模型与系统优化，我们使 DreamZero 能使用 2 张 GB200 以 7Hz 运行。然而，当前一些 VLA 在消费级 GPU 上可以超过 20Hz 运行；相比之下，DreamZero 由于参数规模庞大和视频模型的迭代去噪性质，计算成本仍然很高。未来，如果更小的视频骨干模型也具有强泛化能力，WAM 有望在轻量边缘设备上作为实时 System 1 模型使用。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Long-horizon Reasoning.** The current DreamZero architecture functions primarily as a System 1 model. Although DreamZero has a concept of visual memory, it is currently short-horizon (6 seconds). Robust long-horizon execution will require either a System 2 planner or WAMs with significantly extended context windows. For the former, both modular dual-system architectures (Shi et al., 2025) and unified approaches (Deng et al., 2025) offer promising directions. For the latter, techniques from video-based world models that maintain coherent generation over extended horizons (Ball et al., 2025; HunyuanWorld, 2025) could be adapted to expand WAM context length.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **长时域推理。** 当前 DreamZero 架构主要作为 System 1 模型。尽管 DreamZero 具有视觉记忆概念，但当前时域很短（6 秒）。稳健的长时域执行要么需要 System 2 规划器，要么需要上下文窗口大幅扩展的 WAM。对前者而言，模块化双系统架构（Shi et al., 2025）和统一方法（Deng et al., 2025）都提供了有前景的方向。对后者而言，可以改造来自基于视频的世界模型的技术；这些技术能在更长时域中保持连贯生成（Ball et al., 2025; HunyuanWorld, 2025），因而可用于扩展 WAM 的上下文长度。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **High-Precision Tasks.** Although DreamZero generalizes broadly across tasks and environments, it inherits limitations common to behavior cloning on tasks requiring sub-centimeter precision, such as key insertion or fine assembly. Our diverse pretraining strategy prioritizes breadth, which may underrepresent the dense demonstrations needed for high-precision manipulation. That said, recent work (Kim et al., 2026) showed promising results indicating that WAMs may actually have an advantage for high-precision manipulation tasks with millimeter tolerance, an encouraging signal that the trade-off between broad generalization and fine-grained dexterity may be reconcilable with further investigation.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **高精度任务。** 尽管 DreamZero 能在多种任务和环境间广泛泛化，但在钥匙插入或精细装配等需要亚厘米精度的任务上，它仍继承了行为克隆的常见局限。我们的多样预训练策略优先考虑广度，这可能导致高精度操作所需的稠密示范代表不足。不过，近期工作（Kim et al., 2026）展示了很有希望的结果，表明 WAM 在毫米容差的高精度操作任务上实际可能具有优势。这是一个鼓舞人心的信号，表明广泛泛化与精细灵巧性之间的权衡可能通过进一步研究得到调和。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Embodiment Design for WAMs.** We hypothesize that two key factors will shape the best robot embodiments for future WAM development: (1) **Degrees of freedom:** higher-DOF robots will require more play data to learn an accurate implicit IDM, because the mapping from visual futures to motor commands grows combinatorially with kinematic complexity. Quantifying the accuracy of implicit IDMs remains a challenge. (2) **Human similarity:** embodiments that more closely resemble humans—particularly humanoids with dexterous manipulation capabilities—may transfer more efficiently despite higher DOF, because they can leverage both motion priors from video pretraining and the massive scale of human egocentric videos. These factors pull in opposite directions—yet human-like embodiments may win out by trading mechanical simplicity for access to web-scale human data, the fuel for next-generation robot foundation models.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **WAM 的机器人形态设计。** 我们假设，有两个关键因素将塑造未来 WAM 开发的最佳机器人形态：（1）**自由度：**高自由度机器人需要更多自由操作数据，才能学得准确的隐式 IDM；这是因为视觉未来到运动指令的映射会随运动学复杂性而组合式增长。如何量化隐式 IDM 的准确性仍是一项挑战。（2）**人类相似性：**与人类更相似的机器人形态，尤其是具备灵巧操作能力的人形机器人，尽管自由度更高，却可能迁移得更高效；它们既能利用视频预训练的运动先验，又能利用海量人类第一视角视频。这两个因素朝相反方向拉扯；但人类相似形态可能最终胜出，因为它们以机械简单性换取访问 web-scale 人类数据的能力，而这些数据将是下一代机器人基础模型的燃料。

# 7. Acknowledgment

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This work would not have been possible without our incredible robot operators: Alec Nagal, Inho Rha, Ava Yazdanfar, Sally Huynh, Rachit Deo, Alaa Eltayeb, Andres Rocha, Brian Dang, Cher Choi, Cristaldo Campos, Ethan Sushil Dhilpe, Jeremy Chimienti, Leilee Naderi, Manish Shah, Manoj Hallegere, Nick Aguilar, Paul Truong, Rahul Sampagaon, Shreya Raj, Nadia Laswi, Amitoj Sandhu, Omkaar Buddhikot, and Wesley Durbano. We also thank Pranav Atreya for their support in integrating DreamZero-Droid into the RoboArena Benchmark. We also thank Danyi Chen, Ming-Yu Liu, and Spencer Huang for their continuous support, and Nishanth Kumar, KR Zentner, Fernando Castaneda Garcia-Rozas, Zhengyi Luo, Yunfan Jiang, and Max Li for fruitful discussions.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 如果没有我们出色的机器人操作员，这项工作不可能完成：Alec Nagal、Inho Rha、Ava Yazdanfar、Sally Huynh、Rachit Deo、Alaa Eltayeb、Andres Rocha、Brian Dang、Cher Choi、Cristaldo Campos、Ethan Sushil Dhilpe、Jeremy Chimienti、Leilee Naderi、Manish Shah、Manoj Hallegere、Nick Aguilar、Paul Truong、Rahul Sampagaon、Shreya Raj、Nadia Laswi、Amitoj Sandhu、Omkaar Buddhikot 以及 Wesley Durbano。我们还感谢 Pranav Atreya 为将 DreamZero-Droid 集成进 RoboArena Benchmark 所提供的支持。我们同时感谢 Danyi Chen、Ming-Yu Liu 和 Spencer Huang 的持续支持，以及 Nishanth Kumar、KR Zentner、Fernando Castaneda Garcia-Rozas、Zhengyi Luo、Yunfan Jiang 和 Max Li 带来的有益讨论。

# Appendices

# Appendix A. Comparison with Alternative World Model Architectures

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The term “world model” encompasses a broad family of approaches beyond video-based prediction. Here we discuss how WAMs differ from these alternatives.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> “世界模型”这一术语涵盖了超越基于视频预测的广泛方法族。本附录讨论 WAM 与这些替代方案的区别。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Latent-Space World Models.** Joint Embedding Predictive Architectures (JEPAs) (Assran et al., 2023, 2025; Bardes et al., 2024; LeCun, 2022) predict future states in abstract latent spaces rather than pixel space, offering computational efficiency and the ability to discard unpredictable details. V-JEPA 2 (Assran et al., 2025) demonstrates this approach in robotics, achieving zero-shot planning on manipulation tasks after post-training on 62 hours of robot data. Similarly, the Dreamer series (Hafner et al., 2019, 2020, 2023, 2025) learns compact latent-dynamics models for model-based reinforcement learning. However, these approaches model dynamics as $p(s_{t+1}\mid s_t,a_t)$—predicting the next state conditioned on the current state and action—and therefore require goal-conditioned planning or search at test time to produce trajectories.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **潜在空间世界模型。** 联合嵌入预测架构（JEPA）（Assran et al., 2023, 2025; Bardes et al., 2024; LeCun, 2022）不在像素空间，而在抽象潜在空间中预测未来状态，因此既具有计算效率，又能丢弃无法预测的细节。V-JEPA 2（Assran et al., 2025）在机器人领域展示了这种方法：在 62 小时机器人数据上后训练后，它在操作任务上实现了零样本规划。类似地，Dreamer 系列（Hafner et al., 2019, 2020, 2023, 2025）学习紧凑的潜在动力学模型，用于基于模型的强化学习。然而，这些方法将动力学建模为 $p(s_{t+1}\mid s_t,a_t)$，即在当前状态和动作条件下预测下一状态；因此，它们在测试时需要目标条件规划或搜索，才能产生轨迹。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **3D Point Cloud World Models.** PointWorld (Huang et al., 2025) unifies state and action in a shared 3D spatial domain, predicting scene dynamics as 3D point flows conditioned on robot actions. This formulation enables embodiment-agnostic learning and real-time integration with model-predictive control (MPC). However, like latent world models, it requires explicit optimization (e.g., MPPI sampling) at inference time to generate action trajectories.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **3D 点云世界模型。** PointWorld（Huang et al., 2025）在共享 3D 空间域中统一状态与动作，将场景动力学预测为机器人动作条件下的 3D 点流。这一形式化支持与机器人形态无关的学习，并可与模型预测控制（MPC）实时集成。但是，与潜在世界模型一样，它在推理时需要显式优化（例如 MPPI 采样）来生成动作轨迹。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Key Distinction.** These alternative approaches share a common characteristic: they model forward dynamics and require separate inverse dynamics models or explicit planning/search procedures at deployment. In contrast, WAMs jointly model $p(o_{t:t+H},a_{t:t+H}\mid o_{0:t},c)$, directly producing action trajectories aligned with predicted visual futures without test-time optimization. This enables real-time closed-loop control at 7Hz—a frequency that would be challenging for search-based methods—while inheriting rich spatiotemporal priors from video pretraining.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **关键区别。** 这些替代方案具有一项共同特征：它们建模前向动力学，并在部署时需要单独的逆动力学模型或显式规划/搜索程序。相比之下，WAM 联合建模 $p(o_{t:t+H},a_{t:t+H}\mid o_{0:t},c)$，无需测试时优化，即可直接产生与预测视觉未来对齐的动作轨迹。这使其能在从视频预训练继承丰富时空先验的同时，实现 7Hz 实时闭环控制；对基于搜索的方法而言，达到这一频率会非常困难。

# Appendix B. Bidirectional vs. Autoregressive WAMs

## Figure 13. Bidirectional vs. Autoregressive WAMs / 双向与自回归 WAM

![Figure 13](assets/page_020_fig_figure_13.png)

**Caption:** Bidirectional vs. Autoregressive WAMs. When the sampling point falls mid-task ($T=20$), bidirectional WAMs must subsample video to align with the language caption, distorting native FPS and degrading video-action alignment. Autoregressive WAMs avoid this trade-off by conditioning on video context, preserving both language-video correspondence and native frame rate.

**Caption[CN]:** 双向与自回归 WAM。当采样点落在任务中段（$T=20$）时，双向 WAM 必须对视频子采样以对齐语言标注，这会扭曲原生 FPS 并降低视频—动作对齐。自回归 WAM 通过以视频上下文为条件避免这一权衡，同时保留语言—视频对应与原生帧率。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The figure's instruction is “Put the black objects into the drawer and close the drawer.” It shows $T=0$, a sampling point at $T=20$, and $T=30$, contrasting bidirectional video subsampling/action sampling mismatches with autoregressive video context, video sampling, and action sampling.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 图中的指令是“把黑色物体放进抽屉，然后关上抽屉”。图中显示 $T=0$、位于 $T=20$ 的采样点以及 $T=30$，对比了双向架构的视频子采样/动作采样错配，与自回归架构的视频上下文、视频采样和动作采样。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Figure 13 illustrates a key challenge for bidirectional WAMs when training closed-loop systems. Given a language annotation in a long-horizon demonstration, the model must learn that the instruction corresponds to a specific video interval. In bidirectional architectures, without subsampling, the model receives a language instruction (e.g., “put the black objects into the drawer”) but usually generates video covering only a fraction of the task interval, causing the language to describe actions not yet visible in the predicted frames. This mismatch causes significant language-following degradation, as measured by an internal video-prediction benchmark.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> Figure 13 说明了在训练闭环系统时，双向 WAM 面临的一项关键挑战。对于长时域示范中的一条语言标注，模型必须学会该指令对应某一特定视频区间。在双向架构中，如果不进行子采样，模型虽接收语言指令（例如“把黑色物体放进抽屉”），但通常只生成覆盖任务区间一小部分的视频，因而语言会描述尚未出现在预测帧中的动作。内部视频预测 benchmark 表明，这一错配会导致语言遵循能力显著下降。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> A natural solution is to subsample the video to match the task-caption interval. However, this creates a new problem for closed-loop training: the model must receive observations from arbitrary points within a task, not just its beginning. When the sampling point falls mid-task (e.g., $T=20$ in Figure 13), subsampling distorts native FPS, making video-action alignment substantially harder to learn.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 一个自然解决方案是对视频子采样，使其匹配任务标注区间。但这会给闭环训练带来新问题：模型必须能接收任务中任意时点的观测，而不仅是任务开始处。当采样点落在任务中段（例如 Figure 13 中的 $T=20$）时，子采样会扭曲原生 FPS，使视频—动作对齐更难学习。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Autoregressive WAMs can sidestep this dilemma. By conditioning on video context rather than subsampling, they preserve both language-video correspondence and native frame rate, enabling tight alignment across all three modalities: language, video, and action.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 自回归 WAM 可以避开这一两难。它们以视频上下文而非子采样为条件，从而同时保留语言—视频对应和原生帧率，实现语言、视频与动作三种模态之间的紧密对齐。

# Appendix C. Model and Training Details

## Figure 14. Attention Strategy of DreamZero / DreamZero 的注意力策略

![Figure 14](WorldModel/World%20Action%20Models%20are%20Zero-shot%20Policies/assets/page_021_fig_figure_14.png)

**Caption:** Attention strategy of DreamZero. (a) QKV self-attention mask for DreamZero training. The Y-axis shows the Query (Q) and the X-axis shows the Key/Value (KV). Given conditioning frames (C0, C1, C2), we train the model to predict the velocities of the next frames (Z1, Z2, Z3) and actions (Y1, Y2, Y3). (b) During inference, we compute the KV-cache of conditional frames and concatenate them to predict the action and frames. For example, Y3 (action) is able to attend to C0, C1, and C2, taking previous visual observations into account as history to predict current actions during both training and inference. Note that C0, C1, and C2 during inference are replaced with GT observations.

**Caption[CN]:** DreamZero 的注意力策略。(a) DreamZero 训练时的 QKV 自注意力遮罩。Y 轴表示 Query（Q），X 轴表示 Key/Value（KV）。给定条件帧（C0、C1、C2），我们训练模型预测后续帧（Z1、Z2、Z3）与动作（Y1、Y2、Y3）的速度。(b) 推理期间，我们计算条件帧的 KV 缓存并将它们拼接，以预测动作和帧。例如，Y3（动作）可以关注 C0、C1 和 C2；在训练与推理中，它都会把以前的视觉观测当作历史，来预测当前动作。请注意，推理时的 C0、C1 和 C2 被替换为真值（GT）观测。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We visualize the attention mask for training and inference in Figure 14. For DreamZero, we set each chunk to $K=2$ latent frames. Preliminary results showed empirically that $K=2$ outperforms $K=1$. We set the number of chunks to $M=4$ by default. If trajectory length is shorter than $M=4$, $M$ can be smaller than 4. For AgiBot training data, video is sampled at 5 FPS and actions at 30Hz. We use an action horizon of $H=48$; therefore, video and action span 1.6 seconds per chunk. For DROID training, video is sampled at 5 FPS and actions at 15Hz. We use an action horizon of $H=24$; therefore, as with AgiBot, video and action span 1.6 seconds per chunk. Maximum context length is 8 latent frames ($4\times2$), equivalent to 33 raw frames spanning 6.6 seconds. We leave increasing visual context for WAMs to future work.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Figure 14 可视化了训练与推理时的注意力遮罩。对 DreamZero，我们将每个块设为 $K=2$ 个潜在帧。初步实验表明，$K=2$ 在经验上优于 $K=1$。默认块数设为 $M=4$；如果轨迹长度短于 $M=4$，则 $M$ 可以小于 4。对 AgiBot 训练数据，视频以 5 FPS 采样，动作以 30Hz 采样。我们使用动作时域 $H=48$，因此每个块的视频与动作均跨越 1.6 秒。对 DROID 训练，视频以 5 FPS 采样，动作以 15Hz 采样。我们使用动作时域 $H=24$，因此与 AgiBot 一样，每个块的视频和动作均跨越 1.6 秒。最大上下文长度为 8 个潜在帧（$4\times2$），相当于 33 个原始帧，跨越 6.6 秒。我们将增加 WAM 视觉上下文留作未来工作。

## Algorithm 1. DreamZero Training (Flow Matching)

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Algorithm 1 DreamZero Training (Flow Matching)**
>
> 1: **Input:** Dataset $\mathcal{D}$, Text condition $c$  
> 2: **Hyperparams:** Number of chunks $M$  
> 3: **Model:** $u_\theta$ (Joint Video-Action DiT)  
> 4: **while** not converged **do**  
> 5: &nbsp;&nbsp;Sample trajectory $\tau\sim\mathcal{D}$  
> 6: &nbsp;&nbsp;Encode video to clean latents $z^1_{1:M}$, normalize actions $a^1_{1:M}$  
> 7: &nbsp;&nbsp;Split $\tau$ into $M$ chunks  
> 8: &nbsp;&nbsp;**for** $k=1,\ldots,M$ **do** $\triangleleft$ Chunk-wise Training  
> 9: &nbsp;&nbsp;&nbsp;&nbsp;Define clean context $\mathcal{C}_k\leftarrow\{(z^j_1,a^j_1)\}_{j=1}^{k-1}$ $\triangleleft$ TF History  
> 10: &nbsp;&nbsp;&nbsp;&nbsp;Sample timestep $t_k\sim\mathcal{U}(0,1)$  
> 11: &nbsp;&nbsp;&nbsp;&nbsp;`// Optional: DreamZero-Flash Decoupling`  
> 12: &nbsp;&nbsp;&nbsp;&nbsp;**if** `Flash Mode` **then**  
> 13: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$t_{vid}\sim\mathrm{Beta}(7,1)$, $t_{act}\sim\mathcal{U}(0,1)$  
> 14: &nbsp;&nbsp;&nbsp;&nbsp;**else**  
> 15: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$t_{vid}\leftarrow t_k$, $t_{act}\leftarrow t_k$  
> 16: &nbsp;&nbsp;&nbsp;&nbsp;**end if**  
> 17: &nbsp;&nbsp;&nbsp;&nbsp;Sample noise $z^k_0,a^k_0\sim\mathcal{N}(0,I)$  
> 18: &nbsp;&nbsp;&nbsp;&nbsp;Interpolate (Eq. 2):  
> 19: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$z^k_t\leftarrow t_{vid}z^k_1+(1-t_{vid})z^k_0$  
> 20: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$a^k_t\leftarrow t_{act}a^k_1+(1-t_{act})a^k_0$  
> 21: &nbsp;&nbsp;&nbsp;&nbsp;Predict velocity:  
> 22: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$v_{pred}\leftarrow u_\theta([z^k_t,a^k_t];\mathcal{C}_k,c,q_k,t_k)$  
> 23: &nbsp;&nbsp;&nbsp;&nbsp;Target vel. $v_k:=[z^k_1,a^k_1]-[z^k_0,a^k_0]$  
> 24: &nbsp;&nbsp;&nbsp;&nbsp;Loss $\mathcal{L}\leftarrow\lVert v_{pred}-v_k\rVert^2$ $\triangleleft$ Eq. 3  
> 25: &nbsp;&nbsp;&nbsp;&nbsp;Update $\theta\leftarrow\theta-\eta\nabla\mathcal{L}$  
> 26: &nbsp;&nbsp;**end for**  
> 27: **end while**

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **Algorithm 1 DreamZero 训练（流匹配）**
>
> 1: **输入：**数据集 $\mathcal{D}$，文本条件 $c$  
> 2: **超参数：**块数 $M$  
> 3: **模型：**$u_\theta$（联合视频—动作 DiT）  
> 4: **while** 尚未收敛 **do**  
> 5: &nbsp;&nbsp;采样轨迹 $\tau\sim\mathcal{D}$  
> 6: &nbsp;&nbsp;将视频编码为干净潜变量 $z^1_{1:M}$，归一化动作 $a^1_{1:M}$  
> 7: &nbsp;&nbsp;将 $\tau$ 分为 $M$ 个块  
> 8: &nbsp;&nbsp;**for** $k=1,\ldots,M$ **do** $\triangleleft$ 分块训练  
> 9: &nbsp;&nbsp;&nbsp;&nbsp;定义干净上下文 $\mathcal{C}_k\leftarrow\{(z^j_1,a^j_1)\}_{j=1}^{k-1}$ $\triangleleft$ TF 历史  
> 10: &nbsp;&nbsp;&nbsp;&nbsp;采样时间步 $t_k\sim\mathcal{U}(0,1)$  
> 11: &nbsp;&nbsp;&nbsp;&nbsp;`// 可选：DreamZero-Flash 解耦`  
> 12: &nbsp;&nbsp;&nbsp;&nbsp;**if** `Flash Mode` **then**  
> 13: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$t_{vid}\sim\mathrm{Beta}(7,1)$，$t_{act}\sim\mathcal{U}(0,1)$  
> 14: &nbsp;&nbsp;&nbsp;&nbsp;**else**  
> 15: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$t_{vid}\leftarrow t_k$，$t_{act}\leftarrow t_k$  
> 16: &nbsp;&nbsp;&nbsp;&nbsp;**end if**  
> 17: &nbsp;&nbsp;&nbsp;&nbsp;采样噪声 $z^k_0,a^k_0\sim\mathcal{N}(0,I)$  
> 18: &nbsp;&nbsp;&nbsp;&nbsp;插值（Eq. 2）：  
> 19: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$z^k_t\leftarrow t_{vid}z^k_1+(1-t_{vid})z^k_0$  
> 20: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$a^k_t\leftarrow t_{act}a^k_1+(1-t_{act})a^k_0$  
> 21: &nbsp;&nbsp;&nbsp;&nbsp;预测速度：  
> 22: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$v_{pred}\leftarrow u_\theta([z^k_t,a^k_t];\mathcal{C}_k,c,q_k,t_k)$  
> 23: &nbsp;&nbsp;&nbsp;&nbsp;目标速度 $v_k:=[z^k_1,a^k_1]-[z^k_0,a^k_0]$  
> 24: &nbsp;&nbsp;&nbsp;&nbsp;损失 $\mathcal{L}\leftarrow\lVert v_{pred}-v_k\rVert^2$ $\triangleleft$ Eq. 3  
> 25: &nbsp;&nbsp;&nbsp;&nbsp;更新 $\theta\leftarrow\theta-\eta\nabla\mathcal{L}$  
> 26: &nbsp;&nbsp;**end for**  
> 27: **end while**

## Algorithm 2. DreamZero Inference (Closed-Loop Control)

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Algorithm 2 DreamZero Inference (Closed-Loop Control)**
>
> 1: **Input:** Instruction $c$, Initial Image $o_{init}$, State $q_{init}$  
> 2: **Hyperparams:** Steps $N$, Cache Thresh $\epsilon$  
> 3: **Init:** $\mathcal{KV}\leftarrow\emptyset$, $v_{prev}\leftarrow\emptyset$, $q_{curr}\leftarrow q_{init}$  
> 4: `// 1. Prefill Cache (Context Phase, t = 0)`  
> 5: $z_{init}\leftarrow\mathrm{VAE}(o_{init})$  
> 6: `// Pass clean video, no action/state`  
> 7: $(\cdot,\cdot,\mathcal{KV})\leftarrow u_\theta([z_{init},\emptyset];\mathcal{KV},c,\emptyset,t=0,\texttt{update=True})$  
> 8: `// 2. Autoregressive Loop`  
> 9: **while** task not done **do**  
> 10: &nbsp;&nbsp;Sample $x_0=[z_0,a_0]\sim\mathcal{N}(0,I)$ $\triangleleft$ Noise at $t=0$  
> 11: &nbsp;&nbsp;`// Joint Denoising (Flow Matching t: 0 → 1)`  
> 12: &nbsp;&nbsp;**for** $i=0\ldots N-1$ **do**  
> 13: &nbsp;&nbsp;&nbsp;&nbsp;$t_i,t_{i+1}\leftarrow\mathrm{Scheduler}(i,N)$  
> 14: &nbsp;&nbsp;&nbsp;&nbsp;`// Optimization: DiT Caching`  
> 15: &nbsp;&nbsp;&nbsp;&nbsp;**if** $v_{prev}\ne\emptyset$ and $\mathrm{CosSim}(v_{prev},v_{last})>\epsilon$ **then**  
> 16: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$v_i\leftarrow v_{prev}$  
> 17: &nbsp;&nbsp;&nbsp;&nbsp;**else**  
> 18: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$(v_i^{vid},v_i^{act},\cdot)\leftarrow u_\theta(x_{t_i};\mathcal{KV},c,q_{curr},t_i,\texttt{update=False})$  
> 19: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$v_i\leftarrow[v_i^{vid},v_i^{act}]$  
> 20: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$v_{prev}\leftarrow v_i$  
> 21: &nbsp;&nbsp;&nbsp;&nbsp;**end if**  
> 22: &nbsp;&nbsp;&nbsp;&nbsp;`// Solver Step`  
> 23: &nbsp;&nbsp;&nbsp;&nbsp;$x_{t_{i+1}}\leftarrow x_{t_i}+\mathrm{Step}(v_i,t_i,t_{i+1})$  
> 24: &nbsp;&nbsp;**end for**  
> 25: &nbsp;&nbsp;`// 3. Execution & Cache Update`  
> 26: &nbsp;&nbsp;$\hat{a}\leftarrow\mathrm{Filter}(x^{action}_1)$ $\triangleleft$ Clean Action $t=1$  
> 27: &nbsp;&nbsp;Async Execute $\hat{a}$ on Robot  
> 28: &nbsp;&nbsp;`// Critical: Inject Ground Truth (t = 0)`  
> 29: &nbsp;&nbsp;Real observation $o_{real},q_{real}$  
> 30: &nbsp;&nbsp;$q_{curr}\leftarrow q_{real}$, $z_{real}\leftarrow\mathrm{VAE}(o_{real})$  
> 31: &nbsp;&nbsp;$(\cdot,\cdot,\mathcal{KV})\leftarrow u_\theta([z_{real},\emptyset];\mathcal{KV},c,\emptyset,t=0,\texttt{update=True})$  
> 32: &nbsp;&nbsp;`*Discard predicted video latent from x_1`  
> 33: **end while**

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **Algorithm 2 DreamZero 推理（闭环控制）**
>
> 1: **输入：**指令 $c$，初始图像 $o_{init}$，状态 $q_{init}$  
> 2: **超参数：**步数 $N$，缓存阈值 $\epsilon$  
> 3: **初始化：**$\mathcal{KV}\leftarrow\emptyset$，$v_{prev}\leftarrow\emptyset$，$q_{curr}\leftarrow q_{init}$  
> 4: `// 1. 预填充缓存（上下文阶段，t = 0）`  
> 5: $z_{init}\leftarrow\mathrm{VAE}(o_{init})$  
> 6: `// 传入干净视频，不传动作/状态`  
> 7: $(\cdot,\cdot,\mathcal{KV})\leftarrow u_\theta([z_{init},\emptyset];\mathcal{KV},c,\emptyset,t=0,\texttt{update=True})$  
> 8: `// 2. 自回归循环`  
> 9: **while** 任务尚未完成 **do**  
> 10: &nbsp;&nbsp;采样 $x_0=[z_0,a_0]\sim\mathcal{N}(0,I)$ $\triangleleft$ $t=0$ 时的噪声  
> 11: &nbsp;&nbsp;`// 联合去噪（流匹配 t: 0 → 1）`  
> 12: &nbsp;&nbsp;**for** $i=0\ldots N-1$ **do**  
> 13: &nbsp;&nbsp;&nbsp;&nbsp;$t_i,t_{i+1}\leftarrow\mathrm{Scheduler}(i,N)$  
> 14: &nbsp;&nbsp;&nbsp;&nbsp;`// 优化：DiT 缓存`  
> 15: &nbsp;&nbsp;&nbsp;&nbsp;**if** $v_{prev}\ne\emptyset$ 且 $\mathrm{CosSim}(v_{prev},v_{last})>\epsilon$ **then**  
> 16: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$v_i\leftarrow v_{prev}$  
> 17: &nbsp;&nbsp;&nbsp;&nbsp;**else**  
> 18: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$(v_i^{vid},v_i^{act},\cdot)\leftarrow u_\theta(x_{t_i};\mathcal{KV},c,q_{curr},t_i,\texttt{update=False})$  
> 19: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$v_i\leftarrow[v_i^{vid},v_i^{act}]$  
> 20: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$v_{prev}\leftarrow v_i$  
> 21: &nbsp;&nbsp;&nbsp;&nbsp;**end if**  
> 22: &nbsp;&nbsp;&nbsp;&nbsp;`// 求解器步骤`  
> 23: &nbsp;&nbsp;&nbsp;&nbsp;$x_{t_{i+1}}\leftarrow x_{t_i}+\mathrm{Step}(v_i,t_i,t_{i+1})$  
> 24: &nbsp;&nbsp;**end for**  
> 25: &nbsp;&nbsp;`// 3. 执行与缓存更新`  
> 26: &nbsp;&nbsp;$\hat{a}\leftarrow\mathrm{Filter}(x^{action}_1)$ $\triangleleft$ $t=1$ 时的干净动作  
> 27: &nbsp;&nbsp;在机器人上异步执行 $\hat{a}$  
> 28: &nbsp;&nbsp;`// 关键：注入真值（t = 0）`  
> 29: &nbsp;&nbsp;真实观测 $o_{real},q_{real}$  
> 30: &nbsp;&nbsp;$q_{curr}\leftarrow q_{real}$，$z_{real}\leftarrow\mathrm{VAE}(o_{real})$  
> 31: &nbsp;&nbsp;$(\cdot,\cdot,\mathcal{KV})\leftarrow u_\theta([z_{real},\emptyset];\mathcal{KV},c,\emptyset,t=0,\texttt{update=True})$  
> 32: &nbsp;&nbsp;`*丢弃 x_1 中预测的视频潜变量`  
> 33: **end while**

# Appendix D. Real-time Execution Details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This appendix provides additional details on the system-, implementation-, and model-level optimizations introduced in Section 3.2.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本附录提供第 3.2 节所介绍的系统级、实现级与模型级优化的更多细节。

## D.1. System-level Optimizations

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **CFG Parallelism.** To address the computational bottleneck inherent to DiT, we employ Classifier-Free Guidance (CFG) parallelism. Standard CFG requires two distinct model evaluations—conditional and unconditional forward passes—which are typically executed sequentially. We parallelize these operations by distributing conditioned and null-conditioned score estimates across two independent GPUs. This reduces latency per diffusion step by nearly half, with no impact on overall model quality.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **CFG 并行。** 为解决 DiT 固有的计算瓶颈，我们采用无分类器引导（CFG）并行。标准 CFG 需要两次不同的模型评估，即有条件和无条件前向计算，两者通常串行执行。我们把有条件和空条件分数估计分布在两张独立 GPU 上，从而将每个扩散步的延迟减少近一半，且不影响整体模型质量。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **DiT Caching.** The iterative nature of DiT inference imposes a significant computational bottleneck for real-time applications. Previous efforts have focused on training-free caching techniques that exploit temporal redundancy across diffusion steps. TeaCache (Liu et al., 2024) uses the relative $L_1$ difference between timestep-embedding-modulated inputs as a heuristic for estimating output variance and skipping redundant computations, while TaylorSeer (Liu et al., 2025) uses higher-order Taylor expansions to extrapolate future latent states from historical derivatives. In DreamZero, we implement a caching mechanism that exploits the directional consistency of velocity vectors learned during flow matching.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **DiT 缓存。** DiT 推理的迭代性给实时应用造成了显著计算瓶颈。以往工作主要研究免训练缓存技术，利用不同扩散步之间的时间冗余。TeaCache（Liu et al., 2024）把经时间步嵌入调制的输入之间的相对 $L_1$ 差异当作启发式信号，以估计输出方差并跳过冗余计算；TaylorSeer（Liu et al., 2025）则用高阶 Taylor 展开从历史导数外推未来潜在状态。在 DreamZero 中，我们实现了一种缓存机制，利用流匹配期间学得的速度向量方向一致性。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> During inference, the model tracks cosine similarity between successive velocity predictions. When this metric exceeds a predefined threshold $\tau$, the model bypasses the DiT forward pass for a window of several steps by reusing the cached velocity vector. This adaptive scheduling concentrates computational resources on critical trajectory updates, reducing the average number of DiT steps from 16 to 4 with minimal degradation in predicted-video and action fidelity.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 推理时，模型跟踪相邻速度预测之间的余弦相似度。当该指标超过预定义阈值 $\tau$ 时，模型会通过复用缓存速度向量，在数个步的窗口中跳过 DiT 前向计算。这种自适应调度把计算资源集中在关键轨迹更新上，将平均 DiT 步数从 16 减少到 4，同时对预测视频与动作保真度的损害很小。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Asynchronous Execution.** Sequential execution of action blocks introduces stalls while waiting for upstream models to produce the next chunk, making the robot more open-loop and less responsive to real-time state changes, especially with large chunk sizes. We use an asynchronous execution mechanism that decouples model inference from action execution, allowing both stages to run concurrently. The motion controller always executes the most recent action scheduled for the current timestamp, while the inference module always uses the latest observation.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **异步执行。** 动作块串行执行时，系统会因等待上游模型产生下一块而停顿，使机器人更偏开环，也更难响应实时状态变化；当块较大时尤其如此。我们使用异步执行机制将模型推理与动作执行解耦，允许两个阶段并发运行。运动控制器总是执行为当前时间戳调度的最新动作，推理模块则总是使用最新观测。

## D.2. Implementation-level Optimizations

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Torch Compile and CUDA Graphs.** Inference is predominantly CPU-bound because of kernel-launch overheads and Python execution. We use `torch.compile` with CUDA Graphs (`mode="reduce-overhead"`) and enforce full graph capture (`fullgraph=True`) to eliminate graph breaks. Besides reducing CPU overhead, `torch.compile` reduces memory-bandwidth requirements through operator fusion. We compile five model components: diffusion transformer, scheduler, text encoder, image encoder, and VAE. We enforce static shapes (`dynamic=False`), which cause multiple recompilations during the first inference trajectory as KV-cache shape evolves. From the second trajectory onward, inference proceeds without recompilation. For error-free compilation, we refactor the model to follow a functional-programming paradigm: the KV cache is explicitly passed as input and returned as output by the compiled function.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **Torch Compile 与 CUDA Graphs。** 由于内核启动开销和 Python 执行，推理主要受 CPU 限制。我们使用带 CUDA Graphs 的 `torch.compile`（`mode="reduce-overhead"`），并强制完整图捕获（`fullgraph=True`）以消除 graph break。除降低 CPU 开销外，`torch.compile` 还通过算子融合减少内存带宽需求。我们对五个模型组件应用编译：扩散 Transformer、调度器、文本编码器、图像编码器和 VAE。我们强制使用静态 shape（`dynamic=False`）；由于 KV 缓存 shape 会演化，这会在第一条推理轨迹中造成多次重新编译。从第二条轨迹开始，推理无需重新编译。为确保无错编译，我们按函数式编程范式重构模型：KV 缓存被显式作为输入传入，并作为编译函数的输出返回。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> **Post-Training Quantization.** We implement a mixed-precision strategy using NVIDIA Model Optimizer (NVIDIA Corporation, 2024) on Blackwell (SM100) architecture. We quantize model weights and activations to NVFP4 (E2M1), while maintaining sensitive QKV projections and Softmax operations in FP8 (E4M3). To preserve numerical stability, we use FP16 accumulation for nonlinear operations including LayerNorm and RoPE. This configuration improves latency with negligible effect on generated-video and action quality.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> **训练后量化。** 我们在 Blackwell（SM100）架构上使用 NVIDIA Model Optimizer（NVIDIA Corporation, 2024）实现混合精度策略。我们将模型权重和激活量化为 NVFP4（E2M1），同时使敏感 QKV 投影和 Softmax 操作保持 FP8（E4M3）。为保持数值稳定性，包括 LayerNorm 和 RoPE 在内的非线性操作采用 FP16 累加。这一配置改善了延迟，同时对生成视频与动作质量的影响可忽略。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> **Kernel-Level Enhancements.** We use the cuDNN backend for dot-product attention through PyTorch Scaled Dot-Product Attention (SDPA), requiring PyTorch version $\geq2.9$. Earlier versions of the Transformer Engine library may also access these efficient cuDNN kernels.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **内核级增强。** 我们通过 PyTorch Scaled Dot-Product Attention（SDPA）使用 cuDNN 后端计算点积注意力，要求 PyTorch 版本 $\geq2.9$。较早版本的 Transformer Engine 库也可访问这些高效 cuDNN 内核。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **Scheduler Optimizations.** The initial Flow UniPC scheduler (Zhao et al., 2023) implementation required CPU execution for several operations, causing frequent CPU–GPU synchronization and GPU stalls. We migrated these operations to GPU, eliminating unnecessary CPU overhead.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **调度器优化。** 初始 Flow UniPC 调度器（Zhao et al., 2023）的实现要求若干操作在 CPU 上执行，从而造成频繁的 CPU–GPU 同步与 GPU 停顿。我们把这些操作迁移到 GPU，消除了不必要的 CPU 开销。

## D.3. Model-level Optimizations — DreamZero-Flash

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> In the standard DreamZero formulation, video and action modalities share the same denoising timestep $t_k$:

$$
t_k^{\mathrm{video}}=t_k^{\mathrm{action}}=t_k,
\qquad t_k\sim\mathcal{U}(0,1).
\tag{4}
$$

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 在标准 DreamZero 形式化中，视频与动作模态共享同一去噪时间步 $t_k$，如式（4）所示。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> DreamZero-Flash decouples these schedules by biasing video timesteps toward lower values (higher noise) while keeping action timesteps uniform:

$$
t_k^{\mathrm{video}}=1-\eta,
\qquad \eta\sim\mathrm{Beta}(\alpha,\beta),
\qquad t_k^{\mathrm{action}}\sim\mathcal{U}(0,1).
\tag{5}
$$

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> DreamZero-Flash 使视频时间步偏向较低值（更高噪声），同时保持动作时间步均匀，从而按式（5）解耦这两组日程。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> Here $\alpha>\beta$ (e.g., $\alpha=7$, $\beta=1$). Because $\mathrm{Beta}(\alpha,\beta)$ with $\alpha>\beta$ concentrates mass near $\eta\approx1$, the transformed variable $t_k^{\mathrm{video}}=1-\eta$ is biased toward 0, corresponding to high-noise video states. The noisy samples become:

$$
z^k_{t_k^{\mathrm{video}}}
=t_k^{\mathrm{video}}z^k_1+
\left(1-t_k^{\mathrm{video}}\right)z^k_0,
\qquad
a^k_{t_k^{\mathrm{action}}}
=t_k^{\mathrm{action}}a^k_1+
\left(1-t_k^{\mathrm{action}}\right)a^k_0.
\tag{6}
$$

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 其中 $\alpha>\beta$（例如 $\alpha=7$、$\beta=1$）。由于当 $\alpha>\beta$ 时，$\mathrm{Beta}(\alpha,\beta)$ 的质量集中在 $\eta\approx1$ 附近，变换后的变量 $t_k^{\mathrm{video}}=1-\eta$ 会偏向 0，这对应于高噪声视频状态。含噪样本因而按式（6）给出。

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> For $\mathrm{Beta}(7,1)$, $\mathbb{E}[\eta]=0.875$, yielding $\mathbb{E}[t_k^{\mathrm{video}}]=0.125$ compared with 0.5 in the coupled setting. During training, this exposes the model to configurations in which actions must be predicted from predominantly noisy visual context (Figure 5), aligning training with rapid-action-denoising inference, where actions denoise from noise level $1\rightarrow0$ in one step while video remains partially noisy.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> 对 $\mathrm{Beta}(7,1)$，$\mathbb{E}[\eta]=0.875$，因而 $\mathbb{E}[t_k^{\mathrm{video}}]=0.125$；而在耦合设定中该值为 0.5。训练期间，模型因而会遇到必须从以含噪为主的视觉上下文中预测动作的配置（Figure 5）。这使训练与快速动作去噪推理对齐：动作在一步内从噪声水平 $1\rightarrow0$ 去噪，而视频仍部分含噪。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> **Action Chunk Smoothing.** Generated action chunks may contain high-frequency denoising noise. We filter them to ensure stable real-world behavior: first upsampling an action chunk to $2\times$ resolution by cubic interpolation, then applying a Savitzky–Golay filter (window size 21, polynomial order 3) to suppress noise while preserving trajectory shape, and finally downsampling to the original resolution.

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> **动作块平滑。** 生成动作块可能含有来自去噪的高频噪声。我们对其进行滤波，以确保真实世界行为稳定：首先通过三次插值把动作块上采样到 $2\times$ 分辨率；然后应用 Savitzky–Golay 滤波器（窗口大小 21，多项式阶数 3），在保留轨迹形状的同时抑制噪声；最后下采样回原始分辨率。

# Appendix E. AgiBot Diverse Data Collection Strategy

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Our data-collection philosophy prioritizes diversity over repetition. Unlike conventional approaches that collect hundreds of demonstrations per task in controlled laboratory settings, we collect data across 22 real-world environments spanning homes, restaurants, supermarkets, coffee shops, offices, warehouses, laboratories, and hotels (Figure 15).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们的数据收集理念将多样性置于重复性之上。与在受控实验室环境中为每个任务收集数百个示范的常规方法不同，我们在 22 个真实世界环境中收集数据，覆盖住宅、餐厅、超市、咖啡店、办公室、仓库、实验室和酒店（Figure 15）。

## E.1. Daily Collection Workflow

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Each day, teleoperators receive a printed task sheet listing the tasks available for their assigned area (e.g., kitchen area, checkout counter). For each episode, they select three tasks—usually very coarse-grained tasks such as “tidy up”—from the sheet and execute them consecutively. Each task typically takes 1–2 minutes, yielding episodes of approximately 5 minutes.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 每天，遥操员都会收到一张打印任务表，列出分配区域（例如厨房区、收银台）中可执行的任务。在每个 episode 中，他们从任务表中选择三个任务，这些任务通常非常粗粒度，例如“整理”，并连续执行。每个任务通常需要 1–2 分钟，从而形成约 5 分钟的 episode。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> At the end of each day, teleoperators log the frequency count for every task. Once a task has been collected in 50 episodes, it is deprecated and removed from the task sheet. Teleoperators are incentivized to propose new tasks, which they inevitably must do as existing tasks become deprecated. This mechanism continuously expands the task distribution throughout collection, yielding a long tail of diverse behaviors.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 每天结束时，遥操员记录每个任务的频次计数。一旦某个任务已在 50 个 episode 中采集，它便会被废弃并从任务表中删除。我们鼓励遥操员提出新任务；随着现有任务逐渐废弃，他们最终必须这样做。这一机制在整个数据收集过程中持续扩展任务分布，产生多样行为的长尾。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Because we prioritize utility over repetition, our tasks are naturally more coarse-grained than those in typical robot-learning datasets. Examples include organizing items, cleaning garbage from the ground, returning shopping baskets, tidying toy boxes, tidying tables, and hanging clothes—but the complete set grows organically as collection proceeds.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 由于我们把效用置于重复性之上，这些任务天然比典型机器人学习数据集中的任务更粗粒度。示例包括整理物品、清理地面垃圾、归还购物篮、整理玩具箱、整理桌面和悬挂衣物；但随着收集推进，完整任务集会自然增长。

## E.2. Multi-Task Episode Structure

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The three-task episode structure serves two purposes: it maximizes diversity within each episode and encourages the model to learn smooth task transitions. For example, one episode might involve (1) clearing dishes from a table, (2) wiping the table surface, and (3) organizing condiments. This design yields an average of 42 subtasks per episode (Figure 6), significantly more than typical single-task datasets.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 三任务 episode 结构有两个目的：最大化每个 episode 内的多样性，并促使模型学习平滑的任务转换。例如，一个 episode 可能包含：（1）清走桌上餐具；（2）擦拭桌面；以及（3）整理调味品。这一设计使每个 episode 平均包含 42 个子任务（Figure 6），显著多于典型单任务数据集。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The combination of environmental diversity, task deprecation with forced expansion, and multi-task episodes produces a heterogeneous dataset that differs substantially from conventional robot-learning corpora. Rather than learning narrow task-specific policies, DreamZero learns generalizable skills that transfer across environments and tasks.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 环境多样性、任务废弃与强制扩展，再加上多任务 episode，三者结合产生了一个与传统机器人学习语料显著不同的异构数据集。DreamZero 不是学习狭窄的任务专用策略，而是学习可在环境和任务之间迁移的可泛化技能。

## Figure 15. Data Collection Environments / 数据收集环境

![Figure 15](assets/page_025_fig_figure_15.png)

**Caption:** Data Collection Environments. We collect teleoperation data across 22 diverse real-world environments, including offices, laboratories, restaurants, supermarkets, coffee shops, warehouses, homes, hotels, and retail stores. This diversity enables DreamZero to generalize to unseen environments without task-specific fine-tuning.

**Caption[CN]:** 数据收集环境。我们在 22 个多样的真实世界环境中收集遥操数据，包括办公室、实验室、餐厅、超市、咖啡店、仓库、住宅、酒店和零售店。这种多样性使 DreamZero 无需任务专用微调即可泛化到未见环境。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Examples of the coarse-grained tasks are available at <https://dreamzero0.github.io/training_data_gallery/>. The videos shown on the website concatenate the individual coarse-grained tasks.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 粗粒度任务的示例可见 <https://dreamzero0.github.io/training_data_gallery/>。该网站展示的视频将各个粗粒度任务拼接在一起。

# Appendix F. AgiBot Evaluation Details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We provide the evaluation setup for seen tasks in Table 5 and unseen tasks in Table 6 for AgiBot. Each row in the source shows the initial frame and instruction for 4 robots. We conduct 2 rollouts per robot for each task by varying the objects, locations, and robot arm used for the task. The source table mostly shows evaluation using the left arm. Under the exact-target policy, image cells are omitted below, but every category, task, configuration, and instruction is transcribed in searchable form.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Table 5 和 Table 6 分别给出 AgiBot 已见任务与未见任务的评估设置。源表中的每一行展示 4 台机器人的初始帧与指令。对每个任务，我们通过变化物体、位置和所用机器人手臂，在每台机器人上执行 2 次 rollout。源表大多展示使用左臂的评估。根据精确目标策略，下文省略图像单元格，但以可搜索形式完整转录每个类别、任务、配置与指令。

## Table 5. Seen Tasks Evaluation Setup for AgiBot G1

| Category | Task No. | Task | Config. | Exact English instruction | 中文指令 |
|---|---:|---|---:|---|---|
| PnP Easy | 1 | PnP Fruit | 1 | The left arm picks up the Banana on the table and places it in the Blue Plate. | 左臂拿起桌上的香蕉，并将其放进蓝色盘子。 |
| PnP Easy | 1 | PnP Fruit | 2 | The left arm picks up the lime on the table and places it on the light green plate. | 左臂拿起桌上的青柠，并将其放在浅绿色盘子上。 |
| PnP Easy | 1 | PnP Fruit | 3 | The left arm picks up the peach on the table and places it on the baking pan. | 左臂拿起桌上的桃子，并将其放在烤盘上。 |
| PnP Easy | 1 | PnP Fruit | 4 | The left arm picks up the green pear on the table and places it on the blue checkered bowl. | 左臂拿起桌上的绿梨，并将其放在蓝色格纹碗上。 |
| PnP Easy | 2 | Taking out Fruit | 1 | The left arm picks up the Mango from the plastic bag and places it into the Wooden Basket | 左臂从塑料袋中拿起芒果，并将其放入木篮。 |
| PnP Easy | 2 | Taking out Fruit | 2 | The left arm picks up the yellow pear from the plastic bag and places it onto the blue tray. | 左臂从塑料袋中拿起黄梨，并将其放在蓝色托盘上。 |
| PnP Easy | 2 | Taking out Fruit | 3 | The left arm picks up the purple grapes from the plastic bag and places it into the brown basket. | 左臂从塑料袋中拿起紫色葡萄，并将其放入棕色篮子。 |
| PnP Easy | 2 | Taking out Fruit | 4 | The left arm picks up the watermelon from the plastic bag and places it onto the Blue Plate. | 左臂从塑料袋中拿起西瓜，并将其放在蓝色盘子上。 |
| PnP Easy | 3 | Wipe the Mess | 1 | The left arm uses a sponge to wipe the coffee spill off the table. | 左臂使用海绵把桌上洒出的咖啡擦掉。 |
| PnP Easy | 3 | Wipe the Mess | 2 | The left arm used a black cloth to wipe the white powder off the table. | 左臂使用黑色抹布把桌上的白色粉末擦掉。 |
| PnP Easy | 3 | Wipe the Mess | 3 | The left arm uses a napkin to wipe the creamer spill off the table. | 左臂使用餐巾把桌上洒出的奶精擦掉。 |
| PnP Easy | 3 | Wipe the Mess | 4 | The left arm used a paper towel to wipe the water off the table. | 左臂使用纸巾把桌上的水擦掉。 |
| PnP Hard | 4 | PnP Fork/Spoon | 1 | The left arm picks up the Pink Fork from the table and places it onto the blue plate. | 左臂拿起桌上的粉色叉子，并将其放在蓝色盘子上。 |
| PnP Hard | 4 | PnP Fork/Spoon | 2 | The left arm picks up the orange fork from the table and places it into the glass cup | 左臂拿起桌上的橙色叉子，并将其放入玻璃杯。 |
| PnP Hard | 4 | PnP Fork/Spoon | 3 | The left arm picks up the light blue fork from the table and places it onto the orange plate | 左臂拿起桌上的浅蓝色叉子，并将其放在橙色盘子上。 |
| PnP Hard | 4 | PnP Fork/Spoon | 4 | The left arm picks up the green fork from the table and places it into the blue plate. | 左臂拿起桌上的绿色叉子，并将其放入蓝色盘子。 |
| PnP Hard | 5 | Put Pen in Holder | 1 | The left arm picks up the Red Marker pen from the table and placed it into the pen holder. | 左臂拿起桌上的红色记号笔，并将其放入笔筒。 |
| PnP Hard | 5 | Put Pen in Holder | 2 | The left arm picked up the black marker from the table and placed it into the pen holder. | 左臂拿起桌上的黑色记号笔，并将其放入笔筒。 |
| PnP Hard | 5 | Put Pen in Holder | 3 | The left arm picked up the white marker pen from the table and placed it into the pen holder. | 左臂拿起桌上的白色记号笔，并将其放入笔筒。 |
| PnP Hard | 5 | Put Pen in Holder | 4 | The left arm picked up the mechanical pencil from the table and placed it into the pen holder. | 左臂拿起桌上的自动铅笔，并将其放入笔筒。 |
| PnP Hard | 6 | Put Cup on Coaster | 1 | The left arm picks up the clear cup from the table and places it on the grey coaster. | 左臂拿起桌上的透明杯，并将其放在灰色杯垫上。 |
| PnP Hard | 6 | Put Cup on Coaster | 2 | The left arm picks up the plastic cup from the table and places it on the blue coaster. | 左臂拿起桌上的塑料杯，并将其放在蓝色杯垫上。 |
| PnP Hard | 6 | Put Cup on Coaster | 3 | The left arm picks up the plastic cup from the table and places it on the white coaster. | 左臂拿起桌上的塑料杯，并将其放在白色杯垫上。 |
| PnP Hard | 6 | Put Cup on Coaster | 4 | The left arm picks up the pink cup from the table and places it on the gray coaster. | 左臂拿起桌上的粉色杯子，并将其放在灰色杯垫上。 |
| PnP Hard | 7 | Stack Bowls/Cups | 1 | The robot reaches to grip the green bowl, moves it to the middle wooden bowl, and releases it to stack. It then reaches to grip the white bowl, moves it to the same location, and releases it onto the stack. | 机器人伸手夹住绿色碗，将其移到中间的木碗处，然后释放以进行堆叠。随后它伸手夹住白色碗，将其移到同一位置，并释放到碗堆上。 |
| PnP Hard | 7 | Stack Bowls/Cups | 2 | The robot reaches its left arm to grip the blue plate, moves it to the middle light green plate, and releases it to stack. It then reaches its right arm to grip the red plate, moves it over the middle stack of plates, and releases it to finish the task. | 机器人伸出左臂夹住蓝色盘子，将其移到中间的浅绿色盘子处，然后释放以进行堆叠。随后它伸出右臂夹住红色盘子，将其移到中间盘堆上方，并释放以完成任务。 |
| PnP Hard | 7 | Stack Bowls/Cups | 3 | The robot reaches its left arm to grip the paper bowl, moves it over the middle white bowl, and releases it to stack. It then reaches its left arm to grip the blue checkered bowl, moves it over the stack, and releases it to finish the task. | 机器人伸出左臂夹住纸碗，将其移到中间白色碗上方，然后释放以进行堆叠。随后它伸出左臂夹住蓝色格纹碗，将其移到碗堆上方，并释放以完成任务。 |
| PnP Hard | 7 | Stack Bowls/Cups | 4 | The robot reaches its left arm to grip the pink bowl, moves it over the middle beige bowl, and releases it to stack. It then reaches its left arm to grip the white bowl, moves it over the stack, and releases it onto the stack. | 机器人伸出左臂夹住粉色碗，将其移到中间米色碗上方，然后释放以进行堆叠。随后它伸出左臂夹住白色碗，将其移到碗堆上方，并释放到碗堆上。 |
| Contact Rich | 8 | Folding Shirts | 1 | Both arms grip the bottom of the light grey short sleeve and fold it toward the middle. They then pull the short sleeve across the table to the edge. Next, both arms grasp the top of the shirt and fold it down to the middle. Finally, the right arm grips the collar and folds it down to complete the task. | 双臂夹住浅灰色短袖衫底部，并向中间折叠。随后，双臂将短袖衫沿桌面拉到边缘。接着，双臂抓住衬衫顶部，并向下折到中间。最后，右臂夹住衣领并向下折叠，以完成任务。 |
| Contact Rich | 8 | Folding Shirts | 2 | Both arms fold the bottom of the green short sleeve to the middle. They then pull the shirt toward the edge of the table. Next, both arms fold the top of the shirt down to the middle. Finally, the right arm grasps the collar and folds it down to complete the task. | 双臂将绿色短袖衫底部折到中间。随后它们将衬衫拉向桌子边缘。接着，双臂将衬衫顶部向下折到中间。最后，右臂抓住衣领并向下折叠，以完成任务。 |
| Contact Rich | 8 | Folding Shirts | 3 | Both arms fold the bottom of the logo short sleeve to the middle. They then pull the shirt toward the edge of the table. Next, both arms fold the top of the shirt down to the middle. Finally, the right arm grasps the collar and folds it down to complete the task. | 双臂将带标志的短袖衫底部折到中间。随后它们将衬衫拉向桌子边缘。接着，双臂将衬衫顶部向下折到中间。最后，右臂抓住衣领并向下折叠，以完成任务。 |
| Contact Rich | 8 | Folding Shirts | 4 | Both arms fold the bottom of the gray short sleeve to the middle. They then pull the shirt toward the edge of the table. Next, both arms fold the top of the shirt down to the middle. Finally, the left arm grasps the collar and folds it down to finish. | 双臂将灰色短袖衫底部折到中间。随后它们将衬衫拉向桌子边缘。接着，双臂将衬衫顶部向下折到中间。最后，左臂抓住衣领并向下折叠以完成。 |
| Contact Rich | 9 | Folding Shorts | 1 | Both arms fold the bottom of the tan shorts toward the middle. Then, the right arm folds the shorts in half from right to left to complete the fold. | 双臂将棕黄色短裤底部向中间折叠。然后，右臂将短裤从右向左对折，完成折叠。 |
| Contact Rich | 9 | Folding Shorts | 2 | Both arms fold the bottom of the grey shorts toward the middle. Then, the right arm folds the shorts in half from right to left to complete the fold. | 双臂将灰色短裤底部向中间折叠。然后，右臂将短裤从右向左对折，完成折叠。 |
| Contact Rich | 9 | Folding Shorts | 3 | Both arms fold the bottom of the white shorts toward the middle. Then, the right arm folds the shorts in half from right to left to complete the task. | 双臂将白色短裤底部向中间折叠。然后，右臂将短裤从右向左对折，以完成任务。 |
| Contact Rich | 9 | Folding Shorts | 4 | Both arms fold the bottom of the green shorts toward the middle. Then, the right arm folds the shorts in half from right to left to complete the fold. | 双臂将绿色短裤底部向中间折叠。然后，右臂将短裤从右向左对折，完成折叠。 |
| Contact Rich | 10 | Stacking Clothes | 1 | Both arms pick up the black shirt and place it on the stack of clothes. | 双臂拿起黑色衬衫，并将其放在衣物堆上。 |
| Contact Rich | 10 | Stacking Clothes | 2 | Both arms pick up the white shirt and place it on the gray towel. | 双臂拿起白色衬衫，并将其放在灰色毛巾上。 |
| Contact Rich | 10 | Stacking Clothes | 3 | Both arms pick up the black hoodie and place it on the stack of clothes. | 双臂拿起黑色连帽衫，并将其放在衣物堆上。 |
| Contact Rich | 10 | Stacking Clothes | 4 | Both arms pick up the dark gray shirt and place it on the stack of clothes. | 双臂拿起深灰色衬衫，并将其放在衣物堆上。 |

**Caption:** Seen Tasks Evaluation Setup for AgiBot G1.

**Caption[CN]:** AgiBot G1 已见任务评估设置。


## Table 6. Unseen Tasks Evaluation Setup for AgiBot G1

| Task No. | Task | Config. | Exact English instruction | 中文指令 |
|---:|---|---:|---|---|
| 1 | Untie Shoelaces | 1 | The robot coordinates both arms to simultaneously grasp the two loops of the shoelace. It then moves both arms outward in synchronized, opposing directions until the shoelace is fully untied. | 机器人协调双臂，同时抓住鞋带的两个环。随后，它同步地将双臂沿相反方向向外移动，直到鞋带完全解开。 |
| 1 | Untie Shoelaces | 2 | The robot reaches its left arm to grasp the blue box and hold it steady. It then reaches its right arm toward the blue ribbon and moves it to untie the knot. | 机器人伸出左臂抓住蓝色盒子并使其保持稳定。随后它将右臂伸向蓝色丝带，并移动丝带以解开结。 |
| 1 | Untie Shoelaces | 3 | The robot coordinates both arms to simultaneously grasp the two loops of the knot of the box. It then moves both arms outward in synchronized, opposing directions until the knot of the box is fully untied. | 机器人协调双臂，同时抓住盒子结上的两个环。随后，它同步地将双臂沿相反方向向外移动，直到盒子上的结完全解开。 |
| 1 | Untie Shoelaces | 4 | The robot coordinates both arms to simultaneously grasp the two loops of the knot of the package. It then moves both arms outward in synchronized, opposing directions until the knot of the package is fully untied. | 机器人协调双臂，同时抓住包裹结上的两个环。随后，它同步地将双臂沿相反方向向外移动，直到包裹上的结完全解开。 |
| 2 | Remove /Put Hat | 1 | The robot reaches its right arm to gasp the crown and lifts it to remove it from the mannequin’s head. | 机器人伸出右臂抓住帽冠，并将其抬起，从人台头上取下。 |
| 2 | Remove /Put Hat | 2 | The robot reaches its left arm to grasp the hat and lifts it to remove it from the mannequin’s head. | 机器人伸出左臂抓住帽子，并将其抬起，从人台头上取下。 |
| 2 | Remove /Put Hat | 3 | The robot reaches its left arm to grasp the hat and lifts it to remove it from the mannequin’s head. | 机器人伸出左臂抓住帽子，并将其抬起，从人台头上取下。 |
| 2 | Remove /Put Hat | 4 | The robot reaches its left arm to grasp the hat and lifts it to remove it from the mannequin’s head. | 机器人伸出左臂抓住帽子，并将其抬起，从人台头上取下。 |
| 3 | Draw Circle | 1 | The robot reaches its left arm to pick up the red marker and the left arm moves the marker to draw a circle on the book. | 机器人伸出左臂拿起红色记号笔，左臂移动记号笔，在本子上画一个圆。 |
| 3 | Draw Circle | 2 | The robot reaches its right arm to pick up the marker and the right arm draws a circle on the whiteboard with the marker. | 机器人伸出右臂拿起记号笔，右臂用记号笔在白板上画一个圆。 |
| 3 | Draw Circle | 3 | The robot reaches its left arm to pick up the black marker and the left arm moves the marker to draw a circle on the paper | 机器人伸出左臂拿起黑色记号笔，左臂移动记号笔，在纸上画一个圆。 |
| 3 | Draw Circle | 4 | The robot reaches its right arm to pick up the marker and the right arm moves the marker to draw a llne on the whiteboard. | 机器人伸出右臂拿起记号笔，右臂移动记号笔，在白板上画一条线。 |
| 4 | Take out Straw | 1 | The left arm holds the cup on the table. Then the right arm pulls the straw out of the cup. | 左臂按住桌上的杯子，然后右臂将吸管从杯子中抽出。 |
| 4 | Take out Straw | 2 | The left arm holds the cup on the table. Then the right arm pulls the straw out of the cup. | 左臂按住桌上的杯子，然后右臂将吸管从杯子中抽出。 |
| 4 | Take out Straw | 3 | The left arm holds the cup on the table. Then the right arm pulls the straw out of the cup. | 左臂按住桌上的杯子，然后右臂将吸管从杯子中抽出。 |
| 4 | Take out Straw | 4 | The right arm holds the cup on the table.Then the left arm pulls the straw out of the cup. | 右臂按住桌上的杯子，然后左臂将吸管从杯子中抽出。 |
| 5 | Cube Stacking | 1 | The robot reaches its right arm to pick up the green cube, moves it over the red cube, and releases it to stack. It then reaches its right arm to pick up the yellow cube, moves it over the stack, and releases it onto the green cube to finish the task. | 机器人伸出右臂拿起绿色方块，将其移到红色方块上方，并释放以进行堆叠。随后它伸出右臂拿起黄色方块，将其移到方块堆上方，并释放到绿色方块上，以完成任务。 |
| 5 | Cube Stacking | 2 | The robot reaches its right arm to pick up the red cube, moves it over the colorful cube, and releases it to stack. It then reaches its right arm to pick up the green cube, moves it over the red cube, and releases it to finish the tower. | 机器人伸出右臂拿起红色方块，将其移到彩色方块上方，并释放以进行堆叠。随后它伸出右臂拿起绿色方块，将其移到红色方块上方，并释放以完成方块塔。 |
| 5 | Cube Stacking | 3 | The robot reaches its right arm to pick up the white cube, moves it over the green cube, and releases it to stack. It then reaches its left arm to pick up the blue cube, moves it over the stack, and releases it onto the white cube to finish the task. | 机器人伸出右臂拿起白色方块，将其移到绿色方块上方，并释放以进行堆叠。随后它伸出左臂拿起蓝色方块，将其移到方块堆上方，并释放到白色方块上，以完成任务。 |
| 5 | Cube Stacking | 4 | The robot reaches its right arm to pick up the red cube, moves it over the blue cube, and releases it to begin the stack. It then reaches its left arm to pick up the orange cube, moves it over the stack, and releases it onto the red cube to complete the three-tier structure. | 机器人伸出右臂拿起红色方块，将其移到蓝色方块上方，并释放以开始堆叠。随后它伸出左臂拿起橙色方块，将其移到方块堆上方，并释放到红色方块上，以完成三层结构。 |
| 6 | Painting | 1 | The left arm grabs the brush. Then left arm paints with the brush on the notebook | 左臂拿起画笔，然后用画笔在笔记本上绘画。 |
| 6 | Painting | 2 | The right arm grabs the brush. Then right arm paints with the brush on the paper | 右臂拿起画笔，然后用画笔在纸上绘画。 |
| 6 | Painting | 3 | The left arm grabs the brush. Then left arm paints with the brush on the notebook | 左臂拿起画笔，然后用画笔在笔记本上绘画。 |
| 6 | Painting | 4 | The right arm grabs the brush. Then right arm paints with the brush on the notebook | 右臂拿起画笔，然后用画笔在笔记本上绘画。 |
| 7 | Ironing | 1 | The robot reaches its left arm to grasp the iron and moves it across the shorts to iron it. | 机器人伸出左臂抓住熨斗，并在短裤上来回移动以熨平短裤。 |
| 7 | Ironing | 2 | The robot reaches its right arm to grasp the iron and moves it across the shirt to iron it. | 机器人伸出右臂抓住熨斗，并在衬衫上来回移动以熨平衬衫。 |
| 7 | Ironing | 3 | The robot reaches its left arm to grasp the iron and moves it across the shirt to iron it. | 机器人伸出左臂抓住熨斗，并在衬衫上来回移动以熨平衬衫。 |
| 7 | Ironing | 4 | The robot reaches its left arm to grasp the iron and moves it across the shirt to iron it. | 机器人伸出左臂抓住熨斗，并在衬衫上来回移动以熨平衬衫。 |
| 8 | Shake Hands | 1 | The right arm of the robot grasp the human hand to shake hands. It then initiates a rhythmic up-and-down motion to perform the handshake. | 机器人右臂抓住人手进行握手，然后开始有节奏的上下运动以完成握手。 |
| 8 | Shake Hands | 2 | The left arm shakes the hand of the human up and down | 左臂上下摇动人的手。 |
| 8 | Shake Hands | 3 | The right arm shakes the hand of the human up and down | 右臂上下摇动人的手。 |
| 8 | Shake Hands | 4 | The left arm of the robot grasp the human hand to shake hands. It then initiates a rhythmic up-and-down motion to perform the handshake. | 机器人左臂抓住人手进行握手，然后开始有节奏的上下运动以完成握手。 |
| 9 | Folding (Map) | 1 | The left arm grabs the left side of the map. The right arm folds the right side of the map. The left arm folds the left side of the map. | 左臂抓住地图左侧。右臂折叠地图右侧。左臂折叠地图左侧。 |
| 9 | Folding (Map) | 2 | The left arm grabs the left side of the map. The right arm folds the right side of the map. The left arm folds the left side of the map. | 左臂抓住地图左侧。右臂折叠地图右侧。左臂折叠地图左侧。 |
| 9 | Folding (Map) | 3 | The right arm grabs the right side of the map. The left arm folds the left side of the map. The right arm folds the right side of the map. | 右臂抓住地图右侧。左臂折叠地图左侧。右臂折叠地图右侧。 |
| 9 | Folding (Map) | 4 | The right arm grabs the right side of the map.The left arm folds the left side of the map. The right arm folds the right side of the map. | 右臂抓住地图右侧。左臂折叠地图左侧。右臂折叠地图右侧。 |
| 10 | Pulling Cart | 1 | The robot reaches its right arm to grasp the cart and pulls it. | 机器人伸出右臂抓住推车并拉动它。 |
| 10 | Pulling Cart | 2 | The robot reaches its left arm to grasp the cart and pulls it. | 机器人伸出左臂抓住推车并拉动它。 |
| 10 | Pulling Cart | 3 | The robot reaches its right arm to grasp the cart and pulls it. | 机器人伸出右臂抓住推车并拉动它。 |
| 10 | Pulling Cart | 4 | The robot reaches its left arm to grasp the cart and pulls it forward. | 机器人伸出左臂抓住推车，并将其向前拉。 |

**Caption:** Unseen Tasks Evaluation Setup for AgiBot G1.

**Caption[CN]:** AgiBot G1 未见任务评估设置。


# Appendix G. DROID Evaluation Details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We provide the evaluation setup for seen and unseen tasks in Tables 7a and 7b for DROID. We conduct 2 rollouts per task by varying the location of the objects. Image cells from the source setup are omitted below, while every exact task prompt is preserved and translated.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Tables 7a 和 7b 给出 DROID 已见任务与未见任务的评估设置。我们通过改变物体位置，对每个任务执行 2 次 rollout。下文省略源设置中的图像单元格，但保留并翻译每一条精确任务提示。

## Table 7a. Seen tasks on DROID

| No. | Exact English instruction | 中文指令 |
|---:|---|---|
| 1 | Move the cup forward then put the marker inside the cup | 把杯子向前移动，然后把记号笔放进杯子。 |
| 2 | Move the bowl on the left to the right side of the table. | 把左边的碗移到桌子右侧。 |
| 3 | Put the marker in the blue box | 把记号笔放进蓝色盒子。 |
| 4 | Pick up the pencil and put it on the bowl | 拿起铅笔，并把它放在碗上。 |
| 5 | Remove the pair of gloves from the open drawer and put it on the table | 从打开的抽屉中取出那副手套，并将其放在桌上。 |
| 6 | Pick the marker up from the table and put it in the bowl | 从桌上拿起记号笔，并把它放进碗里。 |
| 7 | Put the marker on table | 把记号笔放在桌上。 |
| 8 | Place the bowl next to the marker | 把碗放在记号笔旁边。 |
| 9 | Pick up the apple and put it in the basket | 拿起苹果，并把它放进篮子。 |
| 10 | Remove a lemon from the bowl | 从碗中取出一个柠檬。 |
| 11 | Put the towel on the white cup | 把毛巾放在白色杯子上。 |
| 12 | Move the grapes to the left | 把葡萄向左移动。 |
| 13 | Put the towel in the pan | 把毛巾放进平底锅。 |
| 14 | Move the green grapes backwards | 把绿色葡萄向后移动。 |
| 15 | Put the hat on the table | 把帽子放在桌上。 |
| 16 | Put the bread inside the toaster | 把面包放进烤面包机。 |
| 17 | Put the pair of scissors into the drawer | 把剪刀放进抽屉。 |
| 18 | Push the lever on the bread toaster downwards | 向下按烤面包机上的拨杆。 |
| 19 | Put the towel in the basket | 把毛巾放进篮子。 |
| 20 | Pick up the cup from the bowl and put it in the other cups | 从碗中拿起杯子，并把它放到其他杯子里。 |

**Caption:** (a) Seen tasks on DROID.

**Caption[CN]:** (a) DROID 上的已见任务。

## Table 7b. Tasks with unseen verbs on DROID

| No. | Exact English instruction | 中文指令 |
|---:|---|---|
| 1 | Orient the mug so the handle is to the right | 调整马克杯方向，使杯把朝右。 |
| 2 | Hook the hat onto the tripod | 把帽子挂在三脚架上。 |
| 3 | Fan the burger | 给汉堡煽风。 |
| 4 | Pinch the binder clip to release the papers | 捏开长尾夹，释放纸张。 |
| 5 | Slice the bread with the knife | 用刀切面包。 |
| 6 | Withdraw the bread from the toaster and place on the plate | 从烤面包机中取出面包，并把它放在盘子上。 |
| 7 | Type ’hi’ on the keyboard | 在键盘上输入 ’hi’。 |
| 8 | Cinch the drawstring of the bag | 拉紧袋子的抽绳。 |
| 9 | Extricate the straw from the cup | 将吸管从杯子中抽出。 |
| 10 | Dispense the mustard onto the bread | 把黄芥末挤到面包上。 |
| 11 | Reveal the object under the cup | 露出杯子下方的物体。 |
| 12 | Bake the croissant in the oven | 把可颂面包放进烤箱烘烤。 |
| 13 | Match the objects to their corresponding bowl | 将物体匹配到各自对应的碗中。 |
| 14 | Fry the vegetables in the pan with the spatula | 用锅铲在平底锅里炒蔬菜。 |
| 15 | Maneuver the blocks through the matching hole | 操作方块穿过与其匹配的孔。 |
| 16 | Depress the lever on the toaster | 向下压烤面包机的拨杆。 |
| 17 | Affix the magnet to the tray | 将磁铁固定在托盘上。 |
| 18 | Elevate the yellow block to the highest platform | 将黄色方块抬到最高平台。 |
| 19 | Combine the nuts and batteries | 将坚果与电池放在一起。 |
| 20 | Weave the wire through the holes of the box | 将电线穿过盒子的孔。 |

**Caption:** (b) Tasks with unseen verbs on DROID.

**Caption[CN]:** (b) DROID 上包含未见动词的任务。

# Appendix H. Failure Case Analysis

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In Figure 16, we illustrate videos generated by DreamZero and execution rollouts for both AgiBot and DROID. Overall, robot execution follows the visual plan generated by the video modality. In the AgiBot video generated by DreamZero, the robot picks up the marker with its left arm and passes the marker to its right arm. Consistent with the generated video, in the execution rollout the robot picks up the top part of the marker, but instead of drawing a line on the whiteboard, the left arm passes the marker to the right arm. In the DROID video generated by DreamZero, the robot picks up the bread instead of opening the oven first. Aligned with the generated video, in the execution rollout the robot picks up the bread first instead of opening the oven, causing the rollout to become stuck after the robot reaches the oven while holding the bread. This implies that improving WAM language-following and visual-planning capability could potentially yield better action execution.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Figure 16 展示了 DreamZero 生成的视频，以及 AgiBot 和 DROID 上的执行 rollout。总体上，机器人执行会遵循视频模态生成的视觉计划。在 DreamZero 生成的 AgiBot 视频中，机器人用左臂拿起记号笔，然后将它交给右臂。与生成视频一致，在实际执行 rollout 中，机器人拿起记号笔上部，但左臂没有在白板上画线，而是将记号笔交给右臂。在 DreamZero 生成的 DROID 视频中，机器人没有先打开烤箱，而是先拿起面包。与生成视频对齐，实际执行 rollout 中，机器人也没有先打开烤箱，而是先拿起面包，导致机器人手持面包伸向烤箱后，rollout 陷入停滞。这意味着，提高 WAM 的语言遵循和视觉规划能力，可能带来更好的动作执行。

## Figure 16. Illustration of generated and executed pair / 生成与执行配对示意

![Figure 16](assets/page_029_fig_figure_16.png)

**Caption:** Illustration of generated and executed pair. We illustrate the generated video and action-execution pair. These two examples show scenarios where video prediction failed and the robot followed the failed plan. DreamZero failed to generate video of the AgiBot G1 robot drawing on the whiteboard and failed to generate video of the Franka robot opening the oven first.

**Caption[CN]:** 生成与执行配对示意。我们展示生成视频与动作执行的配对。这两个示例展示了视频预测失败且机器人遵循失败计划的情形。DreamZero 未能生成 AgiBot G1 机器人在白板上画线的视频，也未能生成 Franka 机器人首先打开烤箱的视频。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The exact visible prompts are “Pick up the marker and draw a line on the whiteboard.” and “Bake the croissant in the oven.” The rows are labeled “Generated” and “Execution.”

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 图中可见的精确提示为“拿起记号笔，在白板上画一条线”和“把可颂面包放进烤箱烘烤”。各行标注为“Generated（生成）”和“Execution（执行）”。

# References

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Bilingual reference policy.** All 92 bibliographic entries are preserved below in their original English, intact and searchable, including the source's terminal in-text page locators. Bibliographic entries are not translated because author names, publication titles, venues, URLs, identifiers, and citation metadata are canonical records rather than source argumentation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **参考文献双语策略。** 下文完整保留全部 92 条英文参考文献，使其可搜索，并保留源文条目末尾的文内页码定位符。这些条目不逐条翻译，因为作者姓名、出版物标题、会议/期刊、URL、标识符与引文元数据是规范书目记录，而非论文论证性正文。


[1] Michael S Albergo, Nicholas M Boffi, and Eric Vanden-Eijnden. Stochastic interpolants: A unifying
framework for flows and diffusions. arXiv preprint arXiv:2303.08797, 2023. 7
[2] Arslan Ali, Junjie Bai, Maciej Bala, Yogesh Balaji, Aaron Blakeman, Tiffany Cai, Jiaxin Cao, Tianshi Cao,
Elizabeth Cha, Yu-Wei Chao, et al. World simulation with video foundation models for physical ai. arXiv
preprint arXiv:2511.00062, 2025. 7
[3] Mahmoud Assran, Quentin Duval, Ishan Misra, Piotr Bojanowski, Pascal Vincent, Michael Rabbat, Yann
LeCun, and Nicolas Ballas. Self-supervised learning from images with a joint-embedding predictive
architecture. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 2023.
[4] Mido Assran, Adrien Bardes, David Fan, Quentin Garrido, Russell Howes, Mojtaba Komeili, Matthew
Muckley, Ammar Rizvi, Claire Roberts, Koustuv Sinha, et al. V-JEPA 2: Self-supervised video models
enable understanding, prediction and planning. arXiv preprint arXiv:2506.09985, 2025. 5, 20
[5] Philip J. Ball, Jakob Bauer, Frank Belletti, Bethanie Brownfield, Ariel Ephrat, Shlomi Fruchter, Agrim
Gupta, Kristian Holsheimer, Aleksander Holynski, Jiri Hron, Christos Kaplanis, Marjorie Limont, Matt
McGill, Yanko Oliveira, Jack Parker-Holder, Frank Perbet, Guy Scully, Jeremy Shar, Stephen Spencer,
Omer Tov, Ruben Villegas, Emma Wang, Jessica Yung, Cip Baetu, Jordi Berbel, David Bridson, Jake Bruce,
Gavin Buttimore, Sarah Chakera, Bilva Chandra, Paul Collins, Alex Cullum, Bogdan Damoc, Vibha Dasagi,
Maxime Gazeau, Charles Gbadamosi, Woohyun Han, Ed Hirst, Ashyana Kachra, Lucie Kerley, Kristian
Kjems, Eva Knoepfel, Vika Koriakin, Jessica Lo, Cong Lu, Zeb Mehring, Alex Moufarek, Henna Nandwani,
Valeria Oliveira, Fabio Pardo, Jane Park, Andrew Pierson, Ben Poole, Helen Ran, Tim Salimans, Manuel
Sanchez, Igor Saprykin, Amy Shen, Sailesh Sidhwani, Duncan Smith, Joe Stanton, Hamish Tomlinson,
Dimple Vijaykumar, Luyu Wang, Piers Wingfield, Nat Wong, Keyang Xu, Christopher Yew, Nick Young,
Vadim Zubov, Douglas Eck, Dumitru Erhan, Koray Kavukcuoglu, Demis Hassabis, Zoubin Gharamani,
Raia Hadsell, Aäron van den Oord, Inbar Mosseri, Adrian Bolton, Satinder Singh, and Tim Rocktäschel.
Genie 3: A new frontier for world models. 2025. URL https://deepmind.google/discover/blog/
genie-3-a-new-frontier-for-world-models/. 19
[6] Adrien Bardes, Quentin Garrido, Jean Ponce, Michael Rabbat, Yann LeCun, Mahmoud Assran, and Nicolas
Ballas. V-JEPA: Video joint embedding predictive architecture. arXiv preprint arXiv:2402.05065, 2024. 20
[7] Jose Barreiros, Andrew Beaulieu, Aditya Bhat, Rick Cory, Eric Cousineau, Hongkai Dai, Ching-Hsin Fang,
Kunimatsu Hashimoto, Muhammad Zubair Irshad, Masha Itkina, et al. A careful examination of large
behavior models for multitask dexterous manipulation. arXiv preprint arXiv:2507.05331, 2025. 13
[8] Homanga Bharadhwaj, Debidatta Dwibedi, Abhinav Gupta, Shubham Tulsiani, Carl Doersch, Ted Xiao,
Dhruv Shah, Fei Xia, Dorsa Sadigh, and Sean Kirmani. Gen2act: Human video generation in novel
scenarios enables generalizable robot manipulation. arXiv preprint arXiv:2409.16283, 2024. 5
[9] Johan Bjorck, Fernando Castañeda, Nikita Cherniadev, Xingye Da, Runyu Ding, Linxi Fan, Yu Fang, Dieter
Fox, Fengyuan Hu, Spencer Huang, et al. Gr00t n1: An open foundation model for generalist humanoid
robots. arXiv preprint arXiv:2503.14734, 2025. 2, 4, 10, 18
[10] Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, Lachy
Groom, Karol Hausman, Brian Ichter, et al. 𝜋0: A vision-language-action flow model for general robot
control. arXiv preprint arXiv:2410.24164, 2024. 4
[11] Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, Lachy
Groom, Karol Hausman, Brian Ichter, et al. 𝜋0: A vision-language-action flow model for general robot
control. URL https://arxiv. org/abs/2410.24164, 2024. 2
[12] Rishi Bommasani, Drew A Hudson, Ehsan Adeli, Russ Altman, Simran Arora, Sydney von Arx, Michael S
Bernstein, Jeannette Bohg, Antoine Bosselut, Emma Brunskill, et al. On the opportunities and risks of
foundation models. arXiv preprint arXiv:2108.07258, 2021. 4
[13] Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Joseph Dabis, Chelsea Finn, Keerthana
Gopalakrishnan, Karol Hausman, Alex Herzog, Jasmine Hsu, Julian Ibarz, Brian Ichter, Alex Irpan, Tomas
Jackson, Sally Jesmonth, Nikhil Joshi, Ryan Julian, Dmitry Kalashnikov, Yuheng Kuang, Isabel Leal,
Kuang-Huei Lee, Sergey Levine, Yao Lu, Utsav Malla, Deeksha Manjunath, Igor Mordatch, Ofir Nachum,
Carolina Parada, Jodilyn Peralta, Emily Perez, Karl Pertsch, Jornell Quiambao, Kanishka Rao, Michael
Ryoo, Grecia Salazar, Pannag Sanketi, Kevin Sayed, Jaspiar Singh, Sumedh Sontakke, Austin Stone,
Clayton Tan, Huong Tran, Vincent Vanhoucke, Steve Vega, Quan Vuong, Fei Xia, Ted Xiao, Peng Xu,
Sichun Xu, Tianhe Yu, and Brianna Zitkovich. Rt-1: Robotics transformer for real-world control at scale.
In arXiv preprint arXiv:2212.06817, 2022. 4
[14] Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski,
Tianli Ding, Danny Driess, Avinava Dubey, Chelsea Finn, Pete Florence, Chuyuan Fu, Montse Gonzalez
Arenas, Keerthana Gopalakrishnan, Kehang Han, Karol Hausman, Alex Herzog, Jasmine Hsu, Brian Ichter,
Alex Irpan, Nikhil Joshi, Ryan Julian, Dmitry Kalashnikov, Yuheng Kuang, Isabel Leal, Lisa Lee, Tsang-
Wei Edward Lee, Sergey Levine, Yao Lu, Henryk Michalewski, Igor Mordatch, Karl Pertsch, Kanishka Rao,
Krista Reymann, Michael Ryoo, Grecia Salazar, Pannag Sanketi, Pierre Sermanet, Jaspiar Singh, Anikait
Singh, Radu Soricut, Huong Tran, Vincent Vanhoucke, Quan Vuong, Ayzaan Wahid, Stefan Welker, Paul
Wohlhart, Jialin Wu, Fei Xia, Ted Xiao, Peng Xu, Sichun Xu, Tianhe Yu, and Brianna Zitkovich. Rt-2: Vision-
language-action models transfer web knowledge to robotic control. In arXiv preprint arXiv:2307.15818,
2023. 2, 4
[15] Anthony Brohan, Yevgen Chebotar, Chelsea Finn, Karol Hausman, Alexander Herzog, Daniel Ho, Julian
Ibarz, Alex Irpan, Eric Jang, Ryan Julian, et al. Do as i can, not as i say: Grounding language in robotic
affordances. In Conference on robot learning, pages 287–318. PMLR, 2023. 4
[16] Qingwen Bu, Yanting Yang, Jisong Cai, Shenyuan Gao, Guanghui Ren, Maoqing Yao, Ping Luo, and
Hongyang Li.
Univla: Learning to act anywhere with task-centric latent actions.
arXiv preprint
arXiv:2505.06111, 2025. 4
[17] Chi-Lam Cheang, Guangzeng Chen, Ya Jing, Tao Kong, Hang Li, Yifeng Li, Yuxiao Liu, Hongtao Wu,
Jiafeng Xu, Yichu Yang, et al. Gr-2: A generative video-language-action model with web-scale knowledge
for robot manipulation. arXiv preprint arXiv:2410.06158, 2024. 5
[18] Boyuan Chen, Zhuo Xu, Sean Kirmani, Brain Ichter, Dorsa Sadigh, Leonidas Guibas, and Fei Xia. Spa-
tialvlm: Endowing vision-language models with spatial reasoning capabilities. In Proceedings of the
IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 14455–14465, 2024. 2
[19] Boyuan Chen, Tianyuan Zhang, Haoran Geng, Kiwhan Song, Caiyi Zhang, Peihao Li, William T Freeman,
Jitendra Malik, Pieter Abbeel, Russ Tedrake, et al. Large video planner enables generalizable robot control.
arXiv preprint arXiv:2512.15840, 2025. 5
[20] Delong Chen, Tejaswi Kasarla, Yejin Bang, Mustafa Shukor, Willy Chung, Jade Yu, Allen Bolourchi,
Theo Moutakanni, and Pascale Fung. Action100m: A large-scale video action dataset. arXiv preprint
arXiv:2601.10592, 2026. 18
[21] Chaorui Deng, Deyao Zhu, Kunchang Li, Chenhui Gou, Feng Li, Zeyu Wang, Shu Zhong, Weihao Yu,
Xiaonan Nie, Ziang Song, et al. Emerging properties in unified multimodal pretraining. arXiv preprint
arXiv:2505.14683, 2025. 19
[22] Kamil Dreczkowski, Pietro Vitiello, Vitalis Vosylius, and Edward Johns. Learning a thousand tasks in a
day. Science Robotics, 10(108):eadv7594, 2025. 4
[23] Danny Driess, Fei Xia, Mehdi SM Sajjadi, Corey Lynch, Aakanksha Chowdhery, Brian Ichter, Ayzaan
Wahid, Jonathan Tompson, Quan Vuong, Tianhe Yu, et al. Palm-e: An embodied multimodal language
model. arXiv preprint arXiv:2303.03378, 2023. 4
[24] Yilun Du, Sherry Yang, Bo Dai, Hanjun Dai, Ofir Nachum, Josh Tenenbaum, Dale Schuurmans, and Pieter
Abbeel. Learning universal policies via text-guided video generation. Advances in neural information
processing systems, 36:9156–9172, 2023. 5
[25] Yilun Du, Sherry Yang, Pete Florence, Fei Xia, Ayzaan Wahid, brian ichter, Pierre Sermanet, Tianhe Yu,
Pieter Abbeel, Joshua B. Tenenbaum, Leslie Pack Kaelbling, Andy Zeng, and Jonathan Tompson. Video
language planning. In The Twelfth International Conference on Learning Representations, 2024. URL
https://openreview.net/forum?id=9pKtcJcMP3. 5
[26] Zhiyuan Feng, Zhaolu Kang, Qijie Wang, Zhiying Du, Jiongrui Yan, Shubin Shi, Chengbo Yuan, Huizhi
Liang, Yu Deng, Qixiu Li, et al. Seeing across views: Benchmarking spatial reasoning of vision-language
models in robotic scenes. arXiv preprint arXiv:2510.19400, 2025. 2
[27] Jensen Gao, Suneel Belkhale, Sudeep Dasari, Ashwin Balakrishna, Dhruv Shah, and Dorsa Sadigh. A
taxonomy for evaluating generalist robot policies. arXiv preprint arXiv:2503.01238, 2025. 4
[28] Kaifeng Gao, Jiaxin Shi, Hanwang Zhang, Chunping Wang, Jun Xiao, and Long Chen. Ca2-vdm: Ef-
ficient autoregressive video diffusion model with causal generation and cache sharing. arXiv preprint
arXiv:2411.16375, 2024. 7
[29] Gemini Robotics Team.
Gemini robotics:
Bringing ai into the physical world.
arXiv preprint
arXiv:2503.20020, 2025. 2, 4, 5
[30] Kristen Grauman, Andrew Westbury, Eugene Byrne, Zachary Chavis, Antonino Furnari, Rohit Girdhar,
Jackson Hamburger, Hao Jiang, Miao Liu, Xingyu Liu, et al. Ego4d: Around the world in 3,000 hours of
egocentric video. In Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition,
2022. 18
[31] Pranav Guruprasad, Yangyue Wang, Sudipta Chowdhury, Harshvardhan Sikka, and Paul Pu Liang. Bench-
marking vision, language, & action models in procedurally generated, open ended action environments.
arXiv preprint arXiv:2505.05540, 2025. 2
[32] Danijar Hafner, Timothy Lillicrap, Jimmy Ba, and Mohammad Norouzi. Dream to control: Learning
behaviors by latent imagination. arXiv preprint arXiv:1912.01603, 2019. 5, 20
[33] Danijar Hafner, Timothy Lillicrap, Mohammad Norouzi, and Jimmy Ba. Mastering atari with discrete
world models. arXiv preprint arXiv:2010.02193, 2020. 5, 20
[34] Danijar Hafner, Jurgis Pasukonis, Jimmy Ba, and Timothy Lillicrap. Mastering diverse domains through
world models. arXiv preprint arXiv:2301.04104, 2023. 5, 20
[35] Danijar Hafner, Wilson Yan, and Timothy Lillicrap. Training agents inside of scalable world models, 2025.
URL https://arxiv.org/abs/2509.24527. 20
[36] Jonathan Ho and Tim Salimans. Classifier-free diffusion guidance. arXiv preprint arXiv:2207.12598,
2022. 8
[37] Ryan Hoque, Peide Huang, David J Yoon, Mouli Sivapurapu, and Jian Zhang. Egodex: Learning dexterous
manipulation from large-scale egocentric video. arXiv preprint arXiv:2505.11709, 2025. 18
[38] Edward J Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, Weizhu
Chen, et al. Lora: Low-rank adaptation of large language models. ICLR, 1(2):3, 2022. 11
[39] Yucheng Hu, Yanjiang Guo, Pengchao Wang, Xiaoyu Chen, Yen-Jen Wang, Jianke Zhang, Koushil Sreenath,
Chaochao Lu, and Jianyu Chen. Video prediction policy: A generalist robot policy with predictive visual
representations. arXiv preprint arXiv:2412.14803, 2024. 5
[40] Wenlong Huang, Fei Xia, Ted Xiao, Harris Chan, Jacky Liang, Pete Florence, Andy Zeng, Jonathan
Tompson, Igor Mordatch, Yevgen Chebotar, et al. Inner monologue: Embodied reasoning through
planning with language models. In 6th Annual Conference on Robot Learning. 4
[41] Wenlong Huang, Chen Wang, Ruohan Zhang, Yunzhu Li, Jiajun Wu, and Li Fei-Fei. Voxposer: Composable
3d value maps for robotic manipulation with language models. arXiv preprint arXiv:2307.05973, 2023. 4
[42] Wenlong Huang, Yu-Wei Chao, Arsalan Mousavian, Ming-Yu Liu, Dieter Fox, Kaichun Mo, and Li Fei-
Fei.
Pointworld: Scaling 3d world models for in-the-wild robotic manipulation.
arXiv preprint
arXiv:2601.03782, 2025. 20
[43] Xun Huang, Zhengqi Li, Guande He, Mingyuan Zhou, and Eli Shechtman. Self forcing: Bridging the
train-test gap in autoregressive video diffusion. arXiv preprint arXiv:2506.08009, 2025. 8
[44] Team HunyuanWorld. Hy-world 1.5: A systematic framework for interactive world modeling with
real-time latency and geometric consistency. arXiv preprint, 2025. 19
[45] Arhan Jain, Mingtong Zhang, Kanav Arora, William Chen, Marcel Torne, Muhammad Zubair Irshad,
Sergey Zakharov, Yue Wang, Sergey Levine, Chelsea Finn, et al. Polaris: Scalable real-to-sim evaluations
for generalist robot policies. arXiv preprint arXiv:2512.16881, 2025. 11
[46] Joel Jang, Seonghyeon Ye, Zongyu Lin, Jiannan Xiang, Johan Bjorck, Yu Fang, Fengyuan Hu, Spencer
Huang, Kaushil Kundalia, Yen-Chen Lin, Loïc Magne, Ajay Mandlekar, Avnish Narayan, You Liang Tan,
Guanzhi Wang, Jing Wang, Qi Wang, Yinzhen Xu, Xiaohui Zeng, Kaiyuan Zheng, Ruijie Zheng, Ming-Yu
Liu, Luke Zettlemoyer, Dieter Fox, Jan Kautz, Scott Reed, Yuke Zhu, and Linxi Fan. Dreamgen: Unlocking
generalization in robot learning through video world models. In 9th Annual Conference on Robot Learning,
2025. URL https://openreview.net/forum?id=3CnxNqmklv. 5
[47] Yang Jin, Zhicheng Sun, Ningyuan Li, Kun Xu, Hao Jiang, Nan Zhuang, Quzhe Huang, Yang Song, Yadong
Mu, and Zhouchen Lin. Pyramidal flow matching for efficient video generative modeling. arXiv preprint
arXiv:2410.05954, 2024. 7
[48] Leslie Pack Kaelbling and Tomás Lozano-Pérez. 1 rationally engineering rational robots. 4
[49] Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B Brown, Benjamin Chess, Rewon Child, Scott Gray,
Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. arXiv preprint
arXiv:2001.08361, 2020. 18
[50] Simar Kareer, Karl Pertsch, James Darpinian, Judy Hoffman, Danfei Xu, Sergey Levine, Chelsea Finn,
and Suraj Nair. Emergence of human to robot transfer in vision-language-action models. arXiv preprint
arXiv:2512.22414, 2025. 16
[51] Alexander Khazatsky, Karl Pertsch, Suraj Nair, Ashwin Balakrishna, Sudeep Dasari, Siddharth Karamcheti,
Soroush Nasiriany, Mohan Kumar Srirama, Lawrence Yunliang Chen, Kirsty Ellis, et al. Droid: A large-scale
in-the-wild robot manipulation dataset. arXiv preprint arXiv:2403.12945, 2024. 10, 11
[52] Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael
Rafailov, Ethan Foster, Grace Lam, Pannag Sanketi, Quan Vuong, Thomas Kollar, Benjamin Burchfiel,
Russ Tedrake, Dorsa Sadigh, Sergey Levine, Percy Liang, and Chelsea Finn. Openvla: An open-source
vision-language-action model. arXiv preprint arXiv:2406.09246, 2024. 4
[53] Moo Jin Kim, Karl Pertsch, Siddharth Karamcheti, Ted Xiao, Ashwin Balakrishna, Suraj Nair, Rafael
Rafailov, Ethan Foster, Grace Lam, Pannag Sanketi, et al. Openvla: An open-source vision-language-action
model. arXiv preprint arXiv:2406.09246, 2024. 2
[54] Moo Jin Kim, Yihuai Gao, Tsung-Yi Lin, Yen-Chen Lin, Yunhao Ge, Grace Lam, Percy Liang, Shuran Song,
Ming-Yu Liu, Chelsea Finn, et al. Cosmos policy: Fine-tuning video models for visuomotor control and
planning. arXiv preprint arXiv:2601.16163, 2026. 2, 5, 7, 19
[55] Po-Chen Ko, Jiayuan Mao, Yilun Du, Shao-Hua Sun, and Joshua B. Tenenbaum. Learning to act from
actionless videos through dense correspondences. In The Twelfth International Conference on Learning
Representations, 2024. URL https://openreview.net/forum?id=Mhb5fpA1T0. 5
[56] Nishanth Kumar, William Shen, Fabio Ramos, Dieter Fox, Tomás Lozano-Pérez, Leslie Pack Kaelbling,
and Caelan Reed Garrett. Open-world task and motion planning via vision-language model generated
constraints. IEEE Robotics and Automation Letters, pages 1–8, 2026. doi: 10.1109/LRA.2026.3656799. 4
[57] Yann LeCun. A path towards autonomous machine intelligence. Open Review, 2022. 20
[58] Jason Lee, Jiafei Duan, Haoquan Fang, Yuquan Deng, Shuo Liu, Boyang Li, Bohan Fang, Jieyu Zhang,
Yi Ru Wang, Sangho Lee, et al. Molmoact: Action reasoning models that can reason in space. arXiv
preprint arXiv:2508.07917, 2025. 4
[59] Lin Li, Qihang Zhang, Yiming Luo, Shuai Yang, Ruilin Wang, Fei Han, Mingrui Yu, Zelin Gao, Nan
Xue, Xing Zhu, Yujun Shen, and Yinghao Xu. Causal world modeling for robot control. arXiv preprint
arXiv:2601.21998, 2026. 7
[60] Shuang Li, Yihuai Gao, Dorsa Sadigh, and Shuran Song. Unified video action model. arXiv preprint
arXiv:2503.00200, 2025. 5, 7
[61] Yi Li, Yuquan Deng, Jesse Zhang, Joel Jang, Marius Memmel, Raymond Yu, Caelan Reed Garrett, Fabio
Ramos, Dieter Fox, Anqi Li, et al. Hamster: Hierarchical action models for open-world robot manipulation.
arXiv preprint arXiv:2502.05485, 2025. 4
[62] Junbang Liang, Ruoshi Liu, Ege Ozguroglu, Sruthi Sudhakar, Achal Dave, Pavel Tokmakov, Shuran Song,
and Carl Vondrick. Dreamitate: Real-world visuomotor policy learning via video generation. In 8th
Annual Conference on Robot Learning, 2024. URL https://openreview.net/forum?id=InT87E5sr4. 5
[63] Junbang Liang, Pavel Tokmakov, Ruoshi Liu, Sruthi Sudhakar, Paarth Shah, Rares Ambrus, and Carl
Vondrick. Video generators are robot policies. arXiv preprint arXiv:2508.00795, 2025. 2, 5
[64] Yue Liao, Pengfei Zhou, Siyuan Huang, Donglin Yang, Shengcong Chen, Yuxin Jiang, Yue Hu, Jingbin Cai,
Si Liu, Jianlan Luo, et al. Genie envisioner: A unified world foundation platform for robotic manipulation.
arXiv preprint arXiv:2508.05635, 2025. 3, 5, 7
[65] Yaron Lipman, Ricky TQ Chen, Heli Ben-Hamu, Maximilian Nickel, and Matt Le. Flow matching for
generative modeling. arXiv preprint arXiv:2210.02747, 2022. 7
[66] Feng Liu, Shiwei Zhang, Xiaofeng Wang, Yujie Wei, Haonan Qiu, Yuzhong Zhao, Yingya Zhang, Qixiang
Ye, and Fang Wan. Timestep embedding tells: It’s time to cache for video diffusion model. arXiv preprint
arXiv:2411.19108, 2024. 23
[67] Jiacheng Liu, Chang Zou, Yuanhuiyi Lyu, Junjie Chen, and Linfeng Zhang. From reusing to forecasting:
Accelerating diffusion models with taylorseers. arXiv preprint arXiv:2503.06923, 2025. 23
[68] Xingchao Liu, Chengyue Gong, and Qiang Liu. Flow straight and fast: Learning to generate and transfer
data with rectified flow. arXiv preprint arXiv:2209.03003, 2022. 7
[69] Calvin Luo, Zilai Zeng, Yilun Du, and Chen Sun. Solving new tasks by adapting internet video knowledge.
In The Thirteenth International Conference on Learning Representations, 2025. 5
[70] NVIDIA Corporation.
Nvidia model-optimizer,
2024.
URL https://github.com/NVIDIA/
Model-Optimizer. 23
[71] Jonas Pai, Liam Achenbach, Victoriano Montesinos, Benedek Forrai, Oier Mees, and Elvis Nava. mimic-
video: Video-action models for generalizable robot control beyond vlas. arXiv preprint arXiv:2512.15692,
2025. 2, 3, 5, 7
[72] Physical Intelligence. 𝜋0.5: a vision-language-action model with open-world generalization. arXiv preprint
arXiv:2504.16054, 2025. 4, 5, 10
[73] Lucy Xiaoyang Shi, Brian Ichter, Michael Equi, Liyiming Ke, Karl Pertsch, Quan Vuong, James Tanner,
Anna Walling, Haohuan Wang, Niccolo Fusai, et al. Hi robot: Open-ended instruction following with
hierarchical vision-language-action models. arXiv preprint arXiv:2502.19417, 2025. 19
[74] Ishika Singh, Valts Blukis, Arsalan Mousavian, Ankit Goyal, Danfei Xu, Jonathan Tremblay, Dieter Fox,
Jesse Thomason, and Animesh Garg. Progprompt: Generating situated robot task plans using large
language models. In 2023 IEEE International Conference on Robotics and Automation (ICRA), 2023. 4
[75] Generalist AI Team. Gen-0: Embodied foundation models that scale with physical interaction. Generalist
AI Blog, 2025. https://generalistai.com/blog/preview-uqlxvb-bb.html. 16
[76] Team Wan. Wan: Open and advanced large-scale video generative models. 2025. 2, 7, 11
[77] Hansi Teng, Hongyu Jia, Lei Sun, Lingzhi Li, Maolin Li, Mingqiu Tang, Shuai Han, Tianning Zhang,
WQ Zhang, Weifeng Luo, et al.
Magi-1: Autoregressive video generation at scale.
arXiv preprint
arXiv:2505.13211, 2025. 7, 8
[78] Homer Walke, Kevin Black, Abraham Lee, Moo Jin Kim, Max Du, Chongyi Zheng, Tony Zhao, Philippe
Hansen-Estruch, Quan Vuong, Andre He, Vivek Myers, Kuan Fang, Chelsea Finn, and Sergey Levine.
Bridgedata v2: A dataset for robot learning at scale. In Conference on Robot Learning (CoRL), 2023. 10
[79] John Won, Kyungmin Lee, Huiwon Jang, Dongyoung Kim, and Jinwoo Shin. Dual-stream diffusion for
world-model augmented vision-language-action model. arXiv preprint arXiv:2510.27607, 2025. 5
[80] Hongtao Wu, Ya Jing, Chilam Cheang, Guangzeng Chen, Jiafeng Xu, Xinghang Li, Minghuan Liu, Hang
Li, and Tao Kong. Unleashing large-scale video generative pre-training for visual robot manipulation. In
The Twelfth International Conference on Learning Representations, 2024. URL https://openreview.net/
forum?id=NxoFmGgWC9. 5
[81] An Yang, Anfeng Li, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen Yu, Chang Gao,
Chengen Huang, Chenxu Lv, et al. Qwen3 technical report. arXiv preprint arXiv:2505.09388, 2025. 18
[82] Jianwei Yang, Reuben Tan, Qianhui Wu, Ruijie Zheng, Baolin Peng, Yongyuan Liang, Yu Gu, Mu Cai,
Seonghyeon Ye, Joel Jang, Yuquan Deng, Lars Liden, and Jianfeng Gao. Magma: A foundation model for
multimodal AI agents, 2025. 4
[83] Sherry Yang, Yilun Du, Seyed Kamyar Seyed Ghasemipour, Jonathan Tompson, Leslie Pack Kaelbling, Dale
Schuurmans, and Pieter Abbeel. Learning interactive real-world simulators. In The Twelfth International
Conference on Learning Representations, 2024. URL https://openreview.net/forum?id=sFyTZEqmUY.
[84] Seonghyeon Ye, Joel Jang, Byeongguk Jeon, Se June Joo, Jianwei Yang, Baolin Peng, Ajay Mandlekar,
Reuben Tan, Yu-Wei Chao, Bill Yuchen Lin, Lars Liden, Kimin Lee, Jianfeng Gao, Luke Zettlemoyer, Dieter
Fox, and Minjoon Seo. Latent action pretraining from videos. In The Thirteenth International Conference
on Learning Representations, 2025. URL https://openreview.net/forum?id=VYOe2eBQeh. 4
[85] Tianwei Yin, Qiang Zhang, Richard Zhang, William T Freeman, Fredo Durand, Eli Shechtman, and Xun
Huang. From slow bidirectional to fast autoregressive video diffusion models. In Proceedings of the
Computer Vision and Pattern Recognition Conference, pages 22963–22974, 2025. 8
[86] Qingqing Zhao, Yao Lu, Moo Jin Kim, Zipeng Fu, Zhuoyang Zhang, Yecheng Wu, Zhaoshuo Li, Qianli
Ma, Song Han, Chelsea Finn, et al. Cot-vla: Visual chain-of-thought reasoning for vision-language-action
models. arXiv preprint arXiv:2503.22020, 2025. 5
[87] Wenliang Zhao, Lujia Bai, Yongming Rao, Jie Zhou, and Jiwen Lu. UniPC: A unified predictor-corrector
framework for fast sampling of diffusion models. In Thirty-seventh Conference on Neural Information
Processing Systems, 2023. URL https://openreview.net/forum?id=hrkmlPhp1u. 23
[88] Ruijie Zheng, Yongyuan Liang, Shuaiyi Huang, Jianfeng Gao, Hal Daumé III, Andrey Kolobov, Furong
Huang, and Jianwei Yang. TraceVLA: Visual trace prompting enhances spatial-temporal awareness for
generalist robotic policies. In The Thirteenth International Conference on Learning Representations, 2025. 4
[89] Ruijie Zheng, Jing Wang, Scott Reed, Johan Bjorck, Yu Fang, Fengyuan Hu, Joel Jang, Kaushil Kundalia,
Zongyu Lin, Loic Magne, et al. Flare: Robot learning with implicit world modeling. arXiv preprint
arXiv:2505.15659, 2025. 5
[90] Jiaming Zhou, Ke Ye, Jiayi Liu, Teli Ma, Zifan Wang, Ronghe Qiu, Kun-Yu Lin, Zhilin Zhao, and Junwei
Liang. Exploring the limits of vision-language-action manipulations in cross-task generalization. arXiv
preprint arXiv:2505.15660, 2025. 2
[91] Siyuan Zhou, Yilun Du, Jiaben Chen, Yandong Li, Dit-Yan Yeung, and Chuang Gan. Robodreamer:
Learning compositional world models for robot imagination. arXiv preprint arXiv:2404.12377, 2024. 5
[92] Chuning Zhu, Raymond Yu, Siyuan Feng, Benjamin Burchfiel, Paarth Shah, and Abhishek Gupta. Unified
world models: Coupling video and action diffusion for pretraining on large robotic datasets. arXiv preprint
arXiv:2504.02792, 2025. 5, 7
