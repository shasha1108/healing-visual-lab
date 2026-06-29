# Pixel Aquarium · 像素水族箱


![Pixel Aquarium — 像素小鱼在 Frutiger Aero 毛玻璃水族箱中游动，点击投食，双击敲玻璃](pixel-aquarium_1.gif)

> 像素小鱼在晶莹剔透的 Frutiger Aero 水族箱里游动。单击投食，双击敲玻璃——每一次触碰都是一次治愈。

一件融合像素画颗粒感与 Frutiger Aero 玻璃美学的互动水族箱。p5.js 驱动 6 条多彩像素小鱼在毛玻璃水箱内自由游动，25 棵程序化生成的珊瑚、海葵和海绵构成斑斓海底花园。CSS 三明治层叠架构（底板毛玻璃 → Canvas 像素层 → 透明高光玻璃壳）确保像素锐利不被模糊，同时保留 Aero 美学的水润光泽。

---

## ✨ 预览

直接用浏览器打开 `pixel-aquarium.html` 即可运行——基于 p5.js 1.9.0 + CSS Glassmorphism + 赛博生命体状态机。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `pixel-aquarium.html` | 完整可运行的 H5 互动水族箱，约 16KB |
| `pixel-aquarium_1.gif` | 预览动图：交互演示 |
| `pixel-aquarium.md` | 本说明文件 |

## 🖱️ 交互

- **单击**：投喂鱼食，鱼群会追踪并吃掉食物，触发爱心反馈动画
- **双击**：敲击水族箱玻璃，触发 CSS 涟漪动画，鱼群受惊散开后缓慢恢复
- **自动生态**：气泡上升、水草/珊瑚随正弦波摇摆、鱼群 AI 自主漫游

## 🛠️ 技术栈

- p5.js 1.9.0（CDN 加载，1 个外部依赖）
- CSS 三明治层级架构（毛玻璃底板 z-index:2 → Canvas z-index:3 → 玻璃高光壳 z-index:4）
- 赛博生命体 AI 状态机（Wander / Chase / Flee）
- 程序化植物生成（堆叠摇摆 / 网格剔除 / 圆域筛选 / 扇形展开 四种模型）
- CSS Knock Ripple 涟漪动画
- 自定义 pointerdown 交互层（防单击/双击冲突）

## 📱 兼容性

| 平台 | 状态 | 备注 |
|------|------|------|
| Chrome / Edge | ✅ | 桌面 + Android 均支持 |
| Safari / iOS | ✅ | Z-index 防御性编程兼容 |
| Firefox | ✅ | |
| 移动端适配 | ✅ | `user-scalable=no`，触摸优化 |
| 需要 WebGL | 否 | Canvas 2D 渲染 |

## 🌱 创作背景

像素画唤起 GameBoy 时代的颗粒记忆，Frutiger Aero 唤起 2000 年代的科技乐观。当像素小鱼在毛玻璃水箱里游动，两种怀旧在一帧内重叠——像小时候趴在玻璃鱼缸前发呆的那个下午。

投食是给予，敲玻璃是打扰，鱼的受惊散开——这些交互刻意保留了对真实养鱼体验的微缩模拟。
