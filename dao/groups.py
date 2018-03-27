from flask import jsonify
from dao.person import PersonDAO


class GroupDAO:
    def __init__(self):

        G1 = [111, 'Los recoge escombros', 1]
        G2 = [112, 'Fortnite PR', 5]
        G3 = [113, 'Los RG4L', 10]

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

    def getOwnerByGroupId(self):
        dao = PersonDAO()
        grouplist = self.getAllGroups()
        mapped_result = []
        for r in grouplist:
            mapped_result.append(dao.getPersonById(r[2]))

        return mapped_result

    def verify(self, gID):
        groups = GroupDAO().getAllGroups()
        for r in groups:
            if gID == r[0]:
                return True
        return False

    def getPeopleByGroupID(self, gID):
        if gID == 111:
            return [[1, 'Luis', 'Vega', '787-634-1091', 'luis.vega5@upr.edu']]
        elif gID == 112:
            T = []
            T.append([1, 'Luis', 'Vega', '787-634-1091', 'luis.vega5@upr.edu'])
            T.append([10, 'Fernando', 'Ortiz', '122-059-9031', 'fernando.ortiz@upr.edu'])
            return T
        elif gID == 113:
            T = []
            T.append([1, 'Luis', 'Vega', '787-634-1091', 'luis.vega5@upr.edu'])
            T.append([5, 'Eric', 'Santillana', '939-089-1011', 'eric.santillana@upr.edu'])
            T.append([10, 'Fernando', 'Ortiz', '122-059-9031', 'fernando.ortiz@upr.edu'])
            return T
        else:
            return []
