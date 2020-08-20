from flask import render_template, redirect, url_for
from application import app
import requests, WTForms

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html', title='Home')

