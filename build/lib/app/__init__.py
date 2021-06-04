from flask import Flask, session
from settings import Config
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from datetime import timedelta


def create_app():

   app = Flask(__name__, static_folder="static")
   app.config.from_object(Config)      
   return app

app = create_app()

db = MongoEngine(app)

login = LoginManager(app)
login.login_view = 'login'

from app import routes

#Session timeout control
@app.before_request
def before_request():
   session.permanent = True
   app.permanent_session_lifetime = timedelta(minutes=30)


   
