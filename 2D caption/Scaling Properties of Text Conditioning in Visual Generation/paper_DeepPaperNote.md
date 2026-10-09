# Scaling Properties of Text Conditioning in Visual Generation

## 核心信息

- **作者**：Zilong Chen, Chaorui Deng, Kunchang Li, Hongyi Yuan, Haoqi Fan（ByteDance Seed）
- **任务**：研究 text-to-image 中“文本条件控制”能否像模型规模、数据和算力一样被定量扩展。
- **核心结论**：真正可扩展的不是 caption token 数，而是 caption 中可被图像验证、且被条件接口明确暴露的**图像接地信息**。
- **技术主线**：用 GPG/ED 测量 caption information → 在固定训练配方下拟合 information–loss 关系 → 用 structured prompt 提升 diffuser 的 diffusability → 用 SFT、Cold-start、verifier-gated OPSD 提升 LLM prompter 的 promptability → 用短程 refine–render–judge 做 inference-time scaling。
- **代码/模型**：论文给出 GitHub、Hugging Face、Demo 与项目页链接；但完整复现仍依赖内部 Seed-VL、BAGEL CT checkpoint 及多个闭源 API judge。

## 原文摘要翻译

论文研究视觉生成中文本条件控制的经验缩放性质。自然语言提示的 token 数并不对应 diffusion loss 的稳定下降；相反，收敛 diffusion loss 会随结构化语言所携带的信息量而变化。作者采用两种互补指标：需要 token likelihood 的白盒 GPG，以及基于图像属性匹配的黑盒 ED。在受控训练中，loss 与 GPG 近似线性，与 ED 呈幂律。基于这一观察，作者以图像语义和几何标注构造 structured prompt 来提升 diffusability，再通过 SFT、Cold-start 和 verifier-gated on-policy distillation 训练 prompter 来提升 promptability。最终系统在几乎所有组合、推理和世界知识基准上超过所评估的开放权重模型，并在多数评测中达到或超过强闭源系统。

## 创新点

1. **把 caption information 变成受控训练变量，而不是把长度当代理变量。** 作者固定图像、架构、初始化、优化与预算，仅改变 caption condition；这是论文最有研究价值的实验设计。
2. **提供两个相互独立但高度一致的信息标尺。** GPG 依赖白盒 token likelihood，ED 依赖黑盒属性提取与匹配；两者对 15 个 caption configuration 的排序 Spearman $\rho=0.96$，减轻了单一指标“自证”的风险。
3. **将系统瓶颈拆成 Diffusability × Promptability。** 前者是 caption interface 对 diffuser 的训练可用性，后者是 LLM 从用户请求实例化该接口的能力。这个分解比“更长 prompt”或“更强 prompt enhancer”更清楚。
4. **训练 prompter 的 OPSD 设计。** 学生在无图条件下生成 on-policy rollout；冻结 teacher 看到配对图像；只有通过结构、对齐、美学门控的 rollout 才接受 image-conditioned token distribution 蒸馏。
5. **给出匹配 NL 控制。** 同样的 Qwen-Image、图像、训练阶段和预算，仅将中间接口改回自然语言，仍显著落后于 SP，说明提升不能简单归因于额外训练。

## 一句话总结

这篇论文不是在证明“JSON 比自然语言神奇”，而是在证明：当 caption interface 持续增加可验证的图像信息，并把对象、属性、几何和关系变成可寻址变量时，条件监督才会随之扩展；随后还需要一个足够强且经过训练的 LLM，把用户请求可靠地填进这个接口。

## 研究问题

论文依次回答四个问题：

1. 自然语言 caption 变长，是否真的让固定 diffuser 恢复更多图像内容？
2. 能否用 caption-side 指标，在训练 diffuser 之前预测某种 caption configuration 的收敛 loss？
3. 如果 structured prompt 更适合 diffusion learning，怎样从图像批量构造高质量结构化监督？
4. 推理时没有参考图像，怎样让 LLM prompter 产生足够详细、合理且可渲染的 SP？

前两个问题是 scaling study；后两个问题把测量结论变成完整系统。需要注意，后半部分系统工程规模远大于前半部分的“缩放定律”本身。

## 数据与任务定义

- scaling sweep 包含 **15 个 caption configurations**：3 个 NL richness level、6 个 nested SP level、3 个空间序列化变体，以及 3 个 field ablation。
- GPG 和 ED 均在共享的 **30,000 对图文**上测量；ED 使用双侧 10% trimmed mean。
- 每个 configuration 单独训练一个 BAGEL diffuser，到统一预算 $2.84\times10^{10}$ cumulative image tokens；每个设置只训练一次。
- 主系统改用 Qwen-Image-2512，并在 SP level 与 NL caption 混合语料上训练一次；之后固定 diffuser，比较 prompter。
- 端到端评测覆盖 GenEval、GenEval2、DPG-Bench、TIIF、WISE、T2I-CoReBench，并配合 GPT-5.4 offline structure/alignment/GSB judge。

