from models.db import db
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(500))
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           nullable=False, onupdate=datetime.now)
    user_id = db.Column(db.Integer, nullable=False)

    # users = db.relationship('User', backref=db.backref('users', lazy=True))

    def __init__(self, title, body, user_id):
        self.title = title
        self.body = body
        self.user_id = user_id

    def json(self):
        return {'id': self.id, 'title': self.title, 'body': self.body, 'created_at': self.created_at,
                'updated_at': self.updated_at, 'user_id': self.user_id}

    def create(self):
        db.session.add(self)
        db.commit()
        return self

    @classmethod
    def find_all(cls):
        posts = Post.query.all()
        return [post.json() for post in posts]

    @classmethod
    def find_by_id(cls, post_id):
        post = Post.query.filter_by(id=post_id).first()
        return post

    @classmethod
    def find_by_user_id(cls, user_id):
        posts = Post.query.filter_by(user_id=user_id).all()
        return [post.json() for post in posts]
