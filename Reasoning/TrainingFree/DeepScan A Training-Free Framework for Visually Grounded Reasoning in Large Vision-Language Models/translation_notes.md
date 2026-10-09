# Translation and Extraction Notes

## Processing status

- Source format: selectable-text PDF (`pdf-text`), 18 pages.
- Paper type: CVPR methods / algorithm paper with supplementary material.
- Included: abstract, main paper, acknowledgments, supplementary discussions, prompts, pseudocode, additional results, qualitative examples, critical reading notes, and the complete numbered bibliography.
- Visual assets: 30 tight crops covering 14 numbered figures, 10 numbered tables, prompt templates, two algorithms, and three Example 1 output panels.

## Translation policy

- Technical names and model/dataset names remain in English.
- `visually grounded reasoning` is consistently translated as “视觉落地推理”.
- `grounding` is translated as “落地/定位” according to context; it does not mean physical grounding.
- English paragraphs are cleaned for line breaks, ligatures, and two-column reading order. Closely connected source paragraphs are occasionally merged into one aligned pair so that the reader remains coherent; technical claims, equations, metrics, methods, limitations, and supplementary discussions are retained.
- Equations use Markdown-compatible `$...$` and `$$...$$` delimiters. Equations (14)-(16) are represented in the accompanying prose because they are intermediate inequalities supporting the four-state pruning argument; the exact printed forms remain visible in the source PDF.
- Bibliographic entries are preserved in a compact original-language list and are not translated title-by-title.

## Extraction uncertainty and source issues

- The PDF text layer is high quality. Figure/table crops were verified against 200-dpi renders.
- The source PDF itself shows an unresolved citation marker `[?]` after “Otsu's method” on page 3; this is preserved as a source issue rather than guessed.
- The paper states that code “will be open-source”; the supplied PDF does not provide a resolvable repository URL.
- Supplementary pages 16-18 are predominantly screenshot-style qualitative output panels. They are preserved as images because OCR would lose layout and model-output relationships.
- The source map uses section- and asset-grounded page mapping. Bounding boxes are intentionally omitted (`[]`) because visual provenance is preserved by exact page number and cropped asset path rather than exposing approximate coordinates.

## QA record

- Relative image paths resolve under `assets/`.
- `source_map.json` is generated from the final bilingual paragraph pairs and visual cards.
- No OCR was applied to selectable prose.
- No browser-only Q&A widget or hidden Markdown provenance comments were added.
