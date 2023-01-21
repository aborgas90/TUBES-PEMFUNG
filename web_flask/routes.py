from web_flask import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html',title = 'Crptod')

@app.route('/main')
def main():
    return render_template('main.html',title = '')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/graphic')
def graphic():
    return render_template('graphic.html')

@app.route('/login')
def login():
    return render_template('login.html')