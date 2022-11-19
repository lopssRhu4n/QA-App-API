from flask import Flask
from flask_cors import CORS
import views.login as login
import views.posts as posts
import views.users as users


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r'/*': {'origins': '*'}})

    users.configure(app)
    posts.configure(app)
    login.configure(app)

    return app