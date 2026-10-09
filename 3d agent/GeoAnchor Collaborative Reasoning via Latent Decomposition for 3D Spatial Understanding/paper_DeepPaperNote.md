---
tags:
  - papers/3d-spatial-reasoning
  - papers/multimodal-llm
  - papers/latent-reasoning
aliases:
  - GeoAnchor
  - Latent Decomposition for 3D Spatial Understanding
date: 2026-08-25
doi: 10.48550/arxiv.2607.13454
arxiv_id: 2607.13454
---

# GeoAnchor：通过潜在分解协作推理实现 3D 空间理解

## 核心信息
- 标题: GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding
- 标题翻译: GeoAnchor：通过潜在分解协作推理实现 3D 空间理解
- 作者: Hao Li, Han Fang, Zixin Pan, Xin Wei, Hongbo Sun, Jinglin Xu, Zhiyu Lin, Ye Yuan, Zhongjiang He, Yu Yu, Hao Sun
- 机构: 上海交通大学；Xingchen AGI Lab / 中国电信人工智能科技（北京）有限公司；北京科技大学；香港科技大学（广州）
- 发表时间: 2026（论文标注 arXiv:2607.13454v2，2026-07-28）
- 发表渠道: arXiv
- DOI: 10.48550/arxiv.2607.13454
- arXiv: 2607.13454
- 论文链接: https://arxiv.org/abs/2607.13454
- 代码 / 项目: https://github.com/JerryPW/GeoAnchor
- 数据 / 资源: ScanNet 派生 3D grounding 数据；SPAR、SpatialLadder-26K、VGGT 特征
- 论文类型: 多模态大模型的 3D 空间推理方法论文

## 原文摘要翻译
尽管多模态大语言模型（MLLM）已经取得显著进展，但从二维图像理解三维空间关系仍然是一个关键挑战。现有方法主要依赖符号化文本 token，而文本 token 天然缺乏表达连续几何信息所需的保真度。近期方法开始使用潜在表示增强推理，但依赖单一潜在类型无法适应空间任务的多样性，因而会在复杂几何场景中产生错位。为解决这些问题，我们提出 GeoAnchor，一种交错式文本—潜在推理框架。GeoAnchor 将三维空间信息分解为三个互补成分：用于目标物体定位的位置潜变量、用于关系朝向的方向潜变量，以及用于场景结构的几何潜变量。这些成分在结构化空间中重新组合，以构造局部证据并捕获全局上下文，从而实现动态且可解释的推理。此外，我们提出协作式训练策略，引导模型从局部空间感知逐步发展到完整的三维理解。在多样且复杂的三维推理任务上的大量实验表明，GeoAnchor 超越了当前最优方法，验证了其有效性和泛化能力。

## 创新点
1. **把“空间潜变量”拆成有物理语义的三类锚点。** 位置、方向、几何分别对应目标 grounding、对象间朝向和场景级结构，避免一个潜变量同时承担所有几何语义。
2. **局部证据与全局上下文协作，而不是只增加一个 3D encoder。** 位置/方向 latent 为查询对象提供可追踪的局部证据，geometry latent 以软覆盖方式吸收 VGGT 的场景结构，问题需要时再组合。
3. **四阶段训练把潜变量从“被监督的几何码”变成“可自主调用的推理变量”。** 先学习局部坐标，再联合局部—全局 latent，继而移除显式 latent 监督使其回到语言流形，最后用带 pattern reward 的 GRPO 学习何时只用局部、何时调用全局。
4. **用 coverage 而非 token-to-token 对齐监督全局几何。** 多尺度池化后的 VGGT 特征只要求被若干 geometry token 覆盖，并用平衡项避免 token 塌缩，适合把高分辨率几何压缩为少量 latent。

## 一句话总结
GeoAnchor 的真正贡献不是“使用 latent reasoning”本身，而是为不同空间证据规定了可组合的 latent 角色，并用 coarse-to-fine 训练让模型学会按问题选择局部或局部加全局路径；在作者的设置中，这使 2B 模型在 SPAR-Bench、SPBench 和 ViewSpatial 上分别达到 68.4%、69.7% 和 47.0% 平均准确率。

