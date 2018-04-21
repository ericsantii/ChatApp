import psycopg2
from config.dbconfig import pg_config


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

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPersons(self):
        cursor = self.conn.cursor()
        query = "select * from Person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPersonById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from Person where pID = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getGroupsByPersonID(self, pID):
        cursor = self.conn.cursor()
        query = "select * from ChatGroup natural inner join isMember where pID = %s;"
        cursor.execute(query, (pID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReactsByPersonID(self, pID):
        cursor = self.conn.cursor()
        query = "select * from react natural inner join Person natural inner join Message where pID = %s;"
        cursor.execute(query, (pID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesByPersonID(self, pID):
        cursor = self.conn.cursor()
        query = "select * from Messages where pID = %s;"
        cursor.execute(query, (pID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getContactsByPersonID(self, pID):
        cursor = self.conn.cursor()
        query = "select * from Person natural inner join hasContact where userID = %s;"
        cursor.execute(query, (pID,))
        result = []
        for row in cursor:
            result.append(row)
        return result


