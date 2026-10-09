# Translation and Extraction Notes: DM0.5

## 1. Extraction Scope and Document Nature (提取范围与文献性质)

- **文献性质说明：** 本文档源自原力灵机（Dexmal / 重庆智能科技有限公司）于 2026 年 9 月发布的官方工业级技术白皮书与系统发布报告（Official Industrial Technical Whitepaper & System Release Report），并非传统的学术会议（如 NeurIPS / CVPR / CoRL）或期刊投稿论文，但具备完整的系统架构定义、数学对齐机制、数据清洗规范以及严谨的多基准实验评估。
- **覆盖完整性：** 全文所有章节内容均已 100% 完整提取并实现逐段中英双语对齐，无任何实质性段落、图表或数据遗漏。
- **主从交付约定：** `detailed_paper.md` 为本项工作的权威主交付物；`paper.md` 按规范保持为 `detailed_paper.md` 的字节级完全相同副本（Exact Byte-for-Byte Copy）。分析性述评置于文末专属后记章节，没有篡改原文段落。

## 2. Source Material and Version Control (源材料与版本控制)

- **原始网页快照：** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/VUPCWDUX/www.dexmal.com.html`
- **本地提取文本：** `extracted_text.txt`（位于当前论文工作目录）
- **本地多模态资产：** `assets/image_01.png` ~ `image_10.png` 共 10 个图像资产，全部验证有效并建立相对链接。
- **辅助数据保护：** 严格遵循用户指令，未触碰或覆盖 `images/` 目录下的精读笔记专属素材，亦未修改 `paper_DeepPaperNote.md`。

## 3. Structural and Linguistic Standards (排版与双语对齐规范)

- **段落配对规范：** 遵循 `nature-reader-detail` 标准，使用高对比度 Markdown 块引用：
  - 英文原段：`> <span style="color:#3B82F6"><strong>Para. X:</strong></span> English text...`
  - 中文学术译文：`> <span style="color:#F59E0B"><strong>Para. X[CN]:</strong></span> 严谨中文翻译...`
  - 全文共 59 对严格一一对应的双语段落，编号从 1 至 59 连续编排，无断号或错位。
- **数学公式排版：**
  - 行内公式统一采用 `$inline$` 格式；
  - 独立显示公式统一采用 `$$...$$` 置于独立行，且严格置于块引用（`>`）外部，严禁任何 `\(...\)` 或 `\[...\]` 语法。
- **图表卡片标准：**
  - 全文包含 10 个图像卡片，覆盖官方标识、全景概念图、系统架构图、Table 1/2 裁图、多机位构型图以及生态渠道图；
  - 每个图像均紧跟 `**Caption:**` 与 `**Caption[CN]:**` 双语说明；
  - Table 1 与 Table 2 图像后紧跟转录的完整 Markdown 表格；
  - Table 3（LIBERO）、Table 4（RoboTwin2.0）、Table 5（R2R/RxR 导航）、Table 6（多机位成功率矩阵）均在对应章节以清晰的 Markdown 表格呈现，保证数值可检索、可计算。

## 4. Key Terminology Conventions (关键专业术语规范)

1. **VLA (Vision-Language-Action):** 统一译为“视觉—语言—动作模型”，指将多模态视觉感知、语言指令与机器人底层动作闭环统一的具身大模型。
2. **Action Expert:** 统一译为“动作专家”，专指负责高频去噪并解码输出连续动作序列的高性能网络分支（680M）。
3. **Context Abstraction Layer:** 统一译为“上下文抽象层”，指对最长 60 秒的历史时序观测进行采样与词元压缩、构建工作记忆的模块。
4. **Embodiment CoT Tasks:** 统一译为“具身思维链任务”，指在机器人示教数据中强化的 11 项自回归多任务推理链。
5. **Trajectory Alignment Layer / Dynamic Action Matching:** 统一译为“轨迹对齐层 / 动态动作匹配”，指通过动态规划与单调性约束对齐预测轨迹与示教轨迹的非刚性对齐技术。
6. **Flow Matching:** 统一译为“流匹配”，保留为学界通用的连续时间生成模型术语。
7. **Action Chunking:** 统一译为“动作块生成”，指单次推理输出一段未来动作序列（50步）的时空控制机制。
8. **RoboChallenge Table30 v2 / LIBERO / RoboTwin2.0 / R2R / RxR:** 均保留原版英文基准名称。

## 5. Technical Caveats and Context (技术局限与背景说明)

- **工业发布性质与参数披露：** 该白皮书展示了 DM0.5 极其强大的综合性能（Table30 v2 达 43% 成功率，仿真基准全面 SOTA），但作为商业公司技术发布，未开源完整的底层训练超参数（如动态规划匹配损失权重 $\lambda$、各模态混合比例等细节）。
- **动作原语数值精度：** Table 1 与 Table 2 为基于图像柱状图（`image_04.png`, `image_05.png`）的像素级测量与物理标尺归一化转录（每 25% 对应 36 像素，100% 对应 144 像素高度），已精确至 0.1% 的精度。
- **真机双臂平台：** 报告中的真机实验基于自研的 Dexmal-Mirror 平台（双臂移动机器人）及 Franka 单臂平台进行，涵盖单臂、双臂、移动操作的多构型验证。

## 6. Deterministic Validation Audit (确定性校验结果)

- **校验脚本：** `/Users/roywangj/Desktop/skills4ai/wj_skills/nature-reader-detail-wj/scripts/validate_detailed_paper.py`
- **校验参数：** `--source paper.md --require-identical`
- **校验结论：** 59 对双语段落严格平衡，10 对双语图注完整闭环，10 个本地图片链接全部可达（0 个断链），`paper.md` 与 `detailed_paper.md` 哈希完全一致（passes: True，0 errors）。
