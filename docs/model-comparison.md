# MiniMax M3.1 Flash vs DeepSeek V4.1 Flash 1017, Claude Opus 5.5 and Gemini 4 Argon

English · [简体中文](zh-CN/model-comparison.md) · [← Back to the collection](../README.md)

Two kinds of evidence, kept apart:

1. **What we measured.** The Lab [Evals boards][evals] show Artificial Analysis data, and the Lab [Pelican Test][pelican] runs the same fixed prompt on every model and scores the result. Small samples, but the same conditions for everyone.
2. **What creators reported.** Head-to-heads posted on X with their own prompts, costs and times. Useful context, not verified by us.

M3.1 Flash shipped on October 19, 2026, and every video in this list was posted within about eleven hours of release. That matters for reading the numbers: the measured side is thin because the model is one day old, and the creator side is large because launch day is when everyone runs the same test.

## What we measured: Lab Evals boards

**There is no MiniMax M3.1 Flash row on any Lab Evals board.** The boards read the Artificial Analysis snapshot of 2026-10-19 (index v4.3, 705 models); M3.1 Flash is not in it yet, so nothing on this page can place it against the frontier. The previous generation is there, which is the closest measured reference point that exists:

| Model (row on the board) | [Intelligence Index][b-intel] | [Coding][b-coding] | [Agentic][b-agentic] | [Output speed][b-speed] | [Cost per task][b-cost] |
|---|---|---|---|---|---|
| **MiniMax M3.1 Flash** | **not on the board** | — | — | — | — |
| MiniMax-M3 (previous generation) | 29.2 (#130 of 695) | 58.6 (#86 of 258) | 29.5 (#64 of 167) | 122 tok/s (#136 of 371) | $0.508 (#99 of 190) |
| Claude Opus 5.5 (Max) | 57.6 (#1) | not on the board | not on the board | 98 tok/s (#187) | $5.98 (#188) |
| Gemini 4 Argon (High) | 52.6 (#9) | — | — | not on the board | $1.99 (#158) |
| GPT-6.1 Sol (Max) | 51.8 (#13) | — | — | 60 tok/s (#281) | $0.724 (#112) |
| DeepSeek V4.1 Flash 1017 (Max) | 45.1 (#36) | — | — | 230 tok/s (#33) | $0.262 (#74) |
| Kimi K3 (Max) | 43.6 (#45) | 76.2 (#20) | 50.0 (#22) | 42 tok/s (#337) | $2.00 (#159) |
| GLM-5.3 (Max) | 44.8 (#38) | 74.8 (#29) | 53.1 (#8) | 95 tok/s (#194) | $2.01 (#160) |
| Claude Haiku 5.5 (Max) | 43.4 (#46) | — | — | 232 tok/s (#31) | $0.213 (#67) |

What this says, and what it doesn't:

- **Nothing about M3.1 Flash's score.** MiniMax's own previous model sits 16 points below DeepSeek V4.1 Flash 1017 and 28 below Opus 5.5 on the Intelligence Index; a launch-day 3x speed and one-third price claim does not tell you where the new one lands. Until Artificial Analysis measures it, treat every "beats DeepSeek" claim on X as a creator's single run.
- **The price gap creators describe shows up on the boards too.** Cost per task runs from $0.213 for Claude Haiku 5.5 and $0.262 for DeepSeek V4.1 Flash up to $5.98 for Opus 5.5 — more than 20x end to end, which makes the $0.014-against-$1.22 landing-page result below plausible from list price alone, with no measurement of M3.1 Flash behind it.
- **No coding or agentic row for most of the field.** Only Kimi K3, GLM-5.3 and MiniMax-M3 have coding rows here. Agent-style results (the four-job test below) are creator-run for that reason.

## What we measured: Lab Pelican Test

The [Pelican Test][pelican] asks each model for an SVG of a pelican riding a bicycle, once static and once animated (wheels spin, legs pedal, CSS/SMIL only). The page is rendered to PNG and scored 0 to 5 by an LLM judge on four questions: recognizable, actually riding, a bike that works, looks good. Cost is the real billed amount on SandBase.

Leaderboard rows from the [live leaderboard][pelican] on 2026-10-20 (22 models, 128 results):

| Rank | Model | Results | Score | Renders | Animation moves | Avg cost |
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

The MiniMax row is new and small: four scored results from two testers, all on October 19 inside a twenty-minute window (12:00–12:20 UTC). The public results feed lists six scored drawings from three runs that day, which is where the detail table below comes from:

| Time (UTC) | Kind | Score | Recognizable / riding / bike / looks | Output tokens | Time | Cost | Judge's note |
|---|---|---|---|---|---|---|---|
| 12:00 | Static | 3.75 | 4 / 4 / 3 / 4 | 3,304 | 32 s | $0.0056 | "A delightfully speedy pelican pedaling smoothly, even if its anatomy is a bit scrambled." |
| 12:03 | Static | 3.75 | 4 / 3 / 4 / 4 | 3,396 | 32 s | $0.0055 | "…its feet are dangling past the pedals." |
| 12:03 | Animated | 3.50 | 4 / 3 / 3 / 4 | 4,850 | 58 s | $0.0068 | "…slightly unusual frame geometry." |
| 12:00 | Animated | 3.00 | 4 / 3 / 2 / 3 | 4,422 | 51 s | $0.0068 | "…the strange twin-saddle bicycle frame defies mechanical logic." |
| 12:20 | Static | 3.00 | 4 / 3 / 2 / 3 | 2,597 | 19 s | $0.0065 | "…the disconnected front wheel defies physics." |
| 12:20 | Animated | 2.75 | 3 / 2 / 3 / 3 | 4,931 | 63 s | $0.0070 | "…it lacks the legs to actually pedal." |

What this says:

- **Recognizable, not quite riding.** Five of six drawings scored 4 on recognizable (the sixth scored 3), but only one scored 4 on actually riding — the rest scored 3, or 2 for the pelican with no legs — and the two weakest failed the bike itself (a twin saddle, a detached front wheel). The judge's notes keep coming back to legs that don't reach the pedals.
- **Mid-table quality at the lowest measured price.** 3.25 puts it level with Claude Haiku 5.5 and GPT-6 Luna, below DeepSeek V4.1 Flash 1017 (3.44) and Opus 5.5 (3.46), and at $0.006 a drawing it is roughly a third of DeepSeek's cost and a fortieth of Opus's.
- **It is cheap partly because it writes short.** 2,597 to 4,931 output tokens per drawing against DeepSeek's 12,000 to 18,500 on the same test ([the DeepSeek list measured that][ds-pelican]).
- **Sample size.** Six drawings, two accounts, one day. [Run it yourself][pelican-run] to add more.

## What creators reported

Same-prompt comparisons posted on X. Numbers are as the creator stated them: different tools (Minimax Code, OpenCode, OpenRouter, subscription plans), different reasoning settings, peak and off-peak prices, often one run. Click through to watch both results. DeepSeek V4.1 Flash 1017 is the rival in 22 of the 27 head-to-heads in this collection, so that is the column that matters most.

| Creator | Task | M3.1 Flash | Rival | Creator's verdict |
|---|---|---|---|---|
| [@thehypedotnews][hype] | Submarine chase in an underwater city, one HTML file, four flash models | ~$0.21, 29m 24s | DeepSeek $0.38, 27m 09s · Gemini 3.8 Flash $1.43, 40m 50s · Claude Haiku 5.5 ~$0.17, 35m 27s | 7x cheaper than Gemini, 1.8x cheaper than DeepSeek; asks which city looks most underwater |
| [@rubenssoto_ai][ruben] | Same prompt, same task | 1h 06m 51s, 8.12M tokens, $0.22 | DeepSeek: 1h 28m 27s, 89.49M tokens, $0.54 | Asks viewers which is better |
| [@marcthecreatorr][marc] | Same prompt | 1h 30m, ~$0.50 | DeepSeek: 80 min, $1.15 | "Simpler design at less than half the cost"; both far too slow for a Flash model |
| [@notjazii][pixel] | Pixel city, highest reasoning on both | 40 min, $0 | DeepSeek: 50 min, $0.40 | "Really surprised by how well minimax did" |
| [@aGim_asf][koi] | Living koi pond in Three.js | 3.3 min, $0 | DeepSeek: 1h 40m, $0.90 | "DeepSeek built the prettier pond, minimax fish could use some work" |
| [@atomic_chat_hq][tesla] | Tesla Roadster police chase | $2.34 | DeepSeek: $3.07 | — |
| [@SPAC89][spac] | Same test, Max | 38 min, ~200 tok/s on a subscription; 6% of a 5-hour limit on the $22 plan | DeepSeek: 38 min | "MiniMax takes the win"; prefers its quality |
| [@bbfu0382][neurobin] | Same figures as the row above | Same | Same | "MiniMax wins this one" |
| [@fawnunwrap][fawn] | FAWNBENCH | $0.029, ~3 min | DeepSeek: $0.067, ~5 min | "…for this. Wow." |
| [@ivanainai][bowser] | Bowser character | $0 (free), "the better Bowser" | DeepSeek: $0.06, "somehow worse" | "You get what you pay for" (ironically) |
| [@hug0_plat][hugo] | Pelican | free | DeepSeek: $0.24 | "MiniMax cooked DeepSeek on the pelican benchmark" |
| [@VulKan42069][vulkan] | Pelican Dream, one shot | — | DeepSeek | "King Deepseek" |
| [@loktar00][loktar] | No harness, 0 shot, 1 turn | Had one console error it was asked to fix | DeepSeek | "DeepSeek Flash is a monster… much better prompt adherence" |
| [@leo114119][gummy] | Gummy bear comparison | 57 min | DeepSeek | "It can do the job, but the result is a notch worse" (translated) |
| [@RafaCrackYT][rafa] | Tesla Roadster POV drive, four models, one shot | ~$1.37, 3h 11m | Opus 5.5 ~$110, 5h 43m · DeepSeek $0.66, 1h 12m · Gemini 4 Argon ~$4.50, 49m | Opus the quality winner; "MiniMax is the worst visually" |
| [@nutlope][nutlope] | Hardware launch landing page | $0.014, 4x faster | Claude Opus 5.5: $1.22 | "This model is insane at design… 88x cheaper" |
| [@narushima_][narushima] | Flying Roadster, same reference photos | $0.71 | Claude Opus 5.5: $11.27 | "Opus still wins on realism. But MiniMax got most of the way there" |
| [@davit__yan][miami] | 1986 Miami, neon and a white sports car | Cheaper | Claude Opus 5.5 | "It held up"; expected more from Opus |
| [@jumperz][jumperz] | Four agent jobs, four parallel agents each | 19m 52s, ~$0.30 in API tokens | Claude Opus 5.5 High: 10m 57s, at least $4.52 | Would wait 9 extra minutes for 1/15 the cost |
| [@alohaproxy][alohaproxy] | 3D mech assembly and launch | 71,038 output tokens, 10m 17s | Muse Wonder: 12,488 tokens, 1m 33s | "Absolutely insane" |
| [@domsilvestre][dom] | Three 3D scenes, one shot, no fixes | $0.19 for three | Claude Opus 5.5: $13.83 | Eiffel Tower weaker than M3's attempt; fish and cat solid |
| [@atomtanstudio][nba] | NBA Jam remake, same gauntlet loop | Did not finish the task | DeepSeek finished | It "threw in the towel and said it couldn't close the gap" |
| [@mhdfaran][connect4] | Six games of Connect Four against DeepSeek | 3-3, median think 9.5 s | DeepSeek: median think 74.4 s | MiniMax much faster, same score |

Solo runs and quality notes without a cost:

- [@ItsmeAjayKV][pagoda] rates the one-shot pagoda above DeepSeek's, from a direct API call with max thinking and 50K tokens total — but flags that the UI text and buttons "look like it's from before bootstrap was a thing" ([@ItsmeAjayKV][flower-pot], 76K tokens, 52K of them thinking).
- [@SahilPanhotra][peacock] on the peacock SVG: "the animation is pretty smooth, the bicycle looks decent, and the colors are nice. But the legs are basically sticks, one wing turned into an arm, and the tail barely moves. Not bad tbh."
- [@kepochnik][nfs] on a Need for Speed remake: "perhaps this model is not the best for creating games".
- [@MiaAI_lab][gummy-bears] on gummy bears: "😐". [@JustMicrock][keygen] on Keygen Bench: "disappointing. bad small model smell".
- [@yohakujpn][amongus] built an Among Us remake in 40 minutes and "saved more than half" of 5,000 credits.
- [@Amank1412][skygarden] built a browser game from one prompt in a few minutes and quotes the list price: "$0.15/M input and $0.60/M output tokens".
- [@PrajwalTomar_][spacebunny] identified the stealth model: the same "Space Bunny" that rebuilt a landing page from a 40-second screen recording was an early M3.1 Flash, and quotes vendor figures of 74% on DeepSWE and 91% on BabyVision.
- [@klarkxy][intro] ran 41m 27s for an intro video, using MiniMax Code's own image and music generation; another run: 12m 45s at 142 tok/s.
- [@ivanfioravanti][water] measured "~100 t/s, prose slower, code faster".
- [@debugsenpai][seaplane] and [@geekbb][geekbb] ran it free through OpenRouter.

The pattern across both sources: on price M3.1 Flash won nearly every launch-day head-to-head, usually by 2x against DeepSeek and by an order of magnitude against Opus. On quality the field split roughly in half. Where creators preferred DeepSeek it was prompt adherence, animation and detail (several of them put DeepSeek's pelican, pond and gummy bear ahead); where they preferred MiniMax it was design taste and speed. Nobody claimed it beats Opus 5.5 on realism.

## Rerun before you trust a comparison

Results move a lot with the setup. [@notjazii][pixel] found it strong on computer use and Three.js but prone to hallucinating on `xhigh` and `max`; [@atomtanstudio][nba] watched it abandon a task that DeepSeek finished; [@RafaCrackYT][rafa] and [@loktar00][loktar] both hedge that the comparison may be unfair without knowing the parameter count. Run the prompt yourself: paste it into the [Lab text arena][arena] with two or three models selected, or see the [tutorial](tutorial.md).

## More measurements

- [Lab Evals boards][evals] — Artificial Analysis data, snapshot 2026-10-19. Search for "MiniMax" to see the absence yourself.
- [Lab Pelican Test][pelican] — same prompt on every model, scored the same way, with the drawings on screen.
- [All AI video collections on SandBase Lab][collections] — the same list for other models, including [DeepSeek V4.1 Flash 1017][ds-repo] and [Gemini 4 Argon][gemini-repo].

---

Lab data: [Evals boards][evals] (Artificial Analysis, snapshot 2026-10-19) and [Pelican Test][pelican] (read 2026-10-20). Creator data: their posts, linked; not independently verified.

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
