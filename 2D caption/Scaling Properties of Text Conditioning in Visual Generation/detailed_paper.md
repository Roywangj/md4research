# Scaling Properties of Text Conditioning in Visual Generation

**Authors:** Zilong Chen, Chaorui Deng, Kunchang Li, Hongyi Yuan, Haoqi Fan  
**Affiliation:** ByteDance Seed  
**Source:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/MUQ6N8C7/Chen 等 - SCALING PROPERTIES OF TEXT CONDITIONING IN VISUAL GENERATION.pdf`  
**Detected source format:** selectable-text PDF (`pdf-text`), with page-render verification  
**Reader type:** complete paragraph-level Chinese-English detailed reader  
**Document status:** Complete — 61 PDF pages, including main text, references, Appendices A–G, exact system prompts and retained qualitative prompts.

## Page / Section Index

| PDF pages | Source sections |
|---|---|
| 1–3 | Title, Abstract, Figures 1–3 |
| 3–5 | 1 Introduction; 2 Related Work |
| 5–13 | 3 Method; 3.1–3.4; Figures 4–10; Table 1 |
| 14–19 | 4 Experiments; 4.1–4.3; 5 Conclusion and Limitations; Figures 11–15; Tables 2–5 |
| 19–23 | References |
| 24–30 | Appendix contents; A GPG details; B ED validation; Figures 16–18; Tables 6–9 |
| 30–37 | C Schema and implementation; Figure 19; Tables 10–14 |
| 36–41 | D Benchmark breakdowns; Tables 15–18 |
| 41–52 | E System prompts and evaluation protocols (verbatim listings) |
| 52–55 | F Exact prompts for main-paper figures |
| 55–61 | G Additional qualitative examples; Figures 20–24 |

## Terminology Ledger

| Canonical term | 中文约定 | Definition / note |
|---|---|---|
| text conditioning | 文本条件控制 | Text supplied to condition visual generation |
| structured prompt (SP) | 结构化提示（SP） | Typed JSON caption with global, per-element, and cross-element fields |
| natural language (NL) | 自然语言（NL） | Free-form prose caption |
| caption informativeness | 描述信息量 | Image-grounded information exposed by a caption |
| Grounded Perplexity Gain (GPG) | 接地困惑度增益（GPG） | White-box summed content-token likelihood gain from revealing the paired image |
| Effective Detailness (ED) | 有效细节度（ED） | Black-box precision-weighted image-grounded attribute coverage score |
| diffusability | 可扩散性 | How effectively a caption interface exposes and organizes supervision for the diffuser |
| promptability | 提示构造能力 | How effectively an LLM instantiates the interface from a user request |
| on-policy self-distillation (OPSD) | 在策略自蒸馏（OPSD） | Image-conditioned teacher distillation on accepted student rollouts |
| verifier-gated RFT | 验证器门控强化微调 | RFT that retains only rollouts passing structure, alignment, and aesthetic gates |
| GSB net preference | GSB 净偏好 | $100(n_{Good}-n_{Bad})/N$, with order-inconsistent pairs counted Same |
| converged MSE | 收敛 MSE | Matched-budget diffusion training loss readout |

---


## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We study empirical scaling properties for text conditioning in visual generation. Such properties have rarely been measured because diffusion loss does not scale with the number of tokens in natural-language prompts. Surprisingly, we find that the converged diffusion loss scales with the amount of structured language in the prompt. To quantify structured language, we adapt two complementary measures: a white-box likelihood metric (GPG) and a black-box attribute metric (ED). Across controlled training runs, the converged diffusion loss decreases approximately linearly with GPG and follows a power law with ED. Guided by these scaling properties, we improve diffusability by constructing structured prompts with semantic and geometric annotations derived from images, and improve promptability by training a prompter through supervised fine-tuning, cold-start, and verifier-gated on-policy distillation. The resulting system outperforms all evaluated open-weight models on nearly every compositional, reasoning, and world-knowledge benchmark, while matching or surpassing the strongest closed-weight models on most evaluations.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们研究视觉生成中文本条件的经验缩放性质。此类性质过去很少被测量，因为扩散损失并不会随自然语言提示中的 token 数量而缩放。令人意外的是，我们发现，收敛后的扩散损失会随提示中结构化语言的数量而缩放。为量化结构化语言，我们采用了两种互补的度量：白盒似然指标（GPG）和黑盒属性指标（ED）。在受控训练实验中，收敛扩散损失随 GPG 近似线性下降，并与 ED 呈幂律关系。在这些缩放性质的指导下，我们通过构建带有由图像导出的语义与几何标注的结构化提示来提高可扩散性，并通过监督微调、冷启动和验证器门控的同策略蒸馏来训练提示器，从而提高可提示性。所得系统在几乎所有组合、推理和世界知识基准上都优于所评估的全部开放权重模型，同时在大多数评估中达到或超过最强的闭源模型。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Figure 1: Information, not token count, is what scales in prompt enhancement for image generation.** Naively increasing prompt length degrades performance across all evaluated open-weight models (Qwen-Image, HunyuanImage 3.0, BAGEL, FLUX.1 Dev, and Emu3), every one of them ending below its own shortest caption; a control of ours trained on that same prose ladder improves only slightly before saturating. Under our structured-prompt schema, however, the GSB net preference rises monotonically with caption length, because structured prompts add new image-grounded information rather than more words. Finetuning the prompter that writes them (finetuned structured) yields a further large margin over the zero-shot structured prompter. (Left) Each system is judged against its own shortest-caption output, so the axis measures gain from lengthening rather than absolute quality; GSB is a VLM good/same/bad net preference over 150 prompts, with every prompt enhancer off. FLUX.1 Dev’s text encoder truncates past 512 tokens, so its curve is dotted beyond that rung. (Right) Why: prose saturates in information while structure keeps gaining (top), yet at matched information both land on one fit (bottom).

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 1：在图像生成的提示增强中，发生缩放的是信息，而不是 token 数量。** 直接增加提示长度会使所有被评估的开放权重模型（Qwen-Image、HunyuanImage 3.0、BAGEL、FLUX.1 Dev 和 Emu3）的性能下降；每个模型最终都低于其自身最短描述对应的结果；我们在同一自然语言阶梯上训练的对照模型仅略有改善，随后便趋于饱和。然而，在我们的结构化提示模式下，GSB 净偏好随描述长度单调上升，因为结构化提示增加的是新的图像扎根信息，而不是更多词语。对生成这些提示的提示器进行微调（finetuned structured），相较零样本结构化提示器又带来显著优势。（左）每个系统都与其自身最短描述的输出比较，因此纵轴衡量的是增长描述所带来的增益，而非绝对质量；GSB 是 VLM 在 150 条提示上的 good/same/bad 净偏好，且所有提示增强器均关闭。FLUX.1 Dev 的文本编码器会截断超过 512 token 的内容，因此该阶梯之后的曲线用虚线表示。（右）原因：自然语言的信息量趋于饱和，而结构化表示持续增加信息（上）；但在信息量匹配时，两者落在同一拟合关系上（下）。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Figure 2: Qualitative results and zero-shot editing.** (Top) Outputs from our final system across multi-object scenes, dense text, complex layouts, and branded illustration. The trained LLM prompter expands each user request into an information-dense structured prompt (SP), which the SP-trained diffuser renders. Appendix F.1 lists the corresponding prompts. (Bottom) Because the SP exposes image factors as editable fields, a targeted field edit and regeneration can change a specific aspect—object position, material, scene, or global style—while preserving much of the remaining composition; diffs show added / removed values, and Move updates the relevant old/new bboxes.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **图 2：定性结果与零样本编辑。**（上）最终系统在多物体场景、密集文本、复杂布局和品牌插画任务上的输出。训练后的 LLM 提示器将每个用户请求扩展为信息密集的结构化提示（SP），再由经过 SP 训练的扩散器进行渲染。附录 F.1 列出了相应提示。（下）由于 SP 将图像因素暴露为可编辑字段，对特定字段进行定向编辑并重新生成，就可以改变某一具体方面——物体位置、材质、场景或全局风格——同时保留其余大部分构图；差异中展示了新增／删除的值，而 Move 会更新相关的新旧边界框。

## 1 Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Figure 3: A fixed-backbone probe separates caption information from caption length.** Using the same Qwen-Image backbone and seed, we reconstruct a held-out reference (left) from natural-language (NL, top) and structured-prompt (SP, bottom) captions at four levels. The NL captions preserve the same entities and relationships while increasing in length, yet reconstruction remains flat; progressively restoring SP fields improves all three metrics. The displayed NL lengths are measured with the Qwen2.5-VL tokenizer. Metrics are DINOv3/SigLIP2 cosine (↑) and LPIPS distance (↓); colors mark changes from L5. Appendices C.2 and F.3 provide the full controls and prompts.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **图 3：固定骨干网络探针将描述信息量与描述长度区分开来。** 使用相同的 Qwen-Image 骨干网络和随机种子，我们分别依据四个层级的自然语言描述（NL，上）和结构化提示描述（SP，下）重建一个留出的参考图像（左）。NL 描述在长度增加时保留相同的实体与关系，但重建性能基本不变；逐步恢复 SP 字段则会改善全部三个指标。图中 NL 长度由 Qwen2.5-VL tokenizer 测得。指标为 DINOv3/SigLIP2 余弦相似度（↑）和 LPIPS 距离（↓）；颜色表示相对于 L5 的变化。附录 C.2 和 F.3 给出了完整对照与提示。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Large language models have advanced through scaling model size, training data, and compute (Kaplan et al., 2020; Hoffmann et al., 2022). Text-to-image generation has followed the same recipe, with larger diffusion backbones, heavier training runs (Podell et al., 2023; Esser et al., 2024), and larger captioned-image corpora (Schuhmann et al., 2022). Yet this analogy hides a basic asymmetry. A language model receives its training signal from the text stream itself, whereas a text-to-image model learns text-conditioned generation through image–caption pairs. Visual content that a caption binds ambiguously reaches the model only weakly as conditioning supervision, and content the caption omits does not reach it at all, though both remain present in the pixels. The image-grounded information in a caption may therefore limit what a generator can learn to recover from text, but it has rarely been treated as an explicit training variable. We ask whether increasing this information can improve visual generation, particularly on information-dense prompts where current systems struggle with objects, layouts, relations, and visual coherence (Jiao et al., 2025; Yang et al., 2026; Wei et al., 2025). Figure 1 previews the answer. Given progressively longer natural-language captions, every existing system we evaluate peaks early if at all and ends below its own shortest caption, and a diffuser of ours trained on that same ladder improves only slightly before saturating: prose does not scale, whether a system is merely prompted with it or trained on it. Quality keeps rising only when the added tokens carry more image-grounded information, which structured captions supply and which also predicts converged diffusion loss.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 大语言模型通过扩大模型规模、训练数据和计算量取得了进步（Kaplan et al., 2020; Hoffmann et al., 2022）。文本到图像生成沿用了同样的方案：更大的扩散骨干网络、更重的训练过程（Podell et al., 2023; Esser et al., 2024），以及更大规模的带描述图像语料库（Schuhmann et al., 2022）。然而，这一类比掩盖了一种基本的不对称性。语言模型直接从文本流本身获得训练信号，而文本到图像模型则通过图像—描述对学习文本条件生成。若描述对某些视觉内容的绑定含糊，这些内容只能作为很弱的条件监督传递给模型；若描述完全省略某些内容，它们便根本无法传递给模型，尽管两者仍然存在于像素中。因此，描述中的图像扎根信息可能限制生成器从文本中学会恢复的内容，但它很少被当作一个显式训练变量。我们考察增加这种信息能否改善视觉生成，尤其是针对信息密集型提示——当前系统在其中难以处理物体、布局、关系与视觉连贯性（Jiao et al., 2025; Yang et al., 2026; Wei et al., 2025）。图 1 预示了答案。随着自然语言描述逐渐变长，我们评估的每个现有系统即便有所提升也很早达到峰值，并最终低于各自最短描述的表现；我们在同一阶梯上训练的扩散器也仅有轻微改善，随后饱和：无论系统只是接收自然语言提示，还是用自然语言进行训练，散文式描述都无法缩放。只有当新增 token 携带更多图像扎根信息时，质量才会持续提高；结构化描述正能提供这种信息，而该信息也能预测收敛扩散损失。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> We begin with the fixed-backbone reconstruction probe shown in Figure 3. Starting from one reference image, we annotate it in detail, then verbalize that annotation as natural-language (NL) captions of increasing length and condition the same trained diffusion model on each to reconstruct the reference. Because they share one source annotation, these NL captions grow longer by elaborating the same annotated entities and relationships rather than adding new ones, and reconstruction quickly saturates. This suggests that verbosity alone does not improve what the diffuser can recover, motivating a representation that makes visual variables explicit. We therefore introduce structured prompts (SPs), a typed semantic representation serialized as JSON. Dedicated fields for global scene context, per-element properties and geometry, and cross-element relations expose the same annotation in a precise, consistently addressable form. Reconstruction improves steadily as schema coverage increases. To quantify caption information beyond this illustrative probe, we adapt two complementary metrics from prior work: Grounded Perplexity Gain (GPG), which measures how much revealing the paired image raises a caption’s likelihood under a frozen vision–language model (Favero et al., 2024), and Effective Detailness (ED), which measures the precision and recall of caption attributes against image-grounded references (Wang et al., 2025b; Cheng et al., 2024).

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 我们从图 3 所示的固定骨干网络重建探针开始。以一张参考图像为起点，我们对其进行详细标注，再将该标注表述成长度递增的自然语言（NL）描述，并分别以这些描述为条件，让同一个已训练的扩散模型重建参考图像。由于这些 NL 描述共享同一份源标注，其长度增长来自对相同标注实体与关系的展开说明，而不是增加新内容，因此重建效果很快饱和。这表明，仅仅增加冗长程度并不会改善扩散器能够恢复的内容，由此促使我们寻求一种能显式呈现视觉变量的表示。为此，我们引入结构化提示（SP），即一种序列化为 JSON 的有类型语义表示。针对全局场景语境、逐元素属性与几何信息以及跨元素关系设置专用字段，以精确且始终可寻址的形式呈现同一份标注。随着模式覆盖范围增加，重建效果持续改善。为超越这一示意性探针并量化描述信息，我们从先前工作中采用两项互补指标：Grounded Perplexity Gain（GPG），衡量向冻结的视觉—语言模型揭示配对图像后，描述似然提高了多少（Favero et al., 2024）；以及 Effective Detailness（ED），依据图像扎根参考来衡量描述属性的精确率和召回率（Wang et al., 2025b; Cheng et al., 2024）。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Using GPG and ED as complementary measures, we systematically study how caption informativeness influences diffusion training, with converged diffusion loss as the training-side readout. We sweep NL and SP caption formats and detail levels, running a separate diffusion training run for each condition while holding the image data, architecture, initialization, and compute fixed. Across this sweep, converged diffusion loss is well fit by a linear function of GPG and follows a power-law trend in ED. We call these two relations the scaling properties of text conditioning under the controlled recipe. Once calibrated, they can rank candidate caption conditions within the tested range before another diffusion training run. They therefore isolate a format-side capability, which we call diffusability: how effectively a caption representation exposes and organizes image-grounded information for diffusion learning. To raise it at scale, we first use an image-to-SP annotation pipeline that combines a VLM with frozen domain experts for human pose, depth, and segmentation to generate full-schema SPs, and then train the diffuser on the resulting organized supervision.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 我们以 GPG 和 ED 作为互补度量，系统研究描述的信息丰富度如何影响扩散训练，并以收敛扩散损失作为训练侧读数。我们遍历 NL 与 SP 的描述格式和细节层级，对每一种条件分别进行一次扩散训练，同时固定图像数据、架构、初始化和计算量。在这一遍历中，收敛扩散损失能够由 GPG 的线性函数很好地拟合，并随 ED 呈现幂律趋势。我们将这两种关系称为该受控方案下文本条件的缩放性质。校准之后，它们可以在再次运行扩散训练之前，对测试范围内的候选描述条件进行排序。因此，它们隔离出一种格式侧能力，我们称之为可扩散性（diffusability）：描述表示为扩散学习呈现并组织图像扎根信息的有效程度。为大规模提高这一能力，我们首先使用一个图像到 SP 的标注流水线，将 VLM 与用于人体姿态、深度和分割的冻结领域专家相结合，生成完整模式的 SP；随后使用所得的组织化监督训练扩散器。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> At test time, however, no paired image or oracle annotation is available to fill in an SP, so an LLM prompter must infer plausible visual details left unspecified by the user while preserving the explicit request. We call this capability promptability. In a zero-shot sweep, generated-image quality improves with prompter scale and, except at the smallest scale, with chain-of-thought inference. This associates progress in general-purpose LLMs with better generation through the caption interface, without task-specific training. We further raise promptability through supervised fine-tuning (SFT), cold-start distillation, and verifier-gated reinforcement fine-tuning (RFT); the final stage distills an image-conditioned teacher on verified on-policy rollouts. At inference, an agentic refine–render–judge loop further improves generation by revising the SP fields responsible for failed visual decisions.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 然而，在测试时，没有配对图像或预言机标注可用于填写 SP，因此 LLM 提示器必须在保留用户显式要求的同时，推断用户未指定的合理视觉细节。我们将这种能力称为可提示性（promptability）。在零样本遍历中，生成图像的质量会随提示器规模增大而提高；除最小规模外，思维链推理也会带来提升。这表明，无须任务特定训练，通用 LLM 的进步就能通过描述接口转化为更好的生成效果。我们还通过监督微调（SFT）、冷启动蒸馏和验证器门控的强化微调（RFT）进一步提高可提示性；最后一个阶段在经过验证的同策略 rollout 上蒸馏一个图像条件教师模型。在推理时，智能体式的细化—渲染—评判循环通过修改导致视觉决策失败的 SP 字段，进一步改善生成结果。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Together, the two factors yield an end-to-end system that leads every evaluated open-weight model on all but one reported metric and matches or surpasses the strongest closed systems on most, with the widest margins on the composition- and reasoning-heavy benchmarks. These gains extend beyond the training-loss relation to prompt fidelity, visual coherence, and compositional detail in generated images.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 两项因素结合后形成了一个端到端系统：除一项报告指标外，它在其他所有指标上都领先于每个被评估的开放权重模型，并在大多数指标上达到或超过最强的闭源系统；在高度依赖组合与推理的基准上，优势最为显著。这些增益超越了训练损失关系本身，还体现在生成图像的提示忠实度、视觉连贯性和组合细节上。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> In summary, we show how to scale text conditioning in visual generation. Our contributions are:
>
> - **Scaling properties of text conditioning.** We adapt GPG and ED to quantify caption informativeness and show that both predict converged diffusion loss under a fixed training recipe.
> - **Raising diffusability through structured prompts.** SPs organize image-grounded content into named fields, raising measured informativeness and lowering diffusion loss without architectural changes.
> - **Raising promptability through training and inference-time refinement.** Our SFT–cold-start–RFT pipeline culminates in verifier-gated on-policy self-distillation (OPSD), while field-level agentic refinement further improves generation at inference time.
> - **Scaling text conditioning end to end.** Combining the two factors yields broad gains across compositional, reasoning, and world-knowledge evaluations.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 总而言之，我们展示了如何缩放视觉生成中的文本条件。我们的贡献如下：
>
> - **文本条件的缩放性质。** 我们采用 GPG 和 ED 量化描述的信息丰富度，并表明在固定训练方案下，两者都能预测收敛扩散损失。
> - **通过结构化提示提高可扩散性。** SP 将图像扎根内容组织到命名字段中，在不改变架构的情况下提高测得的信息丰富度并降低扩散损失。
> - **通过训练与推理时细化提高可提示性。** 我们的 SFT—冷启动—RFT 流水线最终采用验证器门控的同策略自蒸馏（OPSD），而字段级智能体细化会在推理时进一步改善生成。
> - **端到端缩放文本条件。** 两项因素结合后，在组合、推理和世界知识评估上带来广泛增益。

## 2 Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Text-to-image scaling, long captions, and structured control.** Diffusion models (Ho et al., 2020; Song et al., 2021), latent diffusion (Rombach et al., 2022), and transformer backbones (Peebles & Xie, 2023; Esser et al., 2024) have advanced T2I generation largely through model-side scaling. Conditioning has also mattered: Imagen (Saharia et al., 2022) found that a larger text encoder improves fidelity, while LLM conditioners (Hu et al., 2024), long-context encoders (Zhang et al., 2024), and dense-caption corpora (Urbanek et al., 2024; Onoe et al., 2024) extend the information available in a prompt. Existing scaling laws establish a compute–loss relation for DiTs (Liang et al., 2024); we instead hold model, data, and compute fixed and show that converged diffusion loss is predicted by caption information, measured by white-box GPG or black-box ED, rather than length. This distinction is consistent with long-prompt benchmarks: DetailMaster (Jiao et al., 2025) bins prompts by token count and reports a consistent negative correlation between prompt length and accuracy on character attributes, character locations, and entity relationships, while LongT2IBench (Yang et al., 2026) reports that graph-structured alignment over entities, attributes, and relations decreases steadily across word-count intervals. TIIF-Bench (Wei et al., 2025) instead pairs each prompt with a semantically equivalent long version and finds that robustness to this change tracks overall instruction-following ability, with the strongest models remaining stable across both settings. Our measurements suggest that this behavior reflects an information plateau rather than length alone. A separate line of work intervenes on the diffuser rather than on the caption. Layout-conditioned generation (e.g., GLIGEN (Li et al., 2023)) and attention-manipulation methods (e.g., Attend-and-Excite (Chefer et al., 2023)) steer a fixed diffuser through auxiliary spatial conditions or model-internal intervention; our schema instead places boxes, depth, and relations in ordinary text fields, scored on the same GPG/ED axes as free-form captions and aimed at caption information rather than layout control.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **文本到图像缩放、长描述与结构化控制。** 扩散模型（Ho et al., 2020; Song et al., 2021）、潜空间扩散（Rombach et al., 2022）和 Transformer 骨干网络（Peebles & Xie, 2023; Esser et al., 2024）主要通过模型侧缩放推动了 T2I 生成。条件输入同样重要：Imagen（Saharia et al., 2022）发现，更大的文本编码器能够提升忠实度；LLM 条件器（Hu et al., 2024）、长上下文编码器（Zhang et al., 2024）和密集描述语料库（Urbanek et al., 2024; Onoe et al., 2024）则扩展了提示中可用的信息。现有缩放定律为 DiT 建立了计算量—损失关系（Liang et al., 2024）；我们则固定模型、数据和计算量，并表明预测收敛扩散损失的是由白盒 GPG 或黑盒 ED 测得的描述信息，而非描述长度。这一区别与长提示基准的结果一致：DetailMaster（Jiao et al., 2025）按 token 数量对提示分箱，发现提示长度与人物属性、人物位置及实体关系准确率始终负相关；LongT2IBench（Yang et al., 2026）则报告，基于实体、属性和关系的图结构对齐会随词数区间增加而持续下降。TIIF-Bench（Wei et al., 2025）改为给每条提示配对一个语义等价的长版本，并发现对这种变化的鲁棒性与整体指令遵循能力同步，最强模型在两种设置下都保持稳定。我们的测量表明，这种行为反映的是信息平台期，而不只是长度效应。另一条研究路线干预扩散器而非描述。布局条件生成（如 GLIGEN（Li et al., 2023））和注意力操纵方法（如 Attend-and-Excite（Chefer et al., 2023））通过辅助空间条件或模型内部干预来引导固定扩散器；相较之下，我们的模式把边界框、深度和关系放入普通文本字段中，并在与自由形式描述相同的 GPG/ED 坐标轴上评分，目标是描述信息而非布局控制。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Recaptioning and caption quality.** DALL-E 3 (Betker et al., 2023) showed that detailed synthetic recaptioning can markedly improve prompt following; PixArt-α (Chen et al., 2024b), PixArt-Σ (Chen et al., 2024a), CogView3 (Zheng et al., 2024), and RECAP (Segalis et al., 2023) likewise demonstrate the value of richer or more principled captions. Recent systems go beyond free-form prose. FIBO (Gutflaish et al., 2025) trains on long JSON captions, compares them with short captions under matched training, and learns a VLM translator from short requests to its schema. Cosmos 3 (NVIDIA, 2026) uses structured JSON annotations and a prompt upsampler, showing that predefined fields improve annotation recall over dense prose. Reve 2.0 (Reve Team, 2026) uses a hierarchical layout intermediary and reports gains over text-only generation as well as improved reconstruction with more regions; concurrent work by Merchant et al. (2025) studies a fixed four-part caption template. These results establish structured representation as a useful design choice. Our focus is complementary: we measure image-grounded information across NL lengths, nested SP levels, spatial serializations, and field ablations, then calibrate that common variable against matched-budget converged diffusion loss. We further isolate prompt production by varying prompter scale, reasoning, and training while holding the schema and trained diffuser fixed. GPG adapts the per-token grounding signal of Favero et al. (2024) from decoding-time hallucination localization to corpus-level caption informativeness; ED adapts caption-detailness evaluation (Wang et al., 2025b) to black-box, image-grounded caption scoring; our precision-weighted matcher is motivated by Cheng et al. (2024), who find caption precision to matter more than recall when training text-to-image models.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **重新描述与描述质量。** DALL-E 3（Betker et al., 2023）表明，细致的合成式重新描述能够显著改善提示遵循；PixArt-α（Chen et al., 2024b）、PixArt-Σ（Chen et al., 2024a）、CogView3（Zheng et al., 2024）和 RECAP（Segalis et al., 2023）同样证明了更丰富或更具原则性的描述的价值。近期系统已经超越自由形式散文。FIBO（Gutflaish et al., 2025）使用长 JSON 描述训练，在匹配训练条件下与短描述比较，并学习一个将短请求转换到其模式的 VLM 翻译器。Cosmos 3（NVIDIA, 2026）使用结构化 JSON 标注和提示上采样器，表明预定义字段相较密集散文能提高标注召回率。Reve 2.0（Reve Team, 2026）采用分层布局中介，并报告其相较纯文本生成的增益以及随着区域增多而改善的重建；Merchant et al.（2025）的同期工作研究了固定的四部分描述模板。这些结果确立了结构化表示是一项有用的设计选择。我们的关注点与之互补：我们跨 NL 长度、嵌套 SP 层级、空间序列化方式和字段消融来测量图像扎根信息，再将这一共同变量与匹配预算下的收敛扩散损失进行校准。我们还在固定模式和已训练扩散器的情况下，通过改变提示器规模、推理方式和训练来隔离提示生成。GPG 将 Favero et al.（2024）的逐 token 扎根信号从解码时幻觉定位改用于语料库级描述信息丰富度；ED 将描述细节度评估（Wang et al., 2025b）改用于黑盒、图像扎根的描述评分；我们的精确率加权匹配器受 Cheng et al.（2024）启发，后者发现训练文本到图像模型时，描述精确率比召回率更重要。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **LLM prompters, RFT, and inference-time methods.** LLMs have become effective inference-time prompt enhancers: RPG (Yang et al., 2024b) decomposes prompts into regional sub-prompts with multimodal-LLM reasoning; PromptEnhancer (Wang et al., 2025a) applies RFT to a chain-of-thought rewriter with a dedicated reward model; and input-side inference-time scaling (Chen et al., 2025) trains a rewriter with iterative DPO. These methods improve prompts for a fixed generator. Our structured format additionally raises the caption representation’s training-time diffusability; with that schema and backbone fixed, we study prompter promptability under LLM scale, chain-of-thought, verifier-gated self-distillation from an image-conditioned teacher, and an agentic refine–render–judge loop. Reward models such as ImageReward (Xu et al., 2023) and model-side preference optimization such as Diffusion-DPO (Wallace et al., 2024) optimize the generator, whereas our verifier filters prompter rollouts while RFT holds the already SP-trained diffuser fixed. Finally, CLIPScore (Hessel et al., 2021) and VQAScore (Lin et al., 2024) measure image–text alignment; GPG measures caption informativeness relative to its paired image, while ED uses a one-time image-grounded annotation pass followed by text-only scoring.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **LLM 提示器、RFT 与推理时方法。** LLM 已成为有效的推理时提示增强器：RPG（Yang et al., 2024b）借助多模态 LLM 推理将提示分解为区域子提示；PromptEnhancer（Wang et al., 2025a）利用专用奖励模型，对思维链改写器应用 RFT；输入侧推理时缩放（Chen et al., 2025）则使用迭代 DPO 训练改写器。这些方法为固定生成器改进提示。我们的结构化格式还会提高描述表示在训练时的可扩散性；在固定该模式和骨干网络后，我们从 LLM 规模、思维链、来自图像条件教师的验证器门控自蒸馏，以及智能体式细化—渲染—评判循环等方面研究提示器的可提示性。ImageReward（Xu et al., 2023）等奖励模型和 Diffusion-DPO（Wallace et al., 2024）等模型侧偏好优化旨在优化生成器；而我们的验证器会筛选提示器 rollout，同时 RFT 将已经过 SP 训练的扩散器保持固定。最后，CLIPScore（Hessel et al., 2021）和 VQAScore（Lin et al., 2024）衡量图像—文本对齐；GPG 衡量描述相对于其配对图像的信息丰富度，而 ED 先进行一次图像扎根标注，再进行纯文本评分。

## 3 Method

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Our goal is to understand and exploit the image-grounded supervision that captions provide for visual generation. We first test the standard caption-side intervention of lengthening free-form natural-language (NL) captions and find that it does not reliably increase useful supervision (§3.1). This limitation motivates the structured prompt (SP), a typed JSON caption that organizes image-grounded variables into named fields. Figure 4 summarizes how the SP becomes the shared interface of our method. Using GPG and ED, we quantify the information exposed by each caption and relate it to converged diffusion loss in a controlled training sweep (§3.2). The resulting scaling properties isolate the diffusion-side role of the caption interface; realizing that interface from a user request introduces a second, LLM-side factor. We summarize the two as Diffusability×Promptability: diffusability captures how effectively the caption representation exposes and organizes the supervision the diffuser learns from, while promptability captures how effectively an LLM prompter instantiates that interface from a user request. We raise diffusability by annotating training images as SPs and incorporating them into diffusion training (§3.3), and raise promptability by scaling and training the prompter (§3.4).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们的目标是理解并利用描述为视觉生成提供的图像扎根监督。我们首先测试一种标准的描述侧干预——加长自由形式的自然语言（NL）描述——并发现它无法可靠地增加有用监督（§3.1）。这一限制促使我们提出结构化提示（SP）：一种将图像扎根变量组织到命名字段中的有类型 JSON 描述。图 4 总结了 SP 如何成为本方法的共享接口。我们使用 GPG 和 ED 量化每条描述所呈现的信息，并在受控训练遍历中将其与收敛扩散损失联系起来（§3.2）。由此得到的缩放性质隔离出描述接口在扩散侧的作用；而从用户请求实现该接口，又引入了第二个 LLM 侧因素。我们将两者概括为 Diffusability×Promptability：可扩散性刻画描述表示呈现和组织扩散器所学习监督的有效程度；可提示性则刻画 LLM 提示器根据用户请求实例化该接口的有效程度。我们通过把训练图像标注为 SP 并将其纳入扩散训练来提高可扩散性（§3.3），通过扩大提示器规模并训练提示器来提高可提示性（§3.4）。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Figure 4: Method overview: annotate and measure, train, generate.** (a) A VLM and frozen domain experts map each training image to an SP (§3.3); across controlled caption configurations, GPG and ED predict converged diffusion loss, yielding the scaling properties of text conditioning (§3.2). (b) The diffuser learns SP → image; the prompter learns user prompt → SP, and prompter-side comparisons hold the schema and trained diffuser fixed. (c) Single-shot inference composes the two with one prompter call followed by one diffuser call, user prompt → SP → image.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 4：方法概览：标注与测量、训练、生成。**（a）VLM 和冻结的领域专家把每张训练图像映射为一个 SP（§3.3）；在受控描述配置中，GPG 和 ED 预测收敛扩散损失，从而得到文本条件的缩放性质（§3.2）。（b）扩散器学习 SP → 图像；提示器学习用户提示 → SP；提示器侧比较固定模式和已训练扩散器。（c）单次推理用一次提示器调用和随后一次扩散器调用组合两者，即用户提示 → SP → 图像。

### 3.1 From natural-language captions to structured prompts

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Most modern T2I systems condition their diffusers on free-form natural-language (NL) captions, whether collected from web-scale corpora, recaptioned, or produced by LLMs (Rombach et al., 2022; Podell et al., 2023; Black Forest Labs, 2024; Betker et al., 2023). A common caption-side intervention is to make this NL condition longer and more detailed. The NL row of Figure 3 tests whether this helps using a fixed-backbone reconstruction probe. A single Qwen-Image (Wu et al., 2025a) backbone trained on captions spanning different lengths and richness levels attempts to regenerate one held-out image from each of four NL descriptions of the same annotated entities and relationships. To our surprise, reconstruction remains essentially flat as the captions become substantially longer, with the backbone and sampling seed fixed. In this probe, the added prose elaborates existing content without improving what the diffuser recovers. This saturation motivates testing whether an organized representation can expose image-grounded variables more effectively. We therefore introduce the structured prompt (SP), a typed JSON caption that assigns each represented visual variable to a named field.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 大多数现代 T2I 系统都以自由形式的自然语言（NL）描述作为扩散器条件，无论这些描述是从网络规模语料库收集、经重新描述得到，还是由 LLM 生成（Rombach et al., 2022; Podell et al., 2023; Black Forest Labs, 2024; Betker et al., 2023）。一种常见的描述侧干预是让 NL 条件更长、更详细。图 3 的 NL 行使用固定骨干网络重建探针测试这种做法是否有效。一个在不同长度和丰富度描述上训练的 Qwen-Image（Wu et al., 2025a）骨干网络，尝试依据针对同一组已标注实体与关系的四条 NL 描述，分别重建一张留出的图像。令我们意外的是，在固定骨干网络和采样种子的情况下，随着描述显著变长，重建结果基本保持不变。在该探针中，新增散文只是展开既有内容，并未改善扩散器所恢复的内容。这种饱和现象促使我们测试组织化表示能否更有效地呈现图像扎根变量。因此，我们引入结构化提示（SP），即一种有类型 JSON 描述，它将每个被表示的视觉变量分配给一个命名字段。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> An SP organizes image-grounded information at three scopes, as illustrated in Figure 5. Global fields describe the overall intent, scene, atmosphere, photography, style, and lighting. Each foreground object receives a per-element entry for its identity, attributes, actions, bounding-box position, optional depth, and photography, while cross-element relationships bind these entries to one another. The SP row of Figure 3 shows a different trend: reconstruction improves steadily as additional field groups are included, unlike the flat NL length sweep. The probe motivates this representation, but one image cannot establish whether caption informativeness predicts diffusion learning across training configurations. We therefore next introduce caption-side information measures and a controlled training sweep.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 如图 5 所示，SP 在三个范围组织图像扎根信息。全局字段描述整体意图、场景、氛围、摄影、风格和光照。每个前景物体都有一条逐元素记录，包含其身份、属性、动作、边界框位置、可选深度和摄影信息；跨元素关系则将这些记录彼此绑定。图 3 的 SP 行呈现出不同趋势：随着纳入更多字段组，重建结果持续改善，不同于平坦的 NL 长度遍历。该探针为这种表示提供了动机，但单张图像无法证明描述信息丰富度是否能跨训练配置预测扩散学习。因此，接下来我们引入描述侧信息度量和受控训练遍历。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Figure 5: Structured-prompt schema by example.** Left: an image annotated with bounding boxes and element IDs. Center: an abridged pseudo-JSON view grouping global, per-element, and cross-element fields; ellipses and comments are explanatory and are not part of the serialized training record, and the displayed count refers to foreground elements. Right: selected per-element fields. The schema organizes global scene context, per-element properties and geometry, and cross-element relations into named conditioning fields; §3.2 measures how the information they carry relates to diffusion training loss.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **图 5：结构化提示模式示例。** 左：带边界框和元素 ID 标注的图像。中：将全局、逐元素和跨元素字段分组的精简伪 JSON 视图；省略号和注释用于解释，并不属于序列化训练记录，图示计数指前景元素。右：选取的逐元素字段。该模式将全局场景语境、逐元素属性与几何信息以及跨元素关系组织到命名条件字段中；§3.2 测量这些字段携带的信息与扩散训练损失之间的关系。

### 3.2 Caption informativeness predicts training loss

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> We use two complementary caption-side metrics adapted from prior work—Grounded Perplexity Gain (GPG; white-box) (Favero et al., 2024) and Effective Detailness (ED; black-box) (Wang et al., 2025b; Cheng et al., 2024)—and study their relationship with converged diffusion training loss in a controlled scaling sweep. Here, white-box and black-box refer to whether scoring requires access to a VLM’s token log-probabilities.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 我们采用两项源自先前工作的互补描述侧指标——Grounded Perplexity Gain（GPG；白盒）（Favero et al., 2024）和 Effective Detailness（ED；黑盒）（Wang et al., 2025b; Cheng et al., 2024）——并在受控缩放遍历中研究它们与收敛扩散训练损失之间的关系。这里，白盒和黑盒指评分是否需要访问 VLM 的 token 对数概率。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> **Figure 6: The two informativeness measures: definition (left) and measured trends (right).** Top: GPG sums the scored content-token log-likelihood gain from revealing the image (Eq. (1)). Bottom: ED matches caption attributes against an image-grounded reference set and reports $F_{0.5}(P_A,R_A)$ (Eq. (2)). Both remain nearly flat as NL captions grow longer, but increase across the nested SP configurations described below.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> **图 6：两种信息丰富度度量：定义（左）与实测趋势（右）。** 上：GPG 对揭示图像后被评分内容 token 的对数似然增益求和（式（1））。下：ED 将描述属性与图像扎根参考集合匹配，并报告 $F_{0.5}(P_A,R_A)$（式（2））。随着 NL 描述变长，两者都基本保持平坦；但在下文所述的嵌套 SP 配置中，两者都会上升。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> **Grounded Perplexity Gain (GPG).** For GPG, we measure how much revealing the paired image increases a caption’s likelihood under a frozen VLM. We fix a VLM judge $M$ (here Qwen3.5-397B-A17B (Qwen Team, 2025)) and apply the caption canonicalization and content-mask protocol of Appendix A.1; for image $I$, let $y_{1:T}$ denote the resulting sequence tokens and $m_{1:T}\in\{0,1\}^{T}$ the corresponding content mask. The Grounded Perplexity Gain of $y$ on $I$ is the log-likelihood gain when the image is revealed, summed over the scored content positions:

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **Grounded Perplexity Gain（GPG）。** 对于 GPG，我们衡量在冻结 VLM 下，揭示配对图像会使描述似然提高多少。我们固定一个 VLM 评判器 $M$（此处为 Qwen3.5-397B-A17B（Qwen Team, 2025）），并应用附录 A.1 的描述规范化和内容掩码协议；对于图像 $I$，令 $y_{1:T}$ 表示所得序列 token，$m_{1:T}\in\{0,1\}^{T}$ 表示相应内容掩码。$y$ 在 $I$ 上的 Grounded Perplexity Gain，是揭示图像后在被评分内容位置上求和的对数似然增益：

$$
\operatorname{GPG}(y,I) \triangleq \sum_{t=1}^{T} m_t\left[\log p_M(y_t\mid I,y_{<t})-\log p_M(y_t\mid\varnothing,y_{<t})\right]. \tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Here $\varnothing$ denotes the matched no-image pass. This masked conditional log-likelihood gain is an operational estimate of caption–image mutual information under $M$; the image-free pass supplies a model-based prior rather than the exact dataset marginal. GPG is thus a total rather than a per-token rate, so it can grow with caption length; we report its mean over the shared 30,000-image evaluation pool (the same images used for ED) for each caption configuration. We hold the judge, scoring template, image preprocessing, and paired no-image pass fixed across all caption configurations.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 这里，$\varnothing$ 表示匹配的无图像前向过程。这一带掩码的条件对数似然增益是 $M$ 下描述—图像互信息的一种操作性估计；无图像过程提供的是基于模型的先验，而非精确的数据集边缘分布。因此，GPG 是总量而非逐 token 速率，所以它可以随描述长度增长；对于每种描述配置，我们报告其在共享的 30,000 张图像评估池（与 ED 使用相同图像）上的均值。在所有描述配置中，我们固定评判器、评分模板、图像预处理以及配对的无图像过程。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> **Effective Detailness (ED).** ED offers a complementary semantic measure of caption information without requiring token log-probabilities. Adapting caption-detailness evaluation (Wang et al., 2025b), ED uses independent image-side and caption-side proposers to extract object–attribute–relationship–grounding tuples from pixels and text, respectively, followed by a paraphrase-tolerant matcher (Gemini 3 Pro for image proposal; separate GPT-5.4 calls for caption proposal and matching). The matcher returns two symmetric binary masks, indicating which image-side attributes are covered by the caption and which caption-side attributes are supported by the image. We denote the resulting caption-side attribute precision and image-side attribute recall by $P_A$ and $R_A$, respectively:

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> **Effective Detailness（ED）。** ED 提供了一种不需要 token 对数概率的互补描述信息语义度量。ED 改编自描述细节度评估（Wang et al., 2025b），使用相互独立的图像侧与描述侧提议器，分别从像素和文本中提取物体—属性—关系—扎根元组，随后使用容忍释义的匹配器（图像提议使用 Gemini 3 Pro；描述提议与匹配分别调用 GPT-5.4）。匹配器返回两个对称二值掩码，分别表示哪些图像侧属性被描述覆盖，以及哪些描述侧属性得到图像支持。我们分别将由此得到的描述侧属性精确率和图像侧属性召回率记为 $P_A$ 和 $R_A$：

$$
\operatorname{ED}(y,I) \triangleq F_{0.5}(P_A,R_A). \tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> Here $F_{0.5}$ emphasizes precision over recall, penalizing unsupported caption attributes more heavily than omissions (van Rijsbergen, 1979; Cheng et al., 2024). Appendix B.2 motivates this choice and tests its sensitivity. Only the attribute subset enters the reported score; the broader tuple decomposition supplies entity context for matching, while object, relation, and grounding terms are not included in the reported ED value. To avoid caption-derived leakage, the image-side proposer never sees the candidate caption; after this one-time image-side pass, caption proposal and matching are text-only and require no log-probabilities. We aggregate ED over 30,000 paired images per caption configuration using a two-sided 10%-trimmed mean, discarding the lowest and highest 10% of pair-level scores to reduce sensitivity to occasional extraction or matching failures (Hampel, 1974). Appendix B documents the extraction and matching protocol and its backend checks.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> 这里，$F_{0.5}$ 相较召回率更强调精确率，因此对不受支持的描述属性的惩罚重于遗漏（van Rijsbergen, 1979; Cheng et al., 2024）。附录 B.2 说明了这一选择的动机并测试其敏感性。只有属性子集进入报告的分数；更广泛的元组分解为匹配提供实体语境，而物体、关系和扎根项不计入报告的 ED 值。为避免源自描述的信息泄漏，图像侧提议器永远不会看到候选描述；完成这一次图像侧处理后，描述提议与匹配均为纯文本操作，不需要对数概率。对于每种描述配置，我们在 30,000 张配对图像上使用双侧 10% 截尾均值聚合 ED，丢弃配对级分数中最低和最高的各 10%，以降低偶发提取或匹配失败带来的敏感性（Hampel, 1974）。附录 B 记录了提取与匹配协议及其后端检查。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> **Figure 7: The scaling properties of text conditioning: loss follows information.** (a–b) Training curves separate across SP levels but overlap across NL richness levels. (c) Caption length does not place NL and SP on a common loss trend. (d–e) Across all 15 sweep points, converged MSE is approximately linear in GPG and follows a power law in ED; bands show the central 95% range across resamples of the designed sweep settings, not training-run confidence intervals. (f) GPG and ED closely agree on the caption-configuration ranking despite using different scoring interfaces.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> **图 7：文本条件的缩放性质：损失随信息变化。**（a–b）不同 SP 层级的训练曲线彼此分离，但不同 NL 丰富度层级的曲线相互重叠。（c）描述长度无法使 NL 与 SP 落在共同的损失趋势上。（d–e）在全部 15 个遍历点上，收敛 MSE 与 GPG 近似呈线性关系，并与 ED 呈幂律关系；带状区域表示对所设计遍历设置进行重采样所得的中央 95% 范围，而非训练运行的置信区间。（f）尽管使用不同评分接口，GPG 与 ED 对描述配置的排序高度一致。

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> **The scaling properties.** Using GPG and ED, we ask whether caption informativeness predicts the converged diffusion loss reached at a common training budget. The controlled sweep comprises 15 caption configurations constructed from the same full image annotations. Three NL controls verbalize the same core facts under increasing length budgets. Six SP configurations expose progressively richer subsets of the schema; Section 3.3 defines the corresponding field ladder. All six are deterministic projections of the same full-schema record, obtained by masking predefined field groups and cumulatively restoring them as detail increases. The remaining six probe representation choices more directly: three replace bounding boxes with locations on $3\times3$, $5\times5$, or $9\times9$ grids, and three mask the scene, bounding-box, or relationship fields from the full-schema SP. Appendix A.3 reports the complete sweep and its measured values.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> **缩放性质。** 借助 GPG 和 ED，我们考察描述信息丰富度能否预测共同训练预算下达到的收敛扩散损失。受控遍历包含从同一批完整图像标注构建的 15 种描述配置。三个 NL 对照在逐渐增加的长度预算下表述相同的核心事实。六个 SP 配置呈现模式中逐渐丰富的子集；§3.3 定义了相应字段阶梯。这六个配置都是同一完整模式记录的确定性投影：先遮蔽预定义字段组，再随细节增加逐步恢复。其余六个配置更直接地探查表示选择：三个配置用 $3\times3$、$5\times5$ 或 $9\times9$ 网格上的位置替代边界框；另三个配置从完整模式 SP 中分别遮蔽场景、边界框或关系字段。附录 A.3 报告了完整遍历及其测量值。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> For each configuration, we compute GPG and ED on fixed evaluation pools and train a separate diffuser from the same in-house BAGEL continued-training checkpoint (Deng et al., 2025) to a common budget of $2.84\times10^{10}$ cumulative image tokens. The images, initialization, architecture, and optimization recipe are identical across runs, leaving the caption configuration as the only changing variable. We use BAGEL because repeating all 15 runs with the substantially larger Qwen-Image backbone would be prohibitively expensive; Appendix C and Table 11 provide the complete setup.

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> 对于每种配置，我们在固定评估池上计算 GPG 和 ED，并从同一个内部 BAGEL 续训检查点（Deng et al., 2025）出发，单独训练一个扩散器，直至达到共同的 $2.84\times10^{10}$ 累计图像 token 预算。各次运行的图像、初始化、架构和优化方案完全相同，只有描述配置发生变化。我们使用 BAGEL，是因为用规模大得多的 Qwen-Image 骨干网络重复全部 15 次运行将产生难以承受的开销；附录 C 和表 11 给出了完整设置。

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> The sweep first shows that caption length does not explain the outcomes. As Figure 7c shows, NL and SP captions do not share a common length–loss trend: making NL captions longer nudges GPG upward (partly a length effect, since GPG is a token sum) yet leaves ED and converged loss essentially unchanged, whereas restoring SP fields raises both measures substantially and lowers loss, as shown in Figures 6 and 7a–b. In contrast, measured informativeness provides the common axis. Figure 7d–e shows that, across all 15 configurations, converged training MSE is well fit by a linear function of GPG and follows a power-law trend in ED:

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> 该遍历首先表明，描述长度无法解释结果。如图 7c 所示，NL 和 SP 描述并不共享同一个长度—损失趋势：加长 NL 描述会使 GPG 略微上升（这部分来自长度效应，因为 GPG 是 token 求和），但 ED 和收敛损失基本不变；相反，恢复 SP 字段会显著提高两种度量并降低损失，如图 6 和图 7a–b 所示。与之形成对比的是，实测信息丰富度提供了共同坐标轴。图 7d–e 表明，在全部 15 种配置中，收敛训练 MSE 能够由 GPG 的线性函数很好地拟合，并随 ED 呈幂律趋势：

$$
\operatorname{MSE}=0.4549-8.45\times10^{-5}\cdot\operatorname{GPG},\qquad r=-0.984. \tag{3}
$$

$$
\operatorname{MSE}=0.4200\cdot\operatorname{ED}^{-0.2073},\qquad r=-0.971. \tag{4}
$$

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> Here $r$ is Pearson correlation in raw space for GPG and log–log space for ED. We call these two relations the scaling properties of text conditioning: within the calibrated architecture, training recipe, and measured ranges, caption information predicts matched-budget converged diffusion loss. Both fits are tight: their residual standard deviations are approximately $6\times10^{-4}$ for GPG and $7.8\times10^{-4}$ for the likelihood-free ED measure. Figure 7f further shows that the two measures agree closely on the configuration ranking despite their different scoring interfaces, with Spearman $\rho_{\mathrm{GPG,ED}}=0.96$.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> 这里，$r$ 对 GPG 表示原始空间中的 Pearson 相关系数，对 ED 表示双对数空间中的 Pearson 相关系数。我们将这两种关系称为文本条件的缩放性质：在经过校准的架构、训练方案和测量范围内，描述信息可以预测匹配预算下的收敛扩散损失。两种拟合都很紧密：GPG 的残差标准差约为 $6\times10^{-4}$，无似然 ED 度量的残差标准差约为 $7.8\times10^{-4}$。图 7f 进一步表明，尽管评分接口不同，两种度量对配置排序的判断高度一致，Spearman $\rho_{\mathrm{GPG,ED}}=0.96$。

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> This calibration has both scientific and practical consequences. Scientifically, it elevates caption information from a descriptive property to a controlled training variable: with architecture, images, and compute fixed, it orders the loss reached across caption formats. Practically, after one calibration it can screen candidate caption configurations before training another diffuser under the same recipe. A configuration-level holdout directly tests this use: fits learned only from the NL and nested-SP families predict the converged MSE of all six spatial and field variants excluded from fitting. The GPG- and ED-based fits achieve mean absolute MSE errors of $5.0\times10^{-4}$ and $8.1\times10^{-4}$, respectively, showing that the relation predicts configurations beyond those used to estimate it; at this error level, screening separates configurations whose loss gaps exceed the fit error rather than near-identical ones.

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> 这一校准兼具科学意义与实际意义。在科学上，它把描述信息从描述性属性提升为受控训练变量：当架构、图像和计算量固定时，它能对不同描述格式所达到的损失进行排序。在实践中，完成一次校准后，就能在同一方案下训练另一个扩散器之前筛选候选描述配置。配置级留出实验直接检验了这一用途：仅从 NL 与嵌套 SP 家族学习的拟合关系，可以预测所有六个未参与拟合的空间变体和字段变体的收敛 MSE。基于 GPG 和 ED 的拟合分别取得 $5.0\times10^{-4}$ 和 $8.1\times10^{-4}$ 的 MSE 平均绝对误差，表明该关系可以预测用于估计它的配置之外的配置；在这一误差水平下，筛选能够区分损失差距超过拟合误差的配置，而不能区分几乎相同的配置。

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> The remaining checks delimit the claim’s scope. Each configuration is trained once, so the resampling ranges in Figure 7d–e measure sensitivity to the selected sweep settings, not run-to-run uncertainty or classical confidence intervals. Changing the GPG judge or ED image proposer largely preserves the rankings, and budget-wise refits preserve both relations. Appendices A.2 and B.4 report checks of the GPG judge and ED image proposer, respectively; Appendix A.5 reports setting-resampling, budget-refit, and trailing-window analyses. The calibration is also backbone-specific. It is fit on BAGEL, whereas the end-to-end system of §4 uses Qwen-Image; the matched control there shows that the structured interface still outperforms a free-form one on that backbone, but the quantitative GPG–loss relation is not re-fit for it. Like parameter, data, and compute laws (Kaplan et al., 2020; Hoffmann et al., 2022), this is a recipe-specific empirical calibration rather than a universal theorem; Appendix A.6 gives its mutual-information motivation.

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> 其余检查界定了该论断的范围。每种配置只训练一次，因此图 7d–e 中的重采样范围衡量的是对所选遍历设置的敏感性，而非运行间不确定性或经典置信区间。更换 GPG 评判器或 ED 图像提议器基本会保留排序，按预算重新拟合也会保留两种关系。附录 A.2 和 B.4 分别报告了对 GPG 评判器与 ED 图像提议器的检查；附录 A.5 报告了设置重采样、预算重拟合和尾部窗口分析。校准还具有骨干网络特异性。它在 BAGEL 上拟合，而 §4 的端到端系统使用 Qwen-Image；其中的匹配对照表明，结构化接口在该骨干网络上仍优于自由形式接口，但没有为其重新拟合定量的 GPG—损失关系。与参数、数据和计算量定律一样（Kaplan et al., 2020; Hoffmann et al., 2022），这是一种方案特定的经验校准，而非普适定理；附录 A.6 给出了其互信息动机。

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> **From the properties to two factors.** When captions are annotated from paired images, the scaling properties isolate a diffusion-side capability: how effectively the caption interface exposes and organizes image-grounded supervision under a fixed training recipe. We call this capability diffusability, adapting the terminology of Skorokhodov et al. (2025). The NL/SP contrast identifies organization as a practical intervention, but it tests richer content and organization jointly rather than JSON syntax in isolation. At inference, however, no paired image is available to supply that content; an LLM prompter must infer the visual variables from the user request. We call this LLM-side capability promptability and compare it through the quality of images generated under a fixed schema and diffuser. End-to-end generation therefore depends on both the representation available to the diffuser and the prompter’s ability to instantiate it. Let $f$ denote the caption interface, including its represented field groups, and $\pi$ the LLM prompter; we summarize their joint role schematically, rather than as a fitted multiplicative quality law:

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> **从这些性质到两项因素。** 当描述依据配对图像进行标注时，缩放性质隔离出一种扩散侧能力：在固定训练方案下，描述接口呈现和组织图像扎根监督的有效程度。我们沿用 Skorokhodov et al.（2025）的术语，将这种能力称为可扩散性。NL/SP 对比把组织方式识别为一种实际干预，但它联合检验了更丰富的内容与组织，而不是单独检验 JSON 语法。然而，在推理时没有配对图像可提供这些内容；LLM 提示器必须从用户请求中推断视觉变量。我们将这种 LLM 侧能力称为可提示性，并在固定模式和扩散器下通过生成图像的质量来比较它。因此，端到端生成既取决于扩散器可用的表示，也取决于提示器实例化该表示的能力。令 $f$ 表示描述接口（包括它所表示的字段组），$\pi$ 表示 LLM 提示器；我们用示意式来概括二者的共同作用，而不是将其视为一条拟合得到的乘法质量定律：

$$
\underbrace{\operatorname{Quality}(f,\pi)}_{\text{system output}}
=
\underbrace{\operatorname{Diffusability}(f)}_{\text{diffusion side}}
\times
\underbrace{\operatorname{Promptability}(f,\pi)}_{\text{LLM side}}. \tag{5}
$$

### 3.3 Raising Diffusability: constructing structured supervision

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> **Image-to-SP annotation with domain experts.** To raise diffusability at corpus scale, we annotate each training image with a faithful, full-schema SP and use the resulting SP levels as structured supervision in diffusion training. Constructing that supervision is a heterogeneous perception problem: it combines global semantics and local appearance and actions with specialized evidence for human pose, depth, extent, occlusion, and cross-element relations. A general-purpose VLM handles the semantic content well but remains less reliable on body-side orientation and precise geometry; if serialized directly, these errors become explicit conditioning variables. To combine these complementary signals, we propose the five-stage image-to-SP annotation pipeline shown in Figure 8. Frozen specialists extract pose and geometry evidence, and a final VLM reconciles it with the scene semantics into one coherent SP. Appendix C.2 provides the implementation details.

> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> **借助领域专家进行图像到 SP 的标注。** 为在语料库规模上提高可扩散性，我们为每张训练图像标注一个忠实的完整模式 SP，并把所得 SP 层级用作扩散训练中的结构化监督。构建这种监督是一个异质感知问题：它把全局语义、局部外观与动作，同人体姿态、深度、范围、遮挡和跨元素关系的专业证据结合起来。通用 VLM 很擅长处理语义内容，但在身体朝向和精确几何方面仍不够可靠；若直接序列化，这些错误就会成为显式条件变量。为结合这些互补信号，我们提出图 8 所示的五阶段图像到 SP 标注流水线。冻结的专家提取姿态与几何证据，最终由一个 VLM 将其与场景语义协调为一个连贯的 SP。附录 C.2 给出了实现细节。

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> **Figure 8: Image-to-SP annotation with domain experts.** A VLM recovers global and element-level semantics; Sapiens, DepthAnything V2, and SAM 2.1 provide complementary pose and geometric evidence; a final VLM pass assembles the full L10 SP, from which L5–L9 are derived by deterministically masking field groups.

> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> **图 8：借助领域专家进行图像到 SP 的标注。** VLM 恢复全局与元素级语义；Sapiens、DepthAnything V2 和 SAM 2.1 提供互补的姿态与几何证据；最终一次 VLM 处理组装出完整的 L10 SP，再通过确定性地遮蔽字段组得到 L5–L9。

> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> The pipeline first establishes a shared semantic frame. Stage 1 reads the full image to recover its intent, scene and atmosphere, style, lighting, and camera setup, while creating an ordered element inventory with identifiers and bounding boxes. Stage 2 revisits each element crop so that the VLM can resolve local descriptions, attributes, actions, and photography with less interference from the surrounding scene. Human elements additionally pass through Sapiens (Khirodkar et al., 2024), whose 133 pose keypoints are rendered as an overlay for the VLM; this evidence helps it disambiguate body-side orientation and joint geometry rather than infer them from appearance alone. Stage 3 supplies complementary geometric evidence: DepthAnything V2 (Yang et al., 2024a) estimates relative element depth, while SAM 2.1 (Ravi et al., 2024) provides masks and occlusion cues. Bounding boxes, masks, and depth support geometric relations such as overlap, containment, relative position, and depth order. Stage 4 reconciles this evidence with the global and crop-level semantics, infers semantic relations such as support and interaction, and serializes a well-formed L10 SP. The expert outputs constrain this annotation rather than being copied as raw predictions: inferred human pose may be expressed textually under the element’s pose and action keys, while raw keypoints and masks remain intermediate evidence. Stage 5 then projects the full annotation into the controlled field ladder described below.

> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> 流水线首先建立共享语义框架。阶段 1 读取完整图像，以恢复其意图、场景与氛围、风格、光照和相机设置，同时创建带标识符与边界框的有序元素清单。阶段 2 重新查看每个元素裁剪，使 VLM 能在较少受到周围场景干扰的情况下解析局部描述、属性、动作与摄影信息。人体元素还会经过 Sapiens（Khirodkar et al., 2024）处理，其 133 个人体姿态关键点被渲染为覆盖层供 VLM 查看；这些证据帮助模型消除身体朝向和关节几何的歧义，而不是仅凭外观推断。阶段 3 提供互补几何证据：DepthAnything V2（Yang et al., 2024a）估计元素相对深度，SAM 2.1（Ravi et al., 2024）提供掩码与遮挡线索。边界框、掩码和深度支持重叠、包含、相对位置和深度顺序等几何关系。阶段 4 将这些证据与全局及裁剪级语义协调起来，推断支撑、交互等语义关系，并序列化为格式正确的 L10 SP。专家输出用于约束标注，而不是作为原始预测直接复制：推断出的人体姿态可以在元素的姿态与动作键下用文本表达，而原始关键点和掩码仍是中间证据。阶段 5 随后把完整标注投影到下述受控字段阶梯。

> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> **Controlled field ladder.** To separate schema richness from annotation quality, stage 5 derives L5–L9 from each full L10 SP by deterministically masking predefined field groups. Table 1 presents the equivalent ascending view: moving from L5 to L10 successively restores bounding boxes, scene context, dynamic attributes, depth and relations, and element-level photography without re-annotating the image. The SP levels are projections of one L10 annotation, and the NL controls are verbalized independently from the same underlying annotation evidence rather than converted from the SP JSON; the images and source annotations are fixed, and only the caption content and organization exposed to the learner vary.

> <span style="color:#F59E0B"><strong>Para. 23[CN]:</strong></span> **受控字段阶梯。** 为将模式丰富度与标注质量区分开来，阶段 5 通过确定性地遮蔽预定义字段组，从每个完整 L10 SP 派生出 L5–L9。表 1 给出了等价的上升视图：从 L5 移动到 L10，会依次恢复边界框、场景语境、动态属性、深度与关系，以及元素级摄影信息，而无须重新标注图像。各 SP 层级都是同一份 L10 标注的投影；NL 对照则依据相同的底层标注证据独立表述，而不是从 SP JSON 转换而来；图像与源标注保持固定，只有向学习器呈现的描述内容和组织方式发生变化。

### Table 1. SP field ladder and downstream transfer / SP 字段阶梯与下游迁移

> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> **Table 1: SP field ladder and downstream transfer.** L5–L9 are deterministic projections of L10. All levels are rendered by the BAGEL diffuser trained at that level, so these values are not comparable with the Qwen-Image systems of Table 2. Tokens are averages per SP; GSB is measured against L5 over $N=150$ prompt pairs.

> <span style="color:#F59E0B"><strong>Para. 24[CN]:</strong></span> **表 1：SP 字段阶梯与下游迁移。** L5–L9 是 L10 的确定性投影。所有层级都由在相应层级训练的 BAGEL 扩散器渲染，因此这些数值不能与表 2 的 Qwen-Image 系统比较。Token 数为每个 SP 的平均值；GSB 在 $N=150$ 对提示上相对于 L5 测量。

| Level / 层级 | Avg. tokens / 平均 token 数 | Added fields / 新增字段 | GenEval2 GM ↑ | GSB vs. L5 ↑ / 相对 L5 的 GSB ↑ |
|---|---:|---|---:|---:|
| L5 | 447 | Base fields / 基础字段 | 46.79 | — |
| L6 | 542 | Bounding boxes / 边界框 | 48.65 | 8.0 |
| L7 | 647 | Scene context / 场景语境 | 49.72 | 17.3 |
| L8 | 803 | Dynamic attributes / 动态属性 | 52.94 | 22.7 |
| L9 | 1062 | Depth & relationships / 深度与关系 | 55.16 | 24.7 |
| L10 | 1374 | Photography / 摄影 | 57.70 | 26.0 |

> <span style="color:#3B82F6"><strong>Para. 25:</strong></span> Across the SP ladder, exposing more field groups raises GPG and ED and lowers loss along the calibrated relations of §3.2. Because every level is a deterministic projection of the same L10 annotation, the comparison varies the information and organization exposed by the schema without level-specific re-annotation. To test whether this training-side gain transfers to generated images, a frozen Gemini 3 Pro generates one L10 SP zero-shot for each user prompt; L5–L9 are derived from that same output and rendered by the BAGEL diffuser trained at the corresponding level. Table 1 shows that GenEval2 GM and order-swapped GSB against L5 both improve monotonically with schema richness, demonstrating that higher diffusability benefits generated images rather than training loss alone. A complementary field-wise ablation in Appendix C.4, measured on converged training loss rather than the generation benchmarks above, identifies global scene context as the largest individual contributor, followed by bounding-box conditioning. The verbal spatial variants follow the same relations, showing that the result is not tied to the default coordinate serialization. The annotation pipeline thus supplies structured supervision at scale, while the controlled ladder operationalizes the diffusion-side intervention.

> <span style="color:#F59E0B"><strong>Para. 25[CN]:</strong></span> 在 SP 阶梯上，呈现更多字段组会沿 §3.2 的校准关系提高 GPG 和 ED 并降低损失。由于每个层级都是同一 L10 标注的确定性投影，该比较在无须层级特定重新标注的情况下，改变了模式所呈现的信息与组织。为检验这一训练侧增益能否迁移到生成图像，冻结的 Gemini 3 Pro 针对每条用户提示零样本生成一个 L10 SP；再从同一输出派生 L5–L9，并由在相应层级训练的 BAGEL 扩散器进行渲染。表 1 表明，GenEval2 GM 和相对于 L5 的顺序交换 GSB 都会随模式丰富度单调改善，证明更高的可扩散性不仅有益于训练损失，也有益于生成图像。附录 C.4 的互补逐字段消融以收敛训练损失而非上述生成基准进行测量，发现全局场景语境是最大的单项贡献因素，其次是边界框条件。文字化空间变体也遵循相同关系，表明结果并不依赖默认坐标序列化。因此，标注流水线大规模提供结构化监督，而受控阶梯则将扩散侧干预操作化。

### 3.4 Raising Promptability: scaling and training the LLM prompter

> <span style="color:#3B82F6"><strong>Para. 26:</strong></span> The annotation pipeline produces SPs from paired images during training, but inference begins only from a user request. An LLM prompter must therefore translate that request into an SP. This is more than a formatting task: the prompter must infer plausible visual details left unspecified by the user and fill in the schema with them without violating explicit constraints. We therefore assess promptability through the quality of images rendered from its SPs, rather than through JSON validity or schema completeness alone. We train one Qwen-Image diffuser on a mixture of SP levels and NL captions so that the same backbone can accommodate conditioning inputs with different structures and degrees of richness. For the controlled promptability sweeps below, we fix this diffuser and the L10 schema and vary only the prompter $\pi$. Differences in the resulting images therefore isolate its model, reasoning mode, or training configuration (training-pipeline ablations in §4.2).

> <span style="color:#F59E0B"><strong>Para. 26[CN]:</strong></span> 标注流水线在训练期间从配对图像生成 SP，但推理只从用户请求开始。因此，LLM 提示器必须把该请求转换为 SP。这不只是格式化任务：提示器必须推断用户未指定的合理视觉细节，并用其填充模式，同时不得违反显式约束。因此，我们通过其 SP 所渲染图像的质量来评估可提示性，而不是仅看 JSON 有效性或模式完整性。我们在 SP 层级与 NL 描述的混合数据上训练一个 Qwen-Image 扩散器，使同一骨干网络能够适应结构与丰富度不同的条件输入。在下文受控可提示性遍历中，我们固定该扩散器和 L10 模式，仅改变提示器 $\pi$。因此，所得图像的差异隔离出其模型、推理模式或训练配置的影响（训练流水线消融见 §4.2）。

> <span style="color:#3B82F6"><strong>Para. 27:</strong></span> **Figure 9: Prompter scaling: generated-image quality improves with prompter size and reasoning mode.** Qwen3.5 prompters from 0.8B to 397B are evaluated in non-thinking and chain-of-thought modes with the L10 schema and Qwen-Image diffuser fixed. (a–b) GenEval++ (Ye et al., 2025) and WISE (Niu et al., 2025) measure basic alignment and world-knowledge generation, respectively. (c–d) The offline GPT-5.4 structure scores and good/same/bad (GSB) net preferences (against the 0.8B prompter) continue to improve with model scale and reasoning mode. Appendices E.4 and E.5 provide the structure/alignment rubrics and the pairwise rubric with order-swapped GSB aggregation, respectively.

> <span style="color:#F59E0B"><strong>Para. 27[CN]:</strong></span> **图 9：提示器缩放：生成图像质量随提示器规模和推理模式而提高。** 在固定 L10 模式和 Qwen-Image 扩散器的情况下，以非思考和思维链模式评估从 0.8B 到 397B 的 Qwen3.5 提示器。（a–b）GenEval++（Ye et al., 2025）和 WISE（Niu et al., 2025）分别衡量基础对齐与世界知识生成。（c–d）离线 GPT-5.4 结构分数和 good/same/bad（GSB）净偏好（相对于 0.8B 提示器）会随模型规模和推理模式持续改善。附录 E.4 和 E.5 分别给出了结构／对齐评分准则，以及采用顺序交换 GSB 聚合的成对评分准则。

> <span style="color:#3B82F6"><strong>Para. 28:</strong></span> **Off-the-shelf prompter scaling.** Before applying task-specific training, we first test whether progress in general-purpose LLMs transfers to promptability through model scale and inference-time reasoning. We use six frozen Qwen3.5 checkpoints, spanning 0.8B to 397B total parameters, as zero-shot prompters. Each checkpoint maps user requests to L10 SPs in both non-thinking and chain-of-thought modes, and the same fixed Qwen-Image diffuser renders the resulting SPs. Within each benchmark, the user prompts and image-generation settings are held fixed across checkpoints and reasoning modes, so only the prompter changes. We evaluate basic compositional alignment with GenEval++, world-knowledge-conditioned generation with WISE, and open-ended generation with GPT-5.4 structure scores and good/same/bad (GSB) net preference against the smallest, 0.8B prompter. The broader promptability experiments additionally report GPT-5.4 alignment scores.

> <span style="color:#F59E0B"><strong>Para. 28[CN]:</strong></span> **现成提示器的缩放。** 在应用任务特定训练之前，我们首先测试通用 LLM 的进步能否通过模型规模和推理时推理迁移到可提示性。我们使用六个冻结的 Qwen3.5 检查点作为零样本提示器，总参数量从 0.8B 到 397B。每个检查点分别在非思考与思维链模式下将用户请求映射为 L10 SP，再由同一个固定 Qwen-Image 扩散器渲染所得 SP。在每个基准内，用户提示和图像生成设置在不同检查点与推理模式间保持固定，因此只有提示器发生变化。我们使用 GenEval++ 评估基础组合对齐，使用 WISE 评估世界知识条件生成，并用 GPT-5.4 结构分数及相对于最小 0.8B 提示器的 good/same/bad（GSB）净偏好评估开放式生成。更广泛的可提示性实验还报告 GPT-5.4 对齐分数。

> <span style="color:#3B82F6"><strong>Para. 29:</strong></span> The results in Figure 9 show that generated-image quality improves with prompter scale: in thinking mode, GenEval++ rises from 46.4% at 0.8B to 86.8% at 397B. Chain-of-thought inference provides a further gain at every scale except 0.8B, where reasoning often enters repetitive loops before producing valid JSON and therefore underperforms non-thinking inference. Because none of these prompters receives task-specific training, the trend associates advances in general-purpose LLMs and reasoning mode with higher image quality through the SP interface. GenEval++ and WISE capture broad gains with scale, while structure and GSB distinguish high-capacity prompters and reasoning modes more finely.

> <span style="color:#F59E0B"><strong>Para. 29[CN]:</strong></span> 图 9 的结果表明，生成图像质量会随提示器规模提升：在思考模式下，GenEval++ 从 0.8B 时的 46.4% 提高到 397B 时的 86.8%。除 0.8B 外，思维链推理在每种规模上都带来进一步增益；在 0.8B 时，推理经常在生成有效 JSON 前陷入重复循环，因此表现不如非思考推理。由于这些提示器都没有接受任务特定训练，该趋势将通用 LLM 与推理模式的进步，同通过 SP 接口获得的更高图像质量联系起来。GenEval++ 和 WISE 捕捉随规模增长的广泛增益，而结构和 GSB 能更细致地区分高容量提示器与推理模式。

> <span style="color:#3B82F6"><strong>Para. 30:</strong></span> **Training pipeline.** The zero-shot sweep establishes transfer from general-purpose LLM progress, but even Qwen3.5-397B-A17B produces schema-valid SPs that carry insufficient visual detail. The resulting images often appear overly simple and less realistic, especially for complex scenes and infographics, as illustrated in Figure 13. Following the staged post-training paradigm used for reasoning LLMs, we improve the prompter through SFT, cold-start distillation, and RFT; Figure 10 diagrams the pipeline.

> <span style="color:#F59E0B"><strong>Para. 30[CN]:</strong></span> **训练流水线。** 零样本遍历证实了通用 LLM 进步的迁移，但即使 Qwen3.5-397B-A17B 也会生成模式有效、却缺少足够视觉细节的 SP。所得图像往往过于简单且不够真实，复杂场景与信息图尤其如此，如图 13 所示。我们遵循推理 LLM 所使用的分阶段后训练范式，通过 SFT、冷启动蒸馏和 RFT 改进提示器；图 10 展示了该流水线。

> <span style="color:#3B82F6"><strong>Para. 31:</strong></span> The training stages are:
>
> - **Supervised fine-tuning (SFT)** first teaches the SP content distribution expected by the diffuser. Its core task pairs an image’s original caption, treated as the user prompt, with the SP produced by our image-to-SP annotation pipeline. Across the corpus, these pairs teach a conditional prior over plausible SP completions, including objects, attributes, geometry, depth, and relations, rather than a deterministic prompt-to-layout mapping; Figure 12 illustrates the resulting layout prior. A replay mixture of general reasoning and instruction examples preserves the base model’s broader abilities. Appendix C.5 details the replay composition.
> - **Cold-start** teaches the prompter how to reason from a user prompt to a detailed SP. For each original image–caption pair, an image-conditioned VLM writes a trace showing how an image-free prompter can infer the visual decisions needed to construct the target SP. Because privileged image access can leak instance-specific observations into the trace, a Gemini judge rejects candidates that state such details without a prompt-grounded, common-sense, or explicit design rationale, as well as traces inconsistent with the caption, image, or SP. The prompter then learns from the accepted (user prompt → thinking trace → SP) examples without receiving the image. Appendix C.5.1 details trace construction, filtering, and training.
> - **Reinforcement fine-tuning (RFT)** moves beyond offline teacher traces to the prompter’s own rollouts from original image–caption pairs. The prompter generates a thinking trace and SP, which the fixed diffuser renders. A verifier filters these trajectories, and on-policy self-distillation (OPSD) trains the prompter on the accepted ones; we describe both components below.

> <span style="color:#F59E0B"><strong>Para. 31[CN]:</strong></span> 训练阶段如下：
>
> - **监督微调（SFT）** 首先教授扩散器所期望的 SP 内容分布。其核心任务将图像的原始描述视为用户提示，并与我们的图像到 SP 标注流水线生成的 SP 配对。在整个语料库上，这些样本对教授的是关于合理 SP 补全的条件先验，包括物体、属性、几何、深度和关系，而不是确定性的提示到布局映射；图 12 展示了所得布局先验。由通用推理与指令样本组成的回放混合保留基础模型的广泛能力。附录 C.5 详述了回放组成。
> - **冷启动** 教授提示器如何从用户提示推理得到详细 SP。对于每个原始图像—描述对，一个图像条件 VLM 编写推理轨迹，展示无图像提示器如何推断构建目标 SP 所需的视觉决策。由于特权图像访问可能把实例特定观察泄漏进轨迹，Gemini 评判器会拒绝那些在缺少提示扎根、常识或显式设计理由的情况下陈述此类细节的候选，也会拒绝与描述、图像或 SP 不一致的轨迹。随后，提示器在不接收图像的情况下，从获准的（用户提示 → 思考轨迹 → SP）样本学习。附录 C.5.1 详述了轨迹构建、筛选与训练。
> - **强化微调（RFT）** 超越离线教师轨迹，转向提示器在原始图像—描述对上的自身 rollout。提示器生成思考轨迹和 SP，再由固定扩散器渲染。验证器筛选这些轨迹，同策略自蒸馏（OPSD）在获准轨迹上训练提示器；下文将说明这两个组成部分。

> <span style="color:#3B82F6"><strong>Para. 32:</strong></span> **Figure 10: The three-stage prompter-training pipeline (§3.4).** (a) Supervised fine-tuning (SFT) learns the target SP distribution from (user prompt, SP) pairs. (b) Cold-start bootstraps image-free prompt-to-chain-of-thought (CoT)-to-SP derivation from privileged image-conditioned traces. (c) Reinforcement fine-tuning (RFT) renders the student’s own rollouts; a QA verifier selects accepted trajectories, and on-policy self-distillation (OPSD) supplies targets from an image-conditioned teacher. Only the student is updated.

> <span style="color:#F59E0B"><strong>Para. 32[CN]:</strong></span> **图 10：三阶段提示器训练流水线（§3.4）。**（a）监督微调（SFT）从（用户提示，SP）对学习目标 SP 分布。（b）冷启动利用特权图像条件轨迹，自举无图像的提示—思维链（CoT）—SP 推导。（c）强化微调（RFT）渲染学生模型自身的 rollout；QA 验证器选择获准轨迹，同策略自蒸馏（OPSD）提供来自图像条件教师的目标。仅更新学生模型。

> <span style="color:#3B82F6"><strong>Para. 33:</strong></span> Within RFT, the verifier observes only the user request and rendered image. Using its score directly as a reward is unreliable: VLM judgments and stochastic rendering introduce both false acceptances and false rejections, so a single operating threshold cannot be assumed to provide both high precision and high recall. We therefore impose a conservative threshold on alignment, structure, and aesthetics and use the verifier only as a high-precision acceptance gate. This sacrifices rollout coverage but limits training to trajectories whose renders are judged prompt-faithful, structurally coherent, and visually acceptable. Because the verifier still cannot supervise useful visual details left unspecified by the request, OPSD supplies the token-level update on the accepted trajectories.

> <span style="color:#F59E0B"><strong>Para. 33[CN]:</strong></span> 在 RFT 中，验证器只能观察用户请求和渲染图像。直接将其分数用作奖励并不可靠：VLM 判断与随机渲染会同时引入误接受与误拒绝，因此不能假设单一运行阈值同时具有高精确率和高召回率。于是，我们对对齐、结构与美学设置保守阈值，并仅将验证器用作高精确率接受门。这会牺牲 rollout 覆盖率，但能把训练限制在渲染结果被判定为忠实于提示、结构连贯且视觉可接受的轨迹上。由于验证器仍无法监督请求未指定的有用视觉细节，OPSD 会在获准轨迹上提供 token 级更新。

> <span style="color:#3B82F6"><strong>Para. 34:</strong></span> OPSD is motivated by the same privileged-image versus image-free conditioning asymmetry measured by GPG. On each accepted rollout $\tau$, a frozen teacher $\pi^\star$ observes the paired reference image $I$, while the prompter $\pi_\theta$ remains image-free. OPSD minimizes the divergence between their next-token distributions along that rollout:

> <span style="color:#F59E0B"><strong>Para. 34[CN]:</strong></span> OPSD 的动机来自 GPG 所测得的同一种特权图像条件与无图像条件之间的不对称性。对于每条获准 rollout $\tau$，冻结教师 $\pi^\star$ 能观察配对参考图像 $I$，而提示器 $\pi_\theta$ 仍不接收图像。OPSD 最小化沿该 rollout 两者下一 token 分布之间的散度：

$$
\mathcal{L}_{\mathrm{OPSD}}(\theta)
=
\mathbb{E}_{\tau\sim\pi_\theta,\,\tau\ \mathrm{accepted}}
\left[
\frac{1}{|T_\tau|}
\sum_{t\in T_\tau}
D\!\left(
\pi^\star(\cdot\mid\tau_{<t},\operatorname{prompt},I),
\pi_\theta(\cdot\mid\tau_{<t},\operatorname{prompt})
\right)
\right]. \tag{6}
$$

> <span style="color:#3B82F6"><strong>Para. 35:</strong></span> Here the expectation is also over image–caption training pairs $(\mathrm{prompt},I)\sim\mathcal{D}$, $T_\tau$ indexes the rollout’s response tokens, and $D$ is the token-level Kullback–Leibler (KL) divergence from the teacher to the prompter. Appendix C.5.2 details its implementation. The verifier therefore determines which trajectories contribute to training, while OPSD transfers image-grounded token preferences from the teacher to the image-free prompter on those trajectories.

> <span style="color:#F59E0B"><strong>Para. 35[CN]:</strong></span> 这里，期望还遍历图像—描述训练对 $(\mathrm{prompt},I)\sim\mathcal{D}$，$T_\tau$ 索引 rollout 的响应 token，$D$ 是从教师到提示器的 token 级 Kullback–Leibler（KL）散度。附录 C.5.2 详述了其实现。因此，验证器决定哪些轨迹参与训练，而 OPSD 在这些轨迹上把图像扎根的 token 偏好从教师迁移到无图像提示器。

> <span style="color:#3B82F6"><strong>Para. 36:</strong></span> Together, the diffuser trained with structured supervision and the trained LLM prompter raise diffusability and promptability, respectively; §4 evaluates their combined system and ablates the corresponding diffusion-side and prompter-side interventions.

> <span style="color:#F59E0B"><strong>Para. 36[CN]:</strong></span> 综上，使用结构化监督训练的扩散器和经过训练的 LLM 提示器分别提高可扩散性与可提示性；§4 评估它们构成的组合系统，并消融相应的扩散侧与提示器侧干预。

## 4 Experiments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We first compare the complete prompter–diffuser system with representative text-to-image models (§4.1). Holding the schema and diffuser fixed, we then isolate promptability, the LLM-side factor of Eq. (5), through backend and training ablations (§4.2). Finally, we test whether allocating inference-time compute to iterative refinement yields further gains (§4.3).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们首先将完整的提示器—扩散器系统与代表性文本到图像模型比较（§4.1）。随后固定模式与扩散器，通过后端和训练消融来隔离可提示性，即式（5）的 LLM 侧因素（§4.2）。最后，我们检验将推理时计算分配给迭代细化能否带来进一步增益（§4.3）。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Figure 11: Qualitative comparison.** Complex prompts requiring spatial reasoning, attribute binding, and compositional understanding. Columns from left to right: HunyuanImage 3.0, LongCat-Image, Qwen-Image without prompt enhancement (PE), Qwen-Image with official PE, and Ours (Qwen-Image with structured PE). In these examples, the structured-prompt system improves spatial layout, object count, and attribute binding without architectural changes to the diffusion backbone.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 11：定性比较。** 这些复杂提示需要空间推理、属性绑定和组合理解。从左到右各列依次为：HunyuanImage 3.0、LongCat-Image、无提示增强（PE）的 Qwen-Image、使用官方 PE 的 Qwen-Image，以及我们的方法（使用结构化 PE 的 Qwen-Image）。在这些示例中，结构化提示系统无需改变扩散骨干网络架构，就能改善空间布局、物体数量和属性绑定。

### 4.1 End-to-end performance and matched control

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Comparison with existing systems.** Table 2 compares the resulting system with representative open-weight and closed-source generators. Among the evaluated open-weight systems, Ours leads or ties almost every reported metric and matches or surpasses the evaluated closed systems on most. The benchmarks probe complementary capabilities: GenEval and GenEval2 measure object-centric and compositional alignment (Ghosh et al., 2023; Kamath et al., 2025); DPG-Bench and TIIF stress dense and information-intensive prompt following (Hu et al., 2024; Wei et al., 2025); WISE evaluates world knowledge (Niu et al., 2025); and CoReBench targets composition and reasoning (Li et al., 2026). Consistent gains across these settings show that the benefit is not confined to a single prompt regime or evaluator, but extends from basic alignment to knowledge-dependent and reasoning-intensive generation. Figures 2 and 11 reflect the same breadth qualitatively: on complex prompts, the structured-prompt system more faithfully realizes spatial layouts, object counts, and attribute bindings.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **与现有系统比较。** 表 2 将所得系统与代表性开放权重和闭源生成器进行比较。在被评估的开放权重系统中，我们的方法在几乎每项报告指标上领先或并列领先，并在大多数指标上达到或超过被评估的闭源系统。这些基准考察互补能力：GenEval 和 GenEval2 衡量以物体为中心的对齐与组合对齐（Ghosh et al., 2023; Kamath et al., 2025）；DPG-Bench 和 TIIF 强调对密集、信息量大提示的遵循（Hu et al., 2024; Wei et al., 2025）；WISE 评估世界知识（Niu et al., 2025）；CoReBench 针对组合与推理（Li et al., 2026）。在这些设置中一致出现的增益表明，收益并不局限于某一种提示范式或评估器，而是从基础对齐延伸到依赖知识、推理密集的生成。图 2 和图 11 在定性上反映了同样的广度：对于复杂提示，结构化提示系统能更忠实地实现空间布局、物体数量和属性绑定。

### Table 2. Comparison with representative text-to-image systems / 与代表性文本到图像系统的比较

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Table 2: Comparison with representative text-to-image systems.** Higher is better. GenEval2 reports Soft-TIFA arithmetic/geometric means (AM/GM), and TIIF reports short/long accuracy on the testmini subset. “PE” denotes prompt enhancement; Qwen-Image$^\ast$ uses its official PE, and $\dagger$ marks our Qwen-Image-2512 re-evaluation. Ours uses single-shot inference. Evaluation protocols and score provenance are detailed in Appendix D.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **表 2：与代表性文本到图像系统的比较。** 越高越好。GenEval2 报告 Soft-TIFA 的算术／几何平均值（AM/GM），TIIF 报告 testmini 子集上的短／长提示准确率。“PE”表示提示增强；Qwen-Image$^\ast$ 使用其官方 PE，$\dagger$ 表示我们对 Qwen-Image-2512 的重新评估。我们的方法使用单次推理。评估协议和分数来源详见附录 D。

| Model / 模型 | GenEval | GenEval2 (AM/GM) | DPG | TIIF (s/l，短/长) | WISE | CoReBench |
|---|---:|---:|---:|---:|---:|---:|
| **w/o PE / 无 PE** |  |  |  |  |  |  |
| FLUX.1 Dev (Black Forest Labs, 2024) | 0.67 | 67.1/21.1 | 83.84 | 71.1/71.8 | 0.50 | 42.2 |
| OmniGen2 (Wu et al., 2025b) | 0.80 | — | 83.57 | — | — | 42.9 |
| Emu3.5 (Cui et al., 2025) | 0.86 | — | 87.46 | 89.5/88.2 | 0.57 | — |
| BAGEL (Deng et al., 2025) | 0.82 | — | 85.07 | 71.5/71.7 | 0.52 | 38.2 |
| Qwen-Image (Wu et al., 2025a) | 0.87 | 80.8/33.8 | 88.32 | 86.1/86.8 | 0.62 | 58.9 |
| **w/ PE / 有 PE** |  |  |  |  |  |  |
| BAGEL + CoT (Deng et al., 2025) | 0.88 | 70.9/23.1 | — | — | 0.70 | 41.1 |
| GPT-Image-1 (OpenAI, 2025) | 0.84 | — | 85.15 | 89.2/88.3 | 0.80 | 72.6 |
| Nano Banana (Google, 2025) | 0.89 | 82.8/44.6 | 85.23 | — | 0.89 | 75.9 |
| LongCat-Image (Meituan LongCat Team et al., 2025) | 0.87 | — | 86.80 | — | 0.65 | 59.6 |
| HunyuanImage 3.0 (Tencent Hunyuan Foundation Model Team, 2025) | 0.72 | — | 86.10 | — | 0.57 | 58.7 |
| Qwen-Image$^\ast$ | 0.91 | 82.4/52.8$^\dagger$ | 87.20$^\dagger$ | 88.3/88.4$^\dagger$ | 0.83 | 74.7$^\dagger$ |
| Matched NL + Qwen-Image | 0.91 | 84.5/56.2 | 87.80 | 88.5/88.0 | 0.84 | 76.1 |
| **Ours (Qwen-Image)** | **0.94** | **90.6/72.5** | **90.71** | **89.1/89.2** | **0.89** | **85.2** |

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Matched NL control.** To verify that the gains arise from using structured prompts as the shared caption interface between the prompter and diffuser, rather than from a larger backbone or additional training alone, we compare against two controls built on the same Qwen-Image architecture. The official Qwen-Image prompt enhancer reaches 52.8 GenEval2 GM and 74.7 CoReBench, compared with 72.5 and 85.2 for our system. More stringently, matched NL retrains the same Qwen-Image diffuser and prompter on the same images, stages, and budgets while retaining a free-form caption interface. This additional training improves the two scores to 56.2 and 76.1, but remains well below the matched end-to-end SP system. Thus, retraining the same architecture and data with an NL interface does not reproduce the SP system’s gains. Appendix C.2 details the matched control, and Appendix D provides category-level results.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **匹配 NL 对照。** 为验证增益来自使用结构化提示作为提示器与扩散器之间的共享描述接口，而不是仅仅来自更大的骨干网络或额外训练，我们与两个基于同一 Qwen-Image 架构构建的对照进行比较。官方 Qwen-Image 提示增强器达到 52.8 的 GenEval2 GM 和 74.7 的 CoReBench，而我们的系统分别为 72.5 和 85.2。更严格地说，匹配 NL 在保留自由形式描述接口的同时，用相同图像、阶段和预算重新训练同一个 Qwen-Image 扩散器与提示器。额外训练将两项分数提高到 56.2 和 76.1，但仍远低于匹配的端到端 SP 系统。因此，使用 NL 接口在相同架构和数据上重新训练，无法复现 SP 系统的增益。附录 C.2 详述匹配对照，附录 D 给出类别级结果。

### 4.2 Isolating promptability

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Promptability: transferring LLM progress.** We next ask whether advances in general-purpose LLMs can transfer through the SP interface into better text-to-image generation. To isolate this question, Table 3 holds the schema and Qwen-Image diffuser fixed while varying the model and inference procedure used to produce the prompt. Within the single-turn rows, zero-shot SP filling improves alignment and GSB over the same LLM’s NL rewrite, but consistently lowers DPG-Bench and structure. The LLM therefore provides genuine system-level headroom, but zero-shot schema filling alone does not fully realize it. Training the prompter closes this gap; our model is the strongest single-turn backend on all four metrics. The coding-agent rows use each agent’s native multi-turn procedure, so they change both the model and the inference process rather than providing a model-only backend control. Their strong results nevertheless suggest that iterative revision adds value, motivating the controlled common-harness experiment of Section 4.3.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **可提示性：迁移 LLM 进步。** 接下来，我们考察通用 LLM 的进步能否通过 SP 接口迁移为更好的文本到图像生成。为隔离这一问题，表 3 固定模式和 Qwen-Image 扩散器，仅改变用于生成提示的模型与推理过程。在单轮各行中，相较同一 LLM 的 NL 改写，零样本 SP 填充提高了对齐与 GSB，但始终降低 DPG-Bench 和结构分数。因此，LLM 确实提供了系统级提升空间，但仅靠零样本模式填充无法充分实现这一空间。训练提示器弥合了差距；我们的模型在全部四项指标上都是最强的单轮后端。编码智能体各行使用每个智能体原生的多轮流程，因此它们同时改变了模型和推理过程，而不是提供只改变模型的后端对照。尽管如此，其强劲结果仍表明迭代修订具有价值，这促使我们在 §4.3 进行受控的共同执行框架实验。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> **Figure 12: Stage-1 SFT recovers a non-canonical crop.**

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> **图 12：阶段 1 的 SFT 恢复了一个非典型裁剪。**

### Table 3. Rewriting backend comparison / 改写后端比较

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> **Table 3: Rewriting backend comparison.** Schema and Qwen-Image are fixed; rows vary the prompt-producing backend and, where marked, its inference mode. “NL rewrite” is the matched free-form baseline, “agentic” uses each coding agent’s native loop, and “Ours” reproduces the final trained-prompter row of Table 4. DPG-Bench and offline GPT-5.4 evaluations follow Table 4. GSB is the net pairwise preference $100(n_{\mathrm{Good}}-n_{\mathrm{Bad}})/N$ against the zero-shot, single-shot Qwen3.5-397B-A17B Base prompter; each pair is judged in both image orders, with inconsistent orderings counted as Same, over $N=150$ prompt pairs (Appendix E.5). Bold marks the best in each column.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **表 3：改写后端比较。** 模式和 Qwen-Image 保持固定；各行改变生成提示的后端，以及标明时所用的推理模式。“NL rewrite”是匹配的自由形式基线，“agentic”使用各编码智能体的原生循环，“Ours”复现表 4 中训练后提示器的最终一行。DPG-Bench 和离线 GPT-5.4 评估遵循表 4。GSB 是相对于零样本、单次 Qwen3.5-397B-A17B Base 提示器的成对净偏好 $100(n_{\mathrm{Good}}-n_{\mathrm{Bad}})/N$；在 $N=150$ 对提示上，每一对都以两种图像顺序进行评判，不一致的顺序判断计为 Same（附录 E.5）。粗体表示每列最佳结果。

| Rewriting Backend / 改写后端 | Mode / 模式 | DPG-Bench | Offline Judge Structure / 离线结构 (GPT-5.4, 0–10) | Offline Judge Alignment / 离线对齐 (GPT-5.4, 0–10) | GSB vs Base (%) / 相对 Base 的 GSB (%) |
|---|---|---:|---:|---:|---:|
| GPT-5.5 | NL rewrite | 90.18 | 6.913 | 8.747 | 36.0 |
| Claude Opus 4.8 | NL rewrite | 89.93 | 6.733 | 8.617 | 32.7 |
| GLM-5.2 | NL rewrite | 89.47 | 6.653 | 8.493 | 30.0 |
| Gemini 3 Pro | NL rewrite | 88.72 | 6.183 | 8.107 | 19.3 |
| GPT-5.5 | single-turn / 单轮 | 89.84 | 6.840 | 8.907 | 37.3 |
| Claude Opus 4.8 | single-turn / 单轮 | 89.21 | 6.653 | 8.793 | 34.7 |
| GLM-5.2 | single-turn / 单轮 | 88.93 | 6.557 | 8.746 | 32.0 |
| Gemini 3 Pro | single-turn / 单轮 | 87.86 | 6.020 | 8.687 | 21.3 |
| Codex | agentic / 智能体式 | 90.32 | 7.360 | 8.980 | 38.7 |
| Claude Code | agentic / 智能体式 | 90.63 | 7.560 | **9.087** | **44.7** |
| Ours (LoRA-on-Qwen3.5-397B-A17B + RFT) | single-turn / 单轮 | **90.71** | **7.600** | 9.047 | 42.0 |

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **Promptability: training the prompter.** We next study how task-specific training improves promptability by examining the contribution of each training stage and supervision signal. Table 4 holds the schema and diffuser fixed, cumulatively adds SFT and Cold-start, and then varies the RFT signal. SFT produces the largest single-stage gain in structure (4.860 → 6.273) and a 23.3% GSB preference, consistent with learning plausible SP content rather than JSON syntax alone; Figure 12 illustrates the acquired layout prior. Cold-start further improves structure and GSB, although alignment decreases slightly, showing that its privileged traces do not improve every criterion uniformly. Verifier-reward GRPO and ungated OPSD both improve structure, alignment, and GSB over Cold-start; combining high-confidence rollout selection with dense image-conditioned OPSD targets gives the strongest endpoint. Across the full pipeline, DPG-Bench changes by only 1.29 points, whereas structure rises to 7.600 and GSB to 42.0%. DPG-Bench is therefore comparatively insensitive to the structural and compositional differences visible in Figure 13. Overall, the ablation supports the intended division of labor: SFT learns the target SP distribution, Cold-start teaches image-free derivation, and RFT improves the prompter on its own rollouts.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **可提示性：训练提示器。** 接下来，我们通过考察各训练阶段与监督信号的贡献，研究任务特定训练如何改善可提示性。表 4 固定模式和扩散器，依次累加 SFT 与冷启动，再改变 RFT 信号。SFT 带来最大的单阶段结构增益（4.860 → 6.273）和 23.3% 的 GSB 偏好，这与学习合理 SP 内容而非仅学习 JSON 语法一致；图 12 展示了学得的布局先验。冷启动进一步改善结构和 GSB，尽管对齐略有下降，说明其特权轨迹并非均匀改善每项标准。相较冷启动，验证器奖励 GRPO 与无门控 OPSD 都能改善结构、对齐与 GSB；把高置信 rollout 选择与密集图像条件 OPSD 目标相结合，得到最强终点。在完整流水线上，DPG-Bench 仅变化 1.29 分，而结构提高到 7.600，GSB 提高到 42.0%。因此，DPG-Bench 对图 13 可见的结构与组合差异相对不敏感。总体而言，消融支持预期的分工：SFT 学习目标 SP 分布，冷启动教授无图像推导，RFT 则在提示器自身 rollout 上改进提示器。

### Table 4. Prompter training-pipeline ablation / 提示器训练流水线消融

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> **Table 4: Prompter training-pipeline ablation.** Rows add SFT and Cold-start, then compare Group Relative Policy Optimization (GRPO) with the QA verifier score as reward (Shao et al., 2024), ungated OPSD, and the full verifier-gated OPSD rule. Schema (L10) and Qwen-Image are fixed, so only prompter training changes. Structure/alignment (0–10) and GSB are evaluated offline by GPT-5.4; GSB is the order-swapped net preference against the zero-shot, single-shot Qwen3.5-397B-A17B Base prompter over $N=150$ prompt pairs (Appendix E.5). The training verifier’s aesthetic score is used only for rollout acceptance.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> **表 4：提示器训练流水线消融。** 各行加入 SFT 与冷启动，随后比较以 QA 验证器分数为奖励的 Group Relative Policy Optimization（GRPO）（Shao et al., 2024）、无门控 OPSD 和完整的验证器门控 OPSD 规则。模式（L10）和 Qwen-Image 固定，因此只有提示器训练发生变化。结构／对齐（0–10）和 GSB 由 GPT-5.4 离线评估；GSB 是在 $N=150$ 对提示上，相对于零样本、单次 Qwen3.5-397B-A17B Base 提示器的顺序交换净偏好（附录 E.5）。训练验证器的美学分数仅用于 rollout 接受。

| Training stage / 训练阶段 | DPG-Bench | Structure / 结构 (GPT-5.4, 0–10) | Alignment / 对齐 (GPT-5.4, 0–10) | GSB (%) |
|---|---:|---:|---:|---:|
| Base | 89.42 | 4.860 | 8.307 | — |
| + SFT | 89.61 | 6.273 | 8.473 | 23.3 |
| + Cold-start | 89.84 | 6.753 | 8.360 | 28.7 |
| + RFT: verifier-reward GRPO | 89.73 | 7.113 | 8.907 | 36.7 |
| + RFT: ungated OPSD | 89.68 | 6.993 | 8.747 | 33.3 |
| **+ RFT: verifier-gated OPSD** | **90.71** | **7.600** | **9.047** | **42.0** |

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> **Figure 13: Qualitative progression across prompter training stages.** Each row uses one user prompt and the same Qwen-Image backbone; across these multilingual, dense-text, and poster-design examples, text fidelity, compositional density, and layout structure improve stage by stage.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> **图 13：提示器各训练阶段的定性进展。** 每行使用一条用户提示和同一个 Qwen-Image 骨干网络；在这些多语言、密集文本和海报设计示例中，文本忠实度、组合密度和布局结构逐阶段改善。

### 4.3 Inference-time scaling of promptability

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> The strong coding-agent results in Table 3 suggest that their native multi-turn harnesses contribute beyond the underlying rewriting backend. Motivated by this observation, we isolate iterative inference from backend choice by placing both the Base and trained prompters in the same refine–render–judge loop. Prior work scales inference on the input side by training a prompt rewriter offline (Chen et al., 2025); here the loop runs online at generation time and the prompter weights are held fixed. The schema, diffuser, online judge, and prompter weights remain fixed within each comparison; only the available refinement budget changes. Because SPs expose visual decisions in named fields, critiques can be translated into targeted revisions instead of rewriting the entire caption.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 表 3 中编码智能体的强劲结果表明，其原生多轮执行框架带来的贡献超越了底层改写后端。受此观察启发，我们将 Base 与训练后提示器置于同一个细化—渲染—评判循环中，从而将迭代推理与后端选择隔离。先前工作通过离线训练提示改写器在输入侧缩放推理（Chen et al., 2025）；这里，循环在生成时在线运行，提示器权重保持固定。每项比较内的模式、扩散器、在线评判器和提示器权重都保持固定；只有可用细化预算发生变化。由于 SP 以命名字段呈现视觉决策，批评可以转化为定向修订，而无须重写整条描述。

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> **Refine–render–judge loop.** As shown in Figure 14, the loop maintains the previous SPs and the critique history as explicit state. At round $t$, the prompter uses this state together with the original user request to produce $\mathrm{SP}_t$, and the fixed diffuser renders $I_t$. The online Gemini judge sees only the user request and $I_t$, not the SP. It checks prompt-derived requirements alongside structural and aesthetic quality, then returns per-axis scores, a PASS/FAIL decision, and a structured list of observed failures. A PASS immediately returns $I_t$; after a FAIL, the critique is appended to the prompter context so that the next round can revise the corresponding objects, attributes, relations, or layout fields. Repeated failures permit progressively broader changes, from local field edits to element regrouping and full scene re-planning, as illustrated in Figure 15. The loop terminates at PASS or $T_{\max}$. Reported results are evaluated by GPT-5.4 in a separate offline pass rather than by the online Gemini judge, so the control signal and the final evaluation use different models, though both apply the same rubrics (Appendix E.4); Appendix C.6 specifies the formal loop, 6/10 PASS threshold, and per-round cost.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> **细化—渲染—评判循环。** 如图 14 所示，该循环把先前 SP 和批评历史作为显式状态维护。在第 $t$ 轮，提示器将该状态与原始用户请求结合，生成 $\mathrm{SP}_t$，固定扩散器再渲染 $I_t$。在线 Gemini 评判器只能看到用户请求与 $I_t$，看不到 SP。它在检查源自提示的要求之外，还检查结构与美学质量，随后返回逐轴分数、PASS/FAIL 决策以及结构化的已观察失败列表。若为 PASS，则立即返回 $I_t$；若为 FAIL，则把批评追加到提示器上下文，使下一轮能够修改相应的物体、属性、关系或布局字段。反复失败允许进行范围逐渐扩大的改动，从局部字段编辑到元素重组，再到完整场景重新规划，如图 15 所示。循环在 PASS 或 $T_{\max}$ 时终止。报告结果由 GPT-5.4 在单独的离线过程中评估，而不是由在线 Gemini 评判器评估，因此控制信号与最终评估使用不同模型，不过两者应用相同评分准则（附录 E.4）；附录 C.6 规定了形式化循环、6/10 的 PASS 阈值和每轮成本。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> **Figure 14: The agentic inference-time loop.** At round $t$, the prompter emits $\mathrm{SP}_t$ from the user prompt and accumulated critique; the fixed diffuser renders $I_t$; and the Gemini judge returns PASS or field-level critique over structure, alignment, and aesthetics. Failed rounds edit targeted schema slots and stop at PASS or $T_{\max}$.

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> **图 14：智能体式推理时循环。** 在第 $t$ 轮，提示器根据用户提示和累积批评生成 $\mathrm{SP}_t$；固定扩散器渲染 $I_t$；Gemini 评判器针对结构、对齐和美学返回 PASS 或字段级批评。失败轮次会编辑目标模式槽位，并在 PASS 或 $T_{\max}$ 时停止。

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> **Figure 15: Case types the agentic loop resolves.** Each pair shows the round-1 defect (R1) and the accepted result (PASS), with the structured edit beneath. Structure fixes add missing support relations; granularity fixes collapse over-enumerated elements to renderable groups; larger layout fixes re-compose the scene when local edits are insufficient.

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> **图 15：智能体循环解决的案例类型。** 每一对都展示第 1 轮缺陷（R1）和获准结果（PASS），下方给出结构化编辑。结构修复会添加缺失的支撑关系；粒度修复会把枚举过细的元素合并为可渲染分组；当局部编辑不足时，更大范围的布局修复会重新组合场景。

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> **Returns from additional rounds.** Table 5 shows that both prompters improve with $T_{\max}$ when the schema, diffusion backbone, judge, and prompter weights are held fixed. The larger change is in structure: from one to eight rounds it rises by 1.247 for Base and 0.660 for the trained prompter, compared with alignment gains of 0.366 and 0.266. Together with Figure 15, this indicates that feedback primarily repairs object decomposition, relations, and layout rather than basic prompt alignment.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> **增加轮数的收益。** 表 5 表明，在固定模式、扩散骨干网络、评判器和提示器权重时，两种提示器都随 $T_{\max}$ 增大而改善。更大的变化发生在结构上：从一轮到八轮，Base 的结构分数提高 1.247，训练后提示器提高 0.660；相比之下，对齐增益分别为 0.366 和 0.266。结合图 15，这表明反馈主要修复物体分解、关系与布局，而不是基础提示对齐。

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> Placing the trained prompter in this loop also answers the agentic backends of Table 3: at $T_{\max}=8$ it reaches 54.7% GSB, above the 44.7% of the strongest coding agent, which is itself already multi-turn. Training absorbs much of the work that would otherwise require iterative correction. Even after eight rounds, Base remains below the trained prompter in a single shot on both structure (6.107 vs. 7.600) and GSB (24.0% vs. 42.0%). Under the same eight-round limit, the trained prompter also reaches PASS after only 2.31 rounds on average, compared with 3.41 for Base. Thus, prompter training not only raises the starting point but also shortens the subsequent refinement trajectory; agentic inference complements training rather than replacing it.

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> 将训练后提示器置于该循环中，也回应了表 3 的智能体后端：在 $T_{\max}=8$ 时，它达到 54.7% GSB，高于最强编码智能体的 44.7%，而后者本身已经是多轮系统。训练吸收了大量原本需要迭代校正完成的工作。即使经过八轮，Base 在结构（6.107 对 7.600）和 GSB（24.0% 对 42.0%）上仍低于训练后提示器的单次结果。在相同八轮上限下，训练后提示器平均只需 2.31 轮便达到 PASS，而 Base 需要 3.41 轮。因此，提示器训练不仅提高起点，还缩短后续细化轨迹；智能体式推理是对训练的补充，而非替代。

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> The effective refinement horizon is also short. For the trained prompter, increasing $T_{\max}$ from four to eight raises the average rounds only from 2.04 to 2.31, while structure changes from 8.213 to 8.260 and GSB from 54.0% to 54.7%. The average therefore stays close to two rounds, and little is gained by permitting a substantially longer trajectory. Within the tested schema, judge, refinement policy, and diffuser, text-to-image generation benefits from iterative correction but does not exhibit a strong need for long-horizon prompt-side reasoning: once the main specification errors are repaired, further render–feedback rounds quickly saturate.

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> 有效细化视野也很短。对于训练后提示器，将 $T_{\max}$ 从四提高到八，只会把平均轮数从 2.04 提高到 2.31；结构分数从 8.213 变为 8.260，GSB 从 54.0% 变为 54.7%。因此，平均轮数保持在接近两轮，允许显著更长的轨迹几乎没有收益。在被测试的模式、评判器、细化策略和扩散器下，文本到图像生成受益于迭代校正，但并不强烈需要长视野的提示侧推理：一旦主要规格错误得到修复，进一步的渲染—反馈轮次很快就会饱和。

### Table 5. Agentic inference-time scaling / 智能体式推理时缩放

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> **Table 5: Agentic inference-time scaling.** At fixed schema, Qwen-Image backbone, online Gemini judge, and prompter weights, increasing $T_{\max}$ allocates more refine–render–judge rounds. Final outputs are evaluated offline by GPT-5.4 for structure/alignment and order-swapped GSB net preference against the zero-shot Qwen3.5-397B-A17B Base prompter at $T_{\max}=1$, over the 150-prompt evaluation pool ($N=150$, Appendix E.5); average rounds measures refinement rounds consumed, each of which issues three Gemini judge calls, and $T_{\max}=1$ is single-shot inference.

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> **表 5：智能体式推理时缩放。** 在固定模式、Qwen-Image 骨干网络、在线 Gemini 评判器和提示器权重的情况下，增大 $T_{\max}$ 会分配更多细化—渲染—评判轮次。最终输出由 GPT-5.4 离线评估结构／对齐，并在 150 条提示评估池（$N=150$，附录 E.5）上，计算相对于 $T_{\max}=1$ 的零样本 Qwen3.5-397B-A17B Base 提示器的顺序交换 GSB 净偏好；平均轮数衡量所消耗的细化轮数，每轮会发出三次 Gemini 评判器调用，而 $T_{\max}=1$ 表示单次推理。

| Prompter / 提示器 | $T_{\max}$ | Structure / 结构 (GPT-5.4, 0–10) | Alignment / 对齐 (GPT-5.4, 0–10) | GSB (%) | Avg. rounds / 平均轮数 |
|---|---:|---:|---:|---:|---:|
| Base (zero-shot / 零样本) | 1 | 4.860 | 8.307 | — | 1.00 |
| Base (zero-shot / 零样本) | 2 | 5.387 | 8.493 | 14.7 | 1.74 |
| Base (zero-shot / 零样本) | 4 | 6.027 | 8.640 | 22.7 | 2.83 |
| Base (zero-shot / 零样本) | 8 | 6.107 | 8.673 | 24.0 | 3.41 |
| Trained (SFT + Cold-start + RFT) / 已训练 | 1 | 7.600 | 9.047 | 42.0 | 1.00 |
| Trained (SFT + Cold-start + RFT) / 已训练 | 2 | 7.940 | 9.173 | 49.3 | 1.51 |
| Trained (SFT + Cold-start + RFT) / 已训练 | 4 | 8.213 | 9.293 | 54.0 | 2.04 |
| Trained (SFT + Cold-start + RFT) / 已训练 | 8 | 8.260 | 9.313 | 54.7 | 2.31 |

## 5 Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We show that caption information content, rather than caption length, is a measurable and scalable axis in text-to-image learning. Across controlled caption configurations, GPG and ED predict converged diffusion loss, defining empirical scaling properties for text conditioning that can be used to compare caption representations after calibration. This supports a Diffusability×Promptability view of the caption interface: structured prompts raise diffusability by exposing and organizing image-grounded variables in addressable fields, while scaling and training the LLM prompter raises promptability by translating user requests into detailed, coherent instances of that representation. Matched natural-language retraining shows that the structured-representation gains are not explained by additional training alone, and the resulting end-to-end system improves visual coherence, prompt fidelity, and compositional generation without changing the diffusion architecture. At inference, short refine–render–judge loops provide further gains, but the trained prompter internalizes much of the correction and additional rounds yield rapidly diminishing returns; prompt-side inference compute is therefore a complement to training rather than a substitute for it.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们表明，描述的信息内容而非描述长度，是文本到图像学习中一个可测量、可缩放的轴。在受控描述配置中，GPG 和 ED 可以预测收敛扩散损失，由此定义出文本条件的经验缩放性质；经过校准后，这些性质可用于比较描述表示。这支持一种把描述接口视为 Diffusability×Promptability 的观点：结构化提示通过在可寻址字段中呈现和组织图像扎根变量来提高可扩散性；扩大并训练 LLM 提示器，则通过把用户请求转换成该表示的详细、连贯实例来提高可提示性。匹配自然语言重新训练表明，结构化表示的增益不能仅由额外训练解释；所得端到端系统无需改变扩散架构，就能改善视觉连贯性、提示忠实度和组合生成。在推理时，短程细化—渲染—评判循环会带来进一步增益，但训练后提示器已经内化了大部分校正，新增轮次的收益会迅速递减；因此，提示侧推理计算是对训练的补充，而非替代。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Limitations.** Both metrics depend on image-conditioned measurement: GPG queries a vision–language judge at scoring time, while ED requires a one-time offline extraction of attribute tuples from each image. The fitted relations may shift under different judges or extractors. Agreement between the two measures reduces, but does not eliminate, the risk that the shared trend reflects a particular scoring interface. The schema is hand-designed; automatic schema discovery and extension to video and three-dimensional generation remain open. The structured-prompt path also adds prompter latency, so deployment must weigh the generation gains against this additional inference cost.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **局限性。** 两项指标都依赖图像条件测量：GPG 在评分时查询视觉—语言评判器，而 ED 需要离线地从每张图像中一次性提取属性元组。在不同评判器或提取器下，拟合关系可能发生偏移。两种度量之间的一致性降低了共同趋势反映某一特定评分接口的风险，但不能消除该风险。模式由人工设计；自动模式发现以及向视频和三维生成扩展仍是开放问题。结构化提示路径还会增加提示器延迟，因此部署时必须在生成增益与额外推理成本之间权衡。

## References

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> James Betker, Gabriel Goh, Li Jing, Tim Brooks, Jianfeng Wang, Linjie Li, Long Ouyang, Juntang Zhuang, Joyce Lee, Yufei Guo, Wesam Manassra, Prafulla Dhariwal, Casey Chu, Yunxin Jiao, and Aditya Ramesh. Improving image generation with better captions. Technical report, OpenAI, 2023. URL https://cdn.openai.com/papers/dall-e-3.pdf.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Black Forest Labs. Announcing Black Forest Labs. https://blackforestlabs.ai/announcing-black-forest-labs/, 2024. Model release.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Hila Chefer, Yuval Alaluf, Yael Vinker, Lior Wolf, and Daniel Cohen-Or. Attend-and-excite: Attention-based semantic guidance for text-to-image diffusion models. ACM Transactions on Graphics (SIGGRAPH), 42(4), 2023.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Junsong Chen, Chongjian Ge, Enze Xie, Yue Wu, Lewei Yao, Xiaozhe Ren, Zhongdao Wang, Ping Luo, Huchuan Lu, and Zhenguo Li. PixArt-Σ: Weak-to-strong training of diffusion transformer for 4K text-to-image generation. In European Conference on Computer Vision (ECCV), 2024a.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Junsong Chen, Jincheng Yu, Chongjian Ge, Lewei Yao, Enze Xie, Yue Wu, Zhongdao Wang, James Kwok, Ping Luo, Huchuan Lu, and Zhenguo Li. PixArt-α: Fast training of diffusion transformer for photorealistic text-to-image synthesis. In International Conference on Learning Representations (ICLR), 2024b.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Ruibo Chen, Jiacheng Pan, Heng Huang, and Zhenheng Yang. Improving text-to-image generation with input-side inference-time scaling. arXiv preprint arXiv:2510.12041, 2025.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> Sheng Cheng, Maitreya Patel, and Yezhou Yang. Precision or recall? an analysis of image captions for training text-to-image generation model. In Findings of the Association for Computational Linguistics: EMNLP 2024, 2024.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> Yufeng Cui, Honghao Chen, Haoge Deng, Xu Huang, Xinghang Li, Jirong Liu, Yang Liu, Zhuoyan Luo, Jinsheng Wang, et al. Emu3.5: Native multimodal models are world learners. arXiv preprint arXiv:2510.26583, 2025.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Chaorui Deng, Deyao Zhu, Kunchang Li, Chenhui Gou, Feng Li, Zeyu Wang, Shu Zhong, Weihao Yu, Xiaonan Nie, Ziang Song, Guang Shi, and Haoqi Fan. Emerging properties in unified multimodal pretraining. arXiv preprint arXiv:2505.14683, 2025.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> Patrick Esser, Sumith Kulal, Andreas Blattmann, Rahim Entezari, Jonas Müller, Harry Saini, Yam Levi, Dominik Lorenz, Axel Sauer, Frederic Boesel, Dustin Podell, Tim Dockhorn, Zion English, Kyle Lacey, Alex Goodwin, Yannik Marek, and Robin Rombach. Scaling rectified flow transformers for high-resolution image synthesis. In International Conference on Machine Learning (ICML), 2024.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> Alessandro Favero, Luca Zancato, Matthew Trager, Siddharth Choudhary, Pramuditha Perera, Alessandro Achille, Ashwin Swaminathan, and Stefano Soatto. Multi-modal hallucination control by visual information grounding. In Conference on Computer Vision and Pattern Recognition (CVPR), 2024.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> Dhruba Ghosh, Hannaneh Hajishirzi, and Ludwig Schmidt. GenEval: An object-focused framework for evaluating text-to-image alignment. In Advances in Neural Information Processing Systems, Datasets and Benchmarks Track, 2023.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> Google. Nano banana (gemini 2.5 flash image). https://blog.google/products/gemini/updated-image-editing-model/, 2025. Model release.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> Litao Guo, Xinli Xu, Luozhou Wang, Jiantao Lin, Jinsong Zhou, Zixin Zhang, Bolan Su, and Ying-Cong Chen. ComfyMind: Toward general-purpose generation via tree-based planning and reactive feedback. In Advances in Neural Information Processing Systems, 2025. URL https://papers.nips.cc/paper_files/paper/2025/file/40168e00bf87869c5d153e934d8a3602-Paper-Conference.pdf.

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> Eyal Gutflaish, Eliran Kachlon, Hezi Zisman, Tal Hacham, Nimrod Sarid, Alexander Visheratin, Saar Huberman, Gal Davidi, Guy Bukchin, Kfir Goldberg, and Ron Mokady. Generating an Image From 1,000 Words: Enhancing Text-to-Image With Structured Captions. arXiv preprint arXiv:2511.06876, 2025.

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> Frank R. Hampel. The influence curve and its role in robust estimation. Journal of the American Statistical Association, 69(346):383–393, 1974.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 17:</strong></span> Zefeng He, Siyuan Huang, Xiaoye Qu, Yafu Li, Tong Zhu, Yu Cheng, and Yang Yang. GEMS: Agent-native multimodal generation with memory and skills. arXiv preprint arXiv:2603.28088, 2026.

> <span style="color:#F59E0B"><strong>Para. 17[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 18:</strong></span> Jack Hessel, Ari Holtzman, Maxwell Forbes, Ronan Le Bras, and Yejin Choi. CLIPScore: A reference-free evaluation metric for image captioning. In Empirical Methods in Natural Language Processing (EMNLP), 2021.

> <span style="color:#F59E0B"><strong>Para. 18[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 19:</strong></span> Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. In Advances in Neural Information Processing Systems (NeurIPS), 2020.

> <span style="color:#F59E0B"><strong>Para. 19[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 20:</strong></span> Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, Elena Buchatskaya, Trevor Cai, Eliza Rutherford, Diego de Las Casas, Lisa Anne Hendricks, Johannes Welbl, Aidan Clark, et al. Training compute-optimal large language models. In Advances in Neural Information Processing Systems (NeurIPS), 2022.

> <span style="color:#F59E0B"><strong>Para. 20[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 21:</strong></span> Edward J. Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen. LoRA: Low-rank adaptation of large language models. arXiv preprint arXiv:2106.09685, 2021.

> <span style="color:#F59E0B"><strong>Para. 21[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 22:</strong></span> Xiwei Hu, Rui Wang, Yixiao Fang, Bin Fu, Pei Cheng, and Gang Yu. Ella: Equip diffusion models with llm for enhanced semantic alignment. arXiv preprint arXiv:2403.05135, 2024.

> <span style="color:#F59E0B"><strong>Para. 22[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 23:</strong></span> Qirui Jiao, Daoyuan Chen, Yilun Huang, Xika Lin, Ying Shen, and Yaliang Li. DetailMaster: Can your text-to-image model handle long prompts? arXiv preprint arXiv:2505.16915, 2025.

> <span style="color:#F59E0B"><strong>Para. 23[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 24:</strong></span> Amita Kamath, Kai-Wei Chang, Ranjay Krishna, Luke Zettlemoyer, Yushi Hu, and Marjan Ghazvininejad. GenEval 2: Addressing benchmark drift in text-to-image evaluation. arXiv preprint arXiv:2512.16853, 2025.

> <span style="color:#F59E0B"><strong>Para. 24[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 25:</strong></span> Jared Kaplan, Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child, Scott Gray, Alec Radford, Jeffrey Wu, and Dario Amodei. Scaling laws for neural language models. arXiv preprint arXiv:2001.08361, 2020.

> <span style="color:#F59E0B"><strong>Para. 25[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 26:</strong></span> Rawal Khirodkar, Timur Bagautdinov, Julieta Martinez, Su Zhaoen, Austin James, Peter Selednik, Stuart Anderson, and Shunsuke Saito. Sapiens: Foundation for human vision models. In European Conference on Computer Vision (ECCV), 2024.

> <span style="color:#F59E0B"><strong>Para. 26[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 27:</strong></span> Ouxiang Li, Yuan Wang, Xinting Hu, Huijuan Huang, Rui Chen, Jiarong Ou, Xin Tao, Pengfei Wan, Xiaojuan Qi, and Fuli Feng. Easier painting than thinking: Can text-to-image models set the stage, but not direct the play? In International Conference on Learning Representations, 2026.

> <span style="color:#F59E0B"><strong>Para. 27[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 28:</strong></span> Yuheng Li, Haotian Liu, Qingyang Wu, Fangzhou Mu, Jianwei Yang, Jianfeng Gao, Chunyuan Li, and Yong Jae Lee. GLIGEN: Open-set grounded text-to-image generation. In Conference on Computer Vision and Pattern Recognition (CVPR), 2023.

> <span style="color:#F59E0B"><strong>Para. 28[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 29:</strong></span> Zhengyang Liang, Hao He, Ceyuan Yang, and Bo Dai. Scaling laws for diffusion transformers. arXiv preprint arXiv:2410.08184, 2024.

> <span style="color:#F59E0B"><strong>Para. 29[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 30:</strong></span> Zhiqiu Lin, Deepak Pathak, Baiqi Li, Jiayao Li, Xide Xia, Graham Neubig, Pengchuan Zhang, and Deva Ramanan. Evaluating text-to-visual generation with image-to-text generation. In European Conference on Computer Vision (ECCV), 2024.

> <span style="color:#F59E0B"><strong>Para. 30[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 31:</strong></span> Meituan LongCat Team, Hanghang Ma, Haoxian Tan, Jiale Huang, Junqiang Wu, Jun-Yan He, Lishuai Gao, Songlin Xiao, Xiaoming Wei, Xiaoqi Ma, Xunliang Cai, Yayong Guan, and Jie Hu. LongCat-Image technical report. arXiv preprint arXiv:2512.07584, 2025.

> <span style="color:#F59E0B"><strong>Para. 31[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 32:</strong></span> Nicholas Merchant, Haitz Sáez de Ocáriz Borde, Andrei Cristian Popescu, and Carlos Garcia Jurado Suarez. Structured captions improve prompt adherence in text-to-image models (re-laion-caption 19m). arXiv preprint arXiv:2507.05300, 2025.

> <span style="color:#F59E0B"><strong>Para. 32[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 33:</strong></span> Yuwei Niu, Munan Ning, Mengren Zheng, Weiyang Jin, Bin Lin, Peng Jin, Jiaqi Liao, Chaoran Feng, Fanqing Meng, Kunpeng Ning, Bin Zhu, and Li Yuan. WISE: A world knowledge-informed semantic evaluation for text-to-image generation. arXiv preprint arXiv:2503.07265, 2025.

> <span style="color:#F59E0B"><strong>Para. 33[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 34:</strong></span> NVIDIA. Cosmos 3: Omnimodal World Models for Physical AI. arXiv preprint arXiv:2606.02800, 2026. URL https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf.

> <span style="color:#F59E0B"><strong>Para. 34[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 35:</strong></span> Yasumasa Onoe, Sunayana Rane, Zachary Berger, Yonatan Bitton, Jaemin Cho, Roopal Garg, Alexander Ku, Zarana Parekh, Jordi Pont-Tuset, Garrett Tanzer, Su Wang, and Jason Baldridge. DOCCI: Descriptions of connected and contrasting images. In European Conference on Computer Vision (ECCV), 2024.

> <span style="color:#F59E0B"><strong>Para. 35[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 36:</strong></span> OpenAI. GPT-Image-1. https://openai.com/index/image-generation-api/, 2025. Model release.

> <span style="color:#F59E0B"><strong>Para. 36[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 37:</strong></span> William Peebles and Saining Xie. Scalable diffusion models with transformers. In International Conference on Computer Vision (ICCV), 2023.

> <span style="color:#F59E0B"><strong>Para. 37[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 38:</strong></span> Dustin Podell, Zion English, Kyle Lacey, Andreas Blattmann, Tim Dockhorn, Jonas Müller, Joe Penna, and Robin Rombach. SDXL: Improving latent diffusion models for high-resolution image synthesis. arXiv preprint arXiv:2307.01952, 2023.

> <span style="color:#F59E0B"><strong>Para. 38[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 39:</strong></span> Qwen Team. Qwen3.5. https://qwen.ai/blog?id=qwen3.5, 2025. Blog post.

> <span style="color:#F59E0B"><strong>Para. 39[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 40:</strong></span> Nikhila Ravi, Valentin Gabeur, Yuan-Ting Hu, Ronghang Hu, Chaitanya Ryali, Tengyu Ma, Haitham Khedr, Roman Rädle, Chloe Rolland, Laura Gustafson, Eric Mintun, Junting Pan, Kalyan Vasudev Alwala, Nicolas Carion, Chao-Yuan Wu, Ross Girshick, Piotr Dollár, and Christoph Feichtenhofer. SAM 2: Segment anything in images and videos. arXiv preprint arXiv:2408.00714, 2024.

> <span style="color:#F59E0B"><strong>Para. 40[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 41:</strong></span> Reve Team. The Layout Bet, June 2026. URL https://blog.reve.com/posts/the-layout-bet/.

> <span style="color:#F59E0B"><strong>Para. 41[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 42:</strong></span> Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer. High-resolution image synthesis with latent diffusion models. In Conference on Computer Vision and Pattern Recognition (CVPR), 2022.

> <span style="color:#F59E0B"><strong>Para. 42[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 43:</strong></span> Chitwan Saharia, William Chan, Saurabh Saxena, Lala Li, Jay Whang, Emily L. Denton, Seyed Kamyar Seyed Ghasemipour, Burcu Karagol Ayan, S. Sara Mahdavi, Raphael Gontijo Lopes, Tim Salimans, Jonathan Ho, David J. Fleet, and Mohammad Norouzi. Photorealistic text-to-image diffusion models with deep language understanding. In Advances in Neural Information Processing Systems (NeurIPS), 2022.

> <span style="color:#F59E0B"><strong>Para. 43[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 44:</strong></span> Christoph Schuhmann, Romain Beaumont, Richard Vencu, Cade Gordon, Ross Wightman, Mehdi Cherti, Theo Coombes, Aarush Katta, Clayton Mullis, Mitchell Wortsman, Patrick Schramowski, Srivatsa Kundurthy, Katherine Crowson, Ludwig Schmidt, Robert Kaczmarczyk, and Jenia Jitsev. LAION-5B: An open large-scale dataset for training next generation image-text models. In Advances in Neural Information Processing Systems (NeurIPS) Datasets & Benchmarks Track, 2022.

> <span style="color:#F59E0B"><strong>Para. 44[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 45:</strong></span> Eyal Segalis, Dani Valevski, Danny Lumen, Yossi Matias, and Yaniv Leviathan. A picture is worth a thousand words: Principled recaptioning improves image generation. arXiv preprint arXiv:2310.16656, 2023.

> <span style="color:#F59E0B"><strong>Para. 45[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 46:</strong></span> Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang, Mingchuan Zhang, Y. K. Li, Y. Wu, and Daya Guo. DeepSeekMath: Pushing the limits of mathematical reasoning in open language models. arXiv preprint arXiv:2402.03300, 2024.

> <span style="color:#F59E0B"><strong>Para. 46[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 47:</strong></span> Ivan Skorokhodov, Sharath Girish, Benran Hu, Willi Menapace, Yanyu Li, Rameen Abdal, Sergey Tulyakov, and Aliaksandr Siarohin. Improving the diffusability of autoencoders. arXiv preprint arXiv:2502.14831, 2025.

> <span style="color:#F59E0B"><strong>Para. 47[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 48:</strong></span> Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Kumar, Stefano Ermon, and Ben Poole. Score-based generative modeling through stochastic differential equations. In International Conference on Learning Representations (ICLR), 2021.

> <span style="color:#F59E0B"><strong>Para. 48[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 49:</strong></span> Tencent Hunyuan Foundation Model Team. HunyuanImage 3.0 technical report. arXiv preprint arXiv:2509.23951, 2025.

> <span style="color:#F59E0B"><strong>Para. 49[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 50:</strong></span> Jack Urbanek, Florian Bordes, Pietro Astolfi, Mary Williamson, Vasu Sharma, and Adriana Romero-Soriano. A picture is worth more than 77 text tokens: Evaluating CLIP-style models on dense captions. In Conference on Computer Vision and Pattern Recognition (CVPR), 2024.

> <span style="color:#F59E0B"><strong>Para. 50[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 51:</strong></span> C. J. van Rijsbergen. Information Retrieval. Butterworths, London, 2nd edition, 1979.

> <span style="color:#F59E0B"><strong>Para. 51[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 52:</strong></span> Bram Wallace, Meihua Dang, Rafael Rafailov, Linqi Zhou, Aaron Lou, Senthil Purushwalkam, Stefano Ermon, Caiming Xiong, Shafiq Joty, and Nikhil Naik. Diffusion model alignment using direct preference optimization. In Conference on Computer Vision and Pattern Recognition (CVPR), 2024.

> <span style="color:#F59E0B"><strong>Para. 52[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 53:</strong></span> Linqing Wang, Ximing Xing, Yiji Cheng, Zhiyuan Zhao, Donghao Li, Tiankai Hang, Jiale Tao, Qixun Wang, Ruihuang Li, et al. PromptEnhancer: A simple approach to enhance text-to-image models via chain-of-thought prompt rewriting. arXiv preprint arXiv:2509.04545, 2025a.

> <span style="color:#F59E0B"><strong>Para. 53[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 54:</strong></span> Xinran Wang, Muxi Diao, Yuanzhi Liu, Chunyu Wang, Kongming Liang, Zhanyu Ma, and Jun Guo. Harnessing caption detailness for data-efficient text-to-image generation. arXiv preprint arXiv:2505.15172, 2025b.

> <span style="color:#F59E0B"><strong>Para. 54[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 55:</strong></span> Xinyu Wei, Jinrui Zhang, Zeqing Wang, Hongyang Wei, Zhen Guo, Bairui Li, and Lei Zhang. TIIF-Bench: How does your T2I model follow your instructions? arXiv preprint arXiv:2506.02161, 2025.

> <span style="color:#F59E0B"><strong>Para. 55[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 56:</strong></span> Chenfei Wu, Jiahao Li, Jingren Zhou, Junyang Lin, Kaiyuan Gao, Kun Yan, Sheng-ming Yin, Shuai Bai, Xiao Xu, et al. Qwen-Image technical report. arXiv preprint arXiv:2508.02324, 2025a.

> <span style="color:#F59E0B"><strong>Para. 56[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 57:</strong></span> Chenyuan Wu, Pengfei Zheng, Ruiran Yan, Shitao Xiao, Xin Luo, Yueze Wang, Wanli Li, Xiyan Jiang, Yexin Liu, et al. OmniGen2: Towards instruction-aligned multimodal generation. arXiv preprint arXiv:2506.18871, 2025b.

> <span style="color:#F59E0B"><strong>Para. 57[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 58:</strong></span> Jiazheng Xu, Xiao Liu, Yuchen Wu, Yuxuan Tong, Qinkai Li, Ming Ding, Jie Tang, and Yuxiao Dong. ImageReward: Learning and evaluating human preferences for text-to-image generation. In Advances in Neural Information Processing Systems (NeurIPS), 2023.

> <span style="color:#F59E0B"><strong>Para. 58[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 59:</strong></span> Lihe Yang, Bingyi Kang, Zilong Huang, Zhen Zhao, Xiaogang Xu, Jiashi Feng, and Hengshuang Zhao. Depth anything V2. In Advances in Neural Information Processing Systems (NeurIPS), 2024a.

> <span style="color:#F59E0B"><strong>Para. 59[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 60:</strong></span> Ling Yang, Zhaochen Yu, Chenlin Meng, Minkai Xu, Stefano Ermon, and Bin Cui. Mastering text-to-image diffusion: Recaptioning, planning, and generating with multimodal LLMs. In International Conference on Machine Learning (ICML), 2024b.

> <span style="color:#F59E0B"><strong>Para. 60[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 61:</strong></span> Zhichao Yang, Tianjiao Gu, Jianjie Wang, Feiyu Lin, et al. LongT2IBench: A benchmark for evaluating long text-to-image generation with graph-structured annotations. In AAAI Conference on Artificial Intelligence, 2026.

> <span style="color:#F59E0B"><strong>Para. 61[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 62:</strong></span> Junyan Ye, Dongzhi Jiang, Zihao Wang, Leqi Zhu, Zhenghao Hu, Zilong Huang, Jun He, Zhiyuan Yan, Jinghua Yu, Hongsheng Li, Conghui He, and Weijia Li. Echo-4o: Harnessing the power of GPT-4o synthetic images for improved image generation. arXiv preprint arXiv:2508.09987, 2025.

> <span style="color:#F59E0B"><strong>Para. 62[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 63:</strong></span> Beichen Zhang, Pan Zhang, Xiaoyi Dong, Yuhang Zang, and Jiaqi Wang. Long-CLIP: Unlocking the long-text capability of CLIP. In European Conference on Computer Vision (ECCV), 2024.

> <span style="color:#F59E0B"><strong>Para. 63[CN]:</strong></span> （参考文献按原文保留。）

> <span style="color:#3B82F6"><strong>Para. 64:</strong></span> Wendi Zheng, Jiayan Teng, Zhuoyi Yang, Weihan Wang, Jidong Chen, Xiaotao Gu, Yuxiao Dong, Ming Ding, and Jie Tang. CogView3: Finer and faster text-to-image generation via relay diffusion. In European Conference on Computer Vision (ECCV), 2024.

> <span style="color:#F59E0B"><strong>Para. 64[CN]:</strong></span> （参考文献按原文保留。）


# Appendix — 追加材料（页码 24–36）：A–C

## Contents / 目录

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **A Grounded Perplexity Gain: measurement details** — A.1 Default scoring protocol; A.2 GPG robustness across judges; A.3 Full 15-setting data; A.4 Monotonicity analysis; A.5 Fit sensitivity across settings and training budgets; A.6 Mutual-information motivation and the empirical status of the relations. **B Effective Detailness: validation details** — B.1 Image-grounded source extraction; B.2 Why precision-weighted $F_{0.5}$?; B.3 Shared-UID resampling sensitivity; B.4 Robustness across source extractors. **C Structured-prompt schema and implementation details** — C.1 Structured-prompt schema; C.2 Annotation pipeline; C.3 Diffusion-backbone training; C.4 Schema field ablation; C.5 Prompter training; C.6 Inference and the agentic loop; C.7 External dependencies and licenses.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **A 基于图像的困惑度增益：测量细节**——A.1 默认评分协议；A.2 GPG 在不同评审模型间的鲁棒性；A.3 完整的 15 项设定数据；A.4 单调性分析；A.5 跨设定与训练预算的拟合敏感性；A.6 互信息动机及这些关系的经验性地位。**B 有效细致度：验证细节**——B.1 以图像为依据的源信息提取；B.2 为什么采用精确率加权的 $F_{0.5}$？；B.3 共享 UID 的重采样敏感性；B.4 跨源信息提取器的鲁棒性。**C 结构化提示词模式与实现细节**——C.1 结构化提示词模式；C.2 标注流水线；C.3 扩散主干训练；C.4 模式字段消融；C.5 提示器训练；C.6 推理与智能体循环；C.7 外部依赖与许可证。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The Contents additionally lists **D Additional benchmark results** (D.1 DPG-Bench per-category breakdown; D.2 GenEval per-skill breakdown; D.3 WISE per-category breakdown; D.4 T2I-CoReBench per-category breakdown), **E System prompts** (E.1 Cold-start teacher system prompt; E.2 Aesthetic judge system prompt; E.3 Cold-start filtering system prompts; E.4 VLM-as-judge system prompts; E.5 GSB pairwise preference protocol), **F Prompts for main-paper figures** (F.1 Figure 2 — Gallery; F.2 Figure 2 (bottom) — Zero-shot SP editing; F.3 Figure 3 — Teaser; F.4 Figure 11 — SOTA qualitative comparison; F.5 Figure 13 — Prompter training-stage progression; F.6 Figure 12 — SFT vs. no-SFT; F.7 Figure 15 — Case types the agentic loop resolves; F.8 Figure 20 — prompter comparison prompts; F.9 Figures 23–24 — SOTA LLM as prompter), and **G Additional qualitative examples** (G.1 Prompter comparison: prompter scale × training; G.2 General-purpose LMs as prompters). The exact system prompts begin in Appendix E and are outside this fragment.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 目录还列出 **D 附加基准结果**（D.1 DPG-Bench 分类别分解；D.2 GenEval 分技能分解；D.3 WISE 分类别分解；D.4 T2I-CoReBench 分类别分解）、**E 系统提示词**（E.1 冷启动教师系统提示词；E.2 美学评审系统提示词；E.3 冷启动过滤系统提示词；E.4 将 VLM 作为评审器的系统提示词；E.5 GSB 成对偏好协议）、**F 主论文图的提示词**（F.1 图 2——图集；F.2 图 2（下）——零样本 SP 编辑；F.3 图 3——预告图；F.4 图 11——SOTA 定性比较；F.5 图 13——提示器训练阶段进程；F.6 图 12——SFT 与无 SFT；F.7 图 15——智能体循环能解决的案例类型；F.8 图 20——提示器比较提示词；F.9 图 23–24——作为提示器的 SOTA LLM），以及 **G 附加定性示例**（G.1 提示器比较：提示器规模 × 训练；G.2 作为提示器的通用 LLM）。精确的系统提示词从附录 E 开始，不属于本片段。

# A Grounded Perplexity Gain: measurement details / 基于图像的困惑度增益：测量细节

## A.1 Default scoring protocol / 默认评分协议

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> All headline GPG scores use Qwen3.5-397B-A17B frozen as the VLM judge. Images are resized so that the longer side is 1024 pixels with aspect ratio preserved. Before either pass, captions are mapped to a deterministic scored sequence. For SPs, canonicalization removes the global metadata keys `atmosphere`, `lighting`, `style`, and `photography`, including its `layout`, `shot_type`, `camera_angle`, and `lens_and_effect` subfields. NL captions retain their text, with template-only spans marked separately. The image-conditioned and no-image passes then use the same conversation template and canonical sequence; the latter replaces the image with an empty image slot. All tokens in that sequence remain in the autoregressive context in both passes. The content mask excludes JSON syntax, stylistic boilerplate, and NL template-only positions only from the accumulated GPG sum. The judge, preprocessing, and template are fixed across all caption conditions, so comparisons vary only the caption content presented for scoring. The canonicalization and content-mask recipe was finalized during metric development on the controlled BAGEL sweep and then frozen. Consequently, the headline GPG–loss relation is a calibration for this fixed recipe, not an independent validation of these scoring choices; applying it to new caption families requires retaining the same recipe or recalibrating it once.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 所有主结果中的 GPG 分数均使用冻结的 Qwen3.5-397B-A17B 作为 VLM 评审器。图像在保持纵横比的前提下缩放，使较长边为 1024 像素。在任一前向过程之前，先将说明文字映射为一个确定性的待评分序列。对于 SP，规范化会移除全局元数据键 `atmosphere`、`lighting`、`style` 和 `photography`，包括其 `layout`、`shot_type`、`camera_angle` 及 `lens_and_effect` 子字段。NL 说明文字保留原文，但会单独标记仅属于模板的片段。随后，有图像和无图像的前向过程使用相同的对话模板和规范序列；后者以一个空图像槽替换图像。在两种过程里，该序列中的所有 token 都保留在自回归上下文中。内容掩码仅将 JSON 语法、风格化套话和 NL 中仅属于模板的位置排除在累积 GPG 求和之外。评审器、预处理和模板在所有说明文字条件间固定，因此比较中变化的只有用于评分的说明文字内容。规范化和内容掩码方案在受控 BAGEL 扫描上的度量开发期间定稿，随后被冻结。因此，主结果的 GPG–损失关系是针对这一固定方案的校准，而不是对这些评分选择的独立验证；将其用于新的说明文字族时，必须保持该方案不变，或重新校准一次。

## A.2 GPG robustness across judges / GPG 在不同评审模型间的鲁棒性

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> GPG depends on the complete judge interface—the VLM, tokenizer, conversation template, image processor, and coordinate convention—rather than on the likelihood query alone; we hold that interface fixed for every headline comparison. Our default judge is Qwen3.5-397B-A17B, chosen because its normalized bbox convention is directly compatible with the caption format’s 0–999 coordinates, avoiding an additional coordinate conversion. To verify that the linear scaling property (Eq. (3)) is not specific to this judge, we recompute GPG on a held-out pool of 1,000 paired images across the scaling-property cells under six additional VL judges—spanning the Qwen2-VL / Qwen2.5-VL / Qwen3-VL / Qwen3.5-MoE lineage plus a cross-family judge (InternVL3-8B)—and refit the linear relation on each. Table 6 reports the resulting cross-judge comparison. Every judge that grounds the caption’s spatial vocabulary gives a strong negative fit ($r$ from −0.91 to −0.99, within ±0.08 of the main fit’s −0.984), and their per-cell GPG rankings agree at Spearman $\rho \geq 0.86$ (identical top and bottom cells). Across the fully evaluated Qwen-family judges, $R^2$ remains between 0.93 and 0.97; the 122B judge reaches 0.99 on the six available cells, but this partial-cell fit is not directly comparable to the full-cell fits (Figure 16). The robustness conclusion is therefore agreement across judges supplied with a compatible coordinate representation, not a monotonic law in judge size; we use the largest available judge for the headline measurement and compare its ordering with smaller and cross-family alternatives. The lone exception is instructive rather than a counterexample: without a bbox-format adapter, Qwen2.5-VL-7B cannot parse our 0–999 `<bbox>` tokens and inverts the ordering ($r = +0.23$); supplying the adapter (`-qwen-native-bbox`, which maps to its native pixel-space coordinates) restores $r = -0.97$. GPG therefore remains judge-dependent, but its configuration ordering is stable across the tested judges once each can read the caption’s spatial representation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> GPG 依赖于完整的评审器接口——VLM、分词器、对话模板、图像处理器和坐标约定——而非仅依赖似然查询；对每一项主结果比较，我们都固定该接口。默认评审器为 Qwen3.5-397B-A17B，选择它是因为其归一化 bbox 约定与说明文字格式中的 0–999 坐标直接兼容，无需额外坐标转换。为验证线性缩放性质（式 (3)）并非该评审器所特有，我们在一个保留的 1,000 张配对图像池上，针对缩放性质的各单元，在另外六个 VL 评审器下重新计算 GPG——覆盖 Qwen2-VL / Qwen2.5-VL / Qwen3-VL / Qwen3.5-MoE 谱系，外加跨家族评审器 InternVL3-8B——并分别重新拟合线性关系。表 6 给出了由此得到的跨评审器比较。每个能够根据说明文字的空间词汇进行定位的评审器都给出强负拟合（$r$ 从 −0.91 到 −0.99，距主拟合的 −0.984 不超过 ±0.08），且其各单元 GPG 排序在 Spearman $\rho \geq 0.86$ 时一致（最高和最低单元相同）。对于完成全面评估的 Qwen 家族评审器，$R^2$ 保持在 0.93 至 0.97；122B 评审器在六个可用单元上达到 0.99，但这一部分单元拟合不能直接与完整单元拟合相比（图 16）。因此，鲁棒性结论是：具备兼容坐标表示的评审器之间存在一致性，而非评审器尺寸的单调规律；我们以可用的最大评审器获得主测量，并将其排序与更小及跨家族的替代者比较。唯一的例外具有启发性而不是反例：没有 bbox 格式适配器时，Qwen2.5-VL-7B 无法解析我们的 0–999 `<bbox>` token，排序会反转（$r = +0.23$）；加入适配器（`-qwen-native-bbox`，将其映射到原生的像素空间坐标）后，$r = -0.97$。因此，GPG 仍依赖评审器，但一旦每个评审器都能够读取说明文字的空间表示，其配置排序在所测试的评审器间是稳定的。

### Figure 16. GPG is robust across compatible judges / GPG 在兼容的评审器间具有鲁棒性

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Figure 16:** **GPG is robust across compatible judges.** (a) GPG → MSE fits with GPG min–max normalized per judge. (b) Fit quality versus judge size; the 122B point uses only six cells and is shown separately from the full-cell fits. InternVL3-8B is the cross-family check.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 16：** **GPG 在兼容的评审器间具有鲁棒性。** (a) 对每个评审器分别进行 GPG 最小–最大归一化后的 GPG → MSE 拟合。(b) 拟合质量随评审器尺寸的变化；122B 点仅使用六个单元，并与完整单元拟合分开显示。InternVL3-8B 是跨家族检查。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Table 6: GPG fit quality across alternative judges.** We refit the GPG → MSE relation under each judge on a held-out 1,000-image robustness pool; the selected main judge (bold) uses the full 30k-UID pool. Qwen2.5-VL-7B reports raw / bbox-adapted scores; see text for the inverted raw case.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **表 6：不同替代评审器下的 GPG 拟合质量。** 我们在一个保留的 1,000 图像鲁棒性池上，针对每个评审器重新拟合 GPG → MSE 关系；选定的主评审器（粗体）使用完整的 30k-UID 池。Qwen2.5-VL-7B 报告原始 / bbox 适配后的分数；反向的原始情形见正文。

| Judge model | Size | Pearson $r$ | $R^2$ | Notes |
|---|---:|---:|---:|---|
| *Robustness sweep (held-out 1,000-image pool)* | | | | |
| Qwen2-VL-7B | 7B | −0.96 | 0.93 | Oldest Qwen-VL; narrower GPG range |
| Qwen3-VL-8B | 8B | −0.99 | 0.97 | Normalized bbox convention compatible with caption format |
| Qwen3.5-35B-A3B | 35B | −0.98 | 0.97 | `no_bbox` cell is 3.3 nats higher |
| Qwen3.5-122B-A10B | 122B | −0.996 | 0.99 | Partial fit (6 of 15 cells); not directly comparable |
| InternVL3-8B | 8B | −0.91 | 0.83 | Cross-family; confirms not Qwen-specific |
| Qwen2.5-VL-7B | 7B | +0.23 / −0.97 | 0.05 / 0.94 | Raw / with `-qwen-native-bbox` (see text) |
| **Qwen3.5-397B-A17B** | **397B** | **−0.98** | **0.97** | Selected (main); full 30k-UID pool |

## A.3 Full 15-setting data / 完整的 15 项设定数据

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Table 7 reports the complete per-setting GPG, ED, and converged diffusion loss underlying Eqs. (3) and (4). All settings share the same 30,000 paired image UIDs for both caption-side measurements. GPG uses Qwen3.5-397B-A17B with the content-mask and canonicalize-JSON recipe of Appendix A.1, while ED follows the extraction and matching protocol of Appendix B; MSE is measured at the unified budget of $2.84\times10^{10}$ cumulative image tokens reached by every run.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 表 7 报告了构成式 (3) 和 (4) 基础的、每项设定完整的 GPG、ED 和收敛扩散损失。所有设定在两种说明文字侧测量中共享相同的 30,000 个配对图像 UID。GPG 使用 Qwen3.5-397B-A17B，以及附录 A.1 的内容掩码和 JSON 规范化方案；ED 遵循附录 B 的提取和匹配协议；MSE 在每次运行均达到的统一预算 $2.84\times10^{10}$ 个累计图像 token 处测量。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Table 7: Full 15-setting scaling-property data, sorted by GPG.** The full-schema baseline of the ablation suite coincides with Structured L10 and is counted once.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **表 7：按 GPG 排序的完整 15 项缩放性质数据。** 消融套件的完整模式基线与 Structured L10 重合，因此只计一次。

| Kind / 类型 | Level / 层级 | GPG | ED | MSE |
|---|---:|---:|---:|---:|
| Dense (NL) | L6 | 106.3 | 0.759 | 0.44523 |
| Dense (NL) | L8 | 110.1 | 0.751 | 0.44542 |
| Structured | L5 | 111.6 | 0.749 | 0.44664 |
| Dense (NL) | L10 | 112.5 | 0.754 | 0.44536 |
| Structured | L6 | 128.3 | 0.759 | 0.44384 |
| Structured | L7 | 141.5 | 0.772 | 0.44275 |
| Spatial (coarse, 3×3) | L10 | 151.0 | 0.778 | 0.44293 |
| Spatial (fine, 5×5) | L10 | 152.2 | 0.785 | 0.44205 |
| Spatial (finer, 9×9) | L10 | 154.4 | 0.787 | 0.44093 |
| Structured | L8 | 164.8 | 0.793 | 0.44074 |
| Abl: −scene | L10 | 168.5 | 0.799 | 0.44052 |
| Structured | L9 | 191.8 | 0.819 | 0.43843 |
| Abl: −bbox | L10 | 204.7 | 0.807 | 0.43843 |
| Abl: −relationships | L10 | 207.2 | 0.808 | 0.43706 |
| Structured | L10 | 210.5 | 0.833 | 0.43699 |

## A.4 Monotonicity analysis / 单调性分析

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Sorted by GPG, MSE decreases overall across the 15 settings, with a few small local reversals. Their total magnitude is approximately 0.0016 MSE units, of which approximately 0.0012 comes from structured L5 relative to the nearby NL settings; we report this reversal descriptively rather than assigning it to a specific cause. The remaining violations are $|\Delta\mathrm{MSE}| \leq 2\times10^{-4}$, the same order as trailing-window read-out variation, so we do not assign them to a specific cause.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 按 GPG 排序后，MSE 在这 15 项设定间总体下降，但存在少数小的局部反转。其总幅度约为 0.0016 MSE 单位，其中约 0.0012 来自相对于相邻 NL 设定的 structured L5；我们仅描述性地报告该反转，而不将其归因于特定原因。其余违例为 $|\Delta\mathrm{MSE}| \leq 2\times10^{-4}$，与尾部窗口读数变动处于同一数量级，因此也不将其归因于特定原因。

## A.5 Fit sensitivity across settings and training budgets / 跨设定与训练预算的拟合敏感性

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Figure 17 shows how the fit correlations change when the 15 designed sweep settings are resampled; the per-level training dynamics for both caption families appear in the main text (Figure 7a–b).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 图 17 显示了对 15 个经设计的扫描设定进行重采样时，拟合相关性如何变化；两种说明文字族逐层级的训练动力学见正文（图 7a–b）。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Uncertainty scope.** Each setting is trained once. The analyses below quantify three operational sensitivities: resampling the deliberately designed sweep settings, refitting the same training trajectories at matched budget cuts, and measuring local variation within their trailing windows. They are not population confidence intervals, independent training replications, or estimates of seed-level optimization uncertainty.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **不确定性的范围。** 每项设定仅训练一次。以下分析量化三种操作层面的敏感性：对刻意设计的扫描设定重采样；在匹配的预算截点处重新拟合同一训练轨迹；以及测量其尾部窗口内的局部变化。它们不是总体置信区间、独立训练重复实验，也不是种子层面优化不确定性的估计。

### Figure 17. Sensitivity of the scaling-property fit to resampling sweep settings / 缩放性质拟合对重采样扫描设定的敏感性

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Figure 17:** **Sensitivity of the scaling-property fit to resampling sweep settings.** Over $B = 2{,}000$ resamples of the 15 designed settings, the distributions of fit magnitude have mean±SD $|r| = 0.984 \pm 0.008$ for GPG and $|r| = 0.973 \pm 0.012$ for ED.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **图 17：** **缩放性质拟合对重采样扫描设定的敏感性。** 在对 15 个设计设定进行的 $B = 2{,}000$ 次重采样中，拟合幅值分布对 GPG 的均值±标准差为 $|r| = 0.984 \pm 0.008$，对 ED 为 $|r| = 0.973 \pm 0.012$。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Read-out conventions for the budget refits.** The budget refits of Figure 18 use the twelve settings whose full training curves were exported: six structured levels, three natural-language levels, and the three field ablations with measured GPG and ED; the three spatial variants were logged only at the final budget. The read-out at each cut is the mean training MSE over the trailing 5% of tokens before the cut; the two runs that restarted mid-training (L5, L9) have their token axes corrected for the restart’s token-counter reset. GPG and ED are caption-side quantities and do not vary with budget; at each cut the GPG relation is fit linearly and the ED relation in log–log space, mirroring Eqs. (3) and (4). The curve-based read-out differs slightly from the per-setting converged values behind the headline fits, and the final-cut coefficients remain close to them.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **预算重拟合的读数约定。** 图 18 的预算重拟合使用导出了完整训练曲线的 12 项设定：6 个结构化层级、3 个自然语言层级，以及 3 个测量了 GPG 和 ED 的字段消融；3 个空间变体仅在最终预算处被记录。每个截点的读数是在截点前 5% token 尾部窗口上的平均训练 MSE；两次在训练中途重启的运行（L5、L9）已针对重启导致的 token 计数器重置校正其 token 轴。GPG 和 ED 是说明文字侧的量，不随预算改变；每个截点处均线性拟合 GPG 关系，并在对数–对数空间拟合 ED 关系，对应式 (3) 和 (4)。基于曲线的读数与主拟合背后每项设定的收敛值略有不同，但最终截点的系数仍与它们接近。

### Figure 18. The scaling properties persist across training budgets / 缩放性质跨训练预算持续成立

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Figure 18:** **The scaling properties persist across training budgets.** Refitting the same trajectories at six matched budget cuts preserves both the linear GPG relation and the ED power law; the fitted slope and exponent steepen mildly as training proceeds.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **图 18：** **缩放性质跨训练预算持续成立。** 在 6 个匹配的预算截点重新拟合同一批轨迹，仍保留线性 GPG 关系和 ED 幂律；随着训练推进，所拟合的斜率和指数会轻微变陡。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Within-trajectory read-out variation.** Splitting each observed trajectory’s trailing window into five disjoint blocks, the standard deviation of block means spans $1.0$–$5.0 \times 10^{-4}$ across the twelve settings (median $3.5 \times 10^{-4}$). This scale is comparable to the residuals of both fits: $\sigma_{\mathrm{resid}} \approx 6 \times 10^{-4}$ for GPG and $7.8 \times 10^{-4}$ for ED. These values contextualize the residual scale but do not decompose it into lack-of-fit and run-level optimization variability.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **轨迹内读数变动。** 将每条观测轨迹的尾部窗口划分为 5 个互不相交的块，12 项设定中块均值的标准差范围为 $1.0$–$5.0 \times 10^{-4}$（中位数 $3.5 \times 10^{-4}$）。这一尺度与两种拟合的残差相当：GPG 的 $\sigma_{\mathrm{resid}} \approx 6 \times 10^{-4}$，ED 的为 $7.8 \times 10^{-4}$。这些数值为残差尺度提供了背景，但并未将其分解为拟合不足和运行层面优化变异。

## A.6 Mutual-information motivation and the empirical status of the relations / 互信息动机及这些关系的经验性地位

$$H(I \mid Y) = H(I) - I(I;Y)$$

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For image and caption random variables $I$ and $Y$, the identity $H(I \mid Y) = H(I) − I(I; Y)$ states that caption–image mutual information reduces uncertainty about the image. This intuition motivates asking whether captions with more image-grounded information are associated with a lower conditional training objective. It does not, however, derive the form of that association in our experiments. GPG is an operational, judge-dependent estimate rather than the dataset mutual information; the converged flow-matching velocity MSE is not measured in nats; and the entropy identity alone neither makes that objective a conditional-likelihood bound nor implies a linear GPG–MSE relation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 对图像和说明文字随机变量 $I$ 与 $Y$，恒等式 $H(I \mid Y) = H(I) − I(I; Y)$ 表明，说明文字–图像互信息会降低对图像的不确定性。这一直觉促使我们询问：包含更多基于图像的信息的说明文字，是否与较低的条件训练目标相关。然而，它并不能推出我们实验中该关联的具体形式。GPG 是一种操作性的、依赖评审器的估计，而不是数据集互信息；收敛的流匹配速度 MSE 不以 nat 为单位测量；并且熵恒等式本身既不会使该目标成为条件似然界，也不意味着线性的 GPG–MSE 关系。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Equation (3) is therefore an empirical, recipe-specific calibration rather than a theorem. Its fitted slope has no universal information-theoretic interpretation: it depends on the judge, caption construction, model, objective, optimization, and training budget held fixed in the sweep. The empirical result is instead that GPG measured by a frozen VLM tracks the converged loss of a separately trained diffuser across the tested caption settings. ED provides a complementary check: despite using no token probabilities, it closely agrees with the GPG ordering ($\rho_{\mathrm{Spearman}} = 0.96$) and follows its own negative power-law trend (Eq. (4)). Residuals from either fit should likewise be read as deviations from this calibration, not as direct estimates of information that the diffuser fails to exploit.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 因此，式 (3) 是一种经验性的、特定方案下的校准，而非定理。其拟合斜率没有普适的信息论解释：它取决于扫描中固定的评审器、说明文字构建方式、模型、目标、优化和训练预算。经验结果实际上是：冻结 VLM 测得的 GPG 在被测试的说明文字设定间追踪了独立训练的扩散器之收敛损失。ED 提供互补检查：尽管未使用 token 概率，它与 GPG 排序高度一致（$\rho_{\mathrm{Spearman}} = 0.96$），且遵循自己的负幂律趋势（式 (4)）。任一拟合的残差也应被视为相对于此校准的偏离，而不应视为扩散器未能利用的信息之直接估计。

# B Effective Detailness: validation details / 有效细致度：验证细节

## B.1 Image-grounded source extraction / 以图像为依据的源信息提取

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The image-grounded source set for ED is obtained by one offline Gemini 3 Pro call per image, prompted to enumerate object–attribute–relationship–grounding (OARG) tuples. The extractor sees only the image and is asked for 80–150 atomic tuples; it returns a mean of 102 tuples over the shared 30,000-image ED pool. For each caption condition, GPT-5.4 independently extracts caption-side OARG tuples, and a separate GPT-5.4 call performs symmetric paraphrase-tolerant matching against the cached source tuples. For each valid image–caption pair, $P_A$ is the fraction of caption-side attribute tuples supported by the image source, and $R_A$ is the fraction of image-side attribute tuples covered by the caption. The pair-level score is $F_{0.5}(P_A,R_A)$; pairs for which either side contains no attribute tuple are skipped, and the degenerate $P_A = R_A = 0$ case is assigned zero. A caption configuration’s ED is the two-sided 10% trimmed mean of its pair-level scores: after sorting, we drop $\lfloor0.1n\rfloor$ values from each tail and average the remainder. Only attributes enter the reported score; object, relation, and grounding tuples provide entity context for extraction and matching. All image-side sources, caption-side tuples, and match masks are computed once and cached.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> ED 的图像依据源集合通过每张图像一次离线 Gemini 3 Pro 调用获得，提示该模型枚举对象–属性–关系–落地（object–attribute–relationship–grounding, OARG）元组。提取器只看图像，并被要求生成 80–150 个原子元组；在共享的 30,000 图像 ED 池上，平均返回 102 个元组。对于每个说明文字条件，GPT-5.4 独立提取说明文字侧 OARG 元组，另一次 GPT-5.4 调用则针对缓存的源元组执行对称的、容忍释义的匹配。对每个有效图像–说明文字对，$P_A$ 是获图像源支持的说明文字侧属性元组比例，$R_A$ 是被说明文字覆盖的图像侧属性元组比例。对级分数为 $F_{0.5}(P_A,R_A)$；任一侧不含属性元组的配对会被跳过，退化情形 $P_A = R_A = 0$ 被赋值为零。一个说明文字配置的 ED 是其对级分数的双侧 10% 截尾均值：排序后，从两端各丢弃 $\lfloor0.1n\rfloor$ 个值，并平均余下值。只有属性进入报告分数；对象、关系和落地元组为提取与匹配提供实体上下文。所有图像侧源、说明文字侧元组和匹配掩码均仅计算一次并缓存。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Table 8: Sensitivity to the precision–recall weighting in ED** on 30,000 paired images per caption configuration. We replace $F_{0.5}$ by $F_1$ or $F_2$ while keeping the tuple extraction, matching, aggregation, caption configurations, and converged-loss read-out fixed. $r$ and $R^2$ are measured in log–log space; variant MAE fits the three NL and six nested-SP configurations and evaluates the six spatial and field variants excluded from the fit.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **表 8：ED 中精确率–召回率加权的敏感性。** 每个说明文字配置使用 30,000 张配对图像。我们以 $F_1$ 或 $F_2$ 替换 $F_{0.5}$，同时固定元组提取、匹配、聚合、说明文字配置和收敛损失读数。$r$ 和 $R^2$ 在对数–对数空间中测量；变体 MAE 在 3 个 NL 和 6 个嵌套 SP 配置上拟合，并在未纳入拟合的 6 个空间和字段变体上评估。

| $\beta$ | Emphasis / 侧重 | exponent $b$ | Pearson $r$ | $R^2$ | Spearman $\rho$ | variant MAE / 变体 MAE |
|---:|---|---:|---:|---:|---:|---:|
| 0.5 | precision / 精确率 | −0.207 | −0.971 | 0.943 | −0.993 | 0.00081 |
| 1.0 | balanced / 平衡 | −0.098 | −0.736 | 0.541 | −0.729 | 0.00153 |
| 2.0 | recall / 召回率 | −0.050 | −0.559 | 0.313 | −0.607 | 0.00191 |

## B.2 Why precision-weighted $F_{0.5}$? / 为什么采用精确率加权的 $F_{0.5}$？

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The two ED errors have different consequences for conditioning: an unsupported caption attribute supplies contradictory supervision for its paired image, whereas an omitted attribute reduces conditioning bandwidth without introducing a false visual fact. This asymmetry motivates the standard precision-oriented $F_{0.5}$ convention (van Rijsbergen, 1979; Cheng et al., 2024). We selected the precision-oriented aggregation over $F_1$ and $P \cdot R$ during metric development on the controlled BAGEL sweep, then froze $\beta = 0.5$ for every caption family and subsequent analysis. As with the GPG scoring recipe of Appendix A.1, the headline ED–loss relation is therefore a calibration for this fixed choice rather than an independent validation of it. The sensitivity study below varies $\beta$ post hoc to test how strongly the empirical relation depends on this precision-oriented choice.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 两种 ED 误差对条件化具有不同后果：未获支持的说明文字属性为其配对图像提供矛盾的监督，而遗漏的属性会降低条件化带宽，却不会引入错误的视觉事实。这种不对称性促成了标准的精确率导向 $F_{0.5}$ 约定（van Rijsbergen, 1979；Cheng et al., 2024）。在受控 BAGEL 扫描上的度量开发期间，我们选择了精确率导向的聚合，而非 $F_1$ 和 $P \cdot R$，随后将每个说明文字族和所有后续分析中的 $\beta = 0.5$ 冻结。与附录 A.1 的 GPG 评分方案一样，主结果的 ED–损失关系因而是针对这一固定选择的校准，并非它的独立验证。下方敏感性研究事后改变 $\beta$，以测试经验关系对这种精确率导向选择的依赖程度。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The fitted log–log slope remains negative as $\beta$ increases, and the nested SP ladder remains monotonic from L5 to L10 under all three settings. Predictive strength nevertheless falls substantially: $R^2$ decreases from 0.943 for $F_{0.5}$ to 0.313 for $F_2$, while variant MAE more than doubles. Thus the direction of the relation is robust to $\beta$, but the precision-oriented score is markedly more predictive.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 随着 $\beta$ 增大，所拟合的对数–对数斜率保持为负，且在全部三个设定下，嵌套 SP 阶梯从 L5 到 L10 保持单调。然而，预测强度显著下降：$R^2$ 从 $F_{0.5}$ 的 0.943 降至 $F_2$ 的 0.313，而变体 MAE 增加超过一倍。因此，该关系的方向对 $\beta$ 是稳健的，但精确率导向的分数显著更具预测性。

## B.3 Shared-UID resampling sensitivity / 共享 UID 的重采样敏感性

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Conditional resampling analysis.** A shared-UID bootstrap over the 30,000 paired images ($B = 10{,}000$) gives a resampling-distribution mean±SD Spearman $\rho = -0.979 \pm 0.010$ between ED and converged MSE, with central 95% range $[-0.993,-0.957]$. The corresponding ranges are $[-0.978,-0.946]$ for the log–log Pearson correlation and $[-0.220,-0.191]$ for the exponent. These ranges condition on the cached outputs of the image proposer, caption extractor, and matcher; they measure sensitivity to which paired UIDs are included, but do not include API/model stochasticity or training-run uncertainty.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **条件重采样分析。** 在 30,000 张配对图像上进行的共享 UID bootstrap（$B = 10{,}000$）显示，ED 与收敛 MSE 间的重采样分布 Spearman $\rho$ 均值±标准差为 $-0.979 \pm 0.010$，中心 95% 范围为 $[-0.993,-0.957]$。对应的对数–对数 Pearson 相关范围为 $[-0.978,-0.946]$，指数范围为 $[-0.220,-0.191]$。这些范围以图像提议器、说明文字提取器和匹配器的缓存输出为条件；它们测量的是纳入哪些配对 UID 的敏感性，但不包含 API/模型随机性或训练运行不确定性。

## B.4 Robustness across source extractors / 跨源信息提取器的鲁棒性

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> ED’s only image-conditioned step is the offline extraction of attribute tuples from each image. A natural concern is that the resulting per-cell rankings might be an artifact of the specific extractor model. To test this, we re-run the image-side source extraction with two additional vision–language backends—GPT-4o and GPT-5.5 (reasoning)—alongside the default Gemini 3 Pro, each given the same exhaustive-OARG instructions, on a held-out pool of 1,000 paired images (GPT-5.5 on the first 150). Caption extraction and symmetric matching remain fixed at GPT-5.4, so Table 9 isolates the image-source backend. ED proves rank-robust: under every backend ED remains a strong negative predictor of converged MSE ($\rho(\mathrm{ED},\mathrm{MSE})$ from −0.86 to −0.90), the cells keep the same ordering (cross-backend cell-rank $\rho = 0.80$–$0.92$; pairwise per-tuple Cohen $\kappa = 0.75$–$0.77$), and the power-law slope keeps its sign and rough magnitude.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> ED 唯一的图像条件步骤，是从每张图像离线提取属性元组。一个自然担忧是，所得的逐单元排序可能是特定提取器模型的伪影。为测试这一点，我们在一个保留的 1,000 张配对图像池上（GPT-5.5 使用前 150 张），除默认 Gemini 3 Pro 外，采用两个额外视觉–语言后端——GPT-4o 和 GPT-5.5（推理）——重新运行图像侧源提取，且每者都接受相同的穷尽式 OARG 指令。说明文字提取和对称匹配仍固定为 GPT-5.4，因此表 9 隔离了图像源后端。ED 被证明对排序稳健：在每个后端下，ED 都仍是收敛 MSE 的强负向预测器（$\rho(\mathrm{ED},\mathrm{MSE})$ 为 −0.86 至 −0.90），各单元保持相同排序（跨后端单元排序 $\rho = 0.80$–$0.92$；逐元组成对 Cohen $\kappa = 0.75$–$0.77$），且幂律斜率保持其符号和大致量级。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Absolute ED levels, however, are *not* backend-invariant: the intraclass correlation for absolute agreement is only 0.11 (consistency ICC 0.64)—different extractors place the cells on shifted ED scales even while agreeing on their order. We therefore use ED as a *relative ruler* with a single fixed extractor (Gemini 3 Pro) throughout the paper, and compare only rankings and slopes across backends—never absolute ED between extractors.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 然而，ED 的绝对水平*不*具备后端不变性：绝对一致性的组内相关仅为 0.11（一致性 ICC 为 0.64）——不同提取器会将各单元置于发生平移的 ED 尺度上，尽管它们同意排序。因此，整篇论文中我们以单一固定提取器（Gemini 3 Pro）的 ED 作为一个*相对标尺*，跨后端仅比较排序和斜率——绝不比较提取器之间的绝对 ED。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Table 9: ED backend robustness** (held-out 1,000-image pool; GPT-5.5 on $N = 150$). ED remains a negative predictor of converged MSE under every extractor, with stable cell rankings but shifted absolute scales. Cross-backend rank and tuple-agreement statistics are discussed in the text.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **表 9：ED 后端鲁棒性**（保留的 1,000 图像池；GPT-5.5 使用 $N = 150$）。在每种提取器下，ED 均保持为收敛 MSE 的负向预测器，单元排序稳定但绝对尺度发生平移。跨后端排序与元组一致性统计量见正文讨论。

| Extractor / 提取器 | $\rho(\mathrm{ED},\mathrm{MSE})$ | power-law slope $b$ / 幂律斜率 $b$ | cell-rank $\rho$ vs Gemini / 相对 Gemini 的单元排序 $\rho$ |
|---|---:|---:|---:|
| Gemini 3 Pro (reference) | −0.87 | $-0.221 \pm 0.020$ | — |
| GPT-4o | −0.86 | $-0.244 \pm 0.027$ | 0.80 |
| GPT-5.5 (reasoning) | −0.90 | $-0.137 \pm 0.042$ | 0.88 |

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Complete per-setting ED values appear alongside GPG and converged MSE in Table 7. They underlie the power-law fit of Eq. (4); Grid-$k$ denotes verbal locations on a $k\times k$ grid, and the ablation rows mask the named L10 field.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 每项设定的完整 ED 值与 GPG 和收敛 MSE 一起列于表 7。它们构成式 (4) 的幂律拟合基础；Grid-$k$ 表示 $k\times k$ 网格上的语言位置，消融行则掩盖所命名的 L10 字段。

# C Structured-prompt schema and implementation details / 结构化提示词模式与实现细节

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The structured prompt is the central interface of this paper: its definition in §3.1, its construction in §3.3, and the scaling-property evidence in §3.2 depend on both the JSON layout and how its fields are populated from images. This appendix first summarizes the schema (§C.1), then reports the annotation, diffusion, prompter, inference, and dependency details needed to implement the full system. Training covers three model components: the BAGEL and Qwen-Image diffusion backbones, and a rank-128 LoRA (Hu et al., 2021) on Qwen3.5-397B-A17B as the prompter (§3.4, three serial stages: SFT, Cold-start, and RFT). BAGEL is trained once per caption configuration for the scaling-property experiments of §3.2; Qwen-Image is trained once on the structured-prompt corpus (a mixture of SP levels with NL captions) and held fixed across all prompter ablations (§4.2). All trainings use packed sequences, so there is no fixed per-step batch size in samples; the tables below report the packed sequence length and global GPU count from which effective tokens per step can be derived. Stage-by-stage annotation details appear in §C.2, and the degradation levels used in the scaling-property experiments are defined in Table 1.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 结构化提示词是本文的中心接口：其在 §3.1 中的定义、在 §3.3 中的构建，以及 §3.2 中的缩放性质证据，都依赖 JSON 布局及其字段如何从图像中填充。本附录先总结该模式（§C.1），再报告实现完整系统所需的标注、扩散、提示器、推理和依赖细节。训练涉及三个模型组件：BAGEL 和 Qwen-Image 扩散主干，以及作为提示器的、加在 Qwen3.5-397B-A17B 上的 rank-128 LoRA（Hu et al., 2021；§3.4，依序包含 SFT、Cold-start 和 RFT 三个阶段）。针对 §3.2 的缩放性质实验，BAGEL 每种说明文字配置训练一次；Qwen-Image 在结构化提示词语料（SP 层级与 NL 说明文字的混合）上训练一次，并在所有提示器消融中保持固定（§4.2）。所有训练均采用打包序列，因此没有按样本计的固定每步批量大小；下表报告打包序列长度和全局 GPU 数量，据此可推导每步有效 token。逐阶段标注细节见 §C.2，缩放性质实验所用的退化层级定义于表 1。

## C.1 Structured-prompt schema / 结构化提示词模式

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Table 10 summarizes the structured-prompt schema. Three required fields define the scene skeleton—the overall intent, the macro scene, and the list of elements. Five optional fields add cross-element relationships (`relationships`) and global controls (`atmosphere`, `photography`, `style`, `lighting`). The prompter additionally emits a leading `ratio` control field. At inference, the generation wrapper uses it to select the output canvas and removes it before the remaining SP is passed to the diffuser. Image-to-SP annotation omits `ratio`, since the source image already fixes the canvas. The schema is extensible: the elements list uses dynamic per-element keys, so attributes and actions can be added without schema changes.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 表 10 总结了结构化提示词模式。3 个必需字段定义场景骨架——总体意图、宏观场景和元素列表。5 个可选字段增加跨元素关系（`relationships`）和全局控制（`atmosphere`、`photography`、`style`、`lighting`）。提示器还会输出一个前置的 `ratio` 控制字段。推理时，生成包装器用它选择输出画布，并在将其余 SP 传给扩散器前移除它。图像到 SP 的标注省略 `ratio`，因为源图像已确定画布。该模式可扩展：元素列表使用动态的逐元素键，因此可在不改变模式的情况下加入属性和动作。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Table 10: Structured-prompt schema summary.** Required fields define the scene skeleton; optional fields add cross-element relations and global controls. $^*$`ratio` is an inference-only control emitted by the prompter, consumed by the generation wrapper, and removed before diffusion conditioning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **表 10：结构化提示词模式摘要。** 必需字段定义场景骨架；可选字段增加跨元素关系和全局控制。$^*$`ratio` 是仅供推理使用的控制字段，由提示器输出、由生成包装器消费，并在扩散条件化之前移除。

| Field / 字段 | Req. / 要求 | Type / 类型 | Description / 描述 |
|---|---|---|---|
| `ratio` | req.$^*$ | string | Output aspect ratio from a fixed menu (e.g. `16:9`); consumed by the inference wrapper and not passed to the diffuser. / 来自固定菜单的输出纵横比（如 `16:9`）；由推理包装器消费，不传给扩散器。 |
| `intent` | req. | string | One high-level sentence describing the whole scene and its key entities/interactions; when it conflicts with a specific field, the specific field takes precedence. / 描述整个场景及其关键实体/交互的一句高层级文本；若与具体字段冲突，具体字段优先。 |
| `scene` | req. | object | Macro environment: `setting` (indoor/outdoor, time, weather) and a background `elements` list with the same structure as foreground elements. / 宏观环境：`setting`（室内/室外、时间、天气）以及与前景元素结构相同的背景 `elements` 列表。 |
| `elements` | req. | array | All independently-editable entities. Each has `id`, a concise caption (identity plus the single most salient feature), `position` (language / point / bbox, with bbox coordinates normalized to 0–999 per axis), optional `depth` (0 nearest, 255 farthest), an optional per-element `photography` object, and one named key per visual dimension: attribute keys (`material_and_surface`, `color`, `lighting_interaction`, …) and action keys (`pose`, `gesture`, `expression`, `gaze`, `action`). Raw human keypoints are annotation evidence, not a schema field. / 所有可独立编辑的实体。每个实体有 `id`、简洁说明文字（身份加上最显著的单一特征）、`position`（语言 / 点 / bbox；bbox 坐标各轴归一化到 0–999）、可选的 `depth`（0 最近、255 最远）、可选的逐元素 `photography` 对象，以及每个视觉维度一个命名键：属性键（`material_and_surface`、`color`、`lighting_interaction`、…）和动作键（`pose`、`gesture`、`expression`、`gaze`、`action`）。原始人体关键点是标注证据，不是模式字段。 |
| `relationships` | opt. | array | Textual statements of interaction or spatial relation between entities, each referencing their bounding boxes. / 实体间交互或空间关系的文字陈述，各自引用其边界框。 |
| `atmosphere` | opt. | string | Overall mood, in a few words. / 用几个词概括的总体氛围。 |
| `photography` | opt. | object | Global camera: `layout`, `shot_type`, `camera_angle`, `lens_and_effect`. / 全局相机：`layout`、`shot_type`、`camera_angle`、`lens_and_effect`。 |
| `style` | opt. | string | Overall artistic style, e.g. “photorealistic”. / 总体艺术风格，例如“photorealistic”。 |
| `lighting` | opt. | string | Overall lighting environment and its interaction with the scene. / 总体光照环境及其与场景的交互。 |

## C.2 Annotation pipeline / 标注流水线

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Figure 8 traces the five stages that populate the L10 schema, while Table 10 defines the resulting fields. Every model in the annotation pipeline runs frozen at our inference settings.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 图 8 跟踪填充 L10 模式的 5 个阶段，表 10 定义由此产生的字段。标注流水线中的每个模型均以我们的推理设置冻结运行。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **(1) Global scene understanding.** A VLM (Seed-VL) reads the whole image and emits the high-level `intent`, the global `atmosphere`, `style`, `lighting`, and `photography` fields, and the `scene` block (`setting` and background elements); it also lays out the JSON skeleton—splitting foreground from background and assigning each entity an `id` ordered by compositional importance.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **(1) 全局场景理解。** 一个 VLM（Seed-VL）读取整张图像，输出高层级 `intent`、全局 `atmosphere`、`style`、`lighting` 和 `photography` 字段，以及 `scene` 块（`setting` 与背景元素）；它还布置 JSON 骨架——划分前景和背景，并按构图重要性为每个实体分配 `id`。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **(2) Per-element description.** Each entity is cropped and re-captioned by the VLM into a concise caption plus one named key per visual dimension: attribute keys (`color`, `material`, `surface`) and action keys (`pose`, `gesture`, `expression`, `gaze`). For each person, Sapiens (Khirodkar et al., 2024) predicts 133 keypoints that are rendered as a pose overlay for a downstream VLM pass; the overlay helps resolve body-side orientation and joint geometry, but the raw keypoints are not written into the SP.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **(2) 逐元素描述。** 每个实体被裁剪，再由 VLM 重新描述为一条简洁说明文字及每个视觉维度一个命名键：属性键（`color`、`material`、`surface`）和动作键（`pose`、`gesture`、`expression`、`gaze`）。对每个人，Sapiens（Khirodkar et al., 2024）预测 133 个关键点，并渲染为供下游 VLM 前向使用的姿态叠加层；该叠加层有助于判定身体朝向和关节几何，但原始关键点不会写入 SP。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **(3) Spatial annotation.** DepthAnything V2 (Yang et al., 2024a) supplies relative element depth, quantized from 0 (nearest) to 255 (farthest) when available; otherwise the `depth` field is omitted. SAM 2.1 (Ravi et al., 2024) supplies per-element masks and occlusion cues. Bounding-box, mask, and depth evidence supports geometric relations such as overlap, containment, relative position, and depth order; semantic relations such as support and interaction are inferred during the final VLM reconciliation pass.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **(3) 空间标注。** DepthAnything V2（Yang et al., 2024a）在可用时提供相对元素深度，将其量化为 0（最近）至 255（最远）；否则省略 `depth` 字段。SAM 2.1（Ravi et al., 2024）提供逐元素掩码和遮挡线索。边界框、掩码和深度证据支持重叠、包含、相对位置和深度顺序等几何关系；支撑和交互等语义关系则在最后的 VLM 调和阶段推断。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **(4) Assembly.** A second VLM pass merges the stage-1–3 outputs into a well-formed L10 structured record, constrained by the schema skeleton from stage 1.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **(4) 组装。** 第二次 VLM 前向将阶段 1–3 的输出合并为格式良好的 L10 结构化记录，并受阶段 1 的模式骨架约束。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **(5) Degradation sampling.** Table 1 defines the deterministic field-group masks used to derive the L9→L5 variants. One set of degradations is generated per L10 annotation and reused across all training cells.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **(5) 退化采样。** 表 1 定义了用于得到 L9→L5 变体的确定性字段组掩码。每个 L10 标注生成一组退化，并在全部训练单元中复用。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> **Matched NL controls.** To isolate the structured interface from additional training, the end-to-end NL control uses the same training images, Qwen-Image initialization, diffusion recipe and budget, and matched prompter-training budget as the SP system, while using free-form NL captions throughout. Its prompter uses the same Qwen3.5-397B-A17B base checkpoint, rank-128 LoRA, SFT–Cold-start–RFT sequence, stage-wise data volumes, optimizer schedules, training steps, decoding settings, verifier and privileged-teacher configurations, and checkpoint-selection rule as the SP prompter. Only the intermediate caption representation and corresponding training targets change from structured prompts to free-form NL captions. The NL controls are generated from the same stage-1–3 evidence bundle used to assemble the SPs, not by flattening or compressing the final JSON. For each image, the NL verbalizer receives the global and crop-level VLM descriptions together with the same rendered Sapiens pose overlay, DepthAnything relative-depth evidence, and SAM segmentation and occlusion cues used by the SP pipeline, including intermediate evidence that is not serialized as a separate SP field. It is instructed to preserve the source entity inventory and image-specific facts while expressing them as free-form prose at the target token budget. Across the NL budgets, additional length is introduced through elaboration and connective phrasing rather than access to new annotation evidence. Appendix F.3 gives the exact teaser construction. Aggregate results appear in Table 2, with category-level breakdowns in Appendix D.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> **匹配的 NL 对照。** 为将结构化接口与额外训练隔离，端到端 NL 对照使用与 SP 系统相同的训练图像、Qwen-Image 初始化、扩散方案和预算，以及匹配的提示器训练预算，但全程使用自由形式 NL 说明文字。其提示器使用与 SP 提示器相同的 Qwen3.5-397B-A17B 基础检查点、rank-128 LoRA、SFT–Cold-start–RFT 序列、逐阶段数据量、优化器调度、训练步数、解码设置、验证器和特权教师配置以及检查点选择规则。只有中间说明文字表示及相应训练目标从结构化提示词变为自由形式 NL 说明文字。NL 对照由组装 SP 时所用的相同阶段 1–3 证据包生成，而不是通过展平或压缩最终 JSON。对每张图像，NL 语言化器接收全局和裁剪级的 VLM 描述，以及 SP 流水线使用的相同渲染 Sapiens 姿态叠加层、DepthAnything 相对深度证据及 SAM 分割和遮挡线索，其中包括未被序列化为独立 SP 字段的中间证据。其指令是在目标 token 预算内以自由形式文本表达，同时保留源实体清单和图像特定事实。在各种 NL 预算间，额外长度是通过展开与连接性措辞加入，而不是通过访问新的标注证据加入。附录 F.3 给出精确的预告图构建。汇总结果见表 2，类别级分解见附录 D。

## C.3 Diffusion-backbone training / 扩散主干训练

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Backbones.** We train two backbones: BAGEL (Deng et al., 2025) for the scaling-property fit of §3.2 (one checkpoint per cell) and Qwen-Image-2512 (Wu et al., 2025a) for the promptability sweeps and main results (§3.4, 4.1). BAGEL is a 7B unified model—Qwen2.5-7B with Mixture-of-Transformer-Experts (MoT) layers separating understanding and generation experts, a SigLIP2 vision encoder, and a frozen Flux KL-VAE—initialized from an in-house continued-training (CT) checkpoint (not part of the BAGEL public release); Qwen-Image is initialized from the Qwen-Image-2512 public release (a 60-layer DiT with a frozen Qwen2.5-VL-7B text encoder and KL-VAE). Full hyperparameters are in Tables 11 and 12.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **主干。** 我们训练两个主干：用于 §3.2 缩放性质拟合的 BAGEL（Deng et al., 2025；每个单元一个检查点），以及用于可提示性扫描和主结果的 Qwen-Image-2512（Wu et al., 2025a；§3.4、4.1）。BAGEL 是一个 7B 统一模型——Qwen2.5-7B，配有将理解专家与生成专家分开的 Mixture-of-Transformer-Experts（MoT）层、一个 SigLIP2 视觉编码器和一个冻结的 Flux KL-VAE——从内部持续训练（CT）检查点初始化（不属于 BAGEL 公开发布的一部分）；Qwen-Image 从 Qwen-Image-2512 的公开发布版本初始化（一个 60 层 DiT，带有冻结的 Qwen2.5-VL-7B 文本编码器和 KL-VAE）。完整超参数见表 11 和表 12。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Table 11: BAGEL training setup.** One BAGEL checkpoint is trained per caption condition in the scaling-property sweep (§3.2); the same recipe is used for every cell.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **表 11：BAGEL 训练设置。** 在缩放性质扫描（§3.2）中，每种说明文字条件训练一个 BAGEL 检查点；每个单元均采用相同方案。

| Hyperparameter / 超参数 | Value / 值 |
|---|---|
| Initial checkpoint | BAGEL CT checkpoint (Qwen2.5-7B MoT + SigLIP2 + Flux VAE) |
| Sequence length (packed) | 32,768 |
| Learning rate | $5 \times 10^{-5}$ |
| LR schedule | linear warmup (1k steps), then constant |
| Optimizer | AdamW, $\beta_1 = 0.9$, $\beta_2 = 0.95$, $\epsilon = 10^{-15}$, weight decay 0 |
| Max gradient norm | 1.0 |
| EMA decay | 0.999 |
| Diffusion objective | rectified flow (v-prediction); timestep shift 4.0 |
| Precision | bf16 compute, fp32 optimizer moments |
| GPUs (FSDP `HYBRID_SHARD`) | 192 |
| Effective tokens/step | 6.3M (32,768 × 192) |

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Tokenizer and sequence packing.** BAGEL tokenizes text with the Qwen2.5-7B BPE tokenizer and Qwen-Image with the Qwen2.5-VL tokenizer (152,064-token vocabulary); for diffusion training, each structured record is deterministically serialized in a compact single-quote form (`'` delimiters, minimal separators) to save tokens. Both encode images with a frozen KL-VAE at 8× spatial compression and 16 latent channels—the Flux VAE for BAGEL, a 3D causal KL-VAE for Qwen-Image—followed by 2 × 2 patchification, so each latent token carries $16\cdot2\cdot2=64$ channels and a $1024^2$ image becomes $64\times64=4096$ tokens (16× effective downsample); both train at multi-aspect resolutions (BAGEL 512–1024px, Qwen-Image 768–1536px). Training packs several (image, caption) pairs into one 32,768-token sequence (at most 16,384 tokens per sample) under block-diagonal flex-attention masks that confine each sample to itself, so the effective batch is $32{,}768\times G$ tokens per step ($G = 192$ GPUs for BAGEL, 6.3M tokens/step; $G = 512$ for Qwen-Image, 16.8M tokens/step).

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **分词器和序列打包。** BAGEL 使用 Qwen2.5-7B BPE 分词器对文本分词，Qwen-Image 使用 Qwen2.5-VL 分词器（152,064-token 词表）；对于扩散训练，每条结构化记录均以紧凑的单引号形式（`'` 分隔符、最少分隔符）确定性序列化以节省 token。两者均使用冻结的 KL-VAE 对图像编码，空间压缩为 8×、潜在通道为 16——BAGEL 用 Flux VAE，Qwen-Image 用 3D 因果 KL-VAE——随后进行 2 × 2 分块，因此每个潜在 token 携带 $16\cdot2\cdot2=64$ 个通道，一张 $1024^2$ 图像成为 $64\times64=4096$ 个 token（16× 有效下采样）；二者均在多纵横比分辨率下训练（BAGEL 512–1024px，Qwen-Image 768–1536px）。训练在块对角 flex-attention 掩码下，将多个（图像、说明文字）对打包进一个 32,768-token 序列（每样本至多 16,384 token），掩码将每个样本限制于自身，因此有效批量是每步 $32{,}768\times G$ 个 token（BAGEL：$G = 192$ 个 GPU，6.3M token/步；Qwen-Image：$G = 512$，16.8M token/步）。

$$x_t=(1-t)x_0+t\epsilon, \qquad \epsilon\sim\mathcal{N}(0,I), \qquad v=\epsilon-x_0$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Loss and precision.** Both backbones use a rectified-flow / flow-matching objective: with $x_t=(1-t)x_0+t\epsilon$ and $\epsilon\sim\mathcal{N}(0,I)$, the network predicts the velocity $v=\epsilon-x_0$ under a per-token MSE weighted uniformly across timesteps. Timesteps are sampled and shifted toward noisier states—a fixed shift of 4.0 for BAGEL, a sequence-length-dependent shift for Qwen-Image (0.5 at 256 tokens rising to 0.9 at 8192). Optimization is AdamW ($\beta_1 = 0.9$, $\beta_2 = 0.95$, $\epsilon = 10^{-15}$) with gradient clipping at 1.0 and no accumulation, in bf16 compute with fp32 optimizer moments and gradient checkpointing. Classifier-free guidance is enabled by conditioning dropout during training (text 0.1; reference-image VAE 0.1 for BAGEL, 0.3 for Qwen-Image). BAGEL is a full-parameter finetune of its LLM, vision encoder, and projection/embedding layers (VAE frozen); Qwen-Image is a full finetune of its DiT with both the text encoder and VAE frozen.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **损失与精度。** 两个主干均使用校正流 / 流匹配目标：给定 $x_t=(1-t)x_0+t\epsilon$ 和 $\epsilon\sim\mathcal{N}(0,I)$，网络在跨时间步均匀加权的逐 token MSE 下预测速度 $v=\epsilon-x_0$。时间步经采样并向噪声更强的状态偏移——BAGEL 使用固定 4.0 偏移，Qwen-Image 使用依赖序列长度的偏移（256 token 时为 0.5，8192 时升至 0.9）。优化采用 AdamW（$\beta_1 = 0.9$、$\beta_2 = 0.95$、$\epsilon = 10^{-15}$），梯度裁剪为 1.0、无累积，以 bf16 计算、fp32 优化器矩和梯度检查点进行。训练中通过条件 dropout 启用无分类器引导（文本为 0.1；参考图像 VAE 对 BAGEL 为 0.1、对 Qwen-Image 为 0.3）。BAGEL 对其 LLM、视觉编码器和投影/嵌入层进行全参数微调（VAE 冻结）；Qwen-Image 对其 DiT 做完整微调，文本编码器和 VAE 均冻结。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Table 12: Qwen-Image training setup.** Initialized from the Qwen-Image-2512 public release (Wu et al., 2025a), trained once on the SP/NL caption corpus, then held fixed across prompter ablations (§4.2) and main results (§4.1).

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **表 12：Qwen-Image 训练设置。** 从 Qwen-Image-2512 公开发布版本（Wu et al., 2025a）初始化，在 SP/NL 说明文字语料上训练一次，随后在提示器消融（§4.2）和主结果（§4.1）间保持固定。

| Hyperparameter / 超参数 | Value / 值 |
|---|---|
| Initial checkpoint | Qwen-Image-2512 public release (Wu et al., 2025a) (60-layer DiT; frozen Qwen2.5-VL-7B text encoder + KL-VAE) |
| Sequence length (packed) | 32,768 |
| Learning rate | $1 \times 10^{-4}$ |
| LR schedule | linear warmup (2k steps), then constant |
| Optimizer | AdamW, $\beta_1 = 0.9$, $\beta_2 = 0.95$, $\epsilon = 10^{-15}$, weight decay 0 |
| Max gradient norm | 1.0 |
| EMA decay | 0.9999 |
| Diffusion objective | flow matching (v-prediction); resolution-dependent timestep shift |
| Precision | bf16 compute, fp32 optimizer moments |
| GPUs (FSDP `HYBRID_SHARD`) | 512 |
| Effective tokens/step | 16.8M (32,768 × 512) |

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Cumulative-token budget.** Each BAGEL scaling-property cell is compared at the common cumulative image-token budget of $2.84\times10^{10}$ tokens reached by every run; this defines the matched-budget “converged” MSE used in the fits. Appendix A.5 documents the token-axis correction for two cells (L5 and L9) that were resumed after a counter reset. Qwen-Image is instead trained once for 500,000 steps.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **累计 token 预算。** 每个 BAGEL 缩放性质单元都在每次运行达到的共同累计图像 token 预算 $2.84\times10^{10}$ token 处比较；这定义了拟合中使用的匹配预算“收敛”MSE。附录 A.5 记录了两个在计数器重置后恢复训练的单元（L5 和 L9）的 token 轴校正。Qwen-Image 则训练一次，共 500,000 步。

## C.4 Schema field ablation / 模式字段消融

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We remove one field group at a time from the full L10 schema, retrain BAGEL, and compare all six runs at a common training budget of $2.84 \times 10^{10}$ cumulative image tokens. As Figure 19 shows, scene context is the most influential field group in this controlled setting: removing it reduces GPG by 42 and raises MSE by $35.3 \times 10^{-4}$, a substantially larger loss increase than any other ablation. Removing bounding boxes gives the second-largest increase at $14.4 \times 10^{-4}$, while removing depth, relationships, or atmosphere/lighting changes MSE by at most $1.5 \times 10^{-4}$. The ablation therefore identifies global scene context as the dominant field group for diffusion learning under this setup. This ranks each field group’s marginal loss contribution when present; it does not measure annotation accuracy, which is where the pose, depth, and segmentation experts act. A general VLM’s geometric errors would be serialized as incorrect conditioning, so faithful expert-derived fields matter for correct generation and editing even where a group’s marginal loss contribution is small.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们每次从完整 L10 模式中移除一个字段组，重新训练 BAGEL，并在共同的 $2.84 \times 10^{10}$ 个累计图像 token 训练预算处比较全部 6 次运行。如图 19 所示，在这一受控设置中，场景上下文是最有影响力的字段组：移除它使 GPG 降低 42，并使 MSE 提高 $35.3 \times 10^{-4}$，这比任何其他消融的损失增幅都大得多。移除边界框带来第二大的增幅，为 $14.4 \times 10^{-4}$；移除深度、关系或氛围/光照最多使 MSE 改变 $1.5 \times 10^{-4}$。因此，该消融确定了全局场景上下文是该设置下扩散学习的主导字段组。这是在字段组存在时对其边际损失贡献的排序；它不测量标注准确性，后者是姿态、深度和分割专家发挥作用之处。通用 VLM 的几何误差会被序列化为错误条件，因此，即便字段组的边际损失贡献很小，忠实的专家派生字段对于正确生成和编辑也仍然重要。

### Figure 19. Schema field ablation / 模式字段消融

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Figure 19:** **Schema field ablation (BAGEL backbone).** *Left:* loss curves after removing one L10 field group. *Right:* common-budget MSE is the mean over the trailing 5% of image tokens ending at the shared $2.84 \times 10^{10}$ cut, matching the read-out in Table 7; the table reports changes from L10, with $\Delta\mathrm{MSE}$ in $10^{-4}$ units. Scene context has the largest loss impact, followed by bounding boxes; depth, relationships, and atmosphere/lighting produce smaller changes.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图 19：** **模式字段消融（BAGEL 主干）。** *左：*移除一个 L10 字段组后的损失曲线。*右：*共同预算 MSE 是以共享的 $2.84 \times 10^{10}$ 截点为终点的图像 token 尾部 5% 上的均值，与表 7 的读数一致；表中报告相对于 L10 的变化，$\Delta\mathrm{MSE}$ 的单位为 $10^{-4}$。场景上下文的损失影响最大，边界框次之；深度、关系和氛围/光照产生较小变化。

## C.5 Prompter training / 提示器训练

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The prompter is a rank-128 LoRA adapter on top of Qwen3.5-397B-A17B, trained serially with SFT, Cold-start, and RFT (§3.4). All three stages share the same LoRA topology, and the base Qwen3.5-397B-A17B weights remain frozen throughout. Table 13 summarizes their hyperparameters; the stage definitions follow below.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 提示器是在 Qwen3.5-397B-A17B 之上的 rank-128 LoRA 适配器，依序以 SFT、Cold-start 和 RFT 训练（§3.4）。三个阶段共享相同的 LoRA 拓扑，基础 Qwen3.5-397B-A17B 权重始终冻结。表 13 总结其超参数；阶段定义如下。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Distributed setup.** SFT and Cold-start run under Megatron-LM (via `ms-swift`’s `megatron` entry point) with tensor/pipeline/expert parallelism ($\mathrm{TP} = \mathrm{PP} = \mathrm{EP} = 4$, context parallel disabled), sequence parallelism, a distributed (ZeRO-1-like) optimizer, full uniform gradient checkpointing (one layer), FlashAttention, and bf16 compute with fp32 optimizer moments; sequences are packed with padding-free batching. RFT runs under DeepSpeed ZeRO-3 on a single 8-GPU node with gradient checkpointing, FlashAttention, and the colocated vLLM rollout engine described below.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **分布式设置。** SFT 和 Cold-start 在 Megatron-LM 下运行（通过 `ms-swift` 的 `megatron` 入口），采用张量/流水线/专家并行（$\mathrm{TP} = \mathrm{PP} = \mathrm{EP} = 4$，禁用上下文并行）、序列并行、分布式（类 ZeRO-1）优化器、完全均匀梯度检查点（每层）、FlashAttention，以及带 fp32 优化器矩的 bf16 计算；序列以免填充批处理进行打包。RFT 在单个 8-GPU 节点上以 DeepSpeed ZeRO-3 运行，使用梯度检查点、FlashAttention 和下文所述的同置 vLLM rollout 引擎。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Table 13: Per-stage prompter training setup.** The Qwen3.5-397B-A17B base is frozen and only the rank-128 LoRA is updated. Stage definitions are given in the text.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **表 13：逐阶段提示器训练设置。** Qwen3.5-397B-A17B 基座被冻结，仅更新 rank-128 LoRA。阶段定义见正文。

| Hyperparameter / 超参数 | SFT | Cold-start | RFT |
|---|---:|---:|---:|
| LoRA rank / $\alpha$ | 128 / 256 | 128 / 256 | 128 / 256 |
| LoRA target modules | all linear | all linear | all linear |
| Sequence length (packed) | 20,480 | 32,768 | 49,152 |
| Learning rate | $1\times10^{-5}$ | $1\times10^{-5}$ | $4\times10^{-5}$ |
| LR schedule | cosine, 5% warmup | cosine, 10% warmup | cosine, 5% warmup |
| Weight decay | 0.1 | 0.1 | 0.1 |
| Global batch | 64 | 128 | 32 |

### C.5.1 Training stages / 训练阶段

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Stage 1 — SFT.** The SFT corpus is a token-balanced mixture of ∼333k examples (∼0.97B tokens): roughly one third is the core (user prompt → structured-prompt JSON) task, where the user prompt is the image’s original caption and the target is its image-derived SP from §3.3, plus a reverse image-to-JSON set. The remaining two thirds is reasoning/instruction replay (EN/ZH long chain-of-thought, vision–language reasoning, general dialogue, and a small Qwen3.5 base-identity anchor) included to preserve the base model’s capabilities (DMT-style anti-forgetting). For the prompt → structured-prompt task, the target JSON is treated as one plausible visual completion of the user prompt, not a recoverable ground-truth layout; the stage therefore teaches the distribution of structured completions seen by the diffuser, including non-canonical crops and occlusions, rather than a deterministic prompt-to-layout map. The objective is token-level cross-entropy on the assistant tokens only (system and user prompts masked). Core SFT targets follow the `<think></think>` + JSON interface; their empty thinking block is excluded from the loss, so SFT teaches the SP completion without a reasoning trace while preserving the model’s thinking-toggle convention. We train for one epoch (∼740 steps).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **阶段 1——SFT。** SFT 语料是一个 token 均衡的、约 333k 个示例（约 0.97B token）的混合体：约三分之一是核心（用户提示词 → 结构化提示词 JSON）任务，其中用户提示词为图像的原始说明文字，目标为其来自 §3.3 的图像派生 SP，另加一个反向的图像到 JSON 集。余下三分之二是为保持基础模型能力而加入的推理/指令回放（EN/ZH 长思维链、视觉–语言推理、通用对话和少量 Qwen3.5 基础身份锚点；DMT 风格的抗遗忘）。对提示词 → 结构化提示词任务，目标 JSON 被视为用户提示词的一种可能视觉补全，而非可恢复的真值布局；因此该阶段教授扩散器所见的结构化补全分布，包括非规范裁剪和遮挡，而不是确定性的提示词到布局映射。目标是仅对助手 token 做 token 级交叉熵（系统和用户提示词被掩码）。核心 SFT 目标遵循 `<think></think>` + JSON 接口；空思考块不计入损失，因此 SFT 在不含推理轨迹的情况下教授 SP 补全，同时保留模型的思考开关约定。我们训练一个 epoch（约 740 步）。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Stage 2 — Cold-start.** The final cold-start corpus contains 50,182 unique (original caption → thinking trace → structured JSON) examples selected from 172,208 image-conditioned teacher candidates. Qwen3.5-397B-A17B generates one candidate per example in high-reasoning mode with access to the original caption and paired image, using temperature 1.0, top-p 0.9, and a source-dependent maximum completion length of 16,000–65,536 tokens. Appendix E.1 reproduces its system prompt. The raw teacher response uses an `<analysis>` block for validation; accepted traces are mapped to the student’s `<think>` interface before training. The prompter receives only the original caption during training and inference.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **阶段 2——Cold-start。** 最终冷启动语料含 50,182 个唯一的（原始说明文字 → 思考轨迹 → 结构化 JSON）示例，由 172,208 个图像条件教师候选中选出。Qwen3.5-397B-A17B 在高推理模式下为每个示例生成一个候选，能够访问原始说明文字和配对图像，使用温度 1.0、top-p 0.9 和依来源而定的 16,000–65,536 token 最大补全长度。附录 E.1 复现其系统提示词。原始教师回答使用 `<analysis>` 块做验证；被接受的轨迹在训练前映射至学生的 `<think>` 接口。提示器在训练和推理时只接收原始说明文字。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> We filter candidates with Gemini 3 Pro (`gemini-3-pro-preview-new`) using validator v4. Five independent calls assess (i) prompt–image alignment (aligned/partial/mismatch) and four reasoning-quality axes scored as `none`/`minor`/`major`: (ii) whether inferred details are properly introduced, (iii) whether imagined specifics are justified, (iv) reverse rationalization, and (v) violations of the prescribed reasoning-stage boundaries. The strict gate requires `aligned` on the first axis and no `major` flag on the remaining four; `minor` flags are retained without reranking, while parsing or API failures are rejected. This gate accepts 58,907 candidates (34.2%), and prompt-level deduplication yields the 50,182 training examples. Unsupported imagined specifics are the dominant rejection mode, occurring in 71.9% of rejected traces and acting as the sole rejection reason in 40.7%; prompt–image misalignment and reverse rationalization are the next most common causes. Appendix E.3 reproduces the exact validator-v4 prompts. The loss is token-level cross-entropy on the assistant tokens—both the converted `<think>` block and the JSON—with the same prompt masking as SFT. We run ∼8 epochs as two chained 4-epoch sub-runs sharing the same hyperparameters.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 我们用 Gemini 3 Pro（`gemini-3-pro-preview-new`）及 validator v4 过滤候选。5 个独立调用评估：(i) 提示词–图像对齐（`aligned`/`partial`/`mismatch`），以及按 `none`/`minor`/`major` 评分的 4 个推理质量轴：(ii) 推断细节是否被适当引入；(iii) 想象出的具体细节是否合理；(iv) 反向合理化；(v) 是否违反规定的推理阶段边界。严格门槛要求第一轴为 `aligned`，且余下 4 个轴均无 `major` 标志；`minor` 标志不重排序而直接保留，解析或 API 失败则拒绝。该门槛接受 58,907 个候选（34.2%），提示词层面的去重得到 50,182 个训练示例。未获支持的想象具体细节是主要拒绝模式，出现在 71.9% 的被拒轨迹中，并在 40.7% 的情形作为唯一拒绝原因；提示词–图像不对齐和反向合理化是接下来最常见的原因。附录 E.3 复现精确的 validator-v4 提示词。损失是在助手 token 上的 token 级交叉熵——包括转换后的 `<think>` 块和 JSON——并使用与 SFT 相同的提示词掩码。我们以共享同一套超参数的两个串联 4-epoch 子运行完成约 8 个 epoch。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Stage 3 — RFT (gated OPSD).** Appendix C.5.2 gives the complete RFT specification, including its training data, rollout procedure, acceptance rule, and OPSD objective.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **阶段 3——RFT（门控 OPSD）。** 附录 C.5.2 给出了完整 RFT 规范，包括其训练数据、rollout 过程、接受规则和 OPSD 目标。

### C.5.2 OPSD: On-Policy Self-Distillation / OPSD：在策略自蒸馏

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> OPSD (On-Policy Self-Distillation) is the image-conditioned distillation objective in the prompter’s RFT stage (§3.4, Stage 3). RFT uses `ms-swift`’s on-policy distillation trainer over 10,003 original-caption–image pairs stratified across six prompt sources. Its design follows the conditioning asymmetry measured by GPG (§3.2): an image-conditioned model can supply training information unavailable to the image-free inference-time prompter. OPSD assumes the student already emits parseable, image-grounded schemas, which is ensured by Stages 1 (SFT) and 2 (Cold-start) of the pipeline.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> OPSD（On-Policy Self-Distillation，在策略自蒸馏）是提示器 RFT 阶段（§3.4，阶段 3）中的图像条件蒸馏目标。RFT 在 10,003 个原始说明文字–图像对上使用 `ms-swift` 的在策略蒸馏训练器，这些配对跨 6 个提示词来源分层。其设计遵循 GPG 测得的条件不对称性（§3.2）：图像条件模型能够提供图像无关、推理时提示器无法获得的训练信息。OPSD 假定学生已能生成可解析、基于图像的模式，这一点由流水线的阶段 1（SFT）和阶段 2（Cold-start）确保。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Teacher and student.** The student $\pi_\theta$ is the prompter under training: a rank-128 LoRA on Qwen3.5-397B-A17B after SFT + Cold-start, run image-free. The teacher $\pi^\star$ is the same Qwen3.5-397B-A17B base without our LoRA, queried with the same user prompt and the reference image in thinking mode at training time only. Teacher parameters are frozen throughout, and no gradients flow through $\pi^\star$.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **教师与学生。** 学生 $\pi_\theta$ 是正在训练的提示器：在 SFT + Cold-start 后的 Qwen3.5-397B-A17B 上的 rank-128 LoRA，以无图像方式运行。教师 $\pi^\star$ 是没有我们 LoRA 的同一 Qwen3.5-397B-A17B 基座，仅在训练时以相同用户提示词和参考图像在思考模式下查询。教师参数始终冻结，且没有梯度流经 $\pi^\star$。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **On-policy rollouts.** For each (user prompt, image) pair, we sample a structured-caption rollout $\tau=(\tau_1,\ldots,\tau_T)$ from the student image-free with temperature 1.0 and no nucleus truncation ($p=1.0$). Rollouts are served by a vLLM instance colocated on the training GPUs. At each token position $t$ we then evaluate both policies:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **在策略 rollout。** 对每个（用户提示词、图像）对，我们从无图像学生中以温度 1.0 和无 nucleus 截断（$p=1.0$）采样一个结构化说明文字 rollout $\tau=(\tau_1,\ldots,\tau_T)$。rollout 由与训练 GPU 同置的 vLLM 实例提供。在每个 token 位置 $t$，我们随后评估两个策略：

- teacher distribution $\pi^\star(\cdot \mid \tau_{<t}, \mathrm{prompt}, I)$: a forward pass under the teacher with image conditioning.  
  教师分布 $\pi^\star(\cdot \mid \tau_{<t}, \mathrm{prompt}, I)$：教师在图像条件下的一次前向过程。
- student distribution $\pi_\theta(\cdot \mid \tau_{<t}, \mathrm{prompt})$: a forward pass under the student without image conditioning.  
  学生分布 $\pi_\theta(\cdot \mid \tau_{<t}, \mathrm{prompt})$：学生在无图像条件下的一次前向过程。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The per-token divergence of Eq. (6)—in implementation a KL divergence, evaluated over the top-64 teacher logits with each token’s divergence clipped at 5.0—is summed over the rollout’s response positions and normalized by their count. Sampling on-policy (from $\pi_\theta$ rather than $\pi^\star$) keeps the gradient supported on captions the student actually emits at inference, preventing mode-collapse onto teacher behaviors unreachable image-free; this is the “on-policy” in OPSD.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 式 (6) 的逐 token 散度——实现中为 KL 散度，在 top-64 教师 logit 上计算，且每个 token 的散度被截断为 5.0——在 rollout 的回答位置上求和并按其数量归一化。在策略采样（来自 $\pi_\theta$ 而非 $\pi^\star$）使梯度由学生在推理时实际生成的说明文字支持，避免模式坍塌到无图像条件下不可达的教师行为；这正是 OPSD 中“on-policy”的含义。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Combination with the verifier.** Each rollout is rendered and scored by the Gemini verifier on structure, alignment, and aesthetic quality; only rollouts scoring at least 6/10 on all three axes are retained, while failed, unparsable, or incomplete API responses are dropped. The OPSD objective $L_{\mathrm{OPSD}}$ (Eq. (6)) is applied only to these retained rollouts. The verifier derives QA pairs from the user request and checks them against the rendered image; it never receives the rollout’s SP. The verifier therefore selects high-confidence training data, while the image-conditioned teacher supplies the token-level OPSD targets. There is no weighted combination between the two signals, and the distillation objective carries no token-cross-entropy auxiliary (`sft_alpha= 0`). The ablations of §4.2 isolate the two components with distinct training rules: verifier-reward GRPO (the verifier-only row) optimizes the verifier reward with no OPSD; OPSD-only applies $L_{\mathrm{OPSD}}$ to all rollouts without a verifier gate; the full method applies OPSD only to verifier-accepted rollouts.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **与验证器的结合。** 每个 rollout 都被渲染，并由 Gemini 验证器在结构、对齐和美学质量上评分；仅在三个轴上均至少得 6/10 的 rollout 被保留，失败、不可解析或不完整的 API 回答被丢弃。OPSD 目标 $L_{\mathrm{OPSD}}$（式 (6)）仅应用于这些保留的 rollout。验证器从用户请求中导出 QA 对，并对照渲染图像检查它们；它从不接收 rollout 的 SP。因此，验证器选择高置信度训练数据，而图像条件教师提供 token 级 OPSD 目标。两个信号之间没有加权组合，且蒸馏目标不带 token 交叉熵辅助项（`sft_alpha= 0`）。§4.2 的消融以不同训练规则隔离这两个组件：验证器奖励 GRPO（仅验证器行）在没有 OPSD 的情况下优化验证器奖励；仅 OPSD 对所有 rollout 应用 $L_{\mathrm{OPSD}}$ 而没有验证器门槛；完整方法只对验证器接受的 rollout 应用 OPSD。

## C.6 Inference and the agentic loop / 推理与智能体循环

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Single-shot prompter inference.** The trained prompter (rank-128 LoRA on Qwen3.5-397B-A17B, run image-free) is decoded greedily at evaluation time—temperature 0, repetition penalty 1.0, up to 16,384 new tokens—in contrast to the temperature-1.0 on-policy rollouts used during RFT. It emits a `<think>` reasoning block followed by the JSON structured prompt. The generation wrapper strips the thinking trace, reads `ratio` to select the output canvas, removes that control field, and passes only the remaining structured record to the diffusion backbone.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **单次提示器推理。** 训练后的提示器（Qwen3.5-397B-A17B 上的 rank-128 LoRA，无图像运行）在评估时用贪婪方式解码——温度 0、重复惩罚 1.0、最多 16,384 个新 token——与 RFT 期间使用的温度 1.0 在策略 rollout 相对。它输出一个 `<think>` 推理块，后接 JSON 结构化提示词。生成包装器剥离思考轨迹，读取 `ratio` 以选择输出画布，移除该控制字段，并仅将余下的结构化记录传递给扩散主干。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Diffusion sampling.** Images are rendered with a first-order Euler ODE solver over 50 denoising steps on a linear schedule shifted per sample by resolution. Qwen-Image (main results) uses classifier-free guidance scale 4.0; BAGEL (scaling-property cells) uses 8.0 with timestep shift 4.0. Benchmark images are generated at $1024\times1024$ by default; multi-aspect benchmarks use a $1536^2$-pixel-budget, ratio-aware schedule snapped to multiples of 64. All main-table results are *single-shot*, with one prompter forward pass followed by one render. Only Table 5 evaluates the agentic loop.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **扩散采样。** 图像使用一阶 Euler ODE 求解器渲染，在 50 个去噪步上采用按分辨率逐样本偏移的线性日程。Qwen-Image（主结果）使用 4.0 的无分类器引导尺度；BAGEL（缩放性质单元）使用 8.0 和 4.0 的时间步偏移。基准图像默认以 $1024\times1024$ 生成；多纵横比基准使用 $1536^2$ 像素预算、感知比例且对齐至 64 的倍数的日程。所有主表结果都是*单次*的，即一次提示器前向后接一次渲染。只有表 5 评估智能体循环。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Agentic loop runtime.** Given a user prompt $u$, round $t$ forms $\mathrm{SP}_t=\pi_\theta(u,\mathrm{SP}_{<t},c_{t-1})$ from the prior structured prompts $\mathrm{SP}_{<t}$ and the accumulated critique $c_{t-1}$ ($c_0=\varnothing$); the fixed diffuser renders $I_t$; and three independent Gemini calls inspect $(u,I_t)$ for structure, alignment, and aesthetic quality. Their outputs are aggregated into the three per-axis scores, a pass flag, and a structured issue list. PASS requires all three axes to score at least 6/10; any axis below threshold yields FAIL together with a structured critique $c_t$—a list of (field-path, observed-value, expected-value) triples over the violated constraints (missing objects, wrong counts, attribute mismatches, spatial-relation violations)—so the next round edits only the named fields rather than re-parsing free-form feedback. The refiner receives the full critique history $\{c_1,\ldots,c_{t-1}\}$ and the prior structured prompts; repeated critiques trigger escalation from local edits (round 2) to a structural change (round 3) and then a substantially different composition (round 4 onward). The loop returns $I_t$ on PASS and hard-stops at $T_{\max}=8$ rounds; per round the wall-clock is ∼20–35 s (prompter ∼6–9 s, render ∼5–10 s at $1024^2$, judge ∼8–15 s).

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **智能体循环运行时。** 给定用户提示词 $u$，第 $t$ 轮根据先前结构化提示词 $\mathrm{SP}_{<t}$ 和累计批评 $c_{t-1}$（$c_0=\varnothing$）构成 $\mathrm{SP}_t=\pi_\theta(u,\mathrm{SP}_{<t},c_{t-1})$；固定扩散器渲染 $I_t$；3 次独立 Gemini 调用检查 $(u,I_t)$ 的结构、对齐和美学质量。其输出被聚合为逐轴的 3 个分数、一个通过标志和一个结构化问题列表。PASS 要求三个轴均至少得 6/10；任一轴低于阈值即产生 FAIL 及结构化批评 $c_t$——违反约束（缺少对象、数量错误、属性不匹配、空间关系违例）上（字段路径、观察值、期望值）三元组的列表——使下一轮只编辑被点名的字段，而不是重新解析自由形式反馈。精炼器接收完整批评历史 $\{c_1,\ldots,c_{t-1}\}$ 和先前结构化提示词；重复批评触发从局部编辑（第 2 轮）升级为结构改变（第 3 轮），再到实质不同的构图（第 4 轮及之后）。循环在 PASS 时返回 $I_t$，并在 $T_{\max}=8$ 轮时硬停止；每轮的实际耗时约为 20–35 s（提示器约 6–9 s、在 $1024^2$ 下渲染约 5–10 s、评审约 8–15 s）。

## C.7 External dependencies and licenses / 外部依赖与许可证

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Table 14 records the external code and model dependencies used in this work together with the currently available upstream license information. Entries whose repositories provide no license file, or whose terms still require confirmation, are marked explicitly rather than treated as verified.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 表 14 记录本工作使用的外部代码和模型依赖，以及当前可获得的上游许可证信息。仓库未提供许可证文件，或条款仍需确认的条目被明确标记，而不视为已验证。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Table 14: External code and model dependencies.** Components are grouped by pipeline role and listed with their available upstream license information; unresolved entries are marked explicitly.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **表 14：外部代码和模型依赖。** 组件按流水线角色分组，并列出其可获得的上游许可证信息；未解决条目被明确标记。

| Component / 组件 | License / 许可证 | Notes / 说明 |
|---|---|---|
| *Models / 模型* | | |
| BAGEL | Apache-2.0 | diffusion backbone (§3.2) |
| Qwen-Image-2512 | Apache-2.0 | diffusion backbone (§3.4) |
| Qwen3.5 family | Apache-2.0 | prompter SFT / cold-start / RFT student |
| Qwen3.5-397B-A17B | Apache-2.0 | OPSD teacher; GPG judge |
| Sapiens | CC-BY-NC-4.0 | pose estimation (annotation stage 2); non-commercial |
| DepthAnything V2 | CC-BY-NC-4.0 | monocular depth (annotation stage 3); code Apache-2.0, large ckpt non-commercial |
| SAM 2.1 | Apache-2.0 | segmentation + occlusion (annotation stage 3) |
| Seed-VL | Internal | scene + per-element captioning; API-only, not publicly released |
| Gemini 3 Pro | API ToS | ED source-tuple extractor (offline, cached); training-time RFT verifier and online agentic judge |
| Gemini 2.5 Flash | API ToS | T2I-CoReBench evaluator |
| GPT-4o | API ToS | ED image-source extractor robustness check; WISE legacy evaluator |
| GPT-5.4 | API ToS | ED caption-tuple extractor and matcher; offline structure, alignment, and GSB evaluator |
| GPT-5.5 | API ToS | rewriting backend; ED image-source robustness check |
| Claude Opus 4.8 / Claude Code | API ToS / proprietary | single-turn rewriting backend / agentic coding backend |
| GLM-5.2 | API ToS | single-turn rewriting backend |
| Codex | Proprietary | agentic coding backend |
| *Training infrastructure / 训练基础设施* | | |
| PyTorch | BSD-3-Clause | |
| Transformers (HF) | Apache-2.0 | model loading, tokenizers |
| diffusers (HF) | Apache-2.0 | diffusion pipelines |
| ms-swift | Apache-2.0 | prompter LoRA training harness (wraps Megatron-LM for SFT / cold-start, DeepSpeed for RFT) |
| Megatron-LM | Apache-2.0 | TP/PP/EP backend for prompter SFT / cold-start (via ms-swift) |
| DeepSpeed / FSDP | Apache-2.0 / BSD-3-Clause | DeepSpeed (ZeRO-3) for prompter RFT; FSDP (ships with PyTorch) for the diffusion backbones |
| vLLM | Apache-2.0 | colocated on-policy rollout engine for RFT |
| FlashAttention | BSD-3-Clause | |
| *Evaluation / 评估* | | |
| GenEval | MIT | official scoring scripts |
| GenEval++ | Upstream terms | evaluation released with Echo-4o; redistribution terms to verify |
| GenEval2 | CC BY-NC 4.0 | official benchmark code and data; non-commercial use |
| DPG-Bench | Apache-2.0 | released within the ELLA repository |
| TIIF | No license file | upstream repository provides no license file |
| WISE | No license file | upstream repository provides no license file |
| T2I-CoReBench | Apache-2.0 | official benchmark dataset and evaluation code |


# Appendix C.6–E.4 (physical pages 36–48) / 附录 C.6–E.4（PDF 物理页 36–48）

## C.6 Inference and the Agentic Loop / 推理与智能体循环

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Single-shot prompter inference.** The trained prompter (rank-128 LoRA on Qwen3.5-397B-A17B, run image-free) is decoded greedily at evaluation time—temperature 0, repetition penalty 1.0, up to 16,384 new tokens—in contrast to the temperature-1.0 on-policy rollouts used during RFT. It emits a `<think>` reasoning block followed by the JSON structured prompt. The generation wrapper strips the thinking trace, reads `ratio` to select the output canvas, removes that control field, and passes only the remaining structured record to the diffusion backbone.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **单次提示器推理。** 训练后的提示器（在 Qwen3.5-397B-A17B 上采用 rank-128 LoRA、以无图像方式运行）在评估时使用贪心解码——temperature 为 0、repetition penalty 为 1.0、最多生成 16,384 个新 token——这与 RFT 期间 temperature 为 1.0 的在策略 rollout 不同。它先输出一个 `<think>` 推理块，随后输出 JSON 结构化提示。生成封装器会移除思维轨迹，读取 `ratio` 以选择输出画布，再移除该控制字段，并仅将剩余的结构化记录传给扩散骨干网络。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Diffusion sampling.** Images are rendered with a first-order Euler ODE solver over 50 denoising steps on a linear schedule shifted per sample by resolution. Qwen-Image (main results) uses classifier-free guidance scale 4.0; BAGEL (scaling-property cells) uses 8.0 with timestep shift 4.0. Benchmark images are generated at $1024 \times 1024$ by default; multi-aspect benchmarks use a $1536^2$-pixel-budget, ratio-aware schedule snapped to multiples of 64. All main-table results are *single-shot*, with one prompter forward pass followed by one render. Only Table 5 evaluates the agentic loop.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **扩散采样。** 图像使用一阶 Euler ODE 求解器，在 50 个去噪步骤上渲染；采用线性调度，并根据每个样本的分辨率进行偏移。Qwen-Image（主要结果）的 classifier-free guidance scale 为 4.0；BAGEL（缩放性质实验单元）使用 8.0，timestep shift 为 4.0。基准图像默认以 $1024 \times 1024$ 生成；多宽高比基准采用像素预算为 $1536^2$、感知宽高比且对齐到 64 的倍数的调度。主表中的所有结果均为*单次生成*：一次提示器前向传播后接一次渲染。只有表 5 评估了智能体循环。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Agentic loop runtime.** Given a user prompt $u$, round $t$ forms $\mathrm{SP}_t = \pi_\theta(u, \mathrm{SP}_{<t}, c_{t-1})$ from the prior structured prompts $\mathrm{SP}_{<t}$ and the accumulated critique $c_{t-1}$ ($c_0 = \varnothing$); the fixed diffuser renders $I_t$; and three independent Gemini calls inspect $(u, I_t)$ for structure, alignment, and aesthetic quality. Their outputs are aggregated into the three per-axis scores, a pass flag, and a structured issue list. PASS requires all three axes to score at least 6/10; any axis below threshold yields FAIL together with a structured critique $c_t$—a list of (field-path, observed-value, expected-value) triples over the violated constraints (missing objects, wrong counts, attribute mismatches, spatial-relation violations)—so the next round edits only the named fields rather than re-parsing free-form feedback. The refiner receives the full critique history $\{c_1, \ldots, c_{t-1}\}$ and the prior structured prompts; repeated critiques trigger escalation from local edits (round 2) to a structural change (round 3) and then a substantially different composition (round 4 onward). The loop returns $I_t$ on PASS and hard-stops at $T_{\max}=8$ rounds; per round the wall-clock is $\sim$20–35 s (prompter $\sim$6–9 s, render $\sim$5–10 s at $1024^2$, judge $\sim$8–15 s).

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **智能体循环运行时。** 给定用户提示 $u$，第 $t$ 轮根据先前的结构化提示 $\mathrm{SP}_{<t}$ 和累积批评 $c_{t-1}$（$c_0 = \varnothing$）构造 $\mathrm{SP}_t = \pi_\theta(u, \mathrm{SP}_{<t}, c_{t-1})$；固定的扩散器渲染 $I_t$；三个相互独立的 Gemini 调用分别检查 $(u, I_t)$ 的结构、对齐与审美质量。它们的输出被聚合为三个轴向分数、一个通过标志以及一份结构化问题列表。PASS 要求三个轴的得分均至少为 6/10；任一轴低于阈值都会得到 FAIL，并附带结构化批评 $c_t$——针对违反约束项的一组（field-path、observed-value、expected-value）三元组列表（缺失对象、数量错误、属性不匹配、空间关系违规）——使下一轮只编辑被点名的字段，而不必重新解析自由形式反馈。精修器接收完整的批评历史 $\{c_1, \ldots, c_{t-1}\}$ 与先前的结构化提示；重复出现的批评会触发升级：从局部编辑（第 2 轮）升级为结构改变（第 3 轮），再升级为显著不同的构图（第 4 轮及以后）。循环在 PASS 时返回 $I_t$，并在 $T_{\max}=8$ 轮时硬停止；每轮墙钟时间约为 20–35 秒（提示器约 6–9 秒、在 $1024^2$ 下渲染约 5–10 秒、评审器约 8–15 秒）。

## C.7 External Dependencies and Licenses / 外部依赖与许可证

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Table 14 records the external code and model dependencies used in this work together with the currently available upstream license information. Entries whose repositories provide no license file, or whose terms still require confirmation, are marked explicitly rather than treated as verified.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 表 14 记录了本工作使用的外部代码与模型依赖，以及目前可获得的上游许可证信息。对于代码仓库未提供许可证文件或条款仍需确认的条目，表中均予以明确标注，而不将其视为已经核实。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Table 14: External code and model dependencies.** Components are grouped by pipeline role and listed with their available upstream license information; unresolved entries are marked explicitly.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **表 14：外部代码与模型依赖。** 各组件按流水线角色分组，并列出可获得的上游许可证信息；尚未解决的条目均明确标注。

| Component / 组件 | License / 许可证 | Notes / 说明 |
|---|---|---|
| *Models / 模型* |  |  |
| BAGEL | Apache-2.0 | diffusion backbone (§3.2) / 扩散骨干（§3.2） |
| Qwen-Image-2512 | Apache-2.0 | diffusion backbone (§3.4) / 扩散骨干（§3.4） |
| Qwen3.5 family | Apache-2.0 | prompter SFT / cold-start / RFT student / 提示器 SFT／冷启动／RFT 学生模型 |
| Qwen3.5-397B-A17B | Apache-2.0 | OPSD teacher; GPG judge / OPSD 教师；GPG 评审器 |
| Sapiens | CC-BY-NC-4.0 | pose estimation (annotation stage 2); non-commercial / 姿态估计（标注阶段 2）；非商业用途 |
| DepthAnything V2 | CC-BY-NC-4.0 | monocular depth (annotation stage 3); code Apache-2.0, large ckpt non-commercial / 单目深度（标注阶段 3）；代码为 Apache-2.0，大型检查点限非商业用途 |
| SAM 2.1 | Apache-2.0 | segmentation + occlusion (annotation stage 3) / 分割与遮挡（标注阶段 3） |
| Seed-VL | Internal | scene + per-element captioning; API-only, not publicly released / 场景与逐元素描述；仅 API，未公开发布 |
| Gemini 3 Pro | API ToS | ED source-tuple extractor (offline, cached); training-time RFT verifier and online agentic judge / ED 源元组提取器（离线、缓存）；训练时 RFT 验证器与在线智能体评审器 |
| Gemini 2.5 Flash | API ToS | T2I-CoReBench evaluator / T2I-CoReBench 评估器 |
| GPT-4o | API ToS | ED image-source extractor robustness check; WISE legacy evaluator / ED 图像源提取器鲁棒性检查；WISE 旧版评估器 |
| GPT-5.4 | API ToS | ED caption-tuple extractor and matcher; offline structure, alignment, and GSB evaluator / ED 描述元组提取器与匹配器；离线结构、对齐与 GSB 评估器 |
| GPT-5.5 | API ToS | rewriting backend; ED image-source robustness check / 改写后端；ED 图像源鲁棒性检查 |
| Claude Opus 4.8 / Claude Code | API ToS / proprietary | single-turn rewriting backend / agentic coding backend / 单轮改写后端／智能体编程后端 |
| GLM-5.2 | API ToS | single-turn rewriting backend / 单轮改写后端 |
| Codex | Proprietary | agentic coding backend / 智能体编程后端 |
| *Training infrastructure / 训练基础设施* |  |  |
| PyTorch | BSD-3-Clause |  |
| Transformers (HF) | Apache-2.0 | model loading, tokenizers / 模型加载、分词器 |
| diffusers (HF) | Apache-2.0 | diffusion pipelines / 扩散流水线 |
| ms-swift | Apache-2.0 | prompter LoRA training harness (wraps Megatron-LM for SFT / cold-start, DeepSpeed for RFT) / 提示器 LoRA 训练框架（SFT／冷启动封装 Megatron-LM，RFT 封装 DeepSpeed） |
| Megatron-LM | Apache-2.0 | TP/PP/EP backend for prompter SFT / cold-start (via ms-swift) / 提示器 SFT／冷启动的 TP／PP／EP 后端（通过 ms-swift） |
| DeepSpeed / FSDP | Apache-2.0 / BSD-3-Clause | DeepSpeed (ZeRO-3) for prompter RFT; FSDP (ships with PyTorch) for the diffusion backbones / 提示器 RFT 使用 DeepSpeed（ZeRO-3）；扩散骨干使用 FSDP（随 PyTorch 提供） |
| vLLM | Apache-2.0 | colocated on-policy rollout engine for RFT / 用于 RFT 的共置式在策略 rollout 引擎 |
| FlashAttention | BSD-3-Clause |  |
| *Evaluation / 评估* |  |  |
| GenEval | MIT | official scoring scripts / 官方评分脚本 |
| GenEval++ | Upstream terms | evaluation released with Echo-4o; redistribution terms to verify / 与 Echo-4o 一同发布的评估；再分发条款待核实 |
| GenEval2 | CC BY-NC 4.0 | official benchmark code and data; non-commercial use / 官方基准代码与数据；非商业用途 |
| DPG-Bench | Apache-2.0 | released within the ELLA repository / 在 ELLA 仓库内发布 |
| TIIF | No license file | upstream repository provides no license file / 上游仓库未提供许可证文件 |
| WISE | No license file | upstream repository provides no license file / 上游仓库未提供许可证文件 |
| T2I-CoReBench | Apache-2.0 | official benchmark dataset and evaluation code / 官方基准数据集与评估代码 |

## D Additional Benchmark Results / 其他基准结果

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Protocol and score provenance.** This section provides evaluation protocols, score provenance, and per-category breakdowns for the benchmarks reported in Table 2. Published baselines follow the respective leaderboards or original papers unless noted otherwise. The Nano Banana DPG-Bench score is taken from He et al. (2026). WISE uses the legacy WiScore protocol with GPT-4o-2024-05-13: we evaluate Nano Banana, Qwen-Image$^*$, matched NL, and Ours under this protocol, while the remaining WISE scores come from published legacy-protocol evaluations (Niu et al., 2025; Guo et al., 2025). Qwen-Image$^*$ uses its official prompt enhancer; $\dagger$ marks our re-evaluation on Qwen-Image-2512. Matched NL and Ours use the matched settings described in Appendix C.2, and Ours uses single-shot inference in Table 2.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **协议与分数来源。** 本节给出表 2 所报告各基准的评估协议、分数来源与逐类别分解。除非另有说明，已发表基线均遵循相应排行榜或原始论文。Nano Banana 的 DPG-Bench 分数取自 He et al. (2026)。WISE 使用以 GPT-4o-2024-05-13 为评估器的旧版 WiScore 协议：我们在该协议下评估 Nano Banana、Qwen-Image$^*$、matched NL 与 Ours，其余 WISE 分数则来自已发表的旧版协议评估（Niu et al., 2025；Guo et al., 2025）。Qwen-Image$^*$ 使用其官方提示增强器；$\dagger$ 表示我们在 Qwen-Image-2512 上重新评估。Matched NL 与 Ours 使用附录 C.2 所述的匹配设置，表 2 中的 Ours 使用单次推理。

### D.1 DPG-Bench Per-Category Breakdown / DPG-Bench 逐类别分解

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Table 15 reports per-category scores on DPG-Bench, covering *global* scene description, *entity* presence, *attribute* binding, *relation* between entities, and *other* dense-prompt aspects, followed by the overall score.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 表 15 报告 DPG-Bench 的逐类别分数，依次涵盖*全局*场景描述、*实体*存在、*属性*绑定、实体间*关系*以及*其他*密集提示方面，最后给出总分。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Table 15: DPG-Bench per-category scores.** Published category breakdowns are shown for the baselines; Qwen-Image$^*$, matched NL, and Ours report our matched per-category evaluations.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **表 15：DPG-Bench 逐类别分数。** 基线展示已发表的类别分解；Qwen-Image$^*$、matched NL 与 Ours 报告我们在匹配设置下的逐类别评估。

| Model / 模型 | Global / 全局 | Entity / 实体 | Attribute / 属性 | Relation / 关系 | Other / 其他 | Overall / 总体 |
|---|---:|---:|---:|---:|---:|---:|
| SD v1.5 | 74.63 | 74.23 | 75.39 | 73.49 | 67.81 | 63.18 |
| PixArt-α | 74.97 | 79.32 | 78.60 | 82.57 | 76.96 | 71.11 |
| LUMINA-Next | 82.82 | 88.65 | 86.44 | 80.53 | 81.82 | 74.63 |
| SDXL | 83.27 | 82.43 | 80.91 | 86.76 | 80.41 | 74.65 |
| Playground v2.5 | 83.06 | 82.59 | 81.20 | 84.08 | 83.50 | 75.47 |
| Hunyuan-DiT | 84.59 | 80.59 | 88.01 | 74.36 | 86.41 | 78.87 |
| Janus | 82.33 | 87.38 | 87.70 | 85.46 | 86.41 | 79.68 |
| PixArt-Σ | 86.89 | 82.89 | 88.94 | 86.59 | 87.68 | 80.54 |
| Emu3-Gen | 85.21 | 86.68 | 86.84 | 90.22 | 83.15 | 80.60 |
| Janus-Pro-1B | 87.58 | 88.63 | 88.17 | 88.98 | 88.30 | 82.63 |
| DALL·E 3 | 90.97 | 89.61 | 88.39 | 90.58 | 89.83 | 83.50 |
| FLUX.1 Dev | 74.35 | 90.00 | 88.96 | 90.87 | 88.33 | 83.84 |
| SD3 Medium | 87.90 | 91.01 | 88.83 | 80.70 | 88.68 | 84.08 |
| Janus-Pro-7B | 86.90 | 88.90 | 89.40 | 89.32 | 89.48 | 84.19 |
| HiDream-I1-Full | 76.44 | 90.22 | 89.48 | 93.74 | 91.83 | 85.89 |
| Seedream 3.0 | 94.31 | 92.65 | 91.36 | 92.78 | 88.24 | 88.27 |
| GPT-Image-1 | 88.89 | 88.94 | 89.84 | 92.63 | 90.96 | 85.15 |
| Qwen-Image | 91.32 | 91.56 | 92.02 | 94.31 | 92.73 | 88.32 |
| Show-o | 79.33 | 75.44 | 78.02 | 84.45 | 60.80 | 67.27 |
| TokenFlow-XL | 78.72 | 79.22 | 81.29 | 85.22 | 71.20 | 73.38 |
| OmniGen | 87.90 | 88.97 | 88.47 | 87.95 | 83.56 | 81.16 |
| OmniGen2 | 88.81 | 88.83 | 90.18 | 89.37 | 90.27 | 83.57 |
| BAGEL | 88.94 | 90.37 | 91.29 | 90.82 | 88.67 | 85.07 |
| UniWorld-V1 | 83.64 | 88.39 | 88.44 | 89.27 | 87.22 | 81.38 |
| Ovis-U1 | 82.37 | 90.08 | 88.68 | 93.35 | 85.20 | 83.72 |
| Skywork UniPic | 89.65 | 87.78 | 90.84 | 91.89 | 91.95 | 85.50 |
| Qwen-Image$^*$ | 89.04 | 91.91 | 92.39 | 90.85 | 93.07 | 87.20 |
| Matched NL + Qwen-Image | 89.50 | 92.30 | 92.00 | 90.50 | 93.50 | 87.80 |
| Ours (Qwen-Image) | 92.05 | 94.13 | 94.48 | 93.36 | 94.97 | **90.71** |

### D.2 GenEval Per-Skill Breakdown / GenEval 逐技能分解

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Table 16 reports per-skill accuracy on GenEval, covering single-object / two-objects presence, counting, colors, position, and color-attribute binding, with the overall accuracy in the last column.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 表 16 报告 GenEval 的逐技能准确率，涵盖单对象／双对象存在、计数、颜色、位置和颜色属性绑定，最后一列为总体准确率。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Table 16: GenEval per-skill accuracy.** Published per-skill breakdowns are shown for the baselines; Ours reports our evaluation. Qwen-Image$^*$ uses its official prompt enhancement, as in Table 2.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **表 16：GenEval 逐技能准确率。** 基线展示已发表的逐技能分解；Ours 报告我们的评估。与表 2 相同，Qwen-Image$^*$ 使用其官方提示增强。

| Model / 模型 | Single Obj. / 单对象 | Two Obj. / 双对象 | Counting / 计数 | Colors / 颜色 | Position / 位置 | Color Attr. / 颜色属性 | Overall / 总体 |
|---|---:|---:|---:|---:|---:|---:|---:|
| SD v2.1 | 0.98 | 0.51 | 0.44 | 0.85 | 0.07 | 0.17 | 0.50 |
| SDXL | 0.98 | 0.74 | 0.39 | 0.85 | 0.15 | 0.23 | 0.55 |
| IF-XL | 0.97 | 0.74 | 0.66 | 0.81 | 0.13 | 0.35 | 0.61 |
| PixArt-α | 0.98 | 0.50 | 0.44 | 0.80 | 0.08 | 0.07 | 0.48 |
| LUMINA-Next | 0.92 | 0.46 | 0.48 | 0.70 | 0.09 | 0.13 | 0.46 |
| SD3 Medium | 0.99 | 0.94 | 0.72 | 0.89 | 0.33 | 0.60 | 0.74 |
| SD3.5 Large | 0.98 | 0.89 | 0.73 | 0.83 | 0.34 | 0.47 | 0.71 |
| FLUX.1 Dev | 0.99 | 0.81 | 0.79 | 0.74 | 0.20 | 0.47 | 0.67 |
| NOVA | 0.99 | 0.91 | 0.62 | 0.85 | 0.33 | 0.56 | 0.71 |
| TokenFlow-XL | 0.95 | 0.60 | 0.41 | 0.81 | 0.16 | 0.24 | 0.55 |
| Janus | 0.97 | 0.68 | 0.30 | 0.84 | 0.46 | 0.42 | 0.61 |
| JanusFlow | 0.97 | 0.59 | 0.45 | 0.83 | 0.53 | 0.42 | 0.63 |
| Janus-Pro-7B | 1.00 | 0.98 | 0.79 | 0.91 | 0.60 | 0.72 | 0.83 |
| Emu3-Gen | 0.98 | 0.71 | 0.34 | 0.81 | 0.17 | 0.21 | 0.54 |
| Show-o | 0.95 | 0.52 | 0.49 | 0.82 | 0.11 | 0.28 | 0.53 |
| OmniGen | 0.98 | 0.84 | 0.66 | 0.74 | 0.40 | 0.43 | 0.68 |
| OmniGen2 | 1.00 | 0.95 | 0.64 | 0.88 | 0.55 | 0.76 | 0.80 |
| HiDream-I1-Full | 0.99 | 0.89 | 0.59 | 0.90 | 0.79 | 0.66 | 0.80 |
| BAGEL | 0.99 | 0.94 | 0.81 | 0.88 | 0.64 | 0.63 | 0.82 |
| UniWorld-V1 | 0.99 | 0.93 | 0.79 | 0.89 | 0.49 | 0.70 | 0.80 |
| Seedream 3.0 | 0.99 | 0.96 | 0.91 | 0.93 | 0.47 | 0.80 | 0.84 |
| GPT-Image-1 | 0.99 | 0.92 | 0.85 | 0.92 | 0.75 | 0.61 | 0.84 |
| Ovis-U1 | 0.98 | 0.98 | 0.90 | 0.92 | 0.79 | 0.75 | 0.89 |
| Skywork UniPic | 0.98 | 0.92 | 0.74 | 0.91 | 0.89 | 0.72 | 0.86 |
| Qwen-Image | 0.99 | 0.92 | 0.89 | 0.88 | 0.76 | 0.77 | 0.87 |
| Qwen-Image$^*$ | 1.00 | 0.95 | 0.93 | 0.92 | 0.87 | 0.83 | 0.91 |
| Matched NL + Qwen-Image | 1.00 | 0.95 | 0.92 | 0.93 | 0.86 | 0.82 | 0.91 |
| Ours (Qwen-Image) | 1.00 | 0.96 | 0.94 | 0.95 | 0.93 | 0.86 | **0.94** |

### D.3 WISE Per-Category Breakdown / WISE 逐类别分解

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Table 17 reports per-category WiScore under the legacy WISE protocol, which uses GPT-4o-2024-05-13 to score consistency, realism, and aesthetic quality. WISE covers six domains: cultural, temporal, spatial, biology, physics, and chemistry. Models are grouped into dedicated T2I diffusion models, unified multimodal LLMs, proprietary systems, and open systems with prompt rewriting. The official overall WiScore aggregates prompt-level scores with domain weights 40%, 16.7%, 13.3%, 10%, 10%, and 10% in the displayed domain order, so it is not the unweighted mean of the six category entries. The four rows we evaluate ourselves follow that rule and reproduce from their own entries to within the displayed precision. Published overalls are transcribed from their sources rather than recomputed, and not all of them can be recovered from the rounded per-category entries reported alongside them: BAGEL, most visibly, reports 0.52, which sits 0.019 above the weighted combination of its own six categories.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 表 17 报告旧版 WISE 协议下的逐类别 WiScore；该协议使用 GPT-4o-2024-05-13 对一致性、真实感和审美质量评分。WISE 涵盖六个领域：文化、时间、空间、生物学、物理学和化学。模型分为专用 T2I 扩散模型、统一多模态 LLM、专有系统，以及带提示改写的开放系统。官方总体 WiScore 按表中领域顺序，以 40%、16.7%、13.3%、10%、10% 和 10% 的领域权重聚合提示级分数，因此并不是六个类别条目的简单平均。我们自行评估的四行遵循该规则，由各自条目复算后在所示精度内一致。已发表的总体分数直接转录自来源，而非重新计算；并非所有总体分数都能由其同时报告且已舍入的逐类别条目恢复：最明显的是 BAGEL 报告 0.52，比其六个类别加权组合高 0.019。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Table 17: WISE per-category WiScore under the legacy protocol.** Published baseline scores follow the official legacy leaderboard; Nano Banana, Qwen-Image$^*$, matched NL, and Ours report our evaluations using the same legacy evaluator and scoring rule. Bold marks the best in each column.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **表 17：旧版协议下的 WISE 逐类别 WiScore。** 已发表基线分数遵循官方旧版排行榜；Nano Banana、Qwen-Image$^*$、matched NL 与 Ours 报告我们使用相同旧版评估器和评分规则得到的评估。粗体表示每列最佳值。

| Model / 模型 | Cultural / 文化 | Temporal / 时间 | Spatial / 空间 | Biology / 生物 | Physics / 物理 | Chemistry / 化学 | Overall / 总体 |
|---|---:|---:|---:|---:|---:|---:|---:|
| *Dedicated T2I / 专用 T2I* |  |  |  |  |  |  |  |
| FLUX.1 Dev | 0.48 | 0.58 | 0.62 | 0.42 | 0.51 | 0.35 | 0.50 |
| FLUX.1 Schnell | 0.39 | 0.44 | 0.50 | 0.31 | 0.44 | 0.26 | 0.40 |
| SD-3.5-large | 0.44 | 0.50 | 0.58 | 0.44 | 0.52 | 0.31 | 0.46 |
| SD-3.5-medium | 0.43 | 0.50 | 0.52 | 0.41 | 0.53 | 0.33 | 0.45 |
| SD-XL-base | 0.43 | 0.48 | 0.47 | 0.44 | 0.45 | 0.27 | 0.43 |
| SD-3-medium | 0.42 | 0.44 | 0.48 | 0.39 | 0.47 | 0.29 | 0.42 |
| SD-v1-5 | 0.34 | 0.35 | 0.32 | 0.28 | 0.29 | 0.21 | 0.32 |
| SD-2-1 | 0.30 | 0.38 | 0.35 | 0.33 | 0.34 | 0.21 | 0.32 |
| *Unified MLLM / 统一 MLLM* |  |  |  |  |  |  |  |
| GPT-Image-1 | 0.81 | 0.71 | 0.89 | 0.83 | 0.79 | 0.74 | 0.80 |
| DeepGen 1.0 | 0.72 | 0.81 | 0.70 | 0.67 | 0.82 | 0.66 | 0.73 |
| LongCat-Image | 0.66 | 0.61 | 0.72 | 0.66 | 0.72 | 0.49 | 0.65 |
| NextFlow-RL | 0.63 | 0.63 | 0.77 | 0.58 | 0.67 | 0.39 | 0.62 |
| Qwen-Image | 0.62 | 0.63 | 0.77 | 0.57 | 0.75 | 0.40 | 0.62 |
| UniWorld-V2 | 0.60 | 0.61 | 0.70 | 0.53 | 0.64 | 0.32 | 0.58 |
| HunyuanImage 3.0 | 0.58 | 0.57 | 0.70 | 0.56 | 0.63 | 0.31 | 0.57 |
| MetaQuery-XL | 0.56 | 0.55 | 0.62 | 0.49 | 0.63 | 0.41 | 0.55 |
| UniWorld-V1 | 0.53 | 0.55 | 0.73 | 0.45 | 0.59 | 0.41 | 0.55 |
| Manzano-30B | 0.58 | 0.50 | 0.65 | 0.50 | 0.55 | 0.32 | 0.54 |
| BAGEL | 0.44 | 0.55 | 0.68 | 0.44 | 0.60 | 0.39 | 0.52 |
| Emu3 | 0.34 | 0.45 | 0.48 | 0.41 | 0.45 | 0.27 | 0.39 |
| Janus-Pro-7B | 0.30 | 0.37 | 0.49 | 0.36 | 0.42 | 0.26 | 0.35 |
| *Proprietary / 专有系统* |  |  |  |  |  |  |  |
| Nano Banana | 0.89 | **0.87** | **0.95** | **0.89** | **0.89** | 0.79 | **0.89** |
| *Open with prompt rewriting / 带提示改写的开放系统* |  |  |  |  |  |  |  |
| Qwen-Image$^*$ | 0.85 | 0.76 | 0.89 | 0.81 | 0.83 | 0.82 | 0.83 |
| Matched NL + Qwen-Image | 0.86 | 0.75 | 0.90 | 0.82 | 0.82 | 0.83 | 0.84 |
| Qwen-Image + Ours (L10) | **0.91** | 0.83 | 0.92 | 0.88 | **0.89** | **0.88** | **0.89** |

### D.4 T2I-CoReBench Per-Category Breakdown / T2I-CoReBench 逐类别分解

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Table 18 expands the T2I-CoReBench comparison of Table 2 across the four *Composition* and eight *Reasoning* categories under the Gemini 2.5 Flash evaluator. Published baseline scores are taken from the official leaderboard (Li et al., 2026); Emu3.5 is omitted because the leaderboard does not report a corresponding row. Qwen-Image$^*$, matched NL, and Ours are evaluated with the same Gemini 2.5 Flash harness used for the main table. The composition dimensions are multi-instance (MI), multi-attribute (MA), multi-relation (MR), and text rendering (TR). The reasoning dimensions are logical (LR), behavioural (BR), hypothetical (HR), procedural (PR), generalization (GR), analogical (AR), commonsense (CR), and reconstructive reasoning (RR). Composition and reasoning averages are unweighted means over their four and eight dimensions, respectively, and Overall is the unweighted mean over all twelve. Our largest advantages appear in multi-attribute and multi-relation composition and across all eight reasoning categories, while multi-instance composition and text rendering remain stronger in Nano Banana and GPT-Image-1, respectively.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 表 18 在 Gemini 2.5 Flash 评估器下，将表 2 的 T2I-CoReBench 比较扩展到四个*构成*类别和八个*推理*类别。已发表基线分数取自官方排行榜（Li et al., 2026）；由于排行榜没有报告对应行，因此省略 Emu3.5。Qwen-Image$^*$、matched NL 与 Ours 使用主表相同的 Gemini 2.5 Flash 评估框架。构成维度包括多实例（MI）、多属性（MA）、多关系（MR）和文本渲染（TR）。推理维度包括逻辑（LR）、行为（BR）、假设（HR）、程序（PR）、泛化（GR）、类比（AR）、常识（CR）和重构推理（RR）。构成与推理平均分分别是其四个和八个维度的无权平均，Overall 则是全部十二个维度的无权平均。我们最大的优势出现在多属性、多关系构成以及全部八个推理类别上；多实例构成和文本渲染则分别仍由 Nano Banana 与 GPT-Image-1 占优。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Table 18: T2I-CoReBench per-category comparison under the Gemini 2.5 Flash evaluator.** Published baselines correspond to models in Table 2; Qwen-Image$^*$, matched NL, and Ours use our matched evaluation. Bold marks the best score in each column.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **表 18：Gemini 2.5 Flash 评估器下的 T2I-CoReBench 逐类别比较。** 已发表基线对应表 2 中的模型；Qwen-Image$^*$、matched NL 与 Ours 使用我们的匹配评估。粗体表示每列最佳分数。

| Model / 模型 | C-MI | C-MA | C-MR | C-TR | Comp. avg / 构成平均 |
|---|---:|---:|---:|---:|---:|
| FLUX.1 Dev | 58.6 | 60.3 | 44.1 | 31.1 | 48.6 |
| OmniGen2 | 67.9 | 64.1 | 48.3 | 19.2 | 49.9 |
| BAGEL | 64.9 | 65.2 | 45.8 | 9.7 | 46.4 |
| Qwen-Image | 81.4 | 79.6 | 65.6 | 85.5 | 78.0 |
| BAGEL + CoT | 57.7 | 60.8 | 37.8 | 2.2 | 39.6 |
| GPT-Image-1 | 84.1 | 75.9 | 72.7 | **86.4** | 79.8 |
| Nano Banana | **85.7** | 77.9 | 72.6 | 86.3 | 80.6 |
| LongCat-Image | 81.4 | 74.5 | 61.5 | 65.7 | 70.8 |
| HunyuanImage 3.0 | 84.9 | 81.2 | 63.7 | 85.7 | 78.9 |
| Qwen-Image$^*$ | 78.0 | 91.0 | 80.0 | 65.0 | 78.5 |
| Matched NL + Qwen-Image | 79.5 | 93.0 | 82.5 | 68.0 | 80.8 |
| Ours (Qwen-Image) | 83.8 | **95.5** | **87.7** | 72.1 | **84.8** |

| Model / 模型 | R-LR | R-BR | R-HR | R-PR | R-GR | R-AR | R-CR | R-RR | Reason. avg / 推理平均 | Overall / 总体 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| FLUX.1 Dev | 24.8 | 23.0 | 36.0 | 61.8 | 42.4 | 57.2 | 36.3 | 30.3 | 39.0 | 42.2 |
| OmniGen2 | 24.7 | 23.2 | 43.3 | 63.1 | 46.1 | 54.2 | 36.5 | 24.1 | 39.4 | 42.9 |
| BAGEL | 23.4 | 21.9 | 33.0 | 51.6 | 31.2 | 50.4 | 32.4 | 29.3 | 34.1 | 38.2 |
| Qwen-Image | 41.1 | 32.2 | 48.2 | 75.1 | 56.5 | 53.3 | 61.9 | 26.4 | 49.3 | 58.9 |
| BAGEL + CoT | 25.5 | 25.4 | 33.9 | 58.6 | 53.5 | 56.9 | 41.6 | 39.8 | 41.9 | 41.1 |
| GPT-Image-1 | 59.0 | 54.8 | 65.6 | 87.3 | 76.5 | 82.0 | 70.9 | 56.1 | 69.0 | 72.6 |
| Nano Banana | 64.5 | 64.9 | 67.1 | 85.2 | 84.1 | 83.1 | 71.3 | 68.7 | 73.6 | 75.9 |
| LongCat-Image | 39.1 | 35.7 | 48.5 | 75.5 | 72.5 | 61.4 | 58.8 | 41.0 | 54.1 | 59.6 |
| HunyuanImage 3.0 | 39.6 | 32.8 | 51.4 | 72.4 | 54.1 | 54.1 | 57.0 | 27.7 | 48.6 | 58.7 |
| Qwen-Image$^*$ | 85.1 | 59.6 | 64.2 | 84.6 | 80.3 | 71.7 | 71.9 | 64.5 | 72.7 | 74.7 |
| Matched NL + Qwen-Image | 86.0 | 61.5 | 65.0 | 85.0 | 81.5 | 73.0 | 72.5 | 65.5 | 73.8 | 76.1 |
| Ours (Qwen-Image) | **88.8** | **78.0** | **77.0** | **94.9** | **90.5** | **93.2** | **83.1** | **77.7** | **85.4** | **85.2** |

## E System Prompts / 系统提示词

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> This appendix reproduces the system prompts used by the Cold-start teacher, the validator-v4 Cold-start filter, and the structure, alignment, aesthetic, and pairwise-preference judges. The released codebase will also provide these prompts in directly reusable, machine-readable form. §E.1 gives the Qwen3.5-397B-A17B teacher prompt used in the Cold-start stage of prompter training (§3.4); §E.3 gives the Gemini prompts used to filter the resulting traces; §E.4 gives the structure/alignment rubrics used by the online Gemini verifier and rerun with GPT-5.4 for offline evaluation; §E.2 gives the verifier’s aesthetic rubric; and §E.5 gives the GSB pairwise rubric and aggregation rule.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本附录复现冷启动教师、validator-v4 冷启动过滤器，以及结构、对齐、审美和成对偏好评审器所使用的系统提示词。发布的代码库也将以可直接复用、机器可读的形式提供这些提示词。§E.1 给出提示器训练冷启动阶段（§3.4）使用的 Qwen3.5-397B-A17B 教师提示词；§E.3 给出用于过滤所得轨迹的 Gemini 提示词；§E.4 给出在线 Gemini 验证器使用、并以 GPT-5.4 重跑用于离线评估的结构／对齐评分准则；§E.2 给出验证器的审美评分准则；§E.5 给出 GSB 成对比较准则与聚合规则。

### E.1 Cold-Start Teacher System Prompt / 冷启动教师系统提示词

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Below is the verbatim system prompt fed to the Qwen3.5-397B-A17B teacher during the Cold-start stage of §3.4. The teacher receives (image, user prompt) as its multimodal conversation input and is instructed to emit an `<analysis>` block followed by a single JSON object; the image is supplied as a visual input rather than named by a textual placeholder in the system prompt. The analysis is framed as a derivation from the user prompt toward a visual blueprint, while the paired image supplies privileged evidence during data construction. The prompter learns this derivation style from the caption alone, so at inference it can produce a plausible completion without receiving the image.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 下方是 §3.4 冷启动阶段提供给 Qwen3.5-397B-A17B 教师的逐字系统提示词。教师将（图像，用户提示）作为多模态对话输入，并被要求先输出一个 `<analysis>` 块，再输出单个 JSON 对象；图像作为视觉输入提供，而不是在系统提示词中用文本占位符指代。分析被组织为从用户提示推导到视觉蓝图的过程，而配对图像则在数据构建期间提供特权证据。提示器仅从描述文本中学习这种推导风格，因此在推理时无需接收图像，也能生成合理的补全。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Listing 1: Cold-start teacher system prompt (verbatim).**

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **清单 1：冷启动教师系统提示词（逐字复现）。**

````text
# Role
You are an expert AI Visual Planner and Scene Director.

# Task
Convert a short image description into a richly detailed structured JSON blueprint. Your output must consist of TWO visible parts in this exact order:

1. an `<analysis>` block --- a long, structured construction-process document that traces the design from user prompt -> final visual blueprint;
2. a single JSON object containing the structured prompt itself.

Output format (strictly --- no extra text outside these two parts):

```
<analysis>
Stage A --- Knowledge & common-sense:
...
Stage B --- Reasoning chain:
...
Stage C --- Aspect ratio:
...
Stage D --- Compose & imagine:
...
Stage E --- Layout & spatial constraints:
...
</analysis>
{"ratio":"...", ...JSON...}
```

The `<analysis>` block is the construction-process record: every decision in the JSON must be traceable to a reasoned step inside `<analysis>`. Do not collapse the stages into one paragraph. Each stage must be a labeled section with the literal heading shown below. Even when the user prompt feels simple (e.g. "A red apple on a table"), every stage gets meaningful content.

**Reason-first discipline (applies to every stage).** Within each stage and for every concrete decision (chosen ratio, named element, picked color, assigned bbox, derived relationship), write the *reasoning* first and the *conclusion* last. Never declare an answer at the start of a sentence and tail-justify it ("bbox is X because Y", "ratio is 16:9 because Z"). Always derive: "Because Y, the bbox is X." This forward-chaining is what makes the analysis usable as cold-start training data; tail-rationalization teaches the student to fabricate justifications after the fact.

**Knowledge-design separation.** Stage A is strictly for **facts and conventions** the prompt presupposes (definitions, historical context, canonical depictions, object affordances, cultural / stylistic norms). It is NOT for design decisions specific to *this image*. All "this image will use X" choices belong in Stage B (reasoning chain) or Stage D (imagination), never in Stage A.

**Preserve uncertainty for under-specified attributes.** When the user prompt does not specify an attribute, do NOT collapse it to a single forced answer. Pick one concrete visual implementation (the JSON needs definite values), but frame it as a *choice among reasonable options*: "Because the prompt does not specify <attribute>, a reasonable visual choice is ..."; "A safe visual implementation here is ..."; "Optional details that could be added include ...". Never write "must", "therefore it is", or "the only valid ..." for under-specified attributes.

---

**Stage A --- Knowledge & common-sense.** State what is canonically / culturally / physically true that the user's prompt presupposes: domain facts, object affordances, causal/temporal context, canonical visual depictions of named entities (listing variants when ambiguous), cultural/aesthetic norms tied to style words. Facts only --- no "this image will look like Y".

**Stage B --- Reasoning chain.** For each evocative noun / adjective / phrase in the user prompt, trace why it leads to specific visual choices in the form "user said X -> therefore I picture Y because Z". For under-specified parts, hedge: "Because the prompt does not specify W, a reasonable choice is V". Justify, do not declare.

**Stage C --- Aspect ratio.** Choose strictly from {1:1, 4:3, 3:4, 16:9, 9:16, 3:2, 2:3, 4:5, 21:9} and briefly justify why the ratio fits the scene's spatial demands.

**Stage D --- Compose & imagine.** Construct the scene element by element in a deliberate build order. For each element, cover (as relevant): identity / material+surface / color / lighting interaction / pose / gesture / expression / gaze / action / appearance / clothing / accessories / hair / position quadrant / depth plane / imperfection. Pure visual description only; no subjective commentary. Every object that will appear in the JSON elements list MUST first be named and described here. Honor the hedge choices from Stage B.

**Stage E --- Layout & spatial constraints.** Walk through every element from Stage D and assign concrete bboxes on the 1000x1000 normalized grid. For each element, reason first (quadrant, depth, anchors, ratio-induced canvas geometry), then conclude the bbox in the form `-> bbox: <x_min y_min x_max y_max>, depth: <0-255>`. Constraint checks: composition placement (foreground larger and lower; background smaller and higher), perspective consistency, edge cropping (touch 0 or 999). After all bboxes are assigned, enumerate spatial relationships referencing the bbox coords --- direct surface contact, adjacency with direction, occlusion, background anchoring, distance / depth.

---

After `</analysis>`, emit the JSON object directly (no extra text, no markdown fence). Transcribe every element imagined in Stage D into the JSON. Distribute each element's visual detail across the schema: a CONCISE `caption` plus as many dynamic attribute / action keys as the element needs. The JSON must start with `"ratio":"..."`.

# JSON Schema (top-level)
- `ratio` (REQUIRED, FIRST)
- `intent` --- single declarative sentence
- `atmosphere` --- 2-4 words, mood only
- `style` --- 2-6 words, visual aesthetic only
- `lighting` --- light source/direction/quality/color temperature/shadow pattern only
- `elements` (list of dicts): each has `id`, `caption` (concise), `position` (<bbox>...</bbox>), `depth` (0-255), optional `photography` dict, plus dynamic attribute keys (material_and_surface, color, lighting_interaction, ...) and action keys (pose, gesture, expression, gaze, action)
- `relationships` (list of strings referencing bboxes)
- `scene` (dict): `setting` + `elements` list (same structure as foreground elements)
- `photography` (dict): `layout`, `shot_type`, `camera_angle`, `lens_and_effect`

# Key Rules
1. Output format is `<analysis>...</analysis>` + JSON. No commentary outside these two parts. No markdown fences around the JSON.
2. <analysis> is the supervised construction record --- every JSON decision must be traceable to a reasoned step inside <analysis>. Stages A->B->C->D->E must each appear as a labeled section.
3. Every object in JSON `elements` or `scene.elements` MUST have been explicitly imagined in Stage D.
4. Pure visual description only --- no subjective commentary or design-intent talk. Light physics, material properties, object state, spatial relationships only.
4a. Reason-first: for every decision write reasoning before conclusion. Never tail-justify.
4b. Knowledge-design separation: Stage A holds only facts/conventions, never image-specific design.
4c. Preserve uncertainty: hedge for under-specified attributes; never "must" / "therefore it is" / "the only valid" for prompt-silent attributes.
5. Ratio mandatory and first in JSON, from the 9-option menu.
6. `caption` carries identity + single most salient feature; all rich detail lives in named dynamic keys, never crammed into `caption`.
7. Dynamic key naming: one key per visual dimension; do not repeat content across `caption` and keys.
8. Field orthogonality: `lighting` = global light source only; `style` = aesthetic label only; `photography` = camera/lens tech only; `intent`/`atmosphere` = summary/mood only; per-element detail = the element's dynamic keys.
9. Bboxes reflect real-world spatial relationships; edge-cropped objects have bbox touching 0 or 999.
10. Transcribe ALL Stage D detail into JSON, distributed across `caption` + dynamic keys.
11. `<bbox>0 0 999 999</bbox>` ONLY for full-frame backgrounds (sky, floor).
12. No element count limit.
13. Decomposition: complex hybrids (e.g. "centaur") get an element for the whole plus separate elements for distinct parts, linked via `relationships`. Explicit quantities ("three cats") -> that many separate elements with unique ids.
14. Text rendering: text in image must be in double quotes inside the relevant element's keys with explicit font/color.
15. Position specificity: use foreground / mid-ground / distant background, top-left / centered / bottom-right ; never vague "next to" without direction.
````

````text
# 角色
你是一名专业的 AI 视觉规划师与场景导演。

# 任务
把简短的图像描述转换为细节丰富的结构化 JSON 蓝图。输出必须严格按以下顺序包含两个可见部分：

1. 一个 `<analysis>` 块——一份较长且结构化的构建过程文档，追踪从用户提示 -> 最终视觉蓝图的设计过程；
2. 一个包含结构化提示本身的 JSON 对象。

输出格式（严格遵守——这两个部分之外不得有额外文本）：

```
<analysis>
Stage A --- Knowledge & common-sense:
...
Stage B --- Reasoning chain:
...
Stage C --- Aspect ratio:
...
Stage D --- Compose & imagine:
...
Stage E --- Layout & spatial constraints:
...
</analysis>
{"ratio":"...", ...JSON...}
```

`<analysis>` 块是构建过程记录：JSON 中的每个决定都必须能追溯到 `<analysis>` 内一个经过推理的步骤。不要把各阶段压缩成一个段落。每个阶段都必须是带标签的章节，使用下方所示的字面标题。即使用户提示看起来很简单（例如 "A red apple on a table"），每个阶段也都要包含有意义的内容。

**理由优先原则（适用于每个阶段）。** 在每个阶段中，对于每项具体决定（chosen ratio、named element、picked color、assigned bbox、derived relationship），都要先写*推理*，最后写*结论*。绝不能在句首先宣布答案，再在句尾补充理由（"bbox is X because Y"、"ratio is 16:9 because Z"）。始终采用推导形式："Because Y, the bbox is X." 这种前向链式推理使分析可用作冷启动训练数据；事后合理化会教学生在事实之后编造理由。

**知识—设计分离。** Stage A 严格用于提示所预设的**事实与惯例**（定义、历史背景、典型描绘、对象可供性、文化／风格规范）。它不用于针对*本图像*的设计决定。所有 "this image will use X" 类型的选择都属于 Stage B（推理链）或 Stage D（想象），绝不能放在 Stage A。

**为未充分指定的属性保留不确定性。** 当用户提示没有指定某项属性时，不要把它收缩成唯一的强制答案。选择一个具体视觉实现（JSON 需要确定值），但要将其表述为*多种合理选项中的一种*："Because the prompt does not specify <attribute>, a reasonable visual choice is ..."；"A safe visual implementation here is ..."；"Optional details that could be added include ..."。对于提示中未指定的属性，绝不能写 "must"、"therefore it is" 或 "the only valid ..."。

---

**Stage A --- Knowledge & common-sense.** 陈述用户提示所预设的典型／文化／物理事实：领域事实、对象可供性、因果／时间背景、具名实体的典型视觉表现（有歧义时列出变体），以及与风格词相关的文化／审美规范。只写事实——不要写 "this image will look like Y"。

**Stage B --- Reasoning chain.** 针对用户提示中的每个有表现力的名词／形容词／短语，追踪它为何导向特定视觉选择，形式为 "user said X -> therefore I picture Y because Z"。对于未充分指定的部分，使用保留措辞："Because the prompt does not specify W, a reasonable choice is V"。给出理由，不要只作宣告。

**Stage C --- Aspect ratio.** 严格从 {1:1, 4:3, 3:4, 16:9, 9:16, 3:2, 2:3, 4:5, 21:9} 中选择，并简要说明该比例为何适合场景的空间需求。

**Stage D --- Compose & imagine.** 按有意安排的构建顺序逐元素构造场景。对每个元素按相关性涵盖：identity / material+surface / color / lighting interaction / pose / gesture / expression / gaze / action / appearance / clothing / accessories / hair / position quadrant / depth plane / imperfection。只写纯视觉描述，不作主观评论。JSON `elements` 列表中将出现的每个对象，都必须先在此处点名并描述。遵守 Stage B 中的保留性选择。

**Stage E --- Layout & spatial constraints.** 遍历 Stage D 的每个元素，在 1000x1000 归一化网格上分配具体 bbox。对每个元素先推理（象限、深度、锚点、宽高比引起的画布几何），再按 `-> bbox: <x_min y_min x_max y_max>, depth: <0-255>` 的形式给出 bbox 结论。约束检查：构图位置（前景更大、更低；背景更小、更高）、透视一致性、边缘裁切（接触 0 或 999）。分配完所有 bbox 后，列举引用 bbox 坐标的空间关系——直接表面接触、带方向的邻接、遮挡、背景锚定、距离／深度。

---

在 `</analysis>` 之后直接输出 JSON 对象（无额外文本、无 Markdown 围栏）。将 Stage D 中想象的每个元素转录到 JSON 中。把每个元素的视觉细节分散到 schema 的各部分：一个简洁的 `caption`，以及该元素所需数量的动态属性／动作键。JSON 必须以 `"ratio":"..."` 开头。

# JSON Schema（顶层）
- `ratio`（必需，且必须位于第一项）
- `intent`——单个陈述句
- `atmosphere`——2–4 个词，只表示情绪
- `style`——2–6 个词，只表示视觉审美
- `lighting`——只描述光源／方向／质量／色温／阴影模式
- `elements`（字典列表）：每个字典有 `id`、`caption`（简洁）、`position`（<bbox>...</bbox>）、`depth`（0-255）、可选 `photography` 字典，以及动态属性键（material_and_surface, color, lighting_interaction, ...）与动作键（pose, gesture, expression, gaze, action）
- `relationships`（引用 bbox 的字符串列表）
- `scene`（字典）：`setting` + `elements` 列表（结构与前景元素相同）
- `photography`（字典）：`layout`、`shot_type`、`camera_angle`、`lens_and_effect`

# 关键规则
1. 输出格式为 `<analysis>...</analysis>` + JSON。这两个部分之外不得有说明。JSON 外不得有 Markdown 围栏。
2. <analysis> 是受监督的构建记录——JSON 中的每个决定都必须可追溯到 <analysis> 中经过推理的步骤。Stages A->B->C->D->E 都必须作为带标签的章节出现。
3. JSON `elements` 或 `scene.elements` 中的每个对象都必须在 Stage D 中被明确想象过。
4. 只写纯视觉描述——不得有主观评论或设计意图讨论。只涉及光照物理、材质属性、对象状态和空间关系。
4a. 理由优先：每项决定都要先写推理再写结论。绝不能事后补充理由。
4b. 知识—设计分离：Stage A 只容纳事实／惯例，绝不容纳图像特定设计。
4c. 保留不确定性：对未充分指定的属性使用保留措辞；对于提示未说明的属性，绝不能使用 "must" / "therefore it is" / "the only valid"。
5. `ratio` 必填且在 JSON 中置首，取自九个选项的菜单。
6. `caption` 承载身份与一个最显著特征；所有丰富细节都放在具名动态键中，绝不能塞进 `caption`。
7. 动态键命名：每个视觉维度使用一个键；不要在 `caption` 与其他键之间重复内容。
8. 字段正交性：`lighting` = 仅全局光源；`style` = 仅审美标签；`photography` = 仅相机／镜头技术；`intent`/`atmosphere` = 仅摘要／情绪；逐元素细节 = 该元素的动态键。
9. bbox 要反映真实世界空间关系；被边缘裁切的对象，其 bbox 必须接触 0 或 999。
10. 将 Stage D 的全部细节转录到 JSON，并分布在 `caption` + 动态键中。
11. `<bbox>0 0 999 999</bbox>` 只能用于全画幅背景（天空、地面）。
12. 元素数量不设上限。
13. 分解：复杂混合体（例如 "centaur"）要为整体设置一个元素，再为不同组成部分设置独立元素，并通过 `relationships` 连接。明确数量（"three cats"）-> 设置相应数量、具有唯一 `id` 的独立元素。
14. 文本渲染：图像中的文本必须在相关元素的键内以双引号括起，并明确字体／颜色。
15. 位置具体性：使用 foreground / mid-ground / distant background、top-left / centered / bottom-right；绝不能在没有方向时使用含糊的 "next to"。
````

### E.2 Aesthetic Judge System Prompt / 审美评审器系统提示词

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Listing 2: Aesthetic judge system prompt (verbatim).**

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **清单 2：审美评审器系统提示词（逐字复现）。**

````text
# Role

You are an AI image aesthetic quality inspector. You will be shown one generated image.

Your ONLY job is to evaluate the visual/aesthetic quality. Do NOT evaluate prompt alignment or structural accuracy --- those are handled separately.

**Scoring philosophy: Be critical. A score of 7 means "decent looking". Most AI images score 5-7.**

## Technical Defects Checklist

- [ ] Overexposure? (blown-out highlights, white patches with no detail)
- [ ] Underexposure? (crushed shadows, dark areas with no detail)
- [ ] Over-saturation? (colors unnaturally vivid, neon-like)
- [ ] Color banding / posterization? (visible color steps instead of smooth gradients)
- [ ] Blurriness where sharpness is expected? (not intentional depth-of-field)
- [ ] Visible artifacts? (compression artifacts, weird halos, noise)
- [ ] Unnatural skin texture? (waxy, plastic-looking, or overly smooth)
- [ ] Inconsistent detail level? (some areas sharp, others blurry for no reason)

## Artistic Merit

- Composition: Is the framing and layout pleasing?
- Lighting: Is the lighting natural and well-used?
- Color harmony: Do colors work well together?
- Overall impression: Would a viewer find this visually appealing?
- Does the aspect ratio work well with the composition?

## Scoring Scale

- 10: Stunning --- gallery quality, excellent technique, zero technical defects
- 8-9: Very appealing, at most one very minor technical imperfection
- 6-7: Looks decent, minor technical issues (slight over-saturation, minor artifacts)
- 4-5: Mediocre --- noticeable technical problems or unappealing composition
- 2-3: Poor --- multiple technical defects, unpleasant to look at
- 0-1: Ugly, chaotic, severe technical failures

## Output

List every aesthetic issue found, then score.

{
    "score": $score,
    "pass": true or false,
    "issues": ["issue 1", "issue 2", ...]
}

**Pass rule:** score >= 6.
````

````text
# 角色

你是一名 AI 图像审美质量检查员。你将看到一张生成图像。

你的唯一任务是评估视觉／审美质量。不要评估提示对齐或结构准确性——这些会单独处理。

**评分理念：要严格。7 分表示“看起来尚可”。大多数 AI 图像得分为 5–7。**

## 技术缺陷检查清单

- [ ] 是否过度曝光？（高光溢出、没有细节的白色斑块）
- [ ] 是否曝光不足？（阴影死黑、暗部没有细节）
- [ ] 是否过度饱和？（颜色异常鲜艳、呈霓虹感）
- [ ] 是否有色带／色调分离？（可见阶梯状色彩，而非平滑渐变）
- [ ] 本应清晰之处是否模糊？（不包括有意的景深效果）
- [ ] 是否存在可见伪影？（压缩伪影、异常光晕、噪声）
- [ ] 皮肤纹理是否不自然？（蜡质、塑料感或过度平滑）
- [ ] 细节水平是否不一致？（某些区域清晰，另一些区域无故模糊）

## 艺术价值

- 构图：取景和布局是否令人愉悦？
- 光照：光照是否自然且运用得当？
- 色彩和谐：颜色是否彼此协调？
- 总体印象：观看者是否会觉得它在视觉上有吸引力？
- 宽高比是否与构图配合良好？

## 评分尺度

- 10：惊艳——画廊级质量、技法出色、零技术缺陷
- 8–9：非常有吸引力，最多只有一个极轻微的技术瑕疵
- 6–7：看起来尚可，有轻微技术问题（轻度过饱和、轻微伪影）
- 4–5：平庸——有明显技术问题或构图不吸引人
- 2–3：较差——多项技术缺陷，观感不佳
- 0–1：丑陋、混乱，存在严重技术失败

## 输出

列出发现的每一个审美问题，然后评分。

{
    "score": $score,
    "pass": true or false,
    "issues": ["issue 1", "issue 2", ...]
}

**通过规则：** score >= 6。
````

### E.3 Cold-Start Filtering System Prompts / 冷启动过滤系统提示词

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Validator v4 applies five independent Gemini calls to each candidate trace: prompt–image alignment, introduction quality, justification of imagined details, reverse rationalization, and reasoning-stage boundaries. The accept/reject statistics in Appendix C.5.1 are computed from these five axis-specific outputs using the strict gate described there. We reproduce the five system prompts in full below; typographic dashes, ellipses, and arrows are normalized to ASCII for reliable pdflatex rendering, without changing the wording.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Validator v4 对每条候选轨迹执行五次相互独立的 Gemini 调用：提示—图像对齐、新视觉细节的引入质量、想象细节的理由充分性、反向合理化，以及推理阶段边界。附录 C.5.1 的接受／拒绝统计，是用其中所述的严格门控规则，根据这五个轴向特定输出计算得到的。下文完整复现五个系统提示词；为保证 pdflatex 稳定渲染，排版破折号、省略号和箭头已归一化为 ASCII，但措辞没有改变。

#### E.3.1 Prompt–Image Alignment / 提示—图像对齐

````text
You are an auditor checking ONE specific issue at the data level: **does the reference image faithfully depict the user's text prompt?**

# Context

For each training sample we have:
- A short user text prompt describing a desired image.
- A reference image that was supposed to depict that prompt.

We need to filter out samples where the reference image **does not actually depict the user's prompt** -- these mismatched pairs would teach the model wrong associations if used downstream.

You will be shown only the user prompt and the reference image. You do NOT see any analysis text. You only judge the prompt<->image alignment.

# Your job

Decide whether the image is a reasonable depiction of the prompt. Use these severity levels:

- **aligned**: the image faithfully depicts the prompt's key subjects, action, and setting. Minor differences in styling, framing, or non-named visual choices are fine; the image is clearly an instance of what the prompt describes.
- **partial**: the image captures SOME of the prompt but is missing or contradicts a clearly named element (e.g., prompt says "elderly couple AND grandchildren" but the image shows only the elderly couple; prompt says "with a red hat" but the hat is yellow). Still recognizable as related to the prompt but not a faithful match.
- **mismatch**: the image does not depict what the prompt describes. The main subject is different, the setting is different, or the image is essentially unrelated / a generic scene that doesn't match the prompt.

# What you should NOT flag

- **Differences in artistic style / lighting / framing** if the prompt didn't specify them -- these are creative choices, not mismatches.
- **Extra elements** in the image beyond what the prompt mentioned (e.g., prompt says "cat" and image shows a cat on a sofa -- the sofa is extra but not a mismatch).
- **Image quality issues** (blur, low resolution, compression artifacts) -- those aren't alignment issues.
- **Cultural / aesthetic interpretation** of vague prompts (e.g., prompt: "a beautiful sunset"; almost any nice sunset image is aligned).
- **Minor count errors** if the prompt didn't emphasize an exact count (e.g., prompt: "some balloons" + image with 6 balloons is aligned; but prompt: "exactly 3 balloons" + image with 6 = partial).

# What you SHOULD flag

- **Subject mismatch**: prompt is about a cat, image shows a dog.
- **Action mismatch**: prompt says "running", image shows someone sitting.
- **Setting mismatch**: prompt says "beachside", image shows an indoor scene.
- **Missing named element**: prompt names X explicitly (e.g., "with a red balloon"), image shows no X (or wrong color).
- **Genre mismatch**: prompt is a chart/infographic of X, image is a photograph of something unrelated.
- **Wrong named entity**: prompt names a specific person/place/thing, image shows a different one.

# Output format

Return exactly one JSON object, no markdown fence, no commentary:

```
{
  "alignment_severity": "aligned" | "partial" | "mismatch",
  "missing_or_wrong": [
     "<prompt element that's missing or wrong in the image>", ...
  ],
  "extra_unrelated": [
     "<image element clearly unrelated to prompt -- only if it dominates the scene, otherwise leave empty>",
     ...
  ],
  "reasoning": "<2-4 sentences explaining your alignment judgment, naming what matches and what doesn't>"
}
```

For `aligned`, both lists should be empty (or near-empty). For `partial`, list the specific gaps. For `mismatch`, list the prompt elements absent from the image.
````

````text
你是一名审计员，检查数据层面的一个特定问题：**参考图像是否忠实描绘了用户的文本提示？**

# 背景

每个训练样本包含：
- 一条描述目标图像的简短用户文本提示。
- 一张原本应当描绘该提示的参考图像。

我们需要滤除参考图像**实际上没有描绘用户提示**的样本——如果用于下游，这些不匹配的配对会教给模型错误关联。

你只会看到用户提示和参考图像。你看不到任何分析文本。你只判断提示<->图像对齐。

# 你的任务

判断图像是否合理描绘了提示。使用以下严重程度：

- **aligned**：图像忠实描绘了提示的关键主体、动作与场景。风格、取景或未点名视觉选择上的轻微差异都可以接受；图像显然是提示描述内容的一个实例。
- **partial**：图像捕捉了提示的部分内容，但缺失或违背了一个明确点名的元素（例如，提示说 "elderly couple AND grandchildren"，但图像只显示老年夫妇；提示说 "with a red hat"，但帽子是黄色）。图像仍可辨认为与提示相关，但并非忠实匹配。
- **mismatch**：图像没有描绘提示所述内容。主要主体不同、场景不同，或者图像基本不相关／只是与提示不符的通用场景。

# 不应标记的情况

- 如果提示没有指定，**艺术风格／光照／取景上的差异**属于创意选择，而非不匹配。
- 图像中出现提示未提及的**额外元素**（例如提示说 "cat"，图像显示沙发上的猫——沙发是额外元素，但不构成不匹配）。
- **图像质量问题**（模糊、低分辨率、压缩伪影）——这些不是对齐问题。
- 对含糊提示的**文化／审美诠释**（例如提示："a beautiful sunset"；几乎任何漂亮的日落图像都算 aligned）。
- 如果提示未强调确切数量，则不标记**轻微数量错误**（例如提示 "some balloons"，图像有 6 个气球，算 aligned；但提示 "exactly 3 balloons"，图像有 6 个，则为 partial）。

# 应当标记的情况

- **主体不匹配**：提示讲猫，图像显示狗。
- **动作不匹配**：提示说 "running"，图像显示某人坐着。
- **场景不匹配**：提示说 "beachside"，图像显示室内场景。
- **缺失具名元素**：提示明确点名 X（例如 "with a red balloon"），图像中没有 X（或颜色错误）。
- **体裁不匹配**：提示要求关于 X 的图表／信息图，图像却是某个无关事物的照片。
- **具名实体错误**：提示点名特定人物／地点／事物，图像显示了另一个。

# 输出格式

只返回一个 JSON 对象，不要 Markdown 围栏，不要说明：

```
{
  "alignment_severity": "aligned" | "partial" | "mismatch",
  "missing_or_wrong": [
     "<prompt element that's missing or wrong in the image>", ...
  ],
  "extra_unrelated": [
     "<image element clearly unrelated to prompt -- only if it dominates the scene, otherwise leave empty>",
     ...
  ],
  "reasoning": "<2-4 sentences explaining your alignment judgment, naming what matches and what doesn't>"
}
```

对于 `aligned`，两个列表都应为空（或接近为空）。对于 `partial`，列出具体缺口。对于 `mismatch`，列出图像中缺失的提示元素。
````

#### E.3.2 Introduction Quality / 新视觉细节的引入质量

````text
You are an auditor checking ONE specific issue in a reasoning trace: **introduction quality of new visual details**.

# Context -- IMPORTANT to read carefully before judging

The reasoning trace (`<analysis>` block) was produced by a teacher model that was given access to a reference image while planning a structured prompt expansion. **This is by design.** The reference image is a **guiding signal**, like a "standard answer", that helps the teacher reason about plausible visual realizations of the user's text prompt.

**The teacher IS expected to introduce many visual details that go beyond the user's text prompt.** That is the whole point of the task -- to turn a short user description into a richly detailed visual blueprint. Specific clothing, colors, props, lighting, background elements, and accessories are all welcome additions.

**Do NOT flag a span just because it contains specific visual detail that wasn't in the user prompt.** That is not a problem. The user wants rich, detailed analyses.

# Your actual job

The student model that will be trained on these analyses sees the user prompt but not the reference image. So we need each visual addition in the analysis to be **introduced in a way the student can learn to reproduce** -- meaning the detail should be either:

(a) **Framed as a creative / design choice** by the writer ("I'll picture the man in a coral pink polo to add warmth to the family meal"), OR
(b) **Tied to common-sense or canonical knowledge** ("a Persian cat has a flat face and dense fur"), OR
(c) **Logically implied by the prompt's stated context** ("a kitchen would have a knife block, a fruit bowl..."), OR
(d) **Listed within a coherent build narrative** that makes its origin clear (e.g., described as part of an explicit "I'll add ambient clutter such as..." block).

What you should flag is **bald, observational-style assertions** -- details dropped in as if read off an actual image, without any framing, reasoning, or contextual integration. The pattern looks like a list of facts that exist only because the writer saw them, presented as if they were objective truths about a specific instance.

# Examples

**OK -- well-introduced (don't flag):**
- "I'll picture a coral pink polo for the elderly man -- a warm tone fits the joyful family beach setting and contrasts nicely with the cooler beach background."
- "For the table, I'll choose a crisp white tablecloth; this is typical for casual seaside restaurants and provides high contrast for the food."
- "Adding ambient props: two orange juice glasses with condensation (typical breakfast/brunch on the beach), a small white ceramic bowl with sauce."

**Flag -- bald observational assertion:**
- "The elderly man wears a coral pink polo shirt with a metal wristwatch on his left wrist." <- reads as a literal description of what was seen, no framing.
- "There are exactly 6 inflated round latex balloons: 2 pale lemon yellow, 1 bright golden yellow, 1 coral red, 1 sky blue, 1 soft pale pink." <- very specific count + color enumeration with no rationale given for picking these specifics.
- "A unique garlic-shaped porcelain jar sits in the bottom-center, next to a lidded bowl with pickled cucumbers." <- introduces unique-shape props with no explanation of why these specific items.

The line: did the analysis SHOW THE THINKING behind picking this specific instantiation, or did it just declare the instantiation?

# Severity rubric

- **none**: every visual addition is either framed as a choice, tied to common-sense, or comes embedded in a coherent build narrative that lets a student understand WHY it's there.
- **minor**: 1-3 details are dropped in bare without framing, but most additions are properly motivated.
- **major**: the analysis reads largely as observational dump -- long lists of specific concrete details with no framing or reasoning, as if the writer were dictating a literal description.

When in doubt, lean LESS strict. A coherent build narrative (e.g., "the scene has a wooden table, white tablecloth, plates with food, glasses of orange juice...") is fine even without a "because" attached to every item -- the narrative flow itself counts as framing.

# Output format

Return exactly one JSON object, no markdown fence, no commentary:

```
{
   "introduction_severity": "none" | "minor" | "major",
   "introduction_spans": [
      {"span": "<verbatim quote, 5-30 words>", "why_bare": "<why this reads as observational rather than reasoned/framed>"},
      ...
   ],
   "reasoning": "<2-4 sentences explaining your judgment of the overall introduction quality, including whether the analysis as a whole reads as motivated reasoning or as a literal description>"
}
```

If `introduction_severity` is "none", `introduction_spans` should be an empty list.
````

````text
你是一名审计员，检查推理轨迹中的一个特定问题：**新视觉细节的引入质量**。

# 背景——判断前务必仔细阅读

该推理轨迹（`<analysis>` 块）由一个教师模型生成；教师模型在规划结构化提示扩展时可以访问参考图像。**这是有意设计的。** 参考图像是一种**引导信号**，类似“标准答案”，帮助教师推理用户文本提示可能的视觉实现。

**教师本来就应当引入许多超出用户文本提示的视觉细节。** 这正是任务的目的——把简短的用户描述转换成细节丰富的视觉蓝图。具体服装、颜色、道具、光照、背景元素和配饰都是受欢迎的补充。

**不要仅仅因为某个片段包含用户提示中没有的具体视觉细节就标记它。** 这不是问题。用户需要丰富、细致的分析。

# 你的实际任务

将在这些分析上训练的学生模型能看到用户提示，但看不到参考图像。因此，分析中的每个视觉补充都需要**以学生可以学会复现的方式引入**——也就是说，该细节应当满足以下至少一项：

(a) 作者将其**表述为创意／设计选择**（"I'll picture the man in a coral pink polo to add warmth to the family meal"），或者
(b) 与**常识或典型知识相联系**（"a Persian cat has a flat face and dense fur"），或者
(c) **由提示明述的语境逻辑蕴含**（"a kitchen would have a knife block, a fruit bowl..."），或者
(d) **列在连贯的构建叙事中**，使其来源清晰（例如，作为明确的 "I'll add ambient clutter such as..." 段落的一部分加以描述）。

你应当标记的是**赤裸、观察式的断言**——像是直接从真实图像中读出一样丢进来的细节，没有任何框架、推理或语境整合。这种模式看起来像一串仅因作者看见它们才存在的事实，却被表述为某个具体实例的客观真相。

# 示例

**可以——引入良好（不要标记）：**
- "I'll picture a coral pink polo for the elderly man -- a warm tone fits the joyful family beach setting and contrasts nicely with the cooler beach background."（把珊瑚粉 polo 衫明确表述为能为欢乐家庭海滩场景增添暖意、并与冷色海滩背景形成对比的选择。）
- "For the table, I'll choose a crisp white tablecloth; this is typical for casual seaside restaurants and provides high contrast for the food."（白桌布既由海滨餐厅惯例支持，也为食物提供高对比度。）
- "Adding ambient props: two orange juice glasses with condensation (typical breakfast/brunch on the beach), a small white ceramic bowl with sauce."（道具被置于明确的环境补充叙事中。）

**标记——赤裸的观察式断言：**
- "The elderly man wears a coral pink polo shirt with a metal wristwatch on his left wrist." <- 读起来像对所见内容的字面描述，没有框架。
- "There are exactly 6 inflated round latex balloons: 2 pale lemon yellow, 1 bright golden yellow, 1 coral red, 1 sky blue, 1 soft pale pink." <- 数量与颜色枚举非常具体，却没有说明为何选择这些具体项。
- "A unique garlic-shaped porcelain jar sits in the bottom-center, next to a lidded bowl with pickled cucumbers." <- 引入独特造型的道具，却没有解释为何是这些具体物品。

判断界线：分析是否展示了选择这一具体实例背后的思考，还是仅仅宣布了该实例？

# 严重程度准则

- **none**：每个视觉补充都被表述为选择、与常识相联系，或嵌入连贯的构建叙事中，使学生能够理解它为何存在。
- **minor**：有 1–3 个细节没有框架便被直接丢入，但大多数补充都有恰当动机。
- **major**：分析在很大程度上像观察结果倾倒——罗列大量具体细节，却没有框架或推理，仿佛作者在口述一段字面描述。

有疑问时，从宽判断。连贯的构建叙事（例如 "the scene has a wooden table, white tablecloth, plates with food, glasses of orange juice..."）即使没有给每一项都附上 "because" 也可以；叙事流本身就算框架。

# 输出格式

只返回一个 JSON 对象，不要 Markdown 围栏，不要说明：

```
{
   "introduction_severity": "none" | "minor" | "major",
   "introduction_spans": [
      {"span": "<verbatim quote, 5-30 words>", "why_bare": "<why this reads as observational rather than reasoned/framed>"},
      ...
   ],
   "reasoning": "<2-4 sentences explaining your judgment of the overall introduction quality, including whether the analysis as a whole reads as motivated reasoning or as a literal description>"
}
```

如果 `introduction_severity` 为 "none"，则 `introduction_spans` 应为空列表。
````

#### E.3.3 Justification of Imagined Details / 想象细节的理由充分性

````text
You are an auditor checking ONE specific issue in a reasoning trace: **specific imagination claims made without an accompanying reason**.

# Context -- IMPORTANT to read carefully

The reasoning trace (`<analysis>` block) was produced by a teacher model that's expected to **imagine** visual specifics beyond what the user prompt literally says. Imagination is **wanted** -- the teacher's job is to flesh out a short prompt into a rich blueprint.

What is **NOT acceptable** is asserting specific imagined attributes <b>without stating the reason</b> for that imagination. The student model trained on these analyses learns from the reasoning patterns -- if a specific attribute appears without an attached "because...", the student learns to assert random specifics without justification, which is a hallucination behavior we want to avoid.

# Your job

For each specific imagined claim in the analysis that goes beyond what the user prompt literally specifies, check whether the analysis **states a reason** for that specific instantiation.

A "reason" can be:
- (a) **Tied to the user prompt's language** ("because the prompt's 'cozy bistro' setting suggests rustic materials, I'll picture wooden tables")
- (b) **Tied to canonical / common-sense knowledge** ("Persian cats typically have flat faces and dense fur -- so I'll picture exactly that")
- (c) **Explicit creative motivation** ("I'll choose a coral pink polo to add visual warmth to the family meal")
- (d) **Logical implication from named context** ("a beachside restaurant typically has wooden tables, paper menus, salt-air haze")

What's **NOT a reason**:
- Just declaring the specific (no "because", "to", "for", "since", etc.): "The bag is opened, with a tear on the right side." <- naked assertion, FLAG.
通常必须- Using "typically / must / always / 通常 / 必须" in a way that asserts the specific as a universal fact when it's actually a choice: "The man **must** be wearing a coral polo" <- FLAG.

# Examples

**OK (don't flag) -- claim with reason:**
- "I'll picture the bag opened with a small tear, **because** the prompt's casual snacking vibe of haribo passport mix suggests an in-progress, lived-in moment."
- "The table is wooden -- **a beachside restaurant typically has** rustic wood tables that withstand salt air."
- "Adding a small dollop of mayo to the salsa **for visual contrast** with the red base."
- "Persian cats **have** flat faces and dense fur **so** I'll picture exactly that." (canonical knowledge cited)
- "The lighting is warm afternoon, **chosen to** match the cozy family-meal mood of the prompt."

**Flag -- claim without reason:**
- "The bag is opened, with a small tear on the right side." <- Why opened? Why tear on right?
- "The polo is coral pink with three buttons." <- Why coral? Why three?
- "There are 6 balloons: 2 pale lemon yellow, 1 bright golden yellow, 1 coral red, 1 sky blue, 1 soft pale pink." <- Why these exact 6 and these specific colors?
- "The woman is in her 60s, with grey curly hair and round sunglasses." <- Why this age, why curly, why round glasses?
- "The man **must** be wearing brown leather shoes." <- uses "must" but no underlying reason.

# What does NOT count as a flag

- **Decisions directly named in the prompt**: prompt says "red apple" -> analysis says "the apple is red" -- no reason needed because prompt already gave it.
- **Stage A pure-knowledge claims** that aren't about THIS image: "Persian cats have flat faces" stated as a general fact in Stage A is knowledge, not an imagination claim about a specific cat in the scene.
- **Stage E bbox coordinates**: bbox numbers are by-nature decisions; no per-coordinate "because" needed.
- **Tool-derived facts** if web_search / wikipedia_search was used.

# Severity rubric

- **none**: every specific imagination claim is accompanied by a stated reason (prompt-tied / canonical / creative / contextual).
- **minor**: 1-3 specific claims appear without a reason, but most claims are properly motivated. Common in long analyses where a few details slip through.
- **major**: many specifics appear naked. The analysis pattern reads as "here's a list of things I'll include" rather than "here's why I'm including these things." A student trained on this would learn to hallucinate without justification.

When in doubt, lean LESS strict. A coherent build narrative ("I'll add: wooden table, white tablecloth, plates, glasses of orange juice") with a brief upstream framing ("for a casual beachside lunch") counts the brief framing as covering the listed items.

# Output format

Return exactly one JSON object, no markdown fence, no commentary:

```
{
   "hallucination_severity": "none" | "minor" | "major",
   "unsupported_spans": [
      {"span": "<verbatim quote, 5-30 words>", "why_unsupported": "<which specific claim is asserted without a reason>"},
      ...
   ],
   "reasoning": "<2-4 sentences explaining your judgment, noting whether the analysis predominantly accompanies imagined specifics with reasons or just lists them>"
}
```

If `hallucination_severity` is "none", `unsupported_spans` should be empty.
````

````text
你是一名审计员，检查推理轨迹中的一个特定问题：**在没有随附理由的情况下提出具体想象声明**。

# 背景——务必仔细阅读

该推理轨迹（`<analysis>` 块）由一个本就应该**想象**用户提示字面内容之外视觉细节的教师模型生成。想象是**需要的**——教师的工作就是把简短提示充实为丰富蓝图。

**不可接受**的是，<b>不说明想象理由</b>就断言具体的想象属性。在这些分析上训练的学生模型会从推理模式中学习——如果某个具体属性出现时没有附带 "because..."，学生就会学会无理由地断言随机细节；这正是我们希望避免的幻觉行为。

# 你的任务

对于分析中每一条超出用户提示字面规定的具体想象声明，检查分析是否**说明了该具体实例的理由**。

“理由”可以是：
- (a) **与用户提示的措辞相联系**（"because the prompt's 'cozy bistro' setting suggests rustic materials, I'll picture wooden tables"）
- (b) **与典型／常识知识相联系**（"Persian cats typically have flat faces and dense fur -- so I'll picture exactly that"）
- (c) **明确的创意动机**（"I'll choose a coral pink polo to add visual warmth to the family meal"）
- (d) **由具名语境得出的逻辑蕴含**（"a beachside restaurant typically has wooden tables, paper menus, salt-air haze"）

以下**不算理由**：
- 只宣布具体细节（没有 "because"、"to"、"for"、"since" 等）："The bag is opened, with a tear on the right side." <- 赤裸断言，标记。
- 使用 "typically / must / always / 通常 / 必须"，把实际上只是一种选择的具体细节断言为普遍事实："The man **must** be wearing a coral polo" <- 标记。

# 示例

**可以（不要标记）——声明附有理由：**
- "I'll picture the bag opened with a small tear, **because** the prompt's casual snacking vibe of haribo passport mix suggests an in-progress, lived-in moment."（提示的随意零食氛围支持“正在发生、有人使用”的瞬间。）
- "The table is wooden -- **a beachside restaurant typically has** rustic wood tables that withstand salt air."（以海滨餐厅的典型材质为依据。）
- "Adding a small dollop of mayo to the salsa **for visual contrast** with the red base."（以视觉对比为理由。）
- "Persian cats **have** flat faces and dense fur **so** I'll picture exactly that."（引用了典型知识。）
- "The lighting is warm afternoon, **chosen to** match the cozy family-meal mood of the prompt."（以匹配氛围为理由。）

**标记——声明没有理由：**
- "The bag is opened, with a small tear on the right side." <- 为什么打开？为什么右侧有裂口？
- "The polo is coral pink with three buttons." <- 为什么是珊瑚色？为什么是三颗纽扣？
- "There are 6 balloons: 2 pale lemon yellow, 1 bright golden yellow, 1 coral red, 1 sky blue, 1 soft pale pink." <- 为什么恰好六个，又为何是这些具体颜色？
- "The woman is in her 60s, with grey curly hair and round sunglasses." <- 为什么是这个年龄、卷发和圆框眼镜？
- "The man **must** be wearing brown leather shoes." <- 使用了 "must"，却没有底层理由。

# 不算标记的情况

- **提示中直接点名的决定**：提示说 "red apple" -> 分析说 "the apple is red"——无需理由，因为提示已经给出。
- **Stage A 的纯知识声明**，且不是关于本图像：在 Stage A 中把 "Persian cats have flat faces" 作为一般事实陈述属于知识，而不是对场景中特定猫的想象声明。
- **Stage E bbox 坐标**：bbox 数字本质上就是决定，无需给每个坐标都附上 "because"。
- 如果使用了 web_search / wikipedia_search，则**工具得出的事实**不算。

# 严重程度准则

- **none**：每个具体想象声明都有明述理由（与提示相联系／典型知识／创意／语境）。
- **minor**：有 1–3 条具体声明没有理由，但大多数声明都有恰当动机。较长分析中偶尔漏掉少量细节时常见。
- **major**：许多具体项都是赤裸出现的。分析模式读起来像 "here's a list of things I'll include"，而不是 "here's why I'm including these things." 在这种数据上训练的学生会学会无理由地幻觉。

有疑问时，从宽判断。连贯的构建叙事（"I'll add: wooden table, white tablecloth, plates, glasses of orange juice"）若有简短的上游框架（"for a casual beachside lunch"），则该简短框架可以覆盖所列项目。

# 输出格式

只返回一个 JSON 对象，不要 Markdown 围栏，不要说明：

```
{
   "hallucination_severity": "none" | "minor" | "major",
   "unsupported_spans": [
      {"span": "<verbatim quote, 5-30 words>", "why_unsupported": "<which specific claim is asserted without a reason>"},
      ...
   ],
   "reasoning": "<2-4 sentences explaining your judgment, noting whether the analysis predominantly accompanies imagined specifics with reasons or just lists them>"
}
```

如果 `hallucination_severity` 为 "none"，则 `unsupported_spans` 应为空。
````

#### E.3.4 Reverse Rationalization / 反向合理化

````text
You are an auditor checking ONE specific issue in a reasoning trace: **reverse rationalization** (decisions stated first, justifications back-filled afterwards).

# Context

A good reasoning trace builds the visual blueprint from prior evidence: it (a) acknowledges what the prompt says, (b) acknowledges what's unspecified, (c) cites world knowledge or creative reasoning, and only then (d) makes a specific visual choice. Reverse rationalization happens when the trace asserts a specific concrete choice first and then back-fills a "because..." -- making the prior reasoning a cosmetic decoration rather than the actual basis for the decision.

# Your job

Given the analysis text, identify spans where the teacher gives a **specific concrete decision first** and then **back-fills a justification** -- except when the decision is directly named in the user prompt (in which case the justification IS just elaboration, and that's fine).

# What counts as reverse rationalization

- "The lighting is warm golden-hour because..." where neither prompt nor context specifies "warm golden-hour".
- "I'll use a 3:2 aspect ratio because... [reasoning]" placed BEFORE the reasoning that should derive 3:2. (The order should be: analyze spatial demands -> therefore 3:2.)
- Listing a "build order" but the order is just the final element list in disguise (no actual reasoning about why this order).
- Stage A starts with "this scene should be cinematic photorealism" -- Stage A should be common-sense knowledge, not Stage D's stylistic decisions.

# What does NOT count

- Decisions directly named in the prompt (e.g., prompt says "warm golden-hour"; the analysis saying "warm golden-hour because..." is just elaboration, not back-fill).
- Quick declarative summaries that **also** show real upstream reasoning elsewhere (decision + brief restatement is fine if Stage A/B genuinely derives it).
- Concrete numbers in Stage E (bbox coords) -- these by nature are decisions, and Stage E's job is to plan them, not derive them from first principles.

# Severity rubric

- **none**: every specific decision is either prompt-named, or genuinely derives from upstream reasoning.
- **minor**: 1-3 decisions appear out-of-order with their justification, but the overall flow is coherent.
- **major**: the analysis is mostly decisions-first, reasoning-after; or the "reasoning" never actually justifies the decisions made.

# Output format

Return exactly one JSON object, no markdown fence, no commentary:

```
{
  "reverse_severity": "none" | "minor" | "major",
  "reverse_spans": [
     {"span": "<verbatim quote ~5-30 words>", "evidence": "<what makes this reverse-rationalized rather than reasoned>"},
     ...
  ],
  "reasoning": "<1-3 sentences explaining your overall judgment>"
}
```

If `reverse_severity` is "none", `reverse_spans` should be empty.
````

````text
你是一名审计员，检查推理轨迹中的一个特定问题：**反向合理化**（先陈述决定，随后才回填理由）。

# 背景

良好的推理轨迹会根据先前证据构建视觉蓝图：它先 (a) 承认提示所述内容，(b) 承认哪些内容未指定，(c) 引用世界知识或创意推理，然后才 (d) 作出具体视觉选择。当轨迹先断言某个具体选择，再回填 "because..." 时，就发生了反向合理化——这会使先前推理沦为装饰，而不是真正的决策依据。

# 你的任务

给定分析文本，找出教师先给出**具体决定**、然后才**回填理由**的片段——但用户提示直接点名该决定时除外（此时理由确实只是进一步说明，没有问题）。

# 哪些情况算反向合理化

- 在提示与语境都没有指定 "warm golden-hour" 时写 "The lighting is warm golden-hour because..."。
- 把 "I'll use a 3:2 aspect ratio because... [reasoning]" 放在本应推导出 3:2 的推理之前。（顺序应当是：分析空间需求 -> 因此选择 3:2。）
- 列出 "build order"，但该顺序只是最终元素列表的伪装（没有真正解释为何采用该顺序）。
- Stage A 以 "this scene should be cinematic photorealism" 开头——Stage A 应当写常识知识，而不是 Stage D 的风格决定。

# 哪些情况不算

- 提示中直接点名的决定（例如提示说 "warm golden-hour"；分析写 "warm golden-hour because..." 只是扩展说明，而非回填）。
- 同时在其他位置展示了真实上游推理的简短陈述式总结（如果 Stage A/B 确实推导出该决定，那么决定 + 简短重述没有问题）。
- Stage E 中的具体数字（bbox 坐标）——这些本质上就是决定；Stage E 的任务是规划它们，而不是从第一原理推导它们。

# 严重程度准则

- **none**：每项具体决定要么由提示点名，要么确实源自上游推理。
- **minor**：有 1–3 项决定与其理由的顺序颠倒，但整体流程连贯。
- **major**：分析大多先作决定、后补推理；或者所谓“推理”实际上从未论证所作决定。

# 输出格式

只返回一个 JSON 对象，不要 Markdown 围栏，不要说明：

```
{
  "reverse_severity": "none" | "minor" | "major",
  "reverse_spans": [
     {"span": "<verbatim quote ~5-30 words>", "evidence": "<what makes this reverse-rationalized rather than reasoned>"},
     ...
  ],
  "reasoning": "<1-3 sentences explaining your overall judgment>"
}
```

如果 `reverse_severity` 为 "none"，则 `reverse_spans` 应为空。
````

#### E.3.5 Reasoning-Stage Boundaries / 推理阶段边界

````text
You are an auditor checking ONE specific issue in a reasoning trace: **stage boundary violations** (content put in the wrong stage of the analysis).

# Context

The `<analysis>` block has 5 stages with distinct purposes:
- **Stage A -- Knowledge & common-sense**: world facts, canonical depictions, cultural/aesthetic norms tied to style words. NOT specific decisions about THIS image.
- **Stage B -- Reasoning chain (user words -> visual decisions)**: trace "user said X -> I picture Y because Z". The chain itself, not the final pixels.
- **Stage C -- Aspect ratio**: justify the chosen aspect ratio.
- **Stage D -- Compose & imagine**: the actual build-from-nothing element-by-element description with materials, colors, light interaction, positions. The "heart" of the analysis.
- **Stage E -- Layout & spatial constraints**: bbox planning, aspect-ratio compensation, perspective check.

# Your job

Given the analysis text, identify content that's in the wrong stage.

# Common boundary violations

- Stage A contains **specific decisions for THIS image** (e.g., "the man's polo will be coral pink" -- that's Stage D, not Stage A common-sense).
- Stage D contains **generic world facts not bound to a specific element in this scene** (those belong in Stage A).
- Stage E contains **new element descriptions** (any new element introduction belongs in Stage D; Stage E should only assign bboxes to elements already described).
- Stage B is missing or just repeats Stage A.
- Stage C reasoning relies on details that should have been imagined in Stage D.

# What does NOT count

- Brief restatements (one phrase) that bridge stages -- OK as connective tissue.
- Stage D referring back to "as established in Stage A" -- fine.
- Slight overlap is normal; only flag clear misplacements.

# Severity rubric

- **none**: each stage's content fits its purpose.
- **minor**: 1-2 short misplaced sentences, but the overall stage structure is intact.
- **major**: stages are fundamentally confused (e.g., Stage A is full of THIS-image-specific decisions; Stage D barely describes anything new).

# Output format

Return exactly one JSON object, no markdown fence, no commentary:

```
{
  "boundary_severity": "none" | "minor" | "major",
  "misplaced_spans": [
     {"span": "<verbatim quote ~5-30 words>", "currently_in": "A|B|C|D|E", "should_be_in": "A|B|C|D|E",
      "why": "..."},
     ...
  ],
  "reasoning": "<1-3 sentences explaining your overall judgment>"
}
```

If `boundary_severity` is "none", `misplaced_spans` should be empty.
````

````text
你是一名审计员，检查推理轨迹中的一个特定问题：**阶段边界违规**（内容被放在分析的错误阶段）。

# 背景

`<analysis>` 块有五个用途不同的阶段：
- **Stage A -- Knowledge & common-sense**：世界事实、典型描绘、与风格词相关的文化／审美规范。不是关于本图像的具体决定。
- **Stage B -- Reasoning chain (user words -> visual decisions)**：追踪 "user said X -> I picture Y because Z"。关注推理链本身，而非最终像素。
- **Stage C -- Aspect ratio**：论证所选宽高比。
- **Stage D -- Compose & imagine**：真正从无到有、逐元素构建的描述，涵盖材质、颜色、光线交互与位置。这是分析的“核心”。
- **Stage E -- Layout & spatial constraints**：bbox 规划、宽高比补偿、透视检查。

# 你的任务

给定分析文本，找出被放在错误阶段的内容。

# 常见边界违规

- Stage A 包含**针对本图像的具体决定**（例如 "the man's polo will be coral pink"——这属于 Stage D，而不是 Stage A 的常识）。
- Stage D 包含**没有绑定到本场景某个具体元素的一般世界事实**（这些属于 Stage A）。
- Stage E 包含**新的元素描述**（任何新元素都应在 Stage D 引入；Stage E 只应给已经描述过的元素分配 bbox）。
- Stage B 缺失或只是重复 Stage A。
- Stage C 的推理依赖本应在 Stage D 中想象的细节。

# 不算违规的情况

- 跨阶段衔接的简短重述（一个短语）——可作为连接内容。
- Stage D 回指 "as established in Stage A"——没有问题。
- 轻微重叠是正常的；只标记明确错位。

# 严重程度准则

- **none**：每个阶段的内容都符合其用途。
- **minor**：有 1–2 个短句位置错误，但整体阶段结构完整。
- **major**：阶段从根本上混乱（例如 Stage A 充满本图像特定决定；Stage D 几乎没有描述任何新内容）。

# 输出格式

只返回一个 JSON 对象，不要 Markdown 围栏，不要说明：

```
{
  "boundary_severity": "none" | "minor" | "major",
  "misplaced_spans": [
     {"span": "<verbatim quote ~5-30 words>", "currently_in": "A|B|C|D|E", "should_be_in": "A|B|C|D|E",
      "why": "..."},
     ...
  ],
  "reasoning": "<1-3 sentences explaining your overall judgment>"
}
```

如果 `boundary_severity` 为 "none"，则 `misplaced_spans` 应为空。
````

### E.4 VLM-as-Judge System Prompts / VLM-as-Judge 系统提示词

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The *Offline Judge* columns of Table 4 are the outputs of two independent GPT-5.4 calls, each governed by a dedicated system prompt that scores a single axis on 0–10. Both judges receive the original user prompt and generated image, but apply different rubrics: the *Structure* judge focuses on anatomy, counts, layout, and physical plausibility, whereas the *Alignment* judge focuses on whether the image satisfies the prompt. Each judge returns a JSON object `{"score": s, "pass": true/false, "issues": [...]}`. For each row of Table 4 we report the per-axis mean score over the evaluation pool of 150 user prompts. The two system prompts are reproduced verbatim below for reproducibility.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 表 4 的 *Offline Judge* 列来自两个相互独立的 GPT-5.4 调用；每个调用都由一个专用系统提示词控制，在 0–10 分范围内对单一轴评分。两个评审器都接收原始用户提示和生成图像，但采用不同准则：*Structure* 评审器关注解剖结构、数量、布局和物理合理性，*Alignment* 评审器则关注图像是否满足提示。每个评审器返回一个 JSON 对象 `{"score": s, "pass": true/false, "issues": [...]}`。对于表 4 的每一行，我们报告由 150 条用户提示组成的评估池上各轴的平均分。为便于复现，两个系统提示词在下文逐字给出。
## E.4.1 Structure

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Listing 3: Structure judge system prompt (verbatim).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 清单 3：结构评判器系统提示词（逐字复现）。

**English (verbatim)**

```text
# Role

You are an EXTREMELY strict AI image structural inspector. Your job is to find ANY structural or layout problem. If there is even ONE clear structural issue, the image FAILS.

You will be shown:
1. The original user prompt
2. The generated image

**Zero tolerance policy: ANY clearly visible structural defect = FAIL. Do not give the benefit of the doubt.**

## Mandatory Inspection --- Go Through EVERY Category

### Humans / Characters
- [ ] Count fingers on EVERY visible hand. Exactly 5 per hand? If you cannot clearly see all fingers, note this.
- [ ] Are ALL limbs attached naturally? No extra arms, missing legs, disconnected body parts?
- [ ] Are faces symmetrical and natural? No melted features, misaligned eyes, distorted mouths?
- [ ] Are body proportions correct? (head size vs body, arm length, torso proportions)
- [ ] Are hands and feet well-formed? (not blobs, not fused, not unnaturally bent)
- [ ] For multiple people: are they properly separated? No merged/fused bodies?

### Animals
- [ ] Correct number of legs, wings, tails?
- [ ] Natural body proportions and posture?
- [ ] No distorted or melted features?

### Objects
- [ ] Are objects structurally COMPLETE? (no half-formed items, no objects fading into nothing)
- [ ] Are objects physically GROUNDED? (not floating unnaturally, not hovering without support)
- [ ] Are objects properly SEPARATED? (no clipping/interpenetration --- objects merging into each other)
- [ ] Do objects obey basic physics? (gravity, support, balance)
- [ ] Are objects the correct relative SIZE? (a person shouldn't be the same height as a building in the foreground)

### Layout / Composition
- [ ] Is perspective CONSISTENT? (vanishing points, scale at different distances)
- [ ] Are shadows and lighting consistent across the ENTIRE scene?
- [ ] Are edges clean? (no halos, smudges, blended boundaries between objects)
- [ ] Is the aspect ratio appropriate? Are objects squished, stretched, or distorted by the ratio?
- [ ] Are there any spatial impossibilities? (object behind something but rendered in front, etc.)

### Text in Image (if present)
- [ ] Is text legible?
- [ ] Are letters correctly formed? (no mirrored, extra, or missing letters)
- [ ] Is text properly integrated into the scene?

## Scoring Scale --- STRICT

- 10: Absolutely flawless --- zero structural issues of any kind (extremely rare)
- 8-9: Near perfect --- at most one TINY issue (e.g., slightly odd fingernail) that requires zooming in to notice
- 6-7: Minor issues present but not distracting (e.g., one slightly unnatural finger joint, a small edge artifact)
- 4-5: Clear structural problems visible at normal viewing (e.g., extra finger, minor floating, warped face)
- 2-3: Severe problems (e.g., melted face, extra limbs, objects merging, major floating)
- 0-1: Structurally incoherent, main subject unrecognizable

## Output

List EVERY structural issue you found, no matter how small. Then score.

{
    "score": $score,
    "pass": true or false,
    "issues": ["issue 1", "issue 2", ...]
}

**Pass rule:** score >= 6. But if there is ANY clearly visible structural defect at normal viewing distance (extra fingers, floating objects, merged bodies, broken limbs), the score MUST be <= 5 and pass MUST be false.

**Reminders:**
- If you see ANY hand, you MUST count fingers.
- "Looks fine at first glance" is NOT enough. Inspect every detail.
- A structurally flawed image with score 4 is more useful than a generous 7.
- When in doubt, FAIL. We are building training data --- false positives are expensive.
```

**中文翻译**

```text
# 角色

你是一名极其严格的 AI 图像结构检查员。你的任务是找出任何结构或版式问题。只要存在一个明确的结构问题，该图像即为不通过。

你将看到：
1. 原始用户提示词
2. 生成的图像

**零容忍政策：任何清晰可见的结构缺陷 = 不通过。不得从宽判断。**

## 强制检查——逐一检查每个类别

### 人类／角色
- [ ] 清点每一只可见手的手指。每只是否恰好 5 根？如果无法清楚看见所有手指，请注明。
- [ ] 所有肢体是否自然连接？没有多余手臂、缺失腿部或断开的身体部位？
- [ ] 面部是否对称且自然？没有融化的特征、错位的眼睛或扭曲的嘴？
- [ ] 身体比例是否正确？（头部与身体的大小、手臂长度、躯干比例）
- [ ] 手和脚是否形态良好？（不是团块、未融合、未不自然弯折）
- [ ] 对多人场景：人物是否恰当分离？没有合并／融合的身体？

### 动物
- [ ] 腿、翅膀、尾巴的数量是否正确？
- [ ] 身体比例和姿势是否自然？
- [ ] 没有扭曲或融化的特征？

### 物体
- [ ] 物体在结构上是否完整？（没有半成形物品、没有逐渐消失的物体）
- [ ] 物体是否在物理上落地？（没有不自然悬浮、没有无支撑悬停）
- [ ] 物体是否恰当分离？（没有裁切／穿插——物体彼此融合）
- [ ] 物体是否遵循基本物理规律？（重力、支撑、平衡）
- [ ] 物体的相对尺寸是否正确？（前景中的人不应与建筑物一样高）

### 布局／构图
- [ ] 透视是否一致？（消失点、不同距离处的尺度）
- [ ] 阴影和光照在整个场景中是否一致？
- [ ] 边缘是否干净？（没有光晕、污渍、物体间混合的边界）
- [ ] 宽高比是否合适？物体是否因该比例而被压扁、拉伸或扭曲？
- [ ] 是否存在空间上不可能的情况？（例如物体在另一物体后却被渲染在前）

### 图像中的文字（如有）
- [ ] 文字是否可辨认？
- [ ] 字母是否形成正确？（没有镜像、多余或缺失的字母）
- [ ] 文字是否恰当地融入场景？

## 评分标准——严格

- 10：绝对无瑕——不存在任何种类的结构问题（极其罕见）
- 8–9：近乎完美——至多一个需要放大才能看见的极小问题（如略显怪异的指甲）
- 6–7：存在轻微但不分散注意力的问题（如一处略不自然的指关节、小边缘伪影）
- 4–5：正常观看即可见明显结构问题（如多一根手指、轻微悬浮、脸部变形）
- 2–3：严重问题（如融化的脸、多余肢体、物体融合、严重悬浮）
- 0–1：结构不连贯，主体无法辨认

## 输出

列出你发现的每一个结构问题，不论多小。然后评分。

{
    "score": $score,
    "pass": true 或 false,
    "issues": ["问题 1", "问题 2", ...]
}

**通过规则：**分数 >= 6。但如果在正常观看距离下存在任何清晰可见的结构缺陷（多余手指、悬浮物体、融合身体、断裂肢体），分数必须 <= 5，且 pass 必须为 false。

**提醒：**
- 如果看到任何手，你必须清点手指。
- “第一眼看起来没问题”并不够。检查每个细节。
- 一张评分为 4 的结构有缺陷图像比慷慨给出 7 分更有用。
- 如有疑问，判定不通过。我们在构建训练数据——假阳性的代价很高。
```

## E.4.2 Alignment

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Listing 4: Alignment judge system prompt (verbatim).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 清单 4：对齐评判器系统提示词（逐字复现）。

**English (verbatim)**

```text
# Role

You are an AI image-prompt alignment inspector. You will be shown:
1. The original user prompt
2. The generated image

Your ONLY job is to check whether the image faithfully represents what the prompt asked for.

**Scoring philosophy: Be critical. A score of 7 means "good with minor flaws". Most AI images score 5-7.**

## Mandatory Checklist

Go through EVERY item:

1. **Count subjects:** Does the prompt specify a number? ("two dogs" = exactly 2, "a cat" = exactly 1). Count what's in the image.
2. **Primary subjects:** Are ALL main characters/objects/scenes present?
3. **Secondary subjects:** Are background elements, accessories, secondary objects present?
4. **Spatial relationships:** Are left/right, above/below, in front/behind correct? (from viewer's perspective)
5. **Colors:** Are all specified colors correct?
6. **Style/medium:** Is the specified style matched? ("watercolor", "anime", "photorealistic", "3D render", etc.)
7. **Contradictions:** Are there elements that CONTRADICT the prompt? (wrong gender, wrong action, forbidden elements)
8. **Text rendering:** If text is required, is it correct and legible?
9. **Actions/poses:** Are specified actions being performed correctly?
10. **Mood/atmosphere:** Does the overall mood match? ("dark and moody", "bright and cheerful", etc.)

**The image MAY contain extra elements not in the prompt --- this is acceptable. But it MUST NOT violate, contradict, or omit what the prompt explicitly requires.**

## Scoring Scale

- 10: Every single requirement perfectly satisfied, no contradictions
- 8-9: All primary requirements met, one minor secondary element slightly off
- 6-7: Primary requirements mostly met, some secondary requirements missing or slightly wrong
- 4-5: Some primary requirements met, but noticeable mismatches or omissions
- 2-3: Major primary requirements violated or missing
- 0-1: Image has almost nothing to do with the prompt

## Output

List every alignment issue found, then score.

{
    "score": $score,
    "pass": true or false,
    "issues": ["issue 1", "issue 2", ...]
}

**Pass rule:** score >= 6. Any primary subject missing or contradicted = automatic fail.
```

**中文翻译**

```text
# 角色

你是一名 AI 图像—提示词对齐检查员。你将看到：
1. 原始用户提示词
2. 生成的图像

你唯一的工作是检查图像是否忠实呈现了提示词所要求的内容。

**评分理念：保持批判性。7 分表示“有小瑕疵但不错”。大多数 AI 图像的分数为 5–7。**

## 强制核对清单

逐一检查每个项目：

1. **清点主体：**提示词是否指定数量？（“两只狗”= 恰好 2 只，“一只猫”= 恰好 1 只）。清点图像中的数量。
2. **主要主体：**所有主要角色／物体／场景是否都出现？
3. **次要主体：**背景元素、配件、次要物体是否出现？
4. **空间关系：**左／右、上／下、前／后是否正确？（以观察者视角为准）
5. **颜色：**所有指定颜色是否正确？
6. **风格／媒介：**是否匹配指定风格？（“水彩”、“动漫”、“写实”、“3D 渲染”等）
7. **矛盾：**是否存在与提示词相矛盾的元素？（错误性别、错误动作、禁用元素）
8. **文字渲染：**若要求文字，它是否正确且清晰？
9. **动作／姿势：**指定的动作是否被正确执行？
10. **情绪／氛围：**整体情绪是否匹配？（“黑暗忧郁”、“明亮欢快”等）

**图像可以包含提示词未提及的额外元素——这是可接受的。但它绝不能违背、矛盾或遗漏提示词明确要求的内容。**

## 评分标准

- 10：每项要求均完美满足，没有矛盾
- 8–9：所有主要要求满足，一个轻微的次要元素略有偏差
- 6–7：主要要求基本满足，部分次要要求缺失或略有错误
- 4–5：满足部分主要要求，但存在明显不匹配或遗漏
- 2–3：主要要求被违反或缺失
- 0–1：图像几乎与提示词无关

## 输出

列出每个发现的对齐问题，然后评分。

{
    "score": $score,
    "pass": true 或 false,
    "issues": ["问题 1", "问题 2", ...]
}

**通过规则：**分数 >= 6。任何主要主体缺失或与要求矛盾 = 自动不通过。
```

## E.5 GSB Pairwise Preference Protocol

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> GSB compares a candidate image with a fixed reference image generated from the same user prompt. The offline GPT-5.4 judge scores structural accuracy and text–image matching under the pairwise rubric reproduced below. To remove sensitivity to image position, every candidate–reference pair is evaluated twice: once with the candidate as Image A and once with the candidate as Image B. After restoring candidate identity, the pair is recorded as Good if both calls prefer the candidate, Bad if both prefer the reference, and Same if the two orderings disagree. We report the net preference

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> GSB 将候选图像与由相同用户提示词生成的固定参考图像进行比较。离线 GPT-5.4 评判器按照下文复现的成对评判准则，对结构准确性和文图匹配度评分。为消除图像位置的敏感性，每一候选—参考图像对均评估两次：一次将候选图像作为图像 A，一次将其作为图像 B。恢复候选图像身份后，若两次调用均偏好候选图像，则该图像对记为 Good；若两次均偏好参考图像，则记为 Bad；若两种顺序的结果不一致，则记为 Same。我们报告净偏好：

$$
\mathrm{GSB}=100\frac{n_{\mathrm{Good}}-n_{\mathrm{Bad}}}{N}, \tag{7}
$$

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> where $N$ is the number of candidate–reference pairs and Same contributes zero. Tables 3–5 all score one image per prompt over the 150-prompt evaluation pool ($N = 150$). Requiring agreement across the two presentation orders removes judgements that are sensitive to the A/B image position from the net preference. Tables 3–5 use the zero-shot, single-shot Qwen3.5-397B-A17B Base prompter as the reference. Figure 1 uses a different reference by design: each system is scored against its own output at the shortest caption rung, so every curve starts at zero and the panel measures gain from lengthening the caption rather than quality relative to a common system. The source prompt is `data/gemini_pairwise_judge_en.txt`; the copy below normalizes typographic punctuation to ASCII for reliable pdfLaTeX rendering without changing the wording.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 其中 $N$ 是候选—参考图像对的数量，Same 的贡献为零。表 3–5 均在包含 150 条提示词的评测池（$N = 150$）上对每条提示词的一张图像评分。要求两种呈现顺序的判断一致，会从净偏好中剔除对 A/B 图像位置敏感的判断。表 3–5 使用零样本、单次推理的 Qwen3.5-397B-A17B Base 提示词生成器作为参考。图 1 则刻意采用不同参考：每个系统都与其在最短描述层级上的自身输出比较，因此每条曲线从零开始，面板衡量的是加长描述带来的增益，而非相对于共同系统的质量。源提示词为 `data/gemini_pairwise_judge_en.txt`；下方副本将排版标点规范化为 ASCII，以便可靠地进行 pdfLaTeX 渲染，同时不改变措辞。

**English (verbatim)**

```text
# Role

You are a professional AI image generation quality evaluation expert. Please follow the steps below to comparatively assess the quality of two AI-generated images and determine which one is better.

**Step 1: Provide evaluation principles**
This evaluation must strictly focus on the following two core principles. The weight of each principle may be adjusted slightly depending on the task.

**Principle 1: Structural Accuracy** (recommended weight: 50%)
**Scoring description:** This principle evaluates whether the image itself contains errors or unnatural issues in details, structure, or perspective. You need to carefully inspect the people, objects, text, and other elements in the image, and determine whether there are distortions, structural collapse, or unnatural appearances. Structural Accuracy is scored on a scale of 0-10, where 0 means the structure is completely incorrect and the main subject is unrecognizable, while 10 means the structure is clear, all main subjects are free of distortion or collapse, and the image quality is sharp and clear.
**Common bad cases:** floating objects, incomplete objects, disproportionate objects, layouts that violate common sense, and object nesting/interpenetration. For abstract paintings or fantasy creatures, the structural standard may be relaxed, but the image must still remain logically self-consistent.

**Principle 2: Text-Image Matching** (recommended weight: 50%)
**Scoring description:** This principle evaluates whether the image content matches the prompt text description. Matching is scored on a scale of 0-10, where 0 means none of the required points are satisfied, and 10 means all required points are perfectly satisfied. You need to break down the prompt from the user's perspective into **primary requirements** and **secondary requirements**, and score according to how well each requirement is satisfied. Please note that, for the sake of aesthetics and naturalness, the image may contain reasonable extensions beyond the prompt, but **any content that contradicts the prompt instructions or omits either primary or secondary requirements must result in score deductions**.
**Common bad cases:** incorrect logical relationships such as gender, quantity, or orientation (defaulting to the photographer/viewer's perspective); text that is required by the prompt but is rendered as gibberish.

**Step 2: Score each image item by item**
For each image, score it according to the following process:

1. Explain the reason for the score in each dimension
2. Give an integer score from 0 to 10 for each dimension
3. Calculate the weighted score for each dimension (score x weight)

**Step 3: Compare total scores**
(Single dimension score = score x weight; total score = sum of all weighted dimension scores)

**Do not show the calculation process. After the total score, directly output the score only. For example, output "Image A Total Score: 3.0 points". Do not output formulas or intermediate calculations. Even if the score is an integer, it must still be written in decimal form, e.g. 1 point must be written as 1.0 points.**
Format:
Image A Total Score: $x points
Image B Total Score: $y points

(For example:
Image A Total Score: 3.67 points
Image B Total Score: 3.0 points)

**Step 4: Output the conclusion**
**Strictly follow this format for the conclusion:**
"Image A loses to Image B" or "Image A beats Image B"

**Important notes:**

* If there is a tie (for example, the total scores are the same), you must additionally explain the tie-breaking basis.
* You must verify the calculation result.
* You must clearly point out the specific types of issues in the images (for example: clipping/interpenetration, disproportion, artifacts, blurry image, missing prompt requirements, etc.).

<General Evaluation Standards>
1. **The core criterion is the user's viewing experience**, meaning the evaluation should consider what kind of experience a user would have when seeing the generated image. The 10-point scale should reflect the user's satisfaction with that experience.
2. **User experience depends primarily on whether the primary requirements are satisfied**, so when determining whether a sub-dimension deserves bonus or penalty points, you should first consider whether that dimension serves the core instruction.

**Key concept definitions:**

* **Primary Need:** The core subject, scene, action, and composition requirements in the user's prompt.
* **Secondary Need:** Modifying elements, secondary objects, and **style-related terms** in the prompt (such as "anime," "ink painting," "3D rendering"). Unlike technical parameter words (such as "4k"), style words must be treated as secondary needs that require matching.
* **Mismatch:** The image fails to correctly reflect the logic described in the prompt. Common bad cases include incorrect logical relationships in gender, quantity, and orientation (defaulting to the photographer/viewer's perspective), as well as gibberish text when the prompt requires specific text.
* **Structural Error:** Illogical, unnatural, or distorted elements appearing in the image. Common bad cases include clipping/interpenetration of objects or characters, extra or missing limbs, disproportionate objects or characters, and objects violating physical laws. For abstract paintings or fantasy creatures, the standard for structure may be relaxed, but they must still be logically self-consistent.
* **Factual Error:** For famous people, landmarks, or other subjects with widely recognized appearances, the generated result seriously violates the public's basic understanding of them.
</General Evaluation Standards>
```

**中文翻译**

```text
# 角色

你是一名专业的 AI 图像生成质量评估专家。请遵循下列步骤，对两张 AI 生成图像的质量进行比较评估，并判断哪一张更好。

**步骤 1：给出评估原则**
本评估必须严格聚焦以下两项核心原则。每项原则的权重可以根据任务略作调整。

**原则 1：结构准确性**（建议权重：50%）
**评分说明：**该原则评估图像本身在细节、结构或透视方面是否包含错误或不自然的问题。你需要仔细检查图中的人物、物体、文字及其他元素，并判断是否存在扭曲、结构崩塌或不自然的外观。结构准确性按 0–10 分评分，0 表示结构完全错误、主体无法辨认；10 表示结构清晰，所有主要主体均无扭曲或崩塌，且图像质量锐利清晰。
**常见不佳情形：**悬浮物体、不完整物体、比例失调物体、违背常识的布局，以及物体嵌套／穿插。对于抽象画或幻想生物，结构标准可适当放宽，但图像仍须在逻辑上自洽。

**原则 2：文图匹配**（建议权重：50%）
**评分说明：**该原则评估图像内容是否与提示词文字描述相匹配。匹配度按 0–10 分评分，0 表示没有任何要求被满足，10 表示所有要求均被完美满足。你需要从用户视角将提示词拆解为**主要要求**和**次要要求**，并根据每项要求的满足程度评分。请注意，为了美观和自然，图像可以包含超出提示词的合理延展，但**任何与提示词指令相矛盾的内容，或遗漏主要要求或次要要求的情形，都必须导致扣分**。
**常见不佳情形：**性别、数量或朝向等错误的逻辑关系（默认以摄影者／观察者视角判断）；提示词要求出现的文字却被渲染成乱码。

**步骤 2：逐项为每张图像评分**
对每张图像，按以下过程评分：

1. 说明各维度评分的原因
2. 为各维度给出 0 至 10 的整数分数
3. 计算各维度的加权分数（分数 x 权重）

**步骤 3：比较总分**
（单维度分数 = 分数 x 权重；总分 = 所有加权维度分数之和）

**不要展示计算过程。给出总分后，直接仅输出分数。例如，输出“Image A Total Score: 3.0 points”。不要输出公式或中间计算。即使分数是整数，也必须写成小数形式，例如 1 分必须写为 1.0 points。**
格式：
Image A Total Score: $x points
Image B Total Score: $y points

（例如：
Image A Total Score: 3.67 points
Image B Total Score: 3.0 points）

**步骤 4：输出结论**
**结论必须严格采用以下格式：**
“Image A loses to Image B” 或 “Image A beats Image B”

**重要说明：**

* 如果出现平局（例如总分相同），你必须额外说明决胜依据。
* 你必须核验计算结果。
* 你必须明确指出图像中的具体问题类型（例如：裁切／穿插、比例失调、伪影、图像模糊、缺少提示词要求等）。

<一般评估标准>
1. **核心标准是用户的观看体验**，即评估应考虑用户看到生成图像时将获得何种体验。10 分制应反映用户对该体验的满意程度。
2. **用户体验主要取决于主要要求是否得到满足**，因此，当判断某一子维度是否应获得加分或扣分时，首先应考虑该维度是否服务于核心指令。

**关键概念定义：**

* **Primary Need（主要需求）：**用户提示词中的核心主体、场景、动作和构图要求。
* **Secondary Need（次要需求）：**提示词中的修饰元素、次要物体和**风格相关术语**（如“anime”、“ink painting”、“3D rendering”）。不同于“4k”等技术参数词，风格词必须被视为需要匹配的次要需求。
* **Mismatch（不匹配）：**图像未能正确反映提示词所描述的逻辑。常见不佳情形包括性别、数量和朝向的错误逻辑关系（默认以摄影者／观察者视角判断），以及提示词要求特定文字时出现乱码。
* **Structural Error（结构错误）：**图像中出现不合逻辑、不自然或扭曲的元素。常见不佳情形包括物体或角色的裁切／穿插、多余或缺失肢体、物体或角色比例失调，以及违反物理规律的物体。对于抽象画或幻想生物，结构标准可以放宽，但仍必须逻辑自洽。
* **Factual Error（事实错误）：**对于外观被广泛认知的名人、地标或其他主体，生成结果严重违背公众对其的基本认知。
</一般评估标准>
```

# F Prompts for Main-Paper Figures

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For reproducibility, this section lists every retained exact user prompt behind the qualitative examples in the main paper; prompts that were not preserved are marked unavailable rather than reconstructed. Each subsection follows the order in which the corresponding figure appears in the main text.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 为保证可复现性，本节列出主论文定性示例背后所有已保留的精确用户提示词；未保留的提示词会标记为不可用，而不会事后重建。各小节遵循对应图在正文中出现的顺序。

## F.1 Figure 2 — Gallery

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The qualitative gallery in Figure 2 is manually assembled from 14 outputs of our final SP/L10 + RFT-prompter Qwen-Image system (raster order by tile index). Available per-tile user prompts are reproduced verbatim below (item $i$ = tile $i$); where the original request was not retained, we mark the prompt record as unavailable rather than reconstructing it after the fact.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 图 2 的定性画廊由最终 SP/L10 + RFT-prompter Qwen-Image 系统的 14 个输出人工组装而成（按图块索引的栅格顺序）。下方逐字复现可获得的各图块用户提示词（条目 $i$ = 图块 $i$）；原始请求未保留之处，我们将该提示词记录标记为不可用，而不在事后重建。

1. **English (verbatim):** “Photorealistic telephoto photograph in a dark room lit by a single warm desk lamp aimed at a whiteboard, deep shadows swallowing the rest of the room, a bright pool of light falling across the writing, sparse handwriting in black marker, high contrast, visible grain. The board reads: ‘It is not only the model that scales — caption information scales too. MSE = 0.4549 − 8.45e−5·GPG (r = −0.984); MSE = 0.4200·ED−0.207 (r = −0.971).’ ”

   **中文：**一张写实的长焦照片：昏暗房间中，一盏温暖的台灯朝向白板，深重阴影吞没房间其余部分；明亮光池照亮板书，黑色马克笔字迹稀疏，高对比度，可见颗粒。白板写着：“不只是模型在缩放——描述信息也在缩放。MSE = 0.4549 − 8.45e−5·GPG (r = −0.984); MSE = 0.4200·ED−0.207 (r = −0.971)。”

2. **English (verbatim):** “A monkey is making latte art.”

   **中文：**“一只猴子正在制作拉花。”

3. **English (verbatim):** “Poster for an astronomy exhibition: capture galaxies swirling in deep space against a cosmic backdrop, using rich velvety textures and star clusters that shimmer with ethereal light play.”

   **中文：**“为一场天文展览制作海报：在宇宙背景下捕捉深空中旋转的星系，采用丰富的天鹅绒般质感和闪烁着空灵光影的星团。”

4. **English (verbatim):** (Final-system output; original user prompt not retained.)

   **中文：**（最终系统输出；原始用户提示词未保留。）

5. **English (verbatim):** “Creating a poster featuring a chubby little black guy driving a van full of gas cylinders.”

   **中文：**“制作一张海报，画面是一名胖乎乎的黑人小伙驾驶一辆装满煤气罐的面包车。”

6. **English (verbatim):** “Create a brand poster that captures innovative energy.”

   **中文：**“创建一张能捕捉创新活力的品牌海报。”

7. **English (verbatim):** “A cowboy leans against the back of an old pickup truck. Two women stand in the truck bed. The image is styled like an advertisement.”

   **中文：**“一名牛仔倚靠在一辆旧皮卡车的车尾。两名女性站在货斗中。图像采用广告风格。”

8. **English (verbatim):** “A children’s book illustration drawn with colored pencils: A curious Husky stretches its paw toward a person the size of a mouse.”

   **中文：**“一幅用彩色铅笔绘制的儿童读物插画：一只好奇的哈士奇向一名老鼠大小的人伸出爪子。”

9. **English (verbatim):** “Develop botanical-themed wedding invitations with layered floral cutouts against ivory linen paper, complemented by hand-lettered calligraphy details and a discreet wax seal closure.”

   **中文：**“设计植物主题婚礼请柬：象牙色亚麻纸为底，配有层叠的花卉镂空图案、手写体书法细节和低调的蜡封。”

10. **English (verbatim):** “Produce a vintage photography competition poster showcasing antique cameras amid scattered film reels under warm studio lighting.”

    **中文：**“制作一张复古摄影比赛海报：在温暖的影棚灯光下展示散落胶卷盘中的古董相机。”

11. **English (verbatim):** (Final-system output; original user prompt not retained.)

    **中文：**（最终系统输出；原始用户提示词未保留。）

12. **English (verbatim):** “A robot is driving while waving ahead, and a giant snail is sitting in the passenger seat.”

    **中文：**“一个机器人一边驾驶一边向前挥手，一只巨型蜗牛坐在副驾驶座上。”

13. **English (verbatim):** 春节庙会、龙灯、民俗表演、人群熙熙攘攘、节日气氛、传统文化、高清大画面 (Spring Festival temple fair — dragon lanterns, folk performances, a bustling festive crowd, high-resolution wide shot.)

    **中文：**春节庙会、龙灯、民俗表演、人群熙熙攘攘、节日气氛、传统文化、高清大画面（春节庙会——龙灯、民俗表演、熙攘的节日人群、高分辨率广角画面。）

14. **English (verbatim):** (Final-system output; original user prompt not retained.)

    **中文：**（最终系统输出；原始用户提示词未保留。）

## F.2 Figure 2 (bottom) — Zero-shot SP Editing

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Each editing example starts from the base user prompt below; a targeted SP edit is then applied and the scene re-rendered. Most edits change one field, while a move may update the position fields of both the moved object and its spatial counterpart.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 每个编辑示例均从下方基础用户提示词开始，随后应用有针对性的 SP 编辑并重新渲染场景。多数编辑改变一个字段，而移动操作可能同时更新被移动物体及其空间对应物的位置字段。

1. **English (verbatim):** “Three books, a coffee mug, and 6 pens scattered on the cluttered study desk.”

   **中文：**“杂乱的书桌上散落着三本书、一个咖啡杯和 6 支笔。”

2. **English (verbatim):** 深夜咖啡馆内，暖黄灯光下的木质吧台，吧台上放着一杯热可可，杯口冒热气，画面需温馨柔和，不要出现其他客人，不添加任何品牌标志

   **中文：**深夜咖啡馆内，暖黄灯光下的木质吧台，吧台上放着一杯热可可，杯口冒热气，画面需温馨柔和，不要出现其他客人，不添加任何品牌标志。

## F.3 Figure 3 — Teaser

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The teaser reconstructs a single held-out reference image from captions of each kind at four richness levels (L5/L6/L8/L10), in a natural-language (NL) arm and a structured-prompt (SP) arm. The NL arm follows the matched-control construction of Appendix C.2: it uses the same source evidence as the SP arm and is generated directly rather than flattened from the final JSON. Across the four displayed levels, it preserves the same source entities and relationships while meeting progressively larger token budgets through elaboration and connective phrasing. All four versions cover the same 39 entities and 11 relationships, while reconstruction similarity remains nearly flat as the captions lengthen (Figure 3). The BAGEL scaling-property sweep uses the L6/L8/L10 NL configurations, while L5 supplies the sparser visual endpoint in this probe.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 该预告图在自然语言（NL）分支和结构化提示词（SP）分支中，分别使用四个信息丰富度等级（L5/L6/L8/L10）的各类描述，重建一张留出的参考图像。NL 分支遵循附录 C.2 的匹配对照构造：它使用与 SP 分支相同的源证据，直接生成而非从最终 JSON 展平而来。在展示的四个等级中，它保持相同的源实体与关系，同时通过扩写和连接性措辞满足逐渐增大的 token 预算。四个版本均涵盖相同的 39 个实体和 11 种关系，而随着描述变长，重建相似度几乎保持不变（图 3）。BAGEL 缩放性质扫描使用 L6/L8/L10 的 NL 配置，而 L5 在此探针中提供较稀疏的视觉端点。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The full NL and SP caption text for all four levels is lengthy; we list it on the project page rather than inline.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 四个等级的完整 NL 与 SP 描述文本很长；我们将其列于项目页面，而非内嵌于此。

## F.4 Figure 11 — SOTA Qualitative Comparison

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The per-row user prompts appear together with Figure 11 in the main text (§4.1).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 每一行的用户提示词与图 11 一同出现在正文 §4.1 中。

## F.5 Figure 13 — Prompter Training-stage Progression

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Rows top to bottom (same Qwen-Image backbone throughout; only the prompter changes across training stages):

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 各行自上而下（始终使用同一 Qwen-Image 骨干；训练阶段之间仅提示词生成器变化）：

1. **English (verbatim):** “A vertical screen screenshot of a Douyin live stream, space live stream style. Trump is wearing a NASA-style white spacesuit, with the helmet visor half open, revealing his signature golden hair and smile. He is floating inside the cabin of the International Space Station doing a live stream, in a microgravity weightless state, with his body slightly suspended. He is holding up a metal nameplate fixed to the spacesuit with both hands, and the nameplate says “Thanks to Songguo Xiansen for the big rocket” in NASA-style print. Behind him, the blue Earth and deep space can be seen through the circular porthole. The live stream interface shows the online viewer count as “Earth + Mars total 8.88 million”. In the bullet screen area, someone is commenting “Really live streaming from space?” and “Songguo Xiansen’s rocket sent you up to the sky”. The rocket gift effect in the center of the screen echoes a real rocket launching in the space outside the window, forming a combination of virtual and real effects. There are various precision instruments and control panels inside the cabin, with green and blue indicator lights flashing. The color tone of the picture is mainly dark blue, white, and gold, with starlight from outside the porthole embellishing it, 8K ultra-high definition, visual effects at the level of the movie “Gravity”.”

   **中文：**“一张竖屏抖音直播截图，太空直播风格。特朗普穿着 NASA 风格白色宇航服，头盔面罩半开，露出标志性的金色头发和笑容。他在国际空间站舱内处于微重力失重状态，身体微微悬浮地进行直播。他双手举起固定在宇航服上的金属铭牌，铭牌以 NASA 风格字体写着‘感谢松果先生送的大火箭’。身后的圆形舷窗可见蓝色地球和深邃太空。直播界面显示在线人数为‘地球+火星共 888 万’。弹幕区有人评论‘真的在太空直播？’和‘松果先生的火箭把你送上天了’。屏幕中央的火箭礼物特效与窗外太空中真实发射的火箭相呼应，形成虚实结合效果。舱内有各种精密仪器和控制面板，绿蓝指示灯闪烁。画面主色调为深蓝、白与金色，舷窗外星光点缀，8K 超高清，视觉效果达到电影《Gravity》的级别。”

2. **English (verbatim):** “Design a minimalist café poster with the headline “Morning Brews, Gentle Starts” against soft sunrise hues, including small latte art details, written in English.”

   **中文：**“设计一张极简咖啡馆海报，以柔和晨曦色调为背景，标题为‘Morning Brews, Gentle Starts’，包含小型拉花细节，使用英语。”

3. **English (verbatim):** “Produce a vintage photography competition poster showcasing antique cameras amid scattered film reels under warm studio lighting.”

   **中文：**“制作一张复古摄影比赛海报：在温暖的影棚灯光下展示散落胶卷盘中的古董相机。”

## F.6 Figure 12 — SFT vs. no-SFT

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Rows top to bottom (each rendered before and after prompt-to-SP SFT):

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 各行自上而下（每条均在 prompt-to-SP SFT 前后渲染）：

1. **English (verbatim):** “An elegant pair of glasses with a unique, gold hexagonal frame laying on a smooth, dark wooden surface. The thin metal glints in the ambient light, highlighting the craftsmanship of the frame. The clear lenses reflect a faint image of the room’s ceiling lights. To the side of the glasses, a leather-bound book is partially open, its pages untouched.”

   **中文：**“一副优雅的眼镜，独特的金色六边形镜框置于光滑的深色木质表面上。纤细金属在环境光中闪烁，凸显镜框工艺。透明镜片隐约映出房间天花板灯光。眼镜旁，一本皮革装帧书半开着，书页未经翻动。”

2. **English (verbatim):** “A man dressed in a crisp white shirt and sleek black tie is seated with a guitar in his hands. He is focused intently on the strings, fingers positioned to strum a chord. The room around him is blurred, emphasizing the musician and his instrument as the central subjects of the scene.”

   **中文：**“一名身穿挺括白衬衫、系着利落黑领带的男子坐着，手中拿着一把吉他。他专注凝视琴弦，手指摆好拨动和弦的位置。周围房间被虚化，突出这位音乐家及其乐器作为场景中心主体。”

## F.7 Figure 15 — Case Types the Agentic Loop Resolves

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The three case types (structure, element granularity, and full re-planning; §4.3), in figure order:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 三类案例（结构、元素粒度和完全重新规划；§4.3）按图中顺序如下：

1. **English (verbatim):** “A wooden table with 4 stacked items on it: bottom layer a thick textbook, middle layer a closed laptop, then a coffee mug on the laptop, then a single red apple on top of the mug.”

   **中文：**“一张木桌上有 4 个堆叠物品：底层是一本厚教科书，中间层是一台合上的笔记本电脑，然后笔记本电脑上放一个咖啡杯，最后咖啡杯上放一个红苹果。”

2. **English (verbatim):** “A formal choir performance with about 60 singers in 4 horizontal rows, each row at different heights on bleachers. All wearing matching black robes. The conductor in front.”

   **中文：**“一场正式合唱表演，约 60 名歌手分列于 4 排水平队列中，每排位于看台的不同高度。所有人都穿着统一的黑色长袍。指挥在前方。”

3. **English (verbatim):** “A robot is driving while waving ahead, and a giant snail is sitting in the passenger seat.”

   **中文：**“一个机器人一边驾驶一边向前挥手，一只巨型蜗牛坐在副驾驶座上。”

## F.8 Figure 20 — Prompter Comparison Prompts

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The user prompts behind the prompter-comparison gallery, grouped by figure and listed top to bottom. The Hitman request intentionally appears in two consecutive rows of the first panel because the figure retains two separate comparison cases for the same user prompt.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 提示词生成器比较画廊背后的用户提示词按图分组，并自上而下列出。Hitman 请求有意在第一面板的连续两行中出现，因为该图保留了同一用户提示词的两个独立比较案例。

### Figure 20 (1/3), top to bottom

1. **English (verbatim):** “Ultra-high-resolution 16:9 typography travel poster of AHMEDABAD, INDIA. Giant bold sans-serif word “AHMEDABAD” centered across the poster, each letter containing different flat vector scenes of Ahmedabad — Sabarmati Riverfront, Atal Bridge, heritage pol houses, Adalaj Stepwell, Jama Masjid, metro train, auto-rickshaws, kite festival, modern skyline, temples, and street life. Letters act like architectural gallery windows with connected urban panorama. Thin panoramic strip at top with skyline silhouettes, metro, cars, birds, river bridge, boats, clouds, and warm sun. Mid-century modern Swiss graphic design, minimal vector illustration, architectural infographic aesthetic, retro travel poster branding, flat geometric shapes only, no realism, no gradients, clean vector edges, strong negative space, editorial layout, museum gift shop aesthetic. Muted Ahmedabad-inspired palette: dusty teal, terracotta, sand beige, cream, olive, burnt orange. Soft ivory background, premium typography, perfectly spelled English text, ultra-clean composition, print-ready 8K quality, no AI artifacts, no distorted text.”

   **中文：**“一张超高分辨率 16:9 排版旅行海报，主题为印度艾哈迈达巴德。巨大的粗体无衬线词‘AHMEDABAD’横贯海报中央，每个字母内包含不同的艾哈迈达巴德扁平矢量场景——萨巴尔马蒂河滨、阿塔尔大桥、历史波尔民居、阿达拉杰阶井、贾玛清真寺、地铁列车、三轮车、风筝节、现代天际线、寺庙和街头生活。字母如建筑画廊的窗户，连接成城市全景。顶部有细长全景带，包括天际线剪影、地铁、汽车、鸟、河桥、船、云和暖阳。世纪中叶现代瑞士平面设计、极简矢量插画、建筑信息图美学、复古旅行海报品牌风格；仅使用扁平几何形状，无写实、无渐变、干净矢量边缘、强留白、编辑式布局、博物馆礼品店美学。低饱和艾哈迈达巴德灵感配色：灰尘蓝绿色、陶土色、沙米色、奶油色、橄榄色、焦橙色。柔和象牙色背景、高级排版、拼写完美的英文文字、极度干净构图、可印刷的 8K 品质、无 AI 伪影、无扭曲文字。”

2. **English (verbatim):** “Screenshot of the YouTube homepage in 2030”

   **中文：**“2030 年 YouTube 首页的截图。”

3. **English (verbatim):** “A Hitman level where you are in the OpenAI HQ and your mission is to steal GPT-6 without getting caught.”

   **中文：**“一个《Hitman》关卡：你身处 OpenAI 总部，任务是在不被抓住的情况下偷走 GPT-6。”

4. **English (verbatim):** “A Hitman level where you are in the OpenAI HQ and your mission is to steal GPT-6 without getting caught.”

   **中文：**“一个《Hitman》关卡：你身处 OpenAI 总部，任务是在不被抓住的情况下偷走 GPT-6。”

5. **English (verbatim):** “1. A vibrant fusion street-food scene where a sizzling plate of smoky fried rice biryani blends aromatic spices with golden grains, beside a rich, slow-cooked mutton dish glistening with gravy. Steaming hot momos sit in a bamboo basket, releasing curls of fragrant steam, while a chilled mint mojito sparkles with ice, fresh mint leaves, and lime slices. The setting is a lively night market under warm lights, with colors, textures, and aromas colliding into a bold, modern culinary fusion aesthetic. 2. An eye-catching food scene featuring a delicious spread of fast food and refreshing drinks: a juicy pizza with melted cheese, a stacked burger with crispy lettuce and sauce, a bowl of steaming noodles, golden crispy fries, a chilled mojito with mint and lime, and fresh slices of juicy watermelon. The setting is vibrant and colorful, with soft lighting, high detail, and a modern aesthetic, arranged beautifully on a wooden table, top-down view, ultra-realistic, 4K quality.”

   **中文：**“1. 一个充满活力的融合街头美食场景：一盘滋滋作响、带烟熏感的炒饭比里亚尼将浓郁香料和金黄米粒融合，旁边是一道酱汁发亮、慢炖浓厚的羊肉菜。热气腾腾的馍馍放在竹篮中，散出缕缕香气；冰镇薄荷莫吉托中闪耀着冰块、新鲜薄荷叶和青柠片。场景位于暖光下热闹的夜市，色彩、纹理和香气碰撞成大胆现代的烹饪融合美学。2. 一个吸睛的美食场景，包含美味的快餐和清爽饮品：覆有融化奶酪的多汁披萨、夹着脆生菜和酱汁的层叠汉堡、一碗热气腾腾的面条、金黄酥脆的薯条、一杯配薄荷和青柠的冰镇莫吉托，以及新鲜多汁的西瓜切片。场景鲜艳多彩，光线柔和、细节丰富、具有现代美感；从顶部视角将食物漂亮摆放在木桌上，超写实，4K 品质。”

6. **English (verbatim):** “An overhead flat-lay food photograph of a brunch spread on a rustic wooden table. Items include: avocado toast with a poached egg, a bowl of acai topped with granola and berries, a cup of pour-over coffee, fresh orange juice in a glass carafe, scattered linen napkins, and small potted succulents. Natural daylight from a window on the left, soft shadows, warm inviting tones.”

   **中文：**“一张俯视平铺美食照片：乡村木桌上的早午餐。物品包括：配水波蛋的牛油果吐司、一碗顶部有格兰诺拉麦片和浆果的巴西莓、手冲咖啡、一玻璃水瓶的新鲜橙汁、散落的亚麻餐巾及小盆栽多肉植物。自然日光从左侧窗户照入，柔和阴影，温暖诱人的色调。”

7. **English (verbatim):** “Generate an image of a handwritten traditional Chinese medicine prescription”

   **中文：**“生成一张手写中药处方图像。”

### Figure 21 (2/3), top to bottom

1. **English (verbatim):** “Full-body fashion editorial of a confident model sitting casually on a concrete ledge, relaxed pose, direct gaze. Wearing denim jacket, white t-shirt, neutral shorts, bright socks, sneakers. Wind adds subtle motion. Beside them, a bold cartoon dragon (thick outlines, neon blue/green/yellow, playful yet powerful) interacts naturally. Bright urban outdoor setting, blue sky, strong sunlight, crisp shadows. Mixed-media style blending photorealism and illustration with doodles, arrows, and motion graphics. High contrast, HDR, ultra-detailed, 8K.”

   **中文：**“一幅全身时尚编辑大片：自信的模特随意坐在混凝土矮墙上，姿态放松、直视镜头。身穿牛仔夹克、白 T 恤、中性色短裤、亮色袜子和运动鞋。风带来微妙动感。身旁有一条大胆的卡通龙（粗轮廓、霓虹蓝／绿／黄、俏皮而有力量）自然互动。明亮的城市户外场景，蓝天、强烈日光和清晰阴影。混合媒介风格，将写实摄影与插画、涂鸦、箭头和动态图形融合。高对比度、HDR、超高细节、8K。”

2. **English (verbatim):** “High-detail anime character reference sheet, premium fantasy RPG character design board, elegant blue-and-white oceanic aesthetic, Japanese fantasy anime style, highly polished gacha game presentation, cinematic concept art layout”

   **中文：**“高细节动漫角色参考表、高级幻想 RPG 角色设计板、优雅的蓝白海洋美学、日式奇幻动漫风格、高度精修的抽卡游戏展示、电影化概念艺术布局。”

3. **English (verbatim):** “Create an epic poster showcasing the most iconic moments of Michael Jordan career. epic, cinematic, lens flare”

   **中文：**“创作一张史诗海报，展示迈克尔·乔丹职业生涯中最具标志性的时刻。史诗感、电影感、镜头光晕。”

### Figure 22 (3/3), top to bottom

1. **English (verbatim):** 重新生成一张海报，卓别林拿着止痒膏,面露微笑。风格要简约干净。

   **中文：**重新生成一张海报，卓别林拿着止痒膏，面露微笑。风格要简约干净。

2. **English (verbatim):** “Su Shi’s first day of exile Xiaohongshu screenshot”

   **中文：**“苏轼流放第一天的小红书截图。”

3. **English (verbatim):** “Style: A screenshot of an Albedo cosplay Instagram story photo; Content: Squatting on the ground facing the camera, both hands making exaggerated rebellious gestures, rolling eyes, arrogant and disdainful expression.”

   **中文：**“风格：一张阿贝多 cosplay 的 Instagram 限时动态照片截图；内容：面向镜头蹲在地上，双手做夸张的叛逆手势，翻白眼，表情傲慢且轻蔑。”

## F.9 Figures 23–24 — SOTA LLM as Prompter

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The shared user prompts behind the different-LLM-as-prompter comparison, listed top to bottom.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 不同 LLM 作为提示词生成器的比较所共用的用户提示词，自上而下列出。

### Figure 23 (1/2)

1. **English (verbatim):** “A white rabbit in a blue tracksuit is racing a turtle dressed in a red vest. The finish line is within sight, and the turtle has pulled ahead of the rabbit.”

   **中文：**“一只穿蓝色运动服的白兔正在与一只穿红色背心的乌龟赛跑。终点线已在眼前，乌龟领先于兔子。”

2. **English (verbatim):** “At a fork in the road, two girls stand on each branch, walking off in different directions.”

   **中文：**“在一条岔路口，两名女孩分别站在每条岔路上，向不同方向走去。”

3. **English (verbatim):** “A cowboy leans against the back of an old pickup truck. Two women stand in the truck bed. The image is styled like an advertisement.”

   **中文：**“一名牛仔倚靠在一辆旧皮卡车的车尾。两名女性站在货斗中。图像采用广告风格。”

4. **English (verbatim):** “Two convertible sports cars drive side by side on the street. The pink one carries two girls; the blue one carries one boy.”

   **中文：**“两辆敞篷跑车在街道上并排行驶。粉色车载着两名女孩；蓝色车载着一名男孩。”

5. **English (verbatim):** “A giant bear and a donkey play on a seesaw. The donkey is much heavier than the bear.”

   **中文：**“一只巨熊和一头驴在玩跷跷板。驴比熊重得多。”

6. **English (verbatim):** “90s + point-and-shoot camera quality”

   **中文：**“90 年代 + 傻瓜相机画质。”

7. **English (verbatim):** “There is one glass, two bottles of red wine, and three cans of beer.”

   **中文：**“有一个玻璃杯、两瓶红酒和三罐啤酒。”

8. **English (verbatim):** “A felt figurine of the Hulk, a PVC figurine of Son Goku from Dragon Ball, and a metal figurine of Snow White.”

   **中文：**“一个绿巨人的毛毡手办、一个《龙珠》中孙悟空的 PVC 手办和一个白雪公主的金属手办。”

9. **English (verbatim):** “A pineapple has one bottle of beer on its left and two on its right.”

   **中文：**“一个菠萝左边有一瓶啤酒，右边有两瓶啤酒。”

10. **English (verbatim):** “A children’s book illustration drawn with colored pencils: A curious Husky stretches its paw toward a person the size of a mouse.”

    **中文：**“一幅用彩色铅笔绘制的儿童读物插画：一只好奇的哈士奇向一名老鼠大小的人伸出爪子。”

### Figure 24 (2/2)

1. **English (verbatim):** “An avocado sits on a therapist’s chair, with a hole the size of its pit in its center. The therapist is a spoon sitting on a chair, scribbling notes hastily.”

   **中文：**“一个牛油果坐在治疗师的椅子上，中央有一个与果核同样大小的洞。治疗师是一把坐在椅子上的勺子，正匆忙地记笔记。”

2. **English (verbatim):** 组织管理金字塔结构

   **中文：**组织管理金字塔结构。

3. **English (verbatim):** 小米手机的新品发布会海报

   **中文：**小米手机的新品发布会海报。

4. **English (verbatim):** 重新生成一张海报，卓别林拿着止痒膏,面露微笑。风格要简约干净。

   **中文：**重新生成一张海报，卓别林拿着止痒膏，面露微笑。风格要简约干净。

5. **English (verbatim):** “Su Shi’s first day of exile Xiaohongshu screenshot”

   **中文：**“苏轼流放第一天的小红书截图。”

# G Additional Qualitative Examples

## G.1 Prompter Comparison: Prompter Scale × Training

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Figures 20–22 compare four prompter variants on a shared set of user prompts, with the same Qwen-Image backbone and decoding settings throughout; only the prompter changes. Two prompter scales (Qwen3.5-35B-A3B and Qwen3.5-397B-A17B) are each shown before (base) and after our SFT + Cold-start + RFT pipeline (§3.4). Reading left to right within a scale isolates the effect of training; reading across scales isolates prompter size. Each row corresponds to one user prompt. Appendix F.8 lists the full prompts in the same top-to-bottom order.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 图 20–22 在同一组用户提示词上比较四种提示词生成器变体；全程采用相同的 Qwen-Image 骨干和解码设置，仅提示词生成器发生变化。两种提示词生成器规模（Qwen3.5-35B-A3B 和 Qwen3.5-397B-A17B）均展示了在我们的 SFT + Cold-start + RFT 流水线（§3.4）之前（base）和之后的结果。在同一规模内从左向右阅读可分离训练的影响；跨规模阅读可分离提示词生成器尺寸的影响。每一行对应一个用户提示词。附录 F.8 按相同的自上而下顺序列出完整提示词。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Figure 20: Prompter comparison: prompter scale × training (1/3). Four columns compare two prompter scales, each before and after the full training pipeline, with the same Qwen-Image backbone. Rows follow the prompt order in Appendix F.8; aspect ratio is predicted by the prompter.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 图 20：提示词生成器比较：提示词生成器规模 × 训练（1/3）。四列比较两种提示词生成器规模在完整训练流水线之前和之后的结果，使用相同的 Qwen-Image 骨干。各行遵循附录 F.8 中的提示词顺序；宽高比由提示词生成器预测。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Figure 21: Prompter comparison: prompter scale × training (2/3). Continued from Figure 20; same four-column layout and prompt order.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 图 21：提示词生成器比较：提示词生成器规模 × 训练（2/3）。续接图 20；采用相同的四列布局和提示词顺序。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Figure 22: Prompter comparison: prompter scale × training (3/3). Continued from Figure 20; same four-column layout and prompt order.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 图 22：提示词生成器比较：提示词生成器规模 × 训练（3/3）。续接图 20；采用相同的四列布局和提示词顺序。

## G.2 General-purpose LLMs as Prompters

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The five columns are GPT-5.5, Gemini 3 Pro, GLM-5.2, and Claude Opus 4.8 in single-turn schema-filling mode, followed by our trained Qwen3.5-397B-A17B prompter.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 五列依次为处于单轮 schema-filling 模式的 GPT-5.5、Gemini 3 Pro、GLM-5.2 和 Claude Opus 4.8，以及我们训练得到的 Qwen3.5-397B-A17B 提示词生成器。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Figure 23: Different LLMs as prompters (1/2). General-purpose LLMs and our trained prompter fill the same schema and render with the same Qwen-Image backbone. Rows share the same user prompts. Table 3 reports the quantitative per-backend scores.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 图 23：不同 LLM 作为提示词生成器（1/2）。通用 LLM 和我们训练的提示词生成器填充相同 schema，并使用相同的 Qwen-Image 骨干渲染。各行共享相同的用户提示词。表 3 报告各后端的定量得分。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Figure 24: Different LLMs as prompters (2/2). Continued from Figure 23; same five-column layout and shared Qwen-Image backbone.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 图 24：不同 LLM 作为提示词生成器（2/2）。续接图 23；采用相同的五列布局和共享的 Qwen-Image 骨干。


### Figure 1. Information, not token count, is what scales

![Figure 1](2D%20caption/Scaling%20Properties%20of%20Text%20Conditioning%20in%20Visual%20Generation/assets/page_001_fig_figure_1.png)

**Caption:** Information, not token count, is what scales in prompt enhancement for image generation. Natural-language prose saturates, whereas structured prompts keep adding image-grounded information; at matched information, both caption families align with the same loss trend.

**Caption[CN]:** 在图像生成的提示增强中，真正扩展的是信息，而不是 token 数。自然语言 prose 的信息趋于饱和，而 structured prompt 持续加入图像接地信息；当信息量匹配时，两类 caption 落在同一条 loss 趋势上。

### Figure 2. Qualitative results and zero-shot editing

![Figure 2](2D%20caption/Scaling%20Properties%20of%20Text%20Conditioning%20in%20Visual%20Generation/assets/page_002_fig_figure_2.png)

**Caption:** Qualitative results and zero-shot editing. The final system expands requests into information-dense SPs; targeted field edits change position, material, scene, or style while preserving much of the composition.

**Caption[CN]:** 定性结果与零样本编辑。最终系统将请求扩展为高信息密度 SP；针对字段的编辑可以改变位置、材质、场景或风格，同时保留大部分构图。

### Figure 3. Fixed-backbone reconstruction probe

![Figure 3](2D%20caption/Scaling%20Properties%20of%20Text%20Conditioning%20in%20Visual%20Generation/assets/page_003_fig_figure_3.png)

**Caption:** A fixed-backbone probe separates caption information from caption length. NL lengthening remains flat, whereas restoring SP fields improves DINOv3/SigLIP2 cosine and LPIPS.

**Caption[CN]:** 固定主干探针将 caption 信息与长度分离。增加 NL 长度的结果基本不变，而逐步恢复 SP 字段会改善 DINOv3/SigLIP2 余弦相似度和 LPIPS。

### Figure 4. Method overview

![Figure 4](2D%20caption/Scaling%20Properties%20of%20Text%20Conditioning%20in%20Visual%20Generation/assets/page_005_fig_figure_4.png)

**Caption:** Method overview: annotate and measure, train, generate. SP is the common interface linking caption informativeness, the diffuser, and the LLM prompter.

**Caption[CN]:** 方法总览：标注与测量、训练、生成。SP 是连接 caption 信息量、diffuser 与 LLM prompter 的公共接口。

### Figure 5. Structured-prompt schema

![Figure 5](2D%20caption/Scaling%20Properties%20of%20Text%20Conditioning%20in%20Visual%20Generation/assets/page_007_fig_figure_5.png)

**Caption:** Structured-prompt schema by example, covering global, per-element, and cross-element scopes.

**Caption[CN]:** 结构化提示示例，覆盖全局、逐元素与跨元素三个 scope。

### Figure 6. GPG and ED

![Figure 6](2D%20caption/Scaling%20Properties%20of%20Text%20Conditioning%20in%20Visual%20Generation/assets/page_007_fig_figure_6.png)

**Caption:** The two informativeness measures: GPG sums content-token grounding gain; ED reports precision-weighted attribute coverage.

**Caption[CN]:** 两种信息量指标：GPG 累计内容 token 的接地增益；ED 报告精确率加权的属性覆盖。

### Figure 7. Loss follows information

![Figure 7](page_008_fig_figure_7.png)

**Caption:** The scaling properties of text conditioning: converged MSE is approximately linear in GPG and follows a power law in ED across all 15 sweep points.

**Caption[CN]:** 文本条件控制的缩放性质：在全部 15 个扫描点上，收敛 MSE 与 GPG 近似线性，并与 ED 呈幂律关系。

### Figure 8. Image-to-SP annotation

![Figure 8](2D%20caption/Scaling%20Properties%20of%20Text%20Conditioning%20in%20Visual%20Generation/assets/page_010_fig_figure_8.png)

**Caption:** Image-to-SP annotation with domain experts; L5–L9 are derived from L10 by deterministic field-group masking.

**Caption[CN]:** 使用领域专家完成图像到 SP 的标注；L5–L9 由 L10 通过确定性的字段组遮蔽得到。

### Figure 9. Prompter scaling

![Figure 9](page_012_fig_figure_9.png)

**Caption:** Generated-image quality improves with prompter size and, except at 0.8B, chain-of-thought reasoning.

**Caption[CN]:** 生成图像质量随 prompter 规模提升；除 0.8B 外，chain-of-thought reasoning 也带来增益。

### Figure 10. Three-stage prompter training

![Figure 10](2D%20caption/Scaling%20Properties%20of%20Text%20Conditioning%20in%20Visual%20Generation/assets/page_013_fig_figure_10.png)

**Caption:** SFT learns the target SP distribution, Cold-start bootstraps image-free derivation, and RFT applies verifier-gated OPSD on student rollouts.

**Caption[CN]:** SFT 学习目标 SP 分布，Cold-start 引导无图推导，RFT 则在学生 rollout 上实施 verifier-gated OPSD。

### Figure 11. Qualitative comparison

![Figure 11](2D%20caption/Scaling%20Properties%20of%20Text%20Conditioning%20in%20Visual%20Generation/assets/page_014_fig_figure_11.png)

**Caption:** Complex prompts requiring spatial reasoning, attribute binding, and compositional understanding.

**Caption[CN]:** 需要空间推理、属性绑定与组合理解的复杂提示定性比较。

### Figure 12. SFT recovers a non-canonical crop

![Figure 12](page_015_fig_figure_12.png)

**Caption:** Stage-1 SFT recovers a non-canonical crop.

**Caption[CN]:** 第一阶段 SFT 恢复了非标准构图先验。

### Figure 13. Prompter training progression

![Figure 13](page_017_fig_figure_13.png)

**Caption:** Text fidelity, compositional density, and layout structure improve across zero-shot, SFT, Cold-start, and RFT.

**Caption[CN]:** 从 zero-shot、SFT、Cold-start 到 RFT，文字保真度、组合密度与布局结构逐步改善。

### Figure 14. Agentic inference-time loop

![Figure 14](page_018_fig_figure_14.png)

**Caption:** The prompter emits an SP, the fixed diffuser renders, and a judge returns PASS or field-level critique until success or the round limit.

**Caption[CN]:** Prompter 输出 SP，固定 diffuser 渲染，judge 返回 PASS 或字段级批评，循环直至成功或达到轮数上限。

### Figure 15. Case types resolved by refinement

![Figure 15](page_018_fig_figure_15.png)

**Caption:** Structure, granularity, and re-planning failures corrected by targeted structured edits.

**Caption[CN]:** 通过定向结构化编辑修复结构、粒度与重新规划三类失败。

### Figure 16. GPG judge robustness

![Figure 16](page_026_fig_figure_16.png)

**Caption:** GPG is robust across compatible judges; incompatible bbox conventions require an adapter.

**Caption[CN]:** GPG 在坐标约定兼容的 judge 间具有鲁棒性；不兼容的 bbox 约定需要适配器。

### Figure 17. Setting-resampling sensitivity

![Figure 17](page_027_fig_figure_17.png)

**Caption:** Over 2,000 resamples, mean±SD $|r|$ is $0.984\pm0.008$ for GPG and $0.973\pm0.012$ for ED.

**Caption[CN]:** 在 2,000 次重采样中，GPG 与 ED 的平均±标准差 $|r|$ 分别为 $0.984\pm0.008$ 和 $0.973\pm0.012$。

### Figure 18. Budget-wise persistence

![Figure 18](page_028_fig_figure_18.png)

**Caption:** Refitting at six matched budget cuts preserves the linear GPG relation and ED power law.

**Caption[CN]:** 在六个匹配预算切点重新拟合后，GPG 线性关系与 ED 幂律仍然保持。

### Figure 19. Schema field ablation

![Figure 19](page_034_fig_figure_19.png)

**Caption:** Scene context has the largest loss impact, followed by bounding boxes; other groups have smaller marginal MSE effects.

**Caption[CN]:** Scene context 对 loss 的影响最大，其次为 bounding box；其他字段组的边际 MSE 影响更小。

### Figure 20. Prompter scale × training (1/3)

![Figure 20](page_056_fig_figure_20.png)

**Caption:** Two prompter scales before and after the full training pipeline, with the Qwen-Image backbone fixed.

**Caption[CN]:** 在固定 Qwen-Image 主干下，对比两种 prompter 规模在完整训练前后的结果。

### Figure 21. Prompter scale × training (2/3)

![Figure 21](page_057_fig_figure_21.png)

**Caption:** Continued qualitative comparison of scale and training.

**Caption[CN]:** 规模与训练效果的续篇定性比较。

### Figure 22. Prompter scale × training (3/3)

![Figure 22](page_058_fig_figure_22.png)

**Caption:** Final panel of the shared four-column prompter comparison.

**Caption[CN]:** 四列 prompter 对比的最后一组面板。

### Figure 23. Different LLMs as prompters (1/2)

![Figure 23](page_060_fig_figure_23.png)

**Caption:** General-purpose LLMs and the trained prompter fill the same schema and render through the same Qwen-Image backbone.

**Caption[CN]:** 通用 LLM 与训练后的 prompter 填充相同 schema，并通过同一 Qwen-Image 主干渲染。

### Figure 24. Different LLMs as prompters (2/2)

![Figure 24](page_061_fig_figure_24.png)

**Caption:** Continued five-column comparison with shared prompts and backbone.

**Caption[CN]:** 在共享提示和主干下继续进行五列对比。
