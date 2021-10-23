from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class ActionType(FlaskForm):
    login = SubmitField("LOGIN")
    sign_up = SubmitField("SIGN UP")


class Login(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("LOGIN!")


class SignUp(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    re_password = PasswordField("Re-enter Password", validators=[DataRequired()])
    submit = SubmitField("LETS GO!")
