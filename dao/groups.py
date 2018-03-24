import random
class GroupDAO:
    def  __init__(self):
        G1 = [111, 'Los recoge escombros']
        G2 = [112,'Fortnite PR']
        G3 = [113,'Los RG4L']

        self.data = []
        self.data.append(G1)
        self.data.append(G2)
        self.data.append(G3)


    def getAllGroups(self):
        return self.data

    def getGroupById(self, gid):
        for r in self.data:
            if gid == r[0]:
                return r
        return None

    def insert(self,gName):
        gid = random.randint(1,102)
        G4 = [gid,gName]
        self.data.append(G4)
        return gid



