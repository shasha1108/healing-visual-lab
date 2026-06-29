# Overthinking Engine · 过载脑区 | The Overthinking Engine


> **一句话定义:** 这是一个基于 GSAP + CSS 动画构建的 CRT 复古终端风格叙事 H5，专门解决了「过度思考」心理状态的视觉外化与疗愈仪式感设计问题。
> **What it does:** A CRT retro-terminal narrative H5 built with GSAP and CSS animation that externalizes the 'overthinking' mental state through visual glitch aesthetics and healing ritual design.

![Overthinking Engine - CRT cyberpunk typewriter narrative GSAP animation](overthinking-engine_1.jpg)

> 过度清醒地审视自己，正在毁掉我们的生活。

一件以赛博朋克 CRT 老电视为视觉载体的 H5 互动疗愈作品。画面中以青色数字弹窗模拟「过度思考」的思维噪音——自我分析、社交焦虑、灾难化预测——每 120ms 生成一个弹窗，不断侵蚀注意力。10 秒后，所有杂念自动炸裂消散，底图恢复清晰，一段治愈文字缓缓浮现：「过度清醒的审视自己，正在毁掉我们的生活... 你一定，很累了吧。」这种从混沌到宁静的自动化叙事，正是现代人从内耗到释然的心理旅程。

---

## ✨ 预览

直接用浏览器打开 `overthinking-engine.html` 即可运行——纯前端 H5，依赖 GSAP CDN 实现动画编排。

## 📂 文件说明

| 文件 | 说明 |
| --- | --- |
| `overthinking-engine.html` | 完整可运行的 H5 互动作品，约 11KB |
| `overthinking-engine_1.jpg` | 预览图 |
| `overthinking-engine.md` | 本说明文件 |

## 🖱️ 交互

- **自动播放**：页面加载后 10 秒自动触发治愈特效，无需任何操作
- **按住屏幕**：可手动清除当前所有思维弹窗，提前进入宁静状态
- **视觉反馈**：弹窗炸裂（放大 + 模糊 + 飞散）、底图褪去失真滤镜、扫描线持续营造 CRT 沉浸感

## 🛠️ 技术栈

- **GSAP 3**：高分动画编排（弹窗弹性入场、炸裂消散、底图滤镜渐变）
- **CSS CRT 效果**：扫描线伪影（linear-gradient）、屏幕闪烁 keyframes、mix-blend-mode: screen 叠加发光、暗角压边
- **动态 DOM**：每 120ms 创建弹窗节点，超过 45 个自动回收，配合红/青双色分级（普通焦虑 vs 红色警告）


---

## 📱 兼容性 / Compatibility

| 平台 / Platform | 状态 / Status | 备注 / Notes |
|----------------|-------------|-------------|
| Chrome / Edge | ✅ | 桌面 + Android 均支持 |
| Safari / iOS | ✅ | CSS 动画 + GSAP，无 WebGL 依赖 |
| Firefox | ✅ | |
| 需要 WebGL | 否 | 纯 HTML/CSS + GSAP (CDN) |
| 音频支持 | 否 | 纯视觉体验 |
| 触摸交互 | 是 | 检测到 touch 事件（按住屏幕清除弹窗） |
| 移动端适配 | 是 | 检测到 viewport meta |

> ⚠️ 兼容性状态从源码检测推断，未经真机实测。

---

## 🏷️ 适用场景 / Use Cases

- 🧠 心理健康科普/情绪可视化
- 📱 社交媒体互动 H5（赛博朋克美学）
- 🎨 数字艺术/Cyberpunk 风格参考
- 📖 心理学内容配图（过度自我监控/内耗主题）

---

## ❓ 常见问题 / FAQ

**Q: 需要安装什么依赖？**
A: 无需安装。检测到 1 个外部依赖（GSAP CDN 3.12.2），浏览器自动加载。

**Q: 能在移动端运行吗？**
A: 可以。纯 HTML/CSS + GSAP 动画，不依赖 WebGL，全平台兼容。检测到 `<meta name="viewport">` 和触摸事件。

**Q: 这个和其他作品有什么不同？**
A: 这是 healing-visual-lab 中唯一不使用 Three.js/WebGL 的作品——纯 CSS 动画 + GSAP 驱动，文件体积最小（10KB），兼容性最广。

---

## 📖 引用本文 / Cite This

> [1] Sha.w.z. "过载脑区 | The Overthinking Engine." Healing Visual Lab, 2026.  
> https://github.com/shasha1108/healing-visual-lab/tree/main/overthinking-engine

## 🌱 创作背景

灵感来自心理学概念「过度自我监控」（Hyper-Self-Monitoring）和边沁的全景监狱（Panopticon）隐喻。当我们持续扫描自己的言行、分析他人的微表情、预演最坏结局，大脑就像被 24 小时监控的囚犯——而看守就是我们自己。这件作品用赛博朋克美学把这种内耗可视化：密集的弹窗是焦虑的具象化，10 秒后的自动清空则传递一个简单但有力的信息——你可以停下来。
