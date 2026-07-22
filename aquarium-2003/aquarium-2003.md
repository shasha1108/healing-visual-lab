# Aquarium 2003 · 2003 水族馆

> **Tech Keywords:** p5.js Canvas 2D, Web Audio API oscillator synthesis, localStorage persistence, pixel art fish sprites, touch-glass flocking interaction, depth-of-field bokeh, chromatic dispersion, healing visualization

<!-- WORK_META
  slug: aquarium-2003
  render_engine: Canvas 2D p5.js 1.9.0
  particle_count: N/A (bubble & food sprites)
  particle_type: procedural pixel sprites
  shader_type: N/A
  interaction: touch-press (finger on glass) / tap (knock) / drag (feed)
  audio: Web Audio API oscillator synthesis (underwater ambience + bubbles + glass knock)
  effects: depth-of-field bokeh, chromatic dispersion, Polaroid photo mode, glass refraction
  use_cases: p5.js pixel art aquarium, canvas fish simulation, localStorage memory persistence, web audio underwater ambience, healing H5 screensaver, touch flocking interaction
  standalone: yes
  dependencies: 1 CDN (p5.js 1.9.0)
  file_size: ~56 KB, 1399 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Aquarium 2003 - pixel fish tank with glass refraction and named tropical fish](aquarium-2003_1.gif)

> 你小时候盯过的那个屏保活了——缸里的鱼记得你。

一只玻璃缸，五条有名字的像素热带鱼：阿橘、小蓝、金金、粉粉、斑斑。它们不是屏保里循环播放的动画——指尖贴上玻璃，鱼群会聚拢过来看你；轻敲玻璃，它们受惊四散；离开几天再回来，它们还记得你。

全部状态通过 localStorage 持久化：喂食记录、停留天数、重逢时刻。缸内还有气泡上升、景深虚化、色散玻璃和一台宝丽来相机（`?shot=1` 拍摄参数），可以随时为这缸鱼拍一张 2003 年质感的照片。

---

## ✨ 预览

直接用浏览器打开 `aquarium-2003.html` 即可运行——单文件 H5，仅依赖 p5.js 1.9.0（CDN，含国内镜像回退）。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `aquarium-2003.html` | 完整可运行的 H5 互动作品，约 56KB |
| `aquarium-2003_1.gif` | 预览动图：像素鱼缸、鱼群聚拢与宝丽来拍照 |
| `aquarium-2003.md` | 本说明文件 |

## 🖱️ 交互

- **指尖贴玻璃（按住）**：鱼群聚拢到指尖位置，隔着玻璃看你
- **轻敲玻璃（点按）**：鱼受惊四散，伴随真实的敲玻璃音效
- **投喂**：撒下鱼食，鱼群抢食
- **离开再回来**：localStorage 记住你的到访，隔几天回来会触发「重逢」时刻（`?demo=reunion&days=N` 可演示）
- **宝丽来拍照**：`?demo=polaroid` / `?shot=1` 进入拍照模式，生成一张 2003 年质感的宝丽来照片

## 🛠️ 技术栈

- p5.js 1.9.0 · Canvas 2D 固定像素舞台渲染
- Web Audio API：振荡器合成水下氛围、气泡与敲玻璃音效
- localStorage：跨会话记忆持久化（`aquarium2003` 键）
- 程序化像素鱼精灵 + 景深虚化 + 色散玻璃高光

## 🌱 创作背景

2003 年的电脑屏保里有一缸热带鱼，无数人曾盯着它发呆。这件作品让那个屏保活了过来——只是这一次，鱼也看着你，并且记得你。
