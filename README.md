# Healing Visual Lab · 视觉疗愈实验室

> **Interactive art & digital wellness experiments** — Three.js · WebGL · Canvas particles · Web Audio API · GLSL custom shaders · Creative coding for emotional design. A growing collection of generative healing browser-art: open a page and let the visuals do what words cannot. Interaction-driven, procedural-art and shader-art throughout.
> **用代码翻译情绪**——当语言不够用时，让画面和声音替你说话。一个持续生长的数字交互疗愈作品集。大部分作品通过 CDN 加载 Three.js。

[![Topics](https://img.shields.io/badge/topics-threejs%20%7C%20webgl%20%7C%20canvas%20%7C%20particle--system%20%7C%20creative--coding%20%7C%20web--audio%20%7C%20glsl%20%7C%20digital--healing-blue)](https://github.com/shasha1108/healing-visual-lab)

---

<p align="center">
  <a href="https://shasha1108.github.io/healing-visual-lab/">
    <img src="assets/previews/hero-inkmeditation.gif" alt="Inkmeditation — 100K+ particles GPU fluid simulation with breath sync" width="720">
  </a>
  <br>
  <sub><b>↑ Inkmeditation</b> — 100K+ particles, GPU fluid dynamics, taichi attractor, breath-synced rhythm. <a href="https://shasha1108.github.io/healing-visual-lab/inkmeditation/inkmeditation.html">Live demo →</a></sub>
</p>

---

## 🌀 What is this / 这是什么

**Problem:** Modern emotional life is crowded — anxiety loops, sleepless nights, somatic tension, digital overstimulation. Traditional outlets (journaling, therapy, art-making) have learning curves. But interactive visuals don't. You don't need any skill. You just open a page.

**Solution:** Every piece in this repo is a self-contained H5 interactive experience. No login. No payment. No psychoeducation reading required. You watch. You touch. You breathe with the algorithm.

**Technical approach:** Each `.html` file is a standalone creative-coding experiment — particle systems (10K–500K particles), GPU fluid simulation, custom GLSL fragment shaders, Web Audio API synthesized soundscapes, CSS 3D spatial animation, and mouse/touch interaction design. Most works load Three.js r128 via CDN; `silent-translator` is the only zero-dependency work.

**问题：** 现代人的情绪太拥挤了——焦虑、失眠、躯体化、过度自我审视。传统的表达出口有门槛，但交互式视觉没有。

**方案：** 每件作品是一个独立的 H5 页面。打开浏览器就能进入一段短暂的自我修复。你只需要看、听、触碰。

**技术路线：** HTML/CSS/JS，无构建步骤。Three.js WebGL + Canvas 2D 粒子系统、GPU 流体模拟、自定义 GLSL 着色器、Web Audio 合成音景、CSS 3D 空间动画、鼠标/触屏交互设计。大部分作品通过 CDN 加载 Three.js r128。

**一个哲学内核贯穿所有作品：**

> 身体记得的，代码可以翻译。代码翻译不了的，时间可以消融。
> What the body remembers, code can translate. What code cannot translate, time dissolves.

---

## 📦 Works / 作品目录

<p align="center">
  <b>🖱️ Click any preview to open the live demo</b>
</p>

<table align="center">
  <tr>
    <td align="center"><a href="https://shasha1108.github.io/healing-visual-lab/inkmeditation/inkmeditation.html"><img src="assets/previews/thumb-inkmeditation.gif" width="200" alt="Inkmeditation"><br><sub>🎨 粒子系统<br>Inkmeditation</sub></a></td>
    <td align="center"><a href="https://shasha1108.github.io/healing-visual-lab/breath-mirror/breath-mirror.html"><img src="assets/previews/thumb-breath-mirror.gif" width="200" alt="Breath Mirror"><br><sub>🔮 GPU流体<br>Breath Mirror</sub></a></td>
    <td align="center"><a href="https://shasha1108.github.io/healing-visual-lab/breathing-boundary/breathing-boundary.html"><img src="assets/previews/thumb-breathing-boundary.gif" width="200" alt="Breathing Boundary"><br><sub>🎵 音频疗愈<br>Breathing Boundary</sub></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://shasha1108.github.io/healing-visual-lab/overthinking-engine/overthinking-engine.html"><img src="assets/previews/thumb-overthinking-engine.gif" width="200" alt="Overthinking Engine"><br><sub>🖥️ CSS3D赛博<br>Overthinking Engine</sub></a></td>
    <td align="center"><a href="https://shasha1108.github.io/healing-visual-lab/pixel-aquarium/pixel-aquarium.html"><img src="assets/previews/thumb-pixel-aquarium.gif" width="200" alt="Pixel Aquarium"><br><sub>🐠 像素艺术<br>Pixel Aquarium</sub></a></td>
    <td align="center" bgcolor="#f6f8fa"><br><sub><i>+ 10 more works below</i><br>⬇️</sub></td>
  </tr>
</table>

---

<details open>
<summary><b>🌀 Three.js / WebGL</b> &ensp;<sub>13 works</sub></summary>

- [水墨太极 / Sumi-e Taichi](sumi-e-taichi/sumi-e-taichi.html) — 一滴墨落入宣纸，既是破坏也是开始
- [墨池心境 / Inkmeditation](inkmeditation/inkmeditation.html) — 十万粒子实时流体，随呼吸节律沉浮
- [宇宙回响 V78 / Cosmic Recollection](cosmic-recollection/cosmic-recollection.html) — 万物皆有裂痕，那是光照进来的地方
- [青绿·层峦 / Layered Mountains](layered-mountains/layered-mountains.html) — 触之即散，聚散随缘
- [琉璃化雨 / Glass Rain](glass-rain/glass-rain.html) — 眼泪落尽，便见晴空
- [息流·幻镜 / Breath Mirror](breath-mirror/breath-mirror.html) — GPU 流体 + 棕噪引擎，呼吸即镜像
- [呼吸边界 / Breathing Boundary](breathing-boundary/breathing-boundary.html) — 一层活着的、会呼吸的边界
- [深蓝呼吸 V204 / Deep Blue Breath](deep-blue-breath/deep-blue-breath.html) — 深蓝之中，金色粒子缓缓上升
- [万里江山图 / Grand Jiangshan](grand-jiangshan/grand-jiangshan.html) — 470K 粒子过程化生成万里江山
- [时间流转 / Time Particle Clock](time-particle-clock/time-particle-clock.html) — 时间是流动的粒子，拖拽加速松开即止
- [释·茧 / Unbound Mind](unbound-mind/unbound-mind.html) — 轻轻抚摸，茧会自己松开
- [无声的翻译官 / Silent Translator](silent-translator/silent-translator.html) — 身体替你说了说不出的话
- [过载脑区 / Overthinking Engine](overthinking-engine/overthinking-engine.html) — 过度清醒地审视自己，正在毁掉我们的生活

</details>

<details open>
<summary><b>🎨 Canvas / p5.js</b> &ensp;<sub>2 works</sub></summary>

- [玻璃天空 / Sky Through Glass](sky-through-glass/sky-through-glass.html) — Frutiger Aero 美学，指腹划过擦开 VHS 噪点
- [像素水族箱 / Pixel Aquarium](pixel-aquarium/pixel-aquarium.html) — 像素小鱼在毛玻璃水箱游动，单击投食双击敲玻璃

</details>

---

## 🖱️ How to use / 如何使用

Each subdirectory is a **standalone H5 page** (most load Three.js r128 via CDN):
每个子目录都是一个**独立 H5 页面**（大部分通过 CDN 加载 Three.js r128）：

```bash
# 1. Open directly in browser / 浏览器直接打开
open <slug>/<slug>.html

# 2. Any HTTP server / 任意本地服务
npx serve <slug>/

# 3. GitHub Pages (already enabled) / 已启用
# https://shasha1108.github.io/healing-visual-lab/<slug>/<slug>.html
```

---

## 🛠️ Technical landscape / 技术全景

| Domain / 领域 | Techniques used / 使用的技术 |
|---------------|---------------------------|
| **Particle systems / 粒子系统** | Three.js WebGL point sprites, GPU instanced rendering, Canvas 2D, 10K–500K real-time particles |
| **Fluid simulation / 流体模拟** | Navier-Stokes simplified, velocity fields, curl noise, semi-Lagrangian advection |
| **Custom shaders / 自定义着色器** | GLSL fragment shaders, simplex noise, FBM, Fresnel effects, vertex displacement, organic undulation |
| **Audio synthesis / 音频合成** | Web Audio API oscillators, binaural beats (Delta/Theta), ASMR-grade chime envelopes, ambient drones |
| **Interaction / 交互设计** | Click/drag physics, long-press detection, ripple/particle collision response, breath-cycle sync |
| **Animation / 动画** | requestAnimationFrame, GSAP timelines, CSS 3D transforms, multi-layer parallax |
| **Rendering / 渲染** | ACES filmic tone mapping, additive blending, post-processing effects, CRT scanlines |

---

## 🌱 Creative philosophy / 创作理念

This is not art. This is a toolkit.
This is not a portfolio. This is an emotional first-aid kit.

Every piece was born from the same impulse: modern life packs too much emotion into too little space. Anxiety, overthinking, insomnia, somatic stress — everyone carries a backlog of unspoken things. Interactive visuals are a release valve. No skill required. Just open the page and let the algorithm sit with you for a while.

**这不是艺术。这是工具。不是作品展示。是情绪急救箱。**

---

## 📂 Repo structure / 仓库结构

```
<slug>/
├── <slug>.html      ← Self-contained runnable H5 / 完整可运行的交互页
├── <slug>.md        ← Bilingual work description / 中英双语作品说明
└── <slug>_N.jpg     ← Preview screenshots / 预览截图
```

New works are pushed via automated pipeline with consistent naming conventions.
新作品通过自动化脚本推送，保持命名约定一致。

---

## 📋 Continuously updated / 持续更新

> If one of these pieces made you feel seen — that's the only reason this repo exists.
> 如果其中某件作品让你感到被看见——那就是这个仓库存在的全部意义。

---

*Last updated: 2026-06-26 | Works: 15 | Languages: 中文 · English | Tech: Three.js · WebGL · Canvas · Web Audio · GSAP*

---

## 🤝 Related / 相关项目

- [h5-publish-skill](https://github.com/shasha1108/h5-publish-skill) — The Claude Code skill that auto-publishes works to this repo with GEO/SEO optimization
- [healing-space](https://github.com/shasha1108/healing-space) — Claude Code skill for generating touch-driven healing H5 pages (p5.js / Three.js / WebGL / Web Audio)

- [inner-voice](https://github.com/shasha1108/inner-voice) — Xiaohongshu emotional content creation skill
- [pixel-bloom](https://github.com/shasha1108/pixel-bloom) — Pixel art + Frutiger Aero H5 generator

<p align="center"><sub>Source code under <a href="LICENSE">MIT License</a> | 网站源代码采用 MIT 协议</sub></p>
