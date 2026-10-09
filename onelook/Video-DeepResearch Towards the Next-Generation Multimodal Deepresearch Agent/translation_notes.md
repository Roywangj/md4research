# Translation notes

## Scope

Complete paragraph-level English–Chinese detailed reader of:

`/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/9FZK7FJH/Fang 等 - 2026 - Video-DeepResearch Towards the Next-Generation Multimodal Deepresearch Agent.pdf`

- arXiv: 2608.03979v1 [cs.CV] 4 Aug 2026
- Source format: selectable-text PDF (`pdf-text`), 20 pages, two-column A4 (arXiv GenPDF)
- Primary reader: `detailed_paper.md` (copied to `paper.md` after validation)
- Mode: new full-paper build (`nature-reader-detail-wj`)

Covered: abstract, §§1–6, author information, limitation, references (bibliographic form, not translated entry-by-entry), appendix B–D, prompt figures 4–8, Table 6.

## Extraction / layout

- Two-column reading order was recovered from page PNGs plus PyMuPDF blocks, not the raw left-to-right text stream.
- Hyphenated line breaks were rejoined (`ground-` / `ing`, `multi-` / `hop`, etc.).
- Page 6 contains a stray typesetting token `arxiv` between the Agentic-setting sentence and the judge-prompt sentence. It is omitted from cleaned prose and recorded here.
- §3.3 SFT cites unresolved `Table ??` in the PDF; retained as printed.
- Equation (1)–(3) were transcribed from the rendered pages. Equation (3) is printed as a compact GRPO clip objective minus $\beta\mathbb{D}_{\mathrm{KL}}$ without an expanded KL argument; the reader follows that typesetting.
- Footnote 1 on page 4 is `YouTube`; it was folded into the Step 0 streaming-platform sentence.

## Assets / crop caveats

Crops are 2× `fitz` clips of the PDF page (not the tiny embedded tiles under `_extract/images/`). Captions are kept in Markdown, not inside the crop.

| Asset | Page | Caveat |
|---|---|---|
| `assets/page_002_fig_figure_1.png` | 2 | Left-column pipeline; caption excluded |
| `assets/page_003_fig_figure_2.png` | 3 | Full-width domain wheel; small Q/A text on cards is hard to read at print size |
| `assets/page_003_tab_table_1.png` | 3 | Table body only |
| `assets/page_004_fig_figure_3.png` | 4 | Tight crop of the four-phase diagram including Benchmark Construction |
| `assets/page_006_tab_table_2.png` | 6 | Right-column table body |
| `assets/page_007_tab_table_3.png` | 7 | Full-width table; best-in-column underlines/bold preserved in the image, partially in Markdown |
| `assets/page_008_tab_table_4.png` | 8 | Left-column table |
| `assets/page_008_tab_table_5.png` | 8 | Right-column table; header prints `VideoDR-Bench` |
| `assets/page_015_fig_figure_4.png`–`page_019_fig_figure_8.png` | 15–19 | Prompt cards; literals also transcribed in the reader |
| `assets/page_020_tab_table_6.png` | 20 | Tool spec table; JSON key is `rational` as printed |

`_extract/` was reused and not deleted.

## Untranslated / skipped policy

- References kept in English bibliographic form; a bilingual policy pair explains this.
- Prompt sentinels, JSON keys, tool names, XML tags (`<tool_call>`, `<answer>`), and output schemas are not translated.
- Model, benchmark, and dataset identifiers stay in English.
- Source-internal naming collisions are transcribed locally rather than normalized:
  - VideoDR-Bench size: **200** (abstract / contributions / conclusion) vs **100 human-annotated VQA pairs** (§4.1). Table 2 counts sum to 200.
  - Qwen3.5-397B-**A17B** (Table 1, §3) vs **A3B** (§4.1) vs **A13B** (Table 3, §4.5).
  - Appendix D heading **VIDEOHUNT** vs body **VIDEODR-BENCH**.
  - §4.2 prose “VIDEODR-BENCH (65.4%)” vs Table 3 Overall **60.0** / ENT **65.9**.
  - Table 3 caption claims Direct and Agentic settings; the printed table is a single score block.
- Shared `_extract/` and existing `images/` / DeepPaperNote files were not overwritten.

## Validation

```
python3.13 .../validate_detailed_paper.py .../detailed_paper.md
passes: True
bilingual paragraph pairs: 159
caption pairs: 14 original / 14 Chinese
image links: 14 (missing: 0)
```

Then `paper.md` was copied from the validated `detailed_paper.md`.
