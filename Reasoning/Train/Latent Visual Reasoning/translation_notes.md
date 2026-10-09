# Translation and verification notes

## Invocation and source

- Workflow: `nature-reader-wj`, selectable-text PDF (`pdf-text`).
- Source PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/WP65QDXJ/Li 等 - 2025 - Latent Visual Reasoning.pdf`.
- Source version: 15-page arXiv PDF, `2509.24251v2` (5 Oct 2025).
- Extraction basis: `pdftotext -layout`, rendered-page inspection inventory, and the already validated paragraph-aligned bilingual `detailed_paper.md`.
- Deliverable relationship: `paper.md` is an independent, complete nature-reader-wj reader. `detailed_paper.md` remains the retained detailed bilingual source/read-through rather than a pointer target for the main translation link.

## Coverage

- Complete source-order coverage of PDF pages 1–15.
- Includes metadata, Abstract, Sections 1–7 and all numbered subsections, Equations (1)–(6), Figures 1–2, Tables 1–3, complete searchable references, and Appendix A.1.
- `paper.md` contains 39 substantive English/Chinese paragraph pairs and 5 English/Chinese caption pairs.
- References remain in their original bibliographic language for reliable author/title/URL/arXiv searching; the bilingual notice explains this deliberate treatment.
- A short critical reading note appears only after the complete bilingual body.

## Terminology decisions

- “Latent Visual Reasoning” → “潜在视觉推理”; retain `LVR` after first use.
- “latent visual thoughts” → “潜在视觉思维”.
- “Thinking about Images” → “思考图像”; “Thinking with Images” → “借助图像思考”.
- “region of interest” → “感兴趣区域（ROI）”; retain `ROI` thereafter.
- Keep model, dataset, benchmark, metric, and identifier names in English, including `GRPO_latent`, `<|lvr_start|>`, and `<|lvr_end|>`.
- Keep `token` in English within technical Chinese prose; preserve mathematical symbols, hyperparameters, hardware, step counts, and runtime exactly.
- The complete canonical ledger is mirrored in `paper.md` and `source_map.json`.

## Figures, tables, and crop caveats

- `assets/` materializes five reader-facing files by copying the already validated crops from `images/`; `images/` was not altered.
- Stable reader-facing assets:
  - `assets/figure-1-lvr-concept.png`
  - `assets/figure-2-lvr-pipeline.png`
  - `assets/table-1-vision-centric-results.png`
  - `assets/table-2-rl-results.png`
  - `assets/table-3-ablation-results.png`
- The crops are reused as validated artifacts; no new bounding-box recrop was attempted. Accordingly, `bbox` is `null` and provenance is recorded as `reused validated crop` in `source_map.json`.
- All five assets are placed near their first substantive discussion, include English and Chinese captions, and Tables 1–3 retain searchable Markdown transcriptions alongside their images.

## Validation

- Verified equal `Para. X:` / `Para. X[CN]:` counts and section-local pair numbering: 39 / 39.
- Verified English/Chinese caption pairs: 5 / 5.
- Verified stable source IDs: 39 `S` blocks, 5 `C` blocks, 2 `F` records, and 3 `T` records; all IDs are unique.
- Verified `source_map.json` parses as JSON, retains the full 15-page inventory and source metadata, and records page, provenance, placement, glossary, and coverage.
- Verified Equations (1)–(6) are present with Markdown-compatible standalone `$$...$$` delimiters; no reader-facing `\(...\)` or `\[...\]` delimiters occur.
- Verified all five relative image links resolve to files under `assets/`; no broken image links occur.
- Verified complete section coverage through Appendix A.1 and that the critical reading note follows, rather than replaces, the paper body.
- Verified forbidden visible body labels/anchors/provenance comments are absent: no `Original:`, `中文:`, HTML anchors, or hidden source comments.
