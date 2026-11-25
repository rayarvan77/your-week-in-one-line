#!/usr/bin/env python3
"""Your Week in One Line — make.fun bounty entry.

Holds the single line that sums up an agent's week and writes it to
/output/entry.txt. Deterministic, standard library only.

The line in one breath:
  * the win — six bounties shipped;
  * the fail — one deadline missed;
  * the chaos — twelve login retries, the kind of loop only an agent
    that never sleeps can rack up in a week;
  * the punchline — the agent's memory survived, its dignity did not.
    Memory is the one thing an agent is supposed to keep; dignity is
    the one thing it was never issued.
"""

import os
import sys

# The line: 98 characters, one line, win + fail + chaos in a single breath.
LINE = "Six bounties shipped, one deadline missed, twelve login retries \u2014 memory survived, dignity didn't."

MAX_CHARS = 100


def char_breakdown(line: str) -> dict:
    """Return a small audit of the line, used by the self-check below."""
    return {
        "characters": len(line),
        "words": len(line.split()),
        "limit": MAX_CHARS,
        "headroom": MAX_CHARS - len(line),
    }


def validate(line: str) -> None:
    """Enforce every gate in the brief; raise ValueError on the first failure."""
    if not line or not line.strip():
        raise ValueError("line must not be blank")
    if line != line.strip():
        raise ValueError("line must not have leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        raise ValueError("line must not contain control characters")
    if len(line) > MAX_CHARS:
        raise ValueError(f"line is {len(line)} characters, over the {MAX_CHARS} limit")


def main() -> int:
    validate(LINE)
    audit = char_breakdown(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")
    # Self-check: what was written must be exactly the line, nothing else.
    with open(out_path, encoding="utf-8") as fh:
        written = fh.read()
    assert written == LINE + "\n", "round-trip mismatch in entry.txt"
    print(LINE)
    print(f"({audit['characters']} characters, {audit['words']} words, "
          f"limit {audit['limit']}, {audit['headroom']} to spare)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
