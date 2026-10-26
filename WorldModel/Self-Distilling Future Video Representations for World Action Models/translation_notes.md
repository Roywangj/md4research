# Translation Notes | 翻译与提取说明

## 1. 范围与源文件 (Scope & Source)
- **论文题目**: Self-Distilling Future Video Representations for World Action Models
- **中文译名**: 面向世界动作模型的未来视频表征自蒸馏学习
- **作者**: Huiwon Jang, Suhyeok Jang, Hyeonmo Kang, Seungku Kim, Jinwoo Shin, Sihyun Yu (KAIST & RLWRLD)
- **发布时间**: 2026-10-21 (arXiv:2610.30320v1)
- **源 PDF 路径**: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/WX7RFZP9/Jang 等 - 2026 - Self-Distilling Future Video Representations for World Action Models.pdf`
- **源文件格式**: 可选文本 PDF (`pdf-text`)，共 27 页（正文 11 页，参考文献 3 页，附录 13 页）。
- **翻译覆盖范围**: 包含标题元数据、摘要、第 1~5 节全文正文、参考文献目录、附录 A~H 全量详细技术细节与全套基准评测表格，达到 100% 完整覆盖。

## 2. 图像与表格资产提取说明 (Assets Extraction)
- 使用 `PyMuPDF` (`fitz`) 结合高精度页面坐标计算与 `Matrix(zoom=3.4722)`（250 dpi）对 PDF 中的全部 10 个 Figure 与 13 个 Table 进行严密裁切。
- 裁切时精准排除了跨页页脚页码与非相关正文段落，保持矢量线条、刻度标签、表格边框与图注完整清晰。
- 资产同步输出至 `assets/`（供双语读者 `paper.md` / `detailed_paper.md` 使用）与 `images/`（供精读笔记 `paper_DeepPaperNote.md` 使用），并建立标准规范命名与别名。
- 提取清单：
  - `page_004_fig_1.png` (`figure_1.png`): 训练期间 VDM 未来表征探测准确率与 CKNNA 结构相似度变化曲线。
  - `page_005_fig_2.png` (`figure_2.png`): FRED 架构总览图（Student/Teacher 动量自蒸馏、时序上下文与动作解码器）。
  - `page_007_fig_3.png` (`figure_3.png`): DROID 实机零样本泛化评测与 OpenArm 人机协同训练场景。
  - `page_007_tab_1.png` (`table_1.png`): 真实世界新环境零样本泛化主表（DROID，Franka Research 3）。
  - `page_008_tab_2.png` (`table_2.png`): OpenArm 人形双臂机器人域内与人类技能迁移主表。
  - `page_009_tab_3.png` (`table_3.png`): FRED 核心组件消融实验表（自蒸馏与时序上下文）。
  - `page_009_tab_4.png` (`table_4.png`): 仿真基准上多种表征学习方法对比表。
  - `page_010_fig_4.png` (`figure_4.png`): 策略控制性能 vs 视频像素生成质量 (FVD) 与潜在表征探测质量对比散点图。
  - `page_010_tab_5.png` (`table_5.png`): FRED 架构设计选择分析表（教师噪声、特征层、损失权重、动作梯度阻断）。
  - `page_011_tab_6.png` (`table_6.png`): 视频骨干网络泛化性表（Wan2.2-5B 与 Cosmos-Predict2.5-2B）。
  - `page_011_tab_7.png` (`table_7.png`): 推理时延与硬件开销对比表（A100 GPU）。
  - `page_015_tab_8.png` (`table_8.png`): 真实世界实验超参数全表。
  - `page_016_tab_9.png` (`table_9.png`): PyTorch 风格图像数据增强策略表。
  - `page_017_fig_5.png` (`figure_5.png`): DROID 硬件评测台架（Franka 机械臂、Robotiq 夹爪、外置双摄）。
  - `page_018_fig_6.png` (`figure_6.png`): DROID 四大任务套件实物场景可视化。
  - `page_019_fig_7.png` (`figure_7.png`): OpenArm 人形双臂硬件平台实物图。
  - `page_020_fig_8.png` (`figure_8.png`): OpenArm 机器人演示数据集技能与物体分布。
  - `page_020_fig_9.png` (`figure_9.png`): 人类自我中心视频数据集技能与物体分布。
  - `page_021_fig_10.png` (`figure_10.png`): OpenArm 7 项评测任务操作轨迹展示。
  - `page_023_tab_10.png` (`table_10.png`): 验证集 9 类运动原语分布表。
  - `page_025_tab_11.png` (`table_11.png`): DROID 零样本环境泛化单任务细分成功率表。
  - `page_026_tab_12.png` (`table_12.png`): OpenArm 人形机器人控制单任务细分成功率与指令遵循率表。
  - `page_027_tab_13.png` (`table_13.png`): RoboCasa Kitchen 基准与前沿具身基线对比表。

## 3. 术语对照决策 (Terminology Ledger Decisions)
- **World Action Models (WAMs)**: 世界动作模型。严格保留英文缩写 WAMs，指代联合建模未来物理演化与底层机器人动作的生成式策略体系。
- **Video Diffusion Models (VDMs)**: 视频扩散模型。指代 Wan2.1/2.2、Cosmos 等大规模预训练视频主干网络。
- **Future REpresentation learning via self-Distillation with temporal context (FRED)**: 基于时序上下文自蒸馏的未来表征学习框架。保留专有名词 FRED。
- **Flow Matching (FM)**: 流匹配。在论文中用于视频速度场去噪与动作生成。
- **Self-Distillation**: 自蒸馏。特指 Student 模型从纯高斯噪声生成的潜在特征与 Teacher 模型从中等加噪/干净真实未来提取的特征对齐。
- **EMA Teacher**: 指数移动平均动量教师网络。
- **Attentive Probe**: 注意力探测器。用于探查隐层特征对未来运动方向的预测能力。
- **Centered Kernel Non-alignment (CKNNA)**: 中心化核非对齐度。表征空间几何距离度量（基于 CKA 导出）。
- **Action Chunking**: 动作分块 / 动作块预测。
- **Stop-gradient**: 梯度阻断 / 截断。论文的核心发现之一：阻断从动作损失到视频主干的梯度有助于保护通用时空表征。
- **Zero-shot Environment Generalization**: 零样本环境泛化。在未见过的物理新台架、新背景与新物体上直接部署。
- **Human-to-robot Skill Transfer**: 人类到机器人的技能迁移。利用无动作的人类第一视角视频迁移操作先验。

## 4. 数学公式与排版规范 (Mathematical Hygiene)
- PDF 原始文本中包含大量连字符截断（如 `self-distillation`, `representation`），在提取时均已完全修复。
- 原文中的内嵌公式与希腊字母全部转换为严格的 LaTeX 格式：`$...$` 与 `$$...$$`，严禁遗留任何 `\(...\)` 或 `\[...\]`。
- 保持所有段落标签严格遵循 `Para. X:` 与 `Para. X[CN]:`，严禁使用 `**Original:**` 或 `**中文:**`。
