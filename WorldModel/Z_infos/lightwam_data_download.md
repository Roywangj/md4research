---
tags:
  - papers/WorldModel
  - Light-WAM
  - Fast-WAM
  - data-download
date: 2026-07-20
status: howto
audience: 用户本地执行下载（本文件只给指令，不代跑大下载）
---

# Light-WAM / Fast-WAM 数据下载指令

> **用途**：先学习、快速迭代时，为 **Light-WAM** 准备数据（raw 与 Fast-WAM **共用**）。  
> **Benchmark**：LIBERO + RoboTwin 2.0（两仓同一套）。  
> **你来执行**：下面命令按顺序复制到终端即可。  
> **建议根目录**：你自己定一个大磁盘路径，例如  
> `export WAM_DATA_ROOT="$HOME/datasets/wam"`  
> 下文一律用 `$WAM_DATA_ROOT`。

---

## 0. 准备（只做一次）

```bash
# 1) 工作根目录（改成你的大磁盘路径）
export WAM_DATA_ROOT="$HOME/datasets/wam"
mkdir -p "$WAM_DATA_ROOT"
cd "$WAM_DATA_ROOT"

# 2) Hugging Face CLI（二选一）
pip install -U "huggingface_hub[cli]"
# 或: brew install huggingface-cli   # 若你环境已有

# 3) 登录（公开数据集一般可不登；若限流再登）
# huggingface-cli login

# 4) 可选：加速
# export HF_ENDPOINT=https://hf-mirror.com   # 仅当你有可用镜像时
```

检查磁盘：RoboTwin raw 分片 + 解压体积很大；Light 的 latent cache 还可再涨到 **TB 级**。先只下 **阶段 A（LIBERO）** 再决定是否下 RoboTwin / cache。

---

## 阶段 A（推荐先做）：LIBERO raw（Fast/Light 共用）

来源：https://huggingface.co/datasets/yuanty/LIBERO-fastwam  

文件（4 个 tar.gz）：

- `libero_spatial_no_noops_lerobot.tar.gz`
- `libero_object_no_noops_lerobot.tar.gz`
- `libero_goal_no_noops_lerobot.tar.gz`
- `libero_10_no_noops_lerobot.tar.gz`

### A1. 下载

```bash
export WAM_DATA_ROOT="${WAM_DATA_ROOT:-$HOME/datasets/wam}"
mkdir -p "$WAM_DATA_ROOT/data/libero_mujoco3.3.2"
cd "$WAM_DATA_ROOT/data/libero_mujoco3.3.2"

# 整库下载到当前目录（会带上 README 等）
huggingface-cli download yuanty/LIBERO-fastwam \
  --repo-type dataset \
  --local-dir . \
  --local-dir-use-symlinks False
```

若只想下 tar（避免多余文件也行，上面整库最省事）。

### A2. 解压

```bash
cd "$WAM_DATA_ROOT/data/libero_mujoco3.3.2"
for f in *.tar.gz; do
  echo "Extracting $f ..."
  tar -xzf "$f"
done
```

### A3. 验收目录

```bash
cd "$WAM_DATA_ROOT"
find data/libero_mujoco3.3.2 -maxdepth 1 -type d | sort
```

期望类似：

```text
data/libero_mujoco3.3.2/
├── libero_10_no_noops_lerobot/
├── libero_goal_no_noops_lerobot/
├── libero_object_no_noops_lerobot/
└── libero_spatial_no_noops_lerobot/
```

**做到这里就可以先 clone Light-WAM，把 `data/` 软链进去，先跑 LIBERO 单 suite。**

---

## 阶段 B：RoboTwin 2.0 raw（Fast/Light 共用，体积大）

来源：https://huggingface.co/datasets/yuanty/robotwin2.0-fastwam  

文件：

- `dataset_stats.json`
- `robotwin2.0.tar.gz.part-00` … `part-07`（共 8 片）

### B1. 下载

```bash
export WAM_DATA_ROOT="${WAM_DATA_ROOT:-$HOME/datasets/wam}"
mkdir -p "$WAM_DATA_ROOT/data/robotwin2.0"
cd "$WAM_DATA_ROOT/data/robotwin2.0"

huggingface-cli download yuanty/robotwin2.0-fastwam \
  --repo-type dataset \
  --local-dir . \
  --local-dir-use-symlinks False
```

### B2. 拼接并解压

