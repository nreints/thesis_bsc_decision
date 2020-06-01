from helperFunctions import alternatives, allVoters, allAlternatives, prefers
from instance import *

class ParetoAxiom:

    def __init__(self):
        self.description = "Pareto Principle"
        self.type = "alternative"

    def getInstance(self, profile, nbAlternatives, nbVoters):
        deleteAlternative, instances = [], []
        for x in allAlternatives(nbAlternatives):
            for y in alternatives(nbAlternatives, lambda y : y != x):    
                dominated = 0
                for i in allVoters(nbVoters):
                    if prefers(i, x, y, profile):
                        dominated += 1
                if dominated == nbVoters and y not in deleteAlternative:
                    deleteAlternative.append(y)
                    descriptionInst = str(y) + " is dominated by " +  str(x)
                    instances += [instance(self, descriptionInst)]
        return deleteAlternative, instances

    def toString(self):
        return self.description