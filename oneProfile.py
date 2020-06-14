from collections import Counter
from helperFunctions import allSublists, allVoters, allAlternatives, removeOutcome
from pareto import *
from condorcet import *
from faithfulness import *
from cancellation import *


class FINDJUST1:

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
                    for instance in instances:
                        winner = instance.getAlternatives()
                        # Check if winner is target outcome
                        if Counter(winner) == Counter(self.outcome):
                            explanation[nbExp] = [instance]
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
        if not exp:
            print("No explanation found")
        else:
            for key in exp:
                print("Found an explanation of size ", len(exp[key]), ":")
                print("\t Normative basis : ", ", ".join([exp.description for exp in normBasis[key]]))
                for instance in exp[key]:
                    instance.toString()
                print()



par = ParetoAxiom()
con = CondorcetAxiom()
faith = Faithfulness()
can = Cancellation()
normativeBasis = [par, con, faith, can]

thing = FINDJUST1([[2,0,1], [1,0,2], [2,1,0]], [2])
exp, normBasis = thing.solve(normativeBasis)
thing.printExplanation(exp, normBasis)
