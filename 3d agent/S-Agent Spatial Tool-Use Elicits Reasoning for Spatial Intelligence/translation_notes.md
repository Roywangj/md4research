# Translation and reading notes

## Scope

This bundle was produced from the local PDF:

`/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/I5V4GXZJ/Dai 等 - 2026 - S-Agent Spatial Tool-Use Elicits Reasoning for Spatial Intelligence.pdf`

The PDF has selectable text and 22 pages. Figures and tables were rendered from the PDF pages, then cropped into `assets/`.

## Copyright-aware handling

The `paper.md` file is a source-grounded bilingual reader, not a verbatim full-text reproduction. English `Para.` blocks are faithful paraphrases/cleaned reading units based on the paper’s order and claims; Chinese `Para.[CN]` blocks are aligned translations/explanations. Figure and table captions are also paraphrased rather than copied wholesale.

## Terminology choices

| English | Chinese used | Rationale |
|---|---|---|
| S-Agent | S-Agent | Model/framework name kept unchanged |
| spatial intelligence | 空间智能 | Standard academic rendering |
| spatial tool-use | 空间工具调用 / 空间工具使用 | “调用” is used when emphasizing agent actions; “使用” when naming the paradigm |
| semantic planner | 语义规划器 | Captures the VLM’s role as a controller/planner rather than a passive answerer |
| hierarchical spatial evidence | 层级化空间证据 | Preserves the L1/L2/L3 evidence hierarchy |
| Scene Memory | 场景记忆 | Stores task-relevant entities, locations, relations, and scene state |
| Agent Memory | 智能体记忆 | Stores reasoning history, tool calls, observations, and intermediate conclusions |
| spatio-temporal evidence accumulation | 时空证据累积 | Central mechanism of the paper |
| trajectory distillation | 轨迹蒸馏 | Training student model from teacher-agent tool traces |
| final-answer trajectories | 最终答案轨迹 | Complete trajectory ending in the final answer |
| turn-level trajectories | 回合级轨迹 | One planner turn becomes one training sample |
| nontrivial tool/expert trajectories | 非平凡工具/专家轨迹 | Kept as “非平凡” to preserve the paper’s filtering meaning |

## Figure/table extraction

The following assets were extracted:

- Fig. 1 overview
- Fig. 2 pipeline
- Fig. 3 S-300K statistics
- Fig. 4 tool-grounded qualitative example
- Fig. 5 main qualitative examples
- Fig. 6 appendix qualitative examples
- Fig. 7 appendix qualitative examples
- Tables 1–7

All crops were manually checked from rendered pages. Table 6 required an extra crop adjustment to avoid clipping the header or including surrounding body text.

## Reading stance

The notes emphasize the paper’s argument structure:

1. Diagnose the semantic-to-geometric gap in VLMs.
2. Recast spatial reasoning as active evidence accumulation.
3. Use a VLM planner plus hierarchical tools and memory.
4. Show zero-shot benchmark improvements.
5. Distill tool-use trajectories into S-Agent-8B.
6. Use ablations and qualitative cases to identify which components matter.

## Cautionary points

- The framework depends on external tool quality; incorrect grounding or depth can propagate into wrong answers.
- The ablation suggests that tools alone do not solve the problem; planner competence and memory integration are necessary.
- ReVSI shows strong but not universally dominant performance, so the claim should be read as targeted improvement on spatial reasoning rather than all-purpose VLM superiority.
- VSI-SUPER results are supplementary because the authors themselves caution about benchmark reliability.

