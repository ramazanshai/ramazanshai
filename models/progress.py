from app import db
from datetime import datetime

class Progress(db.Model):
    __tablename__ = 'progress'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    step_id = db.Column(db.Integer, db.ForeignKey('steps.id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'), nullable=False)
    
    is_completed = db.Column(db.Boolean, default=False)
    xp_earned = db.Column(db.Integer, default=0)
    attempts = db.Column(db.Integer, default=0)
    code_submitted = db.Column(db.Text)
    quiz_answer = db.Column(db.Integer)
    
    completed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    __table_args__ = (db.UniqueConstraint('user_id', 'step_id', name='unique_user_step'),)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'step_id': self.step_id,
            'lesson_id': self.lesson_id,
            'is_completed': self.is_completed,
            'xp_earned': self.xp_earned,
            'attempts': self.attempts,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None,
            'created_at': self.created_at.isoformat()
        }