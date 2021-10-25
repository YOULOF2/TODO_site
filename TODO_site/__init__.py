from flask import Flask
import os
from TODO_site.database import db
from TODO_site.auth import auth as auth_app, login_manager
from TODO_site.website import website as website_app

SECRET_KEY = os.urandom(32)


def create_app():
    flask_app = Flask(__name__)
    flask_app.config['SECRET_KEY'] = SECRET_KEY
    flask_app.register_blueprint(auth_app)
    flask_app.register_blueprint(website_app)
    login_manager.init_app(flask_app)

    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/database.db'
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(flask_app)
    return flask_app


app = create_app()

if not os.path.isfile("/database/database.db"):
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
