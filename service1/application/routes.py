from flask import render_template, redirect, url_for
from application import app
import requests


@app.route('/', methods = ['GET', 'POST'])
def home():
    username = requests.get('http://service2:5001/ball/questions')
	game = requests.get('http://service3:5002/ball/responses')
    return render_template('home.html', title='Home', questions=questions.text, responses=responses.text)

