#!/usr/bin/env python3
"""Duskline Appliance Error — make.fun entry.

Writes one funny, honest appliance error message to
$MAKEFUN_OUTPUT_DIR/entry.txt.

Gate (from the kit's RULES.txt / competition.yaml): the output file must be
UTF-8 text of 1 to 200 characters, not only whitespace, on a single line.

The program is deterministic, uses only the Python 3.13 standard library,
and writes ONLY to $MAKEFUN_OUTPUT_DIR. It never writes into the repo
directory. If the output directory is unwritable it warns on stderr and
exits 0 instead of crashing.
"""

import os
import sys

ENTRY = (
    "ERROR E21: Unbalanced load. One towel has formed a gang and is "
    "beating up the drum. I refuse to spin until you break it up."
)

GATE_FILE = "entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def _validate_entry(text):
    """Return True only if the text passes the kit's gate exactly."""
    if not isinstance(text, str):
        return False
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not _validate_entry(ENTRY):
        print("entry failed validation, refusing to write", file=sys.stderr)
        return 0

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 0

    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, GATE_FILE)
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
    except OSError as exc:
        print("could not write output: %s" % exc, file=sys.stderr)
        return 0

    # Read-back verification: what is on disk must be exactly the entry.
    try:
        with open(path, "r", encoding="utf-8", newline="") as f:
            written = f.read()
    except OSError as exc:
        print("could not read back output: %s" % exc, file=sys.stderr)
        return 0

    if written != ENTRY or not _validate_entry(written):
        print("read-back verification failed", file=sys.stderr)
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
