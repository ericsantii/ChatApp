from flask import jsonify, request
from dao.person import PersonDAO
from mapToDictFunctions import mapMessageToDict, mapPersonToDict, mapGroupToDict, mapToReactDict


class PersonHandler:


    def getAllPersons(self):
        dao = PersonDAO()
        result = dao.getAllPersons()
        if not result:
            dao.closeDB()
            return jsonify(Error="Person NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapPersonToDict(r))
        dao.closeDB()
        return jsonify(Person=mapped_result)


    def getPersonById(self, pID):
        dao = PersonDAO()
        result = dao.getPersonById(pID)
        if result is None:
            dao.closeDB()
            return jsonify(Error="Person NOT FOUND"), 404
        else:
            mapped = mapPersonToDict(result)
            dao.closeDB()
            return jsonify(Person=mapped)

    def getPersonByUsername(self, args):
        dao = PersonDAO()
        username = args.get('username')
        if not username or len(args) != 1:
            dao.closeDB()
            return jsonify(Error="Bad Request Arguments"), 400
        result = dao.getPersonByUsername(username)
        if result is None:
            dao.closeDB()
            return jsonify(Error="Person NOT FOUND"), 404
        else:
            mapped = mapPersonToDict(result)
            dao.closeDB()
            return jsonify(Person=mapped)

    def getGroupsByPersonID(self, pID):
        dao = PersonDAO()
        if not dao.getPersonById(pID):
            dao.closeDB()
            return jsonify(Error="Person NOT FOUND"), 404
        groups_list = dao.getGroupsByPersonID(pID)
        if not groups_list:
            dao.closeDB()
            return jsonify(Error="Group NOT FOUND"), 404
        results = []
        for row in groups_list:
            result = mapGroupToDict(row)
            results.append(result)
        dao.closeDB()
        return jsonify(Group=results)

    def getReactsByPersonID(self, pID):
        dao = PersonDAO()
        if not dao.getPersonById(pID):
            dao.closeDB()
            return jsonify(Error="Person NOT FOUND"), 404
        reacts_list = dao.getReactsByPersonID(pID)
        if not reacts_list:
            dao.closeDB()
            return jsonify(Error="React NOT FOUND"), 404
        results = []
        for row in reacts_list:
            result = mapToReactDict(row)
            results.append(result)
        dao.closeDB()
        return jsonify(React=results)

    def getMessagesByPersonID(self, pID):
        dao = PersonDAO()
        if not dao.getPersonById(pID):
            dao.closeDB()
            return jsonify(Error="Person NOT FOUND"), 404
        message_list = dao.getMessagesByPersonID(pID)
        if not message_list:
            dao.closeDB()
            return jsonify(Error="Message NOT FOUND"), 404
        results = []
        for row in message_list:
            result = mapMessageToDict(row)
            results.append(result)
        dao.closeDB()
        return jsonify(Message=results)

    def getContactsByPersonID(self, pID):
        dao = PersonDAO()
        if not dao.getPersonById(pID):
            dao.closeDB()
            return jsonify(Error="Person NOT FOUND"), 404
        contact_list = dao.getContactsByPersonID(pID)
        if contact_list is None:
            dao.closeDB()
            return jsonify(Error="Contact NOT FOUND"), 404
        results = []
        for row in contact_list:
            mappedResult = {}
            mappedResult['pID'] = row[0]
            mappedResult['username'] = row[1]
            mappedResult['pFirstName'] = row[2]
            mappedResult['pLastName'] = row[3]
            mappedResult['pPhone'] = row[4]
            mappedResult['pEmail'] = row[5]
            results.append(mappedResult)
        dao.closeDB()
        return jsonify(Persons=results)

    def loginUser(self, json):
        dao = PersonDAO()
        if len(json) != 2:
            dao.closeDB()
            return jsonify(Error="Malformed post request"), 400
        else:
            username = json['username']
            password = json['password']
            if username and password:
                result = dao.loginUser(username, password)
                if not result:
                    dao.closeDB()
                    return jsonify(Error="Error Not Found"), 404
                mapped = {}
                mapped['pID'] = result[0]
                mapped['authenticated'] = result[1]
                dao.closeDB()
                return jsonify(Authentication=mapped)
            else:
                dao.closeDB()
                return jsonify(Error="Unexpected attributes in post request"), 400


    def addPerson(self, json):
        dao = PersonDAO()
        if len(json) != 6:
            dao.closeDB()
            return jsonify(Error="Malformed post request"), 400
        else:
            username = json['username']
            password = json['password']
            firstname = json['pfirstname']
            lastname = json['plastname']
            phone = json['pphone']
            email = json['pemail']
            if username and password and firstname and lastname and phone and email:
                pid = dao.addPerson(username, password, firstname, lastname, phone, email)
                result = mapPersonToDict([pid, username, password, firstname, lastname, phone, email])
                dao.closeDB()
                return jsonify(Person=result), 201
            else:
                dao.closeDB()
                return jsonify(Error="Unexpected attributes in post request"), 400






