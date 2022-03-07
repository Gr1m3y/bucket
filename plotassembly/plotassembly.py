from typing import Any

import sys
import pyfastx
import matplotlib.pyplot as plt


def build_table(faa_in: str) -> str:
    lengths = []
    for name, seq in pyfastx.Fasta(faa_in, build_index=False):
        length = len(seq)
        lengths.append(length)
    return lengths


def main():
    lengths: list = build_table(str(sys.argv[1]))
    plt.hist(lengths)
    plt.show()


if __name__ == "__main__":
    main()
