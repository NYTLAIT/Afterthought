from datetime import datetime

from extensions import db

class Session(db.Model):
    '''
    Represents a single study or learning session tied to a course.

    Attributes:
        id:         Auto-incremented primary key.
        user_id:    Foreign key referencing the owning User.
        course_id:  Foreign key referencing the parent Course.
        title:      Optional short title for the session (max 120 characters).
        content:    Main body content of the session.
        reflection: User's reflection or notes on the session.
        questions:  Optional questions raised during the session.
        created_at: Timestamp of when this record was created.
        updated_at: Timestamp of the most recent update to this record.
    '''
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False, index=True)

    title = db.Column(db.String(120), index=True)
    content = db.Column(db.Text, nullable=False)
    reflection = db.Column(db.Text, nullable=False)
    questions = db.Column(db.Text)

    created_at = db.Column(db.DateTime, default=datetime.now, index=True)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def __repr__(self):
        return f"<Session {self.title}>" if self.title else f"<Session {self.id}>"