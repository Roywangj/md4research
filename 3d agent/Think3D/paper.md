# Think3D: Thinking with Space for Spatial Reasoning

**Authors:** Zaibin Zhang, Yuhan Wu, Lianjie Jia, Yifan Wang, Zhongbo Zhang, Yijiang Li, Binghao Ran, Fuxi Zhang, Zhuohan Sun, Zhenfei Yin, Lijun Wang, Huchuan Lu  
**Source:** `Zhang 等 - 2026 - Think3D Thinking with Space for Spatial Reasoning.pdf`  
**Detected source format:** selectable-text PDF (`pdf-text`)  
**Reader type:** full-paper Chinese-English Markdown reader with figure/table assets.  
**Version read:** arXiv `2601.13029v3`, visible PDF date `17 Mar 2026`.

## Page / Section Index

| Section | Pages | Notes |
|---|---:|---|
| Abstract | p.1 | bilingual body |
| 1 Introduction | pp.1-4 | problem framing, motivation, contributions |
| 2 Related Work | pp.4-5 | spatial reasoning, tool calling, 3D reconstruction |
| 3 Think3D for Spatial Reasoning | pp.5-9 | pipeline, 3D toolkit, agent loop, Think3D-RL |
| 4 Experiment | pp.9-12 | setup and main results |
| 5 Ablation Study | pp.12-15 | component, exploration, RL dynamics, efficiency, tool robustness |
| 6 Conclusion | p.15 | high-level conclusion |
| Appendix: Prompts and Implementation Details | pp.16-23 | prompts, tool rules, self-refine baseline |
| Appendix: Further Experiment Analysis | pp.23-26 | ego/global usage, tool iterations, training settings, more models |
| Appendix: Interaction Visualization | pp.26-32 | MindCube, BLINK, VSI-Bench qualitative cases |
| References | pp.33-38 | bibliography preserved in source map; not translated line by line |

## Terminology Ledger

| Canonical term | Chinese rendering | Decision |
|---|---|---|
| Think3D | Think3D | 方法名；保持英文。 |
| Think3D-RL | Think3D-RL | 强化学习变体；保持英文。 |
| think with 3D space | think with 3D space / 用 3D 空间思考 | 论文核心范式；首次解释后保持英文短语。 |
| VLM | 视觉语言模型（VLM） | 首次展开后保持 VLM。 |
| 3D Manipulation Toolkit | 3D 操作工具箱 | 包含重建、变换和新视角渲染。 |
| point cloud | 点云 | 指由多视角图像重建得到的显式 3D 表示。 |
| camera anchor | 相机锚点 | 用输入相机位姿作为旋转与视角操作参考。 |
| global mode | 全局视角模式 | 围绕场景中心旋转点云，观察整体布局。 |
| ego mode | 自我中心视角模式 | 以选定相机为第一人称锚点生成局部视角。 |
| observe → manipulate → reflect | 观察 → 操作 → 反思 | Think3D 的多轮工具交互循环。 |
| GRPO | Group Relative Policy Optimization（GRPO） | 强化学习优化方法。 |
| BLINK Multi-view | BLINK Multi-view | 多视角几何理解评测。 |
| MindCube | MindCube | 空间心理建模/相机运动评测子集。 |
| VSI-Bench-tiny | VSI-Bench-tiny | 视频空间智能小规模评测 split。 |
| Self-Refine | Self-Refine | 多轮自我批判和修正基线。 |

## Abstract

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> While contemporary Vision-Language Models excel at 2D visual understanding, they remain constrained by a passive, 2D-centric paradigm that limits genuine 3D spatial reasoning. Think3D equips VLM agents with interactive 3D chain-of-thought capabilities by integrating a 3D manipulation toolkit. Instead of only inspecting original images, the agent reconstructs a 3D point cloud, renders new views, and iteratively explores the space.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 当代视觉语言模型虽然已经擅长二维视觉理解，但仍被动地停留在以二维图像为中心的范式中，因此难以完成真正的三维空间推理。Think3D 通过引入三维操作工具箱，让 VLM 代理具备交互式的三维思维链能力。代理不再只看原始图像，而是重建三维点云、渲染新视角，并以多轮方式主动探索空间。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The paper reports that Think3D works as a zero-shot plug-in for closed-source models such as GPT-4.1 and Gemini 2.5 Pro, giving absolute gains of +7.8% on BLINK Multi-view and MindCube and +4.7% on VSI-Bench. For smaller open-weight models, the authors propose Think3D-RL so that Qwen3-VL-4B can learn exploration strategies from final task rewards.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 论文报告称，Think3D 可以作为闭源模型的零样本插件使用，例如用于 GPT-4.1 和 Gemini 2.5 Pro 时，在 BLINK Multi-view 与 MindCube 上带来 +7.8% 的绝对提升，在 VSI-Bench 上带来 +4.7% 的提升。对于较小的开源模型，作者提出 Think3D-RL，使 Qwen3-VL-4B 能够仅从最终任务奖励中学习空间探索策略。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The core claim is that tool-augmented active exploration helps multimodal agents reason more like humans: they do not merely classify a static image, but choose where to look next in a reconstructed 3D space.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 论文的核心主张是：工具增强的主动探索可以让多模态代理更接近人的空间推理方式。模型不只是对静态图像分类，而是在重建出的三维空间中决定下一步应该从哪里观察。

