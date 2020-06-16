from profile import *
from node import *
from pylgl import solve
from collections import deque
from atLeastOne import *
from goalConstraint import *
from pareto import *
from condorcet import *
from cancellation import *

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
        oneTarg = one.getInstancesCNF(self.targProfile)
        goal = goalConstraint()
        goalTarg = goal.getInstancesCNF(self.targProfile, self.targOutcome)
        explanation = [oneTarg, goalTarg]
        normBasis = []

        usedProfiles = [self.targProfile]

        root = node(usedProfiles, explanation, normBasis)
        root.setDiscovered()

        queue = [root]
        while queue != []:
            currentNode = queue[0]
            currentCNF = currentNode.getExpCNF()

            print("now checking exp", currentNode.getProfiles()[0].listProfile, "++ CNF", currentCNF)
            if solve(currentCNF) == "UNSAT":
                return currentNode.getExp(), currentNode.getNormBasis()
            # print("satisfiable", solve(currentNode.getExpCNF()))

            for axiom in normativeBasis:
                print("for axiom ", axiom)
                for currentProfile in currentNode.getProfiles():
                    print("\t",currentProfile)
                    for instance in axiom.getInstancesCNF(currentProfile):
                        print("\t\t",instance)
                        # print(instance.description, " ".join([currentNode.explanation[i].description for i in range(len(currentNode.explanation))]))
                        # print(instance.description in [currentNode.explanation[i].description for i in range(len(currentNode.explanation))])
                        if instance.description not in [currentNode.explanation[i].description for i in range(len(currentNode.explanation))]:
                            usedProfiles = list(set(currentNode.getProfiles() + [currentProfile]))
                            tempExplanation = currentNode.getExp() + [instance] + [one.getInstancesCNF(prof) for prof in usedProfiles if prof not in currentNode.getProfiles()]
                            tempNormBasis = currentNode.getNormBasis() + [axiom]
                            print("\t\t\tCreating new node ")
                            print("\t\t\t+ used prof : ", usedProfiles)
                            print("\t\t\t+ exp : ", " ".join([tempExplanation[i].axiom.toString() for i in range(len(tempExplanation))]))
                            print("\t\t\t+ exp : ", " ".join([str(tempExplanation[i].cnf) for i in range(len(tempExplanation))]))
                            # print("\t\t\t+ nom : ", tempNormBasis)
                            nextNode = node(usedProfiles, tempExplanation, tempNormBasis)

                            if nextNode.discovered == False:
                                nextNode.setDiscovered()
                                queue.append(nextNode)
            print("NEW")
            # print(len(queue))
            # for n in queue:
            #     print("newNode")
            #     for prof in n.getProfiles():
            #         print(prof.listProfile)
            queue.pop(0)
            # for n in queue:
            #     print("newNode")
            #     for prof in n.getProfiles():
            #         print(prof.listProfile)
            # print(len(queue))

        return None, None


par = ParetoAxiom()
con = CondorcetAxiom()
can = Cancellation()
thing2 = findJUST2([[2,1,0], [2,1,0]], [0])
exp, norm = thing2.solve2([par,con])

print("++++ DONEE ++++")
if exp:
    for instance in exp:
        print(instance.toString())


