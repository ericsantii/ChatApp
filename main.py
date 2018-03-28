from flask import Flask, request, jsonify, render_template, redirect, url_for
from handler.person import PersonHandler
from handler.groups import GroupHandler
from handler.message import MessageHandler

app = Flask(__name__)


# Home Route which the applications starts in
@app.route('/')
def home():
    return "Welcome to Chat App"


@app.route('/ChatApp/person', methods=['GET'])
def getPerson():
    return PersonHandler().getAllPersons()


# Displays all persons/users of the database app
# Or choose a specific person to display through pID
@app.route('/ChatApp/person/<int:pID>', methods=['GET'])
def getPersonByID(pID):
    return PersonHandler().getPersonById(pID)


# Displays all owners of the chat groups
@app.route('/ChatApp/group/<int:gID>/owner', methods=['GET'])
def getOwnerByGroupID(gID):
    return GroupHandler().getOwnerByGroupId(gID)


# Displays all chat groups of the database  app
# Or choose a specific group to display through gID
@app.route('/ChatApp/group', methods=['GET'])
def getGroup():
    return GroupHandler().getAllGroups()


@app.route('/ChatApp/group/<int:gID>')
def getGroupByID(gID):
    return GroupHandler().getGroupById(gID)


# Displays all messages of the database  app
# Or choose a specific message to display through mID
@app.route('/ChatApp/group/<int:gID>/messages', methods=['GET'])
def displayMessagesByGroupID(gID):
    return GroupHandler().getMessagesByGroupID(gID)


# Displays all messages of the database  app
# Or choose a specific message to display through mID
@app.route('/ChatApp/messages', methods=['GET'])
def getMessages():
    return MessageHandler().getAllMessages()


@app.route('/ChatApp/message/<int:mID>', methods=['GET'])
def getMessageByID(mID):
    return MessageHandler().getMessageById(mID)

@app.route('/ChatApp/person/<int:pID>/messages', methods=['GET'])
def getMessageByPersonID(pID):
    return PersonHandler().getMessagesByPersonID(pID)


@app.route('/ChatApp/group/<int:gID>/person', methods=['GET'])
def getMembersByGroupID(gID):
    return GroupHandler().getPeopleByGroupID(gID)


@app.route('/ChatApp/person/<int:pID>/groups', methods=['GET'])
def getGroupsByPersonID(pID):
    return PersonHandler().getGroupsByPersonID(pID)


@app.route('/ChatApp/person/<int:pID>/reacts', methods=['GET'])
def getReactsByPersonID(pID):
    return PersonHandler().getReactsByPersonID(pID)


@app.route('/ChatApp/message/<int:mID>/reacts', methods=['GET'])
def getReactsByMessageID(mID):
    return MessageHandler().getReactsByMessageID(mID)


@app.route('/ChatApp/message/<int:mID>/replies', methods=['GET'])
def getRepliesByMessageID(mID):
    return MessageHandler().getRepliesByMessageID(mID)


@app.route('/ChatApp/message/<int:mID>/originalMessage', methods=['GET'])
def getOriginalMessageByReplyID(mID):
    return MessageHandler().getOriginalMessageByReplyID(mID)


@app.route('/ChatApp/person/<int:pID>/contacts', methods=['GET'])
def getContactsByPersonID(pID):
    return PersonHandler().getContactsByPersonID(pID)


@app.route('/ChatApp/owner', methods=['GET'])
def getAllOwners():
    return GroupHandler().getAllOwners()


if __name__ == '__main__':
    app.run()
