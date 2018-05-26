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
        query = "select mID, mText, timedate, pID, gID from message as m, reply as r where m.mID = r.replyMessageID and r.originalMessageID = %s;"
        cursor.execute(query, (mID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getOriginalMessageByReplyID(self, rID):
        cursor = self.conn.cursor()
        query = "select mID, mText, timedate, pID, gID from message as m, reply as r where m.mID = r.originalMessageID and r.replyMessageID = %s;"
        cursor.execute(query, (rID,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    ###############
    # CHECK RETURN

    def getNumofLikesbyMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select count(*) as NumOfLikes from react where mID = %s and rType = True;"
        cursor.execute(query, (mID,))
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
        query = "select pID, pFirstName, pLastName, username, pEmail from Person natural inner join react where rType = True and mID = %s;"
        cursor.execute(query, (mID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPersonWhoDislikedMessageID(self, mID):
        cursor = self.conn.cursor()
        query = "select pID, pFirstName, pLastName, username, pEmail from Person natural inner join react where rType = False and mID = %s;"
        cursor.execute(query, (mID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessagesPostedByPersoninGroupID(self, mID, gID):
        cursor = self.conn.cursor()
        query = "select * from Message where mID = %s and gID = %s"
        cursor.execute(query, (mID, gID))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def addMessage(self, mtext, pid, gid):
        cursor = self.conn.cursor()
        query = "insert into Message(mtext, timedate, pid, gid) values (%s, now(), %s, %s) returning mID, timedate"
        cursor.execute(query, (mtext, pid, gid,))
        result = cursor.fetchone()
        (mID, timedate) = result[0], result[1]
        self.conn.commit()
        return mID, timedate

    def likeMessage(self, pID, mID):
        cursor = self.conn.cursor()
        query = "insert into react values (%s, %s, true, now()) returning pID, mID, rType"
        cursor.execute(query, (mID, pID,))
        result = cursor.fetchone()
        (pid, gid, rType) = result[0], result[1], result[2]
        self.conn.commit()
        return pid, gid, rType

    def dislikeMessage(self, pID, mID):
        cursor = self.conn.cursor()
        query = "insert into react values (%s, %s, false, now()) returning pID, mID, rType"
        cursor.execute(query, (mID, pID,))
        result = cursor.fetchone()
        (pid, gid, rType) = result[0], result[1], result[2]
        self.conn.commit()
        return pid, gid, rType

    def getMessagesWithHashtagInGroupID(self, ht, gID):
        cursor = self.conn.cursor()
        query = "select pid, mid, numoflikes, numofdislikes, mtext, timedate, username, pfirstName, " \
                "pLastName from (select message.mID, count(sub1.mID) as numOfLikes from message left join " \
                "(select * from react where rTYpe = true) as sub1 on MESSAGE.mID = sub1.mID group by message.mID) as sub2 " \
                "natural inner join (select message.mID, count(sub1.mID) as numOfDislikes from message" \
                " left join (select * from react where rTYpe = false) as sub1 on MESSAGE.mID = sub1.mID group by message.mID) as sub3 " \
                "natural INNER JOIN message natural inner join person natural inner join contains natural " \
                "inner join hashtag  where gID = %s and htext = %s order by timedate desc;"
        cursor.execute(query, (gID, ht,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    def addMessageAsReply(self, originalMessageID, replyID):
        cursor = self.conn.cursor()
        query = "insert into reply values (%s, %s) returning originalmessageid, replymessageid;"
        cursor.execute(query, (originalMessageID, replyID))
        result = cursor.fetchone()
        (oid, rid) = result[0], result[1]
        self.conn.commit()
        return oid,rid

    def getNumOfMessagesPerDay(self):
        cursor = self.conn.cursor()
        query = "select DATE(timedate) as day, count(*) from message group by day order by day desc limit 7"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumOfRepliesPerDay(self):
        cursor = self.conn.cursor()
        query = "select DATE(timedate) as day, count(*) from (select * from message where mid in (select replymessageid from reply)) as replies group by day order by day desc limit 7"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumOfLikesPerDay(self):
        cursor = self.conn.cursor()
        query = "select DATE(time) as day, count(*) from react where rType = True group by day order by day desc limit 7"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumOfDislikesPerDay(self):
        cursor = self.conn.cursor()
        query = "select DATE(time) as day, count(*) from react where rType = False group by day order by day desc limit 7"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getNumOfActiveUsersPerDay(self):
        cursor = self.conn.cursor()
        query = "select DATE(timedate) as day, count(distinct pid) from message group by day order by day desc limit 7"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def closeDB(self):
        self.conn.close()