---
tags:
  - papers/WorldModel
  - roadmap
  - sim-anchored
  - mini-pipeline
aliases:
  - Sim-anchored WAM 最小验证路线
date: 2026-07-16
status: action-plan
compute: 4xH100-80G
---

# Mini Pipeline：Sim-anchored WAM 的最小化验证路线（4×H100 版）

> 配套设计文档见 [[insight]]。本文回答三个问题：**用什么数据、什么视频模型、什么仿真器**，以及一条零经验也能走通的阶梯路线——每一步都有明确交付物和"给 mentor 的一句话"，走完 Step 0 你就有底气了。

## 0. 先定心：为什么这条路走得通

你不需要一上来就"训练一个强大的 world action model"。整条路被拆成 5 级台阶，**每级 2–3 周、有独立可展示的结果**，且前两级几乎不可能失败（Step 0 不训练任何模型，Step 1 是复现成熟做法）。真正有风险的创新点被推迟到 Step 2/3，而那时你已经有了完整的数据引擎、训练管线和评测脚本兜底——即使创新点效果一般，Step 0–1 的产出本身就是一份合格的阶段性工作。

**三个"不要"（新手最容易在这里烧掉两个月）：**
1. **不要先碰 Isaac Lab / Omniverse**——安装配置极重，等需要更高保真度时再迁移；
2. **不要先碰 14B 模型**——DreamZero 的 14B 结论不需要你复现，1–5B 足够验证方法论，4×H100 也养不起 14B 全参训练；
3. **不要先碰真实机器人数据**——real2sim 对齐是单独的坑，放到 Step 4。MVP 全程 sim-native，GT 免费且完美。

## 1. 三大选型（直接抄这个默认值）

### 1.1 仿真器：ManiSkill3 ✅

| 候选 | 结论 | 理由 |
|---|---|---|
| **ManiSkill3**（SAPIEN） | **✅ 默认选择** | `pip install mani_skill` 一行装好；GPU 并行仿真+渲染（单张 H100 上数千 env）；官方提供可下载、可重放的 demo 轨迹；物体位姿/接触/分割/深度 API 齐全——[[insight]] §3.3 的"GT 监督包"全部免费拿到 |
| Isaac Lab | ❌ 暂缓 | 功能最强但安装/学习成本高，Step 4 以后再考虑 |
| MuJoCo (robosuite/LIBERO) | 🔶 备胎 | 若 ManiSkill GPU 渲染在集群上有兼容问题就退到这里；LIBERO 也有现成 demo 数据 |

- 仓库：https://github.com/haosulab/ManiSkill ，文档 https://maniskill.readthedocs.io
- 关键机制：官方 demo 是"轨迹文件"（h5，含 states + actions），用 `mani_skill.trajectory.replay_trajectory` 重放时可以**任意指定相机、分辨率、随机化外观**重新渲染——这就是天然的"同一动作轨迹 → 配对视频+状态 GT"数据引擎，你几乎不用写数据生成代码。

### 1.2 任务与数据：ManiSkill3 三个刚体任务，sim-native 全配对

| 任务 | 角色 | 规模 |
|---|---|---|
| `PushCube-v1` | 调试任务（最简单，平面推动） | 1k 条，先把管线跑通 |
| `PickCube-v1` | 主任务（抓取+移动） | 10k 条 |
| `StackCube-v1` | 难任务（接触丰富，video model 最容易穿透/漂移的场景） | 10k 条 |

**数据规格（定死，避免反复纠结）：**
- 分辨率 256×256，单相机（先别搞多视角），控制频率用环境默认（20 Hz）
- 每条轨迹存：mp4（或帧序列）+ h5（actions、机器人关节态、**物体 6D 位姿序列、接触标志、深度图、分割 mask**）
- 域随机化：桌面纹理、光照、相机小扰动、物体颜色——重放渲染时开关即可
- 训练窗口：上下文 1–4 帧 + 预测 16 帧，动作条件 = 对应 16 步动作（先做 1 帧对 1 动作，别学 DreamZero 的 latent 时间压缩对齐，那是优化不是必需）
- 存储估算：21k 条 × ~100 帧 × 256²，mp4 + h5 约 100–200 GB，集群盘上完全可行
- 数据生成成本：ManiSkill GPU 并行下，占用 1 张 H100 半天内可完成全部渲染

### 1.3 视频模型：4×H100 下的定案

