h# A4-Agent: An Agentic Framework for Zero-Shot Affordance Reasoning

## Metadata

| Field | Value |
|---|---|
| Title | A4-Agent: An Agentic Framework for Zero-Shot Affordance Reasoning |
| Authors | Zixin Zhang, Kanghao Chen, Hanqing Wang, Hongfei Zhang, Harold H. Chen, Chenfei Liao, Litao Guo, Ying-Cong Chen |
| Source | arXiv:2512.14442v1 [cs.CV], 16 Dec 2025 |
| Paper type | Conference-style methods paper / zero-shot affordance reasoning framework |
| Core task | Given an image and task instruction, predict actionable object regions as masks, boxes, or key points |
| Reader mode | Full-paper Chinese-English side-by-side reader with figure/table assets |

## Page / Section Index

| Pages | Sections |
|---|---|
| 1 | Title, Fig. 1, Abstract, Introduction begins |
| 2 | Introduction, Related Work |
| 3 | Fig. 2, Related Work, Motivation |
| 4 | Fig. 3, Motivation, Problem Definition, Framework Overview, Dreamer begins |
| 5 | Fig. 4, Dreamer, Thinker, Spotter begins |
| 6 | Tables 1-2, Spotter, Experimental Settings, Datasets, Quantitative Results begins |
| 7 | Fig. 5, Table 3, Quantitative Results, Open-world Qualitative Results, Ablation begins |
| 8 | Fig. 6, Tables 4-5, Ablation Study, Conclusion |
| 9-11 | References |
| 12 | Supplement: implementation details, baseline categories, metrics, Dreamer prompt |
| 13 | Supplement: Thinker prompt, exploratory experiment, Table 6, intermediate-results overview |
| 14-19 | Supplement: Figs. 8-13 full intermediate demonstrations |

## Terminology Ledger

| Canonical term | 中文译法 | Notes |
|---|---|---|
| affordance / affordance prediction | 可供性 / 可供性预测 | 指对象可支持某种行动的部位或区域；本文具体是按任务指令预测可操作区域 |
| actionable region / affordance region | 可操作区域 / 可供性区域 | 最终通常以 segmentation mask 为主要表示 |
| zero-shot | 零样本 | 论文强调没有在目标 affordance 数据集上训练或微调 |
| training-free | 免训练 | 指测试时编排预训练基础模型，而非端到端训练新模型 |
| reasoning | 高层语义推理 | 由 Thinker/VLM 负责决定“操作哪个部件” |
| grounding | 低层视觉定位 / 视觉落地 | 由 Spotter/视觉基础模型负责把语义部件落到像素区域 |
| Dreamer | Dreamer（想象器） | 用图像生成/编辑模型显式想象交互状态 |
| Thinker | Thinker（推理器） | 用 VLM 比较原图与想象图，输出结构化 object part |
| Spotter | Spotter（定位器） | 用 Rex-Omni + SAM2 做 coarse-to-fine 定位与分割 |
| Rex-Omni | Rex-Omni | 开放词表检测器，输出 boxes/key points |
| SAM2 | SAM2 | Segment Anything Model 2，用于根据 boxes/key points 生成 masks |
| gIoU / cIoU | generalized IoU / cumulative IoU | 本文的主要分割评价指标 |
| P@50 / P@50:95 | IoU 阈值精度指标 | P@50 是 IoU > 0.5 的比例；P@50:95 是 0.5-0.95 多阈值平均 |

## Figure 1. A4-Agent 总览与零样本性能

![Fig. 1](3d%20agent/A4-Agent%20An%20Agentic%20Framework%20for%20Zero-Shot%20Affordance%20Reasoning/assets/fig1_overview.png)

**Caption:** Left: Overview of A4-Agent, an affordance-centric vision-language agent that predicts actionable regions based on complex task instruction. Given an observed object, A4-Agent integrates image generation, object detection, segmentation, and a vision-language model to imagine plausible interactions and localize the proper action-specific part. Right: A4-Agent achieves state-of-the-art performance across multiple benchmarks with zero-shot setting, surpassing baseline models that are specifically trained for affordance prediction task.

**Caption[CN]:** 左：A4-Agent 的整体概览。它是一个以可供性为中心的视觉语言智能体，可以根据复杂任务指令预测可操作区域。给定观察到的对象，A4-Agent 结合图像生成、目标检测、分割和视觉语言模型，先想象可能的交互，再定位与动作相关的正确部件。右：A4-Agent 在零样本设置下跨多个基准达到最先进表现，超过了专门为可供性预测训练的基线模型。

**Reading note:** Fig. 1 把论文的核心立场压缩得很清楚：不是训练一个“全能模型”，而是把 imagination、reasoning、detection、segmentation 串成一个可替换的 agentic pipeline。

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Affordance prediction, which identifies interaction regions on objects based on language instructions, is critical for embodied AI. Prevailing end-to-end models couple high-level reasoning and low-level grounding into a single monolithic pipeline and rely on training over annotated datasets, which leads to poor generalization on novel objects and unseen environments. In this paper, we move beyond this paradigm by proposing A4-Agent, a training-free agentic framework that decouples affordance prediction into a three-stage pipeline. Our framework coordinates specialized foundation models at test time: (1) a Dreamer that employs generative models to visualize how an interaction would look; (2) a Thinker that utilizes large vision-language models to decide what object part to interact with; and (3) a Spotter that orchestrates vision foundation models to precisely locate where the interaction area is. By leveraging the complementary strengths of pre-trained models without any task-specific fine-tuning, our zero-shot framework significantly outperforms state-of-the-art supervised methods across multiple benchmarks and demonstrates robust generalization to real-world settings.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 可供性预测根据语言指令识别对象上的交互区域，是具身智能中的关键能力。现有主流端到端模型通常把高层推理和低层视觉定位耦合进单一整体流水线，并依赖带标注数据集训练，因此在新对象和未见环境中泛化较差。本文提出 A4-Agent，跳出这一范式：它是一个免训练的 agentic 框架，把可供性预测拆成三个阶段。该框架在测试时协调专门的基础模型：（1）Dreamer 使用生成模型想象交互会是什么样子；（2）Thinker 使用大型视觉语言模型判断应该与对象的哪个部件交互；（3）Spotter 编排视觉基础模型，精确定位交互区域。由于不进行任务特定微调，而是利用预训练模型的互补优势，这一零样本框架在多个基准上显著超过监督式 SOTA 方法，并展示了对真实世界场景的稳健泛化。

