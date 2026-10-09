# GPIC: A Giant Permissive Image Corpus for Visual Generation

**Authors:** Keshigeyan Chandrasegaran, Kyle Sargent, Suchir Agarwal, Michael Jang, Michael Poli, Juan Carlos Niebles, Justin Johnson, Jiajun Wu, Li Fei-Fei  
**Affiliations:** Stanford University; Radical Numerics; University of Michigan; Salesforce Research  
**Date:** 28 May 2026  
**arXiv:** 2605.30341v1 [cs.CV]  
**Project:** [gpic.stanford.edu](https://gpic.stanford.edu)  
**Source:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/JZ3SBICG/Chandrasegaran 等 - 2026 - GPIC A Giant Permissive Image Corpus for Visual Generation.pdf`  
**Detected source format:** selectable-text PDF (`pdf-text`)  
**Reader type:** full-paper Chinese-English Markdown reader with figure/table assets.

## Page / Section Index

| PDF pages | Section |
|---|---|
| 1–3 | Abstract; 1 Introduction |
| 4–7 | 2 Dataset Construction |
| 7–8 | 3 Benchmarking Protocol |
| 9–10 | 4 Experiments; 5 Conclusion; Broader Impact and Limitations |
| 11–13 | References |
| 14–15 | Appendix contents; A Additional Image-Text Examples |
| 16–17 | B Evaluation |
| 18 | C Image Filtering; D Deduplication |
| 19 | E Microbenchmark |
| 20–25 | F Prompts |

## Terminology Ledger

| English term | 中文统一译法 | Note |
|---|---|---|
| permissive / permissively licensed | 宽松许可 / 采用宽松许可证 | 指同时允许研究、商业使用与再分发，不对衍生产物施加额外限制 |
| stable dataset | 稳定数据集 | 数据内容冻结，不因 URL 失效而漂移 |
| accessible | 易获取 | 可直接以分片形式下载，无需自行抓取或大内存重分片 |
| caption | 描述文本（caption） | 在数据集语境下也可译为图像描述 |
| source pool | 源数据池 | 过滤与去重前的候选图像集合 |
| deduplication | 去重 | 包含精确重复、近重复与重复簇处理 |
| copy-detection feature | 拷贝检测特征 | 本文使用 SSCD 特征 |
| flow matching | 流匹配 | 文中基线在像素空间训练 |
| classifier-free guidance (CFG) | 无分类器引导（CFG） | 生成采样时的引导尺度 |
| fidelity / diversity | 保真度 / 多样性 | Precision、Density 衡量前者；Recall、Coverage 衡量后者 |
| held-out test statistics | 留出测试集统计量 | GPIC 不以训练集统计量作为主要真实参考 |
| oracle reference | oracle 参考值 | 真实子集与真实测试集之间的距离，用于解释指标尺度 |
| register tokens | register token | DINOv2 变体中的额外 token，用于缓解高范数伪影 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Studying scalable methods for visual generative modeling requires large, accessible, and stable datasets. We introduce GPIC, a Giant Permissive Image Corpus of approximately 28 trillion pixels. GPIC comprises diverse internet images captioned by a state-of-the-art vision-language model, including 100M training, 200K validation, and 1M test examples. Moreover, all GPIC images are permissively licensed for both research and commercial use. GPIC is safety-filtered, deduplicated, and centrally hosted on Hugging Face. We provide a benchmarking protocol for generative modeling on GPIC. Finally, we provide a reference baseline for pixel-space flow matching on GPIC. Our dataset, benchmark, and models are available on Hugging Face. The evaluation toolkit and code are available at gpic.stanford.edu.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 研究可扩展的视觉生成建模方法，需要规模大、易获取且稳定的数据集。我们提出 GPIC，即 Giant Permissive Image Corpus（巨型宽松许可图像语料库），包含约 28 万亿像素。GPIC 汇集了由先进视觉语言模型生成描述文本的多样互联网图像，其中包括 1 亿个训练样本、20 万个验证样本和 100 万个测试样本。更重要的是，GPIC 中的所有图像均采用同时允许研究与商业用途的宽松许可证。GPIC 经过安全过滤和去重，并集中托管于 Hugging Face。我们给出了在 GPIC 上评测生成模型的协议，并提供一个像素空间流匹配参考基线。数据集、基准和模型均发布在 Hugging Face，评测工具包与代码见 gpic.stanford.edu。

## 1 Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> As the capabilities of modern generative models for images and videos have rapidly advanced, so has their appetite for data. Although the training details of frontier visual generative models are seldom made public, state-of-the-art open-weight models are trained on image and video corpora containing hundreds of millions to billions of examples [1–4]. Proprietary models presumably operate at comparable or greater data scales [5, 6]. In addition, visual generation has shifted away from class-conditioning signals toward dense conditioning signals such as rich text captions [3, 5].

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 随着现代图像与视频生成模型的能力快速提升，它们对数据的需求也同步增长。尽管前沿视觉生成模型很少公开训练细节，但最先进的开放权重模型通常在包含数亿至数十亿样本的图像和视频语料库上训练 [1–4]；专有模型所用的数据规模大概相当或更大 [5, 6]。与此同时，视觉生成的条件信号也已由类别条件转向信息更密集的条件，例如丰富的文本描述 [3, 5]。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The class-conditional ImageNet-1K benchmark has driven substantial progress in visual generation research, serving as a testbed for methods such as BigGAN [7], VQVAE [8], VQGAN [9], and DiT [10]. However, after more than a decade of focus on the same visual generation benchmark, two critical issues have become apparent. First, modern visual generative models rely on much larger and more diverse training corpora together with rich conditioning signals such as free-form text. As a result, the ImageNet-1K benchmark has increasingly drifted away from contemporary visual generative modeling practice, with conclusions less likely to transfer to modern practical settings. Second, over a decade of hillclimbing on ImageNet-1K has saturated FID scores and driven “Goodharting” of the metric. Notably, several recent methods achieve lower FID scores on the ImageNet-1K benchmark than held-out real images [11–14].

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 类别条件的 ImageNet-1K 基准曾显著推动视觉生成研究，并成为 BigGAN [7]、VQVAE [8]、VQGAN [9] 和 DiT [10] 等方法的试验场。然而，对同一视觉生成基准持续十余年优化后，两个关键问题日益明显。第一，现代视觉生成模型依赖规模更大、内容更多样的训练语料，并使用自由文本等丰富条件信号。因此，ImageNet-1K 与当代视觉生成实践之间的距离越来越大，在该基准上得到的结论也更难迁移到现代实际场景。第二，十余年的逐点爬坡已使 ImageNet-1K 上的 FID 趋于饱和，并诱发对指标的“Goodhart 化”。值得注意的是，若干近期方法在 ImageNet-1K 上得到的 FID 甚至低于留出的真实图像 [11–14]。脚注所引 Goodhart 定律是：当一个度量成为目标时，它就不再是一个好的度量。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> On the other hand, many industrial labs report results on text-conditioned generation of images and video, but use proprietary or unstable datasets, hindering reproducibility and open scientific comparisons. This motivates rethinking benchmark datasets for visual generative modeling research. Concretely, we identify four key properties of a modern benchmark dataset for visual generation.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 另一方面，许多工业实验室报告文本条件图像或视频生成结果时，使用的是专有或不稳定的数据集，这阻碍了结果复现与开放的科学比较。因此，有必要重新思考视觉生成研究所需的基准数据集。具体而言，我们认为现代视觉生成基准应具备四项关键属性。

### Figure 1. GPIC 图像—描述样例

![Figure 1](2D%20caption/GPIC%20A%20Giant%20Permissive%20Image%20Corpus%20for%20Visual%20Generation/assets/page_002_fig_figure_1.png)

**Caption:** Example image-caption pairs from GPIC. Additional samples are shown in Figure A.1.

**Caption[CN]:** GPIC 中的图像—描述文本样例。更多样例见图 A.1。

**Reading note:** 图中同时展示 tag、short、medium 和 long 四种描述粒度，直观说明 GPIC 不只提供单一风格的文本条件。

### Table 1. 现有基准与 GPIC 的四项属性

![Table 1](page_003_table_table_1.png)

| Property | ImageNet-1K | YFCC100M | OpenImages | DataComp | GPIC |
|---|---:|---:|---:|---:|---:|
| Permissive |  |  | ✓ |  | ✓ |
| Stable | ✓ | ✓ |  |  | ✓ |
| Large |  | ✓ |  | ✓ | ✓ |
| Accessible | ✓ |  | ✓ |  | ✓ |

**Caption:** Existing image benchmark datasets fail to satisfy all four criteria. GPIC satisfies all four criteria.

**Caption[CN]:** 现有图像基准数据集均无法同时满足四项标准，而 GPIC 同时满足全部四项。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Permissive:** Every image in the dataset should have a known license permitting both research and commercial use, without imposing restrictions on derived artifacts. Moreover, the dataset itself, including metadata and annotations, should be released under a permissive license. **Stable:** To ensure valid scientific comparisons, the benchmark dataset cannot change over time. Many modern image datasets are distributed as URL indices, which makes comparisons difficult due to link rot [15, 16]. **Large:** The benchmark dataset should be large enough, with rich text captions, to train and evaluate modern visual generative models. **Accessible:** The dataset must be easily downloadable in a sharded format without requiring crawling infrastructure [17, 15, 18] or memory-intensive resharding [16].

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **宽松许可（Permissive）：**数据集中的每张图像都应具有已知许可证，允许研究和商业使用，并且不限制衍生产物；数据集本身及其元数据、标注也应以宽松许可证发布。**稳定（Stable）：**为了保证科学比较有效，基准数据集不能随时间变化。许多现代图像数据集以 URL 索引发布，链接腐烂会使不同实验难以公平比较 [15, 16]。**大规模（Large）：**数据集应足够大，并配有丰富文本描述，以支撑现代视觉生成模型的训练和评测。**易获取（Accessible）：**数据集应可直接按分片下载，不要求用户自行搭建抓取基础设施 [17, 15, 18]，也不要求进行高内存开销的重新分片 [16]。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> We introduce GPIC, a Giant Permissive Image Corpus designed to satisfy all four criteria for benchmarking visual generative models (Table 1). GPIC comprises 27.97 trillion pixels across 100M training, 200K validation, and 1M test examples captioned with Qwen3-VL-4B [19]. GPIC is centrally hosted on Hugging Face as 8,000 shards, providing stable and accessible infrastructure for large-scale training. To construct GPIC, we develop pipelines for licensed image crawling, large-scale captioning, safety and quality filtering, and deduplication (Section 2). We also revisit the ImageNet-1K evaluation protocol (Figure 9), providing a new benchmarking protocol based on FD-DINOv2 [20] against a held-out set of one million GPIC images. Finally, we provide a reference pixel-space flow matching baseline on GPIC (Section 4). We hope GPIC enables open, accessible, and reproducible research in visual generative modeling.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 我们提出 GPIC，一个为同时满足上述四项视觉生成基准标准而设计的 Giant Permissive Image Corpus（表 1）。GPIC 包含 27.97 万亿像素，由 Qwen3-VL-4B [19] 为 1 亿训练样本、20 万验证样本和 100 万测试样本生成描述文本。数据集以 8,000 个分片集中托管在 Hugging Face，为大规模训练提供稳定、易用的基础设施。构建 GPIC 时，我们开发了许可图像抓取、大规模描述生成、安全与质量过滤以及去重流程（第 2 节）。我们还重新审视 ImageNet-1K 的评测协议（图 9），提出以 FD-DINOv2 [20] 为核心、对比 100 万张留出 GPIC 图像的新协议。最后，我们在 GPIC 上提供一个像素空间流匹配参考基线（第 4 节）。我们希望 GPIC 能推动开放、易获取且可复现的视觉生成研究。

### Figure 2. GPIC 数据集统计

![Figure 2](2D%20caption/GPIC%20A%20Giant%20Permissive%20Image%20Corpus%20for%20Visual%20Generation/assets/page_003_fig_figure_2.png)

**Caption:** GPIC dataset statistics. The figure shows GPIC’s image height and width distributions, license composition, caption statistics, release format, dataset splits, and benchmark scales. GPIC images have an average height of 479 pixels and an average width of 587 pixels. GPIC is centrally hosted on Hugging Face as 8,000 shards totaling 12.9TB and released under the MIT license. GPIC-Lite (10M) and GPIC-Nano (1M) provide smaller subsets for development. Best viewed in color.

**Caption[CN]:** GPIC 数据集统计。图中给出图像高度与宽度分布、许可证组成、描述文本统计、发布形式、数据划分与基准规模。GPIC 图像平均高度为 479 像素、平均宽度为 587 像素；共 12.9TB，以 8,000 个分片集中托管于 Hugging Face，数据集本身采用 MIT License 发布。GPIC-Lite（1,000 万）与 GPIC-Nano（100 万）是面向开发的小规模子集。建议彩色查看。

## 2 Dataset Construction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> In this section, we provide an overview of the GPIC construction pipeline (Figure 3).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本节概述 GPIC 的构建流程（图 3）。

### Figure 3. 数据集构建流程

![Figure 3](2D%20caption/GPIC%20A%20Giant%20Permissive%20Image%20Corpus%20for%20Visual%20Generation/assets/page_004_fig_figure_3.png)

**Caption:** Our dataset construction pipeline. We develop a four-stage pipeline to create GPIC. We source permissive images from Flickr and Wikimedia (Stage 1), filter low-quality and harmful images (Stage 2), deduplicate images using similarity scores derived from SSCD [23] copy detection features (Stage 3), and caption into one of tag, short, medium, or long (Stage 4). Qwen3-VL-4B-Instruct [19] is used for filtering and captioning.

**Caption[CN]:** 数据集构建流程。GPIC 由四阶段流程构建：从 Flickr 与 Wikimedia 获取宽松许可图像（阶段 1），过滤低质量和有害图像（阶段 2），利用 SSCD [23] 拷贝检测特征得到的相似度对图像去重（阶段 3），再生成 tag、short、medium 或 long 四类描述之一（阶段 4）。过滤和描述生成均使用 Qwen3-VL-4B-Instruct [19]。

### 2.1 Source Pool and Licensing

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We construct GPIC by collecting images under permissive licenses that allow redistribution and commercial use. We source images from Flickr and Wikimedia, restricting the source pool to CC BY, CC0, Public Domain, and No-Known-Restrictions categories. This licensing criterion ensures that GPIC can be used by both academic and industrial researchers without restricting the release or downstream use of derived artifacts. For each retrieved image, we retain provenance and attribution metadata, including a dataset-generated key, image height and width, retrieval timestamp, license name, license URL, and attribution string. The final dataset excludes retrieved image URLs, avoiding release of a large-scale URL index while preserving attribution and license information. The initial source pool contains 110,569,761 images, with 87.7% sourced from Flickr and 12.3% from Wikimedia.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们通过收集允许再分发和商业使用的宽松许可图像来构建 GPIC。图像来源为 Flickr 和 Wikimedia，源数据池仅保留 CC BY、CC0、Public Domain 与 No-Known-Restrictions 四类许可证。该标准使学术界与工业界研究者都能使用 GPIC，且不会限制衍生产物的发布或下游使用。对于每张抓取图像，我们保留来源与署名元数据，包括数据集生成的键、图像高度和宽度、抓取时间戳、许可证名称、许可证 URL 以及署名字符串。最终数据集不包含抓取时的图像 URL，从而避免发布大规模 URL 索引，同时保留署名与许可信息。初始源数据池共有 110,569,761 张图像，其中 87.7% 来自 Flickr，12.3% 来自 Wikimedia。

### 2.2 Image Filtering

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We apply a sequence of image-level filters to remove images unsuitable for training or benchmarking. First, we remove images with extreme resolutions or aspect ratios. Together, these filters remove approximately 0.01% of the source pool. We also discard images whose longest side is smaller than 256 pixels. Next, we apply VLM-based quality filtering using Qwen3-VL-4B. This filter removes images with poor visual quality or limited semantic content, including near-blank images, severe blur, underexposure, and overexposure. This stage removes approximately 0.3% of the source pool. We show examples in Figures 4 and C.1. Finally, we apply a conservative safety filter using Qwen3-VL-4B to remove images flagged as unsafe. This stage removes approximately 0.35% of the source pool.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们依次应用多种图像级过滤器，移除不适合训练或评测的图像。首先去掉分辨率或宽高比极端的图像，这两项过滤合计移除约 0.01% 的源数据池；同时丢弃最长边小于 256 像素的图像。随后使用 Qwen3-VL-4B 进行基于 VLM 的质量过滤，去除视觉质量差或语义内容有限的图像，包括近乎空白、严重模糊、曝光不足与过曝样本，该阶段移除约 0.3%，示例见图 4 与图 C.1。最后，再使用 Qwen3-VL-4B 施加保守的安全过滤，移除被判为不安全的图像，约占源数据池的 0.35%。

### Figure 4. 被质量过滤器移除的图像样例

![Figure 4](2D%20caption/GPIC%20A%20Giant%20Permissive%20Image%20Corpus%20for%20Visual%20Generation/assets/page_004_fig_figure_4.png)

**Caption:** Example images that are filtered due to low resolution and poor visual quality.

**Caption[CN]:** 因低分辨率与较差视觉质量而被过滤的图像样例。

### 2.3 Deduplication

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> GPIC is built from Flickr and Wikimedia, where duplicated visual content naturally arises from burst photography, reposts, and edited variants of memes and viral images. Since permissively licensed images are costly to obtain at scale, we adopt conservative duplicate removal: removing clear duplicates and near-duplicates while retaining visually related but distinct images. Many duplicates are not pixel-identical, so we perform deduplication using copy-detection features. Specifically, we extract SSCD features [23] for all images and use FAISS for approximate nearest-neighbor search. We first manually inspect nearest-neighbor pairs across SSCD similarity ranges to calibrate removal thresholds. This inspection shows that similarity above 0.90 often indicates substantial shared visual content, but still includes distinct images with changes in pose, viewpoint, or scene composition. Even pairs between 0.95 and 0.9625 can remain visually distinct, so we avoid removing images from individual pairs unless their similarity exceeds a more conservative threshold (Figure 5).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> GPIC 来源于 Flickr 与 Wikimedia，其中连拍、转发以及 meme 或网络热门图像的编辑版本会自然造成重复视觉内容。由于大规模获取宽松许可图像的成本很高，我们采取保守去重策略：移除明确的重复与近重复，同时保留视觉相关但确实不同的图像。很多重复样本并非逐像素一致，因此我们使用拷贝检测特征去重。具体做法是为所有图像提取 SSCD 特征 [23]，再用 FAISS 做近似最近邻搜索。我们先人工检查不同 SSCD 相似度区间的最近邻图像对，以校准移除阈值。检查表明，相似度高于 0.90 往往意味着共享大量视觉内容，但仍可能包含姿态、视角或场景构图不同的独立图像。即便相似度在 0.95 至 0.9625 之间，图像也可能有明显差异，因此除非单对图像的相似度超过更保守的阈值，否则不会直接移除（图 5）。

### Figure 5. 不同 SSCD 相似度区间的近邻图像对

![Figure 5](2D%20caption/GPIC%20A%20Giant%20Permissive%20Image%20Corpus%20for%20Visual%20Generation/assets/page_005_fig_figure_5.png)

**Caption:** Qualitative examples of similar image pairs across SSCD similarity ranges. Each group shows nearest-neighbor image pairs within the indicated SSCD similarity interval. At lower thresholds, similar pairs often contain visually related but distinct images, including changes in pose, viewpoint, or object identity. At higher thresholds, pairs increasingly correspond to near-duplicates, but visible differences can still remain (highlighted in red). Together with the high cost of obtaining permissively licensed images at scale, these examples motivate conservative duplicate removal rather than aggressive thresholding. Best viewed in color.

**Caption[CN]:** 不同 SSCD 相似度区间内的相似图像对。每组展示落在给定区间的最近邻对。阈值较低时，图像往往视觉相关但并不相同，可能在姿态、视角或物体身份上有差别；阈值较高时，图像对更常为近重复，但仍可能保留可见差异（红圈标出）。结合大规模获取宽松许可图像的高成本，这些样例支持保守去重，而非激进阈值裁剪。建议彩色查看。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Image collision models.** Full-corpus deduplication at 110M-image scale is expensive, and threshold choice strongly affects how many images are removed. We therefore build predictive collision models on smaller subsets before running the final full-corpus pass. We run SSCD-based deduplication on six subsets ranging from 108K to 3.4M images, across thresholds $\theta \in \{0.75, 0.80, 0.85, 0.90, 0.95\}$. For each threshold, we connect nearest-neighbor pairs whose SSCD cosine similarity exceeds $\theta$, count the number of images that would be removed by retaining the highest-resolution image in each connected component, and fit a power law $D(N)=AN^\beta$ to predict removals at full scale. The resulting curves are shown in Figure 6. These models show that lower thresholds would remove too many images at full scale, while $\theta=0.95$ provides a conservative operating point. At $\theta=0.95$, the model estimates $9.62\times10^6$ removed images, leaving approximately $1.01\times10^8$ images for the final release pipeline.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **图像碰撞模型。**在 1.1 亿张图像规模上对全语料去重代价很高，而且阈值选择会显著影响移除数量。因此，在执行最终全语料去重前，我们先在较小子集上建立预测性的碰撞模型。我们对六个规模从 10.8 万到 340 万张图像的子集运行基于 SSCD 的去重，并考察阈值 $\theta \in \{0.75, 0.80, 0.85, 0.90, 0.95\}$。对每个阈值，我们连接 SSCD 余弦相似度超过 $\theta$ 的最近邻对；在每个连通分量中保留最高分辨率图像，据此统计将被移除的图像数；再拟合幂律 $D(N)=AN^\beta$，预测全规模的移除量。结果曲线见图 6。模型表明，较低阈值在全规模上会移除过多图像，而 $\theta=0.95$ 是较保守的工作点。在该阈值下，模型估计会移除 $9.62\times10^6$ 张图像，最终发布流程约剩 $1.01\times10^8$ 张。

### Figure 6. 图像碰撞模型

![Figure 6](2D%20caption/GPIC%20A%20Giant%20Permissive%20Image%20Corpus%20for%20Visual%20Generation/assets/page_005_fig_figure_6.png)

**Caption:** Image collision models. SSCD-based duplicate removals follow a power-law trend across subset sizes and similarity thresholds. Extrapolating to the 110M-image source pool shows that $\theta=0.95$ is estimated to remove $9.62\times10^6$ images, leaving approximately $1.01\times10^8$ images.

**Caption[CN]:** 图像碰撞模型。基于 SSCD 的重复移除量在不同子集规模和相似度阈值下呈幂律趋势。外推到 1.1 亿张图像的源数据池时，$\theta=0.95$ 预计移除 $9.62\times10^6$ 张，剩余约 $1.01\times10^8$ 张。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Full-corpus deduplication.** Rather than applying a single threshold of 0.95 to remove images from all similar pairs, we use a more conservative two-tier rule calibrated by manual inspection. We first construct a candidate similarity graph by connecting image pairs with SSCD similarity above 0.90. Within this graph, we apply two removal rules. First, for pairs with similarity above 0.9625, we remove the lower-resolution image, targeting high-confidence duplicate pairs. Second, for connected components containing at least five images, we keep only the highest-resolution image in the component, targeting repeated near-copy clusters. This rule prioritizes avoiding false removals of distinct images while still removing high-confidence duplicates and large repeated clusters. After deduplication, 101.3M images remain. We show examples in Figure D.1. We also verify that no exact duplicates remain by computing SHA-256 hashes over image file bytes.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **全语料去重。**我们没有对所有相似图像对统一使用 0.95 阈值，而是采用经人工检查校准的、更保守的两级规则。首先连接 SSCD 相似度高于 0.90 的图像对，构建候选相似图。随后应用两条移除规则：其一，对于相似度高于 0.9625 的图像对，移除分辨率较低者，处理高置信重复；其二，对于至少包含 5 张图像的连通分量，只保留分辨率最高者，处理反复出现的近拷贝簇。该规则优先避免误删不同图像，同时仍能移除高置信重复与大型重复簇。去重后剩余 1.013 亿张图像，示例见图 D.1。我们还对图像文件字节计算 SHA-256 哈希，确认不再存在精确重复。

### 2.4 Captioning GPIC

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> GPIC uses high-quality synthetic captions generated by a vision-language model rather than source metadata or alt text, which are often unavailable, noisy, or weakly aligned with image content.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> GPIC 不使用常常缺失、噪声较大或与图像内容弱对齐的源元数据和 alt text，而采用视觉语言模型生成的高质量合成描述文本。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Caption formats.** There are many valid ways to describe an image in words, ranging from unordered keywords to detailed scene descriptions. To capture this variation, GPIC uses four caption formats: tag, short, medium, and long. Tag captions are unordered keyword lists, while short, medium, and long captions provide increasingly detailed natural-language descriptions of an image. Examples are shown in Figure 2. In the final corpus, caption types are assigned with proportions 1% tag, 45% short, 45% medium, and 9% long.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **描述格式。**用文字描述图像有很多合理方式，从无序关键词到细致的场景叙述不等。为覆盖这种变化，GPIC 使用 tag、short、medium 与 long 四种格式。tag 是无序关键词列表；short、medium 与 long 则以自然语言逐级增加描述细节。示例见图 2。最终语料中四类描述的比例分别为 1%、45%、45% 与 9%。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Captioning model selection.** Captioning 100M images requires a model that is accurate, fast, and practical to run at scale. Closed-source VLMs are prohibitively expensive for full-corpus captioning, so we focus on open-source models. We consider Qwen3-VL models [19] because they are among the strongest open-source models for image understanding, are available at multiple scales, and support efficient inference through standard serving frameworks such as vLLM [24] and SGLang [25]. Existing VLM benchmarks do not directly measure the captioning capability required for GPIC, where captions must be generated at multiple levels of detail. We therefore construct a microbenchmark of 1,520 GPIC images, covering 720 short, 640 medium, and 160 long captions. For each image, human annotators refine initial VLM-generated captions to produce reference captions. We evaluate Qwen3-VL-Instruct models at 2B, 4B, 8B, and 30B-A3B (sparse MoE) on this benchmark.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **描述模型选择。**为 1 亿张图像生成描述，需要模型同时准确、快速且适合规模化运行。闭源 VLM 用于全语料描述的成本高得难以接受，因此我们聚焦开源模型。Qwen3-VL [19] 是候选之一，因为它属于图像理解能力最强的开源模型，提供多个规模，并支持通过 vLLM [24]、SGLang [25] 等标准服务框架高效推理。现有 VLM 基准并不直接衡量 GPIC 所需的多细节层级图像描述能力，因此我们构建了包含 1,520 张 GPIC 图像的微基准，其中有 720 个 short、640 个 medium 和 160 个 long 描述。对每张图像，人工标注者修订 VLM 初始描述，形成参考答案。我们在该基准上评测 Qwen3-VL-Instruct 的 2B、4B、8B 与 30B-A3B（稀疏 MoE）版本。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> All captions are generated from the full image without cropping. We score captions along five axes: overall summary quality, counting accuracy, spatial understanding, attribute binding, and OCR. Each axis is scored on a 0–2 scale using an LLM-as-a-judge pipeline, and we also measure captioning throughput. As shown in Figure 7, Qwen3-VL-4B-Instruct provides the best quality-throughput tradeoff: strong overall summary quality compared to the largest model (1.68 vs. 1.73 for 30B-A3B); best spatial understanding and attribute binding scores (1.60 and 1.55); and high short- and medium-caption throughput (56.10 and 49.31 images/sec). Since short and medium captions make up 90% of GPIC, throughput on these caption types is critical for full-corpus captioning. Using Qwen3-VL-4B-Instruct, captioning the full corpus required approximately 1,500 H100 GPU-hours.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 所有描述都基于未裁剪的完整图像生成。我们从五个维度评分：总体概括质量、计数准确性、空间理解、属性绑定和 OCR。每个维度通过 LLM-as-a-judge 流程按 0–2 分计分，同时测量描述吞吐率。如图 7 所示，Qwen3-VL-4B-Instruct 给出最佳的质量—吞吐折中：总体概括质量接近最大模型（1.68，对比 30B-A3B 的 1.73）；空间理解与属性绑定得分最高（1.60 与 1.55）；short 和 medium 描述吞吐也较高（56.10 与 49.31 张/秒）。由于 short 与 medium 合计占 GPIC 的 90%，这两类吞吐率对全语料处理至关重要。使用 Qwen3-VL-4B-Instruct 为全语料生成描述约消耗 1,500 个 H100 GPU 小时。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Prompts and microbenchmark details.** For reproducibility, we provide the tag, short, medium, and long captioning prompts in Figures F.1, F.2, F.3, and F.4, respectively. We provide the LLM-as-a-judge prompt in Figure F.5 and additional microbenchmark details in Appendix E.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **提示词与微基准细节。**为保证可复现性，我们分别在图 F.1、F.2、F.3 与 F.4 给出 tag、short、medium 和 long 描述提示词，在图 F.5 给出 LLM-as-a-judge 提示词；更多微基准细节见附录 E。

### 2.5 Split Construction and Release

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Dataset splits.** We partition GPIC into 100M training images, 200K validation images, and 1M test images. Each split preserves the source distribution between Flickr and Wikimedia and the global caption-type distribution of 1% tag, 45% short, 45% medium, and 9% long. This keeps the validation and test splits compositionally aligned with the training split.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **数据划分。**GPIC 被划分为 1 亿张训练图像、20 万张验证图像和 100 万张测试图像。每个划分都保持 Flickr/Wikimedia 的来源分布，以及 1% tag、45% short、45% medium、9% long 的全局描述类型分布，使验证集和测试集在组成上与训练集对齐。

### Figure 7. 描述模型选择

![Figure 7](2D%20caption/GPIC%20A%20Giant%20Permissive%20Image%20Corpus%20for%20Visual%20Generation/assets/page_006_fig_figure_7.png)

**Caption:** Captioning model selection. We evaluate Qwen3-VL-Instruct models on the GPIC captioning microbenchmark across five caption-quality criteria and throughput. Throughput in images per second (1×H100) is shown in parentheses below each model. Qwen3-VL-4B-Instruct provides the best quality-throughput tradeoff: it matches or approaches the best quality scores across short, medium, and long captions while maintaining higher throughput than larger models.

**Caption[CN]:** 描述模型选择。我们在 GPIC 描述微基准上，从五项质量标准与吞吐率评测 Qwen3-VL-Instruct。每个模型下方括号内为单张 H100 上的每秒图像数。Qwen3-VL-4B-Instruct 在 short、medium、long 描述上的质量接近或达到最佳，同时吞吐率高于更大模型，因而具有最佳质量—吞吐折中。

### Figure 8. GPIC 分片统计

![Figure 8](2D%20caption/GPIC%20A%20Giant%20Permissive%20Image%20Corpus%20for%20Visual%20Generation/assets/page_007_fig_figure_8.png)

**Caption:** GPIC shard statistics. We show the per-shard distribution of image counts and caption-type percentages for GPIC-Full. GPIC-Full is shuffled into 8,000 approximately balanced shards, each containing approximately 12,500 images and preserving the target caption mixture of 1% tag, 45% short, 45% medium, and 9% long captions.

**Caption[CN]:** GPIC 分片统计。图中展示 GPIC-Full 各分片的图像数量与描述类型百分比分布。GPIC-Full 经打乱后分成约等量的 8,000 个分片，每个约含 12,500 张图像，并保持 1% tag、45% short、45% medium、9% long 的目标混合比例。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Benchmark scales.** We divide the GPIC train set into three nested tiers: GPIC-Nano with 1M images, GPIC-Lite with 10M images, and GPIC-Full with 100M images. Nano and Lite are intended for faster iteration and smaller-scale development. All three tiers preserve the source and caption-type distributions of GPIC-Full. The first 80, 800, and 8,000 shards correspond to GPIC-Nano, GPIC-Lite, and GPIC-Full, respectively, so switching between tiers only requires selecting the corresponding shard range.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **基准规模。**GPIC 训练集被划分为三个嵌套层级：100 万图像的 GPIC-Nano、1,000 万图像的 GPIC-Lite 和 1 亿图像的 GPIC-Full。Nano 与 Lite 面向快速迭代和小规模开发。三个层级都保持 GPIC-Full 的来源与描述类型分布；前 80、800 和 8,000 个分片分别对应 Nano、Lite 与 Full，因此切换层级只需选择相应分片范围。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Packaging and release.** We package GPIC as tar shards containing images, captions, and metadata, and release the dataset on Hugging Face with documentation. To support large-scale streaming training, GPIC-Full is shuffled and organized into 8,000 balanced shards, each containing approximately 12,500 images. As shown in Figure 8, the shards are balanced in both image count and caption-type composition. Each shard closely follows the target caption mixture, making it compositionally representative of the full corpus and avoiding shard-level bias during training.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **打包与发布。**GPIC 以 tar 分片打包，每个分片包含图像、描述和元数据，并连同文档发布在 Hugging Face。为支持大规模流式训练，GPIC-Full 先被打乱，再组织为 8,000 个均衡分片，每个约 12,500 张图像。如图 8 所示，各分片在图像数量和描述类型组成上均较平衡，且紧密遵循目标比例，因此每个分片都能代表完整语料的组成，并可避免训练中的分片级偏差。

## 3 Benchmarking Protocol

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Rigorous evaluation protocols are imperative to drive progress in visual generation. A good evaluator should distinguish real and generated images while remaining aligned with human perception. GPIC is designed to provide a more human-aligned and less saturated evaluation setting for modern visual generative models.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 严格的评测协议是推动视觉生成进展的必要条件。好的评估器既应区分真实图像与生成图像，又应与人类感知保持一致。GPIC 旨在为现代视觉生成模型提供一个更符合人类判断、饱和程度更低的评测环境。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Metrics.** On GPIC, we evaluate generated images using metrics computed over DINOv2 features. Our primary metric is FD-DINOv2 [20], which uses the same Fréchet Distance formula as FID [26] but replaces Inception features [27] with DINOv2 features. We also report Precision and Density, which measure fidelity, and Recall and Coverage, which measure diversity [28–30]. We recommend DINOv2 features because ImageNet-1K FID is saturated, while FD-DINOv2 remains informative for current models. Figure 9 illustrates this difference. Prior work also shows that FD-DINOv2 correlates better with human judgments than FID [20].

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **指标。**GPIC 使用基于 DINOv2 特征计算的指标评测生成图像。主要指标 FD-DINOv2 [20] 与 FID [26] 使用相同的 Fréchet Distance 公式，但以 DINOv2 特征替代 Inception 特征 [27]。我们还报告衡量保真度的 Precision 与 Density，以及衡量多样性的 Recall 与 Coverage [28–30]。之所以推荐 DINOv2 特征，是因为 ImageNet-1K FID 已经饱和，而 FD-DINOv2 对当前模型仍有区分力。图 9 展示了这一差异；既有工作也表明 FD-DINOv2 与人类判断的相关性优于 FID [20]。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Evaluation protocol.** To evaluate a model on GPIC, users generate 50K images using the fixed set of 50K test captions that we provide, sampled randomly from the 1M GPIC test set. The generated samples are compared against reference statistics computed from the 1M GPIC test set. We release these precomputed test statistics on Hugging Face. We also provide `gpic-eval`, a PyTorch evaluation suite that computes FD-DINOv2, Precision, Recall, Density, Coverage, and Maximum Mean Discrepancy as a non-parametric alternative to FD. Additional details are provided in Appendix B.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **评测协议。**在 GPIC 上评测模型时，用户须使用固定的 5 万条测试描述生成 5 万张图像；这些描述从 100 万样本的 GPIC 测试集中随机抽取并由作者发布。生成样本与基于 100 万 GPIC 测试图像预计算的参考统计量比较，这些统计量发布在 Hugging Face。作者还提供 PyTorch 评测套件 `gpic-eval`，计算 FD-DINOv2、Precision、Recall、Density、Coverage，以及作为 FD 非参数替代的 Maximum Mean Discrepancy。更多细节见附录 B。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Held-out test statistics.** GPIC also differs from standard ImageNet-1K evaluation in how reference statistics are computed. Standard ImageNet-1K FID compares generated samples against training-set statistics. GPIC instead compares generated samples against statistics from a held-out 1M-image test set. This is better scientific practice because comparing against train-set statistics can fail to detect memorization or overfitting.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **留出测试统计量。**GPIC 与标准 ImageNet-1K 评测的另一个区别，在于真实参考统计量的计算方式。标准 ImageNet-1K FID 将生成样本与训练集统计量比较；GPIC 则与一个包含 100 万图像的留出测试集统计量比较。这是更合理的科学实践，因为以训练集为参考可能无法发现记忆或过拟合。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Oracle references.** To provide reference points for interpreting generative model performance on GPIC, we report real-vs-real distances between GPIC subsets and the 1M GPIC test set. We compute metrics for Test-50K, GPIC-Val, GPIC-Nano, GPIC-Lite, and GPIC-Full against Test-1M in Table 2. These oracle references quantify the distance between real GPIC subsets under the GPIC evaluation protocol. In particular, Test-50K versus Test-1M provides a reference point for monitoring benchmark saturation as models trained on GPIC improve.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **Oracle 参考值。**为帮助解释生成模型在 GPIC 上的表现，我们报告各 GPIC 子集与 100 万图像测试集之间的真实—真实距离。表 2 给出 Test-50K、GPIC-Val、GPIC-Nano、GPIC-Lite 和 GPIC-Full 相对于 Test-1M 的指标。这些 oracle 参考值量化了 GPIC 协议下不同真实子集之间的距离；其中 Test-50K 对 Test-1M 尤其可用于在模型持续改进时监控基准是否趋于饱和。

### Figure 9. ImageNet-1K 上 FID 与 FD-DINOv2 的比较

![Figure 9](2D%20caption/GPIC%20A%20Giant%20Permissive%20Image%20Corpus%20for%20Visual%20Generation/assets/page_008_fig_figure_9.png)

**Caption:** Comparison of FID and FD-DINOv2 on ImageNet-1K. ImageNet-1K FID is saturated: several models achieve lower FID than the distance between 50K held-out real ImageNet-1K images and the ImageNet-1K training set. By contrast, FD-DINOv2 remains unsaturated: all evaluated models have higher FD-DINOv2 than the corresponding held-out real-image distance, including models trained with DINOv2 features. Dotted lines indicate the distance between 50K held-out real images and the ImageNet-1K training set. SiD2 [12] is omitted from the FD-DINOv2 comparison because checkpoints or generated samples are not available.

**Caption[CN]:** ImageNet-1K 上 FID 与 FD-DINOv2 的比较。FID 已饱和：若干模型的 FID 低于 5 万张留出真实图像与 ImageNet-1K 训练集之间的距离。相比之下，FD-DINOv2 尚未饱和：所有评测模型的 FD-DINOv2 都高于对应的留出真实图像距离，包括使用 DINOv2 特征训练的模型。虚线表示 5 万张留出真实图像与训练集之间的距离。由于缺少检查点或生成样本，FD-DINOv2 比较中未列 SiD2 [12]。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **GPIC Evaluation Protocol compliance.** Use of DINOv2 features, FD-DINOv2-related loss functions, or other objectives that explicitly optimize the primary GPIC evaluation representation is strongly discouraged and must be disclosed. Such use constitutes a material deviation from the standard GPIC protocol, since DINOv2 may have been trained on images overlapping with the GPIC test set, and DINOv2-based objectives directly train models to match the same representation space used by the primary GPIC metric. Therefore, improvements in FD-DINOv2 under this setting are difficult to interpret as improvements in generative modeling capability rather than metric-specific optimization. Results that use DINOv2 or FD-DINOv2-aligned training objectives should be treated as non-standard GPIC results.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **GPIC 评测协议合规性。**作者强烈不建议在训练中使用 DINOv2 特征、与 FD-DINOv2 相关的损失函数，或任何显式优化 GPIC 主要评测表征的目标；若使用则必须披露。这构成对标准 GPIC 协议的实质偏离，因为 DINOv2 可能在与 GPIC 测试集重叠的图像上训练过，而基于 DINOv2 的目标又会直接让模型匹配主要评测指标使用的同一表征空间。因此，此时 FD-DINOv2 的改善很难被解释为生成建模能力提升，而非针对指标的优化。使用 DINOv2 或与 FD-DINOv2 对齐的训练目标所得结果，应视为非标准 GPIC 结果。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> We also strongly encourage transparent reporting on the use of auxiliary networks trained on other datasets, especially larger foundation models trained on significantly more data, such as DINOv3 [31] or SigLIP [32]. Using large auxiliary models, which see considerably more data and training FLOPs, is an unfair advantage versus models trained exclusively on the GPIC benchmark dataset, and apples-to-apples comparisons are preferred whenever possible. Other deviations from the protocol should also be reported, including prompt upsampling or rewriting of the provided 50K evaluation captions, and use of different captioning models or text embedding models.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 作者也强烈建议透明报告是否使用了在其他数据集上训练的辅助网络，尤其是 DINOv3 [31]、SigLIP [32] 这类使用显著更多数据训练的大型基础模型。相较于仅在 GPIC 基准数据上训练的模型，见过更多数据且消耗更多训练 FLOPs 的大型辅助模型会带来不公平优势，因此应尽可能进行同条件比较。其他协议偏离也应报告，包括对作者提供的 5 万条评测描述做提示上采样或改写，以及使用不同的描述模型或文本嵌入模型。

### Table 2. GPIC 子集在 DINOv2 特征上的 oracle 参考指标

![Table 2](page_008_table_table_2.png)

| GPIC subset | FD ↓ | Precision ↑ | Recall ↑ | Density ↑ | Coverage ↑ |
|---|---:|---:|---:|---:|---:|
| Full | 1.19 | 0.947 | 0.950 | 1.000 | 0.972 |
| Lite | 1.25 | 0.951 | 0.947 | 1.010 | 0.973 |
| Nano | 1.60 | 0.946 | 0.946 | 1.002 | 0.968 |
| Val | 2.37 | 0.948 | 0.949 | 0.993 | 0.966 |
| Test-50K | 7.44 | 0.949 | 0.953 | 0.997 | 0.967 |

**Caption:** Oracle reference metrics over DINOv2 features for GPIC subsets evaluated against the 1M GPIC test set. These real-vs-real values provide reference points for interpreting generative model performance on GPIC. Metrics over Inception-v3 representations are provided in Table B.1. Density is not upper bounded by 1.0, so values above 1.0 are valid.

**Caption[CN]:** GPIC 各子集相对于 100 万样本测试集、基于 DINOv2 特征计算的 oracle 参考指标。这些真实—真实数值用于解释生成模型表现。基于 Inception-v3 表征的指标见表 B.1。Density 不以 1.0 为上界，因此大于 1.0 的数值有效。

## 4 Experiments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We train a simple reference baseline on GPIC-Full to provide a point of comparison for future work. Our goal is not to optimize model performance, but to establish a reproducible baseline for training and evaluation on GPIC. We use JiT [33], a pixel-space flow matching model with a Transformer backbone. JiT is a natural baseline because it uses single-stage training, does not require tokenizer pretraining, and does not rely on auxiliary losses. We use the JiT-T2I (PixGen-XXL/16 1.1B) architecture proposed by Ma et al. [34], which uses Qwen3-1.7B [35] for text conditioning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们在 GPIC-Full 上训练一个简单参考基线，为未来工作提供比较点。目标不是极致优化模型表现，而是建立一套可复现的 GPIC 训练与评测基线。所用 JiT [33] 是以 Transformer 为骨干的像素空间流匹配模型。JiT 适合作为基线，因为它采用单阶段训练，不需要预训练 tokenizer，也不依赖辅助损失。具体使用 Ma 等人 [34] 提出的 JiT-T2I（PixGen-XXL/16，1.1B）架构，以 Qwen3-1.7B [35] 提供文本条件。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Experiment setup.** We train JiT-T2I on GPIC-Full for one epoch at $256\times256$ resolution. The global batch size is 256. We use AdamW with learning rate $10^{-4}$, betas 0.9 and 0.95, and no weight decay. We use a constant learning-rate schedule with 0.1% warmup. During training, images are randomly cropped by sampling a crop scale between 0.8 and 1.0 of the original image, followed by a random square crop resized to $256\times256$. The maximum text length is 300 tokens. Training took approximately 40 hours on a single 8×H100 node. Due to streaming and prefetching errors during distributed training, a small number of samples were repeated.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **实验设置。**JiT-T2I 在 GPIC-Full 上以 $256\times256$ 分辨率训练 1 个 epoch。全局 batch size 为 256。优化器为 AdamW，学习率 $10^{-4}$，betas 为 0.9 与 0.95，不使用权重衰减；学习率保持常数，并进行 0.1% 的 warmup。训练时从原图的 0.8–1.0 范围采样裁剪尺度，再随机裁成正方形并缩放到 $256\times256$。最大文本长度为 300 tokens。训练在单个 8×H100 节点上耗时约 40 小时。由于分布式训练期间出现流式读取与预取错误，少量样本被重复使用。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> For evaluation, we follow the GPIC benchmarking protocol and generate images for the released 50K test captions. We sample with Euler sampling using 50 steps and evaluate classifier-free guidance scales of 1.75, 4.0, and 6.25.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 评测时遵循 GPIC 基准协议，为发布的 5 万条测试描述生成图像。采样使用 50 步 Euler sampling，并评测 1.75、4.0 与 6.25 三个无分类器引导（CFG）尺度。

### Figure 10. JiT-T2I 预训练损失

![Figure 10](2D%20caption/GPIC%20A%20Giant%20Permissive%20Image%20Corpus%20for%20Visual%20Generation/assets/page_009_fig_figure_10.png)

**Caption:** Pretraining loss for the JiT-T2I reference baseline [34] on GPIC-Full. We show training loss versus iterations. The model is trained for one epoch on GPIC-Full (100M text-image pairs).

**Caption[CN]:** JiT-T2I 参考基线 [34] 在 GPIC-Full 上的预训练损失。横轴为迭代次数；模型在 1 亿图文对上训练 1 个 epoch。

### Figure 11. JiT-T2I 单 epoch 训练后的样例

![Figure 11](2D%20caption/GPIC%20A%20Giant%20Permissive%20Image%20Corpus%20for%20Visual%20Generation/assets/page_009_fig_figure_11.png)

**Caption:** JiT-T2I samples after training on GPIC-Full for one epoch. We show generated images for prompts in the held-out Test-50K subset. Each group contains a real test image, the corresponding text prompt, and JiT-T2I generations sampled with classifier-free guidance scales CFG = 1.75, 4.00, and 6.25. The examples span diverse object-centric and scene-level prompts, including animals, vehicles, natural scenes, architecture, and indoor environments. Quantitative results for each CFG scale are reported in Table 3.

**Caption[CN]:** JiT-T2I 在 GPIC-Full 上训练一个 epoch 后的样例。图中给出留出 Test-50K 子集提示对应的生成图像。每组包含一张真实测试图像、对应文本提示，以及在 CFG = 1.75、4.00、6.25 下采样的 JiT-T2I 结果。样例覆盖动物、车辆、自然场景、建筑和室内环境等物体中心与场景级提示。各 CFG 的定量结果见表 3。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Results.** We report quantitative results in Table 3, the pretraining loss curve in Figure 10, and qualitative samples in Figure 11. The baseline achieves its best FD of 76.25 at CFG 6.25. Increasing CFG improves FD, recall, and coverage in this baseline. The best CFG value under FD-DINOv2 on GPIC is higher than values commonly used for class-conditional ImageNet-1K evaluation with FID. We release the model as a reference baseline for future comparisons on GPIC.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **结果。**定量结果见表 3，预训练损失曲线见图 10，定性样例见图 11。基线在 CFG 6.25 时取得最佳 FD 76.25。对该基线而言，提高 CFG 会改善 FD、Recall 和 Coverage。以 FD-DINOv2 在 GPIC 上选出的最佳 CFG，高于类别条件 ImageNet-1K 使用 FID 评测时的常见取值。作者将该模型作为未来 GPIC 比较的参考基线发布。

### Table 3. JiT-T2I 在 GPIC-Full 上训练一个 epoch 的结果

![Table 3](2D%20caption/GPIC%20A%20Giant%20Permissive%20Image%20Corpus%20for%20Visual%20Generation/assets/page_010_table_table_3.png)

| CFG | FD ↓ | Precision ↑ | Recall ↑ | Density ↑ | Coverage ↑ |
|---:|---:|---:|---:|---:|---:|
| 1.75 | 204.01 | 0.917 | 0.530 | 1.034 | 0.806 |
| 4.00 | 87.80 | 0.933 | 0.765 | 1.012 | 0.906 |
| 6.25 | 76.25 | 0.942 | 0.792 | 1.014 | 0.908 |

**Caption:** JiT-T2I baseline results on GPIC-Full after training for one epoch. We report FD, Precision, Recall, Density, and Coverage for three classifier-free guidance scales. We use 50-step Euler sampling for all generations. All metrics are computed against the 1M GPIC test set.

**Caption[CN]:** JiT-T2I 在 GPIC-Full 上训练一个 epoch 后的结果。表中报告三个 CFG 尺度下的 FD、Precision、Recall、Density 与 Coverage。所有生成均使用 50 步 Euler sampling，所有指标均以 100 万 GPIC 测试图像为参考计算。

## 5 Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> GPIC (Giant Permissive Image Corpus) is a large, permissive benchmark dataset for visual generative modeling. In this paper, we described the design choices needed to make GPIC permissive, stable, large, and accessible, including its construction pipeline, release format, evaluation protocol, compliance guidelines, and reference baseline. As visual generative models continue to evolve, benchmark datasets and metrics must evolve with them. Beyond text-to-image generation, GPIC provides a large-scale, high-quality image-text resource for broader multimodal research. We hope GPIC supports open, accessible, and reproducible research on large-scale visual generative modeling. GPIC is available at Hugging Face, and the evaluation toolkit and PyTorch code are available at gpic.stanford.edu.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> GPIC（Giant Permissive Image Corpus）是面向视觉生成建模的大规模宽松许可基准数据集。本文说明了让 GPIC 同时具备宽松许可、稳定、大规模和易获取四项属性所需的设计选择，包括构建流程、发布形式、评测协议、合规指南与参考基线。视觉生成模型持续演进时，基准数据集与指标也必须随之更新。除文本到图像生成外，GPIC 还为更广泛的多模态研究提供大规模、高质量图文资源。作者希望 GPIC 支持开放、易获取且可复现的大规模视觉生成研究。GPIC 发布在 Hugging Face，评测工具包与 PyTorch 代码见 gpic.stanford.edu。

### Broader Impact and Limitations

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> GPIC is a fully permissive 100M-image dataset for visual generative modeling, supporting transparent and legally verifiable benchmarking and model training. At the same time, GPIC carries societal risks shared with prior large-scale image corpora [15–17], including potential misuse for harmful generation, memorization of training content, and amplification of source-platform biases. We take several steps to mitigate these risks. Every image in GPIC has a clear legal basis for redistribution and use, and license names, license URLs, and attribution strings are retained as metadata for every sample. Captions are generated by Qwen3-VL-4B [19] rather than scraped from alt text, avoiding direct release of source text that may contain toxic or personally identifying language. We also release GPIC as frozen tar shards rather than a URL index, eliminating silent dataset drift, exposure to URL-level data poisoning, and the need to re-scrape source images outside our filtering pipeline. Finally, despite our deduplication efforts, some near-duplicates may remain in GPIC, although their prevalence is estimated to be small.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> GPIC 是一个包含 1 亿张图像、完全采用宽松许可的视觉生成数据集，可支持透明且在法律上可核验的基准测试与模型训练。同时，GPIC 也具有既有大规模图像语料 [15–17] 共有的社会风险，包括被滥用于有害生成、记忆训练内容，以及放大源平台偏差。作者采取多项措施缓解风险：每张图像都具有明确的再分发与使用法律依据，并为每个样本保留许可证名称、许可证 URL 和署名字符串；描述由 Qwen3-VL-4B [19] 生成，而非从 alt text 抓取，从而避免直接发布可能含有有毒或个人身份信息的源文本；GPIC 以冻结 tar 分片而非 URL 索引发布，消除无声的数据集漂移、URL 级数据投毒暴露，以及绕过过滤流程重新抓取源图像的需求。最后，尽管已经去重，GPIC 中仍可能残留少量近重复样本。

### Acknowledgments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We thank Radical Numerics and World Labs for providing compute for this project. We thank Willie Neiswanger, Yue Zhao, Armin W. Thomas, Garyk Brixi, Manling Li, Tristan Thrush, Bailey Trang, and Aryaman Arora for their feedback on the manuscript. We thank Agrim Gupta for valuable discussions. We thank members of the Stanford Vision Lab and the CogAI group for their feedback.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 作者感谢 Radical Numerics 与 World Labs 为项目提供算力；感谢 Willie Neiswanger、Yue Zhao、Armin W. Thomas、Garyk Brixi、Manling Li、Tristan Thrush、Bailey Trang 和 Aryaman Arora 对稿件的反馈；感谢 Agrim Gupta 的宝贵讨论，以及 Stanford Vision Lab 和 CogAI 小组成员的意见。

## References

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The bibliography is preserved below in its original bibliographic form. In accordance with the reader convention, publication titles, author lists, venues, identifiers, and URLs are not translated line by line.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 以下按原始书目信息保留参考文献。依照阅读器约定，论文题名、作者、会议或期刊、标识符与 URL 不逐项翻译，以避免破坏可检索性。

1. Team Wan et al. “Wan: Open and advanced large-scale video generative models.” arXiv:2503.20314, 2025.
2. Robin Rombach et al. “High-resolution image synthesis with latent diffusion models.” CVPR, 2022.
3. Chitwan Saharia et al. “Photorealistic text-to-image diffusion models with deep language understanding.” NeurIPS, 2022.
4. Zekai Zhang et al. “Qwen-image-vae-2.0 technical report.” arXiv:2605.13565, 2026.
5. Tim Brooks et al. “Video generation models as world simulators.” OpenAI, 2024.
6. Google. “Nano banana 2: Google’s latest AI image generation model.” February 2026.
7. Andrew Brock, Jeff Donahue, and Karen Simonyan. “Large scale GAN training for high fidelity natural image synthesis.” arXiv:1809.11096, 2018.
8. Aäron van den Oord, Oriol Vinyals, and Koray Kavukcuoglu. “Neural discrete representation learning.” arXiv:1711.00937, 2017.
9. Patrick Esser, Robin Rombach, and Björn Ommer. “Taming transformers for high-resolution image synthesis.” arXiv:2012.09841, 2021.
10. William Peebles and Saining Xie. “Scalable diffusion models with transformers.” arXiv:2212.09748, 2023.
11. Boyang Zheng, Nanye Ma, Shengbang Tong, and Saining Xie. “Diffusion transformers with representation autoencoders.” 2025.
12. Emiel Hoogeboom et al. “Simpler diffusion (SiD2): 1.5 FID on ImageNet512 with pixel-space diffusion.” arXiv:2410.19324, 2025.
13. Jingfeng Yao, Bin Yang, and Xinggang Wang. “Reconstruction vs. generation: Taming optimization dilemma in latent diffusion models.” arXiv:2501.01423, 2025.
14. Keyu Tian et al. “Visual autoregressive modeling: Scalable image generation via next-scale prediction.” arXiv:2404.02905, 2024.
15. Samir Yitzhak Gadre et al. “DataComp: In search of the next generation of multimodal datasets.” arXiv:2304.14108, 2023.
16. Bart Thomee et al. “YFCC100M: The new data in multimedia research.” Communications of the ACM, 2016.
17. Christoph Schuhmann et al. “LAION-5B: An open large-scale dataset for training next generation image-text models.” NeurIPS, 2022.
18. Romain Beaumont. “img2dataset: Easily turn large sets of image URLs to an image dataset.” GitHub, 2021.
19. Shuai Bai et al. “Qwen3-VL technical report.” arXiv:2511.21631, 2025.
20. George Stein et al. “Exposing flaws of generative model evaluation metrics and their unfair treatment of diffusion models.” NeurIPS, 2023.
21. Jia Deng et al. “ImageNet: A large-scale hierarchical image database.” CVPR, 2009.
22. Alina Kuznetsova et al. “The Open Images Dataset V4: Unified image classification, object detection, and visual relationship detection at scale.” IJCV, 2020.
23. Ed Pizzi et al. “A self-supervised descriptor for image copy detection.” CVPR, 2022.
24. Woosuk Kwon et al. “Efficient memory management for large language model serving with PagedAttention.” SOSP, 2023.
25. Lianmin Zheng et al. “SGLang: Efficient execution of structured language model programs.” NeurIPS, 2024.
26. Martin Heusel et al. “GANs trained by a two time-scale update rule converge to a local Nash equilibrium.” arXiv:1706.08500, 2018.
27. Christian Szegedy et al. “Going deeper with convolutions.” CVPR, 2015.
28. Tuomas Kynkäänniemi et al. “Improved precision and recall metric for assessing generative models.” NeurIPS, 2019.
29. Mehdi S. M. Sajjadi et al. “Assessing generative models via precision and recall.” arXiv:1806.00035, 2018.
30. Muhammad Ferjad Naeem et al. “Reliable fidelity and diversity metrics for generative models.” ICML, 2020.
31. Oriane Siméoni et al. “DINOv3.” arXiv:2508.10104, 2025.
32. Xiaohua Zhai et al. “Sigmoid loss for language image pre-training.” arXiv:2303.15343, 2023.
33. Tianhong Li and Kaiming He. “Back to basics: Let denoising generative models denoise.” arXiv:2511.13720, 2025.
34. Zehong Ma, Ruihan Xu, and Shiliang Zhang. “PixelGen: Pixel diffusion beats latent diffusion with perceptual loss.” arXiv:2602.02493, 2026.
35. An Yang et al. “Qwen3 technical report.” arXiv:2505.09388, 2025.
36. Alex Clark. *Pillow (PIL Fork) Documentation*. 2015.
37. Gaurav Parmar, Richard Zhang, and Jun-Yan Zhu. “On aliased resizing and surprising subtleties in GAN evaluation.” CVPR, 2022.

## Appendix

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Contents: A Additional Image-Text Examples from GPIC; B Evaluation (B.1 Construction of ImageNet-256 and GPIC-256, B.2 Additional Oracle Reference Metrics, B.3 Effect of DINOv2 Backbone Size and Register Tokens on FD); C Image Filtering; D Deduplication; E Microbenchmark; F Prompts.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 目录：A GPIC 的更多图文样例；B 评测（B.1 ImageNet-256 与 GPIC-256 的构建，B.2 更多 oracle 参考指标，B.3 DINOv2 骨干规模与 register token 对 FD 的影响）；C 图像过滤；D 去重；E 微基准；F 提示词。

## Appendix A. Additional Image-Text Examples from GPIC

### Figure A.1. 更多 GPIC 图文样例

![Figure A.1](page_015_fig_figure_A1.png)

**Caption:** Additional example image-caption pairs from GPIC.

**Caption[CN]:** 更多 GPIC 图像—描述文本样例。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The figure contains ten additional caption examples: (1) a long caption describing a winding road through a reddish desert canyon; (2) a short caption reading a plaque on a white brick wall, “COPPER HALL BUILT BY JOHN MERRIOTT 1777,” dated APR 82; (3) a medium caption describing a dark stone marker among moss, hydrangeas, and a garden-like setting; (4) a medium caption describing the rear of an FDNY ambulance with “KEEP BACK”; (5) a medium caption describing several giraffes in a dry savanna; (6) a short caption describing a dragonfly on a twig; (7) a short caption describing a speedboat numbered 94 with “Visit Jacksonville”; (8) a short caption describing a bird above red flowers; (9) a short caption describing a motocross rider jumping on a dirt track; and (10) a tag caption, “gorilla, rocky stream, green foliage, wet stones,” plus a short caption of two fighter jets displayed in a museum hangar.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 图中给出更多描述样例：（1）long：一条蜿蜒道路穿过红褐色荒漠峡谷，路边有车辆、岩板、灌木与远处台地；（2）short：白砖墙上的铭牌写着“COPPER HALL BUILT BY JOHN MERRIOTT 1777”，照片标注 APR 82；（3）medium：一块深色石质标记立在基座上，周围有苔藓、岩石、紫白绣球花与花园式环境；（4）medium：FDNY 救护车尾部停在街道上，写有醒目的“KEEP BACK”；（5）medium：数只长颈鹿站在干燥稀树草原中，一只在前景向右行走；（6）short：一只绿黑相间的蜻蜓停在枯枝上；（7）short：编号 94、侧面写有“Visit Jacksonville”的白色快艇驶过起伏水面；（8）short：一只鸟停在开有鲜红花朵的树顶；（9）short：穿红灰装备的越野摩托车手跃过土路；（10）tag：“大猩猩、岩石溪流、绿色植被、湿石”，以及 short：两架战斗机陈列在博物馆机库，一架蓝色、一架灰色且翼下挂有导弹。

## Appendix B. Evaluation

### B.1 Construction of ImageNet-256 and GPIC-256

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We adopt the following protocol: (1) center crop along the longer edge to form a square image; (2) bicubic downsampling to $256\times256$ using the Pillow library [36]. We note that popular Python image libraries use different bicubic interpolation kernels. Our choice of Pillow is consistent with prior work [20, 37].

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们采用如下协议：（1）沿较长边做中心裁剪，形成正方形图像；（2）使用 Pillow [36] 的双三次插值下采样到 $256\times256$。常用 Python 图像库的双三次插值核并不相同，选择 Pillow 是为了与既有工作 [20, 37] 保持一致。

### B.2 Additional Oracle Reference Metrics

### Table B.1. 基于 Inception-v3 表征的 GPIC oracle 指标

![Table B.1](page_016_table_table_B1.png)

| GPIC subset | FD ↓ | Precision ↑ | Recall ↑ | Density ↑ | Coverage ↑ |
|---|---:|---:|---:|---:|---:|
| Full | 0.07 | 0.757 | 0.762 | 0.973 | 0.966 |
| Lite | 0.07 | 0.762 | 0.768 | 1.041 | 0.973 |
| Nano | 0.11 | 0.756 | 0.769 | 1.000 | 0.973 |
| Val | 0.21 | 0.760 | 0.758 | 1.007 | 0.971 |
| Test-50K | 0.68 | 0.7688 | 0.763 | 0.979 | 0.964 |

**Caption:** Generative quality metrics over Inception-v3 representations across GPIC subsets against GPIC-Test-1M. We omit MMD as each subset scores approximately 0.

**Caption[CN]:** 各 GPIC 子集相对于 GPIC-Test-1M、基于 Inception-v3 表征的生成质量指标。各子集的 MMD 均约为 0，因此省略。

### Table B.2. FD 均值项与协方差项

![Table B.2](page_016_table_table_B2.png)

| GPIC subset | DINOv2 $FD_\mu$ ↓ | DINOv2 $FD_\Sigma$ ↓ | Inception-v3 $FD_\mu$ ↓ | Inception-v3 $FD_\Sigma$ ↓ |
|---|---:|---:|---:|---:|
| Full | 0.051 | 1.140 | 0.005 | 0.065 |
| Lite | 0.052 | 1.197 | 0.005 | 0.069 |
| Nano | 0.053 | 1.547 | 0.005 | 0.100 |
| Val | 0.012 | 2.353 | 0.001 | 0.208 |
| Test-50K | 0.040 | 7.404 | 0.004 | 0.678 |

**Caption:** $FD_\mu$ and $FD_\Sigma$ across GPIC subsets against GPIC-Test-1M.

**Caption[CN]:** 各 GPIC 子集相对于 GPIC-Test-1M 的 $FD_\mu$ 与 $FD_\Sigma$。

### B.3 Effect of DINOv2 Backbone Size and Register Tokens on FD

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> A practical question when using FD-DINOv2 is how to interpret its numerical scale. Unlike pixel-space distances, FD-DINOv2 depends on feature values produced by a learned neural network. In particular, these feature values can change with the DINOv2 backbone size and whether the model uses registers. We therefore ablate variants with and without registers across four DINOv2 backbone sizes: ViT-S/14, ViT-B/14, ViT-L/14, and ViT-g/14.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 使用 FD-DINOv2 时，一个实际问题是如何解释其数值尺度。与像素空间距离不同，FD-DINOv2 依赖由学习型神经网络产生的特征值；这些数值会随 DINOv2 骨干规模以及是否使用 register 而改变。因此，我们在 ViT-S/14、ViT-B/14、ViT-L/14 与 ViT-g/14 四种 DINOv2 骨干规模上，消融有无 register 的变体。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Registers in vision transformers were introduced to reduce high-norm artifacts in DINOv2 feature maps. Since FD-DINOv2 is computed directly in DINOv2 feature space, changes to the feature distribution can affect both the absolute metric value and comparisons between generative models. Results are shown in Figure B.1. For the small, base, and large backbones, variants with registers consistently produce lower FD-DINOv2 scores than corresponding variants without registers. At the giant scale, variants with and without registers are much closer.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在视觉 Transformer 中引入 register，是为了减少 DINOv2 特征图中的高范数伪影。由于 FD-DINOv2 直接在 DINOv2 特征空间计算，特征分布变化既会影响指标绝对值，也会影响生成模型间的比较。图 B.1 显示，在 small、base 和 large 骨干上，带 register 的变体始终得到更低的 FD-DINOv2；在 giant 规模上，有无 register 的结果则更接近。

### Figure B.1. 不同 DINOv2 规模和 register 变体的 FD-DINOv2

![Figure B.1](page_017_fig_figure_B1.png)

**Caption:** FD-DINOv2 across DINOv2 model sizes and variants with and without registers.

**Caption[CN]:** 不同 DINOv2 模型规模以及有无 register 变体对应的 FD-DINOv2。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The feature-value histograms in Figure B.2 help explain this pattern. For the small, base, and large backbones, variants with registers produce feature values over a much smaller range than corresponding variants without registers. Since Fréchet distance depends on both feature means and covariances, changes in the range and variance of feature values directly affect the scale of FD-DINOv2. In contrast, ViT-g/14 distributions with and without registers nearly overlap, matching the smaller FD-DINOv2 difference at the giant scale.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 图 B.2 的特征值直方图有助于解释这一现象。对于 small、base 与 large 骨干，带 register 变体的特征值范围明显小于不带 register 的版本。Fréchet distance 同时依赖特征均值与协方差，因此特征范围和方差的变化会直接改变 FD-DINOv2 的尺度。相反，ViT-g/14 有无 register 的分布几乎重合，与 giant 规模上较小的 FD-DINOv2 差异一致。

### Figure B.2. DINOv2 特征值分布

![Figure B.2](page_017_fig_figure_B2.png)

**Caption:** Distribution of DINOv2 feature values on ImageNet-1K training images.

**Caption[CN]:** ImageNet-1K 训练图像上的 DINOv2 特征值分布。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Despite these differences in absolute metric scale, the variants remain broadly consistent as evaluators. Across the eight DINOv2 configurations, the mean pairwise Pearson correlation over the five models and ImageNet-1K validation set is 0.847, and Kendall’s coefficient of concordance over the five models is 0.795. These values indicate strong agreement in the relative ordering of models. Following prior generative model evaluation work that uses DINOv2 ViT-L/14 features [20], we use the non-register ViT-L/14 backbone as the default FD-DINOv2 configuration. We leave a dedicated human-alignment study of variants with registers to future work.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 尽管绝对指标尺度不同，各变体作为评估器仍大体一致。在 8 种 DINOv2 配置上，针对 5 个模型和 ImageNet-1K 验证集计算的平均成对 Pearson 相关系数为 0.847，5 个模型上的 Kendall 协同系数为 0.795，说明模型相对排序具有较强一致性。遵循使用 DINOv2 ViT-L/14 特征的既有生成模型评测工作 [20]，本文将不带 register 的 ViT-L/14 作为默认 FD-DINOv2 配置；带 register 变体与人类判断的专门对齐研究留待未来工作。

## Appendix C. Image Filtering

### Figure C.1. 更多低分辨率与低质量图像

![Figure C.1](page_018_fig_figure_C1.png)

**Caption:** Additional low resolution and poor visual quality image examples.

**Caption[CN]:** 更多低分辨率与较差视觉质量的图像样例。

## Appendix D. Deduplication

### Figure D.1. 不同相似度区间与簇规模的去重样例

![Figure D.1](page_018_fig_figure_D1.png)

**Caption:** Qualitative examples of deduplication over similarity-score tiers and cluster sizes. All clusters with exact similarity score $\geq0.9625$ are removed, and only clusters of size $\geq5$ are removed for similarity scores in $[0.9, 0.9625)$.

**Caption[CN]:** 不同相似度区间和簇规模上的定性去重样例。精确相似度得分 $\geq0.9625$ 的簇全部移除；得分处于 $[0.9, 0.9625)$ 时，仅移除规模 $\geq5$ 的簇。

## Appendix E. Microbenchmark

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We sampled 1,520 images from the initial source-pooling stage of our dataset construction for a microbenchmark evaluating the captioning quality of Qwen3-VL-Instruct models. Human annotators examined and relabeled initial VLM captions, fixing errors and hallucinations. Common errors included counting and spatial relations. Examples of VLM-labeled and human-labeled caption pairs are shown in Figure E.1. The final human-labeled captions were used as ground truth for our LLM-as-a-judge pipeline.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们从数据构建的初始源池阶段抽取 1,520 张图像，建立用于评估 Qwen3-VL-Instruct 描述质量的微基准。人工标注者检查并重新标注初始 VLM 描述，修正错误与幻觉；常见错误包括计数和空间关系。图 E.1 给出 VLM 标注与人工标注对。最终人工描述被用作 LLM-as-a-judge 流程的 ground truth。

### Figure E.1. VLM 与人工描述的完整比较

![Figure E.1](page_019_fig_figure_E1.png)

**Caption:** Full caption comparison between VLM-generated and human-labeled annotations. Red highlights VLM outputs and blue highlights human annotations. Underlined text indicates specific differences in counting, spatial relations, and fine-grained visual details.

**Caption[CN]:** VLM 生成描述与人工标注的完整比较。红色标出 VLM 输出，蓝色标出人工标注；下划线表示计数、空间关系与细粒度视觉细节上的具体差异。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Tag.** Model: “tennis court, athletic shoes, grass, shadow, player.” Human: “tennis court, athletic shoes, grass, shadow, lower body.” **Short.** Model: “A group of people looks at papers on a wall in an office.” Human: “A group of people pins papers and sticky notes to an office wall.” **Medium.** Both captions describe a baseball batter after swinging, with the ball traveling right, a catcher and umpire behind him, and fans in the background; the model places another player near the first-base line, whereas the human places that player near the third-base line.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **Tag。**模型：“网球场、运动鞋、草地、阴影、球员。”人工：“网球场、运动鞋、草地、阴影、下半身。”**Short。**模型：“一群人在办公室里看墙上的纸。”人工：“一群人把纸张和便利贴钉到办公室墙上。”**Medium。**两者都描述击球后的棒球击球手、向右飞行的球、身后的接球手与裁判，以及背景观众；模型把另一名球员放在一垒线附近，而人工标注指出该球员在三垒线附近。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Long.** The model describes five female volleyball players, three red-and-blue players on the left, a yellow-jersey player with number 16 crouching, another yellow-jersey player near the sideline, a fifth black-and-yellow player farther right, a blue post labeled “Olympic Games,” spectators, and an umpire chair. The human caption corrects this to seven players, four red-and-blue players on the left, removes the sideline claim, and reads “London 2012” on the blue post; the remaining court-layout description is similar.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **Long。**模型描述 5 名女排球员：左侧 3 名红蓝队服球员、身穿 16 号黄色球衣且低姿势蹲伏的球员、靠近边线的另一名黄衣球员，以及更右侧的第 5 名黑黄队服球员；蓝色立柱上写着“Olympic Games”，背景有观众和裁判椅。人工描述将人数修正为 7 人、左侧红蓝队服球员修正为 4 人，删除“靠近边线”的说法，并将蓝色立柱文字修正为“London 2012”；其余球场布局描述大致一致。

## Appendix F. Prompts

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We include the exact prompts used for tag-style, short-form, medium-length, and long-form GPIC image captioning (Figures F.1–F.4), and for evaluating VLM-generated captions against ground-truth captions in the microbenchmark (Figure F.5).

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 本附录给出 GPIC 的 tag、short、medium 与 long 图像描述精确提示词（图 F.1–F.4），以及微基准中比较 VLM 生成描述与 ground-truth 描述的精确评判提示词（图 F.5）。

### F.1 Tag-style captioning prompt

### Figure F.1. Tag 风格描述提示词

![Figure F.1](page_021_fig_figure_F1.png)

**Caption:** Prompt used to generate tag-styled captions for GPIC images.

**Caption[CN]:** 用于生成 GPIC 图像 tag 风格描述的提示词。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Main instructions (strict).** Write a compressed keyword-style caption (unordered tags) for one given image. The output must be a short unordered list of tags describing the main visible content. Use only what is clearly visible; do not guess or add details. **Format:** output one line of comma-separated tags; use 3–8 tags; each tag has 1–3 words; do not write full sentences. **Unordered tag style:** tags must not form a sentence when read left to right; order should feel arbitrary; do not group tags into a logical flow such as subject → action → object → setting; mix subjects, attributes, and setting. Good: “snowy road, forest, winter, bare trees, cloudy.” Bad: “snowy road in a forest with bare trees on a cloudy day.” **Style:** use short noun phrases, nouns, or simple adjectives; prefer “snowy road” or “bare trees”; avoid connecting words such as “with,” “on,” “in,” and “and”; avoid explicit object relationships; do not use articles. **Content:** include the 1–3 most important people, animals, objects, or landmarks; include visible attributes such as color, texture, and condition; include 1–2 coarse environment tags; include an action only if extremely obvious and short, preferring nouns over verbs. **Compression:** do not describe everything; include only key visual elements; missing details are acceptable. **Counting:** avoid exact numbers unless extremely obvious and prefer plural forms. **Text:** do not include text from the image. **Edge case:** if blank or not visible, output exactly “NOT VISIBLE.” **Output rules:** output only the tag list; no sentences or explanations; no punctuation except commas; all lowercase. Style examples: “snowy road, forest, bare trees, winter, cloudy”; “white cat, sunlight, cozy”; “city street, night, race car, neon lights.” **User message:** “Write a keyword-style caption (tag-style) for the image shown.”

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **主指令（严格）。**为给定的一张图像编写压缩的关键词式描述（无序 tag）。输出必须是简短、无序的 tag 列表，只描述主要可见内容；只使用明确可见的信息，不猜测、不添加额外细节。**格式：**只输出一行，以逗号分隔 tag；共 3–8 个；每个 1–3 个词；不得写完整句子。**无序 tag 风格：**从左到右读时不得形成句子；顺序应显得任意；不得按“主体 → 动作 → 宾语 → 环境”组织逻辑流，而要混合主体、属性和环境。正确示例：“snowy road, forest, winter, bare trees, cloudy”；错误示例：“snowy road in a forest with bare trees on a cloudy day”。**风格：**使用短名词短语、名词或简单形容词；优先使用“snowy road”“bare trees”这类名词短语；避免 “with/on/in/and” 等连接词；避免明确表达物体间关系；不使用冠词。**内容：**包含 1–3 个最重要的人、动物、物体或地标；包含颜色、材质、状态等可见属性；包含 1–2 个粗粒度环境 tag；仅在动作极其明显且可简短表达时加入动作，并优先用名词而非动词。**压缩：**不要试图描述全部内容，只保留关键视觉元素，遗漏细节可以接受。**计数：**除非极其明显，否则避免精确数字，并优先用复数。**图中文字：**不得包含。**边界情况：**若图像空白或内容不可见，精确输出“NOT VISIBLE.”。**输出规则：**只输出 tag 列表；无句子、无解释；除逗号外不得有标点；全部小写。风格示例：“snowy road, forest, bare trees, winter, cloudy”；“white cat, sunlight, cozy”；“city street, night, race car, neon lights”。**用户消息：**“请为所示图像编写关键词式描述（tag 风格）。”

### F.2 Short-form captioning prompt

### Figure F.2. Short 描述提示词

![Figure F.2](page_022_fig_figure_F2.png)

**Caption:** Prompt used to generate short-length captions for GPIC images.

**Caption[CN]:** 用于生成 GPIC 图像 short 描述的提示词。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Main instructions (strict).** Write a short caption of 1–2 sentences in simple language understandable to a middle-school student. You receive one image. The caption must identify the main subject and basic setting or action. Use only clearly visible information; do not guess or add details. **Sentence rule:** output one sentence by default; use two only when absolutely required for clear identification. **Allowed content only:** (1) mention the 1–3 most important people, animals, objects, or landmarks; (2) add 1–3 simple visible identifying details, such as “red tie,” “blue bottle,” or “white car”; (3) add one short setting word such as “street,” “park,” or “kitchen”; (4) include a simple main-action verb only when clearly visible; otherwise omit actions. **Counting:** use an exact number only when very easy and unambiguous; otherwise do not guess, and use “several” or “a group of” only when clearly correct. **Text in the image:** do not reproduce it, except when large, clearly readable, and necessary to identify the main subject or scene, for example a “NOW BOARDING” airport sign. **Edge cases:** if the image is blank or the main content is not visible or understandable because it is black/white, too blurry, too dark, overexposed, or corrupted, output exactly “NOT VISIBLE.” **Output rules:** 1–2 sentences, maximum two; start immediately with the main subjects and no meta phrase; no bullet points, lists, headings, or JSON; do not mention “photo,” “image,” or “picture”; use neutral, literal language. **Length:** aim for about 12–25 words and keep sentences short and easy to read. Examples: “Two cyclists ride on a paved road.” “A white cat lies on a bed near a window.” “A bowl of noodles sits on a table with chopsticks.” **User message:** “Write a short caption (1–2 sentences) for the image shown.”

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **主指令（严格）。**使用初中生能够理解的简单语言，为一张图像写 1–2 句 short 描述。描述必须足以识别主要主体以及基本环境或动作。只使用明确可见的信息，不猜测、不添加额外细节。**句子规则：**默认输出一句；仅在清楚识别场景绝对需要时使用两句。**仅允许包含：**（1）1–3 个最重要的人、动物、物体或地标；（2）1–3 个有助识别的简单可见细节，如“红领带”“蓝瓶子”“白色汽车”；（3）一个简短环境词，如“街道”“公园”“厨房”；（4）仅当主要动作明确可见时加入简单动词，否则省略动作。**计数：**仅在非常容易且无歧义时使用精确数字；不清楚时不猜，可在明确正确时使用“several”或“a group of”。**图中文字：**一般不得抄写；唯一例外是文字很大、清楚可读且对识别主体或场景必不可少，例如机场的“NOW BOARDING”标牌。**边界情况：**图像空白，或因全黑/全白、过度模糊、过暗、过曝、损坏而无法看清或理解主要内容时，精确输出“NOT VISIBLE.”。**输出规则：**1–2 句，最多两句；直接从主要主体开始，不使用元话语；不使用项目符号、列表、标题或 JSON；不得提及“photo/image/picture”；语言中性、字面。**长度：**约 12–25 个英文词，句子短且易读。示例：“Two cyclists ride on a paved road.”；“A white cat lies on a bed near a window.”；“A bowl of noodles sits on a table with chopsticks.”。**用户消息：**“请为所示图像写一段 short 描述（1–2 句）。”

### F.3 Medium-length captioning prompt

### Figure F.3. Medium 描述提示词

![Figure F.3](page_023_fig_figure_F3.png)

**Caption:** Prompt used to generate medium-length captions for GPIC images.

**Caption[CN]:** 用于生成 GPIC 图像 medium 描述的提示词。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Main instructions (strict).** Write a medium-length caption of 2–3 sentences in simple language understandable to a middle-school student. You receive one image. The caption must identify the main subject and basic setting or action. Use only clearly visible information; do not guess or add details. **Caption-content rules:** (1) start immediately with the main visible entities and no meta phrase, for example “Two cyclists…,” “Close-up of…,” “Passengers…,” or “A street…”; (2) when clearly visible, include main entities, key visible attributes such as color/material/clothing/object type, indoor/outdoor scene context and setting, and grounded spatial layout such as foreground/background/left/right/next to/in front of; (3) count entities only when clearly countable, never guessing, and use “several” or “a group of” only when clearly correct; (4) describe actions or poses only when directly supported visually, otherwise describe a static configuration; (5) do not reproduce image text, except when it is large, clearly readable, and necessary to identify the main subject or scene. **Edge case:** if blank or not visible/understandable because it is black/white, too blurry, too dark, overexposed, or corrupted, output exactly “NOT VISIBLE.” **Output rules:** output two sentences by default and three only when absolutely required; aim for about 25–60 words; no bullets, lists, headings, or JSON; no disclaimer or meta commentary; do not mention “image,” “photo,” or “picture”; use neutral, literal language; be informative but not exhaustive. Style examples describe two cyclists on a marked road with an orange barrier and background people; a white cat on a bed near a window; and passengers facing an airport departure board with people and luggage in front. **User message:** “Please write a 2–3 sentence caption for the image shown.”

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **主指令（严格）。**使用初中生能够理解的简单语言，为一张图像写 2–3 句 medium 描述。描述必须足以识别主要主体以及基本环境或动作；只使用明确可见的信息，不猜测、不添加额外细节。**内容规则：**（1）直接从主要可见实体开始，不使用元话语，例如“Two cyclists…”“Close-up of…”“Passengers…”或“A street…”；（2）在明确可见时，包含主要实体、颜色/材质/服装/物体类型等关键属性、室内外和具体场景语境，以及“前景/背景/左/右/旁边/前方”等有视觉依据的空间布局；（3）仅在实体明确可数时计数，不得猜测，仅在明确正确时使用“several”或“a group of”；（4）仅在视觉证据直接支持时描述动作或姿态，否则描述静态配置；（5）不得抄写图中文字，除非文字很大、清晰可读且对识别主要主体或场景必不可少。**边界情况：**若图像空白，或因全黑/全白、过度模糊、过暗、过曝、损坏而不可见或不可理解，精确输出“NOT VISIBLE.”。**输出规则：**默认两句，仅在绝对必要时三句；约 25–60 个英文词；不使用项目符号、列表、标题或 JSON；不写免责声明或元评论；不得提及“image/photo/picture”；语言中性、字面；提供足够信息但不穷举物体。示例分别描述：标线道路上的两名骑行者、橙色护栏与背景人群；窗边床上的白猫；面向机场航班信息板、前方有人和行李的旅客。**用户消息：**“请为所示图像写 2–3 句描述。”

### F.4 Long-form captioning prompt

### Figure F.4. Long 描述提示词

![Figure F.4](page_024_fig_figure_F4.png)

**Caption:** Prompt used to generate long-form captions for GPIC images.

**Caption[CN]:** 用于生成 GPIC 图像 long 描述的提示词。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Main instructions (strict).** Write a long, highly detailed caption of 5–7 sentences in simple language understandable to a middle-school student. You receive one image. Assume you are describing the scene over the phone. Include enough foreground, background, and layout detail for the listener to picture the scene. Use only clearly visible information; do not guess. **Captioning protocol, in order:** (1) **Objects/entities:** identify main visible people, animals, vehicles, objects, or structures; cover important secondary elements without listing every small background object; prefer grounded order such as foreground to background; count repeated entities only when clearly visible, and do not guess under occlusion, distance, or blur. (2) **Visible attributes:** describe color, size, shape, material, texture, and patterns only when observable; do not guess brands, logos, or fine details unless text is clearly readable. (3) **Pose/actions:** describe standing, sitting, leaning, extended arms, head direction, riding, walking, or holding only when directly supported by body position or physical contact; if not verifiable, describe how the body looks rather than inferring an action. (4) **Relations/layout:** use grounded left/right/top/bottom relationships; do not overstate alignment such as “side-by-side.” (5) **OCR requirement:** if any text is visible on signs, labels, screens, posters, documents, packaging, subtitles, watermarks, interfaces, or worded logos, try to transcribe it; reproduce only clearly legible text exactly, preserving case, punctuation, numbers, symbols, and spelling; if text exists but is not fully readable, do not guess and simply say text is present; place OCR naturally, preferably in sentences 3–5.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **主指令（严格）。**使用初中生能够理解的简单语言，为一张图像写 5–7 句高度详细的 long 描述。假设你正在电话中向他人描述场景，需提供足够的前景、背景与布局细节，使对方能够在脑中还原场景。只使用明确可见的信息，不猜测。**按顺序执行描述协议：**（1）**物体/实体：**识别主要可见的人、动物、车辆、物体或结构；涵盖重要次级元素，但不罗列每个微小背景物；优先按前景到背景等有依据的顺序描述；仅在清楚可见时计数相似实体，若有遮挡、距离或模糊则不得猜数字。（2）**可见属性：**仅在可观察时描述颜色、大小、形状、材质、纹理和图案；除非文字清晰可读，否则不猜品牌、logo 或精细细节。（3）**姿态/动作：**仅在身体位置或物理接触直接支持时，描述站立、坐、倾斜、伸臂、头部朝向、骑行、步行或拿持；若动作不可验证，则描述身体外观，而不推断动作。（4）**关系/布局：**使用有视觉依据的左、右、上、下关系；不得夸大“并排”等对齐关系。（5）**OCR 要求：**若标牌、标签、屏幕、海报、文件、包装、字幕、水印、界面或带文字 logo 中有任何文字，应尝试转写；仅精确转写清楚可辨的内容，并保留大小写、标点、数字、符号与拼写；有文字但无法完全辨认时不得猜，只说明存在文字；OCR 内容应自然放入描述，优先位于第 3–5 句。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Edge case:** if blank or not visible/understandable because it is black/white, too blurry, too dark, overexposed, or corrupted, output exactly “NOT VISIBLE.” **Output rules:** produce exactly 5–7 sentences; sentences 1–3 cover main subjects, key attributes, main actions, and core setting; sentences 4–6 cover layout, secondary elements, background, and OCR when possible; optional sentence 7 adds reconstruction-helpful fine details. Sentences must be information-dense, not brief. Do not use bullets, lists, headings, JSON, disclaimers, or meta commentary. Do not mention “image,” “photo,” “picture,” or “foreground.” Start immediately with the main visible entities. Use neutral, literal language for high-quality dataset annotation. **Quality check:** a strong caption should let a reader picture the scene, main subjects, and spatial layout with minimal ambiguity; never begin with meta phrases such as “The image shows,” “The image displays,” “This image contains,” “In this image,” “The photo shows,” “The picture shows,” or “This photo contains.” The supplied good example describes two white-helmeted cyclists, their road positions and shadows, dashed lane markings, an orange crowd barrier, people, trees, buildings, a red car, a white column, and daylight in seven sentences. **User message:** “Please write a caption (5–7 sentences) for the image shown.”

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **边界情况：**若图像空白，或因全黑/全白、过度模糊、过暗、过曝、损坏而不可见或不可理解，精确输出“NOT VISIBLE.”。**输出规则：**必须恰好 5–7 句；第 1–3 句覆盖主要主体、关键属性、主要动作和核心环境；第 4–6 句覆盖布局、次级元素、背景语境，并在可能时加入 OCR；可选第 7 句添加有助重建的精细细节。句子应信息密集，而非过短。不得使用项目符号、列表、标题、JSON、免责声明或元评论。不得提及“image/photo/picture/foreground”。直接从主要可见实体开始。使用适合高质量数据标注的中性、字面语言。**质量检查：**高质量描述应让读者以最小歧义想象场景、主要主体和空间布局；绝不能以“The image shows”“The image displays”“This image contains”“In this image”“The photo shows”“The picture shows”或“This photo contains”等元话语开头。给定的优秀示例用 7 句描述两名戴白色头盔的骑行者、道路位置与影子、虚线车道标记、橙色人群护栏、人群、树木、建筑、红色汽车、白色立柱与日光。**用户消息：**“请为所示图像写 5–7 句描述。”

### F.5 LLM-as-a-Judge prompt

### Figure F.5. 微基准 LLM-as-a-Judge 提示词

![Figure F.5](page_025_fig_figure_F5.png)

**Caption:** Prompt used to evaluate VLM-generated captions against ground-truth captions in the microbenchmark.

**Caption[CN]:** 微基准中用于比较 VLM 生成描述与 ground-truth 描述的提示词。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> You are an expert evaluator comparing a VLM-generated caption against a human-written ground-truth caption. Captions may be natural-language descriptions or unordered tag-style captions. Assess how well the VLM caption matches the human caption across multiple criteria. Inputs are `HUMAN CAPTION (Ground Truth): {human_caption}` and `VLM CAPTION (To Evaluate): {vlm_caption}`. Evaluate five criteria on a 0–1–2 scale: 0 = wrong/incorrect with major errors, contradictions, or missing critical information; 1 = partially correct, capturing the main idea but with mistakes or omissions; 2 = correct/perfect match, accurate and aligned with the human caption.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 你是一名专家评估者，需要将 VLM 生成描述与人工撰写的 ground-truth 描述比较。描述可以是自然语言，也可以是无序 tag。任务是在多个标准上判断 VLM 描述与人工描述的匹配程度。输入为 `HUMAN CAPTION (Ground Truth): {human_caption}` 和 `VLM CAPTION (To Evaluate): {vlm_caption}`。五项标准均使用 0–1–2 评分：0 表示错误，存在重大错误、矛盾或缺失关键信息；1 表示部分正确，抓住主旨但有错误或遗漏；2 表示正确或完美匹配，与人工描述准确对齐。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **1. Overall summary (required):** does the VLM caption capture the overall scene and main content? Score 0 for a fundamentally different scene, missed main subjects, or major contradictions; 1 for the general scene with some important omissions or minor errors; 2 for accurate overall scene and main elements. **2. Counting accuracy (N/A if the human caption has no counts):** if the human caption gives quantities such as “two cyclists” or “three cars,” does the VLM match them? Score N/A when no counts appear; 0 for wrong counts; 1 for partially correct counts, missing some counts, or vague terms such as “several”; 2 when all counts match exactly. Evaluate only counts present in the human caption and ignore extra counts added by the VLM.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **1. 总体概括（必评）：**VLM 描述是否覆盖整体场景与主要内容？若描述根本不同的场景、遗漏主要主体或有重大矛盾，记 0；覆盖大致场景但遗漏重要元素或有轻微错误，记 1；准确覆盖整体场景与主要元素，记 2。**2. 计数准确性（人工描述无计数时为 N/A）：**若人工描述给出“两名骑行者”“三辆汽车”等数量，VLM 是否一致？无计数时 N/A；数量错误记 0；部分数量正确、漏计或使用“several”等模糊词记 1；所有计数完全一致记 2。仅评估人工描述中出现的计数，忽略 VLM 额外添加的计数。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **3. Spatial understanding (N/A if the human caption has no spatial descriptions):** assess left/right, foreground/background, near/far, above/below, and beside relations. Score N/A when none appear; 0 when the VLM contradicts them; 1 when some are correct but others are missed or wrong; 2 when all align. Evaluate only spatial relations in the human caption. **4. Attribute binding (N/A if the human caption has no attributes):** determine whether colors, shapes, sizes, materials, and patterns are bound to the correct objects. Score N/A when none appear; 0 for wrong bindings such as “blue car” instead of “red car”; 1 when some are correct but others are missed or wrong; 2 when all bindings match. Evaluate only attributes in the human caption and ignore extra VLM attributes.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **3. 空间理解（人工描述无空间关系时为 N/A）：**评估左/右、前景/背景、近/远、上/下、旁边等关系。无空间关系时 N/A；VLM 与之矛盾记 0；部分正确但有遗漏或错误记 1；全部对齐记 2。只评估人工描述中的空间关系。**4. 属性绑定（人工描述无属性时为 N/A）：**判断颜色、形状、大小、材质和图案是否绑定到正确物体。无属性时 N/A；如把“红车”写成“蓝车”的错误绑定记 0；部分正确但有遗漏或错误记 1；全部绑定一致记 2。只评估人工描述中的属性，忽略 VLM 额外添加的属性。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **5. OCR text accuracy (N/A if the human caption mentions no text):** when the human caption mentions signs, labels, subtitles, watermarks, or other visible text, determine whether the VLM transcribes the same text correctly. Score N/A when there is no OCR content; 0 when text is wrong, omitted entirely, or fabricated; 1 for partially correct transcription with errors or omissions; 2 when all mentioned text is accurate. Evaluate only text mentioned by the human caption; case, punctuation, and spelling must match.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **5. OCR 文字准确性（人工描述未提文字时为 N/A）：**若人工描述提到标牌、标签、字幕、水印或其他可见文字，判断 VLM 是否正确转写同一内容。无 OCR 内容时 N/A；转写错误、完全遗漏或捏造文字记 0；部分正确但有错误或遗漏记 1；人工提到的全部文字均准确记 2。只评估人工描述中提到的文字，大小写、标点和拼写必须一致。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Evaluation instructions:** compare criterion by criterion; use “N/A” whenever a criterion does not apply; be strict but fair, accepting minor wording differences if meaning is preserved; focus on factual accuracy rather than style or length; penalize content mentioned by the human caption but omitted by the VLM; do not penalize extra correct information; captions may be prose or unordered tags, and each comma-separated tag is a semantic assertion; do not penalize tag captions for grammar, sentence structure, or order. **Output:** respond with only a valid JSON object, no extra text or Markdown, using keys `overall_summary`, `counting_accuracy`, `spatial_understanding`, `attribute_binding`, `ocr_text_accuracy`, and `explanation`. The first score must be 0, 1, or 2; the other four may also be `"N/A"`; `explanation` is a brief rationale. Critical: output only JSON, with no preamble, formatting, or commentary.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **评测说明：**逐项比较；不适用时使用“N/A”；严格但公平，只要语义保留即可接受轻微措辞差异；关注事实准确性，而非写作风格或长度；人工描述提到但 VLM 完全遗漏的内容应扣分；VLM 添加额外且正确的信息不扣分；描述既可以是自然语言，也可以是无序 tag，每个逗号分隔的 tag 都视为一个语义断言；不得因 tag 缺少语法、句子结构或顺序而扣分。**输出：**只返回有效 JSON 对象，不得有额外文字或 Markdown；键为 `overall_summary`、`counting_accuracy`、`spatial_understanding`、`attribute_binding`、`ocr_text_accuracy` 与 `explanation`。第一项只能为 0、1 或 2；其余四项还可为 `"N/A"`；`explanation` 给出简短理由。关键要求：只能输出 JSON，不得添加前言、格式标记或评论。

## Critical Reading Notes

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> GPIC’s primary contribution is infrastructure and protocol design rather than a new generator: permissive licensing at 100M scale, frozen centrally hosted shards, multi-granularity synthetic captions, a held-out one-million-image test reference, and an explicit metric-compliance policy. The reference JiT result is deliberately modest and should not be read as the dataset’s performance ceiling.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> GPIC 的核心贡献是基础设施与协议设计，而不是新的生成器：在 1 亿规模上保证宽松许可，提供冻结且集中托管的分片、多粒度合成描述、100 万图像的留出真实参考，以及明确的指标合规政策。JiT 参考结果刻意保持简单，不应被误读为数据集上的性能上限。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The strongest scientific choice is the held-out test statistic, which reduces the risk that memorization looks like high quality. The main unresolved risks are inherited source-platform bias, residual near-duplicates, safety-filter dependence on one VLM, and evaluator dependence on DINOv2. Caption quality is audited on only 1,520 examples, so the microbenchmark supports model selection but does not fully characterize annotation errors across 100M images.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 最有科学价值的设计是使用留出测试统计量，它降低了“记住训练集却看起来质量很高”的风险。尚未解决的主要风险包括源平台偏差、残留近重复、对单一 VLM 安全过滤器的依赖，以及对 DINOv2 评估器的依赖。描述质量只在 1,520 个样例上审计，因此微基准足以支持模型选择，却不能完整刻画 1 亿图像上的标注误差分布。
