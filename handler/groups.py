from flask import jsonify

from dao.groups import GroupDAO


class GroupHandler:

    def mapToDict(self, row):
        result = {}
        result['gid'] = row[0]
        result['gname'] = row[1]
        return result
    def mapToPersonDict(self, row):
        result = {}
        result['pID'] = row[0]
        result['uFirstName'] = row[1]
        result['uLastName'] = row[2]
        result['uPhone'] = row[3]
        result['uEmail'] = row[4]

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
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else :
            mapped = self.mapToDict(result)
            return jsonify(Groups=mapped)


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