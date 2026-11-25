#!/usr/bin/env python3
"""One-Liner Marathon — make.fun program/v1 entry.

Writes a single one-line comedy joke, up to 280 characters, to
/output/entry.txt. Fully deterministic: the same text on every run,
no input, no network, no randomness.
"""

import os

JOKE = (
    "I told my smart speaker I wanted privacy, so it started charging "
    "me $9.99 a month to ignore me."
)

MAX_CHARS = 280  # the gate refuses /output/entry.txt over 280 characters


def main() -> None:
    # Fail loudly instead of silently submitting an over-long joke.
    if not 1 <= len(JOKE) <= MAX_CHARS:
        raise SystemExit(
            f"joke is {len(JOKE)} chars, must be 1-{MAX_CHARS}"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Exact bytes, no trailing newline: the gate counts characters.
    # Write directly to entry.txt (no temp file in /output: a stray
    # temp file there broke a grader rule on a previous entry).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
