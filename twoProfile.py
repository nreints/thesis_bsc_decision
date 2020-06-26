from profile import *
from node import *
from pylgl import solve
from Axioms.atLeastOne import *
from Axioms.goalConstraint import *
from Axioms.pareto import *
from Axioms.condorcet import *
from Axioms.cancellation import *
from Axioms.faithfulness import *
from Axioms.anonymity import *
from Axioms.neutrality import *
from helperFunctions import *

class findJUST2:
    def __init__(self, targProfile, outcome):
        self.allProfiles = listAllProfiles(targProfile)
        self.targProfile = profile(targProfile, self.allProfiles)
        self.targOutcome = outcome
        self.visitedDict = {}


    def solve(self, normativeBasis):
        print("............ Trying to find a justification .........")
        print("   .... The target profile is: ", self.targProfile.toString())
        print("   .... The target outcome is: ", self.targOutcome)
        print("   .... The axioms in the normative basis are: ", 
                ", ".join([axiom.toString() for axiom in normativeBasis]))
        one, goal = atLeastOne(), goalConstraint()
        oneTarget = one.getInstancesCNF(self.targProfile)
        goalTarget = goal.getInstancesCNF(self.targProfile, self.targOutcome)
        
        explanation = [oneTarget, goalTarget]
        normBasis = []

        usedProfiles = [self.targProfile]

        root = node(usedProfiles, explanation, normBasis)
        queue = [root]
        nbNode = 0

        while queue != []:
            currentNode = queue[0]
            self.visitedDict[nbNode] = [currentNode.explanation[i].description for i in range(len(currentNode.explanation))]
            currentCNF = currentNode.getExpCNF()
            # If the current explanation is unsatisfiable the justification is found
            if solve(currentCNF) == "UNSAT":
                return currentNode.getExp(), currentNode.getNormBasis()

            for axiom in normativeBasis:
                currentProfiles = currentNode.getProfiles()
                for currentProfile in currentProfiles:
                    if axiom.description == "Neutrality" or axiom.description == "Anonymity":
                        instances = axiom.getInstancesCNF(currentProfile, self.getAllProfiles())
                    else:
                        instances = axiom.getInstancesCNF(currentProfile)

                    for instance in instances:
                        nextNode = self.getNextNode(currentNode, axiom, currentProfile, instance, one, nbNode)
                        if nextNode and self.alreadyVisited(nextNode):
                            queue.append(nextNode)
            nbNode += 1
            queue.pop(0)
        return None, None

    # Check if nextNode already has been visited
    def alreadyVisited(self, nextNode):
        return Counter([exp.description for exp in nextNode.explanation]) not in [Counter(val) for val in self.visitedDict.values()]

    # Return all profiles
    def getAllProfiles(self):
        return self.allProfiles

    # Generate the next node
    def getNextNode(self, currentNode, axiom, currentProfile, instance, one, nbNode):
        if instance.description not in [currentNode.explanation[i].description for i in range(len(currentNode.explanation))]:
            tempUsedProfiles = list(set(currentNode.getProfiles() + [instance.getProfile()]))
            tempExplanation = currentNode.getExp() + [instance] + [one.getInstancesCNF(prof) for prof in tempUsedProfiles if prof not in currentNode.getProfiles()]
            tempNormBasis = currentNode.getNormBasis() + [axiom]
            nextNode = node(tempUsedProfiles, tempExplanation, tempNormBasis)
            return nextNode
        return None

    # Print explanation
    def printExplanation(self, exp, norm):
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        if exp:
            print("Found an explanation:")
            for instance in exp:
                if instance.axiom.description != "At least one" and instance.axiom.description != "Goal constraint":
                    print("\t", instance.toString())
        else:
            print("Found no explanation")

par = Pareto()
con = Condorcet()
can = Cancellation()
faith = Faithfulness()
ano = Anonymity()
neu = Neutrality()
normativeBasis = [can, faith, con, par, neu, ano]

# A sublist in the profile is the preference of one agent
targProfile = [[0, 1, 2], [1, 0, 2]]
# Represent the target outcome as a list
targOutcome = [0, 1]

twoProfile = findJUST2(targProfile, targOutcome)
exp, normBasis = twoProfile.solve(normativeBasis)
twoProfile.printExplanation(exp, normBasis)
