# Translation / Extraction Notes

## Source and extraction

- Source file: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/WV97ZMIL/Zhang 等 - 2025 - A4-Agent An Agentic Framework for Zero-Shot Affordance Reasoning.pdf`
- Detected source format: selectable-text PDF (`pdf-text`).
- PDF metadata: 19 pages; arXiv GenPDF; arXiv:2512.14442v1, 16 Dec 2025.
- Text extraction used the embedded text layer; no OCR was used.
- Figures/tables were rendered from PDF pages at 200 dpi and cropped into `assets/`.

## Included content

- `paper.md` includes the main paper and supplementary material as a Chinese-English side-by-side reader.
- All major prose sections are represented: Abstract, Introduction, Related Work, Motivation, Method, Experiments, Conclusion, Supplementary implementation details, prompts, exploratory experiments, and intermediate-result demonstrations.
- Figures 1-13, Tables 1-6, and the Dreamer/Thinker prompt cards are included as separate image assets.
- The reference list is summarized by key clusters rather than translated entry-by-entry, because it is bibliographic material rather than argumentative prose.

## Translation policy

- Technical terms are kept consistent with the terminology ledger in `paper.md`.
- Mathematical notation was normalized to Markdown-compatible `$...$` and `$$...$$` delimiters.
- Visible paragraph labels use `Para. X:` / `Para. X[CN]:`; source provenance is stored in `source_map.json`, not as hidden comments in `paper.md`.

## Source issues and uncertainties

- The source paper appears to contain a numerical inconsistency: the text says A4-Agent reaches 71.83 gIoU on ReasonAff, while Table 1 reports 70.52 gIoU. The note in `paper.md` flags this and recommends using the table value unless a later author version resolves it.
- A few source typos or formatting artifacts were normalized in the reader for clarity, including forms such as `A4-Agentframework`, `geneative`, and OCR-like metric spellings in table captions. The substantive values were not changed.
- Crop boxes are manually selected from 200-dpi rendered pages and should be regarded as high-confidence visual crops, but not publisher-provided vector extractions.

## Output bundle

- `paper.md`: main bilingual reader.
- `source_map.json`: block IDs, pages, figure/table paths, crop boxes, captions, and glossary.
- `translation_notes.md`: this file.
- `assets/`: extracted figures, tables, and prompt cards.
