import psycopg2
from config.dbconfig import pg_config


class PersonDAO:
    def __init__(self):
        DATABASE_URL = 'postgres://zftpdfatjwqsqn:6392cffdaac746ec46a140c526c4ef71b595543eb05feb5f223bf7ac1a3e323c@ec2-54-225-96-191.compute-1.amazonaws.com:5432/dg5rkiotg2tr8'
        self.conn = psycopg2._connect(DATABASE_URL)

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

    def getPersonById(self, username):
        cursor = self.conn.cursor()
        query = "select * from Person where username = %s;"
        cursor.execute(query, (username,))
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

    def closeDB(self):
        self.conn.close()
