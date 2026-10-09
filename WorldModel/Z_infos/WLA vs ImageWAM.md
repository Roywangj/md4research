---
title: WLA vs ImageWAM 在 RMBench 上的差别
date: 2026-08-13
tags:
  - WorldModel
  - WLA
  - ImageWAM
  - RMBench
  - Dataset
  - FlowMatching
---

# WLA vs ImageWAM 在 RMBench 上的差别

> [!abstract] 阅读结论
> 1. **盘上的 RMBench 是同一份**（`RMBench-LeRobot/.../aloha-agilex_clean_50`，三路 AV1，30 fps，14 维动作）。两边 Dataset 取出来的样本 **不是同一种东西**。
> 2. **世界模型头都站在 ImageWAM 这条线**：监督「当前图 → 一张未来图」的 2D flow matching，**不是** Fast-WAM 那种多帧视频 DiT。
> 3. 预测起点两边都是当前时刻 \(t\)。WLA 额外把 **episode 第 0 帧** 和 **\(t-32\)** 喂给 RynnBrain 当上下文；ImageWAM 只有 \(t\) 与 \(t{+}16\) 一对端点。
> 4. 图像 FM 的速度场定义一样：\(x_\sigma=(1-\sigma)x_0+\sigma\varepsilon\)，\(v=\varepsilon-x_0\)。差在 \(x_0\) 是哪张图、条件是什么、\(\sigma\) 怎么采。动作 FM 的 \(t\) 方向两边写反了。
> 5. ImageWAM 在同一台机、同一份 AV1 上没炸 host 内存，不是数据更友好，而是 **每条样本解码跨度短、worker 少、并且专门 close / malloc_trim**。

核对日期：2026-08-13。以本地代码为准：

| 仓库 | 路径 | 本次对照的配置 |
|---|---|---|
| WLA | `/Users/roywangj/journey_wj/research/author/WAM/WLA` | `configs_wj/rmbench_battery_try_image_action_language.yaml` |
| ImageWAM | `/Users/roywangj/journey_wj/research/author/WAM/ImageWAM` | `configs/data/rmbench_wla_v3.yaml` + `configs/task/rmbench_battery_try_flux2_klein_4b_base_imagewam.yaml` |
| 数据 | teleai `/data_wj/dataset_wj/WAM/RMBench-LeRobot/battery_try/aloha-agilex_clean_50` | 50 条 episode，三相机 `cam_high` / `cam_left_wrist` / `cam_right_wrist`，AV1，240×320 |

本文 **不** 把 Fast-WAM 当成 RMBench 对照（Fast-WAM 仓库里没有 RMBench Dataset）。它只在第 6 节用来标「真视频头」那条线。

---

## 1. 一句话定位

```text
同一份 RMBench 录像
        │
        ├─ WLA       主相机 t / t±32 + episode 开头
        │            RynnBrain 看多张独立图
        │            Sana 2D 预测主相机 t+32 那一张
        │
        └─ ImageWAM  三相机拼图的 t 与 t+16
                     FLUX.2 把当前拼图当 ref，预测终点拼图
```

两边都是 **图像世界模型 + 动作头**，不是视频世界模型。ImageWAM 配置里的 `video: [C, T=2, H, W]` 和 `lambda_video` 只是接口命名；RMBench 配方开了 `endpoint_frames_only`，\(T=2\) 就是「现在 / 未来」两张静图。

---

## 2. Dataset：同一份文件，两套取样本协议

### 2.1 总表

