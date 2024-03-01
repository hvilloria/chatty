from models.base import db
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

chats_users = db.Table('chats_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('chat_id', db.Integer, db.ForeignKey('chats.id'), primary_key=True)
)

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    chats = db.relationship('Chat', secondary=chats_users, backref=db.backref('users', lazy='dynamic'))
    messages: Mapped[List["Message"]] = db.relationship(back_populates="owner")
    
    def __init__(self, name):
        self.name = name
    
    def as_dict(self):
        return {
            'name': self.name
        }
