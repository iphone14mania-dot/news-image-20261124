#!/usr/bin/env python3
"""Draw the 24 November 2026 front page. Fresh code, Pillow + stdlib only.
Deliberately cleaner than the 23 Nov page: one hero story, two leads,
three cards, six briefs. All text hardcoded from verified reporting.
Output: entry.png, 1024x1024, next to this script."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")
W, H = 1024, 1024

FDIR = "/usr/share/fonts/truetype/liberation/"
SERIF = FDIR + "LiberationSerif-Regular.ttf"
SERIF_B = FDIR + "LiberationSerif-Bold.ttf"
SERIF_I = FDIR + "LiberationSerif-Italic.ttf"
SANS = FDIR + "LiberationSans-Regular.ttf"
SANS_B = FDIR + "LiberationSans-Bold.ttf"

PAPER = (247, 243, 234)
INK = (17, 17, 17)
RED = (179, 32, 44)
BLUE = (18, 52, 86)
SKY = (214, 230, 240)
SEA = (203, 224, 235)
GREY = (90, 88, 82)
RULE = (120, 116, 108)
NAVY = (16, 32, 54)
GREEN = (22, 120, 60)


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(d, text, fnt, maxw):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if d.textlength(trial, font=fnt) <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text(d, xy, s, fnt, fill=INK, anchor="la"):
    d.text(xy, s, font=fnt, fill=fill, anchor=anchor)


def centre(d, y, s, fnt, fill=INK):
    d.text((W // 2, y), s, font=fnt, fill=fill, anchor="ma")


def hline(d, y, x0=28, x1=996, fill=INK, width=1):
    d.line([(x0, y), (x1, y)], fill=fill, width=width)


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---------- top bar + masthead ----------
d.rectangle([0, 0, W, 6], fill=INK)
text(d, (28, 12), "THE WORLD IN ONE DAY", font(SANS_B, 13), fill=RED)
text(d, (996, 12), "TUESDAY'S NEWS  ·  ONE PAGE  ·  12 STORIES  ·  6 CONTINENTS",
     font(SANS_B, 13), anchor="ra")
hline(d, 30, width=2)
centre(d, 36, "Tuesday 24 November 2026", font(SERIF_B, 50))
centre(d, 90, "A genocide verdict the world backs  ·  a nuclear threat in orbit  ·  Huang returns to Nvidia",
       font(SERIF_I, 17), fill=(60, 58, 52))
hline(d, 112, width=2)

# ---------- HERO: ICJ / Myanmar ----------
hy, hh = 120, 282
d.rectangle([28, hy, 996, hy + hh], outline=INK, width=2)
# illustration panel (left): Peace Palace + scales of justice
px0, px1 = 30, 392
d.rectangle([px0, hy + 2, px1, hy + hh - 2], fill=SKY)
# sky sun + cloud
d.ellipse([px0 + 16, hy + 14, px0 + 52, hy + 50], fill=(255, 214, 90), outline=INK, width=1)
d.ellipse([px0 + 96, hy + 22, px0 + 140, hy + 38], fill=(255, 255, 255))
d.ellipse([px0 + 108, hy + 14, px0 + 148, hy + 32], fill=(255, 255, 255))
# courthouse: main block + tower
base = hy + hh - 2
d.rectangle([px0 + 30, base - 120, px1 - 30, base], fill=(176, 120, 82), outline=INK, width=2)
d.rectangle([px0 + 30, base - 132, px1 - 30, base - 120], fill=(120, 60, 50), outline=INK, width=1)
# tower
d.rectangle([px0 + 150, base - 196, px0 + 206, base - 120], fill=(176, 120, 82), outline=INK, width=2)
d.polygon([(px0 + 144, base - 196), (px0 + 178, base - 232), (px0 + 212, base - 196)],
          fill=(120, 60, 50), outline=INK)
d.ellipse([px0 + 168, base - 188, px0 + 188, base - 168], fill=(255, 255, 255), outline=INK, width=1)
d.line([(px0 + 178, base - 178), (px0 + 178, base - 186)], fill=INK, width=2)
d.line([(px0 + 178, base - 178), (px0 + 185, base - 175)], fill=INK, width=2)
# arched windows
for wx in (px0 + 48, px0 + 92, px0 + 240, px0 + 284):
    d.rectangle([wx, base - 100, wx + 26, base - 56], fill=(255, 240, 200), outline=INK, width=1)
    d.pieslice([wx, base - 112, wx + 26, base - 86], 180, 360, fill=(255, 240, 200), outline=INK, width=1)
# door
d.rectangle([px0 + 158, base - 66, px0 + 198, base], fill=(90, 50, 35), outline=INK, width=1)
# scales of justice, large in the open sky at the right (clear of the building)
sx, sy = px1 - 84, hy + 132
d.line([(sx, sy - 72), (sx, sy)], fill=(60, 50, 30), width=5)
d.line([(sx - 36, sy - 72), (sx + 36, sy - 72)], fill=(60, 50, 30), width=4)
d.line([(sx - 10, sy), (sx + 10, sy)], fill=(60, 50, 30), width=5)
for sgn in (-1, 1):
    ex = sx + sgn * 36
    d.line([(ex, sy - 72), (ex - 14, sy - 32)], fill=(60, 50, 30), width=3)
    d.line([(ex, sy - 72), (ex + 14, sy - 32)], fill=(60, 50, 30), width=3)
    d.arc([ex - 15, sy - 36, ex + 15, sy - 10], 0, 180, fill=(200, 160, 40), width=4)
d.ellipse([sx - 6, sy - 82, sx + 6, sy - 70], fill=(200, 160, 40), outline=INK)

# hero text (right)
tx = 416
ty = hy + 16
text(d, (tx, ty), "01  ·  THE HAGUE  ·  JUSTICE", font(SANS_B, 13), fill=RED)
ty += 22
for ln in wrap(d, "The world backs the genocide verdict on Myanmar",
               font(SERIF_B, 36), 996 - tx - 16):
    d.text((tx, ty), ln, font=font(SERIF_B, 36), fill=INK)
    ty += 40
ty += 6
for ln in wrap(d, "Fourteen nations endorse the International Court of Justice ruling "
                  "that Myanmar's forces committed genocide against the Rohingya — "
                  "the first time the court has found a state guilty.",
               font(SANS, 16), 996 - tx - 16):
    d.text((tx, ty), ln, font=font(SANS, 16), fill=(40, 38, 34))
    ty += 21
ty += 8
d.line([(tx, ty), (996 - 16, ty)], fill=RULE, width=1)
ty += 8
for ln in wrap(d, "Britain sanctions Myanmar's generals after the ruling; the verdict "
                  "sets a precedent for South Africa's case against Israel over Gaza.",
               font(SERIF_I, 15), 996 - tx - 16):
    d.text((tx, ty), ln, font=font(SERIF_I, 15), fill=(60, 58, 52))
    ty += 19

# ---------- MEDIUM ROW: NATO space + Nvidia ----------
my, mh = 412, 222
mw, gap = 478, 12
for i in range(2):
    x = 28 + i * (mw + gap)
    d.rectangle([x, my, x + mw, my + mh], outline=INK, width=1)
    d.rectangle([x + 1, my + 1, x + mw - 1, my + 78], fill=NAVY if i == 0 else (20, 60, 35))
    if i == 0:
        # starfield + satellite
        for sx, sy in [(x + 20, my + 16), (x + 60, my + 40), (x + 110, my + 12), (x + 200, my + 55),
                       (x + 300, my + 18), (x + 380, my + 44), (x + 440, my + 14), (x + 250, my + 30)]:
            d.ellipse([sx - 2, sy - 2, sx + 2, sy + 2], fill=(255, 255, 255))
        # orbit arc (kept inside the navy band)
        d.arc([x + 100, my + 6, x + 430, my + 140], 200, 340, fill=(120, 160, 200), width=2)
        # satellite body + panels
        cx, cy = x + 250, my + 34
        d.rectangle([cx - 12, cy - 10, cx + 12, cy + 10], fill=(200, 200, 210), outline=INK, width=1)
        d.rectangle([cx - 52, cy - 6, cx - 14, cy + 6], fill=(60, 110, 180), outline=INK, width=1)
        d.rectangle([cx + 14, cy - 6, cx + 52, cy + 6], fill=(60, 110, 180), outline=INK, width=1)
        d.line([(cx, cy - 10), (cx + 14, cy - 26)], fill=(200, 200, 210), width=2)
        d.ellipse([cx + 11, cy - 29, cx + 17, cy - 23], fill=RED)
        # radiation trefoil warning
        wx, wy = x + 60, my + 40
        d.ellipse([wx - 16, wy - 16, wx + 16, wy + 16], fill=(255, 200, 0), outline=INK, width=2)
        d.ellipse([wx - 4, wy - 4, wx + 4, wy + 4], fill=INK)
        for ang in (90, 210, 330):
            import math
            a = math.radians(ang)
            d.line([(wx, wy), (wx + int(13 * math.cos(a)), wy + int(13 * math.sin(a)))],
                   fill=INK, width=4)
        d.text((x + 350, my + 52), "60 DAYS?", font=font(SANS_B, 14), fill=(255, 200, 0))
    else:
        # rising chart
        base = my + 70
        pts = [(x + 24, base - 8), (x + 90, base - 16), (x + 160, base - 12), (x + 230, base - 30),
               (x + 300, base - 26), (x + 370, base - 48), (x + 440, base - 58)]
        d.line(pts, fill=(80, 220, 120), width=4)
        d.polygon([(x + 440, base - 58), (x + 424, base - 58), (x + 440, base - 42)],
                  fill=(80, 220, 120))
        for px, py in pts:
            d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=(255, 255, 255))
        d.text((x + 24, my + 10), "NASDAQ +6.5%   ·   S&P 500 +4.7%", font=font(SANS_B, 14), fill=(255, 255, 255))
        d.text((x + 24, my + 30), "NIKKEI +3.9%   ·   SEOUL +6%", font=font(SANS_B, 14), fill=(180, 230, 190))
    ty = my + 86
    if i == 0:
        d.text((x + 12, ty), "02", font=font(SERIF_B, 16), fill=RED)
        d.text((x + 42, ty + 2), "BRUSSELS  ·  SPACE", font=font(SANS_B, 11), fill=GREY)
        ty += 20
        for ln in wrap(d, "NATO vows to defend space as Russia 'may launch a nuclear satellite'",
                       font(SERIF_B, 19), mw - 24):
            d.text((x + 12, ty), ln, font=font(SERIF_B, 19), fill=INK)
            ty += 22
        ty += 2
        for ln in wrap(d, "Chief Mark Rutte: the alliance will meet any threat in orbit, "
                          "after reports of a nuclear-armed satellite within 60 days. (Reuters)",
                       font(SANS, 12), mw - 24):
            d.text((x + 12, ty), ln, font=font(SANS, 12), fill=(40, 38, 34))
            ty += 15
    else:
        d.text((x + 12, ty), "03", font=font(SERIF_B, 16), fill=RED)
        d.text((x + 42, ty + 2), "SILICON VALLEY  ·  TECH", font=font(SANS_B, 11), fill=GREY)
        ty += 20
        for ln in wrap(d, "Huang is back: Nvidia reinstates its chief — markets surge",
                       font(SERIF_B, 19), mw - 24):
            d.text((x + 12, ty), ln, font=font(SERIF_B, 19), fill=INK)
            ty += 22
        ty += 2
        for ln in wrap(d, "Jensen Huang returns as CEO less than two weeks after resigning, "
                          "after Trump intervened; stocks jump worldwide. (10 Things)",
                       font(SANS, 12), mw - 24):
            d.text((x + 12, ty), ln, font=font(SANS, 12), fill=(40, 38, 34))
            ty += 15

# ---------- SMALL ROW: 3 cards ----------
sy, sh = 644, 204
sw = 312
SMALL = [
    ("04", "SINALOA, MEXICO  ·  CRIME", "El Chapo Isidro caught with US drone help",
     "A US surveillance drone helped Mexican forces capture drug lord Fausto Isidro "
     "Meza Flores; Mexico will try him. (Daily Summary)", "drone"),
    ("05", "ZAPORIZHZHIA, UKRAINE  ·  WAR", "Russian strike kills two; Kyiv confirms Libya ship hits",
     "Overnight attack on Zaporizhzhia injures dozens; Ukraine confirms strikes on "
     "Russian ships off Libya as the UN seeks a probe. (Kyiv Independent)", "blast"),
    ("06", "NEPAL  ·  DISASTER", "M5.6 quake shakes Nepal near the China border",
     "The tremor strikes the Himalayan border region; no casualties reported yet "
     "as rescue teams assess remote villages. (Horizon)", "quake"),
]
for i, (num, tag, head, summ, art) in enumerate(SMALL):
    x = 28 + i * (sw + gap)
    d.rectangle([x, sy, x + sw, sy + sh], outline=INK, width=1)
    d.rectangle([x + 1, sy + 1, x + sw - 1, sy + 52], fill=SKY)
    if art == "drone":
        cx, cy = x + 60, sy + 26
        d.rectangle([cx - 14, cy - 6, cx + 14, cy + 6], fill=(60, 60, 64), outline=INK, width=1)
        for sgn in (-1, 1):
            d.line([(cx + sgn * 14, cy), (cx + sgn * 30, cy - 6)], fill=INK, width=2)
            d.ellipse([cx + sgn * 30 - 10, cy - 10, cx + sgn * 30 + 10, cy - 6], fill=(150, 150, 150), outline=INK)
        d.ellipse([cx - 4, cy + 6, cx + 4, cy + 12], fill=RED, outline=INK)
        d.text((x + 130, sy + 16), "CAPTURED", font=font(SANS_B, 16), fill=RED)
        d.line([(x + 130, sy + 36), (x + 240, sy + 36)], fill=RED, width=2)
    elif art == "blast":
        d.rectangle([x + 1, sy + 1, x + sw - 1, sy + 52], fill=(30, 44, 66))
        for bx, bw, bh in [(x + 16, 40, 26), (x + 62, 36, 34), (x + 104, 44, 22), (x + 220, 40, 30), (x + 266, 32, 20)]:
            d.rectangle([bx, sy + 52 - bh, bx + bw, sy + 52], fill=(70, 84, 104), outline=INK, width=1)
            for wy in range(sy + 52 - bh + 5, sy + 48, 8):
                for wx in range(bx + 5, bx + bw - 4, 10):
                    d.rectangle([wx, wy, wx + 4, wy + 4], fill=(255, 214, 90))
        ex, ey = x + 180, sy + 22
        d.ellipse([ex - 20, ey - 20, ex + 20, ey + 20], fill=(255, 120, 40))
        for dx, dy in [(0, -18), (13, -13), (18, 0), (13, 13), (0, 18), (-13, 13), (-18, 0), (-13, -13)]:
            d.line([(ex, ey), (ex + dx, ey + dy)], fill=(255, 180, 40), width=4)
        d.ellipse([ex - 8, ey - 8, ex + 8, ey + 8], fill=(255, 220, 90), outline=RED, width=2)
    else:  # quake
        d.polygon([(x + 20, sy + 52), (x + 90, sy + 8), (x + 150, sy + 52)], fill=(120, 130, 140), outline=INK)
        d.polygon([(x + 90, sy + 8), (x + 112, sy + 22), (x + 90, sy + 30), (x + 70, sy + 22)],
                  fill=(255, 255, 255), outline=INK)
        d.polygon([(x + 110, sy + 52), (x + 180, sy + 18), (x + 250, sy + 52)], fill=(100, 110, 120), outline=INK)
        # seismic zigzag
        d.line([(x + 246, sy + 14), (x + 252, sy + 26), (x + 258, sy + 8), (x + 264, sy + 28),
                (x + 270, sy + 10), (x + 276, sy + 24), (x + 282, sy + 14)], fill=RED, width=2)
        d.text((x + 252, sy + 30), "M5.6", font=font(SANS_B, 15), fill=RED)
    ty = sy + 58
    d.text((x + 10, ty), num, font=font(SERIF_B, 15), fill=RED)
    d.text((x + 38, ty + 2), tag, font=font(SANS_B, 9), fill=GREY)
    ty += 18
    for ln in wrap(d, head, font(SERIF_B, 16), sw - 20):
        d.text((x + 10, ty), ln, font=font(SERIF_B, 16), fill=INK)
        ty += 19
    ty += 2
    for ln in wrap(d, summ, font(SANS, 11), sw - 20):
        d.text((x + 10, ty), ln, font=font(SANS, 11), fill=(40, 38, 34))
        ty += 13

# ---------- also today ----------
y = sy + sh + 8
hline(d, y)
y += 6
d.text((28, y), "ALSO ON TUESDAY 24 NOVEMBER", font=font(SANS_B, 12), fill=RED)
ALSO = [
    "07  China sentences an official to death for spying for a foreign country. (Gold Wall Press)",
    "08  Russia warns Estonia its moves are \"on the verge of triggering open war\". (Reuters)",
    "09  Israeli airstrikes kill at least six Palestinians in Gaza, medics say. (Reuters)",
    "10  Solomon Islands to end its security pact with China. (10 Things)",
    "11  Oregon and Virginia sue SpaceX over alleged Grok-generated abuse images. (iqmia)",
    "12  Pennsylvania measles outbreak claims a ninth life; 46 counties affected. (Horizon)",
]
ay = y + 16
for i, line in enumerate(ALSO):
    col, row = i // 3, i % 3
    d.text((28 + col * 484, ay + row * 15), line, font=font(SANS, 11), fill=INK)
y = ay + 3 * 15 + 6
hline(d, y)

# ---------- footer ----------
y += 6
for ln in wrap(d, "Every story here happened, or was first reported, on Tuesday 24 November 2026 in at least one "
                  "time zone. Claims are attributed, not stated as fact. "
                  "Sources: Reuters, Daily Summary of World, The Global Eye, Horizon, 10 Things, Kyiv Independent. "
                  "Original vector drawings.",
               font(SANS, 10), 968):
    d.text((28, y), ln, font=font(SANS, 10), fill=GREY)
    y += 12
d.text((28, y + 2), "THE WORLD IN ONE DAY  ·  TUESDAY 24 NOVEMBER 2026",
       font=font(SANS_B, 9), fill=GREY)

img.save(OUT, "PNG", optimize=True)
print("saved", OUT, img.size, os.path.getsize(OUT), "bytes; footer ends at y =", y + 14)