## 1 Introduction

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Understanding and interacting with the physical world requires spatial intelligence: reasoning about geometry, viewpoint, object relationships, route planning, and relative direction. Existing VLMs have improved greatly on general visual understanding, but their performance still drops on tasks that require genuine 3D reasoning.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 理解并交互物理世界需要空间智能，也就是对几何、视角、物体关系、路径规划和相对方向进行推理。现有 VLM 在通用视觉理解上进步很大，但遇到真正需要三维推理的任务时，表现仍会明显下降。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The authors describe two broad attempts to bridge this gap. One route internalizes spatial knowledge through large-scale spatial data, which is expensive and may hurt general reasoning. Another route lets models “think with images” by calling tools such as crop, zoom, or depth estimation. These tools provide useful but shallow spatial cues, and they do not let the agent manipulate a coherent 3D representation across views.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 作者概括了两条弥合差距的路线。第一条是通过大规模空间数据把空间知识内化到模型里，但这需要巨大计算量，也可能损害通用推理。第二条是让模型通过裁剪、缩放、深度估计等工具“用图像思考”。这些工具可以提供有用但偏浅层的空间线索，却不能让代理在多视角之间操作一个一致的三维表示。

### Fig. 1. 从 “think with image” 到 “think with 3D space”

![Fig. 1](3d%20agent/Think3D/assets/page_002_fig_fig_1.png)

**Caption:** Fig. 1: Comparison between prior “think with image” and Think3D’s “think with 3D space”. The former manipulates 2D images; Think3D operates in reconstructed 3D point cloud space.

**Caption[CN]:** 图 1：已有 “think with image” 与 Think3D 的 “think with 3D space” 对比。前者操作二维图像，Think3D 则在重建得到的三维点云空间中操作。

**Reading note:** 这张图是整篇论文的动机图。上半部分强调二维裁剪/选择视角的局限；下半部分强调通过三维重建、相机选择和全局视角拖动获得更直接的空间证据。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Think3D is built on recent 3D reconstruction systems that can recover camera poses and point clouds from videos or multi-view images. With this foundation, the model can choose cameras, rotate views, switch between global and local observations, and refine its spatial understanding through repeated interaction.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> Think3D 建立在近期三维重建系统之上，这些系统能够从视频或多视角图像中恢复相机位姿和点云。基于这一基础，模型可以选择相机、旋转视角、在全局和局部观察之间切换，并通过重复交互逐步修正空间理解。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> A key empirical observation is that strong frontier models can select more diverse and meaningful viewpoints, while weaker models often choose redundant or misleading camera poses. The paper therefore adds Think3D-RL, a reinforcement learning formulation that trains smaller models to discover useful exploration policies without operation-trajectory annotations.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 一个关键经验观察是：强前沿模型能够选择更多样且更有语义意义的视角，而较弱模型常常选择冗余甚至误导性的相机姿态。因此论文加入 Think3D-RL，用强化学习让小模型在没有操作轨迹标注的情况下学习有效探索策略。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The paper’s contributions are threefold: it reframes spatial reasoning as active 3D exploration; it designs a 3D interaction framework where a VLM manipulates point clouds through camera-based actions; and it formulates viewpoint/action selection as a reinforcement learning problem.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 论文贡献可以概括为三点：第一，把空间推理重新表述为主动三维探索；第二，设计了一个三维交互框架，使 VLM 能通过基于相机的动作操作点云；第三，把视角和动作选择建模为强化学习问题。

## 2 Related Work

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Work on VLM spatial reasoning has introduced spatial benchmarks, 3D reconstruction cues, depth prompts, spatial VQA data, explicit grounding, mental simulation, visual chain-of-thought, and reinforcement learning. Some systems extend these ideas to embodied agents, robotics, and navigation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 关于 VLM 空间推理的工作已经引入空间评测基准、三维重建线索、深度提示、空间问答数据、显式 grounding、心理模拟、视觉思维链和强化学习等方向。一些系统还把这些能力扩展到具身代理、机器人和导航场景。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Tool calling improves VLMs by letting them use external tools through prompts or code generation. Existing systems have been used for long video, high-resolution images, medical diagnosis, and general visual reasoning. Think3D is closest to the “think with images” line, but replaces 2D image manipulation with explicit 3D manipulation.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 工具调用通过提示词或代码生成让 VLM 使用外部工具，从而增强模型能力。已有系统覆盖长视频、高分辨率图像、医学诊断和通用视觉推理等任务。Think3D 与 “think with images” 路线最接近，但它把二维图像操作替换成显式三维操作。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The reconstruction backbone matters because Think3D needs camera poses and point clouds. The paper mentions DUSt3R, MASt3R, VGGT, CUT3R, MapAnything, and Pi3 as representative progress in feed-forward or multi-view 3D geometry. Pi3 is used as the main reconstruction tool, while VGGT is later used for robustness analysis.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 三维重建 backbone 很重要，因为 Think3D 需要相机位姿和点云。论文提到 DUSt3R、MASt3R、VGGT、CUT3R、MapAnything 和 Pi3 等前馈或多视角三维几何方法。Pi3 被用作主要重建工具，VGGT 则在后续稳健性分析中作为替代工具。

