## Paths and Actions: ##
### Authentication ###
- /login
GET: Show login form
POST: Authenticate user and log them in

- /signup
GET: Show registration form
POST: Create a new user account

- /logout
POST: Log the current user out

### User ###
- /dashboard
GET: Show most recently viewed sessions and active courses plus most recently accessed course

- /sessions
GET: Retrieve and display all sessions for the current user

### Courses ###
- /courses
GET: Retrieve and display all courses for the current user
POST: Create a new course

- /courses/new
GET: Show form to create a new course

- /courses/:course_id
GET: Retrieve and display a specific course
PATCH: Update an existing course (e.g., title, description)
DELETE: Delete a course and all its associated sessions

- /courses/:course_id/edit
GET: Show form to edit a course

### Sessions ###
- /courses/:course_id/sessions
POST:  Create a new session recap for a specific course

- /courses/:course_id/sessions/new
GET: Show form to create a new session recap

- /courses/:course_id/sessions/:session_id
GET: Retrieve and display a specific session recap
PATCH: Update a session recap (edit reflection, notes, etc.)
DELETE: Delete a session recap

- /courses/:course_id/sessions/:session_id/edit
GET: Show form to edit a session