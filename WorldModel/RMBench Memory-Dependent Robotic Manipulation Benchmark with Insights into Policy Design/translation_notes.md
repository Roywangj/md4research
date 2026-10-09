# Translation and Extraction Notes

## Source and processing status

- **Source:** `Chen 等 - 2026 - RMBench Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design.pdf`
- **Source type:** selectable-text PDF (`pdf-text`); 16 pages verified with `pdfinfo`.
- **Coverage:** pp. 1–9 main paper; pp. 9–11 complete References; pp. 12–16 Appendix A–C.
- **Reader identity requirement:** `paper.md` and `detailed_paper.md` are intentionally byte-identical copies.
- **Companion deep-reading package:** `paper_DeepPaperNote.md`, four validation/planning JSON artifacts, and 17 selected source-native crops under `images/` were completed after the bilingual reader and independently validated.

## Coverage ledger

| Category | Required | Included | Notes |
|---|---:|---:|---|
| PDF pages | 16 | 16 | Reader index and source map retain all page ranges. |
| Main-text equations | 9 | 9 | Eq. (1)–(9) rendered as standalone Markdown math. |
| Figures | 11 | 11 | Fig. 1–11 each have a native PNG crop, relative link, English caption, and Chinese caption. |
| Tables | 6 | 6 | Table 1–6 each have a native PNG crop, caption pair, and searchable Markdown transcription. |
| Reference entries | 38 | 38 | Full bibliography transcribed in `paper.md`; exact count from PDF pp. 9–11. |
| Appendix sections | A–C | A–C | Includes task descriptions, planning/execution training details, and failure analysis. |
| Bilingual paragraph pairs | — | 61 | All visible substantive prose uses `Para. X:` / `Para. X[CN]:` pairs. |

## Extraction and layout notes

- The source uses a two-column layout. Text was extracted from its selectable layer and reconciled against page-level layout extraction; paragraph text was reordered into natural reading order.
- Figure/table files in `assets/` are native rendered PDF crops (not whole-page screenshots). Crops are labeled through `source_map.json` with their source page, content role, caption ID, approximate crop box, and reader placement.
- Tables 1–6 are transcribed as Markdown in addition to their visual crop to make task definitions and values searchable.
- The bibliography contains 38 entries. The PDF itself contains bibliographic quirks retained in the reader (e.g., the two DiffusionVLA entries and `arXiv:None` in one source entry); no external normalization was introduced.
- The paper itself spells the Appendix-A task name as `Swap Block` in Table 4, while the main text and figures use `Swap Blocks`; both source forms are preserved where they occur.

## Terminology decisions

| English | Chinese used | Rationale |
|---|---|---|
| Task Memory Complexity (TMC) | 任务记忆复杂度 | Paper-defined task-side metric. |
| memory-dependent | 记忆依赖型 | Indicates decisions that require history beyond the current observation. |
| Anchor Memory | 锚点记忆 | Fixed first-frame memory within a subtask. |
| Sliding Memory | 滑动记忆 | Recent-token window. |
| Key Memory / key memory window | 关键记忆 / 关键记忆窗口 | Completed-subtask and terminal-observation memory. |
| Subtask End Classifier | 子任务终止分类器 | Paper’s classifier that triggers high-level replanning. |
| Planning Module / Execution Module | 规划模块 / 执行模块 | Kept consistent throughout reader and source map. |
| Vision-Language-Action (VLA) | 视觉—语言—动作 | Expanded at first use. |
| Diffusion Transformer (DiT) | 扩散 Transformer | Kept as established model name plus Chinese class term. |

## Confidence and limitations

- **Text and tables:** high confidence; all derive from the source PDF’s selectable text layer and were manually normalized for multi-column reading order.
- **Equations:** high confidence; visual Markdown normalization preserves Eq. (1)–(9). Equation (9) begins on PDF p. 6 after the p. 5 classifier subsection and is placed with Section 4.3 in the reader.
- **Crops:** high confidence for semantic figure/table content. Some crop boxes are approximate source-map coordinates because they are generated from 160-dpi PDF renders; they intentionally exclude prose margins where feasible.
- **No missing-source content is known:** Appendix A (task definitions), Appendix B (training details), and Appendix C (failure cases) are all included. No OCR was used.

## Validation target

Run:

```bash
python3 /Users/roywangj/Desktop/skills4ai/wj_skills/nature-reader-detail-wj/scripts/validate_detailed_paper.py \
  detailed_paper.md --source paper.md --require-identical
```

Expected checks: valid paired labels; 17 caption pairs (11 figures + 6 tables); 17 valid local image links; 38 numbered references; byte-identical reader files.
