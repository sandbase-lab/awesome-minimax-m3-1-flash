"""Every model-specific value for this list. The other scripts are generic and read from here."""
import os

ORIGIN = os.environ.get('LAB_ORIGIN', 'https://www.sandbase.ai').rstrip('/')
SITE = 'https://www.sandbase.ai'  # public links in READMEs and docs always use the canonical host

SLUG = 'minimax-m3-1-flash'
REPO = 'sandbase-lab/awesome-minimax-m3-1-flash'

CFG = dict(
    slug=SLUG,
    name='MiniMax M3.1 Flash',
    short='M3.1 Flash',  # how the prose refers to the model after the first mention
    vendor='MiniMax',
    model_id='minimax/minimax-m3.1-flash',
    repo=REPO,
    repo_url=f'https://github.com/{REPO}',
    campaign='awesome-minimax-m3-1-flash',
    lab_collection=f'{SITE}/lab/ai-videos/{SLUG}',
    lab_data=f'{ORIGIN}/lab/data/ai-videos/{SLUG}.json',
    media_prefix=f'{SITE}/lab/media/x/{SLUG}/',
    model_page=f'{SITE}/model/minimax/minimax-m3.1-flash',
    arena=f'{SITE}/lab/x/llm-arena?models=minimax%2Fminimax-m3.1-flash',
    evals=f'{SITE}/lab/evals',
    pelican=f'{SITE}/lab/pelican-test',
    keys=f'{SITE}/console/keys',
    sandbox=f'{SITE}/landing/sandbox',
    lab_home=f'{SITE}/lab/',
    all_collections=f'{SITE}/lab/ai-videos',
    user_agent=f'awesome-minimax-m3-1-flash-sync/1.0 (+https://github.com/{REPO})',
    html_out='minimax.html',
    # Output limit for the curl example. Thinking is always on for this model and the hidden
    # reasoning tokens come out of max_tokens: a creator's first one-shot page used 76,000
    # completion tokens, 52,000 of them thinking (@ItsmeAjayKV), so 128,000 leaves room for a
    # long page. `sandbase inspect minimax/minimax-m3.1-flash --json` accepts up to 512,000.
    max_tokens=128000,
    max_tokens_limit=512000,
    context_length=1000000,
    guide_patterns=7,  # numbered sections in docs/prompt-guide.md
    banner_title='Awesome MiniMax M3.1 Flash',
    banner_sub='Videos · prompts · tutorial · model comparison',
    # Finished pieces only on the banner: no comparisons or other models' names.
    banner_skip=('vs', 'versus', 'comparison', 'compar', 'benchmark', 'test', 'opus', 'claude', 'sonnet',
                 'haiku', 'gpt', 'gemini', 'argon', 'deepseek', 'kimi', 'qwen', 'glm', 'muse'),
    not_affiliated={'en': 'Not affiliated with or endorsed by MiniMax.', 'zh-CN': '与 MiniMax 无隶属或背书关系。'},
    # No SandBase blog post on this model existed when the list shipped (blog.sandbase.ai sitemap,
    # checked 2026-10-20: only three MiniMax H3 video-model posts). build_readme.py skips the
    # reading section while this is empty — do not invent links here.
    reading=[],
)

