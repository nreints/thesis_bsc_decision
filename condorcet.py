from helperFunctions import alternatives, allAlternatives, prefers, prefers2, allVoters, posLiteral, negLiteral
from instance import *
from instanceCNF import *

class CondorcetAxiom:

    def __init__(self):
        self.description = "Condorcet Principle"
        self.type = "outcome"

    # Return instances
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
        return None

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
                # print("CON", instCNF)
                return [instanceCNF(self, instCNF, instDescription, profile)]
        return []

    def getType(self):
        return self.type

    def toString(self):
        return self.description
