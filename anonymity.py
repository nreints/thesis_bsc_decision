from helperFunctions import voters, allVoters, allAlternatives, prefers
from instance import *
import copy

class Anonymity:

    def __init__(self):
        self.description = "Anonymity"
        self.type = "2prof"

    def getInstances(self, profile, nbAlternatives, nbVoters):
        xSkip = []

        for x in voters(nbVoters, lambda x: x not in xSkip):
            for y in voters(nbVoters, lambda y : y != x and y not in xSkip):
                xSkip += [x]


                otherProf = copy.deepcopy(profile)
                otherProf[x] = profile[y]
                otherProf[y] = profile[x]
    
                instDescription = "F(" + str(profile) + ") = F(" + str(otherProf) + ")"
                print(instDescription)
        return None

    def toString(self):
        return self.description
