# DeepScan: A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models

> **中文题名：** DeepScan：面向大型视觉语言模型视觉落地推理的免训练框架  
> **作者：** Yangfu Li, Hongjian Zhan, Jiawei Chen, Yuning Gong, Qi Liu, Yue Lu  
> **出处：** CVPR 2026（论文注明已接收）；arXiv:2603.03857v1，2026-03-04  
> **源文件：** `Li 等 - 2026 - DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models.pdf`（18 页）  
> **完整性状态：** 完整；正文、补充材料、图表、提示词、算法、示例输出与参考文献均按源顺序覆盖。

## 阅读导航

- [术语表](#术语表)
- [Abstract](#abstract--摘要)
- [1. Introduction](#1-introduction--引言)
- [2. Related Work](#2-related-work--相关工作)
- [3. Methodology](#3-methodology--方法)
- [4. Experiments](#4-experiments--实验)
- [5. Conclusion](#5-conclusion--结论)
- [Acknowledgments](#acknowledgments--致谢)
- [Supplementary Material](#supplementary-material--补充材料)
- [References](#references)

## 术语表

| Canonical term | 中文 | 说明 |
|---|---|---|
| Large Vision-Language Model (LVLM) | 大型视觉语言模型 | 后文统一保留 LVLM |
| visually grounded reasoning | 视觉落地推理 | 答案显式依赖定位后的视觉证据 |
| Hierarchical Scanning | 分层扫描 | 局部线索探索与多尺度证据提取 |
| Local Cue Exploration | 局部线索探索 | 在图块内寻找高响应线索 |
| Multi-Scale Evidence Extraction | 多尺度证据提取 | 由点代理在原图恢复证据 |
| Refocusing | 再聚焦 | 搜索证据中心且上下文合适的视图 |
| Evidence-Enhanced Reasoning | 证据增强推理 | 使用多粒度证据完成回答 |
| Hybrid Evidence Memory | 混合证据记忆 | 保存细粒度证据与粗粒度视图 |
| point-based proxy | 点式代理 | 驱动点提示分割的图块内点 |
| attention sink / attention drift | 注意力汇聚 / 注意力漂移 | 显著干扰吸引注意或注意转向相似物体 |

## Figure 1

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig1.png)

**Caption:** Comparison of grounding pipelines in existing methods and the proposed DeepScan. (a) Existing methods depend on *one-shot* localization of evidence regions, making them sensitive to noisy contexts. (b) DeepScan uses local cue exploration to identify discriminative cues and recovers evidence from these cues in a *bottom-up* manner, robustly localizing critical visual content even in challenging scenes.

**Caption[CN]:** 现有方法与所提出的 DeepScan 的定位流程对比。(a) 现有方法依赖对证据区域进行*一次性*定位，因此容易受到噪声上下文的影响。(b) DeepScan 通过局部线索探索来识别具有判别力的线索，并以*自底向上*的方式从这些线索中恢复证据，即使在具有挑战性的场景中也能稳健地定位关键视觉内容。

# Abstract / 摘要

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Humans can robustly localize visual evidence and provide grounded answers even in noisy environments by identifying critical cues and then relating them to the full context in a bottom-up manner. Inspired by this, we propose DeepScan, a training-free framework that combines Hierarchical Scanning, Refocusing, and Evidence-Enhanced Reasoning for visually grounded reasoning in Large Vision–Language Models (LVLMs). Unlike existing methods that pursue one-shot localization of complete evidence, Hierarchical Scanning performs local cue exploration and multi-scale evidence extraction to recover evidence in a bottom-up manner, effectively mitigating the impacts of distractive context. Refocusing then optimizes the localized evidence view through collaboration of LVLMs and visual experts. Finally, Evidence-Enhanced Reasoning aggregates multi-granular views via a hybrid evidence memory and yields accurate and interpretable answers. Experimental results demonstrate that DeepScan significantly boosts LVLMs in diverse visual tasks, especially in fine-grained visual understanding. It achieves 90.6% overall accuracy on V* when integrated with Qwen2.5-VL-7B. Moreover, DeepScan provides consistent improvements for LVLMs across various architectures and model scales without additional adaptation cost. The code will be open-source at [DeepScan](https://github.com/YChenL/DeepScan).

> <span style="color:#3B82F6"><strong>Para. 1[CN]:</strong></span> 人类即使身处噪声环境，也能通过识别关键线索，再以自底向上的方式将其与完整上下文关联起来，从而稳健地定位视觉证据并给出有依据的答案。受此启发，我们提出 DeepScan：一个无需训练的框架，它结合了分层扫描（Hierarchical Scanning）、重新聚焦（Refocusing）和证据增强推理（Evidence-Enhanced Reasoning），用于大型视觉—语言模型（LVLM）的视觉依据推理。不同于追求一次性定位完整证据的现有方法，分层扫描通过局部线索探索和多尺度证据提取，以自底向上的方式恢复证据，从而有效减轻干扰性上下文的影响。随后，重新聚焦通过 LVLM 与视觉专家的协作来优化已定位的证据视图。最后，证据增强推理借助混合证据记忆聚合多粒度视图，并生成准确且可解释的答案。实验结果表明，DeepScan 在多种视觉任务上显著增强了 LVLM，尤其是在细粒度视觉理解方面。当与 Qwen2.5-VL-7B 集成时，它在 V* 上取得了 90.6% 的总体准确率。此外，无需额外的适配成本，DeepScan 即可在不同架构和模型规模的 LVLM 上带来一致提升。代码将在 [DeepScan](https://github.com/YChenL/DeepScan) 开源。

# 1. Introduction / 引言

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Humans excel at grounding critical visual information and reasoning based on the located evidence, which is a hallmark of intelligence recognized in the cognitive and vision science [@wang2023statistical; @wolfe2020visual; @wolfe2017five]. While this is natural to humans, it remains challenging for Large Vision-Language Models (LVLMs) to replicate this behavior, leading to suboptimal performance in complex visual tasks [@wangscaling; @wu2024vstar; @wang2025hrbench; @li20251+].

> <span style="color:#3B82F6"><strong>Para. 1[CN]:</strong></span> 人类擅长将关键视觉信息落到具体依据上，并基于所定位的证据进行推理；认知科学与视觉科学将其视为智能的标志之一 [@wang2023statistical; @wolfe2020visual; @wolfe2017five]。这种行为对人类而言十分自然，但大型视觉—语言模型（LVLM）仍难以复现它，因而在复杂视觉任务上的表现并不理想 [@wangscaling; @wu2024vstar; @wang2025hrbench; @li20251+]。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> To reproduce this ability in LVLMs, some approaches have employed reinforcement learning [@su2025pixelreasoner; @zheng2025deepeyes; @wang2025traceable; @zhang2025thyme] with visually supervised rewards (e.g., IoU) or context engineering [@wu2024vstar; @yu2025zoom], enabling active perception and localization of evidence during reasoning. Another line of research augments LVLM grounding with auxiliary modules [@chen2023shikra; @Rasheed2024GLaMM; @You2024Ferret; @Zhang2025PSALM]. More recently, several studies [@li2025dyfo; @an2025mitigating; @qian2025zoomer] integrate external visual experts, such as GroundingDINO [@liu2024grounding; @ren2024grounding] and LangSAM [@medeiros2024language], to localize visual evidence based on the consensus between these experts and LVLMs, significantly enhancing fine-grained visual understanding in LVLMs.

> <span style="color:#3B82F6"><strong>Para. 2[CN]:</strong></span> 为了在 LVLM 中复现这种能力，一些方法采用带有视觉监督奖励（例如 IoU）的强化学习 [@su2025pixelreasoner; @zheng2025deepeyes; @wang2025traceable; @zhang2025thyme] 或上下文工程 [@wu2024vstar; @yu2025zoom]，使模型能够在推理过程中主动感知并定位证据。另一条研究路线利用辅助模块增强 LVLM 的定位能力 [@chen2023shikra; @Rasheed2024GLaMM; @You2024Ferret; @Zhang2025PSALM]。近期，若干研究 [@li2025dyfo; @an2025mitigating; @qian2025zoomer] 引入 GroundingDINO [@liu2024grounding; @ren2024grounding]、LangSAM [@medeiros2024language] 等外部视觉专家，依据这些专家与 LVLM 之间的共识来定位视觉证据，显著增强了 LVLM 的细粒度视觉理解能力。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Despite these advances, most existing methods follow a *top-down* grounding paradigm: they first perform an image-level search for coarse-grained proxies, such as region proposals [@su2025pixelreasoner; @zheng2025deepeyes; @wang2025traceable; @zhang2025thyme; @yu2025zoom], detection boxes [@li2025dyfo; @qian2025zoomer], or textual descriptions [@wang2025hrbench], and then refine these proxies to obtain fine-grained evidence. However, this paradigm requires the *one-shot* localization of complete evidence regions from the entire image, which is easily affected by noisy context, i.e., attention sink [@xiaoefficient], or semantically similar objects, i.e., attention drift [@cheng2017focusing], leading to suboptimal performance. In such cases, the LVLM either refuses to answer or makes uninformed guesses based on incorrect evidence, as illustrated in Figure 1. By contrast, humans intuitively adopt a *bottom-up* routine in challenging visual tasks. For example, when playing the “*spot-the-difference*” puzzles, people scan local patches for subtle discrepancies within largely similar content, then verify these cues at the image level to recover the target while suppressing distracting context.

> <span style="color:#3B82F6"><strong>Para. 3[CN]:</strong></span> 尽管取得了这些进展，大多数现有方法仍遵循一种*自顶向下*的定位范式：首先在图像层面搜索粗粒度代理，例如区域提议 [@su2025pixelreasoner; @zheng2025deepeyes; @wang2025traceable; @zhang2025thyme; @yu2025zoom]、检测框 [@li2025dyfo; @qian2025zoomer] 或文本描述 [@wang2025hrbench]，然后再细化这些代理以获得细粒度证据。然而，这种范式要求从整幅图像中*一次性*定位完整的证据区域，极易受到噪声上下文——即注意力汇聚（attention sink）[@xiaoefficient]——或语义相似对象——即注意力漂移（attention drift）[@cheng2017focusing]——的影响，从而导致次优表现。在这种情况下，LVLM 要么拒绝回答，要么依据错误证据作出缺乏信息支撑的猜测，如图 1 所示。相比之下，人类在具有挑战性的视觉任务中会直觉地采用*自底向上*的过程。例如，在玩“*找不同*”游戏时，人们会在内容大体相似的局部图块中扫描细微差异，再在图像层面对这些线索加以验证，从而在抑制干扰上下文的同时恢复目标。

## Figure 2

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig2.png)

**Caption:** Performance of LVLMs and visually grounded reasoning variants on V*. DeepScan achieves highly competitive results.

**Caption[CN]:** LVLM 与视觉依据推理变体在 V* 上的表现。DeepScan 取得了极具竞争力的结果。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Inspired by this human behavior, we propose **DeepScan**, a training-free framework for visually grounded reasoning in LVLMs, comprising Hierarchical Scanning, Refocusing, and Evidence-Enhanced Reasoning. Unlike existing methods, Hierarchical Scanning leverages patch-wise cue exploration and image-level evidence extraction to robustly localize visual evidence in a bottom-up manner. Refocusing further refines the surrounding context of the extracted evidence through collaboration between the visual experts and LVLMs, reducing information loss. Finally, Evidence-Enhanced Reasoning utilizes a Hybrid Evidence Memory to provide LVLMs with multi-granular evidence views, producing accurate and well-grounded answers. Figure 2 shows that DeepScan performs competitively with leading approaches. Moreover, as a training-free framework, DeepScan scales seamlessly to larger models (e.g., Qwen2.5-VL-72B), yielding consistently improved performance. Extensive experiments across diverse visual tasks further demonstrate its effectiveness. Our contributions are fourfold:

> <span style="color:#3B82F6"><strong>Para. 4[CN]:</strong></span> 受这种人类行为启发，我们提出 **DeepScan**，这是一个面向 LVLM 视觉依据推理的无需训练框架，由分层扫描、重新聚焦和证据增强推理组成。不同于现有方法，分层扫描利用逐图块线索探索与图像级证据提取，以自底向上的方式稳健地定位视觉证据。重新聚焦进一步通过视觉专家与 LVLM 之间的协作来细化已提取证据的周边上下文，从而减少信息损失。最后，证据增强推理利用混合证据记忆为 LVLM 提供多粒度证据视图，生成准确且依据充分的答案。图 2 表明，DeepScan 的表现可与领先方法竞争。此外，作为无需训练的框架，DeepScan 可以无缝扩展至更大的模型（例如 Qwen2.5-VL-72B），并持续带来性能提升。跨多种视觉任务的大量实验进一步证明了其有效性。我们的贡献有以下四点：

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> 1. We introduce **DeepScan**, a training-free framework that boosts LVLM performance by explicitly localizing, recalibrating, and integrating evidence before answering.

> <span style="color:#3B82F6"><strong>Para. 5[CN]:</strong></span> 1. 我们提出 **DeepScan**：一个无需训练的框架，通过在作答前显式地定位、重新校准并整合证据来提升 LVLM 的性能。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> 2. We propose **Hierarchical Scanning**, a bottom-up visual grounding paradigm that mitigates noisy context via local cue exploration and multi-scale evidence extraction.

> <span style="color:#3B82F6"><strong>Para. 6[CN]:</strong></span> 2. 我们提出**分层扫描**：一种自底向上的视觉定位范式，通过局部线索探索和多尺度证据提取减轻噪声上下文的影响。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> 3. We present **Refocusing**, a collaborative search paradigm that recalibrates the evidence view through interactions between LVLMs and external visual experts.

> <span style="color:#3B82F6"><strong>Para. 7[CN]:</strong></span> 3. 我们提出**重新聚焦**：一种协作式搜索范式，通过 LVLM 与外部视觉专家之间的交互重新校准证据视图。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> 4. Comprehensive experiments validate the superiority of DeepScan. It provides average improvements of 16.3% on V* and 5.5% on TreeBench for Qwen2.5-VL-7B. Detailed ablation studies across LVLM architectures and scales further validate the generalizability of our method.

> <span style="color:#3B82F6"><strong>Para. 8[CN]:</strong></span> 4. 全面的实验验证了 DeepScan 的优越性。对于 Qwen2.5-VL-7B，它在 V* 和 TreeBench 上分别带来平均 16.3% 和 5.5% 的提升。跨 LVLM 架构和规模的详细消融研究进一步验证了我们方法的泛化能力。

# 2. Related Work / 相关工作

## 2.1 Large Vision-Language Models / 大型视觉—语言模型

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Early breakthroughs in Large Vision-Language Models (LVLMs), such as Flamingo [@alayrac2022flamingo] and BLIP-2 [@li2023blip], integrated visual features into an LLM via cross-attention. In contrast, LLaVA [@liu2023llava] maps features from a frozen vision encoder (e.g., CLIP [@radford2021learning]) into the LLM’s semantic space with a lightweight MLP. This feature-projection paradigm has driven rapid progress, with subsequent work scaling LVLMs and tackling increasingly complex tasks, such as OCR [@zhan2024free; @li2025msa2; @zhan2024fare], general VQA [@liu2024llavanext; @li2024llavaov; @zhu2025internvl3], and latent visual reasoning [@zhang2025latent; @li2024mvot]. A critical frontier is to handle high-resolution input. For instance, LLaVA-NeXT [@liu2024llavanext] and InternVL1.5 [@chen2024internvl15] support arbitrary resolutions, while Qwen2-VL [@wang2024qwen2vl] and Qwen2.5-VL [@bai2025qwen25vl] introduce mRoPE for resolution generality. Despite these advances, current LVLMs lack an explicit mechanism to perceive and localize task-relevant visual evidence, which leads to hallucinations, especially in high-resolution scenes. We address this gap with DeepScan, a training-free framework that couples LVLMs with external experts to achieve visually grounded reasoning, yielding more accurate and interpretable answers.

> <span style="color:#3B82F6"><strong>Para. 1[CN]:</strong></span> 大型视觉—语言模型（LVLM）的早期突破，例如 Flamingo [@alayrac2022flamingo] 和 BLIP-2 [@li2023blip]，通过交叉注意力将视觉特征整合进 LLM。相比之下，LLaVA [@liu2023llava] 使用轻量级 MLP，将冻结视觉编码器（例如 CLIP [@radford2021learning]）提取的特征映射到 LLM 的语义空间。这种特征投影范式推动了快速进展，后续工作不断扩大 LVLM 的规模，并处理日益复杂的任务，例如 OCR [@zhan2024free; @li2025msa2; @zhan2024fare]、通用 VQA [@liu2024llavanext; @li2024llavaov; @zhu2025internvl3] 和潜在视觉推理 [@zhang2025latent; @li2024mvot]。一个关键前沿是处理高分辨率输入。例如，LLaVA-NeXT [@liu2024llavanext] 和 InternVL1.5 [@chen2024internvl15] 支持任意分辨率，而 Qwen2-VL [@wang2024qwen2vl] 与 Qwen2.5-VL [@bai2025qwen25vl] 则引入 mRoPE 以获得分辨率通用性。尽管取得了这些进展，当前 LVLM 仍缺乏显式感知并定位任务相关视觉证据的机制，因而会产生幻觉，尤其是在高分辨率场景中。我们以 DeepScan 弥补这一缺口：该无需训练的框架将 LVLM 与外部专家耦合，实现视觉依据推理，从而给出更准确、更可解释的答案。

## Figure 3

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig3.png)

**Caption:** Overall architecture of **DeepScan**: Hierarchical Scanning progressively recovers visual evidence from *in-patch* cues formulated as point-based proxies using Local Cue Exploration and Multi-Scale Evidence Extraction, e.g., $c^1_{T} \mapsto e_{t-1}$ in step $T$; Refocusing further refines the surrounding context for the fused evidence via interactions between LVLMs and visual experts; Evidence-Enhanced Reasoning leverages a Hybrid Evidence Memory to provide multi-granular information to the LVLM, enabling detailed yet comprehensive answers.

**Caption[CN]:** **DeepScan** 的整体架构：分层扫描利用局部线索探索和多尺度证据提取，从被表示为点式代理的*图块内*线索中逐步恢复视觉证据，例如步骤 $T$ 中的 $c^1_{T} \mapsto e_{t-1}$；重新聚焦通过 LVLM 与视觉专家之间的交互，进一步细化融合证据的周边上下文；证据增强推理利用混合证据记忆向 LVLM 提供多粒度信息，使其能够生成既细致又全面的答案。

## 2.2 Visually Grounded Reasoning / 视觉依据推理

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Recent agents with “*think-with-images*” capabilities (e.g., GPT-o3 [@o3]) perform visually grounded reasoning that localizes and emphasizes the critical visual content during inference through dynamic image manipulation [@xie2024large; @su2025thinking; @o3]. Building on this, subsequent works employ SFT and reinforcement learning (RL) with visual rewards [@wang2025vgr; @zheng2025deepeyes; @wang2025traceable; @zhang2025thyme; @su2025openthinkimg; @lai2025mini], or curiosity-driven objectives [@su2025pixelreasoner] to reproduce this ability in general LVLMs; SEAL [@wu2024vstar] further integrates explicit evidence localization and visual memory. However, these approaches are costly and challenging to generalize to different architectures and model scales. To overcome this, a parallel line explores training-free paradigms that leverage external visual experts [@li2025dyfo; @an2025mitigating; @You2024Ferret; @Zhang2025PSALM], tree search [@shen2024zoomeye], or self-refinement [@yu2025zoom] to enhance LVLMs by “grounding-then-answering.” Despite these advances, most of them rely on a *coarse-to-fine* grounding strategy, which is sensitive to noisy context and semantically similar objects, resulting in inaccurate localization. By contrast, we propose Hierarchical Scanning, a *bottom-up* grounding paradigm that progressively recovers visual evidence from associated local cues via point-based proxies, enabling robust localization of fine-grained visual evidence in complex scenes.

> <span style="color:#3B82F6"><strong>Para. 2[CN]:</strong></span> 近期，具备“*用图像思考*”能力的智能体（例如 GPT-o3 [@o3]）能够执行视觉依据推理，即在推理期间通过动态图像操作来定位并突出关键视觉内容 [@xie2024large; @su2025thinking; @o3]。在此基础上，后续工作采用带视觉奖励的监督微调（SFT）和强化学习（RL）[@wang2025vgr; @zheng2025deepeyes; @wang2025traceable; @zhang2025thyme; @su2025openthinkimg; @lai2025mini]，或采用好奇心驱动的目标 [@su2025pixelreasoner]，以便在通用 LVLM 中复现这种能力；SEAL [@wu2024vstar] 还进一步整合了显式证据定位与视觉记忆。然而，这些方法成本高昂，并且难以泛化到不同架构与模型规模。为克服这一问题，另一条并行研究路线探索无需训练的范式，利用外部视觉专家 [@li2025dyfo; @an2025mitigating; @You2024Ferret; @Zhang2025PSALM]、树搜索 [@shen2024zoomeye] 或自我细化 [@yu2025zoom]，通过“先定位、后作答”来增强 LVLM。尽管取得了这些进展，其中大多数方法仍依赖*由粗到细*的定位策略；该策略对噪声上下文和语义相似对象十分敏感，因而会造成定位不准。相比之下，我们提出分层扫描：一种*自底向上*的定位范式，通过点式代理从相关局部线索中逐步恢复视觉证据，从而在复杂场景中稳健地定位细粒度视觉证据。

# 3. Methodology / 方法

## 3.1 Overview / 概述

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> To equip LVLMs with visually grounded reasoning, we propose **DeepScan** that localizes, recalibrates, and integrates visual evidence to produce more accurate and interpretable answers, as shown in Figure 3. To enhance fine-grained perception, DeepScan augments LVLMs with two *plug-and-play* models, i.e., a search expert and a visual expert. Formally, given an image $I\in\mathbb{R}^{H\times W\times3}$ with a question $q$, the search expert highlights the potential cues in a local patch $p\in I$ via its attention map $S$ induced by GradCAM [@Selvaraju2017GradCAM]:

> <span style="color:#3B82F6"><strong>Para. 1[CN]:</strong></span> 为使 LVLM 具备视觉依据推理能力，我们提出 **DeepScan**；如图 3 所示，它通过定位、重新校准和整合视觉证据来生成更准确、更可解释的答案。为增强细粒度感知，DeepScan 为 LVLM 配备两个*即插即用*模型，即搜索专家和视觉专家。形式化地，给定图像 $I\in\mathbb{R}^{H\times W\times3}$ 及问题 $q$，搜索专家通过由 GradCAM [@Selvaraju2017GradCAM] 诱导的注意力图 $S$，突出局部图块 $p\in I$ 中的潜在线索：

$$
S =\operatorname{Search}(p,q)\in\mathbb{R}^{h\times w},\quad p\in\mathbb{R}^{h\times w\times3}.
\tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> By contrast, the visual expert exposes two primitives to indicate the image-level evidence: segmentation from a point prompt $c=(x,y)\in I$ and detection from the question $q$:

> <span style="color:#3B82F6"><strong>Para. 2[CN]:</strong></span> 相比之下，视觉专家提供两个用于指示图像级证据的基本操作：根据点提示 $c=(x,y)\in I$ 进行分割，以及根据问题 $q$ 进行检测：

$$
m=\operatorname{Segment}(I,c),\quad \mathcal{B}=\operatorname{Detect}(I,q).
\tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> where $m$ denotes the evidence mask, and $\mathcal{B}$ represents the union of evidence bounding boxes. In this way, the LVLM can generate a well-grounded answer for the question using the image regions enclosed by $m$ or $\mathcal{B}$. This pipeline is general and training-free, improving LVLMs across architectures and model scales without adaptation cost.

> <span style="color:#3B82F6"><strong>Para. 3[CN]:</strong></span> 其中，$m$ 表示证据掩码，$\mathcal{B}$ 表示证据边界框的并集。这样，LVLM 便可利用 $m$ 或 $\mathcal{B}$ 所围定的图像区域，针对问题生成依据充分的答案。该流程具有通用性且无需训练，可以在不产生适配成本的情况下提升不同架构和模型规模的 LVLM。

## 3.2 Hierarchical Scanning / 分层扫描

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> To suppress the effects of irrelevant visual content, a natural idea is to partition the image into patches and perform a patch-wise evidence extraction. However, this poses a fundamental challenge: when evidence spans multiple patches, conventional proxies (e.g., region proposals [@su2025pixelreasoner; @zheng2025deepeyes; @wang2025traceable; @zhang2025thyme], detection boxes [@li2025dyfo; @qian2025zoomer], or textual descriptions [@wang2025hrbench]) struggle to represent the resulting incomplete evidence.

> <span style="color:#3B82F6"><strong>Para. 4[CN]:</strong></span> 为抑制无关视觉内容的影响，一种自然的思路是将图像划分为若干图块，并逐图块提取证据。然而，这带来了一个根本性挑战：当证据跨越多个图块时，传统代理（例如区域提议 [@su2025pixelreasoner; @zheng2025deepeyes; @wang2025traceable; @zhang2025thyme]、检测框 [@li2025dyfo; @qian2025zoomer] 或文本描述 [@wang2025hrbench]）难以表示由此产生的不完整证据。

### Figure 4

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig4.png)

**Caption:** Illustration of morphological post-processing. **+** marks the point-based proxies; $m$ and $m^+$ denote evidence masks before and after post-processing, showing improved robustness.

**Caption[CN]:** 形态学后处理示意图。**+** 标记点式代理；$m$ 和 $m^+$ 分别表示后处理前后的证据掩码，显示出更强的鲁棒性。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> To address this issue, Hierarchical Scanning introduces novel *point-based proxies* to bridge two well-designed processes, i.e., *patch-wise* Local Cue Exploration and *image-level* Multi-scale Evidence Extraction, thereby enabling a bottom-up visual grounding paradigm.

> <span style="color:#3B82F6"><strong>Para. 5[CN]:</strong></span> 为解决这一问题，分层扫描引入新颖的*点式代理*，将两个经过精心设计的过程连接起来，即*逐图块*局部线索探索和*图像级*多尺度证据提取，从而实现一种自底向上的视觉定位范式。

### Local Cue Exploration / 局部线索探索

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Given a patch $p \in \mathbb{R}^{h\times w\times 3}$ from the input image $I$ and a question $q$, we first apply the search expert and Otsu’s method [@otsu1975threshold] to produce potential cue regions indicated by a high-value attention mask $S_p^{+}$:

> <span style="color:#3B82F6"><strong>Para. 6[CN]:</strong></span> 给定输入图像 $I$ 中的图块 $p \in \mathbb{R}^{h\times w\times 3}$ 以及问题 $q$，我们首先应用搜索专家和 Otsu 方法 [@otsu1975threshold]，生成由高值注意力掩码 $S_p^{+}$ 指示的潜在线索区域：

$$
S_p^{+} = \mathbb{I}\big(S_p \ge T_p^\star\big)\in\{0,1\}^{h\times w},\quad
T_p^\star = \operatorname{Otsu}(S_p).
\tag{3}
$$

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> where $S_p = \operatorname{Search}(p, q) \in \mathbb{R}^{h\times w}$. We then formulate the *cues* $\{G_p^k\}_{k=1}^{K}$ as the connected components in $S_p^{+}$. To associate these cues with evidence, we represent each cue by an interior point derived from its geometric and semantic information, enabling efficient evidence retrieval via point-prompt segmentation. For any interior location $c\in G$, the geometric term is its distance to the cue boundary $\partial G$:

> <span style="color:#3B82F6"><strong>Para. 7[CN]:</strong></span> 其中，$S_p = \operatorname{Search}(p, q) \in \mathbb{R}^{h\times w}$。随后，我们将*线索* $\{G_p^k\}_{k=1}^{K}$ 表示为 $S_p^{+}$ 中的连通分量。为了将这些线索与证据关联起来，我们依据每条线索的几何信息和语义信息，用一个内部点来表示它，从而可通过点提示分割高效检索证据。对于任意内部位置 $c\in G$，其几何项为该点到线索边界 $\partial G$ 的距离：

$$
d(c,\partial G)=\inf_{\gamma\in\partial G}\lVert c-\gamma\rVert_2.
\tag{4}
$$

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Considering only Equation (4) can yield multiple candidates for complex cues (e.g., U-shaped regions); we therefore incorporate the attention scores to disambiguate and bias the evidence proxies $\mathcal{C}_p$ toward semantically significant regions:

> <span style="color:#3B82F6"><strong>Para. 8[CN]:</strong></span> 若只考虑公式 (4)，复杂线索（例如 U 形区域）可能产生多个候选点；因此，我们引入注意力分数来消除歧义，并使证据代理 $\mathcal{C}_p$ 偏向语义显著区域：

$$
\mathcal{C}_p=\Big\{c_p^k \mid c_p^k{=}\arg\max_{c\in G_p^k}
\tilde{S}_p(c)\,\tilde{d}(c,\partial G_p^k),\ |G_p^k|{\ge}\tau\Big\}.
\tag{5}
$$

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> where $\tau$ is a threshold that filters out spurious small cues. $\tilde{S}_p(c)$ is the normalized attention score at $c$, and $\tilde{d}(c,\partial G_p^k)$ is the normalized distance-to-boundary at $c$. Finally, we lift these *in-patch* proxies $\mathcal{C}_p$ to the image coordinates for $\mathcal{C}_p'$.

> <span style="color:#3B82F6"><strong>Para. 9[CN]:</strong></span> 其中，$\tau$ 是用于滤除虚假小线索的阈值。$\tilde{S}_p(c)$ 是位置 $c$ 处归一化后的注意力分数，$\tilde{d}(c,\partial G_p^k)$ 是位置 $c$ 处归一化后的边界距离。最后，我们将这些*图块内*代理 $\mathcal{C}_p$ 提升到图像坐标系中，得到 $\mathcal{C}_p'$。

### Figure 5

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig5.png)

**Caption:** Analysis of (*left*) performance gain w.r.t. target area ratio and (*right*) performance-latency trade-off on V*, where the $\infty$ mark denotes the case *without* explicit truncation of candidate count $k$.

**Caption[CN]:** 在 V* 上对（*左*）相对于目标面积占比的性能增益以及（*右*）性能—时延权衡的分析，其中 $\infty$ 标记表示*未*对候选数量 $k$ 进行显式截断的情形。

### Multi-scale Evidence Extraction / 多尺度证据提取

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> Given a proxy $c^\prime_p \in \mathcal{C}^\prime_{p}$ obtained from image $I$, we employ the visual expert to recover the evidence mask $m$ by point-prompt segmentation:

> <span style="color:#3B82F6"><strong>Para. 10[CN]:</strong></span> 给定从图像 $I$ 获得的代理 $c^\prime_p \in \mathcal{C}^\prime_{p}$，我们利用视觉专家，通过点提示分割来恢复证据掩码 $m$：

$$
m = \operatorname{Segment}(I, c^\prime_p)\in \{0,1\}^{H \times W},\quad
I \in \mathbb{R}^{H \times W \times 3}.
\tag{6}
$$

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> In particular, although the mask $m$ captures image-level evidence, the single-point prompt has limited expressiveness; as a result, $m$ often contains artifacts, e.g., interior holes or incomplete surrounding context, as shown in Figure 4. To ensure the evidence integrity, we adopt morphological post-processing and produce the enhanced mask $m^{+}$:

> <span style="color:#3B82F6"><strong>Para. 11[CN]:</strong></span> 具体而言，尽管掩码 $m$ 捕获了图像级证据，但单点提示的表达能力有限；因此，如图 4 所示，$m$ 往往包含伪影，例如内部孔洞或不完整的周边上下文。为确保整条证据的完整性，我们采用形态学后处理并生成增强掩码 $m^{+}$：

$$
m^+= \bigl(m \bullet \mathcal{K}\bigr) \,\oplus\, \mathcal{S}_r,\qquad
m^{+}\in \{0,1\}^{H \times W}.
\tag{7}
$$

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> where $\bullet$ denotes *closing* with a flat kernel $\mathcal{K}$ to seal interior holes, and $\oplus$ denotes *dilation* with a disk kernel $\mathcal{S}_r$ to extend the mask outward. To avoid repeated extraction, we filter any proxies that fall inside the same evidence mask:

> <span style="color:#3B82F6"><strong>Para. 12[CN]:</strong></span> 其中，$\bullet$ 表示使用平坦核 $\mathcal{K}$ 进行*闭运算*以封闭内部孔洞，$\oplus$ 表示使用圆盘核 $\mathcal{S}_r$ 进行*膨胀*以向外扩展掩码。为避免重复提取，我们会滤除落在同一证据掩码内的所有代理：

$$
\mathcal{C}^\prime_p \leftarrow
\left\{c \in \mathcal{C}^\prime_p \;\middle|\; m^+(c) = 0 \right\}.
\tag{8}
$$

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> where $m^+(c)$ denotes the value of $m^+$ at the location indicated by proxy $c$. The evidence candidate $e$ is then cropped from the minimal enclosing region $b$ of $m^{+}$. Motivated by [@li2025dyfo; @yu2025zoom; @wang2025hrbench], we query the LVLM to make a binary judgment of the evidence $e$ (detailed in the supplementary material) and, if affirmed, update the evidence set $\mathcal{E} \leftarrow \mathcal{E} \cup \{(b,\,e)\}$.

> <span style="color:#3B82F6"><strong>Para. 13[CN]:</strong></span> 其中，$m^+(c)$ 表示 $m^+$ 在代理 $c$ 所指位置处的取值。随后，从 $m^{+}$ 的最小包围区域 $b$ 中裁剪出证据候选 $e$。受 [@li2025dyfo; @yu2025zoom; @wang2025hrbench] 启发，我们查询 LVLM，让其对证据 $e$ 作出二元判断（详见补充材料）；若判断为肯定，则更新证据集合 $\mathcal{E} \leftarrow \mathcal{E} \cup \{(b,\,e)\}$。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> Finally, we maintain a global visited mask over the examined evidence, i.e., $I\gets I\odot (1-m^+)$, and bypass the masked region to reduce redundant computation.

> <span style="color:#3B82F6"><strong>Para. 14[CN]:</strong></span> 最后，我们针对已检查的证据维护一个全局已访问掩码，即 $I\gets I\odot (1-m^+)$，并跳过被掩蔽的区域，以减少冗余计算。

### Heuristic Acceleration / 启发式加速

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> As shown in Figure 5 (*left*), localizing less salient evidence leads to a significantly higher performance gain for LVLMs. This is because large evidence regions are often detected by the LVLM without explicit grounding. Therefore, we pre-filter candidates by area and evaluate only the top-$k$ smallest regions, which limits the number of LVLM evaluations to $k$ and reduces the visual-token cost. Empirically, even $k=1$ preserves about 96% of the maximum achievable performance while yielding roughly a $2\times$ speedup, as presented in Figure 5 (*right*).

> <span style="color:#3B82F6"><strong>Para. 15[CN]:</strong></span> 如图 5（*左*）所示，定位不那么显著的证据能够为 LVLM 带来显著更高的性能增益。这是因为 LVLM 通常无需显式定位便可发现较大的证据区域。因此，我们按面积对候选区域进行预过滤，只评估最小的前 $k$ 个区域，从而将 LVLM 的评估次数限制为 $k$ 次，并降低视觉 token 成本。经验结果表明，如图 5（*右*）所示，即使 $k=1$，也能保留最大可达性能的约 96%，同时获得约 $2\times$ 的加速。

### Figure 6

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig6.png)

**Caption:** Illustration of Refocusing, where $V^*$ denotes its results. It reveals that Refocusing recalibrates the proxy misalignment by adaptively completing (*left*) or further amplifying (*right*) evidence.

**Caption[CN]:** 重新聚焦示意图，其中 $V^*$ 表示其结果。该图表明，重新聚焦通过自适应地补全（*左*）或进一步放大（*右*）证据，对代理错位进行重新校准。

## 3.3 Refocusing / 重新聚焦

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> While Hierarchical Scanning effectively recovers evidence via point-based proxies, precise proxy placement becomes challenging when multiple visual elements are spatially adjacent, often yielding insufficient or excessive surrounding context, as shown in Figure 6. To address this, we introduce Refocusing, a collaborative search paradigm that integrates the LVLM with the visual expert to identify an evidence-centric view with an optimal surrounding context window.

> <span style="color:#3B82F6"><strong>Para. 16[CN]:</strong></span> 尽管分层扫描能够通过点式代理有效恢复证据，但当多个视觉元素在空间上相邻时，精确放置代理会变得困难，常常导致周边上下文不足或过多，如图 6 所示。为解决这一问题，我们引入重新聚焦；这是一种将 LVLM 与视觉专家相结合的协作式搜索范式，用于识别以证据为中心且具有最优周边上下文窗口的视图。

### Initialization / 初始化

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> Given an evidence set $\mathcal{E}$ collected by Hierarchical Scanning in image $I$, we initialize the search with the aggregated evidence, i.e., $V_1=\operatorname{Crop}(I, b_{\rm m})$, where $b_{\rm m}$ is the minimum bounding box enclosing all evidence.

> <span style="color:#3B82F6"><strong>Para. 17[CN]:</strong></span> 给定分层扫描在图像 $I$ 中收集的证据集合 $\mathcal{E}$，我们使用聚合后的证据来初始化搜索，即 $V_1=\operatorname{Crop}(I, b_{\rm m})$，其中 $b_{\rm m}$ 是包围全部证据的最小边界框。

### States & Successor Function / 状态与后继函数

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> Search states are defined as neighborhoods of $V_1$ obtained by varying the surrounding context. We design two actions to generate candidate states:

> <span style="color:#3B82F6"><strong>Para. 18[CN]:</strong></span> 搜索状态被定义为通过改变周边上下文而获得的 $V_1$ 的邻域。我们设计了两个动作来生成候选状态：

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> ♦ *Zoom-In.* Narrow the surrounding context by cropping $V$ to the union of detections conditioned on query $q$:

> <span style="color:#3B82F6"><strong>Para. 19[CN]:</strong></span> ♦ *放大。* 以查询 $q$ 为条件，将 $V$ 裁剪为检测结果的并集，从而缩小周边上下文：

$$
\operatorname{In}(V,q)=
\operatorname{Crop}\bigl(V,\,\operatorname{Detect}(V,q)\bigr).
\tag{9}
$$

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> ♦ *Zoom-Out.* Enlarge the surrounding context by isotropically expanding $V$ with scale $s>1$ with respect to its center:

> <span style="color:#3B82F6"><strong>Para. 20[CN]:</strong></span> ♦ *缩小。* 以 $V$ 的中心为基准，按尺度 $s>1$ 对其进行各向同性扩展，从而扩大周边上下文：

$$
\operatorname{Out}(V,s)=
\operatorname{Crop}\bigl(I,\,\operatorname{ScaleBbox}(V,s)\bigr).
\tag{10}
$$

### Selection Policy / 选择策略

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> Motivated by Figure 5 (*left*), we prefer the smallest view that still contains all evidence required to answer the question. Accordingly, we define an LVLM-based reward and select the state with the highest score:

> <span style="color:#3B82F6"><strong>Para. 21[CN]:</strong></span> 受图 5（*左*）启发，我们倾向于选择仍包含回答问题所需全部证据的最小视图。据此，我们定义一个基于 LVLM 的奖励，并选择得分最高的状态：

$$
R(V)=\mathbb{I}_{V\leadsto q}\cdot HW/hw,\quad
V\in\mathbb{R}^{h\times w\times3}.
\tag{11}
$$

> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> Here, $\mathbb{I}_{V\leadsto q}$ is an indicator equal to $1$ if $V$ contains sufficient evidence for answering $q$, and $0$ otherwise. In practice, $\mathbb{I}_{V\leadsto q}$ is obtained from a one-shot binary judgment by the LVLM over the objects in $\mathcal{E}$ (details in the supplementary material).

> <span style="color:#3B82F6"><strong>Para. 22[CN]:</strong></span> 其中，$\mathbb{I}_{V\leadsto q}$ 是一个指示变量：若 $V$ 包含足以回答 $q$ 的证据，则其值为 $1$，否则为 $0$。实践中，$\mathbb{I}_{V\leadsto q}$ 通过 LVLM 对 $\mathcal{E}$ 中对象进行一次性二元判断而获得（详见补充材料）。

### Search Space Design / 搜索空间设计

> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> Unlike existing methods [@shen2024zoomeye; @li2025dyfo] that search the entire image, Hierarchical Scanning provides a well-initialized view $V_1$ for Refocusing, which motivates the following design principles to prune the search space:

> <span style="color:#3B82F6"><strong>Para. 23[CN]:</strong></span> 不同于在整幅图像中进行搜索的现有方法 [@shen2024zoomeye; @li2025dyfo]，分层扫描为重新聚焦提供了一个良好初始化的视图 $V_1$，由此得到以下用于剪枝搜索空间的设计原则：

> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> ♦ The optimal evidence view lies in a neighborhood of $V_1$; thus, *Zoom-In* at $V_1$ is empirically idempotent:

> <span style="color:#3B82F6"><strong>Para. 24[CN]:</strong></span> ♦ 最优证据视图位于 $V_1$ 的某个邻域内；因此，根据经验，在 $V_1$ 上执行*放大*具有幂等性：

$$
\operatorname{In}(\operatorname{In}(V_1,q),q)
=\operatorname{In}(V_1,q)=\mathrm{evidence}.
\tag{12}
$$

> <span style="color:#3B82F6"><strong>Para. 25:</strong></span> ♦ $V_1$ covers a small fraction of $I$; thus, *Zoom-Out* expands $V_1$ without boundary clipping. Hence, for any $s_1,s_2 \ge 1$,

> <span style="color:#3B82F6"><strong>Para. 25[CN]:</strong></span> ♦ $V_1$ 仅覆盖 $I$ 的一小部分；因此，*缩小*可以在不发生边界裁剪的情况下扩展 $V_1$。所以，对于任意 $s_1,s_2 \ge 1$，

$$
\operatorname{Out}(\operatorname{Out}(V_1,s_1),s_2)
=\operatorname{Out}(V_1,s_1s_2).
\tag{13}
$$

> <span style="color:#3B82F6"><strong>Para. 26:</strong></span> ♦ If $V_1$ already contains complete evidence, i.e., $\mathbb{I}_{V_1 \leadsto q}=1$, then $\mathbb{I}_{\operatorname{In}(V_1,q)\leadsto q}=\mathbb{I}_{\operatorname{Out}(\operatorname{In}(V_1,q),s)\leadsto q}=1$, and thus

> <span style="color:#3B82F6"><strong>Para. 26[CN]:</strong></span> ♦ 若 $V_1$ 已经包含完整证据，即 $\mathbb{I}_{V_1 \leadsto q}=1$，则 $\mathbb{I}_{\operatorname{In}(V_1,q)\leadsto q}=\mathbb{I}_{\operatorname{Out}(\operatorname{In}(V_1,q),s)\leadsto q}=1$，因此

$$
R(\operatorname{Out}(\operatorname{In}(V_1,q),s))
\le R(\operatorname{In}(V_1,q)).
\tag{14}
$$

> <span style="color:#3B82F6"><strong>Para. 27:</strong></span> Otherwise (i.e., $\mathbb{I}_{\operatorname{In}(V_1,q)\leadsto q}=\mathbb{I}_{V_1\leadsto q}=0$), if *Zoom-Out* fails to restore the missing context for $\operatorname{In}(V_1,q)$, then

> <span style="color:#3B82F6"><strong>Para. 27[CN]:</strong></span> 否则（即 $\mathbb{I}_{\operatorname{In}(V_1,q)\leadsto q}=\mathbb{I}_{V_1\leadsto q}=0$），若*缩小*无法为 $\operatorname{In}(V_1,q)$ 恢复缺失的上下文，则

$$
R(\operatorname{Out}(\operatorname{In}(V_1,q),s))=0.
\tag{15}
$$

> <span style="color:#3B82F6"><strong>Para. 28:</strong></span> If *Zoom-Out* can restore the context for $\operatorname{In}(V_1,q)$, then it can also restore the context directly from $V_1$, and thus

> <span style="color:#3B82F6"><strong>Para. 28[CN]:</strong></span> 若*缩小*可以为 $\operatorname{In}(V_1,q)$ 恢复上下文，则它也可以直接从 $V_1$ 恢复上下文，因此

$$
R(\operatorname{Out}(\operatorname{In}(V_1,q),s))
\le R(\operatorname{In}(\operatorname{Out}(V_1,s),q)).
\tag{16}
$$

> <span style="color:#3B82F6"><strong>Para. 29:</strong></span> Thus, the state $\operatorname{Out}(\operatorname{In}(V_1,q),s)$ can be omitted from the search space without affecting global optimality.

> <span style="color:#3B82F6"><strong>Para. 29[CN]:</strong></span> 因此，可从搜索空间中省略状态 $\operatorname{Out}(\operatorname{In}(V_1,q),s)$，而不会影响全局最优性。

> <span style="color:#3B82F6"><strong>Para. 30:</strong></span> Based on these principles, we construct the search space via only a depth-2 expansion of $V_1$ and consider a *concise yet behaviorally complete* view set $\mathcal{V}=\{V_1, V_2, V_3, V_4\}$:

> <span style="color:#3B82F6"><strong>Para. 30[CN]:</strong></span> 基于这些原则，我们仅对 $V_1$ 进行深度为 2 的扩展来构建搜索空间，并考虑一个*简洁但在行为上完备*的视图集合 $\mathcal{V}=\{V_1, V_2, V_3, V_4\}$：

$$
V_2=\operatorname{In}(V_1,q),\quad
V_3=\operatorname{Out}(V_1,s),\quad
V_4=\operatorname{In}(V_3,q).
\tag{17}
$$

> <span style="color:#3B82F6"><strong>Para. 31:</strong></span> where the scale $s$ is set to $1.5$ via a grid search. We traverse $\mathcal{V}$ in depth-first order and greedily select the best view.

> <span style="color:#3B82F6"><strong>Para. 31[CN]:</strong></span> 其中，尺度 $s$ 通过网格搜索设为 $1.5$。我们按深度优先顺序遍历 $\mathcal{V}$，并贪心地选择最佳视图。

## 3.4 Evidence-Enhanced Reasoning / 证据增强推理

> <span style="color:#3B82F6"><strong>Para. 32:</strong></span> During the preceding stages, we build a hybrid evidence memory $\mathcal{H}$ that stores fine-grained evidence from Hierarchical Scanning and coarse-grained views from Refocusing:

> <span style="color:#3B82F6"><strong>Para. 32[CN]:</strong></span> 在前述阶段中，我们构建了一个混合证据记忆 $\mathcal{H}$，其中存储来自分层扫描的细粒度证据和来自重新聚焦的粗粒度视图：

$$
\mathcal{H}
= \bigl\{e,\,V^* \ \big|\ (b,e)\in\mathcal{E},\
V^*=\operatorname*{\arg\max}_{V\in\mathcal{V}}R(V)\bigr\}.
\tag{18}
$$

> <span style="color:#3B82F6"><strong>Para. 33:</strong></span> This hybrid memory $\mathcal{H}$ is then materialized as an ordered *multi-image prompt* $[e_1,\dots,V^*]$. Leveraging this, LVLMs can resolve object attributes from fine-grained evidence and infer relations from coarse-grained views, yielding more comprehensive and accurate answers $\mathcal{A} = \operatorname{Reason}(\mathcal{H},\, q)$.

> <span style="color:#3B82F6"><strong>Para. 33[CN]:</strong></span> 随后，这个混合记忆 $\mathcal{H}$ 被具现为有序的*多图像提示* $[e_1,\dots,V^*]$。借助它，LVLM 可以从细粒度证据中解析对象属性，并从粗粒度视图中推断关系，从而生成更加全面、准确的答案 $\mathcal{A} = \operatorname{Reason}(\mathcal{H},\, q)$。

## Table 1

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table1.png)

**Caption:** Comparisons on V* Bench and HR-Bench, where all the baselines are developed from Qwen2.5-VL-7B, and the RL-based methods are marked by <span style="color:gray">gray</span>. Results$^\dagger$ are self-collected.

**Caption[CN]:** V* Bench 与 HR-Bench 上的比较。所有基线均基于 Qwen2.5-VL-7B 开发，基于 RL 的方法以<span style="color:gray">灰色</span>标记。带 $^\dagger$ 的结果由作者自行收集。

| Model | V* [@wu2024vstar] Avg | V* *Att* | V* *Spa* | HR-4K [@wang2025hrbench] Avg | HR-4K *Sin* | HR-4K *Cro* | HR-8K [@wang2025hrbench] Avg | HR-8K *Sin* | HR-8K *Cro* |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **General Large Vision-Language Models** |  |  |  |  |  |  |  |  |  |
| GPT-4o-1120 [@gpt4o] | 66.0 | -- | -- | 59.0 | 70.0 | 48.0 | 55.5 | 62.0 | 49.0 |
| LLaVA-OV-7B [@li2024llavaov] | 70.7 | 73.0 | 60.5 | 64.3 | 74.8 | 53.8 | 59.8 | 65.3 | 54.3 |
| LLaVA-OV-72B | 73.8 | 80.9 | 63.2 | 66.3 | 76.5 | 56.0 | 60.9 | 68.8 | 53.0 |
| InternVL3-8B [@zhu2025internvl3] | 72.3 | 73.0 | 71.1 | 70.8 | 79.3 | 62.3 | 62.0 | 64.3 | 59.8 |
| InternVL3-38B | 77.5 | 77.4 | 77.6 | 76.3 | 83.5 | 69.0 | 67.0 | 71.3 | 62.8 |
| InternVL3-78B | 76.4 | 75.7 | 77.6 | 75.5 | 84.5 | 66.5 | 67.3 | 71.8 | 62.8 |
| Qwen2.5VL-7B [@bai2025qwen25vl] | 74.3 | 77.4 | 69.7 | 72.1 | 88.8 | 55.5 | 68.8 | 83.5 | 54.0 |
| Qwen2.5VL-32B | 85.9 | 83.5 | 89.5 | 74.8 | 89.3 | 60.3 | 71.6 | 86.5 | 56.8 |
| Qwen2.5VL-72B | 84.8 | 90.8 | 80.9 | 79.4 | 88.8 | 70.0 | 76.3 | 84.3 | 68.3 |
| **Visually Grounded Reasoning Models** |  |  |  |  |  |  |  |  |  |
| <span style="color:gray">PixelReasoner</span> [@su2025pixelreasoner] | 80.6 | 83.5 | 76.3 | 72.9 | 86.0 | 60.3 | 66.9 | 80.0 | 54.3 |
| <span style="color:gray">DeepEyes</span> [@zheng2025deepeyes] | **90.0** | **92.1** | **86.8** | **75.1** | **91.3** | 59.0 | **72.6** | **86.8** | **58.5** |
| <span style="color:gray">Thyme-VL</span> [@zhang2025thyme] | 82.2 | 83.5 | 80.3 | **77.0** | **91.0** | **63.0** | 72.0 | 86.5 | **57.5** |
| <span style="color:gray">TreeVGR</span>$^\dagger$ [@wang2025traceable] | 85.9 | 86.1 | **85.5** | 72.7 | 89.5 | **61.5** | 69.8 | 84.4 | 57.2 |
| ZoomRefine$^\dagger$ [@yu2025zoom] | 82.2 | 85.3 | 77.6 | 71.5 | 88.5 | 55.3 | 68.6 | 83.9 | 54.0 |
| Dyfo$^\dagger$ [@li2025dyfo] | 84.3 | 82.6 | **86.8** | 71.3 | 89.2 | 53.5 | 69.8 | 86.5 | 53.2 |
| **DeepScan** | **90.6** | **93.0** | **86.8** | **75.0** | 90.1 | 59.7 | **72.4** | **87.2** | **57.6** |
| vs Qwen2.5-VL-7B | ↑16 | ↑16 | ↑17 | ↑2.8 | ↑1.3 | ↑4.2 | ↑3.6 | ↑3.7 | ↑3.6 |

## Table 2

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table2.png)

**Caption:** Comparison with state-of-the-art alternatives on TreeBench [@wang2025traceable]. All the baselines are developed from Qwen2.5-VL-7B, and the RL-based methods are marked by <span style="color:gray">gray</span>. Results$^\dagger$ are self-collected. **DeepScan** *achieves competitive results compared to SOTAs.*

**Caption[CN]:** 与 TreeBench [@wang2025traceable] 上最先进替代方法的比较。所有基线均基于 Qwen2.5-VL-7B 开发，基于 RL 的方法以<span style="color:gray">灰色</span>标记。带 $^\dagger$ 的结果由作者自行收集。**DeepScan** *取得了可与 SOTA 竞争的结果。*

| Model | Overall | mIoU | Perception: Attributes | Perception: Material | Perception: Phy. State | Perception: Obj. Retr. | Perception: OCR | Reasoning: Per. Trans. | Reasoning: Ordering | Reasoning: Con. & Oc. | Reasoning: Spa. Cont. | Reasoning: Comparison |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **General Large Vision-Language Models** |  |  |  |  |  |  |  |  |  |  |  |  |
| Gemini-2.5-Flash-0520 [@gemini-2.5-flash] | 45.9 | -- | 48.3 | 53.9 | 69.6 | 68.8 | 75.0 | 15.3 | 19.3 | 56.1 | 72.4 | 43.2 |
| GPT-4o-1120 [@gpt4o] | 46.9 | -- | 51.7 | 61.5 | 65.2 | 43.8 | 69.1 | 18.8 | 38.6 | 48.8 | 72.4 | 43.2 |
| Gemini-2.5-Pro-0605 [@gemini-2.5-pro] | 54.1 | -- | 51.7 | 61.5 | 56.5 | 75.0 | 83.8 | 20.0 | 36.8 | 65.9 | 86.2 | 54.6 |
| GPT-o3-0416 [@o3] | 54.8 | -- | 69.0 | 69.2 | 65.2 | 68.8 | 79.4 | 22.4 | 38.6 | 61.0 | 86.2 | 50.0 |
| LLaVA-OneVision-7B [@li2024llavaov] | 37.3 | -- | 55.2 | 53.8 | 56.5 | 50.0 | 32.4 | 21.2 | 22.8 | 41.5 | 72.4 | 36.4 |
| LLaVA-OneVision-72B | 40.5 | -- | 62.1 | 53.8 | 65.2 | 62.3 | 36.8 | 12.9 | 28.1 | 53.7 | 65.5 | 47.7 |
| Qwen2.5-VL-7B [@bai2025qwen25vl] | 37.0 | -- | 55.2 | 53.8 | 56.5 | 62.5 | 27.9 | 20.0 | 35.1 | 39.0 | 44.8 | 43.2 |
| Qwen2.5-VL-32B | 42.5 | -- | 51.7 | 53.8 | 69.6 | 62.5 | 54.4 | 16.5 | 33.3 | 46.3 | 62.1 | 38.6 |
| Qwen2.5-VL-72B | 42.2 | -- | 65.5 | 69.2 | 56.5 | 56.3 | 48.5 | 11.8 | 33.3 | 51.2 | 72.4 | 38.6 |
| InternVL3-8B [@zhu2025internvl3] | 38.8 | -- | 51.7 | 69.2 | 56.5 | 56.3 | 33.7 | 21.2 | 24.6 | 39.0 | 72.4 | 43.2 |
| InternVL3-38B | 42.0 | -- | 51.7 | 61.5 | 52.2 | 68.8 | 51.5 | 12.9 | 33.3 | 56.1 | 65.5 | 38.6 |
| InternVL3-78B | 46.4 | -- | 62.1 | 61.5 | 52.2 | 68.8 | 52.9 | 16.5 | 33.3 | 61.0 | 86.2 | 45.5 |
| **Visually Grounded Reasoning Models** |  |  |  |  |  |  |  |  |  |  |  |  |
| <span style="color:gray">DeepEyes</span> [@zheng2025deepeyes] | 37.5 | 30.0 | **62.1** | 53.8 | **65.2** | **68.8** | **51.5** | 11.8 | 24.6 | 36.6 | **51.7** | **47.7** |
| <span style="color:gray">Pixel-Reasoner</span> [@su2025pixelreasoner] | 39.0 | **35.7** | **58.6** | **61.5** | **65.2** | 50.0 | 48.5 | 14.1 | 31.6 | 39.0 | 44.8 | 40.9 |
| <span style="color:gray">TreeVGR</span>$^\dagger$ [@wang2025traceable] | **41.0** | 31.8 | 55.2 | **61.5** | **65.2** | 50.0 | **61.7** | 15.3 | 24.6 | **46.3** | 44.8 | 40.9 |
| ZoomRefine$^\dagger$ [@yu2025zoom] | 38.0 | -- | 48.3 | **61.5** | 56.5 | **62.5** | 39.7 | **18.8** | 29.8 | **46.3** | 44.8 | 38.6 |
| Dyfo$^\dagger$ [@li2025dyfo] | 39.3 | -- | **58.6** | **69.2** | 56.5 | **62.5** | 35.3 | **21.2** | **35.1** | 41.5 | 44.8 | 40.9 |
| **DeepScan** | **42.5** | **37.3** | **62.1** | **69.2** | **60.9** | **68.8** | 44.1 | **21.2** | **36.8** | **43.9** | **48.3** | **43.2** |
| $\Delta$ vs Qwen2.5-VL-7B | ↑5.5 | -- | ↑6.9 | ↑15.4 | ↑4.4 | ↑6.3 | ↑16.2 | ↑1.2 | ↑1.7 | ↑4.9 | ↑3.5 | $\pm0.0$ |

# 4. Experiments / 实验

## 4.1 Experimental Settings / 实验设置

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Datasets & Evaluation Metrics.** **V* Bench** contains 191 images with an average resolution of $2246\times1582$ and emphasizes very small targets (mean area $< 0.05\%$). It covers two tasks: *Direct Attribute* recognition (*Att*, 115 samples) and *Spatial Relationship* reasoning (*Spa*, 76 samples). We report multiple-choice accuracy. **HR-Bench** is available at two resolutions (8K/4K). Each version contains 200 images, split evenly into *Single-Instance Perception* (*Sin*, 100 samples) and *Cross-Instance Perception* (*Cro*, 100 samples). We evaluate using multiple-choice accuracy with a cyclic-permutation protocol. **TreeBench** [@wang2025traceable] is designed to assess “*thinking-with-images*” capabilities via three principles: localization of traceable evidence, perception of subtle targets, and second-order reasoning. It provides 405 images with an average resolution of $2152\times1615$ and reports both multiple-choice accuracy and localization quality (mIoU).

> <span style="color:#3B82F6"><strong>Para. 1[CN]:</strong></span> **数据集与评估指标。****V* Bench** 包含 191 幅图像，平均分辨率为 $2246\times1582$，重点关注极小目标（平均面积 $< 0.05\%$）。它涵盖两项任务：*直接属性*识别（*Att*，115 个样本）和*空间关系*推理（*Spa*，76 个样本）。我们报告多项选择准确率。**HR-Bench** 提供两种分辨率版本（8K/4K）。每个版本包含 200 幅图像，均分为*单实例感知*（*Sin*，100 个样本）和*跨实例感知*（*Cro*，100 个样本）。我们采用循环置换协议评估多项选择准确率。**TreeBench** [@wang2025traceable] 通过三项原则评估“*用图像思考*”能力：可追溯证据的定位、细微目标的感知以及二阶推理。它提供 405 幅图像，平均分辨率为 $2152\times1615$，同时报告多项选择准确率与定位质量（mIoU）。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Baseline Methods.** We compare DeepScan with RL-based methods [@su2025pixelreasoner; @zheng2025deepeyes; @wang2025traceable; @zhang2025thyme], training-free methods [@yu2025zoom; @li2025dyfo], private models [@o3; @gpt4o; @gemini-2.5-pro; @gemini-2.5-flash], and open-source general models [@li2024llavaov; @bai2025qwen25vl; @zhu2025internvl3]. Further details are provided in the supplementary material.

> <span style="color:#3B82F6"><strong>Para. 2[CN]:</strong></span> **基线方法。**我们将 DeepScan 与基于 RL 的方法 [@su2025pixelreasoner; @zheng2025deepeyes; @wang2025traceable; @zhang2025thyme]、无需训练的方法 [@yu2025zoom; @li2025dyfo]、闭源模型 [@o3; @gpt4o; @gemini-2.5-pro; @gemini-2.5-flash] 以及开源通用模型 [@li2024llavaov; @bai2025qwen25vl; @zhu2025internvl3] 进行比较。更多细节见补充材料。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Implementation Details.** We adopt BLIP-ITM base [@li2022blip; @li-etal-2023-lavis] as the search expert and LangSAM [@medeiros2024language] as the visual expert. To balance performance and latency, we set $k=10$ in practice. We evaluate DeepScan with 5 LVLMs: LLaVA-1.5-7B, Qwen2-VL-7B, and Qwen2.5-VL-7B / 32B / 72B. We query the LVLM to classify the question type (detailed in the supplementary material) and dynamically set the patch size to $576\times576$ for single-object and $768\times768$ for multi-object scenarios. All the hyperparameters are listed in the supplementary material. All experiments were performed on $4\times$ NVIDIA L20 GPUs.

> <span style="color:#3B82F6"><strong>Para. 3[CN]:</strong></span> **实现细节。**我们采用 BLIP-ITM base [@li2022blip; @li-etal-2023-lavis] 作为搜索专家，采用 LangSAM [@medeiros2024language] 作为视觉专家。为平衡性能与时延，实践中我们将 $k$ 设为 $10$。我们使用 5 个 LVLM 评估 DeepScan：LLaVA-1.5-7B、Qwen2-VL-7B，以及 Qwen2.5-VL-7B / 32B / 72B。我们查询 LVLM 以对问题类型进行分类（详见补充材料），并将单对象场景的图块大小动态设为 $576\times576$，将多对象场景的图块大小动态设为 $768\times768$。所有超参数均列于补充材料中。全部实验均在 $4\times$ NVIDIA L20 GPU 上完成。

## 4.2 Main Results / 主要结果

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Fine-grained Visual Understanding.** As shown in Table 1, DeepScan delivers substantial gains over vanilla Qwen2.5-VL-7B across all benchmarks, e.g., 16.3% overall improvement on V*. Compared with the popular general LVLMs, DeepScan attains state-of-the-art performance. Noticeably, it even surpasses several 70B general models on perception tasks, such as the *Attribute* subset in V* Bench and the *Single* subset of HR-Bench, where evidence localization is crucial. Moreover, DeepScan consistently outperforms *all the* training-free baselines, achieving 6.3%, 3.6%, and 2.6% overall gains over DyFo on V* Bench and HR-Bench-4K/8K. Benefiting from the well-designed grounding pipeline, DeepScan remains competitive with leading RL-based methods, e.g., DeepEyes, *without additional fine-tuning* of the LVLM, especially on perception tasks.

> <span style="color:#3B82F6"><strong>Para. 4[CN]:</strong></span> **细粒度视觉理解。**如表 1 所示，在所有基准上，DeepScan 相比原始 Qwen2.5-VL-7B 均带来显著增益，例如在 V* 上总体提升 16.3%。与流行的通用 LVLM 相比，DeepScan 达到了最先进性能。值得注意的是，在证据定位至关重要的感知任务上，例如 V* Bench 的 *Attribute* 子集和 HR-Bench 的 *Single* 子集，它甚至超过了若干 70B 通用模型。此外，DeepScan 始终优于*所有*无需训练的基线；相较 DyFo，它在 V* Bench、HR-Bench-4K 和 HR-Bench-8K 上分别取得 6.3%、3.6% 和 2.6% 的总体增益。得益于精心设计的定位流程，DeepScan 在*无需对 LVLM 进行额外微调*的情况下仍可与 DeepEyes 等领先的 RL 方法竞争，尤其是在感知任务上。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **General Visual Tasks.** In general, RL-based and training-free methods are comparable, as reported in Table 2. Specifically, RL-based approaches have clear advantages on complex perception tasks (e.g., Physical State, OCR, *etc.*), whereas on second-order reasoning tasks (e.g., Perspective Transform, Ordering, *etc.*) they deliver trivial gains. We hypothesize that RL does not fundamentally strengthen LVLMs in visual reasoning; rather, it biases LVLMs toward perception behaviors. Furthermore, DeepScan shows strong perception ability, exceeding the RL-based DeepEyes, Pixel-Reasoner, and TreeVGR by 7.3, 1.6, and 5.5 mIoU, respectively, revealing the superiority of Hierarchical Scanning. Based on this, DeepScan attains the best overall results among not only training-free but also RL-based baselines, outperforming DeepEyes, Pixel-Reasoner, and TreeVGR by 5.0%, 3.5%, and 1.5% without fine-tuning.

> <span style="color:#3B82F6"><strong>Para. 5[CN]:</strong></span> **通用视觉任务。**总体而言，如表 2 所示，基于 RL 的方法与无需训练的方法表现相当。具体而言，基于 RL 的方法在复杂感知任务（例如 Physical State、OCR 等）上具有明显优势，而在二阶推理任务（例如 Perspective Transform、Ordering 等）上仅带来微小增益。我们推测，RL 并未从根本上增强 LVLM 的视觉推理能力；相反，它使 LVLM 偏向感知行为。此外，DeepScan 表现出强大的感知能力，其 mIoU 分别比基于 RL 的 DeepEyes、Pixel-Reasoner 和 TreeVGR 高出 7.3、1.6 和 5.5，体现了分层扫描的优越性。在此基础上，DeepScan 不仅在无需训练的基线中，而且在基于 RL 的基线中也取得了最佳总体结果；无需微调，它便分别超过 DeepEyes、Pixel-Reasoner 和 TreeVGR 5.0%、3.5% 和 1.5%。

## Figure 8

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig7.png)

**Caption:** Ablations of DeepScan across LVLMs on V*, where the $y$-axis shows average performance (%), the $x$-axis reports latency (s), and the shadow shows performance deviation across subsets.

**Caption[CN]:** DeepScan 在不同 LVLM 上针对 V* 的消融，其中 $y$ 轴表示平均性能（%），$x$ 轴表示时延（s），阴影表示不同子集之间的性能偏差。

## 4.3 Ablation Study / 消融研究

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Framework.** We conduct ablations of the DeepScan framework in two aspects: its components and overall pipelines.

> <span style="color:#3B82F6"><strong>Para. 6[CN]:</strong></span> **框架。**我们从两个方面对 DeepScan 框架进行消融：其组件与整体流程。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> ♦ *Components.* As presented in Figure 8, DeepScan consistently improves diverse LVLMs across architectures and parameter scales without adaptation cost, demonstrating its strong generalization. Besides, Table 3 shows that the experts of different sizes deliver similar performance and exhibit comparable memory footprint and latency, indicating that DeepScan is insensitive to the expert scale.

> <span style="color:#3B82F6"><strong>Para. 7[CN]:</strong></span> ♦ *组件。*如图 8 所示，无需适配成本，DeepScan 即可持续提升不同架构和参数规模的多种 LVLM，体现出很强的泛化能力。此外，表 3 表明，不同规模的专家带来相近的性能，并具有相当的内存占用和时延，这说明 DeepScan 对专家规模不敏感。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> ♦ *Pipelines.* As illustrated in Figure 8, all stages contribute to the improvement. Specifically, Hierarchical Scanning is the primary driver; Refocusing adds further gains while maintaining a favorable performance–latency trade-off. Building on them, Evidence-Enhanced Reasoning delivers additional improvements with negligible overhead. This demonstrates the completeness of the DeepScan framework.

> <span style="color:#3B82F6"><strong>Para. 8[CN]:</strong></span> ♦ *流程。*如图 8 所示，所有阶段都对性能提升作出了贡献。具体而言，分层扫描是主要驱动力；重新聚焦在保持良好性能—时延权衡的同时带来进一步增益。在二者基础上，证据增强推理以可忽略的开销取得额外提升。这证明了 DeepScan 框架的完整性。

### Table 3

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table3.png)

**Caption:** Ablation of external experts on V*; Mem denotes the memory footprint of each DeepScan variant in gigabytes (G). Time reports the average per-sample inference latency in seconds (s).

**Caption[CN]:** V* 上外部专家的消融；Mem 表示每种 DeepScan 变体的内存占用，单位为千兆字节（G）。Time 表示每个样本的平均推理时延，单位为秒（s）。

| Expert | Scale | Overall | Attribute | Spatial | Mem (↓) | Time (↓) |
|---|---|---:|---:|---:|---:|---:|
| BLIP-ITM | base | **90.6** | **93.0** | 86.8 | 29.4G | 24.5s |
| BLIP-ITM | large | 90.1 | 92.2 | **86.8** | 32.8G | 25.8s |
| LangSAM | small | 89.5 | **93.0** | 84.2 | 31.5G | 23.2s |
| LangSAM | base$^+$ | 89.5 | 91.3 | **86.8** | 31.9G | 24.0s |
| LangSAM | large | **90.6** | **93.0** | **86.8** | 32.8G | 24.5s |

### Table 4

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table4.png)

**Caption:** Ablation of Hierarchical Scanning on V*.

**Caption[CN]:** V* 上分层扫描的消融。

| Method | Overall | Attribute | Spatial | Time (↓) |
|---|---:|---:|---:|---:|
| Detection [@li2025dyfo] | 82.2 | 81.7 | 82.9 | 13.0s |
| Hierarchical Scanning | **90.6** | **93.0** | **86.8** | 24.5s |
| $w/o$ Post-Processing | 87.4 | 89.6 | 85.5 | 32.1s |

### Table 5

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table5.png)

