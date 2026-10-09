# Translation Notes — Code2Worlds

## Scope

- Built as a Chinese-English Markdown reader for `Code2Worlds: Empowering Coding LLMs for 4D World Generation`.
- Output follows the existing vault style used by `3dAgent/Skill-3D/paper.md`: section-level bilingual reading blocks with `Para. X` / `Para. X[CN]`.
- The main paper and appendices A-G are covered. The bibliography is preserved in the PDF and is not translated line-by-line.

## Source and extraction

- Source format: selectable-text PDF (`pdf-text`).
- Source PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/7GVZKM2T/Zhang 等 - 2026 - Code2Worlds Empowering Coding LLMs for 4D World Generation.pdf`.
- The PDF extraction contained multi-column reading-order noise, especially around Figure 2 and the transition from Related Work to Method. The reader file cleans this into the intended section order.

## Assets

- `assets/` contains 28 PNG candidates copied from the earlier DeepPaperNote extraction.
- Main inserted assets in `paper.md`: Figure 1, Figure 2, Figure 3, Figure 4, Tables 1-6, Figures 7-20, and Figure 23.
- Table 6 crop is incomplete in the extracted PNG candidate; therefore the reader includes a complete Markdown transcription of the prompt table.
- Some appendix prompt figures were not available as clean independent crops in the extraction. The reader summarizes and translates their substantive prompt design in Appendix G.

## Known caveats

- This is a polished paper-reader translation, not a legal facsimile of every line in the PDF. It preserves the argument, equations, metrics, tables, and appendix content in reading order.
- Code blocks and bibliographic entries are not translated line-by-line; code is discussed and figure captions are translated.
- If a strict paragraph-by-paragraph verbatim bilingual edition is required later, the next step would be to run a page-by-page extraction pass and expand `source_map.json` to every PDF paragraph block.
