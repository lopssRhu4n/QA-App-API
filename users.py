from flask import Blueprint, jsonify, request
import json
from model import database

bp = Blueprint("users", __name__, url_prefix="/users")
db = database(path='db/users.json')



@bp.route('/',methods=['GET'])
def getUsers():
    return jsonify(db.getData()) 

@bp.route('/<int:id>', methods=['GET'])
def getUsersByID(id):
    return jsonify(db.getItemByID(id))

@bp.route('/<int:id>', methods=['PUT'])
def editUser(id):
    new_user = request.get_json()
    return db.editItem(new_user, id)

@bp.route('/', methods=['POST'])
def createNewUser():
    new_user = request.get_json()
    return db.createNewItem(new_user)

@bp.route('/<int:id>', methods=['DELETE'])
def deleteUser(id):
     return db.DeleteItem(id) 

def configure(app):
    app.register_blueprint(bp)