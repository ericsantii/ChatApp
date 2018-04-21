import psycopg2

from config.dbconfig import pg_config


class GroupDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllGroups(self):
        cursor = self.conn.cursor()
        query = "select * from ChatGroup;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGroupById(self, gID):
        cursor = self.conn.cursor()
        query = "select * from ChatGroup where gID = %s;"
        cursor.execute(query, (gID,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getOwnerByGroupId(self, gID):
        cursor = self.conn.cursor()
        query = "select distinct pID, username, passwd, pFirstName, pLastName, pPhone, pEmail from Person natural inner join ChatGroup where gID = %s;"
        cursor.execute(query, (gID,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getMessagesByGroupID(self, gID):
        cursor = self.conn.cursor()
        query = "select * from message where gID = %s;"
        cursor.execute(query, (gID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPeopleByGroupID(self, gID):
        cursor = self.conn.cursor()
        query = "select pID, username, passwd, pFirstName, pLastName, pPhone, pEmail from Person natural inner join isMember where gID = %s;"
        cursor.execute(query, (gID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOwners(self):
        cursor = self.conn.cursor()
        query = "select distinct pID, username, passwd, pFirstName, pLastName, pPhone, pEmail from ChatGroup natural inner join Person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

