from flask import Blueprint, jsonify, request
import json
from model import db_users

bp = Blueprint("users", __name__, url_prefix="/users")
db = db_users()

users = db.getDb()
print(users)


@bp.route('/',methods=['GET'])
def getUsers():
    return jsonify(users) 

@bp.route('/<int:id>', methods=['GET'])
def getUsersByID(id):
    for user in users:
        if user.get('id') == id:
            return jsonify(user)

@bp.route('/<int:id>', methods=['PUT'])
def editUser(id):
    global users
    new_user = request.get_json()
    for  index, user in enumerate(users):
        if user.get('id') == id:
            users[index].update(new_user)
            users = db.setDb(users)
            return jsonify(users[index])

@bp.route('/', methods=['POST'])
def createNewUser():
    global users
    new_user = request.get_json()
    for user in users:
        if new_user.get("username") == user.get("username"):
            return {"msg": "Username already used", "status": "error"} 
        elif new_user.get("email") == user.get("email"):
            return {"msg": "Email already used", "status": "error"}
        else:
            users.append(new_user)
            users = db.setDb(users)
    
            return jsonify(new_user)

@bp.route('/<int:id>', methods=['DELETE'])
def deleteUser(id):
    global users
    for index,user in enumerate(users):
        if user.get('id') == id:
            del users[index]
    users = db.setDb(users)
    
    return jsonify(users)

def configure(app):
    app.register_blueprint(bp)