# MiniMax M3.1 Flash 教程：从提示词到视频

[English](../tutorial.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)

四步把提示词变成 MP4。M3.1 Flash 写网页，你来播放并录制。

## 1. 从喜欢的视频开始

在[合集](../../README.zh-CN.md)里点任意标题，进入它在 [SandBase Lab][lab] 的页面：视频、原帖，以及作者公开的提示词（如果有）。点 **复刻**，Lab 会打开文本竞技场，自动填好帖子内容并选中 MiniMax M3.1 Flash。登录后运行，就能拿到 HTML，并带实时预览。

作者没有公开提示词？照[提示词写法](prompt-guide.md)自己写一条，里面有填空模板。

## 2. 用同一个提示词对比模型

在[文本竞技场][arena]里，在 M3.1 Flash 旁边再加一两个模型（例如 `deepseek/deepseek-v4.1-flash`、`anthropic/claude-opus-5.5` 或 `google/gemini-4-argon`），跑一次。所有模型拿到同样的文字，每个结果都显示花费和耗时。发布当天这个合集大多就是这样产出的——55 条视频里有 27 条是同提示词对比，其中 22 条对的是 DeepSeek V4.1 Flash 1017——这也是在你自己任务上验证[对比页](model-comparison.md)结论的最快方式。

## 3. 或者直接调用 API

MiniMax M3.1 Flash 在 SandBase 上的模型 ID 是 `minimax/minimax-m3.1-flash`，兼容 OpenAI，自 2026 年 10 月 19 日起提供。

1. 在[控制台][keys]创建 Key 并导出：`export SANDBASE_API_KEY=sk-sb-...`
2. 把提示词保存为 `prompt.txt`。
3. 运行：

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

- `max_tokens: 128000`：这个模型的思考始终开启，隐藏的推理 token 也占用同一份额度。有一个记录在案的一次生成页面用了 7.6 万补全 token，其中 5.2 万是思考（[@ItsmeAjayKV][flower-pot]）；额度给小了，你会拿到被截断的页面，而且照样为这些 token 付费。SandBase 最多接受 512000。
- `--max-time 900`：长页面要跑好几分钟，而这个模型在 harness 里的运行被记录为 41 分钟到 3 小时。
- `sed '/^```/d'` 去掉模型可能加上的 Markdown 代码围栏。
- `usage` 显示计费的 token，包括 `completion_tokens_details.reasoning_tokens`。推理按输出价（每百万 $0.60）计费，输入每百万 $0.15；价格见[模型页][model]。
- 可选：加 `reasoning_effort` —— `low`、`medium`、`high`、`xhigh` 或 `max` —— 用思考换速度和成本。试过 `xhigh` 和 `max` 的作者提醒说它可能跑偏（[@notjazii][pixel]）。
- 图片同理：这个模型是多模态的，可以把参考图放进 `messages[].content`，而不用费劲描述（[@narushima_][roadster] 就是"相同提示词、相同参考图"与 Claude Opus 5.5 对比的）。

用浏览器打开 `minimax.html`。如果一片空白，打开开发者工具：常见原因是被截断的文件（加大 `max_tokens`）或 CDN 没加载（要求所有资源内联）。发布当天也有一位作者遇到相反的问题——页面能跑，但"文字和按钮看起来像是 bootstrap 出现之前的年代"（[@ItsmeAjayKV][flower-pot]），所以除了画面，也检查一下 UI。

### 用 SandBase CLI

同一个调用也可以走 [SandBase CLI](https://www.npmjs.com/package/@sandbaseai/cli)，它同样读取 `SANDBASE_API_KEY`：

```bash
npx -y @sandbaseai/cli@latest inspect minimax/minimax-m3.1-flash   # 输入字段和价格，免费
jq -n --rawfile prompt prompt.txt '{max_tokens: 128000, messages: [{role: "user", content: $prompt}]}' > input.json
npx -y @sandbaseai/cli@latest run sandbase_minimax_minimax_m3_1_flash -f input.json --timeout 900 -o result.json
```

`-o result.json` 保存响应；页面在 assistant 消息里，和 API 一样。

## 4. 把页面录成视频

大多数作者是直接录屏。想每次得到一样的片段，可以用 [`scripts/record.mjs`](../../scripts/record.mjs) 无头录制：

```bash
npm i -D playwright@1.56.1
npx playwright install chromium          # 或使用本机 Chrome：export RECORD_CHANNEL=chrome
node scripts/record.mjs minimax.html minimax.mp4 12 1920 1080   # 12 秒，1080p
```

它按你给的尺寸打开页面，录指定秒数，再用 ffmpeg 转成 H.264 MP4。想要干净的效果，就在提示词里要求自动镜头巡游或定长循环（见[提示词写法 §4](prompt-guide.md#4-说清录制时要捕捉的状态)），让整个画面不依赖鼠标。

想要声音？录制本身只有画面，音频在剪辑里加。这里不少页面自带音乐，因为 MiniMax Code 会连页面带图片和音频一起生成（[@klarkxy][intro]）；如果你自己录页面，记得捕获标签页音频，而不是麦克风。

这个列表里很多视频并非一次 API 调用的产物：MiniMax Code 负责页面和素材（[@klarkxy][intro]），OpenCode 做出了完整游戏（[@PrajwalTomar_][skygarden]），也有坚持"不用 harness、0 shot、1 turn"的（[@loktar00][loktar]）。

## 安全运行生成的代码

这段 HTML 是你没读过的代码。单文件页面从本地打开通常没问题，但它仍然可以加载脚本、发起网络请求。对于不完全信任的内容，或者要批量运行很多页面，请使用 [SandBase Sandbox][sandbox]：一个有时限、接触不到你的文件和 Key 的隔离环境。

## 分享

把视频发到 X，附上提示词并 @ MiniMax M3.1 Flash。想被收录，就[提交给我们](https://github.com/sandbase-lab/awesome-minimax-m3-1-flash/issues/new?template=submit-video.yml)；通过后会先进入 Lab 合集，下一次每日同步时出现在本列表。

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
