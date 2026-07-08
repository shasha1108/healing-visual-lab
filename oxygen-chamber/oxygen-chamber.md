# oxygen-chamber · 内心气象日记 · 60s 氧气舱

> **Tech Keywords:** p5.js Canvas 2D, Web Audio API OscillatorNode, BiquadFilterNode, Bayer ordered dithering, Frutiger Aero glassmorphism, mood-based particle system, 60s breathing timer

<!-- WORK_META
  slug: oxygen-chamber
  render_engine: Canvas 2D (p5.js)
  particle_count: yes
  particle_type: pixel weather particles (rain/snow/sun)
  shader_type: N/A
  interaction: mood button switching, touch-to-breathe
  audio: Web Audio API oscillator synthesis (ambient drone + breathing cue)
  effects: Bayer ordered dithering, Frutiger Aero glass overlay, env-glow color shift
  use_cases: pixel weather diary, emotional breathing tool, frutiger aero interactive, 60s meditation H5
  standalone: yes
  dependencies: 2 CDN (p5.js 1.9.0)
  file_size: ~45 KB, 1102 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![预览](oxygen-chamber_1.gif)

> 60秒情绪氧气舱——选一种天气，让内心在玻璃小屋里安静呼吸。

一个像素天气系统被封存在 Frutiger Aero 玻璃容器中。顶部情绪栏切换五种内心气象——晴天、微雨、飘雪、雷暴、雾霭。点击玻璃开始60秒呼吸倒计时，画面随情绪切换色调、粒子、和声音。没有文字，没有任务——只是一个属于你的微气候，在浏览器角落里安静地活着。

核心交互：情绪切换按钮 + 点击玻璃容器开始/重置 60 秒计时器。Web Audio 合成环境音随情绪变化。像素粒子系统（雨滴/雪花/阳光）在玻璃容器内实时渲染，配合 Bayer 有序抖动模拟连续色调过渡。

创作意图：爆款重构——重新思考"情绪日记"的交互形态。去文字化、去打卡化、去社交化。只保留一个简单机制：选情绪 → 进玻璃屋 → 待60秒 → 出来。像洗了一次情绪澡。

---

## ✨ 预览

![oxygen-chamber · 内心气象日记 · 60s 氧气舱](oxygen-chamber_1.gif)

---

## 📂 文件说明

| 文件 | 说明 |
|------|------|
| `oxygen-chamber.html` | 自包含交互 H5——内联 CSS + p5.js CDN + Web Audio 合成 |
| `oxygen-chamber_1.gif` | 动态预览截图 |

---

## 🖱️ 交互

| 操作 | 响应 |
|------|------|
| 点击情绪按钮 | 切换晴/雨/雪/雷/雾五种天气，玻璃容器内粒子系统瞬间变换 |
| 点击玻璃容器 | 开始/重置 60 秒呼吸倒计时，环形进度条显示剩余时间 |
| 倒计时结束 | 环境光闪烁 + 音频渐弱，提示"呼吸完成" |

---

## 🛠️ 技术栈

| 技术 | 用途 |
|------|------|
| p5.js Canvas 2D | 像素粒子系统渲染、Bayer 有序抖动 |
| CSS Frutiger Aero | 玻璃容器 — backdrop-filter blur + 拟物高光罩 + env-glow |
| Web Audio API | OscillatorNode + BiquadFilterNode 环境音合成 |
| CSS custom properties | 情绪色板切换——全局暗色主题变量 |

---

## 🌱 创作背景

"情绪日记"被小红书做成了模板化的文字填空题。但情绪最难被文字捕捉的那个瞬间——胸口闷、脑子乱、说不清——恰恰是最需要被接住的时刻。

这个作品的野心很简单：不让你写一个字。选一种天气代替你此刻的心情，然后躲在玻璃小屋里待 60 秒。时间到，门开，你可以走了。什么都没发生，但你知道自己变轻了一点。
