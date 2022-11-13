from flask import Blueprint, request, jsonify
import json
from model import db_posts

bp = Blueprint("posts", __name__, url_prefix="/posts")
db = db_posts()

posts = db.getDb()


def saveJson(posts):
    json_posts = json.dumps(posts)
    with open('db/posts.json','w') as file:
        file.write(json_posts)
 
 
@bp.route('/',methods=['GET'])
def getPosts():
    return jsonify(posts) 

@bp.route('/<author>', methods=['GET'])
def getPostsByID(author):
    matched = []
    for post in posts:
        if post.get('author') == author:
            matched.append(post)    
            
    return jsonify(matched)
        
        
@bp.route('/<int:id>', methods=['PUT'])
def editPost(id):
    global posts
    new_post = request.get_json()
    for  index, post in enumerate(posts):
        if post.get('id') == id:
            posts[index].update(new_post)
            posts = db.setDb(posts)
            return jsonify(posts[index])

@bp.route('/', methods=['POST'])
def createNewPost():
    global posts
    post = request.get_json()
    posts.append(post)
    posts = db.setDb(posts)
    
    return jsonify(posts)

@bp.route('/<int:id>', methods=['DELETE'])
def deletePost(id):
    global posts
    for index,post in enumerate(posts):
        if post.get('id') == id:
            del posts[index]
    posts = db.setDb(posts)
    
    return jsonify(posts)

def configure(app):
    app.register_blueprint(bp)