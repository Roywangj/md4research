---
tags:
  - papers/visually-grounded-reasoning
  - papers/agentic-VLM
aliases:
  - "DeepScan"
  - "DeepScan Visually Grounded Reasoning"
date: 2026-03-04
doi: 10.48550/arXiv.2603.03857
arxiv_id: 2603.03857
---

# DeepScan: A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models

## 核心信息

- 标题: DeepScan: A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models
- 标题翻译: DeepScan：面向大型视觉语言模型视觉落地推理的免训练框架
- 作者: Yangfu Li, Hongjian Zhan, Jiawei Chen, Yuning Gong, Qi Liu, Yue Lu
- 机构: 华东师范大学、四川大学、上海人工智能实验室
- 发表时间: 2026-03-04
- 发表渠道: CVPR 2026；arXiv
- DOI: 10.48550/arXiv.2603.03857
- arXiv: 2603.03857
- 论文链接: https://arxiv.org/abs/2603.03857
- 代码 / 项目: https://github.com/YChenL/DeepScan
- 数据 / 资源: V* Bench；HR-Bench-4K/8K；TreeBench
- 论文类型: AI 方法；免训练视觉落地推理；测试时视觉搜索

## 原文摘要翻译

人类即使身处嘈杂环境，也能通过识别关键线索，再自底向上地把这些线索关联回完整语境，从而稳健地定位视觉证据并给出有依据的答案。受此启发，本文提出 DeepScan：一个结合分层扫描、再聚焦与证据增强推理的免训练框架，用于大型视觉语言模型的视觉落地推理。

不同于试图一次性定位完整证据的现有方法，分层扫描通过局部线索探索和多尺度证据提取，以自底向上的方式恢复证据，有效减弱干扰上下文的影响。随后，再聚焦通过大型视觉语言模型与视觉专家的协作优化已定位证据的视图。最后，证据增强推理借助混合证据记忆聚合多粒度视图，生成准确且可解释的答案。

实验结果表明，DeepScan 在多种视觉任务上显著增强大型视觉语言模型，尤其适用于细粒度视觉理解。与 Qwen2.5-VL-7B 结合时，它在 V* 上达到 `90.6%` 的总体准确率。DeepScan 无需额外适配成本，也能跨不同架构和模型规模带来一致提升。

## 创新点

1. 把视觉证据定位从自顶向下改成自底向上。方法先在局部图块中寻找判别性线索，再把线索提升回全图恢复对象，避免全局显著区域或相似物体在第一步就劫持搜索。
2. 提出结合语义与几何的点式代理。每个局部连通区域不再用框或文字描述表示，而是选择一个既靠近区域内部、又具有高注意响应的点，作为全图点提示分割的锚点。
3. 把形态学后处理和访问掩码纳入推理流程。闭运算修补掩码孔洞，膨胀补回邻近上下文；访问掩码屏蔽已检查证据，既提高质量也减少重复调用。
4. 用四状态再聚焦校准上下文范围。系统不盲目追求更紧裁剪，而是在证据完整性约束下选择面积最小的视图，平衡细节放大与空间关系语境。
5. 用混合证据记忆同时保存细粒度证据和粗粒度视图。局部裁剪用于辨认属性，较宽视图用于维持对象关系，最终以有序多图提示交给模型回答。
6. 给出可批处理的工程优化。分层扫描是确定性的，注意图、候选判断和视图完整性判断可批量执行；补充实验结合 vLLM 后获得约 `8` 倍加速。

## 一句话总结

DeepScan 的关键不是“让模型多看几次裁剪图”，而是先用局部线索建立可靠锚点，再恢复全图证据并校准上下文窗口；它有力改善了高分辨率细粒度感知和证据定位，但定位更准并不等于所有二阶视觉推理能力都会同步增强。

## 研究问题

大型视觉语言模型处理高分辨率图像时，真正困难的往往不是语言推理，而是先在大量视觉内容中找到决定答案的细小证据。若目标只占图像的万分之几，整图显著区域、相似物体和背景纹理都可能吸走注意力。

