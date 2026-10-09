# Translation & Extraction Notes

## 模式 / Mode
- **完整双语阅读器（full bilingual reader）**，非摘要。覆盖全部 16 页正文 + 附录 A–F + 参考文献。
- 源文件：selectable-text PDF（`pdf-text`）。用 PyMuPDF 抽取文本层，未做 OCR。
- 图/表：用 PyMuPDF 在 zoom 4.0（约 288 dpi）下按 PDF 坐标裁剪为 PNG，存于 `assets/`。所有 16 个裁剪均经肉眼核对，裁切框准确、内容完整。

## 术语一致性 / Terminology
- 全文锁定术语见 `paper.md` 末尾"术语表"。关键：MPM=物质点法，VLM=视觉-语言模型/代码生成，VDM=视频扩散模型。
- 五个评估指标统一译法并标注方向：W-MAE/CTV/OCS/RTSJ 越低越好（↓），mIoU 越高越好（↑）。
- 数据集名以源文最常用形式 **MPMWorlds** 为准（摘要/引言曾出现单数变体 "MPMWorld"，已统一为 MPMWorlds，详见下"已知不一致")。

## 已知原文不一致 / Source inconsistencies (保留并标注，未擅自改写原文含义)
- 引言 Para.3 原文写 "a new dataset, MPMWorld"（单数），而标题与其余处均为 "MPMWorlds"。译文统一用 MPMWorlds，属原文笔误。
- 数据集规模描述存在两处数字：3.2 节给出精确值 **95,805** 渲染模拟、**9,204** Scene Templates；而 3.1 节与正文多处口语化称 "approximately 1k Parent + 9k Child = 10k Scene Templates"。二者并不矛盾（10k 为约数，9,204 为精确数），译文均如实保留。

## 公式 / Equations
- 6 个公式（IoU、s_t_n、OCS、e_t、anomaly 指示函数、门控 argmin）已转写为标准 Markdown `$$...$$` 显示块，置于段落 blockquote 之外，保证渲染。
- 公式由 PDF 文本层重组（原 PDF 文本层把分式拆成多行散块），已按数学含义重建；如需逐字符核验请对照原文 P13–P15。**置信度：高**（结构清晰，符号无歧义）。

## 图表放置 / Figure placement
- 按"首次实质提及处就近放置"原则，而非严格 PDF 物理页序。例如：
  - Figure 12、13（位于 PDF 附录页 15/16）在正文 §5 首次被讨论，故就近放在 §5。
  - Figure 5（PDF 第 8 页右栏）放在材料敏感性讨论处。
  - Figure 6（"failure cases shown in Figure 6"）紧跟其首次提及段。
- 原始页码与裁剪框（crop_box）全部记录在 `source_map.json` 的 `figures`/`tables` 字段。

## 数值核对 / Number cross-check
- 图 4（热力图）与表 2（数值表）为同一测试集结果，数字一致（如 Frames+Full Config: W-MAE VLM 0.254 / VDM 0.298 两处吻合）。
- 图 12 与表 3 为修改验证集，同样交叉吻合。
- 表 1 门控数值与图 4 的 VLM/VDM 列一致。
- 以上交叉核对通过，主结果数字可信。

## 未处理/低置信 / Skipped or low-confidence
- 无整页缺失、无扫描页，全部页面均有可选文本层。
- Figure 1 与 Figure 9/10/11 等含大量小图块（image grids）；裁剪为整幅复合图，未逐子图拆分（保持论文原排布即可理解）。
- 参考文献按原始书目格式保留英文，未翻译（学术惯例）。

## 交付物 / Deliverables
- `paper.md` — 全文中英对照阅读器（主交付物）
- `source_map.json` — 稳定块 ID、页码、裁剪框、术语表、关键数字
- `translation_notes.md` — 本文件
- `assets/` — 16 个图/表裁剪 PNG
