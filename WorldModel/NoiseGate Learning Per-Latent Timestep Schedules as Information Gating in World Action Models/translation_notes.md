# Translation Notes — NoiseGate

## Source and extraction

- **Primary evidence:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/AWLP29XD/Huang 等 - 2026 - NoiseGate Learning Per-Latent Timestep Schedules as Information Gating in World Action Models.pdf`
- **Identity:** *NoiseGate: Learning Per-Latent Timestep Schedules as Information Gating in World Action Models*; Wen Huang et al.; arXiv:2605.07794v1 [cs.RO]; 8 May 2026.
- **Format:** selectable-text PDF (`pdf-text`); `pdfinfo` reports 17 pages, letter pages (612 × 792 pt), no encryption, and no OCR requirement.
- **Extraction:** text was extracted with `pdftotext -layout`; every page was rendered with `pdftoppm` for layout and figure/table verification. The PDF is a two-column arXiv preprint with figures and tables interleaved in the main text and appendices.

## Coverage inventory

- **Pages:** 17/17 inventoried and represented in `source_map.json`.
- **Sections:** Abstract; §§1–6; Appendices A–F; subsections §3.1–§3.3, §4.1–§4.4, §5.1–§5.5, §F.1–§F.2; References [1]–[41].
- **Technical blocks:** equations (1)–(11), Algorithm 1, Table 1–5, Figure 1–7, all caption text and appendix hyperparameters.
- **Bilingual alignment:** every substantive prose block in the reader has an adjacent English `Para. X:` block and Chinese `Para. X[CN]:` block. Source-native algorithm literals are preserved and their explanatory steps are translated inline.

## Translation policy and terminology

- Model, dataset, benchmark, metric, API, optimizer, and code-like identifiers remain in English when that preserves precision: NoiseGate, WAM, MoT, GPN, Diffusion Forcing, GRPO, RoboTwin, Wan 2.2, Fast-WAM, LingBot-VA, Motus, Shared-$t$, and Hand-crafted.
- Mathematical symbols, superscripts/subscripts, intervals, units, percentages, arrows, and numeric values are retained. Display equations use standalone `$$...$$` blocks; inline math uses `$...$`.
- References remain searchable source-native bibliographic entries. They are not paraphrased or translated because names, titles, identifiers, venues, years, and pages are citation evidence.

## Figures, tables, and assets

- Assets were created by rendering the supplied PDF at 150 dpi and cropping the visual content rather than using a full-page screenshot. `fig3.png` and `fig4.png` are separate crops from the two-panel Figure 3/4 page; `table1.png`–`table5.png` are page-rendered table crops.
- Crop rectangles are approximate but exclude page headers, footers, and unrelated prose. Captions remain in the Markdown and are paired in English and Chinese. Tables are also transcribed as searchable Markdown.
- No broken local image links are intended; all `assets/*.png` links used by the reader are within the target directory.

## Uncertainty and source conflicts

- The text layer interleaves some equation glyphs and column fragments. Equations (1)–(11) and the Algorithm 1 update equations were reconstructed by checking the rendered pages against surrounding prose; no values or symbols were intentionally omitted.
- Figure 2’s page layout and the Appendix C interface use related but not identical range notation (`(0,2)^F` in §4.3 versus `(0,1)^F` in Appendix C). Both source forms are retained in their respective contexts rather than silently normalized.
- Table 1 contains an ellipsis row (`···`) in the source; it is retained as `$\cdots$` and the omitted rows are explicitly stated to be expanded in Appendix E.

## Availability and limitations

- The supplied PDF contains no separate code-availability, data-availability, competing-interests, or acknowledgments statement. The reader records this absence rather than fabricating a statement.
- The source itself states the schedule-policy training limitation: simulator rollout collection dominates cost under sparse success rewards, and scaling a general policy to large multi-task suites remains future work.
- The source is an arXiv preprint (`v1`); numerical results and benchmark provenance are reported as claims from the PDF and were not independently reproduced.

## Validation record

- `detailed_paper.md` and `paper.md` are intended to be byte-identical copies.
- `source_map.json` is UTF-8 JSON and records paragraph, caption, figure, table, reference, page, section, order, relation, confidence, and asset-path metadata.
- Deterministic validation command required by the local skill:

```bash
python3 /Users/roywangj/Desktop/skills4ai/wj_skills/nature-reader-detail-wj/scripts/validate_detailed_paper.py \
  "/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/worldmodel/NoiseGate Learning Per-Latent Timestep Schedules as Information Gating in World Action Models/detailed_paper.md"
```

- Strict target-boundary verification uses the pre-write snapshot `/tmp/noisegate-boundary.json`; only the requested target directory was created/modified. Companion `paper_DeepPaperNote.md`, its JSON files, `images/`, and files outside the target directory were not touched by this workflow.
