from flask import Flask
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
@app.route('/project/<int:pagenumber>')
def show_project_page(pagenumber):
    return '<h1>This is project no: {}</h1>'.format(pagenumber)


# showing json format(dictionary) output in the web application
@app.route('/json')
def show_json_page():
    return jsonify({'name':'Bhuvi', 'location':'Chennai'})


if __name__ == '__main__':
    app.run(debug=True)