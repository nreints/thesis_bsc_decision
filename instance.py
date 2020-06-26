# Instance object (oneProfile.py)
class instance:
    def __init__(self, axiom, alternatives, description):
        self.axiom = axiom
        self.alternatives = alternatives
        self.description = description

    # Return alternative(s)
    def getAlternatives(self):
        return self.alternatives

    # Return axiom
    def getAxiom(self):
        return self.axiom

    # Return string instance description
    def toString(self):
        print("\t", self.description + " (" + self.axiom.toString() + ") ")

# Instance object (twoProfile.py)
class instanceCNF:
    def __init__(self, axiom, cnf, description, profiles):
        self.axiom = axiom
        self.cnf = cnf
        self.description = description
        self.profiles = profiles

    # Return CNF
    def getCNF(self):
        return self.cnf
    
    # Return profiles
    def getProfile(self):
        return self.profiles

    # Return string instance description
    def toString(self):
        return self.description + "   (" + self.axiom.toString() + ")"