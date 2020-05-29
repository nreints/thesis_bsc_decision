from helperFunctions import alternatives, allVoters, allAlternatives, prefers


class ParetoAxiom:

    def __init__(self):
        self.description = "Pareto Principle"
        self.type = "alternative"
        

    def getAlternative(self, profile, nbAlternatives, nbVoters):
        deleteAlternative = []
        instance = []
        for x in allAlternatives(nbAlternatives):
            for y in alternatives(nbAlternatives, lambda y : y != x):    
                dominated = 0
                for i in allVoters(nbVoters):
                    if prefers(i, x, y, profile):
                        dominated += 1
                if dominated == nbVoters and y not in deleteAlternative:
                    deleteAlternative.append(y)
                    instance.append((profile, x, y))
        return deleteAlternative, instance

    def printInstance(self, instance):
        print("In profile ", instance[0], ":", instance[2], " is dominated by ",  instance[1], "  (", self.description,")")

    def toString(self):
        return self.description