| 阶段 | 选型 | 理由 |
|---|---|---|
| **Step 1–3 主力** | **✅ Wan2.1-T2V-1.3B 全参微调**（https://github.com/Wan-Video/Wan2.1） | 4×H100 上全参微调 + 大 batch 很从容，迭代一轮实验 1–2 天；与 DreamZero 同为 Wan 家族 DiT+流匹配，你在 1.3B 上验证的损失设计可直接声称"可随骨干放大" |
| Step 3 后的规模验证（可选） | Wan2.2-TI2V-5B，FSDP + gradient checkpointing 全参（紧）或 LoRA（松） | 方法在 1.3B 上验证成功后，用 5B 复跑最优配置一次，证明结论不随规模翻转；4×H100 可以做，但别用它做日常迭代 |
| 快速原型脚手架（可选） | IRASim（https://github.com/bytedance/IRASim） | 开源的"轨迹→视频"动作条件模型，代码可直接抄动作注入与评测部分 |

**动作条件化的最小改法**（对 Wan）：动作块 $a_{l:l+16}\in\mathbb{R}^{16\times d_a}$ 过一个 2 层 MLP 编码成 16 个 action token，**与文本 token 拼接后走原有 cross-attention**。改动量小、不动骨干结构、加载预训练权重不冲突。文本固定为任务模板句或直接置空。

**4×H100 的分工建议**：3 张训练 + 1 张常驻"数据/评测/critic"卡（跑 ManiSkill 重放、CoTracker、IDM 探针、Step 3 的在线采样）——这样评测和 critic 永远不阻塞训练迭代。

## 2. 阶梯路线（总计 ~11 周到第一个可发表证据）

### Step 0（第 1–2 周）：不训练，先让问题自己开口 —— "存在性报告"

**做什么：**
1. 装 ManiSkill3，下载官方 demo，跑通 replay_trajectory，产出 1k 条 PushCube 配对数据（视频+状态 GT）——顺便验收 §1.2 的数据规格；
2. 拿**现成的** Wan I2V（或任何开源 I2V）对 sim 场景首帧生成"未来"，人工 + 简单脚本统计物理错误：物体消失/复制、穿透、无动作漂移；
3. 写 1 页报告 + 一张失败案例九宫格。

**交付物**：数据引擎脚本（以后一直用）+ 存在性报告。
**成功标准**：能稳定批量产出配对数据；报告里有量化的幻觉率。
**给 mentor 的一句话**：*"我量化了现成视频模型在受控场景下的物理错误率是 X%，这是我们方法要打的靶子，配对数据引擎已就绪。"*
> 这一步没有任何训练、没有任何可以"失败"的环节，但它给了你（和 mentor）继续投入的证据。底气从这里来。

### Step 1（第 3–5 周）：复现最小动作条件视频模型（无创新，纯执行）

**做什么**：Wan2.1-1.3B + action token 注入，在 PushCube 1k → PickCube 10k 上微调，目标只有原始流匹配损失（= [[insight]] §4.4 的 S1 但不加任何 sim 约束项，先立 baseline）。

**交付物**：baseline checkpoint + 训练/推理脚本。
**成功标准（三个测试，全是脚本可跑的）：**
1. **换动作测试**：同一首帧、两条不同动作 → 生成视频肉眼可见地跟随各自动作；
2. **IDM 探针**：用 sim 数据另训一个小 inverse dynamics model，从生成视频反推动作，与条件动作的误差显著低于随机基线；
3. 视觉质量 PSNR/FVD 在合理范围（和 GT 渲染帧比）。

**给 mentor 的一句话**：*"动作条件视频模型 baseline 已立起来，模型确实在'听'动作，接下来所有 sim 约束都和它 A/B 对比。"*

### Step 2（第 6–8 周）：加入 sim-GT 约束 —— 核心主张的第一个证据 ⭐

**做什么**：在 Step 1 之上加两个约束项（见 [[insight]] §4.3）：
1. **状态一致性头**：从生成潜变量回归物体 6D 位姿，用 h5 里的 GT 位姿监督（$\lambda_s$）；
2. **深度一致性**：轻量深度头对 GT 深度图（$\lambda_g$）。
接触头（$\lambda_e$）作为加分项，时间不够就砍。

**评测（就用这三个指标，Step 0 的数据引擎全部支持）：**
| 指标 | 怎么算 |
|---|---|
| 物体轨迹漂移 | 用 GT 初始 mask + CoTracker（https://github.com/facebookresearch/co-tracker）在生成视频里追踪物体，对比 sim GT 位姿的 2D 投影轨迹，报告像素漂移 |
| 末态正确率 | 生成视频最后一帧里物体是否到达 sim GT 末态位置（mask IoU / 中心距离阈值） |
| IDM 动作跟随误差 | 同 Step 1，确认加约束没有牺牲动作跟随 |

**成功标准**：漂移 ↓、末态正确率 ↑，且 FVD 不明显变差。
**给 mentor 的一句话**：*"同骨干同数据下，把 sim 从'数据源'升级成'结构化监督'，物理一致性提升了 X%——这就是我们区别于 Cosmos 式用法的净贡献。"*

### Step 3（第 9–11 周）：sim 在线 critic + 偏好优化 —— 可发表点 ⭐⭐

