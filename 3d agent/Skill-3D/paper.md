# Skill-3D: Evolving Scene-Aware Skills for Agentic 3D Spatial Reasoning
**Authors:** Haoyuan Li, Zhengdong Hu, Jun Wang, Hehe Fan, Yi Yang  
**Source:** `Li 等 - 2026 - Skill-3D Evolving Scene-Aware Skills for Agentic 3D Spatial Reasoning.pdf`  
**Detected source format:** selectable-text PDF (`pdf-text`)  
**Reader type:** full-paper Chinese-English Markdown reader with figure/table assets.

## Page / Section Index
| Section | Pages | Notes |
|---|---:|---|
| Abstract | p.1 | bilingual body and related figures/tables |
| 1 Introduction | pp.1-2 | bilingual body and related figures/tables |
| 2 Related Work | pp.2-3 | bilingual body and related figures/tables |
| 3 Method | pp.3-5 | bilingual body and related figures/tables |
| 4 Experiments | pp.5-8 | bilingual body and related figures/tables |
| 5 Conclusion and Limitations | pp.8-9 | bilingual body and related figures/tables |
| Appendix A. LLM Usage Claim | p.14 | bilingual body and related figures/tables |
| Appendix B. More Experimental Results | p.14 | bilingual body and related figures/tables |
| Appendix C. Experimental Details | pp.14-15 | bilingual body and related figures/tables |
| Appendix D. Qualitative Results | pp.15-17 | bilingual body and related figures/tables |
| Appendix E. Prompt Design | pp.18-21 | bilingual body and related figures/tables |
| References | pp.9-13 | bibliography preserved in the source PDF; not translated line-by-line |

## Terminology Ledger
| Canonical term | Chinese rendering | Decision |
|---|---|---|
| Skill-3D | Skill-3D | 本文方法名；保持英文。 |
| agentic 3D spatial reasoning | agentic 3D 空间推理 | 通过 agent 和外部工具完成 3D 空间理解。 |
| MLLM | 多模态大语言模型（MLLM） | 首次展开后保持 MLLM。 |
| Scene Memory | Scene Memory | 保存场景上下文、工具轨迹、证据与失败模式的记忆。 |
| Skill Library | Skill Library | 保存 static skills 与 dynamic skills 的技能库。 |
| scene-aware skill | 场景感知技能 | 由相似场景成功轨迹蒸馏出的工具工作流。 |
| static skill | 静态技能 | 固定任务级先验。 |
| dynamic skill | 动态技能 | 可被成功/失败 rollout 合并、修补和更新的技能。 |
| rollout / trajectory | rollout / 轨迹 | 一次完整问题求解过程，包括推理、工具调用和答案。 |
| failure lesson | failure lesson / 失败教训 | 从失败轨迹中提取并附着到技能的纠错信息。 |
| effective tool usage (ETU) | 有效工具使用率（ETU） | 有效且被后续推理使用的工具调用比例。 |
| agentic SFT | agentic SFT | 在技能引导轨迹上学习结构化交互格式的监督微调。 |
| GRPO | Group Relative Policy Optimization（GRPO） | 组内相对优势优化方法。 |
| Pi3 | Pi3 | 论文使用的 3D 重建/视觉几何工具。 |
| GroundingDINO | GroundingDINO | 目标检测/grounding 工具。 |
| SAM3 | SAM3 | 分割工具。 |
| Depth Anything 3 | Depth Anything 3 | 深度估计工具。 |
| Orient Anything v2 | Orient Anything v2 | 朝向估计工具。 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This paper explores agentic 3D spatial understanding, i.e., MLLM agents performing 3D reasoning through tool use. Existing methods often misuse tools and exhibit biased tool preferences under 3D scenarios, leaving the agentic paradigm with only marginal gains over non-agentic strategies. The authors argue that 3D spatial reasoning tasks are heterogeneous across scenes, whereas existing agents tend to apply one uniform tool-use strategy. Skill-3D addresses this by identifying the task scene, recording tool-use trajectories into Scene Memory, distilling successful trajectories from similar scenes into reusable scene-aware skills, and attaching failures as lessons. During training, recurring similar scenes trigger skill injection, producing new trajectories that further refine the memory and skill library. Experiments show that Skill-3D improves tool utilization from 39% to 78% on VSI-Bench, improves Gemini-3-Flash by 67% on MMSI-Bench, and skill-guided post-training boosts Qwen3-VL-8B by 60% on VSI-Bench.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本文研究 agentic 3D 空间理解，即 MLLM agent 通过调用工具完成 3D 推理。已有方法在 3D 场景中常常误用工具，并表现出偏向少数工具的选择偏置，因此相比非 agentic 策略只能带来有限收益。作者指出，3D 空间推理任务在不同场景中高度异质，而现有 agent 往往对所有场景采用统一工具策略。Skill-3D 的解决方式是：识别任务场景，把工具使用轨迹写入 Scene Memory，将相似场景中的成功轨迹蒸馏为可复用的场景感知技能，并把失败轨迹附着为 lessons。训练期间，当相似场景再次出现时，相应技能会被注入以指导 agent，新的成功和失败又继续细化记忆与技能库。实验显示，Skill-3D 将 VSI-Bench 上的有效工具使用率从 39% 提升到 78%，使 Gemini-3-Flash 在 MMSI-Bench 上提升 67%，并通过技能引导后训练使 Qwen3-VL-8B 在 VSI-Bench 上提升 60%。

## 1 Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Agentic 3D spatial reasoning aims to enable MLLM agents to solve indoor 3D understanding tasks through external tool use. Tools can provide spatial and geometric evidence that is difficult for the MLLM alone to infer, such as object detection, segmentation, depth estimation, and 3D reconstruction. However, existing tool-augmented methods often fail to realize the potential of tools in 3D reasoning: they prefer a few dominant tools regardless of the actual scene requirement, so adding tools yields only marginal gains over non-agentic baselines in some scenarios.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Agentic 3D 空间推理旨在让 MLLM agent 通过外部工具解决室内 3D 理解任务。工具能够提供 MLLM 单独难以推断的空间和几何证据，例如目标检测、分割、深度估计和 3D 重建。然而，现有工具增强方法并没有充分发挥工具在 3D 推理中的潜力：它们无论场景需要什么，都偏好少数主导工具，因此在某些场景中，加工具相比非 agentic 基线只带来很小收益。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The authors attribute this limitation to the scene heterogeneity of indoor 3D reasoning. Different questions require different evidence and tool workflows. For example, an object-to-object distance question requires depth evidence, but existing methods may rely on object detection and 3D reconstruction, which mainly provide relative spatial relationships rather than the absolute depth grounding needed for distance estimation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 作者把这一限制归因于室内 3D 推理的场景异质性。不同问题需要不同证据和不同工具流程。例如，物体到物体的距离估计需要深度证据，但现有方法可能依赖目标检测和 3D 重建；这些工具主要提供相对空间关系，而不是距离估计所需的绝对深度 grounding。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Skill-3D is proposed as a framework that equips MLLM agents with reusable scene-aware skills. Given the same object-to-object distance question, Skill-3D identifies the scene-task context, retrieves a relevant skill, and invokes suitable perception tools such as depth estimation. It learns these skills by constructing a Scene Memory and co-evolving a Skill Library on top of that memory.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Skill-3D 被提出为一种让 MLLM agent 具备可复用场景感知技能的框架。面对同样的物体间距离问题，Skill-3D 会识别场景-任务上下文，检索相关技能，并调用深度估计等合适的感知工具。它通过构建 Scene Memory，并在其上共同演化 Skill Library 来学习这些技能。

