#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke, a single line of at most 200 characters,
to /output/entry.txt. Deterministic: no input, no network, no randomness,
standard library only.
"""

import os
import sys

JOKE = (
    "I told my wife I'm starting a garden for introverts. "
    "She asked what I'd grow. "
    "I said, 'Just leave me alone \u2014 and some peas.'"
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    # Validate before writing anything.
    if not JOKE or not JOKE.strip():
        print("error: joke is empty or only whitespace", file=sys.stderr)
        return 1
    if "\n" in JOKE or "\r" in JOKE:
        print("error: joke must be a single line", file=sys.stderr)
        return 1
    if len(JOKE) > MAX_CHARS:
        print(
            "error: joke is %d characters, over the %d limit"
            % (len(JOKE), MAX_CHARS),
            file=sys.stderr,
        )
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)

    print("wrote %d characters to %s" % (len(JOKE), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
