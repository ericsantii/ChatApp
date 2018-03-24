from flask import Flask, request
from handler.person import PersonHandler
from handler.groups import GroupHandler

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Chat App"

@app.route('/ChatApp/persons', methods = ['POST', 'GET'])
def getPersonByID():

    if request.method == 'GET':
        if request.args:
            return PersonHandler().getPersonById(request.args)
        else:
            return PersonHandler().getAllPersons()

    elif request.method == 'POST':
        return PersonHandler().insertPerson(request.form)



@app.route('/ChatApp/groups')
def groups():
        handler = GroupHandler()
        return handler.getAllGroups()

if __name__ == '__main__':
    app.run()