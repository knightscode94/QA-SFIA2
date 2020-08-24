from flask import request,Response,jsonify
import requests
from application import app
import random

@app.route('/probability',methods=['GET','POST'])
def probability():
    
    data_sent = request.get_json()
    question = data_sent.keys()
    answer = data_sent.values()

    
    return Response(probability, mimetype='text/plain')
