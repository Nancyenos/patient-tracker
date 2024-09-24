import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Define the SQLite database URI
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'asdfrevbclojhg'

