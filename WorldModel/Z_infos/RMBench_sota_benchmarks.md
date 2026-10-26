---
tags:
  - papers/WorldModel
  - RMBench
  - benchmark
  - memory
  - paper-comparison
  - long-horizon
aliases:
  - RMBench SOTA 与 Insight 对比
date: 2026-08-05
last_updated: 2026-10-26
status: synthesis
---

# RMBench SOTA、长程任务语言规划与前沿 Insight 全景对比

> [!tip] 核心问题诊断与作者实操建议
> **你遇到的现象**：“目前基于 ImageWAM (FLUX.2 骨干) 做开发，在 RMBench 长程任务中把标注里的 GT 子任务句拼进 prompt 作为 DiT 的文本条件去学动作，基本上没啥用偶尔还会掉点。有没有推荐的『VLM 规划子任务 → 底层 WAM / policy 只执行当前子任务』的做法？”
>
> **为什么直接拼 GT 子任务文本会掉点？**
> 1. **语义与几何的粒度脱节（Semantic-Geometric Gap）**：DiT 动作专家对毫米级的空间坐标、旋转角度、接触点及夹爪开合极其敏感；而 T5/FLUX 的文本 embedding 属于高度抽象的高层粗语义。单纯在 Cross-Attention 注入文本，并不能提供精细的三维物理几何对齐。
> 2. **阶段状态混淆与死循环（State Aliasing & Phase Indistinguishability）**：长程任务（如 *Press Button*, *Swap Blocks*）中，在接近按钮、下压接触、回弹撤离这三段过程中，相机视觉极其相似，但数据标注给出的当前 `subtask_text` 全都是同一句话（如 `"press red button"`）。马尔可夫单帧策略只看到静态文本，**根本不知道自己处于动作的前半段还是后半段**，导致策略在接触面附近剧烈震荡、陷入无限死循环（[MaP-WAM](<../Memory as Plans World-Action Modeling with Memory-Grounded Planning/paper_DeepPaperNote.md>) 的消融实验严谨证实：若没有连续进度 $p_t$ 约束，*Press Button* 成功率直接从 96% 断崖式跌至 18%！）。
> 3. **训练-推理暴露偏差（Exposure Bias）与文本过敏**：训练时 GT 子任务随着帧精确硬切，测试时若没有针对 prompt 的 Dropout / CFG 机制，动作头会严重过拟合于文本的特定先验，一旦视觉轻微扰动便丧失鲁棒的视觉伺服闭环能力。
>
> **学术界最高效的解法路径推荐**：
> - **首选必读（机制完美契合你的痛点）**：[MaP-WAM (Memory as Plans)](<../Memory as Plans World-Action Modeling with Memory-Grounded Planning/paper_DeepPaperNote.md>)（哈工大 & NTU，2026.09）。提出“记忆即计划”，宏观切换时由世界模型一次性将长程记忆编译为未来的**视觉方案（Visual Plan）+ 语言子目标**；底层动作执行器**完全不读冗长历史**，以静态视觉方案为前缀，由动作专家 + 进度专家联合输出动作与连续进度 $p_t \in [0, 1]$，配合计划—观测自适应校准。在 RMBench 斩获 **83.3%** 总体 SOTA（$M(n)$ 高达 **96.7%**），推理延迟恒定为 ~827ms，彻底解决 80GB OOM 崩溃！
> - **端到端多模态交织推荐**：[WLA (World-Language-Action)](<../World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis/paper_DeepPaperNote.md>)（2026）。在生成动作前，必须让模型显式自回归预测当前子任务文本，将语言作为可读写的离散阶段进度状态，切除语言预测损失后 $M(n)$ 均值从 56.5% 暴跌至 17.3%。
> - **分层编排与外挂智能体推荐**：[Towards Agentic Robots](<../Towards Agentic Robots Model, Data, Environment, and Harness/paper_DeepPaperNote.md>)、[HarnessWAM](<../HarnessWAM Bridging Prediction and Deliberation in World Action Models/paper_DeepPaperNote.md>) 与 [VoLo](<../VoLo A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation/paper_DeepPaperNote.md>)。外层由慢思考 Agent（Harness）调度记忆并验证完成谓词，底层调用冻结的快思考 WAM/VLA 原语执行。
> - **代码记忆与神经解耦推荐**：[Skills in Weights, Memory in Code (HyMeS)](<../Skills in Weights, Memory in Code Hybrid Learning for Memory-Dependent Robot Manipulation/paper_DeepPaperNote.md>)。底层物理控制固化在网络权重中，长时程的离散试错与记忆字典全部放在 Python 代码空间中管理。

