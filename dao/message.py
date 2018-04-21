class MessageDAO:
    def __init__(self):
        M1 = [3, 'Hola como tu estas?', '1970-01-01 00:00:01', 'NULL', 1, 111]
        M2 = [12, 'Subele el volumen al radio', '2001-12-04 03:02:22', 'https://ibb.co/cN3MkS', 5, 112]
        M3 = [53, 'Ahahahaha lol!', '2018-01-04 10:30:10', 'NULL', 10, 112]
        M4 = [102, 'Llego Santa Claus temprano!! :)', '2017-01-04 09:00:00', 'NULL', 10, 112]
        M5 = [209, 'Eres una bestia en ICOM5016', '2010-01-04 02:34:07', 'NULL', 5, 113]
        self.data = []
        self.data.append(M1)
        self.data.append(M2)
        self.data.append(M3)
        self.data.append(M4)
        self.data.append(M5)

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
