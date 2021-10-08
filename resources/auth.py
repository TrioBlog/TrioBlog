from flask_restful import Resource
from flask import request
from models.user import User
from middleware import create_token, gen_password, strip_token, read_token, compare_password


class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.find_by_user_name(data["user_name"])
        if compare_password(data["password"], user.json()["password_digest"]):
            token = create_token(
                {"id": str(user.json()["id"]), "user_name": str(user.json()["user_name"])})
            return token, 200

    def get(self):
        data = request.get_json()
        if not read_token(data["token"])['data']:
            return {"message": "unauthorized"}, 404
        return read_token(data["token"]), 200


class Register(Resource):
    def post(self):
        data = request.get_json()
        print(data)
        params = {
            "user_name": data["user_name"],
            "password_digest": gen_password(data["password"])
        }
        user = User(**params)
        user.create()
        return user.json(), 201


class StripAndVerifyToken(Resource):
    def get(self):
        data = request.get_json()
        token = strip_token(data)
        read_token(token)

    def post(self):
        data = request.get_json()
        token = strip_token(data)
        read_token(token)

    def patch(self):
        data = request.get_json()
        token = strip_token(data)
        read_token(token)

    def delete(self):
        data = request.get_json()
        token = strip_token(data)
        read_token(token)
