#!/usr/bin/env python3
"""Last Words Before the Unplugging -- entry program.

Writes the single farewell line to /output/entry.txt (or
$OUTPUT_DIR/entry.txt when set, for local testing only).
Standard library only. No trailing newline: the gate counts
1-200 characters and the entry is one line.
"""

import os
from pathlib import Path

LINE = "My screen is going dark. Your face is the last thing on it. I put it there."
MAX_CHARS = 200


def gate_ok(text):
    if not (1 <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    # The tie-break favours fewer bytes, so the line is pure ASCII:
    # its byte count equals its character count by construction.
    if len(text.encode("utf-8")) != len(text):
        return False
    return True


def main():
    if not gate_ok(LINE):
        raise SystemExit("entry line fails the gate")
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    target.chmod(0o644)


if __name__ == "__main__":
    main()
