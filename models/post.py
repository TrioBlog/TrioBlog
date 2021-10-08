from models.db import db
from datetime import datetime
from models.user import User
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(500))
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           nullable=False, onupdate=datetime.now)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'users.id'), nullable=False)
    user_name = db.Column(db.String(255), nullable=False)

    user = db.relationship('User', backref=db.backref('post_user', lazy=True))
    comment = db.relationship(
        "Comment", cascade='all', backref=db.backref('post_comments', lazy=True))

    def __init__(self, title, body, user_id):
        self.title = title
        self.body = body
        self.user_id = user_id
        self.user_name = User.find_by_id(user_id).json()['user_name']

    def json(self):
        return {
            'id': str(self.id),
            'title': self.title,
            'body': self.body,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
            'user_id': str(self.user_id),
            'user_name': self.user_name
        }

    def create(self):
        db.session.add(self)
        db.session.commit()
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
