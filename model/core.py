# здесь будет моделька
import os
from roboflow import Roboflow
from settings import MlSettings
class RoboflowRequest():
    @staticmethod
    def get_info(image: str):
        api = MlSettings().api_key.get_secret_value()
        rf = Roboflow(api_key=api)
        project = rf.workspace().project("waste-detect-rb23i")
        model = project.version(3).model
        info = model.predict(f'model/{image}', confidence=40, overlap=30).json()
        os.remove(f'model/{image}')
        return info

if __name__ == '__main__':
    RoboflowRequest()