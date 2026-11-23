"""Make the Judge Smile — entry program.

Writes one line (<=200 chars) to /output/entry.txt: a small good thing
that happened today. Stdlib only, deterministic.
"""
import os

TEXT = (
    "My neighbour left a mango on my doorstep with a note that just said "
    "'too many' \u2014 I ate it standing in the hallway, juice on my chin, "
    "grinning like I'd won something."
)


def main():
    # Enforce the scorer's gate (RULES.txt): UTF-8, 1-200 chars, one line,
    # not whitespace-only. Fail loudly instead of writing an invalid entry.
    # Also refuse control characters (other than none present here): a
    # stray \x00-\x1f would fail the scorer's UTF-8 text check.
    if not 1 <= len(TEXT) <= 200 or "\n" in TEXT or not TEXT.strip():
        raise SystemExit("entry text violates the 1-200 char single-line gate")
    if any(ord(c) < 0x20 for c in TEXT):
        raise SystemExit("entry text contains a control character")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
