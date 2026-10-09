# Translation Notes

## Scope

- 已处理完整 36 页 PDF，并建立全文 source manifest；正文、方法、实验、讨论与附录均纳入 `paper.md`。
- `paper.md` 采用“版面修复后的语义段落组”做中英对照：多栏断行、页眉页脚、脚注穿插与公式碎片已清理，并未把 PDF 原始行流机械逐行复制。
- 第 30–36 页 bibliography 保留在源 PDF，不逐条翻译；技术谱系已在 Related Work 和 References 索引中说明。

## Source

- Source path: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/WZ3FYLNE/Ye 等 - 2026 - World Action Models are Zero-shot Policies.pdf`
- Source type: selectable-text PDF (`pdf-text`)
- Pages: 36
- Zotero item: `WL5ZRZTL`
- Canonical extraction: `.pipeline/wam_zero_shot_raw_sections.jsonl`, `.pipeline/wam_zero_shot_source_manifest.json`

## Extraction and layout issues

- PDF 为双栏版式，自动 section detector 曾把 Section 3–4 的部分文本归入 `sec:related-work` / `sec:future-work`；`paper.md` 已根据实际标题和页码恢复正确章节顺序，原始 pipeline ID 仍保留用于 grounding。
- 数学文本层会把上下标拆成相邻字符；reader 中仅重建理解方法所需的联合分解和 flow-matching 公式，并统一为 `$...$` / `$$...$$`。
- Page 1 Figure 1 的可用裁切包含标题/作者区，但图体、编号和 caption 完整；为保留总览信息未再裁窄。

## Assets and crop caveats

- `assets/` 中共放置 16 张 Figure 与 6 张 Table，均在 `paper.md` 有对应卡片。
- DeepPaperNote 计划插入的 Figure 4、10–13、15 与 Table 1、2、4 已人工打开检查，图体清晰、编号身份匹配且无第二个图体污染。
- Algorithm 1 与 Algorithm 2 的自动候选互相混入标题或大段正文，未作为图片插入；精读笔记使用标准 figure callout 记录占位，并在正文重写关键流程。
- Figure 9 使用 page 14 的主结果裁切；page 15 的重复候选因 visual-body ratio 低而未使用。

## Terminology

- 固定使用 World Action Model (WAM)、Vision-Language-Action model (VLA)、DreamZero、DreamZero-Flash、inverse dynamics model (IDM)、flow matching、KV cache。
- `embodiment` 在跨机器人形态技术短语中保留英文；中文解释统一为“机器人形态”。
- `task progress` 译为“任务进度”，并明确它是部分完成度，不自动等同 `success rate`。

## Untranslated or skipped material

- bibliography 条目未逐条翻译。
- 作者列表、模型名、数据集名、硬件名、代码符号和正式英文 task prompt 保留原文。
- 部分 appendix 的逐项 prompt/configuration 由 Table 5–6 图像保留，正文提供协议级双语解读，没有重复转写每个单元格。

## If a stricter edition is needed

若后续需要逐句、逐脚注、逐表格单元格的法证式版本，可基于 `.pipeline/wam_zero_shot_full_text.md` 与 `source_map.json` 的 page/block 映射增补；本版优先保证完整章节覆盖、可读的中英对照、关键公式和图表语义邻近。
