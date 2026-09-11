# Egret Sunrise · 今天，由你升起

> **Tech Keywords:** p5.js, canvas 2d, web audio api, touch interaction

<!-- WORK_META
  slug: egret-sunrise
  render_engine: Canvas 2D p5.js 1.9.0
  particle_count: N/A
  particle_type: N/A
  shader_type: N/A
  interaction: touch / click
  audio: Web Audio API synthesis
  effects: 4px pixel quantisation, six-colour letterpress palette, two-pass ink glaze dawn wash, banded submerged sun, mirrored scaffold reflection, palette-swapped water dawn field, ten-state interaction FSM, spring-damped drag physics, pulley angular interpolation, Web Audio synthesis (catch / feed / pulley step / water break / settle), prefers-reduced-motion branch
  use_cases: p5.js, canvas 2d, web audio api, touch interaction
  standalone: yes
  dependencies: 1 CDN (p5)
  file_size: ~50 KB, 1469 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Egret Sunrise - preview 1](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/egret-sunrise/v-6e7285fb485e/egret-sunrise_1.gif)

> 拖一条晨光鱼喂给白鹭，它咬住滑轮上的绳，把太阳从海里一寸寸吊起来。

海里游着三条金色的晨光鱼。按住其中任意一条，把它拖到白鹭嘴边松手——白鹭咬住鱼，翅膀一起一落，一口一口咬住滑轮上的绳；绳结绷紧，滑轮转出八圈，太阳被从海里一寸寸吊出来。破水的那一瞬间水面炸开，水滴落回海面，溅起一圈圈铜色涟漪。等太阳站稳，白鹭轻轻甩了甩嘴——那是它的庆祝。

所有笔触都被压进 4 像素的网格里：太阳不是圆，是按像素行切出来的半圆；倒影不是模糊，是一排排宽度随深度变化的色块。整张 1080×1440 的竖版海报用六色凸版色板画成——暖纸做底，靛蓝做结构，朱红做太阳，黄铜做所有你要动手的地方。纸纹、干笔与反光都靠这几支「印版」反复叠出来。

第一次触摸之后声音才开始：Web Audio 现场合成捕捞、喂食、每一步起吊、破水和落定，各有各的音高。整个页面是一台十状态的机器——从黎明前的静默到升日后的余韵，每一步都有名字；它同样认得 `prefers-reduced-motion`，此时所有缓动收紧成一步到位。

---

## ✨ 预览

直接用浏览器打开 `egret-sunrise.html` 即可运行——单文件 H5，仅依赖 1 个 CDN（p5）。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `egret-sunrise.html` | 完整可运行的 H5 互动作品，约 50KB |
| [`egret-sunrise_1.gif`](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/egret-sunrise/v-6e7285fb485e/egret-sunrise_1.gif) | 预览图 1（外部资源仓库） |
| `egret-sunrise.md` | 本说明文件 |

## 🖱️ 交互

- **拖一条晨光鱼**：按住海中任意一条金色胖鱼，拖到白鹭喙边松手即可喂食
- **中途松手**：鱼会自己游回原位，涟漪散开，随时可以重来，没有失败状态
- **点水面**：任意位置轻触都会荡开一圈涟漪
- **键盘**：聚焦画面后按 Enter 或空格，白鹭自动完成一次喂食与升日
- **静音**：右上角按钮开关声音，图标上的声波会随之消失或出现

## 🛠️ 技术栈

- p5.js
- Canvas 2D
- Web Audio API

## 🌱 创作背景

这件作品的原点是一张用户提供的参考图：白鹭、脚手架、滑轮与升日之间的关系由它给出。因为原图作者与授权不明，本作没有嵌入任何源图像素或水印，而是按那层关系独立重绘；六色凸版色板则来自已确认的设计稿。

作品名「今天，由你升起」把日出的主语交了出去——在这张画里，太阳升不升，取决于你有没有把那条鱼拖过去。
