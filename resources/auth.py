from flask_restful import Resource
from flask import request
from models.user import User
from middleware import create_token, gen_password, strip_token, read_token, compare_password

class Login(Resource):
  def post(self):
    data = request.get_json()
    user = User.find_by_user_name(data["user_name"])
    if compare_password(data["password"], user.json()["password_digest"]):
      user_id = str(user.json()["id"])
      print({"id": "{val}".format(val=str(user.json()["id"])), "user_name": "{val}".format(val=str(user.json()["user_name"])) })
      token = create_token({"id": "{val}".format(val=str(user.json()["id"])), "user_name": "{val}".format(val=str(user.json()["user_name"])) })
      return token, 200

  def get(self):
    data = request.get_json()
    if read_token(data) == "Signature Invalid" or read_token(data) == "Token Invalid":
      return { "message": "unauthorized" }, 404

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
