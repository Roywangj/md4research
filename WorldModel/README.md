# WorldModel

`WorldModel` 下 60 篇。机器人相关 50 篇，视频世界模型 / 游戏世界模型 10 篇。

有 GitHub 仓库的写出链接，没有的写 `-`。链接来自论文正文、arXiv 摘要或官方项目页上的 Code 按钮。参考文献里引用的其他项目不记入。时间是 arXiv 编号里的年月，2026 年 8 月写成 `202608`。DM0.5 没有 arXiv，用文中发布日期 2026-09。

分类按论文的主要任务。机械臂、移动操作、导航和具身策略放在机器人。视频生成、交互视频、游戏预演放在视频 / 游戏。ReWorld 做的是自动驾驶视频世界模型，放在后一类。

两类分开排序、分开编号。时间新的在上，时间早的在下。同一月份按论文目录名排列。编号从上往下由大到小，最新的一篇编号最大。

## 机器人

| 编号 | 论文目录 | 时间 | GitHub |
| --- | --- | --- | --- |
| 50 | Long-WAM Scaling the Context of World-Action Models | 202610 | https://github.com/NVlabs/Long-WAM |
| 49 | Native Action-Prior Learning from Videos for World Action Models | 202610 | - |
| 48 | Video Prediction Policy 2 Predict Better, Act Better | 202610 | https://github.com/roboterax/video-prediction-policy-2 |
| 47 | Benchmarking World Models for Continual Learning on Compositional Tasks | 202609 | - |
| 46 | Beyond Future Prediction Denoising as Generative Adaptation for Robot Control | 202609 | https://github.com/xmz111/NowWAM |
| 45 | DM0.5 An Open-World Foundation Model for General-Purpose Embodied Intelligence | 202609 | https://github.com/dexmal |
| 44 | In-Context Robot Learning with VLM Agents | 202609 | https://github.com/cheng-haha/GPT-Policy |
| 43 | InternW0-Δ A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data | 202609 | - |
| 42 | Memory as Plans World-Action Modeling with Memory-Grounded Planning | 202609 | https://github.com/aipixel/MaP-WAM |
| 41 | OpenWAM An Open, Modular Exploration Towards Systematic World-Action Model Pretraining | 202609 | https://github.com/OpenWAM-Official/OpenWAM |
| 40 | RoboSPA Can VLA Models Go Beyond Simple Scenes and Short-Horizon Tasks | 202609 | https://github.com/fanzhenxuan/RoboSPA |
| 39 | SimpleMemVLA A Simple but Effective Native-Video Memory for Vision-Language-Action Models | 202609 | https://github.com/wadeKeith/SimpleMemVLA ；arXiv 摘要另写 https://github.com/OpenBMB/SimpleMemVLA |
| 38 | BridgeVLA++ A Data-Efficient, Generalizable, and Memory-Augmented Vision-Language-Action Framework | 202608 | https://github.com/BridgeVLA/BridgeVLA |
| 37 | FACT Failure-Aware Causal Training for World-Action Models | 202608 | https://github.com/Bariona/FACT |
| 36 | Foresight Without Seeing Latent Futures for World Action Models | 202608 | - |
| 35 | GaussianWAM Distilling Geometry and Semantics from 3D Gaussian Fields into World-Action Models | 202608 | https://github.com/TuojingAI/GaussianWAM |
| 34 | HarnessWAM Bridging Prediction and Deliberation in World Action Models | 202608 | - |
| 33 | Motus2 A Self-Evolving General World Model for Dexterous Manipulation | 202608 | https://github.com/shengshu-ai/Motus2 |
| 32 | SC²-WM A Self-Correcting World Model with Closed-Loop Feedback for Vision-and-Language Navigation in Continuous Environments | 202608 | https://github.com/sunrise-ikun/SC2_WM |
| 31 | SelfWAM A Self-Grounded Unified World Action Model for Fast Robot Control | 202608 | https://github.com/SelfWAM/SelfWAM |
| 30 | Skills in Weights, Memory in Code Hybrid Learning for Memory-Dependent Robot Manipulation | 202608 | - |
| 29 | ABot-M0.5 Unified Mobility-and-Manipulation World Action Model | 202607 | https://github.com/amap-cvlab/ABot-Manipulation |
| 28 | DC-WAM Dynamic-Centric Visual Supervision and Reasoning for World-Action Models | 202607 | - |
| 27 | Harness VLA Steering Frozen VLAs into Reliable Manipulation Primitives via Memory-Guided Agents | 202607 | https://github.com/RLinf/RPent |
| 26 | Learning 4D Geometric Priors for Inference-Efficient World Action Models | 202607 | - |
| 25 | Masked Visual Actions for Unified World Modeling | 202607 | https://github.com/HadiZayer/masked-visual-actions |
| 24 | RynnWorld-4D 4D Embodied World Models for Robotic Manipulation | 202607 | https://github.com/alibaba-damo-academy/RynnWorld-4D |
| 23 | Test-Time Scaling for World Action Models via Zero-Shot Geometric Evaluation | 202607 | - |
| 22 | WSA_1 a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control | 202607 | https://github.com/zaleni/WSA |
| 21 | DIM-WAM World-Action Modeling with Diverse Historical Event Memory | 202606 | - |
| 20 | Efficient-WAM A 1B-Parameter World-Action Model with Low-Cost Future Imagination | 202606 | https://github.com/jiajun613/Efficient-WAM |
| 19 | EventVLA Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies | 202606 | https://github.com/InternRobotics/EventVLA |
| 18 | GeoSem-WAM Geometry- and Semantic-Aware World Action Models | 202606 | - |
| 17 | ImageWAM Do World Action Models Really Need Video Generation, or Just Image Editing | 202606 | https://github.com/yuyangalin/ImageWAM |
| 16 | LaWAM Latent World Action Models for Efficient Dynamics-Aware Robot Policies | 202606 | - |
| 15 | Light-WAM Efficient World Action Models with State-Fusion Action Decoding | 202606 | https://github.com/L1ziang/Light-WAM |
| 14 | MemoryWAM Efficient World Action Modeling with Persistent Memory | 202606 | https://github.com/yangsizhe/MemoryWAM |
| 13 | VoLo A Physical Orchestrator for Open-Vocabulary Long-Horizon Manipulation | 202606 | 代码 https://github.com/NVlabs/VoLoAgent ；基准 https://github.com/NVlabs/RoboVoLo |
| 12 | WAM4D Fast 4D World Action Model via Spatial Register Tokens | 202606 | https://github.com/myendless1/wam4d |
| 11 | World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis | 202606 | https://github.com/SJTU-DENG-Lab/WLA |
| 10 | NoiseGate Learning Per-Latent Timestep Schedules as Information Gating in World Action Models | 202605 | - |
| 9 | RoboMemArena A Comprehensive and Challenging Robotic Memory Benchmark | 202605 | https://github.com/OpenHelix-Team/RoboMemArena |
| 8 | DiT4DiT Jointly Modeling Video Dynamics and Actions for Generalizable Robot Control | 202603 | https://github.com/Mondo-Robotics/DiT4DiT |
| 7 | Fast-WAM Do World Action Models Need Test-time Future Imagination | 202603 | https://github.com/yuantianyuan01/FastWAM |
| 6 | RMBench Memory-Dependent Robotic Manipulation Benchmark with Insights into Policy Design | 202603 | https://github.com/robotwin-Platform/rmbench |
| 5 | Simulation Distillation Pretraining World Models in Simulation for Rapid Real-World Adaptation | 202603 | https://github.com/CLeARoboticsLab/simdist |
| 4 | World Action Models are Zero-shot Policies | 202602 | https://github.com/dreamzero0/dreamzero |
| 3 | Causal World Modeling for Robot Control | 202601 | https://github.com/robbyant/lingbot-va |
| 2 | RLinf Flexible and Efficient Large-scale Reinforcement Learning via Macro-to-Micro Flow Transformation | 202509 | https://github.com/RLinf/RLinf |
| 1 | Inference-Time Enhancement of Generative Robot Policies via Predictive World Modeling | 202502 | - |

