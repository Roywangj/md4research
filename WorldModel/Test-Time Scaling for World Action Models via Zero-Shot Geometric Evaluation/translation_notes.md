# Translation Notes

## Scope

- Complete bilingual reader built from the single canonical local PDF supplied by the user.
- Source type: selectable-text, two-column arXiv PDF (`pdf-text`), 8 pages.
- `detailed_paper.md` is the authoritative build. `paper.md` is an exact byte-identical copy, not a separately edited derivative.
- All body sections are retained in source order: Abstract; 1 Introduction; 2 Related Work; 3 Method and §§3.1–3.3; 4 Experiments and §§4.1–4.5; 5 Conclusion; References.
- All five numbered equations, three figures, five tables, and 29 references are included.

## Source and provenance

- Canonical PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/QWZWYPV8/Zhao 等 - 2026 - Test-Time Scaling for World Action Models via Zero-Shot Geometric Evaluation.pdf`
- SHA256: `1fa68da603965ee37506d0bb38f187bb55062132c442b42eaa8fcd226ac7959e`
- arXiv: `2607.17454v1` (20 July 2026)
- DOI: `10.48550/arXiv.2607.17454`
- Zotero parent: `2UT6H548`; attachment: `QWZWYPV8`; collection: `worldmodel`.

## Title discrepancy

The canonical Zotero record, filename, embedded PDF metadata, DOI title, and requested folder use **“Test-Time Scaling for World Action Models via Zero-Shot Geometric Evaluation.”** The title visibly typeset at the top of PDF page 1 instead reads **“…via Zero-Shot Geometric Verification.”** The reader uses “Evaluation” for its canonical title/folder metadata while quoting “Verification” as the rendered title in provenance. No assumption is made about which wording the authors ultimately intend.

## Extraction and layout

- All eight pages were rendered at 300 DPI and visually inventoried before drafting.
- The selectable text layer was extracted with layout preservation, then reordered according to the visually inspected two-column reading order.
- Line-end hyphenation was rejoined, typography was normalized for readable Markdown, and formulas were reconstructed as standalone display math.
- Page 5 is unusually dense: Tables 2–4, Figure 2, and surrounding prose share the page. Their order was verified visually against the rendered page rather than inferred from raw extraction order.
- The PDF contains no algorithm block.

## Figures, tables, and crop caveats

- All three figures and all five tables were cropped from 300-DPI page renders into `assets/` and visually inspected.
- Crops intentionally preserve the source caption edge in some images for visual verification; the complete captions are also provided separately in bilingual searchable text.
- Every substantive table is transcribed in Markdown. Table 1 preserves all 13 displayed result rows, grouping, bold best fixed-budget values, and paired $N=8$ confidence intervals. Tables 2–5 preserve all displayed settings and values.
- Figure 2’s rates are searchable as $N=2/4/8/16 \rightarrow 7/10/12/32\%$.
- The X-WAM native-depth exception is retained explicitly: X-WAM uses its own predicted depth rather than the external geometry foundation model for reprojection scoring.

## Translation policy

- English source paragraphs are cleaned for display without summarizing them; each is followed immediately by its Chinese translation.
- Claims, hedging, comparisons, citations, thresholds, units, model variants, success rates, confidence intervals, hardware, random-seed counts, and rollout protocols are preserved.
- Method, model, benchmark, and metric identifiers remain in English where translation would reduce precision.
- Fixed parameters are retained exactly: $\delta_{\mathrm{idle}}=1\,\mathrm{cm}$, $\tau_{\mathrm{gate}}=-0.2$, $\rho_{\mathrm{cap}}=30$ pixels, and $\gamma_{\mathrm{conf}}=0.5$.

## References policy

All 29 references are retained in searchable original bibliographic form rather than translated line by line. This preserves author names, paper titles, venues, and arXiv identifiers for citation matching.

## Material absent from the source

The supplied eight-page source has no appendix or supplementary material and no dedicated Limitations, Acknowledgments, Data Availability, Code Availability, Broader Impact, or Ethics section. These sections were not fabricated. The paper’s own failure analysis (§4.5) is retained in full, but it is not relabeled as a dedicated Limitations section.

## Temporary artifacts

No temporary extraction paths are linked from either reader. Only the eight final figure/table assets under `assets/` are referenced. Page renders and extraction helpers are build artifacts and are not part of reader provenance.
