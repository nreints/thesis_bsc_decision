from helperFunctions import negLiteral, posLiteral, alternatives
from instanceCNF import *

class goalConstraint():
    def __init__(self):
        self.description = "goal constraint"

    def getInstancesCNF(self, profile, outcome):
        instCNF = []
        for x in outcome:
            instCNF.append(negLiteral(profile.id, x, profile.nbAlternatives))
        for x in alternatives(profile.nbAlternatives, lambda x: x not in outcome):
            instCNF.append(posLiteral(profile.id, x, profile.nbAlternatives))
        instDescription = "F(" + profile.toString() + ") != " + str(outcome)
        instances = instanceCNF(self, [instCNF], instDescription)
        print("goal", [instCNF])
        return instances

    def toString(self):
        return self.description