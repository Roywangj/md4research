# Translation and material notes

## Source inspection

- Source PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/G7H4ME3D/Peng 等 - 2026 - FACT Failure-Aware Causal Training for World-Action Models.pdf`
- PDF page count: 19 (verified with `pypdf.PdfReader`).
- Text extraction: all 19 pages yielded non-empty text through the PDF text layer. Pages 1–9 contain the main paper; pages 10–13 references; pages 14–19 appendices and tables.
- Page rendering: all 19 pages rendered to `assets/page-01.png` through `assets/page-19.png` at 120 dpi using `pdftoppm -png -r 120`.

## Coverage

The bilingual reader covers the title/author block, abstract, keywords, Figure 1, Sections 1–6, Figures 2–8, Tables 1–4, all 53 references, Algorithms 1–3, Appendices B–H, Figures 9–13, Tables 5–8, real-world prompts, the full 50-task RoboTwin table, and all reported numbers and inference-time values.

`paper.md` is a byte-for-byte copy of `detailed_paper.md`; it is not an abstract or shortened companion.

## Material-level caveats

1. The source is a two-column PDF. The text layer is readable, but extraction concatenates some column boundaries and removes spaces in mathematical expressions and table cells. Main prose, equations, captions, and table values were checked against rendered pages.
2. Figure assets are full-page renders rather than individual crops. This preserves every figure edge and label and avoids cropped/incorrect assets, but includes surrounding page context. Captions and searchable table transcriptions are placed in the reader.
3. Equations (1)–(10) were normalized from the PDF glyph stream into Markdown LaTeX while preserving variables, operators, intervals, clipping, and equation numbering. The PDF text layer rendered some superscripts/subscripts without spacing; rendered page images are the visual authority.
4. The PDF's Appendix D table has tightly packed values in the extracted text layer. Table 6 was transcribed from the rendered page 18, retaining all 50 task rows and the Average row.
5. Reference author names and bibliographic literals are retained in searchable original form. Chinese title glosses are added after each entry; they are translations, not replacements for the source bibliography.
6. No source page was missing or unreadable. No OCR-only page was required. No figure/table crop is claimed as an independently cropped asset.

## Deterministic checks performed/planned

- Page count and non-empty extraction: passed (19/19 pages non-empty).
- Asset count: passed (19 page renders for 19 source pages).
- Output boundary: a pre-write snapshot was taken with the local `file_boundary.py` tool; only the requested output tree is intended to be copied from the isolated worktree to the requested root.
- Detailed-reader validator: run the command reported in the completion message after copying the files to the requested root.
