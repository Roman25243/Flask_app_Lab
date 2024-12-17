from app import db
from sqlalchemy import Column, DateTime
from datetime import datetime
class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    posted = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True) 
    category = db.Column(db.String(50), nullable=True)
    author = db.Column(db.String(50), nullable=True)

def __repr__(self):
        return f"<Post(title={self.title})>" 