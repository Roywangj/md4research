# Translation Notes / 翻译与解析说明

- **Source Paper:** *ASPIRE: Agentic /Skills Discovery for Robotics* (Runyu Lu, Yubo Wu, Ethan Kou, Letian Fu, Wenli Xiao, Ajay Mandlekar, Yinzhen Xu, Guanya Shi, Ken Goldberg, Ang Chen, Mosharaf Chowdhury, Yuke Zhu, Linxi "Jim" Fan, Guanzhi Wang; NVIDIA, UMich, UIUC, UC Berkeley, CMU).
- **Version & Date:** arXiv:2607.00272v1 [cs.RO], 30 Jun 2026. 43 pages. Project page: `https://research.nvidia.com/labs/gear/aspire/`.
- **Mode:** New full-paper build under `nature-reader-detail`; `detailed_paper.md` serves as the primary paragraph-by-paragraph bilingual reader, duplicated byte-for-byte to `paper.md`.
- **Extraction & Source Integrity:** Sourced from `extracted_text.txt` and verified against original PDF `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/JGD7JHIJ/Lu 等 - 2026 - ASPIRE Agentic Skills Discovery for Robotics.pdf`.
- **Structural Alignment:**
  - All 43 pages and all sections are faithfully covered: Frontmatter, Title, Abstract, Section 1 Introduction, Section 2 Method / The Aspire Framework (2.1 Robot Execution Engine, 2.2 Skill Library, 2.3 Evolutionary Search), Section 3 Experiments (3.1 Setup, 3.2 Benchmarks & Baselines, 3.3 Protocol, 3.4 Main Results, 3.5 Zero-Shot Transfer, 3.6 Real-Robot Cross-Embodiment Transfer, 3.7 Ablations), Section 4 Related Work, Section 5 Limitations & Future Work, Section 6 Conclusion, Acknowledgments, References (all 45 entries), and Appendices A through E (Skill Library Details & Figures 7-12, Main Benchmark Result Tables 2-4, LIBERO-Pro Long Zero-Shot Transfer Tables 5-6, Ablation Details Tables 7-9, and Agent Pipeline Skills E.1-E.5).
- **Bilingual Arrangement:**
  - Strict paragraph-by-paragraph blockquote pairing:
    `> <span style="color:#3B82F6"><strong>Para. X:</strong></span> English text...`
    `> <span style="color:#F59E0B"><strong>Para. X[CN]:</strong></span> 对应严谨学术中文翻译...`
  - Numbering restarts cleanly at major sections or follows natural sequence, maintaining identical label tags within each pair.
- **Figures and Tables:**
  - All 12 figures (`assets/figure_1.png` to `figure_12.png`) are embedded with relative links, followed immediately by bilingual captions `**Caption:**` and `**Caption[CN]:**`.
  - All 9 tables (`assets/table_1.png` to `table_9.png`) are embedded with relative links, fully transcribed into searchable Markdown tables, and followed immediately by bilingual captions `**Caption:**` and `**Caption[CN]:**`.
- **Mathematical Notation & Technical Literals:**
  - Standalone display math is rendered outside blockquotes ($$...$$) while inline math uses $...$.
  - All code blocks, API names, function signatures, JSON schemas, parameters, and benchmark suite names (`CaP-X`, `SAM3`, `OpenVLA`, `pi_0`, `pi_0.5`, `LIBERO-Pro`, `BEHAVIOR-1K`, `Robosuite`) are preserved with 100% precision.
- **Reference Preservation:**
  - All 45 bibliographic entries from the paper are preserved in full searchable citation format, accompanied by bilingual Chinese translated titles.
- **File Boundaries:**
  - Files created: `detailed_paper.md`, `paper.md`, `source_map.json`, `translation_notes.md`.
  - Untouched / Preserved: `paper_DeepPaperNote.md`, `paper_DeepPaperNote.*.json`, `images/`, `assets/`.
