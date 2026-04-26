from flask import Blueprint, redirect, render_template, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime

from extensions import db
from models.user import User

auth = Blueprint('auth', __name__)

# SIGNUP
@auth.route('/signup', methods=['GET', 'POST'])
def signup():

    if current_user.is_authenticated:
        return redirect(url_for('dashboard.dashboard'))
    
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = datetime.strptime(request.form['dob'], '%Y-%m-%d').date()
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if existing user
        if User.query.filter_by(email=email).first():
            flash('User already exists. Please sign in.', 'error')
            return redirect(url_for('auth.login'))
        
        # Username already taken
        if User.query.filter_by(username=username).first():
            flash('Username already taken.', 'error')
            return redirect(url_for('auth.signup'))
        
        # Create User in User Model
        user = User(
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            username=username,
            email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash('Account successfully created.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('signup.html')
    
# LOGIN
@auth.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('dashboard.dashboard'))
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        
        # Password or user name does not match
        if not user or not user.check_password(password):
            flash('Invalid username or password.', 'error')
            return redirect(url_for('auth.login'))
        
        login_user(user)
        return redirect(url_for('dashboard.dashboard'))
    
    return render_template('login.html')
    
# LOGOUT
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You've been logged out.", 'success')
    return redirect(url_for('auth.login'))


