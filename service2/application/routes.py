from flask import request, Response
from application import app
import requests


@app.route('/ball/questions', methods=['GET'])
def questions():
    
    return Response(questions, mimetype='text/plain')



