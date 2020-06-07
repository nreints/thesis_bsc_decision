from helperFunctions import alternatives, allVoters, allAlternatives, prefers
from instance import *
import copy

class Neutrality:

    def __init__(self):
        self.description = "Neutrality"
        self.type = "2prof"

    def getInstances(self, profile, nbAlternatives, nbVoters):
        xSkip = []
        for x in alternatives(nbAlternatives, lambda x: x not in xSkip):
            for y in alternatives(nbAlternatives, lambda y : y != x and y not in xSkip):
                xSkip += [x]

                otherProf = copy.deepcopy(profile)
                for voter in allVoters(nbVoters):
                    index1 = profile[voter].index(x)
                    index2 = profile[voter].index(y)
                    otherProf[voter][index1] = y
                    otherProf[voter][index2] = x
    
                instDescription = "F(" + str(profile) + ") and F(" + str(otherProf) + ") are linked (" + str(x) + " <-> " + str(y) + ")"
                # print(instDescription)
        return None

    def toString(self):
        return self.description
