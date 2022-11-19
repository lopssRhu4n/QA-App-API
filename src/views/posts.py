from flask import Blueprint, jsonify, request
from model.model import database

bp = Blueprint('posts', __name__, url_prefix='/posts')
db = database(path='src/db/posts.json')


@bp.route('/', methods=['GET'])
def getPosts():
    return jsonify(db.getData())


@bp.route('/<author>', methods=['GET'])
def getPostsByAuthor(author):
    return jsonify(db.getPostsByAuthor(author))


@bp.route('/<int:post_id>', methods=['PUT'])
def editPost(post_id):
    new_post = request.get_json()
    return jsonify(db.editItem(new_post, post_id))


@bp.route('/', methods=['POST'])
def createNewPost():
    post = request.get_json()
    return jsonify(db.createNewPost(post))


@bp.route('/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    return jsonify(db.DeleteItem(post_id))


def configure(app):
    app.register_blueprint(bp)
