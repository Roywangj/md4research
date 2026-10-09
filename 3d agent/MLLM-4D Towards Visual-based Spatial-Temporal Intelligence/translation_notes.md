# Translation notes

## Method

- Source: local read-only PDF `Yin 等 - 2026 - MLLM-4D Towards Visual-based Spatial-Temporal Intelligence.pdf`, identified as *MLLM-4D: Towards Visual-based Spatial-Temporal Intelligence*, arXiv:2603.00515v1, 21 physical pages (printed pages 1–21).
- Text recovery: the local Zotero full-text cache was used for searchable prose and references; PDF page rendering/visual inspection was used to check page order, two-column boundaries, tables, figures, prompts, and qualitative panels.
- Translation: English source text is followed immediately by a Chinese translation, with section order, equations, lists, tables, prompts, literals, citations, and numerical values retained. Bibliographic references remain in original searchable form.

## Coverage

- Covered PDF pages 1–21 / printed pages 1–21.
- Covered Abstract; Sections 1–7; References; Appendix Sections 8.1–8.5; Figures 1–17; Tables 1–3; Equations (1)–(9); Algorithm 1; exact SFT, Cold Start, GRPO, entity-extraction, and ST-CoT prompt blocks; and the qualitative comparison records.
- The output includes the source’s model names, dataset names, metric names, citations, percentages, training settings, GPU/runtime figures, answer options, JSON schema, XML-like tags, placeholders, and sentinel `null`.

## Ambiguities and normalization

- The PDF’s text layer splits equation layouts, summation limits, and superscripts/subscripts. Equations were re-typeset in Markdown math delimiters based on the rendered equation and surrounding definitions; no new scientific claim was added.
- The entity-extraction prompt visibly skips output requirement number 2 and contains the example literal `gril`; both are retained exactly and explicitly noted in `detailed_paper.md`.
- Figure 16 contains an apparent inconsistency between the answer-letter marker/prose and the option text. It is preserved and called out rather than silently corrected.
- Some source bibliography spellings and OCR-like forms (for example `Bootstap`, capitalization, and model-name punctuation) are retained close to the searchable source text rather than normalized to external records.

## Figures and assets

- The source contains dense raster figures. The PDF reader in this environment exposed rendered pages for inspection but did not provide an allowed raster-crop export path. No fabricated or misleading image crop was created.
- Each figure has a bilingual caption and a PDF-page anchor. Tables 1–3 are transcribed as searchable Markdown tables and also have readable local SVG renderings (`assets/table_1.svg`, `assets/table_2.svg`, and `assets/table_3.svg`) linked near their corresponding table cards. Figure 6, Figure 10, and Figure 11 prompt/code content is transcribed in fenced blocks; Figures 12–17 preserve questions, choices, model-answer content, and source caveats, including the full Figure 17 panel on physical page 21.

## Validation

- `source_map.json` is valid JSON and records the 21-page coverage, page/section/figure/table anchors.
- `paper.md` was copied from the final `detailed_paper.md`; the required validator passed with byte identity enforced: 68 bilingual paragraph pairs, 20 caption pairs, and 3 local image links with 0 missing. Local link and asset checks confirm that `assets/table_1.svg`, `assets/table_2.svg`, and `assets/table_3.svg` exist. No local image links are intentionally left broken.
- A preliminary snapshot comparison detected a concurrent change in the pre-existing protected `paper_DeepPaperNote.md`; it was not edited or restored. A fresh final snapshot/verification after the repair reported no changes and no unexpected paths, with only the four explicitly permitted file paths allowed.
