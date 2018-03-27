from flask import jsonify, request
from dao.message import MessageDAO


class MessageHandler:
    def mapToDict(self, row):
        result = {}
        result['mID'] = row[0]
        result['mText'] = row[1]
        result['timedate'] = row[2]
        result['multimedia'] = row[3]
        result['posterID'] = row[4]
        result['groupID'] = row[5]
        return result

    def build_message_attributes(self, mID, mText, timedate, multimedia, posterID, groupID):
        result = {}
        result['mID'] = mID
        result['mText'] = mText
        result['timedate'] = timedate
        result['multimedia'] = multimedia
        result['posterID'] = posterID
        result['groupID'] = groupID
        return result

    def mapToReactDict(self, row):
        result = {}
        result['mID'] = row[0]
        result['pID'] = row[1]
        result['rType'] = row[2]
        return result

    def getAllMessages(self):
        dao = MessageDAO()
        result = dao.getAllMessages()
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(Messages=mapped_result)

    def getMessageById(self, args):
        dao = MessageDAO()
        result = dao.getMessageById(int(args.get('mID')))
        if result == None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped = self.mapToDict(result)
            return jsonify(Messages=mapped)

    def getMessageByGroup(self, gID):
        dao = MessageDAO()
        result = dao.getMessageByGroup(gID)
        if result is None:
            return jsonify(Error="NOT FOUND"), 404
        else:
            mapped_results = []
            for row in result:
                mapped_results.append(self.mapToDict(row))
            return jsonify(Messages=mapped_results)

    def CreateNewMessage(self, form):
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            mText = form['mText']
            timedate = form['timedate']
            multimedia = form['multimedia']
            posterID = form['posterID']
            groupID = form['groupID']
            if MessageDAO().verify(posterID, groupID):
                if (mText or multimedia) and timedate and posterID and groupID:
                    dao = MessageDAO()
                    mID = dao.insert(mText, timedate, multimedia, posterID, groupID)
                    result = self.build_message_attributes(mID, mText, timedate, multimedia, posterID, groupID)
                    return jsonify(Message=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400
            else:
                return jsonify(Error="Invalid Message Creation: Person or Group does not exist in the database"), 400

    def getReactsByMessageID(self, mID):
        dao = MessageDAO()
        if not dao.getMessageById(mID):
            return jsonify(Error="Message Not Found"), 404
        reacts_list = dao.getReactsByMessageID(mID)
        results = []
        for row in reacts_list:
            result = self.mapToReactDict(row)
            results.append(result)
        return jsonify(ReactsForMessage=results)

    def getRepliesByMessageID(self, mID):
        dao = MessageDAO()
        if not dao.getMessageById(mID):
            return jsonify(Error="Message Not Found"), 404
        reply_list = dao.getRepliesByMessageID(mID)
        results = []
        for row in reply_list:
            result = self.mapToDict(row)
            results.append(result)
        return jsonify(RepliesForMessage=results)

    def getOriginalMessageByReplyID(self, rID):
        dao = MessageDAO()
        if not dao.getMessageById(rID):
            return jsonify(Error="Reply Not Found"), 404
        result = dao.getOriginalMessageByReplyID(rID)
        result = self.mapToDict(result)

        return jsonify(OriginalMessageForReply=result)
