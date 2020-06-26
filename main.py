from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.before_request
def before_request():
    #Funcion to test callback before the request
    print('Before the request')

@app.after_request
def after_request(response):
    #Funcion to test callback after the request
    print('After the request')    
    return response

@app.route('/')
def index():
    #Function to render template in index.html and hide or not information with the conditionals in the html document
    name = 'Everyone'
    test = 'Flask'
    is_premium = False
    skills = ['Python', 'MySQL', 'MongoDB', 'Flask', 'Django']

    return render_template('index.html', username=name, test=test, is_premium=is_premium, skills=skills)

@app.route('/about')
def about():
    #Another template with different html document
    print('Test Callback')
    return render_template('about.html')

@app.route('/user/<last_name>/<name>/<int:age>')   
def usuario(last_name, name, age):
    return 'Hello ' + last_name + ' ' + name + ' ' + str(age)

@app.route('/data')
def datos():
    #Function to test query strings
    nombre = request.args.get('name', '') #Dic
    course = request.args.get('course', '') #Dic
    
    return 'List of data: ' 'of ' + nombre + ' in ' + course

if __name__ == "__main__":
    app.run(debug=True)
