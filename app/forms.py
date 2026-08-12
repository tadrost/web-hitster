from wtforms import SubmitField
from flask_wtf import FlaskForm

class EmptyForm(FlaskForm):
    submit = SubmitField("Submit")