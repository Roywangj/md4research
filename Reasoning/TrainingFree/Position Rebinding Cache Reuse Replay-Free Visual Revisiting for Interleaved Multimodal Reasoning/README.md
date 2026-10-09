# Position Rebinding Cache Reuse: Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning

- 分类: `TrainingFree`
- 分类理由: 方法在 KV cache 层复用历史视觉证据并做 position rebinding，不训练模型参数，主要解决 replay-free visual revisiting 的效率和位置一致性。
- Zotero item: `IBQ6CTBU`
- PDF: [source](</Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/TA2B3XTE/Wang 等 - 2026 - Position Rebinding Cache Reuse Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning.pdf>)
- 精读: [paper_DeepPaperNote.md](Reasoning/TrainingFree/Position%20Rebinding%20Cache%20Reuse%20Replay-Free%20Visual%20Revisiting%20for%20Interleaved%20Multimodal%20Reasoning/paper_DeepPaperNote.md)
- 翻译: [paper.md](Reasoning/TrainingFree/Position%20Rebinding%20Cache%20Reuse%20Replay-Free%20Visual%20Revisiting%20for%20Interleaved%20Multimodal%20Reasoning/paper.md)
- Source map: [source_map.json](Reasoning/TrainingFree/Position%20Rebinding%20Cache%20Reuse%20Replay-Free%20Visual%20Revisiting%20for%20Interleaved%20Multimodal%20Reasoning/source_map.json)
- Translation notes: [translation_notes.md](Reasoning/TrainingFree/Position%20Rebinding%20Cache%20Reuse%20Replay-Free%20Visual%20Revisiting%20for%20Interleaved%20Multimodal%20Reasoning/translation_notes.md)

一句话概括: PRCR 发现直接复用旧视觉 KV cache 会因位置绑定过期而出错，于是重绑位置后注入当前解码缓存，降低重复视觉回放成本。
