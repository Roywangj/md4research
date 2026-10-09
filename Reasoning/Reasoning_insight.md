# Reasoning Insight：从“交错视觉 CoT”到可验证的工具轨迹

> 研究目标：精读本地 `Reasoning` collection 后，回答一个比“怎样让模型多看图”更重要的问题：**怎样让模型生成真正依赖外部证据、能够被训练、审计和迁移的工具调用轨迹？**
>
> 证据范围：本文基于当前目录中的论文精读笔记、实验表格与 source anchors；没有把本地材料之外的最新工作混入结论。文中明确区分论文证据、综合推断与待验证假设。

## 0. 一句话结论

这组论文共同指向一个判断：

> **高质量多模态 reasoning 的最小单元不是更长的文本 CoT，也不是插入一张中间图像，而是一次闭环的认识行动：`不确定性 → 证据需求 → 工具动作 → 环境观察 → 证据解释 → 反事实验证 → 停止/继续`。**

工具只有在三个条件同时成立时才构成推理：

1. 它获取了原上下文中不足或不可用的信息；
2. 返回结果被后续判断实际使用；
3. 删除、置换或破坏该结果会以可预测方式影响答案。

如果缺少第 3 条，漂亮的中间图、代码块和多轮轨迹都可能只是“推理舞台布景”。

## 1. 文献图谱：这组工作分别解决了哪一层

| 层次 | 代表工作 | 论文直接解决的问题 | 仍未解决的问题 |
|---|---|---|---|
| 是否需要额外推理 | [SDR-MCoT](<TrainingFree/Mitigating Low-Quality Reasoning in MLLMs Self-Driven Refined Multimodal CoT with Selective Thinking and Step-wise Visual Enhancement/paper_DeepPaperNote.md>) | 用首标记熵选择直接回答或进入长推理；避免所有样本一律 CoT | 开放式 agent 任务中，首标记熵未必代表整体决策风险 |
| 去哪里找证据 | [DeepScan](<TrainingFree/DeepScan A Training-Free Framework for Visually Grounded Reasoning in Large Vision-Language Models/paper_DeepPaperNote.md>)、[ICoT](<TrainingFree/Interleaved-Modal Chain-of-Thought/paper_DeepPaperNote.md>)、[DaP-ICoT](<TrainingFree/Lets Think with Images Efficiently An Interleaved-Modal Chain-of-Thought Reasoning Framework with Dynamic and Precise Visual Thoughts/paper_DeepPaperNote.md>) | 分层扫描、注意力选择、动态插入局部视觉内容 | 选中的视觉内容是否真是答案的因果证据 |
| 怎样在长推理中保持视觉证据 | [VisRef](<TrainingFree/VisRef Visual Refocusing while Thinking Improves Test-Time Scaling in Multi-Modal Large Reasoning Models/paper_DeepPaperNote.md>)、[Qwen Look Again](<Train/Qwen Look Again Guiding Vision-Language Reasoning Models to Re-attention Visual Information/paper_DeepPaperNote.md>) | 测试时重注入相关且多样的视觉 token；训练模型主动回看 | token 级“相关”不保证对象完整，也不保证证据必要 |
| 怎样高效回看 | [PRCR](<TrainingFree/Position Rebinding Cache Reuse Replay-Free Visual Revisiting for Interleaved Multimodal Reasoning/paper_DeepPaperNote.md>) | 保存 RoPE 前视觉 K/V 与空间坐标，在当前解码位置重新绑定 | 只能复用已编码证据，不能生成新视角或新尺度观察 |
| 怎样学习视觉中间轨迹 | [PatchCue](<Train/PatchCue Enhancing Vision-Language Model Reasoning with Patch-Based Visual Cues/paper_DeepPaperNote.md>)、[MINT-CoT](<Train/MINT-CoT Enabling Interleaved Visual Tokens in Mathematical Chain-of-Thought Reasoning/paper_DeepPaperNote.md>)、[PFlowNet](<Train/Perceptual Flow Network for Visually Grounded Reasoning/paper_DeepPaperNote.md>) | 学 patch cue、视觉 token 或 `区域 + 证据描述` 的 perceptual flow | 专家/奖励模型偏差可能被写进轨迹 |
| 怎样在隐藏状态中重建视觉证据 | [Latent Visual Reasoning](<Train/Latent Visual Reasoning/paper_DeepPaperNote.md>)、[Reasoning in the Dark](<Train/Reasoning in the Dark Interleaved Vision-Text Reasoning in Latent Space/paper_DeepPaperNote.md>) | LVR 用 ROI 视觉标记监督隐藏状态重建，IVT-LR 将显式视觉—文本步骤压缩为联合潜在状态 | 中间状态不可读；都只重组初始视觉编码，且缺少隐藏状态级因果干预 |
| 怎样学习主动工具使用 | [DeepEyes](<Train/DeepEyes Incentivizing Thinking with Images via Reinforcement Learning/paper_DeepPaperNote.md>)、[Thyme](<Train/Thyme Think Beyond Images/paper_DeepPaperNote.md>)、[DeepEyesV2](<Train/DeepEyesV2 Toward Agentic Multimodal Model/paper_DeepPaperNote.md>) | 学习 crop、图像代码、数值计算、文本/图像搜索及多轮反馈整合 | 工具安全、跨工具信用分配和真实因果使用仍不充分 |
| 3D 中的开放世界 reasoning grounding | [REALM](<TrainingFree/REALM An MLLM-Agent Framework for Open World 3D Reasoning Segmentation and Editing on Gaussian Splatting/paper_DeepPaperNote.md>) | 把多视角 2D MLLM 推理回连到持久 3D identity | 重预处理、长时延、MLLM/SAM 共同偏差 |
| 机制审计 | [Position paper](<TrainingFree/Position Your VLM May Not Be Thinking with Interleaved Images/paper_DeepPaperNote.md>) | 直接删除交错图像、做遮挡与注意力分析，质疑涨点归因 | 它否定的是过强归因，不是否定所有视觉工具 |