### Fig. 1. 动机与 Skill-3D 概览

![Fig. 1](fig1_motivation_overview.png)

**Caption:** Figure 1: Motivation and overview of Skill-3D. (a) Scene-agnostic tool calls can yield mismatched evidence and unreliable answers. (b) Skill-3D retrieves scene-aware skills to guide tool-use workflows, e.g., detection, depth, 3D reconstruction. (c) Skill-3D improves over strong MLLM baselines across diverse spatial reasoning dimensions.

**Caption[CN]:** 图 1：Skill-3D 的动机与总体概览。(a) 与场景无关的工具调用会产生不匹配的证据和不可靠答案。(b) Skill-3D 检索场景感知技能来指导工具使用流程，例如检测、深度估计和 3D 重建。(c) Skill-3D 在多种空间推理维度上优于强 MLLM 基线。

**Reading note:** 重点看 (a) 与 (b) 的对比：同一个距离问题下，是否调用深度工具决定了证据是否充分。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> During training, an MLLM agent identifies each question’s scene and stores the corresponding tool-use trajectory and outcome into Scene Memory. The Skill Library aggregates successful trajectories from similar scenes and distills them into reusable scene-aware skills, while failed trajectories are attached as lessons. Once a skill forms, it is injected back into subsequent questions from similar scenes; the resulting successes and failures refine that same skill, so Scene Memory and the Skill Library co-evolve.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 训练期间，MLLM agent 会识别每个问题的场景，并把相应工具使用轨迹及其结果存入 Scene Memory。Skill Library 会聚合相似场景中的成功轨迹，并将其蒸馏为可复用的场景感知技能；失败轨迹则作为 lessons 附着到技能上。一旦某个技能形成，它会被重新注入到后续相似场景问题中；由此产生的新成功和失败继续细化同一技能，使 Scene Memory 与 Skill Library 共同演化。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> This design has two practical benefits. First, skills are dynamically updated because new trajectories under similar scenes are written back, broadening skill coverage and reducing overfitting to a narrow scene slice. Second, Scene Memory and Skill Library evolve together without being predefined upfront, allowing both to become more discriminative as the agent encounters more diverse 3D tasks.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 这种设计有两个实际好处。第一，技能会动态更新：相似场景下的新轨迹会写回记忆，扩展技能覆盖范围，减少对狭窄场景片段的过拟合。第二，Scene Memory 与 Skill Library 不是预先定义的，而是共同演化；随着 agent 遇到更多样的 3D 任务，二者会变得更具区分性。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The paper further introduces skill-guided agentic post-training. The authors first apply supervised fine-tuning on skill-guided trajectories to teach the policy skill retrieval, tool invocation, and evidence accumulation. They then perform GRPO with a composite reward over answer correctness, skill-guided tool-use quality, and structured output, encouraging the policy to internalize the scene-aware behavior encoded by the Skill Library.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 论文进一步引入技能引导的 agentic 后训练。作者首先在技能引导轨迹上进行监督微调，使策略学习技能检索、工具调用和证据积累的格式。随后，他们使用包含答案正确性、技能引导工具使用质量和结构化输出的复合奖励进行 GRPO，促使策略内化 Skill Library 所编码的场景感知行为。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> The claimed contributions are threefold: Skill-3D constructs Scene Memory and co-evolves a Skill Library to obtain scene-aware skills; it proposes skill-guided agentic reinforcement learning under a composite reward; and it validates the framework across closed-source and open-source MLLMs on multiple 3D spatial reasoning benchmarks, with substantial improvements in tool usage.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 论文声称的贡献有三点：第一，Skill-3D 构建 Scene Memory，并在其上共同演化 Skill Library，从而得到场景感知技能；第二，在复合奖励下提出技能引导的 agentic reinforcement learning；第三，在多个 3D 空间推理基准上，对闭源和开源 MLLM 进行验证，并显著提升工具使用质量。

## 2 Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> MLLMs have shown growing capability in spatial reasoning, driven by stronger backbones and dedicated benchmarks. Recent methods improve fine-grained spatial understanding by incorporating 3D reconstruction, depth cues, spatial VQA data, explicit grounding, prompting, mental simulation, visual chain-of-thought, reinforcement learning, code-driven 3D reasoning, and generative imagination of 3D space. These capabilities are also extending into embodied and robotic settings.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> MLLM 在空间推理上的能力不断增强，背后来自更强 backbone 和专门基准的推动。近期方法通过引入 3D 重建、深度线索、空间 VQA 数据、显式 grounding、prompting、心理模拟、visual chain-of-thought、强化学习、代码驱动 3D 推理以及 3D 空间生成式想象，提升细粒度空间理解。这些能力也逐步扩展到具身和机器人场景。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Tool augmentation extends MLLMs by allowing them to invoke external modules through prompts, structured APIs, or code generation. Prior systems show that tools can compensate for limitations of end-to-end multimodal models. Recent tool-augmented VLM agents cover long-video understanding, high-resolution image analysis, medical diagnosis, and general visual reasoning. Some work trains VLMs to use tools through SFT or RL, while 3D agentic methods introduce reconstruction-based reasoning loops but often rely on uniform workflows across heterogeneous scenes.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 工具增强通过 prompt、结构化 API 或代码生成，让 MLLM 调用外部模块。已有系统表明，工具可以弥补端到端多模态模型的局限。近期工具增强 VLM agent 覆盖长视频理解、高分辨率图像分析、医学诊断和通用视觉推理。一些工作通过 SFT 或 RL 训练 VLM 使用工具；3D agentic 方法则引入基于重建的推理循环，但通常仍在异质场景中依赖统一流程。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Memory-based agents store trajectories for reflection or experience replay, but raw trajectories are long, redundant, and noisy. Recent work therefore studies skills as reusable behavioral primitives distilled from historical interactions. Existing skill-based agents mainly focus on general task automation, skill retrieval, or policy improvement. In contrast, Skill-3D studies skills for 3D spatial reasoning, where each skill must encode perception-grounded tool workflows involving objects, geometry, and multi-view evidence.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 基于记忆的 agent 会保存轨迹用于反思或经验回放，但原始轨迹往往冗长、冗余且有噪声。因此近期工作研究 skills，即从历史交互中蒸馏出的可复用行为原语。现有 skill-based agent 主要关注通用任务自动化、技能检索或策略改进。相比之下，Skill-3D 研究的是面向 3D 空间推理的技能，其中每个技能都必须编码由感知证据支撑的工具流程，涉及物体、几何和多视角证据。

