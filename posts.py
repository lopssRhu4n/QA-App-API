from flask import Blueprint, request, jsonify
import json
from model import database

bp = Blueprint("posts", __name__, url_prefix="/posts")
db = database(path="db/posts.json")


 
@bp.route('/',methods=['GET'])
def getPosts():
    return jsonify(db.getData()) 

@bp.route('/<author>', methods=['GET'])
def getPostsByAuthor(author):
     return jsonify(db.getPostsByAuthor(author))
        
        
@bp.route('/<int:id>', methods=['PUT'])
def editPost(id):
    new_post = request.get_json()
    return jsonify(db.editItem(new_post, id))

@bp.route('/', methods=['POST'])
def createNewPost():
    global posts
    post = request.get_json()    
    return jsonify(db.createNewPost(post))

@bp.route('/<int:id>', methods=['DELETE'])
def deletePost(id):
    return jsonify(db.DeleteItem(id))

def configure(app):
    app.register_blueprint(bp)