## 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Affordance, a concept describing the action possibilities that objects offer to agents, serves as a crucial bridge between visual perception and physical interaction. In embodied AI and robotic manipulation, affordance prediction aims to identify specific object regions that enable task-relevant interactions from natural language instructions. For instance, given the instruction “open the refrigerator,” a model must recognize the handle as the actionable region. This capability is fundamental to task planning [21], robotic grasping [2, 17], and human-robot collaboration [4, 13], where successful execution depends not only on knowing what objects are present, but also where and how to interact with them.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 可供性描述的是对象向智能体提供的行动可能性，是视觉感知与物理交互之间的关键桥梁。在具身智能和机器人操作中，可供性预测旨在根据自然语言指令识别对象上支持任务相关交互的具体区域。例如，给定“打开冰箱”的指令，模型必须识别门把手是可操作区域。这种能力对任务规划 [21]、机器人抓取 [2, 17] 和人机协作 [4, 13] 都很基础，因为成功执行任务不仅需要知道场景中有什么对象，还要知道在哪里、以什么方式与它们交互。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Affordance prediction requires two complementary capabilities: high-level reasoning, which interprets natural-language instructions and identifies task-relevant object parts, and low-level grounding, which precisely localizes these parts in pixel coordinates. Traditional approaches [24, 30, 31] mainly focused on grounding and treated the task as a regression problem: given an affordance type, the model predicts an affordance map. Such methods lack high-level reasoning and struggle with complex instructions. Recent works [36, 45, 49] incorporate LLMs or train unified models that perform both reasoning and grounding, but the tightly coupled design introduces trade-offs between reasoning and grounding, limited generalization, and reduced flexibility.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 可供性预测需要两种互补能力：一是高层推理，即理解自然语言指令并识别任务相关的对象部件；二是低层定位，即把这些部件精确落到像素坐标中。传统方法 [24, 30, 31] 主要关注定位，把任务当作回归问题：给定某种可供性类型，模型预测一张可供性图。这类方法缺少高层推理能力，因此难以处理复杂指令。近期工作 [36, 45, 49] 尝试引入 LLM，或训练同时承担推理和定位的统一模型，但这种强耦合设计带来了推理与定位之间的能力折中、泛化受限和灵活性下降。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The authors therefore ask whether entangling high-level reasoning and low-level grounding is truly the right path for affordance prediction. Their answer is A4-Agent, a preliminary exploration of an agentic framework that coordinates foundation models without task-specific training. The key insight is to decouple reasoning and grounding: Dreamer generates imagined interaction scenarios, Thinker uses VLMs to convert original and imagined images into structured textual descriptions of the target object part, and Spotter uses vision foundation models to localize the described part in the original image.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 因此，作者提出一个核心问题：把高层推理和低层定位纠缠在一起，真的是可供性预测的正确路径吗？他们给出的回答是 A4-Agent，这是一个通过协调基础模型、但不做任务特定训练的 agentic 框架。其关键洞见是将推理与定位解耦：Dreamer 生成想象中的交互场景；Thinker 用 VLM 把原图和想象图转化为目标对象部件的结构化文本描述；Spotter 再用视觉基础模型把该部件定位回原图。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> As shown in Fig. 1, A4-Agent significantly outperforms supervised state-of-the-art methods across multiple benchmarks despite using no task-specific training. The paper summarizes three contributions: introducing A4-Agent as a training-free framework with strong zero-shot generalization; validating a decoupled reasoning-grounding approach that allows specialized SOTA models to be integrated for each subtask; and proposing an imagination-assisted affordance reasoning paradigm that highlights the role of explicit visual imagination.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 如 Fig. 1 所示，A4-Agent 虽然没有进行任务特定训练，却在多个基准上显著超过监督式 SOTA 方法。论文总结了三点贡献：提出一个免训练且具有强零样本泛化能力的 A4-Agent 框架；验证将推理与定位解耦的可供性预测方法，使每个子任务都能接入对应的 SOTA 专门模型；提出“想象辅助”的可供性推理范式，强调显式视觉想象在推理过程中的关键作用。

## 2. Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Affordance learning originates from Gibson’s concept of action possibilities [12] and has inspired extensive work for robotic systems. Earlier approaches learned from human-object interaction images [11, 39, 53], human demonstration videos [32], 3D point clouds [9, 10, 34, 36, 54], or 3D Gaussian Splatting [47]. Recent MLLM-based methods such as AffordanceLLM [36] and Seqafford [54] introduce special tokens and map affordance regions to token embeddings for segmentation outputs. LISA [22] extends language-driven segmentation with reasoning, and Affordance-R1 [45] applies reinforcement learning to improve affordance reasoning and grounding. The authors argue, however, that most of these systems remain end-to-end trained and therefore inherit the reasoning-grounding trade-off.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 可供性学习源自 Gibson 关于“行动可能性”的概念 [12]，并启发了机器人系统中的大量研究。早期方法从人-物交互图像 [11, 39, 53]、人类示范视频 [32]、3D 点云 [9, 10, 34, 36, 54] 或 3D Gaussian Splatting [47] 中学习。近期 MLLM 方法如 AffordanceLLM [36] 和 Seqafford [54] 引入特殊 token，并把可供性区域映射到 token embedding，以输出分割结果。LISA [22] 将推理能力引入语言驱动分割，Affordance-R1 [45] 则用强化学习提升可供性推理和定位。但作者认为，这些系统大多仍采用端到端训练，因此继承了推理与定位之间的能力折中。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Multimodal large language models have shown strong visual understanding, generation, and reasoning capabilities [1, 26, 52]. Inference-time reasoning has been advanced by models such as OpenAI o1 [35] and DeepSeek-R1 [14], and related ideas have been extended to vision tasks [18, 28, 41]. Beyond text-based reasoning, some works use explicit visual imagination: VoT [50] introduces textual imagery representations, while generative-model-based methods [6, 8, 16, 23] create intermediate visuals to support reasoning. A4-Agent uses this line of thought but places it inside a modular affordance pipeline rather than inside a single end-to-end model.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 多模态大语言模型已经展示出强视觉理解、生成和推理能力 [1, 26, 52]。OpenAI o1 [35] 与 DeepSeek-R1 [14] 等模型推动了推理时扩展，相关思想也被扩展到视觉任务 [18, 28, 41]。除文本推理外，一些工作开始使用显式视觉想象：VoT [50] 引入文本化意象表征，基于生成模型的方法 [6, 8, 16, 23] 则生成中间视觉内容来辅助推理。A4-Agent 借鉴了这一思路，但将其放入模块化可供性流水线，而不是压进单一端到端模型。

