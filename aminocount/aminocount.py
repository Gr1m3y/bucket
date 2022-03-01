import pyfastx
import sys
from collections import Counter


def get_counts(faa_in):
    """prints count of all amino acids in faa_in, in tsv format"""
    all_proteins = ""
    for name, seq in pyfastx.Fasta(faa_in, build_index=False):
        seq = seq.strip()
        all_proteins = f"{all_proteins}{seq}"
    counts = Counter(all_proteins)
    total = sum(counts.values())
    for aa in counts:
        proportion = counts[aa] / float(total)
        print(f"{aa}\t{counts[aa]}\t{proportion:.3f}")


def main():
    get_counts(sys.argv[1])


if __name__ == "__main__":
    main()
