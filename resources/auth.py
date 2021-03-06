from flask_restful import Resource
from flask import request
from models.user import User
from middleware import create_token, gen_password, strip_token, read_token, compare_password


class Login(Resource):
    def post(self):
        data = request.get_json()
        user = User.find_by_user_name(data["user_name"])
        if user:
            if compare_password(data["password"], user.json()["password_digest"]):
                token = create_token(
                    {"id": str(user.id), "user_name": user.user_name})
                return token, 200
        else:
            return 'Unauthorized', 404

    def get(self):
        data = request.get_json()
        if not read_token(data["token"])['data']:
            return {"message": "unauthorized"}, 404
        return read_token(data["token"]), 200


class Register(Resource):
    def post(self):
        data = request.get_json()
        params = {
            "user_name": data["user_name"],
            "password_digest": gen_password(data["password"])
        }
        user = User(**params)
        user.create()
        print(user.json())
        return user.json(), 201