## 研究问题
论文针对一个明确的表示错配：二维图像中的深度、距离、方向和视角变化是连续几何量，但 MLLM 的自然推理轨迹主要由离散文本 token 构成。文本 CoT 可以说出“物体在左边”或生成数字，却不保证中间状态保留了可靠的几何证据；另一方面，已有 latent spatial reasoning 通常用单一 latent 或单一深度图监督，难以同时表达局部目标关系和全局布局。

具体任务包括深度/距离估计、相对位置和方向、物体大小、相机视角与人物视角转换，以及 viewpoint change 后的空间想象。论文的关键假设是：不同问题需要不同粒度的证据；精确距离更依赖局部坐标，跨对象或视角推断则需要方向与全局结构。因而 latent 设计应当具有功能分工，而不是一个不可解释的连续瓶颈。

## 数据与任务定义
### 训练数据
- **Stage 1 grounding 数据。** 从 ScanNet 的 1,500+ scans、超过 250 万个视图中采样 10k 个场景。Qwen3-VL-32B 为每张图最多提取 5 个显著物体、指代表达和 2D 框；用 Depth Anything v3 估计深度和相机姿态，再通过反投影得到 3D 坐标，并由坐标差得到方向。最终保留 549,440 个样本：224,990 个单位置问题、159,530 个多位置问题、164,920 个方向问题。
- **Stage 2/3 与 RL 数据。** 从 SPAR 采样 100k 个问题，并加入 SpatialLadder-26K 的 5k 个样本，共 105k。论文还使用 VGGT 为每张图提取全局几何特征。
- **伪深度质量。** 附录报告，伪深度恢复坐标相对 ground-truth depth 的平均/中位欧氏误差为 0.09 m/0.04 m，Acc@0.5m 为 98.0%，Acc@0.2m 为 92.9%。grounding 自一致性过滤后，47,663 个候选标注中 44,998 个通过，保留率 94.41%，平均/中位 IoU 为 0.787/0.856。

### 评测集与指标
SPAR-Bench 使用单图子集 2,866 样本，覆盖深度、距离、邻近关系、物体关系和空间想象；SPBench-SI 使用 1,009 样本，覆盖相对方向、相对距离、绝对距离和物体大小；ViewSpatial-Bench 使用 4,607 个单图样本，评估相机视角和人物视角下的方向与物体朝向。选择题直接算准确率；数值题按照置信度阈值 0.5 至 0.9、步长 0.05 的平均准确率计算。

## 方法主线
### 机制流程
1. **交错生成。** 给定图像 $I$ 和问题 $Q$，模型生成文本与 latent 交错的轨迹 $O=t_1\oplus z_1\oplus\cdots\oplus z_{k-1}\oplus t_k$。文本承担语义规划和逻辑表达，latent 保留连续 3D 证据。
2. **生成并回灌 latent。** 每个 latent 是长度为 $M$ 的连续 hidden-state 序列。输出 hidden state 经过 projector $P(h)=\mathrm{LayerNorm}(h)+\mathrm{MLP}(\mathrm{LayerNorm}(h))$ 后回灌输入 embedding 空间，避免输出流形与输入流形不一致造成 latent drift。
3. **构造局部—全局证据。** 位置 latent 解码为 3D 坐标，方向 latent 解码为 3D 向量；geometry latent 投影为少量 geometry tokens，与多尺度池化的 VGGT 特征做 soft coverage 对齐。
4. **按问题选择路径并回答。** 模型可执行 local-only 或 local-plus-global 模式；GRPO 的 pattern reward 根据组内平滑准确率鼓励更适合当前问题的路径，最终文本 token 读取 latent 证据完成答案。

