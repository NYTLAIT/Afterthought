from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from app.config import Config
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

###########################
# Authentication
###########################

# TODO: Add authentication setup code here!
'''
create login manager and initialize in app
tells where to find login route: in ... blueprint and called login

figure out what line 24 does later
'''
login_manager = LoginManager()
login_manager.login_view = '.login' #TODO: finish this, make blueprint
login_manager.init_app(app)

'''
tells login manager how to load user with the certain id
'''
from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get

'''
initializing bycrypt to hash
'''
bcrypt = Bcrypt(app)


