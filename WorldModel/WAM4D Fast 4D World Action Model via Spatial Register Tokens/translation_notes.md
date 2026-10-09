# Translation and Extraction Notes

## Scope

- Canonical source: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/UMKJ276I/Li 等 - 2026 - WAM4D Fast 4D World Action Model via Spatial Register Tokens.pdf`
- Source type: selectable-text PDF (`pdf-text`), 19 pages.
- Verified SHA256: `35ab949057809b5e150f6b2c6dff3d2f559bfc61b29dfa371c07fa1894d02b6f`.
- Main text is pp. 1–15; references are pp. 16–19. There is no appendix or supplementary section in the canonical PDF.
- All substantive main prose, the homepage date/code/keywords block, the contribution list, Algorithm 1, equations, captions, table notes, limitations, and the printed code-availability line are retained in source order. References remain searchable English-only.

## Extraction and reading order

- Text was extracted from the selectable layer with layout preservation and checked against the canonical page images, with high-resolution inspection of dense tables including Table 6.
- The source uses a two-column layout. Paragraph reading order was repaired across page breaks, especially the Introduction spanning pp. 1–2 and the discussion around Tables 3–8.
- Display equations were reconstructed as Markdown-compatible LaTeX. Equations interrupt nearby prose but no source paragraph required a separate `(cont.)` bilingual fragment in the final reader.
- Algorithm 1 is preserved as an exact 11-step ordered procedure following its bilingual introductory pair.

## Figures and tables

- Extracted all seven numbered figures and all nine numbered tables into `assets/`.
- Each numbered object has complete English and faithful Chinese captions in the reader.
- Figures 6 and 7 occupy most of their source pages; their crops intentionally retain the complete multi-row qualitative sequence while excluding page headers/footers where practical.
- Tables 1 and 2 share a source page and were cropped separately. Figure 4 appears below them on the same page.
- Table 3 is transcribed as 51 searchable rows (50 task rows plus the average row); averages were checked against the source.
- Table 6 is transcribed as 36 searchable data rows. Because it is extremely wide and combines summary metrics with two per-task blocks, the complete crop remains the visual authority. The searchable transcription has explicit headers for all nine variants and preserves sparse depth-metric cells with em dashes, so every value remains aligned to its actual variant. Source bold best and underlined second-best indicators are preserved with Markdown/HTML where practical, including ties.
- Other central tables are transcribed into ordinary Markdown with explicit columns.

## Terminology and semantic boundaries

- “4D” is rendered as time-indexed RGB-D/depth and point-cloud evolution. The deployed policy does not retain a dense explicit 4D scene.
- “Spatial registers” remains “空间寄存器 token” to distinguish these learnable queries from hardware registers.
- “Clean/randomized” is used for the aggregate RoboTwin protocol; Table 3’s “Easy/Hard” maps to the same two settings.
- Depth targets are offline DA3 pseudo-depth for the stated datasets; the paper does not claim sensor-depth ground truth for real-world demonstrations.

## Known caveats

- PDF text extraction yielded 70 searchable reference entries after line joining. The paper itself does not number references, so the reader’s list numbering is a convenience and not a source citation index.
- No LIBERO experiment appears in this paper. Any statement about merged or separately trained LIBERO suites would be unsupported.
- The printed GitHub URL establishes stated code availability, but this package did not use network access to verify repository contents or release completeness.
- Cross-paper comparisons in the deep note are explicitly labeled synthesis and restricted to claims supported by WAM4D’s own text/reference positioning; no outside mechanism is imported.

## Completeness statement

The reader is intended as a semantically complete bilingual reconstruction of all substantive non-bibliographic prose in the canonical 19-page PDF. `paper.md` and `detailed_paper.md` are required and maintained byte-identically. The final source coverage audit in the reader records 63 base bilingual pairs, zero continuation fragments, seven figures, nine tables, and ten display equations.
