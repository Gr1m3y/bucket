from aminocount import aminocount


def test_counter(capfd):
    aminocount.get_counts("tests/data/sample.faa")
    out, err = capfd.readouterr()
    results = {}
    for line in out.splitlines():
        aa = line.split("\t")[0].strip()
        count = int(line.split("\t")[1])
        results[aa] = count
    assert(results["M"] == 37)
    assert(results["W"] == 7)
    assert(results["N"] == 42)