**Caption:** Ablation of the Local Cue Exploration on V*. *left*: proxy type, where S and T denote semantic and topological information. *right*: patch size, where S / M denotes single-/multi-object scenes.

**Caption[CN]:** V* 上局部线索探索的消融。*左*：代理类型，其中 S 和 T 分别表示语义信息与拓扑信息。*右*：图块大小，其中 S / M 表示单对象/多对象场景。

**Left / 左：Proxy type / 代理类型**

| Proxy | S | T | Att | Spa |
|---|:---:|:---:|---:|---:|
| Centroid |  | ✓ | 84.3 | 80.3 |
| Chebyshev Center |  | ✓ | **91.3** | 82.9 |
| Attention Peak | ✓ |  | 87.8 | **85.5** |
| **Ours** | ✓ | ✓ | **93.0** | **86.8** |

**Right / 右：Patch size / 图块大小**

| *S* / *M* | Avg | Att | Spa |
|---|---:|---:|---:|
| 384 | 87.4 | 90.4 | 82.9 |
| 576 | 90.1 | **94.0** | 84.2 |
| 768 | 88.5 | 88.7 | **88.2** |
| 576 / 768 | **90.6** | 93.0 | 86.8 |

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **Hierarchical Scanning.** As shown in Table 4, compared with the detection-based grounding method applied in Dyfo [@li2025dyfo], Hierarchical Scanning delivers obvious overall gains, with particularly large improvements on the *Attribute* subset.

