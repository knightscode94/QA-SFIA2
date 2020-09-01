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
            probability = str(random.randint(30,100)), "% True"
        elif answer == "Sure why not":
            probability = str(random.randint(1,60)), "% True"
        elif answer == "I mean maybe?":
            probability = "Lol even the 8 ball doesnt know!"
        else:
            probability = "Yea no clue sorry..."

    elif question == "Is Luke the most epic lecturer at QA?":
        if answer == "Not a chance":
            probability = str(random.randint(1,70)), "% True"
        elif answer == "Sure why not":
            probability = str(random.randint(48,100)), "% True"
        elif answer == "I mean maybe?":
            probability = "Lol even the 8 ball doesnt know!"
        else:
            probability = "Yea no clue sorry..."
        
    elif question == "Will I live a long life?": 
        if answer == "Not a chance":
            probability = str(random.randint(26,69)), "% True"
        elif answer == "Sure why not":
            probability = str(random.randint(48,80)), "% True"
        elif answer == "I mean maybe?":
            probability = "Lol even the 8 ball doesnt know!"
        else:
            probability = "Yea no clue sorry..."

    elif question == "Is this a load of rubbish?":
        if answer == "Not a chance":
            probability = str(random.randint(1,50)), "% True"
        elif answer == "Sure why not":
            probability = str(random.randint(50,100)), "% True"
        elif answer == "I mean maybe?":
            probability = "Lol even the 8 ball doesnt know!"
        else:
            probability = "Yea no clue sorry..."
            
    else:
        probability = "Yea no clue sorry..."


    return Response(probability, mimetype='text/plain')
