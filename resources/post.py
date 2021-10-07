from models.post import Post
from models.db import db
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload


class Posts(Resource):
    def get(self):
        posts = Post.find_all()
        return posts

    def post(self):
        data = request.get_json()
        params = {}
        for key in data.keys():
            params[key] = data[key]
        post = Post(**params)
        post.create()
        return post.json(), 201

    def patch(self, post_id):
        data = request.get_json()
        post = Post.find_by_id(post_id)
        for key in data.keys():
            post[key] = data[key]
        db.session.commit()
        return post.json()

    def delete(self, post_id):
        post = Post.find_by_id(post_id)
        if not post:
            return {'msg': 'Post Not Found'}
        copy = {}
        for key in post.json().keys():
            copy[key] = post.json()[key]
        db.session.delete(post)
        db.session.commit()
        return {'msg': 'Post Deletion Successful', 'payload': copy}


class UserPosts(Resource):
    def get(self, user_id):
        posts = Post.find_by_user_id(user_id)
        return posts
