from flask import request, Response
from application import app


@app.route('/ball/response', thods=['POST'])
def ball_response():
    ball = request.data.decode("utf-8")
    if ball == "1":
        response = "You may rely on it."
    elif ball == "2":
        response = "Yes – definitely."
    elif ball == "3":
        response = "Yes."
    elif ball == "4":
        response = "Without a doubt."
    elif ball == "5":
        response = "Very doubtful."
    elif ball == "6":
        response = "Signs point to yes."
    elif ball == "7":
        response = "Reply hazy, try again."
    elif ball == "8":
        response = "Outlook good."
    elif ball == "9":
        response = "Outlook not so good."
    elif ball == "10":
        response = "My sources say no."
    elif ball == "11":
        response = "My reply is no."
    elif ball == "12":
        response = "Most likely."
    elif ball == "13":
        response = "It is decidedly so."
    elif ball == "14":
        response = "It is certain."
    elif ball == "15":
        response = "Don’t count on it."
    elif ball == "16":
        response = "Concentrate and ask again"
    elif ball == "17":
        response = "Cannot predict now."
    elif ball == "18":
        response = "Better not tell you now."
    elif ball == "19":
        response = "Ask again later."
    elif ball == "20":
        response = "As I see it, yes."
    else:
        response = "Error magic not working..."

    return Response(response, meimtype='text/plain')
