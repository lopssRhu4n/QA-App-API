from flask import Blueprint, request, jsonify
import json
from flask_cors import CORS
from model import db_users

bp = Blueprint("login", __name__, url_prefix="/login")
db = db_users()

@bp.route("/", methods=['POST'])
def LoginUser():
    credentials = request.get_json()
    users = db.getDb()
    for user in users:
        if (user.get('email') == credentials['email']) & (user.get('password') == credentials['password']):
            return user.get('jwt')

@bp.route("/", methods=['GET'])
def Teste():
    return 'Teste'    
    
def configure(app):
    app.register_blueprint(bp)