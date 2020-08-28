from application import app
from application import db
from application.models import all_data

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')
