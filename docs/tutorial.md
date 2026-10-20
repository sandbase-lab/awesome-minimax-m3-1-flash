# MiniMax M3.1 Flash tutorial: from prompt to video

English · [简体中文](zh-CN/tutorial.md) · [← Back to the collection](../README.md)

From a prompt to an MP4 in four steps. M3.1 Flash writes a web page; you play it and record it.

## 1. Start from a video you like

Open any title in the [collection](../README.md) to reach its page on [SandBase Lab][lab]: the video, the original post and, when the creator shared one, the prompt. Press **Recreate**. Lab opens the text arena with the post loaded and MiniMax M3.1 Flash selected. Sign in, run it, and you get the HTML back, with a live preview.

No prompt shared? Write one with the [prompt guide](prompt-guide.md). It has a fill-in template.

## 2. Compare models on the same prompt

In the [text arena][arena], add one or two more models next to M3.1 Flash (for example `deepseek/deepseek-v4.1-flash`, `anthropic/claude-opus-5.5` or `google/gemini-4-argon`) and run once. Every model gets the same words, and each result shows its cost and time. That is how most of this collection was made on launch day — 27 of the 55 videos here are head-to-heads, 22 of them against DeepSeek V4.1 Flash 1017 — and it is the quickest way to check a claim from the [comparison page](model-comparison.md) on your own task.

## 3. Or call the API

MiniMax M3.1 Flash is `minimax/minimax-m3.1-flash` on SandBase, OpenAI-compatible, since October 19, 2026.

1. Create a key in the [console][keys] and export it: `export SANDBASE_API_KEY=sk-sb-...`
2. Save your prompt as `prompt.txt`.
3. Run:

```bash
jq -n --rawfile prompt prompt.txt '{
  model: "minimax/minimax-m3.1-flash",
  max_tokens: 128000,
  messages: [{role: "user", content: $prompt}]
}' |
curl -sS --max-time 900 https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d @- > response.json

jq -r '.choices[0].message.content' response.json | sed '/^```/d' > minimax.html
jq '.usage' response.json
```

- `max_tokens: 128000`: thinking is always on for this model and the hidden reasoning tokens come out of the same budget. One documented one-shot page used 76,000 completion tokens, 52,000 of them thinking ([@ItsmeAjayKV][flower-pot]); with a tight limit you get a truncated page and still pay for the tokens. SandBase accepts up to 512,000.
- `--max-time 900`: one long page can take several minutes, and harness runs on this model were reported at 41 minutes to 3 hours.
- `sed '/^```/d'` removes Markdown fences if the model added them.
- `usage` shows the tokens you were billed for, including `completion_tokens_details.reasoning_tokens`. Reasoning bills at the output rate ($0.60 per million), input at $0.15 per million; prices are on the [model page][model].
- Optional: add `reasoning_effort` — `low`, `medium`, `high`, `xhigh` or `max` — to trade thinking for speed and cost. Creators who tried `xhigh` and `max` warn that it can wander off the brief ([@notjazii][pixel]).
- Images work the same way: the model is multimodal, so you can put a reference frame in `messages[].content` instead of describing it ([@narushima_][roadster] compared it with Claude Opus 5.5 on "same prompt, same reference photos").

Open `minimax.html` in a browser. If it is blank, open the developer console: the usual causes are a truncated file (raise `max_tokens`) or a CDN that did not load (ask for everything inline). One launch-day creator also flagged the opposite problem — a page that worked but whose "text and buttons look like it's from before bootstrap was a thing" ([@ItsmeAjayKV][flower-pot]) — so check the UI, not just the render.

### With the SandBase CLI

The same call through the [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli), which reads `SANDBASE_API_KEY` as well:

```bash
npx -y @sandbaseai/cli@latest inspect minimax/minimax-m3.1-flash   # input fields and price, free
jq -n --rawfile prompt prompt.txt '{max_tokens: 128000, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_minimax_minimax_m3_1_flash -f input.json --timeout 900 -o result.json
```

`-o result.json` saves the response; the page is in the assistant message, as with the API.

## 4. Turn the page into a video

Most creators screen-record the page. To get the same clip every time, record it headlessly with [`scripts/record.mjs`](../scripts/record.mjs):

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # or use your installed Chrome: export RECORD_CHANNEL=chrome
node scripts/record.mjs minimax.html minimax.mp4 12 1920 1080   # 12 seconds at 1080p
```

It opens the page at the size you give, records for that many seconds, and converts to H.264 MP4 with ffmpeg. For a clean result, ask in the prompt for an autoplay camera tour or a fixed-length loop (see [prompt guide §4](prompt-guide.md#4-ask-for-the-state-a-recording-should-catch)), so nothing depends on a mouse.

Want sound? The recording is picture only, so add audio in the edit. Several pages here already have music in them, because MiniMax Code generates images and audio alongside the page ([@klarkxy][intro]); if you record the page yourself, capture the tab audio, not the microphone.

Many videos in this list came out of a harness rather than a single API call: MiniMax Code for the page plus its assets ([@klarkxy][intro]), OpenCode for a whole game ([@PrajwalTomar_][skygarden]), and "no harness, 0 shot, 1 turn" for the purists ([@loktar00][loktar]).

## Run generated code safely

The HTML is code you haven't read. Opening it from disk is usually fine for a single-file page, but it can still load scripts and make network requests. For anything you don't trust, or to run many pages automatically, use a [SandBase Sandbox][sandbox]: an isolated environment with a time limit and no access to your files or keys.

## Share it

Post your video on X with the prompt and mention MiniMax M3.1 Flash. To have it added here, [submit it](https://github.com/sandbase-lab/awesome-minimax-m3-1-flash/issues/new?template=submit-video.yml); accepted posts go into the Lab collection and show up in this list on the next daily sync.

[lab]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[arena]: https://www.sandbase.ai/lab/x/llm-arena?models=minimax%2Fminimax-m3.1-flash&utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[keys]: https://www.sandbase.ai/console/keys?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[model]: https://www.sandbase.ai/model/minimax/minimax-m3.1-flash?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[sandbox]: https://www.sandbase.ai/landing/sandbox?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[flower-pot]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112111033359933516?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[pixel]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112200201507311699?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[roadster]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112192337925521881?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[intro]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112198804128895153?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[skygarden]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112220100300513770?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
[loktar]: https://www.sandbase.ai/lab/ai-videos/minimax-m3-1-flash/2112233437574914132?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash
