# Translation Notes

## Source and coverage

- Source: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/59DCWCTW/Li 等 - 2026 - Perceptual Flow Network for Visually Grounded Reasoning.pdf`
- Source type: selectable-text PDF.
- Paper identity: arXiv:2605.02730v1, accepted to ICML 2026.
- Coverage: all 36 pages were extracted and inspected; the reader contains 80 bilingual paragraph pairs, 22 figure/table cards, and a 36-page source index.
- Reader mode: full-paper bilingual reading, not abstract-only or summary-only mode.
- Paragraph organization: counters restart at each major section; stable source IDs are stored only in `source_map.json` so the rendered reader remains clean.

## Terminology ledger

| Source term | Translation | Consistency note |
|---|---|---|
| Perceptual Flow | 感知流 | Method-defined structured latent trajectory |
| Planning State | 规划状态 | The initial text state $z_0$ |
| Perceptual State | 感知状态 | Each RoI-caption pair $\langle r_k,c_k\rangle$ |
| Visually Grounded Reasoning | 视觉落地推理 | Kept distinct from generic visual reasoning |
| reasoning utility / efficacy | 推理效用 | Refers to usefulness for inducing the target answer |
| geometric precision | 几何精度 | Refers to spatial agreement with expert RoIs |
| Sub-Trajectory Balance | 子轨迹平衡 | `SubTB` remains available as the English abbreviation |
| variational reinforcement fine-tuning | 变分强化微调 | Abbreviated as `RFT` when needed |
| vicinal geometric shaping | 邻域几何塑形 | “邻域” emphasizes support around, rather than equality to, expert priors |
| Chamfer-IoU distance | Chamfer-IoU 距离 | Proper metric name retained |
| tunnel vision | 隧道视野 | Context loss caused by overly tight evidence crops |
| test-time scaling | 测试时扩展 | Additional independent samples at inference time |

## Text and equation handling

- PDF line wrapping, ligatures, running headers, page numbers, and duplicated figure text were removed from the visible prose.
- Core equations were reconstructed with standard `$...$` and `$$...$$` delimiters. Display equations remain outside blockquotes so Obsidian/MathJax can render them.
- The PDF extractor grouped several main-text subsections into a broad `Introduction` record. Section titles and page boundaries were therefore recovered from page layout and verified against the rendered PDF.
- Theorem statements and appendix proofs were translated at the level needed to preserve assumptions, factorization, limit regimes, and proof logic. Long algebraic expansions are represented by their defining equations and argument sequence rather than duplicated line by line.

## Figures and tables

- `assets/` contains 16 figures and 6 tables. Every asset has one figure/table card in `paper.md`, with original caption, Chinese caption, and reading note.
- Figures 4 and Tables 1, 2, and 6 were manually re-cropped from rendered pages because the automatic extraction included adjacent prose or clipped rows.
- Tables 4 and 5 were initially marked as visual defects by the automatic quality heuristic; manual inspection confirmed that their table bodies and values are complete, so they were retained.
- Figures 2 and 7 were initially low-priority candidates, but manual inspection showed that they directly support the objective comparison and test-time-scaling argument, so they were retained.
- Figure 5 was not inserted because its automatic crop contains substantial surrounding body text and is not a tight valid figure crop. Its RoI-count and flow-length statistics are translated in Section 3.1. This is the only figure asset omitted from the reader.

## Bibliography policy

- Pages 13-16 contain 66 bibliographic entries. Author names, titles, venues, identifiers, and URLs are metadata rather than translatable argumentative prose, so they remain in their original language in the source PDF.
- The bibliography range is represented by stable block `R001` in `source_map.json`; the main reader includes a bilingual coverage note instead of mechanically translating 66 titles.

## Confidence and limitations

- Confidence is high for paper identity, body prose, numerical results, captions, and manually inspected crops.
- Mathematical symbols damaged by PDF text extraction were checked against page renders before reconstruction.
- Paragraph blocks in `paper.md` are cleaned, aligned reading units. A few long source paragraphs were divided or adjacent short paragraphs merged to keep English-Chinese alignment readable; source order and claim chains were preserved.
- No source pages are missing and the output is not in draft mode.

