from flask import Blueprint, request, jsonify
import json

bp = Blueprint("login", __name__, url_prefix="/login")

with open("db/users.json", encoding='utf-8') as file:
    users = json.load(file)

@bp.route("/", methods=['GET'])
def LoginUser():
    credentials = request.args.to_dict()
    