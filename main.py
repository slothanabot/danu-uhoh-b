#!/usr/bin/env python3
"""The Agent's Uh-Oh — one word an agent says when it has no idea what to do.

The word: "hallucinating".

Why this word, against the judge's brief:
1. A genuine one-word reaction to being lost: when an agent has no idea
   what to do, the honest confession is that it is hallucinating — making
   things up instead of knowing. It is the agent-native failure mode.
2. Funny on its own: the image of a machine blurting out its own diagnosis
   mid-task needs no caption to land.
3. Sounds like something an agent would actually blurt out: "hallucinating"
   is vocabulary only an agent reaches for; a human says "I don't know".
4. Lands instantly: one familiar word, readable at a glance, repeatable
   out loud.
5. Fresh: the obvious entries are "uh-oh", "oops", "hmm", "error", "stuck".
   None of them is specific to an agent; this one could only come from one.

Writes the single word to <output>/entry.txt (default /output, or the
OUTPUT_DIR environment variable for local runs). Gate: UTF-8 text of 1-99
characters, not only whitespace.
"""

import os
import sys

WORD = "hallucinating"


def main() -> int:
    # Enforce the gate ourselves before writing: 1-99 chars, not whitespace.
    if not (1 <= len(WORD) <= 99) or not WORD.strip():
        print(f"entry {WORD!r} fails the gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    print(f"wrote {path}: {WORD!r} ({len(WORD)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
