from itertools import permutations, product
import numpy as np

class profile:

    def __init__(self, listProfile, allProfiles):
        self.listProfile = listProfile
        # self.id = 2
        self.id = allProfiles.index(listProfile)
        # print(allProfiles[self.id])
        self.nbVoters = len(listProfile)
        self.nbAlternatives = len(listProfile[0])

    def getList(self):
        return self.listProfile

    def toString(self):
        return str(self.listProfile)
