# Sky Through Glass · 玻璃天空

> **Tech Keywords:** p5.js, FBO masking, Web Audio API, Frutiger Aero, VHS aesthetic, glass-wipe interaction

![Sky Through Glass - Frutiger Aero glass-wipe interaction with VHS noise and blue sky](sky-through-glass_1.gif)

> 蒙尘的玻璃下，是小时候的温柔天空。指腹划过，VHS 噪点被轻轻擦开。

一件以 Frutiger Aero 美学为灵感的 H5 互动疗愈作品。屏幕上覆盖着一层蒙尘的玻璃——杂乱的 VHS 噪点和 CRT 扫描线让天空变得模糊不清。用户用手指划过屏幕，噪点被逐片擦去，露出藏在玻璃背后的温柔蓝天。这是一次数字化的"擦拭仪式"——每一道划痕都在说：干净的过去还在那里，你只是需要亲手把灰尘擦掉。

---

## ✨ 预览

直接用浏览器打开 `sky-through-glass.html` 即可运行——基于 p5.js 1.9.0 + FBO 遮罩合成 + Web Audio 纯代码合成音频。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `sky-through-glass.html` | 完整可运行的 H5 互动作品，约 14KB（含 p5.js CDN 引用） |
| `sky-through-glass_1.gif` | 预览动图：擦拭交互过程 |
| `sky-through-glass.md` | 本说明文件 |

## 🖱️ 交互

- **拖拽擦拭**：手指/鼠标划过屏幕，蒙尘玻璃被逐片擦净，露出背后的蓝天光晕
- **自定义光标**：发光光点跟随手指，按压时光点变暖金色——暗示"你的触碰在温暖这片天空"
- **三阶段情绪弧线**：浑浊噪点 → 持续擦拭 → 清澈天空。擦得越干净，风铃声越清晰
- **移动端适配**：响应式画布，移动端使用系统光标

## 🛠️ 技术栈

- p5.js 1.9.0（CDN 加载，1 个外部依赖）
- FBO Masking（离屏 Graphics 层收集笔触 → 作为 alpha 遮罩合成）
- Web Audio API（棕噪 drone 底噪 → 五声音阶正弦波风铃，无音频文件）
- CSS CRT/VHS 装饰层（repeating-linear-gradient 扫描线 + radial-gradient 暗角 + RGB split 色散）
- CSS 自定义光标（radial-gradient 发光光点 + lerp 悬浮跟随 + :active 温暖变色）
- meta viewport 移动端适配

## 🌱 创作背景

Frutiger Aero 是 2004-2013 年间流行的一种设计美学——半透明玻璃、水面、极光、蓝天白云、自然光感。它代表的不是某个操作系统，而是一种对"科技让生活更美好"的天真信仰。当用户擦开 VHS 噪点，看到的不仅是蓝天——也是那个相信未来会更好的自己。

擦拭 = 净化。噪点 = 日常压力的视觉隐喻。蓝天 = 被遗忘的宁静。这是一个用指尖完成的数字疗愈仪式。
