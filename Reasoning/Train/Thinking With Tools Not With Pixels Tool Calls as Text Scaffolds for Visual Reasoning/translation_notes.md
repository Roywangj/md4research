# Translation notes

- Source: selectable-text 33-page PDF; canonical extraction is `source_full_text.txt`.
- Fixed literal `[Image output skipped]` is preserved exactly.
- The delivered `paper.md` and `detailed_paper.md` are a structured bilingual reconstruction of the full paper's main sections and appendices, with key claims, tables, figures, formulas, and resource figures retained. They are not a literal paragraph-by-paragraph reproduction of every reference entry; the original PDF and `source_full_text.txt` remain authoritative for verbatim checking.
- Key evidence covered: TextCall carrier swap, returned-pixel ablation, factorial scaffold audit, six-benchmark results, LoRA/full fine-tuning/SFT/GRPO, RL dynamics, latency, hardware cost, and overclaim boundaries.
- Fixed page-level PNG assets are included under `assets/` for selected protocol and training-dynamics evidence. Quantitative tables are transcribed in Markdown where searchable values matter more than a crop.
- Classification: `Train`, because the carrier swap is applied during SFT/RL training and inference and the central result depends on parameter updates.