## Figure 2. 推理与定位能力的错位

![Fig. 2](fig2_motivation_capabilities.png)

**Caption:** Vision Foundation Models are good at fine-grained grounding, but are poor at reasoning. Vision Language Models are good at reasoning, but are poor at visual grounding. Some works finetuned VLMs for better grounding ability, but both abilities are underwhelming.

**Caption[CN]:** 视觉基础模型擅长细粒度定位，但推理较弱；视觉语言模型擅长推理，但视觉定位较弱。一些工作通过微调 VLM 提升定位能力，但两种能力都不够理想。

**Reading note:** 这是全文最重要的动机图：它把“为什么要拆模块”讲成了能力边界问题，而不是单纯工程偏好。

## 3. Motivation

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Affordance prediction fundamentally requires high-level reasoning and low-level grounding. Specialized vision foundation models can localize fine-grained regions but lack the semantic understanding needed for complex task instructions. Recent MLLMs can reason impressively but often produce coarse or inaccurate spatial predictions, making them insufficient for precise affordance prediction.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 可供性预测本质上需要高层推理和低层定位。专门的视觉基础模型能够定位细粒度区域，却缺少理解复杂任务指令所需的语义能力。近期 MLLM 推理能力很强，但空间预测常常粗糙或不准确，因此无法单独满足精确可供性预测。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Existing systems attempt to solve this dichotomy through monolithic end-to-end models, usually by training MLLMs on visual grounding data such as bounding boxes, key points, and masks. The authors argue that this tightly coupled paradigm has four limitations: limited generalization because finite datasets cannot cover real-world diversity; capability trade-offs because reasoning and grounding objectives compete; poor flexibility because the full system must be retrained to upgrade components; and a gap to closed-source models because open-source checkpoint restrictions cap reasoning ability.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 现有系统通常用单体端到端模型解决这种二分问题，例如在 bounding boxes、key points、masks 等视觉定位数据上训练 MLLM。作者指出，这种强耦合范式有四个限制：有限数据集无法覆盖真实世界多样性，导致泛化有限；推理与定位目标相互竞争，造成能力折中；升级组件必须重训整个系统，灵活性差；由于管线受限于开源 checkpoint，难以利用最强闭源模型，推理能力上限受限。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The proposed alternative is to decouple reasoning and grounding into specialized, coordinated agents. The authors argue that affordance prediction is inherently multi-stage; rather than forcing one model to master every capability, each component should be independently designed with state-of-the-art foundation models and orchestrated at test time.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 作者提出的替代路线是：把推理与定位拆分为专门且协同的智能体。作者认为，可供性预测天然是多阶段任务；与其强迫一个模型掌握所有能力，不如用最先进的基础模型分别设计各个组件，并在测试时进行编排。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> This paradigm offers three advantages: training-free generalization by leveraging pre-trained models’ broad knowledge; modular specialization, where each component can exploit complementary strengths and be independently upgraded; and interpretable reasoning, where explicit intermediate steps make decisions transparent, debuggable, and easier to refine.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 这一范式带来三点优势：第一，利用预训练模型的广泛知识，实现免训练泛化；第二，模块化专长，每个组件都能发挥互补优势并独立升级；第三，可解释推理，显式中间步骤让决策过程透明、可调试，也更容易迭代优化。

## Figure 3. A4-Agent 三阶段流水线

![Fig. 3](fig3_a4_agent_pipeline.png)

**Caption:** The pipeline of our A4-Agent framework, which decouples affordance prediction into three stages. (1) Dreamer: Imagines the interaction by generating a simulated image. (2) Thinker: Reasons over the original and simulated images to produce a textual description of the actionable object part. (3) Spotter: Takes this description to locate the part with bounding boxes and keypoints, then refines them into a precise segmentation mask.

**Caption[CN]:** A4-Agent 的流水线将可供性预测拆成三阶段：（1）Dreamer：通过生成模拟图像来想象交互；（2）Thinker：基于原图和模拟图推理，生成可操作对象部件的文本描述；（3）Spotter：根据该描述用 bounding boxes 与 keypoints 定位部件，再细化为精确 segmentation mask。

**Reading note:** 这张图也暴露了框架的工程依赖：A4-Agent 的性能会随 GPT-4o、Qwen-Image、Rex-Omni、SAM2 等组件能力变化而变化。

## 4. A4-Agent: Agentic Affordance Reasoning

### 4.1. Problem Definition

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper formulates affordance prediction as a visual grounding problem conditioned on natural-language instructions. Given an image $I \in \mathbb{R}^{H \times W \times 3}$ and a task description $T$, such as “open the refrigerator,” the objective is to identify the affordance region $A_{\mathrm{ff}}$ that enables the specified interaction:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文将可供性预测表述为一个受自然语言指令条件约束的视觉定位问题。给定图像 $I \in \mathbb{R}^{H \times W \times 3}$ 和任务描述 $T$（例如“打开冰箱”），目标是识别能够完成指定交互的可供性区域 $A_{\mathrm{ff}}$：

$$
A_{\mathrm{ff}} = F(I,T).
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The affordance region can be represented as bounding boxes $\{B_i\}_{i=1}^{N}$, key points $\{P_i\}_{i=1}^{N}$, or segmentation masks $\{M_i\}_{i=1}^{N}$. Following recent work [45, 49], the authors use segmentation masks as the primary representation because they provide pixel-level precision.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 可供性区域可以表示为 bounding boxes $\{B_i\}_{i=1}^{N}$、key points $\{P_i\}_{i=1}^{N}$ 或 segmentation masks $\{M_i\}_{i=1}^{N}$。按照近期工作 [45, 49]，作者把 segmentation mask 作为主要表示，因为它具有像素级精度。

### 4.2. Framework Overview

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> A4-Agent is a training-free, agentic framework for zero-shot affordance prediction. Unlike end-to-end models that directly regress $(B,M)$ from $(I,T)$, A4-Agent first reasons about which object part requires interaction, then grounds that part in the image:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> A4-Agent 是一个用于零样本可供性预测的免训练 agentic 框架。不同于从 $(I,T)$ 直接回归 $(B,M)$ 的端到端模型，A4-Agent 先推理需要交互的对象部件，再把该部件定位到图像中：