![Figure 1](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/page_001_fig_figure_1.png)
*论文原图编号：Figure 1。左侧自顶向下流程先猜完整区域，容易被相似对象误导；右侧 DeepScan 先找局部差异线索，再向上恢复真实证据。*

现有视觉落地方法多采用“整图搜索粗代理，再细化”的顺序。粗代理可能是候选框、检测结果或文字描述。这个顺序隐含了一个强假设：模型必须在第一次整图观察时就找对完整对象。一旦出现注意力汇聚陷阱或注意力漂移，后续分割与裁剪只会精细化错误区域。

DeepScan 的问题意识因此很明确：能否像人做“找不同”那样，把整图拆成局部图块，先发现微小但有判别力的线索，再回到全图恢复对象，并在回答前决定应该保留多少上下文？

## 数据与任务定义

### 输入与输出

输入为图像 $I$ 与问题 $q$。图像张量满足：

$$
I\in\mathbb{R}^{H\times W\times 3}.
$$

输出不只是最终答案，还包括显式证据集合、再聚焦视图和混合证据记忆。因此论文同时评价回答准确率和证据定位质量。

### 评测基准

| 基准 | 规模与分辨率 | 任务 | 指标 |
| --- | --- | --- | --- |
| V* Bench | 191 张；平均 `2246×1582`；目标平均面积小于 `0.05%` | 115 个直接属性问题；76 个空间关系问题 | 选择题准确率 |
| HR-Bench-4K | 200 张；4K | 100 个单实例问题；100 个跨实例问题 | 循环置换选择题准确率 |
| HR-Bench-8K | 200 张；8K | 100 个单实例问题；100 个跨实例问题 | 循环置换选择题准确率 |
| TreeBench | 405 张；平均 `2152×1615` | 可追踪证据、细小目标、二阶视觉推理 | 选择题准确率与 mIoU |

### 模型与实现设置

搜索专家使用 BLIP-ITM base，通过 Grad-CAM 生成局部注意图。视觉专家使用 LangSAM，提供点提示分割与文本条件检测。

主实验覆盖五种视觉语言骨干：

- LLaVA-1.5-7B。
- Qwen2-VL-7B。
- Qwen2.5-VL 的 7B、32B、72B 版本。

默认保留面积最小的 `10` 个候选。单对象问题使用 `576×576` 图块，多对象问题使用 `768×768` 图块。主实验在 `4` 张 NVIDIA L20 上运行。

补充材料给出更多复现参数：局部噪声区域阈值为 `50` 像素，闭运算核为 `5×5`，膨胀圆盘半径为 `20`，证据框去重阈值为 `0.3`，检测框四周填充 `28` 像素，再聚焦缩放因子为 `1.5`。推理温度设为 `0`，固定随机种子为 `13`。

## 方法主线

### 机制流程

1. 局部扫描输入：系统把图像按问题类型切成图块，搜索专家提取每个图块的注意图，并用 Otsu 阈值和连通域分析生成局部候选线索。
2. 证据恢复输出：系统融合注意强度与边界距离选择点式代理，把代理投影回全图；视觉专家据此解码掩码，形态学处理后输出证据裁剪与访问掩码。
3. 上下文再聚焦：系统以全部证据的最小包围框为初始视图，查询四个放大/缩小状态；模型判断证据完整性，奖励函数选择完整且尽量紧凑的视图 $V^*$。
4. 多粒度推理：系统把细粒度证据裁剪与粗粒度视图拼成混合证据记忆 $\mathcal{H}$，送入视觉语言模型，最终输出有证据支撑的答案 $A$。

![Figure 3](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/page_003_fig_figure_3.png)
*论文原图编号：Figure 3。DeepScan 总体架构：分层扫描恢复局部证据，再聚焦校准上下文，混合证据记忆支持最终推理。*

### 搜索专家与视觉专家

给定局部图块 $p$ 和问题 $q$，搜索专家通过注意图给出潜在线索：

$$
S=\operatorname{SEARCH}(p,q)\in\mathbb{R}^{h\times w}.
$$

