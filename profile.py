class profile:
    'Represents a profile'

    def __init__(self, listProfile, allProfiles):
        self.listProfile = listProfile
        self.id = allProfiles.index(listProfile)
        self.nbVoters = len(listProfile)
        self.nbAlternatives = len(listProfile[0])

    # Return list of profile
    def getList(self):
        return self.listProfile

    # Return profile as string
    def toString(self):
        return str(self.listProfile)
