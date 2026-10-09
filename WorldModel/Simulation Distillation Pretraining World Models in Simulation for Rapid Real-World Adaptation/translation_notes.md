# Translation Notes

## Scope

- 已处理完整 16 页 PDF（arXiv:2603.15759v2），正文（Abstract、I–VI）、Acknowledgments、References 索引与 Appendix A–D 全部纳入 `paper.md`。
- `paper.md` 采用"版面修复后的语义段落组"做中英对照：双栏断行、图注穿插、公式碎片已清理，不是对 PDF 原始行流的逐行复制。第 IV、V 节的短小带标题小段（如 Expert Policy Training、Chunked Prediction）按主题合并为段落对，未改变论述顺序。
- 第 10–13 页共 59 条 bibliography 保留在源 PDF，不逐条翻译；正文相关技术谱系已在 References 索引段说明。
- Algorithm 1 与 Algorithm 2 未作为图片插入（自动裁切为 1700×200 的贴条状碎片，质量被判定 reject）；两个算法的完整流程已在 IV-A Para. 4 与 Appendix A Para. 1 中以双语正文忠实转述，无信息丢失。

## Source

- Source path: `/root/wwwroy/papernotes/papers/Levy 等 - 2026 - Simulation Distillation Pretraining World Models in Simulation for Rapid Real-World Adaptation.pdf`
- Source type: selectable-text PDF (`pdf-text`)
- Pages: 16；PDF sha256: `9c846f2c1c3433969a556d99e9c27acbdc8c649e45a2a9527d49d8739fadff7d`
- arXiv: 2603.15759 (v2, 12 May 2026)，RSS 双栏模板
- Canonical extraction（本会话独立跑的一份，不与精读 agent 的 workdir 共享）: `/tmp/claude-0/-root-wwwroy-papernotes/fbcd5d0c-d98e-409d-8a49-a3bbe90bb6f3/scratchpad/simdistill_tr/paper_raw_sections.jsonl`、`paper_full_text.md`

## Extraction and layout issues

- 双栏版式导致自动 section detector 产生大量伪 section（Fig. 2 流程图的文字块被切成十几个 "Model/Data" 小节）；`paper.md` 已按真实标题（I–VI、Appendix A–D）恢复章节顺序。
- 数学文本层把上下标拆成相邻字符。式 (1)–(3)、MPPI 回报式、Appendix A 的噪声采样式均已按语义重建为 `$...$` / `$$...$$`。
- 式 (2) 的求和上界在文本层丢失（只剩 `i=0`）；参照式 (3) 提取到的 `\sum_{i=0}^{T}` 统一写作上界 $T$。如需引用逐项精确形式请核对原 PDF 第 5–6 页。
- Appendix 的 Table II、III、VII、VIII（结构/MPPI 超参数表）在文本层里"参数名与数值列错位"，多数数值行丢失；正文段落已保留文本层尚存的数值（初始/最小动作标准差、temperature、momentum、discount 等），其余数值列未转写，段内已标注"请对照原 PDF"。
- Table IV–VI、X 的行列在文本层同样错位，未逐格转写；其关键内容（域随机化范围、reward 权重、观测维度、1080 个消融环境的参数组合）已在 Appendix C/D 的段落翻译中覆盖。

## Assets and crop caveats

- `assets/` 共 13 张：11 张 Figure（Fig. 1–11 全部收录）+ 2 张 Table（Table I、Table IX），均在 `paper.md` 有对应图表块。
- Fig. 5、Fig. 7、Table I、Table IX 为自制裁切（PyMuPDF 220 dpi 直接按版面矩形裁取）：pipeline 的 Fig. 5 候选实际是"Fig. 5 图注 + Fig. 6 图体"的错误组合，Fig. 7 候选混入了 Fig. 5 的曲线图；自制裁切已逐张目检确认图体、编号与图注一致。
- Fig. 1 裁切包含首页作者区，但图体、任务标签与原始图注完整，为保留总览信息未再裁窄。
- Table I 数值同时转写进了 caption（图片 + 文本双保险）；Table IX 因列数过多只以图片呈现，关键结论（SimDist 各速度 4/5–5/5、RLPD Foam 失稳未报）在 Appendix C Para. 6 的译文中给出。

## Terminology

- 固定使用 SimDist、world model、MPPI、TD-MPC、RLPD、IQL、SGFT、Diffusion Policy、$\pi_{0.5}$、PPO、IsaacLab、UR5e、Unitree Go2、ResNet-18 等英文名。
- `system identification` 译"系统辨识"；`privileged state` 译"特权状态"；`catastrophic forgetting` 译"灾难性遗忘"；`credit assignment` 译"信用分配"；`proprioceptive/exteroceptive` 译"本体感知/外感知"。
- `bootstrap/bootstrapping` 依上下文译"引导/自举"并在首次出现处保留英文；`play data`、`rollout`、`checkpoint`、`off-policy`、`warm-start` 保留英文。
- 完整对照见 `paper.md` 的 Terminology Ledger 与 `source_map.json` 的 glossary（15 条）。

## Untranslated or skipped material

- bibliography 条目（59 条）未逐条翻译。
- 作者列表、机构、项目网址、资助编号保留原文。
- Appendix 超参数表（Table II–VIII、X）未逐格转写，原因见上；正文提供协议级双语解读。

## If a stricter edition is needed

若需逐句、逐脚注、逐表格单元格的法证式版本，可基于会话 workdir 的 `paper_full_text.md` 与 `source_map.json` 的 page/block 映射增补，并用 PyMuPDF 对第 13–16 页各表逐格重取数值。本版优先保证全文段落级双语覆盖、公式语义重建与图表在首次讨论处的邻近放置。
