# Healing Visual Lab · 视觉疗愈实验室

> **Interactive art & digital wellness experiments** — Three.js · WebGL · Canvas particles · Web Audio API · GLSL custom shaders · Creative coding for emotional design. A growing collection of generative healing browser-art: open a page and let the visuals do what words cannot. Interaction-driven, procedural-art and shader-art throughout.
> **用代码翻译情绪**——当语言不够用时，让画面和声音替你说话。一个持续生长的数字交互疗愈作品集。大部分作品通过 CDN 加载 Three.js。

[![Topics](https://img.shields.io/badge/topics-threejs%20%7C%20webgl%20%7C%20canvas%20%7C%20particle--system%20%7C%20creative--coding%20%7C%20web--audio%20%7C%20glsl%20%7C%20digital--healing-blue)](https://github.com/shasha1108/healing-visual-lab)

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

> Click any work name to open live demo · 点击作品名打开在线演示

| # | Work / 作品 | What it does | Tech |
|:--:|------------|-------------|------|
| 1 | **[Inkmeditation · 墨池心境](inkmeditation/inkmeditation.html)** | 100K+ particles flow like ink in water, synced to breath rhythm | Three.js · GLSL · Web Audio |
| 2 | **[Breath Mirror · 息流幻镜](breath-mirror/breath-mirror.html)** | GPU fluid simulation + camera AR mirror + Brown noise engine | Three.js · GLSL · WebRTC |
| 3 | **[Unbound Mind · 释·茧](unbound-mind/unbound-mind.html)** | 150K particles cocoon dissolves with touch, 4-7-8 breathing, 432Hz singing bowl | Three.js · GLSL · Web Audio |
| 4 | **[Grand Jiangshan · 万里江山图](grand-jiangshan/grand-jiangshan.html)** | 470K particles form procedural Chinese landscape with 4D Simplex noise | Three.js · GLSL |
| 5 | **[Glass Rain · 琉璃化雨](glass-rain/glass-rain.html)** | GPU FBO fluid, touch-drag ripple perturbation, additive blending | Three.js · GLSL |
| 6 | **[Breathing Boundary · 呼吸边界](breathing-boundary/breathing-boundary.html)** | Living membrane with binaural beats (Delta 58Hz+61Hz), dual particle systems | Three.js · GLSL · Web Audio |
| 7 | **[Overthinking Engine · 过载脑区](overthinking-engine/overthinking-engine.html)** | CRT cyberpunk terminal, GSAP typewriter narrative, auto 10s healing ritual | CSS 3D · GSAP · Web Audio |
| 8 | **[Cosmic Recollection · 宇宙回响V78](cosmic-recollection/cosmic-recollection.html)** | Deep space multi-layer parallax, Three.js + Canvas textures + CSS 3D | Three.js · Canvas 2D · CSS 3D |
| 9 | **[Silent Translator · 无声翻译官](silent-translator/silent-translator.html)** | Frame-by-frame anatomical sketch, Fmaj7 chord synthesis — zero dependencies | Canvas 2D · Web Audio |
| 10 | **[Pixel Aquarium · 像素水族箱](pixel-aquarium/pixel-aquarium.html)** | 6 pixel fish with AI FSM, 25 procedural flora, CSS glassmorphism | p5.js · Canvas 2D |

<details>
<summary><b>+ 5 more works / 另外 5 件作品</b></summary>

| Work / 作品 | One-liner |
|------------|-----------|
| [Sumi-e Taichi · 水墨太极](sumi-e-taichi/sumi-e-taichi.html) | Ink drop meets rice paper — taichi gravity field, ink ripple |
| [Layered Mountains · 青绿层峦](layered-mountains/layered-mountains.html) | 250K particle landscape, 3-layer shanshui, touch scatter |
| [Deep Blue Breath · 深蓝呼吸](deep-blue-breath/deep-blue-breath.html) | 25K particles, press-and-hold breath progress, blue→gold transition |
| [Time Particle Clock · 时间流转](time-particle-clock/time-particle-clock.html) | 200K particle analog clock, mouse-drag time control, Web Audio ticks |
| [Sky Through Glass · 玻璃天空](sky-through-glass/sky-through-glass.html) | p5.js FBO masking, drag-to-wipe, VHS/CRT nostalgia overlays |

</details>

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
