from flask import Blueprint, jsonify, request
import json

bp = Blueprint("users", __name__, url_prefix="/users")

with open("db/users.json", encoding='utf-8') as file:
    users = json.load(file)
    print(users)


def saveJson(users):
    json_users = json.dumps(users)
    with open('db/users.json','w') as file:
        file.write(json_users)

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
    new_user = request.get_json()
    for  index, user in enumerate(users):
        if user.get('id') == id:
            users[index].update(new_user)
            return jsonify(users[index])

@bp.route('/', methods=['POST'])
def createNewUser(users):
    user = request.get_json()
    users.append(user)
    saveJson(users)
    
    return jsonify(users)

@bp.route('/', methods=['DELETE'])
def deleteUser(id):
    for index,user in enumerate(users):
        if user.get('id') == id:
            del users[index]
    saveJson(users)
    
    return jsonify(users)

def configure(app):
    app.register_blueprint(bp)