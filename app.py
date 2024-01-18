from flask import Flask, request
from like_db import LikeDB
app = Flask(__name__)
likeDB = LikeDB('like_db.json')

@app.route("/")
def home():
    return "Hello World!"


@app.route("/api/addImage", methods=["POST"])
def addImage():
    # Get the image from the request
    if request.method == "POST":
        # Get json data from request
        data = request.get_json(force=True)
        # Get the image id from data
        image_id = data["image_id"]
        # Get the message id from data
        message_id = data["message_id"]
        url = data["url"]
        likeDB.add_image(image_id, message_id, url)
        print(f'Image id: {image_id} Message id: {message_id}')

    return {}

@app.route("/api/addUsers",methods=['POST'])
def addUsers():
    if request.method=="POST":
        data = request.get_json(force=True)
        users_id = data['users_id']
        image_id = data["image_id"]
        likeDB.add_user(users_id,image_id)
    return {}



@app.route("/api/LikesDislike",methods=['POST'])
def likes_dislike():
    if request.method=="POST":
        data = request.get_json(force=True)
        image_id = data["image_id"]
        likeDB.get_likes_dislike(image_id)
    return {}

@app.route("/api/Dislikes",methods=["POST"])
def dislike():
    if request.method=="POST":

        data = request.get_json(force=True)
        user_id = data['user_id']
        image_id = data['image_id']
        likeDB.add_dislike(user_id,image_id,)
    return {}

@app.route("/api/addLike",methods=['POST'])
def addlike():
    if request.method=="POST":

        data = request.get_json(force=True)
        user_id=data["user_id"]
        image_id=data["image_id"]
        likeDB.add_like(user_id,image_id)

    return {}


@app.route("/api/Dislike",methods=['POST'])
def dislikes():
    return likeDB.all_dislikes(False)


@app.route("/app/Likes")
def likes():
    return likeDB.all_likes(True)

if __name__ == "__main__":
    app.run(debug=True,port=9000)