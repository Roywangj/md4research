# Translation Notes

## Extraction

- Source format detected as `pdf-text`: the Zotero local PDF has a selectable text layer.
- The reader was generated with the WJ `nature-reader` workflow and uses the existing Zotero/DeepPaperNote extraction artifacts for text and figure/table assets.
- Figure/table crops are stored under `assets/`; the earlier deep-reading assets remain under `images/`.
- The manifest referenced a shared terminology-ledger file that was not present on disk, so the terminology ledger was maintained directly inside `paper.md` and `source_map.json`.

## Coverage

- Main body translated as a bilingual reader: Abstract, Introduction, SimWorld Studio / SimCoder, Co-Evolution, three experiment case studies, Related Work, Conclusion.
- Substantive appendix material translated/covered: limitations and broader impact, interface panels, running configuration, assets/licenses/model-access notes, evaluation-detail summaries, and prompt examples.
- References on pp.12-21 are bibliographic metadata and were preserved in the source PDF rather than translated line-by-line.
- Dense appendix numeric breakdowns are represented through narrative translation and source-map notes instead of retyping every table cell; the key main-table values are included in `paper.md`.

## Figures and Tables

Included assets:

- Fig. 1 overview and co-evolution result.
- Fig. 2 SimCoder self-evolving loop.
- Fig. 3 workspace UI.
- Fig. 4 three case studies.
- Fig. 5 SimCoder ablation.
- Fig. 6 medieval-village qualitative example.
- Table 2 embodied navigation results.
- Table 3 platform comparison.
- Fig. 10 representative interface views.

Not fully re-cropped in this pass:

- Fig. 7, Fig. 8, Fig. 9 and several appendix tables/figures were not selected in the existing high-confidence asset set. Their substantive claims are translated in nearby prose, but their visual crops are not inserted to avoid low-confidence or broken assets.
- Table 1 is rendered as a compact Markdown table of average scores rather than a crop, because the prior extraction did not materialize a clean high-confidence Table 1 image.

## Terminology Decisions

- Method names, model names, dataset names, metrics, and platform names are kept in English.
- `self-evolution` is translated as `自我演化`; `co-evolution` as `共同演化`; `adaptive curriculum` as `自适应课程`; `Gymnasium-style environment` as `Gymnasium 风格环境`.
- `SimCoder` is kept as the agent name rather than translated literally.
