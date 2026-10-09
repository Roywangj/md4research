# Translation Notes

- Paper: `Interleaved-Modal Chain-of-Thought`
- Source format: `pdf-text`
- Source PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/DMT6SNMT/Gao 等 - 2025 - Interleaved-Modal Chain-of-Thought.pdf`
- Zotero item key: `LKAFNEE6`
- arXiv: `2411.19488`
- DOI: `10.48550/arXiv.2411.19488`

## Scope

This folder follows the WJ reading contract:

- `paper.md`: bilingual reader with figure/table placement.
- `source_map.json`: stable source anchors, page ranges, and asset paths.
- `assets/`: images used by `paper.md`.
- `paper_DeepPaperNote.md`: Chinese deep-reading note.
- `images/`: images used by `paper_DeepPaperNote.md`.

The translation covers the main argument, method, experiments, case study, conclusion, and useful supplementary material. Reference entries are indexed but not translated line by line.

## Extraction Notes

- The PDF is searchable, but the automatic metadata extractor mistook an affiliation line for the title. The note manually uses the correct title from the PDF title page and Zotero metadata.
- Algorithm 1 and Figure 5 were cropped poorly by the automatic figure extractor. Their logic is transcribed in text rather than inserted as primary visuals.
- Table 1 is readable but dense; key values are repeated in prose and in the deep-reading note.
- Figure 4 includes an adjacent supplementary example in the crop; the selected-patch trend remains readable.

## Terminology Decisions

| Term | Translation |
|---|---|
| Chain-of-Thought | 思维链 |
| Interleaved-modal Chain-of-Thought | 交错模态思维链 |
| Attention-driven Selection | 注意力驱动选择 |
| text-only rationales | 纯文本理由 |
| visual rationales | 视觉理由 |
| textual rationales | 文本理由 |
| Fine-grained Visual Information | 细粒度视觉信息 |
| signal token | 信号 token |
| KV Cache | KV 缓存 |

## QA Checklist

- `paper.md` uses `Para. X:` / `Para. X[CN]:` style.
- Relative image paths in `paper.md` resolve under `assets/`.
- Relative image paths in `paper_DeepPaperNote.md` resolve under `images/`.
- Math uses Markdown `$...$` / `$$...$$` style.
- No `**Original:**` / `**中文:**` labels are used.
