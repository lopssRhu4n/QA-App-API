from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, request
import users, posts


def create_app():
    app = Flask(__name__)
    CORS(app)

    users.configure(app)
    posts.configure(app)
    
    return app
