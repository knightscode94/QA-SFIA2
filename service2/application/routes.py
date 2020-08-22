from flask import request,Response
import requests
from application import app
import random

@app.route('/get_question',methods=['GET'])
def get_question():
    questions = []
    question = questions[random.randrange(4)]
    return Response(question,mimetype='text/plain')

