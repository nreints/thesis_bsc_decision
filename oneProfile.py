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
        print("............ Trying to find a justification .........")
        print("\t.... The target profile is: ", self.profile)
        print("\t.... The target outcome is: ", self.outcome)
        print("\t.... The axioms in the normative basis are: ", ", ".join([axiom.toString() for axiom in normativeBasis]))
        explanation, normBasis = {}, {}
        nbExp = 0

        # allInstances = self.getAllInstances(normativeBasis)

        axiomsOutcome, axiomsAlternative = self.splitAxioms(normativeBasis)
        
        for axiom in axiomsOutcome:
            instances = axiom.getInstances(self.profile, self.nbAlternatives, self.nbVoters)
            if instances:
                for instance in instances:
                    winner = instance.alternatives
                    if Counter(winner) == Counter(self.outcome):
                        explanation[nbExp] = [instance]
                        normBasis[nbExp] = axiom
                        nbExp += 1
        
        posOutcomes = list(allSublists(self.profile[0]))

        # Delete target outcome from possible outcomes
        posOutcomes = removeOutcome(posOutcomes, self.outcome)

        posExplanation = []
        for axiom in axiomsAlternative:
            instances = axiom.getInstances(self.profile, self.nbAlternatives, self.nbVoters)
            if instances:
                for i in range(len(instances)):
                    alternative = instances[i].alternatives
                    lenBefore = len(posOutcomes)
                    posOutcomes = [outcome for outcome in posOutcomes if alternative not in outcome]
                    if len(posOutcomes) < lenBefore:
                        posExplanation.append(instances[i])
                if posOutcomes == []:
                    explanation[nbExp] = posExplanation
                    normBasis[nbExp] = axiom
                    nbExp += 1
        return explanation, normBasis

    # Spit normative basis
    def splitAxioms(self, normativeBasis):
        axiomsOutcome, axiomsAlternative = [], []
        for axiom in normativeBasis:
            if axiom.type == "outcome":
                axiomsOutcome.append(axiom)
            elif axiom.type == "alternative":
                axiomsAlternative.append(axiom)
        return axiomsOutcome, axiomsAlternative

    # Find all instances given a normative basis
    def getAllInstances(self, normativeBasis):
        allInstances = []
        for axiom in normativeBasis:
            allInstances.append(axiom.getInstances(self.profile, self.nbAlternatives, self.nbVoters))
        print(allInstances)
        return allInstances

    # Print explanation
    def printExplanation(self, exp, normBasis):
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
        if not exp:
            print("No explanation found")
        else:
            for key in exp:
                print("Found an explanation of size ", len(exp[key]), ":")
                print("Normative basis : ", normBasis[key].description)
                for instance in exp[key]:
                    instance.toString()
                print()



par = ParetoAxiom()
con = CondorcetAxiom()
faith = Faithfulness()
can = Cancellation()
normativeBasis = [par, con, faith, can]

thing = FINDJUST([[2,0,1], [2,1,0]], [2])
exp, normBasis = thing.solve(normativeBasis)
thing.printExplanation(exp, normBasis)