---

# 一、RMBench 相关论文实验与 Insight 对比

> [!abstract] 核心结论先行
> 对本代码库 73+ 篇论文进行全景排查与实质实验审计，涉及 RMBench 真实实验与深度基准审计的代表性工作共 **8 篇**：
>
> - **总体最高分**：[MaP-WAM](<../Memory as Plans World-Action Modeling with Memory-Grounded Planning/paper_DeepPaperNote.md>) 达到 **83.3%**（$M(n)$ 均值高达 **96.7%**，在最难的 *Press Button* 达到 96%、*Cover Blocks* 达到 100%），且消除了因果窗口 OOM 与时延线性暴涨的致命瓶颈。
> - **此前最高报告值**：[MemoryWAM](<../MemoryWAM Efficient World Action Modeling with Persistent Memory/paper_DeepPaperNote.md>) 报告总体 **83.0%**（$M(n)$ 均值 81.5%），采用 Gist KV-Cache + Anchor + Sliding Window，但缓存随时间非定长增加且非完全等价 backbone 对齐。
> - **基准重大审计与缺陷揭露**：[EventVLA](<../EventVLA Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies/paper_DeepPaperNote.md>) 与 [DiM-WAM](<../DIM-WAM World-Action Modeling with Diverse Historical Event Memory/paper_DeepPaperNote.md>) 深入审计了 RMBench，揭露该基准存在严重的**“初始帧偏见泄漏”**与**“腕部相机位姿泄漏”**——仅靠任务第 0 步的初始视觉锚点（VA only），成功率就高达 **67.8%**（远超双系统 Mem-0 的 42.0%）。这促使领域向具备真实非马尔可夫长程依赖的 [RoboMemArena](<../RoboMemArena A Comprehensive and Challenging Robotic Memory Benchmark/paper_DeepPaperNote.md>) 演进。
> - **记忆架构演进主线**：**显式分层记忆 (Mem-0) $\to$ 语言化进度记忆 (WLA) $\to$ 多保真度视觉缓存 (MemoryWAM) $\to$ 有界多样事件记忆 (DiM-WAM) $\to$ 记忆编译为视觉方案+微观进度闭环 (MaP-WAM)**。

---

## 1. 全库涉及 RMBench 的代表性工作筛选

