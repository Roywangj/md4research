# Translation notes

## Scope

- Source: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/A94M5EQ5/Li 等 - 2026 - Learning How the World Evolves Extrapolative Video World Models via Latent Dynamics Reasoning.pdf`
- Source type: 9-page selectable-text arXiv PDF, two-column layout, arXiv:2608.09926v1 (10 Aug 2026).
- Delivered: complete bilingual `detailed_paper.md`; byte-identical `paper.md`; `source_map.json`; eight local figure/table crops in `assets/`.

## Extraction and layout

The PDF uses a two-column conference layout. Text was extracted with `pdftotext -layout` and cross-checked against rendered page images, especially the column transitions, equations, algorithm, captions, tables, footnote markers, and the references pages. A few PDF text-layer glyphs in equations (overdots, hats, bold script symbols, and superscripts) are visually ambiguous in plain extraction; the displayed equations in the reader were reconstructed from the rendered source while retaining the paper's variable names and equation numbering. The source contains no appendix or supplementary section beyond the main paper, footnotes, and references.

## Assets and crop caveats

The assets are actual PNG crops rendered from source PDF pages at 120 dpi. Figure 1, Figure 2, Figure 3, Figure 4, Figure 5, Tables 1–2, Tables 3–4, and Table 5 are each referenced by local relative links. Crops preserve the substantive panels/cells and captions are transcribed separately in bilingual form. The table crops are visual supplements; searchable Markdown tables are included for all quantitative values. The source combines figures and tables with surrounding prose on pages 3–6, so crop boundaries follow the visual panel rather than the original page boundary.

## Translation policy and references

Model, dataset, metric, benchmark, equation, variable, citation, and software identifiers remain in their original literal form. Chinese translations follow each English source block using the required `Para. X` / `Para. X[CN]` blockquote pattern. Bibliographic entries are retained in original English form for auditability, with a following Chinese title/use translation; this is intentional and avoids altering author names, venues, years, and arXiv identifiers.

## Caveats

- The PDF has no separate acknowledgments, data-availability statement, or appendix; none was silently omitted.
- The visual source contains small labels in Figure 1–5 and tables. The crops are readable at their rendered resolution, while all substantive table numbers are additionally transcribed as Markdown.
- No claim is made that the translated Chinese prose is an official author translation; it is a faithful reader translation aligned paragraph by paragraph to the supplied PDF.
