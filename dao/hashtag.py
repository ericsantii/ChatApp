import psycopg2

from config.dbconfig import pg_config


class HashTagDAO:
    def __init__(self):
        DATABASE_URL = 'postgres://zftpdfatjwqsqn:6392cffdaac746ec46a140c526c4ef71b595543eb05feb5f223bf7ac1a3e323c@ec2-54-225-96-191.compute-1.amazonaws.com:5432/dg5rkiotg2tr8'
        self.conn = psycopg2._connect(DATABASE_URL)


    def getAllHashTags(self):
        cursor = self.conn.cursor()
        query = "select * from HashTag;"
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
        query = "select * from HashTag where mID = %s;"
        cursor.execute(query, (mID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMessageByHashTag(self, text):
        cursor = self.conn.cursor()
        query = "select mID, mText, timedate, multimedia, pID, gID from message as m natural inner join contains as c natural inner join hashtag where hText = %s;"
        cursor.execute(query, (text,))
        result = []
        for row in cursor:
            result.append(row)
        return result
