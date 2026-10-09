# Translation Notes for InternW0-Δ

## Scope and Source

- **Source Document:** arXiv:2609.31394v1 [cs.RO], 25 Sep 2026.
- **Local PDF File:** `/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/PSJ9YU3M/Miao 等 - 2026 - InternW0-$Δ$ A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open.pdf`
- **Output Target:** `detailed_paper.md` and identical `paper.md` in the target directory.
- **Scope Covered:** Full paper from Abstract to Section 9 (Team), References, and Appendix A (Human-to-Robot IK Details).

## Terminology Ledger and Conventions

- **World Action Model (WAM)**: 译为“世界动作模型”，联合建模视觉动力学与机器人连续动作生成的具身基座模型范式。
- **Causal Imprint (CI / $\Delta$)**: 译为“因果印记”，紧凑隐层差分表征与未来物理对齐向量，用于测试期免自回归视频生成下的动作引导。
- **Mixture-of-Transformers (MoT)**: 译为“Transformer 混合架构”，视频生成专家与动作生成专家的双流解耦与定向交互结构。
- **4D-Aware Representation Distillation**: 译为“4D 动态感知表征蒸馏”，利用点轨迹追踪（Track4World）将连续空间几何与运动场先验注入模型。
- **Canonical 80-D State-Action Space**: 译为“规范化 80 维状态-动作空间”，统一双臂、末端、夹爪、灵巧手与底盘的通用高维物理动作空间。
- **Ego2Robot**: 译为“人类第一人称向机器人动作重定向流水线”，采用阻尼伪逆零空间约束与虚拟接触点对齐算法。
- **Real-Time Chunking (RTC)**: 译为“实时分块执行算法”，解决异步高频重规划中的动作突变跳跃（Action Jetting）物理冲击。
- **Action Jetting**: 译为“动作突变跳跃 / 动作喷涌”，相邻动作分块交界处的位移不连续现象。
- **Feature Caching**: 译为“特征离线缓存机制”，消除了重复图像与语言前向计算，提速 4.2 倍。
- **Layerwise MoT Compilation**: 译为“逐层 MoT 模块化编译”，降低 38% 训练峰值显存。

## Asset and Crop Caveats

- All 12 figures (`figure_1.png` to `figure_12.png`) and 18 tables (`table_1.png` to `table_18.png`) were cropped directly from the original PDF at 250 DPI.
- High-resolution copies are deposited into both `assets/` (for translation readers) and `images/` (for the deep reading note).
- Tables I–XVIII are transcribed into clean, searchable Markdown tables alongside their image crops, ensuring full text searchability in Obsidian.
- All display math equations (Equations 1 to 29) are formatted outside blockquotes using `$$...$$` to guarantee flawless rendering in Markdown engines.
