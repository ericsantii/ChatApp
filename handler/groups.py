from flask import jsonify

from dao.groups import GroupDAO

from mapToDictFunctions import mapGroupToDict, mapMessageToDict, mapPersonToDict


class GroupHandler:


    def getAllGroups(self):
        dao = GroupDAO()
        group_list = dao.getAllGroups()
        if not group_list:
            return jsonify(Error="Group NOT FOUND"), 404
        result_list = []
        for row in group_list:
            result = mapGroupToDict(row)
            result_list.append(result)
        return jsonify(Group=result_list)

    def getGroupById(self, gid):
        dao = GroupDAO()
        result = dao.getGroupById(gid)
        if result is None:
            return jsonify(Error="Group NOT FOUND"), 404
        else:
            mapped = mapGroupToDict(result)
            return jsonify(Group=mapped)

    def getOwnerByGroupId(self, gID):
        dao = GroupDAO()
        result = dao.getOwnerByGroupId(gID)
        if result is None:
            return jsonify(Error="Group NOT FOUND"), 404
        result = mapPersonToDict(result)
        return jsonify(Person=result)

    def getPeopleByGroupID(self, gID):
        dao = GroupDAO()
        if not dao.getGroupById(gID):
            return jsonify(Error="Group NOT FOUND"), 404
        person_list = dao.getPeopleByGroupID(gID)
        results = []
        for row in person_list:
            result = mapPersonToDict(row)
            results.append(result)
        return jsonify(Person=results)

    def getMessagesByGroupID(self, gID):
        dao = GroupDAO()
        if not dao.getGroupById(gID):
            return jsonify(Error="Group NOT FOUND"), 404
        message_list = dao.getMessagesByGroupID(gID)
        if not message_list:
            return jsonify(Error="Message NOT FOUND"), 404
        results = []
        for row in message_list:
            result = mapMessageToDict(row)
            results.append(result)
        return jsonify(Message=results)

    def getAllOwners(self):
        dao = GroupDAO();
        ownerList = dao.getAllOwners()
        if not ownerList:
            return jsonify(Error="Owner NOT FOUND"), 404
        result = []
        for r in ownerList:
            result.append(mapPersonToDict(r))
        return jsonify(Owner=result)