## 3 Method

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Skill-3D is a scene-aware skill learning framework for agentic 3D spatial reasoning. It has three stages: recording completed rollouts into Scene Memory and evolving a Skill Library from successes and failures; retrieving scene-task-relevant skills to guide inference-time tool-use planning; and using skill-guided trajectories to post-train compact agents through agentic SFT and RL.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Skill-3D 是一个用于 agentic 3D 空间推理的场景感知技能学习框架。它包含三个阶段：将完成的 rollout 写入 Scene Memory，并从成功与失败中演化 Skill Library；检索与场景-任务相关的技能，以指导推理时工具规划；使用技能引导轨迹，通过 agentic SFT 和 RL 对小型 agent 进行后训练。

### Fig. 2. Skill-3D 框架

![Fig. 2](fig2_skill3d_framework.png)

**Caption:** Figure 2: Overview of Skill-3D. (a) Skill-3D records scene-task rollouts into Scene Memory, which stores scene context, tool evidence, and failure patterns. Successful rollouts are distilled into dynamic skills, while failed rollouts are attached as lessons, enabling Scene Memory and the Skill Library to co-evolve. (b) Given a new query, Skill-3D identifies the scene-task context, retrieves relevant static and dynamic skills, and selects a compact skill set to guide tool-use workflow and evidence acquisition. (c) Skill-guided trajectories are used for agentic SFT and GRPO, encouraging compact agents to internalize skill selection, tool use, and evidence-grounded spatial reasoning.

**Caption[CN]:** 图 2：Skill-3D 概览。(a) Skill-3D 将场景-任务 rollout 写入 Scene Memory，保存场景上下文、工具证据和失败模式；成功 rollout 被蒸馏为动态技能，失败 rollout 作为 lessons 附着到技能上，使 Scene Memory 与 Skill Library 共同演化。(b) 对新查询，Skill-3D 识别场景-任务上下文，检索相关静态/动态技能，并选择紧凑技能集来指导工具流程和证据获取。(c) 技能引导轨迹用于 agentic SFT 和 GRPO，使小型 agent 内化技能选择、工具使用和证据驱动的空间推理。

**Reading note:** 这张图对应方法三段：技能提取、技能引导推理、技能引导后训练。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For scene-aware skill extraction, each spatial question q is paired with visual observations O from an indoor scene. An MLLM agent predicts an answer by optionally invoking tools such as object detection, segmentation, depth estimation, orientation estimation, super-resolution, and 3D reconstruction. A rollout stores the question, observations, reasoning trace, selected skills, tool calls, tool outputs, and final answer. Skill-3D updates the Skill Library after each completed rollout.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在场景感知技能提取中，每个空间问题 q 与来自室内场景的视觉观测 O 配对。MLLM agent 可以选择调用目标检测、分割、深度估计、朝向估计、超分辨率和 3D 重建等工具来预测答案。一个 rollout 保存问题、观测、推理轨迹、所选技能、工具调用、工具输出和最终答案。Skill-3D 在每个 rollout 完成后更新 Skill Library。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Successful rollouts are treated as workflows. Skill-3D extracts a reusable tool-use routine from each successful rollout, including trigger condition, required evidence, tool order, key arguments, and evidence-to-answer mapping. The routine is promoted to a new dynamic skill if no compatible skill exists; otherwise it is merged into an existing skill only when it adds coverage such as a new scene condition, stronger evidence source, or lower-cost workflow.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 成功 rollout 被视为 workflow。Skill-3D 从每个成功 rollout 中提取可复用工具使用例程，包括触发条件、所需证据、工具顺序、关键参数以及证据到答案的映射。如果不存在兼容技能，该例程会被提升为新的 dynamic skill；否则，只有当它带来新场景条件、更强证据来源或更低成本流程等覆盖增益时，才会被合并进已有技能。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Failed rollouts are treated as lessons rather than discarded. Skill-3D diagnoses each failure from Scene Context and Tool Usage, with typical error types including wrong tool selection, missing evidence, invalid tool input, ignored tool output, and redundant tool calls. Evidence-supported failures are attached to related skills as lessons, and reliable corrections can patch a dynamic skill with fallback rules.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 失败 rollout 不会被丢弃，而是作为 lessons 使用。Skill-3D 根据 Scene Context 和 Tool Usage 诊断每个失败，典型错误包括工具选择错误、证据缺失、无效工具输入、忽略工具输出和冗余工具调用。有证据支持的失败会作为 lessons 附着到相关技能；可靠的修正则可以用 fallback rules 修补 dynamic skill。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The Skill Manager keeps the active library compact and reliable by filtering noisy rollouts and deciding whether candidate updates should be inserted, merged, patched, or rejected. Static skills remain fixed as task-level priors, whereas dynamic skills evolve through validated merges and patches. Thus, the library stores reusable scene-aware procedures rather than raw trajectories.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> Skill Manager 通过过滤噪声 rollout，并判断候选更新应被插入、合并、修补还是拒绝，保持活跃技能库紧凑且可靠。Static skills 作为任务级先验保持固定，而 dynamic skills 通过经过验证的合并与修补持续演化。因此，技能库保存的是可复用的场景感知过程，而不是原始轨迹。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> At inference time, Skill-3D first identifies the scene-task context, including task category, target entities, scene signature, and required evidence. This determines whether the agent should seek object-level evidence, boundary evidence, depth cues, orientation cues, multi-view geometry, or combinations of them.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 推理时，Skill-3D 首先识别场景-任务上下文，包括任务类别、目标实体、场景签名和所需证据。这一步决定 agent 应寻找物体级证据、边界证据、深度线索、朝向线索、多视角几何，还是这些证据的组合。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Scene-task skill retrieval performs top-k retrieval over the Skill Library to obtain candidate static and dynamic skills. Each skill is indexed by trigger condition, applicable scene context, required evidence type, and historical metadata. Ranking combines semantic alignment with query category, target entities, scene signature, evidence requirement, historical success rate, attached failure lessons, and estimated tool cost.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 场景-任务技能检索在 Skill Library 上执行 top-k 检索，得到候选 static skills 和 dynamic skills。每个技能由触发条件、适用场景上下文、所需证据类型和历史元数据索引。排序会综合查询类别、目标实体、场景签名、证据需求的语义匹配，以及历史成功率、附着失败 lessons 和估计工具成本。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Because candidate skills may be redundant or overlapping, Skill-3D uses the policy to select a compact subset for the current query. The selected skills should cover the required evidence while avoiding unnecessary tool calls. The selector can also generate fallback rules such as switching from detection to segmentation when closest-point boundaries are required, or using multi-view evidence when single-view localization is ambiguous.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 由于候选技能可能冗余或重叠，Skill-3D 使用策略为当前查询选择紧凑子集。被选技能应覆盖所需证据，同时避免不必要的工具调用。选择器还可以生成 fallback rules，例如当最近点边界是关键时从检测切换到分割，或在单视角定位不明确时使用多视角证据。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Conditioned on the selected skill, the agent performs iterative tool reasoning. At each step, it decides whether to invoke a tool, incorporate returned evidence, continue reasoning, or stop and answer. Tool outputs are appended to the reasoning history and used to update accumulated evidence. Compared with direct tool invocation, the skill-guided workflow constrains both evidence acquisition and evidence usage.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 在所选技能条件下，agent 执行迭代式工具推理。每一步，它决定是否调用工具、吸收返回证据、继续推理，或停止并回答。工具输出被追加到推理历史中，并用于更新累积证据。相比直接工具调用，技能引导流程同时约束证据获取和证据使用。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> Skill-guided agentic post-training transfers scene-aware tool-use behavior into compact MLLM agents. The Skill Library is frozen during post-training to avoid non-stationarity. Each training sample contains the question and observations, available skill candidates, selected skill sequence, tool calls and outputs, intermediate evidence, and final answer.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 技能引导的 agentic 后训练把场景感知工具使用行为迁移到小型 MLLM agent 中。为了避免非平稳性，后训练期间 Skill Library 被冻结。每个训练样本包含问题和观测、可用技能候选、所选技能序列、工具调用与输出、中间证据以及最终答案。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> Agentic SFT teaches the model the complete structured interaction pattern. Its target is not only to imitate tool calls, but also to learn when and how to select suitable skills from the Skill Library according to scene-task context, giving the policy a stable initialization before RL.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> Agentic SFT 教模型完整的结构化交互模式。它的目标不仅是模仿工具调用，还要根据场景-任务上下文学习何时以及如何从 Skill Library 中选择合适技能，从而在 RL 前为策略提供稳定初始化。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> For agentic RL, the authors optimize the skill-augmented policy with GRPO. For each query, the policy observes the question, visual observations, and retrieved skill candidates, then samples a group of complete trajectories. Each trajectory contains skill choices, tool calls, tool outputs, reasoning steps, and a final answer. The reward combines answer correctness, structured-format compliance, and tool-use efficiency.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 对于 agentic RL，作者使用 GRPO 优化技能增强策略。对每个查询，策略观察问题、视觉观测和检索到的技能候选，然后采样一组完整轨迹。每条轨迹包含技能选择、工具调用、工具输出、推理步骤和最终答案。奖励结合答案正确性、结构化格式合规性和工具使用效率。