## 方法主线

![Figure 1 — scaling overview](figure_1_scaling_overview.png)

### 机制流程

1. **Image → full annotation evidence**：Seed-VL 负责场景和局部语义；Sapiens 提供人体姿态；DepthAnything V2 提供相对深度；SAM 2.1 提供 mask 与遮挡线索。
2. **Evidence → L10 SP**：第二次 VLM pass 将证据组装为 global / per-element / cross-element 三个 scope 的 JSON record。
3. **L10 → L5–L9**：按预定义 field group 确定性遮蔽，形成信息逐级增加的 controlled ladder。
4. **Measure**：对每个 caption configuration 计算 GPG、ED，并与 matched-budget converged MSE 拟合。
5. **Train diffuser**：让结构化信息成为 diffusion conditioning supervision。
6. **Train prompter**：SFT 学 target SP distribution；Cold-start 学 image-free derivation；RFT 中用 gated OPSD 从 image-conditioned teacher 吸收 token preference。
7. **Generate**：单次 user prompt → SP → image；可选 agentic loop 根据 judge critique 修改具体字段。

### GPG：白盒的信息总量标尺

$$
\mathrm{GPG}(y,I)=\sum_{t=1}^{T}m_t\left[\log p_M(y_t\mid I,y_{<t})-\log p_M(y_t\mid\varnothing,y_{<t})\right].
$$

它度量“揭示配对图像后，caption 内容 token 的总 log-likelihood 增益”。这里的关键是 **total 而非 per-token rate**，并且 JSON 语法、样式 boilerplate 等不进入累计和。它可以随长度增大，但只有新增 token 真正被图像支持时才有意义。

### ED：黑盒的属性精确率优先标尺

$$
\mathrm{ED}(y,I)=F_{0.5}(P_A,R_A).
$$

图像侧 proposer 独立提取 OARG tuples，caption 侧 proposer 再提取文本 tuples，matcher 做同义容忍匹配。$F_{0.5}$ 强调 precision：错误属性会给 paired image 提供矛盾监督，遗漏属性只是减少带宽。附录显示改用 $F_1$ 或 $F_2$ 后预测能力明显下降。

### Structured prompt 为什么有效

SP 有三层：

- global：`intent`, `scene`, `atmosphere`, `photography`, `style`, `lighting`；
- per-element：`id`, `caption`, dynamic attributes/actions, `position`, `depth`, photography；
- cross-element：`relationships`。

真正作用不是花括号，而是**信息增量与寻址性**：每一级恢复新的 field group，而不是用更多连接词反复描述同一批实体。Figure 3 中 NL 从 470 增至 2,130 tokens，重建相似度基本不动；SP 随字段恢复，DINOv3/SigLIP2 上升、LPIPS 下降。

### Prompter 的三阶段训练

![Figure 10 — prompter training](figure_10_training_pipeline.png)

- **SFT**：约 333k examples / 0.97B tokens。核心 prompt→SP 任务约占三分之一，其余为推理/指令 replay。最大贡献是让模型学会 diffuser 期望的 SP 内容分布，而不只是合法 JSON。
- **Cold-start**：image-conditioned teacher 产生 `<analysis>` + SP，再由 Gemini 五轴 validator 严格筛选。172,208 candidates 中接受 58,907（34.2%），去重后 50,182。
- **RFT / gated OPSD**：学生无图 on-policy rollout；teacher 有图；render 后通过三个至少 6/10 的门控才做 top-64 teacher logits KL 蒸馏。这里 verifier 只筛数据，不和 OPSD 做加权 reward 混合。

### 推理时的字段级修正

![Figure 14 — agentic loop](figure_14_agentic_loop.png)

judge 不看 SP，只看 user request 与生成图，输出结构、对齐、美学分数和 `(field-path, observed, expected)` 问题列表。失败后，prompter 修改对应 SP slot；多次失败才升级到 regroup 或 full re-planning。这个接口天然比自由文本 caption 更适合局部修正。

## 关键结果

![Figure 7 — information–loss relations](figure_7_scaling_laws.png)

### 主结果与强基线

- 15 个设置上：

$$
\mathrm{MSE}=0.4549-8.45\times10^{-5}\cdot \mathrm{GPG},\quad r=-0.984,
$$

$$
\mathrm{MSE}=0.4200\cdot \mathrm{ED}^{-0.2073},\quad r=-0.971.
$$

