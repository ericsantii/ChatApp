

class HashTagDAO:
    def __init__(self):
        H1 = [1, 'TeamRubio',3]
        H2 = [2, 'Sobrevivi',12]
        H3 = [3, 'TeamRubio', 53]
        H4 = [4, 'Sobrevivi', 102]
        H5 = [5, 'TeamRubio', 209]

        self.data = []
        self.data.append(H1)
        self.data.append(H2)
        self.data.append(H3)
        self.data.append(H4)
        self.data.append(H5)

    def getAllHashsTags(self):
        return self.data

    def getHashTagByID(self,hID):
        for r in self.data:
            if hID == r[0]:
                return r
        return None

    def getHashTagList(self,mID):
        result = []
        for r in self.data:
            if r[2] == mID:
                result.append(r)
        return result