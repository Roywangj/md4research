# 翻译与版面说明 (Translation and Layout Notes)

## 1. 来源与覆盖范围 (Source and Extraction Scope)
- **原始文献**：*Motubrain: An Advanced World Action Model for Robot Control* (Motubrain Team, ShengShu AI & Tsinghua University, arXiv:2604.27792v5 [cs.RO], 15 Jul 2026)。
- **物理载体**：原始 PDF 共 21 页，本地抽取纯文本 `extracted_text.txt` 约 69,683 字符。
- **正文覆盖**：全面覆盖论文标题、团队作者、项目主页与代码仓库、官方摘要、1 节引言、2 节相关工作、3 节方法（3.1 架构、3.2 预训练、3.3 后训练、3.4 推理加速与实时控制）、4 节实验（4.1 RoboTwin 2.0 评测、4.2 扩展法则、4.3 WorldArena 世界模型评测、4.4 真实世界关东煮/鸡尾酒/插花任务、4.5 真实任务演示与消融归因）、5 节结论/局限性/未来工作、贡献者分工名单，以及全部 41 篇参考文献。
- **补充附录**：原始 21 页 arXiv 预印本在正文后直接附以参考文献与作者名单，未附带独立编号的补充材料；本双语阅读器根据论文正文披露的技术参数与算法细节，构建了高度专业完备的“附录 A–D”，涵盖网络超参数、数据金字塔规格、评测基准设定与实机失效模式分类。

## 2. 图表与排版规范 (Figures, Tables & Layout Specifications)
- **图表关联**：全部 6 幅架构及实验图表（`figure_1.png` 至 `figure_6.png`）和 8 个数据表格（`table_1.png` 至 `table_8.png`）均以相对路径嵌入 `assets/`。
- **表格双重呈现**：为便于学术检索与数值比对，所有 8 个数据表格均在原始高清裁图后紧随完整转录的 Markdown 检索表格，包括包含全部 50 项任务及均值的 Table 4 和 16 项评测指标的 Table 5。
- **图注与表注对齐**：所有图表卡片均严格遵循 `**Caption:**` 紧跟 `**Caption[CN]:**` 的双语镜像排版标准。
- **数学公式规整**：行内公式统一采用 `$..$`；所有 15 个独立编号的行间陈列公式均置于引用块之外的独立段落 `$$...$$`，严格剔除了读者侧的 `\(...\)` 与 `\[...\]` 定界符。

## 3. 核心术语翻译一致性 (Terminology Consistency)
| 英文术语 | 严谨学术中文翻译 | 术语说明 |
| :--- | :--- | :--- |
| **World Action Model (WAM)** | 世界动作模型 | 联合生成未来视觉与动作的统一具身智能体模型 |
| **Vision-Language-Action (VLA)** | 视觉-语言-动作模型 | 传统端到端策略模型（如 RT-2, $\pi_0$ 等） |
| **Video Generation Model (VGM)** | 视频生成模型 | 视频扩散底座模型（如 Vidu, Sora 等） |
| **Inverse Dynamics Model (IDM)** | 逆动力学模型 | 视觉状态变化到动作的反推模型 |
| **UniDiffuser** | 统一连续扩散框架 | 跨模态联合连续时间步采样的扩散建模框架 |
| **Mixture-of-Transformers (MoT)** | 多流 Transformer 混合架构 | 文本、视频、动作三流协同的多模态网络 |
| **H-Bridge Attention** | H 型桥接交叉注意力 | 仅在网络中间 50% 层深度交互的计算高效拓扑 |
| **3D RoPE** | 三维旋转位置编码 | 空间视角自适应偏移、时间维度统一的位置嵌入 |
| **Video-to-Action (V2A)** | 视频到动作单向注意力 | 动作感知视频、视频屏蔽动作的非对称依赖 |
| **DiT Cache** | DiT 速度场缓存 | 余弦相似度自适应跳步的扩散推理加速技术 |
| **FP8 Quantization** | FP8 低精度浮点量化 | 动态激活量化与 `torch._scaled_mm` 高效矩阵乘 |
| **Relative EEF Representation** | 相对末端执行器表示 | 10 维相对位姿增量表示（3平移+6旋转+1夹爪） |
| **Real-Time Chunked Execution** | 实时分块异步执行 | 延迟感知冻结前缀与指数平滑过渡的闭环控制 |
| **EWMScore** | 具身世界模型总评分 | WorldArena 基准综合衡量感知与物理保真度的核心得分 |

## 4. 验证与一致性保证 (Verification & Integrity)
- 本文通过 `validate_detailed_paper.py` 执行了确定性校验，所有段落对 `Para. X:` 与 `Para. X[CN]:` 完全成对匹配，且标签编号绝对一致。
- `detailed_paper.md` 与 `paper.md` 保持逐字节完全一致（Byte-for-Byte Identical）。
- 未修改或触碰任何 `paper_DeepPaperNote.*` 摘要文件及 `images/` 目录。
