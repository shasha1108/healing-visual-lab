# dreamcore-summer-rain · 七里香 Dreamcore夏夜

> 极致冷暖光碰撞 — 深黑蓝天 vs 售货机刺眼白光 vs 铁路脉冲红灯，日本动漫夏夜最经典的情感锚点。

## ✨ 预览

![dreamcore-summer-rain - Summer night rain scene with vending machine glow and railway signal](dreamcore-summer-rain_1.gif)

## 📂 文件说明

| 文件 | 描述 |
|------|------|
| `dreamcore-summer-rain.html` | 主页面 |
| `dreamcore-summer-rain_1.gif` | 预览动图 |

## 🖱️ 交互

- 移动光标靠近蝴蝶 → 蝴蝶躲避飞走
- 首次点击激活雨声和虫鸣

## 🛠️ 技术栈

- **渲染**: p5.js Canvas2D，7层纵深透视
- **光影**: 售货机 shadowBlur=30 青白冷光 + 铁路红灯脉冲光晕
- **水面**: beginClip + bezierCurve 不规则水洼 + filter blur(6px) 倒影
- **蝴蝶**: Lissajous曲线三维盘旋 + 深度缩放 + 三色区分
- **紫阳花**: 算法交叠圆形簇 + shadowBlur发光
- **音频**: Web Audio 粉噪雨声 + 虫鸣

## 🌱 创作背景

灵感来自周杰伦《七里香》与日本动漫（新海诚）夏夜雨景。核心视觉语言是 Dreamcore — 用极度刺眼的人工光源（售货机青白光、铁路脉冲红灯）在深黑夜色中制造情感张力。冷暖对比是画面最核心的情绪载体。