## 2. Insight 1：长 CoT 的主要风险不是“想错”，而是“越想越脱离感知”

**论文证据。** SDR-MCoT 中，普通 CoT 在 Qwen2-VL-7B 和 InternVL3-8B 上都低于直接回答；选择性思考显著减少 token，而逐步视觉增强主要贡献准确率。VisRef 进一步表明，相同测试时预算下，持续补回视觉证据比增加纯文本轨迹更稳定。

**综合推断。** 多模态 test-time scaling 应拆成两个正交轴：

- `reasoning budget`：生成多少假设、步骤或候选答案；
- `evidence refresh budget`：在多少关键步骤重新获取、选择或回看视觉证据。

只扩展前者，容易让语言先验逐步压过视觉输入；只扩展后者，又可能重复观察而不形成推理。真正应优化的是二者的路由关系。

因此合理的控制器不是“是否开启 CoT”一个二值变量，而是：

```text
当前不确定性来自哪里？
├── 语义/逻辑不确定 → 增加 reasoning
├── 视觉证据不足 → 获取新观察
├── 旧证据被长上下文稀释 → 低成本回看
├── 工具结果互相冲突 → 验证或换工具
└── 证据充分且答案稳定 → 停止
```

## 3. Insight 2：应把“中间图像是否存在”升级为“中间观察是否提供可识别的新信息”

**直接证据。** Position paper 删除 DeepEyes、Pixel-Reasoner、Thyme 的交错图像后，多个基准只发生很小且方向不一致的变化；普通 SFT 也能获得类似涨点。其遮挡实验还显示，目标不可见时微调模型仍显著强于基座，说明部分结果可由 benchmark 对齐和语言先验解释。

这并不证明 crop、旋转、搜索或渲染无用，而是给出一条更严格的判据：

