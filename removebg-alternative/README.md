# remove.bg is shutting down: remove backgrounds on your own computer with rembg

On **December 1, 2026 at 9:00 CET**, remove.bg's standalone website stops working. The self-service API, the Photoshop plugin, the desktop app and the other integrations go with it. Unused pay-as-you-go credits expire on the same day ([remove.bg FAQ](https://www.remove.bg/faq)). The official replacement is Canva, and the API is moving to Leonardo.ai.

If you'd rather not upload your photos anywhere, [rembg](https://github.com/danielgatis/rembg) by Daniel Gatis does the same job on your own machine. It's free, MIT-licensed, has 25,000+ GitHub stars, and works offline once the model is downloaded.

- Repo: https://github.com/danielgatis/rembg (MIT)
- Model we use: [BiRefNet](https://github.com/ZhengPeng7/BiRefNet) by Peng Zheng et al. (MIT)

> 🤖 **Don't want to do it by hand?** Paste [PROMPT.md](PROMPT.md) into Claude Code, Codex or Gemini CLI. The agent tells you what it will install before it does, sets everything up in one folder, and removes it all when you're done.

> 🎙️ The voiceover in our video is made with [ElevenLabs](https://try.elevenlabs.io/s3p4rzmexcmc). Affiliate link: we earn a commission if you subscribe, at no extra cost to you.

## ⚠️ Read this first: the default model is non-commercial

If you run `rembg` without `-m`, it uses **`bria-rmbg`** (RMBG-2.0 by BRIA AI). Its weights are licensed **CC BY-NC 4.0**: commercial use needs a paid agreement with BRIA ([model card](https://huggingface.co/briaai/RMBG-2.0)). rembg's own README says it too: model weights have their own licenses, separate from rembg's MIT license.

For client work, products or anything you sell, pick a model yourself:

```bash
rembg i -m birefnet-general photo.jpg photo.png
```

`birefnet-general` is BiRefNet, MIT-licensed. That's the model in every example below.

## Install

You need about **1 GB of disk** for the model and **8 GB of RAM** (peak memory was 7–9 GB in our tests).

> ✅ **macOS:** tested by us on a MacBook Air M4.
> 📄 **Windows and Linux:** not tested by us. These commands are taken from the official documentation: [uv installation](https://docs.astral.sh/uv/getting-started/installation/), [rembg README](https://github.com/danielgatis/rembg#installation), [onnxruntime CUDA requirements](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html#requirements).

rembg needs Python 3.11–3.13, and your system may have a different one. The easy way on every system is [uv](https://docs.astral.sh/uv/): a small tool that downloads the right Python just for rembg and doesn't touch anything else. Two steps.

**Step 1. Install uv** (skip it if `uv --version` already works):

| System | Command |
| --- | --- |
| macOS | `brew install uv` (no Homebrew? use the Linux command) |
| Linux (from the uv docs) | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Windows, PowerShell (from the uv docs) | `winget install --id=astral-sh.uv -e` or `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 \| iex"` |

Then **close the terminal and open a new one**.

**Step 2. Install rembg** (the same command on macOS, Windows and Linux):

```bash
uv tool install "rembg[cpu,cli]" --python 3.12
```

Check it with `rembg --help`. If you see `command not found` (on Windows: `is not recognized`), run `uv tool update-shell` and open a new terminal.

**NVIDIA graphics card (Windows / Linux)?** Install the GPU build instead, it's much faster. It also needs NVIDIA's CUDA and cuDNN, in the versions listed on [onnxruntime's CUDA page](https://onnxruntime.ai/docs/execution-providers/CUDA-ExecutionProvider.html#requirements):

```bash
uv tool install "rembg[gpu,cli]" --python 3.12
```

**Already have Python 3.11–3.13 and prefer pip?** `pip install "rembg[cpu,cli]"` works too, ideally inside a virtual environment.

**Docker (x86-64 only):**

```bash
docker run -v .:/data danielgatis/rembg i -m birefnet-general /data/photo.jpg /data/photo.png
```

The official image has no ARM build, so on an Apple Silicon Mac use `uv` instead.

The first run downloads the model (~930 MB for `birefnet-general`). After that, it works with no internet connection. We checked this with networking switched off.

**Remove it later:** `uv tool uninstall rembg`, then delete the model folder `.rembg` (or the older `.u2net`) in your home folder.


## Use it

The commands are the same on macOS, Windows and Linux. Run them in the folder with your photos (`cd` into it first), or use full paths.

**One photo:**

```bash
rembg i -m birefnet-general photo.jpg photo.png
```

**Hair and fur: add `-vm -dc`.** Without it, fluffy edges can keep a thin halo of the old background. `-vm` refines the edge with a second model (ViTMatte), and `-dc` removes the leftover background colour. It takes about twice as long.

```bash
rembg i -m birefnet-general -vm -dc dog.jpg dog.png
```

**A whole folder:**

```bash
rembg p -m birefnet-general ./photos ./cutouts
```

**Watch a folder** (new photos get processed as soon as they land):

```bash
rembg p -w -m birefnet-general ./inbox ./cutouts
```

**Replace the background with a colour** instead of transparency (R G B A):

```bash
rembg i -m birefnet-general --bgcolor 255 255 255 255 product.jpg product-white.png
```

**From Python:**

```python
from rembg import new_session, remove

session = new_session("birefnet-general")
with open("photo.jpg", "rb") as f:
    out = remove(f.read(), session=session)
with open("photo.png", "wb") as f:
    f.write(out)
```

## How fast is it?

Our tests on a MacBook Air M4 (16 GB), CPU only, photos 1600 px wide, native macOS (`uv`):

| What you run | Time |
| --- | --- |
| `rembg i -m birefnet-general` (one photo, model already downloaded) | ~25 s per command |
| …the very first run (downloads the 973 MB model) | ~1 min 45 s |
| `rembg p` on a folder (model loads once) | ~19 s per photo |
| `-vm -dc` (hair/fur) | ~17–25 s per command |
| `glass.py` (model already downloaded) | ~13 s per photo |
| …its first run (downloads ~880 MB) | ~70 s |

Most of a single command is loading the model, so for many photos use a folder (`rembg p`). Peak memory was 7–9 GB. An NVIDIA GPU is much faster, and you can rent one by the hour if you don't have one. Docker on the same Mac was several times slower, so on a Mac run it natively.

Apple's CoreML acceleration isn't worth it here: rembg doesn't turn it on by default, and when we forced it, compiling the model for the Neural Engine was still running after 30 minutes.

## What it's good at, and what it isn't

We ran ten hard photos through it: curly hair, fur, wine glasses and perfume bottles.

- **Hair:** excellent. Single curls survive.
- **Fur:** good with `-vm -dc`. Without it, white fur kept a light outline from the grass behind it.
- **Glass and other transparent objects:** every rembg model we tried (`birefnet-general`, `-lite`, `massive`, `hrsod`, `dis`, `bria-rmbg`, with `-a` and with `-vm`) cuts the shape fine but keeps the old background *inside* the glass. Glass comes out opaque.

## Glass: use BiRefNet-matting → [glass-cutout](../glass-cutout/)

[BiRefNet-matting](https://huggingface.co/ZhengPeng7/BiRefNet-matting) (same authors as the BiRefNet model inside rembg, MIT) keeps glass see-through. It isn't part of rembg, so it has its own page with an upgraded script: **[glass-cutout](../glass-cutout/)**. It handles whole folders, uses your GPU automatically (NVIDIA or Apple Silicon: ~6 s a photo on a MacBook Air M4), and has a `--black` mode for glass shot on pure black (the brightness trick, no AI).

The [`glass.py`](glass.py) in this folder is the original single-photo version from the video and still works.

## Other models in rembg

| Model | Use it for | License of the weights |
| --- | --- | --- |
| `birefnet-general` | everything, our default | MIT |
| `birefnet-general-lite` | weaker machines (214 MB) | MIT |
| `birefnet-portrait` | people | MIT |
| `bria-rmbg` | the default if you pass no `-m` | **CC BY-NC 4.0, non-commercial** |
| `withoutbg`, `atlascloud` | not local: they upload your photo to a cloud API | their own terms |

## The numbers in the video

- **December 1, 2026, 9:00 CET; credits expire:** [remove.bg FAQ](https://www.remove.bg/faq), checked October 29, 2026.
- **25,000+ stars, MIT:** GitHub API, October 29, 2026 (25,222 stars).
- **About 25 seconds per command, closer to 20 a photo in a folder:** our native test, MacBook Air M4, CPU.
- **Default model is non-commercial:** [BRIA RMBG-2.0 model card](https://huggingface.co/briaai/RMBG-2.0) and rembg's README.
- **Speed, memory, offline:** our own tests above, rembg 2.0.86, onnxruntime 1.31.1.
- **Glass turns see-through with BiRefNet-matting:** our test, model `ZhengPeng7/BiRefNet-matting` (MIT), PyTorch on CPU.

Test photos from [Unsplash](https://unsplash.com) (Unsplash License): ALMA, amin naderloei, Alexander Naglestad, Honza Vojtek, Michael Oeser, Jessica Weiller, Lana Graves, Kier in Sight Archives, Siora Photography.

---

How we make these videos: the voiceover is made with [ElevenLabs](https://try.elevenlabs.io/s3p4rzmexcmc) (affiliate link: we get a commission if you subscribe, at no extra cost to you).

From the Explainbrew video about remove.bg alternatives. We're not affiliated with remove.bg, Canva, rembg or BiRefNet. Check each model's license before you use it commercially.

**Use at your own risk:** provided as is, with no warranty. See the [disclaimer](../README.md#disclaimer-use-at-your-own-risk).
