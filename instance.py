from helperFunctions import alternatives, allVoters, allAlternatives, prefers


class instance:

    def __init__(self, axiom, description):
        self.axiom = axiom
        self.description = description


    def toString(self):
        print(self.description + " (" + self.axiom.toString() + ") ")
