class GroupDAO:
    def __init__(self):

        G1 = [111, 'Group 1', 1]
        G2 = [112, 'Group 2', 5]
        G3 = [113, 'Group 3', 10]

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

    def getOwnerByGroupId(self, gID):
        if gID == 111:
            return [1, 'Luis', 'Vega', 'user1', '657rfv87tr76', '787-634-1091', 'luis.vega5@upr.edu']
        elif gID == 112:
            return [5, 'Eric', 'Santillana', 'user2', '97yhiup87t', '939-089-1011', 'eric.santillana@upr.edu']
        elif gID == 113:
            return [10, 'Fernando', 'Ortiz', 'user3', 'uig76r7ofvi', '122-059-9031', 'fernando.ortiz@upr.edu']
        else:
            return None

    def getMessagesByGroupID(self, gID):
        if gID == 111:
            return [[3, 'Hola como tu estas?', '1970-01-01 00:00:01', 'NULL', 1, 111]]
        elif gID == 112:
            T = []
            T.append([12, 'Subele el volumen al radio', '2001-12-04 03:02:22', 'https://ibb.co/cN3MkS', 5,112])
            T.append([53, 'Ahahahaha lol!', '2018-01-04 10:30:10', 'NULL', 10, 112])
            T.append([102, 'Llego Santa Claus temprano!! :)', '2017-01-04 09:00:00', 'NULL', 10, 112])
            return T
        elif gID == 113:
            T = []
            T.append([209, 'Eres una bestia en ICOM5016', '2010-01-04 02:34:07', 'NULL', 5, 113])

            return T
        else:
            return None

    def getPeopleByGroupID(self, gID):
        if gID == 111:
            return [[1, 'Luis', 'Vega', 'user1', '657rfv87tr76', '787-634-1091', 'luis.vega5@upr.edu']]
        elif gID == 112:
            T = []
            T.append([1, 'Luis', 'Vega', 'user2', '97yhiup87t','787-634-1091', 'luis.vega5@upr.edu'])
            T.append([10, 'Fernando', 'Ortiz', 'user3', 'uig76r7ofvi', '122-059-9031', 'fernando.ortiz@upr.edu'])
            return T
        elif gID == 113:
            T = []
            T.append([1, 'Luis', 'Vega', 'user1', '657rfv87tr76', '787-634-1091', 'luis.vega5@upr.edu'])
            T.append([5, 'Eric', 'Santillana', 'user2', '97yhiup87t', '939-089-1011', 'eric.santillana@upr.edu'])
            T.append([10, 'Fernando', 'Ortiz', 'user3', 'uig76r7ofvi', '122-059-9031', 'fernando.ortiz@upr.edu'])
            return T
        else:
            return None

    def getAllOwners(self):
        T = []
        T.append([1, 'Luis', 'Vega', 'user1', '657rfv87tr76', '787-634-1091', 'luis.vega5@upr.edu'])
        T.append([5, 'Eric', 'Santillana', 'user2', '97yhiup87t', '939-089-1011', 'eric.santillana@upr.edu'])
        T.append([10, 'Fernando', 'Ortiz', 'user3', 'uig76r7ofvi', '122-059-9031', 'fernando.ortiz@upr.edu'])
        if not T:
            return None
        return T

