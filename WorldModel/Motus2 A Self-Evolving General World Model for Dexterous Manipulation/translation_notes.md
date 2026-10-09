# Translation & Extraction Notes: Motus2

## 1. Extraction Scope & Completeness
- Full paper (30 pages) text extracted from `Bi 等 - 2026 - Motus2 A Self-Evolving General World Model for Dexterous Manipulation.pdf`.
- All figures (Figures 1–8) and tables (Tables 1–5) cropped at 250 DPI into both `assets/` and `images/`.
- All substantive tables transcribed into clean, searchable GitHub Flavored Markdown tables.
- Equations 1–16 formatted as standalone `$$...$$` blocks outside blockquotes.

## 2. Terminology & Conceptual Mapping
- `General World Model (GWM)`: Translated as “通用世界模型”, unifying policy, simulation, and evaluation.
- `Action-First Factorization`: Translated as “动作优先因果分解”, factorizing joint density into $\pi_	heta \cdot p_	heta^{	ext{wm}} \cdot p_	heta^{	ext{vm}}$.
- `DiffusionNFT`: Non-fine-tuning policy optimization via flow matching.
- `Tactile Expert`: Lightweight high-rate action refinement and force prediction network.

## 3. Structural Validation
- Validated via `validate_detailed_paper.py` ensuring exact paragraph-by-paragraph bilingual alignment, blockquote syntax, figure/table card formatting, and byte-for-byte identity between `detailed_paper.md` and `paper.md`.
