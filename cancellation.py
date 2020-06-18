from helperFunctions import alternatives, allVoters, allAlternatives, prefers, prefers2, posLiteral
from instance import *
from instanceCNF import *

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
            return [instance(self, allAlternatives(nbAlternatives), instDescription, profile)]
        return []

    def getInstancesCNF(self, profile, thing):
        perfTie = 0
        xSkip = []
        for x in alternatives(profile.nbAlternatives, lambda x: x not in xSkip):
            for y in alternatives(profile.nbAlternatives, lambda y : y != x and y not in xSkip):
                XOverY, YOverX = 0, 0
                for i in allVoters(profile.nbVoters):
                    if prefers2(i, x, y, profile.id, profile.nbAlternatives):
                        XOverY += 1
                    else:
                        YOverX += 1
                if XOverY == YOverX:
                    perfTie += 1
                    xSkip += [x]

        if perfTie >= profile.nbAlternatives:
            instCNF = [[posLiteral(profile.id, x, profile.nbAlternatives)] for x in allAlternatives(profile.nbAlternatives)]
            instDescription = "F(" + profile.toString() + ") = X"
            return [instanceCNF(self, instCNF, instDescription)]
        return []

    def getType(self):
        return self.type

    def toString(self):
        return self.description
