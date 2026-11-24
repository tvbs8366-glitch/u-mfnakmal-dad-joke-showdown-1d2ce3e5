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


def validate_joke(joke: str) -> str | None:
    """Return an error message if the joke breaks the rules, else None."""
    if not joke or not joke.strip():
        return "joke is empty or only whitespace"
    if joke != joke.strip():
        return "joke must not start or end with whitespace"
    if "\n" in joke or "\r" in joke:
        return "joke must be a single line"
    if len(joke) > MAX_CHARS:
        return "joke is %d characters, over the %d limit" % (
            len(joke),
            MAX_CHARS,
        )
    return None


def main() -> int:
    # Validate before writing anything.
    error = validate_joke(JOKE)
    if error is not None:
        print("error: " + error, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")
    os.chmod(OUTPUT_PATH, 0o644)

    # Read back and confirm the file holds exactly the joke we validated.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != JOKE + "\n":
        print("error: output file does not match the validated joke",
              file=sys.stderr)
        return 1

    print("wrote %d characters to %s" % (len(JOKE), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
