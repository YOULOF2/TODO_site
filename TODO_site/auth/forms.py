from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class ActionType(FlaskForm):
    login = SubmitField(label="LOGIN")
    sign_up = SubmitField(label="SIGN UP")


class Login(FlaskForm):
    email = StringField("Email", validators=[Email(), DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("LOGIN!")


class SignUp(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[Email(), DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    re_password = PasswordField("Re-enter Password", validators=[DataRequired()])
    submit = SubmitField("LETS GO!")
