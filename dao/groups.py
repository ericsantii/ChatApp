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

    def insert(self,gName):

        gid = random.randint(1,102)
        return gid



