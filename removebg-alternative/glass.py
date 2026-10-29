# Transparent glass with BiRefNet-matting (MIT, https://huggingface.co/ZhengPeng7/BiRefNet-matting).
# Usage: python glass.py photo.jpg photo.png
# Install: pip install torch torchvision transformers timm kornia einops opencv-python-headless pillow
# The colour fix (estimate_foreground) follows the official BiRefNet demo, after Photoroom's fast-foreground-estimation.
import sys

import cv2
import numpy as np
import torch
from PIL import Image
from torchvision import transforms
from transformers import AutoModelForImageSegmentation


def blur_fusion(image, fg, bg, alpha, r):
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


src, dst = sys.argv[1], sys.argv[2]
model = AutoModelForImageSegmentation.from_pretrained("ZhengPeng7/BiRefNet-matting", trust_remote_code=True).float().eval()
image = Image.open(src).convert("RGB")
prep = transforms.Compose([
    transforms.Resize((1024, 1024)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
])
with torch.no_grad():
    pred = model(prep(image).unsqueeze(0))[-1].sigmoid()[0, 0]
alpha = transforms.ToPILImage()(pred).resize(image.size)
fg = estimate_foreground(np.asarray(image, np.float32) / 255, np.asarray(alpha, np.float32) / 255)
out = Image.fromarray((fg * 255).astype(np.uint8))
out.putalpha(alpha)
out.save(dst)
print(f"saved {dst}")
