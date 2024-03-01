from flask import Flask
from flask_migrate import Migrate
from models.base import db
from dotenv import load_dotenv
from models.user import User
from models.chat import Chat
from models.message import Message

load_dotenv()
app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')

db.init_app(app)
Migrate(app, db)

@app.route('/')
def hello():
   return [user.as_dict() for user in  User.query.all()]


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
