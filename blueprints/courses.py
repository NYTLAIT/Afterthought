from flask import Blueprint, redirect, render_template, url_for, flash, request
from flask_login import login_required, current_user
from datetime import datetime, timezone, date

from extensions import db
from models.course import Course
from models.session import Session

def parse_date(value):
    return date.fromisoformat(value) if value else None

courses = Blueprint('courses', __name__, url_prefix='/courses')

@courses.route('/new', methods=['GET', 'POST'])
@login_required
def new():
    context = request.args.get('context', 'dashboard')

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')

        if Course.query.filter_by(user_id=current_user.id, title=title).first():
            flash('Title taken.', 'error')
            return redirect(url_for('courses.new', context=context))

        course = Course(
            user_id=current_user.id,
            title=title,
            description=description,
            start_date=parse_date(request.form.get('start-date')),
            end_date=parse_date(request.form.get('end-date')),
        )
        db.session.add(course)
        db.session.commit()

        flash('Course successfully created.', 'success')
        return redirect(url_for('courses.show_one', course_id=course.id, context=context))

    return render_template('courses/new.html', context=context)


@courses.route('/')
@login_required
def show_all():
    courses = current_user.courses
    return render_template('courses/courses.html', courses=courses)


@courses.route('/<int:course_id>')
@login_required
def show_one(course_id):
    context = request.args.get('context', 'dashboard')
    course = Course.query.get_or_404(course_id)

    if course.user_id != current_user.id:
        flash('Unauthorized.', 'error')
        if context == 'courses':
            return redirect(url_for('courses.show_all'))
        return redirect(url_for('dashboard.index'))

    course.last_viewed = datetime.now(timezone.utc)
    db.session.commit()

    sessions = Session.query.filter_by(course_id=course.id).order_by(Session.created_at.desc()).all()
    return render_template('courses/course.html', course=course, sessions=sessions, context=context)


@courses.route('/<int:course_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(course_id):
    context = request.args.get('context', 'dashboard')
    course = Course.query.get_or_404(course_id)

    if course.user_id != current_user.id:
        flash('Unauthorized.', 'error')
        if context == 'courses':
            return redirect(url_for('courses.show_all'))
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        new_title = request.form.get('title')
        existing = Course.query.filter_by(user_id=current_user.id, title=new_title).first()

        if existing and existing.id != course.id:
            flash('Title taken.', 'error')
            return redirect(url_for('courses.edit', course_id=course_id, context=context))

        course.title = new_title
        course.description = request.form.get('description')
        course.start_date = parse_date(request.form.get('start-date'))
        course.end_date = parse_date(request.form.get('end-date'))
        db.session.commit()

        flash('Course updated.', 'success')
        return redirect(url_for('courses.show_one', course_id=course.id, context=context))

    return render_template('courses/edit.html', course=course, context=context)


@courses.route('/<int:course_id>/delete', methods=['POST'])
@login_required
def delete(course_id):
    context = request.form.get('context', 'dashboard')
    course = Course.query.get_or_404(course_id)

    if course.user_id != current_user.id:
        flash('Unauthorized.', 'error')
        if context == 'courses':
            return redirect(url_for('courses.show_all'))
        return redirect(url_for('dashboard.index'))

    db.session.delete(course)
    db.session.commit()

    flash('Course deleted.', 'success')
    if context == 'courses':
        return redirect(url_for('courses.show_all'))
    return redirect(url_for('dashboard.index'))