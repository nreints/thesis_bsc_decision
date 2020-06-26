class node:
    'Represents a node'

    def __init__(self, profiles, exp, normBasis):
        self.usedProfiles = profiles
        self.explanation = exp
        self.normBasis = normBasis

    # Return CNF of explanation
    def getExpCNF(self):
        res = []
        for explanation in self.explanation:
            for subCNF in explanation.cnf:
                res += [subCNF]
        return res

    # Return explanation
    def getExp(self):
        return self.explanation

    # Return normative basis
    def getNormBasis(self):
        return self.normBasis

    # Return used profiles
    def getProfiles(self):
        return self.usedProfiles