## 3 Think3D for Spatial Reasoning

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Think3D equips a VLM with a multi-turn loop: observe the current images and rendered views, manipulate the 3D scene through tool calls, then reflect on the newly rendered observations. The loop runs for at most $K$ iterations, with default $K=3$; the model can stop early when it considers the evidence sufficient.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Think3D 给 VLM 配备了一个多轮循环：先观察当前图像和已渲染视图，再通过工具调用操作三维场景，随后根据新渲染出的观察结果继续反思。该循环最多运行 $K$ 轮，默认 $K=3$；当模型认为证据足够时可以提前停止。

### Fig. 2. Think3D pipeline

![Fig. 2](3d%20agent/Think3D/assets/page_005_fig_fig_2.png)

**Caption:** Fig. 2: The Think3D pipeline. The VLM interacts with the 3D scene through iterative calls to the 3D Manipulation Toolkit, controls camera pose and rendering parameters, and appends each rendered image to memory for the next reasoning step.

**Caption[CN]:** 图 2：Think3D 流程。VLM 通过多轮调用 3D 操作工具箱与三维场景交互，控制相机姿态和渲染参数，并把每次渲染图像加入记忆，供下一轮推理使用。

**Reading note:** 这张图把方法压缩成一条闭环：多图像输入 → 三维重建 → 视角操作 → 新渲染图像 → 继续推理 → 最终答案或 RL 奖励。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The 3D Manipulation Toolkit has three functions: reconstruction, transformation, and novel-view rendering. Given multi-view images $\{I_t\}_{t=1}^{T}$, Pi3 estimates a point cloud and camera poses. Each camera is represented as:

$$
C_t = (\mathbf{K}_t, \mathbf{R}_t, \mathbf{t}_t),
$$

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 3D 操作工具箱包含三个功能：三维重建、三维变换和新视角渲染。给定多视角图像 $\{I_t\}_{t=1}^{T}$，Pi3 会估计点云和相机位姿。每个相机表示为上式，其中 $\mathbf{K}_t$ 是内参矩阵，$\mathbf{R}_t$ 是旋转矩阵，$\mathbf{t}_t$ 是世界坐标中的相机中心。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The fused colored point cloud is written as:

$$
\mathcal{X}=\{(\mathbf{x}_n,\mathbf{c}_n)\}_{n=1}^{N},
$$

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 融合后的彩色点云写作上式，其中 $\mathbf{x}_n$ 是三维位置，$\mathbf{c}_n$ 是 RGB 颜色。也就是说，模型不是直接操作像素，而是在一个显式三维点集合上生成新观察。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> At each step, the agent predicts a camera index, a pair of azimuth/elevation angles, and a binary mode: global or ego. In global mode, the point cloud is rotated around the scene centroid while the camera remains fixed. In ego mode, the point cloud remains fixed and a virtual camera is rotated around the selected anchor camera.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在每一步中，代理会预测一个相机索引、一对方位角/俯仰角，以及一个二值模式：全局视角或自我中心视角。全局模式围绕场景中心旋转点云，同时保持相机固定；自我中心模式保持点云不动，并围绕选定锚点相机旋转虚拟相机。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> The global transformation can be summarized as:

$$
\mathbf{x}_n' = s\,\Delta \mathbf{R}(\Delta \alpha,\Delta \beta)(\mathbf{x}_n-\mathbf{c})+\mathbf{c}.
$$

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 全局变换可以概括为上式。这里 $\mathbf{c}$ 是场景中心，$\Delta \mathbf{R}$ 由预测角度产生，$s$ 控制全局视角缩放，论文默认 $s=1$。这个公式表达的是：围绕场景中心旋转点云，而不是只在原图上做裁剪。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> For the ego-centric mode, the new camera is:

$$
C_{\mathrm{new}}=(\mathbf{K}_i,\Delta \mathbf{R}(\Delta \alpha,\Delta \beta)\mathbf{R}_i,\mathbf{t}_i).
$$

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 对自我中心模式，新相机由上式构造。它保留第 $i$ 个输入相机的内参和相机中心，只改变相机方向，因此更像“站在某个输入相机位置转头看”。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> The rendered view is produced by a lightweight point-based renderer:

