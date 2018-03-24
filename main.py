from flask import Flask, request

from handler.groups import GroupHandler

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Chat App"

@app.route('/ChatApp/groups')
def groups():
        handler = GroupHandler()
        return handler.getAllGroups()

if __name__ == '__main__':
    app.run()