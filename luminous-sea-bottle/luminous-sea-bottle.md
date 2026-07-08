# luminous-sea-bottle · 玻璃瓶里的夜光海

> **Tech Keywords:** p5.js Canvas 2D, Bayer ordered dithering, canvas glass container pipeline, touch-to-glow bioluminescence, Perlin noise algae drift, Frutiger Aero glassmorphism

<!-- WORK_META
  slug: luminous-sea-bottle
  render_engine: Canvas 2D (p5.js)
  particle_count: yes
  particle_type: pixel algae + plankton + fish (Perlin noise drift)
  shader_type: N/A
  interaction: touch-to-glow, drag-to-stir bioluminescent particles
  audio: no
  effects: Bayer ordered dithering, canvas glass clip path + bezier highlight, additive blending glow
  use_cases: pixel terrarium, frutiger aero digital object, touch bioluminescence, quiet desktop companion
  standalone: yes
  dependencies: 1 CDN (p5.js 1.9.0)
  file_size: ~30 KB, 779 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![luminous-sea-bottle · 玻璃瓶里的夜光海](luminous-sea-bottle_1.gif)

> 你碰它，它亮给你看。然后慢慢，慢慢暗回去。像深海里的一个秘密。

一个封存在像素玻璃瓶里的发光海洋生态系统。瓶内有藻类、浮游生物和小鱼在 Perlin 噪声驱动下缓缓漂移。触碰或拖拽瓶身会唤醒生物荧光——光从触碰点扩散，藻类和鱼群随之闪避和散射，6 秒后慢慢恢复平静。不碰它时，瓶子自己呼吸：微光涟漪随机出现，像深海里偶尔亮起的生物荧光。

核心交互：触摸契约——"你碰瓶身，海水发光，藻类和鱼群散开，然后慢慢回到宁静"。Bayer 有序抖动模拟水下光衰减的像素过渡。Canvas 玻璃容器路径（clip + bezier 高光弧线）定义瓶身形状和材质。

创作意图：这不是水族箱——不需要养鱼、不需要设定、不需要目标。它是一个安静的桌面物件，打开浏览器标签页放在角落里。它活着，但不要求你。这是 pixel-bloom 的第一件产品化尝试：验证"可以被拥有的数字物件"是否值得被付费。

---

## ✨ 预览

![luminous-sea-bottle · 玻璃瓶里的夜光海](luminous-sea-bottle_1.gif)

---

## 📂 文件说明

| 文件 | 说明 |
|------|------|
| `luminous-sea-bottle.html` | 自包含交互 H5——内联 CSS + p5.js CDN |
| `luminous-sea-bottle_1.gif` | 动态预览截图 |

---

## 🖱️ 交互

| 操作 | 响应 |
|------|------|
| 触碰/点击瓶身 | 触碰处发光，藻类闪避散射，光扩散 6 秒后恢复 |
| 拖拽 | 搅动瓶内水体，粒子跟随拖拽方向 |
| 无操作 | 瓶身呼吸动画 + 随机微光涟漪（Perlin noise idle life） |

---

## 🛠️ 技术栈

| 技术 | 用途 |
|------|------|
| p5.js Canvas 2D | 像素粒子渲染、FSM 生命行为、Perlin noise 漂移 |
| Bayer 有序抖动 | 水下光衰减的像素级过渡 |
| Canvas 玻璃容器路径 | clip + bezierCurveTo 瓶身 + 阶梯高光弧线 |
| 触摸/拖拽物理 | 粒子闪避距离检测 + 发光扩散衰减算法 |

---

## 🌱 创作背景

这是"玻璃瓶里的夜光海"——pixel-bloom 从情绪设计框架走向产品化的第一步。之前讨论过一个核心问题：人不为功能付费，人付费是因为一个东西可靠地触发了他们想要但不容易自己获得的情感状态。

这个作品试图验证一个命题：一个 $5 的自包含 HTML 文件，如果能成为某个人角落里安静的陪伴——像电子蜡烛、像雪花球、像一块从海边捡回来的石头——那它就值得被拥有。不是因为它有用，是因为它属于你。