```bash
cd "$WAM_DATA_ROOT/data/robotwin2.0"

# 确认 8 个 part 都在
ls -lh robotwin2.0.tar.gz.part-*

# 官方推荐：cat 后直接 tar（不必先合成单个大 tar）
cat robotwin2.0.tar.gz.part-* | tar -xzf -
```

### B3. 验收

```bash
cd "$WAM_DATA_ROOT"
ls -la data/robotwin2.0/dataset_stats.json
find data/robotwin2.0/robotwin2.0 -maxdepth 2 -type d | head
```

期望：

```text
data/robotwin2.0/
├── dataset_stats.json          # 建议保留在此
└── robotwin2.0/
    ├── data/
    ├── meta/
    └── videos/
```

---

## 阶段 C（可选，Light-WAM 专用）：offline latent / text cache

> **只有当你要用 Light-WAM 训练、且想少做 precompute 时再下。**  
> 体积可能极大；也可跳过本阶段，用仓库脚本自己 `precompute_*`。

来源：https://huggingface.co/datasets/l1ziang/lightwam-offline-cache  

主要内容：

- `latent_cache_Wan2.1-T2V-1.3B/libero_*_2cam224.tar`（4 个）
- `latent_cache_Wan2.1-T2V-1.3B/robotwin_3cam384_sharded.tar.part-000` … `part-005`
- `text_embeds_cache/libero.tar`  
- **RoboTwin text cache 未发布** → 需本地生成（见 C3）

### C1. 下载

```bash
export WAM_DATA_ROOT="${WAM_DATA_ROOT:-$HOME/datasets/wam}"
mkdir -p "$WAM_DATA_ROOT/data"
cd "$WAM_DATA_ROOT/data"

huggingface-cli download l1ziang/lightwam-offline-cache \
  --repo-type dataset \
  --local-dir lightwam-offline-cache \
  --local-dir-use-symlinks False
```

### C2. 解压到 Light 期望布局

```bash
export WAM_DATA_ROOT="${WAM_DATA_ROOT:-$HOME/datasets/wam}"
cd "$WAM_DATA_ROOT/data"

# 目录结构按 Light README
mkdir -p latent_cache_Wan2.1-T2V-1.3B text_embeds_cache

# LIBERO latent
for f in lightwam-offline-cache/latent_cache_Wan2.1-T2V-1.3B/libero_*.tar; do
  echo "Extracting $f ..."
  tar -xf "$f" -C latent_cache_Wan2.1-T2V-1.3B
done

# RoboTwin latent（分片）
cd lightwam-offline-cache/latent_cache_Wan2.1-T2V-1.3B
cat robotwin_3cam384_sharded.tar.part-* | tar -xf - -C "$WAM_DATA_ROOT/data/latent_cache_Wan2.1-T2V-1.3B"
cd "$WAM_DATA_ROOT/data"

# LIBERO text embeds
tar -xf lightwam-offline-cache/text_embeds_cache/libero.tar -C text_embeds_cache
```

期望：

```text
data/
├── latent_cache_Wan2.1-T2V-1.3B/
│   ├── libero_spatial_2cam224/
│   ├── libero_object_2cam224/
│   ├── libero_goal_2cam224/
│   ├── libero_10_2cam224/
│   └── robotwin_3cam384_sharded/
└── text_embeds_cache/
    ├── libero/
    └── robotwin/    # 需本地生成，见 C3
```

### C3. RoboTwin text cache（官方未打包时）

在 **Light-WAM 仓库根目录**、环境装好后执行（需先把 raw 数据链好）：

```bash
# 仅在 Light-WAM repo 内
RUN_TEXT=true RUN_VIDEO=false bash scripts/precompute_robotwin.sh
# 或按官方 README 的 text-only 命令
```

若不用发布 cache，也可全程本地 precompute：

```bash
LIBERO_SUITE=spatial bash scripts/precompute_libero.sh
LIBERO_SUITE=object  bash scripts/precompute_libero.sh
LIBERO_SUITE=goal    bash scripts/precompute_libero.sh
LIBERO_SUITE=10      bash scripts/precompute_libero.sh
bash scripts/precompute_robotwin.sh
```

---

## 挂到 Light-WAM 仓库（下载完后）

