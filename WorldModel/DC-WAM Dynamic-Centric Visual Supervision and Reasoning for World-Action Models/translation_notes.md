# Translation Notes

## Scope

- Complete bilingual reader for all 9 supplied PDF pages.
- Main text: pages 1–7; References: pages 8–9.
- Covered: Abstract, Introduction, Related Work, Method, Eqs. (1)–(26), Experiments, Analysis, Conclusion, 30 References entries.
- Native inventory: Figure 1–5 and Table 1–4 only. The supplied PDF contains no appendix or supplementary pages; none were invented.

## Source and extraction

- Source type: selectable-text PDF (`pdf-text`).
- Multi-column reading order was reconstructed against rendered pages.
- Text used the native selectable layer; no OCR substitution was used.
- References remain in original searchable bibliographic English by design.

## Assets

- `assets/` contains five native figure crops and four native table crops.
- Tables 1–4 are additionally transcribed into searchable Markdown with exact rows, arrows, parentheses, and values.
- Every asset has a matching bilingual `Caption` / `Caption[CN]` pair and a valid relative link.

## Terminology and technical checks

- Canonical terms: temporal-difference supervision, tracker-guided flow matching (TrackFM), tracker-derived dynamic map, DynaRoute, action-only inference, routed visual cache.
- Figure 1 is preserved as a key result: future-frame PSNR is not monotonically aligned with policy success.
- Eqs. (1)–(26) were checked for continuous numbering; display equations remain outside blockquotes.
- The source sentence says additional details appear in an Appendix, but the supplied 9-page artifact has no Appendix. The reader preserves that statement and explicitly records the source limitation rather than fabricating content.

## Skipped or uncertain content

- Skipped substantive source content: none.
- Untranslated source body: none.
- Low-confidence OCR blocks: none.
- Appendix content: unavailable in the supplied PDF, therefore not generated.
