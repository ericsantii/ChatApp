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
        result = mapPersonToDict(result)
        dao.closeDB()
        return jsonify(Person=result)

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
            result.append(mapPersonToDict(r))
        dao.closeDB()
        return jsonify(Owner=result)


