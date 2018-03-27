from dao.groups import PersonDAO


class ContactDAO:
    def __init__(self):
        # contact = [personid, contactid]

        c1 = [1, 5]
        c2 = [1, 10]
        c3 = [1, 50]
        c4 = [1, 95]
        c5 = [50, 5]

        self.data = []
        self.data.append(c1)
        self.data.append(c2)
        self.data.append(c3)
        self.data.append(c4)
        self.data.append(c5)

    def getAllContacts(self, pID):
        for r in self.data:
            if pID == r[0]:
                return r
        return None

    def getContactInfo(self, pid):
        persons = PersonDAO().getAllPersons()
        for r in self.data:
            if pid == r[0]:
                for p in persons:
                    if r[1] == p[0]:
                        return p
        return None
