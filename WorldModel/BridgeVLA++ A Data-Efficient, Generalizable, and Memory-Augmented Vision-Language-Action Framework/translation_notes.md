# Translation and Extraction Notes

## Scope

- `detailed_paper.md` and `paper.md` contain the same complete bilingual reader.
- Covered content: abstract, main Sections I–VI, central equations, all substantive appendices A–P, all 21 figure captions, all 19 table captions, main quantitative tables, evaluation protocols, computational cost, and failure-mode discussion.
- References remain in original searchable bibliographic form via `.pipeline/arxiv_src/main.bib`; they are not translated entry by entry.

## Source and provenance

- Primary source PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/UQ5DQRWD/Li 等 - 2026 - BridgeVLA++ A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework.pdf`
- Source type: 36-page selectable-text, two-column PDF.
- Stronger structural source: author-submitted arXiv LaTeX package for `2608.05042v1`, stored under `.pipeline/arxiv_src/`.
- The author LaTeX was used as the authority for paragraph order, equations, figure captions, table captions, and appendix structure; rendered PDF pages were visually checked at the first page, section boundaries, main tables, appendix start, full-result pages, and final gallery page.

## Layout and assets

- The deterministic DeepPaperNote PDF asset extractor did not return usable candidates for this PDF. Author-original vector figures were therefore obtained from the arXiv source package and rendered to PNG at 180 dpi.
- All 21 source figures are present in `assets/` with no broken links.
- Main tables are transcribed into searchable Markdown. Very wide per-task matrices (COLOSSEUM Tables VIII–X and GemBench Tables XIII–XVI) are preserved as rendered source pages in `assets/`; their aggregate values and substantive interpretation are searchable in the reader.
- The page renders for the wide matrices include neighboring text in addition to the table. This preserves every value and label, but is less visually compact than a hand-cropped table-only image.

## Terminology and literal policy

- Model, dataset, benchmark, metric, hardware, and code identifiers remain in English.
- `what to do next` / `where exactly to act` are translated consistently as “下一步做什么” / “精确在哪里操作”.
- Equations use `$...$` and `$$...$$`; all variables, operators, dimensions, thresholds, and numerical values are retained.
- The source contains no standalone Limitations, Ethics, Data Availability, prompt, or code appendix. Limitations are reconstructed only in the final critical-reading notes and DeepPaperNote, not presented as source prose.

## Validation

- Nature-reader-detail validator: passed.
- Bilingual paragraph pairs: 77.
- Caption pairs: 37 English / 37 Chinese.
- Image links: 27; missing: 0.
- `paper.md` is byte-identical to `detailed_paper.md` at delivery time.