| 论文 / 模型 | RMBench 实验范围与协议 | 核心机制与架构 | 关联交付文档 |
|---|---|---|---|
| **[RMBench (Mem-0)](<../RMBench Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design/paper_DeepPaperNote.md>)** | 全部 9 任务：5 个 $M(1)$ + 4 个 $M(n)$ | 提出 Benchmark；双系统 Mem-0（Anchor + Sliding + Key 记忆 + 终止分类器） | [精读](<../RMBench Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design/paper_DeepPaperNote.md>) · [翻译](<../RMBench Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design/paper.md>) |
| **[WLA (WLA-0)](<../World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis/paper_DeepPaperNote.md>)** | 仅评测 4 个 $M(n)$ 任务 | 统一世界动作语言模型；将子任务语言作为多模态流中自回归预测的离散进度状态 | [精读](<../World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis/paper_DeepPaperNote.md>) · [翻译](<../World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis/paper.md>) |
| **[MemoryWAM](<../MemoryWAM Efficient World Action Modeling with Persistent Memory/paper_DeepPaperNote.md>)** | 全部 9 任务 | 混合保真度持久缓存：Anchor 帧 + Sliding 窗口 + 逐帧轻量 Gist KV 缓存 | [精读](<../MemoryWAM Efficient World Action Modeling with Persistent Memory/paper_DeepPaperNote.md>) · [翻译](<../MemoryWAM Efficient World Action Modeling with Persistent Memory/paper.md>) |
| **[DiM-WAM](<../DIM-WAM World-Action Modeling with Diverse Historical Event Memory/paper_DeepPaperNote.md>)** | 全部 9 任务；审计后调整相机与步幅协议 | 多样性历史事件记忆（DHEM）：多库并行、新颖性淘汰、相邻事件质量加权合并 | [精读](<../DIM-WAM World-Action Modeling with Diverse Historical Event Memory/paper_DeepPaperNote.md>) · [翻译](<../DIM-WAM World-Action Modeling with Diverse Historical Event Memory/paper.md>) |
| **[MaP-WAM (Memory as Plans)](<../Memory as Plans World-Action Modeling with Memory-Grounded Planning/paper_DeepPaperNote.md>)** | 全部 9 任务 + Franka 实体真机实测 | “记忆即计划”解耦范式：因果世界模型生成 Visual Plan，底层执行器接收计划与连续进度 $p_t$，彻底打破 OOM | [精读](<../Memory as Plans World-Action Modeling with Memory-Grounded Planning/paper_DeepPaperNote.md>) · [翻译](<../Memory as Plans World-Action Modeling with Memory-Grounded Planning/paper.md>) |
| **[BridgeVLA++](<../BridgeVLA++ A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework/paper_DeepPaperNote.md>)** | 全部 9 任务（每任务单独训练 50 演示） | 粗阶段注入时序进度记忆，细阶段注入少遮挡几何空间记忆，报告 96.0% 最佳 checkpoint | [精读](<../BridgeVLA++ A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework/paper_DeepPaperNote.md>) · [翻译](<../BridgeVLA++ A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework/paper.md>) |
| **[EventVLA](<../EventVLA Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies/paper_DeepPaperNote.md>)** | 基准审计与测试 | 提出关键帧事件记忆（KEM）；揭露 RMBench 仅靠 $o_0$ 初始帧即达 67.8% 的泄漏问题 | [精读](<../EventVLA Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies/paper_DeepPaperNote.md>) · [翻译](<../EventVLA Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies/paper.md>) |
| **[SimpleMemVLA](<../SimpleMemVLA A Simple but Effective Native-Video Memory for Vision-Language-Action Models/paper_DeepPaperNote.md>)** | 记忆策略比对 | 探索无复杂启发式规则的原生视频长程记忆流 | [精读](<../SimpleMemVLA A Simple but Effective Native-Video Memory for Vision-Language-Action Models/paper_DeepPaperNote.md>) · [翻译](<../SimpleMemVLA A Simple but Effective Native-Video Memory for Vision-Language-Action Models/paper.md>) |

---

## 2. 作者报告结果账本与横向比对

以下成功率（%）均严格摘自各篇论文实验表。**由于不同工作使用的基座规模、是否输入动作历史、相机视角与采样步幅存在审计差异，表格用于定位各方案的机制优势，而非单维度的绝对排位**。

### 2.1 整体综合指标对比

