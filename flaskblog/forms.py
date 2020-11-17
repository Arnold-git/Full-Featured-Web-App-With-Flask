from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User

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


	def validate_username(self, username):

		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Username already exist,Please choose a different one')
	def validate_email(self, email):

		user = User.query.filter_by(username=email.data).first()
		if user:
			raise ValidationError('Email already exist,Please choose a different one')




class LoginForm(FlaskForm):

	"""docstring for RegistrationForm"""
	email = StringField('Email',
		validators=[DataRequired(), Email()])

	password = PasswordField('Password', validators=[DataRequired(), Length(
		min=5, max=100)])

	remember = BooleanField('Remember Me')

	submit = SubmitField('Login')		