$$
\hat{I}_k=\mathrm{Render}(\mathcal{X}^{(m)}, C^{(m)}, m).
$$

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> 新视角由轻量点渲染器生成。$\mathcal{X}^{(m)}$ 和 $C^{(m)}$ 由当前模式决定：全局模式使用旋转后的点云和原相机，自我中心模式使用受视锥约束的点云和虚拟相机。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> The VLM policy receives the question, original images, and history. It outputs text plus an optional tool call:

$$
\mathbf{o}_k=\pi_\theta(q,\{I_t\}_{t=1}^{T},\mathcal{H}_{k-1}).
$$

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> VLM 策略接收问题、原始图像和历史记录，然后输出文本响应以及可选工具调用。这里的历史不仅包含语言推理，还包含此前渲染出的图像和对应动作。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> The action at step $k$ is:

$$
\mathbf{a}_k=(i_k,m_k,\Delta \alpha_k,\Delta \beta_k),
$$

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> 第 $k$ 步动作由相机索引、视角模式、方位角和俯仰角组成。渲染后的图像 $\hat{I}_k$ 与动作 $\mathbf{a}_k$ 一起追加到历史 $\mathcal{H}_k$，形成“观察—操作—反思”的闭环。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> Think3D-RL represents a complete reasoning episode as a trajectory $\tau$ containing states, outputs, and final answer. To avoid repeatedly running reconstruction during RL, the authors precompute a point cloud for each training sample and only render selected views during training.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> Think3D-RL 把一次完整推理过程表示为轨迹 $\tau$，其中包含每轮状态、输出和最终答案。为了避免 RL 训练时反复运行三维重建，作者为每个训练样本预先生成点云，训练时只根据模型选择渲染对应视角。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> The trajectory-level reward is:

$$
R(\tau)=R_{\mathrm{ans}}(\hat{y})+R_{\mathrm{fmt}}(\hat{y}).
$$

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> 轨迹级奖励由答案正确性和格式奖励组成。值得注意的是，论文没有给中间工具动作提供标注轨迹监督，而是让最终答案奖励反向塑造前面的视角选择。

## 4 Experiment

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The RL implementation is based on SWIFT. The authors fine-tune the language model with GRPO, using 8 rollouts per step, one epoch, 8 H200 GPUs, batch size 8, gradient accumulation 4, cosine learning-rate schedule, 5% warmup, base learning rate $1\times 10^{-6}$, and maximum completion length 1024. The vision encoder is frozen. Training uses 977 MindCube samples with no test overlap.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> RL 实现基于 SWIFT。作者用 GRPO 微调语言模型，每步 8 个 rollout，训练 1 个 epoch，使用 8 张 H200 GPU，batch size 为 8，梯度累积为 4，采用余弦学习率、5% warmup、基础学习率 $1\times 10^{-6}$，最大生成长度为 1024。视觉编码器冻结。训练集包含 977 个 MindCube 样本，与测试集不重叠。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The evaluation uses three spatial reasoning benchmarks: BLINK Multi-view, MindCube, and VSI-Bench-tiny. BLINK focuses on relative camera motion across views. MindCube contains rotation, around, and among camera-motion types, with 40 questions per category. VSI-Bench-tiny evaluates route planning, relative direction, appearance order, and relative distance from seven sampled video frames.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 评测使用三个空间推理基准：BLINK Multi-view、MindCube 和 VSI-Bench-tiny。BLINK 关注多视角之间的相机相对运动。MindCube 包含 rotation、around 和 among 三类相机运动，每类 40 个问题。VSI-Bench-tiny 从视频中采样七帧，评测路径规划、相对方向、外观顺序和相对距离。

### Table 1. VSI-Bench-tiny results

![Table 1](3d%20agent/Think3D/assets/page_010_fig_table_1.png)

**Caption:** Table 1: Results on VSI-Bench-tiny. Think3D uses up to two exploration iterations for proprietary baselines and up to three for Qwen-VL-4B variants.

**Caption[CN]:** 表 1：VSI-Bench-tiny 结果。Think3D 对闭源模型最多使用两轮探索，对 Qwen-VL-4B 相关模型最多使用三轮探索。

**Reading note:** GPT-4.1 平均从 48.18 提升到 51.14，Gemini-2.5-Pro 从 45.16 提升到 51.61。普通 Qwen3-VL-4B 只从 38.28 到 39.08，但 Think3D-RL 后再用 Think3D 从 33.36 到 45.41。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Table 1 shows that Think3D improves closed-source models on VSI-Bench-tiny, especially Gemini-2.5-Pro. For Qwen3-VL-4B, direct Think3D brings only a small average gain and even hurts some categories, but the RL-trained variant benefits much more.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 表 1 显示，Think3D 能提升闭源模型在 VSI-Bench-tiny 上的表现，尤其是 Gemini-2.5-Pro。对 Qwen3-VL-4B，直接使用 Think3D 只带来很小平均增益，甚至在一些子类上下降；但经过 RL 训练的变体受益明显更大。

### Table 2. BLINK Multi-view and MindCube results