| 论文 / 方法 | 基座架构与参数 | $M(1)$ 均值 | $M(n)$ 均值 | 九任务总体 | 关键同文基准与消融变化 | 可比性与协议说明 |
|---|---|---:|---:|---:|---|---|
| **RMBench / Mem-0** | 双系统 (LLaVA-1.5 + DP) | 52.8 | 28.5 | 42.0 | 对比 $\pi_{0.5}$ 总体仅 10.4 | 原始基准协议；$M(n)$ 强依赖模拟器阶段判定与外部终止分类器 |
| **WLA / WLA-0** | 统一自回归 WLA | — | **56.5** | — | 去掉语言预测损失：56.5 $\to$ 17.3 | 仅评测 4 个 $M(n)$ 任务；每任务训练 30k 步 |
| **MemoryWAM** | LingBot-VA + Gist 机制 | 84.2¹ | **81.5¹** | **83.0** | 对比 LingBot-VA 78.2；去掉 Gist，Press Button 降至 5 | 总体 83.0；Swap T 额外注入动作历史，Observe & Pick 采用预训练 |
| **DiM-WAM** | LingBot-VA + DHEM 记忆 | **80.6** | **56.3** | **69.8** | 严格训练匹配 LingBot-VA：34.8 $\to$ 69.8 | 发现位姿泄漏后收紧相机与采样步幅（严格审计版协议） |
| **MaP-WAM (Memory as Plans)** | WAN-2.2-5B + 1B 动作专家 | **72.6** | **96.7** | **83.3** | 去掉进度条件：Press Button 96 $\to$ 18；去对齐 94 $\to$ 38 | 全九任务，单块时延稳定在 ~827ms，彻底规避 80GB 显存 OOM 崩溃 |
| **EventVLA (VA only)** | Qwen3-VL-4B + StarVLA | — | — | **67.8** | 仅依赖初始帧视觉锚点，超越 Mem-0 25.8% | 基准审计实验：证明 RMBench 绝大多数任务存在初始帧泄漏 |

> ¹ MemoryWAM 论文正文报告总体 83.0；84.2 与 81.5 是根据论文 Table 1 的五个 $M(1)$ 和四个 $M(n)$ 逐项成功率重算得出。

---

### 2.2 核心长程 $M(n)$ 任务逐项表现深挖

$M(n)$ 任务必须在交互过程中多次跨时间步累积或更新历史线索，最能暴露出不同记忆与规划机制的本质瓶颈：

| 方法 | Battery Try<br>*(电池极性与插槽探索)* | Blocks Ranking Try<br>*(盲测重力并排序积木)* | Cover Blocks<br>*(杯子完全遮盖后位置)* | Press Button<br>*(多色按钮时序连续按压)* | $M(n)$ 平均 | 架构偏好与机理解读 |
|---|---:|---:|---:|---:|---:|---|
| **Mem-0** | 28 | 18 | 68 | 0 | 28.5 | 纯语言日记丢失几何接触细节，按钮按压彻底瘫痪（0%）。 |
| **WLA-0** | 45 | 23 | 84 | 74 | 56.5 | 离散语言程序状态对有明确计数与顺序的任务（按按钮、盖积木）极强。 |
| **MemoryWAM** | 41 | **100** | 98 | 87 | 81.5 | 连续高保真视觉锚点 + 过程 Gist 缓存，视觉记忆全面覆盖。 |
| **DiM-WAM** | 48 | 87 | 56 | 34 | 56.3 | 多库新颖性事件筛选对多阶段试错（Ranking Try）极其擅长。 |
| **MaP-WAM** | **82** | 94 | **100** | **96** | **96.7** | **统治级表现**：宏观 Visual Plan 消除盲猜，微观连续进度 $p_t$ 彻底解决死循环。 |

---

## 3. 各代表作的核心 Insight 与技术演化

### 3.1 RMBench (Mem-0)：定义长程记忆复杂度与诊断职责
- **贡献**：首次在具身操作中形式化定义了任务记忆复杂度：$M(1)$（只需单次关键历史帧，但当前帧不可见）与 $M(n)$（需跨交互多步动态累积历史）。
- **痛点暴露**：长程任务失败往往不是机器人“忘了”，而是**“不知道当前子任务何时结束、何时该切换阶段”**。当赋予 Mem-0 仿真器真值终止信号时，$M(n)$ 成功率从 28.5% 跃升至 45.3%，证明终止检测是规划闭环的致命瓶颈。

