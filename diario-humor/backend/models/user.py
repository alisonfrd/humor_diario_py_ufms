from datetime import datetime
from extensions import db  # agora importa do novo arquivo

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    diary_entries = db.relationship('DiaryEntry', backref='user', lazy=True)
