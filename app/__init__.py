from flask import Flask, g
from flask_wtf import CSRFProtect
from flask_cors import CORS
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from .blueprints.auth import auth

flaskApp = Flask(__name__)
CORS(flaskApp)  # enable CORS on all routes
flaskApp.config.from_object(Config)
csrf = CSRFProtect(flaskApp)
db = SQLAlchemy(flaskApp)
migrate = Migrate(flaskApp, db)
login = LoginManager(flaskApp)
login.login_view = 'index'  # route for index.html

from app import routes, model, gameplay
from app.model import Person

@login.user_loader
def load_user(id):
    return Person.query.get(int(id))

def create_app():
    app = Flask(__name__)
    app.config['TESTING'] = True  # Enable testing mode

    # Register Blueprints
    app.register_blueprint(auth, url_prefix='/auth')

    return app