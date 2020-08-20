from flask import request, Response
from application import app


@app.route('/ball/response', thods=['POST'])
def ball_response():
    ball = request.data.decode("utf-8")
    if ball == "1":
        ball_response = "You may rely on it."
    elif ball == "2":
        ball_response = "Yes – definitely."
    elif ball == "3":
        ball_response = "Yes."
    elif ball == "4":
        ball_response = "Without a doubt."
    elif ball == "5":
        ball_response = "Very doubtful."
    elif ball == "6":
        ball_response = "Signs point to yes."
    elif ball == "7":
        ball_response = "Reply hazy, try again."
    elif ball == "8":
        ball_response = "Outlook good."
    elif ball == "9":
        ball_response = "Outlook not so good."
    elif ball == "10":
        ball_response = "My sources say no."
    elif ball == "11":
        ball_response = "My reply is no."
    elif ball == "12":
        ball_response = "Most likely."
    elif ball == "13":
        ball_response = "It is decidedly so."
    elif ball == "14":
        ball_response = "It is certain."
    elif ball == "15":
        ball_response = "Don’t count on it."
    elif ball == "16":
        ball_response = "Concentrate and ask again"
    elif ball == "17":
        ball_response = "Cannot predict now."
    elif ball == "18":
        ball_response = "Better not tell you now."
    elif ball == "19":
        ball_response = "Ask again later."
    elif ball == "20":
        ball_response = "As I see it, yes."
    else:
        ball_response = "Error magic not working..."

    return Response(ball_response, meimtype='text/plain')