# README and prompt-index copy. Placeholders in {braces} are filled by build_readme.py
# ({name}, {short}, {model_id}, {html_out}, links such as {lab_stats} or {model_page}, counts {n}/{a}/{p}).
# Every fact here is sourced: `sandbase inspect minimax/minimax-m3.1-flash`, the Lab collection's
# own posts (linked), the Lab Pelican Test leaderboard on 2026-10-20, and the Lab Evals boards
# (Artificial Analysis snapshot 2026-10-19), which have no row for this model yet.
COPY = {
    'en': {
        'switch': 'English · [简体中文](README.zh-CN.md)',
        'tagline': 'A curated list of **MiniMax M3.1 Flash examples**: videos, prompts and demos made with MiniMax-M3.1-Flash, the fast, low-cost tier of MiniMax\'s M3.1 generation, released on October 19, 2026. Three.js and WebGPU 3D scenes, SVG and canvas animation, motion graphics, product UI and playable browser games, most of them written as one self-contained HTML page from a prompt, each one credited to its creator and linked to the original post.',
        'alt': 'Awesome MiniMax M3.1 Flash: videos, prompts, tutorial and model comparison',
        'stats': '**{n} videos** from **{a} creators** · **{p}** with the creator\'s prompt · synced daily from [SandBase Lab]({lab_stats})',
        'start': 'Start here',
        'start_rows': [
            ('Watch the videos', '[Browse by category](#contents) below, or [play them full-size on SandBase Lab]({lab_quickstart})'),
            ('Copy a prompt', '[Prompt index](docs/prompts.md): every video that comes with its prompt'),
            ('Write your own prompt', '[Prompt guide](docs/prompt-guide.md): {guide_patterns} patterns and a fill-in template'),
            ('Make a video', '[Tutorial](docs/tutorial.md): prompt → HTML → MP4, with the API, the CLI and a recording script'),
            ('Pick a model', '[MiniMax M3.1 Flash vs. DeepSeek V4.1 Flash 1017, Claude Opus 5.5 and Gemini 4 Argon](docs/model-comparison.md)'),
            ('Try it now', '[Run MiniMax M3.1 Flash in the Lab arena]({arena_quickstart}), next to other models'),
        ],
        'goal': 'I want to…', 'where': 'Go to',
        'how': 'Click a preview to play the video. Click a title for the post, the prompt and **Recreate** on SandBase Lab. **@handle** links to the creator\'s post on X.',
        'contents': 'Contents',
        'featured': 'Featured',
        'show_all': 'Show all {n}',
        'recreate': 'Recreate a video with {name}',
        'recreate_body': [
            'Every video page on [SandBase Lab]({lab_recreate}) has a **Recreate** button: it sends the post to {short} in the Lab text arena and returns the code, ready to play in the browser.',
            '',
            'With the API, {name} is `{model_id}` on SandBase (OpenAI-compatible); the id has served M3.1 Flash since it shipped on October 19, 2026. Put a prompt in `prompt.txt`, create a key in the [console]({keys}), and run:',
        ],
        'recreate_after': 'Open `{html_out}` in a browser, or run it in a [SandBase Sandbox]({sandbox}) to keep generated code isolated. Thinking is always on for this model, and the hidden reasoning tokens come out of `max_tokens`, so the call above asks for 128,000. Full walkthrough: [tutorial](docs/tutorial.md). Pricing: [model page]({model_page}).',
        'prompt_tag': 'prompt',
        'more': '**[See all {n} on SandBase Lab →]({lab_section})**',
        'faq': 'FAQ',
        'faq_items': [
            ('What is MiniMax M3.1 Flash?', 'MiniMax-M3.1-Flash is the fast, cost-efficient tier of MiniMax\'s M3.1 generation, released on October 19, 2026. It accepts text, image and video input, has a 1,000,000-token context window and up to 512,000 output tokens, and thinking is always on, with reasoning effort from `low` to `max`. MiniMax says it is 3x faster and about a third of the price of M3, and SandBase\'s model card calls it open-weight. On SandBase it is `{model_id}`. Source: `sandbase inspect minimax/minimax-m3.1-flash`.'),
            ('How are these MiniMax M3.1 Flash videos made?', 'The model doesn\'t render video. It writes a web page (HTML with Three.js, WebGPU, Canvas or SVG), and the creator records the page playing. Several creators ran it inside MiniMax Code, which also generates images and music for the page, and a few let it drive a coding harness. See the [tutorial](docs/tutorial.md).'),
            ('Where do I find the prompt for a video?', 'Videos tagged **prompt** come with the creator\'s prompt on their Lab page. The [prompt index](docs/prompts.md) lists all of them.'),
            ('How do I write a good MiniMax M3.1 Flash prompt?', 'Name one self-contained HTML file and the renderer you want (Three.js, WebGPU, Canvas or SVG), describe the scene, the controls and the state a recording should catch, ban external assets, and ask it to test its own page. Leave a large `max_tokens`: thinking is always on and shares that budget. Details and a template: [prompt guide](docs/prompt-guide.md).'),
            ('How do I use the MiniMax M3.1 Flash API?', 'On SandBase the model id is `{model_id}` on the OpenAI-compatible `/v1/chat/completions` endpoint. One key works for every model, and `reasoning_effort` takes `low`, `medium`, `high`, `xhigh` or `max`. See [Recreate](#recreate) and the [model page]({model_page}).'),
            ('Is MiniMax M3.1 Flash better than DeepSeek V4.1 Flash 1017, Claude Opus 5.5 or Gemini 4 Argon?', 'Creators mostly ran it against DeepSeek, and they disagree. On price {short} usually wins: $0.21 against $0.38 for the same submarine scene, $0.22 against $0.54 for a pixel city, $0.50 against $1.15 on one prompt, and $0.014 against $1.22 for Claude Opus on a landing page. On quality it is split — several creators preferred its design work or its pelican, while others found DeepSeek\'s prompt adherence and detail better, and one called it the weakest of four on a Roadster drive. There is no measured answer yet: the Lab [Evals boards]({evals}) (Artificial Analysis, snapshot 2026-10-19) have no MiniMax M3.1 Flash row, so the Lab [Pelican Test]({pelican}) is the only measured result — 3.25, rank 6 of 22, at about $0.006 a drawing. Details: [model comparison](docs/model-comparison.md).'),
            ('How much does one video cost?', 'Creators report from $0.014 (a hardware landing page) and $0.029 (one benchmark task) up to $2.34 (a Tesla Roadster chase scene), with most one-shot pages between $0.02 and $0.70. The list price on SandBase is $0.15 per million input tokens and $0.60 per million output tokens, and reasoning tokens bill as output.'),
            ('Can I reuse these videos?', 'No, not by default. They belong to their creators. See [MEDIA-RIGHTS](MEDIA-RIGHTS.md).'),
        ],
        'contribute': 'Suggest a video',
        'contribute_body': 'Know a MiniMax M3.1 Flash creation that should be here? [Open a submission]({repo_url}/issues/new?template=submit-video.yml) with the original X post. Accepted posts are added on SandBase Lab and show up here on the next daily sync. If this list helped you, a ⭐ helps others find it.',
        'credits': 'Credits & rights',
        'credits_body': [
            'Every video, prompt and post belongs to its creator. Cards credit the author and link to the original post. The MIT license covers this repository\'s scripts only. To correct a credit or remove a video, see [MEDIA-RIGHTS](MEDIA-RIGHTS.md).',
            '{not_affiliated}',
        ],
        'footer': 'Maintained by [SandBase Lab]({lab_home}) · [All AI video collections]({all_collections})',
        'p_title': 'MiniMax M3.1 Flash prompts',
        'p_switch': 'English · [简体中文](zh-CN/prompts.md) · [← Back to the collection](../README.md)',
        'p_intro': '{n} MiniMax M3.1 Flash videos whose creators shared the prompt. Open one to read the prompt, watch the video and **Recreate** it with {short} on SandBase Lab. New to prompting {short}? Start with the [prompt guide](prompt-guide.md).',
        'p_note': 'Each entry quotes the creator\'s post as published on X, where the prompt is shared. Some creators describe the task rather than pasting the whole prompt, and some put the full text in a reply: open the post on X to read the thread. Posts keep the creator\'s language.',
        'p_watch': 'Watch',
        'p_open': 'Recreate on SandBase Lab',
    },
    'zh-CN': {
        'switch': '[English](README.md) · 简体中文',
        'tagline': '精选 **MiniMax M3.1 Flash 案例**合集：用 MiniMax-M3.1-Flash（MiniMax M3.1 系列中更快、更便宜的一档，2026 年 10 月 19 日发布）做出的视频、提示词和演示。包括 Three.js 与 WebGPU 3D 场景、SVG 与 Canvas 动画、动效、产品界面和可在浏览器里玩的游戏，大多是模型根据提示词写成的单文件网页，均注明作者并链接原帖。',
        'alt': 'Awesome MiniMax M3.1 Flash：视频、提示词、教程和模型对比',
        'stats': '共 **{n} 条视频**，来自 **{a} 位创作者** · **{p} 条**附作者提示词 · 每天从 [SandBase Lab]({lab_stats}) 同步',
        'start': '从这里开始',
        'start_rows': [
            ('看视频', '在下方 [按分类浏览](#contents)，或 [在 SandBase Lab 大屏播放]({lab_quickstart})'),
            ('复制提示词', '[提示词索引](docs/zh-CN/prompts.md)：所有附带提示词的视频'),
            ('自己写提示词', '[提示词写法](docs/zh-CN/prompt-guide.md)：{guide_patterns} 条写法和一个填空模板'),
            ('做一个视频', '[教程](docs/zh-CN/tutorial.md)：提示词 → HTML → MP4，含 API、CLI 调用和录屏脚本'),
            ('选模型', '[MiniMax M3.1 Flash 对比 DeepSeek V4.1 Flash 1017、Claude Opus 5.5 和 Gemini 4 Argon](docs/zh-CN/model-comparison.md)'),
            ('马上试试', '[在 Lab 竞技场运行 MiniMax M3.1 Flash]({arena_quickstart})，和其他模型并排对比'),
        ],
        'goal': '我想…', 'where': '去这里',
        'how': '点击预览图播放视频；点击标题前往 SandBase Lab 查看原帖、提示词，并一键 **复刻**；**@作者** 链接到 X 原帖。',
        'contents': '目录',
        'featured': '精选',
        'show_all': '展开全部 {n} 条',
        'recreate': '用 {name} 复刻视频',
        'recreate_body': [
            '[SandBase Lab]({lab_recreate}) 的每个视频页都有 **复刻** 按钮：在 Lab 文本竞技场把帖子内容发给 {short}，返回可在浏览器直接播放的代码。',
            '',
            '用 API 的话，{name} 在 SandBase 上的模型 ID 是 `{model_id}`（兼容 OpenAI），自 2026 年 10 月 19 日发布起就是它。把提示词写进 `prompt.txt`，在 [控制台]({keys}) 创建 Key，然后运行：',
        ],
        'recreate_after': '用浏览器打开 `{html_out}`，或在 [SandBase Sandbox]({sandbox}) 中运行，让生成的代码保持隔离。这个模型的思考始终开启，隐藏的推理 token 也占用 `max_tokens`，所以上面的示例给到 128000。完整步骤见 [教程](docs/zh-CN/tutorial.md)，价格见 [模型页]({model_page})。',
        'prompt_tag': '提示词',
        'more': '**[在 SandBase Lab 查看全部 {n} 条 →]({lab_section})**',
        'faq': '常见问题',
        'faq_items': [
            ('MiniMax M3.1 Flash 是什么？', 'MiniMax-M3.1-Flash 是 MiniMax M3.1 系列中更快、更便宜的一档，2026 年 10 月 19 日发布。它接受文本、图片和视频输入，上下文窗口 100 万 token，最多输出 512K token；思考始终开启，推理强度可从 `low` 调到 `max`。MiniMax 称它比 M3 快 3 倍、价格约为三分之一，SandBase 的模型卡片把它标为开放权重模型。在 SandBase 上它是 `{model_id}`。来源：`sandbase inspect minimax/minimax-m3.1-flash`。'),
            ('这些 MiniMax M3.1 Flash 视频是怎么做出来的？', '模型并不直接渲染视频。它写出一个网页（用 Three.js、WebGPU、Canvas 或 SVG 的 HTML），作者再把页面播放过程录下来。也有作者在 MiniMax Code 里运行，让它同时生成页面里的图片和音乐；少数作者让它驱动编码 harness。见 [教程](docs/zh-CN/tutorial.md)。'),
            ('在哪里找到视频的提示词？', '标有 **提示词** 的视频，其 Lab 页面上有作者的提示词。[提示词索引](docs/zh-CN/prompts.md) 列出了全部。'),
            ('怎么写好 MiniMax M3.1 Flash 提示词？', '指定输出一个独立的 HTML 文件，并说明用哪个渲染方式（Three.js、WebGPU、Canvas 或 SVG）；描述场景、交互操作，以及录屏需要捕捉的状态；禁止外部素材，并让它自测页面。`max_tokens` 要给足：思考始终开启，也占用这个额度。详细写法和模板见 [提示词写法](docs/zh-CN/prompt-guide.md)。'),
            ('怎么调用 MiniMax M3.1 Flash API？', '在 SandBase 上模型 ID 是 `{model_id}`，使用兼容 OpenAI 的 `/v1/chat/completions` 接口，一个 Key 调用所有模型；`reasoning_effort` 可选 `low`、`medium`、`high`、`xhigh`、`max`。见 [复刻](#recreate) 和 [模型页]({model_page})。'),
            ('MiniMax M3.1 Flash 比 DeepSeek V4.1 Flash 1017、Claude Opus 5.5 或 Gemini 4 Argon 更强吗？', '创作者大多拿它和 DeepSeek 对比，而且结论不一致。价格上 {short} 通常更省：同一段海底场景 $0.21 对 $0.38，像素城市 $0.22 对 $0.54，同一提示词 $0.50 对 $1.15，落地页 $0.014 对 Claude Opus 的 $1.22。效果上则是分裂的：好几位创作者更喜欢它的设计或鹈鹕，也有人认为 DeepSeek 的提示词遵循度和细节更好，还有一位在 Roadster 驾驶对比里把它排在四款之末。目前没有实测结论：Lab [Evals 榜单]({evals})（Artificial Analysis 数据，2026-10-19 快照）还没有 MiniMax M3.1 Flash 这一行，唯一的实测结果是 Lab [Pelican Test]({pelican})：3.25 分，22 个模型中排第 6，每张图约 $0.006。详见 [模型对比](docs/zh-CN/model-comparison.md)。'),
            ('做一个视频要花多少钱？', '创作者报告的花费从 $0.014（一个硬件产品落地页）、$0.029（一项基准任务）到 $2.34（特斯拉 Roadster 追逐场景）不等，多数一次生成的页面在 $0.02 到 $0.70 之间。SandBase 标价为每百万输入 token $0.15、每百万输出 token $0.60，推理 token 按输出计费。'),
            ('可以转用这些视频吗？', '默认不可以，视频归作者所有。见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。'),
        ],
        'contribute': '推荐作品',
        'contribute_body': '发现了应该收录的 MiniMax M3.1 Flash 作品？附上 X 原帖 [提交给我们]({repo_url}/issues/new?template=submit-video.yml)。通过后会先加入 SandBase Lab，下一次每日同步时出现在这里。觉得有用的话，点个 ⭐ 能让更多人看到。',
        'credits': '致谢与权利',
        'credits_body': [
            '所有视频、提示词和帖子归作者所有。每张卡片都注明作者并链接原帖。MIT 许可证只覆盖本仓库的脚本。更正署名或下架视频请见 [MEDIA-RIGHTS](MEDIA-RIGHTS.md)。',
            '{not_affiliated}',
        ],
        'footer': '由 [SandBase Lab]({lab_home}) 维护 · [全部 AI 视频合集]({all_collections})',
        'p_title': 'MiniMax M3.1 Flash 提示词',
        'p_switch': '[English](../prompts.md) · 简体中文 · [← 返回合集](../../README.zh-CN.md)',
        'p_intro': '共 {n} 条 MiniMax M3.1 Flash 视频，作者公开了提示词。打开即可查看提示词、观看视频，并在 SandBase Lab 上用 {short} 一键 **复刻**。第一次写 {short} 提示词？先看 [提示词写法](prompt-guide.md)。',
        'p_note': '每条都按 X 上发布的原文引用作者帖子。有的作者描述的是任务而不是完整提示词，有的把全文放在回复里，请打开 X 原帖查看讨论串。帖子原文保留作者语言。',
        'p_watch': '观看',
        'p_open': '在 SandBase Lab 复刻',
    },
}

# Labels mirror shared/ai-videos.ts VIDEO_CATEGORIES in the Lab repo.
CATEGORIES = {
    '3d-scene': ('3D scenes', '3D 场景'),
    'motion-graphics': ('Motion graphics', '动效'),
    'game': ('Games', '游戏'),
    'ui-demo': ('Product UI', '产品界面'),
    'particles': ('Particles & shapes', '粒子与形状'),
    'data-viz': ('Charts & diagrams', '图表图解'),
    'kinetic-type': ('Kinetic type', '文字动效'),
    'explainer': ('Explainers', '讲解'),
    'launch-film': ('Launch films', '发布片'),
    'short-film': ('Short films', '短片'),
    'music-video': ('Music videos', '音乐视频'),
    'anime': ('Anime', '动画'),
    'action': ('Action', '动作'),
    'ad': ('Ads', '广告'),
    'comparison': ('Tests & comparisons', '测试对比'),
    'showcase': ('Model showcases', '模型展示'),
}


def utm(medium, content=None):
    q = f'utm_source=github&utm_medium={medium}&utm_campaign={CFG["campaign"]}'
    return q + (f'&utm_content={content}' if content else '')
