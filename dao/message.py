import psycopg2

from config.dbconfig import pg_config


class MessageDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllMessages(self):
        cursor = self.conn.cursor()
        query = "select * from message;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageById(self, mID):
        cursor = self.conn.cursor()
        query = "select * from message where mID = %s;"
        cursor.execute(query, (mID,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getReactsByMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select * from react where mID = %s;"
        cursor.execute(query, (mID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRepliesByMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select mID, mText, timedate, multimedia, pID, gID from message as m, reply as r where m.mID = r.replyMessageID and r.originalMessageID = %s;"
        cursor.execute(query, (mID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOriginalMessageByReplyID(self, rID):
        cursor = self.conn.cursor()
        query = "select mID, mText, timedate, multimedia, pID, gID from message as m, reply as r where m.mID = r.originalMessageID and r.replyMessageID = %s;"
        cursor.execute(query, (rID,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    ###############
    # CHECK RETURN

    def getNumofLikesbyMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select count(*) as NumOfLikes from react where mID = %s and rType = %s;"
        cursor.execute(query, (mID, True))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getNumofDislikesbyMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select count(*) as NumOfDislikes from react where mID = %s and rType = %s;"
        cursor.execute(query, (mID, False))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getPersonWhoLikedMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select pID, username, passwd, pFirstName, pLastName, pPhone, pEmail from Person natural inner join react where rType = %s and mID = $s;"
        cursor.execute(query, (True, mID,))
        result = []
        for row in cursor:
            return None
        return result

    def getPersonWhoDislikedMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select pID, username, passwd, pFirstName, pLastName, pPhone, pEmail " \
                "from Person natural inner join react where rType = %s and mID = %s;"
        cursor.execute(query, (False, mID,))
        result = []
        for row in cursor:
            return None
        return result

    def getMessagesPostedByPersoninGroupID(self, mID, gID):
        cursor = self.conn.cursor()
        query = "select mID from Message where mID = %s and gID = %s"
        cursor.execute(query, (mID, gID))
        result = []
        for row in cursor:
            return None
        return result
