from flask import request, Response
from application import app
import requests, random


@app.route('/ball/number', methods=['GET'])
def ball_num():
    ball = random.randint(1,20)
    return Response(ball, mimetype='text/plain')



