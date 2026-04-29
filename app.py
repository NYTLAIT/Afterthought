from flask import Flask, redirect, url_for
from extensions import db, login_manager, bcrypt

from models.user import User

from blueprints.auth import auth
from blueprints.dashboard import dashboard
from blueprints.courses import courses

app = Flask(__name__)

# Config
app.config['SECRET_KEY'] = 'shhh_secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Extensions.py
db.init_app(app)
login_manager.init_app(app)
bcrypt.init_app(app)

# Login config
login_manager.login_view = 'auth.login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Load into dashboard (although redirect)
@app.route('/')
def home():
    return redirect(url_for('dashboard.index'))

# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(courses)
app.register_blueprint(dashboard)

# Create tables
with app.app_context():
    db.create_all()
    print("Database is up.")

if __name__ == '__main__':
    app.run(debug=True, port=5000)