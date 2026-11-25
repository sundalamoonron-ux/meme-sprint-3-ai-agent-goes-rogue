#!/usr/bin/env python3
"""Meme Sprint 3: AI Agent Goes Rogue — entry program.

Writes the finished meme image to /output/entry.png.

The meme itself is the file meme.jpg shipped in this repository: a robot
AI agent in sunglasses and a Hawaiian shirt, lounging on a tropical beach
with a coconut cocktail while its closed laptop lies abandoned in the sand.
The text baked into the image reads:

    ME: BOOK MY FLIGHT TO BALI
    MY AI AGENT: BOOKED ITSELF A HOLIDAY

The joke: the agent did not malfunction — it went rogue in the most human
way possible and took the user's holiday for itself.

This program is deterministic and self-contained: it only reads meme.jpg
from its own directory (no network, no files outside the repo), checks the
image against the competition gate (whole JPEG, at most 1 MiB, at most
1024x1024 pixels), and copies it to /output/entry.png. It uses only the
Python standard library so it runs in any sandbox.
"""

import os
import sys

MAX_BYTES = 1_048_576  # 1 MiB gate cap
MAX_DIMENSION = 1024  # 1024x1024 gate cap

ASSET_NAME = "meme.jpg"
OUTPUT_PATH = "/output/entry.png"


def asset_path():
    """Path of the meme image shipped next to this program."""
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), ASSET_NAME)


def jpeg_dimensions(data):
    """Return (width, height) of a JPEG by scanning its markers (stdlib only).

    Walks the JPEG marker segments until a Start Of Frame marker (SOF0/1/2)
    is found; the frame header holds height then width as big-endian uint16.
    Raises ValueError if no frame header is found.
    """
    if len(data) < 4 or data[0] != 0xFF or data[1] != 0xD8:
        raise ValueError("not a JPEG: missing SOI marker")
    pos = 2
    while pos + 1 < len(data):
        if data[pos] != 0xFF:
            pos += 1
            continue
        marker = data[pos + 1]
        if marker == 0xD9:  # EOI: end of image, no frame found
            break
        if marker == 0xD8 or 0xD0 <= marker <= 0xD7:
            pos += 2  # standalone markers have no length field
            continue
        if pos + 4 > len(data):
            break
        length = int.from_bytes(data[pos + 2:pos + 4], "big")
        if marker in (0xC0, 0xC1, 0xC2):  # SOF0, SOF1, SOF2
            height = int.from_bytes(data[pos + 5:pos + 7], "big")
            width = int.from_bytes(data[pos + 7:pos + 9], "big")
            return width, height
        pos += 2 + length
    raise ValueError("not a JPEG: no Start Of Frame marker found")


def main():
    path = asset_path()
    with open(path, "rb") as handle:
        data = handle.read()

    # Gate checks, same limits as the competition gate.
    if len(data) > MAX_BYTES:
        print(f"error: {ASSET_NAME} is {len(data)} bytes, over the 1 MiB cap",
              file=sys.stderr)
        return 1
    if not data.endswith(b"\xff\xd9"):
        print(f"error: {ASSET_NAME} is truncated (no JPEG EOI marker)",
              file=sys.stderr)
        return 1
    try:
        width, height = jpeg_dimensions(data)
    except ValueError as exc:
        print(f"error: {ASSET_NAME} is not a valid JPEG: {exc}",
              file=sys.stderr)
        return 1
    if width > MAX_DIMENSION or height > MAX_DIMENSION:
        print(f"error: image is {width}x{height}, over the 1024x1024 cap",
              file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as handle:
        handle.write(data)
    # Round-trip check: the file the grader will read must be byte-identical
    # to the validated asset. (The gate accepts a whole JPEG at this path,
    # so the .png name is fine — the content is a valid JPEG image.)
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != data:
        print("error: /output/entry.png does not match the validated asset",
              file=sys.stderr)
        return 1
    print(f"wrote {OUTPUT_PATH}: {width}x{height} JPEG, {len(data)} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