$$
A_{\mathrm{ff}} = \mathrm{Ground}(\mathrm{Reason}(I,T)).
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The reasoning process has two steps: Dreamer imagines how the operation could be performed, and Thinker decides which part should be operated on. The grounding process is handled by Spotter, which first identifies broad regions through bounding boxes and key points, then refines them with a segmentation model to produce pixel-accurate masks.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 推理过程包含两步：Dreamer 想象操作如何发生；Thinker 判断应该操作哪个部件。定位过程由 Spotter 完成：它先用 bounding boxes 和 key points 找到粗略区域，再用分割模型细化，得到像素级精确的 mask。

### 4.3. Dreamer: Imagine how to Operate

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The Dreamer is motivated by a human-like process: when people reason about how to use a tool, they often mentally simulate the hand-object interaction and the broader usage scenario. Instead of relying only on text reasoning, A4-Agent first prompts an image-generation module to visualize a plausible interaction state, such as a hand grasping a handle or a door being opened, based on the observation $I$ and task $T$.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Dreamer 的动机来自一种类人的过程：人们推理如何使用工具时，常常会在心里模拟手与物体如何交互，以及更大的使用场景。因此，A4-Agent 不只依赖文本推理，而是先根据观测图像 $I$ 和任务 $T$，提示图像生成模块可视化一个合理交互状态，例如手抓住把手，或门被打开。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> To construct the image-editing prompt, A4-Agent queries a VLM with an instruction template applied to $(I,T)$:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 为了构造图像编辑 prompt，A4-Agent 使用作用于 $(I,T)$ 的指令模板来查询 VLM：

$$
T_{\mathrm{sim}} = \Phi_{\mathrm{VLM}}(I,T;\tau),
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Here $\Phi_{\mathrm{VLM}}$ denotes the VLM and $\tau$ is the instruction template. The template asks the model to output a short, visually actionable description that names the target object and functional part visible in $I$, specifies the minimal interaction/contact configuration, and avoids unsupported image attributes. The resulting prompt is concise and robust for image editing. The generative model $G$ then synthesizes an imagined interaction image:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 其中 $\Phi_{\mathrm{VLM}}$ 表示 VLM，$\tau$ 是指令模板。该模板要求模型输出一个简短、视觉上可执行的描述：它要命名 $I$ 中可见的目标对象及功能部件，指定最小交互/接触配置，并避免图像中没有支持的属性。得到的 prompt 适合图像编辑且较稳健。随后生成模型 $G$ 合成想象交互图像：

$$
I_{\mathrm{sim}} = G(I,T_{\mathrm{sim}}).
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The imagined image $I_{\mathrm{sim}}$ explicitly highlights where interaction should occur by depicting plausible contact and motion cues. This improves the success rate and interpretability of affordance reasoning, and it lets the system use the generative model’s priors about interaction states within the agentic framework.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 想象图像 $I_{\mathrm{sim}}$ 通过描绘合理的接触与运动线索，显式突出交互应该发生的位置。它提高了可供性推理的成功率和可解释性，也让系统能在 agentic 框架中利用生成模型关于交互状态的先验知识。

### 4.4. Thinker: Decide what to Operate

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The Thinker reasons about the appropriate interactive areas in textual form. Given the original image $I$, the imagined image $I_{\mathrm{sim}}$, and the task $T$, A4-Agent prompts a VLM with a preset template to perform three steps: perceive key components and candidate interaction points in $I$; consult $I_{\mathrm{sim}}$ to infer contact or motion cues consistent with the affordance; and ground the actionable part back in $I$ as a compact, machine-readable specification.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Thinker 以文本形式推理合适的交互区域。给定原图 $I$、想象图 $I_{\mathrm{sim}}$ 和任务 $T$，A4-Agent 用预设模板提示 VLM 完成三步：感知 $I$ 中的关键部件和候选交互点；参考 $I_{\mathrm{sim}}$ 推断与可供性一致的接触或运动线索；再把可操作部件定位回 $I$，并输出紧凑、机器可读的规格。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The VLM returns two sections: Thinking, a free-form rationale, and Output, a machine-readable JSON. A4-Agent ignores the Thinking section and parses only the JSON fields `"task"`, `"object_name"`, and `"object_part"`. The object part is phrased as “the [object part] of the [object name],” yielding a concise textual affordance description $D$ that says what to interact with, without spatial coordinates.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> VLM 返回两个部分：自由形式推理的 Thinking，以及机器可读 JSON 形式的 Output。A4-Agent 忽略 Thinking，只解析 JSON 字段 `"task"`、`"object_name"` 与 `"object_part"`。对象部件写成 “the [object part] of the [object name]” 形式，从而得到简洁的文本可供性描述 $D$，说明“要操作什么”，但不包含空间坐标。

### 4.5. Spotter: Locate where to Operate

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The Spotter converts the semantic affordance description into precise pixel-level localization. Given a textual description $D$, such as “handle on the right refrigerator door,” it uses two complementary vision foundation models for coarse-to-fine grounding: an open-vocabulary detector for initial region identification, followed by a segmentation model for pixel-accurate mask refinement.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Spotter 将语义可供性描述转化为精确像素级定位。给定文本描述 $D$，例如“右侧冰箱门上的把手”，它使用两个互补的视觉基础模型进行由粗到细的定位：先用开放词表检测器识别初始区域，再用分割模型细化出像素精确 mask。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The first step uses Rex-Omni [20], a state-of-the-art open-vocabulary object detector. Given the textual description $D$ from Thinker, Rex-Omni outputs bounding boxes $\{B_i\}_{i=1}^{N}$ that coarsely enclose affordance parts and key points $\{P_i\}_{i=1}^{N}$ as representative spatial anchors within each affordance region.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 第一步使用 Rex-Omni [20]，这是一个开放词表目标检测器。给定 Thinker 生成的文本描述 $D$，Rex-Omni 输出粗略包围可供性部件的 bounding boxes $\{B_i\}_{i=1}^{N}$，以及作为区域内代表性空间锚点的 key points $\{P_i\}_{i=1}^{N}$。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The second step sends the predicted boxes and points to SAM, which generates segmentation masks $\{M_i\}_{i=1}^{N}$ that delineate the precise boundaries of the affordance regions. The final prediction aggregates multi-granular spatial information:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 第二步把预测的 boxes 和 points 送入 SAM，生成 segmentation masks $\{M_i\}_{i=1}^{N}$，以刻画可供性区域的精确边界。最终预测聚合多粒度空间信息：

