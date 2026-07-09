# Pocket Forest Radio · 露光口袋森林电台

> **Tech Keywords:** p5.js Canvas 2D, Web Audio oscillator synthesis, AnalyserNode FFT 256-bin, Bayer 4x4 ordered dithering, screen composite blend mode, spring physics tuning ring, getUserMedia mic reactive, Frutiger Aero glass shell

<!-- WORK_META
  slug: pocket-forest-radio
  render_engine: Canvas 2D (p5.js 1.9.0) — mixed smooth Frutiger Aero glass shell + 180×126 pixel sub-canvas
  particle_count: 56 animated sprites (34 pixel trees + 22 fireflies)
  particle_type: pixel rect sprites (fillRect 2×2) with per-entity energy/bend state
  shader_type: Bayer 4x4 ordered dithering (sky gradient), radial gradient screen composite (ambient glow layers)
  interaction: pointer-down-move-up on tuning ring + screen; spring physics drives tuneAngle; audio file drag-drop
  audio: Web Audio oscillator synthesis (86Hz sine drone + deterministic noise buffer + triangle-wave glass ping with exponentialRampToValueAtTime); AnalyserNode FFT 256-bin (bass 0-10 / mid 11-50 / high 51-127); beat detection
  effects: screen composite blend mode (ambient glow, device sheen, tuning ring halo); radial gradient glow linked to AudioReactive RMS
  use_cases: p5.js interactive radio device, canvas 2d pixel forest, web audio oscillator healing, frutiger aero glass ui, microphone reactive visualization, audio file drag-drop H5
  standalone: yes
  dependencies: 1 CDN (p5.js 1.9.0)
  file_size: ~24 KB, 766 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Pocket Forest Radio - Frutiger Aero glass radio device with pixel forest screen and tuning ring](pocket-forest-radio_1.gif)

> 轻拨调谐环，把一片像素森林调到你的频率上。

一台透明 Frutiger Aero 玻璃小电台，屏幕里装着会呼吸的像素森林。转动调谐环，34 棵像素树随风摆动，22 只萤火虫随频率闪烁——森林风场、萤光和低频电台声会回应每一次触碰和麦克风里的声音，然后慢慢回到安静。

核心技术亮点：Canvas 2D 双画布架构（180×126 像素子画布 Bayer 抖动渲染天空 + 主画布 smooth 模式绘制 Aero 玻璃外壳），Web Audio oscillator 合成完整音景（86Hz 正弦波 drone + 确定性噪声缓冲 + 三角波玻璃 ping），AnalyserNode FFT 256-bin 三频段（bass/mid/high）实时驱动树木弯曲度和萤火虫亮度，spring physics 模拟调谐环惯性回弹。支持麦克风实时音频反应和拖放音频文件两种输入模式。

---

## ✨ 预览

直接用浏览器打开 `pocket-forest-radio.html` 即可运行——p5.js 1.9.0 自动从 CDN 加载，无需构建工具。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `pocket-forest-radio.html` | 完整可运行的 H5 互动作品，约 24KB |
| `pocket-forest-radio_1.gif` | 预览图：调谐环交互与像素森林动画 |
| `pocket-forest-radio.md` | 本说明文件 |

## 🖱️ 交互

- **拨动调谐环**：按住右下角调谐环外围旋转，切换电台频道，树木弯曲度和萤火虫亮度随之变化
- **触碰屏幕**：点击或按住屏幕区域唤醒森林，增加整体能量水平
- **麦克风输入**：首次触摸后自动请求麦克风权限，环境声音/音乐实时驱动树木摆动和萤火虫闪烁
- **拖放音频文件**：将音频文件拖入页面，替换麦克风输入作为音频源
- **偶遇飞鸟**：像素小鸟随机飞过屏幕，屏幕唤醒程度越高出现越频繁

## 🛠️ 技术栈

- **p5.js 1.9.0** — Canvas 2D 主渲染循环（setup/draw/windowResized）
- **Web Audio API** — oscillator 合成（sine drone + noise buffer + triangle glass ping），AnalyserNode FFT 256-bin 实时频谱分析，BiquadFilter 低频提取
- **Bayer 4x4 有序抖动** — 像素天空渐变，消除色带伪影
- **Spring Physics** — 调谐环惯性回弹系统（tuneAngle → targetTune 弹簧阻尼模型）
- **Canvas 2D composite 'screen'** — Frutiger Aero 玻璃高光、环境光晕、调谐环发光层
- **getUserMedia** — 麦克风实时音频流捕获
- **FileReader + Audio element** — 拖放音频文件解码播放

## 🌱 创作背景

"露光口袋森林电台"的灵感来自老式晶体管收音机——那种需要轻轻转动旋钮才能对准频率的仪式感。在这里，频率不指向人类电台，而指向一片像素森林：风穿过针叶的沙沙声、萤火虫的微光、偶遇的飞鸟。Frutiger Aero 的透明玻璃外壳让这台小电台看起来像从 2000 年代初期的 UI 梦境中取出的一样——半透明、发光、圆润，触感温柔。