> <span style="color:#3B82F6"><strong>Para. 9[CN]:</strong></span> **分层扫描。**如表 4 所示，与 Dyfo [@li2025dyfo] 中采用的基于检测的定位方法相比，分层扫描带来了明显的总体增益，在 *Attribute* 子集上的提升尤其显著。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> ♦ *Morphological Post-Processing.* As shown in Table 4, it fills interior holes in evidence masks; thus, it not only yields clear performance gains but markedly accelerates inference by preventing repeated processing of the same evidence.

> <span style="color:#3B82F6"><strong>Para. 10[CN]:</strong></span> ♦ *形态学后处理。*如表 4 所示，它可以填补证据掩码内部的孔洞；因此，它不仅带来了明显的性能增益，还通过避免重复处理同一证据显著加速了推理。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> ♦ *Evidence Proxy.* As shown in Table 5 (*left*), centroid-based proxies can fall outside U-shaped cues, which compromises evidence recovery and degrades the overall performance. In contrast, attention peak and Chebyshev center provide complementary performance gains across scenes, while our design in Equation (5) fuses them and yields noticeably better results.

> <span style="color:#3B82F6"><strong>Para. 11[CN]:</strong></span> ♦ *证据代理。*如表 5（*左*）所示，基于质心的代理可能落在 U 形线索之外，这会损害证据恢复并降低总体性能。相比之下，注意力峰值与切比雪夫中心在不同场景中提供了互补的性能增益，而公式 (5) 中的设计将二者融合，取得了明显更好的结果。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> ♦ *Patch Size.* As reported in Table 5 (*right*), smaller patches are more effective at suppressing context and yield better performance in single-object scenes, while larger patches are preferred in multi-object scenes because context provides valuable spatial relations. Accordingly, we condition patch size on the scene type to enhance overall performance.

