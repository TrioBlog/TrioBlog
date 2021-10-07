from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from models.post import Post
from models.comment import Comment
from models.user import User
from resources.user import UsersDetail, AllUsers
from resources.comment import UserComments, PostComments
from resources.auth import Register, Login
from resources.post import Posts, UserPosts

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/trioblog_db"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

# auth
api.add_resource(Login, '/user/login')
api.add_resource(Register, '/user/register')
# User Routes
api.add_resource(UsersDetail, '/user')
api.add_resource(UsersDetail, '/user/<int:user_id>')
api.add_resource(AllUsers, '/users')
# Post Routes
api.add_resource(UserPosts, '/user/posts')
api.add_resource(Posts, '/posts')
api.add_resource(Posts, '/posts/<int:post_id>')
# Comment Routes
api.add_resource(PostComments, '/posts/comments/<int:post_id>')
api.add_resource(UserComments, '/user/comments')
api.add_resource(UserComments, '/user/comment/<int:comment_id>')
api.add_resource(UserComments, '/user/comments/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
