# Translation & Extraction Notes: Beyond Future Prediction (NowWAM)

## 1. Extraction Scope & Completeness
- Full paper (14 pages) text extracted from `Wang 等 - 2026 - Beyond Future Prediction Denoising as Generative Adaptation for Robot Control.pdf`.
- All figures (Figures 1–4) and tables (Tables 1–4) cropped at 250 DPI into both `assets/` and `images/`.
- All tables transcribed into clean, searchable GitHub Flavored Markdown tables.
- Equations 1–11 formatted as standalone `$$...$$` blocks outside blockquotes.

## 2. Terminology & Conceptual Mapping
- `Generative Adaptation`: Translated as “生成式自适应”, referring to transferring visual and geometric priors from pretrained DiTs to robot control.
- `NowWAM`: Named from “Now-World-Action Model”, highlighting that the generative objective operates on the current observation rather than future targets.
- `Future-Target-Free Co-Training`: Translated as “无未来目标联合训练”, eliminating the secondary visual stream during training.
- `Denoising Trajectory Coupling`: Translated as “去噪轨迹表征耦合”, sampling current latents across noise levels during training.
- `Clean-Endpoint Control`: Translated as “纯净端点控制”, running single forward passes at $\sigma = 0$ during inference.

## 3. Structural Validation
- Validated via `validate_detailed_paper.py` ensuring exact paragraph-by-paragraph bilingual alignment, blockquote syntax, figure/table card formatting, and byte-for-byte identity between `detailed_paper.md` and `paper.md`.
