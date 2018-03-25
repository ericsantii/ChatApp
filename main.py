from flask import Flask, request,jsonify,render_template, redirect, url_for
from handler.person import PersonHandler
from handler.groups import GroupHandler
registeredForm = object
app = Flask(__name__)
@app.route('/')
def home():
    return "Welcome to PapayaChat App"

# Route for handling the login page logic
@app.route('/ChatApp/register', methods=['GET', 'POST'])
def register():
    global registeredForm
    if request.method == 'POST':
        registeredForm = request.form
        return redirect(url_for('welcome'))
    else:
        return render_template('register.html')

@app.route('/ChatApp/welcome')
def welcome():
    #Se verifica si el usuario existe
    #PersonHandler().CreateNewPerson(request.form)
    #Aqui se utiliza request.form['pFirstName] y request.form['pLastName']
    return "Welcome to PapayaChat!"

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