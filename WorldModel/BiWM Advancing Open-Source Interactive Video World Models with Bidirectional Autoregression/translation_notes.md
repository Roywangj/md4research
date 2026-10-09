# Translation Notes

## Scope

- 已处理完整 19 页 PDF 并建立全文 source map；摘要、引言、相关工作、方法（3.1–3.7）、实现细节、结果（5.1–5.2）、结论全部段落级双语覆盖，共 55 组 `Para. X:` / `Para. X[CN]:` 对照与 9 个图卡片。
- 本文没有附录、没有表格（正文未出现任何 "Table"，抽取器也未产出表格裁切），因此不存在"附录分块略译"问题——正文即全文。
- `paper.md` 采用"版面修复后的语义段落组"做中英对照：双栏断行、公式碎片、脚注穿插已清理；Introduction 的脚注 1（"causal" 模型常用局部窗口）折叠为 Para. 2 中的括号句。原始 PDF 行流未逐行机械复制。
- 第 17–19 页 bibliography 保留在源 PDF，不逐条翻译；References 一节给出双语的技术谱系索引。

## Source

- Source path: `/root/wwwroy/papernotes/papers/Rui 等 - 2026 - BiWM Advancing Open-Source Interactive Video World Models with Bidirectional Autoregression.pdf`
- Source type: selectable-text PDF (`pdf-text`)，19 页，arXiv:2606.10135v1（2026-06-08），代码 https://github.com/LynnReal-AI/BiWM
- Canonical extraction（翻译侧独立运行，未触碰精读 agent 的 workdir）：
  `/tmp/claude-0/-root-wwwroy-papernotes/fbcd5d0c-d98e-409d-8a49-a3bbe90bb6f3/scratchpad/biwm_tr/paper_raw_sections.jsonl`、`paper_full_text.md`
- 图表裁切来源（pipeline 共享资产根，仅拷贝、未修改）：
  `/root/wwwroy/papernotes/tmp/DeepPaperNote/assets/BiWM_Advancing_Open_Source_Interactive_Video_World_Models_with_Bidirectional_Autoregression/images/`

## Extraction and layout issues

- 双栏版式，section detector 把页 13 的 "Implementation Details" 归入 `sec:method`（页 5–13），把图 7–9 的 caption 归入 `sec:conclusion`（页 14–17）；`paper.md` 已按论文自身编号（5.1/5.2 表明 Results 是第 5 节）恢复为 4. Implementation Details / 5. Results / 6. Conclusion，并把图 7–9 放回 5.2 的讨论处。
- 数学文本层碎裂严重：式 1 的连乘号、式 2 的 underbrace、式 3–6 的矩阵维度、式 7–11 的期望下标在原始抽取中均被拆散。全部 12 个编号公式已按上下文重建为 `$...$` / `$$...$$`，编号跟随论文（\tag{1}–\tag{12}）。重建过程做过一致性验证（如 flow-matching 参数化 $\hat{x}_0 = x_\sigma - \sigma v_\theta$ 与 $x_\sigma=(1-\sigma)x_0+\sigma\epsilon$ 自洽），但若需引用逐符号细节，建议回对 PDF 原页。
- 长段落（如 Introduction 的因果/双向对比、3.3 的四步机制、3.5 的目标函数族）按语义拆成多个 Para 对；公式前后被拆开的英文句用 "Para. N (cont.):" 续块承接，中文侧则合并为完整一段。

## Assets and crop caveats

- `assets/` 共 9 张 Figure 裁切（page_002 两张、page_003、page_009、page_012、page_013、page_015 两张、page_016），全部在 `paper.md` 有对应图卡片，编号身份与图注逐一核对（人工查看了 Fig. 1、3、4、8 四张，其余按 pipeline quality_signals=usable 采信）。
- 所有裁切均带原始印刷图注，图体完整、无正文污染。
- Figure 2（页 2 的展示图）按"首次实质讨论"原则放在 5.2 Camera controllability 段旁，而非页序位置；Figure 7/8 的裁切文件名是 page_015（其 caption 印在页 15），与 PDF 实际排版一致。
- 本文无表格资产，无需 Markdown 转写补救。

## Terminology

- 固定使用 bidirectional autoregression（双向自回归）、chunk（保留英文）、KV cache（KV 缓存）、DMD、Self-Forcing、camera-text、mode-seeking / mass-covering（保留英文并首次注释）、FramePack / PackForcing、first-frame sink（首帧 sink）、NVFP4 / FP8-E4M3、QAT。
- 模型/数据集/框架名一律保留英文：minWM、Yume-1.0/1.5、Matrix-Game-3.0、Wan2.1-T2V-1.3B、Wan2.2-TI2V-5B、HunyuanVideo-1.5-TI2V-8B、LTX-2.3-22B、Sekai、OpenVid、WorldPlay、SANA-WM、HunyuanWorld-1.5、CaPE、GTA、PRoPE、UCPE、CausVid。
- `rollout` 保留英文（语境中偶配"滚动生成"解释）；`anchor loss` 译"锚损失"；`teacher/student` 在蒸馏语境保留英文。
- Terminology Ledger 共 20 条，见 `paper.md` 表格。

## Untranslated or skipped material

- bibliography 条目未逐条翻译（约 40 条，页 17–19）。
- 作者列表、机构、邮箱、代码链接、图内文字（joystick 叠层、网格标签）保留原文。
- 式 3 中相机短语示例 "Camera moves forward. Camera yaws right." 按原文保留不译。
- 无其他跳过内容：本文无附录、无表格、无补充材料。

## If a stricter edition is needed

若需逐句、逐脚注的法证式逐字版，可基于 scratchpad 的 `paper_full_text.md`（含原始行流）与本 `source_map.json` 的 S/F 块映射增补：主要工作量在 (1) 把语义段落组还原为 PDF 原始段落切分；(2) 公式逐符号与 PDF 原页比对（尤其式 3–4 的维度标注与式 7 的期望下标）；(3) References 逐条转写。本版优先保证全文章节覆盖、公式可渲染、图表语义邻近与可读的中英对照。
