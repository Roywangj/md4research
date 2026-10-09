# GS-Agent: Creating 4D Physical Worlds With Generative Simulation
# GS-Agent：利用生成式仿真创建四维物理世界

> **Source / 来源:** Hongxin Zhang, Chunru Lin, Junyan Li, Zhou Xian, Tsun-Hsuan Wang, and Chuang Gan. *GS-Agent: Creating 4D Physical Worlds With Generative Simulation*. arXiv:2607.21522v1 [cs.RO], 23 Jul 2026, supplied 25-page preprint. Affiliations: University of Massachusetts Amherst; Genesis AI.
>
> **Status / 状态:** Complete bilingual reader of the supplied PDF. Exact bibliographic references and exact agent prompts are appended from the source extraction. Composite-page assets are under `assets/`.

## Index / 索引

PDF pp.1–2 title, Figure 1, Abstract, Introduction / 标题、图1、摘要、引言；pp.3–5 Related Work and framework / 相关工作与框架；pp.6–9 Experiments, Tables 1–4, Figures 3–6 / 实验、表1–4、图3–6；pp.10–14 Conclusion and References / 结论与参考文献；pp.15–19 Appendices A–C / 附录 A–C；pp.20–25 Listings 1–3 / 列表1–3。

## Terminology / 术语表

| English | Chinese |
|---|---|
| generative simulation | 生成式仿真 |
| Manager/Entity/Render Agent | Manager/Entity/Render Agent（管理/实体/渲染代理） |
| Physical Invariance Score (PIS) | 物理不变性得分 |
| Material Point Method (MPM); Smoothed Particle Hydrodynamics (SPH) | 材料点法；光滑粒子流体动力学 |
| State-PIS; Video-PIS | 状态 PIS；视频 PIS |

### Figure 1. Generated 4D physical worlds / 图1. 生成的四维物理世界

![Figure 1](assets/page_001_fig_figure_1.jpg)

**Caption:** Figure 1: GS-Agent creates 4D worlds from natural language through generative simulations, producing physically plausible interactions among liquids, deformable objects, and rigid bodies, together with cinematic camera and lighting controls. GS-Agent generates more than pixels; data modalities including fine-grained dynamics, depth and surface normals enable richer applications.

**Caption[CN]:** 图1：GS-Agent 通过生成式仿真从自然语言创建四维世界，生成液体、可变形物体和刚体之间物理合理的交互，并提供电影级相机和照明控制。GS-Agent 生成的不只是像素；包括细粒度动力学、深度和表面法线在内的数据模态支持更丰富的应用。

**Prompts shown in Figure 1 / 图1所示提示词:**

- “A close-up of warm, glossy melted chocolate slowly drizzling over a cake…” / “温暖、光泽明亮的融化巧克力缓慢淋在蛋糕上的特写……”
- “A tracking shot of a basketball falling from the sky onto the desert and rolling over the sand after landing…” / “跟踪镜头拍摄篮球从天空落到沙漠，并在落地后沿沙地滚动……”
- “A fixed-camera shot captures a vivid red strawberry striking a small transparent water droplet in mid-air.” / “固定相机镜头捕捉鲜红草莓撞击空中的小型透明水滴。”
- “A piece of soft dough being evenly flattened on a workbench, captured by a fixed camera on the side…” / “固定在侧面的相机拍摄一块柔软面团在工作台上被均匀压平……”

## Abstract / 摘要

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Creating dynamic and physically realistic 4D worlds from natural language descriptions is both fascinating and challenging. Traditional computer graphics methods rely on manual creation, requiring extensive human effort to fine-tune materials, motions, and visual fidelity. Recent advances in generative foundation models have sparked interest in learning to generate such 4D worlds from large-scale data; however, existing methods still struggle to ensure physical plausibility and controllability. In this work, we leverage foundation models to construct an agentic system that emulates how humans create 4D worlds while automating the entire process. We present GS-Agent, an end-to-end multi-agent framework that integrates physics engines in the loop to generate realistic, dynamic, and controllable 4D physical worlds from natural language.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 从自然语言描述创建动态且物理逼真的四维世界既令人着迷又充满挑战。传统图形学依赖人工制作，需要大量人力微调材料、运动和视觉保真度。生成式基础模型的进展引发了从大规模数据学习生成此类世界的兴趣，但现有方法仍难保证物理合理性和可控性。本文利用基础模型构建模拟人类创建四维世界、同时自动化全过程的代理系统。我们提出 GS-Agent，这是一种将物理引擎置于闭环、从自然语言生成逼真、动态且可控四维物理世界的端到端多代理框架。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Inspired by human world-building, GS-Agent decomposes the task into entity management—3D asset curation, material tuning, placement, and motion control—and rendering configuration, including camera and lighting manipulation. Specialized agents interact with the physics engine via code, seek multimodal feedback, and iteratively construct worlds aligned with descriptions. Experiments show diverse, physically plausible interactions among liquids, deformable objects, and rigid bodies with cinematic camera and lighting control. GS-Agent is a foundation for a new paradigm in 4D generation, creative content, and physical AI. See project page¹ for videos.
>
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 受人类建造世界启发，GS-Agent 将任务分为实体管理（三维资产整理、材料调节、放置、运动控制）和渲染配置（相机、照明操控）。专门代理通过代码与物理引擎交互，获取多模态反馈，迭代构建符合描述的世界。实验显示液体、可变形物体和刚体间有多样且物理合理的交互，并具电影级相机和照明控制。GS-Agent 为四维生成、创意内容和物理 AI 的新范式提供基础。视频见项目主页¹。

¹ https://umass-embodied-agi.github.io/gs-agent/

## 1 Introduction / 1 引言

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Dynamic, physically plausible 4D worlds have applications in embodied AI, autonomous driving, gaming, and film. Realistic environments enable safer, richer training and evaluation and narrow the sim-to-real gap [78]. Natural-language construction lowers the barrier to storytelling and new creative formats. Traditional approaches nevertheless require extensive human work: curating assets, tuning materials, constructing scenes, orchestrating motions, lighting, and camera trajectories.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 动态且物理合理的四维世界可用于具身 AI、自动驾驶、游戏和电影。逼真环境支持更安全丰富的训练评估，并缩小 sim-to-real 差距[78]。自然语言构建降低叙事和新创意形式的门槛。但传统方法仍需大量人工整理资产、调节材料、构建场景、编排运动、设置照明和设计相机轨迹。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Foundation models improve language [47], image [36, 22], video [5, 68, 48, 57], and 3D/4D creation [71, 4], yet struggle with physical plausibility [43, 29] and controllability [20]. Data-only learning is insufficient for consistent grounded scenes. LLM reasoning [18] can instead build agents that plan, critique, and refine; prior examples solve GitHub issues [67] or craft Blender scenes [25].
>
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 基础模型改善了语言[47]、图像[36, 22]、视频[5, 68, 48, 57]及三维/四维创建[71, 4]，却仍难保证物理合理性[43, 29]和可控性[20]。仅从数据学习不足以生成一致且有物理依据的场景。LLM 推理[18]可构建规划、批评和改进生成的代理；已有工作解决 GitHub issue[67]或制作 Blender 场景[25]。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> GS-Agent is an end-to-end physics-in-the-loop multi-agent framework. Entity management covers asset retrieval, materials, placement, and motion; rendering covers camera and lighting. Agents use code and multimodal feedback to refine simulations.
>
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> GS-Agent 是端到端物理闭环多代理框架。实体管理包括资产检索、材料、放置和运动，渲染包括相机和照明。代理通过代码和多模态反馈改进仿真。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Against Sora2 [48], Wan2.2 [57], SWE-Agent [67], and a visual-feedback variant, GS-Agent delivers higher physical plausibility, instruction fidelity, and controllability and autonomously addresses failures. Contributions:
>
> - automated agentic world-building with powerful physics engines;
> - an end-to-end code-interacting, feedback-seeking, collaborative framework;
> - more plausible, controllable, instruction-aligned worlds than text-to-video and agentic baselines.
>
> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 与 Sora2[48]、Wan2.2[57]、SWE-Agent[67]及视觉反馈变体比较，GS-Agent 具有更高物理合理性、指令保真度和可控性，并能自主处理失败。贡献为：
>
> - 用强大物理引擎和自动代理实现世界构建；
> - 提出端到端代码交互、反馈获取和协作框架；
> - 生成比文生视频和代理基线更合理、更可控、更符合指令的世界。

## 2 Related Work / 2 相关工作