- residual SD：GPG 约 $6\times10^{-4}$，ED 约 $7.8\times10^{-4}$。
- configuration holdout：只用 NL + nested-SP 拟合，再预测 6 个 spatial/field variants，MAE 分别为 $5.0\times10^{-4}$ 与 $8.1\times10^{-4}$。
- SP ladder 的 GenEval2 GM 从 L5 的 **46.79** 单调升到 L10 的 **57.70**；相对 L5 的 GSB 从 8.0% 逐步升至 **26.0%**。
- 端到端 Ours：GenEval **0.94**、GenEval2 AM/GM **90.6/72.5**、DPG **90.71**、TIIF **89.1/89.2**、WISE **0.89**、CoReBench **85.2**。
- 最关键 matched NL 对照：GenEval2 GM **56.2 → 72.5**，CoReBench **76.1 → 85.2**。这比“超过某个闭源模型”更能支撑方法因果解释。

### 消融到底说明了什么

- field ablation 中，移除 scene background：MSE **+35.3×10⁻⁴**，GPG **−42.0**；移除 bbox：MSE **+14.4×10⁻⁴**。scene context 与 bbox 是主要训练贡献。
- depth、relationships、atmosphere/lighting 的 marginal MSE 增量仅 **0.4–1.5×10⁻⁴**。这不等于它们无用：它们可能对局部正确性、编辑性和特定 benchmark 更重要，但总体 loss 对它们不敏感。
- prompter pipeline：Base structure **4.860**；SFT **6.273**；Cold-start **6.753**；full gated OPSD **7.600**。GSB 从 SFT 的 **23.3%** 升至 full 的 **42.0%**。
- DPG 只从 89.42 到 90.71，说明 DPG 对结构密度和复杂布局不够敏感；不能只凭该指标判断后训练是否有效。
- agentic loop：trained prompter 从 1 round 的 structure **7.600 / GSB 42.0%** 提升到 8 rounds 的 **8.260 / 54.7%**，但平均只消费 2.31 rounds，且 4→8 收益很小。

### Prompter scaling

零样本 Qwen3.5 从 0.8B 到 397B，在 thinking mode 的 GenEval++ 从 **46.4%** 升到 **86.8%**。除 0.8B 外，CoT 通常有效；0.8B 容易陷入重复循环并生成无效 JSON。说明通用 LLM 进步能够通过 SP interface 转移为视觉生成增益，但规模与 reasoning 仍不能代替 task-specific SFT/RFT。

## 深度分析

### 真正贡献是什么

最扎实的贡献是**实验变量的重新定义与控制**：过去讨论 long caption，往往把 token length、事实数量、组织方式和 annotation quality 混在一起。这篇论文明确提出 caption information，并用 15-cell matched training sweep 将它和 converged loss 对齐。

系统方面真正新颖的是将训练期“有图监督”与推理期“无图 prompt expansion”拆开：SP 只解决 diffuser 如何读，prompter 还要解决用户没说的视觉决策怎样合理补全。OPSD 正面利用了这个 conditioning asymmetry。

### 为什么结果成立

1. **条件带宽增加**：SP ladder 实际增加新的对象属性、场景、几何和关系事实，降低 $H(I\mid Y)$ 的直觉成立。
2. **变量可寻址**：同一类信息总出现在稳定字段中，text encoder / diffuser 不必从自由 prose 的句法变化中重新定位变量。
3. **错误监督被显式控制**：domain experts 改善 pose、depth、mask 等明确字段，避免错误几何成为硬 conditioning variable。
4. **prompter 学的是视觉 completion prior**：SFT 的目标不是恢复唯一 ground-truth layout，而是学习 diffuser 训练分布中的合理 SP completion。
5. **on-policy distillation 缩小 train–inference gap**：teacher 在学生真实会访问的 prefix 上给分布，而不是强迫学生模仿其无图条件下不可到达的完整行为。

### 容易误读的地方

- **不是“token 越多越差”**：Figure 1 的结论是无新增信息的 prose ladder 饱和或退化；长度本身不是因果毒素。
- **不是“JSON syntax 导致缩放”**：NL/SP 对比同时改变了信息丰富度和组织方式，论文也明确承认未隔离 JSON syntax。
- **不是 universal scaling law**：这是 BAGEL、特定初始化、训练目标、预算、caption family、judge recipe 下的 empirical calibration。
- **Eq. (5) 不是拟合的乘法质量公式**：`Diffusability × Promptability` 是概念分解，不是可直接代数预测的 law。
- **低 loss 不自动等于更好的所有视觉维度**：paper 用 downstream evaluation 补证，但个别字段的 loss marginal effect 与编辑/组合价值并不等价。
- **GPG 不是严格 mutual information**：no-image pass 是 model prior，不是数据边际；MSE 也不是以 nat 为单位的 conditional likelihood bound。

### 复现注意点

