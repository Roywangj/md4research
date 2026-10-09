# PatchCue: Enhancing Vision-Language Model Reasoning with Patch-Based Visual Cues

- 分类: `Train`
- 分类理由: 论文明确训练 VLM：先用 cold-start SFT 学 patch-level cue，再用 GRPO 和过程监督 cue reward 优化中间视觉推理。
- Zotero item: `BBHEDHWA`
- PDF: [source](</Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/FJ9U6FIG/Qi 等 - 2026 - PatchCue Enhancing Vision-Language Model Reasoning with Patch-Based Visual Cues.pdf>)
- 精读: [paper_DeepPaperNote.md](Reasoning/Train/PatchCue%20Enhancing%20Vision-Language%20Model%20Reasoning%20with%20Patch-Based%20Visual%20Cues/paper_DeepPaperNote.md)
- 翻译: [paper.md](Reasoning/Train/PatchCue%20Enhancing%20Vision-Language%20Model%20Reasoning%20with%20Patch-Based%20Visual%20Cues/paper.md)
- Source map: [source_map.json](Reasoning/Train/PatchCue%20Enhancing%20Vision-Language%20Model%20Reasoning%20with%20Patch-Based%20Visual%20Cues/source_map.json)
- Translation notes: [translation_notes.md](Reasoning/Train/PatchCue%20Enhancing%20Vision-Language%20Model%20Reasoning%20with%20Patch-Based%20Visual%20Cues/translation_notes.md)

一句话概括: PatchCue 把视觉提示从像素级坐标变成 patch 级区域，让模型以更粗但更稳定的视觉 cue 参与中间推理。