> <span style="color:#3B82F6"><strong>Para. 12[CN]:</strong></span> ♦ *图块大小。*如表 5（*右*）所示，较小图块在抑制上下文方面更加有效，并在单对象场景中表现更好；而在多对象场景中，更大的图块更受青睐，因为上下文提供了有价值的空间关系。因此，我们以场景类型为条件设定图块大小，以提升总体性能。

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> **Refocusing.** We conduct ablations of refocusing in three aspects: action set, search-space design, and zoom-out scale.

> <span style="color:#3B82F6"><strong>Para. 13[CN]:</strong></span> **重新聚焦。**我们从三个方面对重新聚焦进行消融：动作集合、搜索空间设计和缩小尺度。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> ♦ *Action Set.* Table 6 (*left*) shows that both actions are indispensable: removing either action degrades performance, whereas using them jointly yields consistent gains.

> <span style="color:#3B82F6"><strong>Para. 14[CN]:</strong></span> ♦ *动作集合。*表 6（*左*）表明，两个动作都不可或缺：移除任一动作都会降低性能，而联合使用二者则会带来一致增益。

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> ♦ *Search Space Design.* We evaluate both search efficiency and search space completeness using *search length*, defined as the mean number of expansions required to first reach the oracle-optimal state. In ablation, MCTS and A* enumerate all depth-2 reachable states and score each using Equation (11), whereas *Refocusing* visits only the states in $\mathcal{V}$. As shown in Table 6 (*right*), under the same expansion budget, *Refocusing* exhibits a shorter search length, empirically supporting our design principles and indicating both the completeness of the search space and the efficiency of the selection policy.

