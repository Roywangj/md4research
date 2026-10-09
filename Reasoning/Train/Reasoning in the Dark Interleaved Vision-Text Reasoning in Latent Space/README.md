# Reasoning in the Dark: Interleaved Vision-Text Reasoning in Latent Space

- 分类: `Train`
- 分类理由: 先用完整显式 CoT 训练，再通过渐进式多阶段训练，把三个显式步骤逐步替换为潜在文本与潜在视觉的联合状态。
- Zotero item: `BY96Y7AI`
- Zotero PDF attachment: `EAWWASN8`
- PDF: [source](</Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/EAWWASN8/Chen 等 - 2026 - Reasoning in the Dark Interleaved Vision-Text Reasoning in Latent Space.pdf>)
- GitHub: [ModalityDance/IVT-LR](https://github.com/ModalityDance/IVT-LR)
- 精读: [paper_DeepPaperNote.md](Reasoning/Train/Reasoning%20in%20the%20Dark%20Interleaved%20Vision-Text%20Reasoning%20in%20Latent%20Space/paper_DeepPaperNote.md)
- 翻译: [paper.md](Reasoning/Train/Reasoning%20in%20the%20Dark%20Interleaved%20Vision-Text%20Reasoning%20in%20Latent%20Space/paper.md)
- Source map: [source_map.json](Reasoning/Train/Reasoning%20in%20the%20Dark%20Interleaved%20Vision-Text%20Reasoning%20in%20Latent%20Space/source_map.json)
- Translation notes: [translation_notes.md](Reasoning/Train/Reasoning%20in%20the%20Dark%20Interleaved%20Vision-Text%20Reasoning%20in%20Latent%20Space/translation_notes.md)

一句话概括: IVT-LR 把每个显式多模态 CoT 步骤压缩成“上一隐藏状态 + 当前选中图像嵌入”，用多阶段训练换取部署时更少的自回归解码。
