# Translation & Extraction Notes: Route2Look

## 1. Extraction Scope & Completeness
- Full paper (19 pages) text extracted from `Wang 等 - 2026 - Routing Before Looking Query-Adaptive Evidence Acquisition for Long-form Video Understanding.pdf`.
- All figures (Figures 1–12) and tables (Tables 1–7) cropped at 250 DPI into both `assets/` and `images/`.
- All substantive tables transcribed into searchable GitHub Flavored Markdown tables.
- All display math equations formatted outside blockquotes as standard `$$...$$` blocks.

## 2. Terminology & Conceptual Mapping
- `Routing Before Looking`: Translated as “先路由后观察”，emphasizing that strategy routing occurs before consuming expensive visual perception tokens.
- `Generation-based Strategy`: Translated as “基于生成的策略”，referring to global anchor sampling, coarse timeline synthesis, and progressive grounding.
- `Retrieval-based Strategy`: Translated as “基于检索的策略”，referring to multimodal lexical/semantic matching followed by localized dense verification.
- `Differential Contrastive Analysis`: Translated as “差异对比分析”，the offline trajectory comparison mechanism used to distill routing skills.
- `Distilled Skill Patch`: Translated as “蒸馏技能补丁”，representing compact, modular prompt rules composed of Trigger, Route, and Lesson tuples.

## 3. Structural Validation
- Validated via `validate_detailed_paper.py` ensuring exact paragraph-by-paragraph bilingual alignment, blockquote syntax, figure/table card formatting, and byte-for-byte identity between `detailed_paper.md` and `paper.md`.
