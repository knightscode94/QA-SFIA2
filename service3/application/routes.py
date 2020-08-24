from flask import request,Response
import requests
from application import app
import random

@app.route('/answer',methods=['GET'])
def answer():
    answers = ["Not a chance",
            "Sure why not",
            "Errrr..."]
    answer = answers[random.randrange(3)]
    return Response(answer,mimetype='text/plain')

