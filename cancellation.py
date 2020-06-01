from helperFunctions import alternatives, allVoters, allAlternatives, prefers
from instance import *

class Cancellation:

    def __init__(self):
        self.description = "Cancellation"
        self.type = "outcome"

    def getInstance(self, profile, nbAlternatives, nbVoters):
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
            description = "There exists a perfect tie so all alternatives should win"
            return allAlternatives(nbAlternatives), instance(self, description)
        return None, None

    def toString(self):
        return self.description