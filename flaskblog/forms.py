from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
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


class UpdateAccountForm(FlaskForm):

	"""docstring for RegistrationForm"""

	username = StringField('Username', validators=[DataRequired(),
		Length(min=2, max=20)])
	email = StringField('Email',
		validators=[DataRequired(), Email()])

	picture = FileField('Update Profile Picture', 
		validators=[FileAllowed(['jpg','png'])])

	submit = SubmitField('Update')



	def validate_username(self, username): 
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Username already exist,Please choose a different one')
	def validate_email(self, email):
		if email.data != current_user.email:

			user = User.query.filter_by(username=email.data).first()
			if user:
				raise ValidationError('Email already exist,Please choose a different one')


class PostForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()])
	content = TextAreaField('Content',validators=[DataRequired()])
	submit =SubmitField('Post')


class RequestResetForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	submit = SubmitField('Request Password Reset')


	def validate_email(self, email):

		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('There is no account with that email You must Register First')


class ResetPasswordForm(FlaskForm):
		password = PasswordField('Password', validators=[DataRequired(), Length(
		min=5, max=100)])
		confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(
			min=5, max=100), EqualTo('password')])
		submit = SubmitField('Reset Password')


