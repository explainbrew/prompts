# ArtCraft: 13 open-source Adobe and Office clones

Notes for the Explainbrew video about **PhotoCraft**, the open-source Photoshop clone from the ArtCraft project. No prompt this time: just the facts, the limits and where to try it.

## Links

- PhotoCraft (Photoshop clone): https://github.com/storytold/photocraft
- All 13 apps: https://getartcraft.com/apps
- Organization: https://github.com/storytold

## The numbers in the video

Checked against GitHub and the PhotoCraft README on 23 and 27 October 2026.

| In the video | Source |
| --- | --- |
| 71,000+ GitHub stars in under a month (71,351 when recorded; repo created 30 Sep) | GitHub API |
| 13 apps: Photo, Pdf, Film, Light, Vector, Effect, Design, Word, Grid, Deck, CAD, Sound, Fig | getartcraft.com/apps |
| Opens and saves real PSD files, with layers and masks | README |
| Re-saved PSDs render the same for 307 of 309 files in the psd-tools test set | README, "Faithful round trips" |
| 500+ commands, also exposed through a CLI and an MCP server, so an AI agent can drive it | README, "Built for agents" |
| "Early alpha… not yet a Photoshop replacement for daily professional work" | README, Status |
| Open source: MIT or Apache-2.0, at your option | README |

## "Built with Claude Opus 5.5"

This comes from press coverage (Ars Technica and outlets quoting it), so the video says "reportedly". The latest commit is signed "Brandon Thomas and claude", but the README does not name the model.

## Try it

PhotoCraft runs on macOS, Windows, Linux and in the browser (WebAssembly). Download builds from the [releases page](https://github.com/storytold/photocraft/releases) or build from source with Rust, as described in the README. It is early alpha: expect rough edges and read the Status section first.

ArtCraft is not affiliated with, sponsored by or endorsed by Adobe Inc.