| | **WLA** | **ImageWAM（teleai 4–7 卡那份）** |
|---|---|---|
| 封装 | 官方 `MultiLeRobotDataset` + `dataset.py` wrapper | 自研 `RobotVideoDataset` + 仓库内 LeRobot v3 adapter |
| backend | 写死 `pyav` | 也是 `pyav`，但会 `container.close()` + worker 里 `malloc_trim` |
| 解哪些相机 | `delta_timestamps` **只有主相机** `cam_high`；腕部当辅助静帧 | **三路都解**：high + left + right |
| 一次取几帧 | \(t-32\)、\(t\)、\(t+32\)，再单独解 episode 第 0 帧 | `endpoint_frames_only`：17 帧窗的第 0 与第 16 帧 |
| 模型看到的图像 | 若干张独立图：begin / history / current / 一张 512 的未来图 | 三路拼成 RoboTwin compact 画幅，再变成 `video: [C, T=2, H, W]` |
| 动作长度 | `chunk_size=32` | `num_frames-1=16` |
| 语言 | `rmbench_seen_instruction.json` 随机抽 + 按段拼 `subtask_text` | 任务级写死一句 `override_instruction`，Qwen3 embedding 可走 cache |
| 归一化 | `configs/norm_stats.json` 的 `rmbench_battery_try` | `RMBench-ImageWAM-meta/.../dataset_stats.json` |
| 输出 key | `input_images`、`target_images`、`actions`、`caption`、subtask | `video`、`action`、`proprio`、`prompt`、text cache |

### 2.2 封装与解码后端

WLA 建集：

```1350:1355:dataset.py
    dataset = MultiLeRobotDataset(
        repo_ids=repo_ids,
        episodes=episodes,
        delta_timestamps=delta_timestamps,
        video_backend="pyav"
    )
```

走 pip 里的 `lerobot`：`__getitem__` → `_query_videos` → `decode_video_frames_torchvision` → `avcodec_open2(libdav1d)`。官方包关解码器不如 ImageWAM 彻底，也没有 glibc `malloc_trim`。

ImageWAM 走 `RobotVideoDataset`，`lerobot_backend: v3`，`lerobot_v3_video_backend: pyav`。自带 `video_utils.py` 在 pyav 路径上显式 `reader.container.close()`；`mem_tools.py` 注释写明 DataLoader worker 里 pyav buffer 会堆在 glibc arena，RSS 只涨不跌，所以定期 `malloc_trim`。

解码器是同一类（CPU 上的 libdav1d）。ImageWAM 多的是 **关句柄 + 把空闲页还给 OS**。

### 2.3 时间戳：WLA 解三段 + 开头，ImageWAM 只解两端

WLA（fps=30，`chunk_size=32`，`history_obs_step=32`）：

```1325:1339:dataset.py
    common_ts = [0] + [
        model_args.chunk_size * i / (model_args.sample_num * ds_meta.fps)
        for i in range(1, model_args.sample_num + 1)
    ]
    ...
    if model_args.use_history_obs:
        common_ts.append(-model_args.history_obs_step / ds_meta.fps)

    delta_timestamps = {
        primary_image_key: list(common_ts),
    }
```

即主相机三个时刻：\(0\)、\(+32/30\)、\(-32/30\)。LeRobot 返回顺序是

```text
images[0]  = t        当前
images[1]  = t+32     未来
images[-1] = t-32     历史
```

另有 `EpisodeBeginFrameCache`，按 `(dataset_index, episode_index)` 再解一次该条 demo 的起始时间戳。

ImageWAM：

```yaml
num_frames: 17
endpoint_frames_only: true
image_obs_steps: 2
```

代码把图像时间戳收成 `[0, num_frames-1]`，三路相机各只要窗口首尾。动作取中间 16 步。

### 2.4 哪一帧是条件，哪一帧是要生成的

**预测起点两边都是当前的 \(t\)。** \(t-32\) 和 episode 第 0 帧不是 flow matching 的 \(x_0\)。

**ImageWAM**

```text
时间轴（三相机已拼成一张）

  t  =============================  t+16
  │                                  │
  video[:, 0]                        video[:, 1]
  当前拼图 → ref_image               未来拼图 → 加噪，预测 v = ε − x
  （条件，不加噪）                    （监督目标）
```

没有 \(t-32\)，没有单独的 episode 开头。一对一：现在 → 约 0.53 s 后。

**WLA**（`use_begin_frame_context: true`，`use_history_obs: true`）

| 角色 | 哪一帧 | 进哪 | 干什么 |
|---|---|---|---|
| 预测起点 / 当前观测 | **\(t\)** | `input_images` 里最后那张主相机图 | `current_image_index` 指这里；world expert 抽的是这张图的 visual token |
| 生成目标 | **\(t+32\)** | `target_images` | VAE 编码后加噪，学 \(v=\varepsilon-x_{t+32}\) |
| 历史上下文 | \(t-32\) | `input_images` 中间一张 | 只给 RynnBrain 看，不加噪、不当 FM 目标 |
| episode 初始帧 | 该条 demo 的 **第 0 帧** | `input_images` 第一张 | 同样只当语言/视觉背景 |

