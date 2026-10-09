# Translation and reading notes

- Source resolved from Zotero item `V854MLW3`, attachment `LMWA29XW`.
- Local PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/LMWA29XW/Chen 等 - 2025 - Geometrically-Constrained Agent for Spatial Reasoning.pdf`.
- Detected source format: selectable-text PDF, read through the `pdf-text` route.
- Extracted coverage: 27 / 27 pages, not truncated.
- The automatic section parser placed appendices and references together under `sec:references`; the reader separates them semantically where needed.
- Main translation policy: method names and symbols are preserved when they carry formal meaning, while explanatory prose is translated into Chinese.
- Figure policy: all extracted figure/table assets are stored in both `assets/` and `images/`. The refined note inserts only the visually usable core items selected by the figure-decision pass.
- Visual quality caveat: Table 1 is too thin after automatic cropping, and Figure 5 contains neighboring page content. Their key values are transcribed in text instead of being treated as clean primary figures in the refined note.
- Version note: metadata identifies arXiv `2511.22659v1`, published on 2025-11-27.

## Important terminology decisions

| Source term | Chinese rendering | Note |
|---|---|---|
| Geometrically-Constrained Agent | 几何约束代理 | First mention keeps English and abbreviation `GCA`. |
| semantic-to-geometric gap | 语义到几何的鸿沟 | Core failure mode of VLM spatial reasoning. |
| formal task constraint | 形式化任务约束 | Preserve symbol `Ctask`. |
| Reference Frame Constraint | 参考系约束 | Preserve symbol `CR`. |
| Objective Constraint | 目标约束 | Preserve symbol `CO`. |
| semantic analyst | 语义分析者 | Role of the VLM in task formalization. |
| task solver | 任务求解器 | Role of the VLM during constrained computation. |
| knowledge-augmented code generation | 知识增强代码生成 | Preserve abbreviation `KACG` after first mention. |

