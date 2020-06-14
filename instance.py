

class instance:

    def __init__(self, axiom, alternatives, description):
        self.axiom = axiom
        self.alternatives = alternatives
        self.description = description

    def getAlternatives(self):
        return self.alternatives

    def getAxiom(self):
        return self.axiom

    def toString(self):
        print("\t", self.description + " (" + self.axiom.toString() + ") ")
