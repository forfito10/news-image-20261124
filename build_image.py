#!/usr/bin/env python3
"""Build the 24 Nov 2026 world-news poster: 1024x1024 PNG, <1 MiB.
All facts verified from Reuters / UN News / AP / The Times / Chess.com on 24 Nov 2026.
No network, no randomness: same bytes every run (PIL writes deterministic PNG)."""
from PIL import Image, ImageDraw, ImageFont
import os

W = H = 1024
BG = (13, 27, 42)
CARD = (22, 40, 63)
BORDER = (42, 63, 92)
WHITE = (255, 255, 255)
SUMMARY = (199, 211, 224)
MUTED = (148, 163, 184)

def font(name, size):
    for p in (f"/usr/share/fonts/truetype/noto/NotoSans-{name}.ttf",
              f"/usr/share/fonts/truetype/dejavu/DejaVuSans-{name}.ttf"):
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

F_TITLE = font("Bold", 66)
F_SUB = font("Regular", 27)
F_KICK = font("Bold", 21)
F_HEAD = font("Bold", 30)
F_BODY = font("Regular", 22)
F_FOOT = font("Regular", 18)

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_icon(d, kind, cx, cy, r, color):
    """Simple geometric icons, drawn with PIL primitives."""
    if kind == "bars":  # markets: ascending bars
        bw, gap = 10, 7
        hs = [16, 28, 42]
        x0 = cx - (3 * bw + 2 * gap) // 2
        for i, h in enumerate(hs):
            x = x0 + i * (bw + gap)
            d.rectangle([x, cy + 22 - h, x + bw, cy + 22], fill=color)
        d.line([cx - 30, cy + 26, cx + 30, cy + 26], fill=color, width=3)
    elif kind == "globe":  # climate: circle + latitude lines
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=color, width=4)
        d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=color, width=3)
        d.arc([cx - r, cy - r, cx + r, cy + r], 20, 160, fill=color, width=3)
        d.line([cx - r, cy, cx + r, cy], fill=color, width=3)
    elif kind == "flame":  # disaster: flame teardrop
        d.polygon([(cx, cy - 30), (cx + 20, cy + 2), (cx + 12, cy + 22),
                   (cx - 12, cy + 22), (cx - 20, cy + 2)], fill=color)
        d.polygon([(cx, cy + 4), (cx + 8, cy + 18), (cx - 8, cy + 18)], fill=BG)
    elif kind == "warn":  # war: triangle + exclamation
        d.polygon([(cx, cy - 28), (cx + 28, cy + 22), (cx - 28, cy + 22)],
                  outline=color, width=4)
        d.rectangle([cx - 3, cy - 12, cx + 3, cy + 6], fill=color)
        d.ellipse([cx - 3, cy + 12, cx + 3, cy + 18], fill=color)
    elif kind == "drop":  # middle east: oil drop
        d.polygon([(cx, cy - 30), (cx + 18, cy + 2), (cx - 18, cy + 2)], fill=color)
        d.ellipse([cx - 18, cy - 6, cx + 18, cy + 26], fill=color)
    elif kind == "crown":  # chess: crown
        d.polygon([(cx - 26, cy + 20), (cx - 26, cy - 6), (cx - 12, cy + 8),
                   (cx, cy - 18), (cx + 12, cy + 8), (cx + 26, cy - 6),
                   (cx + 26, cy + 20)], fill=color)
        d.rectangle([cx - 26, cy + 24, cx + 26, cy + 30], fill=color)

STORIES = [
    ("bars", (46, 204, 113), "MARKETS  ·  UNITED STATES",
     "Nvidia's chief is back",
     "Jensen Huang returns as CEO 11 days after resigning. Shares jump 31%."),
    ("globe", (26, 188, 156), "CLIMATE  ·  ANTALYA, TÜRKIYE",
     "COP31 collapses",
     "UN climate talks end with no deal — the longest COP ever — split over fossil fuels."),
    ("flame", (230, 126, 34), "DISASTER  ·  INDONESIA",
     "Factory fire kills 24",
     "A candy factory blaze in Banten leaves 24 confirmed dead and about 30 workers still missing."),
    ("warn", (231, 76, 60), "WAR  ·  UKRAINE",
     "Strikes at sea and near Kyiv",
     "Ukraine sinks a Russian warship off Libya; Russian strikes near Kyiv kill at least 14."),
    ("drop", (241, 196, 15), "MIDDLE EAST  ·  IRAN",
     "Hormuz showdown",
     "Trump dares Iran to test the US naval blockade; Tehran vows to break it."),
    ("crown", (243, 156, 18), "SPORT  ·  GENEVA",
     "Chess crown on the line",
     "Game 1 begins: Gukesh, 20, defends against Sindarov, 20 — the youngest final ever."),
]

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# header
d.text((36, 34), "THE WORLD IN ONE PICTURE", font=F_KICK, fill=(255, 214, 64))
d.text((36, 62), "24 November 2026", font=F_TITLE, fill=WHITE)
d.text((36, 140), "Tuesday  ·  Six stories that defined the day", font=F_SUB, fill=MUTED)
d.line([36, 182, W - 36, 182], fill=BORDER, width=2)

# grid of story cards
mx, my, gap = 36, 202, 20
cw = (W - 2 * mx - gap) // 2
ch = 236
for i, (icon, color, kick, head, body) in enumerate(STORIES):
    x = mx + (i % 2) * (cw + gap)
    y = my + (i // 2) * (ch + gap)
    d.rounded_rectangle([x, y, x + cw, y + ch], radius=18, fill=CARD, outline=BORDER, width=2)
    d.line([x + 18, y + 18, x + 18, y + ch - 18], fill=color, width=5)
    draw_icon(d, icon, x + 66, y + 56, 30, color)
    tx = x + 108
    d.text((tx, y + 22), kick, font=F_KICK, fill=color)
    hl = wrap(d, head, F_HEAD, cw - 126)
    yy = y + 52
    for ln in hl[:2]:
        d.text((tx, yy), ln, font=F_HEAD, fill=WHITE)
        yy += 36
    bl = wrap(d, body, F_BODY, cw - 126)
    yy = y + 128
    for ln in bl[:3]:
        d.text((tx, yy), ln, font=F_BODY, fill=SUMMARY)
        yy += 27

# footer
d.line([36, 968, W - 36, 968], fill=BORDER, width=2)
d.text((36, 980), "Sources: Reuters  ·  UN News  ·  AP  ·  The Times  ·  Chess.com  —  verified 24 Nov 2026",
       font=F_FOOT, fill=MUTED)

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
img.save(out, format="PNG", optimize=True)
print("wrote", out, os.path.getsize(out), "bytes,", img.size)
