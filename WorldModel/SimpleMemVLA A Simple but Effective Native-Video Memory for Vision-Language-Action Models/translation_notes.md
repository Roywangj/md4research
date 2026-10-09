# Translation & Extraction Notes: SimpleMemVLA

## 1. Extraction Scope & Completeness
- Full paper (29 pages) text extracted from `Yin 等 - 2026 - SimpleMemVLA A Simple but Effective Native-Video Memory for Vision-Language-Action Models.pdf`.
- All figures (Figures 1–12) and tables (Tables 1–11) cropped at 250 DPI into both `assets/` and `images/`.
- All substantive tables transcribed into clean, searchable GitHub Flavored Markdown tables.
- Equations 1–4 formatted as standalone `$$...$$` blocks outside blockquotes.

## 2. Terminology & Conceptual Mapping
- `Native-Video Memory`: Translated as “原生视频记忆”, emphasizing direct input into the VLM video channel without dedicated memory structures.
- `Narrow Text Channel`: Translated as “极窄文本通道”, using generated sub-task tokens $g_t$ and their contextual hidden states as the only bridge to continuous action generation.
- `Sub-task Bottleneck`: Translated as “子任务表征瓶颈”, preventing direct attention from past tokens to continuous actions.
- `Exact Streaming Inference`: Translated as “无损流式推断”, prefilling prefix KV-cache during action execution.
- `Sliding-Window Attention (SWA)`: Translated as “滑动窗口注意力变体”, evicting old softmax KV tokens while retaining linear-attention recurrent states.

## 3. Structural Validation
- Validated via `validate_detailed_paper.py` ensuring exact paragraph-by-paragraph bilingual alignment, blockquote syntax, figure/table card formatting, and byte-for-byte identity between `detailed_paper.md` and `paper.md`.
