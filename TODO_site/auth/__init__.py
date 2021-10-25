from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from .forms import SignUp, Login, ActionType
from TODO_site.database import db as database
from TODO_site.database import User
from flask_login import LoginManager, current_user

auth = Blueprint('auth', __name__, template_folder='templates')

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@auth.route("/", methods=["GET", "POST"])
def home():
    if current_user.is_authenticated:
        return "<h1>YOU ARE AUTHENTICATED</h1>"
    else:
        return redirect(url_for("auth.welcome"))


@auth.route("/user/welcome")
def welcome():
    action_form = ActionType()
    if request.method == "POST":
        if action_form.validate_on_submit():
            if action_form.login.data:
                return redirect(url_for("auth.user_login"))
            else:
                return redirect(url_for("auth.user_signup"))

    return render_template("home.html", form=action_form)


@auth.route("/user/login", methods=["GET", "POST"])
def user_login():
    login_form = Login()
    # POST METHOD
    if request.method == "POST":
        if login_form.validate_on_submit():
            email = login_form.email.data
            password = login_form.password.data
            user = User.query.filter_by(email=email).first()
            if user is not None:
                pass
    return render_template("login.html", form=login_form)


@auth.route("/user/signup", methods=["GET", "POST"])
def user_signup():
    signup_form = SignUp()
    # POST METHOD
    if request.method == "POST":
        if signup_form.validate_on_submit():
            name = signup_form.name.data
            email = signup_form.email.data
            password = signup_form.password.data
            re_password = signup_form.re_password.data
    return render_template("sign_up.html", form=signup_form)
