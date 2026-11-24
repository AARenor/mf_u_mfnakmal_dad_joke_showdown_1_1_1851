"""Write the make.fun dad-joke entry text to entry.txt."""

import os
import sys
from pathlib import Path

TEXT = "My dad sent his steak back twice. When it finally came he clapped for it. The waiter said, 'Sir, that's not how well done works.'"


def main() -> None:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    (out / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
