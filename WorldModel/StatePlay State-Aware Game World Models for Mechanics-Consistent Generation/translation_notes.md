# Translation Notes

## Scope

Full-paper bilingual reader for all 12 pages of the supplied StatePlay PDF, including abstract, main sections, equations (1)–(6), figures, tables, references, appendices A–F, NPC prompt, mechanics-fidelity prompt, and exact JSON response schema.

## Source

- PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/2GC8LZER/Lin 等 - 2026 - StatePlay State-Aware Game World Models for Mechanics-Consistent Generation.pdf`
- Format: selectable-text arXiv PDF, `arXiv:2607.26754v1`, 12 pages, 29 Jul 2026.
- Extraction: `pdftotext -layout` plus PyMuPDF page rendering. The two-column source was checked against rendered pages at section transitions and figure/table/prompt pages.

## Layout and extraction issues

The paper is a dense two-column, untagged PDF. Text extraction interleaves columns and places captions/diagram labels among prose; the reader was rebuilt in source order using the rendered page layout. Equations were normalized into Markdown-compatible LaTeX while retaining variables, dimensions, operators, and numeric values. References are preserved as searchable original bibliographic entries rather than translated line by line.

## Assets and crop caveats

The `assets/` and `images/` files are rendered-page extracts for the pages containing Figures 1–7 and Tables 1–5. This preserves all vector text, panels, legends, and prompt material without broken links, but several files include surrounding page whitespace and neighboring text because the source figures are tightly interleaved with two-column content. Important Tables 1–5 are also transcribed as Markdown. DeepPaperNote uses the same valid local page extracts under `images/`.

## Untranslated or skipped material

No substantive source section was intentionally skipped. Bibliography entries remain in their source language/form for traceability. Diagram labels and exact prompt literals (for example `result_win`, `macro_success`, `YOU WIN`, and JSON keys) remain unchanged where literal identity is part of the method.

## Material-level caveat

Because the supplied PDF is an arXiv preprint and the text layer is not semantically tagged, paragraph boundaries in the bilingual reader are reconstructed from visual layout rather than extracted XML/LaTeX. The full textual content, captions, appendices, tables, prompts, and references are covered, but a strict character-for-character comparison against the source's hidden TeX line breaks is not possible. Page-level rendered assets are legible but are not tightly isolated crops for every panel.

## If a stricter verbatim edition is required

Use the paper's source TeX or project-page supplementary files, if available, to replace reconstructed paragraph boundaries and produce tightly clipped per-panel assets; retain this reader as the auditable PDF-grounded edition.