> **工具观察必须满足信息增量，而不能只满足形式增量。**

可以把工具分成三类：

| 工具类型 | 示例 | 是否可能产生新信息 | 审计重点 |
|---|---|---:|---|
| 重编码工具 | 重复插入原图、KV replay、token refocus | 通常不增加世界信息，只提高可用性 | 是否缓解注意力稀释；同预算纯文本对照 |
| 变换工具 | crop、rotate、contrast、OCR、局部超分 | 可能暴露原输入中低可读信息 | 删除/打乱变换结果后是否掉点 |
| 外部测量/交互工具 | 搜索、新视角渲染、深度、3D 重建、仿真、传感器动作 | 可以产生原上下文没有的观察 | 观察是否改变 belief；错误观察能否被发现 |

对 3D agent 而言，最有研究价值的是第三类：改变相机、查询深度、建立点云、执行碰撞或物理仿真，理论上都能给出单张图无法确定的新信息。因此 3D 工具轨迹反而比普通 2D 插图更适合做“真实证据使用”的因果验证。

## 4. Insight 3：真正的 reasoning trace 应表示 belief 更新，而不只是动作序列

现有轨迹常写成：

```text
thought → tool_call → observation → thought → answer
```

它能回放流程，却没有说明每次调用解决了什么不确定性。结合 PFlowNet、DeepEyesV2 与 S-Agent 类工作的启发，一个更有研究价值的轨迹单元应为：

$$
z_t=(b_t, u_t, n_t, a_t, o_t, e_t, v_t)
$$

- $b_t$：当前 belief / 场景状态；
- $u_t$：尚未解决的不确定性；
- $n_t$：下一步证据需求；
- $a_t$：工具与参数；
- $o_t$：环境返回的原始观察；
- $e_t$：从观察中抽取的任务级证据；
- $v_t$：证据充分性、一致性和成本验证。

随后执行：

$$
b_{t+1}=\mathrm{Update}(b_t,e_t,v_t).
$$

**综合推断。** 这个表示比“调用了哪个工具”更可迁移。换一个检测器、渲染器或搜索 API，`a_t` 会变，但 `n_t` 和 `e_t` 仍然可以保持稳定；长期技能应优先记忆后两者。

## 5. Insight 4：工具学习不是一个决策，而是六个可分离的策略

Thyme 的成功/失败案例、DeepEyesV2 的工具分布与 Skill-3D 类指标共同提示，工具使用至少包含六个阶段：

1. **Invoke**：是否需要工具；
2. **Route**：选择哪类工具；
3. **Parameterize**：目标、区域、视角、代码参数是否正确；
4. **Execute**：工具是否成功返回有效观察；
5. **Interpret**：观察被解释成了什么证据；
6. **Stop/Recover**：证据是否足够，失败后是否换策略。

只报告最终准确率会把六类错误压在一起。只报告执行成功率也不够：代码可以成功运行但与答案无关。后续实验应至少同时记录：

- 调用率与 no-tool accuracy；
- 工具执行成功率；
- 有效观察率；
- 观察被后续引用/计算的比例；
- 工具删除后的性能差；
- 重复或无信息调用率；
- 恢复成功率。

## 6. Insight 5：训练配方已经出现稳定共识——先建立协议，再优化策略

### 6.1 为什么不应直接从零做 RL

DeepEyesV2 的 pioneer experiment 显示：无工具奖励时，模型尝试几次错误代码后会退回文本 CoT；加入工具奖励后，又容易生成占位式或低质量调用。Skill-3D 与 Thyme 的训练稳定性也指向同一问题：**RL 擅长在已有行为邻域中做选择，不擅长凭稀疏奖励发明复杂工具协议。**

更稳的方案是：

1. `cold-start SFT`：学习结构化格式、基本工具调用、观察读取、no-tool 行为；
2. `agentic RL`：学习何时调用、怎样组合、何时停止与回退；
3. `offline skill update`：从新成功/失败轨迹更新技能库，再进入下一轮训练。

