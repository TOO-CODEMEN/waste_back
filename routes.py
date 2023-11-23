from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class MlVideo(Resource):
    def post(self):
        pass

api.add_resource(MlVideo, '/video')