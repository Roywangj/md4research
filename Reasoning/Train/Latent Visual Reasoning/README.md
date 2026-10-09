# Latent Visual Reasoning

- 分类: `Train`
- 分类理由: 方法通过 ROI 视觉标记监督的 SFT 学习潜在视觉状态，并进一步使用 `GRPO_latent` 优化潜在状态与文本答案的耦合，需要更新模型参数。
- Zotero item: `ABAL4CZP`
- PDF: [source](</Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/WP65QDXJ/Li 等 - 2025 - Latent Visual Reasoning.pdf>)
- 完整双语读本: [paper.md](<Reasoning/Train/Latent Visual Reasoning/paper.md>)
- 全文双语详读: [detailed_paper.md](<Reasoning/Train/Latent Visual Reasoning/detailed_paper.md>)
- 精读笔记: [paper_DeepPaperNote.md](<Reasoning/Train/Latent Visual Reasoning/paper_DeepPaperNote.md>)
- 翻译说明: [translation_notes.md](<Reasoning/Train/Latent Visual Reasoning/translation_notes.md>)

一句话概括: LVR 让语言模型在隐藏空间中自回归重建与问题相关的视觉标记，再恢复文本解码；它强化的是初始视觉编码中已有的证据，而不是通过工具获取新的像素信息。
