#This service will also create an “Object” however this “Object” 
# must be based upon the results of service #2 + #3 using some pre-defined rules.


from flask import request, Response
from application import app
import requests, random


@app.route('/get/animal',methods=['GET','POST'])
def animal():
    number = requests.get('http://service2:5001/ball/number')
    response = requests.post('http://service2:5002/ball/response', data=number.text)
    return response = response.text
