# Translation and reading notes

## Source

Local PDF:

`/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/Y32MYA9Q/Zhang 等 - 2025 - Thyme Think Beyond Images.pdf`

The PDF has selectable text and 32 pages. It was treated as `pdf-text` under the `nature-reader` workflow. Pages were rendered at 200 dpi for figure/table extraction.

## Output policy

`paper.md` is a bilingual reading companion, not a verbatim full-text copy. English `Para.` blocks are faithful cleaned paraphrases of the paper’s content, and Chinese `Para.[CN]` blocks are aligned translations/explanations. Figure and table captions are also paraphrased.

## Terminology decisions

| English | Chinese used | Note |
|---|---|---|
| Thyme | Thyme | Framework/model name kept unchanged |
| Think Beyond Images | 超越图像思考 | Used as conceptual translation when explaining the name |
| MLLM | 多模态大语言模型 | Multimodal Large Language Model |
| thinking with images | 借助图像思考 | Kept close to the OpenAI phrase |
| image manipulation | 图像操作 / 图像处理 | “操作” for model actions; “处理” for general capability |
| executable code | 可执行代码 | Core interface between model and sandbox |
| sandbox | 沙箱 | Secure execution and correction layer |
| SFT | 监督微调 | Supervised fine-tuning |
| RL | 强化学习 | Reinforcement learning |
| GRPO-ATS | 自适应温度采样的 GRPO | Group Relative Policy Optimization with Adaptive Temperature Sampling |
| consistency reward | 一致性奖励 | Checks whether reasoning supports the answer |
| code reward | 代码奖励 | Based on successful code execution, but may encourage unnecessary code |
| process reward | 过程奖励 | MLLM-based score for reasoning quality |

## Figure/table extraction

Extracted visual assets:

- Figures 1–16
- Tables 1–9

Total assets: 25 PNG files under `assets/`.

The first crop pass included some captions inside figure images. I tightened the crop boxes so visible captions are attached in Markdown card text rather than embedded in most figure images. For tables, the table title/caption is often visually integrated with the table body in the PDF, so the crop preserves the table block as printed.

## Reading stance

The notes follow the paper’s argument order:

1. Existing “thinking with images” systems are either generation-heavy or cropping-limited.
2. Thyme expands the action space to executable image-processing and computation code.
3. A sandbox makes model-generated code safer and more robust.
4. SFT cold-start teaches when and how to write code.
5. RL and GRPO-ATS refine decision-making, especially by separating text and code sampling temperatures.
6. Experiments show gains on perception, reasoning, and general tasks.
7. Failure cases reveal that tool-use decisions and crop grounding remain fragile.

## Cautionary points

- The paper’s performance claims rely heavily on Qwen2.5-VL-7B as the baseline; larger reasoning models still have advantages on some reasoning-heavy benchmarks.
- Some prompt templates use ground-truth boxes or angles during data construction while instructing the visible reasoning not to reveal them. This is useful for supervised behavior imitation but should be remembered when interpreting “autonomous” training traces.
- Final-answer accuracy can hide poor tool use, as shown by the inaccurate-cropping failure case.
- Existing benchmarks under-test rotation correction and low-contrast enhancement, so Thyme’s full capability set is not exhaustively evaluated.

