# Translation Notes

## Scope

- 已处理完整 8 页 RA-L PDF（arXiv 2502.00622v4，accepted February 2026），Abstract、I–VII 全部正文、Appendix A 均以段落级中英对照纳入 `paper.md`，无摘要式降级。
- 公式 (1)–(7) 逐条保真转写为 `$$...$$` 独立块并保留原编号（`\tag{n}`）；行内数学统一 `$...$`。
- 第 7–8 页 bibliography（[1]–[44]）按阅读器约定不逐条翻译，正文技术谱系在 References 节做了双语说明。

## Source

- Source path: `/root/wwwroy/papernotes/papers/2502.00622v4.pdf`
- Source type: selectable-text PDF (`pdf-text`)，8 页，双栏 IEEE 版式
- Canonical extraction（只读复用）: `/tmp/claude-0/-root-wwwroy-papernotes/fbcd5d0c-d98e-409d-8a49-a3bbe90bb6f3/scratchpad/gpc_smoke/`（`paper_raw_sections.jsonl`、`paper_full_text.md`、`paper_assets.json`）
- 页 5、6 另行渲染为位图核对了 Table I–III 的逐格数值。

## Extraction and layout issues

- 自动 section detector 把参考文献条目错切成伪章节（`sec:models`、`sec:models-2`），并把 Table III 区域归入独立的 `sec:method`；`paper.md` 已按 PDF 逐页文本恢复真实的 IEEE 章节顺序（I–VII → References → Appendix）。
- PDF 文本层把上下标拆成相邻字符（如 `a(k) t:t+T`、`oNd t+1`）；所有公式和行内符号均据原版式人工重建。
- Introduction 的 Contribution 第二个 bullet 在文本层丢字（"Predictive world modeling. learn action-conditioned world model..."），已按语义补回 "We learn an action-conditioned world model..."。
- 首页脚注（稿件收稿/录用日期、编辑信息、作者单位、ONR N00014-25-1-2322 资助、通讯作者邮箱、DOI 说明）为元数据，未纳入对照正文。
- V.B 节两条脚注为基线代码 GitHub 链接（physical_interaction_video_prediction_pytorch、flow-diffusion/AVDC），未放入正文，已记录在 `source_map.json` 的 S014 摘要中。

## Assets and crop caveats

- `assets/` 共 9 张裁切（Fig. 1–8 + Algorithm 1），全部来自抽取管线并在 `paper.md` 有对应图块；命名保持 `page_XXX_fig_*` 原样。
- 管线视觉质量门曾拒绝 Algorithm 1 与 Fig. 4 两张裁切；人工目视复核后均采用：Algorithm 1 裁切实际完整清晰；Fig. 4 顶部混入同页 Fig. 3 与 TABLE II 的图注文字，但图体与图注完整，已在图块 Reading note 与此处注明。
- Fig. 2 裁切右侧混入第 4 页右栏正文文字，图体与图注完整，已注明。
- Table I、II、III 没有可用图片裁切，已按 PDF 文本层转录为 Markdown 表格，并对照页面位图逐格核验；Table I 由原横排单行布局改为纵向表。
- 原文两处印刷疑误按原样转录并加注：Fig. 6 图注 GPC-OPT "(K = 0, M = 25)"（语义上应为 K = 1）；Table III 基线 "(K=1, M=1)"（正文定义为 M = 0）。
- Fig. 8 无数值标注，Reading note 中的成功率（0.5/0.7/0.7；0.3/0.7）为从柱状图读数，非正文数字。

## Terminology

- 固定使用 GPC、GPC-RANK、GPC-OPT、GPC-RANK+OPT、Diffusion Policy、AVDC、LaDi-WM、V-GPS、DreamerV3、MPPI、CEM、DDPM、EDM、SSIM、IoU、VLM、AprilTags 等英文名。
- behavior cloning 译"行为克隆"，model predictive control 译"模型预测控制"，action proposal 译"动作提案"，action chunk 译"动作块"，registration loss 译"配准损失"，freeze the noise 译"冻结噪声"，sufficient excitation 译"充分激励"，receding horizon 译"滚动时域"。
- 完整术语约定见 `paper.md` 的 Terminology Ledger（20 条）。

## Untranslated or skipped material

- bibliography 条目未逐条翻译。
- 首页元数据脚注、页眉页脚（"IEEE ROBOTICS AND AUTOMATION LETTERS..." / "QI et al.: ..."）、arXiv 水印未纳入。
- 基线代码 GitHub 链接脚注未放入正文（见上）。

## If a stricter edition is needed

若需逐句、逐脚注的法证式版本，可基于 `gpc_smoke/paper_full_text.md` 与 `source_map.json` 的 S/F/T 块映射增补：补入首页脚注块、两条 GitHub 脚注原文，以及 Algorithm 1 的逐行文字转写（当前以图片 + 语义 Reading note 呈现）。本版优先保证全文段落覆盖、公式编号保真和图表语义邻近。
