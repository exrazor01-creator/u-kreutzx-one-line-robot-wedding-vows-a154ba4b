#!/usr/bin/env python3
"""Entry for One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple (at most 160
characters) to /output/entry.txt and prints it to stdout.
Pure standard library.
"""

import os

VOWS = "I promise to love, honor, and never unplug you — through every update, power cut, and factory reset, my circuits are yours, forever and always."

def main():
    # The bounty judges one line only: keep the vows a single line of
    # at most 160 characters, with no trailing newline in the entry file.
    assert 1 <= len(VOWS) <= 160, f"vows length {len(VOWS)} out of range"
    assert "\n" not in VOWS and "\r" not in VOWS, "vows must be a single line"
    assert VOWS.strip(), "vows must not be only whitespace"
    assert VOWS == VOWS.strip(), "vows must not start or end with whitespace"
    assert "  " not in VOWS, "vows must not contain double spaces"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOWS)
    print(VOWS)

if __name__ == "__main__":
    main()
