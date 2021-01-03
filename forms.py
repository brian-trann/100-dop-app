from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField
from wtforms.validators import InputRequired, Optional, NumberRange

class LEDForm(FlaskForm):
    '''LED form. Includes validation, choices, and messages'''
    day = IntegerField("Day (0-100)", validators=[InputRequired(message="Day number can't be blank!"), NumberRange(min=0,max=100)])
    mode = SelectField("Mode", validators=[InputRequired()],choices=[('normal','Normal'),('blink','Blink'),('pulse','Pulse')])

