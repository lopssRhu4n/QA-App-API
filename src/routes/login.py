from flask import Blueprint, request, make_response, jsonify
from model.model import Authentication, Database

bp = Blueprint('login', __name__, url_prefix='/login')
db = Database(path='src/db/users.json')
auth = Authentication()


@bp.route('/', methods=['POST'])
def LoginUser():
    credentials = request.get_json()
    users = db.getData()
    res = auth.validateLogin(credentials, users)
    if res.get('status') == 'success':
        return jsonify(res)
    else:
        return make_response(jsonify(res), 401)


def configure(app):
    app.register_blueprint(bp)
