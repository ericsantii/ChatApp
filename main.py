from flask import Flask, request, jsonify, render_template, redirect, url_for
from handler.person import PersonHandler
from handler.groups import GroupHandler
from handler.message import MessageHandler
from handler.contact import ContactHandler

app = Flask(__name__)


# Home Route which the applications starts in
@app.route('/')
def home():
    return "Welcome to PapayaChat App"


# Displays all persons/users of the database app
# Or choose a specific person to display through pID
@app.route('/ChatApp/persons', methods=['GET'])
def getPersonByID():
    if request.args:
        return PersonHandler().getPersonById(request.args)
    else:
        return PersonHandler().getAllPersons()


# Displays all owners of the chat groups
@app.route('/ChatApp/persons/owners', methods=['GET'])
def owners():
    return GroupHandler().getOwnerByGroupId()


# Displays all chat groups of the database  app
# Or choose a specific group to display through gID
@app.route('/ChatApp/groups', methods=['GET'])
def groups():
    if request.args:
        return GroupHandler().getGroupById(request.args)
    else:
        return GroupHandler().getAllGroups()


# Displays all messages of the database  app
# Or choose a specific message to display through mID
@app.route('/ChatApp/groups/<int:gID>/displaymessages', methods=['GET'])
def displayMessages(gID):
    return MessageHandler().getMessageByGroup(gID)


# Displays all messages of the database  app
# Or choose a specific message to display through mID
@app.route('/ChatApp/messages', methods=['GET'])
def messages():
    if request.args:
        return MessageHandler().getMessageById(request.args)
    else:
        return MessageHandler().getAllMessages()


# Add a new person/user to the database through the POST request
# Displays a message if a Get request is sent instead
@app.route('/ChatApp/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return PersonHandler().CreateNewPerson(request.form)
    else:
        return "Please formulate a post request to create a New USER"


# Creates a new group and add it to the database through the POST request
# Delete a desired group from the database with a DELETE request
# Displays a message if a GET request is sent instead
@app.route('/ChatApp/createGroup', methods=['GET', 'POST', 'DELETE'])
def groupCreate():
    if request.method == 'POST':
        return GroupHandler().createNewChatGroup(request.form)
    elif request.method == 'DELETE':
        return GroupHandler().deleteChatGroupbyID(request.args)
    else:
        return "Please formulate a post request to create a new Chat Group or a delete request to delete a new Chat Group"


# Creates a new message and add it to the database through the POST request
# Prompt for a post request if a GET request is sent instead
@app.route('/ChatApp/postMessage', methods=['GET', 'POST'])
def messageCreate():
    if request.method == 'POST':
        return MessageHandler().CreateNewMessage(request.form)
    return "Please formulate a post request to post a new message in a desired group in the Database"

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



@app.route('/ChatApp/contacts/<int:pID>', methods=['GET'])
def displayContacts(pID):
    return ContactHandler().getAllContacts(pID)


@app.route('/ChatApp/contactsinfo/<int:pID>', methods=['GET'])
def displayContactsInfo(pID):
    return ContactHandler().getAllContacts(pID)


if __name__ == '__main__':
    app.run()