### 3.2 WLA：将语言子任务视为可读写的离散阶段进度状态
- **核心机制**：不把语言当成单向静态提示词，而是在多模态流中，要求模型在去噪动作前先自回归预测当前应当执行的文本子任务：$p(\text{subtask}_k \mid h) \to p(\text{action} \mid h, \text{subtask}_k)$。
- **消融证据**：一旦移除语言监督损失，模型在 Cover Blocks 上从 84% 暴跌至 18%，Press Button 从 74% 暴跌至 1%！这表明**离散程序状态与动作生成必须保持动态同步**。

### 3.3 MemoryWAM：按信息保真度分层压缩视觉流，而非全存或全丢
- **核心机制**：初始事件保留无损 Anchor 帧，近期局部保留完整 Sliding 窗口，更早历史逐帧提取压缩为极少量的 Gist Tokens 并追加进持久 KV 缓存。动作专家直接 cross-attend 视频侧 KV 缓存，无需测试期生成未来视频。
- **局限**：Gist Token 仍然是逐帧线性追加（$O(N/d)$），在超长序列下仍存在上下文增长与键值混淆问题。

### 3.4 DiM-WAM：固定预算下的事件选择与合并（DHEM）
- **核心机制**：抛弃无界追加，设置多个固定容量的有界记忆库（Memory Banks）。从当前观测抽取候选事件，通过计算特征余弦相似度度量新颖性，容量饱和时淘汰最旧冗余帧，并按质量加权合并相邻事件。
- **基准治理发现**：作者率先发现 RMBench 的 $M(1)$ 任务中，仅开启机械臂腕部相机就会导致初始位置泄漏（通过机械臂初始姿态反算），因此严格规范了相机评测协议。

### 3.5 MaP-WAM：具身控制新范式——“记忆即计划”（Memory as Plans）
- **破解核心矛盾**：以往因果世界模型（如 LingBot-VA）试图“生吞所有历史帧”，导致输入序列 $T$ 激增。实测在 1,700 帧时显存直接冲破 **80GB 发生 OOM 崩溃**，推理延迟随 $O(T^2)$ 飙升。
- **创新解耦设计**：
  1. **宏观阶段规划器（CWM）**：仅在阶段边界被唤醒，利用稀疏长期关键帧与指令，由因果视频扩散模型前瞻生成包含未来 8 帧几何与物体演变的 **Visual Plan（视觉方案）**。
  2. **微观执行器（WAP）**：底层动作执行器**完全不读过去的视频历史**，仅以生成的静态 Visual Plan 为条件运行；
  3. **任务进度一等公民化**：引入 207M 进度专家，实时联合预测动作与连续进度标量 $p_t \in [0, 1]$。当夹爪下压与回弹画面极度相似时，连续进度为策略提供了明确的单向物理时钟，彻底根治了死循环！
  4. **工程优势**：单块去噪延迟恒定钉死在 **~827ms**，显存处于恒定平直低位，彻底解除长程任务步数限制。

### 3.6 EventVLA：基准审计风暴——揭露 RMBench 的“初始帧偏见”
- **颠覆性发现**：作者通过对 RMBench 的系统审计指出，该基准绝大多数任务根本不需要复杂的动态瞬态记忆！例如在 *Rearrange Blocks* 或 *Put Back Block* 中，目标方块的位置在任务第 0 步就已经静态摆在桌面上。策略只要记住初始帧 $o_0$（提供静态参考），加上局部滑窗即可通过。
- **实证证据**：仅靠最基础的视觉锚点（VA only，记住 $o_0$），在 RMBench 就能刷出 **67.8%** 的超高成功率，远超很多精心设计的复杂记忆模型。这直接促成了具身智能领域向覆盖更多交互状态翻转、非马尔可夫强依赖的 **[RoboMemArena](<../RoboMemArena A Comprehensive and Challenging Robotic Memory Benchmark/paper_DeepPaperNote.md>)** 迁移。

