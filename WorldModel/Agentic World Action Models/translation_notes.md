# Translation Notes: Agentic World Action Models (AW-0)

## Scope
The full 50-page source manuscript (*Agentic World Action Models*, arXiv:2610.30136v1 [cs.RO], 21 Oct 2026, by Zhuoyang Liu, Dantong Niu, Botong Zhang, Boning Shao, Jing Wang, Ruijie Zheng, Yuvan Sharma, Runyu Lu, Jiaming Liu, Renrui Zhang, Roei Herzig, Yutong Bai, Ken Goldberg, Danfei Xu, Yuke Zhu, Guanzhi Wang, Linxi "Jim" Fan, and Trevor Darrell) was thoroughly inspected, translated, and structured into `detailed_paper.md` as an exhaustive paragraph-by-paragraph Chinese-English bilingual reader.

The companion `paper.md` is an exact byte-for-byte replica of `detailed_paper.md` (sharing identical SHA-256 hash), strictly satisfying the nature-reader contract. Sibling analytical files such as `paper_DeepPaperNote.md`, `paper_DeepPaperNote.*.json`, and directory `images/` have been kept completely intact without modification.

## Source and Extraction Verification
- **Source PDF:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/BR3SEPJQ/Liu 等 - 2026 - Agentic World Action Models.pdf` (50 pages).
- **Text Corpus:** `extracted_text.txt` (153,096 bytes, 4,000+ lines).
- **Visual Assets:** 100 visual elements in `assets/` comprising:
  - 38 figures: `figure_1.png` to `figure_38.png`
  - 12 tables: `table_1.png` to `table_12.png`
  - 50 rendered page composites: `page_001.png` to `page_050.png`
- **Sections Fully Covered:**
  - Frontmatter, Title, Authors, Affiliations, Project Page, Abstract
  - 1 Introduction (Paragraphs 1-6)
  - 2 Agentic World Action Model (2.1 MoT Architecture, 2.2 Joint Denoising Generation, 2.3 Agentic Coding in WAM, 2.4 Training Recipe, Equations 1-6)
  - 3 Experiments (3.1 RoboTwin 2.0 Simulation, 3.2 Real-World Experiments, 3.3 Semantic Reasoning & Language Following, 3.4 Ablation Studies, Tables 1-4, Figures 4-7)
  - 4 Related Work (World Action Models & Agentic Robotics)
  - 5 Conclusion, Acknowledgments, AI Use Statement, Ethics Statement, Reproducibility Statement
  - References 1-50 in standard searchable bibliographic citation format
  - Appendix Contents (Overview of Appendices A through L)
  - Appendix A: Model and Training Details (Tables 5 & 6)
  - Appendix B: Analysis on Pretraining Dataset (Tables 7, 8, 9; Figures 8-19, including full listings of 23 YAM skills and 27 Egocentric human skills)
  - Appendix C: Baseline Implementation Details (pi0.5, DreamZero, EgoScale, WLA)
  - Appendix D: Real-world Experimental Setup (Figure 20)
  - Appendix E: Real-world Task Progress (8 tasks across YAM and Tianji-Sharpa, Figures 21-28, complete executable Python slices, frame timelines, and additive rubrics)
  - Appendix F: Analysis on Code Generation Quality (Table 10, Figures 29-32)
  - Appendix G: Additional Analysis on Real-world Results (Figures 33-35)
  - Appendix H: Failure Case Analysis (Figure 36, 6 distinct failure mode analyses)
  - Appendix I: Hybrid Actions Algorithm (Algorithms 1 & 2)
  - Appendix J: Additional Simulation Experiment Details (Table 11 with full 50-task breakdown, Table 12, Figure 37)
  - Appendix K: Agentic Annotation Details (Figure 38, declaration-only APIs, prompts, coordinator protocol)
  - Appendix L: Limitations and Future Work

## Terminology Ledger and Linguistic Precision
Key terminology has been mapped rigorously according to established academic conventions:
- *World Action Model (WAM)* -> 世界动作模型
- *Agentic World Action Model (AW-0)* -> 智能体世界动作模型
- *Mixture-of-Transformers (MoT)* -> 混合 Transformer 架构
- *Continuous Flow Matching* -> 连续流匹配
- *Discrete Masked Diffusion* -> 离散掩码扩散
- *Joint Denoising* -> 联合去噪
- *Blockwise Causal Attention* -> 分块因果注意力
- *Code-as-Policies (CaP)* -> 代码即策略
- *Skill Program / Slice* -> 技能程序 / 程序切片
- *Skill Library* -> 可复用技能库
- *Primitive APIs* -> 底层基元 API
- *Hybrid Actions / Execution* -> 混合动作执行
- *RoboTwin 2.0* -> RoboTwin 2.0 双臂协作仿真基准
- *Tianji–Sharpa Platform* -> 天机-夏尔巴双臂仿人多指灵巧手平台

## Formatting and Compliance
- Every English paragraph is wrapped in `> <span style="color:#3B82F6"><strong>Para. X:</strong></span> ...` and followed immediately by `> <span style="color:#F59E0B"><strong>Para. X[CN]:</strong></span> ...`.
- Display math formulas ($$ ... $$) are positioned outside blockquotes.
- Every figure and table is embedded with relative markdown links (`assets/figure_X.png`, `assets/table_X.png`), accompanied by balanced `**Caption:**` and `**Caption[CN]:**` pairs.
- Substantive tables (Tables 1-12) are transcribed into clean Markdown tables between the image link and the captions.
- Automated validation via `validate_detailed_paper.py --require-identical` confirms zero errors.
