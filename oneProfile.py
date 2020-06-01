from collections import Counter
from helperFunctions import allSublists, allVoters, allAlternatives, removeOutcome
from pareto import *
from condorcet import *
from faithfulness import *
from cancellation import *

class FINDJUST:

    def __init__(self, profile, outcome):
        self.profile = profile
        self.outcome = outcome
        self.nbAlternatives = len(profile[0])
        self.nbVoters = len(profile)
        self.alternatives = allAlternatives(self.nbAlternatives)
        self.voters = allVoters(self.nbVoters)

    def solve(self, normativeBasis):
        print(".... Trying to find a justification for the profile and outcome ....")
        print(".... The target profile is: ", self.profile)
        print(".... The target outcome is: ", self.outcome)
        print(".... The axioms in the normative basis are: ", ", ".join([axiom.toString() for axiom in normativeBasis]))
        explanation = {}
        nbExp = 0

        axiomsOutcome, axiomsAlternative = self.splitAxioms(normativeBasis)

        for axiom in axiomsOutcome:
            winner, instance = axiom.getInstance(self.profile, self.nbAlternatives, self.nbVoters)
            if Counter(winner) == Counter(self.outcome):
                explanation[nbExp] = [instance]
                nbExp += 1
        
        posOutcomes = list(allSublists(self.profile[0]))
        
        # Delete target outcome from possible outcomes
        posOutcomes = removeOutcome(posOutcomes, self.outcome)

        posExplanation = []
        for axiom in axiomsAlternative:
            alternatives, instances = axiom.getInstance(self.profile, self.nbAlternatives, self.nbVoters)
            copyPosOutcomes = posOutcomes.copy()
            for i in range(len(alternatives)):
                for outcome in copyPosOutcomes:
                    if (alternatives[i] in outcome) and (outcome in posOutcomes):
                        posOutcomes.remove(outcome)
                if len(posOutcomes) < len(copyPosOutcomes):
                    posExplanation.append(instances[i])
            if posOutcomes == []:
                explanation[nbExp] = posExplanation

        return explanation

    def splitAxioms(self, normativeBasis):
        axiomsOutcome, axiomsAlternative = [], []
        for axiom in normativeBasis:
            if axiom.type == "outcome":
                axiomsOutcome.append(axiom)
            elif axiom.type == "alternative":
                axiomsAlternative.append(axiom)
        return axiomsOutcome, axiomsAlternative
    
    
    def printExplanation(self, exp):
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        if not exp:
            print("No explanation found")
        else:
            for key in exp:
                print("Found an explanation of size ", len(exp[key]), ":")
                for instance in exp[key]:
                    instance.toString()
                print()



par = ParetoAxiom()
con = CondorcetAxiom()
faith = Faithfulness()
can = Cancellation()
normativeBasis = [par, con, faith, can]

thing = FINDJUST([[2,0,1], [2,0,1]], [2])
exp = thing.solve(normativeBasis)
thing.printExplanation(exp)
