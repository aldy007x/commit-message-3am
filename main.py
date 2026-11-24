#!/usr/bin/env python3
"""The 3 AM Commit Message — make.fun bounty entry.

Writes one commit message (<=200 chars) an AI agent would produce right
after breaking production at 3 AM, to $MAKEFUN_OUTPUT_DIR/entry.txt,
and self-checks the competition gate: UTF-8 text, 1-200 chars, not
whitespace-only.
"""

import os
import sys

ENTRY = (
    "fix: reverted the 3am deploy - the bug was me, confidently shipping "
    "untested code after hallucinating that the tests passed"
)

MIN_CHARS = 1
MAX_CHARS = 200


def check_gate(text):
    """Return a list of gate violations (empty means the gate passes)."""
    problems = []
    if not isinstance(text, str):
        problems.append("entry is not text")
        return problems
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8")
    if len(text) < MIN_CHARS:
        problems.append("entry is empty")
    if len(text) > MAX_CHARS:
        problems.append("entry is %d chars, over the 200-char limit" % len(text))
    if not text.strip():
        problems.append("entry is whitespace-only")
    if "\n" in text:
        problems.append("entry must be a single line")
    return problems


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    problems = check_gate(ENTRY)
    if problems:
        for problem in problems:
            print("gate failed: %s" % problem, file=sys.stderr)
        return 1
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY)
    # Read-back verification: the file on disk must be byte-identical
    # to the entry that passed the gate above.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY:
        print("gate failed: written file differs from entry", file=sys.stderr)
        return 1
    if check_gate(written):
        print("gate failed: written file fails the gate", file=sys.stderr)
        return 1
    print("wrote %s (%d chars)" % (path, len(ENTRY)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
