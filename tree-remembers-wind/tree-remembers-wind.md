# tree-remembers-wind · 记得风的树

> **Tech Keywords:** p5.js, Canvas 2D pixel rendering, Web Audio API oscillator synthesis, graph-distance wind propagation, bezier arc fireflies, procedural particle system, pentatonic healing audio

<!-- WORK_META
  slug: tree-remembers-wind
  render_engine: Canvas 2D (p5.js 1.9.0)
  particle_count: ~80 dust motes + 6 fireflies + ~200 leaves + dynamic stars + ~40 grass blades
  particle_type: pixel-rect particle system with radial glow overlays
  shader_type: N/A (pure Canvas 2D with radialGradient for soft glow effects)
  interaction: pointer drag (press-move-release) — stroke direction and length determine wind vector; longer strokes produce stronger gusts
  audio: Web Audio API oscillator synthesis — bandpass-filtered white noise wind bed + pentatonic scale sine oscillators (C5-G5) for treetop chimes
  effects: additive blending (fireflies/meteors), radial gradient glow halos, pixelated image rendering, BFS wind propagation along fractal branch graph
  use_cases: p5.js pixel art tree, canvas wind simulation, web audio procedural sound, fractal tree interaction, healing H5 visualization
  standalone: yes
  dependencies: 2 CDN (p5.js 1.9.0 from cdnjs + bootcdn fallback)
  file_size: ~26 KB, 820 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![tree-remembers-wind preview](tree-remembers-wind_1.gif)

> 释放与辽阔 —— 一座悬浮小岛上，像素树把每一次拂过树冠的手势变成一阵沿枝传播的风。

**记得风的树** 是一件像素风格的 H5 互动疗愈作品。深蓝夜空下，一座微缩岛屿悬浮于柔光云海之上，岛上矗立着一棵分形像素树。用手指划过树冠，风便从触碰点开始，沿着枝干逐级传播——每一片叶子依次翻面，草丛如波浪般起伏，六只萤火虫沿二次贝塞尔弧线飞散，树梢随之奏响五声音阶的清脆铃音。

核心技术亮点在于**图距离风传播算法**：树枝被建模为带权重的有向图，风从最近的触碰枝梢开始，通过 BFS 逐层传播到整棵树，每根枝条和每片叶子都根据其到风源的最短路径计算独立的抵达时间和摆动幅度。这种逐枝响应、由近及远的传播节奏，赋予了风以可感知的"速度感"和"方向感"。

音频系统完全由 **Web Audio API 实时合成**——无任何外部音频文件。底层持续播放带通滤波白噪声模拟风擦声，呼吸周期驱动音量轻柔起伏；每次手势释放后，树梢根据风速和方向选择五声音阶（C5-G5）中的一个音高，用正弦波振荡器合成清亮泛音。

---

## ✨ 预览

直接用浏览器打开 `tree-remembers-wind.html` 即可运行——p5.js 从 CDN 自动加载，无需构建工具或本地服务器。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `tree-remembers-wind.html` | 完整可运行的 H5 互动作品，约 26KB |
| `tree-remembers-wind_1.gif` | 预览动图：风传播 + 萤火虫弧线 + 叶片翻面 |
| `tree-remembers-wind.md` | 本说明文件 |

## 🖱️ 交互

- **按住并划动**：在树冠区域拖拽手指/鼠标，产生方向性阵风
- **划动越长越强**：手势路径长度决定风速，方向决定枝叶摇摆方向
- **观察传播**：风从触碰点沿枝干逐级扩散，叶片依次翻转为亮绿色
- **聆听声音**：风擦声 + 树梢五声音阶铃音（首次交互后启用）
- **等待自然**：静置时可见流星划过、萤火虫绕树飘浮、云海缓慢漂移

## 🛠️ 技术栈

- **p5.js 1.9.0** — Canvas 2D 渲染引擎，全视口自适应
- **Canvas 2D Pixel Rendering** — `imageSmoothingEnabled=false` + `pixelDensity(1)` + 像素级对齐（PX 原子单位）
- **Graph-Distance Wind Propagation** — 分形树枝建模为有向图，BFS 计算每枝每叶到风源的最短路径，独立抵达时间
- **Web Audio API** — 带通滤波白噪声风床 + 五声音阶正弦波振荡器，实时合成无外部文件
- **Additive Blending** — 萤火虫和流星使用 `blendMode(ADD)` + 径向渐变柔光
- **Pixel Ellipse** — 纯像素椭圆填充算法，用于岛屿绘制

## 🌱 创作背景

灵感来自一个简单的念头：**树记得风**。每一次风吹过，树枝弯曲、叶子翻面——这些物理痕迹就是树的"记忆"。这件作品试图把这种记忆可视化：你的每一次手势都是一阵风，树枝会摇摆、叶片会翻转，它们短暂地"记住"了你的触碰，然后在 5 秒后渐渐回到静止——就像记忆慢慢消散，回到辽阔的夜空之中。

作品的中文名"记得风的树"呼应了一个更深层的隐喻：我们如何记住那些抚过我们生命的事物？不是牢牢抓住，而是允许痕迹存在，也允许它随时间释放。