> <span style="color:#3B82F6"><strong>Para. 15[CN]:</strong></span> ♦ *搜索空间设计。*我们使用*搜索长度*同时评估搜索效率与搜索空间完备性；搜索长度被定义为首次到达预言机最优状态所需扩展次数的均值。在消融中，MCTS 和 A* 枚举所有深度为 2 的可达状态，并使用公式 (11) 对每个状态评分，而*重新聚焦*只访问 $\mathcal{V}$ 中的状态。如表 6（*右*）所示，在相同扩展预算下，*重新聚焦*的搜索长度更短；这从经验上支持了我们的设计原则，同时表明了搜索空间的完备性和选择策略的高效性。

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> ♦ *Scale of Zoom-Out.* Figure 9 shows that a moderate *Zoom-Out* recalibrates evidence, i.e., higher Hit@1, and increases DeepScan accuracy, while overly large *Zoom-Outs* bring excessive context and impair both grounding and reasoning. DeepScan shows greater tolerance to *Zoom-Out* in *Direct Attributes*, which is attributed to their smaller initial views.

> <span style="color:#3B82F6"><strong>Para. 16[CN]:</strong></span> ♦ *缩小尺度。*图 9 表明，适度的*缩小*可以重新校准证据，即获得更高的 Hit@1，并提高 DeepScan 的准确率；而过大的*缩小*会引入过多上下文，同时损害定位和推理。DeepScan 在*直接属性*任务上对*缩小*表现出更高的容忍度，这归因于其初始视图更小。

### Figure 9

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig8.png)

**Caption:** Ablation of the *Zoom-Out* scale on V*, where the left y-axis shows Hit@1 of evidence detection on the zoomed-out view, while the right y-axis shows the accuracy (Acc) of DeepScan.

**Caption[CN]:** V* 上*缩小*尺度的消融，其中左侧 y 轴表示缩小后视图上证据检测的 Hit@1，右侧 y 轴表示 DeepScan 的准确率（Acc）。

### Table 6

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table6.png)

**Caption:** *Left*: effects of each action; *Right*: comparison of search length with different search methods and search space design.

**Caption[CN]:***左*：各动作的影响；*右*：不同搜索方法和搜索空间设计的搜索长度比较。

**Left / 左：Effects of each action / 各动作的影响**

| In | Out | Att | Spa |
|:---:|:---:|---:|---:|
| ✓ |  | 89.6 | 73.7 |
|  | ✓ | 87.8 | 72.4 |
| ✓ | ✓ | **93.0** | **86.8** |

**Right / 右：Search length / 搜索长度**

| Method | State | Length (↓) | Budget |
|---|---:|---:|---:|
| MCTS | 7 | 2.24 | 4 |
| A* | 7 | 3.07 | 4 |
| **Ours** | 4 | **1.87** | 4 |

## 4.4 In-depth Analysis / 深入分析

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> **Case Study.** Figure 10 presents case studies from V* Bench and TreeBench. Specifically, GPT-4o and DyFo easily suffer from attention drift, leading to mislocalization and incorrect answers; in contrast, DeepScan accurately localizes evidence and produces interpretable answers (Figure 10a, c). Furthermore, DeepScan precisely grounds ultra-subtle evidence (area ratio $<1‰$) and generates correct answers, demonstrating the effectiveness of Hierarchical Scanning (Figure 10b, d). TreeBench typically involves long queries and complex visual reasoning. Despite this, DeepScan consistently identifies evidence and enhances LVLMs via visually grounded reasoning, revealing its robustness (Figure 10c, d).

> <span style="color:#3B82F6"><strong>Para. 17[CN]:</strong></span> **案例研究。**图 10 展示了来自 V* Bench 和 TreeBench 的案例研究。具体而言，GPT-4o 和 DyFo 很容易受到注意力漂移的影响，从而导致错误定位和错误答案；相比之下，DeepScan 能准确定位证据并生成可解释的答案（图 10a、c）。此外，DeepScan 能够精确定位极其细微的证据（面积占比 $<1‰$）并生成正确答案，证明了分层扫描的有效性（图 10b、d）。TreeBench 通常涉及较长的查询和复杂的视觉推理。即便如此，DeepScan 仍能持续识别证据，并通过视觉依据推理增强 LVLM，体现出其鲁棒性（图 10c、d）。

### Figure 10

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig9.png)

**Caption:** Case study of grounding results and model responses of GPT-4o, DyFo, and the proposed DeepScan. Panels (a–b) are from V* Bench; panels (c–d) are from TreeBench. Correct and incorrect responses are highlighted in **blue** and **red** text, respectively. GT, evidence searched by Dyfo, and evidence localized by DeepScan are marked in the image using *white*, *red*, and *blue* bboxes, respectively.

**Caption[CN]:** GPT-4o、DyFo 与所提出的 DeepScan 的定位结果及模型响应案例研究。面板 (a–b) 来自 V* Bench；面板 (c–d) 来自 TreeBench。正确与错误响应分别用**蓝色**和**红色**文本突出显示。GT、Dyfo 搜索到的证据以及 DeepScan 定位的证据在图像中分别使用*白色*、*红色*和*蓝色*边界框标记。

### Figure 11

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig10.png)

**Caption:** Qualitative analysis of the grounding paradigms with the attention map $S$ of the search expert.

**Caption[CN]:** 使用搜索专家的注意力图 $S$ 对定位范式进行定性分析。

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig14.png)

**Caption:** Qualitative analysis of the grounding paradigms with the attention map $S$ of the *search expert* in Figure 10 (a).

**Caption[CN]:** 使用图 10(a) 中*搜索专家*的注意力图 $S$ 对定位范式进行定性分析。

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> **Analysis of Grounding Paradigms.** The key insight of DeepScan is the *bottom-up* grounding paradigm. To further reveal its fundamental superiority, we design a *one-shot* variant of Hierarchical Scanning that performs *image-level* rather than *patch-wise* cue exploration, and provide qualitative and quantitative comparisons between the two variants.

> <span style="color:#3B82F6"><strong>Para. 18[CN]:</strong></span> **定位范式分析。**DeepScan 的关键洞见是*自底向上*的定位范式。为进一步揭示其根本优势，我们设计了分层扫描的一个*一次性*变体；该变体执行*图像级*而非*逐图块*线索探索，并对这两个变体进行定性和定量比较。

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> ♦ *Qualitative Analysis.* As shown in Figure 11, the one-shot variant exhibits errors similar to DyFo with distinct experts (GroundingDINO vs BLIP), where attention drifts toward the same object, “box sign.” This highlights the general impact of attention sink/drift on visual grounding. By contrast, the bottom-up variant suppresses the distractions and aligns attention with the correct target “cyclist's box,” revealing the fundamental advantage of the bottom-up paradigm.

> <span style="color:#3B82F6"><strong>Para. 19[CN]:</strong></span> ♦ *定性分析。*如图 11 所示，采用不同专家（GroundingDINO vs BLIP）的一次性变体与 DyFo 表现出相似错误：注意力都漂移到同一对象“box sign”。这凸显了注意力汇聚/漂移对视觉定位的普遍影响。相比之下，自底向上变体抑制了干扰，并使注意力与正确目标“cyclist's box”对齐，揭示了自底向上范式的根本优势。

### Table 7

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table7.png)

**Caption:** Quantitative analysis of the grounding paradigms on V*.

**Caption[CN]:** V* 上定位范式的定量分析。

| Grounding paradigm | Overall | Attribute | Spatial | Time (↓) |
|---|---:|---:|---:|---:|
| One-shot Localization | 83.8 | 83.5 | 84.2 | 20.4s |
| **Bottom-up Localization** | **90.6** | **93.0** | **86.8** | 24.5s |

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> ♦ *Quantitative Analysis.* As reported in Table 7, bottom-up localization clearly outperforms one-shot localization, particularly on fine-grained tasks. Moreover, the one-shot variant does not achieve a markedly higher inference speed than the bottom-up one. We attribute this to the proxy filtering in the evidence extraction, which keeps the LVLM judgment counts roughly comparable between the two paradigms.

> <span style="color:#3B82F6"><strong>Para. 20[CN]:</strong></span> ♦ *定量分析。*如表 7 所示，自底向上定位明显优于一次性定位，尤其是在细粒度任务上。此外，一次性变体并未获得显著高于自底向上变体的推理速度。我们将其归因于证据提取过程中的代理过滤：它使两种范式的 LVLM 判断次数大致相当。

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> **Impact of Grounding on LVLM Reasoning.** We study the reasoning performance in Qwen2.5-VL series under varying grounding precision, achieved by cropping the target with different sizes of surrounding context from the images on V*. As shown in Figure 12, we point out two key insights:

> <span style="color:#3B82F6"><strong>Para. 21[CN]:</strong></span> **定位对 LVLM 推理的影响。**我们研究了 Qwen2.5-VL 系列在不同定位精度下的推理表现；具体做法是在 V* 图像中裁剪目标，并保留不同大小的周边上下文。如图 12 所示，我们指出两个关键洞见：

> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> ♦ *More aggressive grounding is not always better.* Excessive zoom-in, e.g., IoU from $1/10$ to $1$, can remove essential context and thus degrade LVLM reasoning. Consistent with this observation, our selection policy avoids naively favoring smaller crops: the state reward in Equation (11) pairs a size regularizer with LVLM feedback to discourage over-cropping.

> <span style="color:#3B82F6"><strong>Para. 22[CN]:</strong></span> ♦ *更激进的定位并不总是更好。*过度放大，例如使 IoU 从 $1/10$ 变为 $1$，可能移除必要上下文，进而损害 LVLM 推理。与这一观察一致，我们的选择策略避免简单地偏好更小的裁剪区域：公式 (11) 中的状态奖励将尺寸正则项与 LVLM 反馈结合，以抑制过度裁剪。

> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> ♦ *Scaling effect benefits second-order reasoning more significantly than perception.* Under precise grounding, perception performance converges across model scales, while spatial reasoning gaps remain. This observation suggests using a lightweight LVLM for evidence judgment, and reserving a large-scale LVLM for Evidence-Enhanced Reasoning, preserving performance yet reducing latency.

> <span style="color:#3B82F6"><strong>Para. 23[CN]:</strong></span> ♦ *规模扩展效应对二阶推理的助益比对感知更显著。*在精确定位条件下，不同模型规模的感知性能趋于一致，但空间推理差距依然存在。这一观察提示我们，可以使用轻量级 LVLM 进行证据判断，并将大规模 LVLM 留给证据增强推理，从而在保持性能的同时降低时延。

### Figure 12

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig11.png)

**Caption:** Performance of Qwen2.5-VL series with the varying grounding precision (measured by IoU) on V* Bench.

**Caption[CN]:** Qwen2.5-VL 系列在 V* Bench 上随定位精度（以 IoU 衡量）变化的性能。

# 5. Conclusion / 结论

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We present DeepScan, a training-free framework for visually grounded reasoning in LVLMs via explicit evidence localization, recalibration, and integration before answering. Leveraging bottom-up Hierarchical Scanning, DeepScan mitigates effects of noisy context and precisely localizes critical visual content. It further refines the evidence view via Refocusing, yielding more accurate and grounded answers. Experiments show that DeepScan delivers superior performance across diverse visual tasks and substantially improves various LVLMs spanning architectures and parameter scales. Comprehensive ablations and analyses provide additional insights for the LVLM community.

> <span style="color:#3B82F6"><strong>Para. 1[CN]:</strong></span> 我们提出 DeepScan：一个用于 LVLM 视觉依据推理的无需训练框架，它在作答前显式地定位、重新校准并整合证据。DeepScan 利用自底向上的分层扫描减轻噪声上下文的影响，并精确定位关键视觉内容。它还通过重新聚焦进一步细化证据视图，从而生成更准确、更有依据的答案。实验表明，DeepScan 在多种视觉任务上均取得优越性能，并显著提升了跨不同架构和参数规模的多种 LVLM。全面的消融与分析为 LVLM 社区提供了更多洞见。

# Acknowledgments / 致谢

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This work was supported by the National Natural Science Foundation of China (62176091) and the Natural Science Foundation of Chongqing (CSTB2024NSCQ-MSX0877).

> <span style="color:#3B82F6"><strong>Para. 1[CN]:</strong></span> 本工作得到国家自然科学基金（62176091）和重庆市自然科学基金（CSTB2024NSCQ-MSX0877）的资助。


## Supplementary Material / 补充材料

## Outline / 大纲

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span>
>
> - § A **Discussions** includes the *failure cases* of DeepScan, limitations and future work, and Broader Impacts, delivering valuable insights.
> - § B **Methodological Details** provides pseudocode, the exact prompts applied, and hyperparameter settings.
> - § C **Additional Results** conducts a comparison against strong baselines and reveals the state-of-the-art performance achieved by DeepScan on fine-grained tasks.
> - § D **Additional Cases** including the advantage of the *bottom-up* grounding paradigm and the Example Model Outputs

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span>
>
> - § A **讨论**包括 DeepScan 的*失败案例*、局限性与未来工作，以及更广泛影响，从而提供有价值的见解。
> - § B **方法细节**提供伪代码、所使用的确切提示词以及超参数设置。
> - § C **补充结果**将 DeepScan 与强基线进行比较，并揭示其在细粒度任务上达到的最先进性能。
> - § D **补充案例**包括*自底向上*定位范式的优势以及模型输出示例

## A. Discussions / 讨论

### Failure Cases / 失败案例

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Based on our analysis, DeepScan’s failures mainly fall into two categories.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 根据我们的分析，DeepScan 的失败主要分为两类。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> *(1) Grounding failure.* In direct-attribute recognition, when multiple visually similar objects remain within the evidence neighborhood, the experts may propose incorrect evidence and the LVLM may misjudge it, leading to an incorrect evidence localization; and thus the LVLM produces an incorrect answer based on wrong evidence (see Figure 11).

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> *（1）定位失败。*在直接属性识别中，当证据邻域内仍存在多个视觉上相似的物体时，专家可能提出错误证据，LVLM 也可能对其误判，从而导致错误的证据定位；因此，LVLM 会基于错误证据生成错误答案（见图 11）。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> *(2) Reasoning failure.* For spatial-relation reasoning with multiple pieces of evidence, DeepScan currently forms a merged evidence view via the minimal enclosing bounding box over all localized evidence. When the evidence is widely separated, this large crop introduces substantial inter-evidence noisy context that hampers reasoning; the issue is exacerbated when the merged view includes distracting content that conflicts with the correct answer (see Figure 12). This points to a promising direction: replace the minimal enclosing box with a generative composition that reassembles localized fine-grained evidence into a compact layout, suppressing inter-evidence context while preserving object attributes and spatial relations.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> *（2）推理失败。*对于涉及多条证据的空间关系推理，DeepScan 当前通过覆盖所有已定位证据的最小外接边界框来形成合并证据视图。当证据彼此相距较远时，这一大范围裁剪会引入大量证据间的噪声上下文，从而妨碍推理；当合并视图包含与正确答案相冲突的干扰内容时，该问题会进一步加剧（见图 12）。这指向一个很有前景的方向：用生成式组合替代最小外接框，将已定位的细粒度证据重新组装成紧凑布局，在保留物体属性和空间关系的同时抑制证据间上下文。

### Figure 11

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig12.png)

**Caption:** Case study of grounding failure

**Caption[CN]:** 定位失败案例研究

*Asset note / 资产说明：The TeX source references a figure asset, but this fragment intentionally does not invent or embed an asset path. / TeX 源文件引用了一个图像资产；本片段有意不虚构或嵌入资产路径。*

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span>
>
> The following literal labels, question, and model response are available in the source asset:
>
> ```text
> GT Evidence
> Q: "What is the color of the clock?
> (A) black (B) yellow (C) green (D) red
> Localized Object
> Answer: (D) red
> ```

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span>
>
> 源资产中可提取到以下逐字标签、问题和模型响应；其中文翻译为：
>
> ```text
> 真实证据
> 问：时钟是什么颜色？
> (A) 黑色 (B) 黄色 (C) 绿色 (D) 红色
> 已定位物体
> 答案：(D) 红色
> ```

### Figure 12

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig13.png)

**Caption:** Case study of reasoning failure

**Caption[CN]:** 推理失败案例研究

