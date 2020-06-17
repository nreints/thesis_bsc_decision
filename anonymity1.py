from instanceCNF import *
from helperFunctions import profiles, iVariants, posLiteral, negLiteral, allAlternatives
from itertools import product, permutations
from collections import Counter

class Anonymity():
    def __init__(self):
        self.description = "anonymity"

    def getInstancesCNF(self, profile):
        
        
        start = [sorted(profile.listProfile[0]) for _ in range(profile.nbVoters)]
        results = product(*[list(permutations(x)) for x in start])
        allProfiles = []
        for res in results:
            res = [list(sub) for sub in res]
            allProfiles += [list(res)]
        
        
        instances = []
        for i in profiles(profile.nbAlternatives, profile.nbVoters, lambda i: i != profile.id):
            # if iVariants(0, profile.id, i, profile.nbAlternatives):
            #     print(allProfiles[i], profile.listProfile)
            
            if i <= profile.id:
                continue
            l1 = [str(sub) for sub in profile.listProfile]
            l2 = [str(sub) for sub in allProfiles[i]]
            if Counter(l1) == Counter(l2):
                cnfInstance = [[negLiteral(profile.id, x, profile.nbAlternatives), posLiteral(i, x, profile.nbAlternatives)] for x in allAlternatives(profile.nbAlternatives)]
                cnfInstance += [[negLiteral(i, x, profile.nbAlternatives), posLiteral(profile.id, x, profile.nbAlternatives)] for x in allAlternatives(profile.nbAlternatives)]
                instDescription = "F(" + profile.toString() + ") = F(" + str(i) + ")"
                instance = instanceCNF(self, cnfInstance, instDescription)
                instances.append(instance)
        return instances

    def toString(self):
        return self.description
