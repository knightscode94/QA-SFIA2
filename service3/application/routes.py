from flask import request, Response
from application import app
import random


@app.route('/ball/response', methods=['POST'])
def ball_response():
    ball = randomint(1,3)

    elif ball == "1":
        ball_response = "Without a doubt."

    elif ball == "2":
        ball_response = "My reply is no."

    elif ball == "3":
        ball_response = "Better not tell you now."

    else:
        ball_response = "Error magic not working..."

    return Response(ball_response, meimtype='text/plain')
