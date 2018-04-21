import psycopg2
from config.dbconfig import pg_config


class PersonDAO:
    def __init__(self):

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


