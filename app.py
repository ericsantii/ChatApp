from flask import Flask, request, jsonify, render_template, redirect, url_for
from handler.person import PersonHandler
from handler.groups import GroupHandler
from handler.message import MessageHandler

app = Flask(__name__)


# Home Route which the applications starts in
@app.route('/')
def home():





    return "Welcome to Chat App"



#Person routes
@app.route('/ChatApp/person', methods=['GET'])
def getPerson():
    return PersonHandler().getAllPersons()

@app.route('/ChatApp/person/<int:pID>', methods=['GET'])
def getPersonByID(pID):
    return PersonHandler().getPersonById(pID)

#Group routes
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

@app.route('/ChatApp/group', methods=['GET'])
def getGroup():
    return GroupHandler().getAllGroups()


@app.route('/ChatApp/group/<int:gID>')
def getGroupByID(gID):
    return GroupHandler().getGroupById(gID)



#Messaging routes
@app.route('/ChatApp/group/<int:gID>/message', methods=['GET'])
def displayMessagesByGroupID(gID):
    return GroupHandler().getMessagesByGroupID(gID)


@app.route('/ChatApp/message', methods=['GET'])
def getMessages():
    return MessageHandler().getAllMessages()


@app.route('/ChatApp/message/<int:mID>', methods=['GET'])
def getMessageByID(mID):
    return MessageHandler().getMessageById(mID)

@app.route('/ChatApp/person/<int:pID>/message', methods=['GET'])
def getMessageByPersonID(pID):
    return PersonHandler().getMessagesByPersonID(pID)




#React routes

@app.route('/ChatApp/person/<int:pID>/reacts', methods=['GET'])
def getReactsByPersonID(pID):
    return PersonHandler().getReactsByPersonID(pID)


@app.route('/ChatApp/message/<int:mID>/reacts', methods=['GET'])
def getReactsByMessageID(mID):
    return MessageHandler().getReactsByMessageID(mID)



#Reply routes

@app.route('/ChatApp/message/<int:mID>/replies', methods=['GET'])
def getRepliesByMessageID(mID):
    return MessageHandler().getRepliesByMessageID(mID)


@app.route('/ChatApp/message/<int:mID>/originalMessage', methods=['GET'])
def getOriginalMessageByReplyID(mID):
    return MessageHandler().getOriginalMessageByReplyID(mID)



#Contact routes

@app.route('/ChatApp/person/<int:pID>/contacts', methods=['GET'])
def getContactsByPersonID(pID):
    return PersonHandler().getContactsByPersonID(pID)





if __name__ == '__main__':
    app.run()
