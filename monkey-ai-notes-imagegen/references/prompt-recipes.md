# 生成与修正配方

提示词顺序：唯一输出用途→参考职责→profile/画布→几何→色形字→插画场景→逐字文案→禁止漂移项。像素是设计坐标，不是工具参数。套图锁定比例、边距、网格、字重、圆角档位、描边、阴影方向；允许换主色、图解类型、场景与信息结构。不要每页都三个按钮和机器人。

## editorial-bold 插画语法

`premium editorial 2D comic illustration; confident variable-width black ink contours; expressive friendly human faces; compact friendly robots with a dark faceplate when appropriate; controlled cel shading and painted material detail; warm cream and wooden workspace; a clear input-to-output story; bright cyan, lime and lavender accents; rich but legible prop silhouettes; illustration confined inside one rounded black frame`

以下2D语法仅用于editorial-bold的bright/warm/sparse。early-playful封面可选storybook-3d：高品质立体童话角色、柔光、毛发与金色室内材质、适度景深；仅框内立体，外部UI仍平面。

中景故事优于无背景大头像。桌面/纸张/杯子/设备/盆栽提供生活感，不能遮挡信息流。深色复杂细节留在框内，暖白底板保持干净。UI不做厚涂、手写、3D塑料。

## 文案与一致性

- 提供逐字title_lines；通常每行6–13个等效汉字，仅作为容量提示。保留用户明确要求原样的字。
- 黑体标题极粗、紧凑，无法确定原始字体名。高亮按参考分为underline（字形高约33%）、marker（约73%）、full-block（约140%含上下留白）三类；不统一成半高，不给字加发光描边。
- 卡片左对齐、短句；信息多就增页。长代码、URL、真实界面小字用真实素材，不凭空编写。
- 只给1张版式参考，必要时再加1张插画参考。首张通过后保留成品和prompt，作为后续样式锚点；另选本页结构锚点，明确各自职责。
- 不一次喂16张参考；冲突样式会被平均。

## 定向修正

先读取当前profile、组件类型与插画variant。以下数值示例只用于editorial-bold普通卡片；截图、流程、封面主框和早期彩卡必须换成各自tokens，不能把正确家族改成默认值。

- 描边：`Keep content and geometry. Set regular card outlines to 7 design px at 1080 width, near-black and consistent. Preserve finer illustration lines.`
- 阴影：`Change only UI shadows to opaque flat offset duplicates, dx=12,dy=14,blur=0. Preserve typography, illustration and text.`
- 网格：`Change only background grid to 82px pitch at1080 width, very faint on warm paper; do not move content.`
- 标题：`Change only headline to a very heavy modern Chinese sans visual, approximately weight900, identical words, line breaks and occupied box.`
- editorial-bold的2D插画（early storybook-3d不适用）：`Change only framed hero to clean inked2D comic, layered cel shading, painted wood/fabric detail and warm everyday light. Preserve page UI.`
- 错字：逐字列位置、原字、正确字；只改该区，再实际查看。
- 比例：要求重排为3:4并保留全文案；不静默拉伸。仅按用户授权裁切或确定性排版。

## 严格像素复用

参考图+tokens+有界修正能提高同系列一致性，随机生图不能保证每次边框/字距/网格逐像素相同。明确要求固定组件坐标或大量准确文字时，以固定排版模板承载文字/UI、生图只负责插画更可靠；清楚说明组合制作方式。不要把原参考成品直接当新生成结果。
