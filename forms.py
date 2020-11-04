from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):

	"""docstring for RegistrationForm"""

	username = StringField('Username', validators=[DataRequired(),
		Length(min=2, max=20)])
	email = StringField('Email',
		validators=[DataRequired(), Email()])

	password = PasswordField('Password', validators=[DataRequired(), Length(
		min=5, max=100)])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(
		min=5, max=100), EqualTo('password')])
	submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):

	"""docstring for RegistrationForm"""
	email = StringField('Email',
		validators=[DataRequired(), Email()])

	password = PasswordField('Password', validators=[DataRequired(), Length(
		min=5, max=100)])

	remember = BooleanField('Remember Me')

	submit = SubmitField('Login')		
