# MiniMax M3.1 Flash prompt guide: how to prompt M3.1 Flash for video

English · [简体中文](zh-CN/prompt-guide.md) · [← Back to the collection](../README.md)

MiniMax M3.1 Flash doesn't output video. It writes code — an HTML page with Three.js, WebGPU, Canvas or SVG — and the creator records that page playing. Several creators made their pages inside MiniMax Code, which also generates the images and music those pages use. The patterns below come from prompts creators posted with their videos and from the fixed prompts SandBase Lab uses to test models. Each example links to the video it produced.

One thing that shapes every prompt: thinking is always on for this model, with reasoning effort from `low` to `max` ([`sandbase inspect`](https://www.sandbase.ai/model/minimax/minimax-m3.1-flash?utm_source=github&utm_medium=docs&utm_campaign=awesome-minimax-m3-1-flash)). It spends tokens before it writes, and those tokens come out of your `max_tokens`.

## 1. Say what file you want

Name the format and where it runs. The strongest pieces here all do it in the first line — sometimes in the creator's own words rather than a pasted prompt:

- "generate a 3d model flower pot, using Three.js, in a 3d model viewer style page" ([@ItsmeAjayKV][flower-pot]) — one shot, no harness, no extra turns.
- "make the most realistic water scene it could, in WebGPU, with a floating camera" ([@ivanfioravanti][water], quoted as written).
- An open brief works too, but say what the deliverable is: "尽你最大的能力，做一个介绍你自己（M3.1-Flash）和Minimax Code的视频" ("do your best to make a video introducing yourself and MiniMax Code") produced a 41-minute run ([@klarkxy][intro], translated).

## 2. Name the renderer, not just "3D"

The same scene looks very different in Three.js, WebGPU and SVG, and the model picks whichever you name. Naming it also decides what can break:

- Three.js as an ES module from a CDN import map is the default for 3D scenes here ([@ItsmeAjayKV][pagoda]).
- WebGPU when you want the water and light to look expensive ([@ivanfioravanti][water]); it only runs in a current Chrome.
- SVG with CSS or SMIL when the page has to stay small and record cleanly — the Pelican Test's animated prompt forbids JavaScript for exactly that reason ([@SahilPanhotra][peacock], [Lab Pelican Test][pelican]).
- Canvas for games and anything with a game loop ([@leo114119][fps]).

## 3. Put the whole absurd brief in one sentence

M3.1 Flash fills in a lot from a short brief, and launch-day creators leaned on that. The most quoted prompt of the day stacks three impossible objects and lets the model resolve them:

- "A PS5 controller waddling down a beach, a pelican standing on it, and the Mona Lisa riding a bicycle on the pelican's back" ([@jan_volad][beach]) — four models, one shot each, no fixes.
- "a living koi pond in Three.js with a waterfall, swimming koi and a 'feed the koi' button" ([@aGim_asf][koi]) — 3.3 minutes and $0.
- Take me back to 1986 Miami, neon, palm trees, a white sports car on Ocean Drive ([@davit__yan][miami]) — same brief as Claude Opus 5.5.

Short prompts give you the model's choices, not yours. When it matters, write the numbers down (see §5).

## 4. Ask for the state a recording should catch

If the point is a video, say what has to be moving when the camera is rolling:

- An autoplay camera move or a loop of known length, so nothing depends on a mouse — the same advice as the [tutorial](tutorial.md#4-turn-the-page-into-a-video).
- A visible change of state: the koi feeding, the mech finishing its assembly, the race starting. State you can check is also state a script can wait for.
- A frame that reads at 400 px. Previews here are 400 px wide ([`make_previews.py`](../scripts/make_previews.py)), and so are the cards on the Lab page; thin lines vanish.

## 5. Set the hard constraints up front

Long pages fail in predictable ways, and this model will happily spend a minute going the wrong way. Rule it out first:

- Everything inline: no external fonts, images or models. A missing CDN is the most common blank page. Three.js from an import map is the usual exception, because it is the renderer.
- The numbers the scene must respect: room counts, lives, gear ratios, camera height, seconds per loop.
- "Return only the complete HTML" so nothing has to be stripped.
- Give it a finish line. [@atomtanstudio][nba] watched it "throw in the towel and say it couldn't close the gap" on an NBA Jam remake, and [@notjazii][pixel] found it "hallucinates a lot on xhigh or max and starts doing stuff I didn't ask for" — which is also why its 100+ tok/s can still feel slow.

## 6. Let the tool stack do the polish

Most of the strong pieces here were not a bare API call:

- MiniMax Code generated the page, its images and its music in one run ([@klarkxy][intro]).
- A coding harness drove the loop: [@PrajwalTomar_][skygarden] built a whole game "with just one prompt in a few minutes" in OpenCode, [@ItsmeAjayKV][flower-pot] went straight to the API with max thinking.
- @ItsmeAjayKV's comparison is the useful one: one-shot with no harness still produced the pagoda they rate above DeepSeek's ([pagoda][pagoda]).

If you want a repeatable result, use the API and record it (§7). If you want the best-looking result and don't mind the wait, let a harness iterate.

## 7. Plan the recording and the budget

- Recording: [`scripts/record.mjs`](../scripts/record.mjs) opens the page at the size you give, records for N seconds and converts to H.264 (see the [tutorial](tutorial.md#4-turn-the-page-into-a-video)).
- Tokens: one one-shot page used 50K tokens total with max thinking ([@ItsmeAjayKV][pagoda]); the next one used 76K, 52K of them thinking ([@ItsmeAjayKV][flower-pot]). Budget accordingly — 128,000 `max_tokens` is what the README's curl example asks for.
- Time: launch-day one-shot pages ran from 3 minutes to over an hour ([@aGim_asf][koi], [@marcthecreatorr][marc]), and the 41-minute intro video was a harness run ([@klarkxy][intro]).
- Cost: the list price is $0.15 per million input tokens and $0.60 per million output tokens, and reasoning bills as output. See what creators actually paid in the [comparison](model-comparison.md).

## A prompt to start from

```text
Build [subject] as ONE self-contained HTML file that opens directly from disk.

Look: [style, e.g. low-poly / cinematic PBR / neon], [mood, lighting, palette].
Motion: [what moves and how]. Autoplay a [10]-second camera tour on load, then loop.
Interaction: [drag = …, scroll = …, click = …, keys = …].
Rules: [the numbers it must respect: rooms, lives, waves, gear ratios, collisions].

Technical:
- Use Three.js as an ES module from a CDN import map. No other libraries.
- No external images, fonts or audio: generate textures in code, sound with Web Audio.
- Fill the viewport, no scrolling, 60 fps on a laptop.
- Before you finish, check that the page loads with zero console errors and that every control works.
- Return only the complete HTML, from <!DOCTYPE html> to </html>. Do not abbreviate.
```

Try it on the [Lab text arena][arena] to run it on M3.1 Flash and other models side by side, or with the API in the [tutorial](tutorial.md).

## Settings

- **Output budget.** Thinking is always on, and the hidden reasoning tokens count toward `max_tokens` and bill as output. Two documented one-shot pages used 50K and 76K completion tokens; set `max_tokens` to 100,000 or more. SandBase accepts up to 512,000.
- **Reasoning effort.** `low`, `medium`, `high`, `xhigh` or `max`. Creators who name a setting split between max for quality ([@SPAC89][spac], [@ItsmeAjayKV][pagoda]) and warnings that `xhigh`/`max` wander off-brief ([@notjazii][pixel]). A middle setting plus a finish line is the safer default.
- **One shot vs. iteration.** Launch-day results are mostly one shot. Where creators iterated, the loop was a harness, and the cost went up: 41 minutes and MiniMax Code's own image and music generation for the intro video ([@klarkxy][intro]).

---

Quotes are short excerpts credited to their authors; follow the links for full prompts and videos. Translations from Chinese are ours.

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
