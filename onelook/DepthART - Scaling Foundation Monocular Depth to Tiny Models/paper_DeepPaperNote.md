# DepthART: Scaling Foundation Monocular Depth to Tiny Models

**Paper:** Feng Xue et al., arXiv:2607.17099v1 (2026)  
**Reader source:** [detailed_paper](onelook/DepthART%20-%20Scaling%20Foundation%20Monocular%20Depth%20to%20Tiny%20Models/detailed_paper.md)  
**定位：** 将 foundation monocular depth 的跨域能力压缩到 6M/11M/32M 部署模型；核心不是新 backbone，而是“数据去偏 + 保守度量适配”。

## 核心信息

DepthART 处理一个很实际的断层：Depth Anything/Metric3D/UniDepth 已经具备跨场景或 metric-scale 能力，但 tiny model 在同一训练预算和资源限制下无法直接继承。论文把失败拆成两个容量受限问题：BRDS 抵抗混合数据中的分布偏置，CamFT 通过冻结蒸馏 encoder 防止单数据集 metric fine-tuning 遗忘。

## 原文摘要翻译

DepthART 以 TinyViM-S/B/L + DPT 为轻量 trunk，从 Depth Anything v2 Large 蒸馏相对深度先验；在 1.7M 抗偏置样本上训练，然后冻结编码器，用内参条件化 adapter 与 multi-query scale head 做 metric calibration。DepthART-S 在 NYUD v2 上达到 zero-shot $\delta_1=0.964$，RTX A6000 严格 FP32 下 $224^2/448^2$ 为 347/245 FPS。

## 创新点

1. **问题分解比结构堆叠更有价值。** 论文将 tiny MDE 的瓶颈区分为“看错数据分布”和“微调忘掉几何”，BRDS/CamFT 分别对症。
2. **BRDS 是面向去偏而非压缩的 coreset。** Stable Diffusion v1.5 的 VAE latent 捕捉布局、光照、视点等整体摄影因素；PCA + 分箱构成 strata，稠密单元按 $m_c=\max(1,\lceil|D_c|/\gamma\rceil)$ 抽样，稀疏单元至少留一张。
3. **CamFT 的关键是冻结。** Camera prompt 不是为了重写 geometry，而是给 adapter 一条相机条件化的低容量修正通道；MQSH 通过多个 query 聚合全局尺度线索。
4. **效率与泛化同时报告。** 不只报参数量，也报严格 FP32、标准分辨率、端到端延迟和 Orin NX/Jetson Nano 结果。

## 一句话总结

DepthART 的真正配方是：用 VAE 特征空间的 density-aware 去偏保证 tiny student 学到“跨场景先验”，再用冻结 trunk 的相机条件化小模块只校准尺度而不重写先验。

## 研究问题

- 在 6M–32M 模型容量下，foundation-style relative-depth transfer 的主要损失来自数据分布还是结构容量？
- 单一 metric dataset fine-tuning 为何会损伤 cross-camera geometry？
- 能否用少量可训练模块恢复 metric scale，同时让 encoder 保持 domain-general geometry？
- 在真实边缘设备上，泛化收益是否值得额外 camera prompt 和 decoder 开销？

## 数据与任务定义

- **Stage 1:** 11 个来源，BRDS 后 1.7M 图像；teacher 是 Depth Anything v2 Large，监督是 pseudo depth。
- **Zero-shot relative:** NYUD v2、KITTI、ETH3D、DIODE-Full、DDAD，指标 AbsRel↓、$\delta_1$↑，逐图 scale–shift 对齐。
- **Stage 2 metric:** NYUD v2 或 KITTI 单域微调；直接在 iBims-1、SUN RGB-D、DIODE、DDAD、ETH3D 测 zero-shot metric transfer，不做 post-hoc rescaling。
- **模型:** TinyViM-S/B/L + DPT，6.0M/11.4M/32.6M 参数。

## 方法主线

### 机制流程

