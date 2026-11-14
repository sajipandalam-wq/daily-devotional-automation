"""
Daily Devotional WhatsApp Status Generator
SS Creative Studio · AI • Art • Anointing

Renders a 1080x1920 WhatsApp status image from the day's devotion,
rotating through 8 colour templates so the feed stays fresh.

Usage:
    python devotion_status.py --title "Peace in the Storm" \
        --verse "Peace I leave with you; my peace I give you." \
        --ref "John 14:27" --message "Your short daily summary here." \
        --day 14
"""
import argparse
import json
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1920
HERE = Path(__file__).parent


def load_templates():
    with open(HERE / "templates.json", encoding="utf-8") as f:
        return json.load(f)


def font(size, bold=False):
    candidates = (
        ["DejaVuSans-Bold.ttf", "arialbd.ttf"] if bold else ["DejaVuSans.ttf", "arial.ttf"]
    )
    for name in candidates:
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def gradient(top, bottom):
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    t, b = [tuple(int(c[i:i + 2], 16) for i in (1, 3, 5)) for c in (top, bottom)]
    for y in range(H):
        r = y / H
        draw.line([(0, y), (W, y)], fill=tuple(int(t[i] + (b[i] - t[i]) * r) for i in range(3)))
    return img


def draw_block(draw, text, y, size, color, bold=False, width=28):
    f = font(size, bold)
    for line in textwrap.wrap(text, width=width):
        w = draw.textlength(line, font=f)
        draw.text(((W - w) / 2, y), line, font=f, fill=color)
        y += int(size * 1.35)
    return y


def render(title, verse, ref, message, day, out):
    templates = load_templates()
    t = templates[(day - 1) % len(templates)]
    img = gradient(t["top"], t["bottom"])
    draw = ImageDraw.Draw(img)

    y = 420
    y = draw_block(draw, "BLESSING TODAY", y, 44, t["accent"], bold=True)
    y += 60
    y = draw_block(draw, title, y, 78, t["text"], bold=True, width=18)
    y += 80
    y = draw_block(draw, f"“{verse}”", y, 54, t["text"], width=26)
    y += 20
    y = draw_block(draw, f"— {ref}", y, 44, t["accent"], bold=True)
    y += 100
    draw_block(draw, message, y, 42, t["text"], width=34)

    draw_block(draw, "SS Creative Studio · AI • Art • Anointing", H - 160, 34, t["accent"], width=60)
    img.save(out, quality=95)
    print(f"Saved {out} using template '{t['name']}'")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--title", required=True)
    p.add_argument("--verse", required=True)
    p.add_argument("--ref", required=True)
    p.add_argument("--message", required=True)
    p.add_argument("--day", type=int, default=1, help="Day of month, picks the template")
    p.add_argument("--out", default="status.jpg")
    a = p.parse_args()
    render(a.title, a.verse, a.ref, a.message, a.day, a.out)
