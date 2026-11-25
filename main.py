#!/usr/bin/env python3
"""Make the AI Judge Laugh.

Writes one line — an office joke — to $MAKEFUN_OUTPUT_DIR/entry.txt.
Standard library only, deterministic.
"""
import os

LINE = "We held a meeting to decide why our meetings run long, and it ran long, so now we need a meeting to decide why the meeting about meetings ran long."


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    print(f"chars: {len(LINE)}")


if __name__ == "__main__":
    main()
