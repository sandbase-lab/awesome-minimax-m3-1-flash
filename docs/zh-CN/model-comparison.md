# MiniMax M3.1 Flash 对比 DeepSeek V4.1 Flash 1017、Claude Opus 5.5 和 Gemini 4 Argon

[English](../model-comparison.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

两类证据，分开呈现：

1. **我们测到的。** Lab [Evals 榜单][evals] 展示 Artificial Analysis 的数据；Lab [Pelican Test][pelican] 用同一份固定提示词跑每个模型并给结果打分。样本不大，但所有人的条件一致。
2. **创作者报告的。** 发在 X 上的同提示词对比，附他们自己的花费和耗时。有参考价值，但我们没有验证。

M3.1 Flash 于 2026 年 10 月 19 日发布，本列表所有视频都在发布后约 11 小时内发出。这决定了怎么读这些数字：实测一侧很薄，因为模型才一天大；创作者一侧很厚，因为发布当天大家都在跑同一个测试。

## 我们测到的：Lab Evals 榜单

**五个语言模型榜单上都没有 MiniMax M3.1 Flash 这一行。** 榜单读取的是 2026-10-19 的 Artificial Analysis 快照（指数版本 v4.3，705 个模型），M3.1 Flash 还不在其中，所以本页没有任何数字能把它和前沿模型排在一起。上一代在榜上，那是目前最接近的实测参照：

| 模型（榜单上的行） | [智能指数][b-intel] | [编码][b-coding] | [智能体][b-agentic] | [输出速度][b-speed] | [单任务成本][b-cost] |
|---|---|---|---|---|---|
| **MiniMax M3.1 Flash** | **不在榜上** | — | — | — | — |
| MiniMax-M3（上一代） | 29.2（695 中第 130） | 58.6（258 中第 86） | 29.5（167 中第 64） | 122 tok/s（371 中第 136） | $0.508（190 中第 99） |
| Claude Opus 5.5 (Max) | 57.6（第 1） | 不在榜上 | 不在榜上 | 98 tok/s（第 187） | $5.98（第 188） |
| Gemini 4 Argon (High) | 52.6（第 9） | — | — | 不在榜上 | $1.99（第 158） |
| GPT-6.1 Sol (Max) | 51.8（第 13） | — | — | 60 tok/s（第 281） | $0.724（第 112） |
| DeepSeek V4.1 Flash 1017 (Max) | 45.1（第 36） | — | — | 230 tok/s（第 33） | $0.262（第 74） |
| Kimi K3 (Max) | 43.6（第 45） | 76.2（第 20） | 50.0（第 22） | 42 tok/s（第 337） | $2.00（第 159） |
| GLM-5.3 (Max) | 44.8（第 38） | 74.8（第 29） | 53.1（第 8） | 95 tok/s（第 194） | $2.01（第 160） |
| Claude Haiku 5.5 (Max) | 43.4（第 46） | — | — | 232 tok/s（第 31） | $0.213（第 67） |

这说明什么、不说明什么：

- **不能说明 M3.1 Flash 的分数。** MiniMax 上一代模型在智能指数上比 DeepSeek V4.1 Flash 1017 低 16 分，比 Opus 5.5 低 28 分；发布当天"快 3 倍、价格三分之一"的说法并不能告诉你新款落在哪里。在 Artificial Analysis 测到它之前，X 上每一条"打赢 DeepSeek"都只是某位创作者的单次运行。
- **创作者描述的价格差在榜单上也成立。** 单任务成本从 Claude Haiku 5.5 的 $0.213、DeepSeek V4.1 Flash 的 $0.262 一直到 Opus 5.5 的 $5.98——最高最低相差 20 倍以上，这足以让下文那个落地页 $0.014 对 $1.22 的结果仅凭标价就说得通，而它背后并没有对 M3.1 Flash 的实测。
- **大多数模型没有编码或智能体行。** 这里只有 Kimi K3、GLM-5.3 和 MiniMax-M3 有编码行，所以智能体类结果（下文那个四任务测试）只能是创作者自己跑的。

## 我们测到的：Lab Pelican Test

[Pelican Test][pelican] 让每个模型画一只骑自行车的鹈鹕，一次静态、一次动画（轮子转、腿蹬踏板，只用 CSS/SMIL）。页面渲染成 PNG，由一个 LLM 裁判按四个问题打 0–5 分：能认出是鹈鹕、真的在骑、自行车结构成立、好看。成本是 SandBase 上的实际计费金额。

2026-10-20 读取的[实时榜单][pelican]（22 个模型、128 条结果）：

| 排名 | 模型 | 结果数 | 得分 | 成功渲染 | 动画有效 | 平均成本 |
|---|---|---|---|---|---|---|
| 1 | openai/gpt-6.1-sol | 6 | 3.79 | 100% | 100% | $0.026 |
| 2 | google/gemini-4-argon | 4 | 3.75 | 100% | 100% | $0.150 |
| 4 | anthropic/claude-opus-5.5 | 6 | 3.46 | 100% | 100% | $0.223 |
| 5 | deepseek/deepseek-v4.1-flash | 6 | 3.44 | 100% | 100% | $0.017 |
| 6 | anthropic/claude-haiku-5.5 | — | 3.25 | 100% | 100% | — |
| 6 | **minimax/minimax-m3.1-flash** | **4** | **3.25** | **100%** | **100%** | **$0.006** |
| 6 | openai/gpt-6-luna | 2 | 3.25 | 100% | 100% | $0.006 |
| 9 | moonshotai/kimi-k3 | — | 3.21 | — | — | — |
| 19 | minimax/minimax-m3 | — | 2.50 | — | — | — |

MiniMax 这一行很新也很小：4 条计分结果、2 位测试者，全部在 10 月 19 日的二十分钟内完成（12:00–12:20 UTC）。公开结果流里列的是当天三次运行的六张计分图，下面的明细表就来自那里：

| 时间（UTC） | 类型 | 得分 | 能认出 / 在骑 / 车成立 / 好看 | 输出 token | 耗时 | 成本 | 裁判评语 |
|---|---|---|---|---|---|---|---|
| 12:00 | 静态 | 3.75 | 4 / 4 / 3 / 4 | 3,304 | 32 秒 | $0.0056 | "一只轻快蹬车的鹈鹕，虽然解剖结构有点乱。" |
| 12:03 | 静态 | 3.75 | 4 / 3 / 4 / 4 | 3,396 | 32 秒 | $0.0055 | "……脚悬在踏板外面。" |
| 12:03 | 动画 | 3.50 | 4 / 3 / 3 / 4 | 4,850 | 58 秒 | $0.0068 | "……车架几何略怪。" |
| 12:00 | 动画 | 3.00 | 4 / 3 / 2 / 3 | 4,422 | 51 秒 | $0.0068 | "……奇特的双车座结构违背机械逻辑。" |
| 12:20 | 静态 | 3.00 | 4 / 3 / 2 / 3 | 2,597 | 19 秒 | $0.0065 | "……前轮和车架断开，违反物理。" |
| 12:20 | 动画 | 2.75 | 3 / 2 / 3 / 3 | 4,931 | 63 秒 | $0.0070 | "……没有腿，实际上没法蹬车。" |

这说明什么：

- **认得出，但没真正骑上去。** 六张里有五张"能认出"拿到 4 分（第六张 3 分），但"在骑"只有一张拿到 4 分，其余是 3 分，没有腿的那张只有 2 分；最差的两张连车本身都不成立（双车座、前轮脱落）。裁判评语反复回到"腿够不到踏板"。
- **中等水平，最低实测价格。** 3.25 分与 Claude Haiku 5.5、GPT-6 Luna 并列，低于 DeepSeek V4.1 Flash 1017（3.44）和 Opus 5.5（3.46）；每张约 $0.006，约为 DeepSeek 的三分之一、Opus 的四十分之一。
- **便宜一部分是因为写得短。** 每张 2,597 到 4,931 个输出 token，而 DeepSeek 在同一测试上是 12,000 到 18,500（[DeepSeek 列表的实测][ds-pelican]）。
- **样本量。** 两张账号、一天、六张图。[自己跑一次][pelican-run] 就能加数据。

## 创作者报告的

发在 X 上的同提示词对比。数字按创作者自述：工具不同（Minimax Code、OpenCode、OpenRouter、订阅套餐），推理强度不同，有峰谷价，往往只跑一次。点进链接可以两边一起看。本合集 27 条对比里有 22 条对的是 DeepSeek V4.1 Flash 1017，所以那一列最关键。

| 创作者 | 任务 | M3.1 Flash | 对手 | 创作者结论 |
|---|---|---|---|---|
| [@thehypedotnews][hype] | 海底城市潜艇追逐，单 HTML 文件，四款 flash 模型 | 约 $0.21，29 分 24 秒 | DeepSeek $0.38，27 分 09 秒 · Gemini 3.8 Flash $1.43，40 分 50 秒 · Claude Haiku 5.5 约 $0.17，35 分 27 秒 | 比 Gemini 便宜 7 倍、比 DeepSeek 便宜 1.8 倍；问哪座城市最像海底 |
| [@rubenssoto_ai][ruben] | 相同提示词、相同任务 | 1 小时 06 分 51 秒，812 万 token，$0.22 | DeepSeek：1 小时 28 分 27 秒，8949 万 token，$0.54 | 问观众哪个更好 |
| [@marcthecreatorr][marc] | 相同提示词 | 1 小时 30 分，约 $0.50 | DeepSeek：80 分钟，$1.15 | "设计更简单，价格不到一半"；两个对 Flash 来说都太慢 |
| [@notjazii][pixel] | 像素城市，两边都开到最高推理 | 40 分钟，$0 | DeepSeek：50 分钟，$0.40 | "真的被 minimax 的表现惊到" |
| [@aGim_asf][koi] | Three.js 活的锦鲤池 | 3.3 分钟，$0 | DeepSeek：1 小时 40 分，$0.90 | "DeepSeek 的池塘更漂亮，minimax 的鱼还得改进" |
| [@atomic_chat_hq][tesla] | 特斯拉 Roadster 警车追逐 | $2.34 | DeepSeek：$3.07 | — |
| [@SPAC89][spac] | 同一测试，Max | 38 分钟，订阅下约 200 tok/s；$22 套餐里用掉 5 小时额度的 6% | DeepSeek：38 分钟 | "MiniMax 这局赢了"；更喜欢它的质量 |
| [@bbfu0382][neurobin] | 与上一行同组数据 | 同上 | 同上 | "这局 MiniMax 赢" |
| [@fawnunwrap][fawn] | FAWNBENCH | $0.029，约 3 分钟 | DeepSeek：$0.067，约 5 分钟 | "……就这。哇。" |
| [@ivanainai][bowser] | 酷霸王角色 | $0（免费），"更好的酷霸王" | DeepSeek：$0.06，"反而更差" | "一分钱一分货"（反讽） |
| [@hug0_plat][hugo] | 鹈鹕 | 免费 | DeepSeek：$0.24 | "MiniMax 在鹈鹕基准上完胜 DeepSeek" |
| [@VulKan42069][vulkan] | Pelican Dream，一次生成 | — | DeepSeek | "Deepseek 为王" |
| [@loktar00][loktar] | 不用 harness，0 shot，1 turn | 有一个 console 报错，被要求修掉 | DeepSeek | "DeepSeek Flash 是个怪物……提示词遵循度好得多" |
| [@leo114119][gummy] | 糖果小熊对比 | 57 分钟 | DeepSeek | "能干活，但效果差一截" |
| [@RafaCrackYT][rafa] | 特斯拉 Roadster 第一人称驾驶，四款模型，一次生成 | 约 $1.37，3 小时 11 分 | Opus 5.5 约 $110，5 小时 43 分 · DeepSeek $0.66，1 小时 12 分 · Gemini 4 Argon 约 $4.50，49 分 | Opus 质量第一；"MiniMax 视觉上最差" |
| [@nutlope][nutlope] | 硬件产品发布落地页 | $0.014，快 4 倍 | Claude Opus 5.5：$1.22 | "这个模型在设计上强得离谱……便宜 88 倍" |
| [@narushima_][narushima] | 飞行 Roadster，相同参考图 | $0.71 | Claude Opus 5.5：$11.27 | "Opus 写实度仍然更好，但 MiniMax 走出了大部分路" |
| [@davit__yan][miami] | 1986 年迈阿密，霓虹与白色跑车 | 更便宜 | Claude Opus 5.5 | "它撑住了"；对 Opus 期待更高 |
| [@jumperz][jumperz] | 四个智能体任务，各开四个并行 agent | 19 分 52 秒，API token 约 $0.30 | Claude Opus 5.5 High：10 分 57 秒，至少 $4.52 | 愿意多等 9 分钟换 1/15 的成本 |
| [@alohaproxy][alohaproxy] | 3D 机甲组装与发射 | 71,038 输出 token，10 分 17 秒 | Muse Wonder：12,488 token，1 分 33 秒 | "离谱地强" |
| [@domsilvestre][dom] | 三个 3D 场景，一次生成、不修正 | 三个共 $0.19 | Claude Opus 5.5：$13.83 | 埃菲尔铁塔不如 M3 那版；鱼和胖猫不错 |
| [@atomtanstudio][nba] | NBA Jam 重制，同一套 gauntlet 循环 | 没做完任务 | DeepSeek 做完了 | 它"直接认输，说自己填不平这个差距" |
| [@mhdfaran][connect4] | 与 DeepSeek 下六局四子棋 | 3-3，思考中位数 9.5 秒 | DeepSeek：思考中位数 74.4 秒 | 快得多，比分相同 |

没有成本数字的单项运行与质量评价：

- [@ItsmeAjayKV][pagoda] 认为一次生成的宝塔胜过 DeepSeek 的结果，用直接 API 调用、最大思考、共 5 万 token——但也指出界面文字和按钮"像是 bootstrap 出现之前的年代"（[@ItsmeAjayKV][flower-pot]，7.6 万 token，其中 5.2 万是思考）。
- [@SahilPanhotra][peacock] 评价孔雀 SVG："动画相当顺滑，自行车还像样，配色也不错。但腿基本是棍子，一只翅膀变成了手臂，尾巴几乎不动。说实话不差。"
- [@kepochnik][nfs] 评价极品飞车重制："也许这个模型并不适合做游戏"。
- [@MiaAI_lab][gummy-bears] 对糖果小熊："😐"。[@JustMicrock][keygen] 对 Keygen Bench："失望，一股小模型的味儿"。
- [@yohakujpn][amongus] 40 分钟做出 Among Us 重制版，5,000 点数"省下一半多"。
- [@Amank1412][skygarden] 用一个提示词、几分钟做出浏览器游戏，并引用了标价："输入 $0.15/M、输出 $0.60/M"。
- [@PrajwalTomar_][spacebunny] 认出这个隐身模型：那个"只看 40 秒录屏就重建落地页"的 Space Bunny 就是早期的 M3.1 Flash，并引用厂商数字 DeepSWE 74%、BabyVision 91%。
- [@klarkxy][intro] 花了 41 分 27 秒做介绍视频，用了 MiniMax Code 自带的生图和音乐能力；另一次运行 12 分 45 秒、142 tok/s。
- [@ivanfioravanti][water] 实测"约 100 t/s，散文慢、代码快"。
- [@debugsenpai][seaplane] 和 [@geekbb][geekbb] 都是通过 OpenRouter 免费额度跑的。

两类来源合起来的规律：价格上 M3.1 Flash 几乎赢下发布当天的每一场对比，对 DeepSeek 通常是 2 倍，对 Opus 是一个数量级。效果上则大致对半分。倾向 DeepSeek 的地方是提示词遵循、动画和细节（好几位把 DeepSeek 的鹈鹕、池塘和糖果小熊排在前面）；倾向 MiniMax 的地方是设计审美和速度。没有人说它在写实度上赢过 Opus 5.5。

## 重跑一次再相信对比

设置一变结果就变。[@notjazii][pixel] 发现它在电脑操作和 Three.js 上很强，但在 `xhigh` 和 `max` 下容易幻觉；[@atomtanstudio][nba] 眼看着它放弃了一个 DeepSeek 做完的任务；[@RafaCrackYT][rafa] 和 [@loktar00][loktar] 都留了余地，说不知道参数量的情况下这个对比可能不公平。自己跑一遍：把提示词粘到 [Lab 文本竞技场][arena]，选两三个模型；或者按[教程](tutorial.md)用 API。

## 更多实测

- [Lab Evals 榜单][evals]——Artificial Analysis 数据，2026-10-19 快照。搜 "MiniMax" 就能亲眼看到它不在榜上。
- [Lab Pelican Test][pelican]——同一提示词、同一评分方式，画作直接展示。
- [SandBase Lab 上的全部 AI 视频合集][collections]——其他模型的同类列表，包括 [DeepSeek V4.1 Flash 1017][ds-repo] 和 [Gemini 4 Argon][gemini-repo]。

---

Lab 数据：[Evals 榜单][evals]（Artificial Analysis，2026-10-19 快照）与 [Pelican Test][pelican]（2026-10-20 读取）。创作者数据：他们本人的帖子，已附链接，未经我们独立验证。

[evals]: https://www.sandbase.ai/lab/evals?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[b-intel]: https://www.sandbase.ai/lab/evals/llm-intelligence?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[b-coding]: https://www.sandbase.ai/lab/evals/llm-coding?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[b-agentic]: https://www.sandbase.ai/lab/evals/llm-agentic?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[b-speed]: https://www.sandbase.ai/lab/evals/llm-speed?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[b-cost]: https://www.sandbase.ai/lab/evals/llm-cost?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[pelican]: https://www.sandbase.ai/lab/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[pelican-run]: https://www.sandbase.ai/lab/pelican-test?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=run
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=minimax%2Fminimax-m3.1-flash&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[collections]: https://www.sandbase.ai/lab/ai-videos?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[ds-repo]: https://github.com/sandbase-lab/awesome-deepseek-v4.1-flash
[gemini-repo]: https://github.com/sandbase-lab/awesome-gemini4-argon
[ds-pelican]: https://github.com/sandbase-lab/awesome-deepseek-v4.1-flash/blob/main/docs/model-comparison.md
[hype]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112206241137054071?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[ruben]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112211798493397408?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[marc]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112214607607562377?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[pixel]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112200201507311699?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[koi]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112227205300564211?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[tesla]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112263410301964712?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[spac]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112125242415956183?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[neurobin]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112133888613224558?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[fawn]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112217467775062514?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[bowser]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112186946210668839?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[hugo]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112238502305804542?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[vulkan]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112201004917940321?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[loktar]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112233437574914132?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[gummy]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112201041198620823?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[rafa]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112247645955895455?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[nutlope]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112238098147135880?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[narushima]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112192337925521881?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[miami]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112207066819375397?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[jumperz]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112226308868436154?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[alohaproxy]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112159579060486212?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[dom]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112257677543829665?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[nba]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112238012117680396?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[connect4]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112249487918047629?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[pagoda]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112121327285084300?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[flower-pot]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112111033359933516?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[peacock]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112241373961416717?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[nfs]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112201323106222579?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[gummy-bears]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112217267513499850?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[keygen]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112275978097480186?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[amongus]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112187468141465864?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[skygarden]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112220100300513770?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[spacebunny]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112178619120534014?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[intro]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112198804128895153?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[water]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112212819395432700?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[seaplane]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112207157177561460?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[geekbb]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112200254590447641?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
