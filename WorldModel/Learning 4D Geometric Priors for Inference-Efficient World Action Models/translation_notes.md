# Translation and extraction notes

## Scope and completion

- Source: `Zhang 等 - 2026 - Learning 4D Geometric Priors for Inference-Efficient World Action Models.pdf`
- Source type: selectable-text PDF (`pdf-text`), 9 pages.
- Coverage: complete. Reader body covers pp.1–7; the complete References section on pp.8–9 is preserved as 42 bilingual author—year entries.
- No appendix appears in the source PDF.
- `detailed_paper.md` is the canonical reader; `paper.md` is required to be byte-identical.

## Source map and visual assets

- `source_map.json` uses stable `S` text, `E` equation, `F` figure, `T` table, `C` caption, and `R` reference IDs.
- Assets are rendered as tight crops from the supplied PDF page regions, with captions separately transcribed rather than baked into crops.
- Extracted native visual objects: Figures 1–6 and Tables 1–4. Each has a valid relative `assets/...` link, an English `Caption`, a Chinese `Caption[CN]`, and a source-map record.
- Important result tables (Tables 1–4) are additionally transcribed in searchable Markdown.

## Equation handling

- All source equations Eq. (1)–(23) are retained in Markdown-friendly display math.
- Eq. (8) is rendered as the standard scaled-dot-product masked attention expression, $\operatorname{softmax}(QK^\top/\sqrt d+M)V$, consistent with the visual PDF.
- The PDF uses `k+` as a next-selected-keyframe notation in Eq. (16)–(19); the reader writes this as $k^+$ without assuming it means a fixed $k+1$ frame.

## Terminology decisions

| Source term | Chosen Chinese | Rationale |
|---|---|---|
| World Action Model (WAM) | 世界动作模型 | First use expands then retains WAM. |
| MECo-WAM / Multi-Expert Co-Training | MECo-WAM／多专家协同训练 | Method name and framework name kept fixed. |
| 4D geometric priors | 四维几何先验 | Covers geometry and its temporal evolution. |
| frozen VGGT | 冻结 VGGT | Teacher is a training-only frozen encoder. |
| decayed 4D read-mask attention | 衰减式四维读掩码注意力 | Fixed module name. |
| action-aware temporal geometric distillation | 动作感知时序几何蒸馏 | Fixed objective name. |
| relational matching | 关系匹配 | Captures pairwise feature-relation alignment. |
| action chunk | 动作块 | Horizon-$H$ action sequence. |

## Faithfulness and uncertainty notes

- No OCR was used; text came from the selectable PDF layer and was checked against visual layout where mathematical glyphs mattered.
- Page 1’s PDF source repeats the lead-in “More importantly” around the generic-supervision argument. The reader retains the substantive claim once rather than carrying forward a likely source-level duplication.
- Table 3’s printed `π0` / Sort Cubes by Size completion-time average is `30.82`; it is transcribed verbatim even though it appears inconsistent with the displayed per-test values. No inferred correction was made.
- References are not numbered in the PDF. The verified bibliography count is **42 author—year entries**, recorded in both this file and `source_map.json`.

## Companion deep-reading package

- `paper_DeepPaperNote.md`、四个规划/验证 JSON 文件与 `images/` 中的 9 个源生图表裁剪，已在双语 reader 完成后合并到规范目录。
- 精读包与 reader 使用分离的图像目录；合并未覆盖 `paper.md`、`detailed_paper.md`、`source_map.json` 或 `assets/`。
