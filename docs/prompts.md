# MiniMax M3.1 Flash prompts

English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)

15 MiniMax M3.1 Flash videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with M3.1 Flash on SandBase Lab. New to prompting M3.1 Flash? Start with the [prompt guide](prompt-guide.md).

Each entry quotes the creator's post as published on X, where the prompt is shared. Some creators describe the task rather than pasting the whole prompt, and some put the full text in a reply: open the post on X to read the thread. Posts keep the creator's language.

- [3D scenes](#3d-scene) (2)
- [Games](#game) (3)
- [Product UI](#ui-demo) (1)
- [Explainers](#explainer) (1)
- [Tests & comparisons](#comparison) (8)

<a id="3d-scene"></a>

## 3D scenes

### A 3D flower pot viewer in Three.js

[@ItsmeAjayKV](https://x.com/ItsmeAjayKV/status/2112111033359933516) · 0:32 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112111033359933516/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112111033359933516?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
First test results for @MiniMax_AI MiniMax-M3.1-Flash

Asked it to generate a 3d model flower pot, using Three.js, in a 3d model viewer style page.

Good result actually, considering this is one-shot without harness and no extra turns.

But text and buttons looks like its from before bootstrap was a thing, wierd.

76k tokens total
52k thinking
24k output
```

### Realistic water scene in WebGPU with floating camera

[@ivanfioravanti](https://x.com/ivanfioravanti/status/2112212819395432700) · 0:13 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112212819395432700/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112212819395432700?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
My first experiment with omp + MiniMax M3.1 Flash
I will now try the same with MiniMax Code to see if there are differences.

Prompt: make the most realistic water scene it could, in WebGPU, with a floating camera.

Average of ~100 t/s  prose slower, code faster.
```

<a id="game"></a>

## Games

### Lunar Lander game generated with code

[@ivanfioravanti](https://x.com/ivanfioravanti/status/2112459195521896760) · 0:27 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112459195521896760/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112459195521896760?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
MiniMax M3.1 Flash is so much better than Space Bunny! RL continued through these weeks with feedback constantly fed to the training run itself.

Here Lunar Lander! I know it seems trivial, but try with past generation models.
Prompt below 👇
```

### A Flappy Bird clone game

[@k2sbhai](https://x.com/k2sbhai/status/2112481123343474731) · 0:20 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112481123343474731/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112481123343474731?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
built this with MiniMax M3.1 Flash 😳

prompt: build a Flappy Bird clone

- clouds hills and ground all moving
- bird tilt up and down when it flap
- screen shake and feathers fly when u crash
- live score best score and play again

used max reasoning with 1M context, one shot and it take 38 mins 👀
```

### Playable Minecraft style 3D voxel sandbox game

[@MAXdeg0](https://x.com/MAXdeg0/status/2112791024112140782) · 0:29 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112791024112140782/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112791024112140782?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

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

## Product UI

### Interactive space bunny webpage with dynamic lighting

[@0x_fokki](https://x.com/0x_fokki/status/2112500742829277565) · 0:15 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112500742829277565/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112500742829277565?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

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

<a id="explainer"></a>

## Explainers

### Introduction video for MiniMax Code and model

[@klarkxy](https://x.com/klarkxy/status/2112198804128895153) · 1:18 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112198804128895153/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112198804128895153?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
41分27秒，使用了minimax code自己带的生图、音乐能力。

提示词：
尽你最大的能力，做一个介绍你自己（M3.1-Flash）和Minimax Code的视频。越酷炫、越惊艳越好
```

<a id="comparison"></a>

## Tests & comparisons

### 3D mech assembly and launch sequence comparison

[@alohaproxy](https://x.com/alohaproxy/status/2112159579060486212) · 0:34 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112159579060486212/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112159579060486212?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
MiniMax M3.1 Flash is absolutely insane🤯

I tested it against Muse Wonder using the exact same prompt to build a 3D mech assembly + launch sequence via AiHubMix

>MiniMax M3.1 Flash: 71,038 output tokens · 10m 17s
 >Muse Wonder: 12,488 output tokens · 1m 33s

Here's how they compare side by side. Which one cooked harder?
```

### Opus 5.5 and MiniMax M3.1 Flash comparison

[@davit__yan](https://x.com/davit__yan/status/2112207066819375397) · 0:25 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112207066819375397/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112207066819375397?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
Gave Opus 5.5 and the new MiniMax M3.1 Flash the same task: take me back to 1986 Miami.
Neon, palm trees, a white sports car on Ocean Drive.
I was sure Opus would win easily.
Then Flash came back, way cheaper, and honestly, it held up.
To be honest, I expected more from Opus 😅
What should I compare next?
```

### Comparing Three.js koi ponds by MiniMax and DeepSeek

[@aGim_asf](https://x.com/aGim_asf/status/2112227205300564211) · 0:22 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112227205300564211/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112227205300564211?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
MiniMax M3.1 Flash vs DeepSeek V4.1 1017

Task: living koi pond in Three.js with a waterfall, swimming koi and a "feed the koi" button

•MiniMax: 3.3 mins, $0
•DeepSeek: 1h 40m, $0.9

deepseek built the prettier pond, minimax fish could use some work

what do you think?
```

### Surreal beach scene compared across four models

[@jan_volad](https://x.com/jan_volad/status/2112245037224382556) · 0:15 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112245037224382556/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112245037224382556?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
A PS5 controller waddling down a beach, a pelican standing on it, and the Mona Lisa riding a bicycle on the pelican's back

DeepSeek V4.1 Flash 1017 vs MiniMax M3.1 Flash vs GPT-6 Luna vs Claude Haiku 5.5, one shot each
```

### Comparing 3D Earth and space shuttle scenes in orbit

[@sakatayasha](https://x.com/sakatayasha/status/2112484646663647344) · 0:34 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112484646663647344/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112484646663647344?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
MiniMax M3.1 Flash vs GLM 5.3 Flash 

tested with the exact same prompt

the task: a cinematic 3D scene of earth with a space shuttle in low orbit, with heat shield tiles, volumetric clouds, city lights on the dark side and sunlight flaring off the metal

> M3.1 Flash finished everything in 48 mins, $0 (it's free on opencode for 72 hours)
> meanwhile GLM 5.3 Flash took 1 hr 6 mins to finish everything for $3.20

M3.1 Flash's build was more interactive, had a cleaner UI and finished 18 mins faster, free, and the better result

which one do you think won?
```

### Retro computer landing page comparison

[@de1lymoon](https://x.com/de1lymoon/status/2112524119862370755) · 0:12 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112524119862370755/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112524119862370755?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
this model is insane at design. and 96x cheaper than claude opus 5.5 on my test

i gave minimax m3.1 flash (left) and opus 5.5 (right) the same prompt: build a landing page for a retro computer you can take apart

minimax: $0.0056 / opus 5.5: $0.56 -> same prompt, 96x cheaper 

prices per 1M tokens:
m3.1 flash: $0.15 in / $0.60 out
opus 5.5: $4 in / $20 out 

judge the sites yourself
```

### Comparing procedural 3D Japanese floating islands in Three.js

[@0xMorlex](https://x.com/0xMorlex/status/2112538682955632663) · 0:24 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112538682955632663/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112538682955632663?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

```text
this model is insane at design. and ~12x cheaper than claude opus 5.5 on my test

i gave minimax m3.1 flash and opus 5.5 the same prompt: build a 3d floating island in japan in one html file. pagoda, torii, sakura, waterfall, all procedural three.js

minimax: ~$0.012 / opus 5.5: ~$0.14 -> same prompt, ~12x cheaper

(est. from output length, minimax wrote 3x more code)

no edits on either. judge the islands yourself
```

### 3D plush spider comparison between two models

[@SamgreyAi](https://x.com/SamgreyAi/status/2112988681933926420) · 0:18 · [Watch](https://www.sandbase.ai/lab/media/x/minimax-m3-1-flash/2112988681933926420/video.mp4) · [Recreate on SandBase Lab](https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112988681933926420?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash&utm_content=prompt-index)

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
