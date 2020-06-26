from helperFunctions import alternatives, allVoters, allAlternatives, prefers, negLiteral, isDominated
from instance import *

class ParetoAxiom:

    def __init__(self):
        self.description = "Pareto Principle"
        self.type = "delete alt"

    # Return instances (oneProfile.py)
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

    # Return instances (twoProfile.py)
    def getInstancesCNF(self, profile):
        instances = []
        for y in allAlternatives(profile.nbAlternatives):
            x = isDominated(y, profile)
            if x >= 0:
                cnfInstance = [[negLiteral(profile.id, y, profile.nbAlternatives)]]
                instDescription = str(y) + " not in F(" + profile.toString() + ") dominated by " + str(x)
                instances += [instanceCNF(self, cnfInstance, instDescription, profile)]
        return instances

    # Return type of axiom
    def getType(self):
        return self.type

    # Return aixom description
    def toString(self):
        return self.description