*Asset note / 资产说明：The TeX source references a figure asset, but this fragment intentionally does not invent or embed an asset path. / TeX 源文件引用了一个图像资产；本片段有意不虚构或嵌入资产路径。*

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span>
>
> The following literal labels, question, and model response are available in the source asset:
>
> ```text
> Fine-grained Evidence
> Coarse-grained Evidence
> Potentially affect to
> Localized Object 1
> Localized Object 2
> Localized Object 3
> Localized Object 4
> Spatially far
> Spatially Close
> Merged Evidence
> Q: Is the white truck on the left or
> right side of the red truck?
> (A) right (B) left
> Confusing View
> Answer: (B) left
> ```

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span>
>
> 源资产中可提取到以下逐字标签、问题和模型响应；其中文翻译为：
>
> ```text
> 细粒度证据
> 粗粒度证据
> 可能影响
> 已定位物体 1
> 已定位物体 2
> 已定位物体 3
> 已定位物体 4
> 空间上相距较远
> 空间上接近
> 合并证据
> 问：白色卡车位于红色卡车的左侧还是
> 右侧？
> (A) 右侧 (B) 左侧
> 混淆视图
> 答案：(B) 左侧
> ```

### Limitations / 局限性

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Compared with one-shot evidence-detection pipelines for visually grounded reasoning, DeepScan has higher inference latency. Nevertheless, as a test-time scaling paradigm, DeepScan offers a controllable performance-efficiency trade-off by tuning the patch size and the number of evidence proposals. In practice, its overall performance-efficiency profile remains acceptable relative to advanced visually grounded models (e.g., GPT-5), as detailed in § D.2 (Example Model Outputs). DeepScan's current implementation sets a relatively small patch size per image to capture fine-grained cues, which is unnecessary and inefficient for simple cases with salient evidence. In the future, we plan to develop an adaptive partition strategy that flexibly assigns a specific patch size within each grounding process based on stronger priors (e.g., evidence saliency), which is expected to further improve the performance-efficiency trade-off.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 与用于视觉定位推理的单次证据检测流水线相比，DeepScan 的推理延迟更高。然而，作为一种测试时扩展范式，DeepScan 可通过调节 patch 大小和候选证据数量，在性能与效率之间提供可控权衡。实践中，与先进的视觉定位模型（例如 GPT-5）相比，其总体性能—效率表现仍处于可接受范围，详见 § D.2（模型输出示例）。DeepScan 当前的实现为每幅图像设置相对较小的 patch 大小，以捕获细粒度线索；对于证据显著的简单案例，这既无必要，也效率低下。未来，我们计划开发一种自适应划分策略，依据更强的先验（例如证据显著性），在每次定位过程中灵活分配特定的 patch 大小，预计这将进一步改善性能—效率权衡。

### Broader Impacts / 更广泛影响

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> We propose DeepScan, a training-free visually grounded reasoning framework that replaces brittle one-shot localization with hierarchical scanning and refocusing. By tying answers to concrete visual evidence and making contextual extent explicit, DeepScan can benefit domains needing reliable, fine-grained perception under clutter and occlusion. Examples include GUI agents (anchoring actions to the correct widget, explaining clicks), embodied manipulation (grasping small parts), and autonomous driving (partially occluded signs). Potential risks include propagation of biases inherited from LVLMs and experts, and automation errors in safety-critical settings. Besides, as a test-time scaling paradigm, DeepScan introduces extra inference overhead, which may limit deployment in compute-constrained scenarios such as edge or mobile devices.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 我们提出 DeepScan，这是一种免训练的视觉定位推理框架，以分层扫描和重聚焦取代脆弱的单次定位。通过将答案与具体视觉证据绑定，并明确上下文范围，DeepScan 可惠及那些需要在杂乱和遮挡条件下实现可靠细粒度感知的领域。例如 GUI 智能体（将动作锚定到正确控件、解释点击）、具身操作（抓取小部件）以及自动驾驶（识别部分遮挡的标志）。潜在风险包括传播从 LVLM 和专家继承的偏差，以及在安全关键场景中产生自动化错误。此外，作为一种测试时扩展范式，DeepScan 会带来额外推理开销，这可能限制其在边缘设备或移动设备等计算受限场景中的部署。

### Exact Prompts / 精确提示词

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/prompts.png)

**Caption:** System prompt and three user prompts for evidence decomposition, evidence judgment, and view-completeness justification.

**Caption[CN]:** 系统提示词，以及用于证据分解、证据判断和视图完整性判断的三个用户提示词。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> **System Prompt**
>
> You are an advanced image understanding assistant. You will be given an image and a question about it.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **系统提示词**
>
> 你是一名高级图像理解助手。你将获得一幅图像以及一个与该图像有关的问题。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **User Prompt 1 (Evidence Decomposition)**
>
> Task: List objects mentioned in text in List format.  
> Input text: {question}  
> Action: What objects are mentioned in original  
> text? List separated by commas. For example, from “person with white trousers on the left or right side of the person in blue”, output “[“person with white trousers”, “person in blue”]”.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **用户提示词 1（证据分解）**
>
> 任务：以列表格式列出文本中提到的物体。  
> 输入文本：{question}  
> 操作：原始文本中提到了哪些物体？用逗号分隔列表。例如，对于“穿白色裤子的人位于穿蓝色衣服的人左侧还是右侧”，输出“[“穿白色裤子的人”, “穿蓝色衣服的人”]”。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> **User Prompt 2 (Evidence Judgment)**
>
> I will provide you an image and a **question**:  
> {question}, please firstly determine whether the image contains the clues for answering the question or not (answer with **Yes** or **No**); then give the evidence of your decision.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> **用户提示词 2（证据判断）**
>
> 我将向你提供一幅图像和一个**问题**：  
> {question}，请首先判断该图像是否包含回答此问题所需的线索（用 **Yes** 或 **No** 回答）；然后给出你作出该判断的证据。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> **User Prompt 3 (View Completeness Justification)**
>
> Question: Does the image fully contain every object in the list {target_list}? Please treat “fully contain” as entirely within the frame (not truncated by image boundaries). Please firstly answer the question with **Yes** or **No**; then give the evidence of your decision. For example, if yes, list the evidence of each object (e.g., object: bbox [x1, y1, x2, y2] or a clear region description); if no, list the missing objects by name.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> **用户提示词 3（视图完整性论证）**
>
> 问题：该图像是否完整包含列表 {target_list} 中的每一个物体？请将“完整包含”理解为完全位于画面之内（未被图像边界截断）。请首先用 **Yes** 或 **No** 回答问题；然后给出你作出该判断的证据。例如，如果回答为 yes，请列出每个物体的证据（例如，物体：bbox [x1, y1, x2, y2] 或清晰的区域描述）；如果回答为 no，请按名称列出缺失的物体。

### Algorithm 1

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/algorithm1.png)

**Caption:** Hierarchical Scanning *with* Acceleration

**Caption[CN]:** *带*加速的分层扫描

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span>
>
> **Require:** image $I \in \mathbb{R}^{H \times W \times 3}$, question $q$, patch size $\{l_s, l_c\}$, candidate count $k$, kernel $\mathcal{K}$, $\mathcal{S}_r$, threshold $\tau_{\mathrm{area}}$, $\theta_{\mathrm{IoU}}$  
> **Ensure:** Evidence set $\mathcal{E}=\{(b_i,e_i)\}$
>
> 1. $\mathcal{E}_{\rm all}\gets\emptyset,\quad \mathcal{E}\gets\emptyset$
> 2. $l \gets \textsc{SelectByLen}(\textsc{Lvlm}(\texttt{Prompt1}(q)), \{l_s,l_c\})$
> 3. **For each** patch $p$ in $\textsc{Partition}(I,l)$:
>    1. $S_p \gets \textsc{Search}(p,q)$
>    2. $S_p^+ \gets \mathbb{I}\big(S_p \ge \textsc{OTSU}(S_p)\big)$
>    3. **For each** $G \in \textsc{ConnComp}(S_p^+)$ with $|G|\ge\tau$:
>       1. $d_G(i,j)\gets\inf_{\gamma\in\partial G}\| (i,j)-\gamma\|_2,\ \forall (i,j)\in G$
>       2. $\tilde{S}_p \gets \textsc{Norm}(S_p),\quad \tilde d\gets\textsc{Norm}(d_G)$
>       3. $c^\star \gets \arg\max_{c\in G}\ \tilde S_p(c)\cdot \tilde d(c)$
>       4. $c'\gets\textsc{LiftToImage}(c^\star,p\rightarrow I),\quad \mathcal{C}_p' \cup \{c'\}$
> 4. **While** $\mathcal{C}_p'$ not empty:
>    1. $c \gets \operatorname{Pop}(\mathcal{C}_p),\quad m \gets \textsc{Segment}(I,c)$
>    2. $m^+ \gets (\,m \bullet \mathcal{K}\,) \ \oplus\ \mathcal{S}_r$
>    3. $b \gets \textsc{BBox}(m^+),\quad e \gets \textsc{Crop}(I,b)$
>    4. **If** $\mathrm{IoU}(b,b_i) \le \theta_{\rm IoU}$ for all $(b_i, e_i)\in\mathcal{E}_{\rm all}$:
>       1. $\mathcal{E}_{\rm all}\gets\mathcal{E}_{\rm all}\cup\{(b,e)\}$
>    5. $I \gets I \odot (\mathbf{1}-m^+),\quad \mathcal{C}_p'\gets \{c'\in\mathcal{C}_p'\mid m^+(c')=0\}$
> 5. $\mathcal{E}_k \gets \textsc{TakeKSmallestByArea}(\mathcal{E}_{\rm all},k)$
> 6. **For each** $(b,e)\in \mathcal{E}_k$:
>    1. **If** $\textsc{Lvlm}(e,\texttt{Prompt2}(q))=\texttt{Yes}$:
>       1. $\mathcal{E}\gets \mathcal{E}\cup\{(b,e)\}$
> 7. **Return** $\mathcal{E}$

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span>
>
> **输入要求：**图像 $I \in \mathbb{R}^{H \times W \times 3}$、问题 $q$、patch 大小 $\{l_s, l_c\}$、候选数量 $k$、核 $\mathcal{K}$、$\mathcal{S}_r$、阈值 $\tau_{\mathrm{area}}$、$\theta_{\mathrm{IoU}}$  
> **输出保证：**证据集合 $\mathcal{E}=\{(b_i,e_i)\}$
>
> 1. $\mathcal{E}_{\rm all}\gets\emptyset,\quad \mathcal{E}\gets\emptyset$
> 2. $l \gets \textsc{SelectByLen}(\textsc{Lvlm}(\texttt{Prompt1}(q)), \{l_s,l_c\})$
> 3. **对于** $\textsc{Partition}(I,l)$ 中的每个 patch $p$：
>    1. $S_p \gets \textsc{Search}(p,q)$
>    2. $S_p^+ \gets \mathbb{I}\big(S_p \ge \textsc{OTSU}(S_p)\big)$
>    3. **对于**满足 $|G|\ge\tau$ 的每个 $G \in \textsc{ConnComp}(S_p^+)$：
>       1. $d_G(i,j)\gets\inf_{\gamma\in\partial G}\| (i,j)-\gamma\|_2,\ \forall (i,j)\in G$
>       2. $\tilde{S}_p \gets \textsc{Norm}(S_p),\quad \tilde d\gets\textsc{Norm}(d_G)$
>       3. $c^\star \gets \arg\max_{c\in G}\ \tilde S_p(c)\cdot \tilde d(c)$
>       4. $c'\gets\textsc{LiftToImage}(c^\star,p\rightarrow I),\quad \mathcal{C}_p' \cup \{c'\}$
> 4. **当** $\mathcal{C}_p'$ 非空时：
>    1. $c \gets \operatorname{Pop}(\mathcal{C}_p),\quad m \gets \textsc{Segment}(I,c)$
>    2. $m^+ \gets (\,m \bullet \mathcal{K}\,) \ \oplus\ \mathcal{S}_r$
>    3. $b \gets \textsc{BBox}(m^+),\quad e \gets \textsc{Crop}(I,b)$
>    4. **如果**对于 $\mathcal{E}_{\rm all}$ 中所有 $(b_i, e_i)$，均有 $\mathrm{IoU}(b,b_i) \le \theta_{\rm IoU}$：
>       1. $\mathcal{E}_{\rm all}\gets\mathcal{E}_{\rm all}\cup\{(b,e)\}$
>    5. $I \gets I \odot (\mathbf{1}-m^+),\quad \mathcal{C}_p'\gets \{c'\in\mathcal{C}_p'\mid m^+(c')=0\}$
> 5. $\mathcal{E}_k \gets \textsc{TakeKSmallestByArea}(\mathcal{E}_{\rm all},k)$
> 6. **对于** $\mathcal{E}_k$ 中的每个 $(b,e)$：
>    1. **如果** $\textsc{Lvlm}(e,\texttt{Prompt2}(q))=\texttt{Yes}$：
>       1. $\mathcal{E}\gets\mathcal{E}\cup\{(b,e)\}$
> 7. **返回** $\mathcal{E}$

### Algorithm 2

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/algorithm2.png)

**Caption:** Refocusing

**Caption[CN]:** 重聚焦

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span>
>
> **Require:** image $I\in\mathbb{R}^{H\times W\times3}$, question $q$, target list $t$, evidence set $\mathcal{E}$  
> **Ensure:** refined view $V$
>
> 1. $\mathcal{R}\gets \emptyset,\quad b_{\rm m}\gets \bigcup_{(b,e)\in\mathcal{E}}b$
> 2. $e_{\rm m}\gets \operatorname{Crop}(I,\, b_{\rm m}),\quad V_1\gets e_m$
> 3. $V_2\gets \operatorname{In}(V_1,q),\quad V_3\gets \operatorname{Out}(V_1),\quad V_4\gets \operatorname{In}(V_3,q)$
> 4. **For** $V\in \{V_1, V_2, V_3, V_4\}$:
>    1. **If** $\operatorname{Lvlm}(V,\texttt{UserPrompt3}(t))=\texttt{Yes}$:
>       1. $h,w\gets \operatorname{Shape}(V)$
>       2. $R\gets HW/hw$
>    2. **Else**:
>       1. $R\gets 0$
>    3. $\mathcal{R}\gets\mathcal{R}\,\cup\,\{R\}$
> 5. $i^*\gets\argmax_{i\in\{1,2,3,4\}} \mathcal{R}(i)$
> 6. **Return** $V_{i^*}$

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span>
>
> **输入要求：**图像 $I\in\mathbb{R}^{H\times W\times3}$、问题 $q$、目标列表 $t$、证据集合 $\mathcal{E}$  
> **输出保证：**细化视图 $V$
>
> 1. $\mathcal{R}\gets \emptyset,\quad b_{\rm m}\gets \bigcup_{(b,e)\in\mathcal{E}}b$
> 2. $e_{\rm m}\gets \operatorname{Crop}(I,\, b_{\rm m}),\quad V_1\gets e_m$
> 3. $V_2\gets \operatorname{In}(V_1,q),\quad V_3\gets \operatorname{Out}(V_1),\quad V_4\gets \operatorname{In}(V_3,q)$
> 4. **对于** $V\in \{V_1, V_2, V_3, V_4\}$：
>    1. **如果** $\operatorname{Lvlm}(V,\texttt{UserPrompt3}(t))=\texttt{Yes}$：
>       1. $h,w\gets \operatorname{Shape}(V)$
>       2. $R\gets HW/hw$
>    2. **否则**：
>       1. $R\gets 0$
>    3. $\mathcal{R}\gets\mathcal{R}\,\cup\,\{R\}$
> 5. $i^*\gets\argmax_{i\in\{1,2,3,4\}} \mathcal{R}(i)$
> 6. **返回** $V_{i^*}$

## B. Methodological Details / 方法细节

### Prompts / 提示词

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We provide below the prompts involved in Section 3: (i) *Evidence Decomposition* (to set the patch size), (ii) *Evidence Judgment* in *Hierarchical Scanning*, and (iii) *View Completeness Justification* in *Refocusing*.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们在下方给出第 3 节涉及的提示词：（i）*证据分解*（用于设置 patch 大小），（ii）*分层扫描*中的*证据判断*，以及（iii）*重聚焦*中的*视图完整性论证*。

### Table 8

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table8.png)

**Caption:** Comparisons between the proposed DeepScan and existing visually grounded reasoning approaches. Like most test-time scaling paradigms, DeepScan is easier to scale up. Furthermore, DeepScan introduces hierarchical scanning and refocusing for a robust bottom-up evidence localization and recalibration and leverages hybrid granular evidence to enable LVLM to produce higher-quality answers.

**Caption[CN]:** 所提出的 DeepScan 与现有视觉定位推理方法之间的比较。与大多数测试时扩展范式一样，DeepScan 更容易扩展。此外，DeepScan 引入分层扫描和重聚焦，以实现稳健的自底向上证据定位与重新校准，并利用混合粒度证据，使 LVLM 能够生成更高质量的答案。

| Methods / 方法 | Venue / 发表场所 | Ease to Scaling / 易扩展 | External Experts / 外部专家 | Search Strategy / 搜索策略 | Grounding Paradigm / 定位范式 | Evidence Granularity / 证据粒度 | Inference Latency / 推理延迟 |
|---|---:|:---:|:---:|---|---|---|---|
| Seal `\cite{wu2024vstar}` | CVPR'24 | ✗ | ✗ | LLM-guided Search | Coarse-to-Fine | Fine | High |
| Dyfo `\cite{li2025dyfo}` | CVPR'25 | ✓ | ✓ | Detection + MCTS | Coarse-to-Fine | Coarse | High |
| DeepEyes `\cite{zheng2025deepeyes}` | NeurIPS'25 | ✗ | ✗ | Generative Bbox | Coarse-to-Fine | Fine | High |
| PixelReasoner `\cite{su2025pixelreasoner}` | NeurIPS'25 | ✗ | ✗ | Generative Bbox | Coarse-to-Fine | Coarse | High |
| ViGoRL `\cite{sarch2025grounded}` | NeurIPS'25 | ✗ | ✗ | Generative Bbox | Coarse-to-Fine | Fine | High |
| ZoomRefine `\cite{yu2025zoom}` | NeurIPS'25 | ✓ | ✗ | Generative Bbox | Coarse-to-Fine | Coarse | Medium |
| TreeVGR `\cite{wang2025traceable}` | Preprint, Jul | ✗ | ✗ | Generative Bbox | Implicit Search | NA | Low |
| Thyme-VL `\cite{zhang2025thyme}` | Preprint, Aug | ✗ | ✗ | Generative Code | Coarse-to-Fine | Coarse | High |
| DeepScan (Ours) | -- | ✓ | ✓ | Hierarchical Scanning + Refocusing | Bottom-up | Hybrid | High |

