# Translation and Extraction Notes

## Scope

- Complete 61-page technical report processed from the user-provided selectable-text PDF.
- Coverage includes title metadata, abstract, Sections 1–5, limitations, complete bibliography, Appendices A–G, exact system prompts/listings, exact retained qualitative prompts, all 24 figure captions, and Tables 1–18.
- `detailed_paper.md` and `paper.md` use adjacent `Para. X` / `Para. X[CN]` pairs. References remain in original searchable bibliographic form, per the reader contract.

## Source

- Path: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/MUQ6N8C7/Chen 等 - SCALING PROPERTIES OF TEXT CONDITIONING IN VISUAL GENERATION.pdf`
- Type: selectable-text PDF (`pdf-text`)
- Page count: 61
- Layout: two-column technical report with full-width figures/tables and appendix listings.

## Extraction and layout handling

- Text was extracted in both layout-preserving and raw modes.
- All 61 pages were rendered to PNG for visual cross-checking of page order, section transitions, multi-column ordering, tables, figures, and appendix boundaries.
- The PDF text layer around page 13 duplicates/interleaves part of §3.2 with Figure 10; the reader follows the visually verified natural order and removes duplicated extraction artifacts.
- Ligatures, line-end hyphenation, mathematical symbols, model names, metrics, and exact literals were normalized conservatively.

## Assets

- `assets/` contains one real PDF-derived PNG for each Figure 1–24.
- Crops are page-region crops rather than reconstructed vector figures. For large gallery figures (20–24), most of the content page is retained; for conventional charts/diagrams, the upper visual region is retained.
- Captions are represented separately in bilingual searchable Markdown.
- `images/` contains selected copies used by `paper_DeepPaperNote.md`.
- Tables 1–18 are transcribed into searchable Markdown; the original PDF values remain the authority.

## Translation policy

- Model, dataset, benchmark, metric, API, JSON key, code identifier, XML-style tag, and sentinel literals remain exact.
- Recurring terms follow the Terminology Ledger in the reader.
- Exact system prompts and retained user prompts preserve the English source and literal output schemas; the immediately paired Chinese block translates their instructions while leaving keys and exact output tokens unchanged.
- Bibliography is retained in English rather than mechanically translated.

## Known caveats

- Full-page qualitative galleries contain very dense image tiles; they are readable when opened at original asset resolution but may appear small in inline Obsidian preview.
- Some source prompts were explicitly marked by the authors as “original user prompt not retained”; these remain unavailable and were not reconstructed.
- The paper is dated 2026 and cites model/evaluator names that may be unavailable publicly; this is source content, not independently verified availability.
