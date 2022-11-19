from flask import Flask
from flask_cors import CORS
from views import login
from views import posts
from views import users


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r'/*': {'origins': '*'}})

    users.configure(app)
    posts.configure(app)
    login.configure(app)

    return app
