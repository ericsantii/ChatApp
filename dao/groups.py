import psycopg2

from config.dbconfig import pg_config


class GroupDAO:
    def __init__(self):
        DATABASE_URL = 'postgres://zftpdfatjwqsqn:6392cffdaac746ec46a140c526c4ef71b595543eb05feb5f223bf7ac1a3e323c@ec2-54-225-96-191.compute-1.amazonaws.com:5432/dg5rkiotg2tr8'
        self.conn = psycopg2._connect(DATABASE_URL)


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
        query = "select distinct pID, username, pFirstName, pLastName, pPhone, pEmail from Person natural inner join ChatGroup where gID = %s;"
        cursor.execute(query, (gID,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getMessagesByGroupID(self, gID):
        cursor = self.conn.cursor()
        query = "select pid, mid, numoflikes, numofdislikes, mtext, timedate, username, pfirstName, pLastName from " \
                "(select message.mID, count(sub1.mID) as numOfLikes from message left join " \
                "(select * from react where rTYpe = true) as sub1 on MESSAGE.mID = sub1.mID group by message.mID) as sub2 " \
                "natural inner join (select message.mID, count(sub1.mID) as numOfDislikes from message " \
                "left join (select * from react where rTYpe = false) as sub1 on MESSAGE.mID = sub1.mID group by message.mID) as sub3 " \
                "natural INNER JOIN message natural inner join person where gID = %s order by timedate desc;"

        cursor.execute(query, (gID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPeopleByGroupID(self, gID):
        cursor = self.conn.cursor()
        query = "select pID, username, password, pFirstName, pLastName, pPhone, pEmail from Person natural inner join isMember where gID = %s;"
        cursor.execute(query, (gID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllOwners(self):
        cursor = self.conn.cursor()
        query = "select distinct pID, username, pFirstName, pLastName, pPhone, pEmail from ChatGroup natural inner join Person;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def addMember(self, pID, gID):
        cursor = self.conn.cursor()
        query = "insert into isMember values (%s, %s) returning pID, gID"
        cursor.execute(query, (pID, gID,))
        result = cursor.fetchone()
        (pid, gid) = result[0], result[1]
        self.conn.commit()
        return pid, gid

    def closeDB(self):
        self.conn.close()