![Table 2](3d%20agent/Think3D/assets/page_011_fig_table_2.png)

**Caption:** Table 2: Results on BLINK Multi-view and the MindCube subset. Think3D uses up to three exploration iterations.

**Caption[CN]:** 表 2：BLINK Multi-view 和 MindCube 子集结果。Think3D 最多使用三轮探索。

**Reading note:** GPT-4.1 平均从 49.62 到 61.19，Gemini-2.5-Pro 从 59.34 到 63.34；Qwen3-VL-4B 的直接收益只有 +0.61，而 Think3D-RL 后达到 +9.32。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> On BLINK and MindCube, the gains are larger for frontier models. GPT-4.1 gains +27.09 on BLINK Multi-view and +11.57 on average. Gemini-2.5-Pro gains +8.02 on BLINK and +4.00 on average. The small model only benefits after RL.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 在 BLINK 和 MindCube 上，强模型收益更明显。GPT-4.1 在 BLINK Multi-view 上提升 +27.09，平均提升 +11.57。Gemini-2.5-Pro 在 BLINK 上提升 +8.02，平均提升 +4.00。小模型只有在经过 RL 后才明显受益。

### Fig. 3. Spatial exploration behavior

![Fig. 3](3d%20agent/Think3D/assets/page_011_fig_fig_3.png)

**Caption:** Fig. 3: Spatial exploration behavior of Think3D. The agent selects viewpoints and switches between global and ego-centric views; after RL training, it explores angles more systematically.

**Caption[CN]:** 图 3：Think3D 的空间探索行为。代理会选择视角，并在全局视角与自我中心视角之间切换；经过 RL 训练后，视角探索更有系统性。

**Reading note:** 这张图帮助理解为什么表 2 中小模型需要 Think3D-RL：不是工具本身不工作，而是弱模型不会自然选择有信息量的视角。

## 5 Ablation Study

### Table 3. Component ablation

![Table 3](3d%20agent/Think3D/assets/page_012_fig_table_3.png)

**Caption:** Table 3: Ablation on different 3D reasoning components: reconstructed geometry, camera anchor, camera choice, and ego-view.

**Caption[CN]:** 表 3：不同三维推理组件的消融，包括三维重建、相机锚点、相机选择和自我中心视角。

**Reading note:** 裸三维重建并不足够；相机锚点、相机选择和 ego-view 共同把点云变成可被代理操作的视角接口。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The ablation starts from GPT-4.1 without the 3D tool. Directly using reconstructed 3D space without camera-pose anchoring can even hurt performance. Adding camera anchoring, camera choice, and ego-view progressively improves BLINK and MindCube results.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 消融从不使用三维工具的 GPT-4.1 开始。直接使用三维重建空间但没有相机位姿锚点，甚至可能损害性能。逐步加入相机锚点、相机选择和自我中心视角后，BLINK 和 MindCube 表现持续改善。

### Fig. 4. Viewpoint selection patterns

![Fig. 4](3d%20agent/Think3D/assets/page_013_fig_fig_4.png)

**Caption:** Fig. 4: Spatial exploration patterns in viewpoint selection. Strong models concentrate on informative angles; after RL, Qwen3-VL-4B shifts toward a similar distribution.

**Caption[CN]:** 图 4：视角选择中的空间探索模式。强模型集中选择更有信息量的角度；经过 RL 后，Qwen3-VL-4B 的分布也向类似模式移动。

**Reading note:** 任务有不同视角偏好：路径规划偏好 top-down，方向和物体朝向任务更需要旋转视角。

### Fig. 5. RL dynamics

![Fig. 5](3d%20agent/Think3D/assets/page_013_fig_fig_5.png)

**Caption:** Fig. 5: Reinforcement Learning Dynamics. The model learns when extra 3D tool calls are worthwhile, shifting from short but less accurate trajectories to more informative explorations.

**Caption[CN]:** 图 5：强化学习动态。模型逐渐学会什么时候额外三维工具调用是值得的，从更短但不准确的轨迹转向更有信息量的探索。

**Reading note:** 训练早期模型会减少工具轮数以追求奖励，但准确率下降；随后它学会增加有用工具调用，准确率逐步提高。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The exploration analysis shows that different tasks prefer different view distributions. Route planning and appearance order benefit from top-down views that capture global layout, while MindCube and orientation tasks need more rotational views.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 探索分析表明，不同任务偏好不同视角分布。路径规划和外观顺序任务更依赖捕获全局布局的 top-down 视角，而 MindCube 和朝向任务更需要旋转视角。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> The RL analysis suggests that the small model is not merely learning to call the tool more often. It learns when additional 3D views improve downstream answer accuracy, and the learned viewpoint distribution becomes closer to that of GPT-4.1 and Gemini-2.5-Pro.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> RL 分析说明，小模型并不是简单学会多调工具，而是学会判断什么时候额外三维视角能提升最终答案准确率。学习后的视角分布更接近 GPT-4.1 和 Gemini-2.5-Pro 等强模型。

