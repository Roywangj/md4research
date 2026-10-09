# Translation and extraction notes

## Scope

- Complete 19-page selectable-text PDF processed in source order.
- Main paper: pages 1–9; searchable references [1]–[98]: pages 10–15; post-reference appendix/supplement: pages 16–19.
- `detailed_paper.md` is authoritative; `paper.md` is a byte-identical copy.

## Canonical source

- PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/YWKZTTTF/Zhang 等 - 2026 - ImageWAM Do World Action Models Really Need Video Generation, or Just Image Editing.pdf`
- SHA256: `0bf354364a18a2e504b46dcefd895ea923a63f04bc2f4ac12d9e8ea57ea80e2a`
- Source type: selectable-text PDF (`pdf-text`), 19 pages.

## Extraction and visual inspection

- Text was extracted from the selectable layer with layout preservation and checked against all 19 high-DPI page renders (180 dpi).
- The complete PDF was visually inspected, including Tables 8–12 after the references.
- Multi-column references were re-extracted in reading order. References remain searchable in original English and are not translated line by line.
- Equations (1)–(11) were normalized to Markdown `$...$` / `$$...$$` math.

## Assets

- Reader assets include every numbered source visual: Figures 1–5 and Tables 1–12 (17 crops).
- `assets/_pages/` contains 19 high-DPI page renders used for manual inspection; these are provenance/QA assets and are not linked as figures.
- Dense central tables are also transcribed into searchable Markdown. Table 12 is fully transcribed per task.
- Five selected visuals were materialized under `images/` for the DeepPaperNote.

## Layout and source caveats

- The PDF places Figure 3, Figure 4, Table 1, and Table 2 tightly on page 6; these were cropped separately.
- Table 12 is dense; the image crop is retained and all 50 task rows plus averages are transcribed.
- Main text states the real-world overall result over 100 trials under multiple initial configurations, while supplementary §7.1 says each model is evaluated over 50 trials per task. Both statements are preserved; the exact aggregation should be confirmed from code or authors for strict replication.
- Main text reports FLUX.2 9B average as 85.21%, while Table 7 rounds to 85.2%; both are noted without harmonizing away the difference.

## Translation policy

- Claims, hedges, citations, model/dataset names, metrics, hardware, timing and protocol details were preserved.
- Stable names such as ImageWAM, FastWAM, LIBERO, RoboTwin, OmniGen2, Ovis-U1, FLUX.2 and Action DiT remain in English.
- No unavailable algorithm section or Light-WAM mechanism was invented.

## Skipped material

- No substantive main-paper or supplementary section was intentionally skipped.
- Bibliography entries are preserved in original English rather than paired one by one, per reader convention and the user's searchability requirement.

## Quantitative source coverage audit

- Main/supplement substantive source paragraph or list groups: 59.
- Reader bilingual pairs: 59.
- Section-by-section mapping is embedded in `detailed_paper.md` and `source_map.json`; every section count matches.
- English source paragraphs are cleaned full text, not summaries; separate source paragraphs and the three-item contribution list are not merged away.
- References [1]–[98] remain English-only. Equations: 11; figures: 5; tables: 12; Table 12 rows: 50 tasks plus average.
