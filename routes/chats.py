from flask import Blueprint

chat_blueprint = Blueprint('chats', __name__, url_prefix='/chats')

chat_blueprint.get('/')
