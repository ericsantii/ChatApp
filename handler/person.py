from flask import jsonify, request
from dao.person import PersonDAO


class PersonHandler:
    def mapToDict(self, row):
        result = {}
        result['pID'] = row[0]
        result['pFirstName'] = row[1]
        result['pLastName'] = row[2]
        result['username'] = row[3]
        result['password'] = row[4]
        result['pPhone'] = row[5]
        result['pEmail'] = row[6]
        return result

    def mapToMessageDict(self, row):
        result = {}
        result['mID'] = row[0]
        result['mText'] = row[1]
        result['timedate'] = row[2]
        result['multimedia'] = row[3]
        result['pID'] = row[4]
        result['gID'] = row[5]
        return result

    def mapToGroupDict(self, row):
        result = {}
        result['gID'] = row[0]
        result['gName'] = row[1]
        result['pID'] = row[2]
        return result

    def mapToReactDict(self, row):
        result = {}
        result['mID'] = row[0]
        result['pID'] = row[1]
        result['rType'] = row[2]
        return result

    def getAllPersons(self):
        dao = PersonDAO()
        result = dao.getAllPersons()
        if not result:
            return jsonify(Error="Person NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Person=mapped_result)

    def getPersonById(self, pID):
        dao = PersonDAO()
        result = dao.getPersonById(pID)
        if result is None:
            return jsonify(Error="Person NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Person=mapped)

    def getGroupsByPersonID(self, pID):
        dao = PersonDAO()
        if not dao.getPersonById(pID):
            return jsonify(Error="Person NOT FOUND"), 404
        groups_list = dao.getGroupsByPersonID(pID)
        if not groups_list:
            return jsonify(Error="Group NOT FOUND"), 404
        results = []
        for row in groups_list:
            result = self.mapToGroupDict(row)
            results.append(result)
        return jsonify(Group=results)

    def getReactsByPersonID(self, pID):
        dao = PersonDAO()
        if not dao.getPersonById(pID):
            return jsonify(Error="Person NOT FOUND"), 404
        reacts_list = dao.getReactsByPersonID(pID)
        if not reacts_list:
            return jsonify(Error="React NOT FOUND"), 404
        results = []
        for row in reacts_list:
            result = self.mapToReactDict(row)
            results.append(result)
        return jsonify(React=results)

    def getMessagesByPersonID(self, pID):
        dao = PersonDAO()
        if not dao.getPersonById(pID):
            return jsonify(Error="Person NOT FOUND"), 404
        message_list = dao.getMessagesByPersonID(pID)
        if not message_list:
            return jsonify(Error="Message NOT FOUND"), 404
        results = []
        for row in message_list:
            result = self.mapToMessageDict(row)
            results.append(result)
        return jsonify(Message=results)

    def getContactsByPersonID(self, pID):
        dao = PersonDAO()
        if not dao.getPersonById(pID):
            return jsonify(Error="Person NOT FOUND"), 404
        contact_list = dao.getContactsByPersonID(pID)
        if contact_list is None:
            return jsonify(Error="Contact NOT FOUND"), 404
        results = []
        for row in contact_list:
            result = self.mapToDict(row)
            results.append(result)
        return jsonify(Persons=results)




