## Blueprints ##

## OVERVIEW ##
### Overview Structure ###
- auth.py: login/signup/logout
- courses.py: course CRUD
- sessions.py: session CRUD
- dashboard.py: aggregated views

### Imports ###
ALL:
from flask import
- Blueprint: mini app inside main Flask that needs to be registered in App.py to be active (app.register_blueprint(name of blueprint) in main app file): variable = Blueprint('name of blueprint flask uses to reference routes', __name__)
    - variable: variable to hold the blueprint to reference later in app.register...
    - name of blueprint, flask uses for:
    referencing routes
    building urls with url_for (ex auth.login - blueprint name.function name)
    debugging
    - __name__ helps flask:
    tell where the blueprint is defined
    locate the templates, static files, and module context (actually dont understand this on too well)
- request: acess abd process data sent by a client to server
- redirect: send user to another route
- render_template: renders html
- url_for: generate url dynamically for a route (route function call, and can be used in jinja with href) 
- flash: popup messages (use get_flashed_messages() in jinja)

AUTH:
from flask_login import:
(easy handle if user is logged in or not)
    - login_user(user): logs in user (creates cookie session)
    - logout_user(): ends session
    - @login_required: protects outes so only logged in users can access them
    - current_user: represent logged in user

### Model Query ###
PARTS:
- filter_by(key=value) -> simple equality checks only
- filter(Model.col == value) -> complex expressions (range, LIKE, OR, etc.)

- .like() -> ex .like('da%')
    - case sensitive
    - da: specifies the prefix that must match exactly
    - % wildcard: represents zero, one, or multiple characters following 'da'
- .ilike() -> ex .ilike('%Da')
    - case insentive
    - Da: specifies the suffix that must match (da, DA, etc will match)
    - % wildcard: represents zero, one, or multiple characters preceding 'Da'

- order_by() -> sort by descending or ascending order
    - .desc(): Largest to smallest, Z-A, newest to oldest
        .order_by(Session.col.desc())
    - .acs(): Smallest to largest, A-Z, oldest to newest
        .order_by(Session.col.asc())

limit() -> ex .limit(6)
    - only give top 6

.first() -> one object or None
.all() -> list
.get(id) -> one object by PK

PATTERNS:
- Get one thing:
    - Model.query.get(primary_key) -> get one thing by primary key 
        User.query.get(current_user.id)
    - Model.query.filter_by(attribute=).first() -> first() returns one or None 
        User.query.filter_by(email="test@email.com").first()
- Get many things:
    - Model.query.all() -> returns list of all
        User.query.all()
- Filtered queries:
    - Model.query.filter_by(attribute=).all()
        User.query.filter_by(username="danica").all()
    - Model.query.filter(Model.attribute.like()).all()
        User.query.filter(User.username.like("da%")).all()

RELATIONSHIPS (specific to project):
Context: defined user.courses, course.sessions, session.course, etc:
- Able to do -> current_user.courses
- No more -> Course.query.filter_by(user_id=current_user.id).all()

### Overview Core Queries ###
Not Set in Stone, will erase note if ever updated
- AUTH
    - User.query.filter_by(username=...).first()
- DASHBOARD
    - current_user.courses
    - Session.query.filter_by(user_id=current_user.id).order_by(...).limit(...)
- COURSES
    - current_user.courses
    - Course.query.get(course_id)
- SESSIONS
    - course.sessions
    - Session.query.get(session_id)

## ACTUAL BLUEPRINTS ##
### auth.py ###
