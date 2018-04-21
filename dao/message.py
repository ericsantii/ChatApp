class MessageDAO:
    def __init__(self):
        M1 = [3, 'Hola como tu estas?', '1970-01-01 00:00:01', 'NULL', 1, 111]
        M2 = [12, 'Subele el volumen al radio #Sobrevivi', '2001-12-04 03:02:22', 'https://ibb.co/cN3MkS', 5,112]
        M3 = [53, 'Ahahahaha lol!', '2018-01-04 10:30:10#TeamRubio', 'NULL', 10, 112]
        M4 = [102, 'Llego Santa Claus temprano!!#Sobrevivi :)', '2017-01-04 09:00:00', 'NULL', 10, 112]
        M5 = [209, 'Eres una bestia en ICOM5016 #TeamRubio', '2010-01-04 02:34:07', 'NULL', 5, 113]
        self.data = []
        self.data.append(M1)
        self.data.append(M2)
        self.data.append(M3)
        self.data.append(M4)
        self.data.append(M5)

    def getAllMessages(self):
        return self.data

    def getMessageById(self, id):
        for r in self.data:
            if id == r[0]:
                return r
        return None


    def getReactsByMessageID(self, mID):
        if mID == 3:
            return [[3, 1, True]]
        elif mID == 12:
            T = []
            T.append([12, 5, False])
            T.append([12, 10, True])
            return T
        elif mID == 53:
            T = []
            T.append([53, 10, False])

            return T
        elif mID == 102:
            T = []
            T.append([102, 10, True])
            return T
        elif mID == 209:
            T = []
            T.append([209, 10, False])
            return T
        else:
            return None

    def getRepliesByMessageID(self, mID):
        if mID == 3:
            T = []
            T.append([12, 'Entra al cuarto y subele el volumen al radio', '2001-12-04 03:02:22', 'https://ibb.co/cN3MkS', 5,112])
            return T
        elif mID == 12:
            T = []
            T.append([53, 'Ahahahaha lol!', '2018-01-04 10:30:10', 'NULL', 10, 112])
            T.append([102, 'Llego Santa Claus temprano!! :)', '2017-01-04 09:00:00', 'NULL', 10, 112])

            return T

        else:
            return None

    def getOriginalMessageByReplyID(self, rID):
        if rID == 12:
            result = [3, 'Hola bebe como tu estas?', '1970-01-01 00:00:01', 'NULL', 1, 111]
            return result

        elif rID == 53 or rID == 102:
            result = [12, 'Entra al cuarto y subele el volumen al radio', '2001-12-04 03:02:22','https://ibb.co/cN3MkS', 5, 112]
            return result

        else:
            return None

