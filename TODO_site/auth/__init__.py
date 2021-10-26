from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import SignUp, Login, ActionType
from TODO_site.database import db
from TODO_site.database import User
from flask_login import LoginManager, current_user, login_user
from functools import wraps

SALT_TIMES = 20

auth = Blueprint('auth', __name__, template_folder='templates')

login_manager = LoginManager()


def login_required(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_anonymous:
            return redirect(url_for("auth.welcome"))
        return func(*args, **kwargs)

    return decorated_function


def not_logged_in(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for("website.main"))
        return func(*args, **kwargs)

    return decorated_function


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@auth.route("/", methods=["GET"])
def home():
    if current_user.is_authenticated:
        return redirect(url_for("website.main"))
    else:
        return redirect(url_for("auth.welcome"))


@auth.route("/user/welcome", methods=["GET", "POST"])
@not_logged_in
def welcome():
    print("WELCOME")
    action_form = ActionType()
    if request.method == "POST":
        if action_form.validate_on_submit():
            if action_form.login.data:
                return redirect(url_for("auth.user_login"))
            else:
                return redirect(url_for("auth.user_signup"))

    return render_template("home.html", form=action_form)


@auth.route("/user/login", methods=["GET", "POST"])
@not_logged_in
def user_login():
    login_form = Login()
    # POST METHOD
    if request.method == "POST":
        if login_form.validate_on_submit():
            email = login_form.email.data
            password = login_form.password.data
            user = User.query.filter_by(email=email).first()
            if user is not None:
                if check_password_hash(user.password, password):
                    login_user(user)
                    return redirect(url_for("website.main"))
                else:
                    flash("Wrong password, please redo")
                    return redirect(url_for("auth.user_login"))
            else:
                flash("You don't have an account. Sign up to continue.")
                return redirect(url_for("auth.user_signup"))
    return render_template("login.html", form=login_form)


@auth.route("/user/signup", methods=["GET", "POST"])
@not_logged_in
def user_signup():
    signup_form = SignUp()
    # POST METHOD
    if request.method == "POST":
        if signup_form.validate_on_submit():
            email = signup_form.email.data
            password = signup_form.password.data
            re_password = signup_form.re_password.data
            # with current_app.app_context():
            if User.query.filter_by(email=email).first() is None:
                if password == re_password:
                    pass_hash = generate_password_hash(password, salt_length=SALT_TIMES, method="pbkdf2:sha256")
                    user = User(
                        email=email,
                        password=pass_hash,
                    )
                    db.session.add(user)
                    db.session.commit()
                    login_user(user)
                    return redirect(url_for("website.main"))
                else:
                    flash("You retyped the password incorrectly, try again.")
                    return redirect(url_for("auth.user_signup"))
            else:
                flash("You are already registered. Please login.")
                return redirect(url_for("auth.user_login"))
    return render_template("sign_up.html", form=signup_form)