$$
A_{\mathrm{ff}} = \{(B_i,P_i,M_i)\}_{i=1}^{N}.
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> This representation supports varied downstream applications: coarse boxes for quick scene understanding, key points for interaction targeting, and fine segmentation masks for precise manipulation planning. Because each model is modular, improved detectors or segmenters can be substituted without retraining the full system.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 这种表示支持多种下游应用：粗框可用于快速场景理解，关键点可用于交互目标指向，精细分割 mask 可用于精确操作规划。由于每个模型都是模块化的，后续更强的检测器或分割器可以直接替换，而不需要重训整个系统。

## 5. Experiment

### 5.1. Experimental Settings

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> A4-Agent coordinates pre-trained foundation models without training. In the complete agent, GPT-4o [19] is used as the VLM, Qwen-Image-Editing [48] is used as the generative model, Rex-Omni [20] is used for open-vocabulary object detection, and SAM2-Large [38] is used for segmentation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> A4-Agent 在不训练的情况下协调预训练基础模型。在完整 agent 中，作者使用 GPT-4o [19] 作为 VLM，使用 Qwen-Image-Editing [48] 作为生成模型，使用 Rex-Omni [20] 进行开放词表目标检测，并使用 SAM2-Large [38] 进行分割。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The evaluation covers three quantitative benchmarks and open-world images. ReasonAff [45] is a reasoning-oriented dataset built on Instruct-Part [44] and contains 600 test image-task pairs. RAGNet [49] is a large-scale reasoning-based affordance segmentation dataset; the authors evaluate on RAGNet-3DOI and RAGNet-HANDAL, totaling 3,018 image-task pairs. UMD Part Affordance [33] covers 17 object categories and 7 affordance types; following prior work [45], the authors sample one-tenth of the frames, yielding 1,922 test images. Open-world images are collected from PhysToolBench [56] and web sources for qualitative evaluation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 评估覆盖三个定量基准和开放世界图像。ReasonAff [45] 是基于 Instruct-Part [44] 构建的推理导向数据集，测试集包含 600 个图像-任务对。RAGNet [49] 是大规模推理型可供性分割数据集；作者在 RAGNet-3DOI 和 RAGNet-HANDAL 上评估，总计 3,018 个图像-任务对。UMD Part Affordance [33] 覆盖 17 类对象和 7 类可供性；按照先前工作 [45]，作者采样十分之一帧，得到 1,922 张测试图像。开放世界图像来自 PhysToolBench [56] 与网络来源，用于定性评估。

### Table 1. ReasonAff 定量结果

![Table 1](table1_reasonaff_results.png)

**Caption:** Quantitative results on ReasonAff. A4-Agent achieves SOTA performance in zero-shot manner without any training.

**Caption[CN]:** ReasonAff 上的定量结果。A4-Agent 在没有任何训练的零样本方式下达到 SOTA 表现。

**Reading note:** 表中 A4-Agent 达到 70.52 gIoU、64.62 cIoU、75.24 P50、55.22 P50-95；它超过了 Affordance-R1、Vision Reasoner 等训练/推理增强基线。

### Table 2. RAGNet-3DOI 与 RAGNet-HANDAL 定量结果

![Table 2](table2_ragnet_results.png)

**Caption:** Quantitative results on RAGNet-3DOI and RAGNet-HANDAL. A4-Agent achieves SOTA performance in zero-shot manner without any training.

**Caption[CN]:** RAGNet-3DOI 与 RAGNet-HANDAL 上的定量结果。A4-Agent 在不训练的零样本方式下达到 SOTA 表现。

**Reading note:** A4-Agent 在 3DOI 上为 63.9 gIoU / 58.3 cIoU，在 HANDAL-easy 上为 61.1 / 61.7，在 HANDAL-hard 上为 61.0 / 59.6。

### 5.2. Quantitative Results

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> On ReasonAff, which requires reasoning over implicit contextual instructions, A4-Agent achieves state-of-the-art performance across all metrics without training. The paper states that compared with supervised methods such as AffordanceLLM and reasoning-enhanced approaches such as Vision Reasoner and Affordance-R1, A4-Agent demonstrates superior reasoning ability and generalization. The surrounding text reports 71.83 gIoU, while Table 1 reports 70.52 gIoU; this appears to be an internal numerical inconsistency in the source.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在 ReasonAff 上，任务需要根据隐含上下文指令进行深度推理，A4-Agent 无需训练即可在所有指标上达到 SOTA。论文称，与 AffordanceLLM 等监督方法，以及 Vision Reasoner、Affordance-R1 等推理增强方法相比，A4-Agent 展示了更强的推理能力与泛化能力。正文附近写到 71.83 gIoU，而 Table 1 中为 70.52 gIoU；这似乎是源文内部的数值不一致。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The authors attribute the ReasonAff performance to three design principles. First, decoupling reasoning from grounding lets VLMs handle semantic interpretation while specialized vision models handle localization. Second, the “think-with-imagination” mechanism grounds abstract instructions in synthesized visual representations. Third, because the method is not constrained by task-specific training data, it naturally generalizes to diverse instructions.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 作者将 ReasonAff 上的表现归因于三个设计原则。第一，推理与定位解耦，使 VLM 负责语义解释，专门视觉模型负责定位。第二，“think-with-imagination” 机制把抽象指令落到合成视觉表征中。第三，由于方法不受任务特定训练数据限制，它自然能够泛化到多样指令。

## Figure 4. ReasonAff 定性比较

![Fig. 4](fig4_reasonaff_qualitative.png)

**Caption:** Qualitative comparison on ReasonAff dataset. Our method continuously predicts appropriate components according to task requirements, achieving results most consistent with ground truth and even surpassing Affordance-R1 specifically trained on this dataset.

**Caption[CN]:** ReasonAff 数据集上的定性比较。该方法能够根据任务要求持续预测合适部件，其结果最接近 ground truth，甚至超过了专门在该数据集上训练的 Affordance-R1。

