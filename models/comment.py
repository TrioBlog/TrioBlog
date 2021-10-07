from models.db import db
from datetime import datetime


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(100), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           nullable=False, onupdate=datetime.now)
    user_id = db.Column(db.Integer, nullable=False)

    user = db.Relationship('User', backref=db.backref('users', lazy=True))

    def __init__(self, title, body, user_id):
        self.title = title
        self.body = body
        self.user_id = user_id

    def json(self):
        return {'id': self.id, "comment": self.comment, 'created_at': self.created_at, 'updated_at': self.updated_at, 'user_id': self.user_id}

    def create(self):
        db.session.add(self)
        db.commit()
        return self

    @classmethod
    def find_all(cls):
        comments = Comment.query.all()
        return [comment.json() for comment in comments]

    @classmethod
    def find_by_id(cls, comment_id):
        post = Comment.query.filter_by(id=comment_id).first()
        return post

    @classmethod
    def find_by_user_id(cls, user_id):
        comments = Comment.query.filter_by(user_id=user_id).all()
        return [comment.json() for comment in comments]