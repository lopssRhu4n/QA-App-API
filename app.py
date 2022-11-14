from flask_cors import CORS, cross_origin
from flask import Flask
import users, posts, login


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    users.configure(app)
    posts.configure(app)
    login.configure(app)
     
    return app
