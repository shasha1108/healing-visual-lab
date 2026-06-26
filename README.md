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

> Click to open live demo · 点击作品名直接体验

| # | Work / 作品 | 核心理念 / Concept | Tech |
|:--:|------------|-------------------|------|
| 1 | **[Inkmeditation · 墨池心境](inkmeditation/inkmeditation.html)** | 一滴墨落入水中，十万粒子随呼吸节律沉浮。An ink drop in water — 100K particles breathe with you. | Three.js · GLSL · Web Audio |
| 2 | **[Breath Mirror · 息流幻镜](breath-mirror/breath-mirror.html)** | 摄像头将你的影像化为GPU流体雾面，呼吸即镜像。Camera turns you into GPU fluid fog — breathing is the mirror. | Three.js · GLSL · WebRTC |
| 3 | **[Unbound Mind · 释·茧](unbound-mind/unbound-mind.html)** | 情绪的茧被指尖轻轻抚开，150K粒子从焦虑过渡到平静。A cocoon dissolves under your fingertips — particles shift from anxiety to calm. | Three.js · GLSL · Web Audio |
| 4 | **[Grand Jiangshan · 万里江山图](grand-jiangshan/grand-jiangshan.html)** | 470K粒子在4D Simplex噪声中生成程序化山水，可旋转探索。470K particles form procedural landscape — rotate and explore. | Three.js · GLSL |
| 5 | **[Glass Rain · 琉璃化雨](glass-rain/glass-rain.html)** | 眼泪化为琉璃，指尖划过玻璃表面激起涟漪。Tears become glass — your fingertip sends ripples across the surface. | Three.js · GLSL |
| 6 | **[Breathing Boundary · 呼吸边界](breathing-boundary/breathing-boundary.html)** | 一层活着的膜在呼吸，双耳节拍（Delta 58Hz+61Hz）引导脑波。A living membrane breathes — binaural beats guide your brainwaves. | Three.js · GLSL · Web Audio |
| 7 | **[Overthinking Engine · 过载脑区](overthinking-engine/overthinking-engine.html)** | CRT终端里，过度思考被逐字敲出，10秒后自动释怀。Overthinking typed out on a CRT terminal — auto-releases after 10 seconds. | CSS 3D · GSAP · Web Audio |
| 8 | **[Cosmic Recollection · 宇宙回响V78](cosmic-recollection/cosmic-recollection.html)** | 多层深空视差——万物皆有裂痕，那是光照进来的地方。Deep space parallax — cracks are where the light gets in. | Three.js · Canvas 2D · CSS 3D |
| 9 | **[Silent Translator · 无声翻译官](silent-translator/silent-translator.html)** | 身体替你说了说不出的话，逐帧素描 + Fmaj7和弦，零依赖。Your body speaks what you can't — frame-by-frame sketch + Fmaj7 chords, zero dependencies. | Canvas 2D · Web Audio |
| 10 | **[Pixel Aquarium · 像素水族箱](pixel-aquarium/pixel-aquarium.html)** | 6条像素小鱼在毛玻璃水箱游动，点击投食、双击敲玻璃。6 pixel fish in a frosted glass tank — tap feed, double-tap knock. | p5.js · Canvas 2D |

<details>
<summary><b>+ 5 more works / 另外 5 件作品</b></summary>

| Work / 作品 | 核心理念 / Concept |
|------------|-------------------|
| [Sumi-e Taichi · 水墨太极](sumi-e-taichi/sumi-e-taichi.html) | 一滴墨落入宣纸，既是破坏也是开始——太极引力场中的墨韵流转。Ink meets rice paper — destruction and beginning in a taichi gravity field. |
| [Layered Mountains · 青绿层峦](layered-mountains/layered-mountains.html) | 250K粒子堆叠出青绿山水，触之即散，聚散随缘。250K particles form layered shanshui — touch scatters, time gathers. |
| [Deep Blue Breath · 深蓝呼吸](deep-blue-breath/deep-blue-breath.html) | 深蓝之中，金色粒子随按住呼吸的节奏缓缓升起。In deep blue, golden particles rise with the rhythm of held breath. |
| [Time Particle Clock · 时间流转](time-particle-clock/time-particle-clock.html) | 时间是流动的粒子——200K粒子构成的表盘，拖拽加速、松手即止。Time is flowing particles — 200K particle clock, drag to speed up. |
| [Sky Through Glass · 玻璃天空](sky-through-glass/sky-through-glass.html) | 指腹划过毛玻璃，擦开VHS噪点露出天空——Frutiger Aero美学的怀旧疗愈。Finger wipes frosted glass to reveal sky — Frutiger Aero nostalgia. |

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

**Code translates what words cannot.** Every piece in this repo starts with an emotional state that's hard to name — and becomes an interactive experience that doesn't need explanation.

**What I believe:**
- **Zero friction.** Open a page. No frameworks, no build steps, no sign-up. Just the browser.
- **Less is more.** Vanilla HTML/CSS/JS wherever possible. Dependencies only when they earn their place.
- **Interaction over instruction.** The best interface doesn't tell you what to do. You touch, it responds, you understand.
- **Emotion deserves engineering.** Feelings are complex systems. So is the code that holds them.

Each `.html` file is a self-contained experiment. Open it, interact, let the algorithm sit with you for a moment.

**代码翻译语言说不清的东西。** 每件作品始于一个难以命名的情绪——焦虑、疲惫、说不出口的重量——然后变成一个不需要解释的交互体验。

**我相信的：**
- **零摩擦。** 打开页面就行。没有框架、没有构建步骤、不需要注册。只有浏览器。
- **少即是多。** 尽可能纯 HTML/CSS/JS。依赖项只在值得时才引入。
- **交互胜过说明。** 最好的界面不告诉你怎么做——你触碰，它回应，你就懂了。
- **情绪值得被认真工程化。** 感情是复杂系统。承载它们的代码也是。

每个 `.html` 文件是一个独立的实验。打开、交互、让算法陪你待一会儿。

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
