---
tags:
  - papers/WorldModel
  - data-engine
  - sim-anchored
  - roadmap
aliases:
  - 成对数据引擎
  - Sim-WAM paired data
date: 2026-07-17
status: design-spec
---

# 数据引擎：仿真器与视频模型的成对数据设计

> 配套文档：[[insight]]（总体方案）、[[mini_pipeline]]（执行路线）、[[paper_insight]]（跨论文修订，本文已吸收其洞见四的修正）。本文回答一个问题：**成对数据到底是什么、怎么产出、怎么存**。

## 1. 核心概念：配对的键是 (初始状态, 动作序列)

"成对"不是两份数据集，而是同一个键 $(s_0, a_{0:H})$ 下的两份"未来"：

$$
(s_0, a_{0:H}) \;\Rightarrow\;
\begin{cases}
\text{仿真器重放} \to \tilde o_{1:H},\ s_{1:H} & \text{物理 GT（帧 + 特权状态）}\\
\text{视频模型预测} \to \hat o_{1:H} & \text{模型的想象}
\end{cases}
$$

让这件事成立的是仿真器独有的能力：**任意时刻的完整物理状态可以精确保存与恢复**（`env.set_state_dict()`），因此"从同一起点重放同一动作"是免费操作——这是真实世界永远做不到、本方案全部依赖的一点。

两个阶段用到配对的方式不同：

| 阶段 | 配对形态 | 视频模型是否参与 | 用途 |
|---|---|---|---|
| A. 训练数据 | 渲染帧 = 视频半边，物理状态 = GT 半边，一次重放全出 | 否 | 训练（流匹配 + 状态/深度/接触监督） |
| B. rollout 裁决 | 模型生成 vs sim 从同一 $(s_0,a)$ 重放 | 是 | 在线 critic 偏好对、评测指标 |

## 2. 阶段 A：训练数据引擎（一次重放，两半全出）

### 2.1 流程

1. **拿轨迹**：ManiSkill 官方 demo（h5，含每步 `env_state` 与 `action`）：
   ```bash
   pip install mani_skill
   python -m mani_skill.utils.download_demo "PushCube-v1"
   ```
2. **重放渲染**：`replay_trajectory` 指定相机/分辨率/域随机化重渲染；同一循环里顺手读特权信息；
3. **扰动注入（不可省，见 §4）**：按概率把重放动作替换为加噪版本，覆盖失败与恢复；
4. **落盘**：每条轨迹一组文件（schema 见 §2.2）。

### 2.2 存储 schema（每条轨迹）

```
trajectory_00042/
  frames.mp4            # 256×256 @ 控制频率（20 Hz），视频模型的输入与目标
  meta.json             # 任务、相机内外参、随机化配置、控制频率
  data.h5:
    actions       [T, d_a]     # 动作条件
    env_states    [T, ...]     # ★ 每步完整物理状态——阶段 B 的命脉
    qpos/qvel     [T, d_q]     # 机器人关节态
    object_poses  [T, K, 7]    # 状态一致性头监督（位置 + 四元数）
    contacts      [T, ...]     # 接触事件（接触头监督）
    depth         [T, H, W]    # 几何一致性监督（可低分辨率存）
    seg_masks     [T, H, W]    # 评测时初始化追踪器用
    is_perturbed  [T]          # 扰动标志位（行为克隆类损失要排除扰动步）
    is_success    scalar       # 轨迹级结果标签
```

要点：
- **`env_states` 每步都存**——这样任何训练窗口都能从它的起点精确重仿真，配对是逐窗口随取随算的，不需要预生成"配对数据集"；
- 训练窗口切法：`(上下文 1–4 帧, 16 步动作) → 16 帧未来`，一帧对一动作（§5 铁律 2）；
- 存储估算：21k 条 × ~100 步，mp4 + h5（depth 降采样存）约 150–250 GB。

## 3. 阶段 B：模型 rollout 与 sim 的配对（critic / 评测）

```python
# 键：窗口起点状态 s0（从 data.h5 的 env_states 取）、动作块 a、上下文帧 o_ctx
pred_frames = video_model.generate(o_ctx, a)      # 模型的未来（低步数采样即可）

env.reset(); env.set_state_dict(s0)               # 恢复到同一初始物理状态
for a_t in a:
    obs, *_ = env.step(a_t)                       # 重放同一动作
    gt_frames.append(env.render())
    gt_poses.append(get_object_poses(env))
    gt_contacts.append(get_contacts(env))

# 偏差 → 序数化（paper_insight 洞见二：不做数值回归）
scores = physics_divergence(pred_frames, gt_frames, gt_poses)   # 漂移/穿透/末态
pairs  = build_preference_pairs(rollouts, scores)               # sim 一致 ≻ 幻觉
```

- GPU 并行 sim 下几千个窗口一批重放，成本相对扩散训练可忽略（mini_pipeline 的"1 卡常驻 critic"分工承接此处）；
- 同一段代码即评测协议：漂移（CoTracker 对 GT 投影轨迹）、末态正确率（mask IoU / 中心距）、穿透事件——外加 GPC 式"真值 sim 规划上界"给模型误差定价。

## 4. 扰动注入配方（洞见四的强制修正 ⚠️）

ManiSkill demo 全部是运动规划生成的**成功轨迹**——直接用它训练，模型没见过"坏动作的后果"，裁决能力恰好缺失（SimDist：等量纯专家数据 0.90→0.10；GPC：去掉探索数据掉约 10 点）。照抄 SimDist 配方：

- **轨迹级**：以概率 $p\approx0.5$ 选中一条 demo 做扰动版重放（原版照存，两版都要）；
- **时间连续噪声窗**：扰动不是逐步独立噪声，而是在随机区间内持续注入——操作任务噪声窗 $U[1,5]$ 步、无噪窗 $U[5,10]$ 步交替；每条轨迹独立采样对角高斯协方差；
- **目标占比**：专家动作占比压到 40–60%（SimDist 操作数据仅 36% 为最优动作；GPC 扰动数据是演示的 6 倍）；
- **标注**：`is_perturbed` 逐步记录——视频/状态预测损失对全部步生效，任何模仿类目标只吃未扰动步。

## 5. 两条对齐铁律（写代码前钉死）

1. **确定性**：同一 $(s_0, a)$ 重放两次必须逐位一致——固定 sim substep 数、physx 求解器迭代数，关掉一切重放路径上的随机源；上线前先做"重放两遍 diff 状态序列"的自检；
2. **一帧一动作**：渲染帧率 = 控制频率（20 Hz），暂不做任何时间压缩/latent 帧聚合——配对键干净，等方法验证后再考虑 DreamZero 式压缩对齐。

## 6. 实施清单

| 交付物 | 内容 | 规模 |
|---|---|---|
| `data_engine.py` | demo 下载→扰动重放→按 §2.2 落盘 | ~300 行 |
| `sim_judge.py` | set_state 重放 + 偏差指标 + 偏好对构造（§3） | ~200 行 |
| 自检脚本 | 确定性 diff、扰动占比统计、随机抽帧目检 | ~100 行 |

任务顺序照 [[mini_pipeline]]：PushCube 1k 条调通 → PickCube/StackCube 各 10k。`sim_judge.py` 同时就是 Step 0 存在性报告与 Idea 3 物理一致性基准的度量核心——一次投入三处复用。
