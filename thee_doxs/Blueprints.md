## Blueprints ##

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


### auth.py ###
