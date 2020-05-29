from collections import Counter
from helperFunctions import allSublists, allVoters, allAlternatives, removeOutcome
from pareto import *
from condorcet import *
from faithfulness import *

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
        print(".... The axioms in the normative basis are: ", ", ".join([i.toString() for i in normativeBasis]))
        explanation = {}
        foundExplanation = False

        axiomsOutcome, axiomsAlternative = self.splitAxioms(normativeBasis)

        for axiom in axiomsOutcome:
            winner, instance = axiom.getWinner(self.profile, self.nbAlternatives, self.nbVoters)
            if Counter([winner]) == Counter(self.outcome):
                explanation[axiom] = [instance]
                foundExplanation = True
        
        posOutcomes = list(allSublists(self.profile[0]))
        # Delete target outcome from possible outcomes 
        posOutcomes = removeOutcome(posOutcomes, self.outcome)

        posExplanation = []
        for axiom in axiomsAlternative:
            alternative, instance = axiom.getAlternative(self.profile, self.nbAlternatives, self.nbVoters)
            copyPosOutcomes = posOutcomes.copy()
            for outcome in copyPosOutcomes:
                for alt in alternative:
                    if alt in outcome and outcome in posOutcomes:
                        posOutcomes.remove(outcome)
                        posExplanation.append((axiom, instance))

        if posOutcomes == []:
            for axiom, instance in posExplanation:
                explanation[axiom] = instance
            foundExplanation = True
        
        if foundExplanation:
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
                    key.printInstance(instance)
                print()



par = ParetoAxiom()
con = CondorcetAxiom()
faith = Faithfulness()
normativeBasis = [par, con, faith]

thing = FINDJUST([[1,0,2], [1, 2, 0]], [1])
exp = thing.solve(normativeBasis)
thing.printExplanation(exp)