### 6.2 SFT 中必须保护的边界

Thyme 最值得迁移的细节不是 Python 本身，而是策略—环境边界：

- 工具观察是环境返回，不应让模型预测；
- SFT loss 应 mask 外部 observation；
- RL 的动作长度与优势不应把 observation token 算作策略动作；
- 数据必须包含足量 no-tool 样本；
- 自然语言规划可保留探索，代码/JSON/相机动作宜更确定。

这会直接影响工具模型是否学会“使用环境”，还是学会“模仿环境输出”。

LVR 补充了一个更底层的训练边界：潜在状态可以有明确视觉教师目标，但“重建视觉嵌入”不能自动等价为“答案因果依赖该状态”。其 MMVP 从 66.7 提升到 72.0 说明视觉语义重建有用；4/8/16 步收益不单调、学习式停止严重失败以及 `GRPO_latent` 的局部退化，则说明连续隐藏轨迹同样需要预算控制和反事实审计。对这类方法，审计对象应从可删除的工具观察扩展为可交换、置零或替换的潜在状态。

### 6.3 奖励应围绕结果与证据，而不是工具表演

DeepEyes 的条件工具奖励只有在答案正确时才给 tool bonus；Thyme 中直接代码奖励和主观过程奖励都弱于结果、一致性与格式组合；PFlowNet 则表明，区域证据应同时满足视觉支持和答案效用。

一个更稳的抽象是：

$$
R(\tau)=R_{ans}+R_{fmt}+\mathbf{1}[R_{ans}>0]
\left(\lambda_eR_{evidence}+\lambda_vR_{verify}-\lambda_cC_{tool}\right)-\lambda_rR_{redundant}.
$$

这里的关键不是具体权重，而是三条原则：

- 工具奖励由正确性门控，避免“为调用而调用”；
- 奖励证据被使用和验证，而非只奖励执行成功；
- 把工具成本与重复调用显式纳入目标。

## 7. Insight 6：PFlowNet 给出的最好启发，是把专家轨迹从唯一答案降级为“可行域”

PFlowNet 不要求策略逐框复制专家区域，而是在专家几何邻域内，让任务效用决定具体轨迹。这解决了一个普遍问题：专家定位可能可靠，却未必包含回答问题所需的全部上下文。

**迁移到工具 agent 的推断：**

- 教师轨迹不应被视为唯一正确 API 序列；
- 教师应提供安全边界、必要证据和禁止行为；
- 在可行域内允许模型探索更低成本或更稳的工具程序；
- 如果教师置信度低，约束半径应更宽；如果涉及安全/坐标系，约束应更紧。

这比纯行为克隆更有希望得到跨工具、跨场景的轨迹多样性。

## 8. Insight 7：视觉记忆要区分“证据内容、空间坐标和解码位置”

PRCR 的直接 KV 复用会严重崩溃，而位置重绑定后可以在基本保持性能的同时把视觉 replay FLOPs 降低多个数量级。它说明视觉记忆不是无位置的内容向量。

对通用 agent，可把记忆分成三层：

1. **raw observation memory**：原图/局部图/搜索结果/点云等不可变来源；
2. **spatial provenance**：相机位姿、区域坐标、尺度、时间戳、对象 identity；
3. **reasoning binding**：当前步骤怎样把旧证据绑定进新的问题和参考系。

这也给出了“复用旧证据”和“获取新证据”的明确边界：PRCR/VisRef 解决前者；crop、新视角、搜索、3D 工具解决后者。

## 9. 一套必须做的因果审计

Position paper 的核心价值可以转成固定评测协议：