- BAGEL scaling fit 使用内部 continued-training checkpoint；这会影响绝对 loss 与 slope。
- 默认 GPG judge 是 Qwen3.5-397B-A17B；bbox coordinate convention 不兼容会直接翻转排序。Qwen2.5-VL-7B 未做 adapter 时 $r=+0.23$，适配后恢复到 $-0.97$。
- ED 依赖 Gemini 3 Pro image proposer 与 GPT-5.4 caption proposer/matcher。不同 extractor 的绝对 ED 不可直接比较，ICC absolute agreement 仅 0.11。
- 每个 scaling cell 只有一次训练，无法估计 seed-level variance。Figure 7 的 band 是 sweep-setting resampling，不是 training-run CI。
- Qwen-Image 训练是 512 GPUs、500k steps；BAGEL 是 192 GPUs。即使代码开放，完整复现成本很高。
- prompter 是 Qwen3.5-397B-A17B 上 rank-128 LoRA；SFT/Cold-start 使用 Megatron，RFT 使用 ZeRO-3 + colocated vLLM。
- 依赖中 Seed-VL 为 internal；Sapiens 与 DepthAnything large checkpoint 是 non-commercial；TIIF/WISE upstream 无 license file。
- offline evaluation 大量依赖 GPT-5.4，online gate 依赖 Gemini；应固定模型版本、prompt、重试和 aggregation。

## 局限

1. **经验关系的外推范围窄。** quantitative fit 没有在 Qwen-Image 上重拟合，也没有覆盖视频、3D 或不同 objective。
2. **单次训练不足以称“定律”。** 高相关可能部分来自人为设计的有序 ladder；虽然 holdout variants 有帮助，但仍缺独立 caption families 与多 seed replication。
3. **指标开发与主 sweep 不是完全独立。** GPG mask/canonicalization 与 ED 的 $\beta=0.5$ 在 controlled BAGEL sweep 上开发后冻结，会带来 calibration selection bias。
4. **闭源 evaluator 依赖重。** GPG/ED、Cold-start filtering、RFT gate、offline metrics 都使用超大或闭源模型；测量、训练与评测之间可能存在共同偏好。
5. **手工 schema 的上限。** schema 设计决定哪些视觉因素可见；未被字段覆盖的因素仍可能丢失，且自动 schema discovery 未解决。
6. **延迟与成本。** 单次 prompter 本身很大；agentic loop 每轮约 20–35 s，并有三次 judge call。
7. **端到端 claim 略强。** “超过所有 open-weight、匹配 closed-weight”依赖特定 benchmark/evaluator/provenance；最可信的证据仍是 matched NL control，而非跨系统 leaderboard。

## 与 2D caption / text conditioning / visual generation 脉络的定位

这篇工作位于 recaptioning（DALL-E 3、RECAP、DOCCI）与 structured control（GLIGEN、layout intermediary）之间，但研究对象不同：它不只问“详细 caption 有没有用”，也不只把 layout 当额外 control，而是把**条件信息量**定义为训练侧可测变量，并要求同一接口同时服务训练和推理。

与 FIBO、Cosmos 3、Reve 2.0 等 structured caption 工作相比，它最明显的增量是：

- 用同一 GPG/ED 轴比较 NL、SP、spatial serialization 和 field ablation；
- 用 matched-budget converged loss 做训练侧 calibration；
- 固定 schema/diffuser，系统研究 prompter scale、reasoning、post-training 与 agentic refinement；
- 给出 matched NL end-to-end control。

对 2D caption 研究的启示是：后续数据工作不应只报告平均 caption length 或 lexical diversity，而应报告**新增事实是否被图像支持、是否提高属性 precision、是否以稳定字段暴露、以及是否真正降低 matched training loss**。对视觉生成系统而言，captioner/prompter 不再只是数据预处理，而是决定条件带宽与结构的可训练组件。

## 我的笔记

- 我会把这篇论文的核心抽象写成：**caption scaling = grounded content scaling + addressability scaling**。GPG/ED 主要量化前者，NL/SP 与 field ladder 混合反映后者。
- 最值得复用的实验模板不是 397B prompter，而是 15-cell controlled sweep + configuration holdout。它可以迁移到视频 caption、3D scene graph、robot trajectory description：先测 condition information，再看固定模型 loss 是否可预测。
- 下一步最关键实验应是：多 seed；新 backbone 重新标定；独立开发 metric；在相同 facts 下严格比较 prose / JSON / graph serialization；以及以 human-verified attribute set 代替闭源 judge 做小规模 gold validation。
- field ablation 表明 scene context 远强于 depth/relationship 的平均 loss 贡献，但这可能是 loss 对稀疏高阶约束不敏感。若研究目标是 compositional reasoning，应专门构造针对 relation/depth 的 conditional evaluation，而不是只看 global MSE。

## 引用

Chen, Z., Deng, C., Li, K., Yuan, H., & Fan, H. *Scaling Properties of Text Conditioning in Visual Generation*. Technical Report, ByteDance Seed, 2026.
