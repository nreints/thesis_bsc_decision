from profile import *
from node import *
from pylgl import solve
from atLeastOne import *
from goalConstraint import *
from pareto import *
from condorcet import *
from cancellation import *
from faithfulness import *

class findJUST2:
    def __init__(self, targProfile, outcome):
        self.allProfiles = self.listAllProfiles(targProfile)
        self.targProfile = profile(targProfile, self.allProfiles)
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

            # print("now checking exp", currentNode.getProfiles()[0].listProfile, "++ CNF", currentCNF)
            if solve(currentCNF) == "UNSAT":
                return currentNode.getExp(), currentNode.getNormBasis()

            for axiom in normativeBasis:
                # print("for axiom ", axiom)
                for currentProfile in currentNode.getProfiles():
                    # print("\t",currentProfile)
                    for instance in axiom.getInstancesCNF(currentProfile):
                        # print("\t\t",instance)
                        # print(instance.description, " ".join([currentNode.explanation[i].description for i in range(len(currentNode.explanation))]))
                        # print(instance.description in [currentNode.explanation[i].description for i in range(len(currentNode.explanation))])
                        if instance.description not in [currentNode.explanation[i].description for i in range(len(currentNode.explanation))]:
                            usedProfiles = list(set(currentNode.getProfiles() + [currentProfile]))
                            tempExplanation = currentNode.getExp() + [instance] + [one.getInstancesCNF(prof) for prof in usedProfiles if prof not in currentNode.getProfiles()]
                            tempNormBasis = currentNode.getNormBasis() + [axiom]
                            # print("\t\t\tCreating new node ")
                            # print("\t\t\t+ used prof : ", usedProfiles)
                            # print("\t\t\t+ exp : ", " ".join([tempExplanation[i].axiom.toString() for i in range(len(tempExplanation))]))
                            # print("\t\t\t+ exp : ", " ".join([str(tempExplanation[i].cnf) for i in range(len(tempExplanation))]))
                            nextNode = node(usedProfiles, tempExplanation, tempNormBasis)

                            if nextNode.discovered == False:
                                nextNode.setDiscovered()
                                queue.append(nextNode)
            queue.pop(0)
            # for n in queue:
            #     print("newNode")
            #     for prof in n.getProfiles():
            #         print(prof.listProfile)
            # print(len(queue))

        return None, None

    def listAllProfiles(self, profile):
        start = [sorted(profile[0]) for _ in range(len(profile))]
        results = product(*[list(permutations(x)) for x in start])
        allProfiles = []
        for res in results:
            res = [list(sub) for sub in res]
            allProfiles += [list(res)]
        return allProfiles

    # Print explanation
    def printExplanation(self, exp, norm):
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        if exp:
            print("Found an explanation of size ", len(exp) - 2, ":")
            for instance in exp:
                if instance.axiom.description != "at least one" and instance.axiom.description != "goal constraint":
                    print(instance.toString())
        else:
            print("No explanation found")



par = ParetoAxiom()
con = CondorcetAxiom()
can = Cancellation()
faith = Faithfulness()

thing2 = findJUST2([[0,1,2], [2,1,0]], [2,0,1])
exp, norm = thing2.solve2([par, con, can])
thing2.printExplanation(exp, norm)


