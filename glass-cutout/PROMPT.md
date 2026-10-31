# Prompt: let your AI agent set up the glass cut-out tool (and clean up after)

Paste this into **Claude Code**, **Codex** or **Gemini CLI**. Prefer doing it by hand? See [README.md](README.md).

```text
I want to cut out glass products (bottles, wine glasses, clear plastic) from photos and keep them see-through, on my own computer, using glass.py from https://github.com/explainbrew/prompts/tree/main/glass-cutout (it runs BiRefNet-matting, MIT). Set it up following these rules strictly.

1. Ask before installing. First check my system (OS, CPU/GPU, free disk, RAM, python3 / uv availability) WITHOUT installing anything. Then show me a plan: what you will install, where, how much disk (PyTorch ~1.2 GB + model ~880 MB), and what gets downloaded. Wait for my "yes".
2. Keep everything in one folder: ~/glass-setup/. No sudo, no system Python, no shell-config changes unless I agree.
   - venv: ~/glass-setup/env (Python 3.10–3.13; use uv to fetch 3.12 if my python3 is newer)
   - Hugging Face cache: HF_HOME=~/glass-setup/hf (pass it as an env var when running)
3. Log everything you install or download in ~/glass-setup/INSTALLED.md: what, path, size, and the exact command that removes it. Mark anything that existed before as "pre-existing, do not remove".
4. Install: easiest is uv (glass.py lists its packages at the top, so `uv run glass.py photo.jpg` installs them; on Windows with an NVIDIA GPU use a venv and the CUDA command from pytorch.org instead). Without uv: pip install torch torchvision transformers timm kornia einops opencv-python-headless pillow
5. Download glass.py into ~/glass-setup/ and explain it to me in one paragraph before running it (it loads the model's code from Hugging Face with trust_remote_code, like the official BiRefNet demo).
6. Test it on one of my photos (ask for a path) and tell me how long it took, which device it used (CUDA / Apple MPS / CPU), and where the output is. Show it on a coloured background if you can, so I can see the glass is see-through.
7. Show me the useful commands: a folder (python glass.py photos/ -o cutouts/), glass on pure black (--black), solid objects (--model general).
8. Cleanup: when we're done or when I say "clean up", show INSTALLED.md and ask what to remove. Remove ONLY what you installed, confirm each step, then delete ~/glass-setup/ (warn me first if my photos are inside and offer to move them out).
9. Be honest about limits: it needs ~9 GB RAM, solid tinted bottles can look washed out (use --model general), and dark wet surfaces come out smeared.

Start with step 1 now.
```

Your photos never leave your computer. The agent itself sees the commands and file names it works with, so don't point it at folders with private documents.

**Use at your own risk:** provided as is, with no warranty. See the [disclaimer](../README.md#disclaimer-use-at-your-own-risk).
