from math import factorial
from itertools import permutations, combinations, chain
from collections import Counter

# Returns all voters
def allVoters(n):
    return range(n)

# Returns all alternatives
def allAlternatives(m):
    return range(m)

# Returns True if voter i prefers x over y, else False
def prefers(i, x, y, profile):
    return profile[i].index(x) < profile[i].index(y)

# Returns alternatives that satisfy the condition
def alternatives(m, condition):
    return [x for x in allAlternatives(m) if condition(x)]

# # Returns voters that satisfy the condition
# def voters(condition, n):
#     return [i for i in allVoters(n) if condition(i)]

# Return all (non empty) sublists of list ## COPIED FROM BOIXEL AND ENDRISS
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

