from flask import Flask, request
from flask.json import jsonify

# creating the flask app
app = Flask(__name__)


# route for starting page of the application
@app.route('/')
def show_index_page():
    return '<h1> This is the starting page of the application</h1>'


# route for contact page of the application
@app.route('/contact')
def show_contact_page():
    return '<h1> This is the contact page of the application</h1>'


# route for about page of the application
@app.route('/about')
def show_about_page():
    return '<h1> This is the about page of the application</h1>'


# route for users page of the application
@app.route('/users/<string:name>')
def show_users_page(name):
    return '<h1>Hello {}</h1>'.format(name)


# route for project page of the application
# by default the route, input datatype is string
@app.route('/project/<int:pagenumber>')
def show_project_page(pagenumber):
    return '<h1>This is project no: {}</h1>'.format(pagenumber)


### passing parameters into the app showing JSON (dictionary format) output

# showing json format(dictionary) output in the web application
@app.route('/json')
def show_json_page():
    return jsonify({'name':'Bhuvi', 'location':'Chennai'})


### choosing get or post method in html forms

# POST, GET
# default method for routing is 'GET' method
@app.route('/form', methods=['POST', 'GET'])
def show_form_page():
    return "<h1>This is the form page, using POST and GET method</h1>"


### taking default values if user doesn't give parameters

# Student page
@app.route('/student',               methods = ['POST', 'GET'], defaults = {"studentname": "Learners"})
@app.route('/student/<studentname>', methods = ['POST', 'GET'])
def show_student_page(studentname):
    return '<h1>Hello {}</h1>'.format(studentname)


### taking multiple inputs from user in flask application

## http://127.0.0.1:5000/query?name=Bhuvanesh&degree=BE&location=Chennai

# query page
@app.route('/query')
def show_query_page():
    name = request.args.get('name')
    degree = request.args.get('degree')
    location = request.args.get('location')
    return "<h1>Hello {} {} from {}.</h1>".format(name, degree, location)


### passing parameters from html form

# login page
@app.route('/login')
def show_login_page():
    return """
        <form action='/processloginform' method = ['POST']>

            <h1>Enter your details to continue</h1>
            <input type = "text" name = 'username' placeholder = 'Enter your name'/></br></br>
            <input type = "password" name = 'password' placeholder = 'Enter your password'/></br></br>


            <input type = "submit" value = "login">

        </form>
    """


@app.route('/processloginform', methods = ['POST'])
def processloginform():
    username = request.form['username']
    password = request.form['password']
    return "<h1>Hello {}, Welcome to our site, you're successfully logged in </h1>".format(username)


if __name__ == '__main__':
    app.run(debug=True)