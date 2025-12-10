# TODO:import database and whatever not
import some.extension import db
from sqlalchemy.orm import
from flask_login import

# TODO: figure out relations to each other

##############
# USER
##############
class User(UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


##############
# COURSES
##############
class Course():


##############
# SESSIONS
##############
class Session():