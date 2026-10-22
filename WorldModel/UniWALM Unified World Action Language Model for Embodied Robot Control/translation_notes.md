# Translation Notes / 翻译笔记

## Scope / 覆盖范围

Full 25-page source PDF (`Sajnani 等 - 2026 - UniWALM Unified World Action Language Model for Embodied Robot Control.pdf`, arXiv:2610.28626v1) was thoroughly inspected and translated into `detailed_paper.md` as adjacent English/Chinese paragraph pairs (`Para. X:` / `Para. X[CN]:`). The companion analytical file `paper_DeepPaperNote.md` is an independent WJ note and was strictly preserved untouched without modification.

## Source and Extraction / 数据来源与文本提取

- **Source Type:** Selectable-text, two-column academic paper PDF; 25 pages in total.
- **Extraction Protocol:** Cross-validated between `extracted_text.txt` and raw PDF parsing, verifying page breaks, multi-column reading flow, and mathematical expressions.
- **Sections Covered:**
  - Frontmatter, Index, Terminology Ledger, Title, Authors, Abstract
  - 1 Introduction (Paragraphs 1–7 + Figure 1)
  - 2 Related Works (Paragraphs 1–5)
  - 3 UniWALM Architecture & Methodology:
    - 3.1 Reasoning with Video Action Models (Paragraphs 1–4 + Figure 2 + Figure 4)
    - 3.2 Multi-Modal Co-Training (Paragraphs 1–2 + Loss Equations)
    - 3.3 Memory Mechanisms (Paragraphs 1–5: Textual Memory, Visual Anchor Frame, 1-D Task Completion $\beta$)
    - 3.4 Flow Matching with Correction (FMC) (Paragraphs 1–6 + Figure 3 + Equations & Algorithm 1)
    - 3.5 Architecture and Training Details (Paragraphs 1–4)
  - 4 Experiments:
    - 4.1 Benchmarks and Setup (Paragraphs 1–4: MolmoSpaces, RMBench M(n), Real-World Dual-Arm Flexiv)
    - 4.2 Main Results: Q1 Manipulation & Q2 Working Memory (Paragraphs 1–3 + Tables 1, 2, 3 + Figures 5, 6, 7)
    - 4.3 Ablations: Manipulation & Memory (Paragraphs 1–3 + Tables 4, 5)
  - 5 Limitations (Paragraph 1)
  - 6 Conclusion & Future Work (Paragraphs 1–3)
  - References [1]–[58] (58 complete entries in searchable bibliographic form)
  - Appendix Contents (Paragraph 1)
  - Appendix A: Related Works Extended Discussion (Paragraphs 1–4)
  - Appendix B: Additional Experimental Details:
    - B.1 Qualitative Results (Paragraph 1 + Figure 8)
    - B.2 RMBench Environment and Tasks (Paragraphs 1–5 + Figure 9)
    - B.3 RMBench Training Configuration (Paragraph 1)
    - B.4 Memory Architecture Details (Paragraphs 1–2)
    - B.5 FMC 2D Robot Trajectory Ablations (Paragraphs 1–3 + Figure 10, Figure 11 + Table 6)
    - B.6 Failure Case: Press Button Timing Lag (Paragraph 1 + Figure 12)
  - Appendix C: Limitations Extended (Paragraph 1)
  - Appendix D: Additional Future Work (Paragraphs 1–8: 7 detailed future research directions)
  - Appendix E: Additional Rollout Visualizations (Paragraph 1 + Figure 13, Figure 14)

## Assets and Tables / 资源与表格处理

- **Figures (1–14):** All 14 figures from `assets/figure_1.png` to `assets/figure_14.png` are properly embedded with relative links, each followed by original English and rigorous academic Chinese captions (`**Caption:**` and `**Caption[CN]:**`).
- **Tables (1–6):** All 6 tables (`assets/table_1.png` to `assets/table_6.png`) are accompanied by high-quality transcribed Markdown tables placed directly between the image link and the captions, preserving all numerical metrics, confidence intervals, sample counts, and bold best values.

## Fidelity and Terminology / 保真度与术语一致性

1. **Mathematical Notation:** Preserved exact mathematical operators, dimensions, and definitions: action chunk $N=32$, video horizon $H=5$, diffusion time $t \in [0, 1]$, flow correction target $v_{\text{corr}} = (\epsilon - x_0) + \frac{1-t}{\Delta t}\epsilon_1$, LoRA rank 256, etc. Display math formulas are formatted outside blockquotes as `$$...$$` with inline math as `$...$`.
2. **Terminology Consistency:** Standardized across all sections:
   - World Action Language Model (WALM) $\rightarrow$ 世界-动作-语言模型
   - Mixture of Transformers (MoT) $\rightarrow$ Transformer 混合架构
   - Flow Matching with Correction (FMC) $\rightarrow$ 带校正的流匹配
   - Co-denoising $\rightarrow$ 同步联合去噪 / 协同去噪
   - Language-as-Memory $\rightarrow$ 语言即记忆
   - Textual Memory / Visual Memory (Anchor Frame) $\rightarrow$ 文本记忆 / 视觉记忆（初始锚点帧）
   - Task-Completion Signal ($\beta$) $\rightarrow$ 任务完成信号（$\beta$）
   - Action Chunking $\rightarrow$ 动作分块预测
3. **No External Fabrication:** No unstated assumptions or unsupported results were invented. All conclusions, experimental figures, and ablation data precisely reflect the author's primary text.
