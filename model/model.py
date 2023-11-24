# здесь будет моделька
from roboflow import Roboflow
from settings import MlSettings

api = MlSettings().api_key.get_secret_value()

rf = Roboflow(api_key=api)
project = rf.workspace().project("waste-detect-rb23i")
model = project.version(3).model

# infer on a local image
print(model.predict("photo.png", confidence=40, overlap=30).json())
