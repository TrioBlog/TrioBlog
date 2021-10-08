from uuid import UUID
from models.comment import Comment
from models.db import db
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload
from middleware import read_token, strip_token


class UserComments(Resource):
    def get(self, user_id):
        token = strip_token(request)
        if read_token(token)['data']:
            user_id = UUID(user_id)
            comments = Comment.find_by_user_id(user_id)
            return comments
        else:
            return read_token(token)['payload']


class Comments(Resource):
    def post(self):
        token = strip_token(request)
        if read_token(token)['data']:
            data = request.get_json()
            params = {}
            for key in data.keys():
                params[key] = data[key]
            comment = Comment(**params)
            comment.create()
            return comment.json(), 201
        else:
            return read_token(token)['payload']


class CommentId(Resource):
    def patch(self, comment_id):
        token = strip_token(request)
        if read_token(token)['data']:
            data = request.get_json()
            comment_id = UUID(comment_id)
            comment = Comment.find_by_id(comment_id)
            for key in data.keys():
                setattr(comment, key, data[key])
            db.session.commit()
            return comment.json()
        else:
            return read_token(token)['payload']

    def delete(self, comment_id):
        token = strip_token(request)
        if read_token(token)['data']:
            comment_id = UUID(comment_id)
            comment = Comment.find_by_id(comment_id)
            if not comment:
                return {'msg': 'Comment Not found'}, 404
            copy = {}
            for key in comment.json().keys():
                copy[key] = comment.json()[key]
            db.session.delete(comment)
            db.session.commit()
            return {'msg': 'Comment Deletion Successful', 'payload': copy}
        else:
            return read_token(token)['payload']


class PostComments(Resource):
    def get(self, post_id):
        token = strip_token(request)
        if read_token(token)['data']:
            post_id = UUID(post_id)
            comments = Comment.find_by_post_id(post_id)
            return comments
        else:
            return read_token(token)['payload']
