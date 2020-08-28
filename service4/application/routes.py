from flask import request, Response, jsonify
import requests
from application import app
import random


@app.route('/probability', methods=['GET', 'POST'])
def probability():

    data = request.get_json()

    question = data["question"]
    answer = data["answer"]
    if question == "Will I ever be good enough at QA?":
        if answer == "Not a chance":
            probability = str(random.randint(1,100)), " True"
        elif answer == "Sure why not":
            probability = str(random.randint(1,100)), " True"
        elif answer == "I mean maybe?":
            probability = "Lol even the 8 ball doesnt know!"
        else:
            probability = "Yea no clue sorry..."

    elif question == "Is Luke the most epic lecturer at QA?":
        if answer == "Not a chance":
            probability = str(random.randint(1,100)), " True"
        elif answer == "Sure why not":
            probability = str(random.randint(1,100)), " True"
        elif answer == "I mean maybe?":
            probability = "Lol even the 8 ball doesnt know!"
        else:
            probability = "Yea no clue sorry..."
        
    elif question == "Will I live a long life?": 
        if answer == "Not a chance":
            probability = str(random.randint(1,100)), " True"
        elif answer == "Sure why not":
            probability = str(random.randint(1,100)), " True"
        elif answer == "I mean maybe?":
            probability = "Lol even the 8 ball doesnt know!"
        else:
            probability = "Yea no clue sorry..."

    elif question == "Is this a load of rubbish?":
        if answer == "Not a chance":
            probability = str(random.randint(1,100)), " True"
        elif answer == "Sure why not":
            probability = str(random.randint(1,100)), " True"
        elif answer == "I mean maybe?":
            probability = "Lol even the 8 ball doesnt know!"
        else:
            probability = "Yea no clue sorry..."
            
    else:
        probability = "Yea no clue sorry..."


    return Response(probability, mimetype='text/plain')
