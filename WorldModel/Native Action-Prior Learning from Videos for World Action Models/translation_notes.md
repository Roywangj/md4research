# Translation Notes: Native Action-Prior Learning from Videos for World Action Models

## Scope and Coverage

- **Manuscript Identity:** "Native Action-Prior Learning from Videos for World Action Models" (Zhaochong An, Fei Zhang, Menglin Jia, Duncan Frost, Zijian Zhou, Yikai Wang, Xudong Wang, Aditya Patel, Belinda Zeng, Tao Xiang, Serge Belongie, Amir Bar, Sen He; Meta AI / Physical Intelligence / Univ. of Copenhagen / Imperial College London, October 2026).
- **Source Material:** Full 27-page manuscript (`arXiv:2610.03391v1 [cs.CV]`, 2 Oct 2026, updated 5 Oct 2026), 91,185 characters extracted in `extracted_text.txt`, and original source PDF at `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/QDPQ5QXT/An 等 - 2026 - Native Action-Prior Learning from Videos for World Action Models.pdf`.
- **Structural Coverage:**
  - Frontmatter, Page / Section Index, Terminology Ledger
  - Title, Authors, Affiliations, Project Links
  - Abstract (3 paragraphs)
  - Section 1: Introduction (5 paragraphs, Figure 1)
  - Section 2: Related Work (2.1 World Action Models, 2.2 Learning from Observation-Only Videos)
  - Section 3: Method: NAVA-WAM (3.1 Preliminaries, 3.2 Native Action-Prior Pre-training, 3.3 Downstream Adaptation, Post-training and Inference; Equations 1–13, Figure 2)
  - Section 4: Experiments (4.1 Setup, 4.2 Main Results, 4.3 Analysis & Ablation Studies; Table 1, Table 2, Figures 3–6)
  - Section 5: Conclusion and Limitations (Conclusion, Acknowledgements)
  - References: Complete bibliography with all 95 citations preserved in searchable bibliographic format (`1. Author et al...`)
  - Appendix A: Theoretical Analysis of Native Action-Prior Learning (Propositions A.1 and A.2 with complete mathematical proofs; Equations 14–30)
  - Appendix B: Additional Implementation Details (B.1 Pre-training, B.2 Downstream Post-training, B.3 Transition-Structured Attention Masks, B.4 Benchmark Protocols, B.5 Action-Only Inference; Tables 3–4, Figure 7, Algorithm 1)
  - Appendix C: Additional Experimental Results (C.1 Pre-training Dynamics, C.2 Motion Transfer, C.3 Detailed Benchmarks, C.4 RoboTwin Rollouts, C.5 Real-Robot Evaluation; Tables 5–8, Figures 8–11)
  - Appendix D: Limitations (Contact-rich manipulation, lack of local execution error recovery)
  - *Note on Appendices:* The 27-page paper concludes with Appendix D Limitations on page 27; there is no Appendix E in the manuscript. All 27 pages are covered completely with 0 text omission.

## Deliverables and File Boundary

- Primary reader deliverable: `detailed_paper.md` (179,357 bytes, 81 bilingual paragraph pairs, 19 bilingual caption pairs, 19 local asset links, 0 broken links).
- Sibling mirror: `paper.md` is an exact byte-for-byte copy of `detailed_paper.md` (`sha256: b85f5216a701f87fdb130940b7434121e6042e621d11a56b2ecc15eda1b09658`).
- Traceability map: `source_map.json` mapping all 11 content blocks, 11 figures, and 8 tables to source pages and assets.
- Untouched files: `paper_DeepPaperNote.md`, `paper_DeepPaperNote.*.json`, and `images/` remain completely untouched as required by strict task rules.

## Formatting and Output Contract Compliance

1. **Paragraph Pair Structure:**
   Every paragraph adheres to the strict blockquote format:
   ```markdown
   > <span style="color:#3B82F6"><strong>Para. X:</strong></span> Original English text...

   > <span style="color:#F59E0B"><strong>Para. X[CN]:</strong></span> 严谨专业学术中文翻译...
   ```
2. **Display and Inline Mathematics:**
   All display mathematics are rendered on standalone lines outside blockquotes (`$$...$$`), with equation tags matching the source paper (Eqs. 1–30). Inline math uses `$..$` throughout. No raw LaTeX delimiters `\(...\)` or `\[...\]` are present.
3. **Visual Assets and Bilingual Captions:**
   All 19 local assets in `assets/` are linked with relative paths:
   - 11 Figures: `assets/figure_1.png` through `assets/figure_11.png`
   - 8 Tables: `assets/table_1.png` through `assets/table_8.png`
   Every figure is immediately followed by `**Caption:**` and `**Caption[CN]:**`.
   Every table image is immediately followed by a clean, contiguous Markdown table, followed by `**Caption:**` and `**Caption[CN]:**`.
4. **Table Transcription Fidelity:**
   - Table 1: Dual benchmarks (LIBERO/LIBERO-Plus and RoboTwin 2.0 Clean/Random).
   - Table 2: Triple ablation panels (a: label efficiency, b: action relevance $R^2$, c: inference compute).
   - Tables 3 & 4: Full training hyperparameters for LIBERO and RoboTwin 2.0.
   - Table 5: Per-suite breakdown on LIBERO (Spatial, Object, Goal, Long).
   - Table 6: Per-perturbation breakdown on LIBERO-Plus across all 7 distribution shifts.
   - Table 7: Complete 50-task breakdown on RoboTwin 2.0 (Clean and Random domains for 9 models) plus Average summary row.
   - Table 8: Real-robot per-task trials (T1, T2, T3) and normalized per-action execution latency on Franka FR3.

## Terminology and Translation Standards

- **World Action Model (WAM):** 世界动作模型（WAM）
- **Native Action-Prior Learning:** 原生动作先验学习
- **Mixture-of-Transformers (MoT):** 混合 Transformer 架构（MoT）
- **Video-DiT / Action-DiT:** 视频扩散 Transformer（Video-DiT） / 动作扩散 Transformer（Action-DiT）
- **Transition-structured Joint Attention:** 状态转移结构化联合注意力
- **Asymmetric Transition Attention:** 非对称转移注意力
- **Future-video Flow Matching:** 未来视频流匹配（Flow Matching）
- **Joint Video–Action Flow Matching:** 联合视频—动作流匹配
- **Latent Action:** 潜在动作
- **Representation-to-Control Transfer:** 表征到控制迁移
- **Target-Copying Shortcut:** 目标复制捷径（作弊解）
- **Continuous Action Chunk / Action Horizon:** 连续动作块 / 动作预测时域（$H$）
- **Action-Only Inference:** 仅动作推理
- **Visual Latent Cache ($\mathcal{C}_V$):** 视觉隐表征缓存
- **Proprioception / Proprioceptive State:** 本体感知状态（$q$）
- **In-Distribution (ID) / Out-of-Distribution (OOD):** 分布内（ID） / 分布外（OOD）跨域泛化

## Verification and Deterministic Testing

The reader was verified using `/Users/roywangj/Desktop/skills4ai/wj_skills/nature-reader-detail-wj/scripts/validate_detailed_paper.py`:
- Deterministic check: `passes: True`, 0 errors, 0 warnings.
- Byte-identity check: `--require-identical --source paper.md` confirmed 100% byte-for-byte identity.
- Visual elements check: 19 image links, 0 missing files, 19 balanced caption pairs.
- Reference check: 95 numbered bibliographic entries.
