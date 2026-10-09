# Translation Notes

## Scope

- Full 25-page reader for **GPIC: A Giant Permissive Image Corpus for Visual Generation**.
- Main paper, Broader Impact and Limitations, Acknowledgments, Appendix A-F, all substantive tables/figure captions, and the exact Appendix F prompt rules are represented in `paper.md`.
- The bibliography is preserved in searchable English bibliographic form rather than translated entry by entry, following the WJ reader convention.
- Body prose uses paragraph-level `Para. X:` / `Para. X[CN]:` pairs; the final reader contains 58 English/Chinese pairs.

## Source

- PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/JZ3SBICG/Chandrasegaran 等 - 2026 - GPIC A Giant Permissive Image Corpus for Visual Generation.pdf`
- Source type: selectable-text PDF (`pdf-text`), 25 pages, not encrypted.
- PDF metadata title and author list were checked with `pdfinfo`.
- Text was extracted from every page with Poppler and natural reading order was checked against rendered page images.

## Extraction and Layout

- The main paper uses a two-column layout on several pages. Line-break hyphenation was repaired and reading order was reconstructed semantically rather than copied from the raw stream.
- Poppler emitted embedded-font mismatch warnings during extraction, but page-by-page comparison showed no substantive text loss.
- Mathematical notation was normalized to Markdown-compatible `$...$` delimiters. No reader-facing `\(...\)` or `\[...\]` delimiters are intentionally used.
- Tables 1-3 and B.1-B.2 are both preserved as image assets and transcribed into Markdown so their values remain searchable.
- Appendix F prompt pages are preserved as high-resolution crops and their substantive rules are transcribed and translated in the bilingual body; the raster is the authority for exact visual formatting.

## Assets

- `assets/` contains 27 PNG files: 22 figure crops and 5 table crops.
- Crops were rendered from the PDF at 200 dpi and visually checked after a second tight-crop pass.
- Figure captions are kept as bilingual Markdown text next to the corresponding asset rather than baked into the crop wherever practical.
- Dense montage figures (Figures 1, A.1, and E.1) necessarily retain small internal text as part of the figure design; the source image is high resolution and can be opened directly for inspection.

## Translation Decisions

- Model, dataset, metric, and software names remain in English: GPIC, Qwen3-VL, SSCD, FAISS, JiT, FD-DINOv2, FID, Precision, Recall, Density, Coverage, vLLM, SGLang.
- `permissive` is consistently translated as “宽松许可”; `stable` as “稳定”; `accessible` as “易获取”; `caption` as “描述文本（caption）” when ambiguity is possible.
- `oracle reference` and `register token` are retained partly in English because there is no single stable Chinese equivalent in this context.
- Numeric values, dataset sizes, thresholds, model variants, citations, and reported metrics were preserved.
- Appendix F output literals such as `NOT VISIBLE.` and JSON key names remain exact.

## Skipped or Untranslated Material

- No substantive body or appendix section was skipped.
- Reference entries 1-37 are not translated line by line; they are retained in compact searchable English form.
- Page numbers, decorative headers, and repeated footer text are not reproduced.

## Material Limitations

- Figure-internal captions in large sample montages are part of raster assets; their exact typography and colored highlights are not recreated as editable Markdown.
- The source PDF is a v1 arXiv preprint dated 28 May 2026. Later revisions may change statistics, wording, or artifacts.
- The `nature-reader` manifest referenced a shared `terminology-ledger.md` file that was absent from the local skill installation. A paper-specific terminology ledger was therefore built directly in `paper.md` and mirrored in `source_map.json`.

## Verification Targets

- Parse `source_map.json` as strict JSON.
- Confirm all Markdown `assets/...` links exist.
- Confirm English and Chinese paragraph-label counts match.
- Confirm no `**Original:**` / `**中文:**` body labels, reader-visible HTML anchors, or unsupported math delimiters remain.