### Fig. 6. Number of exploration turns

![Fig. 6](3d%20agent/Think3D/assets/page_014_fig_fig_6.png)

**Caption:** Fig. 6: The ablation of turns.

**Caption[CN]:** 图 6：探索轮数消融。

**Reading note:** 未经过 RL 的模型增加交互轮数并不稳定提升；Think3D-RL 后的小模型开始表现出“更多有用观察带来更好结果”的趋势。

### Fig. 7. Efficiency against Self-Refine

![Fig. 7](3d%20agent/Think3D/assets/page_014_fig_fig_7.png)

**Caption:** Fig. 7: Efficiency ablation on BLINK, comparing accuracy and token usage.

**Caption[CN]:** 图 7：BLINK 上的效率消融，对比准确率和 token 使用。

**Reading note:** Self-Refine 的多轮自我修正消耗类似甚至更高，但收益远小于 Think3D，说明关键不是“多想几轮”，而是有新三维观察。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> The Self-Refine comparison tests whether Think3D’s gain simply comes from extra rounds of reasoning. The answer is no: multi-round critique without 3D tools brings only marginal improvement, while Think3D’s explicit 3D interaction gives a larger accuracy gain.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 与 Self-Refine 的对比检验了 Think3D 的收益是否只是来自更多推理轮数。答案是否定的：没有三维工具的多轮自我批判只带来有限提升，而 Think3D 的显式三维交互带来更大准确率收益。

### Table 4. Robustness to reconstruction tool

![Table 4](3d%20agent/Think3D/assets/page_015_fig_table_4.png)

**Caption:** Table 4: Comparison of 3D reconstruction tools on spatial benchmarks.

**Caption[CN]:** 表 4：不同三维重建工具在空间基准上的对比。

**Reading note:** VGGT 也能超过无工具基线，但 Pi3 更强；这说明 Think3D 不完全绑定某个重建器，但底层几何质量仍会影响结果。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> Replacing Pi3 with VGGT while keeping the rest of the pipeline unchanged still improves over the no-tool baseline. This supports the claim that Think3D is largely reconstruction-tool agnostic, although stronger reconstruction quality remains beneficial.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 在保持其余流程不变的情况下，把 Pi3 替换为 VGGT 仍然优于无工具基线。这支持了 Think3D 在一定程度上与具体重建工具解耦的说法，不过更强的重建质量仍然有益。

## 6 Conclusion

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The paper concludes that VLM agents should reason in 3D through active interaction rather than rely only on passive 2D perception. Think3D iteratively explores reconstructed point clouds and improves spatial understanding on BLINK, MindCube, and VSI-Bench-tiny. Its RL-enhanced version helps smaller VLMs approach the exploration behavior of stronger proprietary models.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 论文结论是：VLM 代理应通过主动交互在三维空间中推理，而不应只依赖被动二维感知。Think3D 通过迭代探索重建点云，在 BLINK、MindCube 和 VSI-Bench-tiny 上提升空间理解。它的 RL 增强版本帮助较小 VLM 接近强闭源模型的探索行为。

## Appendix: Prompts and Implementation Details

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The training-free workflow prompt is modular: a system prompt, a tool prompt, and a continual prompt. The system prompt defines the model role, tool-call format, multi-step workflow, and final answer format. It also warns the model not to request the original $(0^\circ,0^\circ)$ view again because that view is already given by the input images.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 免训练工作流的提示词是模块化的：系统提示、工具提示和续写提示。系统提示定义模型角色、工具调用格式、多步工作流和最终答案格式。它还明确提醒模型不要再次请求原始 $(0^\circ,0^\circ)$ 视角，因为输入图像已经对应这个视角。

### Fig. 8. System prompt

![Fig. 8](3d%20agent/Think3D/assets/page_017_fig_fig_8.png)

**Caption:** Fig. 8: The system prompt, including tool invocation rules and the multi-step workflow.

**Caption[CN]:** 图 8：系统提示词，包含工具调用规则和多轮三维视角探索工作流。

**Reading note:** 这里最关键的约束是“不要重复默认视角”，并建议 left/right/top/back/diagonal 等新视角。

### Fig. 9. Pi3 tool prompt

![Fig. 9](3d%20agent/Think3D/assets/page_018_fig_fig_9.png)

**Caption:** Fig. 9: The Pi3 Tool Prompt, specifying tool capabilities, angle parameters, camera reference, and global/ego view mode.

**Caption[CN]:** 图 9：Pi3 工具提示词，定义工具能力、角度参数、相机参考和全局/自我中心视角模式。

**Reading note:** 这张图给出了工具 API 的语义边界：方位角、俯仰角、参考相机和是否使用第一人称视角。

### Algorithm 1. Self-Refine baseline

![Algorithm 1](3d%20agent/Think3D/assets/page_018_fig_algorithm_1.png)

**Caption:** Algorithm 1: Self-Refine Inference.

**Caption[CN]:** 算法 1：Self-Refine 推理。

