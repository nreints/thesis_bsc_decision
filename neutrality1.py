from itertools import permutations, product
from helperFunctions import profiles, allAlternatives, negLiteral, posLiteral, alternatives
from collections import Counter
from instanceCNF import *
from profile import *
# from profile import getList
import copy

class Neutrality():
    def __init__(self):
        self.description = "neutrality"

    def getInstancesCNF(self, prof, thing):
        start = [sorted(prof.listProfile[0]) for _ in range(prof.nbVoters)]
        results = product(*[list(permutations(x)) for x in start])
        allProfiles = []
        for res in results:
            res = [list(sub) for sub in res]
            allProfiles += [list(res)]
        
        
        instances = []

        ind = []
        xSkip = []
        for x in alternatives(prof.nbAlternatives, lambda x: x not in xSkip):
            xSkip += [x]
            for y in alternatives(prof.nbAlternatives, lambda y: y != x and y not in xSkip):
                test = copy.deepcopy(prof.getList())
                p2 = self.swap(test, x, y)
                ind += [(thing.index(p2), x, y)]
        cnfInstance = []
        for (indProf2, x, y) in ind:
            cnfInstance += [[negLiteral(prof.id, x, prof.nbAlternatives), posLiteral(indProf2, y, prof.nbAlternatives)]]
            cnfInstance += [[negLiteral(indProf2, y, prof.nbAlternatives), posLiteral(prof.id, x, prof.nbAlternatives)]]
            instDescription = "F(" + prof.toString() + ") and F(" + str(thing[indProf2]) + ") are linked (" + str(x) +" <-> " +str(y) + ")"
            profile2 = profile(thing[indProf2], thing)
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