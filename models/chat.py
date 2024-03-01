from models.base import db
from sqlalchemy.orm import Mapped, mapped_column
from typing import List


class Chat(db.Model):
    __tablename__ = 'chats'

    id: Mapped[int] = mapped_column(primary_key=True)
    messages: Mapped[List["Message"]] = db.relationship(back_populates="chat")
