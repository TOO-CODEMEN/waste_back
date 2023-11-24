import os
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from model.core import RoboflowRequest
from werkzeug.utils import secure_filename

basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = {'mp4', 'mpeg', 'png', 'jpg'}

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'uploads')

def allowed_file(filename):
    """ Функция проверки расширения файла """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class MlVideo(Resource):
    """ Класс наследуемый от класса Resource flask_restful

        post - Метод срабатывающий при post запросе url/video, обработка файла.
    """
    def post(self):
        try:
            print(request.files.get('file'))
            if 'file' not in request.files:
                return {'data': 'Не могу прочитать файл'}
            file = request.files['file']
            if file and allowed_file(file.filename):
                file.save(f'model/{secure_filename(file.filename)}')
                return RoboflowRequest.get_info(secure_filename(file.filename))
        except Exception as es:
            return {'data': f'{es}'}

api.add_resource(MlVideo, '/file')