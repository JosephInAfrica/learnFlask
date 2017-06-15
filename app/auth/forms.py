from flask.ext.wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtoforms.validators import Required,Length,Email,Regexp,EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(Form):
    email=StringField('Email',validators=[Required(),Length(1,64)])
    password=PasswordField('Password',validators=[Required()])
    remember_me=BooleanField('Keep me logged in')
    submit=SubmitField('Submit')

class RegistrationForm(Form):
    email=StringField('Email',validators=[Required(),Length(1,64),Email()])
    username=StringField('Username',validators=[Required(),Length(1,64),Regexp('^[A-Za-z][A-Za-z_.]*$',0,'Username must have onlhy letters,numbers,dots or underscores')])


    password=PasswordField('Password',validators=[Required(),EqualTo('password2',message='Passwords must match')])
    password2=PasswordField('Confirm Password',validators=[Required()])
    submit=SubmitField('Register')

    def validate_email(self,field):
        if User.query.filter_by(email.field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class ChangePasswordForm(Form):
    old_password=PasswordField('Old password',validators=[Required()])
    password=PasswordField('New password',validators=[Required(),EqualTo('password2',message='Password must match.')])
    password2=PasswordField('Confirm New Password',validators=[Required()])
    submit=SubmitField('Update Password.')

class PasswordResetRequestForm(Form):
    email=StringField('Email',validators=[Required(),Length(1,64),Email()])
    submit=SubmitField('Reset Password')

class PasswordResetForm(Form):
    email=StringField('Email',validators=[Required(),Length(1,64),Email()])
    password=PasswordField('New Password',validators=[Required(),EqualTo('password2',message=Password must match.)])
    password2=PasswordField('Confirm Password',validators=[Required()])

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown email address.')
class ChangeEmailForm(Form):
    email=StringField('New Email',validators=[Required(),Length(1,64),Email()])
    password=PasswordField('password',validators=[Required()])
    submit=SubmitField('Update Email Address')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')










