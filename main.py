from flask import Flask, request,jsonify,render_template, redirect, url_for
from handler.person import PersonHandler
from handler.groups import GroupHandler
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to PapayaChat App"

@app.route('/ChatApp/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        return PersonHandler().CreateNewPerson(request.form)

    else:
        return "Welcome to PapayaChat! Please formulate a post request to create a New USER"

@app.route('/ChatApp/persons', methods = ['POST', 'GET'])
def getPersonByID():
    if request.method == 'GET':
        if request.args:
            return PersonHandler().getPersonById(request.args)
        else:
            return PersonHandler().getAllPersons()



@app.route('/ChatApp/groups', methods = ['POST', 'DELETE'])
def groups():
        handler = GroupHandler()
        if request.method == 'POST':
            print("Hello")
            return handler.createNewChatGroup(request.form)
        else:
            return handler.deleteChatGroupbyID(request.args)

if __name__ == '__main__':
    app.run()