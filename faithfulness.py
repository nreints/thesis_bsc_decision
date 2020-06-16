from instance import *
from helperFunctions import topAlternative

class Faithfulness:

    def __init__(self):
        self.description = "Faithfulness"
        self.type = "outcome"

    #  Return instances
    def getInstances(self, profile, nbAlternatives, nbVoters):
        if nbVoters == 1:
            instDescription = "F(" + str(profile) + ") = {" + str(profile[0][0]) + "}"
            winner = topAlternative(profile[0])
            return [instance(self, [winner], instDescription)]
        return []

    def getType(self):
        return self.type

    def toString(self):
        return self.description