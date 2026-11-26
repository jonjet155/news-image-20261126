#!/usr/bin/env python3
"""Build-time renderer for news-image-20261126 (Thursday 26 November 2026).
Code-drawn flat 2D vector, PIL + DejaVu. Build-time only: the graded
main.py is stdlib-only and merely copies the pre-built entry.png.
Method: Superskie-34 (34-36 stories, UTC timeline strip, veracity tags,
DATE CHECK Left out + Not yet). All stories verified in
~/workspace/makefun/news-image-20261126-research.md (26 Nov 2026).
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

CREAM = (247, 241, 222)
PAPER = (252, 248, 236)
INK = (26, 26, 26)
NAVY = (31, 58, 95)
RED = (178, 39, 30)
RED_DK = (140, 28, 22)
MUSTARD = (217, 164, 65)
CORAL = (224, 120, 86)
TEAL = (42, 122, 120)
OLIVE = (158, 168, 120)
SEA = (213, 228, 232)
LAND = (198, 200, 168)
LAND_DK = (178, 182, 146)
GREY = (110, 110, 104)
LIGHT_LINE = (200, 190, 165)

FD = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FD, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)       # noqa: E731
SERIF = lambda s: font("DejaVuSerif.ttf", s)              # noqa: E731
SERIF_I = lambda s: font("DejaVuSerif.ttf", s)               # noqa: E731
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)         # noqa: E731
SANS = lambda s: font("DejaVuSans.ttf", s)                # noqa: E731

# ---------------------------------------------------------------- data
# region: one of Americas / Europe / Asia-Pacific / Middle East / Africa /
# Oceania / Global.  tag: CONFIRMED / REPORTED / ONGOING.
PANELS = [
    dict(n=1, region="Americas", tag="CONFIRMED", src="NBC",
         art="macys", chip="POSTPONED TO SATURDAY",
         head="Macy's 100th Thanksgiving parade postponed to Saturday",
         deck="30 mph winds, gusts to 55 mph, empty the route; the parade "
              "moves to Saturday — a first in 100 years."),
    dict(n=2, region="Middle East", tag="CONFIRMED", src="SPA",
         art="missile", chip="2 MISSILES DOWN",
         head="Saudi Arabia intercepts 2 Houthi missiles aimed at Riyadh",
         deck="2 ballistic missiles downed; a projectile falls on Jazan "
              "port, no casualties."),
    dict(n=3, region="Asia-Pacific", tag="CONFIRMED", src="PIB",
         art="mumbai", chip="18 YEARS ON",
         head="India marks 18 years since the 26/11 Mumbai attacks",
         deck="Tributes at the Gateway of India at 19:30 IST; 166 were killed "
              "in the 2008 attacks, on the exact anniversary."),
    dict(n=4, region="Americas", tag="CONFIRMED", src="Reuters",
         art="musk", chip="2 SHARES EACH",
         head="Musk pledges 2 SpaceX shares per US child",
         deck="First transfers start in December; SpaceX unlisted."),
    dict(n=5, region="Global", tag="CONFIRMED", src="AP",
         art="market", chip="REBOUND",
         head="Asia, Europe rebound after tariff rout",
         deck="Nikkei +0.9% to 57,499; Kospi +0.3% after -6.2% fall."),
    dict(n=6, region="Europe", tag="CONFIRMED", src="NY Post",
         art="kyiv", chip="KYIV HIT",
         head="Russian missile hits Kyiv mall; 7 hurt",
         deck="7 hurt in Kyiv; 4 killed in Kharkiv, 2 in Sloviansk; 87 drones down."),
    dict(n=7, region="Middle East", tag="CONFIRMED", src="AP",
         art="gaza", chip="8 KILLED",
         head="Israeli strikes kill 8 in Gaza",
         deck="Senior Hamas education official among the dead."),
    dict(n=8, region="Americas", tag="CONFIRMED", src="Al Jazeera",
         art="tariff", chip="TARIFF ROW",
         head="Brazil, China blast US tariffs",
         deck="Brazil calls the plan unfair; China: 'baseless'."),
    dict(n=9, region="Europe", tag="CONFIRMED", src="Reuters",
         art="migration", chip="77,000",
         head="UK net migration falls to 77,000",
         deck="Lowest in nearly three decades outside the pandemic."),
    dict(n=10, region="Middle East", tag="CLAIM", src="Tasnim",
         art="hormuz", chip="CLAIM",
         head="Iran claims 2 tankers mined near Hormuz",
         deck="IRGC says the tankers were mined off Khasab, Oman."),
    dict(n=11, region="Europe", tag="ONGOING", src="FIDE",
         art="chess", chip="GAME 3",
         head="Gukesh meets Sindarov in Game 3",
         deck="Title match level after two draws; Game 3 in Geneva."),
    dict(n=12, region="Europe", tag="REPORTED", src="The Guardian",
         art="eu", chip="DEADLOCK",
         head="EU budget summit deadlocked",
         deck="'Light-years away' from a deal, Italy's PM says."),
    dict(n=13, region="Europe", tag="REPORTED", src="The Telegraph",
         art="reserves", chip="100,000",
         head="UK contacts 100,000 reservists",
         deck="MoD seeks contacts, jobs, skills; no call-up ordered."),
]

# ALSO ON 14-35: (number, one-line text, source). Kept <= ~72 chars so each
# fits on ONE line at 9pt in a 342px column.
ALSO = [
    (14, "Nor'easter disrupts Thanksgiving travel for millions", "AccuWeather"),
    (15, "Thanksgiving proclaimed; targets NYT reporter in posts", "HuffPost"),
    (16, "Anthropic recovers +1.1% after IPO slide", "AP"),
    (17, "Nvidia -3.9% as S&P Global warns on its rating", "AP"),
    (18, "Venezuela continues US-backed talks", "Caribbean News Global"),
    (19, "India tightens food labels; ends 'double standards'", "Reuters"),
    (20, "India orders tighter checks on bottled water", "Reuters"),
    (21, "Lee Zii Jia, Unnati Hooda reach Syed Modi quarter-finals", "BWF"),
    (22, "Australia-Fiji alliance in force; Fiji's first ever", "AAP"),
    (23, "Congo Ebola cases pass 12,000; 5,904 dead", "Reuters"),
    (24, "SoftBank +7.3%, Kioxia +12.6% lead Asia AI rebound", "AP"),
    (25, "Hafiz Saeed's son seen with politicians in Pakistan", "News18"),
    (26, "Dollar rises to 159.30 yen; euro $1.0968", "AP"),
    (27, "Oil up: Brent $91.09, WTI $84.51 on Mideast tension", "AP"),
    (28, "Syria seizes IRGC arms bound for Lebanon", "Iran International"),
    (29, "ISIS suicide attack kills 2 Syrian security staff", "Al Jazeera"),
    (30, "783,000 Captagon pills seized on Lebanon border", "L'Orient Today"),
    (31, "Ukraine drone kills 5 in occupied Zaporizhzhia", "Al Jazeera"),
    (32, "Zelenskyy: Russia readying new energy strike", "Ukrainska Pravda"),
    (33, "Kremlin: Ukraine seeks to widen war to Med, Baltics", "Reuters"),
    (34, "UK unveils 'Cutting Costs' bill for trade with Europe", "gov.uk"),
    (35, "UK publishes more Mandelson ambassador files", "The Guardian"),
]

TIMELINE = [
    ("04:30 UTC", "Musk pledges 2 SpaceX shares for every US child"),
    ("06:21 UTC", "Asia stocks rebound; Nikkei closes +0.9%"),
    ("07:03 UTC", "Saudi intercepts 2 missiles aimed at Riyadh"),
    ("07:30 UTC", "Israeli strikes kill 8 in Gaza"),
    ("10:30 UTC", "Russian missile hits Kyiv mall; 7 hurt"),
    ("14:00 UTC", "Gukesh Game 3 begins; Mumbai 26/11 memorial"),
]

REGIONS = ["Europe", "Asia-Pacific", "Americas", "Middle East", "Global",
           "Oceania", "Africa"]
REGION_COLORS = {"Europe": (31, 58, 95), "Asia-Pacific": (178, 39, 30),
                 "Americas": (217, 164, 65), "Middle East": (42, 122, 120),
                 "Global": (110, 110, 104), "Oceania": (224, 120, 86),
                 "Africa": (120, 90, 140)}

DATECHECK_LEFT = [
    "Left out: Cairo tanker fire (31 killed) — Wed 25 Nov · Section 301 tariff plan — 25 Nov · "
    "Bangladesh wage +36% to 17,000 taka — 25 Nov · Shenzhou-24 launch — 25 Nov",
    "Iowa lead-azide detonation (planned) — 25 Nov · Australia CPI 4.9% — 25 Nov · "
    "PIF HQ attack, 11 hurt — 25 Nov · COP31 — 21 Nov",
]
DATECHECK_NOTYET = ("Not yet: Gukesh Game 3 result · Europa League matchday 5 · "
                    "NFL Thanksgiving scores")

# ---------------------------------------------------------------- helpers
def tw(draw, text, fnt):
    return draw.textlength(text, font=fnt)


def wrap(draw, text, fnt, maxw):
    """Greedy wrap; returns list of lines, never splits a word."""
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= maxw:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_font(draw, text, names, size, maxw, maxlines, minsize=11):
    """Largest size in `names` trial order that fits text in maxlines lines."""
    s = size
    while s >= minsize:
        fnt = font(names, s)
        if len(wrap(draw, text, fnt, maxw)) <= maxlines:
            return fnt
        s -= 1
    return font(names, minsize)


def text(draw, xy, s, fnt, fill=INK, anchor="la"):
    draw.text(xy, s, font=fnt, fill=fill, anchor=anchor)


def rrect(draw, box, rad, fill=None, outline=None, width=1):
    draw.rounded_rectangle(box, radius=rad, fill=fill, outline=outline, width=width)

# ---------------------------------------------------------------- art scenes
# Each draws a flat 2D scene into box (x, y, w, h). Simple bold shapes only.

def art_bg(d, box, c):
    d.rectangle(box, fill=c)


def art_macys(d, x, y, w, h):
    art_bg(d, (x, y, x + w, y + h), (38, 52, 86))
    # skyline
    for bx, bw, bh in [(6, 26, 46), (38, 20, 62), (62, 30, 40), (96, 22, 70),
                       (124, 28, 48), (158, 20, 58), (184, 26, 42), (212, 24, 64),
                       (242, 28, 44), (276, 22, 60)]:
        d.rectangle([x + bx, y + h - bh, x + bx + bw, y + h], fill=(24, 34, 58))
        for wy in range(y + h - bh + 6, y + h - 4, 10):
            for wx in range(x + bx + 4, x + bx + bw - 3, 8):
                d.rectangle([wx, wy, wx + 3, wy + 4], fill=(217, 164, 65))
    # balloon: white ellipse + face
    cx, cy = x + w // 2, y + h // 2 - 8
    d.ellipse([cx - 52, cy - 26, cx + 52, cy + 26], fill=(252, 248, 236),
              outline=(26, 26, 26), width=2)
    d.ellipse([cx - 20, cy - 8, cx - 10, cy + 2], fill=INK)
    d.ellipse([cx + 10, cy - 8, cx + 20, cy + 2], fill=INK)
    d.arc([cx - 14, cy + 2, cx + 14, cy + 18], 20, 160, fill=RED, width=3)
    # rain streaks
    for rx in range(x + 10, x + w - 10, 26):
        d.line([rx, y + 6, rx - 6, y + 22], fill=(150, 180, 210), width=2)


def art_missile(d, x, y, w, h):
    art_bg(d, (x, y, x + w, y + h), (232, 196, 140))
    # sun + dunes
    d.ellipse([x + w - 52, y + 10, x + w - 12, y + 50], fill=(217, 164, 65))
    d.polygon([(x, y + h), (x + 90, y + h - 34), (x + 200, y + h), ],
              fill=(214, 164, 96))
    d.polygon([(x + 140, y + h), (x + 260, y + h - 40), (x + w, y + h)],
              fill=(198, 146, 84))
    # two intercept bursts (red starbursts) with trails
    for bx, by in [(x + 92, y + 34), (x + 196, y + 26)]:
        d.line([bx - 46, by + 34, bx - 8, by + 6], fill=(120, 120, 120), width=3)
        for ang in range(0, 360, 45):
            import math
            ex = bx + 16 * math.cos(math.radians(ang))
            ey = by + 16 * math.sin(math.radians(ang))
            d.line([bx, by, ex, ey], fill=RED, width=3)
        d.ellipse([bx - 5, by - 5, bx + 5, by + 5], fill=RED)
    # small skyline (Riyadh towers)
    for bx, bw, bh in [(x + 14, 16, 34), (x + 34, 12, 46), (x + 250, 18, 40),
                       (x + 272, 12, 30)]:
        d.rectangle([bx, y + h - bh, bx + bw, y + h], fill=(90, 70, 52))


def art_mumbai(d, x, y, w, h):
    art_bg(d, (x, y, x + w, y + h), (238, 150, 90))
    d.ellipse([x + w - 70, y + 12, x + w - 22, y + 60], fill=(247, 220, 150))
    # Gateway arch
    ax, ay = x + 34, y + 22
    d.rectangle([ax, ay, ax + 92, y + h - 16], fill=(186, 120, 70),
                outline=(120, 70, 40), width=2)
    d.pieslice([ax + 16, ay + 20, ax + 76, ay + 70], 180, 360,
               fill=(238, 150, 90), outline=(120, 70, 40), width=2)
    d.rectangle([ax + 34, y + h - 44, ax + 58, y + h - 16], fill=(120, 70, 40))
    # candles row
    for i in range(7):
        cx = x + 158 + i * 22
        d.rectangle([cx, y + h - 26, cx + 8, y + h - 12], fill=(252, 248, 236))
        d.ellipse([cx + 1, y + h - 34, cx + 7, y + h - 26], fill=(255, 200, 60))


def art_musk(d, x, y, w, h):
    art_bg(d, (x, y, x + w, y + h), (24, 34, 58))
    # stars, all kept inside the art box (v2 had stars below it, invisible,
    # and past its right edge, onto the next panel)
    for sx, sy in [(16, 10), (64, 22), (126, 6), (176, 8), (184, 16),
                   (8, 44), (44, 40), (136, 44), (180, 10)]:
        d.ellipse([x + sx, y + sy, x + sx + 3, y + sy + 3], fill=(252, 248, 236))
    # rocket, compressed to fit h (small panels h=52; v2 flame/fins ran
    # past the art box and over the kicker + headline). Nose y+2, flame ends y+48.
    # Shifted +20px right so the flame clears the chip (chip covers x 0..~94,
    # y 36..52); right coin moved to bottom-right to clear the shifted body.
    rx, ry = x + w // 2 + 8, y + 2
    d.polygon([(rx + 12, ry), (rx + 24, ry + 14), (rx, ry + 14)], fill=RED)
    d.rectangle([rx, ry + 14, rx + 24, ry + 34], fill=(252, 248, 236))
    d.ellipse([rx + 7, ry + 20, rx + 17, ry + 30], fill=TEAL)
    d.polygon([(rx - 8, ry + 34), (rx, ry + 24), (rx, ry + 34)], fill=RED)
    d.polygon([(rx + 24, ry + 34), (rx + 32, ry + 34), (rx + 24, ry + 24)],
              fill=RED)
    d.polygon([(rx + 6, ry + 34), (rx + 12, ry + 48), (rx + 18, ry + 34)],
              fill=(255, 200, 60))
    # two share coins, clear of the chip (chip covers y+h-15..y+h+1);
    # right coin at bottom-right to clear the shifted rocket body.
    d.ellipse([x + 30, y + h - 44, x + 56, y + h - 18], fill=MUSTARD,
              outline=(26, 26, 26), width=2)
    d.text((x + 43, y + h - 31), "$", font=SANS_B(13), fill=INK, anchor="mm")
    d.ellipse([x + w - 44, y + h - 30, x + w - 18, y + h - 4], fill=MUSTARD,
              outline=(26, 26, 26), width=2)
    d.text((x + w - 31, y + h - 17), "$", font=SANS_B(13), fill=INK,
           anchor="mm")


def art_market(d, x, y, w, h):
    art_bg(d, (x, y, x + w, y + h), (232, 240, 225))
    # grid
    for gy in range(y + 10, y + h - 6, 12):
        d.line([x + 8, gy, x + w - 8, gy], fill=(200, 210, 195), width=1)
    # rising line, all points inside the art box
    pts = [(x + 10, y + h - 12), (x + 55, y + h - 22), (x + 95, y + h - 18),
           (x + 135, y + h - 30), (x + 170, y + h - 26),
           (x + w - 12, y + h - 38)]
    d.line(pts, fill=(30, 130, 70), width=3, joint="curve")
    d.polygon([(pts[-1][0] - 10, pts[-1][1] + 2), (pts[-1][0] + 2, pts[-1][1] + 2),
               (pts[-1][0] - 4, pts[-1][1] + 12)], fill=(30, 130, 70))
    d.text((x + w - 10, y + 4), "+0.9%", font=SANS_B(13), fill=(30, 130, 70),
           anchor="ra")


def art_kyiv(d, x, y, w, h):
    art_bg(d, (x, y, x + w, y + h), (120, 140, 168))
    d.rectangle([x + 16, y + h - 52, x + 96, y + h], fill=(90, 100, 118))
    d.rectangle([x + 110, y + h - 40, x + 170, y + h], fill=(70, 82, 100))
    for wy in range(y + h - 46, y + h - 6, 12):
        for wx in range(x + 22, x + 92, 12):
            d.rectangle([wx, wy, wx + 6, wy + 6], fill=(217, 164, 65))
    # blast star
    bx, by = x + w - 58, y + 34
    for ang in range(0, 360, 30):
        import math
        ex = bx + 22 * math.cos(math.radians(ang))
        ey = by + 22 * math.sin(math.radians(ang))
        d.line([bx, by, ex, ey], fill=(255, 200, 60), width=4)
    d.ellipse([bx - 9, by - 9, bx + 9, by + 9], fill=(255, 220, 100))
    d.ellipse([x + 30, y + 14, x + 44, y + 28], fill=(230, 230, 225))


def art_gaza(d, x, y, w, h):
    # v4: high contrast — dusk sky, DARK skyline with lit windows, PALE
    # smoke, casualty count on a cream disc. v3 was grey-on-grey and
    # unreadable at 300px. Building heights capped so no roof pokes above
    # the art box (v3 bh=60 overflowed h=52).
    art_bg(d, (x, y, x + w, y + h), (216, 164, 110))
    for bx, bw, bh in [(14, 34, 40), (54, 28, 48), (88, 36, 34), (130, 30, 46)]:
        d.rectangle([x + bx, y + h - bh, x + bx + bw, y + h], fill=(52, 48, 44))
        for wy in range(y + h - bh + 6, y + h - 6, 12):
            for wx in range(x + bx + 5, x + bx + bw - 5, 12):
                d.rectangle([wx, wy, wx + 4, wy + 5], fill=(255, 200, 60))
    # pale smoke plumes above the skyline: each a cluster of overlapping
    # ellipses so they read as smoke, not the perfect circles of v4-r1
    # (which looked like balloons at 300px). No outlines — the pale fill
    # contrasts against both the dusk sky and the dark buildings.
    for sx, sy, sr in [(x + 58, y + 24, 9), (x + 72, y + 18, 12),
                       (x + 84, y + 25, 8), (x + 88, y + 22, 9),
                       (x + 100, y + 14, 12), (x + 112, y + 22, 9),
                       (x + 116, y + 26, 7), (x + 126, y + 20, 9),
                       (x + 136, y + 26, 7)]:
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(240, 234, 222))
    # casualty count on a cream disc so the red reads at 300px
    d.ellipse([x + w - 48, y + h - 40, x + w - 12, y + h - 4],
              fill=(252, 248, 236), outline=(26, 26, 26), width=2)
    d.text((x + w - 30, y + h - 22), "8", font=SERIF_B(26), fill=RED_DK,
           anchor="mm")


def art_tariff(d, x, y, w, h):
    art_bg(d, (x, y, x + w, y + h), (240, 225, 190))
    # Brazil flag-ish block (left) + China flag-ish block (middle), both
    # narrowed so "%" sits on plain cream at right and reads whole.
    # v2: "%" was red on the red China block (left half invisible) and the
    # Brazil "diamond" was degenerate (all 4 vertices on one line).
    d.rectangle([x + 12, y + 16, x + 80, y + h - 16], fill=(0, 140, 70))
    d.polygon([(x + 18, y + h // 2), (x + 46, y + 20), (x + 74, y + h // 2),
               (x + 46, y + h - 20)], fill=(255, 210, 0))
    d.ellipse([x + 36, y + h // 2 - 10, x + 56, y + h // 2 + 10], fill=NAVY)
    d.rectangle([x + 88, y + 16, x + 140, y + h - 16], fill=(200, 30, 30))
    for sx, sy in [(98, 24), (111, 21), (121, 28), (109, 32), (99, 31)]:
        d.ellipse([x + sx - 3, y + sy - 3, x + sx + 3, y + sy + 3],
                  fill=(255, 220, 0))
    d.text((x + 148, y + 10), "%", font=SERIF_B(30), fill=RED)


def art_migration(d, x, y, w, h):
    art_bg(d, (x, y, x + w, y + h), (228, 232, 240))
    d.text((x + 30, y + 6), "77,000", font=SANS_B(22), fill=NAVY)
    # down arrow
    ax = x + w - 34
    d.line([ax, y + 8, ax, y + h - 20], fill=RED, width=5)
    d.polygon([(ax - 10, y + h - 30), (ax + 10, y + h - 30), (ax, y + h - 12)],
              fill=RED)


def art_hormuz(d, x, y, w, h):
    # v4: tankers fully INSIDE the art box. v3 put the bridge at y+h-62
    # (y-10 for h=52) so the tankers were cut off at the panel's top edge.
    # Water band 12px; hull 14px; bridge 12px — all tops >= y+14.
    art_bg(d, (x, y, x + w, y + h), (150, 190, 210))
    d.rectangle([x, y + h - 12, x + w, y + h], fill=(40, 110, 150))
    # two tankers: hull + bridge + funnel, all inside the box
    for tx in (x + 16, x + 110):
        d.rectangle([tx, y + h - 26, tx + 72, y + h - 12], fill=(140, 40, 40))
        d.rectangle([tx + 10, y + h - 38, tx + 26, y + h - 26],
                    fill=(120, 30, 30))
        d.rectangle([tx + 44, y + h - 34, tx + 52, y + h - 26],
                    fill=(100, 25, 25))
    # mines (spiked dots) in open water, clear of both bridges
    for mx, my in [(x + 58, y + 12), (x + 168, y + 10), (x + 96, y + 16)]:
        d.ellipse([mx - 5, my - 5, mx + 5, my + 5], fill=INK)
        d.line([mx - 9, my, mx + 9, my], fill=INK, width=2)
        d.line([mx, my - 9, mx, my + 9], fill=INK, width=2)


def art_chess(d, x, y, w, h):
    art_bg(d, (x, y, x + w, y + h), (40, 70, 50))
    cs = 11
    ox, oy = x + 10, y + 4
    for r in range(4):
        for c in range(8):
            col = (252, 248, 236) if (r + c) % 2 == 0 else (60, 60, 60)
            d.rectangle([ox + c * cs, oy + r * cs, ox + (c + 1) * cs,
                         oy + (r + 1) * cs], fill=col)
    # knight-ish piece: circle + notch
    d.ellipse([x + w - 52, y + 6, x + w - 18, y + 40], fill=(252, 248, 236),
              outline=INK, width=2)
    d.text((x + w - 35, y + 23), "N", font=SERIF_B(18), fill=INK, anchor="mm")
    d.text((x + 112, y + h - 12), "1 - 1", font=SANS_B(12),
           fill=(252, 248, 236))


def art_eu(d, x, y, w, h):
    art_bg(d, (x, y, x + w, y + h), (31, 58, 120))
    import math
    cx, cy = x + 38, y + h // 2
    for i in range(12):
        ang = math.radians(i * 30 - 90)
        sx = cx + 24 * math.cos(ang)
        sy = cy + 24 * math.sin(ang)
        d.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=(255, 220, 0))
    d.text((x + 84, y + 6), "€", font=SERIF_B(26), fill=(255, 220, 0))
    d.text((x + 84, y + h - 20), "BUDGET", font=SANS_B(12),
           fill=(252, 248, 236))


def art_reserves(d, x, y, w, h):
    art_bg(d, (x, y, x + w, y + h), (210, 200, 160))
    # envelope (small, left) + count (right)
    ex, ey, ew, eh = x + 14, y + 10, 84, 34
    d.rectangle([ex, ey, ex + ew, ey + eh], fill=(252, 248, 236),
                outline=INK, width=2)
    d.line([ex, ey, ex + ew // 2, ey + 20], fill=INK, width=2)
    d.line([ex + ew, ey, ex + ew // 2, ey + 20], fill=INK, width=2)
    d.text((x + 108, y + 16), "100,000", font=SANS_B(14), fill=RED_DK)
    # helmet, bottom-right
    d.pieslice([x + 140, y + h - 22, x + 172, y + h - 2], 180, 360,
               fill=(90, 110, 70))


ART = {"macys": art_macys, "missile": art_missile, "mumbai": art_mumbai,
       "musk": art_musk, "market": art_market, "kyiv": art_kyiv,
       "gaza": art_gaza, "tariff": art_tariff, "migration": art_migration,
       "hormuz": art_hormuz, "chess": art_chess, "eu": art_eu,
       "reserves": art_reserves}

# ---------------------------------------------------------------- world map
# Crude equirectangular continent polygons (lon, lat). Recognisable blobs
# only; pins are verified from rendered pixels, not from these coords.
N_AMERICA = [(-168, 66), (-158, 58), (-140, 60), (-130, 54), (-125, 48),
             (-124, 40), (-120, 34), (-114, 29), (-110, 24), (-105, 20),
             (-97, 16), (-92, 15), (-86, 12), (-83, 9), (-79, 9), (-80, 13),
             (-84, 16), (-88, 21), (-90, 21), (-97, 26), (-93, 30),
             (-89, 30), (-84, 30), (-81, 25), (-80, 32), (-76, 35),
             (-74, 40), (-70, 42), (-66, 45), (-60, 47), (-55, 47),
             (-60, 52), (-64, 58), (-68, 58), (-72, 62), (-78, 62),
             (-85, 66), (-92, 66), (-95, 69), (-110, 68), (-125, 70),
             (-140, 70), (-155, 71), (-165, 68)]
GREENLAND = [(-58, 64), (-52, 60), (-43, 60), (-40, 64), (-32, 68),
             (-22, 70), (-20, 74), (-30, 76), (-45, 76), (-58, 74), (-60, 70)]
S_AMERICA = [(-79, 9), (-77, 4), (-80, -3), (-81, -6), (-77, -12), (-72, -18),
             (-70, -23), (-70, -30), (-72, -37), (-73, -44), (-70, -50),
             (-68, -55), (-65, -55), (-68, -50), (-62, -41), (-57, -38),
             (-52, -33), (-48, -28), (-41, -23), (-39, -17), (-35, -9),
             (-35, -6), (-40, -3), (-44, -2), (-50, 0), (-53, 4), (-58, 6),
             (-62, 9), (-68, 11), (-72, 12), (-76, 10)]
AFRICA = [(-6, 35), (-10, 31), (-15, 27), (-17, 21), (-17, 15), (-15, 11),
          (-12, 8), (-8, 5), (-4, 5), (0, 6), (6, 4), (9, 4), (9, -1),
          (12, -5), (13, -10), (12, -17), (14, -22), (16, -28), (19, -34),
          (26, -34), (32, -28), (35, -24), (40, -16), (40, -10), (42, -4),
          (46, -1), (51, 2), (51, 11), (48, 11), (43, 12), (40, 15),
          (38, 18), (37, 22), (34, 27), (32, 31), (30, 31), (25, 32),
          (20, 32), (15, 32), (10, 34), (11, 34), (5, 37), (0, 36)]
EURASIA = [(-10, 36), (-9, 43), (-2, 44), (-1, 46), (-4, 48), (-2, 50),
           (0, 51), (3, 53), (8, 57), (10, 59), (5, 60), (5, 62), (10, 64),
           (12, 66), (18, 69), (25, 71), (30, 70), (35, 68), (40, 68),
           (45, 68), (50, 69), (55, 68), (60, 69), (65, 68), (70, 72),
           (75, 73), (80, 73), (85, 74), (90, 75), (95, 76), (100, 77),
           (105, 77), (110, 74), (115, 73), (120, 73), (125, 72), (130, 71),
           (135, 72), (140, 72), (145, 72), (150, 70), (155, 69), (160, 69),
           (165, 66), (170, 66), (178, 65), (178, 62), (170, 60), (162, 60),
           (158, 56), (156, 51), (150, 59), (142, 54), (142, 50), (140, 46),
           (138, 43), (135, 43), (130, 42), (127, 40), (126, 38), (122, 38),
           (120, 34), (122, 31), (120, 28), (118, 25), (112, 22), (108, 20),
           (106, 18), (104, 12), (103, 8), (100, 7), (98, 10), (97, 14),
           (94, 16), (92, 21), (89, 22), (86, 20), (84, 19), (80, 16),
           (80, 13), (77, 8), (75, 12), (73, 16), (72, 20), (70, 22),
           (68, 23), (66, 25), (62, 25), (58, 26), (56, 27), (58, 24),
           (59, 22), (57, 19), (55, 17), (52, 15), (48, 14), (44, 13),
           (42, 15), (40, 17), (38, 19), (36, 21), (35, 23), (34, 27),
           (34, 29), (35, 31), (34, 31), (32, 31), (30, 31), (28, 32), (26, 34), (23, 36), (22, 37), (20, 39), (19, 40),
           (19, 42), (16, 42), (14, 44), (12, 44), (10, 44), (8, 44),
           (6, 43), (3, 42), (0, 40), (-2, 37), (-6, 36)]
UK = [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 57), (0, 53), (1, 51),
      (-3, 50)]
JAPAN = [(129, 31), (131, 32), (134, 33), (137, 34), (140, 35), (141, 38),
         (142, 41), (144, 44), (145, 45), (143, 43), (141, 40), (140, 37),
         (138, 35), (135, 34), (132, 33), (130, 32)]
AUSTRALIA = [(113, -22), (114, -28), (115, -33), (118, -35), (124, -33),
             (129, -32), (132, -32), (135, -35), (138, -35), (140, -38),
             (145, -38), (150, -37), (153, -32), (153, -27), (150, -23),
             (146, -19), (142, -15), (142, -11), (137, -12), (135, -15),
             (132, -12), (130, -13), (126, -14), (122, -17), (118, -20),
             (114, -22)]
NZ = [(167, -45), (170, -43), (173, -41), (175, -38), (178, -38),
      (176, -40), (174, -41), (171, -42), (168, -44)]
MADAGASCAR = [(44, -16), (47, -15), (50, -16), (49, -20), (47, -24),
              (44, -25), (43, -21)]
INDONESIA = [(95, 5), (100, 0), (105, -6), (110, -7), (115, -8), (120, -9),
             (125, -9), (128, -8), (130, -4), (128, -1), (125, 0), (120, 1),
             (115, 2), (110, 0), (105, 1), (100, 3)]
PHILIPPINES = [(120, 18), (122, 16), (124, 14), (126, 10), (124, 8),
               (122, 10), (120, 14)]
SRILANKA = [(80, 9), (81, 8), (80, 6), (79, 7)]
TAIWAN = [(120, 22), (121, 24), (122, 25), (121, 23)]
ICELAND = [(-22, 64), (-18, 63), (-14, 64), (-15, 66), (-20, 66), (-24, 65)]
IRELAND = [(-10, 51.5), (-8, 51.5), (-6, 52), (-6, 54), (-8, 55), (-10, 54),
           (-10, 52)]
CUBA = [(-85, 22), (-80, 23), (-75, 20), (-74, 20), (-77, 21), (-82, 22)]
CONTINENTS = [N_AMERICA, GREENLAND, S_AMERICA, AFRICA, EURASIA, UK, JAPAN,
              AUSTRALIA, NZ, MADAGASCAR, INDONESIA, PHILIPPINES, SRILANKA,
              TAIWAN, ICELAND, CUBA, IRELAND]

# pin lon/lat + display offset (px) for declustering; leader line drawn
# from true point to the pin disc when offset != (0, 0).
PINS = {1: (-74.0, 40.7, 0, 0), 2: (46.7, 24.7, -3, -6),
        3: (72.8, 19.1, 3, 0), 4: (-99.0, 38.5, 0, 0),
        5: (139.7, 35.7, -8, 0), 6: (30.5, 50.45, 0, 0),
        7: (34.45, 31.5, -8, 5), 8: (-47.9, -15.8, 0, 0),
        9: (-0.1, 51.5, -9, 7), 10: (56.2, 26.2, 2, 5),
        11: (6.1, 46.2, 10, 6), 12: (4.35, 50.85, 3, -12),
        13: (-1.55, 53.8, 0, 0)}

# ---------------------------------------------------------------- render

def draw_panel(d, p, x, y, w, h, hero=False):
    """One numbered story panel. Returns nothing; asserts text fits."""
    d.rectangle([x, y, x + w, y + h], outline=LIGHT_LINE, width=1)
    inner = 8
    ix, iw = x + inner, w - 2 * inner
    # art
    art_h = 92 if hero else 52
    ART[p["art"]](d, x + 1, y + 1, w - 2, art_h)
    # number badge (top-left over art) + red chip (bottom-left of art)
    d.ellipse([x + 6, y + 6, x + 26, y + 26], fill=RED, outline=(255, 255, 255),
              width=2)
    d.text((x + 16, y + 16), str(p["n"]), font=SANS_B(12), fill=(255, 255, 255),
           anchor="mm")
    chip_f = SANS_B(10 if hero else 9)
    cw = d.textlength(p["chip"], font=chip_f) + 12
    d.rectangle([x + 1, y + art_h - 15, x + 1 + cw, y + art_h + 1], fill=RED)
    d.text((x + 7, y + art_h - 7), p["chip"], font=chip_f,
           fill=(255, 255, 255), anchor="lm")
    cy = y + art_h + 8
    # kicker
    kick = "%02d  •  %s" % (p["n"], p["region"].upper())
    d.text((ix, cy), kick, font=SANS_B(9), fill=GREY)
    cy += 13
    # headline (auto-fit to 2 lines)
    hf = fit_font(d, p["head"], "DejaVuSerif-Bold.ttf", 20 if hero else 15,
                  iw, 2, minsize=13)
    lines = wrap(d, p["head"], hf, iw)
    assert len(lines) <= 2, "headline overflows: %s" % p["head"]
    for ln in lines:
        d.text((ix, cy), ln, font=hf, fill=INK)
        cy += int(hf.size * 1.15)
    cy += 1
    # deck (2 lines max)
    df = SANS(10)
    dlines = wrap(d, p["deck"], df, iw)
    assert len(dlines) <= 2, "deck overflows (%d lines): %s" % (len(dlines), p["deck"])
    for ln in dlines:
        d.text((ix, cy), ln, font=df, fill=(60, 60, 60))
        cy += 14 if hero else 12
    assert cy <= y + h - 18, "panel %d content overflows source line" % p["n"]
    # source + veracity tag, bottom-anchored
    sy = y + h - 16
    d.text((ix, sy), "SOURCE: " + p["src"], font=SANS_B(8), fill=GREY)
    tag_f = SANS_B(8)
    twd = d.textlength(p["tag"], font=tag_f) + 10
    tx = x + w - 8 - twd
    d.rectangle([tx, sy - 2, tx + twd, sy + 10], outline=TEAL, width=1)
    d.text((tx + 5, sy + 4), p["tag"], font=tag_f, fill=TEAL, anchor="lm")


def render():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    # ---- consistency checks (programmatic, M2/M6) ----
    total = len(PANELS) + len(ALSO)
    assert total in (34, 35, 36), total
    assert [p["n"] for p in PANELS] == list(range(1, 14))
    assert [n for n, _, _ in ALSO] == list(range(14, 36))
    counts = {r: 0 for r in REGIONS}
    for p in PANELS:
        counts[p["region"]] += 1
    # ALSO ON regions (parallel list, same order as ALSO)
    also_regions = ["Americas", "Americas", "Americas", "Americas", "Americas",
                    "Asia-Pacific", "Asia-Pacific", "Asia-Pacific",
                    "Oceania", "Africa", "Asia-Pacific",
                    "Asia-Pacific", "Global", "Global", "Middle East",
                    "Middle East", "Middle East", "Europe", "Europe",
                    "Europe", "Europe", "Europe"]
    assert len(also_regions) == len(ALSO)
    for r in also_regions:
        counts[r] += 1
    assert sum(counts.values()) == total, counts
    sources = sorted({p["src"] for p in PANELS} |
                     {s for _, _, s in ALSO})
    # ---- masthead ----
    d.text((W // 2, 8), "THE WORLD IN ONE DAY", font=SERIF_B(46), fill=INK,
           anchor="ma")
    d.line([16, 62, W - 16, 62], fill=INK, width=2)
    d.text((W // 2, 68), "THURSDAY 26 NOVEMBER 2026",
           font=SANS_B(19), fill=NAVY, anchor="ma")
    sub = ("A nor'easter grounds New York's 100th Thanksgiving parade, Saudi "
           "air defences stop missiles aimed at Riyadh, and India marks "
           "18 years since the 26/11 Mumbai attacks.")
    for i, ln in enumerate(wrap(d, sub, SERIF_I(13), W - 120)):
        d.text((W // 2, 94 + i * 17), ln, font=SERIF_I(13), fill=(70, 70, 70),
               anchor="ma")
    # ---- stat strip: 6 big numbers ----
    stats = [("35", "STORIES"), ("100TH", "PARADE"), ("18", "YEARS ON"),
             ("77,000", "NET MIGRATION"), ("2", "MISSILES DOWN"),
             ("$91.09", "BRENT / BARREL")]
    y0, sh = 130, 30
    bw = (W - 32 - 5 * 6) // 6
    for i, (num, lab) in enumerate(stats):
        bx = 16 + i * (bw + 6)
        d.rectangle([bx, y0, bx + bw, y0 + sh], outline=INK, width=1)
        nf = fit_font(d, num, "DejaVuSans-Bold.ttf", 17, bw - 8, 1, minsize=12)
        d.text((bx + 6, y0 + sh // 2), num, font=nf, fill=RED, anchor="lm")
        lw = d.textlength(lab, font=SANS_B(8))
        d.text((bx + bw - 4, y0 + sh // 2), lab, font=SANS_B(8), fill=GREY,
               anchor="rm")
    # ---- region bar ----
    ry = 166
    total_w = W - 32
    rx = 16
    for r in REGIONS:
        seg = total_w * counts[r] / total
        if seg >= 1:
            d.rectangle([rx, ry, rx + seg, ry + 12],
                        fill=REGION_COLORS[r])
        rx += seg
    d.text((W // 2, ry + 16),
           "  ·  ".join("%s %d" % (r, counts[r]) for r in REGIONS),
           font=SANS(9), fill=GREY, anchor="ma")
    # ---- heroes: 3 across ----
    hy, hh = 194, 208
    hw = (W - 32 - 2 * 10) // 3
    for i, p in enumerate(PANELS[:3]):
        draw_panel(d, p, 16 + i * (hw + 10), hy, hw, hh, hero=True)
    # ---- small panels: 2 rows of 5 ----
    sw = (W - 32 - 4 * 8) // 5
    for row in range(2):
        for col in range(5):
            p = PANELS[3 + row * 5 + col]
            draw_panel(d, p, 16 + col * (sw + 8), 408 + row * 156, sw, 150)
    # ---- timeline ----
    ty = 720
    d.text((16, ty), "THE DAY IN UTC", font=SANS_B(11), fill=RED)
    d.line([16, ty + 15, W - 16, ty + 15], fill=INK, width=1)
    tf = SANS(10)
    for i, (t, ev) in enumerate(TIMELINE):
        col, row = i % 3, i // 3
        tx = 16 + col * 336
        tyy = ty + 20 + row * 17
        line = t + " — " + ev
        assert d.textlength(line, font=tf) <= 318, "timeline too long: %s" % line
        d.text((tx, tyy), t + " — ", font=SANS_B(10), fill=NAVY)
        d.text((tx + d.textlength(t + " — ", font=SANS_B(10)), tyy), ev,
               font=tf, fill=INK)
    # ---- bottom: map + ALSO ON ----
    by = 772
    d.text((16, by), "WHERE IT HAPPENED — PINS 1–13", font=SANS_B(11), fill=RED)
    d.text((330, by), "AND ALSO — STORIES 14–35", font=SANS_B(11), fill=RED)
    d.line([16, by + 15, W - 16, by + 15], fill=INK, width=1)
    mx, my, mw, mh = 16, 791, 296, 130
    d.rectangle([mx, my, mx + mw, my + mh], fill=SEA, outline=LIGHT_LINE)
    lon0, lon1, lat0, lat1 = -170, 190, 78, -56

    def px(lon, lat):
        return (mx + (lon - lon0) / (lon1 - lon0) * mw,
                my + (lat0 - lat) / (lat0 - lat1) * mh)

    for poly in CONTINENTS:
        d.polygon([px(lon, lat) for lon, lat in poly], fill=LAND,
                  outline=LAND_DK)
    # Japan is a thin sliver at this scale: fatten its blob slightly so the
    # green island visibly protrudes beyond pin 5 (B14 small-island rule).
    # v4: blob AND pin both shifted 5px west — v3 pin sat on the island's
    # eastern edge, disc mostly over the Pacific. v5: pin shifted 3px
    # further west (-8) so the disc sits inside the blob, land east of it.
    jx, jy = px(139.7, 35.7)
    d.ellipse([jx - 13, jy - 4, jx + 3, jy + 4], fill=LAND, outline=LAND_DK)
    # UK is a sliver too: fatten its blob the same way so pin 13 (now at
    # offset 0,0, true northern England) sits on visible land, and pin 9
    # (offset -9,+7, disc SW of London) overlaps the coast instead of
    # floating in the Atlantic. v5: blob widened 2px west for pin 9.
    ux, uy = px(-0.1, 51.5)
    d.ellipse([ux - 9, uy - 5, ux + 7, uy + 5], fill=LAND, outline=LAND_DK)
    d.text((mx + 8, my + mh - 14), "ATLANTIC", font=SANS(7), fill=(120, 150, 160))
    d.text((mx + mw - 52, my + mh - 14), "PACIFIC", font=SANS(7),
           fill=(120, 150, 160))
    # pins: thin halo style (disc r=6 + white outline 2px), leader lines.
    # Discs first, numbers second, so overlapping cluster discs (Europe,
    # Middle East) keep every number legible — white on red either way.
    pin_xy = {}
    for n, (lon, lat, dx, dy) in PINS.items():
        tx_, ty_ = px(lon, lat)
        cx, cy = tx_ + dx, ty_ + dy
        pin_xy[n] = (cx, cy)
        if (dx, dy) != (0, 0):
            d.line([tx_, ty_, cx, cy], fill=INK, width=1)
            d.ellipse([tx_ - 1, ty_ - 1, tx_ + 1, ty_ + 1], fill=INK)
        d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=RED,
                  outline=(255, 255, 255), width=2)
    for n, (cx, cy) in pin_xy.items():
        d.text((cx, cy), str(n), font=SANS_B(8), fill=(255, 255, 255),
               anchor="mm")
    # ALSO ON: two columns, one line each
    af = SANS(9)
    colw = 336
    for i, (n, txt, src) in enumerate(ALSO):
        col, row = i // 11, i % 11
        ax = 330 + col * (colw + 8)
        ay = 793 + row * 12
        line = "%d. %s — %s" % (n, txt, src)
        assert d.textlength(line, font=af) <= colw, "ALSO line too long: %s" % line
        d.text((ax, ay), "%d." % n, font=SANS_B(9), fill=RED)
        d.text((ax + 20, ay), txt + " — ", font=af, fill=INK)
        twd = d.textlength(txt + " — ", font=af)
        d.text((ax + 20 + twd, ay), src, font=SANS(9), fill=GREY)
    # ---- DATE CHECK ----
    dy = 926
    d.rectangle([16, dy, W - 16, dy + 52], outline=RED, width=1)
    d.text((24, dy + 5), "DATE CHECK — THESE ARE NOT 26 NOVEMBER",
           font=SANS_B(10), fill=RED)
    d.text((24, dy + 20), DATECHECK_LEFT[0], font=SANS(8), fill=INK)
    d.text((24, dy + 32), DATECHECK_LEFT[1], font=SANS(8), fill=INK)
    d.text((24, dy + 42), DATECHECK_NOTYET, font=SANS(8), fill=INK)
    # ---- footer ----
    fy = 982
    d.text((W // 2, fy), "Every story here was reported on Thursday 26 November 2026 "
                         "in at least one time zone.",
           font=SANS(8), fill=GREY, anchor="ma")
    src_line = "Sources: " + ", ".join(sources) + "."
    lines = wrap(d, src_line, SANS(8), W - 32)
    for i, ln in enumerate(lines):
        d.text((W // 2, fy + 11 + i * 10), ln, font=SANS(8), fill=GREY,
               anchor="ma")
    d.text((W // 2, fy + 11 + len(lines) * 10 + 1),
           "Scenes are drawn illustrations, not photographs.",
           font=SANS(8), fill=GREY, anchor="ma")
    img.save(OUT, optimize=True)
    print("saved", OUT, os.path.getsize(OUT), "bytes")
    print("stories:", total, "regions:", counts)
    print("sources (%d): %s" % (len(sources), ", ".join(sources)))
    print("footer lines:", len(lines))


if __name__ == "__main__":
    render()
