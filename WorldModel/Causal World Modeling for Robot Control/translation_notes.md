# Translation Notes — Causal World Modeling for Robot Control

## Scope

- 完整处理 PDF 31 页中的可提取正文：Abstract、Introduction、Preliminary、Method、Experiments、Related Work、Conclusion、Acknowledgment 与 Appendix A。
- 参考文献 [1]–[97] 不逐条翻译；标准书目信息以源 PDF 为准。
- 主文 Figure 1–10、Table 1–3 与附录 Table S1–S7 均已裁切到 `assets/`，并在 `paper.md` 中附中英图注与阅读提示。
- 附录逐 trial 表格以高分辨率图片完整保留；正文翻译其评测协议、指标定义、任务说明和关键汇总数值，不重复转写数百个表格单元格。

## Source

- Source path: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/ECJKCB63/Li 等 - 2026 - Causal World Modeling for Robot Control.pdf`
- Source type: selectable-text PDF (`pdf-text`)
- PDF metadata: 31 pages; arXiv:2601.21998v2; generated 22 Mar 2026.
- Extraction used Poppler text extraction in normal and layout-preserving modes. Multi-column paragraphs were manually restored to natural reading order.

## Translation and notation decisions

- 方法名、模型名、数据集名与 benchmark 名保留英文；稳定概念采用 Terminology Ledger 中的统一中文。
- 将论文中的 flow time 保留为 $s$；可见公式统一使用 `$...$` / `$$...$$`，未使用 `\(...\)` 或 `\[...\]`。
- 将“causal”限定解释为跨 chunk 的时间因果依赖。论文明确说明 chunk 内 token 仍通过双向注意力并行生成，因此没有把它误译为“所有 token 都严格单向”。
- 原 PDF 的动作初始化缩放公式在文本层的根号排版较弱；结合公式版面保留为 $\alpha=\sqrt{d_v/d_a}$。
- Algorithm 1–2 以忠实的过程性双语段落重写，保留所有关键状态、积分终点、缓存更新和并发分支；未逐行复制 LaTeX algorithmic 排版。

## Layout and asset notes

- 图表裁切基于 144 dpi 页面渲染，bbox 记录在 `source_map.json` 的 `bbox_144dpi` 字段。
- Figure 3 位于双栏页面右栏，已紧裁到 attention mask 与图注区域；其较小字号来自论文原版面。
- Figure 6 与附录表格纵向较长，保留原始纵横比，建议在 Obsidian 中点击放大查看。
- Table 3 在原稿中只列出部署与预训练消融；正文所称 AR 与 bidirectional 消融未在当前版本表格中显示，reader 未补造缺失行。

## Evidence caveats recorded in the reader

- Appendix Table S4 显示 Fold Clothes 上 LingBot-VA 的 SR 略高，但 PS 低于 $\pi_{0.5}$；这与主文“所有任务、两个指标均领先”的概括并不完全一致，已在 Critical Reading Notes 中明确指出。
- Novel object / spatial generalization 主要为定性图，缺少完整量化表。
- 长期记忆证据来自 horizon 分组和两项专门任务，但未系统消融 KV 上下文长度。

## If a stricter edition is required

当前版本是完整、意义忠实的双语 reader，而非逐句法律式直译。若需要逐行复刻算法环境或把 Appendix Table S1–S7 转成可搜索 Markdown 表格，可在现有 `source_map.json` 与裁图基础上继续扩展，无需重新提取 PDF。
