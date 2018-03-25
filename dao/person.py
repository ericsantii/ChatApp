class PersonDAO:
    def __init__(self):
        P1 = [1, 'Luis','Vega', '787-634-1091', 'luis.vega5@upr.edu']
        P2 = [5, 'Eric', 'Santillana', '939-089-1011', 'eric.santillana@upr.edu']
        P3 = [10, 'Fernando', 'Ortiz', '122-059-9031', 'fernando.ortiz@upr.edu']
        P4 = [50, 'Petraca', 'Rivera', '787-990-293', 'mamichulitaexotica@gmail.edu']
        P5 = [95, 'Indy', 'Flow', '787-010-1111', 'laduraquita@hotmail.edu']

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

    def insert(self,pFirstName, pLastName, pPhone, pEmail):
        # cursor = self.conn.cursor()
        # query = "insert into Person(pFirstName, pLastName, pPhone, pEmail) values (%s, %s, %s, %s) returning pid;"
        # cursor.execute(query, (pFirstName, pLastName, pPhone, pEmail))
        # pid = cursor.fetchone()[0]
        # self.conn.commit()
        pid = 30
        return pid

