# overwork · 下班回家了，脑子却还在加班

> **Tech Keywords:** p5.js Canvas 2D, text dissolve animation, particle settlement physics, bezier glass container, pointer interaction, healing visualization, work-stress relief, frutiger aero glassmorphism

<!-- WORK_META
  slug: overwork
  render_engine: Canvas 2D p5.js
  particle_count: 24 motes + 12 fireflies
  particle_type: pixel motes (rect-based) with CSS text fragments (DOM span overlay)
  shader_type: N/A
  interaction: pointer-triggered surge wave within bezier collision polygon
  audio: no
  effects: screen blending, radial gradient halos, CSS text-shadow glow, blur dissolve, lighter composite fireflies
  use_cases: p5.js text dissolve animation, canvas bezier glass container, pointer surge wave interaction, work-stress healing visualization, particle settlement simulation, frutiger aero echo box H5
  standalone: yes
  dependencies: 1 CDN (p5.js 1.9.0)
  file_size: ~44 KB, 1226 lines
  compatibility: Chrome/Edge/Firefox, Safari iOS 15+
  WORK_META_END
-->

![overwork - thought fragments dissolving into pixel motes inside a bezier glass echo box](overwork_1.gif)

> 把下班后仍在脑内重播的短语交出去，让语言松解成微光并自然沉底。

这是一件以"下班后大脑仍在加班"为主题的 H5 互动疗愈作品。屏幕上漂浮着 6 句职场人下班后脑中挥之不去的短语——「刚才那句话是不是说重了」「有条消息还没回」「是不是我做得还不够好」——它们在一条贝塞尔曲线围成的玻璃回响盒内随机碰撞游走。

轻触玻璃盒任意位置，一波珊瑚色冲击波从触点向外扩散，24 颗像素微光粒子被推向盒壁，6 句短语在冲击中失去字形、化为模糊光斑，随后在重力作用下缓缓沉降到盒底。沉降完成后，12 只萤火虫从底部亮起，盒内进入静谧模式——顶层文字切换为「该好好休息了」。

作品用 Canvas 2D 原生 API 绘制玻璃容器（clip + bezierCurveTo + screen 混合模式），短语用 DOM span 叠加在 Canvas 上方，通过 CSS text-shadow 和 filter blur 实现字形溶解特效。

---

## ✨ 预览

直接用浏览器打开 `overwork.html` 即可运行——p5.js 1.9.0 CDN 加载，无需构建工具。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `overwork.html` | 完整可运行的 H5 互动作品，约 44KB |
| `overwork_1.gif` | 预览图：短语碎片在玻璃回响盒内沉降为微光粒子 |
| `overwork.md` | 本说明文件 |

## 🖱️ 交互

- **轻触玻璃盒**：触发冲击波，24 颗微光粒子被推向盒壁，6 句短语开始溶解
- **等待沉降**：粒子在重力作用下自然沉底，短语逐渐模糊消失
- **静谧模式**：全部粒子沉底后，12 只萤火虫亮起，文字切换为安眠提示

## 🛠️ 技术栈

- **p5.js 1.9.0** — Canvas 2D 渲染引擎，pixelDensity 自适应 HiDPI
- **Canvas Glass Pipeline** — clip + bezierCurveTo + screen 混合模式绘制玻璃容器
- **Bezier Collision Detection** — 贝塞尔曲线采样多边形，射线法做粒子/文字碰撞检测
- **CSS Text Dissolve** — DOM span 叠加，text-shadow glow + filter blur + letter-spacing 实现字形溶解
- **Particle Settlement Physics** — 冲击波后重力沉降 + 弹性碰撞 + restTime 静默判定

## 🌱 创作背景

下班回家，身体离开了工位，脑子却还在回放今天说过的话、没回的消息、明天的 deadline。这种「脑内加班」是现代职场人最普遍却最少被谈论的情绪状态。

这件作品试图为这种状态提供一个仪式性的出口：把那些在脑中打转的短语交出去，看着它们在冲击波中失去意义、化为微光、沉入盒底——然后告诉自己：**今晚不用再回答。**
