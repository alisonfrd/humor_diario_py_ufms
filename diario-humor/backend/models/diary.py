from datetime import datetime
from extensions import db

class DiaryEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    mood = db.Column(db.String(20), nullable=False)
    entry_date = db.Column(db.Date, nullable=False)  
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
