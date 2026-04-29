from flask import Blueprint, redirect, render_template, url_for, flash, request
from flask_login import login_required, current_user
from datetime import datetime, timezone
from extensions import db
from models.session import Session
from models.course import Course

sessions = Blueprint('sessions', __name__, url_prefix='/sessions')

@sessions.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    course_id = request.args.get('course_id', type=int)
    course = Course.query.get_or_404(course_id)

    if course.user_id != current_user.id:
        flash('Unauthorized.', 'error')
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        session = Session(
            user_id=current_user.id,
            course_id=course_id,
            title=request.form.get('title'),
            summary=request.form.get('summary'),
            notes=request.form.get('notes'),
            reflection=request.form.get('reflection'),
            questions=request.form.get('questions'),
        )
        db.session.add(session)
        db.session.commit()
        flash('Session created.', 'success')
        return redirect(url_for('sessions.show_one', session_id=session.id))

    return render_template('sessions/new.html', course=course)


@sessions.route('/<int:session_id>')
@login_required
def show_one(session_id):
    session = Session.query.get_or_404(session_id)

    if session.user_id != current_user.id:
        flash('Unauthorized.', 'error')
        return redirect(url_for('dashboard.index'))

    session.last_viewed = datetime.now(timezone.utc)
    db.session.commit()

    return render_template('sessions/session.html', session=session)


@sessions.route('/<int:session_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(session_id):
    session = Session.query.get_or_404(session_id)

    if session.user_id != current_user.id:
        flash('Unauthorized.', 'error')
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        session.title = request.form.get('title')
        session.summary = request.form.get('summary')
        session.notes = request.form.get('notes')
        session.reflection = request.form.get('reflection')
        session.questions = request.form.get('questions')
        db.session.commit()
        flash('Session updated.', 'success')
        return redirect(url_for('sessions.show_one', session_id=session.id))

    return render_template('sessions/edit.html', session=session)


@sessions.route('/<int:session_id>/delete', methods=['POST'])
@login_required
def delete(session_id):
    session = Session.query.get_or_404(session_id)

    if session.user_id != current_user.id:
        flash('Unauthorized.', 'error')
        return redirect(url_for('dashboard.index'))

    course_id = session.course_id
    db.session.delete(session)
    db.session.commit()
    flash('Session deleted.', 'success')
    return redirect(url_for('courses.show_one', course_id=course_id))