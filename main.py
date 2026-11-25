#!/usr/bin/env python3
"""news-image-20261125 entrypoint (Python 3.13, standard library only).

Copies the front page built by draw_news.py — entry.png, stored beside
this file — to /output/entry.png. Outside the grading sandbox,
MAKEFUN_OUTPUT_DIR stands in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The copy is byte for byte, so two runs write identical bytes. No network,
no randomness, no clock: the image is fixed at build time.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
print("wrote", OUT / "entry.png")
