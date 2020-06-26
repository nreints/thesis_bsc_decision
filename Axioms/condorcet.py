from helperFunctions import alternatives, allAlternatives, prefers, prefers2, allVoters, posLiteral, negLiteral
from instance import *

class Condorcet:
    'Represents the Condorcet principle'

    def __init__(self):
        self.description = "Condorcet principle"
        self.type = "outcome"

    # Return instances (oneProfile.py)
    def getInstances(self, profile, nbAlternatives, nbVoters):
        for x in allAlternatives(nbAlternatives):
            timesY = 0
            for y in alternatives(nbAlternatives, lambda y: x != y):
                voters = 0
                for i in allVoters(nbVoters):
                    if prefers(i, x, y, profile):
                        voters += 1
                if voters > (nbVoters/2):
                    timesY += 1
            if timesY == nbAlternatives - 1:
                instDescription = "F(" + str(profile) + ") = {" + str(x) + "}"
                return [instance(self, [x], instDescription)]
        return []

    # Return instances (twoProfile.py)
    def getInstancesCNF(self, profile):
        for x in allAlternatives(profile.nbAlternatives):
            timesY = 0
            for y in alternatives(profile.nbAlternatives, lambda y: x != y):
                voters = 0
                for i in allVoters(profile.nbVoters):
                    if prefers2(i, x, y, profile.id, profile.nbAlternatives):
                        voters += 1
                if voters > (profile.nbVoters/2):
                    timesY += 1
            if timesY == profile.nbAlternatives - 1:
                instCNF = [[posLiteral(profile.id, x, profile.nbAlternatives)]]
                instCNF += [[negLiteral(profile.id, y, profile.nbAlternatives)] for y in alternatives(profile.nbAlternatives, lambda y: x != y)]
                instDescription = "F(" + profile.toString() + ") = {" + str(x) + "}"
                return [instanceCNF(self, instCNF, instDescription, profile)]
        return []

    # Return type of axiom
    def getType(self):
        return self.type

    # Return aixom description
    def toString(self):
        return self.description
