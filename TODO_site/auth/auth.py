from flask import Blueprint, render_template, request
from forms import SignUp, Login, ActionType

auth = Blueprint('auth', __name__, template_folder='templates')


@auth.route("/", method=["GET", "POST"])
def home():
    action_form = ActionType()
    if request.method == "POST":

    return render_template("home.html", form=action_form)
