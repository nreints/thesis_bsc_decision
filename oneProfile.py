from collections import Counter
from helperFunctions import allSublists, allVoters, allAlternatives, removeOutcome
from Axioms.pareto import *
from Axioms.condorcet import *
from Axioms.faithfulness import *
from Axioms.cancellation import *

class findJUST1:

    def __init__(self, profile, outcome):
        self.profile = profile
        self.outcome = outcome
        self.nbAlternatives = len(profile[0])
        self.nbVoters = len(profile)
        self.alternatives = allAlternatives(self.nbAlternatives)
        self.voters = allVoters(self.nbVoters)

    def solve(self, normativeBasis):
        print("............ Trying to find a justification .........")
        print("   .... The target profile is: ", self.profile)
        print("   .... The target outcome is: ", self.outcome)
        print("   .... The axioms in the normative basis are: ", 
                ", ".join([axiom.toString() for axiom in normativeBasis]))
        explanation, normBasis = {}, {}
        nbExp = 0

        # Create list of all possible outcomes
        posOutcomes = list(allSublists(self.profile[0]))
        # Delete target outcome from possible outcomes
        posOutcomes = removeOutcome(posOutcomes, self.outcome)

        for axiom in normativeBasis:
            if axiom.getType() == "outcome":
                instances = axiom.getInstances(self.profile, self.nbAlternatives, self.nbVoters)
                if instances:
                    winner = instances[0].getAlternatives()
                    # Check if winner is target outcome
                    if Counter(winner) == Counter(self.outcome):
                        explanation[nbExp] = [instances[0]]
                        normBasis[nbExp] = [axiom]
                        nbExp += 1

            posExplanation = []
            if axiom.getType() == "delete alt":
                instances = axiom.getInstances(self.profile, self.nbAlternatives, self.nbVoters)
                if instances:
                    for instance in instances:
                        delAlternatives = instance.getAlternatives()
                        if len(delAlternatives) > 0:
                            # Delete outcomes that contain alternative
                            posOutcomes = [outcome for outcome in posOutcomes 
                                            if set(delAlternatives).isdisjoint(outcome)]
                            posExplanation.append(instance)

            if axiom.getType() == "force alt":
                instances = axiom.getInstances(self.profile, self.nbAlternatives, self.nbVoters)
                if instances:
                    for instance in instances:
                        forceAlternatives = instance.getAlternatives()
                        if len(forceAlternatives) > 0:
                            # Delete outcomes that do not contain alternative
                            posOutcomes = [outcome for outcome in posOutcomes 
                                            if not set(delAlternatives).isdisjoint(outcome)]
                            posExplanation.append(instance)

            if posOutcomes == [] and (axiom.getType() == "force alt"
                                        or axiom.getType() == "delete alt"):
                explanation[nbExp] = [instance for instance in posExplanation]
                normBasis[nbExp] = [instance.getAxiom() for instance in posExplanation]
                nbExp += 1
        return explanation, normBasis

    # Print explanation
    def printExplanation(self, exp, normBasis):
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        if exp:
            for key in exp:
                print("Found an explanation of size ", len(exp[key]), ":")
                for instance in exp[key]:
                    instance.toString()
                print()
        else:
            print("Found no explanation")

par = ParetoAxiom()
con = CondorcetAxiom()
faith = Faithfulness()
can = Cancellation()
normativeBasis = [par, con, faith, can]

# A sublist in the profile is the preference of one agent
targProfile = [[0,1,2], [0,1,2]]
# Represent the target outcome as a list
targOutcome = [0]
oneProfile = findJUST1(targProfile, targOutcome)
exp, normBasis = oneProfile.solve(normativeBasis)
oneProfile.printExplanation(exp, normBasis)
