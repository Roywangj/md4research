---
tags:
  - papers/cad
  - papers/reinforcement-learning
  - train
aliases:
  - CReFT-CAD Deep Paper Note
---

# CReFT-CAD 深度精读笔记

## 核心信息
- 标题: CReFT-CAD: Boosting Orthographic Projection Reasoning for CAD via Reinforcement Fine-Tuning
- 标题翻译: 通过强化微调提升 CAD 正投影推理
- 作者: Ke Niu, Zhuofan Chen, Haiyang Yu, Yuwen Chen, Teng Fu, Mengyang Zhao, Bin Li, Xiangyang Xue
- 机构: 复旦大学
- 发表时间: 2025
- 发表渠道: NeurIPS 2025
- 论文类型: 视觉语言模型训练方法与基准

## 原文摘要翻译
论文提出 CReFT-CAD，通过两阶段微调提升 CAD 正投影推理：第一阶段使用带难度感知奖励的课程式强化学习，逐步建立推理能力；第二阶段使用监督后调优，改善指令遵循和语义提取。论文同时发布 TriView2CAD 基准，包含 200,000 个合成三视图样本、3,000 个真实世界样本、精确尺寸标注和六种可互操作数据模态。实验表明，CReFT-CAD 在正投影推理准确率和真实场景分布外泛化方面显著提升。

## 创新点
1. **课程驱动强化微调。** 将二元选择、多选和复合参数计算按难度递进组织，并为任务设计难度感知奖励。
2. **TriView2CAD 基准。** 将正投影理解从像素重建推进到尺寸、几何原语和跨视图逻辑推理。
3. **强化学习与监督后调优结合。** GRPO 负责建立推理策略，后续多任务 SFT 负责交互式 CAD 指令遵循。

## 一句话总结
CReFT-CAD 的关键不是让 VLM 记住更多图纸模板，而是用逐级任务和奖励把正投影推理拆成可优化的策略学习问题。

## 方法主线
### 机制流程
1. 输入三视图、参考图像与文字属性；模型识别尺寸、配对视图、计数原语并计算复合参数。
2. 使用 TriView2CAD 的 160,000 个合成图文指令对训练三类递进任务。
3. 通过 GRPO 和任务特定奖励优化输出正确性与推理轨迹。
4. 通过多任务 SFT 进一步改善指令遵循和语义抽取。

## 关键证据与结果
| 设置 | 最佳准确率 |
|---|---:|
| Qwen2.5-VL，无调优 | 38.88% |
| Qwen2.5-VL + SFT | 80.30% |
| CReFT-CAD | 84.03% |

消融实验显示，Task 1 + Task 2 + Task 3 加入 CoT 后准确率从 46.24% 提升到 81.35%；单独 Task 3 从 46.16% 提升到 74.15%。训练使用 8 张 A100、batch size 64、RL 学习率 $10^{-6}$、SFT 学习率 $2\\times10^{-5}$、GRPO 1500 steps。

## 局限性与边界
论文指出真实世界数据仅 3,000 个样本且全部保留作测试，因此 OOD 评估有价值但无法覆盖更广泛的工业分布；方法也依赖合成数据和精确标注，实际 CAD 图纸中的噪声、视图缺失和标注风格变化仍可能造成退化。上述结论来自论文的局限性与补充材料，不能外推为对所有工业 CAD 场景的保证。

## 复现要点
- 先固定三类任务的训练/采样顺序，再比较是否加入 CoT。
- 独立报告合成域内和真实世界 OOD，不要混合两者。
- 按四种 prompt configuration 复现结果，并保留 reasoning guidance 开关。

## 图表索引
- 图 1：无调优模型与 CReFT-CAD 的任务示例。
- 图 2：TriView2CAD 约束驱动合成流程。
- 图 4：三类课程任务。
- 表 1/3：VLM 基线比较；表 2：CoT 与任务组合消融；表 4：training-free、SFT 与 GRPO 比较。

## 来源边界
本笔记基于本地 23 页 PDF 及 `plan/creft_cad_*` 提取工件；完整段落对照见 `detailed_paper.md`，稳定页码/块 ID 见 `source_map.json`。
