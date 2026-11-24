# Five free tools, a whole motion stack

Five open-source tools that cover a motion workflow from reference to final file. "Free" here means their licences; your agent and voice are separate.

| # | Tool | Job | Licence | Command |
| --- | --- | --- | --- | --- |
| 1 | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | pulls just the section of a reference you need | Unlicense | `yt-dlp --download-sections "*0:10-0:25" URL` |
| 2 | [whisper.cpp](https://github.com/ggml-org/whisper.cpp) | local transcript with word timing | MIT | `whisper-cli -m models/ggml-base.en.bin -f voice.wav -ml 1 -oj` |
| 3 | [HyperFrames](https://github.com/heygen-com/hyperframes) | renders an HTML/CSS/JS page into an MP4 | Apache-2.0 | `npx hyperframes render <project> --output reel.mp4` |
| 4 | [FFmpeg](https://ffmpeg.org) | cuts, encodes, mixes | LGPL 2.1+ (GPL if built so) | `ffmpeg -i picture.mp4 -i mix.wav -c:v copy reel.mp4` |
| 5 | [ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill) | an agent skill + MCP: 42 local FFmpeg tools, no cloud, no API keys | MIT | `npx ffmpeg-skill setup` |

## What's real in the video

- The reel itself is an HTML page rendered to MP4 by HyperFrames (our engine); the frame counter on the HyperFrames card is the real frame.
- The JSON on the whisper.cpp card is this reel's own word timing (made with a local Whisper model; whisper.cpp's `-ml 1 -oj` gives the same kind of file).
- The FFmpeg card shows this reel's own tracks: voice words, the beat grid, the sound effects.
- ffmpeg-skill: facts from its README; we haven't used it in this video.

---

From the [Explainbrew](https://github.com/explainbrew/prompts) short "Five tools. Zero dollars. A whole motion stack.", Nov 2026. Facts and licences checked Nov 22, 2026. Not affiliated with any of the projects. Voice: AI.
