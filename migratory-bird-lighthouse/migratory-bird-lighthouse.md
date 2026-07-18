# Migratory Bird Lighthouse · 雾中候鸟灯塔

> **Tech Keywords:** Canvas 2D volumetric cylinder rendering, Web Audio API pentatonic chimes, pointer event beam aiming, screen blend mode, state machine, boid flocking, radial gradient fog, localStorage persistence

<!-- WORK_META
  slug: migratory-bird-lighthouse
  render_engine: Canvas 2D (Vanilla)
  particle_count: ~200 (35 boids, 100 stars, 40 dust motes, 11 fog banks, 9 lamp sparks, rising mists)
  particle_type: 2D point sprites (arc fills)
  shader_type: N/A
  interaction: pointer-drag beam aiming, press-and-hold ignite
  audio: Web Audio API oscillator synthesis / pentatonic chimes (C5-C6) / noise drone with lowpass filter / feedback delay reverb
  effects: screen blending / radial gradient glow / cylindrical volumetric beam with clip-path / boid flocking with alignment / sine wave sea / pointer capture drag
  use_cases: canvas 2d lighthouse beam, web audio healing visualization, migratory bird interactive H5, volumetric light canvas, boid flocking demo, cylindrical beam rendering
  standalone: yes
  dependencies: 0 CDN (vanilla JavaScript)
  file_size: ~28 KB, 935 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![雾中候鸟灯塔 - volumetric cylindrical beam over dark sea with migratory birds](migratory_bird_lighthouse.gif)

> 光落处，漂泊暂歇。

点击唤醒一道平行于海面的圆柱光束，照耀 3 秒后自然消散。迷途的候鸟穿过光束时被"救赎"——它们从迷失的徘徊中升腾，化作光点隐入夜空。每一次救赎都会被记住，累计计数保存在本地。

作品以 Vanilla Canvas 2D 实现完整的体积光渲染管线：光束由三层 clip-path 遮罩叠加构成（外层宽淡、内层细亮），每层独立径向高斯衰减 + 纵向锥台扩散 + 大气抖动；海面反射以多频正弦波叠加模拟水面起伏；雾团经过光束时被实时照亮，表现体积散射。

---

## ✨ 预览

直接用浏览器打开 `migratory-bird-lighthouse.html` 即可运行——纯原生 Canvas 2D + Web Audio API，零依赖，单文件完整 H5 互动作品。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `migratory-bird-lighthouse.html` | 完整可运行的 H5 互动作品，约 28KB |
| `migratory_bird_lighthouse.gif` | 预览动图：光束照耀海面、候鸟穿行升华 |
| `migratory-bird-lighthouse.md` | 本说明文件 |

## 🖱️ 交互

- **点击 / 按住**：在灯塔位置唤醒一束平行于海面的圆柱光束，持续 3 秒后自然消散
- **拖动**：按住后上下拖拽可调整光束角度（-20° ~ +10°），瞄准不同高度的候鸟群
- **被动观察**：3 秒无操作后提示文字"长明如晤"重新浮现，候鸟持续从右侧飞入

## 🛠️ 技术栈

- **Canvas 2D**：体积圆柱光束渲染（clip-path + 径向渐变 + screen 混合）、Boid 集群算法（对齐力）、多层正弦波海面
- **Web Audio API**：五声音阶钟声合成（C5–C6）、噪声底噪 + lowpass 动态滤波、反馈延迟混响网络、音频 ducking
- **Pointer Events**：setPointerCapture 拖动瞄准、状态机驱动光束生命周期（idle → on → fading）
- **localStorage**：累计救赎计数持久化
- **Canvas toDataURL**：一键生成分享卡片 PNG

## 🌱 创作背景

"雾中候鸟灯塔"是关于漂泊与归属的隐喻。每一只从右侧飞入的候鸟都在迷雾中漫无目的地徘徊——直到一束光出现。光束由你亲手点亮、亲手瞄准，每一次照亮都意味着一次"被接住"。作品底部计数器记录着"被光接住的漂泊的羽"，那是所有曾迷失、最终找到方向的灵魂。