### 三类潜在 token
位置与方向 latent 分别定义为 $z_{pos}=\{h^{pos}_j\}_{j=1}^{l_{pos}}$、$z_{dir}=\{h^{dir}_j\}_{j=1}^{l_{dir}}$。对序列平均后用独立线性头映射到 $\hat p,\hat d\in\mathbb R^3$：
$$\hat p=W_{pos}\frac{1}{l_{pos}}\sum_j h^{pos}_j,\quad \hat d=W_{dir}\frac{1}{l_{dir}}\sum_j h^{dir}_j.$$
位置用 Smooth L1 loss，方向用余弦损失 $L_{dir}=1-\frac{\hat d\cdot d}{\|\hat d\|\|d\|}$。这种监督很重要：它让“第一个局部 latent”不只是模型内部的任意连续向量，而是有可检查的坐标/方向语义。

geometry latent 不进行密集的一一对应。VGGT 最后一层特征图经分辨率 ${1,2,4}$ 的多尺度平均池化并展平，得到 $V\in\mathbb R^{l_{vggt}\times D}$；geometry latent 经线性层得到 $G=\{g_j\}_{j=1}^{l_{geo}}$。对每个 VGGT feature，计算与每个 geometry token 的相似度并 softmax，使每个 VGGT 区域至少被一个 token 覆盖；同时加入 token 使用均衡项，防止所有信息集中在单个 geometry token。该设计承认高分辨率特征与紧凑 latent 的粒度不可能严格相等。

### 四阶段协作训练
- **S1：局部感知 warm-up。** 目标为 $L_{S1}=\lambda_tL_{NTP}+\lambda_l(L_{pos}+L_{dir})$。以 3D grounding 先建立可靠的对象级空间锚点。
- **S2：空间 latent reasoning。** 在 105k 空间推理样本上同时训练文本、位置、方向和几何损失：$L_{S2}=\lambda_tL_{NTP}+\lambda_l(L_{pos}+L_{dir})+\lambda_gL_{geo}$。模型开始按问题组合局部与全局证据。
- **S3：latent relaxation。** 令 $\lambda_l=\lambda_g=0$，只保留文本监督。作者的解释是，过强几何对齐可能把 latent 拉离语言流形；这一阶段让 latent 能够参与语言推理而不是只做几何回归。
- **S4：自适应 latent RL。** 用 GRPO 对 local-only 与 local-plus-global 两种 pattern 采样。除格式和准确率奖励外，组内按 EMA 平滑准确率选出表现更好的 pattern，额外加 $r_{pattern}$。这不是单纯追求更多 latent，而是将“调用全局信息的代价”转化为可学习的选择行为。

## 关键结果
### 主结果与强基线
| 模型 | SPAR-Bench Avg. | SPBench Avg. | ViewSpatial Avg. |
|---|---:|---:|---:|
| GPT-4o | 40.1 | 49.4 | 43.6 |
| Gemini-2.5-Flash | 48.7 | 44.7 | 45.5 |
| Qwen3-VL-2B（基线） | 32.4 | 52.9 | 37.2 |
| SpatialLadder | 32.4 | 69.6 | 45.4 |
| GeoAnchor | **68.4** | **69.7** | **47.0** |

GeoAnchor 在 SPAR-Bench 比基线高 36.0 个百分点，在 SPBench 高 16.8 个百分点，在 ViewSpatial 高 9.8 个百分点（论文正文概括为 10.7% gain，按表中 37.2→47.0 是 9.8 个百分点；这一处应以表格原始数值为准，避免混用相对提升与百分点）。它还超过 GPT-4o 和 Gemini-2.5-Flash 的平均分，但并非所有子任务都绝对领先：SpatialLadder 在 SPBench 的 Abs. 指标略高，说明 GeoAnchor 的优势主要是整体和跨任务稳健性，而非每个数值子任务都占优。

### 消融到底说明了什么
| 推理范式 | SPAR | SPBench | ViewSpatial | Avg. |
|---|---:|---:|---:|---:|
| Qwen3-VL-2B | 32.4 | 52.9 | 36.3 | 40.5 |
| Vanilla SFT | 56.4 | 58.1 | 40.9 | 51.8 |
| Text CoT SFT | 60.1 | 52.9 | 42.2 | 51.7 |
| 单一 latent | 62.4 | 57.8 | 40.5 | 53.6 |
| 仅 local tokens | 65.8 | 66.9 | 44.4 | 59.0 |
| 仅 global token | 63.8 | 64.3 | 46.0 | 58.0 |
| local + global | 67.5 | 68.8 | 46.3 | 60.9 |

