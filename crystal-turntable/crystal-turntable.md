# Crystal Turntable · 雪夜晶莹唱片机 — Frutiger Aero Vector Edition

> **Tech Keywords:** p5.js, Canvas 2D, Web Audio API, Lo-fi Jazz, Frutiger Aero, CSS3 Glassmorphism

<!-- WORK_META
  slug: crystal-turntable
  render_engine: Canvas 2D (p5.js)
  particle_count: 120 (snow flakes x3 layers)
  particle_type: BufferGeometry point sprites
  shader_type: N/A
  interaction: touch interaction
  audio: BiquadFilterNode LPF sweep, ConvolverNode reverb
  effects: N/A
  use_cases: web audio healing soundscape, digital healing visualization, p5.js creative coding demo, frutiger aero aesthetic H5
  standalone: yes
  dependencies: 1 CDN (p5.js CDN)
  file_size: N/A
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![Snowy night vinyl turntable with crystal glow and falling snow](crystal-turntable_1.gif)

> 屋外雪花纷飞，这里的旋律永远为你温暖。

一件 Frutiger Aero 风格的 H5 像素互动作品。画面以雪夜中的唱片机为核心——黑胶唱片缓缓旋转，真空管发出暖色辉光，三层景深雪花从窗外飘落。CSS 玻璃拟态盒包裹着整个场景，镀铬唱臂和旋转扇形高光共同构成通透、湿润、晶莹的视觉质感。

音乐上，作品内置了 Lo-fi 爵士和弦循环（Cmaj7 → Am7 → Dm7 → G7），通过 Web Audio API 实时合成，不含任何外部音频文件。Lo-fi 处理总线包含低通滤波、磁带颤音（Tape Wow）和反馈延迟混响，叠加雪风声和黑胶噼啪音效，营造深夜独处的温暖氛围。

---

## ✨ 预览

直接用浏览器打开 `crystal-turntable.html` 即可运行——p5.js 从 CDN 加载，无需构建工具。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `crystal-turntable.html` | 完整可运行的 H5 互动作品，约 23KB |
| `crystal-turntable_1.gif` | 预览动图：雪夜唱片机完整交互演示 |
| `crystal-turntable.md` | 本说明文件 |

## 🖱️ 交互

- **点击唱片机任意位置** — 触发玻璃轻敲音效，同时启动音频引擎
- **冰雪光彩旋钮** — 在 6 套 Frutiger Aero 通透色板间切换（冰晶水蓝 / 极光冰薄荷 / 晨露珊瑚 / 月光紫罗兰 / 晴空蔚蓝 / 初雪银白）
- **解忧签按钮** — 随机抽取一句雪夜暖心语录卡片
- **黑胶旋转** — 唱片持续旋转，扇形高光跟随节奏律动
- **三层雪花** — 远景朦胧、中景不规则椭圆、近景带景深虚化，部分雪花在盒顶堆积

## 🛠️ 技术栈

- **p5.js** — Canvas 2D 渲染，矢量化绘制（无位图素材）
- **Web Audio API** — 实时合成 Lo-fi 爵士和弦 + 雪风白噪 + 黑胶噼啪
- **Lo-fi 处理总线** — 低通滤波 + Tape Wow 磁带颤音 + 反馈延迟混响
- **CSS3** — Frutiger Aero 玻璃拟态（acrylic box + 多层渐变 + 内阴影高光）
- **纯矢量** — 所有视觉元素（黑胶、真空管、唱臂、雪花、音符）均由代码绘制

## 🌱 创作背景

深夜独处时，总想拥有一台属于自己的唱片机——它不用播放任何现成的歌曲，只需在雪夜中缓缓转动，用简单的爵士和弦填满房间的寂静。这件作品是对那种「被音乐包裹的孤独感」的像素致敬：没有复杂交互，没有任务目标，只有雪花、旋律、和一颗慢慢转动的心。
