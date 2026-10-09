# Translation Notes

## Scope and authority

- Canonical source: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/M7EWTUEW/Yang 等 - 2026 - MemoryWAM Efficient World Action Modeling with Persistent Memory.pdf`
- Selectable-text PDF, 15 pages, SHA256 `a2beffa47141bcc8d5593d0eb50be681ee286a75f543848cef86e7f56d310c8a`.
- `detailed_paper.md` is authoritative; `paper.md` is byte-identical. References [1]–[68] remain English-only by policy.

## Extraction and reading order

All 15 pages were rendered at 220 dpi and visually inspected. Main prose is predominantly one column. Page 5 contains a two-column float around Figure 3; page 8 interleaves Table 1, Figure 5, and Table 2 with prose; page 14 interleaves Figure 6 and appendix prose, with the final sentence continuing on page 15. The reader restores semantic order rather than PDF geometric order. No OCR was used for selectable prose.

## Assets and crop caveats

- Six numbered figures and three numbered tables were cropped from high-DPI page renders into `assets/`.
- Some crops intentionally retain a narrow amount of caption/neighbor context because several source floats are tightly interleaved with body text; complete captions are separately transcribed and translated in the reader.
- Tables 1–3 are fully transcribed as searchable Markdown: 10, 2, and 3 data rows respectively (15 rows total, including average rows where present). There is no dense appendix table.
- `images/` contains only Figures 2–4 selected for the deep note.

## Terminology and math

`gist token` is retained in English to distinguish the learned compression tokens from a free-form summary. `event-boundary memory` is translated literally, while the notes flag that the implementation operationalizes it as the first two episode frames. Equations (1)–(7) use standalone `$$...$$`; Python-generated files were scanned for escape/control-character damage.

## Omissions / uncertainty

No substantive main-text or appendix prose is intentionally omitted. The inventory has 40 substantive paragraph/list groups and 40 bilingual pairs. Six paired `(cont.)` blocks appear where display equations interrupt a source paragraph; these continue the preceding paragraph and are not counted as additional source groups. No algorithms, code/prompt blocks, acknowledgments, availability statements, or supplementary dense tables appear in the PDF.
