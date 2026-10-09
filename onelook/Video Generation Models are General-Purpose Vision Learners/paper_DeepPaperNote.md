# Video Generation Models are General-Purpose Vision Learners

## 核心信息

- **论文：** Video Generation Models are General-Purpose Vision Learners（Wang 等，2026，arXiv:2607.09024）
- **模型：** GenCeption，基于 WAN 2.1 的视频生成骨干改造。
- **核心判断：** 文本到视频生成的预训练目标同时提供时空/物理先验、视觉—语言对齐和可扩展的训练路径，可作为通用视觉模型的“下一词预测”。
- **任务：** depth、surface normal、camera pose、foreground / expression-referring segmentation、dense pose、2D/3D keypoints。
- **数据：** 7,500 个以人为中心的合成视频；800 RenderPeople 资产 × 200 CMU 动作，加入 TartanAir、Virtual KITTI、MVS Synth；表达式分割使用 MeViS、Ref-COCO、YouTube-VOS。

## 原文摘要翻译

GenCeption 将预训练视频生成扩散骨干变成由文本指令控制的前馈感知模型。在深度、法线、相机位姿、表达式指代分割和 3D 关键点等任务上，它常常达到或超过专用模型；在相同微调设置下超过 V-JEPA 和 VideoMAE V2。模型规模和数据量扩大时性能提高，以少 7 倍至 500 倍训练数据取得 D4RT、VGGT-Ω 的相当性能。只在合成人类视频上训练也能泛化到真实视频、动物和机器人。

## 创新点

1. **把视频生成预训练提升为视觉基础学习范式。** 贡献重点不是“用扩散模型做深度”这个技巧，而是提出生成式视频骨干可作为通用视觉先验的总体论点。
2. **单步前馈化。** 将输入干净 latent 直接送入 WAN DiT，固定 $t=0$，取负 Rectified Flow velocity：$-v=x_0-\epsilon$，避免 50 步迭代采样。
3. **数据表示替代任务专用工程。** 稠密任务统一到 $[0,1]$ RGB 空间，深度和分割复制通道；相机位姿压成 “Rothko” raymap；稀疏任务仅追加每帧可学习 token。
4. **多任务统一损失。** 全部任务使用标准 $L_2$，不手动设计任务损失；尺度歧义由深度归一化和 $d'=\operatorname{clip}(\alpha\log(d+1),0,1)$ 处理。
5. **展示涌现泛化。** 合成人体单物体训练转移到真实多物体视频和动物/拟人角色。

## 一句话总结

这篇论文的真正命题是：如果视频生成器必须生成“运动中的世界”，它学到的表征比图像/视频自监督特征更接近可复用的世界模型；GenCeption 用低改动、单步和数据格式把这个先验暴露给感知任务。

## 研究问题

计算机视觉为何仍需每个任务一个专用模型？作者寻找视觉版 next-token prediction，并要求预训练目标同时内化 4D 因果、对齐语言、在大数据和大算力上扩展。

## 数据与任务定义

合成管线的覆盖是论文说服力的一半：800 RenderPeople、200 CMU motions、HDRI/3D 背景、变化焦距和相机轨迹，共 7,500 视频；Blender render pass 直接给深度、法线、分割，rigged joints 给 2D/3D 关键点。由于大多数真实数据集只提供一种标注，合成数据天然适合多模态共同训练。

评测涵盖 Hi4D / SINTEL（法线）、KITTI / SINTEL / ETH3D / Goliath（深度）、VideoMatte / PhotoMatte85 / PPM-100（软前景）、SINTEL（相机）、EMDB（3D 关键点）和 Ref-DAVIS / MeViS（表达式分割）。指标为 mAE、AbsRel、RMSE、MSE、J&F、MPJPE、ATE、RPE-T、RPE-R。

## 方法主线

### 机制流程

1. RGB 视频经 VAE encoder 得到 video tokens；文本任务提示经 text encoder 得到 text tokens。
2. 输入**干净**视频 latent 而非噪声 latent；DiT 条件时间步固定 $t=0$，进行一次前向。
3. WAN 的 Rectified Flow 预测 velocity $v=\epsilon-x_0$，模型将其取负后接 decoder 或输出头。
4. 稠密结果以 RGB 视频表达；稀疏任务向 latent 序列加 $T$ 个 learnable tokens，MLP 输出坐标。
5. 训练只用 $L_2$；深度先中位数归一化，再进行对数压缩。

