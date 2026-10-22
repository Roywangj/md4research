# Translation & Extraction Notes

## Scope
- 完成论文《Rolling-WAM: World Action Models with Rolling Imagination》（arXiv:2609.30247v2, 10 页）全文段落级中英文对照精读 Reader，包括标题、作者机构、摘要、第 I 节至第 V 节正文、致谢、35 条完整参考文献，以及附录（附录 A 50 项 RoboTwin 任务评测表 VI、附录 B 超参数配置总表、附录 C 失效模式分析）。
- 正文共 70 对段落（140 个带有样式标注的 `Para. X:` / `Para. X[CN]:` 块），13 对中英文图表题注（7 幅 Figure 与 6 幅 Table），严格保持段落编号与结构对齐。
- 所有公式（式 1 至式 8 及欧拉流更新式、偏移调度式）均转写为标准 LaTeX / MathJax 格式（行内 `$...$`，独立行 `$$...$$`），独立行公式置于引用块外部。
- 所有表格（表 I、II、III、IV、V、VI）均在配图下方提供完整、可全文搜索的 Markdown 表格转录，高光最佳数据加粗标出。

## Source Information
- Source Path: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/PQDH947H/Zhou 等 - 2026 - Rolling-WAM World Action Models with Rolling Imagination.pdf`
- Extracted Full Text: `extracted_text.txt` (49,095 字符，10 页)
- Source Type: Selectable-text PDF (`pdf-text`)
- Layout: IEEE/CVPR 风格双栏排版，跨栏宽图表。
- Project Page: [https://rolling-wam.github.io/](https://rolling-wam.github.io/)

## Extraction and Layout Decisions
1. **多栏断行与跨页文本重构：** 原始 PDF 中跨行连字符断词（如 `re-planning`, `gener-ation`, `suc-cessive`）已按自然英文单词重组还原；公式与变量符号拆分已按学术排版规范对齐纠正。
2. **图表裁剪与可搜索转录：** 全部 7 幅插图（`figure_1.png` 至 `figure_7.png`）和 6 幅表格（`table_1.png` 至 `table_6.png`）均已保存在 `assets/` 目录下。针对附录中拥有 51 行、13 列超大容量的表 VI，本 Reader 完整转录了全部 50 项任务及 Average 行在 Clean 与 Randomized 两种设定下的 600 余项具体数值，确保知识库检索完全可触达。
3. **独立公式布局：** 严格遵循 Nature Reader 规范，所有独立编号公式（式 1 至 8）放置于双语引用块外部，杜绝在 blockquote 内部嵌套 `$$` 语法，确保各类 Markdown 渲染引擎的一致性。

## Terminology Decisions
- `Rolling Imagination / Rolling Denoising`: 统一译为“滚动想象 / 滚动去噪”，指在滑动窗口中维持错落噪声阶梯、随控制步推进多轮部分精细化去噪的机制。
- `Staggered Noise Levels / Schedule`: 统一译为“错落噪声水平 / 错峰噪声调度”，表示窗口内各块随未来时域延伸而递增的噪声阶梯。
- `Imminent Action Chunk`: 统一译为“即时动作块”，指窗口中首个达到完全无噪状态、即将交付物理控制器执行的动作分块。
- `Farther-future Chunks`: 统一译为“远期未来块”，指窗口中后续尚处部分加噪状态的分块。
- `Replanning Cycle / Latency`: 统一译为“重规划周期 / 闭环重规划延迟”，表示策略从新观测生成新动作的时间开销。
- `Receding-Horizon Control`: 统一译为“滚动时域控制”，强调每次仅执行预测视界起始片段并重复规划的控制范式。
- `Mixture-of-Transformers (MoT)`: 统一译为“Transformer 混合架构”，指视频 DiT 与动作专家 DiT 分立并联合注意力的架构。
- `Masked Joint Attention`: 统一译为“掩蔽联合注意力”，指动作关注视频但视频不反向关注动作的非对称设计。
- `SONIC Motion Latent`: 统一保留为“SONIC 运动隐表征”，指用于 Unitree G1 全身动作追踪与控制的 64 维隐空间向量。
- `Shifted Noise Schedule`: 统一译为“偏移噪声调度”，指 Rectified Flow 中通过参数 $\rho$ 调整信噪比的时间步重映射函数。

## Fidelity & Quality Checks
- **完整性验证：** 覆盖原论文 10 页全部实质性内容，无任何未标明的删节或简化。
- **数值与指标保真：** LIBERO 各套件得分、RoboTwin Clean/Rand 平均值、Unitree G1 各任务成功率、A100 上的延迟测试毫秒数（215 ms, 978 ms, 548 ms 等）及 4.5× 加速比全部严格核验。
- **文件一致性：** `paper.md` 与 `detailed_paper.md` 保持完全相同的字节内容（byte-for-byte identical），且通过官方 `validate_detailed_paper.py` 自动化测试脚本，报告 0 错误（`passes: True`）。
