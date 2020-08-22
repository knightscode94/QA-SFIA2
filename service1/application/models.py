#import the db instance
from application import db

#creates a table to save the pair animal-noise
class all_quotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100), nullable = False)
    answer = db.Column(db.String(100), nullable = False)
    probability = db.Column(db.String(100), nullable = False)
