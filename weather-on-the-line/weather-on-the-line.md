# Weather On The Line · 天气晾在房间里

> **Tech Keywords:** p5.js, canvas 2d, webgl, web audio api, touch interaction

<!-- WORK_META
  slug: weather-on-the-line
  render_engine: WebGL p5.js 1.9.0
  particle_count: 441 cloth nodes
  particle_type: N/A
  shader_type: N/A
  interaction: touch / click
  audio: Web Audio API synthesis
  effects: mass-spring cloth simulation (7 cloths × 8×6 verlet nodes), 5-iteration constraint solver, affine triangle texture warping of a painted atlas, p5.js WEBGL orthographic renderer with Canvas2D triangle fallback sharing one physics world, rope impulse wave propagation, clip-angle spring animation, bed/floor landing validation, deterministic-PRNG brown-noise Web Audio synthesis, tag-driven rehang snapping, prefers-reduced-motion branch, pointer capture input, aria-live announcements
  use_cases: p5.js, canvas 2d, webgl, web audio api, touch interaction
  standalone: yes
  dependencies: 1 CDN (p5)
  file_size: ~7997 KB, 360 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Weather On The Line - preview 1](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/weather-on-the-line/v-f1627fc67481/weather-on-the-line_1.gif)

> 把天气一件件晾上去，再一件件摘下来。

一间薰衣草紫的卧室，床头横着一根晾衣绳，绳上夹着七块布——雨、雾林、风、乌云、雪、雷雨，还有一块是空白的。布上画的就是天气本身。按住拨一拨，布片会荡开，绳子和夹子跟着一起颤；往下拉，夹子先松开一侧，布就离开绳子，落到床上或地板上。

每块布都是一张 8×6 的受力网格：48 个节点、五轮约束迭代，各自算自己的垂坠与摆动，所以七块布的节奏并不一样。原画只当作纹理图集用——画面里的四边形坐标被换算成三角形，逐片贴到变形后的网格上，于是布弯下去的时候，上面的雨也跟着一起弯。渲染优先走 p5 的 WEBGL 正交投影，整条链路失败才切到 Canvas2D 的三角形仿射路径，两套渲染共用同一份物理，不会各算各的。声音是现场合成的：摘夹子是一声短促下滑的三角波，布料摩擦、落床、落地来自一段确定性噪声的带通滤波。它同样认得 `prefers-reduced-motion`，此时所有缓动收紧成一步到位。

摘下来的布还能挂回去：拎着它靠近空着的夹位，它会自己吸附、重新咬住绳子。枕头按下去会陷一块，被角往上拎会翻折过来，露出下面的床垫。整间屋子只存在于这一次会话里——刷新之后，一切回到最初晾好的样子。

---

## ✨ 预览

直接用浏览器打开 `weather-on-the-line.html` 即可运行——单文件 H5，仅依赖 1 个 CDN（p5）。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `weather-on-the-line.html` | 完整可运行的 H5 互动作品，约 7997KB |
| [`weather-on-the-line_1.gif`](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/weather-on-the-line/v-f1627fc67481/weather-on-the-line_1.gif) | 预览图 1（外部资源仓库） |
| `weather-on-the-line.md` | 本说明文件 |

## 🖱️ 交互

- **拨动布片**：按住绳上任一块布拨一下，布片荡开，绳和夹子跟着一起颤
- **往下拉，摘下天气**：按住布片向下拖，夹子会先松开一侧，布随即脱落；落点在床上还是地板，取决于脱手时的位置
- **把布挂回去**：拎着布靠近空着的夹位，它会自己吸附上去
- **按压枕头**：按下去会陷一块，松手回弹
- **掀起被角**：从被角往上拎，被子翻折过来，露出下面的床垫
- **拨绳子**：在空处拨一下绳，波动顺着绳传到两头，把挂着的布一起晃起来
- **键盘**：聚焦画面后，Tab 可触到「触碰中央空白布 / 按压枕头 / 掀起被角」三个按钮
- **静音**：右上角按钮开关声音，图标上的声波随之消失或出现

## 🛠️ 技术栈

- p5.js
- WebGL
- Canvas 2D
- Web Audio API

## 🌱 创作背景

这件作品的原点是整理的快乐：在一个房间里把东西一件件拿起来、再放回去，手上一直有小事做，脑子反而松下来了。所以这里的整理没有目标，也不计分——布摘下来落在床上或地板上都行，随手挂回去就好，没有哪一步会「弄坏」。

七块布上画的是天气，房间是薰衣草紫配暖纸底。天气和这套配色各自还想说点什么，做的时候也说不清；它们更像先被做出来、再看它像什么。这里就照实留着，不替它们补一个解释。
