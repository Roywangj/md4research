# Translation Notes

## Scope

- 已处理完整 23 页 PDF，并建立全文 source map；正文（Abstract、Introduction、Related Work、Method、Experiments、Limitations、Conclusion）与附录 A–D 全部纳入 `paper.md`，均为段落级中英对照。
- `paper.md` 采用“版面修复后的语义段落组”做对照：双栏断行、图注穿插、公式碎片和被 section detector 误切的文本已清理合并，不是 PDF 原始行流的逐行复制。
- 第 9–12 页 bibliography（[1]–[47]）不逐条翻译；References 一节给出双语的技术谱系索引。

## Source

- Source path: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/2I9EGQ7W/Chen 等 - 2026 - LaWAM Latent World Action Models for Efficient Dynamics-Aware Robot Policies.pdf`
- Source type: selectable-text PDF (`pdf-text`)
- Pages: 23（正文 1–9，参考文献 9–12，附录 13–23）
- arXiv: 2606.15768（cs.RO, 14 Jun 2026）
- Canonical extraction: pipeline workdir（scratchpad `lawam_tr/`）中的 `paper_raw_sections.jsonl` 与 `paper_full_text.md`；后者 sha256 记录于 `source_map.json`。

## Extraction and layout issues

- 自动 section detector 把第 6–8 页切出了虚假的 `sec:method-2` / `sec:method-3` / `sec:appendix-d-4-...` 区块（实际是 Table 1 数据行、4.2–4.5 小节正文），并把全部附录并入 `sec:references`（标注 pages 9–23）。`paper.md` 已按论文真实标题层级（4.1–4.5、A–D、C.1–C.5、D.1–D.4）恢复章节顺序。
- Table 1 的文本层丢失了大部分基线的 Size/Latency 单元格（仅 F1 的 399.0 可见），成功率列完整；正文与图注只引用了可从文本层核实的数字，其余以 Table 1 裁切图为准。
- Table 2/Table 4 的逐任务数值在文本层缺失（只有六列平均值），以裁切图为准；平均值已在图注和 Appendix A 段落中双语转写。
- Eq. (7) 的 $\omega_k$ 表达式在文本层断裂为 `exp(−log(P_max) · max(K−1,1))`，缺少分子 $k$。`paper.md` 按标准正弦位置编码重建为 $\omega_k=\exp(-\log(P_{\max})\cdot k/\max(K-1,1))$，此处为低置信重建，若需引用请对照原 PDF 第 15 页。
- 数学上下标在文本层被拆散（如 `˜uT`、`∥·∥2 2`），已统一重建为 `$...$` / `$$...$$` 记号。

## Assets and crop caveats

- `assets/` 共 18 张：15 张 Figure（1–5、6*、7–15）+ 3 张 Table（1、2、4），全部在 `paper.md` 有对应图表卡片，命名保持 pipeline 的 `page_XXX_fig_*.png` 约定。
- Figure 6（消融图）：pipeline 原裁切含整栏左侧正文（reject: large_text_block_suspected）。本版对其做了二次裁切去除左栏文字，图例上缘轻微裁边但五个图例项可辨认，左边缘残留个别字符碎片；图注中已提示纵轴从 90% 起。
- Table 3（真机成功率）：自动裁切只截到图注区（reject: table_body_missing / caption_only_suspected），未作为图片插入；已按文本层数值在 `paper.md` 中转写为 Markdown 表格，数值完整（4 方法 + LaWAM × 3 任务 + 平均）。
- Figure 7：pipeline 因空白占比大标记 reject（low_visual_body_ratio），人工检查图体与图注完整清晰，照常使用。
- page_018 的 `fig_12` 候选是把 "Fig. 12." 引用行误判为图，未使用。
- Figure 5 与 Figure 15 中 (d)(e)/(f)–(j) 面板来自 pi.website 截图，属论文原始内容，非裁切问题。

## Terminology

- 固定使用 LaWAM、LaWM、WAM（世界—动作模型）、VLA（视觉—语言—动作模型）、LAM（潜在动作模型）、latent action（潜在动作）、latent visual subgoal（潜在视觉子目标）、IDM（逆动力学模型）、Knowledge Insulation（知识隔离）、physical-time encoding（物理时间编码）、action chunk（动作块）、action expert（动作专家）。
- 模型/数据集/benchmark 名保留英文：DINOv3、Qwen3-VL、Alternate-DiT、V-JEPA2、Genie、LIBERO、RoboTwin、Fast-WAM、LingBot-VA、GigaWorld-Policy、Motus、Cosmos-Policy、LDA-1B、$\pi_0$/$\pi_{0.5}$/$\pi_{0.7}$、GR00T-N1.6、Franka Emika Panda、Quanta X1。
- `embodiment` 在技术短语（cross-embodiment 等）中保留英文，中文释义统一为“机器人形态”。
- 作者名采用 PDF 首页拼写（Kang Chen、Weilin Liu、Chao Yu）；Semantic Scholar 元数据给出变体 Kanghao Chen、Weiling Liu、Chaoyang Yu，已记录于 `source_map.json`。

## Untranslated or skipped material

- bibliography 条目 [1]–[47] 未逐条翻译。
- 作者列表、机构名、模型名、数据集名、任务名（如 RoboTwin 的 50 个任务名）保留英文；Table 4 逐任务数值由图片承载，未逐格转写。
- 图 8、11–13 的逐 chunk 面板内容由图片承载，正文提供协议级双语解读。

## If a stricter edition is needed

若需逐句、逐单元格的法证式版本，可基于 scratchpad `lawam_tr/paper_full_text.md`（sha256 见 `source_map.json`）与 `source_map.json` 的 page/block 映射增补；需要优先补的三处是：Table 1 的 Size/Latency 列、Table 2/4 的逐任务数值（都需从 PDF 渲染页或原图重新读取），以及 Eq. (7) 中 $\omega_k$ 的精确表达式核对。本版优先保证全文段落级覆盖、正确章节顺序、关键公式重建和图表语义邻近放置。
