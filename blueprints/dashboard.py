from flask import Blueprint, redirect, render_template, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from datetime import date