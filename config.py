import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_DEVELOPMENT_URL')


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DB_TEST_URL')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
