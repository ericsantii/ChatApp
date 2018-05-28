from flask import Flask, request, jsonify, render_template, redirect, url_for

from handler.hashtag import HashTagHandler
from handler.person import PersonHandler
from handler.groups import GroupHandler
from handler.message import MessageHandler
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


# Home Route which the applications starts in
@app.route('/')
def home():
    return "Welcome to Chat App"


# Person routes
@app.route('/ChatApp/login', methods= ['POST'])
def loginPerson():
    return PersonHandler().loginUser(request.json)

@app.route('/ChatApp/person', methods=['GET', 'POST'])
def getPerson():
    if request.method == 'GET':
        if len(request.args) >= 1:
            return PersonHandler().getPersonByUsername(request.args)
        else:
            return PersonHandler().getAllPersons()
    if request.method == 'POST':
        return PersonHandler().addPerson(request.json)


@app.route('/ChatApp/person/<int:pID>', methods=['GET'])
def getPersonByID(pID):
    return PersonHandler().getPersonById(pID)


# Group routes
@app.route('/ChatApp/group/<int:gID>/owner', methods=['GET'])
def getOwnerByGroupID(gID):
    return GroupHandler().getOwnerByGroupId(gID)


@app.route('/ChatApp/owner', methods=['GET'])
def getAllOwners():
    return GroupHandler().getAllOwners()


@app.route('/ChatApp/person/<int:pID>/group', methods=['GET'])
def getGroupsByPersonID(pID):
    return PersonHandler().getGroupsByPersonID(pID)


@app.route('/ChatApp/group/<int:gID>/person', methods=['GET'])
def getMembersByGroupID(gID):
    return GroupHandler().getPeopleByGroupID(gID)

@app.route('/ChatApp/group/<int:gID>/person/<int:pID>', methods=['POST'])
def addMemberToGroup(gID, pID):
    return GroupHandler().addMember(gID, pID)


@app.route('/ChatApp/group', methods=['GET'])
def getGroup():
    return GroupHandler().getAllGroups()


@app.route('/ChatApp/group/<int:gID>')
def getGroupByID(gID):
    return GroupHandler().getGroupById(gID)


# Messaging routes
@app.route('/ChatApp/group/<int:gID>/message', methods=['GET'])
def displayMessagesByGroupID(gID):
    return GroupHandler().getMessagesByGroupID(gID)


@app.route('/ChatApp/message', methods=['GET', 'POST'])
def getMessages():
    if request.method == 'GET':
        return MessageHandler().getAllMessages()
    elif request.method == 'POST':
        print(request)
        return MessageHandler().addMessage(request.json)

@app.route('/ChatApp/reply/<int:mID>', methods=['POST'])
def addMessageAsReply(mID):
    return MessageHandler().addMessageAsReply(mID, request.json)

@app.route('/ChatApp/message/<int:mID>', methods=['GET'])
def getMessageByID(mID):
    return MessageHandler().getMessageById(mID)


@app.route('/ChatApp/person/<int:pID>/message', methods=['GET'])
def getMessageByPersonID(pID):
    return PersonHandler().getMessagesByPersonID(pID)


@app.route('/ChatApp/message/group/<int:gID>/person/<int:pID>', methods=['GET'])
def getMessagesPostedByPersoninGroupID(gID, pID):
    return MessageHandler().getMessagesPostedByPersoninGroupID(pID, gID)


@app.route('/ChatApp/message/<int:mID>/likes/num', methods=['GET'])
def getNumofLikesbyMessageID(mID):
    return MessageHandler().getNumofLikesbyMessageID(mID)


@app.route('/ChatApp/message/<int:mID>/dislikes/num')
def getNumofDislikesbyMessageID(mID):
    return MessageHandler().getNumOfDislikesMessageID(mID)


@app.route('/ChatApp/message/<int:mID>/likes/person', methods=['GET'])
def getPersonWhoLikedMessageID(mID):

    return MessageHandler().getPersonWhoLikedMessageID(mID)


@app.route('/ChatApp/message/<int:mID>/dislikes/person', methods=['GET'])
def getPersonWhoDisikedMessageID(mID):
    return MessageHandler().getPersonWhoDisikedMessageID(mID)


# React routes
@app.route('/ChatApp/like/message/<int:mID>/person/<int:pID>', methods=['POST'])
def likeMessage(mID, pID):
    return MessageHandler().likeMessage(pID, mID)

@app.route('/ChatApp/dislike/message/<int:mID>/person/<int:pID>', methods=['POST'])
def dislikeMessage(mID, pID):
    return MessageHandler().dislikeMessage(pID, mID)

@app.route('/ChatApp/person/<int:pID>/reacts', methods=['GET'])
def getReactsByPersonID(pID):
    return PersonHandler().getReactsByPersonID(pID)


@app.route('/ChatApp/message/<int:mID>/reacts', methods=['GET'])
def getReactsByMessageID(mID):
    return MessageHandler().getReactsByMessageID(mID)


# Reply routes

@app.route('/ChatApp/message/<int:mID>/replies', methods=['GET'])
def getRepliesByMessageID(mID):
    return MessageHandler().getRepliesByMessageID(mID)


@app.route('/ChatApp/message/<int:mID>/originalMessage', methods=['GET'])
def getOriginalMessageByReplyID(mID):
    return MessageHandler().getOriginalMessageByReplyID(mID)






# Contact routes

@app.route('/ChatApp/person/<int:pID>/contacts', methods=['GET'])
def getContactsByPersonID(pID):
    return PersonHandler().getContactsByPersonID(pID)



#Hashtag Routes
@app.route('/ChatApp/hashtag',methods=['GET'])
def getHash():
    if len(request.args) > 0:
        return HashTagHandler().getMessageByHashtag(request.args)
    else:
        return HashTagHandler().getAllHashTags()

@app.route('/ChatApp/messages/hashtag/<string:ht>/group/<int:gID>',methods=['GET'])
def getMessagesWithHashtagInGroupID(ht, gID):
    return MessageHandler().getMessagesWithHashtagInGroupID(ht, gID)

@app.route('/ChatApp/hashtag/<int:hID>', methods=['GET'])
def getHashByID(hID):
    return HashTagHandler().getHashTagByID(hID)

@app.route('/ChatApp/message/<int:mID>/hashtag', methods=['GET'])
def getHashByMessageID(mID):
    return HashTagHandler().getHashTagsByMessageID(mID)

@app.route('/ChatApp/hashtags/top', methods=['GET'])
def getTopHashtags():
    return HashTagHandler().getTopHashTags()

@app.route('/ChatApp/messages/count', methods=['GET'])
def getMessagesPerDay():
    return MessageHandler().getNumOfMessagesPerDay()

@app.route('/ChatApp/replies/count', methods=['GET'])
def getRepliesPerDay():
    return MessageHandler().getNumOfRepliesPerDay()

@app.route('/ChatApp/likes/count', methods=['GET'])
def getLikesPerDay():
    return MessageHandler().getNumOfLikesPerDay()

@app.route('/ChatApp/dislikes/count', methods=['GET'])
def getDislikesPerDay():
    return MessageHandler().getNumOfDislikesPerDay()

@app.route('/ChatApp/users/top', methods=['GET'])
def getNumOfActiveUsersPerDay():
    return MessageHandler().getNumOfActiveUsersPerDay()

if __name__ == '__main__':
    app.run()
