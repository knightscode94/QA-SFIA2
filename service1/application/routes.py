from flask import render_template,redirect, url_for, request, jsonify
import requests
from application import app,db
from application.models import all_answers


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/generate_answer',methods=['GET','POST'])
def generate_answer():
    question = requests.get('http://service2:5001/get_question')
    answer = requests.get('http://service3:5002/get_answer')
    probability = requests.post('http://service4:5003/get_probability',json={question.text: answer.text})
    
    db_data = all_answers(question=question.text,answer=answer.text,probability=probability.text)
    db.session.add(db_data)
    db.session.commit()
    data_record=all_data.query.all()
    
    return render_template('generate_data.html',title='data Generator',question=question.text,answer=answer.text,probability=probability.text,posts=data_record)
