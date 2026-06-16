# Overthinking Engine · 过载脑区 | The Overthinking Engine

> **Tech Keywords:** GSAP animation engine, CRT cyberpunk aesthetic, typewriter narrative, overthinking, visual therapy H5

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

## 🌱 创作背景

灵感来自心理学概念「过度自我监控」（Hyper-Self-Monitoring）和边沁的全景监狱（Panopticon）隐喻。当我们持续扫描自己的言行、分析他人的微表情、预演最坏结局，大脑就像被 24 小时监控的囚犯——而看守就是我们自己。这件作品用赛博朋克美学把这种内耗可视化：密集的弹窗是焦虑的具象化，10 秒后的自动清空则传递一个简单但有力的信息——你可以停下来。
