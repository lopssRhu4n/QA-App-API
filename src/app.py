from flask import Flask
from flask_cors import CORS
from routes import login
from routes import posts
from routes import users
from routes import answers


def create_app():
    app = Flask(__name__)
    CORS(app, resources={r'/*': {'origins': '*'}})

    users.configure(app)
    posts.configure(app)
    login.configure(app)
    answers.configure(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return 'Not found 404 :('
    
    return app
