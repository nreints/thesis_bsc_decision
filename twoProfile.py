from collections import Counter
from helperFunctions import allSublists, allVoters, allAlternatives, removeOutcome
from pareto import *
from condorcet import *
from faithfulness import *
from cancellation import *
from neutrality import *
from anonymity import *


class FINDJUST2:
    
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
        for axiom in normativeBasis:
            instance = axiom.getInstances(self.profile, self.nbAlternatives, self.nbVoters)
            # print(axiom, instance)

        return 0, 0


par = ParetoAxiom()
con = CondorcetAxiom()
faith = Faithfulness()
can = Cancellation()
neu = Neutrality()
ano = Anonymity()
normativeBasis = [par, con, faith, can, neu, ano]

thing = FINDJUST2([[2,0,1], [0,2,1], [1,2,0], [0,1,2]], [2])
exp, normBasis = thing.solve(normativeBasis)
# thing.printExplanation(exp, normBasis)
