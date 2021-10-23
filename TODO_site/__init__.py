from flask import Flask
from TODO_site.auth.auth import auth
from flask_login import LoginManager


def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(auth)
    return flask_app


app = create_app()
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.blueprint_login_views = {
    'admin': '/admin/login',
    'site': '/login',
}


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


if __name__ == "__main__":
    app.run()
