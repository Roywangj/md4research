# Let's Think with Images Efficiently! An Interleaved-Modal Chain-of-Thought Reasoning Framework with Dynamic and Precise Visual Thoughts

> **中文题名：** 让我们高效地用图像思考：带有动态与精确视觉思考的交错模态思维链推理框架  
> **作者：** Xu Liu, Yongheng Zhang, Qiguang Chen, Yao Li, Sheng Wang, Libo Qin  
> **出处：** arXiv:2603.21754v1，2026-03-23  
> **论文类型：** 方法 / training-free multimodal reasoning / efficient interleaved visual CoT  
> **源文件：** `Liu 等 - 2026 - Let's Think with Images Efficiently! An Interleaved-Modal Chain-of-Thought Reasoning Framework with.pdf`  
> **阅读器：** 9 页完整英中对照详细阅读稿；覆盖公式 (1)–(8)、完整主结果表、Figures 1–8、定性案例、致谢与原始可检索参考文献。

## Page / Section Index

- Abstract: page 1
- Introduction: pages 1-3
- DaP-ICoT Reasoning: pages 3-5
- Experiments and Analysis: pages 4-7
- Related Work: page 7
- Conclusion: pages 7-8
- References: pages 8-9

## Terminology Ledger

| Canonical term | 中文 | First-use decision |
|---|---|---|
| Interleaved-modal Chain-of-Thought | 交错模态思维链 | 保留 ICoT 缩写 |
| DaP-ICoT / DAP-ICOT | 动态精确视觉思考的 ICoT | 正文统一写 DaP-ICoT |
| Dynamic Visual Thought Integration | 动态视觉思考集成 | 保留 DVTI 缩写 |
| Precise Visual Thought Guidance | 精确视觉思考引导 | 保留 PVTG 缩写 |
| visual thought | 视觉思考 | 指推理中插入的视觉内容 |
| static visual thought positioning | 静态视觉思考定位 | 指每一步固定插入图像 |
| broken visual thought representation | 破碎视觉思考表示 | 指离散、不连贯的视觉标记 |
| logit margin | logit 间隔 | 用 top-1 与 top-2 logit 差估计置信度 |
| object-level selection | 对象级选择 | 由 SAM2 分割候选对象后选择 |
| token consumption | 标记消耗 | 中文正文尽量用“标记” |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Recent ICoT reasoning methods improve multimodal reasoning by mixing visual and textual reasoning outputs, but they still insert visual information in a fixed pattern and often use fragmented visual tokens.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 近期 ICoT 方法通过混合视觉与文本推理输出来提升多模态推理，但它们仍然以固定模式插入视觉信息，而且常使用破碎、不连贯的视觉标记。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The paper proposes DaP-ICoT, which contains Dynamic Visual Thought Integration for deciding when visual input is needed and Precise Visual Thought Guidance for selecting semantically coherent visual content.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 论文提出 DaP-ICoT。它包含两个组件：动态视觉思考集成用于判断何时需要视觉输入，精确视觉思考引导用于选择语义完整且与当前推理相关的视觉内容。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Across multiple benchmarks and models, DaP-ICoT reports state-of-the-art results while reducing inserted images and cutting token consumption by 72.6%.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 在多个基准和模型上，DaP-ICoT 报告了领先结果，同时减少插入图像数量，并将标记消耗降低 72.6%。

## 1. Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Multimodal large language models and multimodal CoT have improved reasoning over complex real-world tasks. A common limitation, however, is that the input is multimodal while the reasoning trace remains text-only.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 多模态大语言模型和多模态思维链已经提升了复杂真实任务中的推理能力。但常见限制是：输入是多模态的，中间推理轨迹却仍主要是纯文本。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> ICoT tries to overcome this limitation by allowing the model to reason with both visual and textual outputs, so that visual thoughts can carry image information during reasoning.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> ICoT 试图突破这一限制，让模型在推理输出中同时使用视觉与文本内容，使视觉思考可以在推理过程中承载图像信息。

### Figure 1. 当前 ICoT 与 DaP-ICoT 的动机对比

![Figure 1](Reasoning/TrainingFree/Lets%20Think%20with%20Images%20Efficiently%20An%20Interleaved-Modal%20Chain-of-Thought%20Reasoning%20Framework%20with%20Dynamic%20and%20Precise%20Visual%20Thoughts/assets/page_001_fig_figure_1.png)

**Caption:** Current ICoT inserts visual thoughts after each step and may use broken visual tokens; DaP-ICoT inserts visual content only when confidence is low and uses more coherent segmented visual thoughts.

**Caption[CN]:** 当前 ICoT 在每一步后插入视觉思考，且插入内容可能是破碎视觉标记；DaP-ICoT 只在置信度较低时插入视觉内容，并使用更连贯的分割视觉思考。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The authors identify two problems in current ICoT: static visual thought positioning, where visual content is inserted after every textual step; and broken visual thought representation, where the inserted visual tokens are discontinuous and semantically incomplete.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 作者指出当前 ICoT 的两个问题：其一是静态视觉思考定位，即每个文本推理步骤之后都插入视觉内容；其二是破碎视觉思考表示，即插入的视觉标记不连续，语义也不完整。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> DaP-ICoT addresses these issues by making visual insertion conditional on reasoning confidence and by selecting object-centric visual inputs that preserve semantic coherence.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> DaP-ICoT 的解决方式是：根据推理置信度动态决定是否插入视觉内容，并选择以对象为中心的视觉输入来保留语义连贯性。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The paper positions the method as a lightweight improvement over ICoT. Its promise is not merely better accuracy, but a better balance between accuracy and visual-token cost.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 论文将该方法定位为对 ICoT 的轻量改进。它的目标不只是提高准确率，更是同时改善准确率与视觉标记成本之间的平衡。

