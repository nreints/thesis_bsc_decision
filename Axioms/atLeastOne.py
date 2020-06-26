from helperFunctions import posLiteral, allAlternatives
from instance import instanceCNF

class atLeastOne():
    'Represents the at least one requirement'

    def __init__(self):
        self.description = "At least one"

    # Return instances (twoProfile.py)
    def getInstancesCNF(self, profile):
        instCNF = [[posLiteral(profile.id, x, profile.nbAlternatives) for x in allAlternatives(profile.nbAlternatives)]]
        instDescription = "F(" + profile.toString() + ") != {}"
        instance = instanceCNF(self, instCNF, instDescription, profile)
        return instance

    # Return aixom description
    def toString(self):
        return self.description
