from instance import *
from helperFunctions import topAlternative

class Faithfulness:

    def __init__(self):
        self.description = "Faithfulness"
        self.type = "outcome"
        

    def getInstance(self, profile, nbAlternatives, nbVoters):
        if nbVoters == 1:
            descriptionInst = "The top alternative " + str(profile[0][0]) + " should be chosen"
            winner = topAlternative(profile[0])
            return winner, instance(self, descriptionInst)
        return None, None

    def toString(self):
        return self.description