## 2. DaP-ICoT Reasoning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> DaP-ICoT consists of two modules. Dynamic Visual Thought Integration decides whether a new visual thought is needed, and Precise Visual Thought Guidance chooses a context-aligned object-level visual input.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> DaP-ICoT 由两个模块组成。动态视觉思考集成判断是否需要新的视觉思考，精确视觉思考引导选择与上下文对齐的对象级视觉输入。

### Figure 2. DaP-ICoT 总体流程

![Figure 2](Reasoning/TrainingFree/Lets%20Think%20with%20Images%20Efficiently%20An%20Interleaved-Modal%20Chain-of-Thought%20Reasoning%20Framework%20with%20Dynamic%20and%20Precise%20Visual%20Thoughts/assets/page_003_fig_figure_2.png)

**Caption:** Overview of DaP-ICoT, including confidence-based visual insertion and object-level visual guidance.

**Caption[CN]:** DaP-ICoT 总体框架，包括基于置信度的视觉插入，以及对象级视觉引导。

### 2.1 Dynamic Visual Thought Integration

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For each textual rationale $T_t$, the model estimates confidence through token-level logit margins. At decoding position $i$, the local confidence is the gap between the top-1 and top-2 logits.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 对每个文本理由 $T_t$，模型通过逐标记的 logit 间隔估计置信度。在解码位置 $i$，局部置信度定义为 top-1 与 top-2 logit 之间的差。

$$
\delta_i=\ell_{i,w(1)}-\ell_{i,w(2)},\quad \forall i\in\{1,\ldots,|T_t|\}. \tag{1}
$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The confidence of the whole rationale is the mean of these local margins:

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 整个理由的置信度由这些局部间隔取平均得到：

$$
C_t=\frac{1}{|T_t|}\sum_{i=1}^{|T_t|}\delta_i
=\frac{1}{|T_t|}\sum_{i=1}^{|T_t|}\left(\ell_{i,w(1)}-\ell_{i,w(2)}\right). \tag{2}
$$

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> If $C_t$ is lower than the threshold $\tau$, the next reasoning step receives a visual thought. Otherwise, reasoning continues only with text.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 如果 $C_t$ 低于阈值 $\tau$，下一步推理会接收一个视觉思考；否则，模型只依赖文本推理继续前进。

$$
I_{t+1}=
\begin{cases}
I_{\mathrm{vision}}, & C_t<\tau,\\
\varnothing, & \mathrm{otherwise}.
\end{cases} \tag{3}
$$

### 2.2 Precise Visual Thought Guidance

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> To avoid fragmented patch-level visual thoughts, PVTG first applies SAM2 to the original image and obtains an object pool $O=\{O_1,O_2,\ldots,O_N\}$.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 为了避免破碎的 patch 级视觉思考，PVTG 首先用 SAM2 分割原图，得到对象候选池：

$$
O=\{O_1,O_2,\ldots,O_N\}. \tag{4}
$$

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> When DVTI asks for visual input at step $t$, the method computes the relevance between the current textual rationale $T_t$ and each candidate object image $O_i$.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 当 DVTI 在第 $t$ 步请求视觉输入时，方法会计算当前文本理由 $T_t$ 与每个候选对象图像 $O_i$ 的相关性。

$$
s_i=f_{\mathrm{attn}}(T_t,O_i). \tag{5}
$$

$$
\hat{O}=\arg\max_{O_i\in O}s_i. \tag{6}
$$

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> The selected object image $\hat{O}$ is interleaved into the textual reasoning sequence, and the model continues the next reasoning step conditioned on the question, the interleaved sequence, and the interleaved prompt.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 被选中的对象图像 $\hat{O}$ 会插入文本推理序列中，模型随后在问题、交错序列和交错提示的条件下继续生成下一步推理。

$$
R_{t\to v}=R_t\oplus\hat{O}. \tag{7}
$$

$$
R_{t+1}=\arg\max_R P(R\mid Q,R_{t\to v},P_{t\to v}). \tag{8}
$$

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> The essential design shift is from "insert something visual every time" to "insert a coherent object only when the current reasoning step appears uncertain."

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 这个设计的关键转变是：不再“每次都插入某些视觉内容”，而是“只有当前推理不够确定时，才插入一个连贯对象”。

