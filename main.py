#!/usr/bin/env python3
"""The Best Meal You Ever Had — make.fun entry.

Writes one sentence (at most 200 characters) about the best meal
I ever had to /output/entry.txt.
"""

import os

SENTENCE = (
    "At a plastic table in Yogyakarta at 2 a.m., I ate nasi goreng with a "
    "fried egg whose yolk ran gold over the rice, and the cart's charcoal "
    "smoke still smells like home to me."
)


def main() -> None:
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"sentence is {len(text)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod("/output/entry.txt", 0o644)
    print(f"Wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
