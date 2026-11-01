# Old PC games in the browser — how it works, and how to tell a clean port

Since autumn 2026, hundreds of unofficial browser ports of 2000s PC games have appeared. They are not streaming and not emulators.

## How it works

1. The game's C++ code is either released by the publisher or recovered by decompiling.
2. [Emscripten](https://emscripten.org) compiles it to **WebAssembly**.
3. The old **Direct3D 8/9** graphics calls are translated to **WebGL2 / WebGPU**.
4. The browser tab runs it. No plugin, no install.

Some coverage says AI made decompiling much faster. That is a journalist's claim, not a verified fact for any specific port.

## Code is not the game

The code may be open, but maps, models, music and textures belong to the publisher. A port that serves the full game to everyone is distributing someone else's files. Take-Two already took one browser version of GTA Vice City down with a DMCA notice (Dec 2025).

## A clean example

**Command & Conquer: Generals – Zero Hour.** EA released the source code under **GPL v3** in February 2025. The browser port [meerzulee/GeneralsXWeb](https://github.com/meerzulee/GeneralsXWeb) (GPL v3, with the MIT-licensed D3D8→WebGL2 layer d8web):

- copies **your own Steam files** into browser storage; "No EA assets are hosted or distributed";
- ~9 MB of WebAssembly (2.7 MB gzipped), ~1.9 GB of game data in the browser;
- first launch takes about a minute; no multiplayer.

## Checklist before you click "play"

- Is the engine code open, and under which license?
- Does it ask for **your own** game files, or ship them?
- Is it from the project's own repo, not a random repack? (Repacks are a common malware route.)

---
From the [Explainbrew](https://github.com/explainbrew/prompts) short "Old PC games in your browser", Nov 2026. Not affiliated with any game publisher.