$$
R(τ) = Rans(τ) + Rfmt(τ) + Rtool(τ)
$$

$$
Rtool(τ) = Rexec(τ) - |A| / B
$$

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> Here A is the set of tool calls and B is the maximum tool budget. Rexec is binary and is assigned 1 only when the trajectory obtains the evidence required by the benchmark task type and the frozen scene-task parser. Because required evidence is not determined by the model-selected skill, the policy cannot select easier skills merely to obtain higher tool-use reward.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> 其中 A 是工具调用集合，B 是最大工具预算。Rexec 是二值奖励，只有当轨迹获得由基准任务类型和冻结场景-任务解析器指定的所需证据时才为 1。由于所需证据并不由模型选择的技能决定，策略不能仅通过选择更容易的技能来获得更高工具使用奖励。

## 4 Experiments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The experiments evaluate Skill-3D on VSI-Bench, BLINK, CV-3D, and MMSI-Bench. VSI-Bench covers eight indoor spatial reasoning categories, including object counting, distance estimation, size estimation, route planning, and appearance order. BLINK evaluates multi-view reasoning, CV-3D evaluates depth ordering and relative distance, and MMSI-Bench evaluates positional relationship reasoning. The authors follow Think3D to randomly sample 30% of questions from each category as training data and use the remaining disjoint samples as the test set.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 实验在 VSI-Bench、BLINK、CV-3D 和 MMSI-Bench 上评估 Skill-3D。VSI-Bench 覆盖八类室内空间推理，包括目标计数、距离估计、尺寸估计、路线规划和出现顺序。BLINK 评估多视角推理，CV-3D 评估深度排序和相对距离，MMSI-Bench 评估位置关系推理。作者沿用 Think3D，从每个类别随机抽取 30% 问题作为训练集，其余问题级不重叠样本作为测试集。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For closed-source agents, the paper evaluates GPT-4o, GPT-5.4, Gemini-2.5-Pro, and Gemini-3-Flash under four settings: w/o Tools, w/ Tools, Think3D, and Skill-3D. For open-source agents, it evaluates Qwen3-VL-4B and Qwen3-VL-8B under the same settings, where Skill-3D-4B and Skill-3D-8B denote skill-guided post-trained models.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 对闭源 agent，论文评估 GPT-4o、GPT-5.4、Gemini-2.5-Pro 和 Gemini-3-Flash，并比较四种设置：w/o Tools、w/ Tools、Think3D 和 Skill-3D。对开源 agent，论文在相同设置下评估 Qwen3-VL-4B 和 Qwen3-VL-8B，其中 Skill-3D-4B 和 Skill-3D-8B 表示技能引导后训练模型。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Implementation uses external tools including Pi3, GroundingDINO, SAM3, Orient Anything v2, SwinIR, and the indoor metric-depth variant of Depth Anything 3. Qwen3-VL-4B/8B are base models, while GPT-5.4 is the teacher for skill distillation and SFT data generation. The training set contains 500 SFT samples and 1k GRPO samples. Training uses a composite reward with weights 0.6 for answer correctness, 0.2 for tool-use efficiency, and 0.2 for skill-tool format rewards, on 4 NVIDIA RTX PRO 6000 Blackwell GPUs.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 实现使用 Pi3、GroundingDINO、SAM3、Orient Anything v2、SwinIR，以及 Depth Anything 3 的室内 metric-depth 版本等外部工具。Qwen3-VL-4B/8B 作为基础模型，GPT-5.4 作为技能蒸馏和 SFT 数据生成的 teacher。训练集包含 500 个 SFT 样本和 1k 个 GRPO 样本。训练在 4 块 NVIDIA RTX PRO 6000 Blackwell GPU 上进行，复合奖励权重为答案正确性 0.6、工具使用效率 0.2、技能-工具格式奖励 0.2。

