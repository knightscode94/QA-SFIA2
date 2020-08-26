from application import db

class all_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(100), nullable = False)
    answer = db.Column(db.String(100), nullable = False)
    probability = db.Column(db.String, nullable = False)
