from itertools import permutations, product
import numpy as np

class profile:

    def __init__(self, listProfile, allProfiles):
        self.listProfile = listProfile
        # self.id = 2
        self.id = allProfiles.index(listProfile)
        self.nbVoters = len(listProfile)
        self.nbAlternatives = len(listProfile[0])

    def toString(self):
        return str(self.listProfile)
