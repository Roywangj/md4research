# Translation & Extraction Notes: VideoSeek

## 1. Extraction Scope & Completeness
- Full paper (18 pages) text extracted from `Lin 等 - 2026 - VideoSeek Long-Horizon Video Agent with Tool-Guided Seeking.pdf`.
- All figures (Figures 1–11) and tables (Tables 1–5) cropped at 250 DPI into both `assets/` and `images/`.
- All substantive tables transcribed into clean, searchable GitHub Flavored Markdown tables.

## 2. Terminology & Conceptual Mapping
- `VideoSeek`: Translated as “VideoSeek 智能体”, emphasizing tool-guided seeking along narrative logic flows.
- `Video Logic Flow`: Translated as “视频逻辑流”, the causal and temporal narrative trajectory across long videos.
- `<overview>`, `<skim>`, `<focus>`: The multi-granular toolkit providing macroscopic (16 frames), mesoscopic (8-16 frames), and microscopic (dense interval) perceptual access.

## 3. Structural Validation
- Validated via `validate_detailed_paper.py` ensuring exact paragraph-by-paragraph bilingual alignment, blockquote syntax, figure/table card formatting, and byte-for-byte identity between `detailed_paper.md` and `paper.md`.
