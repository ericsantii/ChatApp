from flask import jsonify, request
from dao.hashtag import HashTagDAO
from dao.message import MessageDAO
from mapToDictFunctions import mapHashTagToDict, mapMessageToDict

class HashTagHandler:


    def getAllHashTags(self):
        dao = HashTagDAO()
        result = dao.getAllHashTags()
        if not result:
            dao.closeDB()
            return jsonify(Error="HashTag NOT FOUND"), 404
        mapped_result = []
        for r in result:
            print(r)
            mapped_result.append(mapHashTagToDict(r))
        dao.closeDB()
        return jsonify(HashTags=mapped_result)

    def getHashTagByID(self,hID):
        dao = HashTagDAO()
        result = dao.getHashTagByID(hID)
        if not result:
            dao.closeDB()
            return jsonify(Error="HashTag NOT FOUND"), 404
        mapped_result = []
        mapped_result.append(mapHashTagToDict(result))
        dao.closeDB()
        return jsonify(HashTag=mapped_result)

    def getHashTagsByMessageID(self,mID):
        dao = MessageDAO()
        result = dao.getMessageById(mID)
        if not result:
            dao.closeDB()
            return jsonify(Error="Message NOT FOUND"), 404
        dao.closeDB()
        dao = HashTagDAO()
        result = dao.getHashTagList(mID)
        mapped_result = []
        for r in result:
            mapped_result.append(mapHashTagToDict(r))
        dao.closeDB()
        return jsonify(HashTags=mapped_result)

    def getMessageByHashtag(self,args):
        dao = HashTagDAO()
        text = args.get('hText')
        if not text:
            dao.closeDB()
            return jsonify(Error="Bad Request Arguments"), 400
        else:
            results = dao.getMessageByHashTag(text)
            mapped_results = []
            for result in results:
                mapped_results.append(mapMessageToDict(result))
            dao.closeDB()
            return jsonify(Messages= mapped_results)

    def getTopHashTags(self):
        dao = HashTagDAO()

        results = dao.getTopHashtags()
        mapped_results = []
        for result in results:
            dict = {}
            dict['htext'] = result[0]
            dict['count'] = result[1]
            mapped_results.append(dict)
        dao.closeDB()
        return jsonify(TopHashtags=mapped_results)