### Hyper-Parameters / 超参数

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In *Local Cue Exploration*, the area threshold for noisy-cue filtering is set to $50$ pixels. In *Multi-Scale Evidence Extraction*, morphological post-processing uses a $5{\times}5$ flat structuring element $\mathcal{K}$ and a disk $\mathcal{S}_r$ with radius $r{=}20$. The IoU threshold for filtering similar evidence is $\theta_{\rm IoU}{=}0.3$. We set $k{=}10$, i.e., retain only the 10 smallest pairs $(b,e)\in\mathcal{E}$ for acceleration. For *Refocusing*, to prevent undersized crops, we pad the visual expert's detections ($\mathcal{B}$) by $28$ pixels on all sides, and set the scaling factor to $s{=}1.5$. For *LVLM Querying*, the maximum output length is $50$ for *Evidence Decomposition*, *Evidence Judgment*, and *View Completeness Justification*, and $1024$ for *Evidence-Enhanced Reasoning*. During inference, we use temperature $t{=}0$ with a fixed random seed ($13$). Beam search and top-$k$ sampling are disabled by default.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在*局部线索探索*中，用于噪声线索过滤的面积阈值设为 $50$ 像素。在*多尺度证据提取*中，形态学后处理使用 $5{\times}5$ 的平坦结构元素 $\mathcal{K}$，以及半径为 $r{=}20$ 的圆盘 $\mathcal{S}_r$。用于过滤相似证据的 IoU 阈值为 $\theta_{\rm IoU}{=}0.3$。我们设置 $k{=}10$，即仅保留 $\mathcal{E}$ 中面积最小的 10 个 $(b,e)$ 对以实现加速。对于*重聚焦*，为防止裁剪区域过小，我们在视觉专家的检测框（$\mathcal{B}$）四周各填充 $28$ 像素，并将缩放因子设为 $s{=}1.5$。对于 *LVLM 查询*，*证据分解*、*证据判断*和*视图完整性论证*的最大输出长度为 $50$，*证据增强推理*的最大输出长度为 $1024$。推理期间，我们使用温度 $t{=}0$，并采用固定随机种子（$13$）。默认禁用束搜索和 top-$k$ 采样。

### Pseudocodes / 伪代码

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Algorithmic details for Hierarchical Scanning and Refocusing are provided in Algorithms 1 and 2. Here, the prompts `Prompt1`, `Prompt2`, and `Prompt3` are specified in the **Prompt** subsection, i.e., “User Prompt 1-3”; $\texttt{Prompt1}(x)$ denotes instantiating the prompt with the string $x$ via template-based substitution. In addition, $\textsc{LiftToImage}$ maps patch coordinates to the full-image coordinate system. $\textsc{Close}$ and $\textsc{Dilate}$ indicate morphological closing and dilation, respectively. The operator $\odot$ denotes element-wise multiplication.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 分层扫描与重聚焦的算法细节见算法 1 和算法 2。这里，提示词 `Prompt1`、`Prompt2` 和 `Prompt3` 在**提示词**小节中给出，即“用户提示词 1–3”；$\texttt{Prompt1}(x)$ 表示通过基于模板的替换，用字符串 $x$ 实例化该提示词。此外，$\textsc{LiftToImage}$ 将 patch 坐标映射到整幅图像的坐标系。$\textsc{Close}$ 和 $\textsc{Dilate}$ 分别表示形态学闭运算和膨胀。运算符 $\odot$ 表示逐元素乘法。

### Table 9

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table9.png)

**Caption:** Additional comparison results on V* Bench between our method with existing baselines. We produced the results$^\dagger$ with the provided official codes for fair comparisons.

**Caption[CN]:** 我们的方法与现有基线在 V* Bench 上的补充比较结果。为进行公平比较，我们使用所提供的官方代码生成了标有 $^\dagger$ 的结果。

| Method / 方法 | Overall / 总体 | Attribute / 属性 | Spatial / 空间 |
|---|---:|---:|---:|
| o3 | 95.0 | - | - |
| Seal | 74.8 | 76.3 | 75.4 |
| Dyfo-L | 62.7 | 53.9 | 59.2 |
| Dyfo-Q | 80.0 | 82.9 | 81.2 |
| Qwen2.5-VL-7B | 74.3 | 77.4 | 69.7 |
| PixelReasoner | 80.6 | 83.5 | 76.3 |
| Thyme-VL | 82.2 | 83.5 | 80.3 |
| ZoomRefine$^\dagger$ | 82.2 | 85.3 | 77.6 |
| Dyfo$^\dagger$ | 84.3 | 82.6 | 86.8 |
| TreeVGR$^\dagger$ | 85.9 | 86.1 | 85.5 |
| ViGoRL | 86.4 | - | - |
| DeepEyes | 90.0 | 92.1 | 86.8 |
| **DeepScan** ($k=10$) | 90.6 | 93.0 | 86.8 |
| **DeepScan** ($k=\infty$) | 91.1 | 93.9 | 86.8 |
| Qwen2.5-VL-72B | 84.8 | 90.8 | 80.9 |
| **DeepScan-72B** ($k=10$) | 93.7 | 93.9 | 93.4 |
| **DeepScan-72B** ($k=\infty$) | 94.2 | 94.8 | 93.4 |

### Figure 13

**Caption:** Qualitative analysis of the grounding paradigms with the attention map $S$ of the *search expert*

**Caption[CN]:** 使用*搜索专家*的注意力图 $S$ 对定位范式进行定性分析

*Asset note / 资产说明：The TeX source references a figure asset, but this fragment intentionally does not invent or embed an asset path. / TeX 源文件引用了一个图像资产；本片段有意不虚构或嵌入资产路径。*

## C. Additional Results / 补充结果

### Baselines / 基线

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> SEAL `\cite{wu2024vstar}`, PixelReasoner `\cite{su2025pixelreasoner}`, TreeVGR `\cite{wang2025traceable}`, DeepEyes `\cite{zheng2025deepeyes}`, ViGoRL `\cite{sarch2025grounded}`, and Thyme-VL `\cite{zhang2025thyme}` depend on learned localization modules or RL-based decision controllers for search. Upgrading these methods to a stronger LVLM typically requires retraining these components. In contrast, DyFo `\cite{li2025dyfo}` performs MCTS over focus actions with a visual expert, and ZoomRefine `\cite{yu2025zoom}` provides an unlearning variant that leverages LVLM prior for visually grounded reasoning through prompt engineering; both scale more readily across larger LVLM backbones. Our method is easier to scale up and introduces a novel bottom-up hierarchical scanning and refocusing for context-optimal views, complemented by a hybrid evidence memory, yielding better robustness than existing approaches.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> SEAL `\cite{wu2024vstar}`、PixelReasoner `\cite{su2025pixelreasoner}`、TreeVGR `\cite{wang2025traceable}`、DeepEyes `\cite{zheng2025deepeyes}`、ViGoRL `\cite{sarch2025grounded}` 和 Thyme-VL `\cite{zhang2025thyme}` 依赖已学习的定位模块或基于强化学习的搜索决策控制器。将这些方法升级到更强的 LVLM 通常需要重新训练这些组件。相比之下，DyFo `\cite{li2025dyfo}` 借助视觉专家对聚焦动作执行 MCTS，而 ZoomRefine `\cite{yu2025zoom}` 提供一种遗忘学习变体，通过提示工程利用 LVLM 先验进行视觉定位推理；二者都更容易扩展到更大的 LVLM 骨干。我们的方法更易扩展，并引入一种新颖的自底向上分层扫描和重聚焦，以获得上下文最优视图；再辅以混合证据记忆，从而比现有方法具有更强的鲁棒性。

### Performance Comparison / 性能比较

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> As shown in Table 9, **DeepScan** attains **90.6**% at $k{=}10$ and **91.1**% at $k{=}\infty$ based on Qwen2.5-VL-7B, which substantially outperforms both the training-free ZoomRefine$^\dagger$ (82.2%) and DyFo$^\dagger$ (84.3%) and even surpasses the RL-based DeepEyes (90.0%), ViGoRL (86.4%), TreeVGR (85.9%), Thyme-VL (82.2%), and PixelReasoner (80.6%) on the V* Benchmark. Specifically, on the *Attribute* subset, DeepScan reaches 93.0-93.9% while maintaining *Spatial* at 86.8%, indicating that bottom-up recovery plus refocusing preserves necessary context for reasoning. When scaling the LVLM backbone to 72B, **DeepScan-72B** achieves **94.2**% overall and 93.4% on the *Spatial* subset, a 9.4% gain over the Qwen2.5-VL-72B (84.8%). These results demonstrate DeepScan as a training-free framework that consistently improves diverse LVLMs and benefits from model scaling, with a controllable performance-latency trade-off via top-$k$ selection.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 如表 9 所示，基于 Qwen2.5-VL-7B 的 **DeepScan** 在 $k{=}10$ 时达到 **90.6**%，在 $k{=}\infty$ 时达到 **91.1**%；这不仅大幅优于免训练的 ZoomRefine$^\dagger$（82.2%）和 DyFo$^\dagger$（84.3%），甚至还在 V* Benchmark 上超过了基于强化学习的 DeepEyes（90.0%）、ViGoRL（86.4%）、TreeVGR（85.9%）、Thyme-VL（82.2%）和 PixelReasoner（80.6%）。具体而言，在*属性*子集上，DeepScan 达到 93.0-93.9%，同时将*空间*子集性能维持在 86.8%，这表明自底向上恢复加重聚焦能够保留推理所必需的上下文。当 LVLM 骨干扩展到 72B 时，**DeepScan-72B** 的总体性能达到 **94.2**%，在*空间*子集上达到 93.4%，相较 Qwen2.5-VL-72B（84.8%）提升 9.4%。这些结果表明，DeepScan 是一个免训练框架，能够持续改进多种 LVLM，并从模型扩展中受益；同时，还可通过 top-$k$ 选择对性能—延迟权衡进行控制。

### Table 10

![Source asset](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table10.png)

**Caption:** Performance--efficiency comparison on V* Benchmark. *End-to-End* Latency is the wall-clock time *per sample* from input to final output, *including all auxiliary steps* (e.g., Evidence Decompositions, Expert Calls, Post-Processing, Evidence Judgments).

**Caption[CN]:** V* Benchmark 上的性能—效率比较。*端到端*延迟是从输入到最终输出的*每个样本*墙钟时间，*包括所有辅助步骤*（例如证据分解、专家调用、后处理和证据判断）。

|  | Qwen2.5-VL 7B | DeepEyes | Zoom Refine | Dyfo | Hierarchical Scan | Refocus | DeepScan |
|---|---:|---:|---:|---:|---:|---:|---:|
| Accuracy (%) | 75.4 | 89.0 | 82.7 | 83.8 | 84.8 | 89.5 | 90.1 |
| Token Cost (k) | 3.5 | 13 | 5.1 | 7.2 | 6.5 | 8.1 | 8.4 |
| *End-to-End* Latency (s) | 0.4 | 6.9 | 0.9 | 2.4 | 2.2 | 3.0 | 3.1 |

### Engineering Optimization / 工程优化

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Our standard implementation of DeepScan relies on nested loops using the *Hugging face transformers backend* (as detailed in Algorithms 1 and 2). However, this implementation is severely bottlenecked by inefficient **sequential computation** during the Scanning and Refocusing stages. Furthermore, the frequent communication overhead between the visual expert and the LVLM leads to poor GPU utilization. Compounded by the *lack of modern primitives* in the standard **HF Transformers backend**, these factors result in substantial inference latency (as shown in Figure 8). To address this, we introduce a suite of engineering optimizations that exploit DeepScan's inherent algorithmic properties, significantly enhancing its viability for latency-sensitive applications. Specifically, unlike MCTS-based methods (e.g., Dyfo), DeepScan is built on *deterministic sampling*, enabling it to fully benefit from parallel acceleration via batching. Hence, we implemented batch processing for **(a)** attention map calculation, **(b)** top-$k$ candidate judgment, and **(c)** evidence view justification, and further parallelized post-processing routines to reduce tail latency. This strategy compresses many sequential interactions into a *single batched* search expert call and *three* LVLM forward passes *with extended context*, thus *substantially improving GPU utilization and reducing GPU idle time*. Moreover, we migrated to the *vLLM backend*, leveraging PagedAttention and optimized CUDA kernels. *Collectively, these standard engineering optimizations yield an **$\sim8\times$ speedup** over our previous implementation.*

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> DeepScan 的标准实现依赖使用 *Hugging face transformers backend* 的嵌套循环（详见算法 1 和算法 2）。然而，该实现在扫描与重聚焦阶段受到低效**顺序计算**的严重制约。此外，视觉专家与 LVLM 之间频繁的通信开销导致 GPU 利用率不佳。再加上标准 **HF Transformers backend** *缺乏现代原语*，这些因素造成了显著的推理延迟（如图 8 所示）。为解决这一问题，我们引入了一套利用 DeepScan 内在算法特性的工程优化，显著提升其对延迟敏感型应用的适用性。具体而言，与基于 MCTS 的方法（例如 Dyfo）不同，DeepScan 建立在*确定性采样*之上，因此能够通过批处理充分受益于并行加速。为此，我们对 **(a)** 注意力图计算、**(b)** top-$k$ 候选判断和 **(c)** 证据视图论证实施了批处理，并进一步并行化后处理程序以降低尾延迟。该策略将许多顺序交互压缩为*单次批处理*搜索专家调用，以及*三次带扩展上下文的* LVLM 前向传播，从而*显著提高 GPU 利用率并减少 GPU 空闲时间*。此外，我们迁移到了 *vLLM backend*，利用 PagedAttention 和优化后的 CUDA 核。*总的来说，这些标准工程优化相较我们之前的实现带来了 **$\sim8\times$ 加速**。*

### Performance-Latency Trade-off / 性能—延迟权衡

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Integrating the above optimizations, we re-evaluated DeepScan via *VLMEvalKit* (with vLLM backend) on 4$\times$L20 GPUs. As shown in Table 10, compared to *DeepEyes* that relies on multi-turn tool executions, DeepScan exhibits striking superiority. Specifically, DeepEyes suffers a severe 6.9s latency and 13k token cost, while DeepScan attains higher accuracy (90.1% *vs.* 89.0%) with $\sim$2.2$\times$ faster speed (3.1s) as well as $\sim$35% fewer tokens. This reveals that batched deterministic sampling effectively bypasses the sequential overhead of agentic paradigms, yielding superior reasoning with higher efficiency. Against the MCTS-based method *Dyfo*, DeepScan also offers a favorable trade-off. It incurs a marginal latency overhead (3.1s *vs.* 2.4s) but delivers a substantial $+6.3%$ accuracy gain. Notably, our *Hierarchical Scan* alone outperforms Dyfo (84.8% *vs.* 83.8%) with lower latency (2.2s).

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在整合上述优化后，我们通过 *VLMEvalKit*（使用 vLLM backend），在 4$\times$L20 GPU 上重新评估了 DeepScan。如表 10 所示，与依赖多轮工具执行的 *DeepEyes* 相比，DeepScan 展现出显著优势。具体而言，DeepEyes 的延迟高达 6.9s，token 成本为 13k；DeepScan 则以约快 $\sim$2.2$\times$ 的速度（3.1s）和少约 $\sim$35% 的 token，获得了更高准确率（90.1% *vs.* 89.0%）。这表明，批处理确定性采样有效绕过了智能体范式的顺序开销，以更高效率实现更优推理。与基于 MCTS 的方法 *Dyfo* 相比，DeepScan 也提供了有利的权衡。它仅带来很小的延迟开销（3.1s *vs.* 2.4s），却取得了显著的 $+6.3%$ 准确率提升。值得注意的是，仅使用我们的*分层扫描*就能以更低延迟（2.2s）超过 Dyfo（84.8% *vs.* 83.8%）。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> In fine-grained scenarios, the target occupies a minuscule fraction of the image, resulting in an inherently low signal-to-noise ratio (SNR) where the effective visual signal is overwhelmed by context noise. In these cases, search-based methods struggle to identify a reliable initial anchor, frequently causing exhaustive tree expansion to degenerate into an inefficient random walk. By slicing the image and evaluating patches via a single batched forward pass, our hierarchical scan explicitly isolates the target, drastically amplifying the local SNR. Coupled with the subsequent *Refocus*---which requires merely 0.8s but yields a massive $+4.7%$ performance leap---these results reveal a profound insight: systematically scaling compute to deterministically maximize visual SNR is fundamentally more efficient than heuristic search-tree expansion.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 在细粒度场景中，目标仅占图像极小的一部分，因而天然具有较低的信噪比（SNR），有效视觉信号会被上下文噪声淹没。在这些情况下，基于搜索的方法很难找到可靠的初始锚点，常使穷举式树扩展退化为低效的随机游走。通过切分图像并以单次批处理前向传播评估各个 patch，我们的分层扫描能够显式隔离目标，从而大幅提升局部 SNR。再结合后续的*重聚焦*——它仅需 0.8s，却带来高达 $+4.7%$ 的性能跃升——这些结果揭示了一个深刻见解：通过系统性扩展计算，以确定性方式最大化视觉 SNR，从根本上比启发式搜索树扩展更高效。

## D. Additional Visualization / 补充可视化

