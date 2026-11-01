# How Claude Code makes our videos — the pipeline

Every Explainbrew short is built with Claude Code. The agent writes the code and runs the tools; a human picks the idea, approves the style and says "yes" to every paid or public step. Numbers below are from one real video (Insomnia, Nov 1, 2026).

## Steps

1. **Facts.** The agent reads the project's rules and writes a fact sheet from primary sources (README, GitHub API). Anything not confirmed stays out of the voiceover.
2. **Script.** About 110 words, 40–45 seconds. The search phrase goes into the first sentence and the first frame.
3. **Voice.** ElevenLabs Eleven v4 through an API gateway: ~700 characters ≈ a few cents per video, only after a human "yes".
4. **Timing.** Speed the voice up 7% (`ffmpeg atempo=1.07`), then get a timestamp for every word (Whisper locally, or ElevenLabs Scribe).
5. **Animation as code.** [Remotion](https://www.remotion.dev) (React): each phrase gets its own object on screen, keyed to the word timings. Check stills with the platforms' safe zones overlaid, then render.
6. **Loudness.** Normalize to −14 LUFS (`ffmpeg loudnorm=I=-14`).
7. **Publishing.** Schedule the post on TikTok, YouTube Shorts, Instagram, X and Threads through the Buffer API, and publish the matching guide here at the same time (a scheduled GitHub Actions merge). Again, only after a "yes".

## Prefer a timeline?

[Hyperframes](https://github.com/heygen-com/hyperframes) (Apache-2.0) is an open-source Claude Code plugin with a visual timeline editor, live preview and local rendering:

```bash
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes
```

Some optional features can use paid HeyGen services. Check before you rely on "free".

---
From the [Explainbrew](https://github.com/explainbrew/prompts) short "How Claude Code makes these videos", Nov 2026.