```text
44M mixed corpus
  -> Stable Diffusion VAE latent
  -> Incremental PCA (J=8)
  -> 10-bin density strata
  -> BRDS (1.7M pool)
  -> Depth Anything v2-L distillation
  -> frozen TinyViM encoder
  -> pyramid ray/Fourier camera prompts
  -> encoder cross-attention adapters + MQSH
  -> metric depth
```

### BRDS：控制 tiny model 看到什么

普通随机子集仍会保留高密度摄影模式；K-Means 更像覆盖选择，但没有显式按密度抑制 dominant modes。BRDS 的设计让每个 cell 至少有一个样本，对高密度 cell 按比例削减。结果支持“数据分布是容量受限 student 的第一类瓶颈”：1.7M 时 NYUD $\delta_1$/AbsRel = 0.964/0.059，KITTI = 0.930/0.082；0.5M 时相对 Random，KITTI 从 0.891/0.117 提升到 0.919/0.090。

### CamFT：控制 tiny model 忘掉什么

相机内参 $K=(f_x,f_y,c_x,c_y)$ 转成逐像素射线并 Fourier encode，在 $1/4,1/8,1/16,1/32$ 四个尺度形成 prompt。冻结 encoder 的每个 stage 用一层单头 cross-attention 读取 prompt；最深特征与 $C^{(32)}$ 进入 8-query scale head，输出正且有界的 $s$。最终 $\hat d_{metric}=d_{max}s\odot\hat d_{rel}$。作者刻意只做 scale-only calibration，避免在 tiny regime 同时拟合 shift 带来的不稳定。

## 关键结果

### 主结果与强基线

- **Zero-shot relative（Table 1）：** DepthART-L 在 <50M 参数模型中 ETH3D $\delta_1=0.958$ 最佳，DIODE-Full AbsRel 0.208 优于 Depth Anything v2-L 的 0.230；Metric3D v2-L 仍精度最高但为 411.9M/452.54ms。
- **Metric transfer（Table 2）：** NYUD 微调后 DepthART-L 在 iBims-1 0.747/0.646、SUN RGB-D 0.847/0.326；KITTI 微调后在 DDAD 0.867/6.340、ETH3D Outdoor 0.258/5.794。所有结果是不做重缩放的直接预测。
- **设备效率（Table 6）：** A6000 严格 FP32，$224^2$ S/B/L 为 347/298/191 FPS，$448^2$ 为 245/204/124 FPS；Orin NX $224^2$ TF32 为 102/86/55 FPS。

### 消融到底说明了什么

- **冻结是 transfer 的因果开关：** full FT 在 NYUD 达 0.928/0.328，却在 iBims 只有 0.572/0.844；冻结 + CamAdp + MQSH 达 0.924/0.340 与 0.713/0.693。
- **两个模块互补：** 去掉 CamAdp 或 MQSH，iBims 分别降至 0.534/0.879、0.544/0.866。
- **融合方式有语义差异：** encoder cross-attention 显著优于 additive 和 Concat+Proj，说明 camera prompt 需要 query-conditioned selective reading，而不是简单加法。
- **BRDS 的预算效应：** 0.5M 时长尾覆盖不够，BRDS 某些指标略输 K-Means；1.0M+ 后 BRDS 稳定领先，说明去偏策略需要最低数据支撑。

## 深度分析

### 真正贡献是什么

真正贡献不是 TinyViM 或 DPT，而是提出一个可部署的训练制度：**在蒸馏阶段控制输入分布，在度量阶段限制可训练自由度。** 这把“foundation model → tiny model”从单纯 knowledge distillation 改写成 transfer-preserving training。BRDS 解决 student 被高频图像模式占满容量；CamFT 解决 metric label 让 student 覆盖旧 geometry。

### 为什么结果成立

