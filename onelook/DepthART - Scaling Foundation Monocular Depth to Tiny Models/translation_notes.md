# Translation notes: DepthART

- **Scope:** Full 11-page arXiv PDF, including ACM front matter, abstract, Sections 1–5, equations (1)–(8), Figures 1–6, Tables 1–6, limitations/future work, and References [1]–[69].
- **Source:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/EZEJ6U4I/Xue 等 - 2026 - DepthART Scaling Foundation Monocular Depth to Tiny Models.pdf`; selectable text, two-column layout.
- **Extraction/layout:** `pdftotext -layout` was used for inventory. Because columns and composite tables/figures interleave, every page was also rendered at 120 DPI and retained under `assets/page-XX.png`. The page renders are the visual authority for exact table/figure positioning.
- **Terminology:** Model, dataset, encoder, decoder, metric, and software names remain English. `zero-shot`, `scale`, `shift`, `prompt`, `adapter`, `teacher`, and `student` are preserved where translating would reduce implementation precision.
- **Equations:** Equations (1)–(8) were normalized to reader-facing `$...$`/`$$...$$` delimiters; symbols, constants, dimensions, and literal values were retained.
- **Tables:** Tables 1–6 have searchable Markdown transcriptions in `detailed_paper.md`; page images preserve the original visual tables and bold/colour emphasis. Table 1's long Depth Anything v2 rows are represented with their source values in the detailed table and the page render.
- **References:** Kept in searchable bibliographic form rather than translated line by line, as required by the detailed-reader contract. Page 10–11 renders preserve the complete original entries.
- **Untranslated/skipped material:** No substantive paper section was skipped. The PDF contains no appendix or supplementary section. Generic conference title, DOI, ISBN, and permission boilerplate are source-native placeholders and are retained, not silently completed.
- **Caveat:** This is a faithful detailed reader rather than a typeset facsimile; the local page renders should be used to audit exact multi-column visual order.
