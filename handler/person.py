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

    def build_person_attributes(self, pID, pFirstName, pLastName, pPhone, pEmail):
        result = {}
        result['pID'] = pID
        result['pFirstName'] = pFirstName
        result['pLastName'] = pLastName
        result['pPhone'] = pPhone
        result['pEmail'] = pEmail
        return result

    def mapToGroupDict(self, row):
        result = {}
        result['gID'] = row[0]
        result['gName'] = row[1]
        result['gOwner'] = row[2]
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
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Person=mapped_result)

    def getPersonById(self, args):
        dao = PersonDAO()
        result = dao.getPersonById(int(args.get('pID')))
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDict(result)
            return jsonify(Person=mapped)

    def CreateNewPerson(self,form):
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            pFirstName = form['pFirstName']
            pLastName = form['pLastName']
            pPhone = form['pPhone']
            pEmail = form['pEmail']
            if pFirstName and pLastName and pPhone and pEmail:
                dao = PersonDAO()
                pID = dao.insert(pFirstName, pLastName, pPhone, pEmail)
                result = {}
                result = self.build_person_attributes(pID, pFirstName, pLastName, pPhone, pEmail)
                return jsonify(Person=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def getGroupsByPersonID(self, pID):
        dao = PersonDAO()
        if not dao.getPersonById(pID):
            return jsonify(Error="Person Not Found"), 404
        groups_list = dao.getGroupsByPersonID(pID)
        results = []
        for row in groups_list:
            result = self.mapToGroupDict(row)
            results.append(result)
        return jsonify(GroupsForID= results)

    def getReactsByPersonID(self, pID):
        dao = PersonDAO()
        if not dao.getPersonById(pID):
            return jsonify(Error="Person Not Found"), 404
        reacts_list = dao.getReactsByPersonID(pID)
        results = []
        for row in reacts_list:
            result = self.mapToReactDict(row)
            results.append(result)
        return jsonify(ReactsForPerson= results)

