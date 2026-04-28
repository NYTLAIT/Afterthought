## Paths and Actions ##

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

- /courses/new
GET: Show form to create a new course
POST: Create a new course

- /courses/:course_id
GET: Retrieve and display a specific course with all sessions

- /courses/:course_id/edit
GET: Show form to edit a course
PATCH: Update an existing course (e.g., title, description)
DELETE: Delete a course and all its associated sessions

### Sessions ###
- /courses/:course_id/sessions/new
GET: Show form to create a new session recap
POST:  Create a new session recap for a specific course

- /courses/:course_id/sessions/:session_id
GET: Retrieve and display a specific session recap

- /courses/:course_id/sessions/:session_id/edit
GET: Show form to edit a session
PATCH: Update a session recap (edit reflection, notes, etc.)
DELETE: Delete a session recap