---

## 4. 四大记忆与长程规划流派横向对比

| 维度 | 显式分层记忆 (Mem-0) | 语言化离散进度 (WLA) | 多保真度视觉缓存 (MemoryWAM) | 有界事件流 (DiM-WAM) | 记忆即计划 (MaP-WAM) |
|---|---|---|---|---|---|
| **记忆承载模态** | 图像关键帧 + 语言日记 | 自回归文本 Token | 完整 KV + 逐帧 Gist KV | 多库稀疏事件 Token | 预生成的未来视觉方案 (8 帧) + 连续标量进度 |
| **底层执行器负担** | 中等（需检索与分类） | 随文本长度微弱增长 | 随步数线性增加 KV 缓存 | 固定常数 Token 预算 | **极低（完全不读历史帧，延迟恒定 ~827ms）** |
| **解决死循环机制** | 外部终止分类器（易成单点故障） | 离散子任务重推断 | 依赖高维隐式表征区分 | 进度头粗粒度辅助 | **连续进度模态 $p_t$ 显式时序校准** |
| **微观几何保真度** | 低（语言日记丢失厘米级位姿） | 低（纯文本无法指导微观对齐） | 极高（完整连续视觉表征） | 高（保留关键视觉事件） | **极高（具备 3D 几何与外观的未来视觉方案）** |
| **防 OOM 极限能力** | 良好 | 优异 | 差（超长序列下显存持续攀升） | 优异（固定 $K \times N$ 槽位） | **最优（执行期显存完全恒定，彻底打破 OOM）** |

---

## 5. 对 ImageWAM / Fast-WAM 开发者的落地实操路线建议

结合你在 ImageWAM（FLUX.2 骨干）上解决 RMBench 长程任务的困惑，建议采取以下三步演进：

1. **切断“仅将子任务文本塞进 prompt”的纯文本依赖**：
   - 必须引入**阶段进度信号**。最快见效的低成本改法是参考 [MaP-WAM](<../Memory as Plans World-Action Modeling with Memory-Grounded Planning/paper_DeepPaperNote.md>)，在动作预测头并行增加一个 1~2 层的轻量级进度头，监督当前窗口归一化进度 $p_t = t / T_{\text{subtask}} \in [0, 1]$，并将 $p_t$ 经过正弦位置编码后与时间步 $t_{\text{diff}}$ 相加注入 DiT 的 Adaptive LayerNorm 中。这能立刻打破下压/回弹时的动作对称死循环。
2. **构建“视觉锚点 + 目标视觉想象”双条件**：
   - 鉴于 EventVLA 揭示的 RMBench 规律，在输入中**必须常驻任务初始帧 $o_0$（或子任务开始时的第一帧）作为 Visual Anchor**。对于 FLUX.2 这类图像生成底座，让其从 $o_0$ 和当前帧 $o_t$ 预测子任务结束时的关键帧目标图像（Goal Image Editing），再由动作头条件化于该目标图像，其效果远优于纯文本条件。
3. **宏观阶段解耦（走向真正的分层智能体）**：
   - 若做长程多阶段组合，推荐采用 [Towards Agentic Robots](<../Towards Agentic Robots Model, Data, Environment, and Harness/paper_DeepPaperNote.md>) / [HarnessWAM](<../HarnessWAM Bridging Prediction and Deliberation in World Action Models/paper_DeepPaperNote.md>) 的思路：高层调用 VLM 只在子任务切换时做决策，底层 ImageWAM 只负责将当前子任务的高保真视觉演化和动作 chunk 解算出来，两层之间通过明确的完成度阈值或进度阈值（如 $p_t > 0.95$）触发切换，切忌在每步高频控制中强行调用高层大模型。
