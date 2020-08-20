from application import db

class Responses(db.Model):
    id = db.Column(db.Interger, Primary_key=True)
    responses = db.Column(db.String(50))