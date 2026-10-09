# Translation & Extraction Notes: In-Context Robot Learning with VLM Agents (GPT-Policy)

## 1. Extraction Scope & Completeness
- Full paper (32 pages) text extracted from `Cheng 等 - 2026 - In-Context Robot Learning with VLM Agents.pdf`.
- All figures (Figures 1–8) and tables (Tables 1–7) cropped at 250 DPI into both `assets/` and `images/`.
- All substantive tables transcribed into searchable GitHub Flavored Markdown tables.

## 2. Terminology & Conceptual Mapping
- `In-Context Robot Learning`: Translated as “语境化机器人学习 / 上下文机器人学习”, policy adaptation without parameter gradient updates.
- `GPT-Policy`: The general-agent framework powered by frontier commercial VLMs (GPT-6 Astra).
- `Context Compiler`: Translated as “语境编译器”, extracts informative spatio-temporal keyframes under token budgets.
- `Execution Harness`: Translated as “执行套具”, ensures kinematics verification, Cartesian safety clamping, and settling checks.

## 3. Structural Validation
- Validated via `validate_detailed_paper.py` ensuring exact paragraph-by-paragraph bilingual alignment, blockquote syntax, figure/table card formatting, and byte-for-byte identity between `detailed_paper.md` and `paper.md`.
