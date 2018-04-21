from flask import jsonify, request
from dao.hashtag import HashTagDAO
from dao.message import MessageDAO
from mapToDictFunctions import mapHashTagToDict, mapMessageToDict

class HashTagHandler:


    def getAllHashTags(self):
        dao = HashTagDAO()
        result = dao.getAllHashTags()
        if not result:
            return jsonify(Error="HashTag NOT FOUND"), 404
        mapped_result = []
        for r in result:
            mapped_result.append(mapHashTagToDict(r))
        return jsonify(HashTags=mapped_result)

    def getHashTagByID(self,hID):
        dao = HashTagDAO()
        result = dao.getHashTagByID(hID)
        if not result:
            return jsonify(Error="HashTag NOT FOUND"), 404
        mapped_result = []
        mapped_result.append(mapHashTagToDict(result))
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
            mapped_result.append(mapHashTagToDict(r))
        return jsonify(HashTags=mapped_result)

    def getMessageByHashtag(self,request):
        dao = HashTagDAO
        text = request.args.get('text')
        if not text:
            return jsonify(Error="Bad Request Arguments"), 400
        else:
            results = dao.getMessageByHashTag(text)
            mapped_results = []
            for result in results:
                mapped_results.append(mapMessageToDict(result))
            return jsonify(Messages= mapped_results)

