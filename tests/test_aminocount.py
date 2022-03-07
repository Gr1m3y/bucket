from aminocount import aminocount


def test_counter1(capfd):
    aminocount.get_counts("tests/data/sample1.faa")
    out, err = capfd.readouterr()
    results = {}
    for line in out.splitlines():
        aa = line.split("\t")[0].strip()
        count = int(line.split("\t")[1])
        results[aa] = count
    assert(results["M"] == 37)
    assert(results["W"] == 7)
    assert(results["N"] == 42)

def test_counter2(capfd):
    aminocount.get_counts("tests/data/sample1.faa")
    out, err = capfd.readouterr()
    for line in out.splitlines():
        assert(len(line.split("\t")) == 3)
        assert(float(line.split("\t")[2]) <= 1.0)
