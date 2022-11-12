from flask import Blueprint, request, jsonify
import json

bp = Blueprint("posts", __name__, url_prefix="/posts")

with open("db/posts.json", encoding='utf-8') as file:
    posts = json.load(file)
    print(posts)


def saveJson(posts):
    json_posts = json.dumps(posts)
    with open('db/posts.json','w') as file:
        file.write(json_posts)
 
@bp.route('/',methods=['GET'])
def getPosts():
    return jsonify(posts) 

@bp.route('/<int:id>', methods=['GET'])
def getPostsByID(id):
    for post in posts:
        if post.get('id') == id:
            return jsonify(post)
        
        
@bp.route('/<int:id>', methods=['PUT'])
def editPost(id):
    new_post = request.get_json()
    for  index, post in enumerate(posts):
        if post.get('id') == id:
            posts[index].update(new_post)
            saveJson()
            return jsonify(posts[index])

@bp.route('/', methods=['POST'])
def createNewPost(posts):
    post = request.get_json()
    posts.append(post)
    saveJson(posts)
    
    return jsonify(posts)

@bp.route('/', methods=['DELETE'])
def deletePost(id):
    for index,post in enumerate(posts):
        if post.get('id') == id:
            del posts[index]
    saveJson(posts)
    
    return jsonify(posts)

def configure(app):
    app.register_blueprint(bp)