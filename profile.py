from helperFunctions import listAllProfiles

class profile:

    def __init__(self, listProfile):
        self.listProfile = listProfile
        self.id = listAllProfiles(listProfile).index(listProfile)
        self.nbVoters = len(listProfile[0])
        self.nbAlternatives = len(listProfile)

    def toString(self):
        return str(self.listProfile)