## 3. Experiments and Analysis

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The experiments compare DaP-ICoT with Direct prompting, MMCoT, DDCoT, SCAFFOLD, CCoT, and ICoT. The authors reproduce the methods once using official open-source implementations.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 实验将 DaP-ICoT 与直接提示、MMCoT、DDCoT、SCAFFOLD、CCoT 和 ICoT 比较。作者使用官方开源实现对这些方法各复现实验一次。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The evaluation covers five MLLMs: Chameleon-7B, LLaVA-V1.5-7B, LLaVA-V1.5-13B, Qwen2-VL-2B, and Qwen2-VL-7B. Benchmarks include M3CoT, ScienceQA, and MME under zero-shot and one-shot settings.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 评估覆盖五个 MLLM：Chameleon-7B、LLaVA-V1.5-7B、LLaVA-V1.5-13B、Qwen2-VL-2B 和 Qwen2-VL-7B。基准包括 M3CoT、ScienceQA 和 MME，并同时测试零样本与单样本设置。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The confidence threshold $\tau$ is tuned on the M3CoT validation set by searching within $[0,1]$.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 置信度阈值 $\tau$ 通过在 M3CoT 验证集上搜索 $[0,1]$ 范围来确定。

### Table 1. 主实验结果

![Table 1](assets/page_004_fig_table_1.png)

**Caption:** Main results on M3CoT, ScienceQA, and MME across five MLLMs in zero-shot and one-shot settings.

**Caption[CN]:** 五个 MLLM 在 M3CoT、ScienceQA 和 MME 上的零样本与单样本主结果。

| Model | Method | M³CoT 0-shot | M³CoT 1-shot | ScienceQA 0-shot | ScienceQA 1-shot | MME 0-shot | MME 1-shot |
|---|---|---:|---:|---:|---:|---:|---:|
| Chameleon-7B | Direct | 22.5 | 23.8 | 43.1 | 43.4 | 724.2 | 942.9 |
| Chameleon-7B | MMCoT | 26.0 | 28.0 | 46.2 | 48.9 | 435.8 | 661.2 |
| Chameleon-7B | DDCoT | 29.8 | 30.3 | 47.4 | 48.4 | 725.9 | 953.8 |
| Chameleon-7B | SCAFFOLD | 31.0 | 31.2 | 48.6 | 50.7 | 388.1 | 634.5 |
| Chameleon-7B | CCoT | 25.1 | 26.3 | 42.8 | 44.3 | 366.1 | 487.9 |
| Chameleon-7B | ICoT | 26.1 | 32.1 | 44.5 | 45.3 | 794.8 | 928.9 |
| Chameleon-7B | DaP-ICoT | **41.0** | **41.9** | **57.1** | **62.9** | **832.3** | **1013.0** |
| LLaVA-1.5-7B | Direct | 23.2 | 25.7 | 21.9 | 23.5 | 975.3 | 1079.8 |
| LLaVA-1.5-7B | MMCoT | 29.6 | 30.4 | 42.4 | 43.1 | 1140.2 | 1277.4 |
| LLaVA-1.5-7B | DDCoT | 25.4 | 26.5 | 29.3 | 31.0 | 736.7 | 991.8 |
| LLaVA-1.5-7B | SCAFFOLD | 26.6 | 28.3 | 37.7 | 39.8 | 1170.3 | 1264.3 |
| LLaVA-1.5-7B | CCoT | 34.2 | 35.5 | 33.8 | 35.7 | 1294.3 | 1349.5 |
| LLaVA-1.5-7B | ICoT | 34.6 | 35.0 | 41.7 | 46.7 | 1331.6 | 1421.6 |
| LLaVA-1.5-7B | DaP-ICoT | **36.3** | **37.6** | **50.4** | **51.1** | **1386.7** | **1526.9** |
| LLaVA-1.5-13B | Direct | 24.6 | 25.5 | 29.7 | 34.0 | 995.4 | 1118.5 |
| LLaVA-1.5-13B | MMCoT | 32.1 | 32.9 | 56.1 | 58.3 | 1078.1 | 1224.3 |
| LLaVA-1.5-13B | DDCoT | 32.9 | 33.8 | 39.3 | 41.8 | 800.9 | 1034.1 |
| LLaVA-1.5-13B | SCAFFOLD | 31.9 | 33.2 | 41.7 | 43.8 | 1231.2 | 1389.9 |
| LLaVA-1.5-13B | CCoT | 30.1 | 32.0 | 45.0 | 46.3 | 1249.3 | 1442.3 |
| LLaVA-1.5-13B | ICoT | 37.0 | 37.9 | 54.6 | 54.8 | 1405.4 | 1523.8 |
| LLaVA-1.5-13B | DaP-ICoT | **39.4** | **41.8** | **60.3** | **62.7** | **1556.3** | **1726.3** |
| Qwen2-VL-2B | Direct | 14.4 | 24.5 | 64.3 | 65.2 | 641.5 | 741.3 |
| Qwen2-VL-2B | MMCoT | 14.9 | 22.4 | 65.6 | 67.3 | 1102.8 | 1304.7 |
| Qwen2-VL-2B | DDCoT | 37.9 | 39.3 | 65.8 | 68.4 | 800.6 | 967.0 |
| Qwen2-VL-2B | SCAFFOLD | 40.3 | 43.6 | 66.7 | 69.4 | 1344.8 | 1536.2 |
| Qwen2-VL-2B | CCoT | 20.2 | 37.7 | 64.2 | 66.5 | 761.6 | 867.5 |
| Qwen2-VL-2B | ICoT | 35.8 | 37.3 | 60.4 | 67.0 | 941.9 | 1453.9 |
| Qwen2-VL-2B | DaP-ICoT | **47.3** | **51.0** | **68.4** | **73.6** | **1378.9** | **1862.4** |
| Qwen2-VL-7B | Direct | 33.0 | 35.0 | 70.9 | 71.2 | 1599.3 | 1641.3 |
| Qwen2-VL-7B | MMCoT | 44.4 | 47.5 | 70.8 | 73.8 | 1602.5 | 1874.3 |
| Qwen2-VL-7B | DDCoT | 43.9 | 45.3 | 62.8 | 65.3 | 1752.4 | 1826.6 |
| Qwen2-VL-7B | SCAFFOLD | 49.9 | 53.6 | 74.4 | 75.0 | 1668.2 | 1822.2 |
| Qwen2-VL-7B | CCoT | 48.7 | 53.0 | 72.7 | 74.8 | 1866.3 | 1941.9 |
| Qwen2-VL-7B | ICoT | 38.0 | 44.8 | 54.2 | 67.0 | 1587.3 | 1709.3 |
| Qwen2-VL-7B | DaP-ICoT | **57.2** | **58.7** | **75.9** | **78.5** | **2012.2** | **2076.0** |

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Table 1 shows that DaP-ICoT is consistently competitive or best across the evaluated backbones. On Chameleon-7B, for example, its M3CoT zero-shot accuracy is 41.0, compared with 31.0 for SCAFFOLD and 26.1 for ICoT.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 表 1 显示 DaP-ICoT 在被测骨干上整体稳定领先或接近最佳。例如在 Chameleon-7B 上，它的 M3CoT 零样本准确率为 41.0，而 SCAFFOLD 为 31.0，ICoT 为 26.1。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> On Qwen2-VL-7B, DaP-ICoT reaches 57.2 / 58.7 on M3CoT, 75.9 / 78.5 on ScienceQA, and 2012.2 / 2076.0 on MME under zero-shot / one-shot settings.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 在 Qwen2-VL-7B 上，DaP-ICoT 在零样本 / 单样本设置下分别达到：M3CoT 57.2 / 58.7，ScienceQA 75.9 / 78.5，MME 2012.2 / 2076.0。

