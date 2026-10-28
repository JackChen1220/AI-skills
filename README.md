# AI Skills

两套用于视觉内容制作的实用 AI Skill：图文封面、英语场景闪卡。每套技能放在独立目录，附使用说明、参考素材和示例图片，可以按需单独使用。

| Skill | 用途 | 入口 |
| --- | --- | --- |
| 猴子 AI 笔记风格图文 | 暖白网格、粗黑标题、荧光高亮与漫画插画，用于项目封面、信息图、流程卡片 | [介绍与示例](monkey-ai-notes-imagegen/README.md) · [SKILL.md](monkey-ai-notes-imagegen/SKILL.md) |
| 英语场景闪卡 | 把教材或自建词表组织成场景插画，独立生成准确的词汇、音标、释义和学习内容 | [介绍与示例](english-scene-flashcards/README.md) · [SKILL.md](english-scene-flashcards/SKILL.md) |

## 看看效果

### 图文封面与漫画插画

![AI 实践分享封面插画示例](monkey-ai-notes-imagegen/examples/ai-sharing-cover.png)

实际生成的横版应用示例；技能默认也提供 3:4 图文版式。正文排版、参考风格与生成插画的职责分别说明，不将参考作品冒称为原创结果。

### 英语场景闪卡

<p>
<img src="english-scene-flashcards/demo/grade3/G3A-C01-pets.jpg" alt="宠物场景英语闪卡示例" width="45%">
<img src="english-scene-flashcards/demo/grade5/G5A-C24-hiking-trip.jpg" alt="徒步场景英语闪卡示例" width="45%">
</p>

场景图负责表达，教学文字由独立数据准确排版；示例年级不限制技能的适用范围。[查看完整图库](english-scene-flashcards/demo/README.md)。

## 开始使用

```bash
git clone https://github.com/JackChen1220/AI-skills.git
cd AI-skills
```

将需要的整个技能目录放入你的 Agent 支持的技能位置，或直接让支持本地文件的 Agent 读取该目录的 `SKILL.md`。请保留子目录结构，不要只复制入口文件。安装位置及图像能力配置以所用 Agent 的说明为准。

示例请求：

```text
使用 $monkey-ai-notes-imagegen，主题是“把零散资料变成可用知识”，制作一张漫画封面。

使用 $english-scene-flashcards，把我提供的词表做成适合学习者年龄的场景闪卡，保留原始英文、音标和释义。
```

## 仓库结构

```text
AI-skills/
├── monkey-ai-notes-imagegen/
└── english-scene-flashcards/
```

每套技能的依赖和检查方法见各自说明。图像生成需要运行环境提供相应能力，本仓库不捆绑个人账号、API 服务或密钥。

## 发布与素材说明

英语闪卡有三张参考 PNG 和一张 Demo JPEG 无法完整解码，文件与公开上游一致，已记录在 [已知问题](KNOWN_ISSUES.md)。首页所选展示图正常；不以文件存在或结构检查通过代替视觉批准。

- 发布前检查文本、脚本、配置与示例图片，排除凭据、私钥、本机缓存和个人绝对路径。
- 本仓库使用新的 Git 历史，不导入本地技能目录的历史记录。
- `design_tokens.json` 等文件是颜色、尺寸、字体等设计参数，不是认证 Token。
- 再次发布前运行 `python3 scan_publication.py`，并按 [安全检查说明](SECURITY.md)检查图片和新增内容。
- 第三方参考图、品牌与原始项目的来源说明见 [NOTICE.md](NOTICE.md)；不将它们统一宣称为本仓库原创或额外授予商用许可。