### Table 1. 闭源模型主结果

![Table 1](table1_closed_source_results.png)

**Caption:** Table 1: Comprehensive evaluation on VSI-Bench, BLINK, CV-3D, and MMSI-Bench. Representative spatial reasoning metrics are reported across multiple benchmarks. MV denotes multi-view. PR denotes positional relationship. Higher values indicate better performance, and all metrics are obtained on the test set.

**Caption[CN]:** 表 1：在 VSI-Bench、BLINK、CV-3D 与 MMSI-Bench 上的综合评测。表中报告多个基准上的代表性空间推理指标；MV 表示 multi-view，PR 表示 positional relationship。数值越高越好，所有指标均来自测试集。

**Reading note:** 横向比较同一 backbone 的四种设置，Skill-3D 在每个闭源模型上都高于 w/o Tools、w/ Tools 和 Think3D。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> For closed-source agents, Skill-3D consistently outperforms non-agentic, direct tool-use, and Think3D baselines across all four backbones. Because Skill-3D uses a single shared Skill Library built from heterogeneous spatial reasoning benchmarks, reusable skills learned from one benchmark can transfer to others when similar scene-task contexts occur. Averaged over four closed-source agents, the VSI-Bench average improves from 42.9 to 64.5, a 50.3% relative gain over the w/o Tools baseline.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 对闭源 agent，Skill-3D 在四个 backbone 上都稳定超过非 agentic、直接工具使用和 Think3D 基线。由于 Skill-3D 使用由异质空间推理基准构建的单一共享 Skill Library，当其他基准出现相似场景-任务上下文时，一个基准学到的可复用技能可以迁移过去。四个闭源 agent 平均来看，VSI-Bench 平均分从 42.9 提升到 64.5，相对 w/o Tools 基线提升 50.3%。

### Table 2. 开源模型主结果

![Table 2](table2_open_source_results.png)

**Caption:** Table 2: Open-source evaluation on VSI-Bench, BLINK, CV-3D, and MMSI-Bench. Representative spatial reasoning metrics are reported across multiple benchmarks. MV denotes multi-view. PR denotes positional relationship. Higher values indicate better performance, and all metrics are obtained on the test set.

**Caption[CN]:** 表 2：开源模型在 VSI-Bench、BLINK、CV-3D 与 MMSI-Bench 上的评测。表中报告多个空间推理指标；MV 表示 multi-view，PR 表示 positional relationship。数值越高越好，所有指标均来自测试集。

**Reading note:** Skill-3D-4B/8B 说明技能引导后训练可以迁移到较小开源 MLLM。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> For open-source agents, Skill-3D transfers effectively to compact models. On VSI-Bench, Skill-3D-4B achieves a 59.7% relative gain over the w/o Tools baseline, and Skill-3D-8B achieves a 60.3% relative gain. The stronger 8B results suggest that larger base models exploit retrieved skills and tool evidence better, while the consistent 4B gains show that smaller agents can still learn scene-aware skills through post-training.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 对开源 agent，Skill-3D 能有效迁移到小型模型。在 VSI-Bench 上，Skill-3D-4B 相对 w/o Tools 基线提升 59.7%，Skill-3D-8B 提升 60.3%。更强的 8B 结果说明更大基础模型能更好利用检索技能和工具证据，而稳定的 4B 提升说明较小 agent 也能通过后训练学习场景感知技能。

### Fig. 3. 有效工具使用率分析

![Fig. 3](fig3_effective_tool_usage.png)

**Caption:** Figure 3: Effective tool usage analysis. The figure reports the percentage of tool calls that contribute valid, relevant evidence to the final answer across VSI-Bench, BLINK, CV-3D, and MMSI-Bench.

**Caption[CN]:** 图 3：有效工具使用率分析。该图报告在 VSI-Bench、BLINK、CV-3D 和 MMSI-Bench 上，真正为最终答案提供有效且相关证据的工具调用比例。

**Reading note:** 核心不是“调用更多工具”，而是“调用后真的产生并使用有效证据”。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> The ablation first examines effective tool usage, defined as the fraction of tool calls that return valid evidence and are actually used by the agent. A tool output is counted as used when it is referenced later, passed to downstream tools, or supports the final answer. ETU is computed after the full rollout, so both execution validity and downstream usage are assessed.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 消融实验首先考察 effective tool usage，即返回有效证据并被 agent 实际使用的工具调用比例。当工具输出在后续推理中被引用、传给下游工具，或用于支撑最终答案时，才算被使用。ETU 在完整 rollout 结束后计算，因此同时评估工具执行有效性和下游证据使用。

$$
ETU = (1 / |A|) Σa∈A I[Valid(a) ∧ Used(a)]
$$

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Skill-3D substantially improves ETU over direct Tool-Use: from 39.2% to 78.7% on VSI-Bench, 36.4% to 79.2% on BLINK, 31.8% to 87.5% on CV-3D, and 30.5% to 80.3% on MMSI-Bench. Since ETU is normalized by the total number of tool calls, the gains indicate that Skill-3D does not simply invoke more tools; it selects evidence-producing tools and integrates the returned evidence.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 相比直接 Tool-Use，Skill-3D 显著提升 ETU：VSI-Bench 从 39.2% 到 78.7%，BLINK 从 36.4% 到 79.2%，CV-3D 从 31.8% 到 87.5%，MMSI-Bench 从 30.5% 到 80.3%。由于 ETU 按总工具调用次数归一化，这些提升表明 Skill-3D 并非只是调用更多工具，而是选择能产生证据的工具，并整合返回证据。

### Fig. 4. 工具使用分布

![Fig. 4](fig4_tool_distribution.png)

**Caption:** Figure 4: Tool usage distribution analysis. The figure illustrates the tool usage distributions of GPT-5.4, Think3D, and Skill-3D across two different kinds of problems on VSI-Bench.

**Caption[CN]:** 图 4：工具使用分布分析。该图展示 GPT-5.4、Think3D 和 Skill-3D 在 VSI-Bench 两类问题上的工具调用分布。

