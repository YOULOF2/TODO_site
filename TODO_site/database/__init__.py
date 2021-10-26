from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    cards = relationship("Cards", back_populates="user")


class Cards(db.Model):
    __tablename__ = 'cards'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    sub_title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, nullable=False)

    user = relationship("User", back_populates="cards")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
