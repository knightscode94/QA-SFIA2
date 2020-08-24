from flask import request,Response,jsonify
import requests
from application import app
import random

@app.route('/probability',methods=['GET','POST'])
def probability():
    
    return Response(probability, mimetype='text/plain')
