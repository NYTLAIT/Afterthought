from datetime import datetime, timezone

from extensions import db

class Session(db.Model):
    '''
    Represents a single study or learning session tied to a course.

    Attributes:
        id:         Auto-incremented primary key.
        user_id:    Foreign key referencing the owning User.
        course_id:  Foreign key referencing the parent Course.
        title:      Optional short title for the session (max 120 characters).
        summary:    Main body content of the session, summary of session.
        notes:      Additional notes
        reflection: User's reflection or notes on the session.
        questions:  Optional questions raised during the session.
        last_viewed: Timestamp of when user last viewed session
        created_at: Timestamp of when this record was created.
        updated_at: Timestamp of the most recent update to this record.
    '''
    __tablename__ = 'sessions'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), nullable=False, index=True)

    title = db.Column(db.String(120), index=True)
    summary = db.Column(db.Text)
    notes = db.Column(db.Text)
    reflection = db.Column(db.Text)
    questions = db.Column(db.Text)

    last_viewed = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), index=True)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda:datetime.now(timezone.utc), index=True)
    updated_at = db.Column(db.DateTime(timezone=True), default=lambda:datetime.now(timezone.utc), onupdate=lambda:datetime.now(timezone.utc))

    def __repr__(self):
        return f"<Session {self.title}>" if self.title else f"<Session {self.id}>"