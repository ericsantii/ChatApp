from flask import jsonify, request
from dao.message import MessageDAO
from dao.groups import GroupDAO


class MessageHandler:
    def mapToDict(self, row):
        result = {}
        result['mID'] = row[0]
        result['mText'] = row[1]
        result['timedate'] = row[2]
        result['multimedia'] = row[3]
        result['pID'] = row[4]
        result['gID'] = row[5]
        return result

    def mapToReactDict(self, row):
        result = {}
        result['mID'] = row[0]
        result['pID'] = row[1]
        result['rType'] = row[2]
        return result

    def mapToCount(self, row):
        result = {}
        result['mID'] = row[0]
        result['total'] = row[1]
        return result

    def getAllMessages(self):
        dao = MessageDAO()
        result = dao.getAllMessages()
        if not result:
            return jsonify(Error="Message NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Messages=mapped_result)

    def getMessageById(self, mID):
        dao = MessageDAO()
        result = dao.getMessageById(int(mID))
        if not result:
            return jsonify(Error="Message NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Messages=mapped)

    def getReactsByMessageID(self, mID):
        dao = MessageDAO()
        if not dao.getMessageById(mID):
            return jsonify(Error="Message NOT FOUND"), 404
        reacts_list = dao.getReactsByMessageID(mID)
        if not reacts_list:
            return jsonify(Error="React NOT FOUND"), 404
        results = []
        for row in reacts_list:
            result = self.mapToReactDict(row)
            results.append(result)
        return jsonify(Reacts=results)

    def getRepliesByMessageID(self, mID):
        dao = MessageDAO()
        if not dao.getMessageById(mID):
            return jsonify(Error="Message NOT FOUND"), 404
        reply_list = dao.getRepliesByMessageID(mID)
        if not reply_list:
            return jsonify(Error="Reply NOT FOUND"), 404
        results = []
        for row in reply_list:
            result = self.mapToDict(row)
            results.append(result)
        return jsonify(Messages=results)

    def getOriginalMessageByReplyID(self, rID):
        dao = MessageDAO()
        if not dao.getMessageById(rID):
            return jsonify(Error="Reply NOT FOUND"), 404
        result = dao.getOriginalMessageByReplyID(rID)
        if not result:
            return jsonify(Error="Original Message NOT FOUND"), 404
        else:
            result = self.mapToDict(result)
            return jsonify(Messages=result)

    def getMessagesPostedByPersoninGroupID(self, mID, gID):
        dao = MessageDAO()
        dao1 = GroupDAO()
        results = []
        if not dao.getMessageById():
            return jsonify(Error="Message NOT FOUND"), 404
        if not dao1.getGroupById(gID):
            return jsonify(Error="Group NOT FOUND"), 404
        message_list = dao.getMessagesPostedByPersoninGroupID(mID, gID)
        for row in message_list:
            result = self.mapToDict(row)
            results.append(result)
        return jsonify(Messages=results)

    def getNumofLikesbyMessageID(self, mID):
        dao = MessageDAO()
        results = []
        if not dao.getMessageById():
            return jsonify(Error="Message NOT FOUND"), 404
        list = dao.getNumofLikesbyMessageID(mID)
        for row in list:
            result = self.mapToCount(row)
            results.append(result)
        return jsonify(Messages=results)

    def getPersonWhoLikedMessageID(self, mID):
        dao = MessageDAO()
        if not dao.getMessageById(mID):
            return jsonify(Error="Message NOT FOUND"), 404
        reacts_list = dao.getPersonWhoLikedMessageID(mID)
        if not reacts_list:
            return jsonify(Error="React NOT FOUND"), 404
        results = []
        for row in reacts_list:
            result = self.mapToReactDict(row)
            results.append(result)
        return jsonify(Reacts=results)

    def getPersonWhoDisikedMessageID(self, mID):
        dao = MessageDAO()
        if not dao.getMessageById(mID):
            return jsonify(Error="Message NOT FOUND"), 404
        reacts_list = dao.getPersonWhoDislikedMessageID(mID)
        if not reacts_list:
            return jsonify(Error="React NOT FOUND"), 404
        results = []
        for row in reacts_list:
            result = self.mapToReactDict(row)
            results.append(result)
        return jsonify(Reacts=results)

    def getNumOfDislikesMessageID(self, mID):
        dao = MessageDAO()
        results = []
        if not dao.getMessageById():
            return jsonify(Error="Message NOT FOUND"), 404
        list = dao.getNumofDislikesbyMessageID(mID)
        for row in list:
            result = self.mapToCount(row)
            results.append(result)
        return jsonify(Messages=results)
