# from helperFunctions import 

class Faithfulness:

    def __init__(self):
        self.description = "Faithfulness"
        self.type = "outcome"
        

    def getWinner(self, profile, nbAlternatives, nbVoters):
        if nbVoters == 1:
            return profile[0][0], (profile, profile[0][0])
        return None, ()

    def printInstance(self, instance):
        print("In profile ", instance[0], ": the most preferred option should be chosen ",  instance[1], "  (", self.description,")")

    def toString(self):
        return self.description