from itertools import permutations, product
import numpy as np
from collections import Counter

class profile:

    def __init__(self, listProfile, allProfiles):
        self.listProfile = listProfile
        self.id = allProfiles.index(listProfile)
        self.nbVoters = len(listProfile)
        self.nbAlternatives = len(listProfile[0])

    def getList(self):
        return self.listProfile

    def toString(self):
        return str(self.listProfile)
