from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
ASSETS = ROOT.parent.parent / "assets"
ASSETS.mkdir(parents=True, exist_ok=True)

# Coordinates are in the 144-dpi page render coordinate system (1224 x 1584).
CROPS = {
    "fig01_overview.png": (2, (55, 45, 1170, 690)),
    "fig02_framework.png": (4, (55, 45, 1170, 380)),
    "fig03_attention_mask.png": (7, (650, 570, 1100, 1140)),
    "fig04_async_pipeline.png": (9, (55, 35, 1170, 390)),
    "fig05_real_world_results.png": (11, (150, 35, 1100, 820)),
    "fig06_task_progressions.png": (12, (45, 35, 1180, 1445)),
    "table01_robotwin_summary.png": (13, (55, 1180, 1170, 1505)),
    "table02_libero.png": (14, (120, 40, 1105, 690)),
    "table03_ablation.png": (15, (105, 35, 1120, 245)),
    "fig07_initialization.png": (15, (65, 255, 1170, 730)),
    "fig08_sample_efficiency.png": (16, (55, 25, 1175, 625)),
    "fig09_memory.png": (16, (55, 620, 1175, 1105)),
    "fig10_generalization.png": (17, (65, 25, 1160, 505)),
    "table_s1_robotwin_all_tasks.png": (25, (85, 40, 1140, 1395)),
    "table_s2_make_breakfast.png": (26, (90, 90, 1140, 1365)),
    "table_s3_pick_screws.png": (27, (135, 90, 1100, 1345)),
    "table_s4_fold_clothes.png": (28, (110, 90, 1120, 1345)),
    "table_s5_unpack_delivery.png": (29, (110, 90, 1120, 1350)),
    "table_s6_insert_tubes.png": (30, (240, 90, 990, 1350)),
    "table_s7_fold_pants.png": (31, (240, 90, 990, 1350)),
}

for name, (page, box) in CROPS.items():
    src = ROOT / f"page_{page}.png"
    with Image.open(src) as image:
        image.crop(box).save(ASSETS / name, optimize=True)
    print(f"{name}: p.{page} {box}")
