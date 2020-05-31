from flask import Flask
from settings import Config
from flask_pymongo import PyMongo

#from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate


app = Flask(__name__, static_folder="static")
app.config.from_object(Config)
mongo = PyMongo(app)


from app import routes