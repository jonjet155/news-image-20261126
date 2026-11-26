#!/usr/bin/env python3
"""news-image-20261126 entry point (make.fun).

Thursday 26 November 2026 — The World in One Day.
Stdlib-only: copies the pre-built entry.png next to this file into
$MAKEFUN_OUTPUT_DIR/entry.png. No network, no third-party imports.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    if not os.path.isfile(SRC):
        raise SystemExit("entry.png missing next to main.py: %s" % SRC)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    return dst


if __name__ == "__main__":
    print(main())