视觉专家提供两个基础操作：从点提示得到掩码，以及根据问题检测目标框：

$$
m=\operatorname{SEGMENT}(I,c),\qquad B=\operatorname{DETECT}(I,q).
$$

搜索专家负责“哪里值得看”，视觉专家负责“从这个点恢复出什么对象”。二者都不直接回答问题，最终判断仍由视觉语言模型完成。

### 分层扫描：从局部线索恢复全图证据

系统先对每个图块的注意图使用 Otsu 阈值，得到高响应连通区域。对每个连通区域 $G$，几何项是候选点到边界的最短距离：

$$
d(c,\partial G)=\inf_{\gamma\in\partial G}\lVert c-\gamma\rVert_2.
$$

代理点同时考虑归一化注意响应 $\widetilde{S}_p$ 与归一化边界距离 $\widetilde{d}$：

$$
c^*=\arg\max_{c\in G}\widetilde{S}_p(c)\,\widetilde{d}(c,\partial G).
$$

注意峰值提供语义相关性，边界距离把点推向区域内部。二者结合能避免质心落到 U 形区域外，也避免只追逐边缘上的高响应噪声。

代理点被提升到全图坐标后，LangSAM 用点提示恢复完整对象掩码。这样，图块中只需要看见一个可靠局部线索，不需要在局部裁剪里包含完整对象。

![Figure 4](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/fig4.png)
*论文原图编号：Figure 4。形态学后处理通过闭运算填补孔洞，再用膨胀补充必要邻域，使点提示掩码更完整。*

增强掩码写为：

$$
m^+=(m\bullet\mathcal{K})\oplus S_r.
$$

系统再删除落入 $m^+$ 的重复代理，裁出最小包围框，让模型做一次“是否包含回答线索”的二元判断。访问掩码将已检查区域从后续步骤中屏蔽，防止重复扫描同一对象。

![Algorithm 1](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/algorithm1.png)
*论文原图编号：Algorithm 1。分层扫描完整伪代码，包括图块选择、代理提取、全图分割、形态学处理、证据去重和最小候选筛选。*

### 最小候选优先

作者观察到，大而显著的证据通常已经能被基础模型直接看见，测试时搜索更应该服务于小而不显著的目标。因此候选按面积排序，只让模型判断最小的前 $k$ 个。

![Figure 5](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/fig5.png)
*论文原图编号：Figure 5。目标越小，显式定位带来的增益越大；减少候选数量可形成可控的准确率—时延权衡。*

即使 $k=1$，仍能保留约 `96%` 的最大可达性能，并获得约 `2` 倍加速。默认 $k=10$ 是性能和时延之间的折中，不是算法必需常数。

### 再聚焦：完整但尽量紧凑

分层扫描获得证据集合 $\mathcal{E}$ 后，系统用全部证据的最小包围框建立初始视图 $V_1$。随后定义两个动作：

$$
\operatorname{IN}(V,q)=\operatorname{CROP}(V,\operatorname{DETECT}(V,q)),
$$

$$
\operatorname{OUT}(V,s)=\operatorname{CROP}(I,\operatorname{SCALEBBOX}(V,s)).
$$

奖励函数先检查视图是否包含回答所需全部证据，再偏好更小的完整视图：

$$
R(V)=\mathbb{I}_{V\rightsquigarrow q}\frac{HW}{hw}.
$$

如果视图不完整，奖励为零；只有完整视图才按面积获得更高分。这避免“裁得越紧越好”的错误目标。

![Figure 6](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/fig6.png)
*论文原图编号：Figure 6。左例需要缩小视图补回人体关系，右例需要放大手套去除干扰；再聚焦依据问题自适应选择。*

论文把搜索空间压缩为四个状态：

$$
\mathcal{V}=\{V_1,V_2,V_3,V_4\},
$$

$$
V_2=\operatorname{IN}(V_1,q),\quad V_3=\operatorname{OUT}(V_1,s),\quad V_4=\operatorname{IN}(V_3,q).
$$

