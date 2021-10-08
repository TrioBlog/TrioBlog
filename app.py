from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from resources import user, auth, comment, post

app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/trioblog_db"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

# auth
api.add_resource(auth.Login, '/user/login')
api.add_resource(auth.Register, '/user/register')
# User Routes
api.add_resource(user.UsersDetail, '/user/<string:user_id>')
api.add_resource(user.AllUsers, '/users')
# Post Routes
api.add_resource(post.UserPosts, '/user/<string:<user_id>')
api.add_resource(post.PostId, '/posts/<string:post_id>')
api.add_resource(post.Post, '/posts')
# Comment Routes
api.add_resource(comment.PostComments, '/posts/comments/<string:post_id>')
api.add_resource(comment.UserComments, '/user/comments/<string:user_id>')
api.add_resource(comment.Comments, '/comments')
api.add_resource(comment.CommentId, '/comments/<string:comment_id>')

if __name__ == '__main__':
    app.run(debug=True)
