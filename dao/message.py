from dao.person import PersonDAO
from dao.groups import GroupDAO

class MessageDAO:
    def __init__(self):
        persons = PersonDAO().getAllPersons()
        groups = GroupDAO().getAllGroups()
        M1 = [3,'Hola bebe como tu estas?', '1970-01-01 00:00:01', 'NULL',persons[0][0], groups[0][0]]
        M2 = [12,'Entra al cuarto y subele el volumen al radio', '2001-12-04 03:02:22', 'https://ibb.co/cN3MkS',persons[1][0], groups[0][0]]
        M3 = [53, 'Ahahahaha lol!', '2018-01-04 10:30:10', 'NULL',persons[3][0], groups[1][0]]
        M4 = [102, 'Llego Santa Claus temprano!! :)', '2017-01-04 09:00:00', 'NULL', persons[4][0], groups[1][0]]
        M5 = [209, 'Eres una bestia en ICOM5016', '2010-01-04 02:34:07', 'NULL', persons[2][0], groups[2][0]]
        self.data = []
        self.data.append(M1)
        self.data.append(M2)
        self.data.append(M3)
        self.data.append(M4)
        self.data.append(M5)

    def getAllMessages(self):
        return self.data

    def getMessagesById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None

    def getMessageByGroup(self,gID):
        groupExist = GroupDAO().verify(gID)
        if groupExist:
            messages = MessageDAO().getAllMessages()
            messagesOfGroup =[]
            for m in messages:
                if(m[5]==gID):
                    messagesOfGroup.append(m)
            return messagesOfGroup
        return None


    def insert(self, mText, timedate, multimedia, posterID,groupID):
        # cursor = self.conn.cursor()
        # query = "insert into Person(pFirstName, pLastName, pPhone, pEmail) values (%s, %s, %s, %s) returning pid;"
        # cursor.execute(query, (pFirstName, pLastName, pPhone, pEmail))
        # pid = cursor.fetchone()[0]
        # self.conn.commit()
        pid = 310
        return pid

    def verify(self,posterID,groupID):
        return PersonDAO().verify(int(posterID)) and GroupDAO().verify(int(groupID))
