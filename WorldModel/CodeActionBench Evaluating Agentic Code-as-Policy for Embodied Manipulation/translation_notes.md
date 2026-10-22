# Translation Notes

## Scope

This directory contains the complete English–Chinese bilingual detailed paper reader for:

**"CodeActionBench: Evaluating Agentic Code-as-Policy for Embodied Manipulation"**  
*Yiheng Lyu, Xueying Jiang, Wenhao Li, Shijian Lu, Gongjie Zhang (Nanyang Technological University, Singapore & Independent Researcher, September 2026, arXiv:2609.33807v1).*

- **Primary Deliverables:**
  - `detailed_paper.md`: Full paragraph-by-paragraph bilingual detailed reader with custom CSS-styled labels.
  - `paper.md`: Exact byte-for-byte identical copy of `detailed_paper.md`.
  - `source_map.json`: Structural traceability metadata mapping sections, figures, tables, and local assets.
  - `translation_notes.md`: Translation scope, conventions, terminology choices, and caveats.
- **Workflow & Rules:** Built under `nature-reader-detail-wj` specifications. Preserves all substantive body text, formulas, diagrams, tables, and appendices A–H in original publication order.

## Source and Extraction

- **Source PDF:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/VKJ5IF59/Lyu 等 - 2026 - CodeActionBench Evaluating Agentic Code-as-Policy for Embodied Manipulation.pdf` (28 pages, single-column / two-column mixed layout).
- **Extracted Text:** `extracted_text.txt` (114,203 characters across 28 pages).
- **Verification Strategy:** Every paragraph was verified against the original PDF blocks extracted via PyMuPDF (`fitz`), ensuring no omitted sections, footnotes, formulas, or tables.

## Formatting & Structural Rules

1. **Bilingual Blockquote Pairs:**
   All substantive prose blocks follow the strict format:
   ```markdown
   > <span style="color:#3B82F6"><strong>Para. X:</strong></span> Original English text...

   > <span style="color:#F59E0B"><strong>Para. X[CN]:</strong></span> 严谨专业学术中文翻译...
   ```
   Lists and enumerations retain bullet-point hierarchy inside both original and Chinese blockquotes.
2. **Display Math:**
   Display equations (such as resource budget formulas $B_{	ext{tool}}$ and $B_{	ext{sim}}$) are placed on standalone lines outside blockquotes using `$$...$$` to guarantee rendering compliance. Inline math uses `$...$`.
3. **Substantive Tables Transcription:**
   All key substantive tables (Table 1, Table 2, Table 8, Table 9, Table 10, Table 11, Table 14, Table 15) are transcribed into clean Markdown tables positioned between the image link and the original caption block.
4. **Figure & Table Cards:**
   Every local image is referenced via relative path (`assets/figure_X.png`, `assets/table_X.png`) and immediately paired with balanced `**Caption:**` and `**Caption[CN]:**` blocks. All 27 local image assets resolve without broken links.

## Terminology Conventions

- **Code-as-Policy (CaP):** 译为“代码即策略”，指模型在推理阶段直接生成控制机器人 API 的计算机程序。
- **Agentic Code-as-Policy:** 译为“智能体式代码即策略”，特指模型在闭环多轮交互中，自主感知、推理、编写代码并根据环境反馈持续修正策略。
- **Embodied Manipulation:** 译为“具身操作”。
- **Vision-Language-Action (VLA):** 译为“视觉-语言-动作”模型。
- **Tool Center Point (TCP):** 译为“工具中心点”，机器人末端执行器的控制参考原点。
- **Hidden / Out-of-band Verifier:** 译为“带外隐藏物理结果验证器”，独立于交互环境、对物理结果和事件进行终局客观判定的判定系统。
- **Subgoal Checkpoint / Spatial Checkpoint:** 译为“子目标检查点 / 空间检查点”。全基准共设计 55 个子目标检查点与 72 个空间检查点。
- **Reference Harness / Vendor Harness:** 译为“参考测试基座 / 厂商测试基座”。
- **Overclaim / Underclaim:** 译为“过度声称 / 保守低报（低估声称）”。Overclaim 指物理失败但智能体误报成功；Underclaim 指物理成功但智能体误报失败。
- **Premature Done Claim:** 译为“过早完成声称”。
- **Ray-Plane Intersection:** 译为“射线-平面求交”。
- **Contact Probing:** 译为“接触探测”。

## Protected Artifacts

In strict compliance with user instructions:
- `paper_DeepPaperNote.md`, `paper_DeepPaperNote.*.json`, and the `images/` directory were completely preserved and left untouched.

## Validation Status

Validated with:
```bash
python3 /Users/roywangj/Desktop/skills4ai/wj_skills/nature-reader-detail-wj/scripts/validate_detailed_paper.py   "detailed_paper.md"   --source "paper.md"   --require-identical
```
- **Result:** `passes: True` (0 errors, 0 warnings).
- **Paragraph pairs:** 109 bilingual pairs.
- **Caption pairs:** 27 original / 27 Chinese.
- **Image links:** 27 local links, 0 missing.
- **Bibliographic entries:** 62 references.
- **Byte identity:** `detailed_paper.md` and `paper.md` are 100% byte-identical.
