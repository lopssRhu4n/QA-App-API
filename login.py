from flask import Blueprint, request, jsonify
from model import database, authentication

bp = Blueprint("login", __name__, url_prefix="/login")
db = database(path="db/users.json")
auth = authentication()



@bp.route("/", methods=['POST'])
def LoginUser():
    credentials = request.get_json()
    users = db.getData()
    return auth.validateLogin(credentials,users)
  
def configure(app):
    app.register_blueprint(bp)