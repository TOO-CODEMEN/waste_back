import os
from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from werkzeug.utils import secure_filename

# папка для сохранения загруженных файлов
UPLOAD_FOLDER = '/uploads'
# расширения файлов, которые разрешено загружать
ALLOWED_EXTENSIONS = {'mp4', 'mpeg'}

app = Flask(__name__)
CORS(app)
api = Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    """ Функция проверки расширения файла """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class MlVideo(Resource):
    """ Класс наследуемый от класса Resource flask_restful

        post - Метод срабатывающий при post запросе url/video, обработка файла.
    """
    def post(self):
            file = request.files['file']
            if 'file' not in request.files or file.filename == '':
                return {'data': 'Не могу прочитать файл'}
            if file and allowed_file(file.filename):
                # безопасно извлекаем оригинальное имя файла
                filename = secure_filename(file.filename)
                # сохраняем файл
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                # Не до конца сделано, здесь нужно отдать то, что определит ML модель
                return {'data': 'answer'}

api.add_resource(MlVideo, '/video')