# Translation Notes

- Source: local Zotero PDF, selectable-text extraction (`pdf-text`).
- Coverage: main text and appendix prose are translated paragraph by paragraph; bibliographic entries are retained through page mapping but are not translated line by line.
- Alignment: every source block uses `Para. X:` and its Chinese counterpart uses `Para. X[CN]:`.
- Terminology ledger:
  - procedural generation → 程序化生成
  - constraint specification API → 约束规约 API / 约束指定 API（正文统一采用前者）
  - arrangement solver → 布局求解器
  - simulated annealing → 模拟退火
  - hard constraint / score term → 硬约束 / 评分项（软约束）
  - degree of freedom (DoF) → 自由度
  - relation plane → 关系平面
  - texture baking → 纹理烘焙
  - occlusion boundary → 遮挡边界
- Known extraction caveat: PDF tables and captions may be linearized into adjacent source blocks; quantitative values in the deep note were checked against the rendered table crops.
