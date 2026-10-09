# Translation Notes

- 源文件: `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/4Z8DAYXR/Wang 等 - 2026 - Beacon Knowing When and How to Perform Agentic Visual Reasoning.pdf`
- 源格式: `pdf-text`，34 页；正文文本可选择，不是扫描件。
- 阅读模式: `wj-reading` 全文双语 reader + `nature-reader-detail` 段落级结构 + DeepPaperNote 分析笔记。
- 论文归类: `Reasoning/Train`。
- 归类依据: 方法以 Qwen3-VL-8B-Instruct 为基座，明确执行 cold-start SFT 与 GRPO 强化学习；NAAR、HCE 都属于训练阶段机制，不是只在测试时工作的提示或搜索框架。

## 术语约定

- Mode Adaptiveness: 模式适应性。
- Tool Effect: 工具效应。
- Tool-Gain / Tool-Harm: 工具增益 / 工具伤害。
- Necessity-Aware Adaptive Reward: 必要性感知自适应奖励。
- Hint-Guided Capability Expansion: 提示引导能力扩展。
- text-easy / text-hard: 保留英文短标签，解释为纯文本稳定可解 / 稳定难解。
- rollout、policy、prompt、token、SFT、RL、GRPO: 在不影响理解处保留研究社区常用形式。

## 公式与数值

- MA 与 Tool Effect 公式按原文含义重排为标准 LaTeX；原 PDF 文本抽取会丢失部分分数线和求和上下标，因此以版面和上下文联合核对。
- Tool-Gain 与 Tool-Harm 均按全部测试样本数 `N` 归一化，不解释为 text-hard 或 text-easy 子集内部准确率。
- 关键平均数同时与 Figure 2、Table 3、Table 4、Table 6 和正文描述交叉核验。

## 图表处理

- 共保留并嵌入 23 个 Figure/Table 素材，分别放在 `assets/` 与 `images/`，服务于双语 reader 和 DeepPaperNote。
- 自动抽取的 Table 2 区域错误，已从 PDF 第 10 页渲染图重新裁剪，并覆盖两个素材目录中的对应文件。
- Table 4 在第 11–12 页存在标题/表体跨页抽取问题；`detailed_paper.md` 使用第 12 页表体素材，并在正文转写关键平均数。
- Tables 7–12 是整页案例表，保留原图以维持图像、问题、轨迹和 hint 的版面关系；正文提供中文可搜索解释。

## 附录与提示词

- Prompt Box 1–5 均被覆盖。
- 对超长 Prompt Box 2、3、5，保留协议关键字、严格输出结构、操作标签和原始字面要求；相邻中文段落解释其训练作用。
- 训练配置覆盖 SFT epoch/学习率/优化设置，以及 RL GPU、rollout、batch、序列长度、工具调用和专家 hint 预算。

## 覆盖与边界

- 主文 Abstract、Introduction、Related Work、Analysis、Method、Experiments、Conclusion 全部覆盖。
- 附录 A–F 覆盖评测、数据、训练、详细消融、失败尝试、推理轨迹与提示案例。
- 参考文献 [1]–[49] 不逐条翻译；其精确书目字符串保留在原 PDF，笔记中只综合与论文论证有关的工作脉络。
- 论文为 2026-07-30 发布的 arXiv v1，并标注 `Preprint. Work in progress.`；阅读笔记以该版本为准。
- 当前没有使用 Zotero 本地 API 元数据写回；给定的 Zotero storage PDF 路径作为 canonical source。