### 关键机制：为什么用最终层和 velocity 取负

作者把 DiT 当作强特征提取器，而不是保留扩散采样。Rectified Flow 的 velocity 在 $t=0$ 取负后更靠近目标 latent；最终层特征与 decoder 原生对齐，避免中间层特征注入和额外架构改动。这里的经验性细节是可复现关键：若仍按常规噪声预测或使用多步采样，论文的速度优势和收敛行为不成立。

### 关键机制：统一 RGB 与 raymap

统一 RGB 空间是工程上最重要的“接口设计”。深度/掩码等一维输出复制到三通道，法线和 DensePose 直接使用三维；六维相机 ray data 则以中心 ray origin、外围 ray direction 的空间布局压成三通道。它把任务差异放进 target representation，而不是损失和头部。这类似 LLM 把各种任务格式化为 token 序列，但视觉侧有一个连续 pixel-space 先验可利用。

### 关键机制：稀疏 token 的代价

3D 关键点需要直接坐标，不能自然地塞进像素空间，所以引入每帧 token。消融显示这是统一模型的薄弱处：从零学习的 token 会扰乱原 DiT 注意力，坐标回归也偏离生成预训练的连续像素域。论文因此给出一个反例：统一架构不是“所有任务天然受益”，稀疏任务可能需要原生设计或更长训练。

## 关键结果

### 主结果与强基线

14B specialist 的 Sintel normal mAE 为 29.7、KITTI depth AbsRel 0.048、Sintel camera ATE 0.050、MEVIS J&F 76.4；14B generalist 的对应 normal mAE 29.3、depth 0.048、J&F 75.8。GenCeption 在多数几何和分割任务上接近或超过 NormalCrafter、Lotus-2、DepthAnything 3、D4RT、VGGT-Ω、SAM3、Genmo 和 TRAM。

推理成本从 WAN 的 50-step diffusion 降为单步：1.3B 为 5.92 s / 13.6 FPS / 15.3 GB VRAM；14B 为 10.03 s / 8.0 FPS / 42.8 GB VRAM（均为 v6e、81 帧、480×832）。这不是轻量模型，但对于视频生成骨干而言，速度改善是方法成立的必要条件。

### 预训练比较、规模与数据效率

同一 7.5K 视频微调时，WAN 2.1-L 平均 AbsRel 0.093、δ1 90.7；VideoMAE V2-G 为 0.154 / 66.9，V-JEPA-H 为 0.281 / 52.2。14B WAN 在 8.08K 视频、1.23M 帧上达到 0.071 / 93.8。作者以此主张生成目标本身比单纯数据规模更重要，但这仍是“可比设置”下的证据，不是严格控制所有 backbone 参数、tokenizer 和优化预算的因果实验。

### 消融到底说明了什么

- 从随机初始化 DiT 开始，曲线近乎平坦；迁移预训练层越多，结果越好：预训练是收敛来源，不只是初始化速度。
- joint training 对 foreground 有益，对 expression referring 基本无影响，对 depth/camera pose 可能退化，对 3D keypoint 严重有害。
- 深度的尺度不确定性可通过 median normalization + logarithmic mapping 转化为数据问题，说明统一 loss 的可行性依赖于精心设计 target。
- 7×–500× 的数据效率数字极强，但对比对象的训练数据来源、标注密度和训练 recipe 不完全同构，不能直接解释成样本复杂度定律。

## 深度分析

### 真正贡献是什么

真正贡献是“生成式预训练的接口化”：把视频生成器内部的世界先验、语言条件和连续像素 latent 暴露为一个统一感知 API。模型架构本身相对朴素（WAN DiT + VAE + text encoder + decoder/token MLP），创新更多来自预训练范式判断、$t=0$ feed-forward reformulation、RGB/raymap 编码和合成多任务数据。

### 为什么结果成立

