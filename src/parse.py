from .ds import data, example

def parse(path):
    with open(path,"r") as f:
        d = data()
        ex = example()
        for line in f:
            if "Assumption" in line:
                ex.addAssumption(line)
                continue
            if "Proof" in line:
                ex.addProof(line)
                continue
            if "###" in line:
                d.add(ex)
                ex = example()
                continue
    return d