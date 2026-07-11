# Firefly Seed Jar · 密封瓶里的萤火种子

> **Tech Keywords:** p5.js Canvas 2D pixel rendering, Web Audio API BiquadFilter low-pass drone, OscillatorNode sine-wave chime synthesis, Canvas globalCompositeOperation additive blending, fixed pixel grid snap (PX=2), press-and-hold touch interaction, glass bottle Frutiger Aero highlights, seed bank simulation

<!-- WORK_META
  slug: firefly-seed-jar
  render_engine: Canvas 2D p5.js 1.9.0
  particle_count: N/A
  particle_type: pixel sprite particles via fillRect on Canvas 2D
  shader_type: N/A
  interaction: press-and-hold, touch-drag
  audio: Web Audio API OscillatorNode sine-wave chime strikes, BiquadFilter low-pass drone, dual-OscillatorNode drone synthesis (108Hz + 162Hz), GainNode linearRampToValueAtTime + exponentialRampToValueAtTime
  effects: additive blending (globalCompositeOperation: lighter), screen blending (globalCompositeOperation: screen), radial gradients, pixel grid snapping (PX=2), Bézier curve glass highlights
  use_cases: p5.js interactive terrarium, web audio healing visualization, canvas glass bottle rendering, pixel seed bank H5, press-and-hold particle animation, frutiger aero H5
  standalone: yes
  dependencies: 1 CDN (p5.js 1.9.0)
  file_size: ~22 KB, 697 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Firefly Seed Jar — glass bottle with amber crystal seeds glowing on shelves](firefly-seed-jar_1.gif)

> 你碰到哪颗琥珀晶种，它就短暂相信春天来了，探出一根被拴住的萤光触角。

密封玻璃瓶里沉睡着成排的琥珀晶种——每一颗都是等待春天的萤火虫。手指按上瓶身，最近的那颗种子就会苏醒，探出一根发光触角轻轻摇曳；松手后，触角缓缓缩回，种子重新入眠。触角的长度和亮度跟随按压时长变化，而玻璃瓶上的高光闪烁呼应着每一次触碰。

画面严格运行在 2px 像素网格上，所有坐标通过 `snap()` 对齐，配合 `globalCompositeOperation: lighter` 实现萤光叠加发光。玻璃瓶轮廓用 Canvas Bézier 曲线绘制，高光层采用 `screen` 混合模式模拟 Frutiger Aero 风格的湿润玻璃质感。音频层面，两个 OscillatorNode 生成持续低音 drone（108Hz + 162Hz 纯音），通过 BiquadFilter 低通滤波塑造温暖质感，每次触碰触发三音泛音列 chime（648Hz / 864Hz / 1296Hz），音高随种子活跃度动态漂移。

---

## ✨ 预览

直接用浏览器打开 `firefly-seed-jar.html` 即可运行——基于 p5.js 1.9.0，单文件零构建，Canvas 2D 像素渲染 + Web Audio 合成音频。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `firefly-seed-jar.html` | 完整可运行的 H5 互动作品，约 22KB |
| `firefly-seed-jar_1.gif` | 预览图：按压唤醒种子、触角生长的动态演示 |
| `firefly-seed-jar.md` | 本说明文件 |

## 🖱️ 交互

- **按住瓶身任意位置**：最近的琥珀种子被唤醒，探出发光触角，周围种子轻微响应
- **按住拖动**：手指划过不同种子，依次唤醒经过的种子
- **松手**：触角缓缓缩回，种子恢复休眠状态，玻璃高光逐渐消退
- **音频反馈**：每次触碰触发玻璃钟声般的泛音列；触角越长，背景 drone 音高越亮

## 🛠️ 技术栈

- **渲染**：Canvas 2D (p5.js 1.9.0)，固定 720×960 画布，2px 像素网格 (`snap()` 对齐所有坐标)
- **玻璃效果**：Canvas `bezierCurveTo` 绘制瓶身轮廓，`screen` 混合模式高光，`lighter` 混合模式内部发光
- **粒子系统**：种子库由 5 层搁板共 ~29 个种子荚 + ~130 颗琥珀种子组成，每颗种子有独立的 sprout/targetSprout 缓动、翻转动画、休眠脉冲
- **音频合成**：Web Audio API — 双 OscillatorNode 生成 drone (108Hz + 162Hz sine)，BiquadFilter 低通滤波，三音泛音列 chime (648Hz/864Hz/1296Hz) 每次触碰触发，drone 频率随最强触角动态漂移
- **交互**：Pointer Events (pointerdown/move/up/cancel)，曼哈顿距离最近种子匹配，按压强度驱动 sprout 目标值缓动

## 🌱 创作背景

"密封瓶里的萤火种子" 延续了 pixel-bloom 系列的玻璃容器主题——将生命封存于透明瓶中的古典浪漫。每一颗琥珀色种子既是像素符号也是情感隐喻：沉睡时暗淡如矿物，被触碰时却会 "相信春天来了"，探出柔软的光之触角。这个作品试图用像素的确定性和音频的有机漂移，在玻璃瓶的封闭空间里制造一种可触碰的渴望。