**Reading note:** Skill-3D 对深度/距离/尺寸问题更多调用 Depth Anything 3，对方向/关系问题更多调用 Orient Anything v2。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Tool usage distribution shows that GPT-5.4 and Think3D have clear tool-selection biases: Think3D heavily relies on Pi3 for depth-, distance-, and size-related tasks, while GPT-5.4 mostly calls GroundingDINO. Skill-3D shifts tool distribution toward the evidence needed by the task: Depth Anything 3 for depth, distance, and size, and Orient Anything v2 for spatial relation and direction reasoning, while still using Pi3, GroundingDINO, and SAM3 for layout, localization, and boundary verification.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 工具使用分布显示，GPT-5.4 和 Think3D 都有明显工具选择偏置：Think3D 在深度、距离和尺寸相关任务中过度依赖 Pi3，而 GPT-5.4 主要调用 GroundingDINO。Skill-3D 会把工具分布转向任务所需证据：对深度、距离和尺寸使用 Depth Anything 3，对空间关系和方向推理使用 Orient Anything v2，同时仍适度使用 Pi3、GroundingDINO 和 SAM3 进行布局、定位和边界验证。

### Table 3. 模块消融

![Table 3](table3_ablation.png)

**Caption:** Table 3: Module ablation of Skill-3D on VSI-Bench. Delta Avg. denotes the performance drop compared with the full Skill-3D pipeline. All experiments are conducted using GPT-5.4, and all metrics are obtained on the test set.

**Caption[CN]:** 表 3：Skill-3D 在 VSI-Bench 上的模块消融。Delta Avg. 表示相对完整 Skill-3D 流程的平均性能下降。所有实验使用 GPT-5.4，所有指标均来自测试集。

**Reading note:** 最大降幅来自去掉 skill retrieval，其次是去掉 MLLM skill selection，说明检索与选择共同决定工具规划质量。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Module ablations show complementary roles for static skills, dynamic workflows, and failure lessons. Removing failure lessons reduces the average score from 69.9 to 68.1; removing dynamic skills reduces it to 67.8; removing static skills drops it to 65.6. Thus static skills provide general task-level priors, dynamic skills adapt them to scene-specific contexts, and failure lessons help avoid recurring error modes.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 模块消融显示 static skills、dynamic workflows 和 failure lessons 作用互补。去掉 failure lessons 平均分从 69.9 降到 68.1；去掉 dynamic skills 降到 67.8；去掉 static skills 降到 65.6。因此，static skills 提供通用任务级先验，dynamic skills 将其适配到特定场景上下文，failure lessons 则帮助避免重复出现的错误模式。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> Retrieval and selection are also complementary. Removing MLLM skill selection lowers the average score from 69.9 to 65.5, suggesting that top-k retrieval alone can include redundant or partially matched skills. Removing skill retrieval further drops the score to 64.1, showing that scene-task-relevant skills are crucial for effective tool planning.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 检索与选择同样互补。去掉 MLLM skill selection 后，平均分从 69.9 降到 65.5，说明仅靠 top-k 检索可能引入冗余或部分匹配技能。去掉 skill retrieval 后进一步降到 64.1，说明与场景-任务相关的技能对有效工具规划至关重要。

### Fig. 5. 技能更新与冷启动

![Fig. 5](fig5_skill_updating_cold_start.png)

**Caption:** Figure 5: Effect of skill updating and cold start during GRPO training. Experiments are conducted using Qwen3-VL-8B as the base model.

**Caption[CN]:** 图 5：GRPO 训练期间技能更新与冷启动的影响。实验以 Qwen3-VL-8B 为基础模型。

**Reading note:** 离线冻结 Skill Library 并先做 SFT warm-up 的训练曲线最稳定，在线更新会引入非平稳性。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> For GRPO training, the paper compares Offline, Online, and Offline without cold start. Offline freezes the dynamic Skill Library during GRPO; Online updates dynamic skills during training; Offline without cold start removes the agentic SFT warm-up and directly applies GRPO. The offline variant with SFT cold start achieves the most stable and highest reward trajectory, while online updating introduces non-stationarity and removing cold start leads to early degradation and slower convergence.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> 对于 GRPO 训练，论文比较 Offline、Online 和 Offline without cold start。Offline 在 GRPO 期间冻结 dynamic Skill Library；Online 在训练中更新 dynamic skills；Offline without cold start 去掉 agentic SFT warm-up，直接做 GRPO。带 SFT cold start 的 offline 变体得到最稳定且最高的奖励曲线；在线更新会引入非平稳性，去掉 cold start 会导致早期退化和收敛更慢。

## 5 Conclusion and Limitations

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper presents Skill-3D as a framework for agentic 3D spatial reasoning with reusable scene-aware skills. Existing tool-augmented MLLM agents often apply uniform tool-use strategies across heterogeneous 3D scenes, leading to biased tool preferences and insufficient evidence acquisition. Skill-3D constructs a Scene Memory of tool-use trajectories and evolves a Skill Library where successful trajectories are distilled into reusable skills and failed trajectories are retained as lessons. Retrieved skills guide tool planning, evidence collection, and answer grounding, and skill-guided post-training transfers this behavior into compact agents.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文提出 Skill-3D：一个使用可复用场景感知技能进行 agentic 3D 空间推理的框架。现有工具增强 MLLM agent 往往在异质 3D 场景中采用统一工具策略，导致工具偏置和证据获取不足。Skill-3D 构建工具使用轨迹的 Scene Memory，并演化 Skill Library：成功轨迹被蒸馏为可复用技能，失败轨迹被保留为 lessons。检索到的技能指导工具规划、证据收集和答案 grounding，而技能引导后训练把这种行为迁移到小型 agent 中。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The limitation is that the current evaluation focuses on indoor 3D spatial reasoning. Transferring the framework to outdoor scenes, embodied navigation, or real-time robotic interaction may require new tool interfaces, scene signatures, and safety constraints.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 局限性在于当前评测集中在室内 3D 空间推理。若要迁移到室外场景、具身导航或实时机器人交互，可能需要新的工具接口、场景签名和安全约束。

## Appendix A. LLM Usage Claim

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The authors state that large language models were used only for language polishing, grammar correction, and improving manuscript clarity. All method design, experimental settings, data analysis, and final claims were developed, verified, and approved by the authors.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 作者声明，大语言模型仅用于语言润色、语法纠正和提升稿件清晰度。所有方法设计、实验设置、数据分析和最终论断均由作者开发、验证并批准。

## Appendix B. More Experimental Results

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The efficiency analysis compares inference cost and tool-use quality on VSI-Bench. Direct tool use only slightly improves average score, with 39.2% effective tool usage. Think3D improves accuracy but incurs higher inference cost, requiring 35.1 seconds per query on average. Skill-3D achieves the best score of 70.0, raises effective tool usage to 78.7%, and reduces average inference time to 20.8 seconds with only 0.5 seconds of retrieval overhead.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 效率分析比较 VSI-Bench 上的推理成本和工具使用质量。直接工具使用只小幅提高平均分，有效工具使用率为 39.2%。Think3D 提升准确率，但推理成本更高，平均每个查询需要 35.1 秒。Skill-3D 得到最佳平均分 70.0，把有效工具使用率提升到 78.7%，并将平均推理时间降至 20.8 秒，其中检索开销仅 0.5 秒。

