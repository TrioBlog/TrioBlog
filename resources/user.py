from uuid import UUID
from middleware import read_token, strip_token
from models.user import User
from models.db import db
from flask_restful import Resource
from flask import request
from sqlalchemy.orm import joinedload


class UsersDetail(Resource):
    def get(self, user_id):
        data = request.get_json()
        token = strip_token(data)
        if read_token(token)['data']:
            user_id = UUID(user_id)
            user = User.find_by_id(user_id)
            return user.json()
        else:
            return read_token(token)['payload']

    def patch(self, user_id):
        token = strip_token(request)
        if read_token(token)['data']:
            data = request.get_json()
            user_id = UUID(user_id)
            user = User.find_by_id(user_id)
            for key in data.keys():
                setattr(user, key, data[key])
            db.session.commit()
            return user.json()
        else:
            return read_token(token)['payload']

    def delete(self, user_id):
        token = strip_token(request)
        if read_token(token)['data']:
            user_id = UUID(user_id)
            user = User.find_by_id(user_id)
            if not user:
                return {'msg': 'User Not found'}, 404
            copy = {}
            for key in user.json().keys():
                copy[key] = user.json()[key]
            db.session.delete(user)
            db.session.commit()
            return {'msg': 'User Deletion Successful', 'payload': copy}
        else:
            read_token(token)['payload']


class AllUsers(Resource):
    def get(self):
        token = strip_token(request)
        if read_token(token)['data']:
            users = User.find_all()
            return users
        else:
            return read_token(token)['payload']
