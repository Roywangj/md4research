# Translation notes

- Source: user-supplied 39-page PDF `Harness VLA...pdf`; metadata identifies arXiv:2607.08448v3 (15 July 2026).
- Extraction: `pdftotext -layout`; all non-empty extracted page blocks were retained in `detailed_paper.md` and copied byte-for-byte to `paper.md`.
- Assets: `assets/page-01.jpg`–`assets/page-39.jpg` are low-resolution rendered page captures. They are page-level evidence, not silently cropped figures.
- Translation status: complete bilingual draft. All 39 extracted page blocks now have paired Chinese translations in `detailed_paper.md`; `paper.md` is a byte-identical copy.
- Material-level caveat: the source PDF was extracted with `pdftotext -layout`, so complex page layout, table alignment, formula typography, and figure placement are represented textually in the bilingual Markdown. The rendered page captures preserve the visual source evidence; terminology and formula/table formatting should still receive a human publication pass.
- No missing material was reconstructed from `paper_DeepPaperNote.md`; that file and its JSON files were not modified.
- Validation completed: 39 bilingual paragraph pairs, zero unfinished translation placeholders, zero broken local links, valid `source_map.json`, and byte-identical `detailed_paper.md` / `paper.md`.