作者在若干幂等性与可恢复性假设下删掉其余分支。这里的“全局最优”只在这些设计假设和奖励定义内成立，并不是任意视觉搜索的普遍保证。

![Algorithm 2](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/algorithm2.png)
*论文原图编号：Algorithm 2。再聚焦伪代码：构造四个视图，用证据完整性判断和面积奖励选择最终视图。*

### 混合证据记忆

最终记忆同时存储细粒度证据 $e$ 与再聚焦视图 $V^*$：

$$
\mathcal{H}=\{e,V^*\mid (b,e)\in\mathcal{E},\ V^*=\arg\max_{V\in\mathcal{V}}R(V)\}.
$$

系统把它组织成有序多图提示 $[e_1,\ldots,V^*]$。局部证据帮助判断颜色、文字和材质；粗粒度视图保留左右关系、遮挡与对象间位置。最终答案为：

$$
A=\operatorname{REASON}(\mathcal{H},q).
$$

## 关键结果

### V* 与 HR-Bench

![Table 1](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/page_005_fig_table_1.png)
*论文原图编号：Table 1。V*、HR-Bench-4K 与 HR-Bench-8K 主结果，所有视觉落地基线均围绕 Qwen2.5-VL-7B 构建。*

| 基准 | 原始 Qwen2.5-VL-7B | DeepScan | 绝对变化 |
| --- | ---: | ---: | ---: |
| V* 总体 | 74.3 | 90.6 | +16.3 |
| V* 属性 | 77.4 | 93.0 | +15.6 |
| V* 空间 | 69.7 | 86.8 | +17.1 |
| HR-Bench-4K 总体 | 72.1 | 75.0 | +2.9 |
| HR-Bench-8K 总体 | 68.8 | 72.4 | +3.6 |

DeepScan 在 V* 上的增益远大于 HR-Bench，符合方法定位：V* 的目标平均面积小于 `0.05%`，更需要主动寻找微小证据。它在 V* 上与强化学习方法 DeepEyes 接近，总体高 `0.6` 点，空间子集持平。

![Figure 2](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/page_002_fig_figure_2.png)
*论文原图编号：Figure 2。V* 上的方法定位：7B 版 DeepScan 达到 90.6，72B 版达到 94.2，接近 GPT-o3 的 95.0。*

### TreeBench

![Table 2](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/page_006_fig_table_2.png)
*论文原图编号：Table 2。TreeBench 的总体、mIoU、感知和二阶推理子任务比较。*

DeepScan 的总体分数为 `42.5`，证据定位 mIoU 为 `37.3`。相对原始 Qwen2.5-VL-7B，总体增加 `5.5` 点。

它的 mIoU 比 DeepEyes、Pixel-Reasoner、TreeVGR 分别高 `7.3`、`1.6`、`5.5` 点。

但提升并非覆盖所有推理项。TreeBench 的比较子任务为 `43.2`，与原始模型相同；物理状态和 OCR 等项目也不总是领先。作者据此提出强化学习可能主要偏置模型去主动感知，而不是从根本上增强视觉推理。这个判断有启发性，但只是从子任务模式推导出的假设，不是独立因果实验。

### 跨骨干组件增益

![Figure 7](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/page_006_fig_figure_7.png)
*论文原图编号：Figure 7。五种视觉语言骨干上的阶段消融，横轴为时延，纵轴为 V* 平均性能。*

LLaVA-1.5、Qwen2 和 Qwen2.5 的 7B、32B、72B 版本都呈现相同趋势：分层扫描贡献主要增益，再聚焦继续提升，证据增强推理以较小开销补充最后一段收益。这支持方法跨架构迁移，但不同模型的绝对时延仍明显增长。

### 外部专家与分层扫描消融

![Table 3](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/table3.png)
*论文原图编号：Table 3。搜索专家和视觉专家规模消融；更大的外部专家没有带来稳定收益。*

BLIP-ITM base 达到 `90.6`，large 为 `90.1`。

LangSAM 的 small、base+、large 版本分别得到 `89.5`、`89.5`、`90.6`。专家变大并不单调提高性能，说明主要贡献来自流程设计，而不是简单堆大辅助模型。

