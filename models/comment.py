from models.db import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from models.user import User


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    body = db.Column(db.String(100), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow,
                           nullable=False, onupdate=datetime.utcnow)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'user.id'), nullable=False)
    post_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'post.id'), nullable=False)
    user_name = db.Column(db.String(255), nullable=False)

    user = db.relationship(
        'User', backref=db.backref('comments', lazy=True))
    post = db.relationship(
        'Post', backref=db.backref('comments', lazy=True))

    def __init__(self, body, user_id, post_id):
        self.body = body
        self.user_id = user_id
        self.user_name = User.find_by_id(user_id).json()['user_name']
        self.post_id = post_id

    def json(self):
        return {'id': str(self.id), "body": self.body, 'created_at': str(self.created_at),
                'updated_at': str(self.updated_at), 'user_id': str(self.user_id), 'post_id': str(self.post_id)}

    def create(self):
        db.session.add(self)
        db.session.commit()
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

    @classmethod
    def find_by_post_id(cls, post_id):
        comments = Comment.query.filter_by(post_id=post_id).all()
        return [comment.json() for comment in comments]
