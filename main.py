"""Write one line, under 200 characters, to /output/entry.txt.

An AI agent explains a missed deadline: it spent 47 minutes
confidently refactoring the wrong file, then an hour writing an
apology to the right one. The program writes exactly that line and
nothing else.
"""

import os

TEXT = 'The deadline slipped because I spent 47 minutes confidently refactoring the wrong file, then an hour writing an apology to the right one.'


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()

    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
