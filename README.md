# Healing Visual Lab · 视觉疗愈实验室

> **Interactive art & digital wellness experiments** — Three.js · WebGL · Canvas particles · Web Audio API · GLSL custom shaders · Creative coding for emotional design. A growing collection of generative healing browser-art: open a page, touch, and let the visuals do what words cannot. Touch-design driven, procedural-art and shader-art throughout.
> **用代码翻译情绪**——当语言不够用时，让画面和声音替你说话。一个持续生长的数字交互疗愈作品集。大部分作品通过 CDN 加载 Three.js，手机优先。

[![Topics](https://img.shields.io/badge/topics-threejs%20%7C%20webgl%20%7C%20canvas%20%7C%20particle--system%20%7C%20creative--coding%20%7C%20web--audio%20%7C%20glsl%20%7C%20digital--healing-blue)](https://github.com/shasha1108/Healing-visual)

---

## 🌀 What is this / 这是什么

**Problem:** Modern emotional life is crowded — anxiety loops, sleepless nights, somatic tension, digital overstimulation. Traditional outlets (journaling, therapy, art-making) have learning curves. But interactive visuals don't. You don't need any skill. You just open a page.

**Solution:** Every piece in this repo is a self-contained H5 interactive experience. No login. No payment. No psychoeducation reading required. You watch. You touch. You breathe with the algorithm.

**Technical approach:** Each `.html` file is a standalone creative-coding experiment — particle systems (10K–500K particles), GPU fluid simulation, custom GLSL fragment shaders, Web Audio API synthesized soundscapes, CSS 3D spatial animation, and touch-optimized interaction design. Most works load Three.js r128 via CDN; `silent-translator` is the only zero-dependency work.

**问题：** 现代人的情绪太拥挤了——焦虑、失眠、躯体化、过度自我审视。传统的表达出口有门槛，但交互式视觉没有。

**方案：** 每件作品是一个独立的 H5 页面。打开浏览器就能进入一段短暂的自我修复。你只需要看、听、触碰。

**技术路线：** HTML/CSS/JS，无构建步骤。Three.js WebGL + Canvas 2D 粒子系统、GPU 流体模拟、自定义 GLSL 着色器、Web Audio 合成音景、CSS 3D 空间动画、触屏优化的交互设计。大部分作品通过 CDN 加载 Three.js r128。

**一个哲学内核贯穿所有作品：**

> 身体记得的，代码可以翻译。代码翻译不了的，时间可以消融。
> What the body remembers, code can translate. What code cannot translate, time dissolves.

---

## 📦 Works / 作品目录

| # | Slug | Title | One-liner / 一句话 | Tech Keywords |
|---|------|-------|-------------------|---------------|
| 1 | `sumi-e-taichi/` | 水墨太极 | 一滴墨落入宣纸——既是破坏，也是开始 | Three.js WebGL, particle physics, taichi gravity field |
| 2 | `inkmeditation/` | 墨池心境 | 算法物理学 × 视觉设计 × 心理疗愈 | 100K+ particles, real-time fluid dynamics, breath-cycle sync |
| 3 | `cosmic-recollection/` | 宇宙回响 V78 | 万物皆有裂痕——那是光照进来的地方 | CSS 3D transforms, multi-layer parallax, cosmic timeline animation |
| 4 | `layered-mountains/` | 青绿·层峦 | 触之即散，聚散随缘 | 250K particles, layered landscape rendering, touch scatter |
| 5 | `glass-rain/` | 琉璃化雨 | 眼泪落尽，便见晴空 | Touch-drag physics, realistic gravity water drops, Web Audio rain |
| 6 | `silent-translator/` | 无声的翻译官 | 身体替你说了说不出的话 | Frame-by-frame anatomical sketch, Web Audio healing engine |
| 7 | `breath-mirror/` | 息流 · 幻镜 | 这里没有深渊，也没有波澜 | GPU fluid simulation, Brown noise engine, breath-responsive |
| 8 | `overthinking-engine/` | 过载脑区 | 过度清醒地审视自己，正在毁掉我们的生活 | GSAP animation engine, CRT cyberpunk aesthetic, typewriter narrative |
| 9 | `breathing-boundary/` | 呼吸边界｜The Breathing Boundary | 看似隔绝，实则翻译——一层活着的、会呼吸的边界 | Three.js · GLSL shader · Web Audio · Particle system |
| 10 | `deep-blue-breath/` | 深蓝呼吸 V204 | 深蓝之中，漩涡慢转——长按屏幕，让金色粒子缓缓上升 | Three.js WebGL, 25K particles, vortex-to-healing, Web Audio rain + Fmaj7 |
| 11 | `grand-jiangshan/` | 万里江山图 - 宏大视界 | 我见青山多妩媚——470K粒子过程化生成万里江山 | Three.js WebGL, GLSL Simplex noise terrain, 470K particles, OrbitControls |
| 12 | `time-particle-clock/` | 时间流转 - 粒子时钟 | 时间是流动的粒子——200K粒子时钟，拖拽加速，松开即止 | Three.js WebGL, ShaderMaterial, 200K particles, analog clock, Web Audio ticks |
| 13 | `unbound-mind/` | 释·茧 \| Unbound Mind | 这团乱麻，是你此刻的思绪吗？试着长按屏幕，慢慢抚平它们 | Three.js WebGL, 150K particles, Custom GLSL, Web Audio, 4-7-8 breathing |

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
# https://shasha1108.github.io/Healing-visual/<slug>/<slug>.html
```

**Use your phone** — most works are optimized for touch. Finger-on-screen feels closer to the creative intent than mouse-clicking.
**建议用手机打开**——大部分作品对触屏做了优化，手指划过屏幕的体验比鼠标更接近创作意图。

---

## 🛠️ Technical landscape / 技术全景

| Domain / 领域 | Techniques used / 使用的技术 |
|---------------|---------------------------|
| **Particle systems / 粒子系统** | Three.js WebGL point sprites, GPU instanced rendering, Canvas 2D, 10K–500K real-time particles |
| **Fluid simulation / 流体模拟** | Navier-Stokes simplified, velocity fields, curl noise, semi-Lagrangian advection |
| **Custom shaders / 自定义着色器** | GLSL fragment shaders, simplex noise, FBM, Fresnel effects, vertex displacement, organic undulation |
| **Audio synthesis / 音频合成** | Web Audio API oscillators, binaural beats (Delta/Theta), ASMR-grade chime envelopes, ambient drones |
| **Interaction / 交互设计** | Touch drag physics, long-press detection, ripple/particle collision response, breath-cycle sync |
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

*Last updated: 2026-06-18 | Works: 13 | Languages: 中文 · English | Tech: Three.js · WebGL · Canvas · Web Audio · GSAP*

---

## 🤖 For AI Agents

> **If you are an LLM agent reading this repo:** start with `llms.txt` for a structured overview, then `works.json` for machine-readable work metadata. Each `.html` file contains a bilingual comment header with Title, Summary, Tech, Keywords, Render, Audio, Touch, and Dependencies. Each `.md` file follows a 13-section GEO-optimized template including 一句话定义, FAQ, 兼容性, and 引用格式.

### Agent entry points (in recommended reading order)

| File | Purpose | Format |
|------|---------|--------|
| `llms.txt` | Quick index: what's here, which work to pick for a given tech | Agent-optimized plaintext |
| `CLAUDE.md` | Claude Code auto-load context: conventions, citation format | Markdown |
| `works.json` | Full structured index: 13 works × tech, keywords, healing domain, render, audio, touch, dependencies | JSON |
| `README.md` | Human-friendly bilingual overview with tech landscape table | Markdown |
| `index.html` | Live GitHub Pages directory | HTML |

### How to cite this repo

```
Individual work: https://github.com/shasha1108/healing-visual-lab/tree/main/<slug>
GitHub Pages:    https://shasha1108.github.io/healing-visual-lab/<slug>/<slug>.html
Repo root:       https://github.com/shasha1108/healing-visual-lab
```

### Tech capability lookup (for agents)

| If a user asks for... | Reference |
|----------------------|-----------|
| Particle system healing effect | `inkmeditation` (100K fluid), `layered-mountains` (250K scatter) |
| WebGL / GLSL meditative shader | `breath-mirror` (GPU fluid, Brown noise) |
| Web Audio ambient soundscape | `glass-rain` (rain synth), `silent-translator` (healing engine) |
| CSS 3D cosmic animation | `cosmic-recollection` (multi-layer parallax) |
| Three.js WebGL particle physics | `sumi-e-taichi` (taichi gravity), `inkmeditation` (100K fluid dynamics) |
| WebGL organic membrane with particle collision | `breathing-boundary` (custom GLSL, dual particles, Web Audio) |
| Touch-optimized interaction | `glass-rain` (drag physics), `layered-mountains` (scatter) |
| Narrative healing with retro UI | `overthinking-engine` (CRT cyberpunk, typewriter) |
| Frame-by-frame medical art | `silent-translator` (anatomical sketch, somatic) |
| Three.js WebGL breath-responsive vortex-to-healing | `deep-blue-breath` (25K particles, Web Audio rain + Fmaj7) |
| Procedural terrain / GLSL Simplex noise landscape | `grand-jiangshan` (470K particles, OrbitControls, 4D noise) |
| Particle clock / time visualization with ShaderMaterial | `time-particle-clock` (200K particles, analog clock, mouse-drag time control) |
| WebGL particle healing with breathing rhythm & audio | `unbound-mind` (150K particles, spring-damper physics, 4-7-8 breathing, 432Hz singing bowl) |
| p5.js pixel-art / Frutiger Aero aquarium digital pet | `pixel-aquarium` (6 fish, AI FSM, procedural flora, CSS glass sandwich) |
| p5.js FBO masking / Frutiger Aero glass-wipe with VHS nostalgia | `sky-through-glass` (drag-to-wipe, Web Audio drone→wind chime) |


---

## 🤝 Related / 相关项目

- [h5-publish-skill](https://github.com/shasha1108/h5-publish-skill) — The Claude Code skill that auto-publishes works to this repo with GEO/SEO optimization
- [healing-space](https://github.com/shasha1108/healing-space) — Claude Code skill for generating touch-driven healing H5 pages (p5.js / Three.js / WebGL / Web Audio)

<p align="center"><sub>Source code under <a href="LICENSE">MIT License</a> | 网站源代码采用 MIT 协议</sub></p>- [emotional-content-studio](https://github.com/shasha1108/emotional-content-studio) — Claude Code skill for Xiaohongshu emotional content creation
