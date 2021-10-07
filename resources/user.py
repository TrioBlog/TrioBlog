from models.user import User
from models.db import db
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload


class UsersDetail(Resource):
    def get(self, user_id):
        user = User.find_by_id(user_id)
        return user.json()

    def post(self):
        data = request.get_json()
        params = {}
        for key in data.keys():
            params[key] = data[key]
        user = User(**params)
        user.create()
        return user.json(), 201

    def patch(self, user_id):
        data = request.get_json()
        user = User.find_by_id(user_id)
        for key in data.keys():
            user[key] = data[key]
        db.session.commit()
        return user.json()

    def delete(self, user_id):
        user = User.find_by_id(user_id)
        if not user:
            return {'msg': 'User Not found'}, 404
        copy = {}
        for key in user.json().keys():
            copy[key] = user.json()[key]
        db.session.delete(user)
        db.session.commit()
        return {'msg': 'User Deletion Successful', 'payload': copy}


class AllUsers(Resource):
    def get(self):
        users = User.find_all()
        return users
