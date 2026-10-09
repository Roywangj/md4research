# Translation Notes

- Paper: `REALM: An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting`
- Source format: `pdf-text`
- Source PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/D99TFPBN/Shi 等 - 2025 - REALM An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Spla.pdf`
- Zotero item key: `BAE6PIDP`
- arXiv: `2510.16410`
- DOI: `10.48550/arXiv.2510.16410`

## Scope

This folder follows the WJ reading contract:

- `paper.md`: paragraph-level English-Chinese reader with figure/table placement.
- `source_map.json`: stable source anchors, page ranges, and asset paths.
- `assets/`: images used by `paper.md`.
- `paper_DeepPaperNote.md`: Chinese deep-reading note.
- `images/`: images used by `paper_DeepPaperNote.md`.

The translation covers the main paper argument, methods, experiments, figures, tables, and conclusion. Reference entries are indexed by page range but are not translated one by one, because they are bibliographic metadata rather than scientific prose.

## Terminology Decisions

| Term | Translation |
|---|---|
| reasoning-based segmentation | 基于推理的分割 |
| open-world 3D reasoning segmentation | 开放世界 3D 推理分割 |
| 3D Gaussian Splatting | 3D 高斯溅射 |
| Gaussian primitive | 高斯基元 |
| 3D Feature Field | 3D 特征场 |
| MLLM-Based Visual Segmenter / LMSeg | 基于 MLLM 的视觉分割器 |
| Global-to-Local Spatial Grounding / GLSpaG | 全局到局部空间落地 |
| global camera | 全局相机视角 |
| local camera | 局部相机视角 |
| mBIoU | 平均边界 IoU |

## Extraction Notes

- The PDF text is searchable, but several figure captions and prompt examples contain broken glyphs or line hyphenation from PDF extraction.
- Figure/Table crops were extracted by the DeepPaperNote pipeline. Figure 6 includes a small portion of adjacent right-column text, but the main ablation visual remains readable.
- The title page lists `Zhijie Wang`; automatic metadata from external services omitted this author in one place, so the notes use the author list visible on the PDF title page.
- The project page in the abstract is line-wrapped in the PDF. It is normalized as `https://ChangyueShi.github.io/REALM`.

## Relationship To Classification

REALM is placed under `TrainingFree` because its claimed contribution is an inference-time MLLM-agent framework that avoids extensive 3D-specific post-training. This does not mean the whole system has no optimization cost: the pipeline still requires 3DGS reconstruction, 3D feature-field optimization, SAM/temporal-propagation preprocessing, MLLM calls, and local mask refinement.

## QA Checklist

- `paper.md` uses `Para. X:` / `Para. X[CN]:` style.
- Relative image paths in `paper.md` resolve under `assets/`.
- Relative image paths in `paper_DeepPaperNote.md` resolve under `images/`.
- Math uses Markdown `$...$` / `$$...$$` style.
- No `**Original:**` / `**中文:**` labels are used.
