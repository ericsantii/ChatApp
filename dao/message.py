import psycopg2

from config.dbconfig import pg_config


class MessageDAO:
    def __init__(self):
        DATABASE_URL = 'postgres://zftpdfatjwqsqn:6392cffdaac746ec46a140c526c4ef71b595543eb05feb5f223bf7ac1a3e323c@ec2-54-225-96-191.compute-1.amazonaws.com:5432/dg5rkiotg2tr8'
        self.conn = psycopg2._connect(DATABASE_URL)


    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "select * from message;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        self.closeDB()
        return result

    def getMessageById(self, mID):
        cursor = self.conn.cursor()
        query = "select * from message where mID = %s;"
        cursor.execute(query, (mID,))
        result = cursor.fetchone()
        if not result:
            self.closeDB()
            return None

        self.closeDB()
        return result

    def getReactsByMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select * from react where mID = %s;"
        cursor.execute(query, (mID,))
        result = []
        for row in cursor:
            result.append(row)
        self.closeDB()
        return result

    def getRepliesByMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select mID, mText, timedate, multimedia, pID, gID from message as m, reply as r where m.mID = r.replyMessageID and r.originalMessageID = %s;"
        cursor.execute(query, (mID,))
        result = []
        for row in cursor:
            result.append(row)
        self.closeDB()
        return result

    def getOriginalMessageByReplyID(self, rID):
        cursor = self.conn.cursor()
        query = "select mID, mText, timedate, multimedia, pID, gID from message as m, reply as r where m.mID = r.originalMessageID and r.replyMessageID = %s;"
        cursor.execute(query, (rID,))
        result = cursor.fetchone()
        if not result:
            self.closeDB()
            return None
        self.closeDB()
        return result

    ###############
    # CHECK RETURN

    def getNumofLikesbyMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select count(*) as NumOfLikes from react where mID = %s and rType = %s;"
        cursor.execute(query, (mID, True))
        result = cursor.fetchone()
        if not result:
            self.closeDB()
            return None
        self.closeDB()
        return result

    def getNumofDislikesbyMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select count(*) as NumOfDislikes from react where mID = %s and rType = %s;"
        cursor.execute(query, (mID, False))
        result = cursor.fetchone()
        if not result:
            self.closeDB()
            return None
        self.closeDB()
        return result

    def getPersonWhoLikedMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select pID, username, passwd, pFirstName, pLastName, pPhone, pEmail from Person natural inner join react where rType = %s and mID = $s;"
        cursor.execute(query, (True, mID,))
        result = []
        for row in cursor:
            self.closeDB()
            return None
        self.closeDB()
        return result

    def getPersonWhoDislikedMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select pID, username, passwd, pFirstName, pLastName, pPhone, pEmail " \
                "from Person natural inner join react where rType = %s and mID = %s;"
        cursor.execute(query, (False, mID,))
        result = []
        for row in cursor:
            self.closeDB()
            return None
        self.closeDB()
        return result

    def getMessagesPostedByPersoninGroupID(self, mID, gID):
        cursor = self.conn.cursor()
        query = "select mID from Message where mID = %s and gID = %s"
        cursor.execute(query, (mID, gID))
        result = []
        for row in cursor:
            self.closeDB()
            return None
        self.closeDB()
        return result
