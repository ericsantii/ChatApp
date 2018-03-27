from flask import jsonify


class ContactHandler:

    def mapToDict(self, row):
        result = {}
        result['pID'] = row[0]
        result['cID'] = row[1]
        return result

    def mapToPersonDict(self, row):
        result = {}
        result['pID'] = row[0]
        result['pFirstName'] = row[1]
        result['pLastName'] = row[2]
        result['pPhone'] = row[3]
        result['pEmail'] = row[4]
        return result

    def build_contact_attributes(self, pID, cName):
        result = {}
        result['pID'] = pID
        result['cID'] = cName
        return result

    def build_owner_dict(self,row):
        result = {}
        result['oID'] = row[0]
        result['oFirstName'] = row[1]
        result['oLastName'] = row[2]
        result['oPhone'] = row[3]
        result['oEmail'] = row[4]
        return result

