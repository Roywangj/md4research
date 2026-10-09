# Translation and Extraction Notes

## Scope

- `detailed_paper.md` and `paper.md` contain the complete paragraph-by-paragraph Chinese-English bilingual reader for "EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies" (Yang et al., 2026).
- The reader covers the complete paper without omissions: Title, Authors, Affiliations, Abstract, Keywords, Section 1 (Introduction), Section 2 (Related Work), Section 3 (EventVLA Framework), Section 4 (RoboTwin-MeM Benchmark), Section 5 (Experiments), Section 6 (Limitations), Section 7 (Conclusion), Acknowledgments, References [1]–[48], and substantive Appendices A, B, C, and D.
- Figures and Tables:
  - All 8 figures from the paper are integrated with local relative links to `assets/figure_1.png` ~ `assets/figure_8.png`, accompanied by exact original English captions and faithful Chinese translations.
  - All 9 tables from the paper are integrated with local relative links to `assets/table_1.png` ~ `assets/table_9.png`, transcribed into clean, searchable Markdown tables, and accompanied by bilingual captions.
  - Mathematical equations (Equations 1 through 8) are displayed using standalone `$$...$$` blocks outside blockquotes, preserving exact notation and variable naming.
  - The exact system prompt for VLM-based keyframe annotation (Appendix A.3) is preserved verbatim in code formatting.

## Source and Provenance

- Primary source PDF: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/RFZ8Y4FX/Yang 等 - 2026 - EventVLA Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies.pdf` (23 pages).
- Structured layout text: `extracted_text.txt` in target directory.
- Local extracted assets: `assets/figure_1.png` ~ `assets/figure_8.png`, `assets/table_1.png` ~ `assets/table_9.png`, `assets/page_001.png` ~ `assets/page_023.png`.
- Multi-column reading order, equations, and tables were visually cross-checked against rendered page images (`assets/page_001.png` ~ `assets/page_023.png`).

## Terminology and Literal Policy

- Model names, framework identifiers, and benchmark names remain in English: EventVLA, Qwen3-VL, QwenOFT, OpenVLA-OFT, $\pi_0$, $\pi_{0.5}$, $\pi_{\text{MEM}}$, DP, ACT, X-VLA, RoboTwin 2.0, RoboTwin-MeM, RMBench, RoboMME, SAPIEN, vLLM.
- Mathematical operators and symbols remain exact: $o_t$, $a_t$, $l$, $M_t$, $\mathcal{A}_t$, $\mathcal{E}_t$, $h_t$, $\hat{p}_t$, $\tau_{\text{commit}}$, $N_{\max}$, $w$, $C$, $\lambda$, $\alpha$, $\mathcal{L}_{\text{action}}$, $\mathcal{L}_{\text{kem}}$.
- Keyframe Evidence Memory (KEM) is translated consistently as "关键帧证据记忆模块".
- Foundational Visual Anchors is translated consistently as "基础视觉锚点".
- Foresight-driven keyframe prediction is translated consistently as "前瞻驱动的关键帧预测".
- Chunk-wise prediction is translated consistently as "动作块级预测 / 分块级预测".
- 1D Non-Maximum Suppression (NMS) is translated as "一维非极大值抑制（1D NMS）".
- System prompt literals, placeholders (`<episode id>`, `<task instruction>`, `<num keyframes>`, etc.), and JSON output specifications are preserved verbatim.

## Deliverables and Boundary Verification

- `detailed_paper.md`: Complete detailed bilingual reader.
- `paper.md`: Exact byte-for-byte copy of `detailed_paper.md`.
- `source_map.json`: Complete structural block map following the project schema.
- `translation_notes.md`: Documentation of extraction scope, provenance, terminology, and validation results.
- Sibling files `paper_DeepPaperNote.md`, `paper_DeepPaperNote.*.json`, and `images/` were left completely untouched.

## Validation

- Validated using `validate_detailed_paper.py`:
  - Passes: True.
  - Zero syntax or formatting errors.
  - Bilingual paragraph pairs: 74.
  - Caption pairs: 17 original / 17 Chinese (8 figures + 9 tables).
  - Image links: 17 (0 broken links).
  - References: 48 entries matching `re.compile(r"^\s*\d+\.\s+")`.
  - `detailed_paper.md` and `paper.md` are verified to be byte-identical via SHA256 checksum matching.
