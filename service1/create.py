from application import db
from application.models import all_data

db.drop_all()
db.create_all()
