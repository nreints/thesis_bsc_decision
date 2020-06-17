from itertools import combinations, permutations, chain, product
from math import factorial
from collections import Counter


# Return all voters
def allVoters(n):
    return range(n)


# Return all alternatives
def allAlternatives(m):
    return range(m)

def allProfilesNumber(m, n):
    return range(factorial(m) ** n)


# Return True if voter i prefers x over y, else False
def prefers(i, x, y, profile):
    return profile[i].index(x) < profile[i].index(y)

def preference(i, r, m):
    base = factorial(m)
    return ( r % (base ** (i+1)) ) // (base ** i)


def preflist(i, r, m):
    preflists = list(permutations(allAlternatives(m)))
    return preflists[preference(i, r, m)]

def prefers2(i, x, y, r, m):
    prefList = preflist(i, r, m)
    return prefList.index(x) < prefList.index(y)

# Return alternatives that satisfy the condition
def alternatives(m, condition):
    return [x for x in allAlternatives(m) if condition(x)]

# Return voters that satisfy the condition
def voters(n, condition):
    return [i for i in allVoters(n) if condition(i)]

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

def allProfiles(m, n):
    return range(factorial(m) ** n)


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
    

def posLiteral(r, x, m):
    return r * m + x + 1

def negLiteral(r, x, m):
    return (-1) * posLiteral(r, x, m)


def iVariants(i, r1, r2, m):
    return all(preference(j,r1, m) == preference(j,r2, m) for j in voters(m, lambda j : j != i))