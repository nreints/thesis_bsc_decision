from profile import *
from node import *
from pylgl import solve
from collections import deque
from atLeastOne import *
from goalConstraint import *

class findJUST2:
    def __init__(self, targProfile, outcome):
        self.targProfile = profile(targProfile)
        self.targOutcome = outcome


    def solve2(self, normativeBasis):
        print("............ Trying to find a justification .........")
        print("   .... The target profile is: ", self.targProfile.toString())
        print("   .... The target outcome is: ", self.targOutcome)
        print("   .... The axioms in the normative basis are: ", 
                ", ".join([axiom.toString() for axiom in normativeBasis]))
        one = atLeastOne()
        goal = goalConstraint()
        explanation = {one.getInstancesCNF(self.targProfile), goal.getInstancesCNF(self.targProfile)}
        normBasis = {}

        usedProfiles = [self.targProfile]

        root = node(usedProfiles, explanation, normBasis)
        root.setDiscovered()

        queue = [root]
        while queue != []:
            currentNode = queue[0]
            if solve(currentNode.getExp()) == "UNSAT":
                return currentNode.getExp(), currentNode.getNormBasis()

            for axiom in normativeBasis:
                for currentProfile in currentNode.getProfiles():
                    for instance in axiom.getInstancesCNF(currentProfile):
                        usedProfiles = currentNode.getProfiles().append(currentProfile)
                        tempExplanation = currentNode.getExp().append(instance) + [one.getInstancesCNF(prof) for prof in usedProfiles]
                        tempNormBasis = currentNode.getNormBasis().append(axiom)
                        nextNode = node(usedProfiles, tempExplanation, tempNormBasis)

                        if nextNode.discovered == False:
                            nextNode.setDiscovered()
                            queue.append(nextNode)
            queue.pop(0)

        return None, None


thing2 = findJUST2([[1,0,2], [1,0,2]], [1])
thing2.solve2(["bla"])
