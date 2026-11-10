# What Claude Code does in our reels (and what it never touches)

Who does what in an Explainbrew reel. This page gives you the overview. It isn't a recipe, so you won't find our prompts or settings here.

## Claude Code's part

[Claude Code](https://code.claude.com/docs/en/overview) is "an agentic coding tool that reads your codebase, edits files, runs commands". In our pipeline it does the work and runs the commands:

| Step | What Claude Code does |
| --- | --- |
| Facts | Builds a fact sheet from primary sources. Only facts with a source make it into the script. Anything unconfirmed is flagged and left out |
| Script | Drafts the script and the voiceover text from those facts |
| Scenes | Writes every scene as code. A video is a JSON spec, and each phrase gets its own object on screen |
| Word timing | Runs speech-to-text on the finished voice, which gives every word a start and end time, so captions and objects land on cue |
| Render | Runs the render to MP4 with [Remotion](https://www.remotion.dev) (React) or [HyperFrames](https://github.com/heygen-com/hyperframes) (HTML, Apache-2.0) |
| Hooks | Our animated openers are HTML pages rendered with HyperFrames, written by Claude Code in sessions we directed |

## What Claude never touches

- **The voice.** The voice you hear is an AI voice from [ElevenLabs](https://try.elevenlabs.io/s3p4rzmexcmc), not Claude. Claude only runs the tools around it.
- **The topic and the hook.** We pick both.
- **Approval.** We approve the script and the final cut.
- **Anything paid or posted.** Every paid call and every external action (posting, uploads, pushes) waits for our explicit "yes" for that run.

## What we don't claim

- We've never timed "idea → finished reel", so we don't make speed claims.
- No reel was made from "one prompt" or "three prompts".
- Remotion isn't free for everyone: its free license covers individuals and companies of up to 3 people. Check the [license](https://www.remotion.dev/) for your case.

For the longer version of the pipeline, see [claude-video-pipeline](../claude-video-pipeline/).

## Want a reel like this for your product?

Email us: **hi@explainbrew.com**

---

From the [Explainbrew](https://github.com/explainbrew/prompts) short "What Claude does in our reels", Nov 2026. ElevenLabs link is an affiliate link (see the [main README](../README.md#tools-we-use-to-make-the-videos)). Not affiliated with Anthropic, Remotion or HeyGen.
