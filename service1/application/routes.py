from flask import render_template, redirect, url_for, requests
from application import app
import requests


@app.route('/', methods = ['GET', 'POST'])
def home():
    questions = requests.get('http://service2:5001/ball/questions')
	#answers = requests.get('http://service3:5002/ball/answers')
    return render_template('home.html', title='Home', questions=questions.text)

