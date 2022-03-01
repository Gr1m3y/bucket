import pyfastx
import sys
from collections import Counter

def get_dist(faa_in):
    """prints table of all amino acid distributions (by proportion)"""
    distributions = {}

    for name, seq in pyfastx.Fasta(faa_in, build_index=False):
        counts = Counter(seq)
        length = len(seq)
        for aa in counts:
            if aa not in distributions:
                distributions[aa] = []
            distributions[aa].append(float(counts[aa]/length))

    for aa in distributions:
        dist = "\t".join(str(c) for c in distributions[aa])
        print(f"{aa}\t{dist}")


def main():
    get_dist(sys.argv[1])


if __name__ == "__main__":
    main()
