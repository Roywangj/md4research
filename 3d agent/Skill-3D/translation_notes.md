# Translation Notes

## Extraction

- Source format detected as `pdf-text`: the PDF has a selectable text layer and 21 pages.
- Text was reorganized into natural reading order because the source PDF uses a two-column academic layout.
- Display equations were normalized to Markdown `$$...$$` blocks outside paragraph blockquotes.
- Figure and table crops were rendered from the source PDF at 2.5x scale into `assets/`.

## Coverage

- Main paper sections translated: Abstract, Introduction, Related Work, Method, Experiments, Conclusion, Limitations.
- Appendix sections translated: LLM usage claim, more experimental results, experimental details, qualitative results, and prompt-design overview.
- Figures and tables included as assets: Fig. 1-5, Table 1-3, Table B.1-B.2, Table C.3-C.4, Fig. E.1-E.6.
- References on pp.9-13 are preserved in the source PDF and not translated line-by-line because they are bibliographic metadata rather than substantive body prose.

## Uncertainty

- Appendix prompt figures E.3-E.6 are image-like prompt panels. Their visual content is included as crops; the surrounding body prose is translated, but the full prompt text inside images is not retyped line-by-line.
- Figure E.4 is a page-continuation prompt panel, so its crop is marked approximate in `source_map.json`.
- Table crops are tight around table bodies and may omit surrounding caption text; captions are provided separately in `paper.md`.

## Terminology Decisions

- Method names, dataset names, model names, and tool names are kept in English.
- `Scene Memory`, `Skill Library`, `static skill`, `dynamic skill`, `rollout`, `GRPO`, and `ETU` are preserved as canonical terms with Chinese explanations in the terminology table.
