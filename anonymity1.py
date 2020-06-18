from instanceCNF import *
from helperFunctions import profiles, iVariants, posLiteral, negLiteral, allAlternatives
from itertools import product, permutations
from collections import Counter
from profile import *

class Anonymity():
    def __init__(self):
        self.description = "anonymity"

    def getInstancesCNF(self, prof):
        start = [sorted(prof.listProfile[0]) for _ in range(prof.nbVoters)]
        results = product(*[list(permutations(x)) for x in start])
        allProfiles = []
        for res in results:
            res = [list(sub) for sub in res]
            allProfiles += [list(res)]
        
        
        instances = []
        for i in profiles(prof.nbAlternatives, prof.nbVoters, lambda i: i != prof.id):

            if i <= prof.id:
                continue
            l1 = [str(sub) for sub in prof.listProfile]
            l2 = [str(sub) for sub in allProfiles[i]]
            if Counter(l1) == Counter(l2):
                cnfInstance = [[negLiteral(prof.id, x, prof.nbAlternatives), posLiteral(i, x, prof.nbAlternatives)] for x in allAlternatives(prof.nbAlternatives)]
                cnfInstance += [[negLiteral(i, x, prof.nbAlternatives), posLiteral(prof.id, x, prof.nbAlternatives)] for x in allAlternatives(prof.nbAlternatives)]
                instDescription = "F(" + prof.toString() + ") = F(" + str(allProfiles[i]) + ")"
                profile2 = profile(allProfiles[i], allProfiles)
                instance = instanceCNF(self, cnfInstance, instDescription, profile2)
                instances.append(instance)
        return instances

    def toString(self):
        return self.description
