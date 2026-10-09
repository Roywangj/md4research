# MPMWorlds: Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics

> **中英文对照精读 / Bilingual close-reading**

| 项目 | 内容 |
|---|---|
| **标题** | MPMWorlds: Material-Point-Method Simulations for Inferring and Extrapolating Physical Dynamics |
| **中文题名** | MPMWorlds：用于推断与外推物理动力学的物质点法模拟 |
| **作者** | Žiga Kovačič，Kevin Ellis（Cornell University 康奈尔大学） |
| **来源** | arXiv:2606.01538v2 [cs.GR]，2026-06-11（Preprint 预印本） |
| **项目主页** | https://zzigak.github.io/mpmworlds/ |
| **论文类型** | 资源/数据集论文 + 实证分析（代码生成 VLM vs. 视频扩散 VDM 的对比研究） |
| **页数** | 16 页 |

---

## 目录 / Index

- [Abstract 摘要](#abstract-摘要)
- [1 Introduction 引言](#1-introduction-引言)
  - [1.1 Problem Definition 问题定义](#11-problem-definition-问题定义推断与外推物理动力学)
- [2 Related Works 相关工作](#2-related-works-相关工作)
- [3 MPMWorlds Dataset 数据集](#3-mpmworlds-dataset-数据集)
  - [3.1 Dataset Creation Pipeline 数据集构建流程](#31-dataset-creation-pipeline-数据集构建流程)
  - [3.2 Dataset Statistics 数据集统计](#32-dataset-statistics-数据集统计)
- [4 Experimental Setup and Evaluation 实验设置与评估](#4-experimental-setup-and-evaluation-实验设置与评估)
  - [4.1 Input Conditions 输入条件](#41-input-conditions-输入条件)
  - [4.2 Models 模型](#42-models-模型)
  - [4.3 Training and Inference 训练与推理](#43-training-and-inference-训练与推理)
  - [4.4 Evaluation Metrics 评估指标](#44-evaluation-metrics-评估指标)
- [5 Results and Analysis 结果与分析](#5-results-and-analysis-结果与分析)
- [6 Discussion 讨论](#6-discussion-讨论)
- [References 参考文献](#references-参考文献)
- [Appendix 附录](#appendix-附录)
- [术语表 / Terminology](#术语表--terminology)
- [阅读提示 / Critical reading notes](#阅读提示--critical-reading-notes)

---

## Abstract 摘要

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> To study the ability to infer physical dynamics from videos and extrapolate them forward in time, we assemble a dataset of 2D Material Point Method (MPM) physical simulations covering rich physical phenomena such as deformable objects, fluids, kinetic objects, and emitters. We study code generation and video diffusion approaches on this dataset, identifying their strengths and weaknesses by varying the amount of physically relevant side information. The code generation model, beyond giving a working demonstration of automatic synthesis of MPM simulations, reveals that such an approach struggles with inferring physical parameters from visual input, but relative to video diffusion, produces physically and temporally stable extrapolations forward in time, while the video diffusion model more strongly identifies geometric properties from visual input but produces physically implausible extrapolations. Project page: https://zzigak.github.io/mpmworlds/.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 为研究从视频中推断物理动力学并将其沿时间向前外推的能力，我们构建了一个二维物质点法（MPM）物理模拟数据集，涵盖可变形物体、流体、运动物体、发射体等丰富的物理现象。我们在该数据集上研究了代码生成（code generation）与视频扩散（video diffusion）两类方法，通过调节"物理相关旁路信息"的多少来识别它们各自的优势与不足。代码生成模型不仅给出了自动合成 MPM 模拟的可行示范，还揭示：该路线难以从视觉输入推断物理参数，但相对于视频扩散，它能产生**物理上与时间上更稳定**的前向外推；而视频扩散模型则更擅长从视觉输入识别**几何属性**，但产生的外推在物理上往往不可信。项目主页：https://zzigak.github.io/mpmworlds/。

---

## 1 Introduction 引言

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Physical simulation is used across robotics, science and engineering, videogames, cognitive science, and the arts. Up until recently, building a high-fidelity physical simulator handling rich physics, such as deformable objects, fluids, etc., meant painstaking programming using techniques such as Material Point Methods (MPM). But could generative models of source code dispense with the need to hand-program new simulations—and could generative models of videos further dispense with the need to have any simulation code at all? These questions are significant, because authoring precise simulation code is expensive and demands domain expertise, while generative video models might achieve much broader coverage of the everyday world than any symbolic simulation ever could.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 物理模拟广泛应用于机器人、科学与工程、电子游戏、认知科学以及艺术领域。直到不久前，构建一个能处理可变形物体、流体等丰富物理现象的高保真物理模拟器，仍意味着需借助物质点法（MPM）等技术进行费力的手工编程。但是：源代码的生成模型能否免去为新模拟手工编程的需要？而视频的生成模型能否进一步免去对任何模拟代码的需要？这些问题意义重大，因为编写精确的模拟代码代价高昂、且需要领域专长，而生成式视频模型也许能比任何符号化模拟覆盖更广阔的日常世界。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The ability to infer the physical dynamics of a scene, and successfully extrapolate to future time points, is also a fundamental test of physical reasoning. While the literature has investigated the ability of generative video models to extrapolate physics forward in time [Kang et al., 2024], such works center on simple rigid body dynamics, not the richer dynamics such as fluids, deformable objects, and various different materials.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 推断一个场景的物理动力学、并成功外推到未来时间点的能力，同时也是对物理推理的一项基本检验。尽管已有文献研究了生成式视频模型沿时间向前外推物理的能力 [Kang et al., 2024]，但这类工作以简单的刚体动力学为中心，而非流体、可变形物体以及各类不同材料等更丰富的动力学。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> To answer these questions, we assemble a new dataset, MPMWorld, of physical simulations covering rich dynamics such as fluids, materials such as snow and sand, deformable bodies, and more (Figure 1). We then study the conditions under which generative models of source code (specifically VLMs) can produce accurate simulation code, given partial information such as a history of past frames, or privileged information such as underlying physical parameters. We also study the conditions under which generative video models (specifically video diffusion models, 'VDMs') can render the output of the desired simulation, without ever explicitly constructing the underlying code.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 为回答这些问题，我们构建了一个新的物理模拟数据集 MPMWorlds，覆盖流体等丰富动力学、雪与沙等材料、可变形体等等（图 1）。随后我们研究：在给定部分信息（如过去帧的历史）或特权信息（如底层物理参数）的条件下，源代码的生成模型（具体为 VLM）何时能产生准确的模拟代码；同时也研究：在何种条件下，生成式视频模型（具体为视频扩散模型，"VDM"）能够直接渲染出所需模拟的输出，而无需显式构造底层代码。

### Fig. 1. MPMWorlds 数据集总览

![Fig. 1](fig1_dataset_overview.png)

**Caption:** Figure 1: MPMWorlds dataset overview. The dataset includes diverse materials and physical interactions. Each entry contains the simulator code, the scene configuration, and the resulting video.

**Caption[CN]:** 图 1：MPMWorlds 数据集总览。数据集包含多样的材料与物理交互。每条数据包含模拟器代码、场景配置（Scene Config）以及生成的模拟视频（Simulation Video）。

**Reading note:** 该图展示数据集涵盖的六大类现象——多材料交互、Drucker–Prager 沙、运动学物体与碰撞体、粒子发射体、网格模拟、单场景多物体；底部"SINGLE DATA ENTRY"说明每条数据由三元组（代码 + YAML 配置 + 渲染视频）构成，是全文方法对比的基础。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> We find both methods achieve only partial success. Code generation excels at consistent long-horizon dynamics, but struggles with geometry. Video diffusion excels at geometry but hallucinates dynamics and deteriorates over long time horizons. We probe the models to understand which elements of the simulations they struggle with, identifying specific classes of materials that are surprisingly challenging (or easy) for each approach.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 我们发现两种方法都只取得部分成功。代码生成擅长保持一致的长时程动力学，但在几何上表现欠佳；视频扩散擅长几何，却会幻想（hallucinate）出动力学并在长时程上逐渐劣化。我们对模型进行探查，以理解它们在模拟的哪些要素上遇到困难，并识别出对每种方法而言出人意料地困难（或容易）的特定材料类别。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> In total we contribute the following:
> 1. A dataset of 2D physical simulations covering fluids, deformable objects, rigid bodies, emitters, 'motorized' objects such as pinwheels and conveyor belts, and more. Each simulation includes both source code, scene configuration file, and an associated video of the simulation running.
> 2. Neural network models trained on this dataset. We train a variety of models which either generate physics simulation source code, or which generate raw frames, and which condition on a variety of information sources, such as past frames or privileged information such as the numerical values of physical parameters or initial positions.
> 3. The evaluative role of our dataset and models is to test learning-based methods for inferring physical dynamics, and extrapolating that inference forward in time. Our work analyzes which physical dynamics are challenging to reconstruct and extrapolate. But importantly the analysis offers constructive guidance for future work: By studying which forms of physically-relevant side information most improves the models, we hope to offer constructive guidance on what future modeling should focus on.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> 我们的贡献总体如下：
> 1. **一个二维物理模拟数据集**，涵盖流体、可变形物体、刚体、发射体，以及风车、传送带等"机动化"物体等等。每个模拟都同时包含源代码、场景配置文件，以及一段模拟运行的关联视频。
> 2. **在该数据集上训练的神经网络模型。** 我们训练了多种模型，它们或生成物理模拟源代码、或生成原始帧，并以多种信息源为条件，例如过去帧，或诸如物理参数数值、初始位置之类的特权信息。
> 3. **数据集与模型的评估作用**在于检验基于学习的方法在推断物理动力学、并将该推断沿时间向前外推方面的能力。我们的工作分析了哪些物理动力学难以重建与外推。但更重要的是，该分析为未来工作提供了建设性指引：通过研究哪种形式的物理相关旁路信息对模型提升最大，我们希望就未来建模应聚焦何处给出建设性建议。

### 1.1 Problem Definition 问题定义：推断与外推物理动力学

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Given partial information about the physical dynamics of a scene, such as a short video clip, we take inferring physical dynamics to mean the recovery (or reconstruction) of a forward simulation of that physical scene. These problems are practically relevant because extrapolations forward in time can serve as a world model for e.g. planning or intuitive physics purposes, and inferring the underlying program is valuable for engineers or artists wishing to work with the physics code. We consider a variety of partial information sources in part because end-users may wish to specify a physical simulation with more than just images or video, but also provide specific physical parameters, while keeping the rest unspecified.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 给定关于场景物理动力学的部分信息（例如一小段视频片段），我们把"推断物理动力学"定义为：恢复（或重建）该物理场景的一个前向模拟。这些问题具有实际意义，因为沿时间向前的外推可充当**世界模型**，服务于例如规划或直觉物理等目的；而推断底层程序对于希望操作物理代码的工程师或艺术家很有价值。我们考虑多种部分信息源，部分原因在于：终端用户也许希望用不止图像或视频来指定一个物理模拟，还可提供特定物理参数，同时其余部分保持不指定。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The recovered physical simulation could be represented explicitly as source code, or it could be implicitly represented as neural activations, but in either case, it should support extrapolation to future time points, meaning that we can predict what the scene will look like at any point in the future.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 恢复出的物理模拟既可以显式地表示为源代码，也可以隐式地表示为神经激活；但无论哪种情形，它都应支持向未来时间点的外推，即我们能够预测场景在未来任意时刻的样子。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> We consider scenes generated by physics simulation programs. We write $\rho$ for one such program; different programs simulate different scenes with different objects, materials, etc. A program $\rho$ produces a video $v$ comprising a sequence of frames. Given a prefix of $v$ up to time $t$, written $v_{\le t}$, inferring the physical dynamics as a program means to recover a $\hat{\rho}$ equivalent to $\rho$. Extrapolating to future time points means predicting a video $\hat{v} = \hat{v}_{\le t} \,||\, \hat{v}_{>t}$ (given $v_{\le t}$).

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 我们考虑由物理模拟程序生成的场景。记 $\rho$ 为一个这样的程序；不同程序以不同的物体、材料等模拟不同的场景。程序 $\rho$ 产生由一系列帧组成的视频 $v$。给定 $v$ 截至时刻 $t$ 的前缀（记为 $v_{\le t}$），"以程序形式推断物理动力学"意味着恢复一个等价于 $\rho$ 的 $\hat{\rho}$；"外推到未来时间点"则意味着（在给定 $v_{\le t}$ 的条件下）预测视频 $\hat{v} = \hat{v}_{\le t} \,||\, \hat{v}_{>t}$。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Given the complexity of physical dynamics that we study, we do not expect inference and extrapolation to be easy. To understand why a model struggles with inference or extrapolation for a particular scene, we can provide physically-relevant side information, such as the positions of objects, their densities, etc. We extract different forms of side information from the underlying program, written $f(\rho)$. Models predict either a video or a program, i.e. estimate either $p(v \mid v_{\le t}, f(\rho))$ or $p(\rho \mid v_{\le t}, f(\rho))$. Figure 2 illustrates the two inference-and-extrapolation pipelines studied in this work: executable simulation synthesis via VLMs and direct pixel-space continuation via VDMs.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 鉴于我们所研究的物理动力学之复杂，我们并不期望推断与外推会很容易。为理解模型为何在某个特定场景上难以推断或外推，我们可提供物理相关的旁路信息，如物体的位置、密度等。我们从底层程序中抽取不同形式的旁路信息，记为 $f(\rho)$。模型预测视频或程序之一，即估计 $p(v \mid v_{\le t}, f(\rho))$ 或 $p(\rho \mid v_{\le t}, f(\rho))$。图 2 展示了本工作研究的两条推断—外推流水线：经由 VLM 的可执行模拟合成，以及经由 VDM 的直接像素空间续写。

### Fig. 2. 重建与外推流水线

![Fig. 2](fig2_pipelines.png)

**Caption:** Figure 2: Reconstruction and extrapolation pipelines. Models must predict a full video sequence ($\hat{v} = \hat{v}_{\le t} \,\|\, \hat{v}_{>t}$) from an initial observation ($v_{\le t}$). Top: The VLM synthesizes a simulation program that executes from $t=0$, explicitly reconstructing the input (blue) alongside the future extrapolation (pink). Bottom: The VDM operates in pixel space, using the input strictly as conditioning to generate future frames.

**Caption[CN]:** 图 2：重建与外推流水线。模型须从初始观测 $v_{\le t}$ 预测完整视频序列 $\hat{v} = \hat{v}_{\le t} \,\|\, \hat{v}_{>t}$。上：VLM 合成一个从 $t=0$ 开始执行的模拟程序，显式地重建输入（蓝色）并给出未来外推（粉色）。下：VDM 在像素空间运行，仅把输入用作条件来生成未来帧。

**Reading note:** 注意两条路线的本质差异：VLM 路线把"输入帧"也作为程序执行结果重新生成出来（reconstruction），因此重建质量可被度量并用于 Best-of-N 选择；VDM 路线把输入仅作 cached context 条件，外推时易出现像素崩坏（图右下马赛克示意）。

---

## 2 Related Works 相关工作

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **Intuitive Physics and Physical Reasoning.** Prior work studies physical reasoning as the ability to infer and predict physical dynamics from visual observations. Cognitive theories propose that human intuitive physics operates through approximate internal simulation [Ullman et al., 2017], while benchmarks such as Physion [Bear et al., 2021] and Physion++ [Tung et al., 2023] evaluate physical understanding in controlled environments. Learned relational and object-centric dynamics models include Interaction Networks [Battaglia et al., 2016], latent physical-property inference from videos [Wu et al., 2015, 2016], and program-like scene representations [Liu et al., 2019]. Our work instead studies whether modern generative models can recover executable or implicit forward models of complex physical scenes.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **直觉物理与物理推理。** 既有工作把物理推理研究为"从视觉观测推断并预测物理动力学"的能力。认知理论认为人类直觉物理通过近似的内部模拟运作 [Ullman et al., 2017]，而 Physion [Bear et al., 2021]、Physion++ [Tung et al., 2023] 等基准在受控环境中评估物理理解。基于学习的关系型与以物体为中心的动力学模型包括交互网络（Interaction Networks）[Battaglia et al., 2016]、从视频推断潜在物理属性 [Wu et al., 2015, 2016]，以及类程序的场景表示 [Liu et al., 2019]。与之不同，我们的工作研究现代生成模型能否恢复复杂物理场景的**可执行或隐式前向模型**。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Programmatic Physical Reasoning and Simulation Code Generation.** Recent work explores executable or symbolic representations for physical reasoning. Scene2Prog [Liu et al., 2019] infers programmatic structure from visual scenes, VisPhyWorld [Liang et al., 2026] studies code-driven physical reconstruction, and PhysCodeBench [Xie et al., 2026] evaluates LLM-based physics simulation synthesis. Our setting instead couples executable MPM programs with rendered rollouts and structured scene configurations, enabling controlled comparison between code-space and pixel-space prediction for deformable multi-material dynamics.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **程序化物理推理与模拟代码生成。** 近期工作探索面向物理推理的可执行或符号化表示。Scene2Prog [Liu et al., 2019] 从视觉场景推断程序化结构，VisPhyWorld [Liang et al., 2026] 研究代码驱动的物理重建，PhysCodeBench [Xie et al., 2026] 评估基于 LLM 的物理模拟合成。我们的设定则把**可执行 MPM 程序**与渲染轨迹（rollouts）及结构化场景配置耦合在一起，从而能够对可变形多材料动力学开展代码空间与像素空间预测之间的受控对比。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Video Generation Models as World Models.** Recent work increasingly views generative video models as implicit world models [Ha and Schmidhuber, 2018, Bruce et al., 2024]. Several benchmarks evaluate physical plausibility in generated videos, including VideoPhy [Bansal et al., 2024, 2025], LikePhys [Yuan et al., 2025], PhyWorldBench [Gu et al., 2025], and analyses of physical-law consistency in video generation [Kang et al., 2024]. Unlike prior work focused primarily on perceptual plausibility or short-horizon events [Qiu et al., 2025, Meng et al., 2024], our setting studies long-horizon continuation of deformable multi-material dynamics with paired executable simulations and structured scene representations.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **作为世界模型的视频生成模型。** 近期工作越来越多地把生成式视频模型视为隐式世界模型 [Ha and Schmidhuber, 2018, Bruce et al., 2024]。多个基准评估生成视频的物理可信度，包括 VideoPhy [Bansal et al., 2024, 2025]、LikePhys [Yuan et al., 2025]、PhyWorldBench [Gu et al., 2025]，以及对视频生成中物理定律一致性的分析 [Kang et al., 2024]。与主要聚焦感知可信度或短时程事件的既有工作 [Qiu et al., 2025, Meng et al., 2024] 不同，我们的设定研究可变形多材料动力学的**长时程续写**，并配有成对的可执行模拟与结构化场景表示。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Physical Reasoning Benchmarks.** Prior benchmarks evaluate physical reasoning through mechanics puzzles, causal reasoning, and interactive simulation, including PHYRE [Bakhtin et al., 2019], CLEVRER [Yi et al., 2020], Physion [Bear et al., 2021], Physion++ [Tung et al., 2023], and I-PHYRE [Li et al., 2024]. PHYBench [Qiu et al., 2025] studies formal physics reasoning in language models. In contrast, our dataset evaluates generative physical continuation, where models must extrapolate future dynamics either through executable simulation synthesis or direct video generation.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **物理推理基准。** 既有基准通过力学谜题、因果推理与交互式模拟来评估物理推理，包括 PHYRE [Bakhtin et al., 2019]、CLEVRER [Yi et al., 2020]、Physion [Bear et al., 2021]、Physion++ [Tung et al., 2023] 与 I-PHYRE [Li et al., 2024]。PHYBench [Qiu et al., 2025] 研究语言模型中的形式化物理推理。相比之下，我们的数据集评估**生成式物理续写**——模型须通过可执行模拟合成或直接视频生成来外推未来动力学。

---

## 3 MPMWorlds Dataset 数据集

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> To study physical dynamics inference and extrapolation, we introduce MPMWorlds, a simulation-based dataset of physical scenes. Each instance includes (i) executable simulation code, (ii) a structured configuration specifying the scene, and (iii) a rendered video of the resulting dynamics. The scene configuration specifies object types, materials, geometry, initial conditions, and appearance, while the simulation code implements the corresponding physical process. This paired representation enables controlled study of dynamics extrapolation, physical state inference, sensitivity to input modalities, and the role of explicit intermediate representations such as code.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 为研究物理动力学的推断与外推，我们提出 MPMWorlds——一个基于模拟的物理场景数据集。每个实例包含：(i) 可执行模拟代码；(ii) 一份指定场景的结构化配置；(iii) 一段所得动力学的渲染视频。场景配置指定物体类型、材料、几何、初始条件与外观，而模拟代码实现相应的物理过程。这种成对表示使得我们可以受控地研究动力学外推、物理状态推断、对输入模态的敏感性，以及代码这类显式中间表示的作用。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Each configuration is a structured YAML file containing object entries with fields for object type, geometry, material model, initial state, appearance, and optional kinematic or emitter behavior. For example, a dynamic body specifies its shape, color, constitutive model, material parameters, and initial position and velocity; emitters specify spawn region, material, and emission rate.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 每份配置是一个结构化 YAML 文件，包含若干物体条目，字段涵盖物体类型、几何、材料模型、初始状态、外观，以及可选的运动学（kinematic）或发射体（emitter）行为。例如，一个动态体会指定其形状、颜色、本构模型（constitutive model）、材料参数以及初始位置与速度；发射体则指定生成区域、材料与发射速率。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Dataset Characteristics.** We implement the simulations in 2D using the Material Point Method (MPM), rendering videos at 512 × 512 resolution and 30 FPS for 10 seconds. All simulations are written in Taichi, with each program explicitly defining the MPM state update, scene initialization, physical parameters, and time-stepping loop, without relying on high-level simulation APIs.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **数据集特性。** 我们使用物质点法（MPM）以二维实现这些模拟，以 512 × 512 分辨率、30 FPS、时长 10 秒渲染视频。所有模拟均用 Taichi 编写，每个程序显式定义 MPM 状态更新、场景初始化、物理参数与时间步进循环，而不依赖高层模拟 API。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> We use MPM due to its stability and its ability to model a wide range of materials and interactions within a unified framework. It is also widely adopted across computer graphics, visual effects, and engineering communities, making it a practical and well-established choice for simulating diverse physical phenomena. The dataset includes diverse dynamic scenes with deformable and multi-material interactions, including liquids, elastic (particle-based and FEM-based), plastic, snow, sand (including wet interactions), viscoplastic and viscoelastic materials, as well as rigid and kinematic objects. We also include emitters that continuously introduce material into the scene (e.g., fountains or rain). All scenes are rendered on a high-contrast background to minimize confounding visual factors such as texture or lighting.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 我们选用 MPM 是因为它稳定，且能在统一框架内对大范围材料与交互建模。它在计算机图形学、视觉特效与工程界也被广泛采用，是模拟多样物理现象的实用且成熟的选择。数据集包含多样的、带可变形与多材料交互的动态场景，涵盖液体、弹性（基于粒子与基于 FEM 两种）、塑性、雪、沙（含湿态交互）、黏塑性与黏弹性材料，以及刚性与运动学物体。我们还加入了向场景中持续注入材料的发射体（如喷泉或降雨）。所有场景均在高对比度背景上渲染，以最大程度减少纹理或光照等混淆性视觉因素。

### 3.1 Dataset Creation Pipeline 数据集构建流程

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> The dataset is generated using a partially synthetic pipeline combining human-written programs, LLM-based synthetic generation, and data augmentation through small perturbations. It is created entirely from scratch and does not rely on existing datasets or sources. The dataset generation pipeline has a hierarchical structure and we explain the steps below:

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 数据集由一条部分合成的流水线生成，结合了人工编写的程序、基于 LLM 的合成生成，以及通过小幅扰动进行的数据增强。它完全从零创建，不依赖任何既有数据集或来源。数据集生成流水线具有层级结构，各步骤说明如下：

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Step 1: Seed Simulations.** We manually write 35 diverse "seed" simulations with varying object layouts, materials, geometries, initial velocities, kinematic elements (e.g., pistons, gates, rotating objects), and rigid colliders. Simulations are paired with a structured scene YAML config.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **第 1 步：种子模拟。** 我们手工编写 35 个多样的"种子"模拟，具有不同的物体布局、材料、几何、初始速度、运动学元素（如活塞、闸门、旋转物体）与刚性碰撞体。每个模拟都配有一份结构化的场景 YAML 配置。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Step 2: Base Simulation Generation and Validation.** We expand the dataset in the style of Self-Instruct [Wang et al., 2023] by prompting large language models (ChatGPT o3 and Gemini 2.5 Pro) with 2–3 seed examples to generate new simulation programs and corresponding scene configurations, by combining and extending the provided human written code. Generated simulations are executed and filtered using automated checks for runtime failures, trivial outputs, and severe numerical instability. We additionally validate consistency between generated programs and configuration files using an LLM-based verification pass checking object counts, materials, and initial conditions, with flagged failures manually inspected. This process yields approximately 1k valid Parent simulations.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **第 2 步：基础模拟生成与验证。** 我们以 Self-Instruct [Wang et al., 2023] 的方式扩充数据集：用 2–3 个种子样例提示大语言模型（ChatGPT o3 与 Gemini 2.5 Pro），通过组合与扩展所提供的人工代码来生成新的模拟程序及相应场景配置。生成的模拟会被执行，并以自动检查（针对运行时失败、平凡输出与严重数值不稳定）进行过滤。我们还用一个基于 LLM 的验证环节来核验生成程序与配置文件之间的一致性，检查物体数量、材料与初始条件，对被标记的失败进行人工复检。该过程产出约 1k 个有效的 **Parent（父）模拟**。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> We further expand the dataset by prompting the LLM to modify previously generated scenes through changes such as adding or removing objects, altering materials or geometries, and modifying interactions, resulting in approximately 9k Child simulations. Together, the Parent and Child simulations constitute the core 10k Scene Templates that define the unique physical setups in our dataset.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 我们进一步扩充数据集：提示 LLM 修改先前生成的场景，如增删物体、改变材料或几何、修改交互方式，由此得到约 9k 个 **Child（子）模拟**。父模拟与子模拟共同构成核心的约 **10k 个 Scene Templates（场景模板）**，定义了数据集中各个独特的物理设置。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Step 3: Automated Perturbations.** We augment the dataset by perturbing numerical parameters, e.g. object positions, subject to spatial constraints that avoid invalid layouts, such as overlapping objects or objects outside the domain. This reduces bias from LLM-chosen initial configurations, introduces variability in initial conditions, and aids generalization.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **第 3 步：自动扰动。** 我们通过扰动数值参数（如物体位置）来增强数据集，并施加空间约束以避免无效布局（如物体重叠或越出域外）。这降低了来自 LLM 所选初始配置的偏差，引入了初始条件的多样性，并有助于泛化。

### 3.2 Dataset Statistics 数据集统计

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> MPMWorlds contains 95,805 rendered simulations, including 9,204 Scene Templates (comprising the full set of Parent and Child simulations) and associated perturbations. Base scenes define the physical setup, while perturbations vary numerical parameters.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> MPMWorlds 包含 95,805 个渲染模拟，其中含 9,204 个场景模板（即父、子模拟的全集）及相应扰动。基础场景定义物理设置，而扰动则改变数值参数。

### Fig. 3. MPMWorlds 数据集统计

![Fig. 3](fig3_statistics.png)

**Caption:** Figure 3: Dataset statistics for MPMWorlds across base scenes. (a) Distribution of number of object per scene. (b) Distribution of dynamic-body material types across the dataset. (c) Distribution of object types illustrating the diversity of interaction mechanisms present in the dataset.

**Caption[CN]:** 图 3：MPMWorlds 在基础场景上的数据集统计。(a) 每场景物体数量的分布。(b) 数据集中动态体材料类型的分布。(c) 物体类型的分布，展示数据集所含交互机制的多样性。

**Reading note:** (a) 每场景物体数中位数为 3；(b) 动态体材料以液体（34.5%）、弹性（32.7%）、雪（24.2%）为主，黏塑性（5.5%）与沙（3.0%）较少——这解释了为何后文 VLM 在"沙"上最吃力（沙样本最稀少且本构最难）；(c) 物体类型以动态体（41%）为主，另有静态/运动学碰撞体与发射体。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Figure 3 summarizes dataset statistics. Scenes have a median of 3 objects and mean of 2.9 objects, with a tail of more complex interactions involving dynamic bodies, colliders, and emitters. The dataset spans multiple classes of physical materials, including liquids, elastic materials, snow, viscoplastic materials, and sand; liquids and elastic materials are most common, followed by snow, while sand and viscoplastic materials provide additional deformation regimes. Overall, 22.5% of scenes contain at least two distinct material types, and 5.3% contain three or more.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 图 3 总结了数据集统计。场景物体数中位数为 3、均值为 2.9，并带有一条涉及动态体、碰撞体与发射体的更复杂交互的长尾。数据集跨越多类物理材料，包括液体、弹性材料、雪、黏塑性材料与沙；液体与弹性材料最常见，其次是雪，而沙与黏塑性材料提供了额外的形变机制。总体上，22.5% 的场景至少含两种不同材料类型，5.3% 含三种或更多。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Object types include dynamic deformable bodies, static colliders, kinematic colliders, and emitters, enabling interactions such as moving boundaries, externally driven motion, and continuous material injection, substantially increasing the diversity and difficulty of long-horizon dynamics prediction.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 物体类型包括动态可变形体、静态碰撞体、运动学碰撞体与发射体，可实现移动边界、外部驱动运动与持续材料注入等交互，从而大幅提升长时程动力学预测的多样性与难度。

---

## 4 Experimental Setup and Evaluation 实验设置与评估

### 4.1 Input Conditions 输入条件

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We evaluate each model under different input regimes designed to identify which physical properties prove difficult to infer from visual observations alone and if one type of information is much easier to infer from visual information for one approach (VLM or VDM) than the other.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们在不同输入条件（regimes）下评估每个模型，旨在识别：哪些物理属性难以仅从视觉观测推断；以及对某一方法（VLM 或 VDM）而言，是否某类信息比另一方法更容易从视觉信息中推断出来。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Frames Only.** Models input only a video prefix of approximately 2.5 seconds ($v_{\le t}$, where $t = 2.5\,\text{sec}$). This is the minimal-information or vision-only setting, so the models have to infer all the information from vision.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **仅帧（Frames Only）。** 模型仅输入约 2.5 秒的视频前缀（$v_{\le t}$，其中 $t = 2.5$ 秒）。这是最小信息（仅视觉）设置，模型必须从视觉推断全部信息。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Full Configuration.** Models receive the video prefix $v_{\le t}$ together with the complete scene configuration, including object positions, material types, geometry, initial conditions, and physical parameters. This is the maximal-information setting: $f(\rho)$ gives the whole YAML file.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **完整配置（Full Configuration）。** 模型接收视频前缀 $v_{\le t}$ 以及完整场景配置，包括物体位置、材料类型、几何、初始条件与物理参数。这是最大信息设置：$f(\rho)$ 给出整份 YAML 文件。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **No Materials.** Models receive the video prefix $v_{\le t}$ and the scene configuration with material identities and material-specific parameters removed. This tests inference of material properties from visual evidence alone. Here $f(\rho)$ returns the YAML but with material properties removed.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **无材料（No Materials）。** 模型接收视频前缀 $v_{\le t}$ 与一份移除了材料身份及材料特定参数的场景配置。这检验仅凭视觉证据推断材料属性的能力。此处 $f(\rho)$ 返回移除材料属性后的 YAML。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **No Positions.** Models receive the video prefix $v_{\le t}$ and the scene configuration with explicit positional information removed. This tests whether models can infer object layout and initial state from the observed frames. Here $f(\rho)$ returns the YAML but with initial positions removed.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **无位置（No Positions）。** 模型接收视频前缀 $v_{\le t}$ 与一份移除了显式位置信息的场景配置。这检验模型能否从观测帧推断物体布局与初始状态。此处 $f(\rho)$ 返回移除初始位置后的 YAML。

### 4.2 Models 模型

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We compare two types of models, a code generation model (VLM) which produces executable simulation code against a video diffusion model (VDM) that directly predicts future frames.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们对比两类模型：产生可执行模拟代码的代码生成模型（VLM），与直接预测未来帧的视频扩散模型（VDM）。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Vision-Language Models.** VLMs predict future dynamics indirectly by generating executable MPM simulation code. Given prefix frames and optional configuration information, the VLM outputs a full Python (Taichi) simulation program $\hat{\rho}$, which when executed predicts video $\hat{v}$.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **视觉-语言模型（VLM）。** VLM 通过生成可执行的 MPM 模拟代码来间接预测未来动力学。给定前缀帧与可选的配置信息，VLM 输出一个完整的 Python（Taichi）模拟程序 $\hat{\rho}$，其执行后即预测出视频 $\hat{v}$。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> We use Qwen2.5-VL-7B-Instruct as the base VLM. At inference time, the model receives sampled frames from the prefix, optional side information, and a lightweight program scaffold containing only boilerplate imports and function signatures. The scaffold fixes non-semantic code structure, such as function names and ordering, while the model generates the simulation logic, object initialization, material parameters, and update rules. This focuses learning on the physically meaningful parts of the program rather than arbitrary formatting choices.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 我们采用 **Qwen2.5-VL-7B-Instruct** 作为基础 VLM。推理时，模型接收来自前缀的采样帧、可选旁路信息，以及一个轻量级程序脚手架（scaffold），其中仅含样板导入与函数签名。脚手架固定了非语义的代码结构（如函数名与排序），而由模型生成模拟逻辑、物体初始化、材料参数与更新规则。这使学习聚焦于程序中物理上有意义的部分，而非任意的格式选择。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Video Diffusion Models.** VDMs predict future dynamics directly in pixel space without constructing an explicit physical representation. We use the 14B LongCat video continuation model as our diffusion baseline. The model is conditioned on the observed video prefix and, when available, the same textual scene information used for the VLM input regimes.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **视频扩散模型（VDM）。** VDM 直接在像素空间预测未来动力学，而不构造显式的物理表示。我们采用 **14B 的 LongCat 视频续写模型**作为扩散基线。该模型以观测到的视频前缀为条件，并在可用时使用与 VLM 输入条件相同的文本场景信息。

### 4.3 Training and Inference 训练与推理

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For all experiments, we construct a 10k-example subset of the dataset with increased sampling weight on base scenes. We evaluate two held-out regimes enabled by the hierarchical dataset structure. The primary test split is partitioned at the Parent simulation level: all modifications (Children) and perturbations derived from a held-out base simulation are assigned to test, so models never observe the underlying scene template during training. This evaluates generalization to entirely novel physical scenes.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 所有实验均构建一个 10k 样例的数据集子集，并对基础场景增大采样权重。借助数据集的层级结构，我们评估两种留出（held-out）方案。主测试划分在 **Parent 模拟层级**进行：来自某个留出基础模拟的所有修改（Children）与扰动都被分配到测试集，因此模型在训练时从未观察到底层场景模板。这评估对**全新物理场景**的泛化能力。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> We additionally construct a modification validation split by withholding some modified descendants of training base scenes. This split intentionally preserves partial template overlap while changing object layouts, materials, etc., providing an intermediate regime between exact memorization and fully novel scene generalization.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 我们另外构建一个**修改验证划分（modification validation split）**：留出训练基础场景的一些修改后代。该划分有意保留部分模板重叠，同时改变物体布局、材料等，从而提供介于"精确记忆"与"完全新场景泛化"之间的中间方案。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> To improve training and inference efficiency, videos are resized to 256×256 resolution at 15 FPS. For VLM training, we use full supervised finetuning. For VDMs, we observed little difference between full finetuning and LoRA adaptation and therefore use LoRA for all diffusion experiments.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 为提升训练与推理效率，视频被缩放至 256×256 分辨率、15 FPS。VLM 训练采用**全量监督微调**；对 VDM，我们观察到全量微调与 LoRA 适配差异甚微，故所有扩散实验均使用 **LoRA**。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> At inference time, we generate multiple candidate programs from the VLM and select among them using evaluation metrics computed on the predicted $\hat{v}_{\le t}$. Specifically, we sample 15 candidate programs per test example. In contrast, we observe relatively low diversity across diffusion samples under different random seeds and therefore draw a single sample from the VDM. We use 50 denoising steps for diffusion inference, which empirically worked well and which calibrates the inference time compute budget of the two models: 50 denoising steps takes about as long as sampling 15 programs.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 推理时，我们从 VLM 生成多个候选程序，并用在预测前缀 $\hat{v}_{\le t}$ 上计算的评估指标在其中进行选择。具体地，每个测试样例采样 **15 个候选程序**。相比之下，我们观察到在不同随机种子下扩散样本的多样性相对较低，故对 VDM 仅抽取**单个样本**。扩散推理使用 **50 步去噪**，这在经验上效果良好，并校准了两模型的推理计算预算：50 步去噪所耗时间约等于采样 15 个程序。

### 4.4 Evaluation Metrics 评估指标

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Evaluating long-horizon physical rollouts requires metrics that capture not only pixel-level similarity, but also temporal consistency, motion fidelity, appearance preservation, and catastrophic physical failures such as collapse or disappearance.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 评估长时程物理轨迹所需的指标，不仅要刻画像素级相似度，还要刻画时间一致性、运动保真度、外观保持，以及坍缩或消失这类灾难性物理失败。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> Unlike classical simulation benchmarks, our setting does not provide direct access to particle trajectories or physical state during evaluation. Additionally, many scenes contain highly deformable materials whose shape and topology evolve over time, making standard tracking- or correspondence-based metrics ill-defined.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 与经典模拟基准不同，我们的设定在评估时无法直接访问粒子轨迹或物理状态。此外，许多场景含高度可变形材料，其形状与拓扑随时间演化，使得标准的基于跟踪或对应关系的指标难以良定义。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Prior work on physical video generation primarily evaluates visual plausibility using perceptual or VLM-judged metrics [Bansal et al., 2025, Yuan et al., 2025, Gu et al., 2025]. We evaluate five complementary aspects of physical continuation: spatial correspondence, appearance and material composition, motion fidelity, internal physical stability, and temporal coherence. Full details about the metrics are provided in Appendix B.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 既有的物理视频生成工作主要用感知或 VLM 评判的指标来评估视觉可信度 [Bansal et al., 2025, Yuan et al., 2025, Gu et al., 2025]。我们评估物理续写的五个互补方面：空间对应、外观与材料构成、运动保真度、内部物理稳定性、时间连贯性。指标的完整细节见附录 B。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> **Mask IoU (mIoU).** We measure spatial overlap between predicted and ground-truth foreground occupancy masks. For each frame, RGB images are thresholded into binary foreground masks and the Intersection-over-Union is computed frame-wise.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> **掩膜交并比（mIoU）。** 度量预测与真值前景占据掩膜之间的空间重叠。对每一帧，将 RGB 图像阈值化为二值前景掩膜，并逐帧计算交并比（Intersection-over-Union）。**（越高越好 ↑）**

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Object Collapse Score (OCS).** We measure prediction-internal temporal stability by checking whether foreground regions generated early in the predicted extrapolation remain visible over time. We compute this by segmenting initial object/material regions, tracking their color-consistent visible area across frames, and measuring the maximum relative area loss.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **物体坍缩分数（OCS）。** 通过检查在预测外推早期生成的前景区域是否随时间保持可见，来度量"预测内部的时间稳定性"。具体做法是：分割初始的物体/材料区域，跨帧跟踪其颜色一致的可见面积，并度量最大相对面积损失。**（越低越好 ↓）**

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> **Windowed Motion Activity Error (W-MAE).** We measure whether the prediction exhibits a similar amount of temporal activity as the ground-truth video, independent of exact spatial alignment. Motion activity is computed from frame-to-frame intensity changes aggregated over coarse spatial regions and temporally smoothed using a sliding window. W-MAE is the normalized difference between predicted and ground-truth activity magnitudes over time.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> **窗口化运动活跃度误差（W-MAE）。** 在不依赖精确空间对齐的前提下，度量预测是否呈现出与真值视频相近的时间活跃度。运动活跃度由逐帧强度变化在粗粒度空间区域上聚合、并用滑动窗口做时间平滑得到。W-MAE 是预测与真值活跃度幅值随时间的归一化差异。**（越低越好 ↓）**

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> **Color Total Variation (CTV).** To evaluate appearance and material-composition accuracy, we compare foreground color distributions between predicted and ground-truth rollouts. At each frame, foreground pixels are discretized into RGB histograms and compared using total variation distance.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> **颜色全变差（CTV）。** 为评估外观与材料构成的准确性，我们比较预测与真值轨迹的前景颜色分布。在每一帧，将前景像素离散化为 RGB 直方图，并用全变差距离（total variation distance）比较。**（越低越好 ↓）**

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> **Temporal Anomaly Rate (RTSJ).** We measure temporal coherence by detecting abrupt local appearance changes in predicted rollouts that exceed corresponding changes in the ground truth. We compute spatially aggregated temporal jump magnitudes from local color-histogram changes and flag a rollout as anomalous if its maximum excess jump exceeds a threshold. The reported anomaly rate is the fraction of test samples flagged as anomalous. Full details are provided in Appendix B.3.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> **时间异常率（RTSJ）。** 通过检测预测轨迹中超过真值相应变化的"局部外观骤变"来度量时间连贯性。我们由局部颜色直方图变化计算空间聚合的时间跳变幅值，若某轨迹的最大超额跳变超过阈值则标记其为异常。所报告的异常率是被标记为异常的测试样本比例。完整细节见附录 B.3。**（越低越好 ↓）**

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **Additional Metrics.** We additionally report standard pixel-level metrics including MSE and sliced Earth Mover's Distance (SEMD) in supplementary experiments. However, we do not use them as primary evaluation metrics because they correlate poorly with long-horizon physical consistency.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **附加指标。** 我们在补充实验中额外报告标准像素级指标，包括 MSE 与切片地动距离（sliced Earth Mover's Distance, SEMD）。但我们不将其作为主要评估指标，因为它们与长时程物理一致性的相关性较差。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> **Metrics enable Best-of-N sampling for program generation.** Because we sample multiple programs at test time, the VLM can benefit from Best-of-N sampling: Each program can be executed and its video compared to the ground truth prefix $v_{\le t}$ under the above metrics, with the best-scoring program being returned. Note that selection only reads the prefix $v_{\le t}$; the suffix $v_{>t}$ remains hidden from the learner at test time and is used solely to evaluate the selected program.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> **指标使程序生成可做 Best-of-N 采样。** 由于测试时采样多个程序，VLM 可受益于 Best-of-N 采样：每个程序均可执行，并在上述指标下将其视频与真值前缀 $v_{\le t}$ 比较，返回得分最高的程序。注意：选择过程**仅读取前缀 $v_{\le t}$**；后缀 $v_{>t}$ 在测试时对学习者保持隐藏，仅用于评估被选中的程序。

---

## 5 Results and Analysis 结果与分析

> <span style="color:#3B82F6"><strong>Para. 0:</strong></span> Unless otherwise stated, results are on the fully held-out test split.

> <span style="color:#F59E0B"><strong>Para. 0[CN]:</strong></span> 除非另有说明，结果均基于完全留出的测试划分。

### Fig. 4. VLM 与 VDM 外推的主结果对比（测试划分）

![Fig. 4](fig4_main_results.png)

**Caption:** Figure 4: Comparison of VLM- and VDM-based extrapolation across input conditions and evaluation metrics. Values are averaged over the held-out test split. Lower is better for W-MAE, CTV, anomaly rate, and object collapse, while higher is better for mIoU. The final column reports the mean normalized score across metrics for each model and input condition.

**Caption[CN]:** 图 4：在各输入条件与评估指标下，基于 VLM 与基于 VDM 的外推对比。数值在留出测试划分上平均。W-MAE、CTV、异常率与物体坍缩越低越好，mIoU 越高越好。最后一列报告每个模型与输入条件在各指标上的平均归一化得分。

**Reading note:** 颜色越深越好。关键对比：VLM 在 W-MAE、CTV、异常率、坍缩四项（时间稳定性）几乎全面优于 VDM；唯独 mIoU（几何重叠）VDM 始终更优。"Avg. Score"列显示完整配置下 VLM 0.86 vs VDM 0.48。

### Table 2. 测试留出集上各共享输入条件的视觉指标

![Table 2](table2_test_metrics.png)

**Caption:** Table 2: Visual metrics for shared input regimes across VLM and VDM on test holdout set (top-1 per metric, mean ± 1 SEM). Blue bold = best, red = worst per metric.

**Caption[CN]:** 表 2：测试留出集上 VLM 与 VDM 各共享输入条件的视觉指标（每指标取 top-1，均值 ± 1 个标准误 SEM）。蓝色加粗 = 该指标最优，红色 = 最差。

**Reading note:** 该表是图 4 的数值版，并额外给出 SEMD 与 MSE。可见有趣反差：在像素级指标 SEMD/MSE 上 VDM 反而更优（如 MSE VLM 0.027 vs VDM 0.019），印证了"像素级指标与长时程物理一致性相关性差"的论断。

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> **How do executable simulation models compare to direct video prediction?** Code generation and direct video prediction exhibit substantially different strengths and failure modes under long-horizon physical extrapolation task (Figure 4, Table 2). Code generation (w/ VLMs) generally outperforms direct video prediction (w/ VDMs) on most metrics and input conditions, particularly on temporal stability and long-horizon consistency. The largest differences appear in anomaly rate and object collapse, where executable simulations remain substantially more stable over time. Because generated programs are executed inside a physically grounded simulator, successful VLM generations typically preserve object persistence and temporal smoothness unless the predicted code itself becomes numerically unstable. In contrast, VDM predictions frequently exhibit hallucinated motion, disappearing regions, abrupt appearance changes, or temporally inconsistent dynamics, leading to significantly worse anomaly and collapse scores. Representative long-horizon failure cases are shown in Figure 6.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> **可执行模拟模型与直接视频预测相比如何？** 在长时程物理外推任务下，代码生成与直接视频预测展现出截然不同的优势与失败模式（图 4、表 2）。代码生成（VLM）在大多数指标与输入条件上总体优于直接视频预测（VDM），尤其在时间稳定性与长时程一致性上。最大差异出现在异常率与物体坍缩上，可执行模拟随时间显著更稳定。由于生成的程序在物理基础的模拟器内执行，成功的 VLM 生成通常能保持物体持久性与时间平滑性，除非预测代码本身变得数值不稳定。相比之下，VDM 预测频繁出现幻想运动、区域消失、外观骤变或时间不一致的动力学，导致异常与坍缩分数显著更差。代表性的长时程失败案例见图 6。

### Fig. 6. VDM 在长时程物理外推中的失败模式

![Fig. 6](fig6_vdm_failures.png)

**Caption:** Figure 6: VDM failure modes in long-horizon physical extrapolation. Left: In an elastoplastic scene, the VLM correctly maintains rigid object permanence and trajectory. The VDM suffers from object collapse, causing the bouncing block to fade and vanish during extrapolation. Right: Subjected to high-energy kinematic colliders, the VLM preserves complex fluid volume and splashing dynamics, whereas the VDM prediction fails to capture high frequency motion.

**Caption[CN]:** 图 6：VDM 在长时程物理外推中的失败模式。左：在弹塑性场景中，VLM 正确保持刚体的物体持久性与轨迹；VDM 出现物体坍缩，使弹跳方块在外推中淡出并消失。右：在高能运动学碰撞体作用下，VLM 保留了复杂的流体体积与飞溅动力学，而 VDM 预测未能捕捉高频运动。

**Reading note:** 红框标出 VDM 的崩坏帧。可对照阅读：左例对应"object collapse"（坍缩），右例对应"hallucinated/缺失的高频运动"。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> The main exception is mIoU, where VDMs consistently outperform VLMs across all input conditions. This suggests that diffusion models are comparatively better at preserving coarse spatial occupancy and approximate object placement directly from visual observations. However, these spatially plausible extrapolation often deteriorate temporally, producing physically inconsistent motion or unstable long-horizon behavior despite maintaining visually reasonable foreground overlap.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 主要例外是 mIoU：VDM 在所有输入条件下都一致优于 VLM。这表明扩散模型相对更擅长直接从视觉观测保持粗粒度空间占据与近似物体摆放。然而，这些在空间上看似合理的外推往往在时间上劣化，尽管维持了视觉上合理的前景重叠，却产生物理不一致的运动或不稳定的长时程行为。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **How sensitive are models to structured scene information?** Figure 4 shows that VLM performance is highly sensitive to the availability of structured scene information. Removing material or positional information substantially degrades performance, particularly for appearance fidelity (CTV) and motion consistency (W-MAE). In contrast, VDM performance changes comparatively little across input regimes, suggesting that current video diffusion models make limited use of additional structured physical information even when it is provided explicitly. Instead, they appear to rely primarily on short-term visual extrapolation.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **模型对结构化场景信息有多敏感？** 图 4 显示 VLM 性能对结构化场景信息的可得性高度敏感。移除材料或位置信息会显著降低性能，尤其在外观保真度（CTV）与运动一致性（W-MAE）上。相比之下，VDM 性能在各输入条件间变化相对很小，表明当前视频扩散模型即便被显式提供额外结构化物理信息也利用有限；相反，它们似乎主要依赖短期视觉外推。

### Fig. 5. 移除材料信息后的性能变化（按材料族分组）

![Fig. 5](fig5_remove_material.png)

**Caption:** Figure 5: Performance change after removing material information, grouped by material family.

**Caption[CN]:** 图 5：移除材料信息后的性能变化，按材料族分组。

**Reading note:** 纵轴为"移除材料信息时的指标变化(%)"。VLM（蓝）在 Elastic/Plastic（−16.5%）、Sand（−14.3%）、Snow（−9.0%）上明显变差，但 Liquid 几乎不受影响；VDM（红）反而普遍变好（+4.7%~+11.0%），说明文本材料信息对 VDM 近乎噪声。

> <span style="color:#3B82F6"><strong>Para. 4:</strong></span> Finally, both model families degrade substantially in the frames-only regime, indicating that long-horizon physical extrapolation remains difficult even when models observe several seconds of rollout history. However, the degradation is qualitatively different: VLM failures typically arise from incorrect physical implementation or unstable generated programs, whereas VDM failures are dominated by accumulated temporal drift, object instability, and incoherent motion over longer horizons. For additional qualitative results, see our project website and Appendix A.1.

> <span style="color:#F59E0B"><strong>Para. 4[CN]:</strong></span> 最后，两类模型在仅帧条件下都显著退化，表明即便模型观察到数秒的轨迹历史，长时程物理外推仍然困难。但退化在性质上不同：VLM 的失败通常源于错误的物理实现或不稳定的生成程序，而 VDM 的失败则主要表现为更长时程上累积的时间漂移、物体不稳定与不连贯运动。更多定性结果见项目网站与附录 A.1。

> <span style="color:#3B82F6"><strong>Para. 5:</strong></span> **Which materials are hardest to infer from visual information?** Figure 5 measures how performance changes when material information is removed from the structured prompt, relative to the full-configuration setting. For VLMs, removing material information has little effect on liquid scenes, but substantially degrades performance for elastic/plastic, snow, and sand scenes. This suggests that fluid-like behavior is either more readily inferred from the visual context or less sensitive to exact material parameters under our metrics, whereas coherent or history-dependent materials require more explicit material information.

> <span style="color:#F59E0B"><strong>Para. 5[CN]:</strong></span> **哪些材料最难从视觉信息推断？** 图 5 度量了相对于完整配置设置，从结构化提示中移除材料信息时性能如何变化。对 VLM，移除材料信息对液体场景影响甚微，却显著降低弹性/塑性、雪、沙场景的性能。这表明类流体行为要么更易从视觉上下文推断、要么在我们的指标下对精确材料参数不那么敏感，而连贯的或依赖历史的材料则需要更显式的材料信息。

> <span style="color:#3B82F6"><strong>Para. 6:</strong></span> In contrast, VDMs slightly improve when material information is removed across all material categories. This suggests that the VDM relies primarily on visual data and does not consistently benefit from textual material specifications. In some cases, additional structured material information may even act as noise for pixel-space extrapolation rather than improving physical consistency.

> <span style="color:#F59E0B"><strong>Para. 6[CN]:</strong></span> 相比之下，移除材料信息后 VDM 在所有材料类别上都略有提升。这表明 VDM 主要依赖视觉数据，并不能从文本材料规格中一致获益。在某些情况下，额外的结构化材料信息对像素空间外推甚至可能充当噪声，而非改善物理一致性。

> <span style="color:#3B82F6"><strong>Para. 7:</strong></span> **Which materials are most challenging for each model class?** Figure 7 aggregates normalized metric performance across tasks for each material family. VLM-based approaches perform strongest on liquid and snow scenes, but struggle substantially on sand dynamics. This is consistent with the fact that sand is implementation wise among the most difficult constitutive models in our dataset, following the approach introduced in [Klár et al., 2016]. Although Drucker–Prager sand is also an elastoplastic material [Li et al., 2026], we separate it from elastic/plastic object scenes because it exhibits qualitatively different dynamics: granular flow, frictional yielding, and loss of coherent object shape. In contrast, our elastic/plastic category primarily contains coherent deformable bodies whose identity and geometry persist over time.

> <span style="color:#F59E0B"><strong>Para. 7[CN]:</strong></span> **对每类模型而言哪些材料最具挑战？** 图 7 对每个材料族跨任务聚合归一化指标性能。基于 VLM 的方法在液体与雪场景上最强，但在沙的动力学上明显吃力。这与一个事实一致：沙在实现上是我们数据集中最难的本构模型之一，其方法沿用 [Klár et al., 2016]。尽管 Drucker–Prager 沙也是一种弹塑性材料 [Li et al., 2026]，我们仍将其与弹性/塑性物体场景分开，因为它呈现出性质不同的动力学：颗粒流、摩擦屈服与连贯物体形状的丧失。相比之下，我们的弹性/塑性类别主要含连贯的可变形体，其身份与几何随时间保持。

### Fig. 7. 按材料族的平均归一化性能（z 分数）

![Fig. 7](fig7_material_zscore.png)

**Caption:** Figure 7: Average normalized performance by material family. Zero denotes each model-family mean across materials.

**Caption[CN]:** 图 7：按材料族的平均归一化性能。零表示每类模型在各材料上的均值。

**Reading note:** 纵轴为平均性能 z 分数（越高越好，0=该模型族均值）。VLM（蓝）在 Snow（+0.61）、Liquid（+0.47）最强，在 Sand（−1.18）断崖式最弱；VDM（红）在 Elastic/Plastic（−0.29）最弱——两类模型的"软肋材料"恰好不同。

> <span style="color:#3B82F6"><strong>Para. 8:</strong></span> In contrast, VDMs perform comparatively poorly on elastic and plastic scenes. Inspection of these rollouts suggests that the main failure mode is maintaining coherent object trajectories over time. Many elastic scenes contain bouncing or highly dynamic bodies whose motion requires temporally precise geometry and velocity propagation. Video diffusion models frequently produce drift, disappearance, or temporally inconsistent motion in these settings. Liquids, while visually complex, are often easier for VDMs because approximate flow structure is sufficient to maintain plausible appearance, even when fine-grained dynamics are inaccurate.

> <span style="color:#F59E0B"><strong>Para. 8[CN]:</strong></span> 相比之下，VDM 在弹性与塑性场景上表现相对较差。检视这些轨迹可见，主要失败模式是难以随时间保持连贯的物体轨迹。许多弹性场景含弹跳或高度动态的物体，其运动需要时间上精确的几何与速度传播。视频扩散模型在此类设置中频繁产生漂移、消失或时间不一致的运动。液体虽视觉复杂，但对 VDM 往往更容易，因为近似的流动结构已足以维持可信外观，即便细粒度动力学并不准确。

> <span style="color:#3B82F6"><strong>Para. 9:</strong></span> **How do failure modes evolve over time?** Figure 8 shows the moving-average W-MAE across extrapolation frames, averaged over input conditions. The VDM's motion-activity error grows quickly after the prefix and remains consistently above the VLM curve, indicating that direct video prediction increasingly deviates from the ground-truth motion magnitude over time. The VLM also degrades with horizon, but more gradually, suggesting that executable simulation provides a more stable long-horizon dynamics prior.

> <span style="color:#F59E0B"><strong>Para. 9[CN]:</strong></span> **失败模式如何随时间演化？** 图 8 展示跨外推帧、在各输入条件上平均的滑动平均 W-MAE。VDM 的运动活跃度误差在前缀之后迅速增长，并持续高于 VLM 曲线，表明直接视频预测随时间越来越偏离真值运动幅值。VLM 也随时程退化，但更为渐进，表明可执行模拟提供了更稳定的长时程动力学先验。

### Fig. 8. 续写帧上的滑动平均 W-MAE

![Fig. 8](fig8_wmae_horizon.png)

**Caption:** Figure 8: Moving-average W-MAE over continuation frames. VDM motion error grows faster with prediction horizon than VLM error.

**Caption[CN]:** 图 8：续写帧上的滑动平均 W-MAE。VDM 的运动误差随预测时程比 VLM 增长更快。

**Reading note:** 两条曲线在约第 30 帧交叉：前期 VLM 误差略高（起步阶段），之后 VDM 误差迅速超越并持续高于 VLM，直观印证"VDM 越外推越崩"。

> <span style="color:#3B82F6"><strong>Para. 10:</strong></span> We observe a similar pattern for collapse failures. Figure 13 plots the cumulative fraction of samples that have collapsed by each extrapolation frame. VDM collapses occur early and continue accumulating throughout the rollout, reaching a substantially higher final collapse rate. In contrast, VLM rollouts exhibit far fewer collapses and mostly remain stable after the initial frames.

> <span style="color:#F59E0B"><strong>Para. 10[CN]:</strong></span> 对坍缩失败我们观察到类似模式。图 13 绘制了截至每个外推帧已坍缩样本的累积比例。VDM 坍缩发生得早，并在整个轨迹中持续累积，最终坍缩率明显更高。相比之下，VLM 轨迹的坍缩远更少，且在最初几帧之后大多保持稳定。

### Fig. 13. 外推帧上的累积坍缩率

![Fig. 13](fig13_collapse_rate.png)

**Caption:** Figure 13: Cumulative collapse rate over extrapolated frames. VDM rollouts collapse earlier and more often than VLM rollouts under the full-configuration setting.

**Caption[CN]:** 图 13：外推帧上的累积坍缩率。在完整配置设置下，VDM 轨迹比 VLM 轨迹坍缩更早、更频繁。

**Reading note:** F+T 指 Frames+Text（完整配置）。VDM 最终坍缩率约 0.19（19%），VLM 约 0.055（5.5%），差距约 3.5 倍。

> <span style="color:#3B82F6"><strong>Para. 11:</strong></span> **How well do models perform on modifications of previously observed scenes?** Figure 12 compares the fully held-out test split with the modification validation split, where models are evaluated on modified descendants of training scene families. Both model classes improve on the modification split, confirming that fully novel scene templates are harder than new variants of familiar scene structures.

> <span style="color:#F59E0B"><strong>Para. 11[CN]:</strong></span> **模型在"已见场景的修改版"上表现如何？** 图 12 对比完全留出测试划分与修改验证划分——后者在训练场景族的修改后代上评估模型。两类模型在修改划分上都有提升，证实"全新场景模板"比"熟悉场景结构的新变体"更难。

### Fig. 12. 修改测试划分上的 VLM/VDM 对比

![Fig. 12](fig12_modification_results.png)

**Caption:** Figure 12: Comparison of VLM- and VDM-based extrapolation across input conditions and evaluation metrics. Values are averaged over the modification test split. Lower is better for W-MAE, CTV, anomaly rate, and object collapse, while higher is better for mIoU. The final column reports the mean normalized score across metrics for each model and input condition.

**Caption[CN]:** 图 12：在各输入条件与评估指标下基于 VLM 与基于 VDM 的外推对比。数值在修改测试划分上平均。W-MAE、CTV、异常率与物体坍缩越低越好，mIoU 越高越好。最后一列报告平均归一化得分。

**Reading note:** 与图 4（全新测试集）对照阅读：完整配置下 VLM 的 Avg. Score 从 0.86 升至 0.91，提升幅度大于 VDM（0.48→0.39 实际略降），印证"VLM 更能从熟悉的交互结构获益"。

### Table 3. 修改验证集上各共享输入条件的视觉指标

![Table 3](table3_mod_metrics.png)

**Caption:** Table 3: Visual metrics for shared input regimes across VLM and VDM on modification validation set (top-1 per metric, mean ± 1 SEM). Blue bold = best, red = worst per metric.

**Caption[CN]:** 表 3：修改验证集上 VLM 与 VDM 各共享输入条件的视觉指标（每指标取 top-1，均值 ± 1 个 SEM）。蓝色加粗 = 最优，红色 = 最差。

> <span style="color:#3B82F6"><strong>Para. 12:</strong></span> The improvement is larger for VLMs, which gain across nearly all metrics and input regimes, especially in motion fidelity and temporal stability. VDMs also improve, but collapse and anomaly rates remain high, while mIoU remains their strongest metric. Thus, the VLM–VDM gap is not explained solely by memorization or scene novelty, suggesting that executable simulation generation benefits from familiar interaction structure, whereas pixel-space prediction remains better at geometric overlap but weaker at long-horizon dynamics. Figure 9 highlights these contrasting failure modes:

> <span style="color:#F59E0B"><strong>Para. 12[CN]:</strong></span> 提升幅度对 VLM 更大，它在几乎所有指标与输入条件上都有增益，尤其在运动保真度与时间稳定性上。VDM 也有提升，但坍缩率与异常率仍高，而 mIoU 仍是其最强指标。因此，VLM–VDM 的差距不能仅用记忆或场景新颖性解释，这表明可执行模拟生成受益于熟悉的交互结构，而像素空间预测在几何重叠上仍更优、在长时程动力学上仍更弱。图 9 突显了这些对比性的失败模式：

### Fig. 9. VLM 对空间输入的敏感性与组合扩展

![Fig. 9](fig9_vlm_spatial.png)

**Caption:** Figure 9: VLM sensitivity to spatial inputs and compositional scaling. Left: When explicit positional coordinates are withheld, the VLM struggles with visual state estimation, hallucinating an incorrect obstacle layout (red boxes) that alters the physical trajectory. The VDM, relying directly on pixels, preserves the geometry. Right: When provided with full configurations, the VLM scales seamlessly to compositional extremes (simultaneous liquid, elastic, and granular materials interacting with kinematic colliders). In contrast, the VDM suffers a catastrophic compositional breakdown, merging distinct materials into a single static average.

**Caption[CN]:** 图 9：VLM 对空间输入的敏感性与组合扩展。左：当显式位置坐标被留空时，VLM 在视觉状态估计上吃力，幻想出错误的障碍布局（红框），改变了物理轨迹；而直接依赖像素的 VDM 则保留了几何。右：当提供完整配置时，VLM 能无缝扩展到组合极端情形（液体、弹性与颗粒材料同时与运动学碰撞体交互）；相比之下，VDM 出现灾难性的组合崩溃，将不同材料合并成单一静态平均。

**Reading note:** 这是全文最能说明"两模型互补"的图：左例 VDM 赢（几何保持），右例 VLM 赢（多材料组合）。红框标注各自的幻想/崩坏处。

> <span style="color:#3B82F6"><strong>Para. 13:</strong></span> VLMs struggle with visual state estimation when positional information is removed, while VDMs fail under compositional multi-material interactions despite preserving coarse geometry.

> <span style="color:#F59E0B"><strong>Para. 13[CN]:</strong></span> 当位置信息被移除时，VLM 在视觉状态估计上吃力；而 VDM 尽管保留了粗粒度几何，却在组合式多材料交互下失败。

> <span style="color:#3B82F6"><strong>Para. 14:</strong></span> **Can prefix quality predict extrapolation quality?** The VLM and VDM exhibit complementary strengths: VLM continuations are typically more physically consistent, while VDM continuations are often geometrically smoother. This motivates a simple question: can observable prefix quality predict which extrapolation to trust?

> <span style="color:#F59E0B"><strong>Para. 14[CN]:</strong></span> **前缀质量能否预测外推质量？** VLM 与 VDM 展现出互补优势：VLM 的续写通常物理上更一致，而 VDM 的续写常在几何上更平滑。这引出一个简单问题：可观测的前缀质量能否预测应当信任哪一个外推？

> <span style="color:#3B82F6"><strong>Para. 15:</strong></span> We test a lightweight prefix-quality gate. For each example, we evaluate how well the VLM reconstructs the visible prefix and use a learned threshold to decide whether to keep the VLM extrapolation or fall back to the VDM prediction. Full details are provided in Appendix D.

> <span style="color:#F59E0B"><strong>Para. 15[CN]:</strong></span> 我们测试了一个轻量级的前缀质量门控（prefix-quality gate）。对每个样例，我们评估 VLM 重建可见前缀的好坏，并用一个学习到的阈值来决定保留 VLM 外推还是回退到 VDM 预测。完整细节见附录 D。

> <span style="color:#3B82F6"><strong>Para. 16:</strong></span> Table 1 shows that this routing strategy consistently improves over either model alone, particularly for temporal and stability metrics such as W-MAE, anomaly rate, collapse score, and CTV, where the gate routes most samples to the VLM. In contrast, mIoU predominantly routes to the VDM, reflecting its stronger geometric consistency. Overall, these results suggest that prefix reconstruction quality is predictive of long-horizon extrapolation quality and that the two model classes capture complementary aspects of physical extrapolation.

> <span style="color:#F59E0B"><strong>Para. 16[CN]:</strong></span> 表 1 显示，这一路由策略一致地优于任一单独模型，尤其在 W-MAE、异常率、坍缩分数与 CTV 等时间与稳定性指标上——门控将大多数样本路由到 VLM。相比之下，mIoU 主要被路由到 VDM，反映其更强的几何一致性。总体而言，这些结果表明前缀重建质量可预测长时程外推质量，且两类模型捕捉了物理外推的互补方面。

### Table 1. VLM vs VDM vs 阈值门控（top-1，测试集）

![Table 1](table1_gate.png)

**Caption:** Table 1: VLM vs VDM vs Threshold Gate (top-1) on the test set. Blue = best, red = worst per metric. X% of time the VLM output is selected by the gate.

**Caption[CN]:** 表 1：测试集上 VLM vs VDM vs 阈值门控（top-1）。蓝色 = 该指标最优，红色 = 最差。"X% LM"表示门控有 X% 的概率选择 VLM 输出。

**Reading note:** GATE 列几乎在所有时间/稳定性指标上都优于两个单模型（如完整配置 Anom. 0.371/0.862→0.001）。注意右侧小字百分比：稳定性指标几乎 80–100% 选 VLM，而 mIoU 仅 0–23% 选 VLM（即主要交给 VDM），完美体现互补路由。

---

## 6 Discussion 讨论

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We introduce a new dataset of physical simulations which help understand the strengths and weaknesses of code generation and video diffusion for physical inference and extrapolation. Despite being limited to 2D physics, the simulations prove challenging for current approaches, owing to the rich variety of physical materials and their interactions instantiated in the data. By feeding privileged information to the models we obtain insight on how to move forward: VLMs benefit strongly from explicit scene information, suggesting they struggle to recover materials, positions, and parameters from vision alone.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们提出了一个新的物理模拟数据集，有助于理解代码生成与视频扩散在物理推断与外推上的优势与不足。尽管局限于二维物理，这些模拟对当前方法仍颇具挑战，原因在于数据中实例化了丰富多样的物理材料及其交互。通过向模型喂入特权信息，我们获得了关于如何前进的洞见：VLM 强烈受益于显式场景信息，这表明它们难以仅凭视觉恢复材料、位置与参数。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> **Toward Hybrid Architectures.** Our analysis of how models leverage side information demonstrates that code generation models (VLMs) excel at long-horizon stability but fail at visual state estimation, struggling to estimate geometry without explicit positional data. VDMs, in contrast, change little when given the same information, suggesting that their main bottleneck is not access to scene state, but using it to maintain coherent long-horizon dynamics. This points toward hybrid architectures that combine strong visual state estimation with explicit or structured dynamics representations. Indeed, we find that code generation and video diffusion can serve complementary roles for physical prediction, and our simple gating mechanism serves as an effective proof-of-concept for combining their strengths.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> **迈向混合架构。** 我们对"模型如何利用旁路信息"的分析表明：代码生成模型（VLM）擅长长时程稳定性，却在视觉状态估计上失败，难以在无显式位置数据时估计几何。相比之下，VDM 在被给予相同信息时几乎不变，表明其主要瓶颈并非"获取场景状态"，而是"用它来维持连贯的长时程动力学"。这指向一种**混合架构**——将强视觉状态估计与显式或结构化的动力学表示相结合。事实上，我们发现代码生成与视频扩散可在物理预测中扮演互补角色，而我们简单的门控机制是结合二者优势的有效概念验证。

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> **Limitations.** Our dataset is limited to 2D MPM simulations and does not capture the full material or visual richness of the real world, including materials such as hair, cloth, or highly stiff bodies. Because all videos are generated by ground-truth simulation code, the benchmark may also favor code-generation approaches in ways that may not transfer to natural video. Future work should extend the benchmark to 3D scenes, real-world deformable dynamics, and natural-language side information, making models more useful for artists and everyday users. More broadly, realistic physical video generation may be misused to produce misleading simulations, making controlled evaluation and failure analysis important for responsible deployment.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> **局限性。** 我们的数据集局限于二维 MPM 模拟，未能捕捉真实世界的全部材料或视觉丰富性，包括头发、布料或高刚度物体等材料。由于所有视频都由真值模拟代码生成，该基准也可能以无法迁移到自然视频的方式偏向代码生成方法。未来工作应将基准扩展到三维场景、真实世界可变形动力学与自然语言旁路信息，使模型对艺术家与日常用户更有用。更广泛地说，逼真的物理视频生成可能被滥用于制造误导性模拟，因此受控评估与失败分析对负责任的部署至关重要。

---

## References 参考文献

> 以下为论文参考文献原文（保留原始书目格式）：

- Anton Bakhtin, Laurens van der Maaten, Justin Johnson, Laura Gustafson, and Ross Girshick. **Phyre: A new benchmark for physical reasoning.** arXiv:1908.05656, 2019.
- Hritik Bansal, Zongyu Lin, Tianyi Xie, Zeshun Zong, Michal Yarom, Yonatan Bitton, Chenfanfu Jiang, Yizhou Sun, Kai-Wei Chang, and Aditya Grover. **Videophy: Evaluating physical commonsense for video generation.** arXiv:2406.03520, 2024.
- Hritik Bansal, Clark Peng, Yonatan Bitton, Roman Goldenberg, Aditya Grover, and Kai-Wei Chang. **Videophy-2: A challenging action-centric physical commonsense evaluation in video generation.** arXiv:2503.06800, 2025.
- Peter Battaglia, Razvan Pascanu, Matthew Lai, Danilo Jimenez Rezende, et al. **Interaction networks for learning about objects, relations and physics.** NeurIPS 29, 2016.
- Daniel M Bear, Elias Wang, Damian Mrowca, Felix J Binder, Hsiao-Yu Fish Tung, RT Pramod, Cameron Holdaway, Sirui Tao, Kevin Smith, Fan-Yun Sun, et al. **Physion: Evaluating physical prediction from vision in humans and machines.** arXiv:2106.08261, 2021.
- Jake Bruce, Michael D Dennis, Ashley Edwards, Jack Parker-Holder, Yuge Shi, Edward Hughes, Matthew Lai, Aditi Mavalankar, Richie Steigerwald, Chris Apps, et al. **Genie: Generative interactive environments.** ICML, 2024.
- Jing Gu, Xian Liu, Yu Zeng, Ashwin Nagarajan, Fangrui Zhu, Daniel Hong, Yue Fan, Qianqi Yan, Kaiwen Zhou, Ming-Yu Liu, et al. **"PhyWorldBench": A comprehensive evaluation of physical realism in text-to-video models.** arXiv:2507.13428, 2025.
- David Ha and Jürgen Schmidhuber. **World models.** arXiv:1803.10122, 2(3):440, 2018.
- Bingyi Kang, Yang Yue, Rui Lu, Zhijie Lin, Yang Zhao, Kaixin Wang, Gao Huang, and Jiashi Feng. **How far is video generation from world model: A physical law perspective.** arXiv:2411.02385, 2024.
- Gergely Klár, Theodore Gast, Andre Pradhana, Chuyuan Fu, Craig Schroeder, Chenfanfu Jiang, and Joseph Teran. **Drucker-Prager elastoplasticity for sand animation.** ACM Trans. Graph., 35(4), July 2016. doi:10.1145/2897824.2925906.
- Minchen Li, Chenfanfu Jiang, Zhaofeng Luo, Wenxin Du, Chang Yu, Žiga Kovačič, and Tianyi Xie. **Physics-Based Simulation.** March 2026. doi:10.5281/zenodo.20597655. Open-source online book (https://phys-sim-book.github.io/).
- Shiqian Li, Kewen Wu, Chi Zhang, and Yixin Zhu. **I-PHYRE: Interactive physical reasoning.** ICLR, 2024.
- Jiarong Liang, Max Ku, Ka-Hei Hui, Ping Nie, and Wenhu Chen. **Visphyworld: Probing physical reasoning via code-driven video reconstruction.** 2026. arXiv:2602.13294.
- Yunchao Liu, Zheng Wu, Daniel Ritchie, William T Freeman, Joshua B Tenenbaum, and Jiajun Wu. **Learning to describe scenes with programs.** ICLR, 2019.
- Fanqing Meng, Jiaqi Liao, Xinyu Tan, Wenqi Shao, Quanfeng Lu, Kaipeng Zhang, Yu Cheng, Dianqi Li, Yu Qiao, and Ping Luo. **Towards world simulator: Crafting physical commonsense-based benchmark for video generation.** arXiv:2410.05363, 2024.
- Shi Qiu, Shaoyang Guo, Zhuo-Yang Song, Yunbo Sun, Zeyu Cai, Jiashen Wei, Tianyu Luo, Yixuan Yin, Haoxu Zhang, Yi Hu, et al. **Phybench: Holistic evaluation of physical perception and reasoning in large language models.** arXiv:2504.16074, 2025.
- Hsiao-Yu Tung, Mingyu Ding, Zhenfang Chen, Daniel Bear, Chuang Gan, Josh Tenenbaum, Dan Yamins, Judith Fan, and Kevin Smith. **Physion++: Evaluating physical scene understanding that requires online inference of different physical properties.** NeurIPS 36:67048–67068, 2023.
- Tomer D Ullman, Elizabeth Spelke, Peter Battaglia, and Joshua B Tenenbaum. **Mind games: Game engines as an architecture for intuitive physics.** Trends in Cognitive Sciences, 21(9):649–665, 2017.
- Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A Smith, Daniel Khashabi, and Hannaneh Hajishirzi. **Self-instruct: Aligning language models with self-generated instructions.** ACL, pages 13484–13508, 2023.
- Jiajun Wu, Ilker Yildirim, Joseph J Lim, Bill Freeman, and Josh Tenenbaum. **Galileo: Perceiving physical object properties by integrating a physics engine with deep learning.** NeurIPS 28, 2015.
- Jiajun Wu, Joseph J Lim, Hongyi Zhang, Joshua B Tenenbaum, and William T Freeman. **Physics 101: Learning physical object properties from unlabeled videos.** BMVC, vol. 2, p. 7, 2016.
- Tianyidan Xie, Peiyu Wang, Yuyi Qian, Yuxuan Wang, Rui Ma, Ying Tai, Song Wu, Qian Wang, Lanjun Wang, and Zili Yi. **Physcodebench: Benchmarking physics-aware symbolic simulation of 3d scenes via self-corrective multi-agent refinement.** arXiv:2604.23580, 2026.
- Kexin Yi, Chuang Gan, Yunzhu Li, Pushmeet Kohli, Jiajun Wu, Antonio Torralba, and Joshua B Tenenbaum. **Clevrer: Collision events for video representation and reasoning.** ICLR, 2020.
- Jianhao Yuan, Fabio Pizzati, Francesco Pinto, Lars Kunze, Ivan Laptev, Paul Newman, Philip Torr, and Daniele De Martini. **Likephys: Evaluating intuitive physics understanding in video diffusion models via likelihood preference.** arXiv:2510.11512, 2025.

---

## Appendix 附录

### A Full test set evaluation results 完整测试集评估结果

#### A.1 Example Results 示例结果

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> Additional qualitative examples of model failure modes are provided in Figures 10 and 11, illustrating object-collapse failures, material misidentification, and spatial reasoning errors across both model classes.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 图 10 与图 11 提供了模型失败模式的更多定性示例，展示两类模型的物体坍缩失败、材料误识别与空间推理错误。

### Fig. 10. 物体持久性与材料推断的失败模式

![Fig. 10](fig10_object_permanence.png)

**Caption:** Figure 10: Failure modes in object permanence and material inference. Left: In an elastoplastic scene, the VLM correctly maintains rigid object trajectories, while the VDM suffers from severe object collapse, causing the bouncing green block to disappear during extrapolation. Right: When explicit material properties are withheld from the input prompt, the VLM sometimes struggles with material inference from frames, hallucinating incorrect interaction dynamics (e.g., treating the liquid surface as a rigid boundary). The VDM, relying purely on pixel patterns, more accurately captures object materials.

**Caption[CN]:** 图 10：物体持久性与材料推断的失败模式。左：弹塑性场景中，VLM 正确保持刚体轨迹，而 VDM 出现严重物体坍缩，使弹跳的绿色方块在外推中消失。右：当输入提示中扣除显式材料属性时，VLM 有时难以从帧推断材料，幻想出错误的交互动力学（如把液面当作刚性边界）；而纯靠像素模式的 VDM 反而更准确地捕捉了物体材料。

**Reading note:** 左例 = VLM 赢（坍缩对比），右例 = VDM 赢（材料推断对比）——再次体现两模型在不同维度互有胜负。

### Fig. 11. 复杂动力学与空间推理中的对比性失败模式

![Fig. 11](fig11_complex_dynamics.png)

**Caption:** Figure 11: Contrasting failure modes in complex dynamics and spatial reasoning. Left: In a scene featuring high-energy multi-material interactions (a kinematic pinwheel, fluid, and a rigid block), the VLM accurately preserves object permanence and fluid volume. The VDM suffers from temporal object collapse, causing the rigid block to unphysically dissipate into the surrounding fluid during extrapolation (red boxes). Right: When explicit positional coordinates are limited, the VLM struggles with visual state estimation, hallucinating an incorrect geometric layout for the obstacle pegs (red boxes). The VDM, relying directly on pixel-space conditioning, successfully preserves the underlying spatial geometry.

**Caption[CN]:** 图 11：复杂动力学与空间推理中的对比性失败模式。左：在含高能多材料交互（运动学风车、流体、刚性方块）的场景中，VLM 准确保持物体持久性与流体体积；VDM 出现时间性物体坍缩，使刚性方块在外推中非物理地消散进周围流体（红框）。右：当显式位置坐标受限时，VLM 在视觉状态估计上吃力，幻想出障碍桩的错误几何布局（红框）；而直接依赖像素空间条件的 VDM 成功保留了底层空间几何。

### B Evaluation Metrics 评估指标（细节）

#### B.1 Mask Intersection-Over-Union 掩膜交并比

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For each frame, RGB images are thresholded into binary foreground masks and the Intersection-over-Union is computed frame-wise, with $\text{IoU}_t = 1$ when both masks are empty. The final score is the mean over all video frames.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 对每一帧，将 RGB 图像阈值化为二值前景掩膜并逐帧计算交并比；当两个掩膜都为空时取 $\text{IoU}_t = 1$。最终分数为所有视频帧上的均值。

$$\text{IoU}_t = \frac{|M^{GT}_t \cap M^{pred}_t|}{|M^{GT}_t \cup M^{pred}_t|}$$

#### B.2 Object Collapse Score (OCS) 物体坍缩分数

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> We measure prediction-internal temporal object coherence by checking whether objects generated early in the predicted rollout remain visible over time. We segment foreground components in an early frame using brightness thresholding and connected components, merge components with near-identical colors, and use the surviving components as predicted object/material regions. Each region defines an initial area $a^{(0)}_n$ and reference color $c_n$.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 我们通过检查"预测轨迹早期生成的物体是否随时间保持可见"来度量预测内部的时间物体连贯性。我们在早期帧用亮度阈值与连通分量分割前景成分，合并颜色近乎一致的成分，并将存活成分用作预测的物体/材料区域。每个区域定义一个初始面积 $a^{(0)}_n$ 与参考颜色 $c_n$。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> At each later frame $t$, we estimate the area $a^{(t)}_n$ of region $n$ by counting foreground pixels whose chromaticity and brightness remain close to $c_n$. The object-level collapse score is given below, and the per-video score is the worst collapse over all initialized regions and frames:

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 在之后每一帧 $t$，我们通过统计色度与亮度仍接近 $c_n$ 的前景像素，估计区域 $n$ 的面积 $a^{(t)}_n$。物体级坍缩分数如下，每段视频的分数取所有初始化区域与帧上的最坏坍缩：

$$s^{(t)}_n = \max\left(0,\ 1 - \frac{a^{(t)}_n}{a^{(0)}_n}\right)$$

$$\text{OCS} = \max_{n,\,t>0} s^{(t)}_n$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> Lower values indicate that predicted objects or material regions remain stable; values near one indicate that at least one generated region nearly disappears during the predicted video. For example a value of 0.8 means on average over all test samples in that group, the single worst object in each generated video lost 80% of its initial pixel count at some point during the predicted video.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 值越低表示预测的物体或材料区域越稳定；值接近 1 表示至少有一个生成区域在预测视频中几乎消失。例如，值为 0.8 意味着在该组所有测试样本上平均，每段生成视频中最差的那个物体在预测视频的某一时刻损失了其初始像素数的 80%。

#### B.3 Temporal Anomaly Rate (RTSJ) 时间异常率

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For each frame, we divide the image into coarse spatial regions and compute HSV color histograms within each region. Temporal jumps are measured by comparing histogram statistics across neighboring temporal windows, producing a localized spatiotemporal change signal. We then spatially aggregate this signal to obtain a jump magnitude $J_t$ for each timestep $t$.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 对每一帧，我们将图像划分为粗粒度空间区域，并在每个区域内计算 HSV 颜色直方图。时间跳变通过比较相邻时间窗口间的直方图统计量来度量，产生一个局部化的时空变化信号。随后我们对该信号做空间聚合，得到每个时间步 $t$ 的跳变幅值 $J_t$。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> For both the prediction and ground truth, we compute jump magnitudes $J^{pred}_t$ and $J^{GT}_t$. The excess jump is defined below, and a prediction is flagged as anomalous if its maximum excess jump exceeds threshold $\tau$. The reported anomaly rate is the proportion of test samples flagged as anomalous.

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 对预测与真值，我们分别计算跳变幅值 $J^{pred}_t$ 与 $J^{GT}_t$。超额跳变定义如下，若某预测的最大超额跳变超过阈值 $\tau$ 则被标记为异常。所报告的异常率是被标记为异常的测试样本比例。

$$e_t = \max\left(J^{pred}_t - J^{GT}_t,\ 0\right)$$

$$\text{anomaly} = \mathbb{1}\left[\max_t e_t > \tau\right]$$

### C Modification test set values 修改测试集数值

> 见上文 [Table 3](#table-3-修改验证集上各共享输入条件的视觉指标) 与 [Fig. 12](#fig-12-修改测试划分上的-vlmvdm-对比)。

### D Prefix-Quality Threshold Gating 前缀质量阈值门控

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> For each metric $m$ and task condition, we compute a prefix score $p^m_i = m(\hat{x}^{VLM}_i, x_i)$ between the predicted and ground-truth prefix, along with continuation scores $c^m_{i,VLM}$ and $c^m_{i,VDM}$ for the corresponding continuations.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 对每个指标 $m$ 与任务条件，我们计算预测前缀与真值前缀之间的前缀分数 $p^m_i = m(\hat{x}^{VLM}_i, x_i)$，以及相应续写的续写分数 $c^m_{i,VLM}$ 与 $c^m_{i,VDM}$。

> <span style="color:#3B82F6"><strong>Para. 2:</strong></span> We then sweep thresholds $\tau$ on a held-out validation set and select the threshold minimizing the average continuation error (for lower-is-better metrics; for higher-is-better metrics such as mIoU, the inequality is reversed):

> <span style="color:#F59E0B"><strong>Para. 2[CN]:</strong></span> 随后我们在留出验证集上扫描阈值 $\tau$，并选择使平均续写误差最小的阈值（针对越低越好的指标；对 mIoU 等越高越好的指标，不等号方向反转）：

$$\tau^{m*} = \arg\min_\tau \frac{1}{N}\sum_{i=1}^{N} \begin{cases} c^m_{i,VLM}, & p^m_i < \tau \\ c^m_{i,VDM}, & \text{otherwise} \end{cases}$$

> <span style="color:#3B82F6"><strong>Para. 3:</strong></span> At inference time, we sample multiple VLM candidates, select the candidate with the best prefix score, and apply the learned threshold to decide whether to use the VLM or VDM continuation. Thresholds are learned independently for each metric and task condition.

> <span style="color:#F59E0B"><strong>Para. 3[CN]:</strong></span> 推理时，我们采样多个 VLM 候选，选出前缀分数最佳的候选，并应用学习到的阈值来决定使用 VLM 还是 VDM 续写。阈值针对每个指标与任务条件独立学习。

### E Temporal cumulative collapse rate 时间累积坍缩率

> 见上文 [Fig. 13](#fig-13-外推帧上的累积坍缩率)。

### F Compute Resources 计算资源

> <span style="color:#3B82F6"><strong>Para. 1:</strong></span> All VLM and VDM experiments were trained on a server with 4 NVIDIA RTX A6000 GPUs. Training each model required approximately 12 hours. Additional compute was used for dataset generation, rendering, and evaluation.

> <span style="color:#F59E0B"><strong>Para. 1[CN]:</strong></span> 所有 VLM 与 VDM 实验均在配备 4 块 NVIDIA RTX A6000 GPU 的服务器上训练。每个模型训练约需 12 小时。数据集生成、渲染与评估使用了额外的计算资源。

---

## 术语表 / Terminology

| 规范术语 (Canonical) | 首次定义 (First-use) | 源文中的变体 (Variants) | 中文译法 (Decision) |
|---|---|---|---|
| MPM | Material Point Method (MPM) | — | 物质点法（MPM） |
| MPMWorlds | the assembled dataset | MPMWorld | 数据集名，保留英文 MPMWorlds |
| VLM | Vision-Language Model (VLM) | code generation model | 视觉-语言模型（VLM）/ 代码生成模型 |
| VDM | Video Diffusion Model (VDM) | video diffusion, 'VDMs' | 视频扩散模型（VDM） |
| inference | inferring physical dynamics | recovery, reconstruction | 推断（恢复/重建前向模拟） |
| extrapolation | extrapolating forward in time | continuation | 外推（沿时间向前续写） |
| side information | physically-relevant side information $f(\rho)$ | privileged information | 旁路信息 / 特权信息 |
| W-MAE | Windowed Motion Activity Error | WMAE | 窗口化运动活跃度误差（↓） |
| CTV | Color Total Variation | — | 颜色全变差（↓） |
| OCS | Object Collapse Score (OCS) | Obj. Collapse, Collapse | 物体坍缩分数（↓） |
| mIoU | Mask IoU (mIoU) | IoU | 掩膜交并比（↑） |
| RTSJ | Temporal Anomaly Rate (RTSJ) | Anomaly Rate, Anom. | 时间异常率（↓） |
| SEMD | sliced Earth Mover's Distance | — | 切片地动距离（↓） |
| Scene Template | core 10k Scene Templates | base scenes | 场景模板 |
| Parent / Child | Parent / Child simulations | — | 父模拟 / 子模拟 |
| constitutive model | — | material model | 本构模型 |
| Drucker–Prager sand | Drucker–Prager sand | sand | Drucker–Prager 沙（颗粒弹塑性） |
| Best-of-N | Best-of-N sampling | — | Best-of-N 采样 |
| prefix-quality gate | prefix-quality gate | Threshold Gate, routing | 前缀质量门控 |

---

## 阅读提示 / Critical reading notes

> 以下为译者基于全文的批判性导读，便于快速把握论文价值与边界，非原文内容。

**一句话总结。** 论文构建了一个 2D MPM 物理模拟数据集 MPMWorlds（≈95.8k 渲染视频，10k 场景模板），并用它系统对比"代码生成（VLM, Qwen2.5-VL-7B）"与"视频扩散（VDM, LongCat-14B）"两条路线在"从视频推断物理 + 长时程外推"上的优劣，结论是二者**强互补**：VLM 长时程稳定但几何弱、对结构化信息敏感；VDM 几何好但会幻想动力学、对结构化信息几乎不敏感。

**核心证据链（值得信任之处）。**
- 互补性结论由多个独立视角交叉支撑：主指标热力图（图 4/表 2）、时间演化曲线（图 8 W-MAE、图 13 坍缩率）、材料族分解（图 5、图 7）、以及定性失败案例（图 6/9/10/11），结论自洽。
- "前缀质量门控"（表 1）是一个干净的概念验证：仅用可见前缀的重建质量做路由，就在几乎所有稳定性指标上超过两个单模型，且 mIoU 主要路由给 VDM、稳定性指标路由给 VLM，直接验证了互补假设。
- 指标设计有意回避像素级度量（MSE/SEMD），并论证其"与长时程物理一致性相关性差"——表 2 中 VDM 反而在 MSE/SEMD 上更优，恰好支持这一论点。

**需要警惕的局限（作者已部分承认）。**
- **基准可能系统性偏向代码生成。** 所有视频都由真值模拟代码渲染，VLM 任务本质上是"逆向工程同源代码"，这种优势未必迁移到自然视频。作者在 Limitations 中明确指出这一点。
- **仅 2D、单一渲染风格、高对比度背景**，缺少布料/头发/高刚度体；外观因素被刻意简化。结论外推到真实世界需谨慎。
- **模型规模不对等**：VLM 7B（全量微调）vs VDM 14B（LoRA），且 VDM 仅采样 1 个样本而 VLM 采样 15 个 + Best-of-N。作者用"50 步去噪 ≈ 15 程序采样"来对齐计算预算，但单样本 vs Best-of-N 的方法学差异仍可能放大 VLM 的稳定性优势，阅读时应将"VLM 更稳"理解为"在该采样协议下更稳"。
- **指标均为自研的代理指标**（OCS/W-MAE/RTSJ/CTV），无粒子级真值监督；虽设计合理，但绝对数值的可比性依赖这些代理的有效性。

**可复用的点子。** ①"父-子-扰动"三级层次化数据构造 + 留出划分，可干净区分"记忆 vs 新模板泛化"（图 12/表 3）；②用"可执行重建前缀质量"作为无需后缀真值的在线置信度信号来路由多模型，是低成本的混合推理范式；③把像素级指标显式排除出主指标并给出反例论证，是物理视频评估值得借鉴的做法。

**判断笔记（draft 标注）。** 个别数值由 PDF 文本层抽取，已与裁剪的图/表图像交叉核对（图 4↔表 2、图 12↔表 3、表 1 数值一致）。文中 §5 提到"Figure 13 / Figure 12 / Figure 11"等前向引用，本阅读器已将这些图就近放在首次实质讨论处而非严格按 PDF 物理页序，以保证阅读流畅；原始页码与裁剪框记录在 `source_map.json`。
