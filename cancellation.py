from helperFunctions import alternatives, allVoters, allAlternatives, prefers
from instance import *

class Cancellation:

    def __init__(self):
        self.description = "Cancellation"
        self.type = "outcome"

    def getInstances(self, profile, nbAlternatives, nbVoters):
        perfTie = 0
        xSkip = []
        for x in alternatives(nbAlternatives, lambda x: x not in xSkip):
            for y in alternatives(nbAlternatives, lambda y : y != x and y not in xSkip):
                XOverY, YOverX = 0, 0
                for i in allVoters(nbVoters):
                    if prefers(i, x, y, profile):
                        XOverY += 1
                    else:
                        YOverX += 1
                if XOverY == YOverX:
                    perfTie += 1
                    xSkip += [x]

        if perfTie >= nbAlternatives:
            instDescription = "F(" + str(profile) + ") = X"
            return [instance(self, allAlternatives(nbAlternatives), instDescription)]
        return None

    def toString(self):
        return self.description
