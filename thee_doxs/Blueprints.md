## Blueprints ##

### user.py ###
IMPORTS
- UserMixin
login status
session handling
get_id()

ATTRIBUTES
- id: for other models
auto generated unique number
primary key

- username: display and login
must be unique
max 20 char

- email: login prolly
unique

- password_hash: for authenticating
store encrypted passwords

Information not really needed:
- first_name
- last_name
- dob

Datetime:
- created_at: when user was created
datetime
- updated_at: last update day
datetime

DB LINGO:
default -> fire once when row is first inserted (pass as callable like onupdate)
onupdate -> fire everytime row is updated (everytime db.session.commit() is called)
unique -> prevents duplicates, data rule
index -> speeds up searches, for performance

METHODS:
- set_password(self, password):
hashes and set the password
- check_password(self, password):
check if given password matches the hash in the database
- __repr__(self):
string representation of user

NOTES:
- Class represent the whole table so variables dont have self. Only use self in methods to refer to specific instance/row. Is just SQLAlchemy magic.
- UserMixin has to be there for later use
- Primary Key also creates index along with index and unique
- Index used for what are frequently searched/filtered often, login lookups, foreign keys. It speeds up searches but slows down inserts/updates, very slightly but just leave it unless need for cleanliness. Dont be needing all that.

### course.py ###
ATTRIBUTES:
- id: for other models
auto generated unique number
primary key

- user_id: foreign key of user that created it
connects owner
not nullable
index true because constant filter

- sessions: establish one to many relationships with courses

- name: name of course
required
- description: description of course
nullable

- start_date: when course starts
datetime
nullable
index
- end_date: when course ends
datetime
nullableå

Datetime:
- created_at: when course was created
datetime
- updated_at: last update day
datetime

DB LINGO:
foreignkey -> database rule that links two tables together, specifically: the value in user_id must match an existing id in the users table.
relationship() -> allows accessing objects directly (relationship ('Child, backref='parent', ...))
backref -> creates two way shortcut so user.courses works
cascade -> controls what happens when parent is deleted (all, deete-orphan, all sessions are deleted)

NOTES:
- Foreign Keys are database level and stores real values (ensures valid references, enforces strctures, required for joins) while Relationship is convenience layer
- Without relationship: course.user_id is just an integer and have to do User.query.get(course.user_id), with relationship: course.user returns full user object
-Child table: must have foreign key, Either side: may have relationship()
- One-to-Many relationships do not need a new model, Many-to-Many does - which we may implement if want users to share courses; (association table)

### session.py ###


