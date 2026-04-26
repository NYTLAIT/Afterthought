from datetime import datetime, timezone
from flask_login import UserMixin

from extensions import db, bcrypt

class User(db.Model, UserMixin):
    '''
    Represent a registered user in the application.

    Attributes:
        id:            Auto-incremented primary key.
        courses:       Related Course records (deleted with the user).
        sessions:      Related Session records (deleted with the user).
        username:      Unique display name (max 20 characters).
        email:         Unique email address (max 120 characters).
        password_hash: Bcrypt-hashed password.
        first_name:    User's first name (max 40 characters).
        last_name:     User's last name (max 40 characters).
        dob:           Date of birth.
        created_at:    Timestamp of when the account was created.
        updated_at:    Timestamp of the most recent update to record.
    '''

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)

    courses = db.relationship('Course', backref='user', cascade='all, delete-orphan')
    sessions = db.relationship('Session', backref='user', cascade='all, delete-orphan')

    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    first_name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(40), nullable=False)
    dob = db.Column(db.Date, nullable=False)

    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), index=True)
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), onupdate=datetime.now)

    def set_password(self, password):
        '''
        Hash and set password
        Args:
            password: The plaintext password to hash.
        '''
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        '''
        Verify user by checking if given password matches the hash
        
        Args:
            password: The plaintext password to verify.
        Returns:
            True if the password matches the hash, False otherwise.
        '''
        return bcrypt.check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"<User {self.username}>" 

