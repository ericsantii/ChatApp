from flask import jsonify, request
from dao.message import MessageDAO
from dao.groups import GroupDAO
from dao.hashtag import HashTagDAO
from mapToDictFunctions import mapToReactDict, mapToCount, mapMessageToDict, mapPersonToDict, mapMessageInfoToDict


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

    def addMessage(self, json):
        dao = MessageDAO()
        if len(json) != 3:
            dao.closeDB()
            return jsonify(Error="Malformed post request"), 400
        else:
            mtext = json['mtext']
            pid = json['pid']
            gid = json['gid']

            if mtext and pid and gid:
                (mid, timedate) = dao.addMessage(mtext, pid, gid)
                self.parseHashTag(mid, mtext)
                result = mapMessageToDict([mid, mtext, timedate, pid, gid])
                dao.closeDB()
                return jsonify(Message=result), 201
            else:
                dao.closeDB()
                return jsonify(Error="Unexpected attributes in post request"), 400

    def addMessageAsReply(self, originalMessage, json):
        dao = MessageDAO()
        if len(json) != 4:
            dao.closeDB()
            return jsonify(Error="Malformed post request"), 400
        else:
            mtext = json['mtext']
            rtext = json['rtext']
            pid = json['pid']
            gid = json['gid']
            if mtext and pid and gid and rtext:
                (mid, timedate) = dao.addMessage(mtext, pid, gid)
                self.parseHashTag(mid, rtext)
                oid, rid = dao.addMessageAsReply(originalMessage, mid)
                result = mapMessageToDict([mid, mtext, timedate, pid, gid])
                result['originalMessageID'] = oid
                dao.closeDB()
                return jsonify(Message=result), 201
            else:
                dao.closeDB()
                return jsonify(Error="Unexpected attributes in post request"), 400

    def likeMessage(self, pID, mID):
        dao = MessageDAO()
        pid, mid, rType = dao.likeMessage(pID, mID)
        result = {}
        result['pid'] = pid
        result['mid'] = mid
        result['rType'] = rType
        dao.closeDB()
        return jsonify(Liked=result), 201

    def dislikeMessage(self, pID, mID):
        dao = MessageDAO()
        pid, mid, rType = dao.dislikeMessage(pID, mID)
        result = {}
        result['pid'] = pid
        result['mid'] = mid
        result['rType'] = rType
        dao.closeDB()
        return jsonify(Disliked=result), 201

    def getMessagesWithHashtagInGroupID(self, ht, gID):
        dao = MessageDAO()
        dao1 = GroupDAO()
        dao2 = HashTagDAO()
        results = []
        if not dao1.getGroupById(gID):
            dao.closeDB()
            dao1.closeDB()
            dao2.closeDB()
            return jsonify(Error="Group NOT FOUND"), 404
        if not dao2.getMessageByHashTag(ht):
            dao.closeDB()
            dao1.closeDB()
            dao2.closeDB()
            return jsonify(Error="HashTag NOT FOUND"), 404
        message_list = dao.getMessagesWithHashtagInGroupID(ht, gID)
        for row in message_list:
            result = mapMessageInfoToDict(row)
            results.append(result)
        dao.closeDB()
        dao1.closeDB()
        dao2.closeDB()
        return jsonify(Messages=results)

    def getNumOfMessagesPerDay(self):
        dao = MessageDAO()

        results = dao.getNumOfMessagesPerDay()
        mapped_results = []
        for result in results:
            dict = {}
            dict['day'] = result[0]
            dict['count'] = result[1]
            mapped_results.append(dict)
        dao.closeDB()
        return jsonify(MessagesPerDay=mapped_results)


    def getNumOfRepliesPerDay(self):
        dao = MessageDAO()

        results = dao.getNumOfRepliesPerDay()
        mapped_results = []
        for result in results:
            dict = {}
            dict['day'] = result[0]
            dict['count'] = result[1]
            mapped_results.append(dict)
        dao.closeDB()
        return jsonify(RepliesPerDay=mapped_results)

    def getNumOfLikesPerDay(self):
        dao = MessageDAO()
        results = dao.getNumOfLikesPerDay()
        mapped_results = []
        for result in results:
            dict = {}
            dict['day'] = result[0]
            dict['count'] = result[1]
            mapped_results.append(dict)
        dao.closeDB()
        return jsonify(LikesPerDay=mapped_results)

    def getNumOfDislikesPerDay(self):
        dao = MessageDAO()
        results = dao.getNumOfDislikesPerDay()
        mapped_results = []
        for result in results:
            dict = {}
            dict['day'] = result[0]
            dict['count'] = result[1]
            mapped_results.append(dict)
        dao.closeDB()
        return jsonify(DislikesPerDay=mapped_results)

    def getNumOfActiveUsersPerDay(self):
        dao = MessageDAO()
        results = dao.getNumOfActiveUsersPerDay()
        mapped_results = []
        for result in results:
            dict = {}
            dict['day'] = result[0]
            dict['count'] = result[1]
            mapped_results.append(dict)
        dao.closeDB()
        return jsonify(NumOfActiveUsersPerDay=mapped_results)

    def parseHashTag(self, mid, mtext):
        hashtags = []
        while '#' in mtext:
            afterhtIndex = mtext.index("#") + 1
            if ' ' in mtext[afterhtIndex:]:
                spaceIndex = mtext[mtext.index("#") + 1:].index(' ') + afterhtIndex
                hashtags.append(mtext[afterhtIndex:spaceIndex])
                mtext = mtext[spaceIndex + 1:]
            else:
                hashtags.append(mtext[afterhtIndex:])
                mtext = ''

        dao = HashTagDAO()

        for ht in hashtags:
            hid = dao.gethashtagIdByText(ht)
            if not hid:
                hid = dao.addHashTag(ht)
            dao.addMessageContains(mid, hid)

        dao.closeDB()

