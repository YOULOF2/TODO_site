from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NewToDo(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    sub_title = StringField("Sub-Title", validators=[DataRequired()])
    body = StringField("Body", validators=[DataRequired()])
    submit = SubmitField("Submit")