**Reading note:** 这张图突出“同一对象，不同任务，操作区域不同”的核心难点；例如刀既可能用于切割，也可能需要安全握持。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> On RAGNet, A4-Agent significantly outperforms all baselines. On 3DOI it reaches 63.9 gIoU, more than 24 points above Vision-Reasoner, and it also obtains the highest scores on HANDAL variants. Importantly, it surpasses AffordanceVLM even though AffordanceVLM is supervised and trained on this dataset, supporting the claim that agentic coordination of foundation models can outperform task-specific fine-tuning for complex reasoning tasks.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在 RAGNet 上，A4-Agent 显著超过所有基线。在 3DOI 上它达到 63.9 gIoU，比 Vision-Reasoner 高出 24 分以上，并且在 HANDAL 变体上也取得最高分。关键的是，它超过了在该数据集上训练的监督式 AffordanceVLM，支持了作者的主张：对于复杂推理任务，基础模型的 agentic 协同可能优于任务特定微调。

## Figure 5. RAGNet 定性比较

![Fig. 5](fig5_ragnet_qualitative.png)

**Caption:** Qualitative comparison on RAGNet dataset. Our zero-shot method effectively reasons over task instructions to identify correct regions and precisely localize them with masks, closely matching ground truth. This outperforms baseline methods including AffordanceVLM trained on this dataset.

**Caption[CN]:** RAGNet 数据集上的定性比较。该零样本方法能有效根据任务指令推理正确区域，并用 mask 精确定位，与 ground truth 高度一致，超过了包括在该数据集上训练的 AffordanceVLM 在内的基线方法。

**Reading note:** RAGNet 图例显示 A4-Agent 的优势不只在“找对物体”，还在“按任务找对物体部件”。

### Table 3. UMD 零样本结果

![Table 3](table3_umd_results.png)

**Caption:** Zero-shot results on UMD dataset. A4-Agent outperforms fine-tuned methods without any training.

**Caption[CN]:** UMD 数据集上的零样本结果。A4-Agent 在没有训练的情况下超过微调方法。

**Reading note:** A4-Agent 在 UMD 上达到 65.38 gIoU、59.81 cIoU、77.31 P50、43.78 P50-95，比 Affordance-R1 高 15.53 gIoU。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> On UMD, A4-Agent also performs strongly on the more traditional task of predicting affordances from action concepts. It outperforms the best baseline by 15.53 gIoU, suggesting that powerful pre-trained models already possess rich general knowledge about how common object parts can be used.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在 UMD 上，A4-Agent 在更传统的“根据动作概念预测可供性”任务中同样表现强劲。它比最佳基线高 15.53 gIoU，说明强预训练模型已经具备关于常见对象部件用途的丰富常识。

### 5.3. Qualitative Results on Open-World Images

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For open-world images, A4-Agent demonstrates robust performance across novel objects, complex scenes, and deep reasoning cases. It can identify actionable regions on objects absent from standard benchmarks, choose suitable tool parts in complex environments, and reason that a slotted spoon can drain water or that a rock can substitute for a hammer to drive nails. This suggests that training-free coordination can exploit broad web-scale knowledge for real-world generalization.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 在开放世界图像中，A4-Agent 在新对象、复杂场景和深层推理案例上都表现稳健。它能识别标准基准之外对象的可操作区域，在复杂环境中选择合适工具部件，并能推理出漏勺可以沥水、石头可以替代锤子钉钉子。这说明免训练协同能够利用大规模预训练知识，实现真实世界泛化。

## Figure 6. 开放世界图像定性结果

![Fig. 6](fig6_open_world_qualitative.png)

**Caption:** Qualitative results on open-world images. A4-Agent demonstrates robust affordance reasoning across diverse scenarios, consistently produces reasonable regions based on complex instructions.

**Caption[CN]:** 开放世界图像上的定性结果。A4-Agent 在多样场景中展示稳健的可供性推理能力，并能根据复杂指令持续产生合理区域。

**Reading note:** 这里最有趣的是“工具替代”类推理：例如为了逃生打碎车窗，模型要把任务映射到可执行工具和接触部件，而不只是识别图中物体。

### 5.4. Ablation Study

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The ablation study first evaluates visual imagination. Across base models, adding the Dreamer / think-with-imagination mechanism improves all metrics. Notably, open-source Qwen-2.5-VL-7B with imagination even outperforms closed-source GPT-4o using text-only reasoning, indicating that generated visual representations can compensate for weaker textual reasoning in this setting.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 消融首先评估视觉想象的作用。对不同基础模型而言，加入 Dreamer / think-with-imagination 机制都会提升所有指标。值得注意的是，带有想象机制的开源 Qwen-2.5-VL-7B 甚至超过了只用文本推理的闭源 GPT-4o，说明在这一任务中，生成式视觉表征可以补偿较弱文本推理能力。

### Table 4. Imagination 消融

![Table 4](table4_imagination_ablation.png)

**Caption:** Ablation on Imagination on RAGNet-3DOI Dataset. Affordance-R1 was fine-tuned from Qwen-2.5-VL-7B. T-w-I refers to think-with-imagination, which is the Dreamer.

**Caption[CN]:** RAGNet-3DOI 上关于 imagination 的消融。Affordance-R1 由 Qwen-2.5-VL-7B 微调得到；T-w-I 表示 think-with-imagination，即 Dreamer。

**Reading note:** 对 GPT-4o 来说，Dreamer 从 62.30 / 54.43 提升到 63.94 / 58.30；对 Qwen-2.5-VL-7B，也从 58.48 / 49.26 提升到 63.02 / 49.87。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The authors then study robustness to different components. Replacing Qwen-2.5-VL with GPT-4o improves performance, showing that the framework can incorporate stronger foundation models as they emerge. Replacing SAM2-Large with smaller SAM2-Base-Plus or SAM2-Tiny causes some performance drop, but the system remains effective and still surpasses baselines, suggesting robustness to weaker grounding components.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 作者随后研究不同组件选择下的稳健性。用 GPT-4o 替换 Qwen-2.5-VL 会提升性能，说明该框架可以无缝接入更强基础模型。把 SAM2-Large 换成较小的 SAM2-Base-Plus 或 SAM2-Tiny 会导致一定性能下降，但系统仍然有效且超过基线，说明对较弱定位组件也较稳健。

### Table 5. 组件消融

![Table 5](table5_component_ablation.png)

**Caption:** Ablation on different components on RAGNet-3DOI Dataset. AffordanceVLM is finetuned from LISA. SAM2-L,B,T denotes SAM2-Large, Base-plus, Tiny.

**Caption[CN]:** RAGNet-3DOI 上不同组件的消融。AffordanceVLM 由 LISA 微调得到；SAM2-L/B/T 分别表示 SAM2-Large、Base-plus 与 Tiny。

**Reading note:** 该表是论文“模块可替换”主张的主要证据：推理 backbone 与分割 backbone 都能独立替换，且性能变化可解释。

