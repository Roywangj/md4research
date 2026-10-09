# Translation Notes

## Scope

- Source: local Zotero attachment `EAWWASN8`, item `BY96Y7AI`.
- Source type: 12-page selectable-text arXiv PDF (`pdf-text`).
- Coverage: abstract, introduction, related work, complete method and training procedure, inference, experiments, conclusion, and Appendix A.
- References: all 31 entries remain in the source PDF; the reader records their scope but does not translate bibliographic entries line by line.

## Extraction and layout

- The PDF uses a two-column layout. Direct extraction occasionally interleaved captions, tables, and the neighboring column, so the visible reader follows recovered section order rather than raw line order.
- Automatic extraction of Figure 4 contained only the caption and neighboring prose. It was re-rendered and tightly cropped from page 8; the repaired crop contains both accuracy curves and axis labels.
- Algorithm 1 and Tables 4-5 had no independent high-confidence automatic crops. They were re-rendered from pages 5 and 12 and visually checked before insertion.
- Other figure and table crops were inspected at original resolution and were readable without contamination from unrelated visuals.

## Terminology

- `latent text` is translated as “潜在文本” and means the previous reasoning step's final hidden state.
- `latent vision` is translated as “潜在视觉” and means the selected image embeddings, not a generated image.
- `autoregressive steps` is translated as “自回归步”. It measures decoded output steps and should not be read as total forward-pass compute.
- Model, dataset, and method names remain in English.

## Source caveats

- Table 1 reports Qwen2-VL IVT-LR at 94.6 on ScienceQA, while Table 2 reports the full model at 94.1. The PDF does not explain this 0.5-point discrepancy.
- The abstract reports an average 5.45% accuracy gain. The four Table 1 gains over the strongest listed baseline average 4.75 points, so the aggregation rule is not directly reproducible from the table.
- The appendix describes $N=4$ as corresponding to three core reasoning steps. The reader preserves this notation and explains the effective three-step setup.

## Completion state

- `paper.md` is a full-structure bilingual reader rather than a sentence-by-sentence translation of reference entries.
- All visible image links use paper-local relative paths under `assets/`.
- Stable section and asset provenance is recorded in `source_map.json`.
