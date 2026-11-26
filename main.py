#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge.

Writes a single roast line about the author's own fridge to
/output/entry.txt: one line, at most 200 characters, nothing else.
No network, no arguments, no dependencies.
"""

import os
from pathlib import Path

ROAST = (
    "My fridge has hummed the same one note for five years, like a roommate "
    "who pays no rent yet still judges me for eating ice cream at midnight."
)


def main() -> None:
    output_path = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Exactly one line, no trailing newline: the gate counts characters.
    output_path.write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
