

class instanceCNF:
    def __init__(self, axiom, cnf, description):
        self.axiom = axiom
        self.cnf = cnf
        self.description = description

    def toString(self):
        return self.description + "   (" + self.axiom.toString() + ")"