**Reading note:** Self-Refine 只做回答、批判、修正循环，不引入新的三维观测，因此是用来排除“只是多轮推理带来收益”的对照。

### Fig. 10. Continual prompt

![Fig. 10](3d%20agent/Think3D/assets/page_019_fig_fig_10.png)

**Caption:** Fig. 10: Multi-step prompt for iterative 3D viewpoint exploration.

**Caption[CN]:** 图 10：用于迭代三维视角探索的多步提示词。

**Reading note:** 续写提示负责把上一轮工具结果、已有角度和剩余轮数重新放入上下文，迫使模型判断是否还需要新的视角。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The RL prompt is further restricted to a smaller set of candidate viewing angles. The authors also split continual training prompts into initial, intermediate, and final stages so that small models receive stage-appropriate instructions during multi-round optimization.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> RL 提示进一步把可选视角限制到更小的候选集合。作者还把训练中的续写提示拆成初始、中间和最终阶段，使小模型在多轮优化中接收更符合当前阶段的指令。

### Fig. 11. RL system prompt

![Fig. 11](3d%20agent/Think3D/assets/page_020_fig_fig_11.png)

**Caption:** Fig. 11: The RL system prompt, defining the constrained 3-view analysis workflow.

**Caption[CN]:** 图 11：RL 系统提示词，定义受约束的三维分析工作流。

**Reading note:** 相比免训练提示，RL 提示把可选角度限定得更强，目的是降低训练搜索空间。

### Fig. 12. RL continuation prompt

![Fig. 12](3d%20agent/Think3D/assets/page_021_fig_fig_12.png)

**Caption:** Fig. 12: The RL continuation prompt used during non-final turns.

**Caption[CN]:** 图 12：非最终轮使用的 RL 续写提示词。

**Reading note:** 非最终轮仍可调用工具，但必须避免重复已经使用过的视角。

### Fig. 13. Final-turn prompt

![Fig. 13](3d%20agent/Think3D/assets/page_022_fig_fig_13.png)

**Caption:** Fig. 13: The final-turn instruction requiring no further tool call and direct answer generation.

**Caption[CN]:** 图 13：最终轮提示，要求不再调用工具，直接基于已有三维视图和原图推理并回答。

**Reading note:** 最终轮把探索阶段和回答阶段分开，避免模型在没有剩余工具预算时继续发起工具调用。

### Fig. 14. No-tool prompt

![Fig. 14](3d%20agent/Think3D/assets/page_022_fig_fig_14.png)

**Caption:** Fig. 14: The prompt without tools.

**Caption[CN]:** 图 14：不使用工具时的基线提示词。

**Reading note:** 这个提示对应纯视觉问答或 CoT 基线。

### Fig. 15. Self-Refine prompts

![Fig. 15](3d%20agent/Think3D/assets/page_023_fig_fig_15.png)

**Caption:** Fig. 15: The critique prompt and refinement prompt used in the Self-Refine experiment.

**Caption[CN]:** 图 15：Self-Refine 实验中使用的批判提示和修正提示。

**Reading note:** 该基线让模型批判自己的答案，但没有获得新的几何证据。

## Appendix: Further Experiment Analysis

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The appendix analyzes ego-view versus global-view usage. Fine-grained tasks such as MindCube and object direction rely more on ego-view, while route planning mostly uses global view. This supports the design choice of exposing both modes.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 附录分析了自我中心视角与全局视角的使用比例。MindCube 和物体方向等细粒度任务更依赖自我中心视角，而路径规划主要使用全局视角。这支持了同时开放两种视角模式的设计。

### Fig. 16. Ego-view usage ratio

![Fig. 16](3d%20agent/Think3D/assets/page_024_fig_fig_16.png)

**Caption:** Fig. 16: Ego-view usage ratio across different tasks.

**Caption[CN]:** 图 16：不同任务中的 ego-view 使用比例。

**Reading note:** 任务类型决定视角模式：全局布局任务不一定需要第一人称局部视角。

### Fig. 17. Tool-call iteration ratio

![Fig. 17](3d%20agent/Think3D/assets/page_024_fig_fig_17.png)

**Caption:** Fig. 17: Tool calling iteration ratio across different tasks.

**Caption[CN]:** 图 17：不同任务中的工具调用轮数比例。

**Reading note:** GPT-4.1 在路径规划上较少调用工具，而在其他任务上常用多轮调用获取更丰富空间信息。

### Table 5. RL training and evaluation settings

> [!figure] Table 5. Think3D-RL training and evaluation settings
> 建议位置：Appendix: Further Experiment Analysis
> 放置原因：这张表列出训练温度、KL penalty、batch、学习率、DeepSpeed 等复现实验参数。
> 当前状态：自动抽取未得到稳定独立表格裁剪；原文内容已在本节概述，详细字段保存在源 PDF 第 25 页。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The appendix reports training and evaluation settings and states that all main results and ablations are averaged over three runs. It also compares random angle sampling, heuristic angles, random exploration with the RL-trained backbone, and the learned RL policy.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 附录报告了训练和评估参数，并说明所有主结果和消融都运行三次后取平均。它还比较了随机角度采样、启发式角度、使用 RL backbone 但随机探索，以及学习得到的 RL 策略。

