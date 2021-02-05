from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextField, TextAreaField, validators
from wtforms.validators import DataRequired, Length, Email, length, optional

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class ContactForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = StringField('Email', [
        Email(message=('Not a valid email address.')),
        DataRequired()])
    body = StringField('Message', [
        DataRequired(), 
        Length(min=4, message=('Your message is too short.'))])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


class createBugdetForm(FlaskForm):        
    title = StringField('Title',validators=[DataRequired()])
    description = TextAreaField('Description',  validators=[optional(), length(max=300, message='Your message is too long')])
    submit = SubmitField('Create')

#class updateBudgetForm(FlaskForm):

