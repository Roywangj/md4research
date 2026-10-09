# Mitigating Low-Quality Reasoning in MLLMs

- 分类: `TrainingFree`
- 分类理由: 正文明确称 SDR-MCoT 完全 training-free；它用熵置信度选择是否进行长推理，并在每个推理步骤增强相关视觉 patch 的注意力。
- Zotero item: `95JR5SU4`
- PDF: [source](</Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/TTWS8WL8/Mitigating Low-Quality Reasoning in MLLMs Self-Driven Refined Multimodal CoT with Selective Thinkin.pdf>)
- 精读: [paper_DeepPaperNote.md](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/paper_DeepPaperNote.md)
- 翻译: [paper.md](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/paper.md)
- Source map: [source_map.json](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/source_map.json)
- Translation notes: [translation_notes.md](Reasoning/TrainingFree/Mitigating%20Low-Quality%20Reasoning%20in%20MLLMs%20Self-Driven%20Refined%20Multimodal%20CoT%20with%20Selective%20Thinking%20and%20Step-wise%20Visual%20Enhancement/translation_notes.md)

一句话概括: SDR-MCoT 同时处理过度思考和视觉利用不足：简单题直接答，复杂题才进入带 step-wise visual enhancement 的 CoT。
