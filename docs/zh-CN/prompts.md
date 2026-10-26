# MiniMax M3.1 Flash 提示词

[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

共 25 条 MiniMax M3.1 Flash 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 M3.1 Flash 一键 **复刻**。第一次写 M3.1 Flash 提示词？先看 [提示词写法](prompt-guide.md)。

每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，有的把全文放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。

- [3D 场景](#3d-scene) (2)
- [动效](#motion-graphics) (1)
- [游戏](#game) (3)
- [产品界面](#ui-demo) (3)
- [讲解](#explainer) (1)
- [发布片](#launch-film) (1)
- [测试对比](#comparison) (14)

<a id="3d-scene"></a>

## 3D 场景

### 使用 Three.js 生成的 3D 花盆查看器

[@ItsmeAjayKV](https://x.com/ItsmeAjayKV/status/2112111033359933516) · 0:32 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112111033359933516/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112111033359933516?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
First test results for @MiniMax_AI MiniMax-M3.1-Flash

Asked it to generate a 3d model flower pot, using Three.js, in a 3d model viewer style page.

Good result actually, considering this is one-shot without harness and no extra turns.

But text and buttons looks like its from before bootstrap was a thing, wierd.

76k tokens total
52k thinking
24k output
```

### WebGPU写实水面场景与悬浮相机

[@ivanfioravanti](https://x.com/ivanfioravanti/status/2112212819395432700) · 0:13 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112212819395432700/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112212819395432700?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
My first experiment with omp + MiniMax M3.1 Flash
I will now try the same with MiniMax Code to see if there are differences.

Prompt: make the most realistic water scene it could, in WebGPU, with a floating camera.

Average of ~100 t/s  prose slower, code faster.
```

<a id="motion-graphics"></a>

## 动效

### 纯代码生成的MiniMax品牌宣传视频

[@xueyu1125](https://x.com/xueyu1125/status/2113569157400928345) · 0:54 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2113569157400928345/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2113569157400928345?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
MiniMax M3.1 Flash实测第二波，我直接在MiniMax M3.1 Flash一句话生成Minimax的宣传视频，效果非常惊艳

Prompt： Motion design生成一个minimax品牌宣传视频

完全是通过代码生成的转场特效，我感觉质感挺不错，能和Claude Opus 5.5碰一碰吗🤔

最终生成效果如下👇
```

<a id="game"></a>

## 游戏

### 通过纯代码生成的登月着陆器游戏

[@ivanfioravanti](https://x.com/ivanfioravanti/status/2112459195521896760) · 0:27 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112459195521896760/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112459195521896760?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
MiniMax M3.1 Flash is so much better than Space Bunny! RL continued through these weeks with feedback constantly fed to the training run itself.

Here Lunar Lander! I know it seems trivial, but try with past generation models.
Prompt below 👇
```

### Flappy Bird复刻游戏

[@k2sbhai](https://x.com/k2sbhai/status/2112481123343474731) · 0:20 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112481123343474731/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112481123343474731?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
built this with MiniMax M3.1 Flash 😳

prompt: build a Flappy Bird clone

- clouds hills and ground all moving
- bird tilt up and down when it flap
- screen shake and feathers fly when u crash
- live score best score and play again

used max reasoning with 1M context, one shot and it take 38 mins 👀
```

### 可玩的类我的世界3D体素沙盒游戏

[@MAXdeg0](https://x.com/MAXdeg0/status/2112791024112140782) · 0:29 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112791024112140782/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112791024112140782?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
Built this Minecraft style voxel game with MiniMax M3.1 Flash

Prompt: Build a playable 3D voxel sandbox

-> Procedural terrain with hills and trees

-> First person movement, jumping and sprinting

-> Break and place blocks

->Inventory and hotbar

-> Day/night cycle

Went from a prompt to a playable game running in the browser.

link below to try it out
```

<a id="ui-demo"></a>

## 产品界面

### 具备光影交互效果的太空兔网页展示

[@0x_fokki](https://x.com/0x_fokki/status/2112500742829277565) · 0:15 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112500742829277565/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112500742829277565?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
whoever handed out the beta of MiniMax M3.1 Flash for free as Space Bunny has zero survival instinct.

MiniMax Code runs on the computer and M3.1 Flash writes the whole page. the prompt is the only brief it gets.

[the page is in the 20 seconds below, here is how it got built]

1. open an empty folder in MiniMax Code and drop in 2 pictures: the bunny dark and the bunny lit
2. paste one prompt: the light that follows the cursor, the intro, the nav and the stats
3. pick M3.1 Flash and let it run. it writes the files and starts the page on its own

I left effort on max, which is the default anyway.

the beta ran #1 on OpenCode for 12 days. the release ties Opus 5 on BankerToolBench and ranks #1 among Chinese models on computer use.

unlimited in MiniMax Code until Oct 25.
```

### 单HTML文件完整操作系统演示

[@Israfilv2](https://x.com/Israfilv2/status/2113182324628308476) · 0:58 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2113182324628308476/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2113182324628308476?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
i gave MiniMax M3.1 Flash one prompt and it built me a whole operating system in a single HTML file 😳

here's what it pulled off:
→ frontend: boot screen, lock screen, dock and spotlight search, all clean and smooth
→ complex logic: a window manager where you can drag, resize, snap and minimize
→ full apps: terminal, files, notes, paint, music and snake, all sharing one file system
→ 3D: a galaxy app built in Three.js
→ agentic tool use: an AI assistant inside the OS, running on M3.1 Flash itself, that opens apps and creates files for you

took 20 minutes and cost me $0 extra (M3.1 Flash is unlimited for MiniMax Code subscribers till oct 25) 💀

prompt in the replies
```

### 交互式落地页与3D场景演示

[@MengTo](https://x.com/MengTo/status/2113553675482525940) · 0:51 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2113553675482525940/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2113553675482525940?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
I made these landing pages with MiniMax M3.1 Flash, at a fraction of the cost of frontier models.

Three keyboard sites, a SaaS page, a rainy 3D Singapore at night and a little 3D lighthouse game.

My favourite is the exploded keyboard one. I made one render of the keyboard in MiniMax first, and every painting, photo and film came from that render, so it's the same board in every room.

$0.15 per 1M input tokens, $0.60 per 1M output. Here's the whole process, prompts included.
```

<a id="explainer"></a>

## 讲解

### MiniMax Code与模型的自我介绍视频

[@klarkxy](https://x.com/klarkxy/status/2112198804128895153) · 1:18 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112198804128895153/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112198804128895153?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
41分27秒，使用了minimax code自己带的生图、音乐能力。

提示词：
尽你最大的能力，做一个介绍你自己（M3.1-Flash）和Minimax Code的视频。越酷炫、越惊艳越好
```

<a id="launch-film"></a>

## 发布片

### Pi Agent Desktop产品宣传片

[@chasen_liao](https://x.com/chasen_liao/status/2113138389172224237) · 0:30 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2113138389172224237/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2113138389172224237?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
挖槽？！花叔这个 huashu-motion skills 是真的绝 🤯

我之前也用过不少 motion skill，没一个能做到这个效果
这次真的就一句话：“给我的项目做个产品宣传片
它直接给 Pi Agent Desktop 出了一整支 30 秒的片子”

最离谱的是模型用的是 MiniMax M3.1 Flash，现在在 OpenRouter 上免费爽用

搭配 Claude Code 开 Ultra Code，模型这块一分钱没花

花叔用的是 Opus 5.5，我用免费模型跑出来的片子也一点不虚 😭

装上只要一行：
npx skills add alchaincyf/huashu-motion
```

<a id="comparison"></a>

## 测试对比

### 3D 机甲组装与发射序列对比演示

[@alohaproxy](https://x.com/alohaproxy/status/2112159579060486212) · 0:34 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112159579060486212/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112159579060486212?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
MiniMax M3.1 Flash is absolutely insane🤯

I tested it against Muse Wonder using the exact same prompt to build a 3D mech assembly + launch sequence via AiHubMix

>MiniMax M3.1 Flash: 71,038 output tokens · 10m 17s
 >Muse Wonder: 12,488 output tokens · 1m 33s

Here's how they compare side by side. Which one cooked harder?
```

### Opus 5.5 与 MiniMax M3.1 Flash 迈阿密场景对比

[@davit__yan](https://x.com/davit__yan/status/2112207066819375397) · 0:25 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112207066819375397/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112207066819375397?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
Gave Opus 5.5 and the new MiniMax M3.1 Flash the same task: take me back to 1986 Miami.
Neon, palm trees, a white sports car on Ocean Drive.
I was sure Opus would win easily.
Then Flash came back, way cheaper, and honestly, it held up.
To be honest, I expected more from Opus 😅
What should I compare next?
```

### MiniMax 与 DeepSeek 的 Three.js 锦鲤池对比

[@aGim_asf](https://x.com/aGim_asf/status/2112227205300564211) · 0:22 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112227205300564211/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112227205300564211?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
MiniMax M3.1 Flash vs DeepSeek V4.1 1017

Task: living koi pond in Three.js with a waterfall, swimming koi and a "feed the koi" button

•MiniMax: 3.3 mins, $0
•DeepSeek: 1h 40m, $0.9

deepseek built the prettier pond, minimax fish could use some work

what do you think?
```

### 四款大模型对比生成的超现实海滩场景

[@jan_volad](https://x.com/jan_volad/status/2112245037224382556) · 0:15 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112245037224382556/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112245037224382556?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
A PS5 controller waddling down a beach, a pelican standing on it, and the Mona Lisa riding a bicycle on the pelican's back

DeepSeek V4.1 Flash 1017 vs MiniMax M3.1 Flash vs GPT-6 Luna vs Claude Haiku 5.5, one shot each
```

### 对比两款模型生成的低轨航天飞机与地球3D场景

[@sakatayasha](https://x.com/sakatayasha/status/2112484646663647344) · 0:34 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112484646663647344/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112484646663647344?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
MiniMax M3.1 Flash vs GLM 5.3 Flash 

tested with the exact same prompt

the task: a cinematic 3D scene of earth with a space shuttle in low orbit, with heat shield tiles, volumetric clouds, city lights on the dark side and sunlight flaring off the metal

> M3.1 Flash finished everything in 48 mins, $0 (it's free on opencode for 72 hours)
> meanwhile GLM 5.3 Flash took 1 hr 6 mins to finish everything for $3.20

M3.1 Flash's build was more interactive, had a cleaner UI and finished 18 mins faster, free, and the better result

which one do you think won?
```

### 复古电脑产品落地页对比

[@de1lymoon](https://x.com/de1lymoon/status/2112524119862370755) · 0:12 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112524119862370755/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112524119862370755?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
this model is insane at design. and 96x cheaper than claude opus 5.5 on my test

i gave minimax m3.1 flash (left) and opus 5.5 (right) the same prompt: build a landing page for a retro computer you can take apart

minimax: $0.0056 / opus 5.5: $0.56 -> same prompt, 96x cheaper 

prices per 1M tokens:
m3.1 flash: $0.15 in / $0.60 out
opus 5.5: $4 in / $20 out 

judge the sites yourself
```

### 对比两款模型生成的Three.js日本浮岛3D场景

[@0xMorlex](https://x.com/0xMorlex/status/2112538682955632663) · 0:24 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112538682955632663/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112538682955632663?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
this model is insane at design. and ~12x cheaper than claude opus 5.5 on my test

i gave minimax m3.1 flash and opus 5.5 the same prompt: build a 3d floating island in japan in one html file. pagoda, torii, sakura, waterfall, all procedural three.js

minimax: ~$0.012 / opus 5.5: ~$0.14 -> same prompt, ~12x cheaper

(est. from output length, minimax wrote 3x more code)

no edits on either. judge the islands yourself
```

### 两款模型生成3D毛绒蜘蛛效果对比

[@SamgreyAi](https://x.com/SamgreyAi/status/2112988681933926420) · 0:18 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112988681933926420/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112988681933926420?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
I gave two AI models the same prompt: “build a 3D plush spider.” One of them made me want to squeeze my screen.

GPT-6 Astra vs. MiniMax M3.1 Flash.
Same brief. No tweaks. No second attempts.
Here’s what came back:

🟣 GPT-6 Astra: a cute, cartoonish spider. Fun, but it felt like a toy.

🟠 MiniMax M3.1 Flash: a fuzzy tarantula with soft fur, striped legs, and lighting that made it look genuinely squeezable.

The hard part of this task isn’t the 3D geometry. It’s turning a word like “plush” into something you can see. Flash got it, and honestly, I didn’t expect that.

But the spider isn’t the real story.

Here’s why @MiniMax_AI M3.1 Flash is worth a look:

⚡ 200+ tokens/sec output speed
💻 Built for coding and complex software engineering
🤖 Designed for multi-step agentic workflows
💸 70% lower overall cost on agentic tasks vs. its predecessor, according to MiniMax

Speed, capability, cost. Few models get all three right.
My takeaway: benchmarks tell you what a model can do. A real challenge shows you what it will do when it counts.
So skip the leaderboard today. Take one project you care about, give the same brief to two models, and compare.
You’ll learn more in 10 minutes than from 10 comparison threads.

Which two models should I put head-to-head next?
```

### 3D地球与航天飞机场景生成对比

[@MAXdeg0](https://x.com/MAXdeg0/status/2113230869699637548) · 0:30 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2113230869699637548/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2113230869699637548?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
MINIMAX M3.1 FLASH vs ASTRA SOL 6.1 

Tested with the exact same prompt.

The task: build a cinematic 3D Earth scene with a space shuttle in low orbit, heat shield tiles, volumetric clouds, city lights on the dark side, and sunlight reflecting off the metal.

- MiniMax M3.1 Flash: 15mins, $0

- Astra Sol 6.1: 1 hr mins, $3.20

M3.1 Flash finished 45minutes faster, delivered the better result, and had a more interactive experience with a cleaner UI.

One was faster and free.

Which model wins?
```

### 四款模型制作动态图形作品集的对比

[@EvoLinkAi](https://x.com/EvoLinkAi/status/2113299349740364076) · 0:15 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2113299349740364076/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2113299349740364076?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
MiniMax M3.1 Flash 🆚 DeepSeek V4.1 Flash 🆚 GPT-6 Luna 🆚 Claude Haiku 5.5

Task: a 15-second motion graphics showreel
• MiniMax: $0.26
• DeepSeek: $0.19
• Luna: $0.06
• Haiku: $0.13

Minimax packed in detail, Luna gave it room to breathe

What do you think? Prompt below👇
```

### MiniMax与Claude果冻俄罗斯方块对比

[@0xRhinoX](https://x.com/0xRhinoX/status/2113336344587952230) · 0:31 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2113336344587952230/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2113336344587952230?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
No way MiniMax did this for $1.60

Same prompt: Tetris, but every block is JELLY.

MiniMax M3.1 Flash - $1.60, 12m
Claude Opus 5.5 - $8.40, 43m

5x cheaper. 3.5x faster. I had to look twice to tell them apart.

Opus added combos and little sparks when a line pops. MiniMax made the prettier glass.

So is the Space Bunny the new king, or is Opus still worth it?

Play both below
```

### Three.js制作的电动机动画演示

[@EvoLinkAi](https://x.com/EvoLinkAi/status/2113605044289650733) · 0:40 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2113605044289650733/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2113605044289650733?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
Same prompt: 40s Three.js electric motor animation.

DeepSeek V4.1 Flash 1017: 2h 14s | ~$0.83
MiniMax M3.1 Flash: 2h 43m | ~$0.25

Which one wins?

Explore more MiniMax M3.1 Flash prompts 👇
 https://t.co/FGAyNjaqyK
```

### 纯代码3D篝火基准测试对比

[@EvoLinkAi](https://x.com/EvoLinkAi/status/2113707025066492154) · 0:30 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2113707025066492154/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2113707025066492154?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
🔥DeepSeek V4.1 Flash 1017 beats MiniMax M3.1 Flash in this code-only 3D campfire test.

DeepSeek V4.1 Flash 1017
Est. cost: $0.33 | Time: 3h 12m 35s

MiniMax M3.1 Flash
Est. cost: $0.51 | Time: ~3h 52m

Both via EvoLink.

Prompt below👇
```

### 鲨鱼电梯生日提示词生成对比

[@sunra_ai](https://x.com/sunra_ai/status/2114434062991659015) · 0:15 · [观看](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2114434062991659015/video.mp4) · [在 SandBase Lab 复刻](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2114434062991659015?lang=zh-CN&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
we gave two brains three words: shark. elevator. birthday.

minimax m3.1 flash vs claude opus 5.5, same prompt in the sunra agent, same video model underneath (seedance 2.5)

who did more with less?
```