**做什么**（[[insight]] §4.2 的最小实现）：
1. 用 Step 2 模型在训练集场景上自采样生成（低步数即可，用那张常驻评测卡）；
2. sim 从相同初始状态重放相同动作 → 拿 GT；CoTracker/状态头量出偏差；
3. 偏差大的样本构成偏好对（sim 一致 ≻ 模型幻觉），做流匹配版 DPO（不需要偏差可微，工程上最稳）；
4. 报告模型**自身错误分布**上的幻觉率下降。

**成功标准**：在 Step 2 已收敛的模型上，幻觉率进一步显著下降（这证明 critic 覆盖了数据监督覆盖不到的错误）。
**给 mentor 的一句话**：*"sim 不只当老师批改作业里的题，还在批改模型自己犯的错——这是方法论上真正的新东西。"*

### Step 4（之后，与 mentor 商定方向）：二选一

- **A. Real-anchored**：引入 DROID/Bridge 真实数据子集 + real2sim 状态估计（[[insight]] §4.1 模式 B），证明约束能迁移到真实视觉分布；
- **B. 下游 policy / RL**：接 IDM/action head 做闭环任务评测；或走 §6 的方向——把这个物理可靠的 WAM 当作 agent 的训练环境。

## 3. 消融矩阵（论文的表 1，从 Step 1 起就按这个存 checkpoint）

| # | 配置 | 对应 |
|---|---|---|
| 1 | baseline：仅流匹配 | Step 1（= sim 只当数据源） |
| 2 | + 状态/深度一致性 | Step 2 |
| 3 | + 在线 critic 偏好 | Step 3 |
| 4 | 2+3 全开 | 最终模型 |

行 2−1 和 3−2 的增益就是"**sim 作为约束 > sim 作为数据**"这一核心主张的直接证据。

## 4. 风险与退路（每一步都有 Plan B）

| 风险 | 退路 |
|---|---|
| ManiSkill GPU 渲染在集群上装不起来 | 退 CPU 渲染（数据生成变慢但可离线攒）或退 LIBERO/MuJoCo |
| Wan 1.3B 微调不收敛 | 先 LoRA 找超参再放开全参；或退 IRASim 小 DiT 从头训 128px——方法论验证不依赖大骨干 |
| 状态头学不好（Step 2 无增益） | 先只用深度/CoTracker 一致性这种 2D 信号；或把位姿监督从潜变量回归改成对生成帧跑冻结位姿估计器 |
| DPO 训崩 | 退化为难例重加权（[[insight]] §4.2 的第二种用法），不改损失只改采样 |
| 时间不够 | Step 0–2 就是一个自洽的 workshop 级故事；Step 3 是主会级增量 |

## 5. 本周就能做的三件事

1. 在集群上 `pip install mani_skill`，跑通官方 PushCube demo 下载 + replay 渲染（半天）；
2. 按 §1.3 的 4×H100 分工方案申请/锁定卡位，写进周报；
3. 把 Step 0 的"存在性报告"排进接下来两周的日程，作为第一次正式汇报。

## 6. 这个项目与 3D agentic RL 的关系（写给自己，也可以讲给 mentor）

这个课题不是 3D agentic RL 的岔路，而是它的**基础设施**，三条通路：

1. **World model 就是 agentic RL 的环境**。3D agent 做 RL 最贵的是环境交互；一个物理可靠的 WAM 正是"可以在里面训 agent 的学习型环境"（Dreamer 一系的 imagination training 走的就是这条线）。你现在做的"用 sim 把 WAM 的物理修可靠"，恰恰是让 world model 能承担 RL 环境职责的前提——物理不可靠的世界模型训出的 agent 学的是幻觉。
2. **技能栈完全重叠**。这条 pipeline 会让你精通：GPU 并行仿真器（3D agent 的标准训练场）、偏好优化/DPO（agentic RL 的核心工具族）、世界模型评测。做完 Step 3，你就是组里同时懂 sim、懂视频世界模型、懂偏好优化的人——这正是 3D agentic RL 需要的人。
3. **自然的接续课题**。Step 4B 之后有一个顺理成章的 proposal 可以主动提给 mentor："在 sim-anchored WAM 里训练 3D agent，用 sim 做 verifier 的 agentic RL"——到那时你是带着自己搭好的环境和证据去谈方向的，而不是空手请求换题。

**一句话**：先把 mentor 的题做成你的地基，再在地基上盖你想盖的楼。

## 附：关键仓库清单

- ManiSkill3：https://github.com/haosulab/ManiSkill
- Wan2.1：https://github.com/Wan-Video/Wan2.1
- IRASim：https://github.com/bytedance/IRASim
- CoTracker：https://github.com/facebookresearch/co-tracker
- DreamZero（协议参考）：https://github.com/dreamzero0/dreamzero
