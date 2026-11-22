"""Make the AI judge feel curious — entry program (Python 3.13).

Writes one short text to /output/entry.txt: a quiet scene with one
small detail that does not quite fit, so the reader is left holding
a calm, open question. No network, no dependencies, deterministic.
"""

import os

TEXT = (
    "The lighthouse at the end of the bay blinks twice, then once, "
    "then twice again \u2014 a pattern no sailor wrote down and no keeper "
    "remembers setting. On still evenings, the light seems to pause, "
    "as if listening for an answer."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
