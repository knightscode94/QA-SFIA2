from flask import render_template, redirect, url_for
from application import app
import requests


@app.route('/', methods = ['GET'])
def home():
    question = requests.get('http://service2:5001/ball/questions')
    response = requests.get('http://service3:5002//ball/response')

    return render_template('home.html', title='Home', question=question.txt, response=response.txt)

