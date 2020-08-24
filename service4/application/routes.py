from flask import request,Response,jsonify
import requests
from application import app
import random

@app.route('/probability',methods=['GET','POST'])
def probability():
    
    data_sent = request.get_json()
    question = data_sent.keys()
    answer = data_sent.values()

    for key in question:
        for value in answer:
            if answer[value] == "Not a chance" & question[key] == "Will I ever be good enough at QA?":
                probability = "60% True"
            elif answer[value] == "Not a chance" & question[key] == "Is Luke the most epic lecturer at QA?":
                probability = "10% True"
            elif answer[value] == "Not a chance" & question[key] == "Will I live a long life?":
                probability = "90%"    
            elif answer[value] == "Not a chance" & question[key] == "Is this a load of rubbish?":
                probability = "100% True"
            elif answer[value] == "Sure why not" & question[key] == "Will I ever be good enough at QA?":
                probability = "30% True"
            elif answer[value] == "Sure why not" & question[key] == "Is Luke the most epic lecturer at QA?":
                probability = "90% True"
            elif answer[value] == "Sure why not" & question[key] == "Will I live a long life?":
                probability = "40% True"    
            elif answer[value] == "Sure why not" & question[key] == "Is this a load of rubbish?":
                probability = "10% True"   
            elif answer[value] == "Errrr..." & question[key] == "Will I ever be good enough at QA?":
                probability = "60% True"
            elif answer[value] == "Errrr..." & question[key] == "Is Luke the most epic lecturer at QA?":
                probability = "20% True"
            elif answer[value] == "Errrr..." & question[key] == "Will I live a long life?":
                probability = "70% True"    
            elif answer[value] == "Errrr..." & question[key] == "Is this a load of rubbish?":
                probability = "10% True"  
            else:
                probability = "You wish I had an answer"
    
    return Response(probability, mimetype='text/plain') 