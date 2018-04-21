from flask import jsonify, request
from dao.hashtag import HashTagDAO
from dao.message import MessageDAO

class HashTagHandler:

    def mapToDict(self, row):
        result = {}
        result['hID'] = row[0]
        result['hText'] = row[1]
        result['mID'] = row[2]
        return result

    def getAllHashTags(self):
        dao = HashTagDAO()
        result = dao.getAllHashTags()
        if not result:
            return jsonify(Error="HashTag NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(HashTags=mapped_result)

    def getHashTagByID(self,hID):
        dao = HashTagDAO()
        result = dao.getHashTagByID(hID)
        if not result:
            return jsonify(Error="HashTag NOT FOUND"), 404
        mapped_result = []
        mapped_result.append(self.mapToDict(result))
        return jsonify(HashTag=mapped_result)

    def getHashTagsByMessageID(self,mID):
        dao = MessageDAO()
        result = dao.getMessageById(mID)
        if not result:
            return jsonify(Error="Message NOT FOUND"), 404

        dao = HashTagDAO()
        result = dao.getHashTagList(mID)
        mapped_result = []
        for r in result:
            mapped_result.append(self.mapToDict(r))
        return jsonify(HashTags=mapped_result)