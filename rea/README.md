# REA — reverse engineering with Claude Code (legally)

[REA](https://github.com/morluto/rea) ("Reverse engineer anything with agents") is an MCP server, an agent skill and a CLI in one npm package. MIT. 400K+ GitHub stars as of Nov 1, 2026.

## Get it only from the official sources

- GitHub: https://github.com/morluto/rea
- Website: https://rea.tools
- npm: `rea-agents`

Unofficial copies of REA exist, and one was reportedly used to spread a trojan. Do not install "REA" from re-uploads, Discord links or prompt packs.

## Setup

```bash
npx rea-agents setup
```

It works with Claude Code, Codex, Cursor, Gemini CLI and others. Analysis runs locally; for native binaries it can drive tools such as Ghidra or Rizin.

## What it is for, and what it refuses

Allowed by its own [DISCLAIMER](https://github.com/morluto/rea/blob/main/DISCLAIMER.md): security and malware research, CTFs and education, interoperability, preservation, and software you own or are authorized to examine.

Refused: bypassing DRM, license checks or anti-cheat, game cheats, copying proprietary code.

It explains behavior and can rebuild **small** functions with evidence. It does not "give you the source code" of an app.

---
From the [Explainbrew](https://github.com/explainbrew/prompts) short on REA, Nov 2026. Not affiliated with the project.
