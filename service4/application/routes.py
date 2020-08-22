from flask import request,Response,jsonify
import requests
from application import app
import random

@app.route('/get_probability',methods=['GET','POST'])
def get_probability():
    
    data_sent = request.get_json()
    question = data_sent.keys()
    answer = data_sent.values()

    
    return Response(data_returned, mimetype='text/plain') 