1. tiny encoder 容量越小，数据频率越容易替代场景因果线索；VAE latent 的全局视觉因素比 object-centric embedding 更适合找摄影/相机偏置。
2. metric depth 的 scale 确实依赖相机，直接让 tiny trunk 在 NYUD/KITTI 上全参数适配会把相机特定统计写回几何表示；冻结 trunk 将 domain-specific correction 限制到 adapter/head。
3. 单一 scale 预测容易被局部纹理干扰，MQSH 用隐式 ensemble 聚合布局、FoV、大平面等互补线索，平均降低方差。

### 容易误读的地方

- “接近大型模型”主要成立于部分 benchmark/指标，不是全面超过 Metric3D 或 Depth Anything；Table 1 的 latency 不是严格同分辨率 apples-to-apples，作者也明确说明这一点。
- Table 2 的 metric transfer 依赖已知内参，且 fine-tuning 只在 NYUD v2/KITTI，不能等同于通用 metric foundation model。
- BRDS 的 44M→1.7M 是数据选择，不是完整数据去重或保证语义均衡；VAE latent 的偏置也可能被采样器继承。
- 论文是 2026 arXiv 版本，ACM conference/DOI 仍是模板占位符；代码虽声称发布，但本文未给出复现实验脚本细节。

### 复现注意点

- 需要 Stable Diffusion v1.5 VAE、Incremental PCA、大规模数据的访问权限、Depth Anything v2 Large teacher、TinyViM+DPT、A800 训练资源。
- 严格复现需区分 strict FP32（TF32 disabled）与 Orin 上 TF32-enabled FP32；不要把 native resolution FPS 与 $224^2$ 控制实验混报。
- 需要保存每一来源的 $\gamma$；正文只给出 $J=8,B=10$，没有逐数据源 reduction factor 表。
- CamFT 的随机缩放/裁剪改变有效内参，复现时必须同步更新 $K$，而不是只增强 RGB。
- metric 结果禁止 post-hoc scale/shift，评估 mask、Eigen crop、最大深度 $d_{max}$ 都要与论文设置一致。

## 局限

1. CamFT 仍是单数据集 fine-tuning，不是 UniDepth/Metric3D 式大规模 metric training。
2. 假设相机内参已知；真实手机/机器人 metadata 缺失时需要 GeoCalib 类估计器。
3. 实验主要是离线 benchmark 和少量自采集定性结果，尚未证明长期视频、动态物体、极端低照度或强畸变下的稳定性。
4. 资源报告较完整，但 TensorRT/FP16 与严格 FP32 的比较跨硬件、功耗和编译栈，部署收益仍需目标设备复核。

## 我的笔记

这篇论文可放在“轻量 world geometry / embodied perception”的交叉位置。它给出的可迁移经验是：当模型小到不能同时容纳 general geometry 与 metric camera calibration 时，应该优先保护 representation，再把 calibration 外置到条件化小模块。对机器人世界模型而言，这比简单蒸馏一个大视频/深度模型更可操作：数据采样决定跨环境鲁棒性，冻结策略决定新相机/新传感器是否摧毁旧先验。

下一步值得做的实验：

- 在真实移动机器人多相机序列上比较 full FT、LoRA、CamFT 的长期漂移；
- 用估计内参而非 GT 内参，测 CamFT 的误差曲线；
- 将 BRDS 的 VAE density 与深度/相机元数据联合分层，验证“视觉偏置”与“几何偏置”是否一致；
- 测动态场景中边界稳定性，而不只测静态 benchmark。

## 引用

```bibtex
@article{xue2026depthart,
  title={DepthART: Scaling Foundation Monocular Depth to Tiny Models},
  author={Xue, Feng and Chen, Wu and Zhao, Mingshuai and Zhong, Guofeng and Ming, Anlong and Wang, Haozhe and Lei, Dianqiao and Lin, Zhaowen and Zhang, Haiyang and Sebe, Nicu},
  year={2026},
  eprint={2607.17099},
  archivePrefix={arXiv},
  primaryClass={cs.CV}
}
```
