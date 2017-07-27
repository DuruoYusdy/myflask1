#flask-wtf 表单

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
    name = StringField('Your name?', validators=[Required()])
    password = StringField('Your password?', validators=[Required()])
    submit = SubmitField('Submit')


class SignForm(FlaskForm):
    email = StringField('Enter your email?', validators=[Required()])
    name = StringField('Enter your name?', validators=[Required()])
    password = StringField('Enter your password?', validators=[Required()])

    submit = SubmitField('Submit')