1. **目标更强。** 生成完整运动序列需要同时解释外观、时间连续性、几何和交互，而 MAE/V-JEPA 的表征目标不要求重建可生成的世界。
2. **语言是任务路由器。** “output: depth/normal/segmentation/pose” 将任务条件直接写进预训练已有的 text-conditioning 通道。
3. **合成标签密集且一致。** 同一渲染场景可同时产生多个 modality，避免现实数据集的任务间错位。
4. **输出接口统一。** RGB latent 让 decoder 能共享，减少多任务训练的架构分支和 loss balancing。

### 容易误读的地方

- “通用世界模型”是作者根据跨域泛化和生成预训练先验提出的解释，不等于已证明模型拥有可查询、可因果干预的物理世界模拟器。
- 14B specialist 和 generalist 的比较不是所有任务都提升；3D keypoint 的 generalist 结果甚至是缺失/退化的。
- 合成人体训练泛化到动物很有趣，但仍可能依赖 WAN 预训练已见过的动物数据，不能把能力全归因于 7,500 条合成视频。
- 论文声明 2026 年 SOTA，引用和基准中包含未来版本模型；结果需要依赖同一代码、数据和评测协议复核。

### 复现注意点

- 需要 WAN 2.1 权重、VAE/text encoder、DiT、v6e TPU 训练环境；14B 推理约 42.8 GB VRAM。
- 必须固定 $t=0$ 并对 velocity 输出取负；这是方法定义的一部分，不是可选 trick。
- 需要 Blender、RenderPeople 许可资产、CMU mocap，以及 TartanAir/Virtual KITTI/MVS Synth。
- 表达式指代分割混入 MeViS、Ref-COCO、YouTube-VOS；其余主训练强调纯合成，复现时应区分数据来源。
- 梯度裁剪和梯度丢弃被作者称为训练稳定性的关键，但阈值没有在正文中给出，是复现缺口。

## 局限

1. **训练数据规模仍小。** 7,500 视频相对 WAN 预训练规模很小，所谓规模定律只是初步趋势。
2. **人的合成偏置。** 主要场景、人类资产和 Blender 分布可能限制几何、物理和类别泛化。
3. **任务接口不对称。** RGB 统一对稠密任务自然，对坐标型稀疏任务不自然，learnable token 反而伤害联合训练。
4. **算力门槛高。** 14B 虽然单步，但仍需要 42.8 GB VRAM；“高效”相对于 50-step WAN，而不是相对于轻量感知网络。
5. **评测和因果证据。** 预训练范式比较尚未完全控制架构、tokenizer、数据处理和算力；新类别的涌现解释依赖定性示例。
6. **论文完整性 caveat。** 正文没有独立 appendix、代码提示或详细梯度阈值；参考文献在 PDF 第 14–19 页，已记录为原始 searchable bibliography。

## 我的笔记

这篇论文值得放在“视频生成器 → 通用视觉 → world-action model”路径上，而不是只放在 diffusion depth。其最可迁移的设计不是把每个 label 画成 RGB，而是把**任务定义、输出编码、统一 loss、预训练条件通道**看作同一个接口问题。对于机器人/世界模型，最值得追问的是：动作条件和可干预状态是否也能被编码进这个接口？如果能，GenCeption 的下一步自然是从 perception-only 的 text prompt 转到 action-conditioned video prediction；如果不能，所谓 general-purpose vision 仍停留在被动估计。

我的判断：论文的证据足以支持“视频生成预训练是强视觉先验”的经验结论，但不足以单独证明“universal world model”。最强事实是 WAN 在少量合成数据上的跨任务性能和单步速度；最需要后续验证的是：去掉 WAN 原本的动物/真实场景知识后，合成人体能否仍产生同样 OOD 泛化；以及在真正动态、可交互、非人体机器人数据上，统一接口是否仍然有效。

## 引用

```bibtex
@article{wang2026videogeneration,
  title={Video Generation Models are General-Purpose Vision Learners},
  author={Wang, Letian and Zhang, Chuhan and Kabra, Rishabh and Uijlings, Jasper and Waslander, Steven and Zisserman, Andrew and Carreira, Joao and He, Kaiming and Andriluka, Misha and Bazavan, Eduard Gabriel and Zanfir, Andrei and Sminchisescu, Cristian},
  journal={arXiv preprint arXiv:2607.09024},
  year={2026}
}
```
