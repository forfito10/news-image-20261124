import os
import sys, shutil
try:
    from PIL import Image, ImageDraw, ImageFont
except Exception:
    _out = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
    os.makedirs(os.path.dirname(_out) or ".", exist_ok=True)
    shutil.copyfile(os.path.join(os.environ.get("MAKEFUN_BOT_DIR", "/bot"), "entry.png"), _out)
    sys.exit(0)

W = H = 1024
NAVY = "#0e1a2b"; TEAL = "#2dd4bf"; CREAM = "#f3ede0"; GRAY = "#aab5c1"; INK = "#17263a"
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
os.makedirs("/output", exist_ok=True)
im = Image.new("RGB", (W, H), NAVY)
d = ImageDraw.Draw(im)
fd = "/usr/share/fonts/truetype/dejavu"
def f(size, heavy=False):
    try: return ImageFont.truetype(os.path.join(fd, "DejaVuSans-Bold.ttf" if heavy else "DejaVuSans.ttf"), size)
    except OSError: return ImageFont.load_default()
def text(x, y, v, s, c, heavy=False): d.text((x, y), v, font=f(s, heavy), fill=c)
def badge(cx, cy, kind, color):
    r = 39
    d.ellipse((cx-r, cy-r, cx+r, cy+r), fill="#203b52")
    if kind == "chip":
        d.rounded_rectangle((cx-19, cy-19, cx+19, cy+19), radius=5, outline=color, width=3)
        d.rectangle((cx-8, cy-8, cx+8, cy+8), outline=color, width=2)
        for n in (-12, 0, 12):
            d.line((cx-25, cy+n, cx-19, cy+n), fill=color, width=3)
            d.line((cx+19, cy+n, cx+25, cy+n), fill=color, width=3)
    elif kind == "chart":
        d.line((cx-22, cy+19, cx-22, cy-20), fill=color, width=3)
        d.line((cx-22, cy+19, cx+23, cy+19), fill=color, width=3)
        d.line((cx-16, cy+9, cx-4, cy-2, cx+6, cy+5, cx+19, cy-13), fill=color, width=4, joint="curve")
    elif kind == "flag":
        d.line((cx-16, cy+23, cx-16, cy-23), fill=color, width=4)
        d.polygon(((cx-13,cy-20),(cx+21,cy-13),(cx+5,cy+1),(cx-13,cy-4)), outline=color)
        d.line((cx-13, cy-20, cx+21, cy-13, cx+5, cy+1, cx-13, cy-4), fill=color, width=3)
    else:
        for off in (-10, 2, 14):
            d.arc((cx-24, cy+off-9, cx+24, cy+off+9), 200, 340, fill=color, width=3)

text(46, 26, "THE WORLD / DAILY BRIEF", 17, TEAL, True)
text(747, 28, "NO. 328  •  GLOBAL", 15, "#d5dde5", True)
text(46, 65, "Tuesday 24 November 2026", 49, "#ffffff", True)
text(48, 130, "Nine stories moving the world today", 20, GRAY)
cards = [
    (46, 184, "#ef6461", "TECH · SANTA CLARA", ["Huang is back as", "Nvidia's chief"], ["Trump personally called the", "board; stocks rally hard on", "his reinstatement."], "24 Nov  /  AP", "chip"),
    (526, 184, "#e8b44d", "MARKETS · NY", ["CrowdStrike to buy", "Zscaler: $43.9bn"], ["Record all-stock cyber deal,", "the largest security tie-up", "ever signed."], "24 Nov  /  BS", "chart"),
    (46, 397, "#67a9e8", "WAR · KYIV", ["700,000 Russian", "soldiers dead - report"], ["Zaporizhzhia strikes kill two;", "UNICEF: children dying at", "2022 levels."], "24 Nov  /  DN", "flag"),
    (526, 397, TEAL, "AFRICA · KHARTOUM", ["RSF drones strike", "Sudan's capital"], ["Airport hit as the national", "power grid nears total", "collapse; four dead."], "24 Nov  /  DN", "waves"),
]
for x, y, accent, kicker, title, body, credit, glyph in cards:
    d.rounded_rectangle((x, y, x+452, y+194), radius=16, fill=CREAM)
    d.rounded_rectangle((x, y+13, x+6, y+181), radius=3, fill=accent)
    text(x+22, y+14, kicker, 12, accent, True)
    text(x+22, y+39, title[0], 21, INK, True)
    text(x+22, y+65, title[1], 21, INK, True)
    for i, line in enumerate(body):
        if line: text(x+22, y+99+i*19, line, 12, "#66717d")
    text(x+22, y+164, credit, 11, "#7e8790", True)
    badge(x+391, y+96, glyph, accent)
d.rounded_rectangle((46, 604, 978, 668), radius=14, fill="#16324a")
text(66, 616, "ALSO TODAY", 12, TEAL, True)
tick = [(66, "TALLINN  Russia warns Estonia", "'on the verge of open war'"), (526, "VATICAN  Pope's private diary", "reveals spiritual crisis")]
for x, l1, l2 in tick:
    text(x, 624, l1, 13, "#d5dde5"); text(x, 643, l2, 13, "#d5dde5")
d.rounded_rectangle((46, 688, 978, 916), radius=18, fill="#16324a")
text(270, 712, "THE HAGUE  /  JUSTICE", 13, "#ef6461", True)
d.rounded_rectangle((823, 707, 948, 737), radius=15, fill="#245d68")
text(851, 714, "COURT", 12, TEAL, True)
text(270, 752, "UN top court: Myanmar guilty of", 27, "#ffffff", True)
text(270, 790, "Rohingya genocide", 27, "#ffffff", True)
text(270, 840, "ICJ rules on the 2017 crackdown, a ruling years in the making.  /  24 Nov", 17, GRAY)
text(270, 868, "and the first genocide verdict of its kind.", 17, GRAY)
d.line((158, 891, 158, 760), fill=TEAL, width=6)
d.line((112, 770, 204, 770), fill=TEAL, width=5)
d.arc((100, 770, 148, 812), 0, 180, fill=TEAL, width=4)
d.arc((168, 770, 216, 812), 0, 180, fill=TEAL, width=4)
d.line((132, 891, 184, 891), fill=TEAL, width=5)
d.line((46, 944, 978, 944), fill="#314457", width=1)
text(46, 962, "WORLD DESK  •  Filed 24 November 2026", 13, GRAY)
text(745, 962, "9 STORIES / ONE DAY", 13, TEAL, True)
os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
im.save(OUT)
print(f"wrote {OUT}")
