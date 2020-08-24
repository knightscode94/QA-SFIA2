from flask import request, Response, jsonify
import requests
from application import app
import random


@app.route('/probability', methods=['GET', 'POST'])
def probability():

    question = request.question()
    answer = request.answer()

    if answer == "Not a chance" & question == "Will I ever be good enough at QA?":
        probability = "60% True"
    elif answer == "Not a chance" & question == "Is Luke the most epic lecturer at QA?":
        probability = "10% True"
    elif answer == "Not a chance" & question == "Will I live a long life?":
        probability = "90%"
    elif answer == "Not a chance" & question == "Is this a load of rubbish?":
        probability = "100% True"
    elif answer == "Sure why not" & question == "Will I ever be good enough at QA?":
        probability = "30% True"
    elif answer == "Sure why not" & question == "Is Luke the most epic lecturer at QA?":
        probability = "90% True"
    elif answer == "Sure why not" & question == "Will I live a long life?":
        probability = "40% True"
    elif answer == "Sure why not" & question == "Is this a load of rubbish?":
        probability = "10% True"
    elif answer == "Errrr..." & question == "Will I ever be good enough at QA?":
        probability = "60% True"
    elif answer == "Errrr..." & question == "Is Luke the most epic lecturer at QA?":
        probability = "20% True"
    elif answer == "Errrr..." & question == "Will I live a long life?":
        probability = "70% True"
    elif answer == "Errrr..." & question == "Is this a load of rubbish?":
        probability = "10% True"
    else:
        probability = "You wish I had an answer"

    return Response(probability, mimetype='text/plain')
