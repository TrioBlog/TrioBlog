from models.db import db
from datetime import datetime

from models.user import User


class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(100), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           nullable=False, onupdate=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    user_name = db.Column(db.String, nullable=False)

    # user = db.relationship('User', backref=db.backref('users', lazy=True))
    # post = db.relationship('Post', backref=db.backref('posts', lazy=True))

    def __init__(self, comment, user_id, post_id):
        self.comment = comment
        self.user_id = user_id
        self.user_name = User.find_by_id(user_id).json()['user_name']
        self.post_id = post_id

    def json(self):
        return {'id': self.id, "comment": self.comment, 'created_at': self.created_at,
                'updated_at': self.updated_at, 'user_id': self.user_id, 'post_id': self.post_id}

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
        comment = Comment.query.filter_by(id=comment_id).first()
        return comment

    @classmethod
    def find_by_user_id(cls, user_id):
        comments = Comment.query.filter_by(user_id=user_id).all()
        return [comment.json() for comment in comments]

    def find_by_post_id(cls, post_id):
        comments = Comment.query.filter_by(post_id=post_id).all()
        return [comment.json() for comment in comments]
