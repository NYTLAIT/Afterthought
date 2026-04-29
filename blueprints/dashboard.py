from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.course import Course
from models.session import Session

dashboard = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard.route('/')
@login_required
def index():
    # Most recently viewed courses
    recent_courses = (
        Course.query
        .filter_by(user_id=current_user.id)
        .order_by(Course.last_viewed.desc())
        .limit(6)
        .all()
    )

    # # Most recent sessions
    # recent_sessions = (
    #     Session.query
    #     .filter_by(user_id=current_user.id)
    #     .order_by(Session.created_at.desc())
    #     .limit(12)
    #     .all()
    # )

    return render_template(
        'dashboard.html',
        recent_courses=recent_courses,
        # recent_sessions=recent_sessions
    )