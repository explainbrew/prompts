# gpu-unlock — why your GeForce does some AI math at half speed

**This page is an explainer, not a how-to. We did not run it, and we don't recommend it on a card you can't afford to lose.** Facts as of Nov 1, 2026.

## The limit is in NVIDIA's own whitepapers

FP16 tensor throughput, dense (TFLOPS):

| Card | FP16 accumulate | FP32 accumulate |
| --- | --- | --- |
| RTX 4090 (Ada) | 330.3 | 165.2 |
| RTX 3090 (Ampere GA102) | 142 | 71 |
| RTX A6000 (same GA102 chip, workstation) | 154.8 | 154.8 |

Sources: NVIDIA Ada Lovelace architecture whitepaper v2.02; NVIDIA Ampere GA102 whitepaper.

## What gpu-unlock is

[Zagitta/gpu-unlock](https://github.com/Zagitta/gpu-unlock) is a Linux kernel module (GPL-2.0-only per its README; NVIDIA firmware stays under NVIDIA's terms). It lifts the limit until the next power-off. No VBIOS flash.

## Real-world effect

"2×" is the peak instruction rate. One RTX 4090 owner measured **+12–34%** on real FP16 work; nothing changes for chatting with an LLM, quantized models or games.

## Risks

- Secure Boot must be off.
- Most cards are experimental (tested on one or a few cards).
- If the GPU firmware hangs, the card is stuck until a full power-off.
- NVIDIA's driver license (§2.6) forbids circumventing "any technical limitation".
- The author warns about fake Windows installers. Malware "unlockers" have happened before.

---
From the [Explainbrew](https://github.com/explainbrew/prompts) short on gpu-unlock, Nov 2026. Not affiliated with NVIDIA or the project.
