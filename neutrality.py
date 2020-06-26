from itertools import permutations, product
from helperFunctions import profiles, allAlternatives, negLiteral, posLiteral, alternatives
from collections import Counter
from instance import instanceCNF
from profile import *
import copy

class Neutrality():
    def __init__(self):
        self.description = "neutrality"

    def getInstancesCNF(self, prof, allProf):
        instances = []
        ind = []
        xSkip = []
        for x in alternatives(prof.nbAlternatives, lambda x: x not in xSkip):
            xSkip += [x]
            for y in alternatives(prof.nbAlternatives, lambda y: y != x and y not in xSkip):
                test = copy.deepcopy(prof.getList())
                p2 = self.swap(test, x, y)
                ind += [(allProf.index(p2), x, y)]
        cnfInstance = []
        for (indProf2, x, y) in ind:
            cnfInstance += [[negLiteral(prof.id, x, prof.nbAlternatives), posLiteral(indProf2, y, prof.nbAlternatives)]]
            cnfInstance += [[negLiteral(indProf2, y, prof.nbAlternatives), posLiteral(prof.id, x, prof.nbAlternatives)]]
            instDescription = "F(" + prof.toString() + ") and F(" + str(allProf[indProf2]) + ") are linked (" + str(x) +" <-> " + str(y) + ")"
            profile2 = profile(allProf[indProf2], allProf)
            instance = instanceCNF(self, cnfInstance, instDescription, profile2)
            instances.append(instance)
        return instances

    def swap(self, profile, x, y):
        copyProf = copy.deepcopy(profile)
        for i in range(len(copyProf)):
            indX = copyProf[i].index(x)
            indY = copyProf[i].index(y)
            copyProf[i][indX] = y
            copyProf[i][indY] = x
        return copyProf

    def toString(self):
        return self.description