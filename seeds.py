# import sys
# import os

# # Agregar el directorio padre al sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app import app, db
from models.user import User
from models.chat import Chat
from models.message import Message
from sqlalchemy import text

users_data = [
    {'name': 'John'},
    {'name': 'Jane'}
]

with app.app_context():
    db.session.execute(text('DELETE FROM messages'))
    db.session.execute(text('DELETE FROM chats_users'))
    db.session.execute(text('DELETE FROM chats'))
    db.session.execute(text('DELETE FROM users'))
    db.session.commit()

    # create users
    for user_data in users_data:
        user = User(name= user_data['name'])
        db.session.add(user)

    # create one chat
    chat = Chat()
    db.session.add(chat)

    #create some messages
    john = User.query.filter_by(name =  'John').first()
    jane = User.query.filter_by(name =  'Jane').first()
    john.chats.append(chat)
    jane.chats.append(chat)
    john_say_hello = Message("hey how are you?",  owner = john)
    jane_say_hi_back = Message("doing good and you?", owner = jane)
    john_answers_hi = Message("good to hear!", owner = john)

    # assign messages
    chat.messages.append(john_say_hello)
    chat.messages.append(jane_say_hi_back)
    chat.messages.append(john_answers_hi)

    # insert changes
    db.session.commit()