## 6. Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper presents A4-Agent, a training-free framework for affordance prediction. Its main contribution is to decouple the task into high-level reasoning and low-level grounding, allowing VLMs to handle semantic interpretation and vision foundation models to handle localization. It also introduces an imagination mechanism in which a generative model visualizes potential interactions to improve reasoning. Experiments show that the zero-shot approach outperforms supervised methods on challenging benchmarks and generalizes to open-world scenarios, highlighting the potential of agentic coordination of foundation models for complex affordance prediction.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本文提出 A4-Agent，一个用于可供性预测的免训练框架。其主要贡献是把任务拆成高层推理和低层定位，使 VLM 负责语义解释，视觉基础模型负责定位。论文还引入想象机制，让生成模型可视化潜在交互，从而提升推理。实验表明，这一零样本方法在挑战性基准上超过监督方法，并泛化到开放世界场景，凸显了基础模型 agentic 协同在复杂可供性预测中的潜力。

## References

The source paper contains 59 references spanning LLM/MLLM systems, visual grounding, affordance learning, segmentation, and generative-model reasoning. For reading purposes, the key reference clusters are:

- Foundation / MLLM backbones and reasoning: GPT-4 [1], Qwen2.5-VL [3], DeepSeek-R1 [14], OpenAI o1 [35], Qwen3 [52], InternVL3 [58].
- Affordance and grounding baselines: LISA [22], AffordanceLLM [36], AffordanceVLM [49], Seqafford [54], Affordance-R1 [45], RAGNet [49], UMD Part Affordance [33].
- Detection and segmentation tools: Grounding-DINO [27], Rex-Omni [20], SAM2 [38], VLPart [42], OVSeg [25], SAN [51].
- Visual imagination / generative reasoning: Thinking with Generated Images [8], VoT [50], Multimodal Visualization-of-Thought [23], Qwen-Image [48], video/world-model related work [5, 6, 15, 16, 43, 55, 59].

## Supplementary Material

## 7. More Implementation Detail

### 7.1. Details of Baseline Methods

## Figure 7. Baseline categories

![Fig. 7](fig7_baseline_categories.png)

**Caption:** Illustration of different categories of baseline methods.

**Caption[CN]:** 不同类别基线方法的示意图。

**Reading note:** 三类基线对应三种路线：纯开放词表分割；MLLM 端到端输出 mask；MLLM 先定位再用 SAM 分割。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The supplementary material groups baselines into three categories. Open-vocabulary segmentation methods take textual prompts and output segmentation masks; examples include VLPart [42], OVSeg [25], SAN [51], and Grounding-DINO [27]. MLLM-enhanced end-to-end segmentation methods fine-tune MLLMs to generate mask tokens and decode them into masks, including AffordanceLLM [36], AffordanceVLM [49], LISA [22], SAM4MLLM [7], and GLaMM [37]. MLLM-grounding-plus-SAM methods first predict boxes and keypoints, then pass them to SAM2; representative methods include Seg-Zero [28], Vision Reasoner [29], and Affordance-R1 [45].

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 补充材料把基线分为三类。开放词表分割方法接收文本 prompt 并输出 segmentation mask，例子包括 VLPart [42]、OVSeg [25]、SAN [51] 和 Grounding-DINO [27]。MLLM 增强的端到端分割方法微调 MLLM，使其生成 mask token 并解码为 mask，包括 AffordanceLLM [36]、AffordanceVLM [49]、LISA [22]、SAM4MLLM [7] 与 GLaMM [37]。MLLM 定位 + SAM 方法则先预测 boxes 和 keypoints，再送入 SAM2；代表方法包括 Seg-Zero [28]、Vision Reasoner [29] 与 Affordance-R1 [45]。

### 7.2. Evaluation Metrics

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Following affordance prediction and semantic segmentation protocols [38, 44, 45, 57], the paper uses four complementary metrics: gIoU, the average intersection-over-union across images; cIoU, the cumulative intersection over cumulative union at dataset level; P@50, the percentage of predictions whose IoU exceeds 0.5; and P@50:95, average precision across IoU thresholds from 0.5 to 0.95 in 0.05 increments.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 按照可供性预测与语义分割协议 [38, 44, 45, 57]，论文使用四个互补指标：gIoU，即跨图像的平均 intersection-over-union；cIoU，即数据集层面的累计交并比；P@50，即 IoU 超过 0.5 的预测比例；P@50:95，即从 0.5 到 0.95、步长 0.05 的多阈值平均精度。

### 7.3. System Prompt of our Agent

## Prompt card: Dreamer

![Prompt for Dreamer](prompt_dreamer.png)

**Caption:** System prompt for Dreamer. It asks the agent to write a concise photorealistic image-editing prompt that imagines a physically plausible interaction while preserving the original object and background.

**Caption[CN]:** Dreamer 的系统 prompt。它要求 agent 写出简洁、照片级真实的图像编辑 prompt，想象物理上合理的交互，同时保持原对象与背景不变。

**Reading note:** Dreamer prompt 的关键不是“随便生成一张图”，而是严格约束交互、姿态、遮挡、光照、尺度、视角与原场景一致。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The Dreamer prompt defines the agent as an “Imagination-driven Image-Editing Prompt Writer.” Given an image and a task, it must imagine a person or another object interacting with the target object and output only a concise prompt beginning with “Edit the input image to...” and ending with “keep others unchanged.” The requirements emphasize physical plausibility, preservation of identity and background, realistic body pose, logical occlusion, and matching scale, perspective, lighting, and shadows.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Dreamer prompt 将 agent 定义为“由想象驱动的图像编辑 prompt 写作者”。给定图像和任务，它必须想象一个人或另一个对象如何与目标对象交互，并且只输出简洁 prompt，开头为 “Edit the input image to...”，结尾为 “keep others unchanged”。要求重点包括物理合理性、保持对象身份和背景、真实人体姿态、合理遮挡，以及尺度、透视、光照和阴影的一致性。

## Prompt card: Thinker

![Prompt for Thinker](prompt_thinker.png)

**Caption:** System prompt for Thinker. It asks the VLM to identify key components, analyze the simulated interaction image, and output a structured JSON with task, object name, and object part.

**Caption[CN]:** Thinker 的系统 prompt。它要求 VLM 识别关键部件、分析模拟交互图，并输出包含 task、object_name 和 object_part 的结构化 JSON。

