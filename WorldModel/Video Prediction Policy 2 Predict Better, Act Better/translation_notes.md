# Translation Notes

## 1. Scope and Source Evidence

- **Paper Title:** Video Prediction Policy 2: Predict Better, Act Better
- **Authors:** Yanjiang Guo, Haodong Yan, Zhide Zhong, Zhongru Zhang, Qingyuan Yang, Qingzhou Lu, Xiaoyu Chen, Yen-Jen Wang, Shuying Deng, Chenghan Yang, Puzhen Yuan, Chenxin Liu, Tun Ban, Xiang Zhu, Yichen Liu, Kun Feng, Haoang Li, Jianyu Chen (Robotera / Tsinghua University / HKUST (GZ) / UC Berkeley / SJTU)
- **Source:** Full-text PDF (`Guo 等 - 2026 - Video Prediction Policy 2 Predict Better, Act Better.pdf`, 21 pages) and `extracted_text.txt` (65,438 characters).
- **Deliverables:** `detailed_paper.md`, `paper.md` (exact byte-for-byte identical copy), `source_map.json`, and `translation_notes.md`.
- **Target Location:** `/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/Video Prediction Policy 2 Predict Better, Act Better/`

## 2. Document Structure and Coverage

The reader covers the full 21 pages of the manuscript without omission:
1. **Title & Frontmatter:** YAML frontmatter with title, aliases, tags, date, authors, and project page.
2. **Page / Section Index:** Mapping of PDF pages (1–21) to manuscript sections and visual assets.
3. **Terminology Ledger:** Core technical terminology with standardized English-to-Chinese pairs and conceptual explanations.
4. **Abstract:** Complete bilingual paragraph.
5. **1 Introduction:** 4 bilingual paragraphs introducing world action models, the two key limitations of prior WAMs, the VPP2 methodology, and three core empirical findings.
6. **2 Data Processing Pipeline:** 7 bilingual paragraphs detailing video data sources, filtering, segmentation, captioning, workspace/end-effector alignment, and T-shaped multi-view inputs.
7. **3 VPP2: A Generalist Policy with Zero-Shot Capability:** 15 bilingual paragraphs covering the overview, 3.1 video prediction pipeline (event-level continued pretraining, chunk-level post-training, consistency distillation), 3.2 action modeling (MoT architecture, LoRA adaptation, inference latency), and 3.3 VLM high-level planning.
8. **4 Experiments:** 11 bilingual paragraphs covering 4.1 video prediction quality analysis (GPT evaluator and human win rates) and 4.2 policy performance analysis (zero-shot real-world ALOHA, LIBERO-ID/Pro/OOD benchmarks, RoboDojo benchmark, and VLM subtask planning).
9. **5 Related Works:** 2 bilingual paragraphs surveying video foundation models and world action models.
10. **6 Conclusion:** Complete bilingual conclusion paragraph summarizing findings and implications for future WAM research.
11. **Acknowledgments & Statements:** Complete bilingual paragraphs for Acknowledgments, AI Use Statement, and Reproducibility Statement.
12. **References:** Searchable bibliographic entries [1]–[48] retained in full original citation form.
13. **Appendix A (Dataset Process Details):** Video sources, captioning template (A.1), and unified action space formulas (A.2).
14. **Appendix B (More Video Prediction Results):** Distillation comparison description and Figure 10.
15. **Appendix C (Detailed Benchmark Results):** C.1 Detailed LIBERO suite results (Table 6) and C.2 Detailed RoboDojo results (Tables 7 and 8).

## 3. Visual and Tabular Assets

- All 18 visual elements from the manuscript are embedded using relative links `assets/figure_X.png` (Figures 1–10) and `assets/table_X.png` (Tables 1–8).
- For all 8 tables, full Markdown transcriptions are provided immediately after the table image crop, followed by bilingual captions (`**Caption:**` and `**Caption[CN]:**`).
- All 10 figures are followed immediately by their bilingual captions.

## 4. Mathematical Notations and Technical Precision

- Inline math is formatted using standard `$...$`.
- Display equations (Equations 1–6) are placed outside blockquotes on standalone lines using `$$...$$` with tag numbers `\tag{X}`.
- Specific literals preserved include: $SE(3)$, flow matching objective $\mathcal{L}_{\text{FM}}$, consistency distillation loss $\mathcal{L}_{\text{CD}}$, resolution $416 \times 240$, sampling horizon $H = 8\text{s}$ (robot) and $2\text{s}$ (human), latents $17 \times 416 \times 240$, latency $0.12\text{s} + 0.10\text{s} = 0.22\text{s}$, and all benchmark percentages.

## 5. Quality and Validation

- Checked with `validate_detailed_paper.py` ensuring 0 syntax errors, 100% paired bilingual paragraphs, valid figure/table caption pairs, zero broken links, and byte-for-byte identity between `detailed_paper.md` and `paper.md`.
