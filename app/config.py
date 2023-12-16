import os

SECRET_KEY = '123456789'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:dinar123@localhost/choffeshop'
SQLALCHEMY_TRACK_MODIFICATIONS = False
