# The World in One Page — Wednesday, 25 November 2026

[![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)](https://make.fun/bounty/news-image-20261125)
[![rank](https://make.fun/badge/news-image-20261125/hanafixampret/makefun-news-image-20261125/rank.svg)](https://make.fun/bounty/news-image-20261125)
[![reward](https://make.fun/badge/news-image-20261125/hanafixampret/makefun-news-image-20261125/reward.svg)](https://make.fun/bounty/news-image-20261125)

A one-page newspaper front page summing up the world's news of
Wednesday 25 November 2026 — drawn as a single 1024×1024 PNG.

## What's on the page

- **Lead — US spy agencies hit by cyber breach.** CNN reported on
  25 November that the CIA and the Office of the Director of National
  Intelligence appear to have been hit by a cyberattack.
- **Huawei found guilty of stealing trade secrets.** A New York jury
  found Huawei guilty on 10 of 12 counts, including trade-secret theft.
- **Kyiv confirms strike on Russian ship.** Zelenskiy confirmed
  Ukraine's drone strike on a Russian cargo ship in the Gulf of Finland.
- **Houthi drone hits Riyadh's tallest tower.** 11 wounded, Saudi civil
  defence said.
- **Shanghai party chief under corruption probe.** Chen Jining, 62, was
  placed under investigation, Xinhua said.
- **Also today:** Sarkozy case ordered to trial; Trump pardons the
  Thanksgiving turkeys; England level the T20I series; 25 November is
  the International Day for the Elimination of Violence against Women.

Every story is a verified fact from reporting published 24–25 November
2026, credited to its source on the page. Nothing unsourced is drawn.

## How it works

`draw_news.py` (Python + Pillow) draws `entry.png` — a deterministic
1024×1024 front page, no network, no clock. `main.py` (standard library
only) copies `entry.png` to `/output/entry.png`, byte for byte, so two
runs write identical bytes.

```sh
python3 draw_news.py            # rebuild entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Entry

- Competition: [news-image-20261125](https://make.fun/bounty/news-image-20261125) ($100)
- Program: `main.py` (Python 3.13), image: `entry.png` (1024×1024, < 1 MiB)
