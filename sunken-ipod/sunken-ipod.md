# Sunken iPod · 沉水 MP3

> **Tech Keywords:** p5.js, Canvas 2D, Frutiger Aero, Web Audio API, Aquatic UI, Emotional Release

<!-- WORK_META
  slug: sunken-ipod
  render_engine: Canvas 2D (p5.js)
  particle_count: 50+ (bubbles + ripples + bgParticles)
  particle_type: BufferGeometry point sprites
  shader_type: N/A
  interaction: touch interaction
  audio: pentatonic chime synthesis
  effects: blend-mode compositing
  use_cases: web audio healing soundscape, digital healing visualization, p5.js creative coding demo, frutiger aero aesthetic H5
  standalone: yes
  dependencies: 1 CDN (p5.js CDN)
  file_size: N/A
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![沉水 iPod 预览 - Frutiger Aero underwater crystal iPod with click wheel and bubbles](sunken-ipod_1.gif)

> 深海之底，一首七里香。触碰水面，音符如气泡升起。

一件以 Frutiger Aero 美学为核心的 2.5D 像素互动作品：一台晶莹剔透的 iPod 沉入深海，屏幕亮着周杰伦的《七里香》，Click Wheel 转盘在幽蓝水光中微微浮动。点击屏幕任意位置，水面泛起涟漪，气泡升腾，同时触发五声音阶的清脆铃音——像在海底按下了播放键。

作品的核心张力来自「科技造物 vs 自然深海」的视觉对比：纯白亚克力外壳与镀铬金属包边勾勒出 iPod 的工业精致感，而环绕其间的焦散光束、上升气泡和柔顺水波则将观者拉回深海的无重状态。Y 型分线器结构耳机线顺水流漂荡，两台耳塞悬浮在 iPod 两侧，仿佛在邀请你戴上倾听。

---

## ✨ 预览

直接用浏览器打开 `sunken-ipod.html` 即可运行——基于 p5.js 渲染引擎，无需构建工具或服务器。推荐在移动端竖屏体验，点击水面与 iPod 互动。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `sunken-ipod.html` | 完整可运行的 H5 互动作品，约 20KB |
| `sunken-ipod_1.gif` | 预览动图：水下 iPod 全景交互演示 |
| `sunken-ipod.md` | 本说明文件 |

## 🖱️ 交互

- **点击水面**：在点击位置生成涟漪扩散动画，同时释放 10 个上升气泡
- **音频反馈**：每次点击触发五声音阶随机铃音（C5-E5-G5-A5-C6），模拟水中风铃
- **iPod 物理**：点击时 iPod 轻微上浮 + 旋转，随之缓慢归位
- **屏幕动态**：均衡器频谱实时跳动，进度条持续前进，绿色脉冲光晕从转盘中心扩散
- **环境动画**：日光束缓慢摇曳、背景微光粒子上升、分线器耳机线随水流漂荡

## 🛠️ 技术栈

- **p5.js** — 渲染主循环 + 画布管理
- **Canvas 2D API** — 渐变填色、贝塞尔曲线耳线、径向焦散光斑
- **BlendMode Screen / Overlay** — 高光条、水波纹叠加层的光学混合
- **Web Audio API** — 五声音阶铃音合成（OscillatorNode + GainNode 包络）
- **Frutiger Aero 着色法则** — 高饱和水下渐变 + 多层高光叠加 + 玻璃质感反光

## 🌱 创作背景

「沉水 MP3」来自一个关于记忆与音乐的白日梦——那些存在 iPod 里的歌，会不会在某个深海中继续播放？作品用像素级的 Crystal Skeuomorphism 渲染一台沉入海底的 iPod，把「旧科技」与「深海静谧」绑定在一起：转盘上的文字是小写全对齐的，气泡是 Bayer 有序抖动的，耳机线是三次贝塞尔曲线的。触碰它，就像触碰一段沉在水下的旧时光。
