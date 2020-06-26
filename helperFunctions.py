# 
# Functions that are used in various files, mainly to encode the restrictions
# of the axioms. Some code is taken from the slides of Ulle Endriss
# https://staff.science.uva.nl/u.endriss/teaching/comsoc/2020/slides/comsoc-automated-reasoning-2020.pdf

from itertools import combinations, permutations, chain, product
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

# Return preference number of agent i in profile r
def preference(i, r, m):
    base = factorial(m)
    return ( r % (base ** (i+1)) ) // (base ** i)

# Return preferences of agent i in profile r as list
def preflist(i, r, m):
    preflists = list(permutations(allAlternatives(m)))
    return preflists[preference(i, r, m)]

# Return True if agent i prefers x over y in profile r
def prefers2(i, x, y, r, m):
    prefList = preflist(i, r, m)
    return prefList.index(x) < prefList.index(y)

# Return alternatives that satisfy the condition
def alternatives(m, condition):
    return [x for x in allAlternatives(m) if condition(x)]

# Return voters that satisfy the condition
def voters(n, condition):
    return [i for i in allVoters(n) if condition(i)]

# Return all profile numbers that satisfy the condition
def profiles(m, n, condition):
    return [i for i in allProfiles(m, n) if condition(i)]

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

# Return all profile numbers
def allProfiles(m, n):
    return range(factorial(m) ** n)

# Return alternative that is Pareto dominated in profile by x
def isDominated(x, profile):
    nbAlternatives = profile.nbAlternatives
    nbVoters = profile.nbVoters
    for y in allAlternatives(nbAlternatives):
        dominated = 0
        for i in allVoters(nbVoters):
            if prefers(i, y, x, profile.listProfile):
                dominated += 1
        if dominated == nbVoters:
            return y
    return -1
    
# Encode positive literal
def posLiteral(r, x, m):
    return r * m + x + 1

# Encode negative literal
def negLiteral(r, x, m):
    return (-1) * posLiteral(r, x, m)

# Return list of all profiles
def listAllProfiles(profile):
    start = [sorted(profile[0]) for _ in range(len(profile))]
    sub_permutations = ([list(p) for p in permutations(l)] for l in start)
    allProfiles = [list(v) for v in product(*sub_permutations)]
    return allProfiles