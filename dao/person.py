class PersonDAO:
    def __init__(self):
        P1 = [1, 'Luis', 'Vega', 'user1', '657rfv87tr76', '787-634-1091', 'luis.vega5@upr.edu']
        P2 = [5, 'Eric', 'Santillana', 'user2', '97yhiup87t', '939-089-1011', 'eric.santillana@upr.edu']
        P3 = [10, 'Fernando', 'Ortiz', 'user3', 'uig76r7ofvi', '122-059-9031', 'fernando.ortiz@upr.edu']
        P4 = [50, 'Luisa', 'Vargas', 'user4', 'yuti56r698', '787-777-1791', 'luisa.vargas@upr.edu']
        P5 = [95, 'Fico', 'Fronte', 'user5', 'rf87g90h', '787-123-4567', 'fico.fronte@gmail.edu']
        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)
        self.data.append(P4)
        self.data.append(P5)

    def getAllPersons(self):
        return self.data

    def getPersonById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None


    def getGroupsByPersonID(self, pID):
        if pID == 1:
            return [[113, 'Los RG4L', 10]]
        elif pID == 5:
            T = []
            T.append([112, 'Fortnite PR', 5])
            T.append([113, 'Los RG4L', 10])
            return T
        elif pID == 10:
            T = []
            T.append([111, 'Los recoge escombros', 1])
            T.append([113, 'Los RG4L', 10])
            T.append([112, 'Fortnite PR', 5])
            return T
        else:
            return None

    def getReactsByPersonID(self, pID):
        if pID == 1:
            return [[3, 1, True]]
        elif pID == 5:
            T = []
            T.append([12, 5, False])
            T.append([52, 'Los RG4L', True])
            return T
        elif pID == 10:
            T = []
            T.append([12, 10, True])
            T.append([53, 10, False])
            T.append([102, 10, True])
            T.append([200, 10, False])
            return T
        else:
            return None

    def getMessagesByPersonID(self, pID):
        if pID == 1:
            T = []
            T.append([3, 'Hola como tu estas?', '1970-01-01 00:00:01', 'NULL', 1, 111])
            return T
        elif pID == 5:
            T = []
            T.append([12, 'Subele el volumen al radio', '2001-12-04 03:02:22', 'https://ibb.co/cN3MkS', 5, 112])
            T.append([209, 'Eres una bestia en ICOM5016', '2010-01-04 02:34:07', 'NULL', 5, 113])
            return T
        elif pID == 10:
            T = []
            T.append([53, 'Ahahahaha lol!', '2018-01-04 10:30:10', 'NULL', 10, 112])
            T.append([102, 'Llego Santa Claus temprano!! :)', '2017-01-04 09:00:00', 'NULL', 10, 112])
            return T
        else:
            return None

    def getContactsByPersonID(self, pID):
        if pID == 1:
            T = []
            T.append([5, 'Eric', 'Santillana', 'user2', '97yhiup87t', '939-089-1011', 'eric.santillana@upr.edu'])
            return T
        elif pID == 5:
            T = []
            T.append([10, 'Fernando', 'Ortiz', 'user3', 'uig76r7ofvi', '122-059-9031', 'fernando.ortiz@upr.edu'])
            return T
        else:
            return None

    def getAllOwners(self):
        T = []
        T.append(self.P1)
        T.append(self.P2)
        T.append(self.P3)
        if not T:
            return None
        return T