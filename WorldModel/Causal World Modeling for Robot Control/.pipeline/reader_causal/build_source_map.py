import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAPER_MD = ROOT / "paper.md"
OUT = ROOT / "source_map.json"
SOURCE = "/Users/roywangj/journey_wj/research/papers4zotero/zotero1/storage/ECJKCB63/Li 等 - 2026 - Causal World Modeling for Robot Control.pdf"

section_pages = {
    "Abstract": "1",
    "1 Introduction": "1-2",
    "2 Preliminary": "3",
    "2.1 Flow Matching": "3",
    "2.2 Video Generation with Conditional Flow Matching": "3-4",
    "3 Method": "4-9",
    "3.1 Problem Statement & Approach Overview": "4",
    "3.2 Autoregressive Video-Action World Modeling": "5-6",
    "3.3 LingBot-VA: Unified Architecture & Training": "6-8",
    "3.4 Real-time Deployment & Asynchronous Inference": "8-9",
    "4 Experiments": "9-17",
    "4.1 Dataset Curation and Preprocessing": "9-10",
    "4.2 Implementation & Training Details": "10-11",
    "4.3 Main Results": "11-14",
    "4.3.1 Real-world Deployment": "11-13",
    "4.3.2 Simulation Evaluation": "13-14",
    "4.4 Ablation": "14-15",
    "4.5 Analysis": "15-17",
    "4.5.1 Sample Efficiency": "15-16",
    "4.5.2 Temporal Memory": "16",
    "4.5.3 Generalization": "17",
    "5 Related Work": "17-18",
    "6 Conclusion": "18",
    "References": "19-22",
    "Appendix A. Real-world Evaluation Details": "23-31",
}

asset_meta = [
    ("F001", 2, "assets/fig01_overview.png", "Fig. 1", [55, 45, 1170, 690]),
    ("F002", 4, "assets/fig02_framework.png", "Fig. 2", [55, 45, 1170, 380]),
    ("F003", 7, "assets/fig03_attention_mask.png", "Fig. 3", [650, 570, 1100, 1140]),
    ("F004", 9, "assets/fig04_async_pipeline.png", "Fig. 4", [55, 35, 1170, 390]),
    ("F005", 11, "assets/fig05_real_world_results.png", "Fig. 5", [150, 35, 1100, 820]),
    ("F006", 12, "assets/fig06_task_progressions.png", "Fig. 6", [45, 35, 1180, 1445]),
    ("T001", 13, "assets/table01_robotwin_summary.png", "Table 1", [55, 1180, 1170, 1505]),
    ("T002", 14, "assets/table02_libero.png", "Table 2", [120, 40, 1105, 690]),
    ("T003", 15, "assets/table03_ablation.png", "Table 3", [105, 35, 1120, 245]),
    ("F007", 15, "assets/fig07_initialization.png", "Fig. 7", [65, 255, 1170, 730]),
    ("F008", 16, "assets/fig08_sample_efficiency.png", "Fig. 8", [55, 25, 1175, 625]),
    ("F009", 16, "assets/fig09_memory.png", "Fig. 9", [55, 620, 1175, 1105]),
    ("F010", 17, "assets/fig10_generalization.png", "Fig. 10", [65, 25, 1160, 505]),
    ("T004", 25, "assets/table_s1_robotwin_all_tasks.png", "Table S1", [85, 40, 1140, 1395]),
    ("T005", 26, "assets/table_s2_make_breakfast.png", "Table S2", [90, 90, 1140, 1365]),
    ("T006", 27, "assets/table_s3_pick_screws.png", "Table S3", [135, 90, 1100, 1345]),
    ("T007", 28, "assets/table_s4_fold_clothes.png", "Table S4", [110, 90, 1120, 1345]),
    ("T008", 29, "assets/table_s5_unpack_delivery.png", "Table S5", [110, 90, 1120, 1350]),
    ("T009", 30, "assets/table_s6_insert_tubes.png", "Table S6", [240, 90, 990, 1350]),
    ("T010", 31, "assets/table_s7_fold_pants.png", "Table S7", [240, 90, 990, 1350]),
]

