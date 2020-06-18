

class instanceCNF:
    def __init__(self, axiom, cnf, description, profiles):
        self.axiom = axiom
        self.cnf = cnf
        self.description = description
        self.profiles = profiles

    def getCNF(self):
        return self.cnf
    
    def getProfile(self):
        return self.profiles

    def toString(self):
        return self.description + "   (" + self.axiom.toString() + ")"