![Table 4](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/table4.png)
*论文原图编号：Table 4。检测式定位、完整分层扫描和去掉形态学后处理的比较。*

| 方案 | 总体 | 属性 | 空间 | 时延 |
| --- | ---: | ---: | ---: | ---: |
| 检测式证据定位 | 82.2 | 81.7 | 82.9 | 13.0 秒 |
| 完整分层扫描 | 90.6 | 93.0 | 86.8 | 24.5 秒 |
| 去掉形态学后处理 | 87.4 | 89.6 | 85.5 | 32.1 秒 |

形态学处理不仅让总体准确率增加 `3.2` 点，还把时延从 `32.1` 秒降到 `24.5` 秒。原因是更完整的掩码能覆盖同一对象上的其他代理，访问掩码因此减少重复处理。这个结果把“图像后处理”和“代理调用去重”连接起来，是论文很实用的工程发现。

### 点式代理与图块大小

![Table 5](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/page_007_fig_table_5.png)
*论文原图编号：Table 5。左侧比较不同点代理，右侧比较固定和按单/多对象动态选择的图块尺寸。*

融合式代理在属性和空间子集达到 `93.0 / 86.8`。质心仅为 `84.3 / 80.3`；切比雪夫中心偏属性，注意力峰值偏空间，二者融合后更稳定。

图块尺寸也与任务结构相关。小图块更能抑制单对象任务的背景噪声，大图块则为多对象空间关系保留必要上下文。动态使用 `576 / 768` 的总体结果为 `90.6`，优于单一尺寸。

### 再聚焦动作与搜索空间

![Table 6](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/table6.png)
*论文原图编号：Table 6。左侧为放大/缩小动作消融，右侧为 MCTS、A* 和四状态搜索的效率比较。*

单独使用放大时，属性/空间为 `89.6 / 73.7`；单独使用缩小时为 `87.8 / 72.4`；两种动作联合达到 `93.0 / 86.8`。这说明属性任务也可能需要补上下文，空间任务更不适合只做单向缩放。

在相同扩展预算 `4` 下，MCTS 和 A* 都枚举 `7` 个状态，到达最优状态的平均搜索长度为 `2.24` 和 `3.07`；DeepScan 的四状态集合长度为 `1.87`。这支持其状态剪枝在当前奖励和深度范围内有效。

![Figure 8](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/page_007_fig_figure_8.png)
*论文原图编号：Figure 8。缩小视图尺度消融；适中扩张能补回证据，扩张过大会重新引入干扰。*

### 自底向上与一次性定位

![Table 7](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/page_008_fig_table_7.png)
*论文原图编号：Table 7。使用相同专家时，自底向上定位和整图一次性定位的直接比较。*

| 定位范式 | 总体 | 属性 | 空间 | 时延 |
| --- | ---: | ---: | ---: | ---: |
| 一次性定位 | 83.8 | 83.5 | 84.2 | 20.4 秒 |
| 自底向上定位 | 90.6 | 93.0 | 86.8 | 24.5 秒 |

属性任务增加 `9.5` 点，空间任务增加 `2.6` 点。自底向上的优势主要来自找到细小目标，而不是普遍增强关系推理；代价是约 `4.1` 秒额外时延。

### 扩展性与工程效率

![Table 8](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/page_013_fig_table_8.png)
*论文原图编号：Table 8。视觉落地方法的路线比较：DeepScan 易于扩展，采用外部专家、自底向上搜索和混合粒度证据，但推理时延较高。*

![Table 9](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/page_013_fig_table_9.png)
*论文原图编号：Table 9。V* 上的补充结果，比较候选截断和 LVLM 规模。*

使用全部候选时，7B 版本从 `90.6` 升到 `91.1`；72B 版本从 `93.7` 升到 `94.2`。增加候选带来的收益只有 `0.5` 点，而时延明显增加，说明默认 $k=10$ 的截断较合理。72B 版本的空间准确率为 `93.4`，相对原始 72B 的 `80.9` 提升显著，表明更大模型主要把精确证据转化成更强关系推理。