lines = PAPER_MD.read_text(encoding="utf-8").splitlines()
blocks = []
pages = {}
section = "Abstract"
order = 0
i = 0
while i < len(lines):
    line = lines[i]
    if line.startswith("## ") and not line.startswith("## Page") and not line.startswith("## Terminology") and not line.startswith("## Critical"):
        section = line[3:].strip()
    elif line.startswith("### ") or line.startswith("#### "):
        candidate = re.sub(r"^#{3,4}\s+", "", line).strip()
        if candidate in section_pages:
            section = candidate
    if '<strong>Para.' in line and '[CN]' not in line:
        original = re.sub(r'^>\s*<span[^>]*><strong>Para\.\s*[^<]+:</strong></span>\s*', '', line)
        j = i + 1
        while j < len(lines) and '[CN]' not in lines[j]:
            j += 1
        translation = ""
        if j < len(lines):
            translation = re.sub(r'^>\s*<span[^>]*><strong>Para\.\s*[^<]+\[CN\]:</strong></span>\s*', '', lines[j])
        order += 1
        block_id = f"S{order:03d}"
        page = section_pages.get(section, "1-31")
        blocks.append({
            "id": block_id,
            "type": "paragraph",
            "section": section,
            "pages": page,
            "order": order,
            "original_text": original,
            "translation": translation,
            "confidence": "high",
            "refs": [],
        })
        for p in str(page).split("-"):
            pages.setdefault(p, []).append(block_id)
        i = j
    i += 1

figures = []
for identifier, page, image_path, label, bbox in asset_meta:
    figures.append({
        "id": identifier,
        "page": page,
        "label": label,
        "image_path": image_path,
        "bbox_144dpi": bbox,
        "placement_hint": "near_first_substantive_mention",
        "confidence": "high",
    })
    pages.setdefault(str(page), []).append(identifier)

glossary = [
    {"term": "causal world modeling", "translation": "因果世界建模", "note": "跨 chunk 仅依赖过去；chunk 内仍可并行"},
    {"term": "inverse dynamics model", "translation": "逆动力学模型", "note": "从视觉转移推断动作"},
    {"term": "Forward Dynamics Model", "translation": "前向动力学模型", "note": "用真实反馈与动作刷新预测"},
    {"term": "Noisy History Augmentation", "translation": "噪声历史增强", "note": "训练动作流适应部分去噪视觉 latent"},
    {"term": "Mixture-of-Transformers", "translation": "Transformer 混合架构", "note": "视频/动作双流共享注意力"},
    {"term": "progress score", "translation": "进度分数", "note": "部分步骤完成也计分"},
]

payload = {
    "paper": {
        "title": "Causal World Modeling for Robot Control",
        "authors": ["Lin Li", "Qihang Zhang", "Yiming Luo", "Shuai Yang", "Ruilin Wang", "Fei Han", "Mingrui Yu", "Zelin Gao", "Nan Xue", "Xing Zhu", "Yujun Shen", "Yinghao Xu"],
        "year": 2026,
        "venue": "arXiv:2601.21998v2",
        "source_type": "pdf",
        "source_format": "pdf-text",
        "language": "en",
        "source_pdf": SOURCE,
        "reader_file": "paper.md",
    },
    "notes": {
        "coverage": "All extractable main-text and appendix prose translated; bibliography entries not translated line by line; large tables preserved as image assets.",
        "page_numbering": "PDF page numbers are used.",
    },
    "blocks": blocks,
    "pages": [{"page": k, "block_ids": v} for k, v in sorted(pages.items(), key=lambda kv: int(kv[0]))],
    "figures": figures,
    "assets": [item[2] for item in asset_meta],
    "glossary": glossary,
}

OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(f"wrote {OUT} with {len(blocks)} paragraph blocks and {len(figures)} assets")
