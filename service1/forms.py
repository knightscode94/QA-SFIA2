from flask_wtf import FlaskForm 
from wtforms import StringField, SelectField, SubmitField
from wtforms.fields.html5 import IntegerRangeField
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError

class QuestionForm(FlaskForm):
    question = SelectField('Key Root',
                        default="Will I do amazing at QA?",
                        choices=["Will I do amazing at QA?",
                            "Is Luke the most awesome lecturer at QA?",
                            "Will tornado shark ever be a real thing?",
                            "Will I live a long life?"],
                        validators=[
                            DataRequired(message="You must ask me a question!")])
    submit = SubmitField('Tell me my future')