```bash
export WAM_DATA_ROOT="${WAM_DATA_ROOT:-$HOME/datasets/wam}"

# clone（若还没有）
git clone https://github.com/L1ziang/Light-WAM.git
cd Light-WAM

# 把数据链进仓库期望的 data/
mkdir -p data
ln -sfn "$WAM_DATA_ROOT/data/libero_mujoco3.3.2" data/libero_mujoco3.3.2
ln -sfn "$WAM_DATA_ROOT/data/robotwin2.0" data/robotwin2.0   # 若已下阶段 B

# 若已下阶段 C
ln -sfn "$WAM_DATA_ROOT/data/latent_cache_Wan2.1-T2V-1.3B" data/latent_cache_Wan2.1-T2V-1.3B
ln -sfn "$WAM_DATA_ROOT/data/text_embeds_cache" data/text_embeds_cache
```

还需要 Wan 骨干权重（训练/推理）：

```bash
cd /path/to/Light-WAM
mkdir -p checkpoints
export DIFFSYNTH_MODEL_BASE_PATH="$(pwd)/checkpoints"
huggingface-cli download Wan-AI/Wan2.1-T2V-1.3B \
  --local-dir checkpoints/Wan-AI/Wan2.1-T2V-1.3B
```

---

## 建议执行顺序（快速迭代）

| 顺序 | 做什么 | 能否开始训 |
|------|--------|------------|
| 1 | 阶段 **A** LIBERO raw | 可以先做 LIBERO 单 suite + 本地 precompute 或 cache |
| 2 | clone Light-WAM + Wan1.3B 权重 | 可装环境 |
| 3 | 阶段 **C** 的 **LIBERO latent/text**（或本地 precompute） | **LIBERO 快速训** |
| 4 | 阶段 **B** RoboTwin raw | 准备双臂 |
| 5 | 阶段 **C** RoboTwin latent + 本地 text | **RoboTwin 训** |

**不建议**第一天就下满 RoboTwin + 全部 cache；先 A → LIBERO 跑通再 B/C。

---

## 常用检查命令

```bash
export WAM_DATA_ROOT="${WAM_DATA_ROOT:-$HOME/datasets/wam}"

# 磁盘
df -h "$WAM_DATA_ROOT"

# LIBERO 是否解压完整
ls -d "$WAM_DATA_ROOT"/data/libero_mujoco3.3.2/libero_*_no_noops_lerobot

# RoboTwin part 是否齐
ls "$WAM_DATA_ROOT"/data/robotwin2.0/robotwin2.0.tar.gz.part-* 2>/dev/null | wc -l   # 应为 8

# 解压后
ls "$WAM_DATA_ROOT"/data/robotwin2.0/robotwin2.0/videos 2>/dev/null | head
```

---

## 故障排查

| 现象 | 处理 |
|------|------|
| `huggingface-cli: command not found` | `pip install -U "huggingface_hub[cli]"` |
| 下载中断 | 同一 `huggingface-cli download ... --local-dir` 再跑，会续传 |
| `cat ... \| tar` 报错 | 确认所有 `part-*` 下全且顺序 `ls` 字典序正确（part-00…07） |
| Light 找不到数据 | 检查 `Light-WAM/data/` 软链是否指向 `$WAM_DATA_ROOT/data/...` |
| 只有 raw 没有 cache | 先跑 `scripts/precompute_*.sh`，或补下阶段 C |

---

## 来源与对应关系

| 资源 | HF | 谁用 |
|------|-----|------|
| LIBERO raw | `yuanty/LIBERO-fastwam` | Fast + Light |
| RoboTwin raw | `yuanty/robotwin2.0-fastwam` | Fast + Light |
| Light offline cache | `l1ziang/lightwam-offline-cache` | **仅 Light**（加速训练，可选） |
| Wan2.1-1.3B | `Wan-AI/Wan2.1-T2V-1.3B` | Light 骨干 |

选型背景见同目录：[[wam_sota_benchmarks]] §0.6。

---

## 你执行时建议回传的信息（可选）

下载/解压后若报错，把下面贴回来即可继续排查：

```bash
echo "WAM_DATA_ROOT=$WAM_DATA_ROOT"
df -h "$WAM_DATA_ROOT"
ls -la "$WAM_DATA_ROOT/data" 2>/dev/null
ls "$WAM_DATA_ROOT/data/libero_mujoco3.3.2" 2>/dev/null | head
ls "$WAM_DATA_ROOT/data/robotwin2.0" 2>/dev/null | head
```
