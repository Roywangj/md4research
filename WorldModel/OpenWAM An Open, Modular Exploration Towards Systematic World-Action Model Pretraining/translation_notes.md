# Translation Notes: OpenWAM

## 1. Extraction Scope and Document Inventory

- **Document:** *OpenWAM: An Open, Modular Exploration Towards Systematic World–Action Model Pretraining* (Yuran Wang et al., NUS / Tsinghua / PKU / HKU / ZJU / CUHK / SJTU, 2026).
- **Canonical Version:** `arXiv:2609.07398v1` [cs.RO], 7 Sep 2026, 43 pages.
- **Canonical PDF:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/6IMBVEAT/Wang 等 - 2026 - OpenWAM An Open, Modular Exploration Towards Systematic World-Action Model Pretraining.pdf`.
- **SHA-256 Digest:** `09606aafdd27a377b669331c2d11ad87c11dbba31066689c8d48d9fd2f28151b`.
- **Scope Covered:** 完整覆盖源 PDF 全部 43 页内容，包含：
  - Frontmatter、标题、作者单位列表、王阳明《传习录》开篇题记；
  - 摘要（Abstract）与第 1 节引言（三大科学问题与核心贡献）；
  - 第 2 节相关工作（世界动作模型、通用机器人策略开源生态、架构设计的实证科学方法论）；
  - 第 3 节 OpenWAM-Infra（3.1 模块化可组合模型与流抽象、公式 (1)–(2)；3.2 训练运行时；3.3 部署运行时、去噪调度公式 (3)、Serving 加速栈；3.4 评估协议与 80 维统一动作空间公式 (4)）；
  - 第 4 节 OpenWAM-Study（4.1 上游世界知识继承、主干规模消融、视觉表征先验消融；4.2 世界与动作协同机制、网络容量消融、注意力掩码信息流消融、去噪调度消融；4.3 跨域知识整合与具身预训练；4.4 经验准则总结）；
  - 第 5 节 OpenWAM-α（5.1 架构、优化与部署；5.2 6,400 小时异构预训练数据集构建与工业级清洗；5.3 涵盖 8 大仿真基准的全面对比与 LIBERO-Plus 特例分析；5.4 单臂、RoboDojo 双臂与无极-天机多指灵巧手真实物理机器人评测）；
  - 第 6 节结论与社区开源声明；
  - 参考文献：完整收录全部 108 条英文原始文献题录 [1]–[108]；
  - 附录 A：局限性与未来研究方向（训练阶段、架构演进、数据源配比、视觉编码器归纳偏置）；
  - 附录 B：训练细节（B.1 预训练全局超参数表 9；B.2 下游特定任务 SFT 微调超参数表 10）；
  - 附录 C：真实物理机器人评测协议（C.1 Franka-Research-3 单臂 6 项任务；C.2 无极灵巧手与天机臂 4 项高难度操控任务、评测指标数学定义与具体判定准则；C.3 RoboDojo 实体双臂 3 大平台 18 项任务协议）；
  - 附录 D：各仿真基准详尽分项得分（表 13 至表 20，包含 LIBERO, VLABench, RoboTwin2.0-Clean2Random, RoboTwin2.0-Full, RoboDojo, EBench, RoboCasa365, RoboCasa-GR1）。

## 2. Deliverables and Byte Parity

- **`detailed_paper.md`:** 完整段落级中英双语对齐精读稿，采用规范的 Markdown 块引用排版：
  ```markdown
  > <span style="color:#3B82F6"><strong>Para. X:</strong></span> English text...
  >
  > <span style="color:#F59E0B"><strong>Para. X[CN]:</strong></span> 严谨专业学术中文翻译...
  ```
  共计 94 组段落对（包含正文、摘要与附录全部叙述段落），零孤立段落，全部数字、符号、缩写与引用严格保持一致。
- **`paper.md`:** `detailed_paper.md` 的逐字节严格复制本（byte-identical copy），经 SHA-256 校验哈希值为 `4f82f589ee80c67476f29bddd0845089e91a8ff11d8cb892e4c02afcea5938bd`，通过官方脚本 `--require-identical` 严苛验证。
- **`source_map.json`:** 符合规范的结构化资产映射文件，记录了论文元数据、附件 SHA-256、各章节分页索引与 41 项图表资产映射。
- **`translation_notes.md`:** 本文件，记录翻译规范、排版约定、图表转录与技术细节边界。

## 3. Visual Assets and Table Transcription

- **图表完整性:** 全部 41 项视觉资产（21 张高清图片 `figure_1.png`–`figure_21.png`，20 张高精表格截图 `table_1.png`–`table_20.png`）均来自 `assets/` 目录，无任何坏链。
- **图片卡片规范:** 每张图片均紧随完整的英文图注（`**Caption:**`）与精准学术中文图注（`**Caption[CN]:**`）。
- **表格双轨呈现:** 全部 20 张表格在插入相对路径截图后，均在图片下方完整转录为原汁原味的 Markdown 表格，并紧随中英文图注；表中所有关键最优数值（粗体）与次优数值（下划线）严格核对并忠实转录。

## 4. Mathematical Typesetting Policy

- 严格遵循 `$...$`（行内公式）与 `$$...$$`（独立行间公式）排版标准。
- 绝不在 blockquote（`>`）引用行内使用 `$$` 标记（避免触发渲染错误与校验告警）。
- 绝不遗留任何 `\(`、`\)`、`\[` 或 `\]` LaTeX 渲染分隔符。
- 重点数学符号严格对齐：
  - 公式 (1)：可见性注意力掩码块矩阵 $\mathbf{M} = \begin{pmatrix} \mathbf{M}_{V \leftarrow V} & \mathbf{M}_{V \leftarrow A} \\ \mathbf{M}_{A \leftarrow V} & \mathbf{M}_{A \leftarrow A} \end{pmatrix}$
  - 公式 (2)：联合流匹配损失函数 $\mathcal{L} = \lambda_v \mathbb{E}_{t_v, \epsilon_v} [ w(t_v) \|\hat{v}_z - (z - \epsilon_v)\|_2^2 ] + \lambda_a \mathbb{E}_{t_a, \epsilon_a} [ w(t_a) \|\mathbf{m} \odot (\hat{v}_a - (a - \epsilon_a))\|_2^2 ]$
  - 公式 (3)：去噪调度函数族 $f_\alpha(s) = \frac{\alpha s}{1 + (\alpha - 1)s}, \quad h_o(s) = \max\left\{ \frac{s - o}{1 - o}, 0 \right\}$
  - 公式 (4)：80 维统一动作空间离散投射与聚合 $\mathbf{u} = \mathrm{Scatter}_\pi(\mathrm{Norm}(\mathbf{a})), \quad \mathbf{a} = \mathrm{Norm}^{-1}(\mathrm{Gather}_\pi(\mathbf{u}))$
  - 附录 C.2：最终成功率与进度得分定义公式。

## 5. Terminology and Academic Translation Standards

- **模型范式名:** World–Action Model (WAM) 统一译为“世界—动作模型（WAM）”；Vision–Language–Action (VLA) 统一译为“视觉—语言—动作模型（VLA）”。
- **生成模型术语:** Flow Matching 译为“流匹配”；Diffusion Transformer 译为“扩散 Transformer（DiT）”；Denoising Schedule 译为“去噪调度”；Variance Shift 译为“方差偏移”；Linear Offset 译为“线性偏置”；DiT Velocity Cache 译为“DiT 速度场缓存”。
- **架构流向术语:** Stream 译为“流”；Visibility Attention Mask 译为“可见性注意力掩码”；Mutual 译为“双向相互可见”；Action Sees Video 译为“动作可见视频”；Video Sees Action 译为“视频可见动作”；Isolated 译为“隔离模式”。
- **具身与控制术语:** Action Chunk 译为“动作块”；Proprioception / Proprioceptive State 译为“本体感受状态”；Unified Action Space 译为“统一动作空间”；In-Distribution (ID) / Out-of-Distribution (OOD) 统一译为“分布内（ID）/ 分布外（OOD）”。
- **编码器术语:** Reconstructive Encoder 译为“重构式编码器”；Representation Encoder 译为“表征式编码器”；Dimension Contraction 译为“维度收缩”；Temporal Compression 译为“时间压缩”。

## 6. Verification and Validation Outcome

使用官方校验脚本执行严格验证：
```bash
python3 /Users/roywangj/Desktop/skills4ai/wj_skills/nature-reader-detail-wj/scripts/validate_detailed_paper.py \
  "/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/OpenWAM An Open, Modular Exploration Towards Systematic World-Action Model Pretraining/detailed_paper.md" \
  --source "/Users/roywangj/journey_wj/research/mds4zotero/markdowns4zotero/WorldModel/OpenWAM An Open, Modular Exploration Towards Systematic World-Action Model Pretraining/paper.md" \
  --require-identical
```
- **Validation Results:**
  - `bytes`: 234,519
  - `bilingual paragraph pairs`: 94
  - `caption pairs`: 41 original / 41 Chinese (21 figures, 20 tables)
  - `image links`: 41 (missing: 0)
  - `errors`: 0
  - `passes`: **True**
- **Boundary Verification:** 严格保护同目录下的 `paper_DeepPaperNote.md`、`paper_DeepPaperNote.*.json` 以及 `images/`，未做任何修改或覆写。
