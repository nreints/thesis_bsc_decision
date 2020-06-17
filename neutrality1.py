from itertools import permutations, product
from helperFunctions import profiles, allAlternatives, negLiteral, posLiteral, alternatives
from collections import Counter
from instanceCNF import *
# from profile import getList

class Neutrality():
    def __init__(self):
        self.description = "neutrality"

    def getInstancesCNF(self, profile):
        instances = []
        start = [sorted(profile.listProfile[0]) for _ in range(profile.nbVoters)]
        results = product(*[list(permutations(x)) for x in start])
        allProfiles = []
        for res in results:
            res = [list(sub) for sub in res]
            allProfiles += [list(res)]
        
        
        instances = []
        # for i in profiles(profile.nbAlternatives, profile.nbVoters, lambda i: i != profile.id):
            # if iVariants(0, profile.id, i, profile.nbAlternatives):
            #     print(allProfiles[i], profile.listProfile)

        ind = []
        xSkip = []
        for x in alternatives(profile.nbAlternatives, lambda x: x not in xSkip):
            xSkip += [x]
            for y in alternatives(profile.nbAlternatives, lambda y: y != x and y not in xSkip):
                p2 = [[1,0,2],[0,1,2]] #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                p2 = self.swap(profile.getList(), x, y)
                ind += [(allProfiles.index(p2), x, y)]
        cnfInstance = []
        for (indProf2, x, y) in ind:
            cnfInstance += [[negLiteral(profile.id, x, profile.nbAlternatives), posLiteral(indProf2, y, profile.nbAlternatives)]]
            cnfInstance += [[negLiteral(indProf2, y, profile.nbAlternatives), posLiteral(profile.id, x, profile.nbAlternatives)]]
            instDescription = "F(" + profile.toString() + ") and F(" + str(allProfiles[indProf2]) + ") are linked (" + str(x) +" <-> " +str(y) + ")"
            instance = instanceCNF(self, cnfInstance, instDescription)
            instances.append(instance)
        return instances

    def swap(self, profile, x, y):
        # prof = profile.getList()
        for i in range(len(profile)):
            indX = profile[i].index(x)
            indY = profile[i].index(y)
            profile[i][indX] = y
            profile[i][indY] = x
        return profile

    def toString(self):
        return self.description