# Sunken Treasure · Console Spawned Ecosystem

> **Tech Keywords:** p5.js, Canvas 2D, Frutiger Aero, Procedural Ecosystem, Pixel-to-Vector Metamorphosis, Mouse POV Parallax

![Crystal aqua world with 3D game console spawning vector fish](sunken-treasure_1.gif)

> 像素鱼游进掌机传送门，逃逸到 3D 水晶水体中，蜕变为优雅的矢量鱼——鱼群随时间越来越多。

一件 Frutiger Aero 风格的 H5 互动水族箱作品。场景中心是一台透明的 3D 水晶掌机，屏幕里运行着 NES 风格的像素鱼小游戏。掌机右侧的传送门不断有像素鱼逃逸出来，蜕变为三种矢量鱼（天使鱼、金鱼、圆盘鱼）游入水体。随着时间推移，水中的矢量鱼群会越来越多——这是一个会自我生长的生态系统。

画面包含七层渲染管线：水晶水体渐变、柔和日光束、液体焦散光池、底沙与珊瑚、3D 立体掌机、游动鱼群、以及水面 Snell 窗口漫反射。鼠标移动产生平滑的 POV 视差效果，点击水面会惊散鱼群。

---

## ✨ 预览

直接用浏览器打开 `sunken-treasure.html` 即可运行——p5.js 从 CDN 加载，无需构建工具。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `sunken-treasure.html` | 完整可运行的 H5 互动作品，约 36KB |
| `sunken-treasure_1.gif` | 预览动图：掌机生态系统完整演示 |
| `sunken-treasure.md` | 本说明文件 |

## 🖱️ 交互

- **鼠标/触摸移动** — POV 视差效果，不同渲染层以不同速率偏移，营造 3D 水体的深度感
- **点击水面** — 产生扩散涟漪，惊吓附近鱼群（鱼会快速逃离后慢慢返回）
- **自动生态增长** — 每 3.2 秒从掌机传送门诞生一条新矢量鱼，鱼群最多 24 条
- **漂浮卡带** — 6 张不同颜色的透明游戏卡带在水中缓缓漂浮
- **气泡与光尘** — 50+ 水晶气泡上升 + 60+ 散斑光尘浮动

## 🛠️ 技术栈

- **p5.js** — Canvas 2D 全视口渲染，`pixelDensity` 适配 Retina 屏
- **7 层渲染管线** — 水体渐变 → 日光束 → 焦散光池 → 底沙/珊瑚 → 3D 掌机 → 鱼群 → Snell 水面
- **3D 掌机建模** — 纯矢量绘制，含侧壁厚度、PCB 电路板、ABXY 四色钻石按键、D-Pad、SELECT/START、扬声器栅格
- **像素→矢量蜕变** — 从屏幕传送门逃逸的鱼获得向外初速度，带发光涟漪和光尘粒子特效
- **Mouse POV Parallax** — 鼠标偏移映射到各渲染层的不同位移系数，模拟水下视差
- **Frutiger Aero 色板** — 冰晶光 → 电光青 → 蓝宝石 → 深海靛蓝 → 四周暗角

## 🌱 创作背景

灵感来自一个念头：如果 Game Boy 沉入海底，里面的像素鱼会不会逃出来，变成真正的鱼？这件作品把「掌机屏幕」和「水族箱」打通，用传送门连接两个世界——像素世界里的鱼穿过屏幕，在 3D 水晶水体中获得新的形态和自由。
