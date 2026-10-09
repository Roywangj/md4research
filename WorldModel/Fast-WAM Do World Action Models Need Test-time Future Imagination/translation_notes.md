# Translation Notes

## Scope

- 完成论文 13 页的可提取正文双语 reader，包括摘要、引言、相关工作、方法、实验、结论与附录。
- 参考文献共 38 条，保留于源 PDF，不逐条翻译；相关工作正文中的数字引用保持原样。
- 公式（1）至（9）已转写为 Markdown 兼容的 `$...$` / `$$...$$` 数学格式。

## Source

- Source path: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/DPU4SKTI/Yuan 等 - 2026 - Fast-WAM Do World Action Models Need Test-time Future Imagination.pdf`
- Source type: selectable-text PDF (`pdf-text`)
- PDF metadata: arXiv:2603.16666v2, 13 pages, 23 March 2026.
- Layout: mainly two-column body text, with full-width figures and tables.

## Extraction and layout

- 文本层可直接提取；正文按自然阅读顺序重新拼接，并修复跨行断词。
- PDF 第 4 页处的式（2）积分符号在原始文本抽取中与公式主体分离，reader 已依据页面视觉布局复原为完整积分表达式。
- 图 1-4、表 1-3 均从 220 dpi 页面渲染中紧裁切，caption 不烘焙进图片，而是在 Markdown 中单独保留中英文图注。
- 表 3 为高密度逐任务表，已保留高分辨率图片；正文只解释整体趋势，不重复转录约 50 个任务的全部数值。

## Terminology decisions

- `video co-training` 统一译为“视频协同训练”，指动作训练同时使用未来视频预测损失；不译为容易被误解为数据预训练的“视频预训练”。
- `test-time future imagination` 统一译为“测试时未来想象”。
- `imagine-then-execute` 统一译为“先想象、后执行”。
- `embodied pretraining` 统一译为“具身预训练”。需要注意，论文所称“without embodied pretraining”仍使用预训练 Wan2.2-5B、T5 与视频 VAE，并非从随机权重训练。
- `w.o. video co-train` 表示移除视频协同训练目标，reader 中统一表述为“无视频协同训练”。

## Fidelity notes

- Reader 保留所有可提取的实质性正文、数值、公式与图表 caption；个别重复性过渡句在清理时与相邻原文段落合并，但未改变论证链。
- Introduction 的三条贡献在 PDF 中为项目符号；reader 为保持段落式中英对齐，将其合并为一个双语段落。
- References 未逐条翻译，符合 WJ reader 默认策略。

## Asset inventory

- `assets/fig1_wam_paradigms.png`
- `assets/fig2_fast_wam_architecture.png`
- `assets/fig3_towel_folding.png`
- `assets/fig4_real_world_results.png`
- `assets/table1_robotwin_results.png`
- `assets/table2_libero_results.png`
- `assets/table3_robotwin_per_task.png`

## If a stricter edition is needed

如需逐句而非逐段对齐，或需将表 3 转录为可搜索 Markdown 表格，可在当前稳定 block ID 与页面定位基础上继续扩充，而无需重新提取 PDF。
