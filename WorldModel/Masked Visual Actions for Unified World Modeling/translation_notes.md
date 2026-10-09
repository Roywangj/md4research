# Translation and extraction notes

## Scope

- Completed against the user-provided selectable-text, unencrypted 21-page PDF.
- The reader covers the title/abstract, sections 1–6, all nine appendix sections (A–I), and the searchable English bibliography on pp. 10–15.
- Paragraph pairs use the required `Para. X:` / `Para. X[CN]:` blockquote form and restart at each major section.

## Terminology decisions

- “Masked Visual Actions” is rendered as **掩码视觉动作**; its English method name is retained at first use and where it functions as a proper name.
- “forward model” / “inverse model” are consistently **前向模型** / **逆向模型**.
- “active entity” / “passive entity” are consistently **主动实体** / **被动实体**.
- Dataset, benchmark, model, metric, and acronym names (DROID, RoboCasa, BEHAVIOR-1K, Wan-Fun-Control, LPIPS, SSIM, PSNR, VLM, LoRA, IDM) are intentionally retained.

## Figure and table handling

- Assets were rendered directly from the original PDF and cropped to the visual object area. Captions are transcribed and translated in `paper.md`; they are not baked into the crop.
- Extracted figure assets: Figs. 1–11. Extracted table assets: Tables 1, 2, and C1. Tables are also transcribed as searchable Markdown.
- Figure/table crop rectangles, source pages, caption IDs, and semantic placement pointers are recorded in `source_map.json`.

## Extraction confidence and caveats

- Main prose, captions, tables, and appendix prose are high-confidence selectable-text extraction.
- The bibliography is deliberately retained as searchable English, as requested; it is not translated paragraph by paragraph.
- Mathematical expressions have been normalized to Markdown-compatible `$...$` / `$$...$$` delimiters. Equation typography is reconstructed from the selectable text and visual page inspection.
- The installed reader workflow requested a separate `pdf` skill, but no such skill was available in this session. Direct selectable-text extraction and rendered-page inspection were used instead.

## Validation record

- JSON parse: **passed** (`source_map.json`).
- Paragraph pair adjacency/parity: **passed** — 75 English `Para. X:` blocks and 75 immediate Chinese `Para. X[CN]:` counterparts.
- Caption parity/locality: **passed** — 14 English/Chinese caption pairs, each attached to a local figure/table card; all 14 assets resolve under `assets/`.
- Math delimiter audit: **passed** — visible math uses `$...$` or standalone `$$...$$`; no legacy `\(...\)` / `\[...\]` delimiters remain.
- Page and section inventory: **passed** — `source_map.json` contains coverage entries for every PDF page 1–21. The system prompt begins on p. 17 and continues on p. 18; this span is recorded under one stable source block (`S063`).
- Legacy body labels: **passed** — no `Original:` or `中文:` body labels.
- Visual inspection: source PDF pages 1–21 were rendered and inspected for the two-column reading order; all 14 visual assets were rendered from tight page clips and visually checked against their source pages.
