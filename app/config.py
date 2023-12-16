import os

SECRET_KEY = 'your_secret_key'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:dinar123@localhost/choffeshop'
SQLALCHEMY_TRACK_MODIFICATIONS = False
