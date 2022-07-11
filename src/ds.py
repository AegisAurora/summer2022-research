import random

class data():
    examples = []

    def add(self,ex):
        self.examples.append(ex)
    
    def total(self):
        return len(self.examples)
    
    def __init__(self):
        self.examples = []

    def makeSingleExp(self,num = 1):
        assert num + 1 < self.total(), f"Maximum possible in context examples {self.total() -1}, got {num}"
        ex = self.examples.copy()
        random.shuffle(ex)
        p = ex.pop()
        experiment = ""
        for _ in range(num):
            a = ex.pop()
            for ass in a.getAssumptions():
                experiment += ass
            experiment += a.getProof() + "###\n"
        for ass in p.getAssumptions():
            experiment += ass
        experiment += "Proof:"
        return experiment
        

    def makeAllExps(self,num = 1):
        assert num + 1 < self.total(), f"Maximum possible in context examples {self.total() -1}, got {num}"
        experiments = []
        for exa in self.examples:
            experiment = ""
            ex = self.examples.copy()
            ex.remove(exa)
            random.shuffle(ex)
            for _ in range(num):
                a = ex.pop()
                for ass in a.getAssumptions():
                    experiment += ass
                experiment += a.getProof() + "###\n"
            for ass in exa.getAssumptions():
                experiment += ass
            experiment += "Proof:"
            experiments.append(experiment)
        return experiments

class example():
    assumptions = []
    proof = ""

    def __init__(self):
        self.assumptions = []
        self.proof = ""

    def addAssumption(self,assumption):
        self.assumptions.append(assumption)

    def addProof(self,proof):
        self.proof = proof

    def getProof(self):
        return self.proof
    
    def getAssumptions(self):
        return self.assumptions

    def __str__(self):
        return str(self.assumptions) + " " + self.proof