### D.1 Qualitative Analysis of Grounding Paradigm / 定位范式的定性分析

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> *Direct Attributes.* For attribute questions (e.g., helmet/slippers/candles color, dog breed), the *one-shot* variant tends to lock onto globally salient but irrelevant regions, a typical *attention sink/drift* failure, yielding mis-localization or missing the true fine-grained cue. By contrast, our *bottom-up* paradigm begins with local cue exploration and iteratively recenters the view on the true evidence, effectively “pulling” attention back to the correct object—consistent with the figure’s transitions from *Attention Sink* to *Align to* on attribute examples. This behavior aligns with the paper’s analysis that top-down, one-shot localization is fragile under noisy context, whereas bottom-up scanning suppresses distractions and aligns attention with the correct target.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> *直接属性。*对于属性问题（例如头盔/拖鞋/蜡烛的颜色、犬种），*单次*变体往往锁定全局显著但无关的区域，这是一种典型的*注意力沉降/漂移*失败，会导致错误定位或遗漏真正的细粒度线索。相比之下，我们的*自底向上*范式从局部线索探索开始，并迭代地将视图重新居中到真实证据上，有效地把注意力“拉回”正确物体——这与图中属性示例从 *Attention Sink* 到 *Align to* 的转变一致。这一行为也符合论文的分析：在噪声上下文下，自顶向下的单次定位十分脆弱，而自底向上扫描能够抑制干扰，并使注意力与正确目标对齐。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> *Spatial Relations.* Relation questions (e.g., left/right of motorcyclist vs. truck, sky wheel vs. rider, blue luggage vs. bus) require jointly grounding *two* targets. The one-shot variant often fixates on a single salient object and *misses the subtle counterpart*, leading to incorrect relational judgments; bottom-up scanning progressively resolves and aligns to *both* entities, producing reliable spatial decisions—exactly reflected by the figure’s captions “Miss the subtle target / Miss one of the target” versus “Align to both targets.” Moreover, after evidence is recovered, *Refocusing* further calibrates the context window to an evidence-centric view, helping retain only the necessary surrounding context for reasoning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> *空间关系。*关系问题（例如摩托车手相对于卡车的左/右、摩天轮相对于骑马者的左/右、蓝色行李相对于公交车的左/右）需要联合定位*两个*目标。单次变体经常固着于某个显著物体，并*遗漏不显眼的对应目标*，从而作出错误的关系判断；自底向上扫描则逐步解析并对齐*两个*实体，生成可靠的空间决策——这恰好体现在图中的说明文字：“Miss the subtle target / Miss one of the target” 与 “Align to both targets”的对比。此外，在证据恢复后，*重聚焦*会进一步将上下文窗口校准为以证据为中心的视图，从而仅保留推理所必需的周围上下文。

### D.2 Example Model Outputs / 模型输出示例

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> To illustrate the advantages of our approach, we present side-by-side qualitative examples comparing **DeepScan** with strong LVLMs—GPT-5 (run in its advanced reasoning mode), GPT-4o, and Qwen3-VL-235B-A22B—as well as training-free baselines *ZoomRefine* and *DyFo*. For a fair comparison across training-free methods, ZoomRefine, DyFo, and **DeepScan** all use Qwen2.5-VL-72B as the LVLM backbone. Each example reports both the visual grounding and the model’s answer. The following examples confirm that **DeepScan** delivers stronger visually grounded reasoning—superior evidence localization and more accurate answers—than the two representative training-free baselines. Moreover, **DeepScan** outperforms GPT-4o and the larger-scale Qwen3-VL-235B-A22B, despite using a smaller Qwen2.5-VL-72B backbone, in both perception and reasoning. Notably, its end-to-end inference latency is of the same order as GPT-5, indicating a favorable performance–efficiency trade-off.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 为展示我们方法的优势，我们给出了并列的定性示例，将 **DeepScan** 与强大的 LVLM——GPT-5（以其高级推理模式运行）、GPT-4o 和 Qwen3-VL-235B-A22B——以及免训练基线 *ZoomRefine* 和 *DyFo* 进行比较。为确保免训练方法之间的公平比较，ZoomRefine、DyFo 和 **DeepScan** 均使用 Qwen2.5-VL-72B 作为 LVLM 骨干。每个示例同时报告视觉定位结果和模型答案。以下示例证实，**DeepScan** 比两个具有代表性的免训练基线展现出更强的视觉定位推理能力——证据定位更优、答案更准确。此外，尽管使用了更小的 Qwen2.5-VL-72B 骨干，**DeepScan** 在感知和推理两方面均优于 GPT-4o 和规模更大的 Qwen3-VL-235B-A22B。值得注意的是，其端到端推理延迟与 GPT-5 处于同一数量级，表明其具有良好的性能—效率权衡。

#### Active uncaptioned figure block 1: input / 活跃无图注图块 1：输入

![Source figure](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/example1_gpt4o.png)

**Caption:** Example 1 input and GPT-4o output.

**Caption[CN]:** 示例 1 输入与 GPT-4o 输出。

**Source caption status:** No `\caption` text is present in the TeX source.

**源图注状态：** TeX 源文件中没有 `\caption` 文本。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span>
>
> The following searchable literals are available in the source asset:
>
> ```text
> Example 1
> Images
> Evidence
> 0.004%
> GT
> (A) white
> Question: What is the color of the man's cap?
> (A) white (B) blue (C) red (D) black
> ```

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span>
>
> 源资产中可检索到以下文字，其中文翻译为：
>
> ```text
> 示例 1
> 图像
> 证据
> 0.004%
> 真实答案
> (A) 白色
> 问题：这名男子的帽子是什么颜色？
> (A) 白色 (B) 蓝色 (C) 红色 (D) 黑色
> ```

#### Active uncaptioned figure block 2: GPT-4o / 活跃无图注图块 2：GPT-4o

**Source caption status:** No `\caption` text is present in the TeX source.

**源图注状态：** TeX 源文件中没有 `\caption` 文本。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **GPT-4o literal response:**
>
> ```text
> There is no man visible in the image, so the question “What is the color of the man's cap?” cannot be answered based on the provided photo. If you meant to upload a different image or if there's a specific region you'd like me to zoom in on or analyze further, please let me know!
> ```

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **GPT-4o 逐字响应译文：**
>
> ```text
> 图像中看不到男子，因此无法根据所提供的照片回答“男子的帽子是什么颜色？”这个问题。如果你原本想上传另一张图像，或者希望我放大或进一步分析某个特定区域，请告诉我！
> ```

#### Active uncaptioned figure block 3: Qwen / 活跃无图注图块 3：Qwen

![Source figure](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/example1_qwen3.png)

**Caption:** Qwen3-VL-235B-A22B output for Example 1.

**Caption[CN]:** Qwen3-VL-235B-A22B 对示例 1 的输出。

**Source caption status:** No `\caption` text is present in the TeX source.

**源图注状态：** TeX 源文件中没有 `\caption` 文本。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Qwen3-VL-235B-A22B literal response:**
>
> ```text
> Actually, there is no man visible in the image. The photo shows a landscaped outdoor area with palm trees, buildings (some beige, some blue), grass, and decorative pots — but no people, and therefore no man wearing a cap.
>
> Since the question asks about “the man's cap” but there is no man in the picture, none of the options (A) white, (B) blue, (C) red, or (D) black can be correct.
>
> ✅ Correct Answer: None — there is no man in the image.
>
> If this is a test question, it may be designed to catch attention to detail — always check whether the subject actually exists in the image before selecting an answer.
>
> Final Answer: Not applicable — no man present.
> ```

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **Qwen3-VL-235B-A22B 逐字响应译文：**
>
> ```text
> 实际上，图像中看不到男子。照片展示的是一处经过景观布置的户外区域，其中有棕榈树、建筑（一些是米色，一些是蓝色）、草地和装饰花盆——但没有人，因此也没有戴帽子的男子。
>
> 由于问题询问“男子的帽子”，但图中没有男子，所以选项 (A) 白色、(B) 蓝色、(C) 红色或 (D) 黑色都不可能正确。
>
> ✅ 正确答案：无——图像中没有男子。
>
> 如果这是一道测试题，它可能旨在考查对细节的注意——选择答案前应始终确认题目中的主体是否确实存在于图像中。
>
> 最终答案：不适用——没有男子。
> ```

#### Active uncaptioned figure block 4: ZoomRefine, Dyfo, and DeepScan / 活跃无图注图块 4：ZoomRefine、Dyfo 与 DeepScan

![Source figure](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/example1_comparison.png)

**Caption:** ZoomRefine, DyFo, and DeepScan grounding and answer comparison for Example 1.

**Caption[CN]:** 示例 1 中 ZoomRefine、DyFo 与 DeepScan 的定位和回答对比。

**Source caption status:** No `\caption` text is present in the TeX source.

**源图注状态：** TeX 源文件中没有 `\caption` 文本。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span>
>
> The following literal model responses are available in the source asset and are transcribed exactly:
>
> **ZoomRefine Answer**
>
> ```text
> Actually, there is no man visible in the
> image provided. The image shows a
> landscape with palm trees, buildings,
> grass, and a signpost, but no people.
> Therefore, there is no man’s cap to
> determine the color of.
>
> Predict Answer: N/A.
> ```
>
> **Dyfo Answer**
>
> ```text
> The man in the image is wearing a cap.
> While the low resolution of the image
> makes it slightly ambiguous, the cap is
> definitively not white, blue, or red. It
> is a deep, dark shade that absorbs most
> of the light, which is characteristic of
> black. Therefore, the color of the
> man's cap is best identified as black.
>
> Predict Answer: (D) black.
> ```
>
> **DeepScan Answer**
>
> ```text
> The main body of the cap is a very
> light color, appearing as white or off-
> white against the darker, greenish
> background. Comparing the observed
> light color to the given options, the
> only option that matches the visual
> evidence is clearly white.
>
> Predict Answer: (A) white.
> ```
>
> The source asset repeats the following question beneath each of the three rows:
>
> ```text
> Question: What is the color of the man's cap? (A) white (B) blue (C) red (D) black
> ```
>
> The row labels in source order are:
>
> ```text
> Images
> Grounding Result
> ZoomRefine Answer
>
> Images
> Grounding Result
> Dyfo Answer
>
> Images
> Scanning Result
> Refocusing Result
> DeepScan Answer
> ```

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span>
>
> 源资产中存在以下模型逐字响应；其中文翻译分别为：
>
> **ZoomRefine 回答**
>
> ```text
> 实际上，所提供的图像中看不到男子。图像展示了一处有棕榈树、建筑、草地和路标的景观，
> 但没有人物。因此，图中没有男子的帽子可供判断颜色。
>
> 预测答案：N/A。
> ```
>
> **Dyfo 回答**
>
> ```text
> 图中的男子戴着一顶帽子。尽管图像分辨率较低，使其略显模糊，但这顶帽子肯定不是白色、
> 蓝色或红色。它呈现一种吸收了大部分光线的深暗色调，这是黑色的典型特征。因此，男子
> 帽子的颜色最应判定为黑色。
>
> 预测答案：(D) 黑色。
> ```
>
> **DeepScan 回答**
>
> ```text
> 帽子的主体颜色很浅，在较暗的绿色背景衬托下呈白色或米白色。将观察到的浅色与给定选项
> 比较，唯一符合视觉证据的选项显然是白色。
>
> 预测答案：(A) 白色。
> ```
>
> 源资产在三行中的每一行下方都重复了以下问题；其中文翻译为：
>
> ```text
> 问题：这名男子的帽子是什么颜色？(A) 白色 (B) 蓝色 (C) 红色 (D) 黑色
> ```
>
> 源文件中的行标签按顺序翻译为：
>
> ```text
> 图像
> 定位结果
> ZoomRefine 回答
>
> 图像
> 定位结果
> Dyfo 回答
>
> 图像
> 扫描结果
> 重聚焦结果
> DeepScan 回答
> ```


## References

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> References are retained in their original bibliographic language and searchable form. The PDF itself abbreviates long author lists with “et al.”; those source-native abbreviations are preserved rather than expanding beyond the authoritative rendered source.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 参考文献保留原始书目语言和可检索形式。PDF 本身使用“et al.”缩写较长作者列表；为避免超出权威渲染来源进行扩写，此处保留这些源生缩写。

1. Alayrac et al. *Flamingo: A Visual Language Model for Few-Shot Learning.* NeurIPS, 2022.
2. An et al. *Mitigating Object Hallucinations in Large Vision-Language Models with Assembly of Global and Local Attention.* CVPR, 2025.
3. Bai et al. *Qwen2.5-VL Technical Report.* arXiv:2502.13923, 2025.
4. Chen et al. *Shikra: Unleashing Multimodal LLM's Referential Dialogue Magic.* arXiv:2306.15195, 2023.
5. Chen et al. *How Far Are We to GPT-4V? Closing the Gap to Commercial Multimodal Models with Open-Source Suites.* Science China Information Sciences, 2024.
6. Cheng et al. *Focusing Attention: Towards Accurate Text Recognition in Natural Images.* ICCV, 2017.
7. DeepMind. *Gemini-2.5-Flash.* 2025.
8. DeepMind. *Gemini-2.5-Pro.* 2025.
9. Lai et al. *Mini-o3: Scaling up Reasoning Patterns and Interaction Turns for Visual Search.* arXiv:2509.07969, 2025.
10. Li et al. *LLaVA-OneVision: Easy Visual Task Transfer.* arXiv:2408.03326, 2024.
11. Li et al. *Imagine While Reasoning in Space: Multimodal Visualization-of-Thought.* ICML, 2025.
12. Li et al. *LAVIS: A One-Stop Library for Language-Vision Intelligence.* ACL, 2023.
13. Li et al. *DyFo: A Training-Free Dynamic Focus Visual Search for Enhancing LMMs in Fine-Grained Visual Understanding.* CVPR, 2025.
14. Li et al. *BLIP: Bootstrapping Language-Image Pre-Training for Unified Vision-Language Understanding and Generation.* ICML, 2022.
15. Li et al. *BLIP-2: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models.* ICML, 2023.
16. Li et al. *Why 1 + 1 < 1 in Visual Token Pruning: Beyond Naive Integration via Multi-Objective Balanced Covering.* NeurIPS, 2025.
17. Li et al. *MSA2: Multi-Task Framework with Structure-Aware and Style-Adaptive Character Representation for Open-Set Chinese Text Recognition.* ICCV, 2025.
18. Liu et al. *Visual Instruction Tuning.* NeurIPS, 2023.
19. Liu et al. *LLaVA-NeXT: Improved Reasoning, OCR, and World Knowledge.* 2024.
20. Liu et al. *Grounding DINO: Marrying DINO with Grounded Pre-Training for Open-Set Object Detection.* ECCV, 2024.
21. Medeiros. *Language Segment-Anything: SAM with Text Prompt.* 2024.
22. OpenAI. *GPT-4o System Card.* 2024.
23. OpenAI. *Introducing o3 and o4-mini.* 2025.
24. Qian et al. *Zoomer: Adaptive Image Focus Optimization for Black-Box MLLM.* arXiv:2505.00742, 2025.
25. Radford et al. *Learning Transferable Visual Models from Natural Language Supervision.* ICML, 2021.
26. Rasheed et al. *GLaMM: Pixel Grounding Large Multimodal Model.* CVPR, 2024.
27. Ren et al. *Grounding DINO 1.5: Advance the Edge of Open-Set Object Detection.* arXiv:2405.10300, 2024.
28. Sarch et al. *Grounded Reinforcement Learning for Visual Reasoning.* arXiv:2505.23678, 2025.
29. Selvaraju et al. *Grad-CAM: Visual Explanations from Deep Networks via Gradient-Based Localization.* ICCV, 2017.
30. Shen et al. *ZoomEye: Enhancing Multimodal LLMs with Human-Like Zooming Capabilities through Tree-Based Image Exploration.* EMNLP, 2025.
31. Su et al. *Pixel Reasoner: Incentivizing Pixel Space Reasoning via Curiosity-Driven Reinforcement Learning.* NeurIPS, 2025.
32. Su et al. *OpenThinkIMG: Learning to Think with Images via Visual Tool Reinforcement Learning.* arXiv:2505.08617, 2025.
33. Su et al. *Thinking with Images for Multimodal Reasoning: Foundations, Methods, and Future Frontiers.* arXiv:2506.23918, 2025.
34. Wang et al. *Scaling Laws in Patchification: An Image Is Worth 50,176 Tokens and More.* ICML, 2025.
35. Wang et al. *Traceable Evidence Enhanced Visual Grounded Reasoning: Evaluation and Method.* ICLR, 2026.
36. Wang et al. *VGR: Visual Grounded Reasoning.* arXiv:2506.11991, 2025.
37. Wang et al. *Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution.* arXiv:2409.12191, 2024.
38. Wang, Cong, and Woodman. *Statistical Learning Speeds Visual Search: More Efficient Selection, or Faster Response?* Journal of Experimental Psychology: General, 2023.
39. Wang et al. *Divide, Conquer and Combine: A Training-Free Framework for High-Resolution Image Perception in Multimodal Large Language Models.* AAAI, 2025.
40. Wolfe. *Visual Search: How Do We Find What We Are Looking For?* Annual Review of Vision Science, 2020.
41. Wolfe and Horowitz. *Five Factors That Guide Attention in Visual Search.* Nature Human Behaviour, 2017.
42. Wu and Xie. *V\*: Guided Visual Search as a Core Mechanism in Multimodal LLMs.* CVPR, 2024.
43. Xiao et al. *Efficient Streaming Language Models with Attention Sinks.* ICLR, 2024.
44. Xie et al. *Large Multimodal Agents: A Survey.* arXiv:2402.15116, 2024.
45. You et al. *Ferret: Refer and Ground Anything Anywhere at Any Granularity.* ICLR, 2024.
46. Yu et al. *Zoom-Refine: Boosting High-Resolution Multimodal Understanding via Localized Zoom and Self-Refinement.* arXiv:2506.01663, 2025.
47. Zhan et al. *FARE: A Feature-Aware Radical Encoding Strategy for Zero-Shot Chinese Character Recognition.* ACCV, 2024.
48. Zhan et al. *Free Lunch: Frame-Level Contrastive Learning with Text Perceiver for Robust Scene Text Recognition in Lightweight Models.* ACM MM, 2024.
49. Zhang et al. *Latent Sketchpad: Sketching Visual Thoughts to Elicit Multimodal Reasoning in MLLMs.* arXiv:2510.24514, 2025.
50. Zhang et al. *Thyme: Think Beyond Images.* arXiv:2508.11630, 2025.
51. Zhang et al. *PSALM: Pixelwise Segmentation with Large Multi-Modal Model.* ECCV, 2024.
52. Zheng et al. *DeepEyes: Incentivizing Thinking with Images via Reinforcement Learning.* arXiv:2505.14362, 2025.
53. Zhu et al. *InternVL3: Exploring Advanced Training and Test-Time Recipes for Open-Source Multimodal Models.* arXiv:2504.10479, 2025.
