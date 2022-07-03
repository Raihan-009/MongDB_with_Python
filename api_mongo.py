from flask import Flask, jsonify, make_response, request, jsonify
from flask_mongoengine import MongoEngine

app = Flask(__name__)

db_name = 'videoInfo'
db_URI = "mongodb+srv://admin:admin@cluster0.dcnym1g.mongodb.net/videoInfo?retryWrites=true&w=majority"
app.config["MONGODB_HOST"] = db_URI

db = MongoEngine()
db.init_app(app)

class Info(db.Document):
    video_id = db.IntField()
    video_title = db.StringField()
    video_keyword = db.StringField()

    def to_json(self):
        return {
            "video_id" : self.video_id,
            "video_title" : self.video_title,
            "video_keyword" : self.video_keyword
        }

@app.route('/')
def index():
    return "Hola"


@app.route('/api/db_populate', methods=['POST'])
def db_populate():
    video1 = Info(video_id = 1, video_title = "REST API with pymongo", video_keyword = "pymongo")
    video2 = Info(video_id = 2, video_title = "Access JSON file with python", video_keyword = "JSON")
    video1.save()
    video2.save()

    return make_response("",201)

@app.route('/api/videos', methods=['GET','POST'])
def api_all_videos():
    if request.method == "GET":
        videos =[]
        for video in Info.objects:
            videos.append(video)
        return make_response(jsonify(videos),200)
    elif request.method == "POST":
        pass

@app.route('/api/videos/<video_id>', methods=['GET', 'PUT', 'DELETE'])
def api_each_video(video_id):
    if request.method == "GET":
        pass
    elif request.method == "PUT":
        pass
    elif request.method == "DELET":
        pass

if __name__ == "__main__":
    app.run(debug=True)