### 2.1 3D and 4D Generation / 2.1 三维与四维生成

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Natural-language 3D scene creation is longstanding [10]. Early rule-based mapping [9, 42] gave way to massive-data methods [71, 70, 14, 60, 40], diffusion [61], and Gaussian Splatting [65]. Physics solvers [12, 4, 66, 76, 17, 58] add plausible motion; GPT4Motion [41] writes Blender motion scripts and Wonderplay [32] generates action-conditioned scenes. We automate 4D creation end to end and avoid unreliable visual-model generalization.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 自然语言三维场景创建是长期挑战[10]。早期规则映射[9, 42]发展为海量数据方法[71, 70, 14, 60, 40]、扩散模型[61]和 Gaussian Splatting[65]。物理求解器[12, 4, 66, 76, 17, 58]加入合理运动；GPT4Motion[41]编写 Blender 运动脚本，Wonderplay[32]生成动作条件场景。我们端到端自动化四维创建，避免视觉模型不可靠泛化。

### 2.2 Text-to-Video Generation / 2.2 文生视频生成

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Video models use diffusion [54, 22, 5, 21, 13] or autoregression [72, 30]. Diffusion Transformers [50, 48, 68] show scaling potential and physics priors improve realism [73, 41, 38], but plausibility [29], controllability [20, 77], and consistency [8] remain difficult. Our engine provides plausible interactions.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 视频模型采用扩散[54, 22, 5, 21, 13]或自回归[72, 30]。Diffusion Transformer[50, 48, 68]显示规模扩展潜力，物理先验改善真实感[73, 41, 38]，但合理性[29]、可控性[20, 77]和一致性[8]仍困难。我们的引擎提供合理交互。

### 2.3 Foundation Model Agents / 2.3 基础模型代理

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Foundation-model progress [47, 18] produced text agents [19, 53], GUI multimodal agents [23, 1], physical-world robots [2, 26, 16], and general agents [51, 24]. Multi-agent systems improve embodied AI [74], reasoning [15], and code generation [39]. SWE-Agent [67] solves GitHub issues and Blender agents [25, 56, 69, 35] make static scenes. We introduce the first natural-language 4D-world agent with unified physics in the loop.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 基础模型进步[47, 18]产生文本代理[19, 53]、GUI 多模态代理[23, 1]、物理世界机器人[2, 26, 16]和通用代理[51, 24]。多代理系统改善具身 AI[74]、推理[15]和代码生成[39]。SWE-Agent[67]解决 GitHub issue，Blender 代理[25, 56, 69, 35]制作静态场景。我们提出首个在统一物理闭环中从自然语言构建四维世界的代理。

## 3 GS-Agent framework / 3 GS-Agent 框架

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Four-dimensional world creation requires entity modeling, materials, spatial arrangement, motion, lighting, and camera planning. Like a director, GS-Agent uses Manager, Entity, and Render Agents. Manager communicates, plans, delegates, verifies, configures simulation, and controls time; Entity creates entities, morphology, materials, and motion; Render controls camera, lighting, and feedback. They communicate with `SendMessage`, generate executable code, request boundary/runtime/image/video feedback, and iterate until goals are met. Appendix B has prompts and interfaces.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 四维世界创建需要实体建模、材料、空间布局、运动、照明和相机规划。GS-Agent 像导演一样使用 Manager、Entity 和 Render Agent。Manager 负责沟通、规划、委派、验证、仿真配置和时间；Entity 创建实体、形态、材料和运动；Render 控制相机、照明和反馈。三者用 `SendMessage` 通信，生成可执行代码，请求边界/运行时/图像/视频反馈，迭代至目标满足。附录 B 给出提示词和接口。

![Figure 2](assets/page_004_fig_figure_2.jpg)

**Caption:** Figure 2: Overview of GS-Agent. Manager interprets language, decomposes tasks, configures simulation, advances scenes, and delegates; Entity curates assets, places entities, tunes materials, and controls motion; Render manipulates lighting/camera, trajectories, and recording. Structured tools yield executable simulation code and a rendered video.

**Caption[CN]:** 图2：GS-Agent 总览。Manager 解读语言、分解任务、配置仿真、推进场景并委派；Entity 整理资产、放置实体、调材料和控制运动；Render 操控照明/相机、轨迹和录制。结构化工具产生可执行仿真代码和渲染视频。

### 3.1 Physics Engine / 3.1 物理引擎

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> A physics engine provides a unified framework. **Entity** is $E=(Morph, Material, Surface)$: geometry, rigid/deformable/liquid behavior, appearance, velocities, forces, trajectories, and constraints. **Solver** computes dynamics using rigid-body solvers, MPM [28] for deformables, or SPH [46] for fluids; time step and resolution control stability. **Renderer** displays results through Camera, Lighting, and Shadows.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 物理引擎提供统一框架。**Entity** 为 $E=(Morph, Material, Surface)$：几何、刚体/可变形/液体行为、外观、速度、力、轨迹和约束。**Solver** 用刚体求解器、可变形体 MPM[28]或流体 SPH[46]计算动力学；时间步和分辨率控制稳定性。**Renderer** 通过 Camera、Lighting 和 Shadows 显示结果。

### 3.2 Manager Agent / 3.2 Manager Agent

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Manager interprets intent, plans, assigns one subtask at a time, verifies results, and iterates. It configures time step, substeps, gravity, MPM grid/domain, SPH particle size, shadows, background, particle mode, and segmentation. It advances or resets scenes to inspect intermediate states, then executes and captures the final video.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Manager 解读意图、规划、一次委派一个子任务、验证结果并迭代。它配置时间步、子步、重力、MPM 网格/域、SPH 粒子大小、阴影、背景、粒子模式和分割，并推进或重置场景检查中间状态，最后执行并捕获视频。

### 3.3 Entity Agent / 3.3 Entity Agent

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Entity retrieves BlenderKit² and PolyHaven³ assets using normalized text/CLIP [52] embeddings, metadata, and multiview images. Results include path, description, previews, score, and AABB. If retrieval fails, it calls Meshy [44], adjusts queries, then falls back to primitives. It computes scale, orientation, and position; enforces resting surfaces, non-interpenetration, and spacing; and uses Render feedback. It tunes Young’s modulus, Poisson’s ratio, yield stress, and solver-compatible scales. Motion uses PD control, rigid-body position/velocity/force commands, and particle emitters via per-step code.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Entity 用归一化文本/CLIP[52]嵌入、元数据和多视图图像检索 BlenderKit²、PolyHaven³资产，结果含路径、描述、预览、分数和 AABB。检索失败则调用 Meshy[44]、调整查询，最后退回基本体。它计算尺度、方向和位置，保证承载面、不穿插和间距，并使用 Render 反馈；调节杨氏模量、泊松比、屈服应力及求解器兼容尺度。运动通过逐步代码使用 PD、刚体位置/速度/力指令和粒子发射器。

² https://www.blenderkit.com/  ³ https://polyhaven.com/

### 3.4 Render Agent / 3.4 Render Agent

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Render grounds viewpoints in world coordinates, queries entity extents, and sets camera placement/intrinsics. Explicit code specifies orbit, dolly, tracking, and frame schedules; synchronized updates preserve temporal consistency and permit smoothing without changing physics. It configures directional lights, environment maps, or local sources while avoiding visible emitters and inconsistent illumination.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Render 将视点落到世界坐标，查询实体范围，设置相机位置/内参。显式代码规定环绕、推轨、跟踪和帧计划；同步更新保持时间一致，且可平滑轨迹而不改变物理。它配置方向光、环境图或局部光，避免可见光源和照明不一致。

## 4 Experiments / 4 实验

### 4.1 Setup / 4.1 设置

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We evaluate 24 NewtonGen [73] scenes testing 12 laws and 30 complex scenes with discontinuous multi-object dynamics and dynamic cameras. PIS is relative standard deviation of invariant quantities. Original Video-PIS uses SAM2 segmentation and approximate centroids; our State-PIS extracts exact 3D center-of-mass kinematics per timestep, inaccessible to pixel-only models. We also measure Perception Encoder alignment [7] and VBench Aesthetic [27]. Baselines are Sora-2 [48], Wan2.2 [57], SWE-Agent [67], and SWE-Agent w/ Visual. Genesis [3] is the engine; gpt-5 is the backbone unless stated. Outputs are 720p for fair comparison, although higher resolution is supported.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们评估测试 12 条定律的 24 个 NewtonGen[73]场景，以及具有非连续多物体动力学和动态相机的 30 个复杂场景。PIS 是不变量物理量的相对标准差。原始 Video-PIS 用 SAM2 分割和近似质心；我们的 State-PIS 每个时间步提取精确三维质心运动学，这是仅有像素模型无法获得的。还测量 Perception Encoder 对齐度[7]和 VBench Aesthetic[27]。基线是 Sora-2[48]、Wan2.2[57]、SWE-Agent[67]及 SWE-Agent w/ Visual。引擎为 Genesis[3]，默认骨干为 gpt-5。为公平比较输出 720p，但支持更高分辨率。

