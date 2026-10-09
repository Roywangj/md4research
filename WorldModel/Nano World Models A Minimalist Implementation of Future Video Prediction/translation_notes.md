# Translation Notes

## Scope

This deliverable covers the complete 19-page source PDF, including the title/author block, abstract, Sections 1–6, all six findings, Figures 1–6, Tables 1–7, footnote URL, and the full References section. No appendix or supplementary section is present in the supplied PDF.

## Source and extraction

- Source PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/AMCJCEKS/Huang 等 - 2026 - Nano World Models A Minimalist Implementation of Future Video Prediction.pdf`
- Source format: selectable-text arXiv PDF, 19 pages, `arXiv:2605.23993v2 [cs.CV]`, 27 May 2026.
- Text was extracted with `pdftotext -layout`. The PDF uses two-column layout on the body and bibliography pages; column order, page headers, and page numbers were removed or reordered manually to restore section order.
- Formula symbols and technical literals were preserved. Display math is normalized to `$$...$$`; no reader-facing `\\(...\\)` or `\\[...\\]` delimiters are used.

## Figures, tables, and assets

The `assets/` directory contains rendered local PNG page crops from the supplied PDF for the overview, qualitative rollout, logging, 3D export, table, long-horizon, and error-accumulation pages. Figure/table captions are paired in English and Chinese. Tables 1–7 are also transcribed as searchable Markdown; page-level PNGs are retained where a visual crop carries information not representable in the table.

Because several figures and tables share a page or are embedded in a multi-panel page, the local assets are page-level renders rather than tightly isolated panel crops. This avoids cutting axes, legends, table columns, or caption edges. Figure 4 is on the same rendered source page as the surrounding methods material, and Figures 5–6 are represented by their source pages.

## Bibliography policy

References are retained as original searchable bibliographic entries, including author names, titles, venues, pagination, URLs, DOIs, and arXiv identifiers. They are not translated line by line because translating bibliographic metadata would reduce auditability and make exact lookup harder. The preceding bilingual body translates every citation-bearing claim and preserves citation keys.

## Completeness and caveats

No source prose was intentionally omitted. The source contains no appendix, supplementary material, explicit limitations section, ethics statement, or acknowledgments section beyond the release/misson statements in the Introduction. Some PDF typography contains minor source-level spelling/grammar issues (for example, “admist”, “thrid”, “informations”, and “fails” agreement); the English side retains the scientific wording while the Chinese side translates the intended meaning. The extracted PDF includes an embedded graphical overview whose internal labels are not separately OCR-transcribed; its bilingual caption and local page asset are provided.
