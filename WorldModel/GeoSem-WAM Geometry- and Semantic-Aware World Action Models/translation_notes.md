# Translation Notes

## Scope

- 完整处理规范源 `arXiv:2606.03188v1` 的 14 页内容。
- `detailed_paper.md` 覆盖摘要、正文、贡献列表、公式 (1)–(9)、Figures 1–6、Tables 1–5、结论与局限、Acknowledgments、45 条英文书目、Appendix A–B。
- 正文采用英文段落后紧跟中文译文的 `Para. X` / `Para. X[CN]` 配对；参考文献保持完整英文书目，以便搜索和核对。

## Source and duplicate attachment

- 规范源：`MRPFNLQG/Ma 等 - 2026 - GeoSem-WAM Geometry- and Semantic-Aware World Action Models.pdf`。
- 重复附件：`NNAX23L5/Ma 等 - 2026 - GeoSem-WAM Geometry- and Semantic-Aware World Action Models.pdf`，仅记录，未重复处理。
- 两个附件的 SHA-256 均为 `11b2421367cfa8167a2cd96938c7b17776ebf3326db4fa19f7fcf78dfcc3dfad`。
- PDF 为可选择文本，另以 arXiv v1 LaTeX 源和 200/300 DPI 页面渲染交叉核对多栏顺序、公式、表格与图注。

## Extraction and layout issues

- PDF 文本提取器在页 6–8 将部分实验文字误判为 `Method`，并未可靠识别附录；最终结构以 PDF 视觉版面和 LaTeX 源为准。
- Table 5 位于第 12 页，字号很小。其 Markdown 转录直接来自 v1 LaTeX 表格并与渲染页核对，严格包含 50 个任务行；`Average` 是额外汇总行，不计入任务数。
- 原文附录使用 `Libero-10`，正文使用 `LIBERO-Long`。阅读稿按各自源位置保留命名，不擅自统一。
- 正文称相对 Fast-WAM 的 RoboTwin 平均成功率“improves by 0.8%”，表中精确值为 92.52% 与 91.80%，绝对差为 0.72 个百分点。详细稿忠实保留正文与表格；精读稿按表值解释。

## Assets

- Figures 1–6 直接采用 arXiv 源包中的原始 PNG，避免页面裁剪损失多 panel、图例和标签。
- Tables 1–5 从 300 DPI 页面渲染裁剪；表头、数据主体与必要脚注均纳入。
- Table 5 同时提供完整高分辨率裁剪与可搜索 Markdown；Markdown 数值是核对权威。
- `images/` 只放精读稿实际使用的 5 张精选图表，`assets/` 保留阅读稿全部 11 张图表资产。

## Terminology policy

- 模型、数据集、指标、硬件与架构标识（如 `Fast-WAM`、`Wan2.2-5B`、`DPT`、`LIBERO`、`RoboTwin`）保留英文。
- `geometry` 根据语境译为“几何”或“几何信息”；源文未明确把所有几何监督等同于公制度量深度，因此不扩写为未证实的具体标注定义。
- `token` 在详细双语稿中保留为 token；精读稿为通过自然中文风格检查，多数表述为“表征单元”。

## Acknowledgments placeholder

- Acknowledgments 是 CoRL 模板占位文字：它说明若论文接收，最终版本应包含致谢，并列举可感谢的对象。
- 该文字已原样保留并翻译；它不是本文具体致谢。未补造资助、同事、审稿人或机构信息。
- 精读稿仅将其视为 arXiv v1 尚未清理 camera-ready 模板的客观成熟度信号，不推测作者意图。

## Completeness and caveats

- 未发现 Algorithm；未创建虚构算法块。
- 没有跳过正文、局限、附录、图表 caption 或表脚注。
- 论文没有给出具体损失权重、训练时长、峰值显存、批大小、多个训练种子、置信区间、深度探针误差或实测推理延迟；这些均在精读稿中作为证据边界处理，而非补造。
