from instance import *

class Faithfulness:

    def __init__(self):
        self.description = "Faithfulness"
        self.type = "outcome"
        

    def getWinner(self, profile, nbAlternatives, nbVoters):
        if nbVoters == 1:
            description = "The top alternative " + str(profile[0][0]) + " should be chosen"
            return profile[0][0], instance(self, description)
        return None, ()

    def toString(self):
        return self.description