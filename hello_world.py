from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return('Hello World')


@app.route('/mars')
def mars():
    return('Welcome to Jupyter')

@app.route('/gallery')
def gallery():
    return('Welcome to Gallery')

@app.route('/contact')
def contact():
    return('Welcome to contact')

@app.route('/login')
def login():
    return('Please enter login credentials')

app.run(debug=True)