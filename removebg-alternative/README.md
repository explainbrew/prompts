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

You need about **1 GB of disk** for the model and **8 GB of RAM** (the model peaked at 6–7 GB in our tests).

**Mac (Apple Silicon or Intel).** rembg supports Python 3.11–3.13, and Homebrew usually installs a newer Python. The easiest way around that is [uv](https://docs.astral.sh/uv/), which fetches the right Python for you:

```bash
brew install uv
uv tool install "rembg[cpu,cli]" --python 3.12
```

**Windows / Linux with Python 3.11–3.13:**

```bash
pip install "rembg[cpu,cli]"          # CPU
pip install "rembg[gpu,cli]"          # NVIDIA GPU (needs CUDA + cuDNN)
```

**Docker (x86-64 only):**

```bash
docker run -v .:/data danielgatis/rembg i -m birefnet-general /data/photo.jpg /data/photo.png
```

The official image has no ARM build, so on an Apple Silicon Mac use `uv` instead.

The first run downloads the model (~930 MB for `birefnet-general`). After that, it works with no internet connection. We checked this with networking switched off.

## Use it

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

Our tests on a MacBook Air M4 (16 GB), CPU only, photos 1600 px wide:

| Setup | Time per photo |
| --- | --- |
| Native macOS (`uv`), `birefnet-general` | ~9 s |
| Docker on the same Mac, `birefnet-general` | 13–16 s |
| Docker, `birefnet-general -vm -dc` (hair/fur) | 22–32 s |

The first photo after start-up also includes ~3 s to load the model. An NVIDIA GPU is much faster.

Apple's CoreML acceleration isn't worth it here: rembg doesn't turn it on by default, and when we forced it, compiling the model for the Neural Engine was still running after 30 minutes.

## What it's good at, and what it isn't

We ran ten hard photos through it: curly hair, fur, wine glasses and perfume bottles.

- **Hair:** excellent. Single curls survive.
- **Fur:** good with `-vm -dc`. Without it, white fur kept a light outline from the grass behind it.
- **Glass and other transparent objects:** every rembg model we tried (`birefnet-general`, `-lite`, `massive`, `hrsod`, `dis`, `bria-rmbg`, with `-a` and with `-vm`) cuts the shape fine but keeps the old background *inside* the glass. Glass comes out opaque.

## Glass: use BiRefNet-matting

[BiRefNet-matting](https://huggingface.co/ZhengPeng7/BiRefNet-matting) is from the same authors as the BiRefNet model inside rembg, also MIT-licensed. It isn't part of rembg, but it predicts real transparency, so wine glasses and clear perfume bottles come out see-through.

It runs with PyTorch, so it needs its own install (~1.2 GB) and is slower: about 50 s a photo on CPU in our tests.

```bash
uv venv --python 3.12 glass-env && source glass-env/bin/activate     # or: python -m venv glass-env
uv pip install torch torchvision transformers timm kornia einops opencv-python-headless pillow
python glass.py wineglass.jpg wineglass.png
```

[`glass.py`](glass.py) is in this folder. The first run downloads the model (~880 MB) from Hugging Face. It loads the model's own code from the author's repo (`trust_remote_code`), the same way the official demo does.

What we saw: a wine glass on a grey gradient and a clear bottle on white fur came out properly transparent. A bottle on a black, wet surface came out blurry, and there rembg's opaque cut looked better. Try both.

**Glass shot on pure black:** you don't even need AI. Use brightness as transparency, the classic studio trick: black becomes transparent, highlights stay. With ffmpeg:

```bash
ffmpeg -i glass.jpg -vf "format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='min(255,max(r(X,Y),max(g(X,Y),b(X,Y)))*3)'" glass.png
```

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
- **About 9 seconds a photo on a MacBook Air:** our native test, MacBook Air M4, CPU.
- **Default model is non-commercial:** [BRIA RMBG-2.0 model card](https://huggingface.co/briaai/RMBG-2.0) and rembg's README.
- **Speed, memory, offline:** our own tests above, rembg 2.0.86, onnxruntime 1.31.1.
- **Glass turns see-through with BiRefNet-matting:** our test, model `ZhengPeng7/BiRefNet-matting` (MIT), PyTorch on CPU.

Test photos from [Unsplash](https://unsplash.com) (Unsplash License): ALMA, amin naderloei, Alexander Naglestad, Honza Vojtek, Michael Oeser, Jessica Weiller, Lana Graves, Kier in Sight Archives, Siora Photography.

---

How we make these videos: the voiceover is made with [ElevenLabs](https://try.elevenlabs.io/s3p4rzmexcmc) (affiliate link: we get a commission if you subscribe, at no extra cost to you).

From the Explainbrew video about remove.bg alternatives. We're not affiliated with remove.bg, Canva, rembg or BiRefNet. Check each model's license before you use it commercially.