连续几何 latent 的收益大于单纯 text CoT，且分解设计比“latent”这一标签本身更关键：local-only 与 local+global 的提升说明位置/方向证据可单独工作，但完整组合在三项 benchmark 上最好。

协作训练的平均分从仅 S1+S2 的 60.9，加入 S3 后达到 61.7；直接延长 S2 并不能复制这一收益。GRPO 无 pattern reward 时为 SPAR/SPBench/ViewSpatial = 67.8/69.2/46.2；加入 pattern reward 后为 68.4/69.7/47.0。论文还报告 Stage 1、2、3 相对增益分别为 5.0%、14.6%、23.0%，但这些是作者的增益概括，需结合 Table 3 的具体配置理解，不能当作统一的百分点定义。

局部 token 可解释性消融中，position-only 在 Position/Direction/Mixed 上为 65.2/36.5/55.8，direction-only 为 62.9/38.7/53.5，完整 local tokens 为 66.4/39.4/57.0；这支持两种局部证据各自有专门语义。VGGT 对齐中，提出的 soft coverage + multi-scale pooling 达到 68.4/69.7/47.0，优于 mean pooling 的 59.9/66.8/45.5、adaptive pooling 的 66.9/66.5/44.4 和 linear interpolation 的 53.7/60.2/37.3。

### 机制证据与失败案例边界
注意力分析显示，GeoAnchor 的最终答案 token 更关注 latent token，且 local latent 在不同位置上分别关注对应的目标区域；Text CoT 的注意力更多落到语义较弱的数字/符号。t-SNE 中 geometry token 位于 VGGT 与 text token 之间，支持 S3 使其兼顾几何和语言流形的解释。

论文没有提供一个系统的“失败案例”章节，也没有按错误类型公开逐样本分析。因此不能从图 5/6 的注意力可视化推出模型在遮挡、深度估计错误、跨域相机姿态或极端数值范围下必然成功。可确认的反例边界是：SpatialLadder 在 SPBench Abs. 略胜；ViewSpatial 仍只有 47.0%；而且作者把 2D 图像反投影得到的伪深度作为局部监督，潜在误差主要集中在深度轴。

## 深度分析
### 真正贡献是什么
工程组件包括 Qwen3-VL、VGGT、Depth Anything v3、ScanNet 派生数据和 GRPO；论文的核心研究贡献在于**把 latent 的语义角色显式化，并将角色选择纳入训练目标**。这比给模型加一个深度 latent 更有解释力：position 是“在哪里”，direction 是“朝哪里/相对谁”，geometry 是“场景整体怎样组织”。模型可以在同一个文本—latent 序列里组合这些证据，而不是把全部几何压成一个无名向量。

### 为什么结果可能成立
1. S1 的坐标/方向损失提供了比答案 token 更密集的几何学习信号，降低了空间任务对语言记忆的依赖。
2. geometry 的 soft coverage 避免了将高分辨率 VGGT 特征硬塞到 8 个 token 的不适定一一对齐，同时 balance loss 防止表示塌缩。
3. S3 解决几何监督与语言生成之间的流形冲突；S4 再解决固定调用全局 latent 的冗余问题。因此收益来自训练顺序和推理路径的共同作用，而非某个单独 loss。

### 容易误读的地方
- “提升 21.2%”是正文摘要对比基线的概括，不等于三项平均准确率都提升 21.2 个百分点；Table 1 中 SPAR、SPBench、ViewSpatial 相对基线的百分点差异分别为 36.0、16.8、9.8。
- “超过 GPT-4o”是本文评测协议下的 benchmark accuracy，不意味着 2B 模型具有更广泛的通用空间智能。
- 注意力和 t-SNE 是支持性证据，不是对 latent 语义的因果证明；尤其 t-SNE 的邻近关系依赖投影设置。
- 论文标题中的“3D spatial understanding”主要是单图输入下利用伪 3D/场景先验完成空间任务，不等同于端到端重建真实可度量的完整三维世界。

