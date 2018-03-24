from flask import Flask, request
from handler.person import PersonHandler
from handler.groups import GroupHandler

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Chat App"

@app.route('/ChatApp/persons')
def persons():
    if request.args:
        return PersonHandler().searchPerson(request.args)
    else:
        handler = PersonHandler()
        return handler.getAllPersons()

@app.route('/ChatApp/persons/<int:pID>')
def getPersonById(pID):
    return PersonHandler().getPersonById(pID)

@app.route('/ChatApp/groups', methods = ['POST', 'DELETE'])
def groups():
        handler = GroupHandler()
        if request.method == 'POST':
            return handler.createNewChatGroup(request.form)
        else:
            return handler.deleteChatGroupbyID(request.args)

@app.route('/ChatApp/member', methods = ['POST', 'GET'])
def memberByID():
        handler = GroupHandler()
        if request.method == 'POST':
            return handler.add(request.form)
        else:
            return handler.deleteChatGroupbyID(request.args)

if __name__ == '__main__':
    app.run()