### Table 6. Exploration strategy comparison

![Table 6](3d%20agent/Think3D/assets/page_026_fig_table_6.png)

**Caption:** Table 6: Effect of exploration strategies.

**Caption[CN]:** 表 6：探索策略效果。

**Reading note:** Random、Heuristic、RLrandom 都明显低于学习得到的 RL 策略，说明收益主要来自空间策略学习。

### Table 7. More model results

![Table 7](3d%20agent/Think3D/assets/page_026_fig_table_7.png)

**Caption:** Table 7: More results on BLINK Multi-view and the MindCube subset.

**Caption[CN]:** 表 7：更多模型在 BLINK Multi-view 和 MindCube 子集上的结果。

**Reading note:** 这些结果提供了更宽的 VLM 对比，也显示 GPT-4.1-mini 加上 Think3D 后平均从 47.20 到 48.72。

## Appendix: Interaction Visualization

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The qualitative cases show how the agent uses top-down or rotated views to resolve questions that are ambiguous in the original images. The examples include MindCube rotation questions, BLINK camera-motion questions, and VSI-Bench object-distance or relative-direction questions.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 定性案例展示了代理如何使用俯视或旋转视角来解决原始图像中不明确的问题。例子包括 MindCube 旋转问题、BLINK 相机运动问题，以及 VSI-Bench 中的物体距离和相对方向问题。

### Fig. 18. MindCube example

![Fig. 18](3d%20agent/Think3D/assets/page_027_fig_fig_18.png)

**Caption:** Fig. 18: MindCube example.

**Caption[CN]:** 图 18：MindCube 示例。

**Reading note:** 该案例通过 top-down 视角确认转身后的左右关系。

### Fig. 19. MindCube example

![Fig. 19](3d%20agent/Think3D/assets/page_028_fig_fig_19.png)

**Caption:** Fig. 19: MindCube example.

**Caption[CN]:** 图 19：MindCube 示例。

**Reading note:** 该案例通过三维重建确认背后对象是 window。

### Fig. 20. BLINK example

![Fig. 20](3d%20agent/Think3D/assets/page_029_fig_fig_20.png)

**Caption:** Fig. 20: BLINK example.

**Caption[CN]:** 图 20：BLINK 示例。

**Reading note:** 该案例结合二维图像变化和三维相机位置判断相机移动方向。

### Fig. 21. BLINK example

![Fig. 21](3d%20agent/Think3D/assets/page_030_fig_fig_21.png)

**Caption:** Fig. 21: BLINK example.

**Caption[CN]:** 图 21：BLINK 示例。

**Reading note:** 该案例再次展示 top-down 视角如何消除相机左右运动歧义。

### Fig. 22. VSI-Bench example

![Fig. 22](3d%20agent/Think3D/assets/page_031_fig_fig_22.png)

**Caption:** Fig. 22: VSI-Bench example.

**Caption[CN]:** 图 22：VSI-Bench 示例。

**Reading note:** 该案例用 top-down 点云判断 pillow 与 plant、chair、heater、ceiling light 的距离关系。

### Fig. 23. VSI-Bench example

![Fig. 23](3d%20agent/Think3D/assets/page_032_fig_fig_23.png)

**Caption:** Fig. 23: VSI-Bench example.

**Caption[CN]:** 图 23：VSI-Bench 示例。

**Reading note:** 该案例用多角度视图判断站在窗边面向时钟时，trash bin 位于 front-right。

## References

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The reference list spans spatial reasoning benchmarks, tool-augmented VLM agents, visual reinforcement learning, 3D reconstruction backbones, robotics systems, and related 3D spatial reasoning agents. The bibliography is preserved in the source PDF and indexed in `source_map.json`; it is not translated line by line here.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 参考文献覆盖空间推理基准、工具增强 VLM 代理、视觉强化学习、三维重建 backbone、机器人系统以及相关 3D 空间推理代理。完整参考文献保留在源 PDF 中，并在 `source_map.json` 中建立索引；此处不逐条翻译。

## 阅读提示

1. 读方法时，不要把 Think3D 简化成“用了 Pi3”。更准确的理解是：它把三维重建输出封装成可被语言代理调用的离散视角操作接口。
2. 读结果时，要区分两类收益：强模型的 zero-shot 工具增强收益，以及小模型通过 Think3D-RL 学会视角策略后的收益。
3. 读消融时，Table 3、Fig. 4、Fig. 5 和 Table 6 是机制证据链：相机锚点、视角分布、工具轮数和学习策略共同解释主结果。
4. 读附录时，Prompt 不是小细节。它定义了模型能否稳定调用工具、避免重复默认视角、在最终轮停止工具调用。
