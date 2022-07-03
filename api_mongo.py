from flask import Flask, jsonify, make_response, request, jsonify
from flask_mongoengine import MongoEngine
import uuid

app = Flask(__name__)

db_name = 'videoInfo'
db_URI = "mongodb+srv://admin:admin@cluster0.dcnym1g.mongodb.net/videoInfo?retryWrites=true&w=majority"

app.config["MONGODB_HOST"] = db_URI

db = MongoEngine()
db.init_app(app)

class Info(db.Document):
    unique_id = db.StringField()
    title = db.StringField()
    keyword = db.StringField()
    URL = db.StringField()
    category = db.StringField()

    def to_json(self):
        return {
            "unique_id" : self.unique_id,
            "category" : self.category,
            "title" : self.title,
            "keyword" : self.keyword,
            "URL" : self.URL
        }

@app.route('/')
def index():
    return "Hola"


@app.route('/api/db_populate', methods=['POST'])
def db_populate():
    video1 = Info(unique_id = ((uuid.uuid4()).hex),category = "Database", title = "REST API with pymongo", keyword = "pymongo", URL = "1234")
    video2 = Info(unique_id = ((uuid.uuid4()).hex),category = "JSON", title = "Access JSON file with python", keyword = "JSON", URL = "5678")
    video3 = Info(unique_id = ((uuid.uuid4()).hex),category = "Gaming", title = "valorant", keyword = "Gameplay", URL = "https://vimeo.com/726468840")
    video1.save()
    video2.save()
    video3.save()

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