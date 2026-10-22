# Translation Notes / 翻译笔记

## Scope / 翻译范围

- Complete bilingual reader built from the canonical local PDF supplied by the user: `PICQTU9H/Yu 等 - 2026 - OpenWAM An Open Framework for Composable World-Action Models.pdf` (18 pages, two-column selectable-text arXiv preprint).
- Authoritative build: `detailed_paper.md`.
- Copy relationship: `paper.md` is an exact byte-identical copy of `detailed_paper.md`.
- Full-text coverage:
  - Title & Frontmatter
  - Abstract
  - 1. Introduction (Paras 1–6, Figure 1)
  - 2. Related Work (§§2.1–2.3, Paras 1–3, 1–5, 1–3)
  - 3. Methodology (§§3.1–3.4, Equations 1–10, Figures 2–4, Table 1)
  - 4. Experiments (§§4.1–4.4, Tables 2–7)
  - 5. Discussion and Conclusion (Paras 1–4)
  - References (Entries [1]–[108], preserved in searchable original bibliographic form)
  - Appendix:
    - A. Implementation Details (§§A.1–A.5, Equations 11–13, Figure 5)
    - B. Robot-Video Pretraining (§§B.1–B.3, Table 8)
    - C. LIBERO-Long-CF: Counterfactual Dynamics Data (§§C.1–C.3, Tables 9–11)
    - D. Ablations (§§D.1–D.2, Tables 12–13)
    - E. External Dynamics Comparison (§§E.1–E.2, Table 14)

## Source and Provenance / 来源与版本证据

- Canonical PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/PICQTU9H/Yu 等 - 2026 - OpenWAM An Open Framework for Composable World-Action Models.pdf`
- arXiv: `2610.07922v1 [cs.RO]` (6 Oct 2026)
- Authors: Heng Yu*, David D. Yuan*, Juze Zhang*, Changan Chen, Yao Feng, Michelle Baldonado, Steve Cousins, Li Fei-Fei, Jiajun Wu, Ehsan Adeli (*Equal contribution)
- Affiliation: Stanford University
- Project Page: `https://openwam.stanford.edu`
- Code Repository: `https://github.com/OpenWAM/OpenWAM`

## Extraction and Layout / 文本提取与排版对齐

- The 18-page PDF was extracted with layout awareness and validated against the rendered page images (`assets/page_001.png` to `page_018.png`).
- Multi-column reading order and figure/table interleaving were verified directly against page visual layouts.
- Line-wrap hyphenation was re-joined naturally (e.g. `video–action`, `modality-specific`).
- All mathematical expressions were transcribed as standard LaTeX (`$...$` for inline math, standalone `$$...$$` outside blockquotes for display equations).

## Figures and Tables / 图表与资产引用

- All 5 figures are embedded with relative paths: `assets/figure_1.png` to `assets/figure_5.png`, immediately followed by paired English and Chinese captions (`**Caption:**` and `**Caption[CN]:**`).
- All 14 tables are embedded with relative links (`assets/table_1.png` to `assets/table_14.png`), transcribed into clean, contiguous Markdown tables without blank lines between table rows, and immediately followed by paired captions (`**Caption:**` and `**Caption[CN]:**`).
- No local image links are broken.

## Translation Policy / 翻译规范与风格约定

- Strict alignment with WJ reading habits and professional AI/Robotics terminology standards.
- English paragraph followed immediately by Chinese paragraph in styled blockquotes:
  `> <span style="color:#3B82F6"><strong>Para. X:</strong></span> English...`
  `> <span style="color:#F59E0B"><strong>Para. X[CN]:</strong></span> 中文...`
- Exact preservation of numbers, thresholds, units, metrics, formulas, dataset sizes, compute budgets (32 NVIDIA B200 GPUs for 14 days), and citations.
- Key technical terms:
  - World-Action Model (WAM) -> 世界动作模型 (WAM)
  - Mixture-of-Transformers (MoT) -> 多专家 Transformer 架构 (MoT)
  - Video-then-Action (VTA) -> 视频先导动作 (VTA)
  - Action-then-Video (ATV) -> 动作先导视频 (ATV)
  - Joint Denoising -> 联合去噪生成 (Joint)
  - Decoupled Denoising -> 解耦去噪生成 (Decoupled)
  - Causal Robot-Video Pretraining -> 因果机器人视频预训练
  - Chunk-Causal Prediction -> 块因果预测 (Chunk-Causal Prediction)
  - Local-Context IDM (LC-IDM) -> 局部上下文逆动力学模型 (LC-IDM)
  - Local-Context FDM (LC-FDM) -> 局部上下文前向动力学模型 (LC-FDM)
  - Counterfactual Transitions -> 反事实状态转移 (Counterfactual Transitions)
  - Outcome Identification -> 结局识别准确率 / 结果辨识度 (Outcome Identification)
  - Delta-OSC Controls -> 增量操作空间控制 (delta-OSC controls)
  - Classifier-Free Guidance (CFG) -> 无分类器引导 (CFG)

## References Policy / 参考文献策略

All 108 references are preserved in searchable original bibliographic form with sequential numbered list prefixes (`1. [1] ...` to `108. [108] ...`). This ensures that bibliography entries can be indexed and searched by citation tools while author names and publication titles remain unmodified.

## Validation Status / 验证状态

The output was verified using `validate_detailed_paper.py`:
- 0 missing or broken images
- Perfectly balanced paragraph pairs
- Perfectly balanced caption pairs
- Exact byte-identical match between `detailed_paper.md` and `paper.md`
- All checks pass with 0 errors.
