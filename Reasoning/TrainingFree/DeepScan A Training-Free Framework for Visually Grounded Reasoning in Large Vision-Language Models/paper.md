# DeepScan: A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models

> **中文题名：** DeepScan：面向大型视觉语言模型视觉落地推理的免训练框架  
> **作者：** Yangfu Li, Hongjian Zhan, Jiawei Chen, Yuning Gong, Qi Liu, Yue Lu  
> **出处：** CVPR 2026（论文注明已接收）；arXiv:2603.03857v1，2026-03-04  
> **论文类型：** 方法 / 算法论文  
> **源文件：** `Li 等 - 2026 - DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models.pdf`  
> **阅读器：** 全文英中对照；图表按首次实质讨论位置重排。页码与稳定块 ID 见 `source_map.json`。

## 阅读导航

- [术语表](#术语表)
- [Abstract](#abstract)
- [1. Introduction](#1-introduction)
- [2. Related Work](#2-related-work)
- [3. Methodology](#3-methodology)
- [4. Experiments](#4-experiments)
- [5. Conclusion](#5-conclusion)
- [Acknowledgments](#acknowledgments)
- [Supplementary Material](#supplementary-material)
- [Critical Reading Notes](#critical-reading-notes)
- [References](#references)

## 术语表

| Canonical term | 中文 | First-use definition / 决策 |
|---|---|---|
| Large Vision-Language Model (LVLM) | 大型视觉语言模型 | 首次展开，后文统一使用 LVLM |
| visually grounded reasoning | 视觉落地推理 | 指答案显式依赖已定位的视觉证据；不译为“扎根推理” |
| DeepScan | DeepScan | 方法名保留英文 |
| Hierarchical Scanning | 分层扫描 | 局部线索探索 + 多尺度证据提取 |
| Local Cue Exploration | 局部线索探索 | 在图像块内寻找高响应线索 |
| Multi-Scale Evidence Extraction | 多尺度证据提取 | 由点代理在原图尺度恢复证据 |
| Refocusing | 再聚焦 | 搜索最合适的证据中心上下文视图 |
| Evidence-Enhanced Reasoning | 证据增强推理 | 使用多粒度证据完成最终回答 |
| Hybrid Evidence Memory | 混合证据记忆 | 同时保存细粒度证据与粗粒度视图 |
| point-based proxy | 点式代理 | 从局部线索中选出的内点，用于点提示分割 |
| search expert | 搜索专家 | BLIP-ITM；通过 Grad-CAM 提供注意图 |
| visual expert | 视觉专家 | LangSAM；提供点提示分割与文本条件检测 |
| attention sink / attention drift | 注意力汇聚陷阱 / 注意力漂移 | 全局显著但无关区域吸引注意，或注意转向相似物体 |
| V* Bench | V* 基准 | 细粒度属性与空间关系基准 |
| HR-Bench | HR-Bench | 4K/8K 高分辨率视觉理解基准 |
| TreeBench | TreeBench | 评估可追踪证据、“以图思考”和二阶推理 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Humans can robustly localize visual evidence and provide grounded answers even in noisy environments by identifying critical cues and then relating them to the full context in a bottom-up manner. Inspired by this, we propose DeepScan, a training-free framework that combines Hierarchical Scanning, Refocusing, and Evidence-Enhanced Reasoning for visually grounded reasoning in Large Vision-Language Models (LVLMs). Unlike existing methods that pursue one-shot localization of complete evidence, Hierarchical Scanning performs local cue exploration and multi-scale evidence extraction to recover evidence in a bottom-up manner, effectively mitigating the impacts of distractive context. Refocusing then optimizes the localized evidence view through collaboration of LVLMs and visual experts. Finally, Evidence-Enhanced Reasoning aggregates multi-granular views via a hybrid evidence memory and yields accurate and interpretable answers. Experimental results demonstrate that DeepScan significantly boosts LVLMs in diverse visual tasks, especially in fine-grained visual understanding. It achieves 90.6% overall accuracy on V* when integrated with Qwen2.5-VL-7B. Moreover, DeepScan provides consistent improvements for LVLMs across various architectures and model scales without additional adaptation cost. The code will be open-source at DeepScan.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 人类即使处在噪声环境中，也能先识别关键线索，再以自底向上的方式把线索关联回完整语境，从而稳健地定位视觉证据并给出有依据的答案。受此启发，作者提出 DeepScan：一个将分层扫描、再聚焦与证据增强推理结合起来的免训练框架，用于提升大型视觉语言模型（LVLM）的视觉落地推理。不同于一次性定位完整证据的现有方法，分层扫描通过局部线索探索和多尺度证据提取，自底向上地恢复证据，从而减弱干扰上下文的影响；再聚焦通过 LVLM 与视觉专家协作优化已定位证据的视图；证据增强推理则借助混合证据记忆聚合多粒度视图，产生准确且可解释的答案。实验表明，DeepScan 在多类视觉任务，尤其是细粒度视觉理解上显著增强 LVLM；与 Qwen2.5-VL-7B 结合时，V* 总体准确率达到 90.6%，且无需额外适配即可跨架构、跨模型规模稳定提升性能。代码将开源于 DeepScan 项目。

## 1. Introduction

### Fig. 1. 自顶向下与 DeepScan 自底向上落地流程的对比

![Fig. 1](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig1.png)

**Caption:** Comparison of grounding pipelines in existing methods and the proposed DeepScan. (a) Existing methods depend on one-shot localization of evidence regions, making them sensitive to noisy contexts. (b) DeepScan uses local cue exploration to identify discriminative cues and recovers evidence from these cues in a bottom-up manner, robustly localizing critical visual content even in challenging scenes.

**Caption[CN]:** 现有方法与 DeepScan 的落地流程对比。(a) 现有方法依赖一次性定位证据区域，因此对噪声上下文敏感；(b) DeepScan 先通过局部线索探索识别有判别力的线索，再从这些线索自底向上恢复证据，即使在困难场景中也能稳健定位关键视觉内容。

**Reading note:** 左侧错误链说明“先猜完整区域、再细化”会被相似目标误导；右侧的关键不是多裁几次图，而是先在局部建立可信锚点，再回到全图恢复对象。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Humans excel at grounding critical visual information and reasoning based on the located evidence, which is a hallmark of intelligence recognized in cognitive and vision science [38, 40, 41]. While this is natural to humans, it remains challenging for LVLMs to replicate this behavior, leading to suboptimal performance in complex visual tasks [16, 34, 39, 42].

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 人类擅长把关键视觉信息落到具体位置，并基于已定位的证据推理；认知科学与视觉科学将这种能力视为智能的重要标志 [38, 40, 41]。这种行为对人类很自然，但 LVLM 仍难以稳定复现，因此在复杂视觉任务中表现欠佳 [16, 34, 39, 42]。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> To reproduce this ability in LVLMs, some approaches employ reinforcement learning with visually supervised rewards such as IoU, or context engineering, enabling active perception and evidence localization during reasoning [31, 35, 42, 46, 50, 52]. Other work augments LVLM grounding with auxiliary modules [4, 26, 45, 51], while recent studies integrate external visual experts such as GroundingDINO and LangSAM and use agreement between experts and LVLMs to localize evidence [2, 13, 20, 21, 24, 27].

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 为把这种能力引入 LVLM，一类方法使用带视觉监督奖励（如 IoU）的强化学习或上下文工程，使模型在推理过程中主动感知并定位证据 [31, 35, 42, 46, 50, 52]；另一类方法加入辅助模块 [4, 26, 45, 51]。近期工作还引入 GroundingDINO、LangSAM 等外部视觉专家，通过专家与 LVLM 的一致性来定位证据 [2, 13, 20, 21, 24, 27]。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Despite these advances, most existing methods follow a top-down grounding paradigm: they first perform an image-level search for coarse-grained proxies, such as region proposals, detection boxes, or textual descriptions, and then refine them into fine-grained evidence. This requires one-shot localization of complete evidence regions from the entire image and is easily affected by noisy context, attention sinks, or semantically similar objects. The LVLM may then refuse to answer or guess from incorrect evidence. Humans instead use a bottom-up routine in difficult visual tasks: in a spot-the-difference puzzle, for example, they scan local patches for subtle discrepancies and verify those cues at image level to recover the target while suppressing distractors.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 尽管已有进展，多数方法仍采用自顶向下的落地范式：先在整幅图像上搜索区域提议、检测框或文本描述等粗粒度代理，再将其细化为证据。这要求模型从全图一次性找准完整证据，容易受到噪声上下文、注意力汇聚陷阱和语义相似物体的影响；随后 LVLM 可能拒答，或依据错误证据猜测。人类在困难任务中更常采用自底向上的过程：例如玩“找不同”时，先扫描局部图块中的细微差异，再回到图像层面核验线索、恢复目标并抑制干扰项。

### Fig. 2. V* 上的性能定位

![Fig. 2](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig2.png)

**Caption:** Performance of LVLMs and visually grounded reasoning variants on V*. DeepScan achieves highly competitive results.

**Caption[CN]:** LVLM 与视觉落地推理方法在 V* 上的性能。DeepScan 取得了极具竞争力的结果。

**Reading note:** 图中把训练型、免训练和通用 LVLM 放在同一坐标系中；DeepScan-72B 接近 GPT-o3，而主干为 Qwen2.5-VL-7B 的版本也显著超过原始模型。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Inspired by this human behavior, DeepScan comprises Hierarchical Scanning, Refocusing, and Evidence-Enhanced Reasoning. Hierarchical Scanning combines patch-wise cue exploration with image-level evidence extraction; Refocusing refines the surrounding context through collaboration between visual experts and LVLMs; and Evidence-Enhanced Reasoning supplies multi-granular views through a Hybrid Evidence Memory. As a training-free framework, DeepScan scales to larger backbones such as Qwen2.5-VL-72B without adaptation.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> DeepScan 由三个环节组成：分层扫描把图块级线索探索与图像级证据提取结合起来；再聚焦通过视觉专家与 LVLM 协作，重新校准证据周围的上下文；证据增强推理则使用混合证据记忆向 LVLM 提供多粒度视图。由于不需要训练，该框架可直接扩展到 Qwen2.5-VL-72B 等更大主干。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The contributions are fourfold: (1) DeepScan explicitly localizes, recalibrates, and integrates evidence before answering; (2) Hierarchical Scanning introduces a bottom-up grounding paradigm based on local cue exploration and multi-scale evidence extraction; (3) Refocusing recalibrates evidence views through interaction between LVLMs and external visual experts; and (4) comprehensive experiments show average improvements of 16.3% on V* and 5.5% on TreeBench for Qwen2.5-VL-7B, with ablations across architectures and scales supporting generalizability.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 论文的四项贡献是：(1) 在回答前显式定位、校准并整合证据；(2) 提出基于局部线索探索和多尺度证据提取的自底向上分层扫描；(3) 提出由 LVLM 与外部视觉专家交互完成证据视图校准的再聚焦；(4) 完整实验显示，基于 Qwen2.5-VL-7B 时在 V* 和 TreeBench 上平均提升 16.3% 与 5.5%，跨架构和跨规模消融也支持其泛化性。

## 2. Related Work

### 2.1 Large Vision-Language Models

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Early LVLMs such as Flamingo and BLIP-2 integrated visual features into an LLM through cross-attention, whereas LLaVA projected features from a frozen vision encoder into the LLM semantic space with a lightweight MLP. Subsequent work scaled LVLMs to OCR, general VQA, and latent visual reasoning. High-resolution input became a critical frontier: LLaVA-NeXT and InternVL1.5 support arbitrary resolutions, while Qwen2-VL and Qwen2.5-VL use mRoPE for resolution generality. Yet current LVLMs lack an explicit mechanism to perceive and localize task-relevant evidence, causing hallucinations especially in high-resolution scenes. DeepScan addresses this gap by coupling LVLMs with external experts.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Flamingo、BLIP-2 等早期 LVLM 通过交叉注意力把视觉特征接入 LLM；LLaVA 则用轻量 MLP 将冻结视觉编码器的特征映射到 LLM 语义空间。后续研究把能力扩展到 OCR、通用 VQA 和潜在视觉推理，高分辨率输入也成为关键前沿：LLaVA-NeXT、InternVL1.5 支持任意分辨率，Qwen2-VL 与 Qwen2.5-VL 通过 mRoPE 提升分辨率泛化。然而，现有 LVLM 通常缺少显式感知并定位任务相关证据的机制，在高分辨率场景中尤其容易产生幻觉。DeepScan 通过耦合外部专家填补这一缺口。

### 2.2 Visually Grounded Reasoning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Agents with “think-with-images” capabilities dynamically manipulate images during inference to localize and emphasize critical content. Subsequent work uses supervised fine-tuning, reinforcement learning with visual rewards, curiosity-driven objectives, explicit evidence localization, and visual memory. These approaches are costly and difficult to generalize across architectures and model scales. Training-free alternatives use external experts, tree search, or self-refinement for grounding-then-answering, but most still rely on a coarse-to-fine strategy sensitive to noisy context and similar objects. Hierarchical Scanning instead progressively recovers evidence from local cues through point-based proxies.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 具备“以图思考”能力的智能体会在推理时动态操作图像，以定位和强调关键视觉内容。后续工作采用监督微调、视觉奖励强化学习、好奇心目标、显式证据定位和视觉记忆，但这些方案代价较高，也难以跨架构、跨模型规模泛化。免训练替代方案会借助外部专家、树搜索或自我细化执行“先落地、后回答”，但多数仍依赖容易受噪声与相似物体影响的由粗到细策略。分层扫描则通过点式代理，从局部线索出发逐步恢复视觉证据。

## 3. Methodology

### Fig. 3. DeepScan 总体架构

![Fig. 3](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig3.png)

**Caption:** Overall architecture of DeepScan. Hierarchical Scanning progressively recovers visual evidence from in-patch cues formulated as point-based proxies using Local Cue Exploration and Multi-Scale Evidence Extraction. Refocusing further refines the surrounding context for the fused evidence via interactions between LVLMs and visual experts. Evidence-Enhanced Reasoning leverages a Hybrid Evidence Memory to provide multi-granular information to the LVLM.

**Caption[CN]:** DeepScan 总体架构。分层扫描通过局部线索探索与多尺度证据提取，将图块内线索表示为点式代理并逐步恢复视觉证据；再聚焦通过 LVLM 与视觉专家交互，为融合证据细化周围语境；证据增强推理利用混合证据记忆向 LVLM 提供多粒度信息。

**Reading note:** 这张图给出了整篇论文的因果链：局部注意线索不是最终证据，而是驱动原图分割的代理；证据经完整性校准后，以细粒度对象 + 粗粒度关系视图共同进入最终推理。

### 3.1 Overview

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> DeepScan localizes, recalibrates, and integrates visual evidence to produce more accurate and interpretable answers. It augments an LVLM with two plug-and-play models: a search expert and a visual expert. Given an image $I \in \mathbb{R}^{H\times W\times 3}$ and a question $q$, the search expert highlights potential cues in a local patch $p \in I$ through a Grad-CAM attention map $S$.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> DeepScan 通过定位、重新校准并整合视觉证据，生成更准确、可解释的答案。它为 LVLM 加入两个即插即用模型：搜索专家和视觉专家。给定图像 $I \in \mathbb{R}^{H\times W\times 3}$ 与问题 $q$，搜索专家用 Grad-CAM 注意图 $S$ 在局部图块 $p \in I$ 中突出潜在线索。

$$
S = \operatorname{SEARCH}(p,q) \in \mathbb{R}^{h\times w},\qquad p \in \mathbb{R}^{h\times w\times 3}. \tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The visual expert exposes two image-level primitives: segmentation from a point prompt $c=(x,y)\in I$, and detection conditioned on the question. Here $m$ is an evidence mask and $\mathcal{B}$ is the union of evidence bounding boxes. The LVLM can answer using regions enclosed by either $m$ or $\mathcal{B}$. Because these modules are used only at inference, the pipeline remains general and training-free.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 视觉专家提供两个图像级原语：由点提示 $c=(x,y)\in I$ 驱动的分割，以及由问题条件化的检测。其中 $m$ 是证据掩码，$\mathcal{B}$ 是证据框的并集。LVLM 可使用 $m$ 或 $\mathcal{B}$ 包围的区域回答问题；这些模块仅在推理时调用，因此流程保持通用且无需训练。

$$
m = \operatorname{SEGMENT}(I,c),\qquad \mathcal{B}=\operatorname{DETECT}(I,q). \tag{2}
$$

### 3.2 Hierarchical Scanning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> A natural way to suppress irrelevant content is to partition the image into patches and extract evidence patch by patch. The difficulty is that evidence may span multiple patches, while conventional proxies such as region proposals, boxes, or textual descriptions poorly represent incomplete evidence. Hierarchical Scanning therefore connects patch-wise Local Cue Exploration and image-level Multi-Scale Evidence Extraction through point-based proxies, producing a bottom-up grounding pipeline.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 抑制无关视觉内容的一种自然方法是切分图像并逐块提取证据。难点在于目标证据可能跨越多个图块，而区域提议、检测框或文本描述等传统代理很难表达不完整证据。分层扫描因此用点式代理连接“图块级局部线索探索”与“图像级多尺度证据提取”，形成自底向上的落地流程。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In Local Cue Exploration, for each patch $p$ and question $q$, the search expert produces an attention map $S_p$. Otsu thresholding converts it into a binary high-response mask $S_p^+$, whose connected components are candidate cue regions.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在局部线索探索中，搜索专家针对图块 $p$ 与问题 $q$ 产生注意图 $S_p$。Otsu 阈值法将其变为二值高响应掩码 $S_p^+$，其中的连通分量构成候选线索区域。

$$
S_p^+ = \mathbb{I}(S_p\ge T_p^*)\in\{0,1\}^{h\times w},\qquad T_p^*=\operatorname{OTSU}(S_p). \tag{3}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Each cue is represented by an interior point derived from geometry and semantics. The geometric term is the Euclidean distance from a candidate point to the cue boundary. Because geometry alone can yield multiple candidates for complex shapes such as U-shaped regions, the method multiplies normalized boundary distance by normalized semantic attention and selects the maximum, while filtering tiny components with threshold $\tau$.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 每个线索都由一个同时考虑几何与语义的内部点表示。几何项是候选点到线索边界的欧氏距离；但对 U 形等复杂区域，仅凭几何可能产生多个候选，因此方法将归一化边界距离与归一化语义注意相乘，选择乘积最大的点，并用阈值 $\tau$ 去除过小连通域。

$$
d(c,\partial G)=\inf_{\gamma\in\partial G}\lVert c-\gamma\rVert_2. \tag{4}
$$

$$
C_p=\left\{c_p^k\,\middle|\,c_p^k=\arg\max_{c\in G_p^k}\widetilde S_p(c)\,\widetilde d(c,\partial G_p^k),\ |G_p^k|\ge\tau\right\}. \tag{5}
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The in-patch proxies are lifted to image coordinates. For each lifted proxy $c'_p$, the visual expert performs point-prompt segmentation on the original image, recovering an image-level evidence mask $m$.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 选出的图块内点被提升到原图坐标。视觉专家随后以每个 $c'_p$ 为点提示，在原图上执行分割，恢复图像级证据掩码 $m$。

$$
m=\operatorname{SEGMENT}(I,c'_p)\in\{0,1\}^{H\times W}. \tag{6}
$$

### Fig. 4. 形态学后处理修复孔洞与缺失上下文

![Fig. 4](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig4.png)

**Caption:** Illustration of morphological post-processing. “+” marks point-based proxies; $m$ and $m^+$ denote evidence masks before and after post-processing, showing improved robustness.

**Caption[CN]:** 形态学后处理示意。“+”表示点式代理；$m$ 与 $m^+$ 分别是处理前后的证据掩码，后处理提升了掩码完整性与鲁棒性。

**Reading note:** 闭运算填补内部孔洞，膨胀补回必要的邻近上下文；它不仅改善证据质量，也避免同一对象因孔洞而被重复扫描。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> A single-point mask can contain interior holes or omit surrounding context. DeepScan applies morphological closing with a flat kernel $\mathcal{K}$ and dilation with disk kernel $S_r$ to form $m^+$. It then removes proxies already covered by $m^+$, crops the evidence from the minimal enclosing box, and asks the LVLM for a binary evidence judgment before adding the candidate to the evidence set $\mathcal{E}$.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 单点提示得到的掩码可能有内部孔洞，或缺失周边语境。DeepScan 使用平坦核 $\mathcal{K}$ 做闭运算，再用圆盘核 $S_r$ 膨胀得到 $m^+$；随后移除已落入 $m^+$ 的代理，从最小包围框裁出证据，并由 LVLM 做二元证据判断，确认后才加入证据集合 $\mathcal{E}$。

$$
m^+=(m\bullet\mathcal{K})\oplus S_r,\qquad m^+\in\{0,1\}^{H\times W}. \tag{7}
$$

$$
C'_p\leftarrow\{c\in C'_p\mid m^+(c)=0\}. \tag{8}
$$

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> A global visited mask is maintained by masking examined evidence from the image, reducing redundant computation. For acceleration, candidates are pre-filtered by area and only the $k$ smallest regions are evaluated by the LVLM. The rationale is that large salient evidence is often already detectable without explicit grounding, whereas localizing less salient evidence yields larger gains.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 方法还在全图上维护访问掩码，把已检查证据从后续扫描中屏蔽，减少重复计算。为加速推理，候选按面积预筛，只让 LVLM 判断最小的 $k$ 个区域。其依据是：大而显著的证据通常无需额外落地即可被 LVLM 识别，真正带来增益的是不显著的小证据。

### Fig. 5. 候选面积与性能—时延权衡

![Fig. 5](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig5.png)

**Caption:** Analysis of performance gain with respect to target area ratio and the performance-latency trade-off on V*. The infinity mark denotes no explicit truncation of candidate count $k$.

**Caption[CN]:** V* 上目标面积比例与性能增益的关系，以及性能—时延权衡。无穷符号表示不显式截断候选数量 $k$。

**Reading note:** $k=1$ 已保留约 96% 的最高性能并带来约 2 倍加速，说明“优先最小候选”是论文最直接的工程启发之一。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Empirically, even $k=1$ preserves about 96% of the maximum achievable performance while yielding roughly a $2\times$ speedup. This heuristic bounds the number of LVLM evaluations and reduces visual-token cost.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 实验上，即使只保留 $k=1$，仍可保持约 96% 的最高可达性能，同时获得约 $2\times$ 加速。该启发式规则直接限制 LVLM 判断次数并降低视觉 token 成本。

### 3.3 Refocusing

### Fig. 6. 再聚焦对证据上下文的校准

![Fig. 6](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig6.png)

**Caption:** Illustration of Refocusing, where $V^*$ denotes the selected result. Refocusing recalibrates proxy misalignment by adaptively completing or further amplifying evidence.

**Caption[CN]:** 再聚焦示意，$V^*$ 表示最终选中的视图。再聚焦通过自适应补全证据上下文或进一步放大目标，修正点式代理错位造成的问题。

**Reading note:** 左例需要 Zoom-Out 补回被裁掉的人体关系，右例需要 Zoom-In 去除干扰并放大手套；同一“更紧的裁剪”策略不可能同时解决两类问题。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Precise proxy placement is difficult when multiple elements are adjacent, so the recovered view may contain too little or too much context. Refocusing integrates the LVLM and visual expert to search for an evidence-centric view with an appropriate context window. It initializes from $V_1=\operatorname{CROP}(I,b_m)$, where $b_m$ is the minimum box enclosing all evidence.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 当多个视觉元素彼此邻近时，点代理很难精确落位，恢复的视图可能缺少语境，也可能包含过多干扰。再聚焦联合 LVLM 与视觉专家，搜索上下文范围合适的“证据中心视图”。初始视图为 $V_1=\operatorname{CROP}(I,b_m)$，其中 $b_m$ 是包围全部证据的最小框。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Two actions generate successor states. Zoom-In crops a view to the union of detections conditioned on the question; Zoom-Out isotropically expands the view around its center by scale $s>1$.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 状态转移使用两个动作：Zoom-In 按问题条件化检测结果的并集进一步裁剪视图；Zoom-Out 以视图中心为基准，按尺度 $s>1$ 各向同性扩大上下文。

$$
\operatorname{IN}(V,q)=\operatorname{CROP}(V,\operatorname{DETECT}(V,q)). \tag{9}
$$

$$
\operatorname{OUT}(V,s)=\operatorname{CROP}(I,\operatorname{SCALEBBOX}(V,s)). \tag{10}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The selection policy prefers the smallest view that still contains all evidence needed for the answer. Its LVLM-based reward is an evidence-completeness indicator multiplied by the inverse area ratio. A view receives zero if the LVLM judges it incomplete; otherwise smaller complete views score higher.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 选择策略偏好“仍包含全部必要证据的最小视图”。基于 LVLM 的奖励由证据完整性指示量乘以反面积比构成：若 LVLM 判断视图不完整，得分为零；若完整，则越小的视图分数越高。

$$
R(V)=\mathbb{I}_{V\rightsquigarrow q}\cdot\frac{HW}{hw},\qquad V\in\mathbb{R}^{h\times w\times3}. \tag{11}
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Because Hierarchical Scanning provides a good initialization, the search need not cover the whole image. Zoom-In is empirically idempotent at $V_1$; repeated Zoom-Out operations compose multiplicatively; and a Zoom-Out after a complete Zoom-In cannot improve the size-regularized reward. If the Zoom-In view is incomplete, any context restored by Zoom-Out can be restored directly from $V_1$. Therefore the branch $\operatorname{OUT}(\operatorname{IN}(V_1,q),s)$ can be omitted without losing the global optimum under these assumptions.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 由于分层扫描提供了良好初始化，搜索无需覆盖整图。论文指出：在 $V_1$ 上 Zoom-In 经验上具有幂等性；连续 Zoom-Out 可合成为尺度相乘的一次操作；若 Zoom-In 后证据已完整，再 Zoom-Out 不会提高带面积正则的奖励。若 Zoom-In 后不完整，那么 Zoom-Out 能补回的上下文也可直接从 $V_1$ 补回。因此在这些假设下，可以删除 $\operatorname{OUT}(\operatorname{IN}(V_1,q),s)$ 分支而不损失全局最优解。

$$
\operatorname{IN}(\operatorname{IN}(V_1,q),q)=\operatorname{IN}(V_1,q). \tag{12}
$$

$$
\operatorname{OUT}(\operatorname{OUT}(V_1,s_1),s_2)=\operatorname{OUT}(V_1,s_1s_2). \tag{13}
$$

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The resulting behaviorally complete search set has only four states: the initial view, its Zoom-In, its Zoom-Out, and the Zoom-In of the Zoom-Out. The scale is set to $s=1.5$ by grid search. States are traversed depth-first and the best-scoring view is selected greedily.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 最终搜索空间只有四个在行为上完备的状态：初始视图、初始视图的 Zoom-In、初始视图的 Zoom-Out，以及 Zoom-Out 结果的 Zoom-In。尺度经网格搜索设为 $s=1.5$；算法按深度优先顺序遍历并贪心选择最高分视图。

$$
\mathcal{V}=\{V_1,V_2,V_3,V_4\},\quad V_2=\operatorname{IN}(V_1,q),\quad V_3=\operatorname{OUT}(V_1,s),\quad V_4=\operatorname{IN}(V_3,q). \tag{17}
$$

### 3.4 Evidence-Enhanced Reasoning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The preceding stages build a Hybrid Evidence Memory $\mathcal{H}$ containing fine-grained evidence from Hierarchical Scanning and the selected coarse-grained view from Refocusing. It is materialized as an ordered multi-image prompt $[e_1,\ldots,V^*]$.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 前两阶段构建混合证据记忆 $\mathcal{H}$：既保存分层扫描得到的细粒度证据，也保存再聚焦选出的粗粒度视图。它最终被组织成有序多图提示 $[e_1,\ldots,V^*]$。

$$
\mathcal{H}=\{e,V^*\mid (b,e)\in\mathcal{E},\ V^*=\arg\max_{V\in\mathcal{V}}R(V)\}. \tag{18}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Fine-grained evidence supports object-attribute recognition, while the coarse view preserves relationships and context. The LVLM therefore produces the final answer as $A=\operatorname{REASON}(\mathcal{H},q)$ with both detailed and comprehensive visual support.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 细粒度证据用于辨认对象属性，粗粒度视图保留对象关系与语境。因此 LVLM 以 $A=\operatorname{REASON}(\mathcal{H},q)$ 生成最终答案，同时兼顾细节与整体关系。

## 4. Experiments

### 4.1 Experimental Settings

### Table 1. V* 与 HR-Bench 主结果

![Table 1](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table1.png)

**Caption:** Comparisons on V* Bench and HR-Bench. All baselines are developed from Qwen2.5-VL-7B; RL-based methods are shaded gray; dagger results are self-collected.

**Caption[CN]:** V* Bench 与 HR-Bench 对比。所有基线均基于 Qwen2.5-VL-7B；灰色为强化学习方法；带 † 的结果由作者复现。

**Reading note:** DeepScan 在 V* 总体 / 属性 / 空间上为 90.6 / 93.0 / 86.8，相比原始 Qwen2.5-VL-7B 提升 16.3 / 15.6 / 17.1 个百分点；HR-Bench 的提升较小但稳定。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> V* Bench contains 191 high-resolution images and emphasizes extremely small targets with mean area below 0.05%. It covers Direct Attribute recognition (115 samples) and Spatial Relationship reasoning (76 samples), evaluated by multiple-choice accuracy. HR-Bench provides 4K and 8K versions, each with 200 images split evenly into Single-Instance and Cross-Instance perception, evaluated by cyclic-permutation multiple-choice accuracy. TreeBench contains 405 images and tests traceable evidence localization, subtle-target perception, and second-order reasoning, reporting both accuracy and mIoU.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> V* Bench 含 191 张高分辨率图像，目标平均面积小于 0.05%，包括 115 个直接属性样本和 76 个空间关系样本，以选择题准确率评估。HR-Bench 有 4K、8K 两个版本，每版 200 张图像，平均分为单实例与跨实例感知，采用循环置换选择题协议。TreeBench 含 405 张图像，评估可追踪证据定位、细微目标感知和二阶推理，同时报告准确率与 mIoU。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Baselines include RL-based methods, training-free methods, private models, and open-source general LVLMs. DeepScan uses BLIP-ITM base as the search expert and LangSAM as the visual expert. The default candidate count is $k=10$. It is evaluated with LLaVA-1.5-7B, Qwen2-VL-7B, and Qwen2.5-VL at 7B, 32B, and 72B scales.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 基线涵盖强化学习方法、免训练方法、闭源模型和开源通用 LVLM。DeepScan 以 BLIP-ITM base 为搜索专家、LangSAM 为视觉专家，默认候选数 $k=10$；评估主干包括 LLaVA-1.5-7B、Qwen2-VL-7B，以及 7B、32B、72B 三种规模的 Qwen2.5-VL。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The LVLM first classifies whether a question involves a single object or multiple objects. Patch size is set dynamically to $576\times576$ for single-object scenes and $768\times768$ for multi-object scenes. Main experiments run on four NVIDIA L20 GPUs; detailed hyperparameters are given in the supplement.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> LVLM 先判断问题涉及单对象还是多对象；单对象场景使用 $576\times576$ 图块，多对象场景使用 $768\times768$ 图块。主实验在 4 张 NVIDIA L20 GPU 上完成，详细超参数见补充材料。

### Table 2. TreeBench 上的总体与细分任务结果

![Table 2](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table2.png)

**Caption:** Comparison with state-of-the-art alternatives on TreeBench. Baselines use Qwen2.5-VL-7B; RL-based methods are shaded; dagger results are self-collected.

**Caption[CN]:** TreeBench 上与先进方法的比较。基线以 Qwen2.5-VL-7B 为主干；灰色为强化学习方法；† 表示作者自行复现。

**Reading note:** DeepScan 的优势主要来自感知与定位质量（mIoU 42.5），而不是每个二阶推理子项都大幅领先；作者据此提出“RL 更像在偏置感知行为，而非根本增强推理”的解释。

### 4.2 Main Results

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> On fine-grained visual understanding, DeepScan improves vanilla Qwen2.5-VL-7B across all benchmarks, including a 16.3-point overall gain on V*. It surpasses several 70B general models on perception subsets and outperforms all training-free baselines. Relative to DyFo, overall gains are 6.3, 3.6, and 2.6 points on V*, HR-Bench-4K, and HR-Bench-8K, respectively. It remains competitive with RL-based methods without fine-tuning the LVLM.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在细粒度视觉理解上，DeepScan 在全部基准上都显著增强原始 Qwen2.5-VL-7B，其中 V* 总体提升 16.3 个百分点；它在感知子任务上超过多个 70B 通用模型，并优于所有免训练基线。与 DyFo 相比，V*、HR-Bench-4K、HR-Bench-8K 的总体增益分别为 6.3、3.6、2.6 个百分点，且无需微调 LVLM 即可与强化学习方法竞争。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> On TreeBench, RL-based and training-free methods are broadly comparable. RL methods lead on complex perception tasks such as physical state and OCR but provide small gains on second-order reasoning tasks. The authors hypothesize that RL biases LVLMs toward perception behavior rather than fundamentally strengthening visual reasoning. DeepScan exceeds DeepEyes, PixelReasoner, and TreeVGR by 7.3, 1.6, and 5.5 mIoU, and by 5.0, 3.5, and 1.5 points in overall score.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在 TreeBench 上，强化学习与免训练方法总体接近。强化学习在物理状态、OCR 等复杂感知任务上占优，但在二阶推理任务上的收益较小。作者由此推测，RL 主要让 LVLM 更偏向感知行为，而非从根本上增强视觉推理。DeepScan 相比 DeepEyes、PixelReasoner、TreeVGR 的 mIoU 分别高 7.3、1.6、5.5，整体分数分别高 5.0、3.5、1.5 个百分点。

### Fig. 7. 跨 LVLM 主干的组件消融

![Fig. 7](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig7.png)

**Caption:** Ablations of DeepScan across LVLMs on V*. The y-axis is average performance, the x-axis is latency, and shaded regions show deviation across subsets.

**Caption[CN]:** DeepScan 在不同 LVLM 上的消融。纵轴为平均性能，横轴为时延，阴影表示子集间的性能偏差。

**Reading note:** 分层扫描是主要增益来源，再聚焦进一步提升；这种顺序在 LLaVA、Qwen2 与不同规模 Qwen2.5-VL 上保持一致。

### 4.3 Ablation Study

### Table 3. 外部专家规模消融

![Table 3](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table3.png)

**Caption:** Ablation of external experts on V*. Memory is the footprint of each variant; time is average per-sample latency.

**Caption[CN]:** V* 上外部专家消融。Mem 为显存占用，Time 为平均单样本推理时延。

**Reading note:** 更大的 BLIP-ITM 或 LangSAM 并未带来稳定收益，说明主要贡献来自流程设计而非堆大专家。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Across architectures and scales, all three stages contribute. Hierarchical Scanning is the main driver, Refocusing adds further gains while maintaining a favorable performance-latency trade-off, and Evidence-Enhanced Reasoning contributes additional improvements with negligible overhead. Expert size has little effect on performance, memory, or latency.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 三个阶段在不同架构、不同规模下均有贡献：分层扫描是主要驱动力；再聚焦在保持较好性能—时延权衡的同时继续增益；证据增强推理以几乎可忽略的额外开销进一步提升。专家模型大小对性能、显存和时延影响都较小。

### Table 4. 分层扫描与形态学后处理消融

![Table 4](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table4.png)

**Caption:** Ablation of Hierarchical Scanning on V*.

**Caption[CN]:** V* 上分层扫描消融。

**Reading note:** 相比检测式落地，分层扫描把总体分数从 82.2 提到 90.6；去掉后处理不仅降到 87.4，时延还从 24.5 秒升至 32.1 秒，印证“修掩码也能省计算”。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Hierarchical Scanning substantially outperforms the detection-based grounding used in DyFo, particularly on Attribute. Morphological post-processing fills mask holes, improves accuracy, and accelerates inference by preventing repeated processing of the same evidence.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 分层扫描明显优于 DyFo 使用的检测式落地，在属性子集上尤其突出。形态学后处理填补掩码孔洞，不仅提高准确率，也通过防止同一证据被重复处理而加速推理。

### Table 5. 点代理类型与图块大小消融

![Table 5](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table5.png)

**Caption:** Ablation of Local Cue Exploration on V*. Left: proxy type, where S and T denote semantic and topological information. Right: patch size for single- and multi-object scenes.

**Caption[CN]:** V* 上局部线索探索消融。左：点代理类型，S/T 表示语义/拓扑信息；右：单对象与多对象场景的图块大小。

**Reading note:** 质心可能落在 U 形线索之外；注意峰与 Chebyshev 中心各有优势，式 (5) 的语义×几何融合最好。单对象适合小块，多对象需要较大块保留关系。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Centroid proxies can lie outside U-shaped cues. Attention peaks and Chebyshev centers offer complementary gains, while the combined semantic-geometric proxy in Eq. (5) performs best. Smaller patches suppress context more effectively in single-object scenes; larger patches are better for multi-object scenes because spatial relations require context.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 质心代理可能落到 U 形线索之外。注意峰和 Chebyshev 中心分别在不同场景中占优，而式 (5) 融合语义与几何后最好。单对象场景中小图块更能抑制上下文；多对象场景则需要较大图块保留空间关系。

### Fig. 8. Zoom-Out 尺度消融

![Fig. 8](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig8.png)

**Caption:** Ablation of the Zoom-Out scale on V*. The left y-axis is evidence-detection Hit@1; the right y-axis is DeepScan accuracy.

**Caption[CN]:** V* 上 Zoom-Out 尺度消融。左纵轴是证据检测 Hit@1，右纵轴是 DeepScan 准确率。

**Reading note:** 适度放大能补回上下文，过大则重新引入噪声；直接属性任务因初始视图更小，对 Zoom-Out 的容忍范围更大。

### Table 6. 动作集合与搜索空间消融

![Table 6](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table6.png)

**Caption:** Left: effects of Zoom-In and Zoom-Out actions. Right: search length under MCTS, A*, and the proposed search-space design.

**Caption[CN]:** 左：Zoom-In 与 Zoom-Out 动作效果；右：MCTS、A* 与本文搜索空间设计的搜索长度。

**Reading note:** 两个动作缺一不可；在相同扩展预算下，四状态搜索空间比 MCTS/A* 更快到达 oracle 最优状态。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Refocusing requires both Zoom-In and Zoom-Out. Under the same depth-2 expansion budget, the proposed four-state space reaches the oracle-optimal state in fewer expansions than MCTS and A*, supporting both the completeness assumptions and the efficiency of the selection policy. A moderate Zoom-Out scale improves evidence Hit@1 and task accuracy; excessive expansion reintroduces noisy context.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 再聚焦同时需要 Zoom-In 和 Zoom-Out。在相同的深度 2 扩展预算下，本文四状态空间比 MCTS 与 A* 用更少扩展即可到达 oracle 最优状态，支持其搜索完备性假设与选择策略效率。适中的 Zoom-Out 能提高证据 Hit@1 和任务准确率，过度扩大则会重新引入噪声。

### 4.4 In-depth Analysis

### Fig. 9. V* 与 TreeBench 案例对比

![Fig. 9](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig9.png)

**Caption:** Case study of grounding results and model responses of GPT-4o, DyFo, and DeepScan. Panels (a-b) are from V*; panels (c-d) are from TreeBench. Correct and incorrect responses are highlighted in blue and red; ground truth, DyFo evidence, and DeepScan evidence use white, red, and blue boxes.

**Caption[CN]:** GPT-4o、DyFo 与 DeepScan 的落地结果和回答案例。(a-b) 来自 V*，(c-d) 来自 TreeBench。蓝/红文字表示正确/错误回答，白/红/蓝框分别表示真值、DyFo 证据与 DeepScan 证据。

**Reading note:** 四个案例覆盖属性、颜色、相对方向与文字识别；DeepScan 的优势首先是“框对了”，然后才是“答对了”。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In qualitative cases, GPT-4o and DyFo suffer from attention drift, producing mis-localization and incorrect answers, whereas DeepScan localizes the evidence and produces interpretable answers. It also grounds ultra-subtle targets with area below 1‰ and handles long, compositional TreeBench questions.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在案例中，GPT-4o 与 DyFo 会因注意力漂移而错定位、错回答；DeepScan 则先找准证据，再给出可解释答案。它还能定位面积低于 1‰ 的极细小目标，并处理 TreeBench 中较长、组合性更强的问题。

### Fig. 10. 一次性定位与自底向上定位的注意图

![Fig. 10](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig10.png)

**Caption:** Qualitative analysis of grounding paradigms using the search expert's attention map for Fig. 9(a).

**Caption[CN]:** 使用图 9(a) 中搜索专家注意图，对两类落地范式进行定性分析。

**Reading note:** 一次性定位把注意力漂移到更显著的“路牌”；图块内探索则先压低背景，再与真正的骑行者箱子对齐。

### Table 7. 一次性与自底向上定位的定量比较

![Table 7](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table7.png)

**Caption:** Quantitative comparison of one-shot and bottom-up localization on V*.

**Caption[CN]:** V* 上一次性定位与自底向上定位的定量比较。

**Reading note:** 自底向上定位以 4.1 秒额外时延换取 6.8 个总体百分点，属性子集提升 9.5 个百分点。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The one-shot variant exhibits errors similar to DyFo even though the experts differ, suggesting that attention sink and drift are paradigm-level problems. Bottom-up localization suppresses distractions and aligns attention with the correct target. Quantitatively, it improves V* from 83.8 to 90.6, with comparable numbers of LVLM judgments because evidence candidates are filtered before evaluation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 尽管外部专家不同，一次性变体仍出现与 DyFo 相似的错误，说明注意力汇聚与漂移更像范式层问题。自底向上定位能抑制干扰并把注意力拉回正确目标；定量上，V* 从 83.8 提升到 90.6。由于证据候选会先过滤，两种范式的 LVLM 判断次数大致相当。

### Fig. 11. 落地精度对感知与空间推理的影响

![Fig. 11](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig11.png)

**Caption:** Performance of the Qwen2.5-VL series under varying grounding precision, measured by IoU, on V*.

**Caption[CN]:** V* 上 Qwen2.5-VL 系列在不同落地精度（以 IoU 衡量）下的性能。

**Reading note:** 裁剪越准并非越好：过度 Zoom-In 会删除必要关系语境。模型扩展对空间关系推理的帮助显著大于对直接属性感知的帮助。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> More aggressive grounding is not always better. Raising IoU toward 1 can remove essential context and degrade reasoning; the reward in Eq. (11) therefore combines size regularization with LVLM completeness feedback. Under precise grounding, perception performance converges across model scales, while spatial reasoning gaps remain. This suggests using a small LVLM for evidence judgment and reserving a large LVLM for Evidence-Enhanced Reasoning.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 落地更激进不一定更好。把 IoU 推近 1 可能删除必要上下文并损害推理，因此式 (11) 将面积正则与 LVLM 完整性反馈结合。精确落地下，不同规模模型的感知性能趋于收敛，空间推理差距却仍明显；这提示可以用小 LVLM 判断证据，把大 LVLM 留给最终的证据增强推理。

## 5. Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> DeepScan is a training-free framework for visually grounded reasoning that explicitly localizes, recalibrates, and integrates evidence before answering. Bottom-up Hierarchical Scanning mitigates noisy context and localizes critical content; Refocusing optimizes the evidence view; and experiments show improvements across visual tasks, LVLM architectures, and parameter scales. Ablations and analyses further characterize where the gains arise.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> DeepScan 是一个免训练视觉落地推理框架，在回答前显式定位、校准并整合证据。自底向上的分层扫描减轻噪声上下文并定位关键内容，再聚焦优化证据视图；实验显示它能跨任务、跨 LVLM 架构与参数规模稳定提升。消融与深入分析进一步解释了增益来源。

## Acknowledgments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This work was supported by the National Natural Science Foundation of China (62176091) and the Natural Science Foundation of Chongqing (CSTB2024NSCQ-MSX0877).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本研究得到国家自然科学基金（62176091）和重庆市自然科学基金（CSTB2024NSCQ-MSX0877）资助。

## Supplementary Material

### A. Discussions

### Fig. 12. 落地失败案例

![Fig. 12](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig12.png)

**Caption:** Case study of grounding failure.

**Caption[CN]:** 落地失败案例。

**Reading note:** 多个外观相似对象同时留在证据邻域时，专家可能提出错误候选，LVLM 也可能把错误候选误判为有效证据，错误会沿“定位—回答”链传播。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> DeepScan failures mainly fall into two categories. In grounding failure, multiple visually similar objects remain in the evidence neighborhood; experts may propose the wrong object, and the LVLM may accept it, leading to an answer grounded in incorrect evidence.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> DeepScan 的失败主要分两类。第一类是落地失败：证据邻域中仍有多个外观相似对象，专家可能提出错误对象，LVLM 又可能把它接受为证据，最终得到“有证据但证据错了”的答案。

### Fig. 13. 多证据空间推理失败案例

![Fig. 13](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig13.png)

**Caption:** Case study of reasoning failure.

**Caption[CN]:** 推理失败案例。

**Reading note:** 四个目标都被找到了，但最小包围框把大面积无关区域也并入视图；这说明正确定位并不足以保证正确关系推理。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In reasoning failure, spatial-relation questions require multiple pieces of evidence. DeepScan forms a merged view using the minimum box enclosing all localized evidence. When evidence is far apart, this crop includes substantial inter-evidence noise, possibly containing distractors that conflict with the answer. A promising direction is generative composition that reassembles localized evidence into a compact layout while preserving attributes and spatial relations.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 第二类是推理失败：空间关系问题需要多处证据，DeepScan 当前用包围全部证据的最小框形成合并视图。若证据相距很远，裁剪会夹带大量证据间噪声，甚至包含与正确答案冲突的干扰物。作者建议未来使用生成式合成，把已定位证据重排为紧凑布局，同时保留属性与空间关系。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> DeepScan has higher inference latency than one-shot evidence detection. The trade-off can be controlled through patch size and proposal count, but the current implementation uses relatively small patches even for easy scenes with salient evidence. Future work should adapt patch size within each grounding process using stronger priors such as evidence saliency.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 与一次性证据检测相比，DeepScan 推理时延更高。图块大小和候选数量可调节性能—效率权衡，但当前实现即使对证据显著的简单场景也使用较小图块，造成浪费。未来可利用证据显著性等更强先验，在每次落地过程中自适应分配图块大小。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> By tying answers to concrete evidence and making context extent explicit, DeepScan may benefit GUI agents, embodied manipulation, and autonomous driving under clutter and occlusion. Risks include inherited biases from LVLMs and experts, automation errors in safety-critical settings, and extra test-time compute that may limit edge or mobile deployment.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> DeepScan 把答案绑定到具体证据，并显式控制上下文范围，因此可能用于 GUI 智能体、具身操作和遮挡环境下的自动驾驶。风险包括继承 LVLM 与视觉专家的偏见、在安全关键场景中的自动化错误，以及额外测试时计算限制边缘或移动部署。

### B. Methodological Details

#### Prompts. 原始提示词

![Prompt templates](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/prompts.png)

**Caption:** System prompt and three user prompts for evidence decomposition, evidence judgment, and view-completeness justification.

**Caption[CN]:** 系统提示词，以及用于证据分解、证据判断和视图完整性判断的三个用户提示词。

**Reading note:** Prompt 1 提取问题中的对象列表并决定图块大小；Prompt 2 判断候选证据能否回答问题；Prompt 3 判断视图是否完整包含所有目标。三个判断都很短，最终推理才使用较长输出。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Evidence Decomposition asks the LVLM to list objects mentioned in the question. Evidence Judgment asks whether a candidate image contains clues sufficient to answer the question and requests a justification. View Completeness Justification asks whether every target object is fully contained within the frame, with bounding boxes or region descriptions for present objects and names of missing objects.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 证据分解要求 LVLM 列出问题中提到的对象；证据判断要求模型判断候选图像是否包含足够线索，并给出理由；视图完整性判断要求确认所有目标是否完整位于画面内，若在则给出框或区域描述，若不在则列出缺失对象。

#### Algorithm 1. 带加速的分层扫描

![Algorithm 1](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/algorithm1.png)

**Caption:** Pseudocode for Hierarchical Scanning with candidate filtering, morphological post-processing, overlap removal, and LVLM evidence judgment.

**Caption[CN]:** 分层扫描伪代码：包含候选过滤、形态学后处理、重叠移除和 LVLM 证据判断。

**Reading note:** 算法先批量扫描图块，再把所有候选恢复到原图、去重并按面积保留最小的 $k$ 个，最后才调用 LVLM 做证据判断。

#### Algorithm 2. 再聚焦

![Algorithm 2](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/algorithm2.png)

**Caption:** Pseudocode for Refocusing over the four-state view set.

**Caption[CN]:** 在四状态视图集合上执行再聚焦的伪代码。

**Reading note:** 四个视图分别由初始合并证据、Zoom-In、Zoom-Out、Zoom-Out 后再 Zoom-In 构成；不完整视图奖励为 0，完整视图按反面积排序。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The noisy-cue area threshold is 50 pixels. Morphological processing uses a $5\times5$ flat kernel and a disk radius of 20. Similar evidence is filtered at IoU 0.3. The default candidate count is $k=10$. Detection boxes used by Refocusing are padded by 28 pixels on all sides, and Zoom-Out scale is 1.5. Maximum output length is 50 tokens for the three auxiliary prompts and 1024 for final reasoning. Inference uses temperature 0 and random seed 13; beam search and top-$k$ sampling are disabled.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 噪声线索面积阈值为 50 像素；形态学处理使用 $5\times5$ 平坦核和半径 20 的圆盘；相似证据以 IoU 0.3 过滤；默认候选数 $k=10$。再聚焦把检测框四周各扩 28 像素，Zoom-Out 尺度为 1.5。三个辅助提示最大输出 50 token，最终推理 1024 token；温度为 0、随机种子为 13，默认关闭 beam search 与 top-$k$ 采样。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> In the pseudocode, Prompt1-3 instantiate the templates above; LIFTTOIMAGE maps patch coordinates to image coordinates; CLOSE and DILATE are morphological closing and dilation; and $\odot$ denotes element-wise multiplication.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 伪代码中的 Prompt1-3 对应上述模板；LIFTTOIMAGE 把图块坐标映射到原图坐标；CLOSE、DILATE 分别表示形态学闭运算与膨胀；$\odot$ 表示逐元素乘法。

### C. Additional Results

### Table 8. 视觉落地推理方法的设计维度比较

![Table 8](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table8.png)

**Caption:** Comparison of DeepScan with existing visually grounded reasoning approaches in scalability, external experts, search strategy, grounding paradigm, evidence granularity, and latency.

**Caption[CN]:** 从可扩展性、外部专家、搜索策略、落地范式、证据粒度与时延等维度比较 DeepScan 和现有视觉落地推理方法。

**Reading note:** DeepScan 的独特组合是：易扩展 + 外部专家 + 分层扫描/再聚焦 + 自底向上 + 混合粒度；代价是时延仍被归为 High。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Learned localization modules and RL decision controllers generally require retraining when the LVLM backbone is upgraded. DyFo and ZoomRefine scale more readily, but retain coarse-to-fine grounding. DeepScan is also easy to scale and introduces bottom-up hierarchical scanning, context-optimal refocusing, and hybrid evidence memory.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 带学习式定位模块或强化学习决策控制器的方法，升级 LVLM 主干时通常需要重训。DyFo、ZoomRefine 更容易扩展，但仍采用由粗到细落地。DeepScan 同样易扩展，并引入自底向上分层扫描、上下文最优再聚焦和混合证据记忆。

### Table 9. V* 上的补充对比

![Table 9](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table9.png)

**Caption:** Additional V* results. Dagger results were reproduced with official code.

**Caption[CN]:** V* 补充结果。带 † 的结果使用官方代码复现。

**Reading note:** $k=\infty$ 只比 $k=10$ 高 0.5 个百分点；72B 主干下为 94.2%，空间子集为 93.4%，说明扩模型主要补强关系推理。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> DeepScan reaches 90.6% with $k=10$ and 91.1% with $k=\infty$ on Qwen2.5-VL-7B, surpassing ZoomRefine, DyFo, and several RL-based methods. With Qwen2.5-VL-72B it reaches 94.2% overall and 93.4% on Spatial, 9.4 points above the vanilla 72B model overall.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 基于 Qwen2.5-VL-7B 时，DeepScan 在 $k=10$ 与 $k=\infty$ 下分别达到 90.6% 和 91.1%，超过 ZoomRefine、DyFo 以及多种强化学习方法。使用 Qwen2.5-VL-72B 时，总体达到 94.2%，空间子集 93.4%，总体比原始 72B 模型高 9.4 个百分点。

### Fig. 14. 更多注意力汇聚/漂移案例

![Fig. 14](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/fig14.png)

**Caption:** Qualitative analysis of grounding paradigms with the search expert's attention map.

**Caption[CN]:** 使用搜索专家注意图对落地范式进行更多定性分析。

**Reading note:** 属性问题中自顶向下方法常锁定全局显著区域；关系问题中它常只命中两个目标之一。自底向上扫描分别表现为“Align to”与“Align to both targets”。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> For direct attributes, one-shot grounding often locks onto globally salient but irrelevant regions. Bottom-up local cue exploration recenters attention on the true evidence. For spatial relations, one-shot grounding often misses one of the two targets, while bottom-up scanning progressively aligns to both; Refocusing then retains the surrounding context needed for the relation.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在直接属性问题中，一次性落地常锁定全局显著但无关区域；自底向上局部探索会把注意力重新拉回真正证据。在空间关系问题中，一次性落地常漏掉两个目标之一，而自底向上扫描逐步对齐两者；再聚焦随后保留关系判断所需的周边语境。

### Table 10. 工程优化后的性能—效率比较

![Table 10](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/table10.png)

**Caption:** Performance-efficiency comparison on V*. End-to-end latency includes evidence decomposition, expert calls, post-processing, and evidence judgments.

**Caption[CN]:** V* 上性能—效率比较。端到端时延包含证据分解、专家调用、后处理与证据判断等全部辅助步骤。

**Reading note:** 优化后 DeepScan 为 90.1%、8.4k token、3.1 秒；比 DeepEyes 快约 2.2 倍且 token 少约 35%，但仍比原始 LVLM 慢得多。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The original nested-loop implementation under Hugging Face Transformers suffers from sequential computation and frequent communication between the visual expert and LVLM. Because DeepScan uses deterministic rather than MCTS sampling, attention-map computation, top-$k$ judgments, view justification, and post-processing can be batched or parallelized. Migrating to vLLM with PagedAttention and optimized CUDA kernels yields about an $8\times$ speedup.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 原始 Hugging Face Transformers 实现采用嵌套循环，受顺序计算以及视觉专家与 LVLM 频繁通信限制。DeepScan 使用确定性采样而非 MCTS，因此注意图计算、top-$k$ 判断、视图完整性判断和后处理均可批处理或并行化；迁移到带 PagedAttention 和优化 CUDA 内核的 vLLM 后，获得约 $8\times$ 加速。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> After optimization, DeepScan reaches 90.1% with 3.1-second latency and 8.4k tokens, versus DeepEyes at 89.0%, 6.9 seconds, and 13k tokens. It is 0.7 seconds slower than DyFo but 6.3 points more accurate; Hierarchical Scan alone is both faster and more accurate than DyFo. The authors argue that deterministic compute scaling to maximize local visual signal-to-noise ratio is more efficient than heuristic search-tree expansion.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 优化后，DeepScan 以 3.1 秒和 8.4k token 达到 90.1%；DeepEyes 为 6.9 秒、13k token、89.0%。它比 DyFo 慢 0.7 秒但准确率高 6.3 个百分点，且仅分层扫描阶段就比 DyFo 更快、更准。作者据此主张：以确定性计算提升局部视觉信噪比，比启发式扩展搜索树更高效。

### D. Example Model Outputs

#### Example 1 setup and GPT-4o output

![Example 1 GPT-4o](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/example1_gpt4o.png)

**Caption:** The target cap occupies only 0.004% of the image. GPT-4o fails to see the man and refuses the multiple-choice answer.

**Caption[CN]:** 目标帽子仅占图像 0.004%。GPT-4o 未发现人物，因而拒绝在选项中作答。

#### Qwen3-VL-235B-A22B output

![Example 1 Qwen3](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/example1_qwen3.png)

**Caption:** Qwen3-VL-235B-A22B similarly concludes that no man is present.

**Caption[CN]:** Qwen3-VL-235B-A22B 同样判断图中没有人物。

#### ZoomRefine, DyFo, and DeepScan comparison

![Example 1 comparison](Reasoning/TrainingFree/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/assets/example1_comparison.png)

**Caption:** ZoomRefine returns N/A; DyFo grounds the wrong region and answers black; DeepScan first scans the tiny person, refocuses on the cap, and answers white correctly.

**Caption[CN]:** ZoomRefine 返回 N/A；DyFo 定位到错误区域并回答黑色；DeepScan 先扫描到极小人物，再聚焦到帽子，正确回答白色。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The supplement compares DeepScan with GPT-5, GPT-4o, Qwen3-VL-235B-A22B, ZoomRefine, and DyFo. For fair training-free comparison, ZoomRefine, DyFo, and DeepScan all use Qwen2.5-VL-72B. The examples are intended to show that evidence localization, rather than backbone size alone, determines whether an answer is visually grounded.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 补充材料将 DeepScan 与 GPT-5、GPT-4o、Qwen3-VL-235B-A22B、ZoomRefine、DyFo 比较；为保证免训练方法公平，后三者均使用 Qwen2.5-VL-72B。案例要说明的是：答案能否真正基于视觉证据，取决于证据定位，而不仅是主干规模。

## Critical Reading Notes

1. **最强证据是范式消融，而不只是 SOTA 数字。** 一次性定位与自底向上定位在相近判断次数下相差 6.8 个 V* 百分点；跨搜索专家仍复现同类注意力漂移，这更直接支持论文的核心机制主张。
2. **分层扫描负责“找到”，再聚焦负责“保留恰当上下文”。** 两者解决的问题不同。过度裁剪会提高局部 IoU，却可能删掉空间关系证据，因此不能把该方法简化为“不断放大图像”。
3. **混合粒度是合理但尚未充分隔离的设计。** 细粒度图用于属性、粗粒度图用于关系的逻辑清楚；不过论文没有给出足够细的记忆组成消融来量化每种视图的独立贡献。
4. **V* 的高增益与任务特征高度相关。** V* 目标极小，正是局部扫描最有优势的场景。TreeBench 上总体增益更温和，且若干二阶推理子任务并未全面领先。
5. **时延结论依赖工程实现。** 补充材料中的 vLLM 批处理版本比正文旧实现快约 8 倍，但仍需要 4×L20；跨硬件、不同并发度和真实在线负载下的收益尚待验证。
6. **当前主要失败点已被作者清楚识别。** 相似对象会导致错误证据被接受；多证据相距很远时，最小包围框会引入大面积噪声。后者提示下一步可以研究“保持几何关系的证据重排/合成”。
7. **可复现性关注项。** 论文给出了关键提示词、阈值、随机种子和伪代码，但正文 PDF 中 Otsu 的引用显示为 `[?]`，且代码在论文版本中仅承诺将开源；完整复现仍依赖代码发布与数据评测脚本。

## References

以下按原论文编号保留参考文献的作者、题名和主要出处；文献页码型反向引用数字已省略。

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
