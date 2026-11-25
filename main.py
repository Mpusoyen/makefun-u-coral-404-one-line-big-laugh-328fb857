"""One Line, Big Laugh — make.fun entry u-coral-404-one-line-big-laugh-328fb857.

Writes a single hilarious line to entry.txt for pairwise judging.
"""

import os

LINE = "My cat gets prescription salmon, filtered water, and a $90 vet visit for one sneeze; I googled my 2:47 a.m. chest pain and clicked 'I'm Feeling Lucky.'"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
