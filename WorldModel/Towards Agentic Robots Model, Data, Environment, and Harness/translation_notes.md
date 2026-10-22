# Translation & Alignment Notes: Towards Agentic Robots (arXiv:2610.20442v1)

## 1. Document Overview
- **Source:** *Towards Agentic Robots: Model, Data, Environment, and Harness* (Chonghan Qin, Guocheng Qian, Guanxing Lu, Yuanhao Zhai, Menglin Jia, Chen Chen, Renrui Zhang, Baoquan Chen, Bernard Ghanem; KAUST, PKU, etc.).
- **Deliverables:**
  - `detailed_paper.md`: Complete paragraph-level Chinese-English bilingual reader adhering strictly to the Nature Reader Detail standard.
  - `paper.md`: Byte-identical full paper reader verified with `--require-identical`.
  - `source_map.json`: Structural anchors, figure/table cross-references, and glossary mapping.
  - `translation_notes.md`: Translation rationale, ledger adherence, and verification audit.

---

## 2. Terminology Ledger Adherence
The translations strictly enforce consistent academic terminology in embodied AI and agentic systems:
| English Term | Standard Chinese Translation | Rationale / Context |
| :--- | :--- | :--- |
| **Agentic Robot** | **具身智能体机器人** | Emphasizes both embodiment and agentic autonomy (perception, reasoning, tool-use, memory, closed-loop execution). |
| **Model** | **模型域** | Domain 1: Policy learning, VLA, World Models, Agentic Model learning. |
| **Data** | **数据域** | Domain 2: Autonomous data collection, annotation, and trajectory refinement. |
| **Environment** | **环境域** | Domain 3: 3D scene reconstruction, task generation, and dynamic interactive benchmarks. |
| **Harness** | **支架 / 治理框架域** | Domain 4: Software infrastructure orchestrating models, memory, tools, and execution guardrails. |
| **Orchestration** | **编排与调度机制** | Layered or centralized coordination of subtasks and foundation models. |
| **Guardrails** | **安全护栏与合规边界** | Safety constraints, runtime intervention, and human-in-the-loop protection. |
| **Curriculum** | **任务课程与渐进编排** | Progressive environment and task difficulty sequencing. |
| **Closed-loop** | **闭环执行** | Feedback-driven execution with continuous state monitoring and replanning. |
| **Affordance** | **可供性 / 可操作性空间** | Spatial-action affordance grounds skills to geometric contact points. |
| **VLA** | **视觉-语言-动作模型 (VLA)** | Vision-Language-Action foundation models. |
| **World-Action Model (WAM)** | **世界-动作模型 (WAM)** | Predictive world dynamics models conditioned on robot action trajectories. |

---

## 3. Structural & Asset Traceability
- **Total Paragraph Pairs:** 182 bilingual paragraph pairs cleanly formatted as blockquotes with `<span style="color:#3B82F6"><strong>Para. X:</strong></span>` and `<span style="color:#F59E0B"><strong>Para. X[CN]:</strong></span>`.
- **Figures:** 7 high-resolution figures placed at their respective semantic introductions, each with complete English and Chinese captions:
  - Figure 1: 具身智能体机器人的闭环定义与四大维度 (Abstract)
  - Figure 2: 具身智能体机器人的四大核心功能域架构 (Section 1)
  - Figure 3: 具身智能体机器人系统的分类体系与研究全景 (Section 3)
  - Figure 4: 五种利用智能体改进机器人模型学习与决策的途径 (Section 4)
  - Figure 5: 共享机器人经验上的三大数据端干预机制 (Section 5)
  - Figure 6: 为单项机器人任务构建与测试环境的三种途径 (Section 6)
  - Figure 7: 围绕机器人执行组织智能体能力的支架治理架构 (Section 7)
- **Tables:** 18 comprehensive comparative survey tables transcribed directly into searchable Markdown tables immediately following their asset image crop, with full bilingual captions:
  - Table 1: Conceptual comparisons across autonomous robots, LLM/VLM agents, VLAs, and Agentic Robots
  - Tables 2-6: Model-domain works (Decision-Making, Policy Learning, Architecture, Multi-Robot Coordination, Post-Training)
  - Tables 7-9: Data-domain works (Collection, Annotation, Refinement)
  - Tables 10-12: Environment-domain works (Reconstruction, Task Generation, Benchmarking)
  - Tables 13-18: Harness-domain works (Orchestration, Memory, Tools, Self-Evolution, Guardrails, Layered Systems)
- **Bibliography:** All 469 references preserved verbatim in standard numbered bibliographic format (`1. [1] ...` to `469. [469] ...`).

---

## 4. Verification & Validation Metrics
- **Validator Script:** `nature-reader-detail-wj/scripts/validate_detailed_paper.py`
- **Results:**
  - `passes: True`
  - `errors: 0`
  - `warnings: 0`
  - `missing_images: 0`
  - `bilingual_paragraph_pairs: 182`
  - `caption_pairs: 25 original / 25 Chinese`
  - `image_links: 25`
  - `reference_entries: 469`
  - `require_identical SHA256 match: PASS`
