from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)
    cards = relationship("Cards", back_populates="user")

    def __repr__(self):
        print(f"There are {self.name.count()} records in  the table\n"
              f"Table name = {self.__tablename__}")


class Cards(db.Model):
    __tablename__ = 'cards'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    sub_title = db.Column(db.Text, nullable=False)
    body = db.Column(db.Text, unique=True, nullable=False)
    cards = relationship("User", back_populates="cards")

    def __repr__(self):
        print(f"There are {self.title.count()} records in  the table\n"
              f"Table name = {self.__tablename__}")
