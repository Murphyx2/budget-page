from flask import Flask
from settings import Config
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate


app = Flask(__name__, static_folder="static")
app.config.from_object(Config)
db = MongoEngine(app)
login = LoginManager(app)

from app import routes