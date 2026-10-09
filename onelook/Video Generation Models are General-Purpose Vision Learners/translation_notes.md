# Translation notes

## Scope

Full 19-page source PDF (arXiv:2607.09024v1) was inspected and translated into `detailed_paper.md` as adjacent English/Chinese paragraph pairs. The separate `paper_DeepPaperNote.md` is an analytical WJ note and is not used as source evidence for the detailed reader.

## Source and extraction

- Source type: selectable-text, two-column PDF; `pdfinfo` reports 19 pages.
- Extraction: `pdftotext -layout`; page rendering with `pdftoppm` for page-order and figure/table inspection.
- Sections covered: Abstract, Introduction, Related Work (2.1–2.3), GenCeption (3.1–3.5), Experiments (4.1–4.6), Conclusion, and References [1]–[87].
- No appendix, supplementary section, or exact prompt/code block was present in the supplied 19-page PDF.

## Assets and caveats

PDF figures are composite multi-panel figures and tables. Page-level PNGs are retained in `assets/` to avoid misleading panel crops. Figure and table captions are bilingual and Table 1/2 values are transcribed in searchable Markdown. `images/` contains selected copies for the DeepPaperNote. Page-level assets preserve original labels and panels but are not individually cropped.

## Fidelity notes

Mathematical literals retained include $v=\epsilon-x_0$, $-v=x_0-\epsilon$, $d'=\operatorname{clip}(\alpha\log(d+1),0,1)$, $t\in\{11.25,22.5,30\}$, $480\times832$, 81 frames, 24 FPS, 7,500 videos, 7×–500× data efficiency, and all reported inference values. Model, dataset, benchmark, metric, and software names remain in English.

The references section is retained in searchable bibliographic form rather than line-by-line Chinese translation, as required by the reader contract. Page-level source assets and `source_map.json` provide traceability.