## 视频世界模型 / 游戏世界模型

| 编号 | 论文目录 | 时间 | GitHub |
| --- | --- | --- | --- |
| 10 | Code World Model Coding Agent as World Brain | 202608 | https://github.com/buaacyw/code-world-model |
| 9 | Learning How the World Evolves Extrapolative Video World Models via Latent Dynamics Reasoning | 202608 | https://github.com/adobe-research/LDR |
| 8 | StateFlow Building Evolving and Accessing 3D World States for Previsualization | 202608 | - |
| 7 | Hierarchical Denoising For Multi-Step Visual Reasoning | 202607 | https://github.com/hierarchical-diffusion-reasoning/hierarchical-diffusion-reasoning.github.io |
| 6 | StatePlay State-Aware Game World Models for Mechanics-Consistent Generation | 202607 | https://github.com/Jimntu/StatePlay |
| 5 | BiWM Advancing Open-Source Interactive Video World Models with Bidirectional Autoregression | 202606 | https://github.com/LynnReal-AI/BiWM |
| 4 | ReWorld Representation Learning for World Action Models | 202606 | https://github.com/xiaomi-research/ReWorld |
| 3 | Light Interaction Training-Free Inference Acceleration for Interactive Video World Models | 202605 | - |
| 2 | Nano World Models A Minimalist Implementation of Future Video Prediction | 202605 | https://github.com/simchowitzlabpublic/nano-world-model |
| 1 | Mixture of Contexts for Long Video Generation | 202508 | - |