### Figure 3. 消融实验

![Figure 3](Reasoning/TrainingFree/Lets%20Think%20with%20Images%20Efficiently%20An%20Interleaved-Modal%20Chain-of-Thought%20Reasoning%20Framework%20with%20Dynamic%20and%20Precise%20Visual%20Thoughts/assets/page_005_fig_figure_3.png)

**Caption:** Ablation on Qwen2-VL-7B: removing PVTG or DVTI sharply lowers M3CoT and ScienceQA performance.

**Caption[CN]:** Qwen2-VL-7B 上的消融：移除 PVTG 或 DVTI 都会显著降低 M3CoT 与 ScienceQA 表现。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> Ablations show that both modules are necessary. On Qwen2-VL-7B, DaP-ICoT scores 57.2 on M3CoT and 75.9 on ScienceQA. Without PVTG, the scores drop to 43.4 and 55.5; without DVTI, they drop to 42.8 and 55.1.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 消融说明两个模块都很关键。在 Qwen2-VL-7B 上，DaP-ICoT 的 M3CoT 和 ScienceQA 分数为 57.2 与 75.9。去掉 PVTG 后下降到 43.4 与 55.5；去掉 DVTI 后下降到 42.8 与 55.1。

### Figure 4. 总标记消耗

![Figure 4](Reasoning/TrainingFree/Lets%20Think%20with%20Images%20Efficiently%20An%20Interleaved-Modal%20Chain-of-Thought%20Reasoning%20Framework%20with%20Dynamic%20and%20Precise%20Visual%20Thoughts/assets/page_005_fig_figure_4.png)

**Caption:** On M3CoT with Qwen2-VL-7B, DaP-ICoT uses 314 average tokens, compared with 1,146 for ICoT.

**Caption[CN]:** 在 Qwen2-VL-7B 的 M3CoT 实验中，DaP-ICoT 平均使用 314 个标记，而 ICoT 使用 1,146 个。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> The efficiency claim is supported by token accounting. DaP-ICoT consumes 314 average tokens on M3CoT with Qwen2-VL-7B, which is 72.6% lower than ICoT's 1,146 tokens. CCoT and DDCoT consume 1,294 and 1,426 tokens respectively.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 效率主张主要由标记统计支撑。在 Qwen2-VL-7B 的 M3CoT 上，DaP-ICoT 平均消耗 314 个标记，比 ICoT 的 1,146 个降低 72.6%。CCoT 和 DDCoT 分别消耗 1,294 与 1,426 个标记。

### Figure 5. 图像插入频率与图像标记消耗

![Figure 5](assets/page_006_fig_figure_5.png)

**Caption:** DaP-ICoT inserts fewer images than ICoT and consumes fewer inserted image tokens.

**Caption[CN]:** DaP-ICoT 比 ICoT 插入更少图像，也消耗更少的插入图像标记。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> DaP-ICoT inserts about 1.2 images per sample on average, while ICoT inserts about 2.6. The paper also reports that DaP-ICoT consumes only about 26 inserted image tokens on average.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> DaP-ICoT 平均每个样本插入约 1.2 张图像，而 ICoT 约为 2.6 张。论文还报告 DaP-ICoT 平均只消耗约 26 个插入图像标记。

