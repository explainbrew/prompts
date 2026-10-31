# /// script
# requires-python = ">=3.10,<3.14"
# dependencies = [
#     "torch", "torchvision", "transformers", "timm", "kornia", "einops",
#     "opencv-python-headless", "pillow", "numpy",
# ]
# ///
# Cut out glass and other see-through objects, keeping them transparent.
# Easiest way to run it on Mac, Windows or Linux: `uv run glass.py photo.jpg` (uv installs everything listed above).
#
#   python glass.py photo.jpg                    -> photo.png next to it
#   python glass.py photos/ -o cutouts/           -> every jpg/png/webp in the folder
#   python glass.py photo.jpg --black             -> glass shot on pure black: no AI, brightness = transparency
#   python glass.py photo.jpg --model hr          -> high-res matting (finer edges, needs ~11 GB RAM)
#   python glass.py photo.jpg --model general     -> plain BiRefNet cut-out (solid objects)
#
# Models: BiRefNet by Peng Zheng et al., MIT (https://github.com/ZhengPeng7/BiRefNet).
# Install: pip install torch torchvision transformers timm kornia einops opencv-python-headless pillow
# The colour fix (estimate_foreground) follows the official BiRefNet demo, after Photoroom's fast-foreground-estimation.
import argparse
import sys
import time
from pathlib import Path

import numpy as np
from PIL import Image

MODELS = {
    "matting": ("ZhengPeng7/BiRefNet-matting", 1024),
    "hr": ("ZhengPeng7/BiRefNet_HR-matting", 2048),
    "general": ("ZhengPeng7/BiRefNet", 1024),
}
EXTS = {".jpg", ".jpeg", ".png", ".webp"}


def blur_fusion(image, fg, bg, alpha, r):
    import cv2

    blurred_alpha = cv2.blur(alpha, (r, r))[:, :, None]
    blurred_fg = cv2.blur(fg * alpha, (r, r)) / (blurred_alpha + 1e-5)
    blurred_bg = cv2.blur(bg * (1 - alpha), (r, r)) / ((1 - blurred_alpha) + 1e-5)
    fg = blurred_fg + alpha * (image - alpha * blurred_fg - (1 - alpha) * blurred_bg)
    return np.clip(fg, 0, 1), blurred_bg


def estimate_foreground(image, alpha):
    """Removes the old background's colour from see-through and soft pixels."""
    a = alpha[:, :, None]
    fg, bg = blur_fusion(image, image, image, a, 90)
    return blur_fusion(image, fg, bg, a, 6)[0]


def black_key(image, floor):
    """Glass on pure black: brightness becomes transparency, highlights stay white."""
    rgb = np.asarray(image, np.float32)
    mx = rgb.max(axis=2)
    alpha = np.clip((mx - floor) * 3, 0, 255)
    colour = np.clip(rgb * 255 / np.maximum(mx, 1)[..., None], 0, 255)
    return Image.fromarray(np.dstack([colour, alpha]).astype(np.uint8), "RGBA")


def load_model(name):
    import torch
    from transformers import AutoModelForImageSegmentation

    repo, res = MODELS[name]
    if torch.cuda.is_available():
        device = "cuda"
    elif torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"
    model = AutoModelForImageSegmentation.from_pretrained(repo, trust_remote_code=True).float().eval().to(device)
    return model, res, device


def ai_cutout(model, res, device, image, clean):
    import torch
    from torchvision import transforms

    prep = transforms.Compose([
        transforms.Resize((res, res)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])
    with torch.no_grad():
        pred = model(prep(image).unsqueeze(0).to(device))[-1].sigmoid()[0, 0].cpu()
    alpha = np.asarray(transforms.ToPILImage()(pred).resize(image.size), np.float32) / 255
    # tiny non-zero alpha in the background shows up as grey smudges on a new background
    alpha = np.clip((alpha - clean) / (1 - clean), 0, 1)
    fg = estimate_foreground(np.asarray(image, np.float32) / 255, alpha)
    out = Image.fromarray((fg * 255).astype(np.uint8))
    out.putalpha(Image.fromarray((alpha * 255).astype(np.uint8)))
    return out


def main():
    ap = argparse.ArgumentParser(description="Cut out glass and keep it see-through.")
    ap.add_argument("input", help="a photo or a folder of photos")
    ap.add_argument("-o", "--out", help="output file or folder (default: next to the input, as .png)")
    ap.add_argument("--model", choices=MODELS, default="matting", help="matting (default), hr, general")
    ap.add_argument("--black", action="store_true", help="glass on pure black: no AI, brightness trick")
    ap.add_argument("--floor", type=float, default=20, help="--black: brightness treated as background (0-255)")
    ap.add_argument("--clean", type=float, default=0.10, help="AI: alpha below this becomes fully transparent")
    args = ap.parse_args()

    src = Path(args.input)
    files = sorted(p for p in src.iterdir() if p.suffix.lower() in EXTS) if src.is_dir() else [src]
    if not files:
        sys.exit(f"no photos found in {src}")
    out_dir = Path(args.out) if args.out and (src.is_dir() or Path(args.out).suffix == "") else None
    if out_dir:
        out_dir.mkdir(parents=True, exist_ok=True)

    model = None
    if not args.black:
        t = time.perf_counter()
        model, res, device = load_model(args.model)
        print(f"model {args.model} on {device} loaded in {time.perf_counter() - t:.1f}s")

    for f in files:
        t = time.perf_counter()
        image = Image.open(f).convert("RGB")
        out = black_key(image, args.floor) if args.black else ai_cutout(model, res, device, image, args.clean)
        dst = out_dir / (f.stem + ".png") if out_dir else Path(args.out) if args.out else f.with_suffix(".png")
        if dst.resolve() == f.resolve():
            dst = f.with_name(f.stem + "-cutout.png")
        out.save(dst)
        print(f"saved {dst}  ({time.perf_counter() - t:.1f}s)")


if __name__ == "__main__":
    main()
