from flask import render_template, redirect, url_for
from application import app
import requests

@app.route('/', methods=['GET'])
def home():
    @app.route('/ball/start', methods = ['GET'])
	username = requests.get('http://service2:5001/ball/questions')
	game = requests.get('http://service3:5002//ball/response')

    return render_template('home.html', title='Home', question=question.txt, response=response.txt)

