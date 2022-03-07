from aminodist import aminodist

def test_dist1(capfd):
    aminodist.get_dist("tests/data/sample2.faa")
    out, err = capfd.readouterr()
    results = {}
    for line in out.splitlines():
        aa = line.split("\t")[0].strip()
        count = float(line.split("\t")[1])
        results[aa] = count
    assert(results["C"] == 0.25)
    assert(results["M"] == 0.25)
    assert(results["H"] == 0.5)
    assert("W" not in results)