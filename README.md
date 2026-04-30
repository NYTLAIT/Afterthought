# Afterthought
Afterthought is a web application designed to track courses and study sessions, with a focus on the benefits of recapping after learning.

## Overview

The application allows users to organize courses and log individual study sessions. It is structured like a cornell note margin entries with summaries and lasting questions. It also includes a notes section for additional notes and a reflections section to jot down feelings of the given content after. A dashboard highlights recent activity, supporting quick review and continuity in learning.

## Features

- Course management (create, edit, delete)
- Session tracking with structured fields (summary, notes, reflection, questions)
- Dashboard with recent courses and sessions
- User authentication and session management
- Clean, dark-themed UI with a modular CSS system

## Tech Stack

- Backend: Flask, Flask-SQLAlchemy
- Frontend: Jinja2, HTML, modular CSS (structure + theme separation)
- Database: SQLite
- Authentication: Flask-Login

## Highlights

- Blueprint-based Flask app with clean separation of concerns
- Context-aware navigation that preserves where you came from
- Ownership checks on routes
- Designed relational data models (cascade deletes across users, courses, and sessions)

## Running the Project

```bash id="h2o6qt"
git clone <repo-url>
cd afterthought
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask run
```

Open http://127.0.0.1:5000 in a browser.

## Future Improvements

- Cleaner CSS
- Search and filtering
----------------------------------------------------
- Tagging system for sessions
- Data insights (learning trends, activity patterns)
- Improved mobile responsiveness
