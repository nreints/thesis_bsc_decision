

class node:
    def __init__(self, profiles, exp, normBasis):
        self.usedProfiles = profiles
        self.explanation = exp
        self.normBasis = normBasis
        self.discovered = False

    def setDiscovered(self):
        self.discovered = True

    def getExp(self):
        return self.explanation

    def getNormBasis(self):
        return self.normBasis

    def getProfiles(self):
        return self.usedProfiles
