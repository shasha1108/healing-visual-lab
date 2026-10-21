# Back to the Wind · 回到风里

> **Tech Keywords:** p5.js, canvas 2d, web audio api, touch interaction, localstorage persistence

<!-- WORK_META
  slug: butterflies-back-to-wind
  render_engine: Canvas 2D p5.js 1.9.0
  particle_count: N/A
  particle_type: N/A
  shader_type: N/A
  interaction: touch / click
  audio: Web Audio API synthesis
  effects: embedded illustration assets, pointer-driven cork physics, staged butterfly flight choreography, particle glows, generative Web Audio
  use_cases: p5.js, canvas 2d, web audio api, touch interaction, localstorage persistence
  standalone: yes
  dependencies: 1 CDN (p5)
  file_size: ~7433 KB, 2211 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Back to the Wind - preview 1](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/butterflies-back-to-wind/v-727fa9545fc0/butterflies-back-to-wind_1.gif)

> Pull the cork free, and let what was held return to the wind.

《回到风里》是一件以玻璃瓶与六只蝴蝶展开的互动作品。按住瓶塞向上拉开，封存的蝴蝶会依次穿过瓶口：三只飞出画面，三只回到花丛；空下来的瓶子不再索取你。

作品使用 p5.js 在 Canvas 中绘制蝴蝶、瓶身与粒子光点，并以指针操作驱动拔塞与放飞节奏。三张画面贴图已嵌入单一 HTML，触摸与鼠标操作均可使用；生成式 Web Audio 随场景状态变化。

---

## ✨ 预览

直接用浏览器打开 `butterflies-back-to-wind.html` 即可运行——单文件 H5，仅依赖 1 个 CDN（p5）。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `butterflies-back-to-wind.html` | 完整可运行的 H5 互动作品，约 7433KB |
| [`butterflies-back-to-wind_1.gif`](https://raw.githubusercontent.com/shasha1108/healing-visual-previews/main/butterflies-back-to-wind/v-727fa9545fc0/butterflies-back-to-wind_1.gif) | 预览图 1（外部资源仓库） |
| `butterflies-back-to-wind.md` | 本说明文件 |

## 🖱️ 交互

- 按住瓶塞向上拖动，将它拔出瓶口并启动放飞。
- 放飞结束后，轻触或掠过花间的蝴蝶，观察它们受到惊动后的飞行。
- 拾起瓶塞并放回瓶口附近，可让它回到原位。

## 🛠️ 技术栈

- p5.js
- Canvas 2D
- Web Audio API
- localStorage

## 🌱 创作背景

作品围绕“释放、交接与松手”展开：瓶中的六只蝴蝶不被全部带向同一处，而是在远飞与归返之间各自完成去向。这个分流过程来自作品本身的既定叙事设定。
