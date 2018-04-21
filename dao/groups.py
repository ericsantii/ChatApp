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

