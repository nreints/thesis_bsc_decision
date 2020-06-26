from instance import instanceCNF
from helperFunctions import profiles, posLiteral, negLiteral, allAlternatives
from collections import Counter
from profile import *

class Anonymity:
    'Represents the anonymity axiom'

    def __init__(self):
        self.description = "Anonymity"

    # Return instances (twoProfile.py)
    def getInstancesCNF(self, prof, allProf):
        instances = []
        for i in profiles(prof.nbAlternatives, prof.nbVoters, lambda i: i != prof.id):
            if i <= prof.id:
                continue
            l1 = [str(sub) for sub in prof.listProfile]
            l2 = [str(sub) for sub in allProf[i]]
            if Counter(l1) == Counter(l2):
                cnfInstance = [[negLiteral(prof.id, x, prof.nbAlternatives), posLiteral(i, x, prof.nbAlternatives)] for x in allAlternatives(prof.nbAlternatives)]
                cnfInstance += [[negLiteral(i, x, prof.nbAlternatives), posLiteral(prof.id, x, prof.nbAlternatives)] for x in allAlternatives(prof.nbAlternatives)]
                instDescription = "F(" + prof.toString() + ") = F(" + str(allProf[i]) + ")"
                profile2 = profile(allProf[i], allProf)
                instance = instanceCNF(self, cnfInstance, instDescription, profile2)
                instances.append(instance)
        return instances

    # Return aixom description
    def toString(self):
        return self.description
