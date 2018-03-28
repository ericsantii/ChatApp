from flask import jsonify

from dao.groups import GroupDAO


class GroupHandler:

    def mapToDict(self, row):
        result = {}
        result['gID'] = row[0]
        result['gName'] = row[1]
        result['gOwner'] = row[2]
        return result

    def mapToMessageDict(self, row):
        result = {}
        result['mID'] = row[0]
        result['mText'] = row[1]
        result['timedate'] = row[2]
        result['multimedia'] = row[3]
        result['posterID'] = row[4]
        result['groupID'] = row[5]
        return result

    def mapToPersonDict(self, row):
        result = {}
        result['pID'] = row[0]
        result['pFirstName'] = row[1]
        result['pLastName'] = row[2]
        result['pPhone'] = row[3]
        result['pEmail'] = row[4]
        return result

    def build_group_attributes(self, gID, gName, gOwner):
        result = {}
        result['gID'] = gID
        result['gName'] = gName
        result['gOwner'] = gOwner
        return result

    def build_owner_dict(self, row):
        result = {}
        result['oID'] = row[0]
        result['oFirstName'] = row[1]
        result['oLastName'] = row[2]
        result['oPhone'] = row[3]
        result['oEmail'] = row[4]
        return result

    def getAllGroups(self):
        dao = GroupDAO()
        group_list = dao.getAllGroups()
        if not group_list:
            return jsonify(Error="Group NOT FOUND"), 404
        result_list = []
        for row in group_list:
            result = self.mapToDict(row)
            result_list.append(result)
        return jsonify(Group=result_list)

    def getGroupById(self, gid):
        dao = GroupDAO()
        result = dao.getGroupById(gid)
        if result is None:
            return jsonify(Error="Group NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Group=mapped)

    def getOwnerByGroupId(self, gID):
        dao = GroupDAO()
        result = dao.getOwnerByGroupId(gID)
        if result is None:
            return jsonify(Error="Group NOT FOUND"), 404
        result = self.mapToPersonDict(result)
        return jsonify(Person=result)

    def getPeopleByGroupID(self, gID):
        dao = GroupDAO()
        if not dao.getGroupById(gID):
            return jsonify(Error="Group NOT FOUND"), 404
        person_list = dao.getPeopleByGroupID(gID)
        results = []
        for row in person_list:
            result = self.mapToPersonDict(row)
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
            result = self.mapToMessageDict(row)
            results.append(result)
        return jsonify(Message=results)

    def getAllOwners(self):
        dao = GroupDAO();
        ownerList = dao.getAllOwners()
        if not ownerList:
            return jsonify(Error="Owner NOT FOUND"), 404
        result = []
        for r in ownerList:
            result.append(self.mapToPersonDict(r))
        return jsonify(Owner=result)


