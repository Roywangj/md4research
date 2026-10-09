# Translation Notes

## Scope

- 完整处理所提供的 6 页 arXiv PDF，覆盖标题与作者信息、摘要、引言、方法、实验、3 幅图、2 张表、图 3 中的完整问题/工具调用/推理轨迹，以及 36 条参考文献。
- 原文不含独立的 Related Work、Conclusion、Appendix 或 Supplementary Material 章节；`paper.md` 按原始章节顺序保留这一结构，并明确记录附录状态。
- 按 WJ reader 规范，正文采用英文 `Para. X:` 后接中文 `Para. X[CN]:` 的逐段对照形式；每个主要章节重新编号。

## Source

- Source PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/VJJ4MCVA/Ruan 等 - 2026 - World2Mind Cognition Toolkit for Allocentric Spatial Reasoning in Foundation Models.pdf`
- Source type: selectable-text PDF (`pdf-text`)
- Version: arXiv:2603.09774v1 [cs.AI], 10 March 2026
- Pages: 6
- Extraction was performed locally with Poppler text extraction and page rendering. The PDF was not uploaded to MinerU or another remote extraction service.

## Extraction and Layout

- 论文采用双栏排版。正文顺序由 `pdftotext -layout` 与 `-raw` 的输出交叉恢复，并使用 160-dpi 整页渲染逐页核对栏目、公式、图表和段落衔接。
- PDF 文本层存在断词、连字符换行、少量词间空格丢失以及公式线性化问题；`paper.md` 已清理断词并按页面渲染恢复公式。
- Equation (1) 及其 $\mu_t$ 定义已手工核对并转换为 Markdown 兼容的 `$...$` / `$$...$$` 数学格式。
- 原文作者单位编号疑似排版错误：Beihang University 与 Huawei Noah’s Ark Lab 在 PDF 文本层均显示上标 `1`，但作者行使用 `1/2/3`。Reader 不猜测修复单位编号，仅列作者姓名。

## Assets

- `assets/figure_1.png`: Figure 1，World2Mind 总体流程；从 PDF 第 2 页渲染图紧裁。
- `assets/table_1.png`: Table 1，VSI-Bench Tiny 主结果；从第 3 页紧裁，并在 Markdown 中完整转录数值。
- `assets/table_2.png`: Table 2，MindCube-Tiny 结果；从第 3 页紧裁，并在 Markdown 中完整转录数值。
- `assets/figure_2.png`: Figure 2，blind 设定比较；从第 4 页紧裁。
- `assets/figure_3.png`: Figure 3，椅子长度案例的完整推理轨迹；从第 4 页紧裁，其问题、参数、地图线索与最终答案亦在正文中逐段转录和翻译。
- 裁剪坐标与放置块均记录在 `source_map.json`。所有裁剪来自 1360×1760 像素的 160-dpi 页面渲染，未包含页眉、页脚或无关正文。

## Terminology and Translation Decisions

- `allocentric` 统一译为“非自我中心式”，`egocentric` 统一译为“自我中心式”。
- `Allocentric-Spatial Tree` 统一译为“非自我中心空间树”，并保留缩写 AST。
- `Landmark Cognitive Map` / `Route Cognitive Map` 分别译为“地标认知地图”/“路径认知地图”。
- 方法名、模型名、数据集名、指标缩写、变量、公式及 YAML/API 字面量保留英文或原始符号。
- 原文交替使用 `geometry-semantic` 与 `semantic-geometry`；中文根据语境统一为“几何—语义（对齐）”，方法链 `geometry-semantics interwoven reasoning` 统一译为“几何—语义交织推理”。

## Source-Level Caveats

- 原文 Abstract 写 GPT-5.2 等模型提升 “5%–18%”，Introduction 后文写 “6%–18%”；Reader 忠实保留各处数值，没有擅自统一。
- MindCube 分析段落在原文中写 “Tab. 1”，但 MindCube 结果实际位于 Table 2。Reader 按实际对应关系写为 Tab. 2，并在 `source_map.json` 记录此源文问题。
- Table 1 并非所有子任务都提升：GPT-5.2 在 Obj. Count、Abs. Dist.、Obj. Size 上下降，Gemini-3-Pro 在 Obj. Size 上下降。数值与升降箭头均按表格原样转录。
- 原文将 MindCube [18] 引向一条题为 “MindCube: an interactive device for gauging emotions” 的参考文献；这可能与文中所述空间基准不一致，但 Reader 不外部更正引用，只忠实保留来源。
- 图 3 的小字号内容经页面图像与文本层交叉核对；图中品牌图标等装饰性文字未单独转录，但所有关键问题、工具参数、测量线索、交叉验证和最终答案均已覆盖。

## References Policy

- 参考文献 [1]–[36] 全部保留在 `paper.md` 中，维持英文书目信息，不逐条翻译。
- PDF 参考文献末尾自动生成的正文引用页码（例如单独的 `1`, `2`, `3`, `4`）不属于书目元数据，已移除。
- 长作者列表中原文使用 `et al.` 的条目维持缩写；其余条目按 PDF 可提取信息转录。

## Untranslated / Skipped Material

- 无正文、方法、实验、标题、图注、重要表格、案例提示词或参考文献被跳过。
- 未翻译每条参考文献的标题与出版信息，符合 WJ reader 的默认参考文献政策。
- PDF 不含附录、补充材料、数据可用性、代码可用性、利益冲突或致谢章节，因此没有对应内容可处理。

## Stricter Verbatim Edition

当前 reader 在保持全部实质内容与来源顺序的前提下，清理了断词、PDF 排版噪声，并对部分长句作最小的可读性规范化。若需要逐字符校勘版，下一步应对照 PDF 逐行复核标点、作者单位上标和每条参考文献的完整作者名单；正文技术内容、公式、数值、图表与提示词已经完整覆盖。
