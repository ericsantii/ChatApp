import psycopg2

from config.dbconfig import pg_config


class HashTagDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

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
