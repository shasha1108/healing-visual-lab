# Transparent Dream Stratigraph · 透明梦境地层仪

> **Tech Keywords:** Canvas 2D pixel art, p5.js createGraphics offscreen rendering, Web Audio API OscillatorNode synthesis, Canvas bezierCurve glass shell, spring-damped mechanism physics, deterministic procedural strata, Pointer Events interaction, localStorage persistence

<!-- WORK_META
  slug: transparent-dream-stratigraph
  render_engine: Canvas 2D (p5.js 1.9.4)
  particle_count: dynamic mineral motes (~10 per interaction)
  particle_type: pixel rect particle system
  shader_type: N/A
  interaction: pointer-down crown rotation + tap-to-wake fossil
  audio: Web Audio API OscillatorNode synthesis (triangle/sine, exponentialRampToValueAtTime, detune)
  effects: Canvas globalCompositeOperation screen blend, Canvas shadowBlur depth, lerpColor energy transitions, deterministic hash-based procedural variation
  use_cases: canvas 2d pixel art healing, p5.js createGraphics offscreen, web audio oscillator synthesis H5, procedural strata generation, interactive dream instrument
  standalone: yes
  dependencies: 1 CDN (p5.js 1.9.4)
  file_size: ~26 KB, 799 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Transparent Dream Stratigraph - pixel art geological instrument with animated crown rotation and glowing strata layers](transparent-dream-stratigraph_1.gif)

> 转动冠轮，地层仪将未说出口的梦压入一层发光的地质年轮。

一件像素风格的透明梦境仪器。核心是一块 112×192 像素的 offscreen canvas，渲染着由确定性哈希算法程序化生成的地质层——每一层都有独特的像素纹理、矿物颜色族（Pixel / Dream / Amber）和化石形态。转动顶部的 12 齿冠轮，仪器以弹簧阻尼物理驱动旋转，同时生成一层新的地层并发出合成器音效；轻敲核心窗口内的任意地层，化石苏醒、矿物微粒迸发、能量以指数衰减缓缓消退。

核心技术特征：p5.js createGraphics 实现的离屏像素渲染管线；Canvas 2D 原生 API 绘制的透明玻璃外壳（bezierCurve + screen 混合模式 + shadowBlur 深度）；Web Audio API 的 OscillatorNode + GainNode + exponentialRampToValueAtTime 合成的机构转动音和地层唤醒音；localStorage 持久化地层计数，跨会话保留记忆。

---

## ✨ 预览

直接用浏览器打开 `transparent-dream-stratigraph.html` 即可运行——单文件、零构建、1 个 CDN 依赖（p5.js 1.9.4）。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `transparent-dream-stratigraph.html` | 完整可运行的 H5 互动作品，约 26KB |
| `transparent-dream-stratigraph_1.gif` | 预览动画：冠轮旋转 + 地层推进 + 化石唤醒效果 |
| `transparent-dream-stratigraph.md` | 本说明文件 |

## 🖱️ 交互

- **转动冠轮**：点击 / 触摸仪器顶部的圆形冠轮区域，触发弹簧阻尼旋转动画，同时生成一层新的程序化地层
- **唤醒化石**：点击 / 触摸核心窗口内的任意地层，该层的化石发光苏醒，矿物微粒粒子从点击位置迸发
- **持久记忆**：地层计数自动保存到 localStorage，下次打开时恢复进度；侧边仪表显示当前齿轮齿位
- **无障碍适配**：检测 `prefers-reduced-motion`，减弱动效幅度；音频在首次交互后才初始化

## 🛠️ 技术栈

- **渲染引擎**：Canvas 2D (p5.js 1.9.4)，p5.createGraphics 离屏像素画布 (112×192px)
- **玻璃外壳**：Canvas 2D 原生 API — bezierCurve 路径 + createLinearGradient 渐变 + globalCompositeOperation screen 高光 + shadowBlur 投影
- **程序化地层**：确定性哈希函数 hash01 (sin-based) 驱动颜色族分配、纹理变化、化石形态和位置的伪随机生成
- **物理动画**：弹簧阻尼系统 (stiffness=92, damping=14) 驱动冠轮旋转；指数衰减 (exp) 驱动脉冲能量消退
- **音频合成**：Web Audio API — OscillatorNode (triangle/sine) + GainNode + exponentialRampToValueAtTime + detune，首次触摸初始化 AudioContext
- **触摸交互**：Pointer Events API (pointerdown/pointermove)，passive:false 阻止默认行为，坐标空间从屏幕映射到设计基准 (720×960)
- **状态持久化**：localStorage JSON 序列化地层计数，跨会话恢复

## 🌱 创作背景

梦境地层仪是一个关于「未说出口的话」的隐喻装置。每一层地层都是时间的一个切片，封存着一个未被表达的梦——转动冠轮不是破坏，而是让新的记忆覆盖旧的沉积。像素材质的选择呼应了记忆的不精确性：每个像素都是一个不可再分的原子事实，而化石的形态——十字星、脊柱、方舟——则是三种不同的沉默形态。Dream Strata Mint 配色（Cyber Mint + Lavender Mist）在暗色地质基调中保留一丝冷光，暗示梦的透明性：它们就在那里，但你看不穿。