![Figure 11](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/fig11.png)
*论文原图编号：Figure 11。不同模型规模随定位精度变化的性能；过度放大到目标本体会删除必要上下文。*

补充实验对确定性流程做批处理，并换用 vLLM 后端：

![Table 10](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/page_015_fig_table_10.png)
*论文原图编号：Table 10。工程优化后的精度、视觉词元成本与端到端时延比较。*

| 方法 | 准确率 | 视觉词元成本 | 时延 |
| --- | ---: | ---: | ---: |
| DeepEyes | 89.0 | 13k | 6.9 秒 |
| ZoomRefine | 82.7 | 5.1k | 0.9 秒 |
| DyFo | 83.8 | 7.2k | 2.4 秒 |
| 分层扫描 | 84.8 | 6.5k | 2.2 秒 |
| 再聚焦阶段 | 89.5 | 8.1k | 3.0 秒 |
| 完整 DeepScan | 90.1 | 8.4k | 3.1 秒 |

优化后完整系统约为原实现的八分之一时延。需要注意，这组补充结果使用 VLMEvalKit 与 vLLM，基础模型分数和主表略有变化，因此 `90.1 / 3.1 秒` 不应和主表 `90.6 / 24.5 秒` 拆开协议直接比较。

## 深度分析

### 真正贡献是提高视觉信噪比

DeepScan 的本质可以概括为测试时视觉信噪比控制。整图一次性搜索时，细小目标信号被背景淹没；切成图块后，目标占局部视图的比例提高，搜索专家更容易形成可靠注意锚点。点代理再把局部锚点提升回全图，避免局部裁剪截断对象。

这解释了为什么属性任务收益最大：颜色、文字、材质通常只需一个小证据。空间关系需要同时保持两个对象和相对语境，仅靠更精准局部定位还不够，因此提升更依赖再聚焦与更大推理模型。

### 定位更准不等于推理更强

TreeBench 结果清楚地划出边界：DeepScan 显著提高 mIoU 和总体分数，但比较推理子项没有超过原始 Qwen。论文关于强化学习“主要增强感知行为”的判断，同样可反过来用于 DeepScan：它首先是一个证据获取器，而不是新的通用推理算法。

![Figure 9](3d%20agent/DeepScan%20A%20Training-Free%20Framework%20for%20Visually%20Grounded%20Reasoning%20in%20Large%20Vision-Language%20Models/images/page_008_fig_figure_9.png)
*论文原图编号：Figure 9。GPT-4o、DyFo 和 DeepScan 的案例比较；DeepScan 能从极小目标或复杂场景中定位证据并给出可追踪答案。*

这些案例说明“有依据”也需要分层理解。正确证据支持正确答案；错误证据同样可能让模型给出措辞自信、看似可解释的错误答案。因此，视觉落地不会自动消除幻觉，它只是把错误来源暴露为可检查的证据选择。

### 再聚焦奖励的假设

奖励函数把证据完整性当作硬门槛，再偏好小视图。这个设计合理，但完整性由同一个视觉语言模型做二元判断。若模型错判“所有对象都已完整出现”，系统会过度裁剪；若错判不完整，又会保留多余背景。

四状态搜索的完备性也依赖若干假设，例如重复放大近似幂等、缩小可以直接从初始视图恢复语境。在真实图像边界、检测不稳定或非中心目标场景中，这些假设可能不成立。实验支持设计有效，但不等价于形式上覆盖所有最优裁剪。

### 失败如何传播

作者将失败分成两类：

1. 定位失败：多个相似物体仍位于证据邻域，视觉专家提出错误对象，模型又把它判断为有效证据，最终答案建立在错误证据上。
2. 推理失败：多个证据相距较远，最小包围框包含大量中间背景；这些噪声可能与正确空间关系冲突，导致模型推理错误。

第二类失败说明“保留空间关系”和“压缩上下文”存在结构张力。作者建议把分散证据重新合成为紧凑视图，但任何生成式重排都必须保留相对位置，否则它会解决噪声问题，却破坏要推理的几何关系。

