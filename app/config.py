import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # environment variable FLASK_SECRET_KEY
    # TODO: set SECRET_KEY value each time on system startup on server
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY")
