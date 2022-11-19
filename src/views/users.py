from flask import Blueprint, jsonify, request
from model.model import database


bp = Blueprint('users', __name__, url_prefix='/users')
db = database(path='src/db/users.json')


@bp.route('/', methods=['GET'])
def getUsers():
    return jsonify(db.getData())


@bp.route('/<int:user_id>', methods=['GET'])
def getUsersByID(user_id):
    return jsonify(db.getItemByID(user_id))


@bp.route('/<int:user_id>', methods=['PUT'])
def editUser(user_id):
    new_user = request.get_json()
    return db.editItem(new_user, user_id)


@bp.route('/', methods=['POST'])
def createNewUser():
    new_user = request.get_json()
    return db.createNewItem(new_user)


@bp.route('/<int:user_id>', methods=['DELETE'])
def deleteUser(user_id):
    return db.DeleteItem(user_id)


def configure(app):
    app.register_blueprint(bp)
