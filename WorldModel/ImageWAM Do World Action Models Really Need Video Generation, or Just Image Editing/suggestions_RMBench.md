---
title: ImageWAM · RMBench 5k 全失败后的建议
date: 2026-08-13
tags:
  - ImageWAM
  - RMBench
  - Eval
  - Memory
---

# ImageWAM · RMBench 5k 全失败后的建议

> [!abstract] 结论
> 1. **先别把 5/5 失败主要归到「没加 \(t{-}32\)」。** 更可能是 **5000 step 不够**。改评测指令 **救不了这次**：`battery_try` 的 seen / unseen / 训练句是同一句，上次 5/5 已经在用它。
> 2. Train loss 收敛只说明 **16 步短窗 FM** 拟合好了，不说明 400 步闭环会做 `battery_try`。
> 3. RMBench 是 \(M(n)\) 记忆任务，当前 ImageWAM 几乎只看「现在这一张拼图」，记忆通道确实偏弱。
> 4. 若确认失败模式是「同一错误朝向反复试」，下一刀加 **episode 第 0 帧当第二张 ref**，**不要**照抄 WLA 的 \(t{\pm}32\)。
> 5. 加历史必须重训；别指望在 5k ckpt 上插两张图就变好。

对照笔记：[[WLA vs ImageWAM]]。核对日期：2026-08-13。

本次事实（teleai）：

| 项 | 值 |
|---|---|
| 任务 | RMBench `battery_try`（\(M(n)\)） |
| 训练 | 约 **5000 / 30000** step，4 卡 FLUX2-4B，`endpoint_frames_only`，窗 16 |
| 训练语言 | 写死 `override_instruction`（与下面 seen/unseen **同一句**） |
| 评测记录 | `/data_wj/WAM/RMBench/eval_result/battery_try/imagewam_policy/demo_clean/.../step_005000.pt/2026-08-12 07:10:51/` |
| 评测设定 | `Instruction Type: unseen`，5 ep，seed 100004–100017，**SR=0**，每条 `episode*.mp4` 均为 100 s |
| 评测脚本默认 | `INSTRUCTION_TYPE=unseen`（WLA 官方评测默认也是 unseen），`horizon=16`，`replan=8` |

---

## 1. 为什么「loss 好、eval 全挂」还很正常

ImageWAM 的 train loss 是窗内：

- 图像：对 **\(t{+}16\) 拼图** 学 \(v=\varepsilon-x_0\)
- 动作：同一 16 步上的 flow matching

它可以掉得很低，闭环仍然崩，因为：

- 评测是 **短窗滚动到 ~400 环境步**，训练从未监督整条 episode；
- 误差会沿 replan 累积；
- `battery_try` 还要求记住更早的尝试，当前帧里经常已经没有那次信息。

WLA 在 RMBench 上 ~800 step 时 train loss 也同样已经很好看。短窗 FM 好看 ≠ 会做任务。5k 只是官方/计划预算 30k 的 **1/6**，还不能下「方法不行」或「必须加历史」的结论。

---

## 2. 「改成和训练同一句」不可行，也和 WLA 官方评测不是一回事

**和 WLA 对齐吗？** 不。WLA 评测默认同样是 `INSTRUCTION_TYPE=unseen`（`experiments/rmbench/_run_rmbench_eval_impl.sh`）。WLA 训练用 `rmbench_seen_instruction.json` 里那一句；评测走 RMBench 的 `get_instruction()`。官方对照应两边都报 unseen，不是把 ImageWAM 改成 seen。

**改指令会比上次评测好吗？** 对 **这次 `battery_try`：不会。** 服务器上 RMBench 全部 task json 的 `seen` 与 `unseen` **字符串完全相同**。`battery_try` 三处是同一句：

```text
There are two batteries and a battery slot on the table.
Combining the two batteries in different orientations causes the dashboard needle to rotate.
```

这句同时是：训练 `override_instruction`、WLA `rmbench_seen_instruction.json`、RMBench `seen`、RMBench `unseen`。  
上次 `_result.txt` 已经写着 `Instruction Type: unseen`，模型听到的就是训练句。把 `unseen` 改成 `seen` 是 **空操作**。

计划里「train 用 ID、eval 用英文」那条错配，在 **当前这套配方上没有发生**（训练已经 override 成这句英文）。那是防以后写错，不能拿来解释这 5/5。

**还剩的便宜实验：** `REPLAN_STEPS=8 → 16`（与训练窗对齐）。5 条都跑满 100 s 且全 Fail，单靠 replan 把 0 拉成可用 SR 的希望很小，可以当对照，不要当主因。

5 次太少，只能排障，不能当正式 SR。录像在上述目录的 `episode0.mp4`–`episode4.mp4`。

---

## 3. 用失败样子决定下一步

| 录像里的样子 | 更像什么 | 下一步 |
|---|---|---|
| 夹不到、对不齐、乱甩 | 动作 / 视觉还没学好 | **接着训到 15k–30k**，先别改 Dataset |
| 动作像样，但同一错误朝向反复试、不记得已经试过 | \(M(n)\) 记忆不够 | 加 **begin-frame 第二 ref** 后重训 |

`battery_try` 两种都会以「没装进槽」收场，不看录像分不清。

---

## 4. 要不要加历史和第一帧

**对这个任务：值得加，但不要照抄 WLA。**

同一 RMBench 上，现在的 ImageWAM 几乎是马尔可夫的：每次 replan 只看 **当前三相机拼图 + 一句固定话**。试错过的朝向、初始摆场，当前帧里经常没了。这和 \(M(n)\) 对得上。WLA 只在 RMBench yaml 里开了 begin + `history_obs_step=32`，不是随便加的。

但 ImageWAM 是 **1 张 ref → 1 张未来** 的图像编辑，不是 WLA 那种多图进 VLM。

| 加什么 | 和 ImageWAM 契不契合 | 建议 |
|---|---|---|
| **episode 第 0 帧当第二张 ref** | 很契合：初始摆场 + 现在 → 未来 | **优先做** |
| **\(t{-}32\) 再解一路视频** | 打破 `endpoint_frames_only`、\(T=2\)，解码更贵 | 先别做 |
| WLA 式 subtask 语言历史 | 要加 LM 头和标注 | 除非做 WLA 对照实验 |

第一帧解决的是「任务一开始长什么样」（非局部）。\(t{-}32\) 大约只覆盖 1 秒，**盖不住** 几十秒前那次失败尝试。记忆若是瓶颈，begin 比 \(t{-}32\) 值钱。

也不要为了「任务有 400 步」去拉长训练窗。400 是环境 `step_lim`；变长靠滚动 replan。ImageWAM 训 16、WLA 训 32，两边都是短窗。见 [[WLA vs ImageWAM]]。

加了记忆通道必须 **重训**。不要在 5k 权重上只改 Dataset 就评。

---

## 5. 建议顺序

1. **5k ckpt + 对齐评测**：同句 instruction、`replan=16`，并看失败录像。
2. 操作烂 → 把 4–7 卡那次跑满 **15k–30k**，暂不改协议。
3. 反复同一错 → ImageWAM 里加 **begin-frame 第二 ref**，保持 endpoint \(t\) / \(t{+}16\) 和 16 步动作，再训。
4. 不要把未来 endpoint 监督误叫成历史记忆（计划里写过的坑）：\(t{+}16\) 是要生成的目标，不是过去。

**一句话：** 5/5 先当「训不够 + 评测可能不一致」；RMBench 上 **加第一帧当第二条件** 是对的下一刀，**不要**为了 400 步去抄 WLA 的 \(t{-}32\)。
