from flask import Flask
from extensions import db, login_manager, bcrypt

from models.user import User

from blueprints.auth import auth
from blueprints.courses import courses


app = Flask(__name__)

# Config
app.config['SECRET_KEY'] = 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Extensions.py
db.init_app(app)
login_manager.init_app(app)
bcrypt.init_app(app)

# Login config
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(courses)

if __name__ == '__main__':
    app.run(debug=True, port=5000)