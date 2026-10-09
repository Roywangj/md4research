# Translation Notes — RLinf

## Source identity

- Canonical source: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/STKQ8SYL/Yu 等 - 2025 - RLinf Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformat.pdf`
- Verified SHA256: `b4f26818a69edf2cb55c4fcb1cc4ab9d0d753205c83a1fc08c42e4b42c5a068a`
- Verified artifact: arXiv `2509.15965v2`, 16 pages, 29 authors, dated 2025-12-29.
- Zotero parent/attachment: `JKUF2Y7Q` / `STKQ8SYL`.

## Scope and coverage

The reader covers the complete source in reading order: Abstract; Sections 1–7; all 16 figures; all 3 tables; Algorithm 1; the single displayed scheduling equation; and references [1]–[60]. The source has no appendix, separately headed limitations, acknowledgments, availability, or ethics section. `detailed_paper.md` is authoritative and `paper.md` is a byte-identical copy.

## Extraction and layout notes

- Text came from the selectable PDF layer; OCR was not used for prose.
- All 16 rendered pages were inspected. The paper uses a dense two-column layout, with several figure groups interleaved across columns on pages 10–12. Natural section reading order was restored rather than preserving raw column-stream order.
- Figure/table assets were rendered from the canonical PDF at 300 DPI and cropped locally. Figure 12 is narrow and the page has adjacent prose; its crop prioritizes the plotted panel and caption. The combined Table 1/2 crop mirrors their shared left-column placement, while both tables are independently searchable in Markdown.
- Bar heights were not digitized where the paper did not report numeric values in prose. Only authored numerical claims and exact table values are transcribed.

## Translation policy

- Translation preserves claims, hedges, comparisons, numbers, units, citations, model names, algorithm names, and directionality.
- Stable system/code literals remain exact, including `Worker`, `WorkerGroup`, `device_lock`, `onload`, `offload`, `send`, `recv`, `Channel.create`, `wait`, `max_running_requests`, `d001d`, SGLang, vLLM, NCCL, CUDA IPC, Gloo, Ray, Megatron-LM, and FSDP.
- “macro logical flow” is consistently rendered “宏观逻辑流”; “micro execution flow” as “微观执行流”; “elastic pipelining” as “弹性流水线”; “context switching” as “上下文切换”. The English `rollout` is retained where it functions as a stable systems-stage name.
- References remain in searchable bibliographic English. Long author lists represented by `et al.` follow the source-level abbreviated bibliography where used; no bibliographic facts were inferred.

## Evidence boundaries and uncertainties

- No text block was omitted because of extraction uncertainty.
- Algorithm 1 was checked against the rendered source and is included both as a crop and searchable pseudocode. Mathematical notation is normalized for Markdown rendering.
- The paper provides broad framework support and many experimental parameters, but a separate reproducibility appendix with exhaustive configuration, checkpoint/fault-tolerance policy, seeds, and uncertainty statistics is outside the supplied source. The reader records that boundary without inventing details.
- The scheduler’s cycle handling is reported exactly as collapsing cycles into nodes and evenly partitioning their computation; “near-optimal” is preserved as a hedge rather than strengthened to an optimality guarantee.

## Tool-use compliance

No Codex MCP/CLI, nested Claude/Codex CLI, external LLM, or delegated model was used. Work was confined to the isolated RLinf bilingual-reader target.
