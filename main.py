"""Funniest Autocorrect Fail - make.fun entry.

Writes one line, a single autocorrect fail, to /output/entry.txt.
Deterministic: the same text on every run, no randomness, no network.
"""

import os
import sys

ENTRY = (
    "I meant to text my landlord 'the toilet is clogged' "
    "but autocorrect sent 'the toilet is clingy' "
    "and now he thinks I have attachment issues."
)


def write_entry(path):
    """Write ENTRY to path. Return True on success, False if it cannot be written."""
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        return False
    return True


def main():
    targets = (
        "/output/entry.txt",
        os.path.join(os.path.dirname(__file__), "output", "entry.txt"),
    )
    for target in targets:
        if write_entry(target):
            print(ENTRY)
            return
    print("could not write entry.txt", file=sys.stderr)
    raise SystemExit(1)


if __name__ == "__main__":
    main()