### 复现注意点
- 基座为 Qwen3-VL-2B，local length $l_{pos}=l_{dir}=2$，global length $l_{geo}=8$；作者使用 8 张 NVIDIA A800。
- S1 一轮，batch size 64，学习率 $10^{-4}$；S2/S3 各一轮，batch size 32，学习率 $2\times10^{-5}$；$\lambda_t=\lambda_l=1,\lambda_g=0.1$。
- VGGT 使用 3 个池化尺度 ${1,2,4}$，$\lambda_{bal}=0.05$。RL 每题 8 次 rollout，temperature 1.0，pattern reward 0.5，KL 系数 0.01，学习率 $5\times10^{-7}$，EMA 参数 $\kappa=8,\mu=0.2$。
- 数据再现并不只需要论文中的 105k QA：还需要 Qwen3-VL-32B 的 object extraction prompt、Depth Anything v3 的深度和姿态、VGGT 特征抽取、IoU 自一致性过滤及相机反投影实现。ViewSpatial 的相关训练集未公开，论文只使用其评测集。
- 需要核对作者代码仓库的 commit、模型权重、VGGT 版本、数值答案判分脚本和 GRPO prompt；这些因素足以改变绝对准确率。

## 局限
1. **监督链条含伪标签误差。** 2D 框由 Qwen3-VL-32B 生成、深度由 Depth Anything v3 估计，虽有自一致性和误差统计，但不是人工逐点 3D 标注。
2. **数据与 benchmark 共享场景来源。** ScanNet 同时出现在 grounding、SPAR 和部分评测中，跨数据集泛化不等价于跨传感器、跨域或真实机器人部署泛化。
3. **自适应 pattern 的效率收益尚未量化。** 作者声称更 concise、efficient，但正文没有报告平均 latent 数、token 数、延迟或显存节省；目前更直接的证据是准确率提升。
4. **缺少公开的系统失败分析。** 没有按遮挡、薄物体、深度不可靠、视角转换幅度、数值距离范围给出错误率，因此不能确定方法的失效边界。
5. **基线协议仍可能不完全同质。** GPT-4o、Gemini-2.5-Flash、不同开源模型和专用模型的提示、视觉输入处理和推理预算在论文主文中未完全展开；跨模型结论应谨慎表述。
6. **latent 解释性仍是功能性解释。** 解码头和注意力图表明 position/direction 有专门化趋势，但还不足以证明 latent 严格对应独立的因果变量。

## 我的笔记
### 与 3D agent 研究地图的关系
GeoAnchor 位于“空间推理 agent”而不是世界模型或动作策略的交叉点。它不预测未来状态、不执行导航动作，也不构建可交互场景；它解决的是视觉语言模型内部如何保留和调用几何证据。对后续 embodied agent，最值得借鉴的是把视觉状态拆成可调用的证据槽位，再让策略决定何时需要全局场景信息。

### 可继续追问的研究方向
- 把 position/direction/geometry 从固定三类扩展为可学习的关系图 latent，并用对象级不变性或跨视角一致性约束验证其稳定性。
- 将 pattern reward 改成显式计算预算奖励，报告 latent 数、延迟和准确率的 Pareto 曲线，而不仅是 accuracy。
- 在真实 RGB-D、稀疏多视图和机器人 egocentric 视频上测试，区分“场景数据记忆”与真正的几何迁移。
- 用人工 3D 标注和扰动深度做监督噪声敏感性实验；特别检查深度轴误差是否会系统性影响绝对距离和 viewpoint change。
- 增加逐样本失败 taxonomy，并验证注意力图、t-SNE 与真正的几何正确性之间是否相关。

## 引用
Li, Hao, et al. “GeoAnchor: Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding.” arXiv:2607.13454v2, 2026. https://arxiv.org/abs/2607.13454

原始 PDF：`/Users/roywangj/research/papers4zotero/zotero1/storage/ARI4BIJK/Li 等 - 2026 - GeoAnchor Collaborative Reasoning via Latent Decomposition for 3D Spatial Understanding.pdf`
