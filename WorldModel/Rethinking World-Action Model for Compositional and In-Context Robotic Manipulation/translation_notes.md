# Translation Notes

## 1. Scope and Metadata

- **Paper Title:** Rethinking World-Action Model for Compositional and In-Context Robotic Manipulation
- **Authors:** Shukai Gong, Xuanran Zhai, Yintianrun Zhang, Ruopeng Cui, Ye Huang, Yiyang Fu, Dexuan Lyu, Chaojie Li, Xinyi Song, Peiwen Lin, Chuang Wang, Mingyuan Jia, Yufan Deng, Jiaxin Fang, Bo Liang, Jiaxin Li, Yuxiang Gao, Hao Liu, Daquan Zhou
- **Affiliations:** Peking University, AgiBot, CocoMatrix
- **arXiv ID:** 2610.02368v1 [cs.RO] 1 Oct 2026
- **Source PDF:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/C3KRZVED/Gong 等 - 2026 - Rethinking World-Action Model for Compositional and In-Context Robotic Manipulation.pdf`
- **Detected Source Format:** Selectable-text PDF (`pdf-text`), 19 pages
- **Target Deliverables:**
  - `detailed_paper.md`: Full-paper paragraph-by-paragraph English–Chinese bilingual detailed reader.
  - `paper.md`: Byte-for-byte identical copy of `detailed_paper.md`.
  - `source_map.json`: Complete structural block and asset manifest.
  - `translation_notes.md`: Translation decisions, layout recovery, notation conventions, and verification logs.
- **Workflow / Skill:** `nature-reader-detail-wj` (Mode: New Full-Paper Build).

---

## 2. Document Layout & Extraction

1. **Section Hierarchy & Alignment:**
   - The paper's core narrative factorizes long-horizon manipulation into visual subgoal planning and subgoal-guided execution.
   - All substantive sections (Title, Abstract, 1 Introduction, 2 Related Work, 3 ViGAR Framework, 4 Simulation Experiments, 5 Real-World Robot Deployment, 6 Conclusion and Limitations, References, Appendices A–C) are completely translated with paragraph-by-paragraph bilingual blockquotes.
   - Paragraph formatting strictly follows:
     `> <span style="color:#3B82F6"><strong>Para. X:</strong></span> English text...`
     `> <span style="color:#F59E0B"><strong>Para. X[CN]:</strong></span> 严谨中文翻译...`
   - Major sections restart paragraph numbering from `Para. 1:` to maintain clean, auditable references.

2. **Mathematical Notation & Display Equations:**
   - In accordance with the output contract, all display equations are set outside blockquotes with `$$...$$` syntax.
   - Inline math preserves exact LaTeX formatting: `$A_{t+1}$`, `$o_t$`, `$\pi^\text{WAM}_\phi$`, `$G_\theta$`, etc.
   - Delimiters `\(...\)` and `\[...\]` were strictly avoided to ensure perfect markdown parser compatibility.
   - Display equations transcribed:
     - Equation (1): In-context manipulation general formulation.
     - Equation (2): Subgoal look-ahead rule (piecewise boundary redirection).
     - Equation (3): End-effector ROI weight calculation $w_i(u)$.
     - Flow matching objectives: $\mathcal{L}_\text{Plan}$, $\mathcal{L}_\text{WAM}$, $\mathcal{L}_\text{Plan-ICL}$.
     - Equations (4) & (5): Stage-wise success rate $\text{SR}_k$ and Task Progress Score $\text{TPS}$.

3. **Tables Transcription:**
   - All five tables (Table 1, Table 2, Table 3, Table 4, Table 5) are fully transcribed into searchable GitHub-flavored Markdown tables.
   - Table images `![Table X](assets/table_X.png)` are embedded immediately before the Markdown table blocks, followed strictly by `**Caption:**` and `**Caption[CN]:**`.
   - Table 1 combines (a) simulation manipulation performance on RoboTwin Clean2Random and (b) visual subgoal quality on both RoboTwin and real-robot benchmarks.
   - Table 2 transcribes (a) goal injection route ablations and (b) look-ahead & ROI weighting ablations.
   - Table 3 transcribes the detailed training hyperparameters for both $G_\theta$ and $\pi^\text{WAM}_\phi$.
   - Tables 4 and 5 transcribe the stage-wise success rates across all stages (S1–S5) and overall task progress scores.

4. **Figures & Asset Embedding:**
   - All 9 figures (Figures 1–9) are embedded with relative links `![Figure X](assets/figure_X.png)`.
   - Each figure card contains bilingual caption pairs: `**Caption:**` and `**Caption[CN]:**`.
   - Page scans `page_001.png`–`page_019.png` in `assets/` are preserved as extraction evidence and not exposed in the reader body to prevent link validation overhead.

---

## 3. Terminology & Translation Policy

| English Term | Chinese Translation | Rationale & Policy |
|---|---|---|
| ViGAR | ViGAR (基于视觉目标条件化动作推理) | Framework name kept in English acronym, Chinese translation provided at first mention |
| World-Action Model (WAM) | 世界-动作模型 (WAM) | Standard terminology in embodied AI for joint observation-action generative models |
| Visual Subgoal Planner ($G_\theta$) | 视觉子目标规划器 | Higher-level module predicting target endpoint images |
| Subgoal Executor ($\pi^\text{WAM}_\phi$) | 子目标执行器 / 世界-动作策略 | Lower-level module generating action trajectories |
| In-Context Robotic Manipulation | 上下文机器人操作 | Analogous to LLM in-context learning, steered via a global goal image |
| Subgoal Look-Ahead Rule | 子目标前瞻规则 | Rule redirecting the last $p\%$ of subtask frames to the subsequent subgoal |
| End-Effector ROI Weighting | 末端执行器 ROI 加权 | Spatial weighting focusing loss on end-effector projection regions |
| Clean2Random Benchmark | Clean2Random 基准 | RoboTwin's clean-training to domain-randomized testing benchmark |
| AgiBot A2 | 智元远征 A2 机器人 | Commercial bimanual humanoid/manipulation platform from AgiBot |
| Cosmos3-Nano | Cosmos3-Nano | Dual-branch foundation world model backbone (16B-A8B MoE) |
| TeaCache | TeaCache | Timestep embedding cache skipping Transformer computation in diffusion steps |
| Task Progress Score (TPS) | 任务进度得分 | Metric quantifying stage completion fraction before first failure |
| Stage-wise Success Rate (SR) | 分阶段成功率 | Conditional probability of completing stage $k$ given prior stages completed |

- **Untranslated Elements:**
  - Bibliographic references [1]–[40] are retained in original English bibliographic format to ensure citation fidelity and searchability.
  - Model identifiers (StarVLA, Abot-M0, X-VLA, $\pi_{0.5}$, Fast-WAM, LingBot-VA, 4D-WAM, Cosmos3-Nano, DINOv2-base, AlexNet) remain in English.
  - Hardware specifications (NVIDIA B20Z, Aloha AgileX, AgiBot A2) remain in English.

---

## 4. Quality & File Boundary Audit

- **Untouched Companion Files:**
  - `paper_DeepPaperNote.md` and related notes were strictly unmodified.
  - `images/` directory was preserved without changes.
- **Validation Execution:**
  - Validated using `validate_detailed_paper.py` from `nature-reader-detail-wj`:
    ```bash
    python3 /Users/roywangj/Desktop/skills4ai/wj_skills/nature-reader-detail-wj/scripts/validate_detailed_paper.py \
      detailed_paper.md \
      --source paper.md \
      --require-identical
    ```
  - **Results:**
    - `passes: True`
    - `bytes: 116878`
    - `bilingual paragraph pairs: 63`
    - `caption pairs: 14 original / 14 Chinese`
    - `image links: 14 (missing: 0)`
    - `errors: 0`
    - `warnings: 0`
