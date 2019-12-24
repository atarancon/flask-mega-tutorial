from flask_wtf import Form 
from wtforms import StringField, PasswordField, ValidationError , SubmitField
from wtforms.validators import DataRequired, EqualTo, Email

from app.models import User


class RegistrationForm(Form):
    email = StringField('Email',validators=[DataRequired()])
    username = StringField('UserName',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(),EqualTo("pass_conf",message="Password must match")])
    pass_conf=PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField("Register")

#validate for email 
    def validate_email(self,field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError("Your Email has been already register")

    def validate_username(self,field):
         if User.query.filter_by(username = field.data).first():
            raise ValidationError("Your username has been already register")


class LoginForm(Form):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField('Log In')