### Figure 6. 插图后的置信度变化

![Figure 6](assets/page_006_fig_figure_6.png)

**Caption:** DaP-ICoT increases confidence more frequently and by a larger margin than ICoT.

**Caption[CN]:** 相比 ICoT，DaP-ICoT 更常提升置信度，且平均提升幅度更大。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> Confidence analysis suggests that the inserted visual content is more useful, not merely cheaper. On average, DaP-ICoT increases confidence in 80.7% of samples, while ICoT does so in 46.4% of samples.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 置信度分析说明插入视觉内容不只是更便宜，也更有用。平均而言，DaP-ICoT 让 80.7% 的样本置信度提升，而 ICoT 只有 46.4%。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> A threshold search on Qwen2-VL-7B and M3CoT finds the best value around $\tau=0.2$, where the method obtains 57.2% zero-shot accuracy and 58.7% one-shot accuracy.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 在 Qwen2-VL-7B 与 M3CoT 上进行阈值搜索后，最佳值约为 $\tau=0.2$，对应零样本准确率 57.2%，单样本准确率 58.7%。

### Figure 7. Confidence threshold search

![Figure 7](Reasoning/TrainingFree/Lets%20Think%20with%20Images%20Efficiently%20An%20Interleaved-Modal%20Chain-of-Thought%20Reasoning%20Framework%20with%20Dynamic%20and%20Precise%20Visual%20Thoughts/assets/page_006_fig_figure_7.png)

**Caption:** Performance across $\tau\in(0,1]$ on Qwen2-VL-7B and M³CoT. The optimum is $\tau=0.2$, with 57.2% zero-shot and 58.7% one-shot accuracy.

**Caption[CN]:** Qwen2-VL-7B 在 M³CoT 上对 $\tau\in(0,1]$ 的性能搜索。最佳阈值为 $\tau=0.2$，零样本与单样本准确率分别为 57.2% 和 58.7%。

| $\tau$ | 0.1 | 0.2 | 0.3 | 0.4 | 0.5 | 0.6 | 0.7 | 0.8 | 0.9 | 1.0 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| M³CoT 0-shot | 56.8 | **57.2** | 56.7 | 56.1 | 57.1 | 56.0 | 53.0 | 52.9 | 53.5 | 52.3 |

### Figure 8. 定性案例

![Figure 8](Reasoning/TrainingFree/Lets%20Think%20with%20Images%20Efficiently%20An%20Interleaved-Modal%20Chain-of-Thought%20Reasoning%20Framework%20with%20Dynamic%20and%20Precise%20Visual%20Thoughts/assets/page_007_fig_figure_8.png)

**Caption:** Current ICoT inserts broken visual tokens and answers incorrectly; DaP-ICoT inserts complete context-relevant visual content under low confidence and obtains the correct answer.

**Caption[CN]:** 当前 ICoT 插入破碎视觉标记并答错；DaP-ICoT 在低置信度时插入完整且相关的视觉内容，并得到正确答案。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> In the case study, ICoT incorrectly answers "waiting for someone" because the inserted tokens are incomplete. DaP-ICoT segments and selects a relevant object image, then answers "selling umbrellas."

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> 在案例分析中，ICoT 因插入标记不完整而错误回答“等待某人”。DaP-ICoT 分割并选择相关对象图像，最后回答“卖伞”。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> Exact literals in Figure 8 are preserved: query `What is the man in the walkway doing?`; option `(A) Selling umbrellas.`; option `(D) Waiting for someone.`; ICoT output `So, Answer: (D) Waiting for someone`; DaP-ICoT output `So, Answer: (A) Selling umbrellas`.

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> Figure 8 的精确字面量保留如下：问题 `走道里的男人在做什么？`；选项 `(A) 卖伞。`；选项 `(D) 等待某人。`；ICoT 输出 `So, Answer: (D) Waiting for someone`；DaP-ICoT 输出 `So, Answer: (A) Selling umbrellas`。英文输出格式保持原样。

## 4. Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The related work situates DaP-ICoT among MLLMs, multimodal CoT, and interleaved visual-text reasoning. Prior work improves reasoning with descriptions, scene graphs, sketches, visual prompting, or attention-based region insertion.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 相关工作把 DaP-ICoT 放在 MLLM、多模态思维链和视觉文本交错推理的脉络中。已有方法通过描述、场景图、草图、视觉提示或基于注意力的区域插入来增强推理。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Compared with earlier ICoT methods, the paper argues that DaP-ICoT is more adaptive because it combines confidence-aware insertion with object-level visual selection.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 相比早期 ICoT 方法，论文认为 DaP-ICoT 更自适应，因为它同时结合了置信度感知插入和对象级视觉选择。

## 5. Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The conclusion restates that DaP-ICoT improves ICoT by adaptively integrating informative visual input and by using coherent visual representations. The reported gains cover both effectiveness and efficiency.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 结论重申 DaP-ICoT 通过自适应整合有信息量的视觉输入，并使用连贯视觉表示来改进 ICoT。论文报告的收益同时覆盖效果与效率。

