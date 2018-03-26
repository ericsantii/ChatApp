from flask import jsonify
from dao.person import PersonDAO
class GroupDAO:
    def  __init__(self):

        persons = PersonDAO().getAllPersons()

        G1 = [111, 'Los recoge escombros',persons[0][0]]
        G2 = [112,'Fortnite PR',persons[2][0]]
        G3 = [113,'Los RG4L',persons[4][0]]

        self.data = []
        self.data.append(G1)
        self.data.append(G2)
        self.data.append(G3)


    def getAllGroups(self):
        return self.data

    def getGroupById(self, gID):
        for r in self.data:
            if gID == r[0]:
                return r
        return None

    def insert(self,gName,gOwner):
        gID = 200
        G4 = [gID,gName,gOwner]
        self.data.append(G4)
        return gID

    def delete(self,gID):
        return self.getGroupById(gID)

    def getOwnerByGroupId(self):
        dao = PersonDAO()
        grouplist = self.getAllGroups()
        mapped_result = []
        for r in grouplist:
            mapped_result.append(dao.getPersonById(r[2]))

        return mapped_result
    def verify(self, gID):
        groups = GroupDAO().getAllGroups()
        groupExist = False
        for r in groups:
            if gID == r[0]:
                return True
        return False





