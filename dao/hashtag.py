import psycopg2

from config.dbconfig import pg_config


class HashTagDAO:
    def __init__(self):
        DATABASE_URL = 'postgres://zftpdfatjwqsqn:6392cffdaac746ec46a140c526c4ef71b595543eb05feb5f223bf7ac1a3e323c@ec2-54-225-96-191.compute-1.amazonaws.com:5432/dg5rkiotg2tr8'
        self.conn = psycopg2._connect(DATABASE_URL)


    def getAllHashTags(self):
        cursor = self.conn.cursor()
        query = "select * from hashtag;"
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getHashTagByID(self, hID):
        cursor = self.conn.cursor()
        query = "select * from HashTag where hID = %s;"
        cursor.execute(query, (hID,))
        result = cursor.fetchone()
        if not result:
            return None
        return result

    def getHashTagList(self, mID):
        cursor = self.conn.cursor()
        query = "select hID, hText from HashTag natural inner join contains where mID = %s;"
        cursor.execute(query, (mID,))
        result = []
        for row in cursor:
            result.append(row)

        return result

    def getMessageByHashTag(self, text):
        cursor = self.conn.cursor()
        query = "select pid, mid, numoflikes, numofdislikes, mtext, timedate, username, pfirstName, " \
                "pLastName from (select message.mID, count(sub1.mID) as numOfLikes from message left join " \
                "(select * from react where rTYpe = true) as sub1 on MESSAGE.mID = sub1.mID group by message.mID) as sub2 " \
                "natural inner join (select message.mID, count(sub1.mID) as numOfDislikes from message" \
                " left join (select * from react where rTYpe = false) as sub1 on MESSAGE.mID = sub1.mID group by message.mID) as sub3 " \
                "natural INNER JOIN message natural inner join person natural inner join contains natural " \
                "inner join hashtag  where gID = %s and htext = %s order by timedate desc;"
        cursor.execute(query, (text,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTopHashtags(self):
        cursor = self.conn.cursor()
        query = "select htext, count from (select hid, count(*) as count from contains group by hid) as num natural inner join hashtag order by count limit 10"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def closeDB(self):
        self.conn.close()