```text
episode 第 0 帧          t-32                 t                    t+32
    │                     │                   │                      │
    begin（额外条件）      history（额外条件）   当前 = 预测起点         要生成的图
    只进 MLLM             只进 MLLM            进 MLLM，且被选作        只进 Sana 监督
                                              world expert 的主条件
```

`encode_condition` 用 `current_image_index`（有 history 时是 2）去定位「当前图」那一段 `<|vision_start|>…<|vision_end|>`，这段 hidden 才接到 Sana。begin / \(t-32\) 仍在整段 MLLM 上下文里。

对照：

```text
              条件（现在）              要预测的未来
WLA           t   （另加 begin、t-32）   t+32   （约 1.07 s，只主相机 512）
ImageWAM      t   （三相机拼图）         t+16   （约 0.53 s，compact 拼图）
```

### 2.5 episode 第 0 帧是什么

LeRobot / RMBench 一条 **episode** = 一次完整演示。battery_try 的 `aloha-agilex_clean_50` 有 50 条，就是 50 次「把电池装进槽」的录像。

训练随机抽这条带子上的某个时刻当「现在」\(t\)。\(t\) 可以是第 50 帧，也可以是第 400 帧。

第 0 帧 **不是**「当前 index 减一个常数」，而是这条 episode 元数据里的起始时间戳：

```83:90:dataset.py
        timestamp = episode[f"videos/{self.image_key}/from_timestamp"]
        frame = decode_video_frames(
            video_path,
            [timestamp],
            ...
        )
```

`from_timestamp` = 这条录像在视频文件里的起点。解出来就是 **cam_high 在这次实验刚开始时的画面**：桌上电池和槽还在初始位置、夹爪还在 home。同一条 episode 里，无论 \(t\) 抽到中间还是末尾，**这张图不变**，所以按 episode 缓存（最多 50 张）。

假设这次 sample 抽到第 **400** 帧当 \(t\)：

| 名字 | 是哪一帧 | 会不会随 \(t\) 变 |
|---|---|---|
| episode 第 0 帧（begin） | 第 **0** 帧 | 整条 demo 固定 |
| \(t-32\)（history） | 第 **368** 帧 | 跟着 \(t\) 滑 |
| \(t\)（当前） | 第 **400** 帧 | 这次抽到的「现在」 |
| \(t+32\)（要生成的） | 第 **432** 帧 | 现在往后 32 步 |

若 \(t\) 很靠前（例如第 10 帧），\(t-32\) 越界，用 `is_pad` 丢掉 history；**begin 仍是第 0 帧**。

WLA 多喂这张图，是为了让 VLM 知道 **整条任务最初的场景**（电池一开始放哪），即使现在已经做到一半、镜头里局部变了。它不是 FM 起点。

### 2.6 相机与画幅

- WLA：只把 `cam_high` 放进 `delta_timestamps`，所以多时刻解码只发生在主相机。腕部若出现在 `auxiliary_image_key` 里，当作当前静帧拼进 `input_images`（`auxiliary_drop_thresh: 0.0`，默认不丢）。目标图 `target_image_size: 512`，条件图 256。
- ImageWAM：三路都解，再 `concat_multi_camera: "robotwin"` / `compact_288x256`：上 high、下左右腕并排，得到一张拼图 × 2 个时刻。世界模型看的是 **拼好的画布**，不是三张独立 token 流。

### 2.7 动作与本体感觉

- WLA：`action` 取 \(t\) 起连续 32 步，与图像跨度 \(t\to t+32\) 对齐。`observation.state` 进 `states`。`action_condition_type: no_action_condition`，图像头 **不用** 动作当条件。
- ImageWAM：动作 16 步，对齐两端点；`proprio` 与动作对齐后少最后一帧。动作和图像在同一套 MOT 里一起去噪。

### 2.8 语言

