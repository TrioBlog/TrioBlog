from models.comment import Comment
from models.db import db
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload


class UserComments(Resource):
    def get(self, user_id):
        comments = Comment.find_by_user_id(user_id)
        return comments

    def post(self):
        data = request.get_json()
        params = {}
        for key in data.keys():
            params[key] = data[key]
        comment = Comment(**params)
        comment.create()
        return comment.json(), 201

    def patch(self, comment_id):
        data = request.get_json()
        comment = Comment.find_by_id(comment_id)
        for key in data.keys():
            comment[key] = data[key]
        db.session.commit()
        return comment.json()

    def delete(self, comment_id):
        comment = Comment.find_by_id(comment_id)
        if not comment:
            return {"msg": "Not found"}, 404
        copy = {}
        for key in comment.keys():
            copy['%s' % key] = comment[key]
        db.session.delete(comment)
        db.session.commit()
        return {"msg": "Task Deleted", "payload": copy}


class PostComments(Resource):
    def get(self, post_id):
        comments = Comment.find_by_post_id(post_id)
        return comments
