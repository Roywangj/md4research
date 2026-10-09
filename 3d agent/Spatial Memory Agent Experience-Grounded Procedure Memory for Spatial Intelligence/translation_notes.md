# Translation Notes

## Source and coverage

- Source: supplied selectable-text PDF, arXiv:2608.12743v1, 80 pages.
- Coverage: pp. 1–80, including abstract, all main sections, equations, numbered findings, Tables 1–32, Figures 1–30, references, Appendices A–F, limitations, qualitative panels, and all seven benchmark prompt triplets.
- English source blocks are followed by Chinese translations. References are intentionally retained in original searchable bibliographic form, following the skill’s reference policy.

## Extraction and normalization

- The selectable-text extraction was checked against rendered PDF pages at the first page, every section transition, all table/example ranges, the qualitative appendix boundary, prompt pages, and the final page.
- Multi-column reading order was normalized manually.
- Prompt whitespace, line wrapping, and repeated explanatory wording were normalized for Markdown readability. Exact runtime literals and contracts were preserved, including `{rank}`, `{similarity:.3f}`, `{task}`, `{transferable_lesson}`, `{summary}`, `summary`, `transferable_lesson`, `prior_model_output`, `<answer>...</answer>`, `Final Answer: <LETTER>`, `Final Answer: <ANSWER>`, strict JSON schemas, anti-leakage enumerations, allowed output forms, and all stated numerical constraints.

## Figures and assets

- No local raster crops were created because the permitted tool interface did not expose a safe PDF-to-asset write operation, and shell-based rendering was blocked by the environment permission policy.
- Consequently, `detailed_paper.md` and `paper.md` intentionally contain no local image links and therefore no broken image links. Figures are preserved through source-numbered bilingual captions and searchable transcriptions of their evidence-bearing questions, memory IDs, TRS values, model predictions, analyses, and issues.
- Tables 1–32 are represented in searchable Markdown; Tables 9–26 are consolidated into one searchable inventory while retaining every source table number, page anchor, sub-category, capability annotation, question/options, and ground truth.

## Validation record

- Required validator command was attempted twice (via `python3` and direct script execution) but blocked by the environment’s approval policy; it did not execute. This is an execution caveat, not a hidden pass.
- Equivalent permitted checks completed: 184 total paragraph labels = 92 English + 92 Chinese labels; 42 original captions = 42 Chinese captions; 0 Markdown image links and therefore 0 missing links; 1,426 lines; 154,922 bytes.
- `cmp` completed successfully with no differences, confirming `paper.md` is byte-identical to `detailed_paper.md`.
- Structural review found labels in alternating original/Chinese order, captions immediately paired, display equations outside blockquotes, and no legacy `**Original:**` / `**中文:**` body labels.
- Scoped file-operation audit confirms this task wrote only `detailed_paper.md`, `paper.md`, `source_map.json`, and `translation_notes.md`. Existing `paper_DeepPaperNote*` files and `images/` assets were read neither as translation sources nor modified.

## Material caveats

- Figure pixels themselves are not embedded locally; consult the source PDF for axes, image content, and panel typography. This is the only material asset caveat.
- The PDF was readable on all 80 pages; no pages, formulas, or prompt literals were marked unreadable.
