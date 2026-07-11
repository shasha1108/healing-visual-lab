# Clockwork Tidal Gauge · 发条潮汐仪

> **Tech Keywords:** p5.js Canvas 2D pixel rendering, Web Audio API OscillatorNode glass knock chime synthesis, BiquadFilter low-pass ocean noise, DelayNode echo feedback, Bayer 4x4 ordered dithering, spring-damper gear physics, sinusoidal tide simulation, Frutiger Aero glass capsule

<!-- WORK_META
  slug: clockwork-tidal-gauge
  render_engine: Canvas 2D p5.js 1.9.4
  particle_count: N/A
  particle_type: N/A (pixel sprites: buoys, bubbles, moon phase frames)
  shader_type: N/A
  interaction: pointerdown touch — knock instrument triggers gear rotation + tide phase shift + glass glow
  audio: Web Audio API OscillatorNode glass knock chime (1850/2600/3150Hz sine), triangle thud sweep (250→50Hz exponentialRampToValueAtTime), DelayNode echo feedback loop (0.45s delay), BiquadFilter low-pass ocean noise (BufferSource white noise), tick sound (800Hz triangle)
  effects: Bayer 4x4 ordered dithering on water surface, screen blend mode (internal atmosphere, tide recording, glass front), pixel grid snapping (PX=2), shadowBlur panel shadow
  use_cases: p5.js clockwork instrument, canvas tide simulation, web audio glass chime synthesis, frutiger aero capsule H5, bayer dithering water rendering, moon phase pixel animation
  standalone: yes
  dependencies: 1 CDN (p5.js 1.9.4)
  file_size: ~20 KB, 519 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Clockwork Tidal Gauge — Frutiger Aero glass capsule with moon phase gear and Bayer-dithered tide water](clockwork-tidal-gauge_1.gif)

> 触碰玻璃舱体，月相齿轮转动一格，潮汐随之涨落——一台封存在像素胶囊里的发条潮汐仪。

这是一个装在 Frutiger Aero 玻璃胶囊中的机械潮汐仪。画面中央是一枚 12 齿月相齿轮，齿轮中央嵌有 8 帧像素月相动画——从满月到新月逐帧切换。齿轮下方是 Bayer 4x4 有序抖动渲染的像素水体，水面高度由正弦潮汐周期（~12 秒）+ 月相齿轮脉冲能量共同驱动。4 个浮标随波浪上下摆动，22 个气泡从水底缓缓上升，左侧还有一条实时潮位记录曲线。

每次触碰胶囊，发条机构被"上紧"——月相齿轮旋转一格、月相前进一帧、潮汐相位偏移 1.5 小时、玻璃表面泛起青色辉光。音频层面，触碰触发三音玻璃敲击泛音列（1850Hz / 2600Hz / 3150Hz）+ 低频闷响（250→50Hz sweep）通过 DelayNode 回声反馈回路产生空间感；背景持续播放经 BiquadFilter 低通滤波的白噪声海浪声，滤波截止频率随潮汐相位动态漂移。

---

## ✨ 预览

直接用浏览器打开 `clockwork-tidal-gauge.html` 即可运行——基于 p5.js 1.9.4，单文件零构建，Canvas 2D 像素渲染 + Web Audio 合成音频。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `clockwork-tidal-gauge.html` | 完整可运行的 H5 互动作品，约 20KB |
| `clockwork-tidal-gauge_1.gif` | 预览图：触碰胶囊、齿轮旋转、潮汐涨落的动态演示 |
| `clockwork-tidal-gauge.md` | 本说明文件 |

## 🖱️ 交互

- **点击/触碰胶囊任意位置**：上紧发条——月相齿轮旋转 30°，月相前进一帧，潮汐相位偏移，玻璃辉光亮起
- **观察潮汐响应**：水面正弦波动（周期 ~12 秒），被发条脉冲叠加短暂拉升
- **观察齿轮弹簧物理**：齿轮带弹簧-阻尼回弹效果，碰后逐渐回归平衡
- **连续点击**：月相循环 8 帧（满月→残月→新月→复原），潮汐记录图实时更新

## 🛠️ 技术栈

- **渲染**：Canvas 2D (p5.js 1.9.4)，固定 720×960 画布，2px 像素网格 (`snap()` 对齐)
- **玻璃胶囊**：Canvas `arcTo` 胶囊路径 + `clip` 裁切内部内容，`screen` 混合模式高光边 + `shadowBlur` 倒角折射模拟水晶厚度
- **水体渲染**：Bayer 4x4 有序抖动矩阵 + 双正弦波叠加 + 脉冲波纹扩散，`fillRect` 逐像素块着色
- **月相齿轮**：12 齿发条齿轮 (`TWO_PI / 12` 步进) + 弹簧-阻尼物理 (`spring * 50 → angleVel → angle`) + 8 帧二进制像素月相动画 + 金色潮汐指针同步旋转
- **音频合成**：Web Audio API — BufferSource 白噪声 → BiquadFilter 低通海浪 (cutoff 随潮汐漂移)，OscillatorNode 三音玻璃敲击 + triangle 低频闷响 sweep，DelayNode 回声反馈回路，tick 声 (800Hz triangle) 随潮汐秒脉冲触发
- **潮汐模拟**：`sin(simTime * TWO_PI / 12 + tidePhaseOffset) * 45` 正弦主周期 + 呼吸微扰 + 发条脉冲拉升

## 🌱 创作背景

"发条潮汐仪" 将 18 世纪航海钟的精密机械美学装入 Frutiger Aero 玻璃胶囊——月相齿轮、潮汐刻度、浮标、记录曲线，所有元素都在致敬人类用机械理解海洋的古老浪漫。触碰即上弦，齿轮转动一格，潮汐随之涨落——这既是一台仪器，也是一个关于时间、月亮与海的诗意隐喻。