WLA 每个 sample：

1. 任务名去 `configs/rmbench_seen_instruction.json` 随机抽一句（5% 概率抽空，作 unconditional）。
2. 按 parquet 的 `subtask_text` 拼「历史段在干什么 / 接下来 32 步干什么」。
3. 后一段当 LM 监督（`language_loss`）。

ImageWAM 整次训练写死一句 `override_instruction`（battery：「桌上两节电池和电池槽…」）。Qwen3-4B 的 hidden 预先算好放 `RMBench-ImageWAM-meta/.../flux2_qwen3_cache_4b`，训练时不跑文本塔。

WLA 在学阶段语言；ImageWAM 在用任务级一句条件。

### 2.9 归一化与输出 key

两边都是对 action / state 做 z-score，但统计文件不是同一份，**不要横比 `action_loss` 绝对值**。

WLA wrapper 吐给 Trainer：`input_images`、`target_images`、`actions`、`action_mask`、`states`、`caption`、`history_subtask_text`、`target_subtask_text`、`current_image_index`。

ImageWAM 吐：`video`、`action`、`proprio`、`prompt`、以及 cache 里的 `text_hidden_states` / `text_attention_mask`。

collate 和模型接口按各自的 key 接，不能互换 DataLoader。

---

## 3. 为什么同一份 AV1，ImageWAM 没炸、WLA 炸过

解码都发生在 **Dataset `__getitem__`**，由 DataLoader worker 在 CPU 上跑。模型 forward 不再读 mp4。训练时只有解码，没有编码。

| | ImageWAM 实际在跑 | WLA 挂掉那次 | WLA 现在 yaml |
|---|---|---|---|
| `num_workers` | **4**（命令行覆盖；task yaml 默认 8） | **12**（更早默认 32） | **4** |
| 4 卡同时解码进程 | 16 | 48（32 时是 128） | 16 |
| 每条样本解码跨度 | 每路约 16 帧 / 0.5 s × 3 相机 | 主相机约 2 s（60+ 帧）+ 再 open 一次 begin | 同左列协议，worker 已压住 |
| 关解码器 / trim | 有 | pip lerobot，弱 | 同左列协议 |

WLA 能先训到 epoch 3 再突然 `av.error.MemoryError: avcodec_open2(libdav1d)`，很像泄漏积到 600 GB cgroup 顶，而不是第一步就炸。teleai 容器 `memory.max=600G` 且无 swap，0–3 与 4–7 共用。

这不是「RMBench 对 ImageWAM 更友好」，是取样本协议和工程防护不同。

---

## 4. 世界模型头：WLA 更接近 ImageWAM，不是 Fast-WAM

| | **WLA `world_expert`** | **ImageWAM FLUX2** | **Fast-WAM**（对照） |
|---|---|---|---|
| 骨干 | `SanaTransformer2DModel`（Sana 600M，**2D**） | FLUX.2 Klein 4B（**2D 图像**） | Wan2.2-TI2V-5B（**3D 视频 DiT**） |
| VAE | Sana `AutoencoderDC`，64 ch，下采样 32 | FLUX.2 AE | Wan 视频 VAE，`in_dim=48` |
| 监督 | 对 **一张** 未来图做 FM | 对 **终点拼图** 做 FM（`lambda_video`，\(T=2\)） | 对 **多帧视频** 做 FM（约 9 帧） |
| 条件 | RynnBrain-2B（Qwen3-VL）看多张图 → connector | 当前拼图 token + Qwen3-4B cache | Wan 文本 + 首帧 |
| patch | 2D spatial | 2D image tokens | `patch_size: [1, 2, 2]` 时空 |
| 动作头 | 独立 `action_expert` DiT | ActionDiT 与 FLUX **同一套 MOT** | Action DiT + 视频 MoT |

WLA 的图像 loss 编码的是 `target_images`（未来那一张），Sana 在 noisy latent 上预测，没有时间维：

```154:236:models/wla.py
        if "image" in self.training_mode and compute_image_loss:
            target_images = kwargs.get("target_images", None)
            latents = self.vae.encode(target_images).latent
            ...
            model_pred = self.model(hidden_states=noisy_latents, ...)
            image_loss = diff.mean()
```

