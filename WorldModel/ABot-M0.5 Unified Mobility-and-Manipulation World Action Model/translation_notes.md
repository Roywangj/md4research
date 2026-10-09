# Translation and Extraction Notes

## Scope

- 已完成 33 页 PDF 的全文级中英对照阅读稿，覆盖摘要、引言、问题定义、完整方法、训练流程、实验、结论、作者贡献、致谢与 82 条参考文献。
- 原 PDF 没有附录或补充材料章节，正文在第 28 页结束，参考文献位于第 29–33 页。
- `detailed_paper.md` 是 `nature-reader-detail` 的主交付；`paper.md` 按 WJ 阅读习惯保留同一份已验证全文读本。
- 分析性判断、局限与复现提示放在 `paper_DeepPaperNote.md`，没有混入原文翻译段落。

## Source

- 源文件：`/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/W37BGA56/Chen 等 - 2026 - ABot-M0.5 Unified Mobility-and-Manipulation World Action Model.pdf`
- 来源类型：可选择文本 PDF（`pdf-text`）
- 页数：33
- 论文标识：arXiv:2607.00678v2，DOI `10.48550/arXiv.2607.00678`
- 源文件是用户明确给出的本地 Zotero 附件，因此作为规范版本使用，没有用标题搜索所得的网络副本覆盖。

## Extraction and Layout

- PDF 为多栏学术排版。正文抽取已按章节和页码重新排序，去除了页眉、目录点线、重复图中文字和空字符。
- 共核对 13 幅图、8 张表和 29 个编号公式。
- 英文正文在读本中按语义完整的段落组清洗，紧跟对应中文译文；所有数字、数据集名、模型名、比较方向和保留语气均按源文检查。
- 公式统一为 `$...$` 与 `$$...$$`，没有保留 `\(...\)` 或 `\[...\]`。

## Assets

- `assets/` 保存全文读本使用的 13 幅图和表 1–6 裁图，共 19 个可用资产。
- `images/` 保存精读笔记中人工选择并检查的 10 幅核心图。
- 所有插入图片均使用论文文件夹内的相对路径，最终检查不存在断链。
- Figure 9 的自动裁图包含较多相邻正文，但主体图完整；它仅放入全文读本，没有放入精读笔记。

## Table Caveats

- Table 7 与 Table 8 的自动裁图只保留了标题，没有完整表体，因此未插入损坏图片。
- 两表已在 `paper.md` / `detailed_paper.md` 和 `paper_DeepPaperNote.md` 中按源 PDF 数值转录为 Markdown，保持可检索、可复制。
- 其余关键表同时保留原图和 Markdown 转录；若原图中文字过小，应以 Markdown 数值为主要阅读入口，并以 PDF 原页作最终核对。

## Terminology

- `World Action Model` 译为“世界—动作模型”。
- `latent action` 译为“潜在动作”，指相邻视觉状态转移的帧级运动表征，不等同于可执行控制。
- `mobility action` 译为“移动动作”，`manipulation action` 译为“操作动作”。
- `Dream Forcing` 与 `Mixture-of-Transformers` 保留英文名称，并在首次出现处解释。
- 模型、数据集、基准与指标名称保留英文，以保证与代码和文献可对应。

## References

- 参考文献保留英文书目信息，不逐条翻译。这样可以保持作者、题名、会议／期刊和 arXiv 标识可搜索。
- 为控制读本长度，参考文献在不改变身份信息的前提下采用紧凑书目格式；需要完整作者列表或 URL 时，以源 PDF 第 29–33 页为准。

## Known Source Ambiguities

- RoboCasa365 的 46.6% 对应 `ABot-M0.5 + Condensed Memory`，基础模型结果为 40.4%。正文没有充分定义 Condensed Memory，精读笔记已单独标注。
- LIBERO-Plus 的 83.4 是表中 WAM 分组最高结果，不是全部方法总体最高；Qwen-RobotManip-Context 为 91.4。
- 真实机器人段落称有“三个多阶段任务”，但正文列表和 Figure 12/13 实际包含四个长时程任务：Plate、Fruits、Cup Stacking、Flower，另有 Peg 精细操作任务。
- 真实平台为 Agilex Piper 六自由度单臂桌面系统，不包含真实移动底盘；因此真实实验不能直接证明实体移动—操作闭环。

## Validation

- `detailed_paper.md` 已通过 `validate_detailed_paper.py`：51 对双语段落、21 对双语图表标题、19 个图片链接、0 个断链。
- `paper_DeepPaperNote.md` 已通过 DeepPaperNote lint 的结构、风格、公式、图像、引用卫生、计划和实质内容门禁。
- `source_map.json`、计划、接地、图表决策和 lint 文件均应保持为有效 JSON；最终交付前另行执行统一解析和链接检查。
