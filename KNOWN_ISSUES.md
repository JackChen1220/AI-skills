# 已知上游素材问题

本次整理发现，英语闪卡包的下列三个参考 PNG 无法完整解码：

- `english-scene-flashcards/assets/golden_set/G3A-U01-C01-approved.png`
- `english-scene-flashcards/assets/style_references/connector-light-01.png`
- `english-scene-flashcards/assets/style_references/connector-light-02.png`

已从原始说明关联的公开上游仓库重新取回并比较文件，字节指纹与本地包一致，问题不是本次复制产生的。这三个文件按来源原样保留，不将它们冒称为已通过本次视觉审阅的基准，也不擅自把其他 Demo 提升为 Golden Sample。

另有 `english-scene-flashcards/demo/grade4/G4A-C05-chores-family.jpg` 无法完整解码，已核对其指纹同样与公开上游一致。图库不直接嵌入这张损坏图片，保留文件及问题说明供追溯。

仓库首页所选展示图片可正常解码。制作新闪卡前，应先提供或恢复有效的视觉基准，并按 Skill 的实际图片检查与 QA 规则处理；文件清单、JSON Schema 检查通过不等于这些图片的视觉检查通过。
