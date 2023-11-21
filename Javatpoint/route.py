from flask import Flask
app = Flask(__name__)  


@app.route('/')  
def home_page():  
    return "hello, welcome to our website"

"""
@app.route('/home')  
def home():  
    return "hello, welocme to the home page"

@app.route('/home/<name>')  
def home(name):  
    return "hello,"+name
"""

@app.route('/home/<int:age>')  
def home(age):  
    return "Age = %d"%age;  

if __name__ =="__main__":  
    app.run(debug = True, port=5002)