from flask import jsonify

from dao.groups import GroupDAO


class GroupHandler:

    def mapToDict(self, row):
        result = {}
        result['gID'] = row[0]
        result['gName'] = row[1]
        result['gOwner'] = row[2]
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
        result_list = []
        for row in group_list:
            result = self.mapToDict(row)
            result_list.append(result)
        return jsonify(Groups=result_list)

    def getGroupById(self, gid):
        dao = GroupDAO()
        result = dao.getGroupById(gid)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Groups=mapped)

    def getOwnerByGroupId(self, gid):
        dao = GroupDAO()
        owner_list = dao.getOwnerByGroupId()
        results = []
        for row in owner_list:
            results.append(self.build_owner_dict(row))
        return jsonify(Owners=results)

    def createNewChatGroup(self, form):
        if form and len(form) == 2:
            gName = form['gName']
            gOwner = form['gOwner']
            if gName:
                dao = GroupDAO()
                gID = dao.insert(gName, gOwner)
                result = self.build_group_attributes(gID, gName, gOwner)
                return jsonify(Group=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    def deleteChatGroupbyID(self, args):
        dao = GroupDAO()
        if not dao.getGroupById(int(args.get('gID'))):
            return jsonify(Error="Part not found."), 404
        else:
            param = int(args.get('gID'))
            if param:
                dao.delete(args.get('gID'))
                return jsonify(DeleteStatus="OK"), 200

    def getPeopleByGroupID(self, gID):
        dao = GroupDAO()
        if not dao.getGroupById(gID):
            return jsonify(Error="Group Not Found"), 404
        person_list = dao.getPeopleByGroupID(gID)
        results = []
        for row in person_list:
            result = self.mapToPersonDict(row)
            results.append(result)
        return jsonify(PeopleGroup=results)

    # def insertGroup(self,form):
    #     if form and len(form) == 2:
    #         gid = form['gid']
    #         gname = form['gname']
    #         if gid and gname:
    #             dao = GroupDAO()
    #             sid = dao.insert(sname, scity, sphone)
    #             result = {}
    #             result["sid"] = sid
    #             result["sname"] = sname
    #             result["scity"] = scity
    #             result["sphone"] = sphone
    #             return jsonify(Supplier=result), 201
    #         else:
    #             return jsonify(Error="Malformed post request")
    #     else:
    #         return jsonify(Error="Malformed post request")
    #
    #     return
    def deleteGroup(self):
        return
