from itertools import combinations, permutations, chain
from math import factorial
from collections import Counter


# Return all voters
def allVoters(n):
    return range(n)


# Return all alternatives
def allAlternatives(m):
    return range(m)


# Return True if voter i prefers x over y, else False
def prefers(i, x, y, profile):
    return profile[i].index(x) < profile[i].index(y)


# Return alternatives that satisfy the condition
def alternatives(m, condition):
    return [x for x in allAlternatives(m) if condition(x)]

# Return voters that satisfy the condition
def voters(n, condition):
    return [i for i in allVoters(n) if condition(i)]


# Return all (non empty) sublists of list ## Copied from Boixel and Endriss
def allSublists(list):
    return chain(*(combinations(list, i) for i in range(1, len(list) + 1)))


# Remove outcome from list
def removeOutcome(posOutcomes, targOutcome):
    for outcome in posOutcomes:
        if (Counter(outcome) == Counter(targOutcome)):
            posOutcomes.remove(outcome)
            break
    return posOutcomes


# Return top alternative in preference
def topAlternative(profile):
    return profile[0]

def allProfiles(m, n):
    return range(factorial(m) ** n)

def listAllProfiles(profile):
    allProf = []
    for sub1 in list(permutations(range(len(profile[0])))):
        for sub2 in list(permutations(range(len(profile[0])))):
            allProf += [[list(sub1), list(sub2)]]
    return allProf