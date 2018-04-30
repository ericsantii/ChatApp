from flask import jsonify, request
from dao.message import MessageDAO
from dao.groups import GroupDAO
from mapToDictFunctions import mapToReactDict, mapToCount, mapMessageToDict, mapPersonToDict


class MessageHandler:

    def getAllMessages(self):
        dao = MessageDAO()
        result = dao.getAllMessages()
        if not result:
            dao.closeDB()
            return jsonify(Error="Message NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapMessageToDict(r))
        dao.closeDB()
        return jsonify(Messages=mapped_result)

    def getMessageById(self, mID):
        dao = MessageDAO()
        result = dao.getMessageById(int(mID))
        if not result:
            dao.closeDB()
            return jsonify(Error="Message NOT FOUND"), 404
        else:
            mapped = mapMessageToDict(result)
            dao.closeDB()
            return jsonify(Messages=mapped)

    def getReactsByMessageID(self, mID):
        dao = MessageDAO()
        if not dao.getMessageById(mID):
            dao.closeDB()
            return jsonify(Error="Message NOT FOUND"), 404
        reacts_list = dao.getReactsByMessageID(mID)
        if not reacts_list:
            dao.closeDB()
            return jsonify(Error="React NOT FOUND"), 404
        results = []
        for row in reacts_list:
            result = mapToReactDict(row)
            results.append(result)
        dao.closeDB()
        return jsonify(Reacts=results)

    def getRepliesByMessageID(self, mID):
        dao = MessageDAO()
        if not dao.getMessageById(mID):
            dao.closeDB()
            return jsonify(Error="Message NOT FOUND"), 404
        reply_list = dao.getRepliesByMessageID(mID)
        if not reply_list:
            dao.closeDB()
            return jsonify(Error="Reply NOT FOUND"), 404
        results = []
        for row in reply_list:
            result = mapMessageToDict(row)
            results.append(result)
        dao.closeDB()
        return jsonify(Messages=results)

    def getOriginalMessageByReplyID(self, rID):
        dao = MessageDAO()
        if not dao.getMessageById(rID):
            dao.closeDB()
            return jsonify(Error="Reply NOT FOUND"), 404
        result = dao.getOriginalMessageByReplyID(rID)
        if not result:
            dao.closeDB()
            return jsonify(Error="Original Message NOT FOUND"), 404
        else:
            result = mapMessageToDict(result)
            dao.closeDB()
            return jsonify(Messages=result)

    def getMessagesPostedByPersoninGroupID(self, mID, gID):
        dao = MessageDAO()
        dao1 = GroupDAO()
        results = []
        if not dao.getMessageById(mID):
            dao.closeDB()
            dao1.closeDB()
            return jsonify(Error="Message NOT FOUND"), 404
        if not dao1.getGroupById(gID):
            dao.closeDB()
            dao1.closeDB()
            return jsonify(Error="Group NOT FOUND"), 404
        message_list = dao.getMessagesPostedByPersoninGroupID(mID, gID)
        for row in message_list:
            result = mapMessageToDict(row)
            results.append(result)
        dao.closeDB()
        dao1.closeDB()
        return jsonify(Messages=results)

    def getNumofLikesbyMessageID(self, mID):
        dao = MessageDAO()
        results = []
        if not dao.getMessageById(mID):
            dao.closeDB()
            return jsonify(Error="Message NOT FOUND"), 404
        result = dao.getNumofLikesbyMessageID(mID)
        mapped = {}
        mapped['mID'] = mID
        mapped['total'] = result[0]
        dao.closeDB()
        return jsonify(NumOfLikes=mapped)

    def getPersonWhoLikedMessageID(self, mID):
        dao = MessageDAO()
        if not dao.getMessageById(mID):
            dao.closeDB()
            return jsonify(Error="Message NOT FOUND"), 404
        persons_list = dao.getPersonWhoLikedMessageID(mID)
        if not persons_list:
            dao.closeDB()
            return jsonify(Error="Person NOT FOUND"), 404
        results = []
        for row in persons_list:
            result = {}
            result['pID'] = row[0]
            result['pFirstName'] = row[1]
            result['pLastName'] = row[2]
            result['username'] = row[3]
            result['pEmail'] = row[4]
            results.append(result)
        dao.closeDB()
        return jsonify(Persons=results)

    def getPersonWhoDisikedMessageID(self, mID):
        dao = MessageDAO()
        if not dao.getMessageById(mID):
            dao.closeDB()
            return jsonify(Error="Message NOT FOUND"), 404
        persons_list = dao.getPersonWhoDislikedMessageID(mID)
        if not persons_list:
            dao.closeDB()
            return jsonify(Error="Person NOT FOUND"), 404
        results = []
        for row in persons_list:
            result = {}
            result['pID'] = row[0]
            result['pFirstName'] = row[1]
            result['pLastName'] = row[2]
            result['username'] = row[3]
            result['pEmail'] = row[4]
            results.append(result)
        dao.closeDB()
        return jsonify(Persons=results)

    def getNumOfDislikesMessageID(self, mID):
        dao = MessageDAO()
        results = []
        if not dao.getMessageById(mID):
            dao.closeDB()
            return jsonify(Error="Message NOT FOUND"), 404
        result = dao.getNumofDislikesbyMessageID(mID)
        mapped = {}
        mapped['mID'] = mID
        mapped['total'] = result[0]
        dao.closeDB()
        return jsonify(NumOfDislikes=mapped)
