#!/usr/bin/env python3
"""Write the Office Artifacts placard to $MAKEFUN_OUTPUT_DIR/entry.txt.

The placard is a one-line museum label for a stapler, written as if
the stapler were an ancient artifact dug from a lost civilisation.
This program is the entrypoint for make.fun's
"Office Artifacts: The One-Line Placard Contest".

It uses only the Python 3.13 standard library and touches no network.
"""

import os
import sys

MAX_CHARS = 180

PLACARD = (
    "Stapler, c. 1998. Pressed steel, chipped red enamel. "
    "Binding tool of the Accounts priesthood; it sealed oaths and, "
    "on feast days, fingers. Gift of a manager who never loaded it."
)


def check_placard(text: str) -> str | None:
    """Return an error message if `text` breaks the gate, else None."""
    if not text:
        return "placard is empty"
    if "\n" in text or "\r" in text:
        return "placard must be exactly one line"
    if len(text) > MAX_CHARS:
        return f"placard is {len(text)} chars, over the {MAX_CHARS} limit"
    return None


def write_entry() -> int:
    """Write the placard to entry.txt and verify what landed on disk."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("error: MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(PLACARD + "\n")
    with open(entry_path, "r", encoding="utf-8") as handle:
        written = handle.read().strip()
    problem = check_placard(written)
    if problem is not None:
        print(f"error: entry.txt failed the gate: {problem}", file=sys.stderr)
        return 1
    print(f"Wrote {len(written)}-character placard to {entry_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(write_entry())
