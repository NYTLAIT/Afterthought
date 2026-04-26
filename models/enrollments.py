from datetime import datetime, timezone
from extensions import db

class Enrollment(db.Model):
    __tablename__ = 'enrollments'

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'), primary_key=True)

    joined_at = db.Column(db.DateTime(timezone=True), default=datetime.now(timezone.utc), nullable=False)
    left_at = db.Column(db.DateTime)