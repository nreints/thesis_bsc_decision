from helperFunctions import alternatives, allAlternatives, prefers, allVoters

class CondorcetAxiom:

    def __init__(self):
        self.description = "Condorcet Principle"
        self.type = "outcome"
        

    def getWinner(self, profile, nbAlternatives, nbVoters):
        for x in allAlternatives(nbAlternatives):
            timesY = 0
            for y in alternatives(nbAlternatives, lambda y: x != y):
                voters = 0
                for i in allVoters(nbVoters):
                    if prefers(i, x, y, profile):
                        voters += 1
                if voters > (nbVoters/2):
                    timesY += 1
            if timesY == nbAlternatives - 1:
                return x, (profile, x, alternatives(nbAlternatives, lambda y: y != x))
        return None, ()

    def printInstance(self, instance):
        print("In profile ", instance[0], ": the majority of voters prefers ", instance[1], " over ",  str(instance[2]), "  (", self.description,")")

    def toString(self):
        return self.description