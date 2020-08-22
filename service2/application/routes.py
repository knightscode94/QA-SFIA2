from flask import request,Response
import requests
from application import app
import random

@app.route('/get_question',methods=['GET'])
def get_question():
    questions = ["Will I ever be good enough at QA?",
                "Is Luke the most epic lecturer at QA?",
                "Will I live a long life?",
                "Is this a load of rubbish?"]
    question = questions[random.randrange(4)]
    return Response(question,mimetype='text/plain')

