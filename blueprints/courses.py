from flask import Blueprint, redirect, render_template, url_for, flash, request
from flask_login import login_required, current_user

from extensions import db
from models.course import Course
from models.session import Session

courses = Blueprint('courses', __name__, url_prefix='/courses')

@courses.route('/')
@login_required
def show_all():
    if request.method == 'POST':

        user_id = current_user.id
        title = request.form.get('title')
        description = request.form.get('description')

        start_date = request.form.get('start-date')
        end_date = request.form.get('end-date')

        course = Course(
            user_id=user_id,
            title=title,
            description=description,
            start_date=start_date,
            end_date=end_date
        )

        db.session.add(course)
        db.session.commit()

        flash('Course successfully created.', 'success')
        return redirect(url_for('courses.courses'))

    courses = current_user.courses
    context = request.args.get('context')

    if context == 'courses':
        return render_template('courses.html', courses=courses)
    
    return redirect(url_for('dashboard.dashbaord'))


@courses.route('/<int:course_id>')
@login_required
def show_one(course_id):

    course = Course.query.get(course_id)
    sessions = 

    return render_template('courses/show.html', course=course, sessions=sessions)


@courses.route('/<int:course_id>/edit', methods=['GET', 'POST'])
@login_required
def edit(course_id):

    course = Course.query.get(course_id)

    if course.user_id != current_user.id:
        flash("Unauthorized.", 'error')
        return redirect(url_for('courses.index'))

    if request.method == 'POST':
        course.title = request.form.get('title')
        course.description = request.form.get('description')

        db.session.commit()

        flash('Course updated.', 'success')
        return redirect(url_for('courses.show', course_id=course.id))

    return render_template('courses/edit.html', course=course)


@courses.route('/courses/new', methods=['GET'])
@login_required
def create():
    return render_template('courses/new.html')