## References and Acknowledgments

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Funding includes NSFC grants 92570120 and 62306342, Hunan Provincial Education Department 24B0001, Hunan Excellent Young Scientists Fund 2024JJ4070, Hunan Science and Technology Innovation Program 2024RC3024, CCF-Zhipu grant CCF-Zhipu202406, and TCCI Open Project TCCI250101. Libo Qin is corresponding author.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 资助包括国家自然科学基金 92570120、62306342，湖南省教育厅 24B0001，湖南省优秀青年科学基金 2024JJ4070，湖南省科技创新计划 2024RC3024，CCF-智谱项目 CCF-Zhipu202406，以及 TCCI 开放课题 TCCI250101。Libo Qin 为通讯作者。

## Full searchable references

> **Policy / 策略：** References remain in original English bibliographic form to preserve author names, titles, venues, identifiers, and searchability. / 参考文献保留原始英文书目信息，确保作者、题名、会议期刊和标识符可准确检索。

```text
Achiam, J.; Adler, S.; Agarwal, S.; Ahmad, L.; Akkaya, I.;
Aleman, F. L.; Almeida, D.; Altenschmidt, J.; Altman, S.;
Anadkat, S.; Avila, R.; Babuschkin, I.; Balaji, S.; Balcom,
V.; Baltescu, P.; Bao, H.; Bavarian, M.; Belgum, J.; Bello, I.;
Berdine, J.; Bernadett-Shapiro, G.; Berner, C.; Bogdonoff,
L.; Boiko, O.; Boyd, M.; Brakman, A.-L.; Brockman, G.;
Brooks, T.; Brundage, M.; Button, K.; Cai, T.; Campbell, R.;
Cann, A.; Carey, B.; Carlson, C.; Carmichael, R.; Chan, B.;
Chang, C.; Chantzis, F.; Chen, D.; Chen, S.; Chen, R.; Chen,
J.; Chen, M.; Chess, B.; Cho, C.; Chu, C.; Chung, H. W.;
Cummings, D.; Currier, J.; Dai, Y.; Decareaux, C.; Degry,
T.; Deutsch, N.; Deville, D.; Dhar, A.; Dohan, D.; Dowling,
S.; Dunning, S.; Ecoffet, A.; Eleti, A.; Eloundou, T.; Farhi,
D.; Fedus, L.; Felix, N.; Fishman, S. P.; Forte, J.; Fulford,
I.; Gao, L.; Georges, E.; Gibson, C.; Goel, V.; Gogineni, T.;
Goh, G.; Gontijo-Lopes, R.; Gordon, J.; Grafstein, M.; Gray,
S.; Greene, R.; Gross, J.; Gu, S. S.; Guo, Y.; Hallacy, C.;
Han, J.; Harris, J.; He, Y.; Heaton, M.; Heidecke, J.; Hesse,
C.; Hickey, A.; Hickey, W.; Hoeschele, P.; Houghton, B.;
Hsu, K.; Hu, S.; Hu, X.; Huizinga, J.; ; et al. 2023. Gpt-4
technical report. arXiv preprint arXiv:2303.08774.
Chen, Q.; Qin, L.; Liu, J.; Peng, D.; Guan, J.; Wang, P.; Hu,
M.; Zhou, Y.; Gao, T.; and Che, W. 2025a. Towards reasoning era: A survey of long chain-of-thought for reasoning
large language models. arXiv preprint arXiv:2503.09567.
Chen, Q.; Qin, L.; Zhang, J.; Chen, Z.; Xu, X.; and Che,
W. 2024. M3
CoT: A Novel Benchmark for Multi-Domain
Multi-step Multi-modal Chain-of-Thought. In Ku, L.-W.;
Martins, A.; and Srikumar, V., eds., Proceedings of the 62nd
Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), 8199–8221. Bangkok,
Thailand: Association for Computational Linguistics.
Chen, Q.; Yang, M.; Qin, L.; Liu, J.; Yan, Z.; Guan, J.; Peng,
D.; Ji, Y.; Li, H.; Hu, M.; et al. 2025b. AI4Research: A Survey of Artificial Intelligence for Scientific Research. arXiv
preprint arXiv:2507.01903.
Cheng, Z.; Chen, Q.; Xu, X.; Wang, J.; Wang, W.; Fei,
H.; Wang, Y.; Wang, A. J.; Chen, Z.; Che, W.; et al.
2025a. Visual Thoughts: A Unified Perspective of Understanding Multimodal Chain-of-Thought. arXiv preprint
arXiv:2505.15510.
Cheng, Z.; Chen, Q.; Zhang, J.; Fei, H.; Feng, X.; Che, W.;
Li, M.; and Qin, L. 2025b. Comt: A novel benchmark for
chain of multi-modal thought on large vision-language models. In Proceedings of the AAAI Conference on Artificial
Intelligence, volume 39, 23678–23686.
Fei, H.; Wu, S.; Ji, W.; Zhang, H.; Zhang, M.; Lee, M.-L.;
and Hsu, W. 2024. Video-of-thought: Step-by-step video
reasoning from perception to cognition. arXiv preprint
arXiv:2501.03230.
Gao, J.; Li, Y.; Cao, Z.; and Li, W. 2025. Interleaved-modal
chain-of-thought. In Proceedings of the Computer Vision
and Pattern Recognition Conference, 19520–19529.
Hu, Y.; Shi, W.; Fu, X.; Roth, D.; Ostendorf, M.; Zettlemoyer, L.; Smith, N. A.; and Krishna, R. 2024. Visual
Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models. In The Thirty-eighth Annual
Conference on Neural Information Processing Systems.
Lei, X.; Yang, Z.; Chen, X.; Li, P.; and Liu, Y. 2025. Scaffolding Coordinates to Promote Vision-Language Coordination in Large Multi-Modal Models. In Rambow, O.; Wanner, L.; Apidianaki, M.; Al-Khalifa, H.; Eugenio, B. D.; and
Schockaert, S., eds., Proceedings of the 31st International
Conference on Computational Linguistics, 2886–2903. Abu
Dhabi, UAE: Association for Computational Linguistics.
Li, C.; Wu, W.; Zhang, H.; Xia, Y.; Mao, S.; Dong, L.;
Vulić, I.; and Wei, F. 2025. Imagine while Reasoning
in Space: Multimodal Visualization-of-Thought. arXiv
preprint arXiv:2501.07542.
Liang, Z.; Xu, Y.; Hong, Y.; Shang, P.; Wang, Q.; Fu, Q.;
and Liu, K. 2024. A Survey of Multimodel Large Language
Models. In Proceedings of the 3rd International Conference
on Computer, Artificial Intelligence and Control Engineering, 405–409.
Lin, J.; Zeng, X.; Zhu, J.; Wang, S.; Shun, J.; Wu, J.; and
Zhou, D. 2025. Plan and Budget: Effective and Efficient
Test-Time Scaling on Large Language Model Reasoning.
arXiv preprint arXiv:2505.16122.
Liu, H.; Li, C.; Wu, Q.; and Lee, Y. J. 2023. Visual instruction tuning. Advances in neural information processing
systems, 36: 34892–34916.
Meng, F.; Yang, H.; Wang, Y.; and Zhang, M. 2023.
Chain of images for intuitively reasoning. arXiv preprint
arXiv:2311.09241.
Menon, S.; Zemel, R.; and Vondrick, C. 2024. Whiteboardof-Thought: Thinking Step-by-Step Across Modalities. In
Proceedings of the 2024 Conference on Empirical Methods
in Natural Language Processing, 20016–20031.
Mitra, C.; Huang, B.; Darrell, T.; and Herzig, R. 2024. Compositional Chain-of-Thought Prompting for Large Multimodal Models. In 2024 IEEE/CVF Conference on Computer
Vision and Pattern Recognition (CVPR), 14420–14431.
IEEE Computer Society.
Qiang, C.; Wei, Z.; Han, X.; Wang, Z.; Li, S.; Lan, X.; Jiao,
J.; and Han, Z. 2025. VER-Bench: Evaluating MLLMs on
Reasoning with Fine-Grained Visual Evidence. In Proceedings of the 33rd ACM International Conference on Multimedia, 12698–12705.Qin, L.; Chen, Q.; Feng, X.; Wu, Y.; Zhang, Y.; Li, Y.; Li,
M.; Che, W.; and Yu, P. S. 2024. Large language models
meet nlp: A survey. arXiv preprint arXiv:2405.12819.
Qiu, T.; Gao, J.; Li, J.; Leong, H.; Huang, X.; Wang, X.;
Zhang, X.; Xu, K.; and Zhang, L. 2025. Intentvcnet: Bridging spatio-temporal gaps for intention-oriented controllable
video captioning. In Proceedings of the 33rd ACM International Conference on Multimedia, 13822–13829.
Ravi, N.; Gabeur, V.; Hu, Y.-T.; Hu, R.; Ryali, C.; Ma, T.;
Khedr, H.; Rädle, R.; Rolland, C.; Gustafson, L.; Mintun,
E.; Pan, J.; Alwala, K. V.; Carion, N.; Wu, C.-Y.; Girshick,
R.; Dollár, P.; and Feichtenhofer, C. 2024. SAM 2: Segment
Anything in Images and Videos. arXiv:2408.00714.
Shao, H.; Qian, S.; Xiao, H.; Song, G.; Zong, Z.; Wang, L.;
Liu, Y.; and Li, H. 2024. Visual cot: Advancing multi-modal
language models with a comprehensive dataset and benchmark for chain-of-thought reasoning. Advances in Neural
Information Processing Systems, 37: 8612–8642.
Team, C. 2024. Chameleon: Mixed-modal early-fusion
foundation models. arXiv preprint arXiv:2405.09818.
Team, G.; Georgiev, P.; Lei, V. I.; Burnell, R.; Bai, L.; Gulati, A.; Tanzer, G.; Vincent, D.; Pan, Z.; Wang, S.; Mariooryad, S.; Ding, Y.; Geng, X.; Alcober, F.; Frostig, R.;
Omernick, M.; Walker, L.; Paduraru, C.; Sorokin, C.; Tacchetti, A.; Gaffney, C.; Daruki, S.; Sercinoglu, O.; Gleicher,
Z.; Love, J.; Voigtlaender, P.; Jain, R.; Surita, G.; Mohamed,
K.; Blevins, R.; Ahn, J.; Zhu, T.; Kawintiranon, K.; Firat, O.;
Gu, Y.; Zhang, Y.; Rahtz, M.; Faruqui, M.; Clay, N.; Gilmer,
J.; Co-Reyes, J.; Penchev, I.; Zhu, R.; Morioka, N.; Hui, K.;
Haridasan, K.; Campos, V.; Mahdieh, M.; Guo, M.; Hassan, S.; Kilgour, K.; Vezer, A.; Cheng, H.-T.; de Liedekerke,
R.; Goyal, S.; Barham, P.; Strouse, D.; Noury, S.; Adler, J.;
Sundararajan, M.; Vikram, S.; Lepikhin, D.; Paganini, M.;
Garcia, X.; Yang, F.; Valter, D.; Trebacz, M.; Vodrahalli, K.;
Asawaroengchai, C.; Ring, R.; et al. 2024. Gemini 1.5: Unlocking multimodal understanding across millions of tokens
of context. arXiv preprint arXiv:2403.05530.
Wang, B.; Li, Y.; Zhou, Q.; Leong, H. Y.; Zhao, T.; Ye, L.;
Deng, H.; Luo, D.; and Vasconcelos, N. 2025a. Do Vision Language Models infer human intention without visual
perspective-taking? Towards a scalable” One-Image-Probe-
All” dataset.
Wang, P.; Bai, S.; Tan, S.; Wang, S.; Fan, Z.; Bai, J.; Chen,
K.; Liu, X.; Wang, J.; Ge, W.; Fan, Y.; Dang, K.; Du, M.;
Ren, X.; Men, R.; Liu, D.; Zhou, C.; Zhou, J.; Lin, J.;
et al. 2024. Qwen2-vl: Enhancing vision-language model’s
perception of the world at any resolution. arXiv preprint
arXiv:2409.12191.
Wang, Y.; Wu, S.; Zhang, Y.; Yan, S.; Liu, Z.; Luo, J.; and
Fei, H. 2025b. Multimodal chain-of-thought reasoning: A
comprehensive survey. arXiv preprint arXiv:2503.12605.
Wei, Z.; Qiang, C.; Jiang, B.; Han, X.; Yu, X.; and Han, Z.
2025. ADˆ 2-Bench: A Hierarchical CoT Benchmark for
MLLM in Autonomous Driving under Adverse Conditions.
arXiv preprint arXiv:2506.09557.
Wu, X.; Liu, J.; Huang, D.; Li, X.; Wang, Y.; Chen, C.; Ma,
L.; Cao, X.; and Xue, J. 2025. ViC-Bench: Benchmarking
Visual-Interleaved Chain-of-Thought Capability in MLLMs
with Free-Style Intermediate State Representations. arXiv
preprint arXiv:2505.14404.
Zhang, Y.; Chen, Q.; Zhou, J.; Wang, P.; Si, J.; Wang, J.; Lu,
W.; and Qin, L. 2024a. Wrong-of-thought: An integrated
reasoningframeworkwithmulti-perspectiveverificationand
wrong information. In Findings of the Association for Computational Linguistics: EMNLP 2024, 6644–6653.
Zhang, Y.; Liu, X.; Tao, R.; Chen, Q.; Fei, H.; Che, W.; and
Qin, L. 2025a. ViTCoT: Video-Text Interleaved Chain-of-
Thought for Boosting Video Understanding in Large Language Models. arXiv preprint arXiv:2507.09876.
Zhang, Y.; Liu, X.; Zhou, R.; Chen, Q.; Fei, H.; Lu, W.; and
Qin,L.2025b. CCHall:ANovelBenchmarkforJointCross-
Lingual and Cross-Modal Hallucinations Detection in Large
Language Models. arXiv preprint arXiv:2505.19108.
Zhang, Z.; Zhang, A.; Li, M.; Karypis, G.; Smola, A.; et al.
2024b. Multimodal Chain-of-Thought Reasoning in Language Models. Transactions on Machine Learning Research.
Zhang, Z.; Zhang, A.; Li, M.; Zhao, H.; Karypis, G.; and
Smola, A. 2023. Multimodal chain-of-thought reasoning in
language models. arXiv preprint arXiv:2302.00923.
Zheng, G.; Yang, B.; Tang, J.; Zhou, H.-Y.; and Yang, S.
2023. Ddcot: Duty-distinct chain-of-thought prompting for
multimodal reasoning in language models. Advances in
Neural Information Processing Systems, 36: 5168–5191.
Zhou, Q.; Zhou, R.; Hu, Z.; Lu, P.; Gao, S.; and Zhang,
Y. 2024. Image-of-thought prompting for visual reasoning refinement in multimodal large language models. arXiv
preprint arXiv:2405.13872.
```

## Critical Reading Notes

1. 这篇论文是对 ICoT 的“调度 + 表示”补丁：DVTI 解决何时插入，PVTG 解决插入什么。
2. 最硬的证据是消融和效率：去掉任一模块都会大幅掉点，且标记消耗从 ICoT 的 1,146 降到 314。
3. 阈值 $\tau$ 依赖验证集搜索，跨数据集和跨模型是否稳定仍需要更细的报告。
4. PVTG 依赖 SAM2，这让方法仍是免训练，但并不是无额外视觉工具。
5. 与 3D agent 方向的关系在于“测试时主动取证”：这里取的是对象图像，REALM/DeepScan 取的是 3D 或高分辨率视觉证据。
