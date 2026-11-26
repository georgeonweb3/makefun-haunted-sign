"""Funniest Sign on a Haunted Server Room Door.

Writes one line, the funniest sign for the door of a haunted server
room, to /output/entry.txt. The line is fixed and deterministic: the
same bytes on every run, so the two grader runs match.

Gate (competition rules): /output/entry.txt must be UTF-8 text of
1 to 120 characters, not only whitespace.
"""

import os

MAX_CHARS = 120

ENTRY = (
    "NO FOOD IN THE SERVER ROOM. "
    "The ghost ate three sandwiches this week and it is still hungry."
)


def validate(text: str) -> None:
    """Enforce the competition gate on a text: 1-120 chars, one line."""
    if not text or not text.strip():
        raise SystemExit("entry is empty")
    if len(text) > MAX_CHARS:
        raise SystemExit("entry exceeds %d characters" % MAX_CHARS)
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")


def main() -> None:
    text = ENTRY
    validate(text)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("read-back mismatch")
    validate(written)


if __name__ == "__main__":
    main()
