# Tidal Moon Moss · 玻璃钟罩里的潮汐月苔

> **Tech Keywords:** p5.js Canvas 2D pixel rendering, Canvas bezier clip glass pipeline, Web Audio OscillatorNode pentatonic synthesis, BiquadFilterNode lowpass drone, touch wave-propagation wake field, Frutiger Aero screen-blend glassmorphism, spore particle moon-gravity system

<!-- WORK_META
  slug: tidal-moon-moss
  render_engine: Canvas 2D (p5.js 1.9.0)
  particle_count: variable (spores + wakeWaves + ripples, ~60 concurrently active)
  particle_type: pixel sprites (snapped PX=2 grid, hf() hash-based procedural placement)
  shader_type: N/A (noise-free procedural, hf() sine-hash for organic variance)
  interaction: pointer press-and-hold with wave-propagation wake field, moss tip bioluminescence, long-hold spore cascade
  audio: Web Audio API OscillatorNode pentatonic synthesis (432Hz root), BiquadFilterNode lowpass drone (108/162/216Hz sine stack with LFO), sine bowl strike decay (432+216Hz)
  effects: screen blend mode + additive lighter blending, bezier clip path dome masking, radial gradient halos, CSS env-glow backdrop
  use_cases: pixel terrarium digital object, canvas glass container rendering, touch bioluminescence H5, web audio oscillator synthesis interactive, frutiger aero healing visualization, bell jar terrarium companion
  standalone: yes
  dependencies: 1 CDN (p5.js 1.9.0)
  file_size: ~22KB, 700 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Tidal Moon Moss — Frutiger Aero bell jar terrarium with glowing moon moss and spore particles](tidal-moon-moss_1.gif)

> 你碰了一下玻璃，罩里的月苔轻轻醒来，像一小片夜晚被照料。

一件封存在玻璃钟罩中的像素月苔生态作品。月苔在钟罩底部柔软铺展，53 簇叶片随潮汐节奏轻轻摇晃，5 株蕨类从苔面探出，像素茎叶逐段生长。当指尖触碰玻璃，波纹自碰触点扩散，苔尖被唤醒发出青色冷光；长按触发孢子释放——银白粒子拖着光尾升空，被上方的月光引力牵向穹顶。

钟罩用 Canvas 原生 API 绘制：`bezierCurveTo` 定义穹顶轮廓，`clip()` 裁切内部场景，`globalCompositeOperation: screen` 叠加玻璃高光。底座用径向渐变 + 椭圆描边模拟 Frutiger Aero 亚克力质感。声音层由三部分构成：低通滤波正弦叠加铺底 drone（被 LFO 轻柔调制）、触碰触发波铃衰减脉冲、以及从五声音阶（432Hz 根音）拾取的月亮音符。

---

## ✨ 预览

直接用浏览器打开 `tidal-moon-moss.html` 即可运行——p5.js 1.9.0 通过 CDN 加载，无需构建工具。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `tidal-moon-moss.html` | 完整可运行的 H5 互动作品，约 22KB |
| `tidal-moon-moss_1.gif` | 预览图：玻璃钟罩月苔互动动画 |
| `tidal-moon-moss.md` | 本说明文件 |

## 🖱️ 交互

- **触碰（pointerdown）**：轻点钟罩任意位置，波纹扩散 + 苔尖亮起 + 波铃声响起 + 月亮音符触发
- **滑动（pointermove）**：手指在玻璃上移动，苔面持续被唤醒，drone 音频亮度随移动增强
- **长按（press and hold）**：按住超过 ~0.4s 后开始持续释放孢子，银色/青色粒子带着光尾升向月光，回落水面
- **松手（pointerup）**：光晕渐暗，音频回到安静 drone 基线

## 🛠️ 技术栈

- **p5.js 1.9.0**（Canvas 2D，`noSmooth` + `pixelDensity(1)` 像素模式）
- **Canvas 原生玻璃管线**：`bezierCurveTo` 穹顶路径 + `clip()` 裁切 + `screen`/`lighter` 混合模式高光
- **Web Audio API**：`OscillatorNode` 五声音阶合成（432/485/544/648/727/864 Hz），`BiquadFilterNode` lowpass drone，`OscillatorNode` LFO 调制，双通道正弦波铃衰减
- **波前传播唤醒系统**：`wakeWaves` 数组记录每次触发的环形波前，按速度×年龄计算当前半径，苔叶/蕨类在波前经过时被注入 energy 和 memory
- **孢子粒子系统**：`hf()` 正弦哈希生成初始位置/速度随机种子，粒子受月光引力（`pullX`/`pullY`）吸引，带光尾 + 光晕渲染
- **像素网格约束**：`snap()` 函数所有坐标取整到 `PX=2` 网格，避免浮点亚像素模糊

## 🌱 创作背景

钟罩（bell jar / cloche）在博物学传统中既是保护也是展示——它把一小片自然封存起来，让你安静地注视。这件作品把月苔放进钟罩里：它不是为你表演的，它有自己的潮汐和呼吸。你碰玻璃的时候，苔醒来一会儿——然后慢慢回到它自己的夜间节奏里。银色孢子和青色光尾是夜晚碎片化的语言。
