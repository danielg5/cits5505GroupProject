from flask import Flask
from flask_cors import CORS
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

flaskApp = Flask(__name__)
CORS(flaskApp)  # enable CORS on all routes
flaskApp.config.from_object(Config)
db = SQLAlchemy(flaskApp)
migrate = Migrate(flaskApp, db)

from app import routes, model, gameplay