**Reading note:** Thinker prompt 的设计把自由推理与机器可读输出分开；实际 pipeline 只解析 JSON，这可以减少推理文本噪声进入后续定位。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The Thinker prompt receives two images: the original image and the image where the object interacts with a person or another object. It instructs the model to identify key object components, analyze the simulated interaction, then return a structured JSON containing the task instruction, object name, and object part. This JSON becomes the semantic bridge to Spotter.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> Thinker prompt 接收两张图：原图，以及对象与人或其他对象交互后的图。它要求模型识别关键对象部件，分析模拟交互，然后返回包含任务指令、对象名称和对象部件的结构化 JSON。这个 JSON 就是通向 Spotter 的语义桥梁。

## 8. More Exploratory Experiments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The authors also test a more exploratory variant using only Rex-Omni and SAM, corresponding to a Spotter-only system without Dreamer and Thinker. Because Rex-Omni’s backbone is an MLLM, it has some language understanding ability, but the results on RAGNet-3DOI are substantially worse. This supports the central motivation: decoupling reasoning and grounding allows the system to fully exploit the strengths of separate components.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 作者还测试了一个探索性变体：只使用 Rex-Omni 和 SAM，也就是没有 Dreamer 与 Thinker 的 Spotter-only 系统。由于 Rex-Omni 的 backbone 是 MLLM，它具备一定语言理解能力，但在 RAGNet-3DOI 上结果明显较差。这进一步支持本文核心动机：将推理与定位解耦，才能充分利用不同组件的优势。

### Table 6. 探索性实验

![Table 6](table6_exploratory_results.png)

**Caption:** More exploratory results on RAGNet-3DOI.

**Caption[CN]:** RAGNet-3DOI 上的更多探索性结果。

**Reading note:** 完整 Dreamer + Thinker + Spotter 为 63.94 / 58.30；去掉 Dreamer 降至 62.30 / 54.43；只剩 Spotter 则降至 45.91 / 39.82。

## 9. More Intermediate Results

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The supplementary material shows full intermediate results from A4-Agent. Figures 8 and 9 are sampled from ReasonAff, Figures 10 and 11 from UMD, and Figures 12 and 13 from RAGNet. Each example exposes the full chain: input image and task, Dreamer’s edited-image prompt and generated image, Thinker’s textual reasoning and JSON output, and Spotter’s Rex-Omni and SAM2 localization.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 补充材料展示了 A4-Agent 的完整中间结果。Fig. 8 和 Fig. 9 来自 ReasonAff，Fig. 10 和 Fig. 11 来自 UMD，Fig. 12 和 Fig. 13 来自 RAGNet。每个例子都暴露完整链条：输入图像与任务、Dreamer 的图像编辑 prompt 和生成图、Thinker 的文本推理与 JSON 输出，以及 Spotter 的 Rex-Omni 和 SAM2 定位。

### Figure 8. ReasonAff bottle intermediate result

![Fig. 8](fig8_intermediate_bottle.png)

**Caption:** Full Demonstration of Intermediate Results. Sampled from results on the ReasonAff dataset.

**Caption[CN]:** 完整中间结果演示，样本来自 ReasonAff 数据集。

**Reading note:** 任务要求安全握住瓶身；Dreamer 生成手握瓶身图，Thinker 输出 “the body of the bottle”，Spotter 最终分割瓶身区域。

### Figure 9. ReasonAff faucet intermediate result

![Fig. 9](fig9_intermediate_faucet.png)

**Caption:** Full Demonstration of Intermediate Results. Sampled from results on the ReasonAff dataset.

**Caption[CN]:** 完整中间结果演示，样本来自 ReasonAff 数据集。

**Reading note:** 任务要求按下水龙头打开水；Thinker 根据想象图定位到 faucet handle，Spotter 分割把手区域。

### Figure 10. UMD ladle intermediate result

![Fig. 10](fig10_intermediate_ladle.png)

**Caption:** Full Demonstration of Intermediate Results. Sampled from results on the UMD dataset.

**Caption[CN]:** 完整中间结果演示，样本来自 UMD 数据集。

**Reading note:** 对 “grasp” 可供性，系统选择 ladle handle，而非勺头，体现了动作类型对部件选择的约束。

### Figure 11. UMD spoon intermediate result

![Fig. 11](fig11_intermediate_spoon.png)

**Caption:** Full Demonstration of Intermediate Results. Sampled from results on the UMD dataset.

**Caption[CN]:** 完整中间结果演示，样本来自 UMD 数据集。

**Reading note:** 对 “scoop” 可供性，系统选择 spoon bowl；同样对象在不同动作下可能对应不同部件。

### Figure 12. RAGNet door intermediate result

![Fig. 12](fig12_intermediate_door.png)

**Caption:** Full Demonstration of Intermediate Results. Sampled from results on the RAGNet dataset.

**Caption[CN]:** 完整中间结果演示，样本来自 RAGNet 数据集。

**Reading note:** “open the door” 被映射为 doorknob，这类例子说明系统把语言任务转化为具体可操作部件。

### Figure 13. RAGNet oven intermediate result

![Fig. 13](fig13_intermediate_oven.png)

**Caption:** Full Demonstration of Intermediate Results. Sampled from results on the RAGNet dataset.

**Caption[CN]:** 完整中间结果演示，样本来自 RAGNet 数据集。

**Reading note:** “preheat the oven” 被映射到 oven knob；这里的难点是从厨房场景中选定正确对象和控制部件。

## Critical Reading Notes

1. 本文真正的新意不是提出新的训练损失或网络结构，而是把可供性预测拆成“想象-推理-定位”的 test-time agentic workflow。它更像是基础模型时代的系统论文。
2. 主要优势来自模块化：GPT-4o、Qwen-Image、Rex-Omni、SAM2 任一组件增强，都可能带来整体提升；但这也意味着论文结论依赖这些外部组件的能力和可用性。
3. 论文最强证据是零样本超过监督/微调基线，尤其是 RAGNet 和 ReasonAff 上的结果；不过需要注意成本、推理延迟、闭源模型依赖、生成图稳定性等实际部署问题。
4. Dreamer 的机制有解释性价值：它把抽象语言指令转化为一个可视化中间状态。但如果生成模型产生不合理交互，后续 Thinker 可能被误导。
5. 源文中 ReasonAff 结果存在一个数值不一致：正文描述 A4-Agent reaches 71.83 gIoU，而 Table 1 显示 70.52 gIoU。阅读和引用时应优先以表格为准，或回查作者后续版本。
