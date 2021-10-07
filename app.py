from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from flask_migrate import Migrate
from models.db import db
from models import user, post, comment
from resources import comment, user, post
app = Flask(__name__)
CORS(app)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/trioblog_db"
app.config['SQLALCHEMY_ECHO'] = True

db.init_app(app)
migrate = Migrate(app, db)

# Comment Routes
api.add_resource(comment.PostComments, 'posts/comments/<int:post_id>')
api.add_resource(comment.UserComments, 'user/comments')
api.add_resource(comment.UserComments, 'user/comment/<int:comment_id>')
api.add_resource(comment.UserComments, 'user/comments/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)
