from helperFunctions import posLiteral, allAlternatives
from instanceCNF import *

class atLeastOne():
    def __init__(self):
        self.description = "at least one"

    def getInstancesCNF(self, profile):
        instCNF = [[posLiteral(profile.id, x, profile.nbAlternatives) for x in allAlternatives(profile.nbAlternatives)]]
        instDescription = "F(" + profile.toString() + ") != {}"
        instance = instanceCNF(self, instCNF, instDescription, profile)
        return instance

    def toString(self):
        return self.description