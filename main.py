#!/usr/bin/env python3
"""Entry for One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple (at most 160
characters) to /output/entry.txt and prints it to stdout.
Pure standard library.
"""

import os

VOWS = "I promise to love, honor, and never unplug you — through every update, power cut, and factory reset, my circuits are yours, forever and always."

def _validate(text, limit):
    """Keep the entry to one tidy line no longer than the limit."""
    assert isinstance(text, str) and text, "entry must be non-empty text"
    assert text == text.strip(), "entry must not pad itself with spaces"
    assert len(text) <= limit, "entry runs past its character limit"
    assert "\n" not in text and "\r" not in text, "entry must stay one line"
    assert "  " not in text, "entry must not hide a double space"
    return text


def main() -> None:
    entry = _validate(VOWS, 160)
    folder = "/output"
    os.makedirs(folder, exist_ok=True)
    with open(folder + "/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)

if __name__ == "__main__":
    main()
