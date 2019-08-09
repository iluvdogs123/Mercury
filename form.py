from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, validators
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8,max=25)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=2, max=32)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=2, max=32)])
    school = SelectField(u'School', choices=[], coerce=int)
    grade = IntegerField('Student Grade', validators=[DataRequired(), validators.NumberRange(min=6, max=12)])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8,max=25)])
    remember = BooleanField('Remember Password')
    submit = SubmitField('Login')
