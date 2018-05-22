from flask import jsonify

from dao.groups import GroupDAO

from mapToDictFunctions import mapGroupToDict, mapMessageToDict, mapPersonToDict, mapMessageInfoToDict


class GroupHandler:


    def getAllGroups(self):
        dao = GroupDAO()
        group_list = dao.getAllGroups()
        if not group_list:
            dao.closeDB()
            return jsonify(Error="Group NOT FOUND"), 404
        result_list = []
        for row in group_list:
            result = mapGroupToDict(row)
            result_list.append(result)
        dao.closeDB()
        return jsonify(Group=result_list)

    def getGroupById(self, gid):
        dao = GroupDAO()
        result = dao.getGroupById(gid)
        if result is None:
            dao.closeDB()
            return jsonify(Error="Group NOT FOUND"), 404
        else:
            mapped = mapGroupToDict(result)
            dao.closeDB()
            return jsonify(Group=mapped)

    def getOwnerByGroupId(self, gID):
        dao = GroupDAO()
        result = dao.getOwnerByGroupId(gID)
        if result is None:
            dao.closeDB()
            return jsonify(Error="Group NOT FOUND"), 404

        mapperResult = {}
        mapperResult['pID'] = result[0]
        mapperResult['username'] = result[1]
        mapperResult['pFirstName'] = result[2]
        mapperResult['pLastName'] = result[3]
        mapperResult['pPhone'] = result[4]
        mapperResult['pEmail'] = result[5]
        dao.closeDB()
        return jsonify(Person=mapperResult)

    def getPeopleByGroupID(self, gID):
        dao = GroupDAO()
        if not dao.getGroupById(gID):
            dao.closeDB()
            return jsonify(Error="Group NOT FOUND"), 404
        person_list = dao.getPeopleByGroupID(gID)
        results = []
        for row in person_list:
            result = mapPersonToDict(row)
            results.append(result)
        dao.closeDB()
        return jsonify(Person=results)

    def getMessagesByGroupID(self, gID):
        dao = GroupDAO()
        if not dao.getGroupById(gID):
            dao.closeDB()
            return jsonify(Error="Group NOT FOUND"), 404
        message_list = dao.getMessagesByGroupID(gID)
        if not message_list:
            dao.closeDB()
            return jsonify(Error="Message NOT FOUND"), 404
        results = []
        for row in message_list:
            result = mapMessageInfoToDict(row)
            results.append(result)
        dao.closeDB()
        return jsonify(Message=results)

    def getAllOwners(self):
        dao = GroupDAO();
        ownerList = dao.getAllOwners()
        if not ownerList:
            dao.closeDB()
            return jsonify(Error="Owner NOT FOUND"), 404
        result = []
        for r in ownerList:
            mappedResult = {}
            mappedResult['pID'] = r[0]
            mappedResult['username'] = r[1]
            mappedResult['pFirstName'] = r[2]
            mappedResult['pLastName'] = r[3]
            mappedResult['pPhone'] = r[4]
            mappedResult['pEmail'] = r[5]
            result.append(mappedResult)
        dao.closeDB()
        return jsonify(Owner=result)

    def addMember(self, gID, pID):
        dao = GroupDAO()
        pid, gid = dao.addMember(pID, gID)
        result = {}
        result['pid'] = pid
        result['gid'] = gid
        dao.closeDB()
        return jsonify(Addition=result), 201



