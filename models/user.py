from datetime import datetime
from models.db import db
from sqlalchemy.dialects.postgresql import UUID
import uuid


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_name = db.Column(db.String(255), nullable=False, unique=True)
    password_digest = db.Column(db.String(255), nullable=False)
    created_at = db.Column(
        db.DateTime, default=datetime.utcnow(), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(
    ), nullable=False, onupdate=datetime.now())

# Associations
    posts = db.relationship("Post", cascade='all',
                            backref=db.backref('posts', lazy=True))
    comments = db.relationship("Comment", cascade='all',
                               backref=db.backref('comments', lazy=True))

    def __init__(self, user_name, password_digest):
        self.user_name = user_name
        self.password_digest = password_digest

    def json(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "password_digest": self.password_digest,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at)
        }

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_all(cls):
        users = User.query.all()
        return [user.json() for user in users]

    @classmethod
    def find_by_id(cls, id):
        user = User.query.filter_by(id=id).first()
        return user

    @classmethod
    def find_by_user_name(cls, user_name):
      user = User.query.filter_by(user_name=user_name).first()
      return user