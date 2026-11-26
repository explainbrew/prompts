# lemo-opuscar: a whole film from one prompt, made in code

A Claude Code plugin with **99 film styles**. You name a style and a topic; the agent writes the film in code: every frame drawn with canvas / WebGL, a text-to-speech narrator, a score built from free samples. No camera, no video model, no stock footage ([README](https://github.com/lemomo-ai/lemo-opuscar)).

## Install (two lines, from the README)

```
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
```

Then, in Claude Code, type `/lemo-opuscar:lemo-opuscar` and it asks what you want, or say it in one sentence, for example: *"Make a 30-second film in Swiss Motion style about five rules for a poster."*

- Needs Node 20+, ffmpeg 7+ and Python 3.11+ (or uv); the agent installs the rest.
- Use `/effort high`.

## The honest part

- One film takes an agent about **30–60 minutes and a fair amount of tokens** (README wording).
- Browse the [gallery](https://lemomo-ai.github.io/lemo-opuscar/) first: pick a style by what the picture looks like.

## Licence, in short

- Code: MIT. Docs and style prompts: CC BY-NC 4.0 (with extra permission to make your own films, commercial ones included). Films you make: yours.
- Demo films: CC BY 4.0. Anthropic's character Clawd and third-party interfaces are **not** covered ([LICENSE](https://github.com/lemomo-ai/lemo-opuscar/blob/main/LICENSE)).

## Credits for our video

Film footage: **Lemo-Opuscar by Lemomo (LemoLab)** — demo films *Swiss Motion Graphics, Material Grid, Ukiyo-e, Pixel RPG, Bauhaus Shapes, ASCII CRT, Neon Tubes, Red Paper-cut, One-line Drawing* from [github.com/lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar), licensed [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). **Changed:** cropped to squares, cut into short clips, audio removed, overlaid with our captions and labels. Three code lines shown from `styles/swiss-motion/demo/film.js` (MIT). We did not run the plugin for this video; the prompt card is an illustration of the README's prompt pattern. Voice: AI.

---

From the [Explainbrew](https://github.com/explainbrew/prompts) short "Find the frame a human made.", Nov 2026. Facts checked Nov 22, 2026. Not affiliated with lemo-opuscar, LemoLab or Anthropic.
