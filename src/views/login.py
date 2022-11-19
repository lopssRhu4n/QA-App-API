from flask import Blueprint, request
from model.model import authentication, database

bp = Blueprint('login', __name__, url_prefix='/login')
db = database(path='src/db/users.json')
auth = authentication()


@bp.route('/', methods=['POST'])
def LoginUser():
    credentials = request.get_json()
    users = db.getData()
    return auth.validateLogin(credentials, users)


def configure(app):
    app.register_blueprint(bp)