### 与 3D agent 的关系

DeepScan 不是三维重建方法，但它对 3D agent 很有启发。Think3D、S-Agent 或 Skill-3D 在多视图和点云工具调用前，都需要决定当前问题真正依赖哪些视觉对象。DeepScan 可以充当证据前端：先在每一视图中定位细小目标，再把证据交给三维提升、跨帧记忆或技能规划。

它与 A4-Agent 的差别也很清楚。A4-Agent 用生成交互图推断“应操作什么部件”；DeepScan 不生成假想交互，而是系统扫描真实图像，寻找回答问题的证据。两者可以组合：先用 A4-Agent 生成部件语义，再用 DeepScan 在复杂场景中稳定找到对应细节。

### 复现注意点

1. 图块坐标到全图坐标的提升必须严格处理缩放和边界，否则点代理会系统偏移。
2. Otsu 阈值、连通域面积阈值、形态学核与膨胀半径共同决定候选数量，不能只复现网络模型而忽略图像处理参数。
3. 访问掩码与框去重会改变后续搜索路径，必须保存中间掩码和候选顺序以便调试。
4. 证据判断与视图完整性判断需要固定提示、温度和解析规则；二元回答之外的解释文本不应改变程序分支。
5. 主表与工程优化表使用不同实现协议，复现报告应分别标记标准流程和批处理流程。
6. 除平均准确率外，应报告定位错误、完整性误判、证据数量、视觉词元、端到端时延和峰值显存。

## 局限

第一，标准实现仍有较高时延。完整自底向上流程在主实验中约为 `24.5` 秒，明显慢于原始模型和一次性定位。工程优化缓解了问题，但需要批处理、vLLM 和多卡环境。

第二，固定图块策略对简单显著目标过度计算。当前方法主要针对细小证据设计，缺少先判断“是否需要扫描”的轻量路由器。

第三，定位阶段仍可能形成确认偏差。若搜索专家、视觉专家与模型都偏向同一个相似干扰物，二元证据判断可能把错误对象确认为真。

第四，分散证据的最小包围框会重新引入大量噪声。生成式重排是潜在方向，但它可能篡改空间关系，需要额外几何一致性约束。

第五，再聚焦依赖模型自评证据完整性。论文没有单独测量这一判断器的校准误差，也没有比较独立分类器或多模型一致性策略。

第六，主要 benchmark 是高分辨率选择题。开放式回答、长视频、连续代理任务和真实机器人操作中的幻觉率与任务成功率没有被系统评估。

第七，外部专家和基础模型会继承训练数据偏差。安全关键场景中的错误证据可能导致自动驾驶、机器人或界面代理采取错误动作，不能仅凭可视化证据就视为可靠。

## 我的笔记

- 这篇最值得复用的设计是“局部找线索，全图恢复对象”。它比局部直接裁出答案对象更稳，因为允许图块只包含对象的一小部分。
- 形态学后处理同时提高精度和降低时延，是很漂亮的系统结果：掩码质量决定了代理去重效率。
- 再聚焦的奖励比“越小越好”成熟，它明确把证据完整性放在面积之前；但完整性判断本身应该被校准和审计。
- 若用于自己的 3D agent，可以把细粒度证据、粗视图、点云对象和跨帧轨迹统一进一个分层证据记忆，而不是只保存文字摘要。
- TreeBench 提醒我不要把 grounding 提升写成 reasoning 提升。定位是必要条件，但第二阶空间关系仍主要取决于主干模型能力。
- 一个自然扩展是训练轻量路由器预测目标显著性、问题类型和证据分散程度，动态决定是否扫描、图块尺寸、候选数和再聚焦动作。

## 引用

Li, Yangfu; Zhan, Hongjian; Chen, Jiawei; Gong, Yuning; Liu, Qi; Lu, Yue. *DeepScan: A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models*. CVPR 2026; arXiv:2603.03857. DOI: 10.48550/arXiv.2603.03857.
