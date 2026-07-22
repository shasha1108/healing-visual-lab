# First Light · 第一束光 · First Light

> **Tech Keywords:** p5.js, canvas 2d, web audio api, touch interaction, localstorage persistence

<!-- WORK_META
  slug: first-light
  render_engine: Canvas 2D p5.js 1.9.0
  particle_count: N/A
  particle_type: N/A
  shader_type: N/A
  interaction: touch / click
  audio: Web Audio API synthesis
  effects: Bayer 4x4 ordered dithering, aero16 palette, glass chamber refraction, glow spores, cyan rain, memory ring etching, exponential easing, Web Audio chime synthesis
  use_cases: p5.js, canvas 2d, web audio api, touch interaction, localstorage persistence
  standalone: yes
  dependencies: 1 CDN (p5)
  file_size: ~43 KB, 1285 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![First Light - preview 1](first-light_1.gif)

> 一颗黑色像素种子，在你的温度里长出第一束光。

掌心托着一只 Frutiger Aero 风格的玻璃育光舱，舱底沉着一颗沉睡的黑色像素种子。长按玻璃，温度透过曲面抵达种子，光须从芽点一丛丛钻出，伴着青涩的雨与萤火，整座育光舱慢慢亮起来。

松手的瞬间，光并不是熄灭，而是沉进舱壁，被刻成一圈温度年轮。localStorage 记得你来过几次，每多一次长按，种子的苏醒就更快一分——它认得你的温度。

aero16 色板、Bayer 4×4 有序抖动、指数趋缓动画与 Web Audio 即兴合成的风铃，共同完成这场「唤醒」。

---

## ✨ 预览

直接用浏览器打开 `first-light.html` 即可运行——单文件 H5，仅依赖 1 个 CDN（p5）。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `first-light.html` | 完整可运行的 H5 互动作品，约 43KB |
| `first-light_1.gif` | 预览图 1 |
| `first-light.md` | 本说明文件 |

## 🖱️ 交互

- **长按玻璃舱**：持续传递温度，种子逐渐苏醒，光须丛生，光点上升汇聚
- **松开手指**：温度回落，光沉淀为舱壁上的「温度年轮」记忆环
- **轻触任意处**：开启 Web Audio 声音（风铃与苏醒和弦）
- **多次回访**：localStorage 累积记忆次数，种子苏醒越来越快
- **苏醒高潮**：青色雨落、萤火环绕、高潮和弦，光须达最盛

## 🛠️ 技术栈

- p5.js
- Canvas 2D
- Web Audio API
- localStorage

## 🌱 创作背景

「第一束光」来自一个很小的想法：种子苏醒不需要别的，只需要温度。冬天隔着玻璃晒太阳，掌心贴在冰冷玻璃上，那块被焐热的地方会起雾、会透光——像是你把一小段自己留给了玻璃。这个作品把那一幕做成像素小世界：一颗黑色的种子躺在玻璃舱底，等一只手长按它。光须长出来的那几秒，是它第一次「看见」你。松手之后留下的年轮，是它记住你的方式。