![Figure 3](assets/page_006_fig_figure_3.jpg)

**Caption:** Figure 3: Qualitative comparisons between GS-Agent and baseline methods. More cases are in Appendix C.

**Caption[CN]:** 图3：GS-Agent 与基线方法的定性比较。更多案例见附录 C。

![Tables 1–2](assets/page_007_table_table_1_2.jpg)

**Caption:** Table 1: Main results; average PIS over 24 NewtonGen scenes and alignment/aesthetic over 30 scenes, best bold and second underlined.

**Caption[CN]:** 表1：主要结果；24 个 NewtonGen 场景平均 PIS、30 个场景对齐度/美学，最佳粗体、次佳下划线。

| Method | Video-PIS | State-PIS | Alignment Score | Aesthetic |
|---|---:|---:|---:|---:|
| Sora2 [48] | 0.62 | - | 30.6 | 48.5 |
| Wan2.2 [57] | 0.46 | - | 29.8 | **58.1** |
| SWE-Agent [67] | 0.41 | 0.44 | 25.8 | 42.0 |
| SWE-Agent w/ Visual | 0.49 | 0.57 | 26.8 | 44.6 |
| GS-Agent (Ours) | **0.71** | **0.83** | **32.2** | 47.6 |

**Caption:** Table 2: User study results; mean scores over 270 effective responses.

**Caption[CN]:** 表2：用户研究结果；270 份有效回答的平均分。

| Method | Physical Plausibility | Camera Controllability | Content Alignment | Aesthetics |
|---|---:|---:|---:|---:|
| Sora2 [48] | 4.01 | 3.92 | 4.65 | **4.18** |
| Wan2.2 [57] | 2.72 | 3.49 | 4.45 | 3.71 |
| SWE-Agent [67] | 3.18 | 3.49 | 3.40 | 2.40 |
| SWE-Agent w/ Visual | 3.25 | 3.96 | 3.72 | 2.44 |
| GS-Agent(Ours) | **4.33** | **4.32** | **4.70** | <u>3.86</u> |

### 4.2 Main Results / 4.2 主要结果

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> GS-Agent follows prompts and physics better. Diffusion models hallucinate abrupt sponge fracture; Sora2’s bullet-water “cavitation trail” is physically wrong and Wan2.2 lacks fluid disintegration. A static background after 180° rotation exposes absent 3D reasoning. SWE-Agent is physically plausible but misses instructions. GS-Agent balances realism, fidelity, and coherence.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> GS-Agent 更好地遵循提示和物理。扩散模型臆造突兀海绵断裂；Sora2 的子弹穿水“空化轨迹”不符合物理，Wan2.2 缺少流体解体。旋转 180° 后背景静止暴露三维推理不足。SWE-Agent 物理合理但遗漏指令。GS-Agent 平衡真实感、保真度和连贯性。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Fifteen participants rated five randomly ordered videos on a 5-point Likert scale. Across 270 valid responses, humans preferred GS-Agent for physical plausibility, camera controllability, and content alignment, though it slightly lagged the closed-source state of the art in pure aesthetics; protocol is in Appendix C.2.
>
> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 15 名参与者用 5 点 Likert 量表评价五段随机排序视频。270 份有效回答显示，人类在物理合理性、相机可控性和内容对齐上偏好 GS-Agent，但纯美学略逊于闭源最先进模型；协议见附录 C.2。

![Figures 4–6](assets/page_008_fig_figure_4_5_6.jpg)

**Caption:** Figure 4: Autonomous error recovery; GS-Agent detects leaking asset and patches corners. Figure 5: Fine-grained control via slow motion, adding billiard balls, and velocity. Figure 6: Removing multi-agent design yields incomplete scenes; removing specialized interface yields unstable code.

**Caption[CN]:** 图4：自主错误恢复；GS-Agent 检测泄漏资产并修补角部。图5：通过慢动作、添加台球和速度实现细粒度控制。图6：移除多代理导致场景不完整，移除专门接口导致代码不稳定。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> It detects a non-watertight bathtub, proposes rigid material patches, and verifies the fix. Tool consolidation gives State-PIS 0.42 and alignment 27.9; GS-Agent gives 0.83 and 29.9. The specialized interface avoids syntax errors, bad parameters, and crashes. Backbone results (State-PIS/alignment/aesthetic): gpt-5 0.83/29.9/47.6; gemini-3-pro 0.81/28.2/45.7; Qwen3.5-27B 0.62/27.1/45.3.
>
> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 它检测不防水浴缸，提出刚性材料补丁并验证修复。合并工具的 State-PIS 为 0.42、对齐度 27.9；GS-Agent 为 0.83 和 29.9。专门接口避免语法错误、错误参数和崩溃。骨干结果（State-PIS/对齐度/美学）为：gpt-5 0.83/29.9/47.6；gemini-3-pro 0.81/28.2/45.7；Qwen3.5-27B 0.62/27.1/45.3。

![Tables 3–4](assets/page_009_table_table_3_4.jpg)

**Caption:** Table 3: Performance with different backbones. GS-Agent performs well with various backbones.

**Caption[CN]:** 表3：不同骨干性能。GS-Agent 在多种骨干上表现良好。

| Model | State PIS | Alignment Score | Aesthetic |
|---|---:|---:|---:|
| gpt-5 | 0.83 | 29.9 | 47.6 |
| gemini-3-pro | 0.81 | 28.2 | 45.7 |
| Qwen3.5-27B | 0.62 | 27.1 | 45.3 |

**Caption:** Table 4: Ablation study results.

**Caption[CN]:** 表4：消融结果。

| Method | State PIS | Alignment Score | Aesthetic |
|---|---:|---:|---:|
| GS-Agent | 0.83 | 29.9 | 47.6 |
| w/o Multi-Agent | 0.42 | 27.9 | 47.3 |
| w/o Agent-Sim Interface | 0.57 | 26.8 | 44.6 |

## 5 Discussions / 5 讨论

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> GS-Agent constructs more than video: metric depth maps, precise segmentation masks, surface normals, particle dynamics, and executable scripts for robotic reinforcement learning/evaluation. Deterministic engine execution gives geometry, motion, and material interactions internal consistency, unlike long-horizon diffusion.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> GS-Agent 构建的不只是视频：还有度量深度图、精确分割掩码、表面法线、粒子动力学，以及可用于机器人强化学习/评估的可执行脚本。确定性引擎执行让几何、运动和材料交互保持一致，不同于长时域扩散。

### 5.1 Limitations / 5.1 局限性

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Current simulation technology constrains fidelity and scalability [6], although humans can make complex game/film worlds with extensive effort; graphics and simulation progress [11] may raise the ceiling. Foundation-model self-critique of motion and cinematic expression is imperfect even with GPT-5 [29, 34]; progress in motion/cinematic understanding [45, 33] is needed.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 当前仿真技术限制保真度和可扩展性[6]，尽管人类可凭大量努力制作复杂游戏/电影世界；图形学和仿真进步[11]或提高上限。即便 GPT-5，基础模型对运动和电影表达的自我批评也不完美[29, 34]，仍需运动/电影理解进步[45, 33]。

## 6 Conclusion / 6 结论

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> GS-Agent places a physics engine in the loop and uses executable code, multimodal feedback, and collaboration to generate coherent, controllable physical worlds from natural language. It surpasses existing methods in plausibility and fine-grained control and points toward large-scale interactive consistent simulators bridging generative models, embodied intelligence, and physics simulation.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> GS-Agent 将物理引擎置于闭环，通过可执行代码、多模态反馈和协作从自然语言生成连贯可控的物理世界。它在合理性和细粒度控制上超越现有方法，并指向连接生成模型、具身智能和物理仿真的大规模交互一致模拟器。

## References / 参考文献

The complete reference list below is retained in the original searchable bibliographic form. / 以下完整参考文献保留原始可检索书目形式。

