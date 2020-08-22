from flask import request, Response
from application import app
import random


@app.route('/ball/answers', methods=['POST'])
def ball_answers():
    ball = random.randint(1,3)

    if ball == "1":
        ball_answers = "Without a doubt."

    elif ball == "2":
        ball_answers = "My reply is no."

    elif ball == "3":
        ball_answers = "Better not tell you now."

    else:
        ball_answers = "Error magic not working..."

    return Response(ball_answers, meimtype='text/plain')
