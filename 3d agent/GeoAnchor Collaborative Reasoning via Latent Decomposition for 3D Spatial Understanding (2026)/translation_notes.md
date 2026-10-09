# Translation notes

## Source and mode

- **Mode:** Repair/restoration of a truncated detailed reader, with the omitted final appendix pages restored from the supplied PDF.
- **Source:** `Li 等 - 2026 - GeoAnchor Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding.pdf`, arXiv:2607.13454v2.
- **Physical pagination:** 23 physical PDF pages, confirmed deterministically with `pypdf`; main paper printed pp. 1–15 occupy physical pp. 1–15, and the appendix restarts at printed p. 1 on physical p. 16 and continues through printed p. 8 on physical p. 23.
- **Output boundary:** Only `detailed_paper.md`, `paper.md`, `source_map.json`, `translation_notes.md`, and existing `assets/` content in the requested target directory were in scope. The pre-existing unsuffixed GeoAnchor directory was not modified.

## Extraction and translation method

- The source PDF was inspected page by page with the local PDF reader. Physical pages 21, 22, and 23 were read separately, and physical pages 19–23 were inspected as a continuity window.
- Deterministic `pypdf` extraction reported **23** physical pages and was used to confirm the final-page boundaries. The restored material was transcribed in source order and translated immediately after each prose paragraph using the required `Para. X:` / `Para. X[CN]:` format.
- Technical identifiers, model and dataset names, citations, equations, units, numbers, table values, JSON keys, prompt sentinels, and code-like literals were preserved. References remain in searchable original bibliographic form.

## Coverage inventory

- Abstract and metadata.
- Main Sections 1–6, including Introduction, Related Works, Method, Experiment, Conclusion, and Acknowledgement.
- Main equations (1)–(11), appendix equations (1)–(5), figures and bilingual captions, searchable main and appendix tables, references, prompts, and exact JSON examples.
- Appendix A, Appendix B, and Appendix C through the complete dense-alignment baseline discussion in C.2.2.
- Physical pages 21–23: Table 9 (SpatialLadder-26K statistics); complete Table 10 (implementation details, including hardware, geometry balance, pattern reward, and EMA settings); the full Adaptive Pooling and Linear Interpolation descriptions; Equation (5); Table 11; Table 12; Sections D.1–D.3; and Tables 13–14.

## Ambiguities and material caveats

1. Several reference author spellings and a few dense table labels were visually small. Identifiers and values were retained where legible; one visually uncertain reference remains explicitly marked in the reader rather than silently corrected.
2. The source contains a likely typographical fragment in the Stage 2/3 ablation paragraph (“confirming that it alleviates value lies...”); the English source is retained as read, while the Chinese translation conveys the intended comparison without silently rewriting the source.
3. Existing local SVG schematics were reused. No new assets were added for physical pages 21–23 because their substantive content is text, equations, tables, and captions; all restored table values are searchable in Markdown. No source-grounded PDF crop was invented.
4. The source-native table layout uses grouped/multi-row headers; the Markdown transcriptions retain every source value and identifier in individually searchable rows, with compact headers where needed for Markdown readability.

## Validation record

- Physical source page count: **23**.
- Page/section anchors: checked across main physical pp. 1–15 and appendix physical pp. 16–23; physical pp. 19–23 were separately inspected for continuity.
- Local links: existing asset links resolve under `assets/`; no broken local image links were introduced.
- JSON and source map: updated for 23 physical pages and appendix physical pp. 16–23; parsed and structurally checked.
- Copy identity: `paper.md` was regenerated as an exact byte copy of the finalized `detailed_paper.md`.
- Final validator: `validate_detailed_paper.py --source paper.md --require-identical` **passed**; it reports 78 bilingual paragraph pairs, 12 original/12 Chinese caption pairs, and 4 image links with 0 missing.
- Copy identity: `paper.md` was regenerated as an exact byte copy of the finalized `detailed_paper.md` and `cmp` passed.
- Boundary verification: the repair files themselves stayed within the requested allowlist, but the pre-change boundary snapshot detected concurrent changes in five forbidden pre-existing `paper_DeepPaperNote*` files (`paper_DeepPaperNote.figure_decisions.json`, `paper_DeepPaperNote.grounding.json`, `paper_DeepPaperNote.lint.json`, `paper_DeepPaperNote.md`, and `paper_DeepPaperNote.plan.json`). They were not read, edited, reverted, or otherwise touched by this repair, so the strict pre-change boundary command cannot honestly be reported as passed. No changes were made to the unsuffixed GeoAnchor directory.