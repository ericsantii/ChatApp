from flask import Flask, request,jsonify,render_template, redirect, url_for
from handler.person import PersonHandler
from handler.groups import GroupHandler
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to PapayaChat App"

@app.route('/ChatApp/persons', methods = ['GET'])
def getPersonByID():
    if request.args:
        return PersonHandler().getPersonById(request.args)
    else:
        return PersonHandler().getAllPersons()

@app.route('/ChatApp/groups', methods = ['GET'])
def groups():
    if request.args:
        return GroupHandler().getGroupById(request.args)
    else:
        return GroupHandler().getAllGroups()

@app.route('/ChatApp/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return PersonHandler().CreateNewPerson(request.form)
    else:
        return "Welcome to PapayaChat! Please formulate a post request to create a New USER"

@app.route('/ChatApp/createNewGroup', methods=['POST', 'DELETE'])
def groupCreate():
    if request.method == 'POST':
        return GroupHandler().createNewChatGroup(request.form)
    else:
        return GroupHandler().deleteChatGroupbyID(request.args)



if __name__ == '__main__':
    app.run()