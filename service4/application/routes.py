#This service will also create an “Object” however this “Object” 
# must be based upon the results of service #2 + #3 using some pre-defined rules.


from flask import request, Response
from application import app
from application.models import Response
import requests, random


@app.route('/get/ball_response',methods=['GET','POST'])
def ball():
    number = requests.get('http://service2:5001/ball/number')
    ball_response = requests.post('http://service2:5002/ball/response', data=number.text)

    ball_response=Response(ball_response=ball_response.text)

    return ball_response.text