和 ImageWAM「当前图 → 未来图」是同一类问题。Fast-WAM 才要求 Dataset 吐 `[C, T, H, W]` 且 \(T>2\)。

和 ImageWAM 仍有的实现差：Sana 600M vs FLUX.2 4B；RynnBrain 当场看多张图 vs 文本 cache + 三相机拼图；未来步长 +32 / 单相机 512 vs +16 / 拼图画布；动作头独立 vs 与图像混注意力。

---

## 5. Flow matching 监督

### 5.1 图像头：同一类速度场

两边图像监督都是 **rectified flow / flow matching**，不是 DDPM 的 \(\varepsilon\)-prediction。

路径（干净图 \(x_0\)，噪声 \(\varepsilon\)）：

\[
x_\sigma = (1-\sigma)\,x_0 + \sigma\,\varepsilon
\]

要学的速度场：

\[
v = \varepsilon - x_0
\]

WLA：

```203:232:models/wla.py
            noisy_latents = (1.0 - sigmas) * latents + sigmas * noise
            ...
            target = noise - latents
            diff = weighting * (model_pred - target) ** 2
```

ImageWAM 调度器：

```49:61:ImageWAM/src/imagewam/models/backbones/schedulers/scheduler_continuous.py
        return (1 - sigma) * original_samples + sigma * noise
        ...
        return noise - sample
```

FLUX2 训练里同样是：对 **未来帧 latent** 加噪，预测 `noise - target_latent`。当前拼图只作为 `ref_image`，不加噪、不进这个 MSE。

**速度场定义一样。** 差别在 \(x_0\)、条件和 \(\sigma\) 采样。

| | WLA | ImageWAM FLUX2 |
|---|---|---|
| 被加噪、被监督的 \(x_0\) | 主相机 \(t+32\) 的 Sana latent | 三相机拼图 \(t+16\) 的 FLUX AE token |
| 条件（不进 \(v\) 的 MSE） | RynnBrain 看 begin / history / current 后的 hidden | 当前拼图 token + Qwen3 cache |
| \(\sigma\) 怎么采 | 均匀 \(u\sim U(0,1)\)，再映射到 scheduler | **shift=5** 的 \(\phi(u)=5u/(1+4u)\)，更偏向高噪 |
| loss 加权 | `compute_loss_weighting_for_sd3`（均匀时接近恒等） | 中间 \(t\) 更大的高斯形 `training_weight` |
| 生成器 | Sana 2D DiT | FLUX.2 2D |
| 记入总 loss 的系数 | `0.1 * image_loss` | `0.5 * loss_video`（名字叫 video，实际是终点帧） |

### 5.2 动作头：都是 FM，WLA 的 \(t\) 方向写反了

ImageWAM 动作和图像用 **同一套** 调度器：

\[
a_\sigma=(1-\sigma)a+\sigma\varepsilon,\quad v=\varepsilon-a
\]

WLA 的 `action_expert` 是 GR00T / π0 常见写法：

```222:223:models/action_model/action_model.py
        noisy_trajectory = (1 - t) * noise + t * actions
        velocity = actions - noise
```

这里 \(t=0\) 是纯噪声，\(t=1\) 是真动作，\(v=a-\varepsilon\)。  
和图像那路 \(v=\varepsilon-x_0\) **符号相反**，因为插值端点对调了。数学上仍是一条直线上的常速度。

另外：

- WLA 动作的 \(t\) 来自 **Beta(1.5, 1.0)**，不是均匀，也不是 shift=5。
- WLA 同一条动作会 `repeat` **16** 次不同噪声再平均（`repeated_diffusion_steps: 16`）。
- ImageWAM 动作和图像在同一套 MOT 里一起去噪；WLA 是 Sana 和 action DiT 两套头，只在 MLLM hidden 上接一下。

### 5.3 语言与总 loss

只有 WLA 有 `language_loss`（RynnBrain next-token CE，权重 **0.005**）。ImageWAM 文本是 cache，不反传 LM。

`training_mode: image_action_language` 时：

```text
loss = 0.1 * image_loss + 1.0 * action_loss + 0.005 * language_loss
```

