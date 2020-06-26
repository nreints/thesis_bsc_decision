from helperFunctions import topAlternative, posLiteral, negLiteral, alternatives
from instance import *

class Faithfulness:

    def __init__(self):
        self.description = "Faithfulness"
        self.type = "outcome"

    #  Return instances (oneProfile.py)
    def getInstances(self, profile, nbAlternatives, nbVoters):
        if nbVoters == 1:
            instDescription = "F(" + str(profile) + ") = {" + str(profile[0][0]) + "}"
            winner = topAlternative(profile[0])
            return [instance(self, [winner], instDescription)]
        return []

    # Return instances (twoProfile.py)
    def getInstancesCNF(self, profile):
        if profile.nbVoters == 1:
            x = topAlternative(profile.listProfile[0])
            instCNF = [posLiteral(profile.id, x, profile.nbAlternatives)]
            instCNF = [[posLiteral(profile.id, x, profile.nbAlternatives)]]
            instCNF += [[negLiteral(profile.id, y, profile.nbAlternatives)] for y in alternatives(profile.nbAlternatives, lambda y: x != y)]
            instDescription = "F(" + profile.toString() + ") = {" + str(x) + "}"
            return [instanceCNF(self, instCNF, instDescription, profile)]
        return []

    # Return type of axiom
    def getType(self):
        return self.type

    # Return aixom description
    def toString(self):
        return self.description
