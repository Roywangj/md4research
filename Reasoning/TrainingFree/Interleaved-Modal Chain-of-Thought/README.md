# Interleaved-Modal Chain-of-Thought

- 分类: `TrainingFree`
- 分类理由: Attention-driven Selection 只使用现有 VLM 的 attention map 选择图像局部作为 visual rationales，论文称其不需要 parameterization，是 plug-and-play / training-free 策略。
- Zotero item: `LKAFNEE6`
- PDF: [source](</Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/DMT6SNMT/Gao 等 - 2025 - Interleaved-Modal Chain-of-Thought.pdf>)
- 本地阅读: [精读](<Reasoning/TrainingFree/Interleaved-Modal Chain-of-Thought/paper_DeepPaperNote.md>) / [翻译](<Reasoning/TrainingFree/Interleaved-Modal Chain-of-Thought/paper.md>) / [source map](<Reasoning/TrainingFree/Interleaved-Modal Chain-of-Thought/source_map.json>)

一句话概括: ICoT 将中间推理从纯文本 rationale 改成图像局部 + 文本 rationale 的交错序列，让模型更明确地把每一步推理绑定到原图证据。