| 审计 | 操作 | 如果工具真被使用，预期现象 |
|---|---|---|
| No-observation | 保留调用文本，删除环境观察 | 在确需工具的子集上明显下降 |
| Shuffled observation | 把同 batch 其他样本的观察换入 | 答案应下降或触发 verifier，而不是照常自信输出 |
| Counterfactual edit | 定向修改数字、对象、方位或搜索证据 | 答案应按编辑方向变化 |
| Irrelevant perturbation | 只改与问题无关的区域/工具字段 | 答案应稳定，避免伪敏感 |
| Tool-free matched compute | 用等 token 的纯文本 self-refine 替代工具 | 若工具提供新证据，应显著优于该对照 |
| Hidden-target | 遮挡或移除目标信息 | 模型不应只靠 benchmark 先验维持高分 |
| Trace swap | 保留最终观察，替换前序 thought/tool narrative | 检查收益来自观察还是轨迹语言模板 |

建议报告三个简单指标：

- `Tool Necessity Gap = Acc_full - Acc_no-observation`；
- `Counterfactual Faithfulness`：定向修改证据后，答案按预期改变的比例；
- `Irrelevant Robustness`：无关观察被扰动时答案保持正确的比例。

三者结合，才能区分“依赖证据”“能读懂证据”和“不过度依赖噪声”。

## 10. 最值得推进的研究方向

| 方向 | 源自的缺口 | 最小实验 | 新颖性 | 可行性 | 价值 | 建议 |
|---|---|---|---:|---:|---:|---|
| Evidence-causal tool trajectories | 工具轨迹缺少因果审计 | 在 DeepEyes/Thyme 类轨迹上加入删除、置换、反事实观察测试 | 5 | 4 | 5 | **优先做** |
| Adaptive reasoning/evidence router | 所有样本走同一长流程 | 预测 `direct / reason / revisit / new-tool` 四路路由 | 4 | 5 | 4 | 优先做 |
| Support-constrained trajectory RL | 行为克隆过度依赖单一教师路径 | 用专家给必要证据与安全边界，RL 在边界内找低成本轨迹 | 5 | 3 | 5 | 中期主线 |
| Provenance-aware multimodal memory | 长轨迹中证据坐标与身份丢失 | 记忆 `content + coordinates + source + time`，测试跨步回看 | 4 | 3 | 5 | 与 3D 结合 |
| Tool-use process benchmark | 现有 benchmark 只看答案 | 标注 invoke/route/parameter/use/stop 六阶段 | 4 | 4 | 4 | 可做资源论文 |

## 11. 对 3D Agent 的直接迁移

Reasoning 论文对 3D agent 的真正贡献，不是把 crop 换成 render 那么简单，而是提供一套训练与审计方法：

```text
selective thinking     → 是否启动昂贵 3D 工具
visual refocusing      → 在长规划中刷新多视角/对象证据
perceptual flow        → 显式记录“看哪里 + 证据是什么”
tool RL                → 学何时调用、组合和停止
cache rebinding        → 低成本、安全地复用旧视角证据
position-paper audit   → 证明轨迹真正依赖 3D 观察
```

最关键的迁移判断是：

> **3D reasoning trace 不应只保存 `camera action / tool call`，而应保存它解决的空间不确定性、采用的参考系、产生的任务级证据和反事实验证结果。**

这一判断将在 [3d_insight_with_reasoning](<3d_insight_with_reasoning.md>) 中展开成具体的 3D agent 架构与实验方案。

## 12. 结论边界

1. 这组论文多数仍以静态图像、短答案或有限工具箱为主；迁移到 3D、视频和具身交互需要重新验证。
2. attention、答案似然和“被文本引用”都不是严格因果证据，必须和干预实验一起看。
3. 训练型方法常依赖闭源教师、奖励模型或精心筛选数据，不能把涨点全归因于轨迹表示。
4. 免训练不等于低成本；VisRef、REALM、多视角投票和工具执行都可能把成本移到推理阶段。
5. 当前最可信的共同结论不是“交错图像一定有效”，而是：**多模态推理必须管理证据，工具策略必须被条件化、成本化并接受因果审计。**
