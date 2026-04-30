## CONTEXT VALUES ##

### sessions ###
  Set when: navigating from the /sessions list page
  Used in:  sessions.show_one, sessions.edit, sessions.delete
  Back arrow goes to: sessions.show_all

### courses ###
  Set when: navigating from the /courses list page
  Used in:  courses.new, courses.show_one, courses.edit, courses.delete
  Back arrow goes to: courses.show_all

### course ###
  Set when: navigating from within a specific course page
  Used in:  sessions.new, sessions.show_one, sessions.edit, sessions.delete
  Back arrow goes to: courses.show_one (for that course)

### dashboard (default) ###
  Set when: navigating from the dashboard, or no context provided
  Used in:  all routes as the fallback
  Back arrow goes to: dashboard.index

## FLOW ##
- Dashboard
  -> courses.new?context=dashboard        -> on save -> courses.show_one?context=dashboard
  -> courses.show_one?context=dashboard   -> back arrow -> dashboard

- Courses list (/courses)
  -> courses.new?context=courses          -> on save -> courses.show_one?context=courses
  -> courses.show_one?context=courses     -> back arrow -> courses.show_all

- Course page
  -> sessions.new?context=course&course_id=X  -> on save -> courses.show_one
  -> sessions.show_one?context=course         -> back arrow -> courses.show_one
  -> sessions.edit?context=course             -> on save -> sessions.show_one?context=course
  -> sessions.delete (POST, context in body)  -> always  -> courses.show_one

## HOW DO ##
GET routes:  query param  -> ?context=courses
POST delete: hidden input -> <input type="hidden" name="context" value="{{ context }}">

### For sessions ###
  context == 'course'   -> courses.show_one
  context == 'sessions' -> sessions.show_all
  context == 'dashboard'-> dashboard.index (default)