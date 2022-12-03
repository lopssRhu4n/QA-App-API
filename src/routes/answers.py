from flask import Blueprint, jsonify, request
from model.model import Database

bp = Blueprint('answers', __name__, url_prefix='/answers')
db = Database(path='src/db/answers.json')


@bp.route('/', methods=['GET'])
def get_answers():
    return jsonify(db.getData())


@bp.route('/<author>', methods=['GET'])
def get_answers_by_author(author):
    return jsonify(db.getItemByAuthor(author))


@bp.route('/<int:answer_id>', methods=['PUT'])
def edit_answer(answer_id):
    edited_answer = request.get_json()
    return jsonify(db.editItem(edited_answer, answer_id))


@bp.route('/', methods=['answer'])
def create_new_answer():
    answer = request.get_json()
    return jsonify(db.createNewPost(answer))


# @bp.route('/<int:answer_id>/answer', methods=['answer'])
# def create_new_answer_answer(id):
    

@bp.route('/<int:answer_id>', methods=['DELETE'])
def delete_answer(answer_id):
    return jsonify(db.DeleteItem(answer_id))


def configure(app):
    app.register_blueprint(bp)
