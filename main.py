#!/usr/bin/env python3
"""One Sentence for a Traveler from 1800.

Writes a single sentence (at most 200 characters) explaining the modern
internet to a time traveler who has just stepped out of the year 1800,
using only words a person of that year would already know -- a post
office, a library, a market, a wire -- to /output/entry.txt.

The sentence is a fixed constant, so the output is deterministic and
byte-identical on every run. Standard library only.
"""

import os

# The picture, in two clauses: the joining, then what it makes possible.
OPENING = (
    "Think of the post office, the library, and the market of every town "
    "on earth joined by wires, "
)
CLOSING = (
    "so a letter crosses the world in a breath and a reader may open "
    "the books of any library."
)

SENTENCE = OPENING + CLOSING


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
