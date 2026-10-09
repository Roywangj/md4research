# Translation & Extraction Notes: Deep Video Discovery (DVD)

## 1. Extraction Scope & Completeness
- Full paper (27 pages) text extracted from `Zhang 等 - 2025 - Deep Video Discovery Agentic Search with Tool Use for Long-form Video Understanding.pdf`.
- All figures (Figures 1–8) and tables (Tables 1–14) cropped at 250 DPI into both `assets/` and `images/`.
- All substantive tables transcribed into searchable GitHub Flavored Markdown tables.

## 2. Terminology & Conceptual Mapping
- `Deep Video Discovery (DVD)`: Translated as “深度视频发现”, emphasizing agentic search over multi-granular video databases.
- `Multi-granular Video Database`: Translated as “多粒度视频数据库”, encompassing global summaries, temporal clip captions, subjects, and frame caches.
- `Agentic Search and Answering (ASA)`: Translated as “智能体搜索与问答”, the iterative reasoning loop.
- `Global Browse Only (GBO)`, `Simple Action (SA)`, `Iterative Search (IS)`, `Frame Inspect Trap (FIT)`, `Clip Search Trap (CST)`: Standard behavioral profiles analyzed in Section 4.5.

## 3. Structural Validation
- Validated via `validate_detailed_paper.py` ensuring exact paragraph-by-paragraph bilingual alignment, blockquote syntax, figure/table card formatting, and byte-for-byte identity between `detailed_paper.md` and `paper.md`.
