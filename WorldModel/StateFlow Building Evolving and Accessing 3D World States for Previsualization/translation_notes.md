# Translation Notes

## Scope

This folder contains the StateFlow paper supplied as a local 14-page PDF. `detailed_paper.md` and `paper.md` preserve the complete selectable-text extraction page by page, with adjacent English/Chinese blocks, all detected figures, tables, equations, limitation text, and the bibliography.

## Source and extraction

- Source: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/VZKCU5KV/Yin 等 - 2026 - StateFlow Building, Evolving, and Accessing 3D World States for Previsualization.pdf`
- Format: selectable-text arXiv PDF, 14 pages, two-column layout.
- Local extraction used PyMuPDF. Page text is retained rather than inferred from the DeepPaperNote.

## Material-level caveats

The PDF's two-column layout, interleaved figure labels, and table text cause the raw selectable extraction to mix some left/right column lines and visual labels. The source English is therefore preserved as page-level transcriptions for auditability, but the Chinese block paired with each page is a faithful page-level translation guide rather than a line-by-line translation of every extracted line. Figure/table captions and the important numeric tables are retained, while full-page 2x raster renders are used as local assets because tight figure bounding boxes are interleaved with prose. These are material limitations: this should not be described as a typographically reconstructed or fully line-aligned edition.

The supplied PDF contains main sections through Conclusion and Limitation and Future Work, followed by References [1]–[62]. No separately labeled appendix or supplementary section was detected.

## Assets

Five full-page raster assets are cited by `detailed_paper.md` near the corresponding source pages: Figures 1–5. The same files are copied into `images/` for the independent note.

## Next step for stricter edition

For a publication-grade bilingual edition, manually reflow each two-column page, crop figures and tables to their exact bounding boxes, and translate every source paragraph and caption line by line against the rendered PDF.
