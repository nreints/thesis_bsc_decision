from helperFunctions import alternatives, allVoters, allAlternatives, prefers
from instance import *


class ParetoAxiom:

    def __init__(self):
        self.description = "Pareto Principle"
        self.type = "delete alt"

    # Get instances
    def getInstances(self, profile, nbAlternatives, nbVoters):
        deleteAlternative, inst = [], []
        for x in allAlternatives(nbAlternatives):
            for y in alternatives(nbAlternatives, lambda y : y != x):
                dominated = 0
                for i in allVoters(nbVoters):
                    if prefers(i, x, y, profile):
                        dominated += 1
                if dominated == nbVoters and y not in deleteAlternative:
                    deleteAlternative.append(y)
                    instDescription = str(y) + " not in F(" + str(profile) + ") dominated by " + str(x)
                    inst += [instance(self, [y], instDescription)]
        return inst

    def getType(self):
        return self.type

    def toString(self):
        return self.description
