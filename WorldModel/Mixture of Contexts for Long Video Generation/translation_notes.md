# Translation Notes

## Scope

- Full 20-page bilingual detailed reader for **"Mixture of Contexts for Long Video Generation"** (Shengqu Cai, Ceyuan Yang, Lvmin Zhang, Yuwei Guo, Junfei Xiao, Ziyan Yang, Yinghao Xu, Zhenheng Yang, Alan Yuille, Leonidas Guibas, Maneesh Agrawala, Lu Jiang, Gordon Wetzstein; Stanford / ByteDance Seed / Johns Hopkins / CUHK, arXiv 2025).
- Covers all substantive sections without omission:
  - Title, Authors, Affiliations, Metadata, Project Page, Abstract.
  - Section 1 Introduction.
  - Section 2 Related Work (Long Video Generation, Sparse Attention for Video Generation, Context Learning in Visual Generation).
  - Section 3 Method (3.1 Mixture of Contexts, 3.2 Attention Chunking and Routing, 3.3 Computation Efficiency, Equations 1–6).
  - Section 4 Experiments (Base Model, Baselines, Evaluation Metrics, Quantitative Results, Qualitative Results, Coherence Visualization).
  - Section 5 Conclusion & Limitations and Future Work.
  - References 1–65 (preserved in searchable bibliographic citation form).
  - Appendix A (Memory Complexity Analysis).
  - Appendix B (MoC Implementation Benchmark).
  - Appendix C (Dataset Details, 500k authentic multi-shot scene curation).
  - Appendix D (Zero-shot Experiment on Pretrained DiT).
  - Appendix E (Single-shot Short Video Generation).
  - Appendix F (Training Details, learning rates, schedules).
  - Appendix G (Ablation Study on chunk sizes, top-$k$, forced links, Context Drop In/Out).
  - Appendix H (Wan-2.1-1.3B Generalization Experiment).
  - Appendix I (Outer Loop Context Routing Hierarchical Architecture).
  - Appendix J (Social Impact & Misuse Mitigation).
  - Appendix K (The Use of Large Language Models).

## Source Material

- **PDF Source:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/7SWAYAM9/Cai 等 - 2025 - Mixture of Contexts for Long Video Generation.pdf`
- **Detected source format:** selectable-text single-column PDF (`pdf-text`), 20 pages, arXiv preprint (arXiv:2508.21058v3, 9 Dec 2025).
- **Layout Extracted Text:** `extracted_text.txt` in the target directory (87,227 characters).
- **Visual Assets:** 12 primary scientific crops in `assets/`:
  - Figures 1–7: `figure_1.png` to `figure_7.png`.
  - Tables 1–5: `table_1.png` to `table_5.png`.
  - Page renders: `page_001.png` to `page_020.png`.

## Format and Alignment

- **Bilingual Structure:** Every substantive prose paragraph is presented as an adjacent pair:
  - `> <span style="color:#3B82F6"><strong>Para. X:</strong></span> English verbatim text...`
  - `> <span style="color:#F59E0B"><strong>Para. X[CN]:</strong></span> 严谨学术中文翻译...`
  Numbering restarts cleanly at major sections or subsections to allow precise navigation.
- **Display Math:** All display equations (Equations 1–6 and standalone formulas) are placed on dedicated standalone lines outside Markdown blockquotes, using standard LaTeX `$$...$$` notation. Inline math within prose utilizes `$ ... $`.
- **Figures and Tables:**
  - Every figure includes its local asset link (`assets/figure_X.png`), original caption (`**Caption:**`), and Chinese translation (`**Caption[CN]:**`).
  - Every table includes its local asset link (`assets/table_X.png`), a searchable, faithfully transcribed Markdown table, original caption, and Chinese translation.
- **Identical Deliverable:** `paper.md` is maintained as an exact byte-for-byte replica of `detailed_paper.md`.

## Terminology and Translation Decisions

- `Mixture of Contexts (MoC)`: 统一译为“上下文混合（MoC）”，在标题和首段中给出中英文对照。
- `Diffusion Transformers (DiT)` / `MMDiT`: 统一译为“扩散 Transformer（DiT）”与“多模态扩散 Transformer（MMDiT）”。
- `content-aligned chunks`: 统一译为“内容对齐的块”，指代沿帧、镜头与文本边界切分的语义均质分块。
- `mean-pooled key / descriptor`: 统一译为“均值池化键 / 描述符”，保留其代数平均与第一主成分估计的数学内涵。
- `top-k selection`: 统一译为“top-$k$ 选择”，保持数学符号一致性。
- `causal routing / causal mask`: 统一译为“因果路由 / 因果掩码”，强调有向无环图（DAG）消除时序自闭环的核心设计。
- `loop closures / self-loops`: 统一译为“回路闭合 / 自反馈闭环”，指代无向注意力导致的双节点死循环。
- `attention sink`: 统一译为“注意力汇聚（Attention Sink）”，保留经典文献术语。
- `forced links / mandatory anchors`: 统一译为“强制连接 / 强制锚点”，指跨模态文本连接与镜头内局部窗口连接。
- `intra-shot local window`: 统一译为“镜头内局部窗口”，强调镜头内部所有 token 强制全互联的局部保真度机制。
- `context drop-off` / `context drop-in`: 统一译为“上下文丢弃（Context Drop-off）”与“上下文注入（Context Drop-in）”。
- `per-head distributed routing`: 统一译为“分头分布式路由”，指每个注意力头独立学习不同特征子空间的稀疏路由。
- `outer loop context routing`: 统一译为“外循环上下文路由”，指针对百万级 token 超长序列的粗粒度镜头预筛选机制。
- `zero-shot context sparsification`: 统一译为“零样本上下文稀疏化”，强调免微调直接将 MoC 插入密集 DiT 的能力。
- `segment_reduce`: 统一译为“段规约（segment_reduce）”，保留 PyTorch 算子原文。
- `Flash-Attention var-len`: 统一保留专用算子名称“Flash-Attention 可变长（var-len）内核”。
- `VBench` 评估指标：`Subject Consistency` 统一译为“主体一致性”，`Background Consistency` 译为“背景一致性”，`Motion Smoothness` 译为“动作平滑度”，`Dynamic Degree` 译为“动态程度”，`Aesthetic Quality` 译为“美学质量”，`Image Quality` 译为“图像质量”。

## Skipped or Untranslated Material

- 参考文献 [1]–[65] 按照学术双语阅读规范保留检索可用的英文原始著录格式，在文末添加了导读说明。
- 图像内部的微小标注（如 Figure 3 与 Figure 6 中小图上的镜头标签 `[Shot 2] man sits in cafe`）属于栅格图像内置像素，在图表对应正文段落中提供了详细完整的中文语义解读与对比分析。
- 严格遵循保护规范：未修改、未覆盖任何 `paper_DeepPaperNote.*` 分析笔记与 `images/` 目录。

## Verification Targets and Results

- **Deterministic Validator:**
  `python3 /Users/roywangj/Desktop/skills4ai/wj_skills/nature-reader-detail-wj/scripts/validate_detailed_paper.py "/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Mixture of Contexts for Long Video Generation/detailed_paper.md" --source "/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Mixture of Contexts for Long Video Generation/paper.md" --require-identical`
  - Passes: `True`
  - Errors: `0`
  - Bilingual paragraph pairs: `46`
  - Bilingual caption pairs: `12 original / 12 Chinese`
  - Broken image links: `0`
  - Reference entries: `65`
  - Byte identity between `detailed_paper.md` and `paper.md`: `True` (`sha256` exact match).
