class PersonDAO:
    def __init__(self):
        P1 = [1, 'Luis','Vega', '787-634-1091', 'luis.vega5@upr.edu']
        P2 = [5, 'Eric', 'Santillana', '939-089-1011', 'eric.santillana@upr.edu']
        P3 = [10, 'Fernando', 'Ortiz', '122-059-9031', 'fernando.ortiz@upr.edu']


        self.data = []
        self.data.append(P1)
        self.data.append(P2)
        self.data.append(P3)


    def getAllPersons(self):
        return self.data

    def getPersonById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def insert(self,pFirstName, pLastName, pPhone, pEmail):
        # cursor = self.conn.cursor()
        # query = "insert into Person(pFirstName, pLastName, pPhone, pEmail) values (%s, %s, %s, %s) returning pid;"
        # cursor.execute(query, (pFirstName, pLastName, pPhone, pEmail))
        # pid = cursor.fetchone()[0]
        # self.conn.commit()
        pid = 30
        return pid

    def verify(self, pID):
        persons = PersonDAO().getAllPersons()
        for r in persons:
            if pID == r[0]:
                return True
        return False

    def getGroupsByPersonID(self, pID):
        if pID == 1:
            return [[113,'Los RG4L', 10]]
        elif pID == 5:
            T = []
            T.append([112,'Fortnite PR', 5])
            T.append([113,'Los RG4L', 10])
            return T
        elif pID == 10:
            T = []
            T.append([111, 'Los recoge escombros', 1])
            T.append([113, 'Los RG4L', 10])
            T.append([112, 'Fortnite PR', 5])
            return T
        else:
            return []

    def getReactsByPersonID(self, pID):
        if pID == 1:
            return [[3, 1, True]]
        elif pID == 5:
            T = []
            T.append([12, 5, False])
            T.append([52,'Los RG4L', True])
            return T
        elif pID == 10:
            T = []
            T.append([12, 10, True])
            T.append([53, 10, False])
            T.append([102, 10, True])
            T.append([200, 10, False])
            return T
        else:
            return []