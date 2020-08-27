from flask import render_template,redirect, url_for, request, jsonify
import requests
from application import app, db
from application.models import all_data


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Magic 8 ball flop')

@app.route('/ball',methods=['GET','POST'])
def ball():
    question = requests.get('http://service2:5001/question')
    answer = requests.get('http://service3:5002/answer')
    probability = requests.post('http://service4:5003/probability',json={"question.text": "answer.text"})
    
    db_data = all_data(question=question.text,answer=answer.text,probability=probability.text)
    db.session.add(db_data)
    db.session.commit()
    data_record=all_data.query.all()
    
    return render_template('ball.html',title='Not so magic 8 Ball',question=question.text,answer=answer.text,probability=probability.text,posts=data_record)
