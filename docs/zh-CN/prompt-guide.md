# MiniMax M3.1 Flash 提示词写法：如何为视频提示 M3.1 Flash

[English](../prompt-guide.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

MiniMax M3.1 Flash 不直接输出视频。它写代码——用 Three.js、WebGPU、Canvas 或 SVG 的 HTML 页面——作者再把页面播放过程录下来。也有不少作者在 MiniMax Code 里完成，它还会一并生成页面用的图片和音乐。下面的写法来自作者随视频公开的提示词，以及 SandBase Lab 用来测试模型的固定提示词。每条都链接到它产出的视频。

有一点会影响所有提示词：这个模型的思考始终开启，推理强度可从 `low` 调到 `max`（[`sandbase inspect`](https://www.sandbase.ai/model/minimax/minimax-m3.1-flash?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash)）。它先花 token 思考再动笔，这些 token 也算在你的 `max_tokens` 里。

## 1. 说清楚要什么文件

点名格式和运行环境。这里效果最好的作品几乎都在第一句就写清楚了——有的只是作者转述，而不是原样贴出的提示词：

- "generate a 3d model flower pot, using Three.js, in a 3d model viewer style page"（用 Three.js 生成一个 3D 花盆，做成 3D 模型查看器那样的页面）（[@ItsmeAjayKV][flower-pot]）——一次生成，没有 harness，没有追加轮次。
- "make the most realistic water scene it could, in WebGPU, with a floating camera"（用 WebGPU 做一个它能做到的最写实的水面场景，加一个悬浮相机）（[@ivanfioravanti][water]，原文引用）。
- 开放式要求也行，但要写清交付物："尽你最大的能力，做一个介绍你自己（M3.1-Flash）和Minimax Code的视频"，跑出 41 分钟的成果（[@klarkxy][intro]）。

## 2. 指明渲染方式，别只说"3D"

同一个场景在 Three.js、WebGPU 和 SVG 里差别很大，而模型会照你点的那一种做。点名渲染方式也决定了哪里会出问题：

- Three.js 用 CDN import map 以 ES module 引入，是这里 3D 场景的默认选择（[@ItsmeAjayKV][pagoda]）。
- 想让水面和光照显得"贵"，就用 WebGPU（[@ivanfioravanti][water]）；它只在较新的 Chrome 里能跑。
- 要文件小、录制干净，就用 SVG 配 CSS 或 SMIL——Pelican Test 的动画提示词正是为此禁用 JavaScript（[@SahilPanhotra][peacock]、[Lab Pelican Test][pelican]）。
- 游戏和任何需要循环的地方用 Canvas（[@leo114119][fps]）。

## 3. 把整段离谱的需求写成一句话

M3.1 Flash 能从一个短需求补出很多东西，发布当天的作者正是这么用的。当天被引用最多的提示词，把三样不可能的东西叠在一起，交给模型自己消化：

- "A PS5 controller waddling down a beach, a pelican standing on it, and the Mona Lisa riding a bicycle on the pelican's back"（一个 PS5 手柄在海滩上摇摆行走，上面站着一只鹈鹕，蒙娜丽莎骑着自行车在鹈鹕背上）（[@jan_volad][beach]）——四款模型，各一次生成，不做修正。
- "a living koi pond in Three.js with a waterfall, swimming koi and a 'feed the koi' button"（用 Three.js 做一个活的锦鲤池，有瀑布、游动的锦鲤和一个"喂鱼"按钮）（[@aGim_asf][koi]）——3.3 分钟，$0。
- 带我回到 1986 年的迈阿密，霓虹、棕榈树、Ocean Drive 上一辆白色跑车（[@davit__yan][miami]）——与 Claude Opus 5.5 同一需求。

短提示词得到的是模型的选择，不是你的。在意的地方就把数字写下来（见 §5）。

## 4. 说清录制时要捕捉的状态

如果目标是一段视频，就说明镜头在跑的时候什么东西应该在动：

- 自动播放的镜头运动，或长度确定的循环，这样整个画面不依赖鼠标——和[教程](tutorial.md#4-把页面录成视频)里的建议一样。
- 状态要有可见变化：锦鲤被喂食、机甲组装完成、比赛开始。能被检查的状态，也是脚本能等待的状态。
- 缩到 400 px 还看得清的画面。这里的预览图宽 400 px（[`make_previews.py`](../../scripts/make_previews.py)），Lab 页面的卡片也一样，细线条会消失。

## 5. 把硬约束写在前面

长页面会以可预期的方式失败，而这个模型很愿意花一分钟往错的方向走。先把这些排除：

- 全部内联：不要外部字体、图片、模型文件。CDN 拉不到是最常见的白屏原因。Three.js 走 import map 是通常的例外，因为它就是渲染器本身。
- 场景必须遵守的数字：房间数、生命数、波次、齿轮比、相机高度、每轮秒数。
- "只返回完整的 HTML"，省得事后清理。
- 给它一条终点线。[@atomtanstudio][nba] 看着它在 NBA Jam 重制版上"直接认输，说自己填不平这个差距"；[@notjazii][pixel] 发现它在 `xhigh` 或 `max` 下"大量幻觉，开始做我没要求的事"——这也是它虽然有 100+ tok/s 却仍然显得慢的原因。

## 6. 让工具链承担打磨

这里效果好的作品，大多不是裸调 API：

- MiniMax Code 一次跑完页面、图片和音乐（[@klarkxy][intro]）。
- 编码 harness 承担了循环：[@PrajwalTomar_][skygarden] 在 OpenCode 里"只用一个提示词、几分钟"做出了完整体育游戏；[@ItsmeAjayKV][flower-pot] 则直接调 API，开最大思考。
- @ItsmeAjayKV 的对比最有参考价值：不用 harness、一次生成，他们仍然认为那座宝塔胜过 DeepSeek 的结果（[pagoda][pagoda]）。

要可复现的结果，用 API 再录制（§7）；要最好看的结果、不在乎等待，就让 harness 多迭代几轮。

## 7. 规划录制和预算

- 录制：[`scripts/record.mjs`](../../scripts/record.mjs) 按你给的尺寸打开页面，录 N 秒并转成 H.264（见[教程](tutorial.md#4-把页面录成视频)）。
- token：一个一次生成的页面在最大思考下用了 5 万 token（[@ItsmeAjayKV][pagoda]）；下一个用了 7.6 万，其中 5.2 万是思考（[@ItsmeAjayKV][flower-pot]）。按这个留预算——README 里的 curl 示例给的是 128000。
- 时间：发布当天的一次生成页面从 3 分钟到一小时以上都有（[@aGim_asf][koi]、[@marcthecreatorr][marc]），那条 41 分钟的介绍视频是 harness 跑出来的（[@klarkxy][intro]）。
- 花费：标价每百万输入 token $0.15、每百万输出 token $0.60，推理 token 按输出计费。作者实际花了多少见[模型对比](model-comparison.md)。

## 可以直接用的提示词

```text
把 [主题] 做成一个从磁盘直接打开就能跑的独立 HTML 文件。

画面：[风格，例如 low-poly / 电影感 PBR / 霓虹]，[氛围、光照、配色]。
运动：[什么在动、怎么动]。加载后自动播放 [10] 秒的镜头巡游，然后循环。
交互：[拖拽 = …，滚轮 = …，点击 = …，按键 = …]。
规则：[必须遵守的数字：房间数、生命、波次、齿轮比、碰撞]。

技术：
- 用 CDN import map 以 ES module 引入 Three.js，不要其他库。
- 不要外部图片、字体、音频：贴图用代码生成，声音用 Web Audio。
- 铺满视口、不出现滚动条、笔记本上 60 fps。
- 完成前自检：页面加载零 console 错误，每个操作都可用。
- 只返回完整的 HTML，从 <!DOCTYPE html> 到 </html>，不要省略。
```

可以到 [Lab 文本竞技场][arena] 里，把这段同时跑在 M3.1 Flash 和其他模型上对比；用 API 的方式见[教程](tutorial.md)。

## 参数设置

- **输出预算。** 思考始终开启，隐藏的推理 token 计入 `max_tokens` 并按输出计费。两个有记录的一次生成页面分别用了 5 万和 7.6 万补全 token；`max_tokens` 给到 10 万以上。SandBase 最多接受 512000。
- **推理强度。** 可选 `low`、`medium`、`high`、`xhigh`、`max`。明确写了设置的作者分成两派：一派为了效果开最大（[@SPAC89][spac]、[@ItsmeAjayKV][pagoda]），另一派提醒 `xhigh`/`max` 会跑偏（[@notjazii][pixel]）。折中的设置加上一条终点线，是更稳的默认值。
- **一次生成 vs. 迭代。** 发布当天的成果大多是一次生成。需要迭代时，循环发生在 harness 里，成本也随之上升：那条介绍视频用了 41 分钟，还调用了 MiniMax Code 自带的生图和音乐能力（[@klarkxy][intro]）。

---

引文均为短摘录并注明作者，完整提示词和视频请点链接。中文、日文原文的翻译为我们所做。

[flower-pot]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112111033359933516?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[pagoda]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112121327285084300?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[water]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112212819395432700?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[intro]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112198804128895153?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[beach]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112245037224382556?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[koi]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112227205300564211?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[miami]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112207066819375397?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[peacock]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112241373961416717?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[fps]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112223208338592187?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[pixel]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112200201507311699?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[nba]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112238012117680396?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[skygarden]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112220100300513770?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[marc]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112214607607562377?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[spac]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112125242415956183?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[pelican]: https://www.sandbase.ai/lab/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=minimax%2Fminimax-m3.1-flash&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