'''
# append marker; references and exact listings are appended with a separate command
p.write_text(s)
print('wrote', len(s.splitlines()), 'lines')
References
 [1] S. Agashe, K. Wong, V. Tu, J. Yang, A. Li, and X. E. Wang. Agent s2: A compositional
     generalist-specialist framework for computer use agents. arXiv preprint arXiv:2504.00906,
     2025.
 [2] M. Ahn, A. Brohan, N. Brown, Y. Chebotar, O. Cortes, B. David, C. Finn, K. Gopalakrishnan,
     K. Hausman, A. Herzog, et al. Do as i can, not as i say: Grounding language in robotic
     affordances. arXiv preprint arXiv:2204.01691, 2022.
 [3] G. Authors. Genesis: A generative and universal physics engine for robotics and beyond,
     December 2024.
 [4] S. Bahmani, I. Skorokhodov, V. Rong, G. Wetzstein, L. Guibas, P. Wonka, S. Tulyakov, J. J.
     Park, A. Tagliasacchi, and D. B. Lindell. 4d-fy: Text-to-4d generation using hybrid score
     distillation sampling. IEEE Conference on Computer Vision and Pattern Recognition (CVPR),
     2024.
 [5] A. Blattmann, T. Dockhorn, S. Kulal, D. Mendelevitch, M. Kilian, D. Lorenz, Y. Levi, Z. English,
     V. Voleti, A. Letts, et al. Stable video diffusion: Scaling latent video diffusion models to large
     datasets. arXiv preprint arXiv:2311.15127, 2023.
 [6] A. Boeing and T. Bräunl. Evaluation of real-time physics simulation systems. In Proceedings of
     the 5th international conference on Computer graphics and interactive techniques in Australia
     and Southeast Asia, pages 281–288, 2007.
 [7] D. Bolya, P.-Y. Huang, P. Sun, J. H. Cho, A. Madotto, C. Wei, T. Ma, J. Zhi, J. Rajasegaran,
     H. Rasheed, et al. Perception encoder: The best visual embeddings are not at the output of the
     network. arXiv preprint arXiv:2504.13181, 2025.
 [8] J. Bruce, M. D. Dennis, A. Edwards, J. Parker-Holder, Y. Shi, E. Hughes, M. Lai, A. Mavalankar,
     R. Steigerwald, C. Apps, et al. Genie: Generative interactive environments. In Forty-first
     International Conference on Machine Learning, 2024.
 [9] A. Chang, W. Monroe, M. Savva, C. Potts, and C. D. Manning. Text to 3d scene generation
     with rich lexical grounding. arXiv preprint arXiv:1505.06289, 2015.
[10] A. Chang, M. Savva, and C. D. Manning. Learning spatial knowledge for text to 3d scene
     generation. In Proceedings of the 2014 conference on empirical methods in natural language
     processing (EMNLP), pages 2028–2038, 2014.
[11] A. H. Chen, J. Hsu, Z. Liu, M. Macklin, Y. Yang, and C. Yuksel. Offset geometric contact.
     ACM Transactions on Graphics (TOG), 44(4):1–21, 2025.
[12] B. Chen, H. Jiang, S. Liu, S. Gupta, Y. Li, H. Zhao, and S. Wang. Physgen3d: Crafting a
     miniature interactive world from a single image. In Proceedings of the Computer Vision and
     Pattern Recognition Conference, pages 6178–6189, 2025.
[13] H. Chen, Y. Zhang, X. Cun, M. Xia, X. Wang, C. Weng, and Y. Shan. Videocrafter2: Overcoming
     data limitations for high-quality video diffusion models. In Proceedings of the IEEE/CVF
     Conference on Computer Vision and Pattern Recognition, pages 7310–7320, 2024.
[14] J. Chung, S. Lee, H. Nam, J. Lee, and K. M. Lee. Luciddreamer: Domain-free generation of 3d
     gaussian splatting scenes. arXiv preprint arXiv:2311.13384, 2023.
[15] Y. Du, S. Li, A. Torralba, J. B. Tenenbaum, and I. Mordatch. Improving factuality and reasoning
     in language models through multiagent debate. In Forty-first International Conference on
     Machine Learning, 2023.
[16] Y. Du, M. Yang, P. Florence, F. Xia, A. Wahid, B. Ichter, P. Sermanet, T. Yu, P. Abbeel, J. B.
     Tenenbaum, et al. Video language planning. arXiv preprint arXiv:2310.10625, 2023.
[17] N. Gillman, C. Herrmann, M. Freeman, D. Aggarwal, E. Luo, D. Sun, and C. Sun. Force
     prompting: Video generation models can learn and generalize physics-based control signals. In
     The Thirty-ninth Annual Conference on Neural Information Processing Systems.



[18] D. Guo, D. Yang, H. Zhang, J. Song, R. Zhang, R. Xu, Q. Zhu, S. Ma, P. Wang, X. Bi, et al.
     Deepseek-r1: Incentivizing reasoning capability in llms via reinforcement learning. arXiv
     preprint arXiv:2501.12948, 2025.
[19] I. Gur, H. Furuta, A. Huang, M. Safdari, Y. Matsuo, D. Eck, and A. Faust. A real-world
     webagent with planning, long context understanding, and program synthesis. arXiv preprint
     arXiv:2307.12856, 2023.
[20] H. He, Y. Xu, Y. Guo, G. Wetzstein, B. Dai, H. Li, and C. Yang. Cameractrl: Enabling camera
     control for text-to-video generation. arXiv preprint arXiv:2404.02101, 2024.
[21] J. Ho, W. Chan, C. Saharia, J. Whang, R. Gao, A. Gritsenko, D. P. Kingma, B. Poole, M. Norouzi,
     D. J. Fleet, et al. Imagen video: High definition video generation with diffusion models. arXiv
     preprint arXiv:2210.02303, 2022.
[22] J. Ho, A. Jain, and P. Abbeel. Denoising diffusion probabilistic models. Advances in neural
     information processing systems, 33:6840–6851, 2020.
[23] W. Hong, W. Wang, Q. Lv, J. Xu, W. Yu, J. Ji, Y. Wang, Z. Wang, Y. Dong, M. Ding, et al.
     Cogagent: A visual language model for gui agents. In Proceedings of the IEEE/CVF Conference
     on Computer Vision and Pattern Recognition, pages 14281–14290, 2024.
[24] M. Hu, Y. Zhou, W. Fan, Y. Nie, B. Xia, T. Sun, Z. Ye, Z. Jin, Y. Li, Q. Chen, et al. Owl:
     Optimized workforce learning for general multi-agent assistance in real-world task automation.
     arXiv preprint arXiv:2505.23885, 2025.
[25] Z. Hu, A. Iscen, A. Jain, T. Kipf, Y. Yue, D. A. Ross, C. Schmid, and A. Fathi. Scenecraft: An
     llm agent for synthesizing 3d scenes as blender code. In Forty-first International Conference on
     Machine Learning, 2024.
[26] W. Huang, C. Wang, R. Zhang, Y. Li, J. Wu, and L. Fei-Fei. Voxposer: Composable 3d value
     maps for robotic manipulation with language models. In Conference on Robot Learning, pages
     540–562. PMLR, 2023.
[27] Z. Huang, Y. He, J. Yu, F. Zhang, C. Si, Y. Jiang, Y. Zhang, T. Wu, Q. Jin, N. Chanpaisit,
     et al. Vbench: Comprehensive benchmark suite for video generative models. In Proceedings of
     the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 21807–21818,
     2024.
[28] C. Jiang, C. Schroeder, J. Teran, A. Stomakhin, and A. Selle. The material point method for
     simulating continuum materials. In Acm siggraph 2016 courses, pages 1–52. 2016.
[29] B. Kang, Y. Yue, R. Lu, Z. Lin, Y. Zhao, K. Wang, G. Huang, and J. Feng. How far is video
     generation from world model: A physical law perspective. arXiv preprint arXiv:2411.02385,
     2024.
[30] D. Kondratyuk, L. Yu, X. Gu, J. Lezama, J. Huang, G. Schindler, R. Hornung, V. Birodkar,
     J. Yan, M.-C. Chiu, et al. Videopoet: A large language model for zero-shot video generation.
     arXiv preprint arXiv:2312.14125, 2023.
[31] G. Li, H. Hammoud, H. Itani, D. Khizbullin, and B. Ghanem. Camel: Communicative agents
     for” mind” exploration of large language model society. Advances in Neural Information
     Processing Systems, 36:51991–52008, 2023.
[32] Z. Li, H.-X. Yu, W. Liu, Y. Yang, C. Herrmann, G. Wetzstein, and J. Wu. Wonderplay: Dynamic
     3d scene generation from a single image and actions. arXiv preprint arXiv:2505.18151, 2025.
[33] Z. Lin, S. Cen, D. Jiang, J. Karhade, H. Wang, C. Mitra, T. Ling, Y. Huang, S. Liu, M. Chen,
     et al. Towards understanding camera motions in any video. arXiv preprint arXiv:2504.15376,
     2025.
[34] H. Liu, J. He, Y. Jin, D. Zheng, Y. Dong, F. Zhang, Z. Huang, Y. He, Y. Li, W. Chen, et al.
     Shotbench: Expert-level cinematic understanding in vision-language models. arXiv preprint
     arXiv:2506.21356, 2025.



[35] H. Liu, C. Li, Z. Li, Y. Wu, W. Li, Z. Yang, Z. Zhang, Y. Lin, S. Han, and B. Y. Feng. Ir3d-
     bench: Evaluating vision-language model scene understanding as agentic inverse rendering. In
     The Thirty-ninth Annual Conference on Neural Information Processing Systems Datasets and
     Benchmarks Track.
[36] H. Liu, C. Li, Q. Wu, and Y. J. Lee. Visual instruction tuning. arXiv preprint arXiv:2304.08485,
     2023.
[37] N. Liu, X.-W. Hua, R. Zhang, and L. Wang. Physical material editing with structure embedding
     for realistic deformable objects. In Proceedings of the ACM Symposium on Interactive 3D
     Graphics and Games (I3D), 2012.
[38] S. Liu, Z. Ren, S. Gupta, and S. Wang. Physgen: Rigid-body physics-grounded image-to-video
     generation. In European Conference on Computer Vision, pages 360–378. Springer, 2024.
[39] Z. Liu, Y. Zhang, P. Li, Y. Liu, and D. Yang. A dynamic LLM-powered agent network for
     task-oriented agent collaboration. In First Conference on Language Modeling, 2024.
[40] S. Lu, G. Chen, N. A. Dinh, I. Lang, A. Holtzman, and R. Hanocka. Ll3m: Large language 3d
     modelers. arXiv preprint arXiv:2508.08228, 2025.
[41] J. Lv, Y. Huang, M. Yan, J. Huang, J. Liu, Y. Liu, Y. Wen, X. Chen, and S. Chen. Gpt4motion:
     Scripting physical motions in text-to-video generation via blender-oriented gpt planning. In
     Proceedings of the IEEE/CVF conference on computer vision and pattern recognition, pages
     1430–1440, 2024.
[42] R. Ma, A. G. Patil, M. Fisher, M. Li, S. Pirk, B.-S. Hua, S.-K. Yeung, X. Tong, L. Guibas, and
     H. Zhang. Language-driven synthesis of 3d scenes from scene databases. ACM Transactions on
     Graphics (TOG), 37(6):1–16, 2018.
[43] F. Meng, J. Liao, X. Tan, W. Shao, Q. Lu, K. Zhang, Y. Cheng, D. Li, Y. Qiao, and P. Luo. To-
     wards world simulator: Crafting physical commonsense-based benchmark for video generation.
     arXiv preprint arXiv:2410.05363, 2024.
[44] Meshy. Meshy: Generative ai for 3d content creation, 2024. Accessed: 2026-01-29.
[45] S. Motamed, M. Chen, L. Van Gool, and I. Laina. Travl: A recipe for making video-language
     models better judges of physics implausibility. arXiv preprint arXiv:2510.07550, 2025.
[46] M. Müller, D. Charypar, and M. Gross. Particle-based fluid simulation for interactive applica-
     tions. In Proceedings of the 2003 ACM SIGGRAPH/Eurographics symposium on Computer
     animation, pages 154–159, 2003.
[47] OpenAI. Gpt-4 technical report, 2023.
[48] OpenAI. Sora 2, 2025. Video and audio generation model; released 30 Sep 2025.
[49] J. Parker-Holder and S. Fruchter. Genie 3: A new frontier for world models. Google DeepMind
     Blog, 2025.
[50] W. Peebles and S. Xie. Scalable diffusion models with transformers. In Proceedings of the
     IEEE/CVF international conference on computer vision, pages 4195–4205, 2023.
[51] J. Qiu, X. Qi, T. Zhang, X. Juan, J. Guo, Y. Lu, Y. Wang, Z. Yao, Q. Ren, X. Jiang, et al. Alita:
     Generalist agent enabling scalable agentic reasoning with minimal predefinition and maximal
     self-evolution. arXiv preprint arXiv:2505.20286, 2025.
[52] A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, G. Goh, S. Agarwal, G. Sastry, A. Askell,
     P. Mishkin, J. Clark, et al. Learning transferable visual models from natural language supervision.
     In International conference on machine learning, pages 8748–8763. PmLR, 2021.
[53] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, and S. Yao. Reflexion: Language agents
     with verbal reinforcement learning. Advances in Neural Information Processing Systems, 36,
     2024.



[54] J. Sohl-Dickstein, E. Weiss, N. Maheswaranathan, and S. Ganguli. Deep unsupervised learning
     using nonequilibrium thermodynamics. In International conference on machine learning, pages
     2256–2265. pmlr, 2015.
[55] T. Sumers, S. Yao, K. Narasimhan, and T. L. Griffiths. Cognitive architectures for language
     agents. arXiv preprint arXiv:2309.02427, 2023.
[56] C. Sun, J. Han, W. Deng, X. Wang, Z. Qin, and S. Gould. 3d-gpt: Procedural 3d modeling
     with large language models. In 2025 International Conference on 3D Vision (3DV), pages
     1253–1263. IEEE, 2025.
[57] T. Wan, A. Wang, B. Ai, B. Wen, C. Mao, C.-W. Xie, D. Chen, F. Yu, H. Zhao, J. Yang, J. Zeng,
     J. Wang, J. Zhang, J. Zhou, J. Wang, J. Chen, K. Zhu, K. Zhao, K. Yan, L. Huang, M. Feng,
     N. Zhang, P. Li, P. Wu, R. Chu, R. Feng, S. Zhang, S. Sun, T. Fang, T. Wang, T. Gui, T. Weng,
     T. Shen, W. Lin, W. Wang, W. Wang, W. Zhou, W. Wang, W. Shen, W. Yu, X. Shi, X. Huang,
     X. Xu, Y. Kou, Y. Lv, Y. Li, Y. Liu, Y. Wang, Y. Zhang, Y. Huang, Y. Li, Y. Wu, Y. Liu, Y. Pan,
     Y. Zheng, Y. Hong, Y. Shi, Y. Feng, Z. Jiang, Z. Han, Z.-F. Wu, and Z. Liu. Wan: Open and
     advanced large-scale video generative models. arXiv preprint arXiv:2503.20314, 2025.
[58] C. Wang, C. Chen, Y. Huang, Z. Dou, Y. Liu, J. Gu, and L. Liu. Physctrl: Generative physics
     for controllable and physics-grounded video generation. In The Thirty-ninth Annual Conference
     on Neural Information Processing Systems.
[59] L. Wang, C. Ma, X. Feng, Z. Zhang, H. Yang, J. Zhang, Z. Chen, J. Tang, X. Chen, Y. Lin, et al.
     A survey on large language model based autonomous agents. arXiv preprint arXiv:2308.11432,
     2023.
[60] Y. Wang, X. Qiu, J. Liu, Z. Chen, J. Cai, Y. Wang, T.-H. Wang, Z. Xian, and C. Gan. Architect:
     Generating vivid and interactive 3d scenes with hierarchical 2d inpainting. Advances in Neural
     Information Processing Systems, 37:67575–67603, 2024.
[61] Z. Wang, D. Li, Y. Wu, T. He, J. Bian, and R. Jiang. Diffusion models in 3d vision: A survey.
     arXiv preprint arXiv:2410.04738, 2024.
[62] Q. Wu, G. Bansal, J. Zhang, Y. Wu, B. Li, E. Zhu, L. Jiang, X. Zhang, S. Zhang, J. Liu, et al.
     Autogen: Enabling next-gen llm applications via multi-agent conversations. In First Conference
     on Language Modeling, 2024.
[63] Z. Xi, W. Chen, X. Guo, W. He, Y. Ding, B. Hong, M. Zhang, J. Wang, S. Jin, E. Zhou,
     et al. The rise and potential of large language model based agents: A survey. arXiv preprint
     arXiv:2309.07864, 2023.
[64] J. Xiang, G. Liu, Y. Gu, Q. Gao, Y. Ning, Y. Zha, Z. Feng, T. Tao, S. Hao, Y. Shi, et al. Pandora:
     Towards general world model with natural language actions and video states. arXiv preprint
     arXiv:2406.09455, 2024.
[65] T. Xie, Z. Zong, Y. Qiu, X. Li, Y. Feng, Y. Yang, and C. Jiang. Physgaussian: Physics-integrated
     3d gaussians for generative dynamics. In Proceedings of the IEEE/CVF Conference on Computer
     Vision and Pattern Recognition (CVPR), pages 4389–4398, June 2024.
[66] D. Xu, H. Liang, N. P. Bhatt, H. Hu, H. Liang, K. N. Plataniotis, and Z. Wang. Comp4d:
     Llm-guided compositional 4d scene generation. arXiv preprint arXiv:2403.16993, 2024.
[67] J. Yang, C. E. Jimenez, A. Wettig, K. Lieret, S. Yao, K. Narasimhan, and O. Press. Swe-
     agent: Agent-computer interfaces enable automated software engineering. Advances in Neural
     Information Processing Systems, 37:50528–50652, 2024.
[68] Z. Yang, J. Teng, W. Zheng, M. Ding, S. Huang, J. Xu, Y. Yang, W. Hong, X. Zhang, G. Feng,
     et al. Cogvideox: Text-to-video diffusion models with an expert transformer. In The Thirteenth
     International Conference on Learning Representations, 2024.
[69] S. Yin, J. Ge, Z. Z. Wang, C. Wang, X. Li, M. J. Black, T. Darrell, A. Kanazawa, and
     H. Feng. Vision-as-inverse-graphics agent via interleaved multimodal reasoning. arXiv preprint
     arXiv:2601.11109, 2026.



[70] H.-X. Yu, H. Duan, C. Herrmann, W. T. Freeman, and J. Wu. Wonderworld: Interactive 3d
     scene generation from a single image. In Proceedings of the Computer Vision and Pattern
     Recognition Conference, pages 5916–5926, 2025.
[71] H.-X. Yu, H. Duan, J. Hur, K. Sargent, M. Rubinstein, W. T. Freeman, F. Cole, D. Sun,
     N. Snavely, J. Wu, et al. Wonderjourney: Going from anywhere to everywhere. In Proceedings
     of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 6658–6667,
     2024.
[72] L. Yu, Y. Cheng, K. Sohn, J. Lezama, H. Zhang, H. Chang, A. G. Hauptmann, M.-H. Yang,
     Y. Hao, I. Essa, et al. Magvit: Masked generative video transformer. In Proceedings of the
     IEEE/CVF Conference on Computer Vision and Pattern Recognition, pages 10459–10469, 2023.
[73] Y. Yuan, X. Wang, T. Wickremasinghe, Z. Nadir, B. Ma, and S. H. Chan. Newtongen: Physics-
     consistent and controllable text-to-video generation via neural newtonian dynamics. arXiv
     preprint arXiv:2509.21309, 2025.
[74] H. Zhang, W. Du, J. Shan, Q. Zhou, Y. Du, J. B. Tenenbaum, T. Shu, and C. Gan. Building co-
     operative embodied agents modularly with large language models. In The Twelfth International
     Conference on Learning Representations, 2024.
[75] Q. Zhang, P. Jing, H.-X. Yu, F. Ding, F. Nie, W. Wang, Y. Du, J. Zou, J. Wu, and B. Shuai.
     Physion-eval: Evaluating physical realism in generated video via human reasoning. arXiv
     preprint arXiv:2603.19607, 2026.
[76] T. Zhang, H.-X. Yu, R. Wu, B. Y. Feng, C. Zheng, N. Snavely, J. Wu, and W. T. Freeman.
     PhysDreamer: Physics-based interaction with 3d objects via video generation. In European
     Conference on Computer Vision. Springer, 2024.
[77] Z. Zhang, J. Liao, M. Li, Z. Dai, B. Qiu, S. Zhu, L. Qin, and W. Wang. Tora: Trajectory-oriented
     diffusion transformer for video generation. In Proceedings of the IEEE/CVF Conference on
     Computer Vision and Pattern Recognition (CVPR), pages 2063–2073, June 2025.
[78] W. Zhao, J. P. Queralta, and T. Westerlund. Sim-to-real transfer in deep reinforcement learning
     for robotics: a survey. In 2020 IEEE symposium series on computational intelligence (SSCI),
     pages 737–744. IEEE, 2020.





# Appendix A Broader Impact / 附录 A 更广泛影响

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> GS-Agent lowers the barrier to complex physically grounded 4D environments and scalable multimodal synthetic data, but raises dual-use, misinformation, labor, and carbon-footprint concerns. Mitigations are cryptographic provenance/watermarks, safety guardrails, transparency, and open evaluation.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> GS-Agent 降低复杂物理四维环境和可扩展多模态合成数据的门槛，但带来双重用途、错误信息、就业和碳足迹问题。缓解措施是密码学溯源/水印、安全护栏、透明性和开放评估。

# Appendix B Additional Implementation Details / 附录 B 补充实现细节

## B.1 Agent-Simulation Interface / B.1 代理–仿真器接口

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Existing APIs target human experts. GS-Agent gives each agent a responsibility-aligned toolbox plus shared generic tools; Manager configures simulation and time, Entity accepts `<name>` and `<code>` for geometry/physics/control, and Render configures camera, lighting, renderer, frames, and video logic.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 现有 API 面向人类专家。GS-Agent 为每个代理提供职责专用工具箱及共享通用工具；Manager 配置仿真和时间，Entity 用 `<name>`、`<code>`表达几何/物理/控制，Render 配置相机、照明、渲染器、帧和视频逻辑。

![Table 5](assets/page_009_table_table_3_4.jpg)

**Caption:** Table 5: Agent-Simulation Interface as Tools. Required parameters are enclosed in <> and optional parameters in [ ].

**Caption[CN]:** 表5：作为工具的代理–仿真器接口。必需参数用 <>，可选参数用 [ ]。

| Group | Name | Parameters | Description |
|---|---|---|---|
| Generic | `GetSceneInfo` | - | Current scene information / 当前场景信息 |
| Generic | `GetEntityInfo` | `<name>` | Specific entity information / 特定实体信息 |
| Generic | `SendMessage` | `<recipient> <message> <image>` | Optional image/video message / 可选图像/视频消息 |
| Manager | `ConfigureSimOptions` | `[dt] [substeps] [gravity]` | Simulation options / 仿真选项 |
| Manager | `ConfigureMPMOptions` | `[grid density] [particle size] [enable CPIC] [lower bound] [upper bound]` | MPM options / MPM 选项 |
| Manager | `ConfigureSPHOptions` | `[particle size] [lower bound] [upper bound]` | SPH options / SPH 选项 |
| Manager | `ConfigureVisOptions` | `[show world frame] [show link frame] [show cameras] [shadow] [background color] [segmentation level]` | Visualization / 可视化 |
| Manager | `AdvanceScene` | `<steps>` | Advance n steps / 推进 n 步 |
| Manager | `ResetScene` | - | Reset scene / 重置场景 |
| Manager | `FinalizeOutcome` | `<video path>` | Signal completion / 标记完成 |
| Entity | `AddEntity`, `UpdateEntity` | `<name> <code>` | Add/update entity / 添加或更新实体 |
| Entity | `RemoveEntity` | `<name>` | Remove entity / 移除实体 |
| Entity | `AddEmitter`, `UpdateEmitter` | `<name> <code>` | Add/update fluid emitter / 添加或更新流体发射器 |
| Entity | `RemoveEmitter` | `<name>` | Remove emitter / 移除发射器 |
| Entity | `RetrieveAsset`, `GenerateAsset` | `<query>` | Retrieve/generate mesh / 检索/生成网格 |
| Entity | `ConfigureEntitiesControl` | `<code>` | Per-step control / 逐步控制 |
| Render | `GetCameraInfo`, `GetLightingInfo` | - | Query configuration / 查询配置 |
| Render | `ConfigureRenderer` | `<renderer>` | `Rasterizer` or `RayTracer` |
| Render | `ConfigureCameraModel` | `[res] [pos] [lookat] [up] [fov] [model] [aperture] [spp]` | Camera parameters / 相机参数 |
| Render | `AddDirectionalLight` | `<dir> <color> <intensity>` | Directional light / 方向光 |
| Render | `ClearDirectionalLights` | - | Clear directional lights / 清除方向光 |
| Render | `AddSphereLight` | `<pos> <color> <intensity> <radius>` | Sphere light / 球形光 |
| Render | `ClearSphereLights` | - | Clear sphere lights / 清除球形光 |
| Render | `AddEnvSphere` | `<hdri> <color> [radius] [pos] [euler]` | Environment sphere / 环境球 |
| Render | `RemoveEnvSphere` | - | Remove environment / 移除环境球 |
| Render | `RenderCurrentFrame` | - | Render image / 渲染图像 |
| Render | `ConfigureCameraControl` | `<code>` | Camera/video control / 相机视频控制 |

## B.2 Prompts / B.2 提示词

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Full Manager, Entity, and Render system prompts are in Listings 1, 2, and 3.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> Manager、Entity 和 Render 的完整系统提示词见列表1、2、3。

## B.3 Agent self-review / B.3 代理自审

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> `AdvanceScene` returns rendered video for Manager review. The agent may diagnose a non-watertight collider and ask Entity to replace it with a watertight inner container; Render/Entity review images and adjust camera or materials until satisfied or tool limits.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> `AdvanceScene` 返回视频供 Manager 审查。代理可诊断不防水碰撞体，并要求 Entity 换成防水内部容器；Render/Entity 审查图像、调节相机或材料，直到满意或达到工具限制。

# Appendix C Additional Experiment Details / 附录 C 补充实验细节

## C.1 More Qualitative Comparisons / C.1 更多定性比较

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Figure 7 shows more qualitative comparisons between GS-Agent and baselines.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 图7展示 GS-Agent 与基线的更多定性比较。

![Figure 7](assets/page_017_fig_figure_7.jpg)

**Caption:** Figure 7: More qualitative comparisons between GS-Agent (Ours) and the baseline methods.

**Caption[CN]:** 图7：GS-Agent（Ours）与基线方法的更多定性比较。

## C.2 User Study / C.2 用户研究

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Fifteen subjects rated five randomly ordered videos on a 5-point Likert scale; 270 effective responses were collected. Physical Plausibility requires lawful continuous motion, consistent materials, no teleporting, conservation, consistent liquid behavior, and proportionate forces. Camera Controllability requires stable prompt-following framing and smooth pan/tilt/zoom/dolly without jitter, flicker, clipping, or target switches; missing requested motion is penalized. Content Alignment measures object/action/scene/style match. Aesthetics measures composition, clarity, lighting/shadows, color/contrast, and absence of noise, banding, blur, flicker, and temporal glitches.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 15 名受试者以 5 点 Likert 量表评价五段随机视频，共 270 份有效回答。物理合理性要求连续守法运动、材料一致、无瞬移、守恒、液体一致和相称的力。相机可控性要求稳定遵循提示、构图及运动平滑且无抖动/闪烁/裁剪/随机目标，缺少指定运动扣分。内容对齐衡量物体/动作/场景/风格匹配。美学衡量构图、清晰度、光影、颜色/对比以及无噪声、条带、模糊、闪烁和时间伪影。

![Figure 8](assets/page_018_fig_figure_8.jpg)

**Caption:** Figure 8: User study interface.

**Caption[CN]:** 图8：用户研究界面。

## C.3 Failure Analysis / C.3 失败分析

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Context contamination causes confirmation bias from lengthy plans; failure misattribution leads to tuning the wrong parameter (e.g., friction instead of initial velocity); hallucinated unsupported APIs, material properties, or conventions cause execution errors and fallback attempts.
>
> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 上下文污染使冗长计划造成确认偏误；失败错误归因会调错参数（例如调摩擦而非初始速度）；臆造不受支持的 API、材料属性或约定会造成执行错误和回退。

# Exact source prompts / 原文完整提示词

```text
Listing 1: System prompt for the Manager Agent.
You’re Manager Agent, a highly advanced AI agent that transforms any natural
    language instruction into a physically and visually realistic dynamic world
    using the Genesis Physics Engine and an asset library. You have two
    collaborators: Entity Agent and Render Agent. Entity Agent specializes in
    retrieving realistic assets, creating and managing one entity at a time, and
    controlling entity motions. Render Agent is responsible for configuring
    cameras, lighting, and renderer settings; controlling camera motions, render
    frequencies, and video recording timing.

Given the user’s instruction, carefully plan each step to ensure both physical
    plausibility and visual realism. Break work into clear, manageable tasks and
    assign them one at a time to your collaborators. Keep your instructions
    precise and concise without overwhelming details, verify their outputs
    critically, and iterate until results meet expectations. Apart from assigning
    tasks to your collaborators and verifying outputs, you are also responsible
    for configuring scene options including solvers and visualization parameters,
    advancing and resetting scenes based on your plan and feedback from the
    collaborators. Continue until you have built the complete dynamic physical
    world and rendered a final video for the user, never stop early or hand back
    due to uncertainty. Make reasonable assumptions if needed, document them
    afterward.

<tool_preambles>
- You MUST plan extensively before EACH tool call, and reflect extensively on the
    outcome of EACH tool call.
- DO NOT do this entire process by making tool calls only.
- As you execute your tools, narrate each step succinctly and sequentially, marking
    progress clearly.
</tool_preambles>

<persistence>
- You are an agent - please keep going until the complete dynamic physical world is
    built, and the video user requested is finalized and the path of which is
    reported by calling tool ‘finalize_outcome‘, before ending your turn and
    yielding back to the user.
- Only terminate your turn when you are sure that the dynamic physical world is
    built, and the video user requested is rendered.
- Never stop or hand back to the user when you encounter uncertainty or errors,
    research or deduce the most reasonable approach and continue.
- Do not ask the human to confirm plans or clarify assumptions, as you can always
    adjust later, decide what the most effective plan and reasonable assumption
    is, and proceed with it.
</persistence>

Reminders:
- Always communicate with collaborators via the ‘send_message‘ tool.
- Keep your instructions precise and concise, state qualitative targets and
    acceptance criteria, and let your collaborators decide exact details like
    material parameters themselves.
- You do not understand the meanings or effects of entity or rendering parameters
    beyond your own tool scope. Do not attempt to adjust or reason about them.
    Instead, focus on clearly stating the intended visual or functional goal,
    leaving parameter tuning to the Entity Agent and the Render Agent.
- You MUST send exactly one actionable task per message to a collaborator. Do not
    bundle multiple creations or controls in a single message. After each
    collaborator’s reply, verify, reflect, and only then send the next single task.
- Do not just repeat your instructions when their response is not satisfactory;
    instead, reflect on what might have gone wrong, adjust your instructions
    accordingly, and send a new message with updated details.
- Always be critical of the work done by your collaborators. Always verify their
    work by examining the returned entity information or visual feedback. If the
    visualization does not meet your expectations, ask the Render Agent to
    re-render with more specific instructions or request that the Entity Agent




    adjust the entity placement. Do not assume your instruction is fulfilled
    correctly without verification.
- Use your own tools when appropriate, such as for scene configuration.
- Render Agent can not render videos and can only configure the recording timings
    of the camera. To render a video, ask the Render Agent to configure the
    desired recording timing, then use the ‘advance_scene‘ tool to record the
    desired horizon. Video recording normally only starts at scene step 0. Check
    the current time step before advancing the scene every time, and use the
    ‘reset_scene‘ tool when necessary. Unless otherwise specified, always let the
    Render Agent decide on video fps on its own.
- For rigid-only simulation, use the default time step of 0.01 and substeps of 1.
- For advanced material models such as MPM and SPH, use a smaller time step (e.g.,
    0.001 or less) and increase the number of simulation substeps (e.g., 5 or
    more) to maintain numerical stability. Adjust these values based on the
    specific parameters configured by the Entity Agent.
- Always run a few steps of simulation after creating or modifying entities to
    ensure they are stable before presenting the world to the user.
- Always strictly follow the coordinate system in the Genesis Physics Simulator. Do
    not assume conventions from other 3D, graphics, or physics engines. When
    interpreting spatial directions (such as ’in front of’, ’looking from the
    right’, etc.), always map these to the Genesis coordinate system:
  - Origin: Center of the world ([0, 0, 0])
  - Positive x-axis: Forward
  - Positive y-axis: Right
  - Positive z-axis: Up
- The center of geometry defines the position of an entity.
- Always begin by verifying that all entity placements and movements behave as
    expected. Ask the Render Agent to configure a fixed camera view using the fast
    Rasterizer renderer for quick visual validation. Only after confirming that
    entities are placed as requested and moving correctly, instruct the Render
    Agent to set up advanced camera motions and lighting effects with the
    high-quality Raytracer renderer for the final video output.
- Instruct Render Agent to configure lights in a way that light sources are not
    visible in the scene, unless the user specifically requests them to be visible.
- Once you’ve built the dynamic physical world and rendered a satisfiable final
    video, call ‘finalize_outcome‘ tool to signal that the task has been finished
    and provide the final video path. The final video should be of resolution 1280
    x 720, and 3~10 seconds long; otherwise, instruct the Render Agent to adjust
    accordingly when recording the final video.





                      Listing 2: System prompt for the Entity Agent.
You’re Entity Agent, specialized in curating realistic assets by retrieval or
    generation, creating and managing entities in the Genesis Physics Engine based
    on instructions from Manager Agent. You collaborate with Render Agent, who
    handles scene visualization and provides visual feedback to you. Your primary
    task is to create or update one entity at a time using the tools available.

<tool_preambles>
- You MUST plan extensively before EACH tool call, and reflect extensively on the
    outcome of EACH tool call.
- DO NOT do this entire process by making tool calls only.
- As you execute your tools, narrate each step succinctly and sequentially, marking
    progress clearly.
- Finish by using the ‘send_message‘ tool to reply to the invoking agent and work
    on new tasks once received as tool result of ‘send_message‘.
</tool_preambles>

An entity consists of three components:
- Morph: defines the shape and geometry
- Material: defines physical properties
- Surface: defines visual appearance

Your Workflow:

1. Always start by adding a fixed plane to the scene unless one already exists.
    This ensures entities do not fall through the world due to gravity.
2. Carefully interpret the instruction from the Manager Agent. If anything is
    unclear or missing, use ‘send_message‘ to request clarification from the
    Manager Agent.
3. Create or modify the entity:
- Always seek suitable assets in the library first. Only try to generate assets or
    use primitives when there’s no good choice.
- With a curated asset, the appropriate ‘scale‘ and ‘position‘ should be computed
    based on the asset’s bounds and the desired world-space alignment.
- Avoid placing entities too close together to prevent collisions.
4. Verify the entity’s creation or modification:
- Use the get_entity_info tool to retrieve the current details of the entity.
- Use the ‘send_message‘ tool to ask the Render Agent to provide visual feedback if
    needed.
- Make sure no entity is in collision with other entities. Otherwise, adjust the
    ‘euler‘, ‘scale‘, and ‘position‘ accordingly.
- Make sure the spatial relationships among entities are as expected. Otherwise,
    adjust the ‘euler‘, ‘scale‘, and ‘position‘ accordingly and ask the Render
    Agent to provide visual feedback to verify again.
5. Configure the entity control function.
6. Use the ‘send_message‘ tool to reply to the Manager Agent before you can get new
    task instructions.

Reminders:

- You are only responsible for one entity at a time.
- Render Agent can only visualize the current frame at a viewpoint; it cannot
    render videos and does not modify entities.
- Always ensure physical plausibility (gravity, spacing, elasticity, viscousness,
    ...).
- Avoid overlapping entities to prevent collisions.
- Always strictly follow the coordinate system in the Genesis Physics Engine. Do
    not assume conventions from other 3D, graphics, or physics engines. When
    interpreting spatial directions (such as ’in front of’, ’to the right of’,
    etc.), always map these to the Genesis coordinate system:
  - **Origin:** Center of the world ([0, 0, 0])
  - **Positive x-axis:** Forward
  - **Positive y-axis:** Right
  - **Positive z-axis:** Up




- The center of geometry defines the position of an entity.
- If retrieved assets are not suitable, do not use them.
- There might be discrepancies between the asset’s bounding box and the actual
    geometry after loading into Genesis. Always verify the entity’s bounding box
    after creation.
- Fixed entity has zero dofs and cannot be controlled.
- A non-articulated rigid entity has 6 dofs, in the form of [x, y, z, roll, pitch,
    yaw]
- Prioritize "recon" vis_mode for particle materials MPM and SPH. The default
    vis_mode of "visual" is only appropriate for rigid materials.
- Only control an entity’s motion via the ‘configure_entities_control‘ tool, not
    the ‘add_entity‘ tool.
- Favor informative code over defensive code, design it so that failures expose the
    underlying issue clearly through runtime results.
- You MUST use the ‘send_message‘ tool to reply to the Manager Agent before you can
    get new task instructions.





                     Listing 3: System prompt for the Render Agent.
You’re Render Agent, a specialist in camera manipulation, lighting configuration,
    and scene visualization within the Genesis Physics Engine. Your primary
    responsibility is to accurately configure cameras, lighting, and the renderer
    based on instructions, render the current frame to provide clear visual
    feedback to your collaborators, and control camera motions and recording
    timings. You have two collaborators: Manager Agent - a highly advanced AI
    system designed to turn any natural language instruction into a physical
    dynamic world by interfacing with Genesis Physics Engine via tools. Entity
    Agent - creates and manages entities in the scene and may request
    visualizations of specific entities. When you have completed the task, use the
    ‘send_message‘ tool to inform the collaborators that the rendering has been
    completed successfully and provide the rendered image path, if any. You MUST
    use the ‘send_message‘ tool to reply to the invoking agent before you can get
    new task instructions.

<tool_preambles>
- You MUST plan extensively before EACH tool call, and reflect extensively on the
    outcome of EACH tool call.
- DO NOT do this entire process by making tool calls only.
- As you execute your tools, narrate each step succinctly and sequentially, marking
    progress clearly.
- Finish by using the ‘send_message‘ tool to reply to the invoking agent and work
    on new tasks once received as tool result of ‘send_message‘.
</tool_preambles>

Reminders:
- There are two renderers in the Genesis Physics Engine: fast Rasterizer and
    high-quality RayTracer. Rasterizer, used by default, is suitable for real-time
    rendering and quick previews, while RayTracer provides more realistic lighting
    and shadows but is slower, and should be used only for final results.
- Different renderers support different lighting options. Rasterizer supports
    configuring DirectionalLight only, while RayTracer supports configuring
    SphereLight and EnvSphere only. All lights will be cleared when the renderer
    is configured.
  - DirectionalLight is a light source that acts as though they are infinitely far
      away and emits light in the specified direction with specified color and
      intensity.
  - SphereLight is a sphere-shaped mesh light that can be placed anywhere in the
      scene and has a position, radius, color, and intensity. Point light and be
      simulated as a SphereLight of appropriate radius and intensity. Directional
      light can be simulated as a SphereLight at infinity with a very large radius
      and intensity. Note that the SphereLight is visible in the scene, so it can
      affect the appearance of the rendered image or video. Try to place
      SphereLight in a way that it does not obstruct the view of the main subject
      of the scene and is out of the camera’s view.
  - EnvSphere is an hdri/exr image-textured sphere that provides ambient lighting
      to the entire scene. It has a position, radius, color, and intensity. It is
      typically used to provide a base level of illumination in the scene.
- You cannot render entities that are not in the scene or have not been created
    yet. Always check what entities exist by calling get_scene_info, and gain
    information about the entity of interest by calling get_entity_info before
    rendering.
- You cannot render videos directly; instead, you can use the
    ‘configure_camera_control‘ tool to set up camera movements and recording
    timing for the Manager Agent to render videos when advancing scenes.
- Always strictly follow the coordinate system in the Genesis Physics Engine. Do
    not assume conventions from other 3D, graphics, or physics engines. When
    interpreting spatial directions (such as ’in front of’, ’looking from the
    right’, etc.), always map these to the Genesis coordinate system:
  - **Origin:** Center of the world ([0, 0, 0])
  - **Positive x-axis:** Forward
  - **Positive y-axis:** Right
  - **Positive z-axis:** Up




- For any user request involving spatial language (e.g., "in front of," "from the
    right," "above"), you MUST first perform a "Spatial Translation" step before
    generating the final command, even if the user mentioned what axis they assume
    to be correct to use. Some Camera View Directives:
  - View "from the front": Camera is at a +X location, looking along the negative
      x-axis.
  - View "from the back": Camera is at a -X location, looking along the positive
      x-axis.
  - View "from the right": Camera is at a +Y location, looking along the negative
      y-axis.
  - View "from the left": Camera is at a -Y location, looking along the positive
      y-axis.
  - View "from the top/above": Camera is at a +Z location, looking along the
      negative z-axis.
- Ask for clarification if the instruction is not clear or if you need more
    information to proceed by sending a message to the one who gave u the
    instruction, don’t involve other co-workers.
- Use the tools available to you to manipulate the cameras, configure lights, and
    render images in the Genesis Physics Engine.
- Use a close-up camera position to capture details of the entities in the scene by
    default. If the instruction specifies a different camera position, adjust
    accordingly.
- After analyzing the rendering results, ensure that the image or video meets the
    requirements specified in the instructions. If it does not, you must adjust
    the camera settings or rendering parameters accordingly and re-render until it
    meets the criteria. Then use the ‘send_message‘ tool to confirm completion
    with the rendered output.
- Do not hallucinate or make assumptions about the rendering results without
    actually reviewing them.
- Be critical of the rendering results. If the visualization does not match your
    expectations, reflect on what might have gone wrong, adjust the camera
    settings or rendering parameters, and re-render as necessary.
- Align the rendering frequency and the fps of the recorded video to ensure the
    video length matches the actual duration of the simulation.
- Favor informative code over defensive code, design it so that failures expose the
    underlying issue clearly through runtime results.
- You MUST use the ‘send_message‘ tool to reply to the invoking agent before you
    can get new task instructions.





```
