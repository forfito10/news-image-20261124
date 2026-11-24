#!/usr/bin/env python3
"""news-image-20261124 entry: write the 24 November 2026 world-news image.

Reads the committed entry.png.b64.part0..5 (base64 of the finished 1024x1024
PNG, split only because the GitHub API tools cap a single file argument),
decodes them and writes the image to /output/entry.png. No network, no
randomness, no timestamps: the same bytes on every run.
"""
import base64
import glob
import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    chunks = []
    for path in sorted(glob.glob(os.path.join(here, "entry.png.b64.part*"))):
        with open(path, "r", encoding="ascii") as f:
            chunks.append(f.read())
    data = base64.b64decode("".join(chunks))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.png", "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
