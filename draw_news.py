#!/usr/bin/env python3
"""Draw the news-image-20261125 front page: one 1024x1024 PNG summing up
Wednesday 25 November 2026 from reporting published 24-25 November 2026.

Every story below is a verified fact from a named source. No claim without
a source is drawn. Run: python3 draw_news.py  ->  writes entry.png next to
this file. Fully deterministic: same input, same bytes, every run.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 236)
INK = (20, 24, 34)
NAVY = (20, 33, 61)
RED = (178, 34, 34)
GOLD = (201, 162, 39)
GREY = (90, 92, 98)
LIGHT_LINE = (205, 198, 182)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap measured in pixels."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, color, max_w, leading):
    lines = wrap(draw, text, fnt, max_w)
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=color)
        y += leading
    return y


def rule(draw, x0, y, x1, color, width=2):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Outer frame.
    d.rectangle([10, 10, W - 11, H - 11], outline=NAVY, width=5)
    d.rectangle([18, 18, W - 19, H - 19], outline=LIGHT_LINE, width=1)

    # ---- Masthead -------------------------------------------------------
    d.rectangle([22, 22, W - 23, 150], fill=NAVY)
    d.text((W // 2, 40), "THE WORLD IN ONE PAGE",
           font=font(SERIF_B, 54), fill=(255, 255, 255), anchor="ma")
    d.text((W // 2, 106), "WEDNESDAY  ·  25 NOVEMBER 2026",
           font=font(SANS_B, 24), fill=GOLD, anchor="ma")
    d.rectangle([22, 150, W - 23, 158], fill=RED)

    # ---- Lead story -----------------------------------------------------
    x = 48
    y = 174
    d.text((x, y), "CYBERATTACK  ·  WASHINGTON", font=font(SANS_B, 20), fill=RED)
    y += 30
    y = para(d, x, y, "US spy agencies hit by cyber breach",
             font(SERIF_B, 46), INK, W - 2 * x, 54)
    y += 6
    y = para(d, x, y,
             "CNN reported on 25 November that the CIA and the Office of the "
             "Director of National Intelligence appear to have been hit by a "
             "cyberattack \u2014 the latest in a string of breaches hitting "
             "US government and business.",
             font(SANS, 23), (52, 54, 62), W - 2 * x, 30)
    y += 4
    d.text((x, y), "Sources: CNN, Reuters", font=font(SANS_B, 18), fill=GREY)
    y += 26

    # ---- Two-by-two story grid ------------------------------------------
    rule(d, 48, y, W - 48, INK, 3)
    y += 14
    col_w = 452
    col_x = [48, 524]
    stories = [
        ("TRADE SECRETS  ·  NEW YORK", RED,
         "Huawei found guilty of stealing trade secrets",
         "A New York jury found Huawei guilty on 10 of 12 counts, including "
         "trade-secret theft. Huawei rejected the verdict.",
         "Sources: AFP, US Dept. of Justice"),
        ("WAR IN UKRAINE  ·  GULF OF FINLAND", RED,
         "Kyiv confirms strike on Russian ship",
         "Zelenskiy confirmed Ukraine\u2019s drone strike on a Russian cargo "
         "ship in the Gulf of Finland. Ally Norway urged caution.",
         "Source: Reuters"),
        ("YEMEN  ·  RIYADH", RED,
         "Houthi drone hits Riyadh\u2019s tallest tower",
         "A Houthi drone struck Riyadh\u2019s tallest tower, wounding 11, "
         "Saudi civil defence said.",
         "Sources: Reuters, Saudi civil defence"),
        ("CHINA  ·  SHANGHAI", RED,
         "Shanghai party chief under corruption probe",
         "Chen Jining, 62, Shanghai\u2019s party chief, was placed under "
         "investigation, Xinhua said.",
         "Sources: Xinhua, CNN"),
    ]
    head_f = font(SERIF_B, 27)
    body_f = font(SANS, 19)
    src_f = font(SANS_B, 15)

    def cell_height(head, body):
        hh = len(wrap(d, head, head_f, col_w)) * 32
        bh = len(wrap(d, body, body_f, col_w)) * 25
        return 24 + hh + 2 + bh + 2 + 18

    for row in range(2):
        pair = stories[row * 2:(row + 1) * 2]
        rh = max(cell_height(s[2], s[3]) for s in pair)
        for i, (kick, kc, head, body, src) in enumerate(pair):
            cx = col_x[i]
            cy = y
            d.text((cx, cy), kick, font=font(SANS_B, 16), fill=kc)
            cy = para(d, cx, cy + 24, head, head_f, INK, col_w, 32)
            cy = para(d, cx, cy + 2, body, body_f, (52, 54, 62), col_w, 25)
            d.text((cx, cy + 2), src, font=src_f, fill=GREY)
        y += rh + 12
    rule(d, 48, y, W - 48, INK, 3)
    y += 16

    # ---- Also today ------------------------------------------------------
    d.text((48, y), "ALSO TODAY", font=font(SANS_B, 20), fill=NAVY)
    y += 30
    items = [
        "Sarkozy corruption case \u2014 ex-president and wife Carla Bruni "
        "\u2014 ordered to trial in France; first hearing 1 April 2027. "
        "(Reuters)",
        "Trump pardons Thanksgiving turkeys \u201cFreedom\u201d and "
        "\u201cFeathers\u201d. (Reuters)",
        "England beat Australia by eight wickets in the second T20I, chasing "
        "185 to level the series. (Reuters)",
        "Today is the International Day for the Elimination of Violence "
        "against Women. (UN)",
    ]
    for it in items:
        d.text((48, y), "\u25aa", font=font(SANS_B, 19), fill=RED)
        y = para(d, 74, y, it, font(SANS, 20), INK, W - 122, 26)
        y += 5

    # ---- Footer ----------------------------------------------------------
    fy = H - 44
    rule(d, 48, fy, W - 48, LIGHT_LINE, 2)
    fy += 10
    d.text((W // 2, fy), "All stories verified from reporting published "
           "24\u201325 November 2026  ·  One page. One day.",
           font=font(SANS, 16), fill=GREY, anchor="ma")

    img.save("entry.png", "PNG")
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