日志里的 `train/image_loss` 等是 **未加权** 原值；`loss` 才是反传标量。因此总 loss 几乎由 action 主导，看图像好不好要看 `train/image_loss`，不要看它在 `loss` 里的份额。

```text
          图像 FM                         动作 FM
WLA       v = ε − x_{t+32}（主相机）      v = a − ε（32 步，Beta 时间）
          条件：多张独立图 → RynnBrain     独立 DiT，重复 16 次噪声
ImageWAM  v = ε − x_{t+16}（三相机拼图）  v = ε − a（16 步，shift=5）
          条件：当前拼图 → FLUX ref        和图像头混在同一 MOT 里
```

---

## 6. 和 Fast-WAM 的边界（避免记混）

Fast-WAM 仓库 **没有** RMBench 配方。它的 RoboTwin 数据是 `num_frames=33`、`action_video_freq_ratio=4` → 约 9 帧真视频 + 三相机拼接，骨干是 Wan 视频 DiT。

WLA 现在既没有 3D DiT，Dataset 也不组 \(T>2\) 的视频 clip。把 WLA 说成「更接近 Fast-WAM」是错的。

---

## 7. 存盘与断点续训（WLA 实现事实）

WLA 有 **两套盘**，用途不同：

| 路径 | 里面有什么 | 用途 |
|---|---|---|
| `output_.../run_name/checkpoint-N/` | 权重 + DeepSpeed ZeRO-1 optimizer + `scheduler.pt` + RNG + `trainer_state.json` | **完整续训**（与 ImageWAM 的 accelerate/DS ckpt 同类） |
| `checkpoints_.../whole_model/epoch*_stepN/model.pt` | 只有 `state_dict` | 评测 / 导出；**不能当续训** |

yaml 里 `resume_from_checkpoint: null` 时，`train.py` 会 `get_last_checkpoint(output_dir)` 再 `trainer.train(resume_from_checkpoint=last_checkpoint)`，步数和 LR 接着走。

若把 `resume_from_checkpoint` 指到 `model.pt` 目录，会 `from_pretrained` 后 `train(resume_from_checkpoint=False)`：**步数归零、LR 从 warmup 再来**。

`save_total_limit: 1`，HF 目录只留最新一个 `checkpoint-*`。`save_steps: 500`。

官方默认 `max_steps: 30000`（约 71.6 epoch，4 卡 × batch 20）。只跑 1/3 应等到 `checkpoint-10000` 再停，不要中途改 `max_steps` 再 resume（cosine 按 30000 建的）。

---

## 8. 相关代码锚点

| 主题 | 文件 |
|---|---|
| WLA 取帧 / begin cache / 组 `input_images` | `WLA/dataset.py`（`EpisodeBeginFrameCache`、`load_robotwin_or_rmbench_dataset`、train wrapper `__getitem__`） |
| WLA 图像 / 动作 / 语言 loss | `WLA/models/wla.py` |
| WLA 动作 FM（\(v=a-\varepsilon\)） | `WLA/models/action_model/action_model.py` |
| WLA 从哪张图抽 world-expert 条件 | `WLA/models/model.py` `encode_condition` |
| WLA 个人 RMBench 超参 | `WLA/configs_wj/rmbench_battery_try_image_action_language.yaml` |
| ImageWAM RMBench 数据协议 | `ImageWAM/configs/data/rmbench_wla_v3.yaml` |
| ImageWAM 端点帧 / 三相机拼接 | `ImageWAM/src/imagewam/datasets/lerobot/robot_video_dataset.py` |
| ImageWAM 连续时间 FM 调度器 | `ImageWAM/src/imagewam/models/backbones/schedulers/scheduler_continuous.py` |
| ImageWAM FLUX2 训练 loss | `ImageWAM/src/imagewam/models/backbones/imagewam.py` `_training_loss_flux2` |
| ImageWAM pyav 泄漏防护 | `ImageWAM/src/imagewam/utils/mem_tools.py` |

同目录对照：[[FastWAM  LightWAM  ImageWAM]]、[[ImageWAM Do World Action Models Really Need Video Generation, or Just Image Editing/paper]]、[[World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis/paper]]。
