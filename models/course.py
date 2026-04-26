from datetime import datetime, timezone

from extensions import db

class Course(db.Model):
    '''
    Represents a course created by a user.

    Attributes:
        id:          Auto-incremented primary key.
        user_id:     Foreign key referencing the owning User.
        sessions:    Related Session records (deleted with the course).
        title:        Name of the course (max 120 characters).
        description: Optional longer description of the course.
        start_date:  When the course begins.
        end_date:    When the course ends.
        last_viewed: Timestamp of when user last viewed course
        created_at:  Timestamp of when this record was created.
        updated_at:  Timestamp of the most recent update to this record.
    '''

    __tablename__ = 'courses'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, index=True)

    sessions = db.relationship('Session', backref='course', cascade='all, delete-orphan')

    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text)

    start_date = db.Column(db.Date, index=True)
    end_date = db.Column(db.Date)

    last_viewed = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), index=True)
    created_at = db.Column(db.DateTime(timezone=True), default=lambda:datetime.now(timezone.utc), index=True)
    updated_at = db.Column(db.DateTime(timezone=True), default=lambda:datetime.now(timezone.utc), onupdate=lambda:datetime.now(timezone.utc))


    def __repr__(self):
        return f"<Course {self.title}>" if self.title else f"<Course {self.id}>"