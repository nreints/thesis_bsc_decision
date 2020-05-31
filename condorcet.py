from helperFunctions import alternatives, allAlternatives, prefers, allVoters
from instance import *

class CondorcetAxiom:

    def __init__(self):
        self.description = "Condorcet Principle"
        self.type = "outcome"
        

    def getWinner(self, profile, nbAlternatives, nbVoters):
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
                description = "The majority of voters prefers " + str(x) + " over all other alternatives"
                return x, instance(self, description)
        return None, ()

    def toString(self):
        return self.description