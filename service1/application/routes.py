from flask import render_template, redirect, url_for
from application import app
import requests


@app.route('/', methods = ['GET', 'POST'])
def home():
    
    return render_template('home.html', title='Home')

