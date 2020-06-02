

class instance:

    def __init__(self, axiom, alternatives, description):
        self.axiom = axiom
        self.alternatives = alternatives
        self.description = description


    def toString(self):
        print(self.description + " (" + self.axiom.toString() + ") ")
