# Translation Notes

## Scope

- Complete 30-page bilingual reader in source order: title, authors and affiliations, abstract, Sections 1–5, Equations (1)–(9), all numbered tables and figures, complete References [1]–[48], Appendices A–E, full harness prompts/tool schema, both worked cases including all AST/route outputs, computational costs, and all 16 NeurIPS checklist questions with answers, justifications, and guidelines.
- **Skipped content: none.** Running page numbers and purely decorative whitespace are not reader content; all substantive prose, captions, tables, prompts, examples, references, and checklist material are included. No acknowledgments section is present in the source.

## Source and extraction

- Source: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/QXAH89IU/Ruan 等 - 2026 - AlloSpatial Agentic Harness Framework for Spatial Reasoning in Foundation Models.pdf`
- Source type: selectable-text PDF, 30 pages, two-column main-paper layout with mixed full-width figures/tables and single-column appendix/checklist pages.
- English was extracted directly from the text layer with Poppler `pdftotext -layout`; line-break hyphenation, ligatures, reading order, superscripts, symbols, and equation notation were cleaned against rendered pages. OCR was not used.
- Machine-readable JSON/YAML/tool-call keys and values are retained verbatim in both language blocks so examples remain executable/searchable; the Chinese blocks translate and explain their semantics without altering numeric content.

## Figures, tables, and crops

- Eight actual visual regions were rendered from the PDF at 130 dpi and tightly cropped into `assets/`: numbered Figures 1–4 plus the two input-contact sheets and two landmark-map visualizations in Appendix D. No asset is a full-page screenshot; all exclude page headers, footers, and unrelated prose. Crop boxes in PDF-point coordinates are recorded in `source_map.json`; the stored PNG crop pixel boxes were derived from the 130-dpi page renders.
- Every asset is linked exactly once near its first substantive discussion and has an English/Chinese caption.
- Tables 1–5 and the World2Mind parameter schema are transcribed as searchable Markdown in both English and Chinese.
- Source inconsistency preserved rather than silently corrected: NeurIPS checklist item 8 states “8 NVIDIA H200 GPUs,” whereas Appendix E states “8 HUAWEI Ascend 910B NPUs.”

## Translation policy

- `allocentric` is consistently rendered as “非自我中心”; `egocentric` as “自我中心.” Method, model, benchmark, tool, tag, field, and metric names remain in English where they are identifiers.
- Display equations use standalone `$$...$$`; inline mathematics uses `$...$`. No reader-facing `\(...\)` or `\[...\]` delimiters are used.
- References retain names, venue/year/URL metadata and provide Chinese translations of titles; bibliographic identifiers are never altered.

## QA

- JSON parse: passed.
- Markdown image-link existence: passed.
- Every asset used exactly once: passed.
- English/Chinese `Para. X` label pairing with per-major-section reset: passed.
- Forbidden body labels `**Original:**` / `**中文:**`: absent.
- Forbidden visible source anchors/comments: absent.
- Forbidden reader-facing `\(...\)` / `\[...\]` math delimiters: absent.
- Standalone display-math placement: passed.
- Page coverage: pages 1–30 all represented in `source_map.json`.