### Table B.1. 效率分析

![Table B.1](table_b1_efficiency.png)

**Caption:** Table B.1: Efficiency analysis on VSI-Bench. The table reports the average number of tool calls, effective tool usage, average inference time per query, and performance gain. All experiments are conducted using GPT-5.4.

**Caption[CN]:** 表 B.1：VSI-Bench 上的效率分析。该表报告平均工具调用次数、有效工具使用率、每个查询的平均推理时间和性能增益。所有实验使用 GPT-5.4。

**Reading note:** Skill-3D 的调用次数更多，但有效使用率显著更高，平均运行时间低于 Think3D。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The cross-benchmark transfer analysis evaluates whether dynamic skills generalize across benchmarks. Skills learned from VSI-Bench transfer to MMSI-Bench and CV-3D, while MMSI-Bench skills also improve VSI-Bench. Pooling all training benchmarks achieves the best results, suggesting that related spatial reasoning tasks share reusable tool-use procedures and that the Skill Library benefits from complementary scene-task knowledge.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 跨基准迁移分析评估 dynamic skills 是否能跨基准泛化。从 VSI-Bench 学到的技能可迁移到 MMSI-Bench 和 CV-3D，而 MMSI-Bench 技能也能提升 VSI-Bench。合并所有训练基准得到最佳结果，说明相关空间推理任务共享可复用工具流程，Skill Library 能从互补的场景-任务知识中获益。

### Table B.2. 跨基准技能迁移

![Table B.2](table_b2_transfer.png)

**Caption:** Table B.2: Cross-benchmark skill transfer. Dynamic skills are built from one source benchmark and evaluated on other target benchmarks. All settings use the same static skills and GPT-5.4.

**Caption[CN]:** 表 B.2：跨基准技能迁移。作者从一个源基准构建动态技能，并在其他目标基准上评估。所有设置使用相同静态技能与 GPT-5.4。

**Reading note:** All Benchmarks 最优，说明不同空间任务之间存在可复用的工具流程。

## Appendix C. Experimental Details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The dataset details clarify that VSI-Bench, BLINK, CV-3D, and MMSI-Bench do not provide official training splits for skill construction or post-training. The authors therefore use a category-wise random split and ensure question-level disjointness. VSI-Bench covers egocentric indoor visual spatial intelligence; BLINK uses a multi-view spatial subset; CV-3D focuses on geometric spatial reasoning; and MMSI-Bench focuses on positional relationship reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 数据集细节说明，VSI-Bench、BLINK、CV-3D 和 MMSI-Bench 都没有为技能构建或后训练提供官方训练划分。因此作者采用类别级随机划分，并确保问题级互斥。VSI-Bench 覆盖第一视角室内视觉空间智能；BLINK 使用多视角空间子集；CV-3D 聚焦几何空间推理；MMSI-Bench 聚焦位置关系推理。

### Table C.3. 数据集划分

![Table C.3](table_c3_dataset_split.png)

**Caption:** Table C.3: Dataset statistics and train/test split. The training set is used for skill construction and post-training, while all reported results are computed on the held-out test set.

**Caption[CN]:** 表 C.3：数据集统计与训练/测试划分。训练集用于技能构建和后训练，所有报告结果都在 held-out 测试集上计算。

**Reading note:** 四个基准均采用问题级互斥划分，训练样本被用于技能构建与 SFT/GRPO。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The hyperparameter table reports the post-training configuration. The foundation models are Qwen3-VL-4B/8B, max sequence length is 4096, training precision is bfloat16, optimizer is AdamW, SFT uses learning rate 1e-5 and batch size 16 for one epoch, while GRPO uses learning rate 1e-6, batch size 16, group size 8, gradient accumulation 4, clipping epsilon 0.2, and KL coefficient 0.05.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 超参数表报告后训练配置。基础模型为 Qwen3-VL-4B/8B，最大序列长度 4096，训练精度 bfloat16，优化器 AdamW。SFT 使用 1e-5 学习率、batch size 16、训练 1 个 epoch；GRPO 使用 1e-6 学习率、batch size 16、group size 8、梯度累积 4、clipping epsilon 0.2、KL 系数 0.05。

### Table C.4. 后训练超参数

![Table C.4](table_c4_hyperparameters.png)

**Caption:** Table C.4: Hyperparameter settings of Skill-3D.

**Caption[CN]:** 表 C.4：Skill-3D 的超参数设置。

**Reading note:** SFT 学习率为 1e-5，GRPO 学习率为 1e-6，group size 为 8，KL 系数为 0.05。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The appendix gives the full GRPO objective. For each query, the policy samples G complete trajectories from the current policy; rewards are normalized within the sampled group to compute relative advantages. The clipped surrogate objective uses the importance ratio between current and old policies, with a KL term to preserve SFT-learned skill-selection and tool-use behavior. This favors trajectories with higher task success, better tool-use efficiency, and valid outputs.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 附录给出了完整 GRPO 目标。对每个查询，策略从当前策略采样 G 条完整轨迹；奖励在组内归一化以计算相对 advantage。裁剪 surrogate objective 使用当前策略与旧策略之间的重要性比率，并加入 KL 项来保持 SFT 学到的技能选择和工具使用行为。这会偏好任务成功率更高、工具使用效率更好且输出有效的轨迹。

$$
Ai = (R(τi) - mean({R(τj)}j=1..G)) / std({R(τj)}j=1..G)
$$

$$
J(θ) = E[ (1/G) Σi=1..G min(ρi Ai, clip(ρi, 1 - ε, 1 + ε) Ai) - βKL DKL(πθ || πref) ]
$$

$$
ρi = πθ(τi | q, O, Scand) / πold(τi | q, O, Scand)
$$

## Appendix D. Qualitative Results

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper shows two representative cases: metric distance estimation and room-level object counting. In the distance case, Think3D calls Pi3 reconstruction and object detection but remains reconstruction-centric; because the table and bathtub appear in different partial views and closest boundaries are not explicitly grounded, it overestimates the distance as 1.5m. Skill-3D retrieves a depth-distance skill and combines Pi3, object detection, and depth estimation, grounding closest object boundaries and predicting the correct 0.9m.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文展示两个代表性案例：metric distance 估计和房间级目标计数。在距离案例中，Think3D 调用 Pi3 重建和目标检测，但仍以重建为中心；由于桌子和浴缸出现在不同局部视角中，最近边界没有被显式 grounding，它把距离高估为 1.5m。Skill-3D 检索 depth-distance 技能，并结合 Pi3、目标检测和深度估计，对最近物体边界进行 grounding，预测正确的 0.9m。

