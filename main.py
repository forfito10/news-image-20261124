#!/usr/bin/env python3
"""news-image-20261124 entry: write the 24 November 2026 world-news image.

Decodes the committed entry.png.b64 (base64 of the finished 1024x1024 PNG)
and writes it to /output/entry.png. No network, no randomness, no
timestamps: the same bytes on every run.
"""
import base64
import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.png.b64"), "r", encoding="ascii") as f:
        data = base64.b64decode(f.read())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.png", "wb") as f:
        f.write(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
