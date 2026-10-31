# Prompt: let your AI agent set up rembg for you (and clean up after)

Paste the prompt below into **Claude Code**, **Codex** or **Gemini CLI** (any agent that can run terminal commands). It installs rembg in an isolated way, tells you exactly what it will install **before** it does, keeps a log of everything, and offers to remove all of it at the end.

Prefer doing it by hand? Everything is in [README.md](README.md).

---

```text
I want to remove photo backgrounds on my own computer with rembg (https://github.com/danielgatis/rembg) and the MIT-licensed BiRefNet model. Set it up for me, following these rules strictly.

RULES
1. Ask before installing. First, check my system (OS, CPU/GPU, free disk space, RAM, whether python3 / uv / brew / pip already exist) WITHOUT installing anything. Then show me a plan: every tool you will install, where it goes, how much disk it takes, and what will be downloaded from the internet. Wait for my "yes" before running any install command.
2. Keep everything isolated. Do not use sudo. Do not install into the system Python or change my shell config (.zshrc, .bashrc, PATH) unless I agree. Put everything you can in one folder: ~/rembg-setup/
   - rembg models: set REMBG_HOME=~/rembg-setup/rembg (pass it as an environment variable when running rembg)
   - Hugging Face cache (glass model only): HF_HOME=~/rembg-setup/hf
3. Log everything. Create ~/rembg-setup/INSTALLED.md and append one line for each thing you install or download: what it is, the exact path, the size, and the exact command that removes it. Mark anything that was already on my system before you started as "pre-existing, do not remove".
4. Install rembg the isolated way:
   - macOS or Linux: use uv (install uv only if it's missing and I agree), then: uv tool install "rembg[cpu,cli]" --python 3.12
     (rembg needs Python 3.11–3.13; uv downloads its own Python 3.12, it does not touch the system one)
   - Windows: use uv the same way, or a venv in ~/rembg-setup/venv with Python 3.11–3.13.
   - NVIDIA GPU: offer "rembg[gpu,cli]" instead and explain it needs CUDA + cuDNN.
5. Always use an MIT model. rembg's default model (bria-rmbg) is non-commercial (CC BY-NC 4.0). Always pass -m birefnet-general. Tell me this once.
6. Test it. Run rembg on one of my photos (ask me for a path, or create a small test image), and tell me how long it took and where the output is. The first run downloads the model (~930 MB).
7. Show me how to use it, with REMBG_HOME set:
   - one photo:         rembg i -m birefnet-general in.jpg out.png
   - hair / fur edges:  rembg i -m birefnet-general -vm -dc in.jpg out.png   (slower, cleaner edges; downloads a small ViTMatte model)
   - a whole folder:    rembg p -m birefnet-general ./photos ./cutouts
   - watch a folder:    rembg p -w -m birefnet-general ./inbox ./cutouts
8. Glass / transparent products (OPTIONAL; ask me first, it's a bigger install, ~1.2 GB of PyTorch + ~880 MB model, about 13 s per photo on a laptop CPU after the first run):
   - create a venv at ~/rembg-setup/glass-env with Python 3.12 (via uv)
   - install: torch torchvision transformers timm kornia einops opencv-python-headless pillow
   - download glass.py from https://github.com/explainbrew/prompts/tree/main/glass-cutout into ~/rembg-setup/ and read it to me in one paragraph before running it (it loads the model's code from Hugging Face with trust_remote_code, the same way the official BiRefNet demo does)
   - run: HF_HOME=~/rembg-setup/hf ~/rembg-setup/glass-env/bin/python ~/rembg-setup/glass.py in.jpg   (on Windows: glass-env\Scripts\python.exe; output is in.png next to the photo)
9. Cleanup. When we're done (or whenever I say "clean up"), show me the list from INSTALLED.md and ask: remove everything you installed, keep it, or remove only some items? Then remove ONLY what you installed (never the pre-existing items), confirm each removal, and finally delete ~/rembg-setup/ itself (warn me first if my output photos are inside it, and offer to move them out).
   Typical removal commands (use the ones that match what you actually installed):
   - uv tool uninstall rembg
   - uv python uninstall 3.12        (only if you downloaded it)
   - brew uninstall uv               (only if you installed uv with brew)
   - rm -rf ~/rembg-setup
   - also check ~/.rembg and ~/.u2net: if a model was downloaded there by mistake, remove it too (only if it did not exist before)
10. Be honest about limits: glass comes out opaque with rembg models (that's what step 8 is for), the default model is non-commercial, and on CPU a single rembg command takes ~25 s (mostly loading the model), a folder ~19 s per photo.

Start with step 1 now: check my system and show me the plan.
```

---

## What to expect

| | |
| --- | --- |
| Disk | ~1 GB for rembg + model; +~2 GB if you add the glass setup |
| RAM | 8 GB recommended (peak memory was 7–9 GB in our tests) |
| Time (MacBook Air M4, CPU) | ~25 s per rembg command · ~19 s/photo in a folder · ~13 s/photo glass model |
| Internet | only for installing and the first model download; then it works offline |

Your photos never leave your computer. The agent itself (Claude, ChatGPT, Gemini) does see the commands and file names it works with, so don't point it at folders with private documents.

From the Explainbrew video about remove.bg alternatives. Not affiliated with rembg, BiRefNet or remove.bg.

**Use at your own risk:** provided as is, with no warranty. See the [disclaimer](../README.md#disclaimer-use-at-your-own-risk).