### Fig. E.1. 边界感知距离推理案例

![Fig. E.1](fig_e1_distance_case.png)

**Caption:** Figure E.1: Case study on boundary-aware metric distance reasoning. Colored highlights indicate different reasoning elements: red marks the question and incorrect answer, green marks the ground-truth or correct answer, teal marks invoked tools, purple marks retrieved skills, and yellow marks iteration or answer labels. Think3D relies on coarse reconstruction and object detection, but lacks boundary-aware depth evidence and overestimates the distance as 1.5m. Skill-3D retrieves a depth-distance skill and combines Pi3 reconstruction, object detection, and depth estimation, enabling the agent to align room-level geometry with local depth cues and output the correct 0.9m answer.

**Caption[CN]:** 图 E.1：边界感知 metric distance 推理案例。彩色高亮表示不同推理元素：红色为问题和错误答案，绿色为真值或正确答案，青色为调用工具，紫色为检索技能，黄色为迭代或答案标签。Think3D 依赖粗粒度重建和目标检测，但缺少边界感知深度证据，因此将距离高估为 1.5m。Skill-3D 检索 depth-distance 技能，并结合 Pi3 重建、目标检测和深度估计，使 agent 能把房间级几何与局部深度线索对齐，输出正确的 0.9m。

**Reading note:** 该案例展示 Skill-3D 为什么要根据“最近边界距离”选择深度和检测证据。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> In the counting case, Think3D mainly relies on Pi3 reconstruction and coarse cross-view matching, causing repeated observations of the same chair to be counted multiple times. Skill-3D retrieves a detection-counting skill and combines Pi3 layout consistency with object detection evidence, grounding chair instances across views and suppressing duplicates to obtain the correct count of four.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在计数案例中，Think3D 主要依赖 Pi3 重建和粗粒度跨视角匹配，导致同一把椅子的重复观测被多次计数。Skill-3D 检索 detection-counting 技能，并结合 Pi3 布局一致性和目标检测证据，在跨视角中 grounding 椅子实例并抑制重复，得到正确计数四。

### Fig. E.2. 多视角计数案例

![Fig. E.2](fig_e2_counting_case.png)

**Caption:** Figure E.2: Case study on multi-view object counting. Colored highlights indicate different reasoning elements: red marks the question and incorrect answer, green marks the ground-truth or correct answer, teal marks invoked tools, purple marks retrieved skills, and yellow marks iteration or answer labels. Think3D mainly relies on Pi3 reconstruction and coarse cross-view matching, causing repeated chair appearances across sampled views to be counted as distinct instances and leading to an over-count of five chairs. Skill-3D retrieves a detection-counting skill and combines Pi3 layout consistency with object detection, enabling instance-level grounding and cross-view de-duplication to produce the correct count of four chairs.

**Caption[CN]:** 图 E.2：多视角目标计数案例。彩色高亮含义同图 E.1。Think3D 主要依赖 Pi3 重建和粗粒度跨视角匹配，导致同一把椅子在相邻视角中被重复计数，得到错误的五把椅子。Skill-3D 检索 detection-counting 技能，并结合 Pi3 布局一致性与目标检测，从而完成实例级定位和跨视角去重，得到正确的四把椅子。

**Reading note:** 该案例说明计数任务需要实例检测和跨视角去重，而不仅是场景重建。

## Appendix E. Prompt Design

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The prompt-design appendix provides detailed prompts for each stage of Skill-3D. The system prompt defines the agent’s goal as answering visual spatial reasoning questions by combining scene memory, static and dynamic skills, external perception or geometry tools, and final reasoning grounded in tool evidence. It instructs the agent not to answer metric, boundary-sensitive, counting, localization, or orientation questions from RGB intuition alone when relevant tools or skills are available.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 提示词设计附录给出 Skill-3D 各阶段的详细 prompt。系统提示词把 agent 的目标定义为：结合场景上下文记忆、静态与动态技能、外部感知或几何工具，以及基于工具证据的最终推理，来回答视觉空间推理问题。它要求 agent 在有相关工具或技能可用时，不要仅凭 RGB 直觉回答 metric、边界敏感、计数、定位或朝向问题。

### Fig. E.3. System Prompt

![Fig. E.3](fig_e3_system_prompt.png)

**Caption:** Figure E.3: System Prompt.

**Caption[CN]:** 图 E.3：系统提示词。

**Reading note:** 提示词把 Skill-3D agent 的内部流程约束为场景理解、技能检索、工具规划、工具证据吸收和最终回答。

### Fig. E.4. System Prompt and Scene Context Prompt

![Fig. E.4](fig_e4_system_scene_context_prompt.png)

**Caption:** Figure E.4: System Prompt and Scene Context Prompt.

**Caption[CN]:** 图 E.4：系统提示词和场景上下文提示词。

**Reading note:** 该图补充要求 agent 在工具选择前先识别场景类型、任务范围、目标物体和所需证据。

### Fig. E.5. Skill Retrieval、Tool Planning 与 Tool Exclusion Prompt

![Fig. E.5](fig_e5_retrieval_planning_exclusion_prompt.png)

**Caption:** Figure E.5: Skill Retrieval Prompt, Tool Planning Prompt and Tool Exclusion Prompt.

**Caption[CN]:** 图 E.5：技能检索提示词、工具规划提示词和工具排除提示词。

**Reading note:** 该图对应从技能候选中选取最小充分工作流，并避免冗余或无效工具调用。

### Fig. E.6. Tool Exclusion 与 Final Answer Prompt

![Fig. E.6](fig_e6_tool_final_prompts.png)

**Caption:** Figure E.6: Tool Exclusion Prompt and Final Answer Prompt.

**Caption[CN]:** 图 E.6：工具排除提示词和最终回答提示词。

**Reading note:** 最终回答提示强调使用工具证据、避免过度精确，并在证据不足时输出合理范围。

## References

The source PDF contains a bibliography on pp.9-13. It is preserved in the original PDF and indexed in `translation_notes.md`; bibliography entries are not translated line-by-line because they are citation metadata rather than paper body prose.

## Critical Reading Notes

- The core claim is not that tools alone improve 3D reasoning, but that scene-conditioned tool workflows improve whether the right evidence is acquired and used.
- The strongest evidence is the combination of Table 1/2 accuracy gains and Fig. 3 ETU gains; together they support both outcome improvement and mechanism-level tool-use improvement.
- The main assumption is that scene-task parsing and benchmark-defined evidence requirements are reliable enough to supervise rewards and skill updates.
- The main open risk is external validity: the paper evaluates indoor 3D reasoning, so outdoor, robotic, or real-time settings may require different tools, safety constraints, and scene signatures.
