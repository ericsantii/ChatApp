from flask import jsonify, request
from dao.person import PersonDAO
class PersonHandler:
    def mapToDict(self, row):
        result = {}
        result['pID'] = row[0]
        result['pFirstName'] = row[1]
        result['pLastName'] = row[2]
        result['pPhone'] = row[3]
        result['pEmail'] = row[4]
        return result

    def getAllPersons(self):
        dao = PersonDAO()
        result = dao.getAllPersons()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Person=mapped_result)

    def getPersonById(self, id):
        dao = PersonDAO()
        result = dao.getPersonById(id)
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDict(result)
            return